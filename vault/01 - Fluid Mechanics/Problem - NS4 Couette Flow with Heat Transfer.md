---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - couette
  - disipacion-viscosa
  - balance-de-energia
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS4.pdf"
id: "ns4"
pill: "NS4: Couette"
tags_html:
  - "Plane Couette flow"
  - "Viscous dissipation"
  - "Heat flux to the walls"
  - "Energy balance"
---

# Problem NS4: Couette Flow with Heat Transfer

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

Consider the steady planar motion of a perfect liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$, and specific heat $c$ in the gap of thickness $h$ that forms between two infinite horizontal walls. The upper wall, at temperature $T_u$, moves parallel to itself with velocity $U$, while the lower wall remains at rest, at temperature $T_l$.

1. Determine the velocity components $v_x(z)$ and $v_z(z)$, as well as the accompanying pressure field $p(x, z)$, assuming that the pressure on the upper wall has the constant value $p = p_u$.

2. Calculate the volume flux for the flow established in the gap.

3. Obtain the pressure distribution $T(z)$.

4. Compute the force per unit surface acting on the upper wall as well as the power needed to move it.

5. Determine the conductive heat flux from the fluid to the upper and lower walls.

6. Use the fixed control volume $V_o$ indicated in the figure to show that the power employed to move the upper wall is dissipated inside the liquid, generating an excess internal energy that is transfered by heat condution to the walls.

Transcribed as printed: in item 3 the sheet says "pressure distribution" where the temperature distribution $T(z)$ is meant, and "transfered" and "condution" are spelling errors of the sheet.

![[attachments/FM-T4/ns4-statement.png]]
*Statement figure (crop of NS4.pdf, p. 1): gap of thickness $h$, upper wall moving with $U$, fixed control volume $V_o$ of unit length in $x$, axes $x$, $z$ and gravity $g$*

Source: NS4.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41, energy Eq. 4.42, internal-energy balance Eq. 4.25, total-energy balance Eq. 4.3.

## Phase 1: Hypotheses, Data and Unknowns

- Steady planar flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$): equations (4.40)-(4.42).
- Infinite horizontal walls, gravity along $-\bar{e}_z$; no chemical reaction and no radiation ($Q_c = Q_r = 0$).
- The velocity and temperature depend only on the distance $z$ to the lower wall: $\partial/\partial x = \partial/\partial y = 0$ for them. The pressure may depend on $x$ and $z$ until it is determined.
- The walls are impermeable. The lower wall ($z = 0$) is at rest at $T_l$; the upper wall ($z = h$) moves with $U\,\bar{e}_x$ at $T_u$ and the pressure on it is $p_u$.
- Data: $[\rho,\ \mu,\ k,\ c,\ h,\ U,\ T_l,\ T_u,\ p_u,\ g]$. Unknowns: $v_x(z)$, $v_z(z)$, $p(x,z)$, $T(z)$, the flow rate, the wall force and power, the wall heat fluxes.
- Degrees of freedom: two velocity components, pressure and temperature, each a function of $z$ (the pressure also of $x$).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $h$ | gap between the walls | m |
| $U$ | velocity of the upper wall | m/s |
| $T_l$, $T_u$ | temperatures of the lower and upper walls | K |
| $p_u$ | pressure on the upper wall | Pa |
| $\rho$, $\mu$, $k$, $c$ | density, viscosity, conductivity, specific heat | kg/m$^3$, Pa s, W/(m K), J/(kg K) |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cartesian frame $(x,y,z)$: $x$ along the walls in the direction of $U$, $z$ normal to the walls and upward from the lower wall, $y$ out of the plane. The basis is orthonormal and right-handed (no change of basis).
- Field form: $\bar{v} = v_x(z)\,\bar{e}_x + v_z(z)\,\bar{e}_z$, $T = T(z)$, $p = p(x,z)$.
- Fixed control volume $V_o$ of the figure: the box $0 < z < h$ of unit length in $x$ and unit width in $y$; its surfaces are the lower wall $\Sigma_l$ ($\bar{n} = -\bar{e}_z$), the upper wall $\Sigma_u$ ($\bar{n} = +\bar{e}_z$) and the two vertical faces $\Sigma_1$ ($\bar{n} = -\bar{e}_x$) and $\Sigma_2$ ($\bar{n} = +\bar{e}_x$).

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $z = 0$ | $v_x = 0$, $v_z = 0$, $T = T_l$ | lower wall at rest, impermeable |
| $z = h$ | $v_x = U$, $v_z = 0$, $T = T_u$ | upper wall moving, impermeable |
| $z = h$ | $p = p_u$ | statement |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity and the normal velocity

$$ \frac{\partial v_x}{\partial x} + \frac{dv_z}{dz} = \underbrace{\cancel{\frac{\partial v_x}{\partial x}}}_{v_x = v_x(z)} + \frac{dv_z}{dz} = 0 \;\Longrightarrow\; v_z = \text{const} \tag{1} $$

