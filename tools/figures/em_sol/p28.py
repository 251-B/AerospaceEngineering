"""Problem 28: spherical pendulum hanging from a point A that oscillates on the vertical axis, z_A = a sin(omega t)."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

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
