"""What's new panel (assets/js/updates.js + assets/data/updates.js): the data file is valid and honest,
the loader in theme.js brings the widget onto every page, and the bell, panel and toast behave.
The widget runs in headless Edge/Chrome."""
import datetime
import html
import json
import pathlib
import re
import subprocess
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "updates_harness.html"
JS = REPO / "assets/js/updates.js"
CSS = REPO / "assets/css/updates.css"
DATA = REPO / "assets/data/updates.js"

TAGS = {"Fluid Mechanics", "Engineering Mechanics", "Aerospace Materials I", "Advanced Maths",
        "Business Management", "Portal"}
FIELDS = {"id", "date", "tag", "title", "text", "link"}


def load_entries():
    """The array between the brackets is pure JSON, so Python can read what the browser reads."""
    source = DATA.read_text(encoding="utf-8")
    m = re.search(r"window\.AE_UPDATES\s*=\s*(\[.*\])\s*;", source, re.S)
    if not m:
        raise AssertionError("assets/data/updates.js must define window.AE_UPDATES = [ ... ];")
    return json.loads(m.group(1))


class UpdatesDataTests(unittest.TestCase):
    """The hand-edited entries."""

    @classmethod
    def setUpClass(cls):
        cls.entries = load_entries()

    def test_there_are_enough_entries_for_the_browser_scenarios(self):
        # The harness relies on a first visit with three unread entries (so "+2 more"), older ones read, and a link to resolve.
        self.assertGreaterEqual(len(self.entries), 4)
        self.assertGreaterEqual(len([e for e in self.entries if e.get("link")]), 1)
        self.assertEqual(len({e["title"] for e in self.entries[:3]}), 3)

    def test_required_fields_and_no_strays(self):
        for e in self.entries:
            with self.subTest(id=e.get("id")):
                self.assertTrue({"id", "date", "tag", "title", "text"} <= set(e), e)
                self.assertTrue(set(e) <= FIELDS, set(e) - FIELDS)
                for name in set(e):
                    self.assertIsInstance(e[name], str)
                    self.assertTrue(e[name].strip(), name)

    def test_ids_are_unique_slugs(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))
        for i in ids:
            self.assertRegex(i, r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(-[a-z0-9]+)*$")

    def test_id_starts_with_the_entry_date(self):
        for e in self.entries:
            self.assertTrue(e["id"].startswith(e["date"]), e["id"])

    def test_dates_are_real_and_newest_first(self):
        dates = [datetime.date.fromisoformat(e["date"]) for e in self.entries]
        self.assertEqual(dates, sorted(dates, reverse=True))

    def test_tags_are_known(self):
        for e in self.entries:
            self.assertIn(e["tag"], TAGS, e["id"])

    def test_lengths(self):
        for e in self.entries:
            self.assertLessEqual(len(e["title"]), 70, e["id"])
            self.assertLessEqual(len(e["text"]), 180, e["id"])

    def test_text_is_plain(self):
        for e in self.entries:
            for name in ("title", "text"):
                self.assertNotRegex(e[name], r"[<>]|\$|\\\(", f"{e['id']}.{name}")

    def test_links_exist_and_are_never_laboratory_material(self):
        for e in self.entries:
            link = e.get("link")
            if link is None:
                continue
            with self.subTest(id=e["id"]):
                self.assertNotRegex(link, r"^([a-z][a-z0-9+.-]*:|/)", "links are paths from the portal root")
                self.assertNotIn("..", link)
                self.assertTrue((REPO / link).is_file(), link)
                self.assertNotRegex(link.lower(), r"laborator|(^|/)labs?([/_.-]|$)")

    def test_no_laboratory_entries(self):
        for e in self.entries:
            # "Focus Lab" is a portal tool, not laboratory material.
            words = f"{e['title']} {e['text']}".lower().replace("focus lab", "")
            self.assertNotRegex(words, r"\blabs?\b|laborator", e["id"])


class UpdatesStaticTests(unittest.TestCase):
    """Checks that need no browser."""

    def test_theme_js_loads_the_data_then_the_widget(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        m = re.search(r"\[('focus-lab\.js'[^\]]*)\]\.forEach", theme)
        self.assertIsNotNone(m)
        names = re.findall(r"'([^']+)'", m.group(1))
        self.assertIn("../data/updates.js", names)
        self.assertIn("updates.js", names)
        self.assertLess(names.index("../data/updates.js"), names.index("updates.js"))

    def test_storage_key_is_not_a_theme_key(self):
        js = JS.read_text(encoding="utf-8")
        keys = re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js)
        self.assertTrue(keys)
        # `probe` is the storage check, written and removed under KEY + '_probe'.
        self.assertEqual(set(keys), {"KEY", "probe"})
        self.assertIn("var probe = KEY + '_probe';", js)
        self.assertIn("var KEY = 'ae_updates';", js)

    def test_no_markup_is_built_from_entry_data(self):
        js = JS.read_text(encoding="utf-8")
        # innerHTML is only used for the two fixed icon paths, never with entry fields.
        for m in re.finditer(r"innerHTML\s*=\s*([^;]+);", js):
            self.assertEqual(m.group(1).strip(), "inner", m.group(0))
        self.assertNotIn("insertAdjacentHTML", js)

    def test_skipped_in_print_mode(self):
        self.assertIn("has('print')", JS.read_text(encoding="utf-8"))

    def test_hidden_in_print(self):
        css = CSS.read_text(encoding="utf-8")
        self.assertRegex(css, r"@media print\s*\{\s*\.upd-bell, \.upd-panel, \.upd-toast, \.upd-sr \{ display: none !important; \}")
        self.assertIn('html[data-theme="print"] .upd-bell', css)
        self.assertIn('html[data-theme="print"] .upd-sr', css)

    def test_text_colours_come_from_the_reading_palette(self):
        css = CSS.read_text(encoding="utf-8")
        colours = set(re.findall(r"(?<![-\w])color:\s*([^;]+);", css))
        self.assertTrue(colours)
        self.assertTrue(colours <= {"var(--upd-text)", "var(--upd-muted)", "var(--upd-surface)"}, colours)

    def test_no_page_carries_its_own_tag(self):
        for page in list((REPO / "subjects").glob("*/*/*.html")) + [REPO / "index.html"]:
            self.assertNotIn("updates.js", page.read_text(encoding="utf-8"), page)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class UpdatesBrowserTests(unittest.TestCase):
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
        self.assertEqual(len(self.results), 38)

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
