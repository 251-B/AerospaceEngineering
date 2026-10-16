---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - cilindros-coaxiales
  - par
  - disipacion-viscosa
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS2.pdf"
id: "ns2"
pill: "NS2: Cylinders"
tags_html:
  - "Circular Couette flow"
  - "Torque and power"
  - "Viscous dissipation"
  - "Temperature profile"
---

# Problem NS2: Rotating Coaxial Cylinders

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

Consider the steady planar motion of a perfect liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$ and specific heat $c$ in the gap formed between two coaxial cylinders of radii $R_1$ and $R_2$ that are rotating with angular velocities $\Omega_1$ and $\Omega_2$, respectively. Because of the symmetry of the problem, $v_z = 0$ and $\partial/\partial z = \partial/\partial\theta = 0$.

1. Obtain the velocity and pressure fields.

2. Calculate the torque exerted on each cylinder, as well as the power needed to keep them rotating.

3. If the temperatures on the cylinder surfaces are $T_1$ and $T_2$, determine the temperature distribution $T(r)$.

![[attachments/FM-T4/ns2-statement.png]]
*Statement figure (crop of NS2.pdf, p. 1): inner cylinder $R_1$ at $T_1$ rotating with $\Omega_1$, outer cylinder $R_2$ at $T_2$ rotating with $\Omega_2$, polar coordinates $r$, $\theta$*

Source: NS2.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, perfect-liquid momentum Eq. 4.41 in cylindrical coordinates, energy Eq. 4.42, stress components in cylindrical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady planar motion ($v_z = 0$, $\partial/\partial z = 0$) of a perfect liquid with constant $\rho$, $\mu$, $k$, $c$: equations (4.40)-(4.42) in cylindrical coordinates.
- Axisymmetric: $\partial/\partial\theta = 0$ for every variable.
- No mass force enters the problem in the plane of motion (the statement lists none; gravity, if present, only shifts the pressure by a hydrostatic term and is absorbed in the reduced pressure of Notes.pdf, Eq. 4.13). No chemical reaction and no radiation: $Q_c = Q_r = 0$.
- The cylinder surfaces are impermeable and move with their own angular velocity (no-slip).
- Data: $[\rho,\ \mu,\ k,\ c,\ R_1,\ R_2,\ \Omega_1,\ \Omega_2,\ T_1,\ T_2]$ with $R_2 > R_1$. Unknowns: $v_r(r)$, $v_\theta(r)$, $p(r)$, the torques, the powers and $T(r)$.
- Degrees of freedom: two velocity components, the pressure and the temperature, each a function of $r$ alone.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R_1$, $R_2$ | inner and outer radii | m |
| $\Omega_1$, $\Omega_2$ | angular velocities (positive counter-clockwise, towards increasing $\theta$) | rad/s |
| $T_1$, $T_2$ | temperatures of the inner and outer surfaces | K |
| $\rho$, $\mu$, $k$ | density, viscosity, thermal conductivity | kg/m$^3$, Pa s, W/(m K) |
| $C_1$, $C_2$ | integration constants of $v_\theta$ | 1/s, m$^2$/s |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cylindrical frame $(r,\theta,z)$ centred on the common axis, with $\bar{e}_r$, $\bar{e}_\theta$, $\bar{e}_z$ orthonormal and right-handed ($\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_z$); the frame is attached to the laboratory, which is inertial.
- Field form: $\bar{v} = v_r(r)\,\bar{e}_r + v_\theta(r)\,\bar{e}_\theta$, $p = p(r)$, $T = T(r)$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = R_1$ | $v_r = 0$, $v_\theta = \Omega_1R_1$ | impermeable inner cylinder, no-slip |
| $r = R_2$ | $v_r = 0$, $v_\theta = \Omega_2R_2$ | impermeable outer cylinder, no-slip |
| $r = R_1$ | $T = T_1$ | thermal equilibrium at the wall |
| $r = R_2$ | $T = T_2$ | thermal equilibrium at the wall |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity and the radial velocity

$$ \frac{1}{r}\frac{d(rv_r)}{dr} + \underbrace{\cancel{\frac{1}{r}\frac{\partial v_\theta}{\partial\theta}}}_{\partial_\theta = 0} + \underbrace{\cancel{\frac{\partial v_z}{\partial z}}}_{v_z = 0} = 0 \;\Longrightarrow\; r\,v_r = \text{const} \tag{1} $$

