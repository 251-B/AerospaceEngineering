---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - pelicula-comprimida
  - piston
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF16.pdf"
id: "vf16"
pill: "VF16: Falling piston"
sheets:
  - 16
tags_html:
  - "Radial squeeze film"
  - "Piston dynamics"
  - "Quasi-steady piston"
---

# Problem VF16: Piston Falling over a Liquid Layer

> Official viscous-flow sheet of the course (exam of Jan 14, 2013), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: radial Poiseuille flow in a thin film (Notes.pdf, Eqs. 7.69-7.71 in cylindrical coordinates), continuity across the gap with a moving boundary (Eq. 7.72) and Newton's second law for the piston.

## Statement

**PROBLEM 4 (1 hour)** A cylindrical piston of weight $W$ and radius $R$, whose upper side is exposed to the atmosphere, slides without friction inside a coaxial container of the same radius. The initial distance between the lower side of the piston and the bottom of the tank is $h_0\ll R$. Below the piston, the container is filled with liquid of density $\rho$ and viscosity $\mu$. The piston falls due to its own weight, and forces the liquid to leave the tank, discharging to the atmosphere through a circular hole of radius $\alpha R\ll R$.

The known data are $(\rho, \mu, h_0, R, \alpha, W, g, p_a)$. The objective is to determine the vertical position of the piston as a function of time, $h(t)$, under the assumption of dominant viscous forces in the liquid. Gravitational forces in the liquid can be neglected ($P\approx p$). The following steps are suggested:

1. (2 points). Using the radial momentum equation, find the liquid velocity profile, $v_r(z,t)$, in the slender region $\alpha R\le r\le R$, $0\le z\le h(t)$, as a function of $h(t)$, and of the pressure gradient $P_l = -\partial p/\partial r$.

2. (2 points). Obtain $p(r,t)$ as a function of $h(t)$, $\dot{h}(t) = dh/dt$, and known data. To that end, integrate the continuity equation across the gap (in the $z$ direction), finding the second order differential equation satisfied by $p(r,t)$. To solve the equation, note that the pressure drop across the non-slender turning region $0\le r\le\alpha R$, $0\le z\le h(t)$, can be neglected, so that $p(r = \alpha R)\approx p_a$. Note also that $v_r = 0$ at the container wall $r = R$.

3. (2 points). Find the vertical force acting on the piston due to the liquid and the external atmosphere, $F$, as a function of $h(t)$, $\dot{h}(t)$, and known data. Note that it proves convenient to introduce a function $f(\alpha)$ to express the dependence of $F$ on $\alpha$.

4. (2 points). Using Newton's second law applied to the piston in the vertical direction, find the second-order ODE with initial conditions satisfied by $h(t)$.

5. (2 points). Obtain $h(t)$, as well as the volume flux through the hole, $Q(t)$, under the assumption of negligible inertia of the piston (acceleration of the piston much smaller than $g$). Note that, in this approximation, the pressure forces balance the weight of the piston, the ODE becomes of first order, and only the initial condition $h(0) = h_0$ can be satisfied.

6. (2 additional points). Provide the condition that must be accomplished for viscous forces to be dominant in the liquid, as well as the criterion of negligible inertia of the piston, in terms of the governing parameters $(\rho, \mu, h_0, R, \alpha, W, g, p_a)$.

The sheet gives the hint $\int x\ln x\,dx = \frac{x^2}{2}\left(\ln x - \frac{1}{2}\right)$.

![[attachments/FM-T7/vf16-statement.svg]]
*Statement figure (redrawn from VF16.pdf): a piston of weight W and radius R at the height h(t) above the bottom of a container; the liquid below it leaves through a central hole of radius αR at the pressure p_a (axisymmetric section, r radial and z vertical)*

Source: VF16.pdf (page 1: statement; page 2: handwritten key; exam of Jan 14, 2013). Notes.pdf, Chapter 7: slender films, Eqs. 7.67-7.71; the wedge effect, Eq. 7.72; Newton's second law.

## Hypotheses, Data and Unknowns

- The film between the piston and the bottom is slender ($h\ll R$), axisymmetric, with $z$ the height above the bottom and $r$ the radius. The velocity at the piston is $v_z = \dot{h}$ ($<0$ while it falls), at the bottom $v_z = 0$.
- The liquid has no weight effects, so $P\approx p$; the pressure at the hole edge is $p_a$ (the non-slender turning region has a negligible pressure drop).
- The piston has its weight $W$ downward and the atmospheric pressure on its upper face; the liquid pressure acts on its lower face.

## Velocity Profile

Radial momentum (Eq. 7.69 in cylindrical coordinates) with no slip at the bottom and the piston:

