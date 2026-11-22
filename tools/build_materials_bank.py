#!/usr/bin/env python3
"""Build the Aerospace Materials I Midterm 2 bank (subjects/aerospace-materials-1/data/problems.json) from its vault notes.

The bank lives in vault/02 - Aerospace Materials I/Problem Bank/ and has two kinds of notes:

* "Quiz - Bank Bnn - <Unit N> <theme>.md": one BLOCK of ten test questions (four options, one right answer) in the style
  of Part I of Assessment Test II. Frontmatter: bank_id, title, category (mt2_test_block), unit, concepts, difficulty,
  tags, origen. Each question is a "## Qnn.k <short title>" section:

      ## Q07.3 Lever rule on the eutectic isotherm

      - id: B07-Q3
      - concept_id: u4-lever-rule-eutectic
      - format: numeric            (one of FORMATS)
      - asks: calculation          (one of ASKS)
      - calc: (61.9-40)/(61.9-18.3)*100      (numeric questions: the number of the right option, recomputed)
      - check: 250 < 6000/(pi*2.5**2) < 310  (optional: a condition the stated answer relies on; must be true)

      Statement (paragraphs, $...$ and $$...$$ math, optionally one figure embed ![[attachments/MAT-MT2/<name>.svg]]).

      a) first option          (an option may be a figure embed)
      b) ...
      c) ...
      d) ...

      ### Answer
      c
      ### Explanation
      Why the right option is right, with the formula or slide. Then one bullet per wrong option, "- a) ...", naming
      the mistake that produces it.
      ### Source
      Session 7, Slide 32.

* "Problem - Bank Pnn - <title>.md": one exam-style problem of Part II, in the note format of
  tools/build_mechanics_bank.py (## Statement / ## Setup / ## (a) ... [1.2 pts] with ### Hint, ### Checkpoint,
  ### Solution / ## Interpretation), category mt2_problem, plus an optional "## Verification" section with one bullet
  per recomputed result, "- <label> | <python expression> | <stated value>", read by tools/materials_bank/verify_mt2.py.

Checks: frontmatter; ten questions per block with ids Bnn-Q1..Q10; four different options and exactly one answer; every
wrong option explained; a source per question; numeric questions recomputed (the right option matches `calc`, no wrong
option does, same unit on the four options); at most MAX_PER_CONCEPT questions per concept_id, and questions that share
a concept differ in (format, asks); the right letter is spread over a/b/c/d and never four times in a row in a block;
text similarity between every pair of questions (statement + options) below SIM_FAIL, pairs above SIM_WARN reported;
subquestion points add up; balanced $ and $$; no emojis, no "Phase N" labels, no \\euro; every figure exists; the index
note lists every note; unit quotas (skipped with --allow-partial while the bank is being written).

It writes problems.json and problems.js (window.AE_MAT_BANK and window.AE_MAT_BLUEPRINT_MT2, the latter read from
data/exam-blueprint-midterm-2.json), the figures of tools/figures/materials_mt2.py, and the generated blocks of the Extra
problems hub and of its two pages (midterm-2-test.html, midterm-2-problems.html).

Usage:
    python tools/build_materials_bank.py                  # rewrite the data, the figures and the pages
    python tools/build_materials_bank.py --check          # exit 1 if they are stale or a note is invalid
    python tools/build_materials_bank.py --lint           # only validate the notes (prints the similarity report)
    python tools/build_materials_bank.py --allow-partial  # with any of the above: do not enforce the unit quotas
"""
import argparse
import difflib
import html
import json
import math
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
from figures import materials_mt2 as mt2fig  # noqa: E402

VAULT = REPO / "vault" / "02 - Aerospace Materials I"
BANK = VAULT / "Problem Bank"
OUT_DIR = REPO / "subjects" / "aerospace-materials-1" / "data"
EXTRA = REPO / "subjects" / "aerospace-materials-1" / "extra-problems"
INDEX_NOTE = "Problem Set - Aerospace Materials I Problem Bank"
HUB = EXTRA / "index.html"
TEST_PAGE, PROBLEMS_PAGE = EXTRA / "midterm-2-test.html", EXTRA / "midterm-2-problems.html"
TEST_PAGE_MT3, PROBLEMS_PAGE_MT3 = EXTRA / "midterm-3-test.html", EXTRA / "midterm-3-problems.html"
BLUEPRINT = "exam-blueprint-midterm-2.json"
BLUEPRINT_MT3 = "exam-blueprint-midterm-3.json"

TEST_CATEGORY, PROBLEM_CATEGORY, BLOCK_CATEGORY = "mt2_test_question", "mt2_problem", "mt2_test_block"
MT3_TEST_CATEGORY, MT3_PROBLEM_CATEGORY, MT3_BLOCK_CATEGORY = "mt3_test_question", "mt3_problem", "mt3_test_block"
PAGES = {
    TEST_CATEGORY: TEST_PAGE.name,
    PROBLEM_CATEGORY: PROBLEMS_PAGE.name,
    MT3_TEST_CATEGORY: TEST_PAGE_MT3.name,
    MT3_PROBLEM_CATEGORY: PROBLEMS_PAGE_MT3.name,
}
# Part II of the 2026-27 MT2 paper: one longer problem on phase diagrams (Unit 4, 3.0 points) and one shorter problem on
# mechanical properties (Unit 5, 2.0 points); Part II of MT3: one 5.0-point problem.
PROBLEM_POINTS = 5.0
MT2_UNITS = {4: "Unit 4 · Phase diagrams", 5: "Unit 5 · Mechanical properties", 6: "Unit 6 · Electrical properties",
             7: "Unit 7 · Magnetic and thermal properties"}
MT3_UNITS = {8: "Unit 8 · Ceramic materials", 9: "Unit 9 · Polymers", 10: "Unit 10 · Composite materials",
             11: "Unit 11 · Adhesives"}
