"""Theory figures of Topic 8 (Constraints, Rolling Motion, Multibody Systems and Torque-Free Motion)."""
import math

from figures.em_theory import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_th.t6 import _add, _ax, _blob, _d, _rotation_view
from figures.mech import S, Scene, bold

TD = "θ̇"
ORANGE = "ACC"
DRED = "#be123c"


def _sub(sym, a=None, b=None):
    return S(bold(sym), a, b)


def _ell(c, rx, ry, rot=0.0, n=90, a0=0.0, a1=360.0):
    """Points of an ellipse (or an arc of it) about c, with its first axis turned by rot degrees."""
    cr, sr = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    pts = []
    for i in range(n + 1):
        t = math.radians(a0 + (a1 - a0) * i / n)
        x, y = rx * math.cos(t), ry * math.sin(t)
        pts.append((c[0] + x * cr - y * sr, c[1] + x * sr + y * cr))
    return pts


def _pv(x, y, z):
    """Oblique projection used for the 3D sketches: x to the right, y receding to the upper right, z up."""
    return (x + 0.45 * y, z + 0.28 * y)


# oblique frame of the portal (x down-left, y right, z up), x foreshortened
_EX = (-0.789 * 0.6, -0.614 * 0.6)


def _p3(x, y, z):
    return (x * _EX[0] + y, x * _EX[1] + z)


def _body(sc, c, r, phase=0.0, sy=0.82, col="BLUE", op=0.16):
    pts = _blob(c, r, phase, sy=sy)
    triangle(sc, pts, col, op)
    sc.poly(pts, col, 1.6, close=True)
    return pts


# --------------------------------------------------------------------------------------------------------------------
@figure("t8-joints",
        "Left, a ball-and-socket joint between two bodies B1 and B2 at the point C; right, a pin connection with the pin "
        "axis Cz pointing out of the paper.",
        r"Fig. 13.1. Ball-and-socket joint (left): $C$ is a point of both bodies, no orientation is constrained. Pin "
        r"connection (right): the axis $Cz$ (out of the paper $\odot$) belongs to both bodies and only the rotation about "
        r"it is free.")
def joints():
    sc = Scene(840, 330, (50, 170), 100)
    # ---------------- left: ball and socket
    C = (2.0, 0.0)
    b1 = _blob((1.0, 0.0), 0.95, 0.4, sy=0.9)
    b2 = _blob((3.05, 0.0), 0.95, 1.9, sy=0.9)
    triangle(sc, b1, "BLUE", 0.14)
    sc.poly(b1, "BLUE", 1.6, close=True)
    triangle(sc, b2, "ACC", 0.16)
    sc.poly(b2, "ACC", 1.6, close=True)
    sc.circle(C, 0.55, "HEAD", 1.8, fill="HEAD", opacity=0.14)
    sc.arc(C, 0.72, 135, 225, "HEAD", 2.4)
    sc.dotp(C, 3.4)
    sc.label(C, "C", "HEAD", "middle", 17, dx=2, dy=-68)
    sc.label((0.55, 0.15), S("B", "1"), "BLUE", "middle", 18, dx=0, dy=0)
    sc.label((3.45, 0.15), S("B", "2"), ORANGE, "middle", 18, dx=0, dy=0)
    sc.note((0.85, -1.3), "ball-and-socket joint", "TEXT", "start", 14)
    # ---------------- right: pin connection (axis Cz out of the paper)
    C2 = (6.1, 0.0)
    l1 = [(4.3, -0.38), (6.1, -0.38), (6.1, 0.38), (4.3, 0.38)]
    l2 = [(6.1, -0.38), (7.9, -0.38), (7.9, 0.38), (6.1, 0.38)]
    triangle(sc, l1, "BLUE", 0.14)
    sc.poly(l1, "BLUE", 1.6, close=True)
    triangle(sc, l2, "ACC", 0.16)
    sc.poly(l2, "ACC", 1.6, close=True)
    sc.circle(C2, 0.3, "HEAD", 1.8, fill="HEAD", opacity=0.14)
    unit(sc, C2, 0, 0.9, bold("x"), off=(14, 8))
    unit(sc, C2, 90, 1.0, bold("y"), off=(12, 2))
    axis_out(sc, C2, None, "HEAD", r_px=8)
    sc.label(C2, bold("z"), "HEAD", "start", 16, dx=14, dy=26)
    sc.label(C2, "C", "HEAD", "end", 17, dx=-16, dy=-22)
    sc.label((5.0, 0.0), S("B", "1"), "BLUE", "middle", 18, dy=6)
    sc.label((7.45, -0.2), S("B", "2"), ORANGE, "middle", 18, dy=6)
    sc.note((4.7, -1.3), "pin connection", "TEXT", "start", 14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t8-collars",
        "A collar on a cylindrical bar that slides along and rotates about z1, and a collar on a prismatic bar that only "
        "slides, with the axes z1 = z2, x1 and x2.",
        r"Fig. 13.2. Left: collar on a cylindrical bar, free to slide along and to turn about $z_1\equiv z_2$ by an angle "
        r"$\phi$ between $x_1$ and $x_2$. Right: collar on a prismatic bar, free only to slide ($x_1\equiv x_2$).")
def collars():
    sc = Scene(900, 450, (170, 225), 100)

    def panel(x0, rot, tag):
        bar = [(x0 - 0.14, -1.55), (x0 + 0.14, -1.55), (x0 + 0.14, 1.65), (x0 - 0.14, 1.65)]
        triangle(sc, bar, "BLUE", 0.18)
        sc.poly(bar, "BLUE", 1.6, close=True)
        col = [(x0 - 0.34, -0.5), (x0 + 0.34, -0.5), (x0 + 0.34, 0.5), (x0 - 0.34, 0.5)]
        triangle(sc, col, "ACC", 0.30)
        sc.poly(col, "ACC", 1.7, close=True)
        arm = [(x0 + 0.34, -0.14), (x0 + 1.9, -0.14), (x0 + 1.9, 0.14), (x0 + 0.34, 0.14)]
        triangle(sc, arm, "ACC", 0.30)
        sc.poly(arm, "ACC", 1.7, close=True)
        # common axis z1 = z2 (dashed) and x2
        sc.line((x0, -1.45), (x0, 1.95), "EDGE", 1.3, "6 4")
        sc.line((x0 + 0.34, 0.0), (x0 + 2.4, 0.0), "EDGE", 1.3, "6 4")
        sc.label((x0, 1.95), S("z", "1") + " ≡ " + S("z", "2"), "TEXT", "middle", 16, dx=0, dy=-8)
        sc.label((x0 + 2.4, 0.0), S("x", "2") if rot else S("x", "1") + " ≡ " + S("x", "2"), "TEXT", "start", 16, dx=8, dy=-6)
        # sliding double arrow
        sc.vec((x0 - 0.62, -0.1), (x0 - 0.62, 0.62), None, "HEAD", 1.8, head=9)
        sc.vec((x0 - 0.62, 0.1), (x0 - 0.62, -0.62), None, "HEAD", 1.8, head=9)
        sc.dotp((x0, 0.0), 3.2)
        sc.label((x0, 0.0), "C", "HEAD", "middle", 17, dx=-24, dy=26)
        sc.label((x0, 1.3), S("B", "1"), "BLUE", "middle", 18, dx=-30, dy=0)
        sc.label((x0 + 1.4, 0.0), S("B", "2"), ORANGE, "middle", 18, dx=0, dy=-18)
        sc.note((x0 - 0.5, -1.9), tag, "TEXT", "start", 13)

    panel(0.0, True, "cylindrical bar (slides and turns)")
    panel(4.2, False, "prismatic bar (slides only)")
    # angle phi between x2 and x1 on the left panel
    x0 = 0.0
    sc.line((x0, 0.0), (x0 + 1.55 * math.cos(math.radians(-38)), 1.55 * math.sin(math.radians(-38))), "EDGE", 1.3, "6 4")
    sc.label((x0 + 1.55 * math.cos(math.radians(-38)), 1.55 * math.sin(math.radians(-38))), S("x", "1"), "TEXT", "start", 16,
             dx=8, dy=14)
    sc.arc((x0, 0.0), 0.95, -38, 0, "GREEN", 1.7, head=True)
    sc.label((x0 + 0.95 * math.cos(math.radians(-19)), 0.95 * math.sin(math.radians(-19))), "φ", "GREEN", "start", 17, dx=10, dy=4)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _arc_len(fn, t0, t1, n=200):
    s = 0.0
    p = fn(t0)
    for i in range(1, n + 1):
        q = fn(t0 + (t1 - t0) * i / n)
        s += math.hypot(q[0] - p[0], q[1] - p[1])
        p = q
    return s


