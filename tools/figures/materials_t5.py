"""Topic 5 figures for Aerospace Materials I: mechanical properties (Sessions 11 and 12).

Most figures are schematic redraws of the slides: they keep the labels and the qualitative shape of the curves,
and they are not to scale. The charts whose values cannot be redrawn faithfully (the cold-work, Cu-Ni, grain-size,
Brinell, micrograph and hardness-strength charts) are copied from the slides as PNG crops, registered with
`REG.raster`. Run `python tools/build_topic_pages.py` to write the SVG files to vault/attachments/T5 and rebuild
the page.
"""
import math

from figures.svgkit import (Canvas, Registry, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, sub, text)

REG = Registry("T5")


class M:
    """Data coordinates mapped to pixels: the origin is at (x0, y0), sx and sy are pixels per unit, y points up."""

    def __init__(self, x0, y0, sx, sy):
        self.x0, self.y0, self.sx, self.sy = x0, y0, sx, sy

    def p(self, x, y):
        return (self.x0 + x * self.sx, self.y0 - y * self.sy)

    def axes(self, c, xmax, ymax, xl, yl, xt=(), yt=(), xl_dy=38):
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
        text(c, (x, y + xl_dy), xl, "HEAD", "end", 13, "700")
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


def bond_force_curves():
    c = Canvas(640, 330)
    m = M(130, 150, 170, 62)

    def force(d, a):
        return lambda x: 2 * d * a * (math.exp(-a * x) - math.exp(-2 * a * x))

    def clip(fn):
        return lambda x: fn(x) if -2.1 <= fn(x) <= 1.9 else None

    line(c, m.p(-0.6, 0), m.p(2.9, 0), "EDGE", 1.3, head=True)
    line(c, m.p(-0.6, -2.2), m.p(-0.6, 1.9), "EDGE", 1.3, head=True)
    text(c, m.p(2.9, 0), "separation r", "HEAD", "end", 13, "700", 0, 24)
    text(c, m.p(-0.6, 1.9), "force F", "HEAD", "start", 13, "700", 8, 4)
    for d, col in ((1.6, "PINK"), (0.8, "BLUE")):
        a = 1.4
        m.poly(c, sample(clip(force(d, a)), -0.45, 2.9, 260), col, 2.4)
        s = 2 * d * a * a
        m.poly(c, [(-0.28, -0.28 * s), (0.28, 0.28 * s)], col, 1.4, "5,4")
    line(c, m.p(0, 0.08), m.p(0, -0.08), "EDGE", 1.2)
    text(c, m.p(0.12, 0), "r0", "HEAD", "start", 13, "400", 0, 18)
    m.text(c, 1.2, 1.35, "strongly bonded", "PINK", "start", 13, "700")
    m.text(c, 1.2, -0.55, "weakly bonded", "BLUE", "start", 13, "700")
    m.text(c, 0.9, -1.35, "dashed: slope (dF/dr) at r0", "TEXT", "start", 12)
    m.text(c, 0.9, -1.75, "steeper slope = larger E", "TEXT", "start", 12)
    REG.put("bond-force-curves", c, "Interatomic force against separation for a strong and a weak bond",
            "Interatomic force against separation for a strongly and a weakly bonded material: E is proportional to the slope at r0 (schematic)")


# --------------------------------------------------------------------------- problem sheet (Problems T5)
def nice_step(vmax, n=5):
    raw = vmax / n
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            return m * mag
    return 10 * mag


def ticks(vmax, n=5):
    step = nice_step(vmax, n)
    k, out = 1, []
    while k * step <= vmax * 1.001:
        out.append((k * step, f"{k * step:g}"))
        k += 1
    return out


def clip_x(pts, xmax):
    """Polyline points with x <= xmax, ending exactly at xmax (linear interpolation on the crossing segment)."""
    out = []
    for i, (x, y) in enumerate(pts):
        if x <= xmax:
            out.append((x, y))
        else:
            x0, y0 = pts[i - 1]
            out.append((xmax, y0 + (y - y0) * (xmax - x0) / (x - x0)))
            break
    return out


