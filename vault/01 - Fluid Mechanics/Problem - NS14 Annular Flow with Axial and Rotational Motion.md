---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - flujo-anular
  - movimiento-helicoidal
  - disipacion-viscosa
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS14.pdf"
id: "ns14"
pill: "NS14: Annulus"
tags_html:
  - "Superposed axial and azimuthal flows"
  - "Pressure from centrifugal force"
  - "Helical pathline"
  - "Viscous heating"
---

# Problem NS14: Annular Flow with Axial and Rotational Motion

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

A liquid of density $\rho$, viscosity $\mu$, specific heat $c$, and thermal conductivity $k$ fills the annular gap formed between two concentric cylinders of radii $R_i$ and $R_o$, respectively. The inner cylinder moves with axial velocity $U$ while the outer cylinder rotates around its axis with angular velocity $\Omega$, inducing in the liquid an axially symmetric motion described in cylindrical coordinates by the velocity components $v_r(r)$, $v_z(r)$, and $v_\theta(r)$ with associated pressure distribution $p(r)$.

1. Obtain the radial velocity $v_r(r)$.

2. Calculate the axial velocity $v_z(r)$.

3. Determine the azimuthal velocity $v_\theta(r)$.

4. Compute the pressure distribution, giving the result in the form $p(r) - p_i$, where $p_i$ is the known pressure on the surface of the inner cylinder.

5. Give the trajectory of the fluid particle located initially at $r = r_o$, $\theta = \theta_o$, and $z = z_o$. Show schematically the resulting path line.

6. Obtain the temperature distribution in the liquid $T(r)$ knowing that the temperatures of the inner and outer cylinders are kept at constant values $T_i$ and $T_o$, respectively.

The sheet is headed "INTRODUCTION TO FLUID MECHANICS, PREFINAL (Dic 16, 2013)".

![[attachments/FM-T4/ns14-statement.png]]
*Statement figure (crop of NS14.pdf, p. 1): annular gap between the cylinders of radii $R_i$ and $R_o$, inner cylinder moving axially with $U$, outer cylinder rotating with $\Omega$, axes $r$, $z$*

Source: NS14.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 and energy Eq. 4.42 in cylindrical coordinates, viscous dissipation $\phi_v$ in cylindrical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, axisymmetric flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$) in the annulus, with the fields depending only on $r$: $\partial/\partial t = \partial/\partial\theta = \partial/\partial z = 0$.
- The walls are impermeable. The inner cylinder ($r = R_i$) moves axially with $U$ and does not rotate; the outer cylinder ($r = R_o$) is at rest axially and rotates with $\Omega$. No mass force enters the plane motion (gravity would shift the pressure by a hydrostatic term); no chemical reaction and no radiation.
- Data: $[\rho,\ \mu,\ c,\ k,\ R_i,\ R_o,\ U,\ \Omega,\ p_i,\ T_i,\ T_o,\ r_o,\ \theta_o,\ z_o]$. Unknowns: $v_r$, $v_z$, $v_\theta$, $p - p_i$, the pathline and $T(r)$.
- Notation: $L = \ln(R_o/R_i)$ and $a = \Omega R_o^2/(R_o^2 - R_i^2)$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R_i$, $R_o$ | inner and outer radii | m |
| $U$ | axial velocity of the inner cylinder | m/s |
| $\Omega$ | angular velocity of the outer cylinder | rad/s |
| $p_i$ | pressure on the inner cylinder | Pa |
| $T_i$, $T_o$ | temperatures of the inner and outer cylinders | K |
| $r_o$, $\theta_o$, $z_o$ | initial position of the fluid particle | m, rad, m |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cylindrical frame $(r,\theta,z)$ with $z$ along the axis in the direction of $U$; the basis $\{\bar{e}_r,\bar{e}_\theta,\bar{e}_z\}$ is orthonormal and right-handed.
- Field form: $\bar{v} = v_r(r)\,\bar{e}_r + v_\theta(r)\,\bar{e}_\theta + v_z(r)\,\bar{e}_z$, $p = p(r)$, $T = T(r)$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = R_i$ | $v_r = 0$, $v_\theta = 0$, $v_z = U$ | impermeable inner cylinder moving axially, not rotating |
| $r = R_o$ | $v_r = 0$, $v_\theta = \Omega R_o$, $v_z = 0$ | impermeable outer cylinder rotating |
| $r = R_i$ | $p = p_i$, $T = T_i$ | known pressure, inner temperature |
| $r = R_o$ | $T = T_o$ | outer temperature |

## Phase 3: Step-by-Step Derivation

### 3.1 Radial velocity (item 1)

