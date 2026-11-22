#!/usr/bin/env python3
"""Build per-subject client-side RAG indices under assets/data/ai-index/ from vault/.

Walks the five subject folders under vault/, strips Obsidian syntax while preserving LaTeX
formulas ($...$, $$...$$), splits notes by section into retrieval chunks, and writes one
compact JSON shard per subject plus manifest.json, loaded lazily by assets/js/ai-rag.js.

Laboratory material is strictly excluded (never published on the web).

Usage:
    python tools/build_ai_index.py           # regenerate assets/data/ai-index/*.json
    python tools/build_ai_index.py --check   # exit 1 if any shard or manifest is stale
"""
import argparse
import json
import pathlib
import re
import sys
import unicodedata

REPO = pathlib.Path(__file__).resolve().parents[1]
VAULT = REPO / "vault"
OUT_DIR = REPO / "assets/data/ai-index"

SUBJECTS = (
    ("01 - Fluid Mechanics", "fluid-mechanics", "Fluid Mechanics"),
    ("02 - Aerospace Materials I", "aerospace-materials-1", "Aerospace Materials I"),
    ("03 - Engineering Mechanics", "engineering-mechanics", "Engineering Mechanics"),
    ("04 - Advanced Maths", "advanced-maths", "Advanced Maths"),
    ("05 - Business Management", "business-management", "Business Management"),
)

_LAB_RE = re.compile(r"laborator|(^|[^a-z])labs?([^a-z]|$)", re.I)
_FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
_EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
_WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_CALLOUT_RE = re.compile(r"^>\s*\[![a-zA-Z0-9_-]+\][+-]?\s*", re.M)
_QUOTE_PREFIX_RE = re.compile(r"^>\s?", re.M)
_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.M)
_UNIT_RE = re.compile(r"\b(?:topic|unit|tema|chapter)\s*0*(\d+)\b", re.I)
_PROB_UNIT_RE = re.compile(r"\bT(\d+)\b")

_CARD_RE = re.compile(r'<(?:article|div|details|section)\s+class="(?:problem-card|problem-box)[^"]*"\s+id="([^"]+)"(.{0,2500}?)class="problem-title"[^>]*>(.*?)</', re.S)
_TAG_RE = re.compile(r"<[^>]+>")
_PROBLEM_NOTE_RE = re.compile(r"^Problem - (?:Bank\s+)?([A-Za-z]{0,4}\d+[a-z]?)\s+(.*)$")

MAX_CHUNK_CHARS = 1400
MIN_CHUNK_CHARS = 120


def parse_frontmatter(raw):
    m = _FM_RE.match(raw)
    if not m:
        return {}, raw
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        k, v = line.split(":", 1)
        meta[k.strip().lower()] = v.strip().strip("\"'")
    return meta, raw[m.end():]


def infer_kind(stem, meta):
    low = stem.lower()
    if low.startswith(("problem -", "problem set -", "solution set -", "exam")):
        return "problem"
    if low.startswith("formula sheet"):
        return "formula"
    if low.startswith(("topic ", "concept -")):
        return "theory"
    t = meta.get("type", "").lower()
    if "problem" in t or "exam" in t:
        return "problem"
    if "formula" in t:
        return "formula"
    return "theory"


def infer_unit(stem, meta):
    for key in ("unit", "topic", "tema"):
        val = meta.get(key, "")
        m = re.search(r"(\d+)", val)
        if m:
            return int(m.group(1))
    m = _UNIT_RE.search(stem)
    if m:
        return int(m.group(1))
    m = _PROB_UNIT_RE.search(stem)
    if m:
        return int(m.group(1))
    return 0


