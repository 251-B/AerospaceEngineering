"""Theory figures of Topic 1, Chapter 1 (Vectors, Rotations and Simple Rotations): Sections 1 to 8 of Notes.pdf."""
import math

from figures.em_theory import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head, poly as _poly, rect as _rect

def dot1(ch):
    """Letter with a proper overdot: a raised full stop centred over the glyph (the combining U+0307 renders after it)."""
    return (ch + '<tspan dx="-0.38em" dy="-0.80em" font-style="normal">.</tspan>'
            '<tspan dx="0.13em" dy="0.80em" font-style="normal">\u200b</tspan>')


ORANGE = "ACC"
DRED = "#be123c"          # second colour: products, angular velocity, small changes
NAVY = "#1e3a8a"          # second rotated basis (two successive rotations)
MINUS = "−"


def _d(deg):
    return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def _add(p, q, k=1.0):
    return (p[0] + k * q[0], p[1] + k * q[1])


# --------------------------------------------------------------------------------------------------------------------
# 3D sketch convention of the portal: x towards the viewer (down-left), y to the right, z up (cabinet projection)
EX = (-0.473, -0.368)


def P3(v):
    return (v[0] * EX[0] + v[1], v[0] * EX[1] + v[2])


def _v3(a, b, k=1.0):
    return (a[0] + k * b[0], a[1] + k * b[1], a[2] + k * b[2])


def _mul(v, k):
    return (v[0] * k, v[1] * k, v[2] * k)


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _unit3(v):
    n = math.sqrt(_dot(v, v))
    return (v[0] / n, v[1] / n, v[2] / n)


def _vec3(sc, o, v, name=None, col="BLUE", w=2.0, off=(8, -8), size=16, head=9):
    sc.vec(P3(o), P3(_v3(o, v)), name, col, w, name_off=off, size=size, head=head)


def _line3(sc, a, b, col="EDGE", w=1.1, dash="5 4"):
    sc.line(P3(a), P3(b), col, w, dash)


def _poly3(sc, pts, col="EDGE", w=1.4, dash=None, fill="none", close=False, opacity=None):
    sc.poly([P3(p) for p in pts], col, w, dash, fill, close, opacity)


def _arc3(sc, u, v, r, col="GREEN", head=False, w=1.6, n=28):
    """Arc of radius r between the directions u and v (3D) about the origin; returns the projected midpoint."""
    u, v = _unit3(u), _unit3(v)
    a = math.acos(max(-1.0, min(1.0, _dot(u, v))))
    pts = []
    for i in range(n + 1):
        t = i / n
        p = _v3(_mul(u, math.sin((1 - t) * a)), _mul(v, math.sin(t * a)))
        pts.append(_mul(p, r / math.sin(a)))
    px = [P3(p) for p in pts]
    sc.poly(px, col, w)
    if head:
        arrow_head(sc.c, sc.P(px[-3]), sc.P(px[-1]), col, 9)
    return px[n // 2]


def _circ3(sc, c, e1, e2, r, a0, a1, col="GREEN", head=False, w=1.6, dash=None, n=60):
    """Circle arc about the 3D centre c in the plane of e1, e2 (unit vectors), from angle a0 to a1 (degrees)."""
    pts = []
    for i in range(n + 1):
        f = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(P3(_v3(c, _v3(_mul(e1, r * math.cos(f)), _mul(e2, r * math.sin(f))))))
    sc.poly(pts, col, w, dash)
    if head:
        arrow_head(sc.c, sc.P(pts[-3]), sc.P(pts[-1]), col, 9)
    return pts


def _push(p, q, k):
    """Point p moved away from the point q by k world units (for labels placed outside an arc)."""
    dx, dy = p[0] - q[0], p[1] - q[1]
    n = math.hypot(dx, dy) or 1.0
    return (p[0] + k * dx / n, p[1] + k * dy / n)


def _pl(sc, X, Y, s, col="HEAD", anchor="middle", size=15, weight="400", italic=False):
    """Label at a pixel position (the scene origin is the reference of the shifts)."""
    sc.label((0.0, 0.0), s, col, anchor, size, italic=italic, weight=weight, dx=X - sc.o[0], dy=Y - sc.o[1])


def _R(sub0, sub1, extra):
    return "[" + S("", sub0) + "R" + S("", sub1) + "(" + extra + ")]"


def _matrix(sc, X, Y, title, rows, cw=76, rh=27, size=16):
    """Boxed 3x3 matrix with its title; (X, Y) is the pixel of the top-left corner of the box."""
    pad = 16
    W = 3 * cw + 2 * pad
    H = 44 + 3 * rh + 12
    _rect(sc.c, X, Y, W, H, "EDGE", 1.2, rx=8)
    _pl(sc, X + W / 2, Y + 26, title, "HEAD", "middle", 17, "400", True)
    top = Y + 44
    x0, x1 = X + pad - 4, X + pad + 3 * cw + 4
    for xb, sgn in ((x0, 1), (x1, -1)):
        _poly(sc.c, [(xb + sgn * 6, top), (xb, top), (xb, top + 3 * rh), (xb + sgn * 6, top + 3 * rh)], "HEAD", 1.6)
    for r, row in enumerate(rows):
        for c, s in enumerate(row):
            _pl(sc, X + pad + (c + 0.5) * cw, top + r * rh + 0.72 * rh, s, "HEAD", "middle", size)
    return (X, Y, W, H)


def _cs(f, a):
    return f + " θ" + S("", a)


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-basis-components",
        "A vector A in the first octant with its three components drawn as the edges of a dashed box along the axes of an "
        "orthonormal right-handed basis.",
        r"Orthonormal right-handed basis $\{\mathbf i,\mathbf j,\mathbf k\}$ and the components of $\mathbf A$ in it "
        r"(Notes.pdf Fig. 1.1).")
