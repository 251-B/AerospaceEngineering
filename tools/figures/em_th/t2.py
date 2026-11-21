"""Theory figures of Topic 2, part A (Notes.pdf Chapter 4, Sections 4.1 to 4.7): momentum, Newton's laws, work and
potential energy, conservation of energy, equilibrium and the simple pendulum. Figures of part B are in t2b.py."""
import math

from figures.em_theory import axis_in, axis_out, figure, fixed_axis, right_angle, triangle  # noqa: F401
from figures.em_th.t1 import DRED, MINUS, ORANGE, _add, _matrix, dot1
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head, line as _line, rect as _rect

TEXT = {
    't2-momentum': (
        'A particle on a curved trajectory with its velocity and its linear momentum drawn along the same tangent line.',
        'The linear momentum $\\mathbf p_0$ has the direction and sense of the velocity $\\mathbf v_0^P$, tangent to the trajectory ([Lecture 2, Slide 3]).'),
    't2-action-reaction': (
        'Two particles P and Q joined by a dashed line, with equal and opposite forces F on P and minus F on Q along that line.',
        'Third law: action and reaction are equal, opposite and share the same line of action ([Lecture 2, Slide 6]).'),
    't2-momentum-conservation': (
        'An isolated system of two particles with equal and opposite internal forces and their momenta, whose vector sum is drawn as a constant total momentum.',
        'In an isolated system the internal forces cancel in pairs and the total linear momentum $\\mathbf p_0^P + \\mathbf p_0^Q$ stays constant ([Lecture 2, Slide 8]).'),
    't2-free-body': (
        'A particle isolated in a dashed circle with three forces drawn from it, and beside it the polygon of the three forces closing with their resultant.',
        'Free-body diagram of a particle: every force acting on $P$ is drawn, and their vector sum is the resultant $\\mathbf F$ of the second law.'),
    't2-projectile': (
        'Parabolic trajectory of a particle launched from the origin with initial velocity components 2 and 5 metres per second under its weight.',
        'Motion under gravity of [Lecture 2, Slide 11]: apex at $1.25\\ \\mathrm m$ after $0.5\\ \\mathrm s$, landing at $x = 2\\ \\mathrm m$ after $1\\ \\mathrm s$.'),
    't2-work-path': (
        'Two paths between the same two positions, with the force and the path element at a point of one of them and the projection of the force on the tangent.',
        "Work along a path: $\\delta W_0 = \\mathbf F\\cdot d\\mathbf r_0^P$ uses only the tangential component of the force, and in general the integral depends on the path ($\\Gamma$ or $\\Gamma'$) ([Lecture 2, Slide 14]; Notes.pdf Eq. 4.12)."),
    't2-potential-force': (
        'A wavy potential energy curve with horizontal arrows pointing downhill, longer where the curve is steeper.',
        'The example potential $V_0(x) = \\cos x + \\cos(x/2 - \\pi/4)$ and its force, which points downslope with a magnitude proportional to the slope (Notes.pdf Fig. 4.1; [Lecture 2, Slide 15]).'),
    't2-closed-circle': (
        'A circle around the origin with the azimuthal force tangent to it everywhere in the sense of travel, so the work around it never cancels.',
        'The azimuthal force $c_4 R^2\\,\\mathbf e_\\theta$ of [Lecture 2, Slide 18] points along the path all the way round the circle, so its work around $\\Gamma$ is $2\\pi c_4 R_0^3$, not zero: the force is not conservative.'),
    't2-energy-diagram': (
        'A potential energy curve crossed by three energy levels, with the forbidden regions and the turning points of the lowest level marked and the kinetic energy shown as the gap between level and curve.',
        'Allowed and forbidden regions for three levels of mechanical energy: the gap between the line $E_0$ and the curve is $T_0$, and the motion is confined where $V_0(x) \\leq E_0$ (Notes.pdf Fig. 4.2; [Lecture 2, Slide 20]).'),
    't2-stable-unstable': (
        'A ball at the bottom of a bowl pushed back towards the bottom when displaced, and a ball on top of a hill pushed further away when displaced.',
        'Stable equilibrium (a marble at the bottom of a bowl) and unstable equilibrium (a ball on the peak of a mountain): near the first the forces restore, near the second they repel ([Lecture 2, Slide 21]; Notes.pdf Sec. 4.6).'),
    't2-equilibria': (
        'A potential energy curve with its valley marked as a stable equilibrium and its peaks as unstable ones, and below it the force crossing zero at each of them.',
        'Equilibria are the critical points of $V_0$; at a minimum the force crosses zero with negative slope and restores, at a maximum with positive slope and repels ([Lecture 2, Slide 22]).'),
    't2-pendulum': (
        'A simple pendulum hanging from the origin, with the angle theta from the downward vertical, the right triangle of the rod and the standard polar angle from the x axis.',
        'Simple pendulum of length $\\ell$ and mass $m$: the angle $\\theta$ is measured from the downward vertical, so $x = \\ell\\sin\\theta$, $y = -\\ell\\cos\\theta$ and $\\theta_{\\mathrm{pol}} = \\theta - \\pi/2$ (Notes.pdf Fig. 4.3; [Lecture 2, Slide 23]).'),
    't2-pendulum-basis': (
        'The polar unit vectors of the pendulum at the bob, along and across the rod, with their projection triangles on the fixed axes and the change of basis matrix.',
        'Polar basis of the pendulum seen with $\\mathbf k$ out of the paper: $\\mathbf e_R$ makes the angle $\\theta$ with $-\\mathbf j$, which puts the minus sign in entry $(2,1)$ of $[{}_0R_{\\mathrm{pol}}]$.'),
    't2-pendulum-fbd': (
        'Free-body diagram of the pendulum bob with its weight split into components along and across the rod and the tension along the rod.',
        'Forces on the bob: weight $m g\\cos\\theta\\,\\mathbf e_R - m g\\sin\\theta\\,\\mathbf e_\\theta$ and tension $-F_t\\,\\mathbf e_R$, perpendicular to the velocity (Notes.pdf Eq. 4.36).'),
    't2-pendulum-potential': (
        'The potential energy of the pendulum against the angle, with its parabolic approximation, the maxima at twice m g l and two energy levels, one oscillating between plus and minus theta star and one above the maxima.',
        'Potential energy of the simple pendulum $V_0(\\theta) = m g\\ell(1 - \\cos\\theta)$ and, dashed, that of the linearised problem $\\tilde V_0(\\theta) = m g\\ell\\,\\theta^2/2$; $E_{0,1}$ gives an oscillation between $\\pm\\theta^*$, $E_{0,2}$ a rotation (Notes.pdf Fig. 4.4).'),
}


def _fig(name):
    alt, cap = TEXT[name]
    return figure(name, alt, cap)


def _vb(name, sub=None, sup=None):
    return bold(name) + S("", sub, sup)


