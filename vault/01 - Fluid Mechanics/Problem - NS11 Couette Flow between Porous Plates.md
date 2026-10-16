---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - couette
  - transpiracion
  - balance-integral
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS11.pdf"
id: "ns11"
pill: "NS11: Porous Couette"
tags_html:
  - "Couette flow with injection"
  - "Pathline"
  - "Wall forces and heat fluxes"
  - "Integral balances"
---

# Problem NS11: Couette Flow between Porous Plates

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

A perfect liquid of constant properties (density $\rho$, viscosity $\mu$, thermal conductivity $k$ and specific heat $c$) is confined between two infinite parallel plates at a distance $h$, as depicted in the figure below. The lower wall is at rest, while the upper one moves parallel to itself with a constant velocity $U$ in the positive $x$-direction. The working fluid is injected through the lower porous wall into the channel with a uniform velocity $v_l$ in the $y$-direction, while being removed from the channel through the upper porous plate with a uniform velocity $v_u$, also in the $y$-direction.

Gravitational forces can be neglected. The velocity field, $\bar{v} = u\bar{e}_x + v\bar{e}_y$, is assumed steady and independent of the $x$- and $z$-coordinates, $\partial/\partial t = \partial/\partial x = \partial/\partial z = 0$. The pressure at the upper wall has a constant value $p_u$. The lower and upper walls are kept at constant temperatures $T_l$ and $T_u$, respectively. Known data: $(\rho, \mu, k, c, h, U, v_l, p_u, T_l, T_u)$.

1. (1 point). Obtain the only possible value of $v_u$ consistent with the assumption of $x$-independence, and find $v(y)$.

2. (2.5 points). Determine the pressure field $p(x, y)$, and the horizontal velocity field, $u(y)$. Express $u(y)$ in terms of the Reynolds number based on the injection velocity, $\mathrm{Re} = \rho v_lh/\mu$.

3. (1 point). Compute the volume flux per unit spanwise length, $Q$, across a surface perpendicular to the plates ($z$ is the spanwise direction). Particularize for the limit $\mathrm{Re} \ll 1$, and explain the result.

4. (1.5 points). Obtain the trajectory of the fluid particle with initial position $(x, y) = (0, x_0)$ at $t = 0$, and the corresponding pathline. Compute the time $t_s$ at which the particle arrives at the upper wall, and the corresponding position $x_s$.

5. (1 point). Compute the viscous force per unit surface that the fluid exerts on the lower and upper walls. Particularize for the limit $\mathrm{Re} \ll 1$, and explain the result.

6. (2 points). Write the differential equation and boundary conditions that determine the temperature field, $T(y)$. Obtain $T(y)$ neglecting the effect of viscous dissipation.

7. (1 point). Compute the conductive heat flux (heat transferred by conduction p.u. surface) from the fluid to each wall.

8. (2 additional points). Using an appropriately defined control volume, perform integral momentum and energy balances, and discuss the results of questions 5 and 7 in the light of these integral balances.

The sheet is headed "INTRODUCTION TO FLUID MECHANICS, Jan 14, 2013, PROBLEM 2 (1 hour)".

![[attachments/FM-T4/ns11-statement.png]]
*Statement figure (crop of NS11.pdf, p. 1): channel of height $h$ between two porous plates, injection velocity $v_l$ through the lower wall at rest, upper wall moving with velocity $U$, axes $x$ and $y$*

