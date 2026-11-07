"""Topic 7 figures for Aerospace Materials I: magnetic and thermal properties (Session 15).

Schematic redraws of the slides (labels and qualitative shape kept, not to scale) plus PNG crops of the slides
for the charts and tables whose values cannot be redrawn faithfully (registered with `REG.raster`; the crops are
200 DPI clips of the PDF pages, written once to vault/attachments/T7). Run `python tools/build_topic_pages.py`
to write the SVG files to vault/attachments/T7.
"""
import math

from figures.svgkit import (Canvas, Registry, arrow, circle, dim, dot, line, pathd, poly, rect, sub, text)

REG = Registry("T7")


# ---------------------------------------------------------------- small helpers

def txt(c, x, y, s, col="TEXT", anchor="middle", size=13, weight="400"):
    text(c, (x, y), s, col, anchor, size, weight)


def axes(c, o, xend, yend, xl=None, yl=None, xdy=24):
    line(c, o, (xend, o[1]), "EDGE", 1.3, head=True)
    line(c, o, (o[0], yend), "EDGE", 1.3, head=True)
    if xl:
        text(c, (xend, o[1] + xdy), xl, "HEAD", "end", 13, "700")
    if yl:
        text(c, (o[0] + 8, yend + 4), yl, "HEAD", "start", 13, "700")


def dip(c, x, y, ang, length, col="BLUE", w=2.2):
    """Dipole arrow centred at (x, y); ang in degrees measured clockwise from 'up'."""
    a = math.radians(ang)
    ux, uy = math.sin(a), -math.cos(a)
    tail = (x - ux * length / 2, y - uy * length / 2)
    head = (x + ux * length / 2, y + uy * length / 2)
    arrow(c, tail, head, col, w, 8)


# ---------------------------------------------------------------- origin of magnetism (S3)

def orbital_spin():
    c = Canvas(660, 300)
    txt(c, 170, 28, "Orbital magnetic moment", "HEAD", "middle", 14, "700")
    circle(c, (170, 150), 62, "EDGE", 1.4, "5,4")
    dot(c, (170, 150), 5, "ATOM", "ATOM")
    dot(c, (232, 150), 6, "BLUE", "BLUE")
    txt(c, 246, 130, "electron", "BLUE", "start", 12)
    txt(c, 160, 168, "nucleus", "TEXT", "end", 12)
    arrow(c, (170, 150), (170, 50), "PINK", 2.6, 11)
    txt(c, 180, 62, sub("m", "l") + " " + sub("μ", "B"), "PINK", "start", 14, "700")
    txt(c, 170, 250, "moment from the motion of the charge", "TEXT", "middle", 12)
    txt(c, 170, 268, "around the nucleus", "TEXT", "middle", 12)
    txt(c, 490, 28, "Spin magnetic moment", "HEAD", "middle", 14, "700")
    circle(c, (490, 150), 34, "BLUE", 1.8, None, "BLUE", 0.15)
    pathd(c, "M470,150 A20,20 0 1 1 490,170", "BLUE", 2.0)
    arrow(c, (490, 150), (490, 50), "PINK", 2.6, 11)
    txt(c, 500, 62, "±" + sub("μ", "B"), "PINK", "start", 14, "700")
    txt(c, 490, 250, "moment from the spin of the electron", "TEXT", "middle", 12)
    txt(c, 490, 268, "(two possible directions)", "TEXT", "middle", 12)
    txt(c, 330, 292, sub("μ", "B") + " = 9.27×" + sub("10", "−24", True) + " A·m² (Bohr magneton)", "HEAD", "middle", 13, "700")
    REG.put("orbital-spin", c, "Orbital and spin magnetic moments of an electron",
            "The magnetic moment of an atom is the sum of the orbital moments (ml μB) and the spin moments (±μB) of its electrons; μB is the Bohr magneton (schematic)")


# ---------------------------------------------------------------- types of magnetism (S5-S13)

