"""Offline unit tests for tools/ai_training/extract_textbooks.py."""
import json
import pathlib
import sys
import tempfile
import unittest
import zipfile

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/ai_training"))

import extract_textbooks as et  # noqa: E402


class ExtractTextbooksTests(unittest.TestCase):
    def test_identify_book_mapping_and_lang(self):
        self.assertEqual(
            et.identify_book("Libros/Libros De Mecánica de Fluidos I (Revisar)/F. M. White. Fluid Mechanics. Mc-Graw Hill. 2015.pdf")[:2],
            ("fluid-mechanics", "en"),
        )
        self.assertEqual(
            et.identify_book("Libros/Libros de Materiales Aeroespaciales I/SHACKELFORD JF. . Introducción a la Ciencia de Materiales para ingenieros. 6th ed. Pearson Prentice-Hall..pdf")[:2],
            ("aerospace-materials-1", "es"),
        )
        self.assertEqual(
            et.identify_book("Libros/Libros de Ampliación de Matemáticas (Revisar)/R. Haberman. Elementary applied partial differential equations. 2nd ed.. Prentice Hall. 1987.pdf")[:2],
            ("advanced-maths", "en"),
        )
        self.assertEqual(
            et.identify_book("Libros/Libros de Mecánica Aplicada a la Ingeniería Aeroespacial (Revisar)/J. H. Ginsberg. Engineering Dynamics. Cambridge Univ. Press. 2007.pdf")[:2],
            ("engineering-mechanics", "en"),
        )
        self.assertIsNone(et.identify_book("random_unrelated_file.pdf"))

    def test_clean_pdf_page_and_hygiene_filters(self):
        raw_page = "142\nThe continuity equa-\ntion describes conservation of mass in steady compressible\nflow.\nChapter 3\n143"
        cleaned = et.clean_pdf_page(raw_page)
        self.assertIn("equation", cleaned)
        self.assertNotIn("equa-\ntion", cleaned)

        good_prose = (
            "In steady incompressible viscous flow through a circular pipe of constant diameter, "
            "the balance between the axial pressure gradient and viscous shear stress governs the velocity profile. "
            "Because fluid particles adhere to the solid wall under the no-slip boundary condition, the velocity vanishes at the wall "
            "and attains its maximum value along the centerline of the conduit. Integrating the radial momentum equation twice yields "
            "the classic parabolic Poiseuille distribution across the entire laminar cross section."
        )
        self.assertEqual(et.is_clean_chunk(good_prose, min_len=200, max_len=1500), (True, "ok"))

        self.assertEqual(et.is_clean_chunk(good_prose + " ........ 45", min_len=200)[1], "toc_or_frontmatter")
        self.assertEqual(et.is_clean_chunk(good_prose + " As shown in Figure 4.2 below.", min_len=200)[1], "figure_dep")
        self.assertEqual(et.is_clean_chunk(good_prose + " \ufffd\ufffd", min_len=200)[1], "replacement_char")

    def test_sft_schema_katex_and_v3_zip_idempotent(self):
        pages = [
            "Example 2.1 Steady Pipe Flow\n"
            "Water of density $\\rho = 1000\\,\\mathrm{kg/m^3}$ flows steadily through a horizontal pipe of diameter $D = 0.05\\,\\mathrm{m}$ at velocity $V = 2.0\\,\\mathrm{m/s}$. Determine the mass flow rate.\n"
            "Solution\n"
            "First compute the cross-sectional area $A = \\pi D^2 / 4 = \\pi (0.05)^2 / 4 = 1.9635 \\times 10^{-3}\\,\\mathrm{m^2}$. "
            "Next multiply by density and velocity to obtain the mass flow rate $\\dot{m} = \\rho A V = 1000 (1.9635 \\times 10^{-3})(2.0) = 3.927\\,\\mathrm{kg/s}$. "
            "Dimensional check: $[\\mathrm{kg/m^3}][\\mathrm{m^2}][\\mathrm{m/s}] = [\\mathrm{kg/s}]$, consistent with SI mass flow rate."
        ]
        seen = set()
        ex = et.extract_examples_from_pages(pages, "fluid-mechanics", "en", "White", seen)
        self.assertEqual(len(ex), 1)
        self.assertEqual([m["role"] for m in ex[0]["messages"]], ["system", "user", "assistant"])
        self.assertTrue(et.katex_balanced(ex[0]["messages"][-1]["content"]))

        with tempfile.TemporaryDirectory() as tmp:
            tmp_p = pathlib.Path(tmp)
            base_zip = tmp_p / "v2.zip"
            v3_zip = tmp_p / "v3.zip"
            with zipfile.ZipFile(base_zip, "w") as zf:
                zf.writestr("train_sft_enriched.jsonl", json.dumps({"id": "base-1", "messages": []}) + "\n")
                zf.writestr("train_dpo_enriched.jsonl", json.dumps({"id": "dpo-1"}) + "\n")
                zf.writestr("train_grpo.jsonl", json.dumps({"id": "grpo-1"}) + "\n")
                zf.writestr("eval_holdout.jsonl", json.dumps({"id": "eval-1"}) + "\n")
                zf.writestr("rewards.py", "# rewards\n")
            cpt = [{"id": "cpt-flui-1", "subject": "fluid-mechanics", "lang": "en", "source": "textbook/White", "text": "x" * 950}]
            et.build_v3_zip(base_zip, v3_zip, ex, cpt)
            with zipfile.ZipFile(v3_zip, "r") as zf:
                self.assertIn("train_cpt.jsonl", zf.namelist())
                self.assertEqual(zf.read("rewards.py").decode("utf-8"), "# rewards\n")
                sft = [json.loads(l) for l in zf.read("train_sft_enriched.jsonl").decode("utf-8").splitlines() if l.strip()]
                self.assertEqual(len(sft), 2)


if __name__ == "__main__":
    unittest.main()
