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


# --------------------------------------------------------------------------- nonlinear portraits, Fourier & transcendental plots
def _nl_field(name):
    """Named 2D nonlinear vector fields (f(x, y), g(x, y)) for Chapter 5."""
    fields = {
        "ch5_e1": lambda x, y: (-y - x * (x * x + y * y), x - y * (x * x + y * y)),
        "ch5_e2_i": lambda x, y: (x * (2 - x - y), y * (2 - 2 * y - 2 * x)),
        "ch5_e2_ii": lambda x, y: (x * (2 - x - y), y * (2 - 2 * y - x / 4.0)),
        "ch5_e2_iii": lambda x, y: (x * (2 - x - 3 * y), y * (2 - 2 * y - 3 * x)),
        "ch5_e2_iv": lambda x, y: (x * (1 - 2 * y), y * (-2 + 3 * x)),
        "ch5_e2_v": lambda x, y: (x * (4 - x / 2.0 - 3 * y), y * (-2 + x)),
        "ch5_e2_vi": lambda x, y: (x * (10 - x - 3 * y), y * (1 + x - 10 * y)),
        "ch5_e2_vii": lambda x, y: (x * (3 - x - y), y * (-2 + x)),
        "ch5_e3_i": lambda x, y: (x * (1 - x + y), y * (1 + x - 2 * y)),
        "ch5_e3_ii": lambda x, y: (x * (2 - x + y), y * (4 + 2 * x - y)),
        "ch5_e4_i": lambda x, y: (y, -x),
        "ch5_e4_ii": lambda x, y: (y, -2 * x**3 + 2 * x),
        "ch5_e4_iii": lambda x, y: (y, -(3 * x**5 - 5 * x**3 + 4 * x)),
        "ch5_e5_ii": lambda x, y: (y, -((2 * x**3 - 2 * x) * (1 + (6 * x**2 - 2) * y**2)) / (1 + (2 * x**3 - 2 * x)**2)),
        "ch5_e6_i": lambda x, y: (y, -x - y),
        "ch5_e6_ii": lambda x, y: (y, -2 * x**3 + 2 * x - y),
        "ch5_e6_iii": lambda x, y: (y, -(3 * x**5 - 5 * x**3 + 4 * x) - y),
        "ch5_e8": lambda x, y: (y, -math.sin(x)),
        "ch5_e9": lambda x, y: (y, -math.sin(x) - 0.5 * y),
        "ch5_e10": lambda x, y: (y, -math.sin(x) - 0.4 * y * abs(y)),
    }
    return fields[name]


def _rk4_nl(fn, p, h):
    k1 = fn(p[0], p[1])
    k2 = fn(p[0] + 0.5 * h * k1[0], p[1] + 0.5 * h * k1[1])
    k3 = fn(p[0] + 0.5 * h * k2[0], p[1] + 0.5 * h * k2[1])
    k4 = fn(p[0] + h * k3[0], p[1] + h * k3[1])
    return (p[0] + h / 6.0 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
            p[1] + h / 6.0 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))


def _trace_nl(fn, seed, bounds, h=0.015, max_steps=1600, both=True):
    xmin, xmax, ymin, ymax = bounds
    margin_x = 0.08 * (xmax - xmin)
    margin_y = 0.08 * (ymax - ymin)
    tol = 1e-4 * max(xmax - xmin, ymax - ymin)

    def run(sign):
        pts, p = [], seed
        for _ in range(max_steps):
            v = fn(p[0], p[1])
            spd = math.hypot(v[0], v[1])
            if spd < 1e-6 or spd > 1e5:
                break
            # normalize step in phase space for smooth, uniform curves
            dt = sign * min(h, 0.015 * max(xmax - xmin, ymax - ymin) / max(spd, 1e-6))
            q = _rk4_nl(fn, p, dt)
            if not (xmin - margin_x <= q[0] <= xmax + margin_x and ymin - margin_y <= q[1] <= ymax + margin_y):
                pts.append(q)
                break
            if math.hypot(q[0] - p[0], q[1] - p[1]) < tol * 0.05:
                break
            pts.append(q)
            p = q
            if len(pts) > 25 and math.hypot(p[0] - seed[0], p[1] - seed[1]) < tol * 18:
                break
        return pts

    fwd = run(+1)
    if not both:
        return [seed] + fwd
    back = run(-1)
    return back[::-1] + [seed] + fwd


