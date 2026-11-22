"""Figures of the Part II problems P05 to P08 of the Midterm 2 bank (archetype eutectic-lever-rule).

p05: the Pb-Sn diagram with the values of Session 7 Slide 32 and the readings used by Bank P05 (alloy Pb-50 wt% Sn).
p06: the hypothetical A-B eutectic diagram that Bank P06 asks the student to draw (straight lines between given points).
p07: a sketch of the micrograph of Bank P07 (primary Cu-rich dendrites in a eutectic matrix).
p08: the A-rich half of the hypothetical system of Bank P08, plotted from the table of its statement, with the cooling
path of the A-30 wt% B alloy.
Every number printed here is a number the solution reads; the curves of p05 are those of tools/figures/materials_t4.py.
"""
import math

from figures.svgkit import Canvas, line, text, rect, circle
from figures.mat_mt2.common import figure
from figures.mat_mt2.u4 import PBSN_SLIDES
from figures.materials_t4 import Plot, pbsn_curves, sub


# --------------------------------------------------------------------------- P05: Pb-Sn, alloy Pb-50 wt% Sn
@figure("p05-pbsn-alloy50", "Pb-Sn phase diagram with the alloy of 50 wt% Sn and tie lines at 200 and 100 °C",
        "Pb-Sn phase diagram with the values of Session 7 Slide 32 (Pb melts at 327 °C, Sn at 232 °C; eutectic at "
        "183 °C and 61.9 wt% Sn; α of 18.3 and β of 97.8 wt% Sn at 183 °C). The dashed vertical line is the alloy "
        "of 50 wt% Sn, which meets the liquidus at 215 °C; the tie line at 200 °C ends at 16.7 (α) and 55.7 (L) "
        "wt% Sn, and the one at 100 °C at 4.8 (α) and 99.8 (β) wt% Sn")
def p05_pbsn():
    c = Canvas(680, 420)
    P = Plot(c, (80, 30, 600, 350), (0, 100), (0, 350))
    d = PBSN_SLIDES
    liq_a, liq_b, sol_a, sol_b, solv_a, solv_b = pbsn_curves(d)
    P.area([(0, 350)] + liq_a + liq_b + [(100, 350)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.16)
    P.area([(100, d["tsn"])] + list(reversed(sol_b)) + solv_b + [(100, 0)], "BLUE", 0.16)
    for cv in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b):
        P.line(cv, "ACC", 2.2)
    P.line([(d["ca"], d["te"]), (d["cb"], d["te"])], "ACC", 2.2)
    P.frame([(0, "0 (Pb)"), (18.3, "18.3"), (50, "50"), (61.9, "61.9"), (80, "80"), (97.8, ""), (100, "100 (Sn)")],
            [(0, "0"), (100, "100"), (183, "183"), (200, "200"), (232, "232"), (327, "327")],
            "Composition (wt% Sn)", "Temperature (°C)")
    P.text(97.8, 183, "97.8", "TEXT", "end", 11.5, "400", dx=-4, dy=16)
    P.text(0, 327, "327 °C", "TEXT", "start", 11.5, "400", dx=8, dy=-4)
    P.text(100, 232, "232 °C", "TEXT", "end", 11.5, "400", dx=-6, dy=-8)
    P.text(61.9, 183, "E", "HEAD", "middle", 12, dy=-8)
    P.dot(61.9, 183, 3.6, "HEAD")
    # the alloy and its readings
    P.vseg(50, 0, 330, "GREEN", 1.6, "6,4")
    P.text(50, 330, sub("C", "0") + " = 50", "GREEN", "start", 12, dx=6, dy=4)
    P.dot(50, 215, 4, "GREEN")
    P.text(50, 215, "215 °C", "GREEN", "start", 11.5, dx=8, dy=-6)
    P.line([(16.7, 200), (55.7, 200)], "BLUE", 2.2)
    P.dot(16.7, 200, 3.4, "BLUE")
    P.dot(55.7, 200, 3.4, "BLUE")
    P.text(16.7, 200, "16.7", "BLUE", "end", 11.5, dx=-6, dy=-4)
    P.text(55.7, 200, "55.7", "BLUE", "start", 11.5, dx=5, dy=-6)
    P.line([(4.8, 100), (99.8, 100)], "BLUE", 2.2)
    P.dot(4.8, 100, 3.4, "BLUE")
    P.dot(99.8, 100, 3.4, "BLUE")
    P.text(4.8, 100, "4.8", "BLUE", "start", 11.5, dx=8, dy=16)
    P.text(99.8, 100, "99.8", "BLUE", "end", 11.5, dx=-6, dy=-6)
    P.text(30, 300, "L", size=15)
    P.text(4, 160, "α", size=14)
    P.text(100, 140, "β", "HEAD", "start", dx=8)
    P.text(32, 55, "α + β", size=14)
    P.text(31, 222, "α + L", size=12)
    P.text(88, 196, "β + L", size=11)
    return c


# --------------------------------------------------------------------------- P06: the diagram built from words
P06 = dict(ta=900, tb=700, te=550, ce=70, ca=20, cb=92, ca_rt=5, cb_rt=97, trt=20)


