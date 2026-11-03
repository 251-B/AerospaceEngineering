---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - compuerta
  - centro-de-presiones
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_9.pdf"
id: "fs9"
pill: "FS9: Hinged gate"
sheets:
  - 9
tags_html:
  - "Plane surface"
  - "Moment about a hinge"
  - "Centre of pressure"
  - "Opening condition"
---

# Problem FS9: Hinged Gate Opening Height

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: the moment of the pressure about the hinge by direct integration (Notes.pdf, Eq. 5.11), and its interpretation with the centre of pressure.

## Statement

Calculate the height $H$ for which the hinged gate shown in the figure will open, if the hinge is at a distance $l$ from the upper wall and at a known distance $h$ from the floor ($h < l$).

Translated from the Spanish original. The upper wall is the fixed wall above the gate, so $l$ is measured from the top edge of the gate.

![[attachments/FM-T5/fs9-statement.svg]]
*Statement figure (redrawn from fluid_statics_9.pdf, p. 1): gate hinged at a distance $l$ below its top edge and $h < l$ above the floor; the water surface is $H$ above the top edge; air at $p_a$ on both sides; a stop at the floor on the dry side*

Source: fluid_statics_9.pdf (page 1, sheet of 10-09-04). Notes.pdf, Chapter 5: Eqs. 5.10, 5.11 and 5.13.

## Hypotheses, Data and Unknowns

- Water at rest, incompressible, density $\rho$; air at $p_a$ on the free surface and on the dry side, so only gauge pressures count.
- The gate is vertical, of height $l + h$ and width $b$, hinged without friction at a distance $l$ below its top edge and $h$ above the floor; its weight passes through the hinge and has no moment.
- A stop at the floor, on the dry side, keeps the lower edge from moving out: it can push the gate only towards the water.
- The free surface is at the height $H$ above the top edge of the gate. Data: $l$, $h$, $\rho$, $g$, $b$. Unknown: the height $H$ at which the gate opens.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $H$ | water above the top edge of the gate | m |
| $l$, $h$ | distances from the hinge to the top edge and to the floor | m |
| $b$ | width of the gate | m |

## Coordinates and the Surface Element

Take $z$ vertical, pointing up, with $z = 0$ at the hinge; the gate covers $-h \leq z \leq l$, and the free surface is at $z = H + l$. The depth of a point is $H + l - z$, so by (5.10)

$$ p(z) - p_a = \rho g (H + l - z) $$

The strip between $z$ and $z + dz$ has the area $b\,dz$ and the horizontal force $(p - p_a)\,b\,dz$ towards the dry side; its arm about the hinge is $z$. Strips above the hinge ($z > 0$) turn the gate with the top edge out (opening); strips below it ($z < 0$) turn it with the lower edge out, against the stop.

![[attachments/FM-T5/fs9-fbd.svg]]
*Free-body diagram of the gate (width $b$): the gauge pressure grows from $\rho g H$ at the top edge to $\rho g(H + l + h)$ at the floor; with $z$ measured up from the hinge, the strip $b\,dz$ has depth $H + l - z$ and arm $z$. The part above the hinge turns the gate open; the part below presses it against the stop*

## Moment about the Hinge

Counting the opening sense as positive, the signed arm $z$ takes care of both parts at once:

$$ M = \int_{-h}^{l}\rho g (H + l - z)\,z\,b\,dz = \rho g b\left[(H + l)\frac{z^2}{2} - \frac{z^3}{3}\right]_{-h}^{l} $$

Barrow's rule, with $(-h)^2 = h^2$ and $(-h)^3 = -h^3$:

$$ M = \rho g b\left[(H + l)\frac{l^2 - h^2}{2} - \frac{l^3 + h^3}{3}\right] $$

## Opening Condition

While $M < 0$ the water presses the lower edge against the stop and the gate stays closed. It opens when $M$ reaches zero and becomes positive; $M$ grows with $H$ because $l^2 - h^2 > 0$ ($h < l$). Setting $M = 0$:

$$ (H + l)\frac{l^2 - h^2}{2} = \frac{l^3 + h^3}{3} \quad\Longrightarrow\quad H + l = \frac{2}{3}\,\frac{l^3 + h^3}{l^2 - h^2} $$

With $l^3 + h^3 = (l + h)(l^2 - lh + h^2)$ and $l^2 - h^2 = (l + h)(l - h)$:

$$ H = \frac{2(l^2 - lh + h^2)}{3(l - h)} - l = \frac{2l^2 - 2lh + 2h^2 - 3l^2 + 3lh}{3(l - h)} = \frac{(l + h)(2h - l)}{3(l - h)} $$

The gate opens for any water level above this value.

**Interpretation with the centre of pressure.** $M = 0$ means that the resultant passes through the hinge: the centre of pressure is at the hinge. As $H$ grows, the centre of pressure rises towards the centroid of the gate (Section 4.1 of Topic 5), which is $(l - h)/2$ above the hinge; the gate opens when the centre of pressure crosses the hinge from below.

## Answers and Checks

- $H + l = \dfrac{2}{3}\,\dfrac{l^3 + h^3}{l^2 - h^2}$, that is $H = \dfrac{(l + h)(2h - l)}{3(l - h)}$.
- **When is it positive?** Only for $l/2 < h < l$. If $h \leq l/2$ the formula gives $H \leq 0$: even with the free surface at the top edge the centre of pressure is already above the hinge (for a triangular distribution it sits at a third of the height from the bottom, $(l + h)/3$ above the floor, which is above the hinge when $h < (l + h)/3$, i.e. $h < l/2$), so the gate cannot be kept closed. At $h = l/2$ the centre of pressure of the triangle is exactly at the hinge, $H = 0$.
- **Limiting case** $h \to l$ (hinge at the centre): $H \to \infty$; the centre of pressure is always below the centroid, so a gate hinged at its centre never opens (compare with FS4).
- **Dimensions**: $H$ is m (cubic over quadratic lengths).
- **Check against the official key**: fluid_statics_9.pdf gives $M = \rho g[(H + l)(l^2 - h^2)/2 - (l^3 + h^3)/3]$ and $H + l = \tfrac{2}{3}(l^3 + h^3)/(l^2 - h^2)$, the same results.
