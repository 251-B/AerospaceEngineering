"""Tests for tools/build_pdfs.py (A4 PDFs of the theory and problem pages)."""
import pathlib
import subprocess
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_pdfs as bp  # noqa: E402


class TargetTests(unittest.TestCase):
    def test_card_ids_come_from_problem_cards_only(self):
        html = ('<article class="problem-card" id="p1"></article><div class="x" id="no"></div>'
                '<section class="problem-box wide" id="ex-2"></section><details open class="problem-card" id="p1">')
        self.assertEqual(bp.card_ids(html), ["p1", "ex-2"])

    def test_theory_pages_get_one_pdf_and_problem_pages_one_per_card(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            for f in bp.INPUTS:
                (root / f).parent.mkdir(parents=True, exist_ok=True)
                (root / f).write_text("x")
            for rel, text in {"subjects/s/teoria/topic-1.html": "<h1>T</h1>",
                              "subjects/s/teoria/index.html": "<h1>I</h1>",
                              "subjects/s/problemas/topic-1.html": '<div class="problem-card" id="a"></div>'}.items():
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / rel).write_text(text)
            t = bp.targets(root)
            self.assertEqual(sorted(t), ["assets/pdf/s/problemas/topic-1.pdf", "assets/pdf/s/problemas/topic-1/a.pdf",
                                         "assets/pdf/s/teoria/topic-1.pdf"])
            todo, orphans = bp.stale(root)
            self.assertEqual(len(todo), 3)
            self.assertEqual(orphans, [])


class MirrorTests(unittest.TestCase):
    def test_mirror_copies_vault_figures_and_points_katex_at_the_local_folder(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dst:
            root, out = pathlib.Path(src), pathlib.Path(dst)
            (root / "assets/css").mkdir(parents=True)
            (root / "assets/css/x.css").write_text("x")
            (root / "vault/attachments/FM").mkdir(parents=True)
            (root / "vault/attachments/FM/fig.png").write_bytes(b"png")
            page = root / "subjects/s/problemas/topic-1.html"
            page.parent.mkdir(parents=True)
            page.write_text('<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>'
                            '<img src="../../../vault/attachments/FM/fig.png">')
            kx = root / "katex"
            kx.mkdir()
            bp._mirror(root, kx, out)
            self.assertEqual((out / "vault/attachments/FM/fig.png").read_bytes(), b"png")
            text = (out / "subjects/s/problemas/topic-1.html").read_text()
            self.assertNotIn("cdn.jsdelivr.net", text)
            self.assertIn(kx.resolve().as_uri(), text)


class RepositoryTests(unittest.TestCase):
    def test_pdfs_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(TOOLS / "build_pdfs.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout[-2000:])


if __name__ == "__main__":
    unittest.main()
