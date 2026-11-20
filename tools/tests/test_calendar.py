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
EXPECTED_SCENARIOS = 40


class CalendarStaticTests(unittest.TestCase):
    def test_storage_key(self):
        js = CORE.read_text(encoding="utf-8")
        self.assertIn("KEY = 'ae_calendar'", js)
        self.assertEqual(set(re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js)), {"KEY"})
        self.assertNotIn("theme", "ae_calendar")

    def test_account_syncs_the_calendar(self):
        js = (REPO / "assets/js/account.js").read_text(encoding="utf-8")
        sync = re.search(r"var SYNC_KEYS = \[([^\]]*)\]", js).group(1)
        self.assertIn("'ae_calendar'", sync)
        self.assertIn("['ae_calendar', 'Calendar (classes, labs, exams)']", js)
        self.assertIn("absorbCalendar(keys[CALENDAR_KEY])", js)
        self.assertIn("changed: function () { schedulePush(); }", js)

    def test_sync_merges_entry_by_entry_on_every_page(self):
        # On pages without calendar-core.js, account.js loads it before merging, so a synced
        # record is never replaced whole by the copy changed last.
        js = (REPO / "assets/js/account.js").read_text(encoding="utf-8")
        body = re.search(r"function absorbCalendar\(cloud\) \{(.*?)\n  \}\n", js, re.S).group(1)
        self.assertIn("assets/js/calendar-core.js", body)
        self.assertIn("window.AECalendar.merge(readJSON(CALENDAR_KEY), cloud)", body)
        self.assertIn("schedulePush()", body)

    def test_account_menu_links_the_calendar(self):
        js = (REPO / "assets/js/account.js").read_text(encoding="utf-8")
        self.assertIn("[['My study', 'dashboard.html'], ['Calendar', 'calendar.html'], ['Settings', 'settings.html']", js)

    def test_timer_and_sideris_pick_up_requests(self):
        pom = (REPO / "assets/js/pomodoro.js").read_text(encoding="utf-8")
        chat = (REPO / "assets/js/ai-chat.js").read_text(encoding="utf-8")
        self.assertIn("sessionStorage.getItem('ae_pomodoro_pending')", pom)
        self.assertIn("sessionStorage.removeItem('ae_pomodoro_pending')", pom)
        self.assertIn("sessionStorage.getItem('ae_sideris_pending')", chat)
        self.assertIn("sessionStorage.removeItem('ae_sideris_pending')", chat)

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
