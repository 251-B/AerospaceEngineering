"""Problem 08: train A on a straight track and train B on a circular track of radius R (Case 2)."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

TH = 40.0            # drawn value of theta_B = omega_B t, degrees


@figure("p08-tracks",
        "Plane of the tracks seen from above: straight track of A along i0, circular track of radius R with centre C "
        "at height R + a, train B at the angle theta_B from the downward vertical, the right triangle CFB with legs "
        "R sin theta_B and R cos theta_B, and the basis i_B, j_B of the train",
        r"Plane of the tracks ($\mathbf k$ out of the paper). $\mathbf r_B = \overrightarrow{OC} + \overrightarrow{CB}$: in "
        r"the shaded right triangle $CFB$ the hypotenuse is $|CB| = R$, the leg opposite $\theta_B$ is $R\sin\theta_B$ "
        r"(along $\mathbf i_0$) and the adjacent leg is $R\cos\theta_B$ (along $-\mathbf j_0$). The tangent $\mathbf i_B$ "
        r"makes the same angle $\theta_B = \omega_B t$ with the horizontal; $\mathbf j_B$ points to $C$")
def tracks():
    sc = Scene(660, 590, (250, 520), 190)
    O = (0.0, 0.0)
    a, R = 0.45, 1.0
    C = (0.0, R + a)
    t = math.radians(TH)
    B = (R * math.sin(t), R + a - R * math.cos(t))
    F = (0.0, B[1])
    # tracks
    sc.line((-1.25, 0.0), (1.95, 0.0), "HEAD", 3.0)
    sc.circle(C, R, "HEAD", 2.6)
    fixed_axis(sc, O, 0, 0.55, bold("i") + S("", "0"), off=(4, 22))
    fixed_axis(sc, O, 90, 0.33, bold("j") + S("", "0"), off=(-16, 4))
    axis_out(sc, O, bold("k"), off=(-22, 24))
    sc.label(O, "O", "HEAD", "end", 17, dx=-30, dy=-6)
    # separation a
    sc.dashed((0.0, a), (-0.42, a))
    sc.dim((-0.36, 0.0), (-0.36, a), "a", off=(-14, 5))
    # key triangle C - F - B
    triangle(sc, [C, F, B])
    right_angle(sc, F, 0, 90, 0.05)
    sc.dashed(C, (0.0, a))
    sc.dashed(F, B)
    sc.line(C, B, "HEAD", 1.6)
    sc.label(((C[0] + B[0]) / 2, (C[1] + B[1]) / 2), "R", "TEXT", "start", 17, dx=10, dy=-4)
    sc.label(((C[0] + F[0]) / 2, (C[1] + F[1]) / 2), "R cos θ" + S("", "B"), "TEXT", "end", 15, dx=-8, dy=-6)
    sc.label(((F[0] + B[0]) / 2, F[1]), "R sin θ" + S("", "B"), "TEXT", "middle", 15, dy=-9)
    sc.angle(C, 0.22, -90, -90 + TH, "θ" + S("", "B"), name_r=0.33)
    sc.dashed(B, (B[0], 0.0))
    sc.label((B[0], B[1] * 0.45), "R + a − R cos θ" + S("", "B"), "TEXT", "start", 15, dx=8)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "end", 17, dx=-10, dy=-8)
    # train B and its basis
    sc.dashed(B, (B[0] + 0.42, B[1]))
    sc.angle(B, 0.24, 0, TH, "ω" + S("", "B") + "t", name_r=0.40)
    unit(sc, B, TH, 0.36, bold("i") + S("", "B"), off=(10, -8))
    unit(sc, B, TH + 90, 0.30, bold("j") + S("", "B"), off=(-22, 12))
    sc.mass(B, "B", r=7, name_off=(18, 24))
    # train A
    A = (1.35, 0.0)
    sc.mass(A, "A", r=7, name_off=(0, 26))
    sc.vec((1.35, 0.12), (1.78, 0.12), S(bold("v"), "A"), "TEXT", 2.2, name_off=(4, -12), size=16)
    return sc


@figure("p08-train-basis",
        "View from +k with k out of the paper: inertial axes i0 to the right and j0 up in grey, the basis i_B, j_B of "
        "train B turned counter-clockwise by omega_B t in blue, with the dashed right triangles of their components",
        r"View from $+\mathbf k$ ($\odot$). $\mathbf i_B$ is $\mathbf i_0$ turned counter-clockwise by $\omega_B t$: legs "
        r"$\cos\omega_B t$ along $\mathbf i_0$ and $\sin\omega_B t$ along $\mathbf j_0$. $\mathbf j_B$ turns the same "
        r"angle from $\mathbf j_0$, so its opposite leg $\sin\omega_B t$ points along $-\mathbf i_0$ (the minus sign "
        r"of $[{}_0R_B]$)")
def train_basis():
    sc = Scene(520, 430, (250, 330), 230)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(TH)), math.sin(math.radians(TH))
    w = "ω" + S("", "B") + "t"
    fixed_axis(sc, O, 0, 1.0, bold("i") + S("", "0"), off=(16, 6))
    fixed_axis(sc, O, 90, 1.15, bold("j") + S("", "0"), off=(16, 4))
    fixed_axis(sc, O, 180, 0.85, "−" + bold("i") + S("", "0"), off=(-4, -12), dashed=True)
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), (-s, c)], "BLUE", 0.10)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((0.0, c), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    unit(sc, O, TH, 1.0, bold("i") + S("", "B"), off=(14, -6))
    unit(sc, O, TH + 90, 1.0, bold("j") + S("", "B"), off=(-14, -8))
    sc.angle(O, 0.30, 0, TH, w, name_r=0.45)
    sc.angle(O, 0.30, 90, 90 + TH, w, name_r=0.46)
    sc.label((c / 2, 0.0), "cos " + w, "TEXT", "middle", 15, dy=22)
    sc.label((c, s / 2), "sin " + w, "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, c), "sin " + w, "TEXT", "middle", 15, dy=-10)
    sc.label((0.0, c / 2), "cos " + w, "TEXT", "start", 15, dx=8, dy=16)
    axis_out(sc, O, bold("k"), off=(-10, 30))
    sc.note((0.30, -0.24), "view from +k", "TEXT", "start", 13)
    return sc
