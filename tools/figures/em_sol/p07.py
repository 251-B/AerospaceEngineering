"""Problem 07: skater B towed by a vehicle A that turns on a circle; rotating frame Ox1y1 along OA."""
import math

from figures.em_sol.rb01 import rotation_view
from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

WT = 35.0            # drawn value of omega t, degrees
PSI = 50.0           # drawn value of psi, degrees (in the motion psi < 0; the formulas are the same)


@figure("p07-attitude",
        "Top view with k0 = k1 out of the paper: inertial axes i0 to the right and j0 up in grey, rotating axes i1 and "
        "j1 turned counter-clockwise by omega t in blue, with the dashed right triangles that give their components",
        r"View from $+\mathbf k_0$ ($\mathbf k_0 = \mathbf k_1$ out of the paper, $\odot$). $\mathbf i_1$ is "
        r"$\mathbf i_0$ turned counter-clockwise by $\omega t$: legs $\cos\omega t$ along $\mathbf i_0$ and "
        r"$\sin\omega t$ along $\mathbf j_0$. $\mathbf j_1$ turns the same angle from $\mathbf j_0$, so its opposite leg "
        r"$\sin\omega t$ points along $-\mathbf i_0$: hence $\mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0$")
def attitude():
    sc = Scene(520, 430, (250, 330), 230)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(WT)), math.sin(math.radians(WT))
    fixed_axis(sc, O, 0, 1.0, bold("i") + S("", "0"), off=(16, 6))
    fixed_axis(sc, O, 90, 1.15, bold("j") + S("", "0"), off=(16, 4))
    fixed_axis(sc, O, 180, 0.85, "−" + bold("i") + S("", "0"), off=(-4, -12), dashed=True)
    # right triangles of i1 and j1
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), (-s, c)], "BLUE", 0.10)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((0.0, c), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    i1 = unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -6))
    unit(sc, O, WT + 90, 1.0, bold("j") + S("", "1"), off=(-14, -8))
    sc.angle(O, 0.30, 0, WT, "ωt", name_r=0.42)
    sc.angle(O, 0.30, 90, 90 + WT, "ωt", name_r=0.43)
    sc.label((c / 2, 0.0), "cos ωt", "TEXT", "middle", 15, dy=22)
    sc.label((c, s / 2), "sin ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, c), "sin ωt", "TEXT", "middle", 15, dy=-10)
    sc.label((0.0, c / 2), "cos ωt", "TEXT", "start", 15, dx=8, dy=16)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-10, 30))
    sc.note((0.30, -0.24), "view from +k₀", "TEXT", "start", 13)
    return sc


@figure("p07-bar-plane",
        "Rotating plane Ox1y1: vehicle A at rest at distance a from O on the x1 axis, bar AB of length a at angle psi, "
        "the right triangle AFB with legs a cos psi and a sin psi, the dashed components of the position of B, the "
        "dashed circle of radius a around A that B can describe, and the bar basis u_AB, u_perp at B",
        r"Plane of $S_1$ ($\mathbf i_1$ along $OA$, $\mathbf k_1$ out of the paper). $\mathbf r_1^B = \overrightarrow{OA} + "
        r"\overrightarrow{AB}$: in the shaded right triangle $AFB$ the hypotenuse is $|AB| = a$, the leg adjacent to "
        r"$\psi$ is $a\cos\psi$ along $\mathbf i_1$ and the opposite leg is $a\sin\psi$ along $\mathbf j_1$. The dashed "
        r"circle is the path of $B$ relative to $S_1$; $\mathbf u_{AB}, \mathbf u_\perp$ in orange")