def dipole_orderings():
    c = Canvas(770, 400)
    xs = [150, 290, 430, 570, 710]
    names = ["Diamagnetic", "Paramagnetic", "Ferromagnetic", "Antiferromagnetic", "Ferrimagnetic"]
    notes = [("induced dipoles,", "opposite to the field"), ("permanent dipoles,", "aligned by the field"),
             ("permanent dipoles,", "aligned without a field"), ("equal dipoles,", "antiparallel: no net moment"),
             ("unequal dipoles,", "antiparallel: net moment")]
    txt(c, 40, 122, "H = 0", "HEAD", "middle", 13, "700")
    txt(c, 40, 270, "H applied", "HEAD", "middle", 13, "700")
    arrow(c, (40, 345), (40, 290), "GREEN", 2.6, 10)
    txt(c, 56, 322, "H", "GREEN", "start", 14, "700")
    for k, x in enumerate(xs):
        txt(c, x, 34, names[k], "HEAD", "middle", 13, "700")
        offs = (-45, -15, 15, 45)
        for j, dx in enumerate(offs):
            xx = x + dx
            if k == 0:
                circle(c, (xx, 120), 7, "EDGE", 1.2, "3,3")
                dip(c, xx, 270, 180, 18, "BLUE")
            elif k == 1:
                dip(c, xx, 120, (40, -130, 150, -60)[j], 26, "BLUE")
                dip(c, xx, 270, (14, -10, 20, -16)[j], 26, "BLUE")
            elif k == 2:
                dip(c, xx, 120, 0, 30, "PINK")
                dip(c, xx, 270, 0, 30, "PINK")
            elif k == 3:
                dip(c, xx, 120, 0 if j % 2 == 0 else 180, 30, "ATOM")
                dip(c, xx, 270, 0 if j % 2 == 0 else 180, 30, "ATOM")
            else:
                dip(c, xx, 120, 0 if j % 2 == 0 else 180, 40 if j % 2 == 0 else 18, "GREEN")
                dip(c, xx, 270, 0 if j % 2 == 0 else 180, 40 if j % 2 == 0 else 18, "GREEN")
        txt(c, x, 336, notes[k][0], "TEXT", "middle", 11)
        txt(c, x, 352, notes[k][1], "TEXT", "middle", 11)
    line(c, (90, 190), (750, 190), "EDGE", 1.0, "4,4")
    REG.put("dipole-orderings", c, "Dipole arrangements of the five types of magnetism",
            "Dipoles without and with an applied field H in diamagnetic, paramagnetic, ferromagnetic, antiferromagnetic and ferrimagnetic materials (schematic)")


# ---------------------------------------------------------------- domains (S15) and magnetization (S16-S18)

