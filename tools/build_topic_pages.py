#!/usr/bin/env python3
"""Build topic theory pages in subjects/ from their vault notes (Obsidian first, web second).

Each page configured in tools/topic_pages.json is generated from one vault note:
    - the YAML frontmatter is dropped; the first blockquote is the "central idea" callout;
    - "# Part ..." headings become part dividers, "## N. Title" sections, "###"/"####" sub-headings;
    - Markdown paragraphs, lists, tables, $$ display math (one line), Obsidian callouts
      (> [!info] / [!note] / [!warning]) and inline **bold**, `code` and $math$ are converted;
    - figure embeds ![[attachments/<folder>/<name>.svg]] are inlined from the topic's figure module
      in tools/figures/ (which also writes the vault copy of each SVG); ![[attachments/<folder>/<name>.png]]
      embeds a figure copied from the slides, registered with its caption in the same module;
    - an optional "questions" list renders problem notes (statement, answer, interpretation) as cards
      in the section whose title starts with "Questions";
    - an optional "problems" {href, label} adds a closing link to the topic's problems page.
Flavor "mechanics" (Engineering Mechanics; "template" = a sibling hand-written theory page) renders the callout
`> [!derivation] Title` with tools/derivation.py (syntax errors and the no-inline-calc gate fail the build and
`--check`); a callout titled "Extension..." gets a dashed accent border, `[!example]` an example card.
The page keeps its own <head>, site header and footer (or those of "template", when given), and
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
import derivation  # noqa: E402

CONFIG = TOOLS / "topic_pages.json"


class NoteError(Exception):
    """A note that breaks a rule of its flavor (derivation box syntax, no-inline-calc gate); `.messages` lists them."""

    def __init__(self, messages):
        super().__init__("; ".join(messages))
        self.messages = list(messages)


_DERIVATION_ERRORS = []


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
    t = re.sub(r"https?://[^\s<)]*[^\s<).,;]", lambda m: f'<a href="{m.group(0)}" target="_blank" rel="noopener">{m.group(0)}</a>', t)
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
    open_, close = STYLE["table"]
    return f'{open_}<thead><tr>{th}</tr></thead><tbody>{trs}</tbody>{close}'


_CALLOUT = {"info": "callout", "note": "callout", "tip": "callout", "warning": "callout callout-warning"}
_FLUIDS_CALLOUT = {"info": "callout-box", "note": "callout-box", "tip": "callout-box",
                   "warning": "callout-box callout-warning"}
_TABLE = ('<div class="table-container"><table class="data-table">', "</table></div>")
_FLUIDS_TABLE = ('<div class="table-wrapper"><table class="fm-table">', "</table></div>")
STYLE = {"callout": _CALLOUT, "table": _TABLE}
_BLOCK_START = re.compile(r"(\$\$|\||> |\s*[-*] |\d+\. |#|!\[\[)")


_LI = re.compile(r"^(\s*)([-*]|\d+\.) (.*)$")


def list_html(rows):
    """Nested <ul>/<ol> from (indent, kind, text) rows: deeper indentation nests inside the item above."""
    def build(idx, indent):
        tag, items = rows[idx][1], []
        while idx < len(rows) and rows[idx][0] >= indent:
            ind, kind, text = rows[idx]
            if ind > indent and items:
                child, idx = build(idx, ind)
                items[-1] += child
                continue
            if kind != tag:
                break
            items.append(f"<li>{inline(text)}")
            idx += 1
        return f"<{tag}>" + "".join(x + "</li>" for x in items) + f"</{tag}>", idx

    out, idx = [], 0
    while idx < len(rows):
        html_list, idx = build(idx, rows[idx][0])
        out.append(html_list)
    return "".join(out)


def blocks(lines, figure=None):
    """Convert Markdown lines (no section headings) to HTML; `figure(name)` renders an SVG embed."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s or s == "---":
            i += 1
            continue
        m = re.match(r"!\[\[attachments/[^\]/]+/([\w-]+)\.(?:svg|png)\]\]$", s)
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
        if derivation.is_start(line):
            block, i = derivation.take(lines, i)
            box, errs = derivation.parse(block)
            _DERIVATION_ERRORS.extend(errs)

            def box_figure(ref, _fig=figure):
                try:
                    if _fig is None:
                        raise ValueError("the page has no figure module")
                    return _fig(pathlib.PurePosixPath(ref[1]).stem)
                except (KeyError, ValueError) as err:
                    _DERIVATION_ERRORS.append(f"box '{box['title']}': figure embed {ref[1]}: {err}")
                    return ""

            out.append(derivation.render(box, inline, box_figure))
            continue
        if line.startswith("> [!"):
            kind, title = re.match(r"> \[!(\w+)\]\s*(.*)", line).groups()
            inner = []
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                inner.append(lines[i][2:] if lines[i].startswith("> ") else lines[i][1:])
                i += 1
            if STYLE.get("callout_fn"):
                out.append(STYLE["callout_fn"](kind.lower(), title, blocks(inner, figure)))
                continue
            cls = STYLE["callout"].get(kind.lower(), "callout")
            out.append(f'<div class="{cls}"><div class="callout-title">{inline(title)}</div>{blocks(inner, figure)}</div>')
            continue
        if _LI.match(line):
            rows = []
            while i < len(lines) and (_LI.match(lines[i]) or (rows and re.match(r"\s{2,}\S", lines[i]))):
                m = _LI.match(lines[i])
                if m:
                    rows.append([len(m.group(1)), "ol" if m.group(2)[0].isdigit() else "ul", m.group(3)])
                else:
                    rows[-1][2] += " " + lines[i].strip()
                i += 1
            out.append(list_html(rows))
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
    def __init__(self, module, css_class="diagram-card"):
        self.reg = importlib.import_module(f"figures.{module}").build() if module else None
        self.count = 0
        self.css_class = css_class

    def __call__(self, name):
        if self.reg is None or name not in self.reg.web:
            raise KeyError(f"unknown figure '{name}'")
        self.count += 1
        cap = html.escape(html.unescape(self.reg.captions[name]))
        return (f'<div class="{self.css_class}">\n{self.reg.web[name]}\n'
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


FLUIDS_CSS = """
    :root { --text-heading: var(--text-primary); --text-faint: var(--text-muted); }
    .table-wrapper { overflow-x: auto; margin: 20px 0; border: 1px solid var(--border-card); border-radius: 10px; background: var(--bg-card); }
    table.fm-table { border-collapse: collapse; width: 100%; font-size: 0.93rem; }
    .fm-table th, .fm-table td { padding: 10px 14px; text-align: left; vertical-align: top; border-bottom: 1px solid var(--border-subtle); }
    .fm-table th { font-family: var(--font-sans); font-size: 0.78rem; letter-spacing: 0.04em; text-transform: uppercase; color: var(--text-muted); }
    .fm-table tr:last-child td { border-bottom: none; }
    h4.sub-heading { font-family: var(--font-sans); font-size: 1.02rem; font-weight: 700; color: var(--text-primary); margin: 22px 0 8px; }
    article ul, article ol { margin: 8px 0 14px 1.4rem; }
    article li { margin: 4px 0; }
    .callout-box p:last-child, .callout-box .math-block:last-child { margin-bottom: 0; }
    .callout-warning { background: rgba(245, 158, 11, 0.10); border-left-color: #f59e0b; }
    .diagram-card { background: var(--bg-card); border: 1px solid var(--border-card); border-radius: 12px; padding: 16px; margin: 22px 0; }
    .diagram-card svg { max-width: 100%; height: auto; }
    .diagram-caption { font-family: var(--font-sans); font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; text-align: center; }
    section[id] { scroll-margin-top: 80px; }
"""


def nav_html(items):
    """Previous / centre / next buttons of the fluid pages: (href, label, kind) with kind prev, center or next."""
    arrow = {"prev": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                     'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="19" y1="12" x2="5" y2="12"></line>'
                     '<polyline points="12 19 5 12 12 5"></polyline></svg>',
             "next": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                     'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line>'
                     '<polyline points="12 5 19 12 12 19"></polyline></svg>'}
    out = []
    for href, label, kind in items:
        label = html.escape(label, quote=False)
        if kind == "prev":
            out.append(f'<a href="{href}" class="bottom-nav-btn">{arrow["prev"]}<span>{label}</span></a>')
        elif kind == "next":
            out.append(f'<a href="{href}" class="bottom-nav-btn"><span>{label}</span>{arrow["next"]}</a>')
        else:
            out.append(f'<a href="{href}" class="bottom-nav-btn center"><span>{label}</span></a>')
    return '<nav class="bottom-nav">\n        ' + "\n        ".join(out) + "\n      </nav>"


def build_fluids_page(page_rel, spec, cfg_links, anchors):
    """A Fluid Mechanics theory page: the shell (head, header, CSS) of a sibling page, the body from the vault note."""
    global STYLE
    vault = REPO / spec["note"]
    md = strip_frontmatter(vault.read_text(encoding="utf-8"))
    figure = FigureSet(spec.get("figures"))
    shell = sl.strip_links((REPO / spec.get("template", page_rel)).read_text(encoding="utf-8"))
    head = shell[:shell.index('<main class="container">')]
    tail = shell[shell.index("  </main>"):]
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(spec['html_title'], quote=False)}</title>", head, count=1, flags=re.S)
    head = re.sub(r'(<span style="font-size: 13px; color: var\(--text-muted\);">)[^<]*(</span>)',
                  lambda m: m.group(1) + html.escape(spec["brand"], quote=False) + m.group(2), head, count=1)
    head = head.replace("  </style>", FLUIDS_CSS + "  </style>", 1)

    m = re.search(r"^> (.*)$", md, re.M)
    first_section = re.search(r"^## \d+\.", md, re.M)
    intro = md[m.start():first_section.start()].split("\n")
    body = md[first_section.start():md.index("**Back to:**")]
    saved = STYLE
    STYLE = {"callout": _FLUIDS_CALLOUT, "table": _FLUIDS_TABLE}
    try:
        parts = []
        for ch in re.split(r"\n(?=## \d+\.)", body.strip()):
            lines = ch.split("\n")
            num, rest = re.match(r"## (\d+)\.\s+(.*)", lines[0]).groups()
            out, chunk = [], []
            for line in lines[1:]:
                hm = re.match(r"(#{3,4}) (.*)", line)
                if hm:
                    out.append(blocks(chunk, figure))
                    chunk = []
                    tag = "h3" if len(hm.group(1)) == 3 else "h4"
                    out.append(f'<{tag} class="sub-heading">{inline(hm.group(2))}</{tag}>')
                elif line.strip() == "---":
                    continue
                else:
                    chunk.append(line)
            out.append(blocks(chunk, figure))
            parts.append(f'      <section id="section-{num}">\n        <h2 class="section-heading">{num}. {inline(rest)}</h2>\n'
                         + "\n".join(x for x in out if x) + "\n      </section>")
        intro_rest = [x for x in intro[1:] if x.strip() != "---"]
        intro_html = (f'      <section id="section-0">\n        <div class="callout-box"><p>{inline(intro[0][2:])}</p></div>\n'
                      f'{blocks(intro_rest, figure)}\n      </section>')
    finally:
        STYLE = saved
    header = f'''<main class="container">
    <article>
      <header class="article-header">
        <div class="article-category">{html.escape(spec["category"], quote=False)}</div>
        <h1 class="article-title">{html.escape(spec["title"], quote=False)}</h1>
        <p class="article-meta">{html.escape(spec["subtitle"], quote=False)}</p>
      </header>

'''
    nav = nav_html([tuple(x) for x in spec["nav"]])
    page = head + header + intro_html + "\n\n" + "\n\n".join(parts) + f"\n\n      {nav}\n    </article>\n" + tail
    if page_rel in cfg_links["pages"]:
        page = sl.build_page(page_rel, page, cfg_links, anchors, {})
    return page, figure


