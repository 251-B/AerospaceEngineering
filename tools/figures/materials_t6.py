"""Topic 6 figures for Aerospace Materials I: electrical properties (Session 13).

PNG crops of the slides (registered with `REG.raster`) plus the few drawings that have no figure on the slides
(conductivity scale, bar of Ohm's law, band-gap trends, cubic BaTiO3 cell).
The figures of the solved problems live in tools/figures/materials_t6_problems.py and are added to the same
registry by `build()`. Run `python tools/build_topic_pages.py` (theory) or `python tools/build_materials_problems.py`
(problems) to write the SVG files to vault/attachments/T6.
"""
import importlib.util

from figures.svgkit import Canvas, Registry, arrow, circle, dim, line, rect, sub, text

REG = Registry("T6")


# ---------------------------------------------------------------- small helpers

def sup(base, s):
    return sub(base, s, True)


def txt(c, x, y, s, col="TEXT", anchor="middle", size=13, weight="400"):
    text(c, (x, y), s, col, anchor, size, weight)


# ---------------------------------------------------------------- bands of solids (S3-S8)

def conductivity_scale():
    c = Canvas(700, 260)
    x0, k = 40, 21.0

    def X(e):
        return x0 + (e + 20) * k
    for e in range(-20, 9, 4):
        line(c, (X(e), 212), (X(e), 218), "EDGE", 1.1)
        txt(c, X(e), 234, sup("10", "−" + str(-e)) if e < 0 else (sup("10", str(e)) if e else "1"), "TEXT", "middle", 12)
    line(c, (x0 - 10, 212), (X(9), 212), "EDGE", 1.3, head=True)
    txt(c, X(9) + 4, 250, "σ in (Ω·m)" + "⁻¹" + " (logarithmic scale)", "HEAD", "end", 12, "700")
    rows = [(-20, -10, 66, "ATOM"), (-6, 4, 116, "GREEN"), (6.5, 7.5, 166, "PINK")]
    for a, b, y, col in rows:
        rect(c, X(a), y, X(b) - X(a), 28, col, 1.5, None, col, 0.35)
    txt(c, X(-10) + 10, 85, "Insulators: 10⁻²⁰ to 10⁻¹⁰, e.g. polyethylene", "HEAD", "start", 13, "700")
    txt(c, X(-6) - 10, 135, "Semiconductors: 10⁻⁶ to 10⁴, e.g. Si, Ge", "HEAD", "end", 13, "700")
    txt(c, X(6.5) - 10, 185, "Conductors: about 10⁷, e.g. metals", "HEAD", "end", 13, "700")
    REG.put("conductivity-scale", c, "Classification of materials by electrical conductivity",
            "Insulators, semiconductors and conductors on a logarithmic conductivity scale, drawn for this page from the table of Session 13 Slide 5 (the slide gives the ranges only as a table; schematic, not to scale)")


# ---------------------------------------------------------------- metallic conductors (S10-S17)

def ohm_geometry():
    c = Canvas(640, 310)
    rect(c, 150, 110, 300, 80, "HEAD", 1.8, None, "ATOM", 0.18)
    c.add('<ellipse cx="450" cy="150" rx="16" ry="40" fill="none" stroke="HEAD" stroke-width="1.8"/>')
    arrow(c, (60, 150), (146, 150), "BLUE", 2.4, 11)
    arrow(c, (466, 150), (560, 150), "BLUE", 2.4, 11)
    txt(c, 100, 140, "I", "BLUE", "middle", 15, "700")
    txt(c, 520, 140, "I", "BLUE", "middle", 15, "700")
    arrow(c, (175, 132), (400, 132), "GREEN", 2.2, 10)
    txt(c, 288, 125, "E", "GREEN", "middle", 14, "700")
    arrow(c, (175, 170), (400, 170), "PINK", 2.2, 10)
    txt(c, 288, 187, "J", "PINK", "middle", 14, "700")
    dim(c, (150, 80), (450, 80), "V = E l", "TEXT", (0, -8))
    dim(c, (150, 222), (450, 222), "l", "TEXT", (0, 18))
    txt(c, 490, 106, "A", "HEAD", "start", 14, "700")
    line(c, (486, 110), (466, 128), "EDGE", 1.0)
    txt(c, 320, 264, "J = σ E,   σ = 1/ρ,   R = V / I = ρ l / A", "HEAD", "middle", 14, "700")
    txt(c, 320, 286, "(I = J A and V = E l give R = l / (σ A))", "TEXT", "middle", 12)
    REG.put("ohm-geometry", c, "Ohm's law and the geometry of a conductor",
            "A bar of length l and cross-section A carries a current I under a voltage V: E = V/l, J = I/A, so R = ρ l / A. Drawn for this page: the slide only writes I = V/R (schematic)")


