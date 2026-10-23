"""Problem 26: heavy particle on a half-circumference wire that turns about the vertical OY."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

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
        "Top view from +Y with j pointing out of the paper: the inertial axes i to the right and k downwards in grey, the "
        "axes i1 and k1 of the wire rotated counter-clockwise by Omega t in blue, and the dashed components cos Omega t "
        "along i and sin Omega t along minus k",
        r"View from $+Y$, with $\mathbf j = \mathbf j_1$ out of the paper ($\odot$): then $\mathbf k = \mathbf i\times\mathbf j$ "
        r"points down the page. $\mathbf i_1, \mathbf k_1$ are $\mathbf i, \mathbf k$ turned counter-clockwise by "
        r"$\Omega t$; the components of $\mathbf i_1$ are $\cos\Omega t$ along $\mathbf i$ and $\sin\Omega t$ along "
        r"$-\mathbf k$ (up the page), hence the minus sign")
def top_view():
    sc = Scene(480, 440, (170, 215), 165)
    O = (0.0, 0.0)
    a = 35.0
    fixed_axis(sc, O, 0, 1.15, bold("i"), off=(14, 5))
    fixed_axis(sc, O, -90, 1.0, bold("k"), off=(14, 4))
    fixed_axis(sc, O, 90, 0.95, "−" + bold("k"), off=(18, 4), dashed=True)
    axis_out(sc, O, bold("j") + " = " + bold("j") + S("", "1"), off=(-46, 24))
    i1 = unit(sc, O, a, 1.0, bold("i") + S("", "1"), off=(14, -6))
    unit(sc, O, a - 90, 1.0, bold("k") + S("", "1"), off=(16, 8))
    sc.angle(O, 0.42, 0, a, "Ωt", name_r=0.56)
    sc.angle(O, 0.30, -90, a - 90, "Ωt", name_r=0.43)
    # components of i1
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, i1[1]), "sin Ωt", "TEXT", "end", 15, dx=-12, dy=5)
    sc.note((0.45, 1.0), "view from +Y", "TEXT", "start", 13)
    sc.note((0.45, 0.88), "Ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc
