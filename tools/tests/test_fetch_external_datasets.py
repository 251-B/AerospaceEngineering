"""Offline unit tests for tools/ai_training/fetch_external_datasets.py."""
import json
import pathlib
import sys
import tempfile
import unittest
import zipfile

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/ai_training"))

import fetch_external_datasets as fed  # noqa: E402


class FetchExternalDatasetsTests(unittest.TestCase):
    def test_normalise_external_latex_delimiters_and_row_breaks(self):
        raw = (
            r"Compute \(v = \sqrt{2gh}\) using "
            r"\[E = \frac{1}{2}mv^2 + mgh\] "
            r"and \begin{equation*}a \\[5pt] b\end{equation*}."
        )
        out = fed.normalise_external_latex(raw)
        self.assertIn("$v = \\sqrt{2gh}$", out)
        self.assertIn("$$\nE = \\frac{1}{2}mv^2 + mgh\n$$", out)
        self.assertIn("$$\na \\\\[5pt] b\n$$", out)
        self.assertNotIn(r"\(", out)
        self.assertNotRegex(out, r"(?<!\\)\\\[")
        self.assertNotIn(r"\begin{equation", out)

    def test_subject_routing_accepts_all_five_and_rejects_off_topic(self):
        self.assertEqual(
            fed.route_subject("camel-physics", {"topic;": "Fluid mechanics", "sub_topic": "Bernoulli equation"}),
            "fluid-mechanics",
        )
        self.assertEqual(
            fed.route_subject("camel-physics", {"topic;": "Classical mechanics", "sub_topic": "Rigid body kinematics"}),
            "engineering-mechanics",
        )
        self.assertEqual(
            fed.route_subject("camel-physics", {"topic;": "Condensed matter", "sub_topic": "Stress-strain elasticity"}),
            "aerospace-materials-1",
        )
        self.assertIsNone(
            fed.route_subject("camel-physics", {"topic;": "Quantum mechanics", "sub_topic": "Schrodinger equation"}),
        )
        self.assertEqual(
            fed.route_subject("camel-math", {"topic;": "Differential equations", "sub_topic": "Laplace transform"}),
            "advanced-maths",
        )
        self.assertIsNone(
            fed.route_subject("camel-math", {"topic;": "Number theory", "sub_topic": "Prime factorization"}),
        )
        self.assertEqual(
            fed.route_subject("camel-chemistry", {"topic;": "Materials chemistry", "sub_topic": "FCC crystal lattice"}),
            "aerospace-materials-1",
        )
        self.assertIsNone(
            fed.route_subject("camel-chemistry", {"topic;": "Organic chemistry", "sub_topic": "Naming organic compounds"}),
        )
        self.assertEqual(
            fed.route_subject(
                "finance-alpaca",
                {"instruction": "Calculate WACC and NPV for this project", "input": "", "output": "Discount cash flows at WACC."},
            ),
            "business-management",
        )
        self.assertIsNone(
            fed.route_subject(
                "finance-alpaca",
                {"instruction": "For a car loan scam with 0% financing", "input": "", "output": "Car dealers earn margin."},
            ),
        )

    def test_quality_gate_rejections(self):
        good_prob = "A steady incompressible pipe flow with density $\\rho = 1000\\,\\mathrm{kg/m^3}$ enters at $2\\,\\mathrm{m/s}$. Find pressure drop."
        good_sol = (
            "### Step 1: Continuity Equation\n"
            "Because the fluid is incompressible, $A_1 v_1 = A_2 v_2$ gives $v_2 = 4\\,\\mathrm{m/s}$.\n\n"
            "### Step 2: Bernoulli Equation\n"
            "Applying $$p_1 + \\frac{1}{2}\\rho v_1^2 = p_2 + \\frac{1}{2}\\rho v_2^2$$ yields "
            "$$\\Delta p = \\frac{1}{2}(1000)(16 - 4) = 6000\\,\\mathrm{Pa}.$$\n"
            "Dimensional check: $[\\mathrm{kg/m^3}][\\mathrm{m^2/s^2}] = [\\mathrm{Pa}]$, matching SI units."
        )
        self.assertEqual(fed.passes_quality_gate(good_prob, good_sol, "fluid-mechanics"), (True, "ok"))

        self.assertEqual(
            fed.passes_quality_gate("As shown in the figure below, compute the pressure drop across the nozzle in SI units.", good_sol, "fluid-mechanics")[0],
            False,
        )
        self.assertEqual(
            fed.passes_quality_gate(good_prob, good_sol + "\nAfter some algebra we get the answer.", "fluid-mechanics"),
            (False, "skip_phrase"),
        )
        self.assertEqual(
            fed.passes_quality_gate(good_prob, good_sol + " $unbalanced", "fluid-mechanics"),
            (False, "katex_unbalanced"),
        )
        self.assertEqual(
            fed.passes_quality_gate(good_prob, good_sol + " 🚀", "fluid-mechanics"),
            (False, "emoji"),
        )
        self.assertEqual(
            fed.passes_quality_gate(good_prob, "Short answer $x=1$.", "fluid-mechanics"),
            (False, "sol_len"),
        )

    def test_anti_contamination_schema_and_v2_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_p = pathlib.Path(tmp)
            holdout_stmt = "A rigid cylinder of mass $m = 5\\,\\mathrm{kg}$ rolls without slipping down an incline of $30^\\circ$. Find its linear acceleration."
            holdout_row = {
                "id": "holdout-1",
                "task": "problem_solve",
                "subject": "engineering-mechanics",
                "messages": [
                    {"role": "system", "content": "sys"},
                    {"role": "user", "content": f'<problem_statement title="P1">\n{holdout_stmt}\n</problem_statement>\n\n# Task\nSolve.'},
                    {"role": "assistant", "content": "sol"},
                ],
            }
            base_zip = tmp_p / "base.zip"
            with zipfile.ZipFile(base_zip, "w") as zf:
                zf.writestr("train_sft_enriched.jsonl", json.dumps({"id": "base-1", "messages": []}) + "\n")
                zf.writestr("train_dpo_enriched.jsonl", json.dumps({"id": "dpo-1"}) + "\n")
                zf.writestr("train_grpo.jsonl", json.dumps({"id": "grpo-1"}) + "\n")
                zf.writestr("eval_holdout.jsonl", json.dumps(holdout_row) + "\n")
                zf.writestr("rewards.py", "# rewards\n")

            hashes = fed.load_base_holdout_hashes(base_zip)
            self.assertIn(fed.norm_text_hash(holdout_stmt), hashes)

            ext_rec = fed.make_sft_record(
                "camel-math",
                "advanced-maths",
                "Solve the ODE $y'' + 4y = 0$ with $y(0) = 1$, $y'(0) = 0$ explicitly step by step.",
                "Characteristic equation $r^2 + 4 = 0$ gives $r = \\pm 2i$, hence $y(t) = \\cos(2t)$ and $\\boxed{\\cos(2t)}$.",
                "abc123def456",
                {"topic;": "Differential equations", "sub_topic": "Second-order ODEs"},
            )
            self.assertEqual([m["role"] for m in ext_rec["messages"]], ["system", "user", "assistant"])
            self.assertEqual(ext_rec["teacher"], "external:camel-math")

            v2_zip = tmp_p / "v2.zip"
            v2_again_zip = tmp_p / "v2_again.zip"
            dpo_ext = {"id": "dpo-rigour-ext-1"}
            grpo_ext = {"id": "grpo-ext-1"}
            fed.build_v2_zip(base_zip, v2_zip, [ext_rec], [dpo_ext], [grpo_ext])
            fed.build_v2_zip(v2_zip, v2_again_zip, [ext_rec], [dpo_ext], [grpo_ext])
            with zipfile.ZipFile(v2_zip, "r") as zf, zipfile.ZipFile(v2_again_zip, "r") as zf2:
                self.assertEqual(zf.read("eval_holdout.jsonl").decode("utf-8").strip(), json.dumps(holdout_row))
                self.assertEqual(zf.read("rewards.py").decode("utf-8"), "# rewards\n")
                for fn in ("train_sft_enriched.jsonl", "train_dpo_enriched.jsonl", "train_grpo.jsonl"):
                    l1 = [json.loads(l) for l in zf.read(fn).decode("utf-8").splitlines() if l.strip()]
                    l2 = [json.loads(l) for l in zf2.read(fn).decode("utf-8").splitlines() if l.strip()]
                    self.assertEqual(len(l1), 2)
                    self.assertEqual(len(l1), len(l2))
                sft_lines = [json.loads(l) for l in zf.read("train_sft_enriched.jsonl").decode("utf-8").splitlines() if l.strip()]
                self.assertEqual(sft_lines[1]["id"], ext_rec["id"])


if __name__ == "__main__":
    unittest.main()
