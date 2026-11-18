"""Topic 7 figures for Business Management: diagrams redrawn from Topic 7_Entrepreneurship  Innovation.pdf."""
import math

from figures.svgkit import Canvas, Registry, circle, line, poly, text

REG = Registry("BM-T7")


def network():
    c = Canvas(560, 310)
    names = ["Firms", "Universities", "Government-funded research", "Private nonprofits", "Individuals"]
    pts = [(280 + 115 * math.sin(2 * math.pi * k / 5), 150 - 115 * math.cos(2 * math.pi * k / 5)) for k in range(5)]
    for i in range(5):
        for j in range(i + 1, 5):
            line(c, pts[i], pts[j], "EDGE", 1.2)
    for (x, y), n in zip(pts, names):
        circle(c, (x, y), 9, "BLUE", 1.4, fill="BLUE", opacity=0.4)
        dx, dy = x - 280, y - 150
        anchor = "middle" if abs(dx) < 20 else ("start" if dx > 0 else "end")
        tx = x + (16 if dx > 20 else -16 if dx < -20 else 0)
        ty = y + (-16 if dy < -60 else 26 if dy > 60 else 4)
        text(c, (tx, ty), n, "HEAD", anchor, 12, "700")
    REG.put("network", c, "Sources of innovation as a system",
            "Firms, universities, government-funded research, private nonprofits and individuals; the linkages between "
            "them are the most important source of innovation (Slide 4)")


def _axes(c, x0, y0, w, h, xl, yl):
    line(c, (x0, y0), (x0 + w, y0), "EDGE", 1.4, head=True)
    line(c, (x0, y0), (x0, y0 - h), "EDGE", 1.4, head=True)
    text(c, (x0 + w, y0 + 18), xl, "HEAD", "end", 12)
    text(c, (x0 + 6, y0 - h + 4), yl, "HEAD", "start", 12)


def _s(t, mid, k):
    return 1 / (1 + math.exp(-(t - mid) / k))


def s_curve():
    c = Canvas(520, 270)
    x0, y0 = 50, 235
    _axes(c, x0, y0, 440, 215, "Effort", "Performance")
    poly(c, [(x0 + t * 4, y0 - 170 * _s(t, 50, 9)) for t in range(0, 106)], "BLUE", 2.4)
    line(c, (x0, y0 - 175), (x0 + 430, y0 - 175), "PINK", 1.2, "5 4")
    text(c, (x0 + 425, y0 - 182), "limit of technology", "PINK", "end", 12, "700")
    REG.put("s-curve", c, "The S-curve of technology performance",
            "Performance grows slowly at first, then quickly, and flattens as it approaches the limit of the technology "
            "(Slide 14)")


def discontinuous():
    c = Canvas(520, 270)
    x0, y0 = 50, 235
    _axes(c, x0, y0, 440, 215, "Effort", "Performance")
    poly(c, [(x0 + t * 4, y0 - 110 * _s(t, 35, 7)) for t in range(0, 106)], "BLUE", 2.4)
    poly(c, [(x0 + t * 4, y0 - 190 * _s(t, 60, 8)) for t in range(0, 106)], "GREEN", 2.4)
    text(c, (x0 + 425, y0 - 118), "first technology", "BLUE", "end", 12, "700")
    text(c, (x0 + 425, y0 - 198), "second (discontinuous) technology", "GREEN", "end", 12, "700")
    REG.put("discontinuous", c, "A discontinuous technology",
            "A second technology serves the same need on a new knowledge base; it may start below the first one and "
            "overtake it (Slide 15)")


def adoption():
    c = Canvas(560, 270)
    x0, y0 = 30, 220
    f = lambda z: math.exp(-z * z / 2)  # noqa: E731
    X = lambda z: 280 + z * 85  # noqa: E731
    poly(c, [(X(z / 20), y0 - 180 * f(z / 20)) for z in range(-60, 61)], "BLUE", 2.4)
    line(c, (x0, y0), (530, y0), "EDGE", 1.4)
    cuts = [(-2, "2.5%", "Innovators"), (-1, "13.5%", "Early adopters"), (0, "34%", "Early majority"),
            (1, "34%", "Late majority"), (3, "16%", "Laggards")]
    prev = -3
    for z, pct, lab in cuts:
        if z < 3:
            line(c, (X(z), y0), (X(z), y0 - 180 * f(z)), "EDGE", 1, "4 3")
        xm = X((prev + min(z, 3)) / 2)
        text(c, (xm, y0 + 16), pct, "HEAD", "middle", 12, "700")
        text(c, (xm, y0 + 32), lab, "TEXT", "middle", 11)
        prev = z
    REG.put("adoption", c, "Adopter categories of a diffusing technology",
            "Innovators (2.5%), early adopters (13.5%), early majority (34%), late majority (34%) and laggards (16%) on "
            "the bell-shaped curve of new adopters (Slide 16)")


def build():
    for fn in (network, s_curve, discontinuous, adoption):
        fn()
    return REG
