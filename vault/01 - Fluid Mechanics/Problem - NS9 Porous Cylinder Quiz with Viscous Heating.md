---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - cilindro-poroso
  - disipacion-viscosa
  - succion
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS9.pdf"
id: "ns9"
pill: "NS9: Quiz 2012"
tags_html:
  - "Axisymmetric flow"
  - "Suction Reynolds number"
  - "Viscous heating"
  - "Blowing: no steady solution"
---

# Problem NS9: Porous Cylinder Quiz with Viscous Heating

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

Consider the steady buoyancy-free motion of a perfect liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$, and specific heat $c$, induced by an infinitely long porous cylinder of radius $R$ that moves with a constant velocity $U_w$ parallel to its axis, while a constant flow rate $q = 2\pi RV_w$ per unit length is uniformly sucked in the radial direction through the porous wall of the cylinder. Far from the cylinder, $r \to \infty$, the fluid is at rest, at pressure $p_\infty$ and temperature $T_\infty$.

To solve the problem, use a cylindrical coordinate system $(r, \theta, z)$, where $z$ is the axis of the cylinder, and assume that the velocity field is axisymmetric, $\partial\bar{v}/\partial\theta = 0$, as well as fully developed, $\partial\bar{v}/\partial z = 0$, thus $\bar{v} = v_r(r)\bar{e}_r + v_z(r)\bar{e}_z$.

1. Using continuity, determine the velocity component $v_r(r)$. (1 point)

2. Obtain the pressure field $p(r, z)$ by integration of the $r$-momentum equation, demonstrating in particular that $\partial p/\partial z = 0$. (2 points)

3. Using the $z$-momentum equation, obtain the axial velocity distribution, $v_z(r)$. (2 points)

4. Compute the trajectory of a particle initially placed at $r = R_i > R$ and $z = z_i$, as well as the corresponding sucking time, $t_s$. (1 point)

5. Calculate the force per unit length that the liquid exerts on the cylinder. (1 point)

6. Write the differential equation that determines the temperature in the liquid $T(r)$. Obtain the function $T(r)$, assuming that the wall is at constant uniform temperature $T_w$. (2 points)

7. Obtain the conductive heat flux per unit length from the liquid to the wall $q_w$. (1 point)

8. Show that there is no steady solution if fluid is blown through the wall, instead of being sucked. (1 extra point)

The sheet is headed "INTRODUCTION TO FLUID MECHANICS, QUIZ # 2 (Nov 26, 2012)" and carries no figure.

Source: NS9.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 and energy Eq. 4.42 in cylindrical coordinates, viscous dissipation $\phi_v$ and stress components in cylindrical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, buoyancy-free flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$) around an infinitely long cylinder: the fields depend only on $r$ ($\partial/\partial\theta = \partial/\partial z = \partial/\partial t = 0$) and $v_\theta = 0$. No chemical reaction and no radiation.
- The wall is porous: it sucks in the volume flow $q = 2\pi RV_w$ per unit length, uniformly, so $v_r(R) = -V_w$ with $V_w > 0$, and it moves axially with $U_w$.
- Far from the cylinder the liquid is at rest at $p_\infty$ and $T_\infty$.
- Data: $[\rho,\ \mu,\ k,\ c,\ R,\ U_w,\ V_w,\ p_\infty,\ T_\infty,\ T_w,\ R_i,\ z_i]$. Unknowns: $v_r$, $p$, $v_z$, the trajectory and $t_s$, the force, $T(r)$ and $q_w$.
- Dimensionless numbers: the suction Reynolds number $\mathrm{Re} = \rho V_wR/\mu = \rho q/(2\pi\mu)$, the Prandtl number $\mathrm{Pr} = \mu c/k$ and the product $\Pi = \mathrm{Pr}\,\mathrm{Re} = \rho cV_wR/k$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R$ | cylinder radius | m |
| $U_w$, $V_w$ | axial velocity of the cylinder, suction velocity | m/s |
| $q = 2\pi RV_w$ | suction flow rate per unit length | m$^2$/s |
| $\mathrm{Re}$, $\mathrm{Pr}$, $\Pi$ | suction Reynolds number, Prandtl number, their product | 1 |
| $T_w$, $T_\infty$ | wall and ambient temperatures | K |
| $R_i$, $z_i$ | initial radial and axial position of the particle | m |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cylindrical frame $(r,\theta,z)$ with $z$ along the axis of the cylinder; the basis $\{\bar{e}_r,\bar{e}_\theta,\bar{e}_z\}$ is orthonormal and right-handed. The liquid occupies $r > R$.
- Field form: $\bar{v} = v_r(r)\,\bar{e}_r + v_z(r)\,\bar{e}_z$, $p = p(r,z)$ until determined, $T = T(r)$.

![[attachments/FM-T4/ns9-setup.svg]]
*Setup of NS9 (drawn for the solution): porous cylinder of radius $R$ at temperature $T_w$ moving with $U_w$ along $z$, suction velocity $V_w$ ($q = 2\pi R V_w$ per unit length), fluid at rest at $p_\infty$, $T_\infty$ far away, axes $r$, $z$*

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = R$ | $v_r = -V_w$ | uniform suction through the porous wall |
| $r = R$ | $v_z = U_w$ | no-slip on the moving cylinder |
| $r \to \infty$ | $v_z \to 0$, $p \to p_\infty$, $T \to T_\infty$ | fluid at rest far away |
| $r = R$ | $T = T_w$ | uniform wall temperature |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity (item 1)

$$ \frac{1}{r}\frac{d(rv_r)}{dr} + \underbrace{\cancel{\frac{1}{r}\frac{\partial v_\theta}{\partial\theta}}}_{v_\theta = 0} + \underbrace{\cancel{\frac{\partial v_z}{\partial z}}}_{\partial_z = 0} = 0 \;\Longrightarrow\; r\,v_r = \text{const} = -RV_w \;\Longrightarrow\; \boxed{\,v_r(r) = -\frac{RV_w}{r} = -\frac{q}{2\pi r}\,} \tag{1} $$

### 3.2 Radial momentum and the pressure (item 2)

The viscous term of the $r$ component vanishes because $rv_r$ is constant, and the $\theta$ and $z$ terms are zero:

$$ \rho\,v_r\frac{dv_r}{dr} = -\frac{\partial p}{\partial r} \;\Longrightarrow\; p + \frac{\rho v_r^2}{2} = f(z) \tag{2} $$

where integration at fixed $z$ leaves a function of $z$. The condition $p \to p_\infty$ for $r \to \infty$ (where $v_r \to 0$) holds for every $z$, so $f(z) = p_\infty$ is a constant:

$$ \boxed{\,p(r) = p_\infty - \frac{\rho R^2V_w^2}{2r^2}\,}, \qquad \frac{\partial p}{\partial z} = 0 \tag{3} $$

### 3.3 Axial momentum (item 3)

The $z$ component of (4.41), with $\partial_z = 0$, $v_\theta = 0$, no mass force and $\partial p/\partial z = 0$, is $\rho v_r\,dv_z/dr = \mu\,r^{-1}d(r\,dv_z/dr)/dr$. Substituting (1) and multiplying by $r/\mu$:

$$ \frac{d}{dr}\left(r\frac{dv_z}{dr}\right) + \mathrm{Re}\,\frac{dv_z}{dr} = 0 \tag{4} $$

Try $v_z = r^\alpha$: $\alpha^2 + \mathrm{Re}\,\alpha = 0$, so $\alpha = 0$ or $\alpha = -\mathrm{Re}$ and $v_z = C_1 + C_2r^{-\mathrm{Re}}$. The condition at infinity gives $C_1 = 0$ and $v_z(R) = U_w$ gives $C_2 = U_wR^{\mathrm{Re}}$:

