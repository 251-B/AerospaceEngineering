"""Problem 50: double pendulum (plane of motion, rotations about k, free-body diagram)."""
import math

from figures.em_sol.p31 import _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import ORANGE, PURPLE, RED, YELLOW, arrow, away, basis_view
from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

L = 1.6
TH, PH = 25.0, 45.0
I1, J1 = S(bold("i"), "1"), S(bold("j"), "1")
I2, J2 = S(bold("i"), "2"), S(bold("j"), "2")
G2 = "#10b981"


def _pt(a):
    a = math.radians(a)
    return (L * math.sin(a), -L * math.cos(a))


O = (0.0, 0.0)
P = _pt(TH)
Q = (P[0] + L * math.sin(math.radians(PH)), P[1] - L * math.cos(math.radians(PH)))


def _add(p, v, k=1.0):
    return (p[0] + k * v[0], p[1] + k * v[1])


def _dirs(a):
    a = math.radians(a)
    return (math.sin(a), -math.cos(a)), (math.cos(a), math.sin(a))


@figure("p50-plane",
        "Double pendulum with the bars OP and PQ, the right triangles of legs l sin and l cos of each angle and the bases of the two bars.",
        r"Plane of the motion, $\mathbf k$ out of the paper. The triangles give $\mathbf r_0^P = \ell\sin\theta\,\mathbf i - \ell\cos\theta\,\mathbf j$ and $\mathbf r_0^Q = \ell(\sin\theta + \sin\phi)\,\mathbf i - \ell(\cos\theta + \cos\phi)\,\mathbf j$; $Q$ reaches the axis $Ox$ only if $\cos\theta + \cos\phi$ vanishes.")
def plane():
    sc = Scene(860, 700, (250, 150), 110)
    F1 = (0.0, P[1])
    F2 = (P[0], Q[1])
    triangle(sc, [O, F1, P], YELLOW, 0.28)
    triangle(sc, [P, F2, Q], YELLOW, 0.28)
    # axes: horizontal line dashed through O, y axis 1 unit up
    sc.line(O, (-1.5, 0.0), "EDGE", 1.3, "6 4")
    fixed_axis(sc, O, 0, 1.5, "x", off=(14, 5))
    fixed_axis(sc, O, 90, 1.0, "y", off=(0, -10))
    sc.label((-1.5, 0.0), "axis Ox: " + S("y", "Q") + " = 0 here", "TEXT", "start", 14, italic=False, dx=0, dy=-10)
    sc.line(O, (0.0, -2.9), "EDGE", 1.1, "5 4")
    sc.line(P, (P[0], Q[1] - 0.3), "EDGE", 1.1, "5 4")
    sc.line(F1, P, "EDGE", 1.1, "5 4")
    sc.line(F2, Q, "EDGE", 1.1, "5 4")
    right_angle(sc, F1, 90, 0, 0.1)
    right_angle(sc, F2, 90, 0, 0.1)
    # bars
    sc.line(O, P, "HEAD", 4.5)
    sc.line(P, Q, "HEAD", 4.5)
    sc.label((P[0] / 2, P[1] / 2), "l", "HEAD", "start", 17, dx=12, dy=-4)
    sc.label(((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2), "l", "HEAD", "start", 17, dx=12, dy=-6)
    # leg labels
    sc.label((0.0, P[1] / 2), "l cos θ", "TEXT", "end", 15, dx=-10, dy=5)
    sc.label((P[0] / 2, F1[1]), "l sin θ", "TEXT", "middle", 15, dy=22)
    sc.label((P[0], (P[1] + Q[1]) / 2), "l cos φ", "TEXT", "end", 15, dx=-10, dy=5)
    sc.label(((P[0] + Q[0]) / 2, Q[1]), "l sin φ", "TEXT", "middle", 15, dy=24)
    # angles
    sc.arc(O, 0.6, -90, -90 + TH, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.85, -90 + TH / 2), "θ", "GREEN", "middle", 16, dy=5)
    sc.arc(P, 0.94, -90, -90 + PH, "GREEN", 1.8, head=True)
    sc.label(_pol(P, 1.16, -90 + 38.0), "φ", "GREEN", "middle", 16, dy=5)
    # bases at P and Q
    e1, n1 = _dirs(TH)
    e2, n2 = _dirs(PH)
    for pt, ev, nv, col, ne, nn in ((P, e1, n1, "BLUE", I1, J1), (Q, e2, n2, "GREEN", I2, J2)):
        te = _add(pt, ev, 0.55 if col == "BLUE" else 0.6)
        tn = _add(pt, nv, 0.6)
        sc.vec(pt, te, None, col, 2.6, head=11)
        sc.vec(pt, tn, None, col, 2.6, head=11)
    sc.label(_pol(P, 0.70, -90 + 11.0), I1, "BLUE", "middle", 17, weight="700", dy=6)
    sc.label(_add(P, n1, 0.6), J1, "BLUE", "start", 17, weight="700", dx=8, dy=-4)
    sc.label(_add(Q, e2, 0.6), I2, "GREEN", "start", 17, weight="700", dx=8, dy=12)
    sc.label(_add(Q, n2, 0.6), J2, "GREEN", "start", 17, weight="700", dx=8, dy=-4)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "end", 17, dx=-12, dy=-8)
    sc.dotp(Q, 5.5)
    sc.label(Q, "Q", "HEAD", "middle", 17, dx=0, dy=-14)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=26)
    return sc


