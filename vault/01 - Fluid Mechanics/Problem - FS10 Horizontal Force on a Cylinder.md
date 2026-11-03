---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - superficie-curva
  - proyecciones
dificultad: baja
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_10.pdf"
id: "fs10"
pill: "FS10: Cylinder"
sheets:
  - 10
sim: curved-surface
tags_html:
  - "Curved surface"
  - "Polar coordinates"
  - "Projection rule"
  - "Simulator"
---

# Problem FS10: Horizontal Force on a Cylinder

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: direct integration of the horizontal component of $-(p - p_a)\vec{n}\,dS$ in polar coordinates (Notes.pdf, Eq. 5.11), checked with the projection rule (Eq. 5.14).

## Statement

Calculate the net horizontal force on the cylinder of length 5 metres shown in the attached figure.

Translated from the Spanish original.

![[attachments/FM-T5/fs10-statement.svg]]
*Statement figure (redrawn from fluid_statics_10.pdf, p. 1): cylinder of diameter $D = 1$ m and length 5 m on the floor; water 1 m deep on the left, up to the top of the cylinder, and 0.5 m deep on the right, up to its centre*

Source: fluid_statics_10.pdf (page 1, sheet of 12-9-01). Notes.pdf, Chapter 5: Eqs. 5.10, 5.11 and 5.14.

## Hypotheses, Data and Unknowns

- Water at rest, incompressible, $\rho = 1000$ kg/m$^3$, $g = 9.81$ m/s$^2$; air at $p_a$ above both free surfaces and on the dry parts of the cylinder, so only gauge pressures count.
- The cylinder, of diameter $D = 2R = 1$ m and length $L = 5$ m, lies on the floor with its axis horizontal and normal to the paper; end effects are neglected (the end faces are vertical, and their horizontal forces act along the axis, normal to the paper, so they do not enter the net force in the plane of the figure).
- Water on the left up to $2R = 1$ m (the top of the cylinder); on the right up to $R = 0.5$ m (its centre).
- Unknown: the net horizontal force $F_x$ in the plane of the figure.

| Symbol | Value | Meaning |
| :--- | :--- | :--- |
| $R$ | 0.5 m | radius |
| $L$ | 5 m | length |
| $2R$, $R$ | 1 m, 0.5 m | water depth on the left and on the right |

## Coordinates, Element and Normal

Take $y$ vertical and up from the floor, $x$ horizontal to the right, and measure the angle $\theta$ from the upward vertical through the centre $C$ (at $y = R$). In the right triangle with the radius $R$ as hypotenuse, the vertical leg $R\cos\theta$ is adjacent to $\theta$ and the horizontal leg $R\sin\theta$ opposite, so a point of the left half is at

$$ x = -R\sin\theta, \qquad y = R + R\cos\theta, \qquad 0 \leq \theta \leq \pi $$

and a point of the right half at $x = +R\sin\theta$, same $y$. The element of the surface is the arc $R\,d\theta$ times the length $L$: $dS = LR\,d\theta$. The unit normal towards the water is the outward radial vector, with the horizontal component $n_x = -\sin\theta$ on the left half and $n_x = +\sin\theta$ on the right half.

![[attachments/FM-T5/fs10-geometry.svg]]
*Element of the cylinder at the angle $\theta$ measured from the upward vertical through the centre $C$. In the right triangle with hypotenuse $R$, the horizontal leg $R\sin\theta$ is opposite to $\theta$ and the vertical leg $R\cos\theta$ adjacent, so the element is at $y = R + R\cos\theta$ above the floor. The unit normal towards the water on the left half is $\vec{n} = -\sin\theta\,\vec{e}_x + \cos\theta\,\vec{e}_y$ and the area is $dS = LR\,d\theta$*

## Left Half

The water on the left reaches $y = 2R$, so the depth of a point is $2R - y = R - R\cos\theta$ and, by (5.10), $p - p_a = \rho g R(1 - \cos\theta)$, over the whole left half ($0 \leq \theta \leq \pi$). The horizontal component of $-(p - p_a)\vec{n}\,dS$:

$$ F_1 = -\int_0^{\pi}\rho g R(1 - \cos\theta)(-\sin\theta)\,LR\,d\theta = \rho g R^2 L\int_0^{\pi}\left(\sin\theta - \sin\theta\cos\theta\right)d\theta $$

With $\int\sin\theta\,d\theta = -\cos\theta$ and $\int\sin\theta\cos\theta\,d\theta = \sin^2\theta/2$ (substitution $u = \sin\theta$, $du = \cos\theta\,d\theta$), by Barrow's rule:

$$ F_1 = \rho g R^2 L\left[-\cos\theta - \frac{\sin^2\theta}{2}\right]_0^{\pi} = \rho g R^2 L\left[(1 - 0) - (-1 - 0)\right] = 2\rho g R^2 L $$

pointing to the right.

## Right Half

The water on the right reaches $y = R$, so only the lower right quarter is wetted, $\pi/2 \leq \theta \leq \pi$, with the depth $R - y = -R\cos\theta$ (positive there, since $\cos\theta \leq 0$):

$$ F_2 = -\int_{\pi/2}^{\pi}\rho g(-R\cos\theta)(\sin\theta)\,LR\,d\theta = \rho g R^2 L\left[\frac{\sin^2\theta}{2}\right]_{\pi/2}^{\pi} = \rho g R^2 L\left(0 - \frac{1}{2}\right) = -\frac{\rho g R^2 L}{2} $$

pointing to the left.

## Check with the Projection Rule

By (5.14), the horizontal force on each side is the force on the vertical projection of the wetted surface. On the left, the projection is a rectangle of height $2R$ and length $L$ with its centroid at the depth $R$: $\rho g R\cdot 2RL = 2\rho g R^2 L$. On the right, it is a rectangle of height $R$ with its centroid at the depth $R/2$: $\rho g (R/2)\cdot RL = \rho g R^2 L/2$. Both agree with the integrals.

## Simulator: the Curved Surface

> [!example] Interactive simulator
> Change the radius and the two water levels, move the element around the arc, and switch between the integration view and the projection view, where the vertical force is split into a circular sector and a right triangle.

## Answers and Checks

$$ F_x = F_1 + F_2 = 2\rho g R^2 L - \frac{\rho g R^2 L}{2} = \frac{3}{2}\rho g R^2 L = \frac{3}{2}(1000)(9.81)(0.5)^2(5) = 18\,394\ \text{N} \approx 18.4\ \text{kN} $$

pointing to the right, from the deeper side to the shallower one.

- **Limiting case** equal levels on both sides: the two projections are equal and $F_x = 0$.
- **Dimensions**: $\rho g R^2 L$ is (kg m$^{-3}$)(m s$^{-2}$)(m$^3$) = N.
- **Beyond the statement**: the vertical force is upward and equals the weight of the water displaced by each wetted part (a half disc on the left, a quarter disc on the right); it is shown in the simulator but not asked for.
- **Check against the official key**: fluid_statics_10.pdf gives $F_1 = 2\rho g R^2 L$ and boxes $F_2 = -\rho g L R^2/2$ (the minus sign is the leftward sense, as above), then writes $F_T = F_1 - F_2 = \tfrac{3}{2}\rho g L R^2$ with $F_2$ taken as a magnitude; the net force is the same.
