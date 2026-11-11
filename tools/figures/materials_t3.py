"""Topic 3 figures for Aerospace Materials I: all copied from the Session 5 slides as PNG crops."""
from figures.svgkit import Registry

REG = Registry("T3")


def build():
    REG.raster("barriers", "Activation energy for vacancy and interstitial jumps",
               "Activation energy along the path of a jumping atom: the vacancy jump (solid curve, barrier E_v) needs more "
               "energy than the interstitial jump (dashed curve, barrier E_i); the atom arrangements before, during and "
               "after each jump are sketched above (vacancy) and below (interstitial). Copied from Session 5 Slide 13", 440)
    REG.raster("fick1", "Steady-state concentration profile",
               "Steady state: the concentration of the diffusing species falls linearly from C_A at x_A to C_B at x_B, so "
               "the gradient, and with it the flux, is the same at every point. Copied from Session 5 Slide 17", 340)
    REG.raster("fick2-b", "Error-function profile in a semi-infinite solid",
               "Concentration against the distance from the surface in a semi-infinite solid: C_s at the surface, C_0 deep "
               "inside, and C_x at depth x; the brackets C_s − C_0 and C_x − C_0 are the two differences of the erf "
               "solution. Copied from Session 5 Slide 20", 420)
    REG.raster("fick2-a", "Profiles at three times",
               "Concentration profiles for a constant surface concentration C_s at three times t1 < t2 < t3: the profile "
               "moves deeper into the solid as time goes on. The curves are a sketch of the slide, not computed from the "
               "erf solution. Copied from Session 5 Slide 18", 460)
    REG.raster("arrhenius", "Arrhenius plot of the diffusivity",
               "ln D against 1/T: a straight line of slope −E/R, where E is the activation energy E_D of the text. "
               "Copied from Session 5 Slide 26", 300)
    return REG
