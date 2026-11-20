"""Business Management Midterm 2 bank: True/False blocks, multiple-choice blocks and problems (Topics 3 Part II to 7).

Called by tools/build_problem_bank.py, which writes one bank for both midterms (subjects/business-management/data/
problems.json and problems.js). The notes live in vault/05 - Business Management/Problem Bank/ next to the Midterm 1
notes; their format and the rules enforced here are in "Rules - Midterm 2 Exam Style Analysis.md" of that folder:

* "Quiz - Bank Fnn - Unit N <theme>.md": a block of ten True/False statements ("## Fnn.k <title>", "- id: Fnn-Sk",
  "- concept_id: uN-...", the statement, "### Answer" T or F, "### Reasoning", "### Source").
* "Quiz - Bank Bnn - Unit N <theme>.md": a block of ten multiple-choice questions, in the format of the Aerospace
  Materials I blocks (tools/build_materials_bank.py), whose helpers are reused here.
* "Problem - Bank Mnn - <title>.md": a 2.5-point problem or case, in the note format of tools/build_mechanics_bank.py,
  with an optional "## Verification" section whose expressions are recomputed on every build.

Checks: frontmatter; ten statements or questions per block in order; T/F answers T or F, 4 to 6 true per block, never
the same answer four times in a row; the multiple-choice rules of the Materials bank (four different options, one
answer, every wrong option explained, `calc` recomputed); at most MAX_TF_PER_CONCEPT statements and MAX_MC_PER_CONCEPT
questions per concept; text similarity of every pair below SIM_FAIL (pairs above SIM_WARN reported); subquestion points
add up to 2.5; every Verification line recomputed; balanced $ and $$; no emojis, "Phase N" labels or \\euro; every figure
drawn; the index note lists every note; and, unless partial, the unit quotas and the spread of the answers.
"""
import html
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parents[1]
REPO = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
import build_problem_bank as bpb  # noqa: E402
import build_materials_bank as mb  # noqa: E402  (shared checks: KaTeX balance, numbers, similarity, calc)
import build_mechanics_bank as emb  # noqa: E402  (problem note parser and page helpers)
import build_topic_pages as bt  # noqa: E402
from figures import bm_mt2 as figmod  # noqa: E402

BANK = bpb.BANK
OUT_DIR = bpb.OUT_DIR
EXTRA = bpb.EXTRA
BLUEPRINT = "exam-blueprint-midterm-2.json"
TF_PAGE, TEST_PAGE, PROBLEMS_PAGE = EXTRA / "midterm-2-tf.html", EXTRA / "midterm-2-test.html", EXTRA / "midterm-2-problems.html"

TF_CAT, MC_CAT, PROB_CAT = "mt2_true_false", "mt2_test_question", "mt2_problem"
TF_BLOCK, MC_BLOCK = "mt2_tf_block", "mt2_mcq_block"
PAGES = {TF_CAT: TF_PAGE.name, MC_CAT: TEST_PAGE.name, PROB_CAT: PROBLEMS_PAGE.name}
UNITS = {3: "Topic 3 · Investment selection (Part II)", 4: "Topic 4 · The production function",
         5: "Topic 5 · Marketing and sales", 6: "Topic 6 · The management function",
         7: "Topic 7 · Entrepreneurship and innovation"}
ARCHETYPES = {
    "npv-irr-fisher": "NPV, IRR and Fisher's rate",
    "bep-ol-elasticity": "Break-even, leverage and elasticity",
    "marketing-case": "Marketing case",
    "management-case": "Management case",
    "innovation-case": "Innovation case",
}
ARCH_UNIT = {"npv-irr-fisher": 3, "bep-ol-elasticity": 4, "marketing-case": 5, "management-case": 6, "innovation-case": 7}
PROBLEM_POINTS = 2.5
TF_POINTS, MC_POINTS = 0.15, 0.25
FORMATS = {k: v for k, v in mb.FORMATS.items() if k not in ("diagram-reading", "choose-figure")}
ASKS = tuple(a for a in mb.ASKS if a != "figure-reading")
QUOTA_TF, QUOTA_MC, QUOTA_PROBLEMS = 24, 20, 3       # per unit, per unit, per archetype (Rules note, section 2)
MAX_TF_PER_CONCEPT, MAX_MC_PER_CONCEPT = 3, 4
SIM_FAIL, SIM_WARN = mb.SIM_FAIL, mb.SIM_WARN
QUIZ_REQUIRED = ("bank_id", "title", "category", "unit", "concepts", "difficulty", "tags", "origen")
_QUIZ_NAME = re.compile(r"Quiz - Bank ([BF]\d{2}) - .+\.md$")
_PROB_NAME = re.compile(r"Problem - Bank (M\d{2}) - .+\.md$")
_THEAD = re.compile(r"([BF])(\d{2})\.(\d{1,2})\s+(.+)$")
_META = re.compile(r"^- (id|concept_id|format|asks|calc|check):\s*(.+?)\s*$")
_CONCEPT = re.compile(r"u([3-7])-[a-z0-9]+(?:-[a-z0-9]+)*$")
_EMBED = re.compile(r"!\[\[attachments/([\w-]+)/([\w-]+)\.(svg|png)\]\]")
TF_OPTIONS = [{"label": "T", "html": "True"}, {"label": "F", "html": "False"}]
BankError = bpb.BankError


