"""Problem 37: particle on an elliptic cone that spins about its vertical axis Oz1."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

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