def tensile_problem(name, title, caption, pts, e_mod, yield_pt, uts_pt, zoom, lin_end, yield_label, fracture_label="fracture",
                    lin_right=False):
    """Engineering stress-strain curve built from the sheet data: full curve (left) and zoom on the elastic
    part with the Young's modulus line and the 0.2 % offset line (right). `pts` includes (0, 0)."""
    c = Canvas(780, 360)
    emax, smax = pts[-1][0], max(p[1] for p in pts)
    m1 = M(70, 300, 300 / (emax * 1.06), 230 / (smax * 1.12))
    m1.axes(c, emax * 1.06, smax * 1.12, "strain ε", "σ (MPa)", ticks(emax * 1.06, 4), ticks(smax * 1.12, 4))
    m1.poly(c, pts, "ACC", 2.2)
    for p in pts[1:]:
        m1.dot(c, p[0], p[1], "HEAD", "HEAD", 2.4)
    m1.dot(c, uts_pt[0], uts_pt[1], "HEAD", "BLUE", 5)
    m1.text(c, uts_pt[0], uts_pt[1] + smax * 0.07, "UTS", "BLUE", "middle", 12.5, "700")
    m1.dot(c, pts[-1][0], pts[-1][1], "HEAD", "PINK", 5)
    m1.text(c, pts[-1][0], pts[-1][1] - smax * 0.09, fracture_label, "PINK", "end", 12.5, "700")
    ze, zs = zoom
    m1.poly(c, [(0, 0), (ze, 0), (ze, zs), (0, zs), (0, 0)], "EDGE", 1.0, "3,3")
    text(c, (70, 24), "full curve", "HEAD", "start", 13, "700")
    m2 = M(450, 300, 270 / ze, 230 / zs)
    m2.axes(c, ze, zs, "strain ε", "σ (MPa)", ticks(ze, 4), ticks(zs, 4))
    zp = clip_x(pts, ze)
    m2.poly(c, zp, "ACC", 2.2)
    for p in zp[1:]:
        m2.dot(c, p[0], p[1], "HEAD", "HEAD", 2.6)
    m2.poly(c, [(0, 0), (lin_end, e_mod * lin_end)], "GREEN", 1.5, "6,4")
    off_end = yield_pt[0] + 0.0006
    m2.poly(c, [(0.002, 0), (off_end, e_mod * (off_end - 0.002))], "BLUE", 1.5, "6,4")
    m2.dot(c, yield_pt[0], yield_pt[1], "HEAD", "HEAD", 5)
    m2.text(c, yield_pt[0] + ze * 0.03, yield_pt[1] - zs * 0.08, yield_label, "HEAD", "start", 12.5, "700")
    if lin_right:
        m2.text(c, lin_end + ze * 0.02, e_mod * lin_end + zs * 0.03, "E (elastic line)", "GREEN", "start", 12)
    else:
        m2.text(c, lin_end, e_mod * lin_end + zs * 0.03, "E (elastic line)", "GREEN", "end", 12)
    m2.text(c, 0.002 + 0.08 * zs / e_mod + ze * 0.02, zs * 0.08, "0.2 % offset", "BLUE", "start", 12)
    text(c, (450, 24), "zoom on the elastic part", "HEAD", "start", 13, "700")
    REG.put(name, c, title, caption)


G = 9.81  # m/s2, used to turn the kilograms of the sheet into newtons