def _dvec(sc, a, b, col, w=2.0, dash="6 4", head=9):
    """Arrow with a dashed shaft from world point a to world point b."""
    pa, pb = sc.P(a), sc.P(b)
    ang = math.atan2(pb[1] - pa[1], pb[0] - pa[0])
    tip = (pb[0] - head * 0.6 * math.cos(ang), pb[1] - head * 0.6 * math.sin(ang))
    _line(sc.c, pa, tip, col, w, dash)
    arrow_head(sc.c, pa, pb, col, head)


def _dbl(sc, a, b, col, w=1.8, head=9):
    """Double-headed arrow between two world points."""
    pa, pb = sc.P(a), sc.P(b)
    _line(sc.c, pa, pb, col, w)
    arrow_head(sc.c, pa, pb, col, head)
    arrow_head(sc.c, pb, pa, col, head)


def _unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy)
    return dx / n, dy / n


def _dir(deg):
    return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def _pt(p, deg, r):
    d = _dir(deg)
    return (p[0] + r * d[0], p[1] + r * d[1])


def _xy_axes(sc, o, lx, ly, nx="x", ny="y", offx=(14, 6), offy=(14, 4)):
    sc.vec(o, (o[0] + lx, o[1]), None, "EDGE", 1.4, head=8)
    sc.vec(o, (o[0], o[1] + ly), None, "EDGE", 1.4, head=8)
    sc.label((o[0] + lx, o[1]), nx, "TEXT", "middle", 16, weight="700", dx=offx[0], dy=offx[1])
    sc.label((o[0], o[1] + ly), ny, "TEXT", "middle", 16, weight="700", dx=offy[0], dy=offy[1])


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-momentum")
def momentum():
    sc = Scene(660, 430, (80, 370), 66)
    O = (0.0, 0.0)

    def traj(x):
        return (x, 1.2 + 1.4 * math.sin(0.45 * x))

    xp = 1.6
    P = traj(xp)
    slope = 1.4 * 0.45 * math.cos(0.45 * xp)
    u = _unit((0, 0), (1, slope))
    fixed_axis(sc, O, 0, 8.4, "x", off=(10, 6))
    fixed_axis(sc, O, 90, 4.8, "y", off=(14, 4))
    sc.curve(traj, 0.5, 8.0, 100, "HEAD", 1.6)
    sc.vec(O, P, None, "EDGE", 1.6, head=9)
    sc.label((P[0] / 2, P[1] / 2), _vb("r", "0", "P"), "TEXT", "middle", 17, dx=-24, dy=-4)
    # momentum (dashed shaft, longer) under the velocity (solid), same line
    tp = (P[0] + 2.3 * u[0], P[1] + 2.3 * u[1])
    tv = (P[0] + 1.45 * u[0], P[1] + 1.45 * u[1])
    _dvec(sc, P, tp, ORANGE, 2.6, "7 4", 11)
    sc.vec(P, tv, None, ORANGE, 3.4, head=12)
    sc.label(tv, _vb("v", "0", "P"), ORANGE, "end", 17, weight="700", dx=-6, dy=-18)
    sc.label(tp, _vb("p", "0") + " = m " + _vb("v", "0", "P"), ORANGE, "start", 17, dx=10, dy=-14)
    sc.dotp(P, 4.5, "HEAD")
    sc.label(P, "P, mass m", "HEAD", "start", 17, dx=12, dy=30)
    sc.dotp(O, 2.0, "HEAD")
    axis_out(sc, O, bold("k"), "HEAD", off=(-20, 24))
    sc.note((6.4, 2.15), "trajectory", "TEXT", "middle", 15)
    return sc


@_fig("t2-action-reaction")
def action_reaction():
    sc = Scene(700, 190, (350, 95), 76)
    Q, Pp = (-1.9, 0.0), (1.9, 0.0)
    sc.line((-4.1, 0), (4.1, 0), "EDGE", 1.3, "7 5")
    sc.vec(Pp, (Pp[0] + 1.9, 0), None, "PINK", 3.4, head=12)
    sc.vec(Q, (Q[0] - 1.9, 0), None, "PINK", 3.4, head=12)
    sc.label((Pp[0] + 0.95, 0), bold("F"), "PINK", "middle", 19, weight="700", dy=-26)
    sc.note((Pp[0] + 0.95, 0), "(force of Q on P)", "TEXT", "middle", 14, dy=-10)
    sc.label((Q[0] - 0.95, 0), MINUS + bold("F"), "PINK", "middle", 19, weight="700", dy=-26)
    sc.note((Q[0] - 0.95, 0), "(force of P on Q)", "TEXT", "middle", 14, dy=-10)
    sc.dotp(Pp, 5.0, "HEAD")
    sc.dotp(Q, 5.0, "HEAD")
    sc.label(Pp, "P", "HEAD", "middle", 19, dy=28)
    sc.label(Q, "Q", "HEAD", "middle", 19, dy=28)
    sc.note((0, 0), "common line of action", "TEXT", "middle", 14, dy=22)
    return sc


@_fig("t2-momentum-conservation")
def momentum_conservation():
    sc = Scene(860, 430, (0, 0), 1.0)
    k = 70.0
    sc.o, sc.k = (60, 320), k
    P, Q = (1.0, 2.3), (4.2, 1.5)
    pP, pQ = (-1.1, 0.9), (1.9, -0.55)
    # left panel: isolated system
    ang = math.degrees(math.atan2(Q[1] - P[1], Q[0] - P[0]))
    cen = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
    pts = []
    for i in range(121):
        t = 2 * math.pi * i / 120
        a, b = 2.9, 1.55
        x, y = a * math.cos(t), b * math.sin(t)
        ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pts.append((cen[0] + x * ca - y * sa, cen[1] + x * sa + y * ca))
    sc.poly(pts, "EDGE", 1.6, "7 5", close=True)
    f = _unit(P, Q)
    sc.vec(P, (P[0] + 1.25 * f[0], P[1] + 1.25 * f[1]), None, "PINK", 3.2, head=11)
    sc.vec(Q, (Q[0] - 1.25 * f[0], Q[1] - 1.25 * f[1]), None, "PINK", 3.2, head=11)
    sc.label((P[0] + 0.62 * f[0], P[1] + 0.62 * f[1]), bold("F"), "PINK", "middle", 18, weight="700", dx=6, dy=26)
    sc.label((Q[0] - 0.62 * f[0], Q[1] - 0.62 * f[1]), MINUS + bold("F"), "PINK", "middle", 18, weight="700", dx=-6, dy=-14)
    sc.vec(P, (P[0] + pP[0], P[1] + pP[1]), None, ORANGE, 3.2, head=11)
    sc.vec(Q, (Q[0] + pQ[0], Q[1] + pQ[1]), None, ORANGE, 3.2, head=11)
    sc.label((P[0] + pP[0], P[1] + pP[1]), _vb("p", "0", "P"), ORANGE, "end", 18, weight="700", dx=-8, dy=-6)
    sc.label((Q[0] + pQ[0], Q[1] + pQ[1]), _vb("p", "0", "Q"), ORANGE, "start", 18, weight="700", dx=8, dy=20)
    sc.dotp(P, 5.0, "HEAD")
    sc.dotp(Q, 5.0, "HEAD")
    sc.label(P, "P", "HEAD", "middle", 19, dx=-14, dy=24)
    sc.label(Q, "Q", "HEAD", "middle", 19, dx=14, dy=-14)
    sc.note((cen[0], cen[1] - 1.95), "isolated system", "TEXT", "middle", 14, dy=10)
    # right panel: vector sum, tail to tail
    C = (8.8, 1.3)
    sc.vec(C, (C[0] + pP[0], C[1] + pP[1]), None, ORANGE, 3.2, head=11)
    sc.vec(C, (C[0] + pQ[0], C[1] + pQ[1]), None, ORANGE, 3.2, head=11)
    s = (pP[0] + pQ[0], pP[1] + pQ[1])
    tP = (C[0] + pP[0], C[1] + pP[1])
    tQ = (C[0] + pQ[0], C[1] + pQ[1])
    tS = (C[0] + s[0], C[1] + s[1])
    sc.line(tP, tS, "EDGE", 1.2, "5 4")
    sc.line(tQ, tS, "EDGE", 1.2, "5 4")
    sc.vec(C, tS, None, "BLUE", 3.8, head=13)
    sc.label(tP, _vb("p", "0", "P"), ORANGE, "end", 18, weight="700", dx=-8, dy=-6)
    sc.label(tQ, _vb("p", "0", "Q"), ORANGE, "start", 18, weight="700", dx=8, dy=20)
    sc.label(tS, _vb("p", "0") + " constant", "BLUE", "start", 18, weight="700", dx=12, dy=-12, italic=False)
    sc.note((C[0] + 0.5, C[1] - 1.9), _vb("p", "0") + " = " + _vb("p", "0", "P") + " + " + _vb("p", "0", "Q"), "TEXT", "middle", 15)
    sc.dotp(C, 3.5, "HEAD")
    sc.note((C[0] + 0.5, C[1] - 2.4), "vector sum", "TEXT", "middle", 14)
    return sc