def bar_plane():
    sc = Scene(660, 525, (70, 300), 200)
    O = (0.0, 0.0)
    A = (1.0, 0.0)
    c, s = math.cos(math.radians(PSI)), math.sin(math.radians(PSI))
    B = (1.0 + c, s)
    F = (1.0 + c, 0.0)
    sc.arc(A, 1.0, 62, 352, "EDGE", 1.1, "5 4")
    fixed_axis(sc, (-0.15, 0.0), 0, 2.75, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.1), 90, 1.3, S("y", "1"), off=(14, 2))
    triangle(sc, [A, F, B])
    right_angle(sc, F, 180, 90, 0.06)
    sc.dashed(F, B)
    sc.rod(A, B, 3.5)
    sc.label(((A[0] + B[0]) / 2, (A[1] + B[1]) / 2), "a", "TEXT", "end", 17, dx=-10, dy=-4)
    sc.angle(A, 0.26, 0, PSI, "ψ", name_r=0.37)
    sc.label(((A[0] + F[0]) / 2, 0.0), "a cos ψ", "TEXT", "middle", 15, dy=22)
    sc.label((0.5, 0.0), "a", "TEXT", "middle", 16, dy=22)
    sc.label((F[0], s / 2), "a sin ψ", "TEXT", "start", 15, dx=10, dy=5)
    sc.dim((0.0, -0.28), (F[0], -0.28), "a(1 + cos ψ)", off=(0, 20))
    sc.dashed((0.0, -0.05), (0.0, -0.32))
    sc.dashed((F[0], -0.04), (F[0], -0.32))
    sc.dotp(A, 5.5)
    sc.label(A, "A", "HEAD", "end", 17, dx=-8, dy=-10)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=22)
    sc.label(F, "F", "HEAD", "start", 15, dx=8, dy=20)
    unit(sc, O, 0, 0.32, bold("i") + S("", "1"), off=(2, -12))
    unit(sc, O, 90, 0.32, bold("j") + S("", "1"), off=(-18, 6))
    unit(sc, B, PSI, 0.30, bold("u") + S("", "AB"), "ACC", off=(18, 2))
    unit(sc, B, PSI + 90, 0.30, bold("u") + S("", "⊥"), "ACC", off=(-14, -8))
    sc.mass(B, "B", r=7, name_off=(18, 16))
    return sc


PSI_V = 40.0         # drawn value of psi in the rotation view, degrees


