"""Problem 07: skater B towed by a vehicle A that turns on a circle; rotating frame Ox1y1 along OA."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

WT = 35.0            # drawn value of omega t, degrees
PSI = 50.0           # drawn value of psi, degrees (in the motion psi < 0; the formulas are the same)


@figure("p07-attitude",
        "Top view with k0 = k1 out of the paper: inertial axes i0 to the right and j0 up in grey, rotating axes i1 and "
        "j1 turned counter-clockwise by omega t in blue, with the dashed right triangles that give their components",
        r"View from $+\mathbf k_0$ ($\mathbf k_0 = \mathbf k_1$ out of the paper, $\odot$). $\mathbf i_1$ is "
        r"$\mathbf i_0$ turned counter-clockwise by $\omega t$: legs $\cos\omega t$ along $\mathbf i_0$ and "
        r"$\sin\omega t$ along $\mathbf j_0$. $\mathbf j_1$ turns the same angle from $\mathbf j_0$, so its opposite leg "
        r"$\sin\omega t$ points along $-\mathbf i_0$: hence $\mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0$")
def attitude():
    sc = Scene(520, 430, (250, 330), 230)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(WT)), math.sin(math.radians(WT))
    fixed_axis(sc, O, 0, 1.0, bold("i") + S("", "0"), off=(16, 6))
    fixed_axis(sc, O, 90, 1.15, bold("j") + S("", "0"), off=(16, 4))
    fixed_axis(sc, O, 180, 0.85, "−" + bold("i") + S("", "0"), off=(-4, -12), dashed=True)
    # right triangles of i1 and j1
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), (-s, c)], "BLUE", 0.10)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((0.0, c), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    i1 = unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -6))
    unit(sc, O, WT + 90, 1.0, bold("j") + S("", "1"), off=(-14, -8))
    sc.angle(O, 0.30, 0, WT, "ωt", name_r=0.42)
    sc.angle(O, 0.30, 90, 90 + WT, "ωt", name_r=0.43)
    sc.label((c / 2, 0.0), "cos ωt", "TEXT", "middle", 15, dy=22)
    sc.label((c, s / 2), "sin ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, c), "sin ωt", "TEXT", "middle", 15, dy=-10)
    sc.label((0.0, c / 2), "cos ωt", "TEXT", "start", 15, dx=8, dy=16)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-10, 30))
    sc.note((0.30, -0.24), "view from +k₀", "TEXT", "start", 13)
    return sc


@figure("p07-bar-plane",
        "Rotating plane Ox1y1: vehicle A at rest at distance a from O on the x1 axis, bar AB of length a at angle psi, "
        "the right triangle AFB with legs a cos psi and a sin psi, the dashed components of the position of B, the "
        "dashed circle of radius a around A that B can describe, and the bar basis u_AB, u_perp at B",
        r"Plane of $S_1$ ($\mathbf i_1$ along $OA$, $\mathbf k_1$ out of the paper). $\mathbf r_1^B = \overrightarrow{OA} + "
        r"\overrightarrow{AB}$: in the shaded right triangle $AFB$ the hypotenuse is $|AB| = a$, the leg adjacent to "
        r"$\psi$ is $a\cos\psi$ along $\mathbf i_1$ and the opposite leg is $a\sin\psi$ along $\mathbf j_1$. The dashed "
        r"circle is the path of $B$ relative to $S_1$; $\mathbf u_{AB}, \mathbf u_\perp$ in orange")
def bar_plane():
    sc = Scene(660, 525, (70, 300), 200)
    O = (0.0, 0.0)
    A = (1.0, 0.0)
    c, s = math.cos(math.radians(PSI)), math.sin(math.radians(PSI))
    B = (1.0 + c, s)
    F = (1.0 + c, 0.0)
    sc.arc(A, 1.0, 62, 352, "EDGE", 1.1, "5 4")
    fixed_axis(sc, (-0.15, 0.0), 0, 2.75, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.1), 90, 1.3, S("y", "1"), off=(14, 2))
    triangle(sc, [A, F, B])
    right_angle(sc, F, 180, 90, 0.06)
    sc.dashed(F, B)
    sc.rod(A, B, 3.5)
    sc.label(((A[0] + B[0]) / 2, (A[1] + B[1]) / 2), "a", "TEXT", "end", 17, dx=-10, dy=-4)
    sc.angle(A, 0.26, 0, PSI, "ψ", name_r=0.37)
    sc.label(((A[0] + F[0]) / 2, 0.0), "a cos ψ", "TEXT", "middle", 15, dy=22)
    sc.label((0.5, 0.0), "a", "TEXT", "middle", 16, dy=22)
    sc.label((F[0], s / 2), "a sin ψ", "TEXT", "start", 15, dx=10, dy=5)
    sc.dim((0.0, -0.28), (F[0], -0.28), "a(1 + cos ψ)", off=(0, 20))
    sc.dashed((0.0, -0.05), (0.0, -0.32))
    sc.dashed((F[0], -0.04), (F[0], -0.32))
    sc.dotp(A, 5.5)
    sc.label(A, "A", "HEAD", "end", 17, dx=-8, dy=-10)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=22)
    sc.label(F, "F", "HEAD", "start", 15, dx=8, dy=20)
    unit(sc, O, 0, 0.32, bold("i") + S("", "1"), off=(2, -12))
    unit(sc, O, 90, 0.32, bold("j") + S("", "1"), off=(-18, 6))
    unit(sc, B, PSI, 0.30, bold("u") + S("", "AB"), "ACC", off=(18, 2))
    unit(sc, B, PSI + 90, 0.30, bold("u") + S("", "⊥"), "ACC", off=(-14, -8))
    sc.mass(B, "B", r=7, name_off=(18, 16))
    return sc
