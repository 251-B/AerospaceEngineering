---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - cilindros-porosos
  - rotacion
  - flujo-radial
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS13.pdf"
id: "ns13"
pill: "NS13: Porous cylinders"
tags_html:
  - "Radial throughflow"
  - "Power-law azimuthal velocity"
  - "Pressure difference"
  - "Temperature profile"
---

# Problem NS13: Porous Rotating Cylinders with Radial Flow

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

A liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$, and specific heat $c$ occupies the gap formed between two porous coaxial cylinders of radius $R_i$ and $R_o$ that are rotating with angular velocities $\Omega_i$ and $\Omega_o$, respectively. The liquid is injected through the surface of the inner cylinder with normal velocity component $v_r = V_i$ and is removed through the outer surface. The temperatures on the inner and outer surfaces are $T_i$ and $T_o$, respectively. The resulting steady, planar, axially symmetric flow field is described in terms of $v_r(r)$, $v_\theta(r)$, $p(r)$, and $T(r)$.

1. Determine the radial velocity component $v_r(r)$. Obtain in particular its value on the surface of the outer cylinder $v_r(R_o)$.

2. Obtain the azimuthal velocity component $v_\theta(r)$. To that end, write the $\theta$-component of the momentum equation in terms of the parameter $\mathrm{Re} = \rho V_iR_i/\mu$ and look for solutions of the form $v_\theta \propto r^\alpha$, demonstrating that the general solution can be expressed as $v_\theta = C_1/r + C_2\,r^{\mathrm{Re}+1}$. Obtain the values of the integration constants $C_1$ and $C_2$.

3. Calculate $p(r) - p_i$, the difference of the pressure $p(r)$ from its inner-surface value $p_i = p(R_i)$.

4. Write the equation that determines the temperature distribution $T(r)$, including the appropriate boundary conditions. Solve the problem assuming that the effect of viscous dissipation is negligibly small.

The sheet is headed "INTRODUCTION TO FLUID MECHANICS, MIDTERM (Nov 11, 2013)".

![[attachments/FM-T4/ns13-statement.png]]
*Statement figure (crop of NS13.pdf, p. 1): porous cylinders of radii $R_i$ and $R_o$ rotating with $\Omega_i$ and $\Omega_o$, injection velocity $V_i$ through the inner surface, polar coordinates $r$, $\theta$*

Source: NS13.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 and energy Eq. 4.42 in cylindrical coordinates, viscous dissipation $\phi_v$ in cylindrical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, planar ($\partial/\partial z = 0$, $v_z = 0$), axisymmetric ($\partial/\partial\theta = 0$) flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$) between two porous cylinders: $\bar{v} = v_r(r)\,\bar{e}_r + v_\theta(r)\,\bar{e}_\theta$, $p = p(r)$, $T = T(r)$.
- No mass force enters the plane of motion; no chemical reaction and no radiation.
- The inner cylinder ($r = R_i$) injects the liquid with $v_r = V_i > 0$ and the outer one removes it; both rotate rigidly with their angular velocities (no-slip).
- Data: $[\rho,\ \mu,\ k,\ c,\ R_i,\ R_o,\ \Omega_i,\ \Omega_o,\ V_i,\ T_i,\ T_o,\ p_i]$. Unknowns: $v_r$, $v_\theta$, $p - p_i$, $T$.
- Dimensionless numbers: $\mathrm{Re} = \rho V_iR_i/\mu$ and $\mathrm{Pr} = \mu c/k$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R_i$, $R_o$ | inner and outer radii | m |
| $\Omega_i$, $\Omega_o$ | angular velocities of the cylinders | rad/s |
| $V_i$ | injection velocity at the inner surface | m/s |
| $T_i$, $T_o$ | surface temperatures | K |
| $\mathrm{Re}$, $\mathrm{Pr}$ | injection Reynolds number, Prandtl number | 1 |
| $C_1$, $C_2$ | integration constants of $v_\theta$ | m$^2$/s, 1/s$\,\cdot\,$m$^{-\mathrm{Re}}$ |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cylindrical frame $(r,\theta,z)$ centred on the common axis, with the orthonormal right-handed basis $\{\bar{e}_r,\bar{e}_\theta,\bar{e}_z\}$ fixed to the laboratory (inertial).
- Field form: $\bar{v} = v_r(r)\,\bar{e}_r + v_\theta(r)\,\bar{e}_\theta$, $p = p(r)$, $T = T(r)$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = R_i$ | $v_r = V_i$, $v_\theta = \Omega_iR_i$ | injection through the inner surface, no-slip |
| $r = R_o$ | $v_\theta = \Omega_oR_o$ | no-slip on the outer cylinder |
| $r = R_i$ | $p = p_i$, $T = T_i$ | reference pressure, inner temperature |
| $r = R_o$ | $T = T_o$ | outer temperature |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity (item 1)

