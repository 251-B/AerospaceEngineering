"""Problem 26: heavy particle on a half-circumference wire that turns about the vertical OY."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

TH = math.radians(50)


@figure("p26-wire-plane",
        "Plane of the wire in the moving frame: centre C above O at height a, particle P on the circle at angle theta from "
        "the downward vertical, the right triangle with legs a sin theta and a cos theta, the dashed components of the "
        "position vector, the basis i1, j1 at O and the wire basis e_t, e_n at P",
        r"Plane of the wire, fixed in $S_1$: $\theta$ is measured at $C$ from the downward vertical $CO$. In the shaded "
        r"right triangle the hypotenuse is $|CP| = a$, the leg opposite $\theta$ is $a\sin\theta$ and the adjacent leg is "
        r"$a\cos\theta$; the dashed lines are the components of $\mathbf r_1^P$. $\mathbf i_1, \mathbf j_1$ in blue, "
        r"$\mathbf e_t, \mathbf e_n$ in orange")
def wire_plane():
    sc = Scene(620, 470, (300, 395), 205)
    C = (0.0, 1.0)
    P = (math.sin(TH), 1 - math.cos(TH))
    F = (0.0, P[1])                                       # foot of the horizontal through P on the axis
    # wire: lower half of the circle of centre C
    sc.curve(lambda s: (math.sin(s), 1 - math.cos(s)), -math.pi / 2, math.pi / 2, col="HEAD", w=3.0)
    sc.dashed((-1.0, 1.0), (1.0, 1.0))
    # axes of S1 (the plane of the wire is fixed in S1)
    fixed_axis(sc, (-1.25, 0.0), 0, 2.55, S("X", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.08), 90, 1.66, S("Y", "1") + " ≡ Y", off=(34, 0))
    spin_about_vertical(sc, (0.0, 1.43), 0.17, 0.05, "Ω")
    # key triangle C - F - P
    triangle(sc, [C, F, P])
    right_angle(sc, F, 0, 90, 0.06)
    sc.line(C, P, "HEAD", 1.6)
    sc.label(((C[0] + P[0]) / 2, (C[1] + P[1]) / 2), "a", "TEXT", "start", 17, dx=12, dy=-2)
    sc.label(((C[0] + F[0]) / 2, (C[1] + F[1]) / 2), "a cos θ", "TEXT", "end", 15, dx=-10, dy=-26)
    sc.angle(C, 0.24, -90, -90 + 50, "θ", name_r=0.34)
    # components of r1P (dashed): horizontal a sin(theta), vertical a(1 - cos(theta))
    sc.dashed(F, P)
    sc.label(((F[0] + P[0]) / 2, F[1]), "a sin θ", "TEXT", "middle", 15, dy=20)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0], P[1] / 2), "a(1 − cos θ)", "TEXT", "start", 15, dx=10, dy=6)
    # points
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "end", 17, dx=-10, dy=-8)
    sc.label((0.0, 0.0), "O", "HEAD", "end", 17, dx=-8, dy=20)
    # moving basis at O
    unit(sc, (0.0, 0.0), 0, 0.30, bold("i") + S("", "1"), off=(4, 22))
    unit(sc, (0.0, 0.0), 90, 0.30, bold("j") + S("", "1"), off=(-18, 8))
    # wire basis at P
    unit(sc, P, 50, 0.30, bold("e") + S("", "t"), "ACC", off=(14, -2))
    unit(sc, P, 140, 0.30, bold("e") + S("", "n"), "ACC", off=(-16, 14))
    sc.mass(P, "P", r=7, name_off=(22, 8))
    sc.gravity((1.18, 1.32), 0.32, "g")
    return sc


@figure("p26-top-view",
        "Top view from +Y with j0 = j1 out of the paper: fixed axes i0 and k0 in grey, the axes i1 and k1 of the wire "
        "rotated counter-clockwise by Omega t in blue, the dashed components of i1 and the wire seen edge-on",
        r"View from $+Y$, with $\mathbf j_0 = \mathbf j_1$ out of the paper ($\odot$): $\mathbf k_0$ points down the page. "
        r"$\mathbf i_1, \mathbf k_1$ are $\mathbf i_0, \mathbf k_0$ turned counter-clockwise by $\Omega t$; the components of "
        r"$\mathbf i_1$ are $\cos\Omega t$ along $\mathbf i_0$ and $\sin\Omega t$ along $-\mathbf k_0$ (up the page), hence "
        r"the minus sign")
def top_view():
    sc = Scene(660, 600, (250, 300), 235)
    O = (0.0, 0.0)
    a = 35.0
    ar = math.radians(a)
    # the wire seen edge-on: thick segment along i1 through O, half-length 0.8
    sc.line((-0.8 * math.cos(ar), -0.8 * math.sin(ar)), (0.8 * math.cos(ar), 0.8 * math.sin(ar)), "HEAD", 5.0)
    sc.label((-0.8 * math.cos(ar), -0.8 * math.sin(ar)), "wire (edge-on)", "HEAD", "start", 15, dx=-30, dy=28)
    fixed_axis(sc, O, 0, 1.2, bold("i") + S("", "0"), off=(18, 6))
    fixed_axis(sc, O, -90, 1.0, bold("k") + S("", "0"), off=(18, 4))
    fixed_axis(sc, O, 90, 1.0, "−" + bold("k") + S("", "0"), off=(24, 4), dashed=True)
    i1 = unit(sc, O, a, 1.0, bold("i") + S("", "1"), off=(16, -8))
    unit(sc, O, a - 90, 1.0, bold("k") + S("", "1"), off=(20, 10))
    sc.angle(O, 0.40, 0, a, "Ωt", name_r=0.52)
    sc.angle(O, 0.30, -90, a - 90, "Ωt", name_r=0.42)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] * 0.5, 0.0), "cos Ωt", "TEXT", "middle", 16, dy=26)
    sc.label((0.0, i1[1]), "sin Ωt", "TEXT", "end", 16, dx=-12, dy=5)
    axis_out(sc, O, bold("j") + S("", "0") + " = " + bold("j") + S("", "1"), off=(-62, -8))
    sc.note((0.55, 1.12), "view from +Y", "TEXT", "start", 14)
    sc.note((0.55, 1.0), "Ω > 0: counter-clockwise", "TEXT", "start", 14)
    return sc


def _dvec(sc, a, b, col="PINK", w=2.4, head=10):
    """Dashed arrow (inertia force or auxiliary velocity) from world point a to b."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


