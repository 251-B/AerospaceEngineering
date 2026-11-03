"""The Topic 5 (Hydrostatics) generator in tools/fluids_fs/ and its exercise simulators: the generated files are up to
date, every problem has its card, its sheet and its figures, no section is labelled "Phase", and each simulator sits
inside the solution of its own problem card (SVG only, no canvas, no storage)."""
import importlib.util
import pathlib
import re
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
BUILD = REPO / "tools/fluids_fs/build.py"
PAGE = REPO / "subjects/fluid-mechanics/problemas/topic-5-hydrostatics.html"
SIM_JS = REPO / "assets/js/hydrostatics-sim.js"
SHEETS = REPO / "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas"


def load_build():
    spec = importlib.util.spec_from_file_location("fluids_fs_build", BUILD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cards(page):
    """id -> html of each problem card."""
    parts = re.split(r'(?=<article class="problem-card" id=")', page)
    return {re.match(r'<article class="problem-card" id="([\w-]+)"', p).group(1): p for p in parts[1:]}


class FluidsFsTests(unittest.TestCase):
    def test_generated_files_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(BUILD), "--check"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_every_problem_has_a_card_its_sheets_and_its_figures(self):
        build = load_build()
        probs = build.load_problems()
        page = PAGE.read_text(encoding="utf-8")
        found = cards(page)
        self.assertEqual(sorted(found), sorted(P["id"] for P in probs))
        for P in probs:
            for n in P["sheets"]:
                self.assertTrue((SHEETS / f"fluid_statics_{n}.pdf").is_file(), (P["id"], n))
            for _, blocks in P["sections"]:
                for b in blocks:
                    if b[0] == "fig":
                        self.assertTrue((REPO / "vault" / build.FIG_DIR / f"{b[1]}.svg").is_file(), b[1])
        covered = {n for P in probs for n in P["sheets"]}
        self.assertEqual(covered, set(range(1, 11)), "every official sheet is solved (FS8 inside FS2)")

    def test_no_phase_labels(self):
        page = PAGE.read_text(encoding="utf-8")
        text = re.sub(r"(?s)<style.*?</style>|<script.*?</script>|<!--.*?-->|<[^>]+>", " ", page)   # what the reader sees
        self.assertNotRegex(text, r"(?i)\bphase\s*\d|four phases|4-phase")

    def test_each_simulator_is_inside_the_solution_of_its_card(self):
        build = load_build()
        found = cards(PAGE.read_text(encoding="utf-8"))
        sims = {P["id"]: P["sim"] for P in build.load_problems() if P["sim"]}
        self.assertEqual(sorted(sims.values()), sorted(build.SIMS))
        for pid, card in found.items():
            here = re.findall(r'<div class="hs-sim" data-sim="([\w-]+)"', card)
            self.assertEqual(here, [sims[pid]] if pid in sims else [], pid)
            if pid in sims:
                solution = card[card.index('<div class="solution-content">'):]
                self.assertIn(f'data-sim="{sims[pid]}"', solution, f"{pid}: the simulator belongs to the solution")
        self.assertEqual(PAGE.read_text(encoding="utf-8").count('src="../../../assets/js/hydrostatics-sim.js"'), 1)

    def test_simulator_script_is_svg_only_and_knows_every_simulator(self):
        js = SIM_JS.read_text(encoding="utf-8")
        for word in ("<canvas", "getContext(", "localStorage", "sessionStorage", "THREE."):
            self.assertNotIn(word, js)
        build = load_build()
        for sim in build.SIMS:
            self.assertIn(f"'{sim}':", js)


if __name__ == "__main__":
    unittest.main()
