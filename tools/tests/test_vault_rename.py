import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import vault_rename as vr  # noqa: E402

MAP = {"Concepto A": "Concept A"}


class RewriteTests(unittest.TestCase):
    def test_plain_alias_heading_and_embed(self):
        text = "[[Concepto A]] [[Concepto A|alias]] [[Concepto A#H]] ![[Concepto A]] [[Other]]"
        out, n = vr.rewrite_links(text, MAP)
        self.assertEqual(out, "[[Concept A]] [[Concept A|alias]] [[Concept A#H]] ![[Concept A]] [[Other]]")
        self.assertEqual(n, 4)

    def test_links_written_with_folder_paths_and_md_suffix(self):
        text = "[[01 - Fluid/Concepto A]] [[01 - Fluid/Concepto A#H|x]] [[Concepto A.md]]"
        out, n = vr.rewrite_links(text, MAP)
        self.assertEqual(out, "[[01 - Fluid/Concept A]] [[01 - Fluid/Concept A#H|x]] [[Concept A.md]]")
        self.assertEqual(n, 3)

    def test_fenced_code_is_left_alone(self):
        text = "```\n[[Concepto A]]\n```\n[[Concepto A]]\n"
        out, n = vr.rewrite_links(text, MAP)
        self.assertEqual(out, "```\n[[Concepto A]]\n```\n[[Concept A]]\n")
        self.assertEqual(n, 1)

    def test_tilde_art_inside_backtick_fence_does_not_close_it(self):
        text = "```\n  ~~~~~ sea\n[[Concepto A]]\n```\n[[Concepto A]]\n"
        out, n = vr.rewrite_links(text, MAP)
        self.assertEqual(n, 1)
        self.assertTrue(out.endswith("[[Concept A]]\n"))

    def test_crlf_preserved(self):
        out, _ = vr.rewrite_links("[[Concepto A]]\r\nx\r\n", MAP)
        self.assertEqual(out, "[[Concept A]]\r\nx\r\n")


class ApplyTests(unittest.TestCase):
    def make(self):
        d = tempfile.TemporaryDirectory()
        v = pathlib.Path(d.name)
        (v / "Concepto A.md").write_text("body", encoding="utf-8")
        (v / "Index.md").write_text("see [[Concepto A|A]]", encoding="utf-8")
        return d, v

    def test_apply_renames_and_rewrites(self):
        d, v = self.make()
        with d:
            self.assertEqual(vr.apply(v, MAP, True), 0)
            self.assertTrue((v / "Concept A.md").exists())
            self.assertFalse((v / "Concepto A.md").exists())
            self.assertEqual((v / "Index.md").read_text(encoding="utf-8"), "see [[Concept A|A]]")

    def test_dry_run_changes_nothing(self):
        d, v = self.make()
        with d:
            vr.apply(v, MAP, False)
            self.assertTrue((v / "Concepto A.md").exists())

    def test_refuses_existing_target_and_illegal_chars(self):
        d, v = self.make()
        with d:
            (v / "Concept A.md").write_text("x", encoding="utf-8")
            self.assertEqual(vr.apply(v, MAP, True), 1)
            self.assertEqual(vr.apply(v, {"Concepto A": "Bad: name"}, True), 1)


if __name__ == "__main__":
    unittest.main()
