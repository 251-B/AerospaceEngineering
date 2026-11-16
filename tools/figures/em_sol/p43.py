"""Problem 43: two connected particles, plane with a hole (vertical section, top view, view along k, free-body diagrams, band of radii)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import ORANGE, PURPLE, RED, YELLOW, arrow, away, basis_view
from figures.em_sol.p42 import ER, ETH, _along, _r0
from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

K_ = bold("k")
I_ = bold("i")
J_ = bold("j")
P1 = S("P", "1")
P2 = S("P", "2")
DARK = "#4b5563"
LGREEN = "#10b981"


def _band(sc, x0, x1, hole=0.06, t=0.12):
    """Cut through the plane: a thick light grey band with a small gap at O."""
    for a, b in ((x0, -hole), (hole, x1)):
        sc.poly([(a, 0.0), (b, 0.0), (b, -t), (a, -t)], "EDGE", 1.2, fill="EDGE", close=True, opacity=0.35)


@figure("p43-elevation",
        "Vertical section through the hole showing P1 on the plane at distance r and P2 hanging at depth 2a minus r on the cord of length 2a.",
        r"Section through the hole, $\mathbf k$ up. The cord has length $r$ on the plane and $2a - r$ below it, so $\mathbf r_0^{P_2} = (r - 2a)\,\mathbf k$; when $P_1$ moves away from the hole, $P_2$ rises by the same amount.")
def elevation():
    sc = Scene(760, 520, (250, 150), 110)
    O = (0.0, 0.0)
    r, d = 1.4, 0.6
    y0 = 0.06                                   # centre line of the cord on the plane
    _band(sc, -0.6, 2.6)
    sc.label((2.0, -0.12), "smooth horizontal plane", "TEXT", "middle", 14, dy=22)
    sc.label((-0.06, 0.0), "O (hole)", "TEXT", "end", 15, dx=-8, dy=-12)
    # lowest possible depth
    sc.line((-1.0, -2.0), (2.6, -2.0), "EDGE", 1.2, "6 5")
    sc.label((2.6, -2.0), "depth 2a (r = 0)", "TEXT", "end", 14, italic=False, dy=-8)
    sc.note((-1.0, -2.0), "r between a and 2a for v0 = √(8ag/3)", "TEXT", "start", 13, dy=22)
    # axes: k up, e_r along the cord (it points from O to P1)
    sc.vec(O, (0.0, 1.3), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 1.3), K_, "TEXT", "start", 16, weight="700", dx=8, dy=6)
    sc.vec((0.0, y0), (2.3, y0), None, "EDGE", 1.4, head=8)
    sc.label((2.3, y0), ER, "TEXT", "middle", 16, weight="700", dy=-10)
    # cord
    sc.line((r, y0), (0.0, y0), "HEAD", 4.5)
    sc.line((0.0, y0), (0.0, -d), "HEAD", 4.5)
    sc.label((r / 2, y0), "r", "HEAD", "middle", 17, dy=-12)
    sc.label((0.0, -d / 2), "2a − r", "HEAD", "end", 16, dx=-10, dy=5)
    # particles
    sc.dotp((r, y0 + 0.06), 6.5)
    sc.label((r, y0 + 0.06), P1, "HEAD", "start", 17, dx=12, dy=-6)
    sc.dotp((0.0, -d), 6.5)
    sc.label((0.0, -d), P2, "HEAD", "start", 17, dx=12, dy=5)
    # e_theta into the paper at P1
    axis_in(sc, (r, 0.62), None, r_px=9)
    sc.label((r, 0.62), ETH + " points into the paper here (⊗)", "HEAD", "start", 14, dx=16, dy=5)
    # depth dimension of P2
    xd = -1.0
    sc.line((xd, 0.0), (-0.6, 0.0), "EDGE", 1.1, "5 4")
    sc.line((xd, -d), (-0.06, -d), "EDGE", 1.1, "5 4")
    sc.dim((xd, 0.0), (xd, -d), "", gap=0.0)
    sc.label((xd, -d / 2), S("z", "2") + " = r − 2a", "TEXT", "end", 15, dx=-10, dy=5)
    return sc


@figure("p43-top",
        "Top view of the plane with P1 at polar coordinates r and theta, its right triangle, the polar basis, the initial push v0 perpendicular to the cord and the band between the circles r = a and r = 2a.",
        r"Top view, $\mathbf k$ out of the paper. $\mathbf r_0^{P_1} = r\,\mathbf e_r$ with legs $r\cos\theta$ and $r\sin\theta$; the push $v_0$ is along $\mathbf e_\theta$ at $\theta = 0$, and for $v_0 = \sqrt{8ag/3}$ the particle stays in the band $a \le r \le 2a$.")
def top():
    sc = Scene(780, 700, (390, 350), 120)
    O = (0.0, 0.0)
    th, r = 40.0, 1.5
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    P = (r * c, r * s)
    F = (r * c, 0.0)
    # band of part (d): the annulus a <= r <= 2a
    ox, oy = sc.P(O)
    R1, R2 = 1.0 * sc.k, 2.0 * sc.k
    sc.c.add(f'<path d="M{ox + R2:.1f},{oy:.1f} A{R2:.1f},{R2:.1f} 0 1 0 {ox - R2:.1f},{oy:.1f} A{R2:.1f},{R2:.1f} 0 1 0 {ox + R2:.1f},{oy:.1f} Z '
             f'M{ox + R1:.1f},{oy:.1f} A{R1:.1f},{R1:.1f} 0 1 0 {ox - R1:.1f},{oy:.1f} A{R1:.1f},{R1:.1f} 0 1 0 {ox + R1:.1f},{oy:.1f} Z" '
             f'fill="{LGREEN}" fill-opacity="0.10" fill-rule="evenodd" stroke="none"/>')
    sc.circle(O, 1.0, "EDGE", 1.3, "6 5")
    sc.circle(O, 2.0, "EDGE", 1.3, "6 5")
    sc.label(_pol(O, 0.78, 300), "r = a", "TEXT", "middle", 14, dy=5)
    sc.label(_pol(O, 2.17, 303), "r = 2a", "TEXT", "middle", 14, dy=5)
    sc.label(_pol(O, 1.5, 246), "band of part (d)", LGREEN, "middle", 14, italic=False, dy=5)
    triangle(sc, [O, F, P], YELLOW, 0.30)
    fixed_axis(sc, O, 0, 2.5, "x", off=(14, 5))
    fixed_axis(sc, O, 90, 2.5, "y", off=(0, -10))
    sc.line(O, (-2.5, 0.0), "EDGE", 1.4)
    sc.line(O, (0.0, -2.5), "EDGE", 1.4)
    # legs
    sc.line(O, F, "EDGE", 1.2, "5 4")
    sc.line(F, P, "EDGE", 1.2, "5 4")
    right_angle(sc, F, 180, 90, 0.1)
    sc.label((F[0] * 0.5, 0.0), "r cos θ", "TEXT", "middle", 15, dx=-4, dy=22)
    sc.label((F[0], P[1] * 0.55), "r sin θ", "TEXT", "start", 15, dx=10, dy=5)
    # cord = position vector
    sc.line(P, O, "HEAD", 4.5)
    _along(sc, O, P, _r0("P1") + " = r " + ER, "HEAD", 15, 0.5, 18)
    sc.arc(O, 0.4, 0, th, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.62, 14), "θ", "GREEN", "middle", 16, dy=5)
    # polar basis at P1
    L = 0.8
    tr = (P[0] + L * c, P[1] + L * s)
    tt = (P[0] - L * s, P[1] + L * c)
    sc.vec(P, tr, None, "BLUE", 2.6, head=11)
    sc.vec(P, tt, None, "BLUE", 2.6, head=11)
    sc.label(tr, ER, "BLUE", "start", 17, weight="700", dx=10, dy=-4)
    sc.label(tt, ETH, "BLUE", "end", 17, weight="700", dx=-10, dy=-4)
    sc.dotp(P, 5.5)
    sc.label(P, P1, "HEAD", "end", 17, dx=-14, dy=6)
    # initial position and push
    sc.circle((1.0, 0.0), 0.055, "HEAD", 2.0)
    sc.vec((1.0, 0.0), (1.0, 0.55), None, "GREEN", 3.2, head=12)
    sc.label((1.0, 0.55), S(bold("v"), "0"), "GREEN", "middle", 17, weight="700", dy=-8, dx=-1)
    sc.label((1.0, 0.0), S("P", "1") + "(0), r = a", "HEAD", "start", 15, dx=10, dy=24)
    sc.label((-2.45, -2.3), S(bold("v"), "0") + " (perpendicular to the cord):", "TEXT", "start", 14, italic=False)
    sc.label((-2.45, -2.47), "push along " + ETH + " at θ = 0", "TEXT", "start", 14, italic=False)
    # O, k and the sense of theta
    axis_out(sc, O, None)
    sc.label(O, K_ + " (up)", "HEAD", "end", 16, dx=-14, dy=-10)
    sc.arc(O, 0.28, 200, 340, "GREEN", 1.8, head=True)
    sc.label(O, "counterclockwise", "GREEN", "end", 12, italic=False, dx=-4, dy=34)
    sc.label(O, "seen from above", "GREEN", "end", 12, italic=False, dx=-4, dy=49)
    return sc


@figure("p43-rotation-k",
        "View from above of the polar basis e_r, e_theta turned by theta from i, j, with the two unit right triangles.",
        r"Rotation by $\theta$ about $\mathbf k$ (upward, out of the paper). The triangle of $\mathbf e_\theta$ has its opposite leg along $-\mathbf i$: the minus sign of $\mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j$.")
def rotation_k():
    sc = Scene(980, 600, (440, 290), 80)
    O = (0.0, 0.0)
    basis_view(sc, O, 40.0, (I_, J_), (ER, ETH), L=2.0, u=1.4, ang="θ",
               legs=("cos θ", "sin θ", "cos θ", "−sin θ on i"), cf=0.9, l1dx=8, l4=(12, "end", 13))
    axis_out(sc, O, None)
    sc.label(O, K_ + " (up)", "HEAD", "end", 17, dx=-20, dy=8)
    _spin(sc, O, 0.3, 200, 340, "positive about k = counterclockwise seen from above", (-26, 46), "end")
    _matrix(sc, 3.0, -1.2, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.8)
    return sc


@figure("p43-fbd",
        "Exploded free-body diagrams of P1 and P2 with the weights, the normal reaction of the plane, the tension at both ends of the cord, and the friction of part (f) opposite to the velocity of P1 (velocity shown in a separate inset).",
        r"Forces on $P_1$: weight, normal reaction $N_1\,\mathbf k$, tension $-T\,\mathbf e_r$ (and friction $\mathbf R$ opposite to $\mathbf v_0^{P_1}$ in part (f)); on $P_2$: weight and tension $T\,\mathbf k$. The tension cancels when the radial equation of $P_1$ and the equation of $P_2$ are added.")
def fbd():
    sc = Scene(1130, 520, (170, 175), 100)
    O = (0.0, 0.0)
    y0 = 0.06
    # ---- left panel: vertical section
    sc.note((-0.6, 1.5), "P1 and P2, vertical section (k up)", "TEXT", "start", 14, dy=0)
    _band(sc, -0.6, 2.8)
    sc.label((-0.06, 0.0), "O", "TEXT", "end", 14, dx=-4, dy=-10)
    p1 = (1.9, y0)
    p2 = (0.0, -1.6)
    sc.line(p1, (0.0, y0), "EDGE", 1.8)
    sc.line((0.0, y0), p2, "EDGE", 1.8)
    # P1
    w1 = arrow(sc, p1, (0.0, -1.0), RED, 3.2, 12, 1.0)
    sc.label(w1, "−m g " + K_, RED, "start", 16, dx=10, dy=5)
    n1 = arrow(sc, p1, (0.0, 1.0), PURPLE, 3.2, 12, 1.0)
    sc.label(n1, S("N", "1") + " = m g", PURPLE, "start", 16, dx=10, dy=5)
    t1 = arrow(sc, p1, (-1.0, 0.0), "PINK", 3.4, 12, 1.3)
    sc.label((1.25, y0), "−T " + ER, "PINK", "middle", 16, dy=-14)
    sc.dotp(p1, 5.5)
    sc.label(p1, P1, "HEAD", "start", 17, dx=12, dy=-14)
    # P2
    w2 = arrow(sc, p2, (0.0, -1.0), RED, 3.2, 12, 1.0)
    sc.label(w2, "−m g " + K_, RED, "start", 16, dx=10, dy=5)
    t2 = arrow(sc, p2, (0.0, 1.0), "PINK", 3.4, 12, 1.3)
    sc.label((0.0, -1.0), "+T " + K_, "PINK", "end", 16, dx=-10, dy=5)
    for sgn in (-1, 1):
        sc.line((sgn * 0.05 + 0.0, p2[1]), (sgn * 0.25, p2[1]), PURPLE, 2.6)
        sc.dotp((sgn * 0.25, p2[1]), 3.2, PURPLE)
    sc.label((0.3, p2[1]), S("R", "x") + " " + I_ + " + " + S("R", "y") + " " + J_ + " (zero)", PURPLE, "start", 14, dx=8, dy=24)
    sc.dotp(p2, 5.5)
    sc.label(p2, P2, "HEAD", "end", 17, dx=-10, dy=-14)
    sc.note((0.35, -1.2), "same T at both ends", "TEXT", "start", 13)
    sc.note((0.35, -1.4), "(massless cord, smooth hole)", "TEXT", "start", 13)
    # ---- right panel: top view of P1 (horizontal forces)
    O2 = (5.9, -0.2)
    th = 40.0
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    r = 1.5
    q = (O2[0] + r * c, O2[1] + r * s)
    sc.note((4.4, 1.5), "P1, top view (k out of the paper)", "TEXT", "start", 14)
    sc.dotp(O2, 3.5, "EDGE")
    sc.label(O2, "O", "TEXT", "end", 15, dx=-8, dy=-8)
    sc.line(q, O2, "EDGE", 1.2, "6 5")
    tp = arrow(sc, q, (-c, -s), "PINK", 3.4, 12, 1.3)
    sc.label((q[0] - 0.65 * c, q[1] - 0.65 * s), "−T " + ER, "PINK", "middle", 16, dx=-12, dy=-14)
    vd = (math.cos(math.radians(th + 55)), math.sin(math.radians(th + 55)))
    fr = arrow(sc, q, (-vd[0], -vd[1]), ORANGE, 3.0, 11, 0.8)
    sc.vec(q, (q[0] - 0.8 * vd[0], q[1] - 0.8 * vd[1]), None, ORANGE, 3.0, head=11)
    ft = (q[0] - 0.8 * vd[0], q[1] - 0.8 * vd[1])
    sc.label(ft, "R = −μ m g v / |v|", ORANGE, "middle", 14, dy=22)
    sc.label(ft, "(part f, opposite to v)", ORANGE, "middle", 14, italic=False, dy=38)
    for d, nm, dx, dy, anc in (((c, s), ER, 8, 14, "start"), ((-s, c), ETH, -8, -6, "end")):
        tip = (q[0] + 0.55 * d[0], q[1] + 0.55 * d[1])
        sc.vec(q, tip, None, "BLUE", 2.4, head=10)
        sc.label(tip, nm, "BLUE", anc, 16, weight="700", dx=dx, dy=dy)
    sc.dotp(q, 5.5)
    sc.label(q, P1, "HEAD", "start", 17, dx=14, dy=22)
    # ---- inset: velocity of P1 (not a force)
    x0, y0b, x1, y1 = 5.0, -3.0, 7.7, -0.95
    sc.poly([(x0, y0b), (x1, y0b), (x1, y1), (x0, y1)], "EDGE", 1.2, close=True)
    sc.note((x0 + 0.1, y1 - 0.2), "velocity of P1 (inset)", "TEXT", "start", 13)
    Q = (6.6, -2.7)
    ve = (1.1 * math.cos(math.radians(55)) * c, 1.1 * math.cos(math.radians(55)) * s)
    vt = (-1.1 * math.sin(math.radians(55)) * s, 1.1 * math.sin(math.radians(55)) * c)
    tip = (Q[0] + ve[0] + vt[0], Q[1] + ve[1] + vt[1])
    sc.line((Q[0] + ve[0], Q[1] + ve[1]), tip, "GREEN", 1.0, "3 4")
    sc.line((Q[0] + vt[0], Q[1] + vt[1]), tip, "GREEN", 1.0, "3 4")
    _dvec(sc, Q, (Q[0] + ve[0], Q[1] + ve[1]), "GREEN", 2.0, 9)
    _dvec(sc, Q, (Q[0] + vt[0], Q[1] + vt[1]), "GREEN", 2.0, 9)
    sc.vec(Q, tip, None, "GREEN", 3.2, head=12)
    sc.label(tip, S(bold("v"), "0", "P1"), "GREEN", "start", 16, weight="700", dx=8, dy=-4)
    sc.label((Q[0] + ve[0], Q[1] + ve[1]), "ṙ " + ER, "GREEN", "start", 14, dx=8, dy=16)
    sc.label((Q[0] + vt[0], Q[1] + vt[1]), "r θ̇ " + ETH, "GREEN", "end", 14, dx=-8, dy=16)
    sc.dotp(Q, 4.0)
    sc.note((-0.6, -3.2), "inertial frame: no inertia forces; in the top view the weight and N1 (along k) cancel", "TEXT", "start", 13)
    return sc


def _cubic(x):
    return -3 * x ** 3 + 7 * x ** 2 - 4


@figure("p43-band",
        "Plot of the cubic -3x^3 + 7x^2 - 4 with roots -2/3, 1 and 2, positive only between 1 and 2, the band of radii of P1.",
        r"The square of the radial rate is proportional to $-3x^3 + 7x^2 - 4 = -(x-1)(x-2)(3x+2)$, with $x = r/a$: it is non-negative only for $1 \le x \le 2$, so $P_1$ oscillates between $r = a$ and $r = 2a$.")
def band():
    W, H = 840, 600
    sc = Scene(W, H, (0, H), 1)
    x0, y0 = 70, 40
    xmin, xmax = -1.0, 2.45
    fmin, fmax = -4.6, 6.6
    sx = (W - 150 - x0) / (xmax - xmin)
    sy = (H - 70 - y0) / (fmax - fmin)
    X = lambda x: x0 + (x - xmin) * sx
    Y = lambda f: y0 + (f - fmin) * sy
    pt = lambda x, f: (X(x), Y(f))
    ax = X(0.0)
    # allowed region
    xs = [1.0 + i / 100.0 for i in range(101)]
    sc.poly([pt(1.0, 0.0)] + [pt(x, _cubic(x)) for x in xs] + [pt(2.0, 0.0)], "BLUE", 0.0, fill="BLUE", close=True, opacity=0.14)
    # axes
    sc.vec((x0 - 10, Y(0.0)), (X(xmax) + 20, Y(0.0)), None, "EDGE", 1.4, head=8)
    sc.vec((ax, Y(fmin) - 10), (ax, Y(fmax) + 14), None, "EDGE", 1.4, head=8)
    sc.label((X(xmax) + 20, Y(0.0)), "x = r/a", "TEXT", "start", 16, dx=-4, dy=24)
    sc.label((ax, Y(fmax) + 14), "−3" + "x" + '<tspan baseline-shift="super" font-size="70%">3</tspan>' + " + 7x" +
             '<tspan baseline-shift="super" font-size="70%">2</tspan>' + " − 4", "TEXT", "start", 16, dx=10, dy=4)
    # curve: dashed grey where forbidden, thick blue in the band
    def runs(a, b, col, w, dash=None):
        sc.poly([pt(a + (b - a) * i / 300.0, _cubic(a + (b - a) * i / 300.0)) for i in range(301)], col, w, dash)
    runs(-1.0, 1.0, DARK, 2.0, "7 5")
    runs(2.0, 2.4, DARK, 2.0, "7 5")
    runs(1.0, 2.0, "BLUE", 4.2)
    # roots
    for xr, txt, dx, dy, anc in ((-2.0 / 3.0, "x = −2/3", -8, 22, "end"), (1.0, "x = 1  (r = a)", -10, -12, "end"), (2.0, "x = 2  (r = 2a)", 10, -12, "start")):
        sc.dotp(pt(xr, 0.0), 5.0, DARK)
        sc.label(pt(xr, 0.0), txt, "TEXT", anc, 15, dx=dx, dy=dy)
    xm = 14.0 / 9.0
    sc.dotp(pt(xm, _cubic(xm)), 3.6, "BLUE")
    sc.label(pt(1.5, 2.45), "allowed: ṙ² = g a³ f(x) / (3 r²) ≥ 0", "BLUE", "middle", 15, italic=False)
    sc.label(pt(0.5, -1.25), "forbidden", "TEXT", "middle", 15)
    sc.label(pt(2.2, 0.95), "forbidden", "TEXT", "middle", 15)
    # radial accelerations at the turning points
    yy = -0.9
    sc.line(pt(1.0, 0.0), pt(1.0, yy), "EDGE", 1.1, "4 4")
    sc.vec(pt(1.0, yy), pt(1.0 + 0.3, yy), None, "GREEN", 2.6, head=10)
    sc.label(pt(1.0, yy), "r̈ = 5g/6 > 0", "GREEN", "start", 14, dy=22)
    sc.line(pt(2.0, 0.0), pt(2.0, yy), "EDGE", 1.1, "4 4")
    sc.vec(pt(2.0, yy), pt(2.0 - 0.3, yy), None, "GREEN", 2.6, head=10)
    sc.label(pt(2.0, yy), "r̈ = −g/3 < 0", "GREEN", "end", 14, dy=22 + 22)
    return sc