def domain_closure():
    c = Canvas(720, 320)
    xs = [40, 215, 390, 565]
    heads = ["One domain", "Two domains", "Four domains", "Closure domains"]
    energy = ["high magnetostatic energy", "lower than one domain", "lower than two domains", "zero magnetostatic energy"]
    for k, x in enumerate(xs):
        txt(c, x + 55, 30, heads[k], "HEAD", "middle", 13, "700")
        rect(c, x, 60, 110, 110, "HEAD", 1.6, None, "ATOM", 0.10)
        if k == 0:
            dip(c, x + 55, 115, 0, 70, "PINK", 2.6)
            for dx in (-18, 0, 18):
                pathd(c, f"M{x + 55 + dx * 3},60 C{x + 55 + dx * 5},30 {x + 55 + dx * 5},{200} {x + 55 + dx * 3},170", "EDGE", 0.9, "3,3")
        elif k == 1:
            line(c, (x + 55, 60), (x + 55, 170), "ACC", 1.8)
            dip(c, x + 28, 115, 0, 60, "PINK", 2.4)
            dip(c, x + 83, 115, 180, 60, "PINK", 2.4)
        elif k == 2:
            for i in range(1, 4):
                line(c, (x + i * 27.5, 60), (x + i * 27.5, 170), "ACC", 1.6)
            for i in range(4):
                dip(c, x + 14 + i * 27.5, 115, 0 if i % 2 == 0 else 180, 60, "PINK", 2.2)
        else:
            line(c, (x, 60), (x + 27.5, 87.5), "ACC", 1.6)
            line(c, (x + 110, 60), (x + 82.5, 87.5), "ACC", 1.6)
            line(c, (x, 170), (x + 27.5, 142.5), "ACC", 1.6)
            line(c, (x + 110, 170), (x + 82.5, 142.5), "ACC", 1.6)
            line(c, (x + 27.5, 87.5), (x + 27.5, 142.5), "ACC", 1.6)
            line(c, (x + 82.5, 87.5), (x + 82.5, 142.5), "ACC", 1.6)
            line(c, (x + 27.5, 87.5), (x + 82.5, 87.5), "ACC", 1.0, "3,3")
            line(c, (x + 27.5, 142.5), (x + 82.5, 142.5), "ACC", 1.0, "3,3")
            dip(c, x + 14, 115, 0, 40, "PINK", 2.2)
            dip(c, x + 55, 115, 180, 40, "PINK", 2.2)
            dip(c, x + 96, 115, 0, 40, "PINK", 2.2)
            arrow(c, (x + 60, 75), (x + 40, 75), "BLUE", 2.0, 8)
            arrow(c, (x + 50, 156), (x + 70, 156), "BLUE", 2.0, 8)
        txt(c, x + 55, 214, energy[k], "TEXT", "middle", 11)
    txt(c, 360, 262, "Domains form spontaneously because each split lowers the magnetostatic energy of the stray field;", "TEXT", "middle", 12)
    txt(c, 360, 280, "orange lines are domain (Bloch) walls, arrows are the magnetization of each domain", "TEXT", "middle", 12)
    REG.put("domain-closure", c, "Origin of magnetic domains",
            "Splitting a single domain into two, four and closure domains lowers the magnetostatic energy of the material, down to zero for closure domains (schematic)")


def initial_magnetization():
    c = Canvas(700, 360)
    o = (80, 310)
    axes(c, o, 650, 30, "Magnetic field H", "Magnetization M (or B)")
    X, Y = 500.0, 240.0

    def f(t):
        t = max(0.0, min(1.0, t))
        return 0.10 * t + 0.90 * (3 * t * t - 2 * t ** 3)
    pts = [(o[0] + t * X, o[1] - Y * f(t)) for t in [i / 80 for i in range(0, 81)]]
    poly(c, pts, "PINK", 2.8)
    line(c, (o[0], o[1] - Y), (o[0] + X + 60, o[1] - Y), "EDGE", 1.0, "5,4")
    txt(c, o[0] + X + 64, o[1] - Y + 4, sub("M", "s"), "HEAD", "start", 14, "700")
    s_max = 0.10 + 0.90 * 1.5
    line(c, o, (o[0] + 190, o[1] - 190 * Y * s_max / X), "ACC", 1.6, "6,4")
    line(c, o, (o[0] + 130, o[1] - 130 * Y * 0.10 / X), "BLUE", 2.4)
    txt(c, o[0] + 190, o[1] - 190 * Y * s_max / X - 12, "slope = maximum permeability " + sub("μ", "max"), "ACC", "end", 12, "700")
    txt(c, o[0] + 140, o[1] - 130 * Y * 0.10 / X - 6, "slope = initial permeability " + sub("μ", "i"), "BLUE", "start", 12, "700")
    for t in (0.12, 0.35, 0.62, 0.86):
        dot(c, (o[0] + t * X, o[1] - Y * f(t)), 4, "HEAD", "HEAD")
    txt(c, o[0] + 0.62 * X + 12, o[1] - Y * f(0.62) + 22, "growth of favourable domains", "TEXT", "start", 11)
    txt(c, o[0] + 0.86 * X, o[1] - Y * f(0.86) + 28, "rotation of domains: saturation", "TEXT", "middle", 11)
    txt(c, o[0] + 0.12 * X + 6, o[1] + 20, "random domains", "TEXT", "start", 11)
    REG.put("initial-magnetization", c, "Initial magnetization curve",
            "Magnetization against field starting from the demagnetized state: slow growth (initial permeability), fast growth of favourable domains (maximum permeability), rotation of domains and saturation Ms (schematic)")


