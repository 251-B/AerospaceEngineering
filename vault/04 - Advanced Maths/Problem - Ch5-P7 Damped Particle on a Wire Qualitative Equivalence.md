---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 7"
dificultad: media
id: "e7"
pill: "Damped particle on a wire"
tags:
  - problema-resuelto
  - advanced-maths
  - phase-plane
  - damping
  - lagrange
---

# Problem 5.7: Damped Particle on a Wire, Qualitative Equivalence

> Official exercise 7 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

A particle of unit mass moves on a wire whose height as a function of $x$ is $V(x)$, and is subject to an additional damping force $-k\dot x$. Write down the equation of motion, and show that the behavior of this system is qualitatively the same as that of $\ddot x = -V'(x) - k\dot x$.

## Equation of Motion and Energy Dissipation

**Kinematics.** The particle sits at $\mathbf r = (x, V(x))$ (unit gravity $g = 1$, height equals potential energy per unit mass). By the chain rule $\dot{\mathbf r} = (\dot x,\, V'(x)\dot x)$, so

$$|\dot{\mathbf r}|^2 = \bigl(1 + [V'(x)]^2\bigr)\dot x^2 .$$

**Lagrangian.** $L = T - U = \tfrac12\bigl(1 + [V']^2\bigr)\dot x^2 - V(x)$. The pieces of the Euler-Lagrange equation, using the product rule and the chain rule $\frac{d}{dt}[V'(x)]^2 = 2V'V''\dot x$:

$$\frac{\partial L}{\partial \dot x} = (1+[V']^2)\dot x, \qquad \frac{d}{dt}\frac{\partial L}{\partial \dot x} = (1+[V']^2)\ddot x + 2V'V''\dot x^2,$$

$$\frac{\partial L}{\partial x} = V'V''\dot x^2 - V' .$$

**Damping.** The generalised force of a force $\mathbf F$ is $Q = \mathbf F\cdot\partial\mathbf r/\partial x$, with $\partial\mathbf r/\partial x = (1, V')$.

- *Horizontal drag* $\mathbf F = (-k\dot x, 0)$ gives $Q = -k\dot x$ (the form of the statement).
- *Tangential drag* $\mathbf F = -k\dot{\mathbf r}$ gives $Q = -k\dot{\mathbf r}\cdot\partial\mathbf r/\partial x = -k(1+[V']^2)\dot x$.

Equation $\frac{d}{dt}\frac{\partial L}{\partial\dot x} - \frac{\partial L}{\partial x} = Q$ then reads, for horizontal drag,

$$\boxed{\bigl(1 + [V'(x)]^2\bigr)\ddot x + V'(x)V''(x)\,\dot x^2 = -V'(x) - k\dot x}$$

(for tangential drag the right-hand side is $-V' - k(1+[V']^2)\dot x$; the conclusion below is identical).

**Energy.** With $E = \tfrac12(1+[V']^2)\dot x^2 + V(x)$, the Euler-Lagrange equation multiplied by $\dot x$ gives

$$\frac{dE}{dt} = \dot x\,Q = -k\dot x^2 \le 0 \quad\text{(horizontal drag)}, \qquad -k(1+[V']^2)\dot x^2 \le 0 \quad\text{(tangential drag)}.$$

Source: Robinson, Sec. 34; `Notes03-05-Nov_v2.pdf`, conservative systems with damping.

## Stationary Points and Linearisation

With $y = \dot x$, solve the equation for $\dot y$:

$$\dot x = y, \qquad \dot y = \frac{-V'(x) - V'(x)V''(x)\,y^2 - ky}{1 + [V'(x)]^2} .$$

**Equilibria.** $y = 0$ and then $-V'(x)/(1+[V']^2) = 0$, i.e. $V'(x^*) = 0$. These are exactly the equilibria $(x^*, 0)$ of the reference system $\dot x = y,\ \dot y = -V'(x) - ky$.

**Jacobian at $(x^*, 0)$.** Write $\dot y = N(x,y)/D(x)$ with $N = -V' - V'V''y^2 - ky$ and $D = 1+[V']^2$. At the equilibrium $N = 0$, so the quotient rule $\partial_\bullet(N/D) = (\partial_\bullet N)/D - N\,\partial_\bullet D/D^2$ loses its second term, and

$$\frac{\partial N}{\partial x}\Big|_{(x^*,0)} = -V''(x^*) - \bigl(V'V''\bigr)'\,y^2\big|_{y=0} = -V''(x^*), \qquad \frac{\partial N}{\partial y}\Big|_{(x^*,0)} = -2V'V''y - k = -k, \qquad D(x^*) = 1 .$$

> [!info] Why $V'(x^*) = 0$ matters
> Away from equilibria, differentiating $\dot y$ keeps the $y^2$ and quotient-rule terms in $D(x) = 1 + [V'(x)]^2$. At an equilibrium $(x^*, 0)$, however, $V'(x^*) = 0$ and $y = 0$, so $N = 0$, $D(x^*) = 1$, and all extra terms drop out:

$$J_{\text{wire}} = \begin{pmatrix} 0 & 1 \\ -V''(x^*) & -k \end{pmatrix} = J_{\ddot x = -V' - k\dot x}.$$

The Jacobians coincide, so the eigenvalues $\lambda = \dfrac{-k \pm \sqrt{k^2 - 4V''(x^*)}}{2}$ coincide, and so does the type of each equilibrium: $V''(x^*) < 0$ saddle; $V''(x^*) > 0$ stable spiral for $k^2 < 4V''$, stable node for $k^2 > 4V''$. By the Hartman-Grobman theorem (hyperbolic cases) the local portraits are topologically equivalent. For tangential drag the lower-right entry is $-k(1+[V']^2)/(1+[V']^2) = -k$ for every $x$, giving the same matrix.

## Phase Portrait and Physical Interpretation

Both systems dissipate energy, $\dot E \le 0$, with $\dot E = 0$ only on $y = 0$, where $\dot y \ne 0$ unless $V' = 0$. By LaSalle's principle trajectories tend to equilibria, i.e. to the minima of $V$ (stable) while maxima of $V$ are saddles; the same wells, hills and basins appear in both. The only difference is the metric factor $1+[V']^2$ that distorts the time scale away from equilibria (the particle has to climb along an arc longer than $\Delta x$), which changes the shape of the orbits but not the topology of the portrait.

> [!result] Conclusion
> Both systems share: the same equilibria, the same linearisation at every equilibrium, the same sign of $\dot E$ and the same Lyapunov decay, hence the same qualitative phase portrait as $\ddot x = -V'(x) - k\dot x$.