@figure("t8-rolling-contact",
        "Two smooth bodies B1 and B2 in contact at a single point C with the contact basis: normal e_n, tangent e_t1 in the "
        "paper and tangent e_t2 out of it, and the equal arc lengths s1 and s2 swept on both perimeters.",
        r"Rolling contact, Fig. 13.3. At the contact point $C$ the frame $S_C$ has $\mathbf e_n$ along the common normal, "
        r"$\mathbf e_{t1}$ in the tangent plane and $\mathbf e_{t2}$ out of the paper $\odot$; rolling without slipping "
        r"makes the arcs $s_1-s_1(0)$ and $s_2-s_2(0)$ equal.")
def rolling_contact():
    sc = Scene(800, 430, (390, 235), 110)
    C = (0.0, 0.0)
    r1 = (1.7, 1.3)
    r2 = (1.4, 1.05)
    c1 = (-r1[0], 0.0)
    c2 = (r2[0], 0.0)
    p1 = lambda a: (c1[0] + r1[0] * math.cos(a), r1[1] * math.sin(a))
    p2 = lambda b: (c2[0] - r2[0] * math.cos(b), r2[1] * math.sin(b))
    for c, r, col in ((c1, r1, "BLUE"), (c2, r2, "ACC")):
        pts = _ell(c, r[0], r[1])
        triangle(sc, pts, col, 0.14)
        sc.poly(pts, col, 1.7, close=True)
    a1 = math.radians(55)
    s_len = _arc_len(p1, 0.0, a1)
    lo, hi = 0.0, math.pi / 2
    for _ in range(50):
        mid = (lo + hi) / 2
        if _arc_len(p2, 0.0, mid) < s_len:
            lo = mid
        else:
            hi = mid
    b1 = lo
    for fn, t1 in ((p1, a1), (p2, b1)):
        sc.poly([fn(t1 * i / 60) for i in range(61)], "PINK", 3.4)
    # starting ticks s(0)
    for fn, t1, sg in ((p1, a1, -1), (p2, b1, 1)):
        q = fn(t1)
        sc.dotp(q, 4.2, "PINK")
    sc.label(p1(a1), S("s", "1") + "(0)", "PINK", "end", 16, dx=-10, dy=-4)
    sc.label(p2(b1), S("s", "2") + "(0)", "PINK", "start", 16, dx=10, dy=-4)
    sc.label(p1(a1 * 0.5), S("s", "1"), "PINK", "end", 17, dx=-10, dy=6)
    sc.label(p2(b1 * 0.5), S("s", "2"), "PINK", "start", 17, dx=10, dy=6)
    # contact basis
    unit(sc, C, 0, 1.0, S(bold("e"), "n"), off=(8, -14))
    unit(sc, C, 90, 1.0, S(bold("e"), "t1"), off=(-6, -14))
    axis_out(sc, C, None, "HEAD", r_px=9)
    sc.label(C, S(bold("e"), "t2"), "HEAD", "end", 16, dx=-14, dy=30)
    sc.dotp(C, 2.4)
    sc.label((-1.5, 0.35), S("B", "1"), "BLUE", "middle", 19)
    sc.label((2.25, 0.35), S("B", "2"), ORANGE, "middle", 19)
    sc.label(C, "C", "HEAD", "start", 17, dx=16, dy=26)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _floor(sc, x0, x1, y):
    sc.ground((x0, y), (x1, y), side=-1, step=9, length=10)


@figure("t8-disk-rolling",
        "A disk B of radius R rolling without slipping on a horizontal floor F, with the fixed frame at O, the frame S_G "
        "at the centre G, the clockwise angle theta and the equal arcs R theta on the disk and on the floor.",
        r"Disk rolling without slip, Fig. 13.4. $S_0$ is fixed to the floor ($\mathbf k_0$ out of the paper $\odot$); the "
        r"disk turns clockwise by $\theta$, so $\boldsymbol\omega_{B0}$ points into the paper $\otimes$, and the arc $R\theta$ "
        r"on the floor equals the arc on the disk.")
def disk_rolling():
    sc = Scene(760, 470, (120, 250), 125)
    R, TH = 1.0, 1.25
    O = (0.0, 0.0)
    G = (R * TH, 0.0)
    C = (G[0], -R)
    _floor(sc, -0.55, 3.9, -R)
    # disk
    sc.circle(G, R, "BLUE", 2.0, fill="BLUE", opacity=0.16)
    # arc swept on the disk (from the contact point back to the initial contact point) and on the floor
    a_end = 270.0 - math.degrees(TH)
    sc.arc(G, R, a_end, 270.0, "PINK", 3.6)
    sc.line((0.0, -R), (C[0], -R), "PINK", 3.6)
    sc.line((0.0, -R - 0.11), (0.0, -R + 0.11), "PINK", 2.4)
    sc.label((0.4, -R), "Rθ", "PINK", "middle", 17, dy=-10)
    # radius to the initial contact point and the angle theta (clockwise)
    P0 = _add(G, _d(a_end), R)
    sc.line(G, P0, "PINK", 1.5, "6 4")
    sc.arc(G, 0.42, 270.0, a_end, "GREEN", 1.8, head=True)
    sc.label(_add(G, _d((270 + a_end) / 2), 0.42), "θ", "GREEN", "middle", 17, dx=-6, dy=24)
    sc.dashed(G, C)
    # S_G axes (blue) and the radius vector
    sc.vec(G, _add(G, (1, 0), 1.55), S(bold("x"), "G"), "BLUE", 2.0, name_off=(18, 6), size=16, head=9)
    sc.vec(G, _add(G, (0, 1), 1.35), S(bold("y"), "G"), "BLUE", 2.0, name_off=(16, 4), size=16, head=9)
    sc.vec(G, _add(G, _d(32), R), bold("R"), "BLUE", 2.4, name_off=(14, -6), size=17, head=10)
    sc.dotp(G, 4)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=-8)
    sc.dotp(C, 4)
    sc.label(C, S("C", None, None) + "(B)", "HEAD", "start", 16, dx=12, dy=-10)
    sc.label(C, "C(F)", "HEAD", "middle", 16, dx=0, dy=44)
    # fixed frame at O (grey) and the coordinate x0G
    fixed_axis(sc, O, 90, 1.5, bold("y") + S("", "0"), off=(16, 4))
    fixed_axis(sc, O, 0, 0.5, "", off=(0, 0))
    sc.label((0.12, 0.0), bold("x") + S("", "0"), "TEXT", "middle", 16, weight="700", dy=22)
    sc.line((0.5, 0.0), G, "EDGE", 1.2, "5 4")
    sc.label((0.9, 0.0), S("x", "0", "G"), "TEXT", "middle", 16, dy=-16)
    sc.dotp(O, 3.6)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=18)
    axis_out(sc, (-0.5, 0.75), bold("k") + S("", "0"), "HEAD", off=(0, 28))
    # angular velocity into the paper
    axis_in(sc, (G[0] + 1.2, 1.15), None, "GREEN")
    sc.label((G[0] + 1.2, 1.15), S(bold("ω"), "B0"), "GREEN", "start", 17, dx=16, dy=6)
    sc.note((3.2, -1.3), "floor F", "TEXT", "start", 13)
    return sc


