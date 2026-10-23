"""Problem 36: pendulum string dragged by a bar that turns about the vertical through its centre O."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

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