@_fig("t2-free-body")
def free_body():
    sc = Scene(860, 440, (60, 400), 74)
    O = (0.0, 0.0)
    s = 0.6
    F1, F2, F3 = (0.0, -3.0), (-1.5, 2.0), (3.0, -0.5)
    P = (3.0, 3.4)
    fixed_axis(sc, O, 0, 1.3, "x", off=(14, 6))
    fixed_axis(sc, O, 90, 1.3, "y", off=(14, 4))
    sc.vec(O, (1.0, 0), bold("i"), "HEAD", 3.0, name_off=(2, 20), size=17, head=11)
    sc.vec(O, (0, 1.0), bold("j"), "HEAD", 3.0, name_off=(-14, 4), size=17, head=11)
    axis_out(sc, O, bold("k"), "HEAD", off=(-22, 16))
    sc.circle(P, 0.42, "EDGE", 1.5, "6 4")
    sc.label(P, "free body", "TEXT", "end", 15, italic=False, dx=-26, dy=50)
    for F, nm, off in ((F1, "1", (16, 4)), (F2, "2", (-14, -4)), (F3, "3", (6, 24))):
        tip = (P[0] + s * F[0], P[1] + s * F[1])
        sc.vec(P, tip, None, "PINK", 3.4, head=12)
        sc.label(tip, _vb("F", nm), "PINK", "middle", 19, weight="700", dx=off[0], dy=off[1])
    vt = (P[0] + 1.5, P[1] + 0.85)
    _dvec(sc, P, vt, ORANGE, 1.6, "5 4", 9)
    sc.label(vt, _vb("v", "0", "P"), ORANGE, "start", 17, weight="700", dx=8, dy=-8)
    sc.note(vt, "(not a force)", "TEXT", "start", 13, dx=8, dy=12)
    sc.dotp(P, 4.5, "HEAD")
    sc.label(P, "P", "HEAD", "middle", 19, dx=-46, dy=8)
    # polygon
    s2 = 0.75
    A = (7.0, 3.9)
    a = A
    for F, nm, off, anc in ((F1, "1", (10, 4), "start"), (F2, "2", (-10, 4), "end"), (F3, "3", (0, 26), "middle")):
        b = (a[0] + s2 * F[0], a[1] + s2 * F[1])
        sc.vec(a, b, None, "PINK", 1.8, head=9)
        mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        if nm == "1":
            mid = (mid[0], mid[1] - 0.45)
        if nm == "3":
            mid = (mid[0] + 0.55, mid[1])
        sc.label(mid, _vb("F", nm), "PINK", anc, 18, weight="700", dx=off[0], dy=off[1])
        a = b
    sc.vec(A, a, None, "PINK", 4.2, head=14)
    sc.label(a, bold("F") + " = " + _vb("F", "1") + " + " + _vb("F", "2") + " + " + _vb("F", "3"), "PINK", "start", 18,
             weight="700", dx=14, dy=6)
    sc.dotp(A, 3.2, "PINK")
    sc.note((A[0], A[1] - 2.9), "vector polygon", "TEXT", "middle", 14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-projectile")
def projectile():
    sc = Scene(660, 470, (96, 420), 165)
    O = (0.0, 0.0)
    YS = 1.5                                    # vertical scale of the drawing (stretched for legibility)

    def Y(y):
        return YS * y

    def parab(x):
        return (x, Y(2.5 * x - 1.25 * x * x))

    fixed_axis(sc, O, 0, 2.5, "x (m)", off=(26, 6))
    fixed_axis(sc, O, 90, 2.35, "y (m)", off=(22, 4))
    for xt, nm in ((1.0, "1"), (2.0, "2")):
        sc.line((xt, 0.0), (xt, -0.045), "EDGE", 1.3)
        sc.label((xt, 0.0), nm, "TEXT", "middle", 15, italic=False, dy=26)
    sc.line((0.0, Y(1.25)), (-0.05, Y(1.25)), "EDGE", 1.3)
    sc.label((0.0, Y(1.25)), "1.25", "TEXT", "end", 15, italic=False, dx=-10, dy=5)
    sc.dashed((0.0, Y(1.25)), (1.0, Y(1.25)))
    sc.dashed((1.0, Y(1.25)), (1.0, 0.0))
    sc.curve(parab, 0.0, 2.0, 120, DRED, 2.2, "7 5")
    # launch velocity with its components
    vx, vy = 0.5, Y(1.25)                       # (2, 5) m/s drawn at 0.25 m per m/s
    triangle(sc, [O, (vx, 0.0), (vx, vy)], ORANGE, 0.16)
    _dvec(sc, O, (vx, 0.0), ORANGE, 1.8, "5 4", 9)
    _dvec(sc, (vx, 0.0), (vx, vy), ORANGE, 1.8, "5 4", 9)
    sc.vec(O, (vx, vy), None, ORANGE, 3.6, head=12)
    sc.label((vx, vy), _vb("v", "0", "P") + "(0)", ORANGE, "end", 17, weight="700", dx=-10, dy=-18)
    sc.label((vx / 2, 0.0), S("v", "x") + " = 2 m/s", ORANGE, "middle", 16, italic=False, dy=30)
    sc.label((vx, vy * 0.35), S("v", "y") + " = 5 m/s", ORANGE, "start", 16, italic=False, dx=10, dy=5)
    # apex, landing, weight
    ap = (1.0, Y(1.25))
    sc.dotp(ap, 4.5, "HEAD")
    sc.label(ap, "apex, t = 0.5 s", "HEAD", "middle", 16, italic=False, dy=-16)
    sc.dotp((2.0, 0.0), 4.5, "HEAD")
    sc.label((2.0, 0.0), "t = 1 s", "HEAD", "start", 16, italic=False, dx=14, dy=-10)
    w0 = parab(1.5)
    sc.vec(w0, (w0[0], w0[1] - 0.85), None, "PINK", 3.4, head=12)
    sc.dotp(w0, 4.0, "HEAD")
    sc.label((w0[0], w0[1] - 0.85), MINUS + "m g " + bold("j"), "PINK", "end", 17, weight="700", italic=False, dx=-10, dy=4)
    sc.dotp(O, 2.0, "HEAD")
    axis_out(sc, O, bold("k"), "HEAD", off=(-20, 24))
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1])