def hysteresis_soft_hard():
    c = Canvas(700, 380)
    o = (350, 190)
    line(c, (60, o[1]), (650, o[1]), "EDGE", 1.3, head=True)
    line(c, (o[0], 360), (o[0], 20), "EDGE", 1.3, head=True)
    txt(c, 650, o[1] + 24, "H", "HEAD", "end", 14, "700")
    txt(c, o[0] + 10, 28, "B", "HEAD", "start", 14, "700")
    Bs = 140.0

    def loop(hc, w, col, wd):
        es = [-300 + 4 * i for i in range(151)]
        up = [(o[0] + e, o[1] - Bs * math.tanh((e + hc) / w)) for e in es]
        dn = [(o[0] + e, o[1] - Bs * math.tanh((e - hc) / w)) for e in es]
        poly(c, up, col, wd)
        poly(c, dn, col, wd)
        return Bs * math.tanh(hc / w)
    br_h = loop(150, 60, "PINK", 2.6)
    br_s = loop(22, 14, "BLUE", 2.6)
    line(c, (60, o[1] - Bs), (640, o[1] - Bs), "EDGE", 1.0, "5,4")
    txt(c, 640, o[1] - Bs - 6, sub("B", "s"), "HEAD", "end", 13, "700")
    dot(c, (o[0], o[1] - br_h), 4, "HEAD", "HEAD")
    txt(c, o[0] - 8, o[1] - br_h - 6, sub("B", "r") + " (hard)", "HEAD", "end", 12, "700")
    dot(c, (o[0] - 150, o[1]), 4, "HEAD", "HEAD")
    txt(c, o[0] - 150, o[1] + 20, "−" + sub("H", "c") + " (hard)", "HEAD", "middle", 12, "700")
    dot(c, (o[0] + 22, o[1]), 4, "HEAD", "HEAD")
    txt(c, o[0] + 30, o[1] + 20, sub("H", "c") + " (soft)", "HEAD", "start", 12, "700")
    txt(c, 160, 90, "Hard magnetic material", "PINK", "middle", 13, "700")
    txt(c, 160, 108, "wide loop, high " + sub("B", "r") + " and " + sub("H", "c"), "TEXT", "middle", 11)
    txt(c, 540, 290, "Soft magnetic material", "BLUE", "middle", 13, "700")
    txt(c, 540, 308, "narrow loop, low " + sub("H", "c") + ", high " + sub("μ", "i"), "TEXT", "middle", 11)
    txt(c, 350, 360, "limit between them: " + sub("H", "c") + " = 10 000 A/m", "ACC", "middle", 12, "700")
    REG.put("hysteresis-soft-hard", c, "Hysteresis loops of soft and hard magnetic materials",
            "B-H hysteresis loops: a soft material has a narrow loop (low coercivity Hc, high initial permeability), a hard material a wide one (high remanence Br, saturation Bs and Hc); the slide fixes the limit at Hc = 10 000 A/m (schematic)")


# ---------------------------------------------------------------- superconductors (S28-S29)

