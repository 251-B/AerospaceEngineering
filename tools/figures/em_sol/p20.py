"""Problem 20: heavy particle on a circular wire that turns about its vertical diameter."""
import math

from figures.em_solutions import (axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle,
                                  unit)
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

WT = 35.0            # drawn value of omega t, degrees
TH = 50.0            # drawn value of theta, degrees


@figure("p20-top-view",
        "Top view with k0 = k1 out of the paper: inertial axes i0, j0 in grey, the trace of the wire plane along i1 "
        "turned by omega t, and j1 normal to the wire plane, with the dashed right triangles of their components",
        r"View from $+\mathbf k_0$ ($\mathbf k_0 = \mathbf k_1$ out of the paper, $\odot$). The wire is seen edge-on, "
        r"along $\mathbf i_1$, turned counter-clockwise by $\omega t$; $\mathbf j_1 = \mathbf k_1\times\mathbf i_1$ is "
        r"normal to it. The opposite leg of $\mathbf j_1$ points along $-\mathbf i_0$: hence "
        r"$\mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0$")
def top_view():
    sc = Scene(560, 480, (270, 330), 220)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(WT)), math.sin(math.radians(WT))
    sc.line((-1.1 * c, -1.1 * s), (1.15 * c, 1.15 * s), "EDGE", 5.0)
    sc.note((-0.2, -0.6), "wire (seen edge-on)", "TEXT", "start", 13)
    fixed_axis(sc, O, 0, 1.05, bold("i") + S("", "0"), off=(16, 6))
    fixed_axis(sc, O, 90, 1.2, bold("j") + S("", "0"), off=(16, 4))
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), (-s, c)], "BLUE", 0.10)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((0.0, c), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(-6, -16))
    unit(sc, O, WT + 90, 1.0, bold("j") + S("", "1"), off=(-14, -8))
    sc.angle(O, 0.30, 0, WT, "ωt", name_r=0.43)
    sc.angle(O, 0.30, 90, 90 + WT, "ωt", name_r=0.44)
    sc.label((c / 2, 0.0), "cos ωt", "TEXT", "middle", 15, dy=22)
    sc.label((c, s * 0.35), "sin ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, c), "sin ωt", "TEXT", "middle", 15, dy=-10)
    sc.label((0.0, c / 2), "cos ωt", "TEXT", "start", 15, dx=8, dy=16)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-58, 4))
    return sc


@figure("p20-wire-plane",
        "Plane of the wire fixed in S1: centre O, vertical axis k1, particle P at the angle theta from the downward "
        "vertical, the right triangle OFP with legs R sin theta and R cos theta, j1 into the paper, and the wire basis "
        "e_r, e_theta at P",
        r"Plane of the wire, fixed in $S_1$ ($\mathbf i_1$ right, $\mathbf k_1$ up, so $\mathbf j_1$ points into the "
        r"paper, $\otimes$). In the shaded right triangle $OFP$ the hypotenuse is $R$, the leg opposite $\theta$ is "
        r"$R\sin\theta$ along $\mathbf i_1$ and the adjacent leg is $R\cos\theta$ along $-\mathbf k_1$. "
        r"$\mathbf e_r, \mathbf e_\theta$ in orange")
