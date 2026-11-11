"""Topic 7 figures for Aerospace Materials I: magnetic and thermal properties (Session 15).

Schematic redraws of the slides (labels and qualitative shape kept, not to scale) plus PNG crops of the slides
for the charts and tables whose values cannot be redrawn faithfully (registered with `REG.raster`; the crops are
200 DPI clips of the PDF pages, written once to vault/attachments/T7). Run `python tools/build_topic_pages.py`
to write the SVG files to vault/attachments/T7.
"""
import math

from figures.svgkit import (Canvas, Registry, dot, line, poly, rect, sub, text)

REG = Registry("T7")


# ---------------------------------------------------------------- small helpers

def txt(c, x, y, s, col="TEXT", anchor="middle", size=13, weight="400"):
    text(c, (x, y), s, col, anchor, size, weight)


def axes(c, o, xend, yend, xl=None, yl=None, xdy=24):
    line(c, o, (xend, o[1]), "EDGE", 1.3, head=True)
    line(c, o, (o[0], yend), "EDGE", 1.3, head=True)
    if xl:
        text(c, (xend, o[1] + xdy), xl, "HEAD", "end", 13, "700")
    if yl:
        text(c, (o[0] + 8, yend + 4), yl, "HEAD", "start", 13, "700")


# ---------------------------------------------------------------- origin of magnetism (S3)

# ---------------------------------------------------------------- types of magnetism (S5-S13)

# ---------------------------------------------------------------- domains (S15) and magnetization (S16-S18)

def initial_magnetization():
    c = Canvas(700, 360)
    o = (80, 310)
    axes(c, o, 650, 30, "Magnetic field H", "Magnetization M (or B)")
    X, Y = 500.0, 240.0

    def f(t):
        t = max(0.0, min(1.0, t))
        return 0.10 * t + 0.90 * (3 * t * t - 2 * t ** 3)
    pts = [(o[0] + t * X, o[1] - Y * f(t)) for t in [i / 80 for i in range(0, 81)]]
    poly(c, pts, "PINK", 2.8)
    line(c, (o[0], o[1] - Y), (o[0] + X + 60, o[1] - Y), "EDGE", 1.0, "5,4")
    txt(c, o[0] + X + 64, o[1] - Y + 4, sub("M", "s"), "HEAD", "start", 14, "700")
    # line from the origin tangent to the curve (maximum of M/H): f(t)/t = f'(t) at t = 0.75, as drawn on the slide
    s_max = f(0.75) / 0.75
    line(c, o, (o[0] + 0.85 * X, o[1] - 0.85 * Y * s_max), "ACC", 1.6, "6,4")
    dot(c, (o[0] + 0.75 * X, o[1] - Y * f(0.75)), 4, "ACC", "ACC")
    line(c, o, (o[0] + 130, o[1] - 130 * Y * 0.10 / X), "BLUE", 2.4)
    txt(c, o[0] + 285, o[1] - 285 * Y * s_max / X - 16, "slope = maximum permeability " + sub("μ", "max"), "ACC", "end", 12, "700")
    txt(c, o[0] + 140, o[1] - 130 * Y * 0.10 / X - 6, "slope = initial permeability " + sub("μ", "i"), "BLUE", "start", 12, "700")
    for t in (0.12, 0.35, 0.62, 0.86):
        dot(c, (o[0] + t * X, o[1] - Y * f(t)), 4, "HEAD", "HEAD")
    txt(c, o[0] + 0.62 * X + 12, o[1] - Y * f(0.62) + 22, "growth of favourable domains", "TEXT", "start", 11)
    txt(c, o[0] + 0.96 * X, o[1] - Y * f(0.86) + 48, "rotation of domains: saturation", "TEXT", "middle", 11)
    txt(c, o[0] + 0.12 * X + 6, o[1] + 20, "random domains", "TEXT", "start", 11)
    REG.put("initial-magnetization", c, "Initial magnetization curve",
            "Magnetization against field starting from the demagnetized state: slow growth (initial permeability), fast growth of favourable domains (maximum permeability), rotation of domains and saturation Ms (schematic)")


