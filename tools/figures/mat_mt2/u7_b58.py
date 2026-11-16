"""Unit 7 figures of block B58 (magnetic moments, fields and types of magnetism, applied).

    u7-b58-b-lines  induction B against mu0*H for three materials, lines 1, 2 and 3, with the dashed vacuum line B = mu0*H
                    (line 1 above the dashed line: paramagnetic; line 2 below: diamagnetic; line 3 much steeper:
                    ferromagnetic). Schematic: the slopes of 1 and 2 are exaggerated.
"""
from figures.svgkit import Canvas, line, text, arrow
from figures.mat_mt2.common import figure

O = (60, 262)


def _pt(dx, slope):
    return (O[0] + dx, O[1] - slope * dx)


@figure("u7-b58-b-lines", "Induction B against mu0 H: dashed line B = mu0 H and three solid lines 1, 2 and 3 through the origin with different slopes")
def b_lines():
    c = Canvas(420, 300)
    arrow(c, (O[0] - 12, O[1]), (400, O[1]), "EDGE", 1.5, 9)
    arrow(c, (O[0], O[1] + 12), (O[0], 14), "EDGE", 1.5, 9)
    text(c, (398, O[1] + 20), "μ₀H", "TEXT", "end", 13)
    text(c, (O[0] + 8, 26), "B", "TEXT", "start", 13)
    line(c, O, _pt(220, 1.0), "EDGE", 1.8, dash="6 5")
    line(c, O, _pt(183, 1.2), "PINK", 2.6)
    line(c, O, _pt(220, 0.8), "BLUE", 2.6)
    line(c, O, _pt(88, 2.5), "GREEN", 2.6)
    e1, e0, e2, e3 = _pt(183, 1.2), _pt(220, 1.0), _pt(220, 0.8), _pt(88, 2.5)
    text(c, (e1[0] - 2, e1[1] - 8), "1", "PINK", "middle", 16, "700")
    text(c, (e3[0] - 2, e3[1] - 8), "3", "GREEN", "middle", 16, "700")
    text(c, (e0[0] + 8, e0[1] + 4), "B = μ₀H", "TEXT", "start", 13)
    text(c, (e2[0] + 8, e2[1] + 5), "2", "BLUE", "start", 16, "700")
    return c
