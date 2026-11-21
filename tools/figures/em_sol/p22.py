"""Problem 22: heavy particle on the curve y = a(1 - cos(x/a)), first fixed and then turning about the vertical OY."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

X = 1.7                                    # abscissa of P in units of a


def _y(x):
    return 1 - math.cos(x)


@figure("p22-curve-plane",
        "Plane of the curve y = a(1 - cos(x1/a)) with k1 out of the paper, the particle P at abscissa x1, the dashed "
        "components x1 and y1 of its position, the slope triangle with legs dx1 and sin(x1/a) dx1 and hypotenuse dℓ, "
        "the basis i1, j1 at O and the unit tangent e_t and normal n at P",
        r"Plane of the curve (fixed in $S_0$ for (a)–(c), fixed in $S_1$ for (d)–(g); $\mathbf k_1$ out of the paper, "
        r"$\odot$). The dashed lines are the components $x_1$ and $y_1 = a(1 - \cos(x_1/a))$ of $\mathbf r_1^P$. In the "
        r"shaded slope triangle the leg adjacent to the tangent angle $\alpha$ is $dx_1$, the opposite leg is "
        r"$dy = \sin(x_1/a)\,dx_1$ and the hypotenuse is the arc element $d\ell$; $\mathbf e_t$ and $\mathbf n$ in orange")
def curve_plane():
    sc = Scene(940, 430, (440, 360), 108)
    P = (X, _y(X))
    s = math.sin(X)                        # slope dy/dx at P
    alpha = math.degrees(math.atan(s))
    # curve and its end lines
    sc.curve(lambda u: (u, _y(u)), -math.pi, math.pi, col="HEAD", w=3.0)
    for xe in (-math.pi, math.pi):
        sc.dashed((xe, 0.0), (xe, 2.0))
    sc.label((-math.pi, 0.0), "−πa", "TEXT", "middle", 16, dy=24)
    sc.label((math.pi, 0.0), "πa", "TEXT", "middle", 16, dy=24)
    sc.dashed((0.0, 2.0), (-0.12, 2.0))
    sc.label((0.0, 2.0), "2a", "TEXT", "end", 16, dx=-16, dy=5)
    # axes
    fixed_axis(sc, (-3.55, 0.0), 0, 7.4, S("X", "1") + " (X for the fixed curve)", off=(-84, 50))
    fixed_axis(sc, (0.0, -0.12), 90, 3.1, "Y ≡ " + S("Y", "1"), off=(40, 2))
    spin_about_vertical(sc, (0.0, 2.55), 0.24, 0.06, "Ω")
    # slope triangle at P: dx along i1, dy = sin(x/a) dx along j1, hypotenuse dℓ along the tangent
    dx = 1.0
    A = (P[0] + dx, P[1])
    B = (P[0] + dx, P[1] + s * dx)
    triangle(sc, [P, A, B])
    right_angle(sc, A, 180, 90, 0.08)
    sc.line(P, B, "EDGE", 1.2, "5 4")
    sc.line(P, A, "EDGE", 1.1)
    sc.line(A, B, "EDGE", 1.1)
    sc.label(((P[0] + A[0]) / 2, P[1]), "dx₁", "TEXT", "middle", 16, dy=21)
    sc.label((A[0] + 0.9, B[1]), "dy = sin(x₁/a) dx₁", "TEXT", "end", 16, dy=-14)
    sc.label((P[0] + 0.5 * dx, P[1] + 0.5 * s * dx), "dℓ", "TEXT", "end", 16, dx=-12, dy=-6)
    sc.angle(P, 0.5, 0, alpha, "α", name_r=0.66)
    # components of the position (dashed)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0], 0.0), "x₁", "TEXT", "middle", 16, dy=24)
    sc.label((P[0], P[1] * 0.5), "y₁ =", "TEXT", "start", 16, dx=10, dy=-6)
    sc.label((P[0], P[1] * 0.5), "a(1 − cos(x₁/a))", "TEXT", "start", 16, dx=10, dy=14)
    # bases
    sc.label((0.0, 0.0), "O", "HEAD", "end", 17, dx=-8, dy=22)
    unit(sc, (0.0, 0.0), 0, 0.5, bold("i") + S("", "1"), off=(4, 22))
    unit(sc, (0.0, 0.0), 90, 0.5, bold("j") + S("", "1"), off=(-14, 6))
    axis_out(sc, (-0.6, 2.3), None)
    sc.label((-0.6, 2.3), bold("k") + S("", "1") + " (" + bold("k") + S("", "0") + " for the fixed curve)", "BLUE", "end",
             15, weight="700", dx=-16, dy=5)
    unit(sc, P, alpha + 90, 0.5, bold("n"), "ACC", off=(-14, -6))
    unit(sc, P, alpha, 0.36, bold("e") + S("", "t"), "ACC", off=(-6, -16))
    sc.mass(P, "P", r=7, name_off=(14, 24))
    sc.gravity((-3.45, 2.75), 0.5, "g")
    return sc


@figure("p22-top-view",
        "Top view from +Y with j0 = j1 out of the paper: fixed axes i0 and k0 in grey, the axes i1 and k1 of the curve "
        "rotated counter-clockwise by Omega t in blue, with the dashed components of i1 and the plane of the curve "
        "seen edge-on",
        r"View from $+Y$, with $\mathbf j_0 = \mathbf j_1$ out of the paper ($\odot$): $\mathbf k_0$ points down the page. "
        r"The plane of the curve contains $\mathbf i_1$ and $\mathbf j_1$ and turns counter-clockwise by $\Omega t$: "
        r"$\mathbf i_1$ has the components $\cos\Omega t$ along $\mathbf i_0$ and $\sin\Omega t$ along $-\mathbf k_0$ (up the "
        r"page), hence the minus sign in $\mathbf i_1 = \cos\Omega t\,\mathbf i_0 - \sin\Omega t\,\mathbf k_0$")
def top_view():
    sc = Scene(660, 600, (250, 300), 235)
    O = (0.0, 0.0)
    a = 35.0
    ar = math.radians(a)
    # the plane of the curve seen edge-on, through O along i1
    sc.line((-0.9 * math.cos(ar), -0.9 * math.sin(ar)), (1.0 * math.cos(ar), 1.0 * math.sin(ar)), "HEAD", 5.0)
    sc.label((-0.9 * math.cos(ar), -0.9 * math.sin(ar)), "plane of the curve", "HEAD", "start", 15, dx=-20, dy=28)
    fixed_axis(sc, O, 0, 1.2, bold("i") + S("", "0"), off=(18, 6))
    fixed_axis(sc, O, -90, 1.0, bold("k") + S("", "0"), off=(18, 4))
    fixed_axis(sc, O, 90, 1.0, "−" + bold("k") + S("", "0"), off=(24, 4), dashed=True)
    i1 = unit(sc, O, a, 1.0, bold("i") + S("", "1"), off=(16, -8))
    unit(sc, O, a - 90, 1.0, bold("k") + S("", "1"), off=(20, 10))
    sc.angle(O, 0.40, 0, a, "Ωt", name_r=0.52)
    sc.angle(O, 0.30, -90, a - 90, "Ωt", name_r=0.42)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] * 0.5, 0.0), "cos Ωt", "TEXT", "middle", 16, dy=26)
    sc.label((0.0, i1[1]), "sin Ωt", "TEXT", "end", 16, dx=-12, dy=5)
    axis_out(sc, O, bold("j") + S("", "0") + " = " + bold("j") + S("", "1"), off=(-62, -8))
    sc.note((0.55, 1.12), "view from +Y", "TEXT", "start", 14)
    sc.note((0.55, 1.0), "Ω > 0: counter-clockwise", "TEXT", "start", 14)
    return sc


def _dvec(sc, a, b, col="PINK", w=2.4, head=10):
    """Dashed arrow (inertia force or auxiliary velocity) from world point a to b."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


