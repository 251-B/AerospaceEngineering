#!/usr/bin/env python3
"""Build the Engineering Mechanics Midterm 1 problem bank (subjects/engineering-mechanics/data/problems.json) from its vault notes.

Every note in vault/03 - Engineering Mechanics/Problem Bank/ named "Problem - Bank <ID> - <title>.md" is one bank item:
Pnn are 10-point exam-style problems (one per Midterm 1, 5 to 7 parts), Cnn are 2-point short conceptual questions in the
style of the final-exam questions on the same units. The note carries its metadata in the YAML frontmatter (bank_id, title,
category, archetype, level, unit, difficulty, points, time_minutes, tags, origen) and its content in "## " sections:

    ## Statement                       -> statement_html (may embed a figure: ![[attachments/EM-M1/<name>.svg]])
    ## Setup                           -> setup_html (optional: data, hypotheses, frames)
    ## (a) <prompt> [1.5 pts]          -> one subquestion; text under the heading is part of the prompt
    ### Hint / ### Checkpoint / ### Solution   -> hint_html, checkpoint_html, solution_html of that subquestion
    ## Interpretation                  -> interpretation_html (optional)

"#### " headings become step titles. Everything after the "**Back to:**" line is ignored. The figures are drawn by
tools/figures/em_midterm1.py (vault copies in vault/attachments/EM-M1/).

The tool checks the content (subquestion points add up, categories and points agree, every subquestion has hint, checkpoint
and solution, every embedded figure exists, the index note lists every item) and writes problems.json and problems.js (the
same data as window.AE_EM_BANK, with data/exam-blueprint.json as window.AE_EM_BLUEPRINT for the Exam Simulator). It also
fills the generated blocks of the Extra problems section: the hub (extra-problems/index.html), the page of conceptual
questions (midterm-1-theory.html) and the page of problems (midterm-1-problems.html).

Usage:
    python tools/build_mechanics_bank.py            # rewrite problems.json, problems.js, the figures and the pages
    python tools/build_mechanics_bank.py --check    # exit 1 if they are stale or a note is invalid
"""
import argparse
import sys
import html
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # warnings may contain Unicode minus signs
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_problem_bank as bpb  # noqa: E402
import build_topic_pages as bt  # noqa: E402
from figures import em_midterm1 as emfig  # noqa: E402

VAULT = REPO / "vault" / "03 - Engineering Mechanics"
BANK = VAULT / "Problem Bank"
OUT_DIR = REPO / "subjects" / "engineering-mechanics" / "data"
EXTRA = REPO / "subjects" / "engineering-mechanics" / "extra-problems"
INDEX_NOTE = "Problem Set - Engineering Mechanics Midterm 1 Problem Bank"  # must link every bank note

CATEGORIES = {"midterm_problem": 10.0, "conceptual_question": 2.0}
PAGES = {"midterm_problem": "midterm-1-problems.html", "conceptual_question": "midterm-1-theory.html"}
ARCHETYPES = {
    "kinematics": "Kinematics and coordinates",
    "dynamics": "Dynamics and energy",
    "constraints": "Constraints and reactions",
    "central-force": "Angular momentum and central forces",
    "relative-motion": "Relative motion and inertia forces",
    "oscillations": "Equilibrium and oscillations",
}
LEVELS = {"standard": "Standard exam level", "trap": "High difficulty / trap", "conceptual": "Conceptual / fast"}
UNITS = {1: "Unit 1 · Kinematics", 2: "Unit 2 · Particle dynamics", 3: "Unit 3 · Constraints and reactions",
         4: "Unit 4 · Angular momentum and central forces", 5: "Unit 5 · Relative motion"}
REQUIRED = ("bank_id", "title", "category", "archetype", "level", "unit", "difficulty", "points", "time_minutes", "tags", "origen")
_NAME = re.compile(r"Problem - Bank ([PC]\d{2}) - .+\.md$")
_SUB = bpb._SUB
_FIG = re.compile(r"!\[\[attachments/EM-M1/([\w-]+)\.svg\]\]")


class Figures:
    """Renders the figure embeds of one item as diagram cards, numbering them per item."""

    def __init__(self):
        self.reg = emfig.REG
        self.count = 0
        self.used = []

    def __call__(self, name):
        if name not in self.reg.web:
            raise bpb.BankError(f"unknown figure {name!r} (not drawn in tools/figures/em_midterm1.py)")
        self.count += 1
        self.used.append(name)
        cap = html.escape(html.unescape(self.reg.captions[name]), quote=False)
        return (f'<div class="diagram-card">\n{self.reg.web[name]}\n'
                f'<div class="diagram-caption">Figure {self.count}. {cap}.</div>\n</div>')


def render(lines, where, figs):
    while lines and not lines[-1].strip():
        lines.pop()
    out, chunk = [], []
    for line in lines + ["#### \x00"]:
        if line.startswith("#### "):
            if any(x.strip() for x in chunk):
                out.append(bt.blocks(chunk, figs))
            chunk = []
            title = line[5:].strip()
            if title != "\x00":
                out.append(f'<h4 class="step-title">{bt.inline(title)}</h4>')
        else:
            chunk.append(line)
    return "\n".join(out)


def parse_note(path):
    where = path.name
    m = _NAME.match(path.name)
    if not m:
        raise bpb.BankError(f"{where}: name must be 'Problem - Bank Pnn|Cnn - <title>.md'")
    meta, body = bpb.frontmatter(path.read_text(encoding="utf-8"), where)
    missing = [k for k in REQUIRED if k not in meta]
    if missing:
        raise bpb.BankError(f"{where}: frontmatter lacks {', '.join(missing)}")
    if meta["bank_id"] != m.group(1):
        raise bpb.BankError(f"{where}: bank_id {meta['bank_id']} does not match the file name")
    category = meta["category"]
    if category not in CATEGORIES:
        raise bpb.BankError(f"{where}: unknown category {category!r}")
    points = float(meta["points"])
    if points != CATEGORIES[category]:
        raise bpb.BankError(f"{where}: a {category} is worth {CATEGORIES[category]} points, not {points}")
    if (category == "midterm_problem") != meta["bank_id"].startswith("P"):
        raise bpb.BankError(f"{where}: P ids are problems, C ids are conceptual questions")
    if meta["archetype"] not in ARCHETYPES:
        raise bpb.BankError(f"{where}: unknown archetype {meta['archetype']!r}")
    if meta["level"] not in LEVELS:
        raise bpb.BankError(f"{where}: unknown level {meta['level']!r}")
    if meta["unit"] not in UNITS or meta["difficulty"] not in (1, 2, 3):
        raise bpb.BankError(f"{where}: unit must be 1-5 and difficulty 1-3")

    figs = Figures()
    body = body.split("**Back to:**")[0]
    parts = re.split(r"\n## ", "\n" + body)
    item = {
        "id": meta["bank_id"], "category": category, "archetype": meta["archetype"], "theme": meta["archetype"],
        "level": meta["level"], "unit": meta["unit"], "title": meta["title"], "difficulty": meta["difficulty"],
        "points": points, "time_minutes": meta["time_minutes"], "tags": [t for t in meta["tags"] if t != "problem-bank"],
        "official": bool(meta.get("official", False)), "source": meta["origen"],
        "vault_note": path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.name,
        "statement_html": None, "setup_html": None, "subquestions": [], "interpretation_html": None, "figures": [],
    }
    for part in parts[1:]:
        head, _, rest = part.partition("\n")
        head, lines = head.strip(), rest.split("\n")
        if head == "Statement":
            item["statement_html"] = render(lines, where, figs)
        elif head == "Setup":
            item["setup_html"] = render(lines, where, figs)
        elif head == "Interpretation":
            item["interpretation_html"] = render(lines, where, figs)
        elif _SUB.match(head):
            item["subquestions"].append(subquestion(head, rest, where, figs))
        else:
            raise bpb.BankError(f"{where}: unexpected section '## {head}'")
    item["figures"] = figs.used
    if not item["statement_html"]:
        raise bpb.BankError(f"{where}: no '## Statement' section")
    if not item["subquestions"]:
        raise bpb.BankError(f"{where}: no subquestions")
    labels = [s["label"] for s in item["subquestions"]]
    if labels != [chr(ord("a") + i) for i in range(len(labels))]:
        raise bpb.BankError(f"{where}: subquestions must be (a), (b), ... in order, got {labels}")
    total = round(sum(s["points"] for s in item["subquestions"]), 4)
    if total != points:
        raise bpb.BankError(f"{where}: subquestion points add up to {total}, not {points}")
    if "$$" in re.sub(r"\$\$.*?\$\$", "", body, flags=re.S):
        raise bpb.BankError(f"{where}: unbalanced $$ delimiters")
    return item


