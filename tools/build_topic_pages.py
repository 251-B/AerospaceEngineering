#!/usr/bin/env python3
"""Build topic theory pages in subjects/ from their vault notes (Obsidian first, web second).

Each page configured in tools/topic_pages.json is generated from one vault note:
    - the YAML frontmatter is dropped; the first blockquote is the "central idea" callout;
    - "# Part ..." headings become part dividers, "## N. Title" sections, "###"/"####" sub-headings;
    - Markdown paragraphs, lists, tables, $$ display math (one line), Obsidian callouts
      (> [!info] / [!note] / [!warning]) and inline **bold**, `code` and $math$ are converted;
    - figure embeds ![[attachments/<folder>/<name>.svg]] are inlined from the topic's figure module
      in tools/figures/ (which also writes the vault copy of each SVG);
    - an optional "questions" list renders problem notes (statement, answer, interpretation) as cards
      in the section whose title starts with "Questions".
The page keeps its own <head>, site header and footer (or those of "template" for a new page), and
the PDF deep links of tools/source_links.py are applied before writing, so the output is the final page.

Usage:
    python tools/build_topic_pages.py                 # write figures and every configured page
    python tools/build_topic_pages.py PAGE [PAGE ...] # only these pages
    python tools/build_topic_pages.py --check         # exit 1 if a page or a figure is stale
"""
import argparse
import html
import importlib
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import source_links as sl  # noqa: E402

CONFIG = TOOLS / "topic_pages.json"


# --------------------------------------------------------------------------- inline and block Markdown
def inline(t):
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
    t = re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)
    maths = []

    def keep(m):
        maths.append(html.escape(m.group(0), quote=False))
        return f"\x00{len(maths) - 1}\x00"

    t = re.sub(r"\$\$.*?\$\$|\$[^$]+\$", keep, t)
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: maths[int(m.group(1))], t)


def table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    head, aligns, data = cells[0], cells[1], cells[2:]
    right = [a.strip().endswith(":") and not a.strip().startswith(":") for a in aligns]
    style = lambda i: ' style="text-align:right"' if i < len(right) and right[i] else ""  # noqa: E731
    th = "".join(f"<th{style(i)}>{inline(c)}</th>" for i, c in enumerate(head))
    trs = "".join("<tr>" + "".join(f"<td{style(i)}>{inline(c)}</td>" for i, c in enumerate(r)) + "</tr>" for r in data)
    return f'<div class="table-container"><table class="data-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


_CALLOUT = {"info": "callout", "note": "callout", "tip": "callout", "warning": "callout callout-warning"}
_BLOCK_START = re.compile(r"(\$\$|\||> |\s*[-*] |\d+\. |#|!\[\[)")


