"""Theory figures of Topic 6 (Kinematics of Rigid Bodies and Inertia Properties)."""
import math

from figures.em_theory import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

ORANGE = "ACC"
DRED = "#be123c"


def _d(deg):
    return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def _add(p, q, k=1.0):
    return (p[0] + k * q[0], p[1] + k * q[1])


def _blob(c, r, phase=0.0, n=72, sy=0.82):
    pts = []
    for i in range(n):
        f = 2 * math.pi * i / n
        rr = r * (1 + 0.12 * math.sin(3 * f + phase) + 0.07 * math.cos(2 * f) + 0.04 * math.sin(5 * f))
        pts.append((c[0] + rr * math.cos(f), c[1] + sy * rr * math.sin(f)))
    return pts


def _body(sc, c, r, phase=0.0, sy=0.82):
    pts = _blob(c, r, phase, sy=sy)
    triangle(sc, pts, "BLUE", 0.16)
    sc.poly(pts, "BLUE", 1.6, close=True)


# 3D sketch convention of the portal: x_0 down-left, y_0 to the right, z_0 up (cabinet projection, x foreshortened)
EX = (-0.789 * 0.6, -0.614 * 0.6)


def _p3(x, y, z):
    return (x * EX[0] + y, x * EX[1] + z)


def _p3v(v):
    return _p3(*v)


def _sub(sym, a, b=None):
    return S(bold(sym), a, b)


# --------------------------------------------------------------------------------------------------------------------
@figure("t6-body-frame",
        "A rigid body with three body points P, Q and R, the fixed frame at O and the body-fixed orthonormal basis built "
        "at P from the vectors PQ and PR.",
        r"Body-fixed frame $S_B$ built from the non-collinear body points $P$, $Q$, $R$: $\mathbf i_B$ along $\mathbf{PQ}$, "
        r"$\mathbf k_B$ normal to the plane $PQR$ and $\mathbf j_B = \mathbf k_B\times\mathbf i_B$, with the fixed frame $S_0$ at $O$.")
def body_frame():
    sc = Scene(670, 520, (140, 405), 135)
    O = (0.0, 0.0)
    P = (2.0, 0.95)
    dq, dr = 300.0, 55.0
    Q = _add(P, _d(dq), 1.05)
    R = _add(P, _d(dr), 0.85)
    _body(sc, (2.4, 0.95), 1.15, 0.6, sy=0.9)
    # fixed frame S_0 (grey)
    fixed_axis(sc, O, 218, 0.9, bold("x") + S("", "0"), off=(-14, 14))
    fixed_axis(sc, O, 0, 1.2, bold("y") + S("", "0"), off=(14, 8))
    fixed_axis(sc, O, 90, 1.7, bold("z") + S("", "0"), off=(-16, 4))
    sc.vec(O, P, None, "HEAD", 1.9, head=9)
    sc.label((0.9, 0.52), S(bold("r"), "0", "P"), "HEAD", "middle", 16, dx=10, dy=22)
    sc.dotp(O, 4)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=18)
    # the two body vectors PQ and PR (orange, construction)
    sc.vec(P, Q, None, ORANGE, 1.8, head=9)
    sc.vec(P, R, None, ORANGE, 1.8, head=9)
    sc.label(_add(P, _d(dq), 0.62), S(bold("PQ")), ORANGE, "start", 16, dx=10, dy=6)
    sc.label(_add(P, _d(dr), 0.55), S(bold("PR")), ORANGE, "start", 16, dx=10, dy=2)
    # body basis at P (blue): i_B along PQ, k_B normal to the plane PQR, j_B = k_B x i_B
    unit(sc, P, dq, 0.72, bold("i") + S("", "B"), off=(-16, 8))
    unit(sc, P, 12, 0.95, bold("j") + S("", "B"), off=(16, 6))
    unit(sc, P, 118, 0.85, bold("k") + S("", "B"), off=(-12, -4))
    for pt, nm, off in ((P, "P", (-14, 20)), (Q, "Q", (12, 8)), (R, "R", (-12, -8))):
        sc.mass(pt, None, r=5, col="BLUE")
        sc.label(pt, nm, "BLUE", "middle", 17, dx=off[0], dy=off[1])
    sc.note((3.35, 1.6), "body B", "TEXT", "start", 14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t6-projection-property",
        "Two body points A and P of a rigid body with their velocities; the projections of both velocities on the line AP "
        "are equal.",
        r"Equal projections: $\mathbf v_0^A\cdot\mathbf{PA}=\mathbf v_0^P\cdot\mathbf{PA}$. The perpendicular parts of the "
        r"velocities differ, the parts along the line $AP$ coincide ($p$), so the distance $AP$ stays constant.")
