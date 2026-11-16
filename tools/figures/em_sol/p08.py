"""Problem 08: train A on a straight track and train B on a circular track of radius R (Case 2)."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

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


@figure("p08-parallel",
        "Two parallel straight tracks at the distance a with trains A and B, their velocities along i0 and the relative "
        "position from A to B",
        r"Case 1. Both observers translate with the basis $\mathcal B_0$: the relative position $\mathbf r_A^B$ keeps the "
        r"component $a$ across the tracks, and only its component along $\mathbf i_0$ changes, at the rate $v_B - v_A$.")
def parallel():
    sc = Scene(780, 520, (110, 330), 150)
    a, xa, xb = 1.0, 1.2, 2.6
    A, B = (xa, 0.0), (xb, a)
    sc.line((-0.6, 0.0), (4.3, 0.0), "HEAD", 3.5)
    sc.line((-0.6, a), (4.3, a), "HEAD", 3.5)
    sc.label((4.3, 0.0), "track of A", "TEXT", "end", 15, dy=22)
    sc.label((4.3, a), "track of B", "TEXT", "end", 15, dy=-12)
    fixed_axis(sc, (0.0, 0.0), 0, 0.5, S(bold("i"), "0"), off=(4, 22))
    fixed_axis(sc, (0.0, 0.0), 90, 0.5, S(bold("j"), "0"), off=(-14, 4))
    axis_out(sc, (0.0, 0.0), None, "HEAD", 8)
    sc.label((0.0, 0.0), S(bold("k"), "") + " (⊙)", "HEAD", "middle", 14, weight="700", dx=-2, dy=44)
    sc.label((0.0, 0.0), "O", "HEAD", "end", 16, dx=-14, dy=22)
    sc.dim((-0.42, 0.0), (-0.42, a), "a", off=(-14, 5))
    # relative position A -> B with its components
    sc.vec(A, B, None, "ACC", 3.0, head=12)
    sc.label(((xa + xb) / 2, a / 2), S(bold("r"), "A", "B"), "ACC", "end", 18, weight="700", dx=-14, dy=-8)
    sc.dashed((xb, 0.0), B)
    sc.label((xb, a / 2), "a", "TEXT", "start", 16, dx=10, dy=5)
    sc.dashed((xa, -0.30), (xa, -0.62))
    sc.dashed((xb, -0.05), (xb, -0.62))
    sc.dim((xa, -0.55), (xb, -0.55), "x" + S("", "B0") + " + (v" + S("", "B") + " − v" + S("", "A") + ") t", off=(0, 22))
    sc.dotp(A, 6.0)
    sc.label(A, "A", "HEAD", "end", 18, dx=-10, dy=-10)
    sc.dotp(B, 6.0)
    sc.label(B, "B", "HEAD", "start", 18, dx=-18, dy=-26)
    sc.vec((xa, -0.14), (xa + 0.9, -0.14), S(bold("v"), "A") + " " + S(bold("i"), "0"), "GREEN", 2.6, name_off=(8, 22), size=15)
    sc.vec((xb, a - 0.14), (xb + 1.3, a - 0.14), S(bold("v"), "B") + " " + S(bold("i"), "0"), "GREEN", 2.6, name_off=(8, 22),
           size=15)
    sc.note((-0.4, -1.1), "frames S_A and S_B translate with the basis B₀ (no rotation)", "TEXT", "start", 14)
    return sc


@figure("p08-observer-b",
        "Train A seen from train B: the relative position from B to A and its components x and y along the tangent and "
        "the inward normal of the circular track",
        r"Frame of train $B$ ($\mathbf k$ out of the paper). The components $x = \mathbf r_B^A\cdot\mathbf i_B$ and "
        r"$y = \mathbf r_B^A\cdot\mathbf j_B$ are the legs of the shaded right triangle whose hypotenuse is "
        r"$\mathbf r_B^A$; their time derivatives are the velocity of $A$ seen by the observer on $B$.")
def observer_b():
    sc = Scene(860, 640, (230, 540), 190)
    R, a = 1.6, 0.45
    C = (0.0, R + a)
    t = math.radians(TH)
    B = (R * math.sin(t), R + a - R * math.cos(t))
    A = (1.9, 0.0)
    ib = (math.cos(t), math.sin(t))
    jb = (-math.sin(t), math.cos(t))
    rx, ry = A[0] - B[0], A[1] - B[1]
    x = rx * ib[0] + ry * ib[1]
    y = rx * jb[0] + ry * jb[1]
    F1 = (B[0] + x * ib[0], B[1] + x * ib[1])
    F2 = (B[0] + y * jb[0], B[1] + y * jb[1])
    sc.line((-0.7, 0.0), (2.6, 0.0), "HEAD", 3.5)
    sc.label((-0.7, 0.0), "track of A", "TEXT", "start", 15, dy=24)
    sc.curve(lambda u: (R * math.sin(u), R + a - R * math.cos(u)), 0.0, math.radians(70), 60, "HEAD", 3.5)
    sc.label((R * math.sin(math.radians(70)), R + a - R * math.cos(math.radians(70))), "track of B", "TEXT", "end", 15,
             dx=-10, dy=-4)
    sc.dashed(B, C)
    sc.dotp(C, 4.5)
    sc.label(C, "C", "HEAD", "end", 17, dx=-10, dy=-8)
    sc.label((0.0, 0.0), "O", "HEAD", "end", 16, dx=-8, dy=22)
    # grey reference axes through B
    sc.line((B[0] - 0.55, B[1]), (B[0] + 0.62, B[1]), "EDGE", 1.1, "5 4")
    sc.line((B[0], B[1] - 0.12), (B[0], B[1] + 0.5), "EDGE", 1.1, "5 4")
    sc.label((B[0] + 0.62, B[1]), S(bold("i"), "0"), "TEXT", "start", 14, weight="700", dx=4, dy=5)
    sc.label((B[0], B[1] + 0.5), S(bold("j"), "0"), "TEXT", "middle", 14, weight="700", dy=-6)
    # triangle and projections
    triangle(sc, [B, F1, A], "ACC", 0.18)
    sc.dashed(A, F1)
    sc.dashed(A, F2)
    sc.line(B, F2, "EDGE", 1.1, "5 4")
    right_angle(sc, F1, TH + 180.0, TH - 90.0, 0.05)
    right_angle(sc, F2, TH + 90.0, TH, 0.05)
    sc.vec(B, A, None, "ACC", 3.0, head=12)
    sc.label(((B[0] + A[0]) / 2, (B[1] + A[1]) / 2), S(bold("r"), "B", "A"), "ACC", "start", 18, weight="700", dx=12, dy=-6)
    n = (-jb[0] * 0.07, -jb[1] * 0.07)
    sc.line((B[0] + n[0], B[1] + n[1]), (F1[0] + n[0], F1[1] + n[1]), "ACC", 2.4, "4 3")
    sc.label((B[0] + n[0] * 1.5, B[1] + n[1] * 1.5), "x", "ACC", "middle", 16, dx=-6, dy=36)
    sc.label(F2, "x = " + S(bold("r"), "B", "A") + " · " + S(bold("i"), "B") + " (the short legs)", "ACC", "end", 15, dx=24, dy=26)
    sc.label(((B[0] + F2[0]) / 2, (B[1] + F2[1]) / 2), "y = " + S(bold("r"), "B", "A") + " · " + S(bold("j"), "B")
             + " (negative here)", "ACC", "end", 15, dx=-12, dy=6)
    # basis and velocity of B
    unit(sc, B, TH, 0.7, S(bold("i"), "B"), "BLUE", off=(14, -4))
    unit(sc, B, TH + 90, 0.7, S(bold("j"), "B"), "BLUE", off=(-14, -4))
    o = (jb[0] * 0.10, jb[1] * 0.10)
    sc.vec((B[0] + o[0], B[1] + o[1]), (B[0] + o[0] + 0.9 * ib[0], B[1] + o[1] + 0.9 * ib[1]), None, "GREEN", 2.4)
    sc.label((B[0] + o[0] + 0.9 * ib[0], B[1] + o[1] + 0.9 * ib[1]), S(bold("v"), "B") + " " + S(bold("i"), "B"), "GREEN",
             "start", 15, weight="700", dx=8, dy=-8)
    sc.spin(B, 0.30, 142, 178, "", "GREEN", name_r=0.4)
    sc.label((B[0] - 0.36, B[1] + 0.16), "ω" + S("", "B") + " = v" + S("", "B") + " / R (S" + S("", "B") + " turns)", "GREEN",
             "end", 15, weight="700", dx=-6, dy=-8)
    sc.mass(B, "B", r=7, name_off=(-30, -16))
    sc.mass(A, "A", r=7, name_off=(0, 26))
    axis_out(sc, (-0.45, 0.35), None, "HEAD", 8)
    sc.label((-0.45, 0.35), S(bold("k"), "") + " (⊙)", "HEAD", "end", 14, weight="700", dx=-12, dy=5)
    return sc
