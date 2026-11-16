"""Problem 39: particle on a string over the smooth edge of a horizontal plate (axonometric view with inset, view along the edge, free-body diagram)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import ORANGE, PURPLE, RED, YELLOW, arrow, away, basis_view
from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

I0, J0, K0 = S(bold("i"), "0"), S(bold("j"), "0"), S(bold("k"), "0")
I1, K1 = S(bold("i"), "1"), S(bold("k"), "1")
EQP = S(bold("e"), "QP")
EPERP = S(bold("e"), "⊥")
TH, PH = 35.0, 25.0
D, L = 1.0, 3.0
CT, ST = math.cos(math.radians(TH)), math.sin(math.radians(TH))
CP, SP = math.cos(math.radians(PH)), math.sin(math.radians(PH))
U = L * CT - D
RHO = L - D / CT


def pr(x, y, z):
    """Oblique projection of the statement figure: x0 towards the viewer at the lower left, y0 to the right, z0 up."""
    return (y - 0.55 * x, z - 0.55 * x)


def prv(v):
    return pr(*v)


O3 = (0.0, 0.0, 0.0)
F3 = (D, 0.0, 0.0)
Q3 = (D, D * math.tan(math.radians(TH)), 0.0)
E3 = (D, L * ST, 0.0)
P3 = (D + U * SP, L * ST, -U * CP)
E23 = (D, L * ST, -U * CP)
O_, F_, Q_, E_, P_, E2_ = (pr(*p) for p in (O3, F3, Q3, E3, P3, E23))


def _plate(sc, faint=False):
    if faint:
        corners = [pr(1.0, -0.8, 0), pr(1.0, 2.6, 0), pr(-0.6, 2.6, 0), pr(-0.6, -0.8, 0)]
    else:
        corners = [pr(1.0, -1.5, 0), pr(1.0, 3.6, 0), pr(-1.5, 3.6, 0), pr(-1.5, -1.5, 0)]
    sc.poly(corners, "EDGE", 1.2, fill="EDGE", close=True, opacity=0.14 if not faint else 0.08)
    sc.line(corners[0], corners[1], "EDGE" if faint else "HEAD", 3.5 if not faint else 2.0)


@figure("p39-plate",
        "Plate with the string from O to Q on the edge and hanging to P, the equal angles at the edge, the right triangle of u cos phi and u sin phi below the edge, and an inset with the triangle of d and d tan theta.",
        r"The string runs from $O$ to $Q$ on the plate (legs $d$ and $d\tan\theta$, inset) and hangs from $Q$ to $P$. The smooth edge makes the two segments meet it at equal angles, so $\mathbf e_{QP}\cdot\mathbf j_0 = \sin\theta$, and $P$ lies at the distance $u = \ell\cos\theta - d$ from the edge, swung out by $\phi$.")
def plate():
    sc = Scene(880, 600, (240, 270), 100)
    _plate(sc)
    sc.label(pr(1.0, 3.0, 0), "edge " + S("x", "0") + " = d", "HEAD", "middle", 15, dy=22)
    # axes
    sc.vec(O_, pr(2.1, 0, 0), None, "EDGE", 1.4, head=8)
    sc.label(pr(2.1, 0, 0), S("x", "0"), "TEXT", "middle", 16, weight="700", dx=-14, dy=14)
    sc.vec(O_, pr(0, 3.9, 0), None, "EDGE", 1.4, head=8)
    sc.label(pr(0, 3.9, 0), S("y", "0"), "TEXT", "middle", 16, weight="700", dx=16, dy=5)
    sc.vec(O_, (0.0, 2.2), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 2.2), S("z", "0"), "TEXT", "middle", 16, weight="700", dy=-10)
    # strings and dashed lines
    sc.line(O_, F_, "EDGE", 1.1, "5 4")
    sc.label(((O_[0] + F_[0]) / 2, (O_[1] + F_[1]) / 2), "d", "TEXT", "end", 15, dx=-10, dy=-6)
    triangle(sc, [E_, E2_, P_], YELLOW, 0.30)
    sc.line(E_, (E_[0], E2_[1] - 0.2), "EDGE", 1.1, "5 4")
    sc.line(E_, P_, "EDGE", 1.1, "5 4")
    sc.line(E2_, P_, "EDGE", 1.1, "5 4")
    sc.line(O_, Q_, "HEAD", 4.0)
    sc.line(Q_, P_, "HEAD", 4.0)
    sc.label(((O_[0] + Q_[0]) / 2, (O_[1] + Q_[1]) / 2), "d / cos θ", "HEAD", "start", 15, dx=12, dy=5)
    sc.label((Q_[0] + 0.75 * (P_[0] - Q_[0]), Q_[1] + 0.75 * (P_[1] - Q_[1])), "ρ = l − d / cos θ", "HEAD", "end", 15, dx=-12, dy=5)
    sc.label((E_[0] + 0.5 * (P_[0] - E_[0]), E_[1] + 0.5 * (P_[1] - E_[1])), "u", "TEXT", "middle", 16, dx=-14, dy=6)
    sc.label((E_[0], (E_[1] + E2_[1]) / 2), "u cos φ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label(((E2_[0] + P_[0]) / 2, (E2_[1] + P_[1]) / 2), "u sin φ", "TEXT", "start", 15, dx=12, dy=22)
    # angle phi at E
    sc.arc(E_, 0.45, -90, -100, "GREEN", 1.8)
    sc.label((E_[0], E_[1] - 0.5), "φ", "GREEN", "start", 16, dx=8, dy=5)
    # equal angles at Q (dashed arcs) and e_QP
    sc.arc(Q_, 0.4, 180, 105, "GREEN", 1.6, "4 3")
    sc.arc(Q_, 0.4, 0, -68, "GREEN", 1.6, "4 3")
    sc.note((-2.3, -2.55), "equal angles: " + EQP + " · " + J0 + " = sin θ", "TEXT", "start", 13)
    ex, ey = P_[0] - Q_[0], P_[1] - Q_[1]
    n = math.hypot(ex, ey)
    tip = (Q_[0] + 0.6 * ex / n, Q_[1] + 0.6 * ey / n)
    sc.vec(Q_, tip, None, ORANGE, 2.8, head=11)
    sc.label(tip, EQP, ORANGE, "start", 17, weight="700", dx=8, dy=8)
    # points
    sc.dotp(O_, 4.0)
    sc.label(O_, "O", "HEAD", "end", 16, dx=-10, dy=-10)
    sc.dotp(F_, 3.5)
    sc.label(F_, "F", "HEAD", "start", 16, dx=6, dy=22)
    sc.dotp(Q_, 4.5)
    sc.label(Q_, "Q", "HEAD", "end", 17, dx=-10, dy=22)
    sc.dotp(E_, 3.5)
    sc.label(E_, "E", "HEAD", "start", 16, dx=8, dy=-8)
    sc.dotp(P_, 5.5)
    sc.label(P_, "P", "HEAD", "end", 17, dx=-12, dy=18)
    # inset: top view of the plate
    o = (2.55, -2.3)
    sc_ = 1.3
    fr = [(2.05, -2.85), (5.3, -2.85), (5.3, -0.95), (2.05, -0.95)]
    sc.poly(fr, "EDGE", 1.0, close=True)
    sc.note((2.15, -1.12), "top view of the plate", "TEXT", "start", 13)
    Fi = (o[0] + sc_ * D, o[1])
    Qi = (o[0] + sc_ * D, o[1] + sc_ * D * math.tan(math.radians(TH)))
    triangle(sc, [o, Fi, Qi], YELLOW, 0.30)
    sc.vec(o, (o[0] + 1.75, o[1]), None, "EDGE", 1.3, head=7)
    sc.label((o[0] + 1.75, o[1]), S("x", "0"), "TEXT", "start", 14, weight="700", dx=6, dy=5)
    sc.vec(o, (o[0], o[1] + 0.95), None, "EDGE", 1.3, head=7)
    sc.label((o[0], o[1] + 0.95), S("y", "0"), "TEXT", "middle", 14, weight="700", dy=-8)
    sc.line(o, Qi, "HEAD", 3.0)
    sc.line(Fi, Qi, "EDGE", 1.1, "5 4")
    right_angle(sc, Fi, 90, 180, 0.1)
    sc.arc(o, 0.45, 0, TH, "GREEN", 1.8, head=True)
    sc.label(_pol(o, 0.68, TH / 2 + 2), "θ", "GREEN", "middle", 15, dy=5)
    sc.label((o[0] + sc_ * D / 2, o[1]), "d", "TEXT", "middle", 15, dy=20)
    sc.label((Fi[0], (Fi[1] + Qi[1]) / 2), "d tan θ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label(((o[0] + Qi[0]) / 2, (o[1] + Qi[1]) / 2), "d / cos θ", "HEAD", "end", 15, dx=-8, dy=-8)
    axis_out(sc, o, None, r_px=7)
    sc.label(o, K0, "HEAD", "end", 15, weight="700", dx=-14, dy=-8)
    return sc


@figure("p39-rotation-j",
        "View along the edge of the basis of the hanging plane turned counterclockwise by phi, with the two unit right triangles and P below the edge.",
        r"View along the edge, $\mathbf j_0$ into the paper. $\phi$ is counterclockwise here, a rotation by $-\phi$ about $\mathbf j_0$; the triangle of $\mathbf k_1$ has its opposite leg along $-\mathbf i_0$, which gives $\mathbf k_1 = -\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf k_0$.")
def rotation_j():
    sc = Scene(860, 640, (360, 250), 80)
    E = (0.0, 0.0)
    sc.line(E, (-3.0, 0.0), "TEXT", 4.5)
    sc.label((-3.0, 0.0), "plate", "TEXT", "start", 14, italic=False, dy=22)
    basis_view(sc, E, PH, (I0, K0), (I1, K1), col="BLUE", L=1.8, u=1.3, axl=2.1, ang="φ", ra=0.6, rl=0.85,
               legs=("cos φ", "sin φ", "cos φ", ""), ls=14, cf=0.85, l1dx=10, l4=(22, "end", 13))
    # opposite leg of the triangle of k1, labelled to the left of k1 (clear of the arrow)
    sc.label((-1.3 * SP, 1.3 * CP), "−sin φ on " + I0, "TEXT", "end", 13, dx=-14, dy=16)
    # string below the edge, along -k1, and the downward vertical -k0 from which phi is measured
    P = (U * SP, -U * CP)
    sc.line(E, (0.0, -1.55), "EDGE", 1.2, "5 4")
    sc.label((0.0, -1.55), "−" + K0, "TEXT", "middle", 14, weight="700", dy=18)
    sc.line(E, P, "EDGE", 1.3, "6 4")
    sc.arc(E, 1.0, -90, -90 + PH, "GREEN", 1.8, head=True)
    sc.label(_pol(E, 1.25, -90 + PH / 2), "φ", "GREEN", "middle", 16, dy=5)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=14)
    sc.label(((E[0] + P[0]) / 2, (E[1] + P[1]) / 2), "u", "TEXT", "middle", 16, dx=16, dy=0)
    axis_in(sc, E, None)
    sc.label(E, J0, "HEAD", "end", 17, weight="700", dx=-14, dy=24)
    sc.note((-3.0, -2.1), J0 + " = " + K0 + " × " + I0 + ", into the paper", "TEXT", "start", 13)
    _spin(sc, E, 0.3, 20, 160, "φ: positive about −" + J0 + " (counterclockwise)", (-24, 78), "end", size=13)
    _matrix(sc, 3.3, -0.6, _mname("0", "1"), (("cos φ", "0", "−sin φ"), ("0", "1", "0"), ("sin φ", "0", "cos φ")), colw=0.78)
    return sc


def _v(vec, k=1.0):
    p = prv(vec)
    return (k * p[0], k * p[1])


@figure("p39-fbd",
        "Free-body diagram of P: weight and string tension towards Q, with the triad i_1, e_perp, e_QP and the components of the weight.",
        r"Forces on $P$. The tension acts only along $\mathbf e_{QP}$, so the projections of Newton's law on $\mathbf i_1$ and $\mathbf e_\perp$ give the two equations of motion free of $T$.")
def fbd():
    sc = Scene(860, 680, (260, 80), 150)
    _plate(sc, faint=True)
    sc.line(O_, Q_, "EDGE", 1.6)
    sc.line(Q_, P_, "EDGE", 1.6)
    sc.dotp(Q_, 3.0, "EDGE")
    sc.label(Q_, "Q", "TEXT", "end", 16, dx=-8, dy=18)
    i1 = (CP, 0.0, SP)
    eperp = (-ST * SP, CT, ST * CP)
    eqp = ((P3[0] - Q3[0]) / RHO, (P3[1] - Q3[1]) / RHO, (P3[2] - Q3[2]) / RHO)
    add = lambda p, v, k=1.0: (p[0] + k * v[0], p[1] + k * v[1])
    W = 1.2
    # weight and its components (dashed)
    wk = -W * SP
    we = -W * ST * CP
    wq = W * CT * CP
    ci = add(P_, _v(i1), wk)
    ce = add(P_, _v(eperp), we)
    cq = add(P_, _v(eqp), wq)
    for c in (ci, ce, cq):
        _dvec(sc, P_, c, RED, 1.8, 8)
    wt = arrow(sc, P_, (0.0, -1.0), RED, 3.0, 12, W)
    sc.label(wt, "−m g " + K0, RED, "middle", 16, dy=22)
    sc.label(ci, "−m g sin φ", RED, "start", 14, dx=8, dy=-6)
    sc.label(ce, "−m g sin θ cos φ", RED, "end", 14, dx=-8, dy=6)
    sc.label(cq, "m g cos θ cos φ", RED, "start", 14, dx=8, dy=14)
    # tension towards Q
    tt = add(P_, _v(eqp), -1.0)
    sc.vec(P_, tt, None, "PINK", 3.4, head=12)
    sc.label(tt, "−T " + EQP, "PINK", "end", 17, dx=-10, dy=-4)
    # triad
    nrm = lambda v: (prv(v)[0] / math.hypot(*prv(v)), prv(v)[1] / math.hypot(*prv(v)))
    ti = add(P_, nrm(i1), 0.5)
    te = add(P_, nrm(eperp), 0.5)
    tq = add(P_, nrm(eqp), 0.5)
    sc.vec(P_, ti, None, "BLUE", 2.4, head=10)
    sc.vec(P_, te, None, ORANGE, 2.4, head=10)
    sc.vec(P_, tq, None, ORANGE, 2.4, head=10)
    sc.label(ti, I1, "BLUE", "end", 17, weight="700", dx=-8, dy=-6)
    sc.label(te, EPERP, ORANGE, "start", 17, weight="700", dx=8, dy=-4)
    sc.label(tq, EQP, ORANGE, "start", 17, weight="700", dx=8, dy=4)
    sc.dotp(P_, 5.5)
    sc.label(P_, "P", "HEAD", "end", 17, dx=-22, dy=-14)
    sc.note((-1.3, -3.75), "inertial frame: no inertia forces; the edge acts on the string only", "TEXT", "start", 13)
    return sc
