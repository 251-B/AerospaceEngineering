"""Theory figures of Topic 1, Chapter 2 (Kinematics of a Point Particle): Sections 9 to 16 of Notes.pdf.

Same colour code and axonometric projection as the chapter 1 figures of t1.py (fixed axes and B0 grey, moving or local
bases blue, auxiliary vectors and the intrinsic triad orange, angles green, trajectories dark red); the helpers are the
ones of that module.
"""
import math

from figures.em_theory import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.em_th.t1 import (DRED, MINUS, ORANGE, P3, _add, _arc3, _circ3, _cross, _d, _line3, _matrix, _mul,
                              _pl, _poly3, _unit3, _v3, _vec3)
from figures.mech import S, Scene, bold

TRAJ = DRED


def _vb(name, sub=None, sup=None):
    """Bold vector name with optional sub- and superscript."""
    return S(bold(name), sub, sup)


def _norm2(v):
    return math.hypot(v[0], v[1])


def _axes3(sc, O, lens, names=("x", "y", "z"), offs=((-10, 14), (14, 6), (-4, -10))):
    """Thin grey axes of the axonometric view from the 3D point O, with their names at the tips."""
    for i in range(3):
        v = [0.0, 0.0, 0.0]
        v[i] = lens[i]
        _vec3(sc, O, tuple(v), None, "EDGE", 1.3, head=8)
        sc.label(P3(_v3(O, tuple(v))), names[i], "TEXT", "middle", 17, weight="700", dx=offs[i][0], dy=offs[i][1])


def _unit_frame(sc, O, L, names=("i", "j", "k"), offs=((-12, 12), (8, 20), (-12, 4)), basis=None, col="HEAD", w=3.0,
                sub=None):
    """The three thick unit vectors of a basis at the 3D point O (default the fixed basis)."""
    basis = basis or ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for v, nm, off in zip(basis, names, offs):
        _vec3(sc, O, _mul(v, L), _vb(nm, sub), col, w, off=off, size=17, head=11)


def _curve3(f, u0, u1, n=160):
    return [f(u0 + (u1 - u0) * i / n) for i in range(n + 1)]


def _deriv3(f, u, h=1e-4):
    a, b = f(u - h), f(u + h)
    return tuple((b[i] - a[i]) / (2 * h) for i in range(3))


def _ellipse_outline(L, n=120):
    """Outline of the unit sphere under the linear part of P3: points of the 2D ellipse (for a sphere of radius L)."""
    ax, ay = EX_X, EX_Y
    # P3(v) = (v0*ax + v1, v0*ay + v2): M M^T
    a11 = ax * ax + 1.0
    a12 = ax * ay
    a22 = ay * ay + 1.0
    det = a11 * a22 - a12 * a12
    sd = math.sqrt(det)
    tr = a11 + a22
    s = math.sqrt(tr + 2 * sd)
    m = ((a11 + sd) / s, a12 / s, (a22 + sd) / s)     # symmetric square root
    pts = []
    for i in range(n + 1):
        t = 2 * math.pi * i / n
        c, sn = math.cos(t), math.sin(t)
        pts.append((L * (m[0] * c + m[1] * sn), L * (m[1] * c + m[2] * sn)))
    return pts


EX_X, EX_Y = -0.473, -0.368


def _dvec3(sc, a, b, col="ACC", w=1.6, dash="6 4", head=9):
    """Thin dashed arrow from the 3D point a to b."""
    pa, pb = P3(a), P3(b)
    ang = math.atan2(-(pb[1] - pa[1]), pb[0] - pa[0])
    k = 0.6 * head / sc.k
    sc.line(pa, (pb[0] - k * math.cos(ang), pb[1] + k * math.sin(ang)), col, w, dash)
    arrow_head(sc.c, sc.P(pa), sc.P(pb), col, head)


def _tick2(sc, p2, t2, half=0.12, col="HEAD", w=1.6):
    """Short tick across the curve at the 2D point p2 with 2D tangent t2."""
    n = math.hypot(*t2) or 1.0
    nx, ny = -t2[1] / n, t2[0] / n
    sc.line((p2[0] - half * nx, p2[1] - half * ny), (p2[0] + half * nx, p2[1] + half * ny), col, w)


from figures.svgkit import arrow_head  # noqa: E402


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-reference-frames",
        r"Two reference frames, each an origin with an orthonormal basis, and the two position vectors of one point measured from their origins.",
        r"A reference frame is an origin plus a basis; the position of $P$ differs from $S_0$ and from $S_1$ because their origins differ, and $\mathcal B_1$ may rotate with $\boldsymbol\omega_{10}$ ([Lecture 1, Slides 8 and 12]).")
def reference_frames():
    sc = Scene(760, 480, (250, 365), 66)
    O = (0.0, 0.0, 0.0)
    for pts, nm, at, off in (
            ([(0, 0, 0), (1.9, 0, 0), (1.9, 2.5, 0), (0, 2.5, 0)], "Oxy", (1.9, 2.5, 0), (-6, 16)),
            ([(0, 0, 0), (1.9, 0, 0), (1.9, 0, 2.3), (0, 0, 2.3)], "Oxz", (1.9, 0, 2.3), (-6, -8)),
            ([(0, 0, 0), (0, 2.5, 0), (0, 2.5, 2.3), (0, 0, 2.3)], "Oyz", (0, 2.5, 2.3), (-26, -8))):
        _poly3(sc, pts, "EDGE", 1.1, "5 4", "EDGE", True, 0.06)
        sc.label(P3(at), nm, "TEXT", "middle", 15, dx=off[0], dy=off[1])
    _axes3(sc, O, (3.0, 4.0, 3.7), ("Ox", "Oy", "Oz"), ((-12, 14), (16, 6), (-4, -10)))
    _unit_frame(sc, O, 1.0, sub="0", offs=((-18, 12), (6, 22), (-16, 4)))
    a, b = math.radians(40), math.radians(-25)
    ca, sa, cb, sb = math.cos(a), math.sin(a), math.cos(b), math.sin(b)
    i1 = (ca, sa, 0.0)
    j1 = (-sa * cb, ca * cb, sb)
    k1 = (sa * sb, -ca * sb, cb)
    O1 = (0.5, 3.3, 1.8)
    P = (0.1, 2.1, 4.5)
    _dvec3(sc, O, O1, "ACC", 1.6)
    _vec3(sc, O, P, None, ORANGE, 3.0, head=11)
    _vec3(sc, O1, _v3(P, O1, -1.0), None, ORANGE, 3.0, head=11)
    sc.label(P3(_mul(P, 0.62)), _vb("r", "0", "P"), "ACC", "end", 18, dx=-12, dy=0, weight="700")
    sc.label(P3(_v3(O1, _v3(P, O1, -1.0), 0.55)), _vb("r", "1", "P"), "ACC", "start", 18, dx=14, dy=0, weight="700")
    for v, nm, off in ((i1, "i", (-12, 14)), (j1, "j", (14, 4)), (k1, "k", (10, -10))):
        _vec3(sc, O1, v, _vb(nm, "1"), "BLUE", 3.0, off=off, size=17, head=11)
    sc.label(P3(_mul(O1, 0.5)), "OO" + S("", "1"), "ACC", "start", 16, dx=8, dy=28)
    sc.dotp(P3(O1), 3.5, "BLUE")
    sc.dotp(P3(O), 3.5)
    sc.dotp(P3(P), 5.0, "ACC")
    sc.label(P3(P), "P", "HEAD", "middle", 18, dx=14, dy=-8)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=-6)
    sc.label(P3(O1), "O" + S("", "1"), "BLUE", "end", 17, dx=-10, dy=22)
    cw = _v3(O1, k1, 0.55)
    _circ3(sc, cw, i1, j1, 0.5, -110, 130, "BLUE", head=True, w=2.0)
    sc.label(P3(_v3(cw, j1, -0.0)), _vb("ω", "10"), "BLUE", "start", 17, dx=34, dy=-4)
    sc.label(P3(O), "S" + S("", "0") + " : {O; ℬ" + S("", "0") + "}", "HEAD", "end", 16, dx=-84, dy=-22, italic=False)
    sc.label(P3(O1), "S" + S("", "1") + " : {O" + S("", "1") + "; ℬ" + S("", "1") + "}", "BLUE", "start", 16, dx=60, dy=52,
             italic=False)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _wavy(u):
    return (1.2 + 0.9 * math.sin(2 * math.pi * 0.9 * u + 0.6), 2.4 + 3.2 * u, 1.0 + 2.2 * math.sin(math.pi * u))