The constant is fixed at the inner wall, where $v_r(R_1) = 0$: $r\,v_r = 0$ for every $r$, therefore

$$ \boxed{\,v_r(r) = 0\,} \tag{2} $$

### 3.2 Azimuthal momentum and the velocity profile

The $\theta$ component of (4.41) in cylindrical coordinates, with $v_r = 0$, $\partial/\partial t = \partial_\theta = \partial_z = 0$ and no mass force:

$$ \rho\Big(\underbrace{\cancel{\frac{\partial v_\theta}{\partial t}}}_{\text{steady}} + \underbrace{\cancel{v_r\frac{\partial v_\theta}{\partial r}}}_{v_r = 0} + \underbrace{\cancel{\frac{v_\theta}{r}\frac{\partial v_\theta}{\partial\theta}}}_{\partial_\theta = 0} + \underbrace{\cancel{\frac{v_rv_\theta}{r}}}_{v_r = 0} + \underbrace{\cancel{v_z\frac{\partial v_\theta}{\partial z}}}_{v_z = 0}\Big) = -\underbrace{\cancel{\frac{1}{r}\frac{\partial p}{\partial\theta}}}_{\partial_\theta = 0} + \mu\frac{d}{dr}\left[\frac{1}{r}\frac{d(rv_\theta)}{dr}\right] \tag{3} $$

Hence $\dfrac{d}{dr}\left[\dfrac{1}{r}\dfrac{d(rv_\theta)}{dr}\right] = 0$. Integrating once, $\dfrac{1}{r}\dfrac{d(rv_\theta)}{dr} = 2C_1$ (the factor 2 is a convenient choice of constant). Multiplying by $r$ and integrating again, $rv_\theta = C_1r^2 + C_2$:

$$ v_\theta = C_1\,r + \frac{C_2}{r} \tag{4} $$

The boundary conditions $v_\theta(R_1) = \Omega_1R_1$ and $v_\theta(R_2) = \Omega_2R_2$, each multiplied by $R_i$, give a linear system:

$$ C_1R_1^2 + C_2 = \Omega_1R_1^2, \qquad C_1R_2^2 + C_2 = \Omega_2R_2^2 \tag{5} $$

Subtracting the first equation from the second, $C_1(R_2^2 - R_1^2) = \Omega_2R_2^2 - \Omega_1R_1^2$, and then $C_2 = \Omega_1R_1^2 - C_1R_1^2$:

$$ C_1 = \frac{\Omega_2R_2^2 - \Omega_1R_1^2}{R_2^2 - R_1^2}, \qquad C_2 = \frac{(\Omega_1 - \Omega_2)\,R_1^2R_2^2}{R_2^2 - R_1^2} \tag{6} $$

$$ \boxed{\,v_\theta(r) = \frac{\Omega_2R_2^2 - \Omega_1R_1^2}{R_2^2 - R_1^2}\,r + \frac{(\Omega_1 - \Omega_2)R_1^2R_2^2}{R_2^2 - R_1^2}\,\frac{1}{r}\,} \tag{7} $$

### 3.3 Radial momentum and the pressure field

The $r$ component of (4.41) with $v_r = 0$ keeps only the centrifugal term and the pressure gradient (all other terms vanish for the same reasons as in (3)):

$$ -\rho\frac{v_\theta^2}{r} = -\frac{dp}{dr} \;\Longrightarrow\; \frac{dp}{dr} = \rho\frac{v_\theta^2}{r} = \rho\left(C_1^2\,r + \frac{2C_1C_2}{r} + \frac{C_2^2}{r^3}\right) \tag{8} $$

Integrating from $R_1$ to $r$, the antiderivatives are $C_1^2r^2/2$, $2C_1C_2\ln r$ and $-C_2^2/(2r^2)$, and Barrow's rule gives

$$ \boxed{\,p(r) - p(R_1) = \rho\left[\frac{C_1^2}{2}\left(r^2 - R_1^2\right) + 2C_1C_2\ln\frac{r}{R_1} - \frac{C_2^2}{2}\left(\frac{1}{r^2} - \frac{1}{R_1^2}\right)\right]\,} \tag{9} $$

