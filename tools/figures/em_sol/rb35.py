"""Problem RB-35: three tracked points of a spaceship and the parallel and perpendicular parts of a velocity."""
import math

from figures.em_solutions import figure, right_angle, triangle
from figures.em_sol.rb01 import add, arrow_px, d, p3, p3v, sub, vscale
from figures.mech import S, Scene, bold


@figure("rb35-three-points",
        "The three tracked points of the spaceship with their velocities and the angular velocity.",
        r"The centre of mass $G$, the point $A$ of the solar array and the point $C$ of the rear side, with the measured "
        r"velocities and the angular velocity that reproduces them.")
def three_points():
    sc = Scene(680, 440, (210, 330), 30)
    G, A, C = (0.0, 0.0, 0.0), (-2.0, 4.0, 0.0), (-8.0, 0.0, 2.0)
    for tip, nm, off in ((p3(6.5, 0, 0), bold("i"), (-12, 14)), (p3(0, 7.5, 0), bold("j"), (14, 6)),
                         (p3(0, 0, 5.5), bold("k"), (-12, -2))):
        sc.vec((0.0, 0.0), tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    pG, pA, pC = p3v(G), p3v(A), p3v(C)
    sc.poly([pG, pA, pC], "HEAD", 1.4, "6 4", close=True)
    kv = 0.5
    vG, vA, vC = (8, 4, 0), (4, 2, 6), (10, -6, 8)
    sc.vec(pG, add(pG, p3v(vscale(vG, kv))), sub("v", "0", "G"), "ACC", 2.8, name_off=(28, 10), size=17, head=11)
    sc.vec(pA, add(pA, p3v(vscale(vA, kv))), sub("v", "0", "A"), "ACC", 2.8, name_off=(28, -4), size=17, head=11)
    sc.vec(pC, add(pC, p3v(vscale(vC, kv))), sub("v", "0", "C"), "ACC", 2.8, name_off=(-4, -14), size=17, head=11)
    sc.vec(pG, add(pG, p3v((2.6, 2.6, 2.6))), "ω", "GREEN", 3.4, name_off=(12, -8), size=19, head=12)
    for pt, nm, off in ((pG, "G", (-14, -10)), (pA, "A", (-14, 4)), (pC, "C", (16, 18))):
        sc.mass(pt, None, r=5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    return sc


@figure("rb35-parallel-perpendicular",
        "Right triangle formed by the velocity of G, its part along the angular velocity and its part perpendicular to "
        "it.",
        r"The velocity of any body point is the hypotenuse of a right triangle whose leg along $\boldsymbol\omega$ is the "
        r"same for all points; the speed is smallest where the other leg vanishes.")
def parallel_perpendicular():
    sc = Scene(620, 440, (130, 360), 70)
    a0 = 20.0
    hyp, adj, opp = 4.47, 3.465, 2.83          # half of 8.94, 6.93 and 5.66 (scale of the drawing)
    alpha = math.degrees(math.acos(adj / hyp))
    G = (0.0, 0.0)
    F = add(G, d(a0), adj)
    V = add(F, d(a0 + 90), opp)
    triangle(sc, [G, F, V], "BLUE", 0.12)
    sc.line(add(F, d(a0), 0.0), add(F, d(a0), 0.9), "EDGE", 1.2, "5 4")
    # unit direction of omega (green), drawn just below the leg it is parallel to
    off = d(a0 - 90)
    g0 = add(G, off, 0.28)
    sc.vec(g0, add(g0, d(a0), 1.3), None, "GREEN", 3.0, head=11)
    sc.label(add(g0, d(a0), 1.3), S("e", "ω"), "GREEN", "start", 18, weight="700", dx=8, dy=14)
    # velocity (hypotenuse), parallel part, perpendicular part
    sc.vec(G, V, None, "ACC", 3.4, head=12)
    sc.vec(G, F, None, "BLUE", 2.6, head=11)
    sc.line(F, V, "BLUE", 2.2, "6 4")
    arrow_px(sc, F, V, "BLUE", 10)
    right_angle(sc, F, a0 + 180, a0 + 90, 0.14)
    sc.arc(G, 0.9, a0, a0 + alpha, "GREEN", 1.6)
    sc.label(add(G, d(a0 + alpha / 2), 1.2), "α", "GREEN", "middle", 16, dy=5)
    sc.label(add(G, d(a0), adj / 2), "v" + S("", "0∥") + " = 4√3 m/s", "BLUE", "middle", 16, weight="700", dx=60, dy=76)
    sc.label(add(G, d(a0 + alpha), hyp / 2), "|" + S(bold("v"), "0", "G") + "| = √80 m/s", "ACC", "end", 16,
             weight="700", dx=-14, dy=-6)
    sc.label(add(F, d(a0 + 90), opp / 2), S(bold("v"), "0⊥", "G"), "BLUE", "start", 17, weight="700", dx=12, dy=4)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=-8)
    return sc
