---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - simetria-esferica
  - presion
  - potencia
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS3.pdf"
id: "ns3"
pill: "NS3: Balloon"
tags_html:
  - "Spherical symmetry"
  - "Unsteady flow"
  - "Inflation power"
  - "Energy balance"
---

# Problem NS3: Spherical Balloon of Variable Radius

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

A spherical balloon of variable radius $R(t)$ is immersed in an infinite liquid medium of density $\rho$ and viscosity $\mu$. Far from the balloon, the liquid is at rest with pressure $p = p_\infty$. Determine the radial velocity $v_r(r,t)$ and pressure distribution $p(r,t)$ for the buoyancy-free spherically-symmetrical motion induced in the surrounding liquid. Obtain also the power required to inflate the balloon.

Additional question (handwritten on the sheet): where does the work go? Consider the following control volume.

The sheet carries no printed figure; the handwritten solution sketches the balloon of radius $r = R$ with surface velocity $v_r = \dot{R}$.

Source: NS3.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 in spherical coordinates, mechanical-energy balance Eq. 4.24, viscous dissipation $\phi_v$ in spherical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Incompressible liquid with constant $\rho$ and $\mu$; equations (4.40) and (4.41) in spherical coordinates $(r,\theta,\phi)$.
- Spherical symmetry: $\bar{v} = v_r(r,t)\,\bar{e}_r$, $v_\theta = v_\phi = 0$, and $\partial/\partial\theta = \partial/\partial\phi = 0$.
- Buoyancy-free: the mass force is neglected (or absorbed in the reduced pressure of Notes.pdf, Eq. 4.13).
- Unsteady: the balloon radius changes with time, so $\partial/\partial t \neq 0$.
- The liquid occupies $r > R(t)$; far from the balloon it is at rest with pressure $p_\infty$.
- Data: $[\rho,\ \mu,\ p_\infty,\ R(t)]$. Unknowns: $v_r(r,t)$, $p(r,t)$ and the inflation power $\dot{W}$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R(t)$, $\dot{R}$, $\ddot{R}$ | balloon radius, its rate of change and acceleration | m, m/s, m/s$^2$ |
| $\rho$, $\mu$ | liquid density and viscosity | kg/m$^3$, Pa s |
| $p_\infty$ | pressure far from the balloon | Pa |
| $\dot{W}$ | power delivered to the liquid by the balloon | W |

## Phase 2: Frames, Field Form and Boundary Conditions

- Spherical frame $(r,\theta,\phi)$ centred on the balloon centre, which stays fixed; $\bar{e}_r$ points away from the centre.
- Field form: $\bar{v} = v_r(r,t)\,\bar{e}_r$, $p = p(r,t)$.

![[attachments/FM-T4/ns3-setup.svg]]
*Balloon of radius $R(t)$ in the liquid: radial velocity $v_r(r,t) = R^2\dot{R}/r^2$, liquid at rest with pressure $p_\infty$ far from the balloon, and the (dashed) control volume of the energy balance of Phase 3*

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = R(t)$ | $v_r = \dot{R}$ | the liquid in contact with the balloon moves with its surface (kinematic condition) |
| $r \to \infty$ | $v_r \to 0$ | liquid at rest far from the balloon |
| $r \to \infty$ | $p \to p_\infty$ | statement |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity and the radial velocity

$$ \nabla\cdot\bar{v} = \frac{1}{r^2}\frac{\partial(r^2v_r)}{\partial r} + \underbrace{\cancel{\frac{1}{r\sin\theta}\frac{\partial(v_\theta\sin\theta)}{\partial\theta}}}_{v_\theta = 0} + \underbrace{\cancel{\frac{1}{r\sin\theta}\frac{\partial v_\phi}{\partial\phi}}}_{v_\phi = 0} = 0 \;\Longrightarrow\; r^2\,v_r = C(t) \tag{1} $$

The kinematic condition $v_r(R,t) = \dot{R}$ gives $C(t) = R^2\dot{R}$:

$$ \boxed{\,v_r(r,t) = \frac{R^2\dot{R}}{r^2}\,} \tag{2} $$

The condition at infinity is satisfied automatically. The velocity at every point is fixed by the instantaneous radius and its rate of change.

### 3.2 Radial momentum and the pressure field

