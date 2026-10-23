"""Problem 30: particle on a quarter circumference that turns about the vertical axis x1 = -R, with a spring to B."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

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
