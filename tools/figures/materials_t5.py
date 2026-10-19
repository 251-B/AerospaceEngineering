"""Topic 5 figures for Aerospace Materials I: mechanical properties (Sessions 11 and 12).

Most figures are schematic redraws of the slides: they keep the labels and the qualitative shape of the curves,
and they are not to scale. The charts whose values cannot be redrawn faithfully (the cold-work, Cu-Ni, grain-size,
Brinell, micrograph and hardness-strength charts) are copied from the slides as PNG crops, registered with
`REG.raster`. Run `python tools/build_topic_pages.py` to write the SVG files to vault/attachments/T5 and rebuild
the page.
"""
import math

from figures.svgkit import (Canvas, Registry, arrow, circle, dim, dot, line, pathd, poly, rect, sub, text)

REG = Registry("T5")


class M:
    """Data coordinates mapped to pixels: the origin is at (x0, y0), sx and sy are pixels per unit, y points up."""

    def __init__(self, x0, y0, sx, sy):
        self.x0, self.y0, self.sx, self.sy = x0, y0, sx, sy

    def p(self, x, y):
        return (self.x0 + x * self.sx, self.y0 - y * self.sy)

    def axes(self, c, xmax, ymax, xl, yl, xt=(), yt=()):
        line(c, self.p(0, 0), self.p(xmax, 0), "EDGE", 1.3, head=True)
        line(c, self.p(0, 0), self.p(0, ymax), "EDGE", 1.3, head=True)
        for v, s in xt:
            x, y = self.p(v, 0)
            line(c, (x, y), (x, y + 5), "EDGE", 1.1)
            text(c, (x, y + 19), s, "TEXT", "middle", 12)
        for v, s in yt:
            x, y = self.p(0, v)
            line(c, (x - 5, y), (x, y), "EDGE", 1.1)
            text(c, (x - 8, y + 4), s, "TEXT", "end", 12)
        x, y = self.p(xmax, 0)
        text(c, (x, y + 38), xl, "HEAD", "end", 13, "700")
        x, y = self.p(0, ymax)
        text(c, (x + 8, y + 4), yl, "HEAD", "start", 13, "700")

    def poly(self, c, pts, col="ACC", w=2.4, dash=None, fill="none", close=False, opacity=None):
        poly(c, [self.p(*q) for q in pts], col, w, dash, fill, close, opacity)

    def text(self, c, x, y, s, col="HEAD", anchor="start", size=13, weight="400"):
        text(c, self.p(x, y), s, col, anchor, size, weight)

    def dot(self, c, x, y, col="HEAD", fill="HEAD", r=4):
        dot(c, self.p(x, y), r, col, fill)

    def guide(self, c, a, b):
        """Dashed guide line between two data points."""
        line(c, self.p(*a), self.p(*b), "EDGE", 1.1, "4,4")


def sample(fn, a, b, n=160):
    """Points (x, fn(x)) on [a, b], skipping the x where fn returns None."""
    out = []
    for i in range(n + 1):
        x = a + (b - a) * i / n
        y = fn(x)
        if y is not None:
            out.append((x, y))
    return out


def stress_strain(e):
    """Schematic engineering stress-strain curve (MPa): elastic line, rounded plastic zone, necking, fracture."""
    if e <= 0.005:
        return 1e5 * e
    if e <= 0.06:
        return 500 + 300 * math.sin(math.pi / 2 * (e - 0.005) / 0.055)
    if e <= 0.11:
        return 800 - 240 * ((e - 0.06) / 0.05) ** 2
    return None


def specimen_geometry():
    c = Canvas(760, 250)
    pts = [(40, 80), (200, 80), (240, 97), (480, 97), (520, 80), (720, 80), (720, 150), (520, 150),
           (480, 133), (240, 133), (200, 150), (40, 150)]
    poly(c, pts, "HEAD", 1.8, None, "none", True)
    dim(c, (290, 168), (430, 168), "gauge length 50 mm", lab_off=(0, -10))
    dim(c, (240, 200), (480, 200), "reduced section 60 mm", lab_off=(0, -10))
    dim(c, (26, 80), (26, 150), "18 mm", lab_off=(-20, 4), anchor="end")
    dim(c, (360, 97), (360, 133), "0.505 D", lab_off=(48, 4), anchor="start")
    text(c, (220, 66), "radius 10 mm", "TEXT", "middle", 12)
    text(c, (120, 178), "grip", "TEXT", "middle", 12)
    text(c, (620, 178), "grip", "TEXT", "middle", 12)
    REG.put("specimen-geometry", c, "Tensile specimen with its dimensions",
            "Standard tensile specimen (ASTM E8, metals) with the dimensions labelled on the slide. Not to scale")


