"""Figures of Advanced Maths chapters 5 and 6 (phase portraits of nonlinear systems, potential wells, the
transcendental eigenvalue equation tan(mu) = -mu and Fourier partial sums).

Every orbit is integrated numerically (RK4 along the normalised direction field, constant arclength steps) and
clipped to the plot box; equilibria are classified from the numerical Jacobian.  Pure stdlib.
"""
import math

from figures.svgkit import Canvas, arrow_head, circle, dot, line, poly, sub, text

W, H = 360, 320
L0, R0, T0, B0 = 46.0, 346.0, 20.0, 262.0       # plot box in pixels (single-panel figures)
DS, NMAX = 0.008, 3000                          # arclength step (box = 1) and step limit
PI = math.pi
MINUS = "−"
PRIME = "′"


def it(s):
    return f'<tspan font-style="italic">{s}</tspan>'


def nice(lo, hi, n=5):
    step = (hi - lo) / n
    mag = 10 ** math.floor(math.log10(step))
    for m in (1, 2, 2.5, 5, 10):
        if step <= m * mag + 1e-12:
            step = m * mag
            break
    t = math.ceil(lo / step - 1e-9) * step
    out = []
    while t <= hi + 1e-9:
        v = round(t, 9) + 0.0
        out.append((v, f"{v:g}".replace("-", MINUS)))
        t += step
    return out


class Plot:
    """A plot box with its data window, clip path, ticks and frame."""

    def __init__(self, c, cid, box, rect=(L0, T0, R0, B0)):
        self.c, self.cid, self.box = c, cid, box
        self.l, self.t, self.r, self.b = rect

    def px(self, x, y):
        x0, x1, y0, y1 = self.box
        return (self.l + (self.r - self.l) * (x - x0) / (x1 - x0), self.b - (self.b - self.t) * (y - y0) / (y1 - y0))

    def pix(self, u, v):                        # normalised box coordinates -> pixels
        return (self.l + u * (self.r - self.l), self.b - v * (self.b - self.t))

    def frame(self, xt, yt, xlab=None, ylab=None, xnums=True):
        c = self.c
        x0, x1, y0, y1 = self.box
        c.add(f'<defs><clipPath id="{self.cid}"><rect x="{self.l}" y="{self.t}" width="{self.r - self.l}" '
              f'height="{self.b - self.t}"/></clipPath></defs>')
        if x0 < 0 < x1:
            xz = self.px(0, 0)[0]
            line(c, (xz, self.t), (xz, self.b), "EDGE", 1.0)
        if y0 < 0 < y1:
            yz = self.px(0, 0)[1]
            line(c, (self.l, yz), (self.r, yz), "EDGE", 1.0)
        c.add(f'<rect x="{self.l}" y="{self.t}" width="{self.r - self.l}" height="{self.b - self.t}" '
              f'fill="none" stroke="EDGE" stroke-width="1"/>')
        for v, lab in xt:
            x = self.px(v, 0)[0]
            line(c, (x, self.b), (x, self.b + 4), "EDGE", 1.0)
            if xnums:
                text(c, (x, self.b + 16), lab, "TEXT", "middle", 11)
        for v, lab in yt:
            y = self.px(0, v)[1]
            line(c, (self.l - 4, y), (self.l, y), "EDGE", 1.0)
            text(c, (self.l - 7, y + 4), lab, "TEXT", "end", 11)
        if xlab:
            text(c, (self.r, self.b + 31), xlab, "TEXT", "end", 13)
        if ylab:
            text(c, (self.l, self.t - 7), ylab, "TEXT", "start", 13)


def _plain_len(s):
    n, skip = 0, False
    for ch in s:
        if ch == "<":
            skip = True
        elif ch == ">":
            skip = False
        elif not skip:
            n += 1
    return n


