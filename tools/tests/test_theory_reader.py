"""Theory reader (assets/js/theory-reader.js + assets/css/theory-reader.css): the loader in theme.js brings
the script onto every page, no page carries its own tag, it acts on theory topic pages only, never runs in
the PDF print mode, stores nothing, and everything it hides or folds is screen-only (print and the PDFs
show the page as written). The PDFs do not depend on these files."""
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
JS = REPO / "assets/js/theory-reader.js"
CSS = REPO / "assets/css/theory-reader.css"


class TheoryReaderStaticTests(unittest.TestCase):
    def test_theme_js_loads_it_after_the_side_menu(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        names = re.findall(r"'([\w./-]+\.js)'", re.search(r"\[('focus-lab\.js'.*?)\]", theme, re.S).group(1))
        self.assertIn("theory-reader.js", names)
        # after sidebar.js, so a heading the side menu named keeps that id
        self.assertLess(names.index("sidebar.js"), names.index("theory-reader.js"))

    def test_no_page_carries_its_own_tag(self):
        for page in sorted((REPO / "subjects").rglob("*.html")):
            self.assertNotIn("theory-reader", page.read_text(encoding="utf-8"), page)

    def test_script_acts_on_theory_topic_pages_only_and_stores_nothing(self):
        js = JS.read_text(encoding="utf-8")
        self.assertIn("print=", js)
        self.assertIn(r"\/teoria\/topic-", js)
        self.assertNotIn("localStorage", js)
        self.assertNotIn("sessionStorage", js)
        self.assertNotIn("eval(", js)

    def test_hiding_and_folding_are_screen_only(self):
        css = CSS.read_text(encoding="utf-8")
        screen = css.index("@media screen")
        for rule in (".tr-cite { display: none", ".tr-fold { display: none", ".tr-folded > :not(.tr-folded-title)",
                     ".tr-hidden { display: none", ".tr-dfolded :is(.derivation-steps"):
            self.assertGreater(css.index(rule), screen, rule)
        printing = css[css.index("@media print"):]
        self.assertIn(".tr-rail, .tr-more, .tr-sec-toggle, .tr-secbar { display: none !important; }", printing)
        self.assertIn(".tr-fold { display: inline !important; }", printing)
        for line in css[screen:css.index("@media print")].splitlines():
            if line.strip().startswith("html."):
                self.assertIn(':not([data-theme="print"])', line)

    def test_text_colours_come_from_the_reading_palette(self):
        css = CSS.read_text(encoding="utf-8")
        for decl in re.findall(r"(?<![-\w])color:\s*([^;]+);", css):
            self.assertTrue(decl.startswith("var(--tr-") or decl.strip() == "inherit !important", decl)
        self.assertIn("var(--study-text, #f8fafc)", css)
        self.assertIn("var(--study-text-2, #334155)", css)

    def test_pdfs_do_not_depend_on_it(self):
        build = (REPO / "tools/build_pdfs.py").read_text(encoding="utf-8")
        inputs = re.search(r"INPUTS = \(([^)]*)\)", build).group(1)
        self.assertNotIn("theory-reader", inputs)
        self.assertNotIn("theory-reader", (REPO / "assets/css/print.css").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