$$ \boxed{\,v_z(r) = U_w\left(\frac{R}{r}\right)^{\mathrm{Re}}\,} \tag{5} $$

### 3.4 Trajectory and sucking time (item 4)

The velocity of the particle is the local velocity. Radial motion: $dr/dt = -RV_w/r$, so $r\,dr = -RV_w\,dt$; integrating from $R_i$ at $t = 0$, $(r^2 - R_i^2)/2 = -RV_wt$:

$$ r(t) = \sqrt{R_i^2 - 2RV_wt}, \qquad \boxed{\,t_s = \frac{R_i^2 - R^2}{2RV_w}\,} \tag{6} $$

Axial motion: $dz/dr = v_z/v_r = -\dfrac{U_wR^{\mathrm{Re}-1}}{V_w}r^{1-\mathrm{Re}}$. Integrating from $R_i$ (where $z = z_i$), with $\int r^{1-\mathrm{Re}}dr = r^{2-\mathrm{Re}}/(2 - \mathrm{Re})$ for $\mathrm{Re} \neq 2$:

$$ \boxed{\,z(r) = z_i + \frac{U_wR}{V_w\,(2 - \mathrm{Re})}\left[\left(\frac{R_i}{R}\right)^{2-\mathrm{Re}} - \left(\frac{r}{R}\right)^{2-\mathrm{Re}}\right]\,} \qquad (\mathrm{Re} \neq 2) \tag{7} $$

For $\mathrm{Re} = 2$, $z = z_i + (U_wR/V_w)\ln(R_i/r)$. The axial position at which the particle is sucked is (7) with $r = R$.

### 3.5 Force on the cylinder (item 5)

The normal pointing into the liquid is $\bar{n} = +\bar{e}_r$; the pressure and the radial normal stress act radially and integrate to zero around the circumference. The axial shear stress is $\tau'_{rz} = \mu\,dv_z/dr$, and from (5), $dv_z/dr\big|_R = -\mathrm{Re}\,U_w/R$:

$$ \tau'_{rz}\Big|_R = -\mu\,\mathrm{Re}\,\frac{U_w}{R} = -\rho V_wU_w, \qquad \boxed{\,\bar{F} = 2\pi R\,\tau'_{rz}\Big|_R\,\bar{e}_z = -\rho\,q\,U_w\,\bar{e}_z\,} \tag{8} $$

The force per unit length equals minus the axial momentum given per unit time to the sucked liquid, $\rho q\,U_w$.

### 3.6 Temperature: the equation (item 6)

The energy equation (4.42) with $v_r = -RV_w/r$, $\partial_z = \partial_\theta = 0$ and the dissipation of the cylindrical expression (Notes.pdf) keeping the non-zero terms, $\phi_v = \mu\left\{2\left[(dv_r/dr)^2 + (v_r/r)^2\right] + (dv_z/dr)^2\right\}$:

$$ \rho c\,v_r\frac{dT}{dr} = \phi_v + \frac{k}{r}\frac{d}{dr}\left(r\frac{dT}{dr}\right), \qquad \phi_v = \mu\left[\frac{4R^2V_w^2}{r^4} + \frac{\mathrm{Re}^2U_w^2}{r^2}\left(\frac{R}{r}\right)^{2\mathrm{Re}}\right] \tag{9} $$

since $dv_r/dr = RV_w/r^2$ and $v_r/r = -RV_w/r^2$. Multiplying by $r/k$ and using $\rho cRV_w/k = \Pi$:

$$ \frac{d}{dr}\left(r\frac{dT}{dr}\right) + \Pi\,\frac{dT}{dr} = -\frac{\mu}{k}\left[\frac{4R^2V_w^2}{r^3} + \frac{\mathrm{Re}^2U_w^2R^{2\mathrm{Re}}}{r^{2\mathrm{Re}+1}}\right] \tag{10} $$

with the boundary conditions $T(R) = T_w$ and $T(\infty) = T_\infty$.

