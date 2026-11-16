"""Problem RB-33: axle with two wheels (radii a and 2a) rolling on the ground about the apex O of a cone."""
import math

from figures.em_solutions import (axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle,
                                  unit)
from figures.em_sol.rb01 import add, d, rotation_view
from figures.em_sol.rb12 import plane_rotation
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold, dot1

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1, K1 = S(I, "1"), S(J, "1"), S(K, "1")
I2, J2, K2 = S(I, "2"), S(J, "2"), S(K, "2")
I3, K3 = S(I, "3"), S(K, "3")
A = 1.0
SQ3 = math.sqrt(3.0)


# ------------------------------------------------------------------------------------------------ rb33-rot-psi
@figure("rb33-rot-psi",
        "Top view: the rotating basis i1, j1 turned by psi, with the contact line OPQ along j1.",
        r"Rotation about $\mathbf k_0$ (⊙) by $\psi$. The line of the contact points $OPQ$ is $\mathbf j_1$; $P$ is at "
        r"$2a$ and $Q$ at $4a$ from $O$.")
def rot_psi():
    ang = 30.0
    j1 = d(ang + 90)

    def pre(sc):
        # the line of the contact points and the top view of the axle (from C1 at sqrt(3) a/2 ... to C2), on that line
        sc.line(add((0.0, 0.0), j1, 1.3), add((0.0, 0.0), j1, 4.5 * A), "EDGE", 1.3, "7 5")
        sc.line(add((0.0, 0.0), j1, 1.5 * A), add((0.0, 0.0), j1, 3.0 * A), "HEAD", 6.0)

    def post(sc):
        for dist, nm in ((2.0 * A, "P"), (4.0 * A, "Q")):
            p = add((0.0, 0.0), j1, dist)
            sc.mass(p, None, r=5, col="ACC")
            sc.label(p, nm + "  (O" + nm + " = " + str(int(dist)) + "a)", "HEAD", "end", 17, dx=-14, dy=5)
        sc.label(add((0.0, 0.0), j1, 3.0 * A), "axle (top view)", "TEXT", "start", 14, dx=12, dy=4)
        sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=22, dy=26)
    return plane_rotation(780, 800, (470, 690), 150, ang, (I0, J0, I1, J1), K0 + " (⊙)", ("ψ", ""),
                          ("ψ̇", 150, 240, 0.40), extra_pre=pre, extra_post=post, out_off=(-34, -16))


# ------------------------------------------------------------------------------------------------ the section of the axle
G30 = math.radians(30.0)
J2D = (math.cos(G30), math.sin(G30))
K2D = (-math.sin(G30), math.cos(G30))
C1 = (SQ3 * A * J2D[0], SQ3 * A * J2D[1])
C2 = (2 * SQ3 * A * J2D[0], 2 * SQ3 * A * J2D[1])
P_ = (2 * A, 0.0)
Q_ = (4 * A, 0.0)
G_ = (4.5 * 0.6 * A, 0.0)
GPT = (9 * SQ3 / 5 * A * J2D[0], 9 * SQ3 / 5 * A * J2D[1])         # (27a/10, 9 sqrt(3) a/10)


def _section(sc, wheels=True):
    """Ground, wheels edge-on, massless axle and the three marked points of the plane of the axle."""
    sc.ground((-0.9, 0.0), (5.0, 0.0), -1)
    if wheels:
        sc.line(add(C1, K2D, A), add(C1, K2D, -A), "EDGE", 7.0)
        sc.line(add(C2, K2D, 2 * A), add(C2, K2D, -2 * A), "EDGE", 7.0)
    sc.line(C1, C2, "HEAD", 4.0)


@figure("rb33-cone",
        "Section through the axle: the wheels as two sections of a cone with apex O and half-angle 30 degrees.",
        r"Plane of the axle. The right triangles $OC_1P$ and $OC_2Q$ are similar: $OC_1 = \sqrt3\,a$, the half-angle is "
        r"$30^\circ$, and $\mathbf j_2$ is $\mathbf j_1$ turned by $30^\circ$ about $\mathbf i_1$ (⊙).")
