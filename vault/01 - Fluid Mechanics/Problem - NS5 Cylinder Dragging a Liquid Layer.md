---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - capa-de-liquido
  - flujo-anular
  - conduccion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS5.pdf"
id: "ns5"
pill: "NS5: Dragged layer"
tags_html:
  - "Annular film"
  - "Gravity and drag"
  - "Volume flux"
  - "Adiabatic outer surface"
---

# Problem NS5: Cylinder Dragging a Liquid Layer

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

The solid cylinder of radius $a$ shown in the figure moves vertically with velocity $U$, dragging in its motion a coaxial cylindrical layer of liquid of constant uniform thickness $h$. The liquid has constant values of its density $\rho$, viscosity $\mu$, thermal conductivity $k$, and specific heat $c$. The air surrounding the liquid has a density $\rho_a \ll \rho$ and viscosity $\mu_a \ll \mu$, so that in the first approximation it moves without significant pressure differences, exerting on the liquid a negligible viscous force. Because of the symmetry of the problem, $\partial/\partial\theta = 0$ and the only nonzero velocity component is $v_z$.

1. Obtain the velocity $v_z(r, z)$ and pressure $p(r, z)$ in the liquid.

2. Compute the force on the cylinder (per unit length).

3. Calculate the volume flux $Q$ dragged by the cylinder, as well as the value of $U$ for which $Q = 0$.

4. Assuming that the thermal conductivity of air is very small compared with that of the liquid and that the cylinder is at constant uniform temperature $T_c$, obtain the temperature distribution in the liquid $T(r)$ as well as the conductive heat flux to the wall.

![[attachments/FM-T4/ns5-statement.svg]]
*Statement figure (redrawn from NS5.pdf, p. 1): solid cylinder of radius $a$ moving upward with $U$, coaxial liquid layer of thickness $h$, surrounding air at pressure $p_a$, gravity $g$ and axes $r$, $z$*

Source: NS5.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 in cylindrical coordinates, energy Eq. 4.42, stress components in cylindrical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady motion of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$): equations (4.40)-(4.42) in cylindrical coordinates.
- Axisymmetric ($\partial/\partial\theta = 0$) with $v_r = v_\theta = 0$ (given). Gravity acts along $-\bar{e}_z$, opposite to the motion of the cylinder.
- The layer has uniform thickness $h$ and is far from its ends: the thickness does not change along $z$ (fully developed). No chemical reaction and no radiation.
- The air exerts no pressure variation on the liquid and a negligible viscous force: at the free surface $r = a + h$, $p = p_a$ and the shear stress of the liquid is zero.
- Data: $[\rho,\ \mu,\ k,\ c,\ a,\ h,\ U,\ g,\ p_a,\ T_c]$. Notation: $b = a + h$, $\nu = \mu/\rho$. Unknowns: $v_z(r)$, $p$, the force, $Q$, $U_0$ (the $U$ with $Q = 0$), $T(r)$ and the wall heat flux.
- Degrees of freedom: one velocity component, the pressure and the temperature, each function of $r$ (and $z$ for the pressure until it is determined).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a$, $h$, $b = a + h$ | cylinder radius, layer thickness, outer radius of the layer | m |
| $U$ | velocity of the cylinder (upward) | m/s |
| $p_a$ | air pressure | Pa |
| $T_c$ | cylinder temperature | K |
| $\rho$, $\mu$, $k$, $c$ | liquid properties | kg/m$^3$, Pa s, W/(m K), J/(kg K) |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cylindrical frame $(r,\theta,z)$ with $z$ along the axis, upward (direction of $U$). The basis $\{\bar{e}_r,\bar{e}_\theta,\bar{e}_z\}$ is orthonormal and right-handed.
- Field form: $\bar{v} = v_z\,\bar{e}_z$, $p = p(r,z)$, $T = T(r)$. The liquid occupies $a < r < b$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = a$ | $v_z = U$ | no-slip on the moving cylinder |
| $r = b$ | $\tau'_{rz} = \mu\,\partial v_z/\partial r = 0$ | negligible viscous force of the air |
| $r = b$ | $p = p_a$ | no significant pressure differences in the air |
| $r = a$ | $T = T_c$ | uniform temperature of the cylinder |
| $r = b$ | $\partial T/\partial r = 0$ | conductivity of the air much smaller than $k$: adiabatic free surface |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity

$$ \frac{1}{r}\frac{\partial(rv_r)}{\partial r} + \frac{1}{r}\frac{\partial v_\theta}{\partial\theta} + \frac{\partial v_z}{\partial z} = \underbrace{\cancel{\frac{1}{r}\frac{\partial(rv_r)}{\partial r}}}_{v_r = 0} + \underbrace{\cancel{\frac{1}{r}\frac{\partial v_\theta}{\partial\theta}}}_{v_\theta = 0} + \frac{\partial v_z}{\partial z} = 0 \;\Longrightarrow\; \frac{\partial v_z}{\partial z} = 0 \tag{1} $$

so $v_z = v_z(r)$ (the field does not change along the axis).

### 3.2 Momentum equations and the pressure

r-component: with $v_r = v_\theta = 0$ and $\partial/\partial\theta = 0$ every term vanishes except the pressure gradient,

$$ 0 = -\frac{\partial p}{\partial r} \;\Longrightarrow\; p = p(z) \tag{2} $$

z-component:

$$ \rho\Big(\underbrace{\cancel{\frac{\partial v_z}{\partial t}}}_{\text{steady}} + \underbrace{\cancel{v_r\frac{\partial v_z}{\partial r}}}_{v_r = 0} + \underbrace{\cancel{\frac{v_\theta}{r}\frac{\partial v_z}{\partial\theta}}}_{v_\theta = 0} + \underbrace{\cancel{v_z\frac{\partial v_z}{\partial z}}}_{\text{by (1)}}\Big) = -\frac{dp}{dz} + \mu\,\frac{1}{r}\frac{d}{dr}\left(r\frac{dv_z}{dr}\right) - \rho g \tag{3} $$

By (2), $p$ depends only on $z$; at $r = b$ it equals $p_a$ for every $z$, therefore

$$ \boxed{\,p(r,z) = p_a\,}, \qquad \frac{dp}{dz} = 0 \tag{4} $$

The liquid is at the pressure of the surrounding air everywhere: the weight of the layer is carried by the viscous stress, not by a pressure gradient. Equation (3) becomes

$$ \frac{1}{r}\frac{d}{dr}\left(r\frac{dv_z}{dr}\right) = \frac{\rho g}{\mu} = \frac{g}{\nu} \tag{5} $$

### 3.3 Velocity profile

Multiply (5) by $r$ and integrate: $r\,dv_z/dr = \dfrac{g}{2\nu}r^2 + C_1$. Divide by $r$ and integrate again, with $\int dr/r = \ln r$:

$$ v_z = \frac{g}{4\nu}r^2 + C_1\ln r + C_2 \tag{6} $$

The shear-free condition at $r = b$, $dv_z/dr\big|_b = \dfrac{g}{2\nu}b + \dfrac{C_1}{b} = 0$, gives $C_1 = -\dfrac{g}{2\nu}b^2$. The no-slip condition $v_z(a) = U$ gives $C_2 = U - \dfrac{g}{4\nu}a^2 + \dfrac{g}{2\nu}b^2\ln a$. Substituting,

$$ \boxed{\,v_z(r) = U + \frac{g}{2\nu}\left[\frac{r^2 - a^2}{2} - (a + h)^2\ln\frac{r}{a}\right]\,} \tag{7} $$

### 3.4 Force on the cylinder