def clean_markdown(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _EMBED_RE.sub("", text)
    text = _WIKILINK_RE.sub(lambda m: (m.group(2) or m.group(1)).split("/")[-1], text)
    text = _MD_LINK_RE.sub(r"\1", text)
    text = _CALLOUT_RE.sub("", text)
    text = _QUOTE_PREFIX_RE.sub("", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"^\s*---+\s*$", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def split_paragraphs(text, limit=MAX_CHUNK_CHARS):
    if len(text) <= limit:
        return [text]
    parts = []
    buf = []
    size = 0
    for para in text.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if size and size + len(para) + 2 > limit:
            parts.append("\n\n".join(buf))
            buf = [para]
            size = len(para)
        else:
            buf.append(para)
            size += len(para) + (2 if buf else 0)
    if buf:
        parts.append("\n\n".join(buf))
    out = []
    for p in parts:
        if len(p) <= limit:
            out.append(p)
        else:
            for i in range(0, len(p), limit):
                seg = p[i:i + limit].strip()
                if seg:
                    out.append(seg)
    return out


def split_sections(body, default_title):
    matches = list(_HEADING_RE.finditer(body))
    if not matches:
        cleaned = clean_markdown(body)
        return [(default_title, cleaned)] if len(cleaned) >= MIN_CHUNK_CHARS else []
    sections = []
    if matches[0].start() > 0:
        lead = clean_markdown(body[:matches[0].start()])
        if len(lead) >= MIN_CHUNK_CHARS:
            sections.append((default_title, lead))
    for i, m in enumerate(matches):
        heading = clean_markdown(m.group(2)).strip("# ").strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = clean_markdown(body[m.end():end])
        if len(content) >= MIN_CHUNK_CHARS:
            sections.append((heading or default_title, content))
    return sections


def _norm(text):
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def page_index(slug):
    """Where each vault note is shown on the portal: theory notes from tools/topic_pages.json (or the
    single teoria/topic-N page of their unit), problem notes from the problem card whose id is the
    note's code (FS3 -> #fs3) or whose title is the note's title."""
    theory, by_unit, cards_by_id, cards_by_title = {}, {}, {}, {}
    cfg = REPO / "tools/topic_pages.json"
    if cfg.is_file():
        for page, entry in json.loads(cfg.read_text(encoding="utf-8")).get("pages", {}).items():
            note = entry.get("note", "") if isinstance(entry, dict) else ""
            if page.startswith(f"subjects/{slug}/") and note:
                theory[pathlib.PurePosixPath(note).stem] = page
    base = REPO / "subjects" / slug
    for page in sorted((base / "teoria").glob("topic-*.html")):
        m = re.match(r"topic-0*(\d+)", page.name)
        if m:
            by_unit.setdefault(int(m.group(1)), []).append(page.relative_to(REPO).as_posix())
    for area in ("problemas", "extra-problems"):
        for page in sorted((base / area).glob("*.html")):
            if page.name == "index.html":
                continue
            rel = page.relative_to(REPO).as_posix()
            for cid, _, title in _CARD_RE.findall(page.read_text(encoding="utf-8", errors="replace")):
                t = _norm(_TAG_RE.sub("", title))
                cards_by_id.setdefault(cid.lower(), []).append((t, f"{rel}#{cid}"))
                cards_by_title.setdefault(t, f"{rel}#{cid}")

    def locate(stem, kind, unit):
        if stem in theory:
            return theory[stem]
        if kind == "theory" and stem.lower().startswith("topic ") and len(by_unit.get(unit, [])) == 1:
            return by_unit[unit][0]
        m = _PROBLEM_NOTE_RE.match(stem)
        if not m:
            return ""
        want = _norm(m.group(2))
        if want in cards_by_title:
            return cards_by_title[want]
        # Same code (fs3 -> #fs3) is not enough: bank P12 and official p12 differ. Ask for half the words too.
        words = set(want.split())
        for t, where in cards_by_id.get(m.group(1).lower(), []):
            if words and len(words & set(t.split())) * 2 >= len(words):
                return where
        return ""
    return locate


# ---------------------------------------------------------------- inverted index (same tokens as ai-rag.js)
RAG_JS = REPO / "assets/js/ai-rag.js"
_TOKEN_RE = re.compile(r"\\[a-z]+|[a-z0-9]+(?:_[a-z0-9]+)?")
_LATEX_SKIP = {"text", "left", "right", "frac", "cdot"}


def _stop_words():
    """The stop words are written once, in ai-rag.js (the browser tokenizes the questions)."""
    src = RAG_JS.read_text(encoding="utf-8")
    block = src[src.index("var STOP = Object.create(null);"):src.index(".split(' ').forEach")]
    return set(" ".join(re.findall(r"'([^']*)'", block)).split())


STOP = _stop_words()


def tokenize(text):
    """Python copy of tokenize() in assets/js/ai-rag.js; test_ai_chat compares the two."""
    s = unicodedata.normalize("NFD", str(text or "").lower())
    s = re.sub("[\u0300-\u036f]", "", s)
    out = []
    for tok in _TOKEN_RE.findall(s):
        if tok.startswith("\\"):
            tok = tok[1:]
            if len(tok) >= 2 and tok not in _LATEX_SKIP:
                out.append(tok)
            continue
        if len(tok) < 2 or tok.isdigit() or tok in STOP:
            continue
        out.append(tok)
    return out


def inverted_index(chunks):
    ix, hx, dl = {}, {}, []
    for d, c in enumerate(chunks):
        body = tokenize(c["x"])
        tf = {}
        for t in body:
            tf[t] = tf.get(t, 0) + 1
        for t, n in tf.items():
            ix.setdefault(t, []).extend((d, n))
        for t in dict.fromkeys(tokenize(f"{c['t']} {c['h']}")):
            hx.setdefault(t, []).append(d)
        dl.append(len(body))
    return ix, hx, dl


def build_shards():
    shards = {}
    summary = {}
    total = 0
    for folder, slug, label in SUBJECTS:
        root = VAULT / folder
        chunks = []
        cid = 0
        locate = page_index(slug)
        pages = []   # chunk "g" = 1-based index into this list (0 or missing: no page)
        if root.is_dir():
            for md in sorted(root.rglob("*.md"), key=lambda p: p.relative_to(VAULT).as_posix()):
                rel = md.relative_to(VAULT).as_posix()
                stem = md.stem
                if stem.endswith(" MOC") or stem.lower() == "readme":
                    continue
                if _LAB_RE.search(rel):
                    continue
                raw = md.read_text(encoding="utf-8", errors="replace")
                meta, body = parse_frontmatter(raw)
                kind = infer_kind(stem, meta)
                unit = infer_unit(stem, meta)
                title = meta.get("title") or stem
                page = locate(stem, kind, unit)
                if page and page not in pages:
                    pages.append(page)
                g = pages.index(page) + 1 if page else 0
                for sec, content in split_sections(body, title):
                    for part in split_paragraphs(content):
                        if len(part) < MIN_CHUNK_CHARS:
                            continue
                        cid += 1
                        chunk = {
                            "i": cid,
                            "u": unit,
                            "k": kind[0],          # 't' theory | 'p' problem | 'f' formula
                            "t": title[:110],
                            "h": sec[:110],
                            "x": part,
                        }
                        if g:
                            chunk["g"] = g
                        chunks.append(chunk)
        shards[slug] = {
            "v": 1,
            "subject": slug,
            "label": label,
            "count": len(chunks),
            "pages": pages,
            "chunks": chunks,
        }
        shards[slug]["ix"], shards[slug]["hx"], shards[slug]["dl"] = inverted_index(chunks)
        summary[slug] = {"label": label, "chunks": len(chunks), "file": f"{slug}.json"}
        total += len(chunks)

    manifest = {"v": 1, "total": total, "subjects": summary}
    return manifest, shards


def serialize(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build per-subject RAG indices under assets/data/ai-index/.")
    ap.add_argument("--check", action="store_true", help="Exit 1 if any shard or manifest is missing, stale or orphaned.")
    args = ap.parse_args(argv)

    manifest, shards = build_shards()
    expected = {"manifest.json": serialize(manifest)}
    for slug, shard in shards.items():
        expected[f"{slug}.json"] = serialize(shard)

    if args.check:
        if not OUT_DIR.is_dir():
            print(f"MISSING: {OUT_DIR.relative_to(REPO).as_posix()}", file=sys.stderr)
            return 1
        on_disk = {p.name for p in OUT_DIR.glob("*.json")}
        orphans = sorted(on_disk - set(expected))
        if orphans:
            print(f"ORPHANED shards: {', '.join(orphans)}", file=sys.stderr)
            return 1
        for name, payload in sorted(expected.items()):
            path = OUT_DIR / name
            if not path.is_file() or path.read_text(encoding="utf-8") != payload:
                print(f"STALE: {path.relative_to(REPO).as_posix()} (run python tools/build_ai_index.py)", file=sys.stderr)
                return 1
        print(f"OK: {manifest['total']} chunks across {len(shards)} subject shards.")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUT_DIR.glob("*.json"):
        if old.name not in expected:
            old.unlink()
    total_kb = 0.0
    for name, payload in sorted(expected.items()):
        path = OUT_DIR / name
        path.write_text(payload, encoding="utf-8")
        kb = len(payload.encode("utf-8")) / 1024
        total_kb += kb
        if name != "manifest.json":
            slug = name[:-5]
            print(f"  {slug}: {shards[slug]['count']} chunks ({kb:.1f} KB)")
    print(f"Wrote {OUT_DIR.relative_to(REPO).as_posix()}/: {manifest['total']} chunks ({total_kb:.1f} KB total)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
