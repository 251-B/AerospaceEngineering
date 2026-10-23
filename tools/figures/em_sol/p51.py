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
