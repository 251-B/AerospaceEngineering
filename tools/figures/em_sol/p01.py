"""Problem 01: rocket on a helical trajectory (cylindrical basis and intrinsic basis)."""
import math

from figures.em_solutions import (axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit)
from figures.mech import S, Scene, bold

PURPLE = "#8b5cf6"          # binormal e_b (no kit token: a fixed colour, readable on every palette)

WT = 35.0                   # drawn value of omega t in the top view, deg
TH3 = 55.0                  # drawn value of omega t in the axonometric view, deg
GAMMA = 25.0                # helix angle, deg


def _e(sub):
    return bold("e") + S("", sub)


@figure("p01-top-view",
        "Top view of the helix projection with the cylindrical basis rotated by theta from the fixed basis about k0, "
        "which points out of the paper",
        r"View along $\mathbf k_0$ (out of the paper, $\odot$). The cylindrical basis is the fixed basis turned "
        r"counter-clockwise by $\theta = \omega t$; the triangles give the components of $\mathbf e_R$ and "
        r"$\mathbf e_\theta$, and the leftward leg of $\mathbf e_\theta$ explains its minus sign")
def top_view():
    sc = Scene(640, 560, (300, 400), 270)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(WT)), math.sin(math.radians(WT))
    Q = (c, s)
    sc.circle(O, 1.0, "EDGE", 1.4, dash="6 4")
    sc.note((0.62, -0.84), "projection of the helix", "TEXT", "start", 13)
    sc.note((0.62, -0.93), "(base circle, radius a)", "TEXT", "start", 13)
    fixed_axis(sc, O, 0, 1.3, bold("i") + S("", "0"), off=(14, 5))
    fixed_axis(sc, O, 90, 1.3, bold("j") + S("", "0"), off=(14, 2))
    # triangle of e_R
    triangle(sc, [O, (c, 0.0), Q], "BLUE", 0.10)
    sc.dashed((c, 0.0), Q)
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    sc.line(O, Q, "HEAD", 1.6)
    # triangle of e_theta
    T = (-s, c)
    triangle(sc, [O, (-s, 0.0), T], "ACC", 0.10)
    sc.dashed((-s, 0.0), T)
    right_angle(sc, (-s, 0.0), 0, 90, 0.05)
    unit(sc, O, WT, 0.62, _e("R"), off=(-6, 20))
    unit(sc, O, WT + 90, 1.0, _e("θ"), off=(-24, -4))
    sc.arc(O, 0.30, 0, WT, "GREEN", 1.6, head=True)
    sc.label((0.43 * math.cos(math.radians(WT / 2)), 0.43 * math.sin(math.radians(WT / 2))), "θ", "GREEN", "middle", 16,
             dx=8, dy=7)
    sc.arc(O, 0.30, 90, 90 + WT, "GREEN", 1.6, head=True)
    sc.label((0.43 * math.cos(math.radians(90 + WT / 2)), 0.43 * math.sin(math.radians(90 + WT / 2))), "θ", "GREEN",
             "middle", 16, dx=-14, dy=0)
    sc.note((0.53, 0.15), "θ = ωt", "GREEN", "start", 14)
    sc.note((-0.56, 0.52), "θ = ωt", "GREEN", "end", 14)
    # rotation sense
    sc.spin(O, 0.13, 215, 330, "ω", name_r=0.23)
    # point Q
    sc.dotp(Q, 4.5)
    sc.label(Q, "Q", "HEAD", "start", 17, dx=10, dy=-6)
    sc.label((Q[0] / 2, Q[1] / 2 + 0.15), "a", "HEAD", "end", 17, dx=-2, dy=-2)
    sc.label(Q, "a " + _e("R"), "HEAD", "start", 16, dx=30, dy=-26)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    # leg labels
    sc.label((c / 2, 0.0), "a cos(ωt)", "TEXT", "middle", 15, dy=22)
    sc.label((c, s / 2), "a sin(ωt)", "TEXT", "start", 15, dx=9, dy=5)
    sc.label((-s / 2, 0.0), "sin θ", "TEXT", "middle", 15, dy=22)
    sc.note((-s / 2, 0.0), "points to −i₀", "TEXT", "middle", 12, dy=38)
    sc.label((-s, c / 2), "cos θ", "TEXT", "end", 15, dx=-8, dy=5)
    axis_out(sc, (-1.05, -0.62), bold("k") + S("", "0") + " = " + _e("z") + " (out of the paper)", off=(60, 30))
    return sc


# ---------------------------------------------------------------------------------------------- axonometric view
def _proj(x, y, z):
    """Isometric projection: k0 up, i0 towards the viewer on the left, j0 to the right."""
    return ((y - x) * 0.866, -0.5 * (x + y) + z)