MECH_CSS = """
    :root { --text-faint: #8a94a6; }
    .callout-extension { border-style: dashed; border-left: 4px solid var(--accent); }
    .example-card h4.example-title { margin: 0; font-size: 1.05rem; color: var(--text-heading); }
    .callout p:last-child, .example-card p:last-child { margin-bottom: 0; }
    .diagram-container.diagram-card { margin: 22px 0; }
    section[id], h2[id], h3[id] { scroll-margin-top: 80px; }
"""
_MECH_TABLE = ('<div class="table-wrapper"><table>', "</table></div>")


def mech_callout(kind, title, inner):
    """Callout of a mechanics note: extension box, warning, worked example or plain information box."""
    t = inline(title)
    if kind == "example":
        return (f'<div class="example-card"><div class="example-header"><h4 class="example-title">{t}</h4>'
                f'<span class="example-badge">Example</span></div>{inner}</div>')
    cls = "callout callout-warning" if kind == "warning" else "callout callout-key" if kind == "key" else "callout callout-info"
    if title.strip().lower().startswith("extension"):
        cls += " callout-extension"
    return f'<div class="{cls}"><div class="callout-title">{t}</div>{inner}</div>'


def slug(text, used):
    base = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>|\$[^$]*\$", "", text.lower())).strip("-")[:48] or "part"
    name, k = base, 2
    while name in used:
        name, k = f"{base}-{k}", k + 1
    used.add(name)
    return name


