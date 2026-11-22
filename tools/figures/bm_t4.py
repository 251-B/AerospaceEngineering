"""Topic 4 figures for Business Management: six crops of Topic 4_ The Production Function.pdf (raster) and two
EXTRA charts drawn for the problem sheets (BEP  OL Statements.pdf)."""
from figures.svgkit import Canvas, Registry, dot, line, text

REG = Registry("BM-T4")


def _crops():
    REG.raster("production-system", "The production system",
               "A production system converts inputs (factors of production) into outputs through a transformation "
               "process, inside a generic and specific environment and with feedback. Copied from Topic 4 slides, Slide 4", 680)
    REG.raster("product-process", "The product-process matrix",
               "The five generic production systems, from project to continuous production, with an example of each; "
               "variability and flexibility grow towards the project end, volume towards the continuous end. "
               "Copied from Topic 4 slides, Slide 7", 600)
    REG.raster("flexible-rigid", "Flexible versus rigid production",
               "Total cost of a flexible and a rigid system: the rigid one has higher fixed costs and a lower variable "
               "cost per unit, so it is cheaper only beyond the crossing volume. Copied from Topic 4 slides, Slide 17", 520)
    REG.raster("gantt", "A Gantt chart",
               "A Gantt chart: one bar per activity from its scheduled start to its stop date, with the current status "
               "marked. Copied from Topic 4 slides, Slide 32", 560)
    REG.raster("bep-chart", "Break-even point",
               "Revenue and total cost TC = FC + VC against the volume Q: below the break-even volume the company has "
               "losses, above it profits. Copied from Topic 4 slides, Slide 37", 600)
    REG.raster("ol-curve", "Operating leverage and the break-even point",
               "OL = Q / (Q − Q*): above the break-even point the leverage is greater than 1 and falls towards 1 as Q "
               "grows; below it the leverage is negative. Copied from Topic 4 slides, Slide 42", 400)


# ---------------------------------------------------------------- problem sheet charts
def p2_profit():
    c = Canvas(560, 300)
    x0, y0 = 70, 270
    X = lambda q: x0 + q * 0.5  # noqa: E731   0..900 units -> 450 px
    Y = lambda b: 150 - b * 0.03  # noqa: E731   profit 0 at y = 150
    line(c, (x0, Y(0)), (X(960), Y(0)), "EDGE", 1.4, head=True)
    line(c, (x0, y0), (x0, 20), "EDGE", 1.4, head=True)
    text(c, (X(960), Y(0) - 8), "q (units)", "HEAD", "end", 12)
    text(c, (x0 + 6, 26), "Profit (€)", "HEAD", "start", 12)
    for b in (-3000, -1500, 1500):
        line(c, (x0 - 4, Y(b)), (x0, Y(b)), "EDGE", 1)
        text(c, (x0 - 8, Y(b) + 4), f"{b:,}", "TEXT", "end", 11)
    line(c, (X(0), Y(-3000)), (X(900), Y(1500)), "BLUE", 2.2)
    dot(c, (X(600), Y(0)), 4, "HEAD")
    text(c, (X(600), Y(0) - 10), "q* = 600", "HEAD", "middle", 12, "700")
    dot(c, (X(500), Y(-500)), 4, "PINK")
    text(c, (X(500) + 8, Y(-500) + 16), "q = 500, B = −500", "PINK", "start", 12)
    line(c, (X(900), Y(1500)), (X(900), Y(0)), "EDGE", 1, "4 3")
    dot(c, (X(900), Y(1500)), 4, "GREEN")
    text(c, (X(900) - 8, Y(1500) - 8), "capacity 900: B = 1,500", "GREEN", "end", 12, "700")
    # EXTRA: solution graph of Exercise 2 with computed points (the official solutions p. 3 has a plainer one)
    REG.put("p2-profit", c, "Exercise 2: profit against volume",
            "Profit B = 5q − 3,000 between 0 and the maximum capacity of 900 units: break-even at 600 units and "
            "maximum profit 1,500 € at 900 units")


def p3_profit():
    c = Canvas(580, 320)
    x0 = 70
    X = lambda q: x0 + q * 0.036  # noqa: E731   0..12,000 units -> 432 px
    Y = lambda b: 170 - b * 0.0028  # noqa: E731
    line(c, (x0, Y(0)), (X(12800), Y(0)), "EDGE", 1.4, head=True)
    line(c, (x0, 300), (x0, 20), "EDGE", 1.4, head=True)
    text(c, (X(12800), Y(0) - 8), "q (units)", "HEAD", "end", 12)
    text(c, (x0 + 6, 26), "Profit (€)", "HEAD", "start", 12)
    for b in (-40000, -20000, 20000, 40000):
        line(c, (x0 - 4, Y(b)), (x0, Y(b)), "EDGE", 1)
        text(c, (x0 - 8, Y(b) + 4), f"{b:,}", "TEXT", "end", 11)
    line(c, (X(0), Y(-40000)), (X(12000), Y(44000)), "PINK", 2.2)
    line(c, (X(0), Y(-20000)), (X(12000), Y(40000)), "BLUE", 2.2, "7 4")
    text(c, (X(12000) + 6, Y(44000) + 2), "A: 7q − 40,000", "PINK", "start", 12, "700")
    text(c, (X(12000) + 6, Y(40000) + 16), "B: 5q − 20,000", "BLUE", "start", 12, "700")
    dot(c, (X(5714), Y(0)), 4, "PINK")
    text(c, (X(5714) + 6, Y(0) + 18), "A: 5,714", "PINK", "start", 12)
    dot(c, (X(4000), Y(0)), 4, "BLUE")
    text(c, (X(4000) - 6, Y(0) - 10), "B: 4,000", "BLUE", "end", 12)
    dot(c, (X(10000), Y(30000)), 4, "HEAD")
    line(c, (X(10000), Y(30000)), (X(10000), Y(0)), "EDGE", 1, "4 3")
    text(c, (X(10000) + 8, Y(30000) + 34), "q = 10,000:", "HEAD", "start", 12, "700")
    text(c, (X(10000) + 8, Y(30000) + 50), "both 30,000 €", "HEAD", "start", 12, "700")
    # EXTRA: solution graph of Exercise 3 with both break-evens (the printed one misplaces its marker)
    REG.put("p3-profit", c, "Exercise 3: profit of processes A and B",
            "Profit of process A (7q − 40,000) and process B (5q − 20,000) at a price of 20 €: break-even points "
            "5,714 and 4,000 units; both lines give 30,000 € at the expected 10,000 units")


def build():
    _crops()
    p2_profit()
    p3_profit()
    return REG
