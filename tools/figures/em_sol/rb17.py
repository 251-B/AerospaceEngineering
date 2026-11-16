"""Problem RB-17: constrained pizza cutter (fork turning about AB with the angle theta, disc turning about CD with phi).

This module also holds `rot_pair`, the view of one elementary rotation drawn at an arbitrary orientation, shared with
rb20 and rb21.
"""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.mech import S, Scene, bold

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I1, K1 = S(I, "1"), S(K, "1")
I2, J2, K2 = S(I, "2"), S(J, "2"), S(K, "2")
J0, K0 = S(J, "0"), S(K, "0")
THETA, PHI = 30.0, 35.0
A_, B_, R_ = 2.0, 4.0, 1.2


def off_dir(deg, r=17.0, bump=5.0):
    """Pixel shift of a label placed just beyond the tip of a vector at `deg` (screen y points down)."""
    return (r * math.cos(math.radians(deg)), -r * math.sin(math.radians(deg)) + bump)


def rot_pair(sc, ang, names, hdr, out, out_kind="out", out_off=(-16, 26), ref=0.0, s=1, L=1.0, Lf=1.62, col="BLUE",
             tri="ACC", arc_r=0.5, hyp="1", o=(0.0, 0.0), arc_lab=None, lab_offs=(None, None), inner2=False, out_anchor="end"):
    """One elementary rotation by `ang` degrees, counterclockwise as seen, at the point o.

    The two old axes are at `ref` (first) and `ref + 90 s` (second); names = (first, second, rotated first, rotated
    second). Each rotated axis has its right triangle: adjacent leg along the old axis (cosine), dashed opposite leg
    (sine), hypotenuse L. `arc_lab` = ((dx, dy), (dx, dy)) pixel shifts of the two angle labels."""
    a1, a2 = ref, ref + 90.0 * s
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    nm1, nm2, nm3, nm4 = names
    fixed_axis(sc, o, a1, Lf, nm1, off=off_dir(a1, 18))
    fixed_axis(sc, o, a2, Lf, nm2, off=off_dir(a2, 18))
    for (a, nm_new), lo in zip(((a1, nm3), (a2, nm4)), lab_offs):
        foot, tip = add(o, d(a), L * c), add(o, d(a + ang), L)
        triangle(sc, [o, foot, tip], tri, 0.20)
        sc.dashed(foot, tip)
        right_angle(sc, foot, a + 180, a + 90, 0.07)
        unit(sc, o, a + ang, L, nm_new, col, off=lo or off_dir(a + ang, 17))
        # leg labels, pushed away from the triangle
        cen = ((o[0] + foot[0] + tip[0]) / 3, (o[1] + foot[1] + tip[1]) / 3)
        for p, q, txt in ((o, foot, "cos " + hdr), (foot, tip, "sin " + hdr)):
            mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
            vx, vy = mid[0] - cen[0], mid[1] - cen[1]
            n = math.hypot(vx, vy) or 1.0
            f = -1.0 if (inner2 and a == a2 and txt.startswith("cos")) else 1.0
            sc.label(mid, txt, "TEXT", "middle", 15, dx=f * vx / n * 30, dy=-f * vy / n * 20 + 5)
        if hyp:
            q = d(a + ang + 90)
            sc.label(add(o, d(a + ang), L * 0.55), hyp, "TEXT", "middle", 14, dx=13 * q[0], dy=-13 * q[1] + 5)
    for a, k in ((a1, 0), (a2, 1)):
        sc.arc(o, arc_r, a, a + ang, "GREEN", 1.7, head=True)
        dx, dy = off_dir(a + ang / 2, 14, 5)
        if arc_lab:
            dx, dy = arc_lab[k]
        sc.label(add(o, d(a + ang / 2), arc_r), hdr, "GREEN", "middle", 17, dx=dx, dy=dy)
    (axis_out if out_kind == "out" else axis_in)(sc, o, None, "HEAD")
    sc.label(o, out, "HEAD", out_anchor, 16, weight="700", dx=out_off[0], dy=out_off[1])


