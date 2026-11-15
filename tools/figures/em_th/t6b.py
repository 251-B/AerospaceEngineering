"""Theory figures of Topic 6, inertia half (Sections 10 to 16): mass distributions, centres of mass, symmetry, standard
bodies, tensor and Steiner."""
import math

from figures.em_theory import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_th.t6 import _add, _blob, _d, S, Scene, bold

ORANGE = "ACC"
DX, DY = -0.789 * 0.6, -0.614 * 0.6          # cabinet depth axis: x towards the lower left, foreshortened


def _p(x, y, z):
    return (x * DX + y, x * DY + z)


def _o(o, x, y, z):
    return (o[0] + x * DX + y, o[1] + x * DY + z)


def _s(sym, a=None, b=None):
    return S(bold(sym), a, b)


def _sup_i(base_sup):
    return base_sup + '<tspan baseline-shift="sub" font-size="80%">i</tspan>'


def _hull(pts):
    pts = sorted(set((round(x, 6), round(y, 6)) for x, y in pts))

    def cr(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo = []
    for p in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cr(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def _axes3(sc, o, lens, names=("x", "y", "z"), subs=("0", "0", "0"), col="EDGE", offs=((-12, 14), (14, 8), (-12, 0)),
           w=1.4):
    dirs = ((DX, DY), (1.0, 0.0), (0.0, 1.0))
    for dv, ln, nm, sb, off in zip(dirs, lens, names, subs, offs):
        tip = _add(o, dv, ln)
        sc.vec(o, tip, None, col, w, head=8)
        sc.label(tip, bold(nm) + (S("", sb) if sb else ""), "TEXT" if col == "EDGE" else col, "middle", 16, weight="700",
                 dx=off[0], dy=off[1])


def _mid(a, b, f=0.5):
    return (a[0] + f * (b[0] - a[0]), a[1] + f * (b[1] - a[1]))


def _square(sc, p, s=0.075, col=ORANGE):
    sc.poly([(p[0] - s, p[1] - s), (p[0] + s, p[1] - s), (p[0] + s, p[1] + s), (p[0] - s, p[1] + s)], "HEAD", 1.0,
            fill=col, close=True, opacity=0.95)


def _mark3(sc, corner, u, w, s=0.1):
    """Right-angle mark at corner (screen point) between the screen directions u and w."""
    p1 = _add(corner, u, s)
    sc.poly([p1, _add(p1, w, s), _add(corner, w, s)], "EDGE", 1.2)


def _blobp(c, r, phase=0.0, sy=0.82):
    return _blob(c, r, phase, sy=sy)


# ------------------------------------------------------------------------------------------------------------ 1
@figure("t6-mass-distribution",
        "A discrete set of point masses and a continuous body, each with the position vector of one mass from the origin O.",
        r"Discrete (left) and continuous (right) mass distributions; the moments of the distribution sum or integrate "
        r"$\mathbf r_0^P$ weighted by the mass (Notes.pdf Fig. 10.1).")
def mass_distribution():
    sc = Scene(860, 420, (110, 340), 105)
    for k_, o in enumerate(((0.0, 0.0), (4.3, 0.0))):
        _axes3(sc, o, (1.0, 2.6, 2.2), subs=("0", "0", "0"))
        sc.dotp(o, 3.5)
        sc.label(o, "O", "HEAD", "end", 17, dx=-8, dy=20)
    O = (0.0, 0.0)
    pts = [((1.45, 1.25), 9, True), ((0.55, 1.1), 5, False), ((2.0, 1.7), 7, False), ((1.15, 2.05), 6, False),
           ((2.15, 0.65), 4, False), ((0.5, 1.85), 5, False)]
    for p, r, main in pts:
        sc.mass(p, None, r=r, col="BLUE" if main else "ACC")
    p0 = pts[0][0]
    sc.vec(O, p0, None, "BLUE", 2.6, head=11)
    sc.label(p0, _sup_i("P"), "HEAD", "start", 17, dx=12, dy=-12)
    sc.label((p0[0] / 2, p0[1] / 2), _s("r", "0", _sup_i("P")), "BLUE", "end", 16, weight="700", dx=-8, dy=-6)
    sc.label((p0[0], p0[1]), "m" + S("", "i"), "HEAD", "middle", 16, dx=-14, dy=24)
    sc.note((0.6, -0.5), "discrete system", "TEXT", "start", 13)
    O2 = (4.3, 0.0)
    c = (6.0, 1.55)
    pts2 = _blobp(c, 1.0, 0.7)
    triangle(sc, pts2, "BLUE", 0.16)
    sc.poly(pts2, "BLUE", 1.6, close=True)
    P = (6.3, 1.7)
    sc.vec(O2, P, None, "BLUE", 2.6, head=11)
    _square(sc, P, 0.07)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=-10)
    sc.label(P, "dm", ORANGE, "start", 16, weight="700", dx=12, dy=14)
    sc.label((O2[0] + (P[0] - O2[0]) / 2, P[1] / 2), _s("r", "0", "P"), "BLUE", "end", 16, weight="700", dx=-8, dy=-6)
    sc.note((4.9, -0.5), "continuous body", "TEXT", "start", 13)
    return sc


# ------------------------------------------------------------------------------------------------------------ 2
@figure("t6-centre-of-mass",
        "An irregular body with a mass element at P and its centre of mass G, both located by position vectors from O.",
        r"The centre of mass $G$ is the mass-weighted average of the positions $\mathbf r_0^P$ of all the mass elements.")
def centre_of_mass():
    sc = Scene(640, 440, (120, 350), 125)
    O = (0.0, 0.0)
    _axes3(sc, O, (1.0, 3.8, 2.4))
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    c = (2.4, 1.4)
    pts = _blobp(c, 1.15, 0.4)
    triangle(sc, pts, "BLUE", 0.16)
    sc.poly(pts, "BLUE", 1.6, close=True)
    P, G = (3.05, 1.95), (2.3, 1.2)
    sc.vec(O, P, None, "BLUE", 2.6, head=11)
    sc.vec(O, G, None, ORANGE, 2.6, head=11)
    sc.dotp(G, 5.5, "PINK")
    _square(sc, P, 0.07)
    sc.label(P, "dm", ORANGE, "start", 16, weight="700", dx=14, dy=-8)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=16)
    sc.label(G, "G", "HEAD", "start", 17, dx=10, dy=22)
    sc.label((G[0] * 0.5, G[1] * 0.5), _s("r", "0", "G"), ORANGE, "start", 16, weight="700", dx=10, dy=14)
    sc.label((P[0] * 0.5, P[1] * 0.5), _s("r", "0", "P"), "BLUE", "end", 16, weight="700", dx=-8, dy=-6)
    return sc


