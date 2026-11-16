"""Tests for tools/build_mech_problems.py (Engineering Mechanics official problem pages from the vault notes)."""
import json
import pathlib
import re
import shutil
import sys
import tempfile
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

    def v3(self, body):
        errors = []
        g.validate_v3("99", g.split_sections(body), body, errors)
        return errors

    def test_structure_3_follows_the_lecturers_order(self):
        good = ("### Reference Frames, Bases and Coordinates\n* x\n### Change of Basis and Position Vector\n* x\n"
                "### Kinematics\n* x\n### Forces and Equations of Motion\n* x\n### Answers and Checks\n"
                "* Check against the official key: same.\n")
        self.assertEqual(self.v3(good), [])
        no_forces = good.replace("### Forces and Equations of Motion\n* x\n", "")
        self.assertEqual(self.v3(no_forces), [])
        swapped = good.replace("### Kinematics", "### Tmp").replace("### Change of Basis and Position Vector", "### Kinematics") \
            .replace("### Tmp", "### Change of Basis and Position Vector")
        self.assertTrue(any("expected" in e for e in self.v3(swapped)))
        self.assertTrue(any("official key" in e for e in self.v3(good.replace("Check against the official key", "Key"))))
        self.assertTrue(any("'Phase'" in e for e in self.v3(good.replace("* x", "* Phase 2 recap", 1))))

    def test_solution_figures_become_numbered_diagram_cards(self):
        errors = []
        g.emsol.build()
        name = next(iter(g.emsol.REG.web), None)
        if name is None:
            self.skipTest("no solution figure drawn yet")
        figs = g.Figures("99", errors)
        out = g.render_solution(f"* a\n\n![[attachments/EM-SOL/{name}.svg]]\n\n* b", figs)
        self.assertIn('class="diagram-card"', out)
        self.assertIn("Figure 1.", out)
        self.assertEqual(errors, [])
        g.render_solution("![[attachments/EM-SOL/no-such-figure.svg]]", figs)
        self.assertTrue(any("unknown figure" in e for e in errors))


class RepositoryTests(unittest.TestCase):
    def test_pages_are_up_to_date_with_their_notes(self):
        self.assertEqual(g.main(["--check"]), 0)

    def test_metadata_covers_the_51_official_particle_problems_once(self):
        meta = g.load_meta()
        particle = {k: v for k, v in meta.items() if not k.startswith("rb-")}
        self.assertEqual(sorted(particle), [f"{i:02d}" for i in range(1, 52)])
        for topic in range(1, 6):
            self.assertEqual(sum(1 for v in particle.values() if v["topic"] == topic), g.EXPECTED[topic])
        for k, v in meta.items():
            if v.get("structure", 1) == 3:
                # a rewritten solution drops the key and is gated; one still waiting keeps "boxed": false
                self.assertIn(v.get("boxed"), (None, False))
            if v.get("structure", 1) == 4:
                self.assertNotIn("boxed", v)

    def test_every_card_has_its_sections_no_phase_label_and_no_pdf_links_in_the_generated_text(self):
        total = 0
        meta = g.load_meta()
        for topic in range(1, 6):
            page = sl.strip_links((g.SUBJECT / f"topic-{topic}.html").read_text(encoding="utf-8"))
            cards = re.split(r'<div class="problem-card"', page)[1:]
            total += len(cards)
            for c in cards:
                pid = re.search(r'id="prob-(\d+)"', c).group(1)
                self.assertIn(pid, meta)
                n = c.count('class="phase-block"')
                self.assertIn(n, (4, 5) if meta[pid].get("structure", 1) >= 3 else (4,))
                self.assertIn(pid, meta)
                self.assertNotIn("phase-badge", c)
                self.assertNotRegex(c[:c.find('class="problem-footer"')], r">\s*Phase \d")
                self.assertIn("<details class=\"solution-details\">", c)
                self.assertIn('class="problem-footer"', c)
        self.assertEqual(total, 51)

    def test_derivation_css_is_linked_and_responsive_css_stays_last(self):
        for topic in range(1, 6):
            text = (g.SUBJECT / f"topic-{topic}.html").read_text(encoding="utf-8")
            head = text[:text.index("</head>")]
            self.assertEqual(head.count("derivation-box.css"), 1)
            local = [l for l in re.findall(r'<link rel="stylesheet" href="([^"]+)"', head)
                     if l.startswith("../../../assets/css/") and "source-links" not in l]
            self.assertTrue(local[-1].endswith("responsive.css"), local)

    def test_no_emoji_in_the_generated_cards(self):
        for topic in range(1, 6):
            text = (g.SUBJECT / f"topic-{topic}.html").read_text(encoding="utf-8")
            start = text.index('<div class="problem-card"')
            end = text.index('<div class="article-nav">')
            self.assertIsNone(g.EMOJI.search(text[start:end]))


