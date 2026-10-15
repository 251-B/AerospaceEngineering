"""Build the Topic 3 (conservation laws) problem page, its Obsidian notes and the links that list them.

    python tools/fluids_cl/build.py            # regenerate every file below
    python tools/fluids_cl/build.py --check    # exit 1 if a generated file is stale

Generated: subjects/fluid-mechanics/problemas/topic-3-conservation-laws.html, one note per problem in
vault/01 - Fluid Mechanics/, the figures in vault/attachments/FM-T3/, and the entries in tools/source_links.json,
the subject MOC, the problems index card and the root badge that list the problems.

Problem content: content/cl_p01.py to content/cl_p04.py (source of truth until the notes move to the vault).
Page head and tail: template_head.html and template_tail.html (copied from the kinematics page).

Block types used by the content modules:
  ("p", text) ("m", latex) ("h4", text) ("ul", [items]) ("table", head, rows)
  ("note", title, text)
  ("bal", dict(label=..., eq=latex, cols=[latex...], rows=[(surface, [cells...], is_wall)],
               wall=text or None, result=latex))
"""
import argparse, glob, html, importlib, json, os, pathlib, re, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONTENT = HERE / "content"
sys.path.insert(0, str(CONTENT))
sys.path.insert(0, str(HERE.parent))           # tools/, for the figures package
import figures.fluids_t3 as FIG  # noqa: E402
import source_links as SL  # noqa: E402   (deep links to the official PDFs)

REG = FIG.build()
FIG_DIR = "attachments/" + REG.folder
VAULT = "vault/01 - Fluid Mechanics"
PAGE = "subjects/fluid-mechanics/problemas/topic-3-conservation-laws.html"
SOURCE_LINKS = "tools/source_links.json"
MOC = VAULT + "/Fluid Mechanics MOC.md"
PROBLEMS_INDEX = "subjects/fluid-mechanics/problemas/index.html"
PORTAL = "index.html"
INPUTS = (SOURCE_LINKS, MOC, PROBLEMS_INDEX, PORTAL)   # edited in place by sync(): read from the repo first
BASE = "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/"
KINEMATICS_PROBLEMS = 10                               # K1 to K10 share the root card with the CL problems

EXTRA_CSS = """
    .balance-block { border-left: 3px solid var(--accent-border, var(--border-subtle)); padding: 4px 0 4px 14px; margin: 18px 0; }
    .balance-label { font-family: var(--font-mono); font-size: 0.78rem; letter-spacing: 0.03em; font-weight: 600; margin-bottom: 4px; }
    table.surface-table td:first-child, table.surface-table th:first-child { white-space: nowrap; }
    table.surface-table tr.wall-row td { background: var(--bg-subtle); font-weight: 600; border-top: 2px solid var(--border-subtle); border-bottom: 2px solid var(--border-subtle); }
    .balance-caption { font-size: 0.92rem; margin: 6px 0 4px; }
    [data-theme="dark"] { --text-faint: #7c8aa0; --border-card: rgba(255, 255, 255, 0.10); }
    [data-theme="light"] { --text-faint: #8a94a6; --border-card: rgba(0, 0, 0, 0.08); }
    .diagram-card { background: var(--bg-surface); border: 1px solid var(--border-card); border-radius: 12px; padding: 16px; margin: 18px 0; text-align: center; }
    .diagram-hint { display: none; font-family: var(--font-sans); font-size: 0.78rem; color: var(--text-muted); margin-top: 6px; }
    .diagram-open { display: inline-block; font-family: var(--font-mono); font-size: 0.75rem; margin-top: 6px; color: var(--accent); }
    @media (max-width: 600px) {
      .diagram-card { padding: 10px 6px; }
      .diagram-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
      .diagram-scroll svg, .diagram-scroll img { min-width: 470px; }
      .diagram-hint { display: block; }
    }
    @media print { .diagram-hint, .diagram-open { display: none !important; } }
    .diagram-caption { font-family: var(--font-sans); font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; text-align: center; }
    .diagram-card svg text tspan { text-decoration-thickness: 1px; }
"""