def curve_regions():
    c = Canvas(680, 420)
    m = M(80, 370, 520 / 0.12, 320 / 900)
    m.poly(c, sample(stress_strain, 0, 0.005, 40) + [(0.005, 0), (0, 0)], "GREEN", 0, None, "GREEN", True, 0.2)
    m.poly(c, sample(stress_strain, 0.005, 0.11, 120) + [(0.11, 0), (0.005, 0)], "PINK", 0, None, "PINK", True, 0.16)
    m.poly(c, sample(stress_strain, 0, 0.11, 200), "ACC", 2.6)
    m.guide(c, (0, 500), (0.005, 500))
    m.guide(c, (0.005, 0), (0.005, 500))
    m.guide(c, (0.06, 0), (0.06, 800))
    m.dot(c, 0.005, 500)
    m.dot(c, 0.06, 800)
    m.dot(c, 0.11, 560)
    m.text(c, 0.0005, 530, sub("σ", "y"))
    m.text(c, 0.0006, 360, "elastic zone (σ &lt; σy)", "GREEN", "start", 12, "700")
    m.text(c, 0.03, 150, "plastic zone (" + "σ &gt; " + sub("σ", "y") + ")", "PINK", "middle", 13, "700")
    m.text(c, 0.062, 825, "tensile strength (UTS)")
    m.text(c, 0.113, 545, "fracture stress")
    m.text(c, 0.06, 30, "uniform deformation", "HEAD", "middle", 12)
    m.axes(c, 0.12, 900, "engineering strain ε", "stress σ (MPa)",
           xt=[(0.02, "0.02"), (0.04, "0.04"), (0.06, "0.06"), (0.08, "0.08"), (0.10, "0.10"), (0.12, "0.12")],
           yt=[(200, "200"), (400, "400"), (600, "600"), (800, "800")])
    REG.put("curve-regions", c, "Schematic stress-strain curve with the elastic and plastic zones",
            "Schematic stress-strain curve: elastic zone, yield strength, uniform deformation, tensile strength and fracture. Not to scale")


def modulus_types():
    c = Canvas(640, 400)
    m = M(70, 330, 540 / 0.05, 300 / 2200)

    def f(e):
        return 1e5 * e - 1.25e6 * e * e

    m.poly(c, sample(f, 0, 0.05, 160), "ACC", 2.6)
    m.poly(c, [(0, 0), (0.012, 1200)], "BLUE", 1.5, "6,4")
    e1 = 0.02
    m.poly(c, [(0, 0), (0.028, f(e1) / e1 * 0.028)], "GREEN", 1.5, "6,4")
    e2 = 0.035
    s2 = f(e2)
    k2 = 1e5 - 2.5e6 * e2
    m.poly(c, [(0.025, s2 + k2 * (0.025 - e2)), (0.045, s2 + k2 * (0.045 - e2))], "PINK", 1.5, "6,4")
    m.dot(c, e1, f(e1))
    m.dot(c, e2, s2)
    m.text(c, 0.0125, 1235, "initial " + "E (" + "ε &lt; 0.5 %)", "BLUE")
    m.text(c, 0.0285, 2075, "secant E", "GREEN")
    m.text(c, 0.0245, 1700, "tangent E at " + sub("σ", "2"), "PINK", "end")
    m.text(c, 0.0205, 1470, sub("σ", "1"))
    m.text(c, 0.0355, 1925, sub("σ", "2"))
    m.axes(c, 0.05, 2200, "strain ε", "σ (MPa)",
           xt=[(0.01, "0.01"), (0.02, "0.02"), (0.03, "0.03"), (0.04, "0.04"), (0.05, "0.05")],
           yt=[(500, "500"), (1000, "1000"), (1500, "1500"), (2000, "2000")])
    REG.put("modulus-types", c, "Initial, secant and tangent moduli of a non-linear material",
            "Schematic non-linear stress-strain curve with the initial, secant and tangent moduli")


def material_curves():
    c = Canvas(760, 300)

    def metal(t):
        return 1 - (1 - t / 0.7) ** 2 if t <= 0.7 else 1 - 0.45 * ((t - 0.7) / 0.3) ** 2

    def thermoplastic(t):
        return 0.55 * (1 - math.exp(-6 * t)) + 0.45 * t ** 4

    def elastomer(t):
        return 0.55 * (1 - math.exp(-3.5 * t)) + 0.3 * t ** 3

    def ceramic(t):
        return 0.95 * t / 0.42 if t <= 0.42 else None

    panels = [("metal", metal, 1.0), ("thermoplastic above Tg", thermoplastic, 1.0),
              ("elastomer", elastomer, 1.0), ("ceramic, glass, concrete", ceramic, 0.42)]
    for i, (title, fn, end) in enumerate(panels):
        m = M(40 + i * 180, 230, 120, 120)
        m.poly(c, sample(fn, 0, end, 120), "ACC", 2.6)
        m.dot(c, end, fn(end), "HEAD", "HEAD")
        m.text(c, 0.0, 1.16, title, "HEAD", "start", 12.5, "700")
        m.axes(c, 1.0, 1.0, "ε", "σ")
    REG.put("material-curves", c, "Qualitative tensile curves of four material families",
            "Qualitative tensile curves of a metal, a thermoplastic above its glass transition, an elastomer and a ceramic, as on the slide")


def poisson():
    c = Canvas(640, 330)
    rect(c, 70, 90, 120, 170, "EDGE", 1.4, "4,4")
    text(c, (130, 286), "before load", "TEXT", "middle", 13)
    rect(c, 348, 67, 104, 196, "HEAD", 1.8)
    text(c, (400, 322), "under axial tension", "TEXT", "middle", 13)
    arrow(c, (400, 30), (400, 62), "BLUE", 1.8, 9)
    arrow(c, (400, 268), (400, 294), "BLUE", 1.8, 9)
    text(c, (414, 44), sub("σ", "z"), "BLUE", "start", 14)
    arrow(c, (316, 165), (344, 165), "PINK", 1.8, 8)
    arrow(c, (484, 165), (456, 165), "PINK", 1.8, 8)
    text(c, (300, 150), "Δl (lateral)/2", "PINK", "end", 13)
    text(c, (462, 100), "Δl (axial)/2", "BLUE", "start", 13)
    text(c, (70, 40), "ν = −ε_transverse / ε_longitudinal", "HEAD", "start", 14, "700")
    REG.put("poisson", c, "Lateral contraction under an axial tension",
            "Axial stretch of a block and the lateral contraction that goes with it (isotropic material, uniaxial stress). Not to scale")


def bend_test():
    c = Canvas(640, 300)
    rect(c, 120, 150, 400, 24, "HEAD", 1.8)
    for x in (170, 470):
        poly(c, [(x, 174), (x - 16, 198), (x + 16, 198)], "HEAD", 1.6, None, "none", True)
        arrow(c, (x, 246), (x, 202), "BLUE", 1.8, 9)
        text(c, (x + 12, 236), "F/2", "BLUE", "start", 13)
    arrow(c, (320, 50), (320, 146), "BLUE", 2.0, 10)
    text(c, (332, 70), "F", "BLUE", "start", 14, "700")
    dim(c, (170, 276), (470, 276), "L", lab_off=(0, -6))
    dim(c, (540, 150), (540, 174), "h", lab_off=(14, 4), anchor="start")
    text(c, (400, 140), "compression (upper surface)", "BLUE", "start", 12.5)
    text(c, (330, 222), "tension (lower surface)", "PINK", "start", 12.5)
    text(c, (120, 128), "b: width, into the page", "TEXT", "start", 12)
    REG.put("bend-test", c, "Three-point bend test",
            "Three-point bend test with the load F, the span L, the thickness h and the width b (schematic)")


def shear_test():
    c = Canvas(520, 300)
    rect(c, 130, 70, 160, 160, "EDGE", 1.2, "4,4")
    poly(c, [(130, 230), (290, 230), (330, 70), (170, 70)], "HEAD", 1.8, None, "none", True)
    dim(c, (130, 56), (170, 56), "a", lab_off=(0, -6))
    dim(c, (100, 70), (100, 230), "h", lab_off=(-16, 4), anchor="end")
    arrow(c, (180, 40), (300, 40), "BLUE", 2.0, 10)
    text(c, (308, 44), "F", "BLUE", "start", 14, "700")
    arrow(c, (300, 262), (120, 262), "BLUE", 2.0, 10)
    text(c, (300, 282), "F", "BLUE", "start", 14, "700")
    text(c, (146, 208), "θ", "HEAD", "start", 15)
    REG.put("shear-test", c, "Shear test",
            "Shear test: the top face moves by a over the height h, and the angle of shear is θ (schematic)")


