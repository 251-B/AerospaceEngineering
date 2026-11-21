"""Theory figures of Topic 6 (Kinematics of Rigid Bodies and Inertia Properties)."""
import math

from figures.em_theory import axis_out, figure, fixed_axis, raster, right_angle, triangle, unit
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


# 3D sketch convention of the portal: x_0 down-left, y_0 to the right, z_0 up (cabinet projection, x foreshortened)
EX = (-0.789 * 0.6, -0.614 * 0.6)


def _p3(x, y, z):
    return (x * EX[0] + y, x * EX[1] + z)


def _p3v(v):
    return _p3(*v)


def _sub(sym, a, b=None):
    return S(bold(sym), a, b)


# --------------------------------------------------------------------------------------------------------------------
raster("t6-body-frame",
       "A rigid body with three body points P, Q and R, the fixed frame at O and the body-fixed basis built at P.",
       r"Body-fixed frame $S_B$ built from the non-collinear body points $P$, $Q$, $R$, with the fixed frame $S_0$ at $O$. Copied from Notes.pdf, Fig. 9.1, p. 75", 440)


# --------------------------------------------------------------------------------------------------------------------
raster("t6-projection-property",
       "Two body points A and P of a rigid body with their velocities and the line AP.",
       r"Equal projections: $\mathbf v_0^A\cdot\mathbf{PA}=\mathbf v_0^P\cdot\mathbf{PA}$. The parts of the velocities along the line $AP$ coincide, so the distance $AP$ stays constant. Copied from Notes.pdf, Fig. 9.2, p. 77", 380)


# --------------------------------------------------------------------------------------------------------------------
raster("t6-iar-foot",
       "The instantaneous axis of rotation, the point A, the foot I of the perpendicular from A and another point I' of the axis.",
       r"The point $I$ is the foot of the perpendicular from $A$ to the instantaneous axis (IAR), so $\mathbf{AI}\perp\boldsymbol\omega_{B0}$; another point $I'$ of the axis makes $\mathbf{AI'}$ longer. Copied from Notes.pdf, Fig. 9.3, p. 77", 400)


# --------------------------------------------------------------------------------------------------------------------
raster("t6-screw-field",
       "Screw motion velocity field: concentric circles of perpendicular velocities and a 3D sketch with the slip velocity.",
       r"Screw (helical) motion. Left: in a plane normal to $\boldsymbol\omega_{B0}$ the perpendicular velocities are tangent to circles about the axis. Right: on top of them all points share the slip velocity. Copied from Notes.pdf, Fig. 9.4, p. 78", 760)


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction or per-rotation view, not printed in the official material
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


# EXTRA: deduction or per-rotation view, not printed in the official material
@figure("t6-euler-313-psi",
        "Precession: the axes i0 and j0 rotated by psi counter-clockwise about k0, which points out of the paper, "
        "giving i1 and j1.",
        r"Precession $\psi$ about $\mathbf k_0=\mathbf k_1$ (out of the paper $\odot$): $\mathbf i_1$ and $\mathbf j_1$ "
        r"in $\mathcal B_0$ from the shaded right triangles (hypotenuse $1$).")
def euler313_psi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("i", "0"), _ax("j", "0")), (_ax("i", "1"), _ax("j", "1")),
                          None, S(bold("k"), "0") + " = " + S(bold("k"), "1"), (_PSI, "view along k0 (out of the paper)"))


# EXTRA: deduction or per-rotation view, not printed in the official material
@figure("t6-euler-313-theta",
        "Nutation: the axes j1 and k1 rotated by theta counter-clockwise about i1, which points out of the paper, "
        "giving j2 and k2.",
        r"Nutation $\theta$ about $\mathbf i_1=\mathbf i_2$ (out of the paper $\odot$, line of nodes): $\mathbf j_2$ and "
        r"$\mathbf k_2$ in $\mathcal B_1$ from the shaded right triangles.")
def euler313_theta():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("j", "1"), _ax("k", "1")), (_ax("j", "2"), _ax("k", "2")),
                          None, S(bold("i"), "1") + " = " + S(bold("i"), "2"), (_THETA, "view along i1 (out of the paper)"))


# EXTRA: deduction or per-rotation view, not printed in the official material
@figure("t6-euler-313-phi",
        "Spin: the axes i2 and j2 rotated by phi counter-clockwise about k2, which points out of the paper, giving iB and jB.",
        r"Spin $\varphi$ about $\mathbf k_2=\mathbf k_B$ (out of the paper $\odot$): $\mathbf i_B$ and $\mathbf j_B$ in "
        r"$\mathcal B_2$ from the shaded right triangles.")
def euler313_phi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("i", "2"), _ax("j", "2")), (_ax("i", "B"), _ax("j", "B")),
                          None, S(bold("k"), "2") + " = " + S(bold("k"), "B"), (_PHI, "view along k2 (out of the paper)"))


# EXTRA: deduction or per-rotation view, not printed in the official material
@figure("t6-euler-321-theta",
        "Pitch: the axes k1 and i1 rotated by theta counter-clockwise about j1, which points out of the paper, giving k2 "
        "and i2.",
        r"Pitch $\theta$ about $\mathbf j_1=\mathbf j_2$ (out of the paper $\odot$): $\mathbf k_1$ to the right, $\mathbf i_1$ "
        r"up, since $\mathbf k_1\times\mathbf i_1=\mathbf j_1$; the shaded triangles give $\mathbf k_2$ and $\mathbf i_2$.")
def euler321_theta():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("k", "1"), _ax("i", "1")), (_ax("k", "2"), _ax("i", "2")),
                          None, S(bold("j"), "1") + " = " + S(bold("j"), "2"), (_THETA, "view along j1 (out of the paper)"))


# EXTRA: deduction or per-rotation view, not printed in the official material
@figure("t6-euler-321-phi",
        "Roll: the axes j2 and k2 rotated by phi counter-clockwise about i2, which points out of the paper, giving jB and kB.",
        r"Roll $\varphi$ about $\mathbf i_2=\mathbf i_B$ (out of the paper $\odot$): $\mathbf j_B$ and $\mathbf k_B$ in "
        r"$\mathcal B_2$ from the shaded triangles (same as the nutation).")
def euler321_phi():
    return _rotation_view(500, 420, (150, 330), 160, 35, (_ax("j", "2"), _ax("k", "2")), (_ax("j", "B"), _ax("k", "B")),
                          None, S(bold("i"), "2") + " = " + S(bold("i"), "B"), (_PHI, "view along i2 (out of the paper)"))