UNITS = {**MT2_UNITS, **MT3_UNITS}
EXAM_FOR_UNIT = {**{u: "midterm-2" for u in MT2_UNITS}, **{u: "midterm-3" for u in MT3_UNITS}}
# Minimum number of test questions per unit.
MT2_QUOTAS = {4: 150, 5: 170, 6: 150, 7: 150}
MT3_QUOTAS = {8: 140, 9: 140, 10: 140, 11: 80}
QUOTAS = {**MT2_QUOTAS, **MT3_QUOTAS}
MAX_NUMERIC_SHARE = {4: 0.16, 5: 0.16, 6: 0.08, 7: 0.08, 8: 0.08, 9: 0.08, 10: 0.08, 11: 0.08}
MIN_PROBLEMS_PER_ARCHETYPE = 4
MIN_PROBLEMS_BY_ARCHETYPE = {
    "phase-diagram-invariant": 4, "eutectic-lever-rule": 4, "fe-c-steels": 4, "tensile-test": 4, "loaded-bar": 4,
    "composite-unidirectional": 4, "composite-hybrid-specific": 3, "composite-selection-inverse": 3,
    "ceramic-structure": 3, "polymer-mw-crystallinity": 3,
}
FORMATS = {
    "true-statement": "Which of the following statements is TRUE",
    "false-statement": "Which of the following statements is FALSE",
    "topic-true": "Referring to / Regarding ... (pick the TRUE statement)",
    "topic-false": "Referring to / Regarding ... (pick the FALSE statement)",
    "complete-sentence": "Sentence completed by the right option",
    "cause-effect": "With an increase in ... (cause and effect)",
    "what-happens": "What will happen to ... (scenario and outcome)",
    "numeric": "Numerical calculation with four values",
    "diagram-reading": "Reading of a phase diagram or a chart",
    "choose-figure": "Which picture describes ...",
    "identify": "Which mechanism, material or property ...",
    "ordering": "Ranking of materials or values",
}
ASKS = ("definition", "cause", "effect", "calculation", "figure-reading", "comparison", "classification", "application")
ARCHETYPES = {
    "phase-diagram-invariant": "Binary diagram with intermetallics and invariant reactions",
    "eutectic-lever-rule": "Eutectic system: lever rule and microconstituents",
    "fe-c-steels": "Fe-Fe3C diagram and steel microstructures",
    "tensile-test": "Tensile test and mechanical properties",
    "loaded-bar": "Bar or rod under load: elastic check, Poisson, design and unloading",
    "composite-unidirectional": "Unidirectional composite: density, rule of mixtures, forces and strain",
    "composite-hybrid-specific": "Hybrid composite: specific modulus, specific strength and weight comparison",
    "composite-selection-inverse": "Composite design: reinforcement selection and inverse volume fraction",
    "ceramic-structure": "Ceramic crystal structure: stoichiometry, packing factor and densities",
    "polymer-mw-crystallinity": "Polymer molecular weight averages, PDI and crystallinity",
}
LEVELS = emb.LEVELS
MAX_PER_CONCEPT = 4
# Points and unit of each problem type.
ARCH_POINTS = {
    "phase-diagram-invariant": 3.0, "eutectic-lever-rule": 3.0, "fe-c-steels": 3.0,
    "tensile-test": 2.0, "loaded-bar": 2.0,
    "composite-unidirectional": 5.0, "composite-hybrid-specific": 5.0, "composite-selection-inverse": 5.0,
    "ceramic-structure": 5.0, "polymer-mw-crystallinity": 5.0,
}
ARCH_UNIT = {
    "phase-diagram-invariant": 4, "eutectic-lever-rule": 4, "fe-c-steels": 4, "tensile-test": 5, "loaded-bar": 5,
    "composite-unidirectional": 10, "composite-hybrid-specific": 10, "composite-selection-inverse": 10,
    "ceramic-structure": 8, "polymer-mw-crystallinity": 9,
}
SIM_FAIL, SIM_WARN = 0.80, 0.65
LETTERS = "abcd"
ORIGINS = ("practice", "official-exam")
QUIZ_REQUIRED = ("bank_id", "title", "category", "unit", "concepts", "difficulty", "tags", "origen")
_QUIZ_NAME = re.compile(r"Quiz - Bank (B\d{2,3}) - .+\.md$")
_PROB_NAME = re.compile(r"Problem - Bank (P\d{2,3}) - .+\.md$")
_EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
_PHASE = re.compile(r"\b(?:Phase \d|First phase|Second phase|four phases|4-phase)\b", re.I)
_EMBED = re.compile(r"!\[\[attachments/([\w-]+)/([\w-]+)\.(svg|png)\]\]")
_QHEAD = re.compile(r"Q(\d{2,3})\.(\d{1,2})\s+(.+)$")
_META = re.compile(r"^- (id|concept_id|format|asks|calc|check|origin):\s*(.+?)\s*$")
_OPT = re.compile(r"^([a-d])\)\s+(.+?)\s*$")
_CONCEPT = re.compile(r"u([4-9]|1[01])-[a-z0-9]+(?:-[a-z0-9]+)*$")
_VERIFY_FOLDERS = ("MAT-MT2", "MAT-MT3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11")
_SLIDE_META = re.compile(
    r"\b(?:the\s+slides?|Session\s+\d+|Slides?\s+\d+|Table\s+\d+[-–.]\d+)\b"
    r"|\b(?:in|from|on|of)\s+the\s+(?:course|notes|lectures?)\b"
    r"|\b(?:named|listed|given)\s+(?:in|on)\s+the\s+(?:course|slides?|notes)\b",
    re.I,
)

# Names available to `calc`, `check` and the "## Verification" expressions.
CALC_ENV = {k: getattr(math, k) for k in ("pi", "e", "sqrt", "exp", "log", "log10", "sin", "cos", "tan", "atan", "radians",
                                         "degrees", "erf")}
CALC_ENV.update({"ln": math.log, "abs": abs, "min": min, "max": max, "round": round,
                 "k_B": 8.62e-5,          # Boltzmann constant, eV/K (Session 13)
                 "k_J": 1.381e-23,        # Boltzmann constant, J/K
                 "q": 1.602e-19,          # elementary charge, C
                 "R": 8.314,              # gas constant, J/(mol K)
                 "N_A": 6.022e23,         # Avogadro's number, 1/mol
                 "mu_0": 4e-7 * math.pi,  # permeability of vacuum, H/m
                 "mu_B": 9.27e-24})       # Bohr magneton, A m^2


def evaluate(expr, where):
    try:
        return eval(expr, {"__builtins__": {}}, dict(CALC_ENV))  # noqa: S307 (expressions come from the repo's own notes)
    except Exception as exc:  # noqa: BLE001
        raise bpb.BankError(f"{where}: cannot evaluate {expr!r}: {exc}") from None


# --------------------------------------------------------------------------- figures
class Figures:
    """Figure embeds of one note. MAT-MT2 figures are the SVGs of tools/figures/materials_mt2.py; an embed of a crop
    that already exists in vault/attachments/T4..T7 (the official figure of the slides) becomes an <img>."""

    def __init__(self, folders):
        self.folders = folders      # name -> (folder, extension), read from the note before rendering
        self.count = 0
        self.used = []

    def html(self, name, numbered=True):
        folder, ext = self.folders.get(name, ("MAT-MT2", "svg"))
        if folder == "MAT-MT2" and ext == "svg":
            if name not in mt2fig.REG.web:
                raise bpb.BankError(f"unknown figure {name!r} (not drawn in tools/figures/mat_mt2/)")
            self.used.append(name)
            body, cap = mt2fig.REG.web[name], mt2fig.REG.captions[name]
        else:
            rel = f"vault/attachments/{folder}/{name}.{ext}"
            if folder not in _VERIFY_FOLDERS or not (REPO / rel).is_file():
                raise bpb.BankError(f"figure {rel} does not exist")
            cap = f"Reference diagram ({name})"
            body = (f'<figure class="slide-figure" style="margin:0"><img src="../../../{rel}" alt="{html.escape(cap)}" '
                    'loading="lazy" style="max-width:min(100%,560px);height:auto;display:block;margin:0 auto;'
                    'background:#fff;border-radius:8px;padding:8px"></figure>')
        if not numbered:
            return f'<span class="mcq-figure">{body}</span>'
        self.count += 1
        cap = html.escape(html.unescape(cap), quote=False)
        return f'<div class="diagram-card">\n{body}\n<div class="diagram-caption">Figure {self.count}. {cap}.</div>\n</div>'

    def __call__(self, name):
        return self.html(name)


def _figures_for(text, where):
    folders = {}
    for folder, name, ext in _EMBED.findall(text):
        if folders.setdefault(name, (folder, ext)) != (folder, ext):
            raise bpb.BankError(f"{where}: figure name {name!r} is used from two folders")
    return Figures(folders)


def _common_checks(text, where):
    if _EMOJI.search(text):
        raise bpb.BankError(f"{where}: emojis are not allowed")
    if re.search(r"\\text\{[^{}]*·", text):
        raise bpb.BankError(f"{where}: '·' inside \\text{{}} breaks KaTeX; close the text and use \\cdot")
    if "\\euro" in text:
        raise bpb.BankError(f"{where}: \\euro is undefined in KaTeX")
    m = _PHASE.search(text)
    if m:
        raise bpb.BankError(f"{where}: visible label {m.group(0)!r} is not allowed (lecturer's order, no phases)")
    if "$$" in re.sub(r"\$\$.*?\$\$", "", text, flags=re.S):
        raise bpb.BankError(f"{where}: unbalanced $$ delimiters")
    for n, line in enumerate(text.split("\n"), 1):
        if re.sub(r"\\\$", "", re.sub(r"\$\$.*?\$\$", "", line)).count("$") % 2:
            raise bpb.BankError(f"{where}: unbalanced $ on line {n}: {line[:60]!r}")


def _join_display_math(body):
    return re.sub(r"(?m)^[ \t]*\$\$[ \t]*\n(.*?)\n[ \t]*\$\$[ \t]*$",
                  lambda mm: "$$" + " ".join(x.strip() for x in mm.group(1).split("\n")) + "$$", body, flags=re.S)