def legend(c, x, y, items):
    """items: ("line", colour, dash, label) or ("dot", colour, None, label)."""
    for kind, col, dash, label in items:
        if kind == "line":
            line(c, (x, y - 4), (x + 20, y - 4), col, 1.8, dash)
            x += 26
        else:
            dot(c, (x + 4, y - 4), 4, col)
            x += 14
        text(c, (x, y), label, "TEXT", "start", 11)
        x += _plain_len(label) * 6.4 + 18


# --------------------------------------------------------------------------- orbits
def classify(f, p):
    h = 1e-5
    fx1, fx0 = f(p[0] + h, p[1]), f(p[0] - h, p[1])
    fy1, fy0 = f(p[0], p[1] + h), f(p[0], p[1] - h)
    a, b = (fx1[0] - fx0[0]) / (2 * h), (fy1[0] - fy0[0]) / (2 * h)
    cc, d = (fx1[1] - fx0[1]) / (2 * h), (fy1[1] - fy0[1]) / (2 * h)
    tr, det = a + d, a * d - b * cc
    disc = tr * tr - 4 * det
    if disc < 0 and abs(tr) <= 1e-6:
        return "centre"
    if disc >= 0:
        r = math.sqrt(disc)
        lo, hi = (tr - r) / 2, (tr + r) / 2
    else:
        lo = hi = tr / 2
    if hi < -1e-6:
        return "attr"
    if lo > 1e-6:
        return "rep"
    return "saddle"


def trace(f, box, seed, sign, targets, cap):
    """Orbit through `seed` in normalised box coordinates, forwards (sign=1) or backwards; (points, closed)."""
    x0, x1, y0, y1 = box
    sx, sy = x1 - x0, y1 - y0

    def g(u, v):
        fx, fy = f(x0 + u * sx, y0 + v * sy)
        gx, gy = fx / sx, fy / sy
        n = math.hypot(gx, gy)
        return (gx / n, gy / n) if n > 1e-12 else (0.0, 0.0)

    u0, v0 = (seed[0] - x0) / sx, (seed[1] - y0) / sy
    u, v = u0, v0
    pts = [(u, v)]
    h = sign * DS
    for k in range(NMAX):
        k1 = g(u, v)
        if k1 == (0.0, 0.0):
            break
        k2 = g(u + h / 2 * k1[0], v + h / 2 * k1[1])
        k3 = g(u + h / 2 * k2[0], v + h / 2 * k2[1])
        k4 = g(u + h * k3[0], v + h * k3[1])
        u += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        pts.append((u, v))
        if not (-0.03 <= u <= 1.03 and -0.03 <= v <= 1.03):
            break
        for tu, tv in targets:
            if math.hypot(u - tu, v - tv) < cap:
                pts.append((tu, tv))
                return pts, False
        if k > 25 and math.hypot(u - u0, v - v0) < 1.2 * DS:
            pts.append((u0, v0))
            return pts, True
    return pts, False


def thin(pts, min_dist=1.5):
    out = [pts[0]]
    for q in pts[1:]:
        if math.hypot(q[0] - out[-1][0], q[1] - out[-1][1]) >= min_dist:
            out.append(q)
    return out


def heads(c, pix, plot, col="BLUE"):
    n = len(pix)
    if n < 6:
        return
    length = sum(math.hypot(pix[i + 1][0] - pix[i][0], pix[i + 1][1] - pix[i][1]) for i in range(n - 1))
    fracs = (0.3, 0.7) if length > 150 else ((0.5,) if length > 35 else ())
    for fr in fracs:
        i = min(max(int(fr * (n - 1)), 2), n - 3)
        a, b = pix[i - 2], pix[i + 2]
        d = math.hypot(b[0] - a[0], b[1] - a[1])
        if d < 1e-6:
            continue
        ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
        p = pix[i]
        if not (plot.l + 4 < p[0] < plot.r - 4 and plot.t + 4 < p[1] < plot.b - 4):
            continue
        arrow_head(c, (p[0] - ux, p[1] - uy), (p[0] + 3.5 * ux, p[1] + 3.5 * uy), col, 8)


