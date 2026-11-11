"""Topic 5 figures for Aerospace Materials I: mechanical properties (Sessions 11 and 12).

Every theory figure is a PNG crop of the slides, registered with `REG.raster`. The SVG functions left draw the
problem-sheet figures. Run `python tools/build_topic_pages.py` to write the files to vault/attachments/T5 and
rebuild the page.
"""
import math

from figures.svgkit import (Canvas, Registry, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, text)

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
    m1.axes(c, emax * 1.06, smax * 1.12, "strain Îµ", "Ïƒ (MPa)", ticks(emax * 1.06, 4), ticks(smax * 1.12, 4))
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
    m2.axes(c, ze, zs, "strain Îµ", "Ïƒ (MPa)", ticks(ze, 4), ticks(zs, 4))
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
    dim(c, (390, 222), (406, 222), "Î”l", lab_off=(0, 18))
    dim(c, (200, 120), (200, 200), "d0", lab_off=(-10, 4), anchor="end")
    line(c, (300, 120), (300, 128), "PINK", 2.5)
    line(c, (300, 192), (300, 200), "PINK", 2.5)
    text(c, (310, 118), "Î”d/2", "PINK", "start", 12)
    text(c, (150, 272), "dashed: undeformed", "TEXT", "start", 12)
    text(c, (300, 272), "Î”d &lt; 0: |Î”d| = Î½ Îµ d0", "PINK", "start", 13)
    REG.put("t5-axial-bar", c, "Bar under axial tension",
            "Cylindrical bar under an axial load F: it elongates by Î”l and its diameter shrinks by Î”d (schematic, exaggerated)")


def p5_wire():
    """Problem 5: a stretched wire kept at constant length while it is heated."""
    c = Canvas(640, 280)
    line(c, (110, 70), (530, 70), "HEAD", 3.0)
    arrow(c, (110, 70), (60, 70), "BLUE", 2.2, 10)
    arrow(c, (530, 70), (580, 70), "BLUE", 2.2, 10)
    text(c, (50, 62), "F", "BLUE", "end", 15, "700")
    text(c, (590, 62), "F", "BLUE", "start", 15, "700")
    text(c, (320, 40), "20 Â°C: stretched by F, tensile stress Ïƒ = F/A", "HEAD", "middle", 13, "700")
    text(c, (320, 104), "length l0 = 1 m", "TEXT", "middle", 12)
    for x in (110, 530):
        line(c, (x, 160), (x, 250), "HEAD", 3.0)
    hatch(c, (110, 160), (110, 250), 1)
    hatch(c, (530, 160), (530, 250), -1)
    line(c, (110, 205), (530, 205), "HEAD", 3.0)
    arrow(c, (330, 235), (360, 235), "PINK", 1.8, 8)
    arrow(c, (310, 235), (280, 235), "PINK", 1.8, 8)
    text(c, (320, 150), "40 Â°C: length kept fixed, the expansion Î±Î”T is blocked", "HEAD", "middle", 13, "700")
    text(c, (320, 270), "thermal stress âˆ’E Î± Î”T (compressive) cancels F/A", "PINK", "middle", 12)
    REG.put("t5-p5-wire", c, "Wire stretched and then heated at constant length",
            "Problem 5: the wire is stretched at 20 Â°C and then held at constant length while it is heated to 40 Â°C (schematic)")


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
    m.text(c, 0.0003, sy + 18, f"Ïƒy = {sy:.1f} MPa", "HEAD", "start", 12.5, "700")
    m.text(c, 0.0003, sp - 26, f"Ïƒ = {sp:.1f} MPa", "HEAD", "start", 12.5, "700")
    m.text(c, ep_tot - 0.0003, sp + 18, "Îµ = 0.011", "HEAD", "end", 12.5, "700")
    m.text(c, er + 0.0004, 25, f"Îµp = {er:.5f}", "BLUE", "start", 12.5, "700")
    m.text(c, 0.0062, 190, "unloading: slope E", "BLUE", "start", 12.5, "700")
    m.axes(c, 0.012, 420, "strain Îµ", "Ïƒ (MPa)", [(0.004, "0.004"), (0.008, "0.008"), (0.012, "0.012")], [(100, "100"), (200, "200"), (300, "300"), (400, "400")])
    REG.put("t5-p10-unloading", c, "Problem 10: unloading of the copper wire",
            "Problem 10: loading beyond the yield point and unloading along a line of slope E; the strain that remains is permanent (the shape between the yield point and the loaded point is not given by the statement)")