@figure("p26-fbd",
        "Free-body diagram of the particle on the turning half-circumference: left, the plane of the wire with the "
        "weight, the in-plane reaction N_n e_n and the centrifugal force; right, the view from above with the "
        "Coriolis force and the normal reaction N_b k1",
        r"Forces on $P$ in $S_1$. In the plane of the wire: weight, $N_n\,\mathbf e_n$ and the centrifugal force "
        r"$m\Omega^2a\sin\theta\,\mathbf i_1$ (dashed, inertia). Normal to it: the reaction $N_b\,\mathbf k_1$ and the "
        r"Coriolis force $2m\Omega a\dot\theta\cos\theta\,\mathbf k_1$ (dashed, inertia), which balance each other.")
def fbd():
    k = 190.0
    sc = Scene(1120, 440, (250, 400), k)
    RX, RY = (790 - 250) / k, (400 - 235) / k           # world offset of the right panel origin (pixel (790, 235))
    P = (math.sin(TH), 1 - math.cos(TH))
    C = (0.0, 1.0)
    # ---- left panel: plane of the wire, k1 out of the paper
    sc.curve(lambda s_: (math.sin(s_), 1 - math.cos(s_)), -math.pi / 2, math.pi / 2, col="HEAD", w=3.0)
    sc.line((0.0, -0.2), (0.0, 1.5), "EDGE", 1.3, "10 3 2 3")
    sc.label((0.0, 1.5), "axis (" + bold("j") + S("", "1") + ")", "TEXT", "start", 15, dx=-34, dy=-28)
    spin_about_vertical(sc, (0.0, 1.3), 0.17, 0.05, "Ω")
    axis_out(sc, (-0.45, 0.5), None, "BLUE")
    sc.label((-0.45, 0.5), bold("k") + S("", "1") + " (⊙)", "BLUE", "start", 16, weight="700", dx=14, dy=5)
    sc.label((0.0, 0.0), "O", "HEAD", "start", 17, dx=8, dy=22)
    sc.dotp((0.0, 0.0), 3.5)
    sc.dotp(C, 3.5)
    sc.label(C, "C", "HEAD", "start", 17, dx=8, dy=-8)
    sc.dashed(C, P)
    sc.dashed((0.0, P[1]), P)
    sc.label((P[0] * 0.5, P[1]), "a sin θ", "TEXT", "middle", 15, dy=-9)
    # forces
    sc.vec(P, (P[0], P[1] - 0.45), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.45), "−m g " + bold("j") + S("", "1"), "PINK", "start", 16, weight="700", dx=10, dy=4)
    en = (-math.sin(TH), math.cos(TH))
    sc.vec(P, (P[0] + 0.4 * en[0], P[1] + 0.4 * en[1]), None, "PINK", 2.8, head=11)
    sc.label((P[0] + 0.4 * en[0], P[1] + 0.4 * en[1]), S("N", "n") + " " + S(bold("e"), "n"), "PINK", "end", 16, weight="700",
             dx=-8, dy=-6)
    _dvec(sc, P, (P[0] + 0.4, P[1]), "PINK", 2.6)
    sc.label((P[0] + 0.4, P[1]), S("F", "C") + " = m Ω² a sin θ " + bold("i") + S("", "1"), "PINK", "start", 15, weight="700",
             dx=10, dy=-4)
    sc.label((P[0] + 0.4, P[1]), "(inertia)", "PINK", "start", 14, dx=10, dy=14)
    unit(sc, P, 50, 0.25, S(bold("e"), "t"), "ACC", off=(18, -6))
    unit(sc, P, 140, 0.25, S(bold("e"), "n"), "ACC", off=(16, 6))
    sc.mass(P, "P", r=7, name_off=(14, 26))
    # ---- right panel: view from above, j1 out of the paper, k1 down the page
    def R(x, y):
        return (RX + x, RY + y)
    xp = P[0]
    sc.line(R(-1.0, 0), R(1.0, 0), "HEAD", 5.0)
    sc.label(R(-1.0, 0), "view from above: the wire is seen edge-on", "TEXT", "start", 15, dy=150, dx=-4)
    unit(sc, R(0, 0), 0, 0.3, bold("i") + S("", "1"), off=(4, -12))
    unit(sc, R(0, 0), -90, 0.3, bold("k") + S("", "1"), off=(-18, 8))
    axis_out(sc, R(0, 0), None, "BLUE")
    sc.label(R(0, 0), bold("j") + S("", "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-16, dy=22)
    sc.spin(R(0, 0), 0.32, 30.0, 150.0, "Ω", name_r=0.44)
    sc.mass(R(xp, 0), "P", r=7, name_off=(-20, -12))
    _dvec(sc, R(xp + 0.04, -0.05), R(xp + 0.04, -0.5), "PINK", 2.6)
    sc.label(R(xp + 0.04, -0.5), S("F", "COR") + " = 2mΩaθ̇ cos θ " + bold("k") + S("", "1"), "PINK", "end", 15,
             weight="700", dx=-10, dy=10)
    sc.label(R(xp + 0.04, -0.5), "(inertia)", "PINK", "end", 14, dx=-10, dy=28)
    sc.vec(R(xp - 0.04, 0.05), R(xp - 0.04, 0.4), None, "PINK", 2.8, head=11)
    sc.label(R(xp - 0.04, 0.4), S("N", "b") + " " + bold("k") + S("", "1") + " = −2mΩaθ̇ cos θ " + bold("k") + S("", "1"),
             "PINK", "middle", 15, weight="700", dx=0, dy=-12)
    _dvec(sc, R(xp + 0.14, 0.05), R(xp + 0.14, 0.35), "GREEN", 2.2)
    sc.label(R(xp + 0.14, 0.35), "transport velocity", "GREEN", "start", 14, weight="700", dx=12, dy=4)
    sc.label(R(xp + 0.14, 0.35), "−Ω a sin θ " + bold("k") + S("", "1"), "GREEN", "start", 14, weight="700", dx=12, dy=22)
    return sc
