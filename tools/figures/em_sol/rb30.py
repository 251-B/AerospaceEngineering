"""Problem RB-30: free spinning asteroid, 1-2-3 Euler angles (psi about i0, theta about j1, phi about k2) and Poinsot's
construction (inertia ellipsoid rolling on the invariant plane, polhode projected on the plane of i_b and j_b).

Figures: one view per rotation, the side view of Poinsot's construction (true section of the ellipsoid by the plane of
G, P and the angular momentum) and the polhode ellipse.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb17 import rot_pair
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

ORANGE = "ACC"
DRED = "#be123c"          # red of the body basis and of the angular velocity (as in the t8 theory figures)
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1, K1 = S(I, "1"), S(J, "1"), S(K, "1")
I2, J2, K2 = S(I, "2"), S(J, "2"), S(K, "2")
IB, JB, KB = S(I, "b"), S(J, "b"), S(K, "b")


# ------------------------------------------------------------------------------------------------ rb30-rot-psi
@figure("rb30-rot-psi",
        "First Euler rotation: the basis B1 turned by psi about i0, which points out of the paper.",
        r"First rotation of the 1-2-3 sequence, $\psi$ about $\mathbf i_0$ (⊙): $\mathbf j_1 = \cos\psi\,\mathbf j_0 + "
        r"\sin\psi\,\mathbf k_0$, $\mathbf k_1 = -\sin\psi\,\mathbf j_0 + \cos\psi\,\mathbf k_0$.")
def rot_psi():
    sc = Scene(820, 760, (330, 400), 130)
    rot_pair(sc, 35.0, (J0, K0, J1, K1), "ψ", I0 + " = " + I1 + " (⊙)", "out", (-14, 30), L=1.9, Lf=2.6, arc_r=0.6,
             arc_lab=((20, 12), (-4, 4)), lab_offs=((24, 4), (-18, -6)))
    return sc


# ------------------------------------------------------------------------------------------------ rb30-rot-theta
@figure("rb30-rot-theta",
        "Second Euler rotation: the basis B2 turned by theta about j1, which points out of the paper.",
        r"Second rotation, $\theta$ about $\mathbf j_1$ (⊙, with $\mathbf k_1$ to the right and $\mathbf i_1$ up): "
        r"$\mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1$, $\mathbf i_2 = \cos\theta\,\mathbf i_1 - "
        r"\sin\theta\,\mathbf k_1$.")
def rot_theta():
    sc = Scene(820, 780, (330, 420), 130)
    rot_pair(sc, 30.0, (K1, I1, K2, I2), "θ", J1 + " = " + J2 + " (⊙)", "out", (-14, 30), L=1.9, Lf=2.6, arc_r=0.6,
             arc_lab=((20, 12), (-4, 4)), lab_offs=((24, 4), (-22, -8)))
    sc.note((-1.6, -1.9), "k₁ × i₁ = j₁ (right-handed view)", "TEXT", "start", 14)
    return sc


# ------------------------------------------------------------------------------------------------ rb30-rot-phi
def asteroid(sc, r0=2.3):
    pts = []
    for t in range(0, 361, 6):
        a = math.radians(t)
        rr = r0 * (1 + 0.10 * math.cos(2 * a + 0.5) + 0.06 * math.cos(3 * a + 1.0) + 0.04 * math.cos(5 * a))
        pts.append((rr * math.cos(a), rr * math.sin(a)))
    sc.poly(pts, "EDGE", 1.6, dash="6 5", fill="EDGE", close=True, opacity=0.07)


@figure("rb30-rot-phi",
        "Third Euler rotation: the body basis Bb turned by phi about k2, which points out of the paper.",
        r"Third rotation, $\phi$ about $\mathbf k_2 = \mathbf k_b$ (⊙): $\mathbf i_b = \cos\phi\,\mathbf i_2 + "
        r"\sin\phi\,\mathbf j_2$, $\mathbf j_b = -\sin\phi\,\mathbf i_2 + \cos\phi\,\mathbf j_2$.")
def rot_phi():
    sc = Scene(860, 800, (430, 400), 120)
    asteroid(sc, 2.45)
    sc.label((1.7, -2.45), "asteroid", "TEXT", "start", 14, dx=8, dy=14)
    rot_pair(sc, 25.0, (I2, J2, IB, JB), "φ", K2 + " = " + KB + " (⊙)", "out", (-14, 30), L=1.9, Lf=3.0, arc_r=0.6, col=DRED, arc_lab=((20, 12), (-4, 4)), lab_offs=((24, 4), (-22, -8)))
    return sc
