"""Topic 10 figures for Aerospace Materials I: composite materials (Sessions 21, 22 and 23) and the problem sheet T10.

Screenshot-First: every figure of this topic is a PNG crop of a slide or of the problem sheet (registered with
`REG.raster`; the crops are 200 DPI clips of the PDF pages, written once to vault/attachments/T10).
"""
from figures.svgkit import Registry

REG = Registry("T10")


def rasters():
    REG.raster('s21-synergy-materials-diagram', 'Synergism diagram of material classes around a composite',
               'Materials (metals, polymers, ceramics, glasses, elastomers) combining into composites to show synergism. Copied from Session 21 Slide 2.', 520)
    REG.raster('s21-abalone-shell-photo', 'Abalone shell photograph',
               'Abalone shell, CaCO3 with 3% organic material, a natural composite. Copied from Session 21 Slide 3.', 420)
    REG.raster('s21-abalone-sem-micrograph', 'Abalone shell SEM micrograph',
               'SEM micrograph of the abalone shell layered structure. Copied from Session 21 Slide 3.', 300)
    REG.raster('s21-wood-micrograph', 'Juniperus ashei wood micrograph',
               'Juniperus ashei wood: cellulose filaments in a lignin and hemicellulose matrix. Copied from Session 21 Slide 3.', 420)
    REG.raster('s21-constituents-diagram', 'Fibre, matrix and composite schematic',
               'A fibre or reinforcement plus a matrix gives a composite. Copied from Session 21 Slide 4.', 620)
    REG.raster('s21-matrix-classification-diagram', 'Composite classification by matrix',
               'PMC, MMC and CMC: architecture and materials used in each. Copied from Session 21 Slide 6.', 760)
    REG.raster('s21-reinforcement-classification-tree', 'Composite classification by reinforcement',
               'Tree of particle, fibre and structural reinforced composites with schematics. Copied from Session 21 Slide 7.', 760)
    REG.raster('s21-factors-concentration-size', 'Factors of particle reinforcement: concentration and size',
               'Dispersed phase in a matrix changing concentration and particle size. Copied from Session 21 Slide 8.', 620)
    REG.raster('s21-factors-shape-distribution-orientation', 'Factors of particle reinforcement: shape, distribution and orientation',
               'Particle shape, distribution and orientation in the matrix. Copied from Session 21 Slide 8.', 760)
    REG.raster('s21-large-vs-nanoparticle-schematic', 'Large-particle and nanoparticle composites',
               'Schematic of a large-particle composite (a) and a nanoparticle composite (b). Copied from Session 21 Slide 9.', 460)
    REG.raster('s21-carbon-black-tem', 'Carbon black particles in styrene-butadiene rubber',
               'TEM view of carbon black particles in styrene-butadiene rubber, scale bar 1 micrometre. Copied from Session 21 Slide 11.', 380)
    REG.raster('s21-td-ni-micrograph', 'TD-Ni electron micrograph',
               'Electron micrograph of TD-Ni with 300 nm diameter ThO2 particles (X2000). Copied from Session 21 Slide 13.', 420)
    REG.raster('s21-fibre-shape-classification', 'Fibre reinforcement classified by shape',
               'Continuous aligned, discontinuous aligned and randomly oriented, and woven fibres. Copied from Session 21 Slide 14.', 760)
    REG.raster('s21-high-performance-schematic', 'High-performance composite: fibres plus matrix',
               'Strong, stiff, brittle fibres plus a soft, ductile matrix give high fatigue strength and stiffness per weight. Copied from Session 21 Slide 16.', 760)
    REG.raster('s21-sizing-process-schematic', 'Glass fibre drawing and sizing process',
               'Molten glass through a bushing, cooled, sprayed with sizing and passed to secondary processing. Copied from Session 21 Slide 19.', 520)
    REG.raster('s21-sizing-application-photo', 'Sizing application on glass fibres',
               'Photograph of an industrial sizing applicator for glass fibres. Copied from Session 21 Slide 19.', 340)
    REG.raster('s21-glass-typical-configurations', 'Typical configurations of glass-fibre reinforcement',
               'a) continuous fibres, b) discontinuous fibres, c) woven fibre, with photographs of each. Copied from Session 21 Slide 20.', 760)
    REG.raster('s21-carbon-fibre-demand-chart', 'Carbon fibre demand by application, 2001-2010',
               'Carbon fibre demand (tons per year) by application, 2001 to 2010. Copied from Session 21 Slide 21.', 620)
    REG.raster('s21-carbon-fibre-modulus-strength-chart', 'Carbon fibre product types by mechanical properties',
               'Tensile strength (GPa) against tensile elastic modulus (GPa) for the carbon fibre product types. Copied from Session 21 Slide 22.', 620)
    REG.raster('s21-pan-stabilization-carbonization-flow', 'PAN to carbon fibre process flow',
               'PAN fibre, stabilization at 200-220 C, carbonization at 1000-1500 C, graphitization at 1800 C. Copied from Session 21 Slide 23.', 720)
    REG.raster('s21-carbon-fibre-cross-section-sem', 'Carbon fibre cross-section micrographs',
               'SEM of carbon fibre cross-sections at increasing magnification (a), (b), (c). Copied from Session 21 Slide 23.', 300)
    REG.raster('s21-carbon-fibre-structure-images', 'Carbon fibre structure: hexagonal planes',
               'Oriented graphite hexagonal planes along the fibre axis and a 1 nm structure view. Copied from Session 21 Slide 23.', 380)
    REG.raster('s21-nanotube-tem', 'Carbon nanotube TEM image',
               'Electron micrograph of a carbon nanotube, scale bar 20 nm. Copied from Session 21 Slide 24.', 320)
    REG.raster('s21-carbon-fibre-product-flow', 'Carbon fibre product forms: filaments, tows, coil, tape and fabric',
               'Individual filaments of 5-20 micrometres bundled into tows (1K to 24K) and processed into coil, unidirectional tape and fabric. Copied from Session 21 Slide 25.', 760)
    REG.raster('s21-carbon-fibre-sem-micrographs', 'Carbon fibre SEM micrographs',
               'SEM views of carbon fibres at X1,500, X3,000 and X20,000. Copied from Session 21 Slide 25.', 620)
    REG.raster('s21-carbon-fibre-product-gallery', 'Carbon fibre product forms gallery',
               'Photographs of filament, tow, staple yarn, woven fabric, braid, chopped fibre, milled, felt mat, prepreg and compound. Copied from Session 21 Slide 26.', 760)
    REG.raster('s21-fabrication-application-diagram', 'Carbon fibre products: fabrication methods and applications',
               'Filament, woven fabric, prepreg and chopped fibre with fabrication methods and applications. Copied from Session 21 Slide 29.', 760)
    REG.raster('s21-kevlar-nomex-formulas', 'Chemical repeat units of Kevlar and Nomex',
               'Repeat units of poly(para-phenylene terephthalamide) (Kevlar) and poly(metaphenylene isophthalamide) (Nomex). Copied from Session 21 Slide 30.', 420)
    REG.raster('s21-aramid-prepreg-photo', '100% aramid fibre prepreg',
               'Photograph of a 100% aramid fibre prepreg. Copied from Session 21 Slide 30.', 300)
    REG.raster('s21-aramid-woven-fabric-photo', 'Aramid fibre woven fabric',
               'Photograph of aramid fibre woven fabric. Copied from Session 21 Slide 30.', 300)
    REG.raster('s21-woven-fabric-weave-patterns', 'Woven fabric weave patterns',
               'Plain weave, 2x2 twill, 4 HS and 8 HS (harness satin) weaves, with fabric photographs. Copied from Session 21 Slide 31.', 760)
    REG.raster('s21-warp-weft-woven-fibres', 'Warp and weft of woven fabric; woven fibres and cross-section',
               'Warp and weft directions in woven fabric, and the woven fibre cross-section. Copied from Session 21 Slide 31.', 300)
    REG.raster('s21-carbon-fabric-cost-chart', 'Typical cost of woven fabric',
               'Typical cost of about 300 g/m2 woven fabric per m2 for E-glass, S-glass, aramid, HS carbon and IM carbon. Copied from Session 21 Slide 32.', 620)
    REG.raster('s21-ncf-structure-photos', 'Non crimp fabric (NCF) structure and photographs',
               'NCF fabric structure with stitched layers at 0, 90, +45 and -45 degrees, and two photographs. Copied from Session 21 Slide 32.', 760)
    REG.raster('s21-3d-braided-preform-diagram', '3D braided preform formation',
               'Braided preform formation with peripheral yarn carriers and base array. Copied from Session 21 Slide 33.', 320)
    REG.raster('s21-preform-photographs', '3D carbon fibre preforms',
               'Photographs of 3D carbon fibre preforms and a braiding machine. Copied from Session 21 Slide 33.', 760)
    REG.raster('s21-laminate-photo', 'Laminate stack photograph',
               'Stacked laminate sheets of composite material. Copied from Session 21 Slide 36.', 300)
    REG.raster('s21-laminate-stacking-schematic', 'Laminate stacking schematic',
               'Laminate built from stacked layers with different fibre orientations. Copied from Session 21 Slide 36.', 520)
    REG.raster('s21-unidirectional-crossplied-stacks', 'Unidirectional and cross-plied laminate stacks',
               'Stacks of unidirectional plies, and a cross-plied quasi-isotropic layup at 0, 90, +45 and -45 degrees. Copied from Session 21 Slide 37.', 520)
    REG.raster('s21-honeycomb-core-photo', 'Honeycomb core photograph',
               'Photograph of a honeycomb core. Copied from Session 21 Slide 36.', 300)
    REG.raster('s21-sandwich-exploded-drawing', 'Exploded sandwich panel drawing',
               'Exploded drawing of a sandwich panel: two face sheets and a core. Copied from Session 21 Slide 36.', 320)
    REG.raster('s21-glare-layup-and-micrograph', 'GLARE lay-up and micrograph',
               'GLARE lay-up, and a micrograph of the GLARE layers (aluminium and GFRP), scale bar 500 micrometres. Copied from Session 21 Slide 39.', 760)
    REG.raster('s21-glare-aircraft-application', 'Aircraft using GLARE panels',
               'Aircraft drawing showing GLARE use on the fuselage. Copied from Session 21 Slide 39.', 360)
    REG.raster('s21-glare-application-photos', 'GLARE panels in production and in service',
               'Photographs of GLARE panels: a panel, a layered sample and a production line. Copied from Session 21 Slide 39.', 760)
    REG.raster('s21-mechanical-properties-fibres-chart', 'Tensile stress against tensile strain for fibres and resin-impregnated strands',
               'Tensile stress (MPa) against tensile strain (%) for boron fibre, HM and HT graphite, Kevlar 49, E-glass, S-glass, Nomex and resin-impregnated strands, with slopes E. Copied from Session 21 Slide 40.', 620)
    REG.raster('s21-specific-strength-modulus-chart', 'Specific tensile strength against specific tensile modulus',
               'Specific tensile strength against specific tensile modulus (units 10^6 in and 10^8 in) for fibres and metals in an epoxy matrix. Copied from Session 21 Slide 43.', 620)
    REG.raster('s21-specific-strength-modulus-MJ-chart', 'Specific tensile strength against specific modulus, SI units',
               'Specific tensile strength (MJ/kg) against specific modulus (MJ/kg) for fibres in an epoxy matrix, with the legend for quasi-isotropic, bulk and unidirectional layups. Copied from Session 21 Slide 43.', 620)
    REG.raster('s22-ashby-strength-density', 'Strength-density chart of material classes',
               'Ashby-style chart of strength against density for the material classes, with the composites region highlighted, copied from Session 22 Slide 2', 517)
    REG.raster('s22-certification-pyramid', 'Certification pyramid for composite structures',
               'Pyramid of the building-block levels from coupons to component, with the aircraft certification and material qualification arrows, copied from Session 22 Slide 3', 472)
    REG.raster('s22-fibre-crack-matrix-functions', 'Fibre crack and the polymer matrix',
               'Sketch of fibres with a fibre crack, the matrix functions and the coordinate system, copied from Session 22 Slide 6', 300)
    REG.raster('s22-phenolic-structure', 'Phenolic structure',
               'Chemical structure of the phenolic resin ring, copied from Session 22 Slide 7', 300)
    REG.raster('s22-epoxy-structure', 'Epoxy structural unit',
               'Chemical structure of the epoxy unit, copied from Session 22 Slide 8', 442)
    REG.raster('s22-polyimide-structure', 'Polyimide structure',
               'Chemical structure of the polyimide imide ring with the R groups, copied from Session 22 Slide 8', 300)
    REG.raster('s22-bmi-structure', 'Bismaleimide structure',
               'Chemical structure of the bismaleimide (BMI) with the R group between the two maleimide rings, copied from Session 22 Slide 9', 347)
    REG.raster('s22-sem-poor-adherence', 'Poor matrix-fibre adherence',
               'SEM micrograph of fibres with poor adherence to the matrix, copied from Session 22 Slide 16', 306)
    REG.raster('s22-sem-good-adherence', 'Good matrix-fibre adherence',
               'SEM micrograph of fibres with good adherence to the matrix, copied from Session 22 Slide 16', 306)
    REG.raster('s22-glass-sizing-interface', 'Chemically bonded and diffused glass-polymer interfaces',
               'Schematic of the chemically bonded and diffused interfaces between glass and the sizing polymer with coupling agent, copied from Session 22 Slide 18', 300)
    REG.raster('s22-isostrain-fibre-bars', 'Isostrain: loading parallel to the fibres',
               'Sketch of a fibre composite loaded parallel to the fibres (isostrain) with the stack of fibre and matrix layers, copied from Session 22 Slide 21', 300)
    REG.raster('s22-fibre-matrix-cell', 'Fibre-matrix cell',
               'Sketch of the fibre-matrix cell with the fibre and matrix labels, copied from Session 22 Slide 21', 300)
    REG.raster('s22-isostress-fibre-matrix', 'Isostress: fibre and matrix sketch',
               'Sketch of fibre and matrix under isostress (loading perpendicular to the fibres), copied from Session 22 Slide 23', 300)
    REG.raster('s22-isostress-layers', 'Isostress: layered model',
               'Sketch of the layered model of the composite under isostress, copied from Session 22 Slide 23', 300)
    REG.raster('s22-fibreglass-epoxy-modulus', 'Modulus of fibreglass-epoxy: isostrain and isostress',
               'Longitudinal (isostrain) and transverse (isostress) modulus against fibre volume fraction for fibreglass in epoxy, E_f = 72.4 GPa and E_m = 6.9 GPa, copied from Session 22 Slide 25', 693)
    REG.raster('s22-fibre-fracture-stress-strain', 'Stress-strain curve with fibre and matrix fracture',
               'Stress against strain of the composite, with fibre fracture and matrix yield labelled (Spanish labels as printed), copied from Session 22 Slide 26', 318)
    REG.raster('s22-critical-fibre-fraction', 'Strength against fibre volume fraction and critical fraction',
               'Composite strength against fibre volume fraction with the critical volume fraction marked (Spanish labels as printed), copied from Session 22 Slide 26', 322)
    REG.raster('s22-particle-aggregate-sketch-b', 'Uniformly dispersed spherical aggregate (Cu-W)',
               'Sketch of spherical tungsten particles uniformly dispersed in the copper matrix, copied from Session 22 Slide 28', 300)
    REG.raster('s22-tungsten-copper-modulus', 'Modulus of Cu-W composite against W volume fraction',
               'Measured modulus of copper reinforced with tungsten particles against tungsten volume percentage, with upper and lower bounds, copied from Session 22 Slide 28', 489)
    REG.raster('s22-kic-ceramic-composites', 'Toughness of ceramic-matrix composites',
               'Fracture toughness K_IC of unreinforced ceramics and ceramic-matrix composites (bar chart as printed), copied from Session 22 Slide 29', 392)
    REG.raster('s22-specific-strength-epoxy', 'Specific strength of epoxy with different reinforcements',
               'Specific strength of noncomposite materials and of epoxy composites with different reinforcements (bar chart as printed), copied from Session 22 Slide 29', 506)
    REG.raster('s23-laminating-process-flow', 'Laminating procedure flow',
               'Stages of the laminating procedure for aircraft-grade composite components, from prepreg production to autoclave curing. (copied from Session 23 Slide 2)', 640)
    REG.raster('s23-prepreg-fiber-impregnation-branch', 'Fiber impregnation branch: prepregs and SMC',
               'Branch of the laminating flow from fiber impregnation to prepregs and sheet molding compound. (copied from Session 23 Slide 3)', 600)
    REG.raster('s23-unidirectional-tape', 'Unidirectional tape',
               'Drawing of a unidirectional prepreg tape, all fibers parallel. (copied from Session 23 Slide 4)', 300)
    REG.raster('s23-bidirectional-fabric', 'Bi-directional fabric',
               'Drawing of a bi-directional woven prepreg fabric with warp and weft directions. (copied from Session 23 Slide 4)', 300)
    REG.raster('s23-glass-fiber-epoxy-prepreg', 'Glass fiber / epoxy prepreg',
               'Photograph of a glass fiber / epoxy prepreg sheet. (copied from Session 23 Slide 5)', 320)
    REG.raster('s23-carbon-fiber-epoxy-prepreg-fabric', 'Carbon fiber fabric / epoxy prepreg',
               'Photograph of a rolled carbon fiber fabric / epoxy prepreg. (copied from Session 23 Slide 5)', 320)
    REG.raster('s23-prepreg-impregnation-schematic', 'Prepreg impregnation line',
               'Schematic of the prepreg impregnation line: spools, surface treatment, resin bath, backing paper. (copied from Session 23 Slide 6)', 520)
    REG.raster('s23-prepreg-calender-schematic', 'Prepreg drying and winding',
               'Schematic of the drying over heated calender rolls and winding of the spooled prepreg. (copied from Session 23 Slide 6)', 480)
    REG.raster('s23-smc-line-schematic', 'Sheet molding compound line',
               'Schematic of the sheet molding compound line: chopped strands, resin paste, carrier films, compaction belt. (copied from Session 23 Slide 7)', 520)
    REG.raster('s23-f14-tape-laying-photo', 'Single-ply tape lay-up, F-14',
               'Photograph of a single-ply lay-up of boron-epoxy tape for the F-14 horizontal stabilizer. (copied from Session 23 Slide 8)', 380)
    REG.raster('s23-molding-methods-tree', 'Processing methods for PMCs',
               'Classification of PMC processing methods: manual lay-up, molding, automatic processes and pultrusion. (copied from Session 23 Slide 9)', 700)
    REG.raster('s23-hand-lay-up-schematic', 'Hand lay-up schematic',
               'Schematic of manual lay-up of resin and reinforcement in a mold with a roller and a brush. (copied from Session 23 Slide 10)', 380)
    REG.raster('s23-spray-lay-up-schematic', 'Spray lay-up schematic',
               'Schematic of spray lay-up: chopped glass roving and resin sprayed into a mold. (copied from Session 23 Slide 10)', 420)
    REG.raster('s23-compression-molding-profile-sections', 'Compression-molded profile sections',
               'Three cross-section sketches of a profile formed in a compression mold. (copied from Session 23 Slide 11)', 300)
    REG.raster('s23-pressure-bag-molding-schematic', 'Pressure-bag molding schematic',
               'Schematic of pressure-bag molding with a flexible bag, clamp, mold release, gel coat and air pressure of 345 kPa. (copied from Session 23 Slide 11)', 500)
    REG.raster('s23-vacuum-bag-layup-diagram', 'Vacuum-bag lay-up layers',
               'Exploded layer diagram of a vacuum-bag lay-up: mould, aluminium foil, laminates, release film, breather, vacuum bag. (copied from Session 23 Slide 12)', 520)
    REG.raster('s23-vacuum-bag-molding-schematic', 'Vacuum-bag molding schematic',
               'Schematic of vacuum-bag molding with clamping bar, gasket, vacuum trap and flexible bar at atmospheric pressure. (copied from Session 23 Slide 12)', 520)
    REG.raster('s23-rtm-figure-1-schematic', 'Resin transfer molding, Figure 1',
               'Schematic of resin transfer molding: resin and catalyst containers, pump, mixing head, upper and lower mold, heating arrangement. (copied from Session 23 Slide 13)', 560)
    REG.raster('s23-rtm-mold-section', 'RTM mold section',
               'Cross-section of an RTM mold showing resin injection points, vent, seal, fabrics and matrix. (copied from Session 23 Slide 13)', 480)
    REG.raster('s23-rfi-layup-schematic', 'Resin film infusion lay-up',
               'Exploded lay-up of resin film infusion: release film, resin, auxiliary products, peel ply, vacuum bagging film. (copied from Session 23 Slide 15)', 460)
    REG.raster('s23-rfi-setup-schematic', 'Resin film infusion setup',
               'Schematic of resin film infusion in an autoclave or oven: sealant tape, dry reinforcement stack, vacuum pump. (copied from Session 23 Slide 15)', 480)
    REG.raster('s23-filament-winding-process', 'Filament winding process',
               'Schematic of filament winding: roving through a traversing resin bath onto a rotating mandrel. (copied from Session 23 Slide 17)', 420)
    REG.raster('s23-filament-winding-patterns', 'Filament winding patterns',
               'Circumferential, helical and polar winding patterns on a cylinder. (copied from Session 23 Slide 17)', 480)
    REG.raster('s23-filament-winding-liners-photo', 'Filament-wound liners',
               'Photograph of fiberglass being wound over aluminum liners for slide-raft inflation vessels of the Boeing 767. (copied from Session 23 Slide 18)', 360)
    REG.raster('s23-atl-machine-schematic', 'Automatic tape laying machine schematic',
               'Schematic of a numerically controlled tape laying machine with x, y and z axes over a mold. (copied from Session 23 Slide 19)', 420)
    REG.raster('s23-atl-gantry-photo', 'Automatic tape laying machine photo',
               'Photograph of a 10-axis computer-numerically-controlled tape-laying system. (copied from Session 23 Slide 20)', 360)
    REG.raster('s23-afp-tow-schematic', 'Fiber placement head schematic',
               'Schematic of an automatic fiber placement head: individual tow payout with controlled tension, cutters, compaction roller and part surface. (copied from Session 23 Slide 21)', 520)
    REG.raster('s23-afp-head-photo', 'Fiber placement head photograph',
               'Photograph of an automatic fiber placement head depositing tows. (copied from Session 23 Slide 21)', 320)
    REG.raster('s23-afp-seven-axis-machine', 'Seven-axis fiber placement machine',
               'Diagram of a seven-axis fiber placement machine with two rotative mandrels and the axes labelled X, Y, Z, C, A, B. (copied from Session 23 Slide 22)', 460)
    REG.raster('s23-pultrusion-schematic', 'Pultrusion schematic',
               'Schematic of pultrusion: fiber rovings, resin impregnation tank, preforming die, curing die and pullers. (copied from Session 23 Slide 23)', 560)
    REG.raster('s23-autoclave-pressure-schematic', 'Autoclave pressure schematic',
               'Cross-section of an autoclave showing the vacuum bag, lay-up, tool, autoclave pressure and vacuum line. (copied from Session 23 Slide 25)', 400)
    REG.raster('s23-composite-curing-autoclave-photo', 'Composite curing autoclave',
               'Photograph of a composite curing autoclave with its internal door open. (copied from Session 23 Slide 25)', 360)
    REG.raster('s23-autoclave-cure-cycle-chart', 'Typical autoclave cure cycle',
               'Chart of curing temperature against curing time for a typical autoclave cycle, with 3 and 1 degree per minute ramps, a 1 h hold at 135 degrees C and a 2 h hold at 180 degrees C. (copied from Session 23 Slide 26)', 560)
    REG.raster('s23-integration-example-flow', 'Integration of structures: example',
               'Process chain for a skin and stringer structure: ATL, vacuum bagging, cure cycle, co-bonding, trimming, inspection and assembly. (copied from Session 23 Slide 28)', 700)
    REG.raster('s23-co-bonded-skin-photo', 'Co-bonded skin with stringers',
               'Photograph of a co-bonded pre-cured skin with wet T-stringers on a turning rack. (copied from Session 23 Slide 29)', 480)
    REG.raster('s23-mmc-processing-tree', 'MMC processing routes',
               'Classification of metal matrix composite processing routes: solid state, liquid phase and two-phase processing. (copied from Session 23 Slide 31)', 600)
    REG.raster('s23-diffusion-bonding-schematic', 'Diffusion bonding',
               'Diffusion bonding route: foil and fiber lay-up, heating and pressure, vacuum encapsulation and the finished product. (copied from Session 23 Slide 32)', 480)
    REG.raster('s23-powder-metallurgy-schematic', 'Powder metallurgy route',
               'Powder metallurgy route: mixing of matrix powder and reinforcement, compaction in a die and sintering. (copied from Session 23 Slide 32)', 480)
    REG.raster('s23-liquid-phase-flow-part-1', 'Liquid phase processing routes, part 1',
               'Classification of liquid-phase MMC routes: melt stirring and liquid infiltration (copied from Session 23 Slide 33)', 520)
    REG.raster('s23-liquid-phase-flow-part-2', 'Liquid phase processing routes, part 2',
               'Continuation of the liquid-phase flow: liquid forced into a porous preform leads to gas pressure infiltration or squeeze casting (copied from Session 23 Slide 33)', 520)
    REG.raster('s23-melt-stirring-schematic', 'Melt stirring furnace',
               'Schematic of a melt stirring furnace with a motor-driven stirrer, matrix material and reinforcement inlets. (copied from Session 23 Slide 33)', 380)
    REG.raster('s23-squeeze-casting-schematic', 'Squeeze casting',
               'Cross-section of a squeeze casting die with a preform, molten metal, pressure ram and heating elements, producing metal matrix composites. (copied from Session 23 Slide 34)', 520)
    REG.raster('s23-gas-pressure-infiltration-stages', 'Gas pressure infiltration stages',
               'Three stages of gas pressure infiltration: preform in the closed die, vacuum in the chamber, and pressurized gas forcing the molten metal into the preform. (copied from Session 23 Slide 35)', 620)
    REG.raster('s23-rheocasting-schematic', 'Rheocasting or composcasting',
               'Sequence of rheocasting: semi-solid alloy heated, stirred with reinforcements, cooled into a composite bullet and hot-extruded. (copied from Session 23 Slide 36)', 600)
    REG.raster('s23-spray-codeposition-schematic', 'Spray co-deposition',
               'Schematic of spray co-deposition: an atomizer breaks the melt into droplets, particles are injected into the spray and co-deposit on a collector substrate. (copied from Session 23 Slide 37)', 480)
    REG.raster('s23-cmc-fracture-micrograph', 'Fracture surface of a SiC/SiC composite',
               'Scanning electron micrograph of the fracture surface of a SiC fiber-reinforced SiC matrix ceramic composite. (copied from Session 23 Slide 38)', 380)
    REG.raster('s23-cmc-silicon-carbide-examples', 'Silicon carbide matrix composites',
               'Silicon carbide matrix composites: key points, reinforcements and applications (rocket nozzle, aeroengine vane). (copied from Session 23 Slide 39)', 700)
    REG.raster('s23-cmc-oxide-zrb2-examples', 'Oxide and ZrB2 or HfB2 matrix composites',
               'Oxide and ZrB2 or HfB2 matrix composites: key points, reinforcements and applications (mixer and acoustic nozzles, rentry nose, nozzle). (copied from Session 23 Slide 40)', 700)
    REG.raster('s23-cmc-carbon-sic-tubes-photo', 'C/SiC tubes',
               'Photograph of carbon fiber reinforced silicon carbide tubes with a micrograph inset. (copied from Session 23 Slide 41)', 340)
    REG.raster('s23-cmc-nozzle-extensions-photo', 'C/SiC nozzle extensions',
               'Photograph of two C/SiC nozzle extensions with dimensions. (copied from Session 23 Slide 41)', 300)
    REG.raster('s23-cmc-nozzle-hot-fire-photo', 'Subscale nozzle hot-fire test',
               'Photograph of a subscale C/SiC nozzle during a hot-fire test. (copied from Session 23 Slide 41)', 300)
    REG.raster('s23-f16-nozzle-photo', 'F-16 nozzle with CMC seals',
               'Photograph of an F-16 engine exhaust nozzle with five CMC divergent seals. (copied from Session 23 Slide 41)', 380)
    REG.raster('s23-cmc-temperature-capability-chart', 'Temperature capability of composites',
               'Chart of temperature capability against nominal thermal conductivity for C/C, UHTC, C/SiC, SiC/SiC and Ni-based superalloys, with curves for thicknesses of 0.3 to 10 cm. (copied from Session 23 Slide 41)', 620)
    REG.raster('s23-cmc-processing-tree', 'CMC processing routes',
               'Classification of ceramic matrix composite processing: conventional mixing, infiltration of a preform, slurry processing and liquid state processing. (copied from Session 23 Slide 42)', 600)
    REG.raster('s23-conventional-mixing-flow', 'Conventional mixing and processing',
               'Flow of conventional powder mixing: powder of matrix and particulate or whisker reinforcement and binder, mixer, pressing and firing. (copied from Session 23 Slide 43)', 520)
    REG.raster('s23-sol-gel-infiltration-cycle', 'Sol-gel infiltration of a preform',
               'Cycle of sol-gel infiltration of a ceramic fiber preform: pour sol, gelation and drying, pyrolysis, repeated 4 to 10 times with pyrolysis at 800 to 1300 degrees C. (copied from Session 23 Slide 44)', 640)
    REG.raster('s23-slurry-processing-schematic', 'Slurry processing',
               'Slurry processing: fibers pass through a matrix slurry tank, impregnated tapes are stacked, pressed, binder burnt out at 500 degrees C and hot pressed at 800 to 925 degrees C in a graphite die. (copied from Session 23 Slide 45)', 600)
    REG.raster('s23-composite-share-chart', 'Share of composite components by aircraft',
               'Chart of share of composite components (%) against year from 1975 to 2010 for aircraft models from MD-80 to 787-8, with the A380 marked. (copied from Session 23 Slide 47)', 600)
    REG.raster('s23-a380-material-pie', 'A380-800 materials distribution',
               'Pie chart of the A380-800 structure material breakdown, excluding engine, landing gear and others. (copied from Session 23 Slide 48)', 420)
    REG.raster('s23-airbus-material-distribution-chart', 'Material distribution in Airbus aircraft',
               'Stacked chart of material distribution in Airbus aircraft A300, A320, A340 and A380 from 1972 to 2006, in percent. (copied from Session 23 Slide 48)', 560)
    REG.raster('s23-a340-600-composite-parts', 'Composite parts of the A340-600',
               'Composite parts of the Airbus A340-600: wing J-nose, engine cowling, vertical and horizontal tail planes, keel beam, belly fairing and rear pressure bulkhead. (copied from Session 23 Slide 49)', 640)
    REG.raster('s23-a350-xwb-structural-design', 'A350 XWB structural design',
               'A350 XWB structural design diagram: nose, fin and fuselage sections with carbon fiber skin panels, aluminium frames and a material breakdown pie chart. (copied from Session 23 Slide 50)', 560)
    REG.raster('s23-a380-composite-parts', 'Composite parts of the Airbus A380',
               'Composite parts of the Airbus A380 with labelled structures: floor beams, J-nose, outer flaps, section 19, rear pressure bulkhead, vertical and horizontal tail planes, center wing box. (copied from Session 23 Slide 51)', 640)
    REG.raster('s23-boeing-757-200-composite-parts', 'Boeing 757-200 composite parts',
               'Diagram of composite parts of the Boeing 757-200 with labels for flap support fairings, ailerons, rudders, spoilers, elevators and fixed trailing edge panels. (copied from Session 23 Slide 52)', 600)
    REG.raster('s23-boeing-767-composite-parts', 'Composite parts of the Boeing 767',
               'Diagram of composite parts of the Boeing 767 with a colour key: graphite, Kevlar-graphite, fiberglass and Kevlar. (copied from Session 23 Slide 52)', 520)
    REG.raster('s23-boeing-777-composite-parts', 'Composite parts of the Boeing 777',
               'Diagram of composite parts of the Boeing 777 with a colour key: toughened graphite, graphite, hybrid. (copied from Session 23 Slide 53)', 520)
    REG.raster('s23-boeing-787-composite-cluster', 'Boeing 787 composite cluster',
               'Boeing 787-8 illustration with photos of the one-piece barrel section, the one-piece forward fuselage and the wing box, and a pie chart of material shares. (copied from Session 23 Slide 53)', 560)
    REG.raster('s23-tornado-composite-components', 'Tornado composite components',
               'Diagram of composite components of the Tornado aircraft, numbered 1 to 9: forward fuselage, cowling, EFA center fuselage, tornado fin, finbox, X31 wing, tornado undercarriage lid, fuselage center part and lid for RAT. (copied from Session 23 Slide 55)', 620)
    REG.raster('s23-eurofighter-material-distribution', 'Material distribution in Eurofighter',
               'Diagram of the material distribution in the Eurofighter: CFRP, aluminium, titanium, GFRP and aluminium casting. (copied from Session 23 Slide 56)', 420)
    REG.raster('s23-fibre-composite-share-chart', 'Fibre composite share in military aircraft',
               'Chart of fibre composite percent of structural mass against year, 1965 to 2000, for US and European fighter aircraft. (copied from Session 23 Slide 56)', 460)
    REG.raster('s23-concept-aircraft-rendering', 'Concept aircraft rendering',
               'Rendering of a concept military aircraft with colour-coded material zones. (copied from Session 23 Slide 57)', 420)
    REG.raster('s23-b2-material-legend', 'Material legend of the B-2 bomber',
               'Colour key of materials used in the B-2 bomber: carbon fiber composite, Al/Li alloy, Ti alloy, glass fiber composite and other Al alloys. (copied from Session 23 Slide 57)', 300)
    REG.raster('s23-rotor-blade-head-comparison', 'Conventional and optimized rotor blade head',
               'Comparison of a conventional and an optimized rotor blade head with integrated functions. (copied from Session 23 Slide 59)', 560)
    REG.raster('s23-ec135-composite-parts', 'Composite parts of the Eurocopter EC135',
               'Side and top views of the Eurocopter EC135 with a colour key of GFRP sandwich, metal, plastics, secondary and primary structure. (copied from Session 23 Slide 58)', 480)
    REG.raster('s23-tiger-composite-parts', 'Composite parts of the Tiger helicopter',
               'Side and top views of the Tiger helicopter with GFRP, CFRP and aramid sandwich composite parts. (copied from Session 23 Slide 58)', 460)
    REG.raster('s23-space-shuttle-thermal-protection-diagram', 'Space shuttle thermal protection system',
               'Diagram of the Orbiter 102 thermal protection system by material: RCC, HRSI, LRSI, FRSI and metal or glass, with an area and weight table. (copied from Session 23 Slide 61)', 680)
    REG.raster('s23-shuttle-rcc-legend', 'Thermal protection system legend',
               'Key to the Orbiter thermal protection materials: RCC, HRSI, LRSI, FRSI and metal or glass (copied from Session 23 Slide 61)', 300)
    REG.raster('s23-sailboard-cross-section', 'Cross-section of a composite sailboard',
               'Cross-section A-A of a composite sailboard with polyurethane coating, polycarbonate skin, glass and Kevlar reinforcements, honeycomb and polystyrene foam core. (copied from Session 23 Slide 63)', 480)


def theory():
    rasters()


def build():
    theory()
    return REG