def _bez_d(p0, p1, p2, p3, t):
    u = 1 - t
    return (3 * u * u * (p1[0] - p0[0]) + 6 * u * t * (p2[0] - p1[0]) + 3 * t * t * (p3[0] - p2[0]),
            3 * u * u * (p1[1] - p0[1]) + 6 * u * t * (p2[1] - p1[1]) + 3 * t * t * (p3[1] - p2[1]))


@_fig("t2-work-path")
def work_path():
    sc = Scene(800, 470, (90, 425), 72)
    O = (0.0, 0.0)
    r1, r2 = (2.2, 1.3), (8.4, 4.0)
    G = (r1, (3.4, 3.9), (6.2, 1.9), r2)
    G2 = (r1, (4.2, 0.1), (6.0, 4.9), r2)
    fixed_axis(sc, O, 0, 9.3, "x", off=(10, 6))
    fixed_axis(sc, O, 90, 5.4, "y", off=(14, 4))
    sc.poly([_bez(*G2, i / 100) for i in range(101)], DRED, 2.0, "8 5")
    sc.poly([_bez(*G, i / 100) for i in range(101)], DRED, 2.8)
    sc.vec(O, r1, None, "EDGE", 1.5, head=9)
    sc.vec(O, r2, None, "EDGE", 1.5, head=9)
    sc.dotp(r1, 4.5, "HEAD")
    sc.dotp(r2, 4.5, "HEAD")
    sc.label(r1, _vb("r", "0,1", "P"), "HEAD", "end", 17, dx=-10, dy=-4)
    sc.label(r2, _vb("r", "0,2", "P"), "HEAD", "start", 17, dx=10, dy=-4)
    sc.label((3.7, 0.45), "Γ'", DRED, "middle", 19, weight="700")
    # point P on Gamma
    t = 0.40
    Pp = _bez(*G, t)
    d = _bez_d(*G, t)
    n = math.hypot(*d)
    u = (d[0] / n, d[1] / n)
    ang = math.degrees(math.atan2(u[1], u[0]))
    sc.label(_bez(*G, 0.8), "Γ", DRED, "middle", 19, weight="700", dx=6, dy=-20)
    # unit tangent (thin), path element (thick), force at ang + 40
    et = _add(Pp, u, 1.35)
    dr = _add(Pp, u, 0.85)
    sc.vec(Pp, et, None, ORANGE, 1.6, head=9)
    sc.vec(Pp, dr, None, ORANGE, 3.8, head=12)
    sc.label(et, _vb("e", "t"), ORANGE, "start", 17, weight="700", dx=2, dy=20)
    af = 40.0
    Fm = 2.5
    Ft = _add(Pp, _dir(ang + af), Fm)
    sc.vec(Pp, Ft, None, "PINK", 3.8, head=13)
    sc.label(Ft, bold("F"), "PINK", "middle", 20, weight="700", dx=-4, dy=-14)
    sc.arc(Pp, 0.95, ang, ang + af, "GREEN", 1.7, head=True)
    sc.label(_add(Pp, _dir(ang + af / 2), 1.45), S("α", "F"), "GREEN", "middle", 17, dx=0, dy=6)
    # projection of F on the tangent: drop line and a shifted copy of the component
    comp = Fm * math.cos(math.radians(af))
    foot = _add(Pp, u, comp)
    sc.line(Ft, foot, "PINK", 1.4, "5 4")
    right_angle(sc, foot, ang + 180, ang + 90, 0.12, "PINK")
    nrm = (u[1], -u[0])                                   # to the right of the direction of travel (away from F)
    off = 0.6
    a0 = _add(Pp, nrm, off)
    a1 = _add(foot, nrm, off)
    sc.line(Pp, a0, "PINK", 1.0, "3 3")
    sc.line(foot, a1, "PINK", 1.0, "3 3")
    _dvec(sc, a0, a1, "PINK", 2.0, "6 4", 9)
    sc.label(_add(a0, u, comp * 0.55), bold("F") + "·" + _vb("e", "t"), "PINK", "middle", 17, weight="700", dx=26, dy=34)
    sc.label(Pp, "d" + _vb("r", "0", "P") + " = " + _vb("v", "0", "P") + " dt", ORANGE, "end", 16,
             weight="700", dx=-34, dy=-36)
    sc.dotp(Pp, 4.5, "HEAD")
    sc.label(Pp, "P", "HEAD", "middle", 18, dx=-16, dy=-12)
    sc.dotp(O, 2.0, "HEAD")
    axis_out(sc, O, bold("k"), "HEAD", off=(-20, 24))
    return sc


# --------------------------------------------------------------------------------------------------------------------
YS = 1.27                                       # vertical stretch of the V0(x) graphs (pixels per unit of V0 over pixels per unit of x)


def _V(x):
    return math.cos(x) + math.cos(x / 2 - math.pi / 4)


def _F(x):
    return math.sin(x) + 0.5 * math.sin(x / 2 - math.pi / 4)


def _root(a, b):
    fa = _F(a)
    for _ in range(60):
        m = (a + b) / 2
        if (_F(m) > 0) == (fa > 0):
            a = m
        else:
            b = m
    return (a + b) / 2


XPEAK1, XVALLEY, XPEAK2 = _root(0.0, 1.0), _root(3.0, 4.0), _root(5.0, 6.5)


def _vgraph(sc, o, x0=-1.0, x1=8.0, xa=(-1.3, 8.4), ya=(-1.35, 2.15), names=("x", "V")):
    """Axes of a V0(x) graph through the origin of the scene and the curve; V0 is drawn stretched by YS."""
    sc.vec((xa[0], 0.0), (xa[1], 0.0), None, "EDGE", 1.4, head=8)
    sc.vec((0.0, ya[0] * YS), (0.0, ya[1] * YS), None, "EDGE", 1.4, head=8)
    sc.label((xa[1], 0.0), names[0], "TEXT", "middle", 16, weight="700", dx=2, dy=24)
    sc.label((0.0, ya[1] * YS), names[1], "TEXT", "start", 16, weight="700", dx=12, dy=4)
    sc.poly([(x0 + (x1 - x0) * i / 240, _V(x0 + (x1 - x0) * i / 240) * YS) for i in range(241)], "HEAD", 2.4)