def load_unload():
    c = Canvas(640, 340)
    m = M(70, 310, 520 / 0.02, 260 / 700)
    m.poly(c, [(0, 0), (0.005, 500)] + [(0.005 + 0.007 * i / 40, 500 + 150 * i / 40) for i in range(1, 41)],
           "HEAD", 2.4)
    m.poly(c, [(0.012, 650), (0.0055, 0)], "ACC", 2.2, "6,4")
    m.dot(c, 0.005, 500)
    m.dot(c, 0.0055, 0)
    m.dot(c, 0.012, 650, "HEAD", "ACC")
    m.text(c, 0.0003, 532, sub("σ", "y"))
    m.text(c, 0.0125, 660, "load at P", "HEAD")
    m.text(c, 0.0125, 240, "unloading (slope E)", "ACC")
    m.text(c, 0.0058, 40, "permanent strain " + sub("ε", "p"), "HEAD")
    m.axes(c, 0.02, 700, "strain ε", "stress σ (MPa)",
           xt=[(0.005, "0.005"), (0.01, "0.01"), (0.015, "0.015"), (0.02, "0.02")],
           yt=[(200, "200"), (400, "400"), (600, "600")])
    REG.put("load-unload", c, "Loading into the plastic zone and unloading",
            "Loading into the plastic zone and unloading parallel to the elastic line: the strain that remains is permanent (schematic)")


def dislocation_directions():
    c = Canvas(640, 300)
    for k in range(6):
        circle(c, (80 + 28 * k, 170), 14, "BLUE", 1.2, None, "BLUE", 0.35)
    for k in range(5):
        circle(c, (94 + 28 * k, 194), 14, "BLUE", 1.2, None, "BLUE", 0.35)
    arrow(c, (136, 170), (164, 170), "ACC", 2.0, 8)
    text(c, (150, 146), "b = 2R", "HEAD", "middle", 13, "700")
    text(c, (150, 40), "compact direction [110]", "HEAD", "middle", 14, "700")
    text(c, (150, 262), "Eb ∝ 4R²", "HEAD", "middle", 13, "700")
    for i in range(3):
        for j in range(3):
            circle(c, (400 + 28 * i, 120 + 28 * j), 14, "BLUE", 1.2, None, "BLUE", 0.35)
    arrow(c, (400, 120), (428, 148), "ACC", 2.0, 8)
    text(c, (440, 104), "b = 2√2 R", "HEAD", "start", 13, "700")
    text(c, (440, 40), "non-compact direction [100]", "HEAD", "middle", 14, "700")
    text(c, (440, 262), "Eb ∝ 8R²", "HEAD", "middle", 13, "700")
    REG.put("dislocation-directions", c, "Burgers vector in a compact and in a non-compact FCC direction",
            "Compact FCC [110] direction with b = 2R (left) and non-compact FCC [100] direction with b = 2√2 R (right), schematic")


def ductility_recovery():
    c = Canvas(640, 340)
    m = M(70, 300, 520 / 0.12, 250 / 700)

    def plastic(e):
        return 500 + 120 * (1 - math.exp(-(e - 0.005) / 0.025)) if e > 0.005 else 1e5 * e

    sf = plastic(0.1)
    ef = 0.1 - sf / 1e5
    m.poly(c, sample(plastic, 0, 0.1, 160), "ACC", 2.6)
    m.poly(c, [(0.1, sf), (ef, 0)], "BLUE", 1.8, "6,4")
    m.dot(c, 0.1, sf, "HEAD", "HEAD")
    m.dot(c, ef, 0, "HEAD", "HEAD")
    m.text(c, 0.1, sf + 40, "fracture", "HEAD", "middle", 12.5, "700")
    m.text(c, 0.07, 170, "elastic recovery", "BLUE")
    m.text(c, ef + 0.001, 42, "plastic elongation " + sub("ε", "p") + " (%EL)", "HEAD", "start", 12)
    m.axes(c, 0.12, 700, "strain ε", "stress σ (MPa)",
           xt=[(0.02, "0.02"), (0.04, "0.04"), (0.06, "0.06"), (0.08, "0.08"), (0.1, "0.1")],
           yt=[(200, "200"), (400, "400"), (600, "600")])
    REG.put("ductility-recovery", c, "Elastic recovery after fracture",
            "After fracture the elastic part is recovered and the remaining strain is the plastic elongation (schematic)")