def basis_components():
    sc = Scene(560, 445, (150, 345), 62)
    O = (0.0, 0.0, 0.0)
    A = (2.0, 3.0, 2.5)
    # thin grey axes
    for v, nm, off in (((3.3, 0, 0), "x", (-10, 14)), ((0, 4.5, 0), "y", (14, 6)), ((0, 0, 4.0), "z", (-4, -10))):
        _vec3(sc, O, v, None, "EDGE", 1.3, head=8)
        sc.label(P3(v), nm, "TEXT", "middle", 17, weight="700", dx=off[0], dy=off[1])
    # dashed box (the three edges from O are the component vectors)
    cs = [(a, b, c) for a in (0, A[0]) for b in (0, A[1]) for c in (0, A[2])]
    for p in cs:
        for q in cs:
            diff = [i for i in range(3) if p[i] != q[i]]
            if len(diff) == 1 and p[diff[0]] == 0 and (p != (0, 0, 0)) and (q != (0, 0, 0)):
                _line3(sc, p, q, "EDGE", 1.1)
    _line3(sc, O, (A[0], A[1], 0), "EDGE", 1.3, "7 4")                       # projection of A on Oxy
    # components (thin orange), then the unit vectors (thick grey) on top
    _vec3(sc, O, (A[0], 0, 0), None, ORANGE, 2.0, head=9)
    _vec3(sc, O, (0, A[1], 0), None, ORANGE, 2.0, head=9)
    _vec3(sc, O, (0, 0, A[2]), None, ORANGE, 2.0, head=9)
    sc.label(P3((A[0], 0, 0)), S("A", "x") + bold("i"), ORANGE, "end", 16, dx=-10, dy=14)
    sc.label(P3((0, A[1], 0)), S("A", "y") + bold("j"), ORANGE, "middle", 16, dx=4, dy=22)
    sc.label(P3((0, 0, A[2])), S("A", "z") + bold("k"), ORANGE, "end", 16, dx=-12, dy=5)
    for v, nm, off in (((1, 0, 0), "i", (-12, 12)), ((0, 1, 0), "j", (6, 20)), ((0, 0, 1), "k", (-12, 4))):
        _vec3(sc, O, v, bold(nm), "HEAD", 3.0, off=off, size=17, head=11)
    _vec3(sc, O, A, bold("A"), ORANGE, 3.2, off=(14, -8), size=18, head=11)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=-6)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-known-angle",
        "A vector in the plane Oxy forming the angle theta with Ox and beta with Oy, with the right triangle of its two "
        "components.",
        r"Components of a vector with a known angle: the cosine goes with the leg adjacent to the given angle, $\theta$ "
        r"from $Ox$ or $\beta$ from $Oy$ (Notes.pdf Fig. 1.2).")
def known_angle():
    sc = Scene(620, 410, (80, 350), 78)
    O = (0.0, 0.0)
    TH, LA = 35.0, 4.0
    c, s = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    tip = (LA * c, LA * s)
    F = (LA * c, 0.0)
    triangle(sc, [O, F, tip], ORANGE, 0.18)
    fixed_axis(sc, O, 0, 5.0, "x", off=(14, 6))
    fixed_axis(sc, O, 90, 3.75, "y", off=(14, 4))
    sc.dashed(F, tip)
    right_angle(sc, F, 180, 90, 0.12)
    sc.vec(O, (1, 0), bold("i"), "HEAD", 3.0, name_off=(-4, 22), size=17, head=11)
    sc.vec(O, (0, 1), bold("j"), "HEAD", 3.0, name_off=(-14, 4), size=17, head=11)
    sc.vec(O, tip, bold("A"), ORANGE, 3.2, name_off=(16, -6), size=18, head=11)
    # green arcs
    sc.arc(O, 1.3, 0, TH, "GREEN", 1.6, head=True)
    sc.label(_add(O, _d(TH / 2 - 1), 1.62), "θ", "GREEN", "middle", 17, dy=5)
    sc.arc(O, 1.9, 90, TH, "GREEN", 1.6, head=True)
    sc.label(_add(O, _d(70), 2.2), "β (from Oy)", "GREEN", "start", 17, dx=-6, dy=-2)
    # leg labels
    sc.label((LA * c / 2, 0), S("A", "x") + " = A cos θ  (adjacent to θ)", "HEAD", "middle", 16, dy=50)
    sc.label(F, S("A", "y") + " = A sin θ", "HEAD", "start", 16, dx=12, dy=-34)
    sc.label(F, "(opposite to θ)", "TEXT", "start", 15, dx=12, dy=-14, italic=False)
    sc.label((LA * c / 2, LA * s / 2), "A", "ACC", "middle", 18, dx=14, dy=26)
    sc.label((LA * c, 0), "F", "HEAD", "middle", 17, dx=12, dy=18)
    axis_out(sc, O, bold("k"), "HEAD", off=(-18, 24))
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _rot2d(sc, O, L, th, n, thn, minus, ra, rb, tri_h=True, tri_v=True, col="BLUE", tcol="HEAD", sz=15,
           lab=(0, 0), fixed_len=1.2):
    """One simple-rotation view: grey axes h0, v0, rotated axes h1, v1 (blue), arcs of the angle and the two shaded triangles.

    `n` holds the bold names h0, v0, h1, v1; `thn` is the angle name; `minus` the label of the leg along -h0 of v1."""
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    fixed_axis(sc, O, 0, L * fixed_len, n["h0"], off=(18, 6))
    fixed_axis(sc, O, 90, L * fixed_len, n["v0"], off=(16, 4))
    cosl, sinl = "cos " + thn, "sin " + thn
    if tri_h:
        foot, tip = (O[0] + L * c, O[1]), (O[0] + L * c, O[1] + L * s)
        triangle(sc, [O, foot, tip], ORANGE, 0.18)
        sc.dashed(foot, tip)
        right_angle(sc, foot, 180, 90, 0.08)
        sc.label((O[0] + L * c / 2, O[1]), cosl, "HEAD", "middle", sz + 1, dy=22)
        sc.label((O[0] + L * c, O[1] + L * s / 2), sinl, "HEAD", "start", sz + 1, dx=9, dy=5)
    if tri_v:
        foot, tip = (O[0], O[1] + L * c), (O[0] - L * s, O[1] + L * c)
        triangle(sc, [O, foot, tip], ORANGE, 0.18)
        sc.dashed(foot, tip)
        right_angle(sc, foot, 270, 180, 0.08)
        sc.label((O[0], O[1] + L * c / 2), cosl, "HEAD", "start", sz + 1, dx=10, dy=5)
        sc.label((O[0] - L * s / 2, O[1] + L * c), minus, "HEAD", "middle", sz + 1, dx=-4, dy=-10)
    # rotated basis (blue) with its names
    for deg, nm, off in ((th, n["h1"], (22, -8)), (th + 90, n["v1"], (-24, 4))):
        tipp = (O[0] + L * math.cos(math.radians(deg)), O[1] + L * math.sin(math.radians(deg)))
        sc.vec(O, tipp, None, col, 2.6, head=11)
        sc.label(tipp, nm, tcol, "middle", 17, weight="700", dx=off[0], dy=off[1])
    # green arcs of clearly different radii
    sc.arc(O, ra, 0, th, "GREEN", 1.6, head=True)
    sc.label(_add(O, _d(th / 2), ra + 0.34), thn, "GREEN", "middle", 17, dy=5)
    sc.arc(O, rb, 90, 90 + th, "GREEN", 1.6, head=True)
    sc.label(_add(O, _d(90 + th / 2), rb + 0.34), thn, "GREEN", "middle", 17, dy=5)


