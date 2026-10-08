"""assets/css/tokens.css defines the design tokens; the hub must load it instead of inlining them."""
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
BLOCKS = ('^\\s*:root\\s*\\{', '^\\s*\\[data-theme="dark"\\]\\s*\\{', '^\\s*\\[data-theme="light"\\]\\s*\\{')


def token_blocks(css):
    """Map selector -> {--token: normalized value} for the three token blocks."""
    result = {}
    for pattern in BLOCKS:
        m = re.search(pattern + r"(.*?)\n\s*\}", css, re.S | re.M)
        if not m:
            continue
        selector = re.sub(r"\s*\{$", "", m.group(0).split("{")[0].strip())
        pairs = re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", m.group(1))
        result[selector] = {k: re.sub(r"\s+", " ", v.strip()) for k, v in pairs}
    return result


class TokensTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokens = (REPO / "assets/css/tokens.css")
        cls.index = (REPO / "index.html")

    def test_tokens_file_exists(self):
        self.assertTrue(self.tokens.is_file(), "assets/css/tokens.css is missing")

    def test_defines_root_dark_and_light_blocks(self):
        blocks = token_blocks(self.tokens.read_text(encoding="utf-8"))
        self.assertEqual(sorted(blocks), [':root', '[data-theme="dark"]', '[data-theme="light"]'])

    def test_hub_uses_shared_assets_instead_of_inline_tokens_and_theme_code(self):
        text = self.index.read_text(encoding="utf-8")
        self.assertIn('href="assets/css/tokens.css"', text)
        self.assertIn('src="assets/js/theme.js"', text)
        self.assertLess(len(token_blocks(text)), 3, "index.html must not redefine the design tokens")
        self.assertNotIn("localStorage", text, "theme storage belongs to assets/js/theme.js")

    def test_core_brand_tokens_are_present(self):
        blocks = token_blocks(self.tokens.read_text(encoding="utf-8"))
        root = blocks[":root"]
        for name in ("--font-display", "--font-body", "--font-mono", "--accent-fluid", "--accent-materials",
                     "--accent-mechanics", "--accent-maths", "--accent-business", "--max-width"):
            self.assertIn(name, root)
        for theme in ('[data-theme="dark"]', '[data-theme="light"]'):
            for name in ("--bg-primary", "--text-primary", "--border-card", "--shadow-card"):
                self.assertIn(name, blocks[theme])
        self.assertIn("Abril Fatface", root["--font-display"])


if __name__ == "__main__":
    unittest.main()
