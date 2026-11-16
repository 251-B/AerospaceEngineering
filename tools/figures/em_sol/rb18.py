"""Problem RB-18: bowling ball on a lane (Euler angles psi, theta, phi; slip at the contact point)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d, rotation_view, sub
from figures.em_sol.rb12 import ground_line, plane_rotation
from figures.mech import S, Scene, bold

ORANGE = "ACC"
A = 1.2
K = bold("k")
I1, J1, K2 = S(bold("i"), "1"), S(bold("j"), "1"), S(bold("k"), "2")
I2 = S(bold("i"), "2")
IB, JB = S(bold("i"), "b"), S(bold("j"), "b")


def _g(sc):
    sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=14, dy=26)


@figure("rb18-rot-psi",
        "First Euler rotation of the ball, by psi about the vertical axis k.",
        r"First rotation, by $\psi$ about $\mathbf k$ (⊙). $\mathbf j_1$ stays horizontal and is the axis of the second rotation.")
def rot_psi():
    return plane_rotation(760, 600, (270, 490), 250, 30.0, (bold("i"), bold("j"), I1, J1), K + " (⊙)", ("ψ", ""), None,
                          extra_post=_g, out_off=(-16, 28))


@figure("rb18-rot-theta",
        "Second Euler rotation, by theta about the horizontal axis j_1, which carries k_2 towards the hole A.",
        r"Second rotation, by $\theta$ about $\mathbf j_1$ (⊗; positive rotations look clockwise from this side). "
        r"$\mathbf k_2$ points from $G$ to the hole $A$.")
def rot_theta():
    ang = -35.0
    a = 1.32

    def pre(sc):
        sc.arc((0.0, 0.0), a, 0, 180, "EDGE", 1.2, "6 4")

    def post(sc):
        ua = d(90 + ang)
        pa = (a * ua[0], a * ua[1])
        sc.dashed((ua[0], ua[1]), pa)
        sc.mass(pa, None, r=4.5, col="ACC")
        sc.label(pa, "A (hole)", "HEAD", "start", 16, dx=10, dy=-6)
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=-14, dy=-26)
    return rotation_view(800, 640, (330, 450), 250, ang, I1, K, I2, K2, J1 + " (⊗)", ("θ", ""),
                         pre=pre, post=post, out_kind="in", out_off=(-6, 30))


@figure("rb18-rot-phi",
        "Third Euler rotation, the spin phi about the axis GA.",
        r"Third rotation, by $\varphi$ about $\mathbf k_2$ (⊙): the spin of the ball about the line $GA$.")
def rot_phi():
    ang = 40.0

    def pre(sc):
        sc.arc((0.0, 0.0), 1.5, 0, 180, "EDGE", 1.2, "6 4")

    def post(sc):
        for da in (-9.0, 9.0):
            c = add((0.0, 0.0), d(ang + da), 1.22)
            sc.circle(c, 0.07, "HEAD", 1.6, fill="ACC", opacity=0.5)
        sc.note(add((0.0, 0.0), d(ang), 1.28), "finger holes", "TEXT", "start", 13, dx=30, dy=-26)
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=-14, dy=-26)
    return plane_rotation(860, 600, (400, 480), 250, ang, (I2, J1, IB, JB), K2 + " (⊙)", ("φ", ""), None,
                          extra_pre=pre, extra_post=post, out_off=(-16, 28), col="ACC")


# ------------------------------------------------------------------------------------------------ side view of the lane
def _lane(sc, x0, x1, faint=False):
    if faint:
        sc.line((x0, 0.0), (x1, 0.0), "EDGE", 1.6)
        for i in range(int((x1 - x0) / 0.14)):
            x = x0 + 0.14 * i + 0.08
            sc.line((x, 0.0), (x - 0.09, -0.11), "EDGE", 0.9)
    else:
        sc.ground((x0, 0.0), (x1, 0.0), -1)


@figure("rb18-slip",
        "Side view of the ball with the velocity of the centre, the angular velocity and the slip velocity of the "
        "contact point.",
        r"Contact kinematics. The body point at $P$ moves with $\mathbf v_0^G$ plus the rotational part "
        r"$-a\,\omega_y\,\mathbf i$; at the release of part (g) the slip velocity is $\tfrac34\xi_0\,\mathbf i$.")
def slip():
    sc = Scene(800, 330, (110, 262), 76)
    G = (2.4, A)
    P = (2.4, 0.0)
    _lane(sc, -0.9, 7.0)
    sc.line((0.0, -0.2), (0.0, 0.5), "HEAD", 3.0)
    sc.label((0.0, 0.5), "O (foul line)", "HEAD", "middle", 16, dx=0, dy=-10)
    sc.circle(G, A, "HEAD", 2.2, fill="EDGE", opacity=0.10)
    # arm GP
    sc.dashed(G, P)
    sc.label((2.4, A / 2), "a  (−a " + bold("k") + ")", "TEXT", "end", 14, dx=-8, dy=5)
    axis_in(sc, G, None, "HEAD")
    sc.label(G, bold("j"), "HEAD", "start", 15, weight="700", dx=14, dy=24)
    # velocity of G and spin
    sc.vec(G, (G[0] + 3.0, G[1]), "ξ", "BLUE", 3.0, name_off=(14, 6), size=18, head=12)
    sc.spin(G, 0.62, 150, 40, "", "GREEN")
    sc.label(add(G, d(95), 0.62), S("ω", "y"), "GREEN", "middle", 17, weight="700", dy=-14)
    # contact point: the two parts of its velocity and their sum (rows separated for legibility)
    sc.vec((P[0], 0.28), (P[0] + 3.0, 0.28), None, "BLUE", 2.6, head=11)
    sc.label((P[0] + 3.0, 0.28), "ξ " + bold("i"), "BLUE", "start", 16, weight="700", dx=8, dy=5)
    sc.line((P[0], 0.28), (P[0] - 0.75, 0.28), "BLUE", 2.6, "6 4")
    sc.vec((P[0] - 0.55, 0.28), (P[0] - 0.75, 0.28), None, "BLUE", 2.6, head=11)
    sc.label((P[0] - 0.75, 0.28), "−a " + S("ω", "y") + " " + bold("i"), "BLUE", "end", 16, weight="700", dx=-26, dy=5)
    sc.vec((P[0], 0.62), (P[0] + 2.25, 0.62), None, ORANGE, 3.2, head=12)
    sc.label((P[0] + 2.25, 0.62), S("v", "slip") + " = (ξ − a " + S("ω", "y") + ") " + bold("i"), ORANGE, "start", 16,
             weight="700", dx=8, dy=5)
    sc.mass(P, None, r=4.5, col="BLUE")
    sc.label(P, "P", "HEAD", "middle", 17, dx=-14, dy=22)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-16, dy=22)
    sc.note((P[0], -0.62), "slip velocity = 0 when rolling without slip", "TEXT", "middle", 14)
    return sc


@figure("rb18-fbd",
        "Free-body diagram of the bowling ball: weight, normal reaction and friction opposite to the slip.",
        r"Free-body diagram. The friction at $P$ opposes the slip; its moment $a F_y\,\mathbf i - a F_x\,\mathbf j$ about $G$ "
        r"is the only moment, so $\omega_z$ is constant.")
def fbd():
    sc = Scene(880, 380, (120, 300), 95)
    G = (2.4, A)
    P = (2.4, 0.0)
    _lane(sc, -0.9, 6.2, faint=True)
    sc.circle(G, A, "HEAD", 2.2, fill="EDGE", opacity=0.10)
    # arm GP as an offset dimension (weight and N lie on the line GP)
    sc.dim((G[0] - 0.7, G[1]), (P[0] - 0.7, 0.0), "−a " + bold("k"), off=(30, 4))
    sc.dashed(G, (G[0] - 0.85, G[1]))
    sc.dashed(P, (P[0] - 0.85, 0.0))
    sc.vec(G, (G[0], G[1] - 0.55), "Mg", "PINK", 3.2, name_off=(26, -6), size=17, head=12)
    sc.vec(P, (P[0], 0.55), "N", "GREEN", 3.2, name_off=(20, 26), size=17, head=12)
    sc.vec(P, (P[0] - 1.25, 0.0), None, "GREEN", 3.2, head=12)
    sc.label((P[0] - 1.25, 0.0), "μ N (with slip)", "GREEN", "end", 16, weight="700", dx=-6, dy=-12)
    sc.spin(G, 0.55, 150, 40, "", "GREEN")
    sc.label(add(G, d(95), 0.55), "−a " + S("F", "x") + " " + bold("j"), "GREEN", "middle", 16, weight="700", dy=-14)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-18, dy=-10)
    sc.mass(P, None, r=4.5, col="BLUE")
    sc.label(P, "P", "HEAD", "middle", 17, dx=14, dy=22)
    axis_in(sc, (4.0, 2.2), None, "HEAD")
    sc.label((4.0, 2.2), bold("j") + " (into the paper)", "HEAD", "start", 16, weight="700", dx=16, dy=5)
    # top-view inset: the lane of width W and length l, x up and y to the left
    ox, oy, W, Ln = 6.55, 0.15, 0.42, 2.52
    sc.poly([(ox - W / 2, oy), (ox + W / 2, oy), (ox + W / 2, oy + Ln), (ox - W / 2, oy + Ln)], "HEAD", 1.8, close=True,
            fill="EDGE", opacity=0.10)
    sc.mass((ox, oy + 0.18), None, r=5, col="ACC")
    for dx in (-0.12, 0.0, 0.12):
        sc.mass((ox + dx, oy + Ln - 0.1), None, r=3, col="HEAD")
    ao = (ox + W / 2 + 0.7, oy + 0.3)
    sc.vec(ao, (ao[0], ao[1] + 0.7), "x", "BLUE", 2.2, name_off=(10, 6), size=16, head=9)
    sc.vec(ao, (ao[0] - 0.45, ao[1]), "y", "BLUE", 2.2, name_off=(-4, 20), size=16, head=9)
    sc.dim((ox - W / 2 - 0.2, oy), (ox - W / 2 - 0.2, oy + Ln), "l = 6", off=(-22, 4))
    sc.dashed((ox - W / 2, oy), (ox - W / 2 - 0.3, oy))
    sc.dashed((ox - W / 2, oy + Ln), (ox - W / 2 - 0.3, oy + Ln))
    sc.dim((ox - W / 2, oy - 0.2), (ox + W / 2, oy - 0.2), "W = 1", off=(0, 20))
    sc.label((ox, oy + Ln), "pins", "TEXT", "middle", 14, dy=-10)
    sc.note((ox, oy - 0.62), "top view", "TEXT", "middle", 13)
    return sc


@figure("rb18-velocities",
        "Speed of the centre and rim speed of the ball against time: they meet at t*, after the ball has already "
        "reached the pins.",
        r"During the slip the speed of $G$ falls and $a\,\omega_y$ grows; they would meet at $t^{*} = 3\xi_0/(14\mu g)$, but "
        r"the ball reaches the pins earlier, at $t_l$, still slipping.")
def velocities():
    sx, sy = 10.0, 2.6
    sc = Scene(900, 800, (130, 710), 230)

    def Q(t, v):
        return (t * sx, v * sy)
    ts, vs = 3.0 / 14.0, 11.0 / 14.0
    tl = 1.0 - 2.0 / math.sqrt(5.0)
    # grid, axes and ticks
    for v in (0.25, 0.5, 0.75, 1.0):
        sc.line(Q(0, v), Q(0.3, v), "EDGE", 0.6, "2 4")
    sc.vec(Q(0, 0), Q(0.32, 0), None, "EDGE", 1.6, head=9)
    sc.vec(Q(0, 0), Q(0, 1.1), None, "EDGE", 1.6, head=9)
    for t in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3):
        sc.line(Q(t, 0), Q(t, -0.02), "EDGE", 1.2)
        sc.label(Q(t, 0), f"{t:.2f}", "TEXT", "middle", 14, italic=False, dy=22)
    for v in (0.25, 0.5, 0.75, 1.0):
        sc.label(Q(0, v), f"{v:.2f}", "TEXT", "end", 14, italic=False, dx=-8, dy=5)
    sc.label(Q(0.32, 0), "t  (units ξ₀/(μ g))", "TEXT", "end", 15, dy=-10)
    sc.label(Q(0, 1.1), "speed (units ξ₀)", "TEXT", "start", 15, dx=10, dy=4)
    # gap between the two speeds
    sc.poly([Q(0, 1.0), Q(ts, vs), Q(0, 0.25)], "ACC", 0.0, fill="ACC", close=True, opacity=0.18)
    sc.label(Q(0.012, 0.66), "slip velocity", "ACC", "start", 16, weight="700")
    # the two speeds
    sc.line(Q(0, 1.0), Q(ts, vs), "BLUE", 3.0)
    sc.line(Q(0, 0.25), Q(ts, vs), ORANGE, 3.0)
    sc.line(Q(ts, vs), Q(0.3, vs), "EDGE", 2.4, "7 5")
    sc.label(Q(0.3, vs), "rolling without slip", "TEXT", "end", 15, italic=False, dy=-10)
    sc.label(Q(0.158, 0.842), "ξ, speed of G", "BLUE", "start", 16, weight="700", dx=6, dy=-14)
    sc.label(Q(0.03, 0.325), "a " + S("ω", "y"), ORANGE, "start", 16, weight="700", dx=12, dy=24)
    # meeting point
    sc.dashed(Q(ts, 0), Q(ts, vs))
    sc.dashed(Q(0, vs), Q(ts, vs))
    sc.mass(Q(ts, vs), None, r=5, col="HEAD")
    sc.label(Q(ts, 0), "t* = 3/14", "HEAD", "middle", 16, dy=46)
    sc.label(Q(0, vs), "11/14", "HEAD", "end", 16, dx=-48, dy=5)
    # the pins
    sc.dashed(Q(tl, 0), Q(tl, 1.06))
    sc.label(Q(tl, 1.06), "pins (l = ξ₀²/(10 μ g))", "HEAD", "start", 16, dx=8, dy=-4)
    sc.label(Q(tl, 0), S("t", "l"), "HEAD", "middle", 16, dy=46)
    for v, nm, dy in ((1.0 - tl, "0.894", -10), (0.25 + 2.5 * tl, "0.514", 20)):
        sc.mass(Q(tl, v), None, r=4.5, col="HEAD")
        sc.label(Q(tl, v), nm, "HEAD", "start", 15, italic=False, dx=10, dy=dy)
    return sc