@figure("t8-disk-velocity",
        "The disk rolling without slip with the vector from the contact point C to the centre G, the zero velocity of C, the "
        "velocity of G and the angular velocity into the paper.",
        r"Velocity field of the rolling disk: $\mathbf v_0^{C(B)}=\mathbf 0$, $\overrightarrow{CG}=R\,\mathbf j_0$ and "
        r"$\boldsymbol\omega_{B0}=-\dot\theta\,\mathbf k_0$ (into the paper $\otimes$) give $\mathbf v_0^G=R\dot\theta\,"
        r"\mathbf i_0$.")
def disk_velocity():
    sc = Scene(780, 440, (140, 250), 125)
    R = 1.0
    G = (1.9, 0.0)
    C = (G[0], -R)
    _floor(sc, -0.3, 4.1, -R)
    sc.circle(G, R, "BLUE", 2.0, fill="BLUE", opacity=0.14)
    # contact point at rest, vector CG, velocity of G, angular velocity
    sc.vec(C, G, None, ORANGE, 3.0, head=11)
    sc.label(_add(C, (0, 1), 0.5), _sub("CG") + " = R " + _sub("j", "0"), ORANGE, "end", 16, dx=-12, dy=6)
    sc.vec(G, _add(G, (1, 0), 1.2), None, "BLUE", 3.0, head=11)
    sc.label(_add(G, (1, 0), 1.2), _sub("v", "0", "G") + " = R" + TD + " " + _sub("i", "0"), "BLUE", "start", 16, dx=12, dy=-10)
    sc.dotp(G, 4)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=-10)
    sc.dotp(C, 4.5)
    sc.label(C, _sub("v", "0", "C(B)") + " = 0", "BLUE", "end", 16, dx=-12, dy=34)
    sc.label(C, "C", "HEAD", "start", 17, dx=12, dy=34)
    wp = (G[0] + 1.25, 0.8)
    axis_in(sc, wp, None, "GREEN")
    sc.label(wp, _sub("ω", "B0") + " = −" + TD + " " + _sub("k", "0"), "GREEN", "start", 16, dx=16, dy=6)
    # fixed axes
    O = (0.05, 1.15)
    fixed_axis(sc, O, 0, 0.8, _ax("i", "0"), off=(16, 4))
    fixed_axis(sc, O, 90, 0.7, _ax("j", "0"), off=(16, 0))
    axis_out(sc, O, _ax("k", "0"), "HEAD", off=(-4, 32))
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t8-wobbling-disk",
        "A disk of radius R rolling and wobbling three-dimensionally on a floor, with the contact point C, the vertical "
        "axis k and the curved trace of C on the floor.",
        r"Fig. 13.5. A disk $B$ rolling without slip and wobbling on the floor $F$: the trace of the contact point $C$ is a "
        r"two-dimensional curve, so two coordinates are needed to place $C$ in the plane.")
def wobbling_disk():
    sc = Scene(720, 470, (60, -48), 120)
    G = (3.0, -2.05)
    a, b, rot = 1.0, 0.33, 72.0
    ring = _ell(G, a, b, rot)
    C = min(ring, key=lambda p: p[1])
    # floor: translucent parallelogram around C (y receding)
    fl = [(C[0] - 2.6, C[1] + 0.05), (C[0] + 0.2, C[1] + 0.95), (C[0] + 2.7, C[1] + 0.05), (C[0] - 0.1, C[1] - 0.75)]
    triangle(sc, fl, "BLUE", 0.07)
    sc.poly(fl, "EDGE", 1.2, close=True)
    # trace of C on the floor (dashed curve ending at C)
    tr = []
    for i in range(60):
        t = i / 59
        tr.append((C[0] - 2.0 * (1 - t), C[1] + 0.08 + 0.17 * math.sin(7.0 * (1 - t)) * (1 - t) + 0.26 * (1 - t) ** 2))
    tr[-1] = C
    sc.poly(tr, "PINK", 2.0, "6 4")
    triangle(sc, ring, "HEAD", 0.08)
    sc.poly(ring, "HEAD", 2.0, close=True)
    sc.poly(_ell((G[0] + 0.05, G[1]), a, b, rot), "HEAD", 1.2, close=True)
    sc.vec(C, (C[0], C[1] + 2.2), bold("k"), "HEAD", 2.4, name_off=(-14, 4), size=17, head=11)
    sc.dotp(G, 4.5)
    sc.label(G, "G", "HEAD", "start", 17, dx=12, dy=4)
    sc.dotp(C, 4.5)
    sc.label(C, "C", "HEAD", "middle", 17, dx=14, dy=24)
    sc.label((G[0] + 0.85, G[1] + 0.3), "B", "BLUE", "middle", 18)
    sc.note((C[0] + 1.6, C[1] - 0.5), "floor F", "TEXT", "start", 13)
    sc.label((C[0] - 2.0, C[1] + 0.55), "trace of C", "PINK", "start", 15, dy=-6)
    return sc


@figure("t8-disk-height",
        "Right triangle in the vertical plane through the disk axis: the hypotenuse GC of length R in the plane of the disk, "
        "the vertical leg R sin theta and the horizontal leg R cos theta, with theta at C and between the axis and the vertical.",
        r"Height of the centre of a rolling disk: $z_0^G=R\sin\theta$ from the shaded right triangle. The angle at $C$ "
        r"between the disk plane and the floor equals the nutation $\theta$ between the disk axis and the vertical "
        r"($\mathbf i_1=\mathbf i_2$ out of the paper $\odot$).")
def disk_height():
    sc = Scene(640, 440, (150, 330), 140)
    R, TH = 1.3, 50.0
    t = math.radians(TH)
    C = (0.0, 0.0)
    G = (R * math.cos(t), R * math.sin(t))
    foot = (G[0], 0.0)
    _floor(sc, -0.8, 3.7, 0.0)
    # the disk seen edge-on (thick segment through G, length 2R)
    top = (2 * G[0], 2 * G[1])
    sc.line(C, top, "HEAD", 5.0)
    # shaded right triangle
    triangle(sc, [C, foot, G], "ACC", 0.22)
    sc.dashed(G, foot)
    right_angle(sc, foot, 180, 90, 0.09)
    sc.dashed(G, (G[0], G[1] + 1.1))
    # disk axis (perpendicular to the disk plane through G)
    ax_end = _add(G, _d(TH + 90), 1.1)
    sc.vec(G, ax_end, _sub("k", "b"), "BLUE", 2.6, name_off=(-4, -12), size=17, head=11)
    # angles: theta at C and theta between the axis and the vertical (counter-clockwise views, i1 out of the paper)
    sc.arc(C, 0.7, 0, TH, "GREEN", 1.8, head=True)
    sc.label(_add(C, _d(TH / 2), 0.7), "θ", "GREEN", "start", 17, dx=8, dy=8)
    sc.arc(G, 0.62, 90, 90 + TH, "GREEN", 1.8, head=True)
    sc.label(_add(G, _d(90 + TH / 2), 0.62), "θ", "GREEN", "end", 17, dx=-6, dy=-6)
    sc.label(_add(C, _d(TH), R / 2), "R", "HEAD", "end", 17, dx=-8, dy=-6)
    sc.label((G[0], G[1] / 2), "R sin θ", "TEXT", "start", 16, dx=10, dy=6)
    sc.label((G[0] / 2, 0.0), "R cos θ", "TEXT", "middle", 16, dy=34)
    sc.dotp(G, 4.5)
    sc.label(G, "G", "HEAD", "start", 17, dx=14, dy=-4)
    sc.dotp(C, 4.5)
    sc.label(C, "C", "HEAD", "middle", 17, dx=-14, dy=22)
    # axes in the view: j1 to the right, k1 up, i1 = i2 out of the paper
    O = (2.45, 0.35)
    fixed_axis(sc, O, 0, 0.7, _ax("j", "1"), off=(16, 4))
    fixed_axis(sc, O, 90, 0.7, _ax("k", "1"), off=(14, 0))
    axis_out(sc, O, None, "HEAD", r_px=8)
    sc.label(O, bold("i") + S("", "1") + " = " + bold("i") + S("", "2"), "HEAD", "start", 15, dx=-34, dy=30)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t8-disk-slip",
        "Free-body diagram of the skidding disk: the weight at G, the normal reaction N and the friction force R at the "
        "contact point, the velocity of G and the slip velocity of C(B).",
        r"Skidding disk: the slip velocity $\mathbf v_0^{C(B)}=(v_0^G-R\dot\theta)\,\mathbf i_0$ points to the left, so "
        r"the friction $\mathbf R=\mu N\,\mathbf i_0$ points to the right; $\mathbf N$ and the weight act on the vertical "
        r"through $G$ and $\mathbf k_0$ points out of the paper.")