@figure("t1-position-velocity",
        r"A curved trajectory with the position vectors at two instants, the displacement chord between them, the arc length and the tangent velocity.",
        r"Position vector at two consecutive instants; as $\Delta t$ tends to zero the chord $\Delta\mathbf r_0^P$ becomes tangent and $\Delta\mathbf r_0^P/\Delta t$ tends to $\mathbf v_0^P$ (Notes.pdf Fig. 2.1).")
def position_velocity():
    sc = Scene(780, 490, (170, 372), 78)
    O = (0.0, 0.0, 0.0)
    u0, u1, u2 = 0.06, 0.26, 0.66
    _axes3(sc, O, (3.0, 6.3, 3.9), ("x", "y", "z"), ((-10, 14), (14, 6), (-4, -10)))
    sc.poly([P3(p) for p in _curve3(_wavy, 0.0, 1.0)], TRAJ, 2.6)
    sc.poly([P3(p) for p in _curve3(_wavy, u1, u2, 40)], TRAJ, 5.5)
    P1, P2 = _wavy(u1), _wavy(u2)
    _vec3(sc, O, P1, None, ORANGE, 2.4, head=10)
    _vec3(sc, O, P2, None, ORANGE, 2.4, head=10)
    sc.label(P3(_mul(P1, 0.5)), _vb("r", "0", "P") + "(t)", "ACC", "end", 17, dx=-10, dy=-4, weight="700")
    sc.label(P3(_mul(P2, 0.45)), _vb("r", "0", "P") + "(t+Δt) = " + _vb("r", "0", "P") + " + Δ" + _vb("r", "0", "P"), "ACC",
             "start", 17, dx=14, dy=20, weight="700")
    _vec3(sc, P1, _v3(P2, P1, -1.0), None, ORANGE, 3.2, head=11)
    sc.label(P3(_v3(P1, _v3(P2, P1, -1.0), 0.5)), "Δ" + _vb("r", "0", "P"), "ACC", "middle", 17, dx=-4, dy=24, weight="700")
    sc.dotp(P3(P1), 4.2)
    sc.dotp(P3(P2), 4.2)
    sc.label(P3(P1), "P(t)", "HEAD", "end", 17, dx=-12, dy=-12)
    sc.label(P3(P2), "P(t+Δt)", "HEAD", "start", 17, dx=12, dy=-10)
    p0 = P3(_wavy(u0))
    _tick2(sc, p0, P3(_deriv3(_wavy, u0)))
    sc.label(p0, "s = 0", "HEAD", "start", 16, dx=12, dy=20)
    sc.label(P3(_wavy((u0 + u1) / 2)), "s", "HEAD", "start", 17, dx=16, dy=6)
    sc.label(P3(_wavy((u1 + u2) / 2)), "Δs", "HEAD", "middle", 17, dx=14, dy=-22)
    sc.label(P3(_wavy(0.97)), "Trajectory", TRAJ, "start", 16, dx=12, dy=0, italic=False)
    d = P3(_deriv3(_wavy, u1))
    n = _norm2(d)
    tip = (P3(P1)[0] + 1.1 * d[0] / n, P3(P1)[1] + 1.1 * d[1] / n)
    sc.vec(P3(P1), tip, _vb("v", "0", "P"), ORANGE, 3.4, name_off=(8, -14), size=18, head=12)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=-6)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _space(u):
    return (1.2 + 1.3 * math.cos(u), 2.7 + 1.3 * math.sin(u), 0.5 + 0.95 * u)


def _triad(f, u):
    r1 = _deriv3(f, u)
    et = _unit3(r1)
    h = 1e-3
    a, b = _unit3(_deriv3(f, u - h)), _unit3(_deriv3(f, u + h))
    dn = tuple((b[i] - a[i]) / (2 * h) for i in range(3))
    en = _unit3(dn)
    eb = _cross(et, en)
    return et, en, eb


@figure("t1-trajectory-triad",
        r"A space curve with the chord and arc between two neighbouring points and the tangent, normal and binormal unit vectors at one point.",
        r"Trajectory, arc length and the intrinsic basis $\{\mathbf e_t,\mathbf e_n,\mathbf e_b\}$ at $P$; $\mathbf e_t$ and $\mathbf e_n$ span the osculating plane ([Lecture 1, Slides 24 and 27]).")
def trajectory_triad():
    sc = Scene(800, 640, (150, 540), 88)
    O = (0.0, 0.0, 0.0)
    _axes3(sc, O, (2.5, 5.6, 5.3), ("x", "y", "z"), ((-10, 14), (14, 6), (-4, -10)))
    u0, ub, uc = 0.05, 1.0, 1.9
    sc.poly([P3(p) for p in _curve3(_space, u0, 4.2)], TRAJ, 2.6)
    sc.poly([P3(p) for p in _curve3(_space, ub, uc, 30)], TRAJ, 5.5)
    P1, P2 = _space(ub), _space(uc)
    et, en, eb = _triad(_space, ub)
    L = 1.4
    corners = [_v3(_v3(P1, et, L * a), en, L * b) for a, b in ((-0.5, -0.4), (1.5, -0.4), (1.5, 1.5), (-0.5, 1.5))]
    _poly3(sc, corners, "EDGE", 1.2, "5 4", "EDGE", True, 0.10)
    sc.label(P3(corners[1]), "osculating plane", "TEXT", "start", 15, dx=10, dy=4, italic=False)
    _vec3(sc, O, P1, None, ORANGE, 2.2, head=10)
    _vec3(sc, O, P2, None, ORANGE, 2.2, head=10)
    sc.label(P3(_mul(P1, 0.40)), _vb("r", "0", "P") + "(s)", "ACC", "middle", 17, dx=0, dy=26, weight="700")
    sc.label(P3(_mul(P2, 0.22)), _vb("r", "0", "P") + "(s+Δs)", "ACC", "middle", 17, dx=-6, dy=-16, weight="700")
    _vec3(sc, P1, _v3(P2, P1, -1.0), None, ORANGE, 3.0, head=11)
    sc.label(P3(_v3(P1, _v3(P2, P1, -1.0), 0.5)), "Δ" + _vb("r", "0", "P"), "ACC", "end", 17, dx=-10, dy=6, weight="700")
    for v, nm, off in ((et, "t", (18, 16)), (en, "n", (-18, 4)), (eb, "b", (-8, -12))):
        _vec3(sc, P1, _mul(v, L), _vb("e", nm), ORANGE, 3.6, off=off, size=18, head=12)
    sc.dotp(P3(P1), 4.2)
    sc.dotp(P3(P2), 4.2)
    sc.label(P3(P1), "P(s)", "HEAD", "end", 17, dx=-10, dy=22)
    sc.label(P3(P2), "P(s+Δs)", "HEAD", "start", 17, dx=12, dy=-6)
    sc.label(P3(_space((ub + uc) / 2)), "Δs", "HEAD", "start", 17, dx=12, dy=22)
    p0 = P3(_space(u0))
    _tick2(sc, p0, P3(_deriv3(_space, u0)))
    sc.label(p0, "s = s(t)", "HEAD", "end", 16, dx=-10, dy=14)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=-6)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-osculating-circle",
        r"The osculating circle of a trajectory with the tangent and normal unit vectors at two neighbouring points, and a detail of the small change of the tangent vector.",
        r"Osculating circle of centre $C$ and radius $\rho$: the tangent turns by the angle $\Delta\theta_t$ subtended at $C$, so $\lvert d\mathbf e_t/ds\rvert$ is $1/\rho$ and $\mathbf e_n$ points to $C$ (Notes.pdf Fig. 2.2).")
