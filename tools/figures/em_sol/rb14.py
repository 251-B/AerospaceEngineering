"""Problem RB-14: thin semicircular arc rocking without slipping on a horizontal plane."""
import math

from figures.em_solutions import figure, right_angle, triangle
from figures.em_sol.rb01 import add, d, sub
from figures.em_sol.rb12 import ground_line, half_disc_points, plane_rotation
from figures.mech import S, Scene, bold

ORANGE = "ACC"
RR0 = S("R", "0")
RRG = S("R", "G")
R0 = 3.0
RG = 1.91
TH = 30.0
TR = math.radians(TH)
Q = (0.0, 0.0)
C0 = (0.0, R0)
G0 = (0.0, R0 - RG)
C = (-R0 * TR, R0)
P = (C[0], 0.0)
G = (C[0] + RG * math.sin(TR), C[1] - RG * math.cos(TR))


@figure("rb14-rotation",
        "The body basis of the arc turned counterclockwise by theta from the fixed basis.",
        r"Rotation about $\mathbf k$ (⊙) by $\theta$. A positive angle rolls the arc to the left, as in the figure of the "
        r"statement.")
def rotation():
    return plane_rotation(700, 600, (270, 500), 250, 30.0,
                          (bold("i"), bold("j"), S(bold("i"), "B"), S(bold("j"), "B")),
                          bold("k") + " (⊙)", ("θ", ""), ("ω = θ̇", -110, -5, 0.30))


def _arc_points(centre, a0, a1, n=96):
    """Lower semicircle of radius R0 about `centre` turned by TH: body angles a0..a1 (degrees)."""
    return half_disc_points(centre, R0, a0, a1, n)


def _scene():
    sc = Scene(900, 700, (470, 600), 100)
    ground_line(sc, -4.5, 3.7)
    return sc


@figure("rb14-geometry",
        "The semicircular arc in its rest position and after rolling by theta, with the contact point, the centre of mass "
        "and their displacements.",
        r"Main plane. The contact point stays below $C$ and travels $R_0\theta$; $G$ rises by $R_G(1 - \cos\theta)$ and "
        r"moves by $R_0\theta - R_G\sin\theta$ in the sense of rolling.")
