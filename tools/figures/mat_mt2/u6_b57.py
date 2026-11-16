"""Unit 6 figures of block B57 (dielectrics, ferroelectrics and piezoelectrics, applied).

    u6-b57-pe-pair  polarisation against electric field of two ferroelectrics, loops 1 (wide) and 2 (narrow); both have
                    the same remanent polarisation (70) and the same polarisation at the tips of the loop (95); schematic.
"""
import math

from figures.svgkit import Canvas, line, text, poly, dot, arrow
from figures.mat_mt2.common import figure

SPAN = 150.0
PR, PS = 70.0, 95.0


def _params(ec):
    """amp, w such that amp*tanh(ec/w) = PR (remanence) and amp*tanh(SPAN/w) = PS (tip of the loop)."""
    lo, hi = 5.0, 5000.0
    for _ in range(100):
        w = (lo + hi) / 2
        if math.tanh(SPAN / w) / math.tanh(ec / w) > PS / PR:
            hi = w
        else:
            lo = w
    return PR / math.tanh(ec / w), w


def _loop(c, o, ec, col):
    amp, w = _params(ec)
    es = [-SPAN + 2 * SPAN * i / 150 for i in range(151)]
    sh = lambda e: ec * (1 - (e / SPAN) ** 2)  # noqa: E731
    up = [(o[0] + e, o[1] - amp * math.tanh((e + sh(e)) / w)) for e in es]
    dn = [(o[0] + e, o[1] - amp * math.tanh((e - sh(e)) / w)) for e in es]
    poly(c, up, col, 2.5)
    poly(c, dn, col, 2.5)


@figure("u6-b57-pe-pair", "Polarisation against electric field for two ferroelectrics: loop 1 is wide and loop 2 is narrow, both with the same height at the tips")
def pe_pair():
    c = Canvas(440, 300)
    o = (220, 150)
    arrow(c, (40, o[1]), (415, o[1]), "EDGE", 1.5, 9)
    arrow(c, (o[0], 285), (o[0], 15), "EDGE", 1.5, 9)
    text(c, (412, o[1] + 20), "E", "TEXT", "end", 13)
    text(c, (o[0] + 8, 26), "P", "TEXT", "start", 13)
    _loop(c, o, 70, "PINK")
    _loop(c, o, 18, "BLUE")
    text(c, (o[0] + 118, o[1] + 62), "1", "PINK", "middle", 16, "700")
    text(c, (o[0] - 118, o[1] - 62), "1", "PINK", "middle", 16, "700")
    text(c, (o[0] + 40, o[1] - 108), "2", "BLUE", "middle", 16, "700")
    text(c, (o[0] - 40, o[1] + 112), "2", "BLUE", "middle", 16, "700")
    return c
