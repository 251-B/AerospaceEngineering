"""Problem 03: astroid x = a cos^3 phi, y = a sin^3 phi, smooth arc of the first quadrant."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

PH = 30.0            # drawn phi, degrees


def _a(deg):
    t = math.radians(deg)
    return math.cos(t) ** 3, math.sin(t) ** 3


def _d(deg, r=1.0):
    return r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg))


@figure("p03-astroid-plane",
        "Astroid with the first-quadrant smooth arc highlighted, the position vector of P with its two projections and "
        "the intrinsic vectors at P.",
        r"The particle runs along the smooth arc between the cusps $(a, 0)$ and $(0, a)$. The position vector has "
        r"projections $a\cos^3\varphi$ and $a\sin^3\varphi$; the normal $\mathbf e_n$ points away from $O$, toward the "
        r"centre of curvature outside the arc.")
def astroid_plane():
    sc = Scene(720, 640, (290, 350), 225)
    O = (0.0, 0.0)
    P = _a(PH)
    cph, sph = math.cos(math.radians(PH)), math.sin(math.radians(PH))
    rho = 3 * sph * cph
    C = (P[0] + rho * sph, P[1] + rho * cph)
    sc.curve(lambda t: _a(math.degrees(t)), 0, 2 * math.pi, 240, col="EDGE", w=1.2)
    fixed_axis(sc, (-1.2, 0.0), 0, 2.4, bold("i") + S("", "0"), off=(14, 5))
    fixed_axis(sc, (0.0, -1.2), 90, 2.4, bold("j") + S("", "0"), off=(14, 2))
    for q in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        sc.dotp(q, 3.2, "EDGE")
    triangle(sc, [O, (P[0], 0.0), P], "BLUE", 0.14)
    sc.dashed((P[0], 0.0), P)
    right_angle(sc, (P[0], 0.0), 180, 90, 0.035)
    sc.curve(lambda t: _a(math.degrees(t)), 0, math.pi / 2, 120, col="HEAD", w=3.4)
    sc.vec(_a(52), _a(60), None, "HEAD", 3.0, head=12)
    sc.vec(O, P, None, "HEAD", 2.0, head=10)
    sc.line(P, C, "GREEN", 1.2, "6 4")
    ang = 180 + PH
    sc.arc(C, rho, ang - 12, ang + 12, "GREEN", 1.4, "3 3")
    unit(sc, P, 180 - PH, 0.36, bold("e") + S("", "t"), "ACC", off=(-12, -10))
    unit(sc, P, 90 - PH, 0.36, bold("e") + S("", "n"), "GREEN", off=(14, -6))
    axis_in(sc, (0.90, 0.32), None, "HEAD", r_px=8)
    sc.label((0.90, 0.32), bold("e") + S("", "b") + " = −" + bold("k") + S("", "0"), "HEAD", "start", 15, dx=16, dy=5)
    sc.dotp(P, 4.5)
    sc.dotp(C, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    sc.label(P, "P", "HEAD", "start", 17, dx=14, dy=-4)
    sc.label(C, "C", "HEAD", "start", 17, dx=10, dy=-4)
    sc.label((P[0] * 0.5, P[1] * 0.5), bold("r") + S("", "0", "P"), "HEAD", "middle", 15, dx=-8, dy=-24)
    sc.label((P[0] * 0.5, 0.0), "a cos³(φ)", "TEXT", "middle", 15, dy=24)
    sc.line((P[0], P[1] / 2), (0.70, -0.10), "EDGE", 1.0)
    sc.label((0.72, -0.10), "a sin³(φ)", "TEXT", "middle", 15, dx=0, dy=22)
    sc.label((C[0] * 0.55 + P[0] * 0.45, C[1] * 0.55 + P[1] * 0.45), "ρ = 3a sin(φ) cos(φ)", "GREEN", "start", 15,
             dx=14, dy=4)
    sc.note((1.0, 0.0), "(a, 0)", "TEXT", "start", 14, dx=8, dy=22)
    sc.note((1.0, 0.0), "φ = 0, t = 0, at rest", "TEXT", "start", 13, dx=8, dy=42)
    sc.note((0.0, 1.0), "(0, a)", "TEXT", "end", 14, dx=-10, dy=-6)
    sc.note((0.0, 1.0), "φ = π/2, t = √(3a/k)", "TEXT", "start", 13, dx=10, dy=6)
    sc.note((0.18, 0.70), "smooth arc used", "HEAD", "start", 14, dx=30, dy=10)
    axis_out(sc, (-0.8, 0.8), bold("k") + S("", "0"), off=(0, 30))
    return sc


@figure("p03-parameter-angle",
        "Auxiliary circle showing that the parameter phi is the angle of the circle point Q, while the particle P is "
        "seen from O at the smaller polar angle vartheta.",
        r"The parameter $\varphi$ is the angle of the auxiliary point $Q$, not the polar angle of $P$. The two angles "
        r"coincide only at $0$, $\pi/4$ and $\pi/2$.")
def parameter_angle():
    sc = Scene(640, 600, (110, 510), 400)
    O = (0.0, 0.0)
    Q = _d(PH)
    P = _a(PH)
    vt = math.degrees(math.atan2(P[1], P[0]))
    fixed_axis(sc, (-0.1, 0.0), 0, 1.25, bold("i") + S("", "0"), off=(12, 5))
    fixed_axis(sc, (0.0, -0.1), 90, 1.2, bold("j") + S("", "0"), off=(12, 2))
    sc.arc(O, 1.0, 0, 90, "EDGE", 1.2, "5 4")
    sc.curve(lambda t: _a(math.degrees(t)), 0, math.pi / 2, 120, col="HEAD", w=3.4)
    sc.line(O, Q, "EDGE", 1.2, "5 4")
    sc.line(O, P, "HEAD", 2.0)
    sc.dashed(Q, (Q[0], 0.0))
    sc.dashed(P, (P[0], 0.0))
    sc.angle(O, 0.22, 0, PH, "φ", name_r=0.30)
    sc.arc(O, 0.50, 0, vt, "GREEN", 1.5)
    sc.label(_d(vt / 2, 0.60), "ϑ", "GREEN", "middle", 16, dy=5)
    m = _a(45)
    sc.circle(m, 0.012, "HEAD", 1.6, fill="none")
    sc.dotp(Q, 4.0, "EDGE")
    sc.dotp(P, 4.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    sc.label(Q, "Q (a cos φ, a sin φ)", "TEXT", "start", 15, dx=10, dy=-6)
    sc.label((P[0], 0.0), "P (a cos³φ, a sin³φ)", "HEAD", "middle", 15, dy=52)
    sc.note(m, "φ = ϑ = π/4", "HEAD", "start", 14, dx=-20, dy=-24)
    sc.note((0.5, 0.95), "tan ϑ = tan³φ", "TEXT", "start", 14, dx=60, dy=0)
    sc.label((1.0, 0.0), "a", "TEXT", "middle", 16, dy=24)
    axis_out(sc, (0.1, 0.9), bold("k") + S("", "0"), off=(0, 30))
    return sc


@figure("p03-arc-element",
        "Infinitesimal right triangle at P with legs dx and dy and hypotenuse ds, the tangent rising at angle phi above "
        "the negative x direction.",
        r"The hint of the statement is Pythagoras on the infinitesimal triangle: the legs are the changes of $x$ and "
        r"$y$, the hypotenuse is the arc element $ds = 3a\sin\varphi\cos\varphi\,d\varphi$.")
def arc_element():
    sc = Scene(640, 420, (470, 250), 330)
    P = (0.0, 0.0)
    ds = 0.62
    Pp = (-ds * math.cos(math.radians(PH)), ds * math.sin(math.radians(PH)))
    F = (Pp[0], 0.0)
    triangle(sc, [P, F, Pp], "BLUE", 0.14)
    sc.dashed(P, F)
    sc.dashed(F, Pp)
    right_angle(sc, F, 0, 90, 0.04)
    sc.vec((0.0, -0.09), (-0.3, -0.09), None, "EDGE", 1.6, head=9)
    sc.label((-0.3, -0.09), "−" + bold("i") + S("", "0"), "TEXT", "end", 15, dx=-8, dy=5)
    sc.line(P, Pp, "HEAD", 3.6)
    unit(sc, P, 180 - PH, 0.40, bold("e") + S("", "t"), "ACC", off=(-6, -14))
    sc.arc(P, 0.20, 180 - PH, 180, "GREEN", 1.5)
    sc.label(_d(180 - PH / 2, 0.265), "φ", "GREEN", "middle", 16, dy=5, dx=-6)
    sc.dotp(P, 4.5)
    sc.dotp(Pp, 4.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=10, dy=22)
    sc.label(Pp, "P′", "HEAD", "end", 17, dx=-10, dy=-4)
    sc.label((F[0] / 2, -0.09), "|dx| = 3a cos²φ sin φ dφ", "TEXT", "middle", 15, dy=30)
    sc.label(F, "dx (negative)", "TEXT", "end", 13, dx=-8, dy=5)
    sc.label((F[0], Pp[1] / 2), "dy = 3a sin²φ cos φ dφ", "TEXT", "end", 15, dx=-10, dy=5)
    sc.label((Pp[0] / 2, Pp[1] / 2), "ds = 3a sin φ cos φ dφ", "HEAD", "start", 15, dx=26, dy=-22)
    sc.note((-0.30, -0.09), "ds² = dx² + dy²", "TEXT", "middle", 15, dy=76)
    axis_out(sc, (0.2, 0.5), bold("k") + S("", "0"), off=(0, 30))
    return sc


@figure("p03-intrinsic-rotation",
        "View along k0 with the tangent at angle phi above the negative x direction and the normal at angle phi from "
        "j0, turned clockwise from the tangent so the binormal points into the paper.",
        r"The tangent makes the angle $\varphi$ with $-\mathbf i_0$ (hence the minus sign of its $\mathbf i_0$ "
        r"component) and the normal makes $\varphi$ with $\mathbf j_0$. The turn from $\mathbf e_t$ to $\mathbf e_n$ is "
        r"clockwise in this view, so $\mathbf e_b = -\mathbf k_0$ points into the paper.")
def intrinsic_rotation():
    sc = Scene(620, 500, (330, 330), 230)
    P = (0.0, 0.0)
    c, s = math.cos(math.radians(PH)), math.sin(math.radians(PH))
    et, en = (-c, s), (s, c)
    triangle(sc, [P, (-c, 0.0), et], "ACC", 0.13)
    triangle(sc, [P, (0.0, c), en], "GREEN", 0.13)
    sc.dashed((-c, 0.0), et)
    sc.dashed((0.0, c), en)
    right_angle(sc, (-c, 0.0), 0, 90, 0.05)
    right_angle(sc, (0.0, c), 270, 0, 0.05)
    fixed_axis(sc, P, 0, 1.15, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, P, 90, 1.15, bold("j") + S("", "0"), off=(16, 2))
    fixed_axis(sc, P, 180, 1.15, "−" + bold("i") + S("", "0"), off=(-8, -12), dashed=True)
    unit(sc, P, 180 - PH, 1.0, bold("e") + S("", "t"), "ACC", off=(-16, -6))
    unit(sc, P, 90 - PH, 1.0, bold("e") + S("", "n"), "GREEN", off=(14, -8))
    right_angle(sc, P, 180 - PH, 90 - PH, 0.09)
    sc.arc(P, 0.30, 180 - PH, 180, "ACC", 1.5)
    sc.label(_d(180 - PH / 2, 0.40), "φ", "ACC", "middle", 16, dx=-4, dy=5)
    sc.arc(P, 0.30, 90 - PH, 90, "GREEN", 1.5)
    sc.label(_d(90 - PH / 2, 0.40), "φ", "GREEN", "middle", 16, dx=6, dy=2)
    from figures.svgkit import arrow_head
    sc.arc(P, 0.62, 90 - PH + 4, 180 - PH - 4, "PINK", 1.8)
    a = math.radians(90 - PH + 4)
    q = sc.P(_d(90 - PH + 4, 0.62))
    arrow_head(sc.c, (q[0] - math.sin(a) * 4, q[1] - math.cos(a) * 4), (q[0] + math.sin(a) * 3, q[1] + math.cos(a) * 3),
               "PINK", 10)
    sc.label((-0.03, 0.80), "clockwise turn: " + bold("e") + S("", "b") + " = −" + bold("k") + S("", "0") + " (into the paper)",
             "PINK", "end", 14)
    axis_in(sc, (0.55, -0.55), bold("e") + S("", "b") + " = −" + bold("k") + S("", "0") + " (into the paper)", "HEAD",
            off=(16, 28))
    axis_out(sc, (-0.75, -0.55), bold("k") + S("", "0") + " (out)", off=(0, 28))
    sc.label((-c / 2, 0.0), "cos φ", "TEXT", "middle", 15, dy=22)
    sc.label((-c, s / 2), "sin φ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((-c / 2, s / 2), "1", "TEXT", "middle", 15, dx=-4, dy=-10)
    sc.label((0.0, c / 2), "cos φ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((s / 2, c), "sin φ", "TEXT", "middle", 15, dy=-10)
    sc.label((s / 2, c / 2), "1", "TEXT", "middle", 15, dx=12, dy=8)
    sc.dotp(P, 4.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=8, dy=22)
    return sc
