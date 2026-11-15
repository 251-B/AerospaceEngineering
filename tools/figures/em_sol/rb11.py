"""Problem RB-11: vertical disc rolling without slipping round a circle, axis through the point O1 on Oz."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, arrow_px, d, p3, p3v, ring, rotation_view, sub, vadd, vscale
from figures.mech import S, Scene, bold, dot1

PHI = 40.0


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


@figure("rb11-overview",
        "Vertical disc rolling round a circle with its axis through the point O1 on Oz, the basis i1, j1, k1 at its "
        "centre and the instantaneous axis through the contact point and O1.",
        r"The disc, its centre $G$ on the circle of centre $O_1$, the contact point $C$ and the basis "
        r"$\{\mathbf i_1, \mathbf j_1, \mathbf k_1\}$ of the key; the instantaneous axis is the line $CO_1$.")
def overview():
    sc = Scene(720, 610, (270, 420), 185)
    R = 1.0
    cp, sp = math.cos(math.radians(PHI)), math.sin(math.radians(PHI))
    i1, j1, k1 = (cp, sp, 0.0), (-sp, cp, 0.0), (0.0, 0.0, 1.0)
    ex, ey, ez = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)
    O, O1 = (0.0, 0.0, 0.0), (0.0, 0.0, R)
    G, C = (R * cp, R * sp, R), (R * cp, R * sp, 0.0)
    # fixed axes
    for tip, nm, off in ((vscale(ex, 1.55), "x", (-12, 14)), (vscale(ey, 1.6), "y", (12, 12)),
                         (vscale(ez, 1.75), "z", (-12, 2))):
        sc.vec((0.0, 0.0), p3v(tip), None, "EDGE", 1.4, head=8)
        sc.label(p3v(tip), bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # circle of G (dashed, at z = R) and its sense, contact circle on Oxy
    sc.poly(ring(O1, ex, ey, R), "EDGE", 1.3, "6 4")
    pts = ring(O1, ex, ey, R, 150, 215, 12)
    sc.poly(pts, "EDGE", 1.8)
    arrow_px(sc, pts[-3], pts[-1], "EDGE", 10)
    sc.poly(ring(O, ex, ey, R), "EDGE", 1.0, "3 4")
    # the disc: circle of radius R in the plane (j1, k1) centred at G
    disc = ring(G, j1, k1, R)
    sc.poly(disc, "ACC", 0.0, fill="ACC", close=True, opacity=0.16)
    sc.poly(disc, "ACC", 2.0, close=True)
    # axis of the disc and instantaneous axis
    sc.line(p3v(O1), p3v(vadd(G, i1, 0.35)), "HEAD", 1.6)
    ax_dir = vadd(C, O1, -1.0)
    sc.line(p3v(vadd(C, ax_dir, 0.30)), p3v(vadd(O1, ax_dir, -0.30)), "GREEN", 1.6, "7 5")
    sc.dashed(p3v(O), p3v(C))
    # basis at G
    sc.vec(p3v(G), add(p3v(G), p3v(vscale(i1, 0.55))), _ax("i", "1"), "BLUE", 2.8, name_off=(-16, 14), size=17, head=11)
    sc.vec(p3v(G), add(p3v(G), p3v(vscale(k1, 0.55))), _ax("k", "1"), "BLUE", 2.8, name_off=(-14, -2), size=17, head=11)
    sc.vec(p3v(G), add(p3v(G), p3v(vscale(j1, 0.45))), _ax("j", "1"), "BLUE", 2.8, name_off=(2, 20), size=17, head=11)
    off = (0.0, 0.07)
    sc.vec(add(p3v(G), off), add(add(p3v(G), off), p3v(vscale(j1, 1.0))), sub("v", "0", "G"), "ACC", 2.2,
           name_off=(14, -10), size=17, head=10)
    # angle phi in the plane Oxy
    pts = ring(O, ex, ey, 0.42, 0, PHI, 16)
    sc.poly(pts, "GREEN", 1.7)
    arrow_px(sc, pts[-3], pts[-1], "GREEN", 9)
    sc.label(p3v(vadd(O, vadd(vscale(ex, 0.60 * math.cos(math.radians(PHI / 2))), ey, 0.60 * math.sin(math.radians(PHI / 2))))),
             "φ", "GREEN", "middle", 17, dy=6)
    for pt, nm, off2 in ((O1, sub("O", "1"), (-18, 4)), (G, "G", (-16, 20)), (C, "C", (14, 18))):
        sc.mass(p3v(pt), None, r=5, col="BLUE")
        sc.label(p3v(pt), nm, "HEAD", "middle", 17, dx=off2[0], dy=off2[1])
    sc.dotp((0.0, 0.0), 3.5)
    sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=14, dy=20)
    sc.note(p3v(vadd(C, ax_dir, 0.30)), "instantaneous axis", "GREEN", "start", 13, dx=8, dy=14)
    return sc


@figure("rb11-rotation-phi",
        "Top view showing the angle phi of the radial unit vector i1 and the disc seen edge-on, perpendicular to it.",
        r"View from above ($\mathbf k$ out of the paper). The frame $S_1$ turns counterclockwise by $\varphi$; the disc, "
        r"seen edge-on, is perpendicular to $\mathbf i_1$ and moves along $\mathbf j_1$.")
def rotation_phi():
    R = 1.0
    c, s = math.cos(math.radians(PHI)), math.sin(math.radians(PHI))

    def pre(sc):
        sc.circle((0.0, 0.0), R, "EDGE", 1.3, dash="6 4")
        G = (R * c, R * s)
        a, b = add(G, d(PHI + 90), R), add(G, d(PHI + 90), -R)
        sc.line(a, b, "ACC", 5.0)

    def post(sc):
        G = (R * c, R * s)
        sc.mass(G, None, r=5, col="BLUE")
        sc.label(G, "G", "HEAD", "middle", 17, dx=-20, dy=18)
        G2 = add(G, d(PHI), 0.12)
        sc.vec(G2, add(G2, d(PHI + 90), 0.55), sub("v", "0", "G"), "ACC", 2.6, name_off=(30, -10), size=17, head=10)
        sc.note(add(G, d(PHI + 90), R), "disc seen edge-on", "TEXT", "start", 13, dx=8, dy=-6)

    return rotation_view(620, 520, (230, 360), 170, PHI, _ax("i"), _ax("j"), _ax("i", "1"), _ax("j", "1"),
                         _ax("k") + " (⊙)", ("φ", ""), pre=pre, post=post, L=0.6, out_off=(-16, 28))


@figure("rb11-rotation-psi",
        "Face view of the disc showing the spin angle psi, the velocity of the centre and the zero velocity of the "
        "contact point.",
        r"Disc seen with its axis $\mathbf i_1$ out of the paper. The centre moves to the right at $\omega R$; the "
        r"no-slip condition makes the spin clockwise (negative), so that the velocity of the body point at $C$ cancels.")
def rotation_psi():
    PSI = 30.0

    def pre(sc):
        sc.circle((0.0, 0.0), 1.0, "ACC", 1.8, fill="ACC", opacity=0.12)
        sc.line((-1.9, -1.0), (1.9, -1.0), "HEAD", 3.0)
        sc.note((1.9, -1.0), "plane Oxy", "TEXT", "end", 13, dy=18)

    def post(sc):
        C = (0.0, -1.0)
        sc.vec((0.0, 0.0), (0.0, -0.97), None, "HEAD", 1.2, head=8)
        sc.label((0.0, -0.5), "GC = −R " + _ax("k", "1"), "HEAD", "start", 15, dx=10, dy=4)
        sc.mass(C, None, r=5, col="BLUE")
        sc.label(C, "C", "HEAD", "middle", 17, dx=-12, dy=-12)
        sc.vec(C, (0.62, -1.0), None, "ACC", 2.6, head=10)
        sc.label((0.62, -1.0), "ωR " + _ax("j", "1"), "ACC", "start", 15, dx=6, dy=-8)
        sc.vec(C, (-0.62, -1.0), None, "PINK", 2.6, head=10)
        sc.label((-0.62, -1.0), "ω × GC", "PINK", "end", 15, dx=-6, dy=-8)
        sc.note((0.0, -1.0), sub("v", "0", "C") + "(B) = 0", "HEAD", "middle", 15, dy=26)
        sc.vec((0.0, 0.05), (1.3, 0.05), None, "ACC", 2.0, head=9)
        sc.label((1.3, 0.05), sub("v", "0", "G") + " = ωR " + _ax("j", "1"), "ACC", "start", 15, dx=2, dy=-30)
        sc.spin((0.0, 0.0), 1.32, 160, 50, "ψ̇ = −ω", name_r=1.62)

    return rotation_view(700, 560, (300, 300), 150, PSI, _ax("j", "1"), _ax("k", "1"), _ax("j", "B"), _ax("k", "B"),
                         _ax("i", "1") + " (⊙)", ("ψ", ""), pre=pre, post=post, out_off=(-16, 28))


@figure("rb11-meridian",
        "Meridian plane with the right triangle O1, G, C, the instantaneous axis along its hypotenuse and the "
        "acceleration of the contact point of the disc.",
        r"Meridian plane through $G$ ($\mathbf j_1$ into the paper). The axis of the disc is the leg $O_1G$, the contact "
        r"radius the leg $GC$; the instantaneous axis is the hypotenuse $CO_1$, at 45 degrees, parallel to "
        r"$\boldsymbol\omega_{B0}$.")
def meridian():
    sc = Scene(760, 540, (150, 430), 180)
    O, O1, G, C = (0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)
    triangle(sc, [O1, G, C], "BLUE", 0.14)
    sc.vec(O, (0.0, 1.95), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 1.95), bold("z") + " (" + _ax("k", "1") + ")", "TEXT", "middle", 16, dx=0, dy=-8)
    sc.line((-0.35, 0.0), (2.35, 0.0), "EDGE", 1.4)
    sc.note((2.35, 0.0), "plane Oxy", "TEXT", "end", 13, dy=18)
    # the disc seen edge-on
    sc.line((1.0, 0.0), (1.0, 2.0), "ACC", 6.0)
    sc.line(O1, G, "HEAD", 1.6)
    right_angle(sc, G, 180, 270, 0.09)
    # instantaneous axis
    ux, uy = -1.0, 1.0
    sc.line((1.35, -0.35), (-0.35, 1.35), "GREEN", 1.6, "7 5")
    sc.note((1.35, -0.35), "instantaneous axis", "GREEN", "start", 13, dx=8, dy=8)
    sc.arc(C, 0.42, 135, 180, "GREEN", 1.6)
    sc.label(add(C, d(157.5), 0.74), "45°", "GREEN", "middle", 15, dy=5)
    # omega_B0 and its two legs
    kw = 0.45
    tip = (1.0 - kw, kw)
    sc.line((1.0, 0.0), (1.0 - kw, 0.0), "GREEN", 1.1, "4 3")
    sc.line((1.0 - kw, 0.0), tip, "GREEN", 1.1, "4 3")
    sc.line((1.0, kw), tip, "GREEN", 1.1, "4 3")
    sc.vec(C, tip, None, "GREEN", 3.2, head=12)
    sc.label((0.95, 0.0), sub("ω", "B0") + " = ω(−" + _ax("i", "1") + " + " + _ax("k", "1") + ")", "GREEN", "end", 16,
             weight="700", dx=0, dy=44)
    sc.label((1.0 - kw / 2, 0.0), "−ω " + _ax("i", "1"), "GREEN", "middle", 14, dy=-16)
    sc.label((1.0, kw / 2), "ω " + _ax("k", "1"), "GREEN", "start", 14, dx=8, dy=0)
    # accelerations
    ka = 0.5
    sc.vec(C, (1.0 + ka * 0.7071, ka * 0.7071), None, "PINK", 3.0, head=11)
    sc.label((1.0 + ka * 0.7071, ka * 0.7071), sub("a", "0", "C") + "(B) = ω²R(" + _ax("i", "1") + " + " + _ax("k", "1") + ")",
             "PINK", "start", 16, weight="700", dx=10, dy=-6)
    sc.vec(G, (1.0 - ka, 1.0), None, "BLUE", 3.0, head=11)
    sc.label((1.0 - ka / 2, 1.0), sub("a", "0", "G") + " = −ω²R " + _ax("i", "1"), "BLUE", "end", 16, weight="700",
             dx=34, dy=-14)
    # legs and hypotenuse
    sc.label((0.5, 1.0), "R", "TEXT", "middle", 16, dy=22)
    sc.label((1.0, 0.5), "R", "TEXT", "end", 16, dx=-8, dy=5)
    sc.label((0.5, 0.5), "R√2", "TEXT", "start", 16, dx=8, dy=-6)
    axis_in(sc, (1.62, 1.35), None, "HEAD")
    sc.label((1.62, 1.35), _ax("j", "1"), "HEAD", "start", 16, weight="700", dx=14, dy=5)
    for pt, nm, off in ((O, "O", (-14, 18)), (O1, sub("O", "1"), (-18, -4)), (G, "G", (18, -12)), (C, "C", (14, 18))):
        sc.mass(pt, None, r=5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    return sc
