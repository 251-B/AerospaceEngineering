"""Figure of bank item P13 (capsule descent with two parachute stages)."""
from figures.em_common import figure
from figures.mech import S, Scene, bold


def _capsule(sc, c, w=0.55, h=0.5):
    """Capsule seen from the side: truncated cone, narrow top, heat shield at the bottom."""
    x, y = c
    sc.poly([(x - 0.18, y + h / 2), (x + 0.18, y + h / 2), (x + w / 2, y - h / 2), (x - w / 2, y - h / 2)], "HEAD", 1.8,
            fill="ACC", opacity=0.9, close=True)


def _canopy(sc, top, r, lines_to):
    """Parachute canopy (a dome of radius r whose rim is at height top[1]) with its suspension lines."""
    cx, cy = top
    sc.arc((cx, cy), r, 0, 180, "HEAD", 2.0)
    sc.line((cx - r, cy), (cx + r, cy), "HEAD", 1.2)
    for sx in (-r, -r / 3, r / 3, r):
        sc.line((cx + sx, cy), lines_to, "EDGE", 1.0)


@figure("p13-two-stage-descent",
        "A capsule falling vertically, drawn at two instants: first under a small drogue parachute, then under the large "
        "main parachute; the coordinate y points downward from the release point O; on the capsule act the weight m g "
        "downward and the drag c v squared upward, and the velocity v points down",
        r"Two-stage descent: coordinate $y$ downward from the release point $O$, velocity $v=\dot y$; forces on the capsule: "
        r"weight $mg$ (down) and drag $cv^2$ (up), with $c=c_1$ under the drogue (stage 1) and $c=c_2\gg c_1$ under the "
        r"main parachute (stage 2)")
def p13():
    sc = Scene(640, 380, (40, 30), 58)      # world y grows upward; the drawing goes downward from O
    O = (0.6, -0.4)
    # downward coordinate y
    sc.dashed(O, (O[0], -5.3))
    sc.vec(O, (O[0], -1.5), "y", "BLUE", 1.9, name_off=(-14, 8))
    sc.label(O, "O", "BLUE", "end", 16, dx=-8, dy=4)
    sc.gravity((5.75, -2.6), 0.9, "g")
    # ---- stage 1: drogue --------------------------------------------------------------
    C1 = (3.6, -4.1)
    _capsule(sc, C1)
    _canopy(sc, (C1[0], -2.0), 0.45, (C1[0], C1[1] + 0.25))
    sc.note((C1[0], -2.0), "drogue", anchor="middle", dy=-34, size=12)
    sc.vec((C1[0] - 0.75, C1[1] + 0.05), (C1[0] - 0.75, C1[1] + 1.15), S("c", "1", "") + "v²", "PINK", 2.0, name_off=(-26, 8))
    sc.vec((C1[0] + 0.0, C1[1] - 0.3), (C1[0] + 0.0, C1[1] - 1.25), "mg", "PINK", 2.0, name_off=(-18, 4))
    sc.vec((C1[0] + 0.7, C1[1] + 0.1), (C1[0] + 0.7, C1[1] - 0.8), bold("v"), "BLUE", 1.9, name_off=(12, 0))
    sc.note((C1[0], -5.8), "stage 1:  c = c₁", anchor="middle", size=13)
    # ---- stage 2: main parachute ----------------------------------------------------------
    C2 = (7.9, -4.1)
    _capsule(sc, C2)
    _canopy(sc, (C2[0], -1.6), 1.25, (C2[0], C2[1] + 0.25))
    sc.note((C2[0], -1.6), "main parachute", anchor="middle", dy=-80, size=12)
    sc.vec((C2[0] - 1.0, C2[1] + 0.05), (C2[0] - 1.0, C2[1] + 1.15), S("c", "2", "") + "v²", "PINK", 2.0, name_off=(-26, 8))
    sc.vec((C2[0] + 0.0, C2[1] - 0.3), (C2[0] + 0.0, C2[1] - 1.25), "mg", "PINK", 2.0, name_off=(-18, 4))
    sc.vec((C2[0] + 0.85, C2[1] + 0.1), (C2[0] + 0.85, C2[1] - 0.8), bold("v"), "BLUE", 1.9, name_off=(12, 0))
    sc.note((C2[0], -5.8), "stage 2:  c = c₂ ≫ c₁", anchor="middle", size=13)
    return sc