# --------------------------------------------------------------------------- numbers in options
_NUMBER = re.compile(
    r"(-?\d+(?:\.\d+)?)\s*(?:(?:\\times|\\cdot|×|x)\s*10\s*\^?\s*\{?\s*(-?\d+)\s*\}?|[eE](-?\d+))?")


def leading_number(text):
    """First number of an option, with its power of ten: '$2.5\\times10^{-4}$ mm' -> (2.5e-4, 'mm'). None if no number."""
    plain = re.sub(r"\\(?:,|;|!| )", " ", text.replace("$", " ").replace("−", "-").replace("{,}", ""))
    plain = re.sub(r"\\(?:text|mathrm)\{([^}]*)\}", r"\1", plain)
    m = _NUMBER.search(plain)
    if not m:
        return None
    value = float(m.group(1)) * 10 ** int(m.group(2) or m.group(3) or 0)
    return value, re.sub(r"\s+", " ", plain[m.end():]).strip(" .")


def _close(a, b, rel):
    return abs(a - b) <= rel * max(abs(a), abs(b), 1e-300)


# --------------------------------------------------------------------------- quiz notes
def parse_quiz_note(path):
    where = path.name
    m = _QUIZ_NAME.match(path.name)
    if not m:
        raise bpb.BankError(f"{where}: name must be 'Quiz - Bank Bnn - <Unit N> <theme>.md'")
    text = path.read_text(encoding="utf-8")
    _common_checks(text, where)
    meta, body = bpb.frontmatter(text, where)
    missing = [k for k in QUIZ_REQUIRED if k not in meta]
    if missing:
        raise bpb.BankError(f"{where}: frontmatter lacks {', '.join(missing)}")
    if meta["bank_id"] != m.group(1):
        raise bpb.BankError(f"{where}: bank_id {meta['bank_id']} does not match the file name")
    unit = meta["unit"]
    if unit not in UNITS or meta["difficulty"] not in (1, 2, 3):
        raise bpb.BankError(f"{where}: unit must be in {sorted(UNITS)} and difficulty 1-3")
    expected_block_cat = BLOCK_CATEGORY if unit in MT2_UNITS else MT3_BLOCK_CATEGORY
    test_cat = TEST_CATEGORY if unit in MT2_UNITS else MT3_TEST_CATEGORY
    if meta["category"] != expected_block_cat:
        raise bpb.BankError(f"{where}: category must be {expected_block_cat}")
    if f"Unit {unit}" not in path.name:
        raise bpb.BankError(f"{where}: the file name must carry 'Unit {unit}'")
    if "Practice item, not an official exercise" not in body and "Includes official exam questions" not in body:
        raise bpb.BankError(f"{where}: lacks the 'Practice item, not an official exercise' callout")
    body = _join_display_math(body.split("**Back to:**")[0])
    figs = _figures_for(body, where)
    block_id = meta["bank_id"]
    questions = []
    for part in re.split(r"\n## ", "\n" + body)[1:]:
        head, _, rest = part.partition("\n")
        hm = _QHEAD.match(head.strip())
        if not hm:
            raise bpb.BankError(f"{where}: unexpected section '## {head.strip()}' (questions are '## Qnn.k <title>')")
        if hm.group(1) != block_id[1:]:
            raise bpb.BankError(f"{where}: '## {head.strip()}' does not belong to block {block_id}")
        questions.append(_question(block_id, int(hm.group(2)), hm.group(3).strip(), rest, meta, where, figs, path, test_cat))
    numbers = [q["number"] for q in questions]
    if numbers != list(range(1, 11)):
        raise bpb.BankError(f"{where}: a block has questions 1 to 10 in order, got {numbers}")
    answers = "".join(q["answer"] for q in questions)
    run = re.search(r"(.)\1{3}", answers)
    if run:
        raise bpb.BankError(f"{where}: the right answer is '{run.group(1)}' four times in a row ({answers})")
    listed = set(meta["concepts"])
    used = {q["concept_id"] for q in questions}
    if listed != used:
        raise bpb.BankError(f"{where}: frontmatter concepts and the questions' concept_id differ: "
                            f"{sorted(listed ^ used)}")
    return {"id": block_id, "unit": unit, "exam": EXAM_FOR_UNIT[unit], "title": meta["title"],
            "difficulty": meta["difficulty"],
            "tags": [t for t in meta["tags"] if t != "problem-bank"], "source": meta["origen"],
            "vault_note": path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.name,
            "figures": figs.used, "questions": questions}


def _question(block_id, number, title, rest, meta, where, figs, path, test_cat=TEST_CATEGORY):
    qid = f"{block_id}-Q{number}"
    where = f"{where} {qid}"
    sections = re.split(r"\n### ", "\n" + rest)
    named = {}
    for sec in sections[1:]:
        name, _, text = sec.partition("\n")
        if name.strip() not in ("Answer", "Explanation", "Source") or name.strip() in named:
            raise bpb.BankError(f"{where}: unexpected or repeated '### {name.strip()}'")
        named[name.strip()] = text.strip("\n")
    for need in ("Answer", "Explanation", "Source"):
        if not named.get(need, "").strip():
            raise bpb.BankError(f"{where}: lacks its '### {need}'")
    info, stem, options = {}, [], {}
    for line in sections[0].split("\n"):
        mm = _META.match(line)
        om = _OPT.match(line)
        if mm and not any(x.strip() for x in stem) and not options:
            if mm.group(1) in info:
                raise bpb.BankError(f"{where}: '{mm.group(1)}' given twice")
            info[mm.group(1)] = mm.group(2)
        elif om:
            if om.group(1) in options:
                raise bpb.BankError(f"{where}: option {om.group(1)}) given twice")
            options[om.group(1)] = om.group(2)
        elif options and line.strip():
            raise bpb.BankError(f"{where}: text after the options: {line[:50]!r}")
        else:
            stem.append(line)
    if info.get("id") != qid:
        raise bpb.BankError(f"{where}: '- id:' must be {qid}")
    cm = _CONCEPT.match(info.get("concept_id", ""))
    if not cm or int(cm.group(1)) != meta["unit"]:
        raise bpb.BankError(f"{where}: concept_id must look like u{meta['unit']}-<kebab-case>")
    if info.get("format") not in FORMATS:
        raise bpb.BankError(f"{where}: unknown format {info.get('format')!r}")
    if info.get("asks") not in ASKS:
        raise bpb.BankError(f"{where}: unknown asks {info.get('asks')!r}")
    origin = info.get("origin", "practice")
    if origin not in ORIGINS:
        raise bpb.BankError(f"{where}: unknown origin {origin!r} (must be one of {ORIGINS})")
    if "".join(sorted(options)) != LETTERS:
        raise bpb.BankError(f"{where}: needs the four options a) to d), got {sorted(options)}")
    if not any(x.strip() for x in stem):
        raise bpb.BankError(f"{where}: no statement")
    norm = [re.sub(r"\W+", "", options[k]).lower() for k in LETTERS]
    if len(set(norm)) != 4:
        raise bpb.BankError(f"{where}: two options are the same")
    answer = named["Answer"].strip().rstrip(")").lower()
    if answer not in LETTERS or len(answer) != 1:
        raise bpb.BankError(f"{where}: '### Answer' must be one letter a-d, got {named['Answer'].strip()!r}")

    lead, distractors, current = [], {}, None
    for line in named["Explanation"].split("\n"):
        dm = re.match(r"^- ([a-d])\)\s+(.+)$", line)
        if dm:
            current = dm.group(1)
            if current in distractors:
                raise bpb.BankError(f"{where}: option {current}) is explained twice")
            distractors[current] = dm.group(2).strip()
        elif current and line.strip():
            distractors[current] += " " + line.strip()
        elif not current:
            lead.append(line)
    wrong = [k for k in LETTERS if k != answer]
    if sorted(distractors) != wrong:
        raise bpb.BankError(f"{where}: the explanation needs one bullet '- x) ...' per wrong option "
                            f"({', '.join(wrong)}), got {sorted(distractors)}")
    if not any(x.strip() for x in lead):
        raise bpb.BankError(f"{where}: the explanation must first say why {answer}) is right")
    for k, v in distractors.items():
        if len(v) < 25:
            raise bpb.BankError(f"{where}: the explanation of {k}) does not name the mistake behind it")

    calc = None
    if info.get("format") == "numeric" and "calc" not in info:
        raise bpb.BankError(f"{where}: a numeric question needs '- calc: <expression>'")
    if "calc" in info:
        calc = float(evaluate(info["calc"], where))
        nums = {k: leading_number(options[k]) for k in LETTERS}
        if any(v is None for v in nums.values()):
            raise bpb.BankError(f"{where}: every option of a question with 'calc' starts with a number")
        if len({v[1] for v in nums.values()}) != 1:
            raise bpb.BankError(f"{where}: the four options must carry the same unit, got {sorted({v[1] for v in nums.values()})}")
        if not _close(nums[answer][0], calc, 0.012):
            raise bpb.BankError(f"{where}: calc gives {calc:.6g} but option {answer}) is {nums[answer][0]:g}")
        for k in wrong:
            if _close(nums[k][0], calc, 0.03):
                raise bpb.BankError(f"{where}: wrong option {k}) = {nums[k][0]:g} coincides with the right value {calc:.6g}")
    if "check" in info and evaluate(info["check"], where) is not True:
        raise bpb.BankError(f"{where}: check {info['check']!r} is not true")

    def option_html(text):
        em = _EMBED.fullmatch(text.strip())
        return figs.html(em.group(2), numbered=False) if em else bt.inline(text)

    plain_stem = " ".join(x.strip() for x in stem if x.strip() and not _EMBED.search(x))
    sm = _SLIDE_META.search(plain_stem)
    if sm:
        raise bpb.BankError(f"{where}: stem must not mention slides, course notes or slide tables: {sm.group(0)!r}")
    return {
        "id": qid, "category": test_cat, "kind": "multiple_choice", "block": block_id, "number": number,
        "unit": meta["unit"], "concept_id": info["concept_id"], "theme": info["concept_id"], "format": info["format"],
        "asks": info["asks"], "origin": origin, "title": title, "difficulty": meta["difficulty"], "points": 0.5,
        "statement_html": emb.render(list(stem), where, figs),
        "options": [{"label": k, "html": option_html(options[k])} for k in LETTERS],
        "answer": answer,
        "explanation_html": emb.render(list(lead), where, figs),
        "distractors": {k: bt.inline(v) for k, v in distractors.items()},
        "source_html": emb.render(named["Source"].split("\n"), where, figs),
        "calc": info.get("calc"), "check": info.get("check"),
        "vault_note": path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.name,
        # for the similarity check an option that is only a picture counts as its figure name
        "_text": plain_stem + " || " + " | ".join(_EMBED.sub(lambda m: m.group(2), options[k]) for k in LETTERS),
    }


