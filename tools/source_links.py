#!/usr/bin/env python3
"""Add deep links from the study pages to the official PDFs in sources/.

Three kinds of link are inserted, all marked with the attribute `data-srclink`
so a re-run removes and rebuilds them (the tool is idempotent and never touches
any other link on the page):

    panel   an "Official material" strip at the end of the page header, one chip
            per source PDF, opening at the first page the topic uses
    card    an "Original statement" link inside every problem card, opening the
            problem sheet at the page where the statement starts
    cite    inline citations such as "[Slide 14]", "Notes.pdf, Eq. 2.26",
            "Robinson, Sec. 7.6, p. 54" or "[Session 4 Slide 22]" become links to
            that page of the cited PDF; text inside $...$ / $$...$$ is never touched

Configuration lives in tools/source_links.json (PDFs, per-page panels, card
pages and citation rules). Citation targets that need the PDF text (equation,
section, figure labels) are resolved once into tools/source_anchors.json with
`--refresh-anchors`, which needs poppler's `pdftotext`; applying the links is
pure stdlib.

Usage:
    python tools/source_links.py                    # apply to every configured page
    python tools/source_links.py --check            # exit 1 if any page is stale
    python tools/source_links.py --refresh-anchors  # re-resolve labels from the PDFs
    python tools/source_links.py -v                 # also list unresolved citations
"""
import argparse
import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
from urllib.parse import quote

REPO = pathlib.Path(__file__).resolve().parent.parent
CONFIG = REPO / "tools" / "source_links.json"
ANCHORS = REPO / "tools" / "source_anchors.json"
CSS_HREF = "assets/css/source-links.css"

# --------------------------------------------------------------------------- removal
_RM_CITE = re.compile(r'<a class="src-cite" data-srclink\b[^>]*>(.*?)</a>', re.S)


def strip_links(text):
    """Remove everything a previous run inserted, restoring the original page."""
    text = _RM_CITE.sub(r"\1", text)
    text = re.sub(r'\n?[ \t]*<link\b[^>]*\bdata-srclink\b[^>]*>', "", text)
    text = re.sub(r'\n?[ \t]*<nav\b[^>]*\bdata-srclink\b[^>]*>.*?</nav>', "", text, flags=re.S)
    text = re.sub(r'\n?[ \t]*<a class="src-link" data-srclink\b[^>]*>.*?</a>', "", text, flags=re.S)
    return text


# --------------------------------------------------------------------------- hrefs
def pdf_href(page_rel, pdf_path, page):
    rel = os.path.relpath(REPO / pdf_path, (REPO / page_rel).parent).replace(os.sep, "/")
    href = "/".join(quote(seg, safe="") if seg != ".." else seg for seg in rel.split("/"))
    return f"{href}#page={page}" if page and page > 1 else href


def _attr(value):
    return html.escape(value, quote=True)


# --------------------------------------------------------------------------- citations
_NUM = r"(?:\(\d+(?:\.\d+)*[a-z]?\)|\d+(?:\.\d+)*[a-z]?)"
_RANGE = rf"{_NUM}(?:\s*(?:[–-]|&ndash;|to)\s*{_NUM})?"
_KIND = {
    "sec": "sec", "secs": "sec", "section": "sec", "sections": "sec", "§": "sec",
    "ch": "chap", "chapter": "chap", "chapters": "chap",
    "p": "page", "pp": "page",
    "eq": "eq", "eqs": "eq", "equation": "eq", "equations": "eq",
    "fig": "fig", "figs": "fig", "figure": "fig",
    "example": "example", "theorem": "thm", "definition": "def",
    "slide": "slide", "slides": "slide",
}
_KEYWORD = r"(Secs?\.|Sections?|Ch\.|Chapters?|pp?\.|Eqs?\.|Equations?|Figs?\.|Figure|Example|Theorem|Definition|Slides?)"
_ITEM = re.compile(rf"(\s*(?:[,;:]|\(|\band\b|&amp;|&)?\s*(?:\band\b\s*|&amp;\s*)?){_KEYWORD}\s*((?:{_RANGE})(?:\s*(?:,|&amp;|\band\b)\s*(?!{_KEYWORD}){_RANGE})*)")
_NUMTOKEN = re.compile(_RANGE)
_TRIGGER = re.compile(r"\b(Robinson(?:\s*\(2004\))?|Notes(?:\.pdf)?|Session\s+(\d+))(?=[\s,;:.)])")
_BARE_SLIDE = re.compile(rf"\bSlides?\s+(?={_NUM})")
_BARE_EQ = re.compile(rf"\bEqs?\.\s*(?={_NUM})")
_EQ_OF_NOTES = re.compile(rf"\b(Eqs?\.\s*)({_RANGE})(\s+(?:of|in)\s+Notes(?:\.pdf)?)")
_MATH = re.compile(r"\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\\(.*?\\\)|\\\[.*?\\\]", re.S)


