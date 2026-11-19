"""Guided tour for new accounts (assets/js/tour.js): twelve skippable steps across the portal,
loaded by account.js for signed-in readers. Browser checks run tour_harness.html in headless
Edge/Chrome."""
import html
import json
import pathlib
import re
import subprocess
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "tour_harness.html"
JS = REPO / "assets/js/tour.js"
CSS = REPO / "assets/css/tour.css"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


class TourStaticTests(unittest.TestCase):
    def test_storage_key(self):
        js = JS.read_text(encoding="utf-8")
        self.assertIn("var KEY = 'ae_tour';", js)
        self.assertEqual(set(re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js)), {"KEY"})

    def test_no_emoji_hidden_in_print_reduced_motion(self):
        js, css = JS.read_text(encoding="utf-8"), CSS.read_text(encoding="utf-8")
        self.assertIsNone(EMOJI.search(js + css))
        self.assertRegex(css, r"@media print\s*\{[^}]*\.tour-card")
        self.assertIn("prefers-reduced-motion", css)
        self.assertIn("has('print')", js)

    def test_text_colours_from_the_reading_palette(self):
        css = CSS.read_text(encoding="utf-8")
        colours = set(re.findall(r"(?<![-\w])color:\s*([^;]+);", css))
        self.assertTrue(colours <= {"var(--tour-text)", "var(--tour-muted)", "var(--tour-on-accent)"}, colours)

    def test_account_loads_and_syncs_the_tour(self):
        js = (REPO / "assets/js/account.js").read_text(encoding="utf-8")
        self.assertIn("'ae_tour'", re.search(r"var SYNC_KEYS = \[([^\]]*)\]", js).group(1))
        self.assertIn("assets/js/tour.js", js)
        self.assertIn("'Take the tour'", js)

    def test_signup_offers_the_tour(self):
        page = (REPO / "account/signup.html").read_text(encoding="utf-8")
        self.assertIn('href="dashboard.html?tour=0"', page)
        self.assertIn("data-skip-tour", page)

    def test_tour_pages_exist(self):
        js = JS.read_text(encoding="utf-8")
        for page in re.findall(r"page: '([^']+)'", js):
            self.assertTrue((REPO / page).is_file(), page)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class TourBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=20000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 10, [r["name"] for r in self.results])

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
