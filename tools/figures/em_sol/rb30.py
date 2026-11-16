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


def left_lab(ang, arc_r, k, gap=16.0):
    """Pixel shift that puts the label of the second angle arc just left of the rotated axis (the arc is too narrow for it)."""
    mid = math.radians(90.0 + ang / 2)
    px, py = arc_r * k * math.cos(mid), arc_r * k * math.sin(mid)
    vx = py * math.cos(math.radians(90.0 + ang)) / math.sin(math.radians(90.0 + ang))
    return (vx - gap - px, 4)


# ------------------------------------------------------------------------------------------------ rb30-rot-psi
@figure("rb30-rot-psi",
        "First Euler rotation: the basis B1 turned by psi about i0, which points out of the paper.",
        r"First rotation of the 1-2-3 sequence, $\psi$ about $\mathbf i_0$ (⊙): $\mathbf j_1 = \cos\psi\,\mathbf j_0 + "
        r"\sin\psi\,\mathbf k_0$, $\mathbf k_1 = -\sin\psi\,\mathbf j_0 + \cos\psi\,\mathbf k_0$.")
def rot_psi():
    sc = Scene(860, 560, (340, 420), 150)
    rot_pair(sc, 35.0, (J0, K0, J1, K1), "ψ", I0 + " = " + I1 + " (⊙)", "out", (-14, 30), L=1.9, Lf=2.6, arc_r=0.6,
             arc_lab=((20, 12), left_lab(35.0, 0.6, 150)), lab_offs=((24, 4), (-18, -6)))
    return sc


# ------------------------------------------------------------------------------------------------ rb30-rot-theta
@figure("rb30-rot-theta",
        "Second Euler rotation: the basis B2 turned by theta about j1, which points out of the paper.",
        r"Second rotation, $\theta$ about $\mathbf j_1$ (⊙, with $\mathbf k_1$ to the right and $\mathbf i_1$ up): "
        r"$\mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1$, $\mathbf i_2 = \cos\theta\,\mathbf i_1 - "
        r"\sin\theta\,\mathbf k_1$.")
def rot_theta():
    sc = Scene(860, 600, (340, 430), 150)
    rot_pair(sc, 30.0, (K1, I1, K2, I2), "θ", J1 + " = " + J2 + " (⊙)", "out", (-14, 30), L=1.9, Lf=2.6, arc_r=0.6,
             arc_lab=((20, 12), left_lab(30.0, 0.6, 150)), lab_offs=((24, 4), (-22, -8)))
    sc.note((-1.9, -1.0), K1 + " × " + I1 + " = " + J1 + " (right-handed view)", "TEXT", "start", 14)
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
    sc = Scene(860, 700, (430, 405), 125)
    asteroid(sc, 2.45)
    sc.label((0.7, -1.6), "asteroid", "TEXT", "start", 14)
    rot_pair(sc, 25.0, (I2, J2, IB, JB), "φ", K2 + " = " + KB + " (⊙)", "out", (-14, 30), L=1.9, Lf=3.0, arc_r=0.6, col=DRED, arc_lab=((20, 12), left_lab(25.0, 0.6, 125)), lab_offs=((24, 4), (-22, -8)))
    return sc


# ------------------------------------------------------------------------------------------------ rb30-poinsot
@figure("rb30-poinsot",
        "The ellipsoid fixed to the asteroid touching the invariant plane at P, with the normals of both surfaces along the "
        "angular momentum and the right triangle G N P.",
        r"Poinsot's construction: $P$ is on the ellipsoid and on the invariant plane at the distance $\delta$ from $G$; "
        r"both normals at $P$ are along $\mathbf H_{G0}^b$, so the surfaces are tangent, and $P$, on the instantaneous axis, "
        r"is at rest.")
