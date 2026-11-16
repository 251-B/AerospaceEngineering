"""Problem 48: two particles joined by a string through the vertex of a paraboloid (meridian plane, view along k0, free-body diagram)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import ORANGE, PURPLE, RED, YELLOW, arrow, away, basis_view
from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

C = 0.8
RP = 1.0
ER = S(bold("e"), "R")
ETH = S(bold("e"), "θ")
K0, I0, J0 = S(bold("k"), "0"), S(bold("i"), "0"), S(bold("j"), "0")
TR = S(bold("t"), "R")
NH = bold("n̂")
THETA = 35.0


def _par(sc, col="HEAD", w=2.6):
    sc.curve(lambda r: (r, C * r * r), -1.4, 1.4, n=140, col=col, w=w)


def _along(sc, a, b, text, col, size, f, off):
    """Text running parallel to the segment a-b, on its upper side, `off` pixels away from the point at fraction f."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.degrees(math.atan2(by - ay, bx - ax))
    mx, my = ax + f * (bx - ax), ay + f * (by - ay)
    nx, ny = by - ay, -(bx - ax)
    n = math.hypot(nx, ny)
    if ny > 0:
        nx, ny = -nx, -ny
    x, y = mx + nx / n * off, my + ny / n * off
    sc.c.add(f'<text x="{x:.1f}" y="{y:.1f}" fill="{col}" font-size="{size}" text-anchor="middle" font-family="Newsreader, \'Times New Roman\', Times, serif" '
             f'style="font-variant-numeric:lining-nums" font-style="italic" transform="rotate({ang:.1f} {x:.1f} {y:.1f})">{text}</text>')


def _geom():
    P = (RP, C * RP * RP)
    rho = RP * math.sqrt(1 + C * C * RP * RP)
    sl = 2 * C * RP
    n = math.hypot(1.0, sl)
    t = (1 / n, sl / n)
    nh = (-sl / n, 1 / n)
    return P, rho, t, nh


@figure("p48-meridian",
        "Meridian section of the paraboloid with the string from O to P and down the axis to Q, the right triangle of legs R and c R squared, and the tangent and normal at P.",
        r"Meridian plane of $P$, $\mathbf e_\theta$ into the paper. The triangle of legs $R$ and $cR^2$ gives the length $\rho = R\sqrt{1 + c^2R^2}$ of string on the side of $P$; the tangent $\mathbf t_R = \mathbf e_R + 2cR\,\mathbf k_0$ rises with the slope $2cR$ and the normal points into the bowl.")
def meridian():
    sc = Scene(800, 600, (330, 300), 140)
    O = (0.0, 0.0)
    P, rho, t, nh = _geom()
    F = (RP, 0.0)
    Q = (0.0, -1.0)
    triangle(sc, [O, F, P], YELLOW, 0.28)
    # axis
    sc.vec(O, (0.0, 1.6), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 1.6), K0, "TEXT", "middle", 16, weight="700", dy=-10)
    sc.line(O, (0.0, -1.6), "EDGE", 1.3, "11 3 2 3")
    _par(sc)
    # slope triangle at P
    h = 0.5
    triangle(sc, [P, (P[0] + h, P[1]), (P[0] + h, P[1] + 2 * C * RP * h)], ORANGE, 0.20)
    sc.line(P, (P[0] + h, P[1]), "EDGE", 1.1, "5 4")
    sc.line((P[0] + h, P[1]), (P[0] + h, P[1] + 2 * C * RP * h), "EDGE", 1.1, "5 4")
    sc.label((P[0] + h / 2, P[1]), "1", "TEXT", "middle", 15, dy=18)
    sc.label((P[0] + h, P[1] + C * RP * h), "2 c R", "TEXT", "start", 15, dx=8, dy=5)
    right_angle(sc, (P[0] + h, P[1]), 180, 90, 0.07)
    # triangle O F P
    sc.line(O, F, "EDGE", 1.1, "5 4")
    sc.line(F, P, "EDGE", 1.1, "5 4")
    right_angle(sc, F, 180, 90, 0.1)
    sc.label((0.78, 0.0), "R", "TEXT", "middle", 16, dy=22)
    sc.label((RP, P[1] / 2), "c R²", "TEXT", "start", 15, dx=10, dy=5)
    # strings
    sc.line(O, P, "HEAD", 4.5)
    sc.line(O, Q, "HEAD", 4.5)
    _along(sc, O, P, "ρ = R √(1 + c² R²)", "HEAD", 15, 0.5, 14)
    sc.label((0.0, -0.5), "l − ρ", "HEAD", "end", 16, dx=-10, dy=5)
    sc.arc(O, 0.5, 0, math.degrees(math.atan2(P[1], P[0])), "GREEN", 1.8, head=True)
    # grey e_R at O
    sc.vec(O, (0.6, 0.0), None, "EDGE", 2.0, head=9)
    sc.label((0.6, 0.0), ER, "TEXT", "middle", 16, weight="700", dx=-2, dy=-14)
    # tangent and normal at P
    tt = (P[0] + 0.8 * t[0], P[1] + 0.8 * t[1])
    tn = (P[0] + 0.8 * nh[0], P[1] + 0.8 * nh[1])
    sc.vec(P, tt, None, ORANGE, 2.8, head=11)
    sc.vec(P, tn, None, ORANGE, 2.8, head=11)
    sc.label(tt, TR + " = " + ER + " + 2 c R " + K0, ORANGE, "start", 16, dx=8, dy=-4)
    sc.label(tn, NH, ORANGE, "end", 17, weight="700", dx=-8, dy=-6)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=7, dy=24)
    sc.dotp(Q, 5.5)
    sc.label(Q, "Q", "HEAD", "start", 17, dx=12, dy=5)
    axis_in(sc, O, None)
    sc.label(O, "O", "HEAD", "end", 16, dx=-14, dy=-10)
    sc.label(O, ETH, "HEAD", "end", 17, weight="700", dx=-14, dy=24)
    sc.note((-1.55, -1.5), ETH + " = " + K0 + " × " + ER + ", into the paper", "TEXT", "start", 13)
    return sc


@figure("p48-rotation-k",
        "View from above of the cylindrical basis turned by theta about k_0, with the parallel of P.",
        r"Rotation by $\theta$ about $\mathbf k_0$ (out of the paper); the triangle of $\mathbf e_\theta$ has its opposite leg along $-\mathbf i_0$, which gives its minus sign.")
def rotation_k():
    sc = Scene(860, 620, (330, 290), 90)
    O = (0.0, 0.0)
    R = 1.4
    basis_view(sc, O, THETA, (I0, J0), (ER, ETH), col="BLUE", L=2.0, u=1.3, axl=2.4, ang="θ", ra=0.65, rl=0.92,
               legs=("cos θ", "sin θ", "cos θ", "sin θ"), ls=14, cf=0.85, l1dx=8, l4=(27, "end", 13))
    sc.arc(O, R, 30, 358, "GREEN", 1.4, "7 5")
    pp = (R * math.cos(math.radians(THETA)), R * math.sin(math.radians(THETA)))
    sc.dotp(pp, 5.0)
    sc.label(pp, "projection of P", "HEAD", "start", 14, dx=12, dy=18)
    sc.label(_pol(O, R, 215), "parallel of P (R = 1.4)", "GREEN", "end", 14, italic=False, dx=-12, dy=14)
    axis_out(sc, O, None)
    sc.label(O, K0, "HEAD", "end", 17, weight="700", dx=-14, dy=-8)
    _spin(sc, O, 0.3, 200, 340, "positive about " + K0, (0, 64), "middle", size=13)
    _matrix(sc, 2.7, -1.5, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.78)
    return sc


@figure("p48-fbd",
        "Exploded free-body diagram: on P the weight, the tension towards the hole and the normal reaction; on Q the weight and the tension, with zero guide reaction.",
        r"Forces on $P$ and $Q$. The string pulls each particle towards $O$ with the same tension $T$; the paraboloid acts on $P$ only along $\hat{\mathbf n}$, and the guide on $Q$ only normal to the axis (it turns out to be zero).")
def fbd():
    sc = Scene(820, 620, (360, 260), 130)
    O = (0.0, 0.0)
    P, rho, t, nh = _geom()
    Q = (0.0, -1.0)
    _par(sc, "EDGE", 2.0)
    sc.vec(O, (0.0, 1.6), None, "EDGE", 1.2, head=8)
    sc.label((0.0, 1.6), K0, "TEXT", "middle", 16, weight="700", dy=-10)
    sc.line(O, (0.0, -1.7), "EDGE", 1.2, "11 3 2 3")
    sc.line(O, P, "EDGE", 1.2)
    sc.dotp(O, 3.0, "EDGE")
    sc.label(O, "O", "TEXT", "end", 16, dx=-12, dy=-10)
    # forces on P
    wt = arrow(sc, P, (0.0, -1.0), RED, 3.0, 12, 1.0)
    sc.label(wt, "−m g " + K0, RED, "start", 16, dx=8, dy=4)
    tp = arrow(sc, P, (-P[0] / rho, -P[1] / rho), "PINK", 3.0, 12, 1.1)
    sc.label(((P[0] + tp[0]) / 2, (P[1] + tp[1]) / 2), "−T " + bold("r") + S("", "P") + " / ρ", "PINK", "end", 16, dx=-6, dy=-18)
    tn = arrow(sc, P, nh, PURPLE, 3.0, 11, 0.7)
    sc.label(tn, "N " + NH, PURPLE, "end", 17, dx=-8, dy=-6)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=-10)
    # forces on Q
    wq = arrow(sc, Q, (0.0, -1.0), RED, 3.0, 12, 1.0)
    sc.label(wq, "−m g " + K0, RED, "start", 16, dx=8, dy=4)
    tq = arrow(sc, Q, (0.0, 1.0), "PINK", 3.0, 12, 1.1)
    sc.label((0.0, -0.45), "T " + K0, "PINK", "end", 17, dx=-10, dy=5)
    sc.dotp(Q, 5.5)
    sc.label(Q, "Q", "HEAD", "start", 17, dx=12, dy=-2)
    sc.label((0.2, -0.72), "guide reaction " + S("R", "x") + " " + I0 + " + " + S("R", "y") + " " + J0 + " = 0", PURPLE, "start", 14, italic=False, dy=-4)
    sc.note((-2.3, -2.2), "same tension T at both ends (massless string, smooth hole); inertial frame: no inertia forces", "TEXT", "start", 13)
    return sc
