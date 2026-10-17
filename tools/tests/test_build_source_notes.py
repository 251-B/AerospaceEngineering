"""Tests for tools/build_source_notes.py (one generated vault note per file under sources/)."""
import pathlib
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_source_notes as bsn  # noqa: E402

CONFIG = {
    "subjects": {"01-fluid-mechanics": "01 - Fluid Mechanics"},
    "root_folder": "General",
    "build_artifact_extensions": [".aux"],
    "working_files": ["sources/cuatrimestre-1/01-fluid-mechanics/teoria/scratch.txt"],
}

FILES = [
    "01-fluid-mechanics/teoria/Notes.pdf",
    "01-fluid-mechanics/teoria/scratch.txt",
    "01-fluid-mechanics/unit-02-flow/problemas/K1.pdf",
    "01-fluid-mechanics/unit-02-flow/problemas/main.aux",
    "01-fluid-mechanics/unit-02-flow/problemas/Fig.png",
    "01-fluid-mechanics/unit-03-laws/problemas/Fig.png",
    "01-fluid-mechanics/laboratorios/lab-1/data.txt",
    "01-fluid-mechanics/schedule/.gitkeep",
]


def make_repo(extra_notes=None):
    """Create a repo with sources/cuatrimestre-1 and a vault; return (root, tmp)."""
    tmp = tempfile.TemporaryDirectory()
    root = pathlib.Path(tmp.name)
    for rel in FILES:
        p = root / "sources" / "cuatrimestre-1" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b"x" * 10)
    (root / "sources").mkdir(exist_ok=True)
    (root / "sources" / "README.md").write_text("root readme", encoding="utf-8")
    notes = {
        "vault/01 - Fluid Mechanics/Topic 1.md":
            "See sources/cuatrimestre-1/01-fluid-mechanics/teoria/Notes.pdf and K1.pdf.",
        "vault/01 - Fluid Mechanics/Problem - K1.md": "Statement from K1.pdf only.",
    }
    notes.update(extra_notes or {})
    for rel, text in notes.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return root, tmp


def by_path(desired):
    return {rel: text for rel, text in desired.items() if "/Source - " in rel}


class SizeTests(unittest.TestCase):
    def test_text_sources_count_lf_bytes_and_binary_sources_count_all_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            text = root / "README.md"
            text.write_bytes(b"line one\r\nline two\r\n")
            binary = root / "Notes.pdf"
            binary.write_bytes(b"%PDF\r\n\x00\r\n")
            self.assertEqual(bsn.size_of(text), len(b"line one\nline two\n"))
            self.assertEqual(bsn.size_of(binary), len(b"%PDF\r\n\x00\r\n"))