def clip_line(a, b, cc, box):
    """End points of the line a x + b y = cc inside the box."""
    x0, x1, y0, y1 = box
    cand = []
    if abs(b) > 1e-12:
        for x in (x0, x1):
            y = (cc - a * x) / b
            if y0 - 1e-9 <= y <= y1 + 1e-9:
                cand.append((x, y))
    if abs(a) > 1e-12:
        for y in (y0, y1):
            x = (cc - b * y) / a
            if x0 - 1e-9 <= x <= x1 + 1e-9:
                cand.append((x, y))
    uniq = []
    for p in cand:
        if all(math.hypot(p[0] - q[0], p[1] - q[1]) > 1e-9 for q in uniq):
            uniq.append(p)
    return uniq[:2] if len(uniq) >= 2 else []


def portrait(plot, f, eqs, seeds, cap=0.015, lines=(), curves=()):
    """Nullclines, extra curves, orbits with arrowheads and equilibria in `plot`."""
    c, box = plot.c, plot.box
    x0, x1, y0, y1 = box
    kinds = [(p[0], p[1], p[2] if len(p) > 2 else classify(f, p)) for p in eqs]

    def norm(p):
        return ((p[0] - x0) / (x1 - x0), (p[1] - y0) / (y1 - y0))

    fwd_t = [norm(p) for p in kinds if p[2] == "attr"]
    bwd_t = [norm(p) for p in kinds if p[2] == "rep"]
    c.add(f'<g clip-path="url(#{plot.cid})">')
    for kind, a, b, cc in lines:
        seg = clip_line(a, b, cc, box)
        if seg:
            pts = [plot.px(*q) for q in seg]
            if kind == "x":
                poly(c, pts, "ACC", 1.8, "6 4")
            else:
                poly(c, pts, "GREEN", 1.8, "2 4")
    for pts, col, dash in curves:
        poly(c, [plot.px(*q) for q in pts], col, 1.6, dash)
    for s in seeds:
        u, v = norm(s)
        if any(math.hypot(u - t[0], v - t[1]) < 2 * cap for t in fwd_t + bwd_t):
            continue
        fw, closed = trace(f, box, s, 1, fwd_t, cap)
        pts = fw if closed else trace(f, box, s, -1, bwd_t, cap)[0][::-1][:-1] + fw
        pix = thin([plot.pix(a, b) for a, b in pts])
        if len(pix) < 3:
            continue
        poly(c, pix, "BLUE", 1.5)
        heads(c, pix, plot)
    c.add("</g>")
    for x, y, kind in kinds:
        p = plot.px(x, y)
        if kind in ("attr", "centre"):
            dot(c, p, 4, "GREEN")
        else:
            circle(c, p, 4, "PINK", 1.8)


def fr(box, pts):
    return [(box[0] + u * (box[1] - box[0]), box[2] + v * (box[3] - box[2])) for u, v in pts]


FR = [(.1, .1), (.3, .6), (.6, .3), (.8, .8), (.15, .9), (.9, .15), (.45, .45), (.7, .55), (.25, .3)]
NUL = [("line", "ACC", "6 4", it("x") + PRIME + " = 0"), ("line", "GREEN", "2 4", it("y") + PRIME + " = 0")]


def pop(f, box, eq, lines, seeds=None):
    return dict(f=f, box=box, eq=eq, lines=lines, seeds=seeds or fr(box, FR), xl="x", yl="y", legend=NUL)


def _sep_theta():
    xs = [-2 * PI + 4 * PI * i / 400 for i in range(401)]
    return [([(x, 2 * math.cos(x / 2)) for x in xs], "ACC", "6 4"), ([(x, -2 * math.cos(x / 2)) for x in xs], "ACC", "6 4")]


def _pend(k):
    return lambda x, y: (y, -math.sin(x) - k * y)