The viscous term of the $r$ component of (4.41) is $\mu\,\partial/\partial r\left[r^{-2}\,\partial(r^2v_r)/\partial r\right]$ (all other viscous terms contain $v_\theta$, $v_\phi$ or derivatives with respect to $\theta$, $\phi$). By (1), $r^2v_r = C(t)$ does not depend on $r$, so $\partial(r^2v_r)/\partial r = 0$ and the viscous force vanishes identically: the flow is irrotational, $\nabla\wedge\bar{v} = 0$. The momentum equation reduces to

$$ \rho\left(\frac{\partial v_r}{\partial t} + v_r\frac{\partial v_r}{\partial r}\right) = -\frac{\partial p}{\partial r} \tag{3} $$

The two accelerations are computed with the product and chain rules, using $d(R^2\dot{R})/dt = 2R\dot{R}^2 + R^2\ddot{R}$ and $\partial(r^{-2})/\partial r = -2r^{-3}$:

$$ \frac{\partial v_r}{\partial t} = \frac{2R\dot{R}^2 + R^2\ddot{R}}{r^2}, \qquad v_r\frac{\partial v_r}{\partial r} = \frac{R^2\dot{R}}{r^2}\left(-\frac{2R^2\dot{R}}{r^3}\right) = -\frac{2R^4\dot{R}^2}{r^5} \tag{4} $$

$$ \frac{\partial p}{\partial r} = -\rho\left[\frac{2R\dot{R}^2 + R^2\ddot{R}}{r^2} - \frac{2R^4\dot{R}^2}{r^5}\right] \tag{5} $$

Integrate (5) from $r$ to $\infty$, with $p(\infty) = p_\infty$. The antiderivatives are $\int r'^{-2}dr' = -1/r'$ and $\int r'^{-5}dr' = -1/(4r'^4)$, and Barrow's rule between $r$ and $\infty$ gives $\int_r^\infty r'^{-2}dr' = 1/r$ and $\int_r^\infty r'^{-5}dr' = 1/(4r^4)$:

$$ p_\infty - p(r,t) = -\rho\left[\frac{2R\dot{R}^2 + R^2\ddot{R}}{r} - \frac{R^4\dot{R}^2}{2r^4}\right] $$

$$ \boxed{\,p(r,t) = p_\infty + \rho\left[\frac{2R\dot{R}^2 + R^2\ddot{R}}{r} - \frac{R^4\dot{R}^2}{2r^4}\right]\,} \tag{6} $$

At the balloon surface $r = R$:

$$ p(R,t) = p_\infty + \rho\left[2\dot{R}^2 + R\ddot{R} - \frac{\dot{R}^2}{2}\right] = p_\infty + \rho\left(\frac{3}{2}\dot{R}^2 + R\ddot{R}\right) \tag{7} $$

### 3.3 Viscous stress at the balloon surface

With the Navier-Poisson law and $\nabla\cdot\bar{v} = 0$, the radial normal stress is (Notes.pdf, stress components in spherical coordinates)

$$ \tau'_{rr} = 2\mu\frac{\partial v_r}{\partial r} = 2\mu\left(-\frac{2R^2\dot{R}}{r^3}\right), \qquad \tau'_{rr}\Big|_{r=R} = -\frac{4\mu\dot{R}}{R} \tag{8} $$

The shear components $\tau'_{r\theta}$ and $\tau'_{r\phi}$ are zero by symmetry, so the viscous traction on the surface is purely radial.

### 3.4 Power required to inflate the balloon

