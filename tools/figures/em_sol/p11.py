"""Problem 11: particle on the axis Ox in the inverted double well V = -(c/2)(x^2 - a^2)^2."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis
from figures.mech import S, Scene, bold

PURPLE = "#8b5cf6"          # normal resultant R_perp (no kit token: a fixed colour, readable on every palette)
RED = "#ef4444"             # level of case (b)

A = 3.0                     # drawn value of a in the axis figure


def _r0p():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">P</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


@figure("p11-axis-forces",
        "The axis Ox with the fixed basis; inside |x| < a the force points towards the origin, beyond a it points away.",
        r"Fixed basis ($\mathbf k$ out of the paper) and free-body diagram at two positions: the force "
        r"$2c\,x(x^2 - a^2)\,\mathbf i$ attracts towards $O$ inside the barriers and repels beyond them.")
def axis_forces():
    sc = Scene(800, 290, (262, 175), 75)
    O = (0.0, 0.0)
    s3 = A / math.sqrt(3.0)
    sc.line((-3.4, 0.0), (6.9, 0.0), "EDGE", 1.2)
    for x, nm in ((-A, "−a"), (-s3, None), (0.0, "0"), (s3, None), (A, "+a")):
        sc.line((x, -0.12), (x, 0.12), "EDGE", 1.4)
        if nm:
            sc.label((x, 0.0), nm, "TEXT", "middle", 16, dx=(-16 if nm == "0" else 0), dy=26)
    fixed_axis(sc, O, 0, 0.6, bold("i"), off=(2, -12))
    fixed_axis(sc, O, 90, 1.0, bold("j"), off=(14, 4))
    axis_out(sc, O, bold("k"), off=(-20, -14))
    x1, x2 = 1.5, 4.2
    # position vector of P1 (black), parallel to the axis a little below it
    yr = -0.55
    sc.dashed((0.0, 0.0), (0.0, yr))
    sc.dashed((x1, 0.0), (x1, yr))
    sc.vec((0.0, yr), (x1, yr), None, "HEAD", 2.2, head=10)
    sc.label((x1 / 2, yr), _r0p(), "HEAD", "middle", 17, dy=22)
    # forces
    sc.vec((x1, 0.0), (x1 - 0.75, 0.0), None, "PINK", 2.8, head=11)
    sc.label((x1 - 0.12, 0.0), bold("F") + " (towards O)", "PINK", "end", 16, dy=-34)
    sc.vec((x2, 0.0), (x2 + 2.5, 0.0), None, "PINK", 2.8, head=11)
    sc.label((x2 + 1.25, 0.0), bold("F") + " (away from O)", "PINK", "middle", 16, dy=-22)
    sc.vec((x1, 0.0), (x1, 1.0), None, PURPLE, 2.8, head=11)
    sc.label((x1, 1.0), bold("R") + S("", "⊥"), PURPLE, "start", 16, dx=10, dy=5)
    sc.dotp((x1, 0.0), 6.0)
    sc.label((x1, 0.0), S("P", "1"), "HEAD", "end", 17, dx=-8, dy=22)
    sc.dotp((x2, 0.0), 6.0)
    sc.label((x2, 0.0), S("P", "2"), "HEAD", "end", 17, dx=-8, dy=-10)
    sc.note((6.7, -1.35), "S₀ inertial: no inertia forces", "TEXT", "end", 13)
    return sc


@figure("p11-potential",
        "The inverted double well V = -(c/2)(x^2 - a^2)^2 with three energy levels and their allowed regions.",
        r"Sketch of the potential with the levels of cases (a), (b) and (c). Allowed regions ($V \le E$) are shaded; "
        r"turning points are the intersections of each level with the curve.")
def potential():
    SY = 1.7                       # world height per unit of V (a = c = 1)
    sc = Scene(940, 480, (400, 130), 190)
    V = lambda x: -0.5 * (x * x - 1.0) ** 2
    W = lambda v: SY * v
    xin, xout = math.sqrt(1 - math.sqrt(0.5)), math.sqrt(1 + math.sqrt(0.5))
    xb = math.sqrt(1 + math.sqrt(1.6))
    Ea, Ec, Eb = 0.15, -0.25, -0.8
    # axes
    sc.vec((-1.75, 0.0), (1.78, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((1.78, 0.0), "x", "TEXT", "middle", 17, dx=12, dy=5)
    sc.vec((0.0, W(-1.0)), (0.0, W(0.30)), None, "EDGE", 1.4, head=8)
    sc.label((0.0, W(0.30)), "V(x)", "TEXT", "start", 17, dx=12, dy=2)

    def band(x0, x1, e, col):
        h = 0.03
        sc.poly([(x0, W(e) - h), (x1, W(e) - h), (x1, W(e) + h), (x0, W(e) + h)], col, 0.0, fill=col, close=True,
                opacity=0.35)

    # case (a): whole axis
    sc.line((-1.7, W(Ea)), (1.7, W(Ea)), "ACC", 1.8, "7 4")
    band(-1.7, 1.7, Ea, "ACC")
    sc.vec((-1.55, W(Ea)), (-1.78, W(Ea)), None, "ACC", 2.0, head=9)
    sc.vec((1.55, W(Ea)), (1.78, W(Ea)), None, "ACC", 2.0, head=9)
    sc.label((1.78, W(Ea)), "(a) E > 0", "ACC", "start", 16, dx=12, dy=5)
    # case (c)
    sc.line((-1.7, W(Ec)), (1.7, W(Ec)), "GREEN", 1.8, "7 4")
    band(-xin, xin, Ec, "GREEN")
    band(xout, 1.7, Ec, "GREEN")
    band(-1.7, -xout, Ec, "GREEN")
    sc.label((1.7, W(Ec)), "(c) −c a" + S("", "", "4") + "/2 < E < 0", "GREEN", "start", 16, dx=12, dy=5)
    # case (b)
    sc.line((-1.7, W(Eb)), (1.7, W(Eb)), RED, 1.8, "7 4")
    band(xb, 1.7, Eb, RED)
    band(-1.7, -xb, Eb, RED)
    sc.label((1.7, W(Eb)), "(b) E < −c a" + S("", "", "4") + "/2", RED, "start", 16, dx=12, dy=5)
    # potential curve
    xm = math.sqrt(1 + math.sqrt(2.0))
    sc.curve(lambda x: (x, W(V(x))), -xm, xm, 240, col="BLUE", w=2.8)
    # maxima, minimum, inflection points
    for x in (-1.0, 1.0):
        sc.dotp((x, W(0.0)), 4.5, "BLUE")
        sc.label((x, W(0.0)), "unstable", "TEXT", "middle", 14, dy=-12)
    sc.dotp((0.0, W(-0.5)), 4.5, "BLUE")
    sc.label((0.0, W(-0.5)), "stable, −c a" + S("", "", "4") + "/2", "TEXT", "middle", 14, dy=24)
    for x in (-1 / math.sqrt(3), 1 / math.sqrt(3)):
        sc.circle((x, W(V(x))), 4.0 / sc.k, "BLUE", 1.6, fill="none")
    # turning points of case (c)
    for x, nm, anc, dx in ((-xout, "−x" + S("", "out"), "end", -8), (-xin, "−x" + S("", "in"), "start", 6),
                           (xin, "x" + S("", "in"), "end", -6), (xout, "x" + S("", "out"), "start", 8)):
        sc.dotp((x, W(Ec)), 4.0, "GREEN")
        sc.label((x, W(Ec)), nm, "GREEN", anc, 15, dx=dx, dy=-10)
    # oscillation in the well
    sc.vec((-0.33, W(Ec) - 0.07), (0.33, W(Ec) - 0.07), None, "GREEN", 2.0, head=9)
    sc.vec((0.33, W(Ec) - 0.07), (-0.33, W(Ec) - 0.07), None, "GREEN", 2.0, head=9)
    sc.note((0.0, W(Ec) - 0.07), "oscillation", "GREEN", "middle", 13, dy=20)
    # turning points of case (b)
    for x, nm, anc, dx in ((-xb, "−x" + S("", "out(b)"), "start", 6), (xb, "x" + S("", "out(b)"), "end", -6)):
        sc.dotp((x, W(Eb)), 4.0, RED)
        sc.label((x, W(Eb)), nm, RED, anc, 15, dx=dx, dy=20)
    # reflection at x_out(b): in along the upper leg, out along the lower one
    r = 0.075
    xc = xb + r
    sc.vec((1.66, W(Eb) + r), (xc, W(Eb) + r), None, RED, 2.0, head=9)
    sc.arc((xc, W(Eb)), r, 90, 270, RED, 2.0)
    sc.vec((xc, W(Eb) - r), (1.66, W(Eb) - r), None, RED, 2.0, head=9)
    return sc