def disk_slip():
    sc = Scene(740, 450, (150, 235), 125)
    R = 1.0
    G = (1.6, 0.0)
    C = (G[0], -R)
    _floor(sc, -0.4, 3.9, -R)
    sc.circle(G, R, "BLUE", 2.0, fill="BLUE", opacity=0.14)
    sc.dotp(G, 4.5)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-18, dy=-12)
    sc.dotp(C, 4.5)
    sc.label(C, "C(B)", "HEAD", "start", 16, dx=40, dy=36)
    # kinematics (blue): velocity of G, and the slip velocity of C(B) drawn just below the floor
    sc.vec(G, _add(G, (1, 0), 1.0), _sub("v", "0", "G"), "BLUE", 2.8, name_off=(30, 12), size=17, head=10)
    q = (C[0], C[1] - 0.27)
    sc.dashed(C, q)
    sc.vec(q, _add(q, (-1, 0), 0.9), _sub("v", "0", "C(B)"), "BLUE", 2.8, name_off=(-6, 26), size=16, head=10)
    wp = (G[0] - 0.5, 0.4)
    axis_in(sc, wp, None, "GREEN")
    sc.label(wp, _sub("ω", "B0"), "GREEN", "start", 17, dx=14, dy=6)
    # forces (pink): weight at G, normal and friction at C
    sc.vec(G, (G[0], G[1] - 0.42), S("m ") + "g", "PINK", 3.0, name_off=(28, 4), size=17, head=11)
    sc.vec(C, (C[0], C[1] + 0.42), bold("N"), "PINK", 3.2, name_off=(-14, 8), size=18, head=12)
    sc.vec(C, _add(C, (1, 0), 1.0), bold("R"), "PINK", 3.2, name_off=(16, 22), size=18, head=12)
    # fixed axes
    O = (-0.35, 0.5)
    fixed_axis(sc, O, 0, 0.8, _ax("i", "0"), off=(16, 4))
    fixed_axis(sc, O, 90, 0.7, _ax("j", "0"), off=(16, 0))
    axis_out(sc, O, _ax("k", "0"), "HEAD", off=(-4, 34))
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _table(sc, ox, legs, tag):
    """Table in oblique projection: top slab 2.0 x 1.4, height 1.0, with the feet at the given (x, y) positions."""
    W, D, H = 2.0, 1.4, 1.05
    # legs behind the top first
    for (x, y) in sorted(legs, key=lambda q: -q[1]):
        a = _pv(ox + x, y, 0.0)
        b = _pv(ox + x, y, H)
        sc.line(a, b, "HEAD", 4.5)
    top = [_pv(ox, 0, H + 0.1), _pv(ox + W, 0, H + 0.1), _pv(ox + W, D, H + 0.1), _pv(ox, D, H + 0.1)]
    front = [_pv(ox, 0, H), _pv(ox + W, 0, H), _pv(ox + W, 0, H + 0.1), _pv(ox, 0, H + 0.1)]
    side = [_pv(ox + W, 0, H), _pv(ox + W, D, H), _pv(ox + W, D, H + 0.1), _pv(ox + W, 0, H + 0.1)]
    triangle(sc, top, "BLUE", 0.30)
    sc.poly(top, "BLUE", 1.6, close=True)
    triangle(sc, front, "BLUE", 0.50)
    sc.poly(front, "BLUE", 1.4, close=True)
    triangle(sc, side, "BLUE", 0.40)
    sc.poly(side, "BLUE", 1.4, close=True)
    # reactions at the feet
    for i, (x, y) in enumerate(legs):
        f = _pv(ox + x, y, 0.0)
        sc.vec(f, (f[0], f[1] + 0.62), None, "PINK", 3.0, head=11)
        sc.dotp(f, 3.6)
        sc.label(f, S(bold("N"), None, f"P{i + 1}"), "PINK", "middle", 16, dx=0, dy=22)
    Gp = _pv(ox + W / 2, D / 2, H + 0.1)
    sc.vec(Gp, (Gp[0], Gp[1] - 0.62), bold("W"), "PINK", 3.0, name_off=(-18, 8), size=17, head=11)
    sc.dotp(Gp, 4)
    sc.label(Gp, "G", "HEAD", "middle", 16, dx=-14, dy=-10)
    sc.note(_pv(ox + 0.1, 0, -0.55), tag, "TEXT", "start", 14)


@figure("t8-table-legs",
        "A table with three legs (determinate reactions) and a table with four legs (indeterminate, hyperstatic reactions), "
        "with the normal reaction at each foot and the weight at the centre of mass.",
        r"Fig. 13.6. Determinate (left, $n=3$) and undetermined (right, $n>3$) system of reactions on a rigid table: "
        r"equilibrium gives only three scalar equations for the normal forces $\mathbf N^{P_i}$.")
def table_legs():
    sc = Scene(880, 400, (40, 240), 135)
    _table(sc, 0.0, [(0.2, 0.2), (1.8, 0.2), (1.0, 1.15)], "n = 3 legs: determinate")
    _table(sc, 3.3, [(0.2, 0.2), (1.8, 0.2), (1.8, 1.2), (0.2, 1.2)], "n > 3 legs: hyperstatic")
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _frame3(sc, o, names, col, length, offs, w=2.2):
    dirs = [(-0.789, -0.614), (1.0, 0.0), (0.0, 1.0)]
    for dv, nm, off in zip(dirs, names, offs):
        sc.vec(o, _add(o, dv, length), nm, col, w, name_off=off, size=15, head=8)


def _two_body_common(sc, exploded):
    # fixed frame at O
    O = (0.0, 0.0)
    for dv, ln, nm, off in (((-0.789, -0.614), 0.9, bold("x"), (-12, 14)), ((1.0, 0.0), 1.0, bold("y"), (12, 8)),
                            ((0.0, 1.0), 1.0, bold("z"), (-10, 2))):
        sc.vec(O, _add(O, dv, ln), None, "EDGE", 1.5, head=8)
        sc.label(_add(O, dv, ln), nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    sc.dotp(O, 3.6)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=18)


@figure("t8-two-bodies",
        "Two rigid bodies B1 and B2 joined by a ball-and-socket joint at the common body point C, with external forces at P1 "
        "and P2 and an equal and opposite pair of forces between P3 and P4 on the same line of action.",
        r"Fig. 13.7. Two rigid bodies joined at $C$; $\mathbf F^{P_1}$, $\mathbf F^{P_2}$ are external and "
        r"$\mathbf f_{P_4}^{P_3}$, $\mathbf f_{P_3}^{P_4}$ are the equal and opposite forces the bodies exert on each other.")
def two_bodies():
    sc = Scene(820, 520, (100, 405), 100)
    _two_body_common(sc, False)
    b1 = _blob((2.35, 1.65), 1.2, 0.3, sy=0.8)
    b2 = _blob((4.85, 1.55), 1.2, 2.0, sy=0.8)
    triangle(sc, b1, "BLUE", 0.15)
    sc.poly(b1, "BLUE", 1.6, close=True)
    triangle(sc, b2, "ACC", 0.18)
    sc.poly(b2, "ACC", 1.6, close=True)
    C = (3.68, 1.3)
    G1, G2 = (2.25, 1.7), (5.0, 1.75)
    _frame3(sc, G1, [bold("x") + S("", "1"), bold("y") + S("", "1"), bold("z") + S("", "1")], "BLUE", 0.55,
            [(-14, 12), (12, 12), (-6, -8)])
    _frame3(sc, G2, [bold("x") + S("", "2"), bold("y") + S("", "2"), bold("z") + S("", "2")], ORANGE, 0.55,
            [(-14, 12), (14, 6), (-6, -8)])
    sc.dotp(G1, 3.6)
    sc.dotp(G2, 3.6)
    sc.label(G1, S("G", "1"), "BLUE", "middle", 16, dx=10, dy=20)
    sc.label(G2, S("G", "2"), ORANGE, "middle", 16, dx=-8, dy=22)
    sc.label((1.35, 0.95), S("B", "1"), "BLUE", "middle", 18)
    sc.label((5.95, 0.9), S("B", "2"), ORANGE, "middle", 18)
    # ball-and-socket joint at the common body point C
    sc.circle(C, 0.13, "HEAD", 1.8, fill="HEAD", opacity=0.35)
    sc.label(C, "C", "HEAD", "start", 17, dx=14, dy=26)
    sc.note((C[0] - 0.6, 0.15), "ball-and-socket joint", "TEXT", "start", 13)
    sc.line((C[0], C[1] - 0.14), (C[0], 0.3), "EDGE", 1.0)
    # external forces
    P1, P2 = (1.8, 2.3), (5.55, 0.85)
    sc.vec(P1, _add(P1, _d(60), 0.8), S(bold("F"), None, "P1"), "PINK", 3.0, name_off=(18, -4), size=17, head=11)
    sc.vec(P2, _add(P2, _d(-65), 0.8), S(bold("F"), None, "P2"), "PINK", 3.0, name_off=(22, 8), size=17, head=11)
    for p, nm, off in ((P1, "1", (-14, -6)), (P2, "2", (-16, 12))):
        sc.mass(p, None, r=4.5)
        sc.label(p, S("P", nm), "HEAD", "middle", 16, dx=off[0], dy=off[1])
    # internal pair on the line P3 P4
    P3, P4 = (2.6, 0.75), (4.4, 2.3)
    sc.dashed(P3, P4)
    n = math.hypot(P4[0] - P3[0], P4[1] - P3[1])
    u = ((P4[0] - P3[0]) / n, (P4[1] - P3[1]) / n)
    sc.vec(P3, _add(P3, u, 0.62), None, "PINK", 2.8, head=10)
    sc.vec(P4, _add(P4, u, -0.5), None, "PINK", 2.8, head=10)
    sc.label(_add(P3, u, 0.55), S(bold("f"), "P4", "P3"), "PINK", "start", 15, dx=18, dy=24)
    sc.label(_add(P4, u, -0.25), S(bold("f"), "P3", "P4"), "PINK", "start", 15, dx=10, dy=22)
    for p, nm, off in ((P3, "3", (-14, 8)), (P4, "4", (14, -10))):
        sc.mass(p, None, r=4.5)
        sc.label(p, S("P", nm), "HEAD", "middle", 16, dx=off[0], dy=off[1])
    return sc


@figure("t8-exploded",
        "Exploded view of the two-body system: each body drawn apart with the reaction components R1, R2, R3 at C on B1 and "
        "the equal and opposite components on B2, plus the external and the internal forces.",
        r"Exploded view (Fig. 13.8). The reaction at $C$ is $\mathbf R=R_1\mathbf i+R_2\mathbf j+R_3\mathbf k$ on $B_1$ and "
        r"$-\mathbf R$ on $B_2$ (third law of Newton).")
def exploded():
    sc = Scene(900, 480, (100, 385), 100)
    _two_body_common(sc, True)
    b1 = _blob((2.1, 1.7), 1.2, 0.3, sy=0.8)
    b2 = _blob((6.3, 1.6), 1.2, 2.0, sy=0.8)
    triangle(sc, b1, "BLUE", 0.15)
    sc.poly(b1, "BLUE", 1.6, close=True)
    triangle(sc, b2, "ACC", 0.18)
    sc.poly(b2, "ACC", 1.6, close=True)
    G1, G2 = (1.9, 1.75), (6.4, 1.85)
    _frame3(sc, G1, [bold("x") + S("", "1"), bold("y") + S("", "1"), bold("z") + S("", "1")], "BLUE", 0.5,
            [(-14, 12), (12, 14), (-6, -8)])
    _frame3(sc, G2, [bold("x") + S("", "2"), bold("y") + S("", "2"), bold("z") + S("", "2")], ORANGE, 0.5,
            [(-14, 12), (14, 6), (-6, -8)])
    sc.dotp(G1, 3.4)
    sc.dotp(G2, 3.4)
    sc.label(G1, S("G", "1"), "BLUE", "middle", 16, dx=-4, dy=24)
    sc.label(G2, S("G", "2"), ORANGE, "middle", 16, dx=-6, dy=26)
    sc.label((0.95, 0.8), S("B", "1"), "BLUE", "middle", 18)
    sc.label((7.4, 0.85), S("B", "2"), ORANGE, "middle", 18)
    # reactions at C(B1) (right edge of B1) and at C(B2) (left edge of B2): R on B1, -R on B2
    C1, C2 = (3.05, 1.4), (5.2, 1.4)
    sc.mass(C1, None, r=4.5)
    sc.mass(C2, None, r=4.5)
    sc.label(C1, "C(" + S("B", "1") + ")", "HEAD", "start", 15, dx=10, dy=30)
    sc.label(C2, "C(" + S("B", "2") + ")", "HEAD", "start", 15, dx=12, dy=30)
    ex = (-0.789 * 0.6, -0.614 * 0.6)
    for base, sg in ((C1, 1), (C2, -1)):
        sc.vec(base, _add(base, ex, 0.75 * sg), S(bold("R"), "1"), "PINK", 2.8,
               name_off=(-14, 14) if sg > 0 else (18, -2), size=16, head=10)
        sc.vec(base, _add(base, (1, 0), 0.6 * sg), S(bold("R"), "2"), "PINK", 2.8,
               name_off=(14, -10) if sg > 0 else (-14, -10), size=16, head=10)
        sc.vec(base, _add(base, (0, 1), 0.7 * sg), S(bold("R"), "3"), "PINK", 2.8,
               name_off=(-14, 0) if sg > 0 else (14, 10), size=16, head=10)
    # external forces and the internal pair
    P1, P2 = (1.5, 2.35), (5.95, 0.85)
    sc.vec(P1, _add(P1, _d(60), 0.8), S(bold("F"), None, "P1"), "PINK", 3.0, name_off=(18, -4), size=17, head=11)
    sc.vec(P2, _add(P2, _d(-65), 0.8), S(bold("F"), None, "P2"), "PINK", 3.0, name_off=(22, 8), size=17, head=11)
    P3, P4 = (2.4, 0.85), (5.75, 2.25)
    sc.vec(P3, _add(P3, _d(-20), 0.55), S(bold("f"), "P4", "P3"), "PINK", 2.8, name_off=(6, 24), size=15, head=10)
    sc.vec(P4, _add(P4, _d(160), 0.55), S(bold("f"), "P3", "P4"), "PINK", 2.8, name_off=(-6, -14), size=15, head=10)
    for p, nm, off in ((P1, "1", (-14, -4)), (P2, "2", (-16, 12)), (P3, "3", (-14, 6)), (P4, "4", (14, -4))):
        sc.mass(p, None, r=4.2)
        sc.label(p, S("P", nm), "HEAD", "middle", 16, dx=off[0], dy=off[1])
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t8-torque-free-frames",
        "A free rigid body with its centre of mass G, the inertial frame S0 and the body-fixed principal frame Sb with "
        "different orientations.",
        r"Torque-free motion, Fig. 15.1: the inertial frame $S_0$ (grey, labels $X,Y,Z$) and the body-fixed principal frame "
        r"$S_b$ (blue, labels $x,y,z$) with origin at the centre of mass $G$.")
def torque_free_frames():
    sc = Scene(620, 500, (310, 255), 130)
    G = (0.0, 0.0)
    pts = _blob((0.0, 0.0), 1.15, 0.9, sy=0.78)
    triangle(sc, pts, "ACC", 0.13)
    sc.poly(pts, "ACC", 1.5, close=True)
    # inertial frame S0 (grey): k0 up, i0 down-left, j0 right
    fixed_axis(sc, G, 218, 1.55, _ax("i", "0"), off=(-12, 14))
    fixed_axis(sc, G, 0, 1.75, _ax("j", "0"), off=(16, 6))
    fixed_axis(sc, G, 90, 1.7, _ax("k", "0"), off=(-14, 2))
    # body frame S_b (blue), tilted
    unit(sc, G, 262, 1.3, _ax("i", "b"), off=(-14, 14))
    unit(sc, G, 28, 1.45, _ax("j", "b"), off=(18, -6))
    unit(sc, G, 112, 1.35, _ax("k", "b"), off=(-14, -4))
    sc.dotp(G, 4.2)
    sc.label(G, "G", "HEAD", "start", 17, dx=12, dy=22)
    sc.note((-2.3, -1.75), "grey: S0, blue: Sb", "TEXT", "start", 13)
    return sc


@figure("t8-rot-psi",
        "Precession: the axes i0 and j0 rotated by psi counter-clockwise about k0, which points out of the paper, giving i1 and "
        "j1.",
        r"Precession $\psi$ about $\mathbf k_0=\mathbf k_1$ (out of the paper $\odot$): the shaded right triangles give "
        r"$\mathbf i_1$ and $\mathbf j_1$ in $\mathcal B_0$.")
def rot_psi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("i", "0"), _ax("j", "0")), (_ax("i", "1"), _ax("j", "1")), None,
                          S(bold("k"), "0") + " = " + S(bold("k"), "1"), ("ψ", "view along k0 (out of the paper)"))


@figure("t8-rot-theta",
        "Nutation: the axes j1 and k1 rotated by theta counter-clockwise about i1, which points out of the paper, giving j2 and "
        "k2.",
        r"Nutation $\theta$ about $\mathbf i_1=\mathbf i_2$ (out of the paper $\odot$): the shaded right triangles give "
        r"$\mathbf j_2$ and $\mathbf k_2=\mathbf k_b$ in $\mathcal B_1$.")
def rot_theta():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("j", "1"), _ax("k", "1")), (_ax("j", "2"), _ax("k", "2")), None,
                          S(bold("i"), "1") + " = " + S(bold("i"), "2"), ("θ", "view along i1 (out of the paper)"))


@figure("t8-rot-phi",
        "Spin: the axes i2 and j2 rotated by phi counter-clockwise about k2, which points out of the paper, giving ib and jb.",
        r"Spin $\varphi$ about $\mathbf k_2=\mathbf k_b$ (out of the paper $\odot$): the shaded right triangles give "
        r"$\mathbf i_b$ and $\mathbf j_b$ in $\mathcal B_2$.")
def rot_phi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("i", "2"), _ax("j", "2")), (_ax("i", "b"), _ax("j", "b")), None,
                          S(bold("k"), "2") + " = " + S(bold("k"), "b"), ("φ", "view along k2 (out of the paper)"))


# --------------------------------------------------------------------------------------------------------------------
# Torque-free motion: 3D sketches (axisymmetric cones, Poinsot construction and polhodes)
def _view(p):
    """Page position of a 3D point (x right, y receding to the upper right, z up)."""
    return (p[0] + 0.40 * p[1], p[2] + 0.22 * p[1])


_TOV = (0.40, -1.0, 0.22)                 # direction towards the viewer (kernel of the projection, reversed)
_TOVN = math.sqrt(sum(c * c for c in _TOV))


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _mv(R, v):
    return tuple(sum(R[i][j] * v[j] for j in range(3)) for i in range(3))


def _mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def _rot(axis, deg):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    if axis == "x":
        return [[1, 0, 0], [0, c, -s], [0, s, c]]
    if axis == "y":
        return [[c, 0, s], [0, 1, 0], [-s, 0, c]]
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


def _axis_angle(axis, ang):
    n = math.sqrt(_dot(axis, axis))
    a = tuple(x / n for x in axis)
    K = [[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]]
    return [[(1 if i == j else 0) + math.sin(ang) * K[i][j] + (1 - math.cos(ang)) * sum(K[i][m] * K[m][j] for m in range(3))
             for j in range(3)] for i in range(3)]


def _look_along(u_body, roll_deg):
    """Body-to-world matrix that turns the body direction u_body towards the viewer, rolled by roll_deg about the view line."""
    un = math.sqrt(_dot(u_body, u_body))
    u = tuple(x / un for x in u_body)
    d = tuple(x / _TOVN for x in _TOV)
    ax = (u[1] * d[2] - u[2] * d[1], u[2] * d[0] - u[0] * d[2], u[0] * d[1] - u[1] * d[0])
    an = math.sqrt(_dot(ax, ax))
    ang = math.acos(max(-1.0, min(1.0, _dot(u, d))))
    Ra = _axis_angle(ax, ang) if an > 1e-9 else [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return _mm(_axis_angle(d, math.radians(roll_deg)), Ra)


def _runs(sc, pts, vis, col, w, hidden_dash=None, hidden_col=None):
    """Draw a polyline split into visible (solid) and hidden (dashed or skipped) runs."""
    run, state = [], None
    for p, v in zip(pts, vis):
        if state is None or v == state:
            run.append(p)
            state = v
            continue
        run.append(p)
        _flush(sc, run, state, col, w, hidden_dash, hidden_col)
        run, state = [p], v
    _flush(sc, run, state, col, w, hidden_dash, hidden_col)


def _flush(sc, run, state, col, w, hidden_dash, hidden_col):
    if len(run) < 2:
        return
    if state:
        sc.poly(run, col, w)
    elif hidden_dash:
        sc.poly(run, hidden_col or col, max(w * 0.7, 1.0), hidden_dash)


def _ellipsoid_wire(sc, R, semi, k, col="EDGE", w=1.0, nmer=8, npar=5):
    """Wire frame of an ellipsoid with semi-axes `semi` (body axes), body-to-world matrix R and scale k; visible part only."""
    a, b, c = semi

    def pt(u, v):
        pb = (a * math.sin(u) * math.cos(v), b * math.sin(u) * math.sin(v), c * math.cos(u))
        nb = (pb[0] / a ** 2, pb[1] / b ** 2, pb[2] / c ** 2)
        return _mv(R, tuple(k * x for x in pb)), _mv(R, nb)

    curves = []
    for i in range(nmer):
        v = math.pi * i / nmer * 2
        curves.append([pt(math.pi * j / 60, v) for j in range(61)])
    for j in range(1, npar + 1):
        u = math.pi * j / (npar + 1)
        curves.append([pt(u, 2 * math.pi * i / 90) for i in range(91)])
    for cv in curves:
        pts = [_view(p) for p, n in cv]
        vis = [_dot(n, _TOV) > 0 for p, n in cv]
        _runs(sc, pts, vis, col, w)


def _euler_run(I, w0, R0, steps, dt):
    """Integrate Euler's equations (torque free) with the attitude matrix; return [(w_body, R)] samples."""
    A, B, C = I

    def f(w):
        return ((B - C) * w[1] * w[2] / A, (C - A) * w[2] * w[0] / B, (A - B) * w[0] * w[1] / C)

    def omega_x(R, w):
        # dR/dt = R [w]x
        W = [[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]]
        return _mm(R, W)

    def ortho(R):
        cols = [[R[i][j] for i in range(3)] for j in range(3)]
        e0 = cols[0]
        n = math.sqrt(_dot(e0, e0))
        e0 = [x / n for x in e0]
        d = _dot(cols[1], e0)
        e1 = [cols[1][i] - d * e0[i] for i in range(3)]
        n = math.sqrt(_dot(e1, e1))
        e1 = [x / n for x in e1]
        e2 = [e0[1] * e1[2] - e0[2] * e1[1], e0[2] * e1[0] - e0[0] * e1[2], e0[0] * e1[1] - e0[1] * e1[0]]
        return [[e0[i], e1[i], e2[i]] for i in range(3)]

    out = [(tuple(w0), R0)]
    w, R = tuple(w0), R0
    for _ in range(steps):
        def add(w, k, s):
            return tuple(w[i] + s * k[i] for i in range(3))
        k1 = f(w)
        k2 = f(add(w, k1, dt / 2))
        k3 = f(add(w, k2, dt / 2))
        k4 = f(add(w, k3, dt))
        wn = tuple(w[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(3))
        # attitude: RK4 on R with the angular velocity interpolated
        wm = tuple((w[i] + wn[i]) / 2 for i in range(3))
        r1 = omega_x(R, w)
        r2 = omega_x([[R[i][j] + dt / 2 * r1[i][j] for j in range(3)] for i in range(3)], wm)
        r3 = omega_x([[R[i][j] + dt / 2 * r2[i][j] for j in range(3)] for i in range(3)], wm)
        r4 = omega_x([[R[i][j] + dt * r3[i][j] for j in range(3)] for i in range(3)], wn)
        R = ortho([[R[i][j] + dt / 6 * (r1[i][j] + 2 * r2[i][j] + 2 * r3[i][j] + r4[i][j]) for j in range(3)] for i in range(3)])
        w = wn
        out.append((w, R))
    return out


def _arc3(c, r, a0, a1, n=60):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n)))
            for i in range(n + 1)]


def _cone(sc, axis, ang_deg, length, col, w, dash=None, fill=None, op=0.1):
    """Right circular cone with apex at the origin (xz plane axis, y = 0): base circle drawn as an ellipse in perspective."""
    d = math.radians(ang_deg)
    L = length
    cen = tuple(L * math.cos(d) * c for c in axis)
    r = L * math.sin(d)
    # orthonormal basis perpendicular to the axis (axis in the xz plane): e1 = y, e2 = axis x y
    e1 = (0.0, 1.0, 0.0)
    e2 = (axis[1] * e1[2] - axis[2] * e1[1], axis[2] * e1[0] - axis[0] * e1[2], axis[0] * e1[1] - axis[1] * e1[0])
    base = []
    for i in range(121):
        t = 2 * math.pi * i / 120
        base.append(tuple(cen[j] + r * (math.cos(t) * e1[j] + math.sin(t) * e2[j]) for j in range(3)))
    pg = [_view(p) for p in base]
    if fill:
        triangle(sc, pg, fill, op)
    sc.poly(pg, col, w, dash)
    # silhouette generators: extreme angles of the base points seen from the apex
    ap = _view((0, 0, 0))
    ax2 = math.atan2(_view(axis)[1], _view(axis)[0])
    best = {}
    for p in pg:
        a = math.atan2(p[1] - ap[1], p[0] - ap[0]) - ax2
        a = (a + math.pi) % (2 * math.pi) - math.pi
        if "lo" not in best or a < best["lo"][0]:
            best["lo"] = (a, p)
        if "hi" not in best or a > best["hi"][0]:
            best["hi"] = (a, p)
    for key in ("lo", "hi"):
        sc.line(ap, best[key][1], col, w, dash)
    return pg


@figure("t8-axisymmetric-cones",
        "Axisymmetric torque-free body: the angular momentum along k0, the symmetry axis kb tilted by theta, and the angular "
        "velocity in their plane as the sum of a precession about k0 and a spin about kb, on the space cone and the body cone.",
        r"Axisymmetric body, $\boldsymbol\omega_{b0}=(H_{G0}/A)\,\mathbf k_0+\lambda\,\mathbf k_b$: the angular velocity lies in "
        r"the plane of $\mathbf k_0$ and $\mathbf k_b$ and describes a cone about $\mathbf k_0$ (space cone) and a cone about "
        r"$\mathbf k_b$ (body cone) at the constant angles shown; prolate case, $\theta$ below a right angle.")
def axisymmetric_cones():
    sc = Scene(640, 520, (200, 450), 150)
    th = 40.0
    kb = (math.sin(math.radians(th)), 0.0, math.cos(math.radians(th)))
    k0 = (0.0, 0.0, 1.0)
    a, b = 1.0, 0.552                     # (H/A) and lambda in units of the drawing
    w = tuple(a * k0[i] + b * kb[i] for i in range(3))
    wl = math.sqrt(_dot(w, w))
    alpha = math.degrees(math.acos(w[2] / wl))
    beta = th - alpha
    G = (0.0, 0.0)
    # cones
    _cone(sc, kb, beta, wl, "BLUE", 1.4, None, "BLUE", 0.10)
    _cone(sc, k0, alpha, wl, "EDGE", 1.3, "6 4")
    # components of omega (thin dashed parallelogram)
    pa = _view(tuple(a * x for x in k0))
    pb = _view(tuple(b * x for x in kb))
    pw = _view(w)
    sc.line(pa, pw, "EDGE", 1.1, "5 4")
    sc.line(pb, pw, "EDGE", 1.1, "5 4")
    # axes
    sc.vec(G, _view(tuple(1.85 * x for x in k0)), None, "EDGE", 1.6, head=9)
    sc.label(_view(tuple(1.85 * x for x in k0)), S(bold("k"), "0") + " ∥ " + S(bold("H"), "G0"), "TEXT", "middle", 16,
             weight="700", dy=-10)
    sc.vec(G, _view(tuple(1.6 * x for x in kb)), S(bold("k"), "b"), "BLUE", 2.6, name_off=(18, -6), size=17, head=11)
    sc.vec(G, pa, None, DRED, 2.4, head=9)
    sc.vec(G, pb, None, DRED, 2.4, head=9)
    sc.label(_view(tuple(0.3 * a * x for x in k0)), "(" + S(bold("H"), "G0") + "/A) " + S(bold("k"), "0"), DRED, "end", 15,
             dx=-26, dy=4)
    sc.label(_view(tuple(0.5 * b * x for x in kb)), "λ " + S(bold("k"), "b"), DRED, "start", 15, dx=12, dy=14)
    sc.vec(G, pw, S(bold("ω"), "b0"), "GREEN", 3.4, name_off=(-4, -30), size=18, head=12)
    sc.dotp(G, 4.2)
    sc.label(G, "G", "HEAD", "end", 17, dx=-10, dy=18)
    # nutation angle between k0 and kb (in the xz plane)
    sc.arc(G, 0.6, 90 - th, 90, "GREEN", 1.7)
    sc.label(_add(G, _d(90 - th / 2), 0.78), "θ", "GREEN", "middle", 17, dx=6, dy=6)
    sc.label(_view(tuple(0.9 * wl * math.cos(math.radians(beta)) * x for x in kb)), "body cone", "BLUE", "start", 15, dx=40, dy=-2)
    sc.label(_view((-0.34, 0.0, 1.25)), "space cone", "TEXT", "end", 15, dx=-6, dy=-4)
    return sc


@figure("t8-poinsot",
        "Poinsot construction: the inertia ellipsoid fixed to the body is tangent at the tip of the angular velocity to a "
        "horizontal invariable plane normal to the angular momentum, with the polhode on the ellipsoid and the herpolhode on the plane.",
        r"Poinsot's construction: the energy ellipsoid rolls without slipping on the invariable plane $\omega_Z=2T_0/H_{G0}$; "
        r"the contact point is the tip of $\boldsymbol\omega_{b0}$, the normal of the plane is $\mathbf H_{G0}\parallel\mathbf k_0$, "
        r"the trace on the ellipsoid is the polhode and the trace on the plane the herpolhode.")
