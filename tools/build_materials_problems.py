#!/usr/bin/env python3
"""Build the Aerospace Materials I Topic 5 problems page from its vault notes (Obsidian first, web second).

    subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html
        Problem - T5-01 ... T5-15 (Problems T5_MechanicalProperties.pdf), in
        vault/02 - Aerospace Materials I/

Per note (same layout as the Topic 4 notes):
    - frontmatter key `badge` is the second chip of the card header;
    - `# ✏️ Problem: T5-NN — Title` gives the card number and title;
    - `## 📄 Official Statement` is a blockquote: the statement (paragraphs, lists, tables, figure embeds)
      and a last line `*(Solution: ...)*` with the key printed on the sheet (the `.solution-box`);
    - the four `## ... Phase k` sections fill the four phase blocks; `### ` headings become bold paragraphs;
    - `## ✅ Check against the official solution` closes phase 4 (callouts `> [!warning]` are kept);
    - `## 🔗 Related Links` is not rendered.
Figure embeds `![[attachments/T5/<name>.svg]]` come from tools/figures/materials_t5.py (the SVG files are
written to vault/attachments/T5 together with the page). The head, header and footer are those of the
Topic 4 problems page. The PDF deep links of tools/source_links.py are applied before writing.

Usage:
    python tools/build_materials_problems.py            # write the figures and the page
    python tools/build_materials_problems.py --check    # exit 1 if the page or a figure is stale
"""
import argparse
import html
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_topic_pages as bt  # noqa: E402
import source_links as sl  # noqa: E402

VAULT = REPO / "vault" / "02 - Aerospace Materials I"
PAGE = "subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html"
SHELL = "subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html"
SHEET = "Problems T5_MechanicalProperties.pdf"
# Labels shown on the four solution blocks. The notes still use "## ... Phase k" headings to delimit them (internal
# only): no page shows the word "Phase" (AGENTS.md, "Problem-solving standard").
PHASES = {1: "Hypotheses &amp; Parameters", 2: "Model &amp; Strategy",
          3: "Step-by-Step Calculation", 4: "Result &amp; Checks"}
TOTAL = 15


