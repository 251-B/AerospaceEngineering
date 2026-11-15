"""Problem 05: airplane A towing a glider B on a cable of length r."""
import math

from figures.em_solutions import (axis_out, figure, fixed_axis, right_angle, triangle, unit)
from figures.mech import S, Scene, bold, dot1, dot2

TH = 30.0            # drawn value of theta, degrees
R = 5.0              # drawn cable length
VT = 7.0             # drawn flight distance v_A t


@figure("p05-cable-plane",
        "Airplane A towing glider B on a cable of length r inclined at theta above the horizontal, behind A.",
        r"Main plane. The position of the glider is the position of the airplane plus the cable vector "
        r"$r\,\mathbf i_1$; the right triangle $AHB$ has hypotenuse $r$, horizontal leg $r\cos\theta$ toward "
        r"$-\mathbf i_0$ and vertical leg $r\sin\theta$.")
def cable_plane():
    sc = Scene(640, 300, (60, 215), 68)
    t = math.radians(TH)
    O = (0.0, 0.0)
    A = (VT, 0.0)
    B = (VT - R * math.cos(t), R * math.sin(t))
    H = (B[0], 0.0)
    sc.line((-0.4, 0.0), (7.9, 0.0), "EDGE", 1.1, "6 4")
    triangle(sc, [A, H, B], "BLUE", 0.12)
    right_angle(sc, H, 0, 90, 0.2)
    sc.dashed(H, B)
    fixed_axis(sc, O, 0, 1.1, bold("i") + S("", "0"), off=(2, -10))
    fixed_axis(sc, O, 90, 1.3, bold("j") + S("", "0"), off=(16, 4))
    axis_out(sc, O, bold("k") + S("", "0"), off=(-22, -14))
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=24)
    # position vectors (black)
    sc.vec(O, A, None, "HEAD", 2.0, head=10)
    sc.vec(O, B, None, "HEAD", 2.0, head=10)
    sc.label((1.3, 0.0), "v" + S("", "A") + " t", "HEAD", "middle", 16, dy=22)
    sc.label((B[0] / 2, B[1] / 2), bold("r") + '<tspan baseline-shift="super" font-size="70%">B</tspan>'
             '<tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>', "HEAD", "end", 16, dx=-8, dy=-8)
    # cable
    sc.line(A, B, "HEAD", 1.8)
    sc.label(((A[0] + B[0]) / 2, (A[1] + B[1]) / 2), "r", "HEAD", "start", 17, dx=10, dy=-8)
    sc.label(((A[0] + H[0]) / 2, 0.0), "r cos θ", "TEXT", "middle", 15, dy=22)
    sc.label((H[0], B[1] / 2), "r sin θ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.angle(A, 1.5, 150, 180, "θ", "TEXT", name_r=1.95)
    # points
    sc.mass(A, "A", r=7, name_off=(0, -16))
    sc.mass(B, "B", r=6, name_off=(-4, -14))
    sc.dotp(H, 3.0)
    sc.label(H, "H", "HEAD", "middle", 16, dy=22)
    # cable basis at A (blue) and flight velocity (green)
    unit(sc, A, 180 - TH, 1.0, bold("i") + S("", "1"), off=(-6, 20))
    unit(sc, A, 180 - TH + 90, 1.0, bold("j") + S("", "1"), off=(-14, 14))
    sc.vec(A, (A[0] + 1.0, 0.0), "v" + S("", "A") + " " + bold("i") + S("", "0"), "GREEN", 2.6, name_off=(0, -14),
           size=16, head=11)
    return sc


@figure("p05-rotation-view",
        "View along k0 of the fixed axes and the cable axes i1, j1, with the angle theta measured from minus i0 and "
        "the polar angle pi minus theta.",
        r"The cable basis is the fixed basis turned by the polar angle $\pi-\theta$ about $\mathbf k_0$ (out of the "
        r"paper); a growing $\theta$ turns it clockwise. Both components of $\mathbf j_1$ are negative because "
        r"$\mathbf j_1$ is $\mathbf i_1$ turned a right angle counterclockwise.")
def rotation_view():
    sc = Scene(560, 480, (280, 275), 170)
    O = (0.0, 0.0)
    t = math.radians(TH)
    c, s = math.cos(t), math.sin(t)
    tip = (-c, s)
    fixed_axis(sc, O, 0, 1.05, bold("i") + S("", "0"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.2, bold("j") + S("", "0"), off=(16, 4))
    fixed_axis(sc, O, 180, 1.05, "−" + bold("i") + S("", "0"), off=(-8, 20), dashed=True)
    triangle(sc, [O, (-c, 0.0), tip], "BLUE", 0.12)
    sc.dashed((-c, 0.0), tip)
    right_angle(sc, (-c, 0.0), 0, 90, 0.06)
    unit(sc, O, 180 - TH, 1.0, bold("i") + S("", "1"), off=(-14, -10))
    unit(sc, O, 180 - TH + 90, 1.0, bold("j") + S("", "1"), off=(-16, 6))
    axis_out(sc, O, bold("k") + S("", "0") + " (⊙)", off=(36, 24))
    # arcs
    sc.arc(O, 0.30, 180, 180 - TH, "GREEN", 1.6, head=True)
    mid = math.radians(180 - TH / 2)
    sc.label((0.43 * math.cos(mid), 0.43 * math.sin(mid)), "θ", "GREEN", "middle", 16, dy=5)
    sc.arc(O, 0.50, 0, 180 - TH, "GREEN", 1.6, head=True)
    a = math.radians(75)
    sc.label((0.50 * math.cos(a), 0.50 * math.sin(a)), "φ = π − θ", "GREEN", "start", 16, dx=6, dy=2)
    sc.arc(O, 0.72, 90, 180 - TH + 90, "GREEN", 1.6, head=True)
    a = math.radians(200)
    sc.label((0.72 * math.cos(a), 0.72 * math.sin(a)), "φ = π − θ", "GREEN", "end", 16, dx=-8, dy=4)
    # components
    sc.label((-c / 2, 0.0), "−cos θ", "TEXT", "middle", 15, dy=-6 + 28)
    sc.label((-c, s / 2), "sin θ", "TEXT", "end", 15, dx=-10, dy=5)
    jt = (-s, -c)
    sc.label(jt, "(−sin θ, −cos θ)", "TEXT", "middle", 15, dx=-16, dy=34)
    sc.spin(O, 1.25, 70, 15, "ω = −" + dot1("θ") + " " + bold("k") + S("", "0"), name_r=1.62)
    return sc


@figure("p05-velocity-acceleration",
        "Velocity of the glider as the sum of the airplane velocity and the velocity perpendicular to the cable, and "
        "the centripetal acceleration along the cable toward the airplane.",
        r"The velocity of $B$ adds the flight velocity of $A$ and a velocity of magnitude $r$ times the angular rate, "
        r"perpendicular to the cable. At constant rate the acceleration points along the cable toward $A$.")
def velocity_acceleration():
    sc = Scene(640, 380, (235, 230), 60)
    B = (0.0, 0.0)
    d = math.radians(-TH)
    A = (4.3 * math.cos(d), 4.3 * math.sin(d))
    sc.line(B, A, "BLUE", 1.4, "7 4")
    sc.label(A, "A", "HEAD", "start", 17, dx=12, dy=6)
    sc.dotp(A, 4.0)
    v1 = (4.0, 0.0)
    v2 = (3.0 * math.cos(math.radians(60)), 3.0 * math.sin(math.radians(60)))
    vs = (v1[0] + v2[0], v1[1] + v2[1])
    sc.dashed(v1, vs)
    sc.dashed(v2, vs)
    sc.vec(B, v1, "v" + S("", "A") + " " + bold("i") + S("", "0"), "GREEN", 2.4, name_off=(0, 22), size=16)
    sc.vec(B, v2, None, "GREEN", 2.4)
    sc.label(v2, "−r " + dot1("θ") + " " + bold("j") + S("", "1"), "GREEN", "end", 16, weight="700", dx=-6, dy=-10)
    sc.vec(B, vs, "v" + S("", "0", "B"), "GREEN", 3.6, name_off=(18, -6), size=17, head=12)
    # tangential term (dashed, offset sideways so it does not hide the velocity arrow)
    off = (0.45 * math.cos(math.radians(150)), 0.45 * math.sin(math.radians(150)))
    t_tip = (off[0] + 1.1 * math.cos(math.radians(60)), off[1] + 1.1 * math.sin(math.radians(60)))
    sc.line(off, t_tip, "ACC", 1.8, "5 4")
    from figures.svgkit import arrow_head
    px0, px1 = sc.P(off), sc.P(t_tip)
    arrow_head(sc.c, px0, px1, "ACC", 9)
    sc.label(t_tip, "−r " + dot2("θ") + " " + bold("j") + S("", "1"), "ACC", "end", 15, weight="700", dx=-8, dy=-14)
    sc.label(t_tip, "(zero at constant rate)", "ACC", "end", 13, italic=False, dx=-8, dy=2)
    # centripetal acceleration along -i1
    a_tip = (2.5 * math.cos(d), 2.5 * math.sin(d))
    sc.vec(B, a_tip, None, "ACC", 3.0, head=11)
    mid = (a_tip[0] / 2, a_tip[1] / 2)
    sc.label(mid, "a" + S("", "0", "B") + " = −r " + dot1("θ") + "² " + bold("i") + S("", "1"), "ACC", "end", 16,
             weight="700", dx=-14, dy=22)
    sc.mass(B, None, r=6)
    sc.label(B, "B", "HEAD", "end", 17, dx=-12, dy=22)
    return sc