# --------------------------------------------------------------------------- problem notes
def parse_problem_note(path):
    where = path.name
    m = _PROB_NAME.match(path.name)
    if not m:
        raise bpb.BankError(f"{where}: name must be 'Problem - Bank Pnn - <title>.md'")
    text = path.read_text(encoding="utf-8")
    _common_checks(text, where)
    meta, body = bpb.frontmatter(text, where)
    missing = [k for k in emb.REQUIRED if k not in meta]
    if missing:
        raise bpb.BankError(f"{where}: frontmatter lacks {', '.join(missing)}")
    if meta["bank_id"] != m.group(1):
        raise bpb.BankError(f"{where}: bank_id {meta['bank_id']} does not match the file name")
    unit = meta["unit"]
    if unit not in UNITS or meta["difficulty"] not in (1, 2, 3):
        raise bpb.BankError(f"{where}: unit must be in {sorted(UNITS)} and difficulty 1-3")
    expected_prob_cat = PROBLEM_CATEGORY if unit in MT2_UNITS else MT3_PROBLEM_CATEGORY
    if meta["category"] != expected_prob_cat:
        raise bpb.BankError(f"{where}: category must be {expected_prob_cat}")
    points = float(meta["points"])
    if meta["archetype"] not in ARCHETYPES:
        raise bpb.BankError(f"{where}: unknown archetype {meta['archetype']!r}")
    if points != ARCH_POINTS[meta["archetype"]]:
        raise bpb.BankError(f"{where}: a {meta['archetype']} problem is worth {ARCH_POINTS[meta['archetype']]} points, not {points}")
    if unit != ARCH_UNIT[meta["archetype"]]:
        raise bpb.BankError(f"{where}: a {meta['archetype']} problem belongs to unit {ARCH_UNIT[meta['archetype']]}")
    if meta["level"] not in LEVELS:
        raise bpb.BankError(f"{where}: unknown level {meta['level']!r}")
    if "Practice item, not an official exercise" not in body and "Includes official exam adaptation" not in body:
        raise bpb.BankError(f"{where}: lacks the 'Practice item, not an official exercise' callout")
    body = _join_display_math(body.split("**Back to:**")[0])
    figs = _figures_for(body, where)
    item = {
        "id": meta["bank_id"], "category": expected_prob_cat, "archetype": meta["archetype"], "theme": meta["archetype"],
        "level": meta["level"], "unit": unit, "title": meta["title"], "difficulty": meta["difficulty"],
        "points": points, "time_minutes": meta["time_minutes"], "tags": [t for t in meta["tags"] if t != "problem-bank"],
        "official": bool(meta.get("official", False)), "source": meta["origen"],
        "vault_note": path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.name,
        "statement_html": None, "setup_html": None, "subquestions": [], "interpretation_html": None,
        "figures": [], "verify": [],
    }
    try:
        for part in re.split(r"\n## ", "\n" + body)[1:]:
            head, _, rest = part.partition("\n")
            head, lines = head.strip(), rest.split("\n")
            if head in ("Statement", "Setup", "Interpretation"):
                item[f"{head.lower()}_html"] = emb.render(lines, where, figs)
            elif head == "Verification":
                item["verify"] = _verify_lines(lines, where)
            elif emb._SUB.match(head):
                item["subquestions"].append(emb.subquestion(head, rest, where, figs))
            else:
                raise bpb.BankError(f"{where}: unexpected section '## {head}'")
    except (ValueError, KeyError) as exc:
        if isinstance(exc, bpb.BankError):
            raise
        raise bpb.BankError(f"{where}: {exc}") from None
    item["figures"] = figs.used
    if not item["statement_html"]:
        raise bpb.BankError(f"{where}: no '## Statement' section")
    labels = [s["label"] for s in item["subquestions"]]
    if not labels or labels != [chr(ord("a") + i) for i in range(len(labels))]:
        raise bpb.BankError(f"{where}: subquestions must be (a), (b), ... in order, got {labels}")
    total = round(sum(s["points"] for s in item["subquestions"]), 4)
    if total != points:
        raise bpb.BankError(f"{where}: subquestion points add up to {total}, not {points}")
    for sub in item["subquestions"]:
        if 'class="step-title"' not in sub["solution_html"]:
            raise bpb.BankError(f"{where}: the solution of ({sub['label']}) needs '#### ' step titles (one box per step)")
    return item


def _verify_lines(lines, where):
    out = []
    for line in lines:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.strip().removeprefix("- ").split("|")]
        if not line.strip().startswith("- ") or len(parts) != 3:
            raise bpb.BankError(f"{where}: a Verification line is '- <label> | <expression> | <stated value>', got {line[:60]!r}")
        try:
            stated = float(parts[2])
        except ValueError:
            raise bpb.BankError(f"{where}: the stated value of {parts[0]!r} is not a number: {parts[2]!r}") from None
        out.append({"label": parts[0], "expr": parts[1], "stated": stated, "text": parts[2]})
    return out


