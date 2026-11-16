"""Problem RB-12: box rolling without slipping on a fixed semicylinder (plane motion, angle phi of the box)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d, rotation_view, sub
from figures.mech import S, Scene, bold, dot2

ORANGE = "ACC"


# ------------------------------------------------------------------------------------------------ shared helpers
def unit_one(sc, ang, L=1.0, t=0.74, side="up"):
    """The label "1" beside the hypotenuse of a unit-vector triangle (at the fraction t of its length)."""
    p = add((0.0, 0.0), d(ang), L * t)
    sc.label(p, "1", "TEXT", "middle", 15, dx=-4 if side == "up" else -14, dy=-10 if side == "up" else 2)


def plane_rotation(w, h, o, k, ang, names, out, hdr, spin, extra_pre=None, extra_post=None, out_off=(-16, 28),
                   out_kind="out", L=1.0, col="BLUE"):
    """Flat view of a rotation about the normal axis, with the hypotenuse labels "1" and the spin arrow of the rate.

    names = (right, up, rotated right, rotated up); spin = (name, first angle, last angle, name radius) or None."""
    def post(sc):
        unit_one(sc, ang, L, 0.76, "up")
        unit_one(sc, ang + 90, L, 0.76, "left")
        if spin:
            nm, a0, a1, nr = spin
            sc.spin((0.0, 0.0), 0.17, a0, a1, nm, "GREEN", name_r=nr, size=16)
        if extra_post:
            extra_post(sc)
    return rotation_view(w, h, o, k, ang, names[0], names[1], names[2], names[3], out, hdr, pre=extra_pre, post=post,
                         out_off=out_off, out_kind=out_kind, L=L, col=col)


def body_pt(o, ib, jb, x, y):
    return (o[0] + x * ib[0] + y * jb[0], o[1] + x * ib[1] + y * jb[1])


def box_outline(sc, m, ib, jb, b, h, col="HEAD", w=2.2, fill=None):
    """Rectangle of width b along ib and height h along jb whose bottom face is centred at m."""
    pts = [body_pt(m, ib, jb, -b / 2, 0), body_pt(m, ib, jb, b / 2, 0), body_pt(m, ib, jb, b / 2, h),
           body_pt(m, ib, jb, -b / 2, h)]
    if fill:
        sc.poly(pts, col, w, fill=fill, close=True, opacity=0.10)
    else:
        sc.poly(pts, col, w, close=True)


def ground_line(sc, x0, x1, y=0.0, side=-1):
    sc.ground((x0, y), (x1, y), side)


def half_disc_points(c, r, a0, a1, n=72):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


# ------------------------------------------------------------------------------------------------ RB-12
R, B, H = 3.0, 4.0, 1.6
PHI = 20.0
PR = math.radians(PHI)
IB = (math.cos(PR), math.sin(PR))
JB = (-math.sin(PR), math.cos(PR))
C = (-R * math.sin(PR), R * math.cos(PR))
M = (C[0] + R * PR * IB[0], C[1] + R * PR * IB[1])
G = (M[0] + H / 2 * JB[0], M[1] + H / 2 * JB[1])


@figure("rb12-rotation",
        "The body basis i_B, j_B turned counterclockwise by phi from the fixed basis i, j, with k out of the paper.",
        r"Rotation of the box about $\mathbf k$ (⊙) by $\varphi$. The tip of $\mathbf j_B$ moves towards negative "
        r"$\mathbf i$, which gives the minus sign in $\mathbf j_B = -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j$.")
def rotation():
    return plane_rotation(700, 600, (270, 500), 250, 30.0,
                          (bold("i"), bold("j"), S(bold("i"), "B"), S(bold("j"), "B")),
                          bold("k") + " (⊙)", ("φ", ""), ("ω = φ̇", -110, -5, 0.30))


def _cylinder(sc, faint=False):
    pts = half_disc_points((0.0, 0.0), R, 0, 180)
    sc.poly(pts, "EDGE" if faint else "HEAD", 1.8 if faint else 2.2, fill="EDGE", close=True, opacity=0.10 if faint else 0.22)
    ground_line(sc, -R - 0.7, R + 0.7)


@figure("rb12-geometry",
        "The box tilted by phi on the cylinder, with the contact point C, the equal rolled arcs R phi on the cylinder "
        "and on the face, and the right triangle of OC.",
        r"Main plane. Tangency puts $C$ on the radius along $\mathbf j_B$; rolling without slipping makes the segment "
        r"$MC$ on the face equal to the arc $TC$ of the cylinder, both of length $R\varphi$.")
def geometry():
    sc = Scene(820, 700, (410, 610), 105)
    O, T = (0.0, 0.0), (0.0, R)
    _cylinder(sc)
    box_outline(sc, M, IB, JB, B, H, "HEAD", 2.2, fill="ACC")
    # triangle of OC and the dashed lines
    foot = (0.0, R * math.cos(PR))
    triangle(sc, [O, foot, C], ORANGE, 0.22)
    sc.dashed(O, (0.0, R + 0.75))
    sc.dashed(O, C)
    sc.dashed(foot, C)
    right_angle(sc, foot, 270, 180, 0.12)
    sc.label((0.0, R * math.cos(PR) / 2), "R cos φ", "TEXT", "start", 15, dx=9, dy=5)
    sc.label((-R * math.sin(PR) / 2, R * math.cos(PR)), "R sin φ", "TEXT", "middle", 15, dy=18)
    sc.label(add(O, d(90 + PHI), 1.55), "R", "TEXT", "end", 16, dx=-8, dy=4)
    # angle of phi at O
    sc.arc(O, 1.45, 90, 90 + PHI, "GREEN", 1.8, head=True)
    sc.label(add(O, d(90 + PHI / 2), 1.80), "φ", "GREEN", "middle", 17, dx=8, dy=6)
    # equal arcs R phi
    sc.poly(half_disc_points(O, R, 90, 90 + PHI, 24), "GREEN", 4.5)
    sc.line(C, M, "GREEN", 4.5)
    sc.label(add(O, d(90 + PHI / 2), 2.32), "Rφ", "GREEN", "middle", 15, weight="700", dx=-14, dy=9)
    mid = ((C[0] + M[0]) / 2, (C[1] + M[1]) / 2)
    sc.label(mid, "Rφ", "GREEN", "middle", 15, weight="700", dx=-14, dy=-14)
    # points
    for pt, nm, off in ((T, "T", (14, 22)), (C, "C", (-14, 22)), (M, "M", (16, -8)), (G, "G", (-16, -6))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "middle", 17, dx=-14, dy=20)
    # body basis at G and the dimension h/2
    sc.vec(G, add(G, IB, 0.8), sub("i", "B"), "BLUE", 2.8, name_off=(16, 14), size=17, head=11)
    sc.vec(G, add(G, JB, 0.8), sub("j", "B"), "BLUE", 2.8, name_off=(-12, -8), size=17, head=11)
    off = (-0.40 * IB[0], -0.40 * IB[1])
    a, b = add(M, off), add(G, off)
    sc.dim(a, b, "h/2", off=(-24, 4))
    sc.dashed(M, add(M, off, 1.1))
    sc.dashed(G, add(G, off, 1.1))
    return sc


@figure("rb12-fbd",
        "Free-body diagram of the box: weight at G, normal reaction and friction at the contact point C.",
        r"Free-body diagram. The arm from $G$ to $C$ has the components $-R\varphi$ along $\mathbf i_B$ and $-h/2$ along "
        r"$\mathbf j_B$; friction has the arm $h/2$ and the normal reaction the arm $R\varphi$ about $G$.")
def fbd():
    sc = Scene(820, 700, (410, 610), 105)
    _cylinder(sc, faint=True)
    box_outline(sc, M, IB, JB, B, H, "HEAD", 2.2)
    # arm G to C with its components
    corner = add(G, IB, -R * PR)
    sc.dashed(G, corner)
    sc.dashed(corner, C)
    sc.dashed(G, C)
    sc.label(add(G, IB, -R * PR / 2), "Rφ", "TEXT", "middle", 15, dx=-2, dy=-12)
    off = (-0.32 * IB[0], -0.32 * IB[1])
    sc.dim(add(corner, off), add(C, off), "h/2", off=(-26, 4))
    sc.dashed(corner, add(corner, off, 1.1))
    sc.dashed(C, add(C, off, 1.1))
    # forces
    sc.vec(G, (G[0], G[1] - 1.25), "mg", "PINK", 3.0, name_off=(18, 6), size=17, head=12)
    sc.vec(C, add(C, JB, 1.25), "N", "GREEN", 3.0, name_off=(-14, -4), size=17, head=12)
    sc.vec(C, add(C, IB, 1.25), "F", "GREEN", 3.0, name_off=(8, 20), size=17, head=12)
    # body basis at G and the angular acceleration
    sc.vec(G, add(G, IB, 0.7), sub("i", "B"), "BLUE", 2.4, name_off=(16, 12), size=16, head=10)
    sc.vec(G, add(G, JB, 0.7), sub("j", "B"), "BLUE", 2.4, name_off=(-14, -2), size=16, head=10)
    sc.spin(G, 0.42, 30, 100, "φ̈", "GREEN", name_r=0.60)
    for pt, nm, off in ((G, "G", (14, 22)), (C, "C", (-14, 22))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp((0.0, 0.0), 3.5)
    sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=-14, dy=20)
    return sc
