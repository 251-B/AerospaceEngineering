"""Problem 22: heavy particle on the curve y = a(1 - cos(x/a)), first fixed and then turning about the vertical OY."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

X = 1.7                                    # abscissa of P in units of a


def _y(x):
    return 1 - math.cos(x)


@figure("p22-curve-plane",
        "Plane of the curve y = a(1 - cos(x/a)) with the particle P at abscissa x1, the dashed components x1 and y(x1) "
        "of its position, the slope triangle with legs dx1 and sin(x1/a) dx1 and hypotenuse ds, the basis i1, j at O and "
        "the unit tangent e_t and normal n at P",
        r"Plane of the curve (fixed in $S_0$ for (a)–(c), fixed in $S_1$ for (d)–(g)). The dashed lines are the "
        r"components $x_1$ and $y(x_1) = a(1 - \cos(x_1/a))$ of the position. In the shaded slope triangle the leg "
        r"adjacent to the tangent angle $\alpha$ is $dx_1$, the opposite leg is $dy = \sin(x_1/a)\,dx_1$ and the "
        r"hypotenuse is the arc element $ds$. $\mathbf i_1, \mathbf j$ in blue, $\mathbf e_t, \mathbf n$ in orange")
def curve_plane():
    sc = Scene(740, 380, (350, 310), 88)
    P = (X, _y(X))
    s = math.sin(X)                        # slope dy/dx at P
    alpha = math.degrees(math.atan(s))
    # curve and its end lines
    sc.curve(lambda u: (u, _y(u)), -math.pi, math.pi, col="HEAD", w=3.0)
    for xe in (-math.pi, math.pi):
        sc.dashed((xe, 0.0), (xe, 2.0))
    sc.label((-math.pi, 0.0), "−πa", "TEXT", "middle", 15, dy=22)
    sc.label((math.pi, 0.0), "πa", "TEXT", "middle", 15, dy=22)
    sc.dashed((0.0, 2.0), (-0.12, 2.0))
    sc.label((0.0, 2.0), "2a", "TEXT", "end", 15, dx=-16, dy=5)
    # axes
    fixed_axis(sc, (-3.55, 0.0), 0, 7.4, S("X", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.12), 90, 2.95, "Y ≡ " + S("Y", "1"), off=(36, 2))
    spin_about_vertical(sc, (0.0, 2.42), 0.22, 0.06, "Ω")
    # slope triangle at P: dx along i1, dy = sin(x/a) dx along j, hypotenuse ds along the tangent
    dx = 1.0
    A = (P[0] + dx, P[1])
    B = (P[0] + dx, P[1] + s * dx)
    triangle(sc, [P, A, B])
    right_angle(sc, A, 180, 90, 0.08)
    sc.line(P, B, "EDGE", 1.2, "5 4")
    sc.line(P, A, "EDGE", 1.1)
    sc.line(A, B, "EDGE", 1.1)
    sc.label(((P[0] + A[0]) / 2, P[1]), "dx₁", "TEXT", "middle", 15, dy=19)
    sc.label((A[0], (A[1] + B[1]) / 2), "sin(x₁/a) dx₁", "TEXT", "start", 15, dx=9, dy=5)
    sc.label((P[0] + 0.78 * dx, P[1] + 0.78 * s * dx), "ds", "TEXT", "end", 15, dx=-10, dy=-4)
    sc.angle(P, 0.5, 0, alpha, "α", name_r=0.62)
    # components of the position (dashed)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0], 0.0), "x₁", "TEXT", "middle", 15, dy=22)
    sc.label((P[0], P[1] * 0.42), "y(x₁)", "TEXT", "start", 15, dx=8)
    # bases
    sc.label((0.0, 0.0), "O", "HEAD", "end", 17, dx=-8, dy=20)
    unit(sc, (0.0, 0.0), 0, 0.5, bold("i") + S("", "1"), off=(6, 22))
    unit(sc, (0.0, 0.0), 90, 0.5, bold("j"), off=(-14, 6))
    unit(sc, P, alpha + 90, 0.5, bold("n"), "ACC", off=(-12, -6))
    unit(sc, P, alpha, 0.36, bold("e") + S("", "t"), "ACC", off=(-20, -4))
    sc.mass(P, "P", r=7, name_off=(-20, 6))
    sc.gravity((-2.5, 2.75), 0.45, "g")
    return sc


@figure("p22-top-view",
        "Top view from +Y with j out of the paper: inertial axes i to the right and k downwards in grey, the axes i1 and "
        "k1 of the curve rotated counter-clockwise by Omega t in blue, with the dashed components of i1",
        r"View from $+Y$, with $\mathbf j$ out of the paper ($\odot$): $\mathbf k = \mathbf i\times\mathbf j$ points down "
        r"the page. The plane of the curve contains $\mathbf i_1$ and $\mathbf j$ and turns counter-clockwise by "
        r"$\Omega t$: the components of $\mathbf i_1$ are $\cos\Omega t$ along $\mathbf i$ and $\sin\Omega t$ along "
        r"$-\mathbf k$ (up the page), hence the minus sign in $\mathbf i_1 = \cos\Omega t\,\mathbf i - \sin\Omega t\,\mathbf k$")
def top_view():
    sc = Scene(480, 440, (170, 215), 165)
    O = (0.0, 0.0)
    a = 35.0
    fixed_axis(sc, O, 0, 1.15, bold("i"), off=(14, 5))
    fixed_axis(sc, O, -90, 1.0, bold("k"), off=(14, 4))
    fixed_axis(sc, O, 90, 0.95, "−" + bold("k"), off=(18, 4), dashed=True)
    axis_out(sc, O, bold("j"), off=(-24, 24))
    i1 = unit(sc, O, a, 1.0, bold("i") + S("", "1"), off=(14, -6))
    unit(sc, O, a - 90, 1.0, bold("k") + S("", "1"), off=(16, 8))
    sc.angle(O, 0.42, 0, a, "Ωt", name_r=0.56)
    sc.angle(O, 0.30, -90, a - 90, "Ωt", name_r=0.43)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, i1[1]), "sin Ωt", "TEXT", "end", 15, dx=-12, dy=5)
    sc.note((0.45, 1.0), "view from +Y", "TEXT", "start", 13)
    sc.note((0.45, 0.88), "Ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc
