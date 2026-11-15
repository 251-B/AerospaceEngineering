"""Problem 23: particle (Topic 3), deduction figures."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

PURPLE = "#8b5cf6"          # reaction, resultant (no kit token: a fixed colour, readable on every palette)
RED = "#ef4444"             # weight
ORANGE = "#f97316"          # surface or polar basis
YELLOW = "#eab308"          # right triangles
BROWN = "#a16207"           # spring


def _pol(c, r, deg):
    a = math.radians(deg)
    return (c[0] + r * math.cos(a), c[1] + r * math.sin(a))


def _en(sub, sup=None):
    """Bold unit vector e with a subscript (and superscript)."""
    return S(bold("e"), sub, sup)


def _r0p(sup="P"):
    return bold("r") + f'<tspan baseline-shift="super" font-size="70%">{sup}</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


def _side(sc, a, b, text, col, t=0.5, off=18, sign=1, anchor="middle", size=15):
    """Label beside the segment a-b (world points), `off` pixels to the given side of its point at fraction t."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    dx, dy = bx - ax, by - ay
    n = math.hypot(dx, dy)
    nx, ny = -dy / n * sign, dx / n * sign
    p = (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
    sc.label(p, text, col, anchor, size, dx=nx * off, dy=ny * off + 5)


def _matrix(sc, x0, y0, name, rows, colw=0.62, rowh=0.36, size=16):
    """Three-row matrix drawn with its brackets; (x0, y0) is the top left corner of the bracket."""
    sc.label((x0, y0 - 1.5 * rowh), name, "HEAD", "end", 17, dx=-10, dy=5)
    h = 3 * rowh
    w = 3 * colw
    for x, s in ((x0, 1), (x0 + w, -1)):
        sc.line((x, y0), (x, y0 - h), "HEAD", 1.6)
        sc.line((x, y0), (x + s * 0.07, y0), "HEAD", 1.6)
        sc.line((x, y0 - h), (x + s * 0.07, y0 - h), "HEAD", 1.6)
    for i, row in enumerate(rows):
        for j, s in enumerate(row):
            sc.label((x0 + (j + 0.5) * colw, y0 - (i + 0.5) * rowh), s, "HEAD", "middle", size, italic=False, dy=5)


def _mname(a, b):
    return "[" + S("", a) + "R" + S("", b) + "] ="


def _pin(sc, p, r_px=9):
    """Particle seen with an axis pointing into the paper: light disk with a cross."""
    x, y = sc.P(p)
    s = r_px * 0.62
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_px}" fill="HEAD" fill-opacity="0.22" stroke="HEAD" stroke-width="1.8"/>')
    sc.c.add(f'<path d="M{x - s:.1f},{y - s:.1f} L{x + s:.1f},{y + s:.1f} M{x - s:.1f},{y + s:.1f} L{x + s:.1f},{y - s:.1f}" '
             f'stroke="HEAD" stroke-width="1.6" fill="none"/>')


def _pout(sc, p, r_px=9, col="HEAD"):
    """Particle seen with an axis pointing out of the paper: light disk with a dot."""
    x, y = sc.P(p)
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_px}" fill="{col}" fill-opacity="0.22" stroke="{col}" stroke-width="1.8"/>')
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{col}"/>')


def _spin(sc, c, r, a0, a1, name, lpos, anchor="start", col="GREEN", size=14):
    """Curved arrow around c from angle a0 to a1 (degrees; a1 > a0 counterclockwise, a1 < a0 clockwise), small label at lpos (px)."""
    sc.arc(c, r, a0, a1, col, 1.8, head=True)
    sc.label(c, name, col, anchor, size, italic=False, dx=lpos[0], dy=lpos[1])