def _rot_figure(h0, v0, h1, v1, thn, minus, axis_name, th, rows, title):
    sc = Scene(740, 350, (170, 295), 88)
    O = (0.0, 0.0)
    _rot2d(sc, O, 2.2, th, {"h0": h0, "v0": v0, "h1": h1, "v1": v1}, thn, minus, 0.9, 1.3)
    axis_out(sc, O, axis_name, "HEAD", off=(-48, 28))
    sc.dotp(O, 2.0, "HEAD")
    _matrix(sc, 445, 70, title, rows)
    return sc


@figure("t1-rotation-x",
        "View down the x axis of a simple rotation by theta x, with the rotated y and z unit vectors, their projection "
        "triangles and the rotation matrix.",
        r"Simple rotation about $\mathbf i_0$, seen with $\mathbf i_0$ out of the paper: $\mathbf k_1$ leans towards "
        r"$-\mathbf j_0$, which puts the minus sign in entry $(2,3)$ (Notes.pdf Fig. 1.3).")
def rotation_x():
    t = "θ" + S("", "x")
    ss, cc = _cs("sin", "x"), _cs("cos", "x")
    return _rot_figure(bold("j") + S("", "0"), bold("k") + S("", "0"), bold("j") + S("", "1"), bold("k") + S("", "1"), t,
                       MINUS + ss + " " + bold("j") + S("", "0"), bold("i") + S("", "0") + " ≡ " + bold("i") + S("", "1"), 30.0,
                       [["1", "0", "0"], ["0", cc, MINUS + ss], ["0", ss, cc]], _R("0", "1", "x, " + t))


@figure("t1-rotation-y",
        "View down the y axis of a simple rotation by theta y, with k to the right and x up, the rotated unit vectors, "
        "their projection triangles and the rotation matrix.",
        r"Simple rotation about $\mathbf j_0$, seen with $\mathbf j_0$ out of the paper: the right-handed pair is "
        r"$(\mathbf k_0, \mathbf i_0)$, so $\mathbf i_1$ leans towards $-\mathbf k_0$ and the minus sign falls in entry "
        r"$(3,1)$ (Notes.pdf Fig. 1.3).")
def rotation_y():
    t = "θ" + S("", "y")
    ss, cc = _cs("sin", "y"), _cs("cos", "y")
    i0, j0, k0 = (bold(c) + S("", "0") for c in "ijk")
    i1, j1, k1 = (bold(c) + S("", "1") for c in "ijk")
    sc = Scene(740, 470, (170, 295), 88)
    O = (0.0, 0.0)
    _rot2d(sc, O, 2.2, 30.0, {"h0": k0, "v0": i0, "h1": k1, "v1": i1}, t, MINUS + ss + " " + k0, 0.9, 1.3)
    axis_out(sc, O, j0 + " ≡ " + j1, "HEAD", off=(-48, 28))
    sc.dotp(O, 2.0, "HEAD")
    _matrix(sc, 445, 30, _R("0", "1", "y, " + t), [[cc, "0", ss], ["0", "1", "0"], [MINUS + ss, "0", cc]])
    # inset: the same plane drawn with i0 to the right and k0 up; j0 points into the paper
    C = (4.5, -0.55)
    Lc = 1.05
    fixed_axis(sc, C, 0, Lc * 1.18, i0, off=(18, 6))
    fixed_axis(sc, C, 90, Lc * 1.18, k0, off=(16, 4))
    for deg, nm, off in ((-30.0, i1, (4, 20)), (60.0, k1, (18, -8))):
        tip = _add(C, _d(deg), Lc)
        sc.vec(C, tip, None, "BLUE", 2.4, head=10)
        sc.label(tip, nm, "BLUE", "middle", 16, weight="700", dx=off[0], dy=off[1])
    sc.arc(C, 0.55, 0, -30, "GREEN", 1.6, head=True)
    sc.label(_add(C, _d(-12), 0.9), t, "GREEN", "middle", 15, dy=5)
    axis_in(sc, C, None, "HEAD", r_px=8)
    sc.label((4.5, -1.7), "same rotation, " + j0 + " into the paper", "TEXT", "middle", 14, italic=False, dy=0)
    return sc


@figure("t1-rotation-z",
        "View down the z axis of a simple rotation by theta z, with the rotated x and y unit vectors, their projection "
        "triangles and the rotation matrix.",
        r"Simple rotation about $\mathbf k_0$, seen with $\mathbf k_0$ out of the paper: $\mathbf j_1$ leans towards "
        r"$-\mathbf i_0$, the minus sign of entry $(1,2)$ (Notes.pdf Fig. 1.3).")