def subquestion(head, rest, where, figs):
    label, prompt, pts = _SUB.match(head).groups()
    blocks = re.split(r"\n### ", "\n" + rest)
    sub = {"label": label, "points": float(pts), "prompt_html": None,
           "hint_html": None, "checkpoint_html": None, "solution_html": None}
    intro = blocks[0].split("\n")
    sub["prompt_html"] = f"<p>{bt.inline(prompt)}</p>" + ("\n" + render(intro, where, figs) if any(x.strip() for x in intro) else "")
    for block in blocks[1:]:
        name, _, text = block.partition("\n")
        key = {"Hint": "hint_html", "Checkpoint": "checkpoint_html", "Solution": "solution_html"}.get(name.strip())
        if key is None:
            raise bpb.BankError(f"{where}: ({label}) has an unexpected '### {name.strip()}'")
        sub[key] = render(text.split("\n"), f"{where} ({label})", figs)
    for key in ("hint_html", "checkpoint_html", "solution_html"):
        if not sub[key]:
            raise bpb.BankError(f"{where}: ({label}) lacks its {key.split('_')[0]}")
    return sub


def check_blueprint(blueprint, items):
    parts = blueprint.get("parts", [])
    total = round(sum(p["count"] * p["points_each"] for p in parts), 4)
    if total != blueprint.get("total_points"):
        raise bpb.BankError(f"exam-blueprint.json: parts add up to {total}, not {blueprint.get('total_points')}")
    for part in parts:
        pool = [i for i in items if i["category"] == part["category"]]
        if any(i["points"] != part["points_each"] for i in pool):
            raise bpb.BankError(f"exam-blueprint.json: {part['id']} expects {part['points_each']}-point items")
        if len(pool) < 2 * part["count"]:
            raise bpb.BankError(f"exam-blueprint.json: {part['id']} needs at least {2 * part['count']} items in the bank")
        for a in part.get("selection_rules", {}).get("archetypes", []):
            if a not in ARCHETYPES or not any(i["archetype"] == a for i in pool):
                raise bpb.BankError(f"exam-blueprint.json: archetype {a!r} has no item in the bank")


def build(bank_dir=None):
    bank_dir = pathlib.Path(bank_dir or BANK)
    emfig.build()
    items = [parse_note(p) for p in sorted(bank_dir.glob("Problem - Bank *.md"))]
    ids = [i["id"] for i in items]
    dup = sorted({x for x in ids if ids.count(x) > 1})
    if dup:
        raise bpb.BankError(f"duplicate bank ids: {', '.join(dup)}")
    index = bank_dir / f"{INDEX_NOTE}.md"
    if index.is_file():
        listed = index.read_text(encoding="utf-8")
        unlisted = [p.stem for p in sorted(bank_dir.glob("Problem - Bank *.md")) if f"[[{p.stem}" not in listed]
        if unlisted:
            raise bpb.BankError(f"{INDEX_NOTE} does not list: {', '.join(unlisted)}")
    unused = sorted(set(emfig.FIGURES) - {f for i in items for f in i["figures"]})
    if unused and pathlib.Path(bank_dir) == BANK:
        raise bpb.BankError(f"figures drawn but not used by any note: {', '.join(unused)}")
    items.sort(key=lambda i: (i["id"][0] != "C", int(i["id"][1:])))
    data = {
        "_comment": "Generated by tools/build_mechanics_bank.py from vault/03 - Engineering Mechanics/Problem Bank/. Do not edit by hand.",
        "subject": "engineering-mechanics",
        "categories": {"midterm_problem": {"label": "Midterm problems", "points": 10.0},
                       "conceptual_question": {"label": "Conceptual questions", "points": 2.0}},
        "pages": PAGES,
        "archetypes": ARCHETYPES, "levels": LEVELS,
        "units": {str(k): v for k, v in UNITS.items()},
        "counts": {c: sum(i["category"] == c for i in items) for c in CATEGORIES},
        "items": items,
    }
    text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    js = ("/* Generated by tools/build_mechanics_bank.py (same data as problems.json). Do not edit by hand. */\n"
          f"window.AE_EM_BANK = {json.dumps(data, ensure_ascii=False)};\n")
    outputs = {}
    blueprint_path = OUT_DIR / "exam-blueprint.json"
    if pathlib.Path(bank_dir) == BANK and blueprint_path.is_file():
        blueprint = json.loads(blueprint_path.read_text(encoding="utf-8"))
        check_blueprint(blueprint, items)
        js += ("/* The exam structure of data/exam-blueprint.json, for the Exam Simulator. */\n"
               f"window.AE_EM_BLUEPRINT = {json.dumps(blueprint, ensure_ascii=False)};\n")
    outputs.update({OUT_DIR / "problems.json": text, OUT_DIR / "problems.js": js})
    if pathlib.Path(bank_dir) == BANK:
        for path, fn in ((HUB, render_hub), (THEORY_PAGE, render_theory), (PROBLEMS_PAGE, render_problems)):
            if path.is_file():
                outputs[path] = fn(path.read_bytes().decode("utf-8").replace("\r\n", "\n"), items)
    return outputs


