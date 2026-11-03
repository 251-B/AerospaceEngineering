---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - compuerta
  - momentos
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_5.pdf"
id: "fs5"
pill: "FS5: Gate between two liquids"
sheets:
  - 5
tags_html:
  - "Plane surface"
  - "Two liquids"
  - "Moment about a hinge"
  - "Critical level"
---

# Problem FS5: Gate between Two Liquids

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: the moment of each pressure distribution about the hinge, by direct integration (Notes.pdf, Eq. 5.11), and the condition that the stop can only push.

## Statement

The gate of the attached figure separates two liquids of densities $\rho_1$ and $\rho_2 > \rho_1$. The height of the liquid on the two sides of the gate is $H_1$ and $H_2 < H_1$. The gate is hinged at its lower end and rests on a stop at its upper end, as shown in the attached figure, so that the configuration is in equilibrium as long as $H_2$ stays below a certain critical value, $H_c$, to be determined as a function of $H_1$, $\rho_1$ and $\rho_2$.

Translated from the Spanish original. The sheet gives no solution for this problem.

![[attachments/FM-T5/fs5-statement.svg]]
*Statement figure (redrawn from fluid_statics_5.pdf, p. 1): gate of height $H_1$ between the liquids $\rho_1$ (left, height $H_1$) and $\rho_2 > \rho_1$ (right, height $H_2 < H_1$), hinged at the bottom and resting on a stop at the top*

Source: fluid_statics_5.pdf (page 1, sheet of 11-2-00). Notes.pdf, Chapter 5: Eqs. 5.10 and 5.11.

## Hypotheses, Data and Unknowns

- Both liquids at rest, incompressible, immiscible and separated by the gate; air at $p_a$ above both, so only gauge pressures count.
- The gate is a vertical rigid plate of height $H_1$ and width $b$ (normal to the paper), hinged at the bottom (point $O$) without friction; its weight passes through the hinge when it is vertical and has no moment about $O$.
- The stop at the top is on the side of liquid 2: it can only push the gate towards liquid 1, never pull.
- Data: $\rho_1$, $\rho_2$, $H_1$, $H_2$, $g$, $b$. Unknowns: the critical level $H_c$ (and, as a by-product, the force on the stop).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $\rho_1$, $\rho_2$ | densities, $\rho_2 > \rho_1$ | kg/m$^3$ |
| $H_1$, $H_2$ | liquid heights | m |
| $b$ | width of the gate | m |

## Coordinates and the Pressure on Each Face

Take $z$ vertical, pointing up from the hinge, so the gate covers $0 \leq z \leq H_1$. By (5.10), measured from each free surface:

$$ p_1(z) - p_a = \rho_1 g (H_1 - z), \quad 0 \leq z \leq H_1; \qquad p_2(z) - p_a = \rho_2 g (H_2 - z), \quad 0 \leq z \leq H_2 $$

The strip between $z$ and $z + dz$ has the area $b\,dz$, its force is horizontal, and its arm about the hinge is $z$. Liquid 1 pushes the gate towards liquid 2 (normal towards liquid 1 is $-\vec{e}_x$), liquid 2 pushes it back.

![[attachments/FM-T5/fs5-fbd.svg]]
*Free-body diagram of the gate (unit width): the triangular gauge pressures $\rho_1 g(H_1 - z)$ and $\rho_2 g(H_2 - z)$, their resultants $F_1$ and $F_2$ at $H_1/3$ and $H_2/3$ above the hinge $O$, and the stop reaction $R$ at the top*

## Moments about the Hinge

Moment of liquid 1 (turning the gate towards liquid 2):

$$ M_1 = \int_0^{H_1}\rho_1 g (H_1 - z)\,z\,b\,dz = \rho_1 g b\left[\frac{H_1 z^2}{2} - \frac{z^3}{3}\right]_0^{H_1} = \rho_1 g b\left(\frac{H_1^3}{2} - \frac{H_1^3}{3}\right) = \frac{\rho_1 g b H_1^3}{6} $$

Moment of liquid 2 (turning it back), with the same integral and $H_2$ in place of $H_1$:

$$ M_2 = \int_0^{H_2}\rho_2 g (H_2 - z)\,z\,b\,dz = \frac{\rho_2 g b H_2^3}{6} $$

Check with the resultants: each triangular distribution has the resultant $\rho_i g b H_i^2/2$ applied at its centroid, $H_i/3$ above the bottom, and $(\rho_i g b H_i^2/2)(H_i/3) = \rho_i g b H_i^3/6$.

## Equilibrium and the Critical Level

Moment balance about the hinge, with the stop reaction $R$ (pushing towards liquid 1) acting at the top, arm $H_1$:

$$ M_1 - M_2 - R\,H_1 = 0 \quad\Longrightarrow\quad R = \frac{g b\,(\rho_1 H_1^3 - \rho_2 H_2^3)}{6 H_1} $$

The stop can only push, $R \geq 0$, so the configuration is in equilibrium while $\rho_1 H_1^3 \geq \rho_2 H_2^3$. The critical level is the one with $R = 0$:

$$ \rho_1 H_1^3 = \rho_2 H_c^3 \quad\Longrightarrow\quad H_c = H_1\left(\frac{\rho_1}{\rho_2}\right)^{1/3} $$

For $H_2 > H_c$ the moment of liquid 2 wins, the gate leaves the stop and turns towards liquid 1.

## Answers and Checks

- $H_c = H_1(\rho_1/\rho_2)^{1/3}$; equilibrium for $H_2 < H_c$; stop force $R = g b(\rho_1 H_1^3 - \rho_2 H_2^3)/(6H_1)$.
- **Consistency with the statement**: $\rho_2 > \rho_1$ gives $H_c < H_1$, so the critical level lies within the gate, as it must for $H_2 < H_1$.
- **Limiting case** $\rho_2 = \rho_1$: $H_c = H_1$, two equal columns of the same liquid balance exactly.
- **Not the force balance**: the horizontal forces are equal when $\rho_1 H_1^2 = \rho_2 H_2^2$, which gives a different level, $H_1(\rho_1/\rho_2)^{1/2}$; the gate turns about the hinge, so the moments decide (the difference is taken by the hinge reaction).
- **Dimensions**: $H_c$ is $H_1$ times a dimensionless ratio, m; $R$ is (m s$^{-2}$)(m)(kg m$^{-3}$ m$^3$)/m = N.
- **Check against the official key**: the sheet has no handwritten solution for this problem; the result was checked with SymPy (`tools/fluids_fs/verify_fluid_statics.py`).
