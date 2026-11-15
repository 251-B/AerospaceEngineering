"""Problem 12: particle on the axis Ox in an anharmonic potential V = m w0^2 (x^2 - b x^4) / 2."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis
from figures.mech import S, Scene, bold, dot1

PURPLE = "#8b5cf6"          # normal resultant R_perp (no kit token: a fixed colour, readable on every palette)


def _r0p():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">P</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


@figure("p12-axis-forces",
        "The segment between the turning points x1 and x2, with the sense of the velocity on each leg and the force at "
        "each turning point.",
        r"The particle sweeps $[x_1, x_2]$: velocity positive on the outward leg, negative on the return leg; at each "
        r"turning point the force points back into the interval.")
def axis_forces():
    sc = Scene(720, 350, (350, 190), 70)
    O = (0.0, 0.0)
    x1, x2, xp = -3.0, 4.2, 1.8
    sc.line((-4.6, 0.0), (4.9, 0.0), "EDGE", 1.2)
    sc.poly([(x1, -0.07), (x2, -0.07), (x2, 0.07), (x1, 0.07)], "ACC", 0.0, fill="ACC", close=True, opacity=0.40)
    for x, nm in ((x1, S("x", "1")), (x2, S("x", "2"))):
        sc.line((x, -0.14), (x, 0.14), "EDGE", 1.6)
        sc.label((x, 0.0), nm, "TEXT", "middle", 17, dy=28)
    fixed_axis(sc, O, 0, 1.2, bold("i"), off=(2, -12))
    fixed_axis(sc, O, 90, 1.2, bold("j"), off=(14, 4))
    axis_out(sc, O, bold("k"), off=(-20, -14))
    # position vector (black), parallel to the axis a little below it
    yr = -0.5
    sc.dashed((0.0, 0.0), (0.0, yr))
    sc.dashed((xp, 0.0), (xp, yr))
    sc.vec((0.0, yr), (xp, yr), None, "HEAD", 2.2, head=10)
    sc.label((xp / 2, yr), _r0p(), "HEAD", "middle", 17, dy=22)
    sc.dotp((xp, 0.0), 6.0)
    sc.label((xp, 0.0), "P", "HEAD", "start", 17, dx=8, dy=26)
    sc.vec((xp, 0.0), (xp, 1.0), None, PURPLE, 2.8, head=11)
    sc.label((xp, 1.0), bold("R") + S("", "⊥"), PURPLE, "start", 16, dx=10, dy=5)
    # forces at the turning points
    sc.vec((x1, 0.0), (x1 + 1.3, 0.0), None, "PINK", 2.8, head=11)
    sc.label((x1, 0.0), bold("F") + "(" + S("x", "1") + ") = −V′(" + S("x", "1") + ") > 0", "PINK", "start", 16, dy=-30)
    sc.vec((x2, 0.0), (x2 - 1.3, 0.0), None, "PINK", 2.8, head=11)
    sc.label((x2, 0.0), bold("F") + "(" + S("x", "2") + ") = −V′(" + S("x", "2") + ") < 0", "PINK", "end", 16, dy=-30)
    # velocity on each leg
    sc.vec((-2.0, 1.7), (2.0, 1.7), None, "GREEN", 2.6, head=11)
    sc.label((0.0, 1.7), "outward leg: " + dot1("x") + " > 0, from " + S("t", "A") + " to " + S("t", "B"), "GREEN", "middle", 16, dy=-12)
    sc.vec((2.0, -1.4), (-2.0, -1.4), None, "GREEN", 2.6, head=11)
    sc.label((0.0, -1.4), "return leg: " + dot1("x") + " < 0, from " + S("t", "B") + " to " + S("t", "C"), "GREEN", "middle", 16, dy=26)
    return sc


@figure("p12-potential",
        "The anharmonic potential compared with the harmonic parabola, with the energy level of an oscillation of "
        "amplitude a.",
        r"For $b > 0$ the potential lies below the harmonic parabola, so the particle moves more slowly and the period "
        r"grows with the amplitude; oscillations need $2ba^2 < 1$.")
def potential():
    SY = 1100.0 / 300.0            # world height per unit of V / (m w0^2)
    sc = Scene(760, 450, (380, 390), 300)
    a = 0.5
    V = lambda x: 0.5 * (x * x - x ** 4)
    E = V(a)
    W = lambda v: SY * v
    sc.vec((-1.0, 0.0), (1.05, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((1.05, 0.0), "x", "TEXT", "middle", 17, dx=12, dy=5)
    sc.vec((0.0, -0.02), (0.0, W(0.31)), None, "EDGE", 1.4, head=8)
    sc.label((0.0, W(0.31)), "V / (m ω₀²)", "TEXT", "start", 17, dx=12, dy=2)
    # harmonic parabola (b = 0), clipped at the top of the plot
    xh = math.sqrt(2 * 0.30)
    sc.curve(lambda x: (x, W(0.5 * x * x)), -xh, xh, 160, col="EDGE", w=1.8, dash="6 4")
    # allowed interval
    sc.poly([(-a, -0.035), (a, -0.035), (a, 0.035), (-a, 0.035)], "ACC", 0.0, fill="ACC", close=True, opacity=0.40)
    # energy level
    sc.line((-0.95, W(E)), (0.95, W(E)), "ACC", 2.0, "7 4")
    # anharmonic curve
    sc.curve(lambda x: (x, W(V(x))), -0.95, 0.95, 200, col="BLUE", w=2.8)
    xm = 1 / math.sqrt(2.0)
    for x in (-xm, xm):
        sc.dotp((x, W(V(x))), 4.5, "BLUE")
        sc.label((x, W(V(x))), "x² = 1/(2b)", "TEXT", "middle", 14, dy=-14)
    for x, nm in ((-a, "−a"), (a, "+a")):
        sc.line((x, W(E)), (x, 0.0), "EDGE", 1.2, "4 4")
        sc.dotp((x, W(E)), 4.5, "BLUE")
        sc.label((x, 0.0), nm, "TEXT", "middle", 16, dy=26)
    # V(a) - V(x) at a generic x
    xg = 0.2
    sc.vec((xg, W(V(xg))), (xg, W(E)), None, "ACC", 2.0, head=9)
    sc.vec((xg, W(E)), (xg, W(V(xg))), None, "ACC", 2.0, head=9)
    sc.label((xg, W(E)), "V(a) − V(x)", "ACC", "middle", 15, dy=-10)
    return sc
