"""Problem 06: particle on the sinusoidal curve y = sin x."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

PI = math.pi
GAM = math.degrees(math.atan(math.cos(PI / 4)))        # 35.26 deg


def _sin(x):
    return (x, math.sin(x))


def _cross(sc, p, size=5):
    x, y = sc.P(p)
    sc.c.add(f'<path d="M{x - size:.1f},{y - size:.1f} L{x + size:.1f},{y + size:.1f} '
             f'M{x - size:.1f},{y + size:.1f} L{x + size:.1f},{y - size:.1f}" stroke="HEAD" stroke-width="1.6" fill="none"/>')


def _axes_and_ticks(sc, tick_dy=20):
    fixed_axis(sc, (0.0, 0.0), 0, 6.9, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, (0.0, -1.15), 90, 2.35, bold("j") + S("", "0"), off=(-14, -2))
    names = {PI / 2: "π/2", PI: "π", 1.5 * PI: "3π/2", 2 * PI: "2π"}
    for x, nm in names.items():
        X, Y = sc.P((x, 0.0))
        sc.c.add(f'<path d="M{X:.1f},{Y - 4:.1f} L{X:.1f},{Y + 4:.1f}" stroke="EDGE" stroke-width="1.3"/>')
        sc.label((x, 0.0), nm, "TEXT", "middle", 14, italic=False, dy=tick_dy)
    for y in (1.0, -1.0):
        X, Y = sc.P((0.0, y))
        sc.c.add(f'<path d="M{X - 4:.1f},{Y:.1f} L{X + 4:.1f},{Y:.1f}" stroke="EDGE" stroke-width="1.3"/>')
        sc.label((0.0, y), "1" if y > 0 else "−1", "TEXT", "end", 14, italic=False, dx=-8, dy=5)


@figure("p06-curve-plane",
        "The sine curve with the intrinsic basis drawn on an upper arch and on a lower arch, and the differential "
        "triangle of the arc element.",
        r"Plane of the trajectory. The differential triangle has hypotenuse $ds = L\,dx$, adjacent leg $dx$ "
        r"($\cos\gamma$) and opposite leg $dy$ ($\sin\gamma$); the normal points to the concave side and flips "
        r"between arches together with the binormal.")
def curve_plane():
    sc = Scene(640, 470, (160, 178), 60)
    O = (0.0, 0.0)
    _axes_and_ticks(sc)
    axis_out(sc, O, bold("k") + S("", "0"), off=(-24, -12))
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=22)
    sc.curve(_sin, 0.0, 2 * PI, 160, "HEAD", 2.2)
    sc.label((2.0, 1.0), "y = sin x", "HEAD", "start", 17, dx=4, dy=-6)
    # inflection marks
    for x in (0.0, PI, 2 * PI):
        _cross(sc, (x, 0.0))
    sc.note((0.0, 0.65), "e_n undefined", "TEXT", "end", 12, dx=-10)
    sc.note((PI, 0.0), "e_n undefined", "TEXT", "start", 12, dx=4, dy=-26)
    sc.note((2 * PI, 0.0), "e_n undefined", "TEXT", "start", 12, dx=10, dy=-14)
    # ---- P on the upper arch
    xp = PI / 4
    P = _sin(xp)
    g = math.radians(GAM)
    L = 0.7
    unit(sc, P, GAM, L, bold("e") + S("", "t"), off=(14, -6))
    sc.vec(P, (P[0] + L * math.cos(g + math.pi / 2), P[1] + L * math.sin(g + math.pi / 2)), None, "BLUE", 1.8,
           head=9)
    sc.line(P, (P[0] + L * math.cos(g + math.pi / 2), P[1] + L * math.sin(g + math.pi / 2)), "BLUE", 1.8, "5 3")
    sc.label((P[0] + L * math.cos(g + math.pi / 2) / 2 - 0.05, P[1] + L * math.sin(g + math.pi / 2) / 2),
             bold("e") + S("", "⊥"), "BLUE", "end", 17, weight="700", dx=-6, dy=-2)
    en = (math.cos(g - math.pi / 2), math.sin(g - math.pi / 2))
    unit(sc, P, GAM - 90, L, bold("e") + S("", "n"), "ACC", off=(16, -4))
    axis_in(sc, P, None, "GREEN", 9)
    sc.line((P[0], P[1] + 0.2), (P[0], 2.2), "EDGE", 1.1, "4 3")
    sc.label((P[0], 2.35), bold("e") + S("", "b") + " = −" + bold("k") + S("", "0") + " (⊗)", "GREEN", "middle", 16,
             weight="700", dy=-8)
    sc.label((P[0], 1.72), "P (x = π/4)", "HEAD", "start", 16, dx=8)
    # ---- Q on the lower arch
    xq = 5 * PI / 4
    Q = _sin(xq)
    gq = -GAM
    unit(sc, Q, gq, 0.7, bold("e") + S("", "t"), off=(16, 10))
    nq = gq + 90
    unit(sc, Q, nq, 0.7, bold("e") + S("", "n"), "ACC", off=(0, -14))
    axis_out(sc, Q, None, "GREEN", 9)
    sc.line((Q[0], Q[1] - 0.2), (Q[0], -1.65), "EDGE", 1.1, "4 3")
    sc.label((Q[0], -1.65), bold("e") + S("", "b") + " = +" + bold("k") + S("", "0") + " (⊙)", "GREEN", "middle", 16,
             weight="700", dy=18)
    sc.label(Q, "Q (x = 5π/4)", "HEAD", "end", 16, dx=-14, dy=24)
    # ---- inset: differential triangle at P
    C = (-0.1, -3.05)
    rr = 1.8
    sc.circle(C, rr, "HEAD", 1.6)
    ang = math.atan2(P[1] - C[1], P[0] - C[0])
    top = (C[0] + rr * math.cos(ang), C[1] + rr * math.sin(ang))
    st = (P[0] - 0.2 * math.cos(ang) * -1 * -1, P[1] - 0.2 * 1.0)
    st = (P[0] + 0.2 * math.cos(ang), P[1] + 0.2 * math.sin(ang))
    sc.line(st, top, "EDGE", 1.1, "4 3")
    LL = (C[0] - 1.25, C[1] - 0.4)
    LR = (LL[0] + 1.1, LL[1])
    UR = (LR[0], LR[1] + 1.1 * math.cos(xp))
    triangle(sc, [LL, LR, UR], "BLUE", 0.14)
    sc.line(LL, LR, "EDGE", 1.4)
    sc.line(LR, UR, "EDGE", 1.4)
    sc.line(LL, UR, "HEAD", 2.2)
    right_angle(sc, LR, 90, 180, 0.1)
    sc.angle(LL, 0.45, 0, GAM, "γ", "TEXT", name_r=0.78)
    sc.label(((LL[0] + LR[0]) / 2, LL[1]), "dx", "HEAD", "middle", 16, dy=20)
    sc.label((LR[0], (LR[1] + UR[1]) / 2), "dy = cos x dx", "HEAD", "start", 15, dx=8, dy=5)
    sc.label((C[0] - 1.1, C[1] + 0.45), "ds = L dx", "HEAD", "middle", 15)
    sc.note((C[0], C[1] + 1.3), "zoom at P", "TEXT", "middle", 12)
    return sc


@figure("p06-rotation-view",
        "View along k0 of the fixed axes and of the tangent and auxiliary normal turned by the tangent angle gamma.",
        r"The tangent basis is the fixed basis turned by $\gamma$ about $\mathbf k_0$ (out of the paper); the "
        r"component of $\mathbf e_\perp$ along $\mathbf i_0$ is negative because $\mathbf e_\perp$ leans toward "
        r"$-\mathbf i_0$.")
def rotation_view():
    sc = Scene(560, 420, (220, 275), 190)
    O = (0.0, 0.0)
    g = math.radians(GAM)
    c, s = math.cos(g), math.sin(g)
    fixed_axis(sc, O, 0, 1.1, bold("i") + S("", "0"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.1, bold("j") + S("", "0"), off=(16, 4))
    fixed_axis(sc, O, 180, 0.75, "", dashed=True)
    tt = (c, s)
    tp = (-s, c)
    triangle(sc, [O, (c, 0.0), tt], "BLUE", 0.12)
    triangle(sc, [O, (-s, 0.0), tp], "ACC", 0.12)
    sc.dashed((c, 0.0), tt)
    sc.dashed((0.0, s), tt)
    sc.dashed((-s, 0.0), tp)
    sc.dashed((0.0, c), tp)
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (-s, 0.0), 0, 90, 0.05)
    unit(sc, O, GAM, 1.0, bold("e") + S("", "t"), off=(18, -8))
    unit(sc, O, GAM + 90, 1.0, bold("e") + S("", "⊥"), off=(-8, -12))
    axis_out(sc, O, bold("k") + S("", "0") + " (⊙)", off=(30, 52))
    sc.angle(O, 0.30, 0, GAM, "γ", "GREEN", name_r=0.42)
    sc.angle(O, 0.30, 90, 90 + GAM, "γ", "GREEN", name_r=0.42)
    sc.label((c / 2, 0.0), "cos γ = 1/L", "TEXT", "middle", 15, dy=24)
    sc.label((c, s / 2), "sin γ = cos x / L", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, 0.0), "−sin γ", "TEXT", "middle", 15, dy=24)
    sc.label((0.0, c), "cos γ", "TEXT", "start", 15, dx=10, dy=5)
    sc.note((-0.95, -0.62), "on an upper arch γ decreases (tangent turns clockwise)", "TEXT", "start", 13)
    return sc


@figure("p06-osculating-circles",
        "Osculating circles of the sine curve at a crest, a trough and an intermediate point.",
        r"The radius of curvature is $1$ m at the crests and troughs, grows away from them ($2.598$ m at "
        r"$x=\pi/4$) and tends to infinity at the inflection points.")
def osculating_circles():
    sc = Scene(560, 290, (70, 120), 60)
    O = (0.0, 0.0)
    fixed_axis(sc, O, 0, 6.9, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, (0.0, -1.35), 90, 2.7, bold("j") + S("", "0"), off=(14, 4))
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=18)
    sc.curve(_sin, 0.0, 2 * PI, 160, "HEAD", 2.2)
    # crest
    C1, T1 = (PI / 2, 1.0), (PI / 2, 0.0)
    sc.circle(T1, 1.0, "ACC", 1.5, "6 4")
    sc.dashed(C1, T1, "ACC")
    sc.dotp(T1, 3.0, "ACC")
    sc.vec(C1, (C1[0], C1[1] - 0.6), None, "ACC", 2.6, head=10)
    sc.label((C1[0], C1[1] - 0.6), bold("e") + S("", "n"), "ACC", "end", 17, weight="700", dx=-8, dy=4)
    unit(sc, C1, 0, 0.8, bold("e") + S("", "t"), off=(6, -10))
    sc.label((C1[0], 0.45), "ρ = 1 m", "ACC", "start", 14, dx=8, dy=5)
    sc.mass(C1, None, r=4, col="HEAD")
    # trough
    C2, T2 = (1.5 * PI, -1.0), (1.5 * PI, 0.0)
    sc.circle(T2, 1.0, "ACC", 1.5, "6 4")
    sc.dashed(C2, T2, "ACC")
    sc.dotp(T2, 3.0, "ACC")
    sc.vec(C2, (C2[0], C2[1] + 0.6), None, "ACC", 2.6, head=10)
    sc.label((C2[0], C2[1] + 0.6), bold("e") + S("", "n"), "ACC", "start", 17, weight="700", dx=8, dy=4)
    unit(sc, C2, 0, 0.8, bold("e") + S("", "t"), off=(6, 16))
    sc.label((C2[0], -0.2), "ρ = 1 m", "ACC", "end", 14, dx=-8, dy=5)
    sc.mass(C2, None, r=4, col="HEAD")
    # intermediate point
    P = _sin(PI / 4)
    g = math.radians(GAM)
    en = (math.cos(g - math.pi / 2), math.sin(g - math.pi / 2))
    rho = 2.598
    Cp = (P[0] + rho * en[0], P[1] + rho * en[1])
    a0 = math.degrees(math.atan2(P[1] - Cp[1], P[0] - Cp[0]))
    sc.arc(Cp, rho, a0 - 22, a0 + 22, "ACC", 1.3, "3 3")
    sc.line(P, Cp, "ACC", 1.1, "2 3")
    sc.dotp(Cp, 3.0, "ACC")
    sc.mass(P, None, r=4, col="HEAD")
    sc.label(P, "P", "HEAD", "end", 16, dx=-8, dy=-8)
    sc.label(Cp, "ρ = 2.598 m", "ACC", "start", 16, dx=10, dy=20)
    # inflection point
    _cross(sc, (PI, 0.0), 6)
    sc.label((PI, 0.0), "ρ → ∞", "TEXT", "middle", 15, dy=-14)
    return sc