The wall is impermeable, $v_z(0) = 0$, so

$$ \boxed{\,v_z(z) = 0\,} \tag{2} $$

### 3.2 Momentum equations

z-component: with $v_z = 0$ every inertial and viscous term vanishes,

$$ 0 = -\frac{\partial p}{\partial z} - \rho g \;\Longrightarrow\; p + \rho g z = f(x) \tag{3} $$

x-component: the convective terms vanish ($\partial_x = 0$, $v_z = 0$),

$$ \rho\Big(\underbrace{\cancel{\frac{\partial v_x}{\partial t}}}_{\text{steady}} + \underbrace{\cancel{v_x\frac{\partial v_x}{\partial x}}}_{\partial_x = 0} + \underbrace{\cancel{v_z\frac{\partial v_x}{\partial z}}}_{v_z = 0}\Big) = -\frac{\partial p}{\partial x} + \mu\frac{d^2v_x}{dz^2} \;\Longrightarrow\; \mu\frac{d^2v_x}{dz^2} = \frac{\partial p}{\partial x} = f'(x) \tag{4} $$

The left side depends only on $z$ and the right side only on $x$, so both are equal to a constant. The pressure on the upper wall is $p(x,h) = p_u$ for every $x$, and by (3) $f(x) = p_u + \rho g h$ is a constant, so $f'(x) = 0$:

$$ \boxed{\,p(x,z) = p_u + \rho g\,(h - z)\,}, \qquad \frac{\partial p}{\partial x} = 0 \tag{5} $$

Equation (4) becomes $d^2v_x/dz^2 = 0$; integrating twice, $v_x = C_1 + C_2z$. The conditions $v_x(0) = 0$ and $v_x(h) = U$ give $C_1 = 0$ and $C_2 = U/h$:

$$ \boxed{\,v_x(z) = U\,\frac{z}{h}\,} \tag{6} $$

### 3.3 Volume flux

The flux per unit width in $y$ through a section $x = \text{const}$ is $Q = \int_0^h v_x\,dz$. The antiderivative of $Uz/h$ is $Uz^2/(2h)$ and Barrow's rule gives:

$$ \boxed{\,Q = \left[\frac{U}{h}\frac{z^2}{2}\right]_0^h = \frac{Uh}{2}\,} \tag{7} $$

### 3.4 Temperature distribution

The energy equation (4.42) with $v_z = 0$, $\partial_x = 0$ and $\phi_v = \mu(dv_x/dz)^2 = \mu U^2/h^2$:

$$ \underbrace{\cancel{\rho c\,v_x\frac{\partial T}{\partial x}}}_{\partial_x = 0} = \phi_v + k\frac{d^2T}{dz^2} \;\Longrightarrow\; \frac{d^2T}{dz^2} = -\frac{\mu U^2}{k\,h^2} \tag{8} $$

Integrating twice, $T = B_1 + B_2z - \dfrac{\mu U^2}{2kh^2}z^2$. The conditions $T(0) = T_l$ and $T(h) = T_u$ give $B_1 = T_l$ and $B_2 = \dfrac{T_u - T_l}{h} + \dfrac{\mu U^2}{2kh}$:

$$ \boxed{\,T(z) = T_l + \left(T_u - T_l\right)\frac{z}{h} + \frac{\mu U^2}{2k}\,\frac{z}{h}\left(1 - \frac{z}{h}\right)\,} \tag{9} $$

### 3.5 Force on the upper wall and power needed to move it

