"""Topic 5 figures for Business Management: diagrams redrawn from Topic 5_ Marketing _ Sales Management (I+II).pdf
and topic 5.2.2.pdf, and the demand curve of the price elasticity sheet (Elasticity exercises STATEMENTS.pdf)."""
import math

from figures.bm_common import arrow, box, elbow, mid
from figures.svgkit import Canvas, Registry, dot, line, poly, text

REG = Registry("BM-T5")


def evolution():
    c = Canvas(660, 250)
    stages = [("Passive marketing", ["production era", "seller's market", "mass production"], "EDGE"),
              ("Organizational marketing", ["sales era", "buyer's market", "consumerism"], "BLUE"),
              ("Active marketing", ["marketing era", "customer orientation", "segmentation arises"], "GREEN"),
              ("Social marketing", ["needs of the target", "market and a better", "welfare state"], "ACC")]
    prev = None
    for k, (head, lines, col) in enumerate(stages):
        b = box(c, 10 + k * 162, 170 - k * 50, 150, 76, [head] + lines, col, size=11, head_first=True)
        if prev:
            elbow(c, [mid(prev, "right"), (b[0] - 6, mid(prev, "right")[1]), (b[0] - 6, mid(b, "left")[1] + 0.01), mid(b, "left")], "EDGE", 1.3)
        prev = b
    REG.put("evolution", c, "Evolution of the marketing concept",
            "From passive marketing (production era) to organizational (sales era), active (marketing era) and social "
            "marketing (Slide 4)")


def segmentation():
    c = Canvas(660, 200)
    text(c, (95, 20), "Undifferentiated", "HEAD", "middle", 12, "700")
    m = box(c, 30, 40, 130, 32, "Marketing-mix", "BLUE", size=12)
    mk = box(c, 30, 120, 130, 40, "Whole market", "EDGE", size=12)
    arrow(c, mid(m, "bottom"), mid(mk, "top"))
    text(c, (330, 20), "Wide differentiated", "HEAD", "middle", 12, "700")
    for k in range(4):
        a = box(c, 230, 36 + k * 38, 120, 28, f"Marketing-mix {k + 1}", "BLUE", size=11)
        s = box(c, 380, 36 + k * 38, 70, 28, f"Seg. {'ABCD'[k]}", "GREEN", size=11)
        arrow(c, mid(a, "right"), mid(s, "left"), "EDGE", 1.2)
    text(c, (570, 20), "Concentrated (niche)", "HEAD", "middle", 12, "700")
    a = box(c, 490, 70, 100, 30, "Marketing-mix", "BLUE", size=11)
    s = box(c, 600, 70, 50, 30, "Seg. A", "GREEN", size=11)
    arrow(c, mid(a, "right"), mid(s, "left"), "EDGE", 1.2)
    REG.put("segmentation", c, "Market segmentation strategies",
            "Undifferentiated (one marketing mix for the whole market), wide differentiated (one mix per segment) and "
            "differentiated concentrated, or niche, marketing (one mix for one segment) (Slide 12)")


def _axes(c, x0, y0, w, h, xl, yl):
    line(c, (x0, y0), (x0 + w, y0), "EDGE", 1.4, head=True)
    line(c, (x0, y0), (x0, y0 - h), "EDGE", 1.4, head=True)
    text(c, (x0 + w, y0 + 18), xl, "HEAD", "end", 12)
    text(c, (x0 + 6, y0 - h + 4), yl, "HEAD", "start", 12)


def plc():
    c = Canvas(580, 280)
    x0, y0 = 50, 240
    _axes(c, x0, y0, 510, 220, "Time", "Sales")
    pts = [(x0 + t * 4.6, y0 - 170 * math.exp(-((t - 60) / 26) ** 2) - 10) for t in range(0, 108)]
    poly(c, pts, "PINK", 2.4)
    for xb, lab in [(140, "Introduction"), (230, "Growth"), (360, "Maturity"), (500, "Decline")]:
        text(c, ((xb + {140: x0, 230: 140, 360: 230, 500: 360}[xb]) / 2, y0 + 18), lab, "TEXT", "middle", 12)
        if xb < 500:
            line(c, (xb, y0), (xb, 30), "EDGE", 1, "4 3")
    REG.put("plc", c, "The product life-cycle",
            "Sales of a product over time through the introduction, growth, maturity and decline stages (Slide 25)")


