"""Shared helpers of the Advanced Maths problem-sheet author (Topic 3 part 2, Topic 4 parts 1 and 2).

The author scripts compute every result with SymPy, write the steps as Markdown (vault notes) and
register the phase portraits that tools/am_problems/build.py draws.  Nothing here touches the web pages.
"""
import json
import pathlib
import re

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
VAULT = ROOT / "vault" / "04 - Advanced Maths"
FIG_JSON = ROOT / "tools" / "am_problems" / "figures.json"

t = sp.Symbol("t", real=True)


# --------------------------------------------------------------------------- LaTeX
def tex(e):
    """LaTeX of a SymPy object (or number) with the portal's spacing conventions."""
    s = sp.latex(sp.sympify(e), fold_func_brackets=True)
    s = s.replace("{- ", "{-").replace("^{- ", "^{-")
    s = re.sub(r"\\sin \{", r"\\sin{", s)
    s = re.sub(r"\\cos \{", r"\\cos{", s)
    return s


def mat(rows, delim="p"):
    """pmatrix of the rows (lists of SymPy objects)."""
    body = r" \\ ".join(" & ".join(tex(x) for x in row) for row in rows)
    return r"\begin{%smatrix} %s \end{%smatrix}" % (delim, body, delim)


def vec(*xs):
    return mat([[x] for x in xs])


def rvec(*xs):
    """Column vector written inline, (a, b)^T."""
    return "(" + ", ".join(tex(x) for x in xs) + r")^{T}"


def signed(e, first=False):
    """' + e' or ' - |e|' for chaining sums (e a SymPy number or expression)."""
    e = sp.sympify(e)
    if e.could_extract_minus_sign():
        return ("-" if first else " - ") + tex(-e)
    return tex(e) if first else " + " + tex(e)


def eq_line(lhs, rhs):
    return f"{lhs} = {rhs}"


# --------------------------------------------------------------------------- note builder
class Doc:
    """A vault note under construction (Markdown with $...$ and $$...$$ maths)."""

    def __init__(self):
        self.out = []

    def raw(self, s):
        self.out.append(s)
        self.out.append("")

    def p(self, s):
        self.raw(s)

    def m(self, s):
        self.raw(f"$$ {s} $$")

    def h(self, level, s):
        self.raw("#" * level + " " + s)

    def ul(self, items):
        self.raw("\n".join(f"- {i}" for i in items))

    def ol(self, items):
        self.raw("\n".join(f"{n}. {i}" for n, i in enumerate(items, 1)))

    def table(self, head, rows):
        def safe(cell):
            # a pipe inside maths would split the cell (here and in Obsidian): write it as \vert
            return re.sub(r"\$[^$]+\$", lambda m: m.group(0).replace("|", "\\vert "), cell)
        lines = ["| " + " | ".join(safe(h) for h in head) + " |", "| " + " | ".join(":---" for _ in head) + " |"]
        lines += ["| " + " | ".join(safe(c) for c in r) + " |" for r in rows]
        self.raw("\n".join(lines))

    def callout(self, kind, title, body):
        """kind: info (note box), warning, result.  body: a string or a list of paragraphs/blocks."""
        parts = [body] if isinstance(body, str) else list(body)
        lines = [f"> [!{kind}] {title}"]
        for i, part in enumerate(parts):
            if i:
                lines.append(">")
            lines += ["> " + ln if ln else ">" for ln in part.split("\n")]
        self.raw("\n".join(lines))

    def fig(self, name, caption):
        self.raw(f"![[attachments/AM-PS/{name}.svg]]\n*{caption}*")

    def text(self):
        return "\n".join(self.out).rstrip() + "\n"


class Note:
    """One exercise: front matter plus a Doc per phase."""

    def __init__(self, sheet, num, title, pill, tags, source, difficulty="media"):
        self.sheet, self.num, self.title, self.pill = sheet, num, title, pill
        self.tags, self.source, self.difficulty = tags, source, difficulty
        self.statement = Doc()
        self.phases = []

    def phase(self, number, heading):
        d = Doc()
        self.phases.append((number, heading, d))
        return d

    @property
    def filename(self):
        clean = re.sub(r'[:?"<>|*/]', "", self.title).replace("  ", " ").strip()
        return f"Problem - {self.sheet['code']}-P{self.num} {clean}.md"

    def markdown(self):
        s = self.sheet
        fm = ["---", 'materia: "Advanced Maths"', f'tema: "{s["tema"]}"', f'origen: "{self.source} - Exercise {self.num}"',
              f"dificultad: {self.difficulty}", f'id: "{s["id_prefix"]}{self.num}"', f"pill: {json.dumps(self.pill, ensure_ascii=False)}", "tags:"]
        fm += [f"  - {t_}" for t_ in self.tags]
        fm += ["---", ""]
        out = fm + [f"# Problem {s['label']}.{self.num}: {self.title}", ""]
        out += [f"> Official exercise {self.num} of the sheet `{self.source}` (UC3M, Advanced Mathematics 2026/27). "
                f"Part of [[{s['index_note']}]]. Method and notation: [[{s['theory_note']}]].", "",
                "## Statement", ""]
        out += [self.statement.text().rstrip(), ""]
        for number, heading, doc in self.phases:
            out += [f"## Phase {number}: {heading}", "", doc.text().rstrip(), ""]
        return "\n".join(out).rstrip() + "\n"


