"""Build the Advanced Maths problem-sheet pages (Chapter 3 part 2, Chapter 4 parts 1 and 2) from their vault notes.

    python tools/am_problems/build.py            # regenerate every file below
    python tools/am_problems/build.py --check    # exit 1 if a generated file is stale

Source of truth: the notes vault/04 - Advanced Maths/Problem - Ch3-II-P*.md, Ch4-I-P*.md and Ch4-II-P*.md (one per
exercise of the official sheets), first written by scripts/author_am_problems.py with every step computed by SymPy
and verified by scripts/verify_topic3_topic4.py.  The sheets and their pages are described in tools/am_problems/sheets.json,
the phase portraits in tools/am_problems/figures.json (drawn by tools/figures/am_portraits.py).

Generated: subjects/advanced-maths/problemas/topic-3-part-2.html, topic-4-part-1.html, topic-4-part-2.html, the SVG
figures in vault/attachments/AM-PS/, and the entries that list the pages in tools/source_links.json, tools/nav.json,
the problems index and the root index (badges).
"""
import argparse
import html
import json
import pathlib
import re
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent))                  # tools/, for the figures package
sys.path.insert(0, str(HERE))

import mdhtml  # noqa: E402
import source_links as SL  # noqa: E402
from figures import am_portraits  # noqa: E402

VAULT = "vault/04 - Advanced Maths"
FIG_DIR = "attachments/AM-PS"
SHEETS = "tools/am_problems/sheets.json"
FIGS = "tools/am_problems/figures.json"
SOURCE_LINKS = "tools/source_links.json"
NAV = "tools/nav.json"
INDEX = "subjects/advanced-maths/problemas/index.html"
PORTAL = "index.html"
INPUTS = (SOURCE_LINKS, NAV, INDEX, PORTAL)            # edited in place by sync(): read from the repo first
SUBJECT = "subjects/advanced-maths/problemas/"
START, END = "<!-- AM-PS:START -->", "<!-- AM-PS:END -->"


def read_json(root, rel):
    return json.loads((root / rel).read_text(encoding="utf-8"))


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def registry(root=ROOT):
    return am_portraits.build(read_json(root, FIGS))


def figure_html(reg):
    def fig(name, caption):
        if name not in reg.web:
            raise SystemExit(f"figure {name} is not in {FIGS}")
        cap = caption or reg.captions[name]
        return ('<div class="diagram-card"><div class="diagram-scroll">' + reg.web[name] + '</div>'
                f'<div class="diagram-caption">{mdhtml.inline(cap)}</div>'
                f'<a class="diagram-open" href="../../../vault/{FIG_DIR}/{name}.svg" target="_blank" rel="noopener">'
                'Open the figure full size</a></div>')
    return fig


# --------------------------------------------------------------------------- notes
def load_notes(root, sheet):
    out = []
    for path in sorted((root / VAULT).glob(f"Problem - {sheet['code']}-P*.md"),
                       key=lambda p: int(re.search(r"-P(\d+) ", p.name).group(1))):
        fm, title, statement, phases = mdhtml.split_note(path.read_text(encoding="utf-8"))
        out.append({"fm": fm, "title": re.sub(r"^Problem [\w.\-]+: ", "", title), "statement": statement, "phases": phases,
                    "id": fm["id"], "num": int(re.search(r"-P(\d+) ", path.name).group(1)), "path": path.name})
    return out


def card_html(P, fig):
    def section(badge_cls, badge, blocks_md):
        body, cur = [], False
        for b in mdhtml.parse(blocks_md):
            if b[0] == "h" and b[1] == 3:
                if cur:
                    body.append("</div>")
                body.append(f'<div class="sub-case-card"><div class="sub-case-header">{mdhtml.inline(b[2])}</div>')
                cur = True
            else:
                body.append(mdhtml.render([b], fig))
        if cur:
            body.append("</div>")
        return (f'      <div class="phase-section">\n        <div class="phase-badge-title {badge_cls}">{html.escape(badge)}</div>\n'
                + "\n".join(body) + "\n      </div>\n")
    s = [f'    <article class="problem-card" id="{P["id"]}">',
         '      <div class="problem-header">', '        <div class="problem-title-group">',
         f'          <div class="problem-num-badge">Exercise {P["num"]}</div>',
         f'          <h2 class="problem-title">{mdhtml.inline(P["title"])}</h2>', '        </div>',
         f'        <span class="problem-meta-badge">{html.escape(P["fm"].get("pill", "").strip(chr(34)))}</span>', '      </div>', '']
    s.append('      <div class="phase-section">\n        <div class="phase-badge-title phase-1-badge">Statement</div>\n'
             '        <div class="problem-statement-box">' + mdhtml.render(mdhtml.parse(P["statement"]), fig) + "</div>\n      </div>\n")
    for number, heading, md in P["phases"]:
        s.append(section(f"phase-{number}-badge", f"Phase {number}: {heading}", md))
    s.append("    </article>\n")
    return "\n".join(s)