def plc_examples():
    c = Canvas(600, 200)
    shapes = {"A": lambda t: 120 * (1 - math.exp(-t / 22)),
              "B": lambda t: 120 * math.sin(math.pi * t / 100),
              "C": lambda t: 75 * math.sin(math.pi * t / 45) if t <= 45 else 0}
    for k, (lab, f) in enumerate(shapes.items()):
        x0, y0 = 30 + k * 195, 160
        _axes(c, x0, y0, 165, 140, "", "Sales" if k == 0 else "")
        poly(c, [(x0 + t * 1.5, y0 - f(t)) for t in range(0, 101)], "GREEN", 2.2)
        text(c, (x0 + 80, y0 + 26), lab, "PINK", "middle", 14, "700")
    REG.put("plc-examples", c, "Three product life-cycles",
            "The three sales curves of Slide 26: A keeps its sales (a product of a dilated life), B rises and falls "
            "(a fashion product) and C falls almost at once (an immediate failure); the slide leaves the matching as a question")


def pricing():
    c = Canvas(600, 200)
    t = box(c, 220, 10, 160, 36, "Approaches to pricing", "HEAD", weight="700", size=12)
    a = [box(c, 10 + k * 200, 80, 180, 36, s, "BLUE", size=12, rx=18)
         for k, s in enumerate(["Competition approach", "Demand approach", "Cost approach"])]
    for b in a:
        elbow(c, [mid(t, "bottom"), (mid(t, "bottom")[0], 63), (mid(b, "top")[0], 63), mid(b, "top")], "EDGE", 1.2)
    p1 = box(c, 330, 150, 130, 40, ["Cost-plus pricing", "(mark-up)"], "GREEN", size=11)
    p2 = box(c, 470, 150, 120, 40, ["Break-even", "analysis"], "GREEN", size=11)
    for p in (p1, p2):
        elbow(c, [mid(a[2], "bottom"), (mid(a[2], "bottom")[0], 135), (mid(p, "top")[0], 135), mid(p, "top")], "EDGE", 1.2)
    REG.put("pricing", c, "Approaches to pricing",
            "Competition, demand and cost approaches to pricing; the cost approach uses cost-plus pricing (a mark-up "
            "on the cost) or break-even analysis (Slide 28)")


def elasticity_limits():
    c = Canvas(560, 250)
    x0, y0 = 60, 220
    _axes(c, x0, y0, 470, 200, "Quantity", "Price")
    line(c, (x0 + 10, 110), (x0 + 440, 110), "BLUE", 2.4)
    line(c, (x0 + 260, 30), (x0 + 260, y0), "PINK", 2.4)
    text(c, (x0 + 20, 102), "perfectly elastic demand: Ed = ∞", "BLUE", "start", 12, "700")
    text(c, (x0 + 268, 44), "perfectly inelastic demand: Ed = 0", "PINK", "start", 12, "700")
    REG.put("elasticity-limits", c, "The two limiting demand curves",
            "A horizontal demand curve is perfectly elastic (Ed = ∞) and a vertical one perfectly inelastic (Ed = 0) "
            "(topic 5.2.2.pdf, p. 4)")


def p1_demand():
    c = Canvas(560, 300)
    x0, y0 = 70, 260
    X = lambda q: x0 + q * 4.2  # noqa: E731
    Y = lambda p: y0 - p * 9  # noqa: E731
    _axes(c, x0, y0, 470, 252, "Quantity Q", "Price P (€)")
    pts = [(25, 0, "A"), (20, 20, "B"), (15, 40, "C"), (10, 60, "D"), (5, 80, "E"), (0, 100, "F")]
    poly(c, [(X(q), Y(p)) for p, q, _ in pts], "BLUE", 2.4)
    for p, q, lab in pts:
        dot(c, (X(q), Y(p)), 4, "HEAD")
        if lab == "F":
            text(c, (X(q) - 4, Y(p) - 14), f"{lab} ({q}, {p})", "HEAD", "end", 12, "700")
        else:
            text(c, (X(q) + 10, Y(p) - 8), f"{lab} ({q}, {p})", "HEAD", "start", 12, "700")
    for v in (0, 20, 40, 60, 80, 100):
        text(c, (X(v), y0 + 16), str(v), "TEXT", "middle", 11)
    for v in (5, 10, 15, 20, 25):
        text(c, (x0 - 8, Y(v) + 4), str(v), "TEXT", "end", 11)
    text(c, (X(34), Y(22)), "elastic: |Ed| > 1", "PINK", "start", 12)
    text(c, (X(72), Y(2)), "inelastic: |Ed| < 1", "GREEN", "middle", 12)
    dot(c, (X(50), Y(12.5)), 5, "ACC")
    text(c, (X(50) - 10, Y(12.5) + 22), "|Ed| = 1 at (50, 12.5)", "ACC", "end", 12, "700")
    REG.put("p1-demand", c, "Exercise 1: demand curve of product X",
            "The six points of the table on the straight demand line P = 25 − Q/4; the demand is elastic on the upper "
            "half, unit elastic at its midpoint and inelastic on the lower half")


def build():
    for fn in (evolution, segmentation, plc, plc_examples, pricing, elasticity_limits, p1_demand):
        fn()
    return REG