@_fig("t2-potential-force")
def potential_force():
    sc = Scene(790, 400, (110, 250), 74)
    V0 = "V" + S("", "0")
    _vgraph(sc, None, names=("x", V0 + "(x)"))
    sc.line((2.0, 0.0), (2.0, -0.05), "EDGE", 1.3)
    sc.label((2.0, 0.0), "2", "TEXT", "middle", 15, italic=False, dy=19)
    sc.line((0.0, 0.5 * YS), (-0.05, 0.5 * YS), "EDGE", 1.3)
    sc.label((0.0, 0.5 * YS), "0.5", "TEXT", "end", 15, italic=False, dx=-9, dy=5)
    sc.label((0.0, 0.0), "0, 0", "TEXT", "end", 15, italic=False, dx=-8, dy=18)
    L = 0.55
    for x in (-0.6, XPEAK1, 1.25, 2.3, XVALLEY, 4.6, XPEAK2, 7.0):
        p = (x, _V(x) * YS)
        f = _F(x)
        if abs(f) < 1e-3:
            sc.dotp(p, 4.5, "PINK")
            continue
        sc.vec(p, (x + L * f, p[1]), None, "PINK", 3.0, head=11)
        sc.dotp(p, 3.0, "HEAD")
    p = (2.3, _V(2.3) * YS)
    sc.label((2.3 + L * _F(2.3) / 2, p[1]), S("F", "x"), "PINK", "middle", 18, weight="700", dy=-12)
    return sc


@_fig("t2-closed-circle")
def closed_circle():
    sc = Scene(700, 590, (330, 315), 78)
    O = (0.0, 0.0)
    R = 3.0
    fixed_axis(sc, O, 0, 4.3, "x", off=(10, 6))
    fixed_axis(sc, O, 90, 3.5, "y", off=(14, 4))
    sc.circle(O, R, DRED, 2.6)
    for a in (148.0, 325.0):                                   # arrowheads: counterclockwise sense of Γ
        q = _pt(O, a, R)
        tdir = (-math.sin(math.radians(a)), math.cos(math.radians(a)))
        sc.vec((q[0] - 0.12 * tdir[0], q[1] - 0.12 * tdir[1]), (q[0] + 0.12 * tdir[0], q[1] + 0.12 * tdir[1]), None, DRED, 2.6, head=13)
    sc.label(_pt(O, 236, R), "Γ", DRED, "middle", 20, weight="700", dx=-20, dy=14)
    # the field at R0 (four points) and at R0/2
    for a in (100.0, 190.0, 280.0, 345.0):
        q = _pt(O, a, R)
        tdir = (-math.sin(math.radians(a)), math.cos(math.radians(a)))
        sc.vec(q, (q[0] + 1.2 * tdir[0], q[1] + 1.2 * tdir[1]), None, "PINK", 3.4, head=12)
        sc.dotp(q, 3.0, DRED)
    q = _pt(O, 190.0, R)
    fl = S("c", "4") + S("R", "0") + '<tspan baseline-shift="super" font-size="70%">2</tspan> ' + _vb("e", "θ")
    sc.label((-2.5, -1.45), fl, "PINK", "start", 17, weight="700", dx=8, dy=4)
    for a in (120.0, 210.0, 300.0):
        q = _pt(O, a, R / 2)
        tdir = (-math.sin(math.radians(a)), math.cos(math.radians(a)))
        sc.vec(q, (q[0] + 0.3 * tdir[0], q[1] + 0.3 * tdir[1]), None, "PINK", 1.8, head=8)
    sc.note((0.0, -2.35), "at " + S("R", "0") + "/2: a quarter of the length", "TEXT", "middle", 14)
    # the local basis, the angle and the path element at P (30 degrees)
    TH = 30.0
    P = _pt(O, TH, R)
    sc.line(O, P, "EDGE", 1.5)
    sc.label((0.5 * P[0], 0.5 * P[1]), S("R", "0"), "TEXT", "middle", 17, dx=-4, dy=-12)
    tdir = (-math.sin(math.radians(TH)), math.cos(math.radians(TH)))
    sc.vec(P, _pt(P, TH, 1.0), None, "BLUE", 3.0, head=11)
    sc.vec(P, (P[0] + 1.0 * tdir[0], P[1] + 1.0 * tdir[1]), None, "BLUE", 3.0, head=11)
    sc.label(_pt(P, TH, 1.0), _vb("e", "R"), "BLUE", "start", 18, weight="700", dx=8, dy=0)
    sc.label((P[0] + tdir[0], P[1] + tdir[1]), _vb("e", "θ"), "BLUE", "start", 18, weight="700", dx=8, dy=-6)
    sc.dotp(P, 4.5, "HEAD")
    sc.label(P, "P", "HEAD", "middle", 18, dx=20, dy=22)
    sc.arc(O, 1.0, 0, TH, "GREEN", 1.7, head=True)
    sc.label(_pt(O, TH / 2 - 3, 1.4), "θ", "GREEN", "middle", 18, dy=8)
    # path element R0 dθ eθ on the circle, a little further on
    a0, a1 = 58.0, 72.0
    pts = [_pt(O, a0 + (a1 - a0) * i / 10, R) for i in range(11)]
    sc.poly(pts, ORANGE, 4.2)
    arrow_head(sc.c, sc.P(pts[-3]), sc.P(pts[-1]), ORANGE, 11)
    sc.label(_pt(O, 61, R + 0.55), S("R", "0") + " dθ " + _vb("e", "θ"), ORANGE, "start", 17, weight="700", dx=6, dy=-2)
    sc.dotp(O, 2.0, "HEAD")
    axis_out(sc, O, bold("k"), "HEAD", off=(-18, 24))
    return sc


def _ex_roots(level, x0=-1.0, x1=8.0, n=4000):
    """x where V0(x) = level, scanning [x0, x1]."""
    out = []
    prev = _V(x0) - level
    for i in range(1, n + 1):
        x = x0 + (x1 - x0) * i / n
        cur = _V(x) - level
        if prev == 0 or prev * cur < 0:
            a, b = x - (x1 - x0) / n, x
            for _ in range(50):
                m = (a + b) / 2
                if (_V(m) - level) * (_V(a) - level) > 0:
                    a = m
                else:
                    b = m
            out.append((a + b) / 2)
        prev = cur
    return out


