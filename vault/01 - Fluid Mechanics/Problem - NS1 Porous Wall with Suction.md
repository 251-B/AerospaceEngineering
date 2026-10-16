---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - succion
  - capa-limite
  - conduccion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS1.pdf"
id: "ns1"
pill: "NS1: Suction"
tags_html:
  - "Unidirectional flow"
  - "Porous wall"
  - "Viscous dissipation"
  - "Streamline"
---

# Problem NS1: Porous Wall with Suction

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

Consider the steady planar motion of a perfect liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$ and specific heat $c$ in the vicinity of a horizontal porous wall. Far from the wall, the horizontal velocity component is $v_x = U_\infty$, the pressure is given by $p + \rho g z = P_\infty$ and the temperature is $T = T_\infty$, different from the value $T_w$ at the wall. The liquid is sucked through the pores of the wall, resulting in a transverse velocity $v_z = -V_w$ at the wall surface. In the analysis, assume that the velocity and temperature fields are only a function of the distance to the wall $z$.

1. Determine the velocity components $v_x(z)$ and $v_z(z)$ and well as the pressure field $p(x, z)$.

2. Obtain the temperature field $T(z)$.

3. Calculate the streamline that crosses $x = x_o$ and $z = 0$.

4. Compute the viscous stress on the wall.

5. Determine the heat flux from the fluid to the wall.

![[attachments/FM-T4/ns1-statement.png]]
*Statement figure (crop of NS1.pdf, p. 1): horizontal porous wall at temperature $T_w$ with suction velocity $V_w$, free stream $U_\infty$, $T_\infty$, $P_\infty$, gravity $g$ and axes $x$, $z$*

Source: NS1.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.7, incompressible momentum Eq. 4.12, perfect-liquid energy Eq. 4.42, no-slip and far-field conditions (Section on initial and boundary conditions).

## Phase 1: Hypotheses, Data and Unknowns

- Steady planar flow of an incompressible liquid with constant $\rho$, $\mu$, $k$, $c$ (perfect liquid, Notes.pdf, Eq. 4.38): the equations to use are (4.40), (4.41) and (4.42).
- Gravity acts along $-\bar{e}_z$ (the far-field pressure is $p + \rho g z = P_\infty$, so $\bar{f}_m = -g\,\bar{e}_z$).
- Given: the fields depend only on the distance to the wall, $\partial/\partial x = \partial/\partial y = \partial/\partial t = 0$ for every variable, except that the pressure is allowed to depend on $x$ (it is determined below).
- No chemical reaction and no radiation: $Q_c = Q_r = 0$.
- The wall is at rest and porous: the tangential velocity is zero (no-slip) and the normal velocity is the suction velocity.
- Data: $[\rho,\ \mu,\ k,\ c,\ U_\infty,\ P_\infty,\ T_\infty,\ T_w,\ V_w,\ g]$ with $V_w > 0$. Unknowns: $v_x(z)$, $v_z(z)$, $p(x,z)$, $T(z)$, the streamline, the wall stress and the wall heat flux.
- Degrees of freedom: two velocity components, the pressure and the temperature, each a function of one coordinate (plus $x$ for the pressure): four unknown fields against continuity, two momentum components and the energy equation.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $\rho$, $\mu$, $\nu = \mu/\rho$ | density, dynamic and kinematic viscosity | kg/m$^3$, Pa s, m$^2$/s |
| $k$, $c$, $\alpha = k/(\rho c)$ | thermal conductivity, specific heat, thermal diffusivity | W/(m K), J/(kg K), m$^2$/s |
| $\mathrm{Pr} = \nu/\alpha = \mu c/k$ | Prandtl number | 1 |
| $U_\infty$, $V_w$ | free-stream velocity, suction velocity | m/s |
| $P_\infty$, $T_\infty$, $T_w$ | far-field reduced pressure, far-field and wall temperatures | Pa, K, K |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cartesian frame $(x,y,z)$ with $x$ along the wall (in the direction of $U_\infty$), $z$ normal to it and pointing into the liquid, $y$ out of the plane. The basis $\{\bar{e}_x,\bar{e}_y,\bar{e}_z\}$ is orthonormal and right-handed, so no change of basis is needed ($\det R = 1$, $R R^T = I$ with $R = I$).
- Field form: $\bar{v} = v_x(z)\,\bar{e}_x + v_z(z)\,\bar{e}_z$, $T = T(z)$, $p = p(x,z)$.
- The wall is at $z = 0$ and the liquid occupies $z > 0$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $z = 0$ | $v_x = 0$ | no-slip on the wall at rest |
| $z = 0$ | $v_z = -V_w$ | suction through the pores (statement) |
| $z = 0$ | $T = T_w$ | thermal equilibrium at the wall |
| $z \to \infty$ | $v_x \to U_\infty$ | free stream (statement) |
| $z \to \infty$ | $p + \rho g z \to P_\infty$ | free stream (statement) |
| $z \to \infty$ | $T \to T_\infty$ | free stream (statement) |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity and the normal velocity