# --------------------------------------------------------------------------- bank-wide checks
def _shingles(text):
    t = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    words = t.split()
    return t, set(zip(words, words[1:])) | set(words)


def similarity_report(questions):
    """Pairs of questions whose normalised text (statement + options) is alike: [(ratio, id1, id2)] over SIM_WARN."""
    prepared = [(q["id"],) + _shingles(q["_text"]) for q in questions]
    pairs = []
    for i, (ida, ta, sa) in enumerate(prepared):
        for idb, tb, sb in prepared[i + 1:]:
            union = len(sa | sb)
            if not union or len(sa & sb) / union < 0.30:
                continue
            ratio = difflib.SequenceMatcher(None, ta, tb, autojunk=False).ratio()
            if ratio >= SIM_WARN:
                pairs.append((round(ratio, 3), ida, idb))
    return sorted(pairs, reverse=True)


def check_bank(blocks, problems, partial=False):
    """Bank-wide rules. Returns the similarity pairs to review (between SIM_WARN and SIM_FAIL)."""
    questions = [q for b in blocks for q in b["questions"]]
    by_concept = {}
    for q in questions:
        by_concept.setdefault(q["concept_id"], []).append(q)
    for concept, qs in sorted(by_concept.items()):
        if len(qs) > MAX_PER_CONCEPT:
            raise bpb.BankError(f"concept {concept} has {len(qs)} questions (maximum {MAX_PER_CONCEPT}): "
                                f"{', '.join(q['id'] for q in qs)}")
        seen = {}
        for q in qs:
            key = (q["format"], q["asks"])
            if key in seen:
                raise bpb.BankError(f"concept {concept}: {seen[key]} and {q['id']} share format and question type "
                                    f"{key}; questions on one concept must differ in format or in what they ask")
            seen[key] = q["id"]
    pairs = similarity_report(questions)
    too_close = [p for p in pairs if p[0] >= SIM_FAIL]
    if too_close:
        raise bpb.BankError("questions too similar (>= %.2f): " % SIM_FAIL +
                            "; ".join(f"{a} ~ {b} ({r:.2f})" for r, a, b in too_close[:12]))
    if questions and not partial:
        for unit, minimum in QUOTAS.items():
            u_qs = [q for q in questions if q["unit"] == unit]
            n = len(u_qs)
            if n < minimum:
                raise bpb.BankError(f"unit {unit} has {n} test questions, the quota is {minimum}")
            num_share = sum(q["format"] == "numeric" for q in u_qs) / n
            if num_share > MAX_NUMERIC_SHARE[unit]:
                raise bpb.BankError(f"unit {unit} has {num_share:.1%} numeric questions (max {MAX_NUMERIC_SHARE[unit]:.0%})")
        for label, group in (("Midterm 2", [q for q in questions if q["unit"] in MT2_UNITS]),
                             ("Midterm 3", [q for q in questions if q["unit"] in MT3_UNITS])):
            if not group:
                continue
            share = {k: sum(q["answer"] == k for q in group) / len(group) for k in LETTERS}
            off = {k: round(v, 3) for k, v in share.items() if not 0.20 <= v <= 0.30}
            if off:
                raise bpb.BankError(f"{label}: the right answer is not spread evenly over a-d: {off}")
        for arch in ARCHETYPES:
            n = sum(p["archetype"] == arch for p in problems)
            req = MIN_PROBLEMS_BY_ARCHETYPE.get(arch, MIN_PROBLEMS_PER_ARCHETYPE)
            if n < req:
                raise bpb.BankError(f"problem type {arch} has {n} problems, the minimum is {req}")
    return [p for p in pairs if p[0] < SIM_FAIL]


def check_blueprint(blueprint, blocks, problems, partial=False, name=BLUEPRINT):
    parts = blueprint.get("parts", [])
    total = round(sum(p["count"] * p["points_each"] for p in parts), 4)
    if total != blueprint.get("total_points"):
        raise bpb.BankError(f"{name}: parts add up to {total}, not {blueprint.get('total_points')}")
    for part in parts:
        if part.get("type") == "multiple_choice":
            for key in ("points_correct", "points_wrong", "points_blank", "floor"):
                if not isinstance(part.get(key), (int, float)):
                    raise bpb.BankError(f"{name}: {part['id']} lacks the number {key}")
            if part["points_correct"] != part["points_each"]:
                raise bpb.BankError(f"{name}: {part['id']} points_correct must equal points_each")
            per_unit = part.get("selection_rules", {}).get("per_unit", {})
            if per_unit and sum(per_unit.values()) != part["count"]:
                raise bpb.BankError(f"{name}: {part['id']} per_unit adds up to {sum(per_unit.values())}, not {part['count']}")
            if not partial:
                for unit, n in per_unit.items():
                    have = sum(len(b["questions"]) for b in blocks if b["unit"] == int(unit))
                    if have < 2 * n:
                        raise bpb.BankError(f"{name}: unit {unit} needs at least {2 * n} test questions")
        else:
            rules = part.get("selection_rules", {})
            kinds = rules.get("archetypes", []) + rules.get("must_archetypes", [])
            if not kinds:
                raise bpb.BankError(f"{name}: {part['id']} must list its problem types (archetypes or must_archetypes)")
            for a in kinds:
                if ARCH_POINTS.get(a) != part["points_each"]:
                    raise bpb.BankError(f"{name}: {part['id']} is worth {part['points_each']} points but {a} problems are worth {ARCH_POINTS.get(a)}")
            for a in kinds:
                if a not in ARCHETYPES or (not partial and not any(p["archetype"] == a for p in problems)):
                    raise bpb.BankError(f"{name}: archetype {a!r} has no problem in the bank")
    _check_modes(blueprint, parts, blocks, problems, partial, name)


def _check_modes(blueprint, parts, blocks, problems, partial, name=BLUEPRINT):
    """Practice scopes ("modes") read by assets/js/exam-simulator.js."""
    modes = blueprint.get("modes")
    if modes is None:
        return
    mc = next((p for p in parts if p.get("type") == "multiple_choice"), None)
    if mc is None or not isinstance(modes, list) or not modes:
        raise bpb.BankError(f"{name}: modes need a list and a multiple-choice part")
    ids = [m.get("id") for m in modes]
    if len(set(ids)) != len(ids) or not all(isinstance(i, str) and re.fullmatch(r"[\w-]+", i) for i in ids):
        raise bpb.BankError(f"{name}: mode ids must be unique words, got {ids}")
    if sum(1 for m in modes if m.get("default")) != 1:
        raise bpb.BankError(f"{name}: exactly one mode must be the default")
    part_ids = {p["id"] for p in parts}
    for m in modes:
        where = f"{name}: mode {m['id']}"
        if not m.get("label") or not m.get("description"):
            raise bpb.BankError(f"{where} needs a label and a description")
        if "duration_minutes" in m:
            if m["duration_minutes"] not in m.get("duration_options_minutes", []):
                raise bpb.BankError(f"{where}: duration_minutes must be one of its duration_options_minutes")
        if isinstance(m.get("parts"), list):
            if not m["parts"] or any(pid not in part_ids for pid in m["parts"]):
                raise bpb.BankError(f"{where}: parts must list valid part ids from {sorted(part_ids)}")
            if m.get("unit_picker"):
                ul = blueprint.get("unit_labels")
                if not isinstance(ul, dict) or not ul or any(int(u) not in UNITS for u in ul):
                    raise bpb.BankError(f"{where}: unit_picker needs blueprint unit_labels in {sorted(UNITS)}")
                opts = m.get("count_options")
                if not isinstance(opts, list) or not opts or m.get("default_count") not in opts:
                    raise bpb.BankError(f"{where}: unit_picker needs count_options containing default_count")
                if not partial:
                    for u in ul:
                        have = sum(len(b["questions"]) for b in blocks if b["unit"] == int(u))
                        if have < 10:
                            raise bpb.BankError(f"{where}: unit {u} needs at least 10 test questions, has {have}")
            if m.get("archetype_picker"):
                arches = m.get("archetypes")
                if arches is None:
                    arches = []
                    for p in parts:
                        if p["id"] in m["parts"] and p.get("type") != "multiple_choice":
                            r = p.get("selection_rules", {})
                            arches += r.get("archetypes", []) + r.get("must_archetypes", [])
                if not arches or any(a not in ARCHETYPES for a in arches):
                    raise bpb.BankError(f"{where}: archetype_picker needs valid archetypes")
                if not partial:
                    for a in arches:
                        if not any(p["archetype"] == a for p in problems):
                            raise bpb.BankError(f"{where}: archetype {a!r} has no problem in the bank")
            continue
        per_unit = m.get("per_unit")
        if not isinstance(per_unit, dict) or not per_unit:
            raise bpb.BankError(f"{where} needs per_unit")
        if any(int(u) not in UNITS or not isinstance(n, int) or n < 1 for u, n in per_unit.items()):
            raise bpb.BankError(f"{where}: per_unit must map the units {sorted(UNITS)} to positive whole numbers")
        if sum(per_unit.values()) != mc["count"]:
            raise bpb.BankError(f"{where}: per_unit adds up to {sum(per_unit.values())}, not {mc['count']}")
        if not m.get("include_problem", True):
            if mc["points_total"] != round(mc["count"] * mc["points_each"], 4):
                raise bpb.BankError(f"{where}: the test alone must add up to {mc['points_total']}")
        if not partial:
            for u, n in per_unit.items():
                unit_blocks = [b for b in blocks if b["unit"] == int(u)]
                have = sum(len(b["questions"]) for b in unit_blocks)
                if have < 2 * n:
                    raise bpb.BankError(f"{where}: unit {u} needs at least {2 * n} test questions, has {have}")
                if len(unit_blocks) < n:
                    raise bpb.BankError(f"{where}: unit {u} has {len(unit_blocks)} blocks for {n} questions of different blocks")