BOX = r"""> [!derivation] Step
> **Law:** definition
> **Source:** Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> a &= b \quad &\text{(why)}
> \end{aligned}$$
>
> $$\boxed{a = b}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** equal."""
V4 = "\n".join(f"### {h}\n{('Does not apply to this problem.' if i == 2 else 'Frames $S_0$ and $S_1$.')}" for i, h in enumerate(g.STEPS_V4))
V4 = V4.replace("Frames $S_0$ and $S_1$.", "Text.", 5) + "\nLimiting cases: none."


class Structure4Tests(unittest.TestCase):
    def v4(self, body):
        errors = []
        g.validate_v4("rb-01", g.split_sections(body), body, errors)
        return errors

    def test_valid_with_a_section_that_does_not_apply(self):
        self.assertEqual(self.v4(V4), [])

    def test_order_and_missing_section(self):
        self.assertTrue(self.v4(V4.replace("### Center of Mass and Inertia Tensor\nDoes not apply to this problem.\n", "")))
        a, b = g.STEPS_V4[0], g.STEPS_V4[1]
        swapped = V4.replace(a, "TMP").replace(b, a).replace("TMP", b)
        self.assertTrue(any("expected" in e for e in self.v4(swapped)))

    def test_answers_need_key_or_limiting_cases_and_no_phase(self):
        self.assertTrue(any("Limiting" in e for e in self.v4(V4.replace("Limiting cases: none.", "nothing"))))
        self.assertEqual(self.v4(V4.replace("Limiting cases: none.", "Check against the official key: same.")), [])
        self.assertTrue(any("'Phase'" in e for e in self.v4(V4.replace("Text.", "Phase 1 recap", 1))))

    def test_empty_section_is_rejected(self):
        self.assertTrue(any("empty" in e for e in self.v4(V4.replace("Does not apply to this problem.", ""))))


class GateAndBoxTests(unittest.TestCase):
    def card(self, meta, sol):
        errors = []
        meta = dict({"topic": 5, "title": "T", "badge": "B", "source_note": ""}, **meta)
        with tempfile.TemporaryDirectory() as tmp:
            old = g.FIG_DIR
            g.FIG_DIR = pathlib.Path(tmp)
            try:
                html_ = g.card_html("99", meta, "Statement with $a = b$.", sol, errors)
            finally:
                g.FIG_DIR = old
        return html_, errors

    def v3(self, extra):
        return ("### Reference Frames, Bases and Coordinates\n" + extra + "\n### Change of Basis and Position Vector\nx\n"
                "### Kinematics\nx\n### Answers and Checks\nCheck against the official key: same.\n")

    def test_box_is_rendered_and_passes_the_gate(self):
        html_, errors = self.card({"structure": 3}, self.v3(BOX))
        self.assertEqual(errors, [])
        self.assertIn('<div class="derivation-box">', html_)

    def test_inline_calculation_fails_unless_boxed_false(self):
        sol = self.v3("The speed is $v = R\\omega$.")
        _, errors = self.card({"structure": 3}, sol)
        self.assertTrue(any("no-inline-calc" in e for e in errors))
        _, errors = self.card({"structure": 3, "boxed": False}, sol)
        self.assertEqual(errors, [])

    def test_statement_is_never_gated_and_structure_2_is_not_gated(self):
        _, errors = self.card({"structure": 3}, self.v3(BOX))
        self.assertFalse(any("Statement" in e for e in errors))

    def test_boxed_false_not_allowed_with_structure_4(self):
        _, errors = self.card({"structure": 4, "boxed": False}, V4)
        self.assertTrue(any("not allowed" in e for e in errors))

    def test_bad_box_is_a_validation_error(self):
        _, errors = self.card({"structure": 3, "boxed": False}, self.v3(BOX.replace("**Law:** definition\n> ", "")))
        self.assertTrue(any("Law" in e for e in errors))

    def test_counts(self):
        c = g.problem_counts({"a": {"structure": 2}, "b": {"structure": 3, "boxed": False}, "c": {"structure": 4}})
        self.assertEqual(c, {"structure2": 1, "legacy": 1, "boxed": 1})


