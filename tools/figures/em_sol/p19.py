"""Problem 19: particle (Topic 3), deduction figures."""
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

TH = _en("θ")
ER = _en("r")
EM = _en("m")
A = 1.5                     # drawn value of a
PHI = math.degrees(math.atan(2.0))
CP, SP = math.cos(math.radians(PHI)), math.sin(math.radians(PHI))


def _parab(sc, x0, x1, col="HEAD", w=1.8):
    sc.curve(lambda t: (t, t * t / A), x0, x1, 120, col=col, w=w)


@figure("p19-meridian",
        "Meridian section of the paraboloid with the particle, its slope triangle of legs a and 2r, and the surface basis e_m, n turned by the slope angle from e_r, k.",
        r"Meridian of the paraboloid, $\mathbf e_\theta$ into the paper. The slope triangle (legs $a$ and $2r$, hypotenuse $\sqrt{a^2 + 4r^2}$) gives $\cos\varphi$ and $\sin\varphi$ of the tangent $\mathbf e_m$; the normal $\mathbf n$ leans towards the axis, hence its component $-\sin\varphi$ on $\mathbf e_r$.")
def meridian():
    K = 110
    sc = Scene(1000, 660, (580, 560), K)
    O = (0.0, 0.0)
    P = (A, A)
    sc.vec(O, (0.0, 4.3), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 4.3), "z", "TEXT", "middle", 16, weight="700", dx=-12, dy=4)
    _parab(sc, -2.4, 2.4)
    sc.label((2.4, 3.84), "a z = r²", "HEAD", "start", 16, dx=10, dy=0)
    # slope triangle, drawn further along the tangent (clear of the basis at P): legs a and 2r at the scale 0.4
    T0 = (A + 0.5, A + 1.0)
    C = (A + 0.9, A + 1.0)
    V = (A + 0.9, A + 1.8)
    sc.line((A + 0.9 * CP, A + 0.9 * SP), T0, ORANGE, 1.0, "4 3")
    triangle(sc, [T0, C, V], YELLOW, 0.30)
    right_angle(sc, C, 180, 90, 0.10)
    # dashed legs of P
    sc.dashed((0.0, A), P)
    sc.dashed((A, 0.0), P)
    sc.label((A / 2, A), "r", "TEXT", "middle", 15, dy=-9)
    sc.label((A, 0.0), "z = r²/a", "TEXT", "start", 15, dx=10, dy=-24)
    # position vector
    sc.vec(O, P, None, "HEAD", 2.2, head=10)
    sc.label((0.78, 0.62), _r0p(), "HEAD", "middle", 17, dy=5)
    # fixed pair at P
    sc.vec(P, (A + 0.9, A), None, "EDGE", 2.0, head=9)
    sc.label((A + 0.9, A), ER, "TEXT", "start", 17, weight="700", dx=8, dy=5)
    sc.vec(P, (A, A + 0.9), None, "EDGE", 2.0, head=9)
    sc.label((A, A + 0.9), bold("k"), "TEXT", "middle", 17, weight="700", dx=-1, dy=-10)
    # rotated pair
    sc.vec(P, (A + 0.9 * CP, A + 0.9 * SP), None, ORANGE, 2.6, head=11)
    sc.label((A + 0.9 * CP, A + 0.9 * SP), EM, ORANGE, "end", 17, weight="700", dx=-10, dy=2)
    sc.vec(P, (A - 0.9 * SP, A + 0.9 * CP), None, ORANGE, 2.6, head=11)
    sc.label((A - 0.9 * SP, A + 0.9 * CP), bold("n"), ORANGE, "end", 17, weight="700", dx=-8, dy=-6)
    # arcs at P
    sc.arc(P, 0.42, 0, PHI, "GREEN", 1.8, head=True)
    sc.label(_pol(P, 0.66, PHI / 2 - 8), "φ", "GREEN", "middle", 16, dy=5)
    sc.arc(P, 0.42, 90, 90 + PHI, "GREEN", 1.8, head=True)
    sc.label(_pol(P, 0.66, 90 + PHI / 2 + 6), "φ", "GREEN", "middle", 16, dy=5)
    # triangle labels
    sc.label((A + 0.7, A + 1.0), "a", "TEXT", "middle", 15, dy=19)
    sc.label((A + 0.9, A + 1.4), "2r", "TEXT", "start", 15, dx=9, dy=5)
    sc.line((A + 0.7, A + 1.4), (1.78, 3.36), "EDGE", 0.9)
    sc.label((1.78, 3.36), "√(a² + 4r²)", "TEXT", "end", 15, dx=-4, dy=0)
    # e_theta into the paper
    _pin(sc, P)
    sc.label(P, "P", "HEAD", "end", 17, dx=-30, dy=18)
    sc.label(P, TH, "HEAD", "start", 17, weight="700", dx=14, dy=44)
    _spin(sc, P, 0.22, -20, -140, "positive about " + TH, (14, 72), "start")
    sc.note((-3.4, -0.55), _en("θ") + " = " + bold("k") + " × " + _en("r") + ", into the paper", "TEXT", "start", 13)
    _matrix(sc, -4.4, 3.9, _mname("1", "2"), (("a/D", "0", "−2r/D"), ("0", "1", "0"), ("2r/D", "0", "a/D")), colw=0.62)
    sc.note((-4.4, 2.55), "D = √(a² + 4r²)", "TEXT", "start", 14, dy=-4)
    return sc


