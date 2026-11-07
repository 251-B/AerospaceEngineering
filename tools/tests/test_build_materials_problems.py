"""The Topic 5 problems page of Aerospace Materials I is generated from its vault notes."""
import pathlib
import sys
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import build_materials_problems as bmp  # noqa: E402


class MaterialsProblemsTests(unittest.TestCase):
    def test_page_and_figures_are_current(self):
        self.assertEqual(bmp.main(["--check"]), 0)

    def test_every_note_is_a_card_with_statement_and_four_phases(self):
        page, _ = bmp.build_page()
        n = len(list(bmp.VAULT.glob("Problem - T5-*.md")))
        self.assertGreater(n, 0)
        self.assertEqual(page.count('class="problem-card"'), n)
        self.assertEqual(page.count('class="statement-box"'), n)
        self.assertEqual(page.count('class="phase-step phase-'), 4 * n)
        self.assertEqual(page.count('class="src-link"'), n)

    def test_cards_are_numbered_in_order(self):
        page, _ = bmp.build_page()
        ids = [int(x) for x in __import__("re").findall(r'id="prob-(\d+)"', page)]
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()


class Topic6ProblemsTests(unittest.TestCase):
    def test_every_t6_note_is_a_card_with_four_blocks(self):
        page, _ = bmp.build_page(6)
        n = len(list(bmp.VAULT.glob("Problem - T6-*.md")))
        self.assertEqual(n, bmp.TOPICS[6]["total"])
        self.assertEqual(page.count('class="problem-card"'), n)
        self.assertEqual(page.count('class="phase-step phase-'), 4 * n)
        self.assertNotIn("Phase 1", page)

    def test_t5_and_t6_notes_do_not_show_the_word_phase(self):
        for path in [*bmp.VAULT.glob("Problem - T5-*.md"), *bmp.VAULT.glob("Problem - T6-*.md")]:
            self.assertNotIn("Phase", path.read_text(encoding="utf-8"), path.name)