def _first_label(token):
    m = re.search(r"\d+(?:\.\d+)*[a-z]?", token)
    return m.group(0) if m else None


class Linker:
    def __init__(self, page_rel, rules, pdfs, anchors):
        self.page_rel = page_rel
        self.rules = rules
        self.pdfs = pdfs
        self.anchors = anchors
        self.unresolved = []
        self.count = 0

    # ---- target resolution
    def target(self, pdf_id, kind, label):
        pdf = self.pdfs.get(pdf_id)
        if not pdf or not label:
            return None
        if kind == "slide":
            n = int(label.split(".")[0])
            return n if 1 <= n <= pdf.get("pages", 10**6) else None
        if kind == "page":
            n = int(label.split(".")[0]) + pdf.get("offset", 0)
            return n if 1 <= n <= pdf.get("pages", 10**6) else None
        return self.anchors.get(pdf_id, {}).get(f"{kind}:{label}")

    def link(self, text, pdf_id, kind, label):
        page = self.target(pdf_id, kind, label)
        if page is None:
            self.unresolved.append(f"{pdf_id} {kind}:{label}")
            return text
        self.count += 1
        name = self.pdfs[pdf_id]["label"]
        href = pdf_href(self.page_rel, self.pdfs[pdf_id]["path"], page)
        return (f'<a class="src-cite" data-srclink href="{_attr(href)}" target="_blank" rel="noopener" '
                f'title="{_attr(f"Open {name} at page {page}")}">{text}</a>')

    def link_numbers(self, numlist, pdf_id, kind):
        out, last = [], 0
        for m in _NUMTOKEN.finditer(numlist):
            out.append(numlist[last:m.start()])
            out.append(self.link(m.group(0), pdf_id, kind, _first_label(m.group(0))))
            last = m.end()
        out.append(numlist[last:])
        return "".join(out)

    # ---- chains after a trigger word
    def chain(self, seg, pos, pdf_for):
        """Link the keyword items that follow position `pos`; return (html, new_pos)."""
        out = []
        while True:
            m = _ITEM.match(seg, pos)
            if not m:
                break
            kind = _KIND[m.group(2).lower().rstrip(".")]
            pdf_id = pdf_for(kind)
            out.append(m.group(1) + m.group(2))
            out.append(seg[m.end(2):m.start(3)])
            out.append(self.link_numbers(m.group(3), pdf_id, kind) if pdf_id else m.group(3))
            pos = m.end()
            tail = re.match(r"\s*\)", seg[pos:])
            if tail and "(" in m.group(1):
                out.append(tail.group(0))
                pos += tail.end()
        return "".join(out), pos

    def slide_pdf(self, pos_in_page):
        spec = self.rules.get("slides")
        if spec is None:
            return None
        if isinstance(spec, str):
            return spec
        current = None
        for pdf_id, start in spec:
            if start <= pos_in_page:
                current = pdf_id
        return current

    def process_text(self, seg, pos_in_page):
        rules = self.rules
        out, i, n = [], 0, len(seg)
        while i < n:
            candidates = []
            for rx, kind in ((_EQ_OF_NOTES, "eqof"), (_TRIGGER, "trigger"), (_BARE_SLIDE, "slide"), (_BARE_EQ, "eq")):
                m = rx.search(seg, i)
                if m:
                    candidates.append((m.start(), kind, m))
            if not candidates:
                break
            start, kind, m = min(candidates, key=lambda c: (c[0], c[1] != "eqof"))
            out.append(seg[i:start])
            if kind == "eqof" and rules.get("notes"):
                out.append(m.group(1) + self.link_numbers(m.group(2), rules["notes"], "eq") + m.group(3))
                i = m.end()
            elif kind == "trigger":
                word = m.group(1)
                if word.startswith("Robinson"):
                    pdf_for = lambda k, p=rules.get("robinson"): p  # noqa: E731
                elif word.startswith("Notes"):
                    pdf_for = lambda k, p=rules.get("notes"): p  # noqa: E731
                else:
                    sess = rules.get("sessions", {}).get(m.group(2))
                    pdf_for = lambda k, p=sess: p if k == "slide" else None  # noqa: E731
                linked, end = self.chain(seg, m.end(), pdf_for)
                out.append(word + linked)
                i = end if end > m.end() else m.end()
            elif kind == "slide" and self.slide_pdf(pos_in_page):
                linked, end = self.chain(seg, m.start(), lambda k: self.slide_pdf(pos_in_page) if k == "slide" else None)
                if end > m.start():
                    out.append(linked)
                    i = end
                else:
                    out.append(m.group(0))
                    i = m.end()
            elif kind == "eq" and rules.get("bare_eq"):
                linked, end = self.chain(seg, m.start(), lambda k: rules["bare_eq"] if k == "eq" else None)
                if end > m.start():
                    out.append(linked)
                    i = end
                else:
                    out.append(m.group(0))
                    i = m.end()
            else:
                out.append(m.group(0))
                i = m.end()
        out.append(seg[i:])
        return "".join(out)

    def process_node(self, node, pos_in_page):
        """Link a text node, leaving every math span untouched."""
        out, last = [], 0
        for m in _MATH.finditer(node):
            out.append(self.process_text(node[last:m.start()], pos_in_page))
            out.append(m.group(0))
            last = m.end()
        out.append(self.process_text(node[last:], pos_in_page))
        return "".join(out)


