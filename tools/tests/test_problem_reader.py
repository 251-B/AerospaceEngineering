"""Problem reader (assets/js/problem-reader.js + assets/css/problem-reader.css): loaded by theme.js after the
card folding and the theory reader (whose helpers it borrows), never carried by a page, skipped in the PDF
print mode and on index pages, stores only the reading mode, and everything it hides is screen-only (print
and the PDFs show every step). The PDFs do not depend on these files."""
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
JS = REPO / "assets/js/problem-reader.js"
CSS = REPO / "assets/css/problem-reader.css"


class ProblemReaderStaticTests(unittest.TestCase):
    def test_theme_js_loads_it_after_its_helpers_and_before_the_close_bar(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        names = re.findall(r"'([\w./-]+\.js)'", re.search(r"\[('focus-lab\.js'.*?)\]", theme, re.S).group(1))
        self.assertLess(names.index("problem-collapse.js"), names.index("problem-reader.js"))
        self.assertLess(names.index("theory-reader.js"), names.index("problem-reader.js"))
        self.assertLess(names.index("problem-reader.js"), names.index("solution-close.js"))

    def test_theory_reader_lends_its_helpers(self):
        js = (REPO / "assets/js/theory-reader.js").read_text(encoding="utf-8")
        self.assertIn("window.AEReaderKit = {", js)
        self.assertLess(js.index("window.AEReaderKit = {"), js.index("if (!IS_THEORY)"))

    def test_no_page_carries_its_own_tag(self):
        for page in sorted((REPO / "subjects").rglob("*.html")):
            self.assertNotIn("problem-reader", page.read_text(encoding="utf-8"), page)

    def test_script_skips_print_mode_and_index_pages_and_stores_only_the_mode(self):
        js = JS.read_text(encoding="utf-8")
        self.assertIn("print=", js)
        self.assertIn("(problemas|extra-problems)", js)
        self.assertIn("(?!index\\.html)", js)
        self.assertEqual(re.findall(r"localStorage\.\w+\(([^,)]+)", js), ["MODE_KEY", "MODE_KEY"])
        self.assertIn("var MODE_KEY = 'ae_problem_mode';", js)
        for use in re.finditer(r"localStorage", js):
            self.assertIn("try {", js[max(0, use.start() - 80):use.start()])
        self.assertNotIn("sessionStorage", js)
        self.assertNotIn("eval(", js)

    def test_hiding_is_screen_only(self):
        css = CSS.read_text(encoding="utf-8")
        screen, printing = css.index("@media screen"), css.index("@media print")
        self.assertGreater(css.index(".pr-hidden { display: none"), screen)
        self.assertIn(".pr-hidden { display: block !important; }", css[printing:])
        for line in css[screen:printing].splitlines():
            if line.strip().startswith("html."):
                self.assertIn(':not([data-theme="print"])', line)

    def test_text_colours_come_from_the_reading_palette(self):
        css = CSS.read_text(encoding="utf-8")
        for decl in re.findall(r"(?<![-\w])color:\s*([^;]+);", css):
            self.assertTrue(decl.startswith("var(--tr-"), decl)

    def test_no_emojis_and_pdfs_do_not_depend_on_it(self):
        for path in (JS, CSS):
            self.assertIsNone(re.search("[\U0001F300-\U0001FAFF☀-➿]", path.read_text(encoding="utf-8")), path)
        build = (REPO / "tools/build_pdfs.py").read_text(encoding="utf-8")
        self.assertNotIn("problem-reader", re.search(r"INPUTS = \(([^)]*)\)", build).group(1))
        self.assertNotIn("problem-reader", (REPO / "assets/css/print.css").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
