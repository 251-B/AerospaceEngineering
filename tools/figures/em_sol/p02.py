"""Problem 02: logarithmic spiral r = alpha e^(beta theta), polar and intrinsic bases."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold, dot1

TH = 40.0            # drawn theta in the rotation view, degrees
BETA = 0.4           # drawn beta in the tangent triangle
BS = 0.2             # beta of the spiral plane figure
TP = 200.0           # drawn theta of P in the spiral plane, degrees


def _d(deg, r=1.0):
    return r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg))


@figure("p02-polar-rotation",
        "Top view of the polar basis rotated by theta about k0 out of the paper, with the right triangles of e_r and "
        "e_theta",
        r"View along $\mathbf k_0$ (out of the paper). The polar basis is the fixed basis turned counterclockwise by "
        r"$\theta$; the leftward leg of the triangle of $\mathbf e_\theta$ gives the minus sign of its $\mathbf i_0$ "
        r"component.")
def polar_rotation():
    sc = Scene(580, 500, (300, 300), 215)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.12)
    triangle(sc, [O, (-s, 0.0), (-s, c)], "BLUE", 0.12)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((c, 0.0), O)
    sc.dashed((-s, 0.0), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (-s, 0.0), 0, 90, 0.05)
    fixed_axis(sc, O, 0, 1.12, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.3, bold("j") + S("", "0"), off=(16, 2))
    fixed_axis(sc, O, 180, 1.0, "−" + bold("i") + S("", "0"), off=(-8, -12), dashed=True)
    unit(sc, O, TH, 1.0, bold("e") + S("", "r"), off=(14, -6))
    unit(sc, O, 90 + TH, 1.0, bold("e") + S("", "θ"), off=(-16, -8))
    sc.angle(O, 0.30, 0, TH, "θ", name_r=0.42)
    sc.angle(O, 0.30, 90, 90 + TH, "θ", name_r=0.42)
    sc.label((c / 2, 0.0), "cos θ", "TEXT", "middle", 15, dy=20)
    sc.label((c, s / 2), "sin θ", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((-s / 2, 0.0), "−sin θ", "TEXT", "middle", 15, dy=20)
    sc.note((-s / 2, 0.0), "toward −i₀", "TEXT", "middle", 12, dy=36)
    sc.label((-s, c / 2), "cos θ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((c / 2, s / 2), "1", "TEXT", "middle", 15, dx=-12, dy=-10)
    sc.label((-s / 2, c / 2), "1", "TEXT", "middle", 15, dx=14, dy=-4)
    # rotation of the basis about O (counterclockwise), below the axes
    sc.spin(O, 0.6, 235, 305, dot1("θ"), name_r=0.74)
    axis_out(sc, O, bold("k") + S("", "0") + " (out of the paper)", off=(115, 56))
    sc.label(O, "O", "HEAD", "end", 17, dx=-16, dy=24)
    return sc


@figure("p02-tangent-triangle",
        "Right triangle with legs beta along e_r and 1 along e_theta whose hypotenuse gives the unit tangent at the "
        "constant angle psi.",
        r"The velocity is $r\dot\theta$ times $(\beta\,\mathbf e_r + \mathbf e_\theta)$, so the unit tangent is the "
        r"hypotenuse direction of a triangle with legs $\beta$ and $1$. The angle $\psi$ between radius and tangent is "
        r"constant; $\mathbf e_n$ is $\mathbf e_t$ turned a right angle counterclockwise.")
def tangent_triangle():
    sc = Scene(580, 500, (270, 400), 250)
    P = (0.0, 0.0)
    psi = math.degrees(math.atan2(1.0, BETA))
    h = math.hypot(1.0, BETA)
    top = (BETA, 1.0)
    triangle(sc, [P, (BETA, 0.0), top], "BLUE", 0.12)
    sc.dashed(P, (-0.95, 0.0))
    sc.note((-0.95, 0.0), "toward O", "TEXT", "middle", 13, dy=22)
    sc.dashed((BETA, 0.0), top)
    sc.line(P, top, "EDGE", 1.0)
    right_angle(sc, (BETA, 0.0), 180, 90, 0.045)
    unit(sc, P, 0, 1.05, bold("e") + S("", "r"), off=(16, 5))
    unit(sc, P, 90, 1.05, bold("e") + S("", "θ"), off=(16, -2))
    unit(sc, P, psi, 1.0, bold("e") + S("", "t"), "ACC", off=(18, -8))
    unit(sc, P, psi + 90, 1.0, bold("e") + S("", "n"), "GREEN", off=(-14, -8))
    right_angle(sc, P, psi, psi + 90, 0.09)
    sc.angle(P, 0.30, 0, psi, "ψ", name_r=0.43)
    sc.angle(P, 0.42, 90, psi + 90, "ψ", name_r=0.55)
    sc.label((BETA / 2, 0.0), "β", "TEXT", "middle", 16, dy=22)
    sc.label((BETA, 0.7), "1", "TEXT", "start", 16, dx=8, dy=4)
    hx, hy = sc.P((BETA * 0.6, 0.6))
    nx, ny = -math.sin(math.radians(psi)), -math.cos(math.radians(psi))     # screen normal, to the left of the hypotenuse
    sc.c.add(f'<text x="{hx + 16 * nx:.1f}" y="{hy + 16 * ny:.1f}" fill="BLUE" font-size="14" text-anchor="middle" '
             f'font-style="italic" font-family="Newsreader, \'Times New Roman\', Times, serif" '
             f'transform="rotate({-psi:.1f} {hx + 16 * nx:.1f} {hy + 16 * ny:.1f})">√(1 + β²)</text>')
    sc.note((0.55, 0.28), "tan ψ = 1/β", "TEXT", "start", 14)
    sc.mass(P, "P", r=5, name_off=(-14, 20), col="HEAD")
    axis_out(sc, (0.85, 0.82), bold("k") + S("", "0") + " = " + bold("e") + S("", "b"), off=(20, 30))
    return sc


@figure("p02-spiral-plane",
        "Logarithmic spiral with the polar and intrinsic bases at P and the centre of curvature C forming a right "
        "triangle OPC with the right angle at O.",
        r"The tangent makes the constant angle $\psi$ with the radius. The centre of curvature lies at $\beta r$ along "
        r"$\mathbf e_\theta$ from the pole, so $OPC$ is a right triangle at $O$ with hypotenuse "
        r"$\rho = r\sqrt{1+\beta^2}$.")
def spiral_plane():
    sc = Scene(680, 640, (350, 260), 125)
    O = (0.0, 0.0)
    r = math.exp(BS * math.radians(TP))
    P = _d(TP, r)
    C = _d(TP + 90, BS * r)
    rho = r * math.sqrt(1 + BS * BS)
    psi = math.degrees(math.atan2(1.0, BS))

    def pt(deg):
        return _d(deg, math.exp(BS * math.radians(deg)))
    triangle(sc, [O, P, C], "BLUE", 0.14)
    sc.circle(C, rho, "EDGE", 1.0, "5 4")
    fixed_axis(sc, O, 0, 1.7, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.6, bold("j") + S("", "0"), off=(16, 2))
    sc.curve(lambda t: pt(math.degrees(t)), math.radians(-180), math.radians(292), 200, col="HEAD", w=2.6)
    sc.vec(pt(292), pt(304), None, "HEAD", 2.6, head=11)
    sc.label(pt(304), "r = α e" + '<tspan baseline-shift="super" font-size="70%">βθ</tspan>', "HEAD", "start", 15,
             dx=12, dy=14)
    sc.vec(pt(95), pt(108), None, "HEAD", 2.6, head=11)
    sc.vec(O, P, None, "HEAD", 2.4, head=11)
    sc.label(_d(TP, r * 0.5), bold("r") + S("", "0", "P") + " = r " + bold("e") + S("", "r"), "HEAD", "middle", 14,
             dx=-6, dy=-30)
    sc.label(_d(TP, r * 0.86), "r", "HEAD", "middle", 16, dx=4, dy=-14)
    L = 0.55
    unit(sc, P, TP, L, bold("e") + S("", "r"), "BLUE", off=(-14, -6))
    unit(sc, P, TP + 90, L, bold("e") + S("", "θ"), "BLUE", off=(20, 14))
    unit(sc, P, TP + psi, L, bold("e") + S("", "t"), "ACC", off=(-18, 16))
    unit(sc, P, TP + psi + 90, L, bold("e") + S("", "n"), "GREEN", off=(-2, 24))
    sc.line(P, C, "GREEN", 1.6, "6 4")
    sc.line(O, C, "HEAD", 1.4, "3 3")
    right_angle(sc, O, TP + 90, TP, 0.12)
    sc.angle(O, 0.55, 0, TP, "θ", name_r=0.7)
    sc.angle(P, 0.30, TP, TP + psi, "ψ", name_r=0.43)
    sc.dotp(O, 4.0)
    sc.dotp(C, 3.5)
    sc.dotp(P, 4.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=-8)
    sc.label(P, "P", "HEAD", "end", 17, dx=-14, dy=-4)
    sc.label(C, "C", "HEAD", "start", 17, dx=8, dy=22)
    mid = ((P[0] + C[0]) / 2, (P[1] + C[1]) / 2)
    sc.label(mid, "ρ = r √(1 + β²)", "GREEN", "middle", 15, dx=45, dy=24)
    sc.label((C[0] / 2, C[1] / 2), "β r", "HEAD", "start", 15, dx=10, dy=6)
    axis_out(sc, (1.2, 1.3), bold("k") + S("", "0") + " (out of the paper)", off=(0, 28))
    return sc