$$ \nabla\cdot\bar{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_z}{\partial z} = \underbrace{\cancel{\frac{\partial v_x}{\partial x}}}_{v_x = v_x(z)} + \frac{dv_z}{dz} = 0 \;\Longrightarrow\; \frac{dv_z}{dz} = 0 \;\Longrightarrow\; v_z = \text{const} \tag{1} $$

The constant is fixed at the wall: $v_z(0) = -V_w$, therefore

$$ \boxed{\,v_z(z) = -V_w\,} \tag{2} $$

### 3.2 Momentum equations

For $\bar{f}_m = -g\,\bar{e}_z$ the Cartesian components of (4.41) with constant $\mu$ are (Notes.pdf, Section on the Navier-Stokes equations in Cartesian coordinates). Every term that contains $\partial/\partial t$, $\partial/\partial x$ or $\partial/\partial y$ of a velocity component is zero.

z-component:

$$ \rho\Big(\underbrace{\cancel{\frac{\partial v_z}{\partial t}}}_{\text{steady}} + \underbrace{\cancel{v_x\frac{\partial v_z}{\partial x}}}_{v_z = v_z(z)} + v_z\underbrace{\frac{dv_z}{dz}}_{=0\ \text{by (1)}}\Big) = -\frac{\partial p}{\partial z} + \mu\underbrace{\frac{d^2 v_z}{dz^2}}_{=0} - \rho g \;\Longrightarrow\; \frac{\partial p}{\partial z} = -\rho g \tag{3} $$

Integrating (3) with respect to $z$ at fixed $x$ (the "constant" may depend on $x$):

$$ p + \rho g z = f(x) \tag{4} $$

The far-field condition $p + \rho g z \to P_\infty$ holds for every $x$, with $P_\infty$ a constant, so $f(x) = P_\infty$:

$$ \boxed{\,p(x,z) = P_\infty - \rho g z\,}, \qquad \frac{\partial p}{\partial x} = 0 \tag{5} $$

x-component:

$$ \rho\Big(\underbrace{\cancel{\frac{\partial v_x}{\partial t}}}_{\text{steady}} + \underbrace{\cancel{v_x\frac{\partial v_x}{\partial x}}}_{\partial_x = 0} + v_z\frac{dv_x}{dz}\Big) = -\underbrace{\frac{\partial p}{\partial x}}_{=0\ \text{by (5)}} + \mu\frac{d^2 v_x}{dz^2} \;\Longrightarrow\; -\rho V_w\frac{dv_x}{dz} = \mu\frac{d^2 v_x}{dz^2} \tag{6} $$

Dividing by $\mu$ and using $\nu = \mu/\rho$:

$$ \frac{d^2 v_x}{dz^2} + \frac{V_w}{\nu}\frac{dv_x}{dz} = 0 \tag{7} $$

This is a linear ODE with constant coefficients. Trying $v_x = e^{\lambda z}$ gives $\lambda^2 + (V_w/\nu)\lambda = 0$, so $\lambda = 0$ or $\lambda = -V_w/\nu$:

$$ v_x = C_1 + C_2\,e^{-V_w z/\nu} \tag{8} $$

Boundary conditions: $v_x(\infty) = U_\infty$ gives $C_1 = U_\infty$ (the exponential vanishes because $V_w > 0$); $v_x(0) = 0$ gives $C_1 + C_2 = 0$, so $C_2 = -U_\infty$:

$$ \boxed{\,v_x(z) = U_\infty\left(1 - e^{-V_w z/\nu}\right)\,} \tag{9} $$

### 3.3 Energy equation and the temperature field

With $e = e_o + cT$, $\bar{v} = v_x\bar{e}_x + v_z\bar{e}_z$ and $\partial/\partial x = \partial/\partial t = 0$, (4.42) reads

$$ \rho c\,v_z\frac{dT}{dz} = \phi_v + k\frac{d^2T}{dz^2} \tag{10} $$

