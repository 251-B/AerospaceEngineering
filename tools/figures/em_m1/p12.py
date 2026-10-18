"""Figure of bank item P12 (block on a turntable that spins up)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold


def _out_of_page(sc, p, r=0.13, col="BLUE"):
    """Axis pointing out of the page: circle with a dot."""
    sc.circle(p, r, col, 1.8)
    sc.dotp(p, 2.6, col)


@figure("p12-turntable-block",
        "Top view of a horizontal turntable of centre O spinning up counter-clockwise with angular rate Omega and angular "
        "acceleration beta; a small block P at distance r0 from the axis, with the unit vectors e_r and e_phi and the "
        "friction force F decomposed into a component towards the axis and a component along e_phi",
        r"Turntable seen from above: fixed axes $x,y$ and $\mathbf k$ (out of the page, upwards) at the axis $O$, rate "
        r"$\Omega=\beta t$ and angular acceleration $\beta$ (counter-clockwise), block $P$ at distance $r_0$; while it sticks, "
        r"the friction $\mathbf F$ has a component $F_r<0$ towards $O$ and a component $F_\varphi>0$ along $\mathbf e_\varphi$")
def p12():
    sc = Scene(640, 375, (205, 192), 62)
    O = (0.0, 0.0)
    R = 2.6
    sc.circle(O, R, "HEAD", 2.0, fill="HEAD", opacity=0.06)
    # fixed axes and k out of the page
    sc.vec(O, (3.4, 0.0), "x", "BLUE", 1.7, name_off=(10, 5))
    sc.vec(O, (0.0, 2.85), "y", "BLUE", 1.7, name_off=(-14, 10))
    _out_of_page(sc, O)
    sc.label(O, bold("k"), "BLUE", "end", 16, dx=-10, dy=20)
    sc.label(O, "O", "HEAD", "end", 16, dx=-10, dy=-8)
    # rotation rate and angular acceleration
    sc.spin(O, R + 0.35, 112, 150, "Ω = βt", name_r=R + 0.85)
    sc.spin(O, R + 0.35, 200, 228, "β", name_r=R + 0.7)
    # block at the angle phi on the table
    phi = math.radians(35)
    er = (math.cos(phi), math.sin(phi))
    et = (-math.sin(phi), math.cos(phi))
    r0 = 1.75
    P = (r0 * er[0], r0 * er[1])
    sc.dashed(O, (R * er[0], R * er[1]))
    sc.angle(O, 0.65, 0, 35, "φ", name_r=0.9)
    sc.dim((0.22 * et[0] + 0.25 * er[0], 0.22 * et[1] + 0.25 * er[1]), (P[0] + 0.22 * et[0], P[1] + 0.22 * et[1]), S("r", "0"), off=(-10, -10))
    s = 0.16
    sc.poly([(P[0] + s * (er[0] * a + et[0] * b), P[1] + s * (er[1] * a + et[1] * b)) for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))],
            "HEAD", 1.6, fill="ACC", opacity=0.9, close=True)
    sc.label(P, "P", "HEAD", "middle", 17, dx=4, dy=30)
    # unit vectors (blue)
    sc.vec(P, (P[0] + 0.95 * er[0], P[1] + 0.95 * er[1]), S(bold("e"), "r"), "BLUE", 1.8, name_off=(16, 4))
    sc.vec(P, (P[0] + 0.85 * et[0], P[1] + 0.85 * et[1]), S(bold("e"), "φ"), "BLUE", 1.8, name_off=(-6, -10))
    # ---- second panel: friction decomposition at P (enlarged) -------------------------
    Q = (5.2, -0.5)
    k = 1.6
    Fr = (-1.0 * er[0] * k, -1.0 * er[1] * k)       # towards the axis
    Ft = (0.55 * et[0] * k, 0.55 * et[1] * k)       # along e_phi
    sc.dashed((Q[0] - 1.9 * er[0], Q[1] - 1.9 * er[1]), (Q[0] + 0.9 * er[0], Q[1] + 0.9 * er[1]))
    sc.note((Q[0] + 0.9 * er[0], Q[1] + 0.9 * er[1]), "radius OP", anchor="middle", dx=0, dy=-10, size=12)
    sc.poly([(Q[0] + s * (er[0] * a + et[0] * b), Q[1] + s * (er[1] * a + et[1] * b)) for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))],
            "HEAD", 1.6, fill="ACC", opacity=0.9, close=True)
    sc.vec(Q, (Q[0] + Fr[0], Q[1] + Fr[1]), S("F", "r"), "PINK", 1.8, name_off=(-6, 20))
    sc.vec(Q, (Q[0] + Ft[0], Q[1] + Ft[1]), S("F", "φ"), "PINK", 1.8, name_off=(-14, -6))
    F = (Q[0] + Fr[0] + Ft[0], Q[1] + Fr[1] + Ft[1])
    sc.vec(Q, F, bold("F"), "PINK", 2.2, name_off=(-12, -4))
    sc.dashed((Q[0] + Fr[0], Q[1] + Fr[1]), F)
    sc.dashed((Q[0] + Ft[0], Q[1] + Ft[1]), F)
    ang_F = math.degrees(math.atan2(F[1] - Q[1], F[0] - Q[0]))
    ang_in = math.degrees(math.atan2(-er[1], -er[0]))
    sc.angle(Q, 0.7, ang_F, ang_in, "ψ", name_r=0.95)
    sc.note((Q[0], Q[1]), "block P, enlarged", anchor="middle", dx=-40, dy=110, size=12)
    return sc