@figure("p01-helix-3d",
        "Helix wound on a cylinder of radius a with the position vector of P built as a e_R plus v_z t k0",
        r"The position vector is built in two steps: from $O$ to the foot $Q$ on the horizontal plane "
        r"($a\,\mathbf e_R$) and then up to $P$ ($v_z t\,\mathbf k_0$)")
def helix_3d():
    sc = Scene(620, 700, (300, 520), 118)
    K = 0.25
    th = math.radians(TH3)
    zP = K * th

    def hel(u):
        return _proj(math.cos(u), math.sin(u), K * u)

    # cylinder
    top = 3.2
    sc.curve(lambda u: _proj(math.cos(u), math.sin(u), 0.0), 0, 2 * math.pi, col="EDGE", w=1.3, dash="5 4")
    sc.curve(lambda u: _proj(math.cos(u), math.sin(u), top), 0, 2 * math.pi, col="EDGE", w=1.3)
    g = math.radians(135)
    for a in (g, g + math.pi):
        sc.line(_proj(math.cos(a), math.sin(a), 0), _proj(math.cos(a), math.sin(a), top), "EDGE", 1.3)
    # axes
    O = _proj(0, 0, 0)
    sc.vec(O, _proj(1.7, 0, 0), None, "EDGE", 1.4, head=8)
    sc.vec(O, _proj(0, 1.7, 0), None, "EDGE", 1.4, head=8)
    sc.vec(O, _proj(0, 0, 3.6), None, "EDGE", 1.4, head=8)
    sc.label(_proj(1.7, 0, 0), bold("i") + S("", "0"), "TEXT", "middle", 16, weight="700", dx=-14, dy=14)
    sc.label(_proj(0, 1.7, 0), bold("j") + S("", "0"), "TEXT", "middle", 16, weight="700", dx=14, dy=14)
    sc.label(_proj(0, 0, 3.6), bold("k") + S("", "0"), "TEXT", "middle", 16, weight="700", dx=14, dy=4)
    # helix: far part faint, near part solid
    n = 400
    u_end = 4 * math.pi
    segs = []
    for i in range(n):
        u0, u1 = u_end * i / n, u_end * (i + 1) / n
        um = (u0 + u1) / 2
        front = math.cos(um) + math.sin(um) >= 0
        sc.line(hel(u0), hel(u1), "HEAD", 2.6 if front else 1.2, None if front else "3 3")
    # sense of motion
    um = math.radians(460)
    d = (hel(um + 0.05)[0] - hel(um)[0], hel(um + 0.05)[1] - hel(um)[1])
    dn = math.hypot(*d)
    p0 = hel(um)
    sc.vec((p0[0] - 0.02 * d[0] / dn * 8, p0[1] - 0.02 * d[1] / dn * 8),
           (p0[0] + 0.02 * d[0] / dn * 8, p0[1] + 0.02 * d[1] / dn * 8), None, "PINK", 2.2, head=10)
    sc.label(p0, "motion", "PINK", "start", 14, dx=14, dy=4)
    # start point
    A = _proj(1, 0, 0)
    x, y = sc.P(A)
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="none" stroke="HEAD" stroke-width="1.8"/>')
    sc.label(A, "(a, 0, 0), t = 0", "TEXT", "start", 14, dx=14, dy=22)
    # P, Q
    Q = _proj(math.cos(th), math.sin(th), 0.0)
    P = _proj(math.cos(th), math.sin(th), zP)
    sc.dashed(Q, P)
    sc.line(O, Q, "HEAD", 1.0, "2 3")
    sc.vec(O, Q, None, "HEAD", 2.2, head=10)
    sc.vec(Q, P, None, "HEAD", 2.2, head=10)
    sc.vec(O, P, None, "HEAD", 2.2, head=10)
    sc.dotp(Q, 4.0)
    sc.label(Q, "Q", "HEAD", "start", 17, dx=8, dy=20)
    sc.dotp(P, 5.0)
    sc.label(P, "P", "HEAD", "start", 17, dx=-24, dy=-10)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=-8)
    sc.label(((O[0] + Q[0]) / 2, (O[1] + Q[1]) / 2), "a " + _e("R"), "HEAD", "end", 16, dx=-8, dy=20)
    sc.label(((Q[0] + P[0]) / 2, (Q[1] + P[1]) / 2), "v" + S("", "z") + " t " + bold("k") + S("", "0"), "HEAD",
             "start", 16, dx=14, dy=26)
    sc.label(((O[0] + P[0]) / 2, (O[1] + P[1]) / 2), "r" + S("", "0") + "ᴾ".replace("ᴾ", "") + S("", ""), "HEAD",
             "end", 1, dx=-1000, dy=-1000)
    return sc
