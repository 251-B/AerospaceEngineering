"""Problem 36: pendulum string dragged by a bar that turns about the vertical through its centre O."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, spin_about_vertical, triangle, unit
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

WT = 35.0          # angle turned by the bar, deg (drawing value)
TH = 30.0          # angle theta of the plane bar-P from the downward vertical, deg
PHI = 60.0         # angle phi between CP and the bar, deg


def _p(r, deg):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


@figure("p36-top-view",
        "Top view from +z0 with k0 out of the paper: fixed axes i0 to the right and j0 up in grey, the bar axes i1 and j1 "
        "turned counter-clockwise by omega t in blue, and the shaded right triangles that give the components of i1 and j1",
        r"View from $+z_0$, with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$), so $\mathbf j_0 = \mathbf k_0\times"
        r"\mathbf i_0$ points up. $\mathbf i_1, \mathbf j_1$ are $\mathbf i_0, \mathbf j_0$ turned counter-clockwise by "
        r"$\omega t$. $\mathbf i_1$ has legs $\cos\omega t$ along $\mathbf i_0$ and $\sin\omega t$ along $\mathbf j_0$; "
        r"$\mathbf j_1$ has legs $\cos\omega t$ along $\mathbf j_0$ and $\sin\omega t$ along $-\mathbf i_0$, hence its minus "
        r"sign. The bar lies along $\mathbf i_1$")
def top_view():
    sc = Scene(520, 450, (250, 300), 165)
    O = (0.0, 0.0)
    fixed_axis(sc, O, 0, 1.2, bold("i") + S("", "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 1.2, bold("j") + S("", "0"), off=(16, 2))
    fixed_axis(sc, O, 180, 1.0, "−" + bold("i") + S("", "0"), off=(-8, -12), dashed=True)
    i1 = (math.cos(math.radians(WT)), math.sin(math.radians(WT)))
    j1 = (-math.sin(math.radians(WT)), math.cos(math.radians(WT)))
    triangle(sc, [O, (i1[0], 0.0), i1])
    triangle(sc, [O, (0.0, j1[1]), j1])
    sc.dashed(i1, (i1[0], 0.0))
    sc.dashed(j1, (0.0, j1[1]))
    right_angle(sc, (i1[0], 0.0), 180, 90, 0.06)
    right_angle(sc, (0.0, j1[1]), 270, 180, 0.06)
    unit(sc, O, WT, 1.0, bold("i") + S("", "1"), off=(14, -4))
    unit(sc, O, 90 + WT, 1.0, bold("j") + S("", "1"), off=(-12, -10))
    sc.label((i1[0] / 2, 0.0), "cos ωt", "TEXT", "middle", 15, dy=20)
    sc.label((i1[0], i1[1] / 2), "sin ωt", "TEXT", "start", 15, dx=8, dy=5)
    sc.label((j1[0] / 2, j1[1]), "sin ωt", "TEXT", "middle", 15, dy=-9)
    sc.label((0.0, j1[1] * 0.42), "cos ωt", "TEXT", "start", 15, dx=10, dy=5)
    sc.angle(O, 0.30, 0, WT, "ωt", name_r=0.44)
    sc.angle(O, 0.24, 90, 90 + WT, "ωt", name_r=0.37)
    axis_out(sc, O, bold("k") + S("", "0") + " = " + bold("k") + S("", "1"), off=(-46, 30))
    sc.note((0.55, -0.62), "view from +z₀", "TEXT", "start", 13)
    sc.note((0.55, -0.74), "ω > 0: counter-clockwise", "TEXT", "start", 13)
    return sc


@figure("p36-anchor-top",
        "Top view of the plane of the bar: the bar along i1 at angle omega t from i0, the point A' directly below the "
        "anchor A at distance R along i0, and the right triangle O F A' with legs R cos omega t along the bar and "
        "R sin omega t perpendicular to it",
        r"Same view from $+z_0$. $A'$ is the point of the plane of the bar directly below the anchor $A$, at distance $R$ "
        r"from $O$ along $\mathbf i_0$, that is $\omega t$ behind the bar. In the shaded right triangle $OFA'$ the "
        r"hypotenuse is $R$, the leg along the bar is $R\cos\omega t$ and the leg $FA'$, parallel to $-\mathbf j_1$, is "
        r"$R\sin\omega t$")
def anchor_top():
    sc = Scene(560, 330, (110, 250), 150)
    O = (0.0, 0.0)
    R = 1.6
    A = (R, 0.0)
    d = (math.cos(math.radians(WT)), math.sin(math.radians(WT)))
    F = (R * math.cos(math.radians(WT)) * d[0], R * math.cos(math.radians(WT)) * d[1])
    fixed_axis(sc, O, 0, 2.3, bold("i") + S("", "0"), off=(14, 5))
    sc.line((-0.45 * d[0], -0.45 * d[1]), (2.15 * d[0], 2.15 * d[1]), "HEAD", 5.0)
    sc.label((2.15 * d[0], 2.15 * d[1]), "bar", "HEAD", "start", 15, italic=False, dx=10, dy=4)
    triangle(sc, [O, F, A])
    sc.dashed(F, A)
    right_angle(sc, F, 180 + WT, WT - 90, 0.07)
    unit(sc, O, WT, 0.4, bold("i") + S("", "1"), off=(4, 22))
    sc.angle(O, 0.72, 0, WT, "ωt", name_r=0.86)
    sc.dotp(A, 4.5)
    sc.label(A, "A′", "HEAD", "middle", 17, dy=24)
    sc.label(F, "F", "HEAD", "end", 17, dx=-8, dy=-6)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=-8)
    sc.label((R * 0.62, 0.0), "R", "TEXT", "middle", 16, dy=20)
    sc.label((F[0] * 0.55, F[1] * 0.55), "R cos ωt", "TEXT", "end", 15, dx=-10, dy=-8)
    sc.label(((F[0] + A[0]) / 2, (F[1] + A[1]) / 2), "R sin ωt", "TEXT", "start", 15, dx=12, dy=4)
    axis_out(sc, (-0.45, 0.65), bold("k") + S("", "1"), off=(26, 6))
    return sc


@figure("p36-bar-view",
        "View along the bar with i1 out of the paper at the contact point C: j1 to the right and k1 up in blue, the "
        "dashed downward vertical, the trace of the plane bar-P at angle theta from it towards negative y1, the unit vector "
        "u along that trace and e_theta perpendicular to it, both orange, and the shaded right triangle with legs cos theta "
        "and sin theta",
        r"View along the bar, with $\mathbf i_1$ out of the paper ($\odot$) at $C$, so $\mathbf j_1 = \mathbf k_1\times"
        r"\mathbf i_1$ points right. The plane bar–$P$ is seen edge-on, at the angle $\theta$ from the downward vertical "
        r"$-\mathbf k_1$. Its unit vector $\mathbf u$ is the hypotenuse of the shaded triangle: leg $\cos\theta$ along "
        r"$-\mathbf k_1$ and leg $\sin\theta$ along $-\mathbf j_1$; $\mathbf e_\theta = d\mathbf u/d\theta$ is perpendicular to it")
def bar_view():
    sc = Scene(520, 470, (270, 190), 165)
    C = (0.0, 0.0)
    ua = 270.0 - TH                                     # screen angle of u
    u = (math.cos(math.radians(ua)), math.sin(math.radians(ua)))
    fixed_axis(sc, C, 270, 1.55, "−" + bold("k") + S("", "1"), off=(22, 8), dashed=True)
    sc.line(C, (1.6 * u[0], 1.6 * u[1]), "HEAD", 1.6)
    sc.note((1.6 * u[0], 1.6 * u[1]), "plane bar–P", "TEXT", "end", 13, dx=-10, dy=6)
    Fk = (0.0, u[1])
    triangle(sc, [C, Fk, u])
    sc.dashed(u, Fk)
    right_angle(sc, Fk, 90, 180, 0.06)
    sc.label((0.0, u[1] / 2), "cos θ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((u[0] / 2, u[1]), "sin θ", "TEXT", "middle", 15, dy=22)
    sc.angle(C, 0.34, 270 - TH, 270, "θ", name_r=0.47)
    unit(sc, C, 0, 0.75, bold("j") + S("", "1"), off=(16, 6))
    unit(sc, C, 90, 0.75, bold("k") + S("", "1"), off=(16, 2))
    unit(sc, C, ua, 1.0, bold("u"), "ACC", off=(-14, -2))
    unit(sc, C, ua - 90, 0.75, bold("e") + S("", "θ"), "ACC", off=(-10, -10))
    sc.mass((1.35 * u[0], 1.35 * u[1]), "P", r=7, name_off=(18, 8))
    axis_out(sc, C, bold("i") + S("", "1") + " (bar)", col="BLUE", off=(46, 26))
    sc.label(C, "C", "HEAD", "start", 17, dx=14, dy=-10)
    sc.note((-1.5, 0.95), "side y₁ < 0", "TEXT", "start", 13)
    sc.note((0.45, 0.95), "side y₁ > 0", "TEXT", "start", 13)
    return sc


@figure("p36-string-plane",
        "True view of the plane that contains the bar and P: the bar to the right with O, the contact point C at distance "
        "xi, the segment CP of length l at angle phi below the bar, the shaded right triangle C E P with legs l cos phi "
        "along the bar and l sin phi along u, and the unit vectors e_CP and e_phi at P",
        r"True view of the plane bar–$P$, which contains $\mathbf i_1$ (along the bar) and $\mathbf u$ (down the page). "
        r"In the shaded right triangle $CEP$ the hypotenuse is $\ell$, the leg along the bar is $\ell\cos\varphi$ and the "
        r"leg along $\mathbf u$ is $\ell\sin\varphi$; $\overrightarrow{OP} = \xi\,\mathbf i_1 + \ell\,\mathbf e_{CP}$. "
        r"$\mathbf e_{CP}$ and $\mathbf e_\varphi = \partial\mathbf e_{CP}/\partial\varphi$ in orange")
def string_plane():
    sc = Scene(600, 500, (70, 170), 150)
    O = (0.0, 0.0)
    C = (1.6, 0.0)
    ell = 1.55
    P = (C[0] + ell * math.cos(math.radians(PHI)), -ell * math.sin(math.radians(PHI)))
    E = (P[0], 0.0)
    sc.line((-0.2, 0.0), (3.3, 0.0), "HEAD", 5.0)
    sc.label((3.3, 0.0), "bar", "HEAD", "start", 15, italic=False, dx=10, dy=5)
    triangle(sc, [C, E, P])
    sc.line(C, P, "EDGE", 1.8)
    sc.dashed(E, P)
    right_angle(sc, E, 180, 270, 0.07)
    sc.dim((0.0, 0.42), (C[0], 0.42), "ξ", off=(0, -10))
    sc.dashed(C, (C[0], 0.5))
    sc.label(((C[0] + E[0]) / 2, 0.0), "ℓ cos φ", "TEXT", "middle", 15, dy=-12)
    sc.label((E[0], P[1] / 2), "ℓ sin φ", "TEXT", "start", 15, dx=10, dy=5)
    sc.label(((C[0] + P[0]) / 2, (C[1] + P[1]) / 2), "ℓ", "TEXT", "end", 17, dx=-12, dy=4)
    sc.angle(C, 0.36, -PHI, 0, "φ", name_r=0.5)
    unit(sc, O, 0, 0.6, bold("i") + S("", "1"), off=(2, 24))
    unit(sc, (0.55, -0.45), 270, 0.5, bold("u"), "ACC", off=(16, 4))
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=-8)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "middle", 17, dx=-14, dy=-12)
    sc.dotp(E, 3.5)
    sc.label(E, "E", "HEAD", "start", 17, dx=8, dy=-10)
    unit(sc, P, -PHI, 0.5, bold("e") + S("", "CP"), "ACC", off=(18, 6))
    unit(sc, P, 180 + 90 - PHI, 0.5, bold("e") + S("", "φ"), "ACC", off=(-12, 16))
    sc.mass(P, "P", r=7, name_off=(20, -6))
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


def _ob(x, y, z, ax=-25.0, ay=30.0, sy=0.6):
    """Oblique projection of body coordinates (x1, y1, z1): x1 at `ax` degrees, y1 at `ay` degrees scaled by `sy`, z1 vertical."""
    cx, sx = math.cos(math.radians(ax)), math.sin(math.radians(ax))
    cy, sy_ = math.cos(math.radians(ay)) * sy, math.sin(math.radians(ay)) * sy
    return (x * cx + y * cy, x * sx + y * sy_ + z)


@figure("p36-contact",
        "Close-up of the contact point C: the bar, the two segments of string towards A and towards P making equal angles "
        "with the bar, the two pulls T e_CA and T e_CP, the push N_b of the bar normal to it, and the dashed components of "
        "the two unit vectors along the bar",
        r"The piece of string at $C$ is massless, so the two equal pulls and the push $\mathbf N_b$ of the bar add up to "
        r"zero. The smooth bar pushes only across itself, so the components of $\mathbf e_{CA}$ and $\mathbf e_{CP}$ along "
        r"the bar are opposite: both segments make the same angle with the bar.")
def contact():
    k = 170.0
    sc = Scene(760, 570, (370, 300), k)
    ex = (1.0, 0.0)
    ey = (0.5 * math.cos(math.radians(30)), 0.5 * math.sin(math.radians(30)))
    ez = (0.0, 1.0)

    def pr(v):
        return (v[0] * ex[0] + v[1] * ey[0] + v[2] * ez[0], v[0] * ex[1] + v[1] * ey[1] + v[2] * ez[1])
    eca = pr((-0.5, 0.35, 0.79))
    ecp = pr((0.5, -0.20, -0.84))
    nb = pr((0.0, -0.75, 0.25))                           # N_b scaled by 5: (0, -0.15, 0.05) x 5
    C = (0.0, 0.0)
    # bar
    sc.line((-1.9, 0.0), (2.0, 0.0), "HEAD", 5.0)
    sc.label((2.0, 0.0), "bar, " + S(bold("i"), "1"), "HEAD", "end", 16, weight="700", dy=-12)
    # plane normal to the bar: dashed line along z1 through C (in the plane y1 z1)
    sc.line((0.0, -1.3), (0.0, 1.45), "EDGE", 1.1, "5 4")
    sc.label((0.0, 1.45), "plane normal to the bar", "TEXT", "start", 14, italic=False, dx=8, dy=4)
    # string segments, 1.2 units long
    sc.line(C, (1.2 * eca[0], 1.2 * eca[1]), "HEAD", 2.4)
    sc.line(C, (1.2 * ecp[0], 1.2 * ecp[1]), "HEAD", 2.4)
    sc.label((1.2 * eca[0], 1.2 * eca[1]), "to A", "HEAD", "middle", 17, italic=False, dy=-12)
    sc.label((1.2 * ecp[0], 1.2 * ecp[1]), "to P", "HEAD", "middle", 17, italic=False, dy=26)
    # the components along the bar (dashed drop lines) and the equal angles
    a_, p_ = (eca[0], 0.0), (ecp[0], 0.0)
    sc.dashed(a_, eca)
    sc.dashed(p_, ecp)
    sc.dotp(eca, 3.5)
    sc.dotp(ecp, 3.5)
    sc.dotp(a_, 3.0, "TEXT")
    sc.dotp(p_, 3.0, "TEXT")
    sc.label((0.0, 0.0), S(bold("e"), "CP") + " · " + S(bold("i"), "1") + " = − " + S(bold("e"), "CA") + " · " + S(bold("i"), "1"),
             "TEXT", "start", 15, dx=128, dy=34)
    aca = math.degrees(math.atan2(eca[1], eca[0]))
    acp = math.degrees(math.atan2(ecp[1], ecp[0]))
    sc.arc(C, 0.62, aca, 180.0, "GREEN", 1.6)
    sc.label((0.78 * math.cos(math.radians((aca + 180) / 2)), 0.78 * math.sin(math.radians((aca + 180) / 2))), "π − φ", "GREEN",
             "middle", 16, dy=5)
    sc.arc(C, 0.62, acp, 0.0, "GREEN", 1.6)
    sc.label((0.80 * math.cos(math.radians(acp / 2)), 0.80 * math.sin(math.radians(acp / 2))), "φ", "GREEN", "middle", 17, dy=5)
    # pulls and push on the string element at C (pulls shifted off the string)
    def shifted(u, d):
        L = math.hypot(*u)
        return (-u[1] / L * d, u[0] / L * d)
    oa = shifted(eca, 0.075)
    op = shifted(ecp, 0.075)
    sc.vec((oa[0], oa[1]), (oa[0] + 0.8 * eca[0], oa[1] + 0.8 * eca[1]), None, "PINK", 2.8, head=11)
    sc.label((oa[0] + 0.8 * eca[0], oa[1] + 0.8 * eca[1]), "T " + S(bold("e"), "CA"), "PINK", "end", 16, weight="700", dx=-8, dy=-4)
    sc.vec((op[0], op[1]), (op[0] + 0.8 * ecp[0], op[1] + 0.8 * ecp[1]), None, "PINK", 2.8, head=11)
    sc.label((op[0] + 0.8 * ecp[0], op[1] + 0.8 * ecp[1]), "T " + S(bold("e"), "CP"), "PINK", "start", 16, weight="700", dx=8, dy=6)
    sc.vec(C, nb, None, "PINK", 2.8, head=11)
    sc.label(nb, S(bold("N"), "b") + " (×5) = −T(" + S(bold("e"), "CA") + " + " + S(bold("e"), "CP") + ")", "PINK", "end", 16,
             weight="700", dx=-6, dy=30)
    sc.dotp(C, 4.5)
    sc.label(C, "C", "HEAD", "start", 17, dx=10, dy=-10)
    # frame of the bar
    O3 = (-1.65, -1.05)
    unit(sc, O3, 0, 0.5, S(bold("i"), "1"), off=(4, 22))
    unit(sc, O3, 30, 0.5 * 0.6, S(bold("j"), "1"), off=(14, -2))
    unit(sc, O3, 90, 0.5, S(bold("k"), "1"), off=(-16, 4))
    sc.note((-1.9, -1.35), "oblique view of the bar frame (y₁ drawn at half scale)", "TEXT", "start", 13)
    return sc


@figure("p36-fbd",
        "Free-body diagram of the particle in the bar frame, in an oblique view: the string from A over the contact point "
        "C to P, the weight, the pull of the string towards C, and the horizontal centrifugal and Coriolis forces, with "
        "the relative velocity at the start",
        r"Forces on $P$ in $S_1$: the weight, the pull $-T\,\mathbf e_{CP}$ of the string towards $C$, the centrifugal "
        r"force $m\omega^2(x\,\mathbf i_1 + y\,\mathbf j_1)$ away from the vertical axis through $O$ and the Coriolis "
        r"force (dashed, both horizontal). The bar acts on the string at $C$, not on $P$.")
def fbd():
    k = 135.0
    sc = Scene(780, 700, (300, 285), k)
    R, h, L = 1.0, 1.0, 2.2
    wt, xi, th = math.radians(25), 1.1, math.radians(20)
    A3 = (R * math.cos(wt), -R * math.sin(wt), h)
    AC = math.sqrt(xi * xi - 2 * R * xi * math.cos(wt) + R * R + h * h)
    cphi = (xi - R * math.cos(wt)) / AC
    phi = math.acos(cphi)
    ell = L - AC
    C3 = (xi, 0.0, 0.0)
    P3 = (xi + ell * cphi, -ell * math.sin(phi) * math.sin(th), -ell * math.sin(phi) * math.cos(th))
    O = _ob(0, 0, 0)
    A = _ob(*A3)
    C = _ob(*C3)
    P = _ob(*P3)
    # vertical axis through O with the rotation
    sc.line((0.0, -0.45), (0.0, 1.75), "EDGE", 1.4, "10 3 2 3")
    spin_about_vertical(sc, (0.0, 1.6), 0.3, 0.08, "ω")
    sc.label((0.0, -0.45), "vertical axis through O", "TEXT", "middle", 13, italic=False, dy=20)
    # bar (x1) with i1 on it, y1 and z1 at O
    bar_end = _ob(2.5, 0, 0)
    sc.line(_ob(-0.25, 0, 0), bar_end, "HEAD", 4.5)
    sc.label(bar_end, "bar", "HEAD", "start", 16, italic=False, dx=10, dy=8)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=24)
    sc.dotp(O, 4.0)
    unit(sc, O, -25, 0.5, S(bold("i"), "1"), off=(4, 24))
    unit(sc, O, 30, 0.45 * 0.6 / 0.6 * 0.6, S(bold("j"), "1"), off=(16, -2))
    unit(sc, O, 90, 0.45, S(bold("k"), "1"), off=(-16, 4))
    # string A - C - P
    sc.line(A, C, "HEAD", 2.2)
    sc.line(C, P, "HEAD", 2.2)
    sc.dotp(A, 5.0)
    sc.label(A, "A", "HEAD", "end", 17, dx=-10, dy=-8)
    sc.dotp(C, 4.5)
    sc.label(C, "C", "HEAD", "start", 17, dx=12, dy=-10)
    # forces at P
    sc.vec(P, (P[0], P[1] - 0.8), None, "PINK", 2.8, head=11)
    sc.label((P[0], P[1] - 0.8), "W = −m g " + S(bold("k"), "1"), "PINK", "start", 16, weight="700", dx=10, dy=6)
    t3 = (-(P3[0] - C3[0]), -(P3[1] - C3[1]), -(P3[2] - C3[2]))
    t3 = tuple(c / ell for c in t3)                      # -e_CP
    ts = _ob(*t3)
    t0 = (P[0] + 0.09, P[1])
    t1 = (t0[0] + 0.7 * ts[0], t0[1] + 0.7 * ts[1])
    sc.vec(t0, t1, None, "PINK", 2.8, head=11)
    sc.label(t1, "−T " + S(bold("e"), "CP"), "PINK", "start", 16, weight="700", dx=8, dy=-2)
    hx, hy = P3[0], P3[1]
    hn = math.hypot(hx, hy)
    hv = _ob(hx / hn, hy / hn, 0.0)
    f1 = (P[0] + 0.6 * hv[0], P[1] + 0.6 * hv[1])
    _dvec(sc, P, f1, "PINK", 2.6)
    sc.label(f1, S(bold("F"), "C") + " = m ω² (x " + S(bold("i"), "1") + " + y " + S(bold("j"), "1") + ")", "PINK", "start", 16,
             weight="700", dx=10, dy=4)
    sc.label(f1, "(inertia)", "PINK", "start", 14, dx=10, dy=22)
    ci = _ob(-1.0, 0.0, 0.0)
    f2 = (P[0] + 0.5 * ci[0], P[1] + 0.5 * ci[1])
    _dvec(sc, P, f2, "PINK", 2.6)
    sc.label(f2, S(bold("F"), "COR") + " = −2 m ω " + S(bold("k"), "1") + " × " + S(bold("v"), "1", "P") + " (inertia)", "PINK",
             "end", 16, weight="700", dx=-8, dy=-30)
    sc.label(f2, "(drawn for the initial relative velocity −ωR " + S(bold("j"), "1") + ")", "PINK", "end", 14, dx=-8, dy=-10)
    vj = _ob(0.0, -1.0, 0.0)
    v1 = (P[0] + 0.5 * vj[0], P[1] + 0.5 * vj[1])
    sc.vec(P, v1, None, "ACC", 2.6, head=11)
    sc.label(v1, S(bold("v"), "1", "P") + "(0) = −ω R " + S(bold("j"), "1"), "ACC", "end", 16, weight="700", dx=-8, dy=14)
    sc.mass(P, "P", r=7, name_off=(30, 2))
    sc.note((-2.0, -2.45), "oblique view of the bar frame", "TEXT", "start", 13)
    sc.note((-2.0, -2.45), "(y₁ drawn at 0.6 scale)", "TEXT", "start", 13, dy=17)
    return sc