The constant $p(R_1)$ is set by the reference pressure of the problem; the pressure grows outwards because the fluid is whirling and needs a centripetal force.

### 3.4 Viscous stress and torque on each cylinder

The only non-zero viscous shear stress is (Notes.pdf, stress components in cylindrical coordinates, with $v_r = 0$):

$$ \tau'_{r\theta} = \mu\left[r\frac{d}{dr}\left(\frac{v_\theta}{r}\right) + \frac{1}{r}\underbrace{\cancel{\frac{\partial v_r}{\partial\theta}}}_{=0}\right] = \mu\,r\frac{d}{dr}\left(C_1 + \frac{C_2}{r^2}\right) = -\frac{2\mu C_2}{r^2} \tag{10} $$

The normal viscous stresses $\tau'_{rr}$ and $\tau'_{\theta\theta}$ are zero ($v_r = 0$, $\nabla\cdot\bar{v} = 0$), and the pressure force on a cylindrical surface is radial, so it has no moment about the axis. Only $\tau'_{r\theta}$ contributes to the torque.

*Inner cylinder* (surface $r = R_1$). The normal pointing into the liquid is $\bar{n} = +\bar{e}_r$, so $\bar{\bar{\tau}}'\cdot\bar{n} = \tau'_{r\theta}\,\bar{e}_\theta$ is the force per unit area that the liquid exerts on the cylinder. The torque per unit length about the axis, with $d\sigma = R_1\,d\theta\,(1)$ and arm $R_1\bar{e}_r$:

$$ \bar{M}_1 = \int_0^{2\pi}R_1\bar{e}_r\wedge\tau'_{r\theta}(R_1)\bar{e}_\theta\,R_1\,d\theta = 2\pi R_1^2\,\tau'_{r\theta}(R_1)\,\bar{e}_z = -4\pi\mu C_2\,\bar{e}_z \tag{11} $$

*Outer cylinder* (surface $r = R_2$). The normal pointing into the liquid is $\bar{n} = -\bar{e}_r$:

