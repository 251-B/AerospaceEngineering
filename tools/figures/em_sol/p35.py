"""Problem 35: string with two particles over a cylinder and a spring (plane of motion, rotations about k, free-body diagram, symmetric equilibrium)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import ORANGE, PURPLE, RED, YELLOW, arrow, away, basis_view
from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

R = 1.0
TH, PS = 30.0, 160.0
XI, ZE = 2.5, 2.0
GREEN2 = "#10b981"
EA = S(bold("e"), "A")
ETH = S(bold("e"), "θ")
EB = S(bold("e"), "B")
EPS = S(bold("e"), "ψ")


def _rim(a):
    return (R * math.cos(math.radians(a)), R * math.sin(math.radians(a)))


def _tan(a):
    return (-math.sin(math.radians(a)), math.cos(math.radians(a)))


A_ = _rim(TH)
B_ = _rim(PS)
etA = _tan(TH)
etB = _tan(PS)
P_ = (A_[0] - XI * etA[0], A_[1] - XI * etA[1])
Q_ = (B_[0] + ZE * etB[0], B_[1] + ZE * etB[1])


def _add(p, v, k=1.0):
    return (p[0] + k * v[0], p[1] + k * v[1])


def _spring(sc, a, b, col="EDGE", amp=5.0):
    sc.spring(a, b, coils=9, amp=amp, col=col, lead=0.08, w=1.4)


@figure("p35-plane",
        "Cylinder with the string wound from A to B over the top, the straight segments AP and BQ tangent at A and B with their right triangles, the spring PQ and the two polar bases.",
        r"Plane of the motion, $\mathbf k$ out of the paper. $AP$ leaves $A$ along $-\mathbf e_\theta$ at the angle $\theta$ from the downward vertical and $BQ$ leaves $B$ along $\mathbf e_\psi$ at the angle $\pi - \psi$; hence $\mathbf r_0^P = R\,\mathbf e_A - \xi\,\mathbf e_\theta$ and $\mathbf r_0^Q = R\,\mathbf e_B + \zeta\,\mathbf e_\psi$.")
def plane():
    sc = Scene(900, 620, (400, 250), 95)
    O = (0.0, 0.0)
    # drawing value of xi larger than in the other views: P lower than Q, so the spring clears the dashed legs
    P_ = (A_[0] - 3.0 * etA[0], A_[1] - 3.0 * etA[1])
    CA = (A_[0], P_[1])
    CB = (B_[0], Q_[1])
    triangle(sc, [A_, CA, P_], YELLOW, 0.26)
    triangle(sc, [B_, CB, Q_], YELLOW, 0.26)
    sc.circle(O, R, "HEAD", 2.2, fill="EDGE", opacity=0.20)
    fixed_axis(sc, O, 0, 2.2, "x", off=(14, 5))
    fixed_axis(sc, O, 90, 2.2, "y", off=(0, -10))
    sc.line(O, (-2.2, 0.0), "EDGE", 1.4)
    sc.line(O, (0.0, -2.2), "EDGE", 1.4)
    # wound string and radii
    sc.arc(O, R, TH, PS, "HEAD", 4.5)
    sc.line(_pol(O, 1.04, 116), _pol(O, 1.16, 119), "HEAD", 1.0)
    sc.label(_pol(O, 1.2, 120), "R (ψ − θ)", "HEAD", "end", 15, dx=-2, dy=0)
    sc.line(O, A_, "HEAD", 1.3)
    sc.line(O, B_, "HEAD", 1.3)
    sc.label((A_[0] / 2, A_[1] / 2), "R", "HEAD", "middle", 16, dx=-8, dy=-10)
    sc.label((B_[0] / 2, B_[1] / 2), "R", "HEAD", "middle", 16, dx=-6, dy=20)
    sc.arc(O, 0.3, 0, TH, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.46, TH / 2), "θ", "GREEN", "middle", 16, dy=5)
    sc.arc(O, 0.62, 0, PS, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.8, 115), "ψ", "GREEN", "middle", 16, dy=5)
    # free segments
    for P0, Cc, Pn in ((A_, CA, P_), (B_, CB, Q_)):
        sc.line(P0, Cc, "EDGE", 1.1, "5 4")
        sc.line(Cc, Pn, "EDGE", 1.1, "5 4")
    right_angle(sc, CA, 90, 0, 0.12)
    right_angle(sc, CB, 90, 180, 0.12)
    # spring: thin straight ends, zigzag only in the middle stretch between the two triangles
    m1 = _add(Q_, (P_[0] - Q_[0], P_[1] - Q_[1]), 0.24)
    m2 = _add(Q_, (P_[0] - Q_[0], P_[1] - Q_[1]), 0.56)
    sc.line(Q_, m1, "EDGE", 1.4)
    sc.line(m2, P_, "EDGE", 1.4)
    sc.spring(m1, m2, coils=6, amp=5.0, col="EDGE", lead=0.04, w=1.4)
    sc.line(A_, P_, "HEAD", 4.5)
    sc.line(B_, Q_, "HEAD", 4.5)
    right_angle(sc, A_, 180 + TH, 270 + TH, 0.14)
    right_angle(sc, B_, PS + 180, 250, 0.14)
    sc.arc(A_, 0.45, -90, -60, "GREEN", 1.8, head=True)
    sc.label(_pol(A_, 0.68, -75), "θ", "GREEN", "middle", 16, dy=5)
    sc.arc(B_, 1.15, -90, -110, "GREEN", 1.8, head=True)
    sc.label(_pol(B_, 1.15, -110), "π − ψ", "GREEN", "end", 15, dx=-8, dy=6)
    # labels of the legs and lengths
    sc.label((A_[0], (A_[1] + CA[1]) / 2 - 0.65), "ξ cos θ", "TEXT", "end", 15, dx=-10, dy=5)
    sc.label(((A_[0] + P_[0]) / 2, CA[1]), "ξ sin θ", "TEXT", "middle", 15, dy=26)
    sc.label(((A_[0] + P_[0]) / 2, (A_[1] + P_[1]) / 2), "ξ", "HEAD", "start", 17, dx=14, dy=-6)
    sc.label((B_[0], (B_[1] + CB[1]) / 2 - 0.65), "−ζ cos ψ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label(((B_[0] + Q_[0]) / 2, CB[1]), "ζ sin ψ", "TEXT", "middle", 15, dy=26)
    mq = _add(B_, (Q_[0] - B_[0], Q_[1] - B_[1]), 0.84)
    sc.label(mq, "ζ = L − ξ − R (ψ − θ)", "HEAD", "end", 16, dx=-16, dy=5)
    km = _add(Q_, (P_[0] - Q_[0], P_[1] - Q_[1]), 0.40)
    sc.label(km, "k", "TEXT", "middle", 17, dx=-22, dy=28)
    # bases at A and B
    for pt, vec_r, vec_t, col, nr, nt in ((A_, (math.cos(math.radians(TH)), math.sin(math.radians(TH))), etA, "BLUE", EA, ETH),
                                         (B_, (math.cos(math.radians(PS)), math.sin(math.radians(PS))), etB, "GREEN", EB, EPS)):
        tr = _add(pt, vec_r, 0.7)
        tt = _add(pt, vec_t, 0.7)
        sc.vec(pt, tr, None, col, 2.6, head=11)
        sc.vec(pt, tt, None, col, 2.6, head=11)
        sc.label(tr, nr, col, "middle", 17, weight="700", dx=16 * vec_r[0], dy=-16 * vec_r[1] + 5)
        sc.label(tt, nt, col, "middle", 17, weight="700", dx=16 * vec_t[0] - (6 if col == "BLUE" else 14), dy=-16 * vec_t[1] + 5 - (22 if col == "GREEN" else 0))
    sc.dotp(A_, 4.5)
    sc.label(A_, "A", "HEAD", "start", 17, dx=16, dy=22)
    sc.dotp(B_, 4.5)
    sc.label(B_, "B", "HEAD", "end", 17, dx=-16, dy=20)
    sc.dotp(P_, 5.5)
    sc.label(P_, "P", "HEAD", "start", 17, dx=14, dy=5)
    sc.dotp(Q_, 5.5)
    sc.label(Q_, "Q", "HEAD", "end", 17, dx=-12, dy=5)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=24)
    return sc


def _panel(sc, O, th, col, nfix, nrot, ang, legs, mat, title, lf, big=False):
    kw = dict(ra=0.85, ra2=0.5, rl=1.05, rl2=0.74, l1dx=-50, la=(30.0, 225.0),
              ones=((-0.95, 0.61), (-0.61, -0.95))) if big else dict(ra=0.65, rl=1.0, l1dx=8)
    basis_view(sc, O, th, nfix, nrot, col=col, L=1.8, u=1.3, axl=2.1, ang=ang, ls=14,
               legs=legs, cf=0.9, lf=lf, l4=(0, "middle", None), **kw)
    axis_out(sc, O, None)
    if big:
        sc.label(O, bold("k"), "HEAD", "start", 17, dx=14, dy=-6)
        _spin(sc, O, 0.28, 200, 340, "positive about k", (30, 52), "start", size=13)
    else:
        sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-8)
        _spin(sc, O, 0.28, 200, 340, "positive about k", (-20, 44), "end", size=13)
    _matrix(sc, O[0] - 0.2, O[1] - 2.4, mat[0], mat[1], colw=0.78, size=15)
    sc.note((O[0] - 1.9, O[1] + 2.6), title, "TEXT", "start", 14)


@figure("p35-rotations-k",
        "Two views along k of the polar bases at the tangency points, turned by theta and by psi from i, j.",
        r"Rotations about $\mathbf k$ (out of the paper) by $\theta$ (left) and by $\psi$ (right). In both, the triangle of the tangent vector has its opposite leg along $-\mathbf i$, which gives the minus sign of $-\sin\theta\,\mathbf i$ and $-\sin\psi\,\mathbf i$.")
def rotations_k():
    sc = Scene(1100, 620, (220, 270), 68)
    i_, j_ = bold("i"), bold("j")
    _panel(sc, (0.0, 0.0), TH, "BLUE", (i_, j_), (EA, ETH), "θ", ("cos θ", "sin θ", "cos θ", "sin θ"),
           (_mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1"))), "rotation θ", 0.5)
    _panel(sc, (7.6, 0.0), PS, "GREEN", (i_, j_), (EB, EPS), "ψ", ("cos ψ &lt; 0", "sin ψ", "cos ψ &lt; 0", "sin ψ"),
           (_mname("0", "2"), (("cos ψ", "−sin ψ", "0"), ("sin ψ", "cos ψ", "0"), ("0", "0", "1"))), "rotation ψ", 0.3, big=True)
    return sc


@figure("p35-fbd",
        "Exploded free-body diagram of P and Q: weights, the equal tensions towards the tangency points and the equal and opposite spring forces.",
        r"Forces on $P$ and $Q$. The string pulls each particle towards its tangency point with the same tension $T$; the spring of zero natural length pulls them towards each other with $\pm k\overrightarrow{PQ}$.")
def fbd():
    sc = Scene(900, 640, (400, 230), 95)
    O = (0.0, 0.0)
    sc.circle(O, R, "EDGE", 1.6, fill="EDGE", opacity=0.10)
    sc.arc(O, R, TH, PS, "EDGE", 3.0)
    sc.line(A_, P_, "EDGE", 1.6)
    sc.line(B_, Q_, "EDGE", 1.6)
    sc.dotp(A_, 3.5, "EDGE")
    sc.dotp(B_, 3.5, "EDGE")
    sc.label(A_, "A", "TEXT", "start", 16, dx=12, dy=-6)
    sc.label(B_, "B", "TEXT", "end", 16, dx=-12, dy=-6)
    pq = ((Q_[0] - P_[0]) / math.hypot(Q_[0] - P_[0], Q_[1] - P_[1]), (Q_[1] - P_[1]) / math.hypot(Q_[0] - P_[0], Q_[1] - P_[1]))
    # P
    wt = arrow(sc, P_, (0.0, -1.0), RED, 3.0, 12)
    sc.label(_add(P_, (0.0, -0.55)), "−m g " + bold("j"), RED, "start", 16, dx=10, dy=5)
    tp = arrow(sc, P_, etA, "PINK", 3.0, 12, 1.1)
    sc.label(tp, "T " + ETH, "PINK", "start", 17, dx=12, dy=-4)
    sp = arrow(sc, P_, pq, ORANGE, 3.0, 11, 0.8)
    sc.label(sp, "k PQ", ORANGE, "end", 16, dx=-8, dy=-10)
    sc.dotp(P_, 5.5)
    sc.label(P_, "P", "HEAD", "start", 17, dx=14, dy=22)
    # Q
    arrow(sc, Q_, (0.0, -1.0), RED, 3.0, 12)
    sc.label(_add(Q_, (0.0, -0.55)), "−m g " + bold("j"), RED, "end", 16, dx=-10, dy=5)
    tq = arrow(sc, Q_, (-etB[0], -etB[1]), "PINK", 3.0, 12, 1.1)
    sc.label(tq, "−T " + EPS, "PINK", "end", 17, dx=-10, dy=-6)
    sq = arrow(sc, Q_, (-pq[0], -pq[1]), ORANGE, 3.0, 11, 0.8)
    sc.label(sq, "−k PQ", ORANGE, "start", 16, dx=8, dy=-12)
    sc.dotp(Q_, 5.5)
    sc.label(Q_, "Q", "HEAD", "end", 17, dx=-14, dy=22)
    sc.note((-2.9, -3.35), "same tension T at both ends (massless string, smooth cylinder); the cylinder acts on the string only;", "TEXT", "start", 13)
    sc.note((-2.9, -3.55), "inertial frame: no inertia forces", "TEXT", "start", 13)
    return sc


@figure("p35-symmetric",
        "Symmetric equilibrium: the segments lean slightly inwards from tangency points just below the horizontal diameter, the spring is horizontal and its pull is balanced by the horizontal part of the tension.",
        r"Symmetric equilibrium of part (f), angle exaggerated. Because the spring pulls the particles together, the segments lean inwards and $\theta_0 \simeq -2kR/(mg + 2k\ell_0)$ is negative.")
def symmetric():
    sc = Scene(860, 640, (430, 190), 95)
    O = (0.0, 0.0)
    t0, p0, xi0 = -8.0, 188.0, 2.0
    A0 = _rim(t0)
    B0 = _rim(p0)
    e0 = _tan(t0)
    Pn = (A0[0] - xi0 * e0[0], A0[1] - xi0 * e0[1])
    Qn = (-Pn[0], Pn[1])
    sc.circle(O, R, "HEAD", 2.2, fill="EDGE", opacity=0.20)
    sc.line((0.0, 1.5), (0.0, -2.9), "EDGE", 1.3, "11 3 2 3")
    sc.label((0.0, 1.5), "mirror", "TEXT", "middle", 15, dy=-10)
    sc.arc(O, R, t0, p0, "HEAD", 4.5)
    sc.line(A0, (A0[0], Pn[1]), "EDGE", 1.1, "5 4")
    sc.line(A0, Pn, "HEAD", 4.5)
    sc.line(B0, Qn, "HEAD", 4.5)
    _spring(sc, Qn, Pn)
    sc.arc(A0, 1.0, -90, -90 + t0 * 0 - 8, "GREEN", 1.8, head=True)
    sc.label(_pol(A0, 1.0, -90), "θ" + '<tspan baseline-shift="sub" font-size="70%">0</tspan>' + " &lt; 0 (inwards)", "GREEN", "start", 15, dx=14, dy=12)
    # forces at P
    arrow(sc, Pn, (0.0, -1.0), RED, 3.0, 12)
    sc.label(_add(Pn, (0.0, -0.55)), "−m g " + bold("j"), RED, "start", 16, dx=10, dy=5)
    tp = arrow(sc, Pn, e0, "PINK", 3.0, 12, 1.05)
    sc.label(tp, "T " + ETH, "PINK", "end", 17, dx=-12, dy=10)
    hx = (Pn[0] + 1.05 * e0[0], Pn[1])
    sc.line(Pn, hx, "EDGE", 1.1, "4 3")
    sc.line(hx, tp, "EDGE", 1.1, "4 3")
    sp = arrow(sc, Pn, (-1.0, 0.0), ORANGE, 3.0, 11, 0.5)
    sc.label(sp, "k PQ", ORANGE, "end", 16, dx=-8, dy=-12)
    sc.dotp(Pn, 5.5)
    sc.label(Pn, "P", "HEAD", "end", 17, dx=-12, dy=26)
    sc.dotp(Qn, 5.5)
    sc.label(Qn, "Q", "HEAD", "end", 17, dx=-14, dy=22)
    sc.dotp(A0, 4.5)
    sc.label(A0, "A", "HEAD", "start", 17, dx=14, dy=-4)
    sc.dotp(B0, 4.5)
    sc.label(B0, "B", "HEAD", "end", 17, dx=-14, dy=-4)
    sc.note((-3.2, -3.5), "horizontal part of T balances the spring force k PQ; same picture mirrored at Q", "TEXT", "start", 13)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=24)
    return sc
