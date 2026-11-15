"""Problem 04: aircraft at constant altitude seen in polar coordinates from a ground observer."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold


@figure("p04-main-plane",
        "Aircraft P flying at constant altitude y0 above the observer O, with the right triangle O H P that gives "
        "its polar coordinates.",
        r"Main plane of the motion. The right triangle $OHP$ has hypotenuse $r$, adjacent leg $x = r\cos\theta$ and "
        r"opposite leg $y_0 = r\sin\theta$; the polar basis $\mathbf e_r, \mathbf e_\theta$ is drawn at $P$.")
def main_plane():
    sc = Scene(640, 420, (90, 350), 85)
    O = (0.0, 0.0)
    P = (4.0, 3.0)
    H = (4.0, 0.0)
    th = math.degrees(math.atan2(3, 4))
    sc.line((-0.5, 0), (6.4, 0), "EDGE", 1.2)
    sc.note((6.3, 0), "ground", "TEXT", "end", 13, dy=18)
    sc.line((-0.5, 3.0), (6.4, 3.0), "EDGE", 1.1, "6 5")
    fixed_axis(sc, O, 0, 1.3, bold("i") + S("", "0"), off=(2, 22))
    fixed_axis(sc, O, 90, 1.3, bold("j") + S("", "0"), off=(14, 4))
    triangle(sc, [O, H, P], "BLUE", 0.10)
    right_angle(sc, H, 180, 90, 0.17)
    sc.dashed(H, P)
    sc.vec(O, P, None, "HEAD", 2.6, head=11)
    sc.label((2.0, 1.5), bold("r"), "HEAD", "middle", 18, dx=-12, dy=-12)
    sc.angle(O, 0.9, 0, th, "θ", "HEAD", name_r=1.18)
    sc.label((2.0, 0.0), "x = r cos θ", "TEXT", "middle", 15, dy=24)
    sc.label((4.0, 1.5), S("y", "0") + " = r sin θ", "TEXT", "start", 15, dx=10, dy=5)
    # faint earlier position
    sc.circle((0.0, 3.0), 0.07, "EDGE", 1.4, fill="EDGE", opacity=0.5)
    sc.label((0.0, 3.0), S("P", "0") + " (t = 0)", "TEXT", "start", 15, dx=14, dy=-12)
    sc.dashed((0.0, 0.0), (0.0, 3.0))
    # velocity and acceleration at P
    sc.vec(P, (5.7, 3.0), bold("v") + " " + bold("i") + S("", "0"), "GREEN", 2.6, name_off=(-2, -14), size=16, head=11)
    sc.vec((4.0, 2.78), (5.2, 2.78), bold("a") + S("", "x") + " " + bold("i") + S("", "0"), "ACC", 2.6,
           name_off=(2, 26), size=16, head=11)
    # polar basis at P
    ur = (0.6, 0.45)
    sc.vec(P, (4.0 + 1.0 * 0.8, 3.0 + 0.6 * 0.8 * 1.0), None, "BLUE", 2.6, head=11)
    sc.label((4.8, 3.48), bold("e") + S("", "r"), "BLUE", "start", 17, weight="700", dx=6, dy=-10)
    sc.vec(P, (4.0 - 0.6 * 0.8, 3.0 + 0.8 * 0.8), None, "BLUE", 2.6, head=11)
    sc.label((3.52, 3.64), bold("e") + S("", "θ"), "BLUE", "end", 17, weight="700", dx=-4, dy=-4)
    sc.mass(P, None, r=7)
    sc.label(P, "P", "HEAD", "middle", 17, dx=-8, dy=36)
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    sc.dotp(H, 3.5)
    sc.label(H, "H", "HEAD", "middle", 17, dx=-2, dy=24)
    axis_out(sc, (-0.35, -0.38), bold("k") + S("", "0"), off=(-4, 26))
    return sc


@figure("p04-rotation-view",
        "View along k0 of the fixed axes i0, j0 and the polar axes e_r, e_theta turned by theta.",
        r"Rotation of the polar basis by $\theta$ about $\mathbf k_0$ (out of the paper). The component of "
        r"$\mathbf e_\theta$ along $\mathbf i_0$ is negative because $\mathbf e_\theta$ leans toward $-\mathbf i_0$.")
def rotation_view():
    TH = 37.0
    sc = Scene(600, 480, (300, 330), 220)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    fixed_axis(sc, O, 0, 1.15, bold("i") + S("", "0"), off=(6, 22))
    fixed_axis(sc, O, 90, 1.15, bold("j") + S("", "0"), off=(14, 4))
    er = (c, s)
    et = (-s, c)
    triangle(sc, [O, (c, 0.0), er], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), et], "BLUE", 0.10)
    sc.dashed((c, 0.0), er)
    sc.dashed((0.0, s), er)
    sc.dashed((-s, 0.0), et)
    sc.dashed((0.0, c), et)
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    unit(sc, O, TH, 1.0, bold("e") + S("", "r"), off=(14, -8))
    unit(sc, O, TH + 90, 1.0, bold("e") + S("", "θ"), off=(-14, -8))
    sc.arc(O, 0.38, 0, TH, "HEAD", 1.6, head=True)
    sc.label((0.52, 0.12), "θ", "HEAD", "middle", 16, dy=5)
    sc.arc(O, 0.38, 90, 90 + TH, "HEAD", 1.6, head=True)
    sc.label((-0.26, 0.58), "θ", "HEAD", "middle", 16, dy=5)
    sc.label((c / 2, 0.0), "cos θ", "TEXT", "middle", 15, dy=22)
    sc.label((c, s / 2), "sin θ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, 0.0), "−sin θ", "TEXT", "middle", 15, dy=22)
    sc.label((-s * 0.35, c), "cos θ", "TEXT", "middle", 15, dy=-10)
    sc.spin(O, 0.2, 200, 340, "", "GREEN")
    axis_out(sc, O, None)
    sc.label(O, bold("k") + S("", "0") + " (⊙)", "HEAD", "middle", 15, dx=2, dy=64)
    return sc


@figure("p04-acceleration-projection",
        "The horizontal acceleration a_x i0 split into a radial component and a negative azimuthal component.",
        r"The acceleration of the aircraft is the hypotenuse; its radial component is the adjacent leg "
        r"$a_x\cos\theta$ and its azimuthal component is the opposite leg, along $-\mathbf e_\theta$.")
def acceleration_projection():
    TH = 37.0
    sc = Scene(640, 440, (200, 250), 60)
    t = math.radians(TH)
    c, s = math.cos(t), math.sin(t)
    P = (0.0, 0.0)
    ax = 4.0
    er = (c, s)
    et = (-s, c)
    for d, L1, L2 in ((er, -2.0, 4.9), (et, -2.2, 2.6)):
        sc.line((P[0] + d[0] * L1, P[1] + d[1] * L1), (P[0] + d[0] * L2, P[1] + d[1] * L2), "BLUE", 1.3)
    sc.label((er[0] * 4.9, er[1] * 4.9), bold("e") + S("", "r"), "BLUE", "start", 17, weight="700", dx=8, dy=-4)
    sc.label((et[0] * 2.6, et[1] * 2.6), bold("e") + S("", "θ"), "BLUE", "end", 17, weight="700", dx=-6, dy=-6)
    tip_r = (ax * c * c, ax * c * s)
    tip_a = (ax, 0.0)
    tip_t = (ax * s * s, -ax * s * c)       # tip of a_theta along -e_theta
    triangle(sc, [P, tip_r, tip_a], "ACC", 0.14)
    right_angle(sc, tip_r, TH + 180, TH + 270, 0.22)
    sc.dashed(tip_r, tip_a)
    sc.dashed(tip_a, tip_t)
    sc.vec(P, tip_a, bold("a") + S("", "x") + " " + bold("i") + S("", "0"), "ACC", 2.8, name_off=(8, 24), size=17, head=12)
    sc.vec(P, tip_r, None, "ACC", 2.0, head=10)
    sc.vec(P, tip_t, None, "ACC", 2.0, head=10)
    K = (5.3, 2.0)
    fixed_axis(sc, K, 0, 0.9, bold("i") + S("", "0"), off=(4, 20))
    fixed_axis(sc, K, 90, 0.9, bold("j") + S("", "0"), off=(14, 4))
    sc.arc(P, 1.3, 0, TH, "HEAD", 1.6)
    sc.label((1.65 * math.cos(t / 2), 1.65 * math.sin(t / 2)), "θ", "HEAD", "middle", 16, dy=5)
    sc.label((0.5, 2.7), S("a", "r") + " = " + S("a", "x") + " x / r", "ACC", "start", 15)
    sc.label((0.5, 2.7), "= " + S("a", "x") + " cos θ", "ACC", "start", 15, dy=20)
    sc.label((tip_t[0] * 0.5, tip_t[1] * 0.5), S("a", "θ") + " = −" + S("a", "x") + " " + S("y", "0") + " / r",
             "ACC", "start", 15, dx=16, dy=-2)
    sc.label((tip_t[0] * 0.5, tip_t[1] * 0.5), "= −" + S("a", "x") + " sin θ", "ACC", "start", 15, dx=16, dy=18)
    sc.mass(P, None, r=7)
    sc.label(P, "P", "HEAD", "middle", 17, dx=-14, dy=24)
    axis_out(sc, K, bold("k") + S("", "0"), r_px=7, off=(-16, 20))
    return sc
