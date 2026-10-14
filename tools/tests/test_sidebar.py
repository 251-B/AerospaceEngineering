"""Side menu (assets/js/sidebar.js + assets/data/nav.js): the loader in theme.js brings it onto every
page, the code stays inside the portal's rules, and the button and drawer behave. The widget runs in
headless Edge/Chrome."""
import html
import json
import pathlib
import re
import subprocess
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "sidebar_harness.html"
JS = REPO / "assets/js/sidebar.js"
CSS = REPO / "assets/css/sidebar.css"


class SidebarStaticTests(unittest.TestCase):
    """Checks that need no browser."""

    def test_theme_js_loads_the_data_then_the_widget(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        m = re.search(r"\[('focus-lab\.js'[^\]]*)\]\.forEach", theme)
        self.assertIsNotNone(m)
        names = re.findall(r"'([^']+)'", m.group(1))
        self.assertIn("../data/nav.js", names)
        self.assertIn("sidebar.js", names)
        self.assertLess(names.index("../data/nav.js"), names.index("sidebar.js"))

    def test_storage_key_is_not_a_theme_key(self):
        js = JS.read_text(encoding="utf-8")
        keys = re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js)
        self.assertTrue(keys)
        self.assertEqual(set(keys), {"KEY"})
        self.assertIn("var KEY = 'ae_nav';", js)

    def test_no_markup_is_built_from_page_or_manifest_text(self):
        js = JS.read_text(encoding="utf-8")
        # innerHTML is only used for the fixed icon paths, never with headings or labels.
        for m in re.finditer(r"innerHTML\s*=\s*([^;]+);", js):
            self.assertEqual(m.group(1).strip(), "inner", m.group(0))
        self.assertNotIn("insertAdjacentHTML", js)

    def test_skipped_in_print_mode(self):
        self.assertIn("has('print')", JS.read_text(encoding="utf-8"))

    def test_hidden_in_print(self):
        css = CSS.read_text(encoding="utf-8")
        self.assertRegex(css, r"@media print\s*\{\s*\.ae-nav-btn, \.ae-nav, \.ae-nav-backdrop \{ display: none !important; \}")

    def test_print_css_is_untouched_so_no_pdf_is_reprinted(self):
        # The PDF hash includes print.css. The menu needs nothing there: in PDF mode (?print=) the script
        # never loads, and the browser's own print is covered by the @media print rule in sidebar.css.
        print_css = (REPO / "assets/css/print.css").read_text(encoding="utf-8")
        self.assertNotIn("ae-nav", print_css)

    def test_text_colours_come_from_the_reading_palette(self):
        css = CSS.read_text(encoding="utf-8")
        colours = set(re.findall(r"(?<![-\w])color:\s*([^;]+);", css))
        self.assertTrue(colours)
        self.assertTrue(colours <= {"var(--nav-text)", "var(--nav-muted)"}, colours)

    def test_no_page_carries_its_own_tag(self):
        for page in list((REPO / "subjects").glob("*/*/*.html")) + [REPO / "index.html"]:
            text = page.read_text(encoding="utf-8")
            self.assertNotIn("sidebar.js", text, page)
            self.assertNotIn("nav.js", text, page)

    def test_manifest_never_lists_laboratory_material(self):
        data = (REPO / "assets/data/nav.js").read_text(encoding="utf-8")
        self.assertNotRegex(data.lower(), r"laborator|(^|/)labs?([/_.-]|\")")
        payload = json.loads(re.search(r"window\.AE_NAV\s*=\s*(\{.*\})\s*;", data, re.S).group(1))
        self.assertEqual(len(payload["subjects"]), 5)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class SidebarBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=60000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, timeout=240,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 38)

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
