"""Account calendar: assets/js/calendar-core.js (occurrences, plan mapping, sync merge), the
calendar page and its wiring into the account scripts. Browser checks run calendar_harness.html
in headless Edge/Chrome."""
import html
import json
import pathlib
import re
import subprocess
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "calendar_harness.html"
CORE = REPO / "assets/js/calendar-core.js"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
EXPECTED_SCENARIOS = 16


class CalendarStaticTests(unittest.TestCase):
    def test_storage_key(self):
        js = CORE.read_text(encoding="utf-8")
        self.assertIn("KEY = 'ae_calendar'", js)
        self.assertEqual(set(re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js)), {"KEY"})
        self.assertNotIn("theme", "ae_calendar")

    def test_no_canvas_no_emoji(self):
        text = CORE.read_text(encoding="utf-8")
        self.assertNotIn("canvas", text.lower())
        self.assertIsNone(EMOJI.search(text))


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class CalendarBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=30000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), EXPECTED_SCENARIOS, [r["name"] for r in self.results])

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