def read_note(path):
    text = path.read_text(encoding="utf-8")
    fm = {}
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if m:
        for line in m.group(1).split("\n"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    body = bt.strip_frontmatter(text)
    head = re.search(r"^# ✏️ Problem: T5-(\d+) — (.*)$", body, re.M)
    if not head:
        raise SystemExit(f"{path.name}: missing '# ✏️ Problem: T5-NN — Title' heading")
    sections = {}
    for chunk in re.split(r"\n(?=## )", body[head.end():]):
        chunk = chunk.strip("\n")
        if chunk.startswith("## "):
            title, _, rest = chunk.partition("\n")
            sections[title[3:]] = rest.split("\n")
    return {"n": int(head.group(1)), "title": head.group(2).strip(), "badge": fm.get("badge", ""), "sections": sections,
            "name": path.stem}


def steps(lines, figure):
    """Section lines to HTML: `### ` headings become bold paragraphs, the rest goes through build_topic_pages."""
    out, chunk = [], []
    for line in lines:
        m = re.match(r"###\s+(.*)", line)
        if m:
            out.append(bt.blocks(chunk, figure))
            chunk = []
            out.append(f"<p><strong>{bt.inline(m.group(1))}</strong></p>")
        else:
            chunk.append(line)
    out.append(bt.blocks(chunk, figure))
    return "\n".join(x for x in out if x)


def card(note, figure):
    n = note["n"]
    sec = note["sections"]
    stmt_key = next(k for k in sec if "Official Statement" in k)
    stmt, key = [], None
    for line in sec[stmt_key]:
        line = re.sub(r"^>\s?", "", line)
        m = re.match(r"^\*\(Solutions?:\s*(.*)\)\*\s*$", line)
        if m:
            key = m.group(1)
        else:
            stmt.append(line)
    phases = {}
    for k, lines in sec.items():
        m = re.search(r"Phase (\d)", k)
        if m:
            phases[int(m.group(1))] = list(lines)
    check = next((v for k, v in sec.items() if "Check against" in k), None)
    if sorted(phases) != [1, 2, 3, 4]:
        raise SystemExit(f"{note['name']}: expected phases 1-4, found {sorted(phases)}")
    stmt_html = bt.blocks(stmt, figure)
    first = re.match(r"^(\d+)\. ", next((l for l in stmt if l.strip()), ""))
    if first and stmt_html.lstrip().startswith("<ol>"):
        stmt_html = stmt_html.replace("<ol>", f'<ol start="{first.group(1)}">', 1)   # the statement keeps the number of the sheet
    blocks = [f'''        <div class="statement-box">
{stmt_html}''']
    if key:
        blocks.append(f'          <div class="solution-box">Official Solution: {bt.inline(key)}</div>')
    blocks.append("        </div>")
    grid = []
    for k in (1, 2, 3, 4):
        inner = steps(phases[k], figure)
        if k == 4 and check is not None:
            inner += "\n<p><strong>Check against the official solution</strong></p>\n" + steps(check, figure)
        grid.append(f'''          <div class="phase-step phase-{k}">
            <span class="phase-badge">{PHASES[k]}</span>
{inner}
          </div>''')
    return f'''    <!-- ========================================== -->
    <!-- PROBLEM {n} -->
    <!-- ========================================== -->
    <details open class="problem-card" id="prob-{n}">
      <summary class="problem-summary">
        <div class="problem-header">
          <div class="problem-badge-group">
            <span class="prob-num-badge">Problem {n}</span>
            <span class="prob-source-badge">{SHEET} #{n}</span>
            <span class="prob-source-badge">{html.escape(note["badge"], quote=False)}</span>
          </div>
          <span style="font-size: 12px; color: var(--accent); font-family: var(--font-mono); font-weight: 700;">Click to Collapse ▲</span>
        </div>
        <h2 class="problem-title">{bt.inline(note["title"])}</h2>
      </summary>

      <div class="card-body">
{chr(10).join(blocks)}

        <div class="phases-grid">
{chr(10).join(grid)}
        </div>
      </div>
    </details>
'''


def build_page():
    notes = sorted((read_note(p) for p in VAULT.glob("Problem - T5-*.md")), key=lambda x: x["n"])
    if not notes:
        raise SystemExit("no Problem - T5-NN notes found")
    figure = bt.FigureSet("materials_t5")
    shell = sl.strip_links((REPO / SHELL).read_text(encoding="utf-8")).replace("Â·", "·")
    head = shell[:shell.index('<main class="problems-container">')]
    tail = shell[shell.index("  <!-- Page Footer -->"):]
    head = re.sub(r"<title>.*?</title>", "<title>Topic 5: Solved Problems (Mechanical Properties) — Aerospace Materials I</title>",
                  head, count=1, flags=re.S)
    head = head.replace("MAT-I · Topic 4", "MAT-I · Topic 5")
    tail = re.sub(r"\s*<!-- Scripts: i18n -->", "", tail)
    n = len(notes)
    nums = [x["n"] for x in notes]
    if n == TOTAL:
        scope = f"all {TOTAL} problems"
    elif nums == list(range(nums[0], nums[-1] + 1)):
        scope = f"problems {nums[0]} to {nums[-1]} of the {TOTAL}"
    else:
        scope = f"problems {', '.join(str(k) for k in nums)} of the {TOTAL}"
    intro = f'''<main class="problems-container">

    <!-- Page Intro Header -->
    <header class="page-intro">
      <h1>Topic 5: Solved Problems</h1>
      <p>
        Step-by-step solutions of {scope} of the official sheet on mechanical properties (Problems T5_MechanicalProperties: the tensile test, the elastic modulus, yield and tensile strength, ductility, resilience, true stress and strain, thermal stress and hardness, from Sessions 11 and 12), written in four phases. The sheet has no worked solutions, only a numeric key for most items, so every solution is derived here and compared with that key.
      </p>
    </header>

'''
    cards = "\n".join(card(x, figure) for x in notes)
    page = head + intro + cards + "\n  </main>\n\n" + tail
    cfg_links = json.loads(sl.CONFIG.read_text(encoding="utf-8"))
    if PAGE in cfg_links["pages"]:
        page = sl.build_page(PAGE, page, cfg_links, sl.load_json(sl.ANCHORS, {}), {})
    return page, figure


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if the page or a figure is out of date")
    args = ap.parse_args(argv)
    page, figs = build_page()
    path = REPO / PAGE
    current = path.read_text(encoding="utf-8") if path.exists() else None
    stale = [PAGE] if current != page else []
    if args.check:
        stale += figs.reg.stale(REPO)
        for s in stale:
            print(f"build_materials_problems: stale {s} (run python tools/build_materials_problems.py)", file=sys.stderr)
        return 1 if stale else 0
    for rel in figs.reg.write(REPO):
        print(f"build_materials_problems: wrote {rel}")
    if stale:
        path.write_text(page, encoding="utf-8", newline="\n")
        print(f"build_materials_problems: wrote {PAGE}")
    print("build_materials_problems: page up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
