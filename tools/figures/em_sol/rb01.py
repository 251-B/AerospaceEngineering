"""Problem RB-01: three body points on the coordinate axes, velocities of a rigid body at one instant.

This module also holds the small helpers shared by the other Topic 6 problem modules (rb02 .. rb35): the cabinet
projection of the portal (x towards the lower left, y to the right, z up), vector arithmetic and the flat view of one
elementary rotation with both shaded right triangles.
"""
import math

from figures.em_solutions import (axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit)
from figures.mech import S, Scene, bold, dot1
from figures.svgkit import arrow_head

ORANGE = "ACC"


# ------------------------------------------------------------------------------------------------ shared helpers
def d(deg):
    return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def add(p, q, k=1.0):
    return (p[0] + k * q[0], p[1] + k * q[1])


DEPTH = (-0.789 * 0.6, -0.614 * 0.6)       # cabinet depth axis: x towards the lower left, foreshortened


def p3(x, y, z):
    """Cabinet projection: x towards the lower left, y to the right, z up."""
    return (x * DEPTH[0] + y, x * DEPTH[1] + z)


def p3v(v):
    return p3(*v)


def sub(sym, a, b=None):
    return S(bold(sym), a, b)


def vsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def vadd(a, b, k=1.0):
    return tuple(x + k * y for x, y in zip(a, b))


def vscale(a, k):
    return tuple(k * x for x in a)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norm(a):
    n = math.sqrt(sum(x * x for x in a))
    return tuple(x / n for x in a)


def arrow_px(sc, p0, p1, col, size=9):
    """Arrow head at the world point p1, pointing away from p0."""
    arrow_head(sc.c, sc.P(p0), sc.P(p1), col, size)


def rotation_view(w, h, o, k, ang, right, up, m1, m2, out, hdr, col="BLUE", tri="ACC", pre=None, post=None,
                  out_off=(-16, 26), out_kind="out", note=None, note_pos=(-0.75, -0.42)):
    """Flat view of one elementary rotation by `ang` degrees (counterclockwise positive in the view).

    right, up: names (SVG text) of the two old axes; m1, m2: names of the rotated copies of `right` and `up`;
    out: name of the axis normal to the paper (symbol at the origin); hdr: name of the angle.
    The two shaded right triangles (hypotenuse 1) give the components of m1 and m2 in the old axes.
    """
    sc = Scene(w, h, o, k)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    ccw = ang > 0
    L, Lf = 1.0, 1.62
    if pre:
        pre(sc)
    fixed_axis(sc, O, 0, Lf, right, off=(16, 6))
    fixed_axis(sc, O, 90, Lf, up, off=(16, 4))
    # triangle of m1: adjacent leg along `right`, opposite leg along +-`up`
    foot1, tip1 = (L * c, 0.0), (L * c, L * s)
    triangle(sc, [O, foot1, tip1], tri, 0.20)
    sc.dashed(foot1, tip1)
    right_angle(sc, foot1, 180, 90 if ccw else 270, 0.07)
    # triangle of m2: adjacent leg along `up`, opposite leg along -+`right`
    foot2, tip2 = (0.0, L * c), (-L * s, L * c)
    triangle(sc, [O, foot2, tip2], tri, 0.20)
    sc.dashed(foot2, tip2)
    right_angle(sc, foot2, 270, 180 if ccw else 0, 0.07)
    unit(sc, O, ang, L, m1, col, off=(18, -10) if ccw else (18, 18))
    unit(sc, O, ang + 90, L, m2, col, off=(-6, -14) if ccw else (6, -14))
    # leg labels
    sc.label((L * c / 2, 0), "cos " + hdr[0], "TEXT", "middle", 15, dy=24 if ccw else -8)
    sc.label((L * c, L * s / 2), "sin " + hdr[0], "TEXT", "start", 15, dx=9, dy=5)
    sc.label((-L * s / 2, L * c), "sin " + hdr[0], "TEXT", "middle", 15, dy=-8)
    if ccw:
        sc.label((0, L * c / 2), "cos " + hdr[0], "TEXT", "start", 15, dx=9, dy=18)
    else:
        sc.label((0, L * c / 2), "cos " + hdr[0], "TEXT", "end", 15, dx=-9, dy=18)
    # angle arcs with their sense
    sc.arc(O, 0.50, 0, ang, "GREEN", 1.7, head=True)
    sc.arc(O, 0.50, 90, 90 + ang, "GREEN", 1.7, head=True)
    if ccw:
        sc.label(add(O, d(ang / 2), 0.50), hdr[0], "GREEN", "middle", 17, dx=-4, dy=18)
        sc.label(add(O, d(90 + ang / 2), 0.50), hdr[0], "GREEN", "middle", 17, dx=14, dy=22)
    else:
        sc.label(add(O, d(ang / 2), 0.50), hdr[0], "GREEN", "middle", 17, dx=-2, dy=-8)
        sc.label(add(O, d(90 + ang / 2), 0.50), hdr[0], "GREEN", "middle", 17, dx=-14, dy=22)
    (axis_out if out_kind == "out" else axis_in)(sc, O, None, "HEAD")
    sc.label(O, out, "HEAD", "end", 16, weight="700", dx=out_off[0], dy=out_off[1])
    if note:
        sc.note(note_pos, note, "TEXT", "start", 13)
    if post:
        post(sc)
    return sc