def yield_offset():
    c = Canvas(700, 350)
    m1 = M(60, 300, 260 / 0.02, 240 / 800)

    def f(e):
        if e <= 0.0035:
            return 1e5 * e
        return 350 + 450 * (1 - math.exp(-(e - 0.0035) / 0.003))

    def gap(e):
        return f(e) - 1e5 * (e - 0.002)

    lo, hi = 0.0075, 0.011
    for _ in range(60):
        mid = (lo + hi) / 2
        if gap(lo) * gap(mid) <= 0:
            hi = mid
        else:
            lo = mid
    ey = (lo + hi) / 2
    sy = f(ey)
    m1.poly(c, sample(f, 0, 0.02, 200), "ACC", 2.6)
    m1.poly(c, [(0.002, 0), (ey, sy)], "BLUE", 1.5, "6,4")
    m1.dot(c, ey, sy, "HEAD", "HEAD")
    m1.text(c, ey + 0.0006, sy + 40, sub("σ", "y"))
    m1.text(c, 0.0036, 110, "0.2 % offset", "BLUE", "start", 12)
    m1.axes(c, 0.02, 800, "strain ε", "σ (MPa)",
            xt=[(0.005, "0.005"), (0.01, "0.01"), (0.015, "0.015"), (0.02, "0.02")],
            yt=[(200, "200"), (400, "400"), (600, "600"), (800, "800")])
    text(c, (60, 24), "conventional yield strength", "HEAD", "start", 13, "700")
    m2 = M(400, 300, 240 / 0.05, 240 / 500)
    m2.poly(c, [(0, 0), (0.002, 380), (0.0035, 300), (0.02, 300), (0.05, 420)], "ACC", 2.6)
    m2.guide(c, (0, 340), (0.05, 340))
    m2.dot(c, 0.002, 380, "HEAD", "HEAD")
    m2.dot(c, 0.0035, 300, "HEAD", "HEAD")
    m2.text(c, 0.0022, 395, "upper " + sub("σ", "max"), "HEAD", "start", 12)
    m2.text(c, 0.0042, 270, "lower " + sub("σ", "min"), "HEAD", "start", 12)
    m2.text(c, 0.022, 250, sub("σ", "y") + " = (" + sub("σ", "max") + " + " + sub("σ", "min") + ")/2", "HEAD", "start", 12)
    m2.axes(c, 0.05, 500, "strain ε", "σ (MPa)",
            xt=[(0.01, "0.01"), (0.02, "0.02"), (0.03, "0.03"), (0.04, "0.04"), (0.05, "0.05")],
            yt=[(200, "200"), (400, "400")])
    text(c, (400, 24), "discontinuous yield", "HEAD", "start", 13, "700")
    REG.put("yield-offset", c, "Yield strength by the offset method and at a discontinuous yield",
            "Left: the 0.2 % offset construction. Right: the upper and lower yield points of a discontinuous yield (schematic)")


def toughness():
    c = Canvas(680, 380)
    m = M(70, 330, 520 / 0.12, 280 / 900)

    def fa(e):
        return 1e5 * e if e <= 0.0085 else 850 + 10000 * (e - 0.0085)

    def fb(e):
        if e <= 0.005:
            return 1e5 * e
        if e <= 0.07:
            return 500 + 350 * (1 - math.exp(-(e - 0.005) / 0.03))
        return 810 - 60 * ((e - 0.07) / 0.04) ** 2

    def fc(e):
        if e <= 0.002:
            return 1e5 * e
        if e <= 0.05:
            return 200 + 130 * (1 - math.exp(-(e - 0.002) / 0.02))
        return 318 - 80 * ((e - 0.05) / 0.07) ** 2

    m.poly(c, sample(fb, 0, 0.11, 200) + [(0.11, 0), (0, 0)], "GREEN", 0, None, "GREEN", True, 0.18)
    m.poly(c, sample(fa, 0, 0.0115, 120), "PINK", 2.4)
    m.poly(c, sample(fb, 0, 0.11, 200), "GREEN", 2.4)
    m.poly(c, sample(fc, 0, 0.12, 200), "BLUE", 2.4)
    m.dot(c, 0.0115, fa(0.0115), "HEAD", "PINK")
    m.dot(c, 0.11, fb(0.11), "HEAD", "GREEN")
    m.dot(c, 0.12, fc(0.12), "HEAD", "BLUE")
    m.text(c, 0.0125, 915, "high strength, low ductility, low toughness", "PINK", "start", 12.5, "700")
    m.text(c, 0.072, 880, "high strength, high ductility, high toughness", "GREEN", "start", 12.5, "700")
    m.text(c, 0.075, 380, "low strength, high ductility, low toughness", "BLUE", "start", 12.5, "700")
    m.axes(c, 0.12, 900, "strain ε", "σ (MPa)",
           xt=[(0.02, "0.02"), (0.04, "0.04"), (0.06, "0.06"), (0.08, "0.08"), (0.10, "0.10"), (0.12, "0.12")],
           yt=[(200, "200"), (400, "400"), (600, "600"), (800, "800")])
    REG.put("toughness", c, "Stress-strain curves of three materials with different toughness",
            "Qualitative curves of three materials as on the slide; the shaded area under the middle curve is its toughness")


