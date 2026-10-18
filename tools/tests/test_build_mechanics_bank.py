"""Tests for tools/build_mechanics_bank.py (Engineering Mechanics Midterm 1 bank from vault notes)."""
import json
import pathlib
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_mechanics_bank as bmb  # noqa: E402

PROBLEM = """---
materia: Engineering Mechanics
bank_id: P99
title: "Demo pendulum"
category: midterm_problem
archetype: relative-motion
level: standard
unit: 5
difficulty: 2
points: 10.0
time_minutes: 60
origen: "test"
tags:
  - problem-bank
  - demo
---

# Demo

## Statement

A pendulum on a moving support.

![[attachments/EM-M1/p05-flight-pendulum.svg]]

## (a) Degrees of freedom [4.0 pts]

### Hint

Count the constraints.

### Checkpoint

- One degree of freedom.

### Solution

#### Step 1. Count

$$n = 2 - 1 = 1$$

## (b) Equation of motion [6.0 pts]

### Hint

Project on the tangent.

### Checkpoint

- $\\ell\\ddot\\theta=-g\\sin\\theta$

### Solution

Newton.
"""

CONCEPT = """---
materia: Engineering Mechanics
bank_id: C99
title: "Demo question"
category: conceptual_question
archetype: dynamics
level: conceptual
unit: 2
difficulty: 1
points: 2.0
time_minutes: 15
origen: "test"
tags:
  - problem-bank
---

## Statement

Judge each claim.

## (a) The energy of a particle is conserved [1.0 pts]

### Hint

Who does work?

### Checkpoint

- False.

### Solution

False.

## (b) The system energy is conserved [1.0 pts]

### Hint

Internal forces.

### Checkpoint

- True.

### Solution

True.
"""


class BankTests(unittest.TestCase):
    def build(self, files):
        with tempfile.TemporaryDirectory() as tmp:
            for name, text in files.items():
                (pathlib.Path(tmp) / name).write_text(text, encoding="utf-8")
            out = bmb.build(tmp)
        return json.loads(out[bmb.OUT_DIR / "problems.json"])

    def test_valid_notes_become_items_with_their_figure(self):
        data = self.build({"Problem - Bank P99 - Demo.md": PROBLEM, "Problem - Bank C99 - Demo.md": CONCEPT})
        self.assertEqual([i["id"] for i in data["items"]], ["C99", "P99"])
        p = data["items"][1]
        self.assertEqual([s["points"] for s in p["subquestions"]], [4.0, 6.0])
        self.assertEqual(p["figures"], ["p05-flight-pendulum"])
        self.assertIn('<div class="diagram-card">', p["statement_html"])
        self.assertIn('<h4 class="step-title">Step 1. Count</h4>', p["subquestions"][0]["solution_html"])
        self.assertEqual(p["tags"], ["demo"])

    def test_points_must_add_up(self):
        with self.assertRaisesRegex(bmb.bpb.BankError, "add up"):
            self.build({"Problem - Bank P99 - Demo.md": PROBLEM.replace("[6.0 pts]", "[5.0 pts]")})

    def test_category_fixes_the_points(self):
        with self.assertRaisesRegex(bmb.bpb.BankError, "worth"):
            self.build({"Problem - Bank C99 - Demo.md": CONCEPT.replace("points: 2.0", "points: 4.0")})

    def test_unknown_figure_is_refused(self):
        with self.assertRaisesRegex(bmb.bpb.BankError, "unknown figure"):
            self.build({"Problem - Bank P99 - Demo.md": PROBLEM.replace("p05-flight-pendulum", "no-such-figure")})

    def test_unknown_archetype_and_level_are_refused(self):
        with self.assertRaisesRegex(bmb.bpb.BankError, "archetype"):
            self.build({"Problem - Bank P99 - Demo.md": PROBLEM.replace("relative-motion", "optics")})
        with self.assertRaisesRegex(bmb.bpb.BankError, "level"):
            self.build({"Problem - Bank P99 - Demo.md": PROBLEM.replace("level: standard", "level: easy")})

    def test_missing_checkpoint_is_refused(self):
        with self.assertRaisesRegex(bmb.bpb.BankError, "checkpoint"):
            self.build({"Problem - Bank C99 - Demo.md": CONCEPT.replace("### Checkpoint\n\n- False.\n\n", "")})

    def test_index_note_must_list_every_item(self):
        with self.assertRaisesRegex(bmb.bpb.BankError, "does not list"):
            self.build({"Problem - Bank C99 - Demo.md": CONCEPT, f"{bmb.INDEX_NOTE}.md": "empty"})


class RepositoryTests(unittest.TestCase):
    def test_bank_is_up_to_date(self):
        self.assertEqual(bmb.main(["--check"]), 0)

    def test_hub_links_the_two_midterm_pages(self):
        hub = bmb.HUB.read_text(encoding="utf-8")
        block = hub[hub.index("EXTRA-HUB:START"):hub.index("EXTRA-HUB:END")]
        self.assertLess(block.index('href="midterm-1-theory.html"'), block.index('href="midterm-1-problems.html"'))
        self.assertNotIn('class="problem-box"', hub)
        self.assertIn('aria-current="page">Extra problems</a>', hub)
        self.assertNotIn("usiness", hub)

    def test_pages_hold_the_solved_items_with_pdf_buttons(self):
        data = json.loads((bmb.OUT_DIR / "problems.json").read_text(encoding="utf-8"))
        for page, cat in ((bmb.THEORY_PAGE, "conceptual_question"), (bmb.PROBLEMS_PAGE, "midterm_problem")):
            text = page.read_text(encoding="utf-8")
            block = text[text.index("EXTRA-PROBLEMS:START"):text.index("EXTRA-PROBLEMS:END")]
            ids = [i["id"] for i in data["items"] if i["category"] == cat]
            self.assertEqual(block.count('class="problem-box"'), len(ids))
            for i in ids:
                self.assertIn(f'id="{i}"', block)
            self.assertIn("assets/js/pdf-export.js", text)
            self.assertIn("assets/js/ask-ai.js", text)
            self.assertNotIn("usiness", text)
            self.assertNotIn("m.u.", block)

    def test_problems_js_carries_the_checked_blueprint(self):
        js = (bmb.OUT_DIR / "problems.js").read_text(encoding="utf-8")
        self.assertIn("window.AE_EM_BANK = ", js)
        self.assertIn("window.AE_EM_BLUEPRINT = ", js)
        items = json.loads((bmb.OUT_DIR / "problems.json").read_text(encoding="utf-8"))["items"]
        blueprint = json.loads((bmb.OUT_DIR / "exam-blueprint.json").read_text(encoding="utf-8"))
        with self.assertRaisesRegex(bmb.bpb.BankError, "add up"):
            bmb.check_blueprint(dict(blueprint, total_points=12.0), items)

    def test_simulator_page_reads_the_bank_and_the_blueprint(self):
        page = (bmb.REPO / "subjects/engineering-mechanics/simulator/index.html").read_text(encoding="utf-8")
        self.assertIn('data-bank="AE_EM_BANK"', page)
        self.assertIn('data-blueprint="AE_EM_BLUEPRINT"', page)
        self.assertIn('data-storage="ae_em_exams"', page)
        self.assertIn("../data/problems.js", page)
        self.assertIn('aria-current="page">Exam simulator</a>', page)
        self.assertNotIn("usiness", page)
        self.assertNotIn("ae_bm", page)

    def test_bank_matches_the_blueprint_and_covers_every_archetype(self):
        data = json.loads((bmb.OUT_DIR / "problems.json").read_text(encoding="utf-8"))
        blueprint = json.loads((bmb.OUT_DIR / "exam-blueprint.json").read_text(encoding="utf-8"))
        for part in blueprint["parts"]:
            items = [i for i in data["items"] if i["category"] == part["category"]]
            self.assertTrue(all(i["points"] == part["points_each"] for i in items))
            self.assertGreaterEqual(len(items), 15)
        problems = [i for i in data["items"] if i["category"] == "midterm_problem"]
        self.assertTrue(all(not i["official"] for i in data["items"]), "the bank holds only items written for it")
        for arch in bmb.ARCHETYPES:
            self.assertGreaterEqual(sum(i["archetype"] == arch for i in problems), 1, arch)
        for level in ("standard", "trap"):
            self.assertGreaterEqual(sum(i["level"] == level for i in problems), 3, level)
        self.assertTrue(all(len(i["figures"]) >= 1 for i in problems), "every problem has its technical sketch")

    def test_no_emojis_in_the_bank(self):
        import re
        text = (bmb.OUT_DIR / "problems.json").read_text(encoding="utf-8")
        self.assertIsNone(re.search("[\U0001F300-\U0001FAFF☀-➿]", text))


if __name__ == "__main__":
    unittest.main()