def osculating_circle():
    sc = Scene(1000, 430, (215, 150), 64)
    C = (0.0, 0.0)
    rho = 3.0
    a1, dth = -78.0, 25.0
    a2 = a1 + dth
    P1 = _add(C, _d(a1), rho)
    P2 = _add(C, _d(a2), rho)
    sc.arc(C, rho, -160, 28, "EDGE", 1.4, "7 5")
    f0 = math.radians(a1)

    def curve(t):
        ph = f0 + t
        r = rho * (1 + 0.10 * t ** 3)
        return (r * math.cos(ph), r * math.sin(ph))
    sc.poly([curve(-1.1 + 2.3 * i / 140) for i in range(141)], TRAJ, 2.8)
    sc.poly([_add(C, _d(a1 + dth * i / 20), rho) for i in range(21)], TRAJ, 5.2)
    sc.line(C, P1, "EDGE", 1.3)
    sc.line(C, P2, "EDGE", 1.3)
    sc.arc(C, 1.0, a1, a2, "GREEN", 1.7, head=True)
    sc.label(_add(C, _d(a2 + 5), 1.4), "Δθ" + S("", "t"), "GREEN", "start", 17, dy=5, dx=4)
    sc.label(_add(C, _d(a1), 1.3), "ρ", "HEAD", "middle", 18, dx=-14, dy=0)
    sc.dotp(C, 3.6)
    sc.label(C, "C", "HEAD", "middle", 18, dx=-14, dy=-8)
    L = 1.1
    specs = ((a1, "s", {"t": (26, 20), "n": (-44, 0)}), (a2, "s+Δs", {"t": (46, 4), "n": (66, -4)}))
    for ang, tag, offs in specs:
        P = _add(C, _d(ang), rho)
        et = _d(ang + 90)
        en = _d(ang + 180)
        sc.vec(P, _add(P, et, L), _vb("e", "t") + "(" + tag + ")", ORANGE, 3.4, name_off=offs["t"], size=17, head=11)
        sc.vec(P, _add(P, en, L), _vb("e", "n") + "(" + tag + ")", ORANGE, 3.4, name_off=offs["n"], size=17, head=11)
        right_angle(sc, P, ang + 180, ang + 90, 0.2, "EDGE")
    sc.dotp(P2, 4.0)
    sc.label(P2, "P(s+Δs)", "HEAD", "start", 17, dx=14, dy=26)
    axis_out(sc, P1, None, "HEAD", r_px=9)
    sc.label(P1, _vb("e", "b") + " (out of the paper)", "HEAD", "start", 16, dx=-60, dy=36)
    sc.label(P1, "P(s)", "HEAD", "middle", 17, dx=-30, dy=14)
    # detail panel: the two tangents from a common origin
    D = (6.0, -1.3)
    Lg = 3.1
    b1, b2 = 15.0, 15.0 + dth
    T1, T2 = _add(D, _d(b1), Lg), _add(D, _d(b2), Lg)
    Mx = ((T1[0] + T2[0]) / 2, (T1[1] + T2[1]) / 2)
    sc.note((D[0] - 0.4, 2.0), "detail: change of the tangent vector", "TEXT", "start", 14)
    triangle(sc, [D, T1, T2], ORANGE, 0.14)
    sc.line(D, Mx, "EDGE", 1.3, "5 4")
    mid_ang = (b1 + b2) / 2
    right_angle(sc, Mx, mid_ang + 180, mid_ang + 90, 0.17, "EDGE")
    sc.vec(D, T1, _vb("e", "t") + "(s)", ORANGE, 3.2, name_off=(40, 24), size=17, head=11)
    sc.vec(D, T2, _vb("e", "t") + "(s+Δs)", ORANGE, 3.2, name_off=(10, -14), size=17, head=11)
    sc.vec(T1, T2, None, ORANGE, 3.0, head=10)
    base_dir = (T2[0] - T1[0], T2[1] - T1[1])
    sc.label(_add(T1, base_dir, 0.22), "Δ" + _vb("e", "t"), "ACC", "start", 17, dx=14, dy=6, weight="700")
    sc.label(_add(T1, base_dir, 0.78), "opposite leg sin(Δθ" + S("", "t") + "/2)", "HEAD", "start", 15, dx=16, dy=4,
             italic=False)
    sc.arc(D, 1.0, b1, b2, "GREEN", 1.7, head=True)
    sc.label(_add(D, _d(b1 - 8), 1.45), "Δθ" + S("", "t"), "GREEN", "middle", 17, dy=5)
    sc.arc(D, 1.9, mid_ang, b2, "GREEN", 1.5, head=True)
    sc.label(_add(D, _d(b2 + 9), 1.9), "Δθ" + S("", "t") + "/2", "GREEN", "end", 16, dy=0, dx=-4)
    sc.label(_add(D, _d(b2), 2.55), "hypotenuse 1", "HEAD", "end", 15, dx=-8, dy=-12, italic=False)
    sc.dotp(D, 3.4)
    tail = (D[0] + 0.5, D[1] - 2.3)
    sc.vec(tail, _add(tail, _d(mid_ang + 90), 1.0), None, ORANGE, 3.0, head=10)
    sc.label(tail, "Δ" + _vb("e", "t") + " points towards C", "HEAD", "start", 15, dx=12, dy=10, italic=False)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-path-angle",
        r"A planar curve with the arc element ds as the hypotenuse of a right triangle whose legs are dx and dy, and the angle of the tangent with the x axis.",
        r"In a planar problem $dx = ds\cos\theta_t$ and $dy = ds\sin\theta_t$, with $\theta_t$ the angle of the tangent from $Ox$ (Notes.pdf Fig. 2.3).")
def path_angle():
    sc = Scene(760, 470, (90, 410), 78)
    O = (0.0, 0.0)
    TH = 35.0
    c, s_ = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    k2 = 0.15
    xP = math.tan(math.radians(TH)) / (2 * k2)

    def yc(x):
        return 1.3 + k2 * x * x
    P = (xP, yc(xP))
    ds = 1.9
    Q = (P[0] + ds * c, P[1] + ds * s_)
    F = (Q[0], P[1])
    fixed_axis(sc, O, 0, 5.6, "Ox", off=(18, 6))
    fixed_axis(sc, O, 90, 5.0, "Oy", off=(16, 4))
    sc.vec(O, (1, 0), bold("i"), "HEAD", 3.0, name_off=(0, 22), size=17, head=11)
    sc.vec(O, (0, 1), bold("j"), "HEAD", 3.0, name_off=(-14, 4), size=17, head=11)
    axis_out(sc, O, bold("k"), "HEAD", off=(-20, 24))
    sc.poly([(0.15 + 4.5 * i / 100, yc(0.15 + 4.5 * i / 100)) for i in range(101)], TRAJ, 2.8)
    triangle(sc, [P, F, Q], ORANGE, 0.20)
    sc.line((P[0] - 0.9, P[1]), (F[0] + 0.0, F[1]), "EDGE", 1.2, "6 4")
    sc.dashed(F, Q)
    right_angle(sc, F, 180, 90, 0.14)
    sc.line(P, Q, ORANGE, 2.2)
    sc.vec(P, (P[0] + 1.05 * c, P[1] + 1.05 * s_), _vb("e", "t"), ORANGE, 3.6, name_off=(4, 22), size=18, head=12)
    en = (-s_, c)
    sc.vec(P, (P[0] + 1.05 * en[0], P[1] + 1.05 * en[1]), _vb("e", "n"), ORANGE, 3.6, name_off=(-16, -2), size=18, head=12)
    sc.arc(P, 0.8, 0, TH, "GREEN", 1.7, head=True)
    sc.label(_add(P, _d(TH / 2 - 1), 1.18), "θ" + S("", "t"), "GREEN", "middle", 17, dy=5, dx=6)
    sc.dotp(P, 4.0)
    sc.dotp(Q, 3.6)
    sc.label(P, "P(s)", "HEAD", "end", 17, dx=-24, dy=-14)
    sc.label(Q, "P(s+ds)", "HEAD", "start", 17, dx=-6, dy=-12)
    sc.label(_add(P, (c, s_), 0.75 * ds), "ds", "ACC", "middle", 17, dx=14, dy=24, weight="700")
    sc.label(((P[0] + F[0]) / 2, P[1]), "dx = ds cos θ" + S("", "t") + " (adjacent)", "HEAD", "middle", 15, dy=26)
    sc.label(F, "dy = ds sin θ" + S("", "t"), "HEAD", "start", 15, dx=12, dy=-(Q[1] - P[1]) * 78 / 2 - 6)
    sc.label(F, "(opposite)", "TEXT", "start", 14, dx=12, dy=-(Q[1] - P[1]) * 78 / 2 + 12, italic=False)
    sc.dotp(O, 2.0, "HEAD")
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _grid(q1, q2):
    return (1.2 * q1 + 0.45 * math.sin(0.8 * q2 + 0.25 * q1) + 0.5,
            1.0 * q2 + 0.40 * math.sin(0.7 * q1 + 0.5) + 0.04 * q1 * q2 + 0.5)