def load_bank(bank_dir=BANK, partial=False, index=True):
    bank_dir = pathlib.Path(bank_dir)
    mt2fig.build()
    quiz_paths = sorted(bank_dir.glob("Quiz - Bank *.md"))
    prob_paths = sorted(bank_dir.glob("Problem - Bank *.md"))
    blocks = [parse_quiz_note(p) for p in quiz_paths]
    problems = [parse_problem_note(p) for p in prob_paths]
    ids = [b["id"] for b in blocks] + [p["id"] for p in problems]
    dup = sorted({x for x in ids if ids.count(x) > 1})
    if dup:
        raise bpb.BankError(f"duplicate bank ids: {', '.join(dup)}")
    if index:
        note = bank_dir / f"{INDEX_NOTE}.md"
        if not note.is_file():
            raise bpb.BankError(f"missing index note {INDEX_NOTE}.md")
        listed = note.read_text(encoding="utf-8")
        unlisted = [p.stem for p in quiz_paths + prob_paths if f"[[{p.stem}" not in listed]
        if unlisted:
            raise bpb.BankError(f"{INDEX_NOTE} does not list: {', '.join(unlisted)}")
    blocks.sort(key=lambda b: int(b["id"][1:]))
    problems.sort(key=lambda p: int(p["id"][1:]))
    review = check_bank(blocks, problems, partial)
    if bank_dir == BANK and not partial:
        used = {f for b in blocks for f in b["figures"]} | {f for p in problems for f in p["figures"]}
        unused = sorted(set(mt2fig.FIGURES) - used)
        if unused:
            raise bpb.BankError(f"figures drawn but not used by any note: {', '.join(unused)}")
    return blocks, problems, review


def build(partial=False):
    blocks, problems, review = load_bank(partial=partial)
    questions = [{k: v for k, v in q.items() if not k.startswith("_")} for b in blocks for q in b["questions"]]
    mt2_blocks = [b for b in blocks if b["unit"] in MT2_UNITS]
    mt3_blocks = [b for b in blocks if b["unit"] in MT3_UNITS]
    mt2_problems = [p for p in problems if p["unit"] in MT2_UNITS]
    mt3_problems = [p for p in problems if p["unit"] in MT3_UNITS]
    data = {
        "_comment": "Generated by tools/build_materials_bank.py from vault/02 - Aerospace Materials I/Problem Bank/. Do not edit by hand.",
        "subject": "aerospace-materials-1",
        "categories": {
            TEST_CATEGORY: {"label": "2nd Midterm test questions", "points": 0.5},
            PROBLEM_CATEGORY: {"label": "2nd Midterm Part II problems", "points": PROBLEM_POINTS},
            MT3_TEST_CATEGORY: {"label": "3rd Midterm test questions", "points": 0.5},
            MT3_PROBLEM_CATEGORY: {"label": "3rd Midterm Part II problems", "points": PROBLEM_POINTS},
        },
        "archetype_points": ARCH_POINTS,
        "pages": PAGES, "archetypes": ARCHETYPES, "levels": LEVELS, "formats": FORMATS,
        "units": {str(k): v for k, v in UNITS.items()},
        "counts": {
            TEST_CATEGORY: sum(q["category"] == TEST_CATEGORY for q in questions),
            PROBLEM_CATEGORY: len(mt2_problems),
            BLOCK_CATEGORY: len(mt2_blocks),
            MT3_TEST_CATEGORY: sum(q["category"] == MT3_TEST_CATEGORY for q in questions),
            MT3_PROBLEM_CATEGORY: len(mt3_problems),
            MT3_BLOCK_CATEGORY: len(mt3_blocks),
        },
        "blocks": [
            {"id": b["id"], "unit": b["unit"], "exam": b["exam"], "title": b["title"],
             "items": [q["id"] for q in b["questions"]]}
            for b in blocks
        ],
        "items": questions + problems,
    }
    bp2 = json.loads((OUT_DIR / BLUEPRINT).read_text(encoding="utf-8"))
    check_blueprint(bp2, mt2_blocks, mt2_problems, partial, name=BLUEPRINT)
    js = ("/* Generated by tools/build_materials_bank.py (same data as problems.json). Do not edit by hand. */\n"
          f"window.AE_MAT_BANK = {json.dumps(data, ensure_ascii=False)};\n"
          f"/* The exam structure of data/{BLUEPRINT}, for the Exam Simulator. */\n"
          f"window.AE_MAT_BLUEPRINT_MT2 = {json.dumps(bp2, ensure_ascii=False)};\n")
    bp3_path = OUT_DIR / BLUEPRINT_MT3
    bp3 = None
    if bp3_path.is_file():
        bp3 = json.loads(bp3_path.read_text(encoding="utf-8"))
        check_blueprint(bp3, mt3_blocks, mt3_problems, partial, name=BLUEPRINT_MT3)
        js += (f"/* The exam structure of data/{BLUEPRINT_MT3}, for the Exam Simulator. */\n"
               f"window.AE_MAT_BLUEPRINT_MT3 = {json.dumps(bp3, ensure_ascii=False)};\n")
    outputs = {OUT_DIR / "problems.json": json.dumps(data, indent=1, ensure_ascii=False) + "\n", OUT_DIR / "problems.js": js}
    renders = [
        (HUB, render_hub(blocks, problems), emb._HUB_BLOCK),
        (TEST_PAGE, render_test_page(mt2_blocks, bp2, exam_num="II", units=MT2_UNITS), emb._PAGE_BLOCK),
        (PROBLEMS_PAGE, render_problems_page(mt2_problems), emb._PAGE_BLOCK),
    ]
    if bp3 is not None and TEST_PAGE_MT3.is_file():
        renders.append((TEST_PAGE_MT3, render_test_page(mt3_blocks, bp3, exam_num="III", units=MT3_UNITS), emb._PAGE_BLOCK))
    if PROBLEMS_PAGE_MT3.is_file():
        renders.append((PROBLEMS_PAGE_MT3, render_problems_page_mt3(mt3_problems), emb._PAGE_BLOCK))
    for path, block, pattern in renders:
        if path.is_file():
            page = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
            outputs[path] = emb._fill(pattern, path, page, block)
    return outputs, data, review


