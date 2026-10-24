import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import build_formula_sheet as fs  # noqa: E402

NOTE = """---
tags: [x]
---
# Title
intro stays in the vault

## Unit 2 — First order
Pages: Theory=teoria/topic-2.html

### Derivation: The integrating factor
In short: multiply by $\\mu$.

| Step | Why |
| --- | --- |
| $a < b$ | **because** |

### Trap: Lost solutions
- dividing by $h(x)$
"""


class BuildFormulaSheetTest(unittest.TestCase):
    def test_note_renders_sections_cards_and_steps(self):
        out = fs.render_note(NOTE)
        self.assertNotIn("intro stays", out)
        self.assertIn('<section class="fs-unit" id="unit-2-first-order"', out)
        self.assertIn('<a href="../teoria/topic-2.html">Theory</a>', out)
        self.assertIn('<details class="fs-deriv" open><summary>', out)
        self.assertIn('<div class="fs-step-math">$a &lt; b$</div>', out)
        self.assertIn("<strong>because</strong>", out)
        self.assertIn('class="fs-card fs-trap"', out)

    def test_derivation_needs_a_summary_and_kind_is_checked(self):
        with self.assertRaises(ValueError):
            fs.render_card("Derivation: x", ["no summary"], set())
        with self.assertRaises(ValueError):
            fs.render_card("Lemma: x", [], set())

    def test_math_is_not_touched_by_inline_markdown(self):
        self.assertEqual(fs.inline("$a*b*c$ and *it*"), "$a*b*c$ and <em>it</em>")

    def test_pages_are_up_to_date(self):
        self.assertEqual(fs.main(["--check"]), 0)


if __name__ == "__main__":
    unittest.main()
