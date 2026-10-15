"""Reading palettes: behaviour of the surface manager in assets/js/theme.js (headless Edge/Chrome)
and the colour contract of the palettes in assets/css/study-surface.css."""
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
HARNESS = pathlib.Path(__file__).resolve().parent / "surface_harness.html"
PAGES_HARNESS = pathlib.Path(__file__).resolve().parent / "surface_pages_harness.html"
CSS = REPO / "assets/css/study-surface.css"
CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]

# id -> (theme polarity, background, card, inset, main text, secondary text)
PALETTES = {
    "cream": ("light", "#f5f2eb", "#ffffff", "#ece8df", "#23272f", "#474b56"),
    "sepia": ("light", "#efe8d8", "#f7f2e4", "#e5dcb7", "#342a22", "#4d4137"),
    "slate-paper": ("light", "#eceff2", "#f6f8fa", "#e2e6eb", "#1a222d", "#414a58"),
    "sage": ("light", "#ebf0ea", "#f4f7f3", "#e1e8e0", "#1f2922", "#404d43"),
    "charcoal": ("dark", "#111620", "#18202f", "#141a26", "#dde4ec", "#9fadc0"),
}


def find_browser():
    for name in ("msedge", "chrome", "google-chrome", "chromium"):
        found = shutil.which(name)
        if found:
            return found
    return next((c for c in CANDIDATES if os.path.exists(c)), None)


BROWSER = find_browser()


def luminance(hex_colour):
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    r, g, b = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def palette_block(css, surface, theme):
    m = re.search(r'html\[data-surface="%s"\]\[data-theme="%s"\]\s*\{(.*?)\}' % (surface, theme), css, re.S)
    assert m, f"no CSS block for {surface}/{theme}"
    return {k: v.strip().lower() for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", m.group(1))}


class PaletteContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = CSS.read_text(encoding="utf-8")

    def test_each_palette_defines_the_specified_colours(self):
        for name, (theme, bg, card, inset, text, text2) in PALETTES.items():
            block = palette_block(self.css, name, theme)
            self.assertEqual(
                [block[f"--study-{k}-{theme}"] for k in ("bg", "surface", "inset")], [bg, card, inset], name)
            self.assertEqual([block["--study-text"], block["--study-text-2"]], [text, text2], name)
            self.assertTrue(block[f"--study-border-{theme}"].startswith("rgba("), name)

    def test_main_text_meets_wcag_aaa_on_every_surface(self):
        for name, (_, bg, card, inset, text, _) in PALETTES.items():
            for surface in (bg, card, inset):
                self.assertGreaterEqual(contrast(text, surface), 7.0, f"{name}: {text} on {surface}")

    def test_secondary_text_meets_wcag_aaa_on_every_surface(self):
        # The requested secondary hex values only reached AA (4.5:1); they were nudged to AAA, keeping the hue.
        for name, (_, bg, card, inset, _, text2) in PALETTES.items():
            for surface in (bg, card, inset):
                self.assertGreaterEqual(contrast(text2, surface), 7.0, f"{name}: {text2} on {surface}")

    def test_no_pure_white_or_black_page_inset_or_text(self):
        for name, (_, bg, _, inset, text, text2) in PALETTES.items():
            for colour in (bg, inset, text, text2):
                self.assertNotIn(colour, ("#ffffff", "#000000"), name)

    def test_accent_window_keeps_every_hue_at_aaa(self):
        css = self.css
        self.assertRegex(css, r'--study-l-max:\s*0\.31')
        self.assertRegex(css, r'--study-l-min:\s*0\.91')
        self.assertIn("min(c, 0.13)", css)
        self.assertIn("-webkit-text-fill-color: oklch(from currentcolor", css)

    def test_palettes_are_screen_only_and_scoped_to_their_polarity(self):
        self.assertIn("@media screen", self.css)
        for name, (theme, *_rest) in PALETTES.items():
            self.assertIn(f'[data-surface="{name}"]', self.css)
            self.assertRegex(self.css, r'\[data-surface="%s"\]\[data-theme="%s"\]' % (name, theme))

    def test_no_inline_script_or_theme_named_storage_key_in_the_surface_code(self):
        js = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        self.assertIn("'ae_surface'", js)
        keys = set(re.findall(r"localStorage\s*\.\s*\w+Item\s*\(\s*['\"]([^'\"]+)", js))
        self.assertFalse([k for k in keys if "theme" in k.lower() and k != "ae_theme"], keys)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class SurfaceScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=15000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, timeout=90,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 20)

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class SurfacePagesTests(unittest.TestCase):
    """Real study pages under every palette: AAA text everywhere, and the page's own text never changes."""

    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=600000", "--dump-dom", PAGES_HARNESS.as_uri()],
                capture_output=True, text=True, timeout=300,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_every_page_and_palette_was_audited(self):
        self.assertEqual(len(self.results), 16 * 6)
        self.assertEqual([r for r in self.results if "error" in r], [])

    def test_palette_and_theme_were_applied(self):
        for r in self.results:
            want = r["state"] if r["state"] != "default" else "default"
            self.assertEqual(r["surface"], want, f"{r['page']} {r['state']}")
            self.assertTrue(r["picker"], f"{r['page']}: picker missing")

    def test_the_open_updates_panel_was_audited_too(self):
        missing = [f"{r['page']} [{r['state']}]" for r in self.results if not r.get("updatesPanel")]
        self.assertEqual(missing, [], "the What's new panel was not open when its text was audited")

    def test_the_open_side_menu_was_audited_too(self):
        missing = [f"{r['page']} [{r['state']}]" for r in self.results if not r.get("sidebar")]
        self.assertEqual(missing, [], "the side menu was not open, with its current page marked, when its text was audited")

    def test_text_is_aaa_on_every_page_and_palette(self):
        failures = [f"{r['page']} [{r['state']}] {r['badCount']} below AAA, e.g. {r['bad'][:3]}"
                    for r in self.results if r["state"] != "default" and r["badCount"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))

    def test_a_palette_never_changes_the_text_of_a_page(self):
        by_page = {}
        for r in self.results:
            by_page.setdefault(r["page"], {})[r["state"]] = (r["hash"], r["length"])
        drift = [f"{page}: {states}" for page, states in by_page.items() if len(set(states.values())) != 1]
        self.assertEqual(drift, [], "\n" + "\n".join(drift))


if __name__ == "__main__":
    unittest.main()
