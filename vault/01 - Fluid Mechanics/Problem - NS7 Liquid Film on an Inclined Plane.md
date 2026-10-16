---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - pelicula-liquida
  - plano-inclinado
  - balance-de-energia
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS7.pdf"
id: "ns7"
pill: "NS7: Inclined film"
tags_html:
  - "Free-surface film"
  - "Gravity-driven flow"
  - "Viscous dissipation"
  - "Energy balance"
---

# Problem NS7: Liquid Film on an Inclined Plane

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

Consider the steady planar motion of a liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$, and specific heat $c$ that flows down over an inclined plane of angle $\alpha$ due to the action of gravity, forming a layer of constant thickness $h$. To solve the problem, use the coordinate system $(x, y)$ indicated in the figure, in which gravity can be expressed as $\bar{g} = g\sin(\alpha)\bar{e}_x - g\cos(\alpha)\bar{e}_y$. To analyze the resulting liquid flow, assume that the velocity components $v_x(y)$ and $v_y(y)$ are a function of the distance to the wall, and that the air surrounding the liquid has a density $\rho_a \ll \rho$ and a viscosity $\mu_a \ll \mu$, such that in the first approximation it moves without significant pressure differences, exerting on the liquid a negligible viscous force.

▪ Using continuity, determine the velocity component $v_y(y)$.

Obtain the pressure field $p(x, y)$ by integration of the $y$ component of the momentum equation, demonstrating in particular that $\partial p/\partial x = 0$.

Compute $v_x(y)$.

Calculate the force per unit surface that the liquid exerts on the wall.

Determine the temperature in the liquid $T(y)$. In the calculation, assume that the thermal conductivity of air is very small compared with that of the liquid ($k_a \ll k$) and that the wall is at constant uniform temperature $T_w$.

Obtain the conductive heat flux from the liquid to the wall $(\bar{q}\cdot\bar{n})_w$, where $\bar{n}$ is appropriately oriented.

To analyze the energy balances emerging in the problem, consider the fixed control volume $V_o$ of unity length indicated in the figure.

▪ Compute the total energy dissipated per unit time inside the control volume $\int_{V_o}\phi_v\,dV$.

▪ Calculate the work per unit time done by gravity $\int_{V_o}\rho\bar{v}\cdot\bar{g}\,dV$.

▪ Use convervation of energy in the control volume to explain why $(\bar{q}\cdot\bar{n})_w = \int_{V_o}\phi_v\,dV = \int_{V_o}\rho\bar{v}\cdot\bar{g}\,dV$.

Transcribed as printed, including the markers of the sheet and the spelling "convervation".

![[attachments/FM-T4/ns7-statement.svg]]
*Statement figure (redrawn from NS7.pdf, p. 1): layer of thickness $h$ on a plane inclined at $\alpha$, axes $x$ (down the plane) and $y$ (normal to it), gravity $\bar{g} = g\sin\alpha\,\bar{e}_x - g\cos\alpha\,\bar{e}_y$, air at $p_a$ and the fixed control volume $V_o$ of unit length*

Source: NS7.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41, energy Eq. 4.42, internal-energy balance Eq. 4.25, total-energy balance Eq. 4.3.

## Phase 1: Hypotheses, Data and Unknowns

