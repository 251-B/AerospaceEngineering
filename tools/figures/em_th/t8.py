"""Topic 8 theory figures: constraints, rolling motion, multibody systems and torque-free motion.

All points are written in screen coordinates (x right, y down) of the brief; class G converts them to the world of a
mech.Scene (origin at the top-left corner, 1 px per unit), so visual angles are the usual counter-clockwise ones.
"""
import math

from figures.em_theory import figure
from figures.mech import S, Scene, bold


def vn(b, sub=None, sup=None):
    """Bold vector name with optional sub/superscript."""
    return bold(b) + (S("", sub, sup) if (sub is not None or sup is not None) else "")


class G:
    def __init__(self, w, h):
        self.sc = Scene(w, h, (0, 0), 1)
        self.ox = self.oy = 0.0
        self.f = 1.0

    def at(self, ox=0.0, oy=0.0, f=1.0):
        self.ox, self.oy, self.f = ox, oy, f

    def pt(self, p):
        return (self.ox + self.f * p[0], -(self.oy + self.f * p[1]))

    @staticmethod
    def ray(c, deg, L):
        return (c[0] + L * math.cos(math.radians(deg)), c[1] - L * math.sin(math.radians(deg)))

    def line(self, a, b, col="HEAD", w=1.6, dash=None):
        self.sc.line(self.pt(a), self.pt(b), col, w, dash)

    def poly(self, pts, col="HEAD", w=1.6, dash=None, fill="none", close=False, op=None):
        self.sc.poly([self.pt(p) for p in pts], col, w, dash, fill, close, op)

    def vec(self, a, b, name=None, col="BLUE", w=2.6, off=(8, -8), size=17, head=11):
        self.sc.vec(self.pt(a), self.pt(b), name, col, w, name_off=off, size=size, head=head)

    def lab(self, p, s, col="HEAD", anchor="middle", size=17, dx=0, dy=0, italic=True, weight="400"):
        self.sc.label(self.pt(p), s, col, anchor, size, italic, weight, dx, dy)

    def note(self, p, s, anchor="middle", size=15, dx=0, dy=0, col="HEAD"):
        self.lab(p, s, col, anchor, size, dx, dy, italic=False)

    def dot(self, p, r=3.5, col="HEAD"):
        self.sc.dotp(self.pt(p), r, col)

    def circ(self, c, r, col="HEAD", w=1.8, fill="none", op=None, dash=None):
        self.sc.circle(self.pt(c), r * self.f, col, w, dash, fill, op)

    def arc(self, c, r, a0, a1, col="GREEN", w=1.8, head=False, dash=None):
        self.sc.arc(self.pt(c), r * self.f, a0, a1, col, w, dash, head)

    def ang(self, c, r, a0, a1, name, name_r, col="GREEN", size=16):
        self.sc.arc(self.pt(c), r * self.f, a0, a1, col, 1.6)
        m = math.radians((a0 + a1) / 2)
        self.lab((c[0] + name_r * math.cos(m), c[1] - name_r * math.sin(m)), name, col, "middle", size, dy=5)

    def out(self, p, name=None, col="HEAD", off=(0, 26)):
        from figures.em_theory import axis_out
        axis_out(self.sc, self.pt(p), name, col, off=off)

    def inn(self, p, name=None, col="HEAD", off=(0, 26)):
        from figures.em_theory import axis_in
        axis_in(self.sc, self.pt(p), name, col, off=off)

    def tri(self, pts, col="ACC", op=0.16):
        self.sc.poly([self.pt(p) for p in pts], col, 0.0, fill=col, close=True, opacity=op)

    def rtang(self, c, d1, d2, size=10):
        a, b = (math.cos(math.radians(d1)), -math.sin(math.radians(d1))), (math.cos(math.radians(d2)), -math.sin(math.radians(d2)))
        p1 = (c[0] + size * a[0], c[1] + size * a[1])
        p2 = (c[0] + size * (a[0] + b[0]), c[1] + size * (a[1] + b[1]))
        p3 = (c[0] + size * b[0], c[1] + size * b[1])
        self.poly([p1, p2, p3], "EDGE", 1.2)

    def blob(self, hull, col="HEAD", fill="HEAD", op=0.14, w=2.0):
        n = len(hull)
        out = []
        for i in range(n):
            p0, p1, p2, p3 = hull[(i - 1) % n], hull[i], hull[(i + 1) % n], hull[(i + 2) % n]
            for k in range(10):
                t = k / 10
                out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                        + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)))
        self.poly(out, col, w, fill=fill, close=True, op=op)
        return out

    @staticmethod
    def ell(c, rx, ry, rot=0.0, a0=0.0, a1=360.0, n=96):
        ph = math.radians(rot)
        u, v = (math.cos(ph), -math.sin(ph)), (math.sin(ph), math.cos(ph))
        pts = []
        for i in range(n + 1):
            t = math.radians(a0 + (a1 - a0) * i / n)
            pts.append((c[0] + rx * math.cos(t) * u[0] + ry * math.sin(t) * v[0],
                        c[1] + rx * math.cos(t) * u[1] + ry * math.sin(t) * v[1]))
        return pts

    def floor(self, x0, x1, y, step=10, ln=9):
        self.line((x0, y), (x1, y), "HEAD", 2.4)
        x = x0 + ln
        while x <= x1:
            self.line((x, y), (x - ln * 0.8, y + ln), "EDGE", 1.0)
            x += step


def fixed(g, o, tip, name, off=(14, 5)):
    g.vec(o, tip, None, "EDGE", 1.4, head=8)
    g.lab(tip, name, "TEXT", "middle", 16, dx=off[0], dy=off[1])


# ----------------------------------------------------------------------------------------------- joints
@figure("t8-joints",
        "A ball-and-socket joint between two bodies and a pin connection with its local axes at C.",
        "Left, a ball-and-socket joint: $C$ is common to both bodies but orientations are free. Right, a pin connection: "
        "the pin axis $Cz$ is common and only rotation about it is allowed.")
