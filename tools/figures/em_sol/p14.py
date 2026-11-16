"""Problem 14: particle on the axis Ox under F = m K x e^(x/a) i (potential barrier), launched from x = a."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis
from figures.mech import S, Scene, bold

PURPLE = "#8b5cf6"          # normal resultant R_perp (no kit token: a fixed colour, readable on every palette)
RED = "#ef4444"             # level of case 3

A = 3.0                     # drawn value of a


def _r0p():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">P</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


@figure("p14-axis-forces",
        "The axis Ox with the fixed basis, the launch at x = a towards the origin, and the force that pushes away from "
        "the origin on both sides.",
        r"Fixed basis ($\mathbf k$ out of the paper) and free-body diagram: $\mathbf F = mKx\,e^{x/a}\,\mathbf i$ points "
        r"away from $O$ on both sides, so the origin is a repelling equilibrium.")
def axis_forces():
    sc = Scene(820, 320, (330, 170), 75)
    O = (0.0, 0.0)
    sc.line((-4.2, 0.0), (6.0, 0.0), "EDGE", 1.2)
    for x, nm, dx in ((-A, "−a", 0), (0.0, "O", -14), (A, "a", 14)):
        sc.line((x, -0.12), (x, 0.12), "EDGE", 1.4)
        sc.label((x, 0.0), nm, "TEXT", "middle", 16, dx=dx, dy=26)
    fixed_axis(sc, O, 0, 0.8, bold("i"), off=(2, -12))
    fixed_axis(sc, O, 90, 1.2, bold("j"), off=(14, 4))
    axis_out(sc, O, bold("k"), off=(-20, -14))
    # position vector (black), parallel to the axis a little below it
    yr = -0.55
    sc.dashed((0.0, 0.0), (0.0, yr))
    sc.dashed((A, 0.0), (A, yr))
    sc.vec((0.0, yr), (A, yr), None, "HEAD", 2.2, head=10)
    sc.label((A / 2, yr), _r0p(), "HEAD", "middle", 17, dy=-16)
    # velocity of the launch, towards the origin
    sc.vec((A, 0.0), (A - 1.8, 0.0), None, "GREEN", 2.8, head=11)
    sc.label((A - 0.9, 0.0), "−" + S("v", "0") + " " + bold("i"), "GREEN", "middle", 16, dy=-16)
    # force at P and at the ghost position x = -a
    sc.vec((A, 0.0), (A + 2.7, 0.0), None, "PINK", 2.8, head=11)
    sc.label((A + 1.35, 0.0), bold("F") + " > 0 for x > 0", "PINK", "middle", 16, dy=-30)
    sc.vec((A, 0.0), (A, 1.0), None, PURPLE, 2.8, head=11)
    sc.label((A, 1.0), bold("R") + S("", "⊥"), PURPLE, "start", 16, dx=10, dy=5)
    sc.dotp((A, 0.0), 6.0)
    sc.label((A, 0.0), "P", "HEAD", "end", 17, dx=-9, dy=-10)
    sc.circle((-A, 0.0), 7.0 / sc.k, "HEAD", 1.6, "3 3")
    sc.vec((-A, 0.0), (-A - 1.0, 0.0), None, "PINK", 2.8, head=11)
    sc.label((-A - 0.5, 0.0), bold("F") + " < 0 for x < 0", "PINK", "middle", 16, dy=-16)
    sc.note((-A - 0.5, 0.0), "(not to scale)", "TEXT", "middle", 12, dy=-34)
    sc.note((6.0, -1.6), "S₀ inertial: no inertia forces", "TEXT", "end", 13)
    return sc


@figure("p14-potential",
        "The single barrier V = mKa(a - x) e^(x/a) with three energy levels: below, equal to and above the barrier top.",
        r"The launch point $x = a$ lies on the right slope of a barrier of height $mKa^2$; the comparison of "
        r"$\tfrac12 m v_0^2$ with that height separates reflection, asymptotic approach and crossing.")
def potential():
    sc = Scene(920, 440, (560, 210), 120)
    V = lambda u: (1.0 - u) * math.exp(u)
    # axes along the left and bottom edges
    xl, yb = -4.0, -1.2
    sc.vec((xl, yb), (1.7, yb), None, "EDGE", 1.4, head=8)
    sc.label((1.7, yb), "x/a", "TEXT", "start", 17, dx=10, dy=5)
    sc.vec((xl, yb), (xl, 1.5), None, "EDGE", 1.4, head=8)
    sc.label((xl, 1.5), "V/(mKa²)", "TEXT", "start", 17, dx=10, dy=2)
    for u in range(-4, 2):
        sc.line((u, yb - 0.03), (u, yb + 0.03), "EDGE", 1.3)
        sc.label((u, yb), "0" if u == 0 else str(u).replace("-", "−"), "TEXT", "middle", 14, dy=20)
    for v, nm in ((-1, "−1"), (0, "0"), (1, "1")):
        sc.line((xl - 0.03, v), (xl + 0.03, v), "EDGE", 1.3)
        sc.label((xl, v), nm, "TEXT", "end", 14, dx=-10, dy=5)
    # asymptote V -> 0
    sc.line((xl, 0.0), (1.0, 0.0), "EDGE", 1.2, "6 4")
    sc.note((-3.9, 0.0), "V → 0 as x → −∞", "TEXT", "start", 12, dy=16)
    # the three levels
    Ea, Eg, Er = 0.72, 1.0, 1.2      # case 1: the example of the solution, v0 = 1.2 (m = K = a = 1)
    xs = 0.608                      # (1 - u) e^u = 0.72
    sc.line((xl, Ea), (1.15, Ea), "ACC", 1.8, "7 4")
    sc.line((xl, Eg), (1.15, Eg), "GREEN", 1.8, "7 4")
    sc.line((xl, Er), (1.15, Er), RED, 1.8, "7 4")
    sc.note((-3.85, Ea), "case 1: v₀ < a√(2K)", "ACC", "start", 13, dy=20)
    sc.note((-3.85, Eg), "case 2: v₀ = a√(2K)", "GREEN", "start", 13, dy=-8)
    sc.note((-3.85, Er), "case 3: v₀ > a√(2K)", RED, "start", 13, dy=-8)
    # potential curve, clipped at the bottom of the plot
    sc.curve(lambda u: (u, V(u)), xl, 1.32, 240, col="BLUE", w=2.8)
    sc.dotp((0.0, 1.0), 4.5, "BLUE")
    sc.label((0.0, 1.0), "barrier top, unstable", "TEXT", "end", 14, dx=-12, dy=-10)
    sc.dotp((1.0, 0.0), 4.5, "BLUE")
    sc.label((1.0, 0.0), "launch point, V(a) = 0", "TEXT", "start", 14, dx=10, dy=-10)
    sc.dotp((xs, Ea), 4.5, "ACC")
    sc.label((xs, Ea), "x*", "ACC", "end", 16, dx=-8, dy=22)
    # case 1: towards x*, reflection, back to the right
    r = 0.09
    xc = xs + r
    sc.vec((1.1, Ea + r), (xc, Ea + r), None, "ACC", 2.0, head=9)
    sc.arc((xc, Ea), r, 90, 270, "ACC", 2.0)
    sc.vec((xc, Ea - r), (1.1, Ea - r), None, "ACC", 2.0, head=9)
    # case 2: approaches the top without reaching it
    sc.line((1.05, Eg), (0.35, Eg), "GREEN", 2.4)
    sc.line((0.35, Eg), (0.2, Eg), "GREEN", 2.4, "4 3")
    sc.vec((0.22, Eg), (0.12, Eg), None, "GREEN", 2.4, head=10)
    # case 3: crosses the barrier, to the left edge
    sc.vec((1.05, Er), (-3.95, Er), None, RED, 2.4, head=10)
    return sc