_SKIP_TAGS = {"script", "style", "a", "code", "pre", "title", "head", "button", "textarea", "svg", "nav"}
_TOKEN = re.compile(r"(<!--.*?-->|<[^>]+>)", re.S)


def link_citations(text, linker):
    if not linker.rules:
        return text
    body = text.find("<body")
    out, stack, pos = [], [], 0
    for part in _TOKEN.split(text):
        if part.startswith("<"):
            tag = re.match(r"</?\s*([a-zA-Z0-9]+)", part)
            if tag and not part.startswith("<!"):
                name = tag.group(1).lower()
                if part.startswith("</"):
                    if name in stack:
                        while stack and stack.pop() != name:
                            pass
                elif name in _SKIP_TAGS and not part.rstrip().endswith("/>"):
                    stack.append(name)
            out.append(part)
        elif pos < body or stack or not part.strip():
            out.append(part)
        else:
            out.append(linker.process_node(part, pos))
        pos += len(part)
    return "".join(out)


# --------------------------------------------------------------------------- panel and cards
def render_panel(page_rel, entries, pdfs, indent):
    chips = []
    for pdf_id, page, note in entries:
        pdf = pdfs[pdf_id]
        href = pdf_href(page_rel, pdf["path"], page)
        where = f" · p. {page}" if page and page > 1 else ""
        label = html.escape(note or pdf["label"])
        chips.append(f'{indent}  <a href="{_attr(href)}" target="_blank" rel="noopener">{label}{where}</a>')
    return (f'\n{indent}<nav class="src-panel" data-srclink aria-label="Official material">\n'
            f'{indent}  <span class="src-panel-label">Official material</span>\n'
            + "\n".join(chips) + f"\n{indent}</nav>")


_HEADER = re.compile(r'<header class="(?:article-header|page-intro)"[^>]*>.*?(\n([ \t]*))</header>', re.S)


def insert_panel(text, html_block):
    """Put the panel at the end of the page header, or right after the lead paragraph under the <h1>."""
    m = _HEADER.search(text)
    if m:
        at = m.start(1)
    else:
        h1 = re.search(r"</h1>", text)
        if not h1:
            return text
        lead = re.compile(r"</p>").search(text, h1.end(), h1.end() + 2000)
        at = lead.end() if lead else h1.end()
    return text[:at] + html_block + text[at:]


