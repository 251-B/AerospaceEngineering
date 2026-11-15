"""Problem 17: particle M attracted to O with force -m k^2 r and under gravity (great-circle motion)."""
import math

from figures.em_solutions import _dir, axis_in, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

PURPLE = "#8b5cf6"          # resultant (no kit token: a fixed colour, readable on every palette)
RED = "#ef4444"             # weight
ORANGE = "#f97316"          # path
YELLOW = "#eab308"          # right triangles

R3 = math.sqrt(3.0)


def _r0m():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">M</tspan><tspan baseline-shift="sub" font-size="70%" dx="-8">0</tspan>'


def _side(sc, a, b, text, col, t=0.5, off=18, sign=1, anchor="middle", size=15):
    """Label beside the segment a-b (world points), `off` pixels to the given side of its point at fraction t."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    dx, dy = bx - ax, by - ay
    n = math.hypot(dx, dy)
    nx, ny = -dy / n * sign, dx / n * sign
    p = (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
    sc.label(p, text, col, anchor, size, dx=nx * off, dy=ny * off + 5)


def _matrix(sc, x0, y0, rows, colw=0.62, rowh=0.36):
    """[0R1] = three-row matrix drawn with its brackets; (x0, y0) is the top left corner of the bracket."""
    sc.label((x0, y0 - 1.5 * rowh), "[" + S("", "0") + "R" + S("", "1") + "] =", "HEAD", "end", 17, dx=-10, dy=5)
    h = 3 * rowh
    w = 3 * colw
    for x, s in ((x0, 1), (x0 + w, -1)):
        sc.line((x, y0), (x, y0 - h), "HEAD", 1.6)
        sc.line((x, y0), (x + s * 0.07, y0), "HEAD", 1.6)
        sc.line((x, y0 - h), (x + s * 0.07, y0 - h), "HEAD", 1.6)
    for i, row in enumerate(rows):
        for j, s in enumerate(row):
            sc.label((x0 + (j + 0.5) * colw, y0 - (i + 0.5) * rowh), s, "HEAD", "middle", 16, italic=False, dy=5)


@figure("p17-rotation-j",
        "View along j (into the paper) of the fixed axes i, k and of the basis e1, e3 of the plane of the path, turned "
        "30 degrees counterclockwise.",
        r"Basis of the plane of the path. With $\mathbf j$ into the paper a positive rotation about $\mathbf j$ is "
        r"clockwise, so $\mathbf e_1$, turned counterclockwise from $\mathbf i$, corresponds to the angle $-\pi/6$; the "
        r"leg of $\mathbf e_3$ along $-\mathbf i$ gives the minus sign of its first component.")
def rotation_j():
    K = 80
    sc = Scene(760, 400, (190, 250), K)
    O = (0.0, 0.0)
    a = 30.0
    u = 1.8
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    # shaded right triangles at unit scale
    triangle(sc, [O, (u * c, 0.0), (u * c, u * s)], YELLOW, 0.22)
    triangle(sc, [O, (0.0, u * c), (-u * s, u * c)], YELLOW, 0.22)
    right_angle(sc, (u * c, 0.0), 180, 90, 0.12)
    right_angle(sc, (0.0, u * c), 0, 270, 0.12)
    # fixed axes (grey) and rotated axes (blue)
    fixed_axis(sc, O, 0, 2.5, bold("i"), off=(14, 5))
    fixed_axis(sc, O, 90, 2.5, bold("k"), off=(0, -10))
    e1 = (2.5 * c, 2.5 * s)
    e3 = (-2.5 * s, 2.5 * c)
    sc.vec(O, e1, S(bold("e"), "1"), "BLUE", 2.6, name_off=(18, -6), size=17, head=11)
    sc.vec(O, e3, S(bold("e"), "3"), "BLUE", 2.6, name_off=(-16, -6), size=17, head=11)
    # angle arcs
    sc.arc(O, 0.9, 0, a, "GREEN", 1.8, head=True)
    sc.label((1.28 * math.cos(math.radians(a / 2)), 1.28 * math.sin(math.radians(a / 2))), "π/6", "GREEN", "middle", 16, dy=5)
    sc.arc(O, 0.9, 90, 90 + a, "GREEN", 1.8, head=True)
    sc.label((1.35 * math.cos(math.radians(90 + a / 2)), 1.35 * math.sin(math.radians(90 + a / 2))), "π/6", "GREEN", "middle", 16, dy=5)
    # triangle legs
    sc.dashed((u * c, u * s), (u * c, 0.0))
    sc.dashed((-u * s, u * c), (0.0, u * c))
    sc.label((u * c / 2, 0.0), "cos(π/6)", "TEXT", "middle", 15, dy=22)
    sc.label((u * c, u * s / 2), "sin(π/6)", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((0.0, u * c * 0.78), "cos(π/6)", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-u * s / 2, u * c), "sin(π/6)", "TEXT", "middle", 15, dy=-10)
    sc.label((u * c / 2 - 0.10, u * s / 2 + 0.18), "1", "TEXT", "middle", 15, dx=-6, dy=-10)
    sc.label((-u * s / 2 - 0.10, u * c / 2 + 0.10), "1", "TEXT", "end", 15, dx=-8, dy=0)
    # j into the paper and the positive sense about it (clockwise)
    axis_in(sc, O, None)
    sc.label(O, bold("j"), "HEAD", "end", 17, dx=-16, dy=6)
    sc.arc(O, 0.42, -15, -150, "GREEN", 1.8, head=True)
    sc.note((0.45, -0.75), "positive sense about j (thumb into the paper)", "GREEN", "start", 13)
    # matrix
    _matrix(sc, 3.3, 2.6, (("√3/2", "0", "−1/2"), ("0", "1", "0"), ("1/2", "0", "√3/2")))
    return sc


# ------------------------------------------------------------------------------------------------ axonometric views
def _camera(az, el):
    A, E = math.radians(az), math.radians(el)

    def proj(p):
        x, y, z = p
        d = x * math.cos(A) + y * math.sin(A)           # towards the viewer, in the horizontal plane
        return (y * math.cos(A) - x * math.sin(A), z * math.cos(E) - d * math.sin(E))

    def depth(p):
        x, y, z = p
        return math.cos(E) * (x * math.cos(A) + y * math.sin(A)) + math.sin(E) * z
    return proj, depth


@figure("p17-fbd",
        "Free-body diagram of the particle M with the attraction towards O, the weight, and their resultant pointing to "
        "the centre C.",
        r"Forces on $M$: the attraction $-mk^2\mathbf r_0^M$ towards $O$ and the weight $-mg\,\mathbf k$. Their "
        r"resultant is $-mk^2\,\overrightarrow{CM}$, an attraction towards the equilibrium point $C$ below $O$.")
def fbd():
    pr, _ = _camera(25, 35)
    K = 105
    sc = Scene(760, 600, (330, 300), K)
    P = lambda x, y, z: pr((x, y, z))
    O = P(0, 0, 0)
    ax = {"i": (2.6, 0, 0), "j": (0, 2.6, 0), "k": (0, 0, 2.2)}
    sc.line(O, P(0, 0, -1.5), "EDGE", 1.2, "5 4")
    for nm, v in ax.items():
        tip = P(*v)
        sc.vec(O, tip, None, "EDGE", 1.4, head=8)
        off = {"i": (-12, 14), "j": (14, 14), "k": (0, -10)}[nm]
        sc.label(tip, bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    M3 = (1.2, 1.4, -0.6)
    M = P(*M3)
    C = P(0, 0, -1)
    # position vector
    sc.vec(O, (O[0] + 0.93 * (M[0] - O[0]), O[1] + 0.93 * (M[1] - O[1])), None, "HEAD", 2.2, head=10)
    sc.label(((O[0] + M[0]) / 2, (O[1] + M[1]) / 2), _r0m(), "HEAD", "start", 17, dx=12, dy=-6)
    # attraction: from M towards O, 1.6 units long, drawn slightly to the side of the position vector
    n = math.sqrt(sum(v * v for v in M3))
    t = 1.6 / n
    tip3 = tuple(M3[i] * (1 - t) for i in range(3))
    off = (-0.16, 0.10)
    A0 = (M[0] + off[0], M[1] + off[1])
    A1 = (P(*tip3)[0] + off[0], P(*tip3)[1] + off[1])
    sc.vec(A0, A1, None, "PINK", 2.8, head=11)
    sc.label(A1, "−m " + S("k", None, "2") + " " + _r0m(), "PINK", "end", 16, dx=-14, dy=-24)
    # weight
    W1 = P(1.2, 1.4, -1.6)
    sc.vec(M, W1, None, RED, 2.8, head=11)
    sc.label(W1, "−m g " + bold("k"), RED, "start", 16, dx=12, dy=8)
    # resultant towards C
    Ce = (M[0] + 0.92 * (C[0] - M[0]), M[1] + 0.92 * (C[1] - M[1]))
    sc.line(M, Ce, PURPLE, 2.6, "7 4")
    arrow_head(sc.c, sc.P(M), sc.P(Ce), PURPLE, 11)
    sc.label(M, "resultant −m " + S("k", None, "2") + " CM", PURPLE, "end", 16, dx=-16, dy=26)
    sc.dotp(M, 5.0)
    sc.label(M, "M", "HEAD", "start", 17, dx=12, dy=-6)
    sc.circle(C, 6.0 / K, "HEAD", 1.8, fill="none")
    sc.label(C, "C (0, 0, −g/" + S("k", None, "2") + ")", "HEAD", "end", 16, dx=-14, dy=5)
    sc.note((-3.05, -2.7), "free particle: no reaction; inertial frame: no inertia forces", "TEXT", "start", 13)
    return sc


@figure("p17-path-plane",
        "The great circle of radius 2g/k^2 centred at C below O, lying in a plane tilted 30 degrees about j, with the "
        "start point on the i axis.",
        r"Path of $M$: a great circle of the sphere of centre $C$ and radius $2g/k^2$, in the plane spanned by "
        r"$\mathbf e_1$ and $\mathbf j$, swept uniformly at the angular rate $k$. The shaded triangle gives the tilt: "
        r"its hypotenuse is $R$, its horizontal leg $\sqrt3\,g/k^2$ and its vertical leg $g/k^2$.")
def path_plane():
    pr, depth = _camera(70, 50)
    K = 105
    sc = Scene(800, 640, (390, 300), K)
    P = lambda p: pr(p)
    Cw = (0.0, 0.0, -1.0)
    e1 = (R3 / 2, 0.0, 0.5)
    e3 = (-0.5, 0.0, R3 / 2)
    j = (0.0, 1.0, 0.0)
    add = lambda *vs: tuple(sum(v[i] for v in vs) for i in range(3))
    mul = lambda k, v: tuple(k * c for c in v)
    O = P((0, 0, 0))
    C = P(Cw)
    # plane (light translucent blue parallelogram)
    h = 2.4
    corners = [add(Cw, mul(sa * h, e1), mul(sb * h, j)) for sa, sb in ((1, 1), (1, -1), (-1, -1), (-1, 1))]
    sc.poly([P(c) for c in corners], "BLUE", 0.0, fill="BLUE", close=True, opacity=0.10)
    # fixed axes
    sc.line(O, P((0, 0, -1.0)), "EDGE", 1.2, "5 4")
    for nm, v, off in (("i", (3.0, 0, 0), (-12, 16)), ("j", (0, 3.0, 0), (14, 14)), ("k", (0, 0, 3.0), (0, -10))):
        sc.vec(O, P(v), None, "EDGE", 1.4, head=8)
        sc.label(P(v), bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # circle: hidden half dashed
    dc = depth(Cw)
    pt = lambda ph: add(Cw, mul(2 * math.cos(ph), e1), mul(2 * math.sin(ph), j))
    n = 240
    for i in range(n):
        p0, p1 = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n
        front = depth(pt((p0 + p1) / 2)) >= dc
        sc.line(P(pt(p0)), P(pt(p1)), ORANGE, 2.6 if front else 1.4, None if front else "3 3")
    # triangle of the tilt in the plane Oxz
    M0 = pt(0.0)
    foot = (R3, 0.0, -1.0)
    triangle(sc, [C, P(foot), P(M0)], YELLOW, 0.30)
    sc.line(C, P(foot), "HEAD", 1.2)
    sc.line(P(foot), P(M0), "HEAD", 1.2)
    # C, e1, e3
    sc.vec(C, P(add(Cw, e1)), None, "BLUE", 2.6, head=11)
    sc.vec(C, P(add(Cw, e3)), None, "BLUE", 2.6, head=11)
    sc.label(P(add(Cw, e1)), S(bold("e"), "1"), "BLUE", "middle", 17, weight="700", dx=-2, dy=-14)
    sc.label(P(add(Cw, e3)), S(bold("e"), "3"), "BLUE", "middle", 17, weight="700", dx=-14, dy=-8)
    sc.circle(C, 5.5 / K, "HEAD", 1.8, fill="none")
    sc.label(C, "C", "HEAD", "end", 17, dx=-12, dy=-8)
    # start point and its velocity
    sc.dotp(P(M0), 5.0)
    sc.label(P(M0), "M(0)", "HEAD", "end", 16, dx=-14, dy=-4)
    sc.vec(P(M0), P(add(M0, mul(1.2, j))), None, "GREEN", 2.6, head=11)
    sc.label(P(add(M0, mul(1.2, j))), "v(0) = (2g/k) " + bold("j"), "GREEN", "end", 15, dx=-8, dy=24)
    # M at phi = 60 deg
    ph = math.pi / 3
    Mp = pt(ph)
    sc.vec(C, (C[0] + 0.94 * (P(Mp)[0] - C[0]), C[1] + 0.94 * (P(Mp)[1] - C[1])), None, "HEAD", 2.2, head=10)
    sc.dotp(P(Mp), 5.0)
    sc.label(P(Mp), "M", "HEAD", "start", 17, dx=10, dy=-8)
    tang = add(mul(-math.sin(ph), e1), mul(math.cos(ph), j))
    sc.vec(P(Mp), P(add(Mp, mul(1.3, tang))), None, "GREEN", 2.6, head=11)
    # angle arc kt inside the circle
    sc.label(P(add(Cw, mul(0.5 * math.cos(ph / 2), e1), mul(0.5 * math.sin(ph / 2), j))), "kt", "GREEN", "middle", 16, dy=5)
    sc.label(P(Mp), "CM = (2g/" + S("k", None, "2") + ")(cos kt " + S(bold("e"), "1") + " + sin kt " + bold("j") + ")", "HEAD", "end", 15, dx=-14, dy=34)
    # triangle labels
    sc.label(((C[0] + P(M0)[0]) / 2, (C[1] + P(M0)[1]) / 2), "R = 2g/" + S("k", None, "2"), "TEXT", "middle", 15, dy=-62)
    _side(sc, C, P(foot), "√3 g/" + S("k", None, "2"), "TEXT", 0.5, 18, -1, size=15)
    sc.label(((P(foot)[0] + P(M0)[0]) / 2, (P(foot)[1] + P(M0)[1]) / 2), "g/" + S("k", None, "2"), "TEXT", "end", 15, dx=-8, dy=5)
    a0 = 0.0
    sc.curve(lambda t: P(add(Cw, mul(1.0 * math.cos(t), (1, 0, 0)), mul(1.0 * math.sin(t), (0, 0, 1)))), 0.0, math.radians(30), 20, col="GREEN", w=1.6)
    sc.label(P(add(Cw, mul(1.3 * math.cos(math.radians(15)), (1, 0, 0)), mul(1.3 * math.sin(math.radians(15)), (0, 0, 1)))), "30°", "GREEN", "middle", 15, dy=5)
    sc.curve(lambda t: P(add(Cw, mul(0.8 * math.cos(t), e1), mul(0.8 * math.sin(t), j))), 0.0, ph, 40, col="GREEN", w=1.6)
    return sc
