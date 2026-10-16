---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - viscosidad-variable
  - flujo-de-poiseuille
  - temperatura
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS16.pdf"
id: "ns16"
pill: "NS16: Variable viscosity"
tags_html:
  - "Viscosity depending on T"
  - "Pressure-driven channel flow"
  - "Linear temperature profile"
  - "Coupled problem"
---

# Problem NS16: Channel Flow with Temperature-Dependent Viscosity

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

A incompressible fluid has constant density $\rho$, specific heat $c$ and thermal coductivity $k$, while the viscosity $\mu$ is a function of temperature acording to

$$ \mu(T) = \mu_0\left(\frac{T}{T_0}\right)^{3/2} \tag{1} $$

The fluid moves between two infinitely long stagnant walls separated a distance $h$. The flow is two-dimensional in the plane $(x, y)$, where $x$ is the coordinate parallel to the walls and $y$ is perpendicular to the walls. The lower wall temperature is $T_0$ and the upper wall temperature is $2T_0$. Because of the geometry, the velocity and the temperature are functions only of the distance to the walls.

1. Find the vertical component $v$ of the velocity field.

2. Determine the temperature field. Neglect the viscous dissipation.

3. write the viscous stress tensor $\bar{\bar{\tau}}'$, as a fuction of the distance $y$ to the lower wall, the velocity $u(y)$ and its derivatives.

4. Prove that the pressure gradient $\partial P/\partial x$ is constant.

5. Find the horizontal component $u(y)$ of the velocity, assuming the pressure gradient $\partial P/\partial x$ is known.

6. Formulate the problem to be solved if the viscous disipation is not neglected.

HINT:
$$ \int\frac{\xi + C}{(1 + \xi)^{3/2}}\,d\xi = \frac{4 + 2\xi - 2C}{\sqrt{1 + \xi}} $$

Note: The momentum equations with variable viscosity $\mu(T)$ can be written, in cartesian coordinates as:
$$ \rho\frac{\partial v_x}{\partial t} + \rho v_x\frac{\partial v_x}{\partial x} + \rho v_y\frac{\partial v_x}{\partial y} = -\frac{\partial p}{\partial x} + \frac{\partial\tau_{xx}}{\partial x} + \frac{\partial\tau_{xy}}{\partial y} + \rho f_{m,x} $$
$$ \rho\frac{\partial v_y}{\partial t} + \rho v_x\frac{\partial v_y}{\partial x} + \rho v_y\frac{\partial v_y}{\partial y} = -\frac{\partial p}{\partial y} + \frac{\partial\tau_{xy}}{\partial x} + \frac{\partial\tau_{yy}}{\partial y} + \rho f_{m,y} $$

The sheet is headed "FLUID MECHANICS I, 24-01-2020, PROBLEM 1 (10 POINTS). Time: 60 minutes" and carries no figure. Transcribed as printed, including the spelling errors of the sheet ("A incompressible", "coductivity", "acording", "fuction", "disipation") and the capital $P$ of items 4 and 5, which is the reduced pressure of the momentum equations.

Source: NS16.pdf (page 1 of 2: statement; page 2: handwritten solution). Notes.pdf, Chapter 4: continuity Eq. 4.7, momentum Eq. 4.10, energy Eq. 4.34, reduced pressure Eq. 4.13, Navier-Poisson law (Eq. 4.36) with variable $\mu$.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, two-dimensional flow of an incompressible liquid with constant $\rho$, $c$, $k$ and the viscosity $\mu(T)$ of (1), between two fixed infinite walls at $y = 0$ ($T = T_0$) and $y = h$ ($T = 2T_0$). The velocity and the temperature depend only on $y$.
- The walls are impermeable and at rest: $u = v = 0$ at both. No chemical reaction and no radiation.
- The mass force is conservative, $\bar{f}_m = -\nabla U$, and $P = p + \rho U$ is the reduced pressure (Notes.pdf, Eq. 4.13): with $\rho$ constant, $-\partial p/\partial x_i + \rho f_{m,i} = -\partial P/\partial x_i$.
- Data: $[\rho,\ c,\ k,\ \mu_0,\ T_0,\ h]$ and, for item 5, $\partial P/\partial x$. Unknowns: $v$, $T(y)$, $\bar{\bar{\tau}}'$, $u(y)$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $h$ | distance between the walls | m |
| $\mu_0$, $T_0$ | reference viscosity and temperature of (1) | Pa s, K |
| $\rho$, $c$, $k$ | density, specific heat, thermal conductivity (constant) | kg/m$^3$, J/(kg K), W/(m K) |
| $P$ | reduced pressure $p + \rho U$ | Pa |
| $\xi = y/h$ | dimensionless distance to the lower wall | 1 |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cartesian frame $(x,y,z)$: $x$ parallel to the walls, $y$ perpendicular to them and upward from the lower wall, $z$ spanwise; the basis is orthonormal and right-handed.
- Field form: $\bar{v} = u(y)\,\bar{e}_x + v(y)\,\bar{e}_y$, $T = T(y)$, $P = P(x,y)$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $y = 0$ | $u = 0$, $v = 0$, $T = T_0$ | lower wall at rest |
| $y = h$ | $u = 0$, $v = 0$, $T = 2T_0$ | upper wall at rest |