def hysteresis_soft_hard():
    c = Canvas(700, 380)
    o = (350, 190)
    line(c, (60, o[1]), (650, o[1]), "EDGE", 1.3, head=True)
    line(c, (o[0], 360), (o[0], 20), "EDGE", 1.3, head=True)
    txt(c, 650, o[1] + 24, "H", "HEAD", "end", 14, "700")
    txt(c, o[0] + 10, 28, "B", "HEAD", "start", 14, "700")

    def loop(amp, hc, w, col, wd):
        es = [-300 + 4 * i for i in range(151)]
        shift = lambda e: hc * (1 - (e / 300) ** 2)   # the coercive shift fades out so both branches meet at saturation
        up = [(o[0] + e, o[1] - amp * math.tanh((e + shift(e)) / w)) for e in es]
        dn = [(o[0] + e, o[1] - amp * math.tanh((e - shift(e)) / w)) for e in es]
        poly(c, up, col, wd)
        poly(c, dn, col, wd)
        return amp * math.tanh(hc / w)
    Bs = 140.0
    br_h = loop(Bs, 150, 90, "PINK", 2.6)
    br_s = loop(105.0, 22, 14, "BLUE", 2.6)
    line(c, (o[0] + 100, o[1] - Bs), (640, o[1] - Bs), "EDGE", 1.0, "5,4")
    txt(c, 640, o[1] - Bs - 6, sub("B", "s") + " (hard)", "HEAD", "end", 13, "700")
    line(c, (o[0] + 100, o[1] - 105), (640, o[1] - 105), "EDGE", 1.0, "5,4")
    txt(c, 640, o[1] - 105 + 16, sub("B", "s") + " (soft)", "HEAD", "end", 13, "700")
    dot(c, (o[0], o[1] - br_s), 4, "HEAD", "HEAD")
    txt(c, o[0] + 8, o[1] - br_s + 16, sub("B", "r") + " (soft)", "HEAD", "start", 12, "700")
    dot(c, (o[0], o[1] - br_h), 4, "HEAD", "HEAD")
    txt(c, o[0] - 8, o[1] - br_h - 6, sub("B", "r") + " (hard)", "HEAD", "end", 12, "700")
    dot(c, (o[0] - 150, o[1]), 4, "HEAD", "HEAD")
    txt(c, o[0] - 150, o[1] + 40, "−" + sub("H", "c") + " (hard)", "HEAD", "middle", 12, "700")
    dot(c, (o[0] + 22, o[1]), 4, "HEAD", "HEAD")
    txt(c, o[0] + 30, o[1] + 20, sub("H", "c") + " (soft)", "HEAD", "start", 12, "700")
    txt(c, 160, 90, "Hard magnetic material", "PINK", "middle", 13, "700")
    txt(c, 160, 108, "wide loop, high " + sub("B", "r") + " and " + sub("H", "c"), "TEXT", "middle", 11)
    txt(c, 540, 290, "Soft magnetic material", "BLUE", "middle", 13, "700")
    txt(c, 540, 308, "narrow loop, low " + sub("H", "c") + ", high " + sub("μ", "i"), "TEXT", "middle", 11)
    txt(c, 540, 340, "limit between them: " + sub("H", "c") + " = 10 000 A/m", "ACC", "middle", 12, "700")
    REG.put("hysteresis-soft-hard", c, "Hysteresis loops of soft and hard magnetic materials",
            "B-H hysteresis loops: a soft material has a narrow loop (low coercivity Hc, high initial permeability), a hard material a wide one (high remanence Br, saturation Bs and Hc); the slide fixes the limit at Hc = 10 000 A/m (schematic)")


# ---------------------------------------------------------------- superconductors (S28-S29)

# ---------------------------------------------------------------- thermal expansion (S36, S39)

def _morse(r, r0=1.0, a=1.6):
    return (1 - math.exp(-a * (r - r0))) ** 2