def projection_property():
    sc = Scene(720, 430, (150, 330), 130)
    ang = 38.0
    u = _d(ang)
    n = _d(ang + 90)
    A = (0.0, 0.0)
    P = _add(A, u, 2.0)
    _body(sc, _add(A, u, 1.0), 1.55, 0.2, sy=0.72)
    # the line AP, extended on both sides (dashed)
    sc.line(_add(A, u, -0.75), _add(A, u, 3.45), "EDGE", 1.2, "6 4")
    s = 1.0
    vA = _add(_add(A, u, s), n, 0.85)
    vP = _add(_add(P, u, s), n, -0.55)
    # perpendicular dashed lines from the tips onto the line AP
    fA, fP = _add(A, u, s), _add(P, u, s)
    sc.dashed(vA, fA)
    sc.dashed(vP, fP)
    right_angle(sc, fA, ang + 180, ang + 90, 0.07)
    right_angle(sc, fP, ang + 180, ang - 90, 0.07)
    # equal projections on the line (green)
    sc.vec(A, fA, None, "GREEN", 3.4, head=10)
    sc.vec(P, fP, None, "GREEN", 3.4, head=10)
    sc.label(_add(A, u, s / 2), "p", "GREEN", "middle", 17, dx=18, dy=22)
    sc.label(_add(P, u, s / 2), "p", "GREEN", "middle", 17, dx=-16, dy=-10)
    sc.vec(A, vA, S(bold("v"), "0", "A"), "BLUE", 2.6, name_off=(-24, -6), size=17, head=11)
    sc.vec(P, vP, S(bold("v"), "0", "P"), "BLUE", 2.6, name_off=(30, 6), size=17, head=11)
    sc.mass(A, None, r=5.5, col="BLUE")
    sc.mass(P, None, r=5.5, col="BLUE")
    sc.label(A, "A", "HEAD", "middle", 17, dx=16, dy=16)
    sc.label(P, "P", "HEAD", "middle", 17, dx=-16, dy=-10)
    sc.note(_add(A, u, 3.45), "line AP", "TEXT", "start", 13, dx=6, dy=-4)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t6-iar-foot",
        "The instantaneous axis of rotation parallel to the angular velocity, the point A, the foot I of the perpendicular "
        "from A to the axis and another point I' of the axis.",
        r"The point $I$ is the foot of the perpendicular from $A$ to the instantaneous axis (IAR), so $\mathbf{AI}\perp"
        r"\boldsymbol\omega_{B0}$; another point $I'$ of the axis makes $\mathbf{AI'}$ longer and the second term of "
        r"Eq. 9.9 does not vanish.")
