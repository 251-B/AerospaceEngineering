"""Problem RB-31: ball bearing between a rotating cone and a cylindrical frame (angles theta of the ball centre, phi of the cone).

Figures: meridian section with the contact points and the instantaneous axis, top view with the two rotations about k0,
and the exploded view of the cone, the ball and the frame with the contact forces as action-reaction pairs.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb17 import rot_pair, off_dir
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1, K1 = S(I, "1"), S(J, "1"), S(K, "1")
N, ET = bold("n"), S(bold("e"), "t")
BETA = 30.0
BR = math.radians(BETA)
CB, SB = math.cos(BR), math.sin(BR)
R = 2.0
# geometry of the meridian plane (world units, R = 2): A on x = 2R, Q below it, P on the wall x = 3R, I on the cone
A = (2 * R, 0.0)
Q = (2 * R, -R)
P = (3 * R, 0.0)
I_PT = (R * (2 - CB), R * SB)
V = (0.0, -(2 * CB - 1) * R / SB)                      # apex of the cone
TOP = V[1] + 2 * R / SB * CB                           # height of the cone base (x = 2R on the generatrix)
GZ = TOP - (TOP - V[1]) / 4.0                          # centre of mass of the solid cone: a quarter of its height
EN = (CB, -SB)                                         # n, from the cone towards A
ETV = (SB, CB)                                         # e_t, up the generatrix


def sub(a, b):
    return S(a, b)


def pt(sc, p, name, off, col="BLUE", r=4.5, size=17):
    sc.mass(p, None, r=r, col=col)
    sc.label(p, name, "HEAD", "middle", size, dx=off[0], dy=off[1])


def hatch_lshape(sc, dx, dz, top=1.6 * R):
    """The frame d: an L-shaped section (bottom plate and wall) shifted by (dx, dz), light grey."""
    t = 0.28
    x0, x1, zb = 1 * R + dx, 3 * R + dx, -R + dz
    pts = [(x0, zb), (x1, zb), (x1, top + dz), (x1 + t, top + dz), (x1 + t, zb - t), (x0, zb - t)]
    sc.poly(pts, "HEAD", 1.8, fill="EDGE", close=True, opacity=0.25)


def cone_poly(sc, dx):
    pts = [(V[0] + dx, V[1]), (2 * R + dx, TOP), (dx, TOP)]
    sc.poly(pts, "HEAD", 1.8, fill="EDGE", close=True, opacity=0.25)


def axis_line(sc, x, z0, z1):
    sc.line((x, z0), (x, z1), "EDGE", 1.3, "11 3 2 3")


# ------------------------------------------------------------------------------------------------ rb31-meridian
@figure("rb31-meridian",
        "Meridian section with the ball touching the bottom at Q, the wall at P and the cone at I, the normal and tangent "
        "of the cone at I and the instantaneous axis PQ.",
        r"Meridian plane ($\mathbf j_1$ into the paper, ⊗): $\mathbf n = \cos\beta\,\mathbf i_1 - \sin\beta\,\mathbf k_1$, "
        r"$\mathbf e_t = \sin\beta\,\mathbf i_1 + \cos\beta\,\mathbf k_1$, $\overrightarrow{AI} = -R\mathbf n$; with no slip "
        r"the instantaneous axis is the line $PQ$, which meets the axis at the depth $3R$.")
def meridian():
    sc = Scene(820, 800, (190, 340), 58)
    O = (0.0, 0.0)
    # bodies: cone, frame, ball
    cone_poly(sc, 0.0)
    hatch_lshape(sc, 0.0, 0.0)
    sc.poly(circle_pts(A, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    axis_line(sc, 0.0, -3.3 * R, TOP + 0.6)
    sc.label((0.0, TOP + 0.6), K1 + " ≡ " + K0, "TEXT", "middle", 16, weight="700", dx=26, dy=-4)
    sc.vec((0.0, TOP + 0.05), (0.0, TOP + 0.6), None, "EDGE", 1.4, head=8)
    sc.vec(O, (7.4, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((7.4, 0.0), I1, "TEXT", "middle", 16, weight="700", dx=14, dy=-8)
    sc.note((-0.2, 3.0), "symmetry axis", "TEXT", "end", 13, dx=-2, dy=0)
    sc.note((0.9, 3.3), "cone c", "TEXT", "start", 14)
    sc.note((4.0, 1.5), "ball b", "TEXT", "middle", 14)
    sc.note((6.9, 2.4), "frame d", "TEXT", "start", 14)
    # basis at O: j1 into the paper
    axis_in(sc, O, None, "HEAD")
    sc.label(O, J1 + " (⊗)", "HEAD", "end", 16, weight="700", dx=-14, dy=-12)
    # the arm AI with its right triangle (corner (A.x, I.z)) and the angle beta at A
    corner = (A[0], I_PT[1])
    triangle(sc, [I_PT, corner, A], ORANGE, 0.20)
    sc.dashed(I_PT, corner)
    sc.dashed(corner, A)
    sc.line(A, I_PT, "EDGE", 1.4)
    sc.label(((I_PT[0] + corner[0]) / 2, I_PT[1]), "R cos β", "TEXT", "middle", 15, dy=-8)
    sc.label((corner[0], corner[1] / 2), "R sin β", "TEXT", "start", 15, dx=8, dy=5)
    sc.label(add(I_PT, (A[0] - I_PT[0], A[1] - I_PT[1]), 0.22), "R", "TEXT", "middle", 16, dx=-4, dy=20)
    sc.arc(A, 0.6, 180 - BETA, 180, "GREEN", 1.7, head=True)
    sc.label(add(A, d(180 - BETA / 2), 1.0), "β", "GREEN", "middle", 17, dx=0, dy=14)
    # apex arc
    sc.arc(V, 1.5, 90 - BETA, 90, "GREEN", 1.7, head=True)
    sc.label(add(V, d(90 - BETA / 2), 1.5), "β", "GREEN", "middle", 17, dx=18, dy=-4)
    # tangent and normal at I, with the triangle of e_t
    L = 1.3
    Fv = (I_PT[0], I_PT[1] + L * CB)
    T = add(I_PT, ETV, L)
    triangle(sc, [I_PT, Fv, T], ORANGE, 0.20)
    sc.dashed(I_PT, Fv)
    sc.dashed(Fv, T)
    sc.label(((I_PT[0] + Fv[0]) / 2, (I_PT[1] + Fv[1]) / 2), "cos β", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label(((Fv[0] + T[0]) / 2, Fv[1]), "sin β", "TEXT", "middle", 15, dy=-8)
    sc.label(add(I_PT, ETV, L * 0.5), "1", "TEXT", "middle", 15, dx=14, dy=8)
    unit(sc, I_PT, 90 - BETA, L, ET, "BLUE", off=(16, -10))
    unit(sc, I_PT, -BETA, 1.2, N, "BLUE", off=(2, 20))
    # instantaneous axis through Q and P, down to the axis of the cone
    X0 = (0.0, -3 * R)
    sc.line(X0, P, "PINK", 1.8, "9 5")
    sc.mass(X0, None, r=4.5, col="PINK")
    sc.label(X0, "IAR, z = −3R", "PINK", "start", 16, weight="700", dx=12, dy=22)
    # angular velocity of the ball (orange) from A
    w = (-1 / math.sqrt(2), -1 / math.sqrt(2))
    sc.vec(A, add(A, w, 1.6), S("ω", "b0"), ORANGE, 3.0, name_off=(-6, 24), size=18, head=12)
    sc.label((3.4, -3.15), S("ω", "b0") + " = −2 " + "θ̇" + " (" + I1 + " + " + K1 + ")", ORANGE, "start", 16, weight="700")
    sc.note((3.4, -3.65), "drawn for a positive θ̇", "TEXT", "start", 13)
    # points
    for p, nm, off, col in ((O, "O", (-14, 24), "HEAD"), (A, "A", (14, 20), "BLUE"), (Q, "Q", (-18, -16), "BLUE"),
                            (P, "P", (-16, -12), "BLUE"), (I_PT, "I", (-14, 8), "BLUE"), ((0.0, GZ), "G", (14, 6), "BLUE")):
        if p is O:
            sc.label(O, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
        else:
            pt(sc, p, nm, off, col)
    return sc


# ------------------------------------------------------------------------------------------------ rb31-rot-theta
@figure("rb31-rot-theta",
        "Top view of the bearing with the frame S1 turned by theta about k0, following the centre A of the ball, and the "
        "cone turned by phi.",
        r"Rotation about $\mathbf k_0$ (⊙): $\mathbf i_1 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0$, "
        r"$\mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$; the cone turns by $\phi$ about the same axis.")
def rot_theta():
    Rb, th, ph = 1.5, 35.0, 70.0
    sc = Scene(800, 800, (400, 400), 74)
    O = (0.0, 0.0)
    sc.poly(circle_pts(O, 3 * Rb), "HEAD", 2.4)
    sc.label(add(O, d(-52), 3 * Rb), "wall of the frame, 3R", "TEXT", "start", 14, italic=False, dx=44, dy=22)
    sc.poly(circle_pts(O, 2 * Rb), "EDGE", 1.4, "7 5", fill="EDGE", close=True, opacity=0.14)
    sc.label(add(O, d(-98), 2 * Rb), "path of A = base of the cone, 2R", "TEXT", "middle", 14, italic=False, dx=0, dy=-12)
    Ap = add(O, d(th), 2 * Rb)
    sc.poly(circle_pts(Ap, Rb), "HEAD", 1.6, fill="EDGE", close=True, opacity=0.10)
    sc.dashed(O, Ap)
    rot_pair(sc, th, (I0, J0, I1, J1), "θ", K0 + " (⊙)", "out", (-14, -14), L=1.3, Lf=4.9, arc_r=0.55, arc_lab=((20, 12), (-2, -2)),
             lab_offs=((22, 8), (-16, -12)))
    sc.mass(Ap, None, r=4.5, col="BLUE")
    sc.label(Ap, "A", "HEAD", "middle", 17, dx=-14, dy=22)
    # velocity of A, along j1
    vt = add(Ap, d(th + 90), 1.2)
    sc.vec(Ap, vt, S("v", "A") + " = 2R θ̇ " + J1, ORANGE, 3.0, name_off=(-10, -14), size=16, head=12)
    sc.label(vt, "", ORANGE, "end")
    # rotation of the cone: phi tick on the base, arc from i0, rate
    tk0, tk1 = add(O, d(ph), 2 * Rb - 0.18), add(O, d(ph), 2 * Rb + 0.18)
    sc.line(O, tk0, "GREEN", 1.3, "3 4")
    sc.line(tk0, tk1, "GREEN", 3.0)
    sc.arc(O, 2.1, 0, ph, "GREEN", 1.7, head=True)
    sc.label(add(O, d(ph / 2 + 12), 2.1), "φ", "GREEN", "middle", 17, dx=8, dy=-14)
    sc.label(tk1, "tick on the cone", "GREEN", "start", 14, italic=False, dx=8, dy=-8)
    sc.arc(O, 2.45, 150, 215, "GREEN", 2.0, head=True)
    sc.label(add(O, d(182), 2.45), "φ̇ " + K0 + " (cone)", "GREEN", "end", 16, weight="700", dx=-8, dy=6)
    return sc


# ------------------------------------------------------------------------------------------------ rb31-exploded
def force(sc, p, v, ln, name, col, off, size=15, w=2.8):
    n = math.hypot(*v)
    q = (p[0] + ln * v[0] / n, p[1] + ln * v[1] / n)
    sc.vec(p, q, name, col, w, name_off=off, size=size, head=11)
    return q


def out_sym(sc, p, kind, name, col, off, size=15):
    (axis_in if kind == "in" else axis_out)(sc, p, None, col, r_px=8)
    sc.label(p, name, col, "start", size, weight="700", dx=off[0], dy=off[1])


@figure("rb31-exploded",
        "Exploded view of the cone, the ball and the frame with the contact forces at I, P and Q as action-reaction pairs, "
        "the weights and the cylindrical joint of the cone.",
        r"Exploded view: the cone acts on the ball with $\mathbf F_I = N_I\mathbf n + F_{Ij}\mathbf j_1 + F_{It}\mathbf e_t$ "
        r"and the ball on the cone with $-\mathbf F_I$; the frame acts with $\mathbf F_Q$ and $\mathbf F_P$; the joint holds "
        r"the cone normal to its axis only.")
def exploded():
    sc = Scene(960, 700, (330, 300), 52)
    cx, fx, fz = -2.4, 1.6, -1.6                         # cone shifted by -1.2R, frame by (+0.8R, -0.8R)
    Ic, Qf, Pf = (I_PT[0] + cx, I_PT[1]), (Q[0] + fx, Q[1] + fz), (P[0] + fx, P[1] + fz)
    Gc = (cx, GZ)
    # bodies
    cone_poly(sc, cx)
    hatch_lshape(sc, fx, fz)
    sc.poly(circle_pts(A, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    axis_line(sc, cx, V[1] - 0.5, TOP + 1.9)
    sc.note((cx + 0.6, 3.2), "cone c", "TEXT", "start", 14)
    sc.note((A[0] - 0.2, 2.35), "ball b", "TEXT", "middle", 14)
    sc.note((P[0] + fx + 0.5, 1.2), "frame d", "TEXT", "start", 14)
    # action-reaction links
    for p, q in ((I_PT, Ic), (Q, Qf), (P, Pf)):
        sc.line(p, q, "EDGE", 1.3, "6 5")
    sc.note(((I_PT[0] + Ic[0]) / 2, 1.0), "action – reaction", "TEXT", "middle", 13, dy=-8)
    # ---- ball alone
    force(sc, A, (0, -1), 0.8, "", "PINK", (0, 0), w=3.2)
    sc.label((A[0], A[1] - 0.45), "mg", "PINK", "end", 17, weight="700", dx=-8, dy=4)
    force(sc, Q, (0, 1), 1.0, sub("N", "Q") + K1, "GREEN", (10, 4))
    force(sc, Q, (1, 0), 1.3, sub("F", "Qx") + I1, "GREEN", (26, 20))
    out_sym(sc, Q, "in", sub("F", "Qy") + J1, "GREEN", (-6, -22))
    force(sc, P, (-1, 0), 1.2, sub("N", "P"), "GREEN", (-4, -10))
    force(sc, P, (0, 1), 1.1, sub("F", "Pz") + K1, "GREEN", (8, 14))
    out_sym(sc, P, "in", sub("F", "Py") + J1, "GREEN", (10, 22))
    force(sc, I_PT, EN, 1.1, sub("N", "I") + N, "GREEN", (10, 20))
    force(sc, I_PT, ETV, 1.1, sub("F", "It") + ET, "GREEN", (20, 0))
    out_sym(sc, I_PT, "in", sub("F", "Ij") + J1, "GREEN", (-70, 28))
    # ---- cone alone
    force(sc, Ic, (-EN[0], -EN[1]), 1.1, "−" + sub("N", "I") + N, ORANGE, (-14, -10))
    force(sc, Ic, (-ETV[0], -ETV[1]), 1.1, "−" + sub("F", "It") + ET, ORANGE, (-8, 22))
    out_sym(sc, Ic, "out", "−" + sub("F", "Ij") + J1, ORANGE, (10, 24))
    # sleeve (joint) at G and the weight 2mg
    sc.poly([(cx - 0.2, GZ - 0.45), (cx + 0.2, GZ - 0.45), (cx + 0.2, GZ + 0.45), (cx - 0.2, GZ + 0.45)], "HEAD", 1.8,
            fill="BLUE", close=True, opacity=0.18)
    sc.mass(Gc, None, r=4.5, col="BLUE")
    sc.label(Gc, "G", "HEAD", "middle", 17, dx=-16, dy=-14)
    force(sc, (cx, GZ - 0.45), (0, -1), 0.9, "", "PINK", (0, 0), w=3.2)
    sc.label((cx, GZ - 0.9), "2mg", "PINK", "start", 17, weight="700", dx=8, dy=6)
    force(sc, (cx + 0.2, GZ), (1, 0), 0.9, "X" + I1, "GREEN", (4, -12))
    out_sym(sc, (cx, GZ + 0.12), "in", "Y" + J1, "GREEN", (12, -14))
    zt = GZ + 0.95
    sc.vec((cx, zt), (cx - 1.5, zt), None, "GREEN", 2.8, head=11)
    sc.vec((cx, zt), (cx + 1.5, zt), None, "GREEN", 2.8, head=11)
    sc.label((cx, zt), sub("M", "x") + I1 + " + " + sub("M", "y") + J1, "GREEN", "middle", 15, weight="700", dx=0, dy=-10)
    sc.note((cx - 0.3, GZ - 1.7), "joint: no axial force,", "TEXT", "end", 13)
    sc.note((cx - 0.3, GZ - 2.1), "no axial moment", "TEXT", "end", 13)
    from figures.em_solutions import spin_about_vertical
    spin_about_vertical(sc, (cx, TOP + 1.25), 0.95, 0.28, "Γ " + K0 + " (part g)", "GREEN", name_off=(12, -4))
    # ---- frame alone
    force(sc, Qf, (0, -1), 0.9, "−" + sub("N", "Q") + K1, ORANGE, (6, 18))
    force(sc, Qf, (-1, 0), 1.3, "−" + sub("F", "Qx") + I1, ORANGE, (-30, -8))
    out_sym(sc, Qf, "out", "−" + sub("F", "Qy") + J1, ORANGE, (12, 20))
    force(sc, Pf, (1, 0), 1.2, "+" + sub("N", "P"), ORANGE, (-2, -14))
    force(sc, Pf, (0, -1), 1.1, "−" + sub("F", "Pz") + K1, ORANGE, (10, 20))
    out_sym(sc, Pf, "out", "−" + sub("F", "Py") + J1, ORANGE, (-70, 24))
    # points
    for p, nm, off in ((A, "A", (-10, -34)), (Q, "Q", (-22, -16)), (P, "P", (-16, -8)), (I_PT, "I", (-8, 22)),
                       (Ic, "I", (14, 22)), (Qf, "Q", (-10, 36)), (Pf, "P", (-20, -8))):
        sc.mass(p, None, r=4.0, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 16, dx=off[0], dy=off[1])
    # basis
    b0 = (8.2, 3.2)
    sc.vec(b0, add(b0, (1, 0), 1.0), I1, "BLUE", 2.6, name_off=(14, 6), size=16, head=10)
    sc.vec(b0, add(b0, (0, 1), 1.0), K1, "BLUE", 2.6, name_off=(-12, -4), size=16, head=10)
    axis_in(sc, b0, None, "HEAD")
    sc.label(b0, J1 + " (⊗)", "HEAD", "end", 16, weight="700", dx=-14, dy=24)
    return sc
