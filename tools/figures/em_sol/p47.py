"""Problem 47: two repelling particles on concentric wires (radii a and 2a) in a plane spinning about the vertical."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold

PHI, THETA = 30.0, -60.0       # the equilibrium configuration of part (i)


def _pt(r, deg):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


@figure("p47-wire-plane",
        "Plane of the two wires, fixed in the moving frame: circles of radii a and 2a centred at O, particle P at angle "
        "phi = 30 degrees and particle Q at angle theta = -60 degrees from x1, the shaded right triangle of P with legs "
        "a cos phi and a sin phi, the polar bases of both particles in orange and the segment PQ",
        r"Plane $Ox_1y_1$, fixed in $S_1$, drawn at the configuration of part (i) ($\varphi = 30^\circ$, $\theta = -60^\circ$). "
        r"For $P$ the hypotenuse of the shaded triangle is $a$, the leg adjacent to $\varphi$ is $a\cos\varphi$ (along "
        r"$\mathbf i_1$) and the opposite one $a\sin\varphi$ (along $\mathbf j_1$); $Q$ works the same way with $2a$ and "
        r"$\theta$ (here negative, below $Ox_1$). Polar bases $\mathbf e_r, \mathbf e_\varphi$ and $\mathbf e_r^Q, "
        r"\mathbf e_\theta$ in orange")
def wire_plane():
    sc = Scene(720, 760, (360, 400), 140)
    O = (0.0, 0.0)
    P = _pt(1.0, PHI)
    Q = _pt(2.0, THETA)
    sc.circle(O, 1.0, "HEAD", 2.4)
    sc.circle(O, 2.0, "HEAD", 2.4)
    fixed_axis(sc, (-2.35, 0.0), 0, 4.75, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -2.3), 90, 5.05, S("y", "1") + " ≡ " + S("y", "0"), off=(36, 2))
    spin_about_vertical(sc, (0.0, 2.33), 0.2, 0.05, "Ω")
    # key triangle of P
    triangle(sc, [O, (P[0], 0.0), P])
    right_angle(sc, (P[0], 0.0), 180, 90, 0.07)
    sc.line(O, P, "HEAD", 1.4)
    sc.dashed(P, (P[0], 0.0))
    sc.label((P[0] / 2, 0.0), "a cos φ", "TEXT", "middle", 14, dy=22)
    sc.label((P[0], P[1] / 2), "a sin φ", "TEXT", "end", 13, dx=-5, dy=10)
    sc.angle(O, 0.25, 0, PHI, "φ", name_r=0.36)
    # Q
    sc.line(O, Q, "HEAD", 1.4)
    sc.angle(O, 0.62, THETA, 0, "θ", name_r=0.78)
    # segment PQ (line of the repulsion)
    sc.line(P, Q, "PINK", 1.4, "6 4")
    mid = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
    sc.label(mid, "PQ", "PINK", "start", 14, dx=10, dy=0)
    # moving basis
    B1 = (-2.25, -2.15)
    unit(sc, B1, 0, 0.45, S(bold("i"), "1"), off=(14, 6))
    unit(sc, B1, 90, 0.45, S(bold("j"), "1"), off=(-16, 6))
    sc.note(B1, "basis " + S("B", "1"), "TEXT", "start", 13, dx=4, dy=22)
    # polar bases
    unit(sc, P, PHI, 0.55, S(bold("e"), "r"), "ACC", off=(10, -6))
    unit(sc, P, PHI + 90, 0.55, S(bold("e"), "φ"), "ACC", off=(-14, -2))
    unit(sc, Q, THETA, 0.55, S(bold("e"), "r") + S("", "", "Q"), "ACC", off=(14, 14))
    unit(sc, Q, THETA + 90, 0.55, S(bold("e"), "θ"), "ACC", off=(16, -2))
    sc.mass(P, "P", r=7, name_off=(-18, 4))
    sc.mass(Q, "Q", r=7, name_off=(20, 8))
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    sc.gravity((-2.3, 2.5), 0.5, "g")
    return sc


@figure("p47-top-view",
        "Top view from +y0 with j0 out of the paper: inertial axes i0 to the right and k0 down the page in grey, the "
        "axes i1 and k1 of the rotating plane turned counter-clockwise by Omega t in blue, with the dashed components of i1",
        r"View from $+y_0$, with $\mathbf j_0 = \mathbf j_1$ out of the paper ($\odot$): $\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ "
        r"points down the page. For $\Omega \gt 0$ the plane of the wires turns counter-clockwise by $\Omega t$; $\mathbf i_1$ "
        r"has the components $\cos\Omega t$ along $\mathbf i_0$ and $\sin\Omega t$ along $-\mathbf k_0$ (up the page), hence "
        r"the minus sign")
def top_view():
    sc = Scene(480, 440, (170, 215), 165)
    O = (0.0, 0.0)
    a = 35.0
    fixed_axis(sc, O, 0, 1.15, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, O, -90, 1.0, S(bold("k"), "0"), off=(14, 4))
    fixed_axis(sc, O, 90, 0.95, "−" + S(bold("k"), "0"), off=(20, 4), dashed=True)
    axis_out(sc, O, S(bold("j"), "0") + " = " + S(bold("j"), "1"), off=(-46, 24))
    i1 = unit(sc, O, a, 1.0, S(bold("i"), "1"), off=(14, -6))
    unit(sc, O, a - 90, 1.0, S(bold("k"), "1"), off=(16, 8))
    sc.angle(O, 0.42, 0, a, "Ωt", name_r=0.56)
    sc.angle(O, 0.30, -90, a - 90, "Ωt", name_r=0.43)
    triangle(sc, [O, (i1[0], 0.0), i1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(i1, (0.0, i1[1]))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, i1[1]), "sin Ωt", "TEXT", "end", 15, dx=-12, dy=5)
    sc.note((0.45, 1.0), "view from " + "+" + S("y", "0"), "TEXT", "start", 13)
    sc.note((0.45, 0.88), "Ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc


def _dvec(sc, a, b, col="PINK", w=2.4, head=10):
    """Dashed arrow (inertia force) from world point a to b."""
    from figures.svgkit import arrow_head
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.atan2(by - ay, bx - ax)
    tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
    sc.c.add(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{col}" stroke-width="{w}" '
             f'stroke-dasharray="7 4"/>')
    arrow_head(sc.c, (ax, ay), (bx, by), col, head)


@figure("p47-fbd",
        "Free-body diagrams of the two particles: top, the plane of the wires with the weights, the repulsion along PQ, "
        "the radial reactions and the centrifugal inertia forces; bottom, the plane seen edge-on from above with the "
        "Coriolis inertia forces along k1 balanced by the reaction components N2 and N4",
        r"Forces seen from $S_1$ at the configuration of part (i). In the plane of the wires: weights, repulsion along $PQ$, "
        r"radial reactions and the centrifugal forces (dashed), horizontal and away from the axis $Oy_1$. Seen from above: "
        r"the Coriolis forces (dashed), normal to the plane, balanced by the reaction components $N_2$ and $N_4$")
def fbd():
    k = 110.0
    sc = Scene(900, 940, (300, 330), k)
    s = 150.0 / k
    LY = -(815 - 330) / k                                   # world y of the lower panel's line (pixel y = 800)
    # ---------------- upper panel: plane of the wires, k1 out of the paper
    P = _pt(1.0, PHI)
    Q = _pt(2.0, THETA)
    O = (0.0, 0.0)
    sc.circle(O, 1.0, "HEAD", 2.4)
    sc.circle(O, 2.0, "HEAD", 2.4)
    sc.line(P, Q, "PINK", 1.3, "6 4")
    axis_out(sc, O, None, "BLUE")
    sc.label(O, "O", "HEAD", "end", 17, dx=-12, dy=-12)
    sc.label(O, S(bold("k"), "1") + " (⊙)", "BLUE", "end", 15, weight="700", dx=-14, dy=6)
    B1 = (-2.45, -2.3)
    unit(sc, B1, 0, 0.45, S(bold("i"), "1"), off=(14, 6))
    unit(sc, B1, 90, 0.45, S(bold("j"), "1"), off=(-16, 6))
    # repulsion directions
    dl = math.hypot(P[0] - Q[0], P[1] - Q[1])
    uq = ((P[0] - Q[0]) / dl, (P[1] - Q[1]) / dl)           # from Q towards P
    # ---- forces on P
    w0 = (P[0] - 0.12, P[1])
    sc.vec(w0, (w0[0], w0[1] - 0.8), None, "PINK", 2.8, head=11)
    sc.label((w0[0], w0[1] - 0.8), "−mg " + S(bold("j"), "1"), "PINK", "end", 16, weight="700", dx=-8, dy=8)
    r1 = (P[0] + 1.75 * uq[0], P[1] + 1.75 * uq[1])
    sc.vec(P, r1, None, "PINK", 2.8, head=11)
    sc.label(r1, "k " + bold("QP"), "PINK", "start", 16, weight="700", dx=8, dy=-4)
    e = _pt(1.0, PHI)
    n1 = (P[0] + 1.5 * e[0], P[1] + 1.5 * e[1])
    sc.vec(P, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, S(bold("N"), "1") + " " + S(bold("e"), "r", "P"), "PINK", "start", 16, weight="700", dx=8, dy=-14)
    sc.note(n1, "(sign unknown)", "PINK", "start", 13, dx=8, dy=2)
    c1 = (P[0] + 1.4, P[1])
    _dvec(sc, P, c1, "PINK", 2.6)
    sc.label(c1, S(bold("F"), "C", "P") + " = m Ω² a cos φ " + S(bold("i"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=-2)
    sc.label(c1, "(inertia)", "PINK", "start", 14, dx=10, dy=17)
    # ---- forces on Q
    q0 = (Q[0] - 0.12, Q[1])
    sc.vec(q0, (q0[0], q0[1] - 0.5), None, "PINK", 2.8, head=11)
    sc.label((q0[0], q0[1] - 0.5), "−mg " + S(bold("j"), "1"), "PINK", "end", 16, weight="700", dx=-6, dy=8)
    r2 = (Q[0] - 0.8 * uq[0], Q[1] - 0.8 * uq[1])
    sc.vec(Q, r2, None, "PINK", 2.8, head=11)
    sc.label(r2, "k " + bold("PQ"), "PINK", "middle", 16, weight="700", dx=-4, dy=24)
    e2 = _pt(1.0, THETA)
    n3 = (Q[0] + 0.85 * e2[0], Q[1] + 0.85 * e2[1])
    sc.vec(Q, n3, None, "PINK", 2.8, head=11)
    sc.label(n3, S(bold("N"), "3") + " " + S(bold("e"), "r", "Q"), "PINK", "start", 16, weight="700", dx=8, dy=0)
    sc.note(n3, "(sign unknown)", "PINK", "start", 13, dx=8, dy=16)
    c2 = (Q[0] + 1.3, Q[1])
    _dvec(sc, Q, c2, "PINK", 2.6)
    sc.label(c2, S(bold("F"), "C", "Q") + " = 2 m Ω² a cos θ " + S(bold("i"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=-2)
    sc.label(c2, "(inertia)", "PINK", "start", 14, dx=10, dy=17)
    sc.mass(P, "P", r=7, name_off=(-18, -10))
    sc.mass(Q, "Q", r=7, name_off=(-18, 4))
    sc.note((-2.6, 2.75), "plane of the wires", "TEXT", "start", 13)
    sc.note((-2.6, 2.6), "N₂ k₁, N₄ k₁ and the Coriolis forces are normal to it: see below", "TEXT", "start", 13)
    # ---------------- lower panel: from above, j1 out of the paper, k1 down the page
    def R(x, y):
        return (x * s, LY + y * s)
    Oc = R(0.0, 0.0)
    Pc = R(P[0], 0.0)
    Qc = R(Q[0], 0.0)
    sc.line((Oc[0] - 0.1, Oc[1]), (Qc[0] + 0.45, Qc[1]), "HEAD", 5.0)
    axis_out(sc, Oc, None, "BLUE")
    sc.label(Oc, "O", "HEAD", "end", 17, dx=-12, dy=-12)
    sc.label(Oc, S(bold("j"), "1") + " (vertical, ⊙)", "BLUE", "end", 15, weight="700", dx=-14, dy=6)
    unit(sc, Oc, 0, 0.3, S(bold("i"), "1"), off=(0, 22))
    unit(sc, Oc, -90, 0.5, S(bold("k"), "1"), off=(16, 8))
    sc.spin(Oc, 0.62, 200, 250, "Ω", name_r=0.78)
    sc.note((Qc[0] + 0.45, Qc[1]), "plane of the wires", "TEXT", "start", 13, dx=8, dy=-6)
    sc.note((Qc[0] + 0.45, Qc[1]), "(edge-on)", "TEXT", "start", 13, dx=8, dy=10)
    ln = 0.42 * s
    # P: Coriolis up the page (dashed), N2 down the page; labels to the left
    _dvec(sc, Pc, (Pc[0], Pc[1] + ln), "PINK", 2.6)
    sc.label((Pc[0], Pc[1] + ln), S(bold("F"), "COR", "P") + " = −2 m Ω a φ̇ sin φ " + S(bold("k"), "1"), "PINK", "end", 16,
             weight="700", dx=-6, dy=-18)
    sc.label((Pc[0], Pc[1] + ln), "(inertia; drawn for φ̇ > 0)", "PINK", "end", 14, dx=-6, dy=-2)
    sc.vec(Pc, (Pc[0], Pc[1] - ln), None, "PINK", 2.8, head=11)
    sc.label((Pc[0], Pc[1] - ln), S(bold("N"), "2") + " " + S(bold("k"), "1"), "PINK", "end", 16, weight="700", dx=-8, dy=6)
    # Q: Coriolis down the page (dashed, theta = -60 deg and a positive rate), N4 up; labels to the right
    _dvec(sc, Qc, (Qc[0], Qc[1] - ln), "PINK", 2.6)
    sc.label((Qc[0], Qc[1] - ln), S(bold("F"), "COR", "Q") + " = −4 m Ω a θ̇ sin θ " + S(bold("k"), "1"), "PINK", "start", 16,
             weight="700", dx=10, dy=6)
    sc.label((Qc[0], Qc[1] - ln), "(inertia; drawn for θ̇ > 0)", "PINK", "start", 14, dx=10, dy=22)
    sc.vec(Qc, (Qc[0], Qc[1] + ln), None, "PINK", 2.8, head=11)
    sc.label((Qc[0], Qc[1] + ln), S(bold("N"), "4") + " " + S(bold("k"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=-4)
    sc.mass(Pc, "P", r=6, name_off=(-14, -10))
    sc.mass(Qc, "Q", r=6, name_off=(14, -10))
    sc.note(R(-1.85, 0.95), "seen from above", "TEXT", "start", 13)
    return sc