## Phase 3: Step-by-Step Derivation

### 3.1 Vertical velocity (item 1)

$$ \frac{\partial u}{\partial x} + \frac{dv}{dy} = \underbrace{\cancel{\frac{\partial u}{\partial x}}}_{u = u(y)} + \frac{dv}{dy} = 0 \;\Longrightarrow\; v = \text{const} \tag{2} $$

The walls are impermeable: $v = 0$ at $y = 0$ (and at $y = h$), so

$$ \boxed{\,v(y) = 0\,} \tag{3} $$

### 3.2 Temperature without dissipation (item 2)

The energy equation (4.34) with $e = e_o + cT$, $v = 0$, $\partial_x = 0$ and the dissipation neglected is $0 = k\,d^2T/dy^2$ (the convective terms vanish because $v = 0$ and $\partial T/\partial x = 0$; the compression work is zero for $\nabla\cdot\bar{v} = 0$). Integrating twice, $T = B_1 + B_2y$. The conditions $T(0) = T_0$ and $T(h) = 2T_0$ give $B_1 = T_0$ and $B_2 = T_0/h$:

$$ \boxed{\,T(y) = T_0\left(1 + \frac{y}{h}\right)\,} \tag{4} $$

so the viscosity is known as a function of $y$: $\mu(y) = \mu_0\,(1 + y/h)^{3/2}$.

### 3.3 Viscous stress tensor (item 3)

For an incompressible fluid ($\nabla\cdot\bar{v} = 0$) the Navier-Poisson law reduces to $\bar{\bar{\tau}}' = \mu(T)\left(\nabla\bar{v} + \nabla\bar{v}^{\,T}\right)$ with the local viscosity. With $\bar{v} = u(y)\bar{e}_x$ the only non-zero velocity gradient is $du/dy$; then $\tau'_{xx} = 2\mu\,\partial u/\partial x = 0$, $\tau'_{yy} = 2\mu\,dv/dy = 0$ and $\tau'_{xy} = \mu\left(\partial u/\partial y + \partial v/\partial x\right) = \mu\,du/dy$:

