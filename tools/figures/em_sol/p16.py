"""Problem 16: ball falling in air with quadratic drag (axis i pointing down) and its dimensionless time laws."""
import math

from figures.em_solutions import axis_out, figure
from figures.mech import S, Scene, bold

ORANGE = "#f97316"          # drag (no kit token: a fixed colour, readable on every palette)
RED = "#ef4444"             # weight


def _r0p():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">P</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


@figure("p16-fall-axis",
        "The football P falling along the vertical through the release point O, with the downward axis i and the distance fallen s.",
        r"Plane of the fall. The axis $\mathbf i$ points down, so the distance fallen $s$ and the velocity $v$ are "
        r"positive during the whole motion.")
def fall_axis():
    W, H, K = 520, 470, 56
    sc = Scene(W, H, (250, 60), K)
    sc.line((0.0, 0.0), (0.0, -6.9), "EDGE", 1.2, "6 4")
    axis_out(sc, (0.0, 0.0), bold("k"), off=(18, -14))
    sc.vec((0.0, 0.0), (0.0, -1.2), bold("i"), "BLUE", 2.6, name_off=(-14, 4), size=17, head=11)
    sc.vec((0.0, 0.0), (-1.2, 0.0), bold("j"), "BLUE", 2.6, name_off=(0, 24), size=17, head=11)
    sc.circle((0.0, 0.0), 0.3, "HEAD", 1.3, "3 3")
    sc.label((0.0, 0.0), "t = 0, v = 0", "TEXT", "end", 14, dx=-24, dy=48)
    sc.circle((0.0, -5.0), 0.3, "HEAD", 1.8, fill="HEAD", opacity=0.35)
    sc.label((0.0, -5.0), "P", "HEAD", "end", 17, dx=-22, dy=5)
    xr = 0.15
    sc.vec((xr, 0.0), (xr, -4.68), None, "HEAD", 2.2, head=10)
    sc.label((xr, -2.5), _r0p() + " = s " + bold("i"), "HEAD", "start", 17, dx=14, dy=5)
    xd = 2.2
    sc.line((xd, 0.0), (xd, -5.0), "EDGE", 1.1)
    for y in (0.0, -5.0):
        sc.line((xd - 0.12, y), (xd + 0.12, y), "EDGE", 1.4)
    sc.label((xd, -2.5), "s", "TEXT", "start", 17, dx=12, dy=5)
    xv = 0.3 + 0.5
    sc.vec((xv, -5.0), (xv, -6.5), None, "GREEN", 2.8, head=11)
    sc.label((xv, -6.5), "v " + bold("i"), "GREEN", "start", 16, dx=12, dy=5)
    return sc


@figure("p16-fbd",
        "Free-body diagram of the falling ball with its weight pointing down and the drag pointing up.",
        r"Forces on the ball while it falls. The weight acts along $\mathbf i$ and the drag, opposite to the downward "
        r"velocity, along $-\mathbf i$ with magnitude $\tfrac12\rho S C_D v^2$; they balance at the terminal speed.")
def fbd():
    K = 70
    sc = Scene(600, 430, (290, 135), K)
    O = (0.0, 0.0)
    sc.circle(O, 1.0, "HEAD", 2.0, fill="HEAD", opacity=0.14)
    sc.vec((0.0, 0.0), (0.0, -3.0), None, RED, 3.0, head=12)
    sc.label((0.0, -3.0), "m g " + bold("i"), RED, "start", 17, dx=14, dy=5)
    # drag at v = 0.6 v_t: 0.36 of the weight
    sc.vec((0.0, 0.0), (0.0, 3 * 0.36), None, ORANGE, 3.0, head=12)
    sc.label((0.0, 3 * 0.36), "−(1/2) ρ S " + S("C", "D") + " " + S("v", None, "2") + " " + bold("i"), ORANGE, "end", 17, dx=-16, dy=-2)
    sc.dotp(O, 4.0)
    sc.vec((2.0, 0.5), (2.0, -0.7), None, "GREEN", 2.2, head=10)
    sc.label((2.0, -0.7), "v " + bold("i") + ", v > 0", "GREEN", "middle", 16, dy=24)
    C = (-3.0, -1.0)
    axis_out(sc, C, bold("k"), off=(-16, -12))
    sc.vec(C, (C[0], C[1] - 0.8), bold("i"), "BLUE", 2.4, name_off=(-14, 4), size=16, head=10)
    sc.vec(C, (C[0] - 0.8, C[1]), bold("j"), "BLUE", 2.4, name_off=(0, 22), size=16, head=10)
    sc.note((0.0, -3.9), "free ball: no reaction; inertial frame: no inertia forces", "TEXT", "middle", 13)
    return sc