def panel_indent(text):
    m = _HEADER.search(text)
    if m:
        return m.group(2) + "  "
    h1 = re.search(r"\n([ \t]*)<h1", text)
    return h1.group(1) if h1 else "    "


_CARD = re.compile(r'<(article|div|details|section)\b[^>]*class="[^"]*\b(?:problem-card|problem-box)\b[^"]*"[^>]*\bid="([^"]+)"[^>]*>')


def insert_cards(text, page_rel, cards, pdfs, missing):
    matches = list(_CARD.finditer(text))
    seen = set()
    for m in reversed(matches):
        card_id = m.group(2)
        spec = cards.get(card_id)
        if not spec:
            missing.append(card_id)
            continue
        seen.add(card_id)
        pdf_id, page = spec[0], spec[1]
        pdf = pdfs[pdf_id]
        end = matches[matches.index(m) + 1].start() if matches.index(m) + 1 < len(matches) else len(text)
        chunk = text[m.end():end]
        title = re.search(r"</h[1-4]>", chunk)
        at = m.end() + (title.end() if title else 0)
        if m.group(1) == "details":
            summ = re.search(r"</summary>", chunk)
            if summ and (not title or summ.start() >= title.start()):
                at = m.end() + summ.end()
        line_start = text.rfind("\n", 0, m.start()) + 1
        indent = re.match(r"[ \t]*", text[line_start:]).group(0) + "  "
        href = pdf_href(page_rel, pdf["path"], page)
        where = f", p. {page}" if page and page > 1 else ""
        link = (f'\n{indent}<a class="src-link" data-srclink href="{_attr(href)}" target="_blank" rel="noopener">'
                f'Original statement · {html.escape(pdf["label"])}{where}</a>')
        text = text[:at] + link + text[at:]
    return text, sorted(set(cards) - seen)


def insert_css(text, page_rel):
    href = os.path.relpath(REPO / CSS_HREF, (REPO / page_rel).parent).replace(os.sep, "/")
    tag = f'<link rel="stylesheet" href="{href}" data-srclink>'
    m = re.search(r"\n([ \t]*)</head>", text)
    if not m:
        return text
    return text[:m.start()] + f"\n{m.group(1)}  {tag}" + text[m.start():]


# --------------------------------------------------------------------------- page build
def build_page(page_rel, original, cfg, anchors, report):
    spec = cfg["pages"][page_rel]
    pdfs = cfg["pdfs"]
    text = strip_links(original)
    linker = Linker(page_rel, spec.get("cite", {}), pdfs, anchors)
    text = link_citations(text, linker)
    missing = []
    if spec.get("cards"):
        text, absent = insert_cards(text, page_rel, spec["cards"], pdfs, missing)
        if absent:
            print(f"source_links: {page_rel}: configured cards not on the page: {absent}", file=sys.stderr)
    if spec.get("panel"):
        entries = []
        for entry in spec["panel"]:
            pdf_id, page = entry[0], entry[1]
            note = entry[2] if len(entry) > 2 else None
            if page == "auto":
                pages = [int(m) for m in re.findall(
                    re.escape(quote(pathlib.PurePosixPath(pdfs[pdf_id]["path"]).name, safe="")) + r"#page=(\d+)", text)]
                page = min(pages) if pages else 1
            entries.append((pdf_id, page, note))
        text = insert_panel(text, render_panel(page_rel, entries, pdfs, panel_indent(text)))
    text = insert_css(text, page_rel)
    report[page_rel] = {"cites": linker.count, "unresolved": linker.unresolved, "missing_cards": missing}
    return text