def _gd(q1, q2, i, h=1e-5):
    a = _grid(q1 + h * (i == 0), q2 + h * (i == 1))
    b = _grid(q1 - h * (i == 0), q2 - h * (i == 1))
    return ((a[0] - b[0]) / (2 * h), (a[1] - b[1]) / (2 * h))


@figure("t1-local-basis",
        r"A curved coordinate grid with the two coordinate vectors at one point, tangent to the coordinate lines, and their unit versions.",
        r"The coordinate vectors are tangent to the coordinate lines, $\mathbf u_{q_i} = \partial\mathbf r_0^P/\partial q_i$; normalised, they form the local basis $\mathcal B_{\mathcal C}(P)$ ([Lecture 1, Slide 15]).")
def local_basis():
    sc = Scene(800, 520, (60, 450), 76)
    qa, qb = 0.0, 4.4
    ra, rb = 0.0, 3.6
    for q1 in (0.0, 1.0, 2.0, 3.0, 4.0):
        sc.poly([_grid(q1, ra + (rb - ra) * i / 60) for i in range(61)], "BLUE", 1.3)
    for q2 in (0.0, 1.0, 2.0, 3.0):
        sc.poly([_grid(qa + (qb - qa) * i / 60, q2) for i in range(61)], "EDGE", 1.5)
    q1P, q2P = 2.0, 1.0
    P = _grid(q1P, q2P)
    u1, u2 = _gd(q1P, q2P, 0), _gd(q1P, q2P, 1)
    sc.vec(P, _add(P, u1, 0.85), _vb("u", "q₁"), ORANGE, 3.6, name_off=(24, 4), size=18, head=12)
    sc.vec(P, _add(P, u2, 0.85), _vb("u", "q₂"), ORANGE, 3.6, name_off=(-22, -8), size=18, head=12)
    n1, n2 = math.hypot(*u1), math.hypot(*u2)
    sc.vec(P, _add(P, u1, 0.5 / n1), _vb("e", "q₁"), "BLUE", 3.0, name_off=(4, 26), size=16, head=10)
    sc.vec(P, _add(P, u2, 0.5 / n2), _vb("e", "q₂"), "BLUE", 3.0, name_off=(-30, 6), size=16, head=10)
    sc.dotp(P, 4.2)
    sc.label(P, "P", "HEAD", "end", 18, dx=-12, dy=22)
    sc.label((0.2, 5.1), "at P:  " + _vb("u", "q") + "ᵢ = ∂" + _vb("r", "0", "P") + "/∂q" + "ᵢ", "HEAD", "start", 17, dx=0, dy=0)
    # growth arrows in the margins and the names of the families
    yb = -0.35
    sc.vec((0.8, yb), (3.6, yb), "q₁ grows", "HEAD", 1.8, name_off=(0, 24), size=15, head=9)
    sc.vec((-0.5, 0.9), (-0.5, 3.3), None, "HEAD", 1.8, head=9)
    sc.label((-0.5, 2.1), "q₂ grows", "HEAD", "start", 15, dx=10, dy=0)
    sc.label(_grid(4.0, 3.6), "q₁ = const", "BLUE", "middle", 15, dx=0, dy=-12)
    sc.label(_grid(4.4, 3.0), "q₂ = const", "TEXT", "start", 15, dx=10, dy=0)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _cyl_pt(R, th, z):
    return (R * math.cos(math.radians(th)), R * math.sin(math.radians(th)), z)


def _cylinder3(sc, R, z0, z1, col="EDGE"):
    """Faint dashed cylinder of radius R about Oz between the heights z0 and z1 (circles and the two silhouette lines)."""
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    for z in (z0, z1):
        _circ3(sc, (0, 0, z), ex, ey, R, 0, 360, col, head=False, w=1.1, dash="5 4", n=90)
    best = max(range(721), key=lambda i: P3(_cyl_pt(R, i / 2, 0))[0])
    worst = min(range(721), key=lambda i: P3(_cyl_pt(R, i / 2, 0))[0])
    for i in (best, worst):
        _line3(sc, _cyl_pt(R, i / 2, z0), _cyl_pt(R, i / 2, z1), col, 1.1, "5 4")


@figure("t1-cylindrical-3d",
        r"Cylindrical coordinates R, theta and z of a point, with the local basis e_R, e_theta, e_z drawn at the point.",
        r"Cylindrical coordinates $\{R,\theta,z\}$ and the local basis $\{\mathbf e_R,\mathbf e_\theta,\mathbf e_z\}$ at $P$ (Notes.pdf Fig. 2.4).")
def cylindrical_3d():
    sc = Scene(760, 560, (200, 440), 84)
    O = (0.0, 0.0, 0.0)
    R, TH, Z = 2.1, 40.0, 2.5
    P = _cyl_pt(R, TH, Z)
    Pp = _cyl_pt(R, TH, 0.0)
    uR = (math.cos(math.radians(TH)), math.sin(math.radians(TH)), 0.0)
    ut = (-math.sin(math.radians(TH)), math.cos(math.radians(TH)), 0.0)
    _cylinder3(sc, R, 0.0, Z)
    _poly3(sc, [O, Pp, _cyl_pt(R, TH, Z + 0.7), (0, 0, Z + 0.7)], "EDGE", 1.1, "5 4", "EDGE", True, 0.07)
    _axes3(sc, O, (3.1, 3.9, 4.0), ("x", "y", "z"), ((-10, 14), (14, 6), (-4, -10)))
    _unit_frame(sc, O, 1.0, offs=((-12, 14), (4, 22), (-14, 4)))
    _line3(sc, O, Pp, "EDGE", 1.4, "6 4")
    _line3(sc, Pp, P, "EDGE", 1.4, "6 4")
    mid = _arc3(sc, (1, 0, 0), uR, 0.8, "GREEN")
    sc.label(mid, "θ", "GREEN", "middle", 17, dx=8, dy=20)
    sc.label(P3(_mul(Pp, 0.5)), "R", "HEAD", "middle", 18, dx=14, dy=20)
    sc.label(P3(_mul(_v3(Pp, P), 0.5)), "z", "HEAD", "start", 18, dx=10, dy=4)
    _vec3(sc, O, P, None, ORANGE, 3.0, head=11)
    sc.label(P3(_mul(P, 0.66)), _vb("r", "0", "P"), "ACC", "end", 18, dx=-10, dy=-4, weight="700")
    _vec3(sc, P, _mul(uR, 1.3), _vb("e", "R"), "BLUE", 3.4, off=(-6, 24), size=18, head=11)
    _vec3(sc, P, _mul(ut, 1.1), _vb("e", "θ"), "BLUE", 3.4, off=(22, 8), size=18, head=11)
    _vec3(sc, P, (0, 0, 1), _vb("e", "z") + " ≡ " + bold("k"), "BLUE", 3.4, off=(-4, -14), size=18, head=11)
    sc.dotp(P3(P), 4.6, "ACC")
    sc.label(P3(P), "P", "HEAD", "end", 18, dx=-12, dy=-8)
    sc.dotp(P3(Pp), 3.6)
    sc.label(P3(Pp), "P′", "HEAD", "start", 17, dx=10, dy=14)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=-6)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _title_R(sub1, extra=""):
    return "[" + S("", "0") + "R" + S("", sub1) + "]" + extra