_MECH_NAV = {"prev": ("← Previous Topic", ""),
             "center": ("Practice Problems", ' style="text-align: center; border-color: var(--accent-border);"'),
             "next": ("Next Topic →", ' style="text-align: right;"')}


def mech_nav(items):
    out = []
    for href, label, kind in items:
        cap, style = _MECH_NAV[kind]
        if kind == "next" and href.startswith("index.html"):
            cap = "Back to Syllabus →"
        title = html.escape(label, quote=False)
        color = ' style="color: var(--accent);"' if kind == "center" else ""
        out.append(f'      <a href="{href}" class="nav-btn"{style}>\n        <span class="nav-btn-label">{cap}</span>\n'
                   f'        <span class="nav-btn-title"{color}>{title}</span>\n      </a>')
    return '    <div class="article-nav">\n' + "\n".join(out) + "\n    </div>"


QUOTE_TAIL = """    <!-- Aerospace Motivational Quote Component -->
    <section class="container" style="max-width: 920px; margin: 48px auto 24px; padding: 0 24px;">
      <div id="quoteContainer"></div>
    </section>
"""


def build_mechanics_page(page_rel, spec, cfg_links, anchors):
    """An Engineering Mechanics theory page: shell of a sibling page, body from the vault note, derivation boxes and gate."""
    global STYLE
    vault = REPO / spec["note"]
    md = strip_frontmatter(vault.read_text(encoding="utf-8"))
    figure = FigureSet(spec.get("figures"), "diagram-container diagram-card")
    shell = sl.strip_links((REPO / spec.get("template", page_rel)).read_text(encoding="utf-8"))
    head = shell[:shell.index('<main class="article-container">')]
    tail = shell[shell.index("  </main>"):]
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(spec['html_title'], quote=False)}</title>", head, count=1, flags=re.S)
    head = head.replace("  </style>", MECH_CSS + "  </style>", 1)
    head = re.sub(r'\n[ \t]*<link rel="stylesheet" href="[^"]*assets/css/derivation-box\.css">', "", head)
    resp = re.search(r'\n([ \t]*)<link\b[^>]*assets/css/responsive\.css[^>]*>', head)
    if not resp:
        raise NoteError([f"the template of {page_rel} has no responsive.css link"])
    head = (head[:resp.start()] + f'\n{resp.group(1)}<link rel="stylesheet" href="../../../assets/css/derivation-box.css">'
            + head[resp.start():])

    end = md.find("**Back to:**")
    md = md[:end] if end >= 0 else md
    idea = re.search(r"^> (?!\[!).*(?:\n> (?!\[!).*)*", md, re.M)
    first_section = re.search(r"^## \d+\.", md, re.M)
    if not idea or not first_section:
        raise NoteError(["the note needs a first blockquote (central idea) and '## N. Title' sections"])
    idea_text = " ".join(x[2:].strip() for x in idea.group(0).split("\n"))
    intro_rest = [x for x in md[idea.end():first_section.start()].split("\n") if x.strip() != "---"]

    saved = STYLE
    STYLE = {"callout": _CALLOUT, "table": _MECH_TABLE, "callout_fn": mech_callout}
    _DERIVATION_ERRORS.clear()
    try:
        parts, toc, used = [], [], set()
        for ch in re.split(r"\n(?=## \d+\.)", md[first_section.start():].strip()):
            lines = ch.split("\n")
            num, rest = re.match(r"## (\d+)\.\s+(.*)", lines[0]).groups()
            toc.append((num, rest))
            out, chunk = [], []
            for line in lines[1:]:
                hm = re.match(r"(#{3,4}) (.*)", line)
                if hm:
                    out.append(blocks(chunk, figure))
                    chunk = []
                    if len(hm.group(1)) == 3:
                        out.append(f'<h3 class="sub-heading" id="{slug(hm.group(2), used)}">{inline(hm.group(2))}</h3>')
                    else:
                        out.append(f'<h4 class="minor-heading">{inline(hm.group(2))}</h4>')
                elif line.strip() == "---" or line.startswith("See also [["):
                    continue
                else:
                    chunk.append(line)
            out.append(blocks(chunk, figure))
            parts.append(f'    <section>\n      <h2 class="section-heading" id="sec-{num}"><span>{num}.</span> {inline(rest)}</h2>\n'
                         + "\n".join(x for x in out if x) + "\n    </section>")
        extra = blocks(intro_rest, figure)
    finally:
        STYLE = saved
    idea_html = (f'    <div class="callout callout-key">\n      <div class="callout-title">Central idea of the topic</div>\n'
                 f'      <p>{inline(idea_text)}</p>\n    </div>')
    if extra.strip():
        idea_html += "\n" + extra
    body = idea_html + "\n\n" + "\n\n".join(parts)

    messages = list(_DERIVATION_ERRORS) + derivation.gate(body)
    if messages:
        raise NoteError(messages)

    toc_html = "\n".join(f'        <a href="#sec-{n}" class="toc-item"><span>{n}.</span> {inline(t)}</a>' for n, t in toc)
    source = f'      <div class="source-box">\n        {inline(spec["source"])}\n      </div>\n' if spec.get("source") else ""
    header = f'''<main class="article-container">
    <header class="article-header">
      <div class="article-category">{html.escape(spec["category"], quote=False)}</div>
      <h1 class="article-title">{html.escape(spec["title"], quote=False)}</h1>
      <div class="article-meta">
        {html.escape(spec["subtitle"], quote=False)}
      </div>
{source}    </header>

    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title"><span>Topic Outline</span></div>
      <div class="toc-grid">
{toc_html}
      </div>
    </nav>

'''
    nav = mech_nav([tuple(x) for x in spec["nav"]])
    page = head + header + body + f"\n\n{nav}\n\n{QUOTE_TAIL}" + tail
    if page_rel in cfg_links["pages"]:
        page = sl.build_page(page_rel, page, cfg_links, anchors, {})
    return page, figure