# ------------------------------------------------------------------------------------------------------------ 3
@figure("t6-symmetry-theorems",
        "A body symmetric about the plane Oyz with a pair of mirror mass elements at opposite x, and its centre of mass "
        "on the plane.",
        r"Mirror elements of a plane of symmetry have opposite signed distances to it: $G$ lies on the plane and every "
        r"product of inertia that involves the plane vanishes.")
def symmetry_theorems():
    sc = Scene(720, 480, (300, 360), 125)
    O = (0.0, 0.0)
    ys, z0, z1 = 1.9, -0.35, 2.0
    plane = [_p(0, -ys, z0), _p(0, ys, z0), _p(0, ys, z1), _p(0, -ys, z1)]
    # body: hull of two ellipses (in the planes x = +-1.0)
    zc, ry, rz = 0.85, 1.25, 0.8
    ring = lambda x: [_p(x, ry * math.cos(t * math.pi / 30), zc + rz * math.sin(t * math.pi / 30)) for t in range(60)]
    body = _hull(ring(1.1) + ring(-1.1))
    triangle(sc, body, "BLUE", 0.10)
    sc.poly(body, "BLUE", 1.5, close=True)
    triangle(sc, plane, "ACC", 0.14)
    sc.poly(plane, "ACC", 1.3, close=True)
    sc.poly(ring(0), "BLUE", 1.5, "5 4", close=True)
    _axes3(sc, O, (1.8, 2.45, 2.35), subs=("0", "0", "0"))
    sc.label(_p(0, ys, z1), "plane " + "Oyz", "ACC", "end", 15, dx=-8, dy=-8)
    # mirror elements
    yy, zz, xx = 0.8, 1.35, 0.85
    A, B = _p(xx, yy, zz), _p(-xx, yy, zz)
    M = _p(0, yy, zz)
    sc.dashed(A, B)
    _square(sc, A)
    _square(sc, B)
    sc.label(A, "dm", ORANGE, "end", 15, weight="700", dx=-12, dy=14)
    sc.label(B, "dm", ORANGE, "start", 15, weight="700", dx=-4, dy=-14)
    sc.label(((A[0] + M[0]) / 2, (A[1] + M[1]) / 2), "x", "TEXT", "middle", 16, dx=-12, dy=-12)
    sc.label(((B[0] + M[0]) / 2, (B[1] + M[1]) / 2), "−x", "TEXT", "middle", 16, dx=14, dy=22)
    sc.dotp(M, 2.5, "EDGE")
    G = _p(0, -0.55, 0.55)
    sc.mass(G, None, r=5, col="PINK")
    sc.label(G, "G", "HEAD", "end", 17, dx=-10, dy=6)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=-6)
    sc.note(_p(-0.3, -ys, 2.05), "products with Oyz cancel", "TEXT", "start", 14, dx=0, dy=-10)
    return sc


# ------------------------------------------------------------------------------------------------------------ 4
def _poly_label(sc, p, s, col="HEAD", anchor="middle", dx=0, dy=0, size=16):
    sc.label(p, s, col, anchor, size, dx=dx, dy=dy)


@figure("t6-composite-bodies",
        "A star, a T-shape and a plate with a hole, decomposed into simple parts with their own centres of mass.",
        r"Divide and conquer: a composite body is the sum of simple parts, and a hole is a part of negative mass "
        r"([Lecture 8, Slide 17]).")
def composite_bodies():
    sc = Scene(920, 360, (20, 180), 100)
    # ---- star: outer radius 1.05, inner 0.45, centred at (1.2, 0)
    c = (1.2, 0.0)
    outer = [_add(c, _d(90 + 72 * k), 1.05) for k in range(5)]
    inner = [_add(c, _d(90 + 36 + 72 * k), 0.43) for k in range(5)]
    star = []
    for k in range(5):
        star += [outer[k], inner[k]]
    triangle(sc, star, "BLUE", 0.14)
    sc.poly(star, "BLUE", 1.8, close=True)
    sc.poly(inner, "EDGE", 1.2, "5 4", close=True)
    sc.dotp(c, 4.5, "PINK")
    sc.label(c, "G", "HEAD", "middle", 16, dx=0, dy=24)
    sc.note((0.35, -1.45), "star: pentagon + 5 triangles", "TEXT", "start", 13)
    # ---- T-shape at offset 3.5
    ox = 3.5
    top = [(ox - 0.9, 0.55), (ox + 0.9, 0.55), (ox + 0.9, 0.05), (ox - 0.9, 0.05)]
    stem = [(ox - 0.25, 0.05), (ox + 0.25, 0.05), (ox + 0.25, -1.15), (ox - 0.25, -1.15)]
    triangle(sc, top, "BLUE", 0.14)
    triangle(sc, stem, "BLUE", 0.22)
    sc.poly(top + [top[0]], "BLUE", 1.8)
    sc.poly(stem, "BLUE", 1.8)
    sc.line((ox - 0.25, 0.05), (ox + 0.25, 0.05), "EDGE", 1.2, "5 4")
    A1, A2 = 0.5 * 1.8, 0.5 * 1.2
    g2, g1 = (ox, 0.30), (ox, -0.55)
    gy = (A2 * g2[1] + A1 * g1[1]) / (A1 + A2)
    G = (ox, gy)
    sc.dotp(g1, 3.5, "BLUE")
    sc.label(g1, _s("G", "1") if False else "G" + S("", "1"), "BLUE", "start", 16, dx=10, dy=5)
    sc.dotp(g2, 3.5, "BLUE")
    sc.label(g2, "G" + S("", "2"), "BLUE", "start", 16, dx=-62, dy=5)
    sc.dotp(G, 5, "PINK")
    sc.label(G, "G", "HEAD", "start", 17, dx=34, dy=-6)
    sc.note((ox - 0.9, -1.45), "T-shape: two bars", "TEXT", "start", 13)
    # ---- plate with a hole at offset 6.9
    px = 6.6
    w, h = 2.0, 1.4
    rect = [(px, -h / 2), (px + w, -h / 2), (px + w, h / 2), (px, h / 2)]
    triangle(sc, rect, "BLUE", 0.14)
    sc.poly(rect, "BLUE", 1.8, close=True)
    g1 = (px + w / 2, 0.0)
    g2 = (px + 1.4, 0.1)
    rh = 0.45
    sc.circle(g2, rh, "PINK", 1.8, fill="PINK", opacity=0.10)
    am, ah = w * h, math.pi * rh ** 2
    G = ((am * g1[0] - ah * g2[0]) / (am - ah), (am * g1[1] - ah * g2[1]) / (am - ah))
    sc.dotp(g1, 3.5, "BLUE")
    sc.label(g1, "G" + S("", "1"), "BLUE", "end", 16, dx=-8, dy=-8)
    sc.dotp(g2, 3.5, "PINK")
    sc.label(g2, "G" + S("", "2"), "PINK", "middle", 16, dx=0, dy=-rh * 100 - 8)
    sc.dotp(G, 5, "HEAD")
    sc.label(G, "G", "HEAD", "end", 17, dx=-8, dy=24)
    sc.label((px + 0.05, h / 2), "D" + S("", "1"), "BLUE", "start", 17, dx=4, dy=-8)
    sc.label((g2[0] + rh, g2[1] - rh), "D" + S("", "2") + " (−)", "PINK", "start", 16, dx=-26, dy=22)
    sc.note((px, -1.45), "plate with a hole: D1 − D2", "TEXT", "start", 13)
    return sc


# ------------------------------------------------------------------------------------------------------------ 5
@figure("t6-inertia-distances",
        "A mass element and its distances to the origin, to the axis Oz and to the plane Oxy.",
        r"Distances used in the moments of inertia about a point, an axis and a plane, and the signed distances of the "
        r"products of inertia.")
def inertia_distances():
    sc = Scene(740, 520, (300, 400), 125)
    O = (0.0, 0.0)
    x, y, z = 1.3, 1.5, 1.2
    P = _p(x, y, z)
    Pxy, Pxz, Pyz = _p(x, y, 0), _p(x, 0, z), _p(0, y, z)
    A = _p(0, 0, z)
    plane = [_p(0, 0, 0), _p(x + 0.6, 0, 0), _p(x + 0.6, y + 0.6, 0), _p(0, y + 0.6, 0)]
    triangle(sc, plane, "BLUE", 0.08)
    sc.poly(plane, "EDGE", 1.0, "4 4", close=True)
    sc.label(_p(x + 0.6, y + 0.6, 0), "plane Oxy", "TEXT", "start", 14, dx=8, dy=14)
    _axes3(sc, O, (2.2, 2.55, 2.1), subs=("", "", ""))
    # dashed projections onto the coordinate planes
    for q in (Pxy, Pxz, Pyz):
        sc.dashed(P, q)
        sc.dotp(q, 2.6, "EDGE")
    sc.dashed(Pxy, _p(x, 0, 0))
    sc.dashed(Pxy, _p(0, y, 0))
    # distance to the point O (blue), to the axis Oz (green), to the plane Oxy (orange)
    sc.vec(O, P, None, "BLUE", 2.6, head=11)
    sc.vec(A, P, None, "GREEN", 2.6, head=11)
    sc.vec(P, Pxy, None, ORANGE, 2.6, head=11)
    sc.dotp(A, 3.5, "GREEN")
    # right angle at the axis between the axis (downwards) and the horizontal segment
    ux = (P[0] - A[0], P[1] - A[1])
    n = math.hypot(*ux)
    _mark3(sc, A, (ux[0] / n, ux[1] / n), (0.0, -1.0), 0.12)
    _square(sc, P, 0.06)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=-8)
    sc.label(P, "dm", ORANGE, "start", 15, weight="700", dx=12, dy=12)
    sc.label(_mid(O, P), "√(x² + y² + z²)", "BLUE", "end", 15, dx=-70, dy=14)
    sc.label(_mid(A, P), "√(x² + y²)", "GREEN", "start", 15, dx=8, dy=-18)
    sc.label(_mid(P, Pxy), "z", ORANGE, "start", 16, dx=10, dy=4)
    sc.label(_mid(P, Pxz, 0.8), "d" + S("", "1") + " = y", "TEXT", "middle", 14, dx=0, dy=20)
    sc.label(_mid(P, Pyz, 0.85), "d" + S("", "2") + " = x", "TEXT", "start", 14, dx=14, dy=-12)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=-8)
    return sc


