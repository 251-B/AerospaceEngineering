"""Theory figures of Topic 3 (Constraints and Reaction Forces): Chapters 6 and 7 of Notes.pdf and Lecture 3.

Colour code of the topic (same helpers and axonometric projection as t1.py and t1b.py): fixed axes and basis grey,
moving or polar bases blue, auxiliary vectors (velocity, tangents, normals, projections) orange, angles green, forces
pink, constraint surfaces light grey with a thin dark outline, curves and trajectories dark red.
"""
import math

from figures.em_theory import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.em_th.t1 import (DRED, ORANGE, P3, _add, _cross, _d, _dot, _matrix, _mul, _pl, _unit3, _v3, dot1)
from figures.em_th.t1b import _ellipse_outline, _triad, _vb
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head, circle as _circle, line as _line, rect as _rect, poly as _poly

TEXT = {
    't3-constraints': (
        'A particle moving on a curved surface and a bead moving along a looped wire, each with its velocity tangent to the constraint.',
        'Simple constraints on a single particle: a stationary surface (two degrees of freedom) and a stationary curve (one degree of freedom) ([Lecture 3, Slide 3]).'),
    't3-curve-surface-forms': (
        'Four sketches: a surface in implicit form, a curve as the intersection of two surfaces, a curve with one parameter and a surface gridded by two parameters.',
        'Surfaces and curves in implicit form (one or two equations) and in parametric form (two or one parameters) (Notes.pdf, Sec. 6.1; [Lecture 3, Slide 5]).'),
    't3-coordinate-choices': (
        'A particle held by a string on a sphere about a fixed point with its two spherical angles, and a particle on a cone with its azimuth and its distance to the vertex shown in the meridian triangle.',
        'Coordinates adapted to the constraint: the spherical angles $\\theta$, $\\varphi$ on the sphere of radius $\\ell$ about $A$, and the azimuth $\\theta$ with the distance $\\ell_V$ to the vertex on a cone of half-angle $\\gamma$ (Notes.pdf, Sec. 6.2).'),
    't3-surface-normal': (
        'A curved surface with a tangent plane at a point, two non-orthogonal tangent vectors along the coordinate lines and the normal gradient vector.',
        'At a point of a surface, $\\mathbf t_\\alpha$ and $\\mathbf t_\\beta$ span the tangent subspace $V_T$ and the gradient $\\nabla f$, parallel to $\\mathbf t_\\alpha\\times\\mathbf t_\\beta$, spans the normal subspace $V_N$ (Notes.pdf, Sec. 6.3; [Lecture 3, Slides 7 and 9]).'),
    't3-curve-normals': (
        'A curve as the intersection of two surfaces, with the two surface normals spanning the normal plane at a point and the tangent along the curve.',
        'A curve given as the intersection of two surfaces: the gradients $\\mathbf n_f$ and $\\mathbf n_h$ span its normal plane $V_N$ and their cross product gives the tangent $\\mathbf t$ (Notes.pdf, Sec. 6.3; [Lecture 3, Slide 10]).'),
    't3-ellipse-vectors': (
        'An ellipse in a plane with a point on it, the tangent vector along the ellipse, the in-plane normal pointing outwards, and the second normal out of the paper.',
        'Tangent $\\mathbf t$ and normals $\\mathbf n_f$ (in the plane) and $\\mathbf n_h = \\mathbf k$ (out of the paper) of the ellipse of [Lecture 3, Slide 11].'),
    't3-paraboloid-vectors': (
        'A paraboloid with a point on it, the meridian and parallel tangent vectors and the outward-downward normal, with the cross product of the tangents pointing the opposite way.',
        'Tangent vectors $\\mathbf t_R$, $\\mathbf t_\\theta$ and normal $\\mathbf n = \\nabla f$ of the paraboloid of [Lecture 3, Slide 12]; $\\mathbf t_R\\times\\mathbf t_\\theta$ is parallel to $\\mathbf n$, here with the opposite sense.'),
    't3-surface-reaction': (
        'A particle on a surface with the normal reaction perpendicular to the surface and the velocity tangent to it, at right angles.',
        'The reaction of a smooth stationary surface is normal to it and the velocity is tangent to it, so the reaction does no work (Notes.pdf, Sec. 6.4; [Lecture 3, Slides 13 and 16]).'),
    't3-spool': (
        'A particle hanging from a string that is wound up by a spool at the origin, with the weight, the tension and the upward velocity.',
        'The string collected at the rate $c$ imposes $\\zeta = \\ell_0 - c\\,t$: a time-dependent constraint whose tension $F_T = m g$ works at the rate $m g\\,c$ ([Lecture 3, Slide 22]).'),
    't3-airplane-fbd': (
        'An airplane on a runway with its weight down, the lift and the normal reaction of the ground up, and its velocity along the runway.',
        'On the runway the ground pushes with $N = m g - L$; the airplane lifts off when $N$ reaches zero ([Lecture 3, Slide 23]).'),
    't3-curve-reaction': (
        'A wire with the tangent, normal and binormal unit vectors at a point and the reaction lying in the normal plane with its two components.',
        'The reaction of a smooth curve lies in its normal plane, $\\mathbf N = N_n\\,\\mathbf e_n + N_b\\,\\mathbf e_b$, so the tangential projection of the second law is free of it (Notes.pdf, Eqs. 6.14 to 6.19; [Lecture 3, Slide 13]).'),
    't3-vertical-circle': (
        'A vertical circle centred at the origin with a particle on it at an angle theta from the horizontal axis and gravity pointing down.',
        'A heavy particle on a smooth vertical circle of radius $a$; its position is given by the angle $\\theta$ from $Ox$ ([Lecture 3, Slide 15]).'),
    't3-vertical-circle-basis': (
        'The fixed and the polar unit vectors at the centre, rotated by theta about the axis out of the paper, with the two right triangles that give their components and the rotation matrix.',
        'The polar basis $\\mathbf e_R$, $\\mathbf e_\\theta$ is $\\mathbf i$, $\\mathbf j$ rotated by $\\theta$ about $\\mathbf k$ (⊙); the leg of $\\mathbf e_\\theta$ along $-\\mathbf i$ is the minus sign of $[{}_0R_1]$.'),
    't3-vertical-circle-fbd': (
        'The particle on the circle with its weight split into radial and tangential components and the reaction of the wire along the radius and out of the plane.',
        'Free-body diagram on the vertical circle: weight $\\mathbf F_g$ and reaction $\\mathbf N = N_R\\,\\mathbf e_R + N_z\\,\\mathbf k$ in the normal plane of the wire.'),
    't3-two-particles': (
        'Two particles hanging from a string over two pulleys, each with its weight and the equal tension of the string, one moving down and the other up.',
        'Two particles joined by a string over two pulleys: one coordinate $d$, the same tension $F_T$ on both, and equal and opposite powers of the string (built for this note on [Lecture 3, Slide 17]).'),
    't3-friction': (
        'Two sketches of a particle on a rough surface: sliding, with friction opposite to the relative velocity and the total reaction on the edge of the friction cone, and sticking, with the total reaction inside the cone.',
        'Coulomb friction: while sliding it is opposite to the relative velocity with magnitude $\\mu\\lvert\\mathbf N\\rvert$; while sticking it is any tangential force within the bound $\\lvert\\mathbf F_R\\rvert \\leq \\mu\\lvert\\mathbf N\\rvert$ (Notes.pdf, Eqs. 6.20 and 6.21; [Lecture 3, Slide 18]).'),
    't3-rough-cylinder': (
        'A particle sliding on a rough cylinder along a helix, with the cylindrical basis, the inward normal reaction and the friction opposite to the velocity, and a top view with the angle theta.',
        'The particle on the rough cylinder of [Lecture 3, Slide 20]: $\\mathbf r_0^P = a\\,\\mathbf e_R + z\\,\\mathbf k$, normal reaction along $\\mathbf e_R$ and friction opposite to the velocity, which keeps a constant angle $\\psi$ with the horizontal.'),
    't3-simple-rotation': (
        'Two sets of axes with a common origin, one rotated by theta about the axis out of the paper, with the right triangles that give the components of the rotated unit vectors and the matrix.',
        'Eq. 7.1: $S_2$ is $S_1$ rotated by $\\theta$ about $\\mathbf k_1$ (⊙); the leg of $\\mathbf j_2$ along $-\\mathbf i_1$ gives the minus sign (Notes.pdf, Sec. 7.3).'),
    't3-region-existence': (
        'The sine curve of the effective potential with three energy levels: one above it for revolutions, one crossing it with two turning angles for oscillations, and one at its minimum.',
        'Regions of existence on the vertical circle: the motion exists where $(g/a)\\sin\\theta \\leq K$; the roots of $\\sin\\theta_* = aK/g$ are the turning angles (Notes.pdf, Sec. 7.7).'),
}

def _fig(name):
    alt, cap = TEXT[name]
    return figure(name, alt, cap)


PINK = "PINK"
LBLUE = "BLUE"


# ---- axonometric helpers (3D points shifted by a 2D world offset `off`) --------------------------------------------
_PR = {"p": P3}


def _q(p, off=(0.0, 0.0)):
    x, y = _PR["p"](p)
    return (x + off[0], y + off[1])