def asymmetric_well():
    c = Canvas(700, 360)
    o = (70, 320)
    axes(c, o, 660, 30, "Interatomic distance r", "Potential energy")
    X0, X1 = 110.0, 600.0
    r_lo, r_hi = 0.27, 2.7
    PX = lambda r: X0 + (r - r_lo) / (r_hi - r_lo) * (X1 - X0)
    PY = lambda v: 300 - v * 215
    rs = [r_lo + i * (r_hi - r_lo) / 320 for i in range(321)]
    poly(c, [(PX(r), PY(_morse(r))) for r in rs if _morse(r) <= 1.25], "PINK", 2.8)
    # the harmonic approximation of this well: its second-order expansion at r0, a^2 (r - r0)^2 with a = 1.6
    harmonic = lambda r: 2.56 * (r - 1) ** 2
    poly(c, [(PX(r), PY(harmonic(r))) for r in rs if harmonic(r) <= 1.25], "BLUE", 1.8, "6,4")
    r0x = PX(1.0)
    line(c, (r0x, 36), (r0x, 308), "EDGE", 1.0, "4,4")
    txt(c, r0x, 338, sub("r", "0"), "HEAD", "middle", 13, "700")
    means = []
    for v, col in ((0.18, "GREEN"), (0.45, "ACC"), (0.78, "PINK")):
        lo = [r for r in rs if r < 1.0 and _morse(r) <= v][0]
        hi = [r for r in reversed(rs) if r > 1.0 and _morse(r) <= v][0]
        y = PY(v)
        line(c, (PX(lo), y), (PX(hi), y), col, 1.6)
        mx = (PX(lo) + PX(hi)) / 2
        dot(c, (mx, y), 4.5, col, col)
        means.append((mx, y))
    poly(c, means, "HEAD", 1.2, "3,3")
    txt(c, 530, 60, "asymmetric well:", "PINK", "start", 12, "700")
    txt(c, 530, 76, "the mean distance (dots)", "TEXT", "start", 11)
    txt(c, 530, 91, "grows with the energy,", "TEXT", "start", 11)
    txt(c, 530, 106, "so the solid expands", "TEXT", "start", 11)
    txt(c, 540, 150, "dashed: symmetric", "BLUE", "start", 12, "700")
    txt(c, 540, 165, "(harmonic) well,", "TEXT", "start", 11)
    txt(c, 540, 180, "mean stays at " + sub("r", "0"), "TEXT", "start", 11)
    REG.put("asymmetric-well", c, "Asymmetric interatomic potential well and thermal expansion",
            "Extension, not printed on the slides: because the real potential well is asymmetric, the mean interatomic distance grows with the vibration energy; a symmetric parabola would keep it at r0 (schematic)")


# ---------------------------------------------------------------- thermal conductivity (S40)

# ---------------------------------------------------------------- thermal stresses (S45, S47)

def thermal_shock():
    c = Canvas(720, 340)
    for k, ox in enumerate((40, 400)):
        txt(c, ox + 140, 28, "Rapid heating" if k == 0 else "Rapid cooling", "HEAD", "middle", 14, "700")
        rect(c, ox, 60, 110, 190, "HEAD", 1.6, None, "ATOM", 0.12)
        txt(c, ox + 55, 76, "surface", "TEXT", "middle", 11)
        txt(c, ox + 55, 160, "interior", "TEXT", "middle", 11)
        txt(c, ox + 55, 242, "surface", "TEXT", "middle", 11)
        # stress profile across the width, zero axis at x = ox + 210
        ax = ox + 210
        line(c, (ax, 56), (ax, 254), "EDGE", 1.2)
        sign = 1 if k == 0 else -1
        pts = []
        for i in range(0, 41):
            x = -1 + i / 20
            s = sign * (1 - 3 * x * x) / 2.0
            pts.append((ax + s * 70, 155 + x * 95))
        poly(c, pts, "ACC", 2.6)
        txt(c, ax + 70, 276, "tensile", "TEXT", "middle", 11)
        txt(c, ax - 70, 276, "compressive", "TEXT", "middle", 11)
        txt(c, ax, 48, "σ", "HEAD", "middle", 13, "700")
        txt(c, ox + 140, 300, ("outside hotter and expanded: compressive surface," if k == 0 else "outside colder and contracted: tensile surface,"), "TEXT", "middle", 11)
        txt(c, ox + 140, 316, ("tensile interior" if k == 0 else "compressive interior"), "TEXT", "middle", 11)
    REG.put("thermal-shock", c, "Thermal stresses from a temperature gradient",
            "Rapid heating makes the surface compressive and the interior tensile; rapid cooling reverses the signs. The stress profile is an extension, not printed on Slide 47 (schematic)")