def blocks(lines, figure=None):
    """Convert Markdown lines (no section headings) to HTML; `figure(name)` renders an SVG embed."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s or s == "---":
            i += 1
            continue
        m = re.match(r"!\[\[attachments/[^\]/]+/([\w-]+)\.svg\]\]$", s)
        if m:
            if figure is None:
                raise ValueError(f"figure embed {s} but the page has no figure module")
            out.append(figure(m.group(1)))
            i += 1
            continue
        if line.startswith("$$"):
            out.append(f'<div class="math-block">{html.escape(s, quote=False)}</div>')
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(table(rows))
            continue
        if line.startswith("> [!"):
            kind, title = re.match(r"> \[!(\w+)\]\s*(.*)", line).groups()
            inner = []
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                inner.append(lines[i][2:] if lines[i].startswith("> ") else lines[i][1:])
                i += 1
            cls = _CALLOUT.get(kind.lower(), "callout")
            out.append(f'<div class="{cls}"><div class="callout-title">{inline(title)}</div>{blocks(inner, figure)}</div>')
            continue
        if re.match(r"\s*[-*] ", line):
            items = []
            while i < len(lines) and re.match(r"\s*[-*] |\s{2,}\S", lines[i]):
                if re.match(r"\s*[-*] ", lines[i]):
                    items.append(re.sub(r"^\s*[-*] ", "", lines[i]))
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        if re.match(r"\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"\d+\. ", lines[i]):
                items.append(re.sub(r"^\d+\. ", "", lines[i]))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not _BLOCK_START.match(lines[i]):
            para.append(lines[i])
            i += 1
        out.append(f"<p>{inline(' '.join(x.strip() for x in para))}</p>")
    return "\n".join(out)


# --------------------------------------------------------------------------- page assembly
def strip_frontmatter(md):
    if md.startswith("---"):
        return md.split("---", 2)[2]
    return md


class FigureSet:
    def __init__(self, module):
        self.reg = importlib.import_module(f"figures.{module}").build() if module else None
        self.count = 0

    def __call__(self, name):
        if self.reg is None or name not in self.reg.web:
            raise KeyError(f"unknown figure '{name}'")
        self.count += 1
        cap = html.escape(html.unescape(self.reg.captions[name]))
        return (f'<div class="diagram-card">\n{self.reg.web[name]}\n'
                f'<div class="diagram-caption">Figure {self.count}. {cap}.</div>\n</div>')


def section_html(sec, figure, questions_html):
    lines = sec.split("\n")
    num, rest = re.match(r"## (\d+)\.\s+(.*)", lines[0]).groups()
    out, chunk = [], []
    for line in lines[1:]:
        m = re.match(r"(#{3,4}) (.*)", line)
        if m:
            out.append(blocks(chunk, figure))
            chunk = []
            tag = "h3" if len(m.group(1)) == 3 else "h4"
            out.append(f'<{tag} class="sub-heading">{inline(m.group(2))}</{tag}>')
        elif line.startswith("See also [[") or line.strip() == "---":
            continue
        else:
            chunk.append(re.sub(r" → \[\[Problem - [^\]]+\]\]", "", line))
    out.append(blocks(chunk, figure))
    if rest.startswith("Questions") and questions_html:
        out.append(questions_html())
    inner = "\n".join(x for x in out if x)
    return (f'    <section id="section-{num}">\n      <h2 class="section-heading"><span class="section-num">§ {num}</span> '
            f'{inline(rest)}</h2>\n{inner}\n    </section>')


def question_cards(names, figure, vault):
    cards = []
    for q, name in enumerate(names, 1):
        t = (vault / f"{name}.md").read_text(encoding="utf-8")
        stmt = re.search(r"## 📄 Statement[^\n]*\n> (.*)", t).group(1)
        title = re.search(r"^# ✏️ Problem: [^,]*, (.*)$", t, re.M).group(1)
        ans = t[t.index("## 3. Answer"):t.index("## 4. Interpretation")].split("\n")[1:]
        interp = t[t.index("## 4. Interpretation"):t.index("**Back to:**")].split("\n")[1:]
        cards.append(f'''<div class="exam-card" id="question-{q}">
  <div class="exam-header"><span class="exam-badge">Question {q}</span><span class="exam-title">{inline(title)}</span></div>
  <div class="exam-body">
    <p><em>{inline(stmt)}</em></p>
    <h4 class="sub-heading">Answer</h4>
{blocks(ans, figure)}
    <h4 class="sub-heading">Interpretation</h4>
{blocks(interp, figure)}
  </div>
</div>''')
    return "\n".join(cards)


def build_page(page_rel, spec, cfg_links, anchors):
    vault = REPO / spec["note"]
    md = strip_frontmatter(vault.read_text(encoding="utf-8"))
    figure = FigureSet(spec.get("figures"))
    shell_src = REPO / spec.get("template", page_rel) if not (REPO / page_rel).exists() else REPO / page_rel
    shell = sl.strip_links(shell_src.read_text(encoding="utf-8"))
    head = shell[:shell.index('<main class="article-container">')]
    tail = shell[shell.index("  </main>"):]
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(spec['html_title'], quote=False)}</title>", head, count=1, flags=re.S)

    m = re.search(r"^> (.*)$", md, re.M)
    first_section = re.search(r"^(# Part |## \d+\.)", md, re.M)
    intro = md[m.start():first_section.start()].split("\n")
    body = md[first_section.start():md.index("**Back to:**")]

    questions = spec.get("questions", [])
    qhtml = (lambda: question_cards(questions, figure, vault.parent)) if questions else None
    parts = []
    chunks = re.split(r"\n(?=# Part |## \d+\.)", body.strip())
    for ch in chunks:
        if ch.startswith("# Part "):
            first, _, rest = ch.partition("\n")
            parts.append(f'    <h2 class="part-divider">{inline(first[2:])}</h2>')
            if rest.strip():
                parts.append(blocks(rest.split("\n"), figure))
        else:
            parts.append(section_html(ch, figure, qhtml))

    intro_rest = [x for x in intro[1:] if x.strip() != "---"]
    header = f'''<main class="article-container">

    <header class="article-header">
      <div class="article-category">{html.escape(spec["category"], quote=False)}</div>
      <h1 class="article-title">{html.escape(spec["title"], quote=False)}</h1>
      <p class="article-subtitle">{html.escape(spec["subtitle"], quote=False)}</p>
      <div class="source-box">
        <span>📖 Source: {html.escape(spec["source"], quote=False)}</span>
      </div>
    </header>

    <section id="section-0">
      <div class="callout"><p>{inline(intro[0][2:])}</p></div>
{blocks(intro_rest, figure)}
    </section>
'''
    page = head + header + "\n".join(parts) + "\n\n" + tail
    if page_rel in cfg_links["pages"]:
        page = sl.build_page(page_rel, page, cfg_links, anchors, {})
    return page, figure


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="*")
    ap.add_argument("--check", action="store_true", help="exit 1 if a page or figure is out of date")
    args = ap.parse_args(argv)
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    cfg_links = json.loads(sl.CONFIG.read_text(encoding="utf-8"))
    anchors = sl.load_json(sl.ANCHORS, {})
    targets = args.pages or list(cfg["pages"])
    stale = []
    for page_rel in targets:
        page_rel = pathlib.PurePosixPath(page_rel).as_posix()
        spec = cfg["pages"][page_rel]
        page, figs = build_page(page_rel, spec, cfg_links, anchors)
        if figs.reg is not None:
            if args.check:
                stale += figs.reg.stale(REPO)
            else:
                for rel in figs.reg.write(REPO):
                    print(f"build_topic_pages: wrote {rel}")
        path = REPO / page_rel
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != page:
            stale.append(page_rel)
            if not args.check:
                path.write_text(page, encoding="utf-8", newline="\n")
                print(f"build_topic_pages: wrote {page_rel}")
    if args.check:
        for s in stale:
            print(f"build_topic_pages: stale {s} (run python tools/build_topic_pages.py)", file=sys.stderr)
        return 1 if stale else 0
    print(f"build_topic_pages: {len(targets)} page(s) checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
