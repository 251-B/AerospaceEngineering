"""Theory figures of Topic 6, inertia half (Sections 10 to 16): mass distributions, centres of mass, symmetry, standard
bodies, tensor and Steiner."""
import math

from figures.em_theory import axis_out, figure, fixed_axis, raster, right_angle, triangle, unit
from figures.em_th.t6 import _add, _blob, _d, S, Scene, bold

ORANGE = "ACC"
DX, DY = -0.789 * 0.6, -0.614 * 0.6          # cabinet depth axis: x towards the lower left, foreshortened


def _p(x, y, z):
    return (x * DX + y, x * DY + z)


def _s(sym, a=None, b=None):
    return S(bold(sym), a, b)


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
raster("t6-mass-distribution",
       "A discrete set of point masses and a continuous body, each with the position vector of one mass from the origin O.",
       r"Discrete (left) and continuous (right) mass distributions, with the position vector $\mathbf r_0^P$ of a mass element from $O$. Copied from Notes.pdf, Fig. 10.1, p. 82", 600)


# ------------------------------------------------------------------------------------------------------------ 2
raster("t6-centre-of-mass",
       "An irregular body with a mass element dm at P and its centre of mass G, both located from O.",
       r"The centre of mass $G$ is the mass-weighted average of the positions $\mathbf r_0^P$ of all the mass elements. Copied from [Lecture 8, Slide 9] (08-inertia-properties.pdf)", 460)


# ------------------------------------------------------------------------------------------------------------ 3
# EXTRA: deduction or per-rotation view, not printed in the official material
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
raster("t6-composite-bodies",
       "A star, a T-shape and a plate with a hole.",
       r"Divide and conquer: a composite body is the sum of simple parts, and a hole is a part of negative mass. Copied from [Lecture 8, Slide 17] (08-inertia-properties.pdf)", 760)


# ------------------------------------------------------------------------------------------------------------ 5
# EXTRA: deduction or per-rotation view, not printed in the official material
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
# EXTRA: deduction or per-rotation view, not printed in the official material
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
# EXTRA: adds the dl element used in the derivation; Notes Fig. 10.2(a) has none
@figure("t6-half-wire",
        "A half circumference of radius R in the upper half plane, with an arc element at angle theta and its centre of "
        "mass on the y axis.",
        r"Half-circumference wire, $\theta$ from $0$ to $\pi$; $G$ lies on the axis of symmetry at $2R/\pi$ "
        r"(Notes.pdf Fig. 10.2(a)).")
def half_wire():
    sc = Scene(700, 610, (300, 330), 220)
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
raster("t6-plate",
       "A rectangular plate of length L and width W centred at O.",
       r"Homogeneous plate of length $L$ and width $W$ centred at $O \equiv G$. The frame $S_1$ at a corner used for Eq. 10.27 is not drawn in the source. Copied from Notes.pdf, p. 85, Fig. 10.2(b)", 340)


# ------------------------------------------------------------------------------------------------------------ 9
raster("t6-half-disk",
       "A half disk of radius R with a polar radius r and the angle theta.",
       r"Half disk of radius $R$ in polar coordinates $(r,\theta)$. Copied from Notes.pdf, p. 85, Fig. 10.2(c)", 300)


# ----------------------------------------------------------------------------------------------------------- 10
raster("t6-half-sphere",
       "A solid hemisphere of radius R on the xy plane with the axes at its centre O.",
       r"Half sphere of radius $R$ with its flat face on $Oxy$, centred at $O$. Copied from Notes.pdf, p. 85, Fig. 10.2(d)", 340)


# ----------------------------------------------------------------------------------------------------------- 11
# EXTRA: deduction or per-rotation view, not printed in the official material
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
# EXTRA: deduction or per-rotation view, not printed in the official material
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
raster("t6-steiner",
       "A fixed frame at O and a parallel frame at the centre of mass G of a body, with the position vectors of a mass element.",
       r"The frame $S_G$ at the centre of mass is parallel to $S_0$, and $\mathbf r_0^P = \mathbf r_0^G + \mathbf r_G^P$. Copied from Notes.pdf, Fig. 10.3, p. 88", 480)


# ----------------------------------------------------------------------------------------------------------- 14
QX, QY = -0.62, -0.5


raster("t6-parallel-axis",
       "Two parallel vertical axes, one through O and one through the centre of mass G of a body.",
       r"Parallel axis theorem: the axes $Oz_0$ and $Gz_G$ are parallel. Copied from Notes.pdf, Fig. 10.4, p. 89", 500)