def iar_foot():
    sc = Scene(560, 450, (90, 390), 140)
    dd = _d(125)
    nn = _d(215)
    I = (1.6, 1.0)
    A = _add(I, nn, 1.75)
    I2 = _add(I, dd, 1.15)
    # translucent triangle A-I-I'
    triangle(sc, [A, I, I2], "ACC", 0.16)
    # the axis (dashed) and omega parallel to it, drawn beside it
    sc.line(_add(I, dd, -1.1), _add(I, dd, 2.0), "EDGE", 1.3, "7 5")
    sc.note(_add(I, dd, 2.0), "IAR", "TEXT", "start", 14, dx=8, dy=-6)
    w0 = _add(_add(I, nn, 0.75), dd, 1.45)
    sc.vec(_add(w0, dd, -0.75), w0, S(bold("ω"), "B0"), "GREEN", 3.2, name_off=(-26, -2), size=17, head=11)
    # AI' (grey) and AI (bold blue)
    sc.vec(A, I2, None, "EDGE", 1.8, head=8)
    sc.vec(A, I, None, "BLUE", 3.0, head=11)
    right_angle(sc, I, 215, 125, 0.11, "HEAD")
    sc.label(_add(A, I2, 0.5), S(bold("AI'")), "TEXT", "start", 16, dx=10, dy=4)
    sc.label(_add(A, I, 0.5), S(bold("AI")), "BLUE", "start", 16, dx=10, dy=14)
    sc.mass(A, None, r=5, col="BLUE")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-4, dy=22)
    sc.dotp(I, 4.5)
    sc.label(I, "I", "HEAD", "start", 17, dx=10, dy=10)
    sc.dotp(I2, 4)
    sc.label(I2, "I'", "TEXT", "start", 16, dx=10, dy=-2)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t6-screw-field",
        "Screw motion velocity field: left, the perpendicular velocities in a plane normal to the angular velocity form "
        "concentric circles about the axis; right, a 3D sketch where every point also has the same slip velocity along the axis.",
        r"Screw (helical) motion, Fig. 9.4. Left: in a plane normal to $\boldsymbol\omega_{B0}$ (out of the paper) the "
        r"perpendicular velocities $\mathbf v_{0\perp}=\boldsymbol\omega_{B0}\times\mathbf{IA}$ are tangent to circles about "
        r"the axis and grow with $d$. Right: on top of them all points share the slip velocity $\mathbf v_{0\parallel}$.")
def screw_field():
    sc = Scene(820, 470, (215, 240), 120)
    I = (0.0, 0.0)
    for r in (0.45, 0.95, 1.45):
        sc.circle(I, r, "EDGE", 1.1, "4 4")
    # three points with tangent velocities proportional to the distance (counter-clockwise, omega out of the paper)
    pts = [(0.95, 25), (0.45, 150), (1.45, 250)]
    kv = 0.42
    for r, a in pts:
        p = _add(I, _d(a), r)
        t = _d(a + 90)
        sc.vec(p, _add(p, t, kv * r + 0.12), None, "BLUE", 2.6, head=10)
        sc.mass(p, None, r=4.5, col="BLUE")
    A = _add(I, _d(25), 0.95)
    sc.line(I, A, "EDGE", 1.3, "5 4")
    sc.label(_add(I, _d(25), 0.55), S("d", "A"), "TEXT", "middle", 16, dx=4, dy=18)
    sc.label(_add(A, _d(25), 0.0), "A", "HEAD", "middle", 17, dx=18, dy=16)
    tipA = _add(A, _d(115), kv * 0.95 + 0.12)
    sc.label(tipA, S(bold("v"), "0⊥", "A"), "BLUE", "start", 16, dx=10, dy=-2)
    sc.dotp(I, 4.5)
    sc.label(I, "I", "HEAD", "middle", 17, dx=14, dy=22)
    axis_out(sc, (-1.45, 1.55), S(bold("ω"), "B0"), "GREEN", off=(30, 5))
    sc.note((-1.0, -1.88), "view along the axis", "TEXT", "start", 13)
    # ---- right: 3D sketch
    C = (3.7, 0.15)
    rx, ry = 1.15, 0.40
    ell = [(C[0] + rx * math.cos(2 * math.pi * i / 90), C[1] + ry * math.sin(2 * math.pi * i / 90)) for i in range(90)]
    triangle(sc, ell, "BLUE", 0.10)
    sc.poly(ell, "BLUE", 1.3, close=True)
    sc.line(_add(C, (0, 1), -0.95), _add(C, (0, 1), 1.5), "EDGE", 1.3, "6 4")
    sc.vec(_add(C, (0, 1), 0.85), _add(C, (0, 1), 1.5), None, "GREEN", 3.0, head=11)
    sc.label(_add(C, (0, 1), 1.4), S(bold("ω"), "B0"), "GREEN", "start", 17, weight="700", dx=10, dy=0)
    sc.note(_add(C, (0, 1), 1.5), "IAR", "TEXT", "end", 14, dx=-8, dy=4)
    for a in (235, 330, 120):
        ar = math.radians(a)
        p = (C[0] + rx * math.cos(ar), C[1] + ry * math.sin(ar))
        t = (-rx * math.sin(ar), ry * math.cos(ar))
        tn = math.hypot(*t)
        t = (t[0] / tn, t[1] / tn)
        sc.vec(p, _add(p, t, 0.55), None, "BLUE", 2.4, head=10)
        sc.vec(p, _add(p, (0, 1), 0.75), None, ORANGE, 2.4, head=10)
        sc.mass(p, None, r=4, col="BLUE")
    ar = math.radians(235)
    p0 = (C[0] + rx * math.cos(ar), C[1] + ry * math.sin(ar))
    p1 = (C[0] + rx * math.cos(math.radians(330)), C[1] + ry * math.sin(math.radians(330)))
    sc.label(_add(p1, (0, 1), 0.75), S(bold("v"), "0∥"), ORANGE, "start", 16, dx=10, dy=2)
    t0 = (-rx * math.sin(ar), ry * math.cos(ar))
    n0 = math.hypot(*t0)
    sc.label(p0, S(bold("v"), "0⊥"), "BLUE", "middle", 16, dx=-6, dy=28)
    sc.dotp(C, 4)
    sc.label(C, "I", "HEAD", "middle", 17, dx=-14, dy=18)
    sc.note((3.5, -1.88), "3D view", "TEXT", "start", 13)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t6-airplane-example",
        "Oblique sketch of the airplane example: the centre of mass G, the wing point A and the tail point C with their "
        "velocities, the angular velocity and the instantaneous axis of rotation and slip.",
        r"Rigid airplane of Lecture 7 (sketch, not to scale): velocities of $G$, $A$, $C$, the angular velocity "
        r"$\boldsymbol\omega_{B0}=\mathbf i+\mathbf j+\mathbf k$ and the instantaneous axis of rotation and slip through "
        r"$I$, where the velocity is the slip velocity $\mathbf v_{0\parallel}=2\mathbf i+2\mathbf j+2\mathbf k$.")
