---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 1"
dificultad: media
id: "e1"
pill: "Linearisation failure at a centre"
tags:
  - problema-resuelto
  - advanced-maths
  - nonlinear-systems
  - linearisation
  - polar-coordinates
  - centre
---

# Problem 5.1: Linearisation Failure at a Centre

> Official exercise 1 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

The linearized system may not give a qualitatively correct picture when the linearized equation produces a center, as this example demonstrates. First show that the origin is a center for the linearized version of the system $\dot x = -y + \lambda x(x^2 + y^2)$, $\dot y = x + \lambda y(x^2 + y^2)$. Write down the equation satisfied by $r$, where $r^2 = x^2 + y^2$, and show that the stability of the origin depends actually on the sign of $\lambda$. Draw the phase portrait for $\lambda < 0$.

## Model Classification and Stationary Points

The system is autonomous, two-dimensional and nonlinear (cubic terms). Write $\dot x = f(x,y)$, $\dot y = g(x,y)$ with

$$f(x,y) = -y + \lambda x(x^2+y^2), \qquad g(x,y) = x + \lambda y(x^2+y^2).$$

#### Stationary points

A stationary point solves $f = g = 0$. Multiply $f=0$ by $x$ and $g=0$ by $y$ and add:

$$x f + y g = -xy + \lambda x^2(x^2+y^2) + xy + \lambda y^2(x^2+y^2) = \lambda (x^2+y^2)^2 .$$

For $\lambda \neq 0$ this vanishes only at $x=y=0$. Multiply $f=0$ by $y$ and $g=0$ by $x$ and subtract:

$$x g - y f = x^2 + \lambda xy(x^2+y^2) + y^2 - \lambda xy(x^2+y^2) = x^2+y^2 ,$$

which vanishes only at the origin for every $\lambda$. Hence $(0,0)$ is the **only** stationary point, for any value of $\lambda$.

## Linearisation and Local Eigenvalues

Method: Jacobian at the stationary point, then trace and determinant (`Notes03-05-Nov_v2.pdf`, linearisation and classification; Robinson, Sec. 33).

#### Jacobian entries

$$\frac{\partial f}{\partial x} = \lambda (x^2+y^2) + 2\lambda x^2 = \lambda(3x^2+y^2), \qquad \frac{\partial f}{\partial y} = -1 + 2\lambda xy,$$

$$\frac{\partial g}{\partial x} = 1 + 2\lambda xy, \qquad \frac{\partial g}{\partial y} = \lambda (x^2+y^2) + 2\lambda y^2 = \lambda(x^2+3y^2).$$

At $(0,0)$ every term containing $\lambda$ vanishes:

$$J(0,0) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$

#### Trace, determinant, eigenvalues

$$\tau = \operatorname{tr}J = 0, \qquad \Delta = \det J = 0\cdot 0 - (-1)(1) = 1 > 0,$$

$$\mu^2 - \tau\mu + \Delta = \mu^2 + 1 = 0 \;\Longrightarrow\; \mu = \pm i .$$

Purely imaginary eigenvalues ($\tau = 0$, $\Delta > 0$) give a **centre** of the linearised system $\dot u = -v$, $\dot v = u$: circles $u^2+v^2=\text{const}$ traversed counter-clockwise (at $(u,v)=(1,0)$ the velocity is $(0,1)$). This is the borderline case of the linearisation theorem, so it **cannot** decide the stability of the nonlinear system: the cubic terms must be examined.

## Global Phase Portrait and Interpretation

#### Equation for $r$

Differentiate $r^2 = x^2+y^2$ with respect to $t$ using the chain rule, $\frac{d}{dt}(r^2) = 2r\dot r$:

$$2r\dot r = 2x\dot x + 2y\dot y = 2x\left[-y + \lambda x r^2\right] + 2y\left[x + \lambda y r^2\right].$$

Expand: $-2xy + 2\lambda x^2 r^2 + 2xy + 2\lambda y^2 r^2 = 2\lambda r^2 (x^2+y^2) = 2\lambda r^4$. Hence $2r\dot r = 2\lambda r^4$ and, for $r>0$,

$$\boxed{\dot r = \lambda r^3 .}$$

#### Equation for the angle

With $\theta = \arctan(y/x)$, $\dot\theta = \dfrac{x\dot y - y\dot x}{x^2+y^2}$. From the stationary-point computation $x\dot y - y\dot x = x g - y f = r^2$, so

$$\boxed{\dot\theta = 1,}$$

independent of $\lambda$: every orbit turns counter-clockwise at unit angular speed.

#### Solving $\dot r = \lambda r^3$

Separate variables, with $r(0)=r_0>0$:

$$\int_{r_0}^{r}\frac{d\rho}{\rho^3} = \lambda\int_0^t ds \;\Longrightarrow\; \left[-\frac{1}{2\rho^2}\right]_{r_0}^{r} = -\frac{1}{2r^2} + \frac{1}{2r_0^2} = \lambda t$$

(Barrow's rule with the limits written). Solving for $r$:

$$r(t) = \frac{r_0}{\sqrt{1 - 2\lambda r_0^2\, t}} .$$

### (i) $\lambda < 0$

Put $\lambda = -|\lambda|$: $r(t) = r_0/\sqrt{1 + 2|\lambda| r_0^2 t}$ is decreasing, and $r(t)\to 0$ like $(2|\lambda| t)^{-1/2}$ as $t\to\infty$ (algebraic, not exponential, decay: the linearisation has $\operatorname{Re}\mu=0$). With $\dot\theta=1$ the orbits are **inward counter-clockwise spirals**: the origin is an **asymptotically stable spiral** (a stable focus), not a centre.

### (ii) $\lambda > 0$

$r(t) = r_0/\sqrt{1 - 2\lambda r_0^2 t}$ grows and becomes infinite at the finite time $t^\ast = 1/(2\lambda r_0^2)$. Orbits are **outward counter-clockwise spirals**; the origin is an **unstable spiral**.

### (iii) $\lambda = 0$

$\dot r = 0$, $\dot\theta=1$: circles $r=r_0$, a genuine **centre**, stable but not asymptotically stable.

> [!result] Conclusion
> The linearisation is identical ($\mu=\pm i$) for all $\lambda$, but the nonlinear origin is asymptotically stable for $\lambda<0$, unstable for $\lambda>0$ and a centre only for $\lambda=0$. The sign of the cubic coefficient decides.

#### Dimensional and consistency check

$\lambda r^3$ has the units of $\dot r$, so $[\lambda] = [\mathrm{L}^{-2}\mathrm{T}^{-1}]$ if $r$ is a length and $t$ a time; the unit angular speed in $\dot\theta=1$ is $[\mathrm{T}^{-1}]$. Limit $\lambda\to0$: $r(t)\to r_0$, recovering the circles.

![[attachments/AM-PS/ch5-e1.svg]]
*Phase portrait for $\lambda<0$: counter-clockwise spirals winding into the origin (asymptotically stable focus), with $\dot r=\lambda r^3<0$ and $\dot\theta=1$.*