def _rot_pair(sc, Pp, th, L, n1, n2, hn, vn, minus, cs="cos θ", sn="sin θ", tn="θ", e2_lab=(-26, -8), e1_lab=(26, -4)):
    """At the 2D point Pp: grey copies of the horizontal and vertical axes (names hn, vn), the blue pair obtained by
    turning them by th (n1 near the horizontal, n2 near the vertical), the two unit-hypotenuse triangles, the two
    green angles and the leg labels."""
    c, s_ = math.cos(math.radians(th)), math.sin(math.radians(th))
    A1 = (Pp[0] + c * L, Pp[1])
    T1 = (A1[0], A1[1] + s_ * L)
    A2 = (Pp[0], Pp[1] + c * L)
    T2 = (A2[0] - s_ * L, A2[1])
    triangle(sc, [Pp, A1, T1], ORANGE, 0.20)
    triangle(sc, [Pp, A2, T2], ORANGE, 0.20)
    sc.vec(Pp, (Pp[0] + L, Pp[1]), hn, "EDGE", 2.6, name_off=(8, 18), size=16, head=10)
    sc.vec(Pp, (Pp[0], Pp[1] + L), vn, "EDGE", 2.6, name_off=(-12, 4), size=16, head=10)
    sc.vec(Pp, T1, n1, "BLUE", 3.4, name_off=e1_lab, size=18, head=12)
    sc.vec(Pp, T2, n2, "BLUE", 3.4, name_off=e2_lab, size=18, head=12)
    sc.arc(Pp, 0.55, 0, th, "GREEN", 1.6, head=True)
    sc.label(_add(Pp, _d(th / 2), 0.9), tn, "GREEN", "middle", 15, dx=2, dy=5)
    sc.arc(Pp, 0.55, 90, 90 + th, "GREEN", 1.6, head=True)
    sc.label(_add(Pp, _d(90 + th / 2), 0.9), tn, "GREEN", "middle", 15, dx=-2, dy=5)
    sc.label(((Pp[0] + A1[0]) / 2, Pp[1]), cs, "HEAD", "middle", 14, dy=18)
    sc.label((A1[0], (A1[1] + T1[1]) / 2), sn, "HEAD", "start", 14, dx=8, dy=5)
    sc.label((Pp[0], Pp[1] + c * L * 0.84), cs, "HEAD", "start", 14, dx=8, dy=5)
    sc.label(((A2[0] + T2[0]) / 2, A2[1]), minus, "HEAD", "middle", 14, dy=-8)
    return A1, T1, A2, T2


@figure("t1-cylindrical-plan",
        r"Plan view of cylindrical coordinates with the angle theta between i and e_R and between j and e_theta, the projection triangles and the change of basis matrix.",
        r"Plan view with $\mathbf k$ out of the paper: $\mathbf e_\theta$ leans towards $-\mathbf i$, which puts the minus sign in entry $(1,2)$ of $[{}_0R_{\mathrm{cyl}}]$, the simple rotation of Eq. 1.20.")
def cylindrical_plan():
    sc = Scene(960, 500, (95, 420), 92)
    O = (0.0, 0.0)
    TH, R, L = 35.0, 3.3, 1.5
    c, s_ = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    Pp = (R * c, R * s_)
    F = (Pp[0], 0.0)
    fixed_axis(sc, O, 0, 4.9, "Ox", off=(18, 6))
    fixed_axis(sc, O, 90, 3.7, "Oy", off=(16, 4))
    sc.vec(O, (1, 0), bold("i"), "HEAD", 3.0, name_off=(0, 22), size=17, head=11)
    sc.vec(O, (0, 1), bold("j"), "HEAD", 3.0, name_off=(-14, 4), size=17, head=11)
    axis_out(sc, O, bold("k") + " ≡ " + bold("e") + S("", "z"), "HEAD", off=(-34, 28))
    triangle(sc, [O, F, Pp], ORANGE, 0.16)
    sc.dashed(F, Pp)
    right_angle(sc, F, 180, 90, 0.14)
    sc.line(O, Pp, ORANGE, 2.0)
    sc.label((Pp[0] / 2, Pp[1] / 2), "R", "ACC", "middle", 18, dx=-14, dy=-8, weight="700")
    sc.arc(O, 1.1, 0, TH, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d(TH / 2), 1.5), "θ", "GREEN", "middle", 17, dx=4, dy=6)
    sc.label((F[0] / 2, 0), "x = R cos θ (adjacent)", "HEAD", "middle", 15, dx=40, dy=44)
    sc.label((F[0], F[1] + Pp[1] / 2), "y = R sin θ (opposite)", "HEAD", "start", 15, dx=12, dy=5)
    _rot_pair(sc, Pp, TH, L, _vb("e", "R"), _vb("e", "θ"), bold("i"), bold("j"), "−sin θ i")
    sc.dotp(Pp, 4.2, "ACC")
    sc.label(Pp, "P′", "HEAD", "end", 17, dx=-14, dy=34)
    sc.dotp(O, 2.0, "HEAD")
    _matrix(sc, 590, 90, _title_R("cyl"),
            [["cos θ", MINUS + "sin θ", "0"], ["sin θ", "cos θ", "0"], ["0", "0", "1"]], cw=82)
    return sc


# --------------------------------------------------------------------------------------------------------------------
PHI_LAT = "ϕ"
PHI_COL = "φ"


def _sph(r, th, ph):
    t, p = math.radians(th), math.radians(ph)
    return (r * math.cos(p) * math.cos(t), r * math.cos(p) * math.sin(t), r * math.sin(p))


@figure("t1-spherical-3d",
        r"Spherical coordinates r, theta and the latitude phi of a point, the colatitude marked from the z axis, and the local basis at the point.",
        r"Spherical coordinates $\{r,\theta,\phi\}$, with the latitude $\phi$ measured from the plane $Oxy$ and the colatitude $\varphi$ from $Oz$, and the local basis $\{\mathbf e_r,\mathbf e_\theta,\mathbf e_\phi\}$ (Notes.pdf Fig. 2.5).")
