"""Unit 5 figures of the Midterm 2 bank: stress-strain curves (Session 11) and strengthening sketches (Session 12).

Statement figures carry the data their question reads (values on the curve or on the axes). Option figures of the
"which picture" questions are named u5-<set>-1 ... u5-<set>-4 and their alt text never names the right answer.
"""
import math
import random

from figures.svgkit import Canvas, line, text, poly, dot, sub
from figures.mat_mt2.common import figure


class Map:
    """Data coordinates to pixels: origin at (x0, y0), sx and sy pixels per unit, y up."""

    def __init__(self, x0, y0, sx, sy):
        self.x0, self.y0, self.sx, self.sy = x0, y0, sx, sy

    def p(self, x, y):
        return (self.x0 + x * self.sx, self.y0 - y * self.sy)

    def pts(self, data):
        return [self.p(x, y) for x, y in data]


def axes(c, m, xmax, ymax, xl="strain ε", yl="σ (MPa)", xt=(), yt=(), grid=False):
    if grid:
        for v, _ in xt:
            line(c, m.p(v, 0), m.p(v, ymax * 0.97), "EDGE", 0.6, "2,4")
        for v, _ in yt:
            line(c, m.p(0, v), m.p(xmax * 0.97, v), "EDGE", 0.6, "2,4")
    line(c, m.p(0, 0), m.p(xmax, 0), "EDGE", 1.3, head=True)
    line(c, m.p(0, 0), m.p(0, ymax), "EDGE", 1.3, head=True)
    for v, s in xt:
        x, y = m.p(v, 0)
        line(c, (x, y), (x, y + 5), "EDGE", 1.1)
        text(c, (x, y + 18), s, "TEXT", "middle", 11.5)
    for v, s in yt:
        x, y = m.p(0, v)
        line(c, (x - 5, y), (x, y), "EDGE", 1.1)
        text(c, (x - 8, y + 4), s, "TEXT", "end", 11.5)
    x, y = m.p(xmax, 0)
    text(c, (x, y + 34), xl, "HEAD", "end", 12.5, "700")
    x, y = m.p(0, ymax)
    text(c, (x + 8, y + 4), yl, "HEAD", "start", 12.5, "700")


def sample(fn, a, b, n=80):
    return [(a + (b - a) * i / n, fn(a + (b - a) * i / n)) for i in range(n + 1)]


def ductile(eps):
    """Generic ductile metal curve (normalised: strain 0-1, stress 0-1): linear, rounded yield, maximum, neck."""
    if eps <= 0.06:
        return eps / 0.06 * 0.62
    if eps <= 0.62:
        t = (eps - 0.06) / 0.56
        return 0.62 + 0.30 * (1 - (1 - t) ** 2.2)
    t = (eps - 0.62) / 0.38
    return 0.92 - 0.22 * t ** 1.6


# --------------------------------------------------------------------------- statement figures
@figure("u5-curve-points", "Engineering stress-strain curve of a metal with four marked points A, B, C and D")
def curve_points():
    c = Canvas(440, 290)
    m = Map(60, 240, 340, 200)
    axes(c, m, 1.08, 1.08, "engineering strain", "engineering stress")
    m_pts = sample(ductile, 0, 1.0, 120)
    poly(c, m.pts(m_pts), "ACC", 2.4)
    marks = {"D": (0.03, ductile(0.03)), "A": (0.06, ductile(0.06)), "B": (0.62, ductile(0.62)), "C": (1.0, ductile(1.0))}
    off = {"D": (12, 6), "A": (-12, -8), "B": (0, -14), "C": (8, -10)}
    anchor = {"D": "start", "A": "end", "B": "middle", "C": "start"}
    for k, (x, y) in marks.items():
        dot(c, m.p(x, y), 4.5, "HEAD", "BLUE")
        px, py = m.p(x, y)
        text(c, (px + off[k][0], py + off[k][1]), k, "BLUE", anchor[k], 14, "700")
    return c


def offset_curve(e):
    return 200000 * e if e <= 0.0015 else 300 + 160 * (1 - math.exp(-(e - 0.0015) / (0.0024 / math.log(2))))


