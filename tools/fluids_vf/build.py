"""Build the Topic 7 (Viscous Flows) problem page and the links that list its problems.

    python tools/fluids_vf/build.py            # regenerate every file below
    python tools/fluids_vf/build.py --check    # exit 1 if a generated file is stale

Problem content: the notes vault/01 - Fluid Mechanics/Problem - VF*.md (the vault is the source of truth). Each note
has the frontmatter keys id, pill, tags, tags_html and sheets (the sheet number, whose page 1 is the card's "Original
statement" link); then "## Statement" ending with the "Source: ..." line, and the solution sections in the Fluid
Mechanics order (every other "## " section, rendered in order, never labelled "Phase").

Blocks are those of tools/fluids_cl/build.py (p, m, h4, ul, table, note), plus a figure of tools/figures/fluids_t7p.py,
    ![[attachments/FM-T7/<name>.svg]]  (or .png for the crop of a sheet)  + caption line (synced here)

Generated: subjects/fluid-mechanics/problemas/topic-7-viscous-flow.html, the SVG figures in
vault/attachments/FM-T7/, the figure captions inside the notes, and the entries in tools/source_links.json,
tools/nav.json, the subject MOC, the problems index card, the "Problem Sets (N Solved)" label of both subject indexes
and the root badge (tools/fluids_cl/build.py, sync_portal).
"""
import argparse
import html
import importlib.util
import json
import pathlib
import re
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent))           # tools/, for the figures package


