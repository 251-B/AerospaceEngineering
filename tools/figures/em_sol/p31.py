"""Problem 31: two particles joined by a string through the vertex of a cone (meridian plane, view along k, free-body diagram)."""
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


def _rot_view(sc, th, nfix, nrot, L=2.0, u=1.4, ax=2.5, ra=0.7, rl=1.0, ang="θ", ls=15, cf=0.72, cdy=22):
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
    sc.label((u * c / 2, 0.0), "cos " + ang, "TEXT", "middle", ls, dy=cdy if sg > 0 else -12)
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

AL = 30.0
SA, CA = math.sin(math.radians(AL)), math.cos(math.radians(AL))
XI = 2.4
ER = _en("R")
ET = _en("θ")
EX = _en("ξ")
P1N = S("P", "1")
P2N = S("P", "2")
XIS = "ξ"


def _cone(sc, light=False):
    """Axis OZ (1 unit up, 3.5 down dash-dotted) and the two generators of the cone in the meridian plane."""
    O = (0.0, 0.0)
    sc.vec(O, (0.0, 1.0), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 1.0), "Z", "TEXT", "middle", 16, weight="700", dx=-1, dy=-10)
    sc.line(O, (0.0, -3.5), "EDGE", 1.3, "11 3 2 3")
    col = "EDGE" if light else "HEAD"
    for sg in (1, -1):
        sc.line(O, (sg * 3.6 * SA, -3.6 * CA), col, 1.3)
    sc.circle(O, 4.5 / sc.k, "HEAD", 1.6, fill="none")
    sc.label(O, "O", "HEAD", "end", 16, dx=-12, dy=-6)


@figure("p31-meridian",
        "Meridian section of the cone with the string from O to P_1 along a generator and to P_2 on the axis, the triangle of legs xi sin alpha and xi cos alpha, and the cone basis at P_1.",
        r"Meridian plane of $P_1$, $\mathbf e_\theta$ into the paper. The triangle (hypotenuse $\xi$, legs $\xi\cos\alpha$ along the axis and $\xi\sin\alpha$ horizontal) gives $\mathbf e_\xi = \sin\alpha\,\mathbf e_R - \cos\alpha\,\mathbf k$; the cone basis is $\mathbf e_R$, $\mathbf k$ turned clockwise by $\pi/2 - \alpha$, a positive rotation about $\mathbf e_\theta$.")
def meridian():
    K = 82
    sc = Scene(780, 560, (540, 120), K)
    O = (0.0, 0.0)
    P1 = (XI * SA, -XI * CA)
    P2 = (0.0, -1.6)
    F = (0.0, P1[1])
    triangle(sc, [O, F, P1], YELLOW, 0.26)
    right_angle(sc, F, 90, 0, 0.12)
    _cone(sc)
    # strings (thick)
    sc.line(O, P1, "HEAD", 4.0)
    sc.line(O, P2, "HEAD", 4.0)
    sc.dashed(F, P1)
    sc.label((P1[0] * 0.5, P1[1] * 0.5), XIS, "HEAD", "middle", 17, dx=18, dy=8)
    sc.label((0.0, -1.3), "l − " + XIS, "HEAD", "end", 16, dx=-12, dy=5)
    sc.label((0.0, -1.9), XIS + " cos α", "TEXT", "end", 15, dx=-12, dy=5)
    sc.label((P1[0] * 0.28, F[1]), XIS + " sin α", "TEXT", "middle", 15, dy=22)
    sc.arc(O, 0.75, -90, -60, "GREEN", 1.8)
    sc.label(_pol(O, 1.05, -75), "α", "GREEN", "middle", 16, dy=5)
    # P2
    sc.dotp(P2, 5.0)
    sc.label(P2, P2N, "HEAD", "start", 17, dx=12, dy=5)
    # fixed pair at P1
    sc.vec(P1, (P1[0] + 0.9, P1[1]), None, "EDGE", 2.0, head=9)
    sc.label((P1[0] + 0.9, P1[1]), ER, "TEXT", "start", 17, weight="700", dx=8, dy=5)
    sc.vec(P1, (P1[0], P1[1] + 0.9), None, "EDGE", 2.0, head=9)
    sc.label((P1[0], P1[1] + 0.9), bold("k"), "TEXT", "middle", 17, weight="700", dx=-1, dy=-10)
    # rotated pair (cone basis)
    ex = (SA, -CA)
    nn = (CA, SA)
    sc.vec(P1, (P1[0] + 0.9 * ex[0], P1[1] + 0.9 * ex[1]), None, ORANGE, 2.6, head=11)
    sc.label((P1[0] + 0.9 * ex[0], P1[1] + 0.9 * ex[1]), EX, ORANGE, "start", 17, weight="700", dx=8, dy=14)
    sc.vec(P1, (P1[0] + 0.9 * nn[0], P1[1] + 0.9 * nn[1]), None, ORANGE, 2.6, head=11)
    sc.label((P1[0] + 0.9 * nn[0], P1[1] + 0.9 * nn[1]), bold("n"), ORANGE, "start", 17, weight="700", dx=8, dy=-4)
    sc.arc(P1, 0.5, 0, -60, "GREEN", 1.8, head=True)
    sc.label(_pol(P1, 0.78, -22), "π/2 − α", "GREEN", "start", 15, dx=0, dy=5)
    sc.arc(P1, 0.5, 90, 30, "GREEN", 1.8, head=True)
    sc.label(_pol(P1, 0.8, 62), "π/2 − α", "GREEN", "start", 15, dx=2, dy=-2)
    _pin(sc, P1)
    sc.label(P1, P1N, "HEAD", "end", 17, dx=-36, dy=-16)          # inside the triangle, clear of the arc below
    sc.label(P1, ET, "HEAD", "middle", 17, weight="700", dx=-2, dy=34)
    _spin(sc, P1, 0.3, 235, 155, "positive", (-20, 58), "end")
    sc.label(P1, "about " + ET, "GREEN", "end", 14, italic=False, dx=-20, dy=74)
    sc.note((-6.1, -4.35), _en("θ") + " = " + bold("k") + " × " + _en("R") + ", into the paper", "TEXT", "start", 13)
    _matrix(sc, -5.0, -2.9, _mname("1", "2"), (("sin α", "0", "cos α"), ("0", "1", "0"), ("−cos α", "0", "sin α")), colw=0.78)
    return sc