class BuildSourceNotesTest(unittest.TestCase):
    def setUp(self):
        self.root, self.tmp = make_repo()
        self.desired, self.summary = bsn.plan(self.root, CONFIG)
        self.notes = by_path(self.desired)

    def tearDown(self):
        self.tmp.cleanup()

    def note_for(self, file_name):
        matches = [t for t in self.notes.values() if f"# Source: {file_name}\n" in t]
        self.assertEqual(len(matches), 1, file_name)
        return matches[0]

    def test_one_note_per_file_except_gitkeep(self):
        # 8 files under sources/cuatrimestre-1 minus .gitkeep, plus sources/README.md
        self.assertEqual(len(self.notes), 8)
        self.assertFalse(any(".gitkeep" in rel for rel in self.notes))

    def test_note_names_are_unique_even_when_file_names_repeat(self):
        names = [pathlib.PurePosixPath(rel).name for rel in self.notes]
        self.assertEqual(len(names), len(set(names)))
        self.assertIn("vault/07 - Sources/01 - Fluid Mechanics/Source - 01-fluid-mechanics - unit-02-flow - problemas - Fig (png).md", self.desired)
        self.assertIn("vault/07 - Sources/01 - Fluid Mechanics/Source - 01-fluid-mechanics - unit-03-laws - problemas - Fig (png).md", self.desired)

    def test_kinds_and_statuses(self):
        self.assertIn("kind: teoria", self.note_for("Notes.pdf"))
        self.assertIn("kind: laboratorio", self.note_for("data.txt"))
        self.assertIn("status: build-artifact", self.note_for("main.aux"))
        self.assertIn("status: working-file", self.note_for("scratch.txt"))
        self.assertIn("kind: other", self.note_for("README.md"))

    def test_citation_by_full_path_and_by_unique_name(self):
        notes_pdf = self.note_for("Notes.pdf")
        self.assertIn("status: referenced", notes_pdf)
        self.assertIn("[[01 - Fluid Mechanics/Topic 1]]", notes_pdf)
        k1 = self.note_for("K1.pdf")
        self.assertIn("status: referenced", k1)
        self.assertIn("[[01 - Fluid Mechanics/Problem - K1]]", k1)

    def test_repeated_file_name_is_not_matched_by_name(self):
        figs = [t for t in self.notes.values() if "# Source: Fig.png\n" in t]
        self.assertEqual(len(figs), 2)
        for text in figs:
            self.assertIn("status: not-referenced", text)

    def test_index_lists_every_file_and_counts_status(self):
        index_rel = "vault/07 - Sources/01 - Fluid Mechanics/Sources Index - Fluid Mechanics.md"
        index = self.desired[index_rel]
        self.assertIn("- Files: 7", index)
        self.assertIn("- Referenced by at least one note (a mention counts): 2", index)
        self.assertIn("[[Source - 01-fluid-mechanics - teoria - Notes (pdf)\\|Notes.pdf]]", index)

    def test_write_then_check_passes_and_detects_missing_note(self):
        refused = bsn.write(self.root, self.desired)
        self.assertEqual(refused, [])
        self.assertEqual(bsn.check(self.root, self.desired), [])
        victim = next(p for p in self.root.rglob("*.md") if "Notes (pdf)" in p.name)
        victim.unlink()
        problems = bsn.check(self.root, self.desired)
        self.assertTrue(any(p.startswith("missing") for p in problems), problems)

    def test_orphan_with_banner_is_removed_but_hand_written_note_is_refused(self):
        bsn.write(self.root, self.desired)
        gen_dir = self.root / "vault" / "07 - Sources" / "01 - Fluid Mechanics"
        stale = gen_dir / "Source - old - gone (pdf).md"
        stale.write_text("---\n---\n" + bsn.BANNER + "\n", encoding="utf-8")
        hand = gen_dir / "Written by hand.md"
        hand.write_text("my own note\n", encoding="utf-8")
        refused = bsn.write(self.root, self.desired)
        self.assertFalse(stale.exists())
        self.assertEqual(refused, [hand.relative_to(self.root).as_posix()])

    def test_shared_name_is_credited_only_within_its_subject(self):
        root, tmp = make_repo({"vault/01 - Fluid Mechanics/Mentions shared.md": "Uses Shared.pdf from the course."})
        self.addCleanup(tmp.cleanup)
        for rel in ("02-other-subject/teoria/Shared.pdf", "01-fluid-mechanics/teoria/Shared.pdf"):
            p = root / "sources" / "cuatrimestre-1" / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b"x")
        config = dict(CONFIG, subjects={**CONFIG["subjects"], "02-other-subject": "02 - Other Subject"})
        desired, _ = bsn.plan(root, config)
        fluid = desired["vault/07 - Sources/01 - Fluid Mechanics/Source - 01-fluid-mechanics - teoria - Shared (pdf).md"]
        other = desired["vault/07 - Sources/02 - Other Subject/Source - 02-other-subject - teoria - Shared (pdf).md"]
        self.assertIn("status: referenced", fluid)
        self.assertIn("[[01 - Fluid Mechanics/Mentions shared]]", fluid)
        self.assertIn("shared with 1 other copy", fluid)
        self.assertIn("status: not-referenced", other)

    def test_output_is_deterministic(self):
        again, _ = bsn.plan(self.root, CONFIG)
        self.assertEqual(self.desired, again)


if __name__ == "__main__":
    unittest.main()
