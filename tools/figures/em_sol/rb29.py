"""Problem RB-29: disk-bar train (disk pinned at O, bar pinned at C on the rim and sliding over the knob K).

Figures: disk basis and bar basis turned by theta and phi about k0, the right triangle C - corner - K that relates theta and
phi, and the exploded view of the disk and the bar.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold, dot1

ORANGE = "ACC"
I0, J0, K0 = S(bold("i"), "0"), S(bold("j"), "0"), S(bold("k"), "0")
I1, J1 = S(bold("i"), "1"), S(bold("j"), "1")
I2, J2 = S(bold("i"), "2"), S(bold("j"), "2")
R, H, LB = 3.0, 3.45, 6.5
THETA, PHI = 20.0, 49.0


def sub(t):
    return '<tspan baseline-shift="sub" font-size="70%">' + t + '</tspan>'


def band(sc, a, b, w=0.3):
    """Thick light-grey band (the bar with its groove) between a and b."""
    u = (b[0] - a[0], b[1] - a[1])
    n = math.hypot(*u)
    nx, ny = -u[1] / n * w / 2, u[0] / n * w / 2
    sc.poly([(a[0] + nx, a[1] + ny), (b[0] + nx, b[1] + ny), (b[0] - nx, b[1] - ny), (a[0] - nx, a[1] - ny)], "HEAD", 1.6,
            fill="EDGE", close=True, opacity=0.35)


# ------------------------------------------------------------------------------------------------ rb29-bases
@figure("rb29-bases",
        "The disk basis i2, j2 turned by theta and the bar basis i1, j1 turned by phi, both about the axis k0 out of the "
        "wall.",
        r"Rotations about $\mathbf k_0$ (⊙): $\mathbf i_2$ along $OC$ at the angle $\theta$; $\mathbf i_1 = \cos\varphi\,"
        r"\mathbf i_0 + \sin\varphi\,\mathbf j_0$ and $\mathbf j_1 = -\sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0$ "
        r"along the bar. The senses of both angles are readings of the statement figure.")
def bases():
    sc = Scene(820, 690, (300, 400), 80)
    O = (0.0, 0.0)
    th, ph = THETA, PHI
    ct, st = math.cos(math.radians(th)), math.sin(math.radians(th))
    cp, sp = math.cos(math.radians(ph)), math.sin(math.radians(ph))
    C = (R * ct, R * st)
    # disk
    sc.poly(circle_pts(O, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.14)
    fixed_axis(sc, O, 0, 4.9, I0, off=(14, 6))
    fixed_axis(sc, O, 90, 4.0, J0, off=(14, 4))
    sc.line(O, C, "EDGE", 1.6)
    # triangle at O for i2: adjacent R cos(theta) along i0, opposite R sin(theta) along j0
    f = (C[0], 0.0)
    triangle(sc, [O, f, C], ORANGE, 0.20)
    sc.dashed(f, C)
    right_angle(sc, f, 180, 90, 0.12)
    sc.label((f[0] / 2, 0.0), "R cos θ", "TEXT", "middle", 15, dy=22)
    sc.label((f[0], C[1] / 2), "R sin θ", "TEXT", "end", 15, dx=-10, dy=5)
    sc.arc(O, 1.4, 0, th, "GREEN", 1.7, head=True)
    sc.label(add(O, d(th / 2), 1.4), "θ", "GREEN", "middle", 17, dx=14, dy=-6)
    # disk basis at C
    unit(sc, C, th, 0.8, I2, "BLUE", off=(18, 8))
    unit(sc, C, th + 90, 0.8, J2, "BLUE", off=(-6, -12))
    # bar basis at C: dashed horizontal and vertical copies of i0, j0, triangles of i1 and j1
    Lu = 2.6
    sc.dashed(C, add(C, (1.0, 0.0), 3.0))
    sc.dashed(C, add(C, (0.0, 1.0), 3.0))
    f1, t1 = add(C, (1.0, 0.0), Lu * cp), add(C, d(ph), Lu)
    triangle(sc, [C, f1, t1], ORANGE, 0.20)
    sc.dashed(f1, t1)
    right_angle(sc, f1, 180, 90, 0.09)
    f2, t2 = add(C, (0.0, 1.0), Lu * cp), add(add(C, (0.0, 1.0), Lu * cp), (1.0, 0.0), -Lu * sp)
    triangle(sc, [C, f2, t2], ORANGE, 0.20)
    sc.dashed(f2, t2)
    right_angle(sc, f2, 270, 0, 0.09)
    sc.label(add(f2, (1.0, 0.0), -Lu * sp / 2), "−sin φ", "TEXT", "middle", 15, dy=-10)
    sc.label(add(f1, (0.0, 1.0), Lu * sp / 2), "sin φ", "TEXT", "start", 15, dx=8, dy=5)
    unit(sc, C, ph, Lu, I1, ORANGE, off=(14, -8))
    unit(sc, C, ph + 90, Lu, J1, ORANGE, off=(-12, -10))
    sc.arc(C, 1.3, 0, ph, "GREEN", 1.7, head=True)
    sc.label(add(C, d(ph * 0.6), 1.3), "φ", "GREEN", "middle", 17, dx=14, dy=8)
    sc.arc(C, 1.3, 90, 90 + ph, "GREEN", 1.7, head=True)
    sc.label(add(C, d(90 + ph * 0.55), 1.3), "φ", "GREEN", "middle", 17, dx=-4, dy=-8)
    for p, nm, off in ((C, "C", (16, 24)),):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 18, dx=off[0], dy=off[1])
    # rates
    sc.arc(O, 0.45, 200.0, 310.0, "GREEN", 1.8, head=True)
    sc.label(add(O, d(255.0), 0.45), dot1("θ") + " " + K0, "GREEN", "middle", 16, weight="700", dy=30, dx=-6)
    sc.arc(C, 0.5, -70.0, -5.0, "GREEN", 1.8, head=True)
    sc.label(add(C, d(-38.0), 0.5), dot1("φ") + " " + K0, "GREEN", "start", 16, weight="700", dx=10, dy=18)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O", "HEAD", "middle", 18, dx=-16, dy=22)
    sc.label(O, K0 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-18, dy=-14)
    return sc


# ------------------------------------------------------------------------------------------------ rb29-knob-triangle
@figure("rb29-knob-triangle",
        "The bar through the knob K with the right triangle of legs R cos theta and h - R sin theta and hypotenuse s that "
        "gives the relation between theta and phi.",
        r"$K$ on the line of the bar: $\tan\varphi = R\cos\theta/(h - R\sin\theta)$, with hypotenuse "
        r"$s = \sqrt{R^2 + h^2 - 2Rh\sin\theta}$ from $C$ to $K$.")
def knob_triangle():
    sc = Scene(860, 840, (330, 560), 78)
    O = (0.0, 0.0)
    th = THETA
    ct, st = math.cos(math.radians(th)), math.sin(math.radians(th))
    C = (R * ct, R * st)
    Kp = (0.0, H)
    s = math.hypot(C[0] - Kp[0], C[1] - Kp[1])
    phi = math.degrees(math.atan2(C[0], Kp[1] - C[1]))          # from the vertical to the bar
    ua = d(90.0 + phi)                                          # j1: along the bar from C towards A
    ia = d(phi)                                                 # i1: normal to the bar
    A = add(C, ua, LB)
    G = add(C, ua, LB / 2)
    corner = (0.0, C[1])
    # disk outline and fixed axes
    sc.poly(circle_pts(O, R), "EDGE", 1.6, close=True)
    fixed_axis(sc, O, 0, 4.1, I0, off=(14, 6))
    fixed_axis(sc, O, 90, 6.0, J0, off=(14, 4))
    # the bar (a thick band) and its points
    band(sc, add(C, ua, -0.15), add(A, ua, 0.15))
    # right triangle C - corner - K
    triangle(sc, [C, corner, Kp], ORANGE, 0.22)
    sc.dashed(C, corner)
    right_angle(sc, corner, 0, 90, 0.12)
    sc.label((C[0] / 2, C[1]), "R cos θ", "TEXT", "middle", 15, dy=22)
    sc.label((0.0, (C[1] + H) / 2), "h − R sin θ", "TEXT", "end", 15, dx=-10, dy=4)
    sc.label(add(((C[0] + Kp[0]) / 2, (C[1] + Kp[1]) / 2), ia, -0.45), "s", "TEXT", "middle", 17, dy=5)
    sc.label((C[0] / 2, C[1] / 2), "R", "TEXT", "start", 16, dx=4, dy=16)
    # projections of C on the axes (dashed) with their dimensions
    sc.dashed(C, (C[0], -0.05))
    sc.dim((0.0, -0.45), (C[0], -0.45), "R cos θ", off=(0, 20))
    sc.dashed((0.0, 0.0), (0.0, -0.55))
    sc.dashed((C[0], -0.05), (C[0], -0.55))
    sc.dim((-0.55, 0.0), (-0.55, C[1]), "R sin θ", off=(-30, 6))
    sc.dashed((0.0, C[1]), (-0.65, C[1]))
    sc.dashed((0.0, 0.0), (-0.65, 0.0))
    sc.line(O, C, "EDGE", 1.3, "5 4")
    # height h of the knob
    sc.dim((-1.3, 0.0), (-1.3, H), "h", off=(-14, 4))
    sc.dashed((0.0, H), (-1.4, H))
    sc.dashed((-0.65, 0.0), (-1.4, 0.0))
    # angle phi at K (between the vertical leg and the hypotenuse) and at C (between the horizontal and i1)
    kc = math.degrees(math.atan2(C[1] - Kp[1], C[0] - Kp[0]))   # direction K -> C
    sc.arc(Kp, 0.75, -90.0, kc, "GREEN", 1.7, head=True)
    sc.label(add(Kp, d((-90.0 + kc) / 2), 1.2), "φ", "GREEN", "middle", 17, dx=0, dy=5)
    sc.dashed(C, add(C, (1.0, 0.0), 1.3))
    sc.dashed(C, add(C, ia, 1.3))
    sc.arc(C, 0.8, 0.0, phi, "GREEN", 1.7, head=True)
    sc.label(add(C, d(phi / 2), 0.8), "φ", "GREEN", "middle", 17, dx=16, dy=0)
    # unit vectors at K
    unit(sc, Kp, phi, 1.1, I1, ORANGE, off=(12, 14))
    unit(sc, Kp, 90.0 + phi, 1.1, J1, ORANGE, off=(-12, -10))
    # points
    sc.mass(Kp, None, r=6.5, col="HEAD")
    sc.label(Kp, "K", "HEAD", "middle", 18, dx=-18, dy=26)
    sc.mass(C, None, r=4.5, col="BLUE")
    sc.label(C, "C", "HEAD", "middle", 18, dx=18, dy=22)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 18, dx=22, dy=-4)
    sc.mass(A, None, r=4.5, col="BLUE")
    sc.label(A, "A", "HEAD", "middle", 18, dx=-14, dy=-12)
    # length L of the bar, parallel to it on the +i1 side
    off = 1.5
    sc.dim(add(C, ia, off), add(A, ia, off), "L", off=(16, -8))
    sc.dashed(C, add(C, ia, off + 0.1))
    sc.dashed(A, add(A, ia, off + 0.1))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O", "HEAD", "middle", 18, dx=14, dy=24)
    sc.label(O, K0 + " (⊙)", "HEAD", "start", 16, weight="700", dx=-52, dy=44)
    return sc


# ------------------------------------------------------------------------------------------------ rb29-exploded
@figure("rb29-exploded",
        "Exploded view of the disk and the bar with the pin pair at C, the pin force at O, the knob force normal to the "
        "groove, the pull on A and the weights.",
        r"Exploded view: the pin $C$ acts on the bar with $\mathbf R_C$ and on the disk with $-\mathbf R_C$; the frictionless "
        r"knob pushes the bar along $\mathbf i_1$; $\mathbf F_A$ pulls $A$ horizontally towards $Oy_0$.")
def exploded():
    sc = Scene(820, 880, (420, 630), 62)
    O = (0.0, 0.0)
    th = THETA
    ct, st = math.cos(math.radians(th)), math.sin(math.radians(th))
    C = (R * ct, R * st)
    Kp0 = (0.0, H)
    s = math.hypot(C[0] - Kp0[0], C[1] - Kp0[1])
    phi = math.degrees(math.atan2(C[0], Kp0[1] - C[1]))
    ua, ia = d(90.0 + phi), d(phi)
    Cb = add(C, ua, 5.0)                       # the bar pulled away along j1
    Kb, Gb, Ab = add(Cb, ua, s), add(Cb, ua, LB / 2), add(Cb, ua, LB)
    # ---- disk alone
    sc.poly(circle_pts(O, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.12)
    sc.note((-0.4, -3.65), "DISK", "HEAD", "start", 15)
    sc.mass(O, None, r=4.5, col="BLUE")
    sc.label(O, "O", "HEAD", "middle", 18, dx=-14, dy=22)
    sc.mass(C, None, r=4.5, col="BLUE")
    sc.label(C, "C", "HEAD", "middle", 18, dx=18, dy=-12)
    kb = (-4.4, -3.0)
    fixed_axis(sc, kb, 0, 1.0, I0, off=(12, 6))
    fixed_axis(sc, kb, 90, 1.0, J0, off=(12, -2))
    axis_out(sc, kb, None, "HEAD")
    sc.label(kb, K0 + " (⊙)", "HEAD", "start", 16, weight="700", dx=-24, dy=30)
    sz = 0.95
    # pin force at O
    sc.vec(O, (sz, 0.0), None, "GREEN", 2.0, head=10)
    sc.vec((sz, 0.0), (sz, sz), None, "GREEN", 2.0, head=10)
    sc.vec(O, (sz, sz), None, "GREEN", 3.2, head=12)
    sc.label((sz / 2, 0.0), S("R", "Ox"), "GREEN", "middle", 15, weight="700", dy=18)
    sc.label((sz, sz / 2), S("R", "Oy"), "GREEN", "start", 15, weight="700", dx=8, dy=5)
    sc.label((sz, sz), S("R", "O"), "GREEN", "start", 17, weight="700", dx=-30, dy=-12)
    sc.vec(O, (0.0, -1.5), "mg", "PINK", 3.0, name_off=(24, 6), size=17, head=12)
    # reaction of the bar on the disk at C: -X along -i0, then -Y along -j0
    a1 = (C[0] - 1.1, C[1])
    a2 = (a1[0], a1[1] - 1.1)
    sc.vec(C, a1, None, ORANGE, 2.0, head=10)
    sc.vec(a1, a2, None, ORANGE, 2.0, head=10)
    sc.vec(C, a2, None, ORANGE, 3.2, head=12)
    sc.label(((C[0] + a1[0]) / 2, C[1]), "−X", ORANGE, "middle", 15, weight="700", dy=-10)
    sc.label((a1[0], (a1[1] + a2[1]) / 2), "−Y", ORANGE, "start", 15, weight="700", dx=8, dy=5)
    sc.label(a2, "−" + S("R", "C"), ORANGE, "start", 17, weight="700", dx=10, dy=14)
    # ---- bar alone
    band(sc, add(Cb, ua, -0.15), add(Ab, ua, 0.15))
    sc.note(add(add(Cb, ua, 1.5), ia, 0.9), "BAR", "HEAD", "start", 15)
    sc.mass(Cb, None, r=4.5, col="BLUE")
    sc.label(Cb, "C", "HEAD", "middle", 18, dx=-4, dy=24)
    sc.mass(Gb, None, r=4.5, col="BLUE")
    sc.label(Gb, "G", "HEAD", "middle", 18, dx=18, dy=22)
    sc.mass(Ab, None, r=4.5, col="BLUE")
    sc.label(Ab, "A", "HEAD", "middle", 18, dx=-4, dy=-14)
    # knob: black dot on the bar and its short hatched support on the -i1 side
    sc.mass(Kb, None, r=6, col="HEAD")
    sc.label(Kb, "K", "HEAD", "middle", 18, dx=-30, dy=2)
    sup = add(Kb, ia, -0.8)
    sc.line(Kb, sup, "HEAD", 2.0)
    n = d(phi + 90)
    sc.line(add(sup, n, -0.45), add(sup, n, 0.45), "HEAD", 2.4)
    for k in range(7):
        q = add(sup, n, -0.45 + 0.15 * k)
        sc.line(q, add(add(q, ia, -0.18), n, -0.12), "EDGE", 1.0)
    # weight of the bar
    sc.vec(Gb, add(Gb, (0.0, -1.0), 1.5), "2mg", "PINK", 3.0, name_off=(30, 6), size=17, head=12)
    # pin force on the bar at C: X along i0, then Y along j0
    b1 = (Cb[0] + 1.5, Cb[1])
    b2 = (b1[0], b1[1] + 1.5)
    sc.vec(Cb, b1, None, ORANGE, 2.0, head=10)
    sc.vec(b1, b2, None, ORANGE, 2.0, head=10)
    sc.vec(Cb, b2, None, ORANGE, 3.2, head=12)
    sc.label(((Cb[0] + b1[0]) / 2, Cb[1]), "X", ORANGE, "middle", 15, weight="700", dy=18)
    sc.label((b1[0], (b1[1] + b2[1]) / 2), "Y", ORANGE, "start", 15, weight="700", dx=8, dy=5)
    sc.label(b2, S("R", "C"), ORANGE, "start", 17, weight="700", dx=8, dy=-6)
    # knob force along i1
    tip = add(Kb, ia, 1.7)
    sc.vec(Kb, tip, None, "GREEN", 3.2, head=12)
    sc.label(tip, S("N", "K") + " " + I1, "GREEN", "start", 17, weight="700", dx=8, dy=0)
    sc.note(tip, "normal to the groove", "TEXT", "start", 13, dx=8, dy=18)
    # pull on A (horizontal, towards the axis Oy0)
    sc.vec(Ab, add(Ab, (1.0, 0.0), 1.8), None, "GREEN", 3.2, head=12)
    sc.label(add(Ab, (1.0, 0.0), 1.8), S("F", "A") + " = −k " + S("x", "A") + " " + I0, "GREEN", "start", 16, weight="700",
             dx=8, dy=-12)
    # axis Oy0 as a thin dashed vertical line through O
    sc.line((0.0, 3.4), (0.0, 9.4), "EDGE", 1.1, "9 5")
    sc.label((0.0, 9.4), "O" + S("y", "0"), "TEXT", "middle", 15, dy=-8, dx=18)
    # arms along the bar from G, parallel on the -i1 side
    for p, q, nm, o2 in ((Gb, Cb, "−L/2", 1.2), (Gb, Ab, "L/2", 1.2), (Gb, Kb, "s − L/2", 2.0)):
        pa, qa = add(p, ia, -o2), add(q, ia, -o2)
        sc.dim(pa, qa, nm, off=(-34, -4) if nm != "−L/2" else (34, 6))
        sc.dashed(p, add(p, ia, -o2 - 0.1))
        sc.dashed(q, add(q, ia, -o2 - 0.1))
    # action - reaction link between the two pin points
    sc.dashed(C, Cb)
    sc.note((1.3, 3.3), "action – reaction pair at C", "TEXT", "start", 13)
    # small orange basis at G
    unit(sc, Gb, phi, 0.9, I1, ORANGE, off=(14, 8))
    unit(sc, Gb, 90.0 + phi, 0.9, J1, ORANGE, off=(-14, -8))
    return sc
