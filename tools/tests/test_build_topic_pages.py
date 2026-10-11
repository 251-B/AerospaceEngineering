"""Tests for tools/build_topic_pages.py (theory pages generated from vault notes) and tools/figures/."""
import pathlib
import subprocess
import sys
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


class RepositoryTests(unittest.TestCase):
    def test_generated_pages_and_figures_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(TOOLS / "build_topic_pages.py"), "--check"],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)


if __name__ == "__main__":
    unittest.main()