_PEND_BOX = (-2 * PI, 2 * PI, -3.0, 3.0)
_PEND_XT = [(v, lab) for v, lab in ((-2 * PI, MINUS + "2π"), (-PI, MINUS + "π"), (0, "0"), (PI, "π"), (2 * PI, "2π"))]
_PEND_EQ = [(0, 0), (PI, 0), (-PI, 0), (2 * PI, 0), (-2 * PI, 0)]
_PEND_SADDLE_SEEDS = [(PI + .06, .06), (PI - .06, -.06), (-PI + .06, .06), (-PI - .06, -.06)]

_B2 = (0.0, 2.5, 0.0, 2.5)
_B2III = (0.0, 2.4, 0.0, 2.4)
_B2IV = (0.0, 1.5, 0.0, 1.1)
_B2V = (0.0, 9.0, 0.0, 2.8)
_B2VI = (0.0, 11.0, 0.0, 1.8)
_B2VII = (0.0, 3.8, 0.0, 3.2)
_B3I = (0.0, 4.2, 0.0, 4.2)
_B3II = (0.0, 6.0, 0.0, 6.0)

PORTRAITS = {
    "ch5-e1": dict(f=lambda x, y: (-y - x * (x * x + y * y), x - y * (x * x + y * y)), box=(-1.2, 1.2, -1.2, 1.2),
                   eq=[(0, 0, "attr")], seeds=[(1.1, 0.0), (0.0, -0.55), (-0.3, 0.2)], cap=0.05, xl="x", yl="y"),
    "ch5-e2-i": pop(lambda x, y: (x * (2 - x - y), y * (2 - 2 * y - 2 * x)), _B2,
                    [(0, 0), (2, 0), (0, 1)], [("x", 1, 1, 2), ("y", 1, 1, 1)]),
    "ch5-e2-ii": pop(lambda x, y: (x * (2 - x - y), y * (2 - 2 * y - x / 4)), _B2,
                     [(0, 0), (2, 0), (0, 1), (8 / 7, 6 / 7)], [("x", 1, 1, 2), ("y", 0.25, 2, 2)]),
    "ch5-e2-iii": pop(lambda x, y: (x * (2 - x - 3 * y), y * (2 - 2 * y - 3 * x)), _B2III,
                      [(0, 0), (2, 0), (0, 1), (2 / 7, 4 / 7)], [("x", 1, 3, 2), ("y", 3, 2, 2)]),
    "ch5-e2-iv": pop(lambda x, y: (x * (1 - 2 * y), y * (-2 + 3 * x)), _B2IV,
                     [(0, 0), (2 / 3, 0.5)], [("x", 0, 1, 0.5), ("y", 1, 0, 2 / 3)],
                     [(0.72, 0.5), (0.78, 0.5), (0.92, 0.5), (1.1, 0.5)]),
    "ch5-e2-v": pop(lambda x, y: (x * (4 - x / 2 - 3 * y), y * (-2 + x)), _B2V,
                    [(0, 0), (8, 0), (2, 1)], [("x", 0.5, 3, 4), ("y", 1, 0, 2)]),
    "ch5-e2-vi": pop(lambda x, y: (x * (10 - x - 3 * y), y * (1 + x - 10 * y)), _B2VI,
                     [(0, 0), (10, 0), (0, 0.1), (97 / 13, 11 / 13)], [("x", 1, 3, 10), ("y", 1, -10, -1)]),
    "ch5-e2-vii": pop(lambda x, y: (x * (3 - x - y), y * (-2 + x)), _B2VII,
                      [(0, 0), (3, 0), (2, 1)], [("x", 1, 1, 3), ("y", 1, 0, 2)]),
    "ch5-e3-i": pop(lambda x, y: (x * (1 - x + y), y * (1 + x - 2 * y)), _B3I,
                    [(0, 0), (1, 0), (0, 0.5), (3, 2)], [("x", 1, -1, 1), ("y", 1, -2, -1)]),
    "ch5-e3-ii": pop(lambda x, y: (x * (2 - x + y), y * (4 + 2 * x - y)), _B3II,
                     [(0, 0), (2, 0), (0, 4)], [("x", 1, -1, 2), ("y", 2, -1, -4)]),
    "ch5-e5-i": dict(f=lambda x, y: (y, -x / (1 + x * x)), box=(-2.0, 2.0, -2.0, 2.0), eq=[(0, 0)],
                     seeds=[(0.5, 0), (1.0, 0), (1.6, 0), (0, 1.0), (0, 1.5)], xl="x", yl="y"),
    "ch5-e5-ii": dict(f=lambda x, y: (y, -(2 * x ** 3 - 2 * x) * (1 + (6 * x * x - 2) * y * y) / (1 + (2 * x ** 3 - 2 * x) ** 2)),
                      box=(-1.8, 1.8, -1.4, 1.4), eq=[(-1, 0), (0, 0), (1, 0)],
                      seeds=[(1.25, 0), (1.5, 0), (-1.25, 0), (-1.5, 0), (0, 0.6), (0, 1.1)], xl="x", yl="y"),
    "ch5-e6-i": dict(f=lambda x, y: (y, -x - y), box=(-2.0, 2.0, -2.0, 2.0), eq=[(0, 0)],
                     seeds=[(1.8, 0.2), (-1.2, -1.0), (0.3, 1.6), (-0.2, -1.8)], xl="x", yl="y"),
    "ch5-e6-ii": dict(f=lambda x, y: (y, -2 * x * (x * x - 1) - y), box=(-1.8, 1.8, -1.5, 1.5),
                      eq=[(0, 0), (1, 0), (-1, 0)],
                      seeds=[(1.6, 0.9), (-1.6, -0.9), (0.3, 1.2), (-0.3, -1.2), (1.0, 0.5), (-1.0, -0.5),
                             (0.06, 0.06), (-0.06, -0.06), (0.06, -0.06), (-0.06, 0.06)], xl="x", yl="y"),
    "ch5-e6-iii-sheet": dict(f=lambda x, y: (y, -(3 * x ** 5 - 5 * x ** 3 + 4 * x) - y), box=(-1.5, 1.5, -1.5, 1.5),
                             eq=[(0, 0)], seeds=[(1.4, 0), (-1.4, 0), (0, 1.3), (0, -1.3), (1.0, -1.0), (-0.9, 0.9)],
                             xl="x", yl="y"),
    "ch5-e6-iii-robinson": dict(f=lambda x, y: (y, -x * (x * x - 1) * (x * x - 4) - y), box=(-2.8, 2.8, -3.5, 3.5),
                                eq=[(0, 0), (1, 0), (-1, 0), (2, 0), (-2, 0)],
                                seeds=[(2.6, 0.5), (-2.6, -0.5), (0.5, 0.8), (-0.5, -0.8), (1.5, 1.5), (-1.5, -1.5),
                                       (1.06, 0.06), (-1.06, -0.06), (0, 3.0), (0, -3.0)], xl="x", yl="y"),
    "ch5-e8": dict(f=_pend(0.0), box=_PEND_BOX, eq=_PEND_EQ, xt=_PEND_XT, xl="θ", yl="y", curves=_sep_theta(),
                   seeds=[(0.7, 0), (1.6, 0), (2.5, 0), (-0.7, 0), (2 * PI - 1.6, 0), (-2 * PI + 1.6, 0),
                          (0, 2.3), (0, 2.8), (0, -2.3), (0, -2.8)],
                   legend=[("line", "ACC", "6 4", "separatrix")]),
    "ch5-e9-under": dict(f=_pend(0.6), box=_PEND_BOX, eq=_PEND_EQ, xt=_PEND_XT, xl="θ", yl="y",
                         seeds=[(2.5, 0.5), (-2.5, -0.5), (0, 2.8), (0, -2.8), (4.5, 1.0), (-4.5, -1.0)]
                         + _PEND_SADDLE_SEEDS),
    "ch5-e9-over": dict(f=_pend(2.5), box=_PEND_BOX, eq=_PEND_EQ, xt=_PEND_XT, xl="θ", yl="y",
                        seeds=[(2.5, 0.5), (-2.5, -0.5), (0, 2.8), (0, -2.8), (4.5, 1.0), (-4.5, -1.0),
                               (1.5, -2.0), (-1.5, 2.0)] + _PEND_SADDLE_SEEDS),
    "ch5-e10": dict(f=lambda x, y: (y, -math.sin(x) - 0.5 * y * abs(y)), box=(-PI, PI, -2.5, 2.5),
                    eq=[(0, 0, "attr"), (PI, 0), (-PI, 0)], cap=0.06, xl="x", yl="y",
                    xt=[(-PI, MINUS + "π"), (-PI / 2, MINUS + "π/2"), (0, "0"), (PI / 2, "π/2"), (PI, "π")],
                    seeds=[(2.5, 0.3), (-2.5, -0.3), (1.5, 1.5), (-1.5, -1.5), (0, 2.3), (0, -2.3), (1.0, 0),
                           (PI - .06, -.06), (-PI + .06, .06)]),
}


