---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-casi-estacionario
  - tuberia-vertical
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF5.pdf"
id: "vf5"
pill: "VF5: Two-liquid discharge"
sheets:
  - 5
tags_html:
  - "Quasi-steady Poiseuille flow"
  - "Two immiscible liquids"
  - "Discharge time"
---

# Problem VF5: Discharge of Two Immiscible Liquids from a Tube

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: quasi-steady Poiseuille flow in a pipe (Notes.pdf, Eqs. 7.13-7.15 and 7.49-7.51), the criterion of Eq. 7.41 and mass conservation of the draining column.

## Statement

A vertical tube of radius $a$ open at the top contains initially two columns of heights $l_1$ and $l_2$ of two inmiscible liquids with different densities $\rho_1$ and $\rho_2$ and viscosities $\mu_1$ and $\mu_2$. At a given instant of time, the bottom end of the pipe opens up, releasing the fluid 2 to the atmosphere. During the discharge process, determine the volume flux as a function of time as well as the pressure distribution along the pipe. Calculate the time for complete discharge of the bottom liquid column.

The sheet prints "inmiscible". The figure labels the upper liquid $(\rho_1, \mu_1)$ of height $l_1$, the lower liquid $(\rho_2, \mu_2)$ of height $h(t)$, the pressure $p_s$ at the interface, $p_a$ above and below, and the axis $x$ pointing down from the top.

![[attachments/FM-T7/vf5-statement.svg]]
*Statement figure (redrawn from VF5.pdf): a vertical tube of radius a, open at both ends once the bottom is released, with liquid 1 (ρ_1, μ_1) of height l_1 above liquid 2 (ρ_2, μ_2) of height h(t); p_s is the pressure at the interface*

Source: VF5.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: steady flow in a circular pipe, Eqs. 7.13-7.15; slender flows dominated by viscosity, Eqs. 7.40-7.46; pipe flow, Eqs. 7.47-7.51.

## Hypotheses, Data and Unknowns

- **Viscous regime.** The flow is dominated by viscosity if the convective and local accelerations are negligible against the viscous force (Eqs. 7.40 and 7.41). With the velocity estimated by the balance of the weight of the column and the viscous force, $V_L\sim\rho g a^2/\mu$, the criterion is (computed in the first section of the solution)
$$ \frac{\rho^2 g\,a^4}{\mu^2\,l}\ll 1 $$
with $l\sim l_1\sim l_2$ the length of the columns (the key writes the characteristic density and viscosity without subscript). Under it the flow is quasi-steady Poiseuille flow in each column.
- The liquids are incompressible and immiscible, so the interface moves with them; the upper column keeps its length $l_1$ (it slides down as a plug as the lower column drains) and the lower column has the length $h(t)$, with $h(0) = l_2$.
- Pressure at the open top and at the open bottom: $p_a$. The interface pressure $p_s(t)$ is unknown.
- The $x$ axis points down from the top and $z$ points up from the bottom (figure); gravity acts along $+x$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a$ | radius of the tube | m |
| $\rho_1$, $\mu_1$, $l_1$ | density, viscosity, height of the upper liquid | kg/m$^3$, kg/(m s), m |
| $\rho_2$, $\mu_2$, $l_2$, $h(t)$ | same for the lower liquid; $h(0) = l_2$ | kg/m$^3$, kg/(m s), m |
| $Q$, $p_s$ | volume flux and interface pressure | m$^3$/s, Pa |

## Criterion for Viscous Dominance

The local acceleration over the viscous term is $\dfrac{a^2/(\mu/\rho)}{t_0}$ with $t_0\sim l/V_L$ the time of variation (the time to travel the column); the convective one is $\dfrac{\rho V_La}{\mu}\dfrac{a}{l}$ (Eqs. 7.40-7.41). They are the same number, and with $V_L\sim\Delta P\,a^2/(\mu l)$, $\Delta P\sim\rho g l$ (the pressure difference that drives the flow is the weight of the column), $V_L\sim\rho g a^2/\mu$:

$$ \frac{\rho V_L a}{\mu}\,\frac{a}{l}\sim\frac{\rho}{\mu}\,\frac{\rho g a^2}{\mu}\,\frac{a^2}{l} = \frac{\rho^2 g a^4}{\mu^2 l}\ll 1 $$

## Flux in Each Column

In a column of length $\ell$ of the pipe the flow goes down, along $+x$, and the reduced pressure $P = p - \rho g x$ ($x$ down: the potential energy falls as $x$ grows) has the uniform gradient along the flow $P_l = \left(P_{top} - P_{bottom}\right)/\ell = \left(p_{top} - p_{bottom} + \rho g\ell\right)/\ell$, so that the weight of the column helps the flow. The profile is the Poiseuille one (Eq. 7.14), $v_x = \frac{P_l}{4\mu}(a^2 - r^2)$, with the flux (Eq. 7.15), $Q = \frac{\pi a^4}{8\mu}P_l$.

**Upper liquid.** From the free surface ($p = p_a$) to the interface ($p = p_s$), of length $l_1$:

$$ Q = \frac{\pi a^4}{8\mu_1}\,\frac{p_a - p_s + \rho_1 g l_1}{l_1} $$

**Lower liquid.** From the interface ($p = p_s$) to the open end ($p = p_a$), of length $h$:

$$ Q = \frac{\pi a^4}{8\mu_2}\,\frac{p_s - p_a + \rho_2 g h}{h} $$

Mass conservation of an incompressible liquid in a tube of constant section gives the same $Q$ in both columns, so the pressure drops are

$$ p_a - p_s + \rho_1 g l_1 = \frac{8\mu_1 l_1}{\pi a^4}\,Q, \qquad p_s - p_a + \rho_2 g h = \frac{8\mu_2 h}{\pi a^4}\,Q $$

## Volume Flux and Evolution of the Interface

Adding the two equations cancels the unknown $p_s$:

$$ \left(\rho_1 l_1 + \rho_2 h\right)g = \frac{8}{\pi a^4}\left(\mu_1 l_1 + \mu_2 h\right)Q \;\Longrightarrow\; Q = \frac{\pi a^4 g}{8}\,\frac{\rho_1 l_1 + \rho_2 h}{\mu_1 l_1 + \mu_2 h} $$

This gives $Q$ as a function of the position $h$ of the lower interface. The lower column loses the volume $dV = -\pi a^2\,dh$ in $dt$, so $Q = -\pi a^2\,dh/dt$. Substituting:

$$ \left(\rho_1 l_1 + \rho_2 h\right)g = -\frac{8}{a^2}\left(\mu_1 l_1 + \mu_2 h\right)\frac{dh}{dt} $$

Separating variables and integrating from $h = l_2$ at $t = 0$ (Barrow's rule on the left, with $\int_0^t dt' = t$):

$$ \int_{l_2}^{h}\frac{\mu_1 l_1 + \mu_2 h'}{\rho_1 l_1 + \rho_2 h'}\,dh' = -\frac{g a^2}{8}\,t $$

The key leaves the left side unevaluated. Writing $\mu_1 l_1 + \mu_2 h' = \frac{\mu_2}{\rho_2}\left(\rho_1 l_1 + \rho_2 h'\right) + l_1\left(\mu_1 - \frac{\mu_2\rho_1}{\rho_2}\right)$ the integrand is $\frac{\mu_2}{\rho_2} + \frac{l_1(\mu_1\rho_2 - \mu_2\rho_1)}{\rho_2}\,\frac{1}{\rho_1 l_1 + \rho_2 h'}$ and, since $\int\frac{dh'}{\rho_1 l_1 + \rho_2 h'} = \frac{1}{\rho_2}\ln\left(\rho_1 l_1 + \rho_2 h'\right)$ (computed here):

$$ \frac{\mu_2}{\rho_2}\left(h - l_2\right) + \frac{l_1\left(\mu_1\rho_2 - \mu_2\rho_1\right)}{\rho_2^2}\,\ln\frac{\rho_1 l_1 + \rho_2 h}{\rho_1 l_1 + \rho_2 l_2} = -\frac{g a^2}{8}\,t $$

