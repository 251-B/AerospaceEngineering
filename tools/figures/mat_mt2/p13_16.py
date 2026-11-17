"""Figures of the Part II problems P13 to P16 of the Midterm 2 bank (archetype tensile-test, Unit 5, 2.0 points).

p13-...: the curve built from the load and gauge-length table of the titanium alloy specimen, with the 0.2 % offset line.
p14-...: the aluminium alloy specimen before the test and after fracture (dimensions of the narrative).
p15-...: the stress-strain curve of a steel with its elastic zoom, from which the student reads every datum.
p16-...: the 0.2 % offset construction that splits the strain at the yield point into its elastic and plastic parts.
The numbers drawn here are the numbers of the notes; the notes' Verification lines recompute the results from them.
"""
import math

from figures.svgkit import Canvas, line, text, poly, dot, rect, pathd, sub
from figures.mat_mt2.common import figure


class Map:
    """Data coordinates to pixels: origin at (x0, y0), sx and sy pixels per unit, y up."""

    def __init__(self, x0, y0, sx, sy):
        self.x0, self.y0, self.sx, self.sy = x0, y0, sx, sy

    def p(self, x, y):
        return (self.x0 + x * self.sx, self.y0 - y * self.sy)

    def pts(self, data):
        return [self.p(x, y) for x, y in data]


def axes(c, m, xmax, ymax, xl, yl, xt=(), yt=(), grid=True, size=11):
    if grid:
        for v, _ in xt:
            line(c, m.p(v, 0), m.p(v, ymax * 0.97), "EDGE", 0.5, "2,4")
        for v, _ in yt:
            line(c, m.p(0, v), m.p(xmax * 0.97, v), "EDGE", 0.5, "2,4")
    line(c, m.p(0, 0), m.p(xmax, 0), "EDGE", 1.3, head=True)
    line(c, m.p(0, 0), m.p(0, ymax), "EDGE", 1.3, head=True)
    for v, s in xt:
        x, y = m.p(v, 0)
        line(c, (x, y), (x, y + 5), "EDGE", 1.1)
        text(c, (x, y + 17), s, "TEXT", "middle", size)
    for v, s in yt:
        x, y = m.p(0, v)
        line(c, (x - 5, y), (x, y), "EDGE", 1.1)
        text(c, (x - 8, y + 4), s, "TEXT", "end", size)
    x, y = m.p(xmax, 0)
    text(c, (x, y + 34), xl, "HEAD", "end", 12, "700")
    x, y = m.p(0, ymax)
    text(c, (x + 8, y + 4), yl, "HEAD", "start", 12, "700")


def pchip(knots):
    """Monotone cubic Hermite interpolant through the knots (x increasing); returns f(x)."""
    xs, ys = [k[0] for k in knots], [k[1] for k in knots]
    n = len(xs)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    d = [(ys[i + 1] - ys[i]) / h[i] for i in range(n - 1)]
    m = [0.0] * n
    m[0], m[-1] = d[0], d[-1]
    for i in range(1, n - 1):
        if d[i - 1] * d[i] <= 0:
            m[i] = 0.0
        else:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])

    def f(x):
        i = max(0, min(n - 2, max(j for j in range(n - 1) if xs[j] <= x) if x >= xs[0] else 0))
        t = (x - xs[i]) / h[i]
        h00, h10 = 2 * t ** 3 - 3 * t ** 2 + 1, t ** 3 - 2 * t ** 2 + t
        h01, h11 = -2 * t ** 3 + 3 * t ** 2, t ** 3 - t ** 2
        return h00 * ys[i] + h10 * h[i] * m[i] + h01 * ys[i + 1] + h11 * h[i] * m[i + 1]
    return f


def sample(fn, a, b, n=120):
    return [(a + (b - a) * i / n, fn(a + (b - a) * i / n)) for i in range(n + 1)]


# --------------------------------------------------------------------------- P13: titanium alloy table
P13_A0 = math.pi * 10.0 ** 2 / 4                    # mm^2
P13_ROWS = [(0, 50.000), (15000, 50.089), (30000, 50.179), (45000, 50.268), (60000, 50.357), (63000, 50.420),
            (66000, 50.500), (69000, 50.900), (72000, 51.750), (74000, 53.000), (71000, 54.600)]
P13_PTS = [((l - 50.0) / 50.0, F / P13_A0) for F, l in P13_ROWS]
P13_E = sum(s / e for e, s in P13_PTS[1:5]) / 4     # MPa, mean secant modulus of rows 1-4
P13_EPS_Y, P13_SY = 0.009814, 835.9                 # crossing of the offset line (solved in the note)


