"""Figures of the Business Management Midterm 2 bank (vault/05 - Business Management/Problem Bank/).

The `npv-irr-fisher` problems carry a schematic graph of NPV(r) for their projects, drawn here from the cash flows of the
statement (EXTRA figures: the course PDFs draw no such graph for these data; the example exam asks the student to draw
one). Each figure marks the IRR of every project (where its curve crosses the axis) and the Fisher rates (where two
curves cross), so the decision intervals of the solution can be read on it. Vault copies go to
vault/attachments/BM-MT2/<name>.svg; the web copies use the portal's CSS variables. `python tools/build_problem_bank.py`
writes them.
"""
import math

from figures.svgkit import Canvas, Registry, dot, line, poly, text

REG = Registry("BM-MT2")

# name -> (title, {project: (initial outlay, [cash flow year 1, year 2, ...])}, highest rate shown in %)
PROFILES = {
    # Bank M01, Aldebaran Space Systems: outlays and cash flows in euros, from the statement and part (b).
    "m01-npv-profile": (
        "NPV of projects A, B and C of Aldebaran Space Systems as a function of the discount rate r, with the IRR of each "
        "project and the Fisher rates of the three pairs (schematic, drawn from the cash flows of the statement)",
        {"A": (500_000, [300_000, 300_000]), "B": (750_000, [200_000, 700_000]), "C": (200_000, [100_000, 150_000])},
        20),
    # Bank M06, Corvus Flight Simulators: projects A, B and C (D is rejected at 8% and left out of the graph).
    "m06-npv-profile": (
        "NPV of projects A, B and C of Corvus Flight Simulators as a function of the discount rate r, with the IRR of each "
        "project and the Fisher rates of the pairs that cross (schematic, drawn from the cash flows of the statement)",
        {"A": (400_000, [380_000, 100_000]), "B": (600_000, [90_000, 680_000]), "C": (300_000, [60_000, 300_000])},
        25),
    # Bank M07, Boreal Hydrogen Aviation: outlays and cash flows in euros, B with the year-2 flow of part (b).
    "m07-npv-profile": (
        "NPV of projects A, B and C of Boreal Hydrogen Aviation as a function of the discount rate r, with the IRR of each "
        "project and the Fisher rates of the three pairs (schematic, drawn from the cash flows of the statement)",
        {"A": (600_000, [400_000, 280_000]), "B": (800_000, [300_000, 610_000]), "C": (400_000, [360_000, 110_000])},
        18),
}

COLOURS = ("BLUE", "PINK", "GREEN", "ACC")


def npv(outlay, flows, r):
    return -outlay + sum(q / (1 + r) ** t for t, q in enumerate(flows, 1))


def _root(fn, lo, hi):
    """Bisection on [lo, hi] for a sign change of fn; None when there is none."""
    flo, fhi = fn(lo), fn(hi)
    if flo == 0:
        return lo
    if flo * fhi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = fn(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def npv_profile(projects, rmax):
    """Canvas with the NPV(r) curves of `projects` for r in [0, rmax] (rmax in %)."""
    W, H, L, R, T, B = 660, 430, 78, 600, 70, 330
    rs = [rmax / 100 * i / 200 for i in range(201)]
    values = [npv(o, f, r) for o, f in projects.values() for r in rs]
    top, bottom = max(values), min(min(values), 0)
    span = top - bottom or 1
    top += 0.08 * span
    bottom -= 0.10 * span

    def px(r):
        return L + (R - L) * r / (rmax / 100)

    def py(v):
        return T + (B - T) * (top - v) / (top - bottom)

    c = Canvas(W, H)
    y0 = py(0)
    line(c, (L, T - 6), (L, B + 4), "EDGE", 1.2, head=False)
    line(c, (L, y0), (R + 12, y0), "EDGE", 1.2, head=True)
    text(c, (L - 8, T - 12), "NPV", "TEXT", anchor="end", size=12)
    # rate marks on the axis, their numbers along the bottom edge of the plot, clear of the curves
    line(c, (L, B + 4), (R, B + 4), "EDGE", 0.8)
    step = 5 if rmax <= 30 else 10
    for k in range(0, int(rmax) + 1, step):
        x = px(k / 100)
        line(c, (x, y0 - 3), (x, y0 + 3), "EDGE", 1)
        line(c, (x, B + 4), (x, B + 8), "EDGE", 1)
        text(c, (x, B + 20), str(k), "TEXT", anchor="middle", size=11)
    text(c, (R, B + 34), "discount rate r (%)", "TEXT", anchor="end", size=12)
    for v in _nice_ticks(bottom, top):
        y = py(v)
        line(c, (L - 3, y), (L + 3, y), "EDGE", 1)
        text(c, (L - 6, y + 4), f"{v:,.0f}", "TEXT", anchor="end", size=11)
    names = list(projects)
    irr_txt, fisher_txt = [], []
    for i, name in enumerate(names):
        o, f = projects[name]
        col = COLOURS[i % len(COLOURS)]
        poly(c, [(px(r), py(npv(o, f, r))) for r in rs], col, 2.2)
        # the name of each project at the right end of its curve, where the curves are furthest apart
        text(c, (R + 22, py(npv(o, f, rs[-1])) + 5), name, col, size=13, weight="700")
        irr = _root(lambda r: npv(o, f, r), 0.0, rmax / 100)
        if irr is not None:
            dot(c, (px(irr), y0), 4, col)
            irr_txt.append(f"{name} {100 * irr:.2f}%")
    fishers = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            (oa, fa), (ob, fb) = projects[names[i]], projects[names[j]]
            fr = _root(lambda r: npv(oa, fa, r) - npv(ob, fb, r), 1e-9, rmax / 100)
            if fr is not None and fr > 1e-6:
                fishers.append((fr, f"{names[i]}–{names[j]}", npv(oa, fa, fr)))
    # a short tag per crossing, raised in steps so that close crossings do not overlap, with a leader line
    for k, (fr, pair, v) in enumerate(sorted(fishers)):
        p = (px(fr), py(v))
        dot(c, p, 4, "HEAD", fill="none")
        line(c, (p[0], p[1] + 5), (p[0], y0 - 2), "EDGE", 1, dash="3 3")
        ty = min(p[1], py(top * 0.9)) - 22 - 18 * k
        line(c, (p[0], p[1] - 5), (p[0], ty + 4), "EDGE", 0.8)
        text(c, (p[0], ty), pair, "HEAD", anchor="middle", size=11, weight="700")
        fisher_txt.append(f"{pair} {100 * fr:.2f}%")
    text(c, (L, B + 56), "IRR (curve meets the axis): " + " · ".join(irr_txt), "TEXT", size=12)
    text(c, (L, B + 74), "Fisher rates (two curves cross): " + " · ".join(fisher_txt), "TEXT", size=12)
    return c


def _nice_ticks(lo, hi):
    span = hi - lo
    raw = span / 5
    mag = 10 ** math.floor(math.log10(raw))
    step = min((s * mag for s in (1, 2, 2.5, 5, 10) if s * mag >= raw), default=raw)
    first = math.ceil(lo / step) * step
    out, v = [], first
    while v <= hi:
        out.append(round(v, 6))
        v += step
    return out


def build():
    """Register every NPV profile in REG (idempotent) and return REG."""
    for name, (title, projects, rmax) in PROFILES.items():
        REG.put(name, npv_profile(projects, rmax), title, title)
    return REG
