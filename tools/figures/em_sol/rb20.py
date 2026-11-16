"""Problem RB-20: Pioneer III spacecraft, yo-yo de-spin (probe angle theta, cord angle phi, involute of the free cord)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb17 import off_dir, rot_pair
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold, dot1

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1 = S(I, "1"), S(J, "1")
ER, ET = S(bold("e"), "r"), S(bold("e"), "t")
TH, PH = 20.0, 60.0
R_ = 3.0


def sub(t):
    return '<tspan baseline-shift="sub" font-size="70%">' + t + "</tspan>"


# ------------------------------------------------------------------------------------------------ rb20-bases
@figure("rb20-bases",
        "The probe seen along its spin axis with the inertial basis, the probe basis turned by theta and the cord basis "
        "turned by phi from the probe basis.",
        r"Rotations about $\mathbf k_0$ (⊙): $\theta$ from $\mathbf i_0$ to $\mathbf i_1$ (probe) and $\phi$ from "
        r"$\mathbf i_1$ to $\mathbf e_r$ (point of tangency $T$, measured in the probe from the release point $A$).")
def bases():
    sc = Scene(840, 800, (400, 400), 82)
    G = (0.0, 0.0)
    L = 2.0
    sc.poly(circle_pts(G, R_), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.14)
    # fixed axes extend beyond the rim; probe basis with its triangles
    rot_pair(sc, TH, (I0, J0, I1, J1), "θ", K0 + " (⊙)", "out", (-18, 30), L=L, Lf=3.5, arc_r=0.7,
             arc_lab=((20, 6), (-16, 14)), lab_offs=((30, 6), (-14, -12)))
    # rim point A (tip of i1) and the release point
    A = add(G, d(TH), R_)
    sc.dashed(add(G, d(TH), L), A)
    sc.mass(A, None, r=5, col="BLUE")
    sc.label(A, "A", "HEAD", "start", 17, dx=12, dy=10)
    # cord basis: e_r turned by phi from i1, e_t at T
    Tp = add(G, d(TH + PH), R_)
    sc.vec(G, add(G, d(TH + PH), L), ER, ORANGE, 2.8, name_off=off_dir(TH + PH, 16), size=17, head=11)
    sc.dashed(add(G, d(TH + PH), L), Tp)
    sc.mass(Tp, None, r=4.5, col="ACC")
    sc.label(Tp, "T", "HEAD", "middle", 17, dx=-20, dy=-10)
    ang_t = TH + PH + 90
    sc.vec(Tp, add(Tp, d(ang_t), 1.6), ET, ORANGE, 2.8, name_off=off_dir(ang_t, 16), size=17, head=11)
    sc.arc(G, 1.25, TH, TH + PH, "GREEN", 1.8, head=True)
    sc.label(add(G, d(TH + PH / 2), 1.25), "φ", "GREEN", "middle", 17, dx=8, dy=22)
    # point H on the rim at 135 deg from i1
    H = add(G, d(TH + 135.0), R_)
    sc.circle(H, 0.09, "HEAD", 1.8, fill="none")
    sc.label(H, "H", "HEAD", "middle", 17, dx=-14, dy=-8)
    # spin of the probe, counterclockwise, near the rim
    sc.spin(G, 2.6, 200.0, 300.0, "", "GREEN")
    sc.label(add(G, d(250.0), 2.0), "spin, rate of θ", "GREEN", "middle", 15, weight="700", dx=0, dy=-4)
    return sc


# ------------------------------------------------------------------------------------------------ rb20-involute
PHI = 1.22


def _P(phi, R=R_):
    return (R * (math.cos(phi) + phi * math.sin(phi)), R * (math.sin(phi) - phi * math.cos(phi)))


@figure("rb20-involute",
        "The probe frame with the right triangle GTP of the unwound cord, the involute traced by the mass and the two "
        "components of its velocity.",
        r"Taut cord tangent at $T$: $\mathbf r_0^P = R\,\mathbf e_r - R\phi\,\mathbf e_t$, with the right angle at $T$, legs "
        r"$R$ and $R\phi$; relative to the probe, $P$ moves on the involute of the rim.")
def involute():
    sc = Scene(860, 760, (290, 520), 68)
    G = (0.0, 0.0)
    er, et = d(math.degrees(PHI)), d(math.degrees(PHI) + 90)
    T = (R_ * er[0], R_ * er[1])
    P = _P(PHI)
    sc.poly(circle_pts(G, R_), "HEAD", 1.8, fill="EDGE", close=True, opacity=0.10)
    fixed_axis(sc, G, 0, 4.0, I1, off=(16, 6))
    fixed_axis(sc, G, 90, 3.6, J1, off=(16, 4))
    # triangle G-T-P
    triangle(sc, [G, T, P], ORANGE, 0.16)
    right_angle(sc, T, math.degrees(PHI) + 180, math.degrees(PHI) - 90, 0.14)
    sc.dashed(G, P)
    sc.line(T, P, "HEAD", 3.2)
    # wound cord (T to H) and unwound arc (A to T)
    H = d(135.0)
    sc.poly(circle_pts(G, R_, math.degrees(PHI), 135.0, 40), "HEAD", 3.4)
    sc.poly(circle_pts(G, R_ * 1.0, 0.0, math.degrees(PHI), 40), "GREEN", 2.0, "5 4")
    # involute
    sc.poly([_P(0.0 + 2.3 * i / 120) for i in range(121)], "EDGE", 1.8, "7 5")
    # points
    A = (R_, 0.0)
    sc.mass(A, None, r=5, col="BLUE")
    sc.label(A, "A", "HEAD", "start", 17, dx=12, dy=18)
    sc.mass(T, None, r=5, col="ACC")
    sc.label(T, "T", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.circle((R_ * H[0], R_ * H[1]), 0.08, "HEAD", 1.8)
    sc.label((R_ * H[0], R_ * H[1]), "H", "HEAD", "middle", 17, dx=-14, dy=-6)
    sc.mass(P, None, r=7, col="BLUE")
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=22)
    sc.note(P, "m/2", "TEXT", "start", 13, dx=12, dy=40)
    sc.label(G, "G", "HEAD", "start", 17, dx=14, dy=24)
    axis_out(sc, G, None, "HEAD")
    sc.label(G, K0 + " (⊙)", "HEAD", "end", 15, weight="700", dx=-14, dy=26)
    # e_r and e_t at T
    sc.vec(T, add(T, er, 0.9), ER, ORANGE, 2.8, name_off=(-6, -16), size=17, head=11)
    sc.vec(T, add(T, et, 0.9), ET, ORANGE, 2.8, name_off=(-18, -8), size=17, head=11)
    # labels of the legs
    mid_gt = (T[0] / 2, T[1] / 2)
    sc.label(mid_gt, "R", "TEXT", "end", 16, dx=-8, dy=-4)
    mid_tp = ((T[0] + P[0]) / 2, (T[1] + P[1]) / 2)
    sc.label(mid_tp, "R φ", "TEXT", "middle", 16, dx=-2, dy=26)
    mid_gp = (P[0] / 2, P[1] / 2)
    sc.label(mid_gp, "R√(1 + φ²)", "TEXT", "middle", 15, dx=4, dy=34)
    # arcs: unwound arc label
    sc.label((1.25, 1.2), "unwound arc R φ", "GREEN", "start", 13, dx=0, dy=0)
    sc.label(add(G, d(110.0), R_), "wound", "TEXT", "end", 14, italic=False, dx=-8, dy=-6)
    # velocity components at P
    sc.vec(P, add(P, er, 1.6), "R φ Ω " + ER, "BLUE", 2.8, name_off=(10, -12), size=15, head=11)
    sc.vec(P, add(P, et, 1.0), "R " + dot1("θ") + " " + ET, "BLUE", 2.8, name_off=(-6, 24), size=15, head=11)
    sc.note((-2.5, 6.5), "Ω: sum of the rates of θ and φ", "TEXT", "start", 13)
    sc.label(_P(2.1), "involute of the rim", "TEXT", "start", 14, italic=False, dx=14, dy=-4)
    return sc


# ------------------------------------------------------------------------------------------------ rb20-exploded
PE = math.radians(70.0)


@figure("rb20-exploded",
        "Exploded view of the probe and the two yo-yo masses with the equal and opposite cord tensions.",
        r"Exploded view: each cord pulls its mass towards $T$ with $T_c$ and the rim towards the mass with $T_c$; the two "
        r"forces on the probe cancel and their moment about $G$ is $-2RT_c\,\mathbf k_0$.")
def exploded():
    sc = Scene(960, 500, (480, 262), 62)
    G = (0.0, 0.0)
    er, et = d(70.0), d(160.0)
    T = (R_ * er[0], R_ * er[1])
    Tp = (-T[0], -T[1])
    P0 = _P(PHI)
    u = (P0[0] / math.hypot(*P0), P0[1] / math.hypot(*P0))
    Ps = (P0[0] + u[0], P0[1] + u[1])
    Pp = (-Ps[0], -Ps[1])
    sc.poly(circle_pts(G, R_), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.12)
    # cords, cut
    sc.line(T, Ps, "EDGE", 1.4, "7 5")
    sc.line(Tp, Pp, "EDGE", 1.4, "7 5")
    for a, b, sg in ((T, Ps, 1), (Tp, Pp, -1)):
        m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        n = (0.34, 0.94)
        sc.line(add(m, n, -0.12), add(m, n, 0.12), "EDGE", 1.6)
        sc.label(m, "pair", "TEXT", "middle", 13, italic=False, dx=0, dy=-14 * sg + (4 if sg < 0 else 0))
    # points
    for p, nm, o in ((T, "T", (-14, -10)), (Tp, "T'", (16, 20))):
        sc.mass(p, None, r=5, col="ACC")
        sc.label(p, nm, "HEAD", "middle", 17, dx=o[0], dy=o[1])
    for p, nm, o in ((Ps, "P", (14, -12)), (Pp, "P'", (-16, 22))):
        sc.mass(p, None, r=7, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=o[0], dy=o[1])
    # forces: cord on the probe at T (-Tc et) and at T' (+Tc et); on the masses (+Tc et at P, -Tc et at P')
    for p, sg, nm, dy, an in ((T, -1, "−", 28, "start"), (Tp, 1, "", -18, "end"), (Ps, 1, "", -18, "middle"),
                              (Pp, -1, "−", 28, "middle")):
        sc.vec(p, add(p, et, 1.5 * sg), None, "GREEN", 3.0, head=12)
        mid = add(p, et, 0.75 * sg)
        dx = {"start": -26, "end": 26, "middle": 0}[an]
        sc.label(mid, nm + S("T", "c") + " " + ET, "GREEN", an, 16, weight="700", dx=dx, dy=dy)
    # moment on the probe
    sc.spin(G, 0.9, 150.0, 30.0, "", "GREEN")
    axis_out(sc, G, None, "HEAD")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=24)
    sc.label(add(G, d(90.0), 0.9), S("M", "G") + " = −2 R " + S("T", "c") + " " + K0, "GREEN", "middle", 16, weight="700", dx=0,
             dy=-12)
    # small basis at T
    sc.vec(T, add(T, er, 0.7), ER, ORANGE, 2.4, name_off=(-8, -14), size=16, head=10)
    sc.vec(T, add(T, et, 0.7), ET, ORANGE, 2.4, name_off=(-14, -8), size=16, head=10)
    sc.note((0.0, -R_ - 0.65), "no gravity", "TEXT", "middle", 14)
    return sc


# ------------------------------------------------------------------------------------------------ rb20-graph
KK = 0.5


def spin_ratio(x):
    return (1.0 - KK * x * x) / (1.0 + KK * x * x)


def tension(x):
    return 2.0 * KK * x / (1.0 + KK * x * x) ** 2


@figure("rb20-graph",
        "Spin of the probe and tension of a cord against time for K equal to one half.",
        r"Part (a) and part (c) for $K = 0.5$: the spin falls from $\omega_0$ and changes sign at $\omega_0 t = 1/\sqrt K$; "
        r"the tension starts at zero and peaks at $\omega_0 t = 1/\sqrt{3K}$. The curves stop being valid when the cords "
        r"are released, at $t_f$.")
def graph():
    sx, sy = 250.0, 330.0
    sc = Scene(980, 740, (120, 60 + sy * 1.0), 1.0)

    def Q(x, y):
        return (x * sx, y * sy)
    ymin, ymax, xmax = -0.8, 1.0, 3.0
    # frame: left axis, bottom axis, grey zero line
    sc.vec(Q(0, ymin), Q(0, ymax + 0.08), None, "EDGE", 1.6, head=9)
    sc.vec(Q(0, ymin), Q(xmax + 0.1, ymin), None, "EDGE", 1.6, head=9)
    sc.line(Q(0, 0), Q(xmax, 0), "EDGE", 1.4)
    for t in (0.5, 1, 1.5, 2, 2.5, 3):
        sc.line(Q(t, ymin), Q(t, ymin + 0.015), "EDGE", 1.2)
        sc.label(Q(t, ymin), f"{t:g}", "TEXT", "middle", 14, italic=False, dy=22)
    for v in (-0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6, 0.8, 1.0):
        sc.line(Q(0, v), Q(xmax, v), "EDGE", 0.6, "2 4")
        sc.label(Q(0, v), f"{v:.1f}".replace("-", "−"), "TEXT", "end", 14, italic=False, dx=-8, dy=5)
    sc.label(Q(0, 0), "0", "TEXT", "end", 14, italic=False, dx=-8, dy=5)
    sc.label(Q(xmax, ymin), S("ω", "0") + " t", "TEXT", "end", 17, dy=46)
    sc.label(Q(0, ymax + 0.08), "ratio", "TEXT", "start", 17, dx=12, dy=-6)
    xs = [xmax * i / 240 for i in range(241)]
    sc.poly([Q(x, spin_ratio(x)) for x in xs], "BLUE", 3.4)
    sc.poly([Q(x, tension(x)) for x in xs], ORANGE, 3.4)
    # check points
    for x in (0.5, 1.0, 2.0, 3.0):
        sc.mass(Q(x, spin_ratio(x)), None, r=3.2, col="BLUE")
        sc.mass(Q(x, tension(x)), None, r=3.2, col="ACC")
    # spin zero and tension maximum
    xz = 1.0 / math.sqrt(KK)
    sc.mass(Q(xz, 0), None, r=5.5, col="BLUE")
    sc.dashed(Q(xz, 0), Q(xz, ymin))
    sc.label(Q(xz, 0), "spin zero, x = 1/√K", "BLUE", "end", 16, weight="700", dx=-10, dy=26)
    xm = 1.0 / math.sqrt(3.0 * KK)
    tm = tension(xm)
    sc.mass(Q(xm, tm), None, r=5.5, col="ACC")
    sc.dashed(Q(xm, tm), Q(xm, 0.93))
    sc.label(Q(xm, 0.93), "maximum, x = 1/√(3K), value 0.459", ORANGE, "start", 16, weight="700", dx=10, dy=-4)
    # legend
    lx, ly = 2.0, 0.78
    sc.line(Q(lx, ly), Q(lx + 0.18, ly), "BLUE", 3.4)
    sc.label(Q(lx + 0.18, ly), S("ω", "") + "/" + S("ω", "0"), "BLUE", "start", 16, dx=10, dy=5)
    sc.line(Q(lx, ly - 0.1), Q(lx + 0.18, ly - 0.1), ORANGE, 3.4)
    sc.label(Q(lx + 0.18, ly - 0.1), S("T", "c") + " R / (I " + S("ω", "0") + "<tspan baseline-shift=\"super\" font-size=\"70%\">2</tspan>)", ORANGE, "start", 16, dx=10, dy=5)
    return sc