def rod_box(sc, p, ang, half, width_px, fill_op=0.35):
    """Edge-on disc or wheel: thick light-grey segment of half-length `half` along `ang`, with an outline."""
    n = d(ang + 90)
    w = width_px / sc.k / 2
    a, b = add(p, d(ang), -half), add(p, d(ang), half)
    pts = [add(a, n, w), add(b, n, w), add(b, n, -w), add(a, n, -w)]
    sc.poly(pts, "HEAD", 1.4, fill="EDGE", close=True, opacity=fill_op)


# ------------------------------------------------------------------------------------------------ rb17-rot-theta
KDIR, IDIR = -90.0 + THETA, THETA          # k2 and i2 on the screen (i1 right, k1 down, j1 out of the paper)


def _arm(sc, o1, extra=True):
    G = add(o1, d(KDIR), A_)
    O = add(o1, d(KDIR), B_)
    return G, O


@figure("rb17-rot-theta",
        "Vertical plane of the fork arm with the fixed basis i1, k1, the fork basis i2, k2 turned by theta about the axis "
        "AB, and the points G and O on the arm.",
        r"Rotation about $\mathbf j_1$ (⊙) by $\theta$: $\mathbf i_2 = \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k_1$, "
        r"$\mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1$; $G$ and $O$ lie on the arm at the distances "
        r"$a$ and $b$ from $O_1$.")