$$ \frac{1}{r}\frac{d(rv_r)}{dr} + \underbrace{\cancel{\frac{1}{r}\frac{\partial v_\theta}{\partial\theta}}}_{\partial_\theta = 0} + \underbrace{\cancel{\frac{\partial v_z}{\partial z}}}_{\partial_z = 0} = 0 \;\Longrightarrow\; r\,v_r = \text{const} \tag{1} $$

The wall is impermeable, $v_r(R_i) = 0$, so the constant is zero:

$$ \boxed{\,v_r(r) = 0\,} \tag{2} $$

### 3.2 Axial velocity (item 2)

The $z$ component of (4.41), with $v_r = 0$, $\partial_z = \partial_\theta = 0$ and the pressure depending only on $r$ ($\partial p/\partial z = 0$), keeps the viscous term:

$$ 0 = \mu\,\frac{1}{r}\frac{d}{dr}\left(r\frac{dv_z}{dr}\right) \;\Longrightarrow\; r\frac{dv_z}{dr} = C \;\Longrightarrow\; v_z = C\ln r + D \tag{3} $$

The conditions $v_z(R_i) = U$ and $v_z(R_o) = 0$ give $C\ln(R_o/R_i) = -U$, that is $C = -U/L$, and then $D = U + (U/L)\ln R_i$:

$$ \boxed{\,v_z(r) = U\,\frac{\ln(R_o/r)}{\ln(R_o/R_i)}\,} \tag{4} $$

### 3.3 Azimuthal velocity (item 3)

The $\theta$ component of (4.41) with $v_r = 0$: $0 = \mu\,d\left[r^{-1}d(rv_\theta)/dr\right]/dr$. Integrating once, $r^{-1}d(rv_\theta)/dr = 2A$; multiplying by $r$ and integrating again, $rv_\theta = Ar^2 + B$:

$$ v_\theta = A\,r + \frac{B}{r} \tag{5} $$

The conditions $v_\theta(R_i) = 0$ and $v_\theta(R_o) = \Omega R_o$ give $AR_i^2 + B = 0$ and $AR_o^2 + B = \Omega R_o^2$, so $A = \Omega R_o^2/(R_o^2 - R_i^2) = a$ and $B = -aR_i^2$:

$$ \boxed{\,v_\theta(r) = \frac{\Omega R_o^2}{R_o^2 - R_i^2}\left(r - \frac{R_i^2}{r}\right) = a\left(r - \frac{R_i^2}{r}\right)\,} \tag{6} $$

### 3.4 Pressure (item 4)

The $r$ component of (4.41) with $v_r = 0$ keeps the centrifugal term:

$$ -\rho\frac{v_\theta^2}{r} = -\frac{dp}{dr} \;\Longrightarrow\; \frac{dp}{dr} = \rho\frac{v_\theta^2}{r} = \rho a^2\left(r - \frac{2R_i^2}{r} + \frac{R_i^4}{r^3}\right) \tag{7} $$

Integrating from $R_i$ to $r$ (antiderivatives $r^2/2$, $-2R_i^2\ln r$ and $-R_i^4/(2r^2)$) and using Barrow's rule:

$$ p - p_i = \rho a^2\left[\frac{r^2 - R_i^2}{2} - 2R_i^2\ln\frac{r}{R_i} - \frac{R_i^4}{2}\left(\frac{1}{r^2} - \frac{1}{R_i^2}\right)\right] $$

$$ \boxed{\,p(r) - p_i = \rho\,a^2R_i^2\left[\frac{1}{2}\left(\frac{r^2}{R_i^2} - \frac{R_i^2}{r^2}\right) - 2\ln\frac{r}{R_i}\right], \qquad a = \frac{\Omega R_o^2}{R_o^2 - R_i^2}\,} \tag{8} $$

### 3.5 Trajectory of a fluid particle (item 5)

The velocity of the particle is the local velocity: $dr/dt = v_r = 0$, $r\,d\theta/dt = v_\theta$ and $dz/dt = v_z$. Hence the particle stays at $r = r_o$, and with the angular and axial velocities of that radius, constant in time:

$$ \frac{d\theta}{dt} = \frac{v_\theta(r_o)}{r_o} = a\left(1 - \frac{R_i^2}{r_o^2}\right) = \frac{\Omega R_o^2\,(r_o^2 - R_i^2)}{r_o^2\,(R_o^2 - R_i^2)}, \qquad \frac{dz}{dt} = v_z(r_o) = U\,\frac{\ln(R_o/r_o)}{\ln(R_o/R_i)} \tag{9} $$

$$ \boxed{\,r = r_o, \quad \theta - \theta_o = \frac{\Omega R_o^2\,(r_o^2 - R_i^2)}{r_o^2\,(R_o^2 - R_i^2)}\,t, \quad z - z_o = U\,\frac{\ln(R_o/r_o)}{\ln(R_o/R_i)}\,t\,} \tag{10} $$

Eliminating $t$, the pathline is the **helix** of radius $r_o$ and constant pitch,