# Data of the four tabulated tensile tests of Problems T5_MechanicalProperties.pdf (the first point of each is (0, 0)).
SHEET = {
    1: dict(d0=12.8, l0=12.5, n_fit=5,
            force=[x * 100.0 for x in (127, 254, 381, 508, 762, 891, 927, 1025, 1078, 1194, 1283, 1497, 1590, 1604, 1595, 1515, 1247)],
            dl=[0.006, 0.012, 0.019, 0.025, 0.038, 0.051, 0.063, 0.095, 0.127, 0.190, 0.254, 0.508, 0.762, 0.889, 1.016, 1.270, 1.460]),
    2: dict(d0=15.0, l0=50.0, n_fit=3,
            force=[x * 1000.0 for x in (70, 120, 150, 160, 170, 200, 220, 233, 233, 220)],
            dl=[0.25, 0.4, 0.5, 0.6, 0.75, 1.75, 3.00, 5.00, 6.50, 8.00]),
    3: dict(d0=13.0, l0=5.148, n_fit=4,
            force=[k * G for k in (500, 1500, 2500, 3500, 3750, 3950, 4000, 4000, 3600)],
            dl=[round(x - 5.148, 3) for x in (5.151, 5.156, 5.161, 5.166, 5.225, 5.354, 5.457, 5.560, 5.676)]),
    4: dict(d0=None, l0=63.50, n_fit=5, area=3.2 * 19.1,
            force=[1380.0, 2780.0, 5630.0, 7430.0, 8140.0, 9870.0, 12850.0, 14100.0, 14300.0, 13830.0, 12500.0],
            dl=[round(x - 63.50, 2) for x in (63.53, 63.58, 63.63, 63.70, 63.75, 64.14, 65.41, 66.68, 67.95, 69.22, 70.49)]),
}


def tensile_test(k):
    """Engineering stress and strain of test k, plus E (least squares through the origin on the first n_fit
    points) and the 0.2 % offset yield point."""
    d = SHEET[k]
    a0 = d["area"] if d.get("area") else math.pi * d["d0"] ** 2 / 4
    eps = [0.0] + [x / d["l0"] for x in d["dl"]]
    sig = [0.0] + [x / a0 for x in d["force"]]
    n = d["n_fit"]
    e_mod = sum(e * s for e, s in zip(eps[1:n + 1], sig[1:n + 1])) / sum(e * e for e in eps[1:n + 1])
    return dict(a0=a0, l0=d["l0"], eps=eps, sig=sig, e_mod=e_mod, n_fit=n, yield_pt=offset_yield(eps, sig, e_mod))


def offset_yield(eps, sig, e_mod, off=0.002):
    """Intersection of the polyline with the offset line sigma = E (eps - off): (eps, sigma, segment index)."""
    for i in range(len(eps) - 1):
        f0 = sig[i] - e_mod * (eps[i] - off)
        f1 = sig[i + 1] - e_mod * (eps[i + 1] - off)
        if f0 > 0 >= f1:
            t = f0 / (f0 - f1)
            return eps[i] + t * (eps[i + 1] - eps[i]), sig[i] + t * (sig[i + 1] - sig[i]), i
    raise ValueError("no intersection")


def axial_bar():
    """Cylindrical bar under tension: elongation along the axis and contraction of the diameter (Problems 9 and 11)."""
    c = Canvas(640, 300)
    rect(c, 150, 120, 240, 80, "EDGE", 1.3, "5,4")
    rect(c, 150, 128, 256, 64, "HEAD", 2.0)
    arrow(c, (406, 160), (470, 160), "BLUE", 2.2, 10)
    arrow(c, (150, 160), (86, 160), "BLUE", 2.2, 10)
    text(c, (488, 165), "F", "BLUE", "start", 15, "700")
    text(c, (70, 165), "F", "BLUE", "end", 15, "700")
    dim(c, (150, 98), (390, 98), "l0 (initial length)", lab_off=(0, -8))
    dim(c, (390, 222), (406, 222), "Δl", lab_off=(0, 18))
    dim(c, (200, 120), (200, 200), "d0", lab_off=(-10, 4), anchor="end")
    line(c, (300, 120), (300, 128), "PINK", 2.5)
    line(c, (300, 192), (300, 200), "PINK", 2.5)
    text(c, (310, 118), "Δd/2", "PINK", "start", 12)
    text(c, (150, 272), "dashed: undeformed", "TEXT", "start", 12)
    text(c, (300, 272), "Δd < 0: |Δd| = ν ε d0", "PINK", "start", 13)
    REG.put("t5-axial-bar", c, "Bar under axial tension",
            "Cylindrical bar under an axial load F: it elongates by Δl and its diameter shrinks by Δd (schematic, exaggerated)")


