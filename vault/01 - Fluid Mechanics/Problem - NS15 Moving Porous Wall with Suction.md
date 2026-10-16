---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - pared-porosa
  - succion
  - balance-integral
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS15.pdf"
id: "ns15"
pill: "NS15: Moving wall"
tags_html:
  - "Asymptotic suction profile"
  - "Wall shear and heat flux"
  - "Integral balances"
  - "Viscous dissipation"
---

# Problem NS15: Moving Porous Wall with Suction

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

Problem 2: Consider a buoyancy-free, steady planar motion occurring in a semi-infinite space filled with a perfect liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$, and specific heat $c$. The liquid is bounded by an infinitely long porous wall that moves parallel to itself with velocity $U_w$ while removing the liquid with a normal suction velocity $V_w$. Far from the wall, the horizontal velocity component is zero and the pressure is $p = p_\infty$. The ambient value of the temperature $T = T_\infty$ is higher than the value $T_w$ at the wall.

1. Determine the velocity components $v_x(y)$ and $v_y(y)$ and well as the pressure field $p(x, y)$.

2. Obtain the temperature distribution $T(y)$.

3. Compute the viscous force acting on the wall per unit surface $\tau_w\bar{e}_x = \bar{\bar{\tau}}'\cdot\bar{n}_w$, where $\bar{n}_w$ is the unit vector normal to the wall.

4. Determine the heat flux from the fluid to the wall $q_w = k(\nabla T)\cdot\bar{n}_w$.

5. For an alternative computation procedure for $\tau_w$ and $q_w$, apply the momentum and energy conservation equations to the control volume indicated in the figure. In dealing with the balance equations, evaluate explicitly the contribution of each term, stating clearly the reasons justifying any simplifications introduced.

The sheet is headed "INTRODUCTION TO FLUID MECHANICS, FINAL (Jan 21, 2014)". Transcribed as printed, including "and well as" in item 1.

![[attachments/FM-T4/ns15-statement.svg]]
*Statement figure (redrawn from NS15.pdf, p. 1): porous wall at temperature $T_w$ moving with $U_w$ and sucking with $V_w$, axes $x$, $y$, normals $\bar{n}$ and $\bar{n}_w$, far field $p_\infty$, $T_\infty$ and the fixed control volume $V_c$ of unit length ($\delta x = 1$)*

Source: NS15.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41, energy Eq. 4.42, integral balances Eqs. 4.2 and 4.3.

## Phase 1: Hypotheses, Data and Unknowns

- Steady planar flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$), buoyancy-free (mass forces neglected), in the half space $y > 0$ above a porous wall. The fields depend only on the distance $y$ to the wall (the wall is infinitely long and the flow is the same at every $x$).
- The wall at $y = 0$ moves in its own plane with $U_w$ and removes the liquid with the suction velocity $V_w > 0$: $v_y(0) = -V_w$. No chemical reaction and no radiation.
- Far from the wall ($y \to \infty$): $v_x \to 0$, $p \to p_\infty$, $T \to T_\infty$, with $T_\infty > T_w$.
- Data: $[\rho,\ \mu,\ k,\ c,\ U_w,\ V_w,\ p_\infty,\ T_\infty,\ T_w]$. Unknowns: $v_x$, $v_y$, $p$, $T$, $\tau_w$ and $q_w$.
- Notation: $\nu = \mu/\rho$, $\alpha = k/(\rho c)$, $\mathrm{Pr} = \nu/\alpha = \mu c/k$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U_w$, $V_w$ | wall velocity along itself, suction velocity | m/s |
| $p_\infty$, $T_\infty$, $T_w$ | far-field pressure and temperature, wall temperature | Pa, K, K |
| $\tau_w$ | viscous force per unit area on the wall, along $x$ | Pa |
| $q_w$ | heat flux from the liquid to the wall | W/m$^2$ |
| $\mathrm{Pr}$ | Prandtl number | 1 |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cartesian frame $(x,y,z)$ attached to the wall: $x$ along the wall in the direction of $U_w$, $y$ normal to the wall and into the liquid, $z$ out of the plane; the basis is orthonormal and right-handed. The normal $\bar{n}_w = +\bar{e}_y$ points from the wall into the liquid (figure).
- Field form: $\bar{v} = v_x(y)\,\bar{e}_x + v_y(y)\,\bar{e}_y$, $p = p(x,y)$, $T = T(y)$.
- Control volume $V_c$ of the figure: fixed, of unit length in $x$ ($\delta x = 1$) and unit width, from the wall to a plane $y = Y$ far from it; surfaces: the wall $\Sigma_w$ ($\bar{n} = -\bar{e}_y$), the top $\Sigma_t$ ($\bar{n} = +\bar{e}_y$) and the two vertical faces $\Sigma_1$ ($\bar{n} = -\bar{e}_x$) and $\Sigma_2$ ($\bar{n} = +\bar{e}_x$).

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $y = 0$ | $v_x = U_w$, $v_y = -V_w$, $T = T_w$ | moving porous wall, suction |
| $y \to \infty$ | $v_x \to 0$, $p \to p_\infty$, $T \to T_\infty$ | liquid at rest far from the wall |