$$ \bar{M}_2 = \int_0^{2\pi}R_2\bar{e}_r\wedge\left[-\tau'_{r\theta}(R_2)\bar{e}_\theta\right]R_2\,d\theta = -2\pi R_2^2\,\tau'_{r\theta}(R_2)\,\bar{e}_z = +4\pi\mu C_2\,\bar{e}_z \tag{12} $$

$$ \boxed{\,\bar{M}_1 = -4\pi\mu\frac{(\Omega_1 - \Omega_2)R_1^2R_2^2}{R_2^2 - R_1^2}\,\bar{e}_z = -\bar{M}_2\,} \tag{13} $$

The two torques are equal and opposite, as the angular momentum balance of the liquid requires: in steady motion the total moment on the liquid between the cylinders is zero, so the moments that the cylinders exert on it, $-\bar{M}_1$ and $-\bar{M}_2$, cancel.

### 3.5 Power needed to keep the cylinders rotating

The external agent must exert on each cylinder the opposite of the liquid torque, so the power it supplies is $\dot{W}_i = -\bar{M}_i\cdot\Omega_i\bar{e}_z$:

$$ \dot{W}_1 = +4\pi\mu C_2\,\Omega_1, \qquad \dot{W}_2 = -4\pi\mu C_2\,\Omega_2 \tag{14} $$

$$ \boxed{\,\dot{W} = \dot{W}_1 + \dot{W}_2 = 4\pi\mu C_2\,(\Omega_1 - \Omega_2) = 4\pi\mu\frac{(\Omega_1 - \Omega_2)^2R_1^2R_2^2}{R_2^2 - R_1^2}\,} \tag{15} $$

The total power is non-negative, as it must be: it equals the viscous dissipation in the gap (checked in 3.6).

### 3.6 Temperature distribution

With $v_r = 0$ the convective terms of (4.42) vanish. The energy equation for the steady, axisymmetric flow reads

$$ 0 = \phi_v + \frac{k}{r}\frac{d}{dr}\left(r\frac{dT}{dr}\right) \tag{16} $$

and the viscous dissipation of this flow (cylindrical $\phi_v$ of Notes.pdf, keeping the only non-zero shear $\tau'_{r\theta}$) is

$$ \phi_v = \mu\left[r\frac{d}{dr}\left(\frac{v_\theta}{r}\right)\right]^2 = \mu\left(\frac{2C_2}{r^2}\right)^2 = \frac{4\mu C_2^2}{r^4} \tag{17} $$

Substituting (17) in (16) and multiplying by $r/k$:

$$ \frac{d}{dr}\left(r\frac{dT}{dr}\right) = -\frac{4\mu C_2^2}{k\,r^3} \tag{18} $$

Integrating once, $r\,dT/dr = \dfrac{2\mu C_2^2}{k\,r^2} + B_1$; dividing by $r$ and integrating again:

$$ T(r) = -\frac{\mu C_2^2}{k\,r^2} + B_1\ln r + B_2 \tag{19} $$

Write $a = \mu C_2^2/k$. The conditions $T(R_1) = T_1$ and $T(R_2) = T_2$ give, after eliminating $B_2$,

$$ T - T_1 = a\left(\frac{1}{R_1^2} - \frac{1}{r^2}\right) + B\ln\frac{r}{R_1}, \qquad B\ln\frac{R_2}{R_1} = T_2 - T_1 - a\left(\frac{1}{R_1^2} - \frac{1}{R_2^2}\right) \tag{20} $$

$$ \boxed{\,T(r) - T_1 = \frac{\mu C_2^2}{k}\left(\frac{1}{R_1^2} - \frac{1}{r^2}\right) + \left[T_2 - T_1 - \frac{\mu C_2^2}{k}\left(\frac{1}{R_1^2} - \frac{1}{R_2^2}\right)\right]\frac{\ln(r/R_1)}{\ln(R_2/R_1)}\,} \tag{21} $$

*Check of the power.* Integrating the dissipation over the gap per unit length, with $dV = 2\pi r\,dr$ and the antiderivative of $r^{-3}$ equal to $-1/(2r^2)$:

$$ \int\phi_v\,dV = 2\pi\int_{R_1}^{R_2}\frac{4\mu C_2^2}{r^4}\,r\,dr = 8\pi\mu C_2^2\left[-\frac{1}{2r^2}\right]_{R_1}^{R_2} = 4\pi\mu C_2^2\,\frac{R_2^2 - R_1^2}{R_1^2R_2^2} = 4\pi\mu C_2\,(\Omega_1 - \Omega_2) \tag{22} $$

where $C_2(R_2^2 - R_1^2)/(R_1^2R_2^2) = \Omega_1 - \Omega_2$ from (6) was used. It coincides with (15): the power supplied by the cylinders is dissipated in the liquid and leaves as heat through the two walls.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** $v_\theta = C_1r + C_2/r$ is a rigid rotation (the $C_1r$ term) plus an irrotational vortex (the $C_2/r$ term). Only the vortex part is sheared, with $\tau'_{r\theta} \propto 1/r^2$, so the stress is larger on the inner cylinder.
- **Limits.** For $\Omega_1 = \Omega_2 = \Omega$ the liquid rotates as a rigid body, $v_\theta = \Omega r$, $C_2 = 0$, the torques and the power vanish and $p - p(R_1) = \rho\Omega^2(r^2 - R_1^2)/2$. For $\Omega_2 = 0$ and $R_2 \to \infty$, $v_\theta = \Omega_1R_1^2/r$ and $\bar{M}_1 = -4\pi\mu\Omega_1R_1^2\,\bar{e}_z$, the viscous torque on a spinning cylinder in an unbounded liquid.
- **Dimensional check.** $v_\theta = C_1r + C_2/r$: $C_1$ has units 1/s and $C_2$ has units m$^2$/s. The torque per unit length $4\pi\mu C_2$ has units $(\mathrm{Pa\,s})(\mathrm{m^2/s}) = \mathrm{N}$, that is N m per metre of length. The power per unit length is N m/s per metre $=$ W/m. In (21), $\mu C_2^2/(kr^2)$ has units $(\mathrm{Pa\,s})(\mathrm{m^4/s^2})/[(\mathrm{W/(m\,K)})\,\mathrm{m^2}] = \mathrm{K}$.
- **Role of the dissipation.** If the viscous heating is negligible ($a \to 0$) the temperature is the purely logarithmic conduction profile between $T_1$ and $T_2$.
