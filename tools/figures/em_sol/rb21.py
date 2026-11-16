"""Problem RB-21: reaction wheel spacecraft (rod with two wheels; azimuth theta, elevation phi, wheel rates)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb17 import off_dir, rod_box, rot_pair
from figures.mech import S, Scene, bold, dot1

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
IP, JP = I + "'", J + "'"
IB, KB, JB = S(I, "b"), S(K, "b"), S(J, "b")
TH, PH = 30.0, 45.0
ROD, RW = 6.0, 0.9


def sub(t):
    return '<tspan baseline-shift="sub" font-size="70%">' + t + "</tspan>"


# ------------------------------------------------------------------------------------------------ rb21-rot-theta
@figure("rb21-rot-theta",
        "View from above of the azimuth rotation by theta about the vertical k0, with the horizontal projection of the "
        "rod along i'.",
        r"Rotation about $\mathbf k_0$ (⊙) by $\theta$: $\mathbf i' = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0$ is "
        r"the horizontal direction under the rod; $\mathbf j' = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$.")
def rot_theta():
    sc = Scene(900, 560, (450, 290), 120)
    G = (0.0, 0.0)
    u = d(TH)
    e1, e2 = add(G, u, 2.5), add(G, u, -2.5)
    sc.line(e2, e1, "HEAD", 4.0, "9 6")
    rot_pair(sc, TH, (I0, J0, IP, JP), "θ", "G, " + K0 + " (⊙)", "out", (14, 40), L=1.2, Lf=1.9, arc_r=0.85,
             inner2=True, lab_offs=((-16, -14), None), out_anchor="start")
    for p, nm, o in ((e1, "G" + sub("1") + " (projected)", (12, -10)), (e2, "G" + sub("2") + " (projected)", (-12, 26))):
        sc.circle(p, 0.07, "HEAD", 2.0)
        sc.label(p, nm, "HEAD", "start" if p is e1 else "end", 16, dx=o[0], dy=o[1])
    sc.label(add(G, u, 1.95), "projection of the rod", "TEXT", "start", 14, italic=False, dx=20, dy=30)
    return sc


# ------------------------------------------------------------------------------------------------ rb21-rot-phi
def _wheel(sc, c, ang, name, nm_off, nm_anchor="start"):
    rod_box(sc, c, ang + 90.0, RW, 11)
    sc.mass(c, None, r=4.5, col="BLUE")
    sc.label(c, name, "HEAD", nm_anchor, 17, dx=nm_off[0], dy=nm_off[1])


@figure("rb21-rot-phi",
        "Vertical plane of the rod with the elevation phi from the horizontal projection, the spacecraft basis i_b, k_b "
        "and the two wheels at the ends.",
        r"Elevation by $\varphi$ about $-\mathbf j'$ (⊗ for $\mathbf j'$): $\mathbf i_b = \cos\varphi\,\mathbf i' + "
        r"\sin\varphi\,\mathbf k_0$, $\mathbf k_b = -\sin\varphi\,\mathbf i' + \cos\varphi\,\mathbf k_0$. The sense of "
        r"$\varphi$ (elevation above the plane $Gxy$) is read from the statement figure.")
def rot_phi():
    sc = Scene(900, 800, (450, 420), 100)
    G = (0.0, 0.0)
    ub = d(PH)
    G1, G2 = add(G, ub, ROD / 2), add(G, ub, -ROD / 2)
    # horizontal plane, rod and wheels
    sc.line((-3.6, 0.0), (1.9, 0.0), "EDGE", 1.2, "8 5")
    sc.line((2.35, 0.0), (3.6, 0.0), "EDGE", 1.2, "8 5")
    sc.label((-3.6, 0.0), "horizontal plane", "TEXT", "start", 14, italic=False, dx=0, dy=-12)
    _wheel(sc, G1, PH, "w" + sub("1") + " (" + "G" + sub("1") + ")", (16, -14))
    _wheel(sc, G2, PH, "w" + sub("2") + " (" + "G" + sub("2") + ")", (-16, 28), "end")
    sc.line(G2, G1, "HEAD", 5.0)
    rot_pair(sc, PH, (IP, K0, IB, KB), "φ", "G, " + JP + " (⊗)", "in", (-20, 30), L=1.3, Lf=1.9, arc_r=0.85,
             inner2=True, lab_offs=((24, 2), (-14, -10)))
    sc.note((0.2, -1.2), "rotation about −" + JB + " (out of the paper), counterclockwise as seen", "TEXT", "start", 13)
    return sc


# ------------------------------------------------------------------------------------------------ rb21-exploded
def _ellipse_arc(sc, c, a_dir, rx, ry, t0, t1, col, n=40):
    """Half-turn about the axis along a_dir (degrees) seen in perspective: an ellipse with the minor axis along the axis."""
    ca, sa = math.cos(math.radians(a_dir)), math.sin(math.radians(a_dir))
    pts = []
    for i in range(n + 1):
        t = math.radians(t0 + (t1 - t0) * i / n)
        u, v = rx * math.cos(t), ry * math.sin(t)      # u along the minor axis (the rotation axis), v along the major
        pts.append((c[0] + u * ca - v * sa, c[1] + u * sa + v * ca))
    sc.poly(pts, col, 1.9)
    p, q = pts[-2], pts[-1]
    sc.vec(p, q, None, col, 1.9, head=10)


@figure("rb21-exploded",
        "Exploded view of the spacecraft rod and the two reaction wheels with the axle forces and torques as equal and "
        "opposite pairs.",
        r"Exploded view: the axle of wheel $i$ acts on the wheel with $\mathbf F_i$, $\mathbf Q_i$ and on the rod with "
        r"$-\mathbf F_i$, $-\mathbf Q_i$. No external load acts, so the sum of the equations of the three bodies keeps $G$ "
        r"at rest and $\mathbf H_G$ constant.")
def exploded():
    sc = Scene(1000, 880, (500, 440), 84)
    G = (0.0, 0.0)
    ub = d(PH)
    G1, G2 = add(G, ub, ROD / 2), add(G, ub, -ROD / 2)
    W1, W2 = add(G1, ub, 1.5), add(G2, ub, -1.5)
    # rod alone, with the centre-of-mass symbol at G
    sc.line(G2, G1, "HEAD", 5.0)
    x, y = sc.P(G)
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="none" stroke="HEAD" stroke-width="1.8"/>')
    sc.c.add(f'<path d="M{x:.1f},{y - 8:.1f} L{x:.1f},{y + 8:.1f} M{x - 8:.1f},{y:.1f} L{x + 8:.1f},{y:.1f}" stroke="HEAD" stroke-width="1.4"/>')
    sc.label(G, "G", "HEAD", "start", 17, dx=14, dy=26)
    sc.note((-0.9, 0.35), "ROD", "HEAD", "start", 15, dx=-14, dy=-14)
    # the loads are unknown internal ones: arbitrary directions in the plane (wheel 2 is the half-turn image of wheel 1)
    for sg, Gp, Wp, nm in ((1, G1, W1, "1"), (-1, G2, W2, "2")):
        fa = 160.0 if sg > 0 else 340.0                      # direction of F_i on the wheel
        qa0, qa1 = (330.0, 440.0) if sg > 0 else (150.0, 260.0)    # arc of Q_i on the wheel
        ra0, ra1 = (100.0, 200.0) if sg > 0 else (280.0, 380.0)    # arc of -Q_i on the rod
        # on the rod: -F_i, -Q_i
        sc.mass(Gp, None, r=4.5, col="BLUE")
        sc.vec(Gp, add(Gp, d(fa + 180.0), 1.2), None, ORANGE, 3.0, head=12)
        sc.label(add(Gp, d(fa + 180.0), 1.2), "−" + S("F", nm), ORANGE, "middle", 17, weight="700", dx=(18 if sg > 0 else -18),
                 dy=(14 if sg > 0 else -6))
        sc.spin(Gp, 0.5, ra0, ra1, "", ORANGE)
        sc.label(add(Gp, d((ra0 + ra1) / 2), 0.5), "−" + S("Q", nm), ORANGE, "middle", 16, weight="700",
                 dx=(-18 if sg > 0 else 18), dy=(-6 if sg > 0 else 16))
        # wheel i alone: F_i, Q_i, the spin about i_b
        rod_box(sc, Wp, PH + 90.0, RW, 11)
        sc.mass(Wp, None, r=4.5, col="BLUE")
        sc.vec(Wp, add(Wp, d(fa), 1.2), None, ORANGE, 3.0, head=12)
        sc.label(add(Wp, d(fa), 1.2), S("F", nm), ORANGE, "middle", 17, weight="700", dx=(-18 if sg > 0 else 18),
                 dy=(-6 if sg > 0 else 16))
        sc.spin(Wp, 0.42, qa0, qa1, "", ORANGE)
        sc.label(add(Wp, d((qa0 + qa1) / 2 + 20 * sg), 0.42), S("Q", nm), ORANGE, "middle", 16, weight="700",
                 dx=(18 if sg > 0 else -18), dy=(-10 if sg > 0 else 18))
        sc.dashed(Gp, Wp)
        _ellipse_arc(sc, add(Wp, ub, 0.8 * sg), PH, 0.14, 0.62, -110.0, 120.0, "BLUE")
        sc.label(add(Wp, ub, 1.5 * sg), "rate of " + S("φ", nm), "BLUE", "start" if sg > 0 else "end", 15, weight="700",
                 dx=(12 if sg > 0 else -12), dy=(-4 if sg > 0 else 14))
        sc.label(Gp, "G" + sub(nm), "HEAD", "middle", 16, dx=(8 if sg > 0 else 0), dy=(30 if sg > 0 else -20))
        low = add(Wp, d(PH - 90.0 if sg > 0 else PH + 90.0), RW)
        sc.note(low, "WHEEL " + nm + " (centre G" + sub(nm) + ")", "HEAD", "start" if sg > 0 else "end", 15, dx=(16 if sg > 0 else -16), dy=(8 if sg > 0 else 2))
        sc.note(low, S("Q", nm) + " · " + IB + " = motor torque", "TEXT", "start" if sg > 0 else "end", 13, dx=(16 if sg > 0 else -16),
                dy=(30 if sg > 0 else 24))
    sc.note((0.0, -4.55), "no external loads (deep space)", "TEXT", "middle", 14)
    b0 = (3.4, -2.2)
    sc.vec(b0, add(b0, ub, 0.9), IB, "BLUE", 2.6, name_off=off_dir(PH, 16), size=16, head=10)
    sc.vec(b0, add(b0, d(PH + 90.0), 0.9), KB, "BLUE", 2.6, name_off=off_dir(PH + 90.0, 16), size=16, head=10)
    axis_in(sc, b0, None, "HEAD")
    sc.label(b0, JB + " (⊗)", "HEAD", "end", 16, weight="700", dx=-16, dy=-8)
    return sc
