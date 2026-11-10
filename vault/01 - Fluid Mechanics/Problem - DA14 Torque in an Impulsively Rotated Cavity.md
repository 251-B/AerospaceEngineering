---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - adimensionalizacion
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA14.pdf"
id: "da14"
pill: "DA14: Rotating cavity"
sheets:
  - 14
tags_html:
  - "Π theorem"
  - "Navier-Stokes"
  - "Nondimensionalization"
  - "Viscous dissipation"
---

# Problem DA14: Torque in an Impulsively Rotated Cavity

> Official dimensional-analysis sheet of the course (Fluid Mechanics I exam of 21-06-2022), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25), the Navier-Stokes equations in cylindrical coordinates (Notes.pdf, Chapter 4), their nondimensionalization with scales taken from the problem (Notes.pdf, Eqs. 6.45-6.50) and the comparison of both methods.

## Statement

The sketch shows a circular cavity full of liquid of density $\rho$ and viscosity $\mu$ surrounded by an outer case at temperature $T_0$. The fluid is initially at rest, temperature $T_0$ and pressure $p_0$. At $t = 0^+$, the outer case is impulsively set to rotate with a constant angular velocity $\Omega$.

1. Use the Π theorem to reduce the parametric dependence of the torque $M$ (per unit length) necessary to sustain the constant angular velocity of the outer case from $t = 0$ to $t \to \infty$.

2. Formulate the **full** mathematical problem that determines the evolution of the fluid field (velocity, pressure and temperature) in the cavity $0 \le r \le R$ for $0 < t < \infty$, including boundary and initial conditions. Consider the pressure in the fluid adjacent to the wall is known to be $p_1$. Simplify the problem as much as possible to obtain the differential equations, with initial and boundary conditions, that determine the azimuthal velocity $v_\theta$, $T$ and $p$. Viscous dissipation might not be negligible.

3. Find $v_\theta$, $T$ and $p$ in the case $t \to \infty$.

4. From the last result, obtain the adequate scales $v_{\theta c}$, $r_c$, respectively for $v_\theta$, $r$. Find the adequate time scale $t_c$ using order-of-magnitude analysis in the time-dependent differential equation for $v_\theta$. Make the problem non-dimensional introducing the scales in the dimensional problem.

5. Define the expression that needs to be evaluated to find the torque $M$ at any instant of time $t$, using the detailed solution of the non-dimensional problem, scaling $M$ adequately.

6. Compare the last result with that of part #1 and comment the result

![[attachments/FM-T6/da14-statement.svg]]
*Statement figure (redrawn from DA14.pdf): a circular cavity of radius R full of liquid (ρ, μ), initially at rest, inside a case at temperature T_0 that is set to rotate at Ω at t = 0⁺*

**Note:** It is strongly recommended to use cylindrical coordinates

