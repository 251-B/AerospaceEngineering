---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - cilindro-poroso
  - succion
  - conduccion
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS8.pdf"
id: "ns8"
pill: "NS8: Porous cylinder"
tags_html:
  - "Axisymmetric flow"
  - "Power-law profile"
  - "Suction Reynolds number"
  - "Prandtl number"
---

# Problem NS8: Porous Cylinder Moving Axially with Suction

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

An infinitely long porous cylinder of radius $R$ is surrounded by a liquid of density $\rho$, viscosity $\mu$, specific heat $c$, and thermal conductivity $k$. The cylinder moves axially with velocity $v_z = U$ and entrains liquid through its surface pores with a suction velocity $v_r = -V$, inducing (for $r > R$) an axisymmetric velocity field with components $v_r(r)$, $v_z(r)$ and $v_\theta = 0$. At large radial distances $r \gg R$ from the cylinder the liquid is at rest with uniform pressure $p_\infty$. Assume in the following analysis that the effect of gravity on the fluid motion can be neglected.

1. Use the continuity equation to determine the radial velocity component $v_r(r)$ for $R \leq r < \infty$.

2. From the radial component of the momentum equation compute the pressure distribution, demonstrating in particular that $\partial p/\partial z = 0$.

3. Determine the axial velocity distribution $v_z(r)$ as a function of the suction Reynolds number $\mathrm{Re} = \rho VR/\mu$ (to solve the problem, assume that the two independent solutions of the resulting linear ODE are of the form $v_z \propto r^\alpha$, obtaining the two values of $\alpha$ that are compatible with the equation).

4. Obtain the force acting on the cylinder (per unit length).

5. Calculate the trajectory of the fluid particle located initially at $r = r_o$ and $z = 0$.

6. Compute the temperature field $T(r)$ when the cylinder temperature $T_c$ is different from that of the surrounding atmosphere $T_\infty > T_c$. Neglect viscous dissipation and express the result with use made of the Prandtl number $\mathrm{Pr} = \mu c/k$.

7. Determine the heat transfered to the cylinder per unit time (per unit length).

Transcribed as printed (exam of Dec 16, 2011). On the sheet, the word "the" after "entrains" is struck out, "for $r > R$" is added by hand before "an axisymmetric", and in item 6 the words "$T(r)$" and the sentence "Neglect viscous dissipation and express the result with use made of the Prandtl number $\mathrm{Pr} = \mu c/k$" are handwritten additions. "transfered" is a spelling error of the sheet.

![[attachments/FM-T4/ns8-statement.svg]]
*Statement figure (redrawn from NS8.pdf, p. 1): porous cylinder of radius $R$ at temperature $T_c$ moving with $U$ along $z$, suction velocity $V$ through its surface, ambient $p_\infty$, $T_\infty$ and axes $r$, $z$*