def spherical_3d():
    sc = Scene(820, 620, (210, 475), 92)
    O = (0.0, 0.0, 0.0)
    r, TH, PH = 3.0, 40.0, 35.0
    t, p = math.radians(TH), math.radians(PH)
    P = _sph(r, TH, PH)
    Pp = _sph(r * math.cos(p), TH, 0.0)
    uR = (math.cos(t), math.sin(t), 0.0)
    er = _sph(1.0, TH, PH)
    et = (-math.sin(t), math.cos(t), 0.0)
    ep = (-math.sin(p) * math.cos(t), -math.sin(p) * math.sin(t), math.cos(p))
    # faint sphere arcs of radius r: the meridian through P and the equator
    _circ3(sc, O, uR, (0, 0, 1), r, -6, 90, "EDGE", head=False, w=1.1, dash="5 4")
    _circ3(sc, O, (1, 0, 0), (0, 1, 0), r, 0, 90, "EDGE", head=False, w=1.1, dash="5 4")
    _axes3(sc, O, (3.5, 3.9, 3.9), ("x", "y", "z"), ((-10, 14), (14, 6), (-4, -10)))
    _unit_frame(sc, O, 1.0, offs=((-12, 14), (4, 22), (-14, 4)))
    _line3(sc, O, Pp, "EDGE", 1.4, "6 4")
    _line3(sc, Pp, P, "EDGE", 1.4, "6 4")
    mid = _arc3(sc, (1, 0, 0), uR, 0.9, "GREEN")
    sc.label(mid, "θ", "GREEN", "middle", 17, dx=8, dy=20)
    mid2 = _arc3(sc, uR, er, 1.5, "GREEN")
    sc.label(mid2, PHI_LAT, "GREEN", "middle", 17, dx=6, dy=22)
    # colatitude: faint dashed green arc from Oz down to OP
    pts = []
    for i in range(41):
        a = math.radians(90.0 - (90.0 - PH) * i / 40)
        pts.append(P3(_v3(_mul(uR, 2.1 * math.cos(a)), _mul((0, 0, 1), 2.1 * math.sin(a)))))
    sc.poly(pts, "GREEN", 1.4, "4 3")
    sc.label(pts[0], PHI_COL + " = π/2 − " + PHI_LAT + " (colatitude)", "GREEN", "end", 15, dx=-12, dy=4, italic=False)
    _vec3(sc, O, P, None, ORANGE, 3.0, head=11)
    sc.label(P3(_mul(P, 0.45)), "r", "ACC", "end", 19, dx=-14, dy=-4, weight="700")
    L = 1.2
    _vec3(sc, P, _mul(er, L), _vb("e", "r"), "BLUE", 3.4, off=(14, 4), size=18, head=11)
    _vec3(sc, P, _mul(et, L), _vb("e", "θ"), "BLUE", 3.4, off=(22, 6), size=18, head=11)
    _vec3(sc, P, _mul(ep, L), _vb("e", "ϕ"), "BLUE", 3.4, off=(-20, -4), size=18, head=11)
    sc.dotp(P3(P), 4.6, "ACC")
    sc.label(P3(P), "P", "HEAD", "start", 18, dx=10, dy=22)
    sc.dotp(P3(Pp), 3.6)
    sc.label(P3(Pp), "P′", "HEAD", "start", 17, dx=10, dy=16)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=-6)
    return sc


@figure("t1-spherical-meridian",
        r"Meridian section of spherical coordinates with the right triangle of the point, the unit vectors e_r and e_phi with their projection triangles and the rotation matrix.",
        r"Meridian view with $\mathbf e_\theta$ into the paper: the latitude turns counterclockwise, a rotation by $-\phi$ about $\mathbf e_\theta$; $\mathbf e_\phi$ leans towards $-\mathbf e_R$, the minus sign of entry $(1,3)$.")
def spherical_meridian():
    sc = Scene(1060, 520, (190, 450), 100)
    O = (0.0, 0.0)
    r, PH, L = 3.4, 35.0, 1.5
    c, s_ = math.cos(math.radians(PH)), math.sin(math.radians(PH))
    P = (r * c, r * s_)
    Pp = (P[0], 0.0)
    fixed_axis(sc, O, 0, 4.5, "", off=(18, 6))
    sc.label((4.5, 0), "OP′ (direction " + _vb("e", "R") + ")", "TEXT", "end", 15, dx=-6, dy=-12, italic=False)
    fixed_axis(sc, O, 90, 3.6, "Oz", off=(16, 4))
    axis_in(sc, O, _vb("e", "θ") + " into the paper", "HEAD", off=(-72, 28))
    triangle(sc, [O, Pp, P], ORANGE, 0.16)
    sc.dashed(Pp, P)
    right_angle(sc, Pp, 180, 90, 0.14)
    sc.line(O, P, ORANGE, 2.0)
    sc.label((P[0] * 0.78, P[1] * 0.78), "r", "ACC", "middle", 18, dx=10, dy=24, weight="700")
    sc.arc(O, 1.0, 0, PH, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d(PH / 2), 1.4), PHI_LAT, "GREEN", "middle", 17, dx=4, dy=6)
    sc.arc(O, 1.7, 90, PH, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d((90 + PH) / 2), 2.1), PHI_COL, "GREEN", "middle", 17, dy=5)
    sc.label((P[0] / 2, 0), "r cos " + PHI_LAT + " (adjacent, the cylindrical radius R)", "HEAD", "middle", 15, dy=26)
    sc.label((P[0], P[1] / 2), "z = r sin " + PHI_LAT + " (opposite)", "HEAD", "start", 15, dx=12, dy=5)
    sc.label(Pp, "P′", "HEAD", "start", 17, dx=8, dy=-8)
    ph_s, ph_c = "sin " + PHI_LAT, "cos " + PHI_LAT
    # unit vectors at P: rotated by phi from (e_R, k)
    c_, s2 = math.cos(math.radians(PH)), math.sin(math.radians(PH))
    A1 = (P[0] + c_ * L, P[1])
    T1 = (A1[0], A1[1] + s2 * L)
    A2 = (P[0], P[1] + c_ * L)
    T2 = (A2[0] - s2 * L, A2[1])
    _rot_pair(sc, P, PH, L, _vb("e", "r"), _vb("e", "ϕ"), _vb("e", "R"), bold("k"), "−sin " + PHI_LAT + " " + _vb("e", "R"),
              cs=ph_c, sn=ph_s, tn=PHI_LAT, e1_lab=(24, -4), e2_lab=(-26, -8))
    sc.dotp(P, 4.4, "ACC")
    sc.label(P, "P", "HEAD", "end", 18, dx=-6, dy=36)
    sc.dotp(O, 2.0, "HEAD")
    _matrix(sc, 700, 200, "[" + S("", "cyl") + "R" + S("", "sph") + "]",
            [[ph_c, "0", MINUS + ph_s], ["0", "1", "0"], [ph_s, "0", ph_c]], cw=78)
    _pl(sc, 700 + 128, 200 + 150, "rotation by " + MINUS + PHI_LAT + " about " + _vb("e", "θ"), "TEXT", "middle", 14)
    return sc


@figure("t1-spherical-plan",
        r"Plan view of spherical coordinates with the horizontal projection r cos phi, its right triangle and the spherical change of basis matrix.",
        r"Plan view: the horizontal projection $r\cos\phi$ is split by $\theta$ into $x$ and $y$; the composed matrix $[{}_0R_{\mathrm{sph}}]$ has $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf e_\phi$ as columns.")
