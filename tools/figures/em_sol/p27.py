"""Problem 27: bead on the sine-shaped wire y1 = sin x1, joined by a vertical spring to the rail y1 = 2, turning about Oy1."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

X = 2.4                                    # position of the bead in the drawing (m)


@figure("p27-wire-plane",
        "Plane of the wire in the rotating frame: the wire y1 = sin x1, the rail y1 = 2, the bead P at abscissa x1 with "
        "the dashed components x1 and sin x1, the vertical spring of length 2 - sin x1, the slope triangle with legs dx1 "
        "and cos x1 dx1, the basis i1, j1 at O and the tangent t and normal n directions at P",
        r"Plane of the wire, fixed in $Ox_1y_1z_1$. The dashed lines are the components $x_1$ and $\sin x_1$ of "
        r"$\mathbf r_1^P$; the spring is vertical, of length $2 - \sin x_1$. In the shaded slope triangle the "
        r"horizontal leg is $dx_1$ and the vertical leg is $dy_1 = \cos x_1\,dx_1$ (negative here: the wire goes down), "
        r"so the tangent direction is $\mathbf t = \mathbf i_1 + \cos x_1\,\mathbf j_1$ and the in-plane normal is "
        r"$\mathbf n = -\cos x_1\,\mathbf i_1 + \mathbf j_1$ (orange, drawn as unit vectors)")
def wire_plane():
    sc = Scene(800, 430, (70, 275), 100)
    P = (X, math.sin(X))
    c = math.cos(X)
    sc.curve(lambda u: (u, math.sin(u)), 0.0, 6.6, col="HEAD", w=3.0)
    # rail y1 = 2
    sc.line((0.0, 2.0), (6.6, 2.0), "HEAD", 2.0)
    sc.label((6.6, 2.0), S("y", "1") + " = 2", "TEXT", "end", 15, dy=-10)
    # axes
    fixed_axis(sc, (-0.3, 0.0), 0, 7.1, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.3), 90, 3.75, S("y", "1"), off=(14, 2))
    spin_about_vertical(sc, (0.0, 2.25), 0.2, 0.05, "ω")
    sc.label((0.0, 0.0), "O", "HEAD", "end", 17, dx=-8, dy=20)
    unit(sc, (0.0, 0.0), 0, 0.75, bold("i") + S("", "1"), off=(4, 22))
    unit(sc, (0.0, 0.0), 90, 0.75, bold("j") + S("", "1"), off=(-18, 4))
    # spring from P up to the rail (vertical)
    sc.spring(P, (P[0], 2.0), coils=6, amp=5)
    sc.label((P[0], (P[1] + 2.0) / 2), "k", "TEXT", "end", 16, dx=-12)
    sc.dim((P[0] + 1.45, P[1]), (P[0] + 1.45, 2.0), "2 − sin x₁", off=(44, 4))
    sc.dashed((P[0] + 1.1, P[1]), (P[0] + 1.52, P[1]))
    # components of the position
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0], 0.0), "x₁", "TEXT", "middle", 15, dy=22)
    sc.label((P[0], P[1] * 0.45), "sin x₁", "TEXT", "end", 15, dx=-8, dy=4)
    # slope triangle at P (to the left: the wire comes down from the crest)
    dx = 1.1
    A = (P[0] + dx, P[1])
    B = (P[0] + dx, P[1] + c * dx)
    triangle(sc, [P, A, B])
    right_angle(sc, A, 180, -90, 0.1)
    sc.line(P, A, "EDGE", 1.1)
    sc.line(A, B, "EDGE", 1.1)
    sc.line(P, B, "EDGE", 1.2, "5 4")
    sc.label(((P[0] + A[0]) / 2, P[1]), "dx₁", "TEXT", "middle", 15, dy=-8)
    sc.label((A[0], (A[1] + B[1]) / 2), "|cos x₁| dx₁", "TEXT", "start", 15, dx=8, dy=5)
    # tangent and normal directions at P (unit)
    at = math.degrees(math.atan2(c, 1.0))
    unit(sc, P, at, 0.6, bold("t"), "ACC", off=(-8, 16))
    unit(sc, P, at + 90, 0.6, bold("n"), "ACC", off=(-4, -12))
    sc.mass(P, "P", r=7, name_off=(-20, 22))
    sc.gravity((6.0, 1.75), 0.6, "g")
    return sc


@figure("p27-top-view",
        "Top view from +y1 with j0 = j1 out of the paper: inertial axes i0 to the right and k0 downwards in grey, the "
        "axes i1 and k1 of the wire rotated counter-clockwise by omega t in blue, with the dashed components of i1",
        r"View from $+y_1$, with $\mathbf j_0 = \mathbf j_1$ out of the paper ($\odot$): $\mathbf k_0 = \mathbf i_0\times"
        r"\mathbf j_0$ points down the page. The plane of the wire turns counter-clockwise by $\omega t$: the components "
        r"of $\mathbf i_1$ are $\cos\omega t$ along $\mathbf i_0$ and $\sin\omega t$ along $-\mathbf k_0$ (up the page), "
        r"hence $\mathbf i_1 = \cos\omega t\,\mathbf i_0 - \sin\omega t\,\mathbf k_0$")
def top_view():
    sc = Scene(480, 440, (170, 215), 165)
    O = (0.0, 0.0)
    a = 35.0
    fixed_axis(sc, O, 0, 1.15, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, O, -90, 1.0, bold("k") + S("", "0"), off=(16, 4))
    fixed_axis(sc, O, 90, 0.95, "−" + bold("k") + S("", "0"), off=(22, 4), dashed=True)
    axis_out(sc, O, bold("j") + S("", "0") + " = " + bold("j") + S("", "1"), off=(-50, 24))
    i1 = unit(sc, O, a, 1.0, bold("i") + S("", "1"), off=(14, -6))
    unit(sc, O, a - 90, 1.0, bold("k") + S("", "1"), off=(16, 8))
    sc.angle(O, 0.42, 0, a, "ωt", name_r=0.56)
    sc.angle(O, 0.30, -90, a - 90, "ωt", name_r=0.43)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos ωt", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, i1[1]), "sin ωt", "TEXT", "end", 15, dx=-12, dy=5)
    sc.note((0.45, 1.0), "view from +" + "y₁", "TEXT", "start", 13)
    sc.note((0.45, 0.88), "ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc
