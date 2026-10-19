"""Close bar of the worked solutions (assets/js/solution-close.js): the loader in theme.js brings it onto
every page, the code stays inside the portal's rules, and the button folds the solution and returns to its
summary. The widget runs in headless Edge/Chrome."""
import html
import json
import pathlib
import re
import subprocess
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "solution_close_harness.html"
JS = REPO / "assets/js/solution-close.js"
CSS = REPO / "assets/css/solution-close.css"


class SolutionCloseStaticTests(unittest.TestCase):
    """Checks that need no browser."""

    def test_theme_js_loads_it_after_the_side_menu(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        m = re.search(r"\[('focus-lab\.js'[^\]]*)\]\.forEach", theme)
        self.assertIsNotNone(m)
        names = re.findall(r"'([^']+)'", m.group(1))
        self.assertIn("solution-close.js", names)
        self.assertEqual(names[-1], "solution-close.js")
        self.assertLess(names.index("sidebar.js"), names.index("solution-close.js"))

    def test_no_storage_is_used(self):
        js = JS.read_text(encoding="utf-8")
        self.assertNotIn("localStorage", js)
        self.assertNotIn("sessionStorage", js)

    def test_no_markup_is_built_from_text(self):
        js = JS.read_text(encoding="utf-8")
        self.assertNotIn("innerHTML", js)
        self.assertNotIn("insertAdjacentHTML", js)

    def test_no_emoji(self):
        emoji = re.compile("[☀-➿\U0001f000-\U0001faff⬀-⯿]")
        for path in (JS, CSS):
            self.assertIsNone(emoji.search(path.read_text(encoding="utf-8")), path.name)

    def test_skipped_in_print_mode(self):
        self.assertIn("has('print')", JS.read_text(encoding="utf-8"))

    def test_hidden_in_print(self):
        css = CSS.read_text(encoding="utf-8")
        self.assertRegex(css, r"@media print\s*\{\s*\.sol-close-bar \{ display: none !important; \}")

    def test_print_css_is_untouched_so_no_pdf_is_reprinted(self):
        print_css = (REPO / "assets/css/print.css").read_text(encoding="utf-8")
        self.assertNotIn("sol-close", print_css)

    def test_text_colours_come_from_the_reading_palette(self):
        css = CSS.read_text(encoding="utf-8")
        colours = set(re.findall(r"(?<![-\w])color:\s*([^;]+);", css))
        self.assertTrue(colours)
        self.assertTrue(colours <= {"var(--sc-text)", "var(--sc-text-strong)"}, colours)

    def test_no_page_carries_its_own_tag(self):
        for page in list((REPO / "subjects").glob("*/*/*.html")) + [REPO / "index.html"]:
            text = page.read_text(encoding="utf-8")
            self.assertNotIn("solution-close", text, page)
            self.assertNotIn("sol-close", text, page)

    def test_pages_have_the_markup_the_script_hooks_into(self):
        """The script needs the summary inside each <details>; a page that loses it would get a dead bar."""
        solution = re.compile(r'<details class="solution-details">\s*<summary class="solution-summary"')
        card = re.compile(r'<details[^>]*class="problem-card"[^>]*>\s*<summary class="problem-summary"')
        found = 0
        for page in sorted((REPO / "subjects").glob("*/problemas/*.html")):
            text = page.read_text(encoding="utf-8")
            n = len(re.findall(r'<details class="solution-details"', text)) + len(re.findall(r'<details[^>]*class="problem-card"', text))
            hooked = len(solution.findall(text)) + len(card.findall(text))
            with self.subTest(page=page.name):
                self.assertEqual(n, hooked)
            found += n
        self.assertGreater(found, 100)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class SolutionCloseBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=60000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 32)

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