$$ z - z_o = \frac{U\ln(R_o/r_o)\;r_o^2\,(R_o^2 - R_i^2)}{\ln(R_o/R_i)\,\Omega R_o^2\,(r_o^2 - R_i^2)}\,(\theta - \theta_o) $$

that is, a spiral on the cylinder $r = r_o$ that advances in $z$ (in the direction of $U$) while turning in the direction of $\Omega$; the axial advance per turn is $2\pi\,v_z(r_o)\,r_o/v_\theta(r_o)$.

### 3.6 Temperature (item 6)

With $v_r = 0$ the convective terms vanish and (4.42) is $0 = \phi_v + k\,r^{-1}d(rdT/dr)/dr$. The non-zero deformation rates are $dv_z/dr$ and $r\,d(v_\theta/r)/dr$ (cylindrical $\phi_v$ of Notes.pdf):

$$ \phi_v = \mu\left[\left(\frac{dv_z}{dr}\right)^2 + \left(r\frac{d}{dr}\frac{v_\theta}{r}\right)^2\right] = \mu\left[\frac{U^2}{L^2r^2} + \frac{4a^2R_i^4}{r^4}\right] \tag{11} $$

since $dv_z/dr = -U/(Lr)$ and $v_\theta/r = a(1 - R_i^2/r^2)$ gives $r\,d(v_\theta/r)/dr = 2aR_i^2/r^2$. Multiplying the energy equation by $r/k$:

$$ \frac{d}{dr}\left(r\frac{dT}{dr}\right) = -\frac{\mu}{k}\left[\frac{U^2}{L^2r} + \frac{4a^2R_i^4}{r^3}\right] \tag{12} $$

Integrating once, $r\,dT/dr = -\dfrac{\mu}{k}\left[\dfrac{U^2\ln r}{L^2} - \dfrac{2a^2R_i^4}{r^2}\right] + D_1$; dividing by $r$ and integrating again, with $\int\ln r\,dr/r = \tfrac{1}{2}\ln^2r$ and $\int r^{-3}dr = -1/(2r^2)$:

$$ T = -\frac{\mu}{k}\left[\frac{U^2\ln^2r}{2L^2} + \frac{a^2R_i^4}{r^2}\right] + D_1\ln r + D_2 \tag{13} $$

With the variable $x = \ln(r/R_i)$ (the linear terms in $x$ are absorbed in $D_1$ and the constants in $D_2$) the conditions $T = T_i$ at $x = 0$ and $T = T_o$ at $x = L$ fix the constants. The result is

$$ \boxed{\,T(r) = T_i + (T_o - T_i)\frac{x}{L} + \frac{\mu}{k}\left\{\frac{U^2}{2}\frac{x}{L}\left(1 - \frac{x}{L}\right) + a^2R_i^2\left[1 - \frac{R_i^2}{r^2} - \frac{x}{L}\left(1 - \frac{R_i^2}{R_o^2}\right)\right]\right\}, \quad x = \ln\frac{r}{R_i}\,} \tag{14} $$

Each viscous-heating term vanishes at both walls ($x = 0$ and $x = L$), so the boundary temperatures are $T_i$ and $T_o$; for $r = R_o$, $1 - R_i^2/R_o^2 - (1 - R_i^2/R_o^2) = 0$.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** Two independent shear flows are superposed: an axial one (logarithmic, from the inner cylinder's motion) and an azimuthal one (rigid rotation plus an irrotational vortex, from the outer cylinder's rotation). They do not interact in the velocity field because there is no radial velocity; they interact only through the pressure (centrifugal force of the azimuthal flow, (8)) and through the heating (sum of two dissipations in (11)).
- **Limits.** For $\Omega = 0$ ($a = 0$): axial flow only, pressure uniform, helix reduced to a straight line. For $U = 0$: pure rotation, and the pathlines are circles. For $R_i \to 0$ the azimuthal flow becomes rigid rotation, $v_\theta = \Omega r$. With the viscous heating neglected, (14) reduces to the logarithmic conduction profile $T_i + (T_o - T_i)\,x/L$.
- **Dimensional check.** $a$ has units 1/s and $a(r - R_i^2/r)$ has units m/s. $\rho a^2R_i^2$ has units $(\mathrm{kg/m^3})(\mathrm{m/s})^2 = \mathrm{Pa}$. $\mu U^2/k$ has units $\mathrm{K}$ and $\mu a^2R_i^2/k$ also $\mathrm{K}$.
- **Check of the pressure.** Differentiating (8): $dp/dr = \rho a^2R_i^2\left[\tfrac{r}{R_i^2} + \tfrac{R_i^2}{r^3} - \tfrac{2}{r}\right] = \rho a^2\left(r - \tfrac{2R_i^2}{r} + \tfrac{R_i^4}{r^3}\right)$, which is (7).