def superconductor_types():
    c = Canvas(720, 330)
    for k, ox in enumerate((60, 400)):
        o = (ox, 270)
        axes(c, o, ox + 260, 40, "H", "−M")
        if k == 0:
            txt(c, ox + 130, 28, "Type I (soft superconductor)", "HEAD", "middle", 14, "700")
            hc = ox + 150
            poly(c, [o, (hc, 90), (hc, o[1])], "PINK", 2.8)
            line(c, (hc, 90), (hc, o[1]), "PINK", 2.8)
            txt(c, hc, o[1] + 22, sub("H", "c"), "HEAD", "middle", 13, "700")
            txt(c, ox + 60, 90, "Meissner state", "BLUE", "middle", 12, "700")
            txt(c, ox + 60, 106, "(perfect diamagnet)", "TEXT", "middle", 11)
            txt(c, ox + 215, 230, "normal state", "TEXT", "middle", 12)
            txt(c, ox + 130, 304, "sharp transition at a low " + sub("H", "c"), "TEXT", "middle", 11)
        else:
            txt(c, ox + 130, 28, "Type II (hard superconductor)", "HEAD", "middle", 14, "700")
            h1, h2 = ox + 70, ox + 210
            pts = [o, (h1, 120)]
            for i in range(0, 21):
                t = i / 20
                pts.append((h1 + t * (h2 - h1), 120 + (o[1] - 120) * (t ** 1.6)))
            poly(c, pts, "PINK", 2.8)
            line(c, (h1, 120), (h1, o[1]), "EDGE", 1.0, "4,4")
            line(c, (h2, 120), (h2, o[1]), "EDGE", 1.0, "4,4")
            txt(c, h1, o[1] + 22, sub("H", "c1"), "HEAD", "middle", 13, "700")
            txt(c, h2, o[1] + 22, sub("H", "c2"), "HEAD", "middle", 13, "700")
            txt(c, ox + 35, 100, "Meissner", "BLUE", "middle", 12, "700")
            txt(c, ox + 140, 100, "mixed state", "ACC", "middle", 12, "700")
            txt(c, ox + 140, 116, "(flux lines penetrate)", "TEXT", "middle", 11)
            txt(c, ox + 240, 230, "normal", "TEXT", "middle", 12)
            txt(c, ox + 130, 304, "gradual transition between " + sub("H", "c1") + " and " + sub("H", "c2"), "TEXT", "middle", 11)
    REG.put("superconductor-types", c, "Type I and Type II superconductors in a magnetic field",
            "Type I: perfect diamagnetism up to Hc and then an abrupt return to the normal state. Type II: the field starts to penetrate at Hc1 and penetration is complete at Hc2, with a mixed state in between (schematic, not to scale)")


# ---------------------------------------------------------------- thermal expansion (S36, S39)

def _morse(r, r0=1.0, a=1.6):
    return (1 - math.exp(-a * (r - r0))) ** 2


def asymmetric_well():
    c = Canvas(700, 360)
    o = (70, 320)
    axes(c, o, 660, 30, "Interatomic distance r", "Potential energy")
    X0, X1 = 110.0, 600.0
    r_lo, r_hi = 0.62, 2.7
    PX = lambda r: X0 + (r - r_lo) / (r_hi - r_lo) * (X1 - X0)
    PY = lambda v: 300 - v * 215
    rs = [r_lo + i * (r_hi - r_lo) / 160 for i in range(161)]
    poly(c, [(PX(r), PY(_morse(r))) for r in rs if _morse(r) <= 1.35], "PINK", 2.8)
    k = 3.2
    poly(c, [(PX(r), PY(k * (r - 1) ** 2 * 0.62)) for r in rs if k * (r - 1) ** 2 * 0.62 <= 1.35], "BLUE", 1.8, "6,4")
    r0x = PX(1.0)
    line(c, (r0x, 36), (r0x, 308), "EDGE", 1.0, "4,4")
    txt(c, r0x, 328, sub("r", "0"), "HEAD", "middle", 13, "700")
    means = []
    for v, col in ((0.18, "GREEN"), (0.45, "ACC"), (0.78, "PINK")):
        lo = [r for r in rs if r < 1.0 and _morse(r) <= v][0]
        hi = [r for r in reversed(rs) if r > 1.0 and _morse(r) <= v][0]
        y = PY(v)
        line(c, (PX(lo), y), (PX(hi), y), col, 1.6)
        mx = (PX(lo) + PX(hi)) / 2
        dot(c, (mx, y), 4.5, col, col)
        means.append((mx, y))
    poly(c, means, "HEAD", 1.2, "3,3")
    txt(c, 530, 60, "asymmetric well:", "PINK", "start", 12, "700")
    txt(c, 530, 76, "the mean distance (dots)", "TEXT", "start", 11)
    txt(c, 530, 91, "grows with the energy,", "TEXT", "start", 11)
    txt(c, 530, 106, "so the solid expands", "TEXT", "start", 11)
    txt(c, 540, 150, "dashed: symmetric", "BLUE", "start", 12, "700")
    txt(c, 540, 165, "(harmonic) well,", "TEXT", "start", 11)
    txt(c, 540, 180, "mean stays at " + sub("r", "0"), "TEXT", "start", 11)
    REG.put("asymmetric-well", c, "Asymmetric interatomic potential well and thermal expansion",
            "Extension, not printed on the slides: because the real potential well is asymmetric, the mean interatomic distance grows with the vibration energy; a symmetric parabola would keep it at r0 (schematic)")


