"""A barred grand-design spiral (after NGC 1300's bar and M74 / M51's arms), face-on, 1200 x 1200,
transparent background. Layers, back to front: outer halo, diffuse disc, blurred arm light (blue),
dust lanes on the inner edge of each arm (dark, blurred), the bar and bulge (warm), resolved stars,
pink HII regions and blue young clusters along the arms, the nucleus."""
import math
import random

random.seed(1300)
S = 1200
C = S / 2
BAR = 120            # half-length of the bar
TILT_BAR = math.radians(-20)


def arm(arm_index, s):
    """Point at parameter s in [0, 1] along an arm that starts at the end of the bar and winds out."""
    theta0 = TILT_BAR + arm_index * math.pi
    t = s * 3.3                          # radians wound
    r = BAR * math.exp(0.42 * t)         # logarithmic spiral from the bar end
    a = theta0 + t
    return C + r * math.cos(a), C + r * math.sin(a), r


def polyline(index, s0, s1, n=220, shift=0.0):
    pts = []
    for k in range(n + 1):
        s = s0 + (s1 - s0) * k / n
        x, y, r = arm(index, s)
        if shift:
            # move towards the centre (inner edge of the arm)
            dx, dy = C - x, C - y
            d = math.hypot(dx, dy) or 1
            x, y = x + dx / d * shift * (6 + r * 0.06), y + dy / d * shift * (6 + r * 0.06)
        pts.append((x, y, r))
    return pts


def strokes(pts, colour, opacity, w0, w1):
    out = []
    for k in range(len(pts) - 1):
        f = k / (len(pts) - 1)
        w = w0 + (w1 - w0) * f
        op = opacity * (1 - 0.8 * f) ** 1.3
        out.append(f'<line x1="{pts[k][0]:.1f}" y1="{pts[k][1]:.1f}" x2="{pts[k + 1][0]:.1f}" y2="{pts[k + 1][1]:.1f}" '
                   f'stroke="{colour}" stroke-opacity="{op:.3f}" stroke-width="{w:.1f}" stroke-linecap="round"/>')
    return ''.join(out)