def brinell_geometry():
    """Problems 14 and 15: the spherical cap left by the ball (exaggerated, not to scale)."""
    c = Canvas(640, 290)
    r, cx, ys = 90, 250, 190
    half = 54
    h = r - math.sqrt(r * r - half * half)
    cy = ys - (r - h)
    pathd(c, f"M {cx - half} {ys} A {r} {r} 0 0 0 {cx + half} {ys} Z", "ACC", 1.6, fill="ACC", opacity=0.35)
    circle(c, (cx, cy), r, "HEAD", 1.8, "7,4")
    line(c, (60, ys), (440, ys), "HEAD", 2.6)
    hatch(c, (60, ys), (440, ys), 1, "EDGE", 10, 9)
    arrow(c, (cx, 8), (cx, cy - r - 2), "BLUE", 2.2, 10)
    text(c, (cx + 12, 22), "P (kgf)", "BLUE", "start", 14, "700")
    xd = cx - r - 26
    line(c, (xd, cy - r), (xd, cy + r), "TEXT", 1.3, head=True)
    line(c, (xd, cy + r), (xd, cy - r), "TEXT", 1.3, head=True)
    for yy in (cy - r, cy + r):
        line(c, (xd - 6, yy), (cx - 40 if yy < cy else cx - 8, yy), "TEXT", 0.9, "3,3")
    text(c, (xd - 8, cy + 5), "D", "TEXT", "end", 14, "700")
    text(c, (cx, cy + 5), "ball", "TEXT", "middle", 13)
    line(c, (cx - half, ys + 26), (cx + half, ys + 26), "PINK", 1.4, head=True)
    line(c, (cx + half, ys + 26), (cx - half, ys + 26), "PINK", 1.4, head=True)
    line(c, (cx - half, ys), (cx - half, ys + 32), "PINK", 1.0, "3,3")
    line(c, (cx + half, ys), (cx + half, ys + 32), "PINK", 1.0, "3,3")
    text(c, (cx, ys + 46), "Di  (diameter of the indentation)", "PINK", "middle", 13, "700")
    line(c, (cx + half + 34, ys), (cx + half + 34, ys + h), "TEXT", 1.4)
    text(c, (cx + half + 42, ys + h / 2 + 5), "h", "TEXT", "start", 14, "700")
    text(c, (440, ys + 18), "surface", "TEXT", "end", 12)
    text(c, (30, 276), "Cap area S = Ï€ D h  with  h = (D âˆ’ âˆš(DÂ² âˆ’ DiÂ²)) / 2   â‡’   HB = P / S", "HEAD", "start", 13, "700")
    REG.put("t5-brinell-geometry", c, "Spherical cap of the Brinell indentation",
            "Brinell test: the cap of height h left by the ball of diameter D (the proportions are exaggerated, not to scale)")


def problems():
    brinell_geometry()
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
                        pts, r["e_mod"], (ey, sy), pts[s["uts_i"]], s["zoom"], s["lin_end"], f"Ïƒy = {sy:.0f} MPa",
                        lin_right=(k == 4))