def rotation_z():
    t = "θ" + S("", "z")
    ss, cc = _cs("sin", "z"), _cs("cos", "z")
    i0, j0, k0 = (bold(c) + S("", "0") for c in "ijk")
    i1, j1, k1 = (bold(c) + S("", "1") for c in "ijk")
    return _rot_figure(i0, j0, i1, j1, t, MINUS + ss + " " + i0, k0 + " ≡ " + k1, 30.0,
                       [[cc, MINUS + ss, "0"], [ss, cc, "0"], ["0", "0", "1"]], _R("0", "1", "z, " + t))


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-two-rotations",
        "Two successive simple rotations, about k0 by theta z and then about i1 by theta x, each in its own view with its "
        "matrix, and the resulting tilted unit vector k2.",
        r"A direction reached by two simple rotations: one 2D view per rotation, each with its own matrix; $\mathbf k_2$ is "
        r"tilted by $\theta_x$ from $\mathbf k_0$ towards $-\mathbf j_1$.")
def two_rotations():
    sc = Scene(960, 480, (130, 265), 70)
    tz, tx = 40.0, 30.0
    tzn, txn = "θ" + S("", "z"), "θ" + S("", "x")
    i0, j0, k0 = (bold(c) + S("", "0") for c in "ijk")
    i1, j1, k1 = (bold(c) + S("", "1") for c in "ijk")
    i2, j2, k2 = (bold(c) + S("", "2") for c in "ijk")
    # panel 1: plane Oxy, k0 = k1 out of the paper
    O1 = (0.0, 0.0)
    _rot2d(sc, O1, 1.8, tz, {"h0": i0, "v0": j0, "h1": i1, "v1": j1}, tzn, MINUS + _cs("sin", "z") + " " + i0, 0.62, 0.98, tri_h=True, tri_v=True, sz=14)
    axis_out(sc, O1, k0 + " ≡ " + k1, "HEAD", off=(-48, 28))
    sc.dotp(O1, 2.0, "HEAD")
    _pl(sc, 20, 24, "first rotation, about " + k0, "TEXT", "start", 13)
    cz, sz_ = _cs("cos", "z"), _cs("sin", "z")
    _matrix(sc, 20, 330, _R("0", "1", "z, " + tzn), [[cz, MINUS + sz_, "0"], [sz_, cz, "0"], ["0", "0", "1"]], cw=72, size=15)
    # panel 2: plane normal to i1, i1 = i2 out of the paper, j1 right, k1 up
    O2 = (4.2, 0.0)
    _rot2d(sc, O2, 1.8, tx, {"h0": j1, "v0": k1, "h1": j2, "v1": k2}, txn, MINUS + _cs("sin", "x") + " " + j1, 0.62, 0.98,
           tri_h=False, tri_v=True, col=NAVY, tcol="HEAD", sz=14)
    axis_out(sc, O2, i1 + " ≡ " + i2, "HEAD", off=(-48, 28))
    sc.dotp(O2, 2.0, "HEAD")
    _pl(sc, 310, 24, "second rotation, about " + i1, "TEXT", "start", 13)
    cx, sx = _cs("cos", "x"), _cs("sin", "x")
    _matrix(sc, 310, 330, _R("1", "2", "x, " + txn), [["1", "0", "0"], ["0", cx, MINUS + sx], ["0", sx, cx]], cw=72, size=15)
    # panel 3: axonometric sketch
    O3 = (8.3, -0.15)
    z, y, x = (0, 0, 1), (0, 1, 0), (1, 0, 0)
    cz_, sz2 = math.cos(math.radians(tz)), math.sin(math.radians(tz))
    cx_, sx2 = math.cos(math.radians(tx)), math.sin(math.radians(tx))
    i1v = (cz_, sz2, 0.0)
    j1v = (-sz2, cz_, 0.0)
    for v, nm, off in (((2.6, 0, 0), i0, (-12, 14)), ((0, 2.7, 0), j0, (14, 6)), ((0, 0, 2.7), k0, (-4, -10))):
        sc.vec(_add(O3, P3((0, 0, 0))), _add(O3, P3(v)), None, "EDGE", 1.3, head=8)
        sc.label(_add(O3, P3(v)), nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # blue line of i1 in the horizontal plane
    a, b = _add(O3, P3(_mul(i1v, -0.5))), _add(O3, P3(_mul(i1v, 2.3)))
    sc.line(a, b, "BLUE", 1.8)
    sc.label(b, i1, "BLUE", "middle", 16, weight="700", dx=14, dy=-4)
    # k2: tilted from k0 by theta_x towards -j1
    k2v = _v3(_mul(z, cx_), _mul(j1v, -sx2))
    L2 = 2.2
    n_ = _mul(j1v, -1.0)
    foot3 = _mul(n_, L2 * sx2)
    tip3 = _mul(k2v, L2)
    sc.line(_add(O3, P3((0, 0, 0))), _add(O3, P3(foot3)), "EDGE", 1.3, "5 4")
    sc.line(_add(O3, P3(foot3)), _add(O3, P3(tip3)), "EDGE", 1.3, "5 4")
    sc.vec(_add(O3, P3((0, 0, 0))), _add(O3, P3(tip3)), None, NAVY, 3.0, head=11)
    sc.label(_add(O3, P3(tip3)), k2, "HEAD", "middle", 17, weight="700", dx=18, dy=-6)
    sc.label(_add(O3, P3(_mul(foot3, 0.5))), "sin " + txn, "HEAD", "middle", 15, dx=12, dy=22)
    _circ3(_Scene3(sc, O3), (0, 0, 0), z, n_, 1.15, 0, tx, "GREEN", head=False)
    mid = _circ3_mid(O3, z, n_, 1.5, tx / 2)
    sc.label(mid, txn, "GREEN", "middle", 16, dx=10, dy=-2)
    sc.dotp(_add(O3, P3((0, 0, 0))), 3.5)
    _pl(sc, 610, 24, "result of the two rotations", "TEXT", "start", 13)
    return sc


class _Scene3:
    """Adapter that draws 3D arcs of `_circ3` around a shifted origin (panel 3 of the two-rotations figure)."""

    def __init__(self, sc, shift):
        self._sc, self._shift = sc, shift
        self.c = sc.c
        self.P = lambda p: sc.P(_add(shift, p))

    def poly(self, pts, col, w, dash=None, *a, **k):
        self._sc.poly([_add(self._shift, p) for p in pts], col, w, dash)


def _circ3_mid(shift, e1, e2, r, a):
    f = math.radians(a)
    return _add(shift, P3(_v3(_mul(e1, r * math.cos(f)), _mul(e2, r * math.sin(f)))))


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-dot-product",
        "Two vectors from a common origin with the projection of A on the direction of B as the adjacent leg of a right "
        "triangle.",
        r"The dot product with a unit vector is the projection on its direction, $A\cos\theta_{AB}$.")
