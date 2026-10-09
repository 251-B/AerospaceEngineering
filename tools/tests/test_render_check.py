"""Tests for tools/render_check.py. The browser test uses static markup, so it needs no network."""
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import render_check as rc  # noqa: E402


class AnalyseDomTests(unittest.TestCase):
    def test_counts_formulas_and_display(self):
        dom = '<span class="katex">a</span><span class="katex">b</span><div class="katex-display"></div>'
        r = rc.analyse_dom("x.html", dom)
        self.assertEqual((r.formulas, r.display, r.errors, r.leftover), (2, 1, [], 0))

    def test_reports_katex_errors(self):
        dom = '<span class="katex-error" title="ParseError: bad \\foo" style="c">x</span>'
        r = rc.analyse_dom("x.html", dom)
        self.assertEqual(len(r.errors), 1)
        self.assertIn("ParseError", r.errors[0])
        self.assertFalse(r.ok)

    def test_leftover_display_delimiters_fail_but_scripts_are_ignored(self):
        self.assertEqual(rc.analyse_dom("x", "<p>$$ x $$</p>" + "a" * 2000).leftover, 2)
        self.assertEqual(rc.analyse_dom("x", "<script>var s='$$';</script>" + "a" * 2000).leftover, 0)

    def test_empty_dom_is_not_ok(self):
        self.assertFalse(rc.analyse_dom("x", "").ok)


@unittest.skipUnless(rc.find_browser(), "no Chromium-based browser available")
class BrowserTests(unittest.TestCase):
    def _run(self, body):
        with tempfile.TemporaryDirectory() as d:
            page = pathlib.Path(d) / "p.html"
            page.write_text(f"<!doctype html><meta charset=utf-8><body>{body}</body>", encoding="utf-8")
            return rc.check([page], rc.find_browser(), repo=pathlib.Path(d))[0]

    def test_clean_page(self):
        r = self._run('<span class="katex">x</span>' + "<p>text</p>" * 300)
        self.assertTrue(r.ok, r)

    def test_page_with_error_is_flagged(self):
        r = self._run('<span class="katex-error" title="ParseError: x">y</span>' + "<p>t</p>" * 300)
        self.assertFalse(r.ok)
        self.assertEqual(len(r.errors), 1)


if __name__ == "__main__":
    unittest.main()