def load_json(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- anchors from PDF text
def _pdf_pages(path):
    exe = shutil.which("pdftotext")
    if not exe:
        sys.exit("pdftotext (poppler-utils) is required for --refresh-anchors")
    out = subprocess.run([exe, "-layout", str(path), "-"], capture_output=True, check=True)
    return out.stdout.decode("utf-8", "replace").split("\f")


def _find(pages, start, rx):
    for i in range(max(start - 1, 0), len(pages)):
        if rx.search(pages[i]):
            return i + 1
    return None


def resolve_label(pages, pdf, kind, label):
    start = pdf.get("body_start", 1)
    lab = re.escape(label)
    if kind == "eq":
        return _find(pages, start, re.compile(rf"\({lab}\)"))
    if kind == "sec":
        return _find(pages, start, re.compile(rf"(?m)^\s*{lab}\s+\*?[A-Z]"))
    if kind == "chap":
        if "." in label:
            return None
        return (_find(pages, start, re.compile(rf"(?m)^\s*Chapter\s+{lab}\b"))
                or _find(pages, start, re.compile(rf"(?m)^\s*{lab}\.1\s+[A-Z]")))
    if kind == "fig":
        return _find(pages, start, re.compile(rf"\bFig(?:ure|\.)\s*{lab}\b(?!\.\d)"))
    if kind in ("example", "thm", "def"):
        word = {"example": "Example", "thm": "Theorem", "def": "Definition"}[kind]
        return _find(pages, start, re.compile(rf"\b{word}\s+{lab}\b(?!\.\d)"))
    return None


class _Collect(Linker):
    """A Linker that records every label it is asked for instead of linking it."""

    def __init__(self, *a):
        super().__init__(*a)
        self.wanted = set()

    def target(self, pdf_id, kind, label):
        if kind not in ("slide", "page") and pdf_id and label:
            self.wanted.add((pdf_id, kind, label))
        return super().target(pdf_id, kind, label)


def refresh_anchors(cfg):
    wanted = set()
    for page_rel, spec in cfg["pages"].items():
        text = strip_links((REPO / page_rel).read_text(encoding="utf-8"))
        collector = _Collect(page_rel, spec.get("cite", {}), cfg["pdfs"], {})
        link_citations(text, collector)
        wanted |= collector.wanted
    anchors = {}
    cache = {}
    for pdf_id, kind, label in sorted(wanted):
        pdf = cfg["pdfs"][pdf_id]
        if pdf_id not in cache:
            cache[pdf_id] = _pdf_pages(REPO / pdf["path"])
        page = resolve_label(cache[pdf_id], pdf, kind, label)
        if page:
            anchors.setdefault(pdf_id, {})[f"{kind}:{label}"] = page
    ANCHORS.write_text(json.dumps(anchors, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    total = sum(len(v) for v in anchors.values())
    print(f"source_links: resolved {total} of {len(wanted)} labels into {ANCHORS.relative_to(REPO)}")


# --------------------------------------------------------------------------- main
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if any page is out of date")
    ap.add_argument("--refresh-anchors", action="store_true", help="re-resolve labels from the PDFs (needs pdftotext)")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    cfg = load_json(CONFIG)
    for pdf_id, pdf in cfg["pdfs"].items():
        if not (REPO / pdf["path"]).exists():
            print(f"source_links: missing PDF for '{pdf_id}': {pdf['path']}", file=sys.stderr)
            return 1
    if args.refresh_anchors:
        refresh_anchors(cfg)
    anchors = load_json(ANCHORS, {})

    stale, report, failed = [], {}, False
    for page_rel in cfg["pages"]:
        path = REPO / page_rel
        original = path.read_text(encoding="utf-8")
        new = build_page(page_rel, original, cfg, anchors, report)
        if new != original:
            stale.append(page_rel)
            if not args.check:
                path.write_text(new, encoding="utf-8", newline="\n")
        rep = report[page_rel]
        if rep["missing_cards"]:
            failed = True
            print(f"source_links: {page_rel}: no PDF page configured for cards {rep['missing_cards']}", file=sys.stderr)
        if args.verbose:
            print(f"{page_rel}: {rep['cites']} citations linked, {len(rep['unresolved'])} unresolved")
            for u in sorted(set(rep["unresolved"])):
                print(f"    unresolved {u}")

    if args.check:
        for p in stale:
            print(f"source_links: stale {p} (run python tools/source_links.py)", file=sys.stderr)
        return 1 if stale or failed else 0
    print(f"source_links: {len(stale)} page(s) updated, {len(cfg['pages'])} configured")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