# --------------------------------------------------------------------------- the Extra problems pages
def _mc_part(blueprint):
    return next(p for p in blueprint["parts"] if p.get("type") == "multiple_choice")


def _question_html(q):
    opts = "\n".join(f'            <li class="mcq-option"><span class="mcq-letter">{o["label"]})</span> '
                     f'<span class="mcq-text">{o["html"]}</span></li>' for o in q["options"])
    wrong = "\n".join(f'              <li><strong>{k})</strong> {v}</li>' for k, v in sorted(q["distractors"].items()))
    badge = '<span class="mcq-origin-badge">Official exam</span>' if q.get("origin") == "official-exam" else ""
    return "\n".join([
        f'        <div class="phase-block mcq-item" id="{q["id"]}">',
        f'          <h3 class="phase-title">Question {q["number"]} · {html.escape(q["title"])}</h3>',
        '          <div class="prompt">' + q["statement_html"] + "</div>",
        '          <ul class="mcq-options">', opts, "          </ul>",
        '          <details class="mcq-answer">',
        "            <summary>Answer and explanation</summary>",
        f'            <p class="mcq-right"><strong>Answer: {q["answer"]})</strong></p>',
        q["explanation_html"],
        '            <p class="mcq-why">Why the other options are wrong:</p>',
        '            <ul class="mcq-distractors">', wrong, "            </ul>",
        f'            <div class="mcq-source"><span class="mcq-source__label">Source.</span> ' + q["source_html"] + badge + "</div>",
        "          </details>",
        "        </div>"])


def _block_card(block, mc, exam_num="II"):
    has_official = any(q.get("origin") == "official-exam" for q in block["questions"])
    note_tag = "Includes official exam questions" if has_official else "Practice item, not an official exercise"
    tag = (f"Test block · {UNITS[block['unit']].split(' · ')[0]} · 10 questions · "
           f"+{mc['points_correct']:g} right, {mc['points_wrong']:g} wrong · {note_tag}")
    return "\n".join([
        f'      <section class="problem-box" id="{block["id"]}">',
        f'        <span class="problem-tag">{html.escape(tag)}</span>',
        f'        <h4 class="problem-title">{block["id"]} — {html.escape(block["title"])}</h4>',
        '        <div class="statement-box">',
        f'<p>Ten test questions on {html.escape(UNITS[block["unit"]].split(" · ")[1].lower())}, written for this portal in '
        f'the style of Part I of Assessment Test {exam_num}. Each question has four options and only one is right. Answer all ten '
        'before opening any explanation.</p>',
        "        </div>",
        "\n".join(_question_html(q) for q in block["questions"]),
        "      </section>"])


def render_test_page(blocks, blueprint, exam_num="II", units=MT2_UNITS):
    mc = _mc_part(blueprint)
    n = sum(len(b["questions"]) for b in blocks)
    sim_q = "" if exam_num == "II" else "?exam=midterm-3"
    u_lo, u_hi = min(units), max(units)
    if not blocks:
        return (f'      <p class="midterm-part-lead">Test blocks for Assessment Test {exam_num} (Units {u_lo} to {u_hi}) are being '
                f'written and will appear here. Meanwhile, open the <a href="../simulator/index.html{sim_q}">Exam simulator</a>.</p>\n')
    out = [f'      <p class="midterm-part-lead">{n} test questions in {len(blocks)} blocks of ten, on Units {u_lo} to {u_hi}. Part I of '
           f'Assessment Test {exam_num} is {mc["count"]} questions with four options and one right answer: '
           f'+{mc["points_correct"]:g} points for a right answer, {mc["points_wrong"]:g} for a wrong one, '
           f'{mc["points_blank"]:g} for a blank, and the mark of the test never goes below {mc["floor"]:g}. '
           f'Blocks mark whether they hold practice items or include official exam questions. The <a href="../simulator/index.html{sim_q}">Exam simulator</a> '
           'draws a timed exam or lets you select specific units and blocks.</p>']
    for unit in units:
        mine = [b for b in blocks if b["unit"] == unit]
        if not mine:
            continue
        out.append(f'      <h2 class="mcq-unit-title" id="unit-{unit}">{html.escape(units[unit])} '
                   f'<span class="mcq-unit-count">{len(mine)} blocks</span></h2>')
        out += [_block_card(b, mc, exam_num) for b in mine]
    return "\n".join(out) + "\n"


def _problem_card(item):
    tag = (f"Part II problem · {UNITS[item['unit']].split(' · ')[0]} · {ARCHETYPES[item['archetype']]} · "
           f"{emb._pts(item['points'])} · {item['time_minutes']} min · Practice item, not an official exercise")
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
                '          <div class="result-callout"><div class="result-callout-title">Key results</div>'
                + sub["checkpoint_html"] + "</div>",
                "        </div>"]
    if item["interpretation_html"]:
        out += ['        <div class="phase-block">', '          <h3 class="phase-title">Interpretation and checks</h3>',
                item["interpretation_html"], "        </div>"]
    out.append("      </section>")
    return "\n".join(out)


def render_problems_page(problems):
    if not problems:
        return ('      <p class="midterm-part-lead">The Part II problems of the bank are being written and will appear here. '
                'Meanwhile, the official problems of Units 4 to 6 are solved on the <a href="../problemas/index.html">Problems</a> '
                'page and the test questions are on the <a href="midterm-2-test.html">test page</a>.</p>\n')
    lead = (f'      <p class="midterm-part-lead">{len(problems)} exam-style problems written for this portal. Part II of '
            'Assessment Test II this year is two problems: a longer one on phase diagrams (3 points: a binary diagram with '
            'its invariant reactions, the lever rule and the microconstituents, or the steels of the Fe-Fe<sub>3</sub>C '
            'diagram) and a shorter one on the mechanical properties of Unit 5 (2 points: a tensile test or a loaded bar). '
            'These are practice items, not official exercises. The <a href="../simulator/index.html">Exam simulator</a> '
            'draws one of each after the test.</p>')
    order = list(ARCHETYPES)
    problems = sorted(problems, key=lambda p: (ARCH_UNIT[p["archetype"]], order.index(p["archetype"]), int(p["id"][1:])))
    out = [lead]
    for unit, title in ((4, "Problem 1 · Phase diagrams (3 points)"), (5, "Problem 2 · Mechanical properties (2 points)")):
        mine = [p for p in problems if ARCH_UNIT[p["archetype"]] == unit]
        if mine:
            out.append(f'      <h2 class="mcq-unit-title" id="unit-{unit}">{title} '
                       f'<span class="mcq-unit-count">{len(mine)} problems</span></h2>')
            out += [_problem_card(p) for p in mine]
    return "\n".join(out) + "\n"


def render_problems_page_mt3(problems):
    if not problems:
        return ('      <p class="midterm-part-lead">The Part II problems of Assessment Test III are being written and will appear here. '
                'Meanwhile, the official problems of Units 8 to 10 are solved on the <a href="../problemas/index.html">Problems</a> '
                'page and the test questions are on the <a href="midterm-3-test.html">test page</a>.</p>\n')
    lead = (f'      <p class="midterm-part-lead">{len(problems)} exam-style problems for Assessment Test III (5 points each). '
            'Part II of the real third partial is a composite-materials problem (unidirectional rule of mixtures, hybrid specific '
            'properties, or reinforcement selection). Ceramic crystal structure (Unit 8) and polymer molecular-weight/crystallinity '
            '(Unit 9) problems from the finals are also available for targeted practice in the '
            '<a href="../simulator/index.html?exam=midterm-3">Exam simulator</a>.</p>')
    order = list(ARCHETYPES)
    problems = sorted(problems, key=lambda p: (ARCH_UNIT[p["archetype"]], order.index(p["archetype"]), int(p["id"][1:])))
    out = [lead]
    for unit, title in ((10, "Composite materials (Part II standard · 5 points)"),
                        (8, "Ceramic crystal structures (Final exam practice · 5 points)"),
                        (9, "Polymer molecular weight & crystallinity (Final exam practice · 5 points)")):
        mine = [p for p in problems if ARCH_UNIT[p["archetype"]] == unit]
        if mine:
            out.append(f'      <h2 class="mcq-unit-title" id="unit-{unit}">{title} '
                       f'<span class="mcq-unit-count">{len(mine)} problems</span></h2>')
            out += [_problem_card(p) for p in mine]
    return "\n".join(out) + "\n"