The viscous dissipation of this flow, from the Cartesian expression of $\phi_v$ (Notes.pdf, Section on the Navier-Stokes equations in Cartesian coordinates), has a single non-zero shear rate $\partial v_x/\partial z$:

$$ \phi_v = \mu\left(\frac{dv_x}{dz}\right)^2, \qquad \frac{dv_x}{dz} = \frac{U_\infty V_w}{\nu}\,e^{-V_w z/\nu} \;\Longrightarrow\; \phi_v = \frac{\mu U_\infty^2 V_w^2}{\nu^2}\,e^{-2V_w z/\nu} \tag{11} $$

Substituting $v_z = -V_w$ and (11) in (10) and dividing by $k$, with $\alpha = k/(\rho c)$:

$$ \frac{d^2T}{dz^2} + \frac{V_w}{\alpha}\frac{dT}{dz} = -\frac{\mu U_\infty^2 V_w^2}{k\,\nu^2}\,e^{-2V_w z/\nu} \tag{12} $$

The solution is the sum of the homogeneous solution $B_1 + B_2e^{-V_w z/\alpha}$ and a particular solution $A\,e^{-2V_w z/\nu}$. Substituting the particular form in (12), with $T_p' = -(2V_w/\nu)A\,e^{-2V_wz/\nu}$ and $T_p'' = (4V_w^2/\nu^2)A\,e^{-2V_wz/\nu}$:

$$ A\left(\frac{4V_w^2}{\nu^2} - \frac{2V_w^2}{\alpha\nu}\right) = -\frac{\mu U_\infty^2V_w^2}{k\nu^2} \;\Longrightarrow\; A\,(4 - 2\,\mathrm{Pr}) = -\frac{\mu U_\infty^2}{k} = -\frac{\mathrm{Pr}\,U_\infty^2}{c} \tag{13} $$

where $\mathrm{Pr} = \nu/\alpha = \mu c/k$ was used. Hence (for $\mathrm{Pr} \neq 2$)

$$ A = \frac{\mathrm{Pr}}{2(\mathrm{Pr} - 2)}\frac{U_\infty^2}{c} \tag{14} $$

so that $T = B_1 + B_2e^{-V_wz/\alpha} + A\,e^{-2V_wz/\nu}$. The condition $T(\infty) = T_\infty$ gives $B_1 = T_\infty$ and $T(0) = T_w$ gives $B_2 = T_w - T_\infty - A$:

$$ \boxed{\,T(z) = T_\infty + \left(T_w - T_\infty - \frac{\mathrm{Pr}\,U_\infty^2}{2(\mathrm{Pr}-2)\,c}\right)e^{-V_wz/\alpha} + \frac{\mathrm{Pr}\,U_\infty^2}{2(\mathrm{Pr}-2)\,c}\,e^{-2V_wz/\nu}\,} \tag{15} $$

Note that $V_wz/\alpha = \mathrm{Pr}\,V_wz/\nu$. For $\mathrm{Pr} = 2$ the two exponents coincide and the particular solution takes the form $A z\,e^{-2V_wz/\nu}$ (a resonant case, not worked out in the sheet).

### 3.4 Streamline through $(x_o, 0)$

The streamlines are the integral curves of $\bar{v}$: $dx/v_x = dz/v_z$. With (2) and (9):

$$ \frac{dx}{dz} = \frac{v_x}{v_z} = -\frac{U_\infty}{V_w}\left(1 - e^{-V_wz/\nu}\right) \tag{16} $$

