"""Problem RB-08: equilateral triangle with a spring at A, G sliding on a vertical guide."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb06 import rotation_view2
from figures.mech import S, Scene, bold, dot1

S3 = math.sqrt(3.0)
DASHDOT = "12 3 2 3"


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _tri(G, th, a=1.0):
    """Vertices A, B, C of the triangle with centre G turned by th degrees (A at a/sqrt3 along j_B from G)."""
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    iB, jB = (c, s), (-s, c)
    A = add(G, jB, a / S3)
    B = add(add(G, iB, -a / 2), jB, -a / (2 * S3))
    C = add(add(G, iB, a / 2), jB, -a / (2 * S3))
    return A, B, C, iB, jB


@figure("rb08-rotation",
        "Rotation of the triangle body axes by the angle theta about the axis normal to the plane.",
        r"Body basis of the triangle, turned by $\theta$ about $\mathbf k$ (⊙). The axis $\mathbf j_B$ leans to negative "
        r"$\mathbf i$, which gives the minus sign of $[{}_0R_B]$.")
def rotation():
    return rotation_view2(620, 500, (230, 340), 160, 35.0, _ax("i"), _ax("j"), _ax("i", "B"), _ax("j", "B"),
                          _ax("k") + " (⊙) at G", ("θ", ""), out_off=(-16, 28), arc_r=0.40, cy=0.62)


def _outline(sc, A, B, C, w=1.8):
    sc.poly([A, B, C], "HEAD", w, close=True)


@figure("rb08-body-frame",
        "Equilateral triangle in its body frame with the right triangle used to compute the height and the position "
        "of the centre of mass.",
        r"The right triangle $MCA$ gives the height $h = \sqrt3 a/2$; $G$ is at one third of it above $BC$, so "
        r"$GA = a/\sqrt3$.")
def body_frame():
    sc = Scene(640, 520, (330, 440), 230)
    h = S3 / 2
    A, B, C, M, G = (0.0, h), (-0.5, 0.0), (0.5, 0.0), (0.0, 0.0), (0.0, h / 3)
    triangle(sc, [M, C, A], "GREEN", 0.18)
    _outline(sc, A, B, C, 2.2)
    sc.vec(M, (0.78, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((0.78, 0.0), _ax("x", "1"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    sc.vec(M, (0.0, 1.0), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 1.0), _ax("y", "1"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    right_angle(sc, M, 0, 90, 0.06)
    sc.vec(G, (0.3, h / 3), _ax("i", "B"), "BLUE", 2.8, name_off=(16, -2), size=17, head=11)
    sc.vec(G, (0.0, h / 3 + 0.28), _ax("j", "B"), "BLUE", 2.8, name_off=(-16, -2), size=17, head=11)
    for p, nm, dx, dy in ((A, "A", 16, -4), (B, "B", -16, 8), (C, "C", 16, 8), (M, "M", -14, 24)):
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=-8)
    sc.dotp(M, 3.5)
    # legs and hypotenuse of the right triangle MCA
    sc.label((0.25, 0.0), "a/2", "TEXT", "middle", 16, dy=26)
    sc.label((0.25, h / 2), "a", "TEXT", "start", 16, dx=16, dy=-4)
    # dimensions to the left, outside the triangle, with dotted extension lines
    xo, xh = -0.62, -0.86
    for y0, y1, nm in ((0.0, h / 3, "√3 a/6"), (h / 3, h, "√3 a/3 = a/√3")):
        sc.dim((xo, y0), (xo, y1), "", gap=0.0)
        sc.label((xo, (y0 + y1) / 2), nm, "TEXT", "end", 15, dx=-8, dy=5)
    sc.dim((xh, 0.0), (xh, h), "")
    sc.label((xh, h / 2), "h = √3 a/2", "TEXT", "end", 15, dx=-8, dy=5)
    for yy, x1 in ((0.0, -0.5), (h / 3, -0.0), (h, 0.0)):
        sc.line((xh - 0.03, yy), (x1 - 0.02 if yy == 0.0 else (-0.5 * (1 - yy / h) - 0.02), yy), "EDGE", 0.8, "2 4")
    return sc


@figure("rb08-geometry",
        "The triangle in the vertical plane with the right triangle that gives the components of the vector from G to A.",
        r"Position of $A$: the segment $GA$ of length $a/\sqrt3$ makes the angle $\theta$ with the vertical; its "
        r"horizontal leg (opposite) points to negative $\mathbf i$ and its vertical leg (adjacent) to $\mathbf j$.")
def geometry():
    sc = Scene(800, 640, (80, 100), 250)
    th = 35.0
    G = (2.0, -1.2)
    A, B, C, iB, jB = _tri(G, th)
    fixed_axis(sc, (0, 0), 0, 2.75, _ax("i"), off=(16, 6))
    fixed_axis(sc, (0, 0), 90, 0.30, _ax("j"), off=(14, 4))
    axis_out(sc, (0, 0), None, "HEAD")
    sc.label((0, 0), _ax("k") + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=24)
    sc.label((0, 0), "O", "HEAD", "start", 17, dx=12, dy=24)
    sc.line((2.0, 0.0), (2.0, -1.78), "EDGE", 1.2, DASHDOT)
    sc.label((2.0, 0.0), "x = 2a", "TEXT", "middle", 15, italic=False, dx=0, dy=-8)
    _outline(sc, A, B, C, 1.5)
    foot = (2.0, A[1])
    triangle(sc, [G, foot, A], "ACC", 0.24)
    sc.dashed(G, foot)
    sc.dashed(foot, A)
    right_angle(sc, foot, 270, 180, 0.07)
    sc.line((0.0, 0.0), A, "EDGE", 1.2, "6 4")
    sc.label(add((0, 0), A, 0.45), S(bold("r"), "0", "A"), "TEXT", "middle", 16, weight="700", dx=-6, dy=-14)
    sc.vec(G, A, None, "ACC", 2.8, head=11)
    sc.label(A, S(bold("r"), "G", "A"), "ACC", "end", 17, weight="700", dx=-12, dy=34)
    sc.label(((G[0] + A[0]) / 2, (G[1] + A[1]) / 2), "a/√3", "TEXT", "end", 14, dx=-6, dy=4)
    sc.label((2.0, A[1] + 0.8 * (G[1] - A[1])), "(a/√3) cos θ", "TEXT", "start", 14, dx=10, dy=5)
    sc.label(((2.0 + A[0]) / 2, A[1]), "(a/√3) sin θ", "TEXT", "middle", 14, dy=-12)
    sc.arc(G, 0.30, 90, 90 + th, "GREEN", 1.8, head=True)
    sc.label(add(G, d(90 + th / 2), 0.30), "θ", "GREEN", "middle", 17, dx=-12, dy=-10)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=14, dy=22)
    for p, nm, dx, dy in ((A, "A", -2, -14), (B, "B", -14, 6), (C, "C", 14, 8)):
        if nm != "A":
            sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    sc.label(A, "A", "HEAD", "middle", 17, dx=-14, dy=14)
    return sc


@figure("rb08-strip",
        "Horizontal strip of the triangle used to integrate the centre of mass and the moments of inertia.",
        r"Mass element of the triangle: a horizontal strip at height $y_1$ with half width "
        r"$w = \tfrac a2(1 - y_1/h)$, obtained from similar triangles.")
def strip():
    sc = Scene(680, 540, (340, 450), 230)
    h = S3 / 2
    y1, dy1 = 0.35, 0.05
    w = 0.5 * (1 - y1 / h)
    A, B, C, M, G = (0.0, h), (-0.5, 0.0), (0.5, 0.0), (0.0, 0.0), (0.0, h / 3)
    triangle(sc, [(-w, y1), (w, y1), (w, y1 + dy1), (-w, y1 + dy1)], "BLUE", 0.55)
    _outline(sc, A, B, C, 2.2)
    sc.vec(M, (0.0, 1.02), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 1.02), _ax("y", "1"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    sc.vec(M, (0.72, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((0.72, 0.0), _ax("x", "1"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    # similar triangles: the dashed segments w (at y1) and a/2 (at the base), and the heights
    sc.line((0.0, y1), (w, y1), "HEAD", 1.2, "5 4")
    sc.label((w / 2, y1), "w", "TEXT", "middle", 16, dy=22)
    sc.line((0.0, 0.0), (0.5, 0.0), "HEAD", 1.2, "5 4")
    sc.label((0.25, 0.0), "a/2", "TEXT", "middle", 16, dy=26)
    sc.dashed((w, y1), (w, 0.0))
    xo, xh = -0.72, -0.72
    sc.dim((xo, 0.0), (xo, y1), "")
    sc.label((xo, y1 / 2), "y₁", "TEXT", "end", 16, dx=-8, dy=5)
    sc.dim((xo, y1), (xo, h), "")
    sc.label((xo, (y1 + h) / 2), "h − y₁", "TEXT", "end", 16, dx=-8, dy=5)
    for yy in (0.0, y1, h):
        sc.line((xo - 0.03, yy), (-(0.5 * (1 - yy / h)) - 0.02, yy), "EDGE", 0.8, "2 4")
    sc.label((w + 0.02, y1 + dy1), "dy₁", "BLUE", "start", 16, dx=26, dy=-8)
    sc.line((w + 0.03, y1 + dy1 / 2), (w + 0.1, y1 + dy1 / 2), "BLUE", 1.0)
    for p, nm, dx, dy in ((A, "A", 16, -4), (B, "B", -16, 8), (C, "C", 16, 8)):
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=14, dy=5)
    return sc


@figure("rb08-fbd",
        "Free-body diagram of the triangle with the weight, the guide reaction and the spring force.",
        r"Free-body diagram: the weight and the guide reaction act at $G$ (no moment about $G$); the spring force "
        r"$-k\,\mathbf r_0^A$ acts at $A$ and points to $O$.")
def fbd():
    sc = Scene(720, 560, (110, 90), 105)
    th = 45.0
    G = (2.0, -2.0)
    A, B, C, iB, jB = _tri(G, th)
    O = (0.0, 0.0)
    sc.spring(O, A, coils=7, amp=7.0, col="EDGE", w=1.4)
    sc.line((2.0, 0.3), (2.0, -2.9), "EDGE", 1.2, DASHDOT)
    _outline(sc, A, B, C, 1.8)
    sc.mass(O, None, r=5, col="HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-14, dy=-10)
    # forces
    sc.vec(G, (2.0, -2.0 - 0.9), "mg", "PINK", 3.4, name_off=(-18, 6), size=17, head=12)
    sc.vec(G, (2.0 + 0.9, -2.0), "R", "PINK", 3.4, name_off=(4, 20), size=17, head=12)
    n = math.sqrt(2.0) / 2
    tip = add(A, (-n, n), 1.25)
    sc.vec(A, tip, None, "PINK", 3.4, head=12)
    sc.label(tip, "k|" + S(bold("r"), "0", "A") + "|", "PINK", "start", 17, weight="700", dx=14, dy=-6)
    # guide label, G, vertices
    sc.note((2.0, 0.3), "guide", "TEXT", "middle", 13, dy=-6)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=-8)
    sc.label(A, "A", "HEAD", "middle", 17, dx=14, dy=-4)
    sc.label(B, "B", "HEAD", "middle", 17, dx=-14, dy=12)
    sc.label(C, "C", "HEAD", "middle", 17, dx=16, dy=12)
    # positive sense of theta
    sc.arc(G, 0.24, 0, th, "GREEN", 1.6, head=True)
    sc.label(add(G, d(th / 2), 0.24), "θ", "GREEN", "middle", 16, dx=14, dy=-2)
    return sc


@figure("rb08-iar",
        "Initial configuration of the triangle with the velocities of A and G and the instantaneous centre of rotation I.",
        r"Instantaneous axis at $t = 0$: normal to the plane through $I$, on the horizontal through $G$, at the "
        r"distance $a v_0/(\sqrt3 u_0)$ to the right of $G$.")
def iar():
    sc = Scene(700, 380, (60, 300), 150)
    u0, v0 = 0.5, 0.6
    A, B, C, iB, jB = _tri((2.0, 0.289), 0.0)
    G = (2.0, 0.289)
    fixed_axis(sc, (0, 0), 0, 3.6, _ax("i"), off=(14, 6))
    fixed_axis(sc, (0, 0), 90, 1.35, _ax("j"), off=(12, 4))
    sc.label((0, 0), "O", "HEAD", "middle", 17, dx=-14, dy=20)
    _outline(sc, A, B, C, 1.8)
    kv = 0.6
    sc.vec(A, (A[0] + kv * u0, A[1] + kv * v0), None, "ACC", 2.8, head=11)
    sc.label((A[0] + kv * u0, A[1] + kv * v0), S(bold("v"), "0", "A"), "ACC", "start", 17, weight="700", dx=8, dy=-4)
    sc.vec(G, (G[0], G[1] + kv * v0), None, "ACC", 2.8, head=11)
    sc.label((G[0], G[1] + kv * v0 * 0.5), S(bold("v"), "0", "G"), "ACC", "start", 17, weight="700", dx=10, dy=6)
    xi = 2.0 + 0.6 / (S3 * 0.5)
    I = (xi, G[1])
    sc.line(G, I, "BLUE", 1.8, "6 4")
    sc.label((G[0] + 0.8 * (xi - G[0]), G[1]), "GI", "BLUE", "middle", 17, weight="700", dy=-10)
    sc.spin(G, 0.17, 270, 180, dot1("θ"), name_r=0.30)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=14, dy=18)
    sc.mass(I, None, r=5, col="BLUE")
    sc.label(I, "I", "HEAD", "middle", 17, dx=14, dy=-12)
    for p, nm, dx, dy in ((A, "A", -14, -4), (B, "B", -14, 8), (C, "C", 14, 20)):
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    return sc