def resilience():
    c = Canvas(600, 340)
    m = M(70, 300, 500 / 0.05, 250 / 700)

    def fr(e):
        return 1e5 * e if e <= 0.005 else 500 + 120 * (1 - math.exp(-(e - 0.005) / 0.02))

    m.poly(c, [(0, 0), (0.005, 0), (0.005, 500)], "BLUE", 0, None, "BLUE", True, 0.22)
    m.poly(c, sample(fr, 0, 0.05, 160), "ACC", 2.6)
    m.guide(c, (0.005, 0), (0.005, 500))
    m.guide(c, (0, 500), (0.005, 500))
    m.dot(c, 0.005, 500)
    m.text(c, 0.0032, 150, "Ur", "BLUE", "middle", 14, "700")
    m.text(c, 0.0052, 520, sub("σ", "y"))
    m.text(c, 0.0052, 80, sub("ε", "y") + " = " + sub("σ", "y") + " / E", "HEAD", "start", 12)
    m.axes(c, 0.05, 700, "strain ε", "σ (MPa)",
           xt=[(0.01, "0.01"), (0.02, "0.02"), (0.03, "0.03"), (0.04, "0.04"), (0.05, "0.05")],
           yt=[(200, "200"), (400, "400"), (600, "600")])
    REG.put("resilience", c, "Modulus of resilience as the area under the elastic line",
            "The shaded triangle under the elastic line is the modulus of resilience (schematic)")


def true_stress():
    c = Canvas(680, 370)
    m = M(70, 320, 520 / 0.12, 270 / 1100)

    def true(e):
        if e <= 0.06:
            return stress_strain(e) * (1 + e)
        return 848 + 250 * ((e - 0.06) / 0.05)

    m.poly(c, sample(stress_strain, 0, 0.11, 200), "ACC", 2.4)
    m.poly(c, sample(true, 0, 0.11, 200), "BLUE", 2.4)
    m.guide(c, (0.06, 0), (0.06, 848))
    m.dot(c, 0.06, 800, "HEAD", "ACC")
    m.dot(c, 0.06, 848, "HEAD", "BLUE")
    m.text(c, 0.0605, 782, "M", "HEAD", "start", 13, "700")
    m.text(c, 0.0605, 868, "M′", "HEAD", "start", 13, "700")
    m.text(c, 0.07, 1000, "true curve", "BLUE", "start", 13, "700")
    m.text(c, 0.07, 620, "engineering curve", "ACC", "start", 13, "700")
    m.axes(c, 0.12, 1100, "strain ε", "σ (MPa)",
           xt=[(0.02, "0.02"), (0.04, "0.04"), (0.06, "0.06"), (0.08, "0.08"), (0.10, "0.10"), (0.12, "0.12")],
           yt=[(200, "200"), (400, "400"), (600, "600"), (800, "800"), (1000, "1000")])
    REG.put("true-stress", c, "Engineering and true stress-strain curves",
            "Engineering curve (orange) and true curve (blue) up to the maximum, M and M′; schematic, not to scale")


