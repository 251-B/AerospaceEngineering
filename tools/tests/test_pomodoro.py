"""Study timer (assets/js/pomodoro.js): session planner, duration parser, wall-clock timer,
persistence, position above the Focus button, and the loader in theme.js. The widget runs in
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
HARNESS = pathlib.Path(__file__).resolve().parent / "pomodoro_harness.html"
JS = REPO / "assets/js/pomodoro.js"
CSS = REPO / "assets/css/pomodoro.css"


class PomodoroStaticTests(unittest.TestCase):
    """Checks that need no browser."""

    def test_theme_js_loads_the_timer(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        self.assertIn("'pomodoro.js'", theme)

    def test_storage_key_is_not_a_theme_key(self):
        js = JS.read_text(encoding="utf-8")
        keys = re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js)
        self.assertTrue(keys)
        self.assertEqual(set(keys), {"KEY"})
        self.assertIn("var KEY = 'ae_pomodoro';", js)

    def test_no_audio_files(self):
        self.assertIsNone(re.search(r"\.(mp3|wav|ogg|m4a)\b", JS.read_text(encoding="utf-8")))

    def test_hidden_in_print(self):
        css = CSS.read_text(encoding="utf-8")
        self.assertRegex(css, r"@media print\s*\{\s*\.pm-launcher, \.pm-panel \{ display: none !important; \}")
        self.assertIn('html[data-theme="print"] .pm-launcher', css)

    def test_text_colours_come_from_the_reading_palette(self):
        css = CSS.read_text(encoding="utf-8")
        colours = set(re.findall(r"(?<![-\w])color:\s*([^;]+);", css))
        self.assertTrue(colours)
        self.assertTrue(colours <= {"var(--pm-text)", "var(--pm-muted)", "var(--pm-surface)"}, colours)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class PomodoroBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=30000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, timeout=180,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 25)

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))
