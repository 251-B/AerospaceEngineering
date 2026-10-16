"""Build the Topic 4 (Navier-Stokes) problem page, its Obsidian notes and the links that list them.

    python tools/fluids_ns/build.py            # regenerate every file below
    python tools/fluids_ns/build.py --check    # exit 1 if a generated file is stale

Generated: subjects/fluid-mechanics/problemas/topic-4-navier-stokes.html, one note per problem in
vault/01 - Fluid Mechanics/ (Problem - NS*.md), the SVG figures in vault/attachments/FM-T4/, and the entries in
tools/source_links.json, the subject MOC, the problems index card and the root badge that list the problems.

Problem content: the notes themselves, vault/01 - Fluid Mechanics/Problem - NS*.md (read back with the reader of
tools/fluids_cl/notes.py; the vault is the source of truth). The statements are transcribed word for word from the
official sheets; the figure of each statement is a crop of the sheet (PNG in vault/attachments/FM-T4/, cropped by
hand, registered in tools/figures/fluids_t4.py RASTER). Page head and tail: the templates of tools/fluids_cl/.
The block types are those of tools/fluids_cl/build.py (p, m, h4, ul, table, note).
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
import figures.fluids_t4 as FIG  # noqa: E402
import source_links as SL  # noqa: E402

REG = FIG.build()
FIG_DIR = "attachments/" + REG.folder
VAULT = CL.VAULT
PAGE = "subjects/fluid-mechanics/problemas/topic-4-navier-stokes.html"
SOURCE_LINKS = CL.SOURCE_LINKS
MOC = CL.MOC
PROBLEMS_INDEX = CL.PROBLEMS_INDEX
PORTAL = CL.PORTAL
NAV = "tools/nav.json"
INPUTS = (SOURCE_LINKS, MOC, PROBLEMS_INDEX, PORTAL, NAV)   # edited in place by sync(): read from the repo first
BASE = "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/"
OTHER_PROBLEMS = 10 + 22                               # K1 to K10 and CL1 to CL22 share the root card with NS
PDF_PAGES = {10: 3, 11: 3, 12: 4, 16: 2, 17: 2}        # pages of the sheets with more than one page
MOC_HEAD = "  * **Solved Navier-Stokes Problems (Official Problem Sheet NS):**\n"

inline_html, block_html, block_md = CL.inline_html, CL.block_html, CL.block_md
EXTRA_CSS = CL.EXTRA_CSS


def load_problems(root=ROOT):
    """The problems, read back from their notes in the vault."""
    return notes.read_all(root / VAULT, "NS", REG.folder)


def fig_name(P, kind):
    name = f"{P['id']}-{kind}"
    return name if name in REG.web or name in FIG.RASTER else None


def fig_html(name):
    if name in REG.web:
        cap = REG.captions[name]
        return (f'<div class="diagram-card"><div class="diagram-scroll">{REG.web[name]}</div>'
                '<div class="diagram-hint">Swipe sideways to see the whole figure.</div>'
                f'<div class="diagram-caption">{html.escape(cap, quote=False)}</div>'
                f'<a class="diagram-open" href="../../../vault/{FIG_DIR}/{name}.svg" target="_blank" rel="noopener">'
                'Open the figure full size</a></div>')
    alt, cap = FIG.RASTER[name]
    src = f"../../../vault/{FIG_DIR}/{name}.png"
    return (f'<figure class="statement-figure"><div class="diagram-scroll"><img src="{src}" alt="{html.escape(alt)}" '
            'loading="lazy" style="max-width:100%;height:auto;display:block;margin:12px auto;background:#fff;'
            'border-radius:8px;padding:8px"></div><div class="diagram-hint">Swipe sideways to see the whole figure.</div>'
            f'<figcaption>{html.escape(cap, quote=False)}</figcaption>'
            f'<a class="diagram-open" href="{src}" target="_blank" rel="noopener">Open the figure full size</a></figure>')


def fig_md(name):
    ext = "svg" if name in REG.web else "png"
    cap = REG.captions[name] if name in REG.web else FIG.RASTER[name][1]
    return f"![[{FIG_DIR}/{name}.{ext}]]\n*{cap}*"


def with_figure(blocks, name, render, anchor="ul"):
    """The blocks of a phase with the solution figure after the first block of type `anchor` (or at the end)."""
    out, done = [], name is None
    for b in blocks:
        out.append(render(b))
        if not done and b[0] == anchor:
            out.append(fig_html(name) if render is block_html else fig_md(name))
            done = True
    if not done:
        out.append(fig_html(name) if render is block_html else fig_md(name))
    return out


def card_html(P):
    num = P["id"].upper()
    s = [f'    <article class="problem-card" id="{P["id"]}">',
         '      <div class="problem-header">',
         '        <div class="problem-title-group">',
         f'          <div class="problem-id">Problem {num}</div>',
         f'          <h2 class="problem-title">{inline_html(P["title"])}</h2>',
         '        </div>',
         '        <div class="tag-group">' + "".join(f'<span class="tag">{html.escape(t)}</span>' for t in P["tags_html"]) + '</div>',
         '      </div>', '',
         '      <div class="enunciado-box">',
         '        <h4>Official Problem Statement</h4>']
    s += [block_html(b) for b in P["statement"]]
    if fig_name(P, "statement"):
        s.append(fig_html(fig_name(P, "statement")))
    s.append(f'<p class="source-line">{inline_html(P["source_line"])}</p>')
    s += ['      </div>', '',
          '      <details class="solution-details">',
          '        <summary class="solution-summary"><span>Worked solution (4-phase method)</span><span class="summary-hint">expand / collapse</span></summary>',
          '        <div class="solution-content">']
    for badge, head, blocks in P["phases"]:
        s.append('<div class="phase-block">')
        s.append(f'<span class="phase-badge">{html.escape(badge)}</span>')
        s.append(f'<h3 class="phase-heading">{inline_html(head)}</h3>')
        name = fig_name(P, "setup")
        s += with_figure(blocks, name, block_html) if badge == "Phase 2" and name else [block_html(b) for b in blocks]
        s.append('</div>')
    s += ['        </div>', '      </details>', '    </article>', '']
    return "\n".join(s)


def note_md(P):
    num = P["id"].upper()
    fm = ["---", "materia: Fluid Mechanics", 'tema: "Topic 4: The Navier-Stokes Equations"', "tags:"]
    fm += [f"  - {t}" for t in P["tags_md"]]
    fm += [f"dificultad: {P.get('difficulty', 'media')}", f'fuente: "{BASE}{num}.pdf"',
           f"id: {json.dumps(P['id'])}", f"pill: {json.dumps(P['pill'])}", "tags_html:"]
    fm += [f"  - {json.dumps(t)}" for t in P["tags_html"]]
    fm += ["---", ""]
    out = fm
    out.append(f"# Problem {num}: {P['title']}")
    out.append("")
    out.append("> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].")
    out.append("> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.")
    out.append("")
    out.append("## Statement")
    out.append("")
    for b in P["statement"]:
        out.append(block_md(b))
        out.append("")
    if fig_name(P, "statement"):
        out += [fig_md(fig_name(P, "statement")), ""]
    out.append(P["source_line"])
    out.append("")
    for badge, head, blocks in P["phases"]:
        out.append(f"## {badge}: {head}")
        out.append("")
        name = fig_name(P, "setup")
        for b in (with_figure(blocks, name, block_md) if badge == "Phase 2" and name else map(block_md, blocks)):
            out.append(b)
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def page(probs):
    head = (ROOT / "tools/fluids_cl/template_head.html").read_text(encoding="utf-8").rstrip("\n")
    last = probs[-1]["id"].upper()
    head = CL.replace_once(head, "Flow Kinematics Solved Problems (K1-K10) - Fluid Mechanics",
                           f"Navier-Stokes Solved Problems (NS1-{last}) - Fluid Mechanics")
    head = CL.replace_once(head, "  </style>", EXTRA_CSS + "  </style>")
    tail = (ROOT / "tools/fluids_cl/template_tail.html").read_text(encoding="utf-8")
    tail = CL.replace_once(tail, "Worked solutions to the official kinematics problem collection (K1 to K10); statements follow the handwritten source sheets.",
                           f"Worked solutions to the official Navier-Stokes problem collection (NS1 to {last}); statements are transcribed word for word from the official sheets.")
    top = f"""
