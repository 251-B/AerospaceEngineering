"""Problem 30: particle on a quarter circumference that turns about the vertical axis x1 = -R, with a spring to B."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

PHI = math.radians(50)


@figure("p30-arc-plane",
        "Plane X1Z1 of the moving frame: the quarter circumference of centre O and radius R, the rotation axis x1 = -R "
        "dashed, the spring from B to P, the angle phi from the negative z1 axis, the right triangle with legs R sin phi "
        "and R cos phi, the basis i1, k1 at O with j1 into the paper, and the path basis e_t, e_n at P",
        r"Plane $X_1Z_1$, fixed in $S_1$ ($\mathbf j_1$ points into the paper, $\otimes$). $\phi$ is measured at $O$ from "
        r"the downward axis $-z_1$. In the shaded right triangle the hypotenuse is $|OP| = R$, the leg adjacent to $\phi$ "
        r"is $R\cos\phi$ (downwards) and the opposite leg is $R\sin\phi$ (to the left); the distance from $P$ to the "
        r"rotation axis is $R(1 - \sin\phi)$. $\mathbf i_1, \mathbf k_1$ in blue, $\mathbf e_t, \mathbf e_n$ in orange")
def arc_plane():
    sc = Scene(660, 450, (500, 160), 205)
    O = (0.0, 0.0)
    P = (-math.sin(PHI), -math.cos(PHI))
    F = (0.0, P[1])                                        # foot of the horizontal through P on the z1 axis
    B = (-2.0, 0.0)
    # axes of S1 (grey) and the rotation axis x1 = -R (dashed)
    fixed_axis(sc, (-2.3, 0.0), 0, 2.72, S("X", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.22), 90, 1.65, S("Z", "1"), off=(16, 4))
    sc.line((-1.0, -1.22), (-1.0, 0.5), "EDGE", 1.3, "7 4")
    spin_about_vertical(sc, (-1.0, 0.36), 0.15, 0.045, "ω")
    # quarter circumference of centre O
    sc.curve(lambda s: (-math.sin(s), -math.cos(s)), 0.0, math.pi / 2, col="HEAD", w=3.0)
    # spring from B to P
    sc.spring(B, P, coils=8, amp=6.0)
    sc.dotp(B, 4.0)
    sc.label(B, "B", "HEAD", "middle", 17, dy=-12)
    # key triangle O - F - P
    triangle(sc, [O, F, P])
    right_angle(sc, F, 180, 90, 0.06)
    sc.line(O, P, "HEAD", 1.6)
    sc.label((0.3 * P[0], 0.3 * P[1]), "R", "TEXT", "end", 17, dx=-12, dy=-4)
    sc.label((0.0, P[1] / 2), "R cos φ", "TEXT", "start", 15, dx=10, dy=4)
    sc.dashed(F, P)
    sc.label(((F[0] + P[0]) / 2, F[1]), "R sin φ", "TEXT", "middle", 15, dy=20)
    sc.angle(O, 0.22, -90 - 50, -90, "φ", name_r=0.32)
    # distance from P to the rotation axis
    sc.dim((-1.0, -0.80), (P[0], -0.80), "R(1 − sin φ)", off=(-80, 5), size=14)
    sc.dashed(P, (P[0], -0.86))
    # points and bases
    sc.label(O, "O", "HEAD", "start", 17, dx=8, dy=-10)
    axis_in(sc, O, bold("j") + S("", "1"), col="BLUE", off=(-24, -14))
    unit(sc, O, 0, 0.30, bold("i") + S("", "1"), off=(2, 22))
    unit(sc, O, 90, 0.30, bold("k") + S("", "1"), off=(-18, 4))
    unit(sc, P, 130, 0.28, bold("e") + S("", "t"), "ACC", off=(-12, -6))
    unit(sc, P, 40, 0.28, bold("e") + S("", "n"), "ACC", off=(-12, -12))
    sc.mass(P, "P", r=7, name_off=(-6, 24))
    return sc


@figure("p30-top-view",
        "View from above with k out of the paper: the rotation axis at Q, the inertial axes i0 to the right and j0 up in "
        "grey, the axes i1 and j1 of the moving frame turned counter-clockwise by omega t in blue, the origin O of the "
        "moving frame at distance R from the axis on its dashed circle, with its velocity omega R j1 and acceleration "
        "minus omega squared R i1, and the point B on the other side of the axis",
        r"View from $+z$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$) at the point $Q$ of the axis: then "
        r"$\mathbf j_0 = \mathbf k_0\times\mathbf i_0$ points up the page. $\mathbf i_1, \mathbf j_1$ are "
        r"$\mathbf i_0, \mathbf j_0$ turned counter-clockwise by $\omega t$; the dashed legs of $\mathbf i_1$ are "
        r"$\cos\omega t$ along $\mathbf i_0$ and $\sin\omega t$ along $\mathbf j_0$. The origin $O$ of $S_1$ runs on the "
        r"dashed circle of radius $R$ with $\mathbf v_0^O = \omega R\,\mathbf j_1$ and $\mathbf a_0^O = -\omega^2R\,\mathbf i_1$")
def top_view():
    sc = Scene(600, 520, (270, 265), 150)
    Q = (0.0, 0.0)
    a = 35.0
    d = (math.cos(math.radians(a)), math.sin(math.radians(a)))
    O = (d[0], d[1])
    B = (-d[0], -d[1])
    sc.circle(Q, 1.0, "EDGE", 1.1, "5 4")
    fixed_axis(sc, Q, 0, 1.45, S(bold("i"), "0"), off=(16, 5))
    fixed_axis(sc, Q, 90, 1.4, S(bold("j"), "0"), off=(14, 4))
    axis_out(sc, Q, S(bold("k"), "0") + " = " + S(bold("k"), "1"), off=(-64, -10))
    sc.label(Q, "Q", "HEAD", "end", 16, dx=-16, dy=8)
    # trace of the plane X1Z1 (it contains i1): B, Q and O are on it
    sc.line(B, (O[0] * 1.35, O[1] * 1.35), "EDGE", 1.0, "2 3")
    i1 = unit(sc, Q, a, 0.5, S(bold("i"), "1"), off=(14, 2))
    unit(sc, Q, a + 90, 0.5, S(bold("j"), "1"), off=(-14, -6))
    sc.angle(Q, 0.22, 0, a, "ωt", name_r=0.33)
    sc.angle(Q, 0.24, 90, a + 90, "ωt", name_r=0.36)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos ωt", "TEXT", "middle", 14, dy=18)
    sc.label((0.0, i1[1]), "sin ωt", "TEXT", "start", 14, dx=8, dy=-6)
    # origin O of S1 and point B
    sc.dotp(O, 4.5)
    sc.label(O, "O", "HEAD", "start", 17, dx=8, dy=20)
    sc.dotp(B, 4.5)
    sc.label(B, "B", "HEAD", "end", 17, dx=-10, dy=14)
    unit(sc, O, a + 90, 0.40, S(bold("v"), "0", "O"), "ACC", off=(-6, -12))
    unit(sc, O, a + 180, 0.25, S(bold("a"), "0", "O"), "ACC", off=(14, 20))
    sc.note((-0.45, -1.12), "circle of radius R", "TEXT", "middle", 13)
    sc.note((0.55, -1.15), "view from +z", "TEXT", "start", 13)
    sc.note((0.55, -1.27), "ω > 0: counter-clockwise", "TEXT", "start", 13)
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


@figure("p30-fbd",
        "Free-body diagram of the particle in the turning frame: top, the plane of the arc with the spring force, the "
        "normal reaction and the inertia force of the rotation; bottom, the view from above with the Coriolis force and "
        "the binormal reaction",
        r"Forces on $P$ in $S_1$. In the plane of the arc: the spring towards $B$, the reaction $N_n\,\mathbf e_n$ and the "
        r"sum of the origin and centrifugal forces, $m\omega^2\rho\,\mathbf i_1$ (dashed, inertia), away from the "
        r"rotation axis. Seen from above: the Coriolis force along $\mathbf j_1$ (dashed, inertia) and the binormal "
        r"reaction, which balance each other.")
def fbd():
    k = 225.0
    sc = Scene(720, 830, (490, 185), k)
    RY = -(640 - 185) / k                               # world y of the plane trace of the lower panel (pixel y = 640)
    O = (0.0, 0.0)
    P = (-math.sin(PHI), -math.cos(PHI))
    B = (-2.0, 0.0)
    et = (-math.cos(PHI), math.sin(PHI))
    en = (math.sin(PHI), math.cos(PHI))
    # ---- upper panel: plane X1Z1, j1 = e_b into the paper
    sc.line((-1.0, -0.88), (-1.0, 0.58), "EDGE", 1.4, "10 3 2 3")
    sc.label((-1.0, 0.18), "rotation axis", "TEXT", "end", 15, dx=-10, dy=0)
    spin_about_vertical(sc, (-1.0, 0.46), 0.15, 0.045, "ω")
    sc.curve(lambda s: (-math.sin(s), -math.cos(s)), 0.0, math.pi / 2, col="HEAD", w=3.0)
    sc.spring(B, P, coils=8, amp=6.0)
    sc.dotp(B, 4.5)
    sc.label(B, "B", "HEAD", "middle", 17, dy=-12)
    sc.label(O, "O", "HEAD", "start", 17, dx=12, dy=-12)
    axis_in(sc, O, None, col="BLUE")
    sc.label(O, bold("j") + S("", "1") + " = " + bold("e") + S("", "b"), "BLUE", "end", 16, weight="700", dx=-16, dy=5)
    unit(sc, O, 0, 0.36, bold("i") + S("", "1"), off=(4, 22))
    unit(sc, O, 90, 0.36, bold("k") + S("", "1"), off=(-16, 4))
    # distance from P to the rotation axis
    sc.dashed(P, (P[0], -0.86))
    sc.dim((-1.0, -0.86), (P[0], -0.86), "", size=14)
    sc.label((-1.0, -0.86), "ρ = R(1 − sin φ)", "TEXT", "end", 15, dx=-8, dy=5)
    # path basis (orange) at P
    unit(sc, P, 130, 0.33, bold("e") + S("", "t"), "ACC", off=(12, -6))
    unit(sc, P, 40, 0.33, bold("e") + S("", "n"), "ACC", off=(-12, -8))
    # spring force along P -> B, shifted off the spring (below it)
    dx, dy = B[0] - P[0], B[1] - P[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    s0 = (P[0] - uy * 0.09, P[1] + ux * 0.09)
    s1 = (s0[0] + 0.7 * ux, s0[1] + 0.7 * uy)
    sc.vec(s0, s1, None, "PINK", 2.8, head=11)
    sc.label(s1, S(bold("F"), "K") + " = −K BP", "PINK", "end", 16, weight="700", dx=-2, dy=26)
    # reaction along e_n (parallel offset, below the inertia arrow's side)
    n0 = (P[0] - et[0] * 0.075, P[1] - et[1] * 0.075)
    n1 = (n0[0] + 0.5 * en[0], n0[1] + 0.5 * en[1])
    sc.vec(n0, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, S(bold("N"), "n") + " " + S(bold("e"), "n"), "PINK", "start", 16, weight="700", dx=8, dy=-6)
    sc.note(n1, "(sign from part (b))", "PINK", "start", 13, dx=8, dy=12)
    # inertia force, horizontal away from the axis
    h0 = (P[0], P[1] - 0.075)
    h1 = (h0[0] + 0.45, h0[1])
    _dvec(sc, h0, h1, "PINK", 2.6)
    sc.label(h1, S(bold("F"), "A") + " + " + S(bold("F"), "C") + " = m ω² ρ " + bold("i") + S("", "1"), "PINK", "start", 16,
             weight="700", dx=10, dy=4)
    sc.label(h1, "(inertia)", "PINK", "start", 14, dx=10, dy=22)
    sc.mass(P, "P", r=7, name_off=(-14, 26))
    sc.note((-2.1, -1.12), "plane X₁Z₁ of the arc", "TEXT", "start", 13)
    # ---- lower panel: view from above, k1 out of the paper, j1 up the page
    def R(x, y):
        return (x, RY + y)
    rho = 1 - math.sin(PHI)
    q0 = -0.889
    Q = R(q0, 0.0)
    Bq = R(q0 - 1.0, 0.0)
    Oq = R(q0 + 1.0, 0.0)
    Pq = R(q0 + rho, 0.0)
    sc.line((Bq[0] - 0.15, Bq[1]), (Oq[0] + 0.15, Oq[1]), "HEAD", 5.0)
    sc.dotp(Bq, 4.5)
    sc.label(Bq, "B", "HEAD", "middle", 17, dy=-16)
    sc.dotp(Oq, 4.5)
    sc.label(Oq, "O", "HEAD", "middle", 17, dy=-16)
    sc.note((Bq[0] - 0.15, Bq[1]), "plane of the arc,", "TEXT", "start", 14, dy=34)
    sc.note((Bq[0] - 0.15, Bq[1]), "seen from above", "TEXT", "start", 14, dy=52)
    axis_out(sc, Q, None, "BLUE")
    sc.label(Q, "Q", "HEAD", "end", 17, dx=-14, dy=28)
    sc.label(Q, bold("k") + S("", "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-14, dy=48)
    unit(sc, Q, 90, 0.5, bold("j") + S("", "1"), off=(-14, -2))
    unit(sc, (Oq[0] + 0.28, Oq[1]), 0, 0.45, bold("i") + S("", "1"), off=(2, 22))
    sc.spin(Q, 0.30, 105, 165, "ω", name_r=0.43)
    # forces at P, along j1
    _dvec(sc, (Pq[0], Pq[1] + 0.06), (Pq[0], Pq[1] + 0.62), "PINK", 2.6)
    sc.label((Pq[0], Pq[1] + 0.62), S(bold("F"), "COR") + " = 2 m ω R cos φ φ̇ " + bold("j") + S("", "1"), "PINK", "start", 16,
             weight="700", dx=12, dy=2)
    sc.label((Pq[0], Pq[1] + 0.62), "(inertia)", "PINK", "start", 14, dx=12, dy=20)
    sc.vec((Pq[0], Pq[1] - 0.06), (Pq[0], Pq[1] - 0.62), None, "PINK", 2.8, head=11)
    sc.label((Pq[0], Pq[1] - 0.62), S(bold("N"), "b") + " " + S(bold("e"), "b") + " = −2 m ω R cos φ φ̇ " + bold("j") + S("", "1"),
             "PINK", "start", 16, weight="700", dx=12, dy=4)
    sc.mass(Pq, None, r=7)
    sc.label(Pq, "P (seen from above)", "HEAD", "start", 16, dx=12, dy=26)
    return sc


@figure("p30-barrier",
        "Barrier function U of the motion along the arc with alpha equal to one quarter, with the levels of three values "
        "of beta squared",
        r"The energy integral reads $\dot\phi^2 = \omega^2[\beta^2 - U(\phi)]$: the particle moves only where $U$ lies "
        r"below $\beta^2$. Below one quarter it turns back at $\phi^*$; at one quarter it creeps towards the top at "
        r"$\pi/6$; above it it crosses the barrier and reaches $\pi/2$.")
def barrier():
    sx, sy = 440.0, 1500.0                                  # px per rad, px per unit of U
    x0, y0 = 90.0, 560.0                                    # pixel of (phi, U) = (0, 0)
    sc = Scene(900, 630, (x0, y0), 1.0)

    def Q(x, y):
        return (x * sx, y * sy)

    def U(f):
        return math.sin(f) * (1 - math.sin(f))
    xm = math.pi / 2
    ylo, yhi = -0.02, 0.33
    # axes
    sc.vec(Q(0, ylo), Q(0, yhi), None, "EDGE", 1.6, head=9)
    sc.vec(Q(-0.04, 0), Q(xm + 0.2, 0), None, "EDGE", 1.6, head=9)
    for v in (0.1, 0.2, 0.25, 0.3):
        sc.line(Q(0, v), Q(xm, v), "EDGE", 0.6, "2 4")
        sc.line(Q(0, v), Q(0.03, v), "EDGE", 1.4)
        sc.label(Q(0, v), f"{v}", "TEXT", "end", 14, italic=False, dx=-8, dy=5)
    sc.label(Q(0, 0), "0", "TEXT", "end", 14, italic=False, dx=-8, dy=5)
    for t, nm in ((math.pi / 6, "π/6"), (math.pi / 3, "π/3"), (math.pi / 2, "π/2")):
        sc.line(Q(t, 0), Q(t, -0.008), "EDGE", 1.4)
        sc.label(Q(t, 0), nm, "TEXT", "middle", 15, italic=False, dy=26)
    sc.label(Q(xm + 0.2, 0), "φ [rad]", "TEXT", "end", 16, dy=28)
    sc.label(Q(0, yhi), "U(φ) = sin φ (1 − sin φ)", "TEXT", "start", 16, dx=12, dy=2)
    # curve
    sc.curve(lambda f: Q(f, U(f)), 0.0, xm, n=200, col="HEAD", w=3.2)
    # levels
    fs = math.asin(0.2)
    sc.line(Q(0, 0.16), Q(fs, 0.16), "BLUE", 2.4, "2 5")
    sc.dashed(Q(fs, 0.16), Q(fs, 0))
    sc.mass(Q(fs, 0.16), None, r=5, col="BLUE")
    sc.label(Q(fs, 0.16), "φ*", "BLUE", "end", 17, weight="700", dx=-10, dy=-10)
    sc.line(Q(0, 0.25), Q(math.pi / 6, 0.25), "ACC", 2.4, "2 5")
    sc.line(Q(0, 0.30), Q(xm, 0.30), "PINK", 2.4, "2 5")
    # the maximum
    sc.circle(Q(math.pi / 6, 0.25), 6.5, "HEAD", 2.2, fill="none")
    # labels of the levels
    sc.label(Q(fs + 0.03, 0.16), "β = 0.4 < 1/2: turns back", "BLUE", "start", 16, weight="700", dy=24)
    sc.label(Q(0.02, 0.25), "β = " + S("β", "c") + " = 1/2", "ACC", "start", 16, weight="700", dy=-10)
    sc.label(Q(xm, 0.30), "β > 1/2: reaches π/2", "PINK", "end", 16, weight="700", dy=-10)
    sc.label(Q(math.pi / 6, 0.25), "unstable equilibrium π/6 (α = 1/4)", "HEAD", "start", 16, weight="700", dx=16, dy=-24)
    # start arrow along the horizontal axis
    sc.vec(Q(0.02, 0.012), Q(0.45, 0.012), None, "GREEN", 2.2, head=10)
    sc.label(Q(0.45, 0.012), "start: φ = 0, φ̇ = βω", "GREEN", "start", 15, weight="700", dx=10, dy=5)
    return sc
