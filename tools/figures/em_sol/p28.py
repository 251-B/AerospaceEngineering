"""Problem 28: spherical pendulum hanging from a point A that oscillates on the vertical axis, z_A = a sin(omega t)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

PHI = 50.0                                 # polar angle of AP from the upward vertical in the drawing (deg)
TH = 35.0                                  # azimuth in the drawing (deg)


@figure("p28-meridian",
        "Vertical plane through the axis Az' and the cord AP: the fixed point O, the support A at height a sin(omega t) "
        "on the common vertical axis z = z', the cord of length L at the angle phi from the upward vertical, the right "
        "triangle with legs L cos phi (vertical) and L sin phi (horizontal, along u), and the unit vectors e_r and e_phi",
        r"Vertical plane that contains $Az'$ and the cord. $A$ moves on the fixed axis $Oz$ ($z \equiv z'$), at height "
        r"$a\sin\omega t$; the axes of $Ax'y'z'$ stay parallel to those of $Oxyz$. In the shaded right triangle the "
        r"hypotenuse is the cord $|AP| = L$, the leg adjacent to $\varphi$ is vertical, $L\cos\varphi$ along $\mathbf k$, "
        r"and the opposite leg is horizontal, $L\sin\varphi$ along $\mathbf u = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j$. "
        r"$\mathbf e_r, \mathbf e_\varphi$ in orange")
def meridian():
    sc = Scene(560, 520, (190, 430), 150)
    O = (0.0, 0.0)
    A = (0.0, 1.05)
    f = math.radians(PHI)
    P = (A[0] + math.sin(f), A[1] + math.cos(f))
    # fixed axes at O (grey) and translated axes at A (blue)
    fixed_axis(sc, O, 0, 1.55, bold("u") + " (at O)", off=(30, 22))
    fixed_axis(sc, (0.0, -0.15), 90, 0.8, "z", off=(14, 6))
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=18)
    sc.dim((-0.35, 0.0), (-0.35, A[1]), "a sin ωt", off=(-44, 4))
    sc.dashed((-0.42, 0.0), (0.0, 0.0))
    sc.dashed((-0.42, A[1]), (0.0, A[1]))
    sc.line(A, (1.6, A[1]), "BLUE", 1.3, "6 4")
    sc.label((1.6, A[1]), bold("u"), "BLUE", "start", 16, dx=8, dy=5)
    sc.line(A, (0.0, A[1] + 1.65), "BLUE", 1.3)
    sc.vec((0.0, A[1] + 1.4), (0.0, A[1] + 1.65), None, "BLUE", 1.3)
    sc.label((0.0, A[1] + 1.65), "z ≡ z′", "BLUE", "start", 16, dx=10, dy=4)
    # key triangle A - (A + L cos phi k) - P
    T = (A[0], P[1])
    triangle(sc, [A, T, P])
    right_angle(sc, T, 0, -90, 0.07)
    sc.dashed(T, P)
    sc.line(A, P, "HEAD", 2.4)
    sc.label(((A[0] + P[0]) / 2, (A[1] + P[1]) / 2), "L", "TEXT", "start", 17, dx=12, dy=8)
    sc.label((0.0, (A[1] + T[1]) / 2), "L cos φ", "TEXT", "end", 15, dx=-10, dy=10)
    sc.label(((T[0] + P[0]) / 2, T[1]), "L sin φ", "TEXT", "middle", 15, dy=-9)
    sc.angle(A, 0.3, 90 - PHI, 90, "φ", name_r=0.42)
    # spherical unit vectors at P: e_r along AP, e_phi = cos(phi) u - sin(phi) k
    unit(sc, P, 90 - PHI, 0.38, bold("e") + S("", "r"), "ACC", off=(12, -6))
    unit(sc, P, -PHI, 0.38, bold("e") + S("", "φ"), "ACC", off=(16, 10))
    sc.mass(P, "P", r=7, name_off=(-6, -16))
    sc.dotp(A, 4.0)
    sc.label(A, "A", "HEAD", "end", 17, dx=-10, dy=-8)
    sc.gravity((1.65, 2.55), 0.4, "g")
    return sc


@figure("p28-azimuth",
        "Top view from +z with k out of the paper: the axes x' and y' of the translating frame, the horizontal "
        "projection of the cord of length L sin phi at the azimuth theta, its dashed components L sin phi cos theta and "
        "L sin phi sin theta, the horizontal unit vector u and the unit vector e_theta",
        r"View from $+z$, with $\mathbf k$ out of the paper ($\odot$). The horizontal projection of $\overrightarrow{AP}$ "
        r"has length $L\sin\varphi$ (the horizontal leg of the meridian triangle) and makes the azimuth $\theta$ with "
        r"$Ax'$; its components are $L\sin\varphi\cos\theta$ (adjacent) and $L\sin\varphi\sin\theta$ (opposite). "
        r"$\mathbf u$ is the unit vector of that direction and $\mathbf e_\theta$ is $\mathbf u$ turned $+90^\circ$ about "
        r"$\mathbf k$")
def azimuth():
    sc = Scene(520, 440, (150, 330), 220)
    A = (0.0, 0.0)
    t = math.radians(TH)
    Q = (math.cos(t), math.sin(t))                 # tip of the projection (L sin(phi) = 1 in the drawing)
    fixed_axis(sc, (-0.25, 0.0), 0, 1.55, "x′ ∥ x", off=(28, 5))
    fixed_axis(sc, (0.0, -0.25), 90, 1.4, "y′ ∥ y", off=(28, 2))
    axis_out(sc, A, bold("k"), off=(-20, 24))
    sc.label(A, "A", "HEAD", "end", 17, dx=-14, dy=-8)
    foot = (Q[0], 0.0)
    triangle(sc, [A, foot, Q])
    right_angle(sc, foot, 180, 90, 0.05)
    sc.line(A, Q, "HEAD", 2.0, "7 4")
    sc.label((Q[0] / 2, Q[1] / 2), "L sin φ", "TEXT", "end", 15, dx=-8, dy=-8)
    sc.dashed(foot, Q)
    sc.label((Q[0] / 2, 0.0), "L sin φ cos θ", "TEXT", "middle", 15, dy=22)
    sc.label((Q[0], Q[1] / 2), "L sin φ sin θ", "TEXT", "start", 15, dx=9, dy=5)
    sc.angle(A, 0.24, 0, TH, "θ", name_r=0.33)
    unit(sc, Q, TH, 0.3, bold("u"), "ACC", off=(10, -6))
    unit(sc, Q, TH + 90, 0.3, bold("e") + S("", "θ"), "ACC", off=(-12, -10))
    sc.dotp(Q, 4.5, "ACC")
    sc.label(Q, "projection of P", "TEXT", "start", 13, italic=False, dx=10, dy=22)
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


@figure("p28-fbd",
        "Free-body diagram of the particle on the cord in the translating frame of the support: cord tension, weight "
        "and the inertia force of the oscillating support",
        r"Forces on $P$ in the translating frame $Ax'y'z'$: the tension $-T\,\mathbf e_r$, the weight $-mg\,\mathbf k$ "
        r"and the inertia force of the origin $ma\omega^2\sin\omega t\,\mathbf k$ (dashed). The last two add up to an "
        r"effective weight $-mg_e\,\mathbf k$ with $g_e = g - a\omega^2\sin\omega t$.")
def fbd():
    sc = Scene(920, 500, (300, 440), 210)
    O = (0.0, 0.0)
    A = (0.0, 0.25)
    f = math.radians(30.0)
    er = (math.sin(f), math.cos(f))                    # (u, k) components of e_r
    ep = (math.cos(f), -math.sin(f))                   # e_phi
    P = (A[0] + er[0], A[1] + er[1])
    # vertical axis through O and A, fixed point O
    sc.line((0.0, -0.15), (0.0, 1.95), "EDGE", 1.3, "10 3 2 3")
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=8)
    sc.label((0.0, 1.95), "z ≡ z′", "TEXT", "start", 15, dx=10, dy=4)
    # the support A oscillates along the axis
    sc.vec((-0.14, A[1]), (-0.14, A[1] + 0.2), None, "GREEN", 2.0, head=9)
    sc.vec((-0.14, A[1]), (-0.14, A[1] - 0.2), None, "GREEN", 2.0, head=9)
    sc.label((-0.14, A[1]), "A oscillates: a sin ωt", "GREEN", "end", 15, weight="700", dx=-12, dy=5)
    sc.dotp(A, 4.0)
    sc.label(A, "A", "HEAD", "start", 17, dx=12, dy=22)
    axis_in(sc, (-0.45, 0.85), None, "ACC")
    sc.label((-0.45, 0.85), S(bold("e"), "θ") + " into the paper", "ACC", "end", 16, weight="700", dx=-16, dy=5)
    # translating axes at A (u to the right, k along the axis)
    unit(sc, A, 0, 0.4, bold("u"), "BLUE", off=(4, 22))
    # cord
    sc.line(A, P, "HEAD", 2.6)
    # forces
    sc.vec(P, (P[0] - 0.6 * er[0], P[1] - 0.6 * er[1]), None, "PINK", 2.8, head=11)
    mid = (P[0] - 0.33 * er[0], P[1] - 0.33 * er[1])
    sc.label(mid, "−T " + S(bold("e"), "r"), "PINK", "end", 16, weight="700", dx=-12, dy=2)
    sc.note((P[0] + 0.15, 0.05), "T ≥ 0: a cord can only pull", "TEXT", "start", 14)
    sc.vec(P, (P[0], P[1] - 0.8), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.8), "−m g " + bold("k"), "PINK", "start", 16, weight="700", dx=10, dy=4)
    xa = P[0] - 0.08
    _dvec(sc, (xa, P[1] + 0.05), (xa, P[1] + 0.4), "PINK", 2.6)
    sc.label((xa, P[1] + 0.4), S("F", "A") + " = m a ω² sin(ωt) " + bold("k"), "PINK", "start", 15, weight="700", dx=-14,
             dy=-36)
    sc.label((xa, P[1] + 0.4), "(inertia)", "PINK", "start", 14, dx=-14, dy=-14)
    unit(sc, P, 60.0, 0.3, S(bold("e"), "r"), "ACC", off=(14, -8))
    unit(sc, P, -30.0, 0.3, S(bold("e"), "φ"), "ACC", off=(18, 10))
    sc.mass(P, "P", r=7, name_off=(16, 26))
    # box: effective weight
    bx0, by0, bx1, by1 = 1.15, 1.0, 2.9, 0.62
    sc.poly([(bx0, by0), (bx1, by0), (bx1, by1), (bx0, by1)], "EDGE", 1.2, close=True)
    sc.note((bx0 + 0.07, by0 - 0.13), "weight + inertia force = −m g_e k", "TEXT", "start", 14)
    sc.note((bx0 + 0.07, by0 - 0.29), "g_e = g − a ω² sin ωt", "TEXT", "start", 14)
    return sc
