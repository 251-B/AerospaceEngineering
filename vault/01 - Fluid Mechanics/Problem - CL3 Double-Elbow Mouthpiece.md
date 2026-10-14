---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - momento-angular
  - tobera
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL3.pdf"
---

# Problem CL3: Double-Elbow Mouthpiece: Exit Velocity, Force and Moment

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].

## Statement

The double-elbow mouth piece of exit cross section $A_o$ shown in the figure of CL3.pdf is to be installed at the end of a circular pipe of cross section $A_p$ to redirect the outflow of water into the open atmosphere. Once the mouth piece is installed, the uniform values $U_p$ and $p_p$ are measured for the flow velocity and the pressure at the end of the pipe (i.e., just at the entrance of the mouth piece). Find the value of the uniform velocity at the exit section, $U_o$, as well as the force exerted on the mouth piece and its corresponding moment with respect to the entrance section. (Handwritten addition: neglect the effect of gravity.)

Source: CL3.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eqs. 3.37-3.38, force and moment on a body Eqs. 3.32-3.33.

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Steady flow of an incompressible liquid (water, constant $\rho$), uniform velocity and pressure over the entrance section (area $A_p$) and over the exit section (area $A_o$); no gravity (handwritten addition to the statement).
- The water discharges into the atmosphere, so the pressure over the exit section is the ambient pressure $p_a$. Viscous stresses over the entrance and exit sections are negligible (uniform velocity, no gradients).
- The wall of the mouth piece is thin and its outer face is in contact with the atmosphere at $p_a$. The 'force exerted on the mouth piece' is the net force of the water inside plus the atmosphere outside, which is how the official solution treats it (it adds the term in $p_a$ explicitly). If the atmosphere were ignored, the force would change by $p_a\,(A_p - A_o)\,\mathbf{e}_x$.
- Geometry from the figure: the exit axis is displaced a vertical distance $H$ below the axis of the entrance, and both the entrance flow and the exit flow are along $+\mathbf{e}_x$ (the mouth piece is S-shaped).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A_p$, $A_o$ | entrance and exit areas | m$^2$ |
| $U_p$, $p_p$ | uniform velocity and pressure at the entrance | m/s, Pa |
| $U_o$, $p_a$ | exit velocity (unknown) and ambient pressure | m/s, Pa |
| $H$ | vertical offset between the entrance and exit axes | m |
| $\mathbf{F}_{MP}$, $\mathbf{M}_{MP}$ | force and moment on the mouth piece (unknowns) | N, N$\cdot$m |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame fixed to the pipe, Cartesian basis $(\mathbf{e}_x, \mathbf{e}_y, \mathbf{e}_z)$: $\mathbf{e}_x$ along the pipe axis in the flow direction, $\mathbf{e}_y$ vertical upwards and $\mathbf{e}_z = \mathbf{e}_x \wedge \mathbf{e}_y$ out of the plane of the figure. The origin $O$ is the centre (centroid) of the entrance section; moments are taken about $O$.
- The centre of the exit section is at the position $\mathbf{x}_o = X\,\mathbf{e}_x - H\,\mathbf{e}_y$ relative to $O$; $X$ is the horizontal offset, which will drop out. The position of a point of a circular section relative to its centre is denoted $\boldsymbol{\eta}$, with $\int\boldsymbol{\eta}\,d\sigma = 0$.
- Fixed control volume: the water inside the mouth piece, with boundary $\Sigma_p$ (entrance, $\mathbf{n} = -\mathbf{e}_x$), $\Sigma_o$ (exit, $\mathbf{n} = +\mathbf{e}_x$) and $\Sigma_w$ (inner wall, $\mathbf{n}$ out of the fluid). Since $\mathbf{v}_c = 0$, Eqs. 3.11, 3.36 and 3.38 apply with $\mathbf{v}_c = 0$.
- Since $\int_{\Sigma_c}p_a\,\mathbf{n}\,d\sigma = 0$ on the closed surface, $p$ is replaced by $p - p_a$ in the balances. The force of the water and the atmosphere on the (thin) wall is then $\mathbf{F}_{MP} = \int_{\Sigma_w}\left[(p - p_a)\,\mathbf{n} - \bar{\bar{\tau}}'\cdot\mathbf{n}\right]d\sigma$ and the force of the wall on the water is $-\mathbf{F}_{MP}$.

## Phase 3: Step-by-Step Derivation

### 3.1 Exit velocity from mass conservation

Why this tool: the velocities at both sections are uniform and the flow is steady, so the continuity balance (Notes Eq. 3.11) relates them directly. On $\Sigma_w$, $\mathbf{v}\cdot\mathbf{n} = 0$:

$$ -\rho\,U_p A_p + \rho\,U_o A_o = 0 \;\Longrightarrow\; \boxed{\,U_o = \frac{A_p}{A_o}\,U_p\,}. $$

### 3.2 Force on the mouth piece: linear momentum

Why this tool: the force on the wall is an unknown surface integral of the (non-uniform) wall pressure; the momentum balance (Notes Eq. 3.36) replaces it by quantities known at the two sections. Left-hand side: the momentum flux is only through $\Sigma_p$ and $\Sigma_o$, and both velocities are along $\mathbf{e}_x$:

$$ \int_{\Sigma_c}\rho\,\mathbf{v}\,(\mathbf{v}\cdot\mathbf{n})\,d\sigma = \left(-\rho U_p^2 A_p + \rho U_o^2 A_o\right)\mathbf{e}_x = \rho U_p A_p\,(U_o - U_p)\,\mathbf{e}_x, $$

where $\rho U_o^2 A_o = (\rho U_o A_o)\,U_o = \rho U_p A_p\,U_o$ by 3.1. Right-hand side: on $\Sigma_p$ the force is $-(p_p - p_a)(-\mathbf{e}_x)A_p = +(p_p - p_a)A_p\,\mathbf{e}_x$; on $\Sigma_o$ it vanishes because $p - p_a = 0$; viscous stresses are negligible on both sections; on $\Sigma_w$ it is $-\mathbf{F}_{MP}$. Hence

$$ \rho U_p A_p\,(U_o - U_p)\,\mathbf{e}_x = (p_p - p_a)\,A_p\,\mathbf{e}_x - \mathbf{F}_{MP} \;\Longrightarrow\; \boxed{\,\mathbf{F}_{MP} = \left[(p_p - p_a)\,A_p + \rho\,U_p\,(U_p - U_o)\,A_p\right]\mathbf{e}_x.\,} $$

The $y$ and $z$ components vanish: no momentum flux and no pressure force on the sections has a component along $\mathbf{e}_y$ or $\mathbf{e}_z$, so the balance gives $F_{MP,y} = F_{MP,z} = 0$.

### 3.3 Moment on the mouth piece: angular momentum about $O$

Why this tool: the moment of the wall forces is also unknown; the angular momentum balance (Notes Eq. 3.38, fixed control volume, no gravity) gives it from the fluxes through the sections:

$$ \int_{\Sigma_c}\rho\,\left[(\mathbf{x} - \mathbf{x}_0)\wedge\mathbf{v}\right](\mathbf{v}\cdot\mathbf{n})\,d\sigma = \sum\mathbf{M}_{O,\text{ext}}, \qquad \mathbf{x}_0 = \mathbf{x}_O. $$

Entrance $\Sigma_p$: $\mathbf{x} - \mathbf{x}_O = \boldsymbol{\eta}$, $\mathbf{v} = U_p\mathbf{e}_x$ uniform and $\int\boldsymbol{\eta}\,d\sigma = 0$, so both the angular momentum flux $-\rho U_p^2\left(\int\boldsymbol{\eta}\,d\sigma\right)\wedge\mathbf{e}_x$ and the moment of the pressure force $(p_p - p_a)\left(\int\boldsymbol{\eta}\,d\sigma\right)\wedge\mathbf{e}_x$ vanish. Exit $\Sigma_o$: $\mathbf{x} - \mathbf{x}_O = \mathbf{x}_o + \boldsymbol{\eta}$ and $\int\boldsymbol{\eta}\,d\sigma = 0$, so with $\mathbf{x}_o \wedge \mathbf{e}_x = (X\,\mathbf{e}_x - H\,\mathbf{e}_y)\wedge\mathbf{e}_x = -H\,\mathbf{e}_y\wedge\mathbf{e}_x = +H\,\mathbf{e}_z$ (since $\mathbf{e}_y\wedge\mathbf{e}_x = -\mathbf{e}_z$), the flux is

$$ \int_{\Sigma_o}\rho\,\left[(\mathbf{x}_o + \boldsymbol{\eta})\wedge U_o\mathbf{e}_x\right]U_o\,d\sigma = \rho\,U_o^2\,A_o\,(\mathbf{x}_o\wedge\mathbf{e}_x) = \rho\,U_o^2\,H\,A_o\,\mathbf{e}_z. $$

The pressure moment on $\Sigma_o$ vanishes ($p - p_a = 0$), viscous stresses are negligible on the sections, and the moment of the wall force on the water is $-\mathbf{M}_{MP}$. Hence $\rho U_o^2 H A_o\,\mathbf{e}_z = -\mathbf{M}_{MP}$ and

$$ \boxed{\,\mathbf{M}_{MP} = -\rho\,U_o^2\,H\,A_o\,\mathbf{e}_z = -\rho\,\frac{A_p^2}{A_o}\,U_p^2\,H\,\mathbf{e}_z\,}\quad\text{about the centre of the entrance section.} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- $A_o < A_p$ implies $U_o > U_p$: the nozzle accelerates the liquid, and the momentum flux $\rho U_p A_p\,(U_o - U_p) > 0$ is the reaction that the wall supplies on the water.
- The moment is non-zero only because the exit axis is displaced by $H$ from the entrance axis: for $H \to 0$ the jet leaves along the line of the entrance axis and $\mathbf{M}_{MP} \to 0$. The sign is negative: with the exit below the entrance, the moment is clockwise as seen in the figure (with $\mathbf{e}_z$ pointing towards the reader).
- Limit $A_o \to A_p$: $U_o = U_p$ and $\mathbf{F}_{MP} \to (p_p - p_a)A_p\,\mathbf{e}_x$, the pure pressure force; the moment becomes $-\rho U_p^2 H A_p\,\mathbf{e}_z$.
- Dimensions (SI): $[\rho U_p A_p\,(U_p - U_o)] = (\text{kg/m}^3)(\text{m/s})\,\text{m}^2\,(\text{m/s}) = \text{N}$; $[\rho U_o^2 H A_o] = (\text{kg/m}^3)(\text{m}^2/\text{s}^2)\,\text{m}\,\text{m}^2 = \text{N}\cdot\text{m}$.
- Numerical illustration (hypothetical data): $\rho = 1000$ kg/m$^3$, $A_p = 0.02$ m$^2$, $A_o = 0.008$ m$^2$, $U_p = 3$ m/s, $p_p = 2.5\times10^5$ Pa, $p_a = 101325$ Pa, $H = 1.5$ m give $U_o = 7.5$ m/s, $F_{MP,x} = 2703.5$ N and $M_{MP,z} = -675$ N$\cdot$m.
- Agreement with the official solution: CL3.pdf obtains $U_o = (A_p/A_o)\,U_p$, $\mathbf{F}_{MP} = \left[(p_p - p_a)A_p + \rho U_p(U_p - U_o)A_p\right]\mathbf{e}_x$ and $\mathbf{M}_{MP} = -\rho U_o^2 H A_o\,\mathbf{e}_z$, the same results.

> [!info] Extension (beyond the official solution)
> If the flow inside were lossless (not stated in the problem), Bernoulli's equation between both sections, $p_p - p_a = \tfrac{1}{2}\rho\,(U_o^2 - U_p^2)$, would give $F_{MP,x} = \tfrac{1}{2}\rho A_p\,(U_o - U_p)^2 \ge 0$. A real mouth piece has losses, and then the measured $p_p$ is the quantity to use.