def joints():
    g = G(880, 262)
    f = 0.8
    # left: ball and socket
    g.at(10, 24, f)
    g.lab((260, 18), "ball-and-socket joint", "HEAD", "middle", 18, italic=False)
    g.blob([(40, 110), (70, 62), (130, 52), (200, 68), (236, 95), (244, 130), (236, 165), (200, 195), (120, 205), (62, 185), (40, 150)])
    g.blob([(280, 95), (270, 130), (280, 165), (320, 195), (400, 205), (460, 185), (480, 140), (465, 80), (400, 52), (330, 60)])
    g.circ((260, 130), 30, "HEAD", 2.0, "BLUE", 0.2)
    g.poly(G.ell((260, 130), 36, 36, 0, 90, 270), "HEAD", 4.0)
    g.dot((260, 130), 4.5)
    g.lab((125, 135), "B" + S("", "1"), "HEAD", "middle", 22)
    g.lab((395, 135), "B" + S("", "2"), "HEAD", "middle", 22)
    g.lab((275, 127), "C", "HEAD", "start", 18, dx=-2)
    # right: pin
    g.at(450, 24, f)
    g.lab((260, 18), "pin connection", "HEAD", "middle", 18, italic=False)
    cap1 = [(40, 95), (260, 95)] + G.ell((260, 130), 35, 35, 0, 90, -90)[1:-1] + [(260, 165), (40, 165)]
    g.poly(cap1, "HEAD", 2.0, fill="HEAD", close=True, op=0.12)
    cap2 = [(480, 105), (260, 105)] + G.ell((260, 130), 25, 25, 0, 90, 270)[1:-1] + [(260, 155), (480, 155)]
    g.poly(cap2, "HEAD", 2.0, fill="BLUE", close=True, op=0.14)
    C = (260, 130)
    pa, pb = G.ray(C, 120, 42), G.ray(C, 120, -42)
    pr = G.ray((0, 0), 30, 9)
    g.poly([(pa[0] + pr[0], pa[1] + pr[1]), (pa[0] - pr[0], pa[1] - pr[1]), (pb[0] - pr[0], pb[1] - pr[1]), (pb[0] + pr[0], pb[1] + pr[1])],
           "HEAD", 1.8, fill="HEAD", close=True, op=0.35)
    g.line(G.ray(C, 120, 105), G.ray(C, 120, -75), "BLUE", 1.3, "6 4")
    g.vec(C, G.ray(C, 120, 62), None, "BLUE", 2.6)
    g.lab(G.ray(C, 120, 108), "z", "BLUE", "middle", 18, dx=-14, dy=0, weight="700")
    g.vec(C, G.ray(C, 35, 62), "y", "BLUE", 2.6, off=(10, -6))
    g.vec(C, G.ray(C, -30, 62), "x", "BLUE", 2.6, off=(10, 10))
    g.dot(C, 3.5)
    g.lab((110, 135), "B" + S("", "1"), "HEAD", "middle", 22)
    g.lab((410, 135), "B" + S("", "2"), "HEAD", "middle", 22)
    g.lab(C, "C", "HEAD", "end", 18, dx=-10, dy=24)
    return g.sc


# ----------------------------------------------------------------------------------------------- collars
@figure("t8-collars",
        "A collar sliding and turning on a cylindrical bar, and a collar that only slides on a prismatic bar.",
        "Left, the collar may slide along and turn about $z_1$. Right, on a prismatic bar it may only slide.")
def collars():
    g = G(700, 320)
    for k, (ox, cyl) in enumerate([(0, True), (350, False)]):
        g.at(ox, 10, 1.0)
        C = (130, 200)
        g.poly([(118, 20), (142, 20), (142, 290), (118, 290)], "HEAD", 2.0, fill="HEAD", close=True, op=0.12)
        if cyl:
            g.poly(G.ell((130, 20), 12, 4), "HEAD", 1.5)
        else:
            g.line((128, 20), (128, 290), "HEAD", 1.0)
            g.poly([(118, 20), (128, 14), (152, 14), (142, 20)], "HEAD", 1.5)
        g.poly([(100, 160), (160, 160), (160, 240), (100, 240)], "HEAD", 2.4, fill="BLUE", close=True, op=0.14)
        g.poly([(160, 192), (300, 192), (300, 208), (160, 208)], "HEAD", 2.2, fill="HEAD", close=True, op=0.14)
        g.line((130, 8), (130, 300), "EDGE", 1.3, "6 4")
        g.line(C, (335, 200), "EDGE", 1.3, "6 4")
        g.dot(C, 4)
        g.lab((130, 8), (S("z", "1") + " = " + S("z", "2")) if cyl else (S("z", "1") + " = " + S("z", "2")), "TEXT", "start", 16, dx=26, dy=4)
        g.vec((60, 150), (60, 250), None, "EDGE", 1.6, head=8)
        g.vec((60, 250), (60, 150), None, "EDGE", 1.6, head=8)
        g.lab((50, 200), "slides", "TEXT", "end", 14, dy=5, italic=False) if False else None
        g.lab((150, 70), "B" + S("", "1"), "HEAD", "start", 21, dx=10)
        g.lab((250, 186), "B" + S("", "2"), "HEAD", "middle", 21, dy=-6)
        g.lab(C, "C", "HEAD", "middle", 18, dx=-14, dy=32)
        if cyl:
            g.line(C, G.ray(C, -40, 105), "EDGE", 1.3, "6 4")
            g.lab(G.ray(C, -40, 105), S("x", "1"), "TEXT", "middle", 16, dx=14, dy=14)
            g.lab((335, 200), S("x", "2"), "TEXT", "middle", 16, dx=4, dy=22)
            g.arc(C, 70, -40, 0, "GREEN", 1.8)
            g.lab(G.ray(C, -20, 90), "φ", "GREEN", "middle", 17, dx=10, dy=6)
            g.lab((335, 200), "", "TEXT")
        else:
            g.lab((335, 200), S("x", "1") + " = " + S("x", "2"), "TEXT", "middle", 16, dx=-18, dy=24)
    return g.sc


# ----------------------------------------------------------------------------------------------- rolling contact
@figure("t8-rolling-contact",
        "Two bodies rolling on each other at a contact point with the contact frame and the arcs swept on each perimeter.",
        "Two smooth bodies in contact at $C$, with the contact basis (normal and tangent plane) and the arc lengths $s_1$ and "
        "$s_2$ travelled by the contact point.")