- Steady planar flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$): equations (4.40)-(4.42).
- The fields depend only on the distance $y$ to the plane: $\partial/\partial x = 0$ for $v_x$, $v_y$ and $T$. The pressure is determined below.
- The plane is impermeable and fixed; the liquid layer has uniform thickness $h$; no chemical reaction and no radiation.
- The air exerts no pressure variation and a negligible viscous force on the liquid, and its thermal conductivity is negligible: at the free surface $y = h$, $p = p_a$, $\tau'_{xy} = 0$ and $\partial T/\partial y = 0$.
- Data: $[\rho,\ \mu,\ k,\ c,\ h,\ \alpha,\ g,\ p_a,\ T_w]$. Unknowns: $v_y$, $p(x,y)$, $v_x(y)$, the wall force, $T(y)$, the wall heat flux and the three energy integrals.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $h$ | layer thickness | m |
| $\alpha$ | inclination of the plane | rad |
| $g\sin\alpha$, $g\cos\alpha$ | components of gravity along and normal to the plane | m/s$^2$ |
| $p_a$, $T_w$ | air pressure, wall temperature | Pa, K |
| $\rho$, $\mu$, $k$, $c$ | liquid properties | kg/m$^3$, Pa s, W/(m K), J/(kg K) |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cartesian frame $(x,y,z)$ attached to the plane: $x$ down the slope, $y$ normal to the plane and into the liquid, $z$ out of the plane; the basis is orthonormal and right-handed. Gravity has the components $g_x = g\sin\alpha$, $g_y = -g\cos\alpha$. The frame is rotated by $\alpha$ with respect to the horizontal-vertical frame; the rotation matrix between them is orthogonal with determinant $1$, since $\bar{e}_x = (\cos\alpha, -\sin\alpha)$ and $\bar{e}_y = (\sin\alpha, \cos\alpha)$ in horizontal-vertical components.
- Field form: $\bar{v} = v_x(y)\,\bar{e}_x + v_y(y)\,\bar{e}_y$, $T = T(y)$, $p = p(x,y)$.
- Fixed control volume $V_o$ of the figure: $0 < y < h$, unit length in $x$ and unit width; surfaces: the wall $\Sigma_w$ ($\bar{n} = -\bar{e}_y$), the free surface $\Sigma_s$ ($\bar{n} = +\bar{e}_y$) and the two faces normal to $x$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $y = 0$ | $v_x = 0$, $v_y = 0$, $T = T_w$ | fixed impermeable wall at $T_w$ |
| $y = h$ | $p = p_a$ | no pressure variations in the air |
| $y = h$ | $\tau'_{xy} = \mu\,dv_x/dy = 0$ | negligible viscous force of the air |
| $y = h$ | $dT/dy = 0$ | $k_a \ll k$: adiabatic free surface |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity

$$ \frac{\partial v_x}{\partial x} + \frac{dv_y}{dy} = \underbrace{\cancel{\frac{\partial v_x}{\partial x}}}_{v_x = v_x(y)} + \frac{dv_y}{dy} = 0 \;\Longrightarrow\; v_y = \text{const} \tag{1} $$

The wall is impermeable, $v_y(0) = 0$, so

$$ \boxed{\,v_y(y) = 0\,} \tag{2} $$

### 3.2 y-momentum and the pressure field

With $v_y = 0$ and $\partial_x = 0$ for the velocity, the inertial and viscous terms of the $y$ component vanish:

$$ 0 = -\frac{\partial p}{\partial y} - \rho g\cos\alpha \;\Longrightarrow\; p = -\rho g\cos\alpha\,y + f(x) \tag{3} $$

The free-surface condition $p(x,h) = p_a$ for every $x$ gives $f(x) = p_a + \rho g h\cos\alpha$, a constant:

$$ \boxed{\,p(x,y) = p_a + \rho g\cos\alpha\,(h - y)\,}, \qquad \frac{\partial p}{\partial x} = 0 \tag{4} $$

### 3.3 x-momentum and the velocity profile

$$ \rho\Big(\underbrace{\cancel{v_x\frac{\partial v_x}{\partial x}}}_{\partial_x = 0} + \underbrace{\cancel{v_y\frac{\partial v_x}{\partial y}}}_{v_y = 0}\Big) = -\underbrace{\frac{\partial p}{\partial x}}_{=0} + \mu\frac{d^2v_x}{dy^2} + \rho g\sin\alpha \;\Longrightarrow\; \frac{d^2v_x}{dy^2} = -\frac{\rho g\sin\alpha}{\mu} \tag{5} $$

Integrating twice, $v_x = -\dfrac{\rho g\sin\alpha}{2\mu}y^2 + C_1y + C_2$. The wall condition $v_x(0) = 0$ gives $C_2 = 0$. The free-surface condition $dv_x/dy\big|_h = -\dfrac{\rho g\sin\alpha}{\mu}h + C_1 = 0$ gives $C_1 = \dfrac{\rho g\sin\alpha}{\mu}h$:

