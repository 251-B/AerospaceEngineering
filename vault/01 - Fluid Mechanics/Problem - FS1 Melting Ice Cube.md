---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - flotacion
  - arquimedes
dificultad: baja
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_1.pdf"
id: "fs1"
pill: "FS1: Melting ice cube"
sheets:
  - 1
tags_html:
  - "Archimedes"
  - "Floating body"
  - "Mass conservation"
---

# Problem FS1: Melting Ice Cube

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: Archimedes' principle for the floating cube (Notes.pdf, Eq. 5.15), then conservation of mass when it melts.

## Statement

An ice cube of density $\rho_h$ is partially submerged in a container holding a fluid of density $\rho_f > \rho_h$. The total volume of the ice cube is $V_h$, while the submerged part of the cube occupies a volume $V_s$ to be determined. Calculate the volume of water displaced once the cube has melted, turning into water of density $\rho_a$, as a function of $\rho_f$, $\rho_h$, $\rho_a$ and $V_h$, knowing that $\rho_h < \rho_a < \rho_f$. Particularize for the case $\rho_f = \rho_a$.

Translated from the Spanish original; the figure of the sheet labels the cube density $\rho_b$, the same quantity as $\rho_h$.

![[attachments/FM-T5/fs1-statement.svg]]
*Statement figure (redrawn from fluid_statics_1.pdf, p. 1): ice cube of volume $V_h$ and density $\rho_h$ floating in a liquid of density $\rho_f > \rho_h$, submerged volume $V_s$*

Source: fluid_statics_1.pdf (page 1, sheet of 11-2-00). Notes.pdf, Chapter 5: Archimedes' principle, Eq. 5.15.

## Hypotheses, Data and Unknowns

- The fluid and the melt water are at rest and incompressible; the air above them is at the uniform pressure $p_a$.
- The cube floats in equilibrium with part of its volume above the free surface (this requires $\rho_h < \rho_f$, given).
- Mass is conserved when the ice melts; the melt water and the fluid do not change volume when they meet (the melt water either floats as a layer, since $\rho_a < \rho_f$, or mixes with additive volumes).
- Data: $\rho_h$, $\rho_f$, $\rho_a$, $V_h$, $g$. Unknowns: the submerged volume $V_s$ and the volume $V_d$ that the liquid gains when the cube melts, that is the change of the volume of liquid below the free surface.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $\rho_h$, $\rho_f$, $\rho_a$ | densities of ice, fluid and melt water | kg/m$^3$ |
| $V_h$ | volume of the cube | m$^3$ |
| $V_s$ | submerged volume of the cube | m$^3$ |
| $V_a$ | volume of the melt water | m$^3$ |

## The Floating Cube: Archimedes' Principle

The forces on the cube are its weight and the pressure of the fluid and of the air on its surface. The air pressure $p_a$ acts over the whole closed surface of the cube and adds up to zero ($\oint p_a\vec{n}\,d\sigma = 0$). The part below the free surface feels the gauge pressure of the fluid, and by Archimedes' principle (Eq. 5.15) applied to the submerged part, closed by the plane of the free surface where the gauge pressure is zero, its resultant is the weight of the displaced fluid, $\rho_f g V_s$, upward.

![[attachments/FM-T5/fs1-fbd.svg]]
*(a) The floating cube: weight $\rho_h g V_h$ at its centre of gravity, buoyancy $\rho_f g V_s$ at the centroid of the submerged part. (b) The cube displaced $V_s$; once melted, the same mass occupies $V_a = \rho_h V_h/\rho_a$; the difference $V_d = V_a - V_s$ is the volume the liquid gains*

Vertical equilibrium of the cube (upward positive):

$$ \rho_f g V_s - \rho_h g V_h = 0 \quad\Longrightarrow\quad V_s = \frac{\rho_h}{\rho_f}\,V_h $$

Since $\rho_h < \rho_f$, $V_s < V_h$: part of the cube emerges, as assumed.

## Melting: Conservation of Mass

When the ice melts, its mass $\rho_h V_h$ is conserved and becomes water of density $\rho_a$:

$$ \rho_a V_a = \rho_h V_h \quad\Longrightarrow\quad V_a = \frac{\rho_h}{\rho_a}\,V_h $$

Before melting, the cube occupied the volume $V_s$ below the free surface; after melting, the melt water occupies $V_a$ in the liquid. The volume of liquid below the free surface therefore grows by

$$ V_d = V_a - V_s = \rho_h V_h\left(\frac{1}{\rho_a} - \frac{1}{\rho_f}\right) = \frac{\rho_h}{\rho_a}\,V_h\left(1 - \frac{\rho_a}{\rho_f}\right) $$

In a container of horizontal section $S$, the free surface rises by $V_d/S$.

## Answers and Checks

- Submerged volume: $V_s = (\rho_h/\rho_f)\,V_h$.
- Extra volume after melting: $V_d = (\rho_h/\rho_a)\,V_h\,(1 - \rho_a/\rho_f)$. With $\rho_a < \rho_f$ it is positive: the level rises, because the melt water is lighter than the fluid it displaced.
- Particular case $\rho_f = \rho_a$ (ice floating in its own water): $V_d = 0$. The melt water fills exactly the hole the cube had made, and the level does not change.
- Limiting case $\rho_h \to \rho_f$: $V_s \to V_h$, the cube is just fully submerged.
- Dimensions: $V_d$ is a ratio of densities times $V_h$, so m$^3$; both brackets are dimensionless.
- Check against the official key: fluid_statics_1.pdf gives $V_s = (\rho_h/\rho_f)V_h$ and $V_d = (\rho_h/\rho_a)V_h(1 - \rho_a/\rho_f)$, the same results.