def rolling_contact():
    g = G(600, 400)
    C = (300, 200)
    n = (80 / math.hypot(80, 25), 25 / math.hypot(80, 25))          # common normal, screen
    t = (-n[1], n[0])                                             # tangent pointing down, screen
    def loc(u, v):
        return (C[0] + u * t[0] + v * n[0], C[1] + u * t[1] + v * n[1])
    def egg(sign):
        pts = []
        for i in range(0, 361, 5):
            th = math.radians(i)
            a = 105 if math.cos(th) < 0 else 125
            pts.append(loc(a * math.cos(th), sign * (100 + 100 * math.sin(th))))
        return pts
    b2, b1 = egg(1), egg(-1)
    g.poly(b1, "HEAD", 2.2, fill="HEAD", close=True, op=0.12)
    g.poly(b2, "HEAD", 2.2, fill="BLUE", close=True, op=0.12)
    g.line(loc(-60, 0), loc(60, 0), "EDGE", 1.2, "5 4")
    # arcs along the perimeters, going up (u < 0)
    def perim(sign, a1, a0=0.0):
        pts = []
        for i in range(21):
            al = math.radians(a0 + (a1 - a0) * i / 20)
            u = -125 * math.sin(al) if False else -105 * math.sin(al)
            pts.append(loc(u, sign * 100 * (1 - math.cos(al))))
        return pts
    for sign, al, name, lbl, off in ((-1, 62, "s" + S("", "1"), "s" + S("", "1") + "(0)", (-18, -6)), (1, 62, "s" + S("", "2"), "s" + S("", "2") + "(0)", (22, -6))):
        pts = perim(sign, al)
        g.poly(pts, "PINK", 3.6)
        e = pts[-1]
        q = pts[-2]
        d = (e[0] - q[0], e[1] - q[1])
        L = math.hypot(*d)
        nn = (-d[1] / L, d[0] / L)
        g.line((e[0] - 7 * nn[0], e[1] - 7 * nn[1]), (e[0] + 7 * nn[0], e[1] + 7 * nn[1]), "PINK", 2.4)
        g.lab(e, lbl, "PINK", "middle", 16, dx=off[0] * 1.6, dy=off[1] - 6)
        m = pts[10]
        g.lab(m, name, "PINK", "middle", 17, dx=off[0], dy=8 if sign < 0 else 8)
    tip_n = (380, 225)
    tip_t = (C[0] + 80 * t[0], C[1] + 80 * t[1])
    g.vec(C, tip_n, "z", "BLUE", 2.6, off=(12, 4))
    g.vec(C, tip_t, "y", "BLUE", 2.6, off=(-10, 14))
    g.out(C, "x", "BLUE", off=(-18, -14))
    g.lab((150, 215), "B" + S("", "1"), "HEAD", "middle", 22)
    g.lab((450, 215), "B" + S("", "2"), "HEAD", "middle", 22)
    g.lab(C, "C(B" + S("", "1") + ")", "HEAD", "end", 17, dx=-22, dy=48)
    g.lab(C, "C(B" + S("", "2") + ")", "HEAD", "start", 17, dx=34, dy=50)
    return g.sc


# ----------------------------------------------------------------------------------------------- disk rolling
def _disk_angle_data():
    th = 0.96
    R = 120
    return th, R


@figure("t8-disk-rolling",
        "A disk of radius R rolling without slip on a floor, with the angle turned and the equal arc on the floor.",
        "The disk turns clockwise by $\\theta$ while its centre advances $R\\theta$; the contact points $C(B)$ of the disk and "
        "$C(F)$ of the floor coincide.")
def disk_rolling():
    g = G(600, 372)
    g.floor(80, 560, 300)
    O = (150, 180)
    fixed(g, O, (210, 180), S("x", "0"))
    fixed(g, O, (150, 100), S("y", "0"), off=(14, 4))
    g.lab(O, "O", "TEXT", "end", 17, dx=-8, dy=20)
    G0 = (360, 180)
    g.circ(G0, 120, "BLUE", 2.2, "BLUE", 0.2)
    g.vec(G0, (500, 180), S("x", "G"), "BLUE", 2.4, off=(14, 6))
    g.vec(G0, (360, 60), S("y", "G"), "BLUE", 2.4, off=(26, 8))
    g.vec(G0, G.ray(G0, 30, 120), "R", "ACC", 2.4, off=(6, -10))
    g.line(G0, (360, 300), "EDGE", 1.2, "5 4")
    ma = math.radians(55)
    M = (360 - 120 * math.sin(ma), 180 + 120 * math.cos(ma))
    g.line(G0, M, "PINK", 1.8, "6 4")
    g.arc(G0, 52, -145, -90, "PINK", 2.0)
    g.lab(G.ray(G0, -117.5, 70), "θ", "PINK", "middle", 18, dy=5)
    g.arc(G0, 120, -145, -90, "PINK", 4.0)
    g.dot(M, 4.5, "PINK")
    g.line((245, 300), (360, 300), "PINK", 4.5)
    g.line((245, 290), (245, 310), "PINK", 2.2)
    g.lab((302, 336), "Rθ", "PINK", "middle", 18)
    g.dot(G0, 3.5)
    g.lab(G0, "G", "HEAD", "middle", 18, dx=-14, dy=-8)
    g.inn((505, 72))
    g.lab((505, 72), vn("ω", "B0"), "HEAD", "start", 18, dx=16, dy=5)
    g.dot((360, 300), 4.5)
    g.lab((360, 300), "C(B)", "HEAD", "start", 17, dx=12, dy=-14)
    g.lab((360, 300), "C(F)", "HEAD", "start", 17, dx=12, dy=36)
    return g.sc


@figure("t8-disk-velocity",
        "Velocities of a disk rolling without slip: zero at the contact, v at the centre, 2v at the top.",
        "Rolling without slip: the contact point is at rest, the centre moves at $R$ times the rate of $\\theta$ and the top "
        "point twice as fast.")
def disk_velocity():
    g = G(600, 372)
    g.floor(60, 560, 300)
    G0 = (300, 180)
    g.circ(G0, 120, "BLUE", 2.2, "BLUE", 0.14)
    g.line((300, 300), G0, "EDGE", 1.4, "5 4")
    g.lab((300, 245), "CG", "TEXT", "end", 17, dx=-8)
    g.vec(G0, (400, 180), vn("v", "0", "G"), "ACC", 3.0, off=(8, 26))
    g.vec((300, 60), (500, 60), "2 " + vn("v", "0", "G"), "ACC", 3.0, off=(26, 6), size=19)
    g.note((310, 40), "velocity of the top point equal to 2 v0G", "start", 14, col="TEXT")
    g.arc(G0, 50, 150, 40, "GREEN", 2.0, head=True)
    g.inn(G0)
    g.lab(G0, "G", "HEAD", "middle", 18, dx=-22, dy=-14)
    g.lab(G0, vn("ω", "B0"), "GREEN", "start", 18, dx=16, dy=44)
    g.circ((300, 300), 7, "ACC", 2.2, fill="BLUE", op=0.0)
    g.lab((300, 300), "C(B)", "HEAD", "start", 17, dx=14, dy=-12)
    g.lab((300, 300), vn("v", "0", "C(B)") + " = 0", "ACC", "middle", 18, dy=40)
    return g.sc


@figure("t8-wobbling-disk",
        "A disk rolling and wobbling on a floor, leaving a curved trace.",
        "A disk rolling without slip in three dimensions: the contact point traces a curve on the floor, so two coordinates "
        "are needed to place it.")
def wobbling_disk():
    g = G(600, 420)
    g.poly([(80, 300), (420, 230), (560, 320), (220, 390)], "EDGE", 1.6, fill="EDGE", close=True, op=0.10)
    C = (300, 330)
    # centre chosen so that the lowest point of the tilted ellipse is C
    a, b, ph = 110, 60, 60
    h = math.hypot(a * math.sin(math.radians(ph)), b * math.cos(math.radians(ph)))
    dx = -(a * a - b * b) * math.sin(math.radians(ph)) * math.cos(math.radians(ph)) / h
    G0 = (C[0] - dx, C[1] - h)
    # trace first (under the disk)
    trace = []
    for i in range(41):
        s = i / 40
        trace.append((200 + 100 * s, 260 + 70 * s + 16 * math.sin(3 * s * math.pi) * (1 - s)))
    trace[-1] = C
    g.poly(trace, "ACC", 2.2, "6 4")
    g.poly(G.ell(G0, a, b, ph), "BLUE", 2.6, fill="BLUE", close=True, op=0.18)
    g.poly(G.ell(G0, a * 0.9, b * 0.9, ph), "BLUE", 1.0)
    g.vec(C, (300, 150), "k", "GREEN", 2.8, off=(14, -2), size=20)
    g.dot(C, 5)
    g.dot(G0, 4)
    g.lab(G0, "G", "HEAD", "start", 18, dx=10, dy=-6)
    g.lab(C, "C", "HEAD", "start", 18, dx=12, dy=22)
    return g.sc