$$ 0 = -\frac{\partial p}{\partial r} + \mu\frac{\partial^2v_r}{\partial z^2} = P_l + \mu\frac{\partial^2v_r}{\partial z^2}; \qquad z = 0:\; v_r = 0, \qquad z = h:\; v_r = 0 \;\Longrightarrow\; v_r = \frac{P_l(r, t)}{2\mu}\,z\,(h - z) $$

## Pressure

Integrate the continuity equation $\frac{\partial(rv_r)}{\partial r} + \frac{\partial(rv_z)}{\partial z} = 0$ across the gap:

$$ \frac{\partial}{\partial r}\left[r\int_0^hv_r\,dz\right] + r\left[v_z(h) - v_z(0)\right] = 0 \;\Longrightarrow\; \frac{\partial}{\partial r}\left[r\,\frac{P_lh^3}{12\mu}\right] + r\dot{h} = 0 $$

and with $P_l = -\partial p/\partial r$: $\frac{\partial}{\partial r}\left(r\frac{\partial p}{\partial r}\right) = \frac{12\mu\dot{h}}{h^3}\,r$. First integration: $r\frac{\partial p}{\partial r} = \frac{6\mu\dot{h}}{h^3}r^2 + A$. At the container wall $v_r = 0$ for every $z$, and since $v_r\propto P_l$ this means $\partial p/\partial r = 0$ at $r = R$:

$$ A = -\frac{6\mu\dot{h}R^2}{h^3}, \qquad \frac{\partial p}{\partial r} = \frac{6\mu\dot{h}}{h^3}\left(r - \frac{R^2}{r}\right) $$

Second integration, with $p(\alpha R) = p_a$:

$$ p = \frac{6\mu\dot{h}}{h^3}\left(\frac{r^2}{2} - R^2\ln r\right) + B \;\Longrightarrow\; p - p_a = -\frac{6\mu\dot{h}}{h^3}\left[R^2\ln\frac{r}{\alpha R} - \frac{r^2 - (\alpha R)^2}{2}\right] $$

For $\dot{h}<0$ it is an overpressure.

## Force on the Piston

The excess force is $F = 2\pi\int_{\alpha R}^{R}(p - p_a)\,r\,dr$ (the part $r<\alpha R$, in front of the hole, is at about $p_a$). With $r = R\eta$, $r\,dr = R^2\eta\,d\eta$:

$$ F = -\frac{12\pi\mu\dot{h}}{h^3}\,R^4f(\alpha), \qquad f(\alpha) = \int_\alpha^1\eta\left[\ln\eta - \ln\alpha - \frac{\eta^2 - \alpha^2}{2}\right]d\eta $$

Evaluating the three pieces with Barrow's rule (using the hint $\int\eta\ln\eta\,d\eta = \frac{\eta^2}{2}\left(\ln\eta - \frac{1}{2}\right)$):

$$ \int_\alpha^1\eta\ln\eta\,d\eta = -\frac{1}{4} - \frac{\alpha^2}{2}\ln\alpha + \frac{\alpha^2}{4}, \qquad -\ln\alpha\int_\alpha^1\eta\,d\eta = -\frac{1 - \alpha^2}{2}\ln\alpha, \qquad -\frac{1}{2}\int_\alpha^1\left(\eta^3 - \alpha^2\eta\right)d\eta = -\frac{1 - \alpha^4}{8} + \frac{\alpha^2(1 - \alpha^2)}{4} $$

$$ f(\alpha) = -\frac{1}{2}\ln\alpha - \frac{3}{8} + \frac{\alpha^2}{2} - \frac{\alpha^4}{8} $$

> [!warning] Discrepancy with the official solution
> The key gives "$f(\alpha) = -\frac{1}{2}\ln\alpha - \frac{5}{12} + \frac{3}{4}\alpha^2 - \frac{1}{3}\alpha^3$" after "computing the integral". That expression is not the value of the integral above (it is not even a function of $\alpha^2$, as the integral is): at $\alpha = 0.5$ the integral is $0.0888$ and the key's polynomial gives $0.0757$. Both vanish at $\alpha = 1$ and both behave as $-\frac{1}{2}\ln\alpha$ for $\alpha\to 0$. The value above is used from here on; its derivative is $f'(\alpha) = -(1 - \alpha^2)^2/(2\alpha)$, which is negative: $f$ decreases from infinity to zero as the hole grows.

The force is positive (upward) for $\dot{h}<0$: the liquid resists the fall.

## Equation of the Piston and Solution

Newton's second law for the piston in the vertical direction (the weight $W$ downward, the force $F$ of the liquid and of the atmosphere upward; $h$ upward):