# ---------------------------------------------------------------- non-metallic conductors (S21-S22)

# ---------------------------------------------------------------- semiconductors (S27-S44)

def compound_trend():
    c = Canvas(700, 300)
    rect(c, 30, 60, 210, 46, "HEAD", 1.6, None, "ATOM", 0.25, 6)
    txt(c, 135, 88, "Si    " + sub("E", "g") + " = 1.1 eV", "HEAD", "middle", 14, "700")
    arrow(c, (135, 112), (135, 158), "ACC", 2.4, 11)
    txt(c, 148, 140, "atom size increases", "ACC", "start", 12)
    rect(c, 30, 164, 210, 46, "HEAD", 1.6, None, "ATOM", 0.25, 6)
    txt(c, 135, 192, "Ge    " + sub("E", "g") + " = 0.67 eV", "HEAD", "middle", 14, "700")
    txt(c, 135, 236, sub("E", "g") + " decreases, σ increases", "TEXT", "middle", 12)
    txt(c, 135, 42, "Group 14, covalent bonds", "HEAD", "middle", 13, "700")
    # right
    arrow(c, (500, 78), (300, 78), "GREEN", 3.0, 12)
    arrow(c, (500, 78), (680, 78), "PINK", 3.0, 12)
    txt(c, 300, 66, "more covalent", "GREEN", "start", 13, "700")
    txt(c, 680, 66, "more ionic", "PINK", "end", 13, "700")
    for x, l1, l2 in ((300, "Group 14", "Si, Ge"), (430, "Groups 13-15", "GaAs, InSb"), (560, "Groups 12-16", "CdS, ZnTe")):
        rect(c, x, 100, 120, 52, "HEAD", 1.5, None, "ATOM", 0.18, 6)
        txt(c, x + 60, 122, l1, "TEXT", "middle", 12)
        txt(c, x + 60, 141, l2, "HEAD", "middle", 13, "700")
    arrow(c, (300, 196), (680, 196), "BLUE", 2.4, 11)
    txt(c, 490, 186, sub("E", "g") + " increases", "BLUE", "middle", 13, "700")
    arrow(c, (300, 250), (680, 250), "PINK", 2.4, 11)
    txt(c, 490, 240, "σ decreases (intrinsic semiconductors)", "PINK", "middle", 13, "700")
    REG.put("compound-trend", c, "Band gap trends in intrinsic semiconductors",
            "Trends of the band gap: it falls as the atom size grows in group 14 and rises as the bonding becomes less covalent and more ionic; the conductivity follows the opposite trend. Drawn for this page from the statements of Session 13 Slides 31 and 32, which give these trends in words (schematic)")


# ---------------------------------------------------------------- applications (S45-S49)

# ---------------------------------------------------------------- dielectrics (S51-S53)

