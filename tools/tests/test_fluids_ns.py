"""The Topic 4 (Navier-Stokes) generator in tools/fluids_ns/: the vault notes are the source, the generated files are
up to date, every problem has its card on the page and its note, and every figure the page embeds exists."""
import importlib.util
import pathlib
import re
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
BUILD = REPO / "tools/fluids_ns/build.py"
PAGE = REPO / "subjects/fluid-mechanics/problemas/topic-4-navier-stokes.html"


def load_build():
    spec = importlib.util.spec_from_file_location("fluids_ns_build", BUILD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FluidsNsTests(unittest.TestCase):
    def test_each_note_is_in_the_canonical_layout(self):
        build = load_build()
        for P in build.load_problems():
            path = REPO / build.VAULT / f"{P['note_title']}.md"
            self.assertEqual(build.note_md(P), path.read_text(encoding="utf-8"), P["note_title"])

    def test_generated_files_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(BUILD), "--check"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_every_problem_has_a_card_a_note_and_its_figures(self):
        build = load_build()
        probs = build.load_problems()
        page = PAGE.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r'class="problem-card"', page)), len(probs))
        for P in probs:
            self.assertIn(f'id="{P["id"]}"', page)
            self.assertTrue((REPO / "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas"
                             / f"{P['id'].upper()}.pdf").is_file())
        for name in build.FIG.RASTER:
            self.assertTrue((REPO / "vault/attachments/FM-T4" / f"{name}.png").is_file(), name)

    def test_statements_have_no_emoji(self):
        page = PAGE.read_text(encoding="utf-8")
        self.assertIsNone(re.search("[\U0001F300-\U0001FAFF\u2600-\u27BF]", page))


if __name__ == "__main__":
    unittest.main()