def geometry():
    sc = _scene()
    # rest position, dashed grey
    sc.poly(_arc_points(C0, 180, 360), "EDGE", 1.6, "7 5")
    sc.dotp(C0, 3.0, "EDGE")
    sc.label(C0, S("C", "0"), "TEXT", "middle", 16, dx=16, dy=-8)
    sc.mass(G0, None, r=4.0, col="EDGE")
    sc.label(G0, S("G", "0"), "TEXT", "middle", 16, dx=-16, dy=-8)
    # displaced position, solid
    sc.poly(_arc_points(C, 180 + TH, 360 + TH), "HEAD", 2.8)
    sc.line(add(C, d(TH), -R0), add(C, d(TH), R0), "EDGE", 1.2, "3 4")
    # rolled lengths
    sc.line(Q, P, "GREEN", 4.5)
    sc.poly(_arc_points(C, 270, 270 + TH, 20), "GREEN", 4.5)
    sc.label(((Q[0] + P[0]) / 2, 0.0), S("x", "C") + " = −" + RR0 + "θ", "GREEN", "middle", 15, weight="700", dy=36)
    sc.label((-0.02, 0.42), "arc " + RR0 + "θ", "GREEN", "start", 15, weight="700", dx=26, dy=-4)
    # radius CP and the triangle of CG
    sc.dashed(C, P)
    foot = (C[0], G[1])
    triangle(sc, [C, foot, G], ORANGE, 0.28)
    sc.line(C, G, "ACC", 2.0)
    sc.dashed(foot, G)
    right_angle(sc, foot, 90, 0, 0.09)
    sc.label((C[0], (C[1] + foot[1]) / 2), RRG + " cos θ", "TEXT", "end", 14, dx=-9, dy=5)
    sc.label(((foot[0] + G[0]) / 2, foot[1]), RRG + " sin θ", "TEXT", "middle", 14, dy=-9)
    sc.label(((C[0] + G[0]) / 2, (C[1] + G[1]) / 2), RRG, "TEXT", "start", 14, dx=10, dy=-2)
    sc.label((C[0], 0.55), RR0, "TEXT", "start", 15, dx=9, dy=5)
    sc.arc(C, 0.80, -90, -90 + TH, "GREEN", 1.8, head=True)
    sc.label(add(C, d(-90 + TH / 2), 1.08), "θ", "GREEN", "middle", 17, dx=0, dy=6)
    # displacements of the centre of mass (short names here, definitions in the legend)
    yx = 0.72
    sc.dashed(G0, (G0[0], yx - 0.12))
    sc.dashed(G, (G[0], yx - 0.12))
    sc.dim((G[0], yx), (G0[0], yx), S("x", "CM"), off=(0, 20))
    xr = 0.5
    sc.dashed(G0, (xr + 0.12, G0[1]))
    sc.dashed(G, (xr + 0.12, G[1]))
    sc.dim((xr, G0[1]), (xr, G[1]), "", off=(0, 0))
    sc.label((xr, (G0[1] + G[1]) / 2), S("y", "CM"), "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((-4.3, 4.55), S("x", "CM") + " = " + RR0 + "θ − " + RRG + " sin θ   (to the left)", "TEXT", "start", 15)
    sc.label((-4.3, 4.25), S("y", "CM") + " = " + RRG + "(1 − cos θ)   (up)", "TEXT", "start", 15)
    for pt, nm, off in ((P, "P", (-4, 26)), (Q, "Q", (14, 26))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.mass(C, None, r=4.5, col="BLUE")
    sc.label(C, "C", "HEAD", "middle", 17, dx=-14, dy=-10)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=14, dy=-10)
    return sc


@figure("rb14-arc-element",
        "Mass element of the semicircular wire at angle alpha and the centre of mass on its axis of symmetry.",
        r"Arc element $dm = \lambda R_0\,d\alpha$ at the distance $R_0$ from $C$: it gives $I_C = MR_0^2$ and the centre "
        r"of mass at $R_G = 2R_0/\pi$ below $C$.")
def arc_element():
    sc = Scene(640, 470, (320, 130), 75)
    A = 55.0
    pts = [(R0 * math.cos(math.radians(t)), -R0 * math.sin(math.radians(t))) for t in range(0, 181, 2)]
    sc.poly(pts, "HEAD", 2.6)
    sc.line((-R0 - 0.3, 0.0), (R0 + 0.3, 0.0), "EDGE", 1.3, "5 4")
    sc.line((0.0, 0.0), (0.0, -R0 - 0.35), "EDGE", 1.3)
    # body basis at C
    sc.vec((0.0, 0.0), (1.0, 0.0), sub("i", "B"), "BLUE", 2.8, name_off=(16, 6), size=17, head=11)
    sc.vec((0.0, 0.0), (0.0, 1.0), sub("j", "B"), "BLUE", 2.8, name_off=(-14, -2), size=17, head=11)
    # element at alpha, drawn wider than d alpha
    a0, a1 = A - 4.5, A + 4.5
    el = [(R0 * math.cos(math.radians(t)), -R0 * math.sin(math.radians(t))) for t in [a0 + (a1 - a0) * i / 8 for i in range(9)]]
    sc.poly(el, "ACC", 7.0)
    pe = (R0 * math.cos(math.radians(A)), -R0 * math.sin(math.radians(A)))
    sc.dashed((0.0, 0.0), pe)
    sc.label((pe[0] / 2, pe[1] / 2), RR0, "TEXT", "start", 16, dx=8, dy=-2)
    sc.arc((0.0, 0.0), 1.0, 0, -A, "GREEN", 1.8, head=True)
    sc.label(add((0.0, 0.0), d(-A / 2), 1.28), "α", "GREEN", "middle", 17, dx=4, dy=6)
    sc.label(pe, "dm = (M/π) dα", "ACC", "start", 16, weight="700", dx=14, dy=22)
    # centre of mass
    Gp = (0.0, -RG)
    sc.mass(Gp, None, r=5, col="BLUE")
    sc.label(Gp, "G", "HEAD", "middle", 17, dx=-16, dy=18)
    sc.dim((-0.55, 0.0), (-0.55, -RG), RRG, off=(-24, 4))
    sc.dashed((0.0, 0.0), (-0.65, 0.0))
    sc.dashed(Gp, (-0.65, -RG))
    sc.mass((0.0, 0.0), None, r=4.5, col="BLUE")
    sc.label((0.0, 0.0), "C", "HEAD", "middle", 17, dx=-14, dy=-10)
    return sc


@figure("rb14-fbd",
        "Free-body diagram of the arc: weight at G, normal reaction and friction at the contact point.",
        r"Free-body diagram. The contact force acts at a body point at rest, so it does no work and the mechanical energy "
        r"is conserved.")
def fbd():
    sc = _scene()
    sc.poly(_arc_points(C, 180 + TH, 360 + TH), "HEAD", 2.8)
    sc.dashed(P, G)
    sc.vec(G, (G[0], G[1] - 0.95), "Mg", "PINK", 3.0, name_off=(-26, 6), size=17, head=12)
    sc.vec(P, (P[0], P[1] + 1.35), "N", "GREEN", 3.0, name_off=(-16, 4), size=17, head=12)
    sc.vec(P, (P[0] + 1.35, 0.0), "F", "GREEN", 3.0, name_off=(8, -12), size=17, head=12)
    sc.spin(C, 0.55, 140, 40, "θ̈", "GREEN", name_r=0.85)
    for pt, nm, off in ((P, "P", (-14, 24)), (G, "G", (-16, 4)), (C, "C", (-14, 22))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    return sc
