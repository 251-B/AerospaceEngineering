"""Problem 49: particle on a sphere of radius a attracted to a point A at 2a, sphere and A spinning about k0."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold


@figure("p49-top-view",
        "View from +z with k0 = k1 out of the paper: inertial axes i0 and j0 in grey, the rotating axes i1 and j1 turned "
        "counter-clockwise by Omega t in blue, the sphere of radius a seen from above and the attracting point A at "
        "distance 2a along i1",
        r"View from $+z$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$), so $\mathbf j_0$ is $\mathbf i_0$ turned "
        r"$90^\circ$ counter-clockwise. $S_1$ turns $\Omega t$ counter-clockwise: $\mathbf i_1$ has the legs $\cos\Omega t$ "
        r"along $\mathbf i_0$ and $\sin\Omega t$ along $\mathbf j_0$; the tip of $\mathbf j_1$ moves to the side of "
        r"$-\mathbf i_0$, hence $-\sin\Omega t$. $A$ sits on the $\mathbf i_1$ axis at $OA = 2a$")
def top_view():
    a = 30.0
    sc = Scene(560, 470, (230, 300), 115)
    O = (0.0, 0.0)
    d1 = (math.cos(math.radians(a)), math.sin(math.radians(a)))
    sc.circle(O, 1.0, "HEAD", 1.8)
    sc.line(O, (2.35 * d1[0], 2.35 * d1[1]), "BLUE", 1.2, "6 4")
    A = (2.0 * d1[0], 2.0 * d1[1])
    sc.dotp(A, 5.0)
    sc.label(A, "A", "HEAD", "start", 17, dx=8, dy=20)
    fixed_axis(sc, (-1.5, 0.0), 0, 3.6, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.5), 90, 3.05, S(bold("j"), "0"), off=(14, 4))
    axis_out(sc, O, S(bold("k"), "0") + " = " + S(bold("k"), "1"), off=(-62, 50))
    i1 = unit(sc, O, a, 1.25, S(bold("i"), "1"), off=(-4, -14))
    j1 = unit(sc, O, a + 90, 1.25, S(bold("j"), "1"), off=(-12, -8))
    triangle(sc, [O, (i1[0], 0.0), i1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((i1[0], i1[1] / 2), "sin Ωt", "TEXT", "start", 15, dx=8, dy=4)
    sc.dashed(j1, (j1[0], 0.0))
    sc.label((j1[0] / 2, 0.0), "−sin Ωt", "TEXT", "middle", 15, dy=20)
    sc.angle(O, 0.42, 0, a, "Ωt", name_r=0.58)
    sc.angle(O, 0.30, 90, 90 + a, "Ωt", name_r=0.44)
    sc.label((A[0] * 0.78, A[1] * 0.78), "2a", "TEXT", "middle", 15, dx=-8, dy=-16)
    sc.note((-1.75, -1.25), "sphere of radius a (from above)", "TEXT", "start", 13)
    return sc


@figure("p49-axis-view",
        "View along the axis OA with i1 out of the paper: j1 to the right and k1 up in grey, the unit vector u at angle "
        "theta from j1 and the unit vector e_theta perpendicular to it, both in orange, with the shaded right triangle "
        "of u, and the projection P' of the particle at distance a sin phi along u",
        r"View along $OA$, with $\mathbf i_1$ out of the paper ($\odot$): then $\mathbf j_1$ points right and "
        r"$\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ up. The azimuth $\theta$ turns counter-clockwise from $\mathbf j_1$: "
        r"$\mathbf u = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1$ (legs of the shaded triangle) and "
        r"$\mathbf e_\theta = d\mathbf u/d\theta$. $P$ projects onto this plane at $P'$, at distance $a\sin\phi$ from the axis")
def axis_view():
    th = 40.0
    sc = Scene(500, 430, (200, 290), 170)
    O = (0.0, 0.0)
    fixed_axis(sc, (-0.7, 0.0), 0, 2.0, S(bold("j"), "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.5), 90, 1.8, S(bold("k"), "1"), off=(14, 4))
    axis_out(sc, O, S(bold("i"), "1") + " (towards A)", off=(-56, 28))
    u = unit(sc, O, th, 0.75, bold("u"), "ACC", off=(-4, -12))
    unit(sc, O, th + 90, 0.75, S(bold("e"), "θ"), "ACC", off=(-14, -6))
    triangle(sc, [O, (u[0], 0.0), u])
    right_angle(sc, (u[0], 0.0), 180, 90, 0.05)
    sc.dashed(u, (u[0], 0.0))
    sc.label((u[0] / 2, 0.0), "cos θ", "TEXT", "middle", 15, dy=20)
    sc.label((u[0], u[1] / 2), "sin θ", "TEXT", "start", 15, dx=8, dy=4)
    sc.angle(O, 0.30, 0, th, "θ", name_r=0.42)
    Pp = (1.25 * math.cos(math.radians(th)), 1.25 * math.sin(math.radians(th)))
    sc.line(u, Pp, "EDGE", 1.1, "5 4")
    sc.dotp(Pp, 4.5)
    sc.label(Pp, "P′", "HEAD", "start", 17, dx=8, dy=-6)
    sc.label(Pp, "OP′ = a sin φ", "TEXT", "start", 13, dx=10, dy=16)
    return sc


@figure("p49-meridian",
        "Meridian plane that contains the axis OA and the particle: i1 to the right and u up, e_theta out of the paper, the "
        "circle of radius a, the particle P at angle phi from OA, the shaded right triangle with legs a cos phi and a sin phi, "
        "the spherical vectors e_r and e_phi at P in orange and the dashed segment from P to A at 2a",
        r"Meridian plane of $P$ (it contains $\mathbf i_1$ and $\mathbf u$; $\mathbf e_\theta = \mathbf i_1\times\mathbf u$ is "
        r"out of the paper). $\phi$ is measured at $O$ from $OA$: in the shaded triangle the hypotenuse is $a$, the leg "
        r"adjacent to $\phi$ is $a\cos\phi$ along $\mathbf i_1$ and the opposite one $a\sin\phi$ along $\mathbf u$. "
        r"$\mathbf e_r, \mathbf e_\phi$ in orange; the attraction acts along $PA$")
def meridian():
    ph = 60.0
    sc = Scene(720, 420, (200, 240), 150)
    O = (0.0, 0.0)
    P = (math.cos(math.radians(ph)), math.sin(math.radians(ph)))
    A = (2.0, 0.0)
    sc.circle(O, 1.0, "HEAD", 2.2)
    fixed_axis(sc, (-1.25, 0.0), 0, 3.6, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.2), 90, 2.55, bold("u"), off=(16, 4))
    axis_out(sc, O, S(bold("e"), "θ"), off=(-30, -12))
    triangle(sc, [O, (P[0], 0.0), P])
    right_angle(sc, (P[0], 0.0), 180, 90, 0.07)
    sc.line(O, P, "HEAD", 1.4)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0] / 2, 0.0), "a cos φ", "TEXT", "middle", 14, dy=20)
    sc.label((P[0], P[1] / 2), "a sin φ", "TEXT", "start", 13, dx=7, dy=4)
    sc.label((P[0] / 2, P[1] / 2), "a", "TEXT", "end", 16, dx=-8, dy=-6)
    sc.angle(O, 0.26, 0, ph, "φ", name_r=0.38)
    sc.line(P, A, "PINK", 1.4, "6 4")
    sc.label(((P[0] + A[0]) / 2, (P[1] + A[1]) / 2), "PA", "PINK", "start", 14, dx=8, dy=-6)
    sc.dotp(A, 5.0)
    sc.label(A, "A", "HEAD", "middle", 17, dy=24)
    sc.label((1.0, 0.0), "2a = OA", "TEXT", "start", 13, dx=36, dy=40)
    unit(sc, P, ph, 0.5, S(bold("e"), "r"), "ACC", off=(10, -6))
    unit(sc, P, ph + 90, 0.5, S(bold("e"), "φ"), "ACC", off=(-8, -12))
    sc.mass(P, "P", r=7, name_off=(-18, 4))
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=22)
    return sc
