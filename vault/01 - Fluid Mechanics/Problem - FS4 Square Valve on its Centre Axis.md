---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - superficie-plana
  - centro-de-presiones
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_4.pdf"
id: "fs4"
pill: "FS4: Square valve"
sheets:
  - 4
sim: plane-gate
tags_html:
  - "Plane surface"
  - "Centre of pressure"
  - "Moment balance"
  - "Simulator"
---

# Problem FS4: Square Valve on its Centre Axis

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: force and moment of the pressure by direct integration over strips (Notes.pdf, Eq. 5.11), checked with the centroid, the centre of pressure and Steiner's theorem.

## Statement

The square valve of side $L$ shown in the figure can turn about the horizontal axis that passes through its centre. Determine:

(a) The force $F$ that the fluid exerts on the valve.

(b) The value of the force $F_A$ that we must apply at the base of the valve to keep it closed.

Translated from the Spanish original.

![[attachments/FM-T5/fs4-statement.svg]]
*Statement figure (redrawn from fluid_statics_4.pdf, p. 1): square valve of side $L$ at the bottom of the right wall, pivoting about the horizontal axis $O$ through its centre; water depth $h$; $F_A$ is applied at the base of the valve*

Source: fluid_statics_4.pdf (page 1, sheet of 10-09-03). Notes.pdf, Chapter 5: Eqs. 5.10 and 5.11.

## Hypotheses, Data and Unknowns

- Water at rest, incompressible, density $\rho$; air at $p_a$ above the water and on the outer face of the valve, so only the gauge pressure counts (Section 4 of Topic 5).
- The valve is a vertical square plate of side $L$ with its lower edge on the bottom of the tank and its top edge at the depth $h - L$ below the free surface ($h \geq L$).
- The axis is horizontal, in the plane of the valve, through its centre; friction on the axis is neglected; the weight of the valve acts through the axis (homogeneous plate) and has no moment about it.
- $F_A$ is horizontal and acts at the base of the valve, as drawn.
- Data: $L$, $h$, $\rho$, $g$. Unknowns: $F$ and $F_A$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $L$ | side of the valve | m |
| $h$ | depth of the water | m |
| $F$, $F_A$ | water force, holding force | N |

## Coordinates and the Surface Element

Take $z$ vertical, pointing up, with $z = 0$ at the bottom of the tank (the lower edge of the valve), so the valve covers $0 \leq z \leq L$ and the free surface is at $z = h$. The depth of a point is $h - z$, and (5.10) gives the gauge pressure

$$ p(z) - p_a = \rho g (h - z) $$

The strip of the valve between $z$ and $z + dz$ has the width $L$ (horizontal side of the square) and the area $dA = L\,dz$. The unit normal towards the water is $\vec{n} = -\vec{e}_x$ (the water is on the left, $x$ points to the right, out of the tank), so the elementary force $-(p - p_a)\vec{n}\,dA = (p - p_a)\,dA\,\vec{e}_x$ pushes the valve outward. The axis is at $z = L/2$; the strip is at the signed distance $L/2 - z$ below it.

![[attachments/FM-T5/fs4-geometry.svg]]
*Left: side view; the gauge pressure on the valve grows linearly from $\rho g(h-L)$ at the top edge to $\rho g h$ at the bottom; the strip $dA = L\,dz$ at height $z$ has the arm $L/2 - z$ about the axis $O$. Right: front view of the valve, the horizontal axis through its centre and the strip*

## (a) The Force on the Valve

$$ F = \int_0^L \rho g (h - z)\,L\,dz = \rho g L\left[hz - \frac{z^2}{2}\right]_0^L = \rho g L\left(hL - \frac{L^2}{2}\right) - 0 = \rho g L^2\left(h - \frac{L}{2}\right) $$

horizontal, pointing out of the tank ($+\vec{e}_x$). Check with the centroid (Section 4.1 of Topic 5): the centroid of the square is at the depth $h - L/2$, so $F = \rho g (h - L/2) L^2$, the same.

## (b) The Moment about the Axis and the Holding Force

The strip below the axis ($z < L/2$) carries more pressure than the strip at the same distance above it, so the water tends to turn the valve with its lower edge outward. The moment about the axis, counted positive in that sense, is the force of each strip times its arm $L/2 - z$ (negative above the axis, where the strip turns the valve the other way):

$$ M = \int_0^L \left(\frac{L}{2} - z\right)\rho g (h - z)\,L\,dz $$

Expanding the integrand, $(L/2 - z)(h - z) = \tfrac{Lh}{2} - z\left(\tfrac{L}{2} + h\right) + z^2$, and integrating term by term with Barrow's rule between $0$ and $L$:

$$ M = \rho g L\left[\frac{Lh}{2}z - \frac{z^2}{2}\left(\frac{L}{2} + h\right) + \frac{z^3}{3}\right]_0^L = \rho g L\left(\frac{L^2 h}{2} - \frac{L^3}{4} - \frac{L^2 h}{2} + \frac{L^3}{3}\right) = \rho g L\cdot\frac{L^3}{12} = \frac{\rho g L^4}{12} $$

The terms in $h$ cancel: **the moment does not depend on the water depth**.

![[attachments/FM-T5/fs4-fbd.svg]]
*Free-body diagram of the valve: the water force $F$ acts at the centre of pressure, a distance $e$ below the axis $O$; $F_A$ acts at the base with the arm $L/2$; the axis reaction passes through $O$ and has no moment about it*

Moment balance of the valve about its axis: the axis reaction and the weight pass through the axis; $F_A$, at the base, has the arm $L/2$ and must turn the valve the other way:

$$ F_A\,\frac{L}{2} = \frac{\rho g L^4}{12} \quad\Longrightarrow\quad F_A = \frac{\rho g L^3}{6} $$

pointing into the tank ($-\vec{e}_x$).

**Check with the centre of pressure.** The centre of pressure is below the centroid by $e = I_C/(s_C A)$ (Section 4.1, with $\theta = 90^\circ$, $s$ = depth): $I_C = L\cdot L^3/12$, $s_C = h - L/2$, $A = L^2$, so

$$ e = \frac{L^4/12}{(h - L/2)L^2} = \frac{L^2}{12\,(h - L/2)}, \qquad F\,e = \rho g L^2\left(h - \frac{L}{2}\right)\frac{L^2}{12\,(h - L/2)} = \frac{\rho g L^4}{12} $$

As the depth grows the centre of pressure approaches the centre ($e \to 0$) but the force grows in the same proportion, so the moment stays $\rho g I_C$ (the general result $\rho g\sin\theta\,I_C$ of Section 4.1).

## Simulator: the Plane Gate

> [!example] Interactive simulator
> Change the depth, the inclination, the size and the shape of the gate and follow the pressure prism, C, CP and the moment about the centroidal axis.

## Answers and Checks

- (a) $F = \rho g L^2 (h - L/2)$, horizontal, out of the tank, at the depth $h - L/2 + L^2/(12(h - L/2))$.
- (b) $F_A = \rho g L^3/6$, horizontal, into the tank, independent of $h$.
- **Limiting case** $h = L$ (free surface at the top edge): $F = \rho g L^3/2$ and $e = L/6$, so the centre of pressure is at $L/3$ above the bottom, the centroid of the triangular pressure diagram.
- **Dimensions**: $\rho g L^3$ is (kg m$^{-3}$)(m s$^{-2}$)(m$^3$) = N.
- **Check against the official key**: fluid_statics_4.pdf gives $F = \rho g L^2(h - L/2)$, $M = \rho g L^4/12$ and $F_A = \rho g L^3/6$, the same results.