@figure("t8-disk-height",
        "Right triangle giving the height of the centre of a tilted disk above the floor.",
        "The height of $G$ above the floor is the leg opposite the angle $\\theta$ at $C$, $R\\sin\\theta$; the angle between "
        "the disk and the floor equals the angle between its axis and the vertical.")
def disk_height():
    g = G(600, 300)
    g.at(0, -70)
    g.floor(60, 560, 320)
    th = 50
    C = (200, 320)
    cs, sn = math.cos(math.radians(th)), math.sin(math.radians(th))
    far = (200 + 240 * cs, 320 - 240 * sn)
    G0 = (200 + 120 * cs, 320 - 120 * sn)
    F = (G0[0], 320)
    g.tri([C, G0, F])
    g.line(G0, F, "EDGE", 1.3, "5 4")
    g.rtang(F, 180, 90, 12)
    g.line(C, far, "BLUE", 6.0)
    g.vec(G0, G.ray(G0, th + 90, 75), vn("k", "b"), "BLUE", 2.6, off=(-12, -8))
    g.vec(G0, G.ray(G0, 90, 75), vn("k", "0"), "EDGE", 2.6, off=(10, -10))
    g.ang(G0, 42, 90, th + 90, "θ", 62)
    g.arc(C, 46, 0, th, "GREEN", 1.8)
    g.lab(G.ray(C, th / 2, 64), "θ", "GREEN", "middle", 17, dy=5)
    g.dot(C, 4.5)
    g.dot(G0, 4.5)
    g.lab(C, "C", "HEAD", "end", 18, dx=-8, dy=24)
    g.lab(F, "F", "HEAD", "start", 18, dx=8, dy=30)
    g.lab(G0, "G", "HEAD", "start", 18, dx=18, dy=12)
    g.lab(((C[0] + G0[0]) / 2, (C[1] + G0[1]) / 2), "R", "HEAD", "end", 19, dx=-12, dy=-4)
    g.lab(((G0[0] + F[0]) / 2, 274), "R sin θ", "HEAD", "start", 17, dx=-86, dy=-4) if False else None
    g.lab((F[0], 274), "R sin θ", "HEAD", "start", 17, dx=10, dy=5)
    g.lab(((C[0] + F[0]) / 2, 320), "R cos θ", "HEAD", "middle", 17, dy=36)
    return g.sc


@figure("t8-disk-slip",
        "A disk skidding on a floor: the contact point slides backwards and friction pushes forwards.",
        "When the disk spins faster than it advances, the contact point slips backwards and friction, opposite to the slip, "
        "acts forwards.")
def disk_slip():
    g = G(600, 372)
    g.floor(60, 560, 300)
    G0 = (300, 180)
    g.circ(G0, 120, "BLUE", 2.2, "BLUE", 0.12)
    g.vec(G0, (360, 180), vn("v", "0", "G"), "ACC", 3.0, off=(6, 24))
    g.arc(G0, 52, 160, 30, "GREEN", 2.0, head=True)
    g.vec(G0, (300, 220), "m g", "GREEN", 2.8, off=(28, 6))
    g.vec((300, 300), (300, 232), "N", "PINK", 2.8, off=(14, 14))
    g.vec((300, 300), (362, 300), "R = μN", "PINK", 2.8, off=(44, 38))
    g.vec((300, 300), (218, 300), None, "ACC", 3.0)
    g.lab((255, 346), vn("v", "0", "C(B)") + " (slip)", "ACC", "middle", 17)
    g.inn(G0)
    g.lab(G0, "G", "HEAD", "middle", 18, dx=-20, dy=-12)
    g.lab(G0, vn("ω", "B0"), "GREEN", "middle", 18, dx=-10, dy=-60) if False else g.lab(G.ray(G0, 118, 78), vn("ω", "B0"), "GREEN", "middle", 18, dy=0)
    g.lab((300, 300), "C(B)", "HEAD", "start", 17, dx=-24, dy=-14)
    return g.sc


@figure("t8-table-legs",
        "Tables with three and four legs and the vertical reactions at their feet.",
        "With three legs the three equilibrium equations give the reactions; with four or more legs they do not.")
def table_legs():
    g = G(860, 340)
    top = [(110, 110), (330, 110), (270, 190), (50, 190)]          # back-left, back-right, front-right, front-left
    th = 12
    def table(ox, legs, labels, title):
        g.at(ox, 0, 1.0)
        g.lab((200, 28), title, "HEAD", "middle", 18, italic=False)
        for (x, y, back) in legs:
            yb = y + th
            foot = y + th + 110
            top_y = (202 if not back else 122 + 0)
            y0 = (190 - (x - 270) * 80 / 60 + th) if x > 270 else 202
            g.line((x, yb if not back else y0), (x, foot), "HEAD", 5.0)
        g.poly(top, "BLUE", 2.0, fill="BLUE", close=True, op=0.55)
        g.poly([(50, 190), (270, 190), (270, 190 + th), (50, 190 + th)], "BLUE", 1.6, fill="BLUE", close=True, op=0.75)
        g.poly([(270, 190), (330, 110), (330, 110 + th), (270, 190 + th)], "BLUE", 1.6, fill="BLUE", close=True, op=0.75)
        for (x, y, back), name in zip(legs, labels):
            foot = y + th + 110
            g.dot((x, foot), 4.5)
            g.vec((x + 16, foot), (x + 16, foot - 52), name, "GREEN", 2.8, off=(16, -4), size=17)
    table(10, [(70, 190, False), (220, 110, True), (255, 190, False)],
          [vn("F", None, "P1"), vn("F", None, "P2"), vn("F", None, "P3")], "determinate (3 legs)")
    table(440, [(70, 190, False), (110, 110, True), (310, 110, True), (255, 190, False)],
          [vn("F", None, "P1"), vn("F", None, "P2"), vn("F", None, "P3"), vn("F", None, "P4")], "hyperstatic (4 legs)")
    return g.sc


# ----------------------------------------------------------------------------------------------- two bodies
def _axes_body(g, c, name_sub, ang=(215, 315, 90), L=50):
    for a, nm in zip(ang, ("x", "y", "z")):
        off = {"x": (-12, 12), "y": (14, 10), "z": (0, -10)}[nm]
        g.vec(c, G.ray(c, a, L), S(nm, name_sub), "BLUE", 2.4, off=off, size=16)


