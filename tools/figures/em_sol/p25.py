"""Problem 25: astronaut tied by a cord of length L to a spacecraft S on a conic orbit around F."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

P_ORB, E_ORB = 1.6, 0.5                    # semi-latus rectum and eccentricity of the drawing
NU = 60.0                                  # true anomaly of S in the drawing (deg)


def _r(nu_deg):
    return P_ORB / (1 + E_ORB * math.cos(math.radians(nu_deg)))


@figure("p25-orbit",
        "Orbital plane Fxy with k out of the paper: the orbit of S around the focus F, the true anomaly nu, the right "
        "triangle with hypotenuse r and legs r cos nu and r sin nu, the polar basis i1 (radial) and j1 at S, and the "
        "unit tangent u_t of the orbit",
        r"Orbital plane seen from $+\mathbf k$ ($\odot$). The shaded right triangle has hypotenuse $|FS| = r$, leg "
        r"$r\cos\nu$ along $\mathbf i$ (adjacent to $\nu$) and leg $r\sin\nu$ along $\mathbf j$ (opposite). "
        r"$\mathbf i_1$ is the radial direction and $\mathbf j_1$ is $\mathbf i_1$ turned $+90^\circ$ (blue); "
        r"$\mathbf u_t$ is the unit tangent of the orbit (orange)")
def orbit():
    sc = Scene(560, 420, (360, 222), 95)
    F = (0.0, 0.0)
    r = _r(NU)
    Sp = (r * math.cos(math.radians(NU)), r * math.sin(math.radians(NU)))
    # orbit (dashed) and axes
    pts = [(_r(n) * math.cos(math.radians(n)), _r(n) * math.sin(math.radians(n))) for n in range(0, 361, 3)]
    sc.poly(pts, "EDGE", 1.2, "6 5")
    fixed_axis(sc, (-3.55, 0.0), 0, 5.3, "x", off=(12, 5))
    fixed_axis(sc, (0.0, -2.05), 90, 4.0, "y", off=(12, 2))
    axis_out(sc, F, bold("k"), off=(-22, -12))
    sc.label(F, "F", "HEAD", "end", 17, dx=-14, dy=22)
    # key triangle F - foot - S
    foot = (Sp[0], 0.0)
    triangle(sc, [F, foot, Sp])
    right_angle(sc, foot, 180, 90, 0.08)
    sc.line(F, Sp, "HEAD", 1.6)
    sc.label((Sp[0] / 2, Sp[1] / 2), "r", "TEXT", "end", 17, dx=-10, dy=-4)
    sc.dashed(foot, Sp)
    sc.label((Sp[0] / 2, 0.0), "r cos ν", "TEXT", "middle", 15, dy=22)
    sc.label((Sp[0], Sp[1] * 0.45), "r sin ν", "TEXT", "start", 15, dx=9)
    sc.angle(F, 0.34, 0, NU, "ν", name_r=0.47)
    # polar basis and tangent at S
    unit(sc, Sp, NU, 0.62, bold("i") + S("", "1"), off=(12, -8))
    unit(sc, Sp, NU + 90, 0.62, bold("j") + S("", "1"), off=(-18, 14))
    nu = math.radians(NU)
    ut = math.degrees(math.atan2(E_ORB + math.cos(nu), -math.sin(nu)))
    unit(sc, Sp, ut, 0.7, bold("u") + S("", "t"), "ACC", off=(16, -2))
    sc.mass(Sp, "S", r=7, col="HEAD", name_off=(20, 12))
    sc.note((-3.4, 1.9), "orbit r = p / (1 + e cos ν)", "TEXT", "start", 13)
    return sc


@figure("p25-cord",
        "Moving frame Sx1y1 with k out of the paper: the astronaut P on the circle of radius L around S at the angle "
        "theta from x1, the right triangle with legs L cos theta and L sin theta, the cord basis e_c and e_theta, and the "
        "inertial direction i at the angle nu from i1",
        r"Frame $Sx_1y_1$ seen from $+\mathbf k$ ($\odot$), with $\mathbf i_1$ to the right. In the shaded triangle the "
        r"hypotenuse is the cord $|SP| = L$, the leg adjacent to $\theta$ is $L\cos\theta$ (along $\mathbf i_1$) and "
        r"the opposite leg is $L\sin\theta$ (along $\mathbf j_1$). $\mathbf e_c, \mathbf e_\theta$ in orange. The "
        r"inertial axis $\mathbf i$ (grey) is at $-\nu$ from $\mathbf i_1$, so the cord makes $\theta + \nu$ with it")
def cord():
    sc = Scene(600, 470, (250, 270), 150)
    Sp = (0.0, 0.0)
    th = 50.0
    t = math.radians(th)
    P = (math.cos(t), math.sin(t))
    sc.circle(Sp, 1.0, "EDGE", 1.1, "5 4")
    fixed_axis(sc, (-0.25, 0.0), 0, 1.75, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.25), 90, 1.6, S("y", "1"), off=(14, 2))
    axis_out(sc, Sp, bold("k"), off=(-20, 24))
    # inertial direction i at -nu from i1 (towards F is -i1)
    fixed_axis(sc, Sp, -NU, 1.4, bold("i"), off=(12, 8))
    sc.angle(Sp, 0.5, -NU, 0, "ν", name_r=0.62)
    sc.note((-1.55, -1.1), "F lies along −" + "i₁", "TEXT", "start", 13)
    # key triangle S - foot - P
    foot = (P[0], 0.0)
    triangle(sc, [Sp, foot, P])
    right_angle(sc, foot, 180, 90, 0.06)
    sc.line(Sp, P, "HEAD", 2.6)
    sc.label((P[0] / 2, P[1] / 2), "L", "TEXT", "end", 17, dx=-10, dy=-6)
    sc.dashed(foot, P)
    sc.label((P[0] / 2, 0.0), "L cos θ", "TEXT", "middle", 15, dy=20)
    sc.label((P[0], P[1] * 0.5), "L sin θ", "TEXT", "start", 15, dx=9)
    sc.angle(Sp, 0.28, 0, th, "θ", name_r=0.4)
    # basis of the cord at P
    unit(sc, P, th, 0.4, bold("e") + S("", "c"), "ACC", off=(12, -6))
    unit(sc, P, th + 90, 0.4, bold("e") + S("", "θ"), "ACC", off=(-14, -8))
    sc.mass(P, "P", r=7, name_off=(26, -4))
    sc.label(Sp, "S", "HEAD", "end", 17, dx=-12, dy=-10)
    return sc