$$ \frac{1}{r}\frac{d(rv_r)}{dr} + \underbrace{\cancel{\frac{1}{r}\frac{\partial v_\theta}{\partial\theta}}}_{\partial_\theta = 0} + \underbrace{\cancel{\frac{\partial v_z}{\partial z}}}_{v_z = 0} = 0 \;\Longrightarrow\; r\,v_r = \text{const} = R_iV_i \tag{1} $$

where the constant is fixed with $v_r(R_i) = V_i$:

$$ \boxed{\,v_r(r) = \frac{R_iV_i}{r}, \qquad v_r(R_o) = \frac{R_iV_i}{R_o}\,} \tag{2} $$

### 3.2 Azimuthal momentum (item 2)

The $\theta$ component of (4.41) with $\partial_t = \partial_\theta = \partial_z = 0$, no mass force and $\partial p/\partial\theta = 0$:

$$ \rho\left(v_r\frac{dv_\theta}{dr} + \frac{v_rv_\theta}{r}\right) = \mu\frac{d}{dr}\left[\frac{1}{r}\frac{d(rv_\theta)}{dr}\right] \tag{3} $$

The left side is $\rho v_r\,\dfrac{1}{r}\dfrac{d(rv_\theta)}{dr}$, since $dv_\theta/dr + v_\theta/r = r^{-1}d(rv_\theta)/dr$. With $v_r = R_iV_i/r$ and $\mathrm{Re} = \rho V_iR_i/\mu$:

$$ \frac{d}{dr}\left[\frac{1}{r}\frac{d(rv_\theta)}{dr}\right] - \mathrm{Re}\,\frac{1}{r}\left(\frac{dv_\theta}{dr} + \frac{v_\theta}{r}\right) = 0 \tag{4} $$

Try $v_\theta = r^\alpha$: $d(rv_\theta)/dr = (\alpha + 1)r^\alpha$, so $r^{-1}d(rv_\theta)/dr = (\alpha + 1)r^{\alpha-1}$ and its derivative is $(\alpha + 1)(\alpha - 1)r^{\alpha-2}$; the second term of (4) is $\mathrm{Re}\,(\alpha + 1)r^{\alpha-2}$. Substituting and dividing by $r^{\alpha-2}$:

$$ (\alpha + 1)(\alpha - 1 - \mathrm{Re}) = 0 \;\Longrightarrow\; \alpha = -1 \quad\text{or}\quad \alpha = \mathrm{Re} + 1 \tag{5} $$

The general solution is therefore

$$ v_\theta = \frac{C_1}{r} + C_2\,r^{\mathrm{Re}+1} \tag{6} $$

The boundary conditions $v_\theta(R_i) = \Omega_iR_i$ and $v_\theta(R_o) = \Omega_oR_o$, each multiplied by $R_i$ and $R_o$ respectively, give

$$ C_1 + C_2R_i^{\mathrm{Re}+2} = \Omega_iR_i^2, \qquad C_1 + C_2R_o^{\mathrm{Re}+2} = \Omega_oR_o^2 \tag{7} $$

Subtracting, $C_2\left(R_o^{\mathrm{Re}+2} - R_i^{\mathrm{Re}+2}\right) = \Omega_oR_o^2 - \Omega_iR_i^2$, and then $C_1 = \Omega_iR_i^2 - C_2R_i^{\mathrm{Re}+2}$:

$$ \boxed{\,C_1 = \frac{R_i^2R_o^2\left(\Omega_iR_o^{\mathrm{Re}} - \Omega_oR_i^{\mathrm{Re}}\right)}{R_o^{\mathrm{Re}+2} - R_i^{\mathrm{Re}+2}}, \qquad C_2 = \frac{\Omega_oR_o^2 - \Omega_iR_i^2}{R_o^{\mathrm{Re}+2} - R_i^{\mathrm{Re}+2}}\,} \tag{8} $$

### 3.3 Pressure difference (item 3)

The $r$ component of (4.41): the viscous term $\mu\,d[r^{-1}d(rv_r)/dr]/dr$ is zero by (1), so

$$ \rho\left(v_r\frac{dv_r}{dr} - \frac{v_\theta^2}{r}\right) = -\frac{dp}{dr} \;\Longrightarrow\; \frac{dp}{dr} = \rho\left[\frac{v_\theta^2}{r} + \frac{(R_iV_i)^2}{r^3}\right] \tag{9} $$

since $v_r\,dv_r/dr = (R_iV_i/r)(-R_iV_i/r^2) = -(R_iV_i)^2/r^3$. Squaring (6), $v_\theta^2/r = C_1^2r^{-3} + 2C_1C_2r^{\mathrm{Re}-1} + C_2^2r^{2\mathrm{Re}+1}$. Integrating from $R_i$ to $r$ (antiderivatives $-C_1^2/(2r^2)$, $2C_1C_2r^{\mathrm{Re}}/\mathrm{Re}$, $C_2^2r^{2\mathrm{Re}+2}/(2\mathrm{Re}+2)$ and $-(R_iV_i)^2/(2r^2)$) and using Barrow's rule:

