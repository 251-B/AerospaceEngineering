"""Subject index pages as solar systems (assets/js/subject-orbits.js + assets/css/subject-orbits.css):
the loader, the pages it acts on and the rules it must keep (no storage, print and reduced motion)."""
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
JS = (REPO / "assets/js/subject-orbits.js").read_text(encoding="utf-8")
CSS = (REPO / "assets/css/subject-orbits.css").read_text(encoding="utf-8")
THEME = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")


class SubjectOrbitsTests(unittest.TestCase):
    def test_theme_loads_the_script(self):
        self.assertIn("'subject-orbits.js'", THEME)

    def test_acts_only_on_the_three_index_pages_and_skips_print_mode(self):
        self.assertIn("(teoria|problemas|extra-problems)", JS)
        self.assertRegex(JS, r"print=")

    def test_no_storage_and_no_theme_key(self):
        self.assertNotRegex(JS, r"localStorage|sessionStorage")
        self.assertNotIn("ae_theme", JS)

    def test_cards_keep_their_classes(self):
        # the badges of the landing page count problem-card / topic-card elements: never rename them
        self.assertNotRegex(JS, r"classList\.remove\('(topic-card|set-card|problem-card)'")

    def test_reduced_motion_and_print(self):
        self.assertIn("prefers-reduced-motion", CSS)
        self.assertRegex(CSS, r"@media print")

    def test_desktop_only(self):
        self.assertRegex(JS, r"var WIDE = 900;")
        self.assertIn(".orb-system:not(.orb-wide)", CSS)


if __name__ == "__main__":
    unittest.main()
