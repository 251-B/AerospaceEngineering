"""Focus Lab (assets/js/focus-lab.js): presets, noise synthesis, stereo routing, persistence and
the loader in theme.js. The audio engine is rendered offline in headless Edge/Chrome."""
import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "focus_lab_harness.html"
CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]


def find_browser():
    for name in ("msedge", "chrome", "google-chrome", "chromium"):
        found = shutil.which(name)
        if found:
            return found
    return next((c for c in CANDIDATES if os.path.exists(c)), None)


BROWSER = find_browser()


class FocusLabStaticTests(unittest.TestCase):
    """Checks that need no browser."""

    def test_theme_js_loads_focus_lab(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        self.assertIn("'focus-lab.js'", theme)

    def test_storage_key_is_not_a_theme_key(self):
        js = (REPO / "assets/js/focus-lab.js").read_text(encoding="utf-8")
        keys = re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js)
        self.assertTrue(keys)
        self.assertEqual(set(keys), {"KEY"})
        self.assertIn("var KEY = 'ae_focus_lab';", js)

    def test_no_audio_files(self):
        js = (REPO / "assets/js/focus-lab.js").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"\.(mp3|wav|ogg|m4a)\b", js))

    def test_hidden_in_print(self):
        css = (REPO / "assets/css/focus-lab.css").read_text(encoding="utf-8")
        self.assertRegex(css, r"@media print\s*\{\s*\.fl-launcher, \.fl-panel \{ display: none !important; \}")
        self.assertIn('html[data-theme="print"] .fl-launcher', css)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class FocusLabBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 "--autoplay-policy=no-user-gesture-required", f"--user-data-dir={profile}",
                 "--virtual-time-budget=60000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 21)

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