def batio3_cell_extra():
    c = Canvas(340, 340)

    def cube(x0, y0, s, h, dx, dy, ti_shift, o_shift, title):
        F = [(x0, y0), (x0 + s, y0), (x0 + s, y0 + h), (x0, y0 + h)]
        B = [(a + dx, b + dy) for a, b in F]
        for k in range(4):
            line(c, F[k], F[(k + 1) % 4], "HEAD", 1.8)
            line(c, F[k], B[k], "EDGE", 1.2, "4,3" if k == 3 else None)
        for k in range(4):
            line(c, B[k], B[(k + 1) % 4], "EDGE", 1.2, "4,3")
        for p_ in F + B:
            circle(c, p_, 8, "ACC", 1.4, None, "ACC", 0.8)
        faces = [(x0 + s / 2, y0 + h / 2), (x0 + s / 2 + dx, y0 + h / 2 + dy), (x0 + dx / 2, y0 + h / 2 + dy / 2),
                 (x0 + s + dx / 2, y0 + h / 2 + dy / 2), (x0 + s / 2 + dx / 2, y0 + dy / 2), (x0 + s / 2 + dx / 2, y0 + h + dy / 2)]
        for p_ in faces:
            circle(c, (p_[0], p_[1] + o_shift), 5, "PINK", 1.4, None, "PINK", 0.8)
        ctr = (x0 + s / 2 + dx / 2, y0 + h / 2 + dy / 2 + ti_shift)
        circle(c, ctr, 6.5, "HEAD", 1.6, None, "HEAD", 0.9)
        txt(c, x0 + s / 2 + dx / 2, y0 + h + 52, title, "HEAD", "middle", 13, "700")
    cube(60, 100, 110, 110, 44, -44, 0, 0, "T &gt; 120 °C: cubic")
    txt(c, 160, 288, "no permanent dipole", "TEXT", "middle", 12)
    # legend
    circle(c, (60, 322), 7, "ACC", 1.4, None, "ACC", 0.8)
    txt(c, 74, 326, "Ba²⁺", "TEXT", "start", 12)
    circle(c, (140, 322), 6, "HEAD", 1.4, None, "HEAD", 0.9)
    txt(c, 152, 326, "Ti⁴⁺", "TEXT", "start", 12)
    circle(c, (220, 322), 5, "PINK", 1.4, None, "PINK", 0.8)
    txt(c, 232, 326, "O²⁻", "TEXT", "start", 12)
    txt(c, 170, 24, "BaTiO" + sub("", "3") + " above the Curie temperature", "HEAD", "middle", 13, "700")
    REG.put("batio3-cell-extra", c, "BaTiO3 cubic cell above the Curie temperature",
            "BaTiO3 above the Curie temperature (120 °C): cubic cell with the Ti4+ ion at the centre, so there is no permanent dipole. Drawn for this page: the slide states the cubic structure in words and draws only the tetragonal cell of the next figure (schematic)")


# ---------------------------------------------------------------- slide crops (not generated here)