<body>
  <!-- Animated Celestial Canvas Background -->

  <!-- TOP HEADER -->
  <header class="site-header">
    <div class="header-inner">
      <div class="brand-area">
        <span class="brand-badge">FLUID MECHANICS</span>
        <span style="font-size: 13px; color: var(--text-muted);">Official Navier-Stokes Problem Sheet</span>
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
      <div class="topic-badge">Topic 4 &middot; Navier-Stokes Equations</div>
      <h1 class="page-title">Solved Problems: Official Collection NS1 to {last}</h1>
      <p class="page-meta">
        Worked solutions to the Navier-Stokes collection of the Department of Thermal and Fluid Engineering, Universidad Carlos III de Madrid. Every problem restates the official statement word for word, then follows four phases: (1) hypotheses, data, unknowns and degrees of freedom; (2) coordinate system, form of the fields and boundary conditions; (3) the derivation, with continuity and each Navier-Stokes component simplified term by term, the integrations written out and every constant fixed with its boundary condition; (4) interpretation, limiting cases and the dimensional check. Where a computed result differs from the handwritten official solution, the discrepancy is flagged in the problem; anything beyond the course material is marked as an extension. References to Notes.pdf are to Chapter 4 (The Navier-Stokes equations) and Chapter 3 (Conservation laws).
      </p>
    </div>

