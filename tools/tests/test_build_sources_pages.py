"""Tests for tools/build_sources_pages.py (Theory & exercise PDF pages and Exams pages)."""
import pathlib
import subprocess
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_sources_pages as bs  # noqa: E402


class ClassifyExamTests(unittest.TestCase):
    def test_kind_year_call_and_solutions(self):
        e = bs.classify_exam("FLUIDS_FINALEXAM_2014_ORD_SOL_P1.pdf")
        self.assertEqual((e["kind"], e["year"], e["label"]), ("final", 2014, "Ordinary call · Solutions, problem 1"))
        e = bs.classify_exam("MATHS_SECONDPARTIAL_2018_MT3_G45_SOL.pdf")
        self.assertEqual((e["kind"], e["label"]), ("second", "Midterm 3 · Group 45 · Solutions"))

    def test_compilations_undated_and_legacy_names(self):
        e = bs.classify_exam("MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf")
        self.assertEqual((e["year"], e["year_label"], e["label"]), (2017, "2013–2017", "Compilation · Exam"))
        e = bs.classify_exam("MATERIALS_FIRSTPARTIAL_UNDATED.pdf")
        self.assertEqual((e["kind"], e["year"], e["year_label"]), ("first", None, "Undated"))
        e = bs.classify_exam("1stPartial2022.pdf")
        self.assertEqual((e["kind"], e["year"]), ("first", 2022))
        self.assertIsNone(bs.classify_exam("Problems T3_Diffusion.pdf"))

    def test_ordinary_call_sorts_before_extraordinary_and_exam_before_solutions(self):
        names = ["X_FINALEXAM_2015_EXTRA_SOL.pdf", "X_FINALEXAM_2015_ORD_SOL.pdf",
                 "X_FINALEXAM_2015_EXTRA.pdf", "X_FINALEXAM_2015_ORD.pdf"]
        order = sorted(names, key=lambda n: bs.classify_exam(n)["sort"])
        self.assertEqual(order, ["X_FINALEXAM_2015_ORD.pdf", "X_FINALEXAM_2015_ORD_SOL.pdf",
                                 "X_FINALEXAM_2015_EXTRA.pdf", "X_FINALEXAM_2015_EXTRA_SOL.pdf"])


class DuplicateTests(unittest.TestCase):
    def test_identical_copies_are_listed_once_with_the_standard_name_and_known_year(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "e" / "old").mkdir(parents=True)
            (root / "e" / "M_FIRSTPARTIAL_UNDATED.pdf").write_bytes(b"same")
            (root / "e" / "old" / "1stPartial2023.pdf").write_bytes(b"same")
            data = {"general": {"examenes": [
                {"name": "M_FIRSTPARTIAL_UNDATED.pdf", "href": "e/M_FIRSTPARTIAL_UNDATED.pdf", "bytes": 4},
                {"name": "1stPartial2023.pdf", "href": "e/old/1stPartial2023.pdf", "bytes": 4}]}, "units": []}
            entries = bs.exam_entries(root, data)
        self.assertEqual(len(entries), 1)
        self.assertEqual((entries[0]["item"]["name"], entries[0]["year"]), ("M_FIRSTPARTIAL_UNDATED.pdf", 2023))


class PageTests(unittest.TestCase):
    def test_pages_load_the_index_fonts_and_exams_are_not_on_the_theory_page(self):
        pages = bs.build()
        for path, text in pages.items():
            self.assertIn("family=Abril+Fatface", text, path)
            self.assertIn("family=Newsreader", text, path)
            if path.parent.name == "sources":
                self.assertNotIn("_FINALEXAM_", text, path)

    def test_generated_pages_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(TOOLS / "build_sources_pages.py"), "--check"],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