def _rot_view(sc, th, nfix, nrot, L=2.0, u=1.4, ax=2.5, ra=0.7, rl=1.0, ang="θ", ls=15, cf=0.72):
    """View along a rotation axis (origin of the scene at world (0, 0)): fixed axes at 0 and 90 degrees (grey), rotated
    axes at th and 90 + th (blue), arcs with arrowheads, and the two right triangles of unit length u."""
    O = (0.0, 0.0)
    sg = 1 if th > 0 else -1
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))      # s carries the sign
    t1 = [O, (u * c, 0.0), (u * c, u * s)]
    t2 = [O, (0.0, u * c), (-u * s, u * c)]
    triangle(sc, t1, YELLOW, 0.24)
    triangle(sc, t2, YELLOW, 0.24)
    right_angle(sc, t1[1], 180, 90 if sg > 0 else 270, 0.12)
    right_angle(sc, t2[1], 270, 180 if sg > 0 else 0, 0.12)
    fixed_axis(sc, O, 0, ax, nfix[0], off=(16, 5))
    fixed_axis(sc, O, 90, ax, nfix[1], off=(0, -10))
    e1 = (L * c, L * s)
    e2 = (-L * s, L * c)
    sc.vec(O, e1, nrot[0], "BLUE", 2.6, name_off=(18, -6 if sg > 0 else 14), size=17, head=11)
    sc.vec(O, e2, nrot[1], "BLUE", 2.6, name_off=(-18 * sg, -8), size=17, head=11)
    sc.arc(O, ra, 0, th, "GREEN", 1.8, head=True)
    sc.arc(O, ra, 90, 90 + th, "GREEN", 1.8, head=True)
    for a0 in (0, 90):
        p = _pol(O, rl, a0 + th / 2)
        sc.label(p, ang, "GREEN", "middle", 16, dy=5)
    # triangle legs
    sc.dashed(t1[2], t1[1])
    sc.dashed(t2[2], t2[1])
    sc.label((u * c / 2, 0.0), "cos " + ang, "TEXT", "middle", ls, dy=22 if sg > 0 else -12)
    sc.label((u * c, u * s / 2), "sin " + ang, "TEXT", "start", ls, dx=10, dy=5)
    sc.label((0.0, u * c * cf), "cos " + ang, "TEXT", "start" if sg > 0 else "end", ls, dx=10 * sg, dy=5)
    sc.label((-u * s / 2, u * c), "sin " + ang, "TEXT", "middle", ls, dy=-10)
    sc.label((u * c / 2, u * s / 2), "1", "TEXT", "middle", ls, dx=-8 * sg if sg > 0 else 14, dy=-10 * sg + 4 if sg > 0 else 16)
    sc.label((-u * s / 2, u * c / 2), "1", "TEXT", "middle", ls, dx=-16 * sg, dy=-4)


def _dvec(sc, a, b, col, w=2.0, head=9):
    """Dashed arrow from a to b (world points): dashed shaft that stops at the arrowhead."""
    from figures.svgkit import arrow_head
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" stroke-dasharray="6 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


from figures.svgkit import arrow_head

L = 2.0
ER = _en("R")
ET = _en("θ")
I2 = S(bold("i"), "1")
K2 = S(bold("k"), "1")
TH = "θ"


def _pt(th):
    a = math.radians(th)
    return (L * math.sin(a), -L * math.cos(a))


@figure("p23-plane",
        "The circumference in its own plane with the angle theta from the downward vertical, the right triangle of legs L sin theta and L cos theta, and the polar basis at P.",
        r"Plane of the circumference, $\mathbf k_1$ out of the paper. $\theta$ is measured from the downward vertical, so the polar angle from $\mathbf i_1$ is $\theta - \pi/2$; the triangle (hypotenuse $L$, legs $L\sin\theta$ and $L\cos\theta$) gives $\mathbf e_R = \sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf j$.")
