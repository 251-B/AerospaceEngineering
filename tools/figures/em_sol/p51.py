"""Problem 51: heavy particle inside a hollow sphere of centre C = R(j1 + k1), frame S1 spinning about k1."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold


@figure("p51-top-view",
        "View from +z with k0 = k1 out of the paper: inertial axes i0 and j0 in grey, the rotating axes i1 and j1 turned "
        "counter-clockwise by Psi in blue, with the dashed components of i1 and of j1",
        r"View from $+z$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$). $S_1$ has turned the angle $\Psi(t)$, "
        r"$\dot\Psi = \Omega(t)$, counter-clockwise: $\mathbf i_1$ has the legs $\cos\Psi$ along $\mathbf i_0$ and $\sin\Psi$ "
        r"along $\mathbf j_0$; the tip of $\mathbf j_1$ moves to the side of $-\mathbf i_0$, hence $-\sin\Psi$")
def top_view():
    a = 32.0
    sc = Scene(500, 400, (230, 290), 180)
    O = (0.0, 0.0)
    fixed_axis(sc, (-0.95, 0.0), 0, 2.1, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.4), 90, 1.5, S(bold("j"), "0"), off=(14, 4))
    axis_out(sc, O, S(bold("k"), "0") + " = " + S(bold("k"), "1"), off=(-62, 48))
    sc.label(O, "A", "HEAD", "start", 17, dx=12, dy=24)
    i1 = unit(sc, O, a, 1.0, S(bold("i"), "1"), off=(12, -6))
    j1 = unit(sc, O, a + 90, 1.0, S(bold("j"), "1"), off=(-10, -8))
    sc.angle(O, 0.36, 0, a, "Ψ", name_r=0.50)
    sc.angle(O, 0.24, 90, 90 + a, "Ψ", name_r=0.36)
    triangle(sc, [O, (i1[0], 0.0), i1])
    right_angle(sc, (i1[0], 0.0), 180, 90, 0.05)
    sc.dashed(i1, (i1[0], 0.0))
    sc.label((i1[0], i1[1] / 2), "sin Ψ", "TEXT", "start", 15, dx=8, dy=4)
    sc.label((i1[0] / 2, 0.0), "cos Ψ", "TEXT", "middle", 15, dy=20)
    sc.dashed(j1, (j1[0], 0.0))
    sc.label((j1[0] / 2, 0.0), "−sin Ψ", "TEXT", "middle", 15, dy=20)
    return sc


@figure("p51-horizontal",
        "Horizontal plane through C seen from above with k1 out of the paper: the rotation axis through A, the centre C at "
        "distance R along j1, the horizontal unit vector e_h at azimuth theta from i1 with its shaded right triangle, the "
        "unit vector u_theta perpendicular to it, and the projection P' of the particle at distance R cos phi from C",
        r"Horizontal plane through $C$ seen from above ($\mathbf k_1$ out of the paper, $\odot$). The azimuth $\theta$ is "
        r"measured at $C$ from $\mathbf i_1$ towards $\mathbf j_1$: $\mathbf e_h = \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1$ "
        r"(legs of the shaded triangle) and $\mathbf u_\theta = d\mathbf e_h/d\theta$. $P$ projects to $P'$ at distance "
        r"$R\cos\phi$ from $C$; the axis of rotation is at distance $R$ from $C$, on the side of $-\mathbf j_1$")
def horizontal():
    th = 35.0
    sc = Scene(560, 520, (230, 235), 170)
    C = (0.0, 0.0)
    Ax = (0.0, -1.0)
    sc.circle(C, 1.0, "HEAD", 1.6, dash="6 4")
    fixed_axis(sc, (-1.2, 0.0), 0, 2.45, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.0), 90, 2.15, S(bold("j"), "1"), off=(14, 4))
    axis_out(sc, Ax, S(bold("k"), "1") + " axis (through A)", off=(86, 22))
    sc.dim((-0.25, -1.0), (-0.25, 0.0), "R", off=(-14, 4))
    eh = unit(sc, C, th, 0.7, S(bold("e"), "h"), "ACC", off=(-24, -8))
    unit(sc, C, th + 90, 0.7, S(bold("u"), "θ"), "ACC", off=(-16, -6))
    triangle(sc, [C, (eh[0], 0.0), eh])
    right_angle(sc, (eh[0], 0.0), 180, 90, 0.05)
    sc.dashed(eh, (eh[0], 0.0))
    sc.label((eh[0] / 2, 0.0), "cos θ", "TEXT", "middle", 15, dy=20)
    sc.label((eh[0], eh[1] / 2), "sin θ", "TEXT", "start", 15, dx=8, dy=4)
    sc.angle(C, 0.28, 0, th, "θ", name_r=0.40)
    rc = math.cos(math.radians(35.0))                     # R cos(phi) for the phi of the vertical view
    Pp = (rc * math.cos(math.radians(th)), rc * math.sin(math.radians(th)))
    sc.line(eh, Pp, "EDGE", 1.1, "5 4")
    sc.dotp(Pp, 4.5)
    sc.label(Pp, "P′", "HEAD", "start", 17, dx=8, dy=-4)
    sc.label((1.05, 0.78), "CP′ = R cos φ", "TEXT", "start", 13)
    sc.label(C, "C", "HEAD", "end", 17, dx=-10, dy=22)
    sc.note((-1.2, -1.42), "dashed circle: equator of the sphere (radius R)", "TEXT", "start", 13)
    return sc


@figure("p51-vertical",
        "Vertical plane through C that contains e_h: e_h to the right and k1 up in grey, u_theta into the paper, the circle "
        "of radius R, the particle P at elevation phi, the shaded right triangle with legs R cos phi and R sin phi, the "
        "spherical vectors u_r and u_phi at P in orange, and the reaction N towards C",
        r"Vertical plane through $C$ that contains $\mathbf e_h$ ($\mathbf u_\theta$ points into the paper, $\otimes$). The "
        r"elevation $\phi$ is measured at $C$ from the horizontal: in the shaded triangle the hypotenuse is $R$, the leg "
        r"adjacent to $\phi$ is $R\cos\phi$ along $\mathbf e_h$ and the opposite one $R\sin\phi$ along $\mathbf k_1$. "
        r"$\mathbf u_r, \mathbf u_\phi$ in orange; the reaction $\mathbf N = -N\,\mathbf u_r$ (pink) pushes towards $C$")
def vertical():
    ph = 35.0
    sc = Scene(560, 470, (220, 250), 150)
    C = (0.0, 0.0)
    P = (math.cos(math.radians(ph)), math.sin(math.radians(ph)))
    sc.circle(C, 1.0, "HEAD", 2.2)
    fixed_axis(sc, (-1.25, 0.0), 0, 2.55, S(bold("e"), "h"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.25), 90, 2.6, S(bold("k"), "1"), off=(14, 4))
    axis_in(sc, C, S(bold("u"), "θ"), off=(-26, -12))
    triangle(sc, [C, (P[0], 0.0), P])
    right_angle(sc, (P[0], 0.0), 180, 90, 0.06)
    sc.line(C, P, "HEAD", 1.4)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0] / 2, 0.0), "R cos φ", "TEXT", "middle", 14, dy=20)
    sc.label((P[0], P[1] / 2), "R sin φ", "TEXT", "end", 13, dx=-6, dy=6)
    sc.label((P[0] / 2, P[1] / 2), "R", "TEXT", "end", 16, dx=-6, dy=-10)
    sc.angle(C, 0.22, 0, ph, "φ", name_r=0.33)
    unit(sc, P, ph, 0.45, S(bold("u"), "r"), "ACC", off=(10, -6))
    unit(sc, P, ph + 90, 0.45, S(bold("u"), "φ"), "ACC", off=(-6, -12))
    sc.vec(P, (P[0] - 0.42 * math.cos(math.radians(ph)), P[1] - 0.42 * math.sin(math.radians(ph))), bold("N"), "PINK", 2.2,
           name_off=(-4, -14), size=16)
    sc.mass(P, "P", r=7, name_off=(24, 6))
    sc.label(C, "C", "HEAD", "end", 17, dx=-10, dy=22)
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


@figure("p51-fbd",
        "Free-body diagrams of the particle in the rotating hollow sphere: top, the vertical plane through the axis and C "
        "at the admissible equilibrium with the weight, the reaction towards C and the centrifugal inertia force; bottom, "
        "the view from above with the Euler, Coriolis and centrifugal inertia forces of a moving particle",
        r"Forces seen from $S_1$. Top: at the admissible equilibrium ($\theta = \pi/2$, $\phi_1 = -30.3^\circ$ for "
        r"$\Omega = 3$ rad/s, $R = 1$ m) the weight, the reaction $-N\,\mathbf u_r$ towards $C$ and the centrifugal force "
        r"(dashed), away from the axis. Bottom: seen from above, the Euler force (dashed, only while the rate changes), the "
        r"Coriolis force (dashed, normal to the relative velocity) and the centrifugal force")
def fbd():
    k = 150.0
    sc = Scene(900, 1090, (130, 470), k)
    ph = math.radians(-30.3)
    C = (1.0, 1.0)
    P = (C[0] + math.cos(ph), C[1] + math.sin(ph))
    O = (0.0, 0.0)
    # ---------------- upper panel: vertical plane x1 = 0 (i1 out of the paper)
    sc.circle(C, 1.0, "HEAD", 2.4)
    sc.vec((-0.25, 0.0), (3.2, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((3.2, 0.0), S(bold("j"), "1"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    sc.line((0.0, -0.3), (0.0, 2.2), "EDGE", 1.8, "10 3 2 3")
    sc.vec((0.0, 2.2), (0.0, 2.4), None, "EDGE", 1.6, head=8)
    sc.label((0.0, 2.4), S(bold("k"), "1"), "TEXT", "start", 16, weight="700", dx=10, dy=4)
    sc.note((0.0, -0.3), "axis of rotation", "TEXT", "start", 13, dx=10, dy=14)
    from figures.em_solutions import spin_about_vertical
    spin_about_vertical(sc, (0.0, 2.65), 0.2, 0.05, "Ω")
    axis_out(sc, O, None, "BLUE")
    sc.label(O, "A", "HEAD", "end", 17, dx=-12, dy=-10)
    sc.label(O, S(bold("i"), "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-14, dy=26)
    sc.dotp(C, 3.5)
    sc.label(C, "C", "HEAD", "start", 17, dx=8, dy=-8)
    sc.dashed((0.0, P[1]), P)
    sc.label((0.3, P[1]), S("r", "⊥"), "TEXT", "middle", 16, dy=-8)
    sc.angle(C, 0.32, -30.3, 0, "φ₁ < 0", name_r=0.62)
    # forces at P
    w1 = (P[0], P[1] - 0.35)
    sc.vec(P, w1, None, "PINK", 2.8, head=11)
    sc.label(w1, "−mg " + S(bold("k"), "1"), "PINK", "start", 16, weight="700", dx=8, dy=6)
    ur = (math.cos(ph), math.sin(ph))
    n1 = (P[0] - 0.85 * ur[0], P[1] - 0.85 * ur[1])
    sc.vec(P, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, "−N " + S(bold("u"), "r"), "PINK", "middle", 16, weight="700", dx=-20, dy=22)
    sc.label(n1, "(N = 1.98 mg)", "PINK", "middle", 14, dx=-20, dy=38)
    c1 = (P[0] + 0.77, P[1])
    _dvec(sc, P, c1, "PINK", 2.6)
    sc.label(c1, S(bold("F"), "C") + " = m Ω² " + S("r", "⊥"), "PINK", "start", 16, weight="700", dx=10, dy=-6)
    sc.label(c1, "(inertia; 1.71 mg)", "PINK", "start", 14, dx=10, dy=12)
    unit(sc, P, -30.3, 0.3, S(bold("u"), "r"), "ACC", off=(12, 10))
    unit(sc, P, 59.7, 0.3, S(bold("u"), "φ"), "ACC", off=(12, -4))
    sc.mass(P, "P", r=7, name_off=(-14, -10))
    sc.note((0.8, 3.0), "vertical plane x₁ = 0, through the axis and C", "TEXT", "start", 13)
    sc.note((0.8, 2.87), "Ω = 3 rad/s, R = 1 m, branch θ = π/2", "TEXT", "start", 13)
    # ---------------- lower panel: from above, k1 out of the paper
    s = 1.3
    LY = -(1000 - 470) / k

    def R(x, y):
        return (x * s + 1.5, LY + y * s)
    Ac = R(0.0, 0.0)
    Cc = R(0.0, 1.0)
    sc.circle(Cc, s, "HEAD", 2.0, dash="6 4")
    sc.dotp(Cc, 3.5)
    sc.label(Cc, "C", "HEAD", "end", 17, dx=-10, dy=-8)
    axis_out(sc, Ac, None, "BLUE")
    sc.label(Ac, "A", "HEAD", "end", 17, dx=-14, dy=24)
    sc.label(Ac, S(bold("k"), "1") + " (⊙)", "BLUE", "start", 15, weight="700", dx=14, dy=30)
    unit(sc, Ac, 0, 0.35 * s, S(bold("i"), "1"), off=(6, 20))
    unit(sc, Ac, 90, 0.35 * s, S(bold("j"), "1"), off=(-16, 4))
    sc.spin(Ac, 0.3 * s, 200, 265, "Ω(t)", name_r=0.42 * s)
    th = math.radians(35.0)
    Pp = R(0.8 * math.cos(th), 1.0 + 0.8 * math.sin(th))
    rv = (Pp[0] - Ac[0], Pp[1] - Ac[1])
    rn = math.hypot(*rv)
    rh = (rv[0] / rn, rv[1] / rn)                           # from A outwards
    cw = (rh[1], -rh[0])                                    # a quarter turn clockwise
    ut = (-math.sin(th), math.cos(th))                      # u_theta, counter-clockwise about C
    sc.line(Ac, Pp, "EDGE", 1.0, "2 3")
    sc.label(((Ac[0] + Pp[0]) / 2, (Ac[1] + Pp[1]) / 2), S(bold("r"), "1", "P") + "⊥", "TEXT", "end", 15, dx=-8, dy=6)

    def sh(pt, v, d):
        return (pt[0] + d * v[0], pt[1] + d * v[1])
    # horizontal part of the relative velocity along u_theta
    v1 = sh(Pp, ut, 0.55)
    sc.vec(Pp, v1, None, "ACC", 2.8, head=11)
    sc.label(v1, "horizontal part of " + S(bold("v"), "1", "P"), "ACC", "end", 15, weight="700", dx=-8, dy=-6)
    # Coriolis: v turned a quarter turn clockwise
    cv = (ut[1], -ut[0])
    f2 = sh(Pp, cv, 0.55)
    _dvec(sc, Pp, f2, "PINK", 2.6)
    sc.label(f2, S(bold("F"), "COR") + " = −2 m Ω " + S(bold("k"), "1") + " × " + S(bold("v"), "1", "P"), "PINK", "start", 16,
             weight="700", dx=10, dy=-4)
    sc.label(f2, "(inertia)", "PINK", "start", 14, dx=10, dy=13)
    # centrifugal: outwards along A -> P'
    f3 = sh(Pp, rh, 0.75)
    _dvec(sc, Pp, f3, "PINK", 2.6)
    sc.label(f3, S(bold("F"), "C") + " (inertia)", "PINK", "start", 16, weight="700", dx=6, dy=-8)
    # Euler: perpendicular to A -> P', clockwise (drawn for a positive rate)
    f4 = sh(Pp, cw, 0.6)
    _dvec(sc, Pp, f4, "PINK", 2.6)
    sc.label(f4, S(bold("F"), "E") + " = −m Ω̇ " + S(bold("k"), "1") + " × " + S(bold("r"), "1", "P"), "PINK", "start", 16,
             weight="700", dx=10, dy=6)
    sc.label(f4, "(inertia; drawn for Ω̇ > 0)", "PINK", "start", 14, dx=10, dy=24)
    sc.mass(Pp, "P′", r=6, name_off=(-18, 16))
    sc.note(R(-1.2, 2.25), "seen from above: moving particle", "TEXT", "start", 13)
    sc.note(R(-1.2, 2.12), "dashed circle: equator of the sphere", "TEXT", "start", 13)
    return sc