@_fig("t2-energy-diagram")
def energy_diagram():
    sc = Scene(830, 440, (110, 290), 74)
    V0 = "V" + S("", "0")
    vmin, vmax = _V(XVALLEY), _V(XPEAK1)
    E = [vmin + f * (vmax - vmin) for f in (0.30, 0.70, 1.10)]
    ytop, ybot = E[2] * YS + 0.12, -1.3 * YS
    # forbidden intervals of the lowest level: V0 > E_{0,1}
    r = [-1.0] + _ex_roots(E[0]) + [8.0]
    for i in range(len(r) - 1):
        m = (r[i] + r[i + 1]) / 2
        if _V(m) > E[0]:
            sc.poly([(r[i], ybot), (r[i + 1], ybot), (r[i + 1], ytop), (r[i], ytop)], "HEAD", 0.0, fill="EDGE", close=True,
                    opacity=0.16)
    _vgraph(sc, None, names=("x", V0 + "(x)"), ya=(-1.3, 2.5))
    sc.line((1.0, 0.0), (1.0, -0.05), "EDGE", 1.3)
    sc.label((1.0, 0.0), "1", "TEXT", "middle", 15, italic=False, dy=19)
    sc.line((0.0, 0.5 * YS), (-0.05, 0.5 * YS), "EDGE", 1.3)
    sc.label((0.0, 0.5 * YS), "0.5", "TEXT", "end", 15, italic=False, dx=-9, dy=5)
    sc.label((0.0, 0.0), "0, 0", "TEXT", "end", 15, italic=False, dx=-8, dy=18)
    for i, e in enumerate(E):
        sc.line((-1.1, e * YS), (8.3, e * YS), "BLUE", 1.8, "8 5")
        sc.label((8.3, e * YS), S("E", f"0,{i + 1}"), "BLUE", "start", 18, weight="700", dx=6, dy=5)
    for x in _ex_roots(E[0]):
        sc.dotp((x, E[0] * YS), 4.8, "GREEN")
    xt = _ex_roots(E[0])[0]
    sc.label((xt, E[0] * YS), "turning point", "GREEN", "end", 15, italic=False, dx=-16, dy=-12)
    for a, b in ((r[0], r[1]), (r[2], r[3])):
        if _V((a + b) / 2) > E[0]:
            sc.note(((a + b) / 2, ybot), "forbidden", "TEXT", "middle", 14, dy=-8)
    xv = XVALLEY
    _dbl(sc, (xv, _V(xv) * YS + 0.05), (xv, E[0] * YS - 0.05), DRED, 2.0, 9)
    sc.label((xv, (_V(xv) + E[0]) / 2 * YS), S("T", "0"), DRED, "start", 18, weight="700", dx=10, dy=5)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-stable-unstable")
def stable_unstable():
    sc = Scene(780, 400, (390, 300), 84)
    c = 0.55
    H = 1.8

    def bowl(cx):
        return [(cx + x, c * x * x) for x in [-1.8 + 3.6 * i / 80 for i in range(81)]]

    def hill(cx):
        return [(cx + x, H - c * x * x) for x in [-1.8 + 3.6 * i / 80 for i in range(81)]]

    cl, cr = -2.6, 2.6
    r = 0.17
    sc.poly(bowl(cl), "HEAD", 2.8)
    sc.poly(hill(cr), "HEAD", 2.8)
    # stable: ball at the bottom (red), displaced hollow ball on the right wall with two restoring arrows
    sc.circle((cl, r), r, "HEAD", 1.6, fill=DRED, opacity=1.0)
    x = 1.0
    pw = (cl + x, c * x * x)
    t = _unit((0, 0), (1.0, 2 * c * x))
    nrm = (-t[1], t[0])
    bc = (pw[0] + nrm[0] * r, pw[1] + nrm[1] * r)
    sc.circle(bc, r, "HEAD", 1.6, "4 3")
    for off in (0.0, 0.2):
        a = (bc[0] - t[0] * (r + 0.1) + nrm[0] * (off - 0.04), bc[1] - t[1] * (r + 0.1) + nrm[1] * (off - 0.04))
        b = (a[0] - t[0] * 0.5, a[1] - t[1] * 0.5)
        sc.vec(a, b, None, "PINK", 3.0, head=11)
    # oscillation: green double-headed arc above the bottom
    pts = [(cl + xx, c * xx * xx + 0.62) for xx in [-0.62 + 1.24 * i / 30 for i in range(31)]]
    sc.poly(pts, "GREEN", 1.8)
    arrow_head(sc.c, sc.P(pts[3]), sc.P(pts[0]), "GREEN", 9)
    arrow_head(sc.c, sc.P(pts[-4]), sc.P(pts[-1]), "GREEN", 9)
    # unstable: ball on top, displaced hollow balls with arrows away from the top
    sc.circle((cr, H + r), r, "HEAD", 1.6, fill=DRED, opacity=1.0)
    for sgn in (-1, 1):
        x = 0.8 * sgn
        pw = (cr + x, H - c * x * x)
        t = _unit((0, 0), (1.0, -2 * c * x))
        if sgn < 0:
            t = (-t[0], -t[1])                       # downhill direction on the left wall
        nrm = (-t[1], t[0]) if sgn > 0 else (t[1], -t[0])
        if nrm[1] < 0:
            nrm = (-nrm[0], -nrm[1])
        bc = (pw[0] + nrm[0] * r, pw[1] + nrm[1] * r)
        sc.circle(bc, r, "HEAD", 1.6, "4 3")
        a = (bc[0] + t[0] * (r + 0.1) + nrm[0] * 0.12, bc[1] + t[1] * (r + 0.1) + nrm[1] * 0.12)
        b = (a[0] + t[0] * 0.55, a[1] + t[1] * 0.55)
        sc.vec(a, b, None, "PINK", 3.0, head=11)
    sc.label((cl, 2.25), "stable", "HEAD", "middle", 20, italic=False, weight="700")
    sc.label((cr, 2.55), "unstable", "HEAD", "middle", 20, italic=False, weight="700")
    sc.vec((0.0, 1.9), (0.0, 1.1), None, "TEXT", 1.8, head=9)
    sc.label((0.0, 1.5), "g", "TEXT", "start", 17, dx=10, dy=5)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _sup(t):
    return f'<tspan baseline-shift="super" font-size="70%">{t}</tspan>'


