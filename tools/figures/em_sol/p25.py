"""Problem 25: astronaut tied by a cord of length L to a spacecraft S on a conic orbit around F."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

P_ORB, E_ORB = 1.0, 0.5                    # semi-latus rectum and eccentricity of the drawing
NU = 110.0                                 # true anomaly of S in the drawing (deg)
TH = 40.0                                  # cord angle theta in the drawing (deg)
I0, J0, K0 = S(bold("i"), "0"), S(bold("j"), "0"), S(bold("k"), "0")
I1, J1, K1 = S(bold("i"), "1"), S(bold("j"), "1"), S(bold("k"), "1")


def _r(nu_deg):
    return P_ORB / (1 + E_ORB * math.cos(math.radians(nu_deg)))


def _dvec(sc, a, b, col="PINK", w=2.4, head=10):
    """Dashed arrow (inertia force) from world point a to b."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


@figure("p25-orbit",
        "Orbital plane with k0 out of the paper: the orbit of S around the focus F, the true anomaly nu, the right "
        "triangle with hypotenuse r and legs r cos nu (negative here) and r sin nu, the polar basis i1 (radial) and j1 "
        "at S, and the unit tangent e_t of the orbit",
        r"Orbital plane seen from $+\mathbf k_0$ ($\odot$). The shaded right triangle has hypotenuse $|FS| = r$, leg "
        r"$r\cos\nu$ along $\mathbf i_0$ (adjacent to $\nu$) and leg $r\sin\nu$ along $\mathbf j_0$ (opposite). "
        r"$\mathbf i_1$ is the radial direction and $\mathbf j_1$ is $\mathbf i_1$ turned $+90^\circ$ (blue); "
        r"$\mathbf e_t$ is the unit tangent of the orbit (orange)")
