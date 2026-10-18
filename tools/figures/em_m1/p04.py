"""Figure of bank item P04 (radial tube on a turntable whose rate increases, bead tied to the axis by a spring)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene


@figure("p04-turntable-tube",
        "Top view of a turntable turning about the vertical axis through O; a smooth radial tube fixed on it carries a bead P joined to O by a spring; the rotating axes x1, y1 make the angle theta with the fixed axes x0, y0",
        r"Top view: turntable with rate $\Omega(t)=\dot\theta=\Omega_0+\beta t$ about the vertical axis $O\mathbf k$ (out of the page); "
        r"smooth tube along $\mathbf i_1$, bead $P$ at distance $x$ from $O$, spring of stiffness $k$ and zero natural length")
def p04():
    sc = Scene(640, 440, (300, 236), 82)
    th = math.radians(32)
    u = (math.cos(th), math.sin(th))
    w = (-math.sin(th), math.cos(th))
    Rt = 2.35
    # turntable and fixed frame
    sc.circle((0, 0), Rt, "HEAD", 2.0, fill="HEAD", opacity=0.06)
    sc.vec((0, 0), (3.0, 0), S("x", "0"), "BLUE", 1.7, name_off=(14, 6))
    sc.vec((0, 0), (0, 2.6), S("y", "0"), "BLUE", 1.7, name_off=(14, 2))
    # tube along i1: two walls
    a0, a1 = -(Rt - 0.05), Rt - 0.05
    hw = 0.13
    for s in (1, -1):
        sc.line((a0 * u[0] + s * hw * w[0], a0 * u[1] + s * hw * w[1]),
                (a1 * u[0] + s * hw * w[0], a1 * u[1] + s * hw * w[1]), "HEAD", 2.2)
    # rotating axes
    L1 = 3.05
    sc.vec((0, 0), (L1 * u[0], L1 * u[1]), S("x", "1"), "BLUE", 2.0, name_off=(12, -6))
    sc.vec((0, 0), (2.35 * w[0], 2.35 * w[1]), S("y", "1"), "BLUE", 2.0, name_off=(-12, -6))
    sc.angle((0, 0), 0.75, 0, 32, "θ", name_r=0.98)
    # spring from O to the bead
    xb = 1.55
    P = (xb * u[0], xb * u[1])
    sc.spring((0.0, 0.0), P, coils=6, amp=5.0)
    sc.mass(P, "P", r=8, name_off=(22, 26))
    sc.label((0.8 * u[0] + 0.3 * w[0], 0.8 * u[1] + 0.3 * w[1]), "k", "TEXT", "middle", 16, dy=5)
    # dimension x parallel to the tube
    off = 0.62
    A = (off * w[0], off * w[1])
    B = (xb * u[0] + off * w[0], xb * u[1] + off * w[1])
    sc.dashed((hw * w[0], hw * w[1]), (0.72 * w[0], 0.72 * w[1]))
    sc.dashed((P[0] + hw * w[0], P[1] + hw * w[1]), (P[0] + 0.72 * w[0], P[1] + 0.72 * w[1]))
    sc.dim(A, B, "x", off=(-8, -10))
    # vertical axis out of the page and the rate
    sc.circle((0, 0), 0.07, "BLUE", 1.4)
    sc.dotp((0, 0), 2.0, "BLUE")
    sc.label((0, 0), "O", "BLUE", "end", 16, dx=-10, dy=18)
    sc.spin((0, 0), 2.7, 118, 160, "Ω(t)", name_r=3.05)
    return sc