def page_html(sheet, probs, fig):
    head = (HERE / "template_head.html").read_text(encoding="utf-8").replace("{{TITLE}}", html.escape(sheet["title"], quote=False) + " — Advanced Mathematics | UC3M")
    n = len(probs)
    prev, nxt = sheet["prev"], sheet["next"]
    body = f"""<body>
  <div class="ambient-glow" aria-hidden="true"></div>

  <header class="site-header">
    <div class="header-inner">
      <div class="brand-area">
        <a href="../../../index.html" class="back-link">
          <span>←</span>
          <span>Main Portal</span>
        </a>
        <span class="brand-badge">{html.escape(sheet['badge'])} • {n} Solved</span>
      </div>
      <div class="nav-actions">
        <button class="theme-toggle" id="themeToggle" title="Toggle theme (Light / Dark)" aria-label="Toggle theme"></button>
      </div>
    </div>
  </header>

  <main class="article-container">

    <header class="article-header">
      <div class="article-meta-top">
        <span class="topic-pill">{html.escape(sheet['badge'])} • Official Solutions</span>
        <span class="course-tag">Department of Mathematics • UC3M Aerospace Engineering</span>
      </div>
      <h1 class="article-title">{html.escape(sheet['title'], quote=False)}</h1>
      <p class="article-lead">{html.escape(sheet['lead'], quote=False)}</p>
      <div class="source-box">
        <span>Source Document:</span>
        <code>{html.escape(sheet['pdf'])}</code>
      </div>
    </header>

"""
    cards = "\n".join(card_html(P, fig) for P in probs)
    tail = f"""
    <nav class="article-nav" aria-label="Topic Navigation">
      <a href="{prev[0]}" class="nav-btn">
        <span class="nav-btn-label">← Previous Problem Set</span>
        <span class="nav-btn-title">{html.escape(prev[1])}</span>
      </a>
      <a href="{nxt[0]}" class="nav-btn" style="text-align: right;">
        <span class="nav-btn-label">{html.escape(nxt[2])} →</span>
        <span class="nav-btn-title">{html.escape(nxt[1])}</span>
      </a>
    </nav>

    <footer class="site-footer">
      <p>Bachelor in Aerospace Engineering — Universidad Carlos III de Madrid (UC3M)</p>
      <p>Advanced Mathematics • {html.escape(sheet['title'], quote=False)} • Grounded in {html.escape(pathlib.PurePosixPath(sheet['pdf']).name)}</p>
      <p style="margin-top: 8px;">
        <a class="end-btn" href="../../../index.html">← Return to Main Aerospace Study Portal</a>
      </p>
    </footer>

    <section class="container" style="max-width: 920px; margin: 48px auto 24px; padding: 0 24px;">
      <div id="quoteContainer"></div>
    </section>
  </main>

  <script src="../../../assets/js/quotes.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      if (window.initAerospaceQuote) {{
        initAerospaceQuote('#quoteContainer');
      }}
    }});
  </script>
</body>
</html>
"""
    return head + body + cards + tail


# --------------------------------------------------------------------------- sync of the lists that mention the pages
def card_for_index(sheet, n):
    pills = "\n".join(f'            <span class="ex-pill">{html.escape(p)}</span>' for p in sheet["pills"])
    return f"""      <a href="{sheet['page']}" class="set-card available">
        <div class="set-accent-strip"></div>
        <div class="set-content">
          <div class="set-meta">
            <span class="set-code">{html.escape(sheet['set_code'])}</span>
            <span class="set-badge available">● {n} Solved Exercises</span>
          </div>
          <h3 class="set-title">{html.escape(sheet['title'], quote=False)}</h3>
          <p class="set-desc">{html.escape(sheet['desc'], quote=False)}</p>
          <div class="exercise-pills-list">
{pills}
          </div>
        </div>
        <div class="set-action">→</div>
      </a>
"""