## Phase 3: Step-by-Step Derivation

### 3.1 Velocity and pressure (item 1)

$$ \frac{\partial v_x}{\partial x} + \frac{dv_y}{dy} = \underbrace{\cancel{\frac{\partial v_x}{\partial x}}}_{v_x = v_x(y)} + \frac{dv_y}{dy} = 0 \;\Longrightarrow\; v_y = \text{const} = -V_w \tag{1} $$

The $y$ component of the momentum equation (no mass force, $dv_y/dy = 0$, $d^2v_y/dy^2 = 0$) gives $0 = -\partial p/\partial y$, so $p = p(x)$, and the far-field condition $p \to p_\infty$ for every $x$ gives $\partial p/\partial x = 0$:

$$ \boxed{\,v_y(y) = -V_w, \qquad p(x,y) = p_\infty\,} \tag{2} $$

The $x$ component:

$$ \rho\Big(\underbrace{\cancel{v_x\frac{\partial v_x}{\partial x}}}_{\partial_x = 0} + v_y\frac{dv_x}{dy}\Big) = -\underbrace{\frac{\partial p}{\partial x}}_{=0} + \mu\frac{d^2v_x}{dy^2} \;\Longrightarrow\; \frac{d^2v_x}{dy^2} + \frac{V_w}{\nu}\frac{dv_x}{dy} = 0 \tag{3} $$

Trying $e^{\lambda y}$: $\lambda(\lambda + V_w/\nu) = 0$, so $v_x = C_1 + C_2e^{-V_wy/\nu}$. The condition $v_x \to 0$ at infinity gives $C_1 = 0$ (the exponential decays because $V_w > 0$), and $v_x(0) = U_w$ gives $C_2 = U_w$:

$$ \boxed{\,v_x(y) = U_w\,e^{-V_wy/\nu}\,} \tag{4} $$

### 3.2 Temperature (item 2)

With $v_y = -V_w$, $\partial_x = 0$ and $\phi_v = \mu\,(dv_x/dy)^2$, equation (4.42) reads $-\rho cV_w\,dT/dy = \phi_v + k\,d^2T/dy^2$. From (4), $dv_x/dy = -(V_wU_w/\nu)e^{-V_wy/\nu}$, so

$$ \frac{d^2T}{dy^2} + \frac{V_w}{\alpha}\frac{dT}{dy} = -\frac{\mu U_w^2V_w^2}{k\,\nu^2}\,e^{-2V_wy/\nu} \tag{5} $$

