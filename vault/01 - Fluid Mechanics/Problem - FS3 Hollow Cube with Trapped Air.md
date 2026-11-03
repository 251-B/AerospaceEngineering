---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - flotacion
  - gas-atrapado
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_3.pdf"
id: "fs3"
pill: "FS3: Hollow cube"
sheets:
  - 3
sim: buoyancy-cube
tags_html:
  - "Floating body"
  - "Trapped air"
  - "Isothermal gas"
  - "Simulator"
---

# Problem FS3: Hollow Cube with Trapped Air

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: equilibrium of the shell of the cube, the hydrostatic law between the two free surfaces (Notes.pdf, Eq. 5.10) and the isothermal state equation of the trapped air; checked with Archimedes' principle.

## Statement

A hollow cube of side $L$ and weight $W < \rho g L^3$ is initially full of air at the ambient pressure $p_a$ and temperature $T_a$. At a certain instant, the cube is placed on the surface of a liquid of density $\rho$. The liquid enters the cube through an orifice in its base until an equilibrium position is reached, characterized by the lengths $H_1$ and $H_2$ of the attached figure. Assuming that the evolution of the air inside the cube is isothermal, determine the values of $H_1/L$ and $H_2/L$, as well as the final pressure inside the cube, $p_c$.

Translated from the Spanish original.

![[attachments/FM-T5/fs3-statement.svg]]
*Statement figure (redrawn from fluid_statics_3.pdf, p. 1): hollow cube of side $L$ with an orifice in its base; the inner interface is $H_1$ below the outer free surface and $H_2$ above the base; air at $p_c$ inside, $p_a$ outside*

Source: fluid_statics_3.pdf (page 1, sheet of 27-01-03). Notes.pdf, Chapter 5: Eqs. 5.10, 5.15 and 5.18.

## Hypotheses, Data and Unknowns

- Liquid and air at rest; the liquid is incompressible; the outside air is at the uniform pressure $p_a$.
- The trapped air has a uniform pressure $p_c$ (its weight and the change of its pressure over a height $L$ are negligible, Section 7 of Topic 5) and keeps the temperature $T_a$: isothermal process, $p\,V = \text{const}$ from the state equation (5.18) at constant $T$ and constant mass.
- Thin walls: the volume of the walls is neglected; $W$ is the weight of the cube alone (the air weight is negligible).
- The cube floats upright with its top face above the outer free surface (checked at the end).
- Data: $L$, $W$, $\rho$, $g$, $p_a$. Unknowns: $H_1$ (depth of the inner interface below the outer free surface), $H_2$ (height of the inner liquid layer above the base) and $p_c$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $L$ | side of the cube | m |
| $W$ | weight of the cube | N |
| $H_1$, $H_2$ | lengths of the figure | m |
| $p_a$, $p_c$ | outside pressure, final air pressure inside | Pa |

## Coordinates and the Free-Body Diagram

Take the vertical axis pointing up. The system for the force balance is the **shell of the cube** alone (not the air, not the liquid inside). Its side walls are vertical, so the pressure on them is horizontal and adds up to zero by symmetry; its base has an orifice and is wetted by the same liquid on both faces at the same depth, so its net pressure force is zero (thin wall). Only the top face carries a net vertical pressure force: $p_a L^2$ downward from the outside air and $p_c L^2$ upward from the trapped air.

![[attachments/FM-T5/fs3-fbd.svg]]
*(a) Vertical forces on the shell of the cube (thin walls): $p_a L^2$ down on the top face from outside, $p_c L^2$ up on it from the trapped air, weight $W$ down; the side walls carry only horizontal forces, which cancel. (b) Walking from the outer free surface down the depth $H_1$ to the inner interface gives $p_c = p_a + \rho g H_1$*

## Equilibrium of the Shell

Vertical equilibrium of the shell (upward positive):

$$ p_c L^2 - p_a L^2 - W = 0 \quad\Longrightarrow\quad p_c = p_a + \frac{W}{L^2} $$

## The Hydrostatic Law between the Two Free Surfaces

The liquid inside the cube is connected with the outside liquid through the orifice, so (5.10) holds through both. Walking from a point of the outer free surface, where $p = p_a$, down a depth $H_1$ to the level of the inner interface (any path inside the connected liquid gives the same result), the pressure grows by $\rho g H_1$; at the interface it equals the air pressure (Section 1 of Topic 5, no surface tension):

$$ p_c = p_a + \rho g H_1 $$

Equating the two expressions of $p_c$:

$$ \rho g H_1 = \frac{W}{L^2} \quad\Longrightarrow\quad \frac{H_1}{L} = \frac{W}{\rho g L^3} $$

The hypothesis $W < \rho g L^3$ gives $H_1 < L$.

## The Trapped Air: Isothermal Compression

Initially the air fills the whole cube, $V_0 = L^3$, at $p_a$. At equilibrium it fills the part of the cube above the inner interface, a prism of base $L^2$ and height $L - H_2$, at $p_c$. With the same mass and the same temperature, $p\,V$ is constant:

$$ p_a L^3 = p_c L^2 (L - H_2) \quad\Longrightarrow\quad \frac{L - H_2}{L} = \frac{p_a}{p_c} \quad\Longrightarrow\quad \frac{H_2}{L} = 1 - \frac{p_a}{p_c} = \frac{p_c - p_a}{p_c} $$

and with $p_c - p_a = W/L^2$ and $p_c = p_a + W/L^2$, multiplying numerator and denominator by $L^2$:

$$ \frac{H_2}{L} = \frac{W/L^2}{p_a + W/L^2} = \frac{W}{p_a L^2 + W} $$

## Simulator: the Floating Cube

> [!example] Interactive simulator
> Move the weight ratio and the pressure ratio and watch both levels and the forces on the top face of the shell.

## Answers and Checks

- $H_1/L = W/(\rho g L^3)$, $H_2/L = W/(p_a L^2 + W)$, $p_c = p_a + W/L^2$.
- **Archimedes check.** For the system cube plus trapped air, the displaced liquid is the air below the outer free surface, a prism of base $L^2$ and height $H_1$ (from the outer level down to the inner interface). Its weight $\rho g L^2 H_1 = W$ balances the cube, which is the same equation as above.
- **Limiting cases.** $W \to 0$: $H_1 \to 0$, $H_2 \to 0$, $p_c \to p_a$ (a weightless box lets no liquid in). $p_a \to \infty$ (incompressible air): $H_2 \to 0$, the air keeps its volume.
- **Consistency.** The top face is above the outer free surface when $H_1 + H_2 < L$, that is $W/(\rho g L^3) + W/(p_a L^2 + W) < 1$. For water and $L = 1$ m, $p_a/(\rho g L) \approx 10.3$, so $H_2 \ll H_1$: the air is barely compressed and the cube floats almost as a closed box.
- **Dimensions.** $W/(\rho g L^3)$: N / (kg m$^{-3}$ m s$^{-2}$ m$^3$) = N/N, dimensionless; $W/(p_a L^2)$: N/(Pa m$^2$) = N/N; $W/L^2$ in Pa.
- **Check against the official key.** fluid_statics_3.pdf gives $H_1 = W/(\rho g L^2)$, $p_c = p_a + W/L^2$ and $H_2/L = 1 - p_a/p_c = W/(p_a L^2 + W)$, the same results.
