"""Collapsible problem cards (assets/js/problem-collapse.js): the loader in theme.js brings the script onto
every page, no page carries its own tag, the folding is screen-only (so print and the PDFs are unchanged)
and the script never runs in the PDF print mode or on index pages."""
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
JS = REPO / "assets/js/problem-collapse.js"
CSS = REPO / "assets/css/study-surface.css"


class ProblemCollapseStaticTests(unittest.TestCase):
    def test_theme_js_loads_it_before_the_close_bar(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        names = re.findall(r"'([\w./-]+\.js)'", re.search(r"\[('focus-lab\.js'.*?)\]", theme, re.S).group(1))
        self.assertIn("problem-collapse.js", names)
        self.assertLess(names.index("problem-collapse.js"), names.index("solution-close.js"))

    def test_no_page_carries_its_own_tag(self):
        for page in sorted((REPO / "subjects").rglob("*.html")):
            self.assertNotIn("problem-collapse", page.read_text(encoding="utf-8"), page)

    def test_script_skips_print_mode_and_index_pages_and_stores_nothing(self):
        js = JS.read_text(encoding="utf-8")
        self.assertIn("print=", js)
        self.assertIn("(problemas|extra-problems)", js)
        self.assertIn("(?!index\\.html)", js)
        self.assertNotIn("localStorage", js)
        self.assertNotIn("sessionStorage", js)

    def test_folding_is_screen_only(self):
        css = CSS.read_text(encoding="utf-8")
        start = css.index("15. COLLAPSIBLE PROBLEM CARDS")
        block = css[start:]
        rule = block.index(".pc-card.pc-collapsed > :not(.pc-head)")
        self.assertLess(block.index("@media screen"), rule)
        self.assertIn("@media print { .pc-toggle, .pc-bar { display: none !important; } }", block)

    def test_title_block_rules_spare_the_print_layout(self):
        css = CSS.read_text(encoding="utf-8")
        block = css[css.index("14. ONE TITLE COLOUR PER SUBJECT"):css.index("15. COLLAPSIBLE PROBLEM CARDS")]
        self.assertIn("@media screen", block)
        for line in block.splitlines():
            if line.strip().startswith("html") and "{" in line or line.strip().startswith("html:not"):
                self.assertIn('html:not([data-theme="print"])', line)


if __name__ == "__main__":
    unittest.main()
