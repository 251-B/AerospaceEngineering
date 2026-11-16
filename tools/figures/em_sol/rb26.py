"""Problem RB-26: unbalanced planetary bearings (disk D, three bearings A, B, C inside a fixed cavity).

Figures: polar basis of the bearings with the three centres, the rolling of one bearing (velocity distribution across its
diameter) and the exploded view with the contact forces.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb23 import circle_pts, rim_hatch
from figures.mech import S, Scene, bold, dot1

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
ER, ET = S(bold("e"), "r"), S(bold("e"), "θ")
THETA = 30.0


def pol(a, r, lat=0.0):
    """World point at the polar angle a (deg), radius r along e_r and lat along e_theta."""
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    return (r * c - lat * s, r * s + lat * c)


# ------------------------------------------------------------------------------------------------ rb26-polar-basis
@figure("rb26-polar-basis",
        "Plane of the cavity with the polar basis e_r, e_theta of bearing A turned by theta about k, and the positions of "
        "the three bearing centres.",
        r"Rotation about $\mathbf k$ (⊙) by $\theta$: $\mathbf e_r = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j$, "
        r"$\mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j$. The centres of $B$ and $C$ are $45^\circ$ "
        r"on either side of the prolongation of $AO$ (reading of the statement figure).")
def polar_basis():
    sc = Scene(900, 880, (450, 440), 62)
    O = (0.0, 0.0)
    Rc, L = 5.0, 2.4
    th = THETA
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    # circle of the bearing centres
    sc.poly(circle_pts(O, Rc), "EDGE", 1.3, "7 5", close=True)
    sc.label(pol(-40, Rc), "path of the bearing centres", "TEXT", "start", 14, italic=False, dx=14, dy=26)
    # fixed axes
    fixed_axis(sc, O, 0, 6.0, I, off=(14, 6))
    fixed_axis(sc, O, 90, 6.0, J, off=(12, 4))
    # points A, B, C and the dashed segments
    A, B, C = pol(th, Rc), pol(th + 135, Rc), pol(th + 225, Rc)
    sc.line(O, A, "EDGE", 1.6)
    sc.dashed(O, B)
    sc.dashed(O, C)
    sc.dashed(O, pol(th + 180, Rc))
    sc.label(pol(th + 180, Rc), "prolongation of AO", "TEXT", "end", 14, italic=False, dx=-4, dy=20)
    for p, nm, off in ((A, "A", (14, -10)), (B, "B", (-14, -8)), (C, "C", (-14, 18))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 18, dx=off[0], dy=off[1])
    # the two 45 degree arcs between the prolongation and OB, OC
    sc.arc(O, 2.3, th + 135, th + 180, "GREEN", 1.5)
    sc.arc(O, 2.3, th + 180, th + 225, "GREEN", 1.5)
    sc.label(pol(th + 157.5, 2.3), "45°", "GREEN", "middle", 15, dx=-22, dy=-4)
    sc.label(pol(th + 202.5, 2.3), "45°", "GREEN", "middle", 15, dx=-8, dy=24)
    # triangles of the basis at O
    f1, t1 = (L * c, 0.0), pol(th, L)
    triangle(sc, [O, f1, t1], ORANGE, 0.20)
    sc.dashed(f1, t1)
    right_angle(sc, f1, 180, 90, 0.08)
    f2, t2 = (0.0, L * c), (-L * s, L * c)
    triangle(sc, [O, f2, t2], ORANGE, 0.20)
    sc.dashed(f2, t2)
    right_angle(sc, f2, 270, 0, 0.08)
    sc.label((L * c / 2, 0.0), "cos θ", "TEXT", "middle", 15, dy=24)
    sc.label((L * c, L * s / 2), "sin θ", "TEXT", "start", 15, dx=10, dy=6)
    sc.label((0.0, L * c / 2), "cos θ", "TEXT", "start", 15, dx=10, dy=6)
    sc.label((-L * s / 2, L * c), "−sin θ", "TEXT", "middle", 15, dy=-10)
    unit(sc, O, th, L, ER, "BLUE", off=(-6, -14))
    unit(sc, O, th + 90, L, ET, "BLUE", off=(-10, -12))
    # arcs of theta at O: i to e_r (small radius), j to e_theta, and i to OA (large radius)
    sc.arc(O, 0.9, 0, th, "GREEN", 1.7, head=True)
    sc.arc(O, 0.9, 90, 90 + th, "GREEN", 1.7, head=True)
    sc.label(pol(th / 2, 1.25), "θ", "GREEN", "middle", 17, dx=4, dy=-2)
    sc.label(pol(90 + th / 2, 0.9), "θ", "GREEN", "middle", 17, dx=-14, dy=-8)
    sc.arc(O, 3.3, 0, th, "GREEN", 1.7, head=True)
    sc.label(pol(th / 2, 3.3), "θ", "GREEN", "middle", 17, dx=16, dy=12)
    # the basis at A
    unit(sc, A, th, 1.5, ER, "BLUE", off=(10, 24))
    unit(sc, A, th + 90, 1.5, ET, "BLUE", off=(-8, -12))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-14, dy=22)
    sc.label(O, K + " (⊙)", "HEAD", "end", 16, weight="700", dx=-18, dy=50)
    return sc


# ------------------------------------------------------------------------------------------------ rb26-rolling
@figure("rb26-rolling",
        "Bearing A between the disk and the fixed cavity with the linear velocity distribution across its diameter, zero "
        "at the cavity contact.",
        r"Rolling of bearing $A$: zero velocity at the cavity contact $Q_A$ gives $\omega_A = -5\dot\theta$; the equal "
        r"velocities at $P_A$ give $\omega_D = \tfrac52\dot\theta$.")
def rolling():
    sc = Scene(820, 740, (400, 420), 78)
    A = (0.0, 0.0)
    Cc = (-5.0, 0.0)                                  # centre O of the disk and the cavity, off the drawing
    PA, QA = (-1.0, 0.0), (1.0, 0.0)
    # disk rim (radius d = 4) and cavity wall (radius 3d/2 = 6), short arcs
    rim = [(Cc[0] + 4 * math.cos(math.radians(a)), Cc[1] + 4 * math.sin(math.radians(a))) for a in range(-26, 27, 2)]
    sc.poly(rim, "HEAD", 2.2)
    wall = [(Cc[0] + 6 * math.cos(math.radians(a)), Cc[1] + 6 * math.sin(math.radians(a))) for a in range(-18, 19, 2)]
    sc.poly(wall, "HEAD", 2.2)
    rim_hatch(sc, Cc, 6.0, -18, 18, inward=False, step=2.0, length=0.22)
    sc.label((-1.9, -1.55), "disk D", "TEXT", "end", 16, italic=False, dx=-6, dy=0)
    sc.label((1.9, -1.55), "cavity, fixed", "TEXT", "start", 16, italic=False, dx=6, dy=0)
    # bearing
    sc.circle(A, 1.0, "HEAD", 2.0, fill="EDGE", opacity=0.12)
    for p, nm, off in ((A, "A", (-4, 6)), ):
        sc.mass(p, None, r=3.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=18, dy=-4)
    sc.mass(PA, None, r=4.5, col="BLUE")
    sc.label(PA, S("P", "A"), "HEAD", "end", 17, dx=-10, dy=22)
    sc.circle(QA, 0.0, "HEAD", 1.0)
    x, y = sc.P(QA)
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="none" stroke="HEAD" stroke-width="1.9"/>')
    sc.label(QA, S("Q", "A"), "HEAD", "start", 17, dx=26, dy=30)
    sc.label(QA, "v = 0", "GREEN", "start", 16, weight="700", dx=36, dy=-6)
    # velocities (scale 0.4): v_A = 5 -> 2 units, v_P = 10 -> 4 units
    sc.vec(A, (0.0, 2.0), None, "GREEN", 3.0, head=12)
    sc.label((0.0, 2.0), "(5d/4) " + dot1("θ"), "GREEN", "start", 16, weight="700", dx=12, dy=-14)
    sc.vec(PA, (-1.0, 4.0), None, "GREEN", 3.0, head=12)
    sc.label((-1.0, 4.0), "(5d/2) " + dot1("θ"), "GREEN", "middle", 16, weight="700", dx=-8, dy=-14)
    sc.vec((-1.3, 0.0), (-1.3, 4.0), None, ORANGE, 3.0, head=12)
    sc.dashed(PA, (-1.3, 0.0))
    sc.label((-1.3, 4.0), "d " + S("ω", "D"), ORANGE, "end", 16, weight="700", dx=-12, dy=6)
    sc.dashed((-1.0, 4.0), (1.0, 0.0), col="GREEN")
    sc.note((0.55, 2.55), "velocity along " + ET, "TEXT", "start", 14, dx=22, dy=0)
    # clockwise spin of the bearing, lower half, and its name
    sc.spin(A, 0.42, -25.0, -155.0, "", "GREEN")
    sc.label((0.0, -1.0), S("ω", "A") + " = −5 " + dot1("θ"), "GREEN", "middle", 16, weight="700", dy=24)
    # dimensions d/4
    for x0, x1 in ((-1.0, 0.0), (0.0, 1.0)):
        sc.dim((x0, -1.75), (x1, -1.75), "d/4", off=(0, 20))
    for xv in (-1.0, 1.0):
        sc.dashed((xv, 0.0), (xv, -1.85))
    sc.dashed((0.0, -1.65), (0.0, -1.85))
    # basis key (bottom right corner)
    b0 = (2.0, -2.9)
    sc.vec(b0, add(b0, (1.0, 0.0), 1.0), ER, "BLUE", 2.6, name_off=(10, 20), size=16, head=10)
    sc.vec(b0, add(b0, (0.0, 1.0), 1.0), ET, "BLUE", 2.6, name_off=(-4, -10), size=16, head=10)
    axis_out(sc, b0, None, "HEAD")
    sc.label(b0, K + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=24)
    return sc


# ------------------------------------------------------------------------------------------------ rb26-exploded
@figure("rb26-exploded",
        "Exploded view of the disk, the three bearings and the cavity with the normal and friction forces at every "
        "contact and the weights.",
        r"Exploded view: the cavity acts on bearing $i$ with $-N_i^c\,\mathbf e_r + F_i^c\,\mathbf e_\theta$, the disk with "
        r"$N_i^d\,\mathbf e_r + F_i^d\,\mathbf e_\theta$, and the bearing on the disk with the opposite pair.")
def exploded():
    sc = Scene(960, 940, (480, 470), 43)
    O = (0.0, 0.0)
    th = THETA
    sub = lambda t: '<tspan baseline-shift="sub" font-size="70%">' + t + '</tspan>'
    sup = lambda t: '<tspan baseline-shift="super" font-size="70%">' + t + '</tspan>'

    def nm(base, who, kind):
        return base + sub(who) + sup(kind)
    # disk
    sc.circle(O, 4.0, "HEAD", 2.0, fill="EDGE", opacity=0.10)
    sc.mass(O, None, r=4, col="BLUE")
    sc.label(O, "O", "HEAD", "middle", 17, dx=14, dy=-8)
    sc.note((-1.0, 3.0), "DISK D", "HEAD", "middle", 15, dx=0, dy=0)
    sc.vec(O, (0.0, -1.7), "2mg", "PINK", 3.0, name_off=(-26, 8), size=17, head=12)
    names = (("A", th, True), ("B", th + 135, False), ("C", th + 225, False))
    for who, a, full in names:
        cen = pol(a, 7.0)
        # cavity arc outside the bearing (pulled outward)
        wall = [pol(a + t, 10.0) for t in range(-13, 14, 1)]
        sc.poly(wall, "HEAD", 2.2)
        rim_hatch(sc, O, 10.0, a - 13, a + 13, inward=False, step=2.0, length=0.28)
        # bearing
        sc.circle(cen, 1.0, "HEAD", 2.0, fill="EDGE", opacity=0.12)
        sc.mass(cen, None, r=3.5, col="BLUE")
        sc.label(cen, who, "HEAD", "middle", 17, dx=-14, dy=-8 if who != "C" else 20)
        sc.vec(cen, add(cen, (0.0, -1.0), 1.7), "mg" if full else None, "PINK", 3.0, name_off=(22, 6), size=16, head=12)
        if not full:
            sc.label(add(cen, (0.0, -1.0), 1.7), "mg", "PINK", "middle", 15, weight="700", dx=18, dy=4)
        # cavity forces on the bearing at Q (r = 8): N^c tip at Q (from the gap), F^c along e_theta
        Q, P, Pd = pol(a, 8.0), pol(a, 6.0), pol(a, 4.0)
        sc.vec(pol(a, 9.25), Q, None, "GREEN", 3.0, head=12)
        sc.vec(Q, pol(a, 8.0, 1.3), None, "GREEN", 3.0, head=12)
        # disk forces on the bearing at P (r = 6)
        sc.vec(pol(a, 4.85), P, None, ORANGE, 3.0, head=12)
        sc.vec(P, pol(a, 6.0, 1.3), None, ORANGE, 3.0, head=12)
        # bearing forces on the disk at P^d (r = 4): -N^d towards O, -F^d clockwise
        sc.vec(Pd, pol(a, 2.75), None, ORANGE, 3.0, head=12)
        sc.vec(Pd, pol(a, 4.0, -1.3), None, ORANGE, 3.0, head=12)
        # dashed pair link, displaced along e_theta so it does not run under the arrows
        sc.dashed(pol(a, 3.96, 0.7), pol(a, 6.29, 0.7))
        for p in (P, Pd):
            sc.mass(p, None, r=3.0, col="HEAD")
        if full:
            sc.label(pol(a, 9.25), nm("N", "A", "c"), "GREEN", "middle", 16, weight="700", dx=-6, dy=-14)
            sc.label(pol(a, 8.0, 1.3), nm("F", "A", "c"), "GREEN", "middle", 16, weight="700", dx=-14, dy=-14)
            sc.label(pol(a, 5.4), nm("N", "A", "d"), ORANGE, "middle", 16, weight="700", dx=18, dy=22)
            sc.label(pol(a, 6.0, 1.3), nm("F", "A", "d"), ORANGE, "middle", 16, weight="700", dx=-18, dy=-10)
            sc.label(pol(a, 3.3), "−" + nm("N", "A", "d"), ORANGE, "middle", 16, weight="700", dx=-30, dy=8)
            sc.label(pol(a, 4.0, -1.3), "−" + nm("F", "A", "d"), ORANGE, "middle", 16, weight="700", dx=14, dy=18)
        else:
            sc.label(pol(a, 9.25), "c", "GREEN", "middle", 15, weight="700", dx=-10, dy=-8)
            sc.label(pol(a, 8.0, 1.3), "c", "GREEN", "middle", 15, weight="700", dx=-8 if who == "B" else 12, dy=-10 if who == "B" else 4)
            sc.label(pol(a, 5.4), "d", ORANGE, "middle", 15, weight="700", dx=10, dy=12)
            sc.label(pol(a, 6.0, 1.3), "d", ORANGE, "middle", 15, weight="700", dx=-8, dy=-10)
            sc.label(pol(a, 3.3), "d", ORANGE, "middle", 15, weight="700", dx=-12, dy=6)
            sc.label(pol(a, 4.0, -1.3), "d", ORANGE, "middle", 15, weight="700", dx=10, dy=12)
    sc.note((1.6, 9.9), "cavity, fixed", "TEXT", "start", 14)
    # small basis at bearing A
    b1 = pol(th, 7.6, -2.6)
    unit(sc, b1, th, 1.0, ER, "BLUE", off=(14, 16))
    unit(sc, b1, th + 90, 1.0, ET, "BLUE", off=(-4, -12))
    sc.note(b1, "basis at A", "TEXT", "start", 13, dx=-26, dy=34)
    # key
    b0 = (-9.3, -9.3)
    sc.vec(b0, add(b0, (1.0, 0.0), 1.0), I, "EDGE", 1.6, name_off=(12, 6), size=16, head=9)
    sc.vec(b0, add(b0, (0.0, 1.0), 1.0), J, "EDGE", 1.6, name_off=(10, -4), size=16, head=9)
    axis_out(sc, b0, None, "HEAD")
    sc.label(b0, K + " (⊙)", "HEAD", "start", 16, weight="700", dx=14, dy=40)
    return sc