@figure("p13-ti-curve", "Engineering stress-strain curve of the titanium alloy built from the eleven rows of the table, "
        "the full test on the left and the first 1.2 % of strain on the right with the elastic line, the 0.2 % offset "
        "line and its crossing Y with the segment between the rows of 63 and 66 kN",
        "Curve of the titanium alloy from the table: full test (left) and elastic zoom with the 0.2 % offset line (right)")
def p13_curve():
    c = Canvas(780, 330)
    m1 = Map(62, 272, 290 / 0.10, 230 / 1000)
    axes(c, m1, 0.102, 1040, "strain ε", "σ (MPa)", [(0.02 * k, f"{0.02 * k:.2f}") for k in range(1, 5)] + [(0.10, "0.10")],
         [(200 * k, str(200 * k)) for k in range(1, 6)])
    poly(c, m1.pts(P13_PTS), "ACC", 2.2)
    for e, s in P13_PTS[1:]:
        dot(c, m1.p(e, s), 3.2, "HEAD", "HEAD")
    e, s = P13_PTS[9]
    text(c, (m1.p(e, s)[0], m1.p(e, s)[1] - 12), "max. load", "HEAD", "middle", 11)
    e, s = P13_PTS[10]
    text(c, (m1.p(e, s)[0] - 4, m1.p(e, s)[1] + 22), "fracture", "HEAD", "middle", 11)

    m2 = Map(470, 272, 270 / 0.012, 230 / 1000)
    axes(c, m2, 0.0125, 1040, "strain ε", "σ (MPa)", [(0.002, "0.002"), (0.006, "0.006"), (0.010, "0.010")],
         [(200 * k, str(200 * k)) for k in range(1, 6)])
    zoom = [(e, s) for e, s in P13_PTS if e <= 0.0101]
    poly(c, m2.pts(zoom), "ACC", 2.2)
    for e, s in zoom[1:]:
        dot(c, m2.p(e, s), 3.2, "HEAD", "HEAD")
    poly(c, [m2.p(0, 0), m2.p(0.0090, P13_E * 0.0090)], "BLUE", 1.2, "2,3")
    poly(c, [m2.p(0.002, 0), m2.p(0.0112, P13_E * 0.0092)], "BLUE", 1.7, "6,4")
    text(c, m2.p(0.0062, 260), "offset line", "BLUE", "start", 11)
    text(c, m2.p(0.0064, 180), "from ε = 0.002", "BLUE", "start", 11)
    dot(c, m2.p(P13_EPS_Y, P13_SY), 5, "PINK", "PINK")
    text(c, (m2.p(P13_EPS_Y, P13_SY)[0] - 10, m2.p(P13_EPS_Y, P13_SY)[1] - 12), "Y", "PINK", "end", 13, "700")
    line(c, m2.p(0, P13_SY), m2.p(P13_EPS_Y, P13_SY), "PINK", 1.0, "3,3")
    text(c, (m2.p(0, P13_SY)[0] + 6, m2.p(0, P13_SY)[1] - 5), "835.9", "PINK", "start", 11, "700")
    return c


# --------------------------------------------------------------------------- P14: aluminium alloy specimen
@figure("p14-al-specimen", "Round aluminium alloy specimen before the test, with a diameter of 8.00 mm and gauge marks "
        "40.00 mm apart, and the two halves fitted together after fracture, with the gauge marks 45.60 mm apart and a "
        "neck of 6.10 mm diameter",
        "Specimen before the test (top) and the broken halves fitted together (bottom)")