@figure("t8-two-bodies",
        "Two rigid bodies joined by a ball-and-socket joint with external forces and an internal action-reaction pair.",
        "Two bodies joined at $C$ by a ball-and-socket joint, loaded by $F^{P1}$ and $F^{P2}$ and by an internal pair along "
        "$P_3P_4$.")
def two_bodies():
    g = G(640, 420)
    O = (140, 330)
    fixed(g, O, (60, 380), "x", off=(-12, 12))
    fixed(g, O, (380, 330), "y", off=(14, 5))
    fixed(g, O, (140, 140), "z", off=(0, -10))
    g.lab(O, "O", "TEXT", "start", 17, dx=8, dy=20)
    g.poly(G.ell((215, 250), 118, 72, 8), "HEAD", 2.0, fill="HEAD", close=True, op=0.12)
    g.poly(G.ell((460, 235), 128, 80, -6), "HEAD", 2.0, fill="HEAD", close=True, op=0.12)
    g.lab((215, 250), "", "HEAD")
    G1, G2 = (200, 250), (470, 220)
    g.dot(G1, 3.5)
    g.dot(G2, 3.5)
    g.lab(G1, "G" + S("", "1"), "HEAD", "start", 17, dx=-30, dy=-12) if False else g.lab(G1, "G" + S("", "1"), "HEAD", "start", 17, dx=8, dy=-6)
    g.lab(G2, "G" + S("", "2"), "HEAD", "start", 17, dx=8, dy=-6)
    _axes_body(g, G1, "1")
    _axes_body(g, G2, "2")
    g.lab((150, 300), "B" + S("", "1"), "HEAD", "middle", 22)
    g.lab((545, 260), "B" + S("", "2"), "HEAD", "middle", 22)
    C = (330, 240)
    g.dot(C, 5)
    g.lab(C, "C", "HEAD", "middle", 18, dx=-18, dy=8)
    g.vec((330, 150), (330, 232), None, "EDGE", 1.4, head=8)
    g.lab((330, 150), "ball-and-socket joint", "HEAD", "middle", 15, dy=-8, italic=False)
    P1, P2, P3, P4 = (170, 190), (450, 300), (250, 310), (415, 275)
    for p, nm, off in ((P1, "P" + S("", "1"), (-14, -8)), (P2, "P" + S("", "2"), (-14, -8)), (P3, "P" + S("", "3"), (-14, -8)),
                       (P4, "P" + S("", "4"), (-4, 22))):
        g.dot(p, 4)
        g.lab(p, nm, "HEAD", "middle", 16, dx=off[0], dy=off[1])
    g.vec(P1, G.ray(P1, 50, 62), vn("F", None, "P1"), "GREEN", 2.8, off=(20, -4))
    g.vec(P2, G.ray(P2, -35, 62), vn("F", None, "P2"), "GREEN", 2.8, off=(20, 10))
    g.line(P3, P4, "EDGE", 1.3, "5 4")
    d = (P4[0] - P3[0], P4[1] - P3[1])
    L = math.hypot(*d)
    u = (d[0] / L, d[1] / L)
    g.vec(P3, (P3[0] + 62 * u[0], P3[1] + 62 * u[1]), vn("f", "P4", "P3"), "ACC", 2.8, off=(-4, 22)) if False else \
        g.vec(P3, (P3[0] + 62 * u[0], P3[1] + 62 * u[1]), S(bold("f"), "P4", "P3"), "ACC", 2.8, off=(-6, 24))
    g.vec(P4, (P4[0] - 62 * u[0], P4[1] - 62 * u[1]), S(bold("f"), "P3", "P4"), "ACC", 2.8, off=(-4, 24))
    return g.sc


@figure("t8-exploded",
        "Exploded view of two bodies with equal and opposite reaction components at the joint.",
        "Each body is drawn apart and the joint replaced by the reaction $R$ on $B_1$ and minus $R$ on $B_2$.")
def exploded():
    g = G(680, 420)
    g.poly(G.ell((165, 235), 112, 78, 6), "HEAD", 2.0, fill="HEAD", close=True, op=0.12)
    g.poly(G.ell((515, 235), 115, 78, -6), "HEAD", 2.0, fill="HEAD", close=True, op=0.12)
    G1, G2 = (140, 235), (515, 245)
    for p, nm in ((G1, "G" + S("", "1")), (G2, "G" + S("", "2"))):
        g.dot(p, 3.5)
        g.lab(p, nm, "HEAD", "start", 17, dx=8, dy=-6)
    _axes_body(g, G1, "1", L=46)
    _axes_body(g, G2, "2", L=46)
    g.lab((85, 262), "B" + S("", "1"), "HEAD", "middle", 22)
    g.lab((585, 262), "B" + S("", "2"), "HEAD", "middle", 22)
    C1, C2 = (277, 240), (400, 240)
    g.dot(C1, 5)
    g.dot(C2, 5)
    g.lab(C1, "C(B" + S("", "1") + ")", "HEAD", "start", 16, dx=10, dy=34)
    g.lab(C2, "C(B" + S("", "2") + ")", "HEAD", "start", 16, dx=14, dy=34)
    g.vec(C1, G.ray(C1, 215, 44), S(bold("R"), "1"), "PINK", 2.8, off=(-14, 12))
    g.vec(C1, (C1[0] + 36, C1[1]), S(bold("R"), "2"), "PINK", 2.8, off=(0, -12))
    g.vec(C1, (C1[0], C1[1] - 50), S(bold("R"), "3"), "PINK", 2.8, off=(-14, -4))
    g.vec(C2, G.ray(C2, 35, 44), "−" + S(bold("R"), "1"), "PINK", 2.8, off=(26, -4))
    g.vec(C2, (C2[0] - 36, C2[1]), "−" + S(bold("R"), "2"), "PINK", 2.8, off=(-6, -12))
    g.vec(C2, (C2[0], C2[1] + 34), "−" + S(bold("R"), "3"), "PINK", 2.8, off=(-24, 6))
    P1, P2, P3, P4 = (100, 185), (590, 295), (215, 306), (470, 306)
    for p, nm, off in ((P1, "P" + S("", "1"), (-14, -8)), (P2, "P" + S("", "2"), (-14, -8)), (P3, "P" + S("", "3"), (-14, 18)),
                       (P4, "P" + S("", "4"), (12, 20))):
        g.dot(p, 4)
        g.lab(p, nm, "HEAD", "middle", 16, dx=off[0], dy=off[1])
    g.vec(P1, G.ray(P1, 50, 58), vn("F", None, "P1"), "GREEN", 2.8, off=(20, -4))
    g.vec(P2, G.ray(P2, -35, 58), vn("F", None, "P2"), "GREEN", 2.8, off=(20, 10))
    g.line(P3, P4, "EDGE", 1.3, "5 4")
    g.vec(P3, (P3[0] + 62, P3[1]), S(bold("f"), "P4", "P3"), "ACC", 2.8, off=(-4, 26))
    g.vec(P4, (P4[0] - 62, P4[1]), S(bold("f"), "P3", "P4"), "ACC", 2.8, off=(4, 26))
    return g.sc