The surface of the cylinder is $r = a$; the normal pointing into the liquid is $\bar{n} = +\bar{e}_r$, so $(-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot\bar{n}$ is the force per unit area that the liquid exerts on the cylinder. The pressure is uniform ($p = p_a$) and radial, so it integrates to zero around the circumference. The viscous stress is $\tau'_{rz} = \mu\,dv_z/dr$ (Notes.pdf, stress components in cylindrical coordinates). From (7), $dv_z/dr = \dfrac{g}{2\nu}\left(r - \dfrac{b^2}{r}\right)$, so at the wall

$$ \tau'_{rz}\Big|_a = \mu\frac{g}{2\nu}\left(a - \frac{b^2}{a}\right) = -\frac{\rho g\,(b^2 - a^2)}{2a} = -\frac{\rho g\,h\,(2a + h)}{2a} \tag{8} $$

The force per unit length of cylinder (area $2\pi a$):

$$ \boxed{\,\bar{F} = 2\pi a\,\tau'_{rz}\Big|_a\,\bar{e}_z = -\rho g\,\pi\left[(a + h)^2 - a^2\right]\bar{e}_z = -2\pi a\,\rho g\,h\left(1 + \frac{h}{2a}\right)\bar{e}_z\,} \tag{9} $$

The liquid pulls the cylinder downward with a force equal to the weight of the layer per unit length, as the equilibrium of the whole layer requires (the pressure forces on it cancel).

### 3.5 Volume flux and the velocity for zero flux

$$ Q = \int_a^b v_z\,2\pi r\,dr \tag{10} $$

With $\kappa = g/(2\nu)$, three integrals are needed. The first is elementary, $\int_a^b r\,dr = (b^2 - a^2)/2$. For the second, the antiderivative of $r(r^2 - a^2)/2$ is $r^4/8 - a^2r^2/4$, and Barrow's rule gives $\dfrac{(b^2 - a^2)^2}{8}$. For the third, integration by parts with $u = \ln(r/a)$, $dv = r\,dr$ gives the antiderivative $\dfrac{r^2}{2}\ln\dfrac{r}{a} - \dfrac{r^2}{4}$, so $\displaystyle\int_a^b r\ln\frac{r}{a}\,dr = \frac{b^2}{2}\ln\frac{b}{a} - \frac{b^2 - a^2}{4}$. Then

$$ \frac{Q}{2\pi} = U\frac{b^2 - a^2}{2} + \kappa\left[\frac{(b^2 - a^2)^2}{8} - b^2\left(\frac{b^2}{2}\ln\frac{b}{a} - \frac{b^2 - a^2}{4}\right)\right] $$

and, simplifying $\frac{(b^2 - a^2)^2}{8} + \frac{b^2(b^2 - a^2)}{4} = \frac{(b^2 - a^2)(3b^2 - a^2)}{8}$,

$$ \boxed{\,Q = \pi U\,(b^2 - a^2) + \frac{\pi g}{\nu}\left[\frac{(b^2 - a^2)(3b^2 - a^2)}{8} - \frac{b^4}{2}\ln\frac{b}{a}\right]\,} \tag{11} $$

Setting $Q = 0$ and solving for $U$:

$$ \boxed{\,U_0 = \frac{g}{\nu}\left[\frac{b^4}{2\,(b^2 - a^2)}\ln\frac{b}{a} - \frac{3b^2 - a^2}{8}\right]\,} \tag{12} $$

For $U > U_0$ the cylinder carries a net upward flux; for $U < U_0$ the layer drains downward.

### 3.6 Temperature distribution and heat flux to the wall

With $v_r = 0$, $\partial T/\partial z = 0$ and the dissipation $\phi_v = \mu\,(dv_z/dr)^2$ (the only non-zero shear is $\tau'_{rz}$), the energy equation (4.42) reduces to

$$ 0 = \phi_v + \frac{k}{r}\frac{d}{dr}\left(r\frac{dT}{dr}\right), \qquad \phi_v = \mu\left[\frac{g}{2\nu}\left(r - \frac{b^2}{r}\right)\right]^2 = \frac{\rho^2g^2}{4\mu}\frac{(r^2 - b^2)^2}{r^2} \tag{13} $$

Let $\Lambda = \rho^2g^2/(4\mu k)$. Multiplying by $r/k$ and expanding $(r^2 - b^2)^2 = r^4 - 2b^2r^2 + b^4$:

$$ \frac{d}{dr}\left(r\frac{dT}{dr}\right) = -\Lambda\left(r^3 - 2b^2r + \frac{b^4}{r}\right) \tag{14} $$

Integrating once, $r\,dT/dr = -\Lambda\left(\dfrac{r^4}{4} - b^2r^2 + b^4\ln r\right) + D_1$. The adiabatic condition $dT/dr\big|_b = 0$ fixes $D_1$ and gives

$$ r\frac{dT}{dr} = -\Lambda\left[\frac{r^4}{4} - b^2r^2 + \frac{3b^4}{4} + b^4\ln\frac{r}{b}\right] \tag{15} $$

Dividing by $r$ and integrating again (the antiderivative of $\ln(r/b)/r$ is $\tfrac{1}{2}\ln^2(r/b)$) with $T(a) = T_c$:

$$ \boxed{\,T(r) = T_c - \frac{\rho^2g^2}{4\mu k}\left[\frac{r^4 - a^4}{16} - \frac{b^2(r^2 - a^2)}{2} + \frac{3b^4}{4}\ln\frac{r}{a} + \frac{b^4}{2}\left(\ln^2\frac{r}{b} - \ln^2\frac{a}{b}\right)\right]\,} \tag{16} $$

*Heat flux to the wall.* The heat flux from the liquid to the cylinder is $\bar{q}\cdot\bar{n}$ with $\bar{n} = -\bar{e}_r$ (out of the liquid): $q_w = k\,dT/dr\big|_a$, and from (15),

$$ \boxed{\,q_w = -\frac{\rho^2g^2}{4\mu}\left[\frac{a^3}{4} - ab^2 + \frac{3b^4}{4a} - \frac{b^4}{a}\ln\frac{b}{a}\right]\,}, \qquad \dot{Q}_w = 2\pi a\,q_w\ \text{per unit length} \tag{17} $$

*Check.* The outer surface is adiabatic, so all the viscous heating generated in the layer must leave through the wall: $\dot{Q}_w = \int_a^b\phi_v\,2\pi r\,dr$. Evaluating both sides numerically for $\rho = 1000$ kg/m$^3$, $\mu = 0.1$ Pa s, $k = 0.6$ W/(m K), $a = 20$ mm, $h = 5$ mm, $U = 0.7$ m/s and $g = 9.81$ m/s$^2$ gives the same value, $6.344$ W/m, to the precision of the integration.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The velocity decreases from $U$ at the wall; the shear stress is largest at the wall and zero at the free surface. The cylinder must support the weight of the layer, which is what (9) says. The pressure plays no role because the free surface is at $p_a$ and the layer is fully developed.
- **Limits.** For $h \ll a$ the layer behaves as a flat film: (11) tends to $Q \simeq 2\pi a\left(Uh - gh^3/(3\nu)\right)$ and (12) to $U_0 \simeq gh^2/(3\nu)$. For $h \to 0$ the force and the flux vanish. For $g \to 0$ the profile is uniform, $v_z = U$.
- **Dimensional check.** $g/\nu$ has units $(\mathrm{m/s^2})/(\mathrm{m^2/s}) = 1/(\mathrm{m\,s})$; in (7) $(g/\nu)\,r^2$ has units m/s. The force per unit length $\rho g\pi b^2$ has units $(\mathrm{kg/m^3})(\mathrm{m/s^2})\,\mathrm{m^2} = \mathrm{N/m}$. In (16), $\Lambda r^4 = \rho^2g^2r^4/(\mu k)$ has units $(\mathrm{kg^2\,s^{-4}})/(\mathrm{kg^2\,s^{-4}\,K^{-1}}) = \mathrm{K}$, with $\mu k$ in $(\mathrm{kg\,m^{-1}s^{-1}})(\mathrm{kg\,m\,s^{-3}K^{-1}})$.
- **Heat balance.** The wall heat flux (17) equals the viscous dissipation of the layer (per unit area of the wall), because no heat leaves through the free surface.