# --------------------------------------------------------------------------- the Extra problems pages
HUB = EXTRA / "index.html"
THEORY_PAGE = EXTRA / "midterm-1-theory.html"
PROBLEMS_PAGE = EXTRA / "midterm-1-problems.html"
_PAGE_BLOCK = re.compile(r"(<!-- EXTRA-PROBLEMS:START[^>]*-->\n).*?(<!-- EXTRA-PROBLEMS:END -->)", re.S)
_HUB_BLOCK = re.compile(r"(<!-- EXTRA-HUB:START[^>]*-->\n).*?(<!-- EXTRA-HUB:END -->)", re.S)


def _pts(x):
    return f"{x:g} point" + ("" if x == 1 else "s")


def _card(item):
    is_q = item["category"] == "conceptual_question"
    tag = (f"{'Conceptual question' if is_q else 'Problem'} · {UNITS[item['unit']].split(' · ')[0]} · {_pts(item['points'])} · "
           f"{item['time_minutes']} min · {LEVELS[item['level']]}")
    out = [f'      <section class="problem-box" id="{item["id"]}">',
           f'        <span class="problem-tag">{html.escape(tag)}</span>',
           f'        <h4 class="problem-title">{html.escape(item["id"])} — {html.escape(item["title"])}</h4>',
           '        <div class="statement-box">', item["statement_html"], "        </div>"]
    if item["setup_html"]:
        out += ['        <div class="phase-block">', '          <h3 class="phase-title">Setup</h3>', item["setup_html"], "        </div>"]
    for sub in item["subquestions"]:
        out += ['        <div class="phase-block">',
                f'          <h3 class="phase-title">Part ({sub["label"]}) · {_pts(sub["points"])}</h3>',
                '          <div class="prompt">' + sub["prompt_html"] + "</div>",
                sub["solution_html"],
                '          <div class="result-callout"><div class="result-callout-title">'
                + ("Key points" if is_q else "Key results") + "</div>" + sub["checkpoint_html"] + "</div>",
                "        </div>"]
    if item["interpretation_html"]:
        out += ['        <div class="phase-block">', '          <h3 class="phase-title">Interpretation and checks</h3>',
                item["interpretation_html"], "        </div>"]
    out.append("      </section>")
    return "\n".join(out)


def _split(items):
    return ([i for i in items if i["category"] == "conceptual_question"],
            [i for i in items if i["category"] == "midterm_problem"])


def _fill(pattern, path, page, block):
    if not pattern.search(page):
        raise bpb.BankError(f"{path.relative_to(REPO).as_posix()} lacks its generated-block markers")
    return pattern.sub(lambda m: m.group(1) + block + m.group(2), page, count=1)


def render_theory(page, items):
    cases, _ = _split(items)
    block = "\n".join([
        f'      <p class="midterm-part-lead">{len(cases)} short conceptual questions on Units 1 to 5, in the style of the '
        'true/false questions of the final exams. Each is worth 2 points and asks for a justified answer. They are '
        'practice for the reasoning behind the Midterm 1 problem; the exam itself is one problem of 10 points, so these '
        'questions do not appear in the <a href="../simulator/index.html">Exam simulator</a>.</p>',
        "\n".join(_card(i) for i in cases),
    ]) + "\n"
    return _fill(_PAGE_BLOCK, THEORY_PAGE, page, block)