def _rel(path):
    return path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.name


class Figures:
    """Figure embeds of one note: only the BM-MT2 figures of tools/figures/bm_mt2.py."""

    def __init__(self):
        self.count = 0
        self.used = []

    def __call__(self, name):
        if name not in figmod.REG.web:
            raise BankError(f"unknown figure {name!r} (not drawn in tools/figures/bm_mt2.py)")
        self.used.append(name)
        self.count += 1
        cap = html.escape(html.unescape(figmod.REG.captions[name]), quote=False)
        return (f'<div class="diagram-card">\n{figmod.REG.web[name]}\n'
                f'<div class="diagram-caption">Figure {self.count}. {cap}.</div>\n</div>')


def _before_back(body):
    """The note body before its "**Back to:**" line, without the horizontal rule that may precede it."""
    return re.sub(r"\n-{3,}\s*$", "\n", body.split("**Back to:**")[0].rstrip()) + "\n"


def _check_embeds(text, where):
    for folder, name, _ext in _EMBED.findall(text):
        if folder != "BM-MT2":
            raise BankError(f"{where}: figures of this bank live in attachments/BM-MT2, not {folder}")


# --------------------------------------------------------------------------- quiz notes (both kinds)
def parse_quiz_note(path):
    where = path.name
    m = _QUIZ_NAME.match(path.name)
    if not m:
        raise BankError(f"{where}: name must be 'Quiz - Bank Fnn|Bnn - Unit N <theme>.md'")
    kind = "true_false" if m.group(1)[0] == "F" else "multiple_choice"
    text = path.read_text(encoding="utf-8")
    mb._common_checks(text, where)
    _check_embeds(text, where)
    meta, body = bpb.frontmatter(text, where)
    missing = [k for k in QUIZ_REQUIRED if k not in meta]
    if missing:
        raise BankError(f"{where}: frontmatter lacks {', '.join(missing)}")
    if meta["bank_id"] != m.group(1):
        raise BankError(f"{where}: bank_id {meta['bank_id']} does not match the file name")
    want = TF_BLOCK if kind == "true_false" else MC_BLOCK
    if meta["category"] != want:
        raise BankError(f"{where}: category must be {want}")
    if meta["unit"] not in UNITS or meta["difficulty"] not in (1, 2, 3):
        raise BankError(f"{where}: unit must be 3-7 and difficulty 1-3")
    if f"Unit {meta['unit']}" not in path.name:
        raise BankError(f"{where}: the file name must carry 'Unit {meta['unit']}'")
    if "Practice item, not an official exercise" not in body:
        raise BankError(f"{where}: lacks the 'Practice item, not an official exercise' callout")
    body = mb._join_display_math(_before_back(body))
    figs = Figures()
    block_id = meta["bank_id"]
    questions = []
    for part in re.split(r"\n## ", "\n" + body)[1:]:
        head, _, rest = part.partition("\n")
        hm = _THEAD.match(head.strip())
        if not hm or hm.group(1) + hm.group(2) != block_id:
            raise BankError(f"{where}: unexpected section '## {head.strip()}' (expected '## {block_id}.k <title>')")
        number, title = int(hm.group(3)), hm.group(4).strip()
        fn = _tf_statement if kind == "true_false" else _mc_question
        questions.append(fn(block_id, number, title, rest, meta, f"{where} {block_id}.{number}", figs, path))
    numbers = [q["number"] for q in questions]
    if numbers != list(range(1, 11)):
        raise BankError(f"{where}: a block has items 1 to 10 in order, got {numbers}")
    answers = "".join(q["answer"] for q in questions)
    run = re.search(r"(.)\1{3}", answers)
    if run:
        raise BankError(f"{where}: the answer is '{run.group(1)}' four times in a row ({answers})")
    if kind == "true_false" and not 4 <= answers.count("T") <= 6:
        raise BankError(f"{where}: a block has 4 to 6 true statements, got {answers.count('T')} ({answers})")
    listed, used = set(meta["concepts"]), {q["concept_id"] for q in questions}
    if listed != used:
        raise BankError(f"{where}: frontmatter concepts and the items' concept_id differ: {sorted(listed ^ used)}")
    return {"id": block_id, "kind": kind, "unit": meta["unit"], "title": meta["title"], "difficulty": meta["difficulty"],
            "tags": [t for t in meta["tags"] if t != "problem-bank"], "source": meta["origen"], "vault_note": _rel(path),
            "figures": figs.used, "questions": questions}


def _sections(rest, names, where):
    sections = re.split(r"\n### ", "\n" + rest)
    named = {}
    for sec in sections[1:]:
        name, _, text = sec.partition("\n")
        if name.strip() not in names or name.strip() in named:
            raise BankError(f"{where}: unexpected or repeated '### {name.strip()}'")
        named[name.strip()] = text.strip("\n")
    for need in names:
        if not named.get(need, "").strip():
            raise BankError(f"{where}: lacks its '### {need}'")
    return sections[0], named


