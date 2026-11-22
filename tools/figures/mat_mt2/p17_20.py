"""Figures of the Part II problems P17 to P20 of the Midterm 2 bank (archetype loaded-bar, Unit 5).

p19-load-unload-path: loading of the aluminium-alloy specimen of P19 beyond yield, elastic unloading parallel to the
elastic line and elastic reloading to 30 kN, to scale (strain axis 0 to 0.04, stress in MPa).
p20-resilience-area: the modulus of resilience of the titanium alloy of P20 as the area of the elastic triangle.
"""
from figures.svgkit import Canvas, line, text, poly, dot
from figures.mat_mt2.common import figure
from figures.mat_mt2.u5 import Map, axes, sample

# P19 data (MPa and strain), the same numbers as the note
E19, SY19 = 69000.0, 275.0
S_LOAD, EPS_LOAD = 353.68, 0.035
S_RE = 265.26
EPS_Y = SY19 / E19
EPS_P = EPS_LOAD - S_LOAD / E19


def _harden(e):
    t = (e - EPS_Y) / (EPS_LOAD - EPS_Y)
    return SY19 + (S_LOAD - SY19) * (1 - (1 - t) ** 2.4)


@figure("p19-load-unload-path",
        "Stress-strain path of the specimen: elastic line to the yield strength of 275 MPa, plastic loading to "
        "353.7 MPa at a strain of 0.035, unloading along a line parallel to the elastic line to a permanent strain "
        "of 0.0299, and elastic reloading to 265.3 MPa",
        "Loading O-Y-B beyond yield (yielding idealised at the end of the elastic line Y), unloading B-P parallel to the elastic line, reloading P-R (to scale)")
def load_unload():
    c = Canvas(520, 330)
    m = Map(70, 270, 10500, 0.6)
    axes(c, m, 0.042, 420, "engineering strain ε", "σ (MPa)",
         xt=[(0.0, "0"), (0.01, "0.01"), (0.02, "0.02"), (0.03, "0.03"), (0.04, "0.04")],
         yt=[(100, "100"), (200, "200"), (300, "300"), (400, "400")])
    # loading: elastic line and hardening curve
    poly(c, m.pts([(0, 0), (EPS_Y, SY19)]), "ACC", 2.4)
    poly(c, m.pts(sample(_harden, EPS_Y, EPS_LOAD, 60)), "ACC", 2.4)
    # unloading parallel to the elastic line
    line(c, m.p(EPS_LOAD, S_LOAD), m.p(EPS_P, 0), "BLUE", 2.2, head=True)
    # reloading point R on the same line
    eps_r = EPS_P + S_RE / E19
    dot(c, m.p(eps_r, S_RE), 4, "HEAD", "GREEN")
    # guide lines
    line(c, m.p(0, S_LOAD), m.p(EPS_LOAD, S_LOAD), "EDGE", 0.8, "3,3")
    line(c, m.p(EPS_LOAD, 0), m.p(EPS_LOAD, S_LOAD), "EDGE", 0.8, "3,3")
    line(c, m.p(0, SY19), m.p(EPS_Y, SY19), "EDGE", 0.8, "3,3")
    for (x, y), s, dx, dy, anc in [((0, 0), "O", -8, -6, "end"), ((EPS_Y, SY19), "Y", -6, -8, "end"),
                                   ((EPS_LOAD, S_LOAD), "B", 6, -8, "start"), ((EPS_P, 0), "P", -6, -8, "end"),
                                   ((eps_r, S_RE), "R", -9, 4, "end")]:
        px, py = m.p(x, y)
        dot(c, (px, py), 3.5, "HEAD", "HEAD")
        text(c, (px + dx, py + dy), s, "HEAD", anc, 13, "700")
    px, py = m.p(0.0, S_LOAD)
    text(c, (px + 6, py - 6), "353.7 MPa", "TEXT", "start", 11)
    px, py = m.p(0.0, SY19)
    text(c, (px + 44, py + 14), "σy = 275 MPa", "TEXT", "start", 11)
    px, py = m.p(EPS_P, 0)
    text(c, (px - 14, py - 34), "εp = 0.0299", "BLUE", "end", 11.5, "700")
    px, py = m.p(EPS_LOAD, 0)
    text(c, (px + 6, py - 40), "ε = 0.035", "TEXT", "start", 11.5)
    px, py = m.p(EPS_P + 150 / E19, 150)
    text(c, (px - 10, py + 4), "slope E", "BLUE", "end", 11.5)
    return c


# P20 data
SY20, E20 = 880.0, 107000.0
EPS_Y20 = SY20 / E20


@figure("p20-resilience-area",
        "Elastic part of the stress-strain line of the titanium alloy: a straight line of slope E = 107 GPa up to "
        "the yield strength of 880 MPa at a strain of 0.00822; the shaded triangle under it is the modulus of resilience",
        "The modulus of resilience is the area under the elastic line from 0 to the yield strain")
def resilience():
    c = Canvas(440, 290)
    m = Map(70, 240, 38000, 0.22)
    axes(c, m, 0.0105, 1000, "strain ε", "σ (MPa)",
         xt=[(0.0, "0"), (EPS_Y20, "εy = 0.00822")], yt=[(SY20, "880")])
    poly(c, m.pts([(0, 0), (EPS_Y20, SY20), (EPS_Y20, 0)]), "GREEN", 1.0, fill="GREEN", close=True, opacity=0.18)
    poly(c, m.pts([(0, 0), (EPS_Y20, SY20)]), "ACC", 2.4)
    line(c, m.p(0, SY20), m.p(EPS_Y20, SY20), "EDGE", 0.8, "3,3")
    line(c, m.p(EPS_Y20, 0), m.p(EPS_Y20, SY20), "EDGE", 0.9, "3,3")
    px, py = m.p(EPS_Y20 * 0.66, SY20 * 0.27)
    text(c, (px, py), "Ur", "GREEN", "middle", 15, "700")
    px, py = m.p(EPS_Y20 * 0.45, SY20 * 0.45)
    text(c, (px - 10, py), "σ = Eε", "ACC", "end", 12.5, "700")
    return c
