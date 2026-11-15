"""Problem 29: particle (Topic 3), deduction figures."""
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

RC = 1.8
ER = _en("R")
ET = _en("θ")
I1 = S(bold("i"), "1")
K1 = S(bold("k"), "1")
J1 = S(bold("j"), "1")


def _pinc(sc, p, col, r_px=9):
    """Axis into the paper drawn at p in colour col (circle with a cross)."""
    x, y = sc.P(p)
    s = r_px * 0.62
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_px}" fill="{col}" fill-opacity="0.18" stroke="{col}" stroke-width="1.8"/>')
    sc.c.add(f'<path d="M{x - s:.1f},{y - s:.1f} L{x + s:.1f},{y + s:.1f} M{x - s:.1f},{y + s:.1f} L{x + s:.1f},{y - s:.1f}" '
             f'stroke="{col}" stroke-width="1.6" fill="none"/>')


@figure("p29-rotation-j",
        "Side view of the tilted cylinder with the vertical axes i_1, k_1 and the axes i, k of the cylinder turned clockwise by alpha about j_1, into the paper.",
        r"Rotation about $\mathbf j_1$ (into the paper): a positive angle is clockwise in this view. The axis $\mathbf k$ leans towards $\mathbf i_1$ and $\mathbf i$ dips below the horizontal; the leg of $\mathbf i$ along $-\mathbf k_1$ is the minus sign of $\mathbf i = \cos\alpha\,\mathbf i_1 - \sin\alpha\,\mathbf k_1$.")
def rotation_j():
    K = 78
    sc = Scene(820, 560, (330, 300), K)
    O = (0.0, 0.0)
    al = 25.0
    c, s = math.cos(math.radians(al)), math.sin(math.radians(al))
    kd = (s, c)                       # axis of the cylinder
    nd = (-c, s)                      # normal to the axis, in the plane of the paper
    for sg in (1, -1):
        sc.line((-2.0 * kd[0] + sg * 1.3 * nd[0], -2.0 * kd[1] + sg * 1.3 * nd[1]),
                (2.4 * kd[0] + sg * 1.3 * nd[0], 2.4 * kd[1] + sg * 1.3 * nd[1]), "EDGE", 1.0)
    _rot_view(sc, -al, (I1, K1), (bold("i"), bold("k")), L=2.4, u=1.5, ax=2.6, ra=0.8, rl=1.15, ang="α")
    _pin(sc, O)
    sc.label(O, J1 + " = " + bold("j"), "HEAD", "end", 17, dx=-14, dy=-12)
    _spin(sc, O, 0.34, 250, 160, "positive about " + J1, (-12, 44), "end")
    sc.gravity((-3.4, 2.9), 0.8, "g")
    sc.note((-3.4, -2.55), J1 + " = " + K1 + " × " + I1 + ", into the paper", "TEXT", "start", 13)
    _matrix(sc, 3.2, 2.6, _mname("1", "2"), (("cos α", "0", "sin α"), ("0", "1", "0"), ("−sin α", "0", "cos α")), colw=0.78)
    return sc


@figure("p29-cross-section",
        "Cross-section of the cylinder seen along its axis, with the angle theta, the cylindrical basis at P and the part of gravity that acts in the section.",
        r"Cross-section, $\mathbf k$ out of the paper. Gravity has the component $g\sin\alpha$ along $\mathbf i$ in this plane, so $\theta = 0$ is the lowest generator; the triangle of $\mathbf e_\theta$ (opposite leg along $-\mathbf i$) gives its minus sign.")
