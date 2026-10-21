"""Tests for tools/build_mech_problems.py (Engineering Mechanics official problem pages from the vault notes)."""
import pathlib
import re
import sys
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_mech_problems as g  # noqa: E402
import source_links as sl  # noqa: E402


def v2_solution(**over):
    """A minimal valid structure-2 solution body (as the 'phases' list used by validate)."""
    subs = "\n".join(f"#### {s}\ntext" for s in g.SUB_V2)
    base = [
        (1, g.PHASES_V2[0], "* x"),
        (2, g.PHASES_V2[1], "* x"),
        (3, g.PHASES_V2[2], subs),
        (4, g.PHASES_V2[3], "* **Check against the official key:** none."),
    ]
    for k, v in over.items():
        base[int(k[1]) - 1] = (int(k[1]), base[int(k[1]) - 1][1], v)
    return base


class RenderTests(unittest.TestCase):
    def test_justification_bullet_becomes_a_box_and_splits_the_list(self):
        out = g.render_solution("* **Label:** a\n* **Pedagogical Justification:** why\n* **Other:** b")
        self.assertEqual(out.count("<ul "), 2)
        self.assertIn('<div class="justification-box"><strong>Pedagogical Justification:</strong> why</div>', out)

    def test_indented_formula_stays_between_the_bullets_in_order(self):
        out = g.render_solution("* first:\n  $$ a = b $$\n* second")
        self.assertLess(out.index("first"), out.index("a = b"))
        self.assertLess(out.index("a = b"), out.index("second"))

    def test_ordered_and_nested_ordered_lists(self):
        out = g.render_solution("1. one\n2. two\n\n* **Hypotheses:**\n  1. h1\n  2. h2")
        self.assertIn("<ol ", out)
        self.assertIn("<ol style=\"margin: 6px 0 6px 20px;\"><li>h1</li><li>h2</li></ol>", out)

    def test_escaped_leading_number_is_a_paragraph(self):
        out = g.render_solution("1\\. not a list item")
        self.assertIn("<p ", out)
        self.assertNotIn("<ol", out)
        self.assertIn("1. not a list item", out)

    def test_table_pipe_inside_math_is_not_a_separator(self):
        out = g.render_solution("| a | b |\n|---|---|\n| $|x|$ | y |")
        self.assertIn("$|x|$", out)
        self.assertEqual(out.count("<td "), 2)

    def test_br_survives_and_angle_brackets_are_escaped(self):
        self.assertEqual(g.inl("a<br>b"), "a<br>b")
        self.assertIn("&lt;", g.inl("$x<y$"))

    def test_headings_and_callouts(self):
        out = g.render_solution("#### 3.1 Kinematics\n##### (a) part\n> [!warning] Erratum\n> first\n>\n> second")
        self.assertIn("<h4 ", out)
        self.assertIn("<h5 ", out)
        self.assertEqual(out.count("<p "), 2)
        self.assertIn("<strong>Erratum</strong>", out)

    def test_statement_keeps_text_and_questions_interleaved(self):
        md = "Intro.\n\n* **(a)** First.\n\nMiddle text.\n\n* **(b)** Second.\n"
        html_, fig = g.render_statement(md, "99", [])
        self.assertIsNone(fig)
        order = [html_.index(s) for s in ("Intro.", "First.", "Middle text.", "Second.")]
        self.assertEqual(order, sorted(order))
        self.assertEqual(html_.count('class="questions-list"'), 2)
        self.assertEqual(html_.count('class="problem-statement"'), 2)

    def test_statement_figure_needs_its_caption(self):
        errors = []
        g.render_statement("![[attachments/EM/T1-P01-figure.png]]\n", "01", errors)
        self.assertTrue(errors)
        errors = []
        h, fig = g.render_statement(
            "![[attachments/EM/T1-P01-figure.png]]\n*Figure: A drawing. Source: Problems.pdf, p. 6.*\n", "01", errors)
        self.assertEqual(errors, [])
        self.assertEqual(fig, "T1-P01-figure.png")
        self.assertIn("(Problems.pdf, p. 6)", h)

    def test_taken_from_line_is_dropped(self):
        html_, _ = g.render_statement("Text.\n\n*(Taken from MIT OCW)*\n", "01", [])
        self.assertNotIn("MIT", html_)


class ValidateTests(unittest.TestCase):
    def check(self, phases, structure=2):
        errors = []
        g.validate("99", phases, structure, errors)
        return errors

    def test_valid_structure_2_passes(self):
        self.assertEqual(self.check(v2_solution()), [])

    def test_structure_1_only_needs_four_phases(self):
        self.assertEqual(self.check([(1, "A", ""), (2, "B", ""), (3, "C", ""), (4, "D", "")], structure=1), [])
        self.assertTrue(self.check([(1, "A", ""), (2, "B", "")], structure=1))

    def test_structure_2_requires_headings_substructure_and_official_key(self):
        bad = v2_solution(p3="#### 3.1 Kinematics\n#### 3.3 Equations of Motion\n#### 3.2 Forces\n#### 3.4 Integration and Answers")
        self.assertTrue(any("out of order" in e for e in self.check(bad)))
        bad = v2_solution(p3="#### 3.1 Kinematics")
        self.assertTrue(any("lacks the sub-heading" in e for e in self.check(bad)))
        bad = v2_solution(p4="* nothing")
        self.assertTrue(any("official key" in e for e in self.check(bad)))
        phases = v2_solution()
        phases[0] = (1, "Wrong heading", "* x")
        self.assertTrue(any("heading is" in e for e in self.check(phases)))


class RepositoryTests(unittest.TestCase):
    def test_pages_are_up_to_date_with_their_notes(self):
        self.assertEqual(g.main(["--check"]), 0)

    def test_metadata_covers_the_51_official_particle_problems_once(self):
        meta = g.load_meta()
        self.assertEqual(sorted(meta), [f"{i:02d}" for i in range(1, 52)])
        for topic, n in g.EXPECTED.items():
            self.assertEqual(sum(1 for v in meta.values() if v["topic"] == topic), n)

    def test_every_card_has_four_phases_and_the_pdf_links_are_not_in_the_generated_text(self):
        total = 0
        for topic in g.EXPECTED:
            page = sl.strip_links((g.SUBJECT / f"topic-{topic}.html").read_text(encoding="utf-8"))
            cards = re.split(r'<div class="problem-card"', page)[1:]
            total += len(cards)
            for c in cards:
                self.assertEqual(c.count('class="phase-block"'), 4)
                self.assertIn("<details class=\"solution-details\">", c)
                self.assertIn('class="problem-footer"', c)
        self.assertEqual(total, 51)

    def test_no_emoji_in_the_generated_cards(self):
        for topic in g.EXPECTED:
            text = (g.SUBJECT / f"topic-{topic}.html").read_text(encoding="utf-8")
            start = text.index('<div class="problem-card"')
            end = text.index('<div class="article-nav">')
            self.assertIsNone(g.EMOJI.search(text[start:end]))


if __name__ == "__main__":
    unittest.main()
