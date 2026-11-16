"""Problem RB-09: rectangle ABCD (b = sqrt3 a) with a spring at A and the corner C sliding on a horizontal guide."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb06 import rlabel, rotation_view2
from figures.mech import S, Scene, bold, dot1

S3 = math.sqrt(3.0)
B_ = S3                       # b / a


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _rect(G, th):
    """Vertices A, B, C, D (a = 1, b = sqrt3) and the body axes i_B, j_B of the plate turned by th degrees."""
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    iB, jB = (c, s), (-s, c)
    A = add(add(G, iB, -B_ / 2), jB, -0.5)
    B = add(add(G, iB, -B_ / 2), jB, 0.5)
    C = add(add(G, iB, B_ / 2), jB, 0.5)
    D = add(add(G, iB, B_ / 2), jB, -0.5)
    return A, B, C, D, iB, jB


def _mid(p, q, k=0.5):
    return (p[0] + k * (q[0] - p[0]), p[1] + k * (q[1] - p[1]))


@figure("rb09-rotation",
        "Rotation of the rectangle body axes by the angle theta about the axis normal to the plane.",
        r"Body basis of the rectangle, turned by $\theta$ about $\mathbf k_1$ (⊙). The axis $\mathbf j_B$ leans to "
        r"negative $\mathbf i_1$, which gives the minus sign of $[{}_0R_B]$.")
def rotation():
    return rotation_view2(640, 500, (260, 350), 140, 60.0, _ax("i", "1"), _ax("j", "1"), _ax("i", "B"), _ax("j", "B"),
                          _ax("k", "1") + " (⊙) at G", ("θ", ""), out_off=(-16, 28), L=1.0, arc_r=0.22, cy=0.62,
                          side="left", lab_r=0.46, jlab=(163, 0.30))


@figure("rb09-diagonal",
        "Rectangle with the right triangle that shows the half diagonal from G to C of length a at the angle pi/6 to "
        "the long side.",
        r"The half diagonal $GC$ has length $a$ and makes the angle $\pi/6$ with $\mathbf i_B$, so its angle from the "
        r"horizontal is $\beta = \theta + \pi/6$; $A$ is at the opposite end of the same diagonal.")
def diagonal():
    sc = Scene(760, 620, (380, 310), 225)
    th = 30.0
    G = (0.0, 0.0)
    A, B, C, D, iB, jB = _rect(G, th)
    F = add(G, iB, B_ / 2)
    triangle(sc, [G, F, C], "GREEN", 0.18)
    sc.poly([A, B, C, D], "HEAD", 1.6, close=True)
    sc.line((-0.2, 0.0), (1.12, 0.0), "EDGE", 1.1, "5 4")
    sc.line(A, C, "ACC", 2.2)
    sc.vec(G, C, None, "ACC", 3.0, head=12)
    sc.vec(G, A, None, "ACC", 3.0, head=12)
    sc.vec(G, add(G, iB, 0.30), _ax("i", "B"), "BLUE", 2.8, name_off=(16, 2), size=17, head=11)
    sc.vec(G, add(G, jB, 0.30), _ax("j", "B"), "BLUE", 2.8, name_off=(-14, -2), size=17, head=11)
    right_angle(sc, F, 180 + th, 90 + th, 0.05)
    # labels of the legs and of the half diagonals, written along their lines
    rlabel(sc, add(G, iB, 0.62), "b/2 = √3 a/2", "TEXT", th, -12, 15)
    rlabel(sc, _mid(F, C), "a/2", "TEXT", th + 90 - 180, 12, 15)
    rlabel(sc, add(G, d(60), 0.52), S(bold("r"), "G", "C") + "   |GC| = a", "ACC", 60, 13, 16, weight="700")
    rlabel(sc, add(G, d(60), -0.52), S(bold("r"), "G", "A") + " = −" + S(bold("r"), "G", "C"), "ACC", 60, -14, 16,
           weight="700")
    # angles at G: theta (horizontal to i_B), gamma (i_B to GC), beta (horizontal to GC)
    sc.arc(G, 0.20, 0, th, "GREEN", 1.6, head=True)
    sc.label(add(G, d(th / 2), 0.20), "θ", "GREEN", "middle", 16, dx=24, dy=8)
    sc.arc(G, 0.38, th, th + 30, "GREEN", 1.6, head=True)
    sc.label(add(G, d(th + 15), 0.38), "γ", "GREEN", "middle", 16, dx=4, dy=-8)
    sc.arc(G, 0.80, 0, th + 30, "GREEN", 1.7, head=True)
    sc.label(add(G, d(0), 0.80), "β = θ + π/6", "GREEN", "middle", 16, dx=8, dy=26)
    sc.note(add(G, d(th + 15), 0.38), "γ = π/6", "GREEN", "start", 13, dx=40, dy=-26)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-6, dy=24)
    for p, nm, dx, dy in ((A, "A", -2, 24), (B, "B", -16, 4), (C, "C", 8, -12), (D, "D", 16, 4)):
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    return sc


@figure("rb09-plate",
        "Rectangle in its body frame with a mass element and its coordinates.",
        r"Mass element of the plate for the integrals of the moments of inertia about the axes through $G$.")
def plate():
    sc = Scene(680, 480, (340, 240), 170)
    hb, ha = B_ / 2, 0.5
    sc.poly([(-hb, -ha), (hb, -ha), (hb, ha), (-hb, ha)], "HEAD", 1.8, close=True)
    sc.vec((0, 0), (hb + 0.22, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((hb + 0.22, 0.0), _ax("x", "B"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    sc.vec((0, 0), (0.0, ha + 0.22), None, "EDGE", 1.4, head=8)
    sc.label((0.0, ha + 0.22), _ax("y", "B"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    # mass element
    px, py, e = 0.5 * hb, 0.4 * ha, 0.035
    sc.poly([(px - e, py - e), (px + e, py - e), (px + e, py + e), (px - e, py + e)], "BLUE", 1.2, fill="BLUE",
            close=True, opacity=0.5)
    sc.line((px, py - e), (px, 0.0), "BLUE", 1.1, "4 3")
    sc.line((px - e, py), (0.0, py), "BLUE", 1.1, "4 3")
    sc.label((px, 0.0), _ax("x", "B"), "BLUE", "middle", 16, weight="700", dy=22)
    sc.label((0.0, py), _ax("y", "B"), "BLUE", "end", 16, weight="700", dx=-8, dy=5)
    sc.label((px, py), "dm = dx" + S("", "B") + " dy" + S("", "B"), "BLUE", "start", 15, dx=16, dy=-14)
    # dimensions
    sc.dim((-hb, -ha - 0.20), (hb, -ha - 0.20), "b = √3 a", off=(0, 24), size=16)
    sc.dim((-hb - 0.22, -ha), (-hb - 0.22, ha), "a", off=(-14, 5), size=16)
    for p, nm, dx, dy in (((-hb, -ha), "A", -16, 8), ((hb, -ha), "D", 16, 8), ((hb, ha), "C", 16, -4),
                          ((-hb, ha), "B", -16, -4)):
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    sc.dotp((0, 0), 4.0)
    sc.label((0, 0), "G", "HEAD", "middle", 17, dx=-12, dy=20)
    return sc


@figure("rb09-fbd",
        "Free-body diagram of the rectangle with its weight, the reaction of the horizontal guide at C and the spring "
        "force at A.",
        r"Free-body diagram: weight at $G$, smooth guide reaction $N\,\mathbf j_1$ at $C$ (arm $a\cos\beta$ about $G$) "
        r"and spring force $-k\,\mathbf r_0^A$ at $A$, pointing to $O_1$.")
def fbd():
    sc = Scene(640, 540, (120, 250), 120)
    th = 60.0
    G = (1.5, 0.25)
    A, B, C, D, iB, jB = _rect(G, th)
    O1 = (0.0, 0.0)
    sc.ground((-0.7, 1.25), (3.0, 1.25), side=1)
    sc.note((3.0, 1.25), "guide, height 5a/4", "TEXT", "end", 13, dy=22)
    sc.spring(O1, A, coils=6, amp=7.0, col="EDGE", w=1.4)
    sc.poly([A, B, C, D], "HEAD", 1.8, close=True)
    sc.mass(O1, None, r=5, col="HEAD")
    sc.label(O1, S("O", "1"), "HEAD", "middle", 17, dx=-16, dy=-8)
    # forces
    sc.vec(G, (G[0], G[1] - 0.7), "mg", "PINK", 3.4, name_off=(22, 4), size=17, head=12)
    sc.vec(C, (C[0], C[1] + 0.6), "N", "PINK", 3.4, name_off=(16, 6), size=17, head=12)
    u = (-A[0], -A[1])
    n = math.hypot(*u)
    tip = add(A, u, 1.0 / n)
    sc.vec(A, tip, None, "PINK", 3.4, head=12)
    sc.label(add(A, u, 0.5 / n), "k|" + S(bold("r"), "0", "A") + "|", "PINK", "end", 17, weight="700", dx=-4, dy=28)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=18, dy=-6)
    for p, nm, dx, dy in ((A, "A", 14, 22), (B, "B", -10, -10), (C, "C", 16, 22), (D, "D", 16, 4)):
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    # positive sense of theta at G
    sc.line(G, (G[0] + 0.55, G[1]), "EDGE", 1.0, "4 3")
    sc.arc(G, 0.30, 0, th, "GREEN", 1.7, head=True)
    sc.label(add(G, d(th / 2), 0.30), "θ", "GREEN", "middle", 16, dx=16, dy=0)
    return sc


@figure("rb09-iar",
        "Initial configuration of the rectangle with side BC on the vertical axis, the velocities of A and C and the "
        "instantaneous centre I on that axis.",
        r"Instantaneous axis at $t = 0$: $I$ lies on $O_1Y_1$, the normal to the horizontal velocity of $C$, at the "
        r"height $a(\tfrac54 - \sqrt3 + u_0/v_0)$.")
def iar():
    sc = Scene(640, 500, (260, 330), 150)
    u0, v0 = 0.4, 0.5
    th = 90.0
    ya = 1.25 - B_
    G = (0.5, 1.25 - B_ / 2)
    A, B, C, D, iB, jB = _rect(G, th)
    O1 = (0.0, 0.0)
    fixed_axis(sc, O1, 0, 1.75, _ax("i", "1"), off=(14, 6))
    fixed_axis(sc, O1, 90, 1.55, _ax("j", "1"), off=(14, 4))
    sc.label(O1, S("O", "1"), "HEAD", "middle", 17, dx=-16, dy=18)
    sc.line((-0.55, 1.25), (1.5, 1.25), "EDGE", 1.2, "8 4")
    sc.note((1.5, 1.25), "guide", "TEXT", "end", 13, dy=-8)
    sc.poly([A, B, C, D], "HEAD", 1.8, close=True, fill="HEAD", opacity=0.05)
    kv = 0.8
    sc.vec(A, (A[0] + kv * u0, A[1] + kv * v0), None, "ACC", 2.8, head=11)
    sc.label((A[0] + kv * u0, A[1] + kv * v0), S(bold("v"), "0", "A"), "ACC", "start", 17, weight="700", dx=8, dy=-4)
    vcx = -0.4655
    sc.vec(C, (C[0] + kv * vcx, C[1]), None, "ACC", 2.8, head=11)
    sc.label((C[0] + kv * vcx, C[1]), S(bold("v"), "0", "C"), "ACC", "end", 17, weight="700", dx=-8, dy=-8)
    yI = ya + u0 / v0
    I = (0.0, yI)
    sc.line(A, I, "BLUE", 1.8, "6 4")
    sc.label(_mid(A, I), "AI", "BLUE", "middle", 17, weight="700", dx=6, dy=26)
    ux, uy = u0, v0
    nu = math.hypot(ux, uy)
    ai = (I[0] - A[0], I[1] - A[1])
    na = math.hypot(*ai)
    q = 0.07
    a1 = (ux / nu, uy / nu)
    a2 = (ai[0] / na, ai[1] / na)
    sc.poly([add(A, a1, q), add(add(A, a1, q), a2, q), add(A, a2, q)], "EDGE", 1.1)
    sc.mass(I, None, r=5, col="BLUE")
    sc.label(I, "I", "HEAD", "middle", 17, dx=-14, dy=-6)
    sc.arc(G, 0.20, 20, 130, "GREEN", 1.8, head=True)
    sc.label(add(G, d(75), 0.20), dot1("θ"), "GREEN", "middle", 17, weight="700", dx=6, dy=-14)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=14, dy=22)
    for p, nm, dx, dy in ((A, "A", 14, 18), (B, "B", -14, 12), (C, "C", -14, -8), (D, "D", 14, -6)):
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    return sc
