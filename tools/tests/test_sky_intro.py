"""Welcome screen and celestial sound of the home page (assets/js/sky-intro.js, assets/js/sky-sound.js,
assets/css/sky-intro.css): files, storage keys, no audio files, reduced motion, accessibility hooks."""
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
INTRO = (REPO / "assets/js/sky-intro.js").read_text(encoding="utf-8")
SOUND = (REPO / "assets/js/sky-sound.js").read_text(encoding="utf-8")
CSS = (REPO / "assets/css/sky-intro.css").read_text(encoding="utf-8")
HEAD = (REPO / "assets/js/constellations.js").read_text(encoding="utf-8")
INDEX = (REPO / "index.html").read_text(encoding="utf-8")


class SkyIntroTests(unittest.TestCase):
    def test_index_carries_the_welcome_screen_and_the_scripts(self):
        for needle in ('id="skyIntro"', 'id="introIgnite"', 'id="introSkip"', 'id="soundToggle"', 'id="introReplay"', "Ready to ignite?"):
            self.assertIn(needle, INDEX)
        self.assertRegex(INDEX, r'src="assets/js/sky-sound\.js(\?v=\w+)?"')
        self.assertRegex(INDEX, r'src="assets/js/sky-intro\.js(\?v=\w+)?"')
        self.assertRegex(INDEX, r'href="assets/css/sky-intro\.css(\?v=\w+)?"')

    def test_storage_keys_are_not_theme_keys(self):
        for source in (INTRO, SOUND, HEAD):
            for key in re.findall(r"['\"](ae_[a-z_]+)['\"]", source):
                self.assertNotIn("theme", key.lower())
        self.assertIn("ae_sky_sound", SOUND)
        self.assertIn("ae_intro", INTRO)

    def test_no_audio_files_and_no_network(self):
        self.assertIsNone(re.search(r"\.(mp3|wav|ogg|m4a)\b", SOUND + INTRO))
        self.assertNotIn("fetch(", SOUND + INTRO)
        self.assertNotIn("XMLHttpRequest", SOUND + INTRO)

    def test_every_storage_access_is_guarded(self):
        self.assertGreaterEqual(SOUND.count("try {"), 2)
        self.assertGreaterEqual(INTRO.count("try {"), 3)

    def test_reduced_motion_is_respected(self):
        self.assertIn("prefers-reduced-motion", INTRO)
        self.assertIn("prefers-reduced-motion", CSS)

    def test_the_map_is_inert_while_the_welcome_screen_is_up(self):
        self.assertIn("'inert'", INTRO)
        self.assertIn("removeAttribute('inert')", INTRO)

    def test_the_intro_can_be_skipped_and_is_shown_once_per_session(self):
        self.assertIn("introSkip", INTRO)
        self.assertIn("sessionStorage", HEAD)
        self.assertIn("intro=0", HEAD)

    def test_no_emoji(self):
        for text in (INTRO, SOUND, CSS):
            self.assertIsNone(re.search("[\U0001F300-\U0001FAFF☀-➿]", text))


if __name__ == "__main__":
    unittest.main()
