"""Problem RB-05: ten bodies (bar, cylinder, box, sphere, hemisphere, cone, disk, half plate, wire, sheet) and the
mass element used by the integral that gives their inertia tensor."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.em_sol.rb01 import DEPTH, add, arrow_px, d, p3, p3v, sub
from figures.mech import S, Scene, bold

ORANGE = "ACC"


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _hull(pts):
    pts = sorted(set((round(x, 6), round(y, 6)) for x, y in pts))
    if len(pts) < 3:
        return pts

    def cr(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo = []
    for p in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cr(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def _ring(P, c, u, v, r, t0=0.0, t1=360.0, n=72):
    out = []
    for i in range(n + 1):
        t = math.radians(t0 + (t1 - t0) * i / n)
        out.append(P(*[c[m] + r * (math.cos(t) * u[m] + math.sin(t) * v[m]) for m in range(3)]))
    return out


def _axes(sc, P, tips, names, offs):
    for tip, nm, off in zip(tips, names, offs):
        q = P(*tip)
        sc.vec((0.0, 0.0) if P is p3 else P(0, 0, 0), q, None, "EDGE", 1.4, head=8)
        sc.label(q, bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])


def _vlab(sc, p, s, col="HEAD", anchor="middle", dx=0, dy=0, size=15):
    sc.label(p, s, col, anchor, size, dx=dx, dy=dy)


def _box_hull(sc, P, c, dirs, halves, col="ACC", opacity=0.9):
    """Small parallelepiped centred at c with edges along dirs (half lengths halves): hull fill and the 12 edges."""
    verts = {}
    for sa in (-1, 1):
        for sb in (-1, 1):
            for sc_ in (-1, 1):
                q = tuple(c[m] + sa * halves[0] * dirs[0][m] + sb * halves[1] * dirs[1][m] + sc_ * halves[2] * dirs[2][m]
                          for m in range(3))
                verts[(sa, sb, sc_)] = P(*q)
    sc.poly(_hull(list(verts.values())), col, 0.0, fill=col, close=True, opacity=opacity)
    for k, v in verts.items():
        for m in range(3):
            if k[m] == -1:
                k2 = tuple(1 if i == m else k[i] for i in range(3))
                sc.line(v, verts[k2], "HEAD", 1.0)


# ------------------------------------------------------------------------------------------------------------ a: bar
def _pa(x, y, z):
    # x right, z up, y = z cross x points into the paper: it recedes to the upper right
    return (x - y * DEPTH[0], -y * DEPTH[1] + z)


@figure("rb05-a-bar",
        "Slender bar along the x axis centred at G with a line element dx at abscissa x.",
        r"The slender bar in its central frame; the mass element is $\lambda\,dx$ and every point has zero $y$ and $z$.")
def a_bar():
    sc = Scene(680, 380, (340, 230), 95)
    P = _pa
    L = 4.0
    sc.vec(P(0, 0, 0), P(2.75, 0, 0), None, "EDGE", 1.4, head=8)
    sc.label(P(2.75, 0, 0), bold("x"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    sc.vec(P(0, 0, 0), P(0, 1.4, 0), None, "EDGE", 1.4, head=8)
    sc.label(P(0, 1.4, 0), bold("y"), "TEXT", "middle", 16, weight="700", dx=12, dy=-6)
    sc.vec(P(0, 0, 0), P(0, 0, 1.3), None, "EDGE", 1.4, head=8)
    sc.label(P(0, 0, 1.3), bold("z"), "TEXT", "middle", 16, weight="700", dx=-12, dy=0)
    sc.line(P(-L / 2, 0, 0), P(L / 2, 0, 0), "BLUE", 8.0)
    # element dm = lambda dx at x = 0.9
    x0, dx = 0.9, 0.28
    sc.line(P(x0, 0, 0), P(x0 + dx, 0, 0), ORANGE, 12.0)
    sc.label(P(x0 + dx / 2, 0, 0), "dm = λ dx", ORANGE, "middle", 16, dy=-20)
    # dimensions L/2 above the bar
    zz = 0.7
    for xa, xb in ((-L / 2, 0.0), (0.0, L / 2)):
        sc.dim(P(xa, 0, zz), P(xb, 0, zz), "L/2", off=(0, -8))
    for xe in (-L / 2, L / 2):
        sc.dashed(P(xe, 0, 0.1), P(xe, 0, zz + 0.05))
    # leader x
    zl = -0.5
    sc.dashed(P(0, 0, -0.08), P(0, 0, zl - 0.05))
    sc.dashed(P(x0, 0, -0.08), P(x0, 0, zl - 0.05))
    sc.dim(P(0, 0, zl), P(x0, 0, zl), "x", off=(0, 20))
    sc.mass(P(0, 0, 0), None, r=5, col="BLUE")
    sc.label(P(0, 0, 0), "G", "HEAD", "end", 17, dx=-10, dy=-10)
    sc.note(P(-L / 2, 0, 0), "y = z = 0", "TEXT", "end", 13, dx=-14, dy=5)
    return sc


# ------------------------------------------------------------------------------------------------------- b: cylinder
def _pb(x, y, z):
    return (x + z * DEPTH[0], y + z * DEPTH[1])


@figure("rb05-b-cylinder",
        "Cylinder with its axis along z, centred at G, and the cylindrical volume element r dr dθ dz.",
        r"Cylindrical coordinates about the axis $z$: the volume element has sides $dr$, $r\,d\theta$ and $dz$, so its "
        r"jacobian is $r$.")
def b_cylinder():
    sc = Scene(720, 580, (400, 300), 105)
    P = _pb
    R, L, r, th = 1.0, 3.0, 0.65, 40.0
    ex, ey = (1, 0, 0), (0, 1, 0)
    near = _ring(P, (0, 0, L / 2), ex, ey, R)
    far = _ring(P, (0, 0, -L / 2), ex, ey, R)
    sc.poly(_hull(near + far), "BLUE", 0.0, fill="BLUE", close=True, opacity=0.13)
    sc.poly(far, "BLUE", 1.2, "5 4", close=True)
    sc.poly(near, "BLUE", 2.2, close=True)
    sc.line(P(-R, 0, L / 2), P(-R, 0, -L / 2), "BLUE", 2.2)
    sc.line(P(R, 0, L / 2), P(R, 0, -L / 2), "BLUE", 2.2)
    sc.line(P(0, R, L / 2), P(0, R, -L / 2), "BLUE", 1.0, "5 4")
    # axes through G
    sc.vec(P(0, 0, 0), P(1.5, 0, 0), None, "EDGE", 1.4, head=8)
    sc.label(P(1.5, 0, 0), bold("x"), "TEXT", "middle", 16, weight="700", dx=14, dy=5)
    sc.vec(P(0, 0, 0), P(0, 1.45, 0), None, "EDGE", 1.4, head=8)
    sc.label(P(0, 1.45, 0), bold("y"), "TEXT", "middle", 16, weight="700", dx=-12, dy=0)
    sc.vec(P(0, 0, 0), P(0, 0, 2.4), None, "EDGE", 1.4, head=8)
    sc.label(P(0, 0, 2.4), bold("z"), "TEXT", "middle", 16, weight="700", dx=-12, dy=14)
    sc.mass(P(0, 0, 0), None, r=4.5, col="BLUE")
    sc.label(P(0, 0, 0), "G", "HEAD", "end", 17, dx=-16, dy=-2)
    # dimensions L/2 along the axis, R on the near face
    for za, zb in ((-L / 2, 0.0), (0.0, L / 2)):
        sc.dim(P(1.35, 0, za), P(1.35, 0, zb), "L/2", off=(24, 4))
    for ze in (-L / 2, 0.0, L / 2):
        sc.dashed(P(R, 0, ze), P(1.4, 0, ze))
    c1 = P(0, 0, L / 2)
    rim = (c1[0] + R * math.cos(math.radians(-70)), c1[1] + R * math.sin(math.radians(-70)))
    sc.dim(c1, rim, "", off=(0, 0))
    sc.label(((c1[0] + rim[0]) / 2, (c1[1] + rim[1]) / 2), "R", "TEXT", "start", 15, dx=8, dy=8)
    # volume element at height z0
    z0, dz, dr, dth = 0.1, 0.45, 0.22, 24.0
    zf = z0 + dz

    def corner(rr, tt, zz):
        return P(rr * math.cos(math.radians(tt)), rr * math.sin(math.radians(tt)), zz)
    sc.poly(_ring(P, (0, 0, z0), ex, ey, R), "EDGE", 1.0, "3 4", close=True)
    back = [corner(r, th, z0), corner(r + dr, th, z0), corner(r + dr, th + dth, z0), corner(r, th + dth, z0)]
    front = [corner(r, th, zf), corner(r + dr, th, zf), corner(r + dr, th + dth, zf), corner(r, th + dth, zf)]
    sc.poly(back, ORANGE, 1.0, fill=ORANGE, close=True, opacity=0.5)
    for a, b in zip(back, front):
        sc.line(a, b, "HEAD", 1.0)
    sc.poly(front, ORANGE, 1.4, fill=ORANGE, close=True, opacity=0.95)
    # dashed radius, theta arc, reference direction x at the height of the element
    sc.dashed(P(0, 0, zf), corner(r, th + dth / 2, zf))
    sc.dashed(P(0, 0, zf), P(0.9, 0, zf))
    arc = _ring(P, (0, 0, zf), ex, ey, 0.38, 0, th)
    sc.poly(arc, "GREEN", 1.7)
    arrow_px(sc, arc[-3], arc[-1], "GREEN", 9)
    sc.label(corner(0.55, th / 2, zf), "θ", "GREEN", "middle", 16, dx=8, dy=14)
    sc.label(corner(r * 0.5, th + dth / 2, zf), "r", "TEXT", "start", 15, dx=16, dy=-14)
    sc.label(corner(r + dr, th + dth, zf), "dr", ORANGE, "start", 15, weight="700", dx=10, dy=-40)
    sc.label(corner(r + dr / 2, th + dth, zf), "r dθ", ORANGE, "end", 15, weight="700", dx=-36, dy=-36)
    sc.label(corner(r + dr, th, z0), "dz", ORANGE, "start", 15, weight="700", dx=22, dy=-8)
    return sc


# ------------------------------------------------------------------------------------------------------------ c: box
@figure("rb05-c-box",
        "Rectangular parallelepiped centred at G with edges a, b, c along x, y, z and a volume element dx dy dz.",
        r"The parallelepiped in its central frame ($a$ along $x$, $b$ along $y$, $c$ along $z$, read from the figure of "
        r"the statement) with the Cartesian volume element.")
def c_box():
    sc = Scene(740, 600, (330, 330), 110)
    a, b, c = 3.0, 2.0, 1.2
    P = p3

    def V(sx, sy, sz):
        return P(sx * a / 2, sy * b / 2, sz * c / 2)
    front = [V(1, -1, -1), V(1, 1, -1), V(1, 1, 1), V(1, -1, 1)]
    top = [V(1, -1, 1), V(1, 1, 1), V(-1, 1, 1), V(-1, -1, 1)]
    right = [V(1, 1, -1), V(-1, 1, -1), V(-1, 1, 1), V(1, 1, 1)]
    for f, o in ((front, 0.12), (top, 0.08), (right, 0.16)):
        sc.poly(f, "BLUE", 0.0, fill="BLUE", close=True, opacity=o)
    hid = V(-1, -1, -1)
    for q in (V(1, -1, -1), V(-1, 1, -1), V(-1, -1, 1)):
        sc.line(hid, q, "BLUE", 1.2, "5 4")
    for f in (front, top, right):
        sc.poly(f, "BLUE", 2.0, close=True)
    # axes
    for tip, nm, off in ((P(3.0, 0, 0), "x", (-12, 14)), (P(0, 2.15, 0), "y", (14, 8)), (P(0, 0, 1.55), "z", (-12, 0))):
        sc.vec((0.0, 0.0), tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    sc.mass((0.0, 0.0), None, r=4.5, col="BLUE")
    sc.label((0.0, 0.0), "G", "HEAD", "start", 17, dx=8, dy=-10)
    # dimension lines a/2, b/2, c/2
    ox, oy = 0.28, -0.28
    for xa, xb in ((-a / 2, 0), (0, a / 2)):
        pa_, pb_ = P(xa, b / 2, -c / 2), P(xb, b / 2, -c / 2)
        sc.dim(add(pa_, (ox, oy)), add(pb_, (ox, oy)), "a/2", off=(22, 14))
    for xe in (-a / 2, 0, a / 2):
        sc.dashed(P(xe, b / 2, -c / 2), add(P(xe, b / 2, -c / 2), (ox, oy)))
    for ya, yb in ((-b / 2, 0), (0, b / 2)):
        sc.dim(add(P(a / 2, ya, -c / 2), (0, -0.3)), add(P(a / 2, yb, -c / 2), (0, -0.3)), "b/2", off=(0, 18))
    for ye in (-b / 2, 0, b / 2):
        sc.dashed(P(a / 2, ye, -c / 2), add(P(a / 2, ye, -c / 2), (0, -0.3)))
    for za, zb in ((-c / 2, 0), (0, c / 2)):
        sc.dim(add(P(a / 2, -b / 2, za), (-0.3, 0)), add(P(a / 2, -b / 2, zb), (-0.3, 0)), "c/2", off=(-22, 5))
    for ze in (-c / 2, 0, c / 2):
        sc.dashed(P(a / 2, -b / 2, ze), add(P(a / 2, -b / 2, ze), (-0.3, 0)))
    # volume element dx dy dz at (x, y, z) with dashed projections on the coordinate planes
    x, y, z = 0.55, -0.35, 0.15
    c0 = P(x, y, z)
    for q in (P(x, y, 0), P(x, 0, z), P(0, y, z)):
        sc.dashed(c0, q)
        sc.dotp(q, 2.5, "EDGE")
    _box_hull(sc, P, (x, y, z), [(1, 0, 0), (0, 1, 0), (0, 0, 1)], (0.1, 0.1, 0.1))
    sc.label(c0, "dx dy dz", ORANGE, "end", 15, weight="700", dx=-16, dy=-14)
    return sc


# ---------------------------------------------------------------------------------------------------------- d: sphere
@figure("rb05-d-sphere",
        "Sphere with the spherical coordinates of the notes: radius r, longitude θ and latitude φ, and the right "
        "triangle that gives r cos φ and r sin φ.",
        r"Spherical coordinates of the notes, with the latitude $\varphi$ measured from the plane $Gxy$: the triangle with "
        r"hypotenuse $r$ gives the legs $r\cos\varphi$ and $r\sin\varphi$, and the volume element is "
        r"$r^2\cos\varphi\,dr\,d\theta\,d\varphi$.")
def d_sphere():
    sc = Scene(820, 700, (400, 380), 160)
    P = p3
    R, r, th, ph = 1.5, 1.3, 70.0, 30.0
    ct, st = math.cos(math.radians(th)), math.sin(math.radians(th))
    cp, sp = math.cos(math.radians(ph)), math.sin(math.radians(ph))
    sc.circle((0.0, 0.0), R, "BLUE", 2.2, fill="BLUE", opacity=0.08)
    sc.poly(_ring(P, (0, 0, 0), (1, 0, 0), (0, 1, 0), R), "BLUE", 1.2, "6 4")
    for tip, nm, off in ((P(3.1, 0, 0), "x", (-12, 14)), (P(0, 2.1, 0), "y", (14, 8)), (P(0, 0, 2.0), "z", (-12, 0))):
        sc.vec((0.0, 0.0), tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    G = (0.0, 0.0)
    Pt = P(r * cp * ct, r * cp * st, r * sp)
    F = P(r * cp * ct, r * cp * st, 0)
    triangle(sc, [G, F, Pt], "ACC", 0.22)
    sc.dashed(G, F)
    sc.dashed(F, Pt)
    sc.line(G, Pt, "HEAD", 2.4)
    # longitude arc in Gxy, latitude arc in the vertical plane
    arc = _ring(P, (0, 0, 0), (1, 0, 0), (0, 1, 0), 0.62, 0, th)
    sc.poly(arc, "GREEN", 1.7)
    arrow_px(sc, arc[-3], arc[-1], "GREEN", 9)
    sc.label(P(0.8 * math.cos(math.radians(th / 2)), 0.8 * math.sin(math.radians(th / 2)), 0), "θ", "GREEN", "middle", 16,
             dx=-34, dy=26)
    arc2 = _ring(P, (0, 0, 0), (ct, st, 0), (0, 0, 1), 0.55, 0, ph)
    sc.poly(arc2, "GREEN", 1.7)
    arrow_px(sc, arc2[-3], arc2[-1], "GREEN", 9)
    sc.label(P(0.78 * ct * math.cos(math.radians(ph / 2)), 0.78 * st * math.cos(math.radians(ph / 2)),
               0.78 * math.sin(math.radians(ph / 2))), "φ", "GREEN", "middle", 16, dx=4, dy=-4)
    sc.label(add(G, Pt, 0.5), "r", "HEAD", "end", 16, dx=-8, dy=-8)
    sc.label(add(G, F, 0.5), "r cos φ", "TEXT", "middle", 16, dx=30, dy=34)
    sc.label(F, "r sin φ", "TEXT", "start", 16, dx=12, dy=10)
    # volume element at P
    er = (cp * ct, cp * st, sp)
    et = (-st, ct, 0.0)
    ef = (-sp * ct, -sp * st, cp)
    c0 = (r * er[0], r * er[1], r * er[2])
    _box_hull(sc, P, c0, [er, et, ef], (0.09, 0.11, 0.11))
    sc.label(Pt, "dr", ORANGE, "start", 15, weight="700", dx=-6, dy=-36)
    sc.label(Pt, "r cos φ dθ", ORANGE, "start", 16, weight="700", dx=26, dy=-56)
    sc.label(Pt, "r dφ", ORANGE, "end", 15, weight="700", dx=-22, dy=-18)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "start", 17, dx=10, dy=18)
    sc.dotp(F, 3.0)
    sc.dim(G, (R * math.cos(math.radians(-60)), R * math.sin(math.radians(-60))), "", off=(0, 0))
    sc.label((R * 0.5 * math.cos(math.radians(-60)), R * 0.5 * math.sin(math.radians(-60))), "R", "TEXT", "start", 15,
             dx=8, dy=10)
    return sc


# ------------------------------------------------------------------------------------------------------- e: hemisphere
@figure("rb05-e-hemisphere",
        "Meridian section of the hemisphere with z pointing into the dome, the centre of mass at 3R/8 below the flat "
        "face and the latitude triangle.",
        r"Meridian section ($\mathbf j$ into the paper). The body is the latitude range from 0 to $\pi/2$ on the side of "
        r"positive $z$; $G$ lies on $Oz$ at $3R/8$, and the axes $Gx$ and $Ox$ are parallel at that distance.")
def e_hemisphere():
    sc = Scene(680, 460, (340, 110), 100)
    R, r, ph = 2.0, 1.4, 40.0
    O = (0.0, 0.0)
    pts = [(R * math.cos(t * math.pi / 60), -R * math.sin(t * math.pi / 60)) for t in range(0, 61)]
    sc.poly(pts + [(R, 0.0)], "BLUE", 0.0, fill="BLUE", close=True, opacity=0.12)
    sc.poly(pts, "BLUE", 2.4)
    sc.line((-R, 0.0), (R, 0.0), "HEAD", 3.2)
    fixed_axis(sc, O, 0, 2.55, _ax("x"), off=(14, 6))
    fixed_axis(sc, O, 270, 2.5, _ax("z"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _ax("y"), "HEAD", "end", 16, weight="700", dx=-14, dy=-8)
    sc.label(O, "O", "HEAD", "start", 17, dx=14, dy=-12)
    G = (0.0, -3 * R / 8)
    sc.line((-1.6, G[1]), (1.6, G[1]), "EDGE", 1.2, "6 4")
    sc.label((1.6, G[1]), "Gx", "TEXT", "start", 15, dx=6, dy=5)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "HEAD", "start", 17, dx=10, dy=18)
    sc.dim((-0.55, 0.0), (-0.55, G[1]), "", off=(0, 0))
    sc.label((-0.55, G[1] / 2), "3R/8", "TEXT", "end", 15, dx=-8, dy=5)
    # latitude triangle
    t = math.radians(ph)
    P_ = (r * math.cos(t), -r * math.sin(t))
    F = (P_[0], 0.0)
    triangle(sc, [O, F, P_], "ACC", 0.22)
    sc.dashed(F, P_)
    right_angle(sc, F, 180, 270, 0.12)
    sc.line(O, P_, "HEAD", 2.2)
    sc.arc(O, 0.6, 0, -ph, "GREEN", 1.7, head=True)
    sc.label((0.85 * math.cos(math.radians(-ph / 2)), 0.85 * math.sin(math.radians(-ph / 2))), "φ", "GREEN", "middle",
             16, dy=5)
    sc.label(add(O, P_, 0.5), "r", "HEAD", "end", 16, dx=-6, dy=18)
    sc.label((F[0] / 2, 0.0), "r cos φ", "TEXT", "middle", 14, dy=-8)
    sc.label((F[0], P_[1] / 2), "r sin φ (= z)", "TEXT", "start", 14, dx=8, dy=5)
    sc.mass(P_, None, r=4.5, col=ORANGE)
    sc.dim((-R, 0.7), (0.0, 0.7), "R", off=(0, -8))
    sc.dashed((-R, 0.0), (-R, 0.75))
    sc.dashed((0.0, 0.0), (0.0, 0.75))
    return sc


# ------------------------------------------------------------------------------------------------------------- f: cone
@figure("rb05-f-cone",
        "Meridian section of the cone with the apex at V, the centre of mass at 3L/4 from it and the similar triangles "
        "that give the radius of a section.",
        r"Meridian section of the cone ($\mathbf k$ out of the paper). The similar right triangles with legs $s$, $R_s$ and "
        r"$L$, $R$ give the radius of the section at the distance $s$; Steiner moves the transverse axis from $V$ to $G$ "
        r"over $3L/4$.")
def f_cone():
    sc = Scene(760, 430, (610, 170), 90)
    R, L, s = 1.2, 4.0, 2.5
    V = (0.0, 0.0)
    base = [(-L, R), (-L, -R)]
    triangle(sc, [V] + base, "BLUE", 0.12)
    sc.poly([V] + base, "BLUE", 2.4, close=True)
    Rs = R * s / L
    triangle(sc, [V, (-s, 0.0), (-s, Rs)], "ACC", 0.28)
    sc.dashed((-s, 0.0), (-s, Rs))
    right_angle(sc, (-s, 0.0), 0, 90, 0.12)
    sc.vec(V, (-L - 0.85, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((-L - 0.85, 0.0), _ax("x"), "TEXT", "middle", 16, weight="700", dx=-2, dy=-10)
    axis_in(sc, V, None, "HEAD")
    sc.label(V, _ax("z"), "HEAD", "start", 16, weight="700", dx=14, dy=-12)
    G = (-3 * L / 4, 0.0)
    fixed_axis(sc, V, 90, 1.75, _ax("y"), off=(14, 4))
    sc.line((G[0], -1.5), (G[0], 1.6), "EDGE", 1.2, "6 4")
    sc.label((G[0], 1.6), "Gy", "TEXT", "middle", 15, dy=-6)
    sc.label(V, "V", "HEAD", "start", 17, dx=14, dy=26)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "HEAD", "start", 17, dx=8, dy=-14)
    sc.dim((0.0, -1.75), (G[0], -1.75), "3L/4", off=(0, 18))
    sc.dashed((G[0], -0.1), (G[0], -1.8))
    sc.dashed((0.0, -0.1), (0.0, -1.8))
    sc.dim((0.0, -2.3), (-L, -2.3), "L", off=(0, 18))
    sc.dashed((-L, -R - 0.05), (-L, -2.35))
    sc.dim((-L - 0.35, 0.0), (-L - 0.35, R), "R", off=(-14, 5))
    sc.label((-s, Rs), S("R", "s"), "TEXT", "start", 18, dx=8, dy=-12)
    sc.label((-s / 2, 0.0), "s", "TEXT", "middle", 15, dy=22)
    return sc


# ------------------------------------------------------------------------------------------------------------- g: disk
@figure("rb05-g-disk",
        "Thin disk in the plane Gxy with the polar area element r dr dθ.",
        r"The thin disk modelled as a plate in the plane $Gxy$; the area element in polar coordinates is "
        r"$r\,dr\,d\theta$.")
def g_disk():
    sc = Scene(720, 540, (340, 260), 105)
    P = p3
    R, h, r, th = 2.0, 0.12, 1.0, 50.0
    ex, ey = (1, 0, 0), (0, 1, 0)
    top = _ring(P, (0, 0, 0), ex, ey, R)
    bot = _ring(P, (0, 0, -h), ex, ey, R)
    sc.poly(_hull(top + bot), "BLUE", 0.0, fill="BLUE", close=True, opacity=0.13)
    sc.poly(bot, "BLUE", 1.2, close=True)
    sc.poly(top, "BLUE", 2.2, close=True)
    for tip, nm, off in ((P(3.0, 0, 0), "x", (-12, 14)), (P(0, 2.5, 0), "y", (14, 8)), (P(0, 0, 1.4), "z", (-12, 0))):
        sc.vec((0.0, 0.0), tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    sc.mass((0.0, 0.0), None, r=4.5, col="BLUE")
    sc.label((0.0, 0.0), "G", "HEAD", "start", 17, dx=-20, dy=18)
    # area element
    dr, dth = 0.24, 14.0
    pts = _ring(P, (0, 0, 0), ex, ey, r, th, th + dth, 8) + list(reversed(_ring(P, (0, 0, 0), ex, ey, r + dr, th, th + dth, 8)))
    sc.poly(pts, ORANGE, 1.4, fill=ORANGE, close=True, opacity=0.95)
    mid = P((r + dr / 2) * math.cos(math.radians(th + dth / 2)), (r + dr / 2) * math.sin(math.radians(th + dth / 2)), 0)
    sc.dashed((0.0, 0.0), mid)
    sc.label(add((0.0, 0.0), mid, 0.5), "r", "TEXT", "end", 15, dx=-8, dy=-10)
    sc.dashed((0.0, 0.0), P(1.9, 0, 0))
    arc = _ring(P, (0, 0, 0), ex, ey, 0.75, 0, th)
    sc.poly(arc, "GREEN", 1.7)
    arrow_px(sc, arc[-3], arc[-1], "GREEN", 9)
    sc.label(P(0.98 * math.cos(math.radians(th / 2)), 0.98 * math.sin(math.radians(th / 2)), 0), "θ", "GREEN", "middle",
             16, dx=2, dy=18)
    sc.label(P((r + dr) * math.cos(math.radians(th)), (r + dr) * math.sin(math.radians(th)), 0), "dr", ORANGE, "end", 15,
             weight="700", dx=-10, dy=22)
    sc.label(P((r + dr) * math.cos(math.radians(th + dth)), (r + dr) * math.sin(math.radians(th + dth)), 0), "r dθ", ORANGE,
             "start", 15, weight="700", dx=14, dy=-4)
    # radius R and thickness h
    rim = P(R * math.cos(math.radians(250)), R * math.sin(math.radians(250)), 0)
    sc.dim((0.0, 0.0), rim, "", off=(0, 0))
    sc.label(add((0.0, 0.0), rim, 0.5), "R", "TEXT", "end", 15, dx=-6, dy=-8)
    q = P(R * math.cos(math.radians(-35)), R * math.sin(math.radians(-35)), 0)
    q2 = (q[0] + 0.12, q[1])
    sc.dashed(q, (q[0] + 0.18, q[1]))
    sc.dashed((q[0], q[1] - h), (q[0] + 0.18, q[1] - h))
    sc.vec((q[0] + 0.15, q[1] + 0.2), (q[0] + 0.15, q[1] + 0.01), None, "TEXT", 1.2, head=7)
    sc.vec((q[0] + 0.15, q[1] - h - 0.2), (q[0] + 0.15, q[1] - h - 0.01), None, "TEXT", 1.2, head=7)
    sc.label((q[0] + 0.15, q[1] - h / 2), "h", "TEXT", "start", 15, dx=12, dy=-2)
    sc.note((q[0] + 0.15, q[1] - h / 2), "h ≪ R", "TEXT", "start", 14, dx=12, dy=28)
    return sc


# ------------------------------------------------------------------------------------------------------ h: half plate
@figure("rb05-h-half-plate",
        "Semicircular plate with its diameter along y, the centre of mass on the x axis at 4R/(3π) and a polar area "
        "element.",
        r"The semicircular plate ($\mathbf k$ out of the paper), with $\theta$ from $-\pi/2$ to $\pi/2$; the triangle with "
        r"hypotenuse $r$ gives the abscissa $r\cos\theta$ and the ordinate $r\sin\theta$.")
def h_half_plate():
    sc = Scene(640, 470, (170, 240), 95)
    R, r, th = 2.0, 1.4, 35.0
    O = (0.0, 0.0)
    arc = [(R * math.cos(math.radians(t)), R * math.sin(math.radians(t))) for t in range(-90, 91, 3)]
    sc.poly(arc, "BLUE", 0.0, fill="BLUE", close=True, opacity=0.12)
    sc.poly(arc, "BLUE", 2.4)
    sc.line((0.0, -R), (0.0, R), "HEAD", 3.2)
    fixed_axis(sc, O, 0, 2.5, _ax("x"), off=(14, 6))
    fixed_axis(sc, O, 90, 2.4, _ax("y"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _ax("z"), "HEAD", "end", 16, weight="700", dx=-14, dy=-10)
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=22)
    xg = 4 * R / (3 * math.pi)
    sc.line((xg, -2.15), (xg, 2.15), "EDGE", 1.2, "6 4")
    sc.label((xg, -2.15), "Gy", "TEXT", "start", 15, dx=7, dy=14)
    sc.mass((xg, 0.0), None, r=5, col="BLUE")
    sc.label((xg, 0.0), "G", "HEAD", "start", 17, dx=10, dy=-10)
    sc.dim((0.0, -0.55), (xg, -0.55), "", off=(0, 0))
    sc.label((xg, -0.55), "4R/(3π)", "TEXT", "end", 15, dx=-5, dy=18)
    t = math.radians(th)
    Pt = (r * math.cos(t), r * math.sin(t))
    F = (Pt[0], 0.0)
    triangle(sc, [O, F, Pt], "ACC", 0.24)
    sc.dashed(F, Pt)
    right_angle(sc, F, 180, 90, 0.1)
    sc.line(O, Pt, "HEAD", 1.6, "5 4")
    sc.arc(O, 0.55, 0, th, "GREEN", 1.7, head=True)
    sc.label((0.78 * math.cos(math.radians(th / 2)), 0.78 * math.sin(math.radians(th / 2))), "θ", "GREEN", "middle", 16,
             dy=5)
    # polar element
    dr, dth = 0.2, 12.0
    pts = [((r - dr / 2) * math.cos(math.radians(th - dth / 2 + k * dth / 6)),
            (r - dr / 2) * math.sin(math.radians(th - dth / 2 + k * dth / 6))) for k in range(7)]
    pts += [((r + dr / 2) * math.cos(math.radians(th + dth / 2 - k * dth / 6)),
             (r + dr / 2) * math.sin(math.radians(th + dth / 2 - k * dth / 6))) for k in range(7)]
    sc.poly(pts, ORANGE, 1.4, fill=ORANGE, close=True, opacity=0.95)
    sc.label(add(O, Pt, 0.5), "r", "HEAD", "end", 16, dx=-6, dy=-10)
    sc.label((F[0] / 2, 0.0), "r cos θ", "TEXT", "middle", 14, dx=-4, dy=22)
    sc.label((F[0], Pt[1] / 2), "r sin θ", "TEXT", "start", 14, dx=8, dy=5)
    sc.label(Pt, "dr", ORANGE, "start", 15, weight="700", dx=12, dy=-6)
    sc.label(Pt, "r dθ", ORANGE, "start", 15, weight="700", dx=14, dy=-24)
    sc.dim(O, (R * math.cos(math.radians(-28)), R * math.sin(math.radians(-28))), "", off=(0, 0))
    sc.label((R * 0.75 * math.cos(math.radians(-28)), R * 0.75 * math.sin(math.radians(-28))), "R", "TEXT", "start", 15,
             dx=4, dy=18)
    return sc


# -------------------------------------------------------------------------------------------------------------- i: wire
@figure("rb05-i-wire",
        "Semicircular wire with its ends on the x axis, the centre of mass on the y axis at 2R/π and a line element R dθ.",
        r"The semicircular wire ($\mathbf k$ out of the paper), parametrised by $\theta$ from 0 to $\pi$; the line element "
        r"is $R\,d\theta$, and $G$ is on the symmetry axis $Oy$ at $2R/\pi$.")
def i_wire():
    sc = Scene(640, 440, (320, 320), 95)
    R, th = 2.0, 55.0
    O = (0.0, 0.0)
    arc = [(R * math.cos(math.radians(t)), R * math.sin(math.radians(t))) for t in range(0, 181, 3)]
    sc.poly(arc, "BLUE", 3.6)
    sc.line((-R, 0.0), (R, 0.0), "EDGE", 1.2, "6 4")
    fixed_axis(sc, O, 0, 2.55, _ax("x"), off=(14, 6))
    fixed_axis(sc, O, 90, 2.6, _ax("y"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _ax("z"), "HEAD", "end", 16, weight="700", dx=-14, dy=-10)
    sc.label(O, "O", "HEAD", "start", 17, dx=12, dy=22)
    yg = 2 * R / math.pi
    sc.line((-1.7, yg), (1.7, yg), "EDGE", 1.2, "6 4")
    sc.label((1.7, yg), "Gx", "TEXT", "start", 15, dx=7, dy=5)
    sc.mass((0.0, yg), None, r=5, col="BLUE")
    sc.label((0.0, yg), "G", "HEAD", "start", 17, dx=10, dy=-10)
    sc.dim((-0.45, 0.0), (-0.45, yg), "2R/π", off=(-8, 5))
    t = math.radians(th)
    Pt = (R * math.cos(t), R * math.sin(t))
    F = (Pt[0], 0.0)
    triangle(sc, [O, F, Pt], "ACC", 0.24)
    sc.dashed(F, Pt)
    right_angle(sc, F, 180, 90, 0.1)
    sc.line(O, Pt, "HEAD", 1.6)
    sc.arc(O, 0.6, 0, th, "GREEN", 1.7, head=True)
    sc.label((0.85 * math.cos(math.radians(th / 2)), 0.85 * math.sin(math.radians(th / 2))), "θ", "GREEN", "middle", 16,
             dy=5)
    sc.poly([(R * math.cos(math.radians(a)), R * math.sin(math.radians(a))) for a in [th + k * 0.75 for k in range(9)]],
            ORANGE, 7.0)
    sc.label(Pt, "ds = R dθ", ORANGE, "start", 16, weight="700", dx=16, dy=-14)
    sc.label(add(O, Pt, 0.5), "R", "HEAD", "end", 16, dx=-6, dy=-10)
    sc.label((F[0] / 2, 0.0), "R cos θ", "TEXT", "middle", 14, dy=24)
    sc.label((F[0], Pt[1] / 2), "R sin θ", "TEXT", "start", 14, dx=8, dy=5)
    return sc


# ------------------------------------------------------------------------------------------------------------- j: sheet
@figure("rb05-j-sheet",
        "Rectangular sheet with its frame at the vertex A, the centre of mass G at the middle and the vector from A to G "
        "used in Steiner's theorem.",
        r"The flat sheet in the frame $S_A$ at the vertex (no figure in the statement; axes chosen along the edges). "
        r"Steiner's theorem moves the tensor from $A$ to $G$ along $\mathbf r_A^G$.")
def j_sheet():
    sc = Scene(660, 460, (150, 330), 90)
    L, w = 4.0, 2.5
    A, G = (0.0, 0.0), (L / 2, w / 2)
    sc.poly([(0, 0), (L, 0), (L, w), (0, w)], "BLUE", 0.0, fill="BLUE", close=True, opacity=0.12)
    sc.poly([(0, 0), (L, 0), (L, w), (0, w)], "BLUE", 2.4, close=True)
    fixed_axis(sc, A, 0, L + 0.6, _ax("x"), off=(14, 6))
    fixed_axis(sc, A, 90, w + 0.5, _ax("y"), off=(14, 4))
    axis_out(sc, A, None, "HEAD")
    sc.label(A, _ax("z"), "HEAD", "end", 16, weight="700", dx=-14, dy=-10)
    sc.label(A, "A", "HEAD", "end", 17, dx=-14, dy=22)
    sc.line((-0.2, G[1]), (L + 0.3, G[1]), "EDGE", 1.2, "6 4")
    sc.label((L + 0.3, G[1]), "Gx", "TEXT", "start", 15, dx=6, dy=5)
    sc.line((G[0], -0.2), (G[0], w + 0.3), "EDGE", 1.2, "6 4")
    sc.label((G[0], w + 0.3), "Gy", "TEXT", "middle", 15, dy=-6)
    sc.dashed((L / 2, 0.0), G)
    sc.label((L / 2, w / 4), "w/2", "TEXT", "start", 14, dx=8, dy=5)
    sc.vec(A, G, None, "GREEN", 3.0, head=12)
    sc.label(add(A, G, 0.5), S(bold("r"), "A", "G"), "GREEN", "end", 17, weight="700", dx=-8, dy=-10)
    sc.label((L / 4, w / 2), "L/2", "TEXT", "middle", 14, dy=-8)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "HEAD", "start", 17, dx=10, dy=-10)
    sc.dotp(A, 3.5)
    # element dx dy at (x, y)
    x, y = 3.1, 1.9
    sc.poly([(x - 0.08, y - 0.08), (x + 0.08, y - 0.08), (x + 0.08, y + 0.08), (x - 0.08, y + 0.08)], ORANGE, 1.2, fill=ORANGE,
            close=True, opacity=0.95)
    sc.dashed((x, y), (0.0, y))
    sc.dashed((x, y), (x, 0.0))
    sc.label((1.0, y), "x", "TEXT", "middle", 15, dy=-8)
    sc.label((x, y / 2), "y", "TEXT", "start", 15, dx=6, dy=5)
    sc.label((x, y), "dx dy", ORANGE, "start", 15, weight="700", dx=12, dy=-8)
    # dimensions L below and w to the left
    sc.dim((0.0, -0.5), (L, -0.5), "L", off=(0, 18))
    sc.dashed((0.0, -0.05), (0.0, -0.55))
    sc.dashed((L, -0.05), (L, -0.55))
    sc.dim((-0.55, 0.0), (-0.55, w), "w", off=(-14, 5))
    sc.dashed((-0.05, w), (-0.6, w))
    return sc
