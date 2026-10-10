"""Tests for tools/source_links.py (deep links from study pages to the official PDFs)."""
import pathlib
import subprocess
import sys
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import source_links as sl  # noqa: E402

PAGE = "subjects/x/teoria/topic-1.html"
PDFS = {
    "slides": {"path": "sources/cuatrimestre-1/x/Session 2 T1.pdf", "label": "Session 2 T1.pdf", "pages": 40},
    "s4": {"path": "sources/cuatrimestre-1/x/Session 4.pdf", "label": "Session 4.pdf", "pages": 50},
    "book": {"path": "sources/cuatrimestre-1/x/Book's.pdf", "label": "Book", "pages": 400, "offset": 16},
    "notes": {"path": "sources/cuatrimestre-1/x/Notes.pdf", "label": "Notes.pdf", "pages": 190},
}
ANCHORS = {"book": {"sec:7.6": 70, "eq:9.8": 93}, "notes": {"eq:2.26": 23}}


def link(html, **rules):
    linker = sl.Linker(PAGE, rules, PDFS, ANCHORS)
    return sl.link_citations("<html><head></head><body>" + html + "</body></html>", linker), linker


def pages_in(text):
    import re
    return re.findall(r'#page=(\d+)"[^>]*>([^<]*)</a>', text)


class CitationTests(unittest.TestCase):
    def test_bracketed_slide_list_links_each_number(self):
        out, _ = link("<p>Ionic bonds [Slides 5, 14–16].</p>", slides="slides")
        self.assertEqual(pages_in(out), [("5", "5"), ("14", "14–16")])
        self.assertIn("Session%202%20T1.pdf", out)

    def test_session_prefix_selects_that_deck(self):
        out, _ = link("<p>[Session 4 Slide 22]</p>", sessions={"4": "s4"})
        self.assertIn("Session%204.pdf#page=22", out)

    def test_slide_beyond_the_deck_is_left_alone(self):
        out, linker = link("<p>(Slide 99)</p>", slides="slides")
        self.assertNotIn("<a", out.split("<body>")[1])
        self.assertEqual(linker.unresolved, ["slides slide:99"])

    def test_robinson_chain_resolves_sections_and_printed_pages(self):
        out, _ = link("<p>[Robinson, Sec. 7.6, p. 54]</p>", robinson="book")
        self.assertEqual(pages_in(out), [("70", "7.6"), ("70", "54")])
        self.assertIn("Book%27s.pdf", out)

    def test_notes_equation_in_either_order(self):
        out, _ = link("<p>(Notes.pdf, Eq. 2.26) and Eq. 2.26 of Notes.pdf</p>", notes="notes")
        self.assertEqual(pages_in(out), [("23", "2.26"), ("23", "2.26")])

    def test_bare_equation_needs_the_page_opt_in(self):
        out, _ = link("<p>by Eq. 2.26</p>", notes="notes")
        self.assertEqual(pages_in(out), [])
        out, _ = link("<p>by Eq. 2.26</p>", notes="notes", bare_eq="notes")
        self.assertEqual(pages_in(out), [("23", "2.26")])

    def test_math_code_and_existing_links_are_never_touched(self):
        src = ("<p>$$x \\text{(Robinson p. 78)}$$ and $[Slide 3]$</p><code>[Slide 3]</code>"
               '<a href="#">[Slide 3]</a>')
        out, _ = link(src, slides="slides", robinson="book")
        self.assertNotIn("src-cite", out)

    def test_strip_restores_the_original_exactly(self):
        src = "<p>See [Slide 4] and (Robinson p. 47).</p>"
        out, _ = link(src, slides="slides", robinson="book")
        self.assertNotEqual(out, src)
        self.assertEqual(sl.strip_links(out), "<html><head></head><body>" + src + "</body></html>")


class CardAndPanelTests(unittest.TestCase):
    PAGE_HTML = ('<html><head>\n</head><body>\n  <main>\n    <header class="article-header">\n'
                 '      <h1>T</h1>\n    </header>\n'
                 '    <article class="problem-card" id="p1">\n      <h2 class="problem-title">A</h2>\n    </article>\n'
                 '    <details class="problem-card" id="p2"><summary><h2>B</h2></summary>\n      <p>x</p></details>\n'
                 '  </main>\n</body></html>')

    def build(self, cards):
        cfg = {"pdfs": PDFS, "pages": {PAGE: {"panel": [["notes", 18, "Notes, Ch. 2"]], "cards": cards}}}
        report = {}
        return sl.build_page(PAGE, self.PAGE_HTML, cfg, ANCHORS, report), report[PAGE]

    def test_cards_get_a_link_after_the_title_or_summary(self):
        out, rep = self.build({"p1": ["notes", 3], "p2": ["s4", 1]})
        self.assertEqual(rep["missing_cards"], [])
        self.assertIn('</h2>\n      <a class="src-link" data-srclink href="../../../sources/cuatrimestre-1/x/Notes.pdf#page=3"', out)
        self.assertIn('</summary>\n', out)
        self.assertRegex(out, r'</summary>\s*<a class="src-link"[^>]*Session%204\.pdf"')

    def test_panel_and_stylesheet_are_added_and_rebuild_is_idempotent(self):
        out, _ = self.build({"p1": ["notes", 3], "p2": ["s4", 1]})
        self.assertIn('<nav class="src-panel" data-srclink', out)
        self.assertIn('Notes, Ch. 2 · p. 18', out)
        self.assertIn('href="../../../assets/css/source-links.css" data-srclink', out)
        self.assertEqual(sl.strip_links(out), self.PAGE_HTML)
        cfg = {"pdfs": PDFS, "pages": {PAGE: {"panel": [["notes", 18, "Notes, Ch. 2"]],
                                              "cards": {"p1": ["notes", 3], "p2": ["s4", 1]}}}}
        self.assertEqual(sl.build_page(PAGE, out, cfg, ANCHORS, {}), out)

    def test_unconfigured_card_is_reported(self):
        _, rep = self.build({"p1": ["notes", 3]})
        self.assertEqual(rep["missing_cards"], ["p2"])


class RepositoryTests(unittest.TestCase):
    def test_portal_pages_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(TOOLS / "source_links.py"), "--check"],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)


if __name__ == "__main__":
    unittest.main()