def _portrait_fig(cfg, uid):
    c = Canvas(W, H)
    p = Plot(c, uid, cfg["box"])
    b = cfg["box"]
    p.frame(cfg.get("xt") or nice(b[0], b[1]), nice(b[2], b[3]), it(cfg["xl"]), it(cfg["yl"]))
    portrait(p, cfg["f"], cfg["eq"], cfg["seeds"], cfg.get("cap", 0.015), cfg.get("lines", ()), cfg.get("curves", ()))
    if cfg.get("legend"):
        legend(c, L0, 312, cfg["legend"])
    return c


# --------------------------------------------------------------------------- potential V(x) above the phase portrait
def _sep_levels(V, level, x_lo, x_hi, n=500):
    xs = [x_lo + (x_hi - x_lo) * i / n for i in range(n + 1)]
    up = [(x, math.sqrt(max(0.0, 2 * (level - V(x))))) for x in xs]
    return [(up, "ACC", "6 4"), ([(x, -y) for x, y in up], "ACC", "6 4")]


_V3 = lambda x: x ** 6 / 6 - 1.25 * x ** 4 + 2 * x * x           # noqa: E731
_V3L = 1 / 6 - 1.25 + 2

STACKED = {
    "ch5-e4-i": dict(V=lambda x: 0.5 * x * x, dV=lambda x: x, xr=(-2.2, 2.2), vr=(0.0, 2.6), yr=(-2.4, 2.4),
                     eq=[(0, "c")], seeds=[(0.8, 0), (1.4, 0), (2.0, 0)]),
    "ch5-e4-ii": dict(V=lambda x: 0.5 * x ** 4 - x * x, dV=lambda x: 2 * x ** 3 - 2 * x, xr=(-1.8, 1.8), vr=(-0.7, 2.2),
                      yr=(-1.9, 1.9), eq=[(-1, "c"), (0, "s"), (1, "c")], level=0.0,
                      seeds=[(1.0, 0.4), (1.0, 0.75), (-1.0, -0.4), (-1.0, -0.75), (0, 1.0), (0, 1.5)],
                      curves=_sep_levels(lambda x: 0.5 * x ** 4 - x * x, 0.0, -math.sqrt(2), math.sqrt(2))),
    "ch5-e4-iii-sheet": dict(V=lambda x: 0.5 * x ** 6 - 1.25 * x ** 4 + 2 * x * x, dV=lambda x: 3 * x ** 5 - 5 * x ** 3 + 4 * x,
                             xr=(-1.6, 1.6), vr=(0.0, 5.6), yr=(-3.2, 3.2), eq=[(0, "c")],
                             seeds=[(0.5, 0), (0.95, 0), (1.4, 0)]),
    "ch5-e4-iii-robinson": dict(V=_V3, dV=lambda x: x ** 5 - 5 * x ** 3 + 4 * x, xr=(-2.5, 2.5), vr=(-1.6, 4.6),
                                yr=(-3.2, 3.2), eq=[(-2, "c"), (-1, "s"), (0, "c"), (1, "s"), (2, "c")], level=_V3L,
                                seeds=[(0.45, 0), (0, 1.0), (1.6, 0), (-1.6, 0), (1.95, 0), (-1.95, 0), (0, 2.0), (0, 2.5)],
                                curves=_sep_levels(_V3, _V3L, -2.345, 2.345)),
}