def strain_hardening():
    c = Canvas(640, 330)
    m = M(70, 300, 520 / 0.2, 250 / 700)

    def hard(ey, sy, su, tau):
        return lambda e: 1e4 * e if e <= ey else sy + (su - sy) * (1 - math.exp(-(e - ey) / tau))

    m.poly(c, sample(hard(0.02, 200, 380, 0.05), 0, 0.2, 200), "EDGE", 2.2)
    m.poly(c, sample(hard(0.033, 330, 460, 0.04), 0, 0.16, 200), "BLUE", 2.2)
    m.poly(c, sample(hard(0.044, 440, 520, 0.03), 0, 0.10, 200), "PINK", 2.2)
    m.text(c, 0.2, 392, "as received", "TEXT", "end", 12.5)
    m.text(c, 0.16, 482, "after cold work (1)", "BLUE", "end", 12.5)
    m.text(c, 0.10, 552, "after cold work (2)", "PINK", "end", 12.5)
    m.axes(c, 0.2, 700, "strain ε", "σ (MPa)",
           xt=[(0.04, "0.04"), (0.08, "0.08"), (0.12, "0.12"), (0.16, "0.16"), (0.2, "0.2")],
           yt=[(200, "200"), (400, "400"), (600, "600")])
    REG.put("strain-hardening", c, "Strain hardening after cold work",
            "Qualitative: each step of cold work raises the yield strength and reduces the strain to fracture")


def grain_boundary():
    c = Canvas(640, 310)
    a = 20.0

    def grid(ox, oy, th, keep):
        cs, sn = math.cos(th), math.sin(th)
        out = []
        for i in range(0, 16):
            for j in range(0, 13):
                x = ox + a * (i * cs - j * sn)
                y = oy + a * (i * sn + j * cs)
                if keep(x, y):
                    out.append((x, y))
        return out

    for x, y in grid(40, 40, 0.0, lambda x, y: x <= 300 and 30 <= y <= 280):
        circle(c, (x, y), 7, "ATOM", 1.2, None, "ATOM", 0.45)
    for x, y in grid(340, 40, math.radians(25), lambda x, y: x >= 340 and 30 <= y <= 280):
        circle(c, (x, y), 7, "ATOM", 1.2, None, "ATOM", 0.45)
    poly(c, [(320, 20), (308, 80), (332, 140), (312, 200), (326, 290)], "HEAD", 2.2)
    line(c, (40, 150), (300, 150), "ACC", 1.6, "6,4")
    text(c, (170, 148), "⊥", "HEAD", "middle", 20, "700")
    text(c, (150, 302), "grain A", "HEAD", "middle", 14, "700")
    text(c, (470, 302), "grain B", "HEAD", "middle", 14, "700")
    text(c, (320, 14), "grain boundary", "HEAD", "middle", 13)
    REG.put("grain-boundary", c, "Grain boundary blocking a dislocation",
            "Two grains with different orientations (schematic): the boundary and the slip plane (dashed) hinder the dislocation (⊥)")


def precip_stages():
    c = Canvas(720, 300)
    for k in range(4):
        ox = 20 + k * 175
        xs = [ox + 40, ox + 90, ox + 140]
        for x in xs:
            circle(c, (x, 215), 9, "ATOM", 1.4, None, "ATOM", 0.6)
        if k == 0:
            line(c, (ox + 10, 120), (ox + 170, 120), "BLUE", 2.2)
            for x in range(ox + 30, ox + 160, 30):
                arrow(c, (x, 96), (x, 114), "PINK", 1.6, 7)
        elif k == 1:
            pathd(c, f"M{ox + 10},120 Q{ox + 90},92 {ox + 170},120", "BLUE", 2.2)
        elif k == 2:
            pathd(c, f"M{ox + 10},120 L{ox + 40},120 A25,25 0 0 1 {ox + 90},120 A25,25 0 0 1 {ox + 140},120 L{ox + 170},120",
                  "BLUE", 2.2)
        else:
            line(c, (ox + 10, 120), (ox + 170, 120), "BLUE", 2.2)
            for x in xs:
                circle(c, (x, 215), 25, "BLUE", 1.2, "3,3")
        labels = ["(a) approach", "(b) sub-critical", "(c) critical", "(d) escape"]
        text(c, (ox + 90, 275), labels[k], "HEAD", "middle", 13, "700")
    REG.put("precip-stages", c, "Dislocation passing precipitate particles",
            "The four stages of a dislocation meeting a row of particles (schematic); the slide labels (c) twice")