def dot_product():
    sc = Scene(600, 330, (70, 255), 100)
    O = (0.0, 0.0)
    TH = 40.0
    c, s = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    A = (3.0 * c, 3.0 * s)
    B = (4.0, 0.0)
    F = (A[0], 0.0)
    triangle(sc, [O, F, A], ORANGE, 0.20)
    sc.vec(O, B, bold("B"), ORANGE, 3.0, name_off=(16, 6), size=18, head=11)
    sc.vec(O, A, bold("A"), ORANGE, 3.0, name_off=(14, -10), size=18, head=11)
    sc.dashed(F, A)
    right_angle(sc, F, 180, 90, 0.11)
    sc.vec(O, (1.0, 0.0), bold("e") + S("", "B"), "BLUE", 3.8, name_off=(2, 25), size=17, head=11)
    sc.arc(O, 0.62, 0, TH, "GREEN", 1.6)
    sc.label(_d(TH / 2 + 2), "θ" + S("", "AB"), "GREEN", "start", 16, dx=18, dy=4)
    sc.label((A[0] / 2 + 0.2, 0.0), "A cos θ" + S("", "AB") + " = " + bold("A") + "·" + bold("e") + S("", "B"), "HEAD", "middle", 16, dy=52)
    sc.label((A[0] / 2, A[1] / 2), "A", "ACC", "middle", 17, dx=-14, dy=-8)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=6)
    sc.dotp(F, 3.0)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-direction-angles",
        "A unit vector e along a line through the origin and its three direction angles alpha, beta and gamma with the "
        "basis vectors.",
        r"Direction angles $\alpha$, $\beta$, $\gamma$ of a unit vector, each between $0$ and $\pi$; their cosines are the "
        r"components of $\mathbf e$ (Notes.pdf Fig. 1.4).")
def direction_angles():
    global EX
    saved, EX = EX, (-0.66, -0.20)      # the usual view is edge-on to the plane of i and e: tilt it so that alpha curves
    try:
        return _direction_angles()
    finally:
        EX = saved


def _direction_angles():
    sc = Scene(640, 450, (245, 322), 78)
    U = 2.4
    O = (0.0, 0.0, 0.0)
    e = _unit3((0.5, 0.6, 0.62))
    for v, nm, off in (((1.5 * U, 0, 0), "x", (-10, 14)), ((0, 1.65 * U, 0), "y", (14, 6)), ((0, 0, 1.45 * U), "z", (-4, -10))):
        _vec3(sc, O, v, None, "EDGE", 1.3, head=8)
        sc.label(P3(v), nm, "TEXT", "middle", 17, weight="700", dx=off[0], dy=off[1])
    # the line r through O
    sc.line(P3(_mul(e, -0.55 * U)), P3(_mul(e, 1.55 * U)), "TEXT", 1.3)
    sc.label(P3(_mul(e, 1.55 * U)), "r", "TEXT", "middle", 18, dx=-10, dy=-8)
    for v, nm, off in (((1, 0, 0), "i", (-12, 12)), ((0, 1, 0), "j", (8, 20)), ((0, 0, 1), "k", (-12, 4))):
        _vec3(sc, O, _mul(v, U), bold(nm), "HEAD", 3.0, off=off, size=17, head=11)
    _vec3(sc, O, _mul(e, U), bold("e"), ORANGE, 3.4, off=(14, -6), size=18, head=12)
    for v, nm, r, dxy in (((1, 0, 0), "α", 2.0, (-14, -10)), ((0, 1, 0), "β", 1.0, (14, 8)), ((0, 0, 1), "γ", 1.4, (-4, -22))):
        mid = _arc3(sc, v, e, r, "GREEN")
        sc.label(mid, nm, "GREEN", "middle", 17, dx=dxy[0], dy=dxy[1])
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=-8)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-cross-product",
        "Two vectors spanning a parallelogram and their cross product normal to it, with the height of the parallelogram "
        "as the opposite leg of a right triangle.",
        r"$\mathbf A\times\mathbf B$ is normal to both factors, follows the right-hand rule and has the area of the "
        r"parallelogram as its magnitude (Notes.pdf Fig. 1.5).")
def cross_product():
    sc = Scene(600, 370, (130, 305), 88)
    O = (0.0, 0.0, 0.0)
    th = math.radians(60.0)
    phi = math.radians(25.0)
    la, lb = 2.5, 1.9
    B0 = (-lb * math.sin(th), lb * math.cos(th), 0.0)
    A = (0.0, la, 0.0)
    B = (B0[0] * math.cos(phi), B0[1], -B0[0] * math.sin(phi))
    C = _unit3(_cross(A, B))
    Ah = _unit3(A)
    F = _mul(Ah, _dot(B, Ah))
    AB = _v3(A, B)
    _poly3(sc, [O, A, AB, B], "EDGE", 1.3, None, "EDGE", True, 0.13)
    triangle(sc, [P3(O), P3(F), P3(B)], ORANGE, 0.22)
    # height (dashed) and right angle at F
    _line3(sc, F, B, "TEXT", 1.4, "6 4")
    hh = _unit3(_v3(B, F, -1.0))
    s_ = 0.2
    _poly3(sc, [_v3(F, Ah, -s_), _v3(_v3(F, Ah, -s_), hh, s_), _v3(F, hh, s_)], "TEXT", 1.2)
    sc.label(P3(_v3(F, _v3(B, F, -1.0), 0.5)), "B |sin θ" + S("", "AB") + "|", "HEAD", "start", 15, dx=14, dy=4)
    _vec3(sc, O, A, bold("A"), ORANGE, 3.0, off=(14, 12), size=18, head=11)
    _vec3(sc, O, B, bold("B"), ORANGE, 3.0, off=(-8, -12), size=18, head=11)
    mid = _arc3(sc, A, B, 0.85, "GREEN")
    sc.label(_push(mid, (0, 0), 0.30), "θ" + S("", "AB"), "GREEN", "middle", 16, dy=5)
    # C = A x B
    Cl = 2.3
    _vec3(sc, O, _mul(C, Cl), None, DRED, 3.4, head=12)
    sc.label(P3(_mul(C, Cl)), bold("C") + " = " + bold("A") + " × " + bold("B"), DRED, "start", 17, dx=12, dy=-4)
    # right-hand rule: curled arrow about C, from A towards B
    e2 = _cross(C, Ah)
    _circ3(sc, _mul(C, 1.2), Ah, e2, 0.5, 5, 290, "HEAD", head=True, w=1.5)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-triple-product",
        "A parallelepiped with edges A, B and C, the normal A cross B of its base and its height as the projection of C on "
        "that normal.",
        r"The triple product is the volume of the parallelepiped, base $\lVert\mathbf A\times\mathbf B\rVert$ times "
        r"height, positive in right-hand order (Notes.pdf Fig. 1.6).")
