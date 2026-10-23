"""Problem 09: astronaut on the inner surface of a cylinder spinning about its axis."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

WT = 25.0            # drawn value of omega t, degrees
PHI = 50.0           # drawn azimuth of the astronaut in S1, degrees


@figure("p09-cross-section",
        "Cross-section of the hull seen along its axis with k out of the paper: inertial axes i0, j0 in grey, hull axes "
        "i1, j1 turned by omega t in blue, astronaut P on the floor at azimuth phi from i1, the right triangle with legs "
        "R cos phi and R sin phi, and the cylindrical basis e_r, e_theta at P",
        r"Cross-section along the axis ($\mathbf k_0 = \mathbf k_1$ out of the paper, $\odot$). The hull axes "
        r"$\mathbf i_1, \mathbf j_1$ are $\mathbf i_0, \mathbf j_0$ turned counter-clockwise by $\omega t$. In the shaded "
        r"right triangle the hypotenuse is $R$, the leg along $\mathbf i_1$ is $R\cos\varphi$ and the leg along "
        r"$\mathbf j_1$ is $R\sin\varphi$; $\mathbf e_r, \mathbf e_\theta$ in orange")
def cross_section():
    sc = Scene(680, 580, (300, 300), 210)
    O = (0.0, 0.0)
    R = 1.0
    sc.circle(O, R, "HEAD", 3.0)
    fixed_axis(sc, O, 0, 1.25, bold("i") + S("", "0"), off=(14, 5))
    fixed_axis(sc, O, 90, 1.22, bold("j") + S("", "0"), off=(16, 2))
    w, p = math.radians(WT), math.radians(WT + PHI)
    P = (R * math.cos(p), R * math.sin(p))
    F = (R * math.cos(math.radians(PHI)) * math.cos(w), R * math.cos(math.radians(PHI)) * math.sin(w))
    sc.line((0.0, 0.0), (1.2 * math.cos(w), 1.2 * math.sin(w)), "EDGE", 1.0, "4 4")
    triangle(sc, [O, F, P])
    right_angle(sc, F, WT + 180, WT + 90, 0.05)
    sc.dashed(F, P)
    sc.line(O, P, "HEAD", 1.6)
    unit(sc, O, WT, 0.42, bold("i") + S("", "1"), off=(6, 20))
    unit(sc, O, WT + 90, 0.42, bold("j") + S("", "1"), off=(-18, 4))
    sc.angle(O, 1.12, 0, WT, "ωt", name_r=1.24)
    sc.angle(O, 0.30, WT, WT + PHI, "φ", name_r=0.40)
    sc.label(((O[0] + P[0]) / 2, (O[1] + P[1]) / 2), "R", "TEXT", "end", 17, dx=-8, dy=-4)
    sc.label((F[0] * 0.86, F[1] * 0.86), "R cos φ", "TEXT", "start", 15, dx=6, dy=22)
    sc.label(((F[0] + P[0]) / 2, (F[1] + P[1]) / 2), "R sin φ", "TEXT", "start", 15, dx=10, dy=6)
    unit(sc, P, WT + PHI, 0.26, bold("e") + S("", "r"), "ACC", off=(10, -8))
    unit(sc, P, WT + PHI + 90, 0.26, bold("e") + S("", "θ"), "ACC", off=(-16, -6))
    sc.mass(P, "P", r=7, name_off=(22, -14))
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-40, 28))
    sc.spin((0.0, 0.0), 1.13, 200, 245, "ω", name_r=1.25)
    return sc


@figure("p09-forces",
        "Astronaut P at the bottom of the hull cross-section running with relative velocity u_theta e_theta: the floor "
        "force N towards the axis, the centrifugal force and the Coriolis force away from the axis",
        r"Forces in $S_1$ on the astronaut at $P$ ($\mathbf k_1$ out of the paper). With $u_\theta \gt 0$ (running in the "
        r"sense of rotation) both $\mathbf F_C = m\omega^2R\,\mathbf e_r$ and $\mathbf F_{COR} = 2m\omega u_\theta\,\mathbf e_r$ "
        r"point away from the axis; the floor force $\mathbf N$ points to the axis and balances them plus $m\mathbf a_1^P$")
def forces():
    sc = Scene(560, 520, (280, 225), 190)
    O = (0.0, 0.0)
    sc.circle(O, 1.0, "HEAD", 3.0)
    P = (0.0, -1.0)
    sc.dashed(O, P)
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=-8)
    axis_out(sc, (0.42, 0.4), bold("k") + S("", "1"), off=(26, 6))
    sc.vec(P, (0.0, -0.45), bold("N"), "PINK", 2.6, name_off=(-18, 8), size=17)
    sc.vec((-0.08, -1.0), (-0.08, -1.42), S(bold("F"), "C"), "PINK", 2.6, name_off=(-24, 4), size=17)
    sc.vec((0.08, -1.0), (0.08, -1.36), S(bold("F"), "COR"), "PINK", 2.6, name_off=(30, 4), size=17)
    unit(sc, P, 0, 0.5, S("u", "θ") + " " + bold("e") + S("", "θ"), "BLUE", off=(30, -8))
    unit(sc, (-0.7, -0.72), -135, 0.22, bold("e") + S("", "r"), "ACC", off=(-12, 18))
    sc.mass(P, "P", r=7, name_off=(-20, -12))
    sc.spin(O, 0.32, 30, 150, "ω", name_r=0.45)
    return sc