def _sub3(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _norm3(v):
    return math.sqrt(_dot(v, v))


def _lin(*terms):
    """Linear combination of 3D vectors: _lin((k1, v1), (k2, v2), ...)."""
    return tuple(sum(k * v[i] for k, v in terms) for i in range(3))


def _V(sc, o, v, name=None, col="BLUE", w=2.6, off=(0.0, 0.0), lab=(8, -8), size=17, head=11, dash=None):
    """Arrow from the 3D point o along the 3D vector v; `dash` gives a dashed shaft."""
    a, b = _q(o, off), _q(_v3(o, v), off)
    if dash:
        pa, pb = sc.P(a), sc.P(b)
        ang = math.atan2(pb[1] - pa[1], pb[0] - pa[0])
        k = 0.6 * head / sc.k
        sc.line(a, (b[0] - k * math.cos(ang) * 1.0, b[1] + k * math.sin(ang) * 1.0), col, w, dash)
        arrow_head(sc.c, pa, pb, col, head)
        if name:
            sc.label(b, name, col, "middle", size, weight="700", dx=lab[0], dy=lab[1])
    else:
        sc.vec(a, b, name, col, w, name_off=lab, size=size, head=head)
    return b


def _L(sc, a, b, off=(0.0, 0.0), col="EDGE", w=1.1, dash="5 4"):
    sc.line(_q(a, off), _q(b, off), col, w, dash)


def _pts(sc, pts, off=(0.0, 0.0), col="HEAD", w=1.6, dash=None, fill="none", close=False, op=None):
    sc.poly([_q(p, off) for p in pts], col, w, dash, fill, close, op)


def _arc_at(sc, c, u, v, r, off=(0.0, 0.0), col="GREEN", head=True, w=1.7, n=28, flip=False):
    """Arc of radius r about the 3D point c, from the direction u to the direction v (head at v); returns its midpoint (2D)."""
    u, v = _unit3(u), _unit3(v)
    a = math.acos(max(-1.0, min(1.0, _dot(u, v))))
    pts = []
    for i in range(n + 1):
        t = i / n
        p = _lin((math.sin((1 - t) * a) * r / math.sin(a), u), (math.sin(t * a) * r / math.sin(a), v))
        pts.append(_q(_v3(c, p), off))
    sc.poly(pts, col, w)
    if head:
        arrow_head(sc.c, sc.P(pts[-3]), sc.P(pts[-1]), col, 9)
    return pts[n // 2]


def _dp(sc, p3, off=(0.0, 0.0), r=4.2, col="HEAD"):
    sc.dotp(_q(p3, off), r, col)


def _surface(sc, f, ur, vr, off=(0.0, 0.0), col="EDGE", op=0.20, ow=1.3, n=18, ocol="HEAD"):
    """Surface patch f(u, v) -> 3D point: translucent fill with a thin outline."""
    (u0, u1), (v0, v1) = ur, vr
    b = [f(u0 + (u1 - u0) * i / n, v0) for i in range(n + 1)]
    b += [f(u1, v0 + (v1 - v0) * i / n) for i in range(1, n + 1)]
    b += [f(u1 - (u1 - u0) * i / n, v1) for i in range(1, n + 1)]
    b += [f(u0, v1 - (v1 - v0) * i / n) for i in range(1, n)]
    _pts(sc, b, off, ocol, ow, None, col, True, op)


def _grid(sc, f, ur, vr, nu, nv, off=(0.0, 0.0), col="HEAD", w=1.0, dash="4 3", n=18, ucol=None, vcol=None):
    """Coordinate lines of a patch: nu lines of constant u (v sweeping) and nv lines of constant v."""
    (u0, u1), (v0, v1) = ur, vr
    for i in range(1, nu + 1):
        u = u0 + (u1 - u0) * i / (nu + 1)
        _pts(sc, [f(u, v0 + (v1 - v0) * j / n) for j in range(n + 1)], off, ucol or col, w, dash)
    for i in range(1, nv + 1):
        v = v0 + (v1 - v0) * i / (nv + 1)
        _pts(sc, [f(u0 + (u1 - u0) * j / n, v) for j in range(n + 1)], off, vcol or col, w, dash)


def _du(f, u, v, h=1e-4):
    a, b = f(u - h, v), f(u + h, v)
    return tuple((b[i] - a[i]) / (2 * h) for i in range(3))


def _dv(f, u, v, h=1e-4):
    a, b = f(u, v - h), f(u, v + h)
    return tuple((b[i] - a[i]) / (2 * h) for i in range(3))


def _right_mark3(sc, p, a, b, size=0.12, off=(0.0, 0.0), col="HEAD"):
    """Right-angle mark at the 3D point p between the 3D directions a and b."""
    a, b = _unit3(a), _unit3(b)
    p1, p2, p3 = _v3(p, a, size), _v3(_v3(p, a, size), b, size), _v3(p, b, size)
    sc.poly([_q(p1, off), _q(p2, off), _q(p3, off)], col, 1.2)


def _txt(sc, p2, s, col="HEAD", anchor="middle", size=16, dx=0, dy=0, italic=True, weight="400"):
    sc.label(p2, s, col, anchor, size, italic=italic, weight=weight, dx=dx, dy=dy)


def _spot(sc, p2, kind="out", r=8, col="HEAD"):
    """⊙ (out of the paper) or ⊗ (into the paper) at a 2D world point."""
    (axis_out if kind == "out" else axis_in)(sc, p2, None, col, r_px=r)


# --------------------------------------------------------------------------------------------------------------------
def _twist(u, v):
    return (u, v, 0.30 * math.sin(0.9 * v + 0.4) + 0.22 * u * (v - 1.6) * 0.55)


def _loop(t):
    """Wire with one loop (prolate trochoid), in the plane of the page with a little depth."""
    a, b = 0.46, 0.86
    return (0.2 * math.sin(t), a * t - b * math.sin(t), b * math.cos(t) * 0.9)


@_fig("t3-constraints")
def constraints():
    sc = Scene(800, 262, (400, 190), 80)
    # left panel: a surface patch
    off = (-3.6, 0.9)
    ur, vr = (0.0, 2.2), (0.0, 3.3)
    _surface(sc, _twist, ur, vr, off, "EDGE", 0.22, 1.5)
    P = (1.0, 1.55)
    _pts(sc, [_twist(0.15 + 1.7 * s, 0.4 + 2.4 * s) for s in [i / 30 for i in range(31)]], off, DRED, 1.4, "5 4")
    p3 = _twist(*P)
    t = _unit3(_v3(_du(_twist, *P), _dv(_twist, *P), 1.5))
    _V(sc, p3, _mul(t, 1.15), _vb("v", "0", "P"), ORANGE, 3.2, off, (4, -16), 18, 12)
    _dp(sc, p3, off, 5.2)
    _txt(sc, _q(p3, off), "P", "HEAD", "middle", 18, dx=-14, dy=18)
    _txt(sc, (off[0] + 1.1, off[1] - 1.6), "P on a surface", "HEAD", "middle", 18, italic=False)
    # right panel: a wire with one loop
    off = (2.6, 0.9)
    ts = [-3.4 + 6.8 * i / 160 for i in range(161)]
    _pts(sc, [_loop(t) for t in ts], off, DRED, 3.0)
    t0 = 0.12
    p3 = _loop(t0)
    h = 1e-4
    d = _unit3(_sub3(_loop(t0 + h), _loop(t0 - h)))
    _V(sc, p3, _mul(d, 0.95), _vb("v", "0", "P"), ORANGE, 3.2, off, (4, -16), 18, 12)
    _dp(sc, p3, off, 5.8)
    _txt(sc, _q(p3, off), "P", "HEAD", "middle", 18, dx=16, dy=-10)
    _txt(sc, (off[0] + 0.0, off[1] - 1.5), "P on a curve (bead on a wire)", "HEAD", "middle", 18, italic=False)
    return sc


# --------------------------------------------------------------------------------------------------------------------
XS = 2.6          # depth scale of the sketches: the x axis is short in the projection, so the patches are stretched along it


def _ga(u, v):
    return (XS * u, v, -0.7 * u + 0.33 * math.sin(1.3 * v + 0.3) + 0.22 * u * u + 0.1 * u)


def _cc(t):
    """Curve of the surface sketches: a space curve running to the right."""
    return (0.18 * math.sin(1.4 * t), t, 0.28 * math.cos(1.1 * t))


def _ruled(t, s, d, bend):
    """Surface through the curve _cc, swept along the direction d (with a small bending term)."""
    c = _cc(t)
    return (c[0] + s * d[0], c[1] + s * d[1], c[2] + s * d[2] + bend * s * s)


D1 = (2.4, 0.0, -0.6)
D2 = (-0.35, 0.0, 1.7)


def _two_surfaces(sc, off, c2="BLUE", op2=0.22, tr=(-1.5, 1.5), s1=(-0.55, 0.85), s2=(-0.45, 0.85), ow=1.3):
    """Two surface patches that intersect along the curve _cc; draws the grey patch, the coloured one and the curve."""
    f1 = lambda s, t: _ruled(t, s, D1, 0.08)
    f2 = lambda s, t: _ruled(t, s, D2, -0.10)
    _surface(sc, f1, s1, tr, off, "EDGE", 0.26, ow)
    _surface(sc, f2, s2, tr, off, c2, op2, ow)
    ts = [tr[0] + (tr[1] - tr[0]) * i / 60 for i in range(61)]
    _pts(sc, [_cc(t) for t in ts], off, DRED, 3.4)


@_fig("t3-curve-surface-forms")
def curve_surface_forms():
    sc = Scene(860, 520, (430, 260), 60)
    # (a) implicit surface
    off = (-4.2, 2.8)
    _surface(sc, _ga, (0.0, 1.3), (0.0, 2.8), off, "EDGE", 0.24, 1.4)
    _txt(sc, _q(_ga(0.65, 1.4), off), "f(x,y,z) = 0", "HEAD", "middle", 17, dy=2)
    _txt(sc, (-6.8, 3.9), "(a)", "TEXT", "start", 15, italic=False)
    # (b) curve as the intersection of two surfaces
    off = (3.6, 1.5)
    _two_surfaces(sc, off)
    _txt(sc, _q(_ruled(-1.5, 0.85, D1, 0.08), off), "f(x,y,z) = 0", "HEAD", "end", 16, dx=-10, dy=8)
    _txt(sc, _q(_ruled(0.2, 0.85, D2, -0.10), off), "h(x,y,z) = 0", "HEAD", "middle", 16, dy=-16)
    _txt(sc, _q(_cc(1.5), off), "curve", DRED, "start", 16, dx=12, dy=10, italic=False)
    _txt(sc, (0.2, 3.9), "(b)", "TEXT", "start", 15, italic=False)
    # (c) parametric curve
    off = (-4.4, -2.3)
    cc = lambda t: (0.9 * math.sin(1.3 * t), 1.1 * t, 0.62 * math.sin(0.9 * t + 0.5))
    ts = [-1.7 + 3.4 * i / 80 for i in range(81)]
    _pts(sc, [cc(t) for t in ts], off, DRED, 3.0)
    for t in (-1.2, -0.6, 0.0, 0.6, 1.2):
        p = _q(cc(t), off)
        h = 1e-3
        a, b = _q(cc(t - h), off), _q(cc(t + h), off)
        tx, ty = b[0] - a[0], b[1] - a[1]
        n = math.hypot(tx, ty)
        nx, ny = -ty / n, tx / n
        sc.line((p[0] - 0.1 * nx, p[1] - 0.1 * ny), (p[0] + 0.1 * nx, p[1] + 0.1 * ny), "HEAD", 1.6)
    a, b = cc(-0.5), cc(0.3)
    sc.vec(_q(_v3(a, (0, 0, 0.5)), off), _q(_v3(b, (0, 0, 0.5)), off), None, ORANGE, 2.8, head=11)
    _txt(sc, _q(_v3(cc(-0.1), (0, 0, 0.5)), off), "α", "GREEN", "middle", 18, dy=-12)
    for i, s in enumerate(("x = x(α)", "y = y(α)", "z = z(α)")):
        _txt(sc, (-2.0, -2.0 - 0.52 * i), s, "HEAD", "start", 16)
    _txt(sc, (-6.8, -0.5), "(c)", "TEXT", "start", 15, italic=False)
    # (d) surface with coordinate lines
    off = (1.4, -1.2)
    gd = lambda u, v: (XS * u, v, -0.7 * u + 0.30 * math.sin(1.2 * v + 0.2) + 0.2 * u * u)
    ur, vr = (0.0, 1.2), (0.0, 2.6)
    _surface(sc, gd, ur, vr, off, "EDGE", 0.22, 1.3)
    for i in range(1, 4):                                   # constant beta: alpha (= u) grows
        v = vr[1] * i / 4
        _pts(sc, [gd(ur[0] + (ur[1] - ur[0]) * j / 20, v) for j in range(21)], off, "BLUE", 1.5, "5 4")
    for i in range(1, 5):                                   # constant alpha: beta (= v) grows
        u = ur[1] * i / 5
        _pts(sc, [gd(u, vr[0] + (vr[1] - vr[0]) * j / 20) for j in range(21)], off, DRED, 1.5, "5 4")
    p0, p1 = gd(0.1, -0.6), gd(0.95, -0.6)
    sc.vec(_q(p0, off), _q(p1, off), None, "BLUE", 2.6, head=10)
    _txt(sc, _q(gd(0.5, -0.6), off), "α", "BLUE", "middle", 18, dx=-16, dy=0)
    p0, p1 = gd(1.35, 0.35), gd(1.35, 1.6)
    sc.vec(_q(p0, off), _q(p1, off), None, DRED, 2.6, head=10)
    _txt(sc, _q(gd(1.35, 1.0), off), "β", DRED, "middle", 18, dx=-4, dy=26)
    for i, s in enumerate(("x = x(α,β)", "y = y(α,β)", "z = z(α,β)")):
        _txt(sc, (4.7, -1.9 - 0.52 * i), s, "HEAD", "start", 16)
    _txt(sc, (0.2, -0.5), "(d)", "TEXT", "start", 15, italic=False)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _cone_hull(r, H):
    """Boundary (2D, relative to the vertex) of the convex hull of the vertex and the rim circle of radius r at height H."""
    n = 360
    E = [P3((r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n), H)) for i in range(n)]

    def side(i):
        a, b = E[i - 1], E[(i + 1) % n]
        d = (b[0] - a[0], b[1] - a[1])
        return d[0] * E[i][1] - d[1] * E[i][0]
    roots = [i for i in range(n) if side(i) * side((i + 1) % n) < 0]
    ia, ib = roots[0], roots[1]
    top = max(range(n), key=lambda i: E[i][1])
    if ia < top < ib:
        arc = list(range(ia, ib + 1))
    else:
        arc = list(range(ib, n)) + list(range(0, ia + 1))
        arc = arc[::-1]
    if not (ia in (arc[0], arc[-1])):
        arc = arc[::-1]
    pts = [(0.0, 0.0)] + [E[i] for i in arc]
    return pts, E


@_fig("t3-coordinate-choices")
def coordinate_choices():
    sc = Scene(900, 500, (450, 250), 68)
    # ---- left: sphere about A ------------------------------------------------------------------------------------
    off = (-3.2, 0.1)
    l = 1.9
    ph, th = math.radians(30), math.radians(40)
    sc.poly([(off[0] + x, off[1] + y) for x, y in _ellipse_outline(l)], "HEAD", 1.4, fill="EDGE", close=True, opacity=0.16)
    _pts(sc, [(l * math.cos(t), l * math.sin(t), 0.0) for t in [2 * math.pi * i / 90 for i in range(91)]], off, "HEAD", 1.0, "6 4")
    ex = (math.cos(th), math.sin(th), 0.0)
    ez = (0.0, 0.0, 1.0)
    ar = (math.cos(ph) * math.cos(th), math.cos(ph) * math.sin(th), math.sin(ph))
    Pp = _mul(ar, l)
    Q = _mul(ex, l * math.cos(ph))
    # axes parallel to Ox, Oy, Oz through A (grey)
    for v, nm, lab in (((0.8, 0, 0), "x", (-12, 12)), ((0, 1.3, 0), "y", (12, 8)), ((0, 0, 2.3), "z", (-4, -10))):
        _V(sc, (0, 0, 0), v, None, "EDGE", 1.4, off, head=8)
        sc.label(_q(v, off), nm, "TEXT", "middle", 17, weight="700", dx=lab[0], dy=lab[1])
    _L(sc, (0, 0, 0), Q, off, "HEAD", 1.2, "5 4")
    _L(sc, Q, Pp, off, "HEAD", 1.2, "5 4")
    sc.line(_q((0, 0, 0), off), _q(Pp, off), "HEAD", 1.7)
    m = _arc_at(sc, (0, 0, 0), (1, 0, 0), ex, 0.85, off, "GREEN", True, 1.8)
    _txt(sc, m, "θ", "GREEN", "middle", 18, dx=2, dy=24)
    m = _arc_at(sc, (0, 0, 0), ex, ar, 1.5, off, "GREEN", True, 1.8)
    _txt(sc, m, "φ", "GREEN", "middle", 18, dx=16, dy=8)
    _dp(sc, (0, 0, 0), off, 4.4)
    _txt(sc, _q((0, 0, 0), off), "A", "HEAD", "middle", 18, dx=-14, dy=-12)
    # basis at P
    er = ar
    et = (-math.sin(th), math.cos(th), 0.0)
    ef = (-math.sin(ph) * math.cos(th), -math.sin(ph) * math.sin(th), math.cos(ph))
    _V(sc, Pp, _mul(er, 0.75), _vb("e", "r"), "BLUE", 3.0, off, (20, -6), 17, 11)
    _V(sc, Pp, _mul(et, 0.75), _vb("e", "θ"), "BLUE", 3.0, off, (-6, 20), 17, 11)
    _V(sc, Pp, _mul(ef, 0.75), _vb("e", "φ"), "BLUE", 3.0, off, (22, -4), 17, 11)
    _dp(sc, Pp, off, 5.2)
    _txt(sc, _q(Pp, off), "P", "HEAD", "middle", 18, dx=-16, dy=-6)
    lab = _q(_mul(ar, 0.5), off)
    sc.line((lab[0] - 0.03, lab[1] + 0.02), (lab[0] - 0.95, lab[1] + 0.72), "HEAD", 0.9)
    _txt(sc, (lab[0] - 0.98, lab[1] + 0.72), "string, length ℓ", "HEAD", "end", 15, dx=-3, dy=-6, italic=False)
    # ---- right: cone ---------------------------------------------------------------------------------------------
    off = (2.5, -1.9)
    g = math.radians(30)
    r, H = 1.95, 3.4
    hull, rim = _cone_hull(r, H)
    sc.poly([(off[0] + x, off[1] + y) for x, y in hull], "HEAD", 1.4, fill="EDGE", close=True, opacity=0.16)
    sc.poly([(off[0] + x, off[1] + y) for x, y in rim], "HEAD", 1.0, close=True)
    for v, nm, lab in (((2.0, 0, 0), "x", (-12, 12)), ((0, 2.5, 0), "y", (12, 8)), ((0, 0, 4.3), "z", (-4, -10))):
        _V(sc, (0, 0, 0), v, None, "EDGE", 1.4, off, head=8)
        sc.label(_q(v, off), nm, "TEXT", "middle", 17, weight="700", dx=lab[0], dy=lab[1])
    lv = 2.5
    ps = math.radians(50)
    ca = (math.cos(ps), math.sin(ps), 0.0)
    Pc = (lv * math.sin(g) * ca[0], lv * math.sin(g) * ca[1], lv * math.cos(g))
    Hh = (0.0, 0.0, lv * math.cos(g))
    Qc = (Pc[0], Pc[1], 0.0)
    _pts(sc, [(0, 0, 0), Hh, Pc], off, ORANGE, 0.0, None, ORANGE, True, 0.20)
    _L(sc, Hh, Pc, off, "HEAD", 1.2, "5 4")
    _L(sc, (0, 0, 0), Qc, off, "HEAD", 1.2, "5 4")
    _L(sc, Qc, Pc, off, "HEAD", 1.2, "5 4")
    sc.line(_q((0, 0, 0), off), _q(Pc, off), "HEAD", 1.7)
    m = _arc_at(sc, (0, 0, 0), (1, 0, 0), ca, 0.8, off, "GREEN", True, 1.8)
    _txt(sc, m, "θ", "GREEN", "middle", 18, dx=-4, dy=24)
    m = _arc_at(sc, (0, 0, 0), ez, Pc, 0.85, off, "GREEN", True, 1.8)
    _txt(sc, m, "γ", "GREEN", "middle", 18, dx=-16, dy=-2)
    _dp(sc, (0, 0, 0), off, 4.4)
    _txt(sc, _q((0, 0, 0), off), "O", "HEAD", "middle", 18, dx=-14, dy=-10)
    _dp(sc, Pc, off, 5.2)
    _txt(sc, _q(Pc, off), "P", "HEAD", "middle", 18, dx=18, dy=4)
    _txt(sc, _q(_mul(Pc, 0.5), off), "ℓ" + S("", "V"), "HEAD", "start", 18, dx=40, dy=14)
    _txt(sc, _q(_mul(Hh, 0.82), off), "ℓ" + S("", "V") + " cos γ", "HEAD", "end", 15, dx=-10, dy=-4)
    _txt(sc, _q(_mul(Hh, 0.82), off), "(adjacent)", "HEAD", "end", 15, dx=-10, dy=14)
    _txt(sc, _q(Hh, off), "ℓ" + S("", "V") + " sin γ (opposite)", "HEAD", "start", 15, dx=10, dy=-14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _tvec(name, sub):
    return S(bold(name), sub)


def _frame_surface():
    """Surface of the normal figure: tangent plane at the origin spanned by t_a and t_b (70 degrees apart), curved away from it."""
    n0 = _unit3((0.22, -0.10, 1.0))
    yb = (0.0, 1.0, 0.0)
    tb = _unit3(_lin((1.0, yb), (-_dot(yb, n0), n0)))
    w = _cross(n0, tb)
    ta = _lin((math.cos(math.radians(70)), tb), (-math.sin(math.radians(70)), w))
    n = _cross(ta, tb)
    n = _unit3(n)

    def f(a, b):
        c = -0.07 * a * a - 0.10 * b * b + 0.03 * a * b
        return _lin((a, ta), (b, tb), (c, n))
    return f, ta, tb, n


@_fig("t3-surface-normal")
def surface_normal():
    sc = Scene(860, 372, (400, 160), 64)
    off = (0.0, -0.2)
    f, ta, tb, n = _frame_surface()
    ar, br = (-2.5, 2.5), (-2.4, 2.4)
    _surface(sc, f, ar, br, off, "EDGE", 0.22, 1.4)
    _grid(sc, f, ar, br, 3, 3, off, "HEAD", 0.9, "4 3")
    O = (0.0, 0.0, 0.0)
    # tangent plane at P
    sa, sb = 1.0, 0.62
    cor = [_lin((sa, ta), (sb, tb)), _lin((sa, ta), (-sb, tb)), _lin((-sa, ta), (-sb, tb)), _lin((-sa, ta), (sb, tb))]
    _pts(sc, cor, off, ORANGE, 1.0, None, ORANGE, True, 0.30)
    # normals at two other points (gradient field)
    for (a, b) in ((-1.7, 1.5), (1.9, -1.6)):
        p = f(a, b)
        nn = _unit3(_cross(_du(f, a, b), _dv(f, a, b)))
        _V(sc, p, _mul(nn, 1.0), None, ORANGE, 1.7, off, head=8)
        _dp(sc, p, off, 3.2)
    # tangent vectors and the normal at P
    _V(sc, O, _mul(ta, 1.9), _tvec("t", "α"), ORANGE, 3.2, off, (-6, 20), 17, 12)
    _V(sc, O, _mul(tb, 1.4), _tvec("t", "β"), ORANGE, 3.2, off, (4, -14), 17, 12)
    _V(sc, O, _mul(n, 1.9), None, ORANGE, 3.4, off, head=13)
    _right_mark3(sc, O, n, tb, 0.2, off, "HEAD")
    _dp(sc, O, off, 5.2)
    _txt(sc, _q(_mul(n, 1.9), off), bold("n") + " = ∇f = " + _tvec("t", "α") + " × " + _tvec("t", "β"), "HEAD", "start", 17, dx=14, dy=-6)
    _txt(sc, _q(_lin((0.55, ta), (0.36, tb)), off), "V" + S("", "T"), "HEAD", "middle", 16, dy=5)
    _txt(sc, _q(_mul(n, 1.2), off), "V" + S("", "N"), "HEAD", "end", 17, dx=-10, dy=4)
    _txt(sc, _q(f(ar[1], br[0]), off), "f(x,y,z) = 0", "HEAD", "start", 17, dx=14, dy=14)
    # parameter arrows at the edges
    p0, p1 = f(-1.5, br[1] + 0.45), f(0.5, br[1] + 0.45)
    sc.vec(_q(p0, off), _q(p1, off), None, "HEAD", 2.0, head=9)
    _txt(sc, _q(p1, off), "α", "HEAD", "middle", 18, dx=14, dy=12)
    p0, p1 = f(ar[1] + 0.5, -1.4), f(ar[1] + 0.5, 0.6)
    sc.vec(_q(p0, off), _q(p1, off), None, "HEAD", 2.0, head=9)
    _txt(sc, _q(p1, off), "β", "HEAD", "middle", 18, dx=12, dy=14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-curve-normals")
def curve_normals():
    sc = Scene(900, 480, (450, 260), 70)
    off = (-0.2, 0.15)
    D1b, D2b = D1, D2
    _two_surfaces(sc, off, "ACC", 0.20, tr=(-1.9, 1.9), s1=(-0.7, 1.0), s2=(-0.5, 1.0))
    C0 = _cc(0.0)
    h = 1e-4
    T = _unit3(_sub3(_cc(h), _cc(-h)))
    nf = _unit3(_cross(D1b, T))
    nh = _unit3(_cross(T, D2b))
    # normal plane at P: disc through n_f and n_h
    e1 = nf
    e2 = _unit3(_lin((1.0, nh), (-_dot(nh, nf), nf)))
    rd = 1.05
    disc = [_v3(C0, _lin((rd * math.cos(t), e1), (rd * math.sin(t), e2))) for t in [2 * math.pi * i / 80 for i in range(81)]]
    _pts(sc, disc, off, "BLUE", 1.0, None, "BLUE", True, 0.14)
    _V(sc, C0, _mul(T, 1.9), None, ORANGE, 3.4, off, head=13)
    _txt(sc, _q(_v3(C0, T, 1.9), off), _vb("t") + " = " + _vb("n", "f") + " × " + _vb("n", "h"), "ORANGE" if False else ORANGE, "start", 17, dx=14, dy=-2)
    _V(sc, C0, _mul(nf, 1.5), None, "BLUE", 3.4, off, head=13)
    _txt(sc, _q(_v3(C0, nf, 1.5), off), _vb("n", "f") + " = ∇f", "BLUE", "end", 17, dx=-12, dy=-2)
    _V(sc, C0, _mul(nh, 1.5), None, "BLUE", 3.4, off, head=13)
    _txt(sc, _q(_v3(C0, nh, 1.5), off), _vb("n", "h") + " = ∇h", "BLUE", "end", 17, dx=8, dy=26)
    _dp(sc, C0, off, 5.2)
    _txt(sc, _q(C0, off), "P", "HEAD", "middle", 18, dx=14, dy=22)
    _txt(sc, _q(_ruled(-1.9, 1.0, D1b, 0.08), off), "f(x,y,z) = 0", "HEAD", "end", 16, dx=-10, dy=8)
    _txt(sc, _q(_ruled(0.2, 1.0, D2b, -0.10), off), "h(x,y,z) = 0", "HEAD", "middle", 16, dy=-16)
    _txt(sc, _q(disc[39], off), "V" + S("", "N"), "BLUE", "middle", 17, dx=4, dy=22)
    _txt(sc, _q(_v3(C0, T, 1.1), off), "V" + S("", "T"), ORANGE, "middle", 17, dy=-14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-ellipse-vectors")
def ellipse_vectors():
    sc = Scene(720, 380, (360, 200), 100)
    a, b = 2.0, 1.0
    al = math.radians(50)
    fixed_axis(sc, (0, 0), 0, 2.55, "x", off=(10, 18))
    fixed_axis(sc, (0, 0), 90, 1.5, "y", off=(-12, 4))
    fixed_axis(sc, (0, 0), 180, 2.3, "", dashed=True, off=(0, 0))
    fixed_axis(sc, (0, 0), 270, 1.3, "", dashed=True, off=(0, 0))
    sc.curve(lambda t: (a * math.cos(t), b * math.sin(t)), 0, 2 * math.pi, 160, DRED, 2.8)
    for p, ang in (((a, 0), 90), ((-a, 0), 90), ((0, b), 0), ((0, -b), 0)):
        d = _d(ang)
        sc.line((p[0] - 0.06 * d[0], p[1] - 0.06 * d[1]), (p[0] + 0.06 * d[0], p[1] + 0.06 * d[1]), "HEAD", 1.8)
    sc.label((a, 0), "a" + S("", "e"), "HEAD", "middle", 17, dx=10, dy=22)
    sc.label((0, b), "b" + S("", "e"), "HEAD", "end", 17, dx=-10, dy=-8)
    P = (a * math.cos(al), b * math.sin(al))
    sc.dashed(P, (P[0], 0))
    sc.dashed(P, (0, P[1]))
    sc.label((P[0], 0), "a" + S("", "e") + " cos α", "HEAD", "middle", 16, dy=22)
    sc.label((0, P[1]), "b" + S("", "e") + " sin α", "HEAD", "end", 16, dx=-12, dy=5)
    t = (-a * math.sin(al), b * math.cos(al))
    n = (2 * P[0] / a ** 2, 2 * P[1] / b ** 2)
    kk = 0.6
    sc.vec(P, (P[0] + kk * t[0], P[1] + kk * t[1]), None, ORANGE, 3.4, head=13)
    sc.vec(P, (P[0] + kk * n[0], P[1] + kk * n[1]), None, "BLUE", 3.4, head=13)
    sc.label((P[0] + kk * t[0], P[1] + kk * t[1]), bold("t"), ORANGE, "middle", 19, dx=-8, dy=-12)
    sc.label((P[0] + kk * n[0], P[1] + kk * n[1]), S(bold("n"), "f"), "BLUE", "middle", 19, dx=14, dy=-8)
    right_angle(sc, P, math.degrees(math.atan2(t[1], t[0])), math.degrees(math.atan2(n[1], n[0])), 0.17, "HEAD")
    axis_out(sc, P, None, "HEAD", r_px=9)
    sc.label(P, "P", "HEAD", "middle", 18, dx=18, dy=26)
    sc.label(P, S(bold("n"), "h") + " = " + bold("k"), "HEAD", "start", 17, dx=18, dy=-26 + 12)
    axis_out(sc, (0, 0), None, "HEAD", r_px=9)
    sc.label((0, 0), bold("k"), "HEAD", "end", 17, dx=-14, dy=24)
    sc.label((0, 0), "O", "HEAD", "start", 17, dx=12, dy=22)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _hull(pts):
    """Convex hull (monotone chain) of 2D points."""
    pts = sorted(set(pts))

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def _par(R, th):
    return (R * math.cos(th), R * math.sin(th), R * R)


@_fig("t3-paraboloid-vectors")
def paraboloid_vectors():
    _PR["p"] = lambda v: (0.15 * v[0] + 1.0 * v[1], -0.62 * v[0] + 0.05 * v[1] + v[2])      # x towards the viewer on the right
    try:
        return _paraboloid_vectors()
    finally:
        _PR["p"] = P3


def _paraboloid_vectors():
    sc = Scene(800, 450, (330, 310), 100)
    off = (0.0, 0.0)
    Rm = 1.25
    cloud = [_q(_par(Rm * i / 24, 2 * math.pi * j / 72)) for i in range(25) for j in range(72)]
    sc.poly(_hull(cloud), "HEAD", 1.4, fill="EDGE", close=True, opacity=0.18)
    for R in (0.84,):
        _pts(sc, [_par(R, 2 * math.pi * j / 72) for j in range(73)], off, "HEAD", 0.9, "4 3")
    _pts(sc, [_par(Rm, 2 * math.pi * j / 72) for j in range(73)], off, "HEAD", 1.0)
    for deg in (90, 180, 270):
        th = math.radians(deg)
        _pts(sc, [_par(Rm * i / 20, th) for i in range(21)], off, "HEAD", 0.9, "4 3")
    O = (0.0, 0.0, 0.0)
    for v, nm, lab in (((1.75, 0, 0), "x", (-12, 12)), ((0, 1.95, 0), "y", (14, 6)), ((0, 0, 2.6), "z", (-4, -10))):
        _V(sc, O, v, None, "EDGE", 1.4, off, head=8)
        sc.label(_q(v, off), nm, "TEXT", "middle", 17, weight="700", dx=lab[0], dy=lab[1])
    R, th = 0.8, math.radians(30)
    P = _par(R, th)
    Q = (P[0], P[1], 0.0)
    _L(sc, P, Q, off, "HEAD", 1.2, "5 4")
    _L(sc, O, Q, off, "HEAD", 1.2, "5 4")
    m = _arc_at(sc, O, (1, 0, 0), (math.cos(th), math.sin(th), 0), 0.6, off, "GREEN", True, 1.8)
    sc.label(m, "θ", "GREEN", "middle", 18, dx=-14, dy=22)
    sc.label(_q(_mul(Q, 0.5), off), "R", "HEAD", "middle", 17, dx=-4, dy=-9)
    sc.label(_q(_mul(_v3(P, Q), 0.5), off), "R²", "HEAD", "start", 17, dx=8, dy=10)
    tR = _mul((math.cos(th), math.sin(th), 2 * R), 0.5)
    tt = _mul((-R * math.sin(th), R * math.cos(th), 0.0), 0.9)
    nn = _mul((2 * P[0], 2 * P[1], -1.0), 0.5)
    _V(sc, P, _mul(nn, -1.0), None, "BLUE", 2.4, off, head=11, dash="6 4")
    sc.label(_q(_v3(P, nn, -1.0), off), S(bold("t"), "R") + " × " + S(bold("t"), "θ") + " = −R " + bold("n"), "BLUE", "start", 16,
             dx=14, dy=-30)
    _V(sc, P, tR, S(bold("t"), "R"), ORANGE, 3.4, off, (-4, -14), 18, 13)
    _V(sc, P, tt, S(bold("t"), "θ"), ORANGE, 3.4, off, (4, -16), 18, 13)
    _V(sc, P, nn, bold("n"), "BLUE", 3.4, off, (14, 10), 18, 13)
    _dp(sc, O, off, 3.6)
    sc.label(_q(O, off), "O", "HEAD", "end", 17, dx=-10, dy=-4)
    _dp(sc, P, off, 5.2)
    sc.label(_q(P, off), "P", "HEAD", "middle", 18, dx=-16, dy=-4)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-surface-reaction")
def surface_reaction():
    sc = Scene(860, 372, (400, 160), 64)
    off = (0.0, -0.2)
    f, ta, tb, n = _frame_surface()
    ar, br = (-2.5, 2.5), (-2.4, 2.4)
    _surface(sc, f, ar, br, off, "EDGE", 0.22, 1.4)
    O = (0.0, 0.0, 0.0)
    path = [f(0.6 * s + 0.08 * s * s, 0.8 * s - 0.06 * s * s) for s in [-2.6 + 5.2 * i / 60 for i in range(61)]]
    _pts(sc, path, off, DRED, 1.6, "6 4")
    v = _mul(_unit3(_lin((0.6, ta), (0.8, tb))), 1.9)
    _V(sc, O, v, None, ORANGE, 3.4, off, head=13)
    sc.label(_q(_v3(O, v), off), _vb("v", "0", "P"), ORANGE, "start", 18, weight="700", dx=12, dy=12)
    _V(sc, O, _mul(n, 2.1), None, "PINK", 3.4, off, head=13)
    sc.label(_q(_mul(n, 2.1), off), bold("N"), "PINK", "middle", 19, dx=-14, dy=-6)
    _right_mark3(sc, O, n, _unit3(v), 0.3, off, "HEAD")
    _dp(sc, O, off, 5.2)
    sc.label(_q(O, off), "P", "HEAD", "middle", 18, dx=-14, dy=18)
    _txt(sc, _q(_mul(n, 1.7), off), dot1("W") + S("", "0") + " = " + bold("N") + " · " + _vb("v", "0", "P") + " = 0", "HEAD",
         "start", 17, dx=18, dy=0)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _dvec2(sc, a, b, col, w=2.4, dash="6 4", head=11):
    """Arrow with a dashed shaft from world point a to world point b."""
    pa, pb = sc.P(a), sc.P(b)
    ang = math.atan2(pb[1] - pa[1], pb[0] - pa[0])
    k = 0.6 * head / sc.k
    sc.line(a, (b[0] - k * math.cos(ang), b[1] + k * math.sin(ang)), col, w, dash)
    arrow_head(sc.c, pa, pb, col, head)


@_fig("t3-spool")
def spool():
    sc = Scene(760, 560, (350, 130), 80)
    O = (0.0, 0.0)
    zeta = 3.3
    # axes
    fixed_axis(sc, O, 90, 1.25, "z", off=(-10, -6))
    fixed_axis(sc, O, 0, 2.1, "y", off=(12, 8))
    fixed_axis(sc, O, 218, 1.5, "x", off=(-10, 14))
    sc.disk(O, 0.2, "HEAD", "HEAD", 0.18, 2.2)
    sc.label(O, "O", "HEAD", "start", 17, dx=-30, dy=-12)
    # string and particle
    Pp = (0.0, -zeta)
    sc.line((0.0, -0.2), Pp, "HEAD", 1.6)
    sc.dim((-1.9, 0.0), (-1.9, -zeta), "ζ", off=(-14, 5), size=18)
    sc.dashed((-0.2, 0.0), (-1.98, 0.0))
    sc.dashed((-0.15, -zeta), (-1.98, -zeta))
    # gravity
    sc.gravity((-3.3, -1.2), 1.0, "g")
    # free-body diagram at P
    L = 1.2
    sc.vec(Pp, (0.0, -zeta - L), None, "PINK", 3.6, head=13)
    sc.vec(Pp, (0.0, -zeta + L), None, "PINK", 3.6, head=13)
    sc.label((0.0, -zeta - L), S(bold("F"), "g") + " = −m g " + bold("k"), "PINK", "start", 18, dx=14, dy=4)
    sc.label((0.0, -zeta + L), S(bold("F"), "T") + " = F" + S("", "T") + " " + bold("k"), "PINK", "end", 18, dx=-14, dy=2)
    _dvec2(sc, (0.5, -zeta), (0.5, -zeta + 1.0), ORANGE)
    sc.label((0.5, -zeta + 1.0), _vb("v", "0", "P") + " = c " + bold("k"), ORANGE, "start", 18, dx=12, dy=4, weight="700")
    sc.dotp(Pp, 5.5)
    sc.label(Pp, "P", "HEAD", "start", 18, dx=-26, dy=-10)
    # data box
    x, y = sc.P((1.7, -0.5))
    from figures.svgkit import rect as _r
    _r(sc.c, x, y, 190, 72, "EDGE", 1.2, rx=8)
    sc.label((1.7, -0.5), dot1("ζ") + " = −c", "HEAD", "start", 17, dx=16, dy=28)
    sc.label((1.7, -0.5), "ζ(0) = ℓ" + S("", "0"), "HEAD", "start", 17, dx=16, dy=56)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-airplane-fbd")
def airplane_fbd():
    sc = Scene(860, 470, (400, 345), 105)
    # runway with hatching below
    sc.line((-3.9, 0.0), (3.9, 0.0), "HEAD", 3.2)
    for i in range(46):
        x = -3.9 + 0.17 * i
        sc.line((x, 0.0), (x - 0.14, -0.2), "EDGE", 1.0)
    sc.label((3.9, -0.02), "z ≥ 0 (unilateral)", "HEAD", "end", 17, dy=34, italic=False)
    # airplane silhouette (outline only)
    cx, cy, rx, ry = 0.0, 1.55, 1.95, 0.30
    sc.poly([(cx + rx * math.cos(t), cy + ry * math.sin(t)) for t in [2 * math.pi * i / 80 for i in range(81)]], "HEAD", 2.0, close=True)
    sc.poly([(-1.0, 1.82), (-1.95, 2.42), (-2.12, 2.42), (-1.72, 1.70)], "HEAD", 2.0)
    sc.poly([(0.7, 1.40), (-0.6, 1.40), (-1.25, 0.98), (-0.55, 0.98)], "HEAD", 1.8, close=True)
    for gx in (-1.55, 1.5):
        sc.line((gx, 1.28), (gx, 0.17), "HEAD", 2.0)
        sc.circle((gx, 0.17), 0.17, "HEAD", 2.0)
    P = (0.0, cy)
    W = 1.25
    sc.vec(P, (0.0, cy - W), None, "PINK", 3.6, head=13)
    sc.vec(P, (0.0, cy + 0.6 * W), None, "PINK", 3.6, head=13)
    sc.vec((0.55, 0.0), (0.55, 0.4 * W), None, "PINK", 3.6, head=13)
    sc.label((0.0, cy - W), S(bold("F"), "g") + " = −m g " + bold("k"), "PINK", "end", 18, dx=-14, dy=4)
    sc.label((0.0, cy + 0.6 * W), "L " + bold("k"), "PINK", "start", 18, dx=14, dy=-6)
    sc.label((0.55, 0.4 * W), "N " + bold("k"), "PINK", "start", 18, dx=14, dy=-2)
    sc.label((0.55, 0.4 * W), "N ≥ 0", "HEAD", "start", 16, dx=14, dy=24, italic=False)
    # velocity
    sc.vec((0.0, cy + 0.0), (2.7, cy + 0.0), None, ORANGE, 3.0, head=12)
    sc.label((2.7, cy), "v " + bold("i"), ORANGE, "start", 18, dx=12, dy=5, weight="700")
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "middle", 18, dx=-14, dy=-10)
    # axes
    fixed_axis(sc, (-3.6, 0.55), 0, 0.9, bold("i"), off=(12, 6))
    fixed_axis(sc, (-3.6, 0.55), 90, 0.9, bold("k"), off=(-12, -2))
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _wire(u):
    return (1.2 + 1.3 * math.cos(u), 2.7 + 1.3 * math.sin(u), 0.5 + 0.95 * u)


def _frame(f, u):
    return _triad(f, u)


@_fig("t3-curve-reaction")
def curve_reaction():
    sc = Scene(900, 540, (430, 300), 92)
    u0 = 1.1
    P = _wire(u0)
    p2 = P3(P)
    off = (-p2[0] + 0.3, -p2[1] - 0.1)
    us = [0.1 + 2.7 * i / 160 for i in range(161)]
    _pts(sc, [_wire(u) for u in us], off, DRED, 3.4)
    et, en, eb = _frame(_wire, u0)
    sc.label(_q(_wire(us[-1]), off), "wire", DRED, "start", 17, dx=12, dy=-4, italic=False)
    # normal plane: translucent disc
    rd = 1.55
    disc = [_v3(P, _lin((rd * math.cos(t), en), (rd * math.sin(t), eb))) for t in [2 * math.pi * i / 80 for i in range(81)]]
    _pts(sc, disc, off, "BLUE", 1.0, None, "BLUE", True, 0.14)
    sc.label(_q(disc[52], off), "V" + S("", "N"), "BLUE", "middle", 17, dx=0, dy=26)
    # intrinsic basis
    _V(sc, P, _mul(et, 1.5), _vb("e", "t"), "BLUE", 3.2, off, (18, -4), 18, 12)
    _V(sc, P, _mul(en, 1.5), _vb("e", "n"), "BLUE", 3.2, off, (-16, -2), 18, 12)
    _V(sc, P, _mul(eb, 1.5), _vb("e", "b"), "BLUE", 3.2, off, (-6, -14), 18, 12)
    # reaction in the normal plane
    Nn, Nb = 0.9, 0.75
    N = _lin((Nn, en), (Nb, eb))
    _V(sc, P, N, None, "PINK", 3.6, off, head=13)
    sc.label(_q(_v3(P, N), off), bold("N"), "PINK", "middle", 19, dx=-14, dy=-10)
    for v in (_mul(en, Nn), _mul(eb, Nb)):
        _dp(sc, _v3(P, v), off, 3.0, "PINK")
    _L(sc, _v3(P, _mul(en, Nn)), _v3(P, N), off, "PINK", 1.1, "3 3")
    _L(sc, _v3(P, _mul(eb, Nb)), _v3(P, N), off, "PINK", 1.1, "3 3")
    sc.label(_q(_v3(P, _mul(en, Nn)), off), S("N", "n") + " " + _vb("e", "n"), "PINK", "end", 16, dx=-12, dy=20)
    sc.label(_q(_v3(P, _mul(eb, Nb)), off), S("N", "b") + " " + _vb("e", "b"), "PINK", "start", 16, dx=12, dy=-4)
    # applied force with its components
    Ft, Fn, Fb = 1.3, -0.85, -0.85
    F = _lin((Ft, et), (Fn, en), (Fb, eb))
    _V(sc, P, F, None, "PINK", 3.6, off, head=13, dash="9 5")
    sc.label(_q(_v3(P, F), off), bold("F"), "PINK", "middle", 19, dx=12, dy=-10)
    for k, v, nm in ((Ft, et, S("F", "t")), (Fn, en, S("F", "n")), (Fb, eb, S("F", "b"))):
        foot = _v3(P, _mul(v, k))
        _L(sc, foot, _v3(P, F), off, "PINK", 1.1, "3 3")
        _dp(sc, foot, off, 3.0, "PINK")
        sc.label(_q(foot, off), nm, "PINK", "start" if nm == S("F", "t") else "middle", 17, dx=14 if nm == S("F", "t") else -10, dy=8 if nm == S("F", "t") else 18)
    _dp(sc, P, off, 5.2)
    sc.label(_q(P, off), "P", "HEAD", "middle", 18, dx=-14, dy=-12)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-vertical-circle")
def vertical_circle():
    sc = Scene(700, 470, (340, 240), 105)
    a = 1.55
    th = 35.0
    fixed_axis(sc, (0, 0), 0, 2.15, "x", off=(12, 18))
    fixed_axis(sc, (0, 0), 90, 1.85, "y", off=(-12, 2))
    fixed_axis(sc, (0, 0), 180, 1.95, "", dashed=True, off=(0, 0))
    fixed_axis(sc, (0, 0), 270, 1.85, "", dashed=True, off=(0, 0))
    sc.curve(lambda t: (a * math.cos(t), a * math.sin(t)), 0, 2 * math.pi, 160, DRED, 3.0)
    P = (a * math.cos(math.radians(th)), a * math.sin(math.radians(th)))
    sc.line((0, 0), P, "HEAD", 1.8)
    sc.arc((0, 0), 0.62, 0, th, "GREEN", 1.8, head=True)
    sc.label(_add((0, 0), _d(th / 2), 0.95), "θ", "GREEN", "middle", 19, dy=6)
    sc.label((P[0] / 2, P[1] / 2), "a", "HEAD", "middle", 18, dx=-6, dy=-14)
    sc.mass(P, None, 7.5)
    sc.label(P, "P", "HEAD", "middle", 18, dx=16, dy=-12)
    axis_out(sc, (0, 0), None, "HEAD", r_px=9)
    sc.label((0, 0), bold("k"), "HEAD", "end", 17, dx=-14, dy=26)
    sc.label((0, 0), "O", "HEAD", "start", 17, dx=12, dy=24)
    sc.gravity((-2.7, 1.0), 0.7, "g")
    return sc


def _rot_view(sc, O, L, th, n, thn, ra, rb):
    """Simple rotation about the axis out of the paper: grey axes, blue rotated axes, arcs of the angle and the two shaded
    triangles with their legs named (adjacent / opposite)."""
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    fixed_axis(sc, O, 0, L * 1.3, n["h0"], off=(16, 6))
    fixed_axis(sc, O, 90, L * 1.3, n["v0"], off=(14, 4))
    cosl, sinl = "cos " + thn, "sin " + thn
    foot, tip = (O[0] + L * c, O[1]), (O[0] + L * c, O[1] + L * s)
    triangle(sc, [O, foot, tip], "BLUE", 0.16)
    sc.dashed(foot, tip)
    right_angle(sc, foot, 180, 90, 0.08)
    sc.label((O[0] + L * c / 2, O[1]), cosl + " (adjacent)", "HEAD", "middle", 15, dy=24)
    sc.label((foot[0], O[1] + L * s / 2), sinl, "HEAD", "start", 15, dx=10, dy=-2)
    sc.label((foot[0], O[1] + L * s / 2), "(opposite)", "HEAD", "start", 15, dx=10, dy=16)
    foot2, tip2 = (O[0], O[1] + L * c), (O[0] - L * s, O[1] + L * c)
    triangle(sc, [O, foot2, tip2], "BLUE", 0.16)
    sc.dashed(foot2, tip2)
    right_angle(sc, foot2, 270, 180, 0.08)
    sc.label((O[0], O[1] + L * c * 0.55), cosl, "HEAD", "start", 15, dx=10, dy=-2)
    sc.label((O[0], O[1] + L * c * 0.55), "(adjacent)", "HEAD", "start", 15, dx=10, dy=16)
    sc.label((O[0] - L * s / 2, tip2[1]), sinl, "HEAD", "middle", 15, dy=-30)
    sc.label((O[0] - L * s / 2, tip2[1]), "(opposite)", "HEAD", "middle", 15, dy=-12)
    for deg, nm, off in ((th, n["h1"], (24, -8)), (th + 90, n["v1"], (-26, 4))):
        tp = (O[0] + L * math.cos(math.radians(deg)), O[1] + L * math.sin(math.radians(deg)))
        sc.vec(O, tp, None, "BLUE", 3.0, head=12)
        sc.label(tp, nm, "BLUE", "middle", 18, weight="700", dx=off[0], dy=off[1])
    sc.arc(O, ra, 0, th, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d(th / 2), ra + 0.3), thn, "GREEN", "middle", 18, dy=5)
    sc.arc(O, rb, 90, 90 + th, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d(90 + th / 2), rb + 0.3), thn, "GREEN", "middle", 18, dy=5)


def _rot_matrix_figure(names, thn, th, title, axis_label):
    sc = Scene(800, 400, (250, 330), 90)
    O = (0.0, 0.0)
    _rot_view(sc, O, 2.1, th, names, thn, 0.8, 1.2)
    axis_out(sc, O, None, "HEAD", r_px=9)
    sc.label(O, axis_label, "HEAD", "end", 17, dx=-14, dy=26)
    cc, ss = "cos " + thn, "sin " + thn
    _matrix(sc, 500, 70, title, [[cc, "−" + ss, "0"], [ss, cc, "0"], ["0", "0", "1"]])
    return sc


@_fig("t3-vertical-circle-basis")
def vertical_circle_basis():
    th = "θ"
    nm = {"h0": bold("i"), "v0": bold("j"), "h1": S(bold("e"), "R"), "v1": S(bold("e"), "θ")}
    return _rot_matrix_figure(nm, th, 35.0, "[" + S("", "0") + "R" + S("", "1") + "] =", bold("k"))


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-vertical-circle-fbd")
def vertical_circle_fbd():
    sc = Scene(860, 560, (330, 290), 100)
    a = 2.2
    th = 35.0
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    sc.curve(lambda t: (a * math.cos(t), a * math.sin(t)), 0, 2 * math.pi, 160, DRED, 2.0)
    P = (a * c, a * s)
    eR, eT = (c, s), (-s, c)
    sc.dotp((0, 0), 3.5)
    sc.label((0, 0), "O", "HEAD", "start", 17, dx=10, dy=22)
    # free body
    sc.circle(P, 0.33, "HEAD", 1.3, "5 4")
    # weight and its components
    W = 1.5
    Wv = (0.0, -W)
    cR, cT = W * s, W * c                  # weight = -cR e_R - cT e_theta
    B = (P[0] - cR * eR[0], P[1] - cR * eR[1])
    D = (P[0] - cT * eT[0], P[1] - cT * eT[1])
    C = (P[0], P[1] - W)
    triangle(sc, [P, B, C], "PINK", 0.16)
    sc.line(B, C, "PINK", 1.3, "4 3")
    sc.line(D, C, "PINK", 1.3, "4 3")
    right_angle(sc, B, math.degrees(math.atan2(eR[1], eR[0])), math.degrees(math.atan2(-eT[1], -eT[0])), 0.1, "PINK")
    _dvec2(sc, P, B, "PINK", 1.8, "5 4", 9)
    _dvec2(sc, P, D, "PINK", 1.8, "5 4", 9)
    sc.label(B, "−m g sin θ", "PINK", "end", 16, dx=-10, dy=14)
    sc.label(D, "−m g cos θ", "PINK", "start", 16, dx=12, dy=8)
    sc.arc(P, 0.5, 270, 270 + th, "GREEN", 1.7, head=True)
    sc.label(_add(P, _d(270 + th / 2), 0.78), "θ", "GREEN", "middle", 18, dy=5)
    sc.vec(P, C, None, "PINK", 3.6, head=13)
    sc.label(C, S(bold("F"), "g") + " = −m g " + bold("j"), "PINK", "end", 18, dx=-6, dy=26)
    # reaction along the radius (towards O) and out of the plane
    Nr = (P[0] - 0.55 * eR[0], P[1] - 0.55 * eR[1])
    sc.vec(P, Nr, None, "PINK", 3.6, head=13)
    sc.label(Nr, S("N", "R") + " " + S(bold("e"), "R") + " (sign from the equations)", "PINK", "end", 16, dx=-14, dy=2)
    # velocity (not a force): dashed orange along the tangent
    tipv = (P[0] + 1.5 * eT[0], P[1] + 1.5 * eT[1])
    _dvec2(sc, P, tipv, ORANGE, 2.4, "7 4", 11)
    sc.label(tipv, "a " + dot1("θ") + " " + S(bold("e"), "θ"), ORANGE, "end", 17, dx=-12, dy=-8, weight="700")
    # polar basis
    sc.vec(P, (P[0] + 0.8 * eR[0], P[1] + 0.8 * eR[1]), None, "BLUE", 3.2, head=12)
    sc.label((P[0] + 0.8 * eR[0], P[1] + 0.8 * eR[1]), S(bold("e"), "R"), "BLUE", "middle", 18, dx=20, dy=-4)
    sc.vec(P, (P[0] + 0.8 * eT[0], P[1] + 0.8 * eT[1]), None, "BLUE", 3.2, head=12)
    sc.label((P[0] + 0.8 * eT[0], P[1] + 0.8 * eT[1]), S(bold("e"), "θ"), "BLUE", "middle", 18, dx=-18, dy=-4)
    axis_out(sc, P, None, "PINK", r_px=10)
    sc.label(P, "P", "HEAD", "end", 18, dx=-44, dy=-8)
    sc.label(P, S("N", "z") + " " + bold("k"), "PINK", "middle", 17, dx=4, dy=-52)
    sc.label(P, "free body", "HEAD", "start", 15, dx=40, dy=4, italic=False)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-simple-rotation")
def simple_rotation():
    nm = {"h0": S(bold("i"), "1"), "v0": S(bold("j"), "1"), "h1": S(bold("i"), "2"), "v1": S(bold("j"), "2")}
    return _rot_matrix_figure(nm, "θ", 30.0, "[" + S("", "1") + "R" + S("", "2") + "] =", S(bold("k"), "1") + " = " + S(bold("k"), "2"))


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-two-particles")
def two_particles():
    sc = Scene(800, 560, (230, 190), 86)
    r = 0.3
    lc = 3.2
    d, dp = 2.3, 1.9
    O, O2 = (0.0, 0.0), (lc, 0.0)
    xs, xs2 = -r, lc + r
    # pulleys and string
    pts = [(xs, -d), (xs, 0.0)]
    pts += [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in range(180, 89, -6)]
    pts += [(lc + r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in range(90, -1, -6)]
    pts += [(xs2, -dp)]
    sc.poly(pts, "HEAD", 1.7)
    sc.disk(O, r, "HEAD", "HEAD", 0.18, 2.2)
    sc.disk(O2, r, "HEAD", "HEAD", 0.18, 2.2)
    fixed_axis(sc, O, 0, 1.2, bold("i"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.15, bold("j"), off=(-12, 2))
    sc.dim((0.0, 1.55), (lc, 1.55), "ℓ" + S("", "c"), off=(0, -10), size=18)
    sc.dashed((0.0, r + 0.1), (0.0, 1.65))
    sc.dashed((lc, r + 0.1), (lc, 1.65))
    # depths
    sc.dashed((-0.4, 0.0), (-2.0, 0.0))
    sc.dashed((-0.45, -d), (-2.0, -d))
    sc.dim((-1.9, 0.0), (-1.9, -d), "d", off=(-14, 4), size=18)
    sc.dashed((lc + 0.4, 0.0), (lc + 2.0, 0.0))
    sc.dashed((lc + 0.45, -dp), (lc + 2.0, -dp))
    sc.dim((lc + 1.9, 0.0), (lc + 1.9, -dp), "d′", off=(14, 4), size=18)
    # forces (m = 1.5 m', tension 1.2 m' g)
    u = 0.85
    for x, y, wl, side, nm, mass in ((xs, -d, 1.5 * u, -1, "P", "m"), (xs2, -dp, 1.0 * u, 1, "P′", "m′")):
        sc.vec((x, y), (x, y + 1.2 * u), None, "PINK", 3.6, head=13)
        sc.vec((x, y), (x, y - wl), None, "PINK", 3.6, head=13)
        anc = "start" if side < 0 else "end"
        dx = -side * 14
        sc.label((x, y + 1.2 * u), "F" + S("", "T") + " " + bold("j"), "PINK", anc, 18, dx=dx, dy=2)
        w = "−m g " if side < 0 else "−m′ g "
        sc.label((x, y - wl), w + bold("j"), "PINK", anc, 18, dx=dx, dy=6)
        sc.dotp((x, y), 5.5)
        sc.label((x, y), nm + ", " + mass, "HEAD", anc, 18, dx=dx, dy=5)
    # velocities (not forces): dashed orange beside the string, on the outer side
    _dvec2(sc, (xs - 0.3, -d), (xs - 0.3, -d - 0.85), ORANGE, 2.4, "7 4", 11)
    sc.label((xs - 0.3, -d - 0.85), "−" + dot1("d") + " " + bold("j"), ORANGE, "end", 17, dx=-8, dy=6, weight="700")
    _dvec2(sc, (xs2 + 0.3, -dp), (xs2 + 0.3, -dp + 0.85), ORANGE, 2.4, "7 4", 11)
    sc.label((xs2 + 0.3, -dp + 0.85), dot1("d") + " " + bold("j"), ORANGE, "start", 17, dx=8, dy=-2, weight="700")
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _hatched(sc, x0, x1, y=0.0, step=0.16, ln=0.16):
    sc.line((x0, y), (x1, y), "HEAD", 3.0)
    x = x0 + 0.1
    while x < x1:
        sc.line((x, y), (x - 0.13, y - ln), "EDGE", 1.0)
        x += step


@_fig("t3-friction")
def friction():
    sc = Scene(920, 340, (460, 270), 82)
    mu = 0.4
    cone = math.degrees(math.atan(mu))
    N = 1.6
    r = 0.09
    for cx, sliding in ((-3.0, True), (3.0, False)):
        P = (cx, r)
        _hatched(sc, cx - 2.3, cx + 2.3)
        sc.vec(P, (cx, r + N), None, "PINK", 3.6, head=13)
        sc.label((cx, r + N), bold("N"), "PINK", "middle", 19, dx=14, dy=-4)
        # friction cone about the normal (dashed green)
        for sg in (-1, 1):
            a = math.radians(90 + sg * cone)
            sc.line(P, (cx + 2.1 * math.cos(a), r + 2.1 * math.sin(a)), "GREEN", 1.3, "6 4")
        if sliding:
            FR = mu * N
            sc.vec(P, (cx + 1.5, r), None, ORANGE, 3.2, head=12)
            sc.label((cx + 1.5, r), _vb("v", "1", "P") + " ≠ " + bold("0"), ORANGE, "start", 18, dx=10, dy=-10, weight="700")
            sc.vec(P, (cx - FR, r), None, "PINK", 3.6, head=13)
            sc.label((cx - FR, r), S(bold("F"), "R") + " = −μ|" + bold("N") + "|", "PINK", "end", 16, dx=-8, dy=-34)
            sc.label((cx - FR, r), _vb("v", "1", "P") + "/|" + _vb("v", "1", "P") + "|", "PINK", "end", 16, dx=-8, dy=-14)
            tot = (cx - FR, r + N)
            sc.line((cx - FR, r), tot, "PINK", 1.1, "3 3")
            sc.line((cx, r + N), tot, "PINK", 1.1, "3 3")
            _dvec2(sc, P, tot, "PINK", 2.4, "6 4", 11)
            sc.label(tot, bold("N") + " + " + S(bold("F"), "R"), "PINK", "end", 17, dx=-10, dy=-6)
            sc.arc(P, 1.0, 90, 90 + cone, "GREEN", 1.7, head=True)
            sc.label(_add(P, _d(90 + cone), 1.35), "arctan μ", "GREEN", "end", 16, dx=-16, dy=6, italic=False)
        else:
            FR = 0.2 * N
            sc.label((cx - 1.4, r), _vb("v", "1", "P") + " = " + bold("0"), "HEAD", "end", 18, dx=-4, dy=-14, weight="700")
            sc.vec(P, (cx + FR, r), None, "PINK", 3.6, head=13)
            sc.label((cx + FR, r), S(bold("F"), "R"), "PINK", "start", 19, dx=10, dy=-10)
            tot = (cx + FR, r + N)
            sc.line((cx + FR, r), tot, "PINK", 1.1, "3 3")
            sc.line((cx, r + N), tot, "PINK", 1.1, "3 3")
            _dvec2(sc, P, tot, "PINK", 2.4, "6 4", 11)
            sc.label(tot, bold("N") + " + " + S(bold("F"), "R"), "PINK", "start", 17, dx=40, dy=-6)
            sc.label((cx, 2.25), "|" + S(bold("F"), "R") + "| ≤ μ|" + bold("N") + "|,", "HEAD", "middle", 15, dy=-18, italic=False)
            sc.label((cx, 2.25), "direction in V" + S("", "T") + " unknown", "HEAD", "middle", 15, dy=0, italic=False)
        sc.dotp(P, 7.0)
        sc.label(P, "P", "HEAD", "middle", 18, dx=-18, dy=-14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-rough-cylinder")
def rough_cylinder():
    sc = Scene(980, 520, (480, 360), 84)
    a, H = 1.35, 2.7
    th, ps = math.radians(40), math.radians(25)
    z = 1.08
    # ---- left: axonometric view ----
    off = (-3.1, -0.3)
    ring = lambda zz, n=90: [(a * math.cos(2 * math.pi * i / n), a * math.sin(2 * math.pi * i / n), zz) for i in range(n + 1)]
    cloud = [P3(p) for p in ring(0.0) + ring(H)]
    sc.poly([(off[0] + x, off[1] + y) for x, y in _hull(cloud)], "HEAD", 1.4, fill="EDGE", close=True, opacity=0.16)
    _pts(sc, ring(0.0), off, "HEAD", 1.0, "5 4")
    _pts(sc, ring(H), off, "HEAD", 1.0)
    O = (0.0, 0.0, 0.0)
    for v, nm, lab in (((1.0, 0, 0), "x", (-12, 12)), ((0, 2.1, 0), "y", (14, 6)), ((0, 0, H + 0.6), "z", (-4, -10))):
        _V(sc, O, v, None, "EDGE", 1.4, off, head=8)
        sc.label(_q(v, off), nm, "TEXT", "middle", 17, weight="700", dx=lab[0], dy=lab[1])
    _dp(sc, O, off, 3.6)
    sc.label(_q(O, off), "O", "HEAD", "end", 17, dx=-8, dy=-4)
    eR = (math.cos(th), math.sin(th), 0.0)
    eT = (-math.sin(th), math.cos(th), 0.0)
    eZ = (0.0, 0.0, 1.0)
    P = _lin((a, eR), (z, eZ))
    base = _lin((a, eR))
    _L(sc, P, base, off, "HEAD", 1.2, "5 4")
    _L(sc, O, (0.0, 0.0, z), off, "HEAD", 1.0, "3 3")
    sc.label(_q(_v3(base, (0, 0, z / 2)), off), "z", "HEAD", "start", 17, dx=8, dy=6)
    # helix piece and velocity
    helix = [_lin((a, (math.cos(th + s * math.cos(ps) / a), math.sin(th + s * math.cos(ps) / a), 0.0)), (z + s * math.sin(ps), eZ))
             for s in [-1.8 + 3.7 * i / 60 for i in range(61)]]
    _pts(sc, helix, off, DRED, 1.8, "6 4")
    v = _lin((math.cos(ps), eT), (math.sin(ps), eZ))
    _V(sc, P, _mul(v, 1.5), None, ORANGE, 3.4, off, head=13)
    sc.label(_q(_v3(P, v, 1.5), off), _vb("v", "0", "P"), ORANGE, "start", 18, dx=12, dy=-4, weight="700")
    m = _arc_at(sc, P, eT, v, 0.55, off, "GREEN", True, 1.8)
    sc.label(m, "ψ", "GREEN", "middle", 17, dx=24, dy=0)
    _V(sc, P, _mul(eR, 0.8), None, "BLUE", 3.0, off, head=12)
    sc.label(_q(_v3(P, eR, 0.8), off), S(bold("e"), "R"), "BLUE", "start", 17, weight="700", dx=8, dy=14)
    _V(sc, P, _mul(eT, 0.8), None, "BLUE", 3.0, off, head=12)
    sc.label(_q(_v3(P, eT, 0.8), off), S(bold("e"), "θ"), "BLUE", "start", 17, weight="700", dx=6, dy=18)
    _V(sc, P, _mul(eZ, 0.8), None, "BLUE", 3.0, off, head=12)
    sc.label(_q(_v3(P, eZ, 0.8), off), S(bold("e"), "z"), "BLUE", "middle", 17, weight="700", dx=-14, dy=-6)
    # reaction (inner face) and friction opposite to the velocity
    _V(sc, P, _mul(eR, -1.2), None, "PINK", 3.6, off, head=13)
    sc.label(_q(_v3(P, eR, -1.2), off), S("N", "R") + " " + S(bold("e"), "R"), "PINK", "end", 17, dx=-10, dy=-2)
    _V(sc, P, _mul(v, -1.2), None, "PINK", 3.6, off, head=13)
    sc.label(_q(_v3(P, v, -1.2), off), S(bold("F"), "R"), "PINK", "end", 18, dx=-10, dy=8)
    _dp(sc, P, off, 5.2)
    sc.label(_q(P, off), "P", "HEAD", "middle", 18, dx=-14, dy=26)
    # ---- right: view along k (out of the paper) ----
    c0 = (3.4, 1.3)
    sc.curve(lambda t: (c0[0] + a * math.cos(t), c0[1] + a * math.sin(t)), 0, 2 * math.pi, 120, DRED, 2.6)
    fixed_axis(sc, c0, 0, a + 0.8, bold("i"), off=(12, 6))
    fixed_axis(sc, c0, 90, a + 0.8, bold("j"), off=(-12, 2))
    axis_out(sc, c0, None, "HEAD", r_px=9)
    sc.label(c0, bold("k"), "HEAD", "end", 17, dx=-14, dy=26)
    sc.label(c0, "O", "HEAD", "start", 17, dx=12, dy=24)
    Pr = (c0[0] + a * math.cos(th), c0[1] + a * math.sin(th))
    sc.line(c0, Pr, "HEAD", 1.4)
    sc.arc(c0, 0.6, 0, 40, "GREEN", 1.8, head=True)
    sc.label(_add(c0, _d(20), 0.95), "θ", "GREEN", "middle", 18, dy=5)
    e1 = (math.cos(th), math.sin(th))
    e2 = (-math.sin(th), math.cos(th))
    sc.vec(Pr, (Pr[0] + 0.7 * e1[0], Pr[1] + 0.7 * e1[1]), None, "BLUE", 3.0, head=12)
    sc.label((Pr[0] + 0.7 * e1[0], Pr[1] + 0.7 * e1[1]), S(bold("e"), "R"), "BLUE", "start", 17, weight="700", dx=8, dy=6)
    sc.vec(Pr, (Pr[0] + 0.7 * e2[0], Pr[1] + 0.7 * e2[1]), None, "BLUE", 3.0, head=12)
    sc.label((Pr[0] + 0.7 * e2[0], Pr[1] + 0.7 * e2[1]), S(bold("e"), "θ"), "BLUE", "end", 17, weight="700", dx=-8, dy=-8)
    _dvec2(sc, Pr, (Pr[0], Pr[1] + 0.8), "EDGE", 1.6, "5 4", 9)
    sc.arc(Pr, 0.45, 90, 90 + 40, "GREEN", 1.8, head=True)
    sc.label(_add(Pr, _d(90 + 20), 0.78), "θ", "GREEN", "middle", 18, dx=-4, dy=-2)
    sc.dotp(Pr, 5.2)
    sc.label(Pr, "P", "HEAD", "middle", 18, dx=18, dy=22)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t3-region-existence")
def region_existence():
    sc = Scene(1000, 400, (590, 255), 76)
    X = 1.4                        # world units per radian
    Y = 1.3                        # world units per unit of g/a
    lo, hi = -1.5 * math.pi, 0.5 * math.pi
    xl, xr = lo * X, hi * X
    ybot, ytop = -1.3 * Y, 1.75 * Y
    # forbidden parts (curve above the level aK/g = 0.5): light grey bands
    for a0, a1 in ((lo, -7 * math.pi / 6), (math.pi / 6, hi)):
        x0, x1 = a0 * X, a1 * X
        sc.poly([(x0, ybot), (x1, ybot), (x1, ytop), (x0, ytop)], "EDGE", 0.0, fill="EDGE", close=True, opacity=0.16)
    # axes
    sc.vec((xl, 0.0), (xr + 0.45, 0.0), None, "EDGE", 1.5, head=9)
    sc.label((xr + 0.45, 0.0), "θ", "TEXT", "middle", 18, weight="700", dx=14, dy=6)
    sc.vec((xl, ybot), (xl, ytop + 0.25), None, "EDGE", 1.5, head=9)
    sc.label((xl, ytop + 0.25), "(g/a) sin θ", "TEXT", "start", 17, dx=-30, dy=-10)
    for k, nm in ((-3, "−3π/2"), (-2, "−π"), (-1, "−π/2"), (0, "0"), (1, "π/2")):
        th = {-3: -1.5 * math.pi, -2: -math.pi, -1: -0.5 * math.pi, 0: 0.0, 1: 0.5 * math.pi}[k]
        sc.line((th * X, -0.06), (th * X, 0.06), "HEAD", 1.4)
        sc.label((th * X, 0.0), nm, "HEAD", "middle", 15, dx=22 if k == -3 else 0, dy=22, italic=False)
    for v in (-1, 0, 1):
        sc.line((xl - 0.06, v * Y), (xl + 0.06, v * Y), "HEAD", 1.4)
        sc.label((xl, v * Y), str(v).replace("-", "−"), "HEAD", "end", 15, dx=-10, dy=5, italic=False)
    # energy levels
    def level(val, col, w, dash, name, sub):
        sc.line((xl, val * Y), (xr + 0.25, val * Y), col, w, dash)
        sc.label((xr + 0.45, val * Y), name, "BLUE", "start", 16, dy=-2, italic=False)
        sc.label((xr + 0.45, val * Y), sub, "BLUE", "start", 14, dy=15, italic=False)
    level(1.4, "BLUE", 1.7, "7 4", "revolutions", "aK/g = 1.4")
    level(1.0, "BLUE", 1.3, "2 3", "separatrix", "aK/g = 1")
    level(0.5, "BLUE", 1.7, "7 4", "oscillation", "aK/g = 0.5")
    level(-1.0, "BLUE", 1.7, "7 4", "rest at the bottom", "aK/g = −1")
    # the effective potential
    n = 240
    sc.poly([((lo + (hi - lo) * i / n) * X, math.sin(lo + (hi - lo) * i / n) * Y) for i in range(n + 1)], "HEAD", 3.0)
    # turning angles of the oscillation
    for th in (-7 * math.pi / 6, math.pi / 6):
        sc.line((th * X, 0.5 * Y), (th * X, -0.32), "BLUE", 1.2, "4 3")
        sc.dotp((th * X, 0.5 * Y), 5.0, "BLUE")
        sc.label((th * X, -0.32), "θ" + S("", "*"), "BLUE", "middle", 17, dy=16)
    sc.dotp((-0.5 * math.pi * X, -1.0 * Y), 5.0, "BLUE")
    return sc