### 3.7 Temperature: the solution (item 6)

Write $y = dT/dr$, so that (10) is $r\,y' + (1 + \Pi)\,y = -S_1r^{-3} - S_2r^{-2\mathrm{Re}-1}$ with $S_1 = 4\mu R^2V_w^2/k$ and $S_2 = \mu\,\mathrm{Re}^2U_w^2R^{2\mathrm{Re}}/k$. The homogeneous solution is $y = D\,r^{-1-\Pi}$ (substitute $r^{s}$: $s + 1 + \Pi = 0$). For each source term try a power of the same form: $y = A_1r^{-3}$ gives $r\,y' = -3A_1r^{-3}$ and $(\Pi - 2)A_1 = -S_1$; $y = A_2r^{-2\mathrm{Re}-1}$ gives $(\Pi - 2\mathrm{Re})A_2 = -S_2$. Hence, for $\Pi \neq 2$ and $\mathrm{Pr} \neq 2$,

$$ A_1 = \frac{S_1}{2 - \Pi}, \qquad A_2 = \frac{S_2}{\mathrm{Re}\,(2 - \mathrm{Pr})} $$

Integrating $y$ ($\int r^{-n}dr = -r^{1-n}/(n-1)$) and writing $\mu/k = \mathrm{Pr}/c$:

$$ T(r) = B - a_1\left(\frac{R}{r}\right)^2 - a_2\left(\frac{R}{r}\right)^{2\mathrm{Re}} + E\left(\frac{R}{r}\right)^{\Pi}, \qquad a_1 = \frac{2\,\mathrm{Pr}\,V_w^2}{c\,(2 - \Pi)}, \quad a_2 = \frac{\mathrm{Pr}\,U_w^2}{2c\,(2 - \mathrm{Pr})} \tag{11} $$

For $r \to \infty$ every power of $R/r$ vanishes, so $T(\infty) = T_\infty$ gives $B = T_\infty$; $T(R) = T_w$ gives $E = T_w - T_\infty + a_1 + a_2$:

$$ \boxed{\,T(r) = T_\infty - a_1\left(\frac{R}{r}\right)^2 - a_2\left(\frac{R}{r}\right)^{2\mathrm{Re}} + \left(T_w - T_\infty + a_1 + a_2\right)\left(\frac{R}{r}\right)^{\Pi}\,} \tag{12} $$

The terms $a_1$ and $a_2$ are the viscous heating by the radial and by the axial deformation. The cases $\Pi = 2$ and $\mathrm{Pr} = 2$ (resonance of the exponents) give logarithmic terms and are not worked out here.

### 3.8 Heat flux to the wall (item 7)

The heat flux from the liquid to the wall is $\bar{q}\cdot\bar{n}$ with $\bar{n} = -\bar{e}_r$: $k\,dT/dr\big|_R$. Differentiating (12) and setting $r = R$:

$$ \frac{dT}{dr}\Big|_R = \frac{1}{R}\left[2a_1 + 2\mathrm{Re}\,a_2 - \Pi\left(T_w - T_\infty + a_1 + a_2\right)\right] = \frac{1}{R}\left[\Pi\,(T_\infty - T_w) + (2 - \Pi)a_1 + (2\mathrm{Re} - \Pi)a_2\right] $$

with $(2 - \Pi)a_1 = 2\mathrm{Pr}\,V_w^2/c$ and $(2\mathrm{Re} - \Pi)a_2 = \mathrm{Re}(2 - \mathrm{Pr})a_2 = \mathrm{Pr}\,\mathrm{Re}\,U_w^2/(2c)$. Multiplying by $k$ and using $k\,\Pi/R = \rho cV_w$, $k\,\mathrm{Pr}/c = \mu$ and $\mu\,\mathrm{Re}/R = \rho V_w$:

$$ k\frac{dT}{dr}\Big|_R = \rho cV_w\,(T_\infty - T_w) + \frac{2\mu V_w^2}{R} + \frac{\rho V_wU_w^2}{2} $$

