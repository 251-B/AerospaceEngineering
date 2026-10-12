"""Topic 3 figures for Aerospace Materials I: diffusion barriers, Fick's first and second laws, Arrhenius plot.
Schematic shapes; the Fick's second law profiles are the erf solution itself with arbitrary D t values."""
import math

from figures.svgkit import Canvas, Registry, curve, line, text

REG = Registry("T3")


def barriers():
    c = Canvas(540, 260)
    x0, x1, base = 60, 500, 210
    xs = [x0 + (x1 - x0) * k / 400 for k in range(401)]
    px = lambda x: x                                             # noqa: E731
    bump = lambda x, h: h * math.exp(-((x - 280) / 55) ** 2)     # noqa: E731
    line(c, (x0, base), (x1, base)); line(c, (x0, 30), (x0, base))
    text(c, (66, 40), "Energy", "HEAD", weight="700"); text(c, (x1, base + 20), "position of the moving atom", anchor="end")
    curve(c, lambda x: bump(x, 1.0), xs, px, base, 150, 20, base + 1, "BLUE", 2.4)
    curve(c, lambda x: bump(x, 0.45), xs, px, base, 150, 20, base + 1, "ACC", 2.4, "6,4")
    line(c, (380, base - 150), (380, base), "BLUE", 1.2, "3,3"); text(c, (388, base - 120), "Eᵥ (vacancy)", "BLUE", weight="700")
    line(c, (420, base - 68), (420, base), "ACC", 1.2, "3,3"); text(c, (428, base - 40), "Eᵢ (interstitial)", "ACC", weight="700")
    line(c, (280, base - 150), (380, base - 150), "BLUE", 1, "2,3"); line(c, (280, base - 68), (420, base - 68), "ACC", 1, "2,3")
    text(c, (120, base - 10), "start", "TEXT", "middle"); text(c, (440, base - 10), "end", "TEXT", "middle")
    REG.put("barriers", c, "Activation energy for vacancy and interstitial diffusion",
            "The atom must cross an energy barrier to jump to the next site: it is lower for interstitial diffusion "
            "(Eᵢ) than for vacancy diffusion (Eᵥ). Schematic")


def fick1():
    c = Canvas(540, 260)
    xa, xb, top, bot = 150, 400, 60, 210
    line(c, (80, bot), (500, bot)); line(c, (80, 30), (80, bot))
    text(c, (86, 40), "Concentration C", "HEAD", weight="700"); text(c, (500, bot + 20), "position x", anchor="end")
    line(c, (80, top), (xa, top), "ACC", 2.6); line(c, (xa, top), (xb, 160), "ACC", 2.6); line(c, (xb, 160), (480, 160), "ACC", 2.6)
    line(c, (xa, top), (xa, bot), "EDGE", 1, "3,3"); line(c, (xb, 160), (xb, bot), "EDGE", 1, "3,3")
    text(c, (xa, bot + 18), "x₁", "TEXT", "middle"); text(c, (xb, bot + 18), "x₂", "TEXT", "middle")
    text(c, (xa - 8, top - 8), 'C<tspan baseline-shift="sub" font-size="72%">ext</tspan>', "ACC", "end", weight="700"); text(c, (xb + 8, 152), 'C<tspan baseline-shift="sub" font-size="72%">int</tspan>', "ACC", weight="700")
    line(c, (230, 185), (330, 185), "BLUE", 2.4, head=True); text(c, (280, 175), "flux J", "BLUE", "middle", weight="700")
    text(c, (300, 70), "constant slope ΔC/Δx", "TEXT")
    REG.put("fick1", c, "Steady-state concentration profile",
            "Steady state: the concentration falls linearly from $C_{ext}$ to $C_{int}$ across the layer, so the gradient "
            "ΔC/Δx and the flux J are the same at every point and do not change with time")


def fick2():
    c = Canvas(540, 270)
    x0, x1, top, bot = 70, 500, 50, 220
    line(c, (x0, bot), (x1, bot)); line(c, (x0, 30), (x0, bot))
    text(c, (76, 40), "Concentration C", "HEAD", weight="700"); text(c, (x1, bot + 20), "distance from the surface x", anchor="end")
    cs, c0 = 1.0, 0.1
    py = lambda v: bot - v * (bot - top)   # noqa: E731
    xs = [k / 300 * 4.0 for k in range(301)]
    px = lambda x: x0 + x / 4.0 * (x1 - x0)  # noqa: E731
    for dt, col, lab in ((0.02, "PINK", "t₁"), (0.25, "GREEN", "t₂"), (1.2, "BLUE", "t₃")):
        f = lambda x, dt=dt: c0 + (cs - c0) * (1 - math.erf(x / (2 * math.sqrt(dt))))   # noqa: E731
        curve(c, lambda x, f=f: f(x), xs, px, bot, bot - top, 0, bot + 1, col, 2.4)
        xl = 2 * math.sqrt(dt) * 0.9
        text(c, (px(xl) + 6, py(f(xl)) - 6), lab, col, weight="700")
    line(c, (x0, py(c0)), (x1, py(c0)), "EDGE", 1, "4,4")
    text(c, (x0 - 6, py(cs) + 4), "Cₛ", "HEAD", "end", weight="700"); text(c, (x0 - 6, py(c0) + 4), "C₀", "HEAD", "end", weight="700")
    text(c, (340, 80), "t₁ &lt; t₂ &lt; t₃", "HEAD", weight="700")
    REG.put("fick2", c, "Concentration profiles in a semi-infinite solid",
            "Non-steady state in a semi-infinite solid with constant surface concentration Cₛ and initial "
            "concentration C₀: the profile (the erf solution) moves deeper into the solid as time goes on")


def arrhenius():
    c = Canvas(540, 260)
    line(c, (80, 220), (500, 220), head=True); line(c, (80, 220), (80, 30), head=True)
    text(c, (500, 240), "1/T", "TEXT", "end"); text(c, (90, 40), "ln D", "HEAD", weight="700")
    line(c, (110, 60), (440, 200), "ACC", 2.8)
    line(c, (250, 119.4), (330, 119.4), "EDGE", 1.2, "3,3"); line(c, (330, 119.4), (330, 153.3), "EDGE", 1.2, "3,3")
    text(c, (338, 142), 'slope = −E<tspan baseline-shift="sub" font-size="72%">D</tspan>/R', "ACC", weight="700")
    REG.put("arrhenius", c, "Arrhenius plot of the diffusivity",
            "Arrhenius plot: ln D falls linearly with 1/T, with slope $-E_D/R$. Schematic")


def build():
    barriers()
    fick1()
    fick2()
    arrhenius()
    return REG
