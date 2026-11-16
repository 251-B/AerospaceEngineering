"""Problem 42: particle attracted to the origin (plane of the motion, view along k, free-body diagram, effective potential)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import ORANGE, RED, YELLOW, arrow, away, basis_view
from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

ER = S(bold("e"), "r")
ETH = S(bold("e"), "θ")
TH = 35.0
CT, ST = math.cos(math.radians(TH)), math.sin(math.radians(TH))
EC, AA = 0.5, 2.2                      # sample orbit: eccentricity, semi-major axis
PP = AA * (1 - EC * EC)                # semi-latus rectum 1.65
RP_ = PP / (1 + EC * CT)               # r of P on the sample ellipse
DARK = "#4b5563"


def _r0(sup="P"):
    return bold("r") + f'<tspan baseline-shift="super" font-size="70%">{sup}</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


def _along(sc, a, b, text, col, size, f, off, sign=1):
    """Text parallel to the segment a-b, `off` pixels to one side (sign = 1: the upper side on screen)."""
    ax, ay = sc.P(a)
    bx, by = sc.P(b)
    ang = math.degrees(math.atan2(by - ay, bx - ax))
    mx, my = ax + f * (bx - ax), ay + f * (by - ay)
    nx, ny = by - ay, -(bx - ax)
    n = math.hypot(nx, ny)
    if ny > 0:
        nx, ny = -nx, -ny
    x, y = mx + sign * nx / n * off, my + sign * ny / n * off
    sc.c.add(f'<text x="{x:.1f}" y="{y:.1f}" fill="{col}" font-size="{size}" text-anchor="middle" font-family="Newsreader, \'Times New Roman\', Times, serif" '
             f'style="font-variant-numeric:lining-nums" font-style="italic" transform="rotate({ang:.1f} {x:.1f} {y:.1f})">{text}</text>')


@figure("p42-plane",
        "Plane of the motion with the particle P at polar coordinates r and theta, its position vector and the polar basis, and the right triangle of legs r cos theta and r sin theta.",
        r"Plane of the motion, $\mathbf k$ out of the paper along the constant angular momentum. $\mathbf r_0^P = r\,\mathbf e_r$; in the right triangle of hypotenuse $r$ the leg $r\cos\theta$ lies along $\mathbf i$ and $r\sin\theta$ along $\mathbf j$.")
def plane():
    sc = Scene(780, 660, (400, 330), 100)
    O = (0.0, 0.0)
    r = RP_
    P = (r * CT, r * ST)
    F = (r * CT, 0.0)
    triangle(sc, [O, F, P], YELLOW, 0.30)
    # axes, 3 units each way
    fixed_axis(sc, O, 0, 3.0, "x", off=(14, 5))
    fixed_axis(sc, O, 90, 3.0, "y", off=(0, -10))
    sc.line(O, (-3.0, 0.0), "EDGE", 1.4)
    sc.line(O, (0.0, -3.0), "EDGE", 1.4)
    # sample orbit (focus at O, pericentre on +x)
    sc.curve(lambda t: (PP / (1 + EC * math.cos(t)) * math.cos(t), PP / (1 + EC * math.cos(t)) * math.sin(t)),
             0.0, 2 * math.pi, n=240, col="EDGE", w=1.4, dash="6 5")
    ang = math.radians(152)
    q = (PP / (1 + EC * math.cos(ang)) * math.cos(ang), PP / (1 + EC * math.cos(ang)) * math.sin(ang))
    away(sc, q, (-AA * EC, 0.0), "orbit (sample)", "TEXT", 14, "middle", 14)
    # legs and right angle
    sc.line(O, F, "EDGE", 1.2, "5 4")
    sc.line(F, P, "EDGE", 1.2, "5 4")
    right_angle(sc, F, 180, 90, 0.1)
    sc.label((F[0] / 2, 0.0), "r cos θ", "TEXT", "middle", 15, dx=12, dy=22)
    sc.label((F[0], P[1] / 2), "r sin θ", "TEXT", "start", 15, dx=24, dy=5)
    # position vector and its label above the segment
    sc.vec(O, P, None, "HEAD", 3.6, head=13)
    _along(sc, O, P, _r0() + " = r " + ER, "HEAD", 15, 0.46, 20)
    sc.label((0.78 * P[0], 0.78 * P[1]), "r", "HEAD", "middle", 16, dx=ST * 14, dy=CT * 14 + 5)
    # angle at O
    sc.arc(O, 0.42, 0, TH, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.66, 12), "θ", "GREEN", "middle", 16, dy=5)
    # polar basis at P
    L = 0.9
    tr = (P[0] + L * CT, P[1] + L * ST)
    tt = (P[0] - L * ST, P[1] + L * CT)
    sc.vec(P, tr, None, "BLUE", 2.6, head=11)
    sc.vec(P, tt, None, "BLUE", 2.6, head=11)
    sc.label(tr, ER, "BLUE", "start", 17, weight="700", dx=10, dy=-4)
    sc.label(tt, ETH, "BLUE", "end", 17, weight="700", dx=-14, dy=-10)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=12, dy=22)
    # O, k and the sense of theta
    axis_out(sc, O, None)
    sc.label(O, bold("k") + ", along " + S(bold("H"), "O"), "HEAD", "end", 16, dx=-16, dy=-10)
    sc.arc(O, 0.3, 200, 340, "GREEN", 1.8, head=True)
    sc.label(O, "θ increasing (h > 0)", "GREEN", "end", 14, italic=False, dx=-14, dy=48)
    return sc


@figure("p42-rotation-k",
        "View along k of the polar basis e_r, e_theta turned by theta from i, j, with the two unit right triangles.",
        r"Rotation by $\theta$ about $\mathbf k$ (out of the paper). The triangle of $\mathbf e_\theta$ has its opposite leg along $-\mathbf i$, which gives the minus sign in $\mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j$.")
def rotation_k():
    sc = Scene(860, 600, (330, 290), 80)
    O = (0.0, 0.0)
    basis_view(sc, O, TH, (bold("i"), bold("j")), (ER, ETH), L=2.0, u=1.4, ang="θ",
               legs=("cos θ", "sin θ", "cos θ", "−sin θ on i"), cf=0.9, l1dx=8, l4=(12, "end", 13))
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-6)
    _spin(sc, O, 0.3, 200, 340, "positive about k", (-26, 46), "end")
    _matrix(sc, 3.0, -1.2, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.8)
    return sc


@figure("p42-fbd",
        "Free-body diagram of P with the single central attraction towards O, the velocity split into radial and transverse parts (separate inset), and the angular momentum out of the paper.",
        r"The only force on $P$ is the attraction towards $O$; its line of action passes through $O$, so its moment about $O$ is zero and $\mathbf H_{O,0}$ (out of the paper) is constant.")
def fbd():
    sc = Scene(900, 480, (250, 300), 100)
    O = (0.0, 0.0)
    r = 2.0
    er = (CT, ST)
    et = (-ST, CT)
    P = (r * CT, r * ST)
    # O: cross, the angular momentum out of the paper
    sc.line((-0.27, 0.0), (0.27, 0.0), "EDGE", 1.6)
    sc.line((0.0, -0.27), (0.0, 0.27), "EDGE", 1.6)
    axis_out(sc, (0.0, -0.0), None, r_px=14)
    sc.label(O, S(bold("H"), "O") + " = m r × v (constant)", "HEAD", "start", 15, dx=-8, dy=44)
    sc.label(O, "O", "TEXT", "end", 16, dx=-32, dy=6)
    sc.line(O, P, "EDGE", 1.2, "6 5")
    # attraction
    f = arrow(sc, P, (-CT, -ST), RED, 3.6, 13, 1.2)
    _along(sc, O, P, "F = −(m μ / " + S("r", None, "α") + ") " + ER, RED, 15, 0.52, 18, sign=-1)
    # basis at P
    for d, nm, dx, dy, anc in ((er, ER, 8, 14, "start"), (et, ETH, -8, -6, "end")):
        tip = (P[0] + 0.6 * d[0], P[1] + 0.6 * d[1])
        sc.vec(P, tip, None, "BLUE", 2.6, head=10)
        sc.label(tip, nm, "BLUE", anc, 17, weight="700", dx=dx, dy=dy)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=-4, dy=34)
    # inset: velocity of P, apart from the forces
    x0, y0, x1, y1 = 3.15, 0.0, 6.0, 2.35
    sc.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], "EDGE", 1.2, close=True)
    sc.note((x0 + 0.12, y1 - 0.18), "velocity of P (inset, not a force)", "TEXT", "start", 13)
    Q = (3.75, 0.45)
    for d, nm, off in ((er, "", 0), (et, "", 0)):
        pass
    ve = (0.65 * CT, 0.65 * ST)
    vt = (1.13 * -ST, 1.13 * CT)
    tip = (Q[0] + ve[0] + vt[0], Q[1] + ve[1] + vt[1])
    sc.line((Q[0] + ve[0], Q[1] + ve[1]), tip, "GREEN", 1.0, "3 4")
    sc.line((Q[0] + vt[0], Q[1] + vt[1]), tip, "GREEN", 1.0, "3 4")
    _dvec(sc, Q, (Q[0] + ve[0], Q[1] + ve[1]), "GREEN", 2.0, 9)
    _dvec(sc, Q, (Q[0] + vt[0], Q[1] + vt[1]), "GREEN", 2.0, 9)
    sc.vec(Q, tip, None, "GREEN", 3.2, head=12)
    sc.label(tip, S(bold("v"), "0", "P") , "GREEN", "start", 17, weight="700", dx=10, dy=-4)
    sc.label((Q[0] + ve[0], Q[1] + ve[1]), "ṙ " + ER, "GREEN", "start", 15, dx=10, dy=18)
    sc.label((Q[0] + vt[0], Q[1] + vt[1]), "r θ̇ " + ETH, "GREEN", "end", 15, dx=-8, dy=18)
    sc.arc(Q, 0.45, TH, TH + 60, "GREEN", 1.4, head=True)
    sc.label(_pol(Q, 0.64, TH + 40), "60°", "GREEN", "middle", 14, italic=False, dy=5)
    sc.dotp(Q, 4.0)
    sc.note((-1.0, -1.05), "inertial frame: no inertia forces; no constraint", "TEXT", "start", 13)
    return sc


# ---------------------------------------------------------------------------------------------- effective potential
def _roots(fn, lo, hi, n=4000):
    out = []
    a = lo
    fa = fn(a)
    for i in range(1, n + 1):
        b = lo + (hi - lo) * i / n
        fb = fn(b)
        if fa == 0 or fa * fb < 0:
            x0, x1 = a, b
            for _ in range(60):
                m = 0.5 * (x0 + x1)
                if fn(x0) * fn(m) <= 0:
                    x1 = m
                else:
                    x0 = m
            out.append(0.5 * (x0 + x1))
        a, fa = b, fb
    return out


class _Panel:
    def __init__(self, sc, x0, y0, wpx, hpx, umax, wmin, wmax, title):
        """(x0, y0): world (pixel) position of the corner of the plot window; u from 0 to umax, W from wmin to wmax;
        the horizontal axis is drawn at W = 0."""
        self.sc, self.x0, self.y0, self.wpx, self.hpx = sc, x0, y0, wpx, hpx
        self.umax, self.wmin, self.wmax = umax, wmin, wmax
        sc.vec((x0, self.V(0)), (x0 + wpx + 14, self.V(0)), None, "EDGE", 1.4, head=8)
        sc.vec((x0, y0), (x0, y0 + hpx + 12), None, "EDGE", 1.4, head=8)
        sc.label((x0 + wpx + 14, self.V(0)), "u", "TEXT", "middle", 16, weight="700", dx=2, dy=-8)
        sc.label((x0, y0 + hpx + 12), "W(u)", "TEXT", "start", 16, weight="700", dx=8, dy=6)
        sc.label((x0 + wpx / 2, y0 + hpx), title, "HEAD", "middle", 17, italic=False, weight="700", dy=14)

    def U(self, u):
        return self.x0 + u * self.wpx / self.umax

    def V(self, w):
        return self.y0 + (w - self.wmin) * self.hpx / (self.wmax - self.wmin)

    def pt(self, u, w):
        return (self.U(u), self.V(w))

    def curve(self, fn, u0, u1, col=DARK, w=2.4, dash=None):
        run = []
        n = 400
        for i in range(n + 1):
            u = u0 + (u1 - u0) * i / n
            ww = fn(u)
            if self.wmin <= ww <= self.wmax:
                run.append(self.pt(u, ww))
            elif run:
                self.sc.poly(run, col, w, dash)
                run = []
        if run:
            self.sc.poly(run, col, w, dash)

    def level(self, e, u0, u1, col=ORANGE, dash=None, w=1.2):
        self.sc.line(self.pt(u0, e), self.pt(u1, e), col, w, dash)

    def seg(self, e, u0, u1, col=ORANGE):
        self.sc.line(self.pt(u0, e), self.pt(u1, e), col, 5.0)

    def dot(self, u, w, col=DARK, r=4.2):
        self.sc.dotp(self.pt(u, w), r, col)

    def tick(self, u, text, dy=18, col="TEXT"):
        x, y = self.pt(u, 0.0)
        self.sc.line((x, y - 3), (x, y + 3), "EDGE", 1.2)
        self.sc.label((x, y), text, col, "middle", 13, dy=dy)


@figure("p42-weff",
        "Effective potential W(u) for the exponents 1, 2, 3 and 4, with energy levels showing bounded, escaping and falling motions.",
        r"Effective potential $W(u)$ with $\mu/h^2 = 1$. The motion is possible only where $W(u)$ lies below the level $E^*$: a well (exponents 1 and 2) gives oscillations, the barrier of the exponent 4 separates escape from fall, and for the exponent 3 the sign of $1 - \mu/h^2$ decides.")
def weff():
    H = 700
    sc = Scene(820, H, (0, H), 1)
    pw, ph = 300, 240
    # ---- alpha = 1
    p = _Panel(sc, 50, 400, pw, ph - 40, 2.4, -0.4, 4.8, "α = 1")
    f1 = lambda u: u * u - 2 * math.log(u)
    p.curve(f1, 0.15, 2.4)
    p.dot(1.0, 1.0)
    sc.label(p.pt(1.0, 1.0), S("u", "c"), "TEXT", "middle", 14, dx=0, dy=22)
    r1 = _roots(lambda u: f1(u) - 1.5, 0.15, 2.4)
    p.level(1.5, 0.0, 2.4, dash=None)
    p.seg(1.5, r1[0], r1[1])
    for rt in r1:
        p.dot(rt, 1.5, ORANGE)
    sc.label(p.pt(0.5 * (r1[0] + r1[1]), 1.5), "(iii) bounded", ORANGE, "middle", 14, italic=False, dy=-12)
    sc.label(p.pt(2.4, 1.5), "E* = 1.5", ORANGE, "end", 13, italic=False, dy=16)
    # ---- alpha = 2
    p = _Panel(sc, 470, 400, pw, ph - 40, 2.6, -1.35, 1.35, "α = 2")
    f2 = lambda u: u * u - 2 * u
    p.curve(f2, 0.0, 2.6)
    p.dot(1.0, -1.0)
    sc.label(p.pt(1.0, -1.0), "circle", "TEXT", "middle", 14, dy=22)
    p.level(-0.5, 0.0, 2.6)
    p.seg(-0.5, 0.2929, 1.7071)
    for rt in (0.2929, 1.7071):
        p.dot(rt, -0.5, ORANGE)
    sc.label(p.pt(1.0, -0.5), "(iii) ellipse", ORANGE, "middle", 14, italic=False, dy=-12)
    p.level(0.5, 0.0, 2.6)
    p.seg(0.5, 0.0, 2.2247)
    p.dot(2.2247, 0.5, ORANGE)
    sc.label(p.pt(1.1, 0.5), "(i) escape", ORANGE, "middle", 14, italic=False, dy=-12)
    # ---- alpha = 3
    p = _Panel(sc, 50, 70, pw, ph - 20, 1.8, -3.4, 1.8, "α = 3")
    p.curve(lambda u: 0.5 * u * u, 0.0, 1.8, w=2.4)
    p.curve(lambda u: -u * u, 0.0, 1.8, w=2.4)
    sc.label(p.pt(1.8, 0.5 * 1.8 * 1.8), "K < 1", "TEXT", "end", 15, dx=-10, dy=-8)
    sc.label(p.pt(1.8, -1.8 * 1.8), "K > 1", "TEXT", "end", 15, dx=-10, dy=22)
    sc.label(p.pt(1.8, 0.0), "K = 1 (W = 0)", "TEXT", "end", 14, italic=False, dx=-4, dy=18)
    # ---- alpha = 4
    p = _Panel(sc, 470, 70, pw, ph - 20, 1.9, -0.45, 0.85, "α = 4")
    f4 = lambda u: u * u - (2.0 / 3.0) * u ** 3
    p.curve(f4, 0.0, 1.9)
    p.dot(1.0, 1.0 / 3.0)
    sc.label(p.pt(1.0, 1.0 / 3.0), S("u", "b") + ", unstable circle", "TEXT", "middle", 14, dy=-10)
    p.dot(1.5, 0.0)
    sc.label(p.pt(1.5, 0.0), S("u", "z"), "TEXT", "start", 14, dx=8, dy=-8)
    p.level(0.2, 0.0, 1.9)
    r4 = _roots(lambda u: f4(u) - 0.2, 0.2, 1.8)
    p.seg(0.2, 0.0, r4[0])
    p.seg(0.2, r4[1], 1.9)
    p.dot(r4[0], 0.2, ORANGE)
    p.dot(r4[1], 0.2, ORANGE)
    sc.label(p.pt(0.28, 0.2), "(i)", ORANGE, "middle", 14, italic=False, dy=-12)
    sc.label(p.pt(1.62, 0.2), "(ii)", ORANGE, "middle", 14, italic=False, dy=-12)
    p.level(0.5, 0.0, 1.9, dash="6 4")
    sc.label(p.pt(1.9, 0.5), "no turning point", ORANGE, "end", 14, italic=False, dy=-8)
    return sc