def bimetal_strip():
    c = Canvas(700, 330)
    # straight strips
    txt(c, 150, 28, "Room temperature", "HEAD", "middle", 13, "700")
    rect(c, 60, 110, 180, 18, "ACC", 1.6, None, "ACC", 0.35)
    rect(c, 60, 128, 180, 18, "BLUE", 1.6, None, "BLUE", 0.30)
    txt(c, 250, 123, "metal 1, " + sub("α", "1"), "ACC", "start", 12, "700")
    txt(c, 250, 141, "metal 2, " + sub("α", "2"), "BLUE", "start", 12, "700")
    txt(c, 150, 190, sub("α", "1") + " &gt; " + sub("α", "2"), "HEAD", "middle", 13, "700")
    line(c, (45, 98), (45, 160), "HEAD", 3)
    txt(c, 150, 220, "clamped at the left end", "TEXT", "middle", 11)
    # bent strip
    txt(c, 500, 28, "Heated, " + sub("T", "2") + " &gt; " + sub("T", "1"), "HEAD", "middle", 13, "700")
    R, t = 260.0, 18.0
    cx, cy = 420, 110 + R
    th = 0.55
    outer = [(cx + (R + t) * math.sin(a * th / 30), cy - (R + t) * math.cos(a * th / 30)) for a in range(31)]
    mid = [(cx + R * math.sin(a * th / 30), cy - R * math.cos(a * th / 30)) for a in range(31)]
    inner = [(cx + (R - t) * math.sin(a * th / 30), cy - (R - t) * math.cos(a * th / 30)) for a in range(31)]
    poly(c, outer + list(reversed(mid)), "ACC", 1.6, None, "ACC", True, 0.35)
    poly(c, mid + list(reversed(inner)), "BLUE", 1.6, None, "BLUE", True, 0.30)
    line(c, (410, 98), (410, 160), "HEAD", 3)
    txt(c, 500, 250, "the metal with the larger α expands more", "TEXT", "middle", 12)
    txt(c, 500, 268, "and the strip bends towards the other metal", "TEXT", "middle", 12)
    txt(c, 350, 306, "A bimetallic strip turns a temperature change into a mechanical displacement", "TEXT", "middle", 12)
    REG.put("bimetal-strip", c, "Bimetallic strip",
            "Two metals with different expansion coefficients bonded together: on heating the strip bends towards the metal with the smaller coefficient (schematic)")


# ---------------------------------------------------------------- thermal conductivity (S40)

def heat_flux_bar():
    c = Canvas(700, 330)
    rect(c, 120, 70, 380, 70, "HEAD", 1.8, None, "ATOM", 0.12)
    txt(c, 100, 110, "hot end", "PINK", "end", 12, "700")
    txt(c, 520, 110, "cold end", "BLUE", "start", 12, "700")
    arrow(c, (160, 105), (460, 105), "PINK", 2.8, 12)
    txt(c, 310, 96, "q = Q / A", "PINK", "middle", 14, "700")
    dim(c, (160, 170), (460, 170), "Δx", "TEXT", (0, 18))
    txt(c, 140, 62, sub("T", "hot"), "PINK", "middle", 13, "700")
    txt(c, 480, 62, sub("T", "cold"), "BLUE", "middle", 13, "700")
    txt(c, 310, 214, "q = −k ΔT / Δx", "HEAD", "middle", 16, "700")
    txt(c, 310, 234, "heat flows towards the cold end, down the temperature gradient", "TEXT", "middle", 12)
    rect(c, 40, 262, 250, 46, "GREEN", 1.5, None, "GREEN", 0.14, 6)
    txt(c, 165, 290, "free electrons: " + sub("k", "e"), "GREEN", "middle", 13, "700")
    rect(c, 330, 262, 250, 46, "BLUE", 1.5, None, "BLUE", 0.14, 6)
    txt(c, 455, 290, "lattice vibrations (phonons): " + sub("k", "ph"), "BLUE", "middle", 12, "700")
    txt(c, 605, 280, "k = " + sub("k", "e") + " + " + sub("k", "ph"), "HEAD", "start", 13, "700")
    REG.put("heat-flux-bar", c, "Heat flux through a bar (Fourier's law)",
            "A bar heated at one end carries a heat flux q = Q/A towards the cold end, proportional to the temperature gradient; the heat is carried by free electrons and by phonons, k = ke + kph (schematic)")