Source: NS11.pdf (page 1 of 3: statement; pages 2 and 3: handwritten solution). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41, energy Eq. 4.42, internal-energy balance Eq. 4.25, stress components in Cartesian coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady planar flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$) between two porous plates, with $\partial/\partial x = \partial/\partial z = \partial/\partial t = 0$ for the velocity. Gravity neglected; no chemical reaction and no radiation.
- The lower wall ($y = 0$) is at rest at $T_l$ and injects the liquid with the uniform normal velocity $v_l > 0$; the upper wall ($y = h$) moves with $U\bar{e}_x$ at $T_u$ and the pressure on it is $p_u$. The tangential velocity of the liquid equals that of each wall (no-slip).
- Data: $(\rho,\ \mu,\ k,\ c,\ h,\ U,\ v_l,\ p_u,\ T_l,\ T_u)$. Unknowns: $v_u$, $v(y)$, $p$, $u(y)$, $Q$, the pathline, the wall forces, $T(y)$ and the wall heat fluxes.
- Dimensionless numbers: $\mathrm{Re} = \rho v_lh/\mu$ and $\mathrm{Pr} = \mu c/k$, so that $\rho cv_lh/k = \mathrm{Re}\,\mathrm{Pr}$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $h$ | gap between the plates | m |
| $U$ | velocity of the upper wall | m/s |
| $v_l$, $v_u$ | injection and removal velocities | m/s |
| $p_u$ | pressure on the upper wall | Pa |
| $T_l$, $T_u$ | wall temperatures | K |
| $\mathrm{Re}$, $\mathrm{Pr}$ | injection Reynolds number, Prandtl number | 1 |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cartesian frame $(x,y,z)$: $x$ along the plates in the direction of $U$, $y$ normal to the plates and upward from the lower wall, $z$ spanwise. The basis is orthonormal and right-handed (no change of basis).
- Field form: $\bar{v} = u(y)\,\bar{e}_x + v(y)\,\bar{e}_y$, $T = T(y)$, $p = p(x,y)$.
- Control volume for item 8: the box $0 < y < h$ and width $\Delta x$ in $x$ (unit spanwise length); surfaces: the lower wall $\Sigma_l$ ($\bar{n} = -\bar{e}_y$), the upper wall $\Sigma_u$ ($\bar{n} = +\bar{e}_y$) and the two faces $\Sigma_1$, $\Sigma_2$ ($\bar{n} = \mp\bar{e}_x$).

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $y = 0$ | $u = 0$, $v = v_l$, $T = T_l$ | lower wall at rest, injection |
| $y = h$ | $u = U$, $v = v_u$, $T = T_u$ | upper wall moving, removal |
| $y = h$ | $p = p_u$ | statement |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity: $v_u$ and $v(y)$ (item 1)

$$ \underbrace{\cancel{\frac{\partial u}{\partial x}}}_{\partial_x = 0} + \frac{dv}{dy} = 0 \;\Longrightarrow\; v = \text{const} \tag{1} $$

The constant is the injection velocity, $v(0) = v_l$, so $v = v_l$ for every $y$ and the removal velocity must be the same:

$$ \boxed{\,v_u = v_l, \qquad v(y) = v_l\,} \tag{2} $$

### 3.2 Pressure and horizontal velocity (item 2)

y-momentum, with $v = v_l$ constant ($dv/dy = 0$) and no gravity:

$$ \rho\Big(\underbrace{\cancel{u\frac{\partial v}{\partial x}}}_{\partial_x = 0} + v\underbrace{\frac{dv}{dy}}_{=0}\Big) = -\frac{\partial p}{\partial y} + \mu\underbrace{\frac{d^2v}{dy^2}}_{=0} \;\Longrightarrow\; \frac{\partial p}{\partial y} = 0 \;\Longrightarrow\; p = p(x) \tag{3} $$

The pressure on the upper wall is $p_u$ for every $x$, so $p$ is the constant $p_u$:

$$ \boxed{\,p(x,y) = p_u\ \ \text{for all } x,\,y\,}, \qquad \frac{\partial p}{\partial x} = 0 \tag{4} $$

x-momentum:

$$ \rho\Big(\underbrace{\cancel{u\frac{\partial u}{\partial x}}}_{\partial_x = 0} + v_l\frac{du}{dy}\Big) = -\underbrace{\frac{\partial p}{\partial x}}_{=0} + \mu\frac{d^2u}{dy^2} \;\Longrightarrow\; \frac{d^2u}{dy^2} - \frac{\mathrm{Re}}{h}\frac{du}{dy} = 0 \tag{5} $$

since $\rho v_l/\mu = \mathrm{Re}/h$. Trying $u = e^{\lambda y}$ gives $\lambda(\lambda - \mathrm{Re}/h) = 0$, so $u = C_1 + C_2\,e^{\mathrm{Re}\,y/h}$. The conditions $u(0) = 0$ and $u(h) = U$ give $C_1 = -C_2$ and $C_2(e^{\mathrm{Re}} - 1) = U$:

$$ \boxed{\,u(y) = U\,\frac{e^{\mathrm{Re}\,y/h} - 1}{e^{\mathrm{Re}} - 1}\,} \tag{6} $$

For $\mathrm{Re} \to 0$, the Taylor expansion $e^x = 1 + x + O(x^2)$ gives $u \to U\,\dfrac{\mathrm{Re}\,y/h}{\mathrm{Re}} = U\,\dfrac{y}{h}$: plane Couette flow is recovered.

