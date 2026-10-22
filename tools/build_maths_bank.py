#!/usr/bin/env python3
"""Build the Advanced Maths problem bank (subjects/advanced-maths/data/problems.json) from its vault notes.

Every note in vault/04 - Advanced Maths/Problem Bank/ named "Problem - Bank Pnn - <title>.md" is one exam-style problem
written for the bank. Its category says which exam it trains: midterm_1_problem (5 points, first partial: ODEs and linear
systems), midterm_2_problem (5 points, second partial: nonlinear systems, Fourier series, PDEs) or final_problem
(2.5 points, one of the four problems of the final). The note format is the one of tools/build_mechanics_bank.py:

    ## Statement / ## Setup / ## (a) <prompt> [1.5 pts] with ### Hint, ### Checkpoint, ### Solution / ## Interpretation

The tool checks the notes (frontmatter keys, categories and points, subquestion points add up, every subquestion has hint,
checkpoint and solution, balanced $$, the index note lists every item) and writes problems.json and problems.js (the same
data as window.AE_AM_BANK, plus the three exam blueprints of data/ as window.AE_AM_BLUEPRINT, AE_AM_BLUEPRINT_MT2 and
AE_AM_BLUEPRINT_FINAL for the Exam Simulator). It also fills the generated blocks of the Extra problems hub and of the
three exam pages (midterm-1-problems.html, midterm-2-problems.html, final-problems.html).

Usage:
    python tools/build_maths_bank.py            # rewrite problems.json, problems.js and the pages
    python tools/build_maths_bank.py --check    # exit 1 if they are stale or a note is invalid
    python tools/build_maths_bank.py --lint     # only validate the notes
"""
import argparse
import html
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_problem_bank as bpb  # noqa: E402
import build_mechanics_bank as emb  # noqa: E402  (shared note parser and page helpers)
import build_topic_pages as bt  # noqa: E402

VAULT = REPO / "vault" / "04 - Advanced Maths"
BANK = VAULT / "Problem Bank"
OUT_DIR = REPO / "subjects" / "advanced-maths" / "data"
EXTRA = REPO / "subjects" / "advanced-maths" / "extra-problems"
INDEX_NOTE = "Problem Set - Advanced Maths Problem Bank"

# category -> (points, page, exam label, blueprint file, window name)
EXAMS = {
    "midterm_1_problem": (5.0, "midterm-1-problems.html", "1st Midterm", "exam-blueprint.json", "AE_AM_BLUEPRINT"),
    "midterm_2_problem": (5.0, "midterm-2-problems.html", "2nd Midterm", "exam-blueprint-midterm-2.json", "AE_AM_BLUEPRINT_MT2"),
    "final_problem": (2.5, "final-problems.html", "Final exam", "exam-blueprint-final.json", "AE_AM_BLUEPRINT_FINAL"),
}
ARCHETYPES = {
    "ode-first-order-modeling": "First-order modelling",
    "ode-first-order-qualitative": "First-order qualitative analysis",
    "ode-second-order-reduction": "Reduction of order",
    "ode-second-order-undetermined-params": "Constant coefficients, Cauchy-Euler and forcing",
    "linear-systems-phase-portrait": "Linear systems and phase portraits",
    "nonlinear-systems-stability": "Nonlinear systems and stability",
    "fourier-series-convergence": "Fourier series and convergence",
    "pde-separation-laplace": "Laplace equation by separation",
    "pde-separation-heat-wave": "Heat and wave equations by separation",
    "sturm-liouville-eigenproblems": "Sturm-Liouville eigenproblems",
}
LEVELS = emb.LEVELS
UNITS = {1: "Unit 1 · Introduction and modelling", 2: "Unit 2 · First-order ODEs", 3: "Unit 3 · Second-order linear ODEs",
         4: "Unit 4 · Systems of ODEs", 5: "Unit 5 · Fourier series and separation of variables",
         6: "Unit 6 · Heat, wave and Laplace equations"}
