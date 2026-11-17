"""Figures of the Part II problems P01 to P04 of the Midterm 2 bank (archetype phase-diagram-invariant).

Four hypothetical binary systems drawn to scale from a small data structure each: every boundary passes through the
invariant points, melting points and compound compositions that the notes use, and every invariant temperature and the
three compositions of each invariant line are printed on the diagram. The microstructure sketches of P01 and P03 are
schematic (primary grains, lamellar eutectic or eutectoid, liquid).
"""
import math

from figures.svgkit import Canvas, line, text, poly, dot, circle
from figures.mat_mt2.common import figure
from figures.materials_t4 import Plot


def smooth(pts, n=12):
    """Catmull-Rom curve through the points (passes exactly through each one)."""
    if len(pts) < 3:
        return list(pts)
    out, ext = [], [pts[0]] + list(pts) + [pts[-1]]
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)))
    out.append(pts[-1])
    return out


def draw_diagram(d):
    """Draw the diagram described by the dict d (see the four data sets below) and return the canvas."""
    c = Canvas(*d.get("size", (720, 480)))
    P = Plot(c, d.get("box", (78, 40, 616, 418)), (0, 100), d["trange"])
    liq = []
    for seg in d["liquidus"]:
        liq += smooth(seg)
    P.area([(0, d["trange"][1])] + liq + [(100, d["trange"][1])], "BLUE", 0.07)
    for seg in d["liquidus"]:
        P.line(smooth(seg), "ACC", 2.2)
    for seg in d["curves"]:
        P.line(smooth(seg), "ACC", 2.2)
    for x, top in d.get("compounds", ()):
        P.line([(x, d["trange"][0]), (x, top)], "ACC", 2.6)
    P.frame(d["xt"], d["yt"], d["xlabel"], "Temperature (°C)")
    for inv in d["invariants"]:
        x1, x2, t = inv["x"][0], inv["x"][1], inv["t"]
        P.line([(x1, t), (x2, t)], "ACC", 2.2)
        tx, tdx, tdy, anchor = inv["tlab"]
        P.text(tx, t, f"{t} °C", "HEAD", anchor, 12, "700", dx=tdx, dy=tdy)
        for x, lab, dx, dy in inv["pts"]:
            P.dot(x, t, 3.6, "GREEN")
            P.text(x, t, lab, "TEXT", "middle", 11.5, "700", dx=dx, dy=dy)
    for x, t, lab, dx, dy, anchor in d.get("melt", ()):
        P.dot(x, t, 3.6, "GREEN")
        P.text(x, t, lab, "HEAD", anchor, 12, "700", dx=dx, dy=dy)
    for x, t, s, size in d["labels"]:
        P.text(x, t, s, "HEAD", "middle", size)
    for (x, t), (lx, lt), s, anchor in d.get("callouts", ()):
        a, b = P.p(x, t), P.p(lx, lt)
        line(c, a, b, "EDGE", 1)
        text(c, (b[0] + (4 if anchor == "start" else -4), b[1] + 4), s, "HEAD", anchor, 12, "700")
    return c


