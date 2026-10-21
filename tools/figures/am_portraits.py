"""Phase portraits of x' = A x for the Advanced Maths problem sheets (Topic 3 part 2, Topic 4 parts 1 and 2).

Every portrait is drawn by integrating the linear system with a Runge-Kutta scheme from a family of seeds
(forwards and backwards in time), clipped to a square box, with arrowheads taken from the vector field A x.
The specification of each figure (matrix, eigenvector lines, marks) is the JSON written by
scripts/author_am_problems.py to tools/am_problems/figures.json; nothing here is hand-placed.  Pure stdlib.
"""
import math
import re

from figures.svgkit import Canvas, Registry, arrow_head, circle, line, poly, text   # noqa: F401

FOLDER = "AM-PS"
W = H = 320
CX = CY = 160.0
HALF = 140.0                     # half-width of the box in pixels (math coordinates in [-1, 1])
EPS = 1e-9


def label_markup(s):
    """'v_1' -> v with subscript 1; '(1,1)' unchanged; italic letters for plain symbols."""
    m = re.fullmatch(r"([A-Za-z\\~]+)_(\w+)", s)
    if m:
        return f'<tspan font-style="italic">{m.group(1)}</tspan><tspan baseline-shift="sub" font-size="72%">{m.group(2)}</tspan>'
    if re.fullmatch(r"[A-Za-z]", s):
        return f'<tspan font-style="italic">{s}</tspan>'
    return s


def eigenvalues(A):
    (a, b), (c, d) = A
    tr, det = a + d, a * d - b * c
    disc = tr * tr - 4 * det
    if disc >= 0:
        r = math.sqrt(disc)
        return (tr + r) / 2, (tr - r) / 2, False
    r = math.sqrt(-disc)
    return complex(tr / 2, r / 2), complex(tr / 2, -r / 2), True


def rk4(A, p, h):
    def f(q):
        return (A[0][0] * q[0] + A[0][1] * q[1], A[1][0] * q[0] + A[1][1] * q[1])
    k1 = f(p)
    k2 = f((p[0] + h / 2 * k1[0], p[1] + h / 2 * k1[1]))
    k3 = f((p[0] + h / 2 * k2[0], p[1] + h / 2 * k2[1]))
    k4 = f((p[0] + h * k3[0], p[1] + h * k3[1]))
    return (p[0] + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), p[1] + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))


def trajectory(A, seed, h, box=1.0, max_steps=7000, rmin=0.012, period=None):
    """Points of the orbit through `seed` inside |x|,|y| <= box, ordered by increasing t."""
    def run(sign):
        pts, p = [], seed
        step = sign * h
        limit = int(period / h) + 2 if period else max_steps
        for _ in range(limit):
            p = rk4(A, p, step)
            if abs(p[0]) > box or abs(p[1]) > box:
                break
            if max(abs(p[0]), abs(p[1])) < rmin:
                break
            pts.append(p)
        return pts
    back, fwd = run(-1), run(+1)
    return back[::-1] + [seed] + fwd


def to_px(p):
    return CX + HALF * p[0], CY - HALF * p[1]


def thin(points, min_dist=1.6):
    out = [points[0]]
    for q in points[1:]:
        if math.hypot(q[0] - out[-1][0], q[1] - out[-1][1]) >= min_dist:
            out.append(q)
    return out


def field_dir(A, p):
    v = (A[0][0] * p[0] + A[0][1] * p[1], A[1][0] * p[0] + A[1][1] * p[1])
    n = math.hypot(*v)
    return (v[0] / n, -v[1] / n) if n > EPS else None       # screen direction (y flips)


def head_at(c, A, p_math, col, size=7.5):
    d = field_dir(A, p_math)
    if d is None:
        return
    x, y = to_px(p_math)
    arrow_head(c, (x - d[0], y - d[1]), (x + 3.2 * d[0], y + 3.2 * d[1]), col, size)