def svg():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">', '<defs>',
         '<radialGradient id="halo"><stop offset="0" stop-color="#c9d4ff" stop-opacity="0.30"/>'
         '<stop offset="0.45" stop-color="#7f8cff" stop-opacity="0.10"/><stop offset="1" stop-color="#7f8cff" stop-opacity="0"/></radialGradient>',
         '<radialGradient id="bulge"><stop offset="0" stop-color="#fffdf5"/><stop offset="0.18" stop-color="#ffefc7"/>'
         '<stop offset="0.45" stop-color="#ffc98a" stop-opacity="0.75"/><stop offset="1" stop-color="#ff9f5c" stop-opacity="0"/></radialGradient>',
         '<radialGradient id="bar"><stop offset="0" stop-color="#ffe7b8" stop-opacity="0.9"/>'
         '<stop offset="0.6" stop-color="#f7b878" stop-opacity="0.35"/><stop offset="1" stop-color="#f7b878" stop-opacity="0"/></radialGradient>',
         '<filter id="b30" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="30"/></filter>',
         '<filter id="b12" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="12"/></filter>',
         '<filter id="b5" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>',
         '<filter id="b2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.6"/></filter>',
         '<filter id="rough" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="4" seed="7" result="n"/>'
         '<feDisplacementMap in="SourceGraphic" in2="n" scale="70" xChannelSelector="R" yChannelSelector="G" result="d"/><feGaussianBlur in="d" stdDeviation="9"/></filter>',
         '<filter id="roughDust" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="11" result="n"/>'
         '<feDisplacementMap in="SourceGraphic" in2="n" scale="26" xChannelSelector="R" yChannelSelector="G" result="d"/><feGaussianBlur in="d" stdDeviation="2.4"/></filter>',
         '</defs>']
    # outer halo and diffuse disc
    o.append(f'<circle cx="{C}" cy="{C}" r="{C - 10}" fill="url(#halo)"/>')
    disc = ''.join(f'<circle cx="{C + random.gauss(0, 150):.1f}" cy="{C + random.gauss(0, 150):.1f}" r="{random.uniform(20, 50):.1f}" '
                   f'fill="#aebcff" opacity="0.035"/>' for _ in range(220))
    o.append(f'<g filter="url(#b30)">{disc}</g>')

    # broad arm light, then a brighter core of each arm
    wide, mid, faint = [], [], []
    for a in range(2):
        pts = polyline(a, 0, 1)
        wide.append(strokes(pts, '#8fa6ff', 0.26, 50, 130))
        # clumps of light along the arm instead of one smooth tube
        for _ in range(260):
            sx = random.random() ** 0.9
            x, y, r = arm(a, sx)
            rad = random.uniform(4, 10) + r * 0.03
            mid.append(f'<circle cx="{x + random.gauss(0, 4 + r * 0.04):.1f}" cy="{y + random.gauss(0, 4 + r * 0.04):.1f}" r="{rad:.1f}" '
                       f'fill="#d7e2ff" opacity="{0.22 * (1 - 0.7 * sx):.3f}"/>')
        # faint outer spurs (flocculent branches)
        for b in range(3):
            s0 = random.uniform(0.35, 0.7)
            spur = [(x + (C - x) * -0.04 * k / 60 + random.gauss(0, 2), y + (C - y) * -0.04 * k / 60 + random.gauss(0, 2), r)
                    for k, (x, y, r) in enumerate(polyline(a, s0, min(1, s0 + 0.28), 60))]
            faint.append(strokes(spur, '#9fb2ff', 0.18, 14, 30))
    o.append(f'<g filter="url(#rough)"><g filter="url(#b30)">{"".join(wide)}</g></g>')
    o.append(f'<g filter="url(#rough)">{"".join(faint)}</g>')
    o.append(f'<g filter="url(#rough)">{"".join(mid)}</g>')

    # dust lanes along the inner (leading) edge of the arms, M51 style
    dust = []
    for a in range(2):
        for s0 in (0.04, 0.2, 0.36, 0.5, 0.64):
            seg = polyline(a, s0, s0 + random.uniform(0.08, 0.13), 40, shift=1.0)
            dust.append(strokes(seg, '#05060f', 0.32, 3, 8))
        for _ in range(140):
            x, y, r = arm(a, random.uniform(0.05, 0.85))
            dx, dy = C - x, C - y
            d = math.hypot(dx, dy) or 1
            k = 8 + r * 0.05
            dust.append(f'<circle cx="{x + dx / d * k + random.gauss(0, 4):.1f}" cy="{y + dy / d * k + random.gauss(0, 4):.1f}" '
                        f'r="{random.uniform(2, 6):.1f}" fill="#05060f" opacity="0.22"/>')
    o.append(f'<g filter="url(#roughDust)">{"".join(dust)}</g>')

    # bar and bulge (NGC 1300)
    bx, by = math.cos(TILT_BAR) * BAR, math.sin(TILT_BAR) * BAR
    o.append(f'<g filter="url(#b12)"><ellipse cx="{C}" cy="{C}" rx="{BAR * 1.15:.0f}" ry="{BAR * 0.32:.0f}" '
             f'transform="rotate({math.degrees(TILT_BAR):.1f} {C} {C})" fill="url(#bar)"/></g>')
    o.append(f'<line x1="{C - bx:.1f}" y1="{C - by:.1f}" x2="{C + bx:.1f}" y2="{C + by:.1f}" stroke="#ffd9a0" stroke-opacity="0.6" '
             f'stroke-width="22" stroke-linecap="round" filter="url(#b12)"/>')
    o.append(f'<ellipse cx="{C}" cy="{C}" rx="105" ry="78" transform="rotate({math.degrees(TILT_BAR):.1f} {C} {C})" fill="url(#bulge)"/>')

    # resolved stars: blue-white in the arms, warm in the bulge, sparse in the disc
    stars = []
    for a in range(2):
        for _ in range(2400):
            s = random.random() ** 0.8
            x, y, r = arm(a, s)
            spread = 6 + r * 0.075
            stars.append((x + random.gauss(0, spread), y + random.gauss(0, spread),
                          random.choices(['#ffffff', '#dfe8ff', '#b8cbff', '#ffe4bd'], [30, 40, 22, 8])[0],
                          random.choice([0.5, 0.7, 0.9, 1.1, 1.4]), max(0.2, 1 - s * 0.6 + random.uniform(-0.2, 0.1))))
    for _ in range(900):
        rr = abs(random.gauss(0, 70))
        ang = random.uniform(0, 2 * math.pi)
        stars.append((C + rr * math.cos(ang) * 1.3, C + rr * math.sin(ang), '#ffe9c4', random.choice([0.5, 0.7, 0.9]), 0.6))
    for _ in range(700):
        rr = random.uniform(80, C - 40)
        ang = random.uniform(0, 2 * math.pi)
        stars.append((C + rr * math.cos(ang), C + rr * math.sin(ang), '#e8eeff', random.choice([0.4, 0.6]), max(0.1, 0.6 - rr / 900)))
    o.append(''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}" opacity="{op:.2f}"/>' for x, y, c, r, op in stars))

    # HII regions (pink) and young clusters (blue) on the outer edge of the arms
    knots = []
    for a in range(2):
        for _ in range(36):
            s = random.uniform(0.12, 0.95)
            x, y, r = arm(a, s)
            dx, dy = x - C, y - C
            d = math.hypot(dx, dy) or 1
            k = random.uniform(0, 10 + r * 0.05)
            x, y = x + dx / d * k + random.gauss(0, 5), y + dy / d * k + random.gauss(0, 5)
            if random.random() < 0.55:
                knots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(3, 7):.1f}" fill="#ff6fae" opacity="0.55"/>')
                knots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.3" fill="#ffd1e6" opacity="0.9"/>')
            else:
                knots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(3, 6):.1f}" fill="#8ec5ff" opacity="0.45"/>')
                knots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.2" fill="#ffffff"/>')
    o.append(f'<g filter="url(#b2)">{"".join(knots)}</g>')
    # nucleus
    o.append(f'<circle cx="{C}" cy="{C}" r="26" fill="#fffaf0" opacity="0.9" filter="url(#b5)"/><circle cx="{C}" cy="{C}" r="6" fill="#ffffff"/>')
    o.append('</svg>')
    return ''.join(o)


def knot_point(arm_index, s):
    """Where the subject knots sit (same geometry), on the 1000 x 1000 knot overlay."""
    x, y, _ = arm(arm_index, s)
    return x * 1000 / S, y * 1000 / S


if __name__ == '__main__':
    import pathlib
    here = pathlib.Path(__file__).parent
    (here / 'galaxy.html').write_text('<!doctype html><html><body style="margin:0;background:transparent">' + svg() + '</body></html>')
    (here / 'galaxy-dark.html').write_text('<!doctype html><html><body style="margin:0;background:#060914">' + svg() + '</body></html>')
    print('ok')