def airplane_example():
    sc = Scene(680, 520, (290, 400), 95)
    G = (0.0, 0.0)
    A = _p3(-1, 2, 0)
    C = _p3(-4, 0, 1)
    I = _p3(-2 / 3, 4 / 3, -2 / 3)
    kv = 0.32
    # fixed axes (grey) at G
    fixed_axis(sc, G, 218, 0.72, bold("i"), off=(-12, 12))
    fixed_axis(sc, G, 0, 1.0, bold("j"), off=(12, 8))
    fixed_axis(sc, G, 90, 1.0, bold("k"), off=(-12, 6))
    # body outline: fuselage G-C, wing through A, small tail fin
    nose, tail = _p3(1.0, 0, 0), _p3(-4.4, 0, 0)
    sc.poly([nose, tail], "HEAD", 3.0)
    wing = [_p3(-0.4, 2.3, 0), _p3(-1.8, 2.3, 0), _p3(-2.4, 0, 0), _p3(-1.8, -2.3, 0), _p3(-0.4, -2.3, 0), _p3(-0.9, 0, 0)]
    triangle(sc, wing, "BLUE", 0.13)
    sc.poly(wing + [wing[0]], "BLUE", 1.5)
    fin = [_p3(-3.2, 0, 0), _p3(-4.4, 0, 0), _p3(-4.4, 0, 1.5), _p3(-4.0, 0, 1.5)]
    triangle(sc, fin, "BLUE", 0.2)
    sc.poly(fin + [fin[0]], "BLUE", 1.5)
    # axis (dashed) and the velocity of its points: the slip velocity
    d = _p3(1, 1, 1)
    sc.line(_add(I, d, -1.3), _add(I, d, 2.55), "EDGE", 1.4, "7 5")
    sc.vec(_add(I, d, -1.15), _add(I, d, -0.4), S(bold("ω"), "B0"), "GREEN", 3.2, name_off=(-30, 16), size=17, head=11)
    sc.vec(I, _add(I, d, 0.55 * 2 * 0.6), None, ORANGE, 2.8, head=11)
    sc.label(_add(I, d, 0.66), S(bold("v"), "0∥"), ORANGE, "start", 16, dx=10, dy=22)
    sc.note(_add(I, d, 2.55), "IAR", "TEXT", "start", 14, dx=8, dy=-2)
    sc.dashed(G, I)
    # velocities (blue)
    vG, vA, vC = _p3v((4, 2, 0)), _p3v((2, 1, 3)), _p3v((5, -3, 4))
    sc.vec(G, _add(G, vG, kv), S(bold("v"), "0", "G"), "BLUE", 2.6, name_off=(34, 6), size=16, head=10)
    sc.vec(A, _add(A, vA, kv), S(bold("v"), "0", "A"), "BLUE", 2.6, name_off=(26, -2), size=16, head=10)
    sc.vec(C, _add(C, vC, kv), S(bold("v"), "0", "C"), "BLUE", 2.6, name_off=(-6, -12), size=16, head=10)
    for pt, nm, off in ((G, "G", (-16, -12)), (A, "A", (14, 14)), (C, "C", (-8, 20))):
        sc.mass(pt, None, r=5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp(I, 4.5)
    sc.label(I, "I", "HEAD", "middle", 17, dx=16, dy=22)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _rotation_view(w, h, o, k, ang, fixed, moving, out, out_name, hdr, labels=None):
    """Generic single-rotation figure.

    ang: rotation angle in degrees (counter-clockwise in the view, axis towards the reader).
    fixed: names of the two old axes (right, up); moving: names of the two new axes; out: name of the axis along the
    paper normal (drawn with the symbol at the origin). `hdr` is the note under the figure.
    """
    sc = Scene(w, h, o, k)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    L, Lf = 1.0, 1.62
    fixed_axis(sc, O, 0, Lf, fixed[0], off=(16, 6))
    fixed_axis(sc, O, 90, Lf, fixed[1], off=(16, 4))
    # triangle of the first new axis (adjacent leg along the old right axis, opposite along the old up axis)
    t1 = _d(ang)
    foot1 = (L * c, 0.0)
    tip1 = (L * c, L * s)
    triangle(sc, [O, foot1, tip1], "ACC", 0.20)
    sc.dashed(foot1, tip1)
    right_angle(sc, foot1, 180, 90, 0.07)
    # triangle of the second new axis (adjacent along the old up axis, opposite along minus the old right axis)
    t2 = _d(ang + 90)
    foot2 = (0.0, L * c)
    tip2 = (-L * s, L * c)
    triangle(sc, [O, foot2, tip2], "ACC", 0.20)
    sc.dashed(foot2, tip2)
    right_angle(sc, foot2, 270, 180, 0.07)
    unit(sc, O, ang, L, moving[0], off=(18, -10))
    unit(sc, O, ang + 90, L, moving[1], off=(-6, -14))
    # leg labels
    sc.label((L * c / 2, 0), "cos " + hdr[0], "TEXT", "middle", 15, dx=0, dy=24)
    sc.label((L * c, L * s / 2), "sin " + hdr[0], "TEXT", "start", 15, dx=9, dy=5)
    sc.label((-L * s / 2, L * c), "sin " + hdr[0], "TEXT", "middle", 15, dy=-8)
    sc.label((0, L * c / 2), "cos " + hdr[0], "TEXT", "start", 15, dx=9, dy=18)
    # angle between both pairs of axes, with the sense (counter-clockwise)
    sc.arc(O, 0.50, 0, ang, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d(ang / 2), 0.50), hdr[0], "GREEN", "middle", 17, dx=-4, dy=18)
    sc.arc(O, 0.50, 90, 90 + ang, "GREEN", 1.7, head=True)
    sc.label(_add(O, _d(90 + ang / 2), 0.50), hdr[0], "GREEN", "middle", 17, dx=14, dy=22)
    # the axis along the paper normal
    axis_out(sc, O, None, "HEAD")
    sc.label(O, out_name, "HEAD", "end", 16, weight="700", dx=-16, dy=26)
    sc.note((-0.75, -0.42), hdr[1], "TEXT", "start", 13)
    return sc