def _panel(sc, o, ang, col, nrot, name, title, ones=None):
    th = ang - 90.0
    basis_view(sc, o, th, (bold("i"), bold("j")), nrot, col=col, L=1.9, u=1.4, axl=2.2, ang=name, arcs=False,
               legs=("", "−cos " + name + " on " + bold("j"), "", ""), ls=14, one=-11, tri2=False, ones=ones)
    xl = 1.4 * math.cos(math.radians(th))
    sc.label((o[0] + xl, o[1]), "sin " + name, "TEXT", "start", 14, dx=10, dy=-8)
    # dashed -j and the two angle arcs
    sc.line(o, (o[0], o[1] - 2.2), "EDGE", 1.3, "5 4")
    sc.label((o[0], o[1] - 2.2), "−" + bold("j"), "TEXT", "middle", 15, dy=18)
    sc.arc(o, 0.9, -90, th, "GREEN", 1.8, head=True)
    sc.label(_pol(o, 1.15, -90 + (th + 90) / 2), name, "GREEN", "middle", 16, dy=5)
    sc.arc(o, 0.5, 0, th, "GREEN", 1.8, head=True)
    sc.label((o[0] + xl, o[1]), name + " − π/2", "GREEN", "start", 14, dx=10, dy=22)
    axis_out(sc, o, None)
    sc.label(o, bold("k"), "HEAD", "end", 17, dx=-14, dy=24)
    _spin(sc, o, 0.3, 20, 160, "positive about k", (-20, -40), "end", size=13)
    sc.note((o[0] - 2.0, o[1] + 2.7), title, "TEXT", "start", 14)


@figure("p50-rotations-k",
        "Two views along k of the bases of the bars, with the angles measured from the downward vertical and the polar angles theta - pi/2 and phi - pi/2.",
        r"Rotations about $\mathbf k$ (out of the paper). An angle from the downward vertical is the polar angle plus $\pi/2$; with $\cos(\theta - \pi/2) = \sin\theta$ and $\sin(\theta - \pi/2) = -\cos\theta$ the triangle gives $\mathbf i_1 = \sin\theta\,\mathbf i - \cos\theta\,\mathbf j$.")
def rotations_k():
    sc = Scene(1140, 640, (230, 280), 85)
    _panel(sc, (0.0, 0.0), TH, "BLUE", (I1, J1), "θ", "bar OP", ones=((0.1, -0.62),))
    _panel(sc, (6.4, 0.0), PH, "GREEN", (I2, J2), "φ", "bar PQ")
    return sc


@figure("p50-fbd",
        "Exploded free-body diagram of P and Q: weights and the forces of the bars along the bars, equal and opposite at the two ends of PQ.",
        r"Forces on $P$ and $Q$. Each massless bar acts along its own direction; the bar $PQ$ pulls $P$ and $Q$ with $\pm T_2\,\mathbf i_2$, so adding the two equations of motion removes $T_2$.")
def fbd():
    sc = Scene(860, 700, (250, 140), 110)
    e1, n1 = _dirs(TH)
    e2, n2 = _dirs(PH)
    sc.line(O, P, "EDGE", 1.8)
    sc.line(P, Q, "EDGE", 1.8)
    sc.dotp(O, 3.5, "EDGE")
    sc.label(O, "O", "TEXT", "end", 16, dx=-10, dy=-8)
    # P
    wt = arrow(sc, P, (0.0, -1.0), RED, 3.0, 12, 1.0)
    sc.label(_add(P, (0.0, -0.55)), "−m g " + bold("j"), RED, "end", 16, dx=-10, dy=5)
    t1 = arrow(sc, P, (-e1[0], -e1[1]), "PINK", 3.0, 12, 1.5)
    sc.label(_add(P, (-e1[0], -e1[1]), 0.75), "−" + S("T", "1") + " " + I1, "PINK", "end", 17, dx=-12, dy=5)
    t2 = arrow(sc, P, e2, "PINK", 3.0, 12, 0.65)
    sc.label(t2, S("T", "2") + " " + I2, "PINK", "start", 17, dx=8, dy=-12)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=-10)
    # Q
    arrow(sc, Q, (0.0, -1.0), RED, 3.0, 12, 1.0)
    sc.label(_add(Q, (0.0, -0.55)), "−m g " + bold("j"), RED, "start", 16, dx=10, dy=5)
    tq = arrow(sc, Q, (-e2[0], -e2[1]), "PINK", 3.0, 12, 0.65)
    sc.label(tq, "−" + S("T", "2") + " " + I2, "PINK", "end", 17, dx=-4, dy=26)
    sc.dotp(Q, 5.5)
    sc.label(Q, "Q", "HEAD", "start", 17, dx=12, dy=-8)
    sc.note((-2.0, -3.35), S("T", "1") + ", " + S("T", "2") + " positive when the bar pulls; a bar may also push;", "TEXT", "start", 13)
    sc.note((-2.0, -3.55), "inertial frame: no inertia forces", "TEXT", "start", 13)
    return sc