def p5_wire():
    """Problem 5: a stretched wire kept at constant length while it is heated."""
    c = Canvas(640, 280)
    line(c, (110, 70), (530, 70), "HEAD", 3.0)
    arrow(c, (110, 70), (60, 70), "BLUE", 2.2, 10)
    arrow(c, (530, 70), (580, 70), "BLUE", 2.2, 10)
    text(c, (50, 62), "F", "BLUE", "end", 15, "700")
    text(c, (590, 62), "F", "BLUE", "start", 15, "700")
    text(c, (320, 40), "20 °C: stretched by F, tensile stress σ = F/A", "HEAD", "middle", 13, "700")
    text(c, (320, 104), "length l0 = 1 m", "TEXT", "middle", 12)
    for x in (110, 530):
        line(c, (x, 160), (x, 250), "HEAD", 3.0)
    hatch(c, (110, 160), (110, 250), 1)
    hatch(c, (530, 160), (530, 250), -1)
    line(c, (110, 205), (530, 205), "HEAD", 3.0)
    arrow(c, (330, 235), (360, 235), "PINK", 1.8, 8)
    arrow(c, (310, 235), (280, 235), "PINK", 1.8, 8)
    text(c, (320, 150), "40 °C: length kept fixed, the expansion αΔT is blocked", "HEAD", "middle", 13, "700")
    text(c, (320, 270), "thermal stress −E α ΔT (compressive) cancels F/A", "PINK", "middle", 12)
    REG.put("t5-p5-wire", c, "Wire stretched and then heated at constant length",
            "Problem 5: the wire is stretched at 20 °C and then held at constant length while it is heated to 40 °C (schematic)")


def p10_unloading():
    c = Canvas(640, 360)
    a = math.pi * 0.5 ** 2
    sy, sp, e_mod, ep_tot = 15.3 * G / a, 29.6 * G / a, 110000.0, 0.011
    ey, er = sy / e_mod, ep_tot - sp / e_mod
    m = M(70, 310, 520 / 0.012, 250 / 420)
    m.poly(c, [(0, 0), (ey, sy), (ep_tot, sp)], "ACC", 2.4)
    m.poly(c, [(ep_tot, sp), (er, 0)], "BLUE", 1.8, "6,4")
    m.guide(c, (0, sy), (ey, sy))
    m.guide(c, (0, sp), (ep_tot, sp))
    m.guide(c, (ep_tot, 0), (ep_tot, sp))
    m.dot(c, ey, sy, "HEAD", "HEAD", 4)
    m.dot(c, ep_tot, sp, "HEAD", "HEAD", 4)
    m.dot(c, er, 0, "HEAD", "HEAD", 4)
    m.text(c, 0.0003, sy + 18, f"σy = {sy:.1f} MPa", "HEAD", "start", 12.5, "700")
    m.text(c, 0.0003, sp - 26, f"σ = {sp:.1f} MPa", "HEAD", "start", 12.5, "700")
    m.text(c, ep_tot - 0.0003, sp + 18, "ε = 0.011", "HEAD", "end", 12.5, "700")
    m.text(c, er + 0.0004, 25, f"εp = {er:.5f}", "BLUE", "start", 12.5, "700")
    m.text(c, 0.0062, 190, "unloading: slope E", "BLUE", "start", 12.5, "700")
    m.axes(c, 0.012, 420, "strain ε", "σ (MPa)", [(0.004, "0.004"), (0.008, "0.008"), (0.012, "0.012")], [(100, "100"), (200, "200"), (300, "300"), (400, "400")])
    REG.put("t5-p10-unloading", c, "Problem 10: unloading of the copper wire",
            "Problem 10: loading beyond the yield point and unloading along a line of slope E; the strain that remains is permanent (the shape between the yield point and the loaded point is not given by the statement)")


