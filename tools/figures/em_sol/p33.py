"""Problem 33: two repelling beads on a parabolic wire z = x^2/(2L) that spins about its vertical axis Oz."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

X1, X2 = -0.7, 1.2                      # abscissas of P1 and P2 in units of L


def z(x):
    return x * x / 2.0


def parabola(sc):
    sc.curve(lambda x: (x, z(x)), -1.85, 1.85, col="HEAD", w=3.0)


@figure("p33-top-view",
        "View from above with k out of the paper at O: the inertial axes i0 to the right and j0 up in grey, the axes i1 "
        "and j1 of the wire frame turned counter-clockwise by omega t in blue, and the trace of the plane of the wire "
        "along i1 with the projections of P1 and P2",
        r"View from $+z$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$) at the vertex $O$: then "
        r"$\mathbf j_0 = \mathbf k_0\times\mathbf i_0$ points up the page. $\mathbf i_1, \mathbf j_1$ are "
        r"$\mathbf i_0, \mathbf j_0$ turned counter-clockwise by $\omega t$; the dashed legs give "
        r"$\mathbf i_1 = \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0$ and "
        r"$\mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0$. The plane of the wire is seen edge-on, "
        r"along $\mathbf i_1$; $P_1$ ($x_1 \lt 0$) and $P_2$ ($x_2 \gt 0$) project on it")
def top_view():
    sc = Scene(560, 470, (260, 240), 150)
    O = (0.0, 0.0)
    a = 35.0
    d = (math.cos(math.radians(a)), math.sin(math.radians(a)))
    sc.line((-1.3 * d[0], -1.3 * d[1]), (1.45 * d[0], 1.45 * d[1]), "EDGE", 1.0, "2 3")
    fixed_axis(sc, O, 0, 1.4, S(bold("i"), "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.3, S(bold("j"), "0"), off=(14, 4))
    axis_out(sc, O, S(bold("k"), "0") + " = " + S(bold("k"), "1"), off=(44, 50))
    sc.label(O, "O", "HEAD", "end", 16, dx=-16, dy=8)
    i1 = unit(sc, O, a, 0.62, S(bold("i"), "1"), off=(14, 2))
    j1 = unit(sc, O, a + 90, 0.62, S(bold("j"), "1"), off=(-12, -8))
    sc.angle(O, 0.24, 0, a, "ωt", name_r=0.36)
    sc.angle(O, 0.20, 90, a + 90, "ωt", name_r=0.31)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos ωt", "TEXT", "middle", 14, dy=18)
    sc.label((0.0, i1[1]), "sin ωt", "TEXT", "start", 14, dx=8, dy=-6)
    sc.dashed(j1, (j1[0], 0.0))
    sc.dashed(j1, (0.0, j1[1]))
    sc.label((j1[0], 0.0), "−sin ωt", "TEXT", "middle", 14, dy=18)
    p1 = (X1 * d[0], X1 * d[1])
    p2 = (X2 * d[0], X2 * d[1])
    sc.dotp(p1, 4.5, "ACC")
    sc.label(p1, S("P", "1"), "HEAD", "end", 16, dx=-10, dy=-8)
    sc.dotp(p2, 4.5, "ACC")
    sc.label(p2, S("P", "2"), "HEAD", "start", 16, dx=8, dy=16)
    sc.note((0.55, -0.95), "view from +z", "TEXT", "start", 13)
    sc.note((0.55, -1.07), "ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc


@figure("p33-wire-plane",
        "Plane Oxz of the wire: the parabola z = x squared over 2L, the axis Oz with the spin omega, j1 into the paper at "
        "O, the beads P1 and P2, the dashed components x2 and x2 squared over 2L of the position of P2, and at P2 the "
        "slope triangle with legs 1 and x2 over L and hypotenuse s2, with the unit tangent t2 and normal n2",
        r"Plane $Oxz$, fixed in $S_1$ ($\mathbf j_1$ points into the paper, $\otimes$). The position of $P_2$ has the "
        r"dashed components $x_2$ and $z_2 = x_2^2/(2L)$. The shaded slope triangle at $P_2$ has a horizontal leg "
        r"proportional to $1$, a vertical leg proportional to $dz/dx = x_2/L$ and the hypotenuse $s_2 = "
        r"\sqrt{1 + x_2^2/L^2}$ along the tangent; dividing by $s_2$ gives $\mathbf t_2$, and turning it $90^\circ$ "
        r"towards the concave side gives $\mathbf n_2$ (orange)")
def wire_plane():
    sc = Scene(640, 400, (320, 335), 150)
    O = (0.0, 0.0)
    P1 = (X1, z(X1))
    P2 = (X2, z(X2))
    fixed_axis(sc, (-2.0, 0.0), 0, 4.0, "x", off=(12, 5))
    fixed_axis(sc, (0.0, -0.15), 90, 2.1, "z", off=(14, 4))
    spin_about_vertical(sc, (0.0, 1.72), 0.17, 0.05, "ω")
    parabola(sc)
    # components of r1(P2)
    sc.dashed(P2, (X2, 0.0))
    sc.dashed(P2, (0.0, P2[1]))
    sc.label((X2 / 2, P2[1]), S("x", "2"), "TEXT", "middle", 16, dy=-8)
    sc.label((X2, P2[1] / 2), S("x", "2", "2") + "/(2L)", "TEXT", "start", 15, dx=8, dy=5)
    # slope triangle at P2 (scaled by h)
    h = 0.42
    A = (X2 + h, P2[1])
    C = (X2 + h, P2[1] + h * X2)
    triangle(sc, [P2, A, C])
    right_angle(sc, A, 180, 90, 0.06)
    sc.line(P2, A, "EDGE", 1.1)
    sc.line(A, C, "EDGE", 1.1)
    sc.line(P2, (X2 + 1.6 * h, P2[1] + 1.6 * h * X2), "EDGE", 1.0, "2 3")
    sc.label(((P2[0] + A[0]) / 2 + 0.06, A[1]), "1", "TEXT", "middle", 15, dy=-6)
    sc.label((A[0], (A[1] + C[1]) / 2), S("x", "2") + "/L", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((P2[0] + 0.85 * (C[0] - P2[0]), P2[1] + 0.85 * (C[1] - P2[1])), S("s", "2"), "TEXT", "end", 15, dx=-12, dy=-2)
    ang = math.degrees(math.atan(X2))
    unit(sc, P2, ang, 0.32, S(bold("t"), "2"), "ACC", off=(-6, -12))
    unit(sc, P2, ang + 90, 0.32, S(bold("n"), "2"), "ACC", off=(-12, -6))
    sc.mass(P2, None, r=7)
    sc.label(P2, S("P", "2"), "HEAD", "start", 17, dx=14, dy=26)
    sc.mass(P1, None, r=7)
    sc.label(P1, S("P", "1"), "HEAD", "end", 17, dx=-12, dy=16)
    # basis of S1 at O
    unit(sc, O, 0, 0.32, S(bold("i"), "1"), off=(2, 22))
    unit(sc, O, 90, 0.32, S(bold("k"), "1"), off=(-18, 4))
    axis_in(sc, O, S(bold("j"), "1"), col="BLUE", off=(-26, 22))
    sc.label(O, "O", "HEAD", "start", 16, dx=10, dy=22)
    sc.gravity((1.0, 1.85), 0.32, "g")
    return sc


@figure("p33-chord",
        "The chord from P1 to P2 on the parabola, with the right triangle whose horizontal leg is x2 minus x1, vertical "
        "leg is the difference of heights and hypotenuse is the distance d, and the two repulsive forces along the chord",
        r"Chord $P_1P_2$: in the shaded right triangle the horizontal leg is $x_2 - x_1$, the vertical leg is "
        r"$z_2 - z_1 = (x_2^2 - x_1^2)/(2L) = (x_2 - x_1)(x_1 + x_2)/(2L)$ and the hypotenuse is the distance $d$; the "
        r"slope of the chord is $(x_1 + x_2)/(2L)$. The repulsions $\mathbf F_{E1}$ and $\mathbf F_{E2} = -\mathbf F_{E1}$ "
        r"(pink) act along the chord, pushing the beads apart")
def chord():
    sc = Scene(660, 380, (320, 330), 150)
    P1 = (X1, z(X1))
    P2 = (X2, z(X2))
    M = (X2, P1[1])
    fixed_axis(sc, (-2.0, 0.0), 0, 4.0, "x", off=(12, 5))
    fixed_axis(sc, (0.0, -0.15), 90, 2.0, "z", off=(14, 4))
    parabola(sc)
    triangle(sc, [P1, M, P2])
    right_angle(sc, M, 180, 90, 0.06)
    sc.line(P1, P2, "HEAD", 1.4, "6 4")
    sc.dashed(P1, M)
    sc.dashed(M, P2)
    sc.label((0.36, M[1]), S("x", "2") + " − " + S("x", "1"), "TEXT", "middle", 15, dy=-8)
    sc.label((M[0], (M[1] + P2[1]) / 2), S("z", "2") + " − " + S("z", "1"), "TEXT", "start", 15, dx=10, dy=5)
    sc.label(((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2), "d", "TEXT", "end", 17, dx=-8, dy=-10)
    u = ((P2[0] - P1[0]), (P2[1] - P1[1]))
    n = math.hypot(*u)
    u = (u[0] / n, u[1] / n)
    ang = math.degrees(math.atan2(u[1], u[0]))
    unit(sc, P2, ang, 0.42, S(bold("F"), "E2"), "PINK", off=(4, -14))
    unit(sc, P1, ang + 180, 0.42, S(bold("F"), "E1"), "PINK", off=(-8, 22))
    sc.mass(P1, None, r=7)
    sc.label(P1, S("P", "1"), "HEAD", "start", 17, dx=6, dy=28)
    sc.mass(P2, None, r=7)
    sc.label(P2, S("P", "2"), "HEAD", "start", 17, dx=14, dy=18)
    sc.label((0.0, 0.0), "O", "HEAD", "start", 16, dx=8, dy=20)
    return sc
