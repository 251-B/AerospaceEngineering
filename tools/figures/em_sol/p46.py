"""Problem 46: airplane P on a spring-damper landing gear taxiing at constant speed c over a sinusoidal runway."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis
from figures.mech import S, Scene, bold, dot1

RED = "#ef4444"             # weight
PURPLE = "#8b5cf6"          # horizontal resultant
BROWN = "#a16207"           # damper force
RUNWAY = "#4b5563"          # runway profile (dark grey)


def _vecs(name, sup):
    return bold(name) + f'<tspan baseline-shift="super" font-size="70%">{sup}</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


KAPPA = 1.0
H = 1.0
XB = 2.4                    # drawn value of c t
YP = 3.2                    # height of the airplane


@figure("p46-taxiway-plane",
        "The airplane P on its landing gear, whose lower end B follows the sinusoidal runway as the airplane taxies at speed c.",
        r"Main plane. The wheel $B$ follows the profile, so its height is $y_b = h\sin(\kappa c\,t)$; the length of the gear "
        r"is the difference of the heights of $P$ and $B$.")
def taxiway_plane():
    K = 64
    sc = Scene(1060, 390, (195, 255), K)
    O = (0.0, 0.0)
    yb = H * math.sin(KAPPA * XB)
    # runway profile and mean level
    sc.line((1.5, 0.0), (4 * math.pi + 0.3, 0.0), "EDGE", 1.0, "6 4")
    sc.curve(lambda x: (x, H * math.sin(KAPPA * x)), 0.0, 4 * math.pi, 300, col=RUNWAY, w=2.6)
    # axes
    fixed_axis(sc, O, 0, 1.4, bold("i"), off=(0, 24))
    fixed_axis(sc, O, 90, 1.4, bold("j"), off=(0, -10))
    axis_out(sc, O, bold("k"), off=(-16, 22))
    # projections of B (and P) on the axes
    sc.dashed((XB, 0.0), (XB, yb - 0.1))
    sc.label((XB, 0.0), "c t", "TEXT", "middle", 16, dy=28)
    sc.dashed((0.0, yb), (XB - 0.12, yb))
    sc.label((0.0, yb), S("y", "b") + " = h sin(κ c t)", "TEXT", "end", 15, dx=-12, dy=5)
    # the box (airplane), centred above B
    bw, bh = 1.5, 0.9
    sc.poly([(XB - bw / 2, YP - bh / 2), (XB + bw / 2, YP - bh / 2), (XB + bw / 2, YP + bh / 2), (XB - bw / 2, YP + bh / 2)],
            "HEAD", 2.0, fill="HEAD", close=True, opacity=0.14)
    sc.label((XB, YP), "m", "HEAD", "middle", 18, dx=-24, dy=6)
    sc.dotp((XB, YP), 3.5)
    sc.label((XB, YP), "P", "HEAD", "start", 17, dx=12, dy=6)
    # landing gear: spring and damper between B and the box
    ys0 = yb + 0.30
    ys1 = YP - bh / 2
    sc.line((XB, yb), (XB, ys0), "HEAD", 1.6)
    xs, xd = XB + 0.20, XB + 0.62
    sc.line((XB, ys0), (xd, ys0), "HEAD", 1.6)
    sc.line((xs, ys1), (xd, ys1), "HEAD", 1.6)
    sc.spring((xs, ys0), (xs, ys1), coils=7, amp=6.0, col="HEAD", lead=0.12)
    sc.damper((xd, ys0), (xd, ys1), col="HEAD")
    sc.circle((XB, yb), 5.5 / K, "HEAD", 1.8, fill="none")
    sc.label((XB, yb), "B", "HEAD", "start", 17, dx=18, dy=6)
    sc.label((XB - 0.12, (ys0 + ys1) / 2), "k", "TEXT", "end", 17, dx=-4, dy=5)
    sc.label((xd, (ys0 + ys1) / 2), "λ (part c)", "TEXT", "start", 16, dx=20, dy=5)
    # position vectors
    ang = math.atan2(YP, XB)
    sc.vec(O, (XB, YP), None, "HEAD", 2.2, head=10)       # arrowhead ends exactly at P
    ex = 2.03
    sc.label((ex / 2, ex * YP / XB / 2), _vecs("r", "P"), "HEAD", "end", 17, dx=-8, dy=-8)
    angb = math.atan2(yb, XB)
    eb = XB - 0.30
    sc.vec(O, (eb, eb * yb / XB), None, "HEAD", 2.2, head=10)
    sc.label((2.05, 0.24), _vecs("r", "B"), "HEAD", "middle", 17, dy=5)
    # length of the gear
    xl = xd + 2.1
    sc.line((xl, yb), (xl, YP), "EDGE", 1.1)
    for y in (yb, YP):
        sc.line((xl - 0.12, y), (xl + 0.12, y), "EDGE", 1.4)
    sc.label((xl, (yb + YP) / 2), S("l", "s") + " = y − " + S("y", "b"), "TEXT", "start", 16, dx=12, dy=5)
    # velocity of the airplane
    sc.vec((XB + bw / 2, YP), (XB + bw / 2 + 1.2, YP), None, "GREEN", 2.8, head=11)
    sc.label((XB + bw / 2 + 1.2, YP), "c " + bold("i"), "GREEN", "start", 17, dx=10, dy=5)
    # first trough: amplitude, and one wavelength below the profile
    xt = 1.5 * math.pi
    sc.line((xt, 0.0), (xt, -H), "EDGE", 1.1)
    for y in (0.0, -H):
        sc.line((xt - 0.12, y), (xt + 0.12, y), "EDGE", 1.4)
    sc.label((xt, -0.32), "h", "TEXT", "end", 17, dx=-10, dy=5)
    yw = -1.5
    sc.line((0.0, yw), (2 * math.pi, yw), "EDGE", 1.1)
    for x in (0.0, 2 * math.pi):
        sc.line((x, yw - 0.12), (x, yw + 0.12), "EDGE", 1.4)
    sc.label((math.pi, yw), "2π / κ", "TEXT", "middle", 16, dy=24)
    return sc


@figure("p46-fbd",
        "Free-body diagram of the airplane with the weight, the spring and damper forces along the gear and the horizontal resultant.",
        r"Forces on the airplane. The spring and the damper act along the vertical gear; the horizontal resultant vanishes "
        r"because the taxiing speed is constant.")
def fbd():
    K = 70
    sc = Scene(520, 480, (200, 255), K)
    bw, bh = 2.0, 1.2
    sc.poly([(-bw / 2, -bh / 2), (bw / 2, -bh / 2), (bw / 2, bh / 2), (-bw / 2, bh / 2)], "HEAD", 2.0, fill="HEAD", close=True, opacity=0.14)
    sc.label((-0.5, 0.2), "m", "HEAD", "middle", 18, dy=0)
    sc.dotp((0.0, 0.0), 4.0)
    # weight
    sc.vec((-0.3, 0.0), (-0.3, -2.5), None, RED, 3.0, head=12)
    sc.label((-0.3, -2.5), "−m g " + bold("j"), RED, "start", 17, dx=12, dy=5)
    # spring (compressed): pushes up
    sc.vec((0.3, 0.0), (0.3, 3.0), None, "PINK", 3.0, head=12)
    sc.label((0.3, 3.0), "−k(" + S("l", "s") + " − L) " + bold("j"), "PINK", "start", 17, dx=12, dy=5)
    # damper, gear extending: force down
    sc.vec((0.7, 0.0), (0.7, -0.8), None, BROWN, 3.0, head=12)
    sc.label((0.7, -0.8), "−λ(" + dot1("y") + " − " + dot1("y") + S("", "b") + ") " + bold("j"), BROWN, "start", 16, dx=12, dy=14)
    # horizontal resultant at the bottom of the box
    sc.vec((bw / 2, -0.45), (bw / 2 + 0.6, -0.45), None, PURPLE, 3.0, head=12)
    sc.label((bw / 2 + 0.6, -0.45), S("F", "x") + " " + bold("i") + " (= 0)", PURPLE, "start", 16, dx=10, dy=-10)
    # reference axes
    C = (-2.4, -1.6)
    fixed_axis(sc, C, 0, 0.9, bold("i"), off=(14, 5))
    fixed_axis(sc, C, 90, 0.9, bold("j"), off=(0, -10))
    axis_out(sc, C, None)
    sc.label(C, bold("k"), "HEAD", "end", 15, dx=-14, dy=18)
    sc.note((0.0, -3.1), "inertial frame: no inertia forces", "TEXT", "middle", 13)
    return sc
