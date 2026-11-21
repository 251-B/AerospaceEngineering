"""The Aerospace Materials I Midterm 2 bank (tools/build_materials_bank.py): note format and checks, the anti-repetition
rules, the recomputation of numeric answers, the generated data and pages, and the multiple-choice mode of the Exam
Simulator (scoring +0.5 / -0.15 with floor 0, block practice), which runs in headless Edge/Chrome."""
import html
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "materials_bank"))
import build_materials_bank as bmb  # noqa: E402
import build_problem_bank as bpb  # noqa: E402
import verify_mt2  # noqa: E402
from test_focus_lab import BROWSER  # noqa: E402

REPO = bmb.REPO
HARNESS = pathlib.Path(__file__).resolve().parent / "mcq_simulator_harness.html"
WORDS = ("copper", "nickel", "ferrite", "austenite", "pearlite", "liquidus", "solidus", "eutectic", "dislocation", "vacancy",
         "modulus", "hardness", "ductility", "resilience", "toughness", "mobility", "donor", "acceptor", "coercivity",
         "remanence", "susceptibility", "expansion", "conduction", "valence", "cementite", "solvus", "peritectic",
         "monotectic", "necking", "yielding", "creep", "fatigue", "anneal", "quench", "temper", "martensite", "bainite",
         "phonon", "exciton", "domain")


def question(block, k, answer="a", concept=None, fmt="true-statement", asks="definition", stem=None, options=None,
             extra="", explain=None):
    """One valid question; every question gets its own vocabulary so that the similarity rule is not triggered."""
    w = [WORDS[(7 * k + 3 * j + 11 * int(block[1:])) % len(WORDS)] for j in range(8)]
    stem = stem or f"Which one of the following statements about {w[0]} and {w[1]} in case {block}-{k} is TRUE"
    options = options or {x: f"The {w[2 + i]} sets the {w[(5 + i) % 8]} of sample {k}{x}" for i, x in enumerate("abcd")}
    wrong = [x for x in "abcd" if x != answer]
    explain = explain or "\n".join(f"- {x}) This option swaps two neighbouring concepts of the slide." for x in wrong)
    return (f"## Q{block[1:]}.{k} Title {k}\n\n- id: {block}-Q{k}\n- concept_id: {concept or f'u5-demo-{block.lower()}-{k}'}\n"
            f"- format: {fmt}\n- asks: {asks}\n{extra}\n{stem}\n\n" + "\n".join(f"{x}) {options[x]}" for x in "abcd") +
            f"\n\n### Answer\n\n{answer}\n\n### Explanation\n\nHooke's law, $\\sigma = E\\varepsilon$, holds here.\n\n{explain}\n\n"
            "### Source\n\nSession 11, Slide 12.\n")


def block_note(block="B01", questions=None, unit=5):
    questions = questions or [question(block, k, "abcdabcdab"[k - 1]) for k in range(1, 11)]
    concepts = sorted(set(re.findall(r"- concept_id: (\S+)", "\n".join(questions))))
    return ("---\nmateria: Aerospace Materials I\nbank_id: " + block + '\ntitle: "Demo block"\ncategory: mt2_test_block\n'
            f"unit: {unit}\nconcepts:\n" + "".join(f"  - {c}\n" for c in concepts) +
            'difficulty: 2\ntags:\n  - problem-bank\norigen: "demo"\n---\n\n# Demo\n\n'
            "> [!info] Practice item, not an official exercise\n> Demo.\n\n" + "\n".join(questions))


PROBLEM = """---
materia: Aerospace Materials I
bank_id: P01
title: "Demo problem"
category: mt2_problem
archetype: tensile-test
level: standard
unit: 5
difficulty: 2
points: 2.0
time_minutes: 15
origen: "demo"
tags:
  - problem-bank
---

# Demo

> [!info] Practice item, not an official exercise
> Demo.

## Statement

A bar of 10 mm diameter carries 22 kN.

## (a) Stress [1.0 pts]

### Hint

Divide by the area.

### Checkpoint

- $\\sigma = 280.1$ MPa

### Solution

#### Compute the stress from its definition

$$\\sigma = F/A_0$$

## (b) Strain [1.0 pts]

### Hint

Hooke.

### Checkpoint

- $\\varepsilon = 0.0025$

### Solution

#### Apply Hooke's law

$$\\varepsilon = \\sigma/E$$

## Verification

- stress (MPa) | 22000/(pi*5**2) | 280.1
"""


class NoteCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def write(self, text, name="Quiz - Bank B01 - Unit 5 Demo.md"):
        path = self.dir / name
        path.write_text(text, encoding="utf-8")
        return path

    def parse(self, text, name="Quiz - Bank B01 - Unit 5 Demo.md"):
        return bmb.parse_quiz_note(self.write(text, name))

    def assertBankError(self, pattern, fn, *args):
        with self.assertRaisesRegex(bpb.BankError, pattern):
            fn(*args)


class QuizNoteTests(NoteCase):
    def test_valid_block_parses(self):
        block = self.parse(block_note())
        self.assertEqual(block["id"], "B01")
        self.assertEqual([q["id"] for q in block["questions"]], [f"B01-Q{k}" for k in range(1, 11)])
        q = block["questions"][0]
        self.assertEqual((q["kind"], q["points"], q["answer"]), ("multiple_choice", 0.5, "a"))
        self.assertEqual([o["label"] for o in q["options"]], list("abcd"))
        self.assertEqual(sorted(q["distractors"]), list("bcd"))
        self.assertIn("Session 11", q["source_html"])

    def test_block_needs_ten_questions(self):
        self.assertBankError("questions 1 to 10", self.parse, block_note(questions=[question("B01", k) for k in range(1, 10)]))

    def test_needs_four_options(self):
        bad = question("B01", 1).replace("\nd) ", "\nd] ")
        self.assertBankError("four options|text after the options", self.parse,
                             block_note(questions=[bad] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_options_must_differ(self):
        bad = question("B01", 1, options={"a": "Ferrite", "b": "Austenite", "c": "ferrite.", "d": "Pearlite"})
        self.assertBankError("two options are the same", self.parse,
                             block_note(questions=[bad] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_exactly_one_answer(self):
        bad = question("B01", 1).replace("### Answer\n\na\n", "### Answer\n\na, c\n")
        self.assertBankError("one letter", self.parse,
                             block_note(questions=[bad] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_every_wrong_option_is_explained(self):
        bad = question("B01", 1, explain="- b) This option swaps two neighbouring concepts.\n- c) This option inverts the trend of the slide.")
        self.assertBankError("one bullet", self.parse,
                             block_note(questions=[bad] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_explanation_must_name_the_mistake(self):
        bad = question("B01", 1, explain="- b) Wrong.\n- c) Wrong.\n- d) Wrong.")
        self.assertBankError("does not name the mistake", self.parse,
                             block_note(questions=[bad] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_source_is_required(self):
        bad = question("B01", 1).replace("### Source\n\nSession 11, Slide 12.\n", "")
        self.assertBankError("lacks its '### Source'", self.parse,
                             block_note(questions=[bad] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_same_letter_four_times_in_a_row(self):
        qs = [question("B01", k, "abbbbcdacd"[k - 1]) for k in range(1, 11)]
        self.assertBankError("four times in a row", self.parse, block_note(questions=qs))

    def test_concept_must_belong_to_the_unit(self):
        self.assertBankError("concept_id must look like u5-", self.parse,
                             block_note(questions=[question("B01", 1, concept="u4-lever-rule")] +
                                        [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_unbalanced_dollar_and_phase_labels_and_emojis(self):
        self.assertBankError("unbalanced \\$", self.parse, block_note().replace("holds here.", "holds $here.", 1))
        self.assertBankError("not allowed", self.parse, block_note().replace("# Demo", "# Demo\n\nPhase 1 of the solution"))
        self.assertBankError("emojis", self.parse, block_note().replace("# Demo", "# Demo \U0001F680"))

    def test_practice_label_is_required(self):
        self.assertBankError("Practice item", self.parse, block_note().replace("Practice item, not an official exercise", "Info"))


class NumericTests(NoteCase):
    OPTS = {"a": "160 GPa", "b": "190 GPa", "c": "220 GPa", "d": "250 GPa"}
    CALC = "- calc: 1122/(pi*(8e-3/2)**2)/((2.5e-7/8e-3)/0.35)/1e9\n"   # question 8 of the real paper: 250 GPa
    EXPLAIN = ("- a) Poisson's ratio applied twice gives a lower value than the right one.\n"
               "- b) The diameter is used as the radius in the area, a different number.\n"
               "- c) The lateral strain is used as the axial strain without Poisson's ratio.")

    def block(self, **kw):
        q = question("B01", 1, answer=kw.get("answer", "d"), fmt="numeric", asks="calculation",
                     options=kw.get("options", self.OPTS), extra=kw.get("extra", self.CALC),
                     explain=kw.get("explain", self.EXPLAIN))
        return block_note(questions=[q] + [question("B01", k, "abcabcdab"[k - 2]) for k in range(2, 11)])

    def test_real_question_8_recomputes_to_250_gpa(self):
        q = self.parse(self.block())["questions"][0]
        self.assertAlmostEqual(bmb.evaluate(q["calc"], "t"), 250.0, delta=0.5)

    def test_numeric_needs_calc(self):
        self.assertBankError("needs '- calc", self.parse, self.block(extra=""))

    def test_answer_must_match_calc(self):
        explain = self.EXPLAIN.replace("- a)", "- d)")
        self.assertBankError("calc gives 250", self.parse, self.block(answer="a", explain=explain))

    def test_wrong_option_must_not_coincide_with_the_right_value(self):
        opts = dict(self.OPTS, c="248 GPa")
        self.assertBankError("coincides with the right value", self.parse, self.block(options=opts))

    def test_options_share_the_unit(self):
        opts = dict(self.OPTS, a="160 MPa")
        self.assertBankError("same unit", self.parse, self.block(options=opts))

    def test_check_condition_must_hold(self):
        ok = question("B01", 1, fmt="what-happens", asks="effect", extra="- check: 250 < 6000/(pi*2.5**2) < 310\n")
        self.parse(block_note(questions=[ok] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))
        bad = ok.replace("6000", "6400")
        self.assertBankError("is not true", self.parse,
                             block_note(questions=[bad] + [question("B01", k, "bcdabcdab"[k - 2]) for k in range(2, 11)]))

    def test_leading_number_reads_scientific_notation(self):
        self.assertEqual(bmb.leading_number("$2.5\\times10^{-4}$ mm"), (2.5e-4, "mm"))
        self.assertEqual(bmb.leading_number("68.2 %"), (68.2, "%"))
        self.assertAlmostEqual(bmb.leading_number("1.6e-19 C")[0], 1.6e-19)
        self.assertIsNone(bmb.leading_number("Pearlite"))


class BankRuleTests(NoteCase):
    def blocks(self, *texts):
        return [self.parse(t, f"Quiz - Bank B{n:02d} - Unit 5 Demo.md") for n, t in enumerate(texts, 1)]

    def test_at_most_four_questions_per_concept(self):
        pairs = [("true-statement", "definition"), ("false-statement", "cause"), ("numeric", "effect"),
                 ("identify", "comparison"), ("ordering", "classification")]
        qs = []
        for k in range(1, 11):
            if k <= 5:
                fmt, asks = pairs[k - 1]
                extra = "- calc: 5\n" if fmt == "numeric" else ""
                opts = {"a": "1 MPa", "b": "3 MPa", "c": "5 MPa", "d": "7 MPa"} if fmt == "numeric" else None
                ans = "c" if fmt == "numeric" else "abcdabcdab"[k - 1]
                qs.append(question("B01", k, ans, concept="u5-same", fmt=fmt, asks=asks, extra=extra, options=opts))
            else:
                qs.append(question("B01", k, "abcdabcdab"[k - 1]))
        with self.assertRaisesRegex(bpb.BankError, "maximum 4"):
            bmb.check_bank(self.blocks(block_note(questions=qs)), [], partial=True)

    def test_same_concept_must_differ_in_format_or_question_type(self):
        qs = [question("B01", k, "abcdabcdab"[k - 1], concept="u5-same" if k <= 2 else None) for k in range(1, 11)]
        with self.assertRaisesRegex(bpb.BankError, "share format and question type"):
            bmb.check_bank(self.blocks(block_note(questions=qs)), [], partial=True)

    def test_near_duplicate_questions_fail(self):
        stem = "With an increase in temperature the electrical conductivity of a pure metal such as copper:"
        opts = {"a": "Decreases because the electrons are scattered more", "b": "Increases because there are more electrons",
                "c": "Increases because there are more imperfections", "d": "Decreases because the atoms vibrate less"}
        q1 = question("B01", 1, "a", stem=stem, options=opts)
        q2 = question("B01", 2, "a", stem=stem.replace("copper", "silver"), options=opts)
        qs = [q1, q2] + [question("B01", k, "cdbcdbcd"[k - 3]) for k in range(3, 11)]
        with self.assertRaisesRegex(bpb.BankError, "too similar"):
            bmb.check_bank(self.blocks(block_note(questions=qs)), [], partial=True)

    def test_similar_pairs_below_the_limit_are_reported_not_failed(self):
        blocks = self.blocks(block_note())
        self.assertEqual(bmb.check_bank(blocks, [], partial=True), [])
        self.assertTrue(all(bmb.SIM_WARN <= r < bmb.SIM_FAIL for r, _a, _b in bmb.similarity_report(
            [q for b in blocks for q in b["questions"]])))

    def test_quota_is_enforced_unless_partial(self):
        blocks = self.blocks(block_note())
        with self.assertRaisesRegex(bpb.BankError, "quota"):
            bmb.check_bank(blocks, [], partial=False)

    def test_blueprint_must_add_up_and_carry_the_scoring_rule(self):
        bp = json.loads((bmb.OUT_DIR / bmb.BLUEPRINT).read_text(encoding="utf-8"))
        bmb.check_blueprint(bp, [], [], partial=True)
        broken = json.loads(json.dumps(bp))
        del broken["parts"][0]["points_wrong"]
        with self.assertRaisesRegex(bpb.BankError, "points_wrong"):
            bmb.check_blueprint(broken, [], [], partial=True)
        broken = json.loads(json.dumps(bp))
        broken["parts"][0]["selection_rules"]["per_unit"]["5"] = 5
        with self.assertRaisesRegex(bpb.BankError, "per_unit adds up"):
            bmb.check_blueprint(broken, [], [], partial=True)


class ModeTests(unittest.TestCase):
    """Practice scopes of the blueprint (read by assets/js/exam-simulator.js)."""

    def bp(self):
        return json.loads((bmb.OUT_DIR / bmb.BLUEPRINT).read_text(encoding="utf-8"))

    def test_real_blueprint_modes_are_valid(self):
        bp = self.bp()
        bmb.check_blueprint(bp, [], [], partial=True)
        ids = [m["id"] for m in bp["modes"]]
        self.assertEqual(ids, ["real-paper", "focus-6-7", "unit-4", "unit-5", "unit-6", "unit-7"])
        self.assertEqual(bp["modes"][0]["per_unit"], bp["parts"][0]["selection_rules"]["per_unit"])
        self.assertGreater(bp["modes"][1]["per_unit"]["6"] + bp["modes"][1]["per_unit"]["7"], 5)

    def test_a_mode_must_add_up_to_the_part_count(self):
        bp = self.bp()
        bp["modes"][1]["per_unit"]["6"] = 5
        with self.assertRaisesRegex(bpb.BankError, "per_unit adds up"):
            bmb.check_blueprint(bp, [], [], partial=True)

    def test_exactly_one_default_and_unique_ids(self):
        bp = self.bp()
        bp["modes"][1]["default"] = True
        with self.assertRaisesRegex(bpb.BankError, "default"):
            bmb.check_blueprint(bp, [], [], partial=True)
        bp = self.bp()
        bp["modes"][2]["id"] = "real-paper"
        with self.assertRaisesRegex(bpb.BankError, "unique"):
            bmb.check_blueprint(bp, [], [], partial=True)

    def test_unknown_unit_and_bad_duration_are_rejected(self):
        bp = self.bp()
        bp["modes"][2]["per_unit"] = {"9": 10}
        with self.assertRaisesRegex(bpb.BankError, "per_unit must map"):
            bmb.check_blueprint(bp, [], [], partial=True)
        bp = self.bp()
        bp["modes"][2]["duration_minutes"] = 25
        with self.assertRaisesRegex(bpb.BankError, "duration_minutes"):
            bmb.check_blueprint(bp, [], [], partial=True)

    def test_bank_needs_enough_blocks_and_questions_for_a_unit_mode(self):
        bp = self.bp()
        blocks = [{"unit": 4, "questions": [0] * 10} for _ in range(3)]
        with self.assertRaisesRegex(bpb.BankError, "needs at least"):
            bmb.check_blueprint(bp, blocks, [], partial=False)

    def test_business_management_blueprint_has_no_modes(self):
        path = bmb.REPO / "subjects" / "business-management" / "data" / "exam-blueprint.json"
        self.assertNotIn("modes", json.loads(path.read_text(encoding="utf-8")))


class ProblemNoteTests(NoteCase):
    NAME = "Problem - Bank P01 - Demo.md"

    def test_valid_problem_and_its_verification(self):
        path = self.write(PROBLEM, self.NAME)
        item = bmb.parse_problem_note(path)
        self.assertEqual((item["points"], len(item["subquestions"]), len(item["verify"])), (2.0, 2, 1))
        self.assertEqual(verify_mt2.verify_problem(item, path), [])

    def test_points_must_add_up(self):
        self.assertBankError("add up to 1.5", bmb.parse_problem_note, self.write(PROBLEM.replace("[1.0 pts]", "[0.5 pts]", 1), self.NAME))

    def test_solution_needs_step_titles(self):
        self.assertBankError("step titles", bmb.parse_problem_note,
                             self.write(PROBLEM.replace("#### Apply Hooke's law\n", ""), self.NAME))

    def test_wrong_stated_value_is_caught(self):
        path = self.write(PROBLEM.replace("| 280.1\n", "| 290.1\n").replace("280.1$ MPa", "290.1$ MPa"), self.NAME)
        errors = verify_mt2.verify_problem(bmb.parse_problem_note(path), path)
        self.assertTrue(errors and "the note states 290.1" in errors[0], errors)

    def test_stated_value_must_be_printed_in_the_note(self):
        path = self.write(PROBLEM.replace("280.1$ MPa", "280$ MPa"), self.NAME)
        errors = verify_mt2.verify_problem(bmb.parse_problem_note(path), path)
        self.assertTrue(errors and "not printed" in errors[0], errors)


class RealBankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs, cls.data, cls.review = bmb.build()
        cls.questions = [i for i in cls.data["items"] if i.get("kind") == "multiple_choice"]
        cls.problems = [i for i in cls.data["items"] if i["category"] == bmb.PROBLEM_CATEGORY]

    def test_generated_files_are_up_to_date(self):
        for path, content in self.outputs.items():
            self.assertEqual(path.read_bytes().decode("utf-8").replace("\r\n", "\n"), content, path.name)
        self.assertEqual(bmb.mt2fig.REG.stale(REPO), [])

    def test_bank_size_and_quotas(self):
        self.assertGreaterEqual(len(self.questions), 520)
        self.assertGreaterEqual(len(self.data["blocks"]), 52)
        self.assertTrue(all(len(b["items"]) == 10 for b in self.data["blocks"]))
        for unit, minimum in bmb.QUOTAS.items():
            self.assertGreaterEqual(sum(q["unit"] == unit for q in self.questions), minimum, unit)
            self.assertGreaterEqual(minimum, 60)
        self.assertGreaterEqual(len(self.problems), 20)
        for arch in bmb.ARCHETYPES:
            self.assertGreaterEqual(sum(p["archetype"] == arch for p in self.problems), 4, arch)

    def test_concepts_and_right_letters(self):
        counts = {}
        for q in self.questions:
            counts[q["concept_id"]] = counts.get(q["concept_id"], 0) + 1
        self.assertLessEqual(max(counts.values()), bmb.MAX_PER_CONCEPT)
        for k in "abcd":
            share = sum(q["answer"] == k for q in self.questions) / len(self.questions)
            self.assertTrue(0.20 <= share <= 0.30, (k, share))

    def test_no_pair_of_questions_is_too_similar(self):
        self.assertTrue(all(r < bmb.SIM_FAIL for r, _a, _b in self.review))

    def test_every_number_is_recomputed(self):
        self.assertEqual(verify_mt2.main([]), 0)
        self.assertTrue(all(q["calc"] for q in self.questions if q["format"] == "numeric"))
        self.assertTrue(all(p["verify"] for p in self.problems))

    def test_pages_carry_the_bank(self):
        test_page = bmb.TEST_PAGE.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r'class="problem-box"', test_page)), len(self.data["blocks"]))
        self.assertEqual(len(re.findall(r'class="phase-block mcq-item"', test_page)), len(self.questions))
        self.assertEqual(len(re.findall(r'<details class="mcq-answer">', test_page)), len(self.questions))
        self.assertNotIn("<details class=\"mcq-answer\" open", test_page)
        self.assertIn("Practice item, not an official exercise", test_page)
        problems_page = bmb.PROBLEMS_PAGE.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r'class="problem-box"', problems_page)), len(self.problems))
        for page in (test_page, problems_page):
            self.assertIsNone(re.search(r">\s*Phase \d", page))
            self.assertIn("ask-ai.js", page)
            self.assertIn("pdf-export.js", page)
            self.assertIn('href="../../../index.html"', page)
        hub = bmb.HUB.read_text(encoding="utf-8")
        self.assertIn('href="midterm-2-test.html"', hub)
        self.assertIn('href="midterm-2-problems.html"', hub)

    def test_blueprint_is_the_real_structure(self):
        bp = json.loads((bmb.OUT_DIR / bmb.BLUEPRINT).read_text(encoding="utf-8"))
        mc, long_problem, short_problem = bp["parts"]
        self.assertEqual((mc["type"], mc["count"], mc["points_correct"], mc["points_wrong"], mc["points_blank"], mc["floor"]),
                         ("multiple_choice", 10, 0.5, -0.15, 0, 0))
        self.assertEqual((long_problem["count"], long_problem["points_each"], long_problem["selection_rules"]["units"]), (1, 3.0, [4]))
        self.assertEqual((short_problem["count"], short_problem["points_each"], short_problem["selection_rules"]["units"]), (1, 2.0, [5]))
        self.assertEqual(bp["total_points"], 10.0)
        self.assertIn("MATERIALS_SECONDPARTIAL_2019.pdf", bp["provenance"]["structure_source"])

    def test_simulator_page_reads_the_bank_and_the_blueprint(self):
        page = (REPO / "subjects/aerospace-materials-1/simulator/index.html").read_text(encoding="utf-8")
        for needle in ('data-bank="AE_MAT_BANK"', 'data-blueprint-midterm-2="AE_MAT_BLUEPRINT_MT2"',
                       'data-default-exam="midterm-2"', 'data-storage="ae_mat_exams"', "../data/problems.js",
                       'aria-current="page">Exam simulator</a>'):
            self.assertIn(needle, page)
        self.assertNotIn("<canvas", page)
        self.assertIsNone(re.search(r"points_wrong|0\.15", page), "the structure must come from the blueprint")

    def test_simulator_script_reads_the_scoring_from_the_blueprint(self):
        js = (REPO / "assets/js/exam-simulator.js").read_text(encoding="utf-8")
        for needle in ("part.points_correct", "part.points_wrong", "part.points_blank", "part.floor", "'multiple_choice'"):
            self.assertIn(needle, js)
        self.assertIsNone(re.search(r"0\.15|ae_mat", js), "no subject or scoring constant in the shared script")

    def test_tab_strips_of_the_subject(self):
        for area in ("teoria", "problemas", "extra-problems", "simulator"):
            page = (REPO / f"subjects/aerospace-materials-1/{area}/index.html").read_text(encoding="utf-8")
            self.assertIn('href="../extra-problems/index.html"', page, area)
            self.assertIn('href="../simulator/index.html"', page, area)
            self.assertNotIn("subject-tab__soon", page, area)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class MultipleChoiceSimulatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=40000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 41, [r["name"] for r in self.results])

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail'][:300]}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
