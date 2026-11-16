"""Problem RB-40: disk with a torque rolling without slip inside a parabolic cavity y = x^2/(4R) (coordinates x_P, phi)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb12 import plane_rotation
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold, dot1, dot2

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
IB, JB = S(I, "b"), S(J, "b")
ET, EN = S(bold("e"), "t"), S(bold("e"), "n")
R = 1.0
XP = 2.0
RIM = 2.0 * math.sqrt(3.0) * R
SLOPE = XP / (2.0 * R)
BETA = math.degrees(math.atan(SLOPE))                    # 45 degrees
S_ = math.hypot(2.0 * R, XP)
ETD = (2.0 * R / S_, XP / S_)
END = (-XP / S_, 2.0 * R / S_)
P_PT = (XP, XP * XP / (4.0 * R))
G_PT = (P_PT[0] + R * END[0], P_PT[1] + R * END[1])


def _par(x):
    return x * x / (4.0 * R)


def _cavity_wall(sc, x0, x1, step=0.2, tick=0.15, n=120):
    """Parabola from x0 to x1 (thick line) with hatching ticks on the solid side (below)."""
    sc.poly([(x0 + (x1 - x0) * i / n, _par(x0 + (x1 - x0) * i / n)) for i in range(n + 1)], "HEAD", 2.6)
    x = x0 + step / 2
    while x <= x1:
        y = _par(x)
        sc.line((x, y), (x - tick * 0.75, y - tick), "EDGE", 1.0)
        x += step


# ------------------------------------------------------------------------------------------------ rb40-tangent
@figure("rb40-tangent",
        "The parabola with the tangent triangle at the contact point P and the centre G on the normal.",
        r"At $P$ the tangent rises $x_P$ over a horizontal run $2R$: $\cos\beta = 2R/s$, $\sin\beta = x_P/s$. $G$ is at "
        r"$R\,\mathbf e_n$ from $P$, on the concave side.")
def tangent():
    sc = Scene(1160, 600, (560, 500), 118)
    O = (0.0, 0.0)
    gx = RIM + 1.45
    # ground at y = 3R beyond the rims
    for sgn in (1, -1):
        a, b = (sgn * RIM, 3.0 * R), (sgn * gx, 3.0 * R)
        sc.ground(a, b, -1, step=10, length=9) if sgn > 0 else sc.ground(b, a, -1, step=10, length=9)
        sc.line((sgn * RIM, 3.0 * R - 0.09), (sgn * RIM, 3.0 * R + 0.09), "TEXT", 1.2)
    sc.label((RIM, 3.0 * R), "y = 3R", "TEXT", "middle", 14, italic=False, dy=-22)
    sc.label((-RIM, 3.0 * R), "y = 3R", "TEXT", "middle", 14, italic=False, dy=-22)
    _cavity_wall(sc, -RIM, RIM)
    # axes and the vertex
    fixed_axis(sc, O, 0, 4.4, I0, off=(16, 6))
    fixed_axis(sc, O, 90, 3.75, J0, off=(14, 0))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, K0 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=32)
    sc.label(O, "O", "HEAD", "middle", 17, dx=16, dy=-10)
    # abscissa of P
    sc.dashed(P_PT, (XP, 0.0))
    sc.dim((0.0, -0.22), (XP, -0.22), S("x", "P"), off=(0, 22))
    sc.dashed((0.0, 0.0), (0.0, -0.3))
    sc.dashed((XP, 0.0), (XP, -0.3))
    # tangent triangle at P
    foot = (P_PT[0] + 2.0 * R, P_PT[1])
    tip = (foot[0], foot[1] + XP)
    triangle(sc, [P_PT, foot, tip], ORANGE, 0.26)
    sc.dashed(foot, tip)
    right_angle(sc, foot, 180, 90, 0.09)
    sc.label(((P_PT[0] + foot[0]) / 2, P_PT[1]), "2R", "TEXT", "middle", 15, dy=22)
    sc.label((foot[0], (foot[1] + tip[1]) / 2), S("x", "P"), "TEXT", "start", 16, dx=12, dy=5)
    sc.label((foot[0] - 0.1, P_PT[1] + 0.5), "s = √(4R² + " + S("x", "P") + "²)", "TEXT", "end", 15, dx=0, dy=5)
    sc.arc(P_PT, 0.42, 0.0, BETA, "GREEN", 1.8, head=True)
    sc.label(add(P_PT, d(BETA / 2), 0.42), "β", "GREEN", "middle", 17, dx=22, dy=2)
    # the disk and the normal
    sc.poly(circle_pts(G_PT, R), "HEAD", 1.8, fill="EDGE", close=True, opacity=0.08)
    sc.dashed(P_PT, G_PT)
    sc.label(add(P_PT, END, 0.8), "R " + EN, "TEXT", "end", 15, weight="700", dx=-12, dy=6)
    unit(sc, P_PT, BETA, 0.8, ET, "GREEN", off=(14, 20))
    unit(sc, P_PT, BETA + 90.0, 0.6, EN, "GREEN", off=(16, -4))
    sc.mass(G_PT, None, r=4.5, col="BLUE")
    sc.label(G_PT, "G", "HEAD", "middle", 17, dx=-4, dy=-14)
    sc.mass(P_PT, None, r=4.5, col="BLUE")
    sc.label(P_PT, "P", "HEAD", "middle", 17, dx=12, dy=26)
    sc.note((-3.4, -0.55), "R = 1,  " + "x_P = 2  (β = 45°)", "TEXT", "start", 13)
    return sc


# ------------------------------------------------------------------------------------------------ rb40-rot-phi
PHI = 55.0
LU = 0.82


@figure("rb40-rot-phi",
        "The body basis of the disk turned counterclockwise by phi from the fixed basis.",
        r"Rotation about $\mathbf k_0$ (⊙) by $\phi$, measured from $\mathbf i_0$ as in the statement figure; "
        r"$\boldsymbol\omega_{b0} = \dot\phi\,\mathbf k_0$.")
def rot_phi():
    def pre(sc):
        sc.poly(circle_pts((0.0, 0.0), R), "HEAD", 1.8, fill="EDGE", close=True, opacity=0.07)

    def post(sc):
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=-16, dy=-12)
        sc.spin((0.0, 0.0), 1.3, 12.0, 80.0, "", "PINK")
        sc.label(add((0.0, 0.0), d(46.0), 1.3), "Q " + K0, "PINK", "start", 17, weight="700", dx=14, dy=-8)
    return plane_rotation(820, 700, (380, 380), 200, PHI, (I0, J0, IB, JB), K0 + " (⊙)", ("φ", ""), None,
                          extra_pre=pre, extra_post=post, out_off=(-26, 30), L=LU)


# ------------------------------------------------------------------------------------------------ rb40-fbd
@figure("rb40-fbd",
        "Free-body diagram of the disk: weight, the torque Q and the normal and friction forces at P.",
        r"Free-body diagram. The contact force at $P$ has a normal part $N\,\mathbf e_n$ ($N \ge 0$) and a friction "
        r"$T_f\,\mathbf e_t$; the torque $Q\,\mathbf k_0$ is a couple.")
def fbd():
    sc = Scene(860, 660, (230, 540), 150)
    _cavity_wall(sc, -0.9, 3.3)
    sc.poly(circle_pts(G_PT, R), "HEAD", 2.2, fill="EDGE", close=True, opacity=0.08)
    # weight and its components along -e_t and -e_n (dashed rectangle)
    W = 0.6
    sc.line(G_PT, add(G_PT, END, -R), "EDGE", 1.4, "5 4")           # arm G-P (the normal N lies over its lower part)
    ft = add(G_PT, ETD, -W * math.sin(math.radians(BETA)))
    fn = add(G_PT, END, -W * math.cos(math.radians(BETA)))
    tipw = (G_PT[0], G_PT[1] - W)
    sc.dashed(tipw, ft)
    sc.dashed(tipw, fn)
    sc.vec(G_PT, ft, None, "EDGE", 1.5, head=8)
    sc.vec(G_PT, fn, None, "EDGE", 1.5, head=8)
    sc.vec(G_PT, tipw, "mg", "PINK", 3.2, name_off=(-24, 8), size=18, head=12)
    sc.label(ft, "mg sin β", "TEXT", "end", 14, dx=-8, dy=6)
    sc.label(fn, "mg cos β", "TEXT", "start", 14, dx=8, dy=-8)
    # reactions at P
    sc.vec(P_PT, add(P_PT, END, 0.4), "N", "GREEN", 3.2, name_off=(-18, 24), size=18, head=12)
    sc.vec(P_PT, add(P_PT, ETD, 0.9), "", "GREEN", 3.2, head=12)
    sc.label(add(P_PT, ETD, 0.9), S("T", "f"), "GREEN", "start", 18, weight="700", dx=10, dy=24)
    # torque
    sc.spin(G_PT, 0.45, 25.0, 150.0, "Q", "PINK", name_r=0.66, size=18)
    # label of the arm
    am = add(G_PT, END, -0.3)
    sc.line(am, (am[0] + 0.14, am[1] + 0.26), "TEXT", 0.9)
    sc.label((am[0] + 0.14, am[1] + 0.26), "−R " + EN, "TEXT", "start", 14, weight="700", dx=4, dy=-4)
    # basis of the point P, in a corner of the cavity
    B0 = (-0.65, 2.05)
    unit(sc, B0, BETA, 0.7, ET, "GREEN", off=(16, 18))
    unit(sc, B0, BETA + 90.0, 0.7, EN, "GREEN", off=(-14, -4))
    sc.note((B0[0] - 0.2, B0[1] - 0.45), "basis at P", "TEXT", "start", 13)
    for p, nm, off in ((P_PT, "P", (10, 28)), (G_PT, "G", (-16, -10))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    return sc