# ---------------------------------------------------------------- thermal stresses (S45, S47)

def constrained_bar():
    c = Canvas(700, 300)
    for k, ox in enumerate((30, 370)):
        title = ("Heating: " + sub("T", "f") + " &gt; " + sub("T", "0")) if k == 0 else ("Cooling: " + sub("T", "f") + " &lt; " + sub("T", "0"))
        txt(c, ox + 150, 28, title, "HEAD", "middle", 14, "700")
        rect(c, ox, 60, 26, 130, "EDGE", 1.4, None, "EDGE", 0.35)
        rect(c, ox + 274, 60, 26, 130, "EDGE", 1.4, None, "EDGE", 0.35)
        rect(c, ox + 26, 105, 248, 40, "HEAD", 1.8, None, "ATOM", 0.25)
        if k == 0:
            arrow(c, (ox + 30, 125), (ox + 75, 125), "PINK", 2.6, 10)
            arrow(c, (ox + 270, 125), (ox + 225, 125), "PINK", 2.6, 10)
            txt(c, ox + 150, 80, "wall forces push on the bar", "TEXT", "middle", 12)
            txt(c, ox + 150, 232, "compressive stress, σ &lt; 0", "PINK", "middle", 14, "700")
        else:
            arrow(c, (ox + 75, 125), (ox + 30, 125), "BLUE", 2.6, 10)
            arrow(c, (ox + 225, 125), (ox + 270, 125), "BLUE", 2.6, 10)
            txt(c, ox + 150, 80, "wall forces pull on the bar", "TEXT", "middle", 12)
            txt(c, ox + 150, 232, "tensile stress, σ &gt; 0", "BLUE", "middle", 14, "700")
    txt(c, 350, 270, "σ = E α (" + sub("T", "0") + " − " + sub("T", "f") + ") = E α ΔT   (bar held at constant length)", "HEAD", "middle", 14, "700")
    REG.put("constrained-bar", c, "Thermal stress in a bar between two rigid walls",
            "A bar that cannot expand or contract: heating gives a compressive stress and cooling a tensile stress, σ = E α (T0 − Tf) (schematic)")


def thermal_shock():
    c = Canvas(720, 340)
    for k, ox in enumerate((40, 400)):
        txt(c, ox + 140, 28, "Rapid heating" if k == 0 else "Rapid cooling", "HEAD", "middle", 14, "700")
        rect(c, ox, 60, 110, 190, "HEAD", 1.6, None, "ATOM", 0.12)
        txt(c, ox + 55, 100, "surface", "TEXT", "middle", 11)
        txt(c, ox + 55, 160, "interior", "TEXT", "middle", 11)
        # stress profile across the width, zero axis at x = ox + 210
        ax = ox + 210
        line(c, (ax, 56), (ax, 254), "EDGE", 1.2)
        sign = 1 if k == 0 else -1
        pts = []
        for i in range(0, 41):
            x = -1 + i / 20
            s = sign * (1 - 3 * x * x) / 2.0
            pts.append((ax + s * 70, 155 + x * 95))
        poly(c, pts, "ACC", 2.6)
        txt(c, ax + 70, 276, "tensile" if k == 0 else "compressive", "TEXT", "middle", 11)
        txt(c, ax - 70, 276, "compressive" if k == 0 else "tensile", "TEXT", "middle", 11)
        txt(c, ax, 48, "σ", "HEAD", "middle", 13, "700")
        txt(c, ox + 140, 300, ("outside hotter and expanded: compressive surface," if k == 0 else "outside colder and contracted: tensile surface,"), "TEXT", "middle", 11)
        txt(c, ox + 140, 316, ("tensile interior" if k == 0 else "compressive interior"), "TEXT", "middle", 11)
    REG.put("thermal-shock", c, "Thermal stresses from a temperature gradient",
            "Rapid heating makes the surface compressive and the interior tensile; rapid cooling reverses the signs, and the tensile surface of a brittle material is where thermal shock cracks start (schematic)")