def _stacked_fig(cfg, uid):
    c = Canvas(380, 350)
    xr, vr, yr = cfg["xr"], cfg["vr"], cfg["yr"]
    top = Plot(c, uid, (xr[0], xr[1], vr[0], vr[1]), (50, 22, 360, 112))
    bot = Plot(c, uid + "-p", (xr[0], xr[1], yr[0], yr[1]), (50, 156, 360, 316))
    xt = nice(xr[0], xr[1])
    top.frame(xt, nice(vr[0], vr[1], 4), None, it("V") + "(" + it("x") + ")", xnums=False)
    bot.frame(xt, nice(yr[0], yr[1]), it("x"), it("y"))
    V, dV = cfg["V"], cfg["dV"]
    c.add(f'<g clip-path="url(#{uid})">')
    if "level" in cfg:
        poly(c, [top.px(xr[0], cfg["level"]), top.px(xr[1], cfg["level"])], "ACC", 1.5, "6 4")
    n = 400
    poly(c, [top.px(xr[0] + (xr[1] - xr[0]) * i / n, V(xr[0] + (xr[1] - xr[0]) * i / n)) for i in range(n + 1)], "BLUE", 2.0)
    c.add("</g>")
    eqs = []
    for xe, k in cfg["eq"]:
        line(c, (top.px(xe, 0)[0], top.b), (bot.px(xe, 0)[0], bot.t), "EDGE", 1.0, "2 3")
        eqs.append((xe, 0, "centre" if k == "c" else "saddle"))
        if k == "c":
            dot(c, top.px(xe, V(xe)), 4, "GREEN")
        else:
            circle(c, top.px(xe, V(xe)), 4, "PINK", 1.8)
    portrait(bot, lambda x, y: (y, -dV(x)), eqs, cfg["seeds"], 0.015, (), cfg.get("curves", ()))
    if "level" in cfg:
        legend(c, 50, 345, [("line", "ACC", "6 4", "separatrix")])
    return c