"""
    cards = "\n".join(card_html(P) for P in probs)
    return head + "\n" + top + cards + "\n" + tail


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sync(root, probs):
    """Update the places that list the NS problems: source links, the MOC, nav.json, the problems index card, the root badge."""
    n = len(probs)
    last = probs[-1]["id"].upper()

    d = json.loads((root / SOURCE_LINKS).read_text(encoding="utf-8"))
    for P in probs:
        k = P["id"]
        num = int(k[2:])
        d["pdfs"][f"fm-{k}"] = {"path": f"{BASE}{k.upper()}.pdf", "label": f"{k.upper()}.pdf", "pages": PDF_PAGES.get(num, 1)}
    entry = d["pages"].setdefault(PAGE, {"panel": [["fm-notes", 46, "Notes.pdf, Chapter 4"]], "cite": {"notes": "fm-notes"}})
    entry["cards"] = {P["id"]: [f"fm-{P['id']}", 1] for P in probs}
    write(root, SOURCE_LINKS, json.dumps(d, indent=1, ensure_ascii=False) + "\n")

    s = (root / MOC).read_text(encoding="utf-8")
    block = MOC_HEAD
    for P in probs:
        block += f"    * [[01 - Fluid Mechanics/{P['note_title']}|Problem {P['id'].upper()}: {P['title']}]]\n"
    if MOC_HEAD in s:
        start = s.index(MOC_HEAD)
        end = s.index("\n", s.index("\n", start) if False else start)
        rest = s[start + len(MOC_HEAD):]
        skip = 0
        for line in rest.split("\n"):
            if line.startswith("    * [["):
                skip += len(line) + 1
            else:
                break
        s = s[:start] + block + rest[skip:]
    else:
        anchor = "  * Official sources: `Notes.pdf` Chapter 4 and the problem sheets"
        i = s.index(anchor)
        j = s.index("\n", i) + 1
        s = s[:j] + block + s[j:]
    write(root, MOC, s)

    nav = json.loads((root / NAV).read_text(encoding="utf-8"))
    fm = next(x for x in nav["subjects"] if x["slug"] == "fluid-mechanics")
    item = {"page": "topic-4-navier-stokes.html", "label": f"4 · Navier-Stokes (NS1–{last})"}
    fm["problemas"] = [x for x in fm["problemas"] if x["page"] != item["page"]] + [item]
    write(root, NAV, json.dumps(nav, indent=1, ensure_ascii=False) + "\n")

    s = (root / PROBLEMS_INDEX).read_text(encoding="utf-8")
    svg = ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
           'stroke-linejoin="round" style="vertical-align: -1px; margin-right: 4px;" aria-hidden="true"><path d="M12 19l7-7 3 3-7 7-3-3z"/>'
           '<path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg>')
    desc = ("The Navier-Stokes problems of the official collection, each restated word for word and solved in four phases: the form of the "
            "fields, continuity and each momentum component simplified term by term, the integrations with their boundary conditions, "
            "and the forces, flow rates, trajectories and heat fluxes asked for. Covers flows between and around cylinders and spheres, "
            "porous walls with suction, free-surface films, similarity solutions and the Rayleigh-type cavity.")
    card = f'''      <a href="topic-4-navier-stokes.html" class="topic-card">
        <div class="topic-accent"></div>
        <div class="topic-body">
          <span class="topic-number">Topic 4 &middot; Chapter 4</span>
          <h2 class="topic-title">Solved Problems: Navier-Stokes Equations (NS1 to {last})</h2>
          <p class="topic-desc">{desc}</p>
          <div class="content-badges">
            <span class="cbadge problems">{svg}{n} Solved Problems</span>
          </div>
        </div>
        <div class="topic-arrow">&rarr;</div>
      </a>
'''
    if 'href="topic-4-navier-stokes.html"' in s:
        s = re.sub(r'      <a href="topic-4-navier-stokes.html" class="topic-card">.*?</a>\n', lambda m: card, s, count=1, flags=re.S)
    else:
        i = s.index('<a href="topic-3-conservation-laws.html" class="topic-card">')
        j = s.index("</a>\n", i) + len("</a>\n")
        s = s[:j] + "\n" + card + s[j:]
    write(root, PROBLEMS_INDEX, s)

    s = (root / PORTAL).read_text(encoding="utf-8")
    i = s.index('href="subjects/fluid-mechanics/problemas/index.html"')
    j = s.index('<span class="area-badge available">', i)
    k = s.index("</span>", j)
    before = int(re.search(r"(\d+) problems", s[j:k]).group(1))
    s = s[:j] + f'<span class="area-badge available">{OTHER_PROBLEMS + n} problems' + s[k:]
    hero = re.search(r'(<span class="stat-value"[^>]*>)(\d+)(</span>\s*<span class="stat-label">Solved problems)', s)
    s = s[:hero.start(2)] + str(int(hero.group(2)) + OTHER_PROBLEMS + n - before) + s[hero.end(2):]
    write(root, PORTAL, s)


def link_sources(root, text):
    cfg = json.loads((root / SOURCE_LINKS).read_text(encoding="utf-8"))
    return SL.build_page(PAGE, text, cfg, SL.load_json(SL.ANCHORS, {}), {})


def generate(root):
    """Write every generated file under `root`; return their paths relative to `root`."""
    probs = load_problems(root)
    REG.write(root)
    outputs = list(REG.files)
    for P in probs:
        rel = f"{VAULT}/{P['note_title']}.md"
        write(root, rel, note_md(P))
        outputs.append(rel)
    sync(root, probs)
    write(root, PAGE, link_sources(root, page(probs)))
    outputs += [PAGE] + list(INPUTS)
    return outputs


def check():
    """Regenerate in a scratch copy of the inputs and return the files that differ from the repository.

    The PNG crops of the official statements in vault/attachments/FM-T4/ are inputs (cropped by hand, never
    regenerated), so only their existence is tested (tools/tests/test_fluids_ns.py)."""
    stale = []
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        for rel in INPUTS:
            write(root, rel, (ROOT / rel).read_text(encoding="utf-8"))
        for path in (ROOT / VAULT).glob("Problem - NS*.md"):
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
            print(f"fluids_ns: {len(stale)} file(s) stale (run python tools/fluids_ns/build.py)")
            return 1
        print("fluids_ns: up to date")
        return 0
    outputs = generate(ROOT)
    print(f"fluids_ns: wrote {len(outputs)} files for {len(load_problems())} problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