@figure("u5-offset-yield", "Stress-strain curve with an elastic line of slope 200 GPa, a dashed line parallel to it from a strain of 0.002, and marked points P and Y")
def offset_yield():
    c = Canvas(460, 320)
    m = Map(70, 270, 340 / 0.0125, 230 / 520)
    xt = [(0.002 * k, f"{0.002 * k:.3f}") for k in range(1, 7)]
    yt = [(100 * k, str(100 * k)) for k in range(1, 6)]
    axes(c, m, 0.0128, 520, "strain ε", "σ (MPa)", xt, yt, grid=True)
    poly(c, m.pts(sample(offset_curve, 0, 0.012, 160)), "ACC", 2.4)
    poly(c, [m.p(0.002, 0), m.p(0.0046, 200000 * 0.0026)], "BLUE", 1.6, "6,4")
    dot(c, m.p(0.0015, 300), 4.5, "HEAD", "HEAD")
    text(c, (m.p(0.0015, 300)[0] - 8, m.p(0.0015, 300)[1] - 6), "P", "HEAD", "end", 13, "700")
    dot(c, m.p(0.0039, 380), 4.5, "HEAD", "PINK")
    text(c, (m.p(0.0039, 380)[0] + 10, m.p(0.0039, 380)[1] + 16), "Y", "PINK", "start", 13, "700")
    line(c, m.p(0, 380), m.p(0.0039, 380), "PINK", 1.0, "3,3")
    text(c, (m.p(0, 380)[0] + 6, m.p(0, 380)[1] - 5), "380", "PINK", "start", 11.5, "700")
    text(c, m.p(0.0048, 70), "line from ε = 0.002", "BLUE", "start", 11.5)
    return c


@figure("u5-discontinuous-yield", "Stress-strain curve of a low-carbon steel with an upper yield point at 330 MPa and a lower yield point at 290 MPa")
def discontinuous_yield():
    c = Canvas(440, 290)
    m = Map(70, 240, 330 / 0.06, 200 / 420)
    yt = [(100, "100"), (200, "200"), (290, "290"), (330, "330"), (400, "400")]
    axes(c, m, 0.062, 430, "strain ε", "σ (MPa)", [(0.02, "0.02"), (0.04, "0.04")], yt)
    pts = [(0, 0), (0.0016, 330), (0.0026, 290), (0.0045, 296), (0.0065, 290), (0.0085, 297), (0.0105, 291),
           (0.0125, 296), (0.0145, 291), (0.0165, 297), (0.019, 292)]
    pts += [(0.019 + 0.04 * i / 30, 292 + 98 * (1 - (1 - i / 30) ** 2)) for i in range(1, 31)]
    poly(c, m.pts(pts), "ACC", 2.2)
    line(c, m.p(0, 330), m.p(0.0016, 330), "EDGE", 1.0, "3,3")
    line(c, m.p(0, 290), m.p(0.0026, 290), "EDGE", 1.0, "3,3")
    text(c, (m.p(0.0016, 330)[0] + 8, m.p(0.0016, 330)[1] - 6), "upper yield point", "HEAD", "start", 11.5)
    text(c, (m.p(0.0045, 290)[0] + 4, m.p(0.0045, 290)[1] + 22), "lower yield point", "HEAD", "start", 11.5)
    return c


@figure("u5-load-unload", "Stress-strain path of an alloy loaded to point L at a strain of 0.010 and a stress of 280 MPa and then unloaded along a dashed line")
def load_unload():
    c = Canvas(440, 290)
    m = Map(70, 240, 330 / 0.013, 200 / 330)
    axes(c, m, 0.0135, 330, "strain ε", "σ (MPa)", [(0.005, "0.005"), (0.010, "0.010")],
         [(100, "100"), (200, "200"), (280, "280")])
    load = [(0, 0), (0.003, 210)] + [(0.003 + 0.007 * i / 20, 210 + 70 * (1 - (1 - i / 20) ** 2)) for i in range(1, 21)]
    poly(c, m.pts(load), "ACC", 2.4)
    poly(c, [m.p(0.010, 280), m.p(0.006, 0)], "BLUE", 1.8, "6,4")
    line(c, m.p(0, 280), m.p(0.010, 280), "EDGE", 1.0, "3,3")
    line(c, m.p(0.010, 0), m.p(0.010, 280), "EDGE", 1.0, "3,3")
    dot(c, m.p(0.010, 280), 4.5, "HEAD", "PINK")
    text(c, (m.p(0.010, 280)[0] + 8, m.p(0.010, 280)[1] - 8), "L", "PINK", "start", 13, "700")
    text(c, (m.p(0.0085, 120)[0] + 10, m.p(0.0085, 120)[1]), "unloading", "BLUE", "start", 11.5)
    return c