@_fig("t2-equilibria")
def equilibria():
    sc = Scene(800, 600, (110, 245), 74)
    V0 = "V" + S("", "0")
    d1 = "d" + V0 + "/dx"
    d2 = "d" + _sup("2") + V0 + "/dx" + _sup("2")
    _vgraph(sc, None, names=("x", V0 + "(x)"), ya=(-1.3, 2.15))
    crit = ((XPEAK1, False), (XVALLEY, True), (XPEAK2, False))
    for xc, stable in crit:
        p = (xc, _V(xc) * YS)
        sc.line((p[0] - 0.55, p[1]), (p[0] + 0.55, p[1]), "GREEN", 1.8)
        if stable:
            sc.dotp(p, 5.5, "GREEN")
        else:
            sc.circle(p, 0.095, "GREEN", 2.0)
    L = 0.4
    for xs, d in ((XPEAK1 - 0.95, -1), (XPEAK1 + 0.95, 1), (XVALLEY - 0.95, 1), (XVALLEY + 0.95, -1),
                  (XPEAK2 - 0.85, -1), (XPEAK2 + 0.85, 1)):
        p = (xs, _V(xs) * YS)
        sc.vec(p, (xs + d * L, p[1]), None, "PINK", 3.0, head=11)
        sc.dotp(p, 3.0, "HEAD")
    sc.label((XVALLEY, -1.05), "stable: " + d1 + " = 0, " + d2 + " > 0", "GREEN", "middle", 16, italic=False)
    sc.label((XPEAK1, _V(XPEAK1) * YS + 0.4), "unstable: " + d2 + " < 0", "GREEN", "start", 16, italic=False, dx=46)
    sc.label((XPEAK2, _V(XPEAK2) * YS + 0.4), "unstable: " + d2 + " < 0", "GREEN", "middle", 16, italic=False)
    # force plot below, aligned in x
    y0, sF = -3.3, 0.5
    sc.vec((-1.3, y0), (8.4, y0), None, "EDGE", 1.4, head=8)
    sc.vec((0.0, y0 - 1.0), (0.0, y0 + 1.0), None, "EDGE", 1.4, head=8)
    sc.label((8.4, y0), "x", "TEXT", "middle", 16, weight="700", dx=2, dy=24)
    sc.label((0.0, y0 + 1.0), S("F", "x"), "PINK", "start", 17, weight="700", dx=12, dy=4)
    sc.poly([(-1.0 + 9.0 * i / 240, y0 + sF * _F(-1.0 + 9.0 * i / 240)) for i in range(241)], "PINK", 2.6)
    for xc, stable in crit:
        p = (xc, y0)
        if stable:
            sc.dotp(p, 5.5, "GREEN")
        else:
            sc.circle(p, 0.095, "GREEN", 2.0)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-pendulum")
def pendulum():
    sc = Scene(720, 560, (230, 120), 80)
    O = (0.0, 0.0)
    TH, L = 30.0, 4.0
    th = math.radians(TH)
    P = (L * math.sin(th), -L * math.cos(th))
    H = (0.0, P[1])
    fixed_axis(sc, O, 0, 3.6, "x", off=(10, 6))
    fixed_axis(sc, O, 90, 1.2, "y", off=(14, 4))
    sc.line(O, (0.0, -4.4), "EDGE", 1.3, "7 5")
    triangle(sc, [O, H, P], ORANGE, 0.16)
    sc.dashed((P[0], 0.0), P)
    sc.line((P[0], 0.0), (P[0], 0.1), "EDGE", 1.3)
    right_angle(sc, H, 90, 0, 0.14)
    sc.rod(O, P, 5.0, "HEAD")
    # arcs of theta and of theta_pol
    sc.arc(O, 1.2, -90, -90 + TH, "GREEN", 1.8, head=True)
    sc.label(_pt(O, -90 + TH / 2, 1.55), "θ", "GREEN", "middle", 18, dx=-4, dy=8)
    sc.arc(O, 2.1, 0, -90 + TH, "GREEN", 1.8, head=True)
    sc.label(_pt(O, -30, 2.1), "θ" + S("", "pol") + " = θ " + MINUS + " π/2 (negative here)", "GREEN", "start", 17, dx=34, dy=-6)
    # leg labels
    sc.label((0.0, P[1] / 2), "ℓ cos θ (adjacent)", "HEAD", "end", 17, dx=-12, dy=5)
    sc.label((P[0] / 2, P[1]), "ℓ sin θ (opposite)", "HEAD", "middle", 17, dy=28)
    sc.label((P[0] / 2, P[1] / 2), "ℓ", "HEAD", "middle", 19, dx=22, dy=-12)
    # coordinates of P
    sc.label((P[0], 0.0), "x = ℓ sin θ", "HEAD", "middle", 16, italic=False, dy=-12)
    sc.label((P[0], P[1] / 2), "y = " + MINUS + "ℓ cos θ", "HEAD", "start", 16, italic=False, dx=10, dy=5)
    sc.dotp(P, 7.0, "HEAD")
    sc.label(P, "m", "HEAD", "start", 19, dx=12, dy=22)
    sc.dotp(O, 3.0, "HEAD")
    axis_out(sc, O, bold("k"), "HEAD", off=(-26, -8))
    gx = 3.7
    sc.vec((gx, -1.5), (gx, -3.0), bold("g"), "PINK", 3.6, name_off=(14, 4), size=19, head=13)
    return sc


@_fig("t2-pendulum-basis")
def pendulum_basis():
    sc = Scene(740, 470, (230, 220), 72)
    TH = 30.0
    th = math.radians(TH)
    P = (0.0, 0.0)
    eR = (math.sin(th), -math.cos(th))
    et = (math.cos(th), math.sin(th))
    L = 2.0
    # rod from the upper left (towards O) and the dashed -j
    q = _add(P, (-eR[0], -eR[1]), 2.3)
    sc.line(P, q, "EDGE", 1.8)
    sc.label(q, "to O", "TEXT", "middle", 16, dy=-8, italic=False)
    sc.line(P, (0.0, -L), "EDGE", 1.4, "6 4")
    # triangles of e_R (legs along -j and along i) and of e_theta
    tipR = _add(P, eR, L)
    tipT = _add(P, et, L)
    footR = (0.0, tipR[1])
    footT = (tipT[0], 0.0)
    triangle(sc, [P, footR, tipR], ORANGE, 0.16)
    triangle(sc, [P, footT, tipT], ORANGE, 0.16)
    sc.dashed(footR, tipR)
    sc.dashed(footT, tipT)
    right_angle(sc, footR, 90, 0, 0.12)
    right_angle(sc, footT, 180, 90, 0.12)
    # fixed basis (grey) at the bob
    sc.vec(P, (L * 1.2, 0), bold("i"), "EDGE", 3.0, name_off=(12, 6), size=18, head=11)
    sc.vec(P, (0, L * 1.25), bold("j"), "EDGE", 3.0, name_off=(-14, 6), size=18, head=11)
    sc.label((0.0, -L), MINUS + bold("j"), "TEXT", "middle", 17, dx=-20, dy=14)
    # polar basis (blue)
    sc.vec(P, tipR, None, "BLUE", 3.6, head=12)
    sc.vec(P, tipT, None, "BLUE", 3.6, head=12)
    sc.label(tipR, _vb("e", "R"), "BLUE", "start", 19, weight="700", dx=10, dy=6)
    sc.label(tipT, _vb("e", "θ"), "BLUE", "start", 19, weight="700", dx=10, dy=-4)
    # angles
    sc.arc(P, 0.95, -90, -90 + TH, "GREEN", 1.8, head=True)
    sc.label(_pt(P, -90 + TH / 2, 1.3), "θ", "GREEN", "middle", 18, dx=14, dy=6)
    sc.arc(P, 1.0, 0, TH, "GREEN", 1.8, head=True)
    sc.label(_pt(P, TH / 2, 1.3), "θ", "GREEN", "middle", 18, dx=2, dy=8)
    # leg labels
    sc.label((0.0, tipR[1] / 2), MINUS + "cos θ " + bold("j"), "HEAD", "end", 17, dx=-10, dy=5, italic=False)
    sc.label((tipR[0] / 2, tipR[1]), "sin θ", "HEAD", "middle", 17, dy=24, italic=False)
    sc.label((tipT[0] / 2, 0.0), "cos θ", "HEAD", "middle", 17, dy=22, dx=22, italic=False)
    sc.label((tipT[0], tipT[1] / 2), "sin θ", "HEAD", "start", 17, dx=10, dy=5, italic=False)
    sc.dotp(P, 4.0, "HEAD")
    axis_out(sc, P, bold("k"), "HEAD", off=(-24, 22))
    # matrix
    _matrix(sc, 470, 110, "[" + S("", "0") + "R" + S("", "pol") + "]",
            [["sin θ", "cos θ", "0"], [MINUS + "cos θ", "sin θ", "0"], ["0", "0", "1"]], cw=74)
    return sc