def p14_specimen():
    c = Canvas(560, 250)
    # before
    y0, h = 40, 32
    rect(c, 70, y0, 400, h, "HEAD", 1.6, fill="EDGE", opacity=0.15)
    for x in (150, 390):
        line(c, (x, y0 - 8), (x, y0 + h + 8), "BLUE", 1.6)
    line(c, (150, y0 - 16), (390, y0 - 16), "TEXT", 1.0)
    text(c, (270, y0 - 22), sub("l", "0") + " = 40.00 mm", "TEXT", "middle", 12)
    line(c, (488, y0), (488, y0 + h), "TEXT", 1.0)
    text(c, (496, y0 + h / 2 + 4), sub("d", "0") + " = 8.00 mm", "TEXT", "start", 12)
    text(c, (70, y0 + h + 24), "before the test", "HEAD", "start", 12, "700")
    # after: two halves with a neck at the break
    y1 = 160
    cx = 296
    top = f"M50,{y1} L{cx - 40},{y1} Q{cx - 10},{y1 + 1} {cx - 2},{y1 + 5} L{cx - 2},{y1 + 27} Q{cx - 10},{y1 + 31} {cx - 40},{y1 + 32} L50,{y1 + 32} Z"
    pathd(c, top, "HEAD", 1.6, fill="EDGE", opacity=0.15)
    right = f"M{cx + 2},{y1 + 5} Q{cx + 10},{y1 + 1} {cx + 40},{y1} L520,{y1} L520,{y1 + 32} L{cx + 40},{y1 + 32} Q{cx + 10},{y1 + 31} {cx + 2},{y1 + 27} Z"
    pathd(c, right, "HEAD", 1.6, fill="EDGE", opacity=0.15)
    for x in (130, 434):
        line(c, (x, y1 - 8), (x, y1 + 40), "BLUE", 1.6)
    line(c, (130, y1 - 16), (434, y1 - 16), "TEXT", 1.0)
    text(c, (220, y1 - 22), sub("l", "f") + " = 45.60 mm", "TEXT", "middle", 12)
    line(c, (cx, y1 + 5), (cx, y1 + 27), "PINK", 1.4)
    line(c, (cx, y1 + 27), (cx + 30, y1 + 62), "PINK", 1.0)
    text(c, (cx + 34, y1 + 68), "neck: " + sub("d", "f") + " = 6.10 mm", "PINK", "start", 12)
    text(c, (50, y1 + 56), "after fracture", "HEAD", "start", 12, "700")
    return c


# --------------------------------------------------------------------------- P15: steel curve read by the student
P15_E = 310 / 0.0015                    # MPa, slope through the marked point A
P15_SP = 380.0                          # end of the straight part
P15_SY = 450.0                          # 0.2 % offset yield strength
P15_EY = 0.002 + P15_SY / P15_E         # strain of the crossing of the offset line
_P15_PLASTIC = pchip([(P15_SP / P15_E, P15_SP), (P15_EY, P15_SY), (0.012, 500), (0.03, 528), (0.08, 560), (0.15, 600)])


def p15_curve(e):
    if e <= P15_SP / P15_E:
        return P15_E * e
    if e <= 0.15:
        return _P15_PLASTIC(e)
    return 600 - 100 * ((e - 0.15) / 0.10) ** 1.8


@figure("p15-steel-curve", "Engineering stress-strain curve of a steel drawn to fracture with gridlines, the maximum U at "
        "a strain of 0.15 and 600 MPa, the point B at 0.08 and 560 MPa and fracture F at 0.25 and 500 MPa; an enlarged "
        "panel of the first 0.8 % of strain shows the point A of the straight part at 0.0015 and 310 MPa, the dashed "
        "line parallel to it from a strain of 0.002 and its crossing Y with the curve at 450 MPa",
        "Engineering stress-strain curve of the steel (left) and enlarged start of the test (right)")