@figure("p31-rotation-k",
        "View from above of the cylindrical basis turned by theta about k, with the parallel of P_1.",
        r"Rotation about $\mathbf k$ (out of the paper); $\theta$ is the azimuth of the projection of $\overrightarrow{OP_1}$, and the triangle of $\mathbf e_\theta$ (opposite leg along $-\mathbf i$) gives its minus sign.")
def rotation_k():
    K = 80
    sc = Scene(860, 560, (330, 290), K)
    O = (0.0, 0.0)
    th = 40.0
    Rc = XI * SA * 1.333333      # 1.6 drawn units
    Rc = 1.6
    _rot_view(sc, th, (bold("i"), bold("j")), (ER, ET), L=2.0, u=1.1, ra=0.55, rl=0.4, ls=13, cf=0.9, cdy=38)
    sc.circle(O, Rc, "GREEN", 1.6, "7 5")
    sc.label(_pol(O, Rc, 215), "radius " + XIS + " sin α", "GREEN", "end", 15, dx=-10, dy=22)
    Pp = _pol(O, Rc, th)
    sc.dotp(Pp, 5.0)
    sc.label(Pp, S("P", "1") + "′", "HEAD", "start", 17, dx=14, dy=16)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-6)
    _spin(sc, O, 0.3, 200, 340, "positive about k", (0, 66), "middle")
    _matrix(sc, 3.0, -1.3, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.78)
    return sc


@figure("p31-fbd",
        "Exploded free-body diagram of the two particles: weights, the string tension towards the aperture on each, the normal reaction of the cone on P_1 and the zero guide reaction on P_2.",
        r"Forces on $P_1$ and $P_2$. The string pulls each particle towards $O$ with the same tension $T$; the cone acts on $P_1$ along its normal $\mathbf n$ and the guide on $P_2$ only normal to the axis. Drawn for the circular motion, with $T = mg$.")
def fbd():
    K = 82
    sc = Scene(860, 560, (400, 110), K)
    O = (0.0, 0.0)
    P1 = (XI * SA, -XI * CA)
    P2 = (0.0, -1.6)
    add = lambda p, v, k=1.0: (p[0] + k * v[0], p[1] + k * v[1])
    ex = (SA, -CA)
    nn = (CA, SA)
    _cone(sc, light=True)
    # P1
    sc.vec(P1, add(P1, (0.0, -1.0)), None, RED, 3.0, head=12)
    sc.label(add(P1, (0.0, -0.55)), "−m g " + bold("k"), RED, "end", 16, dx=-10, dy=5)
    T1 = add(P1, ex, -1.0)
    sc.vec(P1, T1, None, "PINK", 3.0, head=12)
    sc.label(T1, "−T " + EX, "PINK", "start", 17, dx=14, dy=-2)
    N1 = add(P1, nn, 0.27)
    sc.vec(P1, N1, None, PURPLE, 3.0, head=10)
    sc.label(N1, "N " + bold("n"), PURPLE, "start", 17, dx=8, dy=-4)
    _pin(sc, P1)
    sc.label(P1, P1N, "HEAD", "end", 17, dx=-18, dy=8)
    sc.label(P1, ET, "HEAD", "end", 16, weight="700", dx=-14, dy=30)
    # P2
    sc.vec(P2, add(P2, (0.0, -1.0)), None, RED, 3.0, head=12)
    sc.label(add(P2, (0.0, -0.5)), "−m g " + bold("k"), RED, "end", 16, dx=-10, dy=5)
    sc.vec(P2, add(P2, (0.0, 1.0)), None, "PINK", 3.0, head=12)
    sc.label(add(P2, (0.0, 0.5)), "T " + bold("k"), "PINK", "end", 17, dx=-10, dy=5)
    sc.dotp(P2, 5.0)
    sc.label(P2, P2N, "HEAD", "start", 17, dx=12, dy=-8)
    sc.line((P2[0] - 0.1, P2[1]), (-1.45, P2[1]), PURPLE, 0.9, "3 3")
    sc.label((-1.45, P2[1]), S("R", "2") + " (normal to the axis) = 0", PURPLE, "end", 15, dx=-4, dy=5)
    sc.note((-4.2, -4.55), "same tension T at both ends (massless string, smooth aperture);", "TEXT", "start", 13)
    sc.note((-4.2, -4.8), "inertial frame: no inertia forces", "TEXT", "start", 13)
    return sc