# --------------------------------------------------------------------------- Chapter 6
def _tan_fig(uid):
    c = Canvas(W, H)
    box = (0.0, 3 * PI, -10.0, 10.0)
    p = Plot(c, uid, box)
    xt = [(k * PI / 2, lab) for k, lab in enumerate(["0", "π/2", "π", "3π/2", "2π", "5π/2", "3π"])]
    p.frame(xt, [(v, f"{v:g}".replace("-", MINUS)) for v in (-10, -5, 0, 5, 10)], it("μ"), it("y"))
    c.add(f'<g clip-path="url(#{uid})">')
    for pole in (PI / 2, 3 * PI / 2, 5 * PI / 2):
        line(c, p.px(pole, -10), p.px(pole, 10), "EDGE", 1.0, "3 4")
    ends = [0.0, PI / 2, 3 * PI / 2, 5 * PI / 2, 3 * PI]
    for a, b in zip(ends[:-1], ends[1:]):
        lo = a + (0.004 if a > 0 else 0.0)
        hi = b - (0.004 if b < 3 * PI else 0.0)
        pts = []
        for i in range(401):
            m = lo + (hi - lo) * i / 400
            pts.append(p.px(m, max(-14.0, min(14.0, math.tan(m)))))
        poly(c, pts, "BLUE", 2.0)
    poly(c, [p.px(0, 0), p.px(3 * PI, -3 * PI)], "ACC", 1.8)
    c.add("</g>")
    for k in range(3):
        a, b = PI / 2 + k * PI + 1e-6, PI + k * PI
        for _ in range(60):
            m = (a + b) / 2
            if math.tan(m) + m < 0:
                a = m
            else:
                b = m
        mu = (a + b) / 2
        line(c, p.px(mu, -mu), p.px(mu, 0), "PINK", 1.0, "2 3")
        dot(c, p.px(mu, -mu), 4, "PINK")
        text(c, p.px(mu, 0), sub("μ", str(k + 1)), "PINK", "middle", 13, "600", 0, -7)
    legend(c, L0, 312, [("line", "BLUE", None, "tan " + it("μ")), ("line", "ACC", None, MINUS + it("μ"))])
    return c