and, multiplying by the area per unit length $2\pi R$,

$$ \boxed{\,q_w = 2\pi R\rho V_w\left[c\,(T_\infty - T_w) + \frac{U_w^2}{2}\right] + 4\pi\mu V_w^2\,} \tag{13} $$

### 3.9 Blowing instead of suction (item 8)

If the liquid is blown, $V_w < 0$ and $\mathrm{Re} < 0$. Continuity still gives $v_r = -RV_w/r = R\lvert V_w\rvert/r > 0$, and the equation for $v_z$ is (4) with $\mathrm{Re} < 0$: $v_z = C_1 + C_2\,r^{\lvert\mathrm{Re}\rvert}$. The condition $v_z \to 0$ for $r \to \infty$ requires $C_2 = 0$ (the power grows) and then $C_1 = 0$, so $v_z(R) = U_w$ cannot be satisfied unless $U_w = 0$. Likewise $T = B + D\,r^{-\Pi}$ with $\Pi < 0$ is unbounded unless $D = 0$, which cannot satisfy $T(R) = T_w \neq T_\infty$. Therefore there is no steady solution with the fluid at rest and at $T_\infty$ far away: the blown liquid carries momentum and heat outward and they cannot be balanced by diffusion towards the cylinder.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** Suction confines the axial momentum to a layer of thickness of order $R/\mathrm{Re}$ and the thermal layer to $R/\Pi$: the thermal layer is thinner than the momentum layer when $\mathrm{Pr} > 1$. The cylinder pays for the entrained momentum with the force (8), and the wall receives the enthalpy, kinetic-energy and viscous-heating terms of (13).
- **Limits.** For $U_w = 0$, $a_2 = 0$ and $E$ contains only $a_1$; for negligible dissipation ($a_1 = a_2 = 0$) the solution is $T = T_\infty + (T_w - T_\infty)(R/r)^{\Pi}$ and $q_w = 2\pi R\rho cV_w(T_\infty - T_w)$, the result of NS8. For $V_w \to 0$ the axial profile is uniform and there is no steady solution that vanishes at infinity.
- **Dimensional check.** $\mathrm{Re} = \rho V_wR/\mu$ is dimensionless. $\rho V_wU_w$ has units N/m$^2$. $a_1$ and $a_2$ have units $\mathrm{Pr}\,V_w^2/c = \mathrm{m^2/s^2}/(\mathrm{J/(kg\,K)}) = \mathrm{K}$. In (13) every term is W/m: $\rho RV_wc\,\Delta T = (\mathrm{kg/m^3})\,\mathrm{m\cdot m/s\cdot J/(kg\,K)\cdot K} = \mathrm{W/m}$ and $\mu V_w^2 = (\mathrm{Pa\,s})(\mathrm{m^2/s^2}) = \mathrm{W/m}$.
- **Energy check.** A steady total-energy balance on the liquid between the wall and infinity gives the same result (13): the energy flux $\rho q\,cT_\infty$ and the pressure work $p_\infty q$ enter at infinity, and the viscous stresses at the wall do the work $4\pi\mu V_w^2 + \rho q\,U_w^2$ on the liquid (from $\tau'_{rr}(R) = 2\mu V_w/R$ and $\tau'_{rz}(R) = -\rho V_wU_w$); through the wall leave $\rho q\,[cT_w + (U_w^2 + V_w^2)/2]$, the pressure work $p(R)\,q$ with $p(R) = p_\infty - \rho V_w^2/2$, and the heat $q_w$. Hence $\rho q\,cT_\infty + p_\infty q + 4\pi\mu V_w^2 + \rho qU_w^2 = \rho q\,[cT_w + (U_w^2 + V_w^2)/2] + p(R)\,q + q_w$; the radial kinetic energy cancels against $(p_\infty - p(R))\,q = \rho qV_w^2/2$, and what remains is (13).