@figure("p16-time-laws",
        "Graph of the dimensionless velocity and distance fallen against the dimensionless time, with the free-fall and "
        "terminal asymptotes.",
        r"Time laws of the fall. The velocity tends to the terminal speed and the distance fallen tends to a straight "
        r"line of slope 1 shifted by $\ln 2$; at early times both follow free fall.")
def time_laws():
    K = 115
    sc = Scene(680, 520, (80, 460), K)
    tanh, lncosh = math.tanh, lambda u: math.log(math.cosh(u))
    sc.vec((0.0, 0.0), (4.25, 0.0), None, "EDGE", 1.4, head=8)
    sc.vec((0.0, 0.0), (0.0, 3.75), None, "EDGE", 1.4, head=8)
    for u in range(0, 5):
        sc.line((u, -0.03), (u, 0.03), "EDGE", 1.3)
        sc.label((u, 0.0), str(u), "TEXT", "middle", 14, dy=22)
    for v, nm in ((0.5, "0.5"), (1, "1"), (2, "2"), (3, "3")):
        sc.line((-0.03, v), (0.03, v), "EDGE", 1.3)
        sc.label((0.0, v), nm, "TEXT", "end", 14, dx=-10, dy=5)
    sc.label((0.0, 0.0), "0", "TEXT", "end", 14, dx=-10, dy=5)
    sc.label((2.1, 0.0), "u = g t / " + S("v", "t"), "TEXT", "middle", 16, dy=48)
    # terminal asymptote
    sc.line((0.0, 1.0), (4.1, 1.0), "EDGE", 1.2, "6 4")
    # free fall v/vt = u
    sc.line((0.0, 0.0), (1.2, 1.2), "GREEN", 1.3, "5 4")
    sc.label((1.2, 1.2), "free fall: u", "GREEN", "end", 15, dx=-6, dy=-12)
    # free-fall distance u^2/2
    sc.curve(lambda u: (u, u * u / 2), 0.0, 1.6, 60, col="HEAD", w=1.4, dash="1.5 3")
    sc.label((1.6, 1.28), "free fall: u²/2", "HEAD", "end", 15, dx=-2, dy=-34)
    # late-time asymptote
    sc.line((1.5, 1.5 - math.log(2)), (4.0, 4.0 - math.log(2)), "HEAD", 1.3, "6 4")
    sc.label((4.0, 4.0 - math.log(2)), "u − ln 2", "HEAD", "start", 15, dx=12, dy=22)
    # curves
    sc.curve(lambda u: (u, tanh(u)), 0.0, 4.0, 160, col="GREEN", w=2.8)
    sc.curve(lambda u: (u, lncosh(u)), 0.0, 4.0, 160, col="HEAD", w=2.8)
    sc.label((3.0, 1.0), "v / " + S("v", "t") + " = tanh u", "GREEN", "middle", 16, dy=26)
    sc.label((3.0, lncosh(3.0)), "s g / " + S("v", "t", "2") + " = ln cosh u", "HEAD", "end", 16, dx=-14, dy=-14)
    return sc