def _load_cl():
    spec = importlib.util.spec_from_file_location("fluids_cl_build", ROOT / "tools/fluids_cl/build.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CL = _load_cl()
notes = CL.notes
import figures.fluids_t7 as FIG  # noqa: E402
import source_links as SL  # noqa: E402

REG = FIG.build()
FOLDER = REG.folder
FIG_DIR = "attachments/" + FOLDER
VAULT = CL.VAULT
PAGE = "subjects/fluid-mechanics/problemas/topic-7-viscous-flow.html"
THEORY = "subjects/fluid-mechanics/teoria/topic-7.html"
SOURCE_LINKS = CL.SOURCE_LINKS
MOC = CL.MOC
PROBLEMS_INDEX = CL.PROBLEMS_INDEX
THEORY_INDEX = CL.THEORY_INDEX
PORTAL = CL.PORTAL
NAV = "tools/nav.json"
INPUTS = (SOURCE_LINKS, MOC, PROBLEMS_INDEX, THEORY_INDEX, PORTAL, NAV)   # edited in place by sync(): read from the repo
BASE = "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/"
SHEETS = range(2, 21)                           # VF2 to VF20 (there is no VF1)
SHEET_PAGES = {2: 5, 15: 3, 16: 2, 20: 3}
SHEET_FILES = {2: "VF2_w_solution.pdf"}             # sheets with more than one page
PANEL = [["fm-notes", 82, "Notes.pdf, Chapter 7"]]
MOC_HEAD = "  * **Solved Viscous Flow Problems (Official Problem Sheets VF):**\n"
MOC_ANCHOR = "  * Official sources: `Notes.pdf` Chapter 7 and the problem sheets"
FIG_RE = re.compile(rf"^!\[\[{re.escape(FIG_DIR)}/([\w-]+)\.(svg|png)\]\]$")

inline_html, block_html = CL.inline_html, CL.block_html
EXTRA_CSS = CL.EXTRA_CSS + """
    .katex-display { overflow-x: auto; overflow-y: hidden; max-width: 100%; }
    .enunciado-box p, .solution-content p, .solution-content li { overflow-wrap: break-word; }
"""


# ----------------------------------------------------------------------------------------------- reading the notes
def _blocks(lines):
    out = []
    for ch in notes._chunks(lines):
        m = FIG_RE.match(ch[0])
        if m:
            if m.group(1) not in REG.web:
                raise ValueError(f"unknown figure {m.group(1)}")
            out.append(("fig", m.group(1)))
        else:
            out += notes._blocks(ch, "NONE")
    return out


def read_problem(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    fm, at = notes._frontmatter(lines)
    for key in ("id", "pill", "tags", "tags_html", "sheets"):
        if key not in fm:
            raise ValueError(f"{path.name}: the frontmatter lacks '{key}'")
    body = lines[at:]
    head = next((re.match(r"^# Problem (VF\d+): (.*)$", l) for l in body if l.startswith("# Problem ")), None)
    if head is None:
        raise ValueError(f"{path.name}: missing the '# Problem VFn: title' heading")
    sections, name = [], None
    for line in body:
        if line.startswith("## "):
            name = line[3:]
            sections.append((name, []))
        elif name is not None:
            sections[-1][1].append(line)
    if not sections or sections[0][0] != "Statement":
        raise ValueError(f"{path.name}: the first section must be '## Statement'")
    st = sections[0][1]
    chunks = notes._chunks(st)
    if not chunks or not chunks[-1][0].startswith("Source: "):
        raise ValueError(f"{path.name}: the statement must end with the 'Source: ...' line")
    statement = _blocks(st[:st.index(chunks[-1][0])])
    parts = [(n, _blocks(b)) for n, b in sections[1:]]
    for n, _ in parts:
        if re.match(r"(?i)phase\b", n):
            raise ValueError(f"{path.name}: section '{n}' (no Phase labels)")
    sheets = [int(x) for x in (fm["sheets"] if isinstance(fm["sheets"], list) else [fm["sheets"]])]
    return {"id": fm["id"], "pill": fm["pill"], "title": head.group(2), "num": head.group(1), "note_title": path.stem,
            "tags_html": fm["tags_html"], "statement": statement, "source_line": "\n".join(chunks[-1]),
            "sections": parts, "sheets": sheets, "path": path}


def load_problems(root=ROOT):
    paths = sorted((root / VAULT).glob("Problem - VF*.md"), key=lambda p: int(re.search(r"VF(\d+)", p.name).group(1)))
    return [read_problem(p) for p in paths]


def synced_note(text):
    """The note with the caption line under each figure embed set to the registry caption."""
    lines = text.split("\n")
    for i, line in enumerate(lines[:-1]):
        m = FIG_RE.match(line)
        if m and m.group(1) in REG.captions:
            lines[i + 1] = f"*{REG.captions[m.group(1)]}*"
    return "\n".join(lines)


# ----------------------------------------------------------------------------------------------- rendering
def fig_html(name):
    cap = REG.captions[name]
    ext = "png" if f"vault/{FIG_DIR}/{name}.png" in REG.rasters else "svg"
    return (f'<div class="diagram-card"><div class="diagram-scroll">{REG.web[name]}</div>'
            '<div class="diagram-hint">Swipe sideways to see the whole figure.</div>'
            f'<div class="diagram-caption">{html.escape(cap, quote=False)}</div>'
            f'<a class="diagram-open" href="../../../vault/{FIG_DIR}/{name}.{ext}" target="_blank" rel="noopener">'
            'Open the figure full size</a></div>')


def render(b):
    return fig_html(b[1]) if b[0] == "fig" else block_html(b)


def card_html(P):
    s = [f'    <article class="problem-card" id="{P["id"]}">',
         '      <div class="problem-header">',
         '        <div class="problem-title-group">',
         f'          <div class="problem-id">Problem {P["num"]}</div>',
         f'          <h2 class="problem-title">{inline_html(P["title"])}</h2>',
         '        </div>',
         '        <div class="tag-group">' + "".join(f'<span class="tag">{html.escape(t)}</span>' for t in P["tags_html"]) + '</div>',
         '      </div>', '',
         '      <div class="enunciado-box">',
         '        <h4>Official Problem Statement</h4>']
    s += [render(b) for b in P["statement"]]
    s.append(f'<p class="source-line">{inline_html(P["source_line"])}</p>')
    s += ['      </div>', '',
          '      <details class="solution-details">',
          '        <summary class="solution-summary"><span>Worked solution</span><span class="summary-hint">expand / collapse</span></summary>',
          '        <div class="solution-content">']
    for head, blocks in P["sections"]:
        s.append('<div class="phase-block">')
        s.append(f'<h3 class="phase-heading">{inline_html(head)}</h3>')
        s += [render(b) for b in blocks]
        s.append('</div>')
    s += ['        </div>', '      </details>', '    </article>', '']
    return "\n".join(s)


def page(probs):
    head = (ROOT / "tools/fluids_cl/template_head.html").read_text(encoding="utf-8").rstrip("\n")
    head = CL.replace_once(head, "Flow Kinematics Solved Problems (K1-K10) - Fluid Mechanics",
                           "Viscous Flow Solved Problems (VF2-VF20) - Fluid Mechanics")
    head = CL.replace_once(head, "  </style>", EXTRA_CSS + "  </style>")
    tail = (ROOT / "tools/fluids_cl/template_tail.html").read_text(encoding="utf-8")
    tail = CL.replace_once(tail, "Worked solutions to the official kinematics problem collection (K1 to K10); statements follow the handwritten source sheets.",
                           "Worked solutions to the official viscous-flow sheets (VF2 to VF20); statements transcribed from the sheets, solutions checked against their handwritten keys.")
    top = """
<body>
  <!-- Animated Celestial Canvas Background -->

  <!-- TOP HEADER -->
  <header class="site-header">
    <div class="header-inner">
      <div class="brand-area">
        <span class="brand-badge">FLUID MECHANICS</span>
        <span style="font-size: 13px; color: var(--text-muted);">Official Viscous Flow Problem Sheets</span>
      </div>
      <div class="nav-actions">
        <a href="../../../index.html" class="back-link">Main Portal</a>
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme"></button>
      </div>
    </div>
  </header>

  <!-- MAIN ARTICLE -->
  <main class="content-container">

    <div class="page-title-box">
      <div class="topic-badge">Topic 7 &middot; Viscous Flows</div>
      <h1 class="page-title">Solved Problems: Official Viscous Flow Sheets VF2 to VF20</h1>
      <p class="page-meta">
        Worked solutions to the nineteen viscous-flow sheets of the course (VF2 to VF20), most of them past exam problems. Each statement is transcribed from the sheet and its figure redrawn; each solution follows the handwritten key of the sheet with every step written out: the simplified Navier-Stokes equations term by term, every integration with its constants fixed by the boundary conditions, the fluxes and stresses, the order-of-magnitude criteria for a slender or quasi-steady flow, and the checks. Where the key has a slip, the correction is shown as an erratum. References to Notes.pdf are to Chapter 7 (Viscous Flows).
      </p>
    </div>

"""
    cards = "\n".join(card_html(P) for P in probs)
    return head + "\n" + top + cards + "\n" + tail


# ----------------------------------------------------------------------------------------------- lists that name the problems
def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sync(root, probs):
    n = len(probs)
    d = json.loads((root / SOURCE_LINKS).read_text(encoding="utf-8"))
    for k in SHEETS:
        name = SHEET_FILES.get(k, f"VF{k}.pdf")
        d["pdfs"][f"fm-vf{k}"] = {"path": f"{BASE}{name}", "label": name, "pages": SHEET_PAGES.get(k, 1)}
    entry = d["pages"].setdefault(PAGE, {"panel": PANEL, "cite": {"notes": "fm-notes"}})
    entry["cards"] = {P["id"]: [f"fm-vf{P['sheets'][0]}", 1] for P in probs}
    d["pages"].setdefault(THEORY, {"panel": PANEL, "cite": {"notes": "fm-notes"}})
    write(root, SOURCE_LINKS, json.dumps(d, indent=1, ensure_ascii=False) + "\n")

    s = (root / MOC).read_text(encoding="utf-8")
    block = MOC_HEAD + "".join(f"    * [[01 - Fluid Mechanics/{P['note_title']}|Problem {P['num']}: {P['title']}]]\n" for P in probs)
    if MOC_HEAD in s:
        start = s.index(MOC_HEAD)
        rest = s[start + len(MOC_HEAD):]
        skip = 0
        for line in rest.split("\n"):
            if line.startswith("    * [["):
                skip += len(line) + 1
            else:
                break
        s = s[:start] + block + rest[skip:]
    else:
        i = s.index(MOC_ANCHOR)
        j = s.index("\n", i) + 1
        s = s[:j] + block + s[j:]
    write(root, MOC, s)

    nav = json.loads((root / NAV).read_text(encoding="utf-8"))
    fm = next(x for x in nav["subjects"] if x["slug"] == "fluid-mechanics")
    item = {"page": "topic-7-viscous-flow.html", "label": "7 · Viscous flow (VF2–VF20)"}
    pages = [x["page"] for x in fm["problemas"]]
    if item["page"] in pages:
        fm["problemas"][pages.index(item["page"])] = item
    else:
        fm["problemas"].append(item)
    theory = {"page": "topic-7.html", "label": "7 · Viscous flows"}
    if not any(x["page"] == theory["page"] for x in fm["teoria"]):
        fm["teoria"].append(theory)
    write(root, NAV, json.dumps(nav, indent=1, ensure_ascii=False) + "\n")

    s = (root / PROBLEMS_INDEX).read_text(encoding="utf-8")
    svg = ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
           'stroke-linejoin="round" style="vertical-align: -1px; margin-right: 4px;" aria-hidden="true"><path d="M12 19l7-7 3 3-7 7-3-3z"/>'
           '<path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg>')
    desc = ("The nineteen viscous-flow sheets of the course, solved step by step after their handwritten keys: "
            "Couette and Poiseuille flows, pipes and films, unsteady layers, slender flows with the criteria of "
            "Chapter 7 and lubrication, each integration written out with its boundary conditions.")
    card = f'''      <a href="topic-7-viscous-flow.html" class="topic-card">
        <div class="topic-accent"></div>
        <div class="topic-body">
          <span class="topic-number">Topic 7 &middot; Chapter 7</span>
          <h2 class="topic-title">Solved Problems: Viscous Flows (VF2 to VF20)</h2>
          <p class="topic-desc">{desc}</p>
          <div class="content-badges">
            <span class="cbadge problems">{svg}{n} Solved Problems</span>
          </div>
        </div>
        <div class="topic-arrow">&rarr;</div>
      </a>
'''
    if 'href="topic-7-viscous-flow.html"' in s:
        s = re.sub(r'      <a href="topic-7-viscous-flow.html" class="topic-card">.*?</a>\n', lambda m: card, s, count=1,
                   flags=re.S)
    else:
        i = s.index('<a href="topic-6-dimensional-analysis.html" class="topic-card">')
        j = s.index("</a>\n", i) + len("</a>\n")
        s = s[:j] + "\n" + card + s[j:]
    write(root, PROBLEMS_INDEX, s)

    CL.sync_portal(root)


def link_sources(root, text):
    cfg = json.loads((root / SOURCE_LINKS).read_text(encoding="utf-8"))
    return SL.build_page(PAGE, text, cfg, SL.load_json(SL.ANCHORS, {}), {})


def generate(root):
    """Write every generated file under `root`; return their paths relative to `root`."""
    REG.write(root)
    outputs = list(REG.files)
    for path in sorted((root / VAULT).glob("Problem - VF*.md")):
        rel = f"{VAULT}/{path.name}"
        write(root, rel, synced_note(path.read_text(encoding="utf-8")))
        outputs.append(rel)
    probs = load_problems(root)
    sync(root, probs)
    write(root, PAGE, link_sources(root, page(probs)))
    return outputs + [PAGE] + list(INPUTS)


def check():
    """Regenerate in a scratch copy of the inputs and return the files that differ from the repository.

    The PNG crop of the VF sheet crops in vault/attachments/FM-T7/ is an input (cropped by hand, never regenerated),
    so only its existence is tested (tools/tests/test_fluids_vf.py)."""
    stale = []
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        for rel in INPUTS:
            write(root, rel, (ROOT / rel).read_text(encoding="utf-8"))
        for path in (ROOT / VAULT).glob("Problem - VF*.md"):
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
            print(f"fluids_vf: {len(stale)} file(s) stale (run python tools/fluids_vf/build.py)")
            return 1
        print("fluids_vf: up to date")
        return 0
    outputs = generate(ROOT)
    print(f"fluids_vf: wrote {len(outputs)} files for {len(load_problems())} problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