# ----------------------------------------------------------------------------------------------- torque-free
@figure("t8-torque-free-frames",
        "Inertial and body-fixed bases at the centre of mass of a free asteroid-like body.",
        "The inertial frame $S_0$ and the body frame $S_b$ of principal axes, both centred at $G$.")
def torque_free_frames():
    g = G(600, 400)
    G0 = (300, 220)
    g.blob([(205, 215), (225, 165), (290, 150), (360, 170), (400, 215), (385, 270), (320, 292), (250, 280)], "HEAD", "HEAD", 0.16, 2.2)
    fixed(g, G0, (300, 90), vn("k", "0"), off=(2, -10))
    fixed(g, G0, (180, 290), vn("i", "0"), off=(-12, 8))
    fixed(g, G0, (430, 290), vn("j", "0"), off=(14, 12))
    g.vec(G0, (250, 85), vn("k", "b"), "BLUE", 2.8, off=(-6, -12))
    g.vec(G0, (440, 170), vn("j", "b"), "BLUE", 2.8, off=(16, -6))
    g.vec(G0, (310, 330), vn("i", "b"), "BLUE", 2.8, off=(16, 10))
    g.ang(G0, 100, 90, 110.3, "θ", 124)
    g.dot(G0, 4.5)
    g.lab(G0, "G", "HEAD", "start", 19, dx=12, dy=-8)
    return g.sc


def _rot(width_name, ang, grey, blue, axname, greek):
    g = G(460, 300)
    O = (200, 200)
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    fixed(g, O, (330, 200), grey[0], off=(16, 5))
    fixed(g, O, (200, 70), grey[1], off=(0, -10))
    a1 = (200 + 130 * c, 200 - 130 * s)
    b1 = (200 - 130 * s, 200 - 130 * c)
    ca, cb = (200 + 130 * c, 200), (200, 200 - 130 * c)
    g.tri([O, ca, a1])
    g.tri([O, cb, b1])
    g.line(a1, ca, "EDGE", 1.2, "5 4")
    g.line(b1, cb, "EDGE", 1.2, "5 4")
    g.rtang(ca, 180, 90, 9)
    g.rtang(cb, 270, 180, 9)
    g.vec(O, a1, blue[0], "BLUE", 2.8, off=(16, -4))
    g.vec(O, b1, blue[1], "BLUE", 2.8, off=(-12, -12))
    g.ang(O, 52, 0, ang, greek, 76)
    g.ang(O, 42, 90, 90 + ang, greek, 64)
    g.lab(((200 + ca[0]) / 2, 200), "cos " + greek, "TEXT", "middle", 15, dy=22)
    g.lab(a1, "sin " + greek, "TEXT", "start", 15, dx=-70, dy=40) if False else g.lab((ca[0], (200 + a1[1]) / 2), "sin " + greek, "TEXT", "start", 15, dx=8, dy=5)
    g.lab(((200 + b1[0]) / 2, b1[1]), "sin " + greek, "TEXT", "middle", 15, dy=-9)
    g.lab((200, 150), "cos " + greek, "TEXT", "start", 15, dx=8, dy=5)
    g.out(O, axname, "HEAD", off=(-50, 34))
    return g.sc


@figure("t8-rot-psi",
        "Precession by psi about k0 seen from above, with the triangles giving i1 and j1.",
        "Precession: the basis turns by $\\psi$ about $\\mathbf k_0$, which points out of the paper; the tip of $\\mathbf j_1$ "
        "moves towards minus $\\mathbf i_0$, hence the minus sign.")
def rot_psi():
    return _rot("psi", 30, (vn("i", "0"), vn("j", "0")), (vn("i", "1"), vn("j", "1")),
                vn("k", "0") + " = " + vn("k", "1"), "ψ")


@figure("t8-rot-theta",
        "Nutation by theta about i1, with the triangles giving j2 and k2.",
        "Nutation: rotation by $\\theta$ about $\\mathbf i_1$, out of the paper; $\\mathbf k_2$ tilts towards minus $\\mathbf j_1$.")
def rot_theta():
    return _rot("theta", 35, (vn("j", "1"), vn("k", "1")), (vn("j", "2"), vn("k", "2")),
                vn("i", "1") + " = " + vn("i", "2"), "θ")


@figure("t8-rot-phi",
        "Spin by phi about k2, with the triangles giving ib and jb.",
        "Spin: rotation by $\\varphi$ about the body axis $\\mathbf k_b$, out of the paper.")
def rot_phi():
    return _rot("phi", 40, (vn("i", "2"), vn("j", "2")), (vn("i", "b"), vn("j", "b")),
                vn("k", "2") + " = " + vn("k", "b"), "φ")


@figure("t8-axisymmetric-cones",
        "The angular velocity of an axisymmetric body as the sum of a precession about H and a spin about the symmetry axis.",
        "For an axisymmetric body the angular velocity lies in the plane of $\\mathbf k_0$ and $\\mathbf k_b$: precession "
        "$H/A$ about the fixed angular momentum plus spin $\\lambda$ about the symmetry axis.")
def cones():
    g = G(640, 400)
    G0 = (300, 320)
    th = 35
    kb_dir = 90 - th
    kb_tip = G.ray(G0, kb_dir, 200)
    p_k0 = (300, 170)
    p_kb = G.ray(G0, kb_dir, 70)
    om = (p_k0[0] + (p_kb[0] - G0[0]), p_k0[1] + (p_kb[1] - G0[1]))
    # cones (thin ellipses) and silhouettes
    r1 = om[0] - 300
    g.poly(G.ell((300, om[1]), r1, 12), "EDGE", 1.3, "5 4")
    g.line(G0, (300 - r1, om[1]), "EDGE", 1.3, "5 4")
    d = ((om[0] - G0[0]), (om[1] - G0[1]))
    Lm = math.hypot(*d)
    ua = (math.cos(math.radians(kb_dir)), -math.sin(math.radians(kb_dir)))
    dpar = d[0] * ua[0] + d[1] * ua[1]
    cb = (G0[0] + dpar * ua[0], G0[1] + dpar * ua[1])
    perp = (d[0] - dpar * ua[0], d[1] - dpar * ua[1])
    rb = math.hypot(*perp)
    pang = -math.degrees(math.atan2(perp[1], perp[0]))
    g.poly(G.ell(cb, rb, 26, pang), "EDGE", 1.3, "5 4")
    g.line(G0, (cb[0] - perp[0], cb[1] - perp[1]), "EDGE", 1.3, "5 4")
    g.vec(G0, (300, 80), vn("H", "G0") if False else None, "GREEN", 3.0)
    g.vec(G0, kb_tip, vn("k", "b"), "BLUE", 3.0, off=(14, -6))
    g.line(G0, p_k0, "ACC", 2.4, "7 5")
    g.line(G0, p_kb, "ACC", 2.4, "7 5")
    g.line(p_k0, om, "ACC", 1.4, "4 4")
    g.line(p_kb, om, "ACC", 1.4, "4 4")
    g.vec(G0, om, vn("ω", "b0"), "ACC", 3.4, off=(36, -14), size=19)
    g.ang(G0, 60, kb_dir, 90, "θ", 98)
    g.dot(G0, 4.5)
    g.lab(G0, "G", "HEAD", "start", 18, dx=10, dy=20)
    g.lab((300, 80), S(bold("H"), "G0") + " = H " + vn("k", "0"), "GREEN", "end", 18, dx=-10, dy=8)
    g.lab((300, 250), "(" + S(bold("H"), "G0") + "/A) " + vn("k", "0"), "ACC", "end", 17, dx=-30)
    g.lab(p_kb, "λ " + vn("k", "b"), "ACC", "start", 18, dx=14, dy=22)
    g.lab(p_kb, "", "ACC")
    g.lab((300 - r1, om[1]), "space cone", "TEXT", "end", 16, dx=-10, dy=6, italic=False)
    g.lab((cb[0] - perp[0], cb[1] - perp[1]), "body cone", "TEXT", "start", 16, dx=-10, dy=24, italic=False)
    g.lab((300, 52), vn("k", "0"), "GREEN", "middle", 18, dx=0, dy=-4) if False else None
    return g.sc