def cross_section():
    K = 80
    sc = Scene(900, 600, (520, 300), K)
    O = (0.0, 0.0)
    th = 50.0
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    P = (RC * c, RC * s)
    Q = (P[0], 0.0)
    triangle(sc, [O, Q, P], YELLOW, 0.26)
    right_angle(sc, Q, 90, 180, 0.12)
    sc.circle(O, RC, "HEAD", 2.0)
    fixed_axis(sc, O, 0, 2.7, bold("i"), off=(14, 5))
    fixed_axis(sc, O, 90, 2.5, bold("j"), off=(0, -10))
    sc.dashed(Q, P)
    sc.vec(O, P, None, "HEAD", 2.2, head=10)
    sc.label((P[0] / 2, 0.0), "R cos θ", "TEXT", "middle", 15, dy=22)
    sc.line((P[0] + 0.03, P[1] / 2), (2.05, P[1] / 2), "EDGE", 0.9)
    sc.label((2.05, P[1] / 2), "R sin θ", "TEXT", "start", 15, dx=6, dy=5)
    sc.label((P[0] * 0.55, P[1] * 0.55), "R", "TEXT", "middle", 15, dx=-12, dy=-6)
    sc.arc(O, 0.55, 0, th, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.85, th / 2 + 3), "θ", "GREEN", "middle", 16, dy=5)
    # basis at P
    sc.vec(P, (P[0] + 0.8 * c, P[1] + 0.8 * s), None, ORANGE, 2.8, head=11)
    sc.label((P[0] + 0.8 * c, P[1] + 0.8 * s), ER, ORANGE, "start", 17, weight="700", dx=8, dy=-4)
    sc.vec(P, (P[0] - 0.8 * s, P[1] + 0.8 * c), None, ORANGE, 2.8, head=11)
    sc.label((P[0] - 0.8 * s, P[1] + 0.8 * c), ET, ORANGE, "end", 17, weight="700", dx=-8, dy=-6)
    sc.vec(P, (P[0] + 0.5, P[1]), None, "EDGE", 1.3, head=7)
    sc.vec(P, (P[0], P[1] + 0.5), None, "EDGE", 1.3, head=7)
    sc.arc(P, 0.34, 0, th, "GREEN", 1.6, head=True)
    sc.label(_pol(P, 0.58, th / 2 - 4), "θ", "GREEN", "middle", 15, dy=5)
    sc.arc(P, 0.28, 90, 90 + th, "GREEN", 1.6, head=True)
    sc.label(_pol(P, 0.5, 90 + th / 2 + 5), "θ", "GREEN", "middle", 15, dy=5)
    sc.dotp(P, 5.0)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=22)
    # gravity in the section
    sc.vec((0.0, -0.6), (1.0, -0.6), None, RED, 3.0, head=12)
    sc.label((0.0, -0.6), "g sin α", RED, "start", 15, dy=24)
    sc.label((0.0, -0.6), "(part of gravity", RED, "start", 14, dy=44)
    sc.label((0.0, -0.6), "in the section)", RED, "start", 14, dy=62)
    # lowest generator and start point
    sc.line((RC, -0.12), (RC, 0.12), "HEAD", 2.0)
    sc.label((RC, 0.0), "lowest generator (θ = 0)", "HEAD", "start", 15, dx=14, dy=28)
    x, y = sc.P((0.0, RC))
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="none" stroke="HEAD" stroke-width="1.8"/>')
    sc.label((0.0, RC), "start", "HEAD", "end", 16, dx=-12, dy=-6)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-8)
    _matrix(sc, -5.4, 2.7, _mname("2", "3"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.78)
    return sc


@figure("p29-fbd",
        "Free-body diagram in the cross-section: the in-plane part of the weight with its radial and tangential components, the radial reaction, and the axial part of the weight into the paper.",
        r"Forces on the particle: the weight, split into $mg\sin\alpha$ along $\mathbf i$ in the section and $-mg\cos\alpha\,\mathbf k$ along the axis, and the reaction $N\mathbf e_R$ of the smooth cylinder.")
def fbd():
    K = 80
    sc = Scene(900, 600, (330, 330), K)
    O = (0.0, 0.0)
    th = 50.0
    a = math.radians(th)
    c, s = math.cos(a), math.sin(a)
    P = (RC * c, RC * s)
    er = (c, s)
    et = (-s, c)
    add = lambda p, v, k=1.0: (p[0] + k * v[0], p[1] + k * v[1])
    sc.circle(O, RC, "EDGE", 1.6)
    sc.dotp(O, 3.0)
    sc.label(O, "O", "TEXT", "start", 16, dx=8, dy=20)
    Wt = add(P, (1.0, 0.0))
    C1 = add(P, er, c)
    C2 = add(P, et, -s)
    sc.line((Wt[0] - 0.03, Wt[1] + 0.04), (C1[0] + 0.03, C1[1] - 0.04), RED, 1.0, "4 4")
    sc.line((Wt[0] - 0.03, Wt[1] - 0.04), (C2[0] + 0.03, C2[1] + 0.04), RED, 1.0, "4 4")
    _dvec(sc, P, C1, RED, 2.0, 9)
    _dvec(sc, P, C2, RED, 2.0, 9)
    sc.vec(P, Wt, None, RED, 3.0, head=12)
    sc.label(Wt, "m g sin α " + bold("i"), RED, "start", 16, dx=10, dy=5)
    sc.label(C1, "m g sin α cos θ", RED, "start", 15, dx=8, dy=-10)
    sc.label(C2, "m g sin α sin θ", RED, "start", 15, dx=10, dy=18)
    # reaction
    T = add(P, er, -1.4)
    sc.vec(P, T, None, PURPLE, 3.0, head=12)
    sc.label(T, "N " + ER + " (drawn for N < 0)", PURPLE, "end", 16, dx=-10, dy=-8)
    # axial part of the weight, into the paper
    _pinc(sc, P, RED)
    sc.line((P[0] - 0.1, P[1] + 0.1), (0.85, 2.3), RED, 0.9, "3 3")
    sc.label((0.85, 2.3), "−m g cos α " + bold("k"), RED, "end", 16, dx=-4, dy=-14)
    sc.label((0.85, 2.3), "(axial part of the weight)", RED, "end", 15, dx=-4, dy=6)
    sc.label(P, "P", "HEAD", "end", 17, dx=-14, dy=10)
    sc.note((-3.9, -2.55), "inertial frame " + S("S", "1") + ": no inertia forces; smooth cylinder: reaction along " + ER + " only", "TEXT", "start", 13)
    return sc