def poinsot():
    sc = Scene(1000, 730, (330, 300), 105)
    dl, rho = 3 * math.sqrt(2) / 2, math.sqrt(2) / 2
    G, N, P = (0.0, 0.0), (0.0, -dl), (rho, -dl)
    # the plane (edge-on), at the distance delta from G along u_H (drawn downwards: the plane is at +delta along u_H)
    sc.line((-3.1, -dl), (3.4, -dl), "EDGE", 6.0)
    sc.label((-3.1, -dl), "invariant plane (edge-on), normal " + bold("H"), "TEXT", "start", 14, dy=28)
    # true section of the ellipsoid x_b^2/12 + y_b^2/6 + z_b^2/3 = l^2 by the plane of G, P and H (x_b = 0):
    # y_b^2/6 + z_b^2/3 = 1, with u = (y + z)/sqrt2 along H and w = (y - z)/sqrt2 along NP
    pts = []
    for t in range(0, 361, 4):
        a = math.radians(t)
        y, z = math.sqrt(6.0) * math.cos(a), math.sqrt(3.0) * math.sin(a)
        pts.append(((y - z) / math.sqrt(2.0), -(y + z) / math.sqrt(2.0)))
    sc.poly(pts, "HEAD", 2.4, fill="EDGE", close=True, opacity=0.08)
    sc.label((-3.1, 2.55), "section of the ellipsoid by the plane of G, P and " + bold("H") + " (semi-axes √6 ℓ and √3 ℓ)",
             "TEXT", "start", 14)
    # right triangle G N P
    triangle(sc, [G, N, P], ORANGE, 0.22)
    sc.dashed(G, N)
    right_angle(sc, N, 90, 0, 0.12)
    # H at G, over the dashed segment
    sc.vec(G, (0.0, -1.1), None, "BLUE", 3.0, head=12)
    sc.label((0.0, -0.55), S(bold("H"), "G0") + " (fixed in " + S("S", "0") + ")", "BLUE", "end", 16, weight="700", dx=-12, dy=4)
    sc.label((0.0, -1.65), "δ", "TEXT", "end", 17, dx=-10, dy=4)
    # r_P = tau l omega, red, along the instantaneous axis
    sc.vec(G, P, None, DRED, 3.0, head=12)
    sc.label(((G[0] + P[0]) / 2, (G[1] + P[1]) / 2), "r" + S("", "P") + " = τℓ" + bold("ω"), DRED, "start", 16, weight="700",
             dx=20, dy=2)
    sc.label((rho / 2, -dl), "ρ", "TEXT", "middle", 16, dy=24)
    sc.mass(P, None, r=5, col=DRED)
    sc.label(P, "P", "HEAD", "start", 18, dx=12, dy=-12)
    sc.mass(N, None, r=3.8, col="BLUE")
    sc.label(N, "N", "HEAD", "end", 17, dx=-8, dy=26)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "start", 18, dx=12, dy=-10)
    # the two normals at P, side by side, along u_H (away from the ellipsoid, towards and through the plane)
    e = 0.13
    sc.vec((rho - e, -dl), (rho - e, -dl - 0.95), None, "GREEN", 3.0, head=12)
    sc.vec((rho + e, -dl), (rho + e, -dl - 0.95), None, "BLUE", 3.0, head=12)
    sc.label((rho - e, -dl - 0.95), "∇F", "GREEN", "end", 16, weight="700", dx=-8, dy=18)
    sc.label((rho + e, -dl - 0.95), bold("H"), "BLUE", "start", 16, weight="700", dx=8, dy=18)
    sc.label((rho, -dl - 0.95), "∇F ∥ H", "TEXT", "middle", 15, dy=42)
    sc.note((1.5, -dl - 0.55), "v of the body point at P = 0 (rolls without slipping)", "TEXT", "start", 14)
    sc.note((-3.1, -dl - 1.85), "δ = 3√2 ℓ/2 ≈ 2.12 ℓ,  ρ = ℓ/√2 ≈ 0.71 ℓ  (initial instant)", "TEXT", "start", 14)
    sc.note((-3.1, -dl - 1.55), "r" + S("", "P") + " = |r| = √5 ℓ ≈ 2.24 ℓ, the hypotenuse of G N P", "TEXT", "start", 14)
    return sc