def _head_lines(first, where):
    info, stem = {}, []
    for line in first.split("\n"):
        mm = _META.match(line)
        if mm and not any(x.strip() for x in stem):
            if mm.group(1) in info:
                raise BankError(f"{where}: '{mm.group(1)}' given twice")
            info[mm.group(1)] = mm.group(2)
        else:
            stem.append(line)
    return info, stem


def _concept(info, meta, where):
    cm = _CONCEPT.match(info.get("concept_id", ""))
    if not cm or int(cm.group(1)) != meta["unit"]:
        raise BankError(f"{where}: concept_id must look like u{meta['unit']}-<kebab-case>")
    return info["concept_id"]


def _tf_statement(block_id, number, title, rest, meta, where, figs, path):
    qid = f"{block_id}-S{number}"
    first, named = _sections(rest, ("Answer", "Reasoning", "Source"), where)
    info, stem = _head_lines(first, where)
    if info.get("id") != qid:
        raise BankError(f"{where}: '- id:' must be {qid}")
    if set(info) - {"id", "concept_id"}:
        raise BankError(f"{where}: a statement carries only '- id' and '- concept_id'")
    concept = _concept(info, meta, where)
    if not any(x.strip() for x in stem):
        raise BankError(f"{where}: no statement")
    answer = named["Answer"].strip().upper()
    if answer not in ("T", "F"):
        raise BankError(f"{where}: '### Answer' must be T or F, got {named['Answer'].strip()!r}")
    if len(named["Reasoning"].strip()) < 40:
        raise BankError(f"{where}: the reasoning must say why (at least one full sentence)")
    plain = " ".join(x.strip() for x in stem if x.strip())
    return {
        "id": qid, "category": TF_CAT, "kind": "true_false", "block": block_id, "number": number,
        "unit": meta["unit"], "concept_id": concept, "theme": concept, "title": title,
        "difficulty": meta["difficulty"], "points": TF_POINTS,
        "statement_html": emb.render(list(stem), where, figs),
        "options": TF_OPTIONS, "answer": answer,
        "explanation_html": emb.render(named["Reasoning"].split("\n"), where, figs),
        "distractors": {},
        "source_html": emb.render(named["Source"].split("\n"), where, figs),
        "vault_note": _rel(path), "_text": plain,
    }


