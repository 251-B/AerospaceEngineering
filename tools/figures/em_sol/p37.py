"""Problem 37: particle on an elliptic cone that spins about its vertical axis Oz1."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

WT = 35.0          # angle turned by the cone, deg (drawing value)
BETA = 50.0        # parameter beta of the drawn point, deg


@figure("p37-top-view",
        "Top view from +z0 with k0 out of the paper: fixed axes i0 to the right and j0 up in grey, the cone axes i1 and "
        "j1 turned counter-clockwise by Omega t in blue, and the shaded right triangles that give their components",
        r"View from $+z_0$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$), so $\mathbf j_0 = \mathbf k_0\times"
        r"\mathbf i_0$ points up. $\mathbf i_1, \mathbf j_1$ are $\mathbf i_0, \mathbf j_0$ turned counter-clockwise by "
        r"$\Omega t$: $\mathbf i_1$ has legs $\cos\Omega t$ along $\mathbf i_0$ and $\sin\Omega t$ along $\mathbf j_0$; "
        r"$\mathbf j_1$ has legs $\cos\Omega t$ along $\mathbf j_0$ and $\sin\Omega t$ along $-\mathbf i_0$, hence its minus sign")
def top_view():
    sc = Scene(520, 430, (250, 300), 165)
    O = (0.0, 0.0)
    fixed_axis(sc, O, 0, 1.2, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.2, bold("j") + S("", "0"), off=(16, 2))
    fixed_axis(sc, O, 180, 1.0, "−" + bold("i") + S("", "0"), off=(-8, -12), dashed=True)
    i1 = (math.cos(math.radians(WT)), math.sin(math.radians(WT)))
    j1 = (-math.sin(math.radians(WT)), math.cos(math.radians(WT)))
    triangle(sc, [O, (i1[0], 0.0), i1])
    triangle(sc, [O, (0.0, j1[1]), j1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(j1, (0.0, j1[1]))
    right_angle(sc, (i1[0], 0.0), 180, 90, 0.06)
    right_angle(sc, (0.0, j1[1]), 270, 180, 0.06)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -4))
    unit(sc, O, 90 + WT, 1.0, bold("j") + S("", "1"), off=(-12, -10))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((i1[0], i1[1] / 2), "sin Ωt", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((j1[0] / 2, j1[1]), "sin Ωt", "TEXT", "middle", 15, dy=-9)
    sc.label((0.0, j1[1] * 0.42), "cos Ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.angle(O, 0.30, 0, WT, "Ωt", name_r=0.44)
    sc.angle(O, 0.24, 90, 90 + WT, "Ωt", name_r=0.37)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-46, 30))
    sc.note((0.55, -0.55), "view from +z₀", "TEXT", "start", 13)
    sc.note((0.55, -0.67), "Ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc


@figure("p37-section",
        "Horizontal section of the cone at height zeta seen from above: the ellipse with semi-axes zeta along i1 and "
        "2 zeta along j1, the dashed auxiliary circle of radius zeta, the point B of the circle at polar angle beta, the "
        "shaded right triangle with legs zeta cos beta and zeta sin beta, the point P of the ellipse with the same x1 and "
        "twice the height, and the tangent vector e_beta at P",
        r"Section $z_1 = \zeta$ seen from above ($\mathbf k_1$ out of the paper). $\beta$ is the polar angle of the point "
        r"$B$ of the dashed auxiliary circle of radius $\zeta$; in the shaded triangle the legs are $\zeta\cos\beta$ and "
        r"$\zeta\sin\beta$. The projection of $P$ has the same $x_1 = \zeta\cos\beta$ and twice the height, "
        r"$y_1 = 2\zeta\sin\beta$; $\mathbf e_\beta$ (orange) is tangent to the ellipse")
def section():
    sc = Scene(560, 560, (280, 280), 115)
    O = (0.0, 0.0)
    z = 1.0
    b = math.radians(BETA)
    sc.curve(lambda s: (z * math.cos(s), 2 * z * math.sin(s)), 0, 2 * math.pi, col="HEAD", w=2.4)
    sc.circle(O, z, "EDGE", 1.2, dash="5 4")
    fixed_axis(sc, (-1.35, 0.0), 0, 2.75, bold("i") + S("", "1"), off=(16, 5))
    fixed_axis(sc, (0.0, -2.25), 90, 4.5, bold("j") + S("", "1"), off=(16, 4))
    B = (z * math.cos(b), z * math.sin(b))
    P = (z * math.cos(b), 2 * z * math.sin(b))
    F = (B[0], 0.0)
    triangle(sc, [O, F, B])
    sc.line(O, B, "EDGE", 1.4)
    right_angle(sc, F, 180, 90, 0.07)
    sc.dashed(F, P)
    sc.dashed(P, (0.0, P[1]))
    sc.angle(O, 0.3, 0, BETA, "β", name_r=0.43)
    sc.label((B[0] / 2, 0.0), "ζ cos β", "TEXT", "middle", 15, dy=20)
    sc.line(B, (1.3, B[1]), "EDGE", 1.0, "2 3")
    sc.dim((1.22, 0.0), (1.22, B[1]), "ζ sin β", off=(34, 5))
    sc.label((0.0, P[1]), "2ζ sin β", "TEXT", "end", 15, dx=-10, dy=5)
    sc.dotp(B, 4.0)
    sc.label(B, "B", "HEAD", "end", 17, dx=-8, dy=-26)
    t = (-math.sin(b), 2 * math.cos(b))
    tn = math.hypot(*t)
    unit(sc, P, math.degrees(math.atan2(t[1], t[0])), 0.55, bold("e") + S("", "β"), "ACC", off=(-6, -12))
    sc.mass(P, "P", r=6, name_off=(16, -8))
    sc.note((-2.4, -1.5), "auxiliary circle, radius ζ", "TEXT", "start", 13)
    sc.note((0.62, -1.75), "ellipse: semi-axes ζ and 2ζ", "TEXT", "start", 13)
    axis_out(sc, (-1.05, 1.95), bold("k") + S("", "1"), off=(26, 6))
    assert tn > 0
    return sc


@figure("p37-sections",
        "The two principal vertical sections of the cone: in the plane x1 z1 the generators make 45 degrees with the "
        "horizontal, with a shaded right triangle of legs zeta and zeta and hypotenuse zeta root 2; in the plane y1 z1 they "
        "rise one unit for two across, with legs 2 zeta and zeta and hypotenuse zeta root 5. At P the generator vector "
        "e_zeta and the normal n are drawn in orange",
        r"Principal vertical sections. Left, plane $x_1z_1$ ($\beta = 0$): legs $\zeta$ and $\zeta$, hypotenuse "
        r"$\zeta\sqrt2$, $\mathbf e_\zeta = \mathbf i_1 + \mathbf k_1$. Right, plane $y_1z_1$ ($\beta = \pi/2$): legs "
        r"$2\zeta$ and $\zeta$, hypotenuse $\zeta\sqrt5$, $\mathbf e_\zeta = 2\mathbf j_1 + \mathbf k_1$. The normal "
        r"$\mathbf n$ is perpendicular to the generator in each plane")
def sections():
    sc = Scene(850, 330, (150, 250), 82)
    # left panel: plane x1 z1
    O1 = (0.0, 0.0)
    fixed_axis(sc, (-1.7, 0.0), 0, 3.3, S("x", "1"), off=(14, 5))
    fixed_axis(sc, O1, 90, 2.15, S("z", "1"), off=(14, 4))
    sc.line((-1.6, 1.6), O1, "HEAD", 2.4)
    sc.line(O1, (1.6, 1.6), "HEAD", 2.4)
    P1 = (1.0, 1.0)
    triangle(sc, [O1, (1.0, 0.0), P1])
    sc.dashed((1.0, 0.0), P1)
    right_angle(sc, (1.0, 0.0), 180, 90, 0.12)
    sc.label((0.5, 0.0), "ζ", "TEXT", "middle", 15, dy=20)
    sc.label((1.0, 0.5), "ζ", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((0.5, 0.5), "ζ√2", "TEXT", "end", 15, dx=-8, dy=-6)
    unit(sc, P1, 45, 0.65, bold("e") + S("", "ζ"), "ACC", off=(14, 0))
    unit(sc, P1, 135, 0.65, bold("n"), "ACC", off=(-8, -8))
    sc.mass(P1, "P", r=6, name_off=(18, 10))
    sc.note((-1.7, -0.62), "plane x₁z₁ (β = 0)", "TEXT", "start", 13)
    # right panel: plane y1 z1
    O2 = (5.0, 0.0)
    fixed_axis(sc, (2.2, 0.0), 0, 5.6, S("y", "1"), off=(14, 5))
    fixed_axis(sc, O2, 90, 2.15, S("z", "1"), off=(14, 4))
    sc.line((O2[0] - 2.6, 1.3), O2, "HEAD", 2.4)
    sc.line(O2, (O2[0] + 2.6, 1.3), "HEAD", 2.4)
    P2 = (O2[0] + 2.0, 1.0)
    triangle(sc, [O2, (P2[0], 0.0), P2])
    sc.dashed((P2[0], 0.0), P2)
    right_angle(sc, (P2[0], 0.0), 180, 90, 0.12)
    sc.label((O2[0] + 1.0, 0.0), "2ζ", "TEXT", "middle", 15, dy=20)
    sc.label((P2[0], 0.5), "ζ", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((O2[0] + 1.0, 0.5), "ζ√5", "TEXT", "end", 15, dx=-6, dy=-10)
    a = math.degrees(math.atan2(1, 2))
    unit(sc, P2, a, 0.65, bold("e") + S("", "ζ"), "ACC", off=(14, -2))
    unit(sc, P2, a + 90, 0.65, bold("n"), "ACC", off=(-10, -6))
    sc.mass(P2, "P", r=6, name_off=(18, 10))
    sc.note((2.6, -0.62), "plane y₁z₁ (β = π/2)", "TEXT", "start", 13)
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


@figure("p37-fbd",
        "Free-body diagram of the particle on the spinning cone at the start: top, the vertical principal plane y1 z1 "
        "with the weight, the normal reaction and the centrifugal force; bottom, the view from above with the relative "
        "velocity, the Coriolis force and the centrifugal force",
        r"Forces on $P$ in $S_1$ at the start ($\zeta = 1$, $\beta = \pi/2$). In the vertical plane $y_1z_1$: the "
        r"weight, the reaction $N\,\mathbf n$ normal to the generator and the centrifugal force (dashed), away from the "
        r"axis. Seen from above: the Coriolis force $-2m\Omega\,\mathbf k_1\times\mathbf v_1^P$ (dashed) for the initial "
        r"velocity $\mathbf i_1$.")
def fbd():
    k = 105.0
    sc = Scene(790, 800, (285, 265), k)
    O = (0.0, 0.0)
    P = (2.0, 1.0)
    n = (-1 / math.sqrt(5), 2 / math.sqrt(5))
    ez = (2 / math.sqrt(5), 1 / math.sqrt(5))
    # ---- upper panel: plane y1 z1, i1 out of the paper
    sc.line((-2.5, 1.25), O, "HEAD", 3.0)
    sc.line(O, (2.5, 1.25), "HEAD", 3.0)
    sc.line((0.0, -0.1), (0.0, 1.6), "EDGE", 1.4, "10 3 2 3")
    spin_about_vertical(sc, (0.0, 1.45), 0.3, 0.08, "Ω")
    axis_out(sc, O, None, "BLUE")
    sc.label(O, S(bold("i"), "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-16, dy=24)
    sc.label(O, "O", "HEAD", "start", 17, dx=14, dy=24)
    unit(sc, O, 0, 0.4, S(bold("j"), "1"), off=(4, 22))
    unit(sc, O, 90, 0.4, S(bold("k"), "1"), off=(-16, 4))
    # forces at P
    sc.vec(P, (P[0], P[1] - 0.9), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.9), "W = −m g " + S(bold("k"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=6)
    n1 = (P[0] + 1.0 * n[0], P[1] + 1.0 * n[1])
    sc.vec(P, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, "N " + bold("n"), "PINK", "end", 16, weight="700", dx=-8, dy=-6)
    f1 = (P[0] + 0.7, P[1])
    _dvec(sc, P, f1, "PINK", 2.6)
    sc.label(f1, S(bold("F"), "C") + " = m Ω² ζ", "PINK", "start", 16, weight="700", dx=10, dy=22)
    sc.label(f1, "(cos β " + S(bold("i"), "1") + " + 2 sin β " + S(bold("j"), "1") + ")", "PINK", "start", 16, weight="700", dx=10, dy=41)
    sc.label(f1, "(inertia)", "PINK", "start", 14, dx=10, dy=59)
    e1 = (P[0] + 0.6 * ez[0], P[1] + 0.6 * ez[1])
    sc.vec(P, e1, None, "ACC", 2.6, head=11)
    sc.label(e1, S(bold("e"), "ζ"), "ACC", "start", 16, weight="700", dx=8, dy=-6)
    right_angle(sc, P, math.degrees(math.atan2(ez[1], ez[0])), math.degrees(math.atan2(n[1], n[0])), 0.11)
    sc.mass(P, "P", r=7, name_off=(-14, 30))
    sc.note((-2.5, -0.35), "vertical plane y₁z₁ (β = π/2, ζ = 1)", "TEXT", "start", 13)
    # ---- lower panel: view from above, k1 out of the paper
    f = 0.65
    RY = -(610 - 265) / k                               # world y of O in the lower panel (pixel y = 610)

    def R(x, y):
        return (f * x, RY + f * y)
    Oq = R(0.0, 0.0)
    sc.curve(lambda t: R(math.cos(t), 2 * math.sin(t)), 0.0, 2 * math.pi, n=160, col="HEAD", w=3.0)
    axis_out(sc, Oq, None, "BLUE")
    sc.label(Oq, S(bold("k"), "1") + " (⊙)", "BLUE", "start", 15, weight="700", dx=14, dy=26)
    sc.label(Oq, "O", "HEAD", "end", 17, dx=-12, dy=-10)
    unit(sc, Oq, 0, 0.35, S(bold("i"), "1"), off=(6, -12))
    unit(sc, Oq, 90, 0.35, S(bold("j"), "1"), off=(-16, 4))
    sc.arc(Oq, 0.32, 200, 255, "GREEN", 1.8, head=True)
    sc.label(Oq, "Ω", "GREEN", "middle", 16, weight="700", dx=-42, dy=46)
    Pq = R(0.0, 2.0)
    sc.mass(Pq, None, r=7)
    sc.label(Pq, "P (seen from above)", "HEAD", "end", 16, dx=-22, dy=-12)
    # initial relative velocity: tangent to the ellipse, along i1
    v1 = (Pq[0] + 0.7, Pq[1])
    sc.vec(Pq, v1, None, "ACC", 2.8, head=11)
    sc.label(v1, S(bold("v"), "1", "P") + "(0) = " + S(bold("i"), "1"), "ACC", "start", 16, weight="700", dx=10, dy=-6)
    tip = (Pq[0] + 0.07, Pq[1] - 0.75)
    _dvec(sc, (Pq[0] + 0.07, Pq[1] - 0.06), tip, "PINK", 2.6)
    lab = (Pq[0] + 0.07 + 0.95, tip[1])
    sc.line((tip[0] + 0.05, tip[1]), (lab[0] - 0.05, lab[1]), "EDGE", 1.0, "2 3")
    sc.label(lab, S(bold("F"), "COR") + " = −2 m Ω " + S(bold("k"), "1") + " × " + S(bold("v"), "1", "P") + " (inertia)",
             "PINK", "start", 16, weight="700", dx=0, dy=-8)
    sc.label(lab, "= −2 m Ω " + S(bold("j"), "1") + "  (drawn at the start)", "PINK", "start", 16, weight="700", dx=0, dy=12)
    _dvec(sc, (Pq[0] - 0.07, Pq[1] + 0.06), (Pq[0] - 0.07, Pq[1] + 0.6), "PINK", 2.6)
    sc.label((Pq[0] - 0.07, Pq[1] + 0.6), S(bold("F"), "C") + " (inertia)", "PINK", "end", 16, weight="700", dx=-6, dy=-4)
    sc.note((-2.5, RY - 1.62), "view from above: elliptic section at ζ = 1 (semi-axes 1 and 2)", "TEXT", "start", 13)
    return sc
