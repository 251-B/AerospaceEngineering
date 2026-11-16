"""Problem 38: particle on a torus attracted by a particle on a plane (meridian half-plane, rotation about j0, free-body diagram)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import ORANGE, PURPLE, RED, YELLOW, arrow, away, basis_view
from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

I1 = S(bold("i"), "1")
J1 = S(bold("j"), "1")
K1 = S(bold("k"), "1")
J2 = S(bold("j"), "2")
K2 = S(bold("k"), "2")
I0 = S(bold("i"), "0")
J0 = S(bold("j"), "0")
K0 = S(bold("k"), "0")
PHI, THETA = 50.0, 35.0


@figure("p38-meridian",
        "Meridian half-plane of P: the tube section of radius 1 centred 2 from the axis, the right triangle of legs cos phi and sin phi, and the poloidal basis at P.",
        r"Meridian half-plane of $P$, $\mathbf i_1$ out of the paper. The triangle of $DP$ (hypotenuse 1, legs $\cos\phi$ along $\mathbf k_1$ and $\sin\phi$ along $\mathbf j_1$) gives $\mathbf r_0^P = 4\,\mathbf k_0 + (2 + \cos\phi)\,\mathbf k_1 + \sin\phi\,\mathbf j_1$; $\phi$ is clockwise here, a rotation by $-\phi$ about $\mathbf i_1$.")
def meridian():
    sc = Scene(860, 600, (235, 440), 95)
    C = (0.0, 0.0)
    D = (0.0, 2.0)
    c, s = math.cos(math.radians(PHI)), math.sin(math.radians(PHI))
    P = (D[0] + s, D[1] + c)
    E = (D[0], D[1] + c)
    F = (P[0], 0.0)
    triangle(sc, [D, E, P], YELLOW, 0.28)
    right_angle(sc, E, 270, 0, 0.12)
    # axis of the torus and tube section
    sc.line((-0.7, 0.0), (4.4, 0.0), "EDGE", 1.3, "11 3 2 3")
    sc.label((1.15, 0.0), "axis of the torus (parallel to " + J0 + ")", "TEXT", "start", 14, dy=-9)
    sc.circle(D, 1.0, "HEAD", 2.2, fill="EDGE", opacity=0.14)
    sc.line(C, D, "HEAD", 1.4)
    sc.label((0.0, 0.5), "2", "HEAD", "end", 16, dx=-10, dy=5)
    sc.line(D, P, "HEAD", 1.6)
    sc.label((D[0] + s / 2, D[1] + c / 2), "1", "HEAD", "middle", 16, dx=12, dy=14)
    sc.line(D, E, "EDGE", 1.1, "5 4")
    sc.line(E, P, "EDGE", 1.1, "5 4")
    sc.label((0.0, D[1] + c / 2), "cos φ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((0.3, E[1]), "sin φ", "TEXT", "middle", 15, dy=-8)
    # distance to the axis
    sc.line(P, F, "EDGE", 1.1, "5 4")
    right_angle(sc, F, 90, 180, 0.12)
    sc.label((F[0], 0.85), "ρ = 2 + cos φ", "TEXT", "start", 15, dx=10, dy=5)
    # angle at D (clockwise from the upward direction to DP)
    sc.arc(D, 0.4, 90, 90 - PHI, "GREEN", 1.8, head=True)
    sc.label(_pol(D, 0.58, 90 - PHI / 2 - 3), "φ", "GREEN", "middle", 16, dy=5)
    # grey basis at D
    sc.vec(D, (D[0] + 0.8, D[1]), None, "EDGE", 2.0, head=9)
    sc.label((D[0] + 0.4, D[1]), J1, "TEXT", "middle", 16, weight="700", dy=20)
    sc.vec(D, (D[0], D[1] + 0.8), None, "EDGE", 2.0, head=9)
    sc.label((D[0], D[1] + 0.8), K1, "TEXT", "end", 16, weight="700", dx=-12, dy=2)
    sc.dotp(D, 3.0)
    sc.label(D, "D", "HEAD", "end", 16, dx=-8, dy=18)
    # basis at P: grey copies and the orange poloidal basis
    sc.vec(P, (P[0], P[1] + 0.65), None, "EDGE", 1.5, head=8)
    sc.vec(P, (P[0] + 0.65, P[1]), None, "EDGE", 1.5, head=8)
    k2 = (s, c)
    j2 = (c, -s)
    tk = (P[0] + 0.8 * k2[0], P[1] + 0.8 * k2[1])
    tj = (P[0] + 0.8 * j2[0], P[1] + 0.8 * j2[1])
    sc.vec(P, tk, None, ORANGE, 2.8, head=11)
    sc.vec(P, tj, None, ORANGE, 2.8, head=11)
    sc.label(tk, K2, ORANGE, "start", 17, weight="700", dx=6, dy=-6)
    sc.label(tj, J2, ORANGE, "start", 17, weight="700", dx=8, dy=14)
    sc.arc(P, 0.42, 90, 90 - PHI, "GREEN", 1.8, head=True)
    sc.arc(P, 0.42, 0, -PHI, "GREEN", 1.8, head=True)
    sc.label(_pol(P, 0.62, 90 - PHI / 2 + 2), "φ", "GREEN", "middle", 16, dy=5)
    sc.label(_pol(P, 0.62, -PHI / 2), "φ", "GREEN", "middle", 16, dy=5)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "end", 17, dx=-6, dy=-12)
    # axis out of the paper at C
    axis_out(sc, C, None)
    sc.dotp(C, 1.0)
    sc.label(C, "C = (0, 0, 4)", "HEAD", "end", 16, dx=-14, dy=-10)
    sc.label(C, I1, "HEAD", "start", 17, weight="700", dx=16, dy=-8)
    _spin(sc, C, 0.3, -20, -160, "φ: positive about −" + I1, (-8, 54), "end", size=14)
    sc.note((-1.6, -0.95), I1 + " = " + J1 + " × " + K1 + ", out of the paper", "TEXT", "start", 13)
    sc.note((-1.6, -1.2), "O is out of this plane: OC = 4 " + K0, "TEXT", "start", 13)
    _matrix(sc, 3.0, 3.9, "[" + S("", "1") + "R" + S("", "2") + "] =", (("1", "0", "0"), ("0", "cos φ", "sin φ"), ("0", "−sin φ", "cos φ")), colw=0.78)
    return sc


@figure("p38-rotation-j",
        "Vertical plane x_0 z_0 with the centre circle of the torus around C, the toroidal basis turned by theta about j_0 and its two unit right triangles.",
        r"Rotation by $\theta$ about $\mathbf j_0$ (into the paper, so the rotation is clockwise as seen). The triangle of $\mathbf i_1$ has its opposite leg along $-\mathbf k_0$, which gives $\mathbf i_1 = \cos\theta\,\mathbf i_0 - \sin\theta\,\mathbf k_0$.")
def rotation_j():
    sc = Scene(820, 700, (210, 625), 80)
    O = (0.0, 0.0)
    C = (0.0, 4.0)
    fixed_axis(sc, O, 0, 3.0, "x" + '<tspan baseline-shift="sub" font-size="70%">0</tspan>', off=(16, 5))
    fixed_axis(sc, O, 90, 7.5, "z" + '<tspan baseline-shift="sub" font-size="70%">0</tspan>', off=(0, -10))
    sc.circle(C, 2.0, "HEAD", 1.6, "7 5")
    sc.label((0.15, 1.72), "centre circle, radius 2", "TEXT", "start", 14)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "end", 17, dx=-12, dy=-8)
    sc.dotp((0.0, 7.0), 4.0)
    sc.label((0.0, 7.0), "top, z = 7", "TEXT", "start", 14, dx=10, dy=5)
    # toroidal basis at C (tilted by theta clockwise = th -35), grey copies of i0, k0
    basis_view(sc, C, -THETA, (I0, ""), (I1, K1), col="BLUE", L=1.2, u=1.2, axl=1.3, ang="θ", ra=0.55, rl=0.8,
               legs=("cos θ", None, "cos θ", "sin θ"), ls=14, cf=0.5, one=15, one2=15, l1dx=26)
    sc.label((C[0] + 1.2 * math.cos(math.radians(THETA)), C[1] - 1.2 * math.sin(math.radians(THETA))), "−sin θ on " + K0, "TEXT", "middle", 14,
             dx=-8, dy=46)
    # projection of P on this plane
    d = 2.0 + math.cos(math.radians(PHI))
    k1 = (math.sin(math.radians(THETA)), math.cos(math.radians(THETA)))
    Pp = (C[0] + d * k1[0], C[1] + d * k1[1])
    sc.line((C[0] + 1.7 * k1[0], C[1] + 1.7 * k1[1]), Pp, "EDGE", 1.1, "5 4")
    sc.dotp(Pp, 5.0)
    sc.label(Pp, "projection of P (distance ρ from C)", "HEAD", "start", 14, dx=12, dy=5)
    axis_in(sc, O, None)
    sc.label(O, "O", "HEAD", "end", 16, dx=-14, dy=5)
    sc.label(O, J0, "HEAD", "middle", 17, weight="700", dy=30)
    sc.note((-0.6, -0.78), J0 + " = " + K0 + " × " + I0 + ", into the paper", "TEXT", "start", 13)
    _spin(sc, O, 0.3, 160, 20, "positive about " + J0, (14, -34), "start", size=14)
    _matrix(sc, 3.0, 3.3, _mname("0", "1"), (("cos θ", "0", "sin θ"), ("0", "1", "0"), ("−sin θ", "0", "cos θ")), colw=0.78)
    return sc


def _ax(x, y, z):
    """Oblique projection of the statement figure: x0 towards the viewer at the lower left, y0 to the right, z0 up."""
    return (y - 1.1 * x, 0.85 * z - 0.6 * x)


def _add2(q, d):
    return (q[0], q[1] - d)


def _circ(sc, c3, r, y, col="EDGE", w=1.2):
    """Circle of radius r in the plane x0 z0 at height of centre c3 = (0, 0, 4), displaced to y, in the projection."""
    pts = [_ax(r * math.cos(a * math.pi / 60), y, 4.0 + r * math.sin(a * math.pi / 60)) for a in range(121)]
    sc.poly(pts, col, w)


@figure("p38-fbd",
        "Free-body diagrams of P on the torus and Q on the plane: weights, mutual attraction and normal reactions, at the initial positions.",
        r"Forces on $P$ and $Q$ at the initial instant. Each reaction is along the single normal of its smooth surface ($\mathbf k_2$, here $\mathbf j_0$, for the torus; $\mathbf k_0$ for the plane), so projections on the tangent directions remove them.")
def fbd():
    sc = Scene(860, 640, (440, 410), 50)
    O = (0.0, 0.0)
    for r, y in ((3.0, 0.0), (1.0, 0.0), (2.0, 1.0), (2.0, -1.0)):
        _circ(sc, None, r, y, "EDGE", 1.2)
    sc.vec(O, _ax(3.9, 0, 0), None, "EDGE", 1.4, head=8)
    sc.label(_ax(3.9, 0, 0), S("x", "0"), "TEXT", "middle", 16, weight="700", dx=-14, dy=14)
    sc.vec(O, (4.2, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((4.2, 0.0), S("y", "0"), "TEXT", "middle", 16, weight="700", dx=16, dy=5)
    sc.vec(O, (0.0, 6.6), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 6.6), S("z", "0"), "TEXT", "middle", 16, weight="700", dy=-10)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "start", 16, dx=10, dy=18)
    Pq = _ax(2, 1, 4)
    Qq = _ax(3, 1, 0)
    sc.line(Pq, Qq, "EDGE", 1.1, "5 4")
    dq = (Qq[0] - Pq[0], Qq[1] - Pq[1])
    n = math.hypot(*dq)
    uq = (dq[0] / n, dq[1] / n)
    # forces on P
    wt = arrow(sc, Pq, (0.0, -1.0), RED, 3.0, 11, 1.0)
    sc.label(wt, "−" + S("m", "P") + " g " + K0, RED, "start", 16, dx=8, dy=-2)
    tp = arrow(sc, Pq, uq, "PINK", 3.0, 11, 1.2)
    sc.label(tp, "k PQ", "PINK", "end", 16, dx=-10, dy=20)
    tn = arrow(sc, Pq, (1.0, 0.0), PURPLE, 3.0, 10, 0.6)
    sc.label(tn, "N " + K2, PURPLE, "start", 16, dx=8, dy=5)
    vp = (Pq[0] - 0.9, Pq[1] - 0.05)
    sc.vec(vp, (vp[0], vp[1] - 0.8), None, "GREEN", 1.6, head=8)
    sc.label((vp[0], vp[1] - 0.8), "v: −" + K0, "GREEN", "end", 14, dx=-4, dy=6)
    sc.dotp(Pq, 5.5)
    sc.label(Pq, "P (2, 1, 4)", "HEAD", "end", 16, dx=-12, dy=-10)
    # forces on Q
    wq = arrow(sc, Qq, (0.0, -1.0), RED, 3.0, 11, 2.0)
    sc.label(_add2(Qq, 1.0), "−" + S("m", "Q") + " g " + K0, RED, "start", 16, dx=8, dy=5)
    tq = arrow(sc, Qq, (-uq[0], -uq[1]), "PINK", 3.0, 11, 1.2)
    sc.label(tq, "−k PQ", "PINK", "start", 16, dx=10, dy=-4)
    tz = arrow(sc, Qq, (0.0, 1.0), PURPLE, 3.0, 10, 0.7)
    sc.label(tz, S("N", "Q") + " " + K0, PURPLE, "end", 16, dx=-8, dy=-2)
    vq = (Qq[0], Qq[1] - 0.18)
    sc.vec(vq, (vq[0] + 0.9, vq[1] + 0.36), None, "GREEN", 1.6, head=8)
    sc.label((vq[0] + 0.9, vq[1] + 0.36), "v: −" + I0 + " + " + J0, "GREEN", "start", 14, dx=8, dy=4)
    sc.dotp(Qq, 5.5)
    sc.label(Qq, "Q (3, 1, 0)", "HEAD", "end", 16, dx=-12, dy=-8)
    sc.note((-4.2, -4.15), "inertial frame: no inertia forces; smooth torus and plane", "TEXT", "start", 13)
    return sc
