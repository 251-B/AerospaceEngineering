"""Geometry simulator of the Engineering Mechanics problem cards (assets/js/mechanics-3d-sim.js): the script stays
inside the "Exercise simulators (SVG only)" rule of AGENTS.md, every archetype renders, the change of basis matrix
stays orthonormal whatever the controls do, the default state is the data of the configuration, nothing is written
to web storage and every text keeps AAA contrast under the six reading palettes. The widget runs in headless
Edge/Chrome through mechanics_sim_harness.html."""
import html
import json
import math
import pathlib
import re
import subprocess
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "mechanics_sim_harness.html"
JS = REPO / "assets/js/mechanics-3d-sim.js"
CSS = REPO / "assets/css/mechanics-3d-sim.css"
SURFACE = REPO / "assets/css/study-surface.css"

ARCHETYPES = ["curvilinear-3d", "rotating-wire-groove", "oscillator-phase", "rb-euler-kinematics",
              "rb-inertia-principal", "rb-planar-dynamics", "rb-rolling-contact", "rb-gyro-multibody"]
VIEWS = {"iso": "3D Isometric", "top": "Top XY", "front": "Front XZ", "side": "Side YZ", "omega": "Plane normal to ω"}
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️]")


class MechanicsSimStaticTests(unittest.TestCase):
    """Checks that need no browser."""

    @classmethod
    def setUpClass(cls):
        cls.js = JS.read_text(encoding="utf-8")
        cls.css = CSS.read_text(encoding="utf-8")

    def test_every_archetype_is_registered(self):
        for name in ARCHETYPES:
            self.assertIn(f"ARCH['{name}'] = {{", self.js, name)
        self.assertEqual(len(re.findall(r"^  ARCH\['[\w-]+'\] = \{", self.js, re.M)), len(ARCHETYPES))

    def test_svg_only_no_canvas_no_webgl(self):
        code = re.sub(r"/\*.*?\*/", "", self.js, flags=re.S)
        for banned in ("canvas", "webgl", "three", "getContext"):
            self.assertNotIn(banned, code.lower(), banned)
        self.assertIn("viewBox: '0 0 760 360'", self.js)

    def test_no_storage_and_no_code_evaluation(self):
        code = re.sub(r"/\*.*?\*/", "", self.js, flags=re.S)
        for banned in ("localStorage", "sessionStorage", "indexedDB", "document.cookie", "eval(", "new Function", "innerHTML",
                       "insertAdjacentHTML", "fetch(", "XMLHttpRequest"):
            self.assertNotIn(banned, code, banned)

    def test_no_emoji(self):
        self.assertIsNone(EMOJI.search(self.js))
        self.assertIsNone(EMOJI.search(self.css))

    def test_controls_are_hidden_in_print_and_the_figure_stays(self):
        m = re.search(r"@media print \{(.*)\}\s*$", self.css, re.S)
        self.assertIsNotNone(m)
        self.assertRegex(m.group(1), r"\.m3-controls[^{]*\{\s*display:\s*none")
        self.assertNotRegex(m.group(1), r"\.m3-(svg|figure|readouts)\s*\{[^}]*display:\s*none")

    def test_text_colours_come_from_the_page_variables(self):
        # text is never painted with a subject accent or a figure colour: only the page's text variables
        for rule in re.findall(r"([^{}]+)\{([^}]*)\}", self.css):
            sel, body = rule
            if re.search(r"(^|[\s,])color\s*:", body) or (" text" in sel and "fill" in body):
                colours = re.findall(r"(?:^|[\s;])(?:color|fill)\s*:\s*([^;]+);", body)
                for c in colours:
                    self.assertRegex(c.strip(), r"^var\(--text-(heading|main)", f"{sel.strip()}: {c}")
        self.assertRegex(self.css, r"\.m3-svg text, \.m3-svg tspan \{ fill: var\(--text-heading\)")

    def test_simulator_text_is_registered_in_the_palette_stylesheet(self):
        css = SURFACE.read_text(encoding="utf-8")
        self.assertIn(".m3-svg :is(text, tspan)", css)
        self.assertIn(".m3-readouts dd", css)


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class MechanicsSimBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=60000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))
        cls.arch = cls.results["archetypes"]

    def readout(self, name, label):
        for line in self.arch[name]["default"]["readouts"]:
            if line.startswith(label + " = "):
                return line[len(label) + 3:]
        self.fail(f"{name}: no readout {label!r}")

    def test_no_script_error(self):
        self.assertEqual(self.results["errors"], [])
        self.assertEqual(self.results["api"]["archetypes"], ARCHETYPES)
        self.assertEqual(self.results["api"]["views"], list(VIEWS))

    def test_every_archetype_renders_inline_svg_inside_its_card(self):
        self.assertEqual(sorted(self.arch), sorted(ARCHETYPES))
        for name, rep in self.arch.items():
            with self.subTest(name):
                self.assertTrue(rep["mounted"])
                self.assertTrue(rep["insideCard"])
                self.assertEqual(rep["viewBox"], "0 0 760 360")
                self.assertEqual(rep["canvas"], 0)
                self.assertGreater(rep["texts"], 15)
                self.assertGreater(rep["shapes"], 20)
                self.assertEqual(rep["matrixRows"], 9, "the 3x3 matrix is written in the fold-down view")
                self.assertFalse(rep["badDefault"], "NaN or undefined in the default drawing")

    def test_matrices_stay_orthonormal_after_moving_every_control(self):
        for name, rep in self.arch.items():
            with self.subTest(name):
                self.assertGreater(rep["moved"], 0)
                self.assertLess(rep["worstOrtho"], 1e-6, "active rotation: R R^T = I and det R = 1")
                self.assertLess(rep["worstTotal"], 1e-6, "total rotation: R R^T = I and det R = 1")
                self.assertFalse(rep["nan"], "NaN or undefined after moving a control")
                self.assertTrue(rep["backToDefault"], "restoring the controls restores the state")

    def test_rotation_selector_lists_every_rotation(self):
        expected = {"rb-euler-kinematics": 3, "rb-gyro-multibody": 3, "rotating-wire-groove": 2, "rb-rolling-contact": 2}
        for name, rep in self.arch.items():
            self.assertEqual(rep["rotations"], expected.get(name, 1), name)

    def test_default_state_reproduces_the_configuration(self):
        # helix R = 2 m, b = 0.5 m/rad at theta = 90 deg: r = (0, 2, b pi/2), |v| = sqrt(R^2 + b^2), rho_c = (R^2 + b^2)/R
        v = self.arch["curvilinear-3d"]["default"]["vars"]
        self.assertAlmostEqual(v["x"], 0, places=6)
        self.assertAlmostEqual(v["y"], 2, places=6)
        self.assertAlmostEqual(v["z"], 0.5 * math.pi / 2, places=6)
        self.assertAlmostEqual(v["v"], math.hypot(2, 0.5), places=4)
        self.assertAlmostEqual(v["rhoc"], 4.25 / 2, places=3)
        self.assertAlmostEqual(v["at"], 0, places=3)
        # hoop R = 1 m at theta = 60 deg in a frame turned 30 deg: rho = R sin(theta)
        w = self.arch["rotating-wire-groove"]["default"]["vars"]
        self.assertAlmostEqual(w["rho"], math.sin(math.radians(60)), places=6)
        self.assertAlmostEqual(w["x"], w["rho"] * math.cos(math.radians(30)), places=6)
        self.assertAlmostEqual(w["vdrag"], 2 * w["rho"], places=6)
        # bar L = 2 m hanging from its end, 30 deg from the downward vertical
        b = self.arch["rb-planar-dynamics"]["default"]["vars"]
        self.assertAlmostEqual(b["xG"], math.sin(math.radians(30)), places=6)
        self.assertAlmostEqual(b["yG"], -math.cos(math.radians(30)), places=6)
        self.assertAlmostEqual(b["vG"], 3.0, places=6)
        # disk r = 0.4 m on a cylinder R = 1.2 m, 30 deg from the top: r phi = (R + r) theta
        r = self.arch["rb-rolling-contact"]["default"]["vars"]
        self.assertAlmostEqual(math.degrees(r["phi"]), 120, places=6)
        self.assertAlmostEqual(math.hypot(r["xC"], r["yC"]), 1.6, places=6)
        self.assertAlmostEqual(math.hypot(r["xK"], r["yK"]), 1.2, places=6)
        # forced oscillator at r = 1, zeta = 0.2: M = 1/(2 zeta), phase lag 90 deg
        o = self.arch["oscillator-phase"]["default"]["vars"]
        self.assertAlmostEqual(o["M"], 2.5, places=6)
        self.assertAlmostEqual(math.degrees(o["psi"]), 90, places=6)
        # the matrix shown by default is the rotation of the first angle of the configuration
        m = self.arch["rb-euler-kinematics"]["default"]["matrix"]
        self.assertAlmostEqual(m[0][0], math.cos(math.radians(20)), places=6)
        self.assertAlmostEqual(m[0][1], -math.sin(math.radians(20)), places=6)

    def test_declared_readouts_are_the_formulas_of_the_configuration(self):
        self.assertEqual(self.readout("curvilinear-3d", "Height b theta"), "0.7854 m")
        self.assertEqual(self.readout("curvilinear-3d", "Speed"), "2.0616 m/s")
        self.assertEqual(self.readout("rotating-wire-groove", "rho"), "0.8660")
        self.assertEqual(self.readout("oscillator-phase", "M"), "2.5000")
        self.assertEqual(self.readout("rb-planar-dynamics", "xG"), "0.5000")
        self.assertEqual(self.readout("rb-planar-dynamics", "yG"), "−0.8660")

    def test_readout_parser_only_does_arithmetic(self):
        # a call that is not a listed function and a property name give no value: nothing is evaluated as code
        self.assertEqual(self.readout("curvilinear-3d", "Not arithmetic"), "–")
        self.assertEqual(self.readout("curvilinear-3d", "Prototype"), "–")

    def test_inertia_tensor_properties(self):
        t = self.results["inertia"]
        self.assertAlmostEqual(t["trace0"], t["trace1"], places=6)
        self.assertAlmostEqual(t["productAtPrincipal"], 0, places=6)
        self.assertEqual(t["symmetric"], 0)
        # L-shaped plate (0.2 x 1 and 0.8 x 0.2 m, 3 kg): the largest principal moment is the polar one, I1 + I2 = I3
        self.assertAlmostEqual(t["principal"][0] + t["principal"][1], t["principal"][2], places=6)

    def test_quick_views_keyboard_and_drag_move_the_camera(self):
        for name, rep in self.arch.items():
            with self.subTest(name):
                self.assertEqual(rep["buttons"], list(VIEWS.values()))
                self.assertEqual(rep["views"]["top"]["cam"], [-90, 90])
                self.assertEqual(rep["views"]["front"]["cam"], [-90, 0])
                self.assertEqual(rep["views"]["side"]["cam"], [0, 0])
                self.assertEqual(rep["views"]["iso"]["cam"][0], 45)
                for key in VIEWS:
                    self.assertEqual(rep["views"][key]["pressed"], "true", key)
                    self.assertEqual(rep["views"][key]["view"], key)
                self.assertFalse(rep["nanViews"])
                self.assertEqual(rep["keyboard"], [5, 5])
                self.assertNotEqual(rep["drag"], [0, 0])

    def test_controls_are_labelled_and_keyboard_reachable(self):
        for name, rep in self.arch.items():
            self.assertEqual(rep["unlabelled"], 0, name)
            self.assertTrue(rep["svgFocusable"], name)

    def test_nothing_is_written_to_storage(self):
        self.assertEqual(self.results["storageWrites"], 0)

    def test_text_is_aaa_under_every_palette(self):
        self.assertEqual(len(self.results["contrast"]), 8)
        for state, rep in self.results["contrast"].items():
            self.assertGreater(rep["texts"], 300, state)
            self.assertGreaterEqual(rep["worst"], 7.0, f"{state}: {rep['where']}")


if __name__ == "__main__":
    unittest.main()