### 3.3 Volume flux (item 3)

The flux per unit spanwise length through a section $x = \text{const}$ is $Q = \int_0^hu\,dy$. The antiderivative of $e^{\mathrm{Re}\,y/h} - 1$ is $(h/\mathrm{Re})\,e^{\mathrm{Re}\,y/h} - y$, and Barrow's rule between $0$ and $h$ gives $(h/\mathrm{Re})(e^{\mathrm{Re}} - 1) - h$:

$$ \boxed{\,Q = \frac{U}{e^{\mathrm{Re}} - 1}\left[\frac{h}{\mathrm{Re}}\left(e^{\mathrm{Re}} - 1\right) - h\right] = Uh\left[\frac{1}{\mathrm{Re}} - \frac{1}{e^{\mathrm{Re}} - 1}\right]\,} \tag{7} $$

For $\mathrm{Re} \ll 1$, $e^{\mathrm{Re}} - 1 = \mathrm{Re}\left(1 + \mathrm{Re}/2 + \mathrm{Re}^2/6 + \dots\right)$, so $1/(e^{\mathrm{Re}} - 1) = 1/\mathrm{Re} - 1/2 + \mathrm{Re}/12 + \dots$ and

$$ Q \simeq Uh\left(\frac{1}{2} - \frac{\mathrm{Re}}{12}\right) \to \frac{Uh}{2} \tag{8} $$

The flux tends to that of plane Couette flow, the mean velocity $U/2$ times the gap: for small injection velocity the transverse flow barely distorts the linear profile.

### 3.4 Trajectory and pathline (item 4)

A particle moves with the local velocity: $dy/dt = v_l$ and $dx/dt = u(y)$. Let its initial position be $(x_i, y_i)$ at $t = 0$. Then $y = y_i + v_lt$ and, with $dt = dy/v_l$,

$$ x - x_i = \int_0^tu\,dt' = \frac{U}{v_l\,(e^{\mathrm{Re}} - 1)}\int_{y_i}^y\left(e^{\mathrm{Re}\,y'/h} - 1\right)dy' = \frac{U}{v_l\,(e^{\mathrm{Re}} - 1)}\left[\frac{h}{\mathrm{Re}}\left(e^{\mathrm{Re}\,y/h} - e^{\mathrm{Re}\,y_i/h}\right) - (y - y_i)\right] \tag{9} $$

which is the pathline $x(y)$; with $y = y_i + v_lt$ it is also the trajectory $x(t)$. The particle reaches the upper wall at $y = h$:

$$ t_s = \frac{h - y_i}{v_l}, \qquad x_s = x_i + \frac{U}{v_l\,(e^{\mathrm{Re}} - 1)}\left[\frac{h}{\mathrm{Re}}\left(e^{\mathrm{Re}} - e^{\mathrm{Re}\,y_i/h}\right) - (h - y_i)\right] \tag{10} $$

> [!info] Reading of the initial position
> The sheet writes the initial position as $(x, y) = (0, x_0)$; the handwritten solution takes the particle at the lower wall, $(x, y) = (x_0, 0)$. Both follow from (9) and (10): for the printed values $(x_i, y_i) = (0, x_0)$ and for the reading of the key $(x_i, y_i) = (x_0, 0)$, which gives $t_s = h/v_l$.

$$ \boxed{\,x - x_0 = \frac{U}{e^{\mathrm{Re}} - 1}\left[\frac{h}{\mathrm{Re}\,v_l}\left(e^{\mathrm{Re}\,v_lt/h} - 1\right) - t\right], \quad t_s = \frac{h}{v_l}, \quad x_s = x_0 + \frac{Uh}{v_l}\left[\frac{1}{\mathrm{Re}} - \frac{1}{e^{\mathrm{Re}} - 1}\right]\,} \qquad (y_i = 0) \tag{11} $$

Note that $x_s - x_0 = Q/v_l$: the particle crosses the channel in the time $h/v_l$ at the mean horizontal velocity $Q/h$.

### 3.5 Viscous forces on the walls (item 5)