Integrating from $z' = 0$ (where $x = x_o$) to $z' = z$. The antiderivative of $1 - e^{-az'}$ with $a = V_w/\nu$ is $z' + e^{-az'}/a$, and Barrow's rule gives $[z' + e^{-az'}/a]_0^z = z + (e^{-az} - 1)/a$:

$$ \boxed{\,x - x_o = -\frac{U_\infty}{V_w}\left[z + \frac{\nu}{V_w}\left(e^{-V_wz/\nu} - 1\right)\right]\,} \tag{17} $$

### 3.5 Viscous stress on the wall

The wall is the surface $z = 0$. Take the unit normal pointing into the liquid, $\bar{n} = \bar{e}_z$: then $\bar{\bar{\tau}}'\cdot\bar{n}$ is the viscous force per unit area that the liquid exerts on the wall. The components of $\bar{\bar{\tau}}'$ with the Navier-Poisson law (Notes.pdf, Section on stress components, Cartesian coordinates) are

$$ \bar{\bar{\tau}}'\cdot\bar{e}_z = \tau'_{xz}\,\bar{e}_x + \tau'_{zz}\,\bar{e}_z, \qquad \tau'_{xz} = \mu\left(\frac{\partial v_x}{\partial z} + \frac{\partial v_z}{\partial x}\right) = \mu\frac{dv_x}{dz}, \qquad \tau'_{zz} = 2\mu\frac{dv_z}{dz} + \left(\mu_B - \tfrac{2}{3}\mu\right)\nabla\cdot\bar{v} = 0 \tag{18} $$

At the wall, from (9), $dv_x/dz\big|_{z=0} = U_\infty V_w/\nu$, so

$$ \boxed{\,\bar{\bar{\tau}}'\cdot\bar{n}\Big|_{w} = \mu\frac{U_\infty V_w}{\nu}\,\bar{e}_x = \rho V_w U_\infty\,\bar{e}_x\,} \tag{19} $$

The liquid drags the wall in the direction of the free stream.

### 3.6 Heat flux from the liquid to the wall

The heat flux from the liquid to the wall is $\bar{q}\cdot\bar{n}$ with $\bar{n} = -\bar{e}_z$ (outward from the liquid, into the wall), and $\bar{q} = -k\nabla T$ (Notes.pdf, Eq. 4.36):

$$ \bar{q}\cdot\bar{n}\Big|_w = -k\frac{dT}{dz}\bar{e}_z\cdot(-\bar{e}_z)\Big|_{z=0} = k\frac{dT}{dz}\Big|_{z=0} \tag{20} $$

Differentiating (15) and evaluating at $z = 0$:

$$ \frac{dT}{dz}\Big|_0 = -\frac{V_w}{\alpha}B_2 - \frac{2V_w}{\nu}A = -\frac{V_w}{\nu}\left(\mathrm{Pr}\,B_2 + 2A\right) \tag{21} $$

Using $k/\nu = \rho c/\mathrm{Pr}$ and $B_2 = T_w - T_\infty - A$:

$$ k\frac{dT}{dz}\Big|_0 = -\rho c V_w\left(B_2 + \frac{2A}{\mathrm{Pr}}\right) = -\rho cV_w\left[T_w - T_\infty - A\,\frac{\mathrm{Pr}-2}{\mathrm{Pr}}\right] = -\rho cV_w\left[T_w - T_\infty - \frac{U_\infty^2}{2c}\right] \tag{22} $$

$$ \boxed{\,\bar{q}\cdot\bar{n}\Big|_w = \rho c V_w\left[T_\infty - T_w + \frac{U_\infty^2}{2c}\right]\,} \tag{23} $$

The result does not depend on the Prandtl number.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** Suction pins the shear layer to the wall: the velocity reaches $99\%$ of $U_\infty$ at $z \approx 4.6\,\nu/V_w$ and the thickness $\nu/V_w$ does not grow with $x$. The liquid is pulled towards the wall by the pores, and the viscous diffusion away from the wall balances this convection (equation (6)).
- **Limits.** For $V_w \to 0$ the layer thickens without bound, consistent with the absence of a steady unidirectional solution. For $z \to \infty$, $v_x \to U_\infty$ and $T \to T_\infty$. At $z = 0$, $v_x = 0$ and $T = T_w$.
- **Dimensional check.** $V_wz/\nu$ and $V_wz/\alpha$ are dimensionless. In (23), $\rho cV_w\,\Delta T$ has units $(\mathrm{kg/m^3})(\mathrm{J/(kg\,K)})(\mathrm{m/s})\,\mathrm{K} = \mathrm{W/m^2}$, and $U_\infty^2/(2c)$ has units $(\mathrm{m^2/s^2})/(\mathrm{J/(kg\,K)}) = \mathrm{K}$. In (19), $\rho V_wU_\infty$ has units $\mathrm{kg/(m^2\,s)}\cdot\mathrm{m/s} = \mathrm{N/m^2}$.
- **Energy check.** Equation (23) is the heat that must flow into the wall in steady state: per unit area the suction brings in from the free stream the energy $\rho V_w(cT_\infty + U_\infty^2/2)$ and the pores take out $\rho V_w\,cT_w$; the pressure work and the work of gravity cancel, and the shear does no work on the wall because it is at rest. The difference is $\rho cV_w[T_\infty - T_w + U_\infty^2/(2c)]$, the result (23).
- **Special case.** For $U_\infty \to 0$ there is no dissipation and (23) reduces to $\rho cV_w(T_\infty - T_w)$, the advection-conduction balance of pure suction.