REQUIRED = emb.REQUIRED
_NAME = re.compile(r"Problem - Bank (P\d{2}) - .+\.md$")
_EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def parse_note(path):
    where = path.name
    m = _NAME.match(path.name)
    if not m:
        raise bpb.BankError(f"{where}: name must be 'Problem - Bank Pnn - <title>.md'")
    text = path.read_text(encoding="utf-8")
    if _EMOJI.search(text):
        raise bpb.BankError(f"{where}: emojis are not allowed")
    meta, body = bpb.frontmatter(text, where)
    missing = [k for k in REQUIRED if k not in meta]
    if missing:
        raise bpb.BankError(f"{where}: frontmatter lacks {', '.join(missing)}")
    if meta["bank_id"] != m.group(1):
        raise bpb.BankError(f"{where}: bank_id {meta['bank_id']} does not match the file name")
    category = meta["category"]
    if category not in EXAMS:
        raise bpb.BankError(f"{where}: unknown category {category!r}")
    points = float(meta["points"])
    if points != EXAMS[category][0]:
        raise bpb.BankError(f"{where}: a {category} is worth {EXAMS[category][0]} points, not {points}")
    if meta["archetype"] not in ARCHETYPES:
        raise bpb.BankError(f"{where}: unknown archetype {meta['archetype']!r}")
    if meta["level"] not in LEVELS:
        raise bpb.BankError(f"{where}: unknown level {meta['level']!r}")
    if meta["unit"] not in UNITS or meta["difficulty"] not in (1, 2, 3):
        raise bpb.BankError(f"{where}: unit must be 1-6 and difficulty 1-3")

    body = body.split("**Back to:**")[0]
    # Display math written as "$$" / formula / "$$" on three lines becomes one line, which is what the shared parser reads.
    body = re.sub(r"(?m)^[ \t]*\$\$[ \t]*\n(.*?)\n[ \t]*\$\$[ \t]*$",
                  lambda mm: "$$" + " ".join(x.strip() for x in mm.group(1).split("\n")) + "$$", body, flags=re.S)
    item = {
        "id": meta["bank_id"], "category": category, "archetype": meta["archetype"], "theme": meta["archetype"],
        "level": meta["level"], "unit": meta["unit"], "title": meta["title"], "difficulty": meta["difficulty"],
        "points": points, "time_minutes": meta["time_minutes"], "tags": [t for t in meta["tags"] if t != "problem-bank"],
        "official": bool(meta.get("official", False)), "source": meta["origen"],
        "vault_note": path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.name,
        "statement_html": None, "setup_html": None, "subquestions": [], "interpretation_html": None,
    }
    try:
        for part in re.split(r"\n## ", "\n" + body)[1:]:
            head, _, rest = part.partition("\n")
            head, lines = head.strip(), rest.split("\n")
            if head in ("Statement", "Setup", "Interpretation"):
                item[f"{head.lower()}_html"] = emb.render(lines, where, None)
            elif emb._SUB.match(head):
                item["subquestions"].append(emb.subquestion(head, rest, where, None))
            else:
                raise bpb.BankError(f"{where}: unexpected section '## {head}'")
    except ValueError as exc:  # figure embeds: this bank has no figure module
        raise bpb.BankError(f"{where}: {exc}") from None
    if not item["statement_html"]:
        raise bpb.BankError(f"{where}: no '## Statement' section")
    labels = [s["label"] for s in item["subquestions"]]
    if not labels or labels != [chr(ord("a") + i) for i in range(len(labels))]:
        raise bpb.BankError(f"{where}: subquestions must be (a), (b), ... in order, got {labels}")
    total = round(sum(s["points"] for s in item["subquestions"]), 4)
    if total != points:
        raise bpb.BankError(f"{where}: subquestion points add up to {total}, not {points}")
    if "$$" in re.sub(r"\$\$.*?\$\$", "", body, flags=re.S):
        raise bpb.BankError(f"{where}: unbalanced $$ delimiters")
    return item


def check_blueprint(name, blueprint, items):
    parts = blueprint.get("parts", [])
    total = round(sum(p["count"] * p["points_each"] for p in parts), 4)
    if total != blueprint.get("total_points"):
        raise bpb.BankError(f"{name}: parts add up to {total}, not {blueprint.get('total_points')}")
    for part in parts:
        rules = part.get("selection_rules", {})
        pool = [i for i in items if i["category"] == part["category"] and i["unit"] in rules.get("units", UNITS)]
        if any(i["points"] != part["points_each"] for i in pool):
            raise bpb.BankError(f"{name}: {part['id']} expects {part['points_each']}-point items")
        if len(pool) < 2 * part["count"]:
            raise bpb.BankError(f"{name}: {part['id']} needs at least {2 * part['count']} items in the bank, has {len(pool)}")
        for a in rules.get("archetypes", []) + rules.get("must_archetypes", []):
            if a not in ARCHETYPES or not any(i["archetype"] == a for i in pool):
                raise bpb.BankError(f"{name}: archetype {a!r} has no item in {part['id']}")