def _dvec(sc, a, b, name, col, w=2.4, name_off=(8, -8), size=15, anchor="middle", head=10):
    """Dashed arrow (inertia force) from world point a to b with its label near the tip."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)
    if name:
        sc.label(b, name, col, anchor, size, weight="700", dx=name_off[0], dy=name_off[1])


@figure("p07-rotation-psi",
        "View along k1 of the bar basis u_AB, u_perp turned by psi from i1, j1, with the two unit right triangles and "
        "the change of basis matrix",
        r"Rotation by $\psi$ about $\mathbf k_1$ (out of the paper). The triangle of $\mathbf u_\perp$ has its opposite leg "
        r"along $-\mathbf i_1$: the minus sign of $\mathbf u_\perp = -\sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1$.")
def rotation_psi():
    def post(sc):
        sc.spin((0.0, 0.0), 0.24, 215, 320, "", "GREEN", name_r=0.34, size=14)
        sc.label((0.0, -0.40), "positive ψ about " + bold("k") + S("", "1"), "GREEN", "middle", 15, weight="700")
        # change of basis matrix, cell by cell
        x0, y0, dx, dy = 1.15, -0.45, 0.34, 0.19
        cells = (("cos ψ", "−sin ψ", "0"), ("sin ψ", "cos ψ", "0"), ("0", "0", "1"))
        sc.label((x0 - 0.30, y0 - dy), "[" + S("", "1") + "R" + S("", "2") + "] =", "TEXT", "end", 16)
        for r, row in enumerate(cells):
            for c, t in enumerate(row):
                sc.label((x0 + c * dx + 0.04, y0 - r * dy), t, "TEXT", "middle", 15)
        top, bot = y0 + 0.16, y0 - 2 * dy - 0.08
        for xb, sg in ((x0 - 0.22, 1), (x0 + 2 * dx + 0.26, -1)):
            sc.poly([(xb + sg * 0.05, top), (xb, top), (xb, bot), (xb + sg * 0.05, bot)], "TEXT", 1.4)
        sc.note((-0.9, -0.95), "in the motion ψ < 0: u_AB lies below i₁", "TEXT", "start", 13)
    sc = rotation_view(900, 700, (270, 440), 250, PSI_V, S(bold("i"), "1"), S(bold("j"), "1"),
                       S(bold("u"), "AB"), S(bold("u"), "⊥"), S(bold("k"), "1") + " (⊙)", ("ψ", ""),
                       col="ACC", tri="ACC", out_off=(-14, 5), post=post)
    return sc


@figure("p07-fbd",
        "Free-body diagram of the skater in the rotating frame with the bar force towards the vehicle, the centrifugal "
        "force away from O, the Coriolis force along the bar and the vertical weight and reaction",
        r"Forces on $B$ in $S_1$: the bar force $-T\,\mathbf u_{AB}$, the centrifugal force $m\omega^2\mathbf r_1^B$ away "
        r"from $O$ and the Coriolis force $2ma\omega\dot\psi\,\mathbf u_{AB}$, which points towards $A$ because "
        r"$\dot\psi \lt 0$; weight and reaction are normal to the plane of the drawing.")
def fbd():
    sc = Scene(1000, 720, (150, 300), 140)
    a, ps = 1.6, math.radians(-50.0)
    O, A = (0.0, 0.0), (a, 0.0)
    B = (a + a * math.cos(ps), a * math.sin(ps))
    uab = (math.cos(ps), math.sin(ps))
    upe = (-math.sin(ps), math.cos(ps))
    sc.circle(A, a, "EDGE", 1.2, "6 5")
    sc.note((0.6, 1.82), "path of B in S₁ (circle of radius a about A)", "TEXT", "start", 13)
    sc.rod(A, B, 4.0)
    sc.dashed(O, B)
    sc.label((B[0] / 2, B[1] / 2), S(bold("r"), "1", "B"), "TEXT", "end", 16, dx=-4, dy=-10)
    x, y = sc.P(O)
    sc.c.add(f'<path d="M{x-6:.1f},{y-6:.1f} L{x+6:.1f},{y+6:.1f} M{x-6:.1f},{y+6:.1f} L{x+6:.1f},{y-6:.1f}" stroke="HEAD" '
             f'stroke-width="2" fill="none"/>')
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=-8)
    ax_, ay_ = sc.P(A)
    sc.c.add(f'<rect x="{ax_-6:.1f}" y="{ay_-6:.1f}" width="12" height="12" fill="HEAD"/>')
    sc.label(A, "A (at rest in S₁)", "HEAD", "middle", 15, dy=-14)
    g0 = (-0.55, 0.95)
    fixed_axis(sc, g0, 0, 0.5, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, g0, 90, 0.5, S(bold("j"), "1"), off=(0, -8))
    axis_out(sc, g0, None, "HEAD", 7)
    sc.label(g0, S(bold("k"), "1") + " (⊙)", "HEAD", "end", 14, weight="700", dx=-12, dy=5)
    unit(sc, B, -50.0, 0.5, S(bold("u"), "AB"), "ACC", off=(-4, 20))
    unit(sc, B, 40.0, 0.5, S(bold("u"), "⊥"), "ACC", off=(14, -4))
    tip_t = (B[0] - 0.9 * uab[0], B[1] - 0.9 * uab[1])
    sc.vec(B, tip_t, None, "PINK", 2.8, head=11)
    sc.label(tip_t, "−T " + S(bold("u"), "AB"), "PINK", "end", 15, weight="700", dx=-8, dy=-2)
    o2 = (upe[0] * 0.14, upe[1] * 0.14)
    b2 = (B[0] + o2[0], B[1] + o2[1])
    t2 = (b2[0] - 0.7 * uab[0], b2[1] - 0.7 * uab[1])
    _dvec(sc, b2, t2, None, "PINK", 2.4)
    sc.label(t2, S(bold("F"), "COR") + " = 2maωψ̇ " + S(bold("u"), "AB") + " (inertia)", "PINK", "start", 14,
             weight="700", dx=10, dy=-6)
    ang = math.atan2(B[1], B[0])
    fc = (B[0] + 1.0 * math.cos(ang), B[1] + 1.0 * math.sin(ang))
    _dvec(sc, B, fc, None, "PINK", 2.6)
    sc.label(fc, S(bold("F"), "C") + " = mω² " + S(bold("r"), "1", "B") + " (inertia)", "PINK", "start", 14,
             weight="700", dx=10, dy=6)
    vt = (B[0] - 0.6 * upe[0], B[1] - 0.6 * upe[1])
    sc.vec(B, vt, None, "GREEN", 2.4)
    sc.label(vt, S(bold("v"), "1", "B") + " = aψ̇ " + S(bold("u"), "⊥"), "GREEN", "end", 14, weight="700", dx=-6, dy=16)
    sc.mass(B, "B", r=7, name_off=(20, -2))
    px, py = (3.1, -2.2)
    axis_out(sc, (px, py), None, "PINK", 8)
    sc.label((px, py), "N " + S(bold("k"), "1"), "PINK", "start", 15, weight="700", dx=16, dy=5)
    axis_in(sc, (px, py - 0.32), None, "PINK", 8)
    sc.label((px, py - 0.32), "m g (weight)", "PINK", "start", 15, weight="700", dx=16, dy=5)
    sc.note((px - 0.12, py - 0.68), "both act on B, normal to the paper: N = m g", "TEXT", "start", 13)
    sc.note((-0.5, -2.5), "F_A = 0 (O fixed), F_E = 0 (ω constant)", "TEXT", "start", 14)
    return sc