The normal pointing into the liquid is $+\bar{e}_y$ on the lower wall and $-\bar{e}_y$ on the upper wall; $(-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot\bar{n}$ is the force per unit area that the liquid exerts on the wall. The viscous components are $\tau'_{xy} = \mu\,du/dy$ and $\tau'_{yy} = 2\mu\,dv/dy = 0$ (Notes.pdf, stress components, Cartesian coordinates). From (6), $du/dy = \dfrac{U\,\mathrm{Re}}{h}\dfrac{e^{\mathrm{Re}\,y/h}}{e^{\mathrm{Re}} - 1}$:

$$ \bar{f}_l^{\,\text{visc}} = \bar{\bar{\tau}}'\cdot\bar{e}_y = \mu\frac{du}{dy}\Big|_0\bar{e}_x = \frac{\mu U\,\mathrm{Re}}{h\,(e^{\mathrm{Re}} - 1)}\bar{e}_x, \qquad \bar{f}_u^{\,\text{visc}} = \bar{\bar{\tau}}'\cdot(-\bar{e}_y) = -\mu\frac{du}{dy}\Big|_h\bar{e}_x = -\frac{\mu U\,\mathrm{Re}\,e^{\mathrm{Re}}}{h\,(e^{\mathrm{Re}} - 1)}\bar{e}_x \tag{12} $$

$$ \boxed{\,\bar{f}_l = \frac{\mu U\,\mathrm{Re}}{h\,(e^{\mathrm{Re}} - 1)}\,\bar{e}_x, \qquad \bar{f}_u = -\frac{\mu U\,\mathrm{Re}\,e^{\mathrm{Re}}}{h\,(e^{\mathrm{Re}} - 1)}\,\bar{e}_x\,} \tag{13} $$

For $\mathrm{Re} \ll 1$, $\mathrm{Re}/(e^{\mathrm{Re}} - 1) \to 1$ and $\mathrm{Re}\,e^{\mathrm{Re}}/(e^{\mathrm{Re}} - 1) \to 1$: $\bar{f}_l \to \dfrac{\mu U}{h}\bar{e}_x$ and $\bar{f}_u \to -\dfrac{\mu U}{h}\bar{e}_x$, the equal and opposite shear forces of plane Couette flow. For $\mathrm{Re} \neq 0$ they are not equal: the lower wall, where the injected liquid has no horizontal velocity, feels less shear than the upper one.

### 3.6 Temperature (item 6)

The energy equation (4.42) with $v = v_l$ and $\partial_x = 0$, and the boundary conditions, are

$$ \rho c\,v_l\frac{dT}{dy} = \mu\left(\frac{du}{dy}\right)^2 + k\frac{d^2T}{dy^2}, \qquad T(0) = T_l, \quad T(h) = T_u \tag{14} $$

where $\phi_v = \mu(du/dy)^2$ is the viscous dissipation. Neglecting it, and dividing by $k$ with $\rho cv_lh/k = \mathrm{Re}\,\mathrm{Pr}$:

$$ \frac{d^2T}{dy^2} - \frac{\mathrm{Re}\,\mathrm{Pr}}{h}\frac{dT}{dy} = 0 \;\Longrightarrow\; T = B_1 + B_2\,e^{\mathrm{Re}\,\mathrm{Pr}\,y/h} \tag{15} $$

the same equation as (5) with $\mathrm{Re}$ replaced by $\mathrm{Re}\,\mathrm{Pr}$. The conditions $T(0) = T_l$ and $T(h) = T_u$ give $B_1 + B_2 = T_l$ and $B_2(e^{\mathrm{Re}\,\mathrm{Pr}} - 1) = T_u - T_l$:

$$ \boxed{\,\frac{T - T_l}{T_u - T_l} = \frac{e^{\mathrm{Re}\,\mathrm{Pr}\,y/h} - 1}{e^{\mathrm{Re}\,\mathrm{Pr}} - 1}\,} \tag{16} $$

### 3.7 Heat flux to each wall (item 7)

The heat flux from the liquid to a wall is $\bar{q}\cdot\bar{n}$ with $\bar{n}$ pointing out of the liquid and $\bar{q} = -k\nabla T$. From (16), $dT/dy = (T_u - T_l)\dfrac{\mathrm{Re}\,\mathrm{Pr}}{h}\dfrac{e^{\mathrm{Re}\,\mathrm{Pr}\,y/h}}{e^{\mathrm{Re}\,\mathrm{Pr}} - 1}$, and $k\,\mathrm{Re}\,\mathrm{Pr}/h = \rho cv_l$:

$$ \boxed{\,q_u = -k\frac{dT}{dy}\Big|_h = -\rho cv_l\,(T_u - T_l)\,\frac{e^{\mathrm{Re}\,\mathrm{Pr}}}{e^{\mathrm{Re}\,\mathrm{Pr}} - 1}, \qquad q_l = k\frac{dT}{dy}\Big|_0 = \rho cv_l\,(T_u - T_l)\,\frac{1}{e^{\mathrm{Re}\,\mathrm{Pr}} - 1}\,} \tag{17} $$

For $\mathrm{Re}\,\mathrm{Pr} \to 0$, $q_l \to k(T_u - T_l)/h$ and $q_u \to -k(T_u - T_l)/h$: pure conduction between the walls.

### 3.8 Integral balances (item 8)

*Momentum, $x$ component* (Notes.pdf, integral momentum balance for the fixed volume, steady):

$$ \int_{\Sigma}\rho\,u\,(\bar{v}\cdot\bar{n})\,d\sigma = -\int_\Sigma p\,n_x\,d\sigma + \int_\Sigma(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma $$

| Surface | $\int\rho u\,\bar{v}\cdot\bar{n}\,d\sigma$ | $-\int p\,n_x\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_l$ | $0$ ($u = 0$) | $0$ ($n_x = 0$) | $-\mu\,u'(0)\,\Delta x$ |
| $\Sigma_u$ | $\rho\,U\,v_l\,\Delta x$ | $0$ ($n_x = 0$) | $+\mu\,u'(h)\,\Delta x$ |
| $\Sigma_1 + \Sigma_2$ | cancel | cancel ($p$ uniform) | cancel ($\tau'_{xx} = 0$) |

$$ \rho\,v_l\,U = \mu\left[\frac{du}{dy}\Big|_h - \frac{du}{dy}\Big|_0\right] \tag{18} $$

Using (13), this is $\rho v_lU = -(f_{u,x} + f_{l,x})$: the net horizontal force that the liquid exerts on the two walls is $-\rho v_lU$, because the liquid leaves through the upper wall carrying the horizontal momentum $\rho U$ per unit mass, which it does not have when it enters through the lower one, and the walls supply it. Equation (18) holds exactly for every $\mathrm{Re}$ (indeed $\mu\,U\,\mathrm{Re}/h = \rho v_lU$) and confirms (13); for $\mathrm{Re} \to 0$ the right-hand side vanishes and the two shear forces cancel.

*Internal energy* (Notes.pdf, Eq. 4.25, steady, no compression work, dissipation neglected): $\displaystyle\int_\Sigma\rho c\,T\,(\bar{v}\cdot\bar{n})\,d\sigma = -\int_\Sigma\bar{q}\cdot\bar{n}\,d\sigma$. The faces $\Sigma_1$, $\Sigma_2$ cancel and the walls give

$$ \rho c\,v_l\,(T_u - T_l)\,\Delta x = -(q_u + q_l)\,\Delta x \;\Longrightarrow\; q_u + q_l = -\rho c\,v_l\,(T_u - T_l) \tag{19} $$

which agrees with (17): the sum of the heat conducted out through the two walls balances the net enthalpy flux that the liquid carries across the control volume, $\rho cv_l(T_u - T_l)$, so that the conductive heat flux balances the net internal-energy flux through the volume.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The injection convects momentum and heat across the channel: for $\mathrm{Re} > 0$ the profiles are exponential, with the velocity gradient concentrated near the upper wall (towards which the liquid is carried), and the thermal profile has the same form with $\mathrm{Re}\,\mathrm{Pr}$.
- **Limits.** For $\mathrm{Re} \to 0$: $u = Uy/h$, $Q = Uh/2$, $\bar{f}_l = -\bar{f}_u = \mu U/h\,\bar{e}_x$ and the temperature is linear (Couette flow with conduction). For $\mathrm{Re} \gg 1$, $u \simeq U\,e^{\mathrm{Re}\,(y - h)/h}$: the horizontal velocity is confined to a layer of thickness $h/\mathrm{Re}$ at the upper wall and $Q \simeq Uh/\mathrm{Re} \to 0$, since the injected liquid, which starts at rest, is swept to the upper wall before it can be dragged.
- **Dimensional check.** $\rho v_lh/\mu$ is dimensionless; $Uh$ has units of a flux per unit span, m$^2$/s; $\mu U\,\mathrm{Re}/h$ is N/m$^2$; $\rho cv_l\,\Delta T$ is W/m$^2$.
- **Consistency of the limits.** At $\mathrm{Re} = 0$, (18) gives $0 = 0$ and (19) gives $q_u = -q_l$.
