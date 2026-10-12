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
    "cream": ("light", "#f5f2eb", "#ffffff", "#ece8df", "#23272f", "#575b66"),
    "sepia": ("light", "#efe8d8", "#f7f2e4", "#e5dcb7", "#342a22", "#63564a"),
    "slate-paper": ("light", "#eceff2", "#f6f8fa", "#e2e6eb", "#1a222d", "#505a69"),
    "sage": ("light", "#ebf0ea", "#f4f7f3", "#e1e8e0", "#1f2922", "#516155"),
    "charcoal": ("dark", "#111620", "#18202f", "#141a26", "#dde4ec", "#94a3b8"),
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

    def test_secondary_text_meets_wcag_aa_on_every_surface(self):
        # The requested secondary colours reach AA (4.5:1) but not AAA (7:1); see the palette comment block.
        for name, (_, bg, card, inset, _, text2) in PALETTES.items():
            for surface in (bg, card, inset):
                self.assertGreaterEqual(contrast(text2, surface), 4.5, f"{name}: {text2} on {surface}")

    def test_no_pure_white_or_black_page_inset_or_text(self):
        for name, (_, bg, _, inset, text, text2) in PALETTES.items():
            for colour in (bg, inset, text, text2):
                self.assertNotIn(colour, ("#ffffff", "#000000"), name)

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


if __name__ == "__main__":
    unittest.main()
