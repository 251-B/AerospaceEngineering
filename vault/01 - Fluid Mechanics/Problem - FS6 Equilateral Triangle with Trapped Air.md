---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - flotacion
  - gas-atrapado
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_6.pdf"
id: "fs6"
pill: "FS6: Floating triangle"
sheets:
  - 6
tags_html:
  - "Floating body"
  - "Trapped air"
  - "Similar triangles"
  - "Erratum"
---

# Problem FS6: Equilateral Triangle with Trapped Air

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: the isothermal state equation of the trapped air, the hydrostatic law between the two free surfaces (Notes.pdf, Eq. 5.10) and Archimedes' principle (Eq. 5.15), with every area computed from similar equilateral triangles.

## Statement

An equilateral triangle of side $L$ and weight $W$ initially contains air at the ambient pressure and temperature, $p_a$ and $T_a$. The triangle has an orifice in its lower side so that, when it is put into the water, the water enters it until the equilibrium position is reached. Obtain the system of equations that determines the equilibrium position, characterized by the heights $H$ and $h$ of the figure, and the pressure of the air inside the triangle. Assume that the sinking process is slow, so that the temperature of the gas stays constant at every moment.

Translated from the Spanish original. The triangle is a long prism (a two-dimensional problem): $W$ and every area are per unit length normal to the paper.

![[attachments/FM-T5/fs6-statement.svg]]
*Statement figure (redrawn from fluid_statics_6.pdf, p. 1): equilateral triangle of side $L$ with an orifice in the lower side; its base is at the depth $H$ below the outer free surface and the inner level is $h$ below it*

Source: fluid_statics_6.pdf (pages 1-2, sheet of 06-09-2008). Notes.pdf, Chapter 5: Eqs. 5.10, 5.15 and 5.18.

## Hypotheses, Data and Unknowns

- Water and air at rest; water incompressible with density $\rho$; outside air at $p_a$.
- The trapped air has a uniform pressure $p$ and keeps the temperature $T_a$ (slow process): $p\,A = \text{const}$ per unit length, from (5.18) at constant mass and temperature.
- Thin walls; the weight of the air is negligible; the triangle floats with its base horizontal and its apex up (as drawn).
- Data: $L$, $W$ (per unit length), $\rho$, $g$, $p_a$. Unknowns: $H$ (depth of the base below the outer free surface), $h$ (depth of the inner level below the outer free surface) and $p$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $L$ | side of the triangle | m |
| $W$ | weight per unit length | N/m |
| $H$, $h$ | heights of the figure | m |
| $p$ | final air pressure | Pa |

## Geometry: Similar Equilateral Triangles

The height of the equilateral triangle is $L\sqrt{3}/2$: in the right triangle formed by the height, half the base $L/2$ and a side $L$ (hypotenuse), Pythagoras gives $\sqrt{L^2 - L^2/4} = L\sqrt{3}/2$.

Every horizontal cut of the triangle is the base of a smaller **equilateral** triangle with the same apex (same angles). The half-angle at the apex is $30^\circ$, so in the right triangle with the vertical height $a$ (adjacent to $30^\circ$) and half the base (opposite), the half base is $a\tan 30^\circ = a/\sqrt{3}$. The area of a triangle of height $a$ is then

$$ A(a) = \frac{1}{2}\cdot\frac{2a}{\sqrt{3}}\cdot a = \frac{a^2}{\sqrt{3}} $$

Check: $a = L\sqrt{3}/2$ gives $A = (3L^2/4)/\sqrt{3} = \sqrt{3}L^2/4$, the area $A_0$ of the whole triangle.

The base is at depth $H$ and the inner level at depth $h$ below the outer free surface, so the inner level is $H - h$ above the base, and the air triangle (from the inner level to the apex) has the height

$$ a = \frac{L\sqrt{3}}{2} - (H - h) = \frac{L\sqrt{3}}{2} + h - H $$

The part of the triangle above the outer free surface has the height $L\sqrt{3}/2 - H$.

![[attachments/FM-T5/fs6-geometry.svg]]
*Every horizontal section of the equilateral triangle is the base of a smaller equilateral triangle with the same apex. The half-angle at the apex is $30^\circ$, so a triangle of height $a$ has the half base $a\tan 30^\circ = a/\sqrt{3}$ and the area $a^2/\sqrt{3}$. Orange: the air triangle, height $a = L\sqrt{3}/2 + h - H$; green: the displaced area $A_d$ between the outer free surface and the inner level; $A_T$: the part above the outer free surface*

## Equation 1: Isothermal Air

