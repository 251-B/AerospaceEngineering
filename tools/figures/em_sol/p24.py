"""Problem 24: particle (Topic 3), deduction figures."""
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

A_ = 2.0                    # radius a
BETA = 1.4
ER = _en("R")
ET = _en("θ")


def _square(sc, p, s=6.0):
    x, y = sc.P(p)
    sc.c.add(f'<rect x="{x - s:.1f}" y="{y - s:.1f}" width="{2 * s:.1f}" height="{2 * s:.1f}" fill="HEAD"/>')


@figure("p24-plane",
        "The circumference with the particle at the angle theta, the anchor A on the vertical axis, the spring AP with its two legs and the polar basis at P.",
        r"Geometry of the spring. The triangle of $OP$ (legs $a\cos\theta$, $a\sin\theta$) and the legs of $\overrightarrow{AP}$ ($a\cos\theta$ and $a(\sin\theta - \beta)$, drawn downwards) give $|\overrightarrow{AP}|^2 = a^2(1 + \beta^2 - 2\beta\sin\theta)$.")
def plane():
    K = 88
    sc = Scene(820, 580, (260, 330), K)
    O = (0.0, 0.0)
    th = 30.0
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    P = (A_ * c, A_ * s)
    A = (0.0, BETA * A_)
    Q = (P[0], 0.0)
    triangle(sc, [O, Q, P], YELLOW, 0.26)
    right_angle(sc, Q, 90, 180, 0.12)
    sc.circle(O, A_, "HEAD", 2.0)
    fixed_axis(sc, O, 0, 3.3, "x", off=(14, 5))
    fixed_axis(sc, O, 90, 3.4, "y", off=(0, -10))
    # legs of the triangle
    sc.dashed(Q, P)
    sc.label((P[0] / 2, 0.0), "a cos θ", "TEXT", "middle", 15, dy=22)
    sc.line((P[0] + 0.03, P[1] * 0.4), (A_ + 0.12, P[1] * 0.4), "EDGE", 0.9)     # leader, so the label clears the circle
    sc.label((A_ + 0.12, P[1] * 0.4), "a sin θ", "TEXT", "start", 15, dx=4, dy=5)
    # position vector
    sc.vec(O, P, None, "HEAD", 2.2, head=10)
    sc.label((0.2, 0.9), _r0p() + " = a " + ER, "HEAD", "start", 17, dy=5)
    sc.label((P[0] * 0.6, P[1] * 0.6), "a", "TEXT", "middle", 15, dx=10, dy=12)
    sc.arc(O, 0.6, 0, th, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.95, th / 2), "θ", "GREEN", "middle", 16, dy=5)
    # anchor and spring
    _square(sc, A)
    sc.label(A, "A (0, β a)", "HEAD", "end", 16, dx=-12, dy=-4)
    sc.spring(A, P, coils=5, amp=7.0, col=BROWN, lead=0.32, w=1.8)   # long straight ends: the coils stay clear of the basis at P
    arrow_head(sc.c, sc.P((P[0] - 0.12 * (P[0] - A[0]), P[1] - 0.12 * (P[1] - A[1]))), sc.P(P), BROWN, 12)
    sc.label((P[0] / 2, (A[1] + P[1]) / 2), "AP", BROWN, "middle", 17, weight="700", dx=22, dy=-14)
    Ah = (P[0], A[1])
    sc.line(A, Ah, BROWN, 1.2, "5 4")
    sc.line(Ah, (P[0], P[1] + 0.1), BROWN, 1.2, "5 4")
    sc.label((P[0] / 2, A[1]), "a cos θ", BROWN, "middle", 15, dy=-9)
    sc.label((P[0], (A[1] + P[1]) / 2), "a(β − sin θ)", BROWN, "start", 15, dx=10, dy=5)
    # basis at P
    sc.vec(P, (P[0] + 0.9 * c, P[1] + 0.9 * s), None, "BLUE", 2.6, head=11)
    sc.label((P[0] + 0.9 * c, P[1] + 0.9 * s), ER, "BLUE", "start", 17, weight="700", dx=8, dy=6)
    sc.vec(P, (P[0] - 0.7 * s, P[1] + 0.7 * c), None, "BLUE", 2.6, head=11)
    sc.label((P[0] - 0.7 * s, P[1] + 0.7 * c), ET, "BLUE", "middle", 17, weight="700", dx=2, dy=-12)
    sc.vec(P, (P[0] + 0.55, P[1]), None, "EDGE", 1.3, head=7)
    sc.vec(P, (P[0], P[1] + 0.55), None, "EDGE", 1.3, head=7)
    sc.arc(P, 0.38, 0, th, "GREEN", 1.6, head=True)
    sc.label(_pol(P, 0.62, th / 2 - 2), "θ", "GREEN", "middle", 15, dy=5)
    sc.arc(P, 0.30, 90, 90 + th, "GREEN", 1.6, head=True)
    sc.label(_pol(P, 0.52, 90 + th / 2 + 6), "θ", "GREEN", "middle", 15, dy=5)
    sc.dotp(P, 5.0)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=22)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-6)
    sc.gravity((4.1, 2.9), 0.8, "g")
    _matrix(sc, 3.4, -0.5, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.78)
    return sc


@figure("p24-fbd",
        "Free-body diagram of the particle on the circumference with weight, spring force towards A, the reaction and the extra force along the velocity.",
        r"Forces on $P$: weight, spring $-k\,\overrightarrow{AP}$, the reaction $N_R\mathbf e_R + N_k\mathbf k$ of the circumference and, in parts (e) and (f), the force $2m\mu\,\mathbf v_0^P$ along the velocity.")
def fbd():
    K = 90
    sc = Scene(860, 560, (280, 330), K)
    O = (0.0, 0.0)
    th = 30.0
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    P = (A_ * c, A_ * s)
    A = (0.0, BETA * A_)
    er = (c, s)
    et = (-s, c)
    u = (A[0] - P[0], A[1] - P[1])
    n = math.hypot(*u)
    u = (u[0] / n, u[1] / n)
    add = lambda p, v, k=1.0: (p[0] + k * v[0], p[1] + k * v[1])
    sc.circle(O, A_, "EDGE", 1.6)
    sc.dotp(O, 3.0)
    sc.label(O, "O", "TEXT", "end", 16, dx=-10, dy=20)
    _square(sc, A)
    sc.label(A, "A", "HEAD", "start", 16, dx=12, dy=-6)
    # weight
    Wt = (P[0], P[1] - 1.0)
    sc.vec(P, Wt, None, RED, 3.0, head=12)
    sc.label((P[0], P[1] - 0.5), "−m g " + bold("j"), RED, "start", 16, dx=14, dy=5)
    # spring force towards A
    Sp = add(P, u, 1.5)
    sc.vec(P, Sp, None, BROWN, 3.0, head=12)
    sc.label(Sp, "−k AP", BROWN, "end", 17, weight="700", dx=-6, dy=-8)
    # reaction inward
    Rn = add(P, er, -0.8)
    sc.vec(P, Rn, None, PURPLE, 3.0, head=12)
    sc.label(Rn, S("N", "R") + " " + ER, PURPLE, "end", 17, dx=-8, dy=16)
    sc.label(Rn, "(drawn for " + S("N", "R") + " < 0)", PURPLE, "end", 15, dx=-8, dy=36)
    # extra force and velocity
    Fx = add(P, et, 0.7)
    sc.line(P, add(P, et, 0.7 - 0.07), "GREEN", 2.8, "6 4")
    arrow_head(sc.c, sc.P(add(P, et, 0.6)), sc.P(Fx), "GREEN", 11)
    Pv = add(P, er, 0.16)
    Vt = add(Pv, et, 0.9)
    sc.vec(Pv, Vt, None, "GREEN", 1.6, head=9)
    sc.label(Vt, "a θ" + '<tspan dx="-6.5" baseline-shift="52%">·</tspan>' + " " + ET, "GREEN", "start", 16, dx=10, dy=-4)
    sc.line((Fx[0] - 0.02, Fx[1] + 0.06), (1.2, 2.14), "GREEN", 0.9)        # leader up and to the left, clear of the velocity
    sc.label((1.2, 2.14), "2 m μ v (parts e, f)", "GREEN", "start", 16, dx=-2, dy=-6)
    # axial reaction (zero)
    _pout(sc, P, 9, PURPLE)
    sc.line((P[0] + 0.13, P[1] - 0.06), (2.1, 0.85), PURPLE, 0.9, "3 3")
    sc.label((2.1, 0.85), S("N", "k") + " " + bold("k") + " (zero)", PURPLE, "start", 16, dx=4, dy=5)
    sc.note((-2.5, -2.5), "inertial frame: no inertia forces", "TEXT", "start", 14)
    return sc
