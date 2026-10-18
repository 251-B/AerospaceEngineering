"""Figure of bank item P14 (drone on a logarithmic spiral at constant speed)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold

B = 0.75          # spiral parameter of the numerical case (alpha = 53.13 deg)
PHI_P = 0.75      # polar angle of the drawn position of P (rad)


def _pt(phi):
    r = math.exp(B * phi)
    return (r * math.cos(phi), r * math.sin(phi))


@figure("p14-log-spiral",
        "Logarithmic spiral in a horizontal plane with the drone P on it, the polar radius r and angle phi from the x axis, "
        "the tangent and normal unit vectors at P and the constant angle alpha between the radius and the tangent",
        r"Drone $P$ on the spiral $r=r_0e^{b\varphi}$ flown with constant speed $v_0$ ($\varphi$ increasing): "
        r"polar coordinates $(r,\varphi)$ about $O$, unit tangent $\mathbf e_t$ and principal normal $\mathbf e_n$, "
        r"constant angle $\alpha$ between $\mathbf e_r$ and $\mathbf e_t$ (drawn for $b=3/4$)")
def p14():
    sc = Scene(640, 400, (250, 330), 82)
    sc.axes((0.0, 0.0), 0, 0.75, ("x", "y"), "BLUE")
    sc.label((0.0, 0.0), "O", "BLUE", "end", 16, dx=-9, dy=-6)
    # the spiral, from deep inside to beyond P
    sc.curve(_pt, -3.0, 1.72, n=260, col="HEAD", w=2.2)
    P = _pt(PHI_P)
    r = math.hypot(*P)
    er = (math.cos(PHI_P), math.sin(PHI_P))
    # polar radius as a vector and its extension beyond P
    sc.vec((0.0, 0.0), P, None, "BLUE", 1.6)
    sc.label((P[0] * 0.52, P[1] * 0.52), "r", "BLUE", "middle", 17, dx=-12, dy=-6)
    sc.dashed(P, (P[0] + 0.85 * er[0], P[1] + 0.85 * er[1]))
    sc.angle((0.0, 0.0), 0.42, 0, math.degrees(PHI_P), "φ", name_r=0.60)
    # intrinsic basis at P
    al = math.atan2(1.0, B)
    th_t = PHI_P + al
    th_n = th_t + math.pi / 2
    Lv = 0.72
    tt = (P[0] + Lv * math.cos(th_t), P[1] + Lv * math.sin(th_t))
    nn = (P[0] + Lv * math.cos(th_n), P[1] + Lv * math.sin(th_n))
    sc.vec(P, tt, S(bold("e"), "t"), "BLUE", 2.0, name_off=(14, 2))
    sc.vec(P, nn, S(bold("e"), "n"), "BLUE", 2.0, name_off=(-4, -10))
    sc.angle(P, 0.38, math.degrees(PHI_P), math.degrees(th_t), "α", name_r=0.55)
    sc.mass(P, "P", r=7.5, name_off=(18, 18))
    # curve label and sense of travel (phi increasing)
    a0, a1 = _pt(1.30), _pt(1.38)
    sc.vec(a0, a1, None, "HEAD", 2.2, head=11)
    lab = _pt(1.45)
    sc.label(lab, S("r = r", "0") + " e" + '<tspan baseline-shift="super" font-size="70%">bφ</tspan>', "HEAD", "start", 16,
             dx=14, dy=0)
    sc.note((2.1, 3.2), "horizontal plane", "TEXT", "start", 13)
    sc.note((2.1, 2.95), S("speed v", "0") + " = const", "TEXT", "start", 13)
    return sc