# ---------------------------------------------------------------- slide crops (not generated here)

def rasters():
    REG.raster('orbital-spin', 'Orbital and spin magnetic moments',
               'Origin of the magnetic moment of an atom: the orbital moment of the electron moving around the nucleus and the spin moment of the electron spinning about its axis, copied from Session 15 Slide 3', 440)
    REG.raster('dipole-orderings-a', 'Diamagnetic material',
               'Diamagnetic material: no dipoles without a field (H = 0) and induced dipoles opposite to an applied field H, copied from Session 15 Slide 6', 460)
    REG.raster('dipole-orderings-b', 'Paramagnetic material',
               'Paramagnetic material: permanent dipoles randomly oriented without a field (H = 0) and aligned with an applied field H, copied from Session 15 Slide 8', 460)
    REG.raster('dipole-orderings-c', 'Ferromagnetic material',
               'Ferromagnetic material: dipoles parallel to each other with no applied field (H = 0), copied from Session 15 Slide 9', 260)
    REG.raster('dipole-orderings-d', 'Antiferromagnetic MnO',
               'Antiparallel alignment of the spin moments of the Mn2+ ions in manganese oxide, with the O2- ions in between, copied from Session 15 Slide 10', 280)
    REG.raster('dipole-orderings-e', 'Cations of a ferrite',
               'Ferrimagnetic ferrite: spin moments of the Fe2+ and Fe3+ ions in octahedral sites and of the Fe3+ ions in tetrahedral sites of the oxygen lattice, copied from Session 15 Slide 11', 340)
    REG.raster('dipole-orderings-f', 'Ferro-, antiferro- and ferrimagnetic dipoles',
               'Dipoles of the ferromagnetic (parallel), antiferromagnetic (antiparallel and equal) and ferrimagnetic (antiparallel and unequal) arrangements, copied from Session 15 Slide 13', 600)
    REG.raster('domain-closure', 'Origin of magnetic domains',
               'One domain (high magnetostatic energy), two domains, four domains and closure domains (zero magnetostatic energy), with the magnetic domain walls, copied from Session 15 Slide 15', 680)
    REG.raster('s15-initial-magnetization', 'Initial magnetization curve',
               'Magnetization M or induction B against the field H from the demagnetized state: initial permeability μi, maximum permeability μmax, growth of domains, rotation of domains and saturation, copied from Session 15 Slide 16', 400)
    REG.raster('s15-hysteresis-loops', 'Hysteresis loops of soft and hard materials',
               'B-H hysteresis loops of a soft magnetic material (narrow loop) and a hard magnetic material (wide loop), copied from Session 15 Slide 18', 320)
    REG.raster('superconductor-types-a', 'Type I superconductor',
               'Type I superconductor: resistivity zero in the superconducting state up to the critical field Hc, then an abrupt return to the normal state, copied from Session 15 Slide 28', 340)
    REG.raster('superconductor-types-b', 'Type II superconductor',
               'Type II superconductor: gradual transition between the lower critical field Hc1 and the upper critical field Hc2 (the vertical axis has no label on the slide), copied from Session 15 Slide 29', 320)
    REG.raster('bimetal-strip', 'Bimetallic strip',
               'Bimetallic strip of two metals with expansion coefficients α1 > α2: straight at T1 and bent at T2 > T1, copied from Session 15 Slide 39', 360)
    REG.raster('heat-flux-bar', 'Heat flux through a bar',
               'A bar heated at one end by a heat source: the heat flow Q crosses the area A down the temperature difference ΔT over the length Δx, copied from Session 15 Slide 40', 480)
    REG.raster('constrained-bar', 'Bar confined between two walls',
               'Bar confined between two rigid walls, so that its thermal expansion or contraction under a temperature change T is restrained, copied from Session 15 Slide 45', 380)
    REG.raster("s15-ferrite-garnet-tables", "Commercial ferrite and garnet compositions",
               "Some commercial ferrite and garnet compositions, copied from Session 15 Slide 12", 560)
    REG.raster("s15-domains-grains-bloch", "Domains in a grain and a Bloch wall",
               "A grain with domains, a single-domain small grain and a Bloch wall between two domains, copied from Session 15 Slide 14", 560)
    REG.raster("s15-domains-iron", "Domain pattern in an iron single crystal film",
               "Domain pattern observed in a (001) iron single crystal film 2500 Å thick, copied from Session 15 Slide 14", 300)
    REG.raster("s15-curie-temperature-chart", "Saturation magnetization against temperature for iron and magnetite",
               "Saturation magnetization and saturation flux density against temperature for pure Fe and Fe3O4, which vanish at the Curie temperature, copied from Session 15 Slide 23", 460)
    REG.raster("s15-typical-properties-tables", "Properties of selected soft, hard and recording magnetic materials",
               "Properties of selected soft magnetic materials, hard (permanent) magnetic materials and magnetic recording powders, copied from Session 15 Slide 24", 720)
    REG.raster("s15-superconducting-envelope", "Superconducting critical surface of Nb3Sn",
               "Superconducting envelope: the combined effect of temperature, magnetic field and current density on a Nb3Sn superconductor (Bc2 = 24.5 T, Tc = 18 K, Jc = 10^7 A/cm2), copied from Session 15 Slide 26", 640)
    REG.raster("s15-heat-capacity-chart", "Heat capacity against temperature for metals and ceramics",
               "Heat capacity as a function of temperature for metals and ceramics, levelling off near 6 cal/(mol·K) above the Debye temperature, copied from Session 15 Slide 35", 380)
    REG.raster("s15-expansion-bonding-curves", "Potential energy curves, weak and strong bonding",
               "Interatomic energy curves: the spacing grows when the vibration energy grows, and more for weak than for strong bonding; the same slide plots the potential well at several vibrational energies, copied from Session 15 Slide 36", 700)
    REG.raster("s15-expansion-iron-melting", "Thermal expansion of iron and of metals against melting temperature",
               "Linear coefficient of thermal expansion of iron against temperature (abrupt changes at the allotropic transformations) and of metals at 25 °C against melting temperature, copied from Session 15 Slide 37", 700)
    REG.raster("s15-properties-table", "Specific heat, thermal expansion and thermal conductivity of materials",
               "Specific heat cp, linear expansion coefficient and thermal conductivity k of metals, ceramics and polymers (Invar and Super Invar boxed on the slide), copied from Session 15 Slide 38", 420)
    REG.raster("s15-conductivity-table", "Thermal conductivity of metals, alloys, ceramics and polymers",
               "Thermal conductivity in W/(m·K) of pure metals, alloys, ceramics and polymers, copied from Session 15 Slide 41", 420)
    REG.raster("s15-conductivity-temperature", "Thermal conductivity against temperature",
               "Effect of temperature on the thermal conductivity of several materials (platinum, aluminium, iron, SiC, Al2O3, glass, firebrick), copied from Session 15 Slide 42", 380)
    REG.raster("s15-conductivity-cuzn", "Thermal conductivity of Cu-Zn alloys",
               "Thermal conductivity of Cu-Zn alloys against zinc content: alloying lowers the thermal conductivity, copied from Session 15 Slide 43", 340)


def theory():
    initial_magnetization()
    hysteresis_soft_hard()
    asymmetric_well()
    thermal_shock()
    rasters()


def build():
    theory()
    return REG