@figure("p06-ab-diagram", "Hypothetical A-B eutectic diagram drawn with straight lines from the data of the statement",
        "The A-B diagram of Bank P06 drawn with straight lines: A melts at 900 °C and B at 700 °C; eutectic at 550 °C "
        "and 70 wt% B; at 550 °C α holds 20 wt% B and β 92 wt% B (8 wt% A); at 20 °C the solvus lines reach 5 and "
        "97 wt% B. Dashed: the alloys of 85 wt% B (liquidus 625 °C) and 12 wt% B (solvus 267 °C)")
def p06_diagram():
    k = P06
    c = Canvas(680, 420)
    P = Plot(c, (80, 30, 600, 350), (0, 100), (0, 1000))
    liq_a = [(0, k["ta"]), (k["ce"], k["te"])]
    liq_b = [(k["ce"], k["te"]), (100, k["tb"])]
    sol_a = [(0, k["ta"]), (k["ca"], k["te"])]
    sol_b = [(100, k["tb"]), (k["cb"], k["te"])]
    solv_a = [(k["ca"], k["te"]), (k["ca_rt"], k["trt"])]
    solv_b = [(k["cb"], k["te"]), (k["cb_rt"], k["trt"])]
    P.area([(0, 1000)] + liq_a + liq_b + [(100, 1000)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, k["trt"])], "BLUE", 0.16)
    P.area([(100, k["tb"])] + sol_b + solv_b + [(100, k["trt"])], "BLUE", 0.16)
    for cv in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b, [(k["ca"], k["te"]), (k["cb"], k["te"])]):
        P.line(cv, "ACC", 2.2)
    P.hseg(0, 100, k["trt"], "EDGE", 1, "2,4")
    P.frame([(0, "0 (A)"), (5, ""), (12, "12"), (20, "20"), (40, "40"), (70, "70"), (85, "85"), (92, ""), (97, ""),
             (100, "100 (B)")],
            [(20, "20"), (267, "267"), (550, "550"), (625, "625"), (700, "700"), (900, "900")],
            "Composition (wt% B)", "Temperature (°C)")
    P.text(5, 20, "5", "TEXT", "middle", 11.5, "400", dy=-8)
    P.text(97, 20, "97", "TEXT", "middle", 11.5, "400", dy=-8)
    P.text(92, 550, "92", "TEXT", "end", 11.5, "400", dx=-3, dy=16)
    P.text(20, 550, "20", "TEXT", "start", 11.5, "400", dx=3, dy=16)
    P.text(70, 550, "E (70)", "HEAD", "middle", 12, dy=18)
    for x in (20, 70, 92):
        P.dot(x, 550, 3.6, "HEAD")
    P.text(0, 900, "900 °C", "TEXT", "start", 11.5, "400", dx=8, dy=-4)
    P.text(100, 700, "700 °C", "TEXT", "end", 11.5, "400", dx=-6, dy=-8)
    for x0, t_top in ((85, 625), (12, 267.3)):
        P.vseg(x0, 0, 960, "GREEN", 1.4, "6,4")
        P.dot(x0, t_top, 4, "GREEN")
    P.text(85, 960, sub("C", "0") + " = 85", "GREEN", "end", 11.5, dx=-6, dy=4)
    P.text(12, 960, sub("C", "0") + " = 12", "GREEN", "start", 11.5, dx=6, dy=4)
    P.text(45, 880, "L", size=15)
    P.text(3, 420, "α", size=14, dx=2)
    P.text(99, 420, "β", size=14, dx=-4)
    P.text(25, 680, "α + L", size=12.5)
    P.line([(88.5, 585), (90, 760)], "TEXT", 1.0)
    P.text(90, 760, "β + L", size=11.5, dy=-4)
    P.text(50, 300, "α + β", size=14)
    return c


# --------------------------------------------------------------------------- P07: micrograph sketch
def _lamellae(c, x, y, w, h, uid, angle=0.6, gap=6):
    c.add(f'<clipPath id="cl-{uid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>'
          f'<g clip-path="url(#cl-{uid})">')
    dx, dy = math.cos(angle), math.sin(angle)
    cx, cy = x + w / 2, y + h / 2
    for k in range(-60, 61):
        px, py = cx + k * gap * -dy, cy + k * gap * dx
        line(c, (px - 400 * dx, py - 400 * dy), (px + 400 * dx, py + 400 * dy), "HEAD", 1.0)
    c.add("</g>")


@figure("p07-agcu-micrograph", "Sketch of the micrograph: rounded primary grains in a lamellar matrix",
        "Sketch of the micrograph of Bank P07 at room temperature: rounded, dendritic grains of a primary constituent "
        "(shaded) in a fine lamellar eutectic matrix; image analysis gives 55 % of the section as lamellar matrix")
