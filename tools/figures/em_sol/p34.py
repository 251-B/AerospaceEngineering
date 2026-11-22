"""Problem 34: bead on a circular wire through O whose vertical plane Oxy swings about Oy with Omega(t) = A w sin(wt)."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

PHI = math.radians(40)


@figure("p34-wire-plane",
        "Plane Oxy of the wire: the circle of centre C on the x axis at distance R from O, the particle P at angle phi from "
        "Ox, the right triangle C F P with legs R cos phi and R sin phi, the horizontal distance R(1 + cos phi) from the "
        "axis Oy, the basis i1, j1 at O with k1 out of the paper, and the polar basis e_r, e_phi at P",
        r"Plane $Oxy$, fixed in $S_1$ ($\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ points out of the paper, $\odot$). "
        r"$\overrightarrow{OC} = R\,\mathbf i_1$; in the shaded right triangle $CFP$ the hypotenuse is $|CP| = R$, the leg "
        r"adjacent to $\varphi$ is $R\cos\varphi$ (along $\mathbf i_1$) and the opposite leg is $R\sin\varphi$ (along "
        r"$\mathbf j_1$). The distance from $P$ to the rotation axis $Oy$ is $R(1 + \cos\varphi)$. $\mathbf i_1, \mathbf j_1$ "
        r"in blue, $\mathbf e_r, \mathbf e_\varphi$ in orange")
def wire_plane():
    sc = Scene(620, 520, (110, 280), 170)
    O = (0.0, 0.0)
    C = (1.0, 0.0)
    P = (1.0 + math.cos(PHI), math.sin(PHI))
    F = (P[0], 0.0)
    fixed_axis(sc, (-0.25, 0.0), 0, 2.65, "x", off=(12, 5))
    fixed_axis(sc, (0.0, -1.25), 90, 2.6, "y", off=(14, 4))
    spin_about_vertical(sc, (0.0, 1.18), 0.15, 0.045, "Ω(t)")
    sc.circle(C, 1.0, "HEAD", 3.0)
    triangle(sc, [C, F, P])
    right_angle(sc, F, 180, 90, 0.06)
    sc.line(C, P, "HEAD", 1.6)
    sc.label((C[0] + 0.35 * math.cos(PHI), 0.35 * math.sin(PHI)), "R", "TEXT", "end", 17, dx=-6, dy=-8)
    sc.angle(C, 0.24, 0, 40, "φ", name_r=0.36)
    sc.dashed(F, P)
    sc.dotp(F, 3.5)
    sc.label(F, "F", "HEAD", "start", 17, dx=9, dy=22)
    sc.label(((C[0] + F[0]) / 2, 0.0), "R cos φ", "TEXT", "middle", 15, dy=20)
    sc.label((P[0], P[1] / 2), "R sin φ", "TEXT", "start", 15, dx=40, dy=5)
    # horizontal distance from the rotation axis
    sc.dashed(P, (P[0], -1.18))
    sc.dim((0.0, -1.12), (P[0], -1.12), "R(1 + cos φ)", off=(0, 22), size=14)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "middle", 17, dx=-6, dy=22)
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=22)
    unit(sc, O, 0, 0.32, S(bold("i"), "1"), off=(0, 22))
    unit(sc, O, 90, 0.32, S(bold("j"), "1"), off=(-18, 4))
    axis_out(sc, O, S(bold("k"), "1"), col="BLUE", off=(-24, -12))
    unit(sc, P, 40, 0.30, S(bold("e"), "r"), "ACC", off=(12, -2))
    unit(sc, P, 130, 0.30, S(bold("e"), "φ"), "ACC", off=(-8, -12))
    sc.mass(P, "P", r=7, name_off=(24, 6))
    sc.gravity((2.35, 1.15), 0.32, "g")
    return sc


@figure("p34-top-view",
        "View from above with j out of the paper: the inertial axes i to the right and k down in grey, the axes i1 and k1 "
        "of the swinging plane turned counter-clockwise by psi in blue, the dashed components cos psi along i and sin psi "
        "along minus k, and the extreme position psi = 2A of the swing",
        r"View from $+y$, with $\mathbf j_0 = \mathbf j_1$ out of the paper ($\odot$): then "
        r"$\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ points down the page. $\mathbf i_1, \mathbf k_1$ are "
        r"$\mathbf i_0, \mathbf k_0$ turned counter-clockwise by $\psi(t) = A(1 - \cos\omega t)$; the legs of "
        r"$\mathbf i_1$ are $\cos\psi$ along $\mathbf i_0$ and $\sin\psi$ along $-\mathbf k_0$ (up the page), hence "
        r"$\mathbf i_1 = \cos\psi\,\mathbf i_0 - \sin\psi\,\mathbf k_0$. The plane swings between $\psi = 0$ and "
        r"$\psi = 2A$ (dotted)")
def top_view():
    sc = Scene(500, 440, (170, 215), 165)
    O = (0.0, 0.0)
    a = 30.0
    fixed_axis(sc, O, 0, 1.15, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, O, -90, 1.0, S(bold("k"), "0"), off=(14, 4))
    fixed_axis(sc, O, 90, 0.95, "−" + S(bold("k"), "0"), off=(20, 4), dashed=True)
    axis_out(sc, O, S(bold("j"), "0") + " = " + S(bold("j"), "1"), off=(-46, 24))
    e = (0.9 * math.cos(math.radians(52)), 0.9 * math.sin(math.radians(52)))
    sc.line(O, e, "EDGE", 1.0, "2 3")
    sc.label(e, "ψ = 2A", "TEXT", "start", 14, dx=6, dy=-4)
    i1 = unit(sc, O, a, 1.0, S(bold("i"), "1"), off=(14, 4))
    unit(sc, O, a - 90, 1.0, S(bold("k"), "1"), off=(16, 8))
    sc.angle(O, 0.30, 0, a, "ψ", name_r=0.42)
    sc.angle(O, 0.26, -90, a - 90, "ψ", name_r=0.38)
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos ψ", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, i1[1]), "sin ψ", "TEXT", "end", 15, dx=-12, dy=5)
    sc.note((-0.95, -0.95), "view from +y", "TEXT", "start", 13)
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


def _swing(sc, c, rx, ry, name):
    """Double-headed flat elliptical arc about a vertical axis (the swing of the plane) and its name."""
    x, y = sc.P(c)
    rxp, ryp = rx * sc.k, ry * sc.k
    p0 = (x - rxp, y)
    p1 = (x + rxp, y)
    sc.c.add(f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{rxp:.1f},{ryp:.1f} 0 0 0 {p1[0]:.1f},{p1[1]:.1f}" fill="none" '
             f'stroke="GREEN" stroke-width="1.8"/>')
    arrow_head(sc.c, (p1[0] - 8, p1[1] + ryp * 0.35), (p1[0] + 1, p1[1] - 1.0), "GREEN", 9)
    arrow_head(sc.c, (p0[0] + 8, p0[1] + ryp * 0.35), (p0[0] - 1, p0[1] - 1.0), "GREEN", 9)
    sc.label(c, name, "GREEN", "start", 16, weight="700", dx=rxp + 12, dy=-2)


PHI_F = math.radians(-60)               # position of the bead in the free-body diagram


@figure("p34-fbd",
        "Free-body diagram of the bead on the swinging circular wire: top, the plane of the wire with the weight, the "
        "radial reaction and the centrifugal force; bottom, the view from above with the Euler and Coriolis forces and "
        "the normal reaction",
        r"Forces on $P$ in $Oxyz$. In the plane of the wire: the weight, the reaction $N_1\,\mathbf e_r$ and the "
        r"centrifugal force along $\mathbf i_1$ (dashed). Seen from above: the Euler and Coriolis forces (dashed), both "
        r"along $\mathbf k_1$, balanced by the normal reaction $N_2\,\mathbf k_1$.")
def fbd():
    k = 170.0
    sc = Scene(700, 930, (110, 295), k)
    RY = -(715 - 295) / k                               # world y of the trace of the lower panel (pixel y = 655)
    O = (0.0, 0.0)
    C = (1.0, 0.0)
    c, s_ = math.cos(PHI_F), math.sin(PHI_F)
    P = (1.0 + c, s_)
    # ---- upper panel: plane Oxy, k1 out of the paper
    sc.line((0.0, -1.15), (0.0, 1.45), "EDGE", 1.4, "10 3 2 3")
    _swing(sc, (0.0, 1.25), 0.3, 0.07, "Ω(t)")
    sc.line((-0.3, 0.0), (2.4, 0.0), "EDGE", 1.0, "2 3")
    sc.circle(C, 1.0, "HEAD", 3.0)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "middle", 17, dx=-6, dy=24)
    sc.line(C, P, "HEAD", 1.2)
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=-12)
    axis_out(sc, O, None, "BLUE")
    sc.label(O, S(bold("k"), "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-14, dy=26)
    unit(sc, O, 0, 0.4, S(bold("i"), "1"), off=(6, -12))
    unit(sc, O, 90, 0.4, S(bold("j"), "1"), off=(-14, 4))
    # forces at P
    sc.vec(P, (P[0], P[1] - 0.7), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.7), "W = −m g " + S(bold("j"), "1"), "PINK", "end", 16, weight="700", dx=-10, dy=6)
    n1 = (P[0] + 0.5 * c, P[1] + 0.5 * s_)
    sc.vec(P, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, S(bold("N"), "1") + " " + S(bold("e"), "r"), "PINK", "start", 16, weight="700", dx=10, dy=4)
    sc.note(n1, "(sign from part (e))", "PINK", "start", 13, dx=10, dy=22)
    f1 = (P[0] + 0.5, P[1])
    _dvec(sc, P, f1, "PINK", 2.6)
    sc.label(f1, S(bold("F"), "C") + " = m Ω² R(1 + cos φ) " + S(bold("i"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=-8)
    sc.label(f1, "(inertia)", "PINK", "start", 14, dx=10, dy=10)
    unit(sc, P, math.degrees(math.atan2(math.cos(PHI_F), -math.sin(PHI_F))), 0.35, S(bold("e"), "φ"), "ACC", off=(12, -6))
    sc.mass(P, "P", r=7, name_off=(-18, 24))
    sc.note((-0.5, -1.62), "plane Oxy of the wire", "TEXT", "start", 13)
    # ---- lower panel: view from above, j1 out of the paper, k1 down the page
    def R(x, y):
        return (x, RY + y)
    sc.line(R(0.0, 0.0), R(2.0, 0.0), "HEAD", 5.0)
    axis_out(sc, R(0.0, 0.0), None, "BLUE")
    sc.label(R(0.0, 0.0), S(bold("j"), "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-14, dy=-12)
    sc.label(R(0.0, 0.0), "O", "HEAD", "end", 17, dx=-12, dy=26)
    unit(sc, R(2.2, 0.0), 0, 0.45, S(bold("i"), "1"), off=(2, 22))
    unit(sc, R(0.0, 0.0), -90, 0.5, S(bold("k"), "1"), off=(-16, 8))
    sc.arc(R(0.0, 0.0), 0.45, -70, -20, "GREEN", 1.8, head=True)
    sc.arc(R(0.0, 0.0), 0.45, -20, -70, "GREEN", 1.8, head=True)
    sc.label(R(0.0, 0.0), "Ω(t)", "GREEN", "start", 16, weight="700", dx=88, dy=64)
    Pq = R(1.0 + c, 0.0)
    sc.mass(Pq, None, r=6.5)
    sc.label(Pq, "P (seen from above)", "HEAD", "end", 16, dx=-14, dy=28)
    xe, xc, xn = Pq[0], Pq[0] - 0.12, Pq[0] + 0.12
    _dvec(sc, (xe, Pq[1] - 0.06), (xe, Pq[1] - 0.6), "PINK", 2.6)
    sc.label((xe, Pq[1] - 0.6), S(bold("F"), "E") + " = m A ω² R cos ωt (1 + cos φ) " + S(bold("k"), "1"), "PINK", "start", 16,
             weight="700", dx=12, dy=4)
    sc.label((xe, Pq[1] - 0.6), "(inertia)", "PINK", "start", 14, dx=12, dy=22)
    _dvec(sc, (xc, Pq[1] + 0.06), (xc, Pq[1] + 0.4), "PINK", 2.6)
    sc.label((xc, Pq[1] + 0.4), S(bold("F"), "COR") + " (inertia)", "PINK", "end", 16, weight="700", dx=-8, dy=-26)
    sc.label((xc, Pq[1] + 0.4), "= −2 m A ω R sin ωt sin φ φ̇ " + S(bold("k"), "1"), "PINK", "end", 16, weight="700",
             dx=-8, dy=-4)
    sc.vec((xn, Pq[1] + 0.06), (xn, Pq[1] + 0.2), None, "PINK", 2.8, head=10)
    sc.label((xn, Pq[1] + 0.2), S(bold("N"), "2") + " " + S(bold("k"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=-4)
    sc.note(R(0.0, -0.9), S("N", "2") + " " + S("k", "1") + " + " + S("F", "E") + " + " + S("F", "COR") + " = 0", "TEXT", "start", 14)
    sc.note((-0.5, RY - 1.08), "view from above: the plane of the wire is seen edge-on", "TEXT", "start", 13)
    return sc