# --------------------------------------------------------------------------- figures
FIGURES = {}


def register_figure(name, spec):
    FIGURES[name] = spec


def write_figures():
    """Merge the figures registered in this run into figures.json (so that a partial run keeps the others)."""
    FIG_JSON.parent.mkdir(parents=True, exist_ok=True)
    merged = json.loads(FIG_JSON.read_text(encoding="utf-8")) if FIG_JSON.exists() else {}
    merged.update(json.loads(json.dumps(FIGURES)))
    FIG_JSON.write_text(json.dumps(merged, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


# --------------------------------------------------------------------------- solving linear systems with the steps shown
def solve_steps(doc, eqs, unknowns, show_system=True):
    """Solve the linear system `eqs` (sympy Eq) by substitution, writing each step into `doc`.

    Returns the solution dict {unknown: value}.  Equations are numbered (1), (2), ... in the order given."""
    eqs = [sp.Eq(sp.expand(e.lhs), sp.expand(e.rhs)) for e in eqs]
    if show_system:
        doc.p("The linear system is")
        doc.m(r"\begin{aligned} " + r" \\ ".join(f"{tex(e.lhs)} &= {tex(e.rhs)} \\quad ({n})" for n, e in enumerate(eqs, 1)) + r" \end{aligned}")
    unk = list(unknowns)
    work = list(eqs)
    steps = []                      # (unknown, expression in the remaining unknowns), in the order solved
    guard = 0
    while work and guard < 30:
        guard += 1
        work = [e for e in work if sp.expand(e.lhs - e.rhs) != 0]
        if not work:
            break
        work.sort(key=lambda e: len([u for u in unk if (e.lhs - e.rhs).has(u)]))
        e = work[0]
        present = [u for u in unk if (e.lhs - e.rhs).has(u)]
        if not present:
            raise ValueError(f"inconsistent equation {e}")
        u = present[0]
        val = sp.expand(sp.solve(e, u)[0])
        if len(present) == 1:
            doc.p(f"${tex(e.lhs)} = {tex(e.rhs)}$ contains one unknown only, so ${tex(u)} = {tex(val)}$.")
        else:
            doc.p(f"Solve ${tex(e.lhs)} = {tex(e.rhs)}$ for ${tex(u)}$: ${tex(u)} = {tex(val)}$.")
        steps.append((u, val))
        unk.remove(u)
        new = []
        for other in work[1:]:
            nl, nr = sp.expand(other.lhs.subs(u, val)), sp.expand(other.rhs.subs(u, val))
            if (other.lhs - other.rhs).has(u):
                doc.p(f"Substitute in ${tex(other.lhs)} = {tex(other.rhs)}$: ${tex(nl)} = {tex(nr)}$.")
            new.append(sp.Eq(nl, nr))
        work = new
    sol = {}
    for u, val in reversed(steps):
        res = sp.expand(val.subs(sol))
        if val.free_symbols & set(sol):
            doc.p(f"Back-substitution: ${tex(u)} = {tex(val)} = {tex(res)}$.")
        sol[u] = res
    doc.p("Hence " + ", ".join(f"${tex(u)} = {tex(sol[u])}$" for u in unknowns if u in sol) + ".")
    return sol


# --------------------------------------------------------------------------- independent variable other than t
def rename_ivar(doc, start, new):
    """Rename the independent variable in the lines of `doc` from index `start` on (text written with t)."""
    pat = re.compile(r"(?<![A-Za-z\\])t(?![A-Za-z])")
    for i in range(start, len(doc.out)):
        s = doc.out[i]
        s = re.sub(r"kt(?![A-Za-z])", "k" + new, s)
        doc.out[i] = pat.sub(new, s)