Initially the air fills the whole triangle, $A_0 = \sqrt{3}L^2/4$, at $p_a$; at equilibrium it fills the air triangle $A = a^2/\sqrt{3}$ at $p$. With constant mass and temperature, $p\,A = p_a A_0$:

$$ \frac{p}{p_a} = \frac{A_0}{A} = \frac{\sqrt{3}L^2/4}{a^2/\sqrt{3}} = \frac{3L^2}{4a^2} = \frac{3}{4}\,\frac{1}{\left(\frac{\sqrt{3}}{2} + \frac{h}{L} - \frac{H}{L}\right)^2} $$

## Equation 2: the Hydrostatic Law

The water inside is connected with the outside through the orifice. From the outer free surface ($p = p_a$) down to the depth $h$ of the inner level, (5.10) adds $\rho g h$, and at the interface the water pressure equals the air pressure:

$$ p = p_a + \rho g h \quad\Longrightarrow\quad \frac{p}{p_a} = 1 + \frac{\rho g L}{p_a}\,\frac{h}{L} $$

## Equation 3: Archimedes' Principle

![[attachments/FM-T5/fs6-fbd.svg]]
*Free-body diagram of the system triangle plus trapped air, per unit length: the weight $W$ (air weight neglected) and the buoyancy $\rho g A_d$, where $A_d$ is the part of the air region below the outer free surface (Archimedes, Eq. 5.15)*

For the system triangle plus trapped air, the volume (area, per unit length) that displaces water is the air region below the outer free surface: the air triangle minus the triangle above the outer free surface,

$$ A_d = \frac{a^2}{\sqrt{3}} - \frac{1}{\sqrt{3}}\left(\frac{L\sqrt{3}}{2} - H\right)^2 $$

and the vertical equilibrium $W = \rho g A_d$ gives, dividing by $\rho g L^2$:

$$ \frac{W}{\rho g L^2} = \frac{1}{\sqrt{3}}\left[\left(\frac{\sqrt{3}}{2} + \frac{h}{L} - \frac{H}{L}\right)^2 - \left(\frac{\sqrt{3}}{2} - \frac{H}{L}\right)^2\right] $$

The same equation follows from the free-body diagram of the shell alone: the air pushes its inner walls with $p - p_a$ over the part above the inner level, the water pushes its outer walls below the outer level, and adding the vertical projections with the rule (5.14) gives $\rho g A_d$.

## Answers and Checks

The equilibrium is the solution of the three equations in the three unknowns $H/L$, $h/L$, $p/p_a$, with the two dimensionless parameters $W/(\rho g L^2)$ and $\rho g L/p_a$:

$$ \frac{p}{p_a} = \frac{3}{4\left(\frac{\sqrt{3}}{2} + \frac{h}{L} - \frac{H}{L}\right)^2}, \qquad \frac{p}{p_a} = 1 + \frac{\rho g L}{p_a}\,\frac{h}{L}, \qquad \frac{W}{\rho g L^2} = \frac{1}{\sqrt{3}}\left[\left(\frac{\sqrt{3}}{2} + \frac{h}{L} - \frac{H}{L}\right)^2 - \left(\frac{\sqrt{3}}{2} - \frac{H}{L}\right)^2\right] $$

- **Numerical example** (solved with SymPy in `tools/fluids_fs/verify_fluid_statics.py`): for $\rho g L/p_a = 0.1$ and $W/(\rho g L^2) = 0.2$, $H/L = 0.244$, $h/L = 0.234$, $p/p_a = 1.023$.
- **Limiting case** $h = H = 0$ (triangle resting on the surface, no water inside): the first equation gives $p/p_a = (3/4)/(3/4) = 1$, as it must.
- **Expanding the bracket** of the third equation: $W/(\rho g L^2) = (h/L)\,[\sqrt{3} - 2H/L + h/L]/\sqrt{3}$, which vanishes for $h = 0$: with no compression there is no displaced air and no buoyancy.
- **Dimensions**: $W$ is N/m and $\rho g L^2$ is (kg m$^{-3}$)(m s$^{-2}$)(m$^2$) = N/m; $\rho g L/p_a$ is Pa/Pa.

> [!warning] Erratum in the official solution
> fluid_statics_6.pdf, page 2, writes $p/p_a = \tfrac{1}{4}(\sqrt{3}/2 + h/L - H/L)^{-2}$. The quotient of the areas is $(\sqrt{3}L^2/4)\cdot\sqrt{3}/a^2 = 3L^2/(4a^2)$, so the coefficient is $3/4$: with $h = H = 0$ the official formula gives $p = p_a/3$ instead of $p = p_a$. Equations 2 and 3 of the official key agree with the ones above.
