"""Problem 21: body at rest on the surface of a spinning spherical planet."""
import math

from figures.em_solutions import (axis_in, axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle,
                                  unit)
from figures.em_sol.rb01 import rotation_view
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

WT = 35.0            # drawn value of Omega t, degrees
LAT = 40.0           # drawn latitude, degrees


@figure("p21-top-view",
        "Equatorial plane seen from above the north pole with k0 = k1 out of the paper: inertial axes i0, j0 in grey, "
        "planet axes i1, j1 turned counter-clockwise by Omega t in blue, with the dashed right triangles of their "
        "components",
        r"View from above the north pole ($\mathbf k_0 = \mathbf k_1$ out of the paper, $\odot$). $\mathbf i_1$ is "
        r"$\mathbf i_0$ turned counter-clockwise by $\Omega t$ (legs $\cos\Omega t$, $\sin\Omega t$); $\mathbf j_1$ turns "
        r"the same angle from $\mathbf j_0$, so its opposite leg points along $-\mathbf i_0$")
def top_view():
    sc = Scene(540, 470, (275, 330), 220)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(WT)), math.sin(math.radians(WT))
    fixed_axis(sc, O, 0, 1.0, bold("i") + S("", "0"), off=(16, 6))
    fixed_axis(sc, O, 90, 1.0, bold("j") + S("", "0"), off=(16, 4))
    triangle(sc, [O, (c, 0.0), (c, s)], "BLUE", 0.10)
    triangle(sc, [O, (0.0, c), (-s, c)], "BLUE", 0.10)
    sc.dashed((c, 0.0), (c, s))
    sc.dashed((0.0, c), (-s, c))
    right_angle(sc, (c, 0.0), 180, 90, 0.05)
    right_angle(sc, (0.0, c), -90, 180, 0.05)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -6))
    unit(sc, O, WT + 90, 1.0, bold("j") + S("", "1"), off=(-14, -8))
    sc.angle(O, 0.30, 0, WT, "Ωt", name_r=0.43)
    sc.angle(O, 0.30, 90, 90 + WT, "Ωt", name_r=0.44)
    sc.label((c / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=22)
    sc.label((c, s * 0.35), "sin Ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-s / 2, c), "sin Ωt", "TEXT", "middle", 15, dy=-10)
    sc.label((0.0, c / 2), "cos Ωt", "TEXT", "start", 15, dx=8, dy=16)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-58, 4))
    return sc


@figure("p21-meridian",
        "Meridian plane of the body: planet of radius R with centre O, polar axis k1 up, i1 in the equatorial plane, "
        "body P at latitude lambda, right triangle OFP with legs R cos lambda and R sin lambda, the distance r_perp to "
        "the axis, the attraction towards O and the centrifugal force away from the axis",
        r"Meridian plane of the body ($\mathbf i_1$ right, $\mathbf k_1$ up, $\mathbf j_1$ into the paper, $\otimes$). "
        r"In the shaded right triangle $OFP$ the hypotenuse is $R$, the leg adjacent to $\lambda$ is $R\cos\lambda$ "
        r"along $\mathbf i_1$ and the opposite leg is $R\sin\lambda$ along $\mathbf k_1$. The centrifugal force "
        r"$m\Omega^2\mathbf r_\perp$ is horizontal, away from the axis; the attraction $-mg_p\mathbf e_r$ points to $O$")