def draw_nonlinear(spec, uid):
    """Nonlinear 2D phase portrait with RK4 orbits, nullclines, separatrices and critical points."""
    w, h_px = int(spec.get("w", 400)), int(spec.get("h", 300))
    L, R, T, B = 48.0, w - 18.0, 20.0, h_px - 36.0
    xmin, xmax, ymin, ymax = [float(v) for v in spec["bounds"]]

    def px(xv, yv):
        return L + (R - L) * (xv - xmin) / (xmax - xmin), B - (B - T) * (yv - ymin) / (ymax - ymin)

    c = Canvas(w, h_px)
    c.add(f'<defs><clipPath id="{uid}"><rect x="{L}" y="{T}" width="{R - L}" height="{B - T}"/></clipPath></defs>')

    # axes inside box
    if xmin <= 0 <= xmax:
        x0 = px(0, 0)[0]
        line(c, (x0, B), (x0, T), "EDGE", 1.1)
    if ymin <= 0 <= ymax:
        y0 = px(0, 0)[1]
        line(c, (L, y0), (R, y0), "EDGE", 1.1)

    # ticks
    tx = _nice_ticks(xmax - xmin)
    v = math.ceil(xmin / tx - 1e-9) * tx
    while v <= xmax + 1e-9:
        if abs(v) < 1e-9:
            v = 0.0
        xp = px(v, ymin)[0]
        line(c, (xp, B), (xp, B + 4), "EDGE", 1.0)
        text(c, (xp, B + 16), f"{v:g}", "TEXT", "middle", 10)
        v += tx
    ty = _nice_ticks(ymax - ymin)
    v = math.ceil(ymin / ty - 1e-9) * ty
    while v <= ymax + 1e-9:
        if abs(v) < 1e-9:
            v = 0.0
        yp = px(xmin, v)[1]
        line(c, (L - 4, yp), (L, yp), "EDGE", 1.0)
        text(c, (L - 7, yp + 3.5), f"{v:g}", "TEXT", "end", 10)
        v += ty

    ax, ay = spec.get("axes", ["x", "y"])
    text(c, ((L + R) / 2, h_px - 6), label_markup(ax), "TEXT", "middle", 12)
    text(c, (14, (T + B) / 2), label_markup(ay), "TEXT", "middle", 12)

    fn = _nl_field(spec["field"])
    c.add(f'<g clip-path="url(#{uid})">')
    # nullclines (dashed)
    for nc in spec.get("nullclines", []):
        pts = [px(p[0], p[1]) for p in nc["pts"]]
        poly(c, pts, nc.get("col", "ACC"), 1.3, "5 4")

    # trajectories
    for seed in spec.get("seeds", []):
        pts = _trace_nl(fn, tuple(seed), (xmin, xmax, ymin, ymax),
                        h=float(spec.get("dt", 0.015)),
                        max_steps=int(spec.get("max_steps", 1200)))
        if len(pts) < 3:
            continue
        ppx = thin([px(q[0], q[1]) for q in pts], 1.8)
        if len(ppx) < 3:
            continue
        poly(c, ppx, "BLUE", 1.35)
        # place 1 arrowhead near the middle of the visible segment
        vis = [i for i, q in enumerate(pts) if xmin + 0.05 * (xmax - xmin) < q[0] < xmax - 0.05 * (xmax - xmin)
               and ymin + 0.05 * (ymax - ymin) < q[1] < ymax - 0.05 * (ymax - ymin)]
        if vis:
            q = pts[vis[len(vis) // 2]]
            vv = fn(q[0], q[1])
            dx = vv[0] * (R - L) / (xmax - xmin)
            dy = -vv[1] * (B - T) / (ymax - ymin)
            nrm = math.hypot(dx, dy)
            if nrm > 1e-9:
                ux, uy = dx / nrm, dy / nrm
                qx, qy = px(q[0], q[1])
                arrow_head(c, (qx - ux, qy - uy), (qx + 3.0 * ux, qy + 3.0 * uy), "BLUE", 6.5)

    # separatrices (highlighted in PINK)
    for sep in spec.get("separatrices", []):
        pts = _trace_nl(fn, tuple(sep), (xmin, xmax, ymin, ymax),
                        h=float(spec.get("dt", 0.012)),
                        max_steps=int(spec.get("max_steps", 1600)))
        if len(pts) < 3:
            continue
        ppx = thin([px(q[0], q[1]) for q in pts], 1.6)
        poly(c, ppx, "PINK", 2.0)

    c.add("</g>")
    c.add(f'<rect x="{L}" y="{T}" width="{R - L}" height="{B - T}" fill="none" stroke="EDGE" stroke-width="1"/>')

    # critical points (drawn on top of frame so boundary equilibria stay crisp)
    for cp in spec.get("crit_pts", []):
        cx_p, cy_p = px(cp["x"], cp["y"])
        st = cp.get("kind", "stable")
        if st == "stable":
            circle(c, (cx_p, cy_p), 3.8, "GREEN", 1.5, fill="GREEN")
        elif st == "centre":
            circle(c, (cx_p, cy_p), 3.8, "BLUE", 1.6, fill="BG")
        elif st == "saddle":
            circle(c, (cx_p, cy_p), 3.8, "ACC", 1.8, fill="BG")
        else:
            circle(c, (cx_p, cy_p), 3.8, "PINK", 1.6, fill="BG")
        if cp.get("label"):
            dx = cp.get("dx", 6)
            dy = cp.get("dy", -6)
            anch = cp.get("anchor", "start")
            text(c, (cx_p + dx, cy_p + dy), cp["label"], "TEXT", anch, 10.5, "600")
    return c


def draw_fourier(spec, uid):
    """Plot periodic extension of f(x) vs its N-term Fourier partial sum S_N(x)."""
    c = Canvas(PW, PH)
    L_val = float(spec.get("L", math.pi))
    xmin, xmax = -3.0 * L_val, 3.0 * L_val
    ymin, ymax = float(spec["ymin"]), float(spec["ymax"])
    L0p, R0p, T0p, B0p = 48.0, PW - 16.0, 20.0, PH - 36.0

    def px(xv, yv):
        return L0p + (R0p - L0p) * (xv - xmin) / (xmax - xmin), B0p - (B0p - T0p) * (yv - ymin) / (ymax - ymin)

    c.add(f'<defs><clipPath id="{uid}"><rect x="{L0p}" y="{T0p}" width="{R0p - L0p}" height="{B0p - T0p}"/></clipPath></defs>')
    c.add(f'<rect x="{L0p}" y="{T0p}" width="{R0p - L0p}" height="{B0p - T0p}" fill="none" stroke="EDGE" stroke-width="1"/>')
    if ymin < 0 < ymax:
        line(c, (L0p, px(0, 0)[1]), (R0p, px(0, 0)[1]), "EDGE", 1.0)
    line(c, (px(0, 0)[0], T0p), (px(0, 0)[0], B0p), "EDGE", 1.0)

    # x ticks at multiples of L
    unit_lbl = "π" if abs(L_val - math.pi) < 1e-6 else "L"
    for m in (-3, -2, -1, 0, 1, 2, 3):
        xp = px(m * L_val, 0)[0]
        line(c, (xp, B0p), (xp, B0p + 4), "EDGE", 1.0)
        lbl = "0" if m == 0 else (unit_lbl if m == 1 else (f"-{unit_lbl}" if m == -1 else f"{m}{unit_lbl}"))
        text(c, (xp, B0p + 16), lbl, "TEXT", "middle", 10.5)
    ty = _nice_ticks(ymax - ymin)
    v = math.ceil(ymin / ty - 1e-9) * ty
    while v <= ymax + 1e-9:
        if abs(v) < 1e-9:
            v = 0.0
        yp = px(0, v)[1]
        line(c, (L0p - 4, yp), (L0p, yp), "EDGE", 1.0)
        text(c, (L0p - 7, yp + 3.5), f"{v:g}", "TEXT", "end", 10)
        v += ty
    text(c, ((L0p + R0p) / 2, PH - 6), label_markup("x"), "TEXT", "middle", 12)
    text(c, (14, (T0p + B0p) / 2), label_markup("y"), "TEXT", "middle", 12)

    fn_name = spec["fn"]
    N = int(spec.get("N", 12))

    def wrap(xv):
        return ((xv + L_val) % (2 * L_val)) - L_val

    def f_val(xv):
        u = wrap(xv)
        if fn_name == "step_pi":
            return 0.0 if u < 0 else math.pi
        if fn_name == "x2":
            return u * u
        if fn_name == "exp_x":
            return math.exp(u)
        if fn_name == "piecewise_68":
            return 1.0 if u < 0 else u + 1.0
        raise ValueError(fn_name)

    def s_val(xv):
        if fn_name == "step_pi":
            s = math.pi / 2.0
            for k in range(1, N + 1):
                if k % 2 == 1:
                    s += (2.0 / k) * math.sin(k * xv)
            return s
        if fn_name == "x2":
            s = L_val * L_val / 3.0
            for k in range(1, N + 1):
                s += (4.0 * L_val * L_val * ((-1) ** k) / ((k * math.pi) ** 2)) * math.cos(k * math.pi * xv / L_val)
            return s
        if fn_name == "exp_x":
            sh = math.sinh(L_val)
            s = sh / L_val
            for k in range(1, N + 1):
                denom = L_val * L_val + (k * math.pi) ** 2
                sg = (-1) ** k
                s += (2.0 * L_val * sg * sh / denom) * math.cos(k * math.pi * xv / L_val)
                s += (-2.0 * k * math.pi * sg * sh / denom) * math.sin(k * math.pi * xv / L_val)
            return s
        if fn_name == "piecewise_68":
            s = 1.0 + L_val / 4.0
            for k in range(1, N + 1):
                an = L_val * (((-1) ** k) - 1.0) / ((k * math.pi) ** 2)
                bn = -L_val * ((-1) ** k) / (k * math.pi)
                s += an * math.cos(k * math.pi * xv / L_val) + bn * math.sin(k * math.pi * xv / L_val)
            return s
        raise ValueError(fn_name)

    c.add(f'<g clip-path="url(#{uid})">')
    # draw periodic extension f(x) piece by piece so jumps do not draw vertical lines
    segs, cur = [], []
    steps = 900
    prev_y = None
    for i in range(steps + 1):
        xv = xmin + (xmax - xmin) * i / steps
        yv = f_val(xv)
        if prev_y is not None and abs(yv - prev_y) > 0.25 * (ymax - ymin):
            if len(cur) >= 2:
                segs.append(cur)
            cur = [px(xv, yv)]
        else:
            cur.append(px(xv, yv))
        prev_y = yv
    if len(cur) >= 2:
        segs.append(cur)
    for seg in segs:
        poly(c, seg, "BLUE", 1.8)

    # partial sum S_N(x)
    spts = [px(xmin + (xmax - xmin) * i / 900, s_val(xmin + (xmax - xmin) * i / 900)) for i in range(901)]
    poly(c, spts, "PINK", 1.4)

    # jump midpoints
    for jp in spec.get("jumps", []):
        circle(c, px(jp[0] * L_val, jp[1]), 3.5, "GREEN", 1.5, fill="GREEN")
    c.add("</g>")

    # legend (top left inside plot)
    line(c, (L0p + 8, T0p + 12), (L0p + 26, T0p + 12), "BLUE", 2.0)
    text(c, (L0p + 31, T0p + 16), "Periodic f(x)", "TEXT", "start", 10.5)
    line(c, (L0p + 115, T0p + 12), (L0p + 133, T0p + 12), "PINK", 1.8)
    text(c, (L0p + 138, T0p + 16), f"S_{N}(x)", "TEXT", "start", 10.5)
    return c


def draw_transcendental(spec, uid):
    """Graphical solution of tan(mu) = -mu/h (Robin) or tan(mu) = mu (Ex. 6.2(ii))."""
    c = Canvas(PW, PH)
    mode = spec.get("mode", "robin")
    h_val = float(spec.get("h", 1.0))
    xmax = float(spec.get("xmax", 3.5 * math.pi))
    ymax = float(spec.get("ymax", 10.0))
    L0p, R0p, T0p, B0p = 48.0, PW - 16.0, 20.0, PH - 36.0

    def px(xv, yv):
        return L0p + (R0p - L0p) * xv / xmax, B0p - (B0p - T0p) * (yv + ymax) / (2 * ymax)

    c.add(f'<defs><clipPath id="{uid}"><rect x="{L0p}" y="{T0p}" width="{R0p - L0p}" height="{B0p - T0p}"/></clipPath></defs>')
    c.add(f'<rect x="{L0p}" y="{T0p}" width="{R0p - L0p}" height="{B0p - T0p}" fill="none" stroke="EDGE" stroke-width="1"/>')
    line(c, (L0p, px(0, 0)[1]), (R0p, px(0, 0)[1]), "EDGE", 1.0)

    # x ticks at multiples of pi/2
    for k_t in range(0, int(xmax / (math.pi / 2)) + 1):
        xv = k_t * math.pi / 2
        if xv > xmax + 1e-6:
            break
        xp = px(xv, 0)[0]
        line(c, (xp, B0p), (xp, B0p + 4), "EDGE", 1.0)
        if k_t == 0:
            lbl = "0"
        elif k_t % 2 == 0:
            m_pi = k_t // 2
            lbl = "π" if m_pi == 1 else f"{m_pi}π"
        else:
            lbl = "π/2" if k_t == 1 else f"{k_t}π/2"
        text(c, (xp, B0p + 16), lbl, "TEXT", "middle", 9.5)
    for yv in (-ymax, -ymax / 2, 0, ymax / 2, ymax):
        yp = px(0, yv)[1]
        line(c, (L0p - 4, yp), (L0p, yp), "EDGE", 1.0)
        text(c, (L0p - 7, yp + 3.5), f"{yv:g}", "TEXT", "end", 10)
    text(c, ((L0p + R0p) / 2, PH - 6), "μ = √λ" if mode == "robin" else "μ = √(-λ)", "TEXT", "middle", 11.5)
    text(c, (14, (T0p + B0p) / 2), "y", "TEXT", "middle", 12)

    c.add(f'<g clip-path="url(#{uid})">')
    # asymptotes and tan(mu) branches
    k_br = 0
    while (k_br - 0.5) * math.pi < xmax:
        a = max(0.0, (k_br - 0.5) * math.pi + 0.04)
        b = min(xmax, (k_br + 0.5) * math.pi - 0.04)
        if (k_br + 0.5) * math.pi < xmax:
            xa = px((k_br + 0.5) * math.pi, 0)[0]
            line(c, (xa, T0p), (xa, B0p), "EDGE", 1.0, "4 4")
        if b > a:
            pts = [px(a + (b - a) * i / 120, math.tan(a + (b - a) * i / 120)) for i in range(121)]
            poly(c, pts, "BLUE", 1.7)
        k_br += 1

    # line y = -mu/h or y = mu
    if mode == "robin":
        poly(c, [px(0, 0), px(xmax, -xmax / h_val)], "PINK", 1.8)
        roots = []
        for idx in (1, 2, 3):
            lo, hi = (idx - 0.5) * math.pi + 1e-5, idx * math.pi - 1e-5
            if lo < xmax:
                for _ in range(60):
                    mid = 0.5 * (lo + hi)
                    if math.tan(mid) + mid / h_val < 0:
                        lo = mid
                    else:
                        hi = mid
                roots.append((idx, 0.5 * (lo + hi), -0.5 * (lo + hi) / h_val))
    else:
        poly(c, [px(0, 0), px(xmax, xmax)], "PINK", 1.8)
        roots = []
        for idx in (1, 2, 3):
            lo, hi = idx * math.pi + 1e-5, (idx + 0.5) * math.pi - 1e-5
            if hi < xmax:
                for _ in range(60):
                    mid = 0.5 * (lo + hi)
                    if math.tan(mid) - mid < 0:
                        lo = mid
                    else:
                        hi = mid
                roots.append((idx, 0.5 * (lo + hi), 0.5 * (lo + hi)))

    for idx, rx, ry in roots:
        if -ymax <= ry <= ymax:
            qx, qy = px(rx, ry)
            circle(c, (qx, qy), 3.8, "GREEN", 1.5, fill="GREEN")
            text(c, (qx + 6, qy - 6 if mode == "robin" else qy + 13), f"μ{idx}≈{rx:.2f}", "TEXT", "start", 10, "600")
    c.add("</g>")

    line(c, (L0p + 8, T0p + 12), (L0p + 26, T0p + 12), "BLUE", 2.0)
    text(c, (L0p + 31, T0p + 16), "y = tan μ", "TEXT", "start", 10.5)
    line(c, (L0p + 98, T0p + 12), (L0p + 116, T0p + 12), "PINK", 2.0)
    text(c, (L0p + 121, T0p + 16), f"y = -μ/{h_val:g}" if mode == "robin" else "y = μ", "TEXT", "start", 10.5)
    return c


def build(specs):
    """Registry of the figures listed in `specs` ({name: spec} with 'caption' and 'title')."""
    reg = Registry(FOLDER)
    renderers = {
        "series": draw_series,
        "response": draw_response,
        "nonlinear": draw_nonlinear,
        "fourier": draw_fourier,
        "transcendental": draw_transcendental,
    }
    for name in sorted(specs):
        spec = specs[name]
        uid = "clip-" + re.sub(r"[^A-Za-z0-9]", "-", name)
        kind = spec.get("kind", "portrait")
        canvas = renderers.get(kind, draw)(spec, uid)
        # EXTRA: computed answer to "sketch the phase portrait" / Fourier / transcendental plot; official sheets print no figure
        reg.put(name, canvas, spec.get("title", name), spec.get("caption"))
    return reg