def _partial(f, n_terms):
    nq = 4000
    h = 2.0 / nq
    xs = [-1 + (i + 0.5) * h for i in range(nq)]
    fv = [f(x) for x in xs]
    a0 = sum(fv) * h
    a = [sum(v * math.cos(k * PI * x) for x, v in zip(xs, fv)) * h for k in range(1, n_terms + 1)]
    b = [sum(v * math.sin(k * PI * x) for x, v in zip(xs, fv)) * h for k in range(1, n_terms + 1)]
    return lambda x: a0 / 2 + sum(a[k - 1] * math.cos(k * PI * x) + b[k - 1] * math.sin(k * PI * x) for k in range(1, n_terms + 1))


FOURIER = {
    "ch6-e8-i": (lambda x: x * x, (-0.2, 1.25), 1, 5, None),
    "ch6-e8-ii": (math.exp, (0.0, 3.2), 2, 10, math.cosh(1)),
    "ch6-e8-iii": (lambda x: 1.0 if x < 0 else x + 1.0, (0.6, 2.4), 2, 10, 1.5),
}


def _fourier_fig(name, uid):
    f, yr, n1, n2, mid = FOURIER[name]
    c = Canvas(W, H)
    p = Plot(c, uid, (-2.0, 2.0, yr[0], yr[1]))
    p.frame([(v, f"{v:g}".replace("-", MINUS)) for v in (-2, -1, 0, 1, 2)], nice(yr[0], yr[1]), it("x"), it("y"))
    c.add(f'<g clip-path="url(#{uid})">')
    for a, b, shift in ((-2.0, -1.0, 2.0), (-1.0, 1.0, 0.0), (1.0, 2.0, -2.0)):
        poly(c, [p.px(a + (b - a) * i / 200, f(a + (b - a) * i / 200 + shift)) for i in range(201)], "HEAD", 2.2)
    for n, col, dash in ((n1, "ACC", "6 4"), (n2, "BLUE", None)):
        s = _partial(f, n)
        poly(c, [p.px(-2 + 4 * i / 400, s(-2 + 4 * i / 400)) for i in range(401)], col, 1.6, dash)
    c.add("</g>")
    items = [("line", "HEAD", None, it("f")), ("line", "ACC", "6 4", sub("S", str(n1))), ("line", "BLUE", None, sub("S", str(n2)))]
    if mid is not None:
        for x in (-1, 1):
            dot(c, p.px(x, mid), 4, "PINK")
        items.append(("dot", "PINK", None, "midpoint"))
    legend(c, L0, 312, items)
    return c


def draw(name, spec, uid):
    if name in PORTRAITS:
        return _portrait_fig(PORTRAITS[name], uid)
    if name in STACKED:
        return _stacked_fig(STACKED[name], uid)
    if name == "ch6-e1-iv":
        return _tan_fig(uid)
    if name in FOURIER:
        return _fourier_fig(name, uid)
    raise KeyError(name)
