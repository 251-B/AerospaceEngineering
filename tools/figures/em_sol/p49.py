"""Problem 49: particle on a sphere of radius a attracted to a point A at 2a, sphere and A spinning about k0."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold


@figure("p49-top-view",
        "View from +z with k0 = k1 out of the paper: inertial axes i0 and j0 in grey, the rotating axes i1 and j1 turned "
        "counter-clockwise by Omega t in blue, the sphere of radius a seen from above and the attracting point A at "
        "distance 2a along i1",
        r"View from $+z$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$), so $\mathbf j_0$ is $\mathbf i_0$ turned "
        r"$90^\circ$ counter-clockwise. $S_1$ turns $\Omega t$ counter-clockwise: $\mathbf i_1$ has the legs $\cos\Omega t$ "
        r"along $\mathbf i_0$ and $\sin\Omega t$ along $\mathbf j_0$; the tip of $\mathbf j_1$ moves to the side of "
        r"$-\mathbf i_0$, hence $-\sin\Omega t$. $A$ sits on the $\mathbf i_1$ axis at $OA = 2a$")
def top_view():
    a = 30.0
    sc = Scene(560, 470, (230, 300), 115)
    O = (0.0, 0.0)
    d1 = (math.cos(math.radians(a)), math.sin(math.radians(a)))
    sc.circle(O, 1.0, "HEAD", 1.8)
    sc.line(O, (2.35 * d1[0], 2.35 * d1[1]), "BLUE", 1.2, "6 4")
    A = (2.0 * d1[0], 2.0 * d1[1])
    sc.dotp(A, 5.0)
    sc.label(A, "A", "HEAD", "start", 17, dx=8, dy=20)
    fixed_axis(sc, (-1.5, 0.0), 0, 3.6, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.5), 90, 3.05, S(bold("j"), "0"), off=(14, 4))
    axis_out(sc, O, S(bold("k"), "0") + " = " + S(bold("k"), "1"), off=(-62, 50))
    i1 = unit(sc, O, a, 1.25, S(bold("i"), "1"), off=(-4, -14))
    j1 = unit(sc, O, a + 90, 1.25, S(bold("j"), "1"), off=(-12, -8))
    triangle(sc, [O, (i1[0], 0.0), i1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((i1[0], i1[1] / 2), "sin Ωt", "TEXT", "start", 15, dx=8, dy=4)
    sc.dashed(j1, (j1[0], 0.0))
    sc.label((j1[0] / 2, 0.0), "−sin Ωt", "TEXT", "middle", 15, dy=20)
    sc.angle(O, 0.42, 0, a, "Ωt", name_r=0.58)
    sc.angle(O, 0.30, 90, 90 + a, "Ωt", name_r=0.44)
    sc.label((A[0] * 0.78, A[1] * 0.78), "2a", "TEXT", "middle", 15, dx=-8, dy=-16)
    sc.note((-1.75, -1.25), "sphere of radius a (from above)", "TEXT", "start", 13)
    return sc


@figure("p49-axis-view",
        "View along the axis OA with i1 out of the paper: j1 to the right and k1 up in grey, the unit vector u at angle "
        "theta from j1 and the unit vector e_theta perpendicular to it, both in orange, with the shaded right triangle "
        "of u, and the projection P' of the particle at distance a sin phi along u",
        r"View along $OA$, with $\mathbf i_1$ out of the paper ($\odot$): then $\mathbf j_1$ points right and "
        r"$\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ up. The azimuth $\theta$ turns counter-clockwise from $\mathbf j_1$: "
        r"$\mathbf u = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1$ (legs of the shaded triangle) and "
        r"$\mathbf e_\theta = d\mathbf u/d\theta$. $P$ projects onto this plane at $P'$, at distance $a\sin\phi$ from the axis")
def axis_view():
    th = 40.0
    sc = Scene(500, 430, (200, 290), 170)
    O = (0.0, 0.0)
    fixed_axis(sc, (-0.7, 0.0), 0, 2.0, S(bold("j"), "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.5), 90, 1.8, S(bold("k"), "1"), off=(14, 4))
    axis_out(sc, O, S(bold("i"), "1") + " (towards A)", off=(-56, 28))
    u = unit(sc, O, th, 0.75, bold("u"), "ACC", off=(-4, -12))
    unit(sc, O, th + 90, 0.75, S(bold("e"), "θ"), "ACC", off=(-14, -6))
    triangle(sc, [O, (u[0], 0.0), u])
    right_angle(sc, (u[0], 0.0), 180, 90, 0.05)
    sc.dashed(u, (u[0], 0.0))
    sc.label((u[0] / 2, 0.0), "cos θ", "TEXT", "middle", 15, dy=20)
    sc.label((u[0], u[1] / 2), "sin θ", "TEXT", "start", 15, dx=8, dy=4)
    sc.angle(O, 0.30, 0, th, "θ", name_r=0.42)
    Pp = (1.25 * math.cos(math.radians(th)), 1.25 * math.sin(math.radians(th)))
    sc.line(u, Pp, "EDGE", 1.1, "5 4")
    sc.dotp(Pp, 4.5)
    sc.label(Pp, "P′", "HEAD", "start", 17, dx=8, dy=-6)
    sc.label(Pp, "OP′ = a sin φ", "TEXT", "start", 13, dx=10, dy=16)
    return sc


@figure("p49-meridian",
        "Meridian plane that contains the axis OA and the particle: i1 to the right and u up, e_theta out of the paper, the "
        "circle of radius a, the particle P at angle phi from OA, the shaded right triangle with legs a cos phi and a sin phi, "
        "the spherical vectors e_r and e_phi at P in orange and the dashed segment from P to A at 2a",
        r"Meridian plane of $P$ (it contains $\mathbf i_1$ and $\mathbf u$; $\mathbf e_\theta = \mathbf i_1\times\mathbf u$ is "
        r"out of the paper). $\phi$ is measured at $O$ from $OA$: in the shaded triangle the hypotenuse is $a$, the leg "
        r"adjacent to $\phi$ is $a\cos\phi$ along $\mathbf i_1$ and the opposite one $a\sin\phi$ along $\mathbf u$. "
        r"$\mathbf e_r, \mathbf e_\phi$ in orange; the attraction acts along $PA$")
def meridian():
    ph = 60.0
    sc = Scene(720, 420, (200, 240), 150)
    O = (0.0, 0.0)
    P = (math.cos(math.radians(ph)), math.sin(math.radians(ph)))
    A = (2.0, 0.0)
    sc.circle(O, 1.0, "HEAD", 2.2)
    fixed_axis(sc, (-1.25, 0.0), 0, 3.6, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.2), 90, 2.55, bold("u"), off=(16, 4))
    axis_out(sc, O, S(bold("e"), "θ"), off=(-30, -12))
    triangle(sc, [O, (P[0], 0.0), P])
    right_angle(sc, (P[0], 0.0), 180, 90, 0.07)
    sc.line(O, P, "HEAD", 1.4)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0] / 2, 0.0), "a cos φ", "TEXT", "middle", 14, dy=20)
    sc.label((P[0], P[1] / 2), "a sin φ", "TEXT", "start", 13, dx=7, dy=4)
    sc.label((P[0] / 2, P[1] / 2), "a", "TEXT", "end", 16, dx=-8, dy=-6)
    sc.angle(O, 0.26, 0, ph, "φ", name_r=0.38)
    sc.line(P, A, "PINK", 1.4, "6 4")
    sc.label(((P[0] + A[0]) / 2, (P[1] + A[1]) / 2), "PA", "PINK", "start", 14, dx=8, dy=-6)
    sc.dotp(A, 5.0)
    sc.label(A, "A", "HEAD", "middle", 17, dy=24)
    sc.label((1.0, 0.0), "2a = OA", "TEXT", "start", 13, dx=36, dy=40)
    unit(sc, P, ph, 0.5, S(bold("e"), "r"), "ACC", off=(10, -6))
    unit(sc, P, ph + 90, 0.5, S(bold("e"), "φ"), "ACC", off=(-8, -12))
    sc.mass(P, "P", r=7, name_off=(-18, 4))
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=22)
    return sc


def _dvec(sc, a, b, col="PINK", w=2.4, head=10):
    """Dashed arrow (inertia force) from world point a to b."""
    from figures.svgkit import arrow_head
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


def _open_pt(sc, p, r=6):
    sc.circle(p, r / sc.k, "HEAD", 1.8, fill="none")


@figure("p49-fbd",
        "Free-body diagrams of the particle on the rotating sphere: top, the meridian plane through the axis and A at the "
        "off-axis equilibrium E3 with the attraction towards A, the centrifugal inertia force and the outward reaction, "
        "and the other equilibria marked; bottom, the view from above with the Coriolis inertia force of a moving particle",
        r"Forces seen from $S_1$. Top: at the equilibrium $E_3$ ($m\Omega^2/k = 4$) in the meridian plane through $A$, the "
        r"attraction $k\,\overrightarrow{PA}$, the centrifugal force (dashed), horizontal and away from the axis, and the "
        r"reaction $N\,\mathbf e_r$ with $N = ka$; the other equilibria are marked. Bottom: the Coriolis force (dashed) of "
        r"a moving particle, normal to $\mathbf k_1$ and to the relative velocity")
def fbd():
    k = 140.0
    sc = Scene(900, 1000, (360, 330), k)
    ph = math.radians(120.0)
    P = (math.cos(ph), math.sin(ph))
    A = (2.0, 0.0)
    O = (0.0, 0.0)
    # ---------------- upper panel: meridian plane x1 z1 (j1 into the paper)
    sc.circle(O, 1.0, "HEAD", 2.4)
    sc.vec((-1.5, 0.0), (2.5, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((2.5, 0.0), S(bold("i"), "1"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    sc.line((0.0, -1.45), (0.0, 1.45), "EDGE", 1.8, "10 3 2 3")
    sc.vec((0.0, 1.45), (0.0, 1.62), None, "EDGE", 1.6, head=8)
    sc.label((0.0, 1.62), S(bold("k"), "1") + " = " + S(bold("k"), "0"), "TEXT", "start", 16, weight="700", dx=10, dy=4)
    sc.note((0.0, -1.45), "axis of rotation", "TEXT", "start", 13, dx=10, dy=14)
    spin_y = 1.85
    from figures.em_solutions import spin_about_vertical
    spin_about_vertical(sc, (0.0, spin_y), 0.2, 0.05, "Ω")
    axis_in(sc, O, None, "BLUE")
    sc.label(O, S(bold("j"), "1") + " (⊗)", "BLUE", "end", 15, weight="700", dx=-14, dy=28)
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=-12)
    sc.dotp(A, 5.0)
    sc.label(A, "A", "HEAD", "middle", 17, dy=-12)
    # the other equilibria
    for pt, nm, off in (((1.0, 0.0), "E₁ (nearest A)", (8, 24)), ((-1.0, 0.0), "E₂", (-10, 24)),
                        ((-0.5, -0.8660254), "E₄", (-12, 18))):
        _open_pt(sc, pt)
        sc.label(pt, nm, "HEAD", "end" if off[0] < 0 else "start", 15, dx=off[0], dy=off[1])
    # distance of P to the axis
    sc.dashed(P, (0.0, P[1]))
    sc.label((-0.14, P[1]), S("x", "1"), "TEXT", "middle", 15, dy=-8)
    sc.note((-2.4, 2.0), "particle P at the equilibrium E₃", "TEXT", "start", 13)
    sc.note((-2.4, 1.87), "x₁ = −2a/Λ = −0.5 a, Λ = m Ω²/k = 4", "TEXT", "start", 13)
    # forces at P
    ur = (P[0], P[1])
    ep = (-math.sin(ph), math.cos(ph))
    dpa = (A[0] - P[0], A[1] - P[1])
    L = math.hypot(*dpa)
    u = (dpa[0] / L, dpa[1] / L)
    f1 = (P[0] + 1.9 * u[0], P[1] + 1.9 * u[1])
    sc.vec(P, f1, None, "PINK", 2.8, head=11)
    sc.label(f1, S(bold("F"), "k") + " = k " + bold("PA"), "PINK", "start", 16, weight="700", dx=10, dy=-2)
    c1 = (P[0] - 0.55, P[1])
    _dvec(sc, P, c1, "PINK", 2.6)
    sc.label(c1, S(bold("F"), "C") + " = m Ω² " + S("x", "1") + " " + S(bold("i"), "1"), "PINK", "end", 16, weight="700", dx=-8, dy=-6)
    sc.label(c1, "(inertia)", "PINK", "end", 14, dx=-8, dy=12)
    n0 = (P[0] - 0.09 * ep[0], P[1] - 0.09 * ep[1])
    n1 = (n0[0] + 0.7 * ur[0], n0[1] + 0.7 * ur[1])
    sc.vec(n0, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, "N " + S(bold("e"), "r") + "  (N = k a)", "PINK", "end", 16, weight="700", dx=-4, dy=-8)
    unit(sc, P, 120, 0.28, S(bold("e"), "r"), "ACC", off=(-14, -6))
    unit(sc, P, 210, 0.28, S(bold("e"), "φ"), "ACC", off=(-14, 12))
    sc.mass(P, None, r=7)
    sc.label(P, "P", "HEAD", "start", 17, dx=10, dy=-10)
    # ---------------- lower panel: from above, k1 out of the paper
    s = 1.1
    LY = -(800 - 330) / k

    def R(x, y):
        return (x * s, LY + y * s)
    Oc = R(0.0, 0.0)
    sc.circle(Oc, s, "HEAD", 2.4)
    sc.vec(R(-1.35, 0.0), R(2.45, 0.0), None, "EDGE", 1.4, head=8)
    sc.label(R(2.45, 0.0), S(bold("i"), "1"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    axis_out(sc, Oc, None, "BLUE")
    sc.label(Oc, S(bold("k"), "1") + " (⊙)", "BLUE", "start", 15, weight="700", dx=14, dy=28)
    sc.label(Oc, "O", "HEAD", "end", 17, dx=-12, dy=22)
    unit(sc, Oc, 90, 0.3 * s, S(bold("j"), "1"), off=(-14, 4))
    sc.spin(Oc, 0.55 * s, 115, 200, "Ω", name_r=0.78 * s)
    Ac = R(2.0, 0.0)
    sc.dotp(Ac, 5.0)
    sc.label(Ac, "A", "HEAD", "middle", 17, dy=24)
    Pc = R(0.3, 0.6)
    v1 = (Pc[0] + 0.45 * s, Pc[1])
    sc.vec(Pc, v1, None, "ACC", 2.8, head=11)
    sc.label(v1, "horizontal part of " + S(bold("v"), "1", "P"), "ACC", "start", 15, weight="700", dx=10, dy=-4)
    cf = (Pc[0], Pc[1] - 0.45 * s)
    _dvec(sc, Pc, cf, "PINK", 2.6)
    sc.label(cf, S(bold("F"), "COR"), "PINK", "start", 16, weight="700", dx=8, dy=8)
    sc.mass(Pc, "P", r=6, name_off=(-16, -12))
    nx = Pc[0] + 1.6 * s
    sc.label((nx, LY + 1.25 * s), S(bold("F"), "COR") + " = −2 m Ω " + S(bold("k"), "1") + " × " + S(bold("v"), "1", "P"),
             "PINK", "start", 16, weight="700")
    sc.label((nx, LY + 1.25 * s), "(inertia)", "PINK", "start", 14, dy=18)
    sc.note((nx, LY + 1.25 * s), "Coriolis: normal to k₁ and to v₁;", "TEXT", "start", 13, dy=38)
    sc.note((nx, LY + 1.25 * s), "zero for a particle at rest", "TEXT", "start", 13, dy=54)
    sc.note(R(-1.8, 1.28), "seen from above: moving particle P", "TEXT", "start", 13)
    return sc
