"""Unit 6, block B56: ln(sigma) against 1/T for two n-type semiconductors with the same donor concentration."""
from figures.svgkit import Canvas, line, text, poly, arrow
from figures.mat_mt2.common import figure


@figure("u6-b56-two-curves",
        "ln σ against 1/T for two n-type semiconductors A and B with the same donor concentration: A leaves the flat "
        "range at a higher temperature and its high-temperature line is steeper than that of B",
        "ln σ against 1/T for two n-type semiconductors, A and B, doped with the same number of donors")
def two_curves():
    c = Canvas(480, 290)
    x0, y0 = 60, 240
    arrow(c, (x0, y0), (455, y0), "EDGE", 1.5, 9)
    arrow(c, (x0, y0), (x0, 20), "EDGE", 1.5, 9)
    text(c, (255, 278), "1/T", "TEXT", "middle", 13)
    text(c, (x0 - 6, 258), "High T", "TEXT", "start", 12)
    text(c, (445, 258), "Low T", "TEXT", "end", 12)
    c.add('<text x="36" y="130" fill="TEXT" font-size="13" text-anchor="middle" transform="rotate(-90 36 130)">ln σ</text>')
    # shared flat range and extrinsic range (same donor concentration)
    poly(c, [(175, 150), (240, 150), (420, 211)], "EDGE", 2.2)
    # curve A leaves the flat range at a higher temperature (smaller 1/T) and rises steeply
    poly(c, [(175, 150), (100, 32)], "PINK", 2.6)
    # curve B leaves it at a lower temperature (larger 1/T) and rises less steeply
    poly(c, [(240, 150), (100, 56)], "BLUE", 2.6)
    text(c, (88, 36), "A", "PINK", "middle", 15, "700")
    text(c, (88, 64), "B", "BLUE", "middle", 15, "700")
    return c
