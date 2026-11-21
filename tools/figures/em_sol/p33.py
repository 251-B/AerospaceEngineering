"""Problem 33: two repelling beads on a parabolic wire z = x^2/(2L) that spins about its vertical axis Oz."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

X1, X2 = -0.7, 1.2                      # abscissas of P1 and P2 in units of L


def z(x):
    return x * x / 2.0


def parabola(sc):
    sc.curve(lambda x: (x, z(x)), -1.85, 1.85, col="HEAD", w=3.0)


@figure("p33-top-view",
        "View from above with k out of the paper at O: the inertial axes i0 to the right and j0 up in grey, the axes i1 "
        "and j1 of the wire frame turned counter-clockwise by omega t in blue, and the trace of the plane of the wire "
        "along i1 with the projections of P1 and P2",
        r"View from $+z$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$) at the vertex $O$: then "
        r"$\mathbf j_0 = \mathbf k_0\times\mathbf i_0$ points up the page. $\mathbf i_1, \mathbf j_1$ are "
        r"$\mathbf i_0, \mathbf j_0$ turned counter-clockwise by $\omega t$; the dashed legs give "
        r"$\mathbf i_1 = \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0$ and "
        r"$\mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0$. The plane of the wire is seen edge-on, "
        r"along $\mathbf i_1$; $P_1$ ($x_1 \lt 0$) and $P_2$ ($x_2 \gt 0$) project on it")
def top_view():
    sc = Scene(560, 470, (260, 240), 150)
    O = (0.0, 0.0)
    a = 35.0
    d = (math.cos(math.radians(a)), math.sin(math.radians(a)))
    sc.line((-1.3 * d[0], -1.3 * d[1]), (1.45 * d[0], 1.45 * d[1]), "EDGE", 1.0, "2 3")
    fixed_axis(sc, O, 0, 1.4, S(bold("i"), "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.3, S(bold("j"), "0"), off=(14, 4))
    axis_out(sc, O, S(bold("k"), "0") + " = " + S(bold("k"), "1"), off=(44, 50))
    sc.label(O, "O", "HEAD", "end", 16, dx=-16, dy=8)
    i1 = unit(sc, O, a, 0.62, S(bold("i"), "1"), off=(14, 2))
    j1 = unit(sc, O, a + 90, 0.62, S(bold("j"), "1"), off=(-12, -8))
    sc.angle(O, 0.24, 0, a, "ωt", name_r=0.36)
    sc.angle(O, 0.20, 90, a + 90, "ωt", name_r=0.31)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos ωt", "TEXT", "middle", 14, dy=18)
    sc.label((0.0, i1[1]), "sin ωt", "TEXT", "start", 14, dx=8, dy=-6)
    sc.dashed(j1, (j1[0], 0.0))
    sc.dashed(j1, (0.0, j1[1]))
    sc.label((j1[0], 0.0), "−sin ωt", "TEXT", "middle", 14, dy=18)
    p1 = (X1 * d[0], X1 * d[1])
    p2 = (X2 * d[0], X2 * d[1])
    sc.dotp(p1, 4.5, "ACC")
    sc.label(p1, S("P", "1"), "HEAD", "end", 16, dx=-10, dy=-8)
    sc.dotp(p2, 4.5, "ACC")
    sc.label(p2, S("P", "2"), "HEAD", "start", 16, dx=8, dy=16)
    sc.note((0.55, -0.95), "view from +z", "TEXT", "start", 13)
    sc.note((0.55, -1.07), "ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc


@figure("p33-wire-plane",
        "Plane Oxz of the wire: the parabola z = x squared over 2L, the axis Oz with the spin omega, j1 into the paper at "
        "O, the beads P1 and P2, the dashed components x2 and x2 squared over 2L of the position of P2, and at P2 the "
        "slope triangle with legs 1 and x2 over L and hypotenuse sigma2, with the unit tangent t2 and normal n2",
        r"Plane $Oxz$, fixed in $S_1$ ($\mathbf j_1$ points into the paper, $\otimes$). The position of $P_2$ has the "
        r"dashed components $x_2$ and $z_2 = x_2^2/(2L)$. The shaded slope triangle at $P_2$ has a horizontal leg "
        r"proportional to $1$, a vertical leg proportional to $dz/dx = x_2/L$ and the hypotenuse $\sigma_2 = "
        r"\sqrt{1 + x_2^2/L^2}$ along the tangent; dividing by $\sigma_2$ gives $\mathbf t_2$, and turning it $90^\circ$ "
        r"towards the concave side gives $\mathbf n_2$ (orange)")
def wire_plane():
    sc = Scene(640, 400, (320, 335), 150)
    O = (0.0, 0.0)
    P1 = (X1, z(X1))
    P2 = (X2, z(X2))
    fixed_axis(sc, (-2.0, 0.0), 0, 4.0, "x", off=(12, 5))
    fixed_axis(sc, (0.0, -0.15), 90, 2.1, "z", off=(14, 4))
    spin_about_vertical(sc, (0.0, 1.72), 0.17, 0.05, "ω")
    parabola(sc)
    # components of r1(P2)
    sc.dashed(P2, (X2, 0.0))
    sc.dashed(P2, (0.0, P2[1]))
    sc.label((X2 / 2, P2[1]), S("x", "2"), "TEXT", "middle", 16, dy=-8)
    sc.label((X2, P2[1] / 2), S("x", "2", "2") + "/(2L)", "TEXT", "start", 15, dx=8, dy=5)
    # slope triangle at P2 (scaled by h)
    h = 0.42
    A = (X2 + h, P2[1])
    C = (X2 + h, P2[1] + h * X2)
    triangle(sc, [P2, A, C])
    right_angle(sc, A, 180, 90, 0.06)
    sc.line(P2, A, "EDGE", 1.1)
    sc.line(A, C, "EDGE", 1.1)
    sc.line(P2, (X2 + 1.6 * h, P2[1] + 1.6 * h * X2), "EDGE", 1.0, "2 3")
    sc.label(((P2[0] + A[0]) / 2 + 0.06, A[1]), "1", "TEXT", "middle", 15, dy=-6)
    sc.label((A[0], (A[1] + C[1]) / 2), S("x", "2") + "/L", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((P2[0] + 0.85 * (C[0] - P2[0]), P2[1] + 0.85 * (C[1] - P2[1])), S("σ", "2"), "TEXT", "end", 15, dx=-12, dy=-2)
    ang = math.degrees(math.atan(X2))
    unit(sc, P2, ang, 0.32, S(bold("t"), "2"), "ACC", off=(-6, -12))
    unit(sc, P2, ang + 90, 0.32, S(bold("n"), "2"), "ACC", off=(-12, -6))
    sc.mass(P2, None, r=7)
    sc.label(P2, S("P", "2"), "HEAD", "start", 17, dx=14, dy=26)
    sc.mass(P1, None, r=7)
    sc.label(P1, S("P", "1"), "HEAD", "end", 17, dx=-12, dy=16)
    # basis of S1 at O
    unit(sc, O, 0, 0.32, S(bold("i"), "1"), off=(2, 22))
    unit(sc, O, 90, 0.32, S(bold("k"), "1"), off=(-18, 4))
    axis_in(sc, O, S(bold("j"), "1"), col="BLUE", off=(-26, 22))
    sc.label(O, "O", "HEAD", "start", 16, dx=10, dy=22)
    sc.gravity((1.0, 1.85), 0.32, "g")
    return sc


@figure("p33-chord",
        "The chord from P1 to P2 on the parabola, with the right triangle whose horizontal leg is x2 minus x1, vertical "
        "leg is the difference of heights and hypotenuse is the distance d, and the two repulsive forces along the chord",
        r"Chord $P_1P_2$: in the shaded right triangle the horizontal leg is $x_2 - x_1$, the vertical leg is "
        r"$z_2 - z_1 = (x_2^2 - x_1^2)/(2L) = (x_2 - x_1)(x_1 + x_2)/(2L)$ and the hypotenuse is the distance $d$; the "
        r"slope of the chord is $(x_1 + x_2)/(2L)$. The repulsions $\mathbf F_{E1}$ and $\mathbf F_{E2} = -\mathbf F_{E1}$ "
        r"(pink) act along the chord, pushing the beads apart")
def chord():
    sc = Scene(660, 380, (320, 330), 150)
    P1 = (X1, z(X1))
    P2 = (X2, z(X2))
    M = (X2, P1[1])
    fixed_axis(sc, (-2.0, 0.0), 0, 4.0, "x", off=(12, 5))
    fixed_axis(sc, (0.0, -0.15), 90, 2.0, "z", off=(14, 4))
    parabola(sc)
    triangle(sc, [P1, M, P2])
    right_angle(sc, M, 180, 90, 0.06)
    sc.line(P1, P2, "HEAD", 1.4, "6 4")
    sc.dashed(P1, M)
    sc.dashed(M, P2)
    sc.label((0.36, M[1]), S("x", "2") + " − " + S("x", "1"), "TEXT", "middle", 15, dy=-8)
    sc.label((M[0], (M[1] + P2[1]) / 2), S("z", "2") + " − " + S("z", "1"), "TEXT", "start", 15, dx=10, dy=5)
    sc.label(((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2), "d", "TEXT", "end", 17, dx=-8, dy=-10)
    u = ((P2[0] - P1[0]), (P2[1] - P1[1]))
    n = math.hypot(*u)
    u = (u[0] / n, u[1] / n)
    ang = math.degrees(math.atan2(u[1], u[0]))
    unit(sc, P2, ang, 0.42, S(bold("F"), "E2"), "PINK", off=(4, -14))
    unit(sc, P1, ang + 180, 0.42, S(bold("F"), "E1"), "PINK", off=(-8, 22))
    sc.mass(P1, None, r=7)
    sc.label(P1, S("P", "1"), "HEAD", "start", 17, dx=6, dy=28)
    sc.mass(P2, None, r=7)
    sc.label(P2, S("P", "2"), "HEAD", "start", 17, dx=14, dy=18)
    sc.label((0.0, 0.0), "O", "HEAD", "start", 16, dx=8, dy=20)
    return sc


def _dvec(sc, a, b, col="PINK", w=2.4, head=10):
    """Dashed arrow (inertia force) from world point a to b."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


XA, XB = -0.8, 1.4                      # abscissas of P1 and P2 in the free-body diagram (units of L)


@figure("p33-fbd",
        "Free-body diagram of the two beads on the turning parabola: top, the plane of the wire with the weight, the "
        "repulsion along the chord, the in-plane reaction and the centrifugal force; bottom, the view from above with "
        "the Coriolis forces and the normal reactions",
        r"Forces in $Oxyz$. In the plane of the wire: weight, repulsion along the chord, reaction $N_{in}\,\mathbf n_i$ "
        r"and the centrifugal force $m\omega^2x_i\,\mathbf i_1$ (dashed). Seen from above: the Coriolis forces "
        r"$-2m\omega\dot x_i\,\mathbf j_1$ (dashed) and the reactions $N_{iy}\,\mathbf j_1$ that cancel them.")
def fbd():
    k = 125.0
    sc = Scene(780, 740, (340, 330), k)
    RY = -(570 - 330) / k                               # world y of the trace of the lower panel (pixel y = 560)
    z = lambda x: x * x / 2.0
    P1 = (XA, z(XA))
    P2 = (XB, z(XB))
    sg = math.sqrt(1 + XB * XB)
    t2 = (1 / sg, XB / sg)
    n2 = (-XB / sg, 1 / sg)
    ch = (P2[0] - P1[0], P2[1] - P1[1])
    cl = math.hypot(*ch)
    ch = (ch[0] / cl, ch[1] / cl)                       # unit vector from P1 to P2
    # ---- upper panel: plane Oxz, j1 into the paper
    fixed_axis(sc, (-2.4, 0.0), 0, 4.9, "x", off=(12, 5))
    sc.line((0.0, -0.15), (0.0, 2.3), "EDGE", 1.4, "10 3 2 3")
    sc.label((0.0, 2.3), "z", "TEXT", "middle", 16, weight="700", dx=14, dy=4)
    spin_about_vertical(sc, (0.0, 2.1), 0.17, 0.05, "ω")
    sc.curve(lambda x: (x, z(x)), -2.0, 2.0, col="HEAD", w=3.0)
    sc.line(P1, P2, "EDGE", 1.2, "6 4")
    sc.label((0.3, 0.64), "chord", "TEXT", "middle", 14, italic=False, dy=-10)
    axis_in(sc, (0.0, 0.0), None, col="BLUE")
    sc.label((0.0, 0.0), bold("j") + S("", "1") + " (into the paper)", "BLUE", "start", 15, weight="700", dx=14, dy=28)
    sc.label((0.0, 0.0), "O", "HEAD", "end", 17, dx=-14, dy=22)
    unit(sc, (0.0, 0.0), 0, 0.4, bold("i") + S("", "1"), off=(6, -12))
    unit(sc, (0.0, 0.0), 90, 0.4, bold("k") + S("", "1"), off=(-16, 4))
    # forces at P2
    sc.vec(P2, (P2[0], P2[1] - 0.6), None, "PINK", 2.8, head=11)
    sc.label((P2[0], P2[1] - 0.6), "−m g " + bold("k") + S("", "1"), "PINK", "start", 16, weight="700", dx=10, dy=6)
    e2 = (P2[0] + 0.6 * ch[0], P2[1] + 0.6 * ch[1])
    sc.vec(P2, e2, None, "PINK", 2.8, head=11)
    sc.label(e2, S(bold("F"), "E2"), "PINK", "start", 16, weight="700", dx=8, dy=-8)
    n0 = (P2[0] - 0.1 * t2[0], P2[1] - 0.1 * t2[1])
    n1 = (n0[0] + 0.55 * n2[0], n0[1] + 0.55 * n2[1])
    sc.vec(n0, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, S(bold("N"), "2n") + " " + S(bold("n"), "2"), "PINK", "end", 16, weight="700", dx=-8, dy=-2)
    c2 = (P2[0] + 0.6, P2[1])
    _dvec(sc, P2, c2, "PINK", 2.6)
    sc.label(c2, S(bold("F"), "C") + " = m ω² " + S("x", "2") + " " + bold("i") + S("", "1"), "PINK", "start", 16, weight="700",
             dx=10, dy=24)
    sc.label(c2, "(inertia)", "PINK", "start", 14, dx=10, dy=42)
    unit(sc, P2, math.degrees(math.atan2(t2[1], t2[0])), 0.35, S(bold("t"), "2"), "ACC", off=(12, -4))
    unit(sc, P2, math.degrees(math.atan2(n2[1], n2[0])), 0.35, S(bold("n"), "2"), "ACC", off=(-6, -12))
    # forces at P1
    e1 = (P1[0] - 0.6 * ch[0], P1[1] - 0.6 * ch[1])
    sc.vec(P1, e1, None, "PINK", 2.8, head=11)
    sc.label(e1, S(bold("F"), "E1"), "PINK", "end", 16, weight="700", dx=-8, dy=20)
    c1 = (P1[0] - 0.35, P1[1])
    _dvec(sc, P1, c1, "PINK", 2.6)
    sc.label(c1, "m ω² " + S("x", "1") + " " + bold("i") + S("", "1") + " (inertia)", "PINK", "end", 16, weight="700", dx=-8, dy=-10)
    sc.mass(P1, None, r=7)
    sc.label(P1, S("P", "1"), "HEAD", "start", 17, dx=12, dy=-12)
    sc.mass(P2, None, r=7)
    sc.label(P2, S("P", "2"), "HEAD", "end", 17, dx=-24, dy=24)
    sc.note((-2.6, -0.45), "plane Oxz of the wire", "TEXT", "start", 13)
    # ---- lower panel: view from above, k1 out of the paper, j1 up the page
    def R(x, y):
        return (x, RY + y)
    O = R(0.0, 0.0)
    sc.line(R(-2.0, 0.0), R(2.0, 0.0), "HEAD", 5.0)
    axis_out(sc, O, None, "BLUE")
    sc.label(O, bold("k") + S("", "1") + " (⊙)", "BLUE", "start", 15, weight="700", dx=14, dy=28)
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=28)
    unit(sc, O, 90, 0.55, bold("j") + S("", "1"), off=(-14, -2))
    unit(sc, R(2.15, 0.0), 0, 0.45, bold("i") + S("", "1"), off=(2, 22))
    sc.spin(O, 0.30, 105, 165, "ω", name_r=0.43)
    for xs, nm in ((XA, "1"), (XB, "2")):
        sc.mass(R(xs, 0.0), None, r=6.5)
        sc.label(R(xs, 0.0), S("P", nm), "HEAD", "end", 17, dx=-12, dy=26)
    # P2: x2-dot > 0
    p2 = R(XB, 0.0)
    _dvec(sc, (p2[0], p2[1] - 0.06), (p2[0], p2[1] - 0.85), "PINK", 2.6)
    sc.label((p2[0], p2[1] - 0.85), S(bold("F"), "COR,2") + " = −2 m ω ẋ₂ " + bold("j") + S("", "1"), "PINK", "start", 16,
             weight="700", dx=12, dy=2)
    sc.label((p2[0], p2[1] - 0.85), "(inertia)", "PINK", "start", 14, dx=12, dy=20)
    sc.vec((p2[0], p2[1] + 0.06), (p2[0], p2[1] + 0.85), None, "PINK", 2.8, head=11)
    sc.label((p2[0], p2[1] + 0.85), S(bold("N"), "2y") + " " + bold("j") + S("", "1") + " = 2 m ω ẋ₂ " + bold("j") + S("", "1"),
             "PINK", "start", 16, weight="700", dx=12, dy=-4)
    # P1: x1-dot < 0
    p1 = R(XA, 0.0)
    _dvec(sc, (p1[0], p1[1] + 0.06), (p1[0], p1[1] + 0.85), "PINK", 2.6)
    sc.label((p1[0], p1[1] + 0.85), S(bold("F"), "COR,1") + " (inertia)", "PINK", "start", 16, weight="700", dx=12, dy=-4)
    sc.vec((p1[0], p1[1] - 0.06), (p1[0], p1[1] - 0.85), None, "PINK", 2.8, head=11)
    sc.label((p1[0], p1[1] - 0.85), S(bold("N"), "1y") + " " + bold("j") + S("", "1"), "PINK", "start", 16, weight="700",
             dx=12, dy=4)
    sc.note((-2.6, RY - 1.2), "view from above: the wire is seen edge-on", "TEXT", "start", 13)
    return sc