def curve_ab(eps, sy, uts, ef, ey):
    if eps <= ey:
        return sy * eps / ey
    t = (eps - ey) / (ef - ey)
    return sy + (uts - sy) * (1 - (1 - t) ** 2) if t <= 0.75 else sy + (uts - sy) * (1 - 0.0625) - (uts - sy) * 1.2 * (t - 0.75) ** 2


@figure("u5-two-curves-toughness", "Engineering stress-strain curves of two alloys, A and B, drawn to fracture on the same axes")
def two_curves():
    c = Canvas(460, 300)
    m = Map(70, 250, 340 / 0.40, 210 / 760)
    axes(c, m, 0.41, 770, "strain ε", "σ (MPa)", [(0.1, "0.1"), (0.2, "0.2"), (0.3, "0.3")],
         [(200, "200"), (400, "400"), (600, "600")])
    a = sample(lambda e: curve_ab(e, 600, 700, 0.05, 0.003), 0, 0.05, 60)
    b = sample(lambda e: curve_ab(e, 300, 400, 0.35, 0.0015), 0, 0.35, 120)
    poly(c, m.pts(a), "PINK", 2.4)
    poly(c, m.pts(b), "BLUE", 2.4)
    text(c, (m.p(0.05, 700)[0] + 10, m.p(0.05, 700)[1] - 4), "A", "PINK", "start", 14, "700")
    text(c, (m.p(0.35, 380)[0] + 2, m.p(0.35, 380)[1] - 16), "B", "BLUE", "start", 14, "700")
    for e, s in ((0.05, a[-1][1]), (0.35, b[-1][1])):
        text(c, (m.p(e, s)[0], m.p(e, s)[1] + 5), "×", "HEAD", "middle", 15, "700")
    return c


@figure("u5-nonlinear-moduli", "Non-linear stress-strain curve with three straight lines labelled 1, 2 and 3; point Q lies on the curve")
def nonlinear_moduli():
    c = Canvas(440, 290)
    m = Map(60, 240, 340 / 1.0, 200 / 1.0)
    axes(c, m, 1.04, 1.06, "strain ε", "σ")
    f = lambda e: 1.05 * (1 - math.exp(-e / 0.42))  # noqa: E731
    poly(c, m.pts(sample(f, 0, 0.95, 100)), "ACC", 2.4)
    slope0 = 1.05 / 0.42
    poly(c, [m.p(0, 0), m.p(0.36, slope0 * 0.36)], "GREEN", 1.6, "6,4")
    q = 0.55
    fq = f(q)
    poly(c, [m.p(0, 0), m.p(0.78, fq / q * 0.78)], "BLUE", 1.6, "6,4")
    sq = 1.05 / 0.42 * math.exp(-q / 0.42)
    poly(c, [m.p(q - 0.40, fq - 0.40 * sq), m.p(q + 0.40, fq + 0.40 * sq)], "PINK", 1.6, "6,4")
    dot(c, m.p(q, fq), 4.5, "HEAD", "HEAD")
    text(c, (m.p(q, fq)[0] + 2, m.p(q, fq)[1] + 22), "Q", "HEAD", "start", 13, "700")
    text(c, (m.p(0.36, slope0 * 0.36)[0] + 8, m.p(0.36, slope0 * 0.36)[1] + 4), "1", "GREEN", "start", 14, "700")
    text(c, (m.p(0.78, fq / q * 0.78)[0] + 8, m.p(0.78, fq / q * 0.78)[1] + 4), "2", "BLUE", "start", 14, "700")
    text(c, (m.p(q + 0.40, fq + 0.40 * sq)[0] + 8, m.p(q + 0.40, fq + 0.40 * sq)[1] + 4), "3", "PINK", "start", 14, "700")
    return c


def eng_curve(e):
    if e <= 0.004:
        return e / 0.004 * 280
    if e <= 0.25:
        t = (e - 0.004) / 0.246
        return 280 + 120 * (1 - (1 - t) ** 2.4)
    t = (e - 0.25) / 0.15
    return 400 - 90 * t ** 1.5