On the upper wall, the normal pointing into the liquid is $\bar{n} = -\bar{e}_z$, so $(-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot\bar{n}$ is the force per unit area that the liquid exerts on the wall. The viscous components are $\tau'_{xz} = \mu\,dv_x/dz = \mu U/h$ and $\tau'_{zz} = 0$ (Notes.pdf, stress components, Cartesian coordinates):

$$ \bar{f}_u = -p_u(-\bar{e}_z) + \bar{\bar{\tau}}'\cdot(-\bar{e}_z) = p_u\,\bar{e}_z - \mu\frac{U}{h}\,\bar{e}_x \tag{10} $$

The viscous part opposes the motion of the wall. The external agent must supply $+\mu U/h\,\bar{e}_x$ per unit area, with the wall velocity $U\bar{e}_x$:

$$ \boxed{\,\bar{f}_u = p_u\,\bar{e}_z - \mu\frac{U}{h}\,\bar{e}_x, \qquad \dot{W} = \mu\frac{U^2}{h}\ \text{per unit area}\,} \tag{11} $$

The pressure force $p_u\bar{e}_z$ is normal to the wall and does no work on it.

### 3.6 Heat fluxes to the walls

The heat flux from the liquid to a wall is $\bar{q}\cdot\bar{n}$, with $\bar{n}$ pointing out of the liquid and $\bar{q} = -k\nabla T$. From (9),

$$ \frac{dT}{dz} = \frac{T_u - T_l}{h} + \frac{\mu U^2}{2kh} - \frac{\mu U^2}{kh^2}z \tag{12} $$

*Upper wall* ($\bar{n} = +\bar{e}_z$, $z = h$):

$$ q_u = -k\frac{dT}{dz}\Big|_{z=h} = k\frac{T_l - T_u}{h} + \frac{\mu U^2}{2h} \tag{13} $$

*Lower wall* ($\bar{n} = -\bar{e}_z$, $z = 0$):

$$ q_l = +k\frac{dT}{dz}\Big|_{z=0} = k\frac{T_u - T_l}{h} + \frac{\mu U^2}{2h} \tag{14} $$

$$ \boxed{\,q_u = k\frac{T_l - T_u}{h} + \frac{\mu U^2}{2h}, \qquad q_l = k\frac{T_u - T_l}{h} + \frac{\mu U^2}{2h}\,} \tag{15} $$

The conductive contributions are equal and opposite and the viscous heating splits equally between the walls. Their sum is $q_u + q_l = \mu U^2/h$.

### 3.7 Integral balance in the fixed control volume $V_o$

*Total energy* (Notes.pdf, Eq. 4.3 in integral form for the fixed volume, steady):

$$ \int_{\Sigma_o}\rho\left(e + \frac{\lvert\bar{v}\rvert^2}{2}\right)\bar{v}\cdot\bar{n}\,d\sigma = -\int_{\Sigma_o}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_o}\bar{v}\cdot\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\int_{V_o}\rho\bar{g}\cdot\bar{v}\,dV}_{=0} - \int_{\Sigma_o}\bar{q}\cdot\bar{n}\,d\sigma \tag{16} $$

Each term, surface by surface (areas of unit length times unit width):

| Surface | Convective $\int\rho(e + v^2/2)\,\bar{v}\cdot\bar{n}$ | Pressure work $-\int p\,\bar{v}\cdot\bar{n}$ | Viscous work $\int\bar{v}\cdot\bar{\bar{\tau}}'\cdot\bar{n}$ | Heat $-\int\bar{q}\cdot\bar{n}$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_l$ ($z = 0$) | $0$ ($\bar{v}\cdot\bar{n} = 0$) | $0$ | $0$ ($\bar{v} = 0$) | $-q_l$ |
| $\Sigma_u$ ($z = h$) | $0$ ($\bar{v}\cdot\bar{n} = 0$) | $0$ | $U\,\tau'_{xz} = \mu U^2/h$ | $-q_u$ |
| $\Sigma_1 + \Sigma_2$ | the two faces cancel ($\bar{v}$, $e$, $p$ do not depend on $x$; opposite normals) | cancel | cancel | $0$ ($T$ independent of $x$) |

The mass-force work vanishes because $\bar{g}\cdot\bar{v} = -g\,v_z = 0$. Equation (16) gives

$$ 0 = \mu\frac{U^2}{h} - q_u - q_l \;\Longrightarrow\; \boxed{\,\mu\frac{U^2}{h} = q_u + q_l\,} \tag{17} $$

*Internal energy* (Notes.pdf, Eq. 4.25, steady, $\nabla\cdot\bar{v} = 0$): $0 = -\int_{\Sigma_o}\bar{q}\cdot\bar{n}\,d\sigma + \int_{V_o}\phi_v\,dV$, with $\int_{V_o}\phi_v\,dV = \dfrac{\mu U^2}{h^2}\,h = \dfrac{\mu U^2}{h}$ (area $1$, height $h$), which again gives $q_u + q_l = \mu U^2/h$.

Equations (11), (15) and (17) show the whole chain: the power spent moving the upper wall, $\mu U^2/h$ per unit area, equals the viscous dissipation in the liquid and leaves the volume as the heat conducted to the two walls.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The pressure is hydrostatic and the velocity is linear: viscous forces alone transmit the motion. The dissipation $\phi_v = \mu U^2/h^2$ is uniform, and it heats the liquid; the parabolic term of (9) is the temperature rise it produces, with its maximum in the middle of the gap.
- **Limits.** For $U \to 0$ there is no flow and no dissipation: $T$ is the linear conduction profile between $T_l$ and $T_u$ and $q_u = -q_l = k(T_l - T_u)/h$. For $T_u = T_l$, the temperature is symmetric about $z = h/2$ and each wall receives $\mu U^2/(2h)$.
- **Dimensional check.** $\mu U/h$: $(\mathrm{Pa\,s})(\mathrm{m/s})/\mathrm{m} = \mathrm{Pa}$. $\mu U^2/h$: $\mathrm{Pa\cdot m/s} = \mathrm{W/m^2}$. In (9), $\mu U^2/(2k)$ has units $(\mathrm{Pa\,s})(\mathrm{m^2/s^2})/[\mathrm{W/(m\,K)}] = \mathrm{K}$.
- **Mean velocity.** From (7), $\bar{v} = Q/h = U/2$, half the wall velocity.