def spherical_plan():
    sc = Scene(1000, 500, (95, 420), 92)
    O = (0.0, 0.0)
    TH, Rh, L = 40.0, 3.3, 1.5
    c, s_ = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    Pp = (Rh * c, Rh * s_)
    F = (Pp[0], 0.0)
    fixed_axis(sc, O, 0, 4.9, "Ox", off=(18, 6))
    fixed_axis(sc, O, 90, 4.1, "Oy", off=(16, 4))
    sc.vec(O, (1, 0), bold("i"), "HEAD", 3.0, name_off=(0, 22), size=17, head=11)
    sc.vec(O, (0, 1), bold("j"), "HEAD", 3.0, name_off=(-14, 4), size=17, head=11)
    axis_out(sc, O, bold("k"), "HEAD", off=(-20, 28))
    triangle(sc, [O, F, Pp], ORANGE, 0.16)
    sc.dashed(F, Pp)
    right_angle(sc, F, 180, 90, 0.14)
    sc.line(O, Pp, ORANGE, 2.0)
    sc.label((Pp[0] / 2, Pp[1] / 2), "r cos " + PHI_LAT, "ACC", "middle", 18, dx=-34, dy=-10, weight="700")
    sc.arc(O, 1.1, 0, TH, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d(TH / 2), 1.5), "θ", "GREEN", "middle", 17, dx=4, dy=6)
    sc.label((F[0] / 2, 0), "x = r cos " + PHI_LAT + " cos θ (adjacent)", "HEAD", "middle", 15, dx=40, dy=44)
    sc.label((F[0], Pp[1] / 2), "y = r cos " + PHI_LAT + " sin θ (opposite)", "HEAD", "start", 15, dx=12, dy=5)
    # at P': e_R (horizontal part of e_r and -e_phi) and e_theta, with the copy of j
    sc.vec(Pp, (Pp[0], Pp[1] + L), bold("j"), "EDGE", 2.6, name_off=(-12, 4), size=16, head=10)
    eR = (Pp[0] + L * c, Pp[1] + L * s_)
    eT = (Pp[0] - L * s_, Pp[1] + L * c)
    sc.line(Pp, eR, "BLUE", 3.2, "7 4")
    arrow_head(sc.c, sc.P(Pp), sc.P(eR), "BLUE", 12)
    sc.label(eR, _vb("e", "R") + ", horizontal part of " + _vb("e", "r") + " and " + MINUS + _vb("e", "ϕ"), "BLUE", "start", 15,
             dx=12, dy=-2, italic=False)
    sc.vec(Pp, eT, _vb("e", "θ"), "BLUE", 3.4, name_off=(-26, -8), size=18, head=12)
    sc.arc(Pp, 0.7, 90, 90 + TH, "GREEN", 1.6, head=True)
    sc.label(_add(Pp, _d(90 + TH / 2), 1.05), "θ", "GREEN", "middle", 15, dx=-4, dy=5)
    sc.dotp(Pp, 4.2, "ACC")
    sc.label(Pp, "P′", "HEAD", "start", 17, dx=8, dy=22)
    sc.dotp(O, 2.0, "HEAD")
    cp, sp, ct, st = "cos " + PHI_LAT, "sin " + PHI_LAT, "cos θ", "sin θ"
    _matrix(sc, 600, 250, "[" + S("", "0") + "R" + S("", "sph") + "] = [" + S("", "0") + "R" + S("", "cyl") + "] [" +
            S("", "cyl") + "R" + S("", "sph") + "]",
            [[cp + " " + ct, MINUS + st, MINUS + sp + " " + ct], [cp + " " + st, ct, MINUS + sp + " " + st],
             [sp, "0", cp]], cw=108, size=15)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _subs(s):
    return S("", s)


@figure("t1-constraints",
        r"A particle on a sphere with two angular coordinates, a bead on a circular wire with one angle, and two blocks joined by a string over a pulley.",
        r"Constraints reduce the coordinates: on a sphere $3 - 1 = 2$, on a circular wire $3 - 2 = 1$, and the string over a pulley ties the two depths, $\dot d_2 = -\dot d_1$ (Notes.pdf Sec. 2.7).")
def constraints():
    sc = Scene(1080, 450, (125, 290), 58)
    # ---- panel 1: particle on a sphere ---------------------------------------------------------------------------------
    O = (0.0, 0.0, 0.0)
    R0, TH, PH = 1.6, 40.0, 35.0
    t, p = math.radians(TH), math.radians(PH)
    sc.note((-1.4, 4.3), "particle on a sphere,", "TEXT", "start", 14)
    sc.note((-1.4, 3.9), "2 degrees of freedom", "TEXT", "start", 14)
    out = _ellipse_outline(R0)
    sc.poly(out, "EDGE", 1.6, None, "HEAD", True, 0.07)
    uR = (math.cos(t), math.sin(t), 0.0)
    _circ3(sc, O, (1, 0, 0), (0, 1, 0), R0, 0, 360, "EDGE", head=False, w=1.1, dash="5 4", n=90)
    _circ3(sc, O, uR, (0, 0, 1), R0, -90, 90, "EDGE", head=False, w=1.1, dash="5 4")
    _axes3(sc, O, (2.5, 2.9, 2.6), ("x", "y", "z"), ((-10, 14), (14, 6), (-4, -10)))
    P = _sph(R0, TH, PH)
    Pp = _sph(R0 * math.cos(p), TH, 0.0)
    er = _sph(1.0, TH, PH)
    et = (-math.sin(t), math.cos(t), 0.0)
    ep = (-math.sin(p) * math.cos(t), -math.sin(p) * math.sin(t), math.cos(p))
    _line3(sc, O, Pp, "EDGE", 1.3, "6 4")
    _line3(sc, Pp, P, "EDGE", 1.3, "6 4")
    sc.line(P3(O), P3(P), "HEAD", 1.6)
    mid = _arc3(sc, (1, 0, 0), uR, 0.6, "GREEN")
    sc.label(mid, "θ", "GREEN", "middle", 16, dx=6, dy=20)
    mid2 = _arc3(sc, uR, er, 0.95, "GREEN")
    sc.label(mid2, PHI_LAT, "GREEN", "middle", 16, dx=10, dy=18)
    sc.label((0.2, -2.25), "r = R" + _subs("0"), "HEAD", "middle", 16)
    _vec3(sc, P, _mul(et, 0.95), _vb("e", "θ"), "BLUE", 3.2, off=(20, 4), size=17, head=10)
    _vec3(sc, P, _mul(ep, 0.95), _vb("e", "ϕ"), "BLUE", 3.2, off=(24, -2), size=17, head=10)
    sc.dotp(P3(P), 4.6, "ACC")
    sc.label(P3(P), "P", "HEAD", "start", 17, dx=12, dy=24)
    sc.dotp(P3(O), 3.2)
    sc.label(P3(O), "O", "HEAD", "end", 16, dx=-8, dy=-6)
    # ---- panel 2: bead on a circular wire --------------------------------------------------------------------------------
    C = (7.5, 0.9)
    TH2 = 50.0
    sc.note((5.3, 4.3), "bead on a circular wire,", "TEXT", "start", 14)
    sc.note((5.3, 3.9), "1 degree of freedom", "TEXT", "start", 14)
    sc.circle(C, R0, "EDGE", 3.6)
    fixed_axis(sc, C, 0, R0 + 0.7, "Ox", off=(16, 6))
    fixed_axis(sc, C, 90, R0 + 0.7, "Oy", off=(16, 4))
    Pb = _add(C, _d(TH2), R0)
    sc.dashed(C, Pb)
    sc.arc(C, 0.65, 0, TH2, "GREEN", 1.7, head=True)
    sc.label(_add(C, _d(TH2 / 2), 0.95), "θ", "GREEN", "middle", 16, dx=4, dy=6)
    sc.vec(Pb, _add(Pb, _d(TH2 + 90), 0.95), _vb("e", "θ"), "BLUE", 3.2, name_off=(-20, -4), size=17, head=10)
    axis_out(sc, C, bold("k"), "HEAD", off=(-14, 26))
    sc.mass(Pb, None, r=7.0)
    sc.label(Pb, "P", "HEAD", "start", 17, dx=12, dy=14)
    sc.label((C[0], C[1] - R0 - 0.4), "z = 0,  R = R" + _subs("0"), "HEAD", "middle", 16, italic=False)
    # ---- panel 3: two particles and a string over a pulley ----------------------------------------------------------------
    PC = (12.9, 2.4)
    rp = 0.7
    sc.note((11.0, 4.3), "two particles and a string,", "TEXT", "start", 14)
    sc.note((11.0, 3.9), "1 degree of freedom", "TEXT", "start", 14)
    ceil_y = PC[1] + 1.3
    sc.ground((PC[0] - 1.0, ceil_y), (PC[0] + 1.0, ceil_y), side=1, step=9, length=9)
    sc.line((PC[0] - 0.45, ceil_y), PC, "HEAD", 1.8)
    sc.line((PC[0] + 0.45, ceil_y), PC, "HEAD", 1.8)
    sc.disk(PC, rp, "HEAD", "HEAD", 0.10, 2.0)
    sc.pin(PC, 5.0)
    x1, x2 = PC[0] - rp, PC[0] + rp
    h1, h2 = 2.5, 1.2
    b = 0.28
    y1, y2 = PC[1] - h1, PC[1] - h2
    sc.line((x1, PC[1]), (x1, y1 + b), "HEAD", 1.6)
    sc.line((x2, PC[1]), (x2, y2 + b), "HEAD", 1.6)
    sc.arc(PC, rp, 0, 180, ORANGE, 3.8)
    sc.label(_add(PC, _d(45), rp + 0.42), "L" + _subs("0"), "ACC", "start", 17, dx=4, dy=-2, weight="700")
    for xx, yy, nm in ((x1, y1, "1"), (x2, y2, "2")):
        sc.poly([(xx - b, yy + b), (xx + b, yy + b), (xx + b, yy - b), (xx - b, yy - b)], "HEAD", 1.8, None, "ACC", True, 0.55)
    sc.line((PC[0] - 2.3, PC[1]), (PC[0] + 2.3, PC[1]), "EDGE", 1.1, "7 4")
    xd1, xd2 = PC[0] - 1.9, PC[0] + 1.9
    sc.dim((xd1, PC[1]), (xd1, y1), "d" + _subs("1"), off=(-16, 4))
    sc.dim((xd2, PC[1]), (xd2, y2), "d" + _subs("2"), off=(16, 4))
    sc.line((x1 - b, y1), (xd1, y1), "EDGE", 1.1, "7 4")
    sc.line((x2 + b, y2), (xd2, y2), "EDGE", 1.1, "7 4")
    # equal and opposite displacements
    ya = (y1 + y2) / 2
    sc.vec((PC[0] - 0.2, y1 + 0.35), (PC[0] - 0.2, y1 - 0.35), None, "BLUE", 3.0, head=10)
    sc.vec((PC[0] + 0.2, y2 - 0.35), (PC[0] + 0.2, y2 + 0.35), None, "BLUE", 3.0, head=10)
    sc.note((PC[0] - 1.9, y1 - 0.75), "equal and opposite displacements", "TEXT", "start", 13)
    return sc