def rasters():
    REG.raster("s11-energy-force-stress", "From the bonding energy and force to the stress-strain line",
               "The bonding energy, the bonding force, the load against the elongation and the stress against the strain of the elastic zone, as drawn on Session 11 Slide 14, copied from the slide", 560)
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
    REG.raster('specimen-geometry', 'ASTM E8 tensile specimen',
               'Standard tensile specimen for metals (ASTM E8): 50 mm gauge length, 60 mm reduced section, 0.505 in. reduced diameter, 18 mm grip diameter and 10 mm shoulder radius, with the general nomenclature of the specimen below, copied from Session 11 Slide 4', 560)
    REG.raster('curve-regions', 'Stress-strain curve of the tension test',
               'Stress-strain curve with the linear-elastic region, the yield strength point, the 0.2 % offset line, the ultimate tensile strength and the breaking strength, and the specimen at each stage of the test (uniform elastic and plastic deformation, necking, fracture), copied from Session 11 Slide 9', 460)
    REG.raster('bond-force-curves', 'Interatomic force against separation',
               'Interatomic force against separation for a strongly and a weakly bonded material, with the slope (dF/dr) at r0 and the relation E proportional to (dF/dr) at r0, copied from Session 11 Slide 13', 520)
    REG.raster('modulus-types-a', 'Initial, secant and tangent moduli',
               'Non-linear stress-strain curve with the initial modulus, the secant modulus at 2 % strain and a tangent modulus, copied from Session 11 Slide 15', 460)
    REG.raster('modulus-types-b', 'Secant and tangent moduli at a given stress',
               'Secant modulus between the origin and Ïƒ1 and tangent modulus at Ïƒ2, copied from Session 11 Slide 15', 320)
    REG.raster('material-curves', 'Qualitative tensile curves of four material families',
               'Qualitative tensile stress-strain curves of (a) a metal, (b) a thermoplastic above its glass transition Tg, (c) an elastomer and (d) ceramics, glasses and concrete, copied from Session 11 Slide 16', 640)
    REG.raster('poisson-a', 'Isotropic block under uniaxial tension',
               'Isotropic block under a uniaxial stress Ïƒz: axial elongation Î”lz and lateral contraction Î”lx, copied from Session 11 Slide 19', 340)
    REG.raster('poisson-b', 'Extension and constriction',
               'Axial extension with transverse constriction, and the changes Î”y (axial) and Î”x (transverse), copied from Session 11 Slide 19', 360)
    REG.raster('bend-test', 'Three-point bend test',
               'Three-point bend test with the load F, the reactions F/2, the span L, the thickness h, the width b and the point of fracture, copied from Session 11 Slide 6', 480)
    REG.raster('shear-test', 'Shear test',
               'Shear test: the top face slides by a over the height h, and Î¸ is the angle of shear, copied from Session 11 Slide 7', 320)
    REG.raster('load-unload', 'Loading into the plastic zone and unloading',
               'Elastic and plastic zones: loading past the yield strength Ïƒy to the point P and unloading parallel to the elastic line, with the 0.002 strain offset, copied from Session 11 Slide 21', 300)
    REG.raster('dislocation-directions', 'Compact and non-compact FCC directions',
               'Slip of a dislocation along the compact FCC [110] direction (b = 2R, Eb proportional to 4RÂ²) and the non-compact FCC [100] direction (b = 2âˆš2 R, Eb proportional to 8RÂ²), copied from Session 11 Slide 24', 720)
    REG.raster('yield-offset-a', 'Conventional yield strength (0.2 % offset)',
               'Conventional yield strength: the line parallel to the elastic part from a strain of 0.002 meets the curve at Ïƒy, with Ïƒy = Ïƒ (0.2 % of Îµ), copied from Session 11 Slide 28', 420)
    REG.raster('yield-offset-b', 'Discontinuous yield point',
               'Discontinuous yield with the upper and lower yield points, and Ïƒy = (Ïƒmax + Ïƒmin)/2, copied from Session 11 Slide 28', 380)
    REG.raster('ductility-recovery', 'Elastic recovery after fracture',
               'Plastic deformation at break, the uniform deformation (UD), the strain to fracture (StF), the 0.2 % offset and the elastic recovery after fracture, copied from Session 11 Slide 32', 520)
    REG.raster('toughness', 'Three materials with different toughness',
               'Stress-strain curves of a high-strength, low-ductility, low-toughness material, a high-strength, high-ductility, high-toughness material and a low-strength, high-ductility, low-toughness material, copied from Session 11 Slide 34', 520)
    REG.raster('resilience', 'Modulus of resilience',
               'Modulus of resilience Ur as the area under the stress-strain curve up to the yield point, with the 0.002 offset line, copied from Session 11 Slide 35', 420)
    REG.raster('true-stress', 'Engineering, true and corrected curves',
               'Engineering and true stress-strain curves, with the maxima M and Mâ€² and the true curve corrected for the necking, copied from Session 11 Slide 37', 380)
    REG.raster('strain-hardening', 'Strain hardening by successive cold work',
               'Stress-strain curves after increasing percent strain hardening: the higher the cold work, the higher R and Ïƒy and the lower the ductility, copied from Session 12 Slide 5', 460)
    REG.raster('grain-boundary', 'Grain boundary blocking a dislocation',
               'Grain A and grain B with different orientations, the grain boundary, the slip plane and an edge dislocation stopped at the boundary, copied from Session 12 Slide 10', 500)
    REG.raster('precip-stages', 'Dislocation passing precipitate particles',
               'A dislocation meeting a row of particles: a) approach, with the force Ï„b per unit length and the spacing L, b) sub-critical, c) critical, with the force Ï„bL, and the escape situation (also printed as c), copied from Session 12 Slide 12', 480)
    REG.raster('indenters-a', 'Brinell ball indenter',
               'Brinell test: ball of diameter D under the load P and the indentation of diameter Di, copied from Session 12 Slide 19', 220)
    REG.raster('indenters-b', 'Vickers pyramid indenter',
               'Vickers test: square-based diamond pyramid with 136Â° between faces, and the diagonals d1 and d2 of the impression, copied from Session 12 Slide 26', 460)
    REG.raster('indenters-c', 'Rockwell indenters',
               'Rockwell indenters: diamond cone of 120Â° for scales A, C and D (60, 150 and 100 kgf) and steel ball of 1/16 to 1/8 in. for scales B, F and G (100, 60 and 150 kgf), side view and impression, with the depth t; the labels are in Portuguese on the slide (Cone de Diamante: diamond cone, Esfera de aÃ§o: steel ball, Lateral: side view, ImpressÃ£o: impression), copied from Session 12 Slide 22', 620)
    REG.raster('rockwell-steps', 'Three steps of the Rockwell test',
               'Rockwell test: 1, preload; 2, preload plus additional load (total load), with the maximum indentation depth h1; 3, additional load removed and the lasting impression depth h read on the depth scale, copied from Session 12 Slide 23', 700)


def build():
    rasters()
    problems()
    return REG