def triple_product():
    sc = Scene(640, 420, (90, 350), 76)
    O = (0.0, 0.0, 0.0)
    A = (0.0, 2.4, 0.0)
    B = (-2.4, 0.4, 0.0)
    C = (-1.0, 1.9, 2.0)
    n = (0.0, 0.0, 1.0)
    AB = _v3(A, B)
    _poly3(sc, [O, A, AB, B], "EDGE", 1.2, None, "EDGE", True, 0.16)
    for p in (O, A, B, AB):
        _line3(sc, p, _v3(p, C), "EDGE", 1.2, "5 4")
    _poly3(sc, [_v3(O, C), _v3(A, C), _v3(AB, C), _v3(B, C)], "EDGE", 1.2, "5 4", "none", True)
    foot = (C[0], C[1], 0.0)
    _line3(sc, C, foot, "TEXT", 1.5, "6 4")
    _vec3(sc, O, A, bold("A"), ORANGE, 3.0, off=(14, 12), size=18, head=11)
    _vec3(sc, O, B, bold("B"), ORANGE, 3.0, off=(-6, -12), size=18, head=11)
    _vec3(sc, O, C, bold("C"), ORANGE, 3.0, off=(-14, -8), size=18, head=11)
    _vec3(sc, O, _mul(n, 1.8), None, DRED, 3.4, head=12)
    sc.label(P3(_mul(n, 1.8)), bold("A") + " × " + bold("B"), DRED, "end", 17, dx=-12, dy=14)
    mid = _arc3(sc, C, n, 1.25, "GREEN")
    sc.label(mid, "γ" + S("", "C"), "GREEN", "middle", 16, dx=-4, dy=-14)
    hm = P3(_mul(_v3(C, foot), 0.5))
    sc.label(hm, "height =", "HEAD", "start", 15, dx=12, dy=-2)
    sc.label(hm, "C cos γ" + S("", "C"), "HEAD", "start", 15, dx=12, dy=18)
    sc.dotp(P3(foot), 3.0, "TEXT")
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-moment",
        "A vector on its line of action, a point O off the line, two position vectors to points of the line and the "
        "perpendicular distance h.",
        r"The moment of $\mathbf A$ about $O$ depends only on $A$ and the distance $h$ to the line of action, not on the "
        r"point $P$ chosen on it (Notes.pdf Fig. 1.7).")
def moment():
    sc = Scene(700, 360, (140, 70), 80)
    a = 12.0
    u = _d(a)
    nrm = _d(a - 90)
    O = (0.0, 0.0)
    h = 2.0
    H = _add(O, nrm, h)
    P = _add(H, u, 2.4)
    Q = _add(H, u, 5.2)
    tip = _add(P, u, 1.5)
    sc.line(_add(H, u, -1.3), _add(H, u, 6.0), "EDGE", 1.2, "8 5")
    sc.note(_add(H, u, -1.3), "line of action", "TEXT", "start", 13, dx=0, dy=24)
    triangle(sc, [O, H, P], ORANGE, 0.18)
    sc.line(O, H, "EDGE", 1.3, "5 4")
    sc.line(H, P, "EDGE", 1.3, "5 4")
    sc.vec(O, Q, None, "EDGE", 1.4, head=9)
    sc.vec(O, P, None, "HEAD", 3.0, head=11)
    sc.vec(P, tip, bold("A"), ORANGE, 3.6, name_off=(4, -16), size=18, head=12)
    right_angle(sc, H, 90 + a, a, 0.12)
    sc.label(_add(O, nrm, h / 2), "h = |" + bold("OP") + S("", "⊥") + "|", "HEAD", "start", 16, dx=12, dy=0)
    sc.label(_add(H, u, 1.2), bold("OP") + S("", "∥"), "HEAD", "middle", 16, dx=-6, dy=26)
    sc.label(_add(O, P, 0.5), bold("OP"), "HEAD", "middle", 16, dx=24, dy=-10)
    sc.label(_add(O, Q, 0.62), bold("OP") + "′", "TEXT", "middle", 16, dx=36, dy=-14)
    for p, nm, off in ((O, "O", (-14, -12)), (H, "H", (-14, 20)), (P, "P", (4, 22)), (Q, "P′", (6, 22))):
        sc.dotp(p, 3.8)
        sc.label(p, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    axis_out(sc, (-0.75, 0.0), bold("M") + " = h A " + bold("e") + S("", "M"), "HEAD", off=(14, 36))
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-rotating-vector-plane",
        "A vector rotating counterclockwise in the plane, its rotated copy and the small change dA tangent to the circle of "
        "its tip.",
        r"A vector of constant magnitude rotating about $\mathbf k$: its change is tangent to the circle of its tip, of "
        r"magnitude $A\,d\theta$, along $\mathbf k\times\mathbf A$ (Notes.pdf Fig. 1.9).")
