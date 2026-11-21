"""Problem 27: bead on the sine-shaped wire y1 = sin x1, joined by a vertical spring to the rail y1 = 2, turning about Oy1."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

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


def _dvec(sc, a, b, col="PINK", w=2.4, head=10):
    """Dashed arrow (inertia force) from world point a to b."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


XF = 2.2                                   # abscissa of the bead in the free-body diagram (m)


@figure("p27-fbd",
        "Free-body diagram of the bead on the turning sine wire: top, the plane of the wire with the weight, the spring "
        "force, the in-plane reaction N_y n and the centrifugal force; bottom, the view from above with the Coriolis "
        "force and the normal reaction N_z k1",
        r"Forces on $P$ in $S_1$. In the plane of the wire: weight, spring $k(2 - \sin x_1)\,\mathbf j_1$, reaction "
        r"$N_y\,\mathbf n$ and the centrifugal force $m\omega^2x_1\,\mathbf i_1$ (dashed, inertia). Normal to it: the "
        r"reaction $N_z\,\mathbf k_1$ and the Coriolis force $2m\omega\dot x_1\,\mathbf k_1$ (dashed, inertia), which "
        r"balance each other.")
def fbd():
    k = 82.0
    sc = Scene(760, 670, (90, 300), k)
    RY = -(520 - 300) / k                              # world y of the origin of the lower panel (pixel y = 570)
    P = (XF, math.sin(XF))
    c = math.cos(XF)
    X2 = 2 * math.pi
    # ---- upper panel: plane of the wire, k1 out of the paper
    sc.curve(lambda u: (u, math.sin(u)), 0.0, X2, col="HEAD", w=3.0)
    sc.line((0.0, 2.0), (X2, 2.0), "HEAD", 1.6)
    sc.label((X2, 2.0), "rail y₁ = 2", "TEXT", "end", 15, dy=-10)
    sc.line((0.0, -1.3), (0.0, 3.0), "EDGE", 1.3, "10 3 2 3")
    sc.label((0.0, 3.0), "axis (" + bold("j") + S("", "1") + ")", "TEXT", "start", 15, dx=14, dy=4)
    spin_about_vertical(sc, (0.0, 2.55), 0.2, 0.05, "ω")
    sc.label((0.0, 0.0), "O", "HEAD", "end", 17, dx=-10, dy=22)
    axis_out(sc, (0.8, -0.75), None, "BLUE")
    sc.label((0.8, -0.75), bold("k") + S("", "1") + " (⊙)", "BLUE", "start", 16, weight="700", dx=14, dy=5)
    # distance to the axis
    sc.dashed((0.0, P[1]), P)
    sc.label((1.1, P[1]), "x₁", "TEXT", "middle", 16, dy=34)
    # spring from P up to the rail
    sc.spring(P, (P[0], 2.0), coils=6, amp=5)
    sc.label((P[0], (P[1] + 2.0) / 2), "k", "TEXT", "start", 16, dx=12)
    # forces
    sc.vec(P, (P[0], P[1] - 0.8), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.8), "−m g " + bold("j") + S("", "1"), "PINK", "start", 16, weight="700", dx=10, dy=4)
    xs_ = P[0] - 0.14
    sc.vec((xs_, P[1] + 0.05), (xs_, P[1] + 0.9), None, "PINK", 2.8, head=11)
    sc.label((xs_, P[1] + 0.9), "k(2 − sin x₁) " + bold("j") + S("", "1"), "PINK", "end", 16, weight="700", dx=-6, dy=-4)
    an = math.atan2(1.0, -c)
    sc.vec(P, (P[0] + 0.6 * math.cos(an), P[1] + 0.6 * math.sin(an)), None, "PINK", 2.8, head=11)
    sc.label((P[0] + 0.6 * math.cos(an), P[1] + 0.6 * math.sin(an)), S("N", "y") + " " + bold("n"), "PINK", "start", 16,
             weight="700", dx=8, dy=-6)
    _dvec(sc, P, (P[0] + 0.7, P[1]), "PINK", 2.6)
    sc.label((P[0] + 0.7, P[1]), S("F", "C") + " = m ω² x₁ " + bold("i") + S("", "1"), "PINK", "start", 15, weight="700",
             dx=10, dy=-4)
    sc.label((P[0] + 0.7, P[1]), "(inertia)", "PINK", "start", 14, dx=10, dy=14)
    at = math.degrees(math.atan2(c, 1.0))
    unit(sc, P, at, 0.32, bold("t"), "ACC", off=(12, 16))
    unit(sc, P, at + 90, 0.32, bold("n"), "ACC", off=(14, 8))
    sc.mass(P, "P", r=7, name_off=(-14, 26))
    # ---- lower panel: view from above, j1 out of the paper, k1 down the page
    def R(x, y):
        return (x, RY + y)
    sc.line(R(0, 0), R(X2, 0), "HEAD", 5.0)
    sc.label(R(X2, 0), "view from above: the wire is seen edge-on", "TEXT", "end", 15, dy=125)
    unit(sc, R(0, 0), 0, 0.5, bold("i") + S("", "1"), off=(4, -12))
    unit(sc, R(0, 0), -90, 0.5, bold("k") + S("", "1"), off=(-18, 6))
    axis_out(sc, R(0, 0), None, "BLUE")
    sc.label(R(0, 0), bold("j") + S("", "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-16, dy=-6)
    sc.spin(R(0, 0), 0.45, 30.0, 150.0, "ω", name_r=0.62)
    sc.mass(R(XF, 0), "P (seen from above)", r=7, name_off=(80, -16), size=16)
    _dvec(sc, R(XF + 0.07, -0.05), R(XF + 0.07, -0.65), "PINK", 2.6)
    sc.label(R(XF + 0.07, -0.65), S("F", "COR") + " = 2mωẋ₁ " + bold("k") + S("", "1"), "PINK", "start", 15, weight="700",
             dx=12, dy=2)
    sc.label(R(XF + 0.07, -0.65), "(inertia)", "PINK", "start", 14, dx=12, dy=20)
    sc.vec(R(XF - 0.07, 0.05), R(XF - 0.07, 0.65), None, "PINK", 2.8, head=11)
    sc.label(R(XF - 0.07, 0.65), S("N", "z") + " " + bold("k") + S("", "1") + " = −2mωẋ₁ " + bold("k") + S("", "1"),
             "PINK", "end", 15, weight="700", dx=6, dy=-8)
    return sc


@figure("p27-potential",
        "Scaled potential of the bead without spring, V = 2 sin x1 - beta x1^2, for a small, the critical and a large "
        "value of beta, with the starting level of each",
        r"Scaled potential $\tilde V = 2\sin x_1 - \beta x_1^2$ for three values of $\beta$. The bead, released at rest "
        r"at $\pi$, moves where $\tilde V$ is below its starting level (dotted): for small $\beta$ the hump near "
        r"$5\pi/2$ stops it, for large $\beta$ nothing does; at $\beta_c$ the top of the hump touches the starting "
        r"level at $x_c$.")
def potential():
    sx, sy = 70.0, 50.0
    ymin, ymax, xmax = -8.0, 3.0, 12.0
    sc = Scene(990, 660, (100, 55 + ymax * sy), 1.0)

    def Q(x, y):
        return (x * sx, y * sy)

    def V(b, x):
        return 2 * math.sin(x) - b * x * x
    # frame: left axis, bottom axis, zero line
    sc.vec(Q(0, ymin), Q(0, ymax + 0.2), None, "EDGE", 1.6, head=9)
    sc.vec(Q(0, ymin), Q(xmax + 0.3, ymin), None, "EDGE", 1.6, head=9)
    sc.line(Q(0, 0), Q(xmax, 0), "EDGE", 1.2)
    for v in range(-8, 4):
        if v == 0:
            sc.label(Q(0, 0), "0", "TEXT", "end", 14, italic=False, dx=-8, dy=5)
            continue
        sc.line(Q(0, v), Q(xmax, v), "EDGE", 0.6, "2 4")
        sc.label(Q(0, v), f"{v}".replace("-", "−"), "TEXT", "end", 14, italic=False, dx=-8, dy=5)
    for t, nm in ((math.pi, "π"), (1.5 * math.pi, "3π/2"), (2 * math.pi, "2π"), (2.5 * math.pi, "5π/2"), (3 * math.pi, "3π")):
        sc.line(Q(t, ymin), Q(t, ymin + 0.12), "EDGE", 1.4)
        sc.label(Q(t, ymin), nm, "TEXT", "middle", 15, italic=False, dy=24)
    sc.label(Q(xmax + 0.3, ymin), "x₁ [m]", "TEXT", "end", 16, dy=50)
    sc.label(Q(0, ymax + 0.2), "Ṽ = 2 sin x₁ − β x₁² [m]", "TEXT", "start", 16, dx=12, dy=-8)

    def clipped(b):
        pts, cur = [], []
        for i in range(0, 721):
            x = xmax * i / 720
            y = V(b, x)
            if y >= ymin:
                cur.append(Q(x, y))
            elif cur:
                pts.append(cur)
                cur = []
        if cur:
            pts.append(cur)
        return pts
    curves = ((0.02, "BLUE", None), (0.040489, "ACC", "9 5"), (0.1, "PINK", "2 5 11 5"))
    for b, col, dash in curves:
        for seg in clipped(b):
            sc.poly(seg, col, 3.2, dash)
    # starting levels (dotted) and the release point
    xr = math.pi
    xt = 8.7
    for _ in range(60):                                  # turning point of beta = 0.02: V(x) = V(pi), beyond the hump
        f = V(0.02, xt) - V(0.02, xr)
        xt += f / (2 * math.cos(xt) - 0.04 * xt) * -1.0
    sc.line(Q(xr, V(0.02, xr)), Q(xt, V(0.02, xr)), "BLUE", 1.6, "2 4")
    sc.line(Q(xr, V(0.040489, xr)), Q(7.544, V(0.040489, xr)), "ACC", 1.6, "2 4")
    sc.line(Q(xr, V(0.1, xr)), Q(xmax, V(0.1, xr)), "PINK", 1.6, "2 4")
    for b, col, dash in curves:
        sc.mass(Q(xr, V(b, xr)), None, r=4.5, col=col)
    sc.dashed(Q(xr, ymin), Q(xr, 0.9))
    sc.label(Q(xr, 0.9), "release at π", "TEXT", "start", 15, dx=-30, dy=-8)
    # turning point and x_c
    sc.circle(Q(xt, V(0.02, xr)), 5.5, "BLUE", 2.0, fill="none")
    sc.label(Q(xt, V(0.02, xr)), "turning point", "BLUE", "start", 15, weight="700", dx=14, dy=-12)
    sc.mass(Q(7.544, V(0.040489, 7.544)), None, r=5.5, col="ACC")
    sc.label(Q(7.544, V(0.040489, 7.544)), S("x", "c"), "ACC", "middle", 16, weight="700", dy=-14)
    # start arrow along the axis
    sc.vec(Q(xr, ymin + 0.45), Q(xr + 1.3, ymin + 0.45), None, "GREEN", 2.2, head=10)
    sc.label(Q(xr + 1.3, ymin + 0.45), "start: Ṽ′(π) < 0", "GREEN", "start", 15, weight="700", dx=10, dy=5)
    # legend
    lx, ly = 7.0, 2.7
    for i, (b, col, dash) in enumerate(curves):
        y = ly - 0.55 * i
        sc.line(Q(lx, y), Q(lx + 0.7, y), col, 3.2, dash)
    sc.label(Q(lx + 0.7, ly), "β = 0.02 (small): oscillation", "TEXT", "start", 15, dx=10, dy=5)
    sc.label(Q(lx + 0.7, ly - 0.55), "β = " + S("β", "c") + " = 0.0405", "TEXT", "start", 15, dx=10, dy=5)
    sc.label(Q(lx + 0.7, ly - 1.1), "β = 0.1 (large): escape", "TEXT", "start", 15, dx=10, dy=5)
    sc.note(Q(lx, ly - 1.65), "dotted: starting level Ṽ(π) = −β π²", "TEXT", "start", 14)
    return sc