def poinsot():
    sc = Scene(680, 600, (330, 430), 185)
    I = (3.0, 2.0, 1.0)
    w0 = (0.70, 0.35, 0.90)
    s = 1.0 / math.sqrt(I[0] * w0[0] ** 2 + I[1] * w0[1] ** 2 + I[2] * w0[2] ** 2)
    w0 = tuple(s * x for x in w0)
    H = tuple(I[i] * w0[i] for i in range(3))
    Hn = math.sqrt(_dot(H, H))
    Hh = tuple(x / Hn for x in H)
    # rotation taking Hh to +z, then a turn about z for the look of the sketch
    ax = (Hh[1], -Hh[0], 0.0)                    # Hh x z
    an = math.sqrt(_dot(ax, ax))
    ang = math.acos(max(-1.0, min(1.0, Hh[2])))
    ax = tuple(x / an for x in ax)
    K = [[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]]
    Rr = [[(1 if i == j else 0) + math.sin(ang) * K[i][j] + (1 - math.cos(ang)) * sum(K[i][m] * K[m][j] for m in range(3))
           for j in range(3)] for i in range(3)]
    R0 = _mm(_rot("z", 200.0), Rr)
    semi = tuple(1.0 / math.sqrt(x) for x in I)
    kk = 1.0
    traj = _euler_run(I, w0, R0, 1500, 0.01)
    # closed polhode: first return to the start
    n_end = len(traj) - 1
    for i in range(200, len(traj)):
        d = math.dist(traj[i][0], w0)
        if d < 0.02:
            n_end = i
            break
    traj = traj[: n_end + 1]
    G = (0.0, 0.0)
    wz = _mv(R0, w0)
    h = wz[2]
    # invariable plane (tangent at the contact point)
    half = 0.95
    plane = [_view((-half, -half, h)), _view((half, -half, h)), _view((half, half, h)), _view((-half, half, h))]
    _ellipsoid_wire(sc, R0, semi, kk, "EDGE", 0.9, nmer=8, npar=5)
    triangle(sc, plane, "ACC", 0.14)
    sc.poly(plane, "ACC", 1.2, close=True)
    # polhode on the ellipsoid (blue, visible part solid) and herpolhode on the plane
    pol = [_mv(R0, w) for w, R in traj]
    nrm = [(w[0] / semi[0] ** 2, w[1] / semi[1] ** 2, w[2] / semi[2] ** 2) for w, R in traj]
    nrm = [_mv(R0, n) for n in nrm]
    _runs(sc, [_view(p) for p in pol], [_dot(n, _TOV) > 0 for n in nrm], "BLUE", 2.4, "3 3")
    her = [_view((_mv(R, w)[0], _mv(R, w)[1], h)) for w, R in traj]
    sc.poly(her, ORANGE, 2.2)
    # angular momentum (normal of the plane) and angular velocity to the contact point
    P = _mv(R0, w0)
    sc.vec(G, _view((0.0, 0.0, h + 0.55)), None, DRED, 2.6, head=11)
    sc.label(_view((0.0, 0.0, h + 0.55)), S(bold("H"), "G0") + " ∥ " + S(bold("k"), "0"), DRED, "start", 16, weight="700", dx=10, dy=-4)
    sc.vec(G, _view(P), None, "GREEN", 3.2, head=11)
    sc.label(_view(P), S(bold("ω"), "b0"), "GREEN", "start", 17, dx=14, dy=-10)
    sc.dotp(_view(P), 4.5, "GREEN")
    sc.dotp(G, 4.2)
    sc.label(G, "G", "HEAD", "end", 17, dx=-10, dy=18)
    sc.note(plane[1], "invariable plane", "TEXT", "start", 13, dx=8, dy=4)
    far = min(her, key=lambda p: p[0])
    sc.label(far, "herpolhode", ORANGE, "end", 15, dx=-12, dy=-6)
    vis = [i for i, n in enumerate(nrm) if _dot(n, _TOV) > 0]
    q = _view(pol[vis[0]]) if vis else _view(pol[0])
    lp = (q[0] - 0.55, q[1] - 0.32)
    sc.line(q, lp, "BLUE", 1.0)
    sc.label(lp, "polhode", "BLUE", "end", 15, dx=-4, dy=5)
    return sc


def _polhode_curves():
    """Closed polhodes of a rigid body with moments (3, 2, 1) at 2T = 1, as lists of body-frame points."""
    A, B, C = 3.0, 2.0, 1.0
    out = []

    def run(w0):
        def f(w):
            return ((B - C) * w[1] * w[2] / A, (C - A) * w[2] * w[0] / B, (A - B) * w[0] * w[1] / C)

        pts = [tuple(w0)]
        w = tuple(w0)
        dt = 0.01
        for i in range(3000):
            def add(w, k, s):
                return tuple(w[j] + s * k[j] for j in range(3))
            k1 = f(w)
            k2 = f(add(w, k1, dt / 2))
            k3 = f(add(w, k2, dt / 2))
            k4 = f(add(w, k3, dt))
            w = tuple(w[j] + dt / 6 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) for j in range(3))
            pts.append(w)
            if i > 150 and math.dist(w, w0) < 0.01:
                break
        return pts

    for h2, col in ((2.45, "x"), (2.75, "x"), (1.2, "z"), (1.5, "z")):
        wx = math.sqrt((h2 - C) / (A * (A - C)))
        wz = math.sqrt((A - h2) / (C * (A - C)))
        out.append((col, run((wx, 0.0, wz))))
    # separatrices: the two ellipses wx = +-k wz through the intermediate axis
    k = math.sqrt(C * (B - C) / (A * (A - B)))
    for sg in (1, -1):
        pts = []
        for i in range(181):
            t = 2 * math.pi * i / 180
            sz = math.cos(t) / math.sqrt(A * k * k + C)
            wy = math.sin(t) / math.sqrt(B)
            pts.append((sg * k * sz, wy, sz))
        out.append(("sep", pts))
    return out


@figure("t8-polhodes",
        "The inertia ellipsoid with the polhodes: closed curves around the major and minor axes and the two separatrix "
        "ellipses through the intermediate axis.",
        r"Polhodes on the inertia ellipsoid (intersection with the angular momentum ellipsoids): closed curves about the "
        r"major axis $\mathbf i_b$ (blue) and the minor axis $\mathbf k_b$ (orange), and the separatrices (green) through "
        r"the intermediate axis $\mathbf j_b$, where the rotation is unstable.")
def polhodes():
    sc = Scene(660, 540, (330, 280), 190)
    A, B, C = 3.0, 2.0, 1.0
    semi = tuple(1.0 / math.sqrt(x) for x in (A, B, C))
    best = None
    for roll in range(0, 360, 5):
        Rc = _look_along((1.0, 0.85, 1.25), roll)
        zx, zy = _view(_mv(Rc, (0.0, 0.0, 1.0)))
        xx, xy = _view(_mv(Rc, (1.0, 0.0, 0.0)))
        score = abs(math.degrees(math.atan2(zy, zx)) - 95.0) + abs(math.degrees(math.atan2(xy, xx)) + 20.0)
        if best is None or score < best[0]:
            best = (score, Rc)
    R = best[1]
    _ellipsoid_wire(sc, R, semi, 1.0, "EDGE", 0.9, nmer=10, npar=5)
    cols = {"x": "BLUE", "z": ORANGE, "sep": "GREEN"}
    for kind, pts in _polhode_curves():
        P3 = [_mv(R, p) for p in pts]
        nrm = [_mv(R, (p[0] / semi[0] ** 2, p[1] / semi[1] ** 2, p[2] / semi[2] ** 2)) for p in pts]
        _runs(sc, [_view(p) for p in P3], [_dot(n, _TOV) > 0 for n in nrm], cols[kind], 2.4 if kind != "sep" else 2.8)
    # principal axes through the ellipsoid
    for idx, nm, off in ((0, S(bold("i"), "b"), (12, 6)), (1, S(bold("j"), "b"), (24, 4)), (2, S(bold("k"), "b"), (0, -12))):
        v = [0.0, 0.0, 0.0]
        v[idx] = semi[idx] * 1.3
        p = _mv(R, tuple(v))
        sc.vec((0, 0), _view(p), None, "HEAD", 1.6, head=8)
        sc.label(_view(p), nm, "HEAD", "middle", 17, weight="700", dx=off[0], dy=off[1])
    sc.dotp((0, 0), 4)
    return sc