# --------------------------------------------------------------------------------------------------------------------
HX_A, HX_W, HX_VZ = 1.0, 1.0, 0.6
ZF = 0.45         # the vertical axis is drawn compressed by this factor so that 1.5 turns fit the sheet (linear map)


def _zv(v):
    return (v[0], v[1], ZF * v[2])


def _helix(t):
    return (HX_A * math.cos(HX_W * t), HX_A * math.sin(HX_W * t), HX_VZ * t)


@figure("t1-helix",
        r"A helix on a cylinder about the z axis with the intrinsic basis at its starting point and the centre of curvature on the far side of the axis.",
        r"Helical trajectory of the rocket: at $(a,0,0)$ the normal $\mathbf e_n = -\mathbf e_R$ points to the axis and the centre of curvature lies beyond it, at $x = -v_z^2/(a\omega^2)$ ([Lecture 1, Slide 29]).")
def helix():
    sc = Scene(940, 810, (345, 640), 185)
    O = (0.0, 0.0, 0.0)
    a, w, vz = HX_A, HX_W, HX_VZ
    tmax = 3 * math.pi
    zmax = ZF * vz * tmax
    _cylinder3(sc, a, 0.0, zmax + 0.15)
    _axes3(sc, O, (1.8, 2.4, zmax + 0.5), ("x", "y", "z"), ((-10, 14), (14, 6), (-4, -10)))
    sc.poly([P3(_zv(_helix(tmax * i / 300))) for i in range(301)], TRAJ, 2.8)
    P0 = _helix(0.0)
    # pitch: between two successive crossings of the generator at the right silhouette of the cylinder
    pitch = 2 * math.pi * vz / w
    tS = math.atan2(1.0, EX_X)
    S0, S1 = _zv(_helix(tS)), _zv(_helix(tS + 2 * math.pi))
    p0, p1 = P3(S0), P3(S1)
    dxs = 0.42
    _line3(sc, S0, S1, "EDGE", 1.1, "5 4")
    sc.line(p0, (p0[0] + dxs, p0[1]), "EDGE", 1.0, "3 3")
    sc.line(p1, (p1[0] + dxs, p1[1]), "EDGE", 1.0, "3 3")
    sc.dim((p0[0] + dxs, p0[1]), (p1[0] + dxs, p1[1]), "2π v" + S("", "z") + "/ω", off=(52, 4))
    sc.dotp(p0, 3.6, TRAJ)
    sc.dotp(p1, 3.6, TRAJ)
    # a later point of the helix and the angle theta in the plane Oxy
    t1 = 2 * math.pi + 1.3
    H1 = _zv(_helix(t1))
    H1p = (H1[0], H1[1], 0.0)
    _line3(sc, O, H1p, "EDGE", 1.3, "6 4")
    _line3(sc, H1p, H1, "EDGE", 1.1, "3 3")
    mid = _arc3(sc, (1, 0, 0), _unit3(H1p), 0.3, "GREEN", head=True)
    sc.label(mid, "θ", "GREEN", "middle", 17, dx=30, dy=2)
    sc.dotp(P3(H1), 3.8, TRAJ)
    # centre of curvature C on the negative x axis, rho = a + v_z^2 /(a w^2)
    xc = -vz * vz / (a * w * w)
    C = (xc, 0.0, 0.0)
    _line3(sc, P0, C, "ACC", 1.5, "6 4")
    # intrinsic triad at P0 (orange) and cylindrical basis (blue)
    n = math.sqrt(a * a * w * w + vz * vz)
    et = _zv((0.0, a * w / n, vz / n))
    eb = _zv((0.0, -vz / n, a * w / n))
    en = (-1.0, 0.0, 0.0)
    L = 0.72
    _vec3(sc, P0, _mul(et, L), _vb("e", "t"), ORANGE, 3.6, off=(20, 6), size=18, head=11)
    _vec3(sc, P0, _mul(eb, L), _vb("e", "b"), ORANGE, 3.6, off=(-16, -6), size=18, head=11)
    _vec3(sc, P0, _mul(en, 0.5), _vb("e", "n"), ORANGE, 3.6, off=(-8, -16), size=18, head=11)
    _vec3(sc, P0, _mul((1, 0, 0), 0.5), _vb("e", "R"), "BLUE", 3.2, off=(-14, 18), size=17, head=10)
    _vec3(sc, P0, (0, 0, ZF * L), _vb("e", "z"), "BLUE", 3.2, off=(-4, -14), size=17, head=10)
    sc.dotp(P3(P0), 4.8, TRAJ)
    sc.label(P3(P0), "(a, 0, 0),  t = 0", "HEAD", "start", 16, dx=22, dy=34, italic=False)
    sc.dotp(P3(C), 4.2, "HEAD")
    sc.label(P3(C), "C", "HEAD", "start", 17, dx=12, dy=2)
    sc.label(P3(_mul(_v3(P0, C), 0.5)), "ρ", "ACC", "start", 18, dx=12, dy=12, weight="700")
    # distance O to C, dimensioned below the x axis
    off = (0.22, 0.40)
    pO, pC = P3(O), P3(C)
    sc.line(pO, (pO[0] + off[0], pO[1] + off[1]), "EDGE", 1.0, "3 3")
    sc.line(pC, (pC[0] + off[0], pC[1] + off[1]), "EDGE", 1.0, "3 3")
    sc.dim((pO[0] + off[0], pO[1] + off[1]), (pC[0] + off[0], pC[1] + off[1]), "v" + S("", "z") + "²/(a ω²)", off=(66, -2))
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-10, dy=-6)
    return sc