def seeds_for(A, kind):
    """Seeds (math coordinates) according to the kind of portrait."""
    out = []
    if kind in ("node", "saddle", "improper", "star"):
        for ring, r, off in ((0, 0.85, 0.17), (1, 0.4, 0.43)):
            n = 8 if kind != "star" else 12
            for k in range(n):
                a = off + 2 * math.pi * k / n
                out.append((r * math.cos(a), r * math.sin(a)))
    elif kind == "spiral":
        for r, a in ((0.3, 0.35), (0.6, 0.35 + math.pi), (0.85, 0.35 + math.pi / 2), (0.15, 0.35 + 3 * math.pi / 2)):
            out.append((r * math.cos(a), r * math.sin(a)))
    elif kind == "centre":
        for r in (0.3, 0.55, 0.8):
            out.append((r, 0.0))
    return out


def classify(A):
    l1, l2, cx = eigenvalues(A)
    (a, b), (c, d) = A
    if cx:
        return "centre" if abs(l1.real) < 1e-9 else "spiral"
    if abs(l1 - l2) < 1e-9:
        return "star" if abs(b) < 1e-9 and abs(c) < 1e-9 else "improper"
    if abs(l1) < 1e-9 or abs(l2) < 1e-9:
        return "zero"
    return "saddle" if l1 * l2 < 0 else "node"


def eigvec(A, lam):
    (a, b), (c, d) = A
    rows = [(a - lam, b), (c, d - lam)]
    row = max(rows, key=lambda r: abs(r[0]) + abs(r[1]))     # a non-zero row p v1 + q v2 = 0 gives v = (q, -p)
    v = (row[1], -row[0])
    if math.hypot(*v) < EPS:
        v = (1.0, 0.0)
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)


