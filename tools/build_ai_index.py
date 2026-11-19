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


def build_shards():
    shards = {}
    summary = {}
    total = 0
    for folder, slug, label in SUBJECTS:
        root = VAULT / folder
        chunks = []
        cid = 0
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
                for sec, content in split_sections(body, title):
                    for part in split_paragraphs(content):
                        if len(part) < MIN_CHUNK_CHARS:
                            continue
                        cid += 1
                        chunks.append({
                            "i": cid,
                            "u": unit,
                            "k": kind[0],          # 't' theory | 'p' problem | 'f' formula
                            "t": title[:110],
                            "h": sec[:110],
                            "x": part,
                        })
        shards[slug] = {
            "v": 1,
            "subject": slug,
            "label": label,
            "count": len(chunks),
            "chunks": chunks,
        }
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