def rotating_vector_plane():
    sc = Scene(660, 430, (110, 360), 90)
    O = (0.0, 0.0)
    TH, DT, LA = 30.0, 15.0, 3.6
    t1 = _add(O, _d(TH), LA)
    t2 = _add(O, _d(TH + DT), LA)
    fixed_axis(sc, O, 0, 4.4, bold("i"), off=(14, 6))
    fixed_axis(sc, O, 90, 3.65, bold("j"), off=(14, 4))
    # dotted circle of the tip
    sc.arc(O, LA, TH - 14, TH + DT + 14, "EDGE", 1.4, "2 4")
    sc.vec(O, t2, bold("A") + " + d" + bold("A"), ORANGE, 1.8, name_off=(-30, -4), size=17, head=10)
    sc.vec(O, t1, bold("A"), ORANGE, 3.2, name_off=(22, 20), size=18, head=11)
    sc.vec(t1, t2, None, DRED, 3.0, head=10)
    mid = _add(t1, _add(t2, t1, -1.0), 0.5)
    sc.label(mid, "d" + bold("A"), "HEAD", "start", 17, dx=22, dy=-4)
    sc.label(mid, "|d" + bold("A") + "| = A dθ", "HEAD", "start", 16, dx=22, dy=-26, italic=False)
    sc.arc(O, 1.0, 0, TH, "GREEN", 1.6, head=True)
    sc.label(_add(O, _d(TH / 2 - 2), 1.45), "θ", "GREEN", "middle", 17, dy=5, dx=8)
    sc.arc(O, 2.1, TH, TH + DT, "GREEN", 1.6, head=True)
    sc.label(_add(O, _d(TH + DT / 2), 2.45), "dθ", "GREEN", "middle", 16, dx=-4, dy=-8)
    sc.spin(O, 0.52, 120, 250, dot1("θ"), "GREEN", name_r=0.82)
    axis_out(sc, O, bold("k"), "HEAD", off=(14, 30))
    sc.dotp(O, 2.0, "HEAD")
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-rotating-vector-3d",
        "A vector rotating about a general axis, split into a part along the axis and a perpendicular part whose tip moves "
        "on a circle.",
        r"Rotation about a general axis $\mathbf e_\omega$: only $\mathbf A_\perp$ changes, on a circle of radius "
        r"$\lvert\mathbf e_\omega\times\mathbf A\rvert$, giving $\boldsymbol\omega\times\mathbf A$ (Notes.pdf Fig. 1.10).")
def rotating_vector_3d():
    sc = Scene(700, 490, (170, 405), 80)
    O = (0.0, 0.0, 0.0)
    ew = _unit3((0.4, 0.4, 0.8))
    m0 = _unit3(_v3((0.0, 1.0, 0.0), ew, -ew[1]))
    psi = 0.0
    m = _v3(_mul(m0, math.cos(psi)), _mul(_cross(ew, m0), math.sin(psi)))
    nn = _cross(ew, m)
    TH = math.radians(50.0)
    LA = 2.7
    R = LA * math.sin(TH)
    Apar = _mul(ew, LA * math.cos(TH))
    A = _v3(Apar, _mul(m, R))
    for v, nm, off in (((2.2, 0, 0), "x", (-10, 14)), ((0, 3.6, 0), "y", (14, 6)), ((0, 0, 1.4), "z", (-12, 0))):
        _vec3(sc, O, v, None, "EDGE", 1.2, head=8)
        sc.label(P3(v), nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    triangle(sc, [P3(O), P3(Apar), P3(A)], ORANGE, 0.20)
    # rotation axis (thin, dashed) and the circle of the tip (dotted)
    sc.line(P3(_mul(ew, -0.4)), P3(_mul(ew, 4.3)), "EDGE", 1.2, "6 4")
    _circ3(sc, Apar, m, nn, R, 0, 360, "EDGE", head=False, w=1.4, dash="2 4")
    # A_par, A_perp, A and the axis vector
    _vec3(sc, O, Apar, None, ORANGE, 2.2, head=9)
    _line3(sc, Apar, A, "TEXT", 1.5, "6 4")
    _vec3(sc, O, _mul(ew, 1.2), None, DRED, 4.0, head=12)
    sc.label(P3(_mul(ew, 1.2)), bold("e") + S("", "ω"), "HEAD", "start", 17, dx=14, dy=-2)
    _vec3(sc, O, A, bold("A"), ORANGE, 3.2, off=(16, 6), size=18, head=11)
    sc.label(P3(_mul(Apar, 0.55)), bold("A") + S("", "∥"), ORANGE, "end", 16, dx=-26, dy=6)
    sc.label(P3(_v3(Apar, _mul(m, R), 0.5)), bold("A") + S("", "⊥"), ORANGE, "middle", 16, dx=4, dy=26)
    mid = _arc3(sc, ew, A, 0.95, "GREEN")
    sc.label(mid, "θ" + S("", "ωA"), "GREEN", "middle", 16, dx=22, dy=12)
    # rotated A_perp + dA_perp and the small arc about the circle centre
    dth = 20.0
    f = math.radians(dth)
    Aperp2 = _v3(_mul(m, R * math.cos(f)), _mul(nn, R * math.sin(f)))
    A2 = _v3(Apar, Aperp2)
    _vec3(sc, Apar, Aperp2, None, ORANGE, 1.8, head=9)
    sc.label(P3(_v3(Apar, Aperp2, 0.5)), bold("A") + S("", "⊥") + " + d" + bold("A") + S("", "⊥"), ORANGE, "middle", 15, dx=-4, dy=-12)
    _vec3(sc, A, _v3(A2, A, -1.0), None, DRED, 3.0, head=10)
    sc.label(P3(A2), "d" + bold("A") + S("", "⊥"), "HEAD", "start", 16, dx=12, dy=-4)
    _circ3(sc, Apar, m, nn, 0.8, 0, dth, "GREEN", head=True)
    sc.label(P3(_v3(Apar, _v3(_mul(m, 1.35 * math.cos(f / 2)), _mul(nn, 1.35 * math.sin(f / 2))))), "dθ", "GREEN", "middle", 16, dx=-24, dy=-4)
    # rotation sense about the axis (right-hand rule)
    _circ3(sc, _mul(ew, 3.6), m, nn, 0.5, 30, 300, "GREEN", head=True, w=1.8)
    sc.label(P3(_mul(ew, 3.6)), dot1("θ"), "GREEN", "start", 17, weight="700", dx=46, dy=-6)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-rotating-basis",
        "A basis rotating about k0, with the derivative of each unit vector drawn at its tip, tangent to the unit circle.",
        r"The derivatives of the unit vectors of a basis in simple rotation are the vectors turned a quarter turn, scaled "
        r"by $\dot\theta_z$: $\boldsymbol\omega\times\mathbf i_1$ and $\boldsymbol\omega\times\mathbf j_1$.")