@figure("u5-true-eng-curves", "Two stress-strain curves of the same tensile test, labelled 1 and 2, both ending with a cross at fracture")
def true_eng():
    c = Canvas(460, 300)
    m = Map(70, 250, 330 / 0.42, 210 / 760)
    axes(c, m, 0.43, 770, "strain", "stress (MPa)", [(0.1, "0.1"), (0.2, "0.2"), (0.3, "0.3"), (0.4, "0.4")],
         [(200, "200"), (400, "400"), (600, "600")])
    eng = sample(eng_curve, 0, 0.40, 140)
    poly(c, m.pts(eng), "BLUE", 2.4)
    true = [(math.log(1 + e), s * (1 + e)) for e, s in eng if e <= 0.25]
    e_n, s_n = true[-1]
    true += [(e_n + 0.12 * i / 20, s_n + 500 * (0.12 * i / 20) + 8000 * (0.12 * i / 20) ** 2) for i in range(1, 21)]
    poly(c, m.pts(true), "PINK", 2.4)
    for x, y in (eng[-1], true[-1]):
        text(c, (m.p(x, y)[0], m.p(x, y)[1] + 5), "×", "HEAD", "middle", 15, "700")
    text(c, (m.p(0.40, eng[-1][1])[0] + 8, m.p(0.40, eng[-1][1])[1] + 18), "1", "BLUE", "start", 14, "700")
    text(c, (m.p(*true[-1])[0] + 10, m.p(*true[-1])[1] + 2), "2", "PINK", "start", 14, "700")
    return c


@figure("u5-elastic-slope", "Linear elastic part of a stress-strain curve passing through the point at a strain of 0.002 and a stress of 140 MPa")
def elastic_slope():
    c = Canvas(420, 290)
    m = Map(70, 240, 300 / 0.003, 200 / 220)
    axes(c, m, 0.0031, 220, "strain ε", "σ (MPa)", [(0.001, "0.001"), (0.002, "0.002"), (0.003, "0.003")],
         [(50, "50"), (100, "100"), (140, "140"), (200, "200")], grid=False)
    poly(c, [m.p(0, 0), m.p(0.0028, 196)], "ACC", 2.4)
    line(c, m.p(0, 140), m.p(0.002, 140), "EDGE", 1.0, "3,3")
    line(c, m.p(0.002, 0), m.p(0.002, 140), "EDGE", 1.0, "3,3")
    dot(c, m.p(0.002, 140), 4.5, "HEAD", "PINK")
    return c


@figure("u5-fracture-el", "Stress-strain curve of an alloy that fractures at a strain of 0.30 and a stress of 280 MPa")
def fracture_el():
    c = Canvas(460, 290)
    m = Map(70, 240, 340 / 0.33, 200 / 420)
    axes(c, m, 0.335, 420, "strain ε", "σ (MPa)", [(0.1, "0.10"), (0.2, "0.20"), (0.3, "0.30")],
         [(100, "100"), (200, "200"), (280, "280"), (380, "380")])
    def f(e):
        if e <= 0.0036:
            return e / 0.0036 * 250
        if e <= 0.20:
            t = (e - 0.0036) / 0.1964
            return 250 + 130 * (1 - (1 - t) ** 2)
        return 380 - 100 * ((e - 0.20) / 0.10) ** 2
    pts = sample(f, 0, 0.30, 140)
    poly(c, m.pts(pts), "ACC", 2.4)
    line(c, m.p(0, 280), m.p(0.30, 280), "EDGE", 1.0, "3,3")
    line(c, m.p(0.30, 0), m.p(0.30, 280), "EDGE", 1.0, "3,3")
    text(c, (m.p(0.30, 280)[0], m.p(0.30, 280)[1] + 5), "×", "HEAD", "middle", 15, "700")
    text(c, (m.p(0.30, 280)[0] + 10, m.p(0.30, 280)[1] - 10), "fracture", "HEAD", "start", 11.5)
    return c


# --------------------------------------------------------------------------- option figures (small)
def small(label_x="ε", label_y="σ"):
    c = Canvas(200, 150)
    m = Map(26, 128, 160, 108)
    line(c, m.p(0, 0), m.p(1.0, 0), "EDGE", 1.2, head=True)
    line(c, m.p(0, 0), m.p(0, 1.0), "EDGE", 1.2, head=True)
    text(c, (m.p(1.0, 0)[0], m.p(1.0, 0)[1] + 16), label_x, "HEAD", "end", 12, "700")
    text(c, (m.p(0, 1.0)[0] + 7, m.p(0, 1.0)[1] + 4), label_y, "HEAD", "start", 12, "700")
    return c, m