def cone():
    sc = Scene(860, 760, (140, 470), 128)
    O = (0.0, 0.0)
    triangle(sc, [O, C2, Q_], ORANGE, 0.10)
    triangle(sc, [O, C1, P_], ORANGE, 0.20)
    _section(sc)
    right_angle(sc, C1, 210, 300, 0.12)
    right_angle(sc, C2, 210, 300, 0.12)
    # grey fixed axes j1 and k1
    fixed_axis(sc, O, 90, 1.7, K1, off=(14, 4))
    sc.line((0.0, 0.0), (1.6, 0.0), "EDGE", 1.6)
    sc.label((1.6, 0.0), J1, "TEXT", "middle", 16, weight="700", dx=4, dy=-10)
    # blue j2 and k2
    unit(sc, O, 30.0, 1.0, J2, "BLUE", off=(16, -10))
    unit(sc, O, 120.0, 1.0, K2, "BLUE", off=(-14, -8))
    sc.arc(O, 0.6, 0, 30, "GREEN", 1.7, head=True)
    sc.label((0.98, 0.2), "30°", "GREEN", "start", 15, dx=0, dy=0)
    sc.arc(O, 0.45, 90, 120, "GREEN", 1.7, head=True)
    sc.label(add(O, d(97), 0.78), "30°", "GREEN", "end", 15, dx=-2, dy=0)
    # legs of the triangles
    sc.label(add(add(O, J2D, SQ3 / 2), K2D, 0.18), "√3 a", "TEXT", "end", 15, dx=-6, dy=-4)
    sc.label(((C1[0] + P_[0]) / 2, (C1[1] + P_[1]) / 2), "a", "TEXT", "start", 15, dx=8, dy=4)
    sc.label(add(add(O, J2D, 2.45), K2D, 0.2), "2√3 a", "TEXT", "end", 15, dx=-2, dy=-6)
    sc.label(((C2[0] + Q_[0]) / 2, (C2[1] + Q_[1]) / 2), "2a", "TEXT", "start", 15, dx=8, dy=4)
    # ground dimensions below the ground
    for x1, off, nm in ((2.0, -0.55, "OP = 2a"), (4.0, -1.0, "OQ = 4a")):
        sc.dim((0.0, off), (x1, off), nm, off=(0, 20))
        sc.dashed((x1, 0.0), (x1, off - 0.1))
    sc.dashed((0.0, 0.0), (0.0, -1.1))
    # centre of mass and its coordinates
    sc.mass(GPT, None, r=5, col="PINK")
    sc.label(GPT, "G", "HEAD", "middle", 17, dx=14, dy=22)
    sc.dashed(GPT, (GPT[0], 0.0))
    sc.dim((GPT[0] - 0.28, GPT[1]), (GPT[0] - 0.28, 0.0), "", off=(0, 0))
    sc.dashed(GPT, (GPT[0] - 0.36, GPT[1]))
    sc.label((GPT[0] - 0.28, GPT[1] / 2), "9√3 a / 10", "TEXT", "end", 15, dx=-8, dy=5)
    sc.dim((0.0, -1.45), (GPT[0], -1.45), "27 a / 10", off=(0, 20))
    sc.dashed((GPT[0], 0.0), (GPT[0], -1.55))
    sc.dashed((0.0, -1.1), (0.0, -1.55))
    for pt in (C1, C2, P_, Q_):
        sc.mass(pt, None, r=4.5, col="BLUE")
    sc.label(C1, S("C", "1"), "HEAD", "middle", 17, dx=22, dy=22)
    sc.label(C2, S("C", "2"), "HEAD", "middle", 17, dx=22, dy=22)
    sc.label(P_, "P", "HEAD", "middle", 17, dx=-14, dy=26)
    sc.label(Q_, "Q", "HEAD", "middle", 17, dx=-14, dy=26)
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.note(add(C2, K2D, 2 * A), "wheel of radius 2a", "TEXT", "start", 14, dx=12, dy=4)
    sc.note(add(C1, K2D, A), "wheel of radius a", "TEXT", "start", 14, dx=12, dy=4)
    axis_out(sc, (0.0, 0.0), None, "HEAD", 8)
    sc.label(O, I1 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-16, dy=30)
    return sc


