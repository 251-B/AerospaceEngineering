"""Problem 40: particle P on the vertical axis and particle Q on a horizontal ring whose centre D revolves about it."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

WT = 35.0          # angle Omega t, deg (drawing value)
PHI = 50.0         # angle phi of Q on the ring, deg


@figure("p40-top-view",
        "Top view from +z0 with k0 out of the paper: fixed axes i0 to the right and j0 up in grey, the frame axes i1 and "
        "j1 turned counter-clockwise by Omega t in blue, j1 pointing to the ring centre D, and the shaded right triangles "
        "that give their components",
        r"View from $+z_0$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$), so $\mathbf j_0 = \mathbf k_0\times"
        r"\mathbf i_0$ points up. $\mathbf i_1, \mathbf j_1$ are $\mathbf i_0, \mathbf j_0$ turned counter-clockwise by "
        r"$\Omega t$, and $\mathbf j_1$ points from $O$ to the centre $D$ of the ring. $\mathbf j_1$ has legs "
        r"$\cos\Omega t$ along $\mathbf j_0$ and $\sin\Omega t$ along $-\mathbf i_0$, hence its minus sign")
def top_view():
    sc = Scene(520, 470, (250, 330), 150)
    O = (0.0, 0.0)
    fixed_axis(sc, O, 0, 1.2, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.2, bold("j") + S("", "0"), off=(16, 2))
    fixed_axis(sc, O, 180, 1.0, "−" + bold("i") + S("", "0"), off=(-8, -12), dashed=True)
    i1 = (math.cos(math.radians(WT)), math.sin(math.radians(WT)))
    j1 = (-math.sin(math.radians(WT)), math.cos(math.radians(WT)))
    D = (1.55 * j1[0], 1.55 * j1[1])
    sc.dashed(j1, D)
    sc.dotp(D, 4.5)
    sc.label(D, "D", "HEAD", "end", 17, dx=-10, dy=-6)
    triangle(sc, [O, (i1[0], 0.0), i1])
    triangle(sc, [O, (0.0, j1[1]), j1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(j1, (0.0, j1[1]))
    right_angle(sc, (i1[0], 0.0), 180, 90, 0.06)
    right_angle(sc, (0.0, j1[1]), 270, 180, 0.06)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -4))
    unit(sc, O, 90 + WT, 1.0, bold("j") + S("", "1"), off=(-16, 6))
    sc.label((i1[0] / 2, 0.0), "cos Ωt", "TEXT", "middle", 15, dy=20)
    sc.label((i1[0], i1[1] / 2), "sin Ωt", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((j1[0] / 2, j1[1]), "sin Ωt", "TEXT", "middle", 15, dy=-9)
    sc.label((0.0, j1[1] * 0.42), "cos Ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.angle(O, 0.30, 0, WT, "Ωt", name_r=0.44)
    sc.angle(O, 0.24, 90, 90 + WT, "Ωt", name_r=0.37)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-46, 30))
    sc.note((0.55, -0.6), "view from +z₀", "TEXT", "start", 13)
    sc.note((0.55, -0.73), "Ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc


@figure("p40-ring",
        "Plane of the ring seen from above in the moving frame: O at the origin, the centre D at distance l along j1, the "
        "ring of radius R, the particle Q at angle phi from j1 towards negative i1, the shaded right triangle D F Q with "
        "legs R cos phi along j1 and R sin phi along minus i1, and the ring basis e_r, e_phi at Q",
        r"Plane of the ring, fixed in $S_1$, seen from above ($\mathbf k_1$ out of the paper). $\overrightarrow{OQ} = "
        r"\ell\,\mathbf j_1 + R\,\mathbf e_r$. In the shaded right triangle $DFQ$ the hypotenuse is $R$, the leg along "
        r"$\mathbf j_1$ is $R\cos\phi$ and the leg along $-\mathbf i_1$ is $R\sin\phi$. $\mathbf i_1, \mathbf j_1$ in blue, "
        r"$\mathbf e_r, \mathbf e_\phi$ in orange")
def ring():
    sc = Scene(560, 560, (300, 470), 125)
    O = (0.0, 0.0)
    ell, R = 1.6, 1.0
    D = (0.0, ell)
    p = math.radians(PHI)
    Q = (-R * math.sin(p), ell + R * math.cos(p))
    F = (0.0, Q[1])
    sc.circle(D, R, "HEAD", 2.4)
    fixed_axis(sc, (-1.5, 0.0), 0, 2.9, S("x", "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.3), 90, 3.3, S("y", "1"), off=(14, 4))
    triangle(sc, [D, F, Q])
    sc.line(D, Q, "HEAD", 1.6)
    sc.dashed(F, Q)
    sc.dotp(F, 3.5)
    sc.label(F, "F", "HEAD", "start", 17, dx=10, dy=-8)
    right_angle(sc, F, 270, 180, 0.07)
    sc.label((0.0, (D[1] + F[1]) / 2), "R cos φ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((Q[0] / 2, F[1]), "R sin φ", "TEXT", "middle", 15, dy=-10)
    sc.label(((D[0] + Q[0]) / 2, (D[1] + Q[1]) / 2), "R", "TEXT", "end", 16, dx=-8, dy=14)
    sc.angle(D, 0.3, 90, 90 + PHI, "φ", name_r=0.42)
    sc.dim((1.25, 0.0), (1.25, ell), "ℓ", off=(14, 5))
    sc.dotp(D, 4.0)
    sc.label(D, "D", "HEAD", "start", 17, dx=10, dy=18)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=20)
    unit(sc, O, 0, 0.45, bold("i") + S("", "1"), off=(4, 22))
    unit(sc, O, 90, 0.45, bold("j") + S("", "1"), off=(-18, 8))
    unit(sc, Q, 90 + PHI, 0.5, bold("e") + S("", "r"), "ACC", off=(-6, -10))
    unit(sc, Q, 180 + PHI, 0.5, bold("e") + S("", "φ"), "ACC", off=(-16, 8))
    sc.mass(Q, "Q", r=7, name_off=(-26, 6))
    axis_out(sc, (1.2, 2.75), bold("k") + S("", "1"), off=(26, 6))
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


@figure("p40-fbd",
        "Free-body diagrams: top, the vertical plane through the axis and Q with the weights, the spring forces and the "
        "reactions on P and Q; bottom, the horizontal plane of the ring seen from above with the reaction N3 e_r, the "
        "horizontal part of the spring force and the centrifugal and Coriolis inertia forces on Q",
        r"Forces seen from $S_1$. On $P$: weight, spring $k\,\overrightarrow{PQ}$ and the reaction of the axis, normal to it; "
        r"no inertia force, since $P$ is on the axis. On $Q$: weight, spring $-k\,\overrightarrow{PQ}$, reaction "
        r"$N_3\,\mathbf e_r + N_4\,\mathbf k_1$, and the centrifugal and Coriolis forces (dashed), both horizontal")
def fbd():
    k = 110.0
    sc = Scene(900, 820, (470, 225), k)
    LY = -(770 - 225) / k                                   # world y of O in the lower panel (pixel y = 740)

    def L(x, y):
        return (x, LY + y)
    # ---------------- upper panel: vertical plane through the axis and Q
    zeta, dq = 0.8, 2.4
    P, Q, O = (0.0, zeta), (dq, 0.0), (0.0, 0.0)
    sc.line((0.0, -0.85), (0.0, 1.5), "EDGE", 1.8, "10 3 2 3")
    sc.vec((0.0, 1.5), (0.0, 1.75), None, "EDGE", 1.6, head=8)
    sc.label((0.0, 1.75), bold("k") + S("", "1"), "TEXT", "middle", 17, weight="700", dy=-8)
    sc.vec((0.0, 0.0), (3.3, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((1.2, 0.0), "towards Q (horizontal)", "TEXT", "middle", 15, dy=24)
    sc.spring(P, Q, coils=9, amp=7.0)
    L_ = math.hypot(Q[0] - P[0], Q[1] - P[1])
    u = ((Q[0] - P[0]) / L_, (Q[1] - P[1]) / L_)
    nrm = (-u[1], u[0])                                      # normal pointing up-right of the spring
    # forces on P
    sc.vec(P, (0.0, zeta - 0.55), None, "PINK", 2.8, head=11)
    sc.label((0.0, zeta - 0.55), "−mg " + bold("k") + S("", "1"), "PINK", "end", 16, weight="700", dx=-10, dy=6)
    sc.vec(P, (-0.8, zeta), None, "PINK", 2.8, head=11)
    sc.label((-0.8, zeta), S(bold("N"), "1") + " " + bold("i") + S("", "1") + " + " + S(bold("N"), "2") + " " + bold("j") + S("", "1"),
             "PINK", "end", 16, weight="700", dx=-8, dy=-8)
    sc.note((-0.8, zeta), "(normal to the axis)", "PINK", "end", 13, dx=-8, dy=14)
    s0 = (P[0] + 0.11 * nrm[0], P[1] + 0.11 * nrm[1])
    s1 = (s0[0] + 0.8 * u[0], s0[1] + 0.8 * u[1])
    sc.vec(s0, s1, None, "PINK", 2.8, head=11)
    sc.label(s1, "k " + bold("PQ"), "PINK", "start", 16, weight="700", dx=6, dy=-14)
    sc.note((0.15, 1.5), "no inertia force on the axis", "TEXT", "start", 13)
    # forces on Q
    sc.vec(Q, (Q[0], -0.55), None, "PINK", 2.8, head=11)
    sc.label((Q[0], -0.55), "−mg " + bold("k") + S("", "1"), "PINK", "start", 16, weight="700", dx=10, dy=6)
    sc.vec(Q, (Q[0], 0.55), None, "PINK", 2.8, head=11)
    sc.label((Q[0], 0.55), S(bold("N"), "4") + " " + bold("k") + S("", "1"), "PINK", "start", 16, weight="700", dx=10, dy=4)
    q0 = (Q[0] + 0.11 * nrm[0], Q[1] + 0.11 * nrm[1])
    q1 = (q0[0] - 0.8 * u[0], q0[1] - 0.8 * u[1])
    sc.vec(q0, q1, None, "PINK", 2.8, head=11)
    sc.label(q1, "−k " + bold("PQ"), "PINK", "middle", 16, weight="700", dx=-4, dy=-18)
    sc.mass(P, "P", r=7, name_off=(-16, 22))
    sc.mass(Q, "Q", r=7, name_off=(-18, 24))
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=22)
    sc.note((-4.2, 1.75), "vertical plane through the axis and Q", "TEXT", "start", 13)
    # ---------------- lower panel: horizontal plane of the ring seen from above, k1 out of the paper
    ell, R = 1.6, 1.0
    p = math.radians(PHI)
    D = L(0.0, ell)
    Qp = L(-R * math.sin(p), ell + R * math.cos(p))
    Oq = L(0.0, 0.0)
    er = (-math.sin(p), math.cos(p))
    ep = (-math.cos(p), -math.sin(p))
    sc.circle(D, R, "HEAD", 2.4)
    sc.dotp(D, 4.0)
    sc.label(D, "D", "HEAD", "start", 17, dx=10, dy=-8)
    axis_out(sc, Oq, None, "BLUE")
    sc.label(Oq, "O", "HEAD", "end", 17, dx=-14, dy=24)
    sc.label(Oq, bold("k") + S("", "1") + " (⊙)", "BLUE", "start", 15, weight="700", dx=14, dy=30)
    unit(sc, Oq, 0, 0.45, bold("i") + S("", "1"), off=(4, -12))
    unit(sc, Oq, 90, 0.45, bold("j") + S("", "1"), off=(-16, 4))
    sc.spin(Oq, 0.62, 110, 170, "Ω", name_r=0.78)
    sc.note(L(-4.2, 3.55), "horizontal plane of the ring, seen from above", "TEXT", "start", 13)
    dq_ = math.hypot(Qp[0] - Oq[0], Qp[1] - Oq[1])
    ur = ((Qp[0] - Oq[0]) / dq_, (Qp[1] - Oq[1]) / dq_)    # from O towards Q (away from the axis)

    def sh(pt, v, d):
        return (pt[0] + d * v[0], pt[1] + d * v[1])
    # N3 e_r and F_COR are both along e_r: parallel arrows on the +e_phi side of Q
    n0 = sh(Qp, ep, 0.07)
    n1 = sh(n0, er, 0.55)
    sc.vec(n0, n1, None, "PINK", 2.8, head=11)
    sc.label(n1, S(bold("N"), "3") + " " + S(bold("e"), "r"), "PINK", "middle", 16, weight="700", dx=-4, dy=-12)
    c0 = sh(Qp, ep, 0.17)
    c1 = sh(c0, er, 0.95)
    _dvec(sc, c0, c1, "PINK", 2.6)
    sc.label(c1, S(bold("F"), "COR") + " = 2 m Ω R φ̇ " + S(bold("e"), "r"), "PINK", "end", 16, weight="700", dx=-10, dy=-2)
    sc.label(c1, "(inertia; drawn for φ̇ > 0)", "PINK", "end", 14, dx=-10, dy=16)
    W = L(1.55, 2.55)                                       # the ring basis at Q, redrawn clear of the forces
    unit(sc, W, 90 + PHI, 0.45, bold("e") + S("", "r"), "ACC", off=(-12, -6))
    unit(sc, W, 180 + PHI, 0.45, bold("e") + S("", "φ"), "ACC", off=(-14, 12))
    sc.note(W, "ring basis at Q", "TEXT", "start", 13, dx=12, dy=22)
    # horizontal part of the spring force: from Q towards O; centrifugal force: away from the axis
    t1 = sh(Qp, ur, -0.8)
    sc.vec(Qp, t1, None, "PINK", 2.8, head=11)
    sc.label(t1, "−k " + bold("PQ"), "PINK", "start", 16, weight="700", dx=8, dy=8)
    sc.note(t1, "(horizontal part)", "PINK", "start", 13, dx=8, dy=24)
    f1 = sh(Qp, ur, 0.7)
    _dvec(sc, Qp, f1, "PINK", 2.6)
    sc.label(f1, S(bold("F"), "C") + " = m Ω² " + S(bold("r"), "1", "Q"), "PINK", "start", 16, weight="700", dx=10, dy=0)
    sc.label(f1, "(inertia)", "PINK", "start", 14, dx=10, dy=18)
    sc.mass(Qp, "Q", r=7, name_off=(22, 6))
    return sc
