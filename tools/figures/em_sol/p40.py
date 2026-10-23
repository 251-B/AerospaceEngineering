"""Problem 40: particle P on the vertical axis and particle Q on a horizontal ring whose centre D revolves about it."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

WT = 35.0          # angle Omega t, deg (drawing value)
PHI = 50.0         # angle phi of Q on the ring, deg


@figure("p40-top-view",
        "Top view from +z0 with k0 out of the paper: fixed axes i0 to the right and j0 up in grey, the frame axes i1 and "
        "j1 turned counter-clockwise by Omega t in blue, j1 pointing to the ring centre D, and the shaded right triangles "
        "that give their components",
        r"View from $+z_0$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$), so $\mathbf j_0 = \mathbf k_0\times"
        r"\mathbf i_0$ points up. $\mathbf i_1, \mathbf j_1$ are $\mathbf i_0, \mathbf j_0$ turned counter-clockwise by "
        r"$\Omega t$, and $\mathbf j_1$ points from $O$ to the centre $D$ of the ring. $\mathbf j_1$ has legs "
        r"$\cos\Omega t$ along $\mathbf j_0$ and $\sin\Omega t$ along $-\mathbf i_0$, hence its minus sign")
def top_view():
    sc = Scene(520, 470, (250, 330), 150)
    O = (0.0, 0.0)
    fixed_axis(sc, O, 0, 1.2, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.2, bold("j") + S("", "0"), off=(16, 2))
    fixed_axis(sc, O, 180, 1.0, "−" + bold("i") + S("", "0"), off=(-8, -12), dashed=True)
    i1 = (math.cos(math.radians(WT)), math.sin(math.radians(WT)))
    j1 = (-math.sin(math.radians(WT)), math.cos(math.radians(WT)))
    D = (1.55 * j1[0], 1.55 * j1[1])
    sc.dashed(j1, D)
    sc.dotp(D, 4.5)
    sc.label(D, "D", "HEAD", "end", 17, dx=-10, dy=-6)
    triangle(sc, [O, (i1[0], 0.0), i1])
    triangle(sc, [O, (0.0, j1[1]), j1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(j1, (0.0, j1[1]))
    right_angle(sc, (i1[0], 0.0), 180, 90, 0.06)
    right_angle(sc, (0.0, j1[1]), 270, 180, 0.06)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -4))
    unit(sc, O, 90 + WT, 1.0, bold("j") + S("", "1"), off=(-16, 6))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((i1[0], i1[1] / 2), "sin Ωt", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((j1[0] / 2, j1[1]), "sin Ωt", "TEXT", "middle", 15, dy=-9)
    sc.label((0.0, j1[1] * 0.42), "cos Ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.angle(O, 0.30, 0, WT, "Ωt", name_r=0.44)
    sc.angle(O, 0.24, 90, 90 + WT, "Ωt", name_r=0.37)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-46, 30))
    sc.note((0.55, -0.6), "view from +z₀", "TEXT", "start", 13)
    sc.note((0.55, -0.73), "Ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc


@figure("p40-ring",
        "Plane of the ring seen from above in the moving frame: O at the origin, the centre D at distance l along j1, the "
        "ring of radius R, the particle Q at angle phi from j1 towards negative i1, the shaded right triangle D F Q with "
        "legs R cos phi along j1 and R sin phi along minus i1, and the ring basis e_r, e_phi at Q",
        r"Plane of the ring, fixed in $S_1$, seen from above ($\mathbf k_1$ out of the paper). $\overrightarrow{OQ} = "
        r"\ell\,\mathbf j_1 + R\,\mathbf e_r$. In the shaded right triangle $DFQ$ the hypotenuse is $R$, the leg along "
        r"$\mathbf j_1$ is $R\cos\phi$ and the leg along $-\mathbf i_1$ is $R\sin\phi$. $\mathbf i_1, \mathbf j_1$ in blue, "
        r"$\mathbf e_r, \mathbf e_\phi$ in orange")
def ring():
    sc = Scene(560, 560, (300, 470), 125)
    O = (0.0, 0.0)
    ell, R = 1.6, 1.0
    D = (0.0, ell)
    p = math.radians(PHI)
    Q = (-R * math.sin(p), ell + R * math.cos(p))
    F = (0.0, Q[1])
    sc.circle(D, R, "HEAD", 2.4)
    fixed_axis(sc, (-1.5, 0.0), 0, 2.9, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.3), 90, 3.3, S("y", "1"), off=(14, 4))
    triangle(sc, [D, F, Q])
    sc.line(D, Q, "HEAD", 1.6)
    sc.dashed(F, Q)
    right_angle(sc, F, 270, 180, 0.07)
    sc.label((0.0, (D[1] + F[1]) / 2), "R cos φ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((Q[0] / 2, F[1]), "R sin φ", "TEXT", "middle", 15, dy=-10)
    sc.label(((D[0] + Q[0]) / 2, (D[1] + Q[1]) / 2), "R", "TEXT", "end", 16, dx=-8, dy=14)
    sc.angle(D, 0.3, 90, 90 + PHI, "φ", name_r=0.42)
    sc.dim((1.25, 0.0), (1.25, ell), "ℓ", off=(14, 5))
    sc.dotp(D, 4.0)
    sc.label(D, "D", "HEAD", "start", 17, dx=10, dy=18)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=20)
    unit(sc, O, 0, 0.45, bold("i") + S("", "1"), off=(4, 22))
    unit(sc, O, 90, 0.45, bold("j") + S("", "1"), off=(-18, 8))
    unit(sc, Q, 90 + PHI, 0.5, bold("e") + S("", "r"), "ACC", off=(-6, -10))
    unit(sc, Q, 180 + PHI, 0.5, bold("e") + S("", "φ"), "ACC", off=(-16, 8))
    sc.mass(Q, "Q", r=7, name_off=(-26, 6))
    axis_out(sc, (1.2, 2.75), bold("k") + S("", "1"), off=(26, 6))
    return sc
