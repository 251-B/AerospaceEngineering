"""Tests for tools/build_problem_bank.py (Business Management problem bank from vault notes)."""
import json
import pathlib
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_problem_bank as bpb  # noqa: E402

PROBLEM = """---
materia: Business Management
bank_id: P99
title: "Demo"
category: extra_practice_problem
archetype: unordered-items
unit: 3
difficulty: 2
points: 4.0
time_minutes: 30
origen: "test"
tags:
  - problem-bank
  - demo
---

# Demo

> [!info] Practice item
> Not official.

## Statement

A list of balances.

## (a) Prepare the income statement [1.5 pts]

### Hint

Gross profit first.

### Checkpoint

- Net income 10 m.u.

### Solution

#### Step 1. Income statement

$$NI = 10$$

## (b) Prepare the balance sheet [2.5 pts]

### Hint

Assets = liabilities + equity.

### Checkpoint

- Total 100 m.u.

### Solution

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| **Total assets** | **100** | **Total liabilities and equity** | **{total}** |

---

**Back to:** [[Business Management MOC]]
"""

CASE = """---
materia: Business Management
bank_id: C99
title: "Demo case"
category: short_theory_case
theme: demo-theme
unit: 1
difficulty: 1
points: 2.0
time_minutes: 15
origen: "test"
tags:
  - problem-bank
---

# Demo case

## Statement

A short case.

## (a) Explain [2.0 pts]

### Hint

Think.

### Checkpoint

- Concept A

### Solution

Answer.
"""


class BankTests(unittest.TestCase):
    def build(self, files):
        with tempfile.TemporaryDirectory() as tmp:
            for name, text in files.items():
                (pathlib.Path(tmp) / name).write_text(text, encoding="utf-8")
            out = bpb.build(tmp)
        return json.loads(out[bpb.OUT_DIR / "problems.json"])

    def test_valid_notes_become_items(self):
        data = self.build({"Problem - Bank P99 - Demo.md": PROBLEM.replace("{total}", "100"),
                           "Problem - Bank C99 - Demo case.md": CASE})
        self.assertEqual([i["id"] for i in data["items"]], ["C99", "P99"])
        p = data["items"][1]
        self.assertEqual([s["points"] for s in p["subquestions"]], [1.5, 2.5])
        self.assertIn('<h4 class="step-title">Step 1. Income statement</h4>', p["subquestions"][0]["solution_html"])
        self.assertEqual(p["tags"], ["demo"])
        self.assertEqual(data["items"][0]["theme"], "demo-theme")

    def test_unbalanced_balance_sheet_is_refused(self):
        with self.assertRaisesRegex(bpb.BankError, "does not balance"):
            self.build({"Problem - Bank P99 - Demo.md": PROBLEM.replace("{total}", "90")})

    def test_points_must_add_up(self):
        with self.assertRaisesRegex(bpb.BankError, "add up"):
            self.build({"Problem - Bank P99 - Demo.md": PROBLEM.replace("{total}", "100").replace("[2.5 pts]", "[2.0 pts]")})

    def test_european_number_format_is_checked(self):
        eu = PROBLEM.replace("origen: \"test\"", "origen: \"test\"\nnumber_format: eu").replace("**100**", "**1.500,50**")
        self.build({"Problem - Bank P99 - Demo.md": eu.replace("{total}", "1.500,50")})
        with self.assertRaisesRegex(bpb.BankError, "does not balance"):
            self.build({"Problem - Bank P99 - Demo.md": eu.replace("{total}", "1.500,05")})

    def test_case_needs_a_theme(self):
        with self.assertRaisesRegex(bpb.BankError, "theme"):
            self.build({"Problem - Bank C99 - Demo case.md": CASE.replace("theme: demo-theme\n", "")})

    def test_missing_checkpoint_is_refused(self):
        broken = CASE.replace("### Checkpoint\n\n- Concept A\n\n", "")
        with self.assertRaisesRegex(bpb.BankError, "checkpoint"):
            self.build({"Problem - Bank C99 - Demo case.md": broken})

    def test_index_note_must_list_every_item(self):
        with self.assertRaisesRegex(bpb.BankError, "does not list"):
            self.build({"Problem - Bank C99 - Demo case.md": CASE, f"{bpb.INDEX_NOTE}.md": "empty"})

    def test_heading_embed_is_resolved_from_the_vault(self):
        lines = bpb.expand(["![[Problem - T3 Extra 2 - Infopymes Full Cycle Financial Statements and ROA ROE"
                            "#Step 1. Depreciation and interest 2016]]"], "test")
        self.assertEqual(lines[0], "#### Step 1. Depreciation and interest 2016")
        self.assertTrue(any("20{,}000" in x for x in lines))
        with self.assertRaises(bpb.BankError):
            bpb.expand(["![[Problem - T3 Extra 2 - Infopymes Full Cycle Financial Statements and ROA ROE#No such step]]"], "test")


class RepositoryTests(unittest.TestCase):
    def test_bank_is_up_to_date(self):
        self.assertEqual(bpb.main(["--check"]), 0)

    def test_bank_matches_the_blueprint(self):
        data = json.loads((bpb.OUT_DIR / "problems.json").read_text(encoding="utf-8"))
        blueprint = json.loads((bpb.OUT_DIR / "exam-blueprint.json").read_text(encoding="utf-8"))
        for part in blueprint["parts"]:
            items = [i for i in data["items"] if i["category"] == part["category"]]
            self.assertTrue(all(i["points"] == part["points_each"] for i in items))
            self.assertGreaterEqual(len({i["unit"] for i in items} if part["category"] == "short_theory_case" else items), part["count"])
        self.assertEqual(data["counts"], {"short_theory_case": 24, "extra_practice_problem": 16})
        problems = [i for i in data["items"] if i["category"] == "extra_practice_problem"]
        new = [i for i in problems if not i["official"]]
        self.assertEqual(len(new), 6)
        for arch in bpb.ARCHETYPES:
            self.assertGreaterEqual(sum(i["archetype"] == arch for i in new), 1, arch)


if __name__ == "__main__":
    unittest.main()
