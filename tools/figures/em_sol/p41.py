"""Problem 41: satellite spinning about z with a solar panel turned by theta about the body x axis (two rotations)."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold


def _components(sc, tip, horiz, vert, h_off=(0, 20), v_off=(-12, 5)):
    """Dashed projections of `tip` on the horizontal and vertical axes through the origin, with their labels."""
    sc.dashed(tip, (tip[0], 0.0))
    sc.dashed(tip, (0.0, tip[1]))
    sc.label((tip[0] / 2, 0.0), horiz, "TEXT", "middle", 15, dx=h_off[0], dy=h_off[1])
    sc.label((0.0, tip[1] / 2), vert, "TEXT", "end", 15, dx=v_off[0], dy=v_off[1])


@figure("p41-spin-view",
        "View from +z with k0 = k1 out of the paper: inertial axes i0 to the right and j0 up in grey, body axes i1 and j1 "
        "rotated counter-clockwise by omega t in blue, with the dashed components of i1 and of j1",
        r"First rotation, seen from $+z$ with $\mathbf k_0 = \mathbf k_1$ out of the paper ($\odot$): $\mathbf i_1, \mathbf j_1$ "
        r"are $\mathbf i_0, \mathbf j_0$ turned counter-clockwise by $\omega t$. $\mathbf i_1$ has components $\cos\omega t$ "
        r"along $\mathbf i_0$ and $\sin\omega t$ along $\mathbf j_0$; the tip of $\mathbf j_1$ moves to the side of "
        r"$-\mathbf i_0$, hence its component $-\sin\omega t$")
def spin_view():
    a = 32.0
    sc = Scene(500, 430, (230, 300), 190)
    O = (0.0, 0.0)
    fixed_axis(sc, (-0.95, 0.0), 0, 2.1, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.4), 90, 1.55, S(bold("j"), "0"), off=(14, 4))
    axis_out(sc, O, S(bold("k"), "0") + " = " + S(bold("k"), "1"), off=(-58, -12))
    i1 = unit(sc, O, a, 1.0, S(bold("i"), "1"), off=(12, -6))
    j1 = unit(sc, O, a + 90, 1.0, S(bold("j"), "1"), off=(-10, -8))
    sc.angle(O, 0.36, 0, a, "ωt", name_r=0.50)
    sc.angle(O, 0.24, 90, 90 + a, "ωt", name_r=0.36)
    triangle(sc, [O, (i1[0], 0.0), i1])
    right_angle(sc, (i1[0], 0.0), 180, 90, 0.05)
    sc.dashed(i1, (i1[0], 0.0))
    sc.label((i1[0], i1[1] / 2), "sin ωt", "TEXT", "start", 15, dx=8, dy=4)
    sc.label((i1[0] / 2, 0.0), "cos ωt", "TEXT", "middle", 15, dy=20)
    sc.dashed(j1, (j1[0], 0.0))
    sc.dashed(j1, (0.0, j1[1]))
    sc.label((j1[0] / 2, 0.0), "−sin ωt", "TEXT", "middle", 15, dy=20)
    sc.label((0.0, j1[1]), "cos ωt", "TEXT", "start", 15, dx=10, dy=-4)
    return sc


@figure("p41-hinge-view",
        "View along the hinge axis with i1 = i2 out of the paper: body axes j1 to the right and k1 up in grey, panel axes "
        "j2 and k2 rotated counter-clockwise by theta in blue, the corner B at distance W from the hinge along j2 and the "
        "shaded right triangle with legs W cos theta and W sin theta",
        r"Second rotation, seen along the hinge with $\mathbf i_1 = \mathbf i_2$ out of the paper ($\odot$), so $\mathbf j_1$ "
        r"points right and $\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ up. The panel turns $\theta$ counter-clockwise: "
        r"$\overrightarrow{CB} = W\,\mathbf j_2$ is the hypotenuse of the shaded triangle, with legs $W\cos\theta$ along "
        r"$\mathbf j_1$ and $W\sin\theta$ along $\mathbf k_1$")
def hinge_view():
    th = 38.0
    sc = Scene(520, 420, (190, 300), 175)
    C = (0.0, 0.0)
    W = 1.35
    B = (W * math.cos(math.radians(th)), W * math.sin(math.radians(th)))
    fixed_axis(sc, (-0.6, 0.0), 0, 2.25, S(bold("j"), "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.45), 90, 1.75, S(bold("k"), "1"), off=(14, 4))
    axis_out(sc, C, S(bold("i"), "1") + " = " + S(bold("i"), "2"), off=(-42, 26))
    triangle(sc, [C, (B[0], 0.0), B])
    right_angle(sc, (B[0], 0.0), 180, 90, 0.06)
    sc.rod(C, B, 6.0, "HEAD")
    sc.dashed(B, (B[0], 0.0))
    sc.label((B[0] / 2, 0.0), "W cos θ", "TEXT", "middle", 15, dy=20)
    sc.label((B[0], B[1] / 2), "W sin θ", "TEXT", "start", 15, dx=10, dy=4)
    sc.label((B[0] * 0.55, B[1] * 0.55), "W", "TEXT", "middle", 17, dx=-10, dy=-12)
    unit(sc, C, th, 0.55, S(bold("j"), "2"), off=(4, 20))
    unit(sc, C, th + 90, 0.55, S(bold("k"), "2"), off=(-14, -4))
    sc.angle(C, 0.32, 0, th, "θ", name_r=0.44)
    sc.dotp(B, 4.5)
    sc.label(B, "B", "HEAD", "start", 17, dx=8, dy=-8)
    sc.label(C, "C", "HEAD", "end", 17, dx=-14, dy=-8)
    sc.note((0.15, -0.42), "panel (plane of " + S(bold("i"), "2") + ", " + S(bold("j"), "2") + ") seen edge-on", "TEXT", "start", 13)
    return sc


@figure("p41-body-plane",
        "View from +z of the body plane: A at the origin, the hinge point C at distance H along i1, the projection B' of "
        "the corner B at height W cos theta along j1, and the vector r_perp from A to B' in orange",
        r"Body plane seen from $+z$ ($\mathbf k_1$ out of the paper): $C$ is at $H$ along $\mathbf i_1$ and the corner $B$ "
        r"projects onto the point $B'$ at $W\cos\theta$ along $\mathbf j_1$ ($B$ itself is $W\sin\theta$ above the paper). "
        r"$\mathbf r_\perp = H\,\mathbf i_1 + W\cos\theta\,\mathbf j_1$ is the distance vector from the spin axis, the one that "
        r"enters the centripetal term")
def body_plane():
    sc = Scene(560, 330, (70, 250), 150)
    A = (0.0, 0.0)
    H, Wc = 2.4, 0.8
    C = (H, 0.0)
    Bp = (H, Wc)
    fixed_axis(sc, (-0.25, 0.0), 0, 3.05, S(bold("i"), "1"), off=(14, 5))
    fixed_axis(sc, (0.0, -0.25), 90, 1.4, S(bold("j"), "1"), off=(14, 4))
    axis_out(sc, A, S(bold("k"), "1"), off=(-24, 26))
    sc.label(A, "A", "HEAD", "start", 17, dx=12, dy=22)
    sc.dashed(C, Bp)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "start", 17, dx=8, dy=22)
    sc.dotp(Bp, 4.5)
    sc.label(Bp, "B′", "HEAD", "start", 17, dx=10, dy=-6)
    sc.dim((0.0, -0.32), (H, -0.32), "H", off=(0, -8))
    sc.label((H, Wc / 2), "W cos θ", "TEXT", "start", 15, dx=10, dy=4)
    sc.vec(A, Bp, None, "ACC", 2.4, head=11)
    sc.label((H * 0.5, Wc * 0.5), S(bold("r"), "⊥"), "ACC", "middle", 17, weight="700", dx=-14, dy=-26)
    sc.note((0.9, 1.25), "B is W sin θ above the paper", "TEXT", "start", 13)
    return sc