def problems():
    REG.raster("t5-p7-chart", "Problem 7: stress-strain curve of the replacement cable",
               "Problem 7: stress-strain curve of the replacement cable, copied from the sheet (Problems T5_MechanicalProperties.pdf, page 3)", 640)
    axial_bar()
    p5_wire()
    p10_unloading()
    spec = {1: dict(zoom=(0.012, 900), lin_end=0.0035, uts_i=14),
            2: dict(zoom=(0.02, 1100), lin_end=0.011, uts_i=8),
            3: dict(zoom=(0.012, 300), lin_end=0.0036, uts_i=7),
            4: dict(zoom=(0.012, 180), lin_end=0.0045, uts_i=9)}
    for k, s in spec.items():
        r = tensile_test(k)
        pts = list(zip(r["eps"], r["sig"]))
        ey, sy, _ = r["yield_pt"]
        tensile_problem(f"t5-p{k}-curve", f"Problem {k}: engineering stress-strain curve from the table",
                        f"Problem {k}: engineering stress-strain curve built from the data of the sheet (every dot is a table row), "
                        "with the elastic line and the 0.2 % offset construction",
                        pts, r["e_mod"], (ey, sy), pts[s["uts_i"]], s["zoom"], s["lin_end"], f"σy = {sy:.0f} MPa",
                        lin_right=(k == 4))


def specimen_geometry():
    c = Canvas(760, 250)
    pts = [(40, 80), (200, 80), (240, 97), (480, 97), (520, 80), (720, 80), (720, 150), (520, 150),
           (480, 133), (240, 133), (200, 150), (40, 150)]
    poly(c, pts, "HEAD", 1.8, None, "none", True)
    dim(c, (290, 168), (430, 168), "gauge length 50 mm", lab_off=(0, -10))
    dim(c, (240, 200), (480, 200), "reduced section 60 mm", lab_off=(0, -10))
    dim(c, (70, 80), (70, 150), "18 mm", lab_off=(12, 4), anchor="start")
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
    line(c, m.p(0.0025, 250), m.p(0.0085, 340), "GREEN", 1.2)
    m.text(c, 0.009, 330, "elastic zone (σ &lt; σy)", "GREEN", "start", 12, "700")
    m.text(c, 0.03, 150, "plastic zone (" + "σ &gt; " + sub("σ", "y") + ")", "PINK", "middle", 13, "700")
    m.text(c, 0.062, 825, "tensile strength (UTS)")
    m.text(c, 0.113, 545, "fracture stress")
    m.text(c, 0.0615, 30, "uniform deformation", "HEAD", "start", 12)
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
    m.text(c, 0.0005, 1420, "initial E (ε &lt; 0.5 %)", "BLUE")
    m.text(c, 0.0268, 2160, "secant E", "GREEN", "end")
    m.text(c, 0.031, 2160, "tangent E at " + sub("σ", "2"), "PINK")
    m.text(c, 0.0207, 1390, sub("σ", "1"))
    m.text(c, 0.0357, 1850, sub("σ", "2"))
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
        m.axes(c, 1.0, 1.0, "ε", "σ", xl_dy=16)
    REG.put("material-curves", c, "Qualitative tensile curves of four material families",
            "Qualitative tensile curves of a metal, a thermoplastic above its glass transition, an elastomer and a ceramic, as on the slide")