@figure("p22-fbd",
        "Free-body diagram of the particle on the turning curve: left, the plane of the curve with the weight, the "
        "in-plane reaction N_n n and the centrifugal force; right, the view from above with the Coriolis force and "
        "the normal reaction N_b k1",
        r"Forces on $P$ in $S_1$. In the plane of the curve: weight, $N_n\,\mathbf n$ and the centrifugal force "
        r"$m\Omega^2x_1\,\mathbf i_1$ (dashed, inertia). Normal to it: the reaction $N_b\,\mathbf k_1$ and the Coriolis "
        r"force $2m\Omega\dot x_1\,\mathbf k_1$ (dashed, inertia), which balance each other.")
def fbd():
    k = 88.0
    sc = Scene(1200, 385, (300, 330), k)
    # world offset of the right panel origin (pixel (880, 255))
    RX, RY = (880 - 300) / k, (330 - 200) / k
    x1 = 1.2
    P = (x1, _y(x1))
    s = math.sin(x1)
    alpha = math.degrees(math.atan(s))
    # ---- left panel: plane of the curve, k1 out of the paper
    sc.curve(lambda u: (u, _y(u)), -math.pi, math.pi, col="HEAD", w=3.0)
    sc.line((0.0, -0.35), (0.0, 2.55), "EDGE", 1.3, "10 3 2 3")
    sc.label((0.0, 2.55), "axis (" + bold("j") + S("", "1") + ")", "TEXT", "start", 15, dx=-34, dy=-26)
    spin_about_vertical(sc, (0.0, 2.2), 0.22, 0.06, "Ω")
    axis_out(sc, (-0.7, 1.3), None, "BLUE")
    sc.label((-0.7, 1.3), bold("k") + S("", "1") + " (⊙)", "BLUE", "start", 16, weight="700", dx=14, dy=5)
    sc.label((0.0, 0.0), "O", "HEAD", "start", 17, dx=8, dy=22)
    sc.dotp((0.0, 0.0), 3.5)
    # distance to the axis
    sc.dashed((0.0, P[1]), P)
    sc.label((P[0] * 0.5, P[1]), "x₁", "TEXT", "middle", 16, dy=-9)
    # forces
    sc.vec(P, (P[0], P[1] - 0.9), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.9), "−m g " + bold("j") + S("", "1"), "PINK", "start", 16, weight="700", dx=10, dy=4)
    na = math.radians(alpha + 90)
    sc.vec(P, (P[0] + 0.8 * math.cos(na), P[1] + 0.8 * math.sin(na)), None, "PINK", 2.8, head=11)
    sc.label((P[0] + 0.8 * math.cos(na), P[1] + 0.8 * math.sin(na)), S("N", "n") + " " + bold("n"), "PINK", "end", 16,
             weight="700", dx=-8, dy=-8)
    _dvec(sc, P, (P[0] + 0.7, P[1]), "PINK", 2.6)
    sc.label((P[0] + 0.7, P[1]), S("F", "C") + " = m Ω² x₁ " + bold("i") + S("", "1"), "PINK", "start", 16, weight="700",
             dx=10, dy=-4)
    sc.label((P[0] + 0.7, P[1]), "(inertia)", "PINK", "start", 14, dx=10, dy=16)
    unit(sc, P, alpha, 0.4, bold("e") + S("", "t"), "ACC", off=(18, -4))
    unit(sc, P, alpha + 90, 0.4, bold("n"), "ACC", off=(14, -4))
    sc.mass(P, "P", r=7, name_off=(18, 26))
    # ---- right panel: view from above, j1 out of the paper, k1 down the page
    def R(x, y):
        return (RX + x, RY + y)
    sc.line(R(-math.pi, 0), R(math.pi, 0), "HEAD", 5.0)
    sc.label(R(-math.pi, 0), "view from above: the curve is seen edge-on", "TEXT", "start", 15, dy=92, dx=-4)
    unit(sc, R(0, 0), 0, 0.5, bold("i") + S("", "1"), off=(4, -12))
    unit(sc, R(0, 0), -90, 0.6, bold("k") + S("", "1"), off=(-18, 8))
    axis_out(sc, R(0, 0), None, "BLUE")
    sc.label(R(0, 0), bold("j") + S("", "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-16, dy=22)
    sc.spin(R(0, 0), 0.55, 30.0, 150.0, "Ω", name_r=0.74)
    xp = x1
    sc.mass(R(xp, 0), "P", r=7, name_off=(-20, -12))
    _dvec(sc, R(xp + 0.07, -0.05), R(xp + 0.07, -0.8), "PINK", 2.6)
    sc.label(R(xp + 0.07, -0.8), S("F", "COR") + " = 2mΩẋ₁ " + bold("k") + S("", "1"), "PINK", "start", 15, weight="700",
             dx=12, dy=-12)
    sc.label(R(xp + 0.07, -0.8), "(inertia)", "PINK", "start", 14, dx=12, dy=8)
    sc.vec(R(xp - 0.07, 0.05), R(xp - 0.07, 0.8), None, "PINK", 2.8, head=11)
    sc.label(R(xp - 0.07, 0.8), S("N", "b") + " " + bold("k") + S("", "1") + " = −2mΩẋ₁ " + bold("k") + S("", "1"),
             "PINK", "middle", 15, weight="700", dx=0, dy=-12)
    _dvec(sc, R(xp + 0.5, 0.05), R(xp + 0.5, 0.62), "GREEN", 2.2)
    sc.label(R(xp + 0.5, 0.62), "transport velocity", "GREEN", "start", 14, weight="700", dx=12, dy=6)
    sc.label(R(xp + 0.5, 0.62), "−Ω x₁ " + bold("k") + S("", "1"), "GREEN", "start", 14, weight="700", dx=12, dy=24)
    return sc