def _ax(sym, sub):
    return bold(sym) + S("", sub)


_PSI, _THETA, _PHI = "ψ", "θ", "φ"


@figure("t6-euler-313-psi",
        "Precession: the axes i0 and j0 rotated by psi counter-clockwise about k0, which points out of the paper, "
        "giving i1 and j1.",
        r"Precession $\psi$ about $\mathbf k_0=\mathbf k_1$ (out of the paper $\odot$): $\mathbf i_1$ and $\mathbf j_1$ "
        r"in $\mathcal B_0$ from the shaded right triangles (hypotenuse $1$).")
def euler313_psi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("i", "0"), _ax("j", "0")), (_ax("i", "1"), _ax("j", "1")),
                          None, S(bold("k"), "0") + " = " + S(bold("k"), "1"), (_PSI, "view along k0 (out of the paper)"))


@figure("t6-euler-313-theta",
        "Nutation: the axes j1 and k1 rotated by theta counter-clockwise about i1, which points out of the paper, "
        "giving j2 and k2.",
        r"Nutation $\theta$ about $\mathbf i_1=\mathbf i_2$ (out of the paper $\odot$, line of nodes): $\mathbf j_2$ and "
        r"$\mathbf k_2$ in $\mathcal B_1$ from the shaded right triangles.")