def rotating_basis():
    sc = Scene(700, 480, (340, 282), 86)
    O = (0.0, 0.0)
    TH, R = 35.0, 2.2
    i0, j0, k0 = (bold(c) + S("", "0") for c in "ijk")
    i1, j1 = (bold(c) + S("", "1") for c in "ij")
    tz = "θ" + S("", "z")
    zd = dot1("θ") + S("", "z")
    sc.circle(O, R, "EDGE", 1.4, "2 4")
    fixed_axis(sc, O, 0, R * 1.2, i0, off=(18, 6))
    fixed_axis(sc, O, 90, R * 1.2, j0, off=(16, 4))
    ti = _add(O, _d(TH), R)
    tj = _add(O, _d(TH + 90), R)
    sc.vec(O, ti, None, "BLUE", 2.8, head=11)
    sc.vec(O, tj, None, "BLUE", 2.8, head=11)
    sc.label(ti, i1, "BLUE", "middle", 17, weight="700", dx=-4, dy=28)
    sc.label(tj, j1, "BLUE", "middle", 17, weight="700", dx=26, dy=2)
    # derivatives at the tips
    di = _add(ti, _d(TH + 90), 0.95)
    dj = _add(tj, _d(TH + 180), 0.95)
    sc.vec(ti, di, None, DRED, 3.0, head=11)
    sc.vec(tj, dj, None, DRED, 3.0, head=11)
    sc.label(di, "d" + i1 + "/dt = " + zd + " " + j1, "HEAD", "start", 16, dx=10, dy=-6)
    sc.label(dj, "d" + j1 + "/dt = " + MINUS + zd + " " + i1, "HEAD", "end", 16, dx=-10, dy=-8)
    sc.dotp(ti, 3.2, "BLUE")
    sc.dotp(tj, 3.2, "BLUE")
    sc.arc(O, 0.9, 0, TH, "GREEN", 1.6, head=True)
    sc.label(_d(TH / 2 - 2), tz, "GREEN", "start", 16, dx=74, dy=10)
    sc.spin(O, 0.5, 200, 340, zd, "GREEN", name_r=0.82)
    axis_out(sc, O, bold("ω") + " = " + zd + " " + k0, "HEAD", off=(-96, 28))
    sc.dotp(O, 2.0, "HEAD")
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t1-infinitesimal-rotation",
        "Three infinitesimal rotations about the coordinate axes combined into one angular velocity vector, and the small "
        "change of a vector rotated about it.",
        r"Infinitesimal rotations about the three axes add up to one angular velocity $\boldsymbol\omega$; $[\Omega]\,"
        r"\mathbf A$ equals $\boldsymbol\omega\times\mathbf A$ (Notes.pdf Eqs. 1.72 and 1.73).")
def infinitesimal_rotation():
    sc = Scene(870, 470, (190, 340), 76)
    O = (0.0, 0.0, 0.0)
    w = (1.1, 1.7, 2.2)
    A = (0.6, 2.4, 1.0)
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    for v, nm, off in (((3.2, 0, 0), "x", (-10, 14)), ((0, 4.6, 0), "y", (14, 6)), ((0, 0, 3.8), "z", (-4, -10))):
        _vec3(sc, O, v, None, "EDGE", 1.3, head=8)
        sc.label(P3(v), nm, "TEXT", "middle", 17, weight="700", dx=off[0], dy=off[1])
    # dashed box of the components of omega and the components on the axes
    cs = [(a, b, c) for a in (0, w[0]) for b in (0, w[1]) for c in (0, w[2])]
    for p in cs:
        for q in cs:
            diff = [i for i in range(3) if p[i] != q[i]]
            if len(diff) == 1 and p[diff[0]] == 0 and p != (0, 0, 0) and q != (0, 0, 0):
                _line3(sc, p, q, "EDGE", 1.0)
    for v, nm, off in (((w[0], 0, 0), S("ω", "x"), (22, 22)), ((0, w[1], 0), S("ω", "y"), (14, 22)),
                       ((0, 0, w[2]), S("ω", "z"), (-18, 0))):
        _line3(sc, O, v, DRED, 2.0, "7 4")
        sc.label(P3(v), nm, "HEAD", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # small rotations about each axis (right-hand sense)
    for c0, e1, e2, nm, lab in (((2.2, 0, 0), ey, ez, "x", (-54, 6)), ((0, 3.4, 0), ez, ex, "y", (4, -46)),
                                ((0, 0, 3.0), ex, ey, "z", (58, -4))):
        _circ3(sc, c0, e1, e2, 0.42, 20, 300, "GREEN", head=True, w=1.7)
        sc.label(P3(c0), "dθ" + S("", nm), "GREEN", "middle", 16, dx=lab[0], dy=lab[1])
    # omega and the rotating vector
    _vec3(sc, O, w, None, DRED, 3.6, head=12)
    sc.label(P3(w), bold("ω"), "HEAD", "start", 18, dx=12, dy=-8)
    ww = _unit3(w)
    dA = _mul(_cross(ww, A), 0.5)
    A2 = _v3(A, dA)
    _vec3(sc, O, A2, None, ORANGE, 1.8, head=9)
    _vec3(sc, O, A, bold("A"), ORANGE, 3.2, off=(-14, 28), size=18, head=11)
    _vec3(sc, A, dA, None, DRED, 3.0, head=10)
    sc.label(P3(A2), "d" + bold("A") + " = " + bold("ω") + " × " + bold("A") + " dt", "HEAD", "start", 16, dx=14, dy=-6)
    sc.dotp(P3(O), 3.5)
    sc.label(P3(O), "O", "HEAD", "end", 17, dx=-8, dy=14)
    # antisymmetric matrix
    wx, wy, wz = (S("ω", c) for c in "xyz")
    _matrix(sc, 600, 120, "[Ω]", [["0", MINUS + wz, wy], [wz, "0", MINUS + wx], [MINUS + wy, wx, "0"]], cw=70)
    return sc

