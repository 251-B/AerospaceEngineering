#!/usr/bin/env python3
"""Build the Engineering Mechanics official problem pages (subjects/engineering-mechanics/problemas/topic-N.html) from the vault.

Per problem, two vault notes are the source of truth:

    vault/03 - Engineering Mechanics/Problem Set - Topic N ....md    statement (verbatim from Problems.pdf)
    vault/03 - Engineering Mechanics/Solution Set - Topic N ....md   worked solution, one "### " section per step

and tools/mech_problems.json holds what the notes do not: the card title, the badge, the credit line and the
structure version of each solution (3 = the lecturer's order, 2 = legacy "### Phase N" layout kept until a topic is
migrated, 1 = older legacy layout). The page never shows the word "Phase": each section is a block with its heading.

Statement note ("## 📌 Problem NN: title"): paragraphs, one-line $$ formulas (consecutive ones share a block),
"![[attachments/EM/<name>.png]]" followed by "*Figure: <caption> Source: Problems.pdf, p. N.*", "* **(a)** question"
items and "> [!note]" callouts. "*(Taken from ...)*" lines are dropped (the credit is in the JSON).

Solution note: "### heading" sections (structure 3) or "### Phase N: heading" (legacy); inside, "#### " and "##### " sub-headings, "* " bullets (a bullet that
starts with **Pedagogical Justification:** becomes a justification box), one-line or multi-line $$ formulas, tables
and "> [!warning] Title" callouts (shown as note banners). A line "![[attachments/EM-SOL/<name>.svg]]" embeds a deduction
figure drawn by tools/figures/em_solutions.py (inline SVG in a diagram card, numbered per problem, with its caption);
the vault copy is written to vault/attachments/EM-SOL/ by this tool.

Structure 3 (the lecturer's order, AGENTS.md "Problem-solving standard") requires these "### " sections, in this order:
    Reference Frames, Bases and Coordinates
    Change of Basis and Position Vector
    Kinematics
    Forces and Equations of Motion        (optional: left out when the problem has no dynamics)
    Answers and Checks                    (must contain "Check against the official key")
and no "Phase" word anywhere in the solution.

Structure 4 (rigid body, "rb-NN" ids, topics 6-8) requires these "### " sections, all six, in this order (a section
may be a single sentence saying that it does not apply to the problem):
    Reference Frames, Bases and Degrees of Freedom
    Change of Basis, Position Vectors and Constraint Kinematics
    Center of Mass and Inertia Tensor
    Linear Momentum, Angular Momentum and Kinetic Energy
    Free-Body Diagram and Equations of Motion
    Answers and Checks                    (must contain "Check against the official key" or "Limiting cases")
and no "Phase" word. Notes: "## 📌 Problem RB-NN: title" (statement) and "## Problem RB-NN: title" (solution); card id
"rb-NN", visible number "RB NN"; a statement may carry several figures (T6-RB04-figure.png, T8-RB20-figure-b.png).
The JSON entry has "group" (A-G); rigid body pages group the cards under <h2 id="group-a"> headings (GROUPS).

Derivation boxes (tools/derivation.py): a solution callout "> [!derivation] Title" (Law, Source, development, boxed
result, Units, Meaning) is rendered as <div class="derivation-box">; a figure embed inside it is numbered like any other.
Gate no-inline-calc: for structure 3 and 4 the rendered solution goes through derivation.gate (no calculation in prose
outside a box); an error unless the JSON entry has "boxed": false (legacy structure-3 solutions; not allowed with
structure 4). Statements are never gated. A run prints how many problems are structure 2, "boxed": false and fully boxed.

Simulator: "> [!example] Interactive simulator" followed by "> sim: {json}" becomes
<div class="m3-sim" data-archetype data-config>; one per problem; pages with one load mechanics-3d-sim.css/.js. Every page
loads derivation-box.css. All are inserted before assets/css/responsive.css, which stays the last stylesheet.

JSON extras: "badges": [...] adds badges next to "badge". Topics 6-8 come from EXPECTED; a topic whose notes do not exist
yet is skipped with a notice; a missing page is created from the head, header, banner and footer of topic-5.html.

Structure 2 (course order, Notes.pdf chapter 7) requires:
    Phase 1: Constraints, Degrees of Freedom & Coordinates
    Phase 2: Reference Frames & Vector Bases
    Phase 3: Derivation, with the sub-headings "#### 3.1 Kinematics", "#### 3.2 Forces", "#### 3.3 Equations of Motion"
             and "#### 3.4 Integration and Answers" (3.2 and 3.3 may be a single "Not applicable" line)
    Phase 4: Interpretation & Checks, containing "Check against the official key"

The page keeps its own <head>, header, banner and navigation; only the cards (from the first "<!-- Problem" comment to
<div class="article-nav">) are rewritten. The PDF deep links of tools/source_links.py are NOT applied here (run that
tool afterwards), so --check compares the page with its links stripped.

Usage:
    python tools/build_mech_problems.py            # rewrite the five pages
    python tools/build_mech_problems.py --check    # exit 1 if a page is stale or a note is invalid
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
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import build_topic_pages as bt  # noqa: E402
import derivation as der  # noqa: E402
import source_links as sl  # noqa: E402
from figures import em_solutions as emsol  # noqa: E402

VAULT = REPO / "vault" / "03 - Engineering Mechanics"
SUBJECT = REPO / "subjects" / "engineering-mechanics" / "problemas"
META = TOOLS / "mech_problems.json"
FIG_DIR = REPO / "vault" / "attachments" / "EM"
SET_NAMES = {
    1: "Topic 1 Particle Kinematics",
    2: "Topic 2 Point Particle Dynamics",
    3: "Topic 3 Constraints and Reaction Forces",
    4: "Topic 4 Angular Momentum and Central Forces",
    5: "Topic 5 Relative Motion",
    6: "Topic 6 Rigid Body Kinematics and Inertia",
    7: "Topic 7 Rigid Body Momentum, Energy and Dynamics",
    8: "Topic 8 Constraints, Rolling, Multibody and Torque-Free Motion",
}
EXPECTED = {1: 6, 2: 10, 3: 12, 4: 3, 5: 20, 6: 8, 7: 8, 8: 26}
RB_TOPICS = {
    6: ("Kinematics of Rigid Bodies and Inertia Properties", "Topic 5: Relative Motion"),
    7: ("Momentum, Kinetic Energy and Rigid Body Dynamics", "Topic 6: Kinematics of Rigid Bodies and Inertia Properties"),
    8: ("Constraints, Rolling Motion, Multibody Systems and Torque-Free Motion",
        "Topic 7: Momentum, Kinetic Energy and Rigid Body Dynamics"),
}
GROUPS = {
    "A": "Rigid body kinematics, Euler angles and the instantaneous axis of rotation",
    "B": "Mass geometry, Steiner's theorem and principal axes",
    "C": "Linear momentum, angular momentum and kinetic energy",
    "D": "Planar and 3D rigid body dynamics, equilibrium and linearized oscillations",
    "E": "Rolling with and without slip, unilateral constraints and lift-off",
    "F": "Multibody systems and exploded views",
    "G": "Torque-free motion, Poinsot's construction and gyroscopes",
}
ARCHETYPES = ("curvilinear-3d", "rotating-wire-groove", "oscillator-phase", "rb-euler-kinematics",
              "rb-inertia-principal", "rb-planar-dynamics", "rb-rolling-contact", "rb-gyro-multibody")
STEPS_V4 = [
    "Reference Frames, Bases and Degrees of Freedom",
    "Change of Basis, Position Vectors and Constraint Kinematics",
    "Center of Mass and Inertia Tensor",
    "Linear Momentum, Angular Momentum and Kinetic Energy",
    "Free-Body Diagram and Equations of Motion",
    "Answers and Checks",
]
ASSET_CSS = '../../../assets/css/'
ASSET_JS = '../../../assets/js/'
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆✅❌]")

PHASES_V2 = [
    "Constraints, Degrees of Freedom & Coordinates",
    "Reference Frames & Vector Bases",
    "Derivation",
    "Interpretation & Checks",
]
SUB_V2 = ["3.1 Kinematics", "3.2 Forces", "3.3 Equations of Motion", "3.4 Integration and Answers"]
STEPS_V3 = [
    "Reference Frames, Bases and Coordinates",
    "Change of Basis and Position Vector",
    "Kinematics",
    "Forces and Equations of Motion",
    "Answers and Checks",
]
OPTIONAL_V3 = {"Forces and Equations of Motion"}
_SOLFIG = re.compile(r"!\[\[attachments/EM-SOL/([\w-]+)\.svg\]\]$")
USED = set()          # figures embedded by the solutions of this run
STYLE_ID = "em-solution-figures"
STYLE = f"""  <style id="{STYLE_ID}">
    /* Deduction figures of the worked solutions (written by tools/build_mech_problems.py) */
    :root {{ --text-faint: #8a94a6; }}
    .diagram-card {{ background: var(--bg-card, var(--bg-surface)); border: 1px solid var(--border-card, var(--border-subtle)); border-radius: 12px; padding: 16px; margin: 18px 0; text-align: center; }}
    .diagram-card svg {{ max-width: 100%; height: auto; }}
    .diagram-caption {{ font-family: var(--font-sans); font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; text-align: center; }}
  </style>
"""

H4 = 'style="font-size: 0.95rem; font-weight: 700; color: var(--accent); margin: 16px 0 8px;"'
H5 = 'style="font-size: 0.9rem; font-weight: 700; color: var(--text-secondary); margin: 12px 0 6px;"'
UL = 'style="margin: 8px 0 12px 20px; display: flex; flex-direction: column; gap: 6px;"'
P = 'style="margin-bottom: 10px;"'
TH = 'style="text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--border-strong); background: var(--bg-subtle);"'
TD = 'style="padding: 8px 10px; border-bottom: 1px solid var(--border-subtle);"'


# --------------------------------------------------------------------------- Markdown to HTML
def inl(text):
    """bt.inline plus literal <br> line breaks; a leading '1\\.' is an escaped number, not a list item."""
    text = re.sub(r"^(\d+)\\\.", r"\1.", text)
    return "<br>".join(bt.inline(part) for part in text.split("<br>"))


def split_cells(row):
    """Cells of a Markdown table row; a '|' inside a $...$ formula is not a separator."""
    row = row.strip()
    row = row[1:] if row.startswith("|") else row
    row = row[:-1] if row.endswith("|") else row
    cells, cur, in_math = [], "", False
    for ch in row:
        if ch == "$":
            in_math = not in_math
        if ch == "|" and not in_math:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def _table(rows):
    cells = [split_cells(r) for r in rows]
    head, data = cells[0], cells[2:]
    th = "".join(f"<th {TH}>{inl(c)}</th>" for c in head)
    trs = "".join("<tr>" + "".join(f"<td {TD}>{inl(c)}</td>" for c in r) + "</tr>" for r in data)
    return (f'<div style="overflow-x: auto; margin: 12px 0;"><table style="width: 100%; border-collapse: collapse; '
            f'font-size: 0.9rem;"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')


def _sublist(rows):
    """Nested <ul> from (indent, text) rows (children of one top-level bullet)."""
    def build(idx, indent):
        items, kind = [], rows[idx][2]
        while idx < len(rows) and rows[idx][0] >= indent:
            if rows[idx][0] > indent and items:
                child, idx = build(idx, rows[idx][0])
                items[-1] += child
                continue
            items.append(f"<li>{inl(rows[idx][1])}")
            idx += 1
        open_ = '<ol style="margin: 6px 0 6px 20px;">' if kind == "ol" else "<ul>"
        return open_ + "".join(x + "</li>" for x in items) + f"</{kind}>", idx
    out, idx = "", 0
    while idx < len(rows):
        chunk, idx = build(idx, rows[idx][0])
        out += chunk
    return out


def _math(lines, i):
    """Consume a $$ formula starting at lines[i]; return (html, next index)."""
    s = lines[i].strip()
    if s.endswith("$$") and len(s) > 4:
        return f'<div class="math-block">{html.escape(s, quote=False)}</div>', i + 1
    buf = [s]
    i += 1
    while i < len(lines):
        t = lines[i].strip()
        buf.append(t)
        i += 1
        if t.endswith("$$"):
            break
    return f'<div class="math-block">{html.escape(" ".join(buf), quote=False)}</div>', i


def _callout(lines, i):
    m = re.match(r"> \[!(\w+)\]\s*(.*)", lines[i])
    if m:
        title, inner = m.group(2).strip(), []
        i += 1
    else:
        title, inner = "", []
    while i < len(lines) and lines[i].startswith(">"):
        inner.append(lines[i][2:] if lines[i].startswith("> ") else lines[i][1:])
        i += 1
    body = "".join(f"<p {P}>{inl(' '.join(x.split()))}</p>" for x in "\n".join(inner).split("\n\n") if x.strip())
    head = f"<strong>{inl(title)}</strong>" if title else ""
    return f'<div class="note-banner">{head}{body}</div>', i


_BULLET = re.compile(r"^(\s*)[-*] (.*)$")


class Figures:
    """Turns the figure embeds of one solution into diagram cards, numbered per problem."""

    def __init__(self, pid, errors):
        self.pid, self.errors, self.count, self.used, self.sims = pid, errors, 0, [], 0

    def __call__(self, name):
        if name not in emsol.REG.web:
            self.errors.append(f"problem {self.pid}: unknown figure {name} (not drawn in tools/figures/em_solutions.py)")
            return ""
        self.count += 1
        self.used.append(name)
        cap = inl(html.unescape(emsol.REG.captions[name]))
        return (f'<div class="diagram-card">\n{emsol.REG.web[name]}\n'
                f'<div class="diagram-caption">Figure {self.count}. {cap}.</div>\n</div>')


def render_sim(block, ctx):
    """HTML of an '[!example] Interactive simulator' callout (block: its lines without the '> ' prefix)."""
    raw = next((ln.strip()[4:].strip() for ln in block[1:] if ln.strip().startswith("sim:")), None)
    if raw is None:
        ctx.errors.append(f"problem {ctx.pid}: simulator callout without a 'sim: {{json}}' line")
        return ""
    try:
        cfg = json.loads(raw)
        if not isinstance(cfg, dict):
            raise ValueError("not an object")
    except ValueError as exc:
        ctx.errors.append(f"problem {ctx.pid}: invalid simulator JSON ({exc})")
        return ""
    arche = cfg.pop("archetype", None)
    if arche not in ARCHETYPES:
        ctx.errors.append(f"problem {ctx.pid}: unknown simulator archetype {arche!r}")
        return ""
    ctx.sims += 1
    if ctx.sims > 1:
        ctx.errors.append(f"problem {ctx.pid}: more than one simulator")
        return ""
    data = html.escape(json.dumps(cfg, separators=(",", ":"), ensure_ascii=False), quote=True)
    return (f'<div class="m3-sim" data-archetype="{arche}" data-config=\'{data}\'>'
            '<p class="m3-fallback">Interactive geometry simulator: it needs JavaScript. '
            'The figures above show the same geometry.</p></div>')


def render_solution(md, figs=None, errors=None):
    ctx = figs or Figures("?", errors if errors is not None else [])
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    ul = []

    def flush():
        if ul:
            out.append(f"<ul {UL}>\n" + "\n".join(ul) + "\n</ul>")
            ul.clear()

    while i < n:
        line = lines[i]
        s = line.strip()
        if not s or s == "---":
            i += 1
            continue
        mf = _SOLFIG.match(s)
        if mf:
            flush()
            out.append(figs(mf.group(1)) if figs else "")
            i += 1
            continue
        m = re.match(r"(#{4,6}) (.*)", line)
        if m:
            flush()
            tag, sty = ("h4", H4) if len(m.group(1)) == 4 else ("h5", H5)
            out.append(f"<{tag} {sty}>{inl(m.group(2))}</{tag}>")
            i += 1
            continue
        if s.startswith("$$"):
            flush()
            h, i = _math(lines, i)
            out.append(h)
            continue
        if line.startswith("|"):
            flush()
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_table(rows))
            continue
        if line.startswith(">") and der.is_start(line):
            flush()
            block, i = der.take(lines, i)
            box, errs = der.parse(block)
            ctx.errors.extend(f"problem {ctx.pid}: {e}" for e in errs)

            def box_fig(val, ctx=ctx):
                folder, fname = val
                if folder != "EM-SOL" or not fname.endswith(".svg"):
                    ctx.errors.append(f"problem {ctx.pid}: figure {folder}/{fname} in a box must be attachments/EM-SOL/<name>.svg")
                    return ""
                return figs(fname[:-4]) if figs else ""
            out.append(der.render(box, inl, figure=box_fig))
            continue
        if line.startswith(">") and re.match(r">\s*\[!example\]\s*Interactive simulator", line):
            flush()
            block, i = der.take(lines, i)
            out.append(render_sim(block, ctx))
            continue
        if line.startswith(">"):
            flush()
            h, i = _callout(lines, i)
            out.append(h)
            continue
        mo = re.match(r"^(\d+)\. (.*)$", line)
        if mo:
            flush()
            items = []
            while i < n and re.match(r"^\d+\. ", lines[i]):
                item = re.sub(r"^\d+\. ", "", lines[i]).strip()
                items.append(f"<li>{inl(item)}</li>")
                i += 1
            out.append(f"<ol {UL}>\n" + "\n".join(items) + "\n</ol>")
            continue
        m = _BULLET.match(line)
        if m and not m.group(1):
            top = m.group(2)
            i += 1
            kids = []
            tail = []
            while i < n:
                nxt = lines[i]
                ns = nxt.strip()
                if not ns:
                    j = i
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and (lines[j].startswith("  ") or _BULLET.match(lines[j]) and not _BULLET.match(lines[j]).group(1)) and not lines[j].strip().startswith("#"):
                        i = j
                        continue
                    break
                mb = _BULLET.match(nxt)
                if mb and not mb.group(1):
                    break
                if nxt.startswith("  ") and ns.startswith("$$"):
                    h, i = _math(lines, i)
                    tail.append(h)
                elif mb:
                    kids.append((len(mb.group(1)), mb.group(2), "ul"))
                    i += 1
                elif re.match(r"^\s+\d+\. ", nxt):
                    mn = re.match(r"^(\s+)\d+\. (.*)$", nxt)
                    kids.append((len(mn.group(1)), mn.group(2), "ol"))
                    i += 1
                elif nxt.startswith("  "):
                    if tail or kids:
                        tail.append(f"<p {P}>{inl(ns)}</p>")
                    else:
                        top += " " + ns
                    i += 1
                else:
                    break
            if top.startswith("**Pedagogical Justification:**"):
                flush()
                out.append(f'<div class="justification-box">{inl(top)}{_sublist(kids) if kids else ""}</div>')
            else:
                ul.append(f"<li>{inl(top)}{_sublist(kids) if kids else ''}</li>")
            if tail:
                flush()
                out.extend(tail)
            continue
        flush()
        para = [s]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"(\$\$|\||>|#|[-*] |\s*[-*] |\d+\. )", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p {P}>{inl(' '.join(para))}</p>")
    flush()
    return "\n".join(out)


def render_statement(md, pid, errors, figures=None):
    """(statement_html, figure_name): text blocks and question lists in the order of the note."""
    lines = md.split("\n")
    segs = []
    i, n = 0, len(lines)
    math = []
    figure = None

    def add(kind, h):
        if segs and segs[-1][0] == kind:
            segs[-1][1].append(h)
        else:
            segs.append((kind, [h]))

    def flush_math():
        if math:
            add("t", '<div class="math-block">\n' + "\n".join(math) + "\n</div>")
            math.clear()

    para = []

    def flush_para():
        if para:
            add("t", f"<p>{inl(' '.join(para))}</p>")
            para.clear()

    while i < n:
        line = lines[i]
        s = line.strip()
        if not s or s == "---":
            flush_para()
            flush_math()
            i += 1
            continue
        mf = re.match(r"!\[\[attachments/EM/([\w.-]+)\]\]$", s)
        if mf:
            flush_para()
            flush_math()
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            cap = lines[j].strip() if j < n else ""
            mc = re.match(r"\*Figure: (.*?)\s*Source: (Problems\.pdf, pp?\. \d+(?:\s*[-–]\s*\d+)?)\.\*$", cap)
            if mc:
                alt, src = mc.group(1), mc.group(2)
                i = j + 1
            else:
                errors.append(f"problem {pid}: figure {mf.group(1)} needs a '*Figure: ... Source: Problems.pdf, p. N.*' line")
                alt, src = "figure", "Problems.pdf"
                i += 1
            figure = mf.group(1)
            if figures is not None:
                figures.append(figure)
            add("t", 
                f'<figure class="statement-figure"><img src="../../../vault/attachments/EM/{figure}" '
                f'alt="{html.escape(alt)}" loading="lazy" style="max-width:100%;height:auto;display:block;margin:12px auto;'
                f'background:#fff;border-radius:8px;padding:8px"><figcaption>Figure: {inl(alt)} ({src}).</figcaption></figure>')
            continue
        if re.match(r"^\*\(Taken from [^)]*\)\*\.?$", s):
            flush_para()
            i += 1
            continue
        mq = re.match(r"^[-*] \*\*(\(?[A-Za-z0-9]+\)?)\*\*[:.]?\s*(.*)$", line)
        if mq:
            flush_para()
            flush_math()
            text = mq.group(2)
            i += 1
            while i < n and lines[i].startswith("  ") and lines[i].strip():
                text += " " + lines[i].strip()
                i += 1
            add("q", 
                f'<li class="question-item">\n<span class="question-label">{inl(mq.group(1))}</span>\n'
                f'<div class="question-text">{inl(text)}</div>\n</li>')
            continue
        if line.startswith(">"):
            flush_para()
            flush_math()
            h, i = _callout(lines, i)
            add("t", h)
            continue
        if s.startswith("$$"):
            flush_para()
            math.append(html.escape(s, quote=False))
            i += 1
            continue
        flush_math()
        para.append(s)
        i += 1
    flush_para()
    flush_math()
    out = []
    for kind, items in segs:
        body = "\n".join(items)
        if kind == "t":
            out.append(f'      <div class="problem-statement">\n{body}\n      </div>')
        else:
            out.append(f'      <ul class="questions-list">\n{body}\n      </ul>')
    return "\n".join(out), figure


# --------------------------------------------------------------------------- notes
def read_note(kind, topic):
    path = VAULT / f"{kind} - {SET_NAMES[topic]}.md"
    return bt.strip_frontmatter(path.read_text(encoding="utf-8"))


def split_problems(md):
    """{id: (heading_title, body)} for every '## ... Problem NN: title' (id 'NN') or 'Problem RB-NN: title' (id 'rb-NN') section."""
    out = {}
    parts = re.split(r"\n(?=## [^\n]*Problem (?:RB-)?\d+:)", md)
    for part in parts:
        m = re.match(r"## [^\n]*Problem (RB-)?(\d+):\s*(.*)\n", part)
        if not m:
            continue
        body = part[m.end():]
        out[("rb-" if m.group(1) else "") + m.group(2).zfill(2)] = (m.group(3).strip(), body)
    return out


def split_phases(body, pid):
    """[(n, heading, markdown)] for the '### Phase N: heading' sections of a solution body."""
    parts = re.split(r"\n(?=### Phase \d)", "\n" + body)
    out = []
    for part in parts:
        m = re.match(r"\s*### Phase (\d+):\s*(.*)\n", part)
        if m:
            out.append((int(m.group(1)), m.group(2).strip(), part[m.end():]))
    return out


def split_sections(body):
    """[(n, heading, markdown)] for the '### heading' sections of a structure-3 solution body."""
    parts = re.split(r"\n(?=### )", "\n" + body)
    out = []
    for part in parts:
        m = re.match(r"\s*### (.*)\n", part)
        if m:
            out.append((len(out) + 1, m.group(1).strip(), part[m.end():]))
    return out


def validate_v3(pid, sections, body, errors):
    heads = [h for _, h, _ in sections]
    want = [h for h in STEPS_V3 if h in heads or h not in OPTIONAL_V3]
    if heads != want:
        errors.append(f"problem {pid}: sections are {heads}, expected {want}")
        return
    if "Check against the official key" not in sections[-1][2]:
        errors.append(f"problem {pid}: 'Answers and Checks' lacks 'Check against the official key'")
    if re.search(r"\bPhase\b", body):
        errors.append(f"problem {pid}: the word 'Phase' appears in a structure-3 solution")


def validate_v4(pid, sections, body, errors):
    heads = [h for _, h, _ in sections]
    if heads != STEPS_V4:
        errors.append(f"problem {pid}: sections are {heads}, expected {STEPS_V4}")
        return
    for _, head, md in sections:
        if not md.strip():
            errors.append(f"problem {pid}: section '{head}' is empty (write a sentence saying it does not apply)")
    last = sections[-1][2]
    if "Check against the official key" not in last and not re.search(r"limiting cases", last, re.I):
        errors.append(f"problem {pid}: 'Answers and Checks' lacks 'Check against the official key' or 'Limiting cases'")
    if re.search(r"\bPhase\b", body):
        errors.append(f"problem {pid}: the word 'Phase' appears in a structure-4 solution")


def validate(pid, phases, structure, errors):
    nums = [p[0] for p in phases]
    if nums != [1, 2, 3, 4]:
        errors.append(f"problem {pid}: solution phases are {nums}, expected [1, 2, 3, 4]")
        return
    if structure < 2:
        return
    for (n, head, md), want in zip(phases, PHASES_V2):
        if head != want:
            errors.append(f"problem {pid}: Phase {n} heading is '{head}', expected '{want}'")
    p3 = phases[2][2]
    heads = re.findall(r"^#### (.*)$", p3, re.M)
    last = -1
    for sub in SUB_V2:
        if sub not in heads:
            errors.append(f"problem {pid}: Phase 3 lacks the sub-heading '#### {sub}'")
        else:
            idx = heads.index(sub)
            if idx < last:
                errors.append(f"problem {pid}: Phase 3 sub-heading '{sub}' is out of order")
            last = idx
    if "Check against the official key" not in phases[3][2]:
        errors.append(f"problem {pid}: Phase 4 lacks 'Check against the official key'")


def card_html(pid, meta, stmt_md, sol_md, errors):
    figures = []
    statement, _ = render_statement(stmt_md, pid, errors, figures)
    for fig in figures:
        if not (FIG_DIR / fig).exists():
            errors.append(f"problem {pid}: missing figure vault/attachments/EM/{fig}")
    structure = meta.get("structure", 1)
    if structure == 4 and meta.get("boxed") is False:
        errors.append(f"problem {pid}: \"boxed\": false is not allowed with structure 4")
    if structure >= 3:
        phases = split_sections(sol_md)
        (validate_v4 if structure == 4 else validate_v3)(pid, phases, sol_md, errors)
    else:
        phases = split_phases(sol_md, pid)
        validate(pid, phases, meta.get("structure", 1), errors)
    figs = Figures(pid, errors)
    blocks = []
    for n, head, md in phases:
        # "phase-block" is an internal class (Ask AI, the close bar and the print layout use it); no label is shown
        blocks.append(
            f'<div class="phase-block">\n'
            f'<h3 class="phase-heading">{inl(head)}</h3>\n{render_solution(md, figs)}\n</div>')
    USED.update(figs.used)
    solution_html = "".join(blocks)
    if structure >= 3 and meta.get("boxed") is not False:
        errors.extend(f"problem {pid}: {e}" for e in der.gate(solution_html))
    credit = f" {meta['source_note']}" if meta.get("source_note") else ""
    rb = pid.startswith("rb-")
    card_id = pid if rb else f"prob-{pid}"
    label = "Problem RB " + pid[3:] if rb else f"Problem {pid}"
    badge = f'<span class="problem-badge">{inl(meta["badge"])}</span>'
    if meta.get("badges"):
        badge = ('<span style="display: flex; flex-wrap: wrap; gap: 6px; justify-content: flex-end;">' + badge
                 + "".join(f'<span class="problem-badge">{inl(b)}</span>' for b in meta["badges"]) + "</span>")
    return f'''    <!-- Problem {pid} -->
    <div class="problem-card" id="{card_id}">
      <div class="problem-header">
        <div class="problem-title-area">
          <div class="problem-num">{label}</div>
          <h2 class="problem-title">{inl(meta["title"])}</h2>
        </div>
        {badge}
      </div>
{statement}
      <!-- Analytical Solution -->
      <details class="solution-details">
        <summary class="solution-summary">
          <span>Worked Solution</span>
          <span style="font-family: var(--font-mono); font-size: 0.8rem;">[ Click to Expand ]</span>
        </summary>
        <div class="solution-content">
{solution_html}
        </div>
      </details>

      <div class="problem-footer">
        <span class="status-solved">Worked Solution</span>
        <span class="source-tag">Source: Problems.pdf{html.escape(credit)}</span>
      </div>
    </div>

'''


def load_meta():
    return json.loads(META.read_text(encoding="utf-8"))


def notes_exist(topic):
    return all((VAULT / f"{kind} - {SET_NAMES[topic]}.md").exists() for kind in ("Problem Set", "Solution Set"))


def new_page(topic):
    """Page of a rigid body topic that has none yet: head, header, banner and footer of topic-5.html."""
    title, prev_title = RB_TOPICS[topic]
    text = sl.strip_links((SUBJECT / "topic-5.html").read_text(encoding="utf-8"))
    text = re.sub(r"<title>.*?</title>", lambda m: f"<title>Topic {topic}: {title} - Problems | Mechanics Applied to Aerospace Engineering</title>", text, count=1)
    text = re.sub(r'<h1 class="article-title">.*?</h1>', lambda m: f'<h1 class="article-title">Topic {topic}: {title} - Problem Sets</h1>', text, count=1, flags=re.S)
    intro = ("<strong>Statements and solutions:</strong> These are the rigid body problems of Problems.pdf section 2, "
             "solved in the lecturer's order: frames, bases and degrees of freedom; change of basis, position vectors and constraint "
             "kinematics; centre of mass and inertia tensor; momentum and energy; free-body diagram and equations of motion; answers and checks.")
    text = re.sub(r'<div class="note-banner">.*?</div>', lambda m: f'<div class="note-banner">\n      {intro}\n    </div>', text, count=1, flags=re.S)
    text = re.sub(r'\n?[ \t]*<style id="em-solution-figures">.*?</style>', "", text, flags=re.S)
    nxt = ""
    if topic + 1 in RB_TOPICS and notes_exist(topic + 1):   # no dead link while the next topic is not written
        nxt = (f'      <a href="topic-{topic + 1}.html" class="nav-btn" style="text-align: right;">\n'
               f'        <span class="nav-btn-label">Next Topic →</span>\n'
               f'        <span class="nav-btn-title">Topic {topic + 1}: {RB_TOPICS[topic + 1][0]}</span>\n      </a>\n')
    nav = (f'    <div class="article-nav">\n      <a href="topic-{topic - 1}.html" class="nav-btn">\n'
           f'        <span class="nav-btn-label">← Previous Topic</span>\n        <span class="nav-btn-title">{prev_title}</span>\n      </a>\n'
           f'      <a href="../teoria/topic-{topic}.html" class="nav-btn" style="text-align: center;">\n'
           f'        <span class="nav-btn-label">Theory Reference</span>\n        <span class="nav-btn-title">Review Topic Theory →</span>\n      </a>\n'
           f'      <a href="index.html" class="nav-btn" style="text-align: right;">\n'
           f'        <span class="nav-btn-label">Back to Syllabus →</span>\n        <span class="nav-btn-title">Problems Hub</span>\n      </a>\n'
           f'{nxt}    </div>\n')
    a = re.search(r"^[ \t]*<!-- (?:Problem|Group) ", text, re.M).start()
    b = re.search(r'^[ \t]*<div class="article-nav">', text, re.M)
    end_nav = re.search(r"</main>", text).start()
    footer = text[end_nav:]
    quote = re.search(r"\n[ \t]*<!-- Aerospace Motivational Quote Component -->.*?(?=</main>)", text[b.start():end_nav], re.S)
    middle = (quote.group(0) if quote else "\n")
    return text[:a] + "    <!-- Problem placeholder -->\n" + nav + middle + footer


def set_head_assets(page, with_sim, errors, topic):
    """derivation-box.css always; mechanics-3d-sim.css/.js when a card has a simulator; all before responsive.css."""
    page = re.sub(r'\n?[ \t]*<link rel="stylesheet" href="\.\./\.\./\.\./assets/css/(?:derivation-box|mechanics-3d-sim)\.css">', "", page)
    page = re.sub(r'\n?[ \t]*<script defer src="\.\./\.\./\.\./assets/js/mechanics-3d-sim\.js"></script>', "", page)
    tags = [f'<link rel="stylesheet" href="{ASSET_CSS}derivation-box.css">']
    if with_sim:
        tags += [f'<link rel="stylesheet" href="{ASSET_CSS}mechanics-3d-sim.css">',
                 f'<script defer src="{ASSET_JS}mechanics-3d-sim.js"></script>']
    anchor = re.search(r'^([ \t]*)<link rel="stylesheet" href="\.\./\.\./\.\./assets/css/responsive\.css">', page, re.M)
    if not anchor:
        errors.append(f"topic {topic}: the page has no link to assets/css/responsive.css")
        return page
    ins = "".join(f"{anchor.group(1)}{t}\n" for t in tags)
    return page[:anchor.start()] + ins + page[anchor.start():]


def group_head(letter):
    return (f'    <!-- Group {letter} -->\n    <h2 id="group-{letter.lower()}" style="font-family: var(--font-display); '
            f'font-size: 1.5rem; margin: 48px 0 16px; color: var(--text-heading);">{html.escape(GROUPS[letter])}</h2>\n\n')


def build_page(topic, meta, errors):
    rb = topic in RB_TOPICS
    ids = [k for k, v in meta.items() if v["topic"] == topic]
    stmts = split_problems(read_note("Problem Set", topic))
    sols = split_problems(read_note("Solution Set", topic))
    if rb:
        ids = [k for k in stmts if k in ids] + [k for k in sorted(ids) if k not in stmts]
        extra = sorted(k for k in list(stmts) + list(sols) if k not in meta)
        if extra:
            errors.append(f"topic {topic}: problems in the notes but not in mech_problems.json: {', '.join(sorted(set(extra)))}")
    else:
        ids.sort()
    if len(ids) != EXPECTED[topic]:
        errors.append(f"topic {topic}: {len(ids)} problems in mech_problems.json, expected {EXPECTED[topic]}")
    if rb:
        for pid in ids:
            if meta[pid].get("group") not in GROUPS:
                errors.append(f"problem {pid}: 'group' must be one of {''.join(GROUPS)}")
    cards, seen = [], None
    ordered = sorted(ids, key=lambda p: sorted(GROUPS).index(meta[p]["group"]) if meta[p].get("group") in GROUPS else 99) if rb else ids
    for pid in ordered:
        for label, src in (("Problem Set", stmts), ("Solution Set", sols)):
            if pid not in src:
                errors.append(f"problem {pid}: missing in {label} - {SET_NAMES[topic]}")
        if pid in stmts and pid in sols:
            if rb and meta[pid].get("group") != seen and meta[pid].get("group") in GROUPS:
                seen = meta[pid]["group"]
                cards.append(group_head(seen))
            cards.append(card_html(pid, meta[pid], stmts[pid][1], sols[pid][1], errors))
    path = SUBJECT / f"topic-{topic}.html"
    text = sl.strip_links(path.read_text(encoding="utf-8")) if path.exists() else new_page(topic)
    start = re.search(r"^[ \t]*<!-- (?:Problem|Group) ", text, re.M).start()
    end = re.search(r'^[ \t]*<div class="article-nav">', text, re.M).start()
    page = text[:start] + "".join(cards) + text[end:]
    if 'class="diagram-card"' in "".join(cards) and f'id="{STYLE_ID}"' not in page:
        page = page.replace("</head>", STYLE + "</head>", 1)
    page = set_head_assets(page, 'class="m3-sim"' in "".join(cards), errors, topic)
    if EMOJI.search("".join(cards)):
        errors.append(f"topic {topic}: emoji in the generated cards")
    return path, page


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if a page is stale or a note is invalid")
    args = ap.parse_args(argv)
    meta = load_meta()
    errors, stale, built = [], [], 0
    for name, warns in emsol.build().items():
        errors += [f"figure {name}: {w}" for w in warns]
    for rel in emsol.REG.stale(REPO):
        if args.check:
            errors.append(f"stale figure {rel} (run python tools/build_mech_problems.py)")
    if not args.check:
        for rel in emsol.REG.write(REPO):
            print(f"build_mech_problems: wrote {rel}")
    for topic in sorted(EXPECTED):
        if not notes_exist(topic):
            print(f"build_mech_problems: topic {topic}: notes '{SET_NAMES[topic]}' do not exist yet, skipped")
            continue
        built += 1
        path, want = build_page(topic, meta, errors)
        have = sl.strip_links(path.read_text(encoding="utf-8")) if path.exists() else None
        if have == want:
            continue
        stale.append(path)
        if not args.check and not errors:
            path.write_text(want, encoding="utf-8", newline="\n")
            print(f"build_mech_problems: wrote {path.relative_to(REPO)}")
    unused = sorted(set(emsol.FIGURES) - USED)
    if unused:
        errors.append(f"figures drawn but not used by any solution: {', '.join(unused)}")
    for e in errors:
        print(f"build_mech_problems: {e}", file=sys.stderr)
    counts = problem_counts(meta)
    print("build_mech_problems: {structure2} problems are structure 2, {legacy} are \"boxed\": false, {boxed} are fully boxed".format(**counts))
    if args.check:
        for p in stale:
            print(f"build_mech_problems: stale {p.relative_to(REPO)} (run python tools/build_mech_problems.py)", file=sys.stderr)
        return 1 if (stale or errors) else 0
    if errors:
        return 1
    print(f"build_mech_problems: {built} page(s) checked")
    return 0


def problem_counts(meta):
    structure2 = sum(1 for v in meta.values() if v.get("structure", 1) <= 2)
    legacy = sum(1 for v in meta.values() if v.get("structure", 1) >= 3 and v.get("boxed") is False)
    return {"structure2": structure2, "legacy": legacy, "boxed": len(meta) - structure2 - legacy}


if __name__ == "__main__":
    sys.exit(main())
