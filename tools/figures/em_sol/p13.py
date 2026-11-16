"""Problem 13: particle on the axis Ox in the cubic potential V = m g a (y^3 - 3y), y = x/a, launched from x = a."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis
from figures.mech import S, Scene, bold

PURPLE = "#8b5cf6"          # normal resultant R_perp (no kit token: a fixed colour, readable on every palette)

A = 2.5                     # drawn value of a


def _r0p():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">P</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


@figure("p13-axis-and-forces",
        "The axis Ox with the fixed basis and the particle launched from x = a towards positive x.",
        r"Fixed basis ($\mathbf k$ out of the paper), launch point $x = a$ and initial velocity "
        r"$\sqrt{8ga}\,\mathbf i$; the marked points are the barrier top, the bottom of the well and the turning point.")
def axis_and_forces():
    sc = Scene(720, 300, (250, 150), 70)
    O = (0.0, 0.0)
    sc.line((-3.5, 0.0), (6.2, 0.0), "EDGE", 1.2)
    for x, nm, dx, sub in ((-A, "−a", 0, "barrier top (unstable)"), (0.0, "O", -14, None),
                           (A, "a", 14, "bottom of the well (stable)"), (2 * A, "2a", 0, "turning point")):
        sc.line((x, -0.12), (x, 0.12), "EDGE", 1.4)
        sc.label((x, 0.0), nm, "TEXT", "middle", 16, dx=dx, dy=26)
        if sub:
            sc.note((x, 0.0), sub, "TEXT", "middle", 12, dy=64)
    fixed_axis(sc, O, 0, 1.0, bold("i"), off=(2, -12))
    fixed_axis(sc, O, 90, 1.2, bold("j"), off=(14, 4))
    axis_out(sc, O, bold("k"), off=(-20, -14))
    # position vector (black), parallel to the axis a little below it
    yr = -0.5
    sc.dashed((0.0, 0.0), (0.0, yr))
    sc.dashed((A, 0.0), (A, yr))
    sc.vec((0.0, yr), (A, yr), None, "HEAD", 2.2, head=10)
    sc.label((A / 2, yr), _r0p(), "HEAD", "middle", 17, dy=-16)
    # launch velocity
    sc.vec((A, 0.0), (A + 2.0, 0.0), None, "GREEN", 2.8, head=11)
    sc.label((A + 1.0, 0.0), S("v", "0") + " = √(8 g a)", "GREEN", "middle", 16, dy=-16)
    sc.dotp((A, 0.0), 6.0)
    return sc


@figure("p13-free-body",
        "Free-body diagrams at three positions: the force vanishes at the bottom of the well and points back towards it "
        "on each side.",
        r"The conservative force $-3mg\,(y^2 - 1)\,\mathbf i$ is positive between $-a$ and $a$, zero at $a$ and negative "
        r"beyond it; at the turning point $2a$ it equals $-9mg\,\mathbf i$.")
def free_body():
    sc = Scene(720, 405, (230, 100), 60)
    ys = (0.0, -1.9, -3.8)
    xs = (0.0, A, 2 * A)
    names = ("x = 0", "x = a", "x = 2a")
    for y, x, nm in zip(ys, xs, names):
        sc.line((-1.0, y), (6.0, y), "EDGE", 1.2)
        sc.dotp((x, y), 8.0)
        sc.label((x, y), nm, "TEXT", "middle", 16, dy=26)
    # x = 0: force along +i, 3 units
    sc.vec((0.0, ys[0]), (3.0, ys[0]), None, "PINK", 2.8, head=11)
    sc.label((1.5, ys[0]), bold("F") + " = 3mg " + bold("i"), "PINK", "middle", 16, dy=-14)
    # x = a: no force, only the normal resultant
    sc.vec((A, ys[1]), (A, ys[1] + 0.9), None, PURPLE, 2.8, head=11)
    sc.label((A, ys[1] + 0.9), bold("R") + S("", "⊥"), PURPLE, "start", 16, dx=10, dy=5)
    sc.label((A, ys[1]), bold("F") + " = 0", "PINK", "end", 16, dx=-14, dy=-12)
    # x = 2a: force along -i, 9 units capped at 4.5 (break mark)
    sc.vec((2 * A, ys[2]), (2 * A - 4.5, ys[2]), None, "PINK", 2.8, head=11)
    xb = 2 * A - 2.25
    for dx in (-0.06, 0.06):
        sc.line((xb + dx - 0.07, ys[2] - 0.22), (xb + dx + 0.07, ys[2] + 0.22), "HEAD", 1.6)
    sc.label((xb, ys[2]), bold("F") + " = −9mg " + bold("i"), "PINK", "middle", 16, dy=-30)
    sc.note((5.9, -4.75), "S₀ inertial: no inertia forces", "TEXT", "end", 13)
    return sc


@figure("p13-potential",
        "The cubic potential with the energy level 2mga, tangent at the barrier top and meeting the curve at the "
        "turning point y = 2.",
        r"The energy equals the barrier top $V(-a) = 2mga$: the particle turns at $x = 2a$ and then creeps towards "
        r"$x = -a$, which it reaches only as $t \to \infty$.")
def potential():
    SY = 60.0 / 110.0              # world height per unit of V / (m g a)
    sc = Scene(780, 560, (340, 290), 110)
    V = lambda y: y ** 3 - 3 * y
    W = lambda v: SY * v
    green = "GREEN"
    sc.vec((-2.3, 0.0), (2.75, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((2.75, 0.0), "y = x/a", "TEXT", "start", 17, dx=10, dy=5)
    sc.vec((0.0, W(-3.3)), (0.0, W(4.3)), None, "EDGE", 1.4, head=8)
    sc.label((0.0, W(4.3)), "V/(mga)", "TEXT", "start", 17, dx=12, dy=2)
    for y, nm in ((-1.0, "−1"), (1.0, "1"), (2.0, "2")):
        sc.line((y, -0.05), (y, 0.05), "EDGE", 1.3)
        sc.label((y, 0.0), nm, "TEXT", "middle", 14, dx=(-12 if y == 1.0 else 0), dy=20)
    # allowed region swept on the axis
    sc.poly([(-1.0, -0.035), (2.0, -0.035), (2.0, 0.035), (-1.0, 0.035)], "ACC", 0.0, fill="ACC", close=True, opacity=0.40)
    # energy level
    sc.line((-2.3, W(2.0)), (2.65, W(2.0)), "ACC", 2.0, "7 4")
    # potential curve, clipped to -3 <= V <= 4
    ylo, yhi = -2.1038, 2.195
    sc.curve(lambda y: (y, W(V(y))), ylo, yhi, 240, col="BLUE", w=2.8)
    sc.dotp((-1.0, W(2.0)), 4.5, "BLUE")
    sc.label((-1.0, W(2.0)), "barrier top, unstable", "TEXT", "middle", 14, dx=26, dy=-14)
    sc.note((-2.3, W(2.0)), "separatrix", "ACC", "start", 12, dy=-8)
    sc.dotp((1.0, W(-2.0)), 4.5, "BLUE")
    sc.label((1.0, W(-2.0)), "launch point, stable", "TEXT", "start", 14, dx=-70, dy=28)
    sc.dotp((2.0, W(2.0)), 4.5, "ACC")
    sc.label((2.0, W(2.0)), "turning point y = 2", "ACC", "end", 14, dx=-10, dy=-14)
    # kinetic energy at y = 1
    sc.vec((1.0, W(-2.0)), (1.0, W(2.0)), None, "ACC", 2.0, head=9)
    sc.vec((1.0, W(2.0)), (1.0, W(-2.0)), None, "ACC", 2.0, head=9)
    sc.label((1.0, W(0.9)), "T = 4mga", "ACC", "end", 15, dx=-10, dy=-2)
    sc.note((1.0, W(0.9)), "(largest)", "ACC", "end", 12, dx=-10, dy=14)
    # sense of motion: outward leg 1 -> 2, return leg 2 -> towards -1 (never reaching it)
    sc.vec((1.0, W(-2.8)), (2.0, W(-2.8)), None, green, 2.2, head=10)
    sc.note((2.0, W(-2.8)), "outward leg", green, "start", 12, dx=10, dy=4)
    sc.line((2.0, W(-3.2)), (-0.2, W(-3.2)), green, 2.2)
    sc.line((-0.2, W(-3.2)), (-0.75, W(-3.2)), green, 2.2, "5 4")
    sc.vec((-0.7, W(-3.2)), (-0.85, W(-3.2)), None, green, 2.2, head=10)
    sc.note((2.0, W(-3.2)), "return leg", green, "start", 12, dx=10, dy=4)
    return sc


@figure("p13-position-time",
        "The position x/a as a function of time: up to 2 at t1, then down towards the asymptote -1.",
        r"Explicit time law $x(t) = a\left[2 - 3\tanh^2\left(\sqrt{3g/(2a)}\,t - \operatorname{arctanh}(1/\sqrt3)\right)\right]$: "
        r"one formula for both legs, with the asymptote $x = -a$.")
def position_time():
    sc = Scene(780, 560, (90, 330), 130)
    c0 = math.atanh(1 / math.sqrt(3.0))
    f = lambda t: 2.0 - 3.0 * math.tanh(math.sqrt(1.5) * t - c0) ** 2
    t1 = c0 / math.sqrt(1.5)
    sc.vec((0.0, 0.0), (4.2, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((4.2, 0.0), "t √(g/a)", "TEXT", "start", 17, dx=10, dy=5)
    sc.vec((0.0, -1.2), (0.0, 2.3), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 2.3), "x/a", "TEXT", "start", 17, dx=12, dy=2)
    for t in (1, 2, 3, 4):
        sc.line((t, -0.05), (t, 0.05), "EDGE", 1.3)
        sc.label((t, 0.0), str(t), "TEXT", "middle", 14, dy=20)
    for v, nm in ((-1, "−1"), (1, "1"), (2, "2")):
        sc.line((-0.05, v), (0.05, v), "EDGE", 1.3)
        sc.label((0.0, v), nm, "TEXT", "end", 14, dx=-10, dy=5)
    sc.line((0.0, 2.0), (4.0, 2.0), "EDGE", 1.2, "6 4")
    sc.note((4.0, 2.0), "turning point", "TEXT", "end", 13, dy=-8)
    sc.line((0.0, -1.0), (4.0, -1.0), "EDGE", 1.2, "6 4")
    sc.note((4.0, -1.0), "asymptote x = −a", "TEXT", "end", 13, dy=18)
    sc.curve(lambda t: (t, f(t)), 0.0, 4.0, 200, col="GREEN", w=2.8)
    sc.dotp((0.0, 1.0), 4.5, "GREEN")
    sc.label((0.0, 1.0), "launch", "GREEN", "start", 15, dx=10, dy=22)
    sc.dotp((t1, 2.0), 4.5, "GREEN")
    sc.line((t1, 2.0), (t1, 0.0), "EDGE", 1.2, "4 4")
    sc.label((t1, 2.0), S("t", "1") + " = 0.5376 √(a/g)", "GREEN", "start", 15, dx=10, dy=-12)
    sc.dotp((2.0, f(2.0)), 4.0, "GREEN")
    return sc
