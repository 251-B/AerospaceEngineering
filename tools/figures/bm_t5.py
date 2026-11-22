"""Topic 5 figures for Business Management: six crops of the Topic 5 slides (raster) and one EXTRA chart drawn for
the price elasticity sheet (Elasticity exercises STATEMENTS.pdf, PED Exercises SOL.pdf)."""
from figures.svgkit import Canvas, Registry, dot, line, poly, text

REG = Registry("BM-T5")


def _crops():
    REG.raster("evolution", "Evolution of the marketing concept",
               "The four stages of the marketing concept, from passive marketing (production era) through organizational "
               "(sales era) and active (marketing era) to social marketing, drawn as a rising path. "
               "Copied from Topic 5 slides, Slide 4", 680)
    REG.raster("segmentation", "Market segmentation strategies",
               "Undifferentiated marketing (one marketing mix for the whole market), wide differentiated marketing (one "
               "mix per segment) and differentiated concentrated marketing (one mix for one segment). "
               "Copied from Topic 5 slides, Slide 12", 680)
    REG.raster("plc", "The product life-cycle",
               "Sales of a product over time through the introduction, growth, maturity and decline stages, with the "
               "four stages listed beside the curve. Copied from Topic 5 slides, Slide 25", 640)
    REG.raster("plc-examples", "Three product life-cycles",
               "Three sales curves against time, A, B and C; the slide asks which is a fashion product, which an "
               "immediate failure and which a product of a dilated life. Copied from Topic 5 slides, Slide 26", 640)
    REG.raster("elasticity-limits", "The two limiting demand curves",
               "Price against quantity: a horizontal demand curve D is perfectly elastic and a vertical one D' is "
               "perfectly inelastic. Copied from topic 5.2.2.pdf, p. 4", 400)
    REG.raster("pricing", "Approaches to pricing",
               "The competition, demand and cost approaches to pricing; the cost approach branches into cost-plus "
               "pricing (mark-up) and break-even analysis. Copied from Topic 5 slides, Slide 28", 600)


def _axes(c, x0, y0, w, h, xl, yl):
    line(c, (x0, y0), (x0 + w, y0), "EDGE", 1.4, head=True)
    line(c, (x0, y0), (x0, y0 - h), "EDGE", 1.4, head=True)
    text(c, (x0 + w, y0 + 18), xl, "HEAD", "end", 12)
    text(c, (x0 + 6, y0 - h + 4), yl, "HEAD", "start", 12)


def p1_demand():
    c = Canvas(590, 305)
    x0, y0 = 70, 260
    X = lambda q: x0 + q * 4.2  # noqa: E731
    Y = lambda p: y0 - p * 9  # noqa: E731
    _axes(c, x0, y0, 470, 252, "", "Price P (€)")
    text(c, (X(50), y0 + 34), "Quantity Q", "HEAD", "middle", 12)
    pts = [(25, 0, "A"), (20, 20, "B"), (15, 40, "C"), (10, 60, "D"), (5, 80, "E"), (0, 100, "F")]
    poly(c, [(X(q), Y(p)) for p, q, _ in pts], "BLUE", 2.4)
    for p, q, lab in pts:
        dot(c, (X(q), Y(p)), 4, "HEAD")
        text(c, (X(q) + 10, Y(p) - 8), f"{lab} ({q}, {p})", "HEAD", "start", 12, "700")
    for v in (0, 20, 40, 60, 80, 100):
        text(c, (X(v), y0 + 16), str(v), "TEXT", "middle", 11)
    for v in (5, 10, 15, 20, 25):
        text(c, (x0 - 8, Y(v) + 4), str(v), "TEXT", "end", 11)
    text(c, (X(46), Y(21)), "elastic: |Ed| > 1", "PINK", "start", 12)
    text(c, (X(72), Y(2)), "inelastic: |Ed| < 1", "GREEN", "middle", 12)
    dot(c, (X(50), Y(12.5)), 5, "ACC")
    text(c, (X(50) - 10, Y(12.5) + 22), "|Ed| = 1 at (50, 12.5)", "ACC", "end", 12, "700")
    # EXTRA: solution graph with the |Ed| = 1 point, which the printed solution does not show
    REG.put("p1-demand", c, "Exercise 1: demand curve of product X",
            "The six points of the table on the straight demand line P = 25 − Q/4; the demand is elastic on the upper "
            "half, unit elastic at its midpoint and inelastic on the lower half")


def build():
    _crops()
    p1_demand()
    return REG
