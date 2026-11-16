"""Problem RB-37: disk of radius R rolling without slip below a fixed cylinder of radius 3R, with a repulsive force from A."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d, rotation_view
from figures.em_sol.rb12 import plane_rotation
from figures.em_sol.rb23 import circle_pts, rim_hatch, tri_pair
from figures.mech import S, Scene, bold, dot1, dot2

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1 = S(I, "1"), S(J, "1")
IB, JB = S(I, "b"), S(J, "b")
R = 1.0
PSI = 40.0
PS = math.radians(PSI)
GPOS = (4 * R * math.sin(PS), -4 * R * math.cos(PS))
CPOS = (3 * R * math.sin(PS), -3 * R * math.cos(PS))
I1D = (math.cos(PS), math.sin(PS))
J1D = (-math.sin(PS), math.cos(PS))                   # from G towards O


def _cylinder(sc, faint=False):
    """Lower half of the fixed cylinder (radius 3R, centre O): outline and hatching ticks just inside the rim."""
    sc.poly(circle_pts((0.0, 0.0), 3 * R, 180.0, 360.0, 120), "EDGE" if faint else "HEAD", 1.6 if faint else 2.2)
    # hatching ticks inside the rim, left out around the contact point so that the labels there stay readable
    rim_hatch(sc, (0.0, 0.0), 3 * R, 180.0, 285.0, inward=True, step=5.0, length=0.2)
    rim_hatch(sc, (0.0, 0.0), 3 * R, 340.0, 360.0, inward=True, step=5.0, length=0.2)
    if not faint:
        sc.label((-3 * R * 0.72, -3 * R * 0.72), "fixed cylinder", "TEXT", "end", 14, dx=-20, dy=-4)


# ------------------------------------------------------------------------------------------------ rb37-rot-psi
@figure("rb37-rot-psi",
        "The basis of the line of centres, turned by psi, with G at 4R from O.",
        r"Rotation about $\mathbf k_0$ (⊙) by $\psi$, measured from the downward vertical. $\mathbf j_1$ points from $G$ "
        r"towards $O$, so $\mathbf r_0^G$ is $-4R\,\mathbf j_1$.")
def rot_psi():
    sc = Scene(860, 780, (370, 190), 100)
    O = (0.0, 0.0)
    _cylinder(sc)
    # disk of radius R touching the cylinder at C
    sc.poly(circle_pts(GPOS, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    # line of centres and the downward vertical
    sc.line(O, GPOS, "HEAD", 1.8)
    sc.dashed(O, (0.0, -3 * R))
    # axes at O
    fixed_axis(sc, O, 0, 1.5, I0, off=(14, 6))
    fixed_axis(sc, O, 90, 1.5, J0, off=(12, -2))
    # triangle of the unit vector along OG
    u = (math.sin(PS), -math.cos(PS))
    foot = (0.0, -math.cos(PS))
    triangle(sc, [O, foot, u], ORANGE, 0.22)
    sc.dashed(foot, u)
    right_angle(sc, foot, 90, 0, 0.07)
    sc.label((0.0, -math.cos(PS) / 2), "cos ψ", "TEXT", "end", 14, dx=-6, dy=4)
    sc.label((u[0] / 2, foot[1]), "sin ψ", "TEXT", "middle", 14, dy=18)
    sc.label(add(O, u, 0.5), "1", "TEXT", "start", 14, dx=8, dy=0)
    # arc of psi at O, from the downward vertical to OG
    sc.arc(O, 1.25, -90, -90 + PSI, "GREEN", 1.8, head=True)
    sc.label(add(O, d(-90 + PSI / 2), 1.25), "ψ", "GREEN", "middle", 17, dx=-2, dy=24)
    # unit vectors at G and the arcs of psi
    unit(sc, GPOS, PSI, 1.0, I1, "BLUE", off=(18, -8))
    unit(sc, GPOS, 90 + PSI, 1.0, J1, "BLUE", off=(-24, 26))
    sc.line(GPOS, add(GPOS, (1.0, 0.0), 0.95), "EDGE", 1.0, "4 4")
    sc.line(GPOS, add(GPOS, (0.0, 1.0), 0.95), "EDGE", 1.0, "4 4")
    sc.arc(GPOS, 0.55, 0, PSI, "GREEN", 1.7, head=True)
    sc.arc(GPOS, 0.55, 90, 90 + PSI, "GREEN", 1.7, head=True)
    sc.label(add(GPOS, d(PSI / 2), 0.55), "ψ", "GREEN", "middle", 17, dx=14, dy=4)
    sc.label(add(GPOS, d(90 + PSI / 2), 0.55), "ψ", "GREEN", "middle", 17, dx=-12, dy=-4)
    # dimensions: 3R and R on the upper-right side of the line of centres, 4R on the lower-left side
    n = (math.cos(PS), math.sin(PS))
    for p, q, off, nm, nmoff in ((O, CPOS, 0.40, "3R", (24, 6)), (CPOS, GPOS, 0.40, "R", (22, 4)), (O, GPOS, -1.65, "4R", (-26, 0))):
        pa, qa = add(p, n, off), add(q, n, off)
        sc.dim(pa, qa, nm, off=nmoff)
        sgn = 1.0 if off > 0 else -1.0
        sc.dashed(p, add(p, n, off + 0.1 * sgn))
        sc.dashed(q, add(q, n, off + 0.1 * sgn))
    # points
    sc.mass(CPOS, None, r=4.5, col="ACC")
    sc.label(CPOS, "C", "HEAD", "middle", 17, dx=-16, dy=-10)
    sc.mass(GPOS, None, r=4.5, col="BLUE")
    sc.label(GPOS, "G", "HEAD", "middle", 17, dx=-4, dy=26)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.label(O, K0 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=-34)
    return sc


# ------------------------------------------------------------------------------------------------ rb37-rot-phi
@figure("rb37-rot-phi",
        "The body basis of the disk turned clockwise by phi from the line GC.",
        r"The body basis is turned by $\phi$ about $-\mathbf k_0$ (⊗) from $\mathcal B_1$, so the disk has turned by "
        r"$\psi - \phi$ in $S_0$; rolling gives $\phi = -3\psi$.")
def rot_phi():
    ang = -60.0
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    sc = Scene(860, 760, (430, 370), 170)
    O = (0.0, 0.0)
    sc.poly(circle_pts(O, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.08)
    fixed_axis(sc, O, 0, 1.62, I1, off=(16, 6))
    fixed_axis(sc, O, 90, 1.62, J1, off=(16, 4))
    tri_pair(sc, O, 0, ang, IB, JB, "φ", col="BLUE", off1=(24, 10), off2=(18, -12))
    # leg labels: the triangle of i_b lies below the axis i1, that of j_b to the right of the axis j1
    sc.label((c * 0.66, 0.0), "cos φ", "TEXT", "middle", 14, dy=17)
    sc.label((c, s * 0.62), "sin φ", "TEXT", "start", 14, dx=9, dy=5)
    sc.label((0.0, c / 2), "cos φ", "TEXT", "end", 14, dx=-9, dy=5)
    sc.label((-s / 2, c), "sin φ", "TEXT", "middle", 14, dy=-8)
    sc.label(add(O, d(ang), 0.55), "1", "TEXT", "middle", 14, dx=-14, dy=4)
    sc.label(add(O, d(ang + 90), 0.7), "1", "TEXT", "middle", 14, dx=-6, dy=-10)
    sc.label(add(O, d(-42.0), 0.40), "φ", "GREEN", "middle", 17, dx=2, dy=6)
    sc.label(add(O, d(62.0), 0.36), "φ", "GREEN", "middle", 17, dx=0, dy=6)
    sc.mass((0.0, 1.0), None, r=5, col="ACC")
    sc.label((0.0, 1.0), "C", "HEAD", "middle", 17, dx=-16, dy=-6)
    p = d(ang)
    sc.mass(p, None, r=5, col="ACC")
    sc.label(p, "P", "HEAD", "end", 17, dx=-14, dy=6)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "G", "HEAD", "middle", 17, dx=-14, dy=24)
    sc.label(O, K0 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-40, dy=26)
    sc.note((-2.1, -1.55), "φ turns clockwise: rotation about −" + K0 + " (⊗)", "TEXT", "start", 14)
    return sc


# ------------------------------------------------------------------------------------------------ rb37-fbd
@figure("rb37-fbd",
        "Free-body diagram of the disk: weight, repulsion from A at P, and the normal reaction and friction of the cylinder at C.",
        r"Free-body diagram. The normal reaction pushes the disk away from $O$ and can only be positive; the repulsion "
        r"$k\,\overrightarrow{AP}$ presses the disk against the cylinder.")
def fbd():
    sc = Scene(960, 1000, (400, 150), 120)
    O = (0.0, 0.0)
    G, C = GPOS, CPOS
    body = math.radians(4 * PSI)
    ibd = (math.cos(body), math.sin(body))
    P = add(G, ibd, R)
    A = (0.0, -6 * R)
    _cylinder(sc, faint=True)
    sc.poly(circle_pts(G, R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.10)
    # fixed point A and the line A-P
    sc.dashed(A, P)
    sc.mass(A, None, r=4.5, col="BLUE")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-16, dy=6)
    # arms from G to C and to P
    sc.dashed(G, P)
    sc.label(add(G, ibd, 0.55), R_IB, "TEXT", "end", 15, dx=-6, dy=-8)
    off = 0.30
    a, b = add(G, I1D, off), add(C, I1D, off)
    sc.dim(a, b, R_J1, off=(26, 6))
    sc.dashed(G, add(G, I1D, off + 0.08))
    # forces
    sc.vec(G, (G[0], G[1] - 1.5), None, "PINK", 3.2, head=12)
    sc.label((G[0], G[1] - 1.5), "mg", "PINK", "start", 17, weight="700", dx=8, dy=16)
    ap = (P[0] - A[0], P[1] - A[1])
    la = math.hypot(*ap)
    fdir = (ap[0] / la, ap[1] / la)
    sc.vec(P, add(P, fdir, 1.5), None, "PINK", 3.2, head=12)
    sc.label(add(P, fdir, 1.5), S("F", "P") + " = k AP", "PINK", "start", 17, weight="700", dx=8, dy=-4)
    sc.vec(C, add(C, J1D, -0.6), None, "GREEN", 3.2, head=12)
    sc.label(add(C, J1D, -0.6), "N", "GREEN", "start", 17, weight="700", dx=12, dy=8)
    sc.vec(C, add(C, I1D, 1.1), None, "GREEN", 3.2, head=12)
    sc.label(add(C, I1D, 1.1), "T", "GREEN", "start", 17, weight="700", dx=8, dy=-6)
    sc.spin(G, 0.40, 185, 255, "4" + dot2("ψ"), "GREEN", name_r=0.70)
    # points
    sc.mass(C, None, r=4.5, col="ACC")
    sc.label(C, "C", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.mass(P, None, r=4.5, col="ACC")
    sc.label(P, "P", "HEAD", "middle", 17, dx=-14, dy=-6)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=18, dy=22)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.label(O, K0 + " (⊙)", "HEAD", "start", 16, weight="700", dx=14, dy=-14)
    return sc


R_IB = "R " + IB
R_J1 = "R " + J1