The balloon surface moves with velocity $\dot{R}\,\bar{e}_r$. The liquid occupies $r > R$, so the unit normal pointing out of the liquid at the balloon surface is $-\bar{e}_r$. The traction that the balloon exerts on the liquid is $(-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot(-\bar{e}_r) = (p - \tau'_{rr})\,\bar{e}_r$, and the power it delivers is the force times the velocity of the surface, integrated over the area $4\pi R^2$:

$$ \dot{W} = 4\pi R^2\,\dot{R}\left[p(R,t) - \tau'_{rr}(R)\right] = 4\pi R^2\dot{R}\,p(R,t) + 16\pi\mu R\dot{R}^2 \tag{9} $$

Substituting (7):

$$ \boxed{\,\dot{W} = 4\pi R^2\dot{R}\,p_\infty + 4\pi\rho R^2\dot{R}\left(\frac{3}{2}\dot{R}^2 + R\ddot{R}\right) + 16\pi\mu R\dot{R}^2\,} \tag{10} $$

### 3.5 Where does the work go? (additional question)

The three terms of (10) are identified by computing independently the rate of change of the kinetic energy of the liquid and its viscous dissipation.

*Kinetic energy of the liquid.* With $v_r^2 = R^4\dot{R}^2/r^4$ and $dV = 4\pi r^2\,dr$:

$$ E_k = \int_R^\infty\frac{\rho}{2}\frac{R^4\dot{R}^2}{r^4}\,4\pi r^2\,dr = 2\pi\rho R^4\dot{R}^2\left[-\frac{1}{r}\right]_R^\infty = 2\pi\rho R^3\dot{R}^2 \tag{11} $$

Differentiating with the product rule,

$$ \frac{dE_k}{dt} = 2\pi\rho\left(3R^2\dot{R}^3 + 2R^3\dot{R}\ddot{R}\right) = 4\pi\rho R^2\dot{R}\left(\frac{3}{2}\dot{R}^2 + R\ddot{R}\right) \tag{12} $$

which is exactly the second term of (10).

*Viscous dissipation.* In spherical coordinates with $v_\theta = v_\phi = 0$ the dissipation is $\phi_v = 2\mu\left[(\partial v_r/\partial r)^2 + 2(v_r/r)^2\right]$ (Notes.pdf, $\phi_v$ in spherical coordinates). With $\partial v_r/\partial r = -2R^2\dot{R}/r^3$ and $v_r/r = R^2\dot{R}/r^3$:

$$ \phi_v = 2\mu\left[\frac{4R^4\dot{R}^2}{r^6} + \frac{2R^4\dot{R}^2}{r^6}\right] = \frac{12\mu R^4\dot{R}^2}{r^6} \tag{13} $$

$$ \Phi = \int_R^\infty\frac{12\mu R^4\dot{R}^2}{r^6}\,4\pi r^2\,dr = 48\pi\mu R^4\dot{R}^2\left[-\frac{1}{3r^3}\right]_R^\infty = 16\pi\mu R\dot{R}^2 \tag{14} $$

which is the third term of (10).

*Pressure term.* $4\pi R^2\dot{R}\,p_\infty = p_\infty\,dV_b/dt$ with $V_b = 4\pi R^3/3$ the balloon volume: the work done against the ambient pressure to displace the liquid, that is, to set the ambient liquid in motion (the outward volume flux through any sphere is $4\pi r^2v_r = 4\pi R^2\dot{R}$).

$$ \boxed{\,\dot{W} = p_\infty\frac{dV_b}{dt} + \frac{dE_k}{dt} + \Phi\,} \tag{15} $$

The work supplied by the balloon increases the kinetic energy of the liquid, displaces the ambient pressure $p_\infty$ and is partly converted into internal energy by viscous dissipation. This agrees with the mechanical energy balance (Notes.pdf, Eq. 4.24) applied to the liquid volume between the balloon and a distant material sphere.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The velocity decays as $1/r^2$ because the volume flux $4\pi r^2v_r$ through every sphere equals the rate of volume growth of the balloon. The motion is irrotational, so viscosity does not enter the pressure field (6); it appears only in the boundary traction (8) and the power (10).
- **Limits.** For $r \to \infty$, $v_r \to 0$ and $p \to p_\infty$. For a balloon at constant radius ($\dot{R} = 0$) every term vanishes: no flow, $p = p_\infty$ and no power. For a constant inflation rate ($\ddot{R} = 0$) the pressure is above $p_\infty$ near the balloon, by the amount $\rho\dot{R}^2(3/2)$ at $r = R$.
- **Dimensional check.** $v_r$: $\mathrm{m^2\cdot m/s}/\mathrm{m^2} = \mathrm{m/s}$. In (6), $\rho R\dot{R}^2/r$ has units $(\mathrm{kg/m^3})(\mathrm{m^2/s^2}) = \mathrm{Pa}$ and $\rho R^2\ddot{R}/r$ has units $(\mathrm{kg/m^3})\,\mathrm{m^2}\,(\mathrm{m/s^2})/\mathrm{m} = \mathrm{Pa}$. In (10), $p_\infty\,4\pi R^2\dot{R}$ is Pa $\cdot\,\mathrm{m^3/s} = \mathrm{W}$ and $16\pi\mu R\dot{R}^2$ is $(\mathrm{Pa\,s})\,\mathrm{m}\,(\mathrm{m^2/s^2}) = \mathrm{W}$.
- **Consistency.** Equation (15) is verified term by term: (12) equals the second term of (10) and (14) equals the third, so the power computed from the surface traction equals the power accounted for inside the liquid.
