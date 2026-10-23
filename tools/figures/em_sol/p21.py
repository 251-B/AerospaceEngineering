"""Problem 21: body at rest on the surface of a spinning spherical planet."""
import math

from figures.em_solutions import (axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle,
                                  unit)
from figures.mech import S, Scene, bold

WT = 35.0            # drawn value of Omega t, degrees
LAT = 40.0           # drawn latitude, degrees


@figure("p21-top-view",
        "Equatorial plane seen from above the north pole with k0 = k1 out of the paper: inertial axes i0, j0 in grey, "
        "planet axes i1, j1 turned counter-clockwise by Omega t in blue, with the dashed right triangles of their "
        "components",
        r"View from above the north pole ($\mathbf k_0 = \mathbf k_1$ out of the paper, $\odot$). $\mathbf i_1$ is "
        r"$\mathbf i_0$ turned counter-clockwise by $\Omega t$ (legs $\cos\Omega t$, $\sin\Omega t$); $\mathbf j_1$ turns "
        r"the same angle from $\mathbf j_0$, so its opposite leg points along $-\mathbf i_0$")
def top_view():
    sc = Scene(540, 470, (275, 330), 220)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(WT)), math.sin(math.radians(WT))
    fixed_axis(sc, O, 0, 1.0, bold("i") + S("", "0"), off=(16, 6))
    fixed_axis(sc, O, 90, 1.0, bold("j") + S("", "0"), off=(16, 4))
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), (-s, c)], "BLUE", 0.10)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((0.0, c), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -6))
    unit(sc, O, WT + 90, 1.0, bold("j") + S("", "1"), off=(-14, -8))
    sc.angle(O, 0.30, 0, WT, "Ωt", name_r=0.43)
    sc.angle(O, 0.30, 90, 90 + WT, "Ωt", name_r=0.44)
    sc.label((c / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=22)
    sc.label((c, s * 0.35), "sin Ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, c), "sin Ωt", "TEXT", "middle", 15, dy=-10)
    sc.label((0.0, c / 2), "cos Ωt", "TEXT", "start", 15, dx=8, dy=16)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-58, 4))
    return sc


@figure("p21-meridian",
        "Meridian plane of the body: planet of radius R with centre O, polar axis k1 up, i1 in the equatorial plane, "
        "body P at latitude lambda, right triangle OFP with legs R cos lambda and R sin lambda, the distance r_perp to "
        "the axis, the attraction towards O and the centrifugal force away from the axis",
        r"Meridian plane of the body ($\mathbf i_1$ right, $\mathbf k_1$ up, $\mathbf j_1$ into the paper, $\otimes$). "
        r"In the shaded right triangle $OFP$ the hypotenuse is $R$, the leg adjacent to $\lambda$ is $R\cos\lambda$ "
        r"along $\mathbf i_1$ and the opposite leg is $R\sin\lambda$ along $\mathbf k_1$. The centrifugal force "
        r"$m\Omega^2\mathbf r_\perp$ is horizontal, away from the axis; the attraction $-mg_p\mathbf e_r$ points to $O$")
def meridian():
    sc = Scene(640, 560, (290, 290), 200)
    O = (0.0, 0.0)
    t = math.radians(LAT)
    P = (math.cos(t), math.sin(t))
    F = (P[0], 0.0)
    sc.circle(O, 1.0, "HEAD", 3.0)
    fixed_axis(sc, (0.0, -1.2), 90, 2.45, "polar axis", off=(46, 0))
    fixed_axis(sc, (-1.2, 0.0), 0, 2.5, "equator", off=(-8, 22))
    spin_about_vertical(sc, (0.0, 1.1), 0.16, 0.05, "Ω")
    triangle(sc, [O, F, P])
    right_angle(sc, F, 180, 90, 0.05)
    sc.dashed(F, P)
    sc.line(O, P, "HEAD", 1.6)
    sc.angle(O, 0.26, 0, LAT, "λ", name_r=0.36)
    sc.label((0.3 * P[0], 0.3 * P[1]), "R", "TEXT", "end", 17, dx=-8, dy=-6)
    sc.label((F[0] * 0.62, 0.0), "R cos λ", "TEXT", "start", 15, dy=22)
    sc.label((F[0], P[1] / 2), "R sin λ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.dashed((0.0, P[1]), P)
    sc.label((P[0] / 2, P[1]), S("r", "⊥") + " = R cos λ", "TEXT", "middle", 15, dy=-9)
    unit(sc, O, 0, 0.28, bold("i") + S("", "1"), off=(-4, 22))
    unit(sc, O, 90, 0.28, bold("k") + S("", "1"), off=(-18, 4))
    axis_in(sc, (-0.55, -0.45), bold("j") + S("", "1"), "BLUE", off=(0, 30))
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    sc.vec(P, (P[0] - 0.36 * math.cos(t), P[1] - 0.36 * math.sin(t)), "−mg" + S("", "p") + bold("e") + S("", "r"),
           "PINK", 2.4, name_off=(-34, -14), size=15)
    sc.vec(P, (P[0] + 0.42, P[1]), S(bold("F"), "C"), "PINK", 2.4, name_off=(10, -10), size=16)
    unit(sc, P, LAT, 0.26, bold("e") + S("", "r"), "ACC", off=(8, -10))
    sc.mass(P, "P", r=7, name_off=(24, 22))
    return sc