# ------------------------------------------------------------------------------------------------ rb33-rot-phi
@figure("rb33-rot-phi",
        "View along the axle: the body basis i3, k3 turned by phi about j2 from its initial position along C2Q.",
        r"Rotation about the axle $\mathbf j_2$ (⊗) by $\phi$. At $\phi = 0$, $\mathbf i_3$ points along $C_2Q$, which is "
        r"$-\mathbf k_2$.")
def rot_phi():
    ph = 35.0
    c, s = math.cos(math.radians(ph)), math.sin(math.radians(ph))
    sc = Scene(860, 860, (430, 400), 120)
    O = (0.0, 0.0)
    R2 = 2.0 * A
    sc.poly(circle_pts(O, R2), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    # fixed axes i2, k2 and the dashed direction -k2 to Q
    fixed_axis(sc, O, 0, 2.5, I2, off=(16, 6))
    fixed_axis(sc, O, 90, 2.5, K2, off=(14, 4))
    sc.line(O, (0.0, -R2), "EDGE", 1.2, "5 4")
    sc.mass((0.0, -R2), None, r=4.5, col="ACC")
    sc.label((0.0, -R2), "Q", "HEAD", "middle", 17, dx=14, dy=22)
    sc.label((0.0, -1.5), S("C", "2") + "Q", "TEXT", "start", 15, dx=8, dy=0)
    # triangle of i3: adjacent leg along -k2, opposite leg along -i2
    i3, k3 = (-s, -c), (c, -s)
    foot_i, foot_k = (0.0, -c), (c, 0.0)
    triangle(sc, [O, foot_i, i3], ORANGE, 0.20)
    sc.dashed(foot_i, i3)
    right_angle(sc, foot_i, 90, 0, 0.07)
    triangle(sc, [O, foot_k, k3], ORANGE, 0.20)
    sc.dashed(foot_k, k3)
    right_angle(sc, foot_k, 180, 270, 0.07)
    unit(sc, O, -90 - ph, 1.0, I3, "BLUE", off=(-14, 20))
    unit(sc, O, -ph, 1.0, K3, "BLUE", off=(22, 12))
    # arcs of phi, clockwise
    sc.arc(O, 0.55, -90, -90 - ph, "GREEN", 1.7, head=True)
    sc.arc(O, 0.55, 0, -ph, "GREEN", 1.7, head=True)
    sc.label(add(O, d(-90 - ph / 2), 0.55), "φ", "GREEN", "middle", 17, dx=-14, dy=10)
    sc.label(add(O, d(-ph / 2), 0.55), "φ", "GREEN", "middle", 17, dx=8, dy=-6)
    # leg labels
    sc.label((-s / 2, -c), "sin φ", "TEXT", "middle", 14, dy=-8)
    sc.label((0.0, -0.41), "cos φ", "TEXT", "start", 14, dx=8, dy=6)
    sc.label((c / 2, 0.0), "cos φ", "TEXT", "middle", 14, dy=-8)
    sc.label((c, -s / 2), "sin φ", "TEXT", "start", 14, dx=8, dy=5)
    # the axle into the paper
    axis_in(sc, O, None, "HEAD", 9)
    sc.label(O, J2 + " (⊗)", "HEAD", "end", 16, weight="700", dx=-16, dy=-14)
    sc.label(O, S("C", "2"), "HEAD", "middle", 17, dx=18, dy=-26)
    sc.note((-2.9, -2.5), "positive rotation about an axis into the paper looks clockwise", "TEXT", "start", 14)
    return sc


# ------------------------------------------------------------------------------------------------ rb33-fbd
@figure("rb33-fbd",
        "Free-body diagram of the wheels and axle with the weight and the two contact forces.",
        r"Free-body diagram. $Y_P$ and $Y_Q$ act along the same line $OPQ$, so only their sum enters the equations of the "
        r"rigid body.")
def fbd():
    sc = Scene(960, 760, (150, 470), 128)
    O = (0.0, 0.0)
    G = GPT
    _section(sc)
    # arms from G to P and to Q: the shared vertical drop of G and the horizontal components below the ground
    foot = (G[0], 0.0)
    sc.dashed(G, P_)
    sc.dashed(G, Q_)
    sc.dashed(G, foot)
    sc.label((P_[0] + 0.45, 0.3), "GP", "TEXT", "start", 15, dx=6, dy=0)
    sc.label((Q_[0] - 0.4, 0.3), "GQ", "TEXT", "end", 15, dx=-2, dy=0)
    sc.label((G[0], 0.5), "−9√3 a/10", "TEXT", "start", 15, dx=10, dy=0)
    sc.label((G[0], 0.3), "(both arms)", "TEXT", "start", 13, dx=10, dy=0)
    for x0, x1, off, nm in ((G[0], P_[0], -0.62, "−7a/10"), (G[0], Q_[0], -0.62, "13a/10")):
        sc.dim((x0, off), (x1, off), nm, off=(0, 20))
        sc.dashed((x1, 0.0), (x1, off - 0.1))
    sc.dashed(foot, (foot[0], -0.72))
    # the common line of action of Y_P and Y_Q (the line OPQ, here the ground line)
    sc.c.add(f'<path d="M{sc.P(O)[0]:.1f},{sc.P(O)[1]:.1f} L{sc.P((4.6, 0.0))[0]:.1f},{sc.P((4.6, 0.0))[1]:.1f}" '
             f'stroke="GREEN" stroke-width="3.5" stroke-dasharray="1 7" stroke-linecap="round" fill="none"/>')
    sc.note((0.1, -1.5), "dotted: common line of action of " + S("Y", "P") + " and " + S("Y", "Q") + " (line OPQ)",
            "GREEN", "start", 14)
    # weight
    sc.vec(G, (G[0], G[1] - 0.5), None, "PINK", 3.2, head=12)
    sc.label((G[0], G[1] - 0.5), "mg", "PINK", "start", 17, weight="700", dx=8, dy=10)
    # contact forces
    for pt, nm in ((P_, "P"), (Q_, "Q")):
        sc.vec(pt, (pt[0], 0.75), None, "GREEN", 3.2, head=12)
        sc.label((pt[0], 0.75), S("N", nm), "GREEN", "end", 17, weight="700", dx=-8, dy=4)
        sc.vec(pt, (pt[0] - 0.9, 0.0), None, "GREEN", 3.2, head=12)
        sc.label((pt[0] - 0.9, 0.0), S("Y", nm), "GREEN", "end", 17, weight="700", dx=-6, dy=-12)
        x, y = sc.P(pt)
        sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="none" stroke="GREEN" stroke-width="2.4"/>')
        sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="GREEN"/>')
        sc.label(pt, S("X", nm) + " (⊙)", "GREEN", "start", 16, weight="700", dx=16, dy=34)
    # rotation rate about the vertical through O
    spin_about_vertical(sc, (0.0, 2.45), 0.45, 0.14, dot1("ψ"), "GREEN")
    fixed_axis(sc, O, 90, 1.9, K1, off=(14, 4))
    sc.line(O, (0.45, 0.0), "EDGE", 1.0)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=16, dy=-12)
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=-8)
    for pt, nm in ((P_, "P"), (Q_, "Q")):
        sc.label(pt, nm, "HEAD", "middle", 17, dx=-22, dy=-8)
    sc.note((2.95, 3.25), S("i", "1") + " out of the paper (⊙)", "TEXT", "start", 14)
    return sc