# ------------------------------------------------------------------------------------------------ RB-01
@figure("rb01-three-points",
        "Points A, B and C on the three coordinate axes with their velocities, and the instantaneous axis through A "
        "parallel to j.",
        r"The three body points, their velocities and the instantaneous axis of rotation and slip, which passes through "
        r"$A$ and is parallel to $\mathbf j$.")
def three_points():
    sc = Scene(640, 520, (250, 340), 190)
    O = (0.0, 0.0)
    A, B, C = p3(1, 0, 0), p3(0, 1, 0), p3(0, 0, 1)
    triangle(sc, [A, B, C], "BLUE", 0.12)
    for p, q in ((A, B), (B, C), (C, A)):
        sc.line(p, q, "BLUE", 1.3, "6 4")
    # fixed axes
    for tip, nm, off in ((p3(1.45, 0, 0), bold("i"), (-12, 14)), (p3(0, 1.62, 0), bold("j"), (14, 8)),
                         (p3(0, 0, 1.45), bold("k"), (-12, -2))):
        sc.vec(O, tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # dimension a on each axis, beside the axis
    sc.label(p3(0.5, 0, 0), "a", "TEXT", "middle", 15, dx=-8, dy=-8)
    sc.label(p3(0, 0.5, 0), "a", "TEXT", "middle", 15, dy=22)
    sc.label(p3(0, 0, 0.5), "a", "TEXT", "end", 15, dx=-8, dy=5)
    # velocities (orange), scale 0.55 per unit v0
    kv = 0.55
    vA, vB, vC = (0, 1, 0), (0, 1, 1), (1, 1, 1)
    sc.vec(A, add(A, p3v(vA), kv), None, ORANGE, 2.8, head=11)
    sc.label(add(A, p3v(vA), kv * 0.5), sub("v", "0", "A"), ORANGE, "middle", 17, weight="700", dx=-2, dy=24)
    sc.vec(B, add(B, p3v(vB), kv), sub("v", "0", "B"), ORANGE, 2.8, name_off=(26, 6), size=17, head=11)
    sc.vec(C, add(C, p3v(vC), kv), sub("v", "0", "C"), ORANGE, 2.8, name_off=(24, 4), size=17, head=11)
    # instantaneous axis through A parallel to j, and omega along it
    sc.line(add(A, (1, 0), -0.55), add(A, (1, 0), 1.75), "GREEN", 1.4, "7 5")
    sc.vec(add(A, (1, 0), 0.72), add(A, (1, 0), 1.4), None, "GREEN", 3.2, head=12)
    sc.label(add(A, (1, 0), 1.4), "ω", "GREEN", "middle", 18, weight="700", dx=2, dy=-12)
    sc.note(add(A, (1, 0), 1.75), "axis", "GREEN", "start", 14, dx=6, dy=4)
    for pt, nm, off in ((A, "A", (-14, 18)), (B, "B", (12, 20)), (C, "C", (-14, -6))):
        sc.mass(pt, None, r=5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=18)
    return sc


@figure("rb01-view-along-omega",
        "View along the angular velocity showing the perpendicular velocity parts of B and C turning counterclockwise "
        "about the axis through A.",
        r"View with $\mathbf j$ out of the paper. The perpendicular parts of the velocities of $B$ and $C$ are normal to "
        r"their radii from the axis and proportional to them: $v_0$ at distance $a$ and $v_0\sqrt2$ at distance $a\sqrt2$.")
def view_along_omega():
    sc = Scene(620, 480, (150, 340), 200)
    O = (0.0, 0.0)
    A, B, C = (0.0, 1.0), (0.0, 0.0), (1.0, 0.0)          # (k, i) components: right = k, up = i
    fixed_axis(sc, O, 0, 1.5, bold("k"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.5, bold("i"), off=(14, 4))
    triangle(sc, [A, B, C], "BLUE", 0.12)
    sc.dashed(A, B)
    sc.dashed(A, C)
    # perpendicular velocity parts (orange)
    kv = 0.55
    sc.vec(B, (kv, 0.0), sub("v", "0"), ORANGE, 2.8, name_off=(-4, -14), size=17, head=11)
    sc.vec(C, (1 + kv, kv), None, ORANGE, 2.8, head=11)
    sc.label((1 + kv, kv), sub("v", "0") + "√2", ORANGE, "start", 17, weight="700", dx=8, dy=0)
    right_angle(sc, B, 90, 0, 0.07)
    right_angle(sc, C, 135, 45, 0.07)
    # distances
    sc.label((0.0, 0.5), "a", "TEXT", "end", 16, dx=-8, dy=5)
    sc.label((0.5, 0.5), "a√2", "TEXT", "start", 16, dx=10, dy=-8)
    # sense of rotation about A and its rate
    sc.arc(A, 0.34, -90, -45, "GREEN", 1.8, head=True)
    sc.label(A, "ω = v" + S("", "0") + " / a", "GREEN", "start", 17, dx=34, dy=16)
    axis_out(sc, A, None, "HEAD")
    sc.label(A, "axis through A (j)", "HEAD", "start", 15, italic=False, dx=14, dy=-6)
    axis_out(sc, B, None, "HEAD")
    sc.label(B, "O, B (j)", "HEAD", "end", 15, italic=False, dx=-14, dy=22)
    sc.mass(C, None, r=5, col="BLUE")
    sc.label(C, "C", "HEAD", "middle", 17, dx=4, dy=22)
    sc.label(A, "A", "HEAD", "middle", 17, dx=-16, dy=5)
    return sc