def plane():
    K = 86
    sc = Scene(800, 580, (250, 270), K)
    O = (0.0, 0.0)
    th = 40.0
    P = _pt(th)
    Q = (0.0, P[1])
    triangle(sc, [O, Q, P], YELLOW, 0.26)
    right_angle(sc, Q, 90, 0, 0.12)
    sc.circle(O, L, "HEAD", 2.0)
    fixed_axis(sc, O, 0, 2.7, I2, off=(16, 5))
    fixed_axis(sc, O, 90, 2.7, bold("j"), off=(0, -10))
    sc.line(O, (0.0, -2.6), "EDGE", 1.2, "5 4")
    sc.label((0.0, -2.6), "−" + bold("j") + " (θ = 0)", "TEXT", "middle", 15, dy=18)
    # position vector and legs
    sc.vec(O, (P[0] * (1 - 0.07 / L), P[1] * (1 - 0.07 / L)), None, "HEAD", 2.2, head=10)   # tip at the rim of the dot of P
    sc.dashed(Q, P)
    sc.label((0.0, P[1] / 2), "L cos θ", "TEXT", "end", 15, dx=-10, dy=5)
    sc.label((P[0] / 2, P[1]), "L sin θ", "TEXT", "middle", 15, dy=22)
    _side(sc, O, P, "L", "TEXT", 0.7, 13, sign=1, size=16)
    sc.label((0.76, -0.68), _r0p() + " = L " + ER, "HEAD", "start", 17, dy=5)
    # angles
    sc.arc(O, 0.55, -90, -50, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.82, -70), "θ", "GREEN", "middle", 16, dy=5)
    sc.arc(O, 0.7, 0, -50, "GREEN", 1.8, head=True)
    sc.label((1.0, 0.0), "θ − π/2", "GREEN", "start", 15, dx=-4, dy=-10)
    # polar basis at P
    er = (math.sin(math.radians(th)), -math.cos(math.radians(th)))
    et = (math.cos(math.radians(th)), math.sin(math.radians(th)))
    e1 = (P[0] + 0.9 * er[0], P[1] + 0.9 * er[1])
    e2 = (P[0] + 0.9 * et[0], P[1] + 0.9 * et[1])
    sc.vec(P, e1, None, ORANGE, 2.8, head=11)
    sc.label(e1, ER, ORANGE, "start", 17, weight="700", dx=8, dy=14)
    sc.vec(P, e2, None, ORANGE, 2.8, head=11)
    sc.label(e2, ET, ORANGE, "start", 17, weight="700", dx=10, dy=-4)
    sc.dotp(P, 5.0)
    sc.label(P, "P", "HEAD", "start", 17, dx=14, dy=5)
    axis_out(sc, O, None)
    sc.label(O, K2, "HEAD", "end", 17, weight="700", dx=-14, dy=22)
    sc.note((-2.6, -3.05), ER + " = sin θ " + I2 + " − cos θ " + bold("j"), "TEXT", "start", 14)
    _matrix(sc, 3.55, 2.5, _mname("1", "2"), (("sin θ", "cos θ", "0"), ("−cos θ", "sin θ", "0"), ("0", "0", "1")), colw=0.78)
    return sc


@figure("p23-rotation-j",
        "View from above of the fixed axes k, i and of the axes i_1, k_1 of the turning plane, rotated by omega t about the vertical j.",
        r"Rotation of the plane about $\mathbf j$ (out of the paper). The triangle of $\mathbf i_1$ has its opposite leg along $-\mathbf k$, the minus sign of $\mathbf i_1 = \cos\omega t\,\mathbf i - \sin\omega t\,\mathbf k$; the circumference is seen edge-on along $\mathbf i_1$.")