$$ \boxed{\,\frac{p(r) - p_i}{\rho} = \frac{C_1^2 + (R_iV_i)^2}{2}\left(\frac{1}{R_i^2} - \frac{1}{r^2}\right) + \frac{2C_1C_2}{\mathrm{Re}}\left(r^{\mathrm{Re}} - R_i^{\mathrm{Re}}\right) + \frac{C_2^2}{2(\mathrm{Re} + 1)}\left(r^{2\mathrm{Re}+2} - R_i^{2\mathrm{Re}+2}\right)\,} \tag{10} $$

(for $\mathrm{Re} \neq 0$; for $\mathrm{Re} = 0$ the second term is $2C_1C_2\ln(r/R_i)$).

### 3.4 Temperature (item 4)

The energy equation (4.42) with $v_r = R_iV_i/r$ and the dissipation $\phi_v$ of the cylindrical expression (Notes.pdf) with $v_z = 0$, and the boundary conditions:

$$ \rho c\,v_r\frac{dT}{dr} = \phi_v + \frac{k}{r}\frac{d}{dr}\left(r\frac{dT}{dr}\right), \quad \phi_v = \mu\left\{2\left[\left(\frac{dv_r}{dr}\right)^2 + \left(\frac{v_r}{r}\right)^2\right] + \left[r\frac{d}{dr}\left(\frac{v_\theta}{r}\right)\right]^2\right\}, \quad T(R_i) = T_i,\ T(R_o) = T_o \tag{11} $$

Neglecting $\phi_v$ and multiplying by $r/k$, with $\rho cR_iV_i/k = \mathrm{Pr}\,\mathrm{Re}$:

$$ \frac{d}{dr}\left(r\frac{dT}{dr}\right) - \mathrm{Pr}\,\mathrm{Re}\,\frac{dT}{dr} = 0 \tag{12} $$

Try $T = r^\beta$: $\beta^2 - \mathrm{Pr}\,\mathrm{Re}\,\beta = 0$, so $\beta = 0$ or $\beta = \mathrm{Pr}\,\mathrm{Re}$ and $T = B_1 + B_2\,r^{\mathrm{Pr}\,\mathrm{Re}}$. The conditions $T(R_i) = T_i$ and $T(R_o) = T_o$ give $B_2\left(R_o^{\mathrm{Pr}\,\mathrm{Re}} - R_i^{\mathrm{Pr}\,\mathrm{Re}}\right) = T_o - T_i$:

$$ \boxed{\,T(r) = T_i + (T_o - T_i)\,\frac{r^{\mathrm{Pr}\,\mathrm{Re}} - R_i^{\mathrm{Pr}\,\mathrm{Re}}}{R_o^{\mathrm{Pr}\,\mathrm{Re}} - R_i^{\mathrm{Pr}\,\mathrm{Re}}}\,} \tag{13} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The radial throughflow convects angular momentum and heat outwards: the term $C_2\,r^{\mathrm{Re}+1}$ is the contribution of the convection (it grows with $r$), and $C_1/r$ is the viscous irrotational part. For $\mathrm{Re} \to 0$ (no injection) the solution reduces to the Couette profile between rotating cylinders, $v_\theta = C_1/r + C_2\,r$ with $C_1 = R_i^2R_o^2(\Omega_i - \Omega_o)/(R_o^2 - R_i^2)$ and $C_2 = (\Omega_oR_o^2 - \Omega_iR_i^2)/(R_o^2 - R_i^2)$, as in problem NS2 (with the roles of the two constants exchanged).
- **Limits.** For $\Omega_i = \Omega_o = 0$: $C_1 = C_2 = 0$, $v_\theta = 0$ and the pressure (10) is $\rho(R_iV_i)^2(1/R_i^2 - 1/r^2)/2$, the Bernoulli drop of the radial flow. For $\mathrm{Pr}\,\mathrm{Re} \to 0$, $r^{\mathrm{Pr}\,\mathrm{Re}} \simeq 1 + \mathrm{Pr}\,\mathrm{Re}\,\ln r$ and (13) tends to the pure conduction profile $T = T_i + (T_o - T_i)\ln(r/R_i)/\ln(R_o/R_i)$.
- **Dimensional check.** $R_iV_i/r$ is a velocity. $C_1$ has units m$^2$/s and $C_2\,r^{\mathrm{Re}+1}$ has units m/s. In (10) every term has units of $\rho\,\mathrm{(m/s)^2}$, that is Pa. $\mathrm{Pr}\,\mathrm{Re}$ is dimensionless, so the argument of (13) is dimensionless.
- **Boundary check.** From (6)-(8), $v_\theta(R_i) = \Omega_iR_i$ and $v_\theta(R_o) = \Omega_oR_o$; from (13), $T(R_i) = T_i$ and $T(R_o) = T_o$.
