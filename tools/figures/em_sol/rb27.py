"""Problem RB-27: rectangle with weight, pulleys and string (block hanging from O by a string, weight P over C, spring to B).

Figures: string basis i1, j1 with the right triangle of the angle theta, block basis i_B, j_B turned by phi, and the
exploded view with the tension, the spring force, the guide force and the weights.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.mech import S, Scene, bold, dot1

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I1, J1 = S(I, "1"), S(J, "1")
IB, JB = S(I, "B"), S(J, "B")
THETA, PHI = 25.0, 35.0


def sub(t):
    return '<tspan baseline-shift="sub" font-size="70%">' + t + '</tspan>'


# ------------------------------------------------------------------------------------------------ rb27-string-basis
@figure("rb27-string-basis",
        "Plane of the motion with the string piece OG at the angle theta from the downward vertical, its right triangle "
        "and the string basis i1, j1.",
        r"$\mathbf i_1 = \sin\theta\,\mathbf i - \cos\theta\,\mathbf j$ along $OG$ and $\mathbf j_1 = \mathbf k\times"
        r"\mathbf i_1$; the angle from the downward vertical is the polar angle $\theta - \pi/2$. The sense of $\theta$ is "
        r"a reading of the statement figure.")
def string_basis():
    sc = Scene(900, 600, (470, 175), 150)
    O = (0.0, 0.0)
    th = THETA
    s, c = math.sin(math.radians(th)), math.cos(math.radians(th))
    Lg = 2.0                                   # 4L - xi with L = 1, xi = 2
    G = (Lg * s, -Lg * c)
    F = (0.0, -Lg * c)
    Cp, Bp = (-2.0, 0.0), (2.0, 0.0)
    P = (-2.0, -2.0)
    # axes and the dashed downward vertical (it carries the cosine leg of the triangle)
    fixed_axis(sc, O, 0, 2.7, I, off=(14, 6))
    fixed_axis(sc, O, 90, 0.9, J, off=(12, 4))
    sc.line(O, (0.0, -2.35), "EDGE", 1.2, "5 4")
    sc.label((0.0, -2.35), "−" + J, "TEXT", "middle", 16, weight="700", dx=-14, dy=14)
    # string over the pulleys: C - O (just above the axis), O - G and C - P
    sc.line((-2.0, 0.05), (0.0, 0.05), "HEAD", 3.0)
    sc.line(O, G, "HEAD", 3.0)
    sc.line(Cp, P, "HEAD", 3.0)
    # triangle with legs on -j and horizontal
    triangle(sc, [O, F, G], ORANGE, 0.20)
    sc.dashed(F, G)
    right_angle(sc, F, 90, 0, 0.1)
    sc.label((0.0, -Lg * c / 2), "(4L − ξ) cos θ", "TEXT", "end", 15, dx=-8, dy=8)
    sc.label((G[0] / 2, F[1]), "(4L − ξ) sin θ", "TEXT", "middle", 15, dx=-12, dy=24)
    # hypotenuse dimension on the right, stopped short of G
    u = (s, -c)
    n = (c, s)
    pa, qa = add(add(O, n, 0.2), u, 0.25), add(add(O, n, 0.2), u, 1.35)
    sc.dim(pa, qa, "4L − ξ", off=(36, 8))
    # arcs: theta from -j to OG (counterclockwise); theta - pi/2 from i to OG (clockwise)
    sc.arc(O, 0.9, -90.0, -90.0 + th, "GREEN", 1.7, head=True)
    sc.label(add(O, d(-90.0 + th / 2), 1.2), "θ", "GREEN", "middle", 17, dx=-10, dy=10)
    sc.arc(O, 0.55, 0.0, -90.0 + th, "GREEN", 1.7, head=True)
    sc.label(add(O, d((-90.0 + th) / 2), 0.55), "θ − π/2", "GREEN", "start", 16, dx=12, dy=18)
    # string basis at G
    unit(sc, G, -90.0 + th, 0.8, I1, "BLUE", off=(12, 16))
    unit(sc, G, th, 0.8, J1, "BLUE", off=(12, -8))
    # points and pulleys
    for p, nm, off in ((Cp, "C", (-22, -16)), (O, "O", (-22, -16))):
        sc.circle(p, 0.09, "HEAD", 1.8)
        axis_out(sc, p, None, "HEAD")
        sc.label(p, nm, "HEAD", "middle", 18, dx=off[0], dy=off[1])
    sc.mass(Bp, None, r=4.5, col="BLUE")
    sc.label(Bp, "B", "HEAD", "middle", 18, dx=0, dy=-16)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 18, dx=14, dy=24)
    sc.mass(P, None, r=5.5, col="HEAD")
    sc.label(P, "P", "HEAD", "middle", 18, dx=16, dy=6)
    sc.dim((-2.3, 0.0), (-2.3, -2.0), "ξ", off=(-14, 4))
    sc.dashed((-2.0, 0.0), (-2.4, 0.0))
    sc.dashed(P, (-2.4, -2.0))
    sc.label(O, K + " (⊙)", "HEAD", "start", 16, weight="700", dx=16, dy=-14)
    return sc


# ------------------------------------------------------------------------------------------------ rb27-block-basis
@figure("rb27-block-basis",
        "The block with its body basis i_B, j_B turned by phi from i, j and the point A on the axis x_B.",
        r"Rotation about $\mathbf k$ (⊙) by $\varphi$: $\mathbf i_B = \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j$, "
        r"$\mathbf j_B = -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j$; $A$ is at the distance $L$ from $G$ along "
        r"$\mathbf i_B$.")
def block_basis():
    sc = Scene(960, 800, (460, 440), 150)
    G = (0.0, 0.0)
    ph = PHI
    c, s = math.cos(math.radians(ph)), math.sin(math.radians(ph))
    Lb = 1.5
    ib, jb = d(ph), d(ph + 90)
    # block: width 2L along i_B, height L along j_B
    pts = [add(add(G, ib, sx * Lb), jb, sy * Lb / 2) for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    sc.poly(pts, "HEAD", 2.2, fill="EDGE", close=True, opacity=0.10)
    # fixed axes and the dashed horizontal through G
    fixed_axis(sc, G, 0, 2.5, I, off=(14, 6))
    fixed_axis(sc, G, 90, 2.1, J, off=(12, 4))
    Lu = 1.3
    # triangle of i_B: adjacent along i, opposite along j
    f1, t1 = (Lu * c, 0.0), d(ph)
    triangle(sc, [G, f1, t1], ORANGE, 0.22)
    sc.dashed(f1, t1)
    right_angle(sc, f1, 180, 90, 0.08)
    f2, t2 = (0.0, Lu * c), (-Lu * s, Lu * c)
    triangle(sc, [G, f2, t2], ORANGE, 0.22)
    sc.dashed(f2, t2)
    right_angle(sc, f2, 270, 0, 0.08)
    sc.label((f1[0] / 2, 0.0), "cos φ", "TEXT", "middle", 15, dy=22)
    sc.label((f1[0], t1[1] / 2), "sin φ", "TEXT", "start", 15, dx=8, dy=6)
    sc.label((0.0, f2[1] / 2), "cos φ", "TEXT", "start", 15, dx=8, dy=6)
    sc.label((t2[0] / 2, t2[1]), "−sin φ", "TEXT", "middle", 15, dy=-10)
    unit(sc, G, ph, Lu, IB, ORANGE, off=(14, -10))
    unit(sc, G, ph + 90, Lu, JB, ORANGE, off=(-10, -12))
    # arcs of phi
    sc.arc(G, 0.5, 0, ph, "GREEN", 1.7, head=True)
    sc.arc(G, 0.5, 90, 90 + ph, "GREEN", 1.7, head=True)
    sc.label(add(G, d(ph / 2), 0.68), "φ", "GREEN", "middle", 17, dx=0, dy=5)
    sc.label(add(G, d(90 + ph / 2), 0.68), "φ", "GREEN", "middle", 17, dx=-2, dy=5)
    # rate of phi about G, lower left
    sc.spin(G, 0.3, 190.0, 285.0, "", "GREEN")
    sc.label(add(G, d(237.0), 0.3), dot1("φ") + " " + K, "GREEN", "end", 16, weight="700", dx=-10, dy=22)
    # A and the dimension L, drawn above the line G-A
    A = add(G, ib, Lb)
    n = jb
    sc.dim(add(G, n, -0.65), add(A, n, -0.65), "L", off=(14, 28))
    sc.dashed(A, add(A, n, -0.73))
    sc.dashed(G, add(G, n, -0.73))
    sc.mass(A, None, r=4.5, col="BLUE")
    sc.label(A, "A", "HEAD", "start", 18, dx=12, dy=-8)
    axis_out(sc, G, None, "HEAD")
    sc.label(G, "G", "HEAD", "middle", 18, dx=16, dy=24)
    sc.label(G, K + " (⊙)", "HEAD", "end", 16, weight="700", dx=-16, dy=5)
    return sc


# ------------------------------------------------------------------------------------------------ rb27-exploded
@figure("rb27-exploded",
        "Exploded view of the block, the weight P and the two massless pulleys with the tension T, the spring force, the "
        "guide force and the weights.",
        r"Exploded view: the same tension $T$ pulls $G$ towards $O$ and $P$ towards $C$; the spring acts at $A$ towards "
        r"$B$; the guide force on $P$ is horizontal and turns out to be zero.")
def exploded():
    sc = Scene(1000, 660, (340, 570), 70)
    th, ph = THETA, PHI
    u1 = d(-90.0 + th)                               # i1, from O towards G
    Cc, Oo = (-2.0, 5.2), (2.2, 5.2)
    G = add(Oo, u1, 4.6)
    ib, jb = d(ph), d(ph + 90)
    Lb = 1.2
    A = add(G, ib, Lb)
    Bp = (G[0] + 3.0, G[1] + 2.2)
    P = (-2.0, 1.6)
    # ---- parts titles
    sc.note((-3.4, -1.0), "WEIGHT P", "HEAD", "start", 15)
    sc.note((0.2, 6.3), "PULLEYS (massless)", "HEAD", "start", 15)
    sc.note((G[0] - 1.7, G[1] - 2.0), "BLOCK", "HEAD", "start", 15)
    # ---- pulleys with their tensions and axle reactions
    for p, nm in ((Cc, "C"), (Oo, "O")):
        sc.circle(p, 0.13, "HEAD", 1.8, fill="EDGE", opacity=0.15)
        axis_out(sc, p, None, "HEAD")
        sc.label(p, nm, "HEAD", "middle", 18, dx=-6, dy=-24)
    # pulley C: T down (towards P), T right (towards O), axle up-left
    sc.vec(add(Cc, (0.0, -1.0), 0.18), add(Cc, (0.0, -1.0), 1.3), None, "GREEN", 3.0, head=12)
    sc.label(add(Cc, (0.0, -1.0), 1.3), "T", "GREEN", "start", 17, weight="700", dx=10, dy=0)
    sc.vec(add(Cc, (1.0, 0.0), 0.18), add(Cc, (1.0, 0.0), 1.3), None, "GREEN", 3.0, head=12)
    sc.label(add(Cc, (1.0, 0.0), 1.3), "T", "GREEN", "middle", 17, weight="700", dx=0, dy=22)
    sc.vec(add(Cc, d(135), 0.18), add(Cc, d(135), 1.5), None, "EDGE", 3.0, head=12)
    sc.label(add(Cc, d(135), 1.5), "axle", "TEXT", "end", 15, italic=False, dx=-8, dy=-4)
    # pulley O: T left (towards C), T along i1 (towards G), axle up-right
    sc.vec(add(Oo, (-1.0, 0.0), 0.18), add(Oo, (-1.0, 0.0), 1.3), None, "GREEN", 3.0, head=12)
    sc.label(add(Oo, (-1.0, 0.0), 1.3), "T", "GREEN", "middle", 17, weight="700", dx=0, dy=22)
    sc.vec(add(Oo, u1, 0.18), add(Oo, u1, 1.3), None, "GREEN", 3.0, head=12)
    sc.label(add(Oo, u1, 1.3), "T", "GREEN", "start", 17, weight="700", dx=10, dy=6)
    ax = (0.577, 0.906)
    n = math.hypot(*ax)
    sc.vec(add(Oo, ax, 0.18 / n), add(Oo, ax, 1.7 / n), None, "EDGE", 3.0, head=12)
    sc.label(add(Oo, ax, 1.7 / n), "axle", "TEXT", "start", 15, italic=False, dx=8, dy=-4)
    # string pieces between the pulleys and the bodies (dashed pair lines)
    sc.dashed(add(Cc, (0.0, -1.0), 1.3), add(P, (0.0, 1.0), 1.2))
    sc.dashed(add(Oo, u1, 1.3), add(G, u1, -1.2))
    sc.dashed(add(Cc, (1.0, 0.0), 1.3), add(Oo, (-1.0, 0.0), 1.3))
    sc.note((0.0, 5.55), "action – reaction pairs along the string", "TEXT", "middle", 13, dx=0, dy=-6)
    # ---- the weight P and its guide
    sc.line((-2.55, 0.2), (-2.55, 4.6), "HEAD", 2.4)
    for k in range(10):
        yy = 0.3 + 0.44 * k
        sc.line((-2.55, yy), (-2.8, yy - 0.12), "EDGE", 1.0)
    sc.note((-2.8, 4.75), "guide", "TEXT", "end", 13)
    sc.mass(P, None, r=7, col="BLUE")
    sc.label(P, "P", "HEAD", "middle", 18, dx=-10, dy=24)
    sc.vec(P, add(P, (0.0, 1.0), 1.2), "T " + J, "GREEN", 3.0, name_off=(26, 6), size=17, head=12)
    sc.vec(P, add(P, (0.0, -1.0), 1.2), "mg", "PINK", 3.0, name_off=(24, 6), size=17, head=12)
    sc.vec(P, add(P, (1.0, 0.0), 0.55), None, "EDGE", 2.4, head=10)
    sc.note(add(P, (1.0, 0.0), 0.55), S("N", "P") + " = 0", "TEXT", "start", 14, dx=10, dy=5)
    # ---- the block, rotated by phi
    pts = [add(add(G, ib, sx * Lb), jb, sy * Lb / 2) for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    sc.poly(pts, "HEAD", 2.2, fill="EDGE", close=True, opacity=0.10)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=24)
    sc.vec(G, add(G, (0.0, -1.0), 1.7), "2mg", "PINK", 3.0, name_off=(30, 6), size=17, head=12)
    sc.vec(G, add(G, u1, -1.2), "−T " + I1, "GREEN", 3.0, name_off=(-42, -4), size=17, head=12)
    # spring: dashed zigzag A - B and its force on the block at A
    sc.mass(A, None, r=4.5, col="BLUE")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-14, dy=-12)
    ab = math.atan2(Bp[1] - A[1], Bp[0] - A[0])
    ua, na = d(math.degrees(ab)), d(math.degrees(ab) + 90)
    lenAB = math.hypot(Bp[0] - A[0], Bp[1] - A[1])
    off = 0.5                                       # the dashed spring runs parallel to the force, on its upper side
    p0, p1 = add(add(A, ua, 0.5), na, off), add(add(A, ua, lenAB - 0.5), na, off)
    pts = [p0]
    nz = 9
    for i in range(1, nz):
        pts.append(add(add(p0, ua, (lenAB - 1.0) * i / nz), na, 0.16 * (1 if i % 2 else -1)))
    pts.append(p1)
    sc.poly(pts, "EDGE", 1.3, "4 3")
    sc.dashed(A, p0)
    sc.dashed(Bp, p1)
    sc.note(add(add(A, ua, lenAB / 2), na, off + 0.35), "spring, replaced by its force", "TEXT", "middle", 13, dx=-30, dy=-6)
    sc.vec(A, add(A, ua, 1.4), S("F", "s"), ORANGE, 3.0, name_off=(8, 20), size=17, head=12)
    sc.mass(Bp, None, r=4.5, col="HEAD")
    sc.label(Bp, "B", "HEAD", "middle", 18, dx=14, dy=-12)
    sc.ground((Bp[0] - 0.5, Bp[1] + 0.12), (Bp[0] + 0.5, Bp[1] + 0.12), 1)
    # small blue basis at G
    unit(sc, G, -90.0 + th, 0.8, I1, "BLUE", off=(12, 14))
    unit(sc, G, th, 0.8, J1, "BLUE", off=(12, -8))
    # key
    b0 = (5.8, 0.2)
    sc.vec(b0, add(b0, (1.0, 0.0), 0.9), I, "EDGE", 1.6, name_off=(12, 6), size=16, head=9)
    sc.vec(b0, add(b0, (0.0, 1.0), 0.9), J, "EDGE", 1.6, name_off=(10, -4), size=16, head=9)
    axis_out(sc, b0, None, "HEAD")
    sc.label(b0, K + " (⊙)", "HEAD", "start", 16, weight="700", dx=14, dy=34)
    return sc