def rasters():
    REG.raster("band-formation", "Formation of energy bands",
               "Energy levels broaden into bands as the number of atoms grouped together increases: one atom, two atoms, a small number of atoms and a solid, with the band gap Eg and the core-level electrons (Figure 19-2 of the slide, courtesy of John Bravman), copied from Session 13 Slide 3", 620)
    REG.raster("bands-vs-spacing", "Energy bands against inter-atomic distance",
               "Conduction and valence bands widening as the inter-atomic distance decreases, with the equilibrium inter-atomic distance marked, copied from Session 13 Slide 4", 520)
    REG.raster("band-types-a", "Band structure of conductors",
               "Band structure of conductors: A1) half-filled valence band (one s electron: Na, Cu, Al) and A2) overlapping filled 3s and empty 3p bands (Mg), with the Fermi energy Ef, copied from Session 13 Slide 6", 640)
    REG.raster("band-types-b", "Band structure of semiconductors and insulators",
               "Band structure of semiconductors (narrow gap, below 2 eV: Si 1.1 eV, Ge 0.67 eV) and insulators (large gap, above 2 eV: diamond 6-7 eV), copied from Session 13 Slide 8", 640)
    REG.raster("electron-drift-a", "Electron path with scattering events",
               "Path of a conduction electron under a field E, with the scattering events and the net electron motion, copied from Session 13 Slide 10", 380)
    REG.raster("electron-drift-b", "Drift velocity against time",
               "Electron drift velocity against time in the classical model of a free electron in a metal: it grows between collisions and falls back at each one, with the maximum and average values vmax and vav, copied from Session 13 Slide 11", 520)
    REG.raster("matthiessen", "Matthiessen's rule",
               "Electrical resistivity against temperature: the temperature component ρT on top of the residual component ρr, copied from Session 13 Slide 14", 400)
    REG.raster("scattering-sources", "Movement of an electron through a crystal",
               "Movement of an electron through (a) a perfect crystal, (b) a crystal heated to a high temperature and (c) a crystal containing atomic-level defects, copied from Session 13 Slide 17", 460)
    REG.raster("graphene-lattice-a", "Graphene lattice",
               "Graphene: a single layer of carbon atoms on a hexagonal lattice, copied from Session 13 Slide 21", 360)
    REG.raster("graphene-lattice-b", "σ bonds and π cloud of graphene",
               "The σ bonds in the plane and the π cloud of delocalised electrons above and below it, copied from Session 13 Slide 21", 360)
    REG.raster("ionic-conduction-a", "Movement of ions or of vacancies",
               "Ionic conduction by the movement of ions or, equivalently, of vacancies, copied from Session 13 Slide 22", 260)
    REG.raster("ionic-conduction-b", "Interstitial cation",
               "Ionic conduction by a small cation (ri smaller than ratom) moving through the interstitial voids, copied from Session 13 Slide 22", 200)
    REG.raster("intrinsic-excitation", "Excitation in an intrinsic semiconductor",
               "Intrinsic semiconductor before and after excitation: an electron excited across the gap Eg becomes a free electron in the conduction band and leaves a hole in the valence band, so both a free electron and a hole are generated, copied from Session 13 Slide 27", 640)
    REG.raster("donor-level", "Donor level in an n-type semiconductor",
               "n-type semiconductor: the donor level Ed just below the conduction band Ec, with ΔE = Ec − Ed, and the table of groups 4A and 5A of the periodic table, copied from Session 13 Slide 36", 560)
    REG.raster("acceptor-level", "Acceptor level in a p-type semiconductor",
               "p-type semiconductor: the acceptor level Ea just above the valence band Ev, with ΔE = Ea − Ev, the electron and the positive hole, and the table of groups 3A and 4A of the periodic table, copied from Session 13 Slide 37", 560)
    REG.raster("extrinsic-temperature", "Effect of temperature on an extrinsic semiconductor",
               "ln σ against 1/T of an extrinsic semiconductor: intrinsic range at high temperature (slope −Eg/2k), exhaustion range and extrinsic range at low temperature (slope printed −(Ec − Ed)/k), copied from Session 13 Slide 43", 420)
    REG.raster("photoconductivity-a", "Photoconductivity and the photovoltaic cell",
               "Photoconductivity: a photon hν lifts an electron across the gap Eg, and the photovoltaic cell (emitter, base, contacts, external load) in which sunlight creates electron-hole pairs, copied from Session 13 Slide 46", 680)
    REG.raster("photoconductivity-b", "Absorption thresholds of Si, GaAs and AlGaAs",
               "Silicon absorbs photons above 1.1 eV, gallium arsenide above 1.43 eV and aluminium gallium arsenide above 1.7 eV; photons of lower energy go through, copied from Session 13 Slide 46", 460)
    REG.raster("led-recombination", "Light-emitting diode",
               "LED: forward-biased p-n junction and its band diagram, where electrons and holes recombine and emit light, copied from Session 13 Slide 47", 360)
    REG.raster("dipole-polarization-a", "Dipole moment",
               "Dipole moment p of two charges −q and +q a distance d apart, copied from Session 13 Slide 51", 260)
    REG.raster("dipole-polarization-b", "Unpolarised and polarised dielectric",
               "Dielectric unpolarised (random dipoles) and polarised by an applied electric field, copied from Session 13 Slide 51", 380)
    REG.raster("capacitor-dielectric", "Parallel-plate capacitor with a dielectric",
               "Parallel-plate capacitor with vacuum between the plates (charges ±Q0) and with a dielectric, whose surface charges ∓Q' let the plates hold Q0 + Q', copied from Session 13 Slide 52", 680)
    REG.raster("loss-factor", "Dipoles in an alternating field",
               "Dipoles of a dielectric realigning when the field between the plates changes sign, the origin of the loss factor tan δ, copied from Session 13 Slide 53", 400)
    REG.raster("ferro-hysteresis", "Ferroelectric hysteresis loop",
               "Polarisation against electric field of a ferroelectric: saturation polarisation Ps, remanent polarisation Pr, non-remanent polarisation and coercive field Ec, copied from Session 13 Slide 56", 520)
    REG.raster("piezo-effects-a", "Direct piezoelectric effect",
               "Direct piezoelectric effect: an external stress deforms the crystal structure, alters the dipoles and generates an electric field, copied from Session 13 Slide 58", 340)
    REG.raster("piezo-effects-b", "Reverse piezoelectric effect",
               "Reverse piezoelectric effect (electrostriction): an external electric field alters the dipoles and deforms the crystal structure (tension or compression), copied from Session 13 Slide 58", 400)
    REG.raster("s13-resistivity-table", "Resistivity at 0 degrees C and temperature coefficient of selected metals",
               "Resistivity at 0 °C and temperature coefficient of resistivity of aluminium, copper, gold, iron and silver, copied from Session 13 Slide 14", 460)
    REG.raster("s13-resistivity-metals-chart", "Resistivity against temperature of selected metals",
               "Effect of temperature on the electrical resistivity of selected metals, copied from Session 13 Slide 14", 520)
    REG.raster("s13-matthiessen-copper", "Resistivity of copper and Cu-Ni alloys against temperature",
               "Resistivity against temperature of pure, alloyed (Cu + Ni) and deformed copper, showing the thermal, impurity and deformation parts, copied from Session 13 Slide 17", 520)
    REG.raster("s13-impurity-copper", "Effect of impurities on the resistivity of copper",
               "Effect of small additions of various elements on the room-temperature electrical resistivity of copper, copied from Session 13 Slide 16", 400)
    REG.raster("s13-hardening-conductivity", "Yield strength and conductivity against cold work and zinc content",
               "Yield strength and electrical conductivity against percent cold work (left) and percent Zn (right), copied from Session 13 Slide 18", 700)
    REG.raster("s13-intrinsic-charts", "Conductivity of an intrinsic semiconductor against temperature",
               "Electrical conductivity against temperature (left) and against 1/T with the slope −Eg/2k (right) of an intrinsic semiconductor, copied from Session 13 Slide 29", 620)
    REG.raster("s13-si-ge-table", "Properties of silicon and germanium",
               "Energy gap, mobilities, intrinsic carrier density, intrinsic resistivity and density of Si and Ge, copied from Session 13 Slide 31", 640)
    REG.raster("s13-semiconductor-table", "Band gap, conductivity and mobilities of intrinsic semiconductors",
               "Band gap, electrical conductivity and mobilities of Si, Ge, GaP, GaAs, InSb, CdS and ZnTe, copied from Session 13 Slide 33", 640)
    REG.raster("s13-dopant-levels", "Donor and acceptor energy gaps in silicon and germanium",
               "Donor and acceptor energy gaps (in eV) when silicon and germanium are doped, copied from Session 13 Slide 40", 640)
    REG.raster("s13-dopant-solubility", "Maximum solid solubility of dopants in silicon and germanium",
               "Maximum solid solubility of some dopants in Si and Ge, copied from Session 13 Slide 40", 460)
    REG.raster("s13-mobility-silicon", "Mobility of electrons and holes in silicon against dopant concentration",
               "Dependence of the room-temperature electron and hole mobilities on the dopant concentration for Si, copied from Session 13 Slide 42", 480)
    REG.raster("s13-thermistor", "Conductivity of aluminium and germanium against temperature",
               "Electrical conductivity against temperature of aluminium (reducing mobility) and germanium (increasing charge carriers), the basis of thermistors, copied from Session 13 Slide 48", 420)
    REG.raster("s13-pn-depletion-bands", "The p-n junction: carriers, depletion layer and energy bands",
               "The p-n junction as drawn on Session 13 Slide 45: (1) holes and electrons on both sides, (2) the depletion layer with its internal electric field, (3) the band bending with the diffusion potential, copied from the slide", 440)
    REG.raster("s13-batio3-dimensions", "BaTiO3 cell dimensions and ion displacements",
               "BaTiO3 unit cell with its dimensions (0.403 nm by 0.398 nm) and, on the right, the displacements of the ions in the tetragonal phase (0.006 nm and 0.009 nm), copied from Session 13 Slide 56", 480)


def theory():
    conductivity_scale()
    ohm_geometry()
    compound_trend()
    batio3_cell_extra()
    rasters()


def build():
    theory()
    if importlib.util.find_spec("figures.materials_t6_problems") is not None:
        from figures import materials_t6_problems
        materials_t6_problems.problems(REG)
    return REG
