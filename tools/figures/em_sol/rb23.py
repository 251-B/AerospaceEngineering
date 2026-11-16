"""Problem RB-23: rectangular plate with a circular hole hanging on a fixed knob, rolling without slip (angles theta, phi).

This module also holds the small helpers shared by rb28, rb33 and rb37 (hatched disc, rim hatching, right-triangle pair
drawn at an arbitrary point, axonometric ellipse helpers).
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d, rotation_view
from figures.em_sol.rb12 import plane_rotation
from figures.mech import S, Scene, bold, dot1, dot2

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
U1, U2 = S(bold("u"), "1"), S(bold("u"), "2")
I1, J1, K1 = S(I, "1"), S(J, "1"), S(K, "1")
IB, JB = S(I, "B"), S(J, "B")
A1, A2 = S("a", "1"), S("a", "2")
PHI = 30.0
THETA = 20.0


# ------------------------------------------------------------------------------------------------ shared helpers
def circle_pts(c, r, a0=0.0, a1=360.0, n=96):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def hatched_disc(sc, c, r, step=9.0, fill_op=0.12):
    """Fixed disc: light fill, outline and hatching ticks just inside the rim (the centre stays free for labels)."""
    sc.poly(circle_pts(c, r), "HEAD", 2.0, fill="EDGE", close=True, opacity=fill_op)
    rim_hatch(sc, c, r, 0.0, 360.0, inward=True, step=step, length=0.17)


def rim_hatch(sc, c, r, a0, a1, inward=True, step=5.0, length=0.2, slant=35.0):
    """Hatching ticks along the arc a0..a1 of the circle (c, r): on the inside (a solid body) or on the outside."""
    a = a0
    while a <= a1 + 1e-9:
        p = (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
        sgn = -1.0 if inward else 1.0
        da = a + slant * (-sgn)
        q = (p[0] + sgn * length * math.cos(math.radians(da)), p[1] + sgn * length * math.sin(math.radians(da)))
        sc.line(p, q, "EDGE", 1.0)
        a += step


def tri_pair(sc, p, ref, ang, m1, m2, hdr, col="BLUE", L=1.0, arcs=True, arc_r=0.5, off1=(18, -10), off2=(-6, -14)):
    """The two right triangles of one rotation drawn at the point p.

    ref: direction (deg, world) of the old "right" axis, the old "up" axis being ref + 90; ang: counterclockwise
    angle of the rotation (positive); m1, m2: names of the rotated copies. Hypotenuse L, legs L cos, L sin."""
    e1, e2 = d(ref), d(ref + 90)
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    n1, n2 = d(ref + ang), d(ref + ang + 90)
    ccw = ang > 0
    foot1 = add(p, e1, L * c)
    tip1 = add(p, n1, L)
    triangle(sc, [p, foot1, tip1], ORANGE, 0.20)
    sc.dashed(foot1, tip1)
    right_angle(sc, foot1, ref + 180, ref + (90 if ccw else 270), 0.07)
    foot2 = add(p, e2, L * c)
    tip2 = add(p, n2, L)
    triangle(sc, [p, foot2, tip2], ORANGE, 0.20)
    sc.dashed(foot2, tip2)
    right_angle(sc, foot2, ref + 270, ref + (180 if ccw else 0), 0.07)
    unit(sc, p, ref + ang, L, m1, col, off=off1)
    unit(sc, p, ref + ang + 90, L, m2, col, off=off2)
    if arcs:
        sc.arc(p, arc_r, ref, ref + ang, "GREEN", 1.7, head=True)
        sc.arc(p, arc_r, ref + 90, ref + 90 + ang, "GREEN", 1.7, head=True)
    return foot1, tip1, foot2, tip2


def hatch_poly(sc, pts, ang=45.0, step=0.14, col="EDGE"):
    """Diagonal hatching of the convex polygon pts."""
    t, n = d(ang), d(ang + 90)
    ss = [p[0] * n[0] + p[1] * n[1] for p in pts]
    s = min(ss) + step / 2
    m = len(pts)
    while s < max(ss):
        hits = []
        for i in range(m):
            a, b = pts[i], pts[(i + 1) % m]
            sa, sb = ss[i], ss[(i + 1) % m]
            if (sa - s) * (sb - s) < 0:
                f = (s - sa) / (sb - sa)
                hits.append((a[0] + f * (b[0] - a[0]), a[1] + f * (b[1] - a[1])))
        if len(hits) >= 2:
            sc.line(hits[0], hits[1], col, 1.0)
        s += step


# ------------------------------------------------------------------------------------------------ rb23-rot-theta
@figure("rb23-rot-theta",
        "The body basis of the plate, turned counterclockwise by theta from the fixed basis.",
        r"Rotation about $\mathbf k_1$ (⊙) by $\theta$. The longitudinal axis $\mathbf j_B$ is $\mathbf j_1$ turned "
        r"counterclockwise, so its component along $\mathbf i_1$ is minus the sine of $\theta$.")
def rot_theta():
    ang = 30.0
    hw, hl = 1.35, 2.3

    def pre(sc):
        ib, jb = d(ang), d(ang + 90)
        pts = [add(add((0.0, 0.0), ib, sx * hw), jb, sy * hl) for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        sc.poly(pts, "EDGE", 1.2, "7 5", fill="EDGE", close=True, opacity=0.06)

    def post(sc):
        jb = d(ang + 90)
        sc.label(add((0.0, 0.0), jb, hl), "longitudinal axis " + S("y", "B"), "TEXT", "end", 15, dx=-8, dy=-8)
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=14, dy=20)
    return plane_rotation(900, 830, (450, 425), 150, ang, (I1, J1, IB, JB), K1 + " (⊙)", ("θ", ""), None,
                          extra_pre=pre, extra_post=post, out_off=(-44, 22))


# ------------------------------------------------------------------------------------------------ rb23-contact
A1V, A2V = 1.0, 3.0
PR = math.radians(PHI)
U2D = (-math.sin(PR), math.cos(PR))
U1D = (math.cos(PR), math.sin(PR))
OI = (A1V * U2D[0], A1V * U2D[1])
GC = (-(A2V - A1V) * U2D[0], -(A2V - A1V) * U2D[1])


def _knob_scene(w, h, o, k, faint=False):
    sc = Scene(w, h, o, k)
    sc.poly(circle_pts(GC, A2V), "HEAD", 2.0, fill="none", close=True)
    if faint:
        sc.poly(circle_pts((0.0, 0.0), A1V), "EDGE", 1.6, fill="EDGE", close=True, opacity=0.16)
    else:
        hatched_disc(sc, (0.0, 0.0), A1V)
    return sc


def _offset(p, n, k):
    return (p[0] + n[0] * k, p[1] + n[1] * k)


@figure("rb23-contact",
        "The knob and the hole in internal contact at I, with O, I and G aligned along u2 and G at a2 minus a1 from O.",
        r"Contact geometry. The common normal $\mathbf u_2$ is $\mathbf j_1$ turned by $\phi$; $G$ lies on it at "
        r"$a_2 - a_1$ from $O$, opposite to $I$, so $\mathbf r_1^G$ is $-(a_2 - a_1)\,\mathbf u_2$.")
def contact():
    sc = _knob_scene(960, 900, (400, 250), 118)
    O = (0.0, 0.0)
    # faint long axis of the plate through G at theta from the vertical
    jb = (-math.sin(math.radians(THETA)), math.cos(math.radians(THETA)))
    sc.line(add(GC, jb, -3.4), add(GC, jb, 1.55), "EDGE", 1.1, "9 5")
    sc.label(add(GC, jb, -3.4), "long axis of the plate, " + S(bold("j"), "B") + " (θ = 20°)", "TEXT", "end", 14, dx=-4, dy=18)
    fixed_axis(sc, O, 0, 1.75, I1, off=(14, 6))
    fixed_axis(sc, O, 90, 1.75, J1, off=(12, -2))
    # unit vectors and triangle of u2
    tri_pair(sc, O, 0, PHI, U1, U2, "φ", col="GREEN", off1=(18, -8), off2=(-24, 2))
    sc.label(add((0.0, 0.0), d(90 + PHI / 2), 0.5), "φ", "GREEN", "middle", 17, dx=8, dy=-12)
    sc.label(add((0.0, 0.0), d(PHI / 2), 0.5), "φ", "GREEN", "middle", 17, dx=4, dy=24)
    sc.label((0.0, math.cos(PR) / 2), "cos φ", "TEXT", "start", 14, dx=8, dy=6)
    sc.label((-math.sin(PR) * 0.4, math.cos(PR)), "sin φ", "TEXT", "middle", 14, dy=20)
    # points
    sc.mass(OI, None, r=4.5, col="BLUE")
    sc.label(OI, "I", "HEAD", "middle", 17, dx=-4, dy=-14)
    sc.mass(GC, None, r=4.5, col="BLUE")
    sc.label(GC, "G", "HEAD", "middle", 17, dx=-16, dy=-10)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=28)
    sc.label(O, K1 + " (⊙)", "HEAD", "start", 16, weight="700", dx=-62, dy=58)
    sc.note((0.95, 1.05), "fixed knob", "TEXT", "start", 14)
    # dimensions on the lower-left side of the line O-I-G
    n = (-U1D[0], -U1D[1])
    for p, q, off, nm, nmoff in ((O, OI, 0.75, A1, (-34, 4)), (O, GC, 0.75, A2 + " − " + A1, (-30, 14)),
                                 (OI, GC, 1.55, A2, (-18, 4))):
        pa, qa = _offset(p, n, off), _offset(q, n, off)
        sc.dim(pa, qa, nm, off=nmoff)
        sc.dashed(p, _offset(p, n, off + 0.12))
        sc.dashed(q, _offset(q, n, off + 0.12))
    # velocity of G
    sc.vec(GC, add(GC, U1D, 1.7), None, "GREEN", 3.0, head=12)
    sc.label(add(GC, U1D, 1.7), "(" + A2 + " − " + A1 + ") " + dot1("φ"), "GREEN", "start", 16, weight="700", dx=8, dy=-8)
    return sc


# ------------------------------------------------------------------------------------------------ rb23-composite
W, H = 2.0, 4.0
RH = 0.8


def _rect(sc, c, col="HEAD", fill=True):
    pts = [(c[0] - H / 2, c[1] - W / 2), (c[0] + H / 2, c[1] - W / 2), (c[0] + H / 2, c[1] + W / 2),
           (c[0] - H / 2, c[1] + W / 2)]
    sc.poly(pts, col, 2.0, fill="EDGE" if fill else "none", close=True, opacity=0.14 if fill else None)


def _body_axes(sc, c, lx=2.45, ly=1.45):
    """Body axes of the plate: y_B to the right, x_B down (view of statement figure (a))."""
    sc.vec(c, (c[0] + lx, c[1]), S("y", "B"), "EDGE", 1.4, name_off=(14, 4), size=15, head=8)
    sc.vec(c, (c[0], c[1] - ly), S("x", "B"), "EDGE", 1.4, name_off=(-12, 14), size=15, head=8)


@figure("rb23-composite",
        "The plate as a full rectangle minus a centred disc, with the Cartesian and polar mass elements.",
        r"Composite body: full rectangle of mass $\tfrac43 m$ minus the hole of mass $\tfrac13 m$, both centred at $G$. "
        r"The rectangle is integrated in Cartesian coordinates, the hole in polar coordinates with the jacobian $\rho$.")
def composite():
    sc = Scene(1020, 470, (510, 215), 62)
    cs = [(-5.4, 0.0), (0.0, 0.0), (5.4, 0.0)]
    # ---- left: full rectangle Q
    c = cs[0]
    _rect(sc, c)
    _body_axes(sc, c)
    # strip of width dy at y0 and the element dx dy
    y0, dy, dx = 0.55, 0.30, 0.30
    sc.poly([(c[0] + y0, c[1] - W / 2), (c[0] + y0 + dy, c[1] - W / 2), (c[0] + y0 + dy, c[1] + W / 2),
             (c[0] + y0, c[1] + W / 2)], "ACC", 1.0, "4 3", fill="ACC", close=True, opacity=0.22)
    sc.poly([(c[0] + y0, c[1] + 0.35), (c[0] + y0 + dy, c[1] + 0.35), (c[0] + y0 + dy, c[1] + 0.35 - dx),
             (c[0] + y0, c[1] + 0.35 - dx)], "ACC", 1.2, fill="ACC", close=True, opacity=0.65)
    sc.label((c[0] + y0 + dy / 2, c[1] + W / 2), "dy", "TEXT", "middle", 15, dy=-8)
    sc.label((c[0] + y0 + dy, c[1] + 0.20), "dx", "TEXT", "start", 15, dx=8, dy=5)
    sc.note((c[0], c[1] + W / 2 + 0.55), "dm = σ dx dy", "TEXT", "middle", 15)
    sc.label(c, "G", "HEAD", "middle", 17, dx=-12, dy=-6)
    sc.mass(c, None, r=3.5, col="BLUE")
    for xv, nm in ((-H / 2, "−w"), (H / 2, "w")):
        sc.line((c[0] + xv, c[1] - W / 2), (c[0] + xv, c[1] - W / 2 - 0.12), "EDGE", 1.1)
        sc.label((c[0] + xv, c[1] - W / 2 - 0.12), nm, "TEXT", "middle", 14, dy=16)
    for yv, nm in ((-W / 2, "−w/2"), (W / 2, "w/2")):
        sc.line((c[0] - H / 2, c[1] - yv), (c[0] - H / 2 - 0.12, c[1] - yv), "EDGE", 1.1)
        sc.label((c[0] - H / 2 - 0.12, c[1] - yv), nm, "TEXT", "end", 14, dx=-4, dy=5)
    sc.note((c[0], c[1] + W / 2 + 1.05), "Q: mass 4m/3", "HEAD", "middle", 16)
    # ---- minus sign
    sc.label((-1.75, 0.0), "−", "HEAD", "middle", 34, italic=False, dy=10)
    # ---- middle: hole H
    c = cs[1]
    sc.poly(circle_pts(c, RH), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.14)
    r0, dr = 0.42, 0.14
    sc.poly(circle_pts(c, r0 + dr), "ACC", 1.0, "4 3", fill="ACC", close=True, opacity=0.25)
    sc.poly(circle_pts(c, r0), "ACC", 1.0, "4 3", fill="EDGE", close=True, opacity=0.0)
    sc.line(c, add(c, d(35), r0), "HEAD", 1.2)
    sc.label(add(c, d(35), r0 / 2), "ρ", "TEXT", "middle", 15, dx=-2, dy=-8)
    sc.line(add(c, d(-30), r0 + dr / 2), add(c, d(-30), RH + 0.3), "EDGE", 1.0)
    sc.label(add(c, d(-30), RH + 0.3), "dρ", "TEXT", "start", 15, dx=4, dy=14)
    sc.mass(c, None, r=3.5, col="BLUE")
    sc.label(c, "G", "HEAD", "middle", 17, dx=-14, dy=16)
    sc.label(add(c, d(90), RH), S("a", "2") + " = 0.8", "TEXT", "middle", 15, dy=-10)
    sc.note((c[0], c[1] + W / 2 + 0.55), "dm = σ ρ dρ dχ", "TEXT", "middle", 15)
    sc.note((c[0], c[1] + W / 2 + 1.05), "H: mass m/3", "HEAD", "middle", 16)
    # ---- equals sign
    sc.label((2.15, 0.0), "=", "HEAD", "middle", 34, italic=False, dy=10)
    # ---- right: plate with hole
    c = cs[2]
    pts = [(c[0] - H / 2, c[1] - W / 2), (c[0] + H / 2, c[1] - W / 2), (c[0] + H / 2, c[1] + W / 2),
           (c[0] - H / 2, c[1] + W / 2)]
    sc.poly(pts, "HEAD", 2.0, fill="EDGE", close=True, opacity=0.14)
    sc.poly(circle_pts(c, RH), "HEAD", 2.0, fill="#ffffff", close=True)
    sc.label(c, "G", "HEAD", "middle", 17, dx=-12, dy=-6)
    sc.mass(c, None, r=3.5, col="BLUE")
    _body_axes(sc, c)
    sc.note((c[0], c[1] + W / 2 + 0.55), "plate with hole", "TEXT", "middle", 15)
    sc.note((c[0], c[1] + W / 2 + 1.05), "mass m", "HEAD", "middle", 16)
    return sc


# ------------------------------------------------------------------------------------------------ rb23-fbd
@figure("rb23-fbd",
        "Free-body diagram of the plate: weight at G, normal reaction and friction of the knob at I.",
        r"Free-body diagram. The weight has no moment about $G$; the normal reaction acts along $GI$ and has no moment "
        r"either, so only the friction $F$ turns the plate, with the arm $a_2$.")
def fbd():
    sc = _knob_scene(840, 800, (360, 330), 62, faint=True)
    O = (0.0, 0.0)
    th = math.radians(THETA)
    ib, jb = (math.cos(th), math.sin(th)), (-math.sin(th), math.cos(th))
    hw, hl = 3.76, 4.4
    # plate outline: the long sides solid, the short ends dashed (the plate continues)
    c1, c2 = add(add(GC, ib, -hw), jb, -hl), add(add(GC, ib, hw), jb, -hl)
    c3, c4 = add(add(GC, ib, hw), jb, hl), add(add(GC, ib, -hw), jb, hl)
    sc.line(c1, c4, "HEAD", 2.0)
    sc.line(c2, c3, "HEAD", 2.0)
    sc.line(c1, c2, "EDGE", 1.2, "6 5")
    sc.line(c3, c4, "EDGE", 1.2, "6 5")
    sc.line(add(GC, jb, -hl), add(GC, jb, hl), "EDGE", 1.0, "9 5")
    sc.label(add(GC, jb, hl), S(bold("j"), "B"), "TEXT", "start", 16, weight="700", dx=8, dy=14)
    # forces
    sc.vec(GC, (GC[0], GC[1] - 1.9), None, "PINK", 3.2, head=12)
    sc.label((GC[0], GC[1] - 1.9), "mg", "PINK", "start", 17, weight="700", dx=10, dy=18)
    sc.vec(OI, add(OI, U2D, 1.9), None, "GREEN", 3.2, head=12)
    sc.label(add(OI, U2D, 1.9), "N " + U2, "GREEN", "end", 17, weight="700", dx=-8, dy=-6)
    sc.vec(OI, add(OI, U1D, 1.9), None, "GREEN", 3.2, head=12)
    sc.label(add(OI, U1D, 1.9), "F " + U1, "GREEN", "start", 17, weight="700", dx=8, dy=-8)
    # arm from G to I, drawn offset to the right of the line G-I (the line carries N)
    n = U1D
    pa, qa = _offset(GC, n, 0.95), _offset(OI, n, 0.95)
    sc.dim(pa, qa, A2 + " " + U2, off=(34, 6))
    sc.dashed(GC, _offset(GC, n, 1.07))
    sc.dashed(OI, _offset(OI, n, 1.07))
    # angular acceleration about G
    sc.spin(GC, 0.7, 150, 250, dot2("θ"), "GREEN", name_r=1.0)
    for pt, nm, off in ((OI, "I", (-14, -6)), (GC, "G", (-16, 22)), (O, "O", (-16, 22))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    return sc
