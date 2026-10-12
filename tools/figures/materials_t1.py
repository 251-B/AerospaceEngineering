"""Topic 1 figures for Aerospace Materials I: the materials tetrahedron, ion-pair force and energy curves,
and the potential wells of titanium and aluminium (schematic shapes, no numerical values)."""
from figures.svgkit import Canvas, Registry, curve, line, text

REG = Registry("T1")


def tetrahedron():
    c = Canvas(520, 300)
    a, s, p, r = (260, 40), (110, 200), (400, 170), (280, 250)   # Applications, Structure, Properties, Processing
    for u, v in ((a, s), (a, p), (a, r), (s, p), (s, r), (p, r)):
        line(c, u, v, "EDGE", 2)
    for q in (a, s, p, r):
        c.add(f'<circle cx="{q[0]}" cy="{q[1]}" r="14" fill="ACC"/>')
    for q, t, anc, dx, dy in ((a, "Applications", "start", 24, -4), (s, "Structure", "end", -16, 4),
                              (p, "Properties", "start", 20, -4), (r, "Processing", "start", 20, 18)):
        text(c, q, t, "HEAD", anc, 15, "700", dx, dy)
    REG.put("tetrahedron", c, "Tetrahedron linking structure, properties, processing and applications",
            "The four linked corners of materials science")


def force_energy():
    n = 6                                     # model shapes: attraction -1/a, repulsion +1/(n a^n), minimum at a = 1
    X0, X1 = 0.8, 3.0
    xs = [X0 + (X1 - X0) * k / 240 for k in range(241)]
    px = lambda a: 70 + (a - X0) / (X1 - X0) * 420   # noqa: E731
    E = lambda a: -1 / a + 1 / (n * a ** n)           # noqa: E731
    F = lambda a: 1 / a ** 2 - 1 / a ** (n + 1)       # noqa: E731  (F = dE/da, attraction positive)
    amax = ((n + 1) / 2) ** (1 / (n - 1))
    ey0, es, et, eb = 70, 120, 24, 200
    fy0, fs, ft, fb = 335, 150, 236, 425
    c = Canvas(540, 450)
    line(c, (70, ey0), (500, ey0)); line(c, (70, et), (70, eb))
    text(c, (76, et + 4), "Energy", "HEAD", weight="700"); text(c, (500, ey0 - 6), "distance a", anchor="end")
    curve(c, lambda a: 1 / (n * a ** n), xs, px, ey0, es, et, eb, "BLUE", 1.6, "9,5")
    curve(c, lambda a: -1 / a, xs, px, ey0, es, et, eb, "PINK", 1.6, "2,3")
    curve(c, E, xs, px, ey0, es, et, eb, "ACC", 2.6)
    text(c, (px(0.98), et + 30), "repulsion (absorbed)", "BLUE")
    text(c, (px(2.05), ey0 - E(2.4) * es + 18), "net energy", "ACC")
    text(c, (px(1.55), eb - 2), "attraction (released)", "PINK")
    x0 = px(1.0)
    line(c, (x0, et), (x0, fb), "EDGE", 1, "3,4")
    text(c, (x0 + 6, ey0 - E(1) * es + 18), "minimum at a&#8320;")
    line(c, (70, fy0), (500, fy0)); line(c, (70, ft), (70, fb))
    text(c, (76, ft + 4), "Force", "HEAD", weight="700"); text(c, (500, fy0 - 6), "distance a", anchor="end")
    text(c, (440, fy0 - 56), "+ attraction"); text(c, (440, fy0 + 60), "− repulsion")
    curve(c, lambda a: 1 / a ** 2, xs, px, fy0, fs, ft, fb, "PINK", 1.6, "2,3")
    curve(c, lambda a: -1 / a ** (n + 1), xs, px, fy0, fs, ft, fb, "BLUE", 1.6, "9,5")
    curve(c, F, xs, px, fy0, fs, ft, fb, "ACC", 2.6)
    xm, ym = px(amax), fy0 - F(amax) * fs
    c.add(f'<circle cx="{xm:.1f}" cy="{ym:.1f}" r="4" fill="ACC"/>')
    text(c, (xm + 8, ym - 8), "maximum force", "ACC")
    text(c, (x0 + 6, fy0 + 16), "zero force at a&#8320;")
    REG.put("force-energy", c, "Energy and force between two ions versus distance",
            "Force and energy between two ions: the dotted line is the attraction part and the long-dashed line the repulsion part, "
            "the solid line is their sum. The net energy is lowest at the equilibrium distance a₀, where the net "
            "force is zero. Schematic curves, no numerical values")


def wells():
    X0, X1 = 0.82, 2.4
    xs = [X0 + (X1 - X0) * k / 240 for k in range(241)]
    px = lambda a: 60 + (a - X0) / (X1 - X0) * 430    # noqa: E731
    ti = lambda a: 1.0 * ((1 / a) ** 12 - 2 * (1 / a) ** 6)   # noqa: E731  deep, narrow
    al = lambda a: 0.55 * ((1 / a) ** 6 - 2 * (1 / a) ** 3)   # noqa: E731  shallow, wide
    y0, sc = 70, 150
    c = Canvas(540, 270)
    line(c, (60, y0), (500, y0)); line(c, (60, 16), (60, 250))
    text(c, (66, 24), "Energy", "HEAD", weight="700"); text(c, (500, y0 - 6), "distance", anchor="end")
    curve(c, al, xs, px, y0, sc, 16, 250, "BLUE", 2.4)
    curve(c, ti, xs, px, y0, sc, 16, 250, "ACC", 2.6)
    text(c, (px(1.12), y0 + 160), "Ti: deeper, narrower, steeper", "ACC")
    text(c, (px(1.55), y0 + 0.55 * 150 - 2), "Al: shallower, wider", "BLUE")
    REG.put("wells", c, "Schematic potential wells of titanium and aluminium",
            "Schematic potential wells: the deeper Ti minimum gives the higher melting temperature, the narrower "
            "trough the lower thermal expansion, the steeper walls the higher stiffness. Shapes only, no numerical values")


def build():
    tetrahedron()
    force_energy()
    wells()
    return REG