@_fig("t2-pendulum-fbd")
def pendulum_fbd():
    sc = Scene(680, 470, (250, 190), 100)
    TH = 30.0
    th = math.radians(TH)
    P = (0.0, 0.0)
    eR = (math.sin(th), -math.cos(th))
    et = (math.cos(th), math.sin(th))
    toO = (-eR[0], -eR[1])
    mg = 2.0
    A = _add(P, eR, mg * math.cos(th))              # foot of the component along e_R
    W = (0.0, -mg)                                  # tip of the weight
    # rod direction to O (dashed grey), free body circle
    sc.line(P, _add(P, toO, 2.0), "EDGE", 1.4, "7 5")
    sc.circle(P, 0.3, "EDGE", 1.5, "6 4")
    sc.label(P, "free body", "TEXT", "end", 15, italic=False, dx=-32, dy=2)
    # triangle of the weight and its components
    triangle(sc, [P, A, W], ORANGE, 0.16)
    right_angle(sc, A, 120, 210, 0.12)
    _dvec(sc, P, A, "PINK", 1.8, "6 4", 9)
    _dvec(sc, A, W, "PINK", 1.8, "6 4", 9)
    # velocity (dashed orange), polar basis (blue, short)
    vt = _add(P, et, 1.9)
    _dvec(sc, P, vt, ORANGE, 1.8, "6 4", 9)
    sc.label(vt, "ℓ" + dot1("θ") + " " + _vb("e", "θ"), ORANGE, "start", 17, weight="700", dx=10, dy=-4)
    sc.vec(P, _add(P, eR, 0.7), None, "BLUE", 3.0, head=11)
    sc.vec(P, _add(P, et, 0.7), None, "BLUE", 3.0, head=11)
    sc.label(_add(P, eR, 0.7), _vb("e", "R"), "BLUE", "start", 18, weight="700", dx=8, dy=8)
    sc.label(_add(P, et, 0.7), _vb("e", "θ"), "BLUE", "middle", 18, weight="700", dx=-12, dy=26)
    # forces (pink)
    sc.vec(P, W, None, "PINK", 4.0, head=13)
    sc.label((0.0, -mg * 0.45), "m g", "PINK", "end", 19, weight="700", dx=-12, dy=5)
    ft = _add(P, toO, 1.5)
    sc.vec(P, ft, None, "PINK", 4.0, head=13)
    sc.label(_add(P, toO, 0.85), S("F", "t"), "PINK", "end", 20, weight="700", dx=-12, dy=0)
    sc.label(_add(P, eR, 1.3), "m g cos θ", "PINK", "start", 16, italic=False, dx=14, dy=6)
    sc.label(_add(A, (-eR[1] * 0 - 0.866, -0.5), 0.5), "m g sin θ", "PINK", "start", 16, italic=False, dx=12, dy=34)
    # angle between the weight and e_R
    sc.arc(P, 0.8, -90, -90 + TH, "GREEN", 1.8, head=True)
    sc.label(_pt(P, -90 + TH / 2, 1.1), "θ", "GREEN", "middle", 18, dx=10, dy=12)
    sc.dotp(P, 5.5, "HEAD")
    axis_out(sc, (-1.45, 1.2), bold("k"), "HEAD", off=(0, 28))
    return sc


@_fig("t2-pendulum-potential")
def pendulum_potential():
    sc = Scene(820, 440, (400, 330), 76)
    V0 = "V" + S("", "0")
    X = 1.3 * math.pi
    sc.vec((-4.35, 0.0), (4.45, 0.0), None, "EDGE", 1.4, head=8)
    sc.vec((0.0, -0.3), (0.0, 3.0), None, "EDGE", 1.4, head=8)
    sc.label((4.45, 0.0), "θ", "TEXT", "middle", 17, weight="700", dx=4, dy=24)
    sc.label((0.0, 3.0), V0 + "(θ)", "TEXT", "start", 17, weight="700", dx=12, dy=4)
    # levels: 2 m g l (dotted), E1, E2 (dashed blue)
    sc.line((-4.3, 2.0), (4.3, 2.0), "EDGE", 1.4, "2 4")
    sc.label((-4.3, 2.0), "2mgℓ", "TEXT", "end", 16, italic=False, dx=-6, dy=5)
    for e, nm in ((1.0, "0,1"), (2.5, "0,2")):
        sc.line((-4.3, e), (4.3, e), "BLUE", 1.8, "8 5")
        sc.label((4.3, e), S("E", nm), "BLUE", "start", 18, weight="700", dx=6, dy=5)
    # curve and parabola
    sc.poly([(-X + 2 * X * i / 300, 1 - math.cos(-X + 2 * X * i / 300)) for i in range(301)], "HEAD", 2.6)
    xp = math.sqrt(2 * 2.6)
    sc.poly([(-xp + 2 * xp * i / 200, (-xp + 2 * xp * i / 200) ** 2 / 2) for i in range(201)], "HEAD", 2.0, "7 5")
    # turning points of E_{0,1}
    ts = math.acos(1 - 1.0)
    for sgn in (-1, 1):
        sc.line((sgn * ts, 0.0), (sgn * ts, 1.0), "EDGE", 1.2, "5 4")
        sc.dotp((sgn * ts, 1.0), 5.0, "GREEN")
    sc.label((-ts, 0.0), MINUS + "θ*", "GREEN", "middle", 17, dy=24)
    sc.label((ts, 0.0), "θ*", "GREEN", "middle", 17, dy=24)
    # equilibria
    sc.dotp((0.0, 0.0), 5.0, "GREEN")
    sc.label((0.0, 0.0), "stable", "GREEN", "middle", 16, italic=False, dy=46)
    for sgn in (-1, 1):
        p = (sgn * math.pi, 2.0)
        sc.circle(p, 0.09, "GREEN", 2.0)
        sc.label(p, "unstable", "GREEN", "middle", 16, italic=False, dy=-14)
    sc.line((1.0, 0.0), (1.0, 0.07), "EDGE", 1.3)
    sc.label((1.0, 0.0), "1", "TEXT", "middle", 15, italic=False, dy=20)
    sc.label((0.0, 0.0), "0, 0", "TEXT", "end", 15, italic=False, dx=-8, dy=20)
    return sc