def load_items(bank_dir=BANK):
    paths = sorted(pathlib.Path(bank_dir).glob("Problem - Bank *.md"))
    items = [parse_note(p) for p in paths]
    ids = [i["id"] for i in items]
    dup = sorted({x for x in ids if ids.count(x) > 1})
    if dup:
        raise bpb.BankError(f"duplicate bank ids: {', '.join(dup)}")
    index = pathlib.Path(bank_dir) / f"{INDEX_NOTE}.md"
    if not index.is_file():
        raise bpb.BankError(f"missing index note {INDEX_NOTE}.md")
    listed = index.read_text(encoding="utf-8")
    unlisted = [p.stem for p in paths if f"[[{p.stem}" not in listed]
    if unlisted:
        raise bpb.BankError(f"{INDEX_NOTE} does not list: {', '.join(unlisted)}")
    return sorted(items, key=lambda i: int(i["id"][1:]))


def build():
    items = load_items()
    data = {
        "_comment": "Generated by tools/build_maths_bank.py from vault/04 - Advanced Maths/Problem Bank/. Do not edit by hand.",
        "subject": "advanced-maths",
        "categories": {c: {"label": f"{e[2]} problems", "points": e[0]} for c, e in EXAMS.items()},
        "pages": {c: e[1] for c, e in EXAMS.items()},
        "archetypes": ARCHETYPES, "levels": LEVELS,
        "units": {str(k): v for k, v in UNITS.items()},
        "counts": {c: sum(i["category"] == c for i in items) for c in EXAMS},
        "items": items,
    }
    js = ("/* Generated by tools/build_maths_bank.py (same data as problems.json). Do not edit by hand. */\n"
          f"window.AE_AM_BANK = {json.dumps(data, ensure_ascii=False)};\n"
          "/* The exam structures of data/exam-blueprint*.json, for the Exam Simulator. */\n")
    for _, _, _, fname, var in EXAMS.values():
        blueprint = json.loads((OUT_DIR / fname).read_text(encoding="utf-8"))
        check_blueprint(fname, blueprint, items)
        js += f"window.{var} = {json.dumps(blueprint, ensure_ascii=False)};\n"
    outputs = {OUT_DIR / "problems.json": json.dumps(data, indent=1, ensure_ascii=False) + "\n", OUT_DIR / "problems.js": js}
    hub = EXTRA / "index.html"
    outputs[hub] = emb._fill(emb._HUB_BLOCK, hub, _read(hub), render_hub(items))
    for cat, (_, page, *_rest) in EXAMS.items():
        path = EXTRA / page
        outputs[path] = emb._fill(emb._PAGE_BLOCK, path, _read(path), render_page(cat, items))
    return outputs, data


def _read(path):
    if not path.is_file():
        raise bpb.BankError(f"missing page {path.relative_to(REPO).as_posix()}")
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


# --------------------------------------------------------------------------- the Extra problems pages
def _card(item):
    exam = EXAMS[item["category"]][2]
    tag = (f"{exam} · {UNITS[item['unit']].split(' · ')[0]} · {ARCHETYPES[item['archetype']]} · {emb._pts(item['points'])} · "
           f"{item['time_minutes']} min · {LEVELS[item['level']]}")
    out = [f'      <section class="problem-box" id="{item["id"]}">',
           f'        <span class="problem-tag">{html.escape(tag)}</span>',
           f'        <h4 class="problem-title">{html.escape(item["id"])} — {html.escape(item["title"])}</h4>',
           '        <div class="statement-box">', item["statement_html"], "        </div>"]
    if item["setup_html"]:
        out += ['        <div class="phase-block">', '          <h3 class="phase-title">Setup and canonical formulation</h3>',
                item["setup_html"], "        </div>"]
    for sub in item["subquestions"]:
        out += ['        <div class="phase-block">',
                f'          <h3 class="phase-title">Part ({sub["label"]}) · {emb._pts(sub["points"])}</h3>',
                '          <div class="prompt">' + sub["prompt_html"] + "</div>",
                sub["solution_html"],
                '          <div class="result-callout"><div class="result-callout-title">Key results</div>'
                + sub["checkpoint_html"] + "</div>",
                "        </div>"]
    if item["interpretation_html"]:
        out += ['        <div class="phase-block">', '          <h3 class="phase-title">Interpretation and checks</h3>',
                item["interpretation_html"], "        </div>"]
    out.append("      </section>")
    return "\n".join(out)