def poisson():
    c = Canvas(640, 330)
    rect(c, 70, 90, 120, 170, "EDGE", 1.4, "4,4")
    text(c, (130, 286), "before load", "TEXT", "middle", 13)
    rect(c, 340, 80, 120, 170, "EDGE", 1.2, "4,4")
    rect(c, 348, 67, 104, 196, "HEAD", 1.8)
    text(c, (400, 322), "under axial tension", "TEXT", "middle", 13)
    arrow(c, (400, 30), (400, 62), "BLUE", 1.8, 9)
    arrow(c, (400, 268), (400, 294), "BLUE", 1.8, 9)
    text(c, (414, 44), sub("σ", "z"), "BLUE", "start", 14)
    arrow(c, (316, 165), (344, 165), "PINK", 1.8, 8)
    arrow(c, (484, 165), (456, 165), "PINK", 1.8, 8)
    text(c, (300, 150), "Δl (lateral)/2", "PINK", "end", 13)
    text(c, (474, 100), "Δl (axial)/2", "BLUE", "start", 13)
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
    c = Canvas(640, 360)
    m = M(70, 310, 520 / 0.02, 260 / 700)
    m.poly(c, [(0, 0), (0.005, 500)] + [(0.005 + 0.007 * i / 40, 500 + 150 * i / 40) for i in range(1, 41)],
           "HEAD", 2.4)
    m.poly(c, [(0.012, 650), (0.0055, 0)], "ACC", 2.2, "6,4")
    m.dot(c, 0.005, 500)
    m.dot(c, 0.0055, 0)
    m.dot(c, 0.012, 650, "HEAD", "ACC")
    m.guide(c, (0, 500), (0.005, 500))
    m.text(c, 0.0052, 470, sub("σ", "y"))
    m.text(c, 0.0125, 660, "load at P", "HEAD")
    m.text(c, 0.0125, 240, "unloading (slope E)", "ACC")
    m.text(c, 0.0068, 45, "permanent strain " + sub("ε", "p"), "HEAD")
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
    m.text(c, ef - 0.002, 42, "plastic elongation " + sub("ε", "p") + " (%EL)", "HEAD", "end", 12)
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
    m1.text(c, ey + 0.0005, sy - 55, sub("σ", "y"))
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
    m.text(c, 0.02, 905, "high strength, low ductility, low toughness", "PINK", "start", 12.5, "700")
    m.text(c, 0.03, 560, "high strength, high ductility, high toughness", "GREEN", "start", 12.5, "700")
    m.text(c, 0.075, 380, "low strength, high ductility, low toughness", "BLUE", "start", 12.5, "700")
    m.axes(c, 0.12, 980, "strain ε", "σ (MPa)",
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
    m.text(c, 0.0047, 535, sub("σ", "y"), "HEAD", "end")
    m.text(c, 0.0065, 80, sub("ε", "y") + " = " + sub("σ", "y") + " / E", "HEAD", "start", 12)
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
    m.text(c, 0.0585, 735, "M", "HEAD", "end", 13, "700")
    m.text(c, 0.0575, 880, "M′", "HEAD", "end", 13, "700")
    m.text(c, 0.07, 1000, "true curve", "BLUE", "start", 13, "700")
    m.text(c, 0.07, 620, "engineering curve", "ACC", "start", 13, "700")
    m.axes(c, 0.12, 1100, "strain ε", "σ (MPa)",
           xt=[(0.02, "0.02"), (0.04, "0.04"), (0.06, "0.06"), (0.08, "0.08"), (0.10, "0.10"), (0.12, "0.12")],
           yt=[(200, "200"), (400, "400"), (600, "600"), (800, "800"), (1000, "1000")])
    REG.put("true-stress", c, "Engineering and true stress-strain curves",
            "Engineering curve (orange) and true curve (blue) up to the maximum, M and M′; schematic, not to scale")


def strain_hardening():
    c = Canvas(640, 350)
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
        for i in range(-12, 28):
            for j in range(-12, 28):
                x = ox + a * (i * cs - j * sn)
                y = oy + a * (i * sn + j * cs)
                if keep(x, y):
                    out.append((x, y))
        return out

    for x, y in grid(40, 40, 0.0, lambda x, y: 40 <= x <= 300 and 30 <= y <= 280 and math.hypot(x - 170, y - 150) > 15):
        circle(c, (x, y), 7, "ATOM", 1.2, None, "ATOM", 0.45)
    for x, y in grid(340, 40, math.radians(25), lambda x, y: 340 <= x <= 620 and 30 <= y <= 280):
        circle(c, (x, y), 7, "ATOM", 1.2, None, "ATOM", 0.45)
    poly(c, [(320, 20), (308, 80), (332, 140), (312, 200), (326, 290)], "HEAD", 2.2)
    line(c, (40, 150), (300, 150), "ACC", 1.6, "6,4")
    text(c, (170, 157), "⊥", "HEAD", "middle", 24, "700")
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
            circle(c, (x, 130), 9, "ATOM", 1.4, None, "ATOM", 0.6)
        if k == 0:
            line(c, (ox + 10, 200), (ox + 170, 200), "BLUE", 2.2)
            for x in range(ox + 30, ox + 160, 30):
                arrow(c, (x, 234), (x, 206), "PINK", 1.6, 7)
            dim(c, (xs[0], 100), (xs[1], 100), "L", lab_off=(0, -6))
            text(c, (ox + 90, 254), "force τb per unit length", "PINK", "middle", 11)
        elif k == 1:
            pathd(c, f"M{ox + 10},160 L{ox + 28},160 L{xs[0]},138 Q{ox + 65},112 {xs[1]},138 Q{ox + 115},112 {xs[2]},138 "
                     f"L{ox + 152},160 L{ox + 170},160", "BLUE", 2.2)
        elif k == 2:
            pathd(c, f"M{ox + 10},160 L{ox + 28},160 L{xs[0]},138 A25,25 0 0 1 {xs[1]},138 A25,25 0 0 1 {xs[2]},138 "
                     f"L{ox + 152},160 L{ox + 170},160", "BLUE", 2.2)
        else:
            line(c, (ox + 10, 70), (ox + 170, 70), "BLUE", 2.2)
            for x in xs:
                circle(c, (x, 130), 17, "BLUE", 1.4, "3,3")
        labels = ["(a) approach", "(b) sub-critical", "(c) critical", "(d) escape"]
        text(c, (ox + 90, 284), labels[k], "HEAD", "middle", 13, "700")
    REG.put("precip-stages", c, "Dislocation passing precipitate particles",
            "The four stages of a dislocation meeting a row of particles (schematic); the slide labels (c) twice")


def indenters():
    c = Canvas(720, 300)
    circle(c, (130, 130), 60, "BLUE", 1.6, None, "BLUE", 0.25)
    pathd(c, "M95,190 Q130,214 165,190", "HEAD", 1.8)
    line(c, (40, 190), (240, 190), "HEAD", 2.0)
    dim(c, (210, 70), (210, 190), "D", lab_off=(14, 0), anchor="start")
    dim(c, (95, 216), (165, 216), "d", lab_off=(0, 16))
    text(c, (130, 262), "Brinell (HBW)", "HEAD", "middle", 14, "700")
    poly(c, [(330, 40), (390, 40), (360, 130)], "HEAD", 1.8, None, "none", True)
    poly(c, [(338, 190), (382, 190), (360, 208)], "BLUE", 1.8, None, "none", True)
    line(c, (300, 190), (430, 190), "HEAD", 2.0)
    text(c, (400, 84), "136°", "HEAD", "start", 13)
    dim(c, (338, 218), (382, 218), "d", lab_off=(0, 16))
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
    bond_force_curves()
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
    problems()
    return REG