def render_problems(page, items):
    _, probs = _split(items)
    block = "\n".join([
        f'      <p class="midterm-part-lead">{len(probs)} exam-style problems on Units 1 to 5, written for this portal. '
        'The Midterm 1 papers of 2011 to 2024 are one problem of 10 points with 5 to 7 parts; the '
        '<a href="../simulator/index.html">Exam simulator</a> draws one of these and times it.</p>',
        "\n".join(_card(i) for i in probs),
    ]) + "\n"
    return _fill(_PAGE_BLOCK, PROBLEMS_PAGE, page, block)


def _hub_card(href, badge, title, desc, items, tags):
    rows = "\n".join(
        '          <li class="exercise-item">\n'
        f'            <span class="ex-num">{html.escape(i["id"])}:</span>\n'
        f'            <span class="ex-title">{html.escape(i["title"])}</span>\n'
        "          </li>" for i in items)
    chips = "\n".join(f'          <span class="meta-tag">{html.escape(t)}</span>' for t in tags)
    return "\n".join([
        f'      <a href="{href}" class="problem-card">',
        f'        <span class="card-badge">{html.escape(badge)}</span>',
        f'        <h2 class="card-title">{html.escape(title)}</h2>',
        f'        <p class="card-desc">{desc}</p>',
        "", '        <ul class="exercise-list">', rows, "        </ul>", "",
        '        <div class="topic-meta">', chips, "        </div>",
        "      </a>"])


def render_hub(page, items):
    cases, probs = _split(items)
    block = "\n".join([
        '    <section class="exam-block" id="midterm-1" aria-labelledby="midterm-1-title">',
        '      <h2 class="exam-block-title" id="midterm-1-title">1st Midterm</h2>',
        '      <p class="exam-block-lead">The first partial exam covers point-particle mechanics (Units 1 to 5) and is one '
        'problem of 10 points. Practise the problems on one page, the shorter conceptual questions on the other, or take '
        'a timed exam built from these items in the <a href="../simulator/index.html">Exam simulator</a>.</p>',
        '      <div class="problem-sets-grid">',
        _hub_card(THEORY_PAGE.name, "1st Midterm • Concepts", f"Conceptual Questions {cases[0]['id']} to {cases[-1]['id']}",
                  f"{len(cases)} short questions on Units 1 to 5, each worth 2 points: true or false with a justification, "
                  "reading a potential, frames and inertia forces, with the key points of every answer.", cases,
                  [f"{len(cases)} Conceptual Questions", "2 points each", "Units 1 to 5", "Key points per answer"]),
        "",
        _hub_card(PROBLEMS_PAGE.name, "1st Midterm • Problems", f"Exam-Style Problems {probs[0]['id']} to {probs[-1]['id']}",
                  f"{len(probs)} problems of 10 points with 5 to 7 parts, solved step by step with a technical sketch, "
                  "the key results of every part and the common mistakes of the exam.", probs,
                  [f"{len(probs)} Problems", "10 points each", "Technical sketches", "Verified with SymPy"]),
        "      </div>",
        "    </section>",
    ]) + "\n"
    return _fill(_HUB_BLOCK, HUB, page, block)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    try:
        outputs = build()
        stale_figs = emfig.REG.stale(REPO)
    except bpb.BankError as exc:
        print(f"build_mechanics_bank: {exc}")
        return 1
    stale = 0
    for path, content in outputs.items():
        current = path.read_bytes().decode("utf-8").replace("\r\n", "\n") if path.exists() else None
        if current != content:
            stale += 1
            if args.check:
                print("stale", path.relative_to(REPO).as_posix())
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content.encode("utf-8"))
                print("wrote", path.relative_to(REPO).as_posix())
    if stale_figs:
        stale += len(stale_figs)
        if args.check:
            for rel in stale_figs:
                print("stale", rel)
        else:
            for rel in emfig.REG.write(REPO):
                print("wrote", rel)
    data = json.loads(outputs[OUT_DIR / "problems.json"])
    print(f"build_mechanics_bank: {data['counts']['midterm_problem']} problems, "
          f"{data['counts']['conceptual_question']} conceptual questions")
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
