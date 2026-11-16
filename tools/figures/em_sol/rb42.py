"""Problem RB-42: gyro on an inclined plane (sphere with an axle and a disk, 3-1-3 Euler angles psi, theta, phi and beta).

Figures: gravity in the basis of the plane, one view per rotation (psi about k0, theta about i1, phi about k2, beta about
ks) and the exploded view of the disk, the sphere with its axle and the plane.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb17 import rot_pair
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1, K1 = S(I, "1"), S(J, "1"), S(K, "1")
I2, J2, K2 = S(I, "2"), S(J, "2"), S(K, "2")
IS, JS, KS = S(I, "s"), S(J, "s"), S(K, "s")
ID, JD = S(I, "d"), S(J, "d")
EH, EV = S(bold("e"), "h"), S(bold("e"), "v")


def sub(a, b):
    return S(a, b)


# ------------------------------------------------------------------------------------------------ rb42-gravity
@figure("rb42-gravity",
        "Section along the line of greatest slope showing i0 down the slope, k0 normal to the plane, j0 into the paper, and "
        "gravity split into g sin gamma along i0 and g cos gamma into the plane.",
        r"Read from the statement figure: $\mathbf i_0$ points down the slope and $\mathbf j_0$ is horizontal, so "
        r"$\mathbf g = g\sin\gamma\,\mathbf i_0 - g\cos\gamma\,\mathbf k_0$.")
def gravity():
    gam, Rs = 20.0, 1.5
    sc = Scene(980, 640, (290, 290), 105)
    O = (0.0, 0.0)
    i0, k0 = d(-gam), d(90 - gam)
    sc.line(add(O, i0, -2.6), add(O, i0, 5.6), "EDGE", 6.0)
    fixed_axis(sc, O, 0, 1.5, EH, off=(16, -12))
    fixed_axis(sc, O, 90, 2.2, EV, off=(14, 0))
    unit(sc, O, -gam, 1.3, I0, "BLUE", off=(14, 16))
    unit(sc, O, 90 - gam, 1.3, K0, "BLUE", off=(14, -6))
    sc.arc(O, 0.6, 0, -gam, "GREEN", 1.7, head=True)
    sc.label(add(O, d(-gam / 2), 0.62), "γ", "GREEN", "middle", 16, dx=14, dy=4)
    sc.arc(O, 0.6, 90, 90 - gam, "GREEN", 1.7, head=True)
    sc.label(add(O, d(90 - gam / 2), 0.62), "γ", "GREEN", "middle", 16, dx=6, dy=-8)
    axis_in(sc, O, None, "HEAD")
    sc.label(O, J0 + " (⊗)", "HEAD", "end", 16, weight="700", dx=-10, dy=32)
    # sphere touching the plane at C
    C = add(O, i0, 2.8)
    G = add(C, k0, Rs)
    sc.poly(circle_pts(G, Rs), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    sc.dashed(C, G)
    sc.label(add(C, k0, 0.28), "R", "TEXT", "end", 16, dx=-8, dy=4)
    sc.mass(C, None, r=4.5, col="BLUE")
    sc.label(C, "C", "HEAD", "middle", 17, dx=-4, dy=24)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=-10)
    # gravity from G, with its right triangle
    Lg = 1.0
    P1 = add(G, k0, -Lg * math.cos(math.radians(gam)))
    tip = (G[0], G[1] - Lg)
    triangle(sc, [G, P1, tip], ORANGE, 0.20)
    sc.dashed(P1, tip)
    sc.line(G, P1, "EDGE", 1.4)
    sc.vec(G, tip, None, "PINK", 3.4, head=13)
    sc.label((G[0], G[1] - 0.7), "g", "PINK", "start", 19, weight="700", dx=10, dy=4)
    sc.label((G[0] + 0.5 * (P1[0] - G[0]), G[1] + 0.5 * (P1[1] - G[1])), "g cos γ", "TEXT", "end", 15, dx=-8, dy=-2)
    sc.label(((P1[0] + tip[0]) / 2, (P1[1] + tip[1]) / 2), "g sin γ", "TEXT", "middle", 15, dx=2, dy=26)
    right_angle(sc, P1, 90 - gam, -gam, 0.1)
    sc.arc(G, 0.6, -90 - gam, -90, "GREEN", 1.7, head=True)
    sc.label(add(G, d(-90 - gam / 2), 0.75), "γ", "GREEN", "middle", 15, dx=-2, dy=6)
    # xi grows down the slope
    a0 = add(add(O, i0, 2.2), k0, -0.45)
    sc.vec(a0, add(a0, i0, 1.2), None, ORANGE, 2.4, head=10)
    sc.note(a0, "ξ grows down the slope", "TEXT", "end", 13, dx=-8, dy=16)
    return sc


# ------------------------------------------------------------------------------------------------ rb42-rot-psi
@figure("rb42-rot-psi",
        "Precession: the basis B1 turned by psi about the normal k0 of the plane.",
        r"Precession about $\mathbf k_0$ (⊙): $\mathbf i_1 = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0$, "
        r"$\mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0$.")
def rot_psi():
    ps = 35.0
    sc = Scene(820, 760, (330, 400), 130)
    rot_pair(sc, ps, (I0, J0, I1, J1), "ψ", K0 + " (⊙)", "out", (-14, 30), L=1.9, Lf=2.6, arc_r=0.6,
             arc_lab=((20, 12), (-4, 4)), lab_offs=((24, 4), (-18, -6)))
    tip = add((0.0, 0.0), d(ps), 2.6)
    sc.line(add((0.0, 0.0), d(ps), 1.9), tip, "BLUE", 1.3, "7 5")
    sc.label(tip, "line of nodes", "BLUE", "start", 15, dx=10, dy=-8)
    return sc


# ------------------------------------------------------------------------------------------------ rb42-rot-theta
@figure("rb42-rot-theta",
        "Nutation: the axle k2 tilted by theta from the normal k0 about the line of nodes i1.",
        r"Nutation about $\mathbf i_1$ (⊙): $\mathbf j_2 = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1$, "
        r"$\mathbf k_2 = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1$.")
def rot_theta():
    th = 30.0
    sc = Scene(820, 800, (330, 450), 130)
    O = (0.0, 0.0)
    ax = d(90 + th)
    sc.line(add(O, ax, -2.3), add(O, ax, 2.9), "EDGE", 6.0)
    rot_pair(sc, th, (J1, K1, J2, K2), "θ", I1 + " (⊙)", "out", (-14, 30), L=1.9, Lf=2.6, arc_r=0.6,
             arc_lab=((20, 12), (-4, 4)), lab_offs=((24, 4), (-22, -8)))
    sc.label(add(O, ax, 2.9), "B", "HEAD", "middle", 18, dx=-14, dy=-6)
    sc.label(add(O, ax, -2.3), "A", "HEAD", "middle", 18, dx=14, dy=14)
    sc.label(add(O, ax, 2.45), "axle, " + K2 + " = " + KS, "TEXT", "end", 15, dx=-16, dy=12)
    return sc


# ------------------------------------------------------------------------------------------------ rb42-rot-phi
@figure("rb42-rot-phi",
        "Spin of the sphere: its basis Bs turned by phi about the axle k2.",
        r"Spin of the sphere about $\mathbf k_2 = \mathbf k_s$ (⊙): $\mathbf i_s = \cos\phi\,\mathbf i_2 + "
        r"\sin\phi\,\mathbf j_2$, $\mathbf j_s = -\sin\phi\,\mathbf i_2 + \cos\phi\,\mathbf j_2$.")
def rot_phi():
    ph = 25.0
    sc = Scene(820, 800, (410, 400), 110)
    O = (0.0, 0.0)
    sc.poly(circle_pts(O, 2.9), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.08)
    sc.label(add(O, d(-60), 2.9), "sphere", "TEXT", "start", 14, dx=12, dy=14)
    rot_pair(sc, ph, (I2, J2, IS, JS), "φ", K2 + " = " + KS + " (⊙)", "out", (-14, 30), L=1.9, Lf=3.2, arc_r=0.6,
             arc_lab=((20, 12), (-4, 4)), lab_offs=((24, 4), (-22, -8)), out_anchor="end")
    return sc


# ------------------------------------------------------------------------------------------------ rb42-rot-beta
@figure("rb42-rot-beta",
        "The disk basis Bd turned by beta about the axle relative to the sphere basis Bs.",
        r"Turn of the disk about the axle (⊙): $\mathbf i_d = \cos\beta\,\mathbf i_s + \sin\beta\,\mathbf j_s$, "
        r"$\mathbf j_d = -\sin\beta\,\mathbf i_s + \cos\beta\,\mathbf j_s$; the disk radius $R/\sqrt3$ is the one implied by "
        r"its tensor.")
def rot_beta():
    be, R = 50.0, 3.0
    rd = R / math.sqrt(3.0)
    sc = Scene(820, 800, (410, 400), 100)
    O = (0.0, 0.0)
    sc.poly(circle_pts(O, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.06)
    sc.label(add(O, d(-62), R), "sphere, R", "TEXT", "start", 14, dx=12, dy=14)
    sc.poly(circle_pts(O, rd), "HEAD", 1.6, fill="EDGE", close=True, opacity=0.25)
    sc.label(add(O, d(-120), rd), "disk, R/√3", "TEXT", "end", 14, dx=-10, dy=22)
    mk = add(O, d(be), rd)
    sc.mass(mk, None, r=5, col="ACC")
    sc.label(mk, "mark", "HEAD", "start", 14, dx=10, dy=-8)
    rot_pair(sc, be, (IS, JS, ID, JD), "β", KS + " = " + S(K, "d") + " (⊙)", "out", (-14, 30), L=1.5, Lf=3.4, arc_r=0.4,
             col="GREEN", arc_lab=((12, 14), (4, 18)), lab_offs=((22, 8), (-22, -8)), inner2=True)
    return sc


# ------------------------------------------------------------------------------------------------ rb42-exploded
def force(sc, p, v, ln, name, col, off, size=15, w=2.6, head=11):
    n = math.hypot(*v)
    q = (p[0] + ln * v[0] / n, p[1] + ln * v[1] / n)
    sc.vec(p, q, name, col, w, name_off=off, size=size, head=head)
    return q


def double_arrow(sc, p, v, ln, col, name, off, size=15):
    """Torque drawn as a double-headed arrow along v (length ln)."""
    from figures.svgkit import arrow_head
    n = math.hypot(*v)
    u = (v[0] / n, v[1] / n)
    q = (p[0] + ln * u[0], p[1] + ln * u[1])
    sc.vec(p, q, None, col, 2.6, head=11)
    q2 = (q[0] - 0.22 * u[0], q[1] - 0.22 * u[1])
    arrow_head(sc.c, sc.P(p), sc.P(q2), col, 11)
    sc.label(q, name, col, "middle", size, weight="700", dx=off[0], dy=off[1])


@figure("rb42-exploded",
        "Exploded view of the disk, the sphere with its axle and the inclined plane, with the bearing force and torque pair "
        "at G, the contact force pair at C and the weights.",
        r"Exploded view: the plane acts on the sphere with $\mathbf R_C = F_1\mathbf i_0 + F_2\mathbf j_0 + N\mathbf k_0$ "
        r"at $C$; the axle acts on the disk with $\mathbf R_d$ and the torque $\mathbf M_d$ normal to $\mathbf k_s$, and the "
        r"disk on the axle with $-\mathbf R_d$ and $-\mathbf M_d$.")
def exploded():
    R = 1.4
    sc = Scene(960, 700, (400, 330), 62)
    ks, i_s, j_s = d(60), d(-50), d(15)
    i0, j0, k0 = d(-12), d(30), (0.0, 1.0)
    G = (0.0, 0.0)
    Gd = add(G, ks, 2.1)                                     # the disk, lifted 1.5 R along the axle
    C = add(G, k0, -R)
    Cp = add(C, k0, -0.84)                                    # the plane, pulled down 0.6 R
    # plane (parallelogram)
    pl = [add(Cp, (-4.0, -0.55)), add(Cp, (1.9, -0.55)), add(Cp, (3.3, 0.55)), add(Cp, (-2.6, 0.55))]
    sc.poly(pl, "HEAD", 1.8, fill="EDGE", close=True, opacity=0.18)
    sc.note(add(Cp, (1.6, -0.3)), "plane", "TEXT", "start", 14)
    # sphere with the axle AB
    sc.poly(circle_pts(G, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    sc.line(add(G, ks, -R), add(G, ks, R), "HEAD", 3.0)
    sc.label(add(G, ks, R), "B", "HEAD", "middle", 16, dx=-12, dy=-2)
    sc.label(add(G, ks, -R), "A", "HEAD", "middle", 16, dx=-14, dy=4)
    sc.note((-1.45, 1.1), "sphere s", "TEXT", "end", 14)
    # disk (ellipse normal to the axle)
    rd = R / math.sqrt(3.0)
    pts = [add(add(Gd, d(-18), rd * math.cos(math.radians(t))), ks, 0.30 * rd * math.sin(math.radians(t))) for t in range(0, 361, 10)]
    sc.poly(pts, "HEAD", 1.8, fill="EDGE", close=True, opacity=0.35)
    sc.note(add(Gd, (-1, 0), 0.95), "disk d", "TEXT", "end", 14, dx=0, dy=4)
    # links
    sc.line(G, Gd, "EDGE", 1.3, "6 5")
    sc.line(C, Cp, "EDGE", 1.3, "6 5")
    # ---- disk alone: R_d (components and resultant), M_d, weight
    comps = [(i_s, 0.9, sub("X", "d")), (j_s, 0.9, sub("Y", "d")), (ks, 0.9, sub("Z", "d"))]
    rs = (0.0, 0.0)
    for v, ln, nm in comps:
        force(sc, Gd, v, ln, nm, "GREEN", (16, 6) if nm.endswith("d</tspan>") and v is i_s else (10, -10), w=1.8, head=9)
        rs = (rs[0] + v[0] * ln, rs[1] + v[1] * ln)
    sc.vec(Gd, add(Gd, rs), sub("R", "d"), "GREEN", 3.6, name_off=(18, -6), size=18, head=13)
    double_arrow(sc, Gd, d(-18), 1.5, "GREEN", sub("M", "d"), (14, 16))
    force(sc, Gd, (0, -1), 0.7, "", "PINK", (0, 0), w=3.2, head=12)
    sc.label(add(Gd, (0, -1), 0.7), "2mg", "PINK", "start", 17, weight="700", dx=8, dy=4)
    sc.note(add(Gd, (-1, 0), 0.95), "M_d = M1 i_s + M2 j_s,", "TEXT", "end", 13, dx=0, dy=-38)
    sc.note(add(Gd, (-1, 0), 0.95), "no component along k_s", "TEXT", "end", 13, dx=0, dy=-22)
    # ---- sphere: -R_d, -M_d, weight, R_C
    nrs = (-rs[0], -rs[1])
    sc.vec(G, add(G, nrs), "−" + sub("R", "d"), ORANGE, 3.6, name_off=(-24, 10), size=17, head=13)
    double_arrow(sc, G, d(162), 1.5, ORANGE, "−" + sub("M", "d"), (-18, 14))
    force(sc, G, (0, -1), 0.5, "", "PINK", (0, 0), w=3.2, head=12)
    sc.label(add(G, (0, -1), 0.5), "mg", "PINK", "start", 17, weight="700", dx=8, dy=4)
    sc.dashed(G, C)
    sc.label(add(G, (0, -1), R / 2), "−R k0", "TEXT", "end", 14, dx=-6, dy=18)
    rc = (0.0, 0.0)
    for v, ln, nm in ((i0, 1.1, sub("F", "1")), (j0, 1.0, sub("F", "2")), (k0, 0.6, "N")):
        force(sc, C, v, ln, nm, "GREEN", (14, 12) if v is i0 else ((-16, -10) if v is j0 else (14, 6)), w=1.8, head=9)
        rc = (rc[0] + v[0] * ln, rc[1] + v[1] * ln)
    sc.vec(C, add(C, rc), sub("R", "C"), "GREEN", 3.6, name_off=(20, -8), size=18, head=13)
    # ---- plane: -R_C
    sc.vec(Cp, add(Cp, (-rc[0], -rc[1])), "−" + sub("R", "C"), ORANGE, 3.6, name_off=(-26, 12), size=17, head=13)
    for p, nm, off in ((G, "G", (-16, -12)), (Gd, "G", (-16, -12)), (C, "C", (-16, 22)), (Cp, "C", (14, 22))):
        sc.mass(p, None, r=4.0, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 16, dx=off[0], dy=off[1])
    # bases: grey at O on the plane, blue at G
    o0 = add(Cp, (-3.0, 0.1))
    unit(sc, o0, -12, 0.9, I0, "EDGE", off=(14, 8))
    unit(sc, o0, 30, 0.9, J0, "EDGE", off=(12, -6))
    unit(sc, o0, 90, 0.9, K0, "EDGE", off=(-10, -6))
    sc.label(o0, "O", "HEAD", "middle", 15, dx=-14, dy=18)
    bg = (-4.2, 0.1)
    unit(sc, bg, -50, 0.9, IS, "BLUE", off=(14, 8))
    unit(sc, bg, 15, 0.9, JS, "BLUE", off=(12, -6))
    unit(sc, bg, 60, 0.9, KS, "BLUE", off=(-6, -12))
    return sc
