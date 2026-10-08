"""Tests for tools/sources_manifest.py (official-PDF manifest for the web portal)."""
import pathlib
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import sources_manifest as sm  # noqa: E402

REPO = TOOLS.parent


def make_tree(files):
    """Create an empty sources/cuatrimestre-1 tree; return the repo root."""
    tmp = tempfile.TemporaryDirectory()
    root = pathlib.Path(tmp.name)
    for rel in files:
        p = root / "sources" / "cuatrimestre-1" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b"%PDF-1.4 test")
    return tmp, root


class ManifestTests(unittest.TestCase):
    def build(self, files):
        tmp, root = make_tree(files)
        self.addCleanup(tmp.cleanup)
        return sm.build_manifest(root)

    def test_subject_key_strips_numeric_prefix(self):
        m = self.build(["01-fluid-mechanics/teoria/Notes.pdf"])
        self.assertIn("fluid-mechanics", m["subjects"])
        self.assertEqual(m["subjects"]["fluid-mechanics"]["folder"], "01-fluid-mechanics")

    def test_laboratorios_are_excluded_entirely(self):
        m = self.build([
            "03-engineering-mechanics/laboratorios/lab-1/report.pdf",
            "03-engineering-mechanics/laboratorios/general-instructions/intro.pdf",
            "03-engineering-mechanics/teoria/Notes.pdf",
        ])
        flat = sm.iter_items(m)
        self.assertEqual([i["name"] for i in flat], ["Notes.pdf"])

    def test_subject_level_folders_are_classified(self):
        m = self.build([
            "03-engineering-mechanics/teoria/Notes.pdf",
            "03-engineering-mechanics/problemas/Problems.pdf",
            "03-engineering-mechanics/slides/s.pdf",
            "02-aerospace-materials-1/examenes/first-partial/e1.pdf",
            "02-aerospace-materials-1/schedule/cal.pdf",
        ])
        mech = m["subjects"]["engineering-mechanics"]["general"]
        self.assertEqual([i["name"] for i in mech["teoria"]], ["Notes.pdf"])
        self.assertEqual([i["name"] for i in mech["problemas"]], ["Problems.pdf"])
        self.assertEqual([i["name"] for i in mech["slides"]], ["s.pdf"])
        mat = m["subjects"]["aerospace-materials-1"]["general"]
        self.assertEqual([i["name"] for i in mat["examenes"]], ["e1.pdf"])
        self.assertEqual([i["name"] for i in mat["schedule"]], ["cal.pdf"])

    def test_unit_folders_are_classified_with_number_and_title(self):
        m = self.build([
            "01-fluid-mechanics/unit-02-flow-kinematics/problemas/K1.pdf",
            "01-fluid-mechanics/unit-02-flow-kinematics/slides/ch2.pdf",
        ])
        units = m["subjects"]["fluid-mechanics"]["units"]
        self.assertEqual(len(units), 1)
        u = units[0]
        self.assertEqual(u["id"], "unit-02-flow-kinematics")
        self.assertEqual(u["number"], 2)
        self.assertEqual(u["title"], "Flow Kinematics")
        self.assertEqual([i["name"] for i in u["problemas"]], ["K1.pdf"])
        self.assertEqual([i["name"] for i in u["slides"]], ["ch2.pdf"])
        self.assertEqual(u["teoria"], [])

    def test_units_sorted_by_number(self):
        m = self.build([
            "04-advanced-maths/unit-10-x/teoria/a.pdf",
            "04-advanced-maths/unit-02-y/teoria/b.pdf",
        ])
        nums = [u["number"] for u in m["subjects"]["advanced-maths"]["units"]]
        self.assertEqual(nums, [2, 10])

    def test_href_is_url_encoded_per_segment(self):
        m = self.build(["04-advanced-maths/unit-01-a/teoria/BookODE's v2.pdf"])
        item = sm.iter_items(m)[0]
        self.assertEqual(item["name"], "BookODE's v2.pdf")
        self.assertEqual(
            item["href"],
            "sources/cuatrimestre-1/04-advanced-maths/unit-01-a/teoria/BookODE%27s%20v2.pdf",
        )

    def test_non_pdf_files_are_ignored(self):
        tmp, root = make_tree(["01-fluid-mechanics/teoria/Notes.pdf"])
        self.addCleanup(tmp.cleanup)
        extra = root / "sources" / "cuatrimestre-1" / "01-fluid-mechanics" / "teoria" / "x.txt"
        extra.write_text("hi")
        names = [i["name"] for i in sm.iter_items(sm.build_manifest(root))]
        self.assertEqual(names, ["Notes.pdf"])

    def test_files_sorted_naturally(self):
        m = self.build([
            "02-aerospace-materials-1/unit-01-a/teoria/Session 10.pdf",
            "02-aerospace-materials-1/unit-01-a/teoria/Session 2.pdf",
        ])
        names = [i["name"] for i in m["subjects"]["aerospace-materials-1"]["units"][0]["teoria"]]
        self.assertEqual(names, ["Session 2.pdf", "Session 10.pdf"])

    def test_item_records_byte_size(self):
        m = self.build(["01-fluid-mechanics/teoria/Notes.pdf"])
        self.assertEqual(sm.iter_items(m)[0]["bytes"], len(b"%PDF-1.4 test"))

    def test_render_js_is_deterministic_and_parseable(self):
        import json
        m = self.build(["01-fluid-mechanics/teoria/Notes.pdf"])
        a, b = sm.render_js(m), sm.render_js(m)
        self.assertEqual(a, b)
        self.assertTrue(a.startswith("window.AE_SOURCES = "))
        self.assertTrue(a.endswith(";\n"))
        self.assertNotIn("\r", a)
        payload = a[len("window.AE_SOURCES = "):-2]
        self.assertEqual(json.loads(payload), m)

    def test_empty_unit_folders_still_listed(self):
        tmp, root = make_tree(["04-advanced-maths/unit-01-a/teoria/a.pdf"])
        self.addCleanup(tmp.cleanup)
        (root / "sources/cuatrimestre-1/04-advanced-maths/unit-06-heat-wave-laplace/teoria").mkdir(parents=True)
        units = sm.build_manifest(root)["subjects"]["advanced-maths"]["units"]
        self.assertEqual([u["number"] for u in units], [1, 6])
        self.assertEqual(units[1]["teoria"], [])


@unittest.skipUnless((REPO / "sources" / "cuatrimestre-1").is_dir(), "real sources tree not present")
class RealTreeTests(unittest.TestCase):
    """Integration: the real manifest must never leak labs and must point at real files."""

    @classmethod
    def setUpClass(cls):
        cls.manifest = sm.build_manifest(REPO)
        cls.items = sm.iter_items(cls.manifest)

    def test_no_lab_material_in_real_manifest(self):
        bad = [i["href"] for i in self.items if "laborator" in i["href"].lower()]
        self.assertEqual(bad, [])

    def test_every_href_resolves_to_an_existing_file(self):
        from urllib.parse import unquote
        missing = [i["href"] for i in self.items if not (REPO / unquote(i["href"])).is_file()]
        self.assertEqual(missing, [])

    def test_covers_all_five_subjects(self):
        self.assertEqual(
            sorted(self.manifest["subjects"]),
            ["advanced-maths", "aerospace-materials-1", "business-management",
             "engineering-mechanics", "fluid-mechanics"],
        )


if __name__ == "__main__":
    unittest.main()