# ---------------------------------------------------------------- slide crops (not generated here)

def rasters():
    REG.raster("s15-ferrite-garnet-tables", "Commercial ferrite and garnet compositions",
               "Some commercial ferrite and garnet compositions, copied from Session 15 Slide 12", 560)
    REG.raster("s15-domains-grains-bloch", "Domains in a grain and a Bloch wall",
               "A grain with domains, a single-domain small grain and a Bloch wall between two domains, copied from Session 15 Slide 14", 560)
    REG.raster("s15-domains-iron", "Domain pattern in an iron single crystal film",
               "Domain pattern observed in a (001) iron single crystal film 2500 Å thick, copied from Session 15 Slide 14", 300)
    REG.raster("s15-curie-temperature-chart", "Saturation magnetization against temperature for iron and magnetite",
               "Saturation magnetization and saturation flux density against temperature for pure Fe and Fe3O4, which vanish at the Curie temperature, copied from Session 15 Slide 23", 460)
    REG.raster("s15-typical-properties-tables", "Properties of selected soft, hard and recording magnetic materials",
               "Properties of selected soft magnetic materials, hard (permanent) magnetic materials and magnetic recording powders, copied from Session 15 Slide 24", 720)
    REG.raster("s15-superconducting-envelope", "Superconducting critical surface of Nb3Sn",
               "Superconducting envelope: the combined effect of temperature, magnetic field and current density on a Nb3Sn superconductor (Bc2 = 24.5 T, Tc = 18 K, Jc = 10^7 A/cm2), copied from Session 15 Slide 26", 640)
    REG.raster("s15-heat-capacity-chart", "Heat capacity against temperature for metals and ceramics",
               "Heat capacity as a function of temperature for metals and ceramics, levelling off near 6 cal/(mol·K) above the Debye temperature, copied from Session 15 Slide 35", 380)
    REG.raster("s15-expansion-bonding-curves", "Potential energy curves, weak and strong bonding",
               "Interatomic energy curves: the spacing grows when the vibration energy grows, and more for weak than for strong bonding; the same slide plots the potential well at several vibrational energies, copied from Session 15 Slide 36", 700)
    REG.raster("s15-expansion-iron-melting", "Thermal expansion of iron and of metals against melting temperature",
               "Linear coefficient of thermal expansion of iron against temperature (abrupt changes at the allotropic transformations) and of metals at 25 °C against melting temperature, copied from Session 15 Slide 37", 700)
    REG.raster("s15-properties-table", "Specific heat, thermal expansion and thermal conductivity of materials",
               "Specific heat cp, linear expansion coefficient and thermal conductivity k of metals, ceramics and polymers (Invar and Super Invar boxed on the slide), copied from Session 15 Slide 38", 420)
    REG.raster("s15-conductivity-table", "Thermal conductivity of metals, alloys, ceramics and polymers",
               "Thermal conductivity in W/(m·K) of pure metals, alloys, ceramics and polymers, copied from Session 15 Slide 41", 420)
    REG.raster("s15-conductivity-temperature", "Thermal conductivity against temperature",
               "Effect of temperature on the thermal conductivity of several materials (platinum, aluminium, iron, SiC, Al2O3, glass, firebrick), copied from Session 15 Slide 42", 380)
    REG.raster("s15-conductivity-cuzn", "Thermal conductivity of Cu-Zn alloys",
               "Thermal conductivity of Cu-Zn alloys against zinc content: alloying lowers the thermal conductivity, copied from Session 15 Slide 43", 340)


def theory():
    orbital_spin()
    dipole_orderings()
    domain_closure()
    initial_magnetization()
    hysteresis_soft_hard()
    superconductor_types()
    asymmetric_well()
    bimetal_strip()
    heat_flux_bar()
    constrained_bar()
    thermal_shock()
    rasters()


def build():
    theory()
    return REG