class SimulatorTests(unittest.TestCase):
    def sim(self, text):
        figs = g.Figures("99", [])
        return g.render_solution(text, figs), figs.errors

    OK = '> [!example] Interactive simulator\n> sim: {"archetype": "rb-rolling-contact", "params": {"R": 0.5}, "defaults": {}, "readouts": ["R"]}\n> Extra text.'

    def test_valid_simulator(self):
        out, errors = self.sim(self.OK)
        self.assertEqual(errors, [])
        self.assertIn('data-archetype="rb-rolling-contact"', out)
        self.assertIn("&quot;params&quot;:{&quot;R&quot;:0.5}", out)
        self.assertNotIn("archetype&quot;", out)
        self.assertIn("m3-fallback", out)
        self.assertNotIn("Extra text", out)

    def test_invalid_json_unknown_archetype_and_two_simulators(self):
        self.assertTrue(any("invalid simulator JSON" in e for e in self.sim("> [!example] Interactive simulator\n> sim: {bad")[1]))
        self.assertTrue(any("unknown simulator archetype" in e for e in
                            self.sim('> [!example] Interactive simulator\n> sim: {"archetype": "nope"}')[1]))
        self.assertTrue(any("more than one" in e for e in self.sim(self.OK + "\n\n" + self.OK)[1]))


class PageTests(unittest.TestCase):
    """Head assets, extra badges and page creation, on a temporary copy of the notes and pages."""

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.saved = (g.VAULT, g.SUBJECT, g.FIG_DIR)
        g.VAULT, g.SUBJECT, g.FIG_DIR = self.tmp / "vault", self.tmp / "pages", self.tmp / "fig"
        for d in (g.VAULT, g.SUBJECT, g.FIG_DIR):
            d.mkdir()
        shutil.copy(self.saved[1] / "topic-5.html", g.SUBJECT / "topic-5.html")
        self.addCleanup(lambda: setattr_all(self.saved))

    def notes(self, topic, sims=True):
        name = g.SET_NAMES[topic]
        (g.VAULT / f"Problem Set - {name}.md").write_text(
            "## 📌 Problem RB-01: A\n\nText.\n\n* **(a)** Q.\n\n## 📌 Problem RB-02: B\n\nText.\n", encoding="utf-8")
        (g.VAULT / f"Solution Set - {name}.md").write_text(
            f"## Problem RB-01: A\n{V4}\n\n## Problem RB-02: B\n{V4}\n\n" + (SimulatorTests.OK + "\n" if sims else ""), encoding="utf-8")

    def meta(self):
        return {"rb-01": {"topic": 6, "title": "A", "badge": "x", "source_note": "", "structure": 4, "group": "B", "badges": ["In-Class Session 2"]},
                "rb-02": {"topic": 6, "title": "B", "badge": "y", "source_note": "", "structure": 4, "group": "A"}}

    def test_new_page_groups_badges_and_head(self):
        old = g.EXPECTED[6]
        g.EXPECTED[6] = 2
        self.addCleanup(g.EXPECTED.__setitem__, 6, old)
        self.notes(6)
        errors = []
        path, page = g.build_page(6, self.meta(), errors)
        self.assertEqual(errors, [])
        self.assertIn("mechanics-3d-sim.js", page)
        self.assertIn('class="m3-sim"', page)
        self.assertEqual(path.name, "topic-6.html")
        self.assertIn("Kinematics of Rigid Bodies and Inertia Properties", page)
        self.assertLess(page.index('id="group-a"'), page.index('id="group-b"'))
        self.assertLess(page.index('id="rb-02"'), page.index('id="rb-01"'))
        self.assertIn("Problem RB 01", page)
        self.assertEqual(page.count('class="problem-badge"'), 3)
        self.assertIn("topic-5.html", page)
        self.assertIn("derivation-box.css", page)
        self.assertEqual(page.count("derivation-box.css"), 1)

    def test_head_assets_are_idempotent_and_responsive_stays_last(self):
        text = (g.SUBJECT / "topic-5.html").read_text(encoding="utf-8")
        for sim in (False, True):
            once = g.set_head_assets(text, sim, [], 5)
            self.assertEqual(g.set_head_assets(once, sim, [], 5), once)
            head = once[:once.index("</head>")]
            links = re.findall(r'<link rel="stylesheet" href="([^"]+)"', head)
            local = [l for l in links if l.startswith("../../../assets/css/") and "source-links" not in l]
            self.assertTrue(local[-1].endswith("responsive.css"))
            self.assertEqual("mechanics-3d-sim.js" in once, sim)
            self.assertEqual("mechanics-3d-sim.css" in once, sim)
        again = g.set_head_assets(g.set_head_assets(text, True, [], 5), False, [], 5)
        self.assertNotIn("mechanics-3d-sim", again)

    def test_missing_notes_are_skipped(self):
        self.assertFalse(g.notes_exist(6))


def setattr_all(saved):
    g.VAULT, g.SUBJECT, g.FIG_DIR = saved


if __name__ == "__main__":
    unittest.main()