$$ \frac{W}{g}\,\ddot{h} = F - W, \qquad h(0) = h_0,\quad\dot{h}(0) = 0 $$

(with $F = -12\pi\mu\dot{h}R^4f(\alpha)/h^3$, a second-order ODE).

**Negligible inertia, $|\ddot{h}|\ll g$.** Then $F = W$ and the equation is of first order, with only $h(0) = h_0$:

$$ \frac{dh}{dt} = -\frac{W}{12\pi\mu R^4f(\alpha)}\,h^3 \equiv -k\,h^3 $$

Separating variables, $\frac{dh}{h^3} = -k\,dt$, and integrating (Barrow's rule): $\left[-\frac{1}{2h^2}\right]_{h_0}^h = -kt$, so $\frac{1}{h^2} = \frac{1}{h_0^2} + 2kt$:

$$ \bar{h} = \frac{h}{h_0} = (1 + 2\tau)^{-1/2}, \qquad \tau = \frac{Wh_0^2}{12\pi\mu R^4f(\alpha)}\,t $$

**Volume flux through the hole.** The liquid expelled equals the volume swept by the piston, $Q = -\pi R^2\dot{h} = \pi R^2kh^3$ (computed here):

$$ Q(t) = \frac{W\,h^3}{12\mu R^2f(\alpha)} = \frac{Wh_0^3}{12\mu R^2f(\alpha)}\left(1 + 2\tau\right)^{-3/2} $$

The piston never reaches the bottom in a finite time: $h\to 0$ as $t^{-1/2}$ (it needs to squeeze an ever thinner film).

## Criteria

**Viscous dominance.** The scale of the velocity of the piston follows from the time scale $t_c\sim\mu R^4/(Wh_0^2)$ (the factor of $\tau$): $\dot{h}_c\sim h_0/t_c = Wh_0^3/(\mu R^4)$. The slender-film conditions (Eqs. 7.67-7.68) reduce, as in VF14, to

$$ \frac{h_0\dot{h}_c}{\nu}\ll 1 \;\Longrightarrow\; \frac{\rho\,Wh_0^4}{\mu^2R^4}\ll 1 $$

(besides $h_0\ll R$).

**Negligible inertia of the piston.** The acceleration scale is $\ddot{h}_c\sim h_0/t_c^2 = h_0\left(\dfrac{Wh_0^2}{\mu R^4}\right)^2 = \dfrac{W^2h_0^5}{\mu^2R^8}$, so the condition $\ddot{h}_c\ll g$ is

$$ \frac{W^2h_0^5}{\mu^2R^8g}\ll 1 $$

## Answers and Checks

- Velocity: $v_r = \frac{P_l}{2\mu}z(h - z)$; pressure: $p - p_a = -\frac{6\mu\dot{h}}{h^3}\left[R^2\ln\frac{r}{\alpha R} - \frac{r^2 - (\alpha R)^2}{2}\right]$.
- Force: $F = -\frac{12\pi\mu\dot{h}}{h^3}R^4f(\alpha)$, $f(\alpha) = -\frac{1}{2}\ln\alpha - \frac{3}{8} + \frac{\alpha^2}{2} - \frac{\alpha^4}{8}$.
- Equation: $\frac{W}{g}\ddot{h} = F - W$, $h(0) = h_0$, $\dot{h}(0) = 0$.
- Quasi-steady piston: $\bar{h} = (1 + 2\tau)^{-1/2}$, $\tau = \frac{Wh_0^2t}{12\pi\mu R^4f(\alpha)}$; $Q(t) = \frac{Wh^3}{12\mu R^2f(\alpha)}$.
- Criteria: $\rho Wh_0^4/(\mu^2R^4)\ll 1$ and $W^2h_0^5/(\mu^2R^8g)\ll 1$.
- Dimensions: $Wh_0^2/(\mu R^4)$ is $MLT^{-2}\cdot L^2/(ML^{-1}T^{-1}L^4) = T^{-1}$, so $\tau$ is dimensionless; $Wh^3/(\mu R^2)$ is $L^3T^{-1}$.
- Limit $\alpha\to 1$ (a hole as wide as the piston): $f\to 0$ and $F\to 0$, so the liquid offers no resistance, as it can escape freely; $\alpha\to 0$ (a tiny hole): $f\simeq-\frac{1}{2}\ln\alpha\to\infty$ and the fall is slowed down.
- Check against the official key: VF16.pdf gives the same profile, pressure, the form of $F$ with $f(\alpha)$ as the integral above, Newton's law, $\bar{h} = (1 + 2\tau)^{-1/2}$ and both criteria; the closed form of $f(\alpha)$ differs, as noted; the key does not write $Q(t)$.