Source: DA14.pdf (page 1: statement; pages 2 and 3: handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; nondimensionalization, Eqs. 6.45-6.50. Notes.pdf, Chapter 4: continuity, momentum and energy equations of a perfect liquid.

## Hypotheses, Data and Dimensional Table

- Perfect liquid: constant $\rho$, $\mu$, thermal conductivity $k$ and specific heat $c$. With constant properties the temperature does not act back on the velocity, so the torque does not depend on $T_0$, $k$ or $c$.
- The cavity is long (the torque is per unit length) and the motion is axisymmetric: $\partial/\partial\theta = 0$, $v_z = 0$, $\partial/\partial z = 0$. Gravity is not considered (it would only add a hydrostatic part to $p$).
- Frame: cylindrical coordinates $(r, \theta, z)$ fixed to the ground, origin on the axis.

| Quantity | Dimensions |
| :--- | :--- |
| $M$ (torque per unit length) | $MLT^{-2}$ |
| $t$ | $T$ |
| $\rho$ | $ML^{-3}$ |
| $\mu$ | $ML^{-1}T^{-1}$ |
| $\Omega$ | $T^{-1}$ |
| $R$ | $L$ |

## Application of the Π Theorem

$$ M = M(t, \rho, \mu, \Omega, R) $$

The torque per unit length has the dimensions of a force: $[M] = ML^2T^{-2}/L = MLT^{-2}$. Exponent matrix with columns $(M, L, T)$, as in the key:

| | $M$ | $L$ | $T$ |
| :--- | ---: | ---: | ---: |
| $M$ | 1 | 1 | −2 |
| $t$ | 0 | 0 | 1 |
| $\rho$ | 1 | −3 | 0 |
| $\mu$ | 1 | −1 | −1 |
| $\Omega$ | 0 | 0 | −1 |
| $R$ | 0 | 1 | 0 |

The rows of $(\mu, \Omega, R)$ give, expanding along the first column, $\det = 1\cdot\left(0\cdot 0 - (-1)\cdot 1\right) = 1 \neq 0$: they have independent dimensions. With $n = 5$ and $k = 3$, two groups remain.

**Torque.** $[M] = [\mu]^a[\Omega]^b[R]^c$: $M:\; 1 = a$; $T:\; -2 = -a - b$, $b = 1$; $L:\; 1 = -a + c$, $c = 2$: $\Pi_0 = M/(\mu\Omega R^2)$.

**Time.** $[t] = [\Omega]^{-1}$: $\Pi_1 = \Omega t$.

**Density.** $[\rho] = [\mu]^a[\Omega]^b[R]^c$: $M:\; 1 = a$; $T:\; 0 = -1 - b$, $b = -1$; $L:\; -3 = -1 + c$, $c = -2$: $\Pi_2 = \rho\Omega R^2/\mu$, a Reynolds number.

$$ \frac{M}{\mu\Omega R^2} = f\left(\Omega t, \frac{\rho\Omega R^2}{\mu}\right) $$

## The Full Problem and its Simplification

The equations of a perfect liquid (Notes.pdf, Chapter 4) in cylindrical coordinates, with $\partial/\partial\theta = 0$ and $v_z = 0$:

**Continuity.**

$$ \frac{1}{r}\frac{\partial(r v_r)}{\partial r} = 0 \;\Longrightarrow\; r v_r = f(t) $$

At the wall $v_r(R, t) = 0$, so $f(t) = 0$ and $v_r = 0$ everywhere.

**Radial momentum.** With $v_r = 0$ the only surviving inertial term is the centripetal one:

$$ -\rho\frac{v_\theta^2}{r} = -\frac{\partial p}{\partial r} $$

**Azimuthal momentum.** The convective terms $v_r\partial v_\theta/\partial r$, $v_rv_\theta/r$ and the pressure term $(1/r)\partial p/\partial\theta$ vanish:

$$ \frac{\partial v_\theta}{\partial t} = \nu\frac{\partial}{\partial r}\left[\frac{1}{r}\frac{\partial(r v_\theta)}{\partial r}\right] $$

**Energy.** The convective terms vanish ($v_r = 0$, $\partial T/\partial\theta = 0$); conduction and viscous dissipation remain:

$$ \rho c\frac{\partial T}{\partial t} = \frac{k}{r}\frac{\partial}{\partial r}\left(r\frac{\partial T}{\partial r}\right) + \mu\left[r\frac{\partial}{\partial r}\left(\frac{v_\theta}{r}\right)\right]^2 $$

The last term is the dissipation $\Phi_v$ of the only non-zero strain rate, $r\,\partial(v_\theta/r)/\partial r$.

**Initial and boundary conditions.**

| Where | Condition | Origin |
| :--- | :--- | :--- |
| $t = 0$ | $v_\theta = 0$, $T = T_0$ | fluid at rest at $T_0$ |
| $r = R$, $t > 0$ | $v_\theta = \Omega R$, $T = T_0$ | no slip on the rotating case; case at $T_0$ |
| $r = R$ | $p = p_1$ | statement |
| $r = 0$ | $v_\theta = 0$, $\partial T/\partial r = 0$ | regularity on the axis |

The velocity problem is closed by itself; $p$ follows from the radial equation and $T$ from the energy equation once $v_\theta$ is known.

## The Limit t → ∞

**Velocity.** Steady state: $\partial/\partial t = 0$ in the azimuthal equation, so

$$ \frac{\partial}{\partial r}\left[\frac{1}{r}\frac{\partial(r v_\theta)}{\partial r}\right] = 0 \;\Longrightarrow\; \frac{1}{r}\frac{d(r v_\theta)}{dr} = A $$

Multiply by $r$ and integrate from the axis, where $r v_\theta = 0$, to $r$ (Barrow's rule):

$$ \int_0^r \frac{d(r' v_\theta)}{dr'}\,dr' = \big[r' v_\theta\big]_0^r = r v_\theta - 0 = \int_0^r A r'\,dr' = \left[\frac{A r'^2}{2}\right]_0^r = \frac{A r^2}{2} $$

so $v_\theta = A r/2$; the general solution $A r/2 + B/r$ has lost its $B/r$ term, singular on the axis. The wall condition $v_\theta(R) = \Omega R$ gives $A = 2\Omega$:

$$ v_\theta = \Omega r $$

the liquid rotates as a rigid body.

**Pressure.** $\partial p/\partial r = \rho v_\theta^2/r = \rho\Omega^2 r$. Integrating from the wall, where $p = p_1$, to $r$:

$$ p(r) - p_1 = \int_R^r \rho\Omega^2 r'\,dr' = \left[\frac{\rho\Omega^2 r'^2}{2}\right]_R^r = \frac{\rho\Omega^2}{2}\left(r^2 - R^2\right) \;\Longrightarrow\; p = p_1 + \frac{1}{2}\rho\Omega^2R^2\left[\left(\frac{r}{R}\right)^2 - 1\right] $$

**Temperature.** In rigid rotation $v_\theta/r = \Omega$ is uniform, so $\Phi_v = 0$, and the steady energy equation is $\frac{d}{dr}\left(r\frac{dT}{dr}\right) = 0$. Integrating from the axis, where regularity gives $r\,dT/dr = 0$, to $r$ (Barrow's rule): $\left[r'\frac{dT}{dr'}\right]_0^r = r\frac{dT}{dr} - 0 = 0$, so $dT/dr = 0$ for $r > 0$, $T$ is uniform, and the wall condition gives

$$ T = T_0 $$

## Scales and Nondimensional Problem

From the steady solution: $r_c = R$ and $v_{\theta c} = \Omega R$. The time scale comes from balancing the two terms of the azimuthal equation (Notes.pdf, Eq. 6.45):

$$ \frac{v_{\theta c}}{t_c} \sim \nu\frac{v_{\theta c}}{r_c^2} \;\Longrightarrow\; t_c \sim \frac{R^2}{\nu} $$

the time for viscous diffusion to cross the cavity. Define

$$ V = \frac{v_\theta}{\Omega R}, \qquad \eta = \frac{r}{R}, \qquad \tau = \frac{t}{R^2/\nu} $$

so $\partial/\partial t = (\nu/R^2)\,\partial/\partial\tau$ and $\partial/\partial r = R^{-1}\partial/\partial\eta$ (chain rule). Term by term:

$$ \frac{\partial v_\theta}{\partial t} = \frac{\Omega R\,\nu}{R^2}\frac{\partial V}{\partial\tau}, \qquad \nu\frac{\partial}{\partial r}\left[\frac{1}{r}\frac{\partial(r v_\theta)}{\partial r}\right] = \frac{\nu\,\Omega R}{R^2}\frac{\partial}{\partial\eta}\left[\frac{1}{\eta}\frac{\partial(\eta V)}{\partial\eta}\right] $$

Both sides carry the same factor $\nu\Omega/R$, which cancels:

$$ \frac{\partial V}{\partial\tau} = \frac{\partial}{\partial\eta}\left[\frac{1}{\eta}\frac{\partial(\eta V)}{\partial\eta}\right]; \qquad \tau = 0:\; V = 0; \qquad \tau > 0:\; V(1, \tau) = 1,\; V(0, \tau) = 0 $$

**A problem without parameters**: $V(\eta, \tau)$ is a universal function.

**Temperature.** With $\Theta = (T - T_0)/T_0$, each term of the energy equation becomes

$$ \rho c\,T_0\frac{\nu}{R^2}\frac{\partial\Theta}{\partial\tau} = \frac{k T_0}{R^2}\frac{1}{\eta}\frac{\partial}{\partial\eta}\left(\eta\frac{\partial\Theta}{\partial\eta}\right) + \mu\Omega^2\left[\eta\frac{\partial}{\partial\eta}\left(\frac{V}{\eta}\right)\right]^2 $$

(the strain rate is $r\,\partial(v_\theta/r)/\partial r = \Omega\,\eta\,\partial(V/\eta)/\partial\eta$). Dividing by $\rho c T_0\nu/R^2 = \mu c T_0/R^2$:

$$ \frac{\partial\Theta}{\partial\tau} = \frac{1}{\mathrm{Pr}}\,\frac{1}{\eta}\frac{\partial}{\partial\eta}\left(\eta\frac{\partial\Theta}{\partial\eta}\right) + \frac{\Omega^2R^2}{c\,T_0}\left[\eta\frac{\partial}{\partial\eta}\left(\frac{V}{\eta}\right)\right]^2, \qquad \mathrm{Pr} = \frac{\mu c}{k} $$

with $\Theta = 0$ at $\tau = 0$, $\Theta = 0$ at $\eta = 1$ and $\partial\Theta/\partial\eta = 0$ at $\eta = 0$. The temperature depends on two parameters: the Prandtl number and $\Omega^2R^2/(cT_0)$, the ratio of the kinetic energy of the wall to the thermal energy (an Eckert-type number; both are **extensions**, not defined in Chapter 6).

> [!warning] Discrepancy with the official solution
> The key writes the conduction term as $\mathrm{Pr}\,\frac{1}{\eta}\frac{\partial}{\partial\eta}(\dots)$ with $\mathrm{Pr} = \mu c/k$; dividing $k T_0/R^2$ by $\mu c T_0/R^2$ gives $k/(\mu c) = 1/\mathrm{Pr}$, as written above.

## Torque from the Nondimensional Solution

The torque per unit length is the shear stress on the wall times the lever arm $R$ times the perimeter $2\pi R$:

$$ M = \tau_{r\theta}\big|_{r=R}\,R\,2\pi R, \qquad \tau_{r\theta} = \mu\left[r\frac{\partial}{\partial r}\left(\frac{v_\theta}{r}\right) + \frac{1}{r}\frac{\partial v_r}{\partial\theta}\right] = \mu\Omega\,\eta\frac{\partial}{\partial\eta}\left(\frac{V}{\eta}\right) $$

($v_r = 0$). Hence

$$ M = 2\pi\mu\Omega R^2\left[\eta\frac{\partial}{\partial\eta}\left(\frac{V}{\eta}\right)\right]_{\eta = 1} \;\Longrightarrow\; \frac{M}{2\pi\mu\Omega R^2} = f(\tau) $$

As $\tau \to \infty$, $V \to \eta$, so $V/\eta \to 1$ and its derivative vanishes: $f \to 0$ and $M \to 0$. Once the liquid turns as a rigid body there is no shear and no torque is needed to keep the case turning.

## Comparison with the Π Theorem

The Π theorem gave $M/(\mu\Omega R^2) = f(\Pi_1, \Pi_2)$ with $\Pi_1 = \Omega t$ and $\Pi_2 = \rho\Omega R^2/\mu$. The nondimensional equations show that the two groups enter only through

$$ \tau = \frac{t\nu}{R^2} = \frac{\Omega t}{\rho\Omega R^2/\mu} = \frac{\Pi_1}{\Pi_2} $$

so $M/(\mu\Omega R^2) = 2\pi f(\Pi_1/\Pi_2)$: the two results are consistent, and the equations reduce the parametric dependence further than the Π theorem, which cannot see that $\rho$ and $t$ appear only in the combination $t\nu/R^2$ (Notes.pdf, p. 68: the nondimensional equations give the minimum set of parameters).

## Answers and Checks

- Π theorem: $M/(\mu\Omega R^2) = f(\Omega t, \rho\Omega R^2/\mu)$.
- Simplified problem: $v_r = 0$; $\rho v_\theta^2/r = \partial p/\partial r$; $\partial v_\theta/\partial t = \nu\,\partial_r[(1/r)\partial_r(r v_\theta)]$; $\rho c\,\partial T/\partial t = (k/r)\partial_r(r\partial_r T) + \mu[r\partial_r(v_\theta/r)]^2$, with the conditions of the table.
- $t \to \infty$: $v_\theta = \Omega r$, $p = p_1 + \tfrac{1}{2}\rho\Omega^2R^2[(r/R)^2 - 1]$, $T = T_0$.
- Scales: $r_c = R$, $v_{\theta c} = \Omega R$, $t_c = R^2/\nu$; nondimensional velocity problem without parameters.
- Torque: $M/(2\pi\mu\Omega R^2) = f(\tau) = [\eta\,\partial_\eta(V/\eta)]_{\eta = 1}$, which tends to 0 for $\tau \to \infty$.
- Dimensions: $\mu\Omega R^2$ is $ML^{-1}T^{-1}\cdot T^{-1}\cdot L^2 = MLT^{-2}$, a torque per unit length; $\Omega^2R^2/(cT_0)$ is $L^2T^{-2}/(L^2T^{-2}\Theta^{-1}\cdot\Theta) = 1$.
- Pressure check: $p$ is lowest on the axis, $p(0) = p_1 - \tfrac{1}{2}\rho\Omega^2R^2$, as the centripetal acceleration requires.
- Check against the official key: DA14.pdf gives the same groups, equations, steady solution, scales, nondimensional problem and torque expression, with $\Pi_1' = \Pi_1/\Pi_2$; the coefficient of the conduction term is corrected above.