def sync(root, sheets, counts):
    # source links: PDFs, pages and cards
    d = read_json(root, SOURCE_LINKS)
    for sh in sheets:
        d["pdfs"][sh["pdf_key"]] = {"path": sh["pdf"], "label": pathlib.PurePosixPath(sh["pdf"]).name, "pages": sh["pdf_pages"]}
        rel = SUBJECT + sh["page"]
        entry = d["pages"].setdefault(rel, {})
        entry["panel"] = [[sh["pdf_key"], 1], ["am-book", "auto"]]
        entry["cite"] = {"robinson": "am-book"}
        entry["cards"] = {f"{sh['id_prefix']}{num}": [sh["pdf_key"], page] for num, page in sh["cards"].items()}
    write(root, SOURCE_LINKS, json.dumps(d, indent=1, ensure_ascii=False) + "\n")

    # side menu
    nav = read_json(root, NAV)
    am = next(x for x in nav["subjects"] if x["slug"] == "advanced-maths")
    keep = [x for x in am["problemas"] if x["page"] not in {sh["page"] for sh in sheets}]
    am["problemas"] = keep + [{"page": sh["page"], "label": sh["nav_label"]} for sh in sheets]
    write(root, NAV, json.dumps(nav, indent=1, ensure_ascii=False) + "\n")

    # problems index
    s = (root / INDEX).read_text(encoding="utf-8")
    block = START + "\n" + "\n".join(card_for_index(sh, counts[sh["code"]]) for sh in sheets) + "      " + END + "\n"
    if START in s:
        s = s[:s.index(START)] + block + s[s.index(END) + len(END) + 1:]
    else:
        a = s.index("      <!-- CHAPTER 4: COMING SOON -->")
        end = "SOON</div>\n      </div>\n"                 # the disabled card ends with its SOON action cell
        b = s.index(end, a) + len(end)
        s = s[:a] + "      " + block + s[b:]
    write(root, INDEX, s)

    # root badges: the problems of Advanced Maths and the hero total
    s = (root / PORTAL).read_text(encoding="utf-8")
    i = s.index('href="subjects/advanced-maths/problemas/index.html"')
    j = s.index('<span class="area-badge available">', i)
    k = s.index("</span>", j)
    before = int(re.search(r"(\d+) problems", s[j:k]).group(1))
    base = 38                                          # Chapters 1 to 3 part 1: 10 + 17 + 11 problem cards
    after = base + sum(counts.values())
    s = s[:j] + f'<span class="area-badge available">{after} problems' + s[k:]
    hero = re.search(r'(<span class="stat-value"[^>]*>)(\d+)(</span>\s*<span class="stat-label">Solved problems)', s)
    s = s[:hero.start(2)] + str(int(hero.group(2)) + after - before) + s[hero.end(2):]
    write(root, PORTAL, s)


def link_sources(root, rel, text):
    cfg = read_json(root, SOURCE_LINKS)
    return SL.build_page(rel, text, cfg, SL.load_json(SL.ANCHORS, {}), {})


def generate(root):
    """Write every generated file under `root`; return their paths relative to `root`."""
    sheets = read_json(root, SHEETS)["sheets"]
    reg = registry(root)
    fig = figure_html(reg)
    outputs = list(reg.files)
    reg.write(root)
    counts, pages = {}, []
    for sh in sheets:
        probs = load_notes(root, sh)
        if not probs:                                   # a sheet whose notes are not written yet
            print(f"am_problems: no notes for {sh['code']}, skipped", file=sys.stderr)
            continue
        counts[sh["code"]] = len(probs)
        pages.append((sh, probs))
    sheets = [sh for sh, _ in pages]
    sync(root, sheets, counts)
    for sh, probs in pages:
        rel = SUBJECT + sh["page"]
        write(root, rel, link_sources(root, rel, page_html(sh, probs, fig)))
        outputs.append(rel)
    return outputs + list(INPUTS)


def check():
    """Regenerate in a scratch copy of the inputs and return the files that differ from the repository."""
    stale = []
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        for rel in INPUTS + (SHEETS, FIGS):
            write(root, rel, (ROOT / rel).read_text(encoding="utf-8"))
        for path in (ROOT / VAULT).glob("Problem - Ch[34]-I*-P*.md"):
            write(root, f"{VAULT}/{path.name}", path.read_text(encoding="utf-8"))
        for rel in generate(root):
            have = ROOT / rel
            if not have.is_file() or have.read_text(encoding="utf-8") != (root / rel).read_text(encoding="utf-8"):
                stale.append(rel)
    return stale


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if a generated file is stale")
    args = ap.parse_args(argv)
    if args.check:
        stale = check()
        for rel in stale:
            print("stale", rel)
        if stale:
            print(f"am_problems: {len(stale)} file(s) stale (run python tools/am_problems/build.py)")
            return 1
        print("am_problems: up to date")
        return 0
    outputs = generate(ROOT)
    print(f"am_problems: wrote {len(outputs)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
