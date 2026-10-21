"""Tests of the Advanced Maths problem-sheet pages (tools/am_problems/)."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "am_problems"))
sys.path.insert(0, str(ROOT / "tools"))

import build  # noqa: E402
import mdhtml  # noqa: E402


class MarkdownDialect(unittest.TestCase):
    def test_math_is_protected_from_emphasis(self):
        self.assertEqual(mdhtml.inline("a $x_1*y*z_2$ and *em* and **b**"), "a $x_1*y*z_2$ and <em>em</em> and <strong>b</strong>")

    def test_display_math_and_lists(self):
        blocks = mdhtml.parse("text\n\n$$ a = b $$\n\n- one\n- two\n\n| h |\n| :--- |\n| c |\n")
        self.assertEqual([b[0] for b in blocks], ["p", "math", "ul", "table"])

    def test_callout_and_figure(self):
        blocks = mdhtml.parse("> [!result] Title\n> body\n\n![[attachments/AM-PS/x.svg]]\n*cap*\n")
        self.assertEqual(blocks[0][:3], ("callout", "result", "Title"))
        self.assertEqual(blocks[1], ("fig", "x", "cap"))


class GeneratedFiles(unittest.TestCase):
    def test_pages_are_up_to_date(self):
        self.assertEqual(build.check(), [])

    def test_every_figure_of_a_note_is_registered(self):
        figs = json.loads((ROOT / build.FIGS).read_text(encoding="utf-8"))
        for path in (ROOT / build.VAULT).glob("Problem - Ch[34]-I*-P*.md"):
            _, _, statement, phases = mdhtml.split_note(path.read_text(encoding="utf-8"))
            for md in [statement] + [p[2] for p in phases]:
                for b in mdhtml.parse(md):
                    if b[0] == "fig":
                        self.assertIn(b[1], figs, f"{path.name}: {b[1]}")

    def test_each_sheet_has_a_page_with_one_card_per_exercise(self):
        sheets = json.loads((ROOT / build.SHEETS).read_text(encoding="utf-8"))["sheets"]
        for sh in sheets:
            html = (ROOT / build.SUBJECT / sh["page"]).read_text(encoding="utf-8")
            self.assertEqual(html.count('class="problem-card"'), len(sh["cards"]), sh["page"])


if __name__ == "__main__":
    unittest.main()