Source: NS8.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 and energy Eq. 4.42 in cylindrical coordinates, stress components in cylindrical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, axisymmetric flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$) around an infinitely long cylinder: the fields depend only on $r$, $\partial/\partial\theta = \partial/\partial z = \partial/\partial t = 0$, with $v_\theta = 0$. Gravity is neglected; no chemical reaction and no radiation; viscous dissipation is neglected in the temperature equation (item 6).
- The cylinder surface is porous: it entrains liquid with $v_r(R) = -V$, $V > 0$, and moves axially with velocity $U$.
- Far from the cylinder the liquid is at rest at $p_\infty$ and $T_\infty$.
- Data: $[\rho,\ \mu,\ c,\ k,\ R,\ U,\ V,\ p_\infty,\ T_c,\ T_\infty,\ r_o]$ with $T_\infty > T_c$. Unknowns: $v_r(r)$, $p(r)$, $v_z(r)$, the force, the particle trajectory, $T(r)$ and the heat rate.
- Dimensionless numbers: the suction Reynolds number $\mathrm{Re} = \rho VR/\mu$ and the Prandtl number $\mathrm{Pr} = \mu c/k$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R$ | cylinder radius | m |
| $U$ | axial velocity of the cylinder | m/s |
| $V$ | suction velocity | m/s |
| $\mathrm{Re}$, $\mathrm{Pr}$ | suction Reynolds number, Prandtl number | 1 |
| $T_c$, $T_\infty$ | cylinder and ambient temperatures | K |
| $r_o$ | initial radius of the fluid particle | m |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cylindrical frame $(r,\theta,z)$ with $z$ along the axis in the direction of $U$; the basis $\{\bar{e}_r,\bar{e}_\theta,\bar{e}_z\}$ is orthonormal and right-handed. The liquid occupies $r > R$.
- Field form: $\bar{v} = v_r(r)\,\bar{e}_r + v_z(r)\,\bar{e}_z$, $p = p(r)$, $T = T(r)$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = R$ | $v_r = -V$ | suction through the porous surface |
| $r = R$ | $v_z = U$ | liquid in contact with the surface moves with the cylinder (no-slip) |
| $r \to \infty$ | $v_z \to 0$, $p \to p_\infty$, $T \to T_\infty$ | liquid at rest far away |
| $r = R$ | $T = T_c$ | uniform temperature of the cylinder |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity and the radial velocity

$$ \frac{1}{r}\frac{d(rv_r)}{dr} + \underbrace{\cancel{\frac{1}{r}\frac{\partial v_\theta}{\partial\theta}}}_{v_\theta = 0} + \underbrace{\cancel{\frac{\partial v_z}{\partial z}}}_{\partial_z = 0} = 0 \;\Longrightarrow\; r\,v_r = \text{const} = -RV \tag{1} $$

where the constant is fixed with $v_r(R) = -V$:

$$ \boxed{\,v_r(r) = -\frac{RV}{r}\,} \tag{2} $$

### 3.2 Radial momentum and the pressure

The viscous term of the $r$ component, $\mu\,\partial\left[r^{-1}\partial(rv_r)/\partial r\right]/\partial r$, is zero because $rv_r$ is constant (1); the terms in $v_\theta$ vanish. What is left is

$$ \rho\,v_r\frac{dv_r}{dr} = -\frac{dp}{dr} \;\Longrightarrow\; p + \frac{\rho v_r^2}{2} = \text{const} = p_\infty \tag{3} $$

(the constant is evaluated at infinity, where $v_r \to 0$):

$$ \boxed{\,p(r) = p_\infty - \frac{\rho R^2V^2}{2\,r^2}\,}, \qquad \frac{\partial p}{\partial z} = 0 \tag{4} $$

The pressure depends only on $r$, hence $\partial p/\partial z = 0$.

### 3.3 Axial momentum and the velocity profile

The $z$ component of (4.41) with $\partial/\partial z = 0$, $v_\theta = 0$, no gravity and $\partial p/\partial z = 0$:

$$ \rho\,v_r\frac{dv_z}{dr} = \mu\,\frac{1}{r}\frac{d}{dr}\left(r\frac{dv_z}{dr}\right) \tag{5} $$

Substituting $v_r = -RV/r$ and multiplying by $r/\mu$:

$$ -\frac{\rho RV}{\mu}\frac{dv_z}{dr} = \frac{d}{dr}\left(r\frac{dv_z}{dr}\right) \;\Longrightarrow\; \frac{d}{dr}\left(r\frac{dv_z}{dr}\right) + \mathrm{Re}\,\frac{dv_z}{dr} = 0 \tag{6} $$

Following the hint of the statement, try $v_z = r^\alpha$: then $r\,dv_z/dr = \alpha r^\alpha$, $\dfrac{d}{dr}(r\,dv_z/dr) = \alpha^2r^{\alpha-1}$ and $\mathrm{Re}\,dv_z/dr = \mathrm{Re}\,\alpha\,r^{\alpha-1}$. Substituting in (6) and dividing by $r^{\alpha-1}$:

$$ \alpha^2 + \mathrm{Re}\,\alpha = 0 \;\Longrightarrow\; \alpha = 0 \quad\text{or}\quad \alpha = -\mathrm{Re} \tag{7} $$

