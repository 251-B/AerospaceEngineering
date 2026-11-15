"""Tests for tools/derivation.py (derivation boxes and the no-inline-calc gate)."""
import pathlib
import sys
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import derivation as d  # noqa: E402

GOOD = r"""> [!derivation] Velocity of the particle
> **Law:** definition of velocity
> **Source:** Notes.pdf, Eq. 2.6; [Lecture 1, Slide 14]
>
> $$\begin{aligned}
> \mathbf v &= \frac{d}{dt}(R\,\mathbf e_r) \quad &\text{(definition)} \\
> &= R\,\dot\theta\,\mathbf e_\theta \quad &\text{(chain rule)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v = R\,\dot\theta\,\mathbf e_\theta}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** tangent to the circle."""


def parse(text):
    block, _ = d.take(text.split("\n"), 0)
    return d.parse(block)


class ParseTests(unittest.TestCase):
    def test_valid_box_parses_and_renders(self):
        box, errors = parse(GOOD)
        self.assertEqual(errors, [])
        self.assertEqual(box["title"], "Velocity of the particle")
        html_ = d.render(box, lambda t: t)
        self.assertIn('<div class="derivation-box">', html_)
        self.assertIn("derivation-result", html_)
        self.assertIn("derivation-steps", html_)
        self.assertIn("<strong>Units:</strong>", html_)

    def errors(self, text):
        return parse(text)[1]

    def test_missing_title(self):
        self.assertTrue(any("title" in e for e in self.errors(GOOD.replace("Velocity of the particle", ""))))

    def test_missing_law(self):
        self.assertTrue(any("Law" in e for e in self.errors(GOOD.replace("> **Law:** definition of velocity\n", ""))))

    def test_source_without_citation(self):
        self.assertTrue(any("citation" in e for e in self.errors(GOOD.replace("Notes.pdf, Eq. 2.6; [Lecture 1, Slide 14]", "the book"))))

    def test_missing_units_and_meaning(self):
        self.assertTrue(any("Units" in e for e in self.errors(GOOD.replace("> **Units:** $[\\mathrm{L\\,T^{-1}}]$\n", ""))))
        self.assertTrue(any("Meaning" in e for e in self.errors(GOOD.replace("> **Meaning:** tangent to the circle.", ""))))

    def test_no_display_formula(self):
        text = "\n".join(l for l in GOOD.split("\n") if "$$" not in l and "mathbf v" not in l and "aligned" not in l and "&=" not in l)
        self.assertTrue(any("no $$" in e for e in self.errors(text)))

    def test_no_boxed_result(self):
        self.assertTrue(any("boxed" in e for e in self.errors(GOOD.replace("\\boxed", ""))))

    def test_aligned_row_without_reason(self):
        self.assertTrue(any("reason" in e for e in self.errors(GOOD.replace("&\\text{(chain rule)}", "").replace("\\quad &\\text{(chain rule)}", ""))))


class GateTests(unittest.TestCase):
    def test_calculations_in_prose_fail(self):
        for frag in ("<p>so $a = b$ here</p>", r"<p>the rate $\dot{\theta}$ grows</p>", r"<li>$\omega\times r$</li>",
                     r"<p>$\frac{a}{b}$</p>", r"<p>$\int x\,dx$</p>", r"<p>$\ddot x$</p>"):
            with self.subTest(frag=frag):
                self.assertTrue(d.gate(frag))

    def test_display_formula_outside_a_box_fails(self):
        self.assertTrue(d.gate('<div class="math-block">$$ a $$</div>'))
        self.assertTrue(d.gate("<p>text $$a+b$$</p>"))

    def test_atomic_identifiers_pass(self):
        frag = (r"<p>The mass $m$ and angle $\theta$ locate $\mathbf r_0^P$ in $S_1$; "
                r"$\odot$ and $\cdot$ and $\dots$ mark the view.</p><ul><li>$\mathbf e_t$</li></ul>")
        self.assertEqual(d.gate(frag), [])

    def test_same_calculations_inside_a_box_pass(self):
        box, _ = parse(GOOD)
        frag = d.render(box, lambda t: t) + "<p>The result uses $m$.</p>"
        self.assertEqual(d.gate(frag), [])

    def test_maths_in_table_cells_pass(self):
        self.assertEqual(d.gate(r"<table><tr><td>$a = b$</td><td>$\dot x$</td></tr></table>"), [])


if __name__ == "__main__":
    unittest.main()
