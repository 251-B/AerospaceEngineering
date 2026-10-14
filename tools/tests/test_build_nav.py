"""tools/build_nav.py: the manifest follows nav.json, and nav.json agrees with the pages on disk."""
import contextlib
import io
import json
import pathlib
import shutil
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

import build_nav  # noqa: E402


def make_repo(root):
    """A tiny portal: one subject with a theory area, a problems area and a sources page."""
    for rel in ("subjects/demo/teoria/index.html", "subjects/demo/teoria/topic-1.html",
                "subjects/demo/problemas/index.html", "subjects/demo/problemas/topic-1.html",
                "subjects/demo/sources/index.html"):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("<html></html>", encoding="utf-8")
    spec = {"subjects": [{"slug": "demo", "name": "Demo", "accent": "#123456",
                          "teoria": [{"page": "topic-1.html", "label": "1 · One"}],
                          "problemas": [{"page": "topic-1.html", "label": "1 · One"}]}]}
    (root / "tools").mkdir()
    (root / "tools/nav.json").write_text(json.dumps(spec), encoding="utf-8")
    return spec


class BuildNavTests(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.spec = make_repo(self.tmp)

    def test_manifest_follows_the_spec_and_adds_the_extras_that_exist(self):
        manifest, errors = build_nav.build_manifest(self.tmp)
        self.assertEqual(errors, [])
        subject = manifest["subjects"][0]
        self.assertEqual([g["id"] for g in subject["groups"]], ["teoria", "problemas"])
        self.assertEqual(subject["groups"][0]["href"], "subjects/demo/teoria/index.html")
        self.assertEqual(subject["groups"][0]["pages"][0], {"href": "subjects/demo/teoria/topic-1.html", "label": "1 · One"})
        # sources/ exists, exams/ does not
        self.assertEqual([x["label"] for x in subject["extras"]], ["Theory & exercise PDFs"])

    def test_a_page_on_disk_that_is_not_listed_is_an_error(self):
        (self.tmp / "subjects/demo/teoria/topic-2.html").write_text("x", encoding="utf-8")
        _, errors = build_nav.build_manifest(self.tmp)
        self.assertTrue(any("topic-2.html exists but is not listed" in e for e in errors), errors)

    def test_a_listed_page_that_is_missing_is_an_error(self):
        (self.tmp / "subjects/demo/problemas/topic-1.html").unlink()
        _, errors = build_nav.build_manifest(self.tmp)
        self.assertTrue(any("listed but does not exist" in e for e in errors), errors)

    def test_a_subject_folder_that_is_not_listed_is_an_error(self):
        (self.tmp / "subjects/other").mkdir()
        _, errors = build_nav.build_manifest(self.tmp)
        self.assertTrue(any("subjects/other/ exists but is not listed" in e for e in errors), errors)

    def test_children_are_nested_and_checked(self):
        (self.tmp / "subjects/demo/teoria/topic-1-1.html").write_text("x", encoding="utf-8")
        spec = json.loads((self.tmp / "tools/nav.json").read_text(encoding="utf-8"))
        spec["subjects"][0]["teoria"][0]["children"] = [{"page": "topic-1-1.html", "label": "1.1"}]
        (self.tmp / "tools/nav.json").write_text(json.dumps(spec), encoding="utf-8")
        manifest, errors = build_nav.build_manifest(self.tmp)
        self.assertEqual(errors, [])
        self.assertEqual(manifest["subjects"][0]["groups"][0]["pages"][0]["children"][0]["href"], "subjects/demo/teoria/topic-1-1.html")

    def run_main(self, *args):
        with contextlib.redirect_stdout(io.StringIO()):
            return build_nav.main(["--root", str(self.tmp), *args])

    def test_check_detects_a_stale_file_and_write_fixes_it(self):
        self.assertEqual(self.run_main("--check"), 1)   # nothing written yet
        self.assertEqual(self.run_main(), 0)
        self.assertEqual(self.run_main("--check"), 0)
        (self.tmp / "assets/data/nav.js").write_text("window.AE_NAV = {};\n", encoding="utf-8")
        self.assertEqual(self.run_main("--check"), 1)


class RealPortalTests(unittest.TestCase):
    def test_the_repository_manifest_is_up_to_date_and_consistent(self):
        manifest, errors = build_nav.build_manifest(REPO)
        self.assertEqual(errors, [])
        self.assertEqual(build_nav.render_js(manifest), (REPO / build_nav.OUT_REL).read_text(encoding="utf-8"))

    def test_every_listed_page_exists(self):
        manifest, _ = build_nav.build_manifest(REPO)
        for subject in manifest["subjects"]:
            hrefs = [x["href"] for x in subject["extras"]] + [g["href"] for g in subject["groups"]]
            for g in subject["groups"]:
                hrefs += [p["href"] for p in build_nav._flatten(g["pages"])]
            for href in hrefs:
                self.assertTrue((REPO / href).is_file(), href)
                self.assertNotRegex(href.lower(), r"laborator")


if __name__ == "__main__":
    unittest.main()
