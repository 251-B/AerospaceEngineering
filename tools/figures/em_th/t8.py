"""Theory figures of Topic 8 (Constraints, Rolling Motion, Multibody Systems and Torque-Free Motion)."""
import math

from figures.em_theory import axis_in, axis_out, figure, fixed_axis, raster, right_angle, triangle
from figures.em_th.t6 import _add, _ax, _d, _rotation_view
from figures.mech import S, Scene, bold

TD = "θ̇"
ORANGE = "ACC"
DRED = "#be123c"


def _sub(sym, a=None, b=None):
    return S(bold(sym), a, b)


# oblique frame of the portal (x down-left, y right, z up), x foreshortened
_EX = (-0.789 * 0.6, -0.614 * 0.6)


# --------------------------------------------------------------------------------------------------------------------
raster("t8-joints",
       "Left, a ball-and-socket joint between two bodies B1 and B2 at the point C; right, a pin connection with the pin axis Cz.",
       r"Ball-and-socket joint (left): $C$ is a point of both bodies, no orientation is constrained. Pin connection (right): the axis $Cz$ belongs to both bodies and only the rotation about it is free. Copied from Notes.pdf, Fig. 13.1, p. 103", 700)


# --------------------------------------------------------------------------------------------------------------------
raster("t8-collars",
       "A collar on a cylindrical bar that slides along and rotates about z1, and a collar on a prismatic bar that only slides, with the axes z1 = z2, x1 and x2.",
       r"Left: collar on a cylindrical bar, free to slide along and to turn about $z_1\equiv z_2$ by an angle $\phi$ between $x_1$ and $x_2$. Right: collar on a prismatic bar, free only to slide ($x_1\equiv x_2$). Copied from Notes.pdf, Fig. 13.2, p. 103", 640)


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
raster("t8-rolling-contact",
       "Two smooth bodies B1 and B2 in contact at a single point C with the contact axes x, y and z and the arc lengths s1 and s2 swept on both perimeters.",
       r"Rolling contact. Two bodies in contact at the single point $C$, with the contact axes $x$ (out of the paper $\odot$), $y$ and $z$; rolling without slipping makes the arcs $s_1-s_1(0)$ and $s_2-s_2(0)$ equal. Copied from Notes.pdf, Fig. 13.3, p. 104", 680)


# --------------------------------------------------------------------------------------------------------------------
def _floor(sc, x0, x1, y):
    sc.ground((x0, y), (x1, y), side=-1, step=9, length=10)


# --------------------------------------------------------------------------------------------------------------------
raster("t8-disk-rolling",
       "A disk B of radius R rolling without slipping on a horizontal floor F, with the fixed frame at O, the frame S_G at the centre G, the clockwise angle theta and the equal arcs R theta on the disk and on the floor.",
       r"Disk rolling without slip. $S_0$ is fixed to the floor; the disk turns clockwise by $\theta$, so $\boldsymbol\omega_{B0}$ points into the paper $\otimes$, and the arc $R\theta$ on the floor equals the arc on the disk. Copied from Notes.pdf, Fig. 13.4, p. 105", 680)


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
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
raster("t8-wobbling-disk",
       "A disk of radius R rolling and wobbling three-dimensionally on a floor, with the contact point C, the vertical axis k and the curved trace of C on the floor.",
       r"A disk $B$ rolling without slip and wobbling on the floor $F$: the trace of the contact point $C$ is a two-dimensional curve, so two coordinates are needed to place $C$ in the plane. Copied from Notes.pdf, Fig. 13.5, p. 105", 420)


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
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
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
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
# --------------------------------------------------------------------------------------------------------------------
raster("t8-table-legs",
       "A table with three legs (determinate reactions) and a table with four legs (indeterminate, hyperstatic reactions), with the reaction at each foot.",
       r"Determinate (left, $n=3$) and undetermined (right, $n>3$) system of reactions on a rigid table: equilibrium gives only three scalar equations for the reactions at the feet. Copied from Notes.pdf, Fig. 13.6, p. 107", 560)


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
raster("t8-two-bodies",
       "Two rigid bodies B1 and B2 joined by a ball-and-socket joint at the common body point C, with external forces at P1 and P2 and an equal and opposite pair of forces between P3 and P4 on the same line of action.",
       r"Two rigid bodies joined at $C$; $\mathbf F^{P_1}$, $\mathbf F^{P_2}$ are external and $\mathbf f_{P_4}^{P_3}$, $\mathbf f_{P_3}^{P_4}$ are the equal and opposite forces the bodies exert on each other. Copied from Notes.pdf, Fig. 13.7, p. 108", 640)


# --------------------------------------------------------------------------------------------------------------------
raster("t8-exploded",
       "Exploded view of the two-body system: each body drawn apart with the reaction components R1, R2, R3 at C on B1 and the equal and opposite components on B2, plus the external and the internal forces.",
       r"Exploded view. The reaction at $C$ is $\mathbf R=R_1\mathbf i+R_2\mathbf j+R_3\mathbf k$ on $B_1$ and $-\mathbf R$ on $B_2$ (third law of Newton). Copied from Notes.pdf, Fig. 13.8, p. 109", 700)


# --------------------------------------------------------------------------------------------------------------------
raster("t8-torque-free-frames",
       "A free rigid body with its centre of mass G, the inertial frame S0 and the body-fixed principal frame Sb with different orientations.",
       r"Torque-free motion: the inertial frame $S_0$ (blue, $\mathbf i_0,\mathbf j_0,\mathbf k_0$) and the body-fixed principal frame $S_b$ (red, $\mathbf i_b,\mathbf j_b,\mathbf k_b$) with origin at the centre of mass $G$. Copied from Notes.pdf, p. 113", 440)


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
@figure("t8-rot-psi",
        "Precession: the axes i0 and j0 rotated by psi counter-clockwise about k0, which points out of the paper, giving i1 and "
        "j1.",
        r"Precession $\psi$ about $\mathbf k_0=\mathbf k_1$ (out of the paper $\odot$): the shaded right triangles give "
        r"$\mathbf i_1$ and $\mathbf j_1$ in $\mathcal B_0$.")
def rot_psi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("i", "0"), _ax("j", "0")), (_ax("i", "1"), _ax("j", "1")), None,
                          S(bold("k"), "0") + " = " + S(bold("k"), "1"), ("ψ", "view along k0 (out of the paper)"))


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
@figure("t8-rot-theta",
        "Nutation: the axes j1 and k1 rotated by theta counter-clockwise about i1, which points out of the paper, giving j2 and "
        "k2.",
        r"Nutation $\theta$ about $\mathbf i_1=\mathbf i_2$ (out of the paper $\odot$): the shaded right triangles give "
        r"$\mathbf j_2$ and $\mathbf k_2=\mathbf k_b$ in $\mathcal B_1$.")
def rot_theta():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("j", "1"), _ax("k", "1")), (_ax("j", "2"), _ax("k", "2")), None,
                          S(bold("i"), "1") + " = " + S(bold("i"), "2"), ("θ", "view along i1 (out of the paper)"))


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
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


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
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


# --------------------------------------------------------------------------------------------------------------------
raster("t8-poinsot",
       "Poinsot construction: the inertia ellipsoid fixed to the body is tangent at the tip of the angular velocity to a horizontal invariable plane normal to the angular momentum, with the polhode on the ellipsoid and the herpolhode on the plane.",
       r"Poinsot's construction: the energy ellipsoid rolls without slipping on the invariable plane; the contact point is the tip of $\boldsymbol\omega_{b0}$, the normal of the plane is $\mathbf H_{G0}$, the trace on the ellipsoid is the polhode and the trace on the plane the herpolhode. Copied from Notes.pdf, p. 117", 340)


# --------------------------------------------------------------------------------------------------------------------
raster("t8-polhodes",
       "The inertia ellipsoid with the polhodes: closed curves around the major and minor axes and the two separatrix ellipses through the intermediate axis.",
       r"Polhodes on the inertia ellipsoid (intersection with the angular momentum ellipsoids): closed curves about the major axis $\mathbf i_b$ and the minor axis $\mathbf k_b$, and the separatrices through the intermediate axis $\mathbf j_b$, where the rotation is unstable. Copied from Notes.pdf, p. 118", 400)

