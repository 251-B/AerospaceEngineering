"""Topic 4 figures for Business Management: diagrams redrawn from Topic 4_ The Production Function.pdf
and the charts of the break-even and operating leverage sheet (BEP  OL Statements.pdf)."""
from figures.bm_common import arrow, box, elbow, mid
from figures.svgkit import Canvas, Registry, circle, dot, line, poly, text

REG = Registry("BM-T4")


def production_system():
    c = Canvas(640, 250)
    env = box(c, 230, 10, 180, 46, ["Environment", "generic and specific"], "GREEN", size=12, head_first=True)
    fac = box(c, 10, 95, 170, 64, ["Factors of production", "creative, basic", "and managerial"], "BLUE", size=12, head_first=True)
    tra = box(c, 230, 95, 180, 64, ["Transformation process", "tasks, flows", "and storage"], "ACC", size=12, head_first=True)
    out = box(c, 470, 106, 150, 42, "Outputs", "BLUE", weight="700", size=13)
    fb = box(c, 240, 196, 160, 40, "Feedback", "EDGE", weight="700", size=13)
    arrow(c, mid(env, "bottom"), mid(tra, "top"))
    elbow(c, [mid(env, "left"), (95, 33), mid(fac, "top")])
    arrow(c, mid(fac, "right"), mid(tra, "left"))
    arrow(c, mid(tra, "right"), mid(out, "left"))
    elbow(c, [mid(out, "bottom"), (545, 216), mid(fb, "right")])
    elbow(c, [mid(fb, "left"), (95, 216), mid(fac, "bottom")])
    REG.put("production-system", c, "The production system",
            "A production system converts inputs (factors of production) into outputs through a transformation "
            "process, inside a generic and specific environment and with feedback (Slide 4)")


def product_process():
    c = Canvas(600, 330)
    x0, y0 = 120, 270
    line(c, (x0, y0), (x0, 25), "EDGE", 1.4, head=True)
    line(c, (x0, y0), (470, y0), "EDGE", 1.4, head=True)
    text(c, (x0, 18), "Process", "HEAD", "middle", 12, "700")
    text(c, (470, y0 + 18), "Product", "HEAD", "end", 12, "700")
    rows = [("Project", "Civil engineering"), ("Craft", "Product under demand"), ("Batch", "Bakery"),
            ("Mass", "Automobiles"), ("Continuous", "Petrochemistry")]
    for k, (proc, ex) in enumerate(rows):
        y = 50 + k * 50
        x = 160 + k * 62
        text(c, (x0 - 10, y + 4), proc, "TEXT", "end", 12)
        circle(c, (x, y), 17, "ACC", 1.4, fill="ACC", opacity=0.25)
        text(c, (x + 24, y + 4), ex, "HEAD", "start", 12)
    line(c, (440, 290), (150, 290), "PINK", 1.4, head=True)
    text(c, (295, 306), "Variability grows to the left", "PINK", "middle", 12)
    line(c, (150, 316), (440, 316), "BLUE", 1.4, head=True)
    text(c, (520, 320), "Volume", "BLUE", "middle", 12)
    line(c, (560, 270), (560, 30), "GREEN", 1.4, head=True)
    text(c, (560, 20), "Flexibility", "GREEN", "middle", 12)
    REG.put("product-process", c, "The product-process matrix",
            "The five generic production systems, from project to continuous production, with an example of "
            "each; variability and flexibility grow towards the project end, volume towards the continuous end (Slides 7-8)")


def _axes(c, x0, y0, w, h, xl, yl):
    line(c, (x0, y0), (x0 + w, y0), "EDGE", 1.4, head=True)
    line(c, (x0, y0 + 10), (x0, y0 - h), "EDGE", 1.4, head=True)
    text(c, (x0 + w, y0 + 18), xl, "HEAD", "end", 12)
    text(c, (x0 + 6, y0 - h + 4), yl, "HEAD", "start", 12)


def flexible_rigid():
    c = Canvas(520, 300)
    x0, y0 = 60, 260
    _axes(c, x0, y0, 420, 240, "Volume of production", "Total cost")
    line(c, (x0, 210), (430, 60), "PINK", 2.2)      # flexible: low FC, high slope
    line(c, (x0, 150), (430, 95), "BLUE", 2.2)      # rigid: high FC, low slope
    text(c, (436, 58), "flexible", "PINK", "start", 12, "700")
    text(c, (436, 99), "rigid", "BLUE", "start", 12, "700")
    xc = x0 + (60 / (150 / 370 - 55 / 370)) * 1  # crossing of the two lines
    yc = 210 - 150 / 370 * (xc - x0)
    line(c, (xc, yc), (xc, y0), "EDGE", 1, "4 3")
    text(c, (xc, y0 + 18), "crossing volume", "TEXT", "middle", 12)
    text(c, (120, 200), "A: flexible cheaper", "HEAD", "start", 12)
    text(c, (330, 140), "B: rigid cheaper", "HEAD", "start", 12)
    REG.put("flexible-rigid", c, "Flexible versus rigid production",
            "Total cost of a flexible and a rigid system: the rigid one has higher fixed costs and a lower variable "
            "cost per unit, so it is cheaper only beyond the crossing volume (Slide 17)")