def orbit():
    sc = Scene(680, 500, (410, 290), 165)
    F = (0.0, 0.0)
    r = _r(NU)
    nu = math.radians(NU)
    Sp = (r * math.cos(nu), r * math.sin(nu))
    # orbit (dashed) and axes
    pts = [(_r(n) * math.cos(math.radians(n)), _r(n) * math.sin(math.radians(n))) for n in range(0, 361, 3)]
    sc.poly(pts, "EDGE", 1.4, "6 5")
    fixed_axis(sc, (-2.3, 0.0), 0, 3.3, "x (" + I0 + ")", off=(-8, -12))
    fixed_axis(sc, (0.0, -1.3), 90, 2.75, "y (" + J0 + ")", off=(30, 6))
    axis_out(sc, F, None)
    sc.label(F, K0 + " (⊙)", "TEXT", "start", 16, weight="700", dx=14, dy=26)
    sc.label(F, "F", "HEAD", "end", 17, dx=-12, dy=26)
    # key triangle F - foot - S (the foot is on the negative side of the x axis)
    foot = (Sp[0], 0.0)
    triangle(sc, [F, foot, Sp])
    right_angle(sc, foot, 0, 90, 0.07)
    sc.line(F, Sp, "HEAD", 2.4)
    sc.label((Sp[0] / 2, Sp[1] / 2), "r", "TEXT", "start", 17, dx=12, dy=2)
    sc.dashed(foot, Sp)
    sc.label((-0.25, 0.0), "r cos ν (negative here)", "TEXT", "end", 15, dy=24)
    sc.label((Sp[0], Sp[1] * 0.5), "r sin ν", "TEXT", "end", 15, dx=-8, dy=5)
    sc.angle(F, 0.30, 0, NU, "ν", name_r=0.42)
    # polar basis and tangent at S
    unit(sc, Sp, NU, 0.35, I1, off=(12, -10))
    unit(sc, Sp, NU + 90, 0.35, J1, off=(-16, 8))
    rp = _r(NU) * E_ORB * math.sin(nu) / (1 + E_ORB * math.cos(nu))
    ut = math.degrees(math.atan2(rp * math.sin(nu) + r * math.cos(nu), rp * math.cos(nu) - r * math.sin(nu)))
    unit(sc, Sp, ut, 0.35, S(bold("e"), "t"), "ACC", off=(-6, -14))
    sc.mass(Sp, "S", r=7, col="HEAD", name_off=(14, -14))
    # nu-dot arrow along the orbit behind S, in the sense of growing nu
    arc = []
    for n in range(135, 154, 2):
        rr = _r(n) + 0.09
        arc.append((rr * math.cos(math.radians(n)), rr * math.sin(math.radians(n))))
    sc.poly(arc, "GREEN", 1.8)
    arrow_head(sc.c, sc.P(arc[-2]), sc.P(arc[-1]), "GREEN", 9)
    sc.label(arc[len(arc) // 2], "ν̇ > 0", "GREEN", "middle", 16, weight="700", dx=-8, dy=-18)
    sc.note((-2.25, -1.1), "orbit r = p / (1 + e cos ν)", "TEXT", "start", 14)
    return sc


@figure("p25-cord",
        "Moving frame Sx1y1 with k1 out of the paper: the astronaut P on the circle of radius L around S at the angle "
        "theta from x1, the right triangle with legs L cos theta and L sin theta, the cord basis e_c and e_theta, and "
        "the inertial axis i0 at the angle nu from i1",
        r"Frame $Sx_1y_1$ seen from $+\mathbf k_1$ ($\odot$), with $\mathbf i_1$ to the right. In the shaded triangle "
        r"the hypotenuse is the cord $|SP| = L$, the leg adjacent to $\theta$ is $L\cos\theta$ (along $\mathbf i_1$) and "
        r"the opposite leg is $L\sin\theta$ (along $\mathbf j_1$). $\mathbf e_c, \mathbf e_\theta$ in orange. The "
        r"inertial axis $\mathbf i_0$ (grey) is at $-\nu$ from $\mathbf i_1$, so the cord makes $\theta + \nu$ with it")
def cord():
    sc = Scene(760, 560, (400, 300), 190)
    Sp = (0.0, 0.0)
    t = math.radians(TH)
    P = (math.cos(t), math.sin(t))
    sc.circle(Sp, 1.0, "EDGE", 1.1, "5 4")
    # moving axes (blue) and the direction of F
    sc.vec((-1.3, 0.0), (1.65, 0.0), "x₁ (" + I1 + ")", "BLUE", 1.6, name_off=(-8, 22), size=16, head=8)
    sc.vec((0.0, -0.3), (0.0, 1.5), "y₁ (" + J1 + ")", "BLUE", 1.6, name_off=(34, 4), size=16, head=8)
    sc.line((-1.3, 0.0), (-1.85, 0.0), "EDGE", 1.3, "6 4")
    sc.vec((-1.7, 0.0), (-2.0, 0.0), None, "EDGE", 1.3, head=9)
    sc.label((-1.65, 0.0), "towards F (−" + I1 + ")", "TEXT", "middle", 15, dy=-12)
    axis_out(sc, Sp, None, "BLUE")
    sc.label(Sp, K1 + " (⊙)", "BLUE", "end", 16, weight="700", dx=-16, dy=26)
    # inertial direction i0 at -nu from i1
    fixed_axis(sc, Sp, -NU, 1.1, I0, off=(14, 14))
    sc.arc(Sp, 0.55, -NU, TH, "GREEN", 1.6)
    sc.label((0.55 * math.cos(math.radians(-35)), 0.55 * math.sin(math.radians(-35))), "θ + ν", "GREEN", "start", 16,
             weight="700", dx=14, dy=8)
    # key triangle S - foot - P
    foot = (P[0], 0.0)
    triangle(sc, [Sp, foot, P])
    right_angle(sc, foot, 180, 90, 0.06)
    sc.line(Sp, P, "HEAD", 2.8)
    sc.label((P[0] / 2, P[1] / 2), "L", "TEXT", "end", 17, dx=-10, dy=-8)
    sc.dashed(foot, P)
    sc.label((P[0] / 2, 0.0), "L cos θ", "TEXT", "middle", 15, dy=22)
    sc.label((P[0], P[1] * 0.5), "L sin θ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.angle(Sp, 0.26, 0, TH, "θ", name_r=0.37)
    # basis of the cord at P
    unit(sc, P, TH, 0.3, S(bold("e"), "c"), "ACC", off=(16, -6))
    unit(sc, P, TH + 90, 0.3, S(bold("e"), "θ"), "ACC", off=(-16, -8))
    sc.mass(P, "P", r=7, name_off=(18, 20))
    sc.label(Sp, "S", "HEAD", "start", 17, dx=12, dy=22)
    return sc


@figure("p25-fbd",
        "Free-body diagram of the astronaut in the moving frame: cord tension, gravity and the four inertia forces",
        r"Forces on $P$ in $S_1$: the tension $-T\,\mathbf e_c$, the gravity $m\,\mathbf g_S$ (equal at $P$ and $S$ by "
        r"hypothesis) and the inertia forces $\mathbf F_A = -m\,\mathbf a_0^S$, $\mathbf F_E$ across the cord and "
        r"$\mathbf F_C$, $\mathbf F_{COR}$ along it (dashed). In free flight $m\,\mathbf g_S$ and $\mathbf F_A$ cancel.")
def fbd():
    sc = Scene(840, 430, (270, 300), 185)
    Sp = (0.0, 0.0)
    t = math.radians(TH)
    ec = (math.cos(t), math.sin(t))
    et = (-math.sin(t), math.cos(t))
    P = (ec[0], ec[1])

    def at(p, d, L, off=(0.0, 0.0)):
        return (p[0] + L * d[0] + off[0], p[1] + L * d[1] + off[1])
    # frame at S
    sc.line(Sp, P, "EDGE", 1.4)
    unit(sc, Sp, 0, 0.5, I1, off=(2, 22))
    unit(sc, Sp, 90, 0.5, J1, off=(-16, 4))
    axis_out(sc, Sp, None, "BLUE")
    sc.label(Sp, K1 + " (⊙)", "BLUE", "end", 16, weight="700", dx=-16, dy=-12)
    sc.label(Sp, "S", "HEAD", "end", 17, dx=-12, dy=26)
    sc.spin(Sp, 0.3, 200.0, 340.0, "", name_r=0.4)
    sc.label((0.0, -0.3), "ω₁₀ = ν̇ " + K1, "GREEN", "middle", 16, weight="700", dy=34)
    # cord tension: from P towards S along the cord
    sc.vec(P, at(P, ec, -0.8), None, "PINK", 2.8, head=11)
    sc.label(at(P, ec, -0.45), "−T " + S(bold("e"), "c"), "PINK", "end", 16, weight="700", dx=-12, dy=-14)
    # gravity of F on P (equal to that at S): along -i1
    sc.vec(P, (P[0] - 0.6, P[1]), None, "PINK", 2.8, head=11)
    sc.label((P[0] - 0.6, P[1]), "m " + S("g", "S") + " = −m " + S("μ", "F") + " / r² " + I1, "PINK", "end", 15, weight="700",
             dx=-8, dy=-12)
    # inertia forces (dashed)
    _dvec(sc, P, (P[0] + 0.6, P[1]), "PINK", 2.6)
    sc.label((P[0] + 0.6, P[1]), S("F", "A") + " = −m " + S("a", "S") + " (inertia)", "PINK", "start", 15, weight="700",
             dx=10, dy=5)
    sc.note((P[0] + 0.6, P[1]), "equal and opposite to m g_S in free flight", "TEXT", "start", 13, dx=10, dy=24)
    fe = at(P, et, -0.5)
    _dvec(sc, P, fe, "PINK", 2.6)
    sc.label(fe, S("F", "E") + " = −m L ν̈ " + S(bold("e"), "θ"), "PINK", "start", 15, weight="700", dx=10, dy=6)
    sc.label(fe, "(inertia)", "PINK", "start", 14, dx=10, dy=24)
    fc = at(P, ec, 0.55)
    _dvec(sc, P, fc, "PINK", 2.6)
    sc.label(fc, S("F", "C") + " = m L ν̇² " + S(bold("e"), "c"), "PINK", "start", 15, weight="700", dx=10, dy=-14)
    sc.label(fc, "(inertia)", "PINK", "start", 14, dx=10, dy=2)
    off = 0.09
    fo = at(P, ec, 0.45, (off * et[0], off * et[1]))
    _dvec(sc, (P[0] + off * et[0], P[1] + off * et[1]), fo, "PINK", 2.6)
    sc.label(fo, S("F", "COR") + " = 2 m L ν̇ θ̇ " + S(bold("e"), "c") + " (inertia)", "PINK", "end", 15, weight="700",
             dx=-10, dy=-14)
    # cord basis at P
    unit(sc, P, TH, 0.3, S(bold("e"), "c"), "ACC", off=(16, 12))
    unit(sc, P, TH + 90, 0.3, S(bold("e"), "θ"), "ACC", off=(-16, -8))
    sc.mass(P, "P", r=7, name_off=(-4, 24))
    return sc
