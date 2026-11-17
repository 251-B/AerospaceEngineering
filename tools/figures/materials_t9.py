"""Topic 9 figures for Aerospace Materials I: polymers (Sessions 19 and 20) and the problem sheet T9.

Screenshot-First: every figure of this topic is a PNG crop of a slide or of the problem sheet (registered with
`REG.raster`; the crops are 200 DPI clips of the PDF pages, written once to vault/attachments/T9).
"""
from figures.svgkit import Registry

REG = Registry("T9")


def rasters():
    REG.raster('s19-monomer-to-polymer', 'Monomers joining into a polymer chain',
               'Monomers join by polymerization into one long polymer chain. Session 19, Slide 2.', 380)
    REG.raster('s19-classification-of-polymers', 'Classification of polymers',
               'Classification of polymers by origin, structure, behaviour, polymerization mechanism, applications and chemical composition. Session 19, Slide 6.', 760)
    REG.raster('s19-ethylene-to-polyethylene', 'Ethylene to polyethylene',
               'Ethylene monomers polymerize into polyethylene, with the repeat unit boxed. Session 19, Slide 8.', 745)
    REG.raster('s19-chain-reaction-conversion', 'Chain-reaction polymerization at 25, 50 and 100 percent conversion',
               'Chain-reaction addition polymerization at 25, 50 and 100 percent conversion. Session 19, Slide 9.', 760)
    REG.raster('s19-step-reaction-conversion', 'Step-reaction polymerization at 25, 50 and 100 percent conversion',
               'Step-reaction condensation polymerization at 25, 50 and 100 percent conversion. Session 19, Slide 9.', 760)
    REG.raster('s19-ethylene-repeat-units', 'Ethylene monomer and repeat units',
               'Ethylene monomer and the polyethylene chain of ethylene repeat units. Session 19, Slide 10.', 380)
    REG.raster('s19-chain-reaction-stages', 'Chain-reaction stages',
               'Initiation, propagation and termination of a chain-reaction polymerization. Session 19, Slide 10.', 310)
    REG.raster('s19-pet-condensation-reaction', 'Condensation reaction forming PET',
               'Dimethyl terephthalate and ethylene glycol condense into PET with methyl alcohol as byproduct. Session 19, Slide 11.', 495)
    REG.raster('s19-step-growth-schematic', 'Step-growth schematic',
               'Monomers form dimers and oligomers before high molecular weight growth. Session 19, Slide 11.', 470)
    REG.raster('s19-molecular-weight-distribution', 'Molecular weight distribution',
               'Number-average and weight-average molecular weights on a molecular weight distribution curve. Session 19, Slide 12.', 360)
    REG.raster('s19-number-fraction-histogram', 'Number fraction histogram',
               'Histogram of number fraction by molecular weight range. Session 19, Slide 14.', 300)
    REG.raster('s19-weight-fraction-histogram', 'Weight fraction histogram',
               'Histogram of weight fraction by molecular weight range. Session 19, Slide 15.', 340)
    REG.raster('s19-conformation-torsion-angles', 'Conformation and torsion angles',
               'Chain segment with bond torsion angles and rotation about C-C bonds. Session 19, Slide 16.', 405)
    REG.raster('s19-coiled-chain-sketch', 'Coiled polymer chain sketch',
               'Non-straight polymer chain drawn as a coil. Session 19, Slide 16.', 300)
    REG.raster('s19-cis-trans-isoprene', 'Cis and trans isoprene',
               'Cis and trans configurations of isoprene around a double bond. Session 19, Slide 17.', 730)
    REG.raster('s19-propene-polymerization', 'Vinyl monomer and repeat unit',
               'Vinyl monomer with substituent R and its polymer repeat unit. Session 19, Slide 18.', 590)
    REG.raster('s19-isotactic-syndiotactic-chains', 'Isotactic and syndiotactic chains',
               'Isotactic and syndiotactic arrangements of R groups along the chain. Session 19, Slide 18.', 760)
    REG.raster('s19-pp-tacticity-balls', 'Polypropylene tacticity',
               'Isotactic, syndiotactic and atactic polypropylene chains. Session 19, Slide 19.', 495)
    REG.raster('s19-polystyrene-tacticity', 'Polystyrene tacticity',
               'Isotactic, syndiotactic and atactic polystyrene chains. Session 19, Slide 19.', 425)
    REG.raster('s19-copolymer-sequences', 'Copolymer sequences',
               'Random, alternating, block and graft copolymer sequences. Session 19, Slide 20.', 755)
    REG.raster('s19-vinyl-copolymerization-equation', 'Vinyl chloride and vinyl acetate copolymerization',
               'Copolymerization of vinyl chloride and vinyl acetate into a polyvinyl chloride-polyvinyl acetate copolymer. Session 19, Slide 20.', 445)
    REG.raster('s19-molecular-structure-types', 'Molecular structure types',
               'Linear, branched, crosslinked and network polymer structures. Session 19, Slide 22.', 530)
    REG.raster('s19-semicrystalline-composition', 'Semicrystalline polymer composition',
               'Crystalline and amorphous regions combine into a semicrystalline polymer. Session 19, Slide 24.', 760)
    REG.raster('s19-spherulite-region-sketch', 'Region of high crystallinity',
               'Lamellar texture with a region of high crystallinity and an amorphous region. Session 19, Slide 24.', 300)
    REG.raster('s19-spherulite-growth-stages', 'Spherulite growth stages',
               'Spherulite growth stages from nucleation to full crystallization. Session 19, Slide 25.', 380)
    REG.raster('s19-spherulite-micrograph', 'Spherulite micrograph of polyethylene',
               'Optical micrograph of polyethylene under polarized light showing spherulites. Session 19, Slide 25.', 300)
    REG.raster('s19-lamellae-chain-folds', 'Lamellae of folded chains',
               'Ordered lamellae of folded chains in a semicrystalline polymer. Session 19, Slide 25.', 352)
    REG.raster('s19-spherulite-structure', 'Spherulite structure',
               'Spherulite with lamellar chain-folded crystallites, tie molecules and amorphous material. Session 19, Slide 25.', 300)
    REG.raster('s19-lamella-schematic', 'Crystalline lamella schematic',
               'Crystalline lamella drawn as aligned chain segments. Session 19, Slide 25.', 300)
    REG.raster('s19-polyethylene-polystyrene-structure', 'Polyethylene and polystyrene structures',
               'Polyethylene with a simple monomer and polystyrene with a complex monomer. Session 19, Slide 27.', 320)
    REG.raster('s19-thermal-transition-scheme', 'Movement of segments at Tg and Tm',
               'Movement of amorphous and crystalline segments at the glass transition Tg and melting temperature Tm. Session 19, Slide 28.', 760)
    REG.raster('s19-specific-volume-temperature', 'Specific volume against temperature',
               'Specific volume against temperature for glass, semicrystalline and crystalline solids and liquid. Session 19, Slide 28.', 305)
    REG.raster('s19-density-temperature', 'Density against temperature',
               'Density against temperature for glass, semicrystalline, crystalline and liquid states. Session 19, Slide 28.', 375)
    REG.raster('s19-tg-structures', 'Repeat units and Tg values',
               'Repeat-unit structures of PE, PP, PS and PVK with their glass transition temperatures. Session 19, Slide 29.', 550)
    REG.raster('s19-mw-tg-regimes', 'Molecular weight and temperature regimes',
               'Temperature against molecular weight showing mobile liquid, viscous liquid, rubber, tough plastic and crystalline regimes. Session 19, Slide 30.', 635)
    REG.raster('s19-stress-strain-classes', 'Stress-strain behaviour classes',
               'Stress-strain curves of brittle, tough and ductile, strain hardening and elastomeric polymers. Session 19, Slide 32.', 430)
    REG.raster('s19-brittle-stress-strain', 'Yield strength and tensile strength',
               'Stress-strain curve with the yield strength and the tensile strength marked. Session 19, Slide 33.', 395)
    REG.raster('s19-nylon-stress-strain', 'Stress-strain curve of 6,6-nylon',
               'Stress-strain curve of 6,6-nylon, a typical thermoplastic, with necking and plastic deformation. Session 19, Slide 33.', 518)
    REG.raster('s19-necking-sketch', 'Necking and cold drawing sketch',
               'Specimen stages of necking and cold drawing under tensile force. Session 19, Slide 34.', 545)
    REG.raster('s19-yield-tensile-specimens', 'Yield and tensile strength on the curve',
               'Stress-strain curve with specimen shapes at yield and at tensile strength. Session 19, Slide 34.', 370)
    REG.raster('s19-elastic-region-curve', 'Elastic region of the stress-strain curve',
               'Elastic region tangent to the nominal stress-strain curve. Session 19, Slide 35.', 580)
    REG.raster('s19-elastic-region-chains', 'Chains in the elastic region',
               'Molecular sketch of chains in the elastic region. Session 19, Slide 35.', 300)
    REG.raster('s19-yield-curve', 'Yield point of a ductile polymer',
               'Yield point of the nominal stress-strain curve of a ductile polymer. Session 19, Slide 36.', 600)
    REG.raster('s19-yield-chains', 'Chains at the yield point',
               'Molecular sketch of chains at the yield point. Session 19, Slide 36.', 300)
    REG.raster('s19-necking-curve', 'Necking on the stress-strain curve',
               'Necking region on the nominal stress-strain curve. Session 19, Slide 37.', 520)
    REG.raster('s19-necking-specimen', 'Specimen with a local neck',
               'Specimen with a local neck under tensile force. Session 19, Slide 37.', 300)
    REG.raster('s19-cold-drawing-curve', 'Cold drawing on the stress-strain curve',
               'Cold drawing region of the nominal stress-strain curve. Session 19, Slide 38.', 555)
    REG.raster('s19-cold-drawing-chains', 'Chains during cold drawing',
               'Chains unravelled and aligned with the applied stress during cold drawing. Session 19, Slide 38.', 300)
    REG.raster('s19-strain-hardening-curve', 'Strain hardening on the stress-strain curve',
               'Strain hardening region at the end of the nominal stress-strain curve. Session 19, Slide 39.', 585)
    REG.raster('s19-strain-hardening-chains', 'Oriented chains in strain hardening',
               'Oriented chains in the strain hardening region. Session 19, Slide 39.', 300)
    REG.raster('s19-failure-curve', 'Failure on the stress-strain curve',
               'Failure point at the end of the nominal stress-strain curve. Session 19, Slide 40.', 575)
    REG.raster('s19-deformation-stages', 'Molecular deformation stages',
               'Molecular deformation stages from elastic deformation to orientation of block segments and tie chains. Session 19, Slide 41.', 760)
    REG.raster('s19-strain-rate-pvc', 'PVC stress-strain at two strain rates',
               'Stress-strain curves of PVC at 1 mm/s and 0.05 mm/s. Session 19, Slide 42.', 445)
    REG.raster('s19-temperature-pmma', 'PMMA stress-strain at several temperatures',
               'Stress-strain curves of PMMA at temperatures from -40 to 140 degrees Celsius. Session 19, Slide 42.', 420)
    REG.raster('s19-yield-vs-crystallinity', 'Yield point against crystallization',
               'Yield point against degree of crystallization in weight percent. Session 19, Slide 43.', 355)
    REG.raster('s19-elastomer-stress-strain', 'Elastomer stress-strain curve',
               'Stress-strain curve of an elastomer with stretching of bonds and uncoiling of chains. Session 19, Slide 44.', 510)
    REG.raster('s19-elastomer-network-sketch', 'Elastomer network under force',
               'Crosslinked elastomer network under force. Session 19, Slide 44.', 310)
    REG.raster('s19-modulus-vs-temperature-crystallinity', 'Modulus against temperature for crystallinity',
               'Modulus of elasticity against temperature for 100 percent crystalline, 100 percent amorphous and 50/50 polymers. Session 19, Slide 45.', 325)
    REG.raster('s19-stiffness-vs-entanglement', 'Stiffness against temperature for molecular weight',
               'Stiffness or modulus against temperature for higher entanglement density and increasing molecular weight. Session 19, Slide 45.', 405)
    REG.raster('s19-crosslinking-modulus', 'Modulus against temperature for crosslinking',
               'Modulus of elasticity against temperature for increasing crosslinking, from no crosslinking to heavy crosslinking. Session 19, Slide 46.', 345)
    REG.raster('s19-elastomer-rubbery-region', 'Elastomer modulus and rubbery region',
               'Modulus of elasticity against temperature for an elastomer with its rubbery region. Session 19, Slide 46.', 345)
    REG.raster('s19-creep-recovery', 'Creep and recovery',
               'Applied stress and resulting strain against time for creep and recovery of a viscoelastic material. Session 19, Slide 47.', 410)
    REG.raster('s19-relaxation-curves', 'Stress relaxation',
               'Applied strain and induced stress against time for a viscoelastic material in stress relaxation. Session 19, Slide 48.', 365)
    REG.raster('s19-relaxation-modulus-log-time', 'Relaxation modulus against log time',
               'Logarithm of relaxation modulus against log time for several temperatures T1 to T7. Session 19, Slide 49.', 300)
    REG.raster('s19-relaxation-modulus-vs-temperature', 'Relaxation modulus against temperature',
               'Relaxation modulus against temperature with glassy, leathery, rubbery and viscous flow regions. Session 19, Slide 49.', 335)
    REG.raster('s19-ps-relaxation-atactic', 'Atactic polystyrene relaxation modulus',
               'Logarithm of relaxation modulus against temperature for atactic polystyrene: crystalline isotactic, lightly crosslinked and amorphous. Session 19, Slide 49.', 380)
    REG.raster('s19-common-polymer-repeat-units', 'Repeat units of common polymers',
               'Repeat units of PE, PP, PS, PVDF, PMMA, nylon and PVC. Session 19, Slide 50.', 760)
    REG.raster('s20-polymer-chain-structures', 'Chain networks of thermoplastics, thermosets and elastomers',
               'Schematic networks of thermoplastic, thermosetting and elastomer chains with their bonding strength. Session 20, Slide 6.', 600)
    REG.raster('s20-analogy-ice-cream-and-egg', 'Ice cream and egg analogy for thermoplastic and thermoset behaviour',
               'Ice cream that softens when heated and an egg that chemically decomposes when heated illustrate the two behaviours. Session 20, Slide 7.', 460)
    REG.raster('s20-commodity-thermoplastic-structures', 'Common commodity thermoplastics: repeat units and melting points',
               'Repeat-unit structures of the common commodity thermoplastics with recycling codes and melting points. Session 20, Slide 8.', 700)
    REG.raster('s20-commodity-thermoplastic-products', 'Commodity thermoplastic products',
               'Photos of products made from commodity thermoplastics with their molecular models. Session 20, Slide 10.', 500)
    REG.raster('s20-engineering-thermoplastic-structures', 'Engineering thermoplastics: polysulfone, nylon 6,6, polycarbonate',
               'Repeat-unit structures of polysulfone, nylon 6,6 and polycarbonate with their melting points and linkages. Session 20, Slide 9.', 500)
    REG.raster('s20-thermoset-polyester-epoxy-examples', 'Epoxy and polyester thermoset reactions',
               'Epoxy resin curing with ethylene diamine and the linear and cross-linked polyester reactions with styrene. Session 20, Slide 12.', 700)
    REG.raster('s20-thermoset-functional-units-table', 'Functional units and applications of thermosets',
               'Table of thermoset families with their functional-unit drawings and typical applications. Session 20, Slide 13.', 500)
    REG.raster('s20-natural-rubber-chain-segment', 'Natural rubber chain segment',
               'Structure of natural rubber and a segment of its polymer chain. Session 20, Slide 14.', 600)
    REG.raster('s20-natural-rubber-vulcanisation', 'Vulcanisation of natural rubber',
               'Chains of natural rubber before and after vulcanisation with sulphur bridges, forming a network. Session 20, Slide 14.', 600)
    REG.raster('s20-guttapercha-isomer', 'Gutta-percha trans isomer',
               'Gutta-percha trans isomer and its polymer chain segment, which is not an elastomer. Session 20, Slide 14.', 600)
    REG.raster('s20-elastomer-rubber-types', 'Elastomers: SBR, NBR, neoprene and polybutadiene',
               'Elastomer repeat units (SBR, NBR, polybutadiene, chloroprene) with a copolymer sketch and product photos. Session 20, Slide 15.', 700)
    REG.raster('s20-fibre-micrographs', 'Fibres: polyester and cotton, and polyacrylonitrile',
               'Colour electron micrograph of polyester and cotton fibres and electron micrograph of polyacrylonitrile fibres. Session 20, Slide 16.', 420)
    REG.raster('s20-extruder-schematic', 'Screw extruder schematic',
               'Cross-section of a screw extruder with its hopper, barrel heaters, screw, zones and die. Session 20, Slide 18.', 700)
    REG.raster('s20-injection-molding-schematic', 'Injection moulding: plunger and rotating screw',
               'Injection moulding machines with a plunger (a) and a rotating screw (b), with the mould, sprue and ejectors. Session 20, Slide 20.', 600)
    REG.raster('s20-injection-cavity-part-photo', 'Moulded part with runners from one shot',
               'Photo of parts moulded in one shot with their sprues, runners and gates. Session 20, Slide 21.', 600)
    REG.raster('s20-blow-molding-schematic', 'Extrusion blow moulding of bottles',
               'Extrusion blow moulding sequence: extruded parison, bottle mould, blow pin and blown bottle. Session 20, Slide 23.', 600)
    REG.raster('s20-rotational-molding-schematic', 'Rotational moulding machine',
               'Rotational moulding machine with two axes of rotation, a mould and a pressurising fluid line. Session 20, Slide 25.', 600)
    REG.raster('s20-thermoforming-processes', 'Four thermoforming processes',
               'Four thermoforming set-ups: straight vacuum forming, drape vacuum forming, force above sheet, and plug and ring forming. Session 20, Slide 27.', 680)
    REG.raster('s20-compression-molding-schematic', 'Compression moulding press',
               'Compression moulding press with platens, plunger, mould cavity and molding compound. Session 20, Slide 28.', 520)
    REG.raster('s20-process-cost-volume-chart', 'Production volume ranges per process',
               'Table of equipment cost, production rate and tooling cost per process with grey bars for typical production volumes. Session 20, Slide 33.', 620)
    REG.raster('s20-natural-rubber-stress-strain', 'Stress-strain curves of natural and vulcanized rubber',
               'Stress against strain of natural rubber and vulcanized natural rubber, copied from Session 20 Slide 14', 560)
    REG.raster('s20-transfer-molding-sequence', 'Sequence of operations in transfer molding',
               'Transfer molding in three steps: (a) plunger and pot with molding powder, (b) mold closed and cavities filled, (c) mold open and molded parts ejected, copied from Session 20 Slide 31', 760)
    REG.raster('t9-p7-molecular-weight-table', 'Problem 7 weight fraction table',
               'Table of molecular weight ranges and weight fractions for problem 7, copied from the Problems on Topic 9 sheet, page 2', 380)
    REG.raster('t9-p7-repeat-unit', 'Problem 7 polymer repeat unit',
               'Repeat unit of the alkene polymer with side chain (CH2)X CH3 for problem 7, copied from the Problems on Topic 9 sheet, page 2', 300)
    REG.raster('t9-p8-number-weight-fraction-table', 'Problem 8 number and weight fractions',
               'Table of molecular weight ranges with number fractions and weight fractions for problem 8, copied from the Problems on Topic 9 sheet, page 2', 420)
    REG.raster('t9-p9-density-crystallinity-table', 'Problem 9 density and crystallinity table',
               'Table of density and crystallinity of two polypropylene samples for problem 9, copied from the Problems on Topic 9 sheet, page 2', 320)


def theory():
    rasters()


def build():
    theory()
    return REG