def build_page(page_rel, spec, cfg_links, anchors):
    if spec.get("flavor") == "mechanics":
        return build_mechanics_page(page_rel, spec, cfg_links, anchors)
    _DERIVATION_ERRORS.clear()
    result = _build_page(page_rel, spec, cfg_links, anchors)
    if _DERIVATION_ERRORS:
        raise NoteError(list(_DERIVATION_ERRORS))
    return result


def _build_page(page_rel, spec, cfg_links, anchors):
    if spec.get("flavor") == "fluids":
        return build_fluids_page(page_rel, spec, cfg_links, anchors)
    vault = REPO / spec["note"]
    md = strip_frontmatter(vault.read_text(encoding="utf-8"))
    figure = FigureSet(spec.get("figures"))
    shell_src = REPO / spec.get("template", page_rel)
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
    if "problems" in spec:
        pr = spec["problems"]
        parts.append(f'''    <section id="problems-link">
      <div class="callout"><p><a class="end-btn" href="{html.escape(pr["href"])}">{html.escape(pr["label"], quote=False)} →</a></p></div>
    </section>''')
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
    stale, failed = [], False
    for page_rel in targets:
        page_rel = pathlib.PurePosixPath(page_rel).as_posix()
        spec = cfg["pages"][page_rel]
        try:
            page, figs = build_page(page_rel, spec, cfg_links, anchors)
        except NoteError as err:
            for msg in err.messages:
                print(f"build_topic_pages: {pathlib.Path(spec['note']).name}: {msg}", file=sys.stderr)
            failed = True
            continue
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
        return 1 if stale or failed else 0
    print(f"build_topic_pages: {len(targets)} page(s) checked")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
