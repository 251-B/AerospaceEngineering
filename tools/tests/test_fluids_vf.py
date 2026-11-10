"""The Topic 7 (Viscous Flows) generator in tools/fluids_vf/: the generated files are up to date, every sheet has
its card and its figures, no section is labelled "Phase", a malformed note names its file, and the four fluid builders
write the same problem count on the portal."""
import importlib.util
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
BUILD = REPO / "tools/fluids_vf/build.py"
PAGE = REPO / "subjects/fluid-mechanics/problemas/topic-7-viscous-flow.html"
SHEETS = REPO / "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas"


def load_build():
    spec = importlib.util.spec_from_file_location("fluids_vf_build", BUILD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cards(page):
    """id -> html of each problem card."""
    parts = re.split(r'(?=<article class="problem-card" id=")', page)
    return {re.match(r'<article class="problem-card" id="([\w-]+)"', p).group(1): p for p in parts[1:]}


class FluidsDaTests(unittest.TestCase):
    def test_generated_files_are_up_to_date(self):
        proc = subprocess.run([sys.executable, str(BUILD), "--check"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_every_sheet_has_a_card_and_its_figures(self):
        build = load_build()
        probs = build.load_problems()
        found = cards(PAGE.read_text(encoding="utf-8"))
        self.assertEqual(sorted(found), sorted(P["id"] for P in probs))
        for P in probs:
            for n in P["sheets"]:
                name = build.SHEET_FILES.get(n, f"VF{n}.pdf")
                self.assertTrue((SHEETS / name).is_file(), (P["id"], n))
            for blocks in [P["statement"]] + [b for _, b in P["sections"]]:
                for b in blocks:
                    if b[0] == "fig":
                        on_disk = [REPO / "vault" / build.FIG_DIR / f"{b[1]}.{ext}" for ext in ("svg", "png")]
                        self.assertTrue(any(p.is_file() for p in on_disk), b[1])
        self.assertEqual({n for P in probs for n in P["sheets"]}, set(build.SHEETS))

    def test_every_exponent_system_and_number_checks(self):
        proc = subprocess.run([sys.executable, str(BUILD.parent / "verify_viscous_flows.py")], capture_output=True,
                              text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout[-2000:] + proc.stderr)

    def test_no_phase_labels(self):
        page = PAGE.read_text(encoding="utf-8")
        text = re.sub(r"(?s)<style.*?</style>|<script.*?</script>|<!--.*?-->|<[^>]+>", " ", page)   # what the reader sees
        self.assertNotRegex(text, r"(?i)\bphase\s*\d|four phases|4-phase")

    def test_malformed_note_names_its_file(self):
        build = load_build()
        good = next((REPO / build.VAULT).glob("Problem - VF3 *.md")).read_text(encoding="utf-8")
        broken = {
            "no-source": re.sub(r"(?m)^Source: .*$", "", good),
            "no-heading": good.replace("# Problem VF3:", "# VF3:"),
            "phase": re.sub(r"(?m)^## (?!Statement).*$", "## Phase 1", good, count=1),
            "no-id": re.sub(r'(?m)^id: "vf3"\n', "", good),
        }
        with tempfile.TemporaryDirectory() as tmp:
            for name, text in broken.items():
                path = pathlib.Path(tmp) / f"Problem - VF3 {name}.md"
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError) as ctx:
                    build.read_problem(path)
                self.assertIn(path.name, str(ctx.exception), name)

    def test_portal_count_is_shared_by_the_fluid_builders(self):
        build = load_build()
        total = build.CL.fluid_problem_count()
        portal = (REPO / "index.html").read_text(encoding="utf-8")
        i = portal.index('href="subjects/fluid-mechanics/problemas/index.html"')
        self.assertIn(f'<span class="area-badge available">{total} problems', portal[i:i + 2000])
        for rel in (build.PROBLEMS_INDEX, build.THEORY_INDEX):
            self.assertIn(f"Problem Sets ({total} Solved)", (REPO / rel).read_text(encoding="utf-8"), rel)
        for name in ("fluids_ns", "fluids_fs"):
            src = (REPO / f"tools/{name}/build.py").read_text(encoding="utf-8")
            self.assertIn("CL.sync_portal(root)", src, name)
            self.assertNotIn('area-badge available">{', src, name)


if __name__ == "__main__":
    unittest.main()