# ----------------------------------------------------------------------------------------------- Poinsot
@figure("t8-poinsot",
        "The inertia ellipsoid rolling without slip on the invariable plane, with polhode and herpolhode.",
        "Poinsot's construction: the body-fixed inertia ellipsoid rolls without slip on the invariable plane; the tip of the "
        "angular velocity traces the polhode on the ellipsoid and the herpolhode on the plane.")
def poinsot():
    g = G(660, 430)
    G0 = (300, 270)
    a, b, ph = 170, 110, 35
    h = math.hypot(a * math.sin(math.radians(ph)), b * math.cos(math.radians(ph)))
    dx = (a * a - b * b) * math.sin(math.radians(ph)) * math.cos(math.radians(ph)) / h
    P = (G0[0] + dx, G0[1] - h)
    # wireframe
    g.poly(G.ell(G0, a, b, ph), "HEAD", 2.2, fill="ACC", close=True, op=0.10)
    g.poly(G.ell(G0, a, 38, ph), "EDGE", 1.1)
    g.poly(G.ell(G0, 60, b, ph), "EDGE", 1.1)
    g.poly(G.ell(G0, 140, 85, ph + 90 * 0, 0, 360), "EDGE", 0.0)
    # small body (cylinder) at G
    g.poly(G.ell((G0[0] - 8, G0[1] + 6), 16, 6, 35), "HEAD", 1.6, fill="HEAD", close=True, op=0.3)
    g.poly(G.ell((G0[0] + 8, G0[1] - 6), 16, 6, 35), "HEAD", 1.6, fill="HEAD", close=True, op=0.3)
    g.line((G0[0] - 22, G0[1] + 3), (G0[0] - 6, G0[1] - 9), "HEAD", 1.6) if False else None
    # invariable plane (grid)
    u, v = (170, -22), (60, -34)
    cn = [(P[0] - u[0] - v[0], P[1] - u[1] - v[1]), (P[0] + u[0] - v[0], P[1] + u[1] - v[1]),
          (P[0] + u[0] + v[0], P[1] + u[1] + v[1]), (P[0] - u[0] + v[0], P[1] - u[1] + v[1])]
    g.poly(cn, "GREEN", 1.8, fill="GREEN", close=True, op=0.10)
    for i in range(1, 6):
        s = i / 6
        a0 = (cn[0][0] + (cn[1][0] - cn[0][0]) * s, cn[0][1] + (cn[1][1] - cn[0][1]) * s)
        a1 = (cn[3][0] + (cn[2][0] - cn[3][0]) * s, cn[3][1] + (cn[2][1] - cn[3][1]) * s)
        g.line(a0, a1, "GREEN", 0.8)
        b0 = (cn[0][0] + (cn[3][0] - cn[0][0]) * s, cn[0][1] + (cn[3][1] - cn[0][1]) * s)
        b1 = (cn[1][0] + (cn[2][0] - cn[1][0]) * s, cn[1][1] + (cn[2][1] - cn[1][1]) * s)
        g.line(b0, b1, "GREEN", 0.8)
    # herpolhode: closed curve on the plane through P, around the foot of G's vertical
    cx = P[0] - 62
    her = []
    for i in range(121):
        t = 2 * math.pi * i / 120
        r = 1 + 0.10 * math.sin(3 * t)
        her.append((cx + 62 * r * math.cos(t), P[1] + 15 * r * math.sin(t)))
    g.poly(her, "GREEN", 2.8)
    # polhode: closed curve on the ellipsoid through P
    g.poly(G.ell((P[0] - 2, P[1] + 28), 40, 28, 10), "PINK", 2.8)
    g.vec(P, (P[0], P[1] - 95), None, "GREEN", 3.0)
    g.vec(G0, P, None, "ACC", 3.4)
    g.lab(((G0[0] + P[0]) / 2, (G0[1] + P[1]) / 2), vn("ω", "b0"), "ACC", "end", 19, dx=-14, dy=6)
    g.dot(G0, 4.5)
    g.dot(P, 4.5)
    g.lab(G0, "G", "HEAD", "start", 19, dx=10, dy=24)
    g.lab((P[0], P[1] - 95), S(bold("H"), "G0") + " ∥ " + vn("k", "0"), "GREEN", "start", 18, dx=14, dy=4)
    g.lab(cn[1], "invariable plane", "TEXT", "start", 16, dx=-10, dy=-14, italic=False) if False else \
        g.lab(cn[1], "invariable plane", "TEXT", "start", 16, dx=-40, dy=34, italic=False)
    g.lab((G0[0] - a * 0.55, G0[1] + 84), "inertia ellipsoid", "TEXT", "end", 16, dx=-4, dy=30, italic=False)
    g.lab((P[0] + 46, P[1] + 34), "polhode", "PINK", "start", 16, italic=False)
    g.lab((cx - 62, P[1]), "herpolhode", "GREEN", "end", 16, dx=-6, dy=-18, italic=False)
    return g.sc


@figure("t8-polhodes",
        "Polhodes on the inertia ellipsoid: loops around the major and minor axes and separatrices crossing at the intermediate axis.",
        "Polhodes are closed loops around the major and minor axes; near the intermediate axis they look like hyperbolas, "
        "bounded by the separatrices.")
