"""Problem figures of Fluid Mechanics Topic 6 (dimensional analysis sheets DA1-DA14).

The statement figure of each sheet is a PNG crop of page 1 of the sheet (the scans carry the handwritten key next to
it), copied to vault/attachments/FM-T6/ and registered with REG.raster. Only DA12 stays a redrawn SVG: in the sheet
the key is handwritten over the figure. Registered in the FM-T6 registry of tools/figures/fluids_t6.py; colour code
as there (BLUE fluid and velocities, GREEN geometry, HEAD/TEXT/EDGE lines and labels).
"""
from figures.fluids_t6 import lab
from figures.svgkit import Canvas, arrow, dim, line, pathd, poly

REG = None


def put(name, c, title, caption):
    REG.put(name, c, title, caption)


# (name, title, caption without the source, crop width in px)
SHEETS = (
    ("da2-statement", "Wind over a wire",
     "A wind stream of velocity U, density ρ and viscosity μ over a wire of radius R; above the critical velocity the wake "
     "becomes a periodic street of vortices of opposite circulation", 640),
    ("da3-statement", "Stirrer in a tank of tar",
     "Section view: a container of diameter D holding a volume V of tar, free surface at p_a, with a 3-blade stirrer of "
     "height h at its bottom rotating at Ω; gravity g downward", 400),
    ("da5-statement", "Measured power of the wind turbine",
     "Power W_1 delivered by the turbine of diameter D = 5 m against its angular velocity n_1 for a wind of U = 10 m/s "
     "(plot of the sheet)", 560),
    ("da6-statement", "Tsunami against a protection wall",
     "A tsunami of height h travelling with velocity U towards a coastal protection wall of height H; the unknowns are U "
     "and the impact force per unit width of wall F", 760),
    ("da7-statement", "Shrouded fan of a submarine",
     "A nozzle of inlet area A_e and outlet area A_s with a fan inside that gives the power Ẇ to water of density ρ and "
     "viscosity μ; E is the thrust", 760),
    ("da10-statement", "Two-belt viscous pump",
     "Two parallel belts of length L, a distance h ≪ L apart, driven at V_u and V_l, drag liquid of density ρ and "
     "viscosity μ from a reservoir at reduced pressure P_0 to one at P_0 + ΔP", 700),
    ("da11-statement", "Wave generator",
     "Above, the pool of liquid (ρ, μ) of undisturbed depth H; below, the lateral wall moved harmonically, "
     "x = A cos(2πωt), by the power Ẇ, generating gravity waves", 520),
    ("da13-statement", "Module descending under a parachute",
     "A module of mass m hangs from a parachute of diameter D and falls at its terminal velocity V under gravity g", 400),
    ("da14-statement", "Circular cavity inside a rotating case",
     "A circular cavity of radius R full of liquid (ρ, μ), initially at rest, inside a case at temperature T_0 that is "
     "set to rotate at Ω at t = 0⁺", 520),
)


# ------------------------------------------------------------------------------------------------- DA12
def da12():
    # INVIABLE: handwriting over the figure in the official sheet
    c = Canvas(660, 280)
    # missile
    poly(c, [(300, 140), (330, 115), (520, 115), (520, 165), (330, 165)], "HEAD", 2.0, fill="EDGE", close=True,
         opacity=0.12)
    poly(c, [(470, 115), (520, 80), (540, 80), (520, 115)], "HEAD", 1.6, close=True)
    poly(c, [(470, 165), (520, 200), (540, 200), (520, 165)], "HEAD", 1.6, close=True)
    dim(c, (345, 115), (345, 165), "D", "GREEN", (14, 6), size=16)
    # bow shock
    pathd(c, "M430,20 C300,60 250,110 250,140 C250,170 300,220 430,260", "ACC", 2.2)
    lab(c, (440, 30), "bow shock", "ACC", "start", 14, italic=False)
    line(c, (250, 185), (300, 185), "GREEN", 1.2, head=True)
    line(c, (300, 185), (250, 185), "GREEN", 1.2, head=True)
    lab(c, (275, 205), "d", "GREEN", "middle", 17)
    arrow(c, (70, 140), (160, 140), "BLUE", 2.4, 11)
    lab(c, (115, 128), "U", "BLUE", "middle", 18)
    lab(c, (115, 90), "ρ, μ", "HEAD", "middle", 17)
    lab(c, (115, 175), "c", "HEAD", "middle", 17)
    arrow(c, (610, 30), (610, 80), "HEAD", 2.0, 10)
    lab(c, (622, 60), "g", "HEAD", "start", 18)
    put("da12-statement", c, "Supersonic missile with its bow shock",
        "Statement figure (redrawn from DA12.pdf, frame of the missile): a gas of density ρ, viscosity μ and sound "
        "speed c meets the missile of diameter D at a speed U > c; a bow shock stands at a distance d ahead of the tip")


def build(reg, raster):
    global REG
    REG = reg
    da12()
    for name, title, cap, w in SHEETS:
        reg.raster(name, title, f"{cap}. Copied from {name[:-10].upper()}.pdf, p. 1.", width=w)
    reg.raster("da8-statement", "Robotic fly wings in mineral oil",
               "Photograph of the sheet (crop of DA8.pdf): the pair of robotic wings of Dickinson's facility, "
               "which flap in a tank of mineral oil", width=660)