def p15_curve_fig():
    c = Canvas(790, 340)
    m1 = Map(62, 282, 300 / 0.30, 240 / 700)
    axes(c, m1, 0.30, 720, "strain ε", "σ (MPa)", [(0.05 * k, f"{0.05 * k:.2f}") for k in range(1, 6)],
         [(100 * k, str(100 * k)) for k in range(1, 7)])
    poly(c, m1.pts(sample(p15_curve, 0, 0.25, 260)), "ACC", 2.4)
    for lab, (e, s), off, anc in (("U", (0.15, 600), (0, -12), "middle"), ("B", (0.08, 560), (-8, -10), "end"),
                                  ("F", (0.25, 500), (8, -8), "start")):
        dot(c, m1.p(e, s), 4.2, "PINK", "PINK")
        px, py = m1.p(e, s)
        text(c, (px + off[0], py + off[1]), lab, "PINK", anc, 13, "700")
    pb = m1.p(0.08, 560)
    line(c, m1.p(0.08, 0), pb, "PINK", 0.9, "3,3")
    line(c, m1.p(0, 560), pb, "PINK", 0.9, "3,3")
    text(c, (m1.p(0, 560)[0] + 4, m1.p(0, 560)[1] - 4), "560", "PINK", "start", 10.5, "700")
    text(c, (m1.p(0.08, 0)[0], m1.p(0.08, 0)[1] - 6), "0.08", "PINK", "middle", 10.5, "700")

    m2 = Map(470, 282, 280 / 0.008, 240 / 560)
    axes(c, m2, 0.0082, 580, "strain ε", "σ (MPa)", [(0.001 * k, f"{0.001 * k:.3f}") for k in (1, 2, 4, 6, 8)],
         [(100 * k, str(100 * k)) for k in range(1, 6)])
    poly(c, m2.pts(sample(p15_curve, 0, 0.008, 200)), "ACC", 2.4)
    poly(c, [m2.p(0.002, 0), m2.p(0.002 + 520 / P15_E, 520)], "BLUE", 1.6, "6,4")
    text(c, m2.p(0.0034, 120), "parallel line", "BLUE", "start", 11)
    text(c, m2.p(0.0034, 85), "from ε = 0.002", "BLUE", "start", 11)
    pa = m2.p(0.0015, 310)
    dot(c, pa, 4.2, "HEAD", "HEAD")
    text(c, (pa[0] - 8, pa[1] - 6), "A", "HEAD", "end", 13, "700")
    line(c, m2.p(0, 310), pa, "HEAD", 0.9, "3,3")
    line(c, m2.p(0.0015, 0), pa, "HEAD", 0.9, "3,3")
    text(c, (m2.p(0, 310)[0] + 4, m2.p(0, 310)[1] - 4), "310", "HEAD", "start", 10.5, "700")
    text(c, (m2.p(0.0015, 0)[0] + 3, m2.p(0.0015, 0)[1] - 6), "0.0015", "HEAD", "start", 10.5, "700")
    py_ = m2.p(P15_EY, P15_SY)
    dot(c, py_, 4.2, "PINK", "PINK")
    text(c, (py_[0] + 8, py_[1] + 16), "Y", "PINK", "start", 13, "700")
    line(c, m2.p(0, P15_SY), py_, "PINK", 0.9, "3,3")
    text(c, (m2.p(0, P15_SY)[0] + 4, m2.p(0, P15_SY)[1] - 4), "450", "PINK", "start", 10.5, "700")
    return c


# --------------------------------------------------------------------------- P16: strain at the offset yield point
@figure("p16-offset-split", "Sketch of the 0.2 % offset construction: the elastic line from the origin, the parallel line "
        "from a strain of 0.002 and their meeting with the curve at the yield strength; the total strain at that point is "
        "split into the plastic offset 0.002 and the elastic part equal to the yield strength divided by E",
        "Strain at the 0.2 % offset yield point: plastic offset plus elastic part")
def p16_offset():
    c = Canvas(470, 320)
    m = Map(70, 240, 330 / 0.0085, 190 / 230)
    axes(c, m, 0.0088, 235, "strain ε", "σ (MPa)", [(0.002, "0.002")], [(170, sub("σ", "y"))], grid=False, size=12)
    E = 45000.0
    ey = 0.002 + 170 / E
    f = pchip([(120 / E, 120), (ey, 170), (0.0085, 205)])
    curve = [(e, E * e) for e in (0, 120 / E)] + sample(f, 120 / E, 0.0085, 80)
    poly(c, m.pts(curve), "ACC", 2.4)
    poly(c, [m.p(0.002, 0), m.p(0.002 + 200 / E, 200)], "BLUE", 1.6, "6,4")
    pY = m.p(ey, 170)
    dot(c, pY, 4.5, "PINK", "PINK")
    text(c, (pY[0] - 10, pY[1] - 10), "Y", "PINK", "end", 13, "700")
    line(c, m.p(0, 170), pY, "PINK", 0.9, "3,3")
    line(c, m.p(ey, 0), pY, "PINK", 0.9, "3,3")
    # strain split under the axis
    yb = m.p(0, 0)[1] + 46
    for a, b, lab, col in ((0, 0.002, "plastic 0.002", "BLUE"), (0.002, ey, "elastic " + sub("σ", "y") + "/E", "GREEN")):
        xa, xb = m.p(a, 0)[0], m.p(b, 0)[0]
        line(c, (xa, yb), (xb, yb), col, 2.2)
        line(c, (xa, yb - 5), (xa, yb + 5), col, 1.4)
        line(c, (xb, yb - 5), (xb, yb + 5), col, 1.4)
        text(c, ((xa + xb) / 2, yb + 18), lab, col, "middle", 11.5)
    text(c, (m.p(ey, 0)[0] + 8, yb + 4), "ε at Y", "PINK", "start", 11.5, "700")
    return c