def bep_chart():
    c = Canvas(560, 320)
    x0, y0, s = 60, 280, 0.75
    _axes(c, x0, y0, 460, 260, "Q", "€")
    # FC = 100, VC per unit = 0.5, P = 1.5 (illustrative); Q0 = FC / (P - VC) = 100
    X = lambda q: x0 + q * 1.6  # noqa: E731
    Y = lambda v: y0 - v * s  # noqa: E731
    line(c, (X(0), Y(100)), (X(260), Y(100)), "BLUE", 2)
    line(c, (X(0), Y(0)), (X(260), Y(130)), "GREEN", 2)
    line(c, (X(0), Y(100)), (X(260), Y(230)), "ACC", 2)
    line(c, (X(0), Y(0)), (X(220), Y(330)), "PINK", 2.2)
    text(c, (X(262), Y(100) + 4), "FC", "BLUE", "start", 12, "700")
    text(c, (X(262), Y(130) + 4), "VC", "GREEN", "start", 12, "700")
    text(c, (X(262), Y(230) + 4), "TC = FC + VC", "ACC", "start", 12, "700")
    text(c, (X(222), Y(330)), "R = P · Q", "PINK", "start", 12, "700")
    dot(c, (X(100), Y(150)), 4, "HEAD")
    line(c, (X(100), Y(150)), (X(100), y0), "EDGE", 1, "4 3")
    text(c, (X(100), y0 + 18), "Q0", "HEAD", "middle", 12, "700")
    text(c, (X(40), Y(110)), "losses", "TEXT", "middle", 12)
    text(c, (X(185), Y(250)), "profits", "TEXT", "middle", 12)
    REG.put("bep-chart", c, "Break-even point",
            "Revenue R and total cost TC = FC + VC against the volume Q: below Q0 the company has losses, above Q0 "
            "profits; Q0 = FC / (P − VC) = FC / m (Slide 37). Values only illustrative")


def ol_curve():
    c = Canvas(560, 320)
    x0, yz = 60, 200
    line(c, (x0, yz), (520, yz), "EDGE", 1.4, head=True)
    line(c, (x0, 300), (x0, 20), "EDGE", 1.4, head=True)
    text(c, (520, yz + 18), "Q", "HEAD", "end", 12)
    text(c, (x0 + 6, 26), "OL", "HEAD", "start", 12)
    qs, k, sy = 100, 1.8, 30   # Q* = 100 units, 1.8 px per unit, 30 px per unit of OL
    X = lambda q: x0 + q * k  # noqa: E731
    Y = lambda v: yz - v * sy  # noqa: E731
    right = [(X(q), Y(q / (q - qs))) for q in range(130, 251, 4)]
    left = [(X(q), Y(q / (q - qs))) for q in range(0, 76, 3)]
    poly(c, right, "BLUE", 2.2)
    poly(c, left, "PINK", 2.2)
    line(c, (X(qs), 20), (X(qs), 300), "EDGE", 1, "4 3")
    text(c, (X(qs) + 6, yz + 18), "Q* (BEP)", "HEAD", "start", 12, "700")
    line(c, (x0, Y(1)), (520, Y(1)), "EDGE", 1, "2 3")
    text(c, (x0 - 8, Y(1) + 4), "1", "TEXT", "end", 12)
    text(c, (x0 - 8, yz + 4), "0", "TEXT", "end", 12)
    text(c, (390, 120), "profits: OL > 1", "BLUE", "middle", 12, "700")
    text(c, (150, 285), "losses: OL < 0", "PINK", "middle", 12, "700")
    REG.put("ol-curve", c, "Operating leverage and the break-even point",
            "OL = Q / (Q − Q*): above the break-even point the leverage is greater than 1 and falls towards 1 as Q "
            "grows; below it the leverage is negative (Slide 42). Q* = 100 units only as an illustration")


def gantt():
    c = Canvas(560, 220)
    x0, y0 = 70, 190
    _axes(c, x0, y0, 470, 175, "Time", "")
    bars = [("A", 0, 2), ("B", 1.5, 4.5), ("C", 0, 3.5), ("D", 4.5, 7), ("E", 7, 9)]
    for k, (lab, a, b) in enumerate(bars):
        y = 30 + k * 30
        text(c, (x0 - 10, y + 14), lab, "HEAD", "end", 12, "700")
        c.add(f'<rect x="{x0 + 10 + a * 45:g}" y="{y + 3}" width="{(b - a) * 45:g}" height="16" rx="2" '
              f'fill="BLUE" fill-opacity="0.25" stroke="BLUE" stroke-width="1.3"/>')
    line(c, (x0 + 10 + 5.5 * 45, 22), (x0 + 10 + 5.5 * 45, y0), "PINK", 1.4, "5 3")
    text(c, (x0 + 10 + 5.5 * 45, 16), "TODAY", "PINK", "middle", 12, "700")
    REG.put("gantt", c, "A Gantt chart",
            "A Gantt chart: one bar per activity from its scheduled start to its stop date; a vertical TODAY line "
            "shows the current status (Slides 30-31). Activities and dates only illustrative")


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
    REG.put("p3-profit", c, "Exercise 3: profit of processes A and B",
            "Profit of process A (7q − 40,000) and process B (5q − 20,000) at a price of 20 €: break-even points "
            "5,714 and 4,000 units; both lines give 30,000 € at the expected 10,000 units")


def build():
    for fn in (production_system, product_process, flexible_rigid, gantt, bep_chart, ol_curve, p2_profit, p3_profit):
        fn()
    return REG
