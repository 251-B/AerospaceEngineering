"""Problem 20: heavy particle on a circular wire that turns about its vertical diameter."""
import math

from figures.em_solutions import (axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle,
                                  unit)
from figures.mech import S, Scene, bold

WT = 35.0            # drawn value of omega t, degrees
TH = 50.0            # drawn value of theta, degrees


@figure("p20-top-view",
        "Top view with k0 = k1 out of the paper: inertial axes i0, j0 in grey, the trace of the wire plane along i1 "
        "turned by omega t, and j1 normal to the wire plane, with the dashed right triangles of their components",
        r"View from $+\mathbf k_0$ ($\mathbf k_0 = \mathbf k_1$ out of the paper, $\odot$). The wire is seen edge-on, "
        r"along $\mathbf i_1$, turned counter-clockwise by $\omega t$; $\mathbf j_1 = \mathbf k_1\times\mathbf i_1$ is "
        r"normal to it. The opposite leg of $\mathbf j_1$ points along $-\mathbf i_0$: hence "
        r"$\mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0$")
def top_view():
    sc = Scene(560, 480, (270, 330), 220)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(WT)), math.sin(math.radians(WT))
    sc.line((-1.1 * c, -1.1 * s), (1.15 * c, 1.15 * s), "EDGE", 5.0)
    sc.note((-0.2, -0.6), "wire (seen edge-on)", "TEXT", "start", 13)
    fixed_axis(sc, O, 0, 1.05, bold("i") + S("", "0"), off=(16, 6))
    fixed_axis(sc, O, 90, 1.2, bold("j") + S("", "0"), off=(16, 4))
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), (-s, c)], "BLUE", 0.10)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((0.0, c), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(-6, -16))
    unit(sc, O, WT + 90, 1.0, bold("j") + S("", "1"), off=(-14, -8))
    sc.angle(O, 0.30, 0, WT, "ωt", name_r=0.43)
    sc.angle(O, 0.30, 90, 90 + WT, "ωt", name_r=0.44)
    sc.label((c / 2, 0.0), "cos ωt", "TEXT", "middle", 15, dy=22)
    sc.label((c, s * 0.35), "sin ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, c), "sin ωt", "TEXT", "middle", 15, dy=-10)
    sc.label((0.0, c / 2), "cos ωt", "TEXT", "start", 15, dx=8, dy=16)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-58, 4))
    return sc


@figure("p20-wire-plane",
        "Plane of the wire fixed in S1: centre O, vertical axis k1, particle P at the angle theta from the downward "
        "vertical, the right triangle OFP with legs R sin theta and R cos theta, j1 into the paper, and the wire basis "
        "e_r, e_theta at P",
        r"Plane of the wire, fixed in $S_1$ ($\mathbf i_1$ right, $\mathbf k_1$ up, so $\mathbf j_1$ points into the "
        r"paper, $\otimes$). In the shaded right triangle $OFP$ the hypotenuse is $R$, the leg opposite $\theta$ is "
        r"$R\sin\theta$ along $\mathbf i_1$ and the adjacent leg is $R\cos\theta$ along $-\mathbf k_1$. "
        r"$\mathbf e_r, \mathbf e_\theta$ in orange")
def wire_plane():
    sc = Scene(600, 560, (290, 290), 200)
    O = (0.0, 0.0)
    t = math.radians(TH)
    P = (math.sin(t), -math.cos(t))
    F = (0.0, P[1])
    sc.circle(O, 1.0, "HEAD", 3.0)
    fixed_axis(sc, (0.0, -1.2), 90, 2.45, S("z", "1"), off=(14, 2))
    fixed_axis(sc, (-1.2, 0.0), 0, 2.45, S("x", "1"), off=(14, 5))
    spin_about_vertical(sc, (0.0, 1.08), 0.16, 0.05, "ω")
    triangle(sc, [O, F, P])
    right_angle(sc, F, 0, 90, 0.05)
    sc.dashed(F, P)
    sc.line(O, P, "HEAD", 1.6)
    sc.angle(O, 0.24, -90, -90 + TH, "θ", name_r=0.34)
    sc.label(((O[0] + P[0]) / 2, (O[1] + P[1]) / 2), "R", "TEXT", "start", 17, dx=10, dy=-2)
    sc.label((0.0, F[1] / 2), "R cos θ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label(((F[0] + P[0]) / 2, F[1]), "R sin θ", "TEXT", "middle", 15, dy=22)
    unit(sc, O, 0, 0.3, bold("i") + S("", "1"), off=(8, -12))
    unit(sc, O, 90, 0.3, bold("k") + S("", "1"), off=(-18, 4))
    axis_in(sc, (-0.55, 0.55), bold("j") + S("", "1"), "BLUE", off=(0, 30))
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    unit(sc, P, TH - 90, 0.28, bold("e") + S("", "r"), "ACC", off=(14, 10))
    unit(sc, P, TH, 0.28, bold("e") + S("", "θ"), "ACC", off=(14, -4))
    sc.mass(P, "P", r=7, name_off=(26, 6))
    sc.gravity((1.15, 0.95), 0.32, "g")
    return sc