# ------------------------------------------------------------------------------------------------ rb30-polhode
@figure("rb30-polhode",
        "Polhode of the asteroid projected on the plane normal to k_b: an ellipse around the major axis traversed "
        "counterclockwise from the initial angular velocity.",
        r"Projection of the polhode on the plane of $\mathbf i_b$ and $\mathbf j_b$ (units of $1/\tau$): the ellipse "
        r"$3\omega_{xb}^2 + 4\omega_{yb}^2 = 16/\tau^2$, travelled from the initial point $(0, 2)$ towards minus "
        r"$\mathbf i_b$, with $\tau\omega_{zb}$ between 1 and 1.291.")
def polhode():
    sc = Scene(1000, 700, (500, 360), 125)
    ax, ay = 4.0 / math.sqrt(3.0), 2.0
    # thin grey axes, in units of 1/tau
    sc.vec((-3.0, 0.0), (3.0, 0.0), None, "EDGE", 1.4, head=8)
    sc.vec((0.0, -2.5), (0.0, 2.5), None, "EDGE", 1.4, head=8)
    sc.label((3.0, 0.0), IB, "TEXT", "start", 17, weight="700", dx=10, dy=5)
    sc.label((0.0, 2.5), JB, "TEXT", "start", 17, weight="700", dx=10, dy=-2)
    for v in (-2, -1, 1, 2):
        sc.line((v, -0.05), (v, 0.05), "EDGE", 1.2)
        if v > 0:
            sc.label((v, 0.0), str(v), "TEXT", "middle", 12, italic=False, dy=-10 if v != 2 else 20)
    for v in (-2, -1, 1, 2):
        sc.line((-0.04, v), (0.04, v), "EDGE", 1.2)
    sc.label((0.0, 1.0), "1", "TEXT", "end", 12, italic=False, dx=-8, dy=4)
    sc.label((0.0, -1.0), "−1", "TEXT", "end", 12, italic=False, dx=-8, dy=4)
    axis_out(sc, (0.0, 0.0), None, "HEAD")
    sc.label((0.0, 0.0), KB + " (⊙)", "HEAD", "end", 15, weight="700", dx=-14, dy=24)
    # polhode ellipse: 3 wx^2 + 4 wy^2 = 16 (units 1/tau^2)
    pts = [(ax * math.cos(math.radians(t)), ay * math.sin(math.radians(t))) for t in range(0, 361, 3)]
    sc.poly(pts, ORANGE, 3.2, close=True)
    # sense of travel: arrowhead just to the left of (0, 2), counterclockwise
    t0, t1 = math.radians(97.0), math.radians(105.0)
    a0 = sc.P((ax * math.cos(t0), ay * math.sin(t0)))
    a1 = sc.P((ax * math.cos(t1), ay * math.sin(t1)))
    arrow_head(sc.c, a0, a1, ORANGE, 15)
    sc.label((-0.75, 1.85), "counterclockwise", "TEXT", "middle", 14, dy=-32)
    # the three marked points
    for p in ((0.0, ay), (ax, 0.0), (-ax, 0.0)):
        sc.mass(p, None, r=5.5, col=DRED)
    sc.label((0.0, ay), "ω(0) = (0, 2, 1)/τ", DRED, "start", 15, weight="700", dx=16, dy=-22)
    sc.label((0.0, ay), "ω" + S("", "z") + " = 1/τ (smallest)", DRED, "start", 15, weight="700", dx=16, dy=-5)
    for sx, anc, dx in ((1, "start", 14), (-1, "end", -14)):
        sc.label((sx * ax, 0.0), "ω" + S("", "y") + " = 0", DRED, anc, 15, weight="700", dx=dx, dy=-32)
        sc.label((sx * ax, 0.0), "τω" + S("", "z") + " = 1.291 (largest)", DRED, anc, 15, weight="700", dx=dx, dy=-14)
    # note inside
    for k, line in enumerate(("polhode around +" + KB, "(major axis of inertia);", "ω" + S("", "z") + " never vanishes")):
        sc.label((0.0, -0.75 - 0.3 * k), line, "TEXT", "start", 15, dx=18, dy=4)
    sc.note((-3.0, -2.35), "axes in units of 1/τ: τω" + S("", "xb") + ", τω" + S("", "yb"), "TEXT", "start", 14)
    sc.note((-3.0, -2.6), "3 ω" + S("", "xb") + "² + 4 ω" + S("", "yb") + "² = 16/τ²", "TEXT", "start", 14)
    return sc
