"""Tests for tools/build_topic_pages.py (theory pages generated from vault notes) and tools/figures/."""
import pathlib
import re
import subprocess
import sys
import tempfile
import types
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_topic_pages as bt  # noqa: E402
from figures import materials_t2, svgkit  # noqa: E402


class MarkdownTests(unittest.TestCase):
    def test_math_is_kept_verbatim_and_bold_may_contain_math(self):
        out = bt.inline("**minimum at $a_0$** and $x<y$ & **b**")
        self.assertEqual(out, "<strong>minimum at $a_0$</strong> and $x&lt;y$ &amp; <strong>b</strong>")

    def test_wikilinks_become_plain_text(self):
        self.assertEqual(bt.inline("see [[Note|the note]] and [[Other]]"), "see the note and Other")

    def test_table_list_callout_and_display_math(self):
        md = ["| A | B |", "| :--- | ---: |", "| 1 | 2 |", "", "- one", "- two", "",
              "> [!warning] Careful", "> body $x$", "", "$$ E = mc^2 $$"]
        out = bt.blocks(md)
        self.assertIn('<th>A</th><th style="text-align:right">B</th>', out)
        self.assertIn("<ul><li>one</li><li>two</li></ul>", out)
        self.assertIn('<div class="callout callout-warning"><div class="callout-title">Careful</div><p>body $x$</p></div>', out)
        self.assertIn('<div class="math-block">$$ E = mc^2 $$</div>', out)

    def test_figure_embed_calls_the_figure_renderer(self):
        out = bt.blocks(["text", "", "![[attachments/T9/cube.svg]]"], figure=lambda n: f"<fig {n}>")
        self.assertEqual(out, "<p>text</p>\n<fig cube>")

    def test_figure_embed_without_module_is_an_error(self):
        with self.assertRaises(ValueError):
            bt.blocks(["![[attachments/T9/cube.svg]]"])


class FigureTests(unittest.TestCase):
    def test_plane_polygons_include_vertices_on_the_plane(self):
        poly, o = materials_t2.plane_poly(1, 0, 0)
        self.assertEqual(len(poly), 4)                      # the whole x = 1 face
        poly, o = materials_t2.plane_poly(1, -1, -1)
        self.assertEqual(o, (0, 1, 1))
        self.assertEqual(sorted(poly), sorted([(0, 0, 1), (0, 1, 0), (1, 1, 1)]))

    def test_registry_writes_fixed_colours_and_keeps_css_variables_for_the_web(self):
        reg = svgkit.Registry("T9")
        c = svgkit.Canvas(10, 10)
        svgkit.line(c, (0, 0), (5, 5), "ACC")
        reg.put("x", c, "A line")
        self.assertIn('stroke="#f59e0b"', reg.files["vault/attachments/T9/x.svg"])
        self.assertIn('fill="var(--text-faint)"', reg.web["x"])


BOX = """> [!derivation] Velocity of the particle
> **Law:** definition of velocity; time derivative taken in $S_0$
> **Source:** Notes.pdf, Eq. 3.8; [Lecture 1, Slide 14]
>
> $$\\begin{aligned}
> \\mathbf v_0^P &= \\frac{d}{dt}\\left(R\\,\\mathbf e_r\\right) \\quad &\\text{(definition of velocity)} \\\\
> &= R\\,\\dot\\theta\\,\\mathbf e_\\theta \\quad &\\text{(chain rule)}
> \\end{aligned}$$
>
> $$\\boxed{\\mathbf v_0^P = R\\,\\dot\\theta\\,\\mathbf e_\\theta}$$
>
> ![[attachments/EMT/demo.svg]]
>
> **Units:** $[\\mathrm{L\\,T^{-1}}]$
> **Meaning:** the velocity is tangent to the circle.
"""
NOTE = """---
title: fixture
---
# Topic 9 - Fixture

> The central idea names $P$ and $S_0$ only.

## 1. First section

A paragraph about $\\mathbf r_0^P$.

### 1.1 Definitions

| Symbol | Meaning |
| :--- | :--- |
| $\\theta$ | angle |

- an item on $m$

> [!info] Extension
> beyond the course

> [!example] A worked example
> text

""" + BOX + """
**Back to:** [[MOC]]
"""


class MechanicsFlavorTests(unittest.TestCase):
    PAGE = "subjects/engineering-mechanics/teoria/topic-9.html"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        fake = types.SimpleNamespace(
            web={"demo": "<svg viewBox='0 0 10 10'></svg>"}, captions={"demo": "A demo"},
            build=lambda: fake, write=lambda root: [], stale=lambda root: [])
        sys.modules["figures.em_fixture"] = fake
        self.addCleanup(sys.modules.pop, "figures.em_fixture", None)

    def build(self, note_text, figures="em_fixture"):
        note = pathlib.Path(self.tmp.name, "Topic 9 - Fixture.md")
        note.write_text(note_text, encoding="utf-8")
        spec = {"flavor": "mechanics", "template": "subjects/engineering-mechanics/teoria/topic-5.html", "note": str(note),
                "figures": figures, "html_title": "Topic 9: Fixture", "category": "Cat", "title": "Fixture",
                "subtitle": "Sub", "source": "Sources: [Lecture 7, Slide 12]",
                "nav": [["topic-8.html", "Topic 8", "prev"], ["../problemas/topic-9.html", "Topic 9 Problems", "center"],
                        ["index.html", "Index", "next"]]}
        return bt.build_page(self.PAGE, spec, {"pages": {}}, {})

    def test_valid_note_builds_a_complete_page(self):
        page, _ = self.build(NOTE)
        for needle in ('<div class="derivation-box">', "assets/css/derivation-box.css", "assets/js/ask-ai.js",
                       "assets/js/pdf-export.js", 'href="../../../index.html"', 'id="themeToggle"',
                       'id="sec-1"', 'class="callout callout-info callout-extension"', "example-card", "Figure 1. A demo",
                       'class="table-wrapper"'):
            self.assertIn(needle, page)
        self.assertLess(page.index("<svg viewBox='0 0 10 10'>"), page.index("Units:"))  # figure inside the box
        for banned in ("pill-nav-bar", "subchapter-nav-bar", "pills-bar", "quick-jump", "quick-nav"):
            self.assertNotIn(banned, page)
        links = re.findall(r'<link rel="stylesheet" href="([^"]*\.css)"', page)
        self.assertTrue(links[-1].endswith("responsive.css"), links)
        self.assertLess(links.index("../../../assets/css/study-surface.css"), links.index("../../../assets/css/derivation-box.css"))
        self.assertEqual(bt.derivation.gate(page.split("<main")[1].split("article-nav")[0]), [])

    def test_inline_calculation_in_prose_fails(self):
        with self.assertRaises(bt.NoteError) as cm:
            self.build(NOTE.replace("A paragraph about $\\mathbf r_0^P$.", "A paragraph with $v = R\\dot\\theta$."))
        self.assertTrue(any("no-inline-calc" in m for m in cm.exception.messages), cm.exception.messages)

    def test_display_formula_outside_a_box_fails(self):
        with self.assertRaises(bt.NoteError) as cm:
            self.build(NOTE.replace("- an item on $m$", "$$x = y$$"))
        self.assertTrue(any("no-inline-calc" in m for m in cm.exception.messages))

    def test_invalid_box_fails(self):
        bad = NOTE.replace("> **Meaning:** the velocity is tangent to the circle.\n", "")
        with self.assertRaises(bt.NoteError) as cm:
            self.build(bad)
        self.assertTrue(any("Meaning" in m for m in cm.exception.messages), cm.exception.messages)

    def test_figure_in_a_box_needs_a_module(self):
        with self.assertRaises(bt.NoteError):
            self.build(NOTE, figures=None)

    def test_source_citations_are_linked_in_the_derivation_source(self):
        import json
        cfg = json.loads(bt.sl.CONFIG.read_text(encoding="utf-8"))
        cfg["pages"][self.PAGE] = {"cite": {"notes": "em-notes"}}
        note = pathlib.Path(self.tmp.name, "n.md")
        note.write_text(NOTE, encoding="utf-8")
        spec = {"flavor": "mechanics", "template": "subjects/engineering-mechanics/teoria/topic-5.html", "note": str(note),
                "figures": "em_fixture", "html_title": "t", "category": "c", "title": "t", "subtitle": "s",
                "nav": [["index.html", "Index", "next"]]}
        page, _ = bt.build_page(self.PAGE, spec, cfg, bt.sl.load_json(bt.sl.ANCHORS, {}))
        src = re.search(r'<span class="derivation-source">.*?</span>', page, re.S).group(0)
        self.assertIn("Notes.pdf#page=", src)
        self.assertIn("01_-_Point_particle_kinematics.pdf#page=14", src)
        links = re.findall(r'<link rel="stylesheet" href="([^"]*\.css)"', page)
        self.assertTrue(links[-1].endswith("responsive.css"), links)


class RepositoryTests(unittest.TestCase):
    def test_generated_pages_and_figures_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(TOOLS / "build_topic_pages.py"), "--check"],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)


if __name__ == "__main__":
    unittest.main()
