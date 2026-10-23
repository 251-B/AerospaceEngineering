"""Problem 47: two repelling particles on concentric wires (radii a and 2a) in a plane spinning about the vertical."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

PHI, THETA = 30.0, -60.0       # the equilibrium configuration of part (i)


def _pt(r, deg):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


@figure("p47-wire-plane",
        "Plane of the two wires, fixed in the moving frame: circles of radii a and 2a centred at O, particle P at angle "
        "phi = 30 degrees and particle Q at angle theta = -60 degrees from x1, the shaded right triangle of P with legs "
        "a cos phi and a sin phi, the polar bases of both particles in orange and the segment PQ",
        r"Plane $Ox_1y_1$, fixed in $S_1$, drawn at the configuration of part (i) ($\varphi = 30^\circ$, $\theta = -60^\circ$). "
        r"For $P$ the hypotenuse of the shaded triangle is $a$, the leg adjacent to $\varphi$ is $a\cos\varphi$ (along "
        r"$\mathbf i_1$) and the opposite one $a\sin\varphi$ (along $\mathbf j_1$); $Q$ works the same way with $2a$ and "
        r"$\theta$ (here negative, below $Ox_1$). Polar bases $\mathbf e_r, \mathbf e_\varphi$ and $\mathbf e_r^Q, "
        r"\mathbf e_\theta$ in orange")
def wire_plane():
    sc = Scene(720, 760, (360, 400), 140)
    O = (0.0, 0.0)
    P = _pt(1.0, PHI)
    Q = _pt(2.0, THETA)
    sc.circle(O, 1.0, "HEAD", 2.4)
    sc.circle(O, 2.0, "HEAD", 2.4)
    fixed_axis(sc, (-2.35, 0.0), 0, 4.75, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -2.3), 90, 5.05, S("y", "1") + " ≡ " + S("y", "0"), off=(36, 2))
    spin_about_vertical(sc, (0.0, 2.33), 0.2, 0.05, "Ω")
    # key triangle of P
    triangle(sc, [O, (P[0], 0.0), P])
    right_angle(sc, (P[0], 0.0), 180, 90, 0.07)
    sc.line(O, P, "HEAD", 1.4)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0] / 2, 0.0), "a cos φ", "TEXT", "middle", 14, dy=22)
    sc.label((P[0], P[1] / 2), "a sin φ", "TEXT", "end", 13, dx=-5, dy=10)
    sc.angle(O, 0.25, 0, PHI, "φ", name_r=0.36)
    # Q
    sc.line(O, Q, "HEAD", 1.4)
    sc.angle(O, 0.62, THETA, 0, "θ", name_r=0.78)
    # segment PQ (line of the repulsion)
    sc.line(P, Q, "PINK", 1.4, "6 4")
    mid = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
    sc.label(mid, "PQ", "PINK", "start", 14, dx=10, dy=0)
    # moving basis
    B1 = (-2.25, -2.15)
    unit(sc, B1, 0, 0.45, S(bold("i"), "1"), off=(14, 6))
    unit(sc, B1, 90, 0.45, S(bold("j"), "1"), off=(-16, 6))
    sc.note(B1, "basis " + S("B", "1"), "TEXT", "start", 13, dx=4, dy=22)
    # polar bases
    unit(sc, P, PHI, 0.55, S(bold("e"), "r"), "ACC", off=(10, -6))
    unit(sc, P, PHI + 90, 0.55, S(bold("e"), "φ"), "ACC", off=(-14, -2))
    unit(sc, Q, THETA, 0.55, S(bold("e"), "r") + S("", "", "Q"), "ACC", off=(14, 14))
    unit(sc, Q, THETA + 90, 0.55, S(bold("e"), "θ"), "ACC", off=(16, -2))
    sc.mass(P, "P", r=7, name_off=(-18, 4))
    sc.mass(Q, "Q", r=7, name_off=(20, 8))
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    sc.gravity((-2.3, 2.5), 0.5, "g")
    return sc


@figure("p47-top-view",
        "Top view from +y0 with j0 out of the paper: inertial axes i0 to the right and k0 down the page in grey, the "
        "axes i1 and k1 of the rotating plane turned counter-clockwise by Omega t in blue, with the dashed components of i1",
        r"View from $+y_0$, with $\mathbf j_0 = \mathbf j_1$ out of the paper ($\odot$): $\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ "
        r"points down the page. For $\Omega \gt 0$ the plane of the wires turns counter-clockwise by $\Omega t$; $\mathbf i_1$ "
        r"has the components $\cos\Omega t$ along $\mathbf i_0$ and $\sin\Omega t$ along $-\mathbf k_0$ (up the page), hence "
        r"the minus sign")
def top_view():
    sc = Scene(480, 440, (170, 215), 165)
    O = (0.0, 0.0)
    a = 35.0
    fixed_axis(sc, O, 0, 1.15, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, O, -90, 1.0, S(bold("k"), "0"), off=(14, 4))
    fixed_axis(sc, O, 90, 0.95, "−" + S(bold("k"), "0"), off=(20, 4), dashed=True)
    axis_out(sc, O, S(bold("j"), "0") + " = " + S(bold("j"), "1"), off=(-46, 24))
    i1 = unit(sc, O, a, 1.0, S(bold("i"), "1"), off=(14, -6))
    unit(sc, O, a - 90, 1.0, S(bold("k"), "1"), off=(16, 8))
    sc.angle(O, 0.42, 0, a, "Ωt", name_r=0.56)
    sc.angle(O, 0.30, -90, a - 90, "Ωt", name_r=0.43)
    triangle(sc, [O, (i1[0], 0.0), i1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, i1[1]), "sin Ωt", "TEXT", "end", 15, dx=-12, dy=5)
    sc.note((0.45, 1.0), "view from " + "+" + S("y", "0"), "TEXT", "start", 13)
    sc.note((0.45, 0.88), "Ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc
