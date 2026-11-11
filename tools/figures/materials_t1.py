"""Topic 1 figures: the tetrahedron and the ion-pair energy/force curves are copied from the slides as PNG (REG.raster);
the potential wells of Ti and Al are a drawn answer (EXTRA)."""
from figures.svgkit import Canvas, Registry, curve, line, text

REG = Registry("T1")


def rasters():
    REG.raster("tetrahedron", "The materials tetrahedron",
               "The four linked ideas of materials science, structure, properties, processing and applications, "
               "drawn as the corners of a tetrahedron: each one is connected to the other three. Copied from Session 2 Slide 2", 480)
    REG.raster("force-energy", "Potential energy and force of an ion pair against separation",
               "Top: potential energy U of an ion pair against the interatomic separation, with the repulsive energy E_r, "
               "the attractive energy E_A and their sum, the net energy E_N; its minimum, dU/dr = 0, is at the equilibrium "
               "separation r_o (a_0 in the text). Bottom: the attractive force F_A and the net force F_N (attraction positive), "
               "zero at r_o and with a maximum just beyond it. Copied from Session 2 Slide 8", 520)


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
            "trough the lower thermal expansion, the steeper walls the higher stiffness. Shapes only, no numerical values. Drawn answer to the question of Slide 39, not in the slides (EXTRA)")


def build():
    rasters()
    wells()
    return REG
