"""The Topic 3 (conservation laws) generator in tools/fluids_cl/: the generated files are up to date, every problem
has its card on the page and its note in the vault, and every figure the page embeds exists."""
import importlib.util
import pathlib
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
BUILD = REPO / "tools/fluids_cl/build.py"
PAGE = REPO / "subjects/fluid-mechanics/problemas/topic-3-conservation-laws.html"


def load_build():
    spec = importlib.util.spec_from_file_location("fluids_cl_build", BUILD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FluidsClTests(unittest.TestCase):
    def test_generated_files_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(BUILD), "--check"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_every_problem_has_a_card_and_a_note(self):
        build = load_build()
        probs = build.load_problems()
        self.assertEqual([P["id"] for P in probs], [f"cl{n}" for n in range(1, 23)])
        page = PAGE.read_text(encoding="utf-8")
        for P in probs:
            self.assertIn(f'id="{P["id"]}"', page)
            self.assertTrue((REPO / build.VAULT / f"{P['note_title']}.md").is_file(), P["note_title"])

    def test_every_figure_the_page_embeds_exists(self):
        build = load_build()
        for rel in build.REG.files:
            self.assertTrue((REPO / rel).is_file(), rel)
        for name in build.FIG.RASTER:
            self.assertTrue((REPO / "vault/attachments/FM-T3" / f"{name}.png").is_file(), name)


if __name__ == "__main__":
    unittest.main()