def load_problems():
    mods = sorted(glob.glob(str(CONTENT / "cl_p*.py")))
    probs = []
    for m in mods:
        name = os.path.splitext(os.path.basename(m))[0]
        mod = importlib.import_module(name)
        probs.extend(mod.PROBLEMS)
    probs.sort(key=lambda P: int(P["id"][2:]))
    return probs


def inline_html(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return t


def bal_html(b):
    d = b[1]
    s = ['<div class="balance-block">', f'<div class="balance-label">{inline_html(d["label"])}</div>',
         f'<div class="math-block">$$ {html.escape(d["eq"], quote=False)} $$</div>',
         '<p class="balance-caption">Each surface integral, surface by surface (the vertical line drawn under each integral in class):</p>']
    head = "<th>Surface</th>" + "".join(f"<th>${html.escape(c, quote=False)}$</th>" for c in d["cols"])
    rows = []
    for surf, cells, wall in d["rows"]:
        cls = ' class="wall-row"' if wall else ""
        rows.append(f"<tr{cls}><td>${html.escape(surf, quote=False)}$</td>" + "".join(f"<td>{inline_html(c)}</td>" for c in cells) + "</tr>")
    s.append(f'<div class="table-wrap"><table class="data-table surface-table"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
    if d.get("wall"):
        s.append(f'<p class="balance-caption">{inline_html(d["wall"])}</p>')
    s.append(f'<div class="math-block">$$ {html.escape(d["result"], quote=False)} $$</div>')
    s.append("</div>")
    return "\n".join(s)


def bal_md(b):
    d = b[1]
    out = [f"**{d['label']}**", "", f"$$ {d['eq']} $$", "",
           "Each surface integral, surface by surface (the vertical line drawn under each integral in class):", "",
           "| Surface | " + " | ".join(f"${c}$" for c in d["cols"]) + " |",
           "| :--- | " + " | ".join(":---" for _ in d["cols"]) + " |"]
    for surf, cells, wall in d["rows"]:
        lab = f"**${surf}$** (boxed)" if wall else f"${surf}$"
        out.append(f"| {lab} | " + " | ".join(cells) + " |")
    out.append("")
    if d.get("wall"):
        out += [d["wall"], ""]
    out.append(f"$$ {d['result']} $$")
    return "\n".join(out)


def block_html(b):
    k = b[0]
    if k == "p":
        return f"<p>{inline_html(b[1])}</p>"
    if k == "m":
        return f'<div class="math-block">$$ {html.escape(b[1], quote=False)} $$</div>'
    if k == "h4":
        return f'<h4 class="step-heading">{inline_html(b[1])}</h4>'
    if k == "ul":
        return '<ul class="bullet-list">' + "".join(f"<li>{inline_html(i)}</li>" for i in b[1]) + "</ul>"
    if k == "table":
        head = "".join(f"<th>{inline_html(h)}</th>" for h in b[1])
        rows = "".join("<tr>" + "".join(f"<td>{inline_html(c)}</td>" for c in r) + "</tr>" for r in b[2])
        return f'<div class="table-wrap"><table class="data-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    if k == "note":
        return f'<div class="note-box"><strong>{inline_html(b[1])}</strong><p>{inline_html(b[2])}</p></div>'
    if k == "bal":
        return bal_html(b)
    raise ValueError(k)


def block_md(b):
    k = b[0]
    if k == "p":
        return b[1]
    if k == "m":
        return f"$$ {b[1]} $$"
    if k == "h4":
        return f"### {b[1]}"
    if k == "ul":
        return "\n".join(f"- {i}" for i in b[1])
    if k == "table":
        out = ["| " + " | ".join(b[1]) + " |", "| " + " | ".join(":---" for _ in b[1]) + " |"]
        out += ["| " + " | ".join(r) + " |" for r in b[2]]
        return "\n".join(out)
    if k == "note":
        kind = "warning" if b[1].startswith(("Erratum", "Discrepancy")) else "info"
        return f"> [!{kind}] {b[1]}\n> {b[2]}"
    if k == "bal":
        return bal_md(b)
    raise ValueError(k)


def fig_name(P, kind):
    """Figure registered for this problem: clN-statement or clN-cv (SVG or PNG crop), or None."""
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


def with_cv(blocks, name, render):
    """Phase 2 blocks with the control-volume figure after the first list (or at the end)."""
    out, done = [], name is None
    for b in blocks:
        out.append(render(b))
        if not done and b[0] == "ul":
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
        s.append(f'<span class="phase-badge">{badge}</span>')
        s.append(f'<h3 class="phase-heading">{head}</h3>')
        s += with_cv(blocks, fig_name(P, "cv"), block_html) if badge == "Phase 2" else [block_html(b) for b in blocks]
        s.append('</div>')
    s += ['        </div>', '      </details>', '    </article>', '']
    return "\n".join(s)


def note_md(P):
    num = P["id"].upper()
    fm = ["---", "materia: Fluid Mechanics", 'tema: "Topic 3: Conservation Laws"', "tags:"]
    fm += [f"  - {t}" for t in P["tags_md"]]
    fm += [f"dificultad: {P.get('difficulty', 'media')}", f'fuente: "{BASE}{num}.pdf"', "---", ""]
    out = fm
    out.append(f"# Problem {num}: {P['title']}")
    out.append("")
    out.append("> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].")
    out.append("> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.")
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
        for b in (with_cv(blocks, fig_name(P, "cv"), block_md) if badge == "Phase 2" else map(block_md, blocks)):
            out.append(b)
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def page(probs):
    head = (HERE / "template_head.html").read_text(encoding="utf-8").rstrip("\n")
    last = probs[-1]["id"].upper()
    head = head.replace("Flow Kinematics Solved Problems (K1-K10) - Fluid Mechanics", f"Conservation Laws Solved Problems (CL1-{last}) - Fluid Mechanics")
    head = head.replace("  </style>", EXTRA_CSS + "  </style>", 1)
    tail = (HERE / "template_tail.html").read_text(encoding="utf-8")
    so_far = "" if last == "CL22" else " so far"
    tail = tail.replace("Worked solutions to the official kinematics problem collection (K1 to K10); statements follow the handwritten source sheets.",
                        f"Worked solutions to the official conservation-laws problem collection (CL1 to {last}{so_far}); statements follow the handwritten source sheets.")
    rest = "" if last == "CL22" else f" ({len(probs)} of the 22 problems so far; the rest of the collection is added in batches)"
    top = f"""
<body>
  <!-- Animated Celestial Canvas Background -->

  <!-- TOP HEADER -->
  <header class="site-header">
    <div class="header-inner">
      <div class="brand-area">
        <span class="brand-badge">FLUID MECHANICS</span>
        <span style="font-size: 13px; color: var(--text-muted);">Official Conservation Laws Problem Sheet</span>
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
      <div class="topic-badge">Topic 3 &middot; Conservation Laws</div>
      <h1 class="page-title">Solved Problems: Official Collection CL1 to {last}</h1>
      <p class="page-meta">
        Worked solutions to the conservation-laws collection of the Department of Thermal and Fluid Engineering, Universidad Carlos III de Madrid{rest}. Every problem restates the official statement, then follows four phases: (1) hypotheses, data and unknowns; (2) frames, control volume and its surfaces; (3) the balances; (4) interpretation, limits and dimensional check. The balances follow the method used in class: each one is written in full with the vanishing terms crossed out and the reason underneath, every surface integral is then evaluated surface by surface (the vertical line drawn under each integral), the wall terms are grouped (boxed) as the force on the body, and each result is boxed and numbered. Discrepancies found in the handwritten official solutions are flagged in the corresponding problem, and anything beyond the course material is marked as an extension. References to Notes.pdf are to Chapter 3 (Conservation laws).
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
    """Update the places that list the CL problems: source links, the MOC, the problems index card, the root badge."""
    n = len(probs)
    last = probs[-1]["id"].upper()

    d = json.loads((root / SOURCE_LINKS).read_text(encoding="utf-8"))
    for P in probs:
        k = P["id"]
        d["pdfs"][f"fm-{k}"] = {"path": f"{BASE}{k.upper()}.pdf", "label": f"{k.upper()}.pdf", "pages": 1}
    d["pages"][PAGE]["cards"] = {P["id"]: [f"fm-{P['id']}", 1] for P in probs}
    write(root, SOURCE_LINKS, json.dumps(d, indent=1, ensure_ascii=False) + "\n")

    s = (root / MOC).read_text(encoding="utf-8")
    start = s.index("  * **Solved Conservation-Laws Problems")
    end = s.index("  * **Practical Modular Subchapters:**")
    status = "complete" if last == "CL22" else f"in progress: CL1 to {last} of CL1 to CL22"
    block = f"  * **Solved Conservation-Laws Problems (Official Problem Sheet CL, {status}):**\n"
    for P in probs:
        block += f"    * [[01 - Fluid Mechanics/{P['note_title']}|Problem {P['id'].upper()}: {P['title']}]]\n"
    write(root, MOC, s[:start] + block + s[end:])

    s = (root / PROBLEMS_INDEX).read_text(encoding="utf-8")
    s = re.sub(r"Solved Problems: Conservation Laws \(CL1 to CL\d+\)", f"Solved Problems: Conservation Laws (CL1 to {last})", s)
    desc = (f"The official conservation-laws collection ({n} of 22 problems so far, added in batches), each restated and solved in four phases with the method used in class: every balance written in full with the vanishing terms crossed out, each surface integral evaluated surface by surface, and the wall terms grouped as the force on the body."
            if last != "CL22" else
            "The 22 problems of the official conservation-laws collection, each restated and solved in four phases with the method used in class: every balance written in full with the vanishing terms crossed out, each surface integral evaluated surface by surface, and the wall terms grouped as the force on the body.")
    s = re.sub(r'(<a href="topic-3-conservation-laws.html" class="topic-card">.*?<p class="topic-desc">).*?(</p>)', lambda m: m.group(1) + desc + m.group(2), s, flags=re.S)
    s = re.sub(r'(<a href="topic-3-conservation-laws.html".*?</svg>)\d+ Solved Problems', lambda m: m.group(1) + f"{n} Solved Problems", s, flags=re.S)
    write(root, PROBLEMS_INDEX, s)

    # root card of the fluid mechanics subject: its kinematics problems plus the CL problems
    s = (root / PORTAL).read_text(encoding="utf-8")
    i = s.index('href="subjects/fluid-mechanics/problemas/index.html"')
    j = s.index('<span class="area-badge available">', i)
    k = s.index("</span>", j)
    s = s[:j] + f'<span class="area-badge available">{KINEMATICS_PROBLEMS + n} problems' + s[k:]
    write(root, PORTAL, s)


def link_sources(root, text):
    """Add the links to the official PDFs (tools/source_links.py) to the page text, using the synced config."""
    cfg = json.loads((root / SOURCE_LINKS).read_text(encoding="utf-8"))
    return SL.build_page(PAGE, text, cfg, SL.load_json(SL.ANCHORS, {}), {})


def generate(root):
    """Write every generated file under `root`; return their paths relative to `root`."""
    probs = load_problems()
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
    """Regenerate in a scratch copy of the inputs and return the files that differ from the repository."""
    stale = []
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        for rel in INPUTS:
            write(root, rel, (ROOT / rel).read_text(encoding="utf-8"))
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
            print(f"fluids_cl: {len(stale)} file(s) stale (run python tools/fluids_cl/build.py)")
            return 1
        print("fluids_cl: up to date")
        return 0
    outputs = generate(ROOT)
    print(f"fluids_cl: wrote {len(outputs)} files for {len(load_problems())} problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
