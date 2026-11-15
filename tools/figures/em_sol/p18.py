"""Problem 18: particle (Topic 3), deduction figures."""
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


R2 = math.sqrt(2.0)
TH = _en("θ")
ER = _en("R")
EG = _en("g")


def _frame_meridian(sc, light=False):
    """Axis Oz, the generators of the cone in the meridian plane and the dot of P at (2, 2)."""
    O = (0.0, 0.0)
    sc.vec(O, (0.0, 3.9), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 3.9), "z", "TEXT", "middle", 16, weight="700", dx=-12, dy=4)
    col = "EDGE" if light else "HEAD"
    sc.line(O, (3.4, 3.4), col, 1.3)
    if not light:
        sc.line(O, (-3.4, 3.4), col, 1.3)


@figure("p18-meridian",
        "Meridian section of the cone through P, with the right triangle of legs R and z and the surface basis e_g, n turned 45 degrees from e_R, k.",
        r"Meridian plane of $P$, with $\mathbf e_\theta$ into the paper. The shaded triangle (hypotenuse $R\sqrt2$, legs $R$ and $z$) gives the 45-degree generator; the surface basis $\mathbf e_g$, $\mathbf n$ is $\mathbf e_R$, $\mathbf k$ turned counterclockwise by $\pi/4$, a negative rotation about $\mathbf e_\theta$.")
def meridian():
    K = 70
    sc = Scene(860, 520, (270, 430), K)
    O = (0.0, 0.0)
    F = (2.0, 0.0)
    P = (2.0, 2.0)
    triangle(sc, [O, F, P], YELLOW, 0.26)
    right_angle(sc, F, 180, 90, 0.14)
    _frame_meridian(sc)
    sc.label((3.4, 3.4), "z = R", "HEAD", "start", 15, dx=10, dy=0)
    sc.line(O, F, "HEAD", 1.3)
    sc.dashed(F, P)
    # position vector
    sc.vec(O, P, None, "HEAD", 2.2, head=10)
    sc.label((1.55, 0.78), _r0p(), "HEAD", "middle", 17, dy=5)
    # triangle labels
    sc.label((1.0, 0.0), "R", "TEXT", "middle", 16, dy=24)
    sc.label((2.0, 0.9), "z (equal to R)", "TEXT", "start", 15, dx=10, dy=5)
    _side(sc, O, P, "R√2", "TEXT", 0.5, 26, sign=-1, size=15)
    sc.arc(O, 0.75, 0, 45, "GREEN", 1.8)
    sc.label(_pol(O, 1.05, 22.5), "π/4", "GREEN", "middle", 15, dy=5)
    # fixed pair at P
    sc.vec(P, (3.0, 2.0), None, "EDGE", 2.0, head=9)
    sc.label((3.0, 2.0), ER, "TEXT", "start", 17, weight="700", dx=8, dy=5)
    sc.vec(P, (2.0, 3.0), None, "EDGE", 2.0, head=9)
    sc.label((2.0, 3.0), bold("k"), "TEXT", "middle", 17, weight="700", dx=-1, dy=-10)
    # rotated pair
    q = 1 / R2
    sc.vec(P, (2 + q, 2 + q), None, ORANGE, 2.6, head=11)
    sc.label((2 + q, 2 + q), EG, ORANGE, "start", 17, weight="700", dx=16, dy=8)
    sc.vec(P, (2 - q, 2 + q), None, ORANGE, 2.6, head=11)
    sc.label((2 - q, 2 + q), bold("n"), ORANGE, "end", 17, weight="700", dx=-8, dy=-6)
    # arcs at P
    sc.arc(P, 0.55, 0, 45, "GREEN", 1.8, head=True)
    sc.label(_pol(P, 0.85, 22.5), "π/4", "GREEN", "middle", 15, dy=5)
    sc.arc(P, 0.55, 90, 135, "GREEN", 1.8, head=True)
    sc.label(_pol(P, 0.9, 112.5), "π/4", "GREEN", "middle", 15, dy=5)
    # e_theta into the paper
    _pin(sc, P)
    sc.label(P, "P", "HEAD", "end", 17, dx=-16, dy=6)
    sc.label(P, TH, "HEAD", "start", 17, weight="700", dx=14, dy=34)
    _spin(sc, P, 0.3, -20, -140, "positive about " + TH, (24, 56), "start")
    sc.note((-3.0, -0.6), _en("θ") + " = " + bold("k") + " × " + _en("R") + ", into the paper", "TEXT", "start", 13)
    _matrix(sc, 5.3, 3.5, _mname("1", "2"), (("1/√2", "0", "−1/√2"), ("0", "1", "0"), ("1/√2", "0", "1/√2")), colw=0.7)
    return sc


@figure("p18-rotation-k",
        "View from above of the fixed axes i, j and of the cylindrical basis e_R, e_theta turned by theta about k, out of the paper.",
        r"Rotation about $\mathbf k$ (out of the paper). The triangle of $\mathbf e_\theta$ has its opposite leg along $-\mathbf i$, which is the minus sign of $-\sin\theta\,\mathbf i$; the dashed circle is the path seen from above.")
def rotation_k():
    K = 78
    sc = Scene(820, 560, (300, 300), K)
    O = (0.0, 0.0)
    th = 35.0
    Rc = 2.25
    _rot_view(sc, th, (bold("i"), bold("j")), (ER, TH), L=1.75)
    sc.circle(O, Rc, "GREEN", 1.6, "7 5")
    sc.label(_pol(O, Rc, 215), "R = a", "GREEN", "end", 16, dx=-10, dy=14)
    Pp = _pol(O, Rc, th)
    sc.line(_pol(O, 1.75, th), Pp, "BLUE", 1.2, "3 3")
    sc.dotp(Pp, 5.0)
    sc.label(Pp, "P′", "HEAD", "start", 17, dx=10, dy=-6)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-6)
    _spin(sc, O, 0.3, 200, 340, "positive about k", (0, 50), "middle")
    _matrix(sc, 2.9, -1.35, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.78)
    return sc


@figure("p18-fbd",
        "Free-body diagram of the particle on the cone: weight down, normal reaction towards the axis at 45 degrees, and their horizontal resultant.",
        r"Forces on $P$ during the circular motion: the weight $-mg\,\mathbf k$ and the reaction $N\mathbf n$ with $N = \sqrt2\,mg$. Their resultant is horizontal and points to the axis: it is the centripetal force of the circle of radius $a$.")
def fbd():
    K = 80
    sc = Scene(760, 560, (330, 440), K)
    O = (0.0, 0.0)
    P = (2.0, 2.0)
    _frame_meridian(sc, light=True)
    w = 1.2
    W = (P[0], P[1] - w)
    N = (P[0] - w, P[1] + w)
    Rs = (P[0] - w, P[1])
    # parallelogram
    sc.line((W[0] - 0.08, W[1] + 0.08), (Rs[0] + 0.08, Rs[1] - 0.08), "EDGE", 1.1, "5 4")
    sc.line((N[0], N[1] - 0.1), (Rs[0], Rs[1] + 0.1), "EDGE", 1.1, "5 4")
    sc.vec(P, W, None, RED, 3.0, head=12)
    sc.label((2.0, 1.4), "−m g " + bold("k"), RED, "start", 16, dx=10, dy=5)
    sc.vec(P, N, None, PURPLE, 3.0, head=12)
    sc.label(N, "N " + bold("n"), PURPLE, "end", 17, dx=-10, dy=0)
    sc.line(P, (Rs[0] + 0.1, Rs[1]), PURPLE, 2.6, "7 4")
    from figures.svgkit import arrow_head
    arrow_head(sc.c, sc.P(P), sc.P(Rs), PURPLE, 11)
    sc.line((-0.12, 2.0), (Rs[0] - 0.12, 2.0), PURPLE, 1.0, "2 3")
    sc.label((-0.2, 2.0), "resultant −m g " + ER + " (centripetal)", PURPLE, "end", 15, dy=5)
    _pin(sc, P)
    sc.label(P, "P", "HEAD", "start", 17, dx=14, dy=-8)
    sc.label(P, TH, "HEAD", "start", 16, weight="700", dx=14, dy=22)
    sc.note((-3.4, -0.7), "inertial frame " + S("S", "0") + ": no inertia forces; smooth cone: reaction along n only", "TEXT", "start", 13)
    return sc