def draw(spec, uid):
    A = spec["A"]
    kind = classify(A)
    l1, l2, cx = eigenvalues(A)
    rho = max(abs(l1), abs(l2), 1e-6)
    h = 0.02 / rho
    c = Canvas(W, H)
    c.add(f'<defs><clipPath id="{uid}"><rect x="{CX - HALF}" y="{CY - HALF}" width="{2 * HALF}" height="{2 * HALF}"/></clipPath></defs>')
    # axes
    line(c, (CX - HALF - 6, CY), (CX + HALF + 6, CY), "EDGE", 1.1)
    line(c, (CX, CY + HALF + 6), (CX, CY - HALF - 6), "EDGE", 1.1)
    arrow_head(c, (CX + HALF - 4, CY), (CX + HALF + 8, CY), "EDGE", 6)
    arrow_head(c, (CX, CY - HALF + 4), (CX, CY - HALF - 8), "EDGE", 6)
    ax, ay = spec.get("axes", ["x", "y"])
    text(c, (CX + HALF + 4, CY + 16), label_markup(ax), "TEXT", "end", 13)
    text(c, (CX + 8, CY - HALF - 2), label_markup(ay), "TEXT", "start", 13)
    c.add(f'<g clip-path="url(#{uid})">')
    # eigenvector lines (dashed amber) with arrows showing the flow along them
    for item in spec.get("lines", []):
        vx, vy = item[0], item[1]
        n = math.hypot(vx, vy)
        ux, uy = vx / n, vy / n
        L = 3.0
        line(c, to_px((-L * ux, -L * uy)), to_px((L * ux, L * uy)), "ACC", 1.6, "6 4")
    c.add("</g>")
    c.add(f'<g clip-path="url(#{uid})">')
    seeds = [tuple(s) for s in spec["seeds"]] if spec.get("seeds") else []
    period = 2 * math.pi / abs(l1.imag) if (cx and abs(l1.real) < 1e-9) else None
    if kind == "zero":
        # line of equilibria along the eigenvector of 0, trajectories parallel to the other eigenvector
        lam0, lam1 = (l1, l2) if abs(l1) < 1e-9 else (l2, l1)
        v0, v1 = eigvec(A, 0.0), eigvec(A, lam1)
        for s in (-0.9, -0.6, -0.3, 0.3, 0.6, 0.9):
            for sg in (1, -1):
                seeds.append((s * v0[0] + sg * 0.5 * v1[0] * 0.8, s * v0[1] + sg * 0.5 * v1[1] * 0.8))
        pts = [to_px((-3 * v0[0], -3 * v0[1])), to_px((3 * v0[0], 3 * v0[1]))]
        poly(c, pts, "GREEN", 3.0)
    elif not seeds:
        seeds = seeds_for(A, kind)
        if kind == "centre":
            # the orbits are ellipses: rescale each seed so that the whole ellipse fits in the box
            def extent(p0):
                pts = [p0]
                p = p0
                for _ in range(int(period / h) + 2):
                    p = rk4(A, p, h)
                    pts.append(p)
                return max(max(abs(q[0]), abs(q[1])) for q in pts)
            e0 = extent((0.1, 0.0))
            seeds = [(0.1 * tgt / e0, 0.0) for tgt in (0.3, 0.6, 0.9)]
    for s in seeds:
        pts = trajectory(A, s, h, period=period)
        if len(pts) < 3:
            continue
        px = thin([to_px(p) for p in pts])
        if period:
            px.append(px[0])
        poly(c, px, "BLUE", 1.5)
        n = len(px)
        if n < 4:
            continue
        for f in ((0.3, 0.7) if n > 60 else (0.5,)):
            q = px[min(n - 1, max(0, int(f * n)))]
            head_at(c, A, ((q[0] - CX) / HALF, (CY - q[1]) / HALF), "BLUE")
    # arrowheads on the eigenvector lines
    for item in spec.get("lines", []):
        vx, vy = item[0], item[1]
        n = math.hypot(vx, vy)
        ux, uy = vx / n, vy / n
        for sg in (1, -1):
            head_at(c, A, (sg * 0.55 * ux, sg * 0.55 * uy), "ACC", 8.5)
    c.add("</g>")
    # equilibrium and frame
    circle(c, (CX, CY), 3.2, "HEAD", 1.4, fill="HEAD")
    c.add(f'<rect x="{CX - HALF}" y="{CY - HALF}" width="{2 * HALF}" height="{2 * HALF}" fill="none" stroke="EDGE" stroke-width="1"/>')
    # labels of the eigenvector lines, outside the clip so that they stay readable
    for item in spec.get("lines", []):
        vx, vy = item[0], item[1]
        lab = item[2] if len(item) > 2 else ""
        if not lab:
            continue
        n = math.hypot(vx, vy)
        ux, uy = vx / n, vy / n
        e = 0.93 / max(abs(ux), abs(uy))
        for sg, suffix in ((1, ""),):
            px, py = to_px((sg * e * ux, sg * e * uy))
            dx = -6 if px > CX + 40 else 6
            anchor = "end" if px > CX + 40 else "start"
            text(c, (px, py), label_markup(lab), "ACC", anchor, 13, "600", dx, 14 if py < CY - 40 else -6)
    for m in spec.get("marks", []):
        px, py = to_px((m[0], m[1]))
        circle(c, (px, py), 2.8, "PINK", 1.2, fill="PINK")
        if len(m) > 2 and m[2]:
            text(c, (px, py), m[2], "PINK", "start", 12, "600", 6, -6)
    if spec.get("plane"):
        text(c, (CX - HALF + 4, CY - HALF + 16), spec["plane"], "TEXT", "start", 12)
    return c


# --------------------------------------------------------------------------- graphs of functions of one variable
PW, PH = 420, 260
L0, R0, T0, B0 = 52.0, 404.0, 18.0, 222.0      # plot box in pixels


def _nice_ticks(hi):
    step = 10 ** math.floor(math.log10(hi / 4.0))
    for m in (1, 2, 5, 10):
        if hi / (step * m) <= 5:
            return step * m
    return step