# --------------------------------------------------------------------------- P01: A-B, congruent compound, two eutectics
P01 = dict(
    trange=(200, 1300), xlabel="Composition (wt% B)",
    xt=[(0, "0 (A)"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (B)")],
    yt=[(200, "200"), (400, "400"), (600, "600"), (800, "800"), (1000, "1000"), (1200, "1200")],
    liquidus=[[(0, 900), (18, 815), (35, 700)],
              [(35, 700), (45, 935), (53, 1105), (60, 1150), (67, 1105), (73, 1010), (78, 850)],
              [(78, 850), (90, 960), (100, 1050)]],
    curves=[[(0, 900), (5, 805), (10, 700)], [(10, 700), (6, 450), (3, 200)],
            [(92, 850), (97, 960), (100, 1050)], [(92, 850), (94, 500), (95, 200)]],
    compounds=[(60, 1150)],
    invariants=[dict(x=(10, 60), t=700, tlab=(10, -6, -6, "end"),
                     pts=[(10, "10", 8, 17), (35, "35", 0, 17), (60, "60", 13, 17)]),
                dict(x=(60, 92), t=850, tlab=(92, 8, -4, "start"),
                     pts=[(60, "60", -13, -7), (78, "78", 0, 17), (92, "92", -6, 17)])],
    melt=[(0, 900, "900 °C", 8, -8, "start"), (100, 1050, "1050 °C", -8, -10, "end"), (60, 1150, "1150 °C", 0, -12, "middle")],
    labels=[(30, 1150, "L", 15), (4, 560, "α", 14), (21, 740, "α + L", 11.5), (35, 450, "α + γ", 13),
            (51, 790, "γ + L", 12), (68, 910, "γ + L", 12), (77, 520, "γ + β", 13), (97, 640, "β", 14),
            (63, 250, "γ", 14)],
    callouts=[((90, 900), (100, 1180), "β + L", "start")],
)


@figure("p01-ab-diagram", "Hypothetical A-B phase diagram with a congruently melting compound γ at 60 wt% B and two eutectics",
        "Hypothetical A-B phase diagram (wt% B): α and β terminal solid solutions, compound γ of 60 wt% B melting "
        "at 1150 °C, eutectics at 700 °C (α 10, L 35, γ 60) and 850 °C (γ 60, L 78, β 92); A melts at 900 °C and B at 1050 °C")
def p01_diagram():
    c = draw_diagram(dict(P01, size=(720, 480)))
    return c


# --------------------------------------------------------------------------- microstructure sketches
def micro(c, cx, cy, r, uid, matrix, blobs, labels, rims=()):
    """Schematic micrograph in a circle. matrix: 'liquid' | 'lam' | 'lamfine'; blobs: (dx, dy, radius, kind) with
    kind 'solid' | 'lamfine'; labels: (text, dx, dy) target points with a leader to the right; rims: blob indices
    drawn with a thick boundary film."""
    holes = "".join(f'<circle cx="{cx + dx:.1f}" cy="{cy + dy:.1f}" r="{rr:.1f}" fill="black"/>' for dx, dy, rr, _ in blobs)
    c.add(f'<clipPath id="clip-{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>')
    c.add(f'<mask id="mask-{uid}"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="white"/>{holes}</mask>')
    c.add(f'<g clip-path="url(#clip-{uid})">')
    if matrix == "liquid":
        circle(c, (cx, cy), r, "BLUE", 0, fill="BLUE", opacity=0.06)
    else:
        gap = 6 if matrix == "lam" else 3.6
        c.add(f'<g mask="url(#mask-{uid})">')
        for k in range(-2 * int(r), 2 * int(r) + 1, int(gap * 1.4) if matrix == "lam" else 4):
            line(c, (cx + k - r, cy + r), (cx + k + r, cy - r), "HEAD", 1.0 if matrix == "lam" else 0.8)
        c.add("</g>")
    for i, (dx, dy, rr, kind) in enumerate(blobs):
        bx, by = cx + dx, cy + dy
        if kind == "lamfine":
            c.add(f'<clipPath id="cb-{uid}-{i}"><circle cx="{bx:.1f}" cy="{by:.1f}" r="{rr:.1f}"/></clipPath>'
                  f'<g clip-path="url(#cb-{uid}-{i})">')
            ang = 0.3 + 0.7 * i
            ux, uy = math.cos(ang), math.sin(ang)
            for k in range(-12, 13):
                px, py = bx - uy * k * 3.2, by + ux * k * 3.2
                line(c, (px - 40 * ux, py - 40 * uy), (px + 40 * ux, py + 40 * uy), "HEAD", 0.8)
            c.add("</g>")
            circle(c, (bx, by), rr, "HEAD", 1.2)
        else:
            circle(c, (bx, by), rr, "HEAD", 1.4, fill="BLUE", opacity=0.16)
        if i in rims:
            circle(c, (bx, by), rr + 1.5, "GREEN", 3.2)
    c.add("</g>")
    circle(c, (cx, cy), r, "HEAD", 1.6)
    for k, (s, dx, dy) in enumerate(labels):
        ty = cy - r + 14 + k * 26
        line(c, (cx + dx, cy + dy), (cx + r + 12, ty - 4), "EDGE", 1)
        text(c, (cx + r + 16, ty), s, "HEAD", "start", 12, "700")


BL_P01 = [(-38, -30, 20, "solid"), (22, -46, 17, "solid"), (-8, 14, 22, "solid"), (40, 18, 19, "solid"),
          (-46, 38, 15, "solid"), (12, 58, 15, "solid")]


@figure("p01-sketches", "Two microstructure sketches of the A-20 wt% B alloy, just above and just below 700 °C",
        "A-20 wt% B: left, at 700 + ΔT °C, primary α grains (60 %) in liquid of 35 wt% B (40 %); right, at 700 − ΔT °C, "
        "the same primary α grains in the lamellar eutectic α + γ (40 %)")
def p01_sketches():
    c = Canvas(720, 260)
    micro(c, 110, 125, 90, "p01a", "liquid", BL_P01, [("primary α", -38, -30), ("liquid L", 30, 70)])
    text(c, (110, 248), "700 + ΔT °C", "HEAD", "middle", 13, "700")
    micro(c, 450, 125, 90, "p01b", "lam", BL_P01, [("primary α", -38, -30), ("eutectic (α + γ)", 30, 70)])
    text(c, (450, 248), "700 − ΔT °C", "HEAD", "middle", 13, "700")
    return c


# --------------------------------------------------------------------------- P02: M-N, peritectic compound + eutectic (at%)
P02 = dict(
    trange=(300, 1500), xlabel="Composition (at% N)",
    xt=[(0, "0 (M)"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (N)")],
    yt=[(300, "300"), (500, "500"), (700, "700"), (900, "900"), (1100, "1100"), (1300, "1300"), (1500, "1500")],
    liquidus=[[(0, 1400), (30, 1260), (60, 1110), (78, 1000)],
              [(78, 1000), (86, 820), (92, 600)],
              [(92, 600), (96, 650), (100, 700)]],
    curves=[[(0, 1400), (12, 1220), (25, 1000)], [(25, 1000), (19, 650), (15, 300)],
            [(98, 600), (99.3, 650), (100, 700)], [(98, 600), (98.7, 450), (99, 300)]],
    compounds=[(66.7, 1000)],
    invariants=[dict(x=(25, 78), t=1000, tlab=(25, -6, -6, "end"),
                     pts=[(25, "25", 8, 17), (66.7, "66.7", -18, 17), (78, "78", 9, -7)]),
                dict(x=(66.7, 98), t=600, tlab=(80, 0, -7, "middle"),
                     pts=[(66.7, "66.7", -18, 17), (92, "92", 0, 17), (98, "98", 5, 17)])],
    melt=[(0, 1400, "1400 °C", 8, -8, "start"), (100, 700, "700 °C", -8, -12, "end")],
    labels=[(62, 1330, "L", 15), (5, 700, "α", 14), (36, 1100, "α + L", 12), (42, 640, "α + δ", 13),
            (76, 830, "δ + L", 12), (83, 450, "δ + β", 13), (69.5, 380, "δ", 14)],
    callouts=[((96, 630), (100, 900), "β + L", "start"), ((99.3, 400), (100, 480), "β", "start")],
)


@figure("p02-mn-diagram", "Hypothetical M-N phase diagram in atomic percent with an incongruently melting compound δ = MN2",
        "Hypothetical M-N phase diagram (at% N): α solid solution, compound δ = MN₂ (66.7 at% N) formed by a peritectic "
        "reaction at 1000 °C (α 25, δ 66.7, L 78), eutectic at 600 °C (δ 66.7, L 92, β 98); M melts at 1400 °C and N at 700 °C")
def p02_diagram():
    return draw_diagram(P02)


# --------------------------------------------------------------------------- P03: X-Y, peritectic, eutectics and eutectoid
P03 = dict(
    trange=(300, 1400), xlabel="Composition (wt% Y)",
    xt=[(0, "0 (X)"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (Y)")],
    yt=[(300, "300"), (500, "500"), (700, "700"), (800, "800"), (1000, "1000"), (1200, "1200"), (1300, "1300")],
    liquidus=[[(0, 1300), (22, 1215), (45, 1100)],
              [(45, 1100), (48, 1010), (50, 900)],
              [(50, 900), (53, 985), (55, 1000), (58, 985), (68, 850), (80, 650)],
              [(80, 650), (90, 720), (100, 800)]],
    curves=[[(0, 1300), (8, 1210), (15, 1100)], [(15, 1100), (12, 850), (10, 600), (7, 300)],
            [(30, 1100), (27, 850), (25, 600)], [(30, 1100), (34, 1000), (38, 900)],
            [(38, 900), (32, 750), (25, 600)],
            [(95, 650), (98, 730), (100, 800)], [(95, 650), (96.3, 450), (97, 300)]],
    compounds=[(55, 1000)],
    invariants=[dict(x=(15, 45), t=1100, tlab=(15, -6, -6, "end"),
                     pts=[(15, "15", -2, 17), (30, "30", 0, 17), (45, "45", 10, -7)]),
                dict(x=(38, 55), t=900, tlab=(55, 8, 12, "start"),
                     pts=[(38, "38", -10, -7), (50, "50", -2, 17), (55, "55", 12, -7)]),
                dict(x=(55, 95), t=650, tlab=(88, 0, -7, "middle"),
                     pts=[(55, "55", 12, -7), (80, "80", 0, 17), (95, "95", -2, 17)]),
                dict(x=(10, 55), t=600, tlab=(40, 0, 18, "middle"),
                     pts=[(10, "10", -2, 17), (25, "25", 0, 17), (55, "55", 12, 17)])],
    melt=[(0, 1300, "1300 °C", 8, -8, "start"), (100, 800, "800 °C", -8, -12, "end"), (55, 1000, "1000 °C", 6, -10, "start")],
    labels=[(25, 1310, "L", 15), (4, 820, "α", 14), (31, 860, "β", 14), (19.5, 830, "α + β", 11.5),
            (42, 1015, "β + L", 11.5), (45, 760, "β + γ", 11.5), (32, 440, "α + γ", 13), (64, 820, "γ + L", 12),
            (75, 450, "γ + δ", 13), (58, 340, "γ", 14)],
    callouts=[((10, 1180), (3, 1365), "α + L", "start"), ((52.5, 940), (60, 1130), "γ + L", "start"),
              ((92, 690), (100, 1000), "δ + L", "start"), ((96.6, 400), (100, 500), "δ", "start")],
)


@figure("p03-xy-diagram", "Hypothetical X-Y phase diagram with a peritectic, two eutectics and a eutectoid decomposition of β",
        "Hypothetical X-Y phase diagram (wt% Y): peritectic at 1100 °C (α 15, β 30, L 45), eutectic at 900 °C (β 38, L 50, "
        "γ 55), compound γ of 55 wt% Y melting at 1000 °C, eutectic at 650 °C (γ 55, L 80, δ 95) and eutectoid at 600 °C "
        "(α 10, β 25, γ 55); X melts at 1300 °C and Y at 800 °C")
def p03_diagram():
    return draw_diagram(P03)


BL_P03 = [(-40, -28, 17, "solid"), (20, -48, 13, "solid"), (-6, 12, 18, "solid"), (42, 20, 15, "solid"),
          (-44, 40, 12, "solid"), (14, 60, 12, "solid")]
BIG_P03 = [(-34, -30, 30, "solid"), (30, -36, 26, "solid"), (-14, 32, 30, "solid"), (44, 30, 22, "solid")]


@figure("p03-sketches", "Three microstructure sketches of the X-40 wt% Y alloy at 1100 + ΔT, 900 − ΔT and 600 − ΔT °C",
        "X-40 wt% Y: at 1100 + ΔT °C, primary α (16.7 %) in liquid; at 900 − ΔT °C, primary β (83.3 %, formed by the "
        "peritectic reaction and grown from the liquid) in the eutectic β + γ (16.7 %); at 600 − ΔT °C, every β has become "
        "the fine eutectoid α + γ, with γ films precipitated between 900 and 600 °C on the grain boundaries")
def p03_sketches():
    c = Canvas(760, 250)
    micro(c, 85, 115, 72, "p03a", "liquid", BL_P03, [("primary α", -40, -28), ("liquid L", 30, 55)])
    text(c, (85, 232), "1100 + ΔT °C", "HEAD", "middle", 13, "700")
    micro(c, 335, 115, 72, "p03b", "lam", BIG_P03, [("primary β", -34, -30), ("eutectic (β + γ)", 8, 60)])
    text(c, (335, 232), "900 − ΔT °C", "HEAD", "middle", 13, "700")
    big = [(dx, dy, rr, "lamfine") for dx, dy, rr, _ in BIG_P03]
    micro(c, 585, 115, 72, "p03c", "lam", big, [("eutectoid (α + γ)", -34, -30), ("γ film", 30, -8),
                                                  ("former eutectic", 8, 60)], rims=(0, 1, 2, 3))
    text(c, (585, 232), "600 − ΔT °C", "HEAD", "middle", 13, "700")
    return c


# --------------------------------------------------------------------------- P04: G-H, congruent θ + incongruent η
P04 = dict(
    trange=(700, 1600), xlabel="Composition (wt% H)",
    xt=[(0, "0 (G)"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (H)")],
    yt=[(700, "700"), (900, "900"), (1100, "1100"), (1300, "1300"), (1500, "1500")],
    liquidus=[[(0, 1500), (8, 1390), (15, 1250)],
              [(15, 1250), (22, 1360), (30, 1400), (34, 1330), (38, 1180), (40, 1000)],
              [(40, 1000), (45, 1080), (50, 1150)],
              [(50, 1150), (75, 1270), (100, 1350)]],
    curves=[[(0, 1500), (3, 1380), (6, 1250)], [(6, 1250), (4, 1000), (3, 700)],
            [(88, 1150), (95, 1270), (100, 1350)], [(88, 1150), (91, 900), (92, 700)]],
    compounds=[(30, 1400), (60, 1150)],
    invariants=[dict(x=(6, 30), t=1250, tlab=(6, -6, -6, "end"),
                     pts=[(6, "6", 8, 17), (15, "15", 0, 17), (30, "30", -10, 17)]),
                dict(x=(30, 60), t=1000, tlab=(45, 0, 18, "middle"),
                     pts=[(30, "30", -10, 17), (40, "40", -8, -7), (60, "60", 11, 17)]),
                dict(x=(50, 88), t=1150, tlab=(88, 8, -4, "start"),
                     pts=[(50, "50", -9, -7), (60, "60", 11, 17), (88, "88", -8, 17)])],
    melt=[(0, 1500, "1500 °C", 8, -8, "start"), (100, 1350, "1350 °C", -8, -12, "end"), (30, 1400, "1400 °C", 0, -12, "middle")],
    labels=[(60, 1460, "L", 15), (1.8, 870, "α", 12), (25.5, 1290, "θ + L", 11), (34.2, 1180, "θ+L", 10),
            (17, 950, "α + θ", 13), (45, 850, "θ + η", 13), (53, 1070, "η + L", 11.5), (74, 900, "η + β", 13),
            (80, 1215, "β + L", 12), (96, 1000, "β", 14), (27, 760, "θ", 13), (63, 760, "η", 13)],
    callouts=[((4, 1350), (12, 1560), "α + L", "start")],
)


@figure("p04-gh-diagram", "Hypothetical G-H phase diagram built from the data table: congruent compound θ and incongruent compound η",
        "Hypothetical G-H phase diagram (wt% H) drawn from the data of the statement: eutectic at 1250 °C (α 6, L 15, θ 30), "
        "compound θ of 30 wt% H melting congruently at 1400 °C, eutectic at 1000 °C (θ 30, L 40, η 60), peritectic at "
        "1150 °C (L 50, η 60, β 88); G melts at 1500 °C and H at 1350 °C")
def p04_diagram():
    return draw_diagram(P04)
