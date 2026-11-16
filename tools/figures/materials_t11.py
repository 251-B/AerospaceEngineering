"""Topic 11 figures for Aerospace Materials I: adhesives (Session 24).

Screenshot-First: every figure of this topic is a PNG crop of a slide of Session 24 (registered with
`REG.raster`; the crops are 200 DPI clips of the PDF pages, written once to vault/attachments/T11).
"""
from figures.svgkit import Registry

REG = Registry("T11")


def rasters():
    REG.raster('s24-joining-methods', 'Joining methods',
               'Physical, metallurgical and chemical joining systems (Session 24 Slide 2)', 620)
    REG.raster('s24-adhesion-cohesion-schematic', 'Adhesion and cohesion',
               'Adhesive molecules between two substrates: adhesion at the substrates, cohesion inside the adhesive (Session 24 Slide 4)', 420)
    REG.raster('s24-surface-roughness-block', 'Rough substrate surface',
               'Block of a rough substrate with the peaks and pores the adhesive fills (Session 24 Slide 9)', 360)
    REG.raster('s24-surface-roughness-profile', 'Roughness profile',
               'Roughness profile of a surface with its height parameters (Session 24 Slide 9)', 560)
    REG.raster('s24-wetting-states', 'Degrees of wetting',
               'Deficient, partial and total wetting of a drop on a rough surface (Session 24 Slide 9)', 520)
    REG.raster('s24-rigid-tough-flexible', 'Rigid, tough and flexible adhesives',
               'Polymerizing adhesives grouped by mechanical behaviour (Session 24 Slide 12)', 620)
    REG.raster('s24-adhesive-joint-process-flow', 'Making an adhesive joint',
               'Stages of an adhesive joint, from selection to assessment of joint resistance (Session 24 Slide 15)', 620)
    REG.raster('s24-joint-design-yes-no', 'Joint design: yes and no',
               'Tension, cleavage and peel joints to avoid, and their redesigned versions (Session 24 Slide 18)', 620)
    REG.raster('s24-joint-design-poor-good', 'Poor, good and very good joint designs',
               'Joint designs ranked as poor, good and very good, and combination joints of an adhesive with a rivet or a spot weld, copied from Session 24 Slide 19', 620)
    REG.raster('s24-lap-joint-types', 'Types of adhesive joints',
               'Lap, scarf, butt, strap and stepped joint cross-sections (Session 24 Slide 20)', 600)
    REG.raster('s24-surface-treatments', 'Surface treatments of the adherent',
               'A grit-blasted rough surface (surface roughness) and an anodized surface with its porous oxide layer (surface cleanliness), copied from Session 24 Slide 22', 300)
    REG.raster('s24-adhesive-application-photos', 'Adhesive application',
               'Adhesive applied by brush or film, dispensing gun and spray (Session 24 Slide 24)', 620)
    REG.raster('s24-tack-tests', 'Tack tests',
               'Tack tests of instantaneous adhesion: a block touched to the adhesive and lifted, and a drop rolling down an inclined plane over a distance, copied from Session 24 Slide 25', 700)
    REG.raster('s24-peel-tests', 'Peel tests',
               '180 degree, 90 degree and T-peel tests, and shear strength against adhesive thickness (Session 24 Slide 26)', 600)
    REG.raster('s24-brittle-tough-peel', 'Peeling of a brittle and a tough adhesive',
               'Behaviour of a brittle adhesive (left) and a tough adhesive (right) in a peeling test, copied from Session 24 Slide 27', 600)
    REG.raster('s24-epoxy-polyurethane-peel', 'Peeling of an epoxy and a polyurethane',
               'Peeling of a rigid epoxy, where only the line at the adhesion front carries the stress, and of a flexible polyurethane, where a volume of adhesive carries it, copied from Session 24 Slide 27', 700)
    REG.raster('s24-normal-shear-stresses', 'Normal and shear stresses on a joint',
               'Joints under normal stresses (compression and tension) and shear stresses, copied from Session 24 Slide 28', 640)
    REG.raster('s24-failure-modes-photos', 'Photographs of failed specimens',
               'Photographs of tensile shear specimens after cohesive failure (adhesive on both faces), adhesive failure (substrate and adhesive faces) and material failure, labelled in Spanish on the slide, copied from Session 24 Slide 30', 620)
    REG.raster('s24-acceptable-failure-modes', 'Acceptable failure modes',
               'Cohesive failure of the adhesive, surface ply delamination and adherend failure (Session 24 Slide 31)', 520)
    REG.raster('s24-unacceptable-failure-modes', 'Unacceptable failure modes',
               'Interface adhesion failure, adhesive peel and adhesive creep (Session 24 Slide 31)', 520)
    REG.raster('s24-tensile-characteristics', 'Tensile characteristics of adhesives',
               'Stress-strain curves of an adhesive at -40 C, ambient and 80 C (Session 24 Slide 33)', 480)
    REG.raster('s24-moisture-attack-interface', 'Moisture attack at the interface',
               'Segregation, hydrolysis and corrosion at the adhesive-adherent interface (Session 24 Slide 33)', 440)


def theory():
    rasters()


def build():
    theory()
    return REG