def _frame(c, x1, ymin, ymax, xlabel, ylabel, uid):
    def px(xv, yv):
        return L0 + (R0 - L0) * xv / x1, B0 - (B0 - T0) * (yv - ymin) / (ymax - ymin)
    c.add(f'<defs><clipPath id="{uid}"><rect x="{L0}" y="{T0}" width="{R0 - L0}" height="{B0 - T0}"/></clipPath></defs>')
    c.add(f'<rect x="{L0}" y="{T0}" width="{R0 - L0}" height="{B0 - T0}" fill="none" stroke="EDGE" stroke-width="1"/>')
    ys = px(0, 0)[1]
    if T0 < ys < B0:
        line(c, (L0, ys), (R0, ys), "EDGE", 1.0)
    ty = _nice_ticks(ymax - ymin)
    v = math.ceil(ymin / ty) * ty
    while v <= ymax + 1e-9:
        y = px(0, v)[1]
        line(c, (L0 - 4, y), (L0, y), "EDGE", 1.0)
        text(c, (L0 - 7, y + 4), f"{v:g}", "TEXT", "end", 11)
        v += ty
    tx = _nice_ticks(x1)
    v = 0.0
    while v <= x1 + 1e-9:
        x = px(v, 0)[0]
        line(c, (x, B0), (x, B0 + 4), "EDGE", 1.0)
        text(c, (x, B0 + 17), f"{v:g}", "TEXT", "middle", 11)
        v += tx
    text(c, ((L0 + R0) / 2, PH - 6), label_markup(xlabel), "TEXT", "middle", 13)
    text(c, (14, (T0 + B0) / 2), label_markup(ylabel), "TEXT", "middle", 13)
    return px


def _series_value(cv, t):
    w, al, a = cv.get("w", 1.0), cv.get("al", 0.0), cv.get("a", 1.0)
    fn = cv["fn"]
    if fn == "beats":
        return a / (w * w - al * al) * (math.cos(al * t) - math.cos(w * t))
    if fn == "beats_env":
        return 2 * a / abs(w * w - al * al) * abs(math.sin((w - al) * t / 2))
    if fn == "resonance":
        return a * t * math.sin(w * t) / (2 * w)
    if fn == "resonance_env":
        return a * t / (2 * w)
    raise ValueError(fn)


def draw_series(spec, uid):
    c = Canvas(PW, PH)
    t1, ymax = float(spec["t1"]), float(spec["ymax"])
    px = _frame(c, t1, -ymax, ymax, spec.get("xlabel", "t"), spec.get("ylabel", "x"), uid)
    c.add(f'<g clip-path="url(#{uid})">')
    n = 1500
    for cv in spec["curves"]:
        env = cv["fn"].endswith("_env")
        for sign in ((1, -1) if env else (1,)):
            pts = [px(t1 * i / n, sign * _series_value(cv, t1 * i / n)) for i in range(n + 1)]
            poly(c, pts, cv.get("col", "BLUE"), 1.1 if env else 1.6, "5 4" if env else None)
    c.add("</g>")
    return c


def draw_response(spec, uid):
    c = Canvas(PW, PH)
    ymax = float(spec.get("ymax", 5.0))
    px = _frame(c, 2.0, 0.0, ymax, "α/ω", "ω²M/a", uid)
    c.add(f'<g clip-path="url(#{uid})">')
    cols = ["BLUE", "GREEN", "ACC", "PINK"]
    n = 800

    def curve(lam):
        out = []
        for i in range(n + 1):
            x = 2.0 * i / n
            d = (1 - x * x) ** 2 + lam * lam * x * x
            out.append(px(x, 1.0 / math.sqrt(d) if d > 1e-9 else 1e9))
        return out
    poly(c, curve(0.0), "EDGE", 1.3, "5 4")
    for lam, col in zip(spec["lams"], cols):
        poly(c, curve(lam), col, 1.8)
    c.add("</g>")
    for k, (lam, col) in enumerate(zip(spec["lams"], cols)):
        y = T0 + 14 + 15 * k
        line(c, (R0 - 96, y - 4), (R0 - 76, y - 4), col, 2)
        text(c, (R0 - 70, y), f"λ/ω = {lam:g}", "TEXT", "start", 11)
    return c


def build(specs):
    """Registry of the figures listed in `specs` ({name: spec} with 'caption' and 'title')."""
    reg = Registry(FOLDER)
    for name in sorted(specs):
        spec = specs[name]
        uid = "clip-" + re.sub(r"[^A-Za-z0-9]", "-", name)
        kind = spec.get("kind", "portrait")
        canvas = {"series": draw_series, "response": draw_response}.get(kind, draw)(spec, uid)
        reg.put(name, canvas, spec.get("title", name), spec.get("caption"))
    return reg