def meridian():
    sc = Scene(640, 560, (290, 290), 200)
    O = (0.0, 0.0)
    t = math.radians(LAT)
    P = (math.cos(t), math.sin(t))
    F = (P[0], 0.0)
    sc.circle(O, 1.0, "HEAD", 3.0)
    fixed_axis(sc, (0.0, -1.2), 90, 2.45, "polar axis", off=(46, 0))
    fixed_axis(sc, (-1.2, 0.0), 0, 2.5, "equator", off=(-8, 22))
    spin_about_vertical(sc, (0.0, 1.1), 0.16, 0.05, "Ω")
    triangle(sc, [O, F, P])
    right_angle(sc, F, 180, 90, 0.05)
    sc.dashed(F, P)
    sc.line(O, P, "HEAD", 1.6)
    sc.angle(O, 0.26, 0, LAT, "λ", name_r=0.36)
    sc.label((0.3 * P[0], 0.3 * P[1]), "R", "TEXT", "end", 17, dx=-8, dy=-6)
    sc.label((F[0] * 0.62, 0.0), "R cos λ", "TEXT", "start", 15, dy=22)
    sc.label((F[0], P[1] / 2), "R sin λ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.dashed((0.0, P[1]), P)
    sc.label((P[0] / 2, P[1]), S("r", "⊥") + " = R cos λ", "TEXT", "middle", 15, dy=-9)
    unit(sc, O, 0, 0.28, bold("i") + S("", "1"), off=(-4, 22))
    unit(sc, O, 90, 0.28, bold("k") + S("", "1"), off=(-18, 4))
    axis_in(sc, (-0.55, -0.45), bold("j") + S("", "1"), "BLUE", off=(0, 30))
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    sc.vec(P, (P[0] - 0.36 * math.cos(t), P[1] - 0.36 * math.sin(t)), "−mg" + S("", "p") + bold("e") + S("", "r"),
           "PINK", 2.4, name_off=(-34, -14), size=15)
    sc.vec(P, (P[0] + 0.42, P[1]), S(bold("F"), "C"), "PINK", 2.4, name_off=(10, -10), size=16)
    unit(sc, P, LAT, 0.26, bold("e") + S("", "r"), "ACC", off=(8, -10))
    sc.mass(P, "P", r=7, name_off=(24, 22))
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


@figure("p21-local-basis",
        "Meridian view of the local basis e_r, e_n turned by the latitude from i1, k1, with the two unit right triangles",
        r"Rotation by $\lambda$ in the meridian plane ($-\mathbf j_1$ out of the paper). The triangle of $\mathbf e_n$ has "
        r"its opposite leg along $-\mathbf i_1$: the minus sign of $\mathbf e_n = -\sin\lambda\,\mathbf i_1 + "
        r"\cos\lambda\,\mathbf k_1$.")
def local_basis():
    def post(sc):
        sc.label((0.0, -0.42), "positive λ counterclockwise", "GREEN", "middle", 14, weight="700")
        x0, y0, dx, dy = 1.30, -0.45, 0.40, 0.19
        cells = (("cos λ", "−sin λ", "0"), ("0", "0", "−1"), ("sin λ", "cos λ", "0"))
        sc.label((x0 - 0.30, y0 - dy), "[" + S("", "1") + "R" + S("", "2") + "] =", "TEXT", "end", 16)
        for r, row in enumerate(cells):
            for c, t in enumerate(row):
                sc.label((x0 + c * dx + 0.04, y0 - r * dy), t, "TEXT", "middle", 15)
        top, bot = y0 + 0.16, y0 - 2 * dy - 0.08
        for xb, sg in ((x0 - 0.22, 1), (x0 + 2 * dx + 0.26, -1)):
            sc.poly([(xb + sg * 0.05, top), (xb, top), (xb, bot), (xb + sg * 0.05, bot)], "TEXT", 1.4)
        sc.note((x0 - 0.22, bot - 0.17), "columns: e_r, e_n, −j₁", "TEXT", "start", 13)
    return rotation_view(980, 720, (360, 450), 250, LAT, S(bold("i"), "1"), S(bold("k"), "1"),
                         S(bold("e"), "r") + " (local vertical)", S(bold("e"), "n") + " (towards the north)",
                         "−" + S(bold("j"), "1") + " (⊙)", ("λ", ""), col="ACC", tri="ACC", out_off=(-14, 5), post=post)


@figure("p21-fbd",
        "Free-body diagrams of a body at rest at the north pole and at the equator of the spinning planet, with the "
        "attraction, the contact force and the centrifugal force",
        r"At the pole the body is on the spin axis: the contact force balances the attraction alone, "
        r"$W_{pole} = mg_p$. At the equator the centrifugal force $m\Omega^2R$ takes away part of it, "
        r"$W_{eq} = m(g_p - \Omega^2R)$; the ratio 2 of the statement means $\Omega^2R = g_p/2$.")
def fbd():
    sc = Scene(1000, 760, (330, 420), 115)
    R = 1.6
    O = (0.0, 0.0)
    sc.disk(O, R, "EDGE", "EDGE", 0.14, 1.8)
    sc.line((0.0, -R - 0.35), (0.0, R + 1.55), "EDGE", 1.3, "10 3 2 3")
    spin_about_vertical(sc, (0.0, R + 1.62), 0.16, 0.05, "Ω")
    axis_in(sc, O, None, "BLUE", 8)
    sc.label(O, "O", "HEAD", "start", 17, dx=14, dy=-12)
    sc.label(O, S(bold("j"), "1") + " (⊗)", "BLUE", "start", 14, weight="700", dx=14, dy=22)
    g0 = (-2.5, -1.9)
    fixed_axis(sc, g0, 0, 0.5, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, g0, 90, 0.5, S(bold("k"), "1"), off=(0, -8))
    # body at the north pole
    top = (0.0, R)
    sc.poly([(-0.07, R - 0.07), (0.07, R - 0.07), (0.07, R + 0.07), (-0.07, R + 0.07)], "HEAD", 2.0, fill="ACC", close=True)
    sc.vec((0.12, R), (0.12, R - 0.8), None, "PINK", 2.8, head=11)
    sc.label((0.12, R - 0.8), "−m " + S("g", "p") + " " + S(bold("e"), "r"), "PINK", "start", 15, weight="700", dx=10, dy=6)
    sc.vec((-0.12, R + 0.1), (-0.12, R + 0.9), None, "PINK", 2.8, head=11)
    sc.label((-0.12, R + 0.9), S("N", "pole") + " = m " + S("g", "p") + " " + S(bold("k"), "1"), "PINK", "end", 15,
             weight="700", dx=-10, dy=-2)
    sc.label((0.0, R), "pole", "HEAD", "start", 16, dx=16, dy=-8)
    sc.note((0.35, R + 0.62), "on the axis: F_C = 0", "TEXT", "start", 13)
    # body at the equator
    sc.poly([(R - 0.07, -0.07), (R + 0.07, -0.07), (R + 0.07, 0.07), (R - 0.07, 0.07)], "HEAD", 2.0, fill="ACC", close=True)
    sc.vec((R - 0.1, -0.05), (R - 0.9, -0.05), None, "PINK", 2.8, head=11)
    sc.label((R - 0.9, -0.05), "−m " + S("g", "p") + " " + S(bold("i"), "1"), "PINK", "middle", 15, weight="700", dy=24)
    _dvec(sc, (R + 0.1, -0.05), (R + 0.5, -0.05), "PINK", 2.6)
    sc.label((R + 0.5, -0.05), S(bold("F"), "C") + " = m Ω² R " + S(bold("i"), "1") + " (inertia)", "PINK", "start", 15,
             weight="700", dx=10, dy=22)
    sc.vec((R + 0.1, 0.17), (R + 0.5, 0.17), None, "PINK", 2.8, head=11)
    sc.label((R + 0.5, 0.17), S("N", "eq") + " = m(" + S("g", "p") + " − Ω² R) " + S(bold("i"), "1"), "PINK", "start", 15,
             weight="700", dx=10, dy=-6)
    sc.label((R, 0.0), "equator", "HEAD", "middle", 16, dx=0, dy=-26)
    sc.note((R + 0.1, -0.95), "W_eq = W_pole / 2 when Ω² R = g_p / 2", "TEXT", "start", 14)
    sc.note((-1.0, -2.45), "body at rest in S₁: no Coriolis force; F_A = F_E = 0", "TEXT", "start", 14)
    return sc