$$ \boxed{\,\bar{\bar{\tau}}' = \mu_0\left(1 + \frac{y}{h}\right)^{3/2}\begin{pmatrix}0 & \dfrac{du}{dy}\\[2mm] \dfrac{du}{dy} & 0\end{pmatrix}\,} \tag{5} $$

### 3.4 The pressure gradient is constant (item 4)

With $v = 0$, $\partial_x = \partial_t = 0$ for the velocity, and $\tau'_{xx} = \tau'_{yy} = 0$, the momentum equations of the statement (with the reduced pressure $P$) become

$$ x:\quad 0 = -\frac{\partial P}{\partial x} + \frac{d\tau'_{xy}}{dy}, \qquad y:\quad 0 = -\frac{\partial P}{\partial y} + \underbrace{\cancel{\frac{\partial\tau'_{xy}}{\partial x}}}_{\tau'_{xy} = \tau'_{xy}(y)} + \underbrace{\frac{\partial\tau'_{yy}}{\partial y}}_{=0} \tag{6} $$

The $y$ equation gives $\partial P/\partial y = 0$, hence $P = P(x)$ and $\partial P/\partial x = dP/dx$ depends only on $x$. The $x$ equation reads

$$ \frac{dP}{dx} = \frac{d}{dy}\left[\mu_0\left(1 + \frac{y}{h}\right)^{3/2}\frac{du}{dy}\right] \tag{7} $$

whose left side depends only on $x$ and whose right side depends only on $y$. Two functions of independent variables can only be equal if both are constant:

$$ \boxed{\,\frac{\partial P}{\partial x} = \text{constant}\,} \tag{8} $$

### 3.5 Horizontal velocity (item 5)

Integrating (7) once, with a constant $K_1$: $\mu_0(1 + y/h)^{3/2}\,du/dy = (dP/dx)\,y + K_1$, that is, with $\xi = y/h$ and $C = K_1/(h\,dP/dx)$,

$$ \left(1 + \xi\right)^{3/2}\frac{du}{d\xi} = \frac{h^2}{\mu_0}\frac{dP}{dx}\,(\xi + C) \;\Longrightarrow\; u(\xi) = \frac{h^2}{\mu_0}\frac{dP}{dx}\int_0^\xi\frac{\xi' + C}{(1 + \xi')^{3/2}}\,d\xi' \tag{9} $$

(using $dy = h\,d\xi$ and $u(0) = 0$). By the hint, the antiderivative is $(4 + 2\xi - 2C)/\sqrt{1 + \xi}$ (indeed its derivative is $(1 + \xi)^{-3/2}\left[2(1 + \xi) - (2 + \xi - C)\right] = (\xi + C)(1 + \xi)^{-3/2}$), and Barrow's rule between $0$ and $\xi$ gives

$$ u(\xi) = \frac{h^2}{\mu_0}\frac{dP}{dx}\left[\frac{4 + 2\xi - 2C}{\sqrt{1 + \xi}} - \left(4 - 2C\right)\right] \tag{10} $$

The upper wall condition $u(\xi = 1) = 0$ fixes $C$: $\dfrac{6 - 2C}{\sqrt{2}} = 4 - 2C$, that is $6 - 2C = 4\sqrt{2} - 2\sqrt{2}\,C$, so

$$ C = \frac{3 - 2\sqrt{2}}{1 - \sqrt{2}} = \frac{2\sqrt{2} - 3}{\sqrt{2} - 1} = 1 - \sqrt{2} \tag{11} $$

(since $3 - 2\sqrt{2} = (\sqrt{2} - 1)^2$). Then $4 - 2C = 2(1 + \sqrt{2})$ and $4 + 2\xi - 2C = 2(1 + \sqrt{2} + \xi)$. With $s = \sqrt{1 + \xi} \in [1, \sqrt{2}]$, so that $\xi = s^2 - 1$, the bracket of (10) is $2\left[\dfrac{\sqrt{2} + s^2}{s} - (1 + \sqrt{2})\right] = \dfrac{2\,(s - 1)(s - \sqrt{2})}{s}$:

$$ \boxed{\,u(y) = \frac{2h^2}{\mu_0}\frac{dP}{dx}\,\frac{\left(\sqrt{1 + y/h} - 1\right)\left(\sqrt{1 + y/h} - \sqrt{2}\right)}{\sqrt{1 + y/h}}\,} \tag{12} $$

Equivalent form of (10) with $C = 1 - \sqrt{2}$: $u = \dfrac{2h^2}{\mu_0}\dfrac{dP}{dx}\left[\dfrac{1 + \sqrt{2} + y/h}{\sqrt{1 + y/h}} - (1 + \sqrt{2})\right]$.

### 3.6 Problem with viscous dissipation (item 6)

If the viscous dissipation $\phi_v = \tau'_{xy}\,du/dy = \mu(T)\,(du/dy)^2$ is not neglected, the energy equation becomes $k\,d^2T/dy^2 + \phi_v = 0$ and the temperature is no longer linear: the viscosity depends on the unknown $T(y)$, which in turn depends on $u(y)$ through $\phi_v$. The system to solve, in $u(y)$ and $T(y)$ with constant $dP/dx$, is

$$ k\frac{d^2T}{dy^2} + \mu_0\left(\frac{T}{T_0}\right)^{3/2}\left(\frac{du}{dy}\right)^2 = 0, \qquad \frac{d}{dy}\left[\mu_0\left(\frac{T}{T_0}\right)^{3/2}\frac{du}{dy}\right] = \frac{dP}{dx} \tag{13} $$

$$ y = 0:\ T = T_0,\ u = 0; \qquad y = h:\ T = 2T_0,\ u = 0 \tag{14} $$

Equation (6) and the argument of item 4 still hold ($v = 0$, $P = P(x)$ with $dP/dx$ constant) because they do not depend on how $\mu$ varies with $y$. The two equations (13) are coupled and nonlinear: a more complex system that must be solved numerically.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The temperature rises linearly from $T_0$ to $2T_0$ and the viscosity grows by the factor $2^{3/2} \simeq 2.83$ towards the hot wall. The liquid is therefore less viscous (faster) near the cold wall and the velocity maximum is displaced towards the cold wall, away from the centre of the channel.
- **Limits.** For constant viscosity ($\mu = \mu_0$) the profile would be the symmetric parabola $u = (1/(2\mu_0))(dP/dx)(y^2 - hy)$, with its maximum at $y = h/2$. The sign of (12): since $(s - 1) \geq 0$ and $(s - \sqrt{2}) \leq 0$, $u \geq 0$ for $dP/dx < 0$ (flow towards $+x$), as it must be. The profile vanishes at $s = 1$ ($y = 0$) and at $s = \sqrt{2}$ ($y = h$).
- **Dimensional check.** $h^2\,(dP/dx)/\mu_0$ has units $\mathrm{m^2\cdot Pa/m}/(\mathrm{Pa\,s}) = \mathrm{m/s}$, a velocity. $C$ is dimensionless. The hint integral is dimensionless.
- **Check of (11).** With $C = 1 - \sqrt{2}$: $(6 - 2C)/\sqrt{2} = (4 + 2\sqrt{2})/\sqrt{2} = 2\sqrt{2} + 2$ and $4 - 2C = 2 + 2\sqrt{2}$, equal as required by $u(h) = 0$.