$$ \boxed{\,v_x(y) = \frac{\rho g\sin\alpha}{\mu}\left(hy - \frac{y^2}{2}\right) = \frac{gh^2\sin\alpha}{\nu}\left[\frac{y}{h} - \frac{1}{2}\left(\frac{y}{h}\right)^2\right]\,} \tag{6} $$

### 3.4 Force per unit surface on the wall

The normal pointing into the liquid is $\bar{n} = +\bar{e}_y$, so $(-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot\bar{n}$ is the force per unit area that the liquid exerts on the wall. At $y = 0$, $p = p_a + \rho gh\cos\alpha$ from (4), $\tau'_{xy} = \mu\,dv_x/dy\big|_0 = \rho gh\sin\alpha$ and $\tau'_{yy} = 0$:

$$ \boxed{\,\bar{f}_w = -\left(p_a + \rho gh\cos\alpha\right)\bar{e}_y + \rho gh\sin\alpha\,\bar{e}_x\,} \tag{7} $$

The normal component pushes on the wall with the air pressure plus the hydrostatic pressure of the layer; the tangential component is the shear that drags the wall down the slope.

### 3.5 Temperature distribution

With $v_y = 0$ and $\partial_x = 0$ the energy equation (4.42) reduces to $0 = \phi_v + k\,d^2T/dy^2$, with $\phi_v = \mu\,(dv_x/dy)^2$ and, from (6), $dv_x/dy = (\rho g\sin\alpha/\mu)(h - y)$:

$$ \phi_v = \frac{(\rho g\sin\alpha)^2}{\mu}(h - y)^2, \qquad \frac{d^2T}{dy^2} = -\frac{(\rho g\sin\alpha)^2}{\mu k}(h - y)^2 \tag{8} $$

Integrate once: the antiderivative of $(h - y)^2$ is $-(h - y)^3/3$, so $dT/dy = \dfrac{(\rho g\sin\alpha)^2}{3\mu k}(h - y)^3 + B_1$. The adiabatic condition $dT/dy\big|_h = 0$ gives $B_1 = 0$. Integrating again, $T = -\dfrac{(\rho g\sin\alpha)^2}{12\mu k}(h - y)^4 + B_2$, and $T(0) = T_w$ gives $B_2 = T_w + \dfrac{(\rho g\sin\alpha)^2h^4}{12\mu k}$:

$$ \boxed{\,T(y) = T_w + \frac{(\rho g\sin\alpha)^2}{12\,\mu k}\left[h^4 - (h - y)^4\right]\,} \tag{9} $$

Expanding, $h^4 - (h - y)^4 = y\left(4h^3 - 6h^2y + 4hy^2 - y^3\right)$.

### 3.6 Heat flux to the wall

The heat flux from the liquid to the wall is $\bar{q}\cdot\bar{n}$ with $\bar{n} = -\bar{e}_y$ (out of the liquid) and $\bar{q} = -k\nabla T$:

$$ (\bar{q}\cdot\bar{n})_w = k\frac{dT}{dy}\Big|_{y=0} = k\,\frac{(\rho g\sin\alpha)^2h^3}{3\mu k} = \boxed{\,\frac{(\rho g\sin\alpha)^2h^3}{3\mu}\,} \tag{10} $$

### 3.7 Energy balances in the fixed control volume $V_o$

*Total viscous dissipation.* The volume $V_o$ has unit length and width and height $h$, so $dV = dy$:

$$ \int_{V_o}\phi_v\,dV = \int_0^h\frac{(\rho g\sin\alpha)^2}{\mu}(h - y)^2\,dy = \frac{(\rho g\sin\alpha)^2}{\mu}\left[-\frac{(h - y)^3}{3}\right]_0^h = \frac{(\rho g\sin\alpha)^2h^3}{3\mu} \tag{11} $$

*Work of gravity.* $\bar{v}\cdot\bar{g} = v_xg\sin\alpha$ since $v_y = 0$. The antiderivative of $hy - y^2/2$ is $hy^2/2 - y^3/6$ and Barrow's rule gives $h^3/2 - h^3/6 = h^3/3$:

$$ \int_{V_o}\rho\bar{v}\cdot\bar{g}\,dV = \rho g\sin\alpha\int_0^hv_x\,dy = \frac{\rho^2g^2\sin^2\alpha}{\mu}\left[\frac{hy^2}{2} - \frac{y^3}{6}\right]_0^h = \frac{(\rho g\sin\alpha)^2h^3}{3\mu} \tag{12} $$

*Conservation of energy.* In the steady total-energy balance of $V_o$ (Notes.pdf, Eq. 4.3 for a fixed volume), each surface contributes as follows:

| Surface | Convective flux | Pressure work | Viscous work | Heat |
| :--- | :--- | :--- | :--- | :--- |
| Wall $\Sigma_w$ | $0$ ($\bar{v}\cdot\bar{n} = 0$) | $0$ | $0$ ($\bar{v} = 0$) | $-(\bar{q}\cdot\bar{n})_w$ |
| Free surface $\Sigma_s$ | $0$ ($v_y = 0$) | $0$ ($v_y = 0$) | $0$ ($\bar{\bar{\tau}}'\cdot\bar{n} = 0$) | $0$ (adiabatic) |
| Faces normal to $x$ | cancel (profiles independent of $x$) | cancel | cancel | $0$ |

The only remaining term besides the heat flux is the work of the mass force, so $0 = \int_{V_o}\rho\bar{g}\cdot\bar{v}\,dV - (\bar{q}\cdot\bar{n})_w$. The internal-energy balance (Notes.pdf, Eq. 4.25), $0 = \int_{V_o}\phi_v\,dV - (\bar{q}\cdot\bar{n})_w$ with no compression work, gives the second equality:

$$ \boxed{\,(\bar{q}\cdot\bar{n})_w = \int_{V_o}\phi_v\,dV = \int_{V_o}\rho\bar{v}\cdot\bar{g}\,dV = \frac{(\rho g\sin\alpha)^2h^3}{3\mu}\,} \tag{13} $$

Equations (10), (11) and (12) confirm it. The work of gravity on the liquid is entirely dissipated by viscosity and leaves through the wall as heat; the kinetic energy of the liquid in $V_o$ does not change.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The profile (6) is half a parabola: the weight component along the slope is balanced by the shear on the wall, $\tau_w = \rho gh\sin\alpha$, and the pressure is hydrostatic with the normal component of gravity. The wall carries the weight component normal to the plane as pressure.
- **Limits.** For $\alpha = 0$ the plane is horizontal and nothing drives the flow: $v_x = 0$, no dissipation, no heat flux. For $\alpha = 90^\circ$ (vertical wall) the pressure is uniform and equal to $p_a$ and the shear equals the weight of the layer per unit area. The mean velocity is $\bar{v} = gh^2\sin\alpha/(3\nu)$ (flux $Q = \int_0^hv_x\,dy = gh^3\sin\alpha/(3\nu)$).
- **Dimensional check.** $gh^2/\nu$ has units $(\mathrm{m/s^2})\,\mathrm{m^2}/(\mathrm{m^2/s}) = \mathrm{m/s}$. $\rho gh\sin\alpha$ is a pressure. $(\rho g)^2h^3/\mu$ has units $(\mathrm{N/m^3})^2\,\mathrm{m^3}/(\mathrm{Pa\,s}) = \mathrm{N^2\,m^{-3}}/(\mathrm{N\,m^{-2}\,s}) = \mathrm{N/(m\,s)} = \mathrm{W/m^2}$. In (9), $(\rho g)^2h^4/(\mu k)$ has units $\mathrm{K}$.
- **Frame check.** With $\bar{e}_X$ horizontal (towards the descending side) and $\bar{e}_Z$ vertical upward, $\bar{e}_x = \cos\alpha\,\bar{e}_X - \sin\alpha\,\bar{e}_Z$ and $\bar{e}_y = \sin\alpha\,\bar{e}_X + \cos\alpha\,\bar{e}_Z$. The matrix of components has $\det R = \cos^2\alpha + \sin^2\alpha = 1$ and $R\,R^T = I$. Then $\bar{g}\cdot\bar{e}_x = (-g\,\bar{e}_Z)\cdot\bar{e}_x = g\sin\alpha$ and $\bar{g}\cdot\bar{e}_y = -g\cos\alpha$, the components given in the statement.