def end_cross(c, m, x, y):
    text(c, (m.p(x, y)[0], m.p(x, y)[1] + 5), "×", "HEAD", "middle", 13, "700")


@figure("u5-family-1", "Tensile curve 1")
def family_1():
    c, m = small()
    pts = [(e * 0.9, ductile(e) * 0.85) for e in [i / 60 for i in range(61)]]
    poly(c, m.pts(pts), "ACC", 2.2)
    end_cross(c, m, *pts[-1])
    return c


@figure("u5-family-2", "Tensile curve 2")
def family_2():
    c, m = small()
    pts = [(0, 0), (0.09, 0.82)]
    poly(c, m.pts(pts), "ACC", 2.2)
    end_cross(c, m, *pts[-1])
    return c


@figure("u5-family-3", "Tensile curve 3")
def family_3():
    c, m = small()
    f = lambda e: 0.32 * math.tanh(e / 0.15) + 0.55 * (e / 0.9) ** 3.2  # noqa: E731
    pts = sample(f, 0, 0.9, 60)
    poly(c, m.pts(pts), "ACC", 2.2)
    end_cross(c, m, *pts[-1])
    return c


@figure("u5-family-4", "Tensile curve 4")
def family_4():
    c, m = small()
    pts = [(0, 0), (0.06, 0.55), (0.10, 0.62), (0.16, 0.48)] + [(0.16 + 0.55 * i / 10, 0.48 + 0.02 * i / 10) for i in range(1, 11)] + \
        [(0.71 + 0.17 * i / 10, 0.50 + 0.28 * (i / 10) ** 2) for i in range(1, 11)]
    poly(c, m.pts(pts), "ACC", 2.2)
    end_cross(c, m, *pts[-1])
    return c


def area_curve(e):
    """Small ductile curve used by the shaded-area pictures (yield at e = 0.12, maximum at 0.6, fracture at 0.9)."""
    if e <= 0.12:
        return e / 0.12 * 0.55
    if e <= 0.6:
        t = (e - 0.12) / 0.48
        return 0.55 + 0.30 * (1 - (1 - t) ** 2)
    t = (e - 0.6) / 0.3
    return 0.85 - 0.18 * t ** 1.6


def area_fig(region):
    c, m = small()
    if region == "elastic":
        shade = [(0, 0), (0.12, 0.55), (0.12, 0)]
    elif region == "all":
        shade = [(0, 0)] + sample(area_curve, 0, 0.9, 60) + [(0.9, 0)]
    elif region == "plastic":
        shade = [(0.12, 0)] + sample(area_curve, 0.12, 0.9, 50) + [(0.9, 0)]
    else:  # neck: from the maximum to fracture
        shade = [(0.6, 0)] + sample(area_curve, 0.6, 0.9, 30) + [(0.9, 0)]
    poly(c, m.pts(shade), "BLUE", 0.8, fill="BLUE", close=True, opacity=0.30)
    pts = sample(area_curve, 0, 0.9, 80)
    poly(c, m.pts(pts), "ACC", 2.2)
    end_cross(c, m, *pts[-1])
    return c


@figure("u5-area-1", "Shaded area 1 under a stress-strain curve")
def area_1():
    return area_fig("all")


@figure("u5-area-2", "Shaded area 2 under a stress-strain curve")
def area_2():
    return area_fig("plastic")


@figure("u5-area-3", "Shaded area 3 under a stress-strain curve")
def area_3():
    return area_fig("elastic")


@figure("u5-area-4", "Shaded area 4 under a stress-strain curve")
def area_4():
    return area_fig("neck")


