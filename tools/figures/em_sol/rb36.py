"""Problem RB-36: Mars rolling rover (slotted cylinder rolling on a slope, particle pushed along the slot by a motor).

Figures: gravity in the basis of the slope, the cylinder basis turned clockwise by phi, and the exploded view of the
cylinder and the particle.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1 = S(I, "1"), S(J, "1")
EH, EV = S(bold("e"), "h"), S(bold("e"), "v")


def sub(a, b):
    return S(a, b)


def stadium2(sc, c, ang, half_len, half_w, w=1.6):
    pts = []
    for t in range(-90, 91, 15):
        pts.append(add(add(c, d(ang), half_len), d(ang + t), half_w))
    for t in range(-90, 91, 15):
        pts.append(add(add(c, d(ang), -half_len), d(ang + 180 + t), half_w))
    sc.poly(pts, "HEAD", w, close=True)


# ------------------------------------------------------------------------------------------------ rb36-gravity
@figure("rb36-gravity",
        "The slope basis i0, j0 turned by gamma from the horizontal and the right triangle that splits gravity into "
        "g sin gamma down the slope and g cos gamma into the slope.",
        r"$\mathbf g = -g(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0)$: the hypotenuse $g$, the leg $g\cos\gamma$ "
        r"normal to the slope and the leg $g\sin\gamma$ down the slope.")
def gravity():
    gam = 15.0
    sc = Scene(760, 620, (300, 450), 75)
    O = (0.0, 0.0)
    S0 = add(O, d(gam), -3.6)
    sc.line(S0, add(O, d(gam), 4.9), "EDGE", 6.0)
    sc.line(S0, add(S0, (1, 0), 3.0), "EDGE", 1.2, "6 4")
    sc.arc(S0, 1.6, 0, gam, "GREEN", 1.7, head=True)
    sc.label(add(S0, d(gam / 2), 1.6), "γ", "GREEN", "middle", 17, dx=16, dy=8)
    sc.note(add(O, d(gam), -3.6), "slope", "TEXT", "start", 13, dx=2, dy=22)
    fixed_axis(sc, O, 0, 2.1, EH, off=(14, 14))
    fixed_axis(sc, O, 90, 2.1, EV, off=(14, 0))
    unit(sc, O, gam, 1.4, I0, "BLUE", off=(8, -14))
    unit(sc, O, gam + 90, 1.4, J0, "BLUE", off=(-16, -4))
    sc.arc(O, 0.6, 0, gam, "GREEN", 1.7, head=True)
    sc.label(add(O, d(gam / 2), 1.0), "γ", "GREEN", "middle", 16, dx=0, dy=5)
    sc.arc(O, 0.6, 90, 90 + gam, "GREEN", 1.7, head=True)
    sc.label(add(O, d(90 + gam / 2), 1.0), "γ", "GREEN", "middle", 16, dx=0, dy=4)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, K0 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=26)
    # gravity and its right triangle
    Lg = 2.4
    G0 = (3.0, 4.2)
    P1 = add(G0, d(gam - 90), Lg * math.cos(math.radians(gam)))
    tip = (G0[0], G0[1] - Lg)
    triangle(sc, [G0, P1, tip], ORANGE, 0.20)
    sc.dashed(P1, tip)
    sc.line(G0, P1, "EDGE", 1.4)
    sc.vec(G0, tip, None, "PINK", 3.4, head=13)
    sc.label((G0[0], G0[1] - Lg * 0.5), "g", "PINK", "end", 19, weight="700", dx=-10, dy=6)
    sc.label(((G0[0] + P1[0]) / 2, (G0[1] + P1[1]) / 2), "g cos γ", "TEXT", "start", 15, dx=10, dy=4)
    sc.label(((P1[0] + tip[0]) / 2, (P1[1] + tip[1]) / 2), "g sin γ", "TEXT", "middle", 15, dx=6, dy=24)
    right_angle(sc, P1, gam + 90, gam + 180, 0.12)
    sc.arc(G0, 0.9, -90, gam - 90, "GREEN", 1.7, head=True)
    sc.label(add(G0, d(gam / 2 - 90), 1.25), "γ", "GREEN", "middle", 16, dx=-4, dy=10)
    return sc


# ------------------------------------------------------------------------------------------------ rb36-rot-phi
@figure("rb36-rot-phi",
        "The cylinder basis i1, j1 turned clockwise by phi from the slope basis i0, j0, with the slot along i1 and the "
        "particle P on it.",
        r"Rotation by $\varphi$ about $-\mathbf k_0$ (clockwise as seen): $\mathbf i_1 = \cos\varphi\,\mathbf i_0 - "
        r"\sin\varphi\,\mathbf j_0$, $\mathbf j_1 = \sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0$. The sense of "
        r"$\varphi$ is a reading of the statement figure.")
def rot_phi():
    ph, Rc, el, x1 = 30.0, 3.0, 2.2, 1.5
    sc = Scene(780, 760, (390, 340), 80)
    O = (0.0, 0.0)
    L = 2.3
    c, s = math.cos(math.radians(ph)), math.sin(math.radians(ph))
    sc.poly(circle_pts(O, Rc), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    stadium2(sc, O, -ph, el, 0.17)
    # slope under the contact point A
    A = (0.0, -Rc)
    sc.ground((-1.8, -Rc), (1.8, -Rc), -1)
    fixed_axis(sc, O, 0, 3.6, I0, off=(16, 8))
    fixed_axis(sc, O, 90, 3.5, J0, off=(14, 0))
    # triangle of i1 (below the i0 axis) and of j1
    f1, t1 = (L * c, 0.0), (L * c, -L * s)
    triangle(sc, [O, f1, t1], ORANGE, 0.20)
    sc.dashed(f1, t1)
    right_angle(sc, f1, 180, 270, 0.08)
    f2, t2 = (0.0, L * c), (L * s, L * c)
    triangle(sc, [O, f2, t2], ORANGE, 0.20)
    sc.dashed(f2, t2)
    right_angle(sc, f2, 270, 0, 0.08)
    unit(sc, O, -ph, L, I1, "BLUE", off=(22, 12))
    unit(sc, O, 90 - ph, L, J1, "BLUE", off=(12, -12))
    sc.label((L * c / 2, 0), "cos φ", "TEXT", "middle", 15, dy=-9)
    sc.label((L * c, -L * s / 2), "sin φ", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((0, L * c / 2), "cos φ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((L * s / 2, L * c), "sin φ", "TEXT", "middle", 15, dy=-9)
    sc.label(add(O, d(-ph), L * 0.55), "1", "TEXT", "middle", 15, dx=8, dy=-14)
    sc.label(add(O, d(90 - ph), L * 0.55), "1", "TEXT", "middle", 15, dx=14, dy=4)
    # clockwise arcs of phi
    sc.arc(O, 0.7, 0, -ph, "GREEN", 1.7, head=True)
    sc.label(add(O, d(-ph / 2), 0.7), "φ", "GREEN", "middle", 16, dx=16, dy=18)
    sc.arc(O, 0.7, 90, 90 - ph, "GREEN", 1.7, head=True)
    sc.label(add(O, d(90 - ph / 2), 0.7), "φ", "GREEN", "middle", 16, dx=8, dy=-12)
    # rate
    sc.arc(O, 1.4, 250, 195, "GREEN", 2.0, head=True)
    sc.label(add(O, d(222), 1.4), S("ω", "10") + " = −" + "φ̇" + " " + K0, "GREEN", "end", 16, weight="700", dx=-10, dy=4)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "C", "HEAD", "middle", 17, dx=-20, dy=26)
    sc.label((-0.25, 2.3), K0 + " (⊙) at C", "HEAD", "end", 16, weight="700")
    # particle and its coordinate x1
    P = add(O, d(-ph), x1)
    sc.mass(P, None, r=6, col="HEAD")
    sc.label(P, "P", "HEAD", "middle", 17, dx=14, dy=28)
    nv = d(-ph - 90)
    a, b = add(O, nv, 0.95), add(P, nv, 0.95)
    sc.dashed(O, add(O, nv, 1.02))
    sc.dashed(P, add(P, nv, 1.02))
    sc.dim(a, b, sub("x", "1"), off=(-8, 24))
    sc.mass(A, None, r=4.5, col="BLUE")
    sc.label(A, "A", "HEAD", "middle", 17, dx=18, dy=-10)
    return sc


# ------------------------------------------------------------------------------------------------ rb36-exploded
def force(sc, p, v, ln, name, col, off, size=16, w=2.8, head=11):
    n = math.hypot(*v)
    q = (p[0] + ln * v[0] / n, p[1] + ln * v[1] / n)
    sc.vec(p, q, name, col, w, name_off=off, size=size, head=head)
    return q


@figure("rb36-exploded",
        "Exploded view of the cylinder and the particle with the force pair F and -F at P, the weights and the contact "
        "force of the slope at A.",
        r"Exploded view: the particle acts on the cylinder with $\mathbf F = F_1\mathbf i_1 + F_2\mathbf j_1$ at $P$ and "
        r"the cylinder on the particle with $-\mathbf F$; the slope acts at $A$ with $f_A\mathbf i_0 + N_A\mathbf j_0$.")
def exploded():
    ph, gam, Rc, el, x1 = 30.0, 10.0, 3.0, 2.2, 1.5
    sc = Scene(900, 760, (330, 350), 70)
    O = (0.0, 0.0)
    i1, j1 = d(-ph), d(90 - ph)
    sc.poly(circle_pts(O, Rc), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    stadium2(sc, O, -ph, el, 0.17)
    A = (0.0, -Rc)
    sc.ground((-3.0, -Rc), (3.0, -Rc), -1)
    # cylinder: weight (true vertical), arm to A and the angle gamma
    sc.line(O, A, "EDGE", 1.2, "6 4")
    sc.label((0, -Rc / 2), "R", "TEXT", "start", 16, dx=8, dy=4)
    wdir = d(-90 - gam)
    sc.vec(O, add(O, wdir, 2.1), None, "PINK", 3.4, head=13)
    sc.label(add(O, wdir, 2.1), "Mg", "PINK", "end", 18, weight="700", dx=-10, dy=8)
    sc.arc(O, 1.5, -90 - gam, -90, "GREEN", 1.7, head=True)
    sc.label(add(O, d(-90 - gam / 2), 2.45), "γ", "GREEN", "middle", 16, dx=-4, dy=4)
    # contact force at A
    force(sc, A, (1, 0), 1.4, sub("f", "A") + "", "GREEN", (4, 20))
    force(sc, A, (0, 1), 0.9, sub("N", "A"), "GREEN", (22, 4))
    sc.mass(A, None, r=4.5, col="BLUE")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-18, dy=24)
    sc.mass(O, None, r=4.0, col="BLUE")
    sc.label(O, "C", "HEAD", "middle", 17, dx=-14, dy=-12)
    # force of the particle on the cylinder at P
    P = add(O, i1, x1)
    sc.mass(P, None, r=4.5, col="BLUE")
    sc.label(P, "P", "HEAD", "middle", 17, dx=-15, dy=-26)
    f1, f2 = 0.9, 0.8
    force(sc, P, i1, f1, sub("F", "1"), ORANGE, (14, 18))
    force(sc, P, j1, f2, sub("F", "2"), ORANGE, (-16, 2))
    rt = add(P, (i1[0] * f1 + j1[0] * f2, i1[1] * f1 + j1[1] * f2))
    sc.vec(P, rt, "F", ORANGE, 3.6, name_off=(14, -4), size=18, head=13)
    # dimension x1 below the slot
    nv = d(-ph - 90)
    a, b = add(O, nv, 0.6), add(P, nv, 0.6)
    sc.dashed(O, add(O, nv, 0.66))
    sc.dashed(P, add(P, nv, 0.66))
    sc.dim(a, b, sub("x", "1"), off=(-14, 18))
    # particle alone, 1.2 R outside along j1
    P2 = add(P, j1, 1.2 * Rc)
    sc.line(P, P2, "EDGE", 1.3, "6 5")
    sc.mass(P2, None, r=7.5, col="HEAD")
    sc.label(P2, "P", "HEAD", "middle", 17, dx=18, dy=22)
    force(sc, P2, (-i1[0], -i1[1]), f1, "−" + sub("F", "1"), ORANGE, (-14, -8))
    force(sc, P2, (-j1[0], -j1[1]), f2, "−" + sub("F", "2"), ORANGE, (-30, 6))
    sc.vec(P2, add(P2, (-(i1[0] * f1 + j1[0] * f2), -(i1[1] * f1 + j1[1] * f2))), "−F", ORANGE, 3.6, name_off=(-8, 20), size=18, head=13)
    sc.vec(P2, add(P2, d(-90 - gam), 1.4), None, "PINK", 3.4, head=13)
    sc.label(add(P2, d(-90 - gam), 1.4), "mg", "PINK", "start", 18, weight="700", dx=10, dy=14)
    # legend
    sc.note((-4.2, -4.1), "F1: push of the motor, along the slot", "TEXT", "start", 13)
    sc.note((-4.2, -4.5), "F2: push of the slot walls, normal to the slot", "TEXT", "start", 13)
    sc.note((P2[0] + 0.4, P2[1] + 0.9), "particle alone", "TEXT", "start", 13)
    sc.note((-2.9, 3.7), "cylinder", "TEXT", "start", 13)
    # bases
    b0 = (-4.2, 3.0)
    unit(sc, b0, 0, 0.9, I0, "EDGE", off=(14, 6))
    unit(sc, b0, 90, 0.9, J0, "EDGE", off=(0, -10))
    return sc
