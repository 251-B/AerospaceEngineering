"""Problem RB-32: rate gyro on an aircraft (gimbal turning by theta about i_a = i_b, disk spinning by phi about j_b = j_d).

Figures: the gimbal rotation (theta about i_a), the spin of the disk (phi about j_b) and the exploded view of the disk,
the massless gimbal and the aircraft posts with the force and moment pairs, the spring and the damper.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb17 import rod_box, rot_pair
from figures.em_sol.rb23 import circle_pts
from figures.em_sol.rb30 import left_lab
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
IA, JA, KA = S(I, "a"), S(J, "a"), S(K, "a")
IB, JB, KB = S(I, "b"), S(J, "b"), S(K, "b")
ID, JD, KD = S(I, "d"), S(J, "d"), S(K, "d")
FBD, MBD = S(bold("F"), "bd"), S(bold("M"), "bd")
FAB, MAB = S(bold("F"), "ab"), S(bold("M"), "ab")


# ------------------------------------------------------------------------------------------------ rb32-rot-theta
@figure("rb32-rot-theta",
        "Gimbal rotation: the gimbal basis turned by theta about the gimbal axis i_a, which points out of the paper; the "
        "spin axle j_b is lifted towards k_a.",
        r"Rotation of the gimbal by $\theta$ about $\mathbf i_a = \mathbf i_b$ (⊙): $\mathbf j_b = \cos\theta\,\mathbf j_a + "
        r"\sin\theta\,\mathbf k_a$, $\mathbf k_b = -\sin\theta\,\mathbf j_a + \cos\theta\,\mathbf k_a$. Read from the "
        r"statement figure: the spin axle is the middle bar of the gimbal, along $\mathbf j_b$.")
def rot_theta():
    th = 25.0
    sc = Scene(900, 700, (360, 420), 140)
    O = (0.0, 0.0)
    # the disk edge-on (its plane holds i_b and k_b) and the spin axle along j_b, drawn under the vectors
    rod_box(sc, O, 90 + th, 1.45, 9)
    sc.line(O, add(O, d(th), 2.55), "HEAD", 1.8)
    rot_pair(sc, th, (JA, KA, JB, KB), "θ", IA + " = " + IB + " (⊙), gimbal axis", "out", (-14, 30), L=1.9, Lf=2.6,
             arc_r=0.6, arc_lab=((20, 12), left_lab(th, 0.6, 140, 26.0)), lab_offs=((24, 4), (-22, -8)))
    sc.label(add(O, d(th), 2.55), "spin axle " + JB + " = " + JD, "HEAD", "start", 15, dx=12, dy=-4)
    sc.label(add(O, d(90 + th + 180), 1.45), "disk (edge-on)", "TEXT", "end", 14, dx=-12, dy=12)
    # restoring turn about the axis: clockwise arc with its arrowhead, on the free side of the view
    sc.arc(O, 0.45, 170, 130, "PINK", 2.0, head=True)
    sc.label((-0.5, 0.45), "spring −kθ, damper −λθ̇", "PINK", "end", 14, dx=-10, dy=0)
    sc.label((-0.5, 0.45), "restoring, clockwise about " + IA, "PINK", "end", 14, dx=-10, dy=18)
    return sc


# ------------------------------------------------------------------------------------------------ rb32-rot-phi
@figure("rb32-rot-phi",
        "Spin of the disk: the disk basis turned by phi about the spin axle j_b, which points out of the paper.",
        r"Spin of the disk by $\phi$ about $\mathbf j_b = \mathbf j_d$ (⊙, with $\mathbf k_b$ to the right and $\mathbf i_b$ "
        r"up): $\mathbf i_d = \cos\phi\,\mathbf i_b - \sin\phi\,\mathbf k_b$, $\mathbf k_d = \sin\phi\,\mathbf i_b + "
        r"\cos\phi\,\mathbf k_b$.")
def rot_phi():
    sc = Scene(900, 790, (410, 440), 140)
    O = (0.0, 0.0)
    sc.poly(circle_pts(O, 2.2), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.14)
    sc.label(add(O, d(-52), 2.2), "disk", "TEXT", "start", 15, dx=-30, dy=-16)
    rot_pair(sc, 30.0, (KB, IB, KD, ID), "φ", JB + " = " + JD + " (⊙), spin axle", "out", (-14, 30), L=1.9, Lf=2.9,
             arc_r=0.6, col="GREEN", arc_lab=((20, 12), left_lab(30.0, 0.6, 140)), lab_offs=((24, 4), (-22, -8)))
    sc.note((-2.75, 2.85), KB + " × " + IB + " = " + JB + " (right-handed view)", "TEXT", "start", 14)
    return sc


# ------------------------------------------------------------------------------------------------ rb32-exploded
CAB = (0.55, 0.38)                       # oblique axes: i_a to the right, k_a up, j_a into the depth (up and right)
TH = math.radians(25.0)
JBV = (0.0, math.cos(TH), math.sin(TH))
KBV = (0.0, -math.sin(TH), math.cos(TH))
IBV = (1.0, 0.0, 0.0)


def pr(x, y=None, z=None):
    """Oblique projection of the components (i_a, j_a, k_a)."""
    if y is None:
        x, y, z = x
    return (x + CAB[0] * y, z + CAB[1] * y)


def comb(*terms):
    """Linear combination of 3D vectors: comb((a, v), (b, w)) = a v + b w."""
    return tuple(sum(c * v[i] for c, v in terms) for i in range(3))


def plus(a, b, k=1.0):
    return (a[0] + k * b[0], a[1] + k * b[1], a[2] + k * b[2])


def dbl(sc, p, v, col, name=None, off=(10, -8), anchor="middle", size=15):
    """Torque: arrow with two heads along the 3D vector v from the 3D point p."""
    a, b = pr(p), pr(plus(p, v))
    sc.vec(a, b, None, col, 2.6, head=11)
    ux, uy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(ux, uy)
    q = (b[0] - 0.22 * ux / n, b[1] - 0.22 * uy / n)
    arrow_head(sc.c, sc.P(a), sc.P(q), col, 11)
    if name:
        sc.label(b, name, col, anchor, size, weight="700", dx=off[0], dy=off[1])
    return b


def frc(sc, p, v, col, name=None, off=(10, -8), anchor="middle", size=16, w=3.0):
    a, b = pr(p), pr(plus(p, v))
    sc.vec(a, b, None, col, w, head=12)
    if name:
        sc.label(b, name, col, anchor, size, weight="700", dx=off[0], dy=off[1])
    return b


def arc3(sc, c, u, v, r, t0, t1, col, name=None, lab_t=None, off=(10, 0), anchor="start", size=14):
    """Arc of the circle of centre c in the plane of u and v (3D), from t0 to t1 degrees, with an arrowhead.

    The label sits on the arc at the angle lab_t (default: the end)."""
    n = 60
    pts = []
    for i in range(n + 1):
        t = math.radians(t0 + (t1 - t0) * i / n)
        pts.append(pr(plus(c, comb((r * math.cos(t), u), (r * math.sin(t), v)))))
    sc.poly(pts, col, 2.2)
    arrow_head(sc.c, sc.P(pts[-4]), sc.P(pts[-1]), col, 11)
    if name:
        lt = math.radians(t1 if lab_t is None else lab_t)
        sc.label(pr(plus(c, comb((r * math.cos(lt), u), (r * math.sin(lt), v)))), name, col, anchor, size, weight="700",
                 dx=off[0], dy=off[1])


@figure("rb32-exploded",
        "Exploded view of the disk, the massless gimbal and the aircraft posts, with the spin-axle force and moment pair, the "
        "gimbal-bearing force and moment pair, the spring and damper torques about the gimbal axis and the weight of the disk.",
        r"Exploded view: the spin axle carries no moment along $\mathbf j_b$ and the gimbal bearings none along "
        r"$\mathbf i_b$; about the gimbal axis only the spring $-k\theta\,\mathbf i_b$ and the damper "
        r"$-\lambda\dot\theta\,\mathbf i_b$ act, and the massless gimbal passes them to the disk.")
def exploded():
    sc = Scene(1040, 930, (490, 370), 115)
    R, WX, WY = 0.9, 1.9, 1.3             # disk radius, half width of the gimbal frame, half length along j_b
    BX = WX + 0.5                          # the bearings sit on the gimbal axis just outside the frame
    G = (0.0, 0.0, 0.0)
    Gd = comb((2.7, JBV))                  # the disk pulled out along +j_b
    DROP = 1.5                             # the posts and their bearings pulled down along -k_a
    BL, BR = (-BX, 0.0, 0.0), (BX, 0.0, 0.0)
    PL, PR = (-BX, 0.0, -DROP), (BX, 0.0, -DROP)
    FL = -4.0                              # floor level (k_a)
    # ---- floor, posts
    fl = [pr(-3.4, -1.0, FL), pr(3.4, -1.0, FL), pr(3.4, 1.6, FL), pr(-3.4, 1.6, FL)]
    sc.poly(fl, "HEAD", 1.6, fill="EDGE", close=True, opacity=0.18)
    for P0 in (PL, PR):
        sc.line(pr(P0), pr(P0[0], 0.0, FL), "HEAD", 4.0)
    sc.label(pr(-BX, 0.0, -2.9), "aircraft posts", "TEXT", "end", 14, dx=-12, dy=4)
    # ---- gimbal frame: rectangle of i_b and j_b, gimbal axis (with the two bearing stubs) and spin axle bars
    corners = [comb((s, IBV), (t, JBV)) for s, t in ((-WX, -WY), (WX, -WY), (WX, WY), (-WX, WY))]
    sc.poly([pr(c) for c in corners], "HEAD", 2.2, close=True)
    sc.line(pr(BL), pr(BR), "HEAD", 3.2)
    sc.line(pr(comb((-WY, JBV))), pr(comb((WY, JBV))), "HEAD", 3.2)
    sc.label(pr(comb((-WY, JBV), (-WX, IBV))), "gimbal (massless)", "TEXT", "end", 14, dx=-4, dy=22)
    # ---- disk, pulled out along +j_b (a circle in the plane of i_b and k_b)
    disk = [pr(plus(Gd, comb((R * math.cos(math.radians(t)), IBV), (R * math.sin(math.radians(t)), KBV))))
            for t in range(0, 361, 6)]
    sc.poly(disk, "HEAD", 2.0, fill="EDGE", close=True, opacity=0.35)
    sc.label(pr(comb((1.0, Gd), (-R, IBV))), "disk d", "TEXT", "end", 14, dx=-12, dy=26)
    # ---- dashed links of the action-reaction pairs
    sc.line(pr(G), pr(Gd), "EDGE", 1.3, "6 5")
    sc.line(pr(BL), pr(PL), "EDGE", 1.3, "6 5")
    sc.line(pr(BR), pr(PR), "EDGE", 1.3, "6 5")
    # ---- bearings and centres
    for p in (BL, BR, PL, PR):
        x, y = sc.P(pr(p))
        sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="none" stroke="HEAD" stroke-width="2"/>')
    for p, nm, off in ((G, "G", (-14, -12)), (Gd, "G (disk)", (-16, 20))):
        sc.mass(pr(p), None, r=4.5, col="BLUE")
        sc.label(pr(p), nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    # ---- disk alone: F_bd, M_bd (normal to the axle), weight
    fdir = (0.7, 0.2, 0.75)
    frc(sc, Gd, fdir, "GREEN", FBD, off=(18, -6))
    mdir = comb((-1.0, IBV), (0.8, KBV))
    dbl(sc, Gd, mdir, "GREEN", MBD + " = −(kθ + λθ̇) " + IB + " + M" + S("", "3") + " " + KB, off=(-8, -24), anchor="end")
    sc.label(pr(plus(Gd, mdir)), "none along " + JB, "GREEN", "end", 14, weight="700", dx=-8, dy=-6)
    frc(sc, Gd, (0.0, 0.0, -0.8), "PINK", "m" + S("", "d") + " g", off=(12, 18), anchor="start")
    # ---- gimbal alone: -F_bd, -M_bd at G; F_ab and M_ab at the left bearing; spring and damper at the right bearing
    frc(sc, G, tuple(-0.8 * c for c in fdir), ORANGE, "−" + FBD, off=(-8, 10), anchor="end")
    dbl(sc, G, tuple(-0.85 * c for c in mdir), ORANGE, "−" + MBD, off=(20, 22), anchor="start")
    frc(sc, BL, (-0.9, -0.2, -0.5), "GREEN", FAB, off=(-8, 20), anchor="end")
    dbl(sc, BL, comb((1.2, KBV)), "GREEN", MAB + " = M" + S("", "3") + " " + KB, off=(-10, -22), anchor="end")
    sc.label(pr(plus(BL, comb((1.2, KBV)))), "none along " + IB, "GREEN", "end", 14, weight="700", dx=-10, dy=-4)
    arc3(sc, BR, JBV, KBV, 0.38, 240, -60, "PINK", "spring −kθ " + IB, lab_t=-60, off=(14, 18))
    arc3(sc, BR, JBV, KBV, 0.65, 240, -60, "PINK", "damper −λθ̇ " + IB, lab_t=25, off=(10, -8))
    # ---- posts alone: -F_ab, -M_ab, +k theta i_b, +lambda theta-dot i_b
    frc(sc, PL, (0.6, 0.2, 0.3), ORANGE, "−" + FAB, off=(10, 24), anchor="start")
    dbl(sc, PL, comb((-1.2, KBV)), ORANGE, "−" + MAB, off=(12, 16), anchor="start")
    arc3(sc, PR, JBV, KBV, 0.38, -60, 240, ORANGE, "spring +kθ " + IB, lab_t=-60, off=(14, 18))
    arc3(sc, PR, JBV, KBV, 0.65, -60, 240, ORANGE, "damper +λθ̇ " + IB, lab_t=25, off=(10, -8))
    # ---- bases: blue at G, grey on the floor; yaw rate beside the floor
    for v, nm, off in ((IBV, IB, (16, -10)), (JBV, JB, (16, 14)), (KBV, KB, (-10, -10))):
        a, b = pr(G), pr(comb((0.8, v)))
        sc.vec(a, b, nm, "BLUE", 2.6, name_off=off, size=16, head=10)
    o3 = (1.9, -0.6, FL)
    o = pr(o3)
    for v, nm, off in (((1, 0, 0), IA, (14, 6)), ((0, 1, 0), JA, (12, -8)), ((0, 0, 1), KA, (-10, -8))):
        sc.vec(o, pr(plus(o3, v, 0.9)), nm, "EDGE", 2.2, name_off=off, size=16, head=9)
    sc.vec(pr(-3.7, 0.0, FL), pr(-3.7, 0.0, FL + 1.6), "Ω(t)", "PINK", 2.6, name_off=(26, 8), size=17, head=11)
    return sc