The homogeneous solution is $B_1 + B_2e^{-V_wy/\alpha}$. A particular solution $A\,e^{-2V_wy/\nu}$ requires (substituting $T_p' = -(2V_w/\nu)A\,e^{-2V_wy/\nu}$ and $T_p'' = (4V_w^2/\nu^2)A\,e^{-2V_wy/\nu}$ and using $\nu/\alpha = \mathrm{Pr}$):

$$ A\,(4 - 2\,\mathrm{Pr}) = -\frac{\mu U_w^2}{k} = -\frac{\mathrm{Pr}\,U_w^2}{c} \;\Longrightarrow\; A = \frac{\mathrm{Pr}}{2(\mathrm{Pr} - 2)}\frac{U_w^2}{c} \tag{6} $$

for $\mathrm{Pr} \neq 2$. (For $\mathrm{Pr} = 2$ the exponents of the homogeneous and the particular solution coincide and the particular solution is $D\,y\,e^{-2V_wy/\nu}$. With $\lambda = 2V_w/\nu$, $T_p' = D(1 - \lambda y)e^{-\lambda y}$ and $T_p'' = D(\lambda^2y - 2\lambda)e^{-\lambda y}$, so $T_p'' + \lambda T_p' = -D\lambda\,e^{-\lambda y}$; matching the right-hand side of (5), $D\lambda = \mu U_w^2V_w^2/(k\nu^2)$, that is $D = \mu U_w^2V_w/(2k\nu)$. The results (8) and (10) do not depend on $\mathrm{Pr}$.) The conditions $T(\infty) = T_\infty$ and $T(0) = T_w$ give $B_1 = T_\infty$ and $B_2 = T_w - T_\infty - A$:

$$ \boxed{\,T(y) = T_\infty + \left(T_w - T_\infty - \frac{\mathrm{Pr}\,U_w^2}{2(\mathrm{Pr} - 2)\,c}\right)e^{-\mathrm{Pr}\,V_wy/\nu} + \frac{\mathrm{Pr}\,U_w^2}{2(\mathrm{Pr} - 2)\,c}\,e^{-2V_wy/\nu}\,} \tag{7} $$

since $V_wy/\alpha = \mathrm{Pr}\,V_wy/\nu$.

### 3.3 Viscous force on the wall (item 3)

With $\bar{n}_w = \bar{e}_y$, the vector $\bar{\bar{\tau}}'\cdot\bar{n}_w$ is the viscous force per unit area that the liquid exerts on the wall: $\tau'_{xy}\,\bar{e}_x + \tau'_{yy}\,\bar{e}_y$ with $\tau'_{xy} = \mu\,dv_x/dy$ and $\tau'_{yy} = 2\mu\,dv_y/dy = 0$. At $y = 0$, from (4):

$$ \boxed{\,\tau_w = \mu\frac{dv_x}{dy}\Big|_0 = -\rho\,V_w\,U_w\,} \tag{8} $$

The liquid pulls the wall back, against its motion.

### 3.4 Heat flux to the wall (item 4)

With $\bar{n}_w = \bar{e}_y$, $q_w = k\,dT/dy\big|_0$. Differentiating (7) at $y = 0$, with $B_2 = T_w - T_\infty - A$:

$$ \frac{dT}{dy}\Big|_0 = -\frac{V_w}{\nu}\left(\mathrm{Pr}\,B_2 + 2A\right) \;\Longrightarrow\; q_w = -\rho cV_w\left(B_2 + \frac{2A}{\mathrm{Pr}}\right) = -\rho cV_w\left[T_w - T_\infty - \frac{(\mathrm{Pr} - 2)A}{\mathrm{Pr}}\right] \tag{9} $$

using $k/\nu = \rho c/\mathrm{Pr}$ and $(\mathrm{Pr} - 2)A/\mathrm{Pr} = U_w^2/(2c)$:

$$ \boxed{\,q_w = \rho cV_w\left[T_\infty - T_w + \frac{U_w^2}{2c}\right] = \frac{1}{2}\rho V_wU_w^2 + \rho cV_w\,(T_\infty - T_w)\,} \tag{10} $$

### 3.5 Alternative computation with the control volume $V_c$ (item 5)

*Momentum, $x$ component* (steady, fixed volume, Notes.pdf Eq. 4.2 in integral form; no mass force):

$$ \int_{\Sigma_c}\rho\,v_x\,(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}p\,n_x\,d\sigma + \int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma \tag{11} $$

| Surface | $\int\rho v_x\,\bar{v}\cdot\bar{n}\,d\sigma$ | $-\int p\,n_x\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_w$ ($\bar{n} = -\bar{e}_y$, $\bar{v}\cdot\bar{n} = V_w$) | $\rho\,U_wV_w$ | $0$ ($n_x = 0$) | $-\tau'_{xy}(0) = -\tau_w$ |
| $\Sigma_t$ ($\bar{n} = +\bar{e}_y$) | $0$ ($v_x \to 0$ far from the wall) | $0$ ($n_x = 0$) | $0$ ($dv_x/dy \to 0$) |
| $\Sigma_1 + \Sigma_2$ | cancel (profile independent of $x$, opposite normals) | cancel ($p$ uniform) | cancel ($\tau'_{xx} = 0$) |

Therefore $\rho\,U_wV_w = -\tau_w$, that is $\tau_w = -\rho V_wU_w$, in agreement with (8): the wall must supply the momentum $\rho U_w$ per unit mass to the liquid it sucks, since the liquid at infinity has none.

*Total energy* (Notes.pdf, Eq. 4.3 for a fixed volume, steady, no mass force):

$$ \int_{\Sigma_c}\rho\left(e + \frac{\lvert\bar{v}\rvert^2}{2}\right)\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma = \int_{\Sigma_c}\bar{v}\cdot\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma \tag{12} $$

| Surface | Convective energy flux | Pressure work | Viscous work $\bar{v}\cdot\bar{\bar{\tau}}'\cdot\bar{n}$ | Conduction $\bar{q}\cdot\bar{n}$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_w$ | $\rho\left[cT_w + \tfrac{1}{2}(U_w^2 + V_w^2)\right]V_w$ | $p_\infty V_w$ | $-U_w\tau_w = \rho V_wU_w^2$ | $k\,dT/dy\big\rvert_0 = q_w$ |
| $\Sigma_t$ | $-\rho\left[cT_\infty + \tfrac{1}{2}V_w^2\right]V_w$ | $-p_\infty V_w$ | $0$ (no shear far away) | $0$ ($dT/dy \to 0$) |
| $\Sigma_1 + \Sigma_2$ | cancel | cancel | cancel | $0$ ($T$ independent of $x$) |

On $\Sigma_w$, $\bar{v}\cdot\bar{n} = V_w$, $\bar{v} = U_w\bar{e}_x - V_w\bar{e}_y$ and $\bar{v}\cdot\bar{\bar{\tau}}'\cdot\bar{n} = -(v_x\tau'_{xy} + v_y\tau'_{yy}) = -U_w\tau_w$; on $\Sigma_t$, $\bar{v} = -V_w\bar{e}_y$ and $T = T_\infty$. The pressure is uniform ($p_\infty$) so its work cancels between $\Sigma_w$ and $\Sigma_t$. Adding the surfaces,

$$ \rho V_w\left[c\,(T_w - T_\infty) + \frac{U_w^2}{2}\right] = \rho V_wU_w^2 - q_w \;\Longrightarrow\; \boxed{\,q_w = \frac{1}{2}\rho V_wU_w^2 + \rho cV_w\,(T_\infty - T_w)\,} \tag{13} $$

which is (10). The simplifications used are justified by the fact that all the fields are independent of $x$ (lateral faces), that the shear and the temperature gradient decay exponentially (top surface, placed at $Y \gg \nu/V_w, \alpha/V_w$), and that the liquid is at rest and at $p_\infty$ far away.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** Suction holds the moving layer of thickness $\nu/V_w$ (momentum) and $\alpha/V_w$ (thermal) against the wall. The wall pays for the momentum of the entrained liquid ((8)), and receives the enthalpy, the kinetic energy and the viscous work ((10)).
- **Limits.** For $U_w = 0$: no shear, no dissipation, $q_w = \rho cV_w(T_\infty - T_w)$ (pure advection-conduction). For $V_w \to 0$ the layer thickens and there is no steady solution. For $T_\infty = T_w$ the heat flux is $\tfrac{1}{2}\rho V_wU_w^2 > 0$: the wall must remove the kinetic energy of the entrained liquid even when the temperatures are equal.
- **Dimensional check.** $V_wy/\nu$ and $\mathrm{Pr}\,V_wy/\nu$ are dimensionless. $\rho V_wU_w$ has units $\mathrm{N/m^2}$. $\rho V_wU_w^2$ and $\rho cV_w\Delta T$ have units $\mathrm{W/m^2}$.
- **Relation to NS1.** The problem is that of NS1 with the wall moving instead of the free stream: the profiles have the same form, and (10) is (23) of NS1 with $U_\infty \to U_w$.