def polhodes():
    g = G(640, 450)
    G0 = (300, 240)
    A = (90.0, 130.0, 180.0)                      # semi-axes along ib, jb, kb
    dv = (0.62, 0.22, 0.75)                        # view direction (towards the viewer) in the frame (ib, jb, kb)
    nd = math.sqrt(sum(q * q for q in dv))
    dv = tuple(q / nd for q in dv)
    ey = [(0, 0, 1)[i] - dv[2] * dv[i] for i in range(3)]
    ny = math.sqrt(sum(q * q for q in ey))
    ey = [q / ny for q in ey]
    ex = [ey[1] * dv[2] - ey[2] * dv[1], ey[2] * dv[0] - ey[0] * dv[2], ey[0] * dv[1] - ey[1] * dv[0]]
    E = tuple((ex[i], -ey[i]) for i in range(3))      # screen image (x right, y down) of each unit axis

    def proj(s):
        x = sum(A[i] * s[i] * E[i][0] for i in range(3))
        y = sum(A[i] * s[i] * E[i][1] for i in range(3))
        return (G0[0] + x, G0[1] + y)

    def vis(s):
        return sum(dv[i] * s[i] / A[i] for i in range(3)) > 0

    u = [1 / a ** 2 for a in A]

    # silhouette of the ellipsoid: image of the unit sphere
    m = [[A[i] * E[i][k] for i in range(3)] for k in range(2)]
    sil = []
    # points of the sphere whose normal is perpendicular to the view direction
    n1 = (dv[1], -dv[0], 0.0)
    n1 = tuple(c / math.sqrt(sum(q * q for q in n1)) for c in n1)
    n2 = (dv[1] * n1[2] - dv[2] * n1[1], dv[2] * n1[0] - dv[0] * n1[2], dv[0] * n1[1] - dv[1] * n1[0])
    # unit vectors normal to the "cone axis" are taken in the ellipsoid frame: s . (dv/A) = 0
    w = [dv[i] / A[i] for i in range(3)]
    wn = math.sqrt(sum(q * q for q in w))
    w = [q / wn for q in w]
    e1 = [w[1], -w[0], 0.0]
    nn = math.hypot(e1[0], e1[1])
    e1 = [q / nn for q in e1]
    e2 = [w[1] * e1[2] - w[2] * e1[1], w[2] * e1[0] - w[0] * e1[2], w[0] * e1[1] - w[1] * e1[0]]
    for i in range(121):
        t = 2 * math.pi * i / 120
        sil.append(proj(tuple(math.cos(t) * e1[j] + math.sin(t) * e2[j] for j in range(3))))
    g.poly(sil, "HEAD", 2.4, fill="ACC", close=True, op=0.22)

    # principal axes
    for i, nm in enumerate(("ib (major axis)", "jb (intermediate)", "kb (minor axis)")):
        s = [0, 0, 0]
        s[i] = 1.0
        tip = proj(s)
        s[i] = -1.0
        back = proj(s)
        if vis([1.0 if k == i else 0.0 for k in range(3)]):
            g.line(G0, tip, "BLUE", 1.8)
        else:
            g.line(G0, back, "BLUE", 1.8)

    def euler(s):
        w3 = [A[i] * s[i] for i in range(3)]
        I = [1 / A[i] ** 2 for i in range(3)]
        d = [(I[1] - I[2]) / I[0] * w3[1] * w3[2], (I[2] - I[0]) / I[1] * w3[2] * w3[0], (I[0] - I[1]) / I[2] * w3[0] * w3[1]]
        return [d[i] / A[i] for i in range(3)]

    def draw_curve(pts, col, w=2.4, arrow_at=None):
        segs = []
        for i in range(len(pts) - 1):
            a, b = pts[i], pts[i + 1]
            front = vis(a) and vis(b)
            if front:
                g.line(proj(a), proj(b), col, w)
        if arrow_at is not None:
            j = next((q for q in range(arrow_at, len(pts) - 1) if vis(pts[q]) and vis(pts[q + 1])), None)
            if j is None:
                return
            a, b = pts[j], pts[(j + 1) % len(pts)]
            ev = euler(a)
            dd = [b[k] - a[k] for k in range(3)]
            sgn = 1 if sum(ev[k] * dd[k] for k in range(3)) >= 0 else -1
            pa, pb = proj(a), proj(b)
            tip = (pa[0] + sgn * (pb[0] - pa[0]) * 0.5, pa[1] + sgn * (pb[1] - pa[1]) * 0.5)
            ang = math.degrees(math.atan2(-(pb[1] - pa[1]) * sgn, (pb[0] - pa[0]) * sgn))
            q = proj(a)
            g.vec(G.ray(q, ang, -9), G.ray(q, ang, 9), None, col, 2.4, head=11)

    # loops around the kb poles (blue) and the ib poles (red)
    for h, col in ((u[2] + 0.18 * (u[1] - u[2]), "BLUE"), (u[2] + 0.5 * (u[1] - u[2]), "BLUE"), (u[2] + 0.8 * (u[1] - u[2]), "BLUE")):
        for sg in (1, -1):
            pts = []
            for i in range(0, 73):
                be = 2 * math.pi * i / 72
                s2 = (h - u[2]) / (u[0] * math.cos(be) ** 2 + u[1] * math.sin(be) ** 2 - u[2])
                al = math.asin(math.sqrt(s2))
                pts.append((math.sin(al) * math.cos(be), math.sin(al) * math.sin(be), sg * math.cos(al)))
            draw_curve(pts, col, 2.4, 12 if (sg == 1 and h < u[2] + 0.6 * (u[1] - u[2])) else None)
    for h in (u[1] + 0.2 * (u[0] - u[1]), u[1] + 0.5 * (u[0] - u[1]), u[1] + 0.8 * (u[0] - u[1])):
        for sg in (1, -1):
            pts = []
            for i in range(0, 73):
                be = 2 * math.pi * i / 72
                s2 = (u[0] - h) / (u[0] - u[1] * math.cos(be) ** 2 - u[2] * math.sin(be) ** 2)
                al = math.asin(math.sqrt(s2))
                pts.append((sg * math.cos(al), math.sin(al) * math.cos(be), math.sin(al) * math.sin(be)))
            draw_curve(pts, "PINK", 2.4, 12 if (sg == 1 and h < u[1] + 0.6 * (u[0] - u[1])) else None)
    # separatrices: two planes crossing along the jb axis
    k = math.sqrt((u[0] - u[1]) / (u[1] - u[2]))
    for sk in (1, -1):
        pts = []
        for i in range(0, 121):
            t = 2 * math.pi * i / 120
            c = math.cos(t) / math.sqrt(1 + k * k)
            pts.append((c, math.sin(t), sk * k * c))
        draw_curve(pts, "HEAD", 2.8)
    # labels
    for i, nm in enumerate(("ib (major axis)", "jb (intermediate)", "kb (minor axis)")):
        sv = [0.0, 0.0, 0.0]
        sv[i] = 1.0 if vis([1.0 if k == i else 0.0 for k in range(3)]) else -1.0
        tip = proj(sv)
        d = (tip[0] - G0[0], tip[1] - G0[1])
        L = math.hypot(*d)
        g.lab(tip, nm, "BLUE", "middle", 16, dx=d[0] / L * 62, dy=d[1] / L * 22 + 5, italic=False)
    return g.sc
