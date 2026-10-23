"""Problem 34: bead on a circular wire through O whose vertical plane Oxy swings about Oy with Omega(t) = A w sin(wt)."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

PHI = math.radians(40)


@figure("p34-wire-plane",
        "Plane Oxy of the wire: the circle of centre C on the x axis at distance R from O, the particle P at angle phi from "
        "Ox, the right triangle C F P with legs R cos phi and R sin phi, the horizontal distance R(1 + cos phi) from the "
        "axis Oy, the basis i1, j1 at O with k1 out of the paper, and the polar basis e_r, e_phi at P",
        r"Plane $Oxy$, fixed in $S_1$ ($\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ points out of the paper, $\odot$). "
        r"$\overrightarrow{OC} = R\,\mathbf i_1$; in the shaded right triangle $CFP$ the hypotenuse is $|CP| = R$, the leg "
        r"adjacent to $\varphi$ is $R\cos\varphi$ (along $\mathbf i_1$) and the opposite leg is $R\sin\varphi$ (along "
        r"$\mathbf j_1$). The distance from $P$ to the rotation axis $Oy$ is $R(1 + \cos\varphi)$. $\mathbf i_1, \mathbf j_1$ "
        r"in blue, $\mathbf e_r, \mathbf e_\varphi$ in orange")
def wire_plane():
    sc = Scene(620, 520, (110, 280), 170)
    O = (0.0, 0.0)
    C = (1.0, 0.0)
    P = (1.0 + math.cos(PHI), math.sin(PHI))
    F = (P[0], 0.0)
    fixed_axis(sc, (-0.25, 0.0), 0, 2.65, "x", off=(12, 5))
    fixed_axis(sc, (0.0, -1.25), 90, 2.6, "y", off=(14, 4))
    spin_about_vertical(sc, (0.0, 1.18), 0.15, 0.045, "Ω(t)")
    sc.circle(C, 1.0, "HEAD", 3.0)
    triangle(sc, [C, F, P])
    right_angle(sc, F, 180, 90, 0.06)
    sc.line(C, P, "HEAD", 1.6)
    sc.label((C[0] + 0.35 * math.cos(PHI), 0.35 * math.sin(PHI)), "R", "TEXT", "end", 17, dx=-6, dy=-8)
    sc.angle(C, 0.24, 0, 40, "φ", name_r=0.36)
    sc.dashed(F, P)
    sc.label(((C[0] + F[0]) / 2, 0.0), "R cos φ", "TEXT", "middle", 15, dy=20)
    sc.label((P[0], P[1] / 2), "R sin φ", "TEXT", "start", 15, dx=40, dy=5)
    # horizontal distance from the rotation axis
    sc.dashed(P, (P[0], -1.18))
    sc.dim((0.0, -1.12), (P[0], -1.12), "R(1 + cos φ)", off=(0, 22), size=14)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "middle", 17, dx=-6, dy=22)
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=22)
    unit(sc, O, 0, 0.32, S(bold("i"), "1"), off=(0, 22))
    unit(sc, O, 90, 0.32, S(bold("j"), "1"), off=(-18, 4))
    axis_out(sc, O, S(bold("k"), "1"), col="BLUE", off=(-24, -12))
    unit(sc, P, 40, 0.30, S(bold("e"), "r"), "ACC", off=(12, -2))
    unit(sc, P, 130, 0.30, S(bold("e"), "φ"), "ACC", off=(-8, -12))
    sc.mass(P, "P", r=7, name_off=(24, 6))
    sc.gravity((2.35, 1.15), 0.32, "g")
    return sc


@figure("p34-top-view",
        "View from above with j out of the paper: the inertial axes i to the right and k down in grey, the axes i1 and k1 "
        "of the swinging plane turned counter-clockwise by psi in blue, the dashed components cos psi along i and sin psi "
        "along minus k, and the extreme position psi = 2A of the swing",
        r"View from $+y$, with $\mathbf j_0 = \mathbf j_1$ out of the paper ($\odot$): then "
        r"$\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ points down the page. $\mathbf i_1, \mathbf k_1$ are "
        r"$\mathbf i_0, \mathbf k_0$ turned counter-clockwise by $\psi(t) = A(1 - \cos\omega t)$; the legs of "
        r"$\mathbf i_1$ are $\cos\psi$ along $\mathbf i_0$ and $\sin\psi$ along $-\mathbf k_0$ (up the page), hence "
        r"$\mathbf i_1 = \cos\psi\,\mathbf i_0 - \sin\psi\,\mathbf k_0$. The plane swings between $\psi = 0$ and "
        r"$\psi = 2A$ (dotted)")
def top_view():
    sc = Scene(500, 440, (170, 215), 165)
    O = (0.0, 0.0)
    a = 30.0
    fixed_axis(sc, O, 0, 1.15, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, O, -90, 1.0, S(bold("k"), "0"), off=(14, 4))
    fixed_axis(sc, O, 90, 0.95, "−" + S(bold("k"), "0"), off=(20, 4), dashed=True)
    axis_out(sc, O, S(bold("j"), "0") + " = " + S(bold("j"), "1"), off=(-46, 24))
    e = (0.9 * math.cos(math.radians(52)), 0.9 * math.sin(math.radians(52)))
    sc.line(O, e, "EDGE", 1.0, "2 3")
    sc.label(e, "ψ = 2A", "TEXT", "start", 14, dx=6, dy=-4)
    i1 = unit(sc, O, a, 1.0, S(bold("i"), "1"), off=(14, 4))
    unit(sc, O, a - 90, 1.0, S(bold("k"), "1"), off=(16, 8))
    sc.angle(O, 0.30, 0, a, "ψ", name_r=0.42)
    sc.angle(O, 0.26, -90, a - 90, "ψ", name_r=0.38)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos ψ", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, i1[1]), "sin ψ", "TEXT", "end", 15, dx=-12, dy=5)
    sc.note((-0.95, -0.95), "view from +y", "TEXT", "start", 13)
    return sc