@figure("p19-rotation-k",
        "View from above of the cylindrical basis turned by theta about k, with the start parallel and the second turning circle.",
        r"Rotation about $\mathbf k$ (out of the paper); the opposite leg of the triangle of $\mathbf e_\theta$ lies along $-\mathbf i$. Seen from above, the path stays in the ring between the parallels of radii $a$ and $r_\ast$.")
def rotation_k():
    K = 80
    sc = Scene(860, 600, (330, 290), K)
    O = (0.0, 0.0)
    th = 35.0
    _rot_view(sc, th, (bold("i"), bold("j")), (ER, TH), L=2.0, u=1.0, ra=0.5, rl=0.36, ls=13, cf=0.95, cdy=38)
    sc.circle(O, 2.0, "GREEN", 1.6, "7 5")
    sc.circle(O, 1.4, "GREEN", 1.6, "7 5")
    # labels of the circles, with a leader line
    a1 = _pol(O, 2.0, 235)
    sc.line(a1, (a1[0] - 0.25, a1[1] - 0.45), "GREEN", 0.9)
    sc.label((a1[0] - 0.25, a1[1] - 0.45), "r = a (start parallel)", "GREEN", "end", 15, dx=-4, dy=14)
    a2 = _pol(O, 1.4, 300)
    sc.line(a2, (a2[0] + 0.3, -2.62), "GREEN", 0.9)
    sc.label((a2[0] + 0.3, -2.62), "r = " + S("r", "*") + " (other turning radius)", "GREEN", "start", 15, dx=-6, dy=16)
    # start point and its velocity
    sc.vec((2.0, 0.0), (2.0, 0.85), None, "GREEN", 2.6, head=10)
    sc.dotp((2.0, 0.0), 5.0)
    sc.label((2.0, 0.85), S("v", "0"), "GREEN", "start", 17, dx=10, dy=4)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-6)
    _spin(sc, O, 0.3, 200, 340, "positive about k", (0, 66), "middle")
    _matrix(sc, 3.2, -0.3, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.78)
    return sc


@figure("p19-fbd",
        "Free-body diagram of the particle on the paraboloid in the circular case: weight, normal reaction and their horizontal resultant.",
        r"Forces on $P$ on the parallel of radius $a$ when $v_0^2 = 2ga$: the weight and the reaction $N\mathbf n$ with $N = \sqrt5\,mg$; the vertical part of the reaction carries the weight, its horizontal part $2mg$ is the centripetal force.")
def fbd():
    K = 88
    sc = Scene(820, 540, (330, 440), K)
    O = (0.0, 0.0)
    P = (A, A)
    sc.vec(O, (0.0, 3.6), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 3.6), "z", "TEXT", "middle", 16, weight="700", dx=-12, dy=4)
    _parab(sc, 0.0, 2.4, "EDGE", 1.5)
    w = 0.6                             # m g = 0.6 units, so every arrowhead stays right of the axis
    W = (A, A - w)
    N = (A - 2.0 * w, A + 1.0 * w)      # N = sqrt5 m g along n: (-2, 1) m g
    Rs = (A - 2.0 * w, A)
    sc.line((W[0] - 0.07, W[1] + 0.035), (Rs[0] + 0.07, Rs[1] - 0.035), "EDGE", 1.1, "5 4")
    sc.line((N[0], N[1] - 0.1), (Rs[0], Rs[1] + 0.1), "EDGE", 1.1, "5 4")
    sc.vec(P, W, None, RED, 3.0, head=12)
    sc.label((A, A - w / 2), "−m g " + bold("k"), RED, "start", 16, dx=10, dy=5)
    sc.vec(P, N, None, PURPLE, 3.0, head=12)
    sc.label(N, "N " + bold("n"), PURPLE, "start", 17, dx=-4, dy=-14)
    sc.line(P, (Rs[0] + 0.1, Rs[1]), PURPLE, 2.6, "7 4")
    arrow_head(sc.c, sc.P(P), sc.P(Rs), PURPLE, 11)
    sc.label((0.0, Rs[1]), "resultant −2 m g " + ER, PURPLE, "end", 15, dx=-10, dy=-2)
    sc.label((0.0, Rs[1]), "(centripetal m " + S("v", "0", "2") + "/a)", PURPLE, "end", 15, dx=-10, dy=20)
    _pin(sc, P)
    sc.label(P, "P", "HEAD", "start", 17, dx=14, dy=-14)
    sc.label(P, TH, "HEAD", "start", 16, weight="700", dx=16, dy=8)
    sc.note((-3.4, -0.6), "inertial frame: no inertia forces; smooth surface: reaction along n only", "TEXT", "start", 13)
    return sc