def p07_micro():
    c = Canvas(460, 300)
    x0, y0, w, h = 30, 20, 260, 260
    blobs = ((70, 70, 34), (180, 55, 30), (120, 150, 38), (215, 170, 32), (60, 210, 30), (160, 235, 22))
    holes = "".join(f'<circle cx="{x0 + bx}" cy="{y0 + by}" r="{r}" fill="black"/>' for bx, by, r in blobs)
    c.add(f'<mask id="mask-p07"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="white"/>{holes}</mask>')
    c.add('<g mask="url(#mask-p07)">')
    _lamellae(c, x0, y0, w, h, "p07")
    c.add("</g>")
    for bx, by, r in blobs:
        circle(c, (x0 + bx, y0 + by), r, "HEAD", 1.6, fill="BLUE", opacity=0.22)
        for a in (0, 1.57, 3.14, 4.71):                       # short dendrite arms
            line(c, (x0 + bx + 0.45 * r * math.cos(a), y0 + by + 0.45 * r * math.sin(a)),
                 (x0 + bx + 0.85 * r * math.cos(a), y0 + by + 0.85 * r * math.sin(a)), "HEAD", 1.2)
    rect(c, x0, y0, w, h, "HEAD", 1.6)
    line(c, (x0 + 120 + 38, y0 + 150), (330, 120), "TEXT", 1.0)
    text(c, (336, 116), "primary grains", "HEAD", "start", 12.5, "700")
    text(c, (336, 132), "(45 % of the area)", "TEXT", "start", 11.5)
    line(c, (x0 + 245, y0 + 110), (330, 190), "TEXT", 1.0)
    text(c, (336, 194), "lamellar matrix", "HEAD", "start", 12.5, "700")
    text(c, (336, 210), "(55 % of the area)", "TEXT", "start", 11.5)
    return c


# --------------------------------------------------------------------------- P08: A-rich half from the table
P08_ROWS = [(1000, 0, 0), (950, 12, 4), (900, 24, 8), (850, 36, 12), (800, 48, 16)]
P08_SOLV = [(800, 16), (600, 10), (400, 6), (20, 3)]
P08_SOLV_B = [(800, 85), (600, 88), (400, 91), (20, 94)]


@figure("p08-table-diagram", "A-B diagram plotted from the table of Bank P08 with the cooling path of the A-30 wt% B alloy",
        "The points of the table of Bank P08 joined by straight segments: liquidus (C_L) and solidus (C_α) from "
        "1000 °C to the eutectic at 800 °C and 48 wt% B, α and β solvus down to 20 °C. Dashed: the alloy of 30 wt% B, "
        "which meets the liquidus at 875 °C (first solid α of 10 wt% B); tie lines at 875 and 850 °C")
def p08_diagram():
    c = Canvas(680, 560)
    P = Plot(c, (80, 30, 600, 490), (0, 100), (0, 1050))
    liq = [(cl, t) for t, cl, _ in P08_ROWS]
    sol = [(ca, t) for t, _, ca in P08_ROWS]
    solv = [(x, t) for t, x in P08_SOLV]
    solv_b = [(x, t) for t, x in P08_SOLV_B]
    P.area([(0, 1050)] + liq + [(48, 1050)], "BLUE", 0.06)
    P.area(sol + solv + [(0, 20)], "BLUE", 0.16)
    P.area(solv_b + [(100, 20), (100, 800)], "BLUE", 0.16)
    for cv in (liq, sol, solv, solv_b, [(16, 800), (85, 800)]):
        P.line(cv, "ACC", 2.2)
    for t, cl, ca in P08_ROWS[1:]:
        P.dot(cl, t, 3.0, "HEAD")
        P.dot(ca, t, 3.0, "HEAD")
    for (t, x) in P08_SOLV[1:] + P08_SOLV_B[1:]:
        P.dot(x, t, 3.0, "HEAD")
    P.frame([(0, "0 (A)"), (10, "10"), (16, "16"), (30, "30"), (48, "48"), (70, "70"), (85, "85"), (100, "100 (B)")],
            [(20, "20"), (400, "400"), (600, "600"), (800, "800"), (1000, "1000")],
            "Composition (wt% B)", "Temperature (°C)")
    P.vseg(30, 0, 1020, "GREEN", 1.5, "6,4")
    P.text(30, 1020, sub("C", "0") + " = 30", "GREEN", "start", 11.5, dx=6, dy=4)
    P.line([(10, 875), (30, 875)], "BLUE", 2.2)
    P.line([(12, 850), (36, 850)], "BLUE", 2.2)
    P.dot(30, 875, 4, "GREEN")
    P.dot(10, 875, 3.6, "BLUE")
    P.text(10, 875, "10", "BLUE", "end", 11.5, dx=-8, dy=4)
    P.text(36, 850, "36", "BLUE", "start", 11.5, dx=7, dy=-4)
    P.text(12, 850, "12", "BLUE", "end", 11.5, dx=-8, dy=14)
    P.text(48, 800, "E", "HEAD", "middle", 12, dy=18)
    P.text(30, 990, "L", size=15, dx=-30)
    P.text(75, 930, "B-rich side not in the table", "TEXT", "middle", 11.5, "400")
    P.text(4, 520, "α", size=14)
    P.text(97, 520, "β", size=14)
    P.text(45, 400, "α + β", size=14)
    P.text(21, 930, "α + L", size=12)
    return c