# ------------------------------------------------------------------------------------------------------------ 6
@figure("t6-flat-plate",
        "A flat plate in the plane Oxy with a mass element and its distances to the axes Ox, Oy and Oz.",
        r"For a flat body the distance to $Oz$ is the hypotenuse of the legs $x$ and $y$, so $I_z$ equals $I_x + I_y$.")
def flat_plate():
    sc = Scene(720, 500, (110, 430), 135)
    O = (0.0, 0.0)
    pts = _blobp((2.0, 1.45), 1.2, 1.1)
    triangle(sc, pts, "BLUE", 0.14)
    sc.poly(pts, "BLUE", 1.6, close=True)
    fixed_axis(sc, O, 0, 3.7, _s("x"), off=(14, 6))
    fixed_axis(sc, O, 90, 2.9, _s("y"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _s("z"), "HEAD", "end", 16, weight="700", dx=-14, dy=-10)
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=24)
    P = (2.4, 1.6)
    F = (P[0], 0.0)
    triangle(sc, [O, F, P], "ACC", 0.2)
    sc.dashed(P, F)
    sc.dashed(P, (0.0, P[1]))
    sc.line(O, P, "HEAD", 1.6, "6 4")
    right_angle(sc, F, 180, 90, 0.1)
    _square(sc, P, 0.07)
    sc.label(P, "dm", ORANGE, "start", 16, weight="700", dx=12, dy=-8)
    sc.label((P[0] / 2, 0.0), "x", "TEXT", "middle", 16, dy=24)
    sc.label((P[0], P[1] / 2), "y", "TEXT", "start", 16, dx=8, dy=5)
    sc.label((P[0] / 2, P[1] / 2), "√(x² + y²)", "HEAD", "end", 15, dx=-6, dy=-12)
    return sc


# ------------------------------------------------------------------------------------------------------------ 7
@figure("t6-half-wire",
        "A half circumference of radius R in the upper half plane, with an arc element at angle theta and its centre of "
        "mass on the y axis.",
        r"Half-circumference wire, $\theta$ from $0$ to $\pi$; $G$ lies on the axis of symmetry at $2R/\pi$ "
        r"(Notes.pdf Fig. 10.2(a)).")
def half_wire():
    sc = Scene(700, 520, (300, 340), 220)
    R, th = 1.0, 40.0
    O = (0.0, 0.0)
    up = [(R * math.cos(math.radians(t)), R * math.sin(math.radians(t))) for t in range(0, 181, 3)]
    lo = [(R * math.cos(math.radians(t)), R * math.sin(math.radians(t))) for t in range(180, 361, 3)]
    sc.poly(lo, "EDGE", 1.3, "6 4")
    sc.poly(up, "BLUE", 4.0)
    fixed_axis(sc, O, 0, 1.3, _s("x", "0"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.25, _s("y", "0"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _s("z", "0"), "HEAD", "end", 16, weight="700", dx=-14, dy=-12)
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=22)
    t = math.radians(th)
    Pt = (R * math.cos(t), R * math.sin(t))
    sc.line(O, Pt, "HEAD", 1.6)
    sc.label((Pt[0] * 0.55, Pt[1] * 0.55), "R", "HEAD", "end", 17, dx=-4, dy=-10)
    sc.arc(O, 0.3, 0, th, "GREEN", 1.7, head=True)
    sc.label((0.43 * math.cos(math.radians(th / 2)), 0.43 * math.sin(math.radians(th / 2))), "θ", "GREEN", "middle", 17,
             dy=6)
    seg = [(R * math.cos(math.radians(a)), R * math.sin(math.radians(a))) for a in [th - 4 + k for k in range(9)]]
    sc.poly(seg, ORANGE, 8.0)
    sc.label(Pt, "dℓ = R dθ", ORANGE, "start", 17, weight="700", dx=16, dy=-12)
    yg = 2 * R / math.pi
    sc.mass((0.0, yg), None, r=5, col="PINK")
    sc.label((0.0, yg), "G", "HEAD", "start", 17, dx=10, dy=-8)
    sc.dim((-0.22, 0.0), (-0.22, yg), "", off=(0, 0))
    sc.label((-0.22, yg / 2), "2R/π", "TEXT", "end", 15, dx=-8, dy=5)
    sc.dashed((-0.22, yg), (0.0, yg))
    return sc


# ------------------------------------------------------------------------------------------------------------ 8
@figure("t6-plate",
        "A rectangular plate of length L and width W centred at O, with a second frame at its lower-left corner A.",
        r"Homogeneous plate centred at $O \equiv G$, and the frame $S_1$ at the corner $A$ used for Eq. 10.27 "
        r"(Notes.pdf Fig. 10.2(b)).")
def plate():
    sc = Scene(740, 460, (330, 240), 105)
    Lx, Wy = 3.2, 1.6
    O = (0.0, 0.0)
    rect = [(-Lx / 2, -Wy / 2), (Lx / 2, -Wy / 2), (Lx / 2, Wy / 2), (-Lx / 2, Wy / 2)]
    triangle(sc, rect, "BLUE", 0.14)
    sc.poly(rect, "BLUE", 2.0, close=True)
    fixed_axis(sc, O, 0, 1.85, _s("x", "0"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.25, _s("y", "0"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O ≡ G", "HEAD", "end", 17, dx=-12, dy=24)
    sc.label(O, _s("z", "0"), "HEAD", "start", 16, weight="700", dx=13, dy=-12)
    A = (-Lx / 2, -Wy / 2)
    sc.vec(A, (A[0] + 1.3, A[1]), _s("x", "1"), ORANGE, 2.6, name_off=(0, -14), size=17, head=11)
    sc.vec(A, (A[0], A[1] + 1.1), _s("y", "1"), ORANGE, 2.6, name_off=(-14, -2), size=17, head=11)
    sc.mass(A, None, r=4.5, col=ORANGE)
    sc.label(A, "A", "HEAD", "end", 17, dx=-10, dy=22)
    # element dx dy at (x, y)
    pe = (0.85, 0.35)
    _square(sc, pe, 0.07)
    sc.dashed(pe, (pe[0], 0.0))
    sc.dashed(pe, (0.0, pe[1]))
    sc.label(pe, "dx dy", ORANGE, "start", 15, weight="700", dx=12, dy=-8)
    sc.label((pe[0], pe[1] / 2), "y", "TEXT", "start", 15, dx=6, dy=5)
    sc.label((pe[0] / 2, pe[1]), "x", "TEXT", "middle", 15, dy=-8)
    # dimensions
    sc.dim((-Lx / 2, -Wy / 2 - 0.45), (Lx / 2, -Wy / 2 - 0.45), "L", off=(0, 18))
    sc.dashed((-Lx / 2, -Wy / 2 - 0.05), (-Lx / 2, -Wy / 2 - 0.5))
    sc.dashed((Lx / 2, -Wy / 2 - 0.05), (Lx / 2, -Wy / 2 - 0.5))
    sc.dim((Lx / 2 + 0.8, -Wy / 2), (Lx / 2 + 0.8, Wy / 2), "W", off=(14, 5))
    sc.dashed((Lx / 2 + 0.05, -Wy / 2), (Lx / 2 + 0.85, -Wy / 2))
    sc.dashed((Lx / 2 + 0.05, Wy / 2), (Lx / 2 + 0.85, Wy / 2))
    return sc


# ------------------------------------------------------------------------------------------------------------ 9
@figure("t6-half-disk",
        "A half disk of radius R with a polar area element and its centre of mass on the y axis.",
        r"Half disk with the polar element $r\,dr\,d\theta$; $G$ lies on the axis of symmetry at $4R/(3\pi)$ "
        r"(Notes.pdf Fig. 10.2(c)).")
def half_disk():
    sc = Scene(700, 440, (300, 340), 230)
    R, r, th = 1.0, 0.6, 45.0
    O = (0.0, 0.0)
    arc = [(R * math.cos(math.radians(t)), R * math.sin(math.radians(t))) for t in range(0, 181, 3)]
    triangle(sc, arc, "BLUE", 0.14)
    sc.poly(arc + [arc[0]], "BLUE", 2.4)
    fixed_axis(sc, O, 0, 1.3, _s("x", "0"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.2, _s("y", "0"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _s("z", "0"), "HEAD", "end", 16, weight="700", dx=-14, dy=-12)
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=22)
    dr, dth = 0.1, 12.0
    pts = [add_pol(r, th - dth / 2 + k * dth / 6) for k in range(7)] + \
          [add_pol(r + dr, th + dth / 2 - k * dth / 6) for k in range(7)]
    sc.poly(pts, "HEAD", 1.0, fill=ORANGE, close=True, opacity=0.95)
    sc.line(O, add_pol(r, th), "HEAD", 1.4, "5 4")
    sc.label(add_pol(r * 0.5, th), "r", "HEAD", "end", 16, dx=-4, dy=-10)
    sc.arc(O, 0.25, 0, th, "GREEN", 1.7, head=True)
    sc.label(add_pol(0.37, th / 2), "θ", "GREEN", "middle", 16, dy=6)
    sc.label(add_pol(r + dr, th), "dA = r dr dθ", ORANGE, "start", 16, weight="700", dx=20, dy=-14)
    yg = 4 * R / (3 * math.pi)
    sc.mass((0.0, yg), None, r=5, col="PINK")
    sc.label((0.0, yg), "G", "HEAD", "start", 17, dx=10, dy=-8)
    sc.dim((-0.2, 0.0), (-0.2, yg), "", off=(0, 0))
    sc.dashed((-0.2, yg), (0.0, yg))
    sc.label((-0.2, yg / 2), "4R/(3π)", "TEXT", "end", 15, dx=-8, dy=5)
    sc.dim((0.0, -0.12), (R, -0.12), "R", off=(0, 18))
    return sc


def add_pol(r, deg):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


# ----------------------------------------------------------------------------------------------------------- 10
@figure("t6-half-sphere",
        "A solid hemisphere on the xy plane with the spherical coordinates r, longitude theta and latitude phi of a point, "
        "and its centre of mass on the z axis.",
        r"Half sphere with the latitude $\phi$ measured from $Oxy$ (so the volume element is "
        r"$r^2\cos\phi\,dr\,d\theta\,d\phi$); $G$ lies on the axis at $3R/8$ (Notes.pdf Fig. 10.2(d)).")
def half_sphere():
    sc = Scene(780, 600, (390, 390), 160)
    R, r, th, ph = 1.5, 1.2, 60.0, 35.0
    O = (0.0, 0.0)
    ex, ey = (1, 0, 0), (0, 1, 0)

    def pp(v):
        return _p(*v)
    # silhouette: hull of the equator and of the dome
    dome = []
    for i in range(0, 91, 6):
        for j in range(0, 360, 10):
            a, b = math.radians(i), math.radians(j)
            dome.append(pp((R * math.cos(a) * math.cos(b), R * math.cos(a) * math.sin(b), R * math.sin(a))))
    sil = _hull(dome)
    triangle(sc, sil, "BLUE", 0.08)
    sc.poly(sil, "BLUE", 2.0, close=True)
    eq = [pp((R * math.cos(math.radians(t)), R * math.sin(math.radians(t)), 0)) for t in range(0, 361, 5)]
    sc.poly(eq, "BLUE", 1.3, "6 4", close=True)
    _axes3(sc, O, (2.9, 2.2, 2.0), subs=("0", "0", "0"))
    ct, st, cp, sp = math.cos(math.radians(th)), math.sin(math.radians(th)), math.cos(math.radians(ph)), math.sin(math.radians(ph))
    Pt = pp((r * cp * ct, r * cp * st, r * sp))
    F = pp((r * cp * ct, r * cp * st, 0))
    triangle(sc, [O, F, Pt], "ACC", 0.24)
    sc.dashed(O, F)
    sc.dashed(F, Pt)
    sc.vec(O, Pt, None, "HEAD", 2.4, head=11)
    sc.dotp(F, 3.0)
    # longitude arc in Oxy and latitude arc in the meridian plane
    a1 = [pp((0.65 * math.cos(math.radians(t)), 0.65 * math.sin(math.radians(t)), 0)) for t in range(0, int(th) + 1, 3)]
    sc.poly(a1, "GREEN", 1.7)
    from figures.svgkit import arrow_head
    arrow_head(sc.c, sc.P(a1[-3]), sc.P(a1[-1]), "GREEN", 9)
    mt = math.radians(th / 2)
    sc.label(pp((0.88 * math.cos(mt), 0.88 * math.sin(mt), 0)), "θ", "GREEN", "middle", 16, dx=-30, dy=22)
    a2 = [pp((0.55 * math.cos(math.radians(t)) * ct, 0.55 * math.cos(math.radians(t)) * st, 0.55 * math.sin(math.radians(t))))
          for t in range(0, int(ph) + 1, 3)]
    sc.poly(a2, "GREEN", 1.7)
    arrow_head(sc.c, sc.P(a2[-3]), sc.P(a2[-1]), "GREEN", 9)
    mp = math.radians(ph / 2)
    sc.label(pp((0.8 * math.cos(mp) * ct, 0.8 * math.cos(mp) * st, 0.8 * math.sin(mp))), "φ", "GREEN", "middle", 16, dx=-4,
             dy=-4)
    sc.label(_mid(O, Pt), "r", "HEAD", "end", 17, dx=-8, dy=-8)
    sc.label(_mid(O, F), "r cos φ", "TEXT", "middle", 15, dx=24, dy=34)
    sc.label(_mid(F, Pt, 0.5), "r sin φ", "TEXT", "start", 15, dx=12, dy=14)
    sc.label(Pt, "P", "HEAD", "start", 17, dx=10, dy=-8)
    sc.dotp(Pt, 4)
    G = pp((0, 0, 3 * R / 8))
    sc.mass(G, None, r=5, col="PINK")
    sc.label(G, "G", "HEAD", "end", 17, dx=-12, dy=6)
    sc.dim(_add(O, (-0.2, 0.0)), _add(G, (-0.2, 0.0)), "", off=(0, 0))
    sc.label(_add(_mid(O, G), (-0.2, 0.0)), "3R/8", "TEXT", "end", 14, dx=-8, dy=5)
    sc.dotp(O, 3.5)
    return sc


# ----------------------------------------------------------------------------------------------------------- 11
@figure("t6-tensor-axis",
        "A line through O with unit vector u, a mass element at P, and the right triangle formed by its position vector, "
        "its projection on the line and its distance d to the line.",
        r"The distance $d$ from $dm$ to the line $\ell$ is the leg of the right triangle with hypotenuse "
        r"$\mathbf r_0^P$ and adjacent leg $\mathbf r_0^P\cdot\mathbf u$.")
def tensor_axis():
    sc = Scene(760, 520, (240, 400), 150)
    O = (0.0, 0.0)
    u3 = (0.3, 0.75, 0.58)
    n = math.sqrt(sum(c * c for c in u3))
    u3 = tuple(c / n for c in u3)
    # perpendicular direction: component of -e_z ... use cross with e_x
    w3 = (0.0, u3[2], -u3[1])
    nw = math.sqrt(sum(c * c for c in w3))
    w3 = tuple(c / nw for c in w3)
    a = math.radians(40.0)
    rr = 2.1
    P3 = tuple(rr * (math.cos(a) * u3[i] + math.sin(a) * w3[i]) for i in range(3))
    H3 = tuple(rr * math.cos(a) * u3[i] for i in range(3))
    _axes3(sc, O, (1.7, 2.3, 1.9), subs=("", "", ""))
    P, H = _p(*P3), _p(*H3)
    ux, uy = _p(*u3)
    L1 = (-1.0, 3.0)
    sc.line(_add(O, (ux, uy), -0.5), _add(O, (ux, uy), 3.3), "ACC", 1.2, "7 5")
    sc.label(_add(O, (ux, uy), 3.3), "ℓ", "ACC", "start", 17, dx=8, dy=0)
    triangle(sc, [O, H, P], "BLUE", 0.2)
    sc.dashed(H, P)
    hu = (ux / math.hypot(ux, uy), uy / math.hypot(ux, uy))
    hp = (P[0] - H[0], P[1] - H[1])
    nh = math.hypot(*hp)
    _mark3(sc, H, (-hu[0], -hu[1]), (hp[0] / nh, hp[1] / nh), 0.1)
    sc.vec(O, _add(O, (ux, uy), 1.0), _s("u"), ORANGE, 3.0, name_off=(-12, -12), size=18, head=12)
    sc.vec(O, P, None, "BLUE", 2.6, head=11)
    _square(sc, P, 0.07)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=-8)
    sc.label(P, "dm", ORANGE, "start", 15, weight="700", dx=12, dy=12)
    sc.dotp(H, 3.5)
    sc.label(H, "H", "HEAD", "start", 17, dx=-24, dy=-8)
    sc.label(_mid(O, P), _s("r", "0", "P"), "BLUE", "middle", 16, weight="700", dx=0, dy=24)
    sc.label(_mid(O, H), _s("r", "0", "P") + "·" + _s("u"), "TEXT", "start", 15, dx=14, dy=22)
    sc.label(_mid(H, P), "d", "TEXT", "start", 17, dx=10, dy=4)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=-8)
    return sc


# ----------------------------------------------------------------------------------------------------------- 12
@figure("t6-principal-axes",
        "A square plate with its corner frame along the sides and the principal axes of inertia rotated forty-five degrees, "
        "along the diagonal and across it.",
        r"About the corner $A$ the principal axes of a square plate are the diagonal ($I_1 = Ma^2/12$) and the "
        r"perpendicular in-plane direction ($I_2 = 7Ma^2/12$), a rotation of $\pi/4$ about $\mathbf k_1$.")
def principal_axes():
    sc = Scene(640, 500, (200, 400), 150)
    a = 2.0
    A = (0.0, 0.0)
    sq = [(0, 0), (a, 0), (a, a), (0, a)]
    triangle(sc, sq, "BLUE", 0.10)
    sc.poly(sq, "BLUE", 1.8, close=True)
    fixed_axis(sc, A, 0, 2.5, _s("i", "1"), off=(14, 6))
    fixed_axis(sc, A, 90, 2.5, _s("j", "1"), off=(14, 4))
    axis_out(sc, A, None, "HEAD")
    sc.label(A, _s("k", "1"), "HEAD", "end", 16, weight="700", dx=-14, dy=24)
    sc.label(A, "A", "HEAD", "end", 17, dx=-12, dy=-8)
    e = 1.55
    unit(sc, A, 45, e, _s("e", "1"), off=(-16, -6))
    unit(sc, A, 135, e, _s("e", "2"), off=(-14, -10))
    sc.line(_add(A, _d(45), e), _add(A, _d(45), a * math.sqrt(2)), "BLUE", 1.2, "6 4")
    sc.arc(A, 0.55, 0, 45, "GREEN", 1.7, head=True)
    sc.arc(A, 0.55, 90, 135, "GREEN", 1.7, head=True)
    sc.label(_add(A, _d(22.5), 0.8), "π/4", "GREEN", "middle", 16, dy=5)
    sc.label(_add(A, _d(112.5), 0.85), "π/4", "GREEN", "middle", 16, dx=-8, dy=-2)
    G = (a / 2, a / 2)
    sc.mass(G, None, r=5, col="PINK")
    sc.label(G, "G", "HEAD", "start", 17, dx=10, dy=22)
    sc.label((a / 2, a), "a", "TEXT", "middle", 16, dy=-8)
    sc.label((a, a / 2), "a", "TEXT", "start", 16, dx=8, dy=5)
    return sc


# ----------------------------------------------------------------------------------------------------------- 13
@figure("t6-steiner",
        "A fixed frame at O and a parallel frame at the centre of mass G of a body, with the position vectors of a mass "
        "element from O and from G.",
        r"The frame $S_G$ at the centre of mass is parallel to $S_0$, and $\mathbf r_0^P = \mathbf r_0^G + \mathbf r_G^P$ "
        r"(Notes.pdf Fig. 10.3).")
def steiner():
    sc = Scene(700, 480, (130, 370), 125)
    O = (0.0, 0.0)
    _axes3(sc, O, (1.0, 3.9, 2.5))
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    G = (2.6, 1.3)
    pts = _blobp((2.7, 1.45), 1.0, 0.9)
    triangle(sc, pts, "BLUE", 0.12)
    sc.poly(pts, "BLUE", 1.5, close=True)
    dirs = ((DX, DY), (1.0, 0.0), (0.0, 1.0))
    for dv, nm, off in zip(dirs, ("x", "y", "z"), ((-10, 14), (14, 6), (-12, 0))):
        tip = _add(G, dv, (0.85 if nm == "y" else 0.7))
        sc.vec(G, tip, None, "BLUE", 2.2, head=9)
        sc.label(tip, bold(nm) + S("", "G"), "BLUE", "middle", 16, weight="700", dx=off[0], dy=off[1])
    P = (3.3, 1.95)
    sc.vec(O, G, None, ORANGE, 2.6, head=11)
    sc.vec(G, P, None, "GREEN", 2.6, head=11)
    sc.vec(O, P, None, "HEAD", 2.2, head=11)
    _square(sc, P, 0.07)
    sc.label(P, "dm", ORANGE, "start", 15, weight="700", dx=12, dy=-6)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=16)
    sc.mass(G, None, r=5, col="PINK")
    sc.label(G, "G", "HEAD", "end", 17, dx=-12, dy=-8)
    sc.label(_mid(O, G), _s("r", "0", "G"), ORANGE, "start", 16, weight="700", dx=6, dy=22)
    sc.label(_mid(G, P), _s("r", "G", "P"), "GREEN", "start", 16, weight="700", dx=14, dy=8)
    sc.label(_mid(O, P), _s("r", "0", "P"), "HEAD", "end", 16, weight="700", dx=-10, dy=-12)
    return sc


# ----------------------------------------------------------------------------------------------------------- 14
def _q(x, y, z):
    return (x * QX + y, x * QY + z)


QX, QY = -0.62, -0.5


@figure("t6-parallel-axis",
        "Two parallel vertical axes, one through O and one through the centre of mass G of a body, with the distance "
        "between them.",
        r"Parallel axis theorem: $I_{z_0}$ exceeds $I_{z_G}$ by $m$ times the squared distance between the axes "
        r"(Notes.pdf Fig. 10.4).")
def parallel_axis():
    sc = Scene(860, 580, (310, 300), 120)
    O = (0.0, 0.0)
    xg, yg = 1.8, 1.9
    plane = [_q(-0.3, -0.3, 0), _q(3.0, -0.3, 0), _q(3.0, 3.5, 0), _q(-0.3, 3.5, 0)]
    triangle(sc, plane, "ACC", 0.08)
    sc.poly(plane, "EDGE", 1.0, "4 4", close=True)
    blob = []
    for i in range(60):
        f = 2 * math.pi * i / 60
        rr = 1.0 * (1 + 0.12 * math.sin(3 * f + 0.5) + 0.06 * math.cos(2 * f))
        blob.append(_q(xg + 0.95 * rr * math.cos(f), yg + 0.9 * rr * math.sin(f), 0))
    triangle(sc, blob, "BLUE", 0.2)
    sc.poly(blob, "BLUE", 1.6, close=True)
    Gp = _q(xg, yg, 0)
    # in-plane axes at O (grey) and at G (blue)
    dirs = ((QX, QY), (1.0, 0.0), (0.0, 1.0))
    for dv, nm, ln in zip(dirs[:2], ("x", "y"), (2.6, 3.9)):
        sc.vec(O, _add(O, dv, ln), None, "EDGE", 1.4, head=8)
    sc.label(_q(2.6, 0, 0), bold("x") + S("", "0"), "TEXT", "middle", 16, weight="700", dx=-12, dy=14)
    sc.label(_q(0, 3.9, 0), bold("y") + S("", "0"), "TEXT", "middle", 16, weight="700", dx=14, dy=6)
    sc.vec(Gp, _add(Gp, dirs[0], 0.8), None, "BLUE", 2.2, head=9)
    sc.label(_add(Gp, dirs[0], 0.8), bold("x") + S("", "G"), "BLUE", "middle", 16, weight="700", dx=-10, dy=14)
    sc.vec(Gp, _add(Gp, dirs[1], 1.0), None, "BLUE", 2.2, head=9)
    sc.label(_add(Gp, dirs[1], 1.0), bold("y") + S("", "G"), "BLUE", "middle", 16, weight="700", dx=14, dy=6)
    # vertical axes
    sc.vec(O, (0.0, 2.0), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 2.0), bold("z") + S("", "0"), "TEXT", "middle", 16, weight="700", dx=-14, dy=0)
    sc.vec(Gp, _add(Gp, (0, 1), 2.2), None, "BLUE", 2.2, head=9)
    sc.label(_add(Gp, (0, 1), 2.2), bold("z") + S("", "G"), "BLUE", "middle", 16, weight="700", dx=14, dy=0)
    # distance between the axes and its legs
    L1 = _q(xg, 0, 0)
    L2 = _q(xg, yg, 0)
    sc.dashed(O, L1)
    sc.dashed(L1, L2)
    sc.vec(O, Gp, None, "HEAD", 2.2, head=10)
    sc.label(_mid(O, L1), S("x", "0", "G"), "TEXT", "end", 15, dx=-6, dy=18)
    sc.label(_mid(L1, L2), S("y", "0", "G"), "TEXT", "start", 15, dx=8, dy=18)
    sc.label(Gp, "√((x" + '<tspan baseline-shift="sub" font-size="70%">0</tspan><tspan baseline-shift="super" '
             'font-size="70%">G</tspan>)² + (y<tspan baseline-shift="sub" font-size="70%">0</tspan>'
             '<tspan baseline-shift="super" font-size="70%">G</tspan>)²)', "HEAD", "start", 15, dx=16, dy=-84)
    sc.mass(Gp, None, r=5, col="PINK")
    sc.label(Gp, "G", "HEAD", "start", 17, dx=-24, dy=-10)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=18)
    return sc
