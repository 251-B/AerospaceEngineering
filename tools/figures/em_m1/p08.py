"""Figure of bank item P08 (seismic accelerometer on a vibrating base)."""
from figures.em_common import figure
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head


def _double_arrow(sc, a, b, col="PINK", w=1.8):
    sc.line(a, b, col, w)
    arrow_head(sc.c, sc.P(a), sc.P(b), col, 9)
    arrow_head(sc.c, sc.P(b), sc.P(a), col, 9)


@figure("p08-seismic-accelerometer",
        "A case whose floor moves vertically by z(t) with respect to a fixed datum; inside, a proof mass m sits on a spring k "
        "and a damper c fixed to the case floor; x is the height of the mass above its static equilibrium level in the case; "
        "gravity points down",
        r"Seismic accelerometer: the case floor moves as $z(t)=Z\cos\nu t$ with respect to the fixed datum of $S_0$; the proof "
        r"mass $m$ is held by the spring $k$ and the damper $c$; $x$ is measured in the case frame $S_1$ from the static "
        r"equilibrium level (both $z$ and $x$ positive upwards)")
def p08():
    sc = Scene(640, 400, (20, 380), 60)
    # fixed wall with the inertial frame and the datum z = 0
    sc.ground((0.9, 0.4), (0.9, 5.9), side=1)
    sc.axes((1.25, 1.2), 0, 0.9, ("", "y"), "BLUE")
    sc.label((1.25, 1.2), S("S", "0"), "BLUE", "start", 15, dx=8, dy=18)
    sc.dashed((0.9, 1.2), (6.9, 1.2))
    sc.note((6.95, 1.2), "datum z = 0", "TEXT", "start", 13, dy=4)
    # case (floor drawn thick, displaced upwards by z)
    fl = 1.75
    sc.poly([(3.0, 5.7), (3.0, fl), (6.4, fl), (6.4, 5.7)], "HEAD", 2.2)
    sc.line((2.95, fl), (6.45, fl), "HEAD", 4.0)
    sc.note((6.5, 5.45), S("S", "1") + " (case)", "TEXT", "start", 13)
    # base motion
    _double_arrow(sc, (4.65, 0.45), (4.65, 1.45))
    sc.note((4.8, 0.75), "z(t) = Z cos νt", "PINK", "start", 14)
    # z dimension from the datum to the floor
    sc.dashed((2.4, fl), (2.95, fl))
    sc.vec((2.55, 1.2), (2.55, fl), None, "BLUE", 1.8, head=8)
    sc.label((2.55, (1.2 + fl) / 2), "z", "BLUE", "end", 17, dx=-8, dy=6)
    # spring and damper from the floor to the mass
    mb = 3.55
    sc.spring((3.85, fl), (3.85, mb), coils=6, amp=9)
    sc.label((3.85, (fl + mb) / 2), "k", "TEXT", "end", 17, dx=-16, dy=5)
    sc.damper((5.45, fl), (5.45, mb))
    sc.label((5.45, (fl + mb) / 2), "c", "TEXT", "start", 17, dx=20, dy=5)
    # proof mass
    sc.poly([(3.45, mb), (5.85, mb), (5.85, mb + 0.9), (3.45, mb + 0.9)], "HEAD", 2.0, fill="ACC", close=True, opacity=0.85)
    sc.label((4.65, mb + 0.45), "m", "HEAD", "middle", 18, dy=6)
    # static equilibrium level (fixed in the case) and the relative coordinate x
    eq = 3.0
    sc.dashed((3.0, eq), (6.4, eq))
    sc.note((6.5, eq), "static equilibrium", "TEXT", "start", 13, dy=4)
    sc.dashed((5.85, mb), (6.3, mb))
    sc.vec((6.1, eq), (6.1, mb), None, "BLUE", 1.8, head=8)
    sc.label((6.1, (eq + mb) / 2), "x", "BLUE", "start", 17, dx=8, dy=6)
    # gravity
    sc.gravity((8.6, 4.6), 0.9, "g")
    return sc