def indenters():
    c = Canvas(720, 300)
    circle(c, (130, 130), 60, "BLUE", 1.6, None, "BLUE", 0.25)
    poly(c, [(95, 190), (130, 206), (165, 190)], "HEAD", 1.8)
    line(c, (40, 190), (240, 190), "HEAD", 2.0)
    dim(c, (210, 70), (210, 190), "D", lab_off=(14, 0), anchor="start")
    dim(c, (95, 216), (165, 216), "d", lab_off=(0, 16))
    text(c, (130, 262), "Brinell (HBW)", "HEAD", "middle", 14, "700")
    poly(c, [(330, 40), (390, 40), (360, 130)], "HEAD", 1.8, None, "none", True)
    poly(c, [(338, 190), (382, 190), (360, 208)], "BLUE", 1.8, None, "none", True)
    line(c, (300, 190), (430, 190), "HEAD", 2.0)
    text(c, (400, 84), "136°", "HEAD", "start", 13)
    text(c, (360, 262), "Vickers (HV)", "HEAD", "middle", 14, "700")
    poly(c, [(560, 40), (620, 40), (590, 130)], "HEAD", 1.8, None, "none", True)
    pathd(c, "M575,190 Q590,204 605,190", "BLUE", 1.8)
    line(c, (520, 190), (660, 190), "HEAD", 2.0)
    text(c, (630, 84), "120°", "HEAD", "start", 13)
    dim(c, (640, 190), (640, 204), "h", lab_off=(14, 4), anchor="start")
    text(c, (590, 262), "Rockwell (HR)", "HEAD", "middle", 14, "700")
    REG.put("indenters", c, "Indenters of the Brinell, Vickers and Rockwell tests",
            "Side views of the Brinell ball, the Vickers pyramid and the Rockwell cone, with the dimensions used in the formulas (not to scale)")


def rockwell_steps():
    c = Canvas(720, 300)
    surface = 180
    for k, cx in enumerate((120, 360, 600)):
        line(c, (cx - 80, surface), (cx + 80, surface), "HEAD", 2.0)
        if k == 0:
            tip = 188
        elif k == 1:
            tip = 216
        else:
            tip = 204
            line(c, (cx - 80, 188), (cx + 80, 188), "EDGE", 1.1, "4,4")
        poly(c, [(cx - 22, tip - 70), (cx + 22, tip - 70), (cx, tip)], "HEAD", 1.8, None, "none", True)
        if k == 1:
            dim(c, (cx + 50, surface), (cx + 50, 216), "h" + sub("", "1"), lab_off=(14, 4), anchor="start")
        if k == 2:
            dim(c, (cx + 50, 188), (cx + 50, 204), "h", lab_off=(14, 4), anchor="start")
    text(c, (120, 262), "1. preload", "HEAD", "middle", 13, "700")
    text(c, (360, 262), "2. preload + additional load", "HEAD", "middle", 13, "700")
    text(c, (600, 262), "3. additional load removed", "HEAD", "middle", 13, "700")
    REG.put("rockwell-steps", c, "Three steps of the Rockwell test",
            "Rockwell test: preload, total load, and the depth h that remains after the additional load is removed (schematic)")


def rasters():
    REG.raster("s11-bubble-chart", "Bubble chart of Young's modulus against density",
               "Bubble chart of Young's modulus against density by material family, copied from Session 11 Slide 18", 620)
    REG.raster("s12-strain-hardening-charts", "Yield strength and ductility against percent cold work",
               "Yield strength (left) and ductility (right) against percent cold work, copied from Session 12 Slide 7", 700)
    REG.raster("s12-cuni", "Yield strength and elongation of Cu-Ni alloys",
               "Yield strength (left) and elongation (right) of Cu-Ni alloys against nickel content, copied from Session 12 Slide 9", 640)
    REG.raster("s12-grain-size-plot", "Yield strength against grain size",
               "Yield strength against d to the power -1/2, with the grain size on the top axis, copied from Session 12 Slide 10", 330)
    REG.raster("s12-precipitate-micrographs", "Micrographs of MgZn2 precipitates",
               "Micrographs of MgZn2 precipitates along grain boundaries of an aluminium alloy, copied from Session 12 Slide 13", 460)
    REG.raster("s12-brinell-q-chart", "Brinell load factor chart",
               "Brinell load factor Q for each group of materials, copied from Session 12 Slide 20", 360)
    REG.raster("s12-hardness-tensile", "Brinell hardness against tensile strength",
               "Tensile strength against Brinell hardness for steels, brass and nodular cast iron, copied from Session 12 Slide 30", 330)


def build():
    specimen_geometry()
    curve_regions()
    modulus_types()
    material_curves()
    poisson()
    bend_test()
    shear_test()
    load_unload()
    dislocation_directions()
    ductility_recovery()
    yield_offset()
    toughness()
    resilience()
    true_stress()
    strain_hardening()
    grain_boundary()
    precip_stages()
    indenters()
    rockwell_steps()
    rasters()
    return REG
