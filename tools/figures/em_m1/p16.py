"""Figure of bank item P16 (particle on a free wedge on a smooth table)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold

ALPHA = 30.0


@figure("p16-free-wedge",
        "Wedge of mass M with a smooth incline at angle alpha on a smooth horizontal table; the wedge position is X measured "
        "from the fixed origin O; the particle P of mass m is on the incline at a distance s from the top edge A, measured "
        "down the slope; the normal reaction N and the weight act on P",
        r"Free wedge: the wedge (mass $M$) slides on the smooth table, its position is $X$ (abscissa of the corner $B$); "
        r"$P$ (mass $m$) slides on the smooth incline of angle $\alpha$, at the distance $s$ from the top edge $A$ measured "
        r"down the slope (unit vector $\mathbf u$); $\mathbf N=N\mathbf n$ is the normal reaction on $P$ (outward normal $\mathbf n$)")
def p16():
    sc = Scene(640, 330, (40, 268), 70)
    a = math.radians(ALPHA)
    # table
    sc.ground((-0.2, 0.0), (8.4, 0.0), side=-1)
    # axes at the fixed origin O on the table
    sc.vec((0.0, 0.0), (0.0, 1.0), "y", "BLUE", 1.9, name_off=(10, 6))
    sc.vec((0.0, 0.0), (1.0, 0.0), "x", "BLUE", 1.9, name_off=(8, 18))
    sc.label((0.0, 0.0), "O", "BLUE", "end", 16, dx=-6, dy=20)
    # wedge: corner B at (xB, 0), incline from the left corner L up to the top edge A above B
    Bw = 4.6
    H = Bw * math.tan(a)
    xB = 7.2
    Lc, Bc, A = (xB - Bw, 0.0), (xB, 0.0), (xB, H)
    sc.poly([Lc, Bc, A], "HEAD", 2.2, fill="HEAD", opacity=0.10, close=True)
    sc.label((xB - 1.05, 0.62), "M", "HEAD", "middle", 18)
    sc.label(A, "A", "HEAD", "start", 17, dx=8, dy=0)
    sc.label(Bc, "B", "HEAD", "start", 17, dx=6, dy=-6)
    sc.angle(Lc, 1.0, 0, ALPHA, "α", name_r=1.3)
    # wedge position X: dimension from O to B, drawn under the table
    sc.dim((0.0, -0.55), (xB, -0.55), "X", off=(0, -6))
    sc.dashed((xB, -0.05), (xB, -0.7))
    # particle on the incline
    u = (-math.cos(a), -math.sin(a))
    nu = (-math.sin(a), math.cos(a))
    s = 2.0
    rp = 0.12
    Pc = (A[0] + s * u[0], A[1] + s * u[1])
    P = (Pc[0] + rp * nu[0], Pc[1] + rp * nu[1])
    # s along the slope, offset outwards
    off = 0.62
    sc.dim((A[0] + off * nu[0], A[1] + off * nu[1]), (Pc[0] + off * nu[0], Pc[1] + off * nu[1]), "s", off=(-6, -8))
    sc.dashed(A, (A[0] + (off + 0.12) * nu[0], A[1] + (off + 0.12) * nu[1]))
    # unit vectors u and nu drawn from a point further down the slope
    Q = (A[0] + 3.1 * u[0] + 0.55 * nu[0], A[1] + 3.1 * u[1] + 0.55 * nu[1])
    sc.vec(Q, (Q[0] + 0.75 * u[0], Q[1] + 0.75 * u[1]), bold("u"), "BLUE", 1.8, name_off=(-4, -10))
    sc.vec(Q, (Q[0] + 0.75 * nu[0], Q[1] + 0.75 * nu[1]), bold("n"), "BLUE", 1.8, name_off=(-12, 2))
    # forces on P
    sc.vec(P, (P[0] + 1.1 * nu[0], P[1] + 1.1 * nu[1]), bold("N"), "PINK", 2.0, name_off=(-14, 0))
    sc.vec(P, (P[0], P[1] - 1.1), "mg", "PINK", 2.0, name_off=(18, 6))
    sc.mass(P, "P", r=8, name_off=(18, -8))
    sc.label(P, "m", "TEXT", "middle", 15, dx=-26, dy=-4)
    sc.gravity((8.1, 2.9), 0.9, "g")
    return sc
