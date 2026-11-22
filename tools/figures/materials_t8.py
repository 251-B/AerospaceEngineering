"""Topic 8 figures for Aerospace Materials I: ceramic materials (Sessions 16 and 18) and the problem sheet T8.

Screenshot-First: every figure of this topic is a PNG crop of a slide or of the problem sheet (registered with
`REG.raster`; the crops are 200 DPI clips of the PDF pages, written once to vault/attachments/T8).
"""
from figures.svgkit import Registry

REG = Registry("T8")


def rasters():
    REG.raster('s16-general-properties-diagram', 'General properties of ceramics',
               'Mind map of the general properties: hard and brittle, low electrical and thermal conductivity, high compressive strength, high melting point, chemical stability, copied from Session 16 Slide 2', 720)
    REG.raster('s16-pauling-ionic-character', 'Ionic and covalent character',
               "Ionic, mixed and covalent bonds, with Pauling's relation for the percentage of ionic character, copied from Session 16 Slide 5", 720)
    REG.raster('s16-coordination-stability', 'Stability of a cation among anions',
               'A cation too small for its cage of anions is unstable; one that touches all its anions is stable, copied from Session 16 Slide 6', 720)
    REG.raster('s16-cscl-unit-cell', 'Caesium chloride cell',
               'Cl⁻ at the corners and Cs⁺ at the centre: simple cubic with two ions, not BCC, copied from Session 16 Slide 7', 560)
    REG.raster('s16-nacl-structure', 'Rock salt structure',
               'FCC chloride anions with the sodium cations in all the octahedral holes, copied from Session 16 Slide 8', 720)
    REG.raster('s16-zincblende-structure', 'Zinc blende structure',
               'FCC S²⁻ with Zn²⁺ in half of the tetrahedral sites, copied from Session 16 Slide 9', 560)
    REG.raster('s16-fluorite-structure', 'Fluorite structure',
               'FCC Ca²⁺ with F⁻ in all the tetrahedral sites, copied from Session 16 Slide 10', 720)
    REG.raster('s16-anti-fluorite-structure', 'Anti-fluorite structure',
               'FCC O²⁻ with Li⁺ in all the tetrahedral sites (Li₂O), copied from Session 16 Slide 11', 420)
    REG.raster('s16-perovskite-cell', 'Perovskite cell',
               'Ca²⁺ at the corners, O²⁻ at the face centres, Ti⁴⁺ at the body centre, copied from Session 16 Slide 12', 420)
    REG.raster('s16-tio6-octahedra', 'TiO₆ octahedra',
               'Corner-sharing TiO₆ octahedra of the perovskite framework, copied from Session 16 Slide 12', 420)
    REG.raster('s16-corundum-hcp-cell', 'Corundum cell',
               'HCP O²⁻ with Al³⁺ in two thirds of the octahedral sites, copied from Session 16 Slide 13', 420)
    REG.raster('s16-corundum-oxygen-layers', 'Corundum layers',
               'Close-packed O²⁻ layer with two thirds of the octahedral sites filled by Al³⁺, and the cell six layers high, copied from Session 16 Slide 13', 720)
    REG.raster('s16-summary-crystal-structures-table', 'Common ceramic crystal structures',
               'Structure type, anion packing, coordination numbers and examples of five structures, copied from Session 16 Slide 14', 720)
    REG.raster('s16-diamond-cell', 'Diamond cubic cell',
               'Interior atoms a quarter of the way along the body diagonals; two atoms per lattice point, copied from Session 16 Slide 15', 560)
    REG.raster('s16-sic-cluster', 'SiC structure',
               'Diamond-type tetrahedral network of silicon carbide, copied from Session 16 Slide 15', 560)
    REG.raster('s16-si3n4-structure', 'Si₃N₄ structure',
               'SiN₄ tetrahedron and the repeated layer of β-Si₃N₄, copied from Session 16 Slide 15', 560)
    REG.raster('s16-specific-moduli-table', 'Specific moduli',
               'Modulus, density and specific modulus of ceramics compared with metals, copied from Session 16 Slide 16', 720)
    REG.raster('s16-stress-strain-alumina-glass', 'Stress-strain of alumina and glass',
               'Linear curves to fracture of aluminium oxide and glass, copied from Session 16 Slide 16', 420)
    REG.raster('s16-brittle-stress-strain', 'Brittle stress-strain curve',
               'A ceramic breaks at the end of the elastic line, with no plastic strain, copied from Session 16 Slide 17', 420)
    REG.raster('s16-porosity-flexural-strength', 'Strength against porosity',
               'Flexural strength falls steeply with the volume fraction of porosity, copied from Session 16 Slide 17', 560)
    REG.raster('s16-porosity-elastic-modulus', 'Modulus against porosity',
               'Elastic modulus falls to zero as the porosity tends to 1, copied from Session 16 Slide 17', 560)
    REG.raster('s16-tension-test-cracks', 'Cracks in tension',
               'Under tension one crack propagates unstably and the specimen fails at low stress, copied from Session 16 Slide 18', 560)
    REG.raster('s16-compression-test-cracks', 'Cracks in compression',
               'Under compression the cracks propagate stably and the strength is much higher, copied from Session 16 Slide 18', 560)
    REG.raster('s16-three-point-bending', 'Three-point bending test',
               'Load at mid-span between supports, with rectangular and circular sections, copied from Session 16 Slide 19', 560)
    REG.raster('s16-weibull-strength-distribution', 'Weibull distribution of strength',
               'Frequency of fracture against strength for a ceramic, copied from Session 16 Slide 20', 420)
    REG.raster('s16-thermal-shock-expansion', 'Thermal shock by restricted expansion',
               'A bar held between walls cracks when heated exactly as if it had expanded freely and then been compressed back to its length, copied from Session 16 Slide 21', 520)
    REG.raster('s16-tempering-stress-profile', 'Stress profile of a sheet cooled from its surfaces',
               'Stress profile across a sheet before and after tempering: zero at high temperature, then compression at the surfaces and tension inside after heat extraction, copied from Session 16 Slide 21', 480)
    REG.raster('s16-batio3-cell', 'BaTiO₃ cell',
               'Tetragonal cell with the Ti⁴⁺ and O²⁻ ions displaced, giving an electric dipole, copied from Session 16 Slide 22', 560)
    REG.raster('s16-earth-crust-abundance', "Elements of the earth's crust",
               "Percentage of each element in the earth's crust: oxygen and silicon dominate, copied from Session 16 Slide 23", 420)
    REG.raster('s16-silicate-compositions-table', 'Compositions of silicate ceramics',
               'Approximate compositions of refractories, porcelains and Portland cement (Table 8.1), copied from Session 16 Slide 23', 560)
    REG.raster('s16-sio4-tetrahedron', 'SiO₄ tetrahedron',
               'Si at the centre and O at the corners: the basic unit of the silicates, copied from Session 16 Slide 24', 420)
    REG.raster('s16-silicate-structure-types', 'Classification of silicates',
               'Island, ring, chain, sheet and 3D arrangements of the tetrahedra, copied from Session 16 Slide 25', 560)
    REG.raster('s16-silicate-mineral-specimens', 'Silicate minerals',
               'Forsterite, enstatite and kaolinite, copied from Session 16 Slide 25', 420)
    REG.raster('s16-silica-phase-diagram', 'Phase diagram of silica',
               'Quartz, tridymite, cristobalite and liquid against temperature and pressure (labels in Spanish), copied from Session 16 Slide 26', 420)
    REG.raster('s16-silica-crystal-cell', 'Silica cell',
               'Crystal cell of silica with Si⁴⁺ and O²⁻, copied from Session 16 Slide 26', 420)
    REG.raster('s16-volume-temperature-glass', 'Volume against temperature',
               'A crystal contracts abruptly at Tm; a glass bends away from the supercooled liquid at Tg, copied from Session 16 Slide 27', 420)
    REG.raster('s16-glass-constituents-diagram', 'Constituents of silicate glasses',
               'Glass formers, modifiers and intermediates, with their roles, copied from Session 16 Slide 28', 560)
    REG.raster('s16-glass-types-composition-table', 'Compositions of glasses',
               'Composition, characteristics and applications of common glasses, copied from Session 16 Slide 29', 560)
    REG.raster('s16-thermal-shock-resistance-table', 'Thermal shock of glasses',
               'Expansion coefficient and thermal shock to failure of glasses and glass-ceramics (Table ST1), copied from Session 16 Slide 31', 560)
    REG.raster('s16-glass-ceramic-microstructure', 'Glass, glass-ceramic and ceramic',
               'Microstructures and micrographs of a glass, a glass-ceramic and a ceramic, copied from Session 16 Slide 32', 560)
    REG.raster('s16-glass-ceramic-hob-photo', 'Glass-ceramic cooktop',
               'A glass-ceramic hob, an application of thermal shock resistance, copied from Session 16 Slide 32', 560)
    REG.raster('s18-ceramic-classification', 'Ceramics need adapted processing',
               'High melting point and brittleness call for adapted processing routes; classification by final properties, copied from Session 18 Slide 4', 560)
    REG.raster('s18-ceramic-raw-materials-branch', 'Raw materials',
               'Synthesis for advanced ceramics; clay, silica and feldspar for traditional ceramics, copied from Session 18 Slide 5', 560)
    REG.raster('s18-powder-solution-tubes', 'Liquid-phase synthesis',
               'Solution, suspension and precipitate, copied from Session 18 Slide 6', 420)
    REG.raster('s18-milling-methods', 'Milling methods',
               '(a) Roll crushing, (b) ball milling, (c) hammer milling, copied from Session 18 Slide 7', 720)
    REG.raster('s18-granulation-stages', 'Granulation',
               'Spraying, wetting, solidifying and drying of a slurry into granules, copied from Session 18 Slide 8', 420)
    REG.raster('s18-spray-dryer-granules', 'Spray dryer',
               'Slurry sprayed into hot air gives spherical granules, copied from Session 18 Slide 8', 560)
    REG.raster('s18-shaping-classification', 'Shaping methods',
               'Dry, wet (colloidal), plastic and free-form shaping methods, copied from Session 18 Slide 9', 720)
    REG.raster('s18-uniaxial-pressing-stages', 'Uniaxial pressing',
               'Charging the die, compaction and ejection, copied from Session 18 Slide 10', 560)
    REG.raster('s18-cip-wet-bag', 'Cold isostatic pressing, wet bag',
               'Wet-bag cold isostatic pressing: a rubber mould filled with powder immersed in the pressure medium of the high-pressure vessel, copied from Session 18 Slide 12', 420)
    REG.raster('s18-cip-dry-bag', 'Dry-bag isostatic pressing',
               'Powder in a forming rubber mould inside a pressure vessel, copied from Session 18 Slide 12', 420)
    REG.raster('s18-cip-spark-plug-stages', 'Isostatic pressing of a spark plug insulator',
               'Powder filling, compaction, depressurization and withdrawal, copied from Session 18 Slide 13', 560)
    REG.raster('s18-colloid-stability', 'Stable and unstable colloids',
               'A stable slip stays dispersed; an unstable one aggregates and sediments, copied from Session 18 Slide 14', 560)
    REG.raster('s18-slip-casting-steps', 'Slip casting',
               '(a) Porous mould, (b) pouring, (c) draining, (d) trimming, (e) removal, copied from Session 18 Slide 15', 720)
    REG.raster('s18-slip-deposition-particles', 'Deposition in slip casting',
               'Particles deposit on the porous mould as the fluid is extracted by capillarity, copied from Session 18 Slide 15', 560)
    REG.raster('s18-pressure-casting-thickness', 'Pressure slip casting',
               'Cast thickness against time for SiC at four applied pressures, copied from Session 18 Slide 16', 560)
    REG.raster('s18-tape-casting-diagram', 'Tape casting',
               'Slip spread by a doctor blade on a moving carrier film and dried, copied from Session 18 Slide 18', 560)
    REG.raster('s18-feedstock-preparation', 'Feedstock preparation',
               'Ceramic powder and binder mixed in an extruder, copied from Session 18 Slide 19', 420)
    REG.raster('s18-extruder', 'Extruder',
               'Feed screw forcing the body through the mouth, copied from Session 18 Slide 20', 720)
    REG.raster('s18-extrusion-jiggering', 'Extrusion and jiggering',
               '(a) Extrusion of a clay slug, (b) jiggering on a revolving mould, copied from Session 18 Slide 20', 720)
    REG.raster('s18-injection-molding-process', 'Injection moulding route',
               'Ceramic powder and binder mixed in an extruder, injection moulded into the green part, debound into the brown part and sintered into ceramic parts, copied from Session 18 Slide 22', 720)
    REG.raster('s18-injection-molded-turbocharger', 'Injection-moulded turbocharger',
               'Ceramic turbocharger rotor made by injection moulding, copied from Session 18 Slide 22', 560)
    REG.raster('s18-sintering-routes', 'From green part to sintering',
               'Debinding or drying give the brown part; pressureless or pressure-assisted sintering follow, copied from Session 18 Slide 23', 560)
    REG.raster('s18-debinding-stages', 'Debinding',
               'Solvent debinding, thermal debinding and sintering of a moulded part, copied from Session 18 Slide 24', 560)
    REG.raster('s18-drying-water-removal', 'Water removal during drying',
               'Interparticle water, pore water and dry clay particles in three stages of drying, copied from Session 18 Slide 24', 520)
    REG.raster('s18-sintering-stages-mechanisms', 'Sintering stages and mechanisms',
               '(a) Initial, intermediate and final stages; (b) the six transport paths to the neck, copied from Session 18 Slide 25', 560)
    REG.raster('s18-alumina-fibre-guide', 'Shrinkage on sintering',
               'Alumina fibre guide machined in the green state and after sintering, copied from Session 18 Slide 25', 560)
    REG.raster('s18-sintering-classification', 'Types of sintering',
               'Solid-state and liquid-phase (permanent or transient) sintering, copied from Session 18 Slide 26', 560)
    REG.raster('s18-liquid-phase-sintering', 'Liquid-phase sintering',
               'Rearrangement, solution-reprecipitation and final densification, copied from Session 18 Slide 26', 420)
    REG.raster('s18-hip-schematic', 'Hot isostatic pressing',
               'Pressure vessel with heater, inert gas, compressor and vacuum line, copied from Session 18 Slide 27', 560)
    REG.raster('s18-sps-schematic', 'Spark plasma sintering',
               'Pulsed DC current through a graphite die and punches under pressure, copied from Session 18 Slide 28', 420)
    REG.raster('s18-am-processes', 'Additive manufacturing of ceramics',
               'Powder bed fusion, binder jetting, photopolymerization, material extrusion, material jetting and laminated object manufacturing, copied from Session 18 Slide 29', 560)
    REG.raster('s18-viscosity-temperature', 'Viscosity of glasses',
               'Viscosity against temperature of four glasses, with the reference points, copied from Session 18 Slide 30', 420)
    REG.raster('s18-volume-temperature', 'Volume-temperature of glass',
               'Crystals, liquid and glass; slower cooling gives a lower Tg, copied from Session 18 Slide 30', 420)
    REG.raster('s18-float-glass', 'Float glass',
               'Molten glass floated on molten tin, then annealed in the lehr, copied from Session 18 Slide 31', 560)
    REG.raster('s18-glass-tube-drawing', 'Tube drawing',
               'Molten glass drawn over a rotating mandrel, copied from Session 18 Slide 31', 560)
    REG.raster('s18-blow-moulding-steps', 'Blow moulding',
               'Six steps from the heated preform to the finished bottle, copied from Session 18 Slide 31', 720)
    REG.raster('s18-press-moulding-steps', 'Pressing of glass',
               'Empty mould, loaded mould, glass pressed, finished product, copied from Session 18 Slide 31', 720)
    REG.raster('s18-tempering-schematic', 'Tempering of glass',
               'Hot glass, cooled surface and final state with surface compression and core tension, copied from Session 18 Slide 33', 720)
    REG.raster('s18-residual-stress-profile', 'Residual stresses in tempered glass',
               'Compression near the surfaces, tension in the interior, copied from Session 18 Slide 33', 720)
    REG.raster('s18-fibre-core-cladding', 'Optical fibre',
               'Core of higher refractive index inside the cladding, copied from Session 18 Slide 35', 560)
    REG.raster('s18-fibre-size-comparison', 'Fibre sizes',
               'Human hair, optical fibre and fibreglass compared, copied from Session 18 Slide 35', 560)
    REG.raster('s18-tps-shuttle-tile-map', 'Space Shuttle tiles',
               'Positions of AFRSI, LI-2200, RCC, FRCI-12 tiles and gap fillers, copied from Session 18 Slide 36', 560)
    REG.raster('s18-tps-shuttle-left', 'Shuttle thermal protection zones',
               'HRSI, LRSI, FRSI and RCC on the orbiter, copied from Session 18 Slide 37', 560)
    REG.raster('s18-tps-shuttle-right', 'Upper and lower surfaces',
               'Distribution of RCC, HRSI, LRSI and coated Nomex felt, copied from Session 18 Slide 37', 720)
    REG.raster('s18-tps-transporter-map', 'Thermal protection of Orbiter 102',
               'Map of the protection with the area and weight of each element, copied from Session 18 Slide 38', 560)
    REG.raster('s18-engine-section', 'Ceramics in a gas turbine',
               'Section of the Rolls-Royce AMED engine with its ceramic components, copied from Session 18 Slide 40', 560)
    REG.raster('s18-tbc-turbine-blade', 'Thermal barrier coating',
               'Turbine blade with a YSZ thermal barrier coating, copied from Session 18 Slide 41', 560)
    REG.raster('s18-traditional-ceramics-applications', 'Applications of traditional ceramics',
               'Map of the traditional ceramic products: refractories, electrical ware, earthenware and whiteware, glasses, structural shapes, cutting tools, abrasives, flooring, building materials and carbon and graphite, copied from Session 18 Slide 42', 720)
    REG.raster('t8-p1-planes-110-100', 'Planes (110) and (100) of AxByCz',
               'Two planes of the cell of Problem 3, copied from Problems T8_CeramicMaterials, p. 1', 560)
    REG.raster('t8-p2-planes-100-110', 'Planes (100) and (110) of AxBy',
               'Two planes of the cubic cell of Problem 4, copied from Problems T8_CeramicMaterials, p. 2', 560)
    REG.raster('t8-p2-planes-020-100', 'Planes (020) and (100) of AB',
               'Two planes of the cubic cell of Problem 5, copied from Problems T8_CeramicMaterials, p. 2', 560)


def theory():
    rasters()


def build():
    theory()
    return REG
