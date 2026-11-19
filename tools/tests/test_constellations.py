"""Home page stellar view (assets/js/constellations.js + assets/css/constellations.css): the files and
keys it must keep, the contrast of its palettes, and the map built from the real nav data in a browser."""
import json
import pathlib
import re
import subprocess
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
JS = (REPO / "assets/js/constellations.js").read_text(encoding="utf-8")
CSS = (REPO / "assets/css/constellations.css").read_text(encoding="utf-8")
INDEX = (REPO / "index.html").read_text(encoding="utf-8")

SLUGS = ["fluid-mechanics", "aerospace-materials-1", "engineering-mechanics", "advanced-maths", "business-management"]
LATIN = ["Stella Fluidorum", "Stella Materiae", "Stella Mechanicae", "Stella Matheseos", "Stella Oeconomiae"]


def luminance(hex_colour):
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


class StaticTests(unittest.TestCase):
    def test_index_loads_the_files_and_keeps_the_classic_view(self):
        self.assertIn('href="assets/css/constellations.css?v=20261125b"', INDEX)
        self.assertIn('src="assets/js/constellations.js?v=20261125a"', INDEX)
        self.assertLess(INDEX.index("theme.js"), INDEX.index("constellations.js"))
        self.assertEqual(INDEX.count('class="subject-card'), 5)
        for slug in SLUGS:
            self.assertIn(f'data-subject="{slug}"', INDEX)
        self.assertIn('id="homeViewToggle"', INDEX)

    def test_storage_keys_are_not_theme_keys(self):
        keys = re.findall(r"var \w+_KEY = '([^']+)'", JS)
        self.assertEqual(sorted(keys), ["ae_home_view", "ae_sky_palette"])
        self.assertFalse([k for k in keys if "theme" in k.lower()])
        self.assertEqual(set(re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", JS)), {"key"})

    def test_latin_titles_and_five_palettes(self):
        for title in LATIN:
            self.assertIn(title, JS)
        for palette in ("deep-cosmos", "observatory-charcoal", "nebula-indigo", "stratospheric-light", "blueprint-cyan"):
            self.assertIn(palette, JS)
            self.assertIn(palette, CSS)

    def test_no_emoji_and_reduced_motion_respected(self):
        for text in (JS, CSS):
            self.assertIsNone(re.search("[\U0001F300-\U0001FAFF☀-➿]", text))
        self.assertIn("prefers-reduced-motion", JS)
        self.assertIn("prefers-reduced-motion", CSS)

    def test_palette_text_is_aaa_on_the_palette_background(self):
        blocks = re.findall(r'html(?:, html)?\[data-sky-palette="([^"]+)"\]\s*\{(.*?)\n\}', CSS, re.S)
        self.assertEqual(len(blocks), 5)
        for name, body in blocks:
            text = re.search(r"--sk-text:\s*(#[0-9a-f]{6})", body).group(1)
            text2 = re.search(r"--sk-text-2:\s*(#[0-9a-f]{6})", body).group(1)
            halo = re.search(r"--sk-halo:\s*(#[0-9a-f]{6})", body).group(1)
            with self.subTest(palette=name):
                self.assertGreaterEqual(contrast(text, halo), 7.0)
                self.assertGreaterEqual(contrast(text2, halo), 7.0)

    def test_open_constellation_names_every_star_with_a_hud_satellite(self):
        self.assertNotIn("SHAPES", JS)   # one plain sparkle per vertex, no per-area polygons
        for cls in ("star-sat", "sat-leader", "sat-ring", "sat-icon", "sat-name", "sat-tag", "sat-hit"):
            self.assertIn(cls, JS)
            self.assertIn("." + cls, CSS)
        self.assertIn("href: '#' + sec.icon", JS)
        self.assertRegex(CSS, r"\.const\.is-active \.star-sat \{ visibility: visible")
        for icon in ("i-theory", "i-problems", "i-extra", "i-formula", "i-sim", "i-pdf", "i-exams"):
            self.assertIn(f'<symbol id="{icon}"', INDEX)

    def test_subject_tag_colours_are_aaa_on_every_palette(self):
        dark = dict(re.findall(r"--ct-(\w+): (#[0-9a-f]{6})", CSS.split("html[data-theme=\"light\"] .sky-view")[0].split(".sky-view {")[1]))
        light = dict(re.findall(r"--ct-(\w+): (#[0-9a-f]{6})", CSS.split("html[data-theme=\"light\"] .sky-view {")[1].split("}")[0]))
        halos = dict(re.findall(r'data-sky-palette="([^"]+)"\]\s*\{[^}]*?--sk-halo:\s*(#[0-9a-f]{6})', CSS))
        self.assertEqual(len(halos), 5)
        for name, halo in halos.items():
            for subject, colour in (light if name == "stratospheric-light" else dark).items():
                with self.subTest(palette=name, subject=subject):
                    self.assertGreaterEqual(contrast(colour, halo), 7.0)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class BrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            with tempfile.TemporaryDirectory() as profile:
                proc = subprocess.run(
                    [BROWSER, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                     f"--user-data-dir={profile}", "--virtual-time-budget=15000", "--dump-dom", (REPO / "index.html").as_uri()],
                    capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=45)
        except subprocess.TimeoutExpired:
            raise unittest.SkipTest("headless browser did not finish (blocked network such as Google Fonts can stall it)")
        cls.dom = proc.stdout

    def test_five_constellations_with_their_stars(self):
        self.assertEqual(len(re.findall(r'<g class="const"', self.dom)), 5)
        for title in LATIN:
            self.assertIn(title, self.dom)
        self.assertGreaterEqual(len(re.findall(r'<a class="star', self.dom)), 25)

    def test_defaults_to_the_stellar_view_and_has_no_preparation_label(self):
        self.assertRegex(self.dom, r'<html[^>]*data-home-view="constellations"')
        self.assertNotIn("In Preparation", self.dom)

    def test_hud_labels_do_not_overlap_or_clip_on_desktop_and_phone(self):
        harness = REPO / "tools/tests/constellations_harness.html"
        try:
            with tempfile.TemporaryDirectory() as profile:
                proc = subprocess.run(
                    [BROWSER, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                     f"--user-data-dir={profile}", "--window-size=1400,1000", "--virtual-time-budget=60000", "--dump-dom", harness.as_uri()],
                    capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        except subprocess.TimeoutExpired:
            raise unittest.SkipTest("headless browser did not finish")
        match = re.search(r'<pre id="result">(.*?)</pre>', proc.stdout, re.S)
        self.assertTrue(match and match.group(1).startswith("{"), proc.stdout[-500:])
        result = json.loads(match.group(1).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))
        self.assertEqual(set(result), {"1280x800", "768x1024", "375x812"})
        for size, slugs in result.items():
            self.assertTrue(slugs.pop("panoramaHidden"), size)
            for slug, issues in slugs.items():
                with self.subTest(size=size, slug=slug):
                    self.assertEqual(issues, [])


if __name__ == "__main__":
    unittest.main()