The two independent solutions are $r^0 = 1$ and $r^{-\mathrm{Re}}$, so $v_z = C_1 + C_2\,r^{-\mathrm{Re}}$. The condition $v_z \to 0$ for $r \to \infty$ requires $C_1 = 0$ (since $r^{-\mathrm{Re}} \to 0$ for $\mathrm{Re} > 0$), and $v_z(R) = U$ gives $C_2 = UR^{\mathrm{Re}}$:

$$ \boxed{\,v_z(r) = U\left(\frac{R}{r}\right)^{\mathrm{Re}}\,} \tag{8} $$

### 3.4 Force on the cylinder

The normal pointing into the liquid is $\bar{n} = +\bar{e}_r$, so $(-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot\bar{n}$ is the force per unit area that the liquid exerts on the cylinder. The pressure and $\tau'_{rr}$ act radially and integrate to zero around the circumference. The axial component is $\tau'_{rz} = \mu\left(\partial v_z/\partial r + \partial v_r/\partial z\right) = \mu\,dv_z/dr$. From (8), $dv_z/dr = -\mathrm{Re}\,U R^{\mathrm{Re}}r^{-\mathrm{Re}-1}$, so at $r = R$:

$$ \tau'_{rz}\Big|_R = -\mu\,\mathrm{Re}\,\frac{U}{R} = -\rho\,V\,U \tag{9} $$

The force per unit length (area $2\pi R$):

$$ \boxed{\,\bar{F} = 2\pi R\,\tau'_{rz}\Big|_R\,\bar{e}_z = -2\pi R\,\rho\,V\,U\,\bar{e}_z\,} \tag{10} $$

The liquid pulls the cylinder back, with the magnitude of the mass flow rate sucked in per unit length, $\dot{m} = 2\pi R\rho V$, times $U$: the cylinder must supply to the entrained liquid the axial momentum $U$ per unit mass, which is zero far away.

### 3.5 Trajectory of a fluid particle

The particle moves with the local velocity: $dr/dt = v_r = -RV/r$ and $dz/dt = v_z$. For the radial motion, separating variables, $r\,dr = -RV\,dt$ and integrating from $r_o$ at $t = 0$:

$$ \frac{r^2 - r_o^2}{2} = -RV\,t \;\Longrightarrow\; r(t) = \sqrt{r_o^2 - 2RV\,t}, \qquad t_s = \frac{r_o^2 - R^2}{2RV} \tag{11} $$

where $t_s$ is the time at which the particle reaches the surface ($r = R$). The axial coordinate follows from $dz/dr = v_z/v_r$:

$$ \frac{dz}{dr} = -\frac{U}{RV}\left(\frac{R}{r}\right)^{\mathrm{Re}}r = -\frac{UR^{\mathrm{Re}-1}}{V}\,r^{1-\mathrm{Re}} \tag{12} $$

Integrating from $r_o$ (where $z = 0$) to $r$ with $\int r^{1-\mathrm{Re}}dr = r^{2-\mathrm{Re}}/(2 - \mathrm{Re})$ for $\mathrm{Re} \neq 2$ and Barrow's rule:

$$ \boxed{\,z = \frac{UR}{V\,(2 - \mathrm{Re})}\left[\left(\frac{r_o}{R}\right)^{2-\mathrm{Re}} - \left(\frac{r}{R}\right)^{2-\mathrm{Re}}\right]\,} \qquad (\mathrm{Re} \neq 2) \tag{13} $$

and, for $\mathrm{Re} = 2$, the integral of $1/r$ gives $z = (UR/V)\ln(r_o/r)$. The particle moves towards the cylinder and is carried along $z$ by the entrained flow; the total axial distance travelled until it reaches the surface is (13) with $r = R$.

### 3.6 Temperature field

Neglecting the viscous dissipation, the energy equation (4.42) reads

$$ \rho c\,v_r\frac{dT}{dr} = k\,\frac{1}{r}\frac{d}{dr}\left(r\frac{dT}{dr}\right) \;\Longrightarrow\; -\rho c\frac{RV}{r}\frac{dT}{dr} = \frac{k}{r}\frac{d}{dr}\left(r\frac{dT}{dr}\right) \tag{14} $$

Multiplying by $r/k$ and using $\rho cRV/k = \dfrac{\rho VR}{\mu}\dfrac{\mu c}{k} = \mathrm{Pr}\,\mathrm{Re}$:

$$ \frac{d}{dr}\left(r\frac{dT}{dr}\right) + \mathrm{Pr}\,\mathrm{Re}\,\frac{dT}{dr} = 0 \tag{15} $$

This is the same ODE as (6) with $\mathrm{Re}$ replaced by $\mathrm{Pr}\,\mathrm{Re}$, so $T = B_1 + B_2\,r^{-\mathrm{Pr}\,\mathrm{Re}}$. The conditions $T(\infty) = T_\infty$ and $T(R) = T_c$ give $B_1 = T_\infty$ and $B_2 = (T_c - T_\infty)R^{\mathrm{Pr}\,\mathrm{Re}}$:

$$ \boxed{\,\frac{T - T_\infty}{T_c - T_\infty} = \left(\frac{R}{r}\right)^{\mathrm{Pr}\,\mathrm{Re}}\,} \tag{16} $$

### 3.7 Heat transferred to the cylinder

The heat flux from the liquid to the cylinder is $\bar{q}\cdot\bar{n}$ with $\bar{n} = -\bar{e}_r$ (out of the liquid): $q_c = k\,dT/dr\big|_R$. From (16), $dT/dr\big|_R = -\mathrm{Pr}\,\mathrm{Re}\,(T_c - T_\infty)/R = \mathrm{Pr}\,\mathrm{Re}\,(T_\infty - T_c)/R$. With $k\,\mathrm{Pr}\,\mathrm{Re}/R = \rho cV$ and the area $2\pi R$ per unit length:

$$ \boxed{\,\dot{Q} = 2\pi R\,\rho\,c\,V\,(T_\infty - T_c)\,} \tag{17} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The suction squeezes the momentum and thermal layers against the cylinder: the velocity decays as $r^{-\mathrm{Re}}$ and the temperature excess as $r^{-\mathrm{Pr}\,\mathrm{Re}}$, with the scales $R/\mathrm{Re}$ and $R/(\mathrm{Pr}\,\mathrm{Re})$ close to the wall for $\mathrm{Re} \gg 1$. The thermal layer is thinner than the viscous one when $\mathrm{Pr} > 1$.
- **Limits.** For $V \to 0$ ($\mathrm{Re} \to 0$) the exponent vanishes and (8) tends to the uniform velocity $U$, which does not decay at infinity: a steady solution that vanishes far away needs the suction. For $U = 0$ there is no axial motion, the force vanishes and (17) remains: the heat is carried by the entrained liquid.
- **Dimensional check.** $\mathrm{Re} = \rho VR/\mu$ is dimensionless: $(\mathrm{kg/m^3})(\mathrm{m/s})\,\mathrm{m}/(\mathrm{Pa\,s}) = 1$. $\rho VU$ in (9) has units $\mathrm{kg/(m^2\,s)}\cdot\mathrm{m/s} = \mathrm{N/m^2}$, and the force per unit length (10) has units N/m. In (17), $\rho cV\,\Delta T$ is W/m$^2$, times $2\pi R$: W/m.
- **Momentum check.** On a cylindrical surface of any radius $r$ the axial momentum flux is $2\pi r\,\rho v_rv_z = -2\pi\rho RV\,v_z(r)$ and the viscous force is $2\pi r\,\mu\,dv_z/dr = -2\pi\mu\,\mathrm{Re}\,v_z(r) = -2\pi\rho RV\,v_z(r)$, using $r\,dv_z/dr = -\mathrm{Re}\,v_z$ from (8): the two are equal at every $r$, and at $r = R$ the viscous force is (10).