def grains(spacing, seed):
    """Grain structure: perturbed grid of grain centres joined into cells (nearest-centre boundaries on a fine mesh)."""
    c = Canvas(200, 150)
    rnd = random.Random(seed)
    x0, y0, w, h = 10, 10, 180, 130
    centres = []
    yy = y0 - spacing / 2
    row = 0
    while yy < y0 + h + spacing:
        xx = x0 - spacing / 2 + (spacing / 2 if row % 2 else 0)
        while xx < x0 + w + spacing:
            centres.append((xx + rnd.uniform(-0.3, 0.3) * spacing, yy + rnd.uniform(-0.3, 0.3) * spacing))
            xx += spacing
        yy += spacing * 0.87
        row += 1
    step = 2.0

    def owner(px, py):
        return min(range(len(centres)), key=lambda i: (centres[i][0] - px) ** 2 + (centres[i][1] - py) ** 2)

    nx, ny = int(w / step), int(h / step)
    grid = [[owner(x0 + (i + 0.5) * step, y0 + (j + 0.5) * step) for i in range(nx)] for j in range(ny)]
    segs = []
    for j in range(ny):
        for i in range(nx):
            if i + 1 < nx and grid[j][i] != grid[j][i + 1]:
                x = x0 + (i + 1) * step
                segs.append(f"M{x:.1f},{y0 + j * step:.1f} V{y0 + (j + 1) * step:.1f}")
            if j + 1 < ny and grid[j][i] != grid[j + 1][i]:
                y = y0 + (j + 1) * step
                segs.append(f"M{x0 + i * step:.1f},{y:.1f} H{x0 + (i + 1) * step:.1f}")
    c.add(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="ACC" fill-opacity="0.10" stroke="HEAD" stroke-width="1.4"/>')
    c.add(f'<path d="{" ".join(segs)}" fill="none" stroke="HEAD" stroke-width="1.1"/>')
    return c


@figure("u5-grains-1", "Grain structure 1 of the same alloy")
def grains_1():
    return grains(46, 3)


@figure("u5-grains-2", "Grain structure 2 of the same alloy")
def grains_2():
    return grains(16, 5)


@figure("u5-grains-3", "Grain structure 3 of the same alloy")
def grains_3():
    return grains(70, 7)


@figure("u5-grains-4", "Grain structure 4 of the same alloy")
def grains_4():
    return grains(30, 11)


def trend(kind):
    c, m = small("%CW", "%EL")
    if kind == "fall":
        f = lambda x: 0.12 + 0.75 * math.exp(-x / 0.22)  # noqa: E731
    elif kind == "rise":
        f = lambda x: 0.15 + 0.70 * (1 - math.exp(-x / 0.3))  # noqa: E731
    elif kind == "flat":
        f = lambda x: 0.5  # noqa: E731
    else:  # maximum
        f = lambda x: 0.2 + 0.6 * math.exp(-((x - 0.45) / 0.22) ** 2)  # noqa: E731
    poly(c, m.pts(sample(f, 0, 0.92, 60)), "ACC", 2.2)
    return c


@figure("u5-trend-1", "Trend 1 of %EL against %CW")
def trend_1():
    return trend("rise")


@figure("u5-trend-2", "Trend 2 of %EL against %CW")
def trend_2():
    return trend("max")


@figure("u5-trend-3", "Trend 3 of %EL against %CW")
def trend_3():
    return trend("fall")


@figure("u5-trend-4", "Trend 4 of %EL against %CW")
def trend_4():
    return trend("flat")


def unload(kind):
    c, m = small()
    if kind == "elastic":
        poly(c, m.pts([(0, 0), (0.08, 0.50)]), "ACC", 2.2)
        poly(c, [(x + 5, y + 4) for x, y in m.pts([(0.08, 0.50), (0, 0)])], "BLUE", 1.6, "5,4")
        return c
    load = [(0, 0), (0.10, 0.55)] + [(0.10 + 0.5 * i / 20, 0.55 + 0.25 * (1 - (1 - i / 20) ** 2)) for i in range(1, 21)]
    poly(c, m.pts(load), "ACC", 2.2)
    top = load[-1]
    if kind == "parallel":
        back = [top, (top[0] - top[1] * 0.10 / 0.55, 0)]
    elif kind == "same":
        poly(c, [(x + 5, y + 4) for x, y in m.pts(list(reversed(load)))], "BLUE", 1.6, "5,4")
        return c
    else:  # vertical drop
        back = [top, (top[0], 0)]
    poly(c, m.pts(back), "BLUE", 1.6, "5,4")
    return c


@figure("u5-unload-1", "Loading and unloading path 1")
def unload_1():
    return unload("same")


@figure("u5-unload-2", "Loading and unloading path 2")
def unload_2():
    return unload("vertical")


@figure("u5-unload-3", "Loading and unloading path 3")
def unload_3():
    return unload("elastic")


@figure("u5-unload-4", "Loading and unloading path 4")
def unload_4():
    return unload("parallel")


_ = sub  # imported for labels with subscripts in later figures