LEADS = {
    "midterm_1_problem": "exam-style problems on Units 1 to 4 (first- and second-order ODEs, linear systems), worth 5 points "
                         "each. The first partials of 2019 to 2025 are 2 or 3 problems in 60 to 90 minutes; the "
                         '<a href="../simulator/index.html">Exam simulator</a> draws one ODE problem and one linear-system problem.',
    "midterm_2_problem": "exam-style problems on nonlinear systems, Fourier series and the heat, wave and Laplace equations, "
                         "worth 5 points each. The second partials of 2019 to 2025 are two problems in 1 to 2 hours; the "
                         '<a href="../simulator/index.html?exam=midterm-2">Exam simulator</a> draws one of each block.',
    "final_problem": "final-exam problems of 2.5 points, one per block of the course (ODEs, systems, Fourier and "
                     "Sturm-Liouville, PDEs), like the four problems of the finals of 2019 and 2020; the "
                     '<a href="../simulator/index.html?exam=final">Exam simulator</a> draws one of each.',
}


def render_page(cat, items):
    mine = [i for i in items if i["category"] == cat]
    return "\n".join([f'      <p class="midterm-part-lead">{len(mine)} {LEADS[cat]}</p>',
                      "\n".join(_card(i) for i in mine)]) + "\n"


HUB_TEXT = {
    "midterm_1_problem": ("midterm-1", "The first partial covers Units 1 to 4: first-order models and qualitative analysis, "
                          "second-order linear equations and linear systems with their phase portraits.",
                          ["5 points each", "Units 1 to 4", "Verified with SymPy"]),
    "midterm_2_problem": ("midterm-2", "The second partial covers nonlinear systems and their linearisation, Fourier series "
                          "and the separation of variables for the heat, wave and Laplace equations.",
                          ["5 points each", "Units 4 to 6", "Verified with SymPy"]),
    "final_problem": ("final", "The final exam has four problems of about 2.5 points, one per block of the course.",
                      ["2.5 points each", "Units 1 to 6", "Verified with SymPy"]),
}


def render_hub(items):
    out = []
    for cat, (_, page, label, *_rest) in EXAMS.items():
        mine = [i for i in items if i["category"] == cat]
        anchor, lead, chips = HUB_TEXT[cat]
        sim = "../simulator/index.html" + ("" if anchor == "midterm-1" else f"?exam={anchor}")
        out += [f'    <section class="exam-block" id="{anchor}" aria-labelledby="{anchor}-title">',
                f'      <h2 class="exam-block-title" id="{anchor}-title">{label}</h2>',
                f'      <p class="exam-block-lead">{lead} Practise the problems one by one or take a timed exam built from '
                f'them in the <a href="{sim}">Exam simulator</a>.</p>',
                '      <div class="problem-sets-grid">',
                emb._hub_card(page, f"{label} • Problems", f"Exam-Style Problems {mine[0]['id']} to {mine[-1]['id']}",
                              f"{len(mine)} problems solved step by step, with the key results of every part and the "
                              "common mistakes of the exam.", mine, [f"{len(mine)} Problems"] + chips),
                "      </div>", "    </section>", ""]
    return "\n".join(out[:-1]) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--lint", action="store_true")
    args = ap.parse_args(argv)
    try:
        if args.lint:
            items = load_items()
            print(f"build_maths_bank: {len(items)} notes valid")
            return 0
        outputs, data = build()
    except bpb.BankError as exc:
        print(f"build_maths_bank: {exc}")
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
    print("build_maths_bank: " + ", ".join(f"{n} {c}" for c, n in data["counts"].items()))
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