def rot_theta():
    sc = Scene(780, 740, (270, 112), 100)
    O1 = (0.0, 0.0)
    G, O = _arm(sc, O1)
    # disc edge-on (under the arm) and the arm
    rod_box(sc, O, KDIR, R_, 15)
    sc.line(O1, O, "EDGE", 5.0)
    sc.line(add(O, d(IDIR), -1.0), add(O, d(IDIR), 1.25), "EDGE", 1.4, "7 4")
    sc.label(add(O, d(IDIR), 1.25), "CD", "TEXT", "start", 16, weight="700", dx=8, dy=0)
    sc.label(add(O, d(KDIR), R_), "disc, edge-on", "TEXT", "start", 14, italic=False, dx=16, dy=12)
    # triangles, arcs and the bases (k1 drawn down)
    rot_pair(sc, THETA, (I1, K1, I2, K2), "θ", "AB, " + J1_OUT, "out", (-12, -20), ref=0.0, s=-1, arc_r=0.6, L=1.5,
             Lf=1.9, arc_lab=((18, 8), (-12, 22)), lab_offs=(None, (26, 12)))
    # AB end-on at O1
    sc.line((-0.55, 0.0), (-0.1, 0.0), "EDGE", 1.6)
    for k in range(5):
        sc.line((-0.55 + 0.1 * k, 0.0), (-0.65 + 0.1 * k, 0.1), "EDGE", 1.0)
    # points G, O with the dimensions a and b (lower-left of the arm)
    nl = d(KDIR - 90.0)
    for p, dist, nm, no in ((G, 1.3, "a", (-14, 4)), (O, 2.0, "b", (-14, 4))):
        pa, qa = add(O1, nl, dist), add(p, nl, dist)
        sc.dim(pa, qa, nm, off=no)
        sc.dashed(O1, add(O1, nl, dist + 0.12))
        sc.dashed(p, add(p, nl, dist + 0.12))
    for p, nm, off in ((G, "G", (16, -8)), (O, "O", (-22, 6))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    # weights
    sc.vec(G, add(G, (0.0, -1.0), 1.0), "Mg", "PINK", 3.0, name_off=(-24, 6), size=17, head=12)
    sc.vec(O, add(O, (0.0, -1.0), 1.1), "mg", "PINK", 3.0, name_off=(24, 6), size=17, head=12)
    return sc


J1_OUT = S(bold("j"), "1") + " (⊙)"


# ------------------------------------------------------------------------------------------------ rb17-rot-phi
@figure("rb17-rot-phi",
        "The disc seen along its axis, with the fork basis j2, k2 and the disc basis j0, k0 turned by phi about i2.",
        r"Rotation about $\mathbf i_2$ (⊙) by $\varphi$: $\mathbf j_0 = \cos\varphi\,\mathbf j_2 + \sin\varphi\,\mathbf k_2$, "
        r"$\mathbf k_0 = -\sin\varphi\,\mathbf j_2 + \cos\varphi\,\mathbf k_2$. The sense of $\varphi$ is a reading of the "
        r"statement figure.")
def rot_phi():
    Rs = 2.75
    sc = Scene(820, 760, (410, 380), 100)
    O = (0.0, 0.0)
    sc.poly([(Rs * math.cos(math.radians(t)), Rs * math.sin(math.radians(t))) for t in range(0, 361, 4)], "HEAD", 1.8,
            fill="EDGE", close=True, opacity=0.08)
    rot_pair(sc, PHI, (J2, K2, J0, K0), "φ", I2 + " (⊙)", "out", (-18, 30), L=1.3, Lf=1.9, col=ORANGE, tri="BLUE",
             arc_r=0.78)
    # mark painted on the disc at the tip direction of j0
    mk = add(O, d(PHI), Rs)
    sc.dashed(add(O, d(PHI), 1.3), mk)
    sc.mass(mk, None, r=5, col="ACC")
    sc.label(mk, "mark", "HEAD", "start", 15, dx=12, dy=-6)
    sc.dashed(O, add(O, d(-45), Rs))
    sc.label(add(O, d(-45), Rs / 2), "R", "TEXT", "start", 16, dx=8, dy=14)
    # rate of phi about i2
    sc.spin(O, 2.15, 150.0, 230.0, "", "GREEN")
    sc.label(add(O, d(200.0), 2.15), "rate of φ, about " + I2, "GREEN", "start", 15, weight="700", dx=14, dy=20)
    # towards O1
    sc.vec((0.0, -Rs - 0.15), (0.0, -Rs - 0.75), None, "EDGE", 1.6, head=9)
    sc.label((0.0, -Rs - 0.75), "towards " + "O<tspan baseline-shift=\"sub\" font-size=\"70%\">1</tspan>", "TEXT", "start", 15,
             italic=False, dx=14, dy=6)
    return sc


# ------------------------------------------------------------------------------------------------ rb17-exploded
def _force_pair(sc, p, sx, sz, nx, nz, nr, col, size, lx, lz, lr):
    """Force with its two components along i2 and k2 (signs sx, sz): the x component from p, the z component from its tip
    (so no arrow lies on the arm), and the resultant. lx, lz, lr: (anchor, dx, dy) of the three labels."""
    a = add(p, d(IDIR), sx * size)
    tip = add(a, d(KDIR), sz * size)
    sc.vec(p, a, None, col, 2.0, head=10)
    sc.vec(a, tip, None, col, 2.0, head=10)
    sc.vec(p, tip, None, col, 3.2, head=12)
    for pt, nm, (an, dx, dy) in ((((p[0] + a[0]) / 2, (p[1] + a[1]) / 2), nx, lx),
                                 (((a[0] + tip[0]) / 2, (a[1] + tip[1]) / 2), nz, lz), (tip, nr, lr)):
        sc.label(pt, nm, col, an, 15 if pt is not tip else 17, weight="700", dx=dx, dy=dy)
    return tip


@figure("rb17-exploded",
        "Exploded view of the fork and the disc with the pin loads at O1, the bearing pair at O and the two weights.",
        r"Exploded view: the bearing acts on the disc with $\mathbf R_O$, $\mathbf Q_O$ (no component along $\mathbf i_2$) "
        r"and on the fork with $-\mathbf R_O$, $-\mathbf Q_O$; the pin acts on the fork with $\mathbf R_{O_1}$, "
        r"$\mathbf Q_{O_1}$ (no component along $\mathbf j_2$).")
def exploded():
    sc = Scene(960, 900, (330, 130), 92)
    ix, iz = d(IDIR), d(KDIR)
    O1 = (0.0, 0.0)
    G, O = add(O1, iz, A_), add(O1, iz, B_)
    Od = add(O, iz, 2.0)                                     # the disc, shifted 2 units along k2
    sub = lambda t: '<tspan baseline-shift="sub" font-size="70%">' + t + '</tspan>'
    sc.note((-0.9, 0.95), "FORK", "HEAD", "start", 15)
    sc.note((Od[0] + 0.9, Od[1] - 1.25), "DISC", "HEAD", "start", 15)
    sc.line(O1, O, "HEAD", 5.0)
    sc.mass(O1, None, r=5, col="BLUE")
    sc.label(O1, "O" + sub("1"), "HEAD", "middle", 17, dx=-22, dy=-10)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=18, dy=-8)
    sc.mass(O, None, r=5, col="BLUE")
    sc.label(O, "O", "HEAD", "middle", 17, dx=18, dy=-10)
    # pin force and torque at O1
    _force_pair(sc, O1, 1, 1, S("R", "1x"), S("R", "1z"), S("R", "O1"), "GREEN", 0.9, ("middle", 0, -10), ("start", 12, 4),
                ("start", 6, 24))
    sc.spin(O1, 0.55, 110.0, 215.0, "", "GREEN")
    sc.label(add(O1, d(200.0), 0.55), S("Q", "O1") + " (along " + I2 + " and " + K2 + " only)", "GREEN", "end", 15, weight="700",
             dx=-12, dy=16)
    # weight of the fork
    sc.vec(G, add(G, (0.0, -1.0), 0.8), "Mg", "PINK", 3.0, name_off=(-24, 6), size=17, head=12)
    # reaction of the bearing on the fork: -R_O and -Q_O
    _force_pair(sc, O, -1, -1, "−" + S("R", "O,x"), "−" + S("R", "O,z"), "−" + S("R", "O"), ORANGE, 0.9, ("middle", 0, 22),
                ("end", -10, 14), ("end", -6, -12))
    sc.spin(O, 0.5, 70.0, -40.0, "", ORANGE)
    sc.label(add(O, d(15.0), 0.5), "−" + S("Q", "O"), ORANGE, "start", 16, weight="700", dx=14, dy=-6)
    # the disc alone
    rod_box(sc, Od, KDIR, R_, 15)
    sc.mass(Od, None, r=5, col="BLUE")
    sc.label(Od, "O", "HEAD", "middle", 17, dx=-20, dy=-8)
    _force_pair(sc, Od, 1, 1, S("R", "O,x"), S("R", "O,z"), S("R", "O"), ORANGE, 0.9, ("middle", 0, -10), ("start", 12, 4),
                ("start", 6, 24))
    sc.spin(Od, 0.5, 150.0, 260.0, "", ORANGE)
    sc.label(add(Od, d(205.0), 0.5), S("Q", "O") + " (along " + J2 + " and " + K2 + " only)", ORANGE, "end", 15,
             weight="700", dx=-12, dy=10)
    sc.vec(Od, add(Od, (0.0, -1.0), 0.9), "mg", "PINK", 3.0, name_off=(-24, 6), size=17, head=12)
    # action-reaction link
    sc.dashed(O, Od)
    mid = ((O[0] + Od[0]) / 2, (O[1] + Od[1]) / 2)
    sc.note(mid, "action – reaction pair", "TEXT", "end", 13, dx=-14, dy=4)
    # basis
    b0 = (5.2, -0.3)
    sc.vec(b0, add(b0, ix, 0.9), I2, "BLUE", 2.6, name_off=off_dir(IDIR, 16), size=16, head=10)
    sc.vec(b0, add(b0, iz, 0.9), K2, "BLUE", 2.6, name_off=off_dir(KDIR, 16), size=16, head=10)
    axis_out(sc, b0, None, "HEAD")
    sc.label(b0, J2 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-16, dy=-10)
    return sc
