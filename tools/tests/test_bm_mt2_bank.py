"""Tests of the Business Management Midterm 2 bank (tools/bm_mt2/bank.py) and of its simulator scopes."""
import html
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_problem_bank as bpb  # noqa: E402
from bm_mt2 import bank  # noqa: E402
from test_focus_lab import BROWSER  # noqa: E402

HARNESS = pathlib.Path(__file__).resolve().parent / "bm_mt2_simulator_harness.html"
HEAD = """---
materia: Business Management
tema: "Unit 4: test block"
bank_id: F09
title: "Test block"
category: mt2_tf_block
unit: 4
concepts:
{concepts}
difficulty: 1
origen: "Test"
tags:
  - problem-bank
---

# Bank F09 — Test block

> [!info] Practice item, not an official exercise
> Test.
"""


def statement(k, answer, concept=None, text=None):
    return (f"\n## F09.{k} Statement {k}\n\n- id: F09-S{k}\n- concept_id: {concept or f'u4-concept-{k}'}\n\n"
            f"{text or f'Statement number {k} about the break-even point of firm number {k * 7}.'}\n\n"
            f"### Answer\n\n{answer}\n\n### Reasoning\n\nBecause the course defines the idea of statement {k} in this precise way.\n\n"
            f"### Source\n\nTopic 4, Slide {k}.\n")


def tf_note(answers="TFTFTFTFTF", concepts=None):
    concepts = concepts or [f"u4-concept-{k}" for k in range(1, 11)]
    body = "".join(statement(k, a, concepts[k - 1]) for k, a in enumerate(answers, 1))
    head = HEAD.format(concepts="\n".join(f"  - {c}" for c in sorted(set(concepts))))
    return head + body


class TrueFalseNoteTests(unittest.TestCase):
    def parse(self, text, name="Quiz - Bank F09 - Unit 4 Test.md"):
        with tempfile.TemporaryDirectory() as tmp:
            p = pathlib.Path(tmp) / name
            p.write_text(text, encoding="utf-8")
            return bank.parse_quiz_note(p)

    def test_valid_block(self):
        b = self.parse(tf_note())
        self.assertEqual(b["kind"], "true_false")
        self.assertEqual([q["answer"] for q in b["questions"]], list("TFTFTFTFTF"))
        q = b["questions"][0]
        self.assertEqual((q["id"], q["category"], q["points"]), ("F09-S1", "mt2_true_false", 0.15))
        self.assertEqual([o["label"] for o in q["options"]], ["T", "F"])

    def test_answer_must_be_t_or_f(self):
        with self.assertRaisesRegex(bpb.BankError, "must be T or F"):
            self.parse(tf_note("TFTFTFTFTX"))

    def test_four_to_six_true(self):
        with self.assertRaisesRegex(bpb.BankError, "4 to 6 true"):
            self.parse(tf_note("TTFTTFTTFT"))

    def test_never_four_in_a_row(self):
        with self.assertRaisesRegex(bpb.BankError, "four times in a row"):
            self.parse(tf_note("TFFFFTTTFT"))

    def test_concept_must_belong_to_the_unit(self):
        with self.assertRaisesRegex(bpb.BankError, "concept_id must look like u4"):
            self.parse(tf_note(concepts=["u5-x"] + [f"u4-c-{k}" for k in range(2, 11)]))

    def test_unit_in_file_name(self):
        with self.assertRaisesRegex(bpb.BankError, "must carry 'Unit 4'"):
            self.parse(tf_note(), "Quiz - Bank F09 - Unit 5 Test.md")

    def test_concept_limit(self):
        b = self.parse(tf_note(concepts=["u4-same"] * 4 + [f"u4-c-{k}" for k in range(5, 11)]))
        with self.assertRaisesRegex(bpb.BankError, "maximum 3"):
            bank.check_bank([b], [], partial=True)

    def test_near_duplicates_fail(self):
        text = "A firm whose costs are mostly variable has a higher economic risk because its profit varies more."
        note = tf_note()
        note = note.replace("Statement number 1 about the break-even point of firm number 7.", text)
        note = note.replace("Statement number 2 about the break-even point of firm number 14.", text.replace("A firm", "One firm"))
        with self.assertRaisesRegex(bpb.BankError, "too similar"):
            bank.check_bank([self.parse(note)], [], partial=True)


class RealBankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = bpb.build()
        cls.data = json.loads(cls.out[bpb.OUT_DIR / "problems.json"])
        cls.bp = json.loads((bpb.OUT_DIR / "exam-blueprint-midterm-2.json").read_text(encoding="utf-8"))

    def test_both_midterms_in_one_bank(self):
        cats = {i["category"] for i in self.data["items"]}
        for c in ("short_theory_case", "extra_practice_problem", "mt2_true_false", "mt2_test_question", "mt2_problem"):
            self.assertIn(c, cats)
        js = self.out[bpb.OUT_DIR / "problems.js"]
        for name in ("window.AE_BM_BANK", "window.AE_BM_BLUEPRINT ", "window.AE_BM_BLUEPRINT_MT2"):
            self.assertIn(name, js)

    def test_blueprint_adds_up_to_ten(self):
        self.assertEqual(round(sum(p["count"] * p["points_each"] for p in self.bp["parts"]), 4), 10.0)
        tf = next(p for p in self.bp["parts"] if p["type"] == "true_false")
        self.assertEqual((tf["count"], tf["points_correct"], tf["points_wrong"], tf["points_total"]), (20, 0.15, -0.15, 3.0))

    def test_every_unit_has_both_kinds(self):
        for unit in bank.UNITS:
            for kind in ("true_false", "multiple_choice"):
                self.assertTrue(any(i.get("kind") == kind and i["unit"] == unit for i in self.data["items"]), (unit, kind))

    def test_every_archetype_has_a_problem(self):
        have = {i["archetype"] for i in self.data["items"] if i["category"] == "mt2_problem"}
        self.assertEqual(have, set(bank.ARCHETYPES))

    def test_numeric_problems_recompute(self):
        for item in self.data["items"]:
            if item["category"] == "mt2_problem" and item["verify"]:
                self.assertTrue(bank.verify_problem(item), item["id"])

    def test_true_share_is_balanced(self):
        tf = [i for i in self.data["items"] if i.get("kind") == "true_false"]
        share = sum(i["answer"] == "T" for i in tf) / len(tf)
        self.assertTrue(0.45 <= share <= 0.55, share)

    def test_pages_and_storage(self):
        for page in ("midterm-2-tf.html", "midterm-2-test.html", "midterm-2-problems.html"):
            text = (REPO / "subjects/business-management/extra-problems" / page).read_text(encoding="utf-8")
            self.assertIn("Practice item, not an official exercise", text)
            self.assertNotIn("<canvas", text)
            self.assertIsNone(re.search(r"\bPhase \d", text))
        js = (REPO / "assets/js/exam-simulator.js").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"localStorage\.setItem\([^)]*theme", js))
        self.assertIn("'true_false'", js)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class Midterm2SimulatorTests(unittest.TestCase):
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
        self.assertEqual(len(self.results), 31, [r["name"] for r in self.results])

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail'][:300]}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