which gives $t(h)$ explicitly, and $h(t)$ implicitly; $Q(t)$ follows from $Q(h)$ above.

## Pressure Distribution

The pressure at the interface follows from the upper column:

$$ p_s - p_a = \rho_1 g l_1 - \frac{8\mu_1 l_1}{\pi a^4}Q = \rho_1 g l_1 - \mu_1 l_1 g\,\frac{\rho_1 l_1 + \rho_2 h}{\mu_1 l_1 + \mu_2 h} = \frac{g\,l_1 h\left(\mu_2\rho_1 - \mu_1\rho_2\right)}{\mu_1 l_1 + \mu_2 h} $$

Inside each column the actual pressure is linear in $x$: with $P_l = (p_{top} - p_{bottom} + \rho g\ell)/\ell$, $p = p_{top} - P_lx + \rho gx = p_{top} - (p_{top} - p_{bottom})x/\ell$, because the weight term $\rho gx$ cancels. With $x$ measured down from the top,

$$ p(x) = p_a + \left(p_s - p_a\right)\frac{x}{l_1}\quad(0 < x < l_1), \qquad p(x) = p_s + \left(p_a - p_s\right)\frac{x - l_1}{h}\quad(l_1 < x < l_1 + h) $$

(it is $p_a$ at both ends; the interface is the only point where it differs, by $p_s - p_a$, positive if $\mu_2\rho_1 > \mu_1\rho_2$).

## Complete Discharge Time

At $h = 0$, $t = t_d$. From the explicit $t(h)$ above:

$$ t_d = \frac{8}{g a^2}\left[\frac{\mu_2 l_2}{\rho_2} + \frac{l_1\left(\mu_1\rho_2 - \mu_2\rho_1\right)}{\rho_2^2}\,\ln\left(1 + \frac{\rho_2 l_2}{\rho_1 l_1}\right)\right] $$

## Answers and Checks

- Viscous dominance: $\rho^2 g a^4/(\mu^2 l)\ll 1$.
- Volume flux: $Q = \frac{\pi a^4 g}{8}\frac{\rho_1 l_1 + \rho_2 h}{\mu_1 l_1 + \mu_2 h}$, with $h(t)$ defined by $\int_{l_2}^{h}\frac{\mu_1 l_1 + \mu_2 h'}{\rho_1 l_1 + \rho_2 h'}dh' = -\frac{g a^2}{8}t$.
- Pressure: linear in each liquid, with the interface value $p_s - p_a = \frac{g l_1 h(\mu_2\rho_1 - \mu_1\rho_2)}{\mu_1 l_1 + \mu_2 h}$.
- Discharge time: the expression above.
- Limit of equal liquids ($\mu_1 = \mu_2 = \mu$, $\rho_1 = \rho_2 = \rho$): $p_s = p_a$, $Q = \pi a^4\rho g/(8\mu)$ (constant, independent of $h$ and $l_1$) and $t_d = 8\mu l_2/(\rho g a^2) = \pi a^2 l_2/Q$, the time to empty a volume $\pi a^2 l_2$ at that flux.
- Limit $l_1\to 0$ (only liquid 2): $Q = \frac{\pi a^4\rho_2 g}{8\mu_2}$ and $t_d = \frac{8\mu_2 l_2}{\rho_2 g a^2}$.
- Dimensions: $\pi a^4\rho g/\mu$ is $L^4\cdot ML^{-3}\cdot LT^{-2}/(ML^{-1}T^{-1}) = L^3T^{-1}$; $\rho^2ga^4/(\mu^2 l)$ is $M^2L^{-6}\cdot LT^{-2}\cdot L^4/(M^2L^{-2}T^{-2}\cdot L) = 1$.
- Check against the official key: VF5.pdf gives the same criterion, profiles and fluxes, the equation for $p_s$, $(\rho_1 l_1 + \rho_2 h)g = \frac{8}{\pi a^4}(\mu_1 l_1 + \mu_2 h)Q$ and the integral relation boxed above; it stops there, so the explicit integral, the pressure field and the discharge time are computed here.