def euler313_theta():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("j", "1"), _ax("k", "1")), (_ax("j", "2"), _ax("k", "2")),
                          None, S(bold("i"), "1") + " = " + S(bold("i"), "2"), (_THETA, "view along i1 (out of the paper)"))


@figure("t6-euler-313-phi",
        "Spin: the axes i2 and j2 rotated by phi counter-clockwise about k2, which points out of the paper, giving iB and jB.",
        r"Spin $\varphi$ about $\mathbf k_2=\mathbf k_B$ (out of the paper $\odot$): $\mathbf i_B$ and $\mathbf j_B$ in "
        r"$\mathcal B_2$ from the shaded right triangles.")
def euler313_phi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("i", "2"), _ax("j", "2")), (_ax("i", "B"), _ax("j", "B")),
                          None, S(bold("k"), "2") + " = " + S(bold("k"), "B"), (_PHI, "view along k2 (out of the paper)"))


@figure("t6-euler-321-theta",
        "Pitch: the axes k1 and i1 rotated by theta counter-clockwise about j1, which points out of the paper, giving k2 "
        "and i2.",
        r"Pitch $\theta$ about $\mathbf j_1=\mathbf j_2$ (out of the paper $\odot$): $\mathbf k_1$ to the right, $\mathbf i_1$ "
        r"up, since $\mathbf k_1\times\mathbf i_1=\mathbf j_1$; the shaded triangles give $\mathbf k_2$ and $\mathbf i_2$.")
def euler321_theta():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("k", "1"), _ax("i", "1")), (_ax("k", "2"), _ax("i", "2")),
                          None, S(bold("j"), "1") + " = " + S(bold("j"), "2"), (_THETA, "view along j1 (out of the paper)"))


@figure("t6-euler-321-phi",
        "Roll: the axes j2 and k2 rotated by phi counter-clockwise about i2, which points out of the paper, giving jB and kB.",
        r"Roll $\varphi$ about $\mathbf i_2=\mathbf i_B$ (out of the paper $\odot$): $\mathbf j_B$ and $\mathbf k_B$ in "
        r"$\mathcal B_2$ from the shaded triangles (same as the nutation).")
def euler321_phi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("j", "2"), _ax("k", "2")), (_ax("j", "B"), _ax("k", "B")),
                          None, S(bold("i"), "2") + " = " + S(bold("i"), "B"), (_PHI, "view along i2 (out of the paper)"))