def render_hub(blocks, problems):
    mt2_blocks = [b for b in blocks if b["unit"] in MT2_UNITS]
    mt3_blocks = [b for b in blocks if b["unit"] in MT3_UNITS]
    mt2_problems = [p for p in problems if p["unit"] in MT2_UNITS]
    mt3_problems = [p for p in problems if p["unit"] in MT3_UNITS]
    sections = []
    cards2 = []
    if mt2_blocks:
        n2 = sum(len(b["questions"]) for b in mt2_blocks)
        cards2.append(emb._hub_card(
            TEST_PAGE.name, "2nd Midterm • Test", f"Test Questions, Blocks {mt2_blocks[0]['id']} to {mt2_blocks[-1]['id']}",
            f"{n2} questions with four options in {len(mt2_blocks)} blocks of ten, each with its answer and the reason why "
            "every wrong option is wrong.", mt2_blocks,
            [f"{n2} Questions", "Blocks of 10", "Units 4 to 7", "Answers explained"]))
    if mt2_problems:
        cards2.append(emb._hub_card(
            PROBLEMS_PAGE.name, "2nd Midterm • Problems", f"Exam-Style Problems {mt2_problems[0]['id']} to {mt2_problems[-1]['id']}",
            f"{len(mt2_problems)} problems solved step by step: the long phase-diagram problem (3 points) and the short "
            "Unit 5 problem (2 points).", mt2_problems,
            [f"{len(mt2_problems)} Problems", "3 + 2 points", "Step-by-step solutions", "Results recomputed"]))
    sections.append("\n".join([
        '    <section class="exam-block" id="midterm-2" aria-labelledby="midterm-2-title">',
        '      <h2 class="exam-block-title" id="midterm-2-title">2nd Midterm</h2>',
        '      <p class="exam-block-lead">Assessment Test II covers Units 4 to 7: phase diagrams, mechanical, electrical, '
        'magnetic and thermal properties. It is a test of ten questions (5 points) and two problems: a longer one on phase diagrams (3 points) and a shorter one on mechanical properties (2 points). Practise '
        'the questions block by block, work through the problems, or take a timed exam in the '
        '<a href="../simulator/index.html">Exam simulator</a>.</p>',
        '      <div class="problem-sets-grid">', "\n\n".join(cards2), "      </div>", "    </section>"]))
    if mt3_blocks or mt3_problems:
        cards3 = []
        if mt3_blocks:
            n3 = sum(len(b["questions"]) for b in mt3_blocks)
            cards3.append(emb._hub_card(
                TEST_PAGE_MT3.name, "3rd Midterm • Test", f"Test Questions, Blocks {mt3_blocks[0]['id']} to {mt3_blocks[-1]['id']}",
                f"{n3} questions with four options in {len(mt3_blocks)} blocks of ten on ceramics, polymers, composites and adhesives.",
                mt3_blocks, [f"{n3} Questions", "Blocks of 10", "Units 8 to 11", "Answers explained"]))
        if mt3_problems:
            cards3.append(emb._hub_card(
                PROBLEMS_PAGE_MT3.name, "3rd Midterm • Problems", f"Exam-Style Problems {mt3_problems[0]['id']} to {mt3_problems[-1]['id']}",
                f"{len(mt3_problems)} problems solved step by step: composite materials (Part II standard, 5 points), ceramic structures and polymers.",
                mt3_problems, [f"{len(mt3_problems)} Problems", "5 points each", "Step-by-step solutions", "Results recomputed"]))
        sections.append("\n".join([
            '    <section class="exam-block" id="midterm-3" aria-labelledby="midterm-3-title">',
            '      <h2 class="exam-block-title" id="midterm-3-title">3rd Midterm</h2>',
            '      <p class="exam-block-lead">Assessment Test III covers Units 8 to 11: ceramic materials, polymers, composite materials '
            'and adhesives. It is a test of ten questions (5 points) and a composite-materials problem (5 points). Practise '
            'by block or take a custom or full timed exam in the <a href="../simulator/index.html?exam=midterm-3">Exam simulator</a>.</p>',
            '      <div class="problem-sets-grid">', "\n\n".join(cards3), "      </div>", "    </section>"]))
    return "\n\n".join(sections) + "\n"


# --------------------------------------------------------------------------- command line
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--lint", action="store_true")
    ap.add_argument("--allow-partial", action="store_true")
    args = ap.parse_args(argv)
    try:
        if args.lint:
            blocks, problems, review = load_bank(partial=args.allow_partial)
            mt2_b = [b for b in blocks if b["unit"] in MT2_UNITS]
            mt2_p = [p for p in problems if p["unit"] in MT2_UNITS]
            check_blueprint(json.loads((OUT_DIR / BLUEPRINT).read_text(encoding="utf-8")), mt2_b, mt2_p, args.allow_partial, BLUEPRINT)
            if (OUT_DIR / BLUEPRINT_MT3).is_file():
                mt3_b = [b for b in blocks if b["unit"] in MT3_UNITS]
                mt3_p = [p for p in problems if p["unit"] in MT3_UNITS]
                check_blueprint(json.loads((OUT_DIR / BLUEPRINT_MT3).read_text(encoding="utf-8")), mt3_b, mt3_p, args.allow_partial, BLUEPRINT_MT3)
            _report(blocks, problems, review)
            return 0
        outputs, data, review = build(partial=args.allow_partial)
        stale_figs = mt2fig.REG.stale(REPO)
    except bpb.BankError as exc:
        print(f"build_materials_bank: {exc}")
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
        for rel in (stale_figs if args.check else mt2fig.REG.write(REPO)):
            print("stale" if args.check else "wrote", rel)
    c = data["counts"]
    print(f"build_materials_bank: MT2 {c[TEST_CATEGORY]} Qs/{c[BLOCK_CATEGORY]} blocks/{c[PROBLEM_CATEGORY]} probs; "
          f"MT3 {c[MT3_TEST_CATEGORY]} Qs/{c[MT3_BLOCK_CATEGORY]} blocks/{c[MT3_PROBLEM_CATEGORY]} probs; "
          f"{len(review)} similar pairs to review")
    return 1 if (args.check and stale) else 0


def _report(blocks, problems, review):
    questions = [q for b in blocks for q in b["questions"]]
    print(f"build_materials_bank: {len(blocks)} blocks ({len(questions)} questions) and {len(problems)} problems valid")
    for unit in UNITS:
        qs = [q for q in questions if q["unit"] == unit]
        fm = {}
        for q in qs:
            fm[q["format"]] = fm.get(q["format"], 0) + 1
        print(f"  unit {unit}: {len(qs)} questions (quota {QUOTAS[unit]}), {len({q['concept_id'] for q in qs})} concepts; "
              + ", ".join(f"{k} {v}" for k, v in sorted(fm.items())))
    if questions:
        print("  right answers: " + ", ".join(f"{k} {sum(q['answer'] == k for q in questions)}" for k in LETTERS))
    for arch in ARCHETYPES:
        print(f"  problems {arch}: {sum(p['archetype'] == arch for p in problems)}")
    print(f"  similar pairs between {SIM_WARN} and {SIM_FAIL}: {len(review)}")
    for r, a, b in review:
        print(f"    {r:.2f} {a} ~ {b}")


if __name__ == "__main__":
    sys.exit(main())