def wire_plane():
    sc = Scene(600, 560, (290, 290), 200)
    O = (0.0, 0.0)
    t = math.radians(TH)
    P = (math.sin(t), -math.cos(t))
    F = (0.0, P[1])
    sc.circle(O, 1.0, "HEAD", 3.0)
    fixed_axis(sc, (0.0, -1.2), 90, 2.45, S("z", "1"), off=(14, 2))
    fixed_axis(sc, (-1.2, 0.0), 0, 2.45, S("x", "1"), off=(14, 5))
    spin_about_vertical(sc, (0.0, 1.08), 0.16, 0.05, "ω")
    triangle(sc, [O, F, P])
    right_angle(sc, F, 0, 90, 0.05)
    sc.dashed(F, P)
    sc.line(O, P, "HEAD", 1.6)
    sc.angle(O, 0.24, -90, -90 + TH, "θ", name_r=0.34)
    sc.label(((O[0] + P[0]) / 2, (O[1] + P[1]) / 2), "R", "TEXT", "start", 17, dx=10, dy=-2)
    sc.label((0.0, F[1] / 2), "R cos θ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label(((F[0] + P[0]) / 2, F[1]), "R sin θ", "TEXT", "middle", 15, dy=22)
    unit(sc, O, 0, 0.3, bold("i") + S("", "1"), off=(8, -12))
    unit(sc, O, 90, 0.3, bold("k") + S("", "1"), off=(-18, 4))
    axis_in(sc, (-0.55, 0.55), bold("j") + S("", "1"), "BLUE", off=(0, 30))
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    unit(sc, P, TH - 90, 0.28, bold("e") + S("", "r"), "ACC", off=(14, 10))
    unit(sc, P, TH, 0.28, bold("e") + S("", "θ"), "ACC", off=(14, -4))
    sc.mass(P, "P", r=7, name_off=(26, 6))
    sc.gravity((1.15, 0.95), 0.32, "g")
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


@figure("p20-fbd",
        "Free-body diagram of the bead on the rotating wire: weight, in-plane reaction and centrifugal force in the plane "
        "of the wire, and normal reaction and Coriolis force normal to it",
        r"Forces on $P$ in $S_1$. In the plane of the wire: weight, $N_r\,\mathbf e_r$ and the centrifugal force "
        r"$m\omega^2R\sin\theta\,\mathbf i_1$. Normal to it: the reaction $N_b\,\mathbf j_1$ and the Coriolis force "
        r"$-2m\omega R\dot\theta\cos\theta\,\mathbf j_1$, which balance each other.")
def fbd():
    sc = Scene(1160, 690, (250, 320), 130)
    R = 1.6
    t = math.radians(TH)
    O = (0.0, 0.0)
    P = (R * math.sin(t), -R * math.cos(t))
    er = (math.sin(t), -math.cos(t))
    # ---- left panel: the plane of the wire
    sc.circle(O, R, "HEAD", 3.0)
    sc.line((0.0, -R - 0.3), (0.0, R + 0.35), "EDGE", 1.3, "10 3 2 3")
    sc.label((0.0, R + 0.35), "axis of rotation (" + S(bold("k"), "1") + ")", "TEXT", "end", 15, dx=-10, dy=2)
    spin_about_vertical(sc, (0.0, R + 0.52), 0.16, 0.05, "ω")
    sc.dashed(O, P)
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 18, dx=-8, dy=22)
    axis_in(sc, (-0.55, 0.55), None, "BLUE", 8)
    sc.label((-0.55, 0.55), S(bold("j"), "1"), "BLUE", "end", 16, weight="700", dx=-14, dy=5)
    g0 = (-1.75, -1.5)
    fixed_axis(sc, g0, 0, 0.5, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, g0, 90, 0.5, S(bold("k"), "1"), off=(0, -8))
    sc.dashed((0.0, P[1]), P)
    sc.label((P[0] / 2, P[1]), S("r", "⊥") + " = R sin θ", "TEXT", "middle", 16, dy=24)
    sc.angle(O, 0.30, -90, -90 + TH, "θ", name_r=0.44)
    # forces at P, all from P itself
    sc.vec(P, (P[0], P[1] - 0.9), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.9), "−m g " + S(bold("k"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=14)
    nr_tip = (P[0] + 0.85 * er[0], P[1] + 0.85 * er[1])
    sc.vec(P, nr_tip, None, "PINK", 2.8, head=11)
    sc.label(nr_tip, S("N", "r") + " " + S(bold("e"), "r"), "PINK", "start", 16, weight="700", dx=10, dy=16)
    fc = (P[0] + 0.8, P[1])
    _dvec(sc, P, fc, "PINK", 2.6)
    sc.label(fc, S(bold("F"), "C") + " = mω²R sin θ " + S(bold("i"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=5)
    unit(sc, P, TH - 90, 0.45, S(bold("e"), "r"), "ACC", off=(-14, 22))
    unit(sc, P, TH, 0.45, S(bold("e"), "θ"), "ACC", off=(8, -10))
    sc.mass(P, "P", r=7, name_off=(-18, -12))
    px, py = -1.5, -2.05
    axis_in(sc, (px, py), None, "PINK", 8)
    sc.label((px, py), S("N", "b") + " " + S(bold("j"), "1") + "  (into the paper), at P", "PINK", "start", 16, weight="700",
             dx=16, dy=5)
    axis_out(sc, (px, py - 0.34), None, "PINK", 8)
    sc.label((px, py - 0.34), S(bold("F"), "COR") + "  (out of the paper), at P", "PINK", "start", 16, weight="700",
             dx=16, dy=5)
    sc.note((px - 0.1, py - 0.72), "F_COR along −j₁ when θ̇ cos θ > 0; dashed = inertia force", "TEXT", "start", 14)
    # ---- right panel: seen from above, k1 out of the paper
    OR = (4.1, 0.0)
    PR = (OR[0] + R * math.sin(t), 0.0)
    sc.line((OR[0] - R, 0.0), (OR[0] + R, 0.0), "HEAD", 5.0)
    sc.note((OR[0] - R, 0.25), "wire seen edge-on", "TEXT", "start", 14)
    fixed_axis(sc, (OR[0] + R, 0.0), 0, 0.4, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, OR, 90, 1.55, S(bold("j"), "1"), off=(0, -8))
    axis_out(sc, OR, None, "HEAD", 9)
    sc.label(OR, S(bold("k"), "1") + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=26)
    sc.spin(OR, 0.55, 105, 165, "ω", "GREEN", name_r=0.78, size=17)
    sc.vec(PR, (PR[0], 0.9), None, "PINK", 2.8, head=11)
    sc.label((PR[0], 0.9), S("N", "b") + " " + S(bold("j"), "1"), "PINK", "end", 16, weight="700", dx=-10, dy=2)
    d = 0.10
    _dvec(sc, (PR[0] - d, 0.0), (PR[0] - d, -0.7), "PINK", 2.6)
    sc.label((PR[0] - d, -0.7), S(bold("F"), "COR") + " = −2mωRθ̇ cos θ " + S(bold("j"), "1"), "PINK", "end",
             16, weight="700", dx=-4, dy=22)
    sc.vec((PR[0] + 0.3, 0.0), (PR[0] + 0.3, 0.5), None, "GREEN", 2.2, head=10)
    sc.label((PR[0] + 0.3, 0.5), S("v", "t") + " = ωR sin θ " + S(bold("j"), "1"), "GREEN", "start", 16, weight="700",
             dx=10, dy=4)
    sc.mass(PR, None, r=6)
    sc.label(PR, "P (top view)", "HEAD", "start", 16, dx=12, dy=26)
    sc.note((OR[0] - R, -1.9), "N_b and F_COR balance: N_b = 2mωR θ̇ cos θ", "TEXT", "start", 14)
    return sc
