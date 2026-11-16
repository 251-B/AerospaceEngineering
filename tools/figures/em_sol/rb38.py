"""Problem RB-38: axisymmetric body on a hanging axle, string OA, centre of mass G guided on the vertical through O."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb06 import rlabel, rotation_view2
from figures.mech import S, Scene, bold

TH = 110.0
H = TH / 2.0
CH, SH = math.cos(math.radians(H)), math.sin(math.radians(H))


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _ceiling(sc, p, half=0.7):
    sc.ground((p[0] - half, p[1]), (p[0] + half, p[1]), side=1)


@figure("rb38-triangle",
        "Isosceles triangle formed by the string, the body axis and the vertical through O, split into two right "
        "triangles.",
        r"The altitude $AM$ splits the isosceles triangle $OAG$ into two right triangles with hypotenuse $\ell$ and "
        r"angle $\theta/2$ at $A$: $OG = 2\ell\sin\tfrac{\theta}{2}$ and the axis $AG$ descends at $\theta/2$ below the "
        r"horizontal.")
def triangle_fig():
    sc = Scene(680, 560, (330, 110), 200)
    O = (0.0, 0.0)
    G = (0.0, -2 * SH)
    M = (0.0, -SH)
    A = (-CH, -SH)
    _ceiling(sc, O)
    triangle(sc, [A, M, O], "ACC", 0.22)
    triangle(sc, [A, M, G], "BLUE", 0.22)
    sc.line(O, G, "EDGE", 1.1, "5 4")
    sc.line(A, M, "EDGE", 1.3, "6 4")
    right_angle(sc, M, 180, 90, 0.07)
    right_angle(sc, M, 180, 270, 0.07)
    sc.line(O, A, "HEAD", 1.6)
    sc.line(A, G, "HEAD", 5.0)
    # angles at A
    sc.arc(A, 0.20, 0, H, "GREEN", 1.5)
    sc.arc(A, 0.20, -H, 0, "GREEN", 1.5)
    sc.label(add(A, d(H / 2), 0.20), "θ/2", "GREEN", "start", 14, dx=-4, dy=-8)
    sc.label(add(A, d(-H / 2), 0.20), "θ/2", "GREEN", "start", 14, dx=-4, dy=20)
    sc.arc(A, 0.34, -H, H, "GREEN", 1.7, head=True)
    sc.label(add(A, d(0), 0.34), "θ", "GREEN", "start", 17, dx=6, dy=-6)
    # labels
    sc.label(add(O, A, 0.5), "ℓ", "TEXT", "end", 17, dx=-10, dy=-4)
    sc.label(((A[0] + G[0]) / 2, (A[1] + G[1]) / 2), "ℓ", "TEXT", "start", 17, dx=14, dy=-8)
    sc.label((0.0, -SH / 2), "ℓ sin(θ/2)", "TEXT", "start", 14, dx=10, dy=5)
    sc.label((0.0, -SH - SH / 2), "ℓ sin(θ/2)", "TEXT", "start", 14, dx=10, dy=5)
    sc.dim((0.62, 0.0), (0.62, -2 * SH), "")
    sc.label((0.62, -SH), "OG = 2ℓ sin(θ/2)", "TEXT", "start", 14, dx=10, dy=5)
    yd = -2 * SH - 0.28
    sc.line((A[0], A[1] - 0.06), (A[0], yd - 0.06), "EDGE", 0.9, "3 3")
    sc.line((0.0, yd + 0.20), (0.0, yd - 0.06), "EDGE", 0.9, "3 3")
    sc.dim((A[0], yd), (0.0, yd), "")
    sc.label((-CH / 2, yd), "ℓ cos(θ/2)", "TEXT", "middle", 14, dy=22)
    sc.line((A[0] - 0.45, A[1]), A, "EDGE", 1.1, "4 3")
    sc.note((A[0] - 0.05, A[1]), "axis descends at θ/2", "GREEN", "end", 13, dx=-8, dy=28)
    # points
    sc.mass(O, None, r=5, col="HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.mass(G, None, r=5, col="HEAD")
    sc.label(G, "G", "HEAD", "middle", 17, dx=16, dy=18)
    sc.mass(A, None, r=5, col="HEAD")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-4, dy=-14)
    sc.dotp(M, 3.5)
    sc.label(M, "M", "HEAD", "middle", 17, dx=14, dy=-14)
    sc.gravity((-1.4, -0.1), 0.45, "g")
    return sc


@figure("rb38-psi",
        "Rotation by psi about the vertical, from the plane Oy0z0 to the plane OAG, seen from above.",
        r"$\mathcal B_1$ is $\mathcal B_0$ turned by $\psi$ about $\mathbf k_0$ (⊙); $\mathbf j_1$ leans to negative "
        r"$\mathbf i_0$ (minus sign). The plane $OAG$ contains $\mathbf j_1$ and $\mathbf k_1$.")
def rotation_psi():
    psi = 35.0

    def pre(sc):
        a = math.radians(psi + 90)
        t = (math.cos(a), math.sin(a))
        sc.line((-1.2 * t[0], -1.2 * t[1]), (1.5 * t[0], 1.5 * t[1]), "GREEN", 2.2, "9 5")
        sc.line((0.0, 0.0), (0.0, -1.0), "EDGE", 1.4, "7 4")

    def post(sc):
        a = math.radians(psi + 90)
        sc.note((1.5 * math.cos(a), 1.5 * math.sin(a)), "plane OAG", "GREEN", "end", 14, dx=-18, dy=-4)
        sc.note((0.0, -1.0), "plane Oy0z0", "TEXT", "start", 13, dx=12, dy=4)

    return rotation_view2(660, 560, (300, 360), 150, psi, _ax("i", "0"), _ax("j", "0"), _ax("i", "1"), _ax("j", "1"),
                          _ax("k", "0") + " = " + _ax("k", "1") + " (⊙) at O", ("ψ", ""), pre=pre, post=post,
                          out_off=(-16, 28), arc_r=0.30, cy=0.72, lab_r=0.50, m2_off=(-30, 4))


@figure("rb38-tilt",
        "Tilt of the axle frame by minus half the angle theta about the normal to the plane OAG.",
        r"$\mathcal B_2$ is $\mathcal B_1$ turned clockwise by $\theta/2$ about $\mathbf i_1$ (⊙), so that $\mathbf j_2$ "
        r"lies along $AG$: $\mathbf j_2 = \cos\tfrac{\theta}{2}\mathbf j_1 - \sin\tfrac{\theta}{2}\mathbf k_1$.")
def rotation_tilt():
    def pre(sc):
        a = math.radians(-H)
        sc.line((-1.35 * math.cos(a), -1.35 * math.sin(a)), (0.0, 0.0), "HEAD", 5.0)

    def post(sc):
        sc.note((-1.75, -0.75), "rotation by −θ/2 about i_1", "TEXT", "start", 13)
        sc.note((-1.5 * math.cos(math.radians(-H)), -1.5 * math.sin(math.radians(-H))), "A", "HEAD", "end", 17, dx=-4, dy=-4)

    return rotation_view2(700, 600, (400, 300), 160, -H, _ax("j", "1"), _ax("k", "1"), _ax("j", "2"), _ax("k", "2"),
                          _ax("i", "1") + " = " + _ax("i", "2") + " (⊙) at G", ("θ/2", ""), pre=pre, post=post,
                          out_off=(-16, 28), arc_r=0.28, cy=0.8, lab_r=0.55, side="right", jlab=(62, 0.36))


@figure("rb38-spin",
        "Spin rotation by phi about the symmetry axis of the body.",
        r"Spin: $\mathcal B_b$ is $\mathcal B_2$ turned by $\varphi$ about $\mathbf j_2$ (⊙, with $\mathbf k_2$ to the "
        r"right and $\mathbf i_2$ up); $\mathbf i_b$ leans to negative $\mathbf k_2$.")
def rotation_spin():
    def pre(sc):
        sc.circle((0.0, 0.0), 1.2, "EDGE", 1.4, fill="HEAD", opacity=0.05)

    return rotation_view2(700, 640, (350, 340), 160, 30.0, _ax("k", "2"), _ax("i", "2"), _ax("k", "b"), _ax("i", "b"),
                          _ax("j", "2") + " = " + _ax("j", "b") + " (⊙) at G", ("φ", ""), pre=pre, out_off=(-16, 28),
                          arc_r=0.34, cy=0.72, lab_r=0.52)


@figure("rb38-fbd",
        "Free-body diagram of the hanging axisymmetric body with the string tension, its weight and the guide "
        "reaction.",
        r"Free-body diagram: weight and the horizontal guide reaction at $G$, tension $T\,\mathbf e_{AO}$ at $A$. About "
        r"$G$ only the tension has a moment, with arm $\ell\sin\theta$: $\mathbf M_G = -\ell T\sin\theta\,\mathbf i_2$.")
def fbd():
    sc = Scene(760, 600, (300, 90), 150)
    O = (0.0, 0.0)
    G = (0.0, -2 * SH)
    A = (-CH, -SH)
    u = (CH, SH)                                   # unit vector from A to O
    _ceiling(sc, O, 0.8)
    sc.line((0.0, 0.0), (0.0, -2 * SH - 0.75), "EDGE", 1.2, "10 4 2 4")
    # body: axle AG with the disk near G
    aG = (CH, -SH)                                 # j_2: from A towards G
    sc.line(add(A, aG, -0.0), add(G, aG, 0.30), "HEAD", 6.0)
    nrm = (SH, CH)                                 # normal to the axle in the plane
    dk = [add(add(G, aG, 0.08), nrm, 0.55), add(add(G, aG, 0.08), nrm, -0.55)]
    sc.line(dk[0], dk[1], "HEAD", 6.0)
    sc.poly([add(dk[0], aG, 0.10), add(dk[1], aG, 0.10), add(dk[1], aG, -0.10), add(dk[0], aG, -0.10)], "HEAD", 0.0,
            fill="HEAD", close=True, opacity=0.12)
    # perpendicular from G to the line AO
    t = ((G[0] - A[0]) * u[0] + (G[1] - A[1]) * u[1])
    F = add(A, u, t)
    sc.line(add(F, u, -0.05), add(A, u, 1.45), "EDGE", 1.2, "7 4")
    sc.line(G, F, "BLUE", 1.6, "6 4")
    q = 0.07
    a1 = (-u[0], -u[1])
    n1 = math.hypot(G[0] - F[0], G[1] - F[1])
    a2 = ((G[0] - F[0]) / n1, (G[1] - F[1]) / n1)
    sc.poly([add(F, a1, q), add(add(F, a1, q), a2, q), add(F, a2, q)], "EDGE", 1.1)
    sc.label(((G[0] + F[0]) / 2, (G[1] + F[1]) / 2), "ℓ sin θ", "BLUE", "end", 15, italic=False, dx=-6, dy=22)
    # arm G -> A
    off = (SH * 0.10, CH * 0.10)
    sc.vec(add(G, off), add(add(G, aG, -0.92), off), None, "BLUE", 2.4, head=10)
    sc.label(A, S(bold("r"), "G", "A") + " = −ℓ " + _ax("j", "2"), "BLUE", "end", 15, weight="700", dx=-10, dy=-24)
    # forces
    sc.vec(A, add(A, u, 0.62), None, "PINK", 3.6, head=13)
    sc.label(add(A, u, 0.62), "T " + _ax("e", "AO"), "PINK", "end", 17, weight="700", dx=-10, dy=-8)
    sc.vec(G, (G[0], G[1] - 0.9), "mg", "PINK", 3.6, name_off=(-22, 12), size=17, head=13)
    sc.vec(G, (G[0] - 0.55, G[1]), None, "PINK", 3.6, head=13)
    sc.label((G[0] - 0.55, G[1]), S("N", "2") + " " + _ax("j", "1"), "PINK", "end", 17, weight="700", dx=-10, dy=6)
    # normal component N_1 i_1 (out of the paper), found zero
    P1 = (G[0] + 0.22, G[1] + 0.78)
    axis_out(sc, P1, None, "HEAD")
    sc.label(P1, S("N", "1") + " " + _ax("i", "1") + " = 0 (⊙)", "HEAD", "start", 15, weight="700", dx=16, dy=5)
    # moment about G, clockwise in this view
    sc.spin(G, 0.52, 70, -80, "", "ACC")
    sc.label(add(G, d(-5), 0.52), S(bold("M"), "G") + " = −ℓ T sin θ " + _ax("i", "2"), "ACC", "start", 16, weight="700",
             dx=14, dy=34)
    # points
    sc.mass(O, None, r=5, col="HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.mass(A, None, r=5, col="HEAD")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-14, dy=6)
    sc.dotp(G, 4.5)
    sc.label(G, "G", "HEAD", "middle", 17, dx=14, dy=-12)
    return sc