def rotation_j():
    K = 80
    sc = Scene(860, 600, (330, 290), K)
    O = (0.0, 0.0)
    th = 30.0
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    # trace of the circumference: thin dashed grey segment parallel to i_1, offset 0.32 units to its left so the vector and its labels stay visible
    off = (-0.32 * c, -0.32 * s)
    sc.line((2.0 * s + off[0], -2.0 * c + off[1]), (-2.0 * s + off[0], 2.0 * c + off[1]), "EDGE", 1.4, "6 4")
    _rot_view(sc, th, (bold("k"), bold("i")), (K2, I2), L=2.0, u=1.4, ang="ωt")
    sc.label((2.0 * s, -2.0 * c), "circumference (edge-on, dashed)", "TEXT", "end", 15, dx=-6, dy=36)
    axis_out(sc, O, None)
    sc.label(O, bold("j"), "HEAD", "end", 17, dx=-14, dy=-6)
    _spin(sc, O, 0.3, 200, 340, "positive about j", (-26, 46), "end")
    _matrix(sc, 3.0, -1.2, _mname("0", "1"), (("cos ωt", "0", "sin ωt"), ("0", "1", "0"), ("−sin ωt", "0", "cos ωt")), colw=0.8)
    return sc


@figure("p23-fbd",
        "Free-body diagram of the particle inside the circumference: weight with its radial and tangential parts, the inward reaction and the reaction normal to the plane.",
        r"Forces on $P$: the weight, whose components are $mg\cos\theta$ outwards and $mg\sin\theta$ against the motion, the inward reaction $-N\mathbf e_R$ of the circumference, which must stay non-negative, and the reaction $N_b\mathbf k_1$ of the turning plane.")
def fbd():
    K = 86
    sc = Scene(860, 600, (250, 290), K)
    O = (0.0, 0.0)
    th = 50.0
    P = _pt(th)
    a = math.radians(th)
    er = (math.sin(a), -math.cos(a))
    et = (math.cos(a), math.sin(a))
    add = lambda p, v, k=1.0: (p[0] + k * v[0], p[1] + k * v[1])
    sc.circle(O, L, "EDGE", 1.6)
    axis_out(sc, O, None)
    sc.label(O, K2, "HEAD", "end", 17, weight="700", dx=-14, dy=-8)
    # weight and its components
    Wt = (P[0], P[1] - 1.0)
    C1 = add(P, er, math.cos(a))
    C2 = add(P, et, -math.sin(a))
    sc.line(Wt, (C1[0] - 0.01, C1[1] - 0.02), RED, 1.0, "4 4")
    sc.line(Wt, (C2[0] + 0.02, C2[1] - 0.01), RED, 1.0, "4 4")
    _dvec(sc, P, C1, RED, 2.0, 9)
    _dvec(sc, P, C2, RED, 2.0, 9)
    sc.vec(P, Wt, None, RED, 3.0, head=12)
    sc.label(Wt, "−m g " + bold("j"), RED, "middle", 16, dy=22)
    sc.label(C1, "m g cos θ", RED, "start", 15, dx=10, dy=6)
    sc.label(C2, "m g sin θ", RED, "end", 15, dx=-4, dy=26)
    # reaction towards O
    T = add(P, er, -1.3)
    sc.vec(P, T, None, PURPLE, 3.0, head=12)
    sc.label(T, "−N " + ER + " (N ≥ 0)", PURPLE, "end", 16, dx=-10, dy=6)
    # velocity
    V = add(P, et, 1.0)
    sc.vec(P, V, None, "GREEN", 2.8, head=11)
    sc.label(V, "L θ" + '<tspan dx="-6.5" baseline-shift="52%">·</tspan>' + " " + ET, "GREEN", "start", 16, dx=10, dy=-2)
    # axial reaction
    _pout(sc, P, 9, PURPLE)
    sc.line((P[0] + 0.13, P[1] - 0.02), (2.7, P[1] - 0.02), PURPLE, 0.9, "3 3")
    sc.label((2.75, P[1] - 0.02), S("N", "b") + " " + K2 + " (normal to the plane;", PURPLE, "start", 15, dy=-4)
    sc.label((2.75, P[1] - 0.02), "zero when the circumference is fixed)", PURPLE, "start", 15, dy=16)
    sc.label(P, "P", "HEAD", "middle", 17, dx=-2, dy=-18)
    sc.note((-2.5, -3.0), "inertial frame " + S("S", "0") + ": no inertia forces", "TEXT", "start", 14)
    return sc