def _mc_question(block_id, number, title, rest, meta, where, figs, path):
    """A multiple-choice question: the rules of tools/build_materials_bank.py, with the units of this bank."""
    qid = f"{block_id}-Q{number}"
    first, named = _sections(rest, ("Answer", "Explanation", "Source"), where)
    info, stem, options = {}, [], {}
    for line in first.split("\n"):
        mm, om = _META.match(line), mb._OPT.match(line)
        if mm and not any(x.strip() for x in stem) and not options:
            if mm.group(1) in info:
                raise BankError(f"{where}: '{mm.group(1)}' given twice")
            info[mm.group(1)] = mm.group(2)
        elif om:
            if om.group(1) in options:
                raise BankError(f"{where}: option {om.group(1)}) given twice")
            options[om.group(1)] = om.group(2)
        elif options and line.strip():
            raise BankError(f"{where}: text after the options: {line[:50]!r}")
        else:
            stem.append(line)
    if info.get("id") != qid:
        raise BankError(f"{where}: '- id:' must be {qid}")
    concept = _concept(info, meta, where)
    if info.get("format") not in FORMATS:
        raise BankError(f"{where}: unknown format {info.get('format')!r}")
    if info.get("asks") not in ASKS:
        raise BankError(f"{where}: unknown asks {info.get('asks')!r}")
    letters = mb.LETTERS
    if "".join(sorted(options)) != letters:
        raise BankError(f"{where}: needs the four options a) to d), got {sorted(options)}")
    if not any(x.strip() for x in stem):
        raise BankError(f"{where}: no statement")
    if len({re.sub(r"\W+", "", options[k]).lower() for k in letters}) != 4:
        raise BankError(f"{where}: two options are the same")
    answer = named["Answer"].strip().rstrip(")").lower()
    if answer not in letters or len(answer) != 1:
        raise BankError(f"{where}: '### Answer' must be one letter a-d, got {named['Answer'].strip()!r}")
    lead, distractors, current = [], {}, None
    for line in named["Explanation"].split("\n"):
        dm = re.match(r"^- ([a-d])\)\s+(.+)$", line)
        if dm:
            current = dm.group(1)
            if current in distractors:
                raise BankError(f"{where}: option {current}) is explained twice")
            distractors[current] = dm.group(2).strip()
        elif current and line.strip():
            distractors[current] += " " + line.strip()
        elif not current:
            lead.append(line)
    wrong = [k for k in letters if k != answer]
    if sorted(distractors) != wrong:
        raise BankError(f"{where}: the explanation needs one bullet '- x) ...' per wrong option "
                        f"({', '.join(wrong)}), got {sorted(distractors)}")
    if not any(x.strip() for x in lead):
        raise BankError(f"{where}: the explanation must first say why {answer}) is right")
    for k, v in distractors.items():
        if len(v) < 25:
            raise BankError(f"{where}: the explanation of {k}) does not name the mistake behind it")
    if info.get("format") == "numeric" and "calc" not in info:
        raise BankError(f"{where}: a numeric question needs '- calc: <expression>'")
    if "calc" in info:
        calc = float(mb.evaluate(info["calc"], where))
        nums = {k: mb.leading_number(re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", options[k])) for k in letters}
        if any(v is None for v in nums.values()):
            raise BankError(f"{where}: every option of a question with 'calc' starts with a number")
        if len({v[1] for v in nums.values()}) != 1:
            raise BankError(f"{where}: the four options must carry the same unit, got {sorted({v[1] for v in nums.values()})}")
        if not mb._close(nums[answer][0], calc, 0.012):
            raise BankError(f"{where}: calc gives {calc:.6g} but option {answer}) is {nums[answer][0]:g}")
        for k in wrong:
            if mb._close(nums[k][0], calc, 0.03):
                raise BankError(f"{where}: wrong option {k}) = {nums[k][0]:g} coincides with the right value {calc:.6g}")
    if "check" in info and mb.evaluate(info["check"], where) is not True:
        raise BankError(f"{where}: check {info['check']!r} is not true")
    plain = " ".join(x.strip() for x in stem if x.strip())
    return {
        "id": qid, "category": MC_CAT, "kind": "multiple_choice", "block": block_id, "number": number,
        "unit": meta["unit"], "concept_id": concept, "theme": concept, "format": info["format"], "asks": info["asks"],
        "title": title, "difficulty": meta["difficulty"], "points": MC_POINTS,
        "statement_html": emb.render(list(stem), where, figs),
        "options": [{"label": k, "html": bt.inline(options[k])} for k in letters],
        "answer": answer,
        "explanation_html": emb.render(list(lead), where, figs),
        "distractors": {k: bt.inline(v) for k, v in distractors.items()},
        "source_html": emb.render(named["Source"].split("\n"), where, figs),
        "calc": info.get("calc"), "check": info.get("check"), "vault_note": _rel(path),
        "_text": plain + " || " + " | ".join(options[k] for k in letters),
    }


# --------------------------------------------------------------------------- problem notes
def parse_problem_note(path):
    where = path.name
    m = _PROB_NAME.match(path.name)
    if not m:
        raise BankError(f"{where}: name must be 'Problem - Bank Mnn - <title>.md'")
    text = path.read_text(encoding="utf-8")
    mb._common_checks(text, where)
    _check_embeds(text, where)
    meta, body = bpb.frontmatter(text, where)
    missing = [k for k in emb.REQUIRED if k not in meta]
    if missing:
        raise BankError(f"{where}: frontmatter lacks {', '.join(missing)}")
    if meta["bank_id"] != m.group(1):
        raise BankError(f"{where}: bank_id {meta['bank_id']} does not match the file name")
    if meta["category"] != PROB_CAT:
        raise BankError(f"{where}: category must be {PROB_CAT}")
    if meta["archetype"] not in ARCHETYPES:
        raise BankError(f"{where}: unknown archetype {meta['archetype']!r}")
    if meta["unit"] != ARCH_UNIT[meta["archetype"]]:
        raise BankError(f"{where}: a {meta['archetype']} problem belongs to unit {ARCH_UNIT[meta['archetype']]}")
    if float(meta["points"]) != PROBLEM_POINTS:
        raise BankError(f"{where}: a Midterm 2 problem is worth {PROBLEM_POINTS} points")
    if meta["level"] not in emb.LEVELS or meta["difficulty"] not in (1, 2, 3):
        raise BankError(f"{where}: unknown level or difficulty")
    if "Practice item, not an official exercise" not in body:
        raise BankError(f"{where}: lacks the 'Practice item, not an official exercise' callout")
    body = mb._join_display_math(_before_back(body))
    figs = Figures()
    item = {
        "id": meta["bank_id"], "category": PROB_CAT, "archetype": meta["archetype"], "theme": meta["archetype"],
        "level": meta["level"], "unit": meta["unit"], "title": meta["title"], "difficulty": meta["difficulty"],
        "points": PROBLEM_POINTS, "time_minutes": meta["time_minutes"],
        "tags": [t for t in meta["tags"] if t != "problem-bank"], "official": False, "source": meta["origen"],
        "vault_note": _rel(path), "statement_html": None, "setup_html": None, "subquestions": [],
        "interpretation_html": None, "figures": [], "verify": [],
    }
    for part in re.split(r"\n## ", "\n" + body)[1:]:
        head, _, rest = part.partition("\n")
        head, lines = head.strip(), rest.split("\n")
        if head in ("Statement", "Setup", "Interpretation"):
            item[f"{head.lower()}_html"] = emb.render(lines, where, figs)
        elif head == "Verification":
            item["verify"] = mb._verify_lines(lines, where)
        elif emb._SUB.match(head):
            item["subquestions"].append(emb.subquestion(head, rest, where, figs))
        else:
            raise BankError(f"{where}: unexpected section '## {head}'")
    item["figures"] = figs.used
    if not item["statement_html"]:
        raise BankError(f"{where}: no '## Statement' section")
    labels = [s["label"] for s in item["subquestions"]]
    if not labels or labels != [chr(ord("a") + i) for i in range(len(labels))]:
        raise BankError(f"{where}: subquestions must be (a), (b), ... in order, got {labels}")
    total = round(sum(s["points"] for s in item["subquestions"]), 4)
    if total != PROBLEM_POINTS:
        raise BankError(f"{where}: subquestion points add up to {total}, not {PROBLEM_POINTS}")
    if item["archetype"] in ("npv-irr-fisher", "bep-ol-elasticity") and not item["verify"]:
        raise BankError(f"{where}: a numeric problem needs its '## Verification' section")
    verify_problem(item)
    return item


def _tolerance(text):
    dec = len(text.split(".")[1]) if "." in text else 0
    return 0.5 * 10 ** -dec + 1e-9


def verify_problem(item):
    """Recompute every Verification line; the stated value must be the computed one, rounded as printed."""
    rows = []
    for v in item["verify"]:
        got = float(mb.evaluate(v["expr"], f"{item['id']} {v['label']}"))
        ok = abs(got - v["stated"]) <= max(_tolerance(v["text"].replace(",", "")), 1e-3 * abs(v["stated"]))
        if not ok:
            raise BankError(f"{item['id']}: {v['label']} computes to {got:.6g}, the note states {v['text']}")
        rows.append((v["label"], got, v["text"]))
    return rows


# --------------------------------------------------------------------------- whole bank
def _similar(items):
    pairs = mb.similarity_report(items)
    too_close = [p for p in pairs if p[0] >= SIM_FAIL]
    if too_close:
        raise BankError("items too similar (>= %.2f): " % SIM_FAIL +
                        "; ".join(f"{a} ~ {b} ({r:.2f})" for r, a, b in too_close[:12]))
    return [p for p in pairs if p[0] < SIM_FAIL]


def check_bank(blocks, problems, partial=False):
    tfs = [q for b in blocks if b["kind"] == "true_false" for q in b["questions"]]
    mcs = [q for b in blocks if b["kind"] == "multiple_choice" for q in b["questions"]]
    for qs, limit, distinct in ((tfs, MAX_TF_PER_CONCEPT, False), (mcs, MAX_MC_PER_CONCEPT, True)):
        by = {}
        for q in qs:
            by.setdefault(q["concept_id"], []).append(q)
        for concept, group in sorted(by.items()):
            if len(group) > limit:
                raise BankError(f"concept {concept} has {len(group)} items (maximum {limit}): "
                                f"{', '.join(q['id'] for q in group)}")
            if distinct:
                seen = {}
                for q in group:
                    key = (q["format"], q["asks"])
                    if key in seen:
                        raise BankError(f"concept {concept}: {seen[key]} and {q['id']} share format and question type {key}")
                    seen[key] = q["id"]
    review = _similar(tfs) + _similar(mcs)
    if not partial:
        for unit in UNITS:
            n_tf, n_mc = sum(q["unit"] == unit for q in tfs), sum(q["unit"] == unit for q in mcs)
            if n_tf < QUOTA_TF or n_mc < QUOTA_MC:
                raise BankError(f"unit {unit} has {n_tf} True/False and {n_mc} multiple-choice items "
                                f"(quotas {QUOTA_TF} and {QUOTA_MC})")
        for arch in ARCHETYPES:
            n = sum(p["archetype"] == arch for p in problems)
            if n < QUOTA_PROBLEMS:
                raise BankError(f"problem type {arch} has {n} problems, the minimum is {QUOTA_PROBLEMS}")
    if tfs:
        share = sum(q["answer"] == "T" for q in tfs) / len(tfs)
        if not 0.45 <= share <= 0.55:
            raise BankError(f"true statements are {share:.0%} of the bank (between 45% and 55%)")
    if mcs and not partial:
        share = {k: sum(q["answer"] == k for q in mcs) / len(mcs) for k in mb.LETTERS}
        off = {k: round(v, 3) for k, v in share.items() if not 0.20 <= v <= 0.30}
        if off:
            raise BankError(f"the right answer is not spread evenly over a-d: {off}")
    return review


def check_blueprint(bp, blocks, problems, partial=False):
    where = BLUEPRINT
    parts = {p["id"]: p for p in bp.get("parts", [])}
    total = round(sum(p["count"] * p["points_each"] for p in parts.values()), 4)
    if total != bp.get("total_points"):
        raise BankError(f"{where}: parts add up to {total}, not {bp.get('total_points')}")
    pools = {TF_CAT: [q for b in blocks if b["kind"] == "true_false" for q in b["questions"]],
             MC_CAT: [q for b in blocks if b["kind"] == "multiple_choice" for q in b["questions"]], PROB_CAT: problems}
    for p in parts.values():
        if round(p["count"] * p["points_each"], 4) != p["points_total"]:
            raise BankError(f"{where}: {p['id']} points_total is not count x points_each")
        pool = pools.get(p["category"])
        if pool is None:
            raise BankError(f"{where}: {p['id']} has an unknown category {p['category']!r}")
        if p.get("type") in ("true_false", "multiple_choice"):
            for key in ("points_correct", "points_wrong", "points_blank", "floor"):
                if not isinstance(p.get(key), (int, float)):
                    raise BankError(f"{where}: {p['id']} lacks the number {key}")
            if p["points_correct"] != p["points_each"]:
                raise BankError(f"{where}: {p['id']} points_correct must equal points_each")
            per_unit = p.get("selection_rules", {}).get("per_unit", {})
            if sum(per_unit.values()) != p["count"] or any(int(u) not in UNITS for u in per_unit):
                raise BankError(f"{where}: {p['id']} per_unit must cover units {sorted(UNITS)} and add up to {p['count']}")
            if not partial:
                for u, n in per_unit.items():
                    if sum(q["unit"] == int(u) for q in pool) < 2 * n:
                        raise BankError(f"{where}: unit {u} needs at least {2 * n} items for {p['id']}")
            elif len(pool) < p["count"]:
                raise BankError(f"{where}: {p['id']} needs at least {p['count']} items, the bank has {len(pool)}")
        else:
            arch = p.get("selection_rules", {}).get("archetypes", [])
            if sorted(arch) != sorted(ARCHETYPES):
                raise BankError(f"{where}: {p['id']} must list every archetype")
            if p["points_each"] != PROBLEM_POINTS:
                raise BankError(f"{where}: {p['id']} items are worth {PROBLEM_POINTS} points")
            if len({x["archetype"] for x in problems}) < p["count"]:
                raise BankError(f"{where}: {p['id']} needs problems of {p['count']} different archetypes")
    for k, v in bp.get("unit_labels", {}).items():
        if int(k) not in UNITS:
            raise BankError(f"{where}: unit_labels has an unknown unit {k}")
    modes = bp.get("modes") or []
    if sum(1 for m in modes if m.get("default")) != 1:
        raise BankError(f"{where}: exactly one mode must be the default")
    for m in modes:
        if not m.get("label") or not m.get("description") or not re.fullmatch(r"[\w-]+", m.get("id", "")):
            raise BankError(f"{where}: mode {m.get('id')} needs an id, a label and a description")
        if not m.get("parts") or any(x not in parts for x in m["parts"]):
            raise BankError(f"{where}: mode {m['id']} must list existing parts")
        opts = m.get("count_options")
        if opts is not None and (m.get("default_count") not in opts):
            raise BankError(f"{where}: mode {m['id']} default_count must be one of its count_options")
        if m.get("duration_minutes") and m["duration_minutes"] not in m.get("duration_options_minutes", [m["duration_minutes"]]):
            raise BankError(f"{where}: mode {m['id']} duration_minutes must be one of its options")


def load(bank_dir=BANK, partial=False):
    figmod.build()
    quiz_paths = sorted(bank_dir.glob("Quiz - Bank *.md"))
    prob_paths = sorted(bank_dir.glob("Problem - Bank M*.md"))
    blocks = [parse_quiz_note(p) for p in quiz_paths]
    problems = [parse_problem_note(p) for p in prob_paths]
    ids = [b["id"] for b in blocks] + [p["id"] for p in problems]
    dup = sorted({x for x in ids if ids.count(x) > 1})
    if dup:
        raise BankError(f"duplicate bank ids: {', '.join(dup)}")
    index = bank_dir / f"{bpb.INDEX_NOTE}.md"
    if index.is_file():
        listed = index.read_text(encoding="utf-8")
        unlisted = [p.stem for p in quiz_paths + prob_paths if f"[[{p.stem}" not in listed]
        if unlisted:
            raise BankError(f"{bpb.INDEX_NOTE} does not list: {', '.join(unlisted)}")
    blocks.sort(key=lambda b: (b["kind"] != "true_false", int(b["id"][1:])))
    problems.sort(key=lambda p: int(p["id"][1:]))
    review = check_bank(blocks, problems, partial)
    used = {f for b in blocks for f in b["figures"]} | {f for p in problems for f in p["figures"]}
    unused = sorted(set(figmod.PROFILES) - used)
    if unused and bank_dir == BANK:
        raise BankError(f"figures drawn but not used by any note: {', '.join(unused)}")
    return blocks, problems, review


def build(partial=False):
    """Items, blocks and blueprint of Midterm 2, plus the generated blocks of its three Extra problems pages."""
    blocks, problems, review = load(partial=partial)
    blueprint = json.loads((OUT_DIR / BLUEPRINT).read_text(encoding="utf-8"))
    check_blueprint(blueprint, blocks, problems, partial)
    items = [{k: v for k, v in q.items() if not k.startswith("_")} for b in blocks for q in b["questions"]] + problems
    block_list = [{"id": b["id"], "kind": b["kind"], "unit": b["unit"], "title": b["title"],
                   "items": [q["id"] for q in b["questions"]]} for b in blocks]
    pages = {}
    for path, fn in ((TF_PAGE, render_tf_page), (TEST_PAGE, render_test_page), (PROBLEMS_PAGE, render_problems_page)):
        if path.is_file():
            page = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
            pages[path] = emb._fill(emb._PAGE_BLOCK, path, page, fn(blocks, problems, blueprint))
    return {"items": items, "blocks": block_list, "blueprint": blueprint, "pages": pages, "review": review,
            "blocks_full": blocks, "problems": problems}


# --------------------------------------------------------------------------- pages
def _part(bp, ptype):
    return next(p for p in bp["parts"] if p.get("type") == ptype)


def _tf_html(q):
    word = "True" if q["answer"] == "T" else "False"
    return "\n".join([
        f'        <div class="phase-block mcq-item tf-item" id="{q["id"]}">',
        f'          <h3 class="phase-title">Statement {q["number"]} · {html.escape(q["title"])}</h3>',
        '          <div class="prompt">' + q["statement_html"] + "</div>",
        '          <p class="tf-choices" aria-hidden="true"><span class="mcq-letter">T</span> / <span class="mcq-letter">F</span></p>',
        '          <details class="mcq-answer">',
        "            <summary>Answer and reasoning</summary>",
        f'            <p class="mcq-right"><strong>Answer: {word} ({q["answer"]})</strong></p>',
        q["explanation_html"],
        '            <div class="mcq-source"><span class="mcq-source__label">Source.</span> ' + q["source_html"] + "</div>",
        "          </details>",
        "        </div>"])


def _block_card(block, part, noun, intro, item_html):
    unit = UNITS[block["unit"]]
    tag = (f"{noun} block · {unit.split(' · ')[0]} · 10 items · +{part['points_correct']:g} right, "
           f"{part['points_wrong']:g} wrong · Practice item, not an official exercise")
    return "\n".join([
        f'      <section class="problem-box" id="{block["id"]}">',
        f'        <span class="problem-tag">{html.escape(tag)}</span>',
        f'        <h4 class="problem-title">{block["id"]} — {html.escape(block["title"])}</h4>',
        '        <div class="statement-box">', intro.format(theme=html.escape(unit.split(" · ")[1].lower())), "        </div>",
        "\n".join(item_html(q) for q in block["questions"]),
        "      </section>"])


def _by_unit(blocks, card):
    out = []
    for unit, label in UNITS.items():
        mine = [b for b in blocks if b["unit"] == unit]
        if mine:
            out.append(f'      <h2 class="mcq-unit-title" id="unit-{unit}">{html.escape(label)} '
                       f'<span class="mcq-unit-count">{len(mine)} block{"s" if len(mine) > 1 else ""}</span></h2>')
            out += [card(b) for b in mine]
    return out


def render_tf_page(blocks, problems, bp):
    tf = _part(bp, "true_false")
    mine = [b for b in blocks if b["kind"] == "true_false"]
    n = sum(len(b["questions"]) for b in mine)
    lead = (f'      <p class="midterm-part-lead">{n} True/False statements in {len(mine)} blocks of ten, on Topics 3 (Part II) '
            f'to 7. Part I of the second partial is {tf["count"]} statements: +{tf["points_correct"]:g} points for a right '
            f'answer, {tf["points_wrong"]:g} for a wrong one, {tf["points_blank"]:g} for a blank, and in the exam no answer '
            'counts without a short written reason. Decide each statement and write your reason before you open the answer. '
            'These are practice items, not official exercises. The <a href="../simulator/index.html?exam=midterm-2">Exam '
            'simulator</a> draws them by unit, timed or corrected as you answer.</p>')
    intro = ('<p>Ten statements on {theme}, written for this portal in the style of the True/False exercise of the course\'s '
             'example exam. State whether each one is true (T) or false (F) and justify it briefly.</p>')
    return "\n".join([lead] + _by_unit(mine, lambda b: _block_card(b, tf, "True/False", intro, _tf_html))) + "\n"


def render_test_page(blocks, problems, bp):
    mc = _part(bp, "multiple_choice")
    mine = [b for b in blocks if b["kind"] == "multiple_choice"]
    n = sum(len(b["questions"]) for b in mine)
    lead = (f'      <p class="midterm-part-lead">{n} multiple-choice questions in {len(mine)} blocks of ten, on Topics 3 '
            f'(Part II) to 7. In the simulated exam, Part II is {mc["count"]} questions with four options and one right '
            f'answer: +{mc["points_correct"]:g} points for a right answer, {mc["points_wrong"]:g} for a wrong one, '
            f'{mc["points_blank"]:g} for a blank, never below {mc["floor"]:g}. The course\'s example exam has no '
            'multiple-choice part: this is a practice format of the portal, and these are practice items, not official '
            'exercises.</p>')
    intro = ('<p>Ten questions on {theme}, written for this portal. Each question has four options and only one is right. '
             'Answer all ten before opening any explanation.</p>')
    return "\n".join([lead] + _by_unit(mine, lambda b: _block_card(b, mc, "Test", intro, mb._question_html))) + "\n"


def _problem_card(item):
    tag = (f"Problem · {UNITS[item['unit']].split(' · ')[0]} · {ARCHETYPES[item['archetype']]} · "
           f"{emb._pts(item['points'])} · {item['time_minutes']} min · Practice item, not an official exercise")
    case = item["archetype"].endswith("-case")
    out = [f'      <section class="problem-box" id="{item["id"]}">',
           f'        <span class="problem-tag">{html.escape(tag)}</span>',
           f'        <h4 class="problem-title">{html.escape(item["id"])} — {html.escape(item["title"])}</h4>',
           '        <div class="statement-box">', item["statement_html"], "        </div>"]
    if item["setup_html"]:
        out += ['        <div class="phase-block">', '          <h3 class="phase-title">Data and model</h3>',
                item["setup_html"], "        </div>"]
    for sub in item["subquestions"]:
        out += ['        <div class="phase-block">',
                f'          <h3 class="phase-title">Part ({sub["label"]}) · {emb._pts(sub["points"])}</h3>',
                '          <div class="prompt">' + sub["prompt_html"] + "</div>",
                sub["solution_html"],
                '          <div class="result-callout"><div class="result-callout-title">'
                + ("Key points" if case else "Key results") + "</div>" + sub["checkpoint_html"] + "</div>",
                "        </div>"]
    if item["interpretation_html"]:
        out += ['        <div class="phase-block">', '          <h3 class="phase-title">Interpretation and checks</h3>',
                item["interpretation_html"], "        </div>"]
    out.append("      </section>")
    return "\n".join(out)


def render_problems_page(blocks, problems, bp):
    lead = (f'      <p class="midterm-part-lead">{len(problems)} exam-style problems and cases written for this portal, '
            'in the style of the course\'s example exam: investment selection with NPV, IRR and Fisher\'s rate; '
            'break-even point, operating leverage and price elasticity; and cases on marketing, management and '
            'innovation. Part III of the simulated exam is two of them, of different types, 2.5 points each. These are '
            'practice items, not official exercises.</p>')
    out = [lead]
    for arch, label in ARCHETYPES.items():
        mine = [p for p in problems if p["archetype"] == arch]
        if mine:
            out.append(f'      <h2 class="mcq-unit-title" id="{arch}">{html.escape(label)} '
                       f'<span class="mcq-unit-count">{len(mine)} item{"s" if len(mine) > 1 else ""}</span></h2>')
            out += [_problem_card(p) for p in mine]
    return "\n".join(out) + "\n"


def render_hub_section(mt2):
    blocks, problems = mt2["blocks_full"], mt2["problems"]
    tf = [b for b in blocks if b["kind"] == "true_false"]
    mc = [b for b in blocks if b["kind"] == "multiple_choice"]
    cards = []
    if tf:
        n = sum(len(b["questions"]) for b in tf)
        cards.append(emb._hub_card(
            TF_PAGE.name, "2nd Midterm • True/False", f"True/False Statements, Blocks {tf[0]['id']} to {tf[-1]['id']}",
            f"{n} statements in {len(tf)} blocks of ten, each with its answer, the reasoning a student must write and "
            "its source.", tf, [f"{n} Statements", "Blocks of 10", "Topics 3 to 7", "Reasoning per answer"]))
    if mc:
        n = sum(len(b["questions"]) for b in mc)
        cards.append(emb._hub_card(
            TEST_PAGE.name, "2nd Midterm • Test", f"Multiple-Choice Questions, Blocks {mc[0]['id']} to {mc[-1]['id']}",
            f"{n} questions with four options in {len(mc)} blocks of ten, each with its answer and the reason why every "
            "wrong option is wrong.", mc, [f"{n} Questions", "Blocks of 10", "Topics 3 to 7", "Answers explained"]))
    if problems:
        cards.append(emb._hub_card(
            PROBLEMS_PAGE.name, "2nd Midterm • Problems",
            f"Exam-Style Problems and Cases {problems[0]['id']} to {problems[-1]['id']}",
            f"{len(problems)} problems and cases of 2.5 points, solved step by step: NPV and Fisher's rate, break-even "
            "and leverage, marketing, management and innovation cases.", problems,
            [f"{len(problems)} Problems and cases", "2.5 points each", "Step-by-step solutions", "Results recomputed"]))
    return "\n".join([
        '    <section class="exam-block" id="midterm-2" aria-labelledby="midterm-2-title">',
        '      <h2 class="exam-block-title" id="midterm-2-title">2nd Midterm</h2>',
        '      <p class="exam-block-lead">The second partial covers Topics 3 (Part II, investment selection) to 7: '
        'production, marketing, management and innovation. The simulated exam has three parts: twenty True/False '
        'statements with a short reason (3 points), eight multiple-choice questions (2 points) and two problems or cases '
        '(5 points), in 90 minutes. Practise each part on its own page, or take a timed exam in the '
        '<a href="../simulator/index.html?exam=midterm-2">Exam simulator</a>.</p>',
        '      <div class="problem-sets-grid">', "\n\n".join(cards), "      </div>", "    </section>"]) + "\n"
