---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 5"
dificultad: media
id: "e5"
pill: "Bead on Wire • Arc-Length Kinetic Energy"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.5: Particle on a Curved Wire

> Official exercise 5 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

For the functions $V(x)$ in parts (i) and (ii) of the previous exercise, write down the kinetic energy of a particle of unit mass moving on a wire whose height as a function of $x$ is $V(x)$. Working in physical units for which the acceleration of gravity is $g = 1$, write down the total energy, and hence derive the second order differential equation satisfied by $x$. Write down a coupled system of equations for $x$ and $y = \dot x$, and sketch the phase portrait.

## Setting up the system

First, we express the speed of the bead along the wire in terms of $x$ and $\dot x$, build the total mechanical energy $E$, and differentiate $E(t) = \text{const}$ to obtain the equation of motion and its equivalent first-order system.

A particle constrained to move without friction on a planar wire of height $z = V(x)$ has position vector $\mathbf r(t) = \bigl(x(t),\, V(x(t))\bigr)$. Differentiating the vertical coordinate $z(t) = V(x(t))$ with respect to time $t$ by the chain rule gives

$$ \dot z = \frac{d}{dt}\bigl[V(x(t))\bigr] = V'(x)\,\dot x. $$

The squared speed along the wire is therefore

$$ v^2 = \dot x^2 + \dot z^2 = \dot x^2 + \bigl[V'(x)\bigr]^2 \dot x^2 = \Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\dot x^2. $$

For a particle of unit mass ($m = 1$) in units where $g = 1$, the kinetic energy $T = \frac{1}{2}mv^2$ and gravitational potential energy $U = mgz$ are

$$ T = \frac{1}{2}\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\dot x^2, \qquad U = V(x), $$

so the total mechanical energy is

$$ E(x, \dot x) = T + U = \frac{1}{2}\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\dot x^2 + V(x). $$

Since the wire is frictionless and the constraint force is perpendicular to the velocity, $E$ is conserved along every trajectory: $\frac{dE}{dt} = 0$. We differentiate $E(x(t), \dot x(t))$ term by term using the product rule and the chain rule:

$$ \frac{dE}{dt} = \frac{1}{2}\frac{d}{dt}\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\cdot \dot x^2 + \frac{1}{2}\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\cdot \frac{d}{dt}(\dot x^2) + \frac{d}{dt}\bigl[V(x)\bigr]. $$

Evaluating each derivative explicitly:

- $\frac{d}{dt}\bigl(1 + [V'(x)]^2\bigr) = 2V'(x)\,V''(x)\,\dot x$, so the first term is $\frac{1}{2}\cdot 2V'(x)V''(x)\dot x \cdot \dot x^2 = V'(x)V''(x)\dot x^3$;
- $\frac{d}{dt}(\dot x^2) = 2\dot x\ddot x$, so the second term is $\frac{1}{2}\bigl(1 + [V'(x)]^2\bigr)\cdot 2\dot x\ddot x = \bigl(1 + [V'(x)]^2\bigr)\dot x\ddot x$;
- $\frac{d}{dt}[V(x)] = V'(x)\dot x$.

Combining the three terms and factoring out $\dot x$:

$$ \frac{dE}{dt} = \dot x\left[\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\ddot x + V'(x)V''(x)\dot x^2 + V'(x)\right] = \dot x\left[\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\ddot x + V'(x)\bigl(1 + V''(x)\dot x^2\bigr)\right] = 0. $$

On any time interval where the particle moves ($\dot x \neq 0$), the factor in brackets must vanish (and by continuity of $\ddot x$ it also vanishes at isolated turning points where $\dot x = 0$). Since $1 + [V'(x)]^2 \ge 1 > 0$ everywhere, we divide by $1 + [V'(x)]^2$ to obtain the general second-order ODE:

$$ \ddot x = -\frac{V'(x)\bigl(1 + V''(x)\dot x^2\bigr)}{1 + \bigl[V'(x)\bigr]^2}. $$

Introducing the phase-plane variable $y = \dot x$ converts this into the autonomous first-order system

$$ \dot x = f(x, y) = y, \qquad \dot y = g(x, y) = -\frac{V'(x)\bigl(1 + V''(x)y^2\bigr)}{1 + \bigl[V'(x)\bigr]^2}. $$

For the two potentials from Exercise 5.4:

- **Part (i):** $V(x) = \frac{1}{2}\omega^2 x^2$ ($\omega > 0$), so $V'(x) = \omega^2 x$ and $V''(x) = \omega^2$. The total energy and coupled system are

$$ E(x, y) = \frac{1}{2}\bigl(1 + \omega^4 x^2\bigr)y^2 + \frac{1}{2}\omega^2 x^2, $$

$$ \dot x = y, \qquad \dot y = -\frac{\omega^2 x\bigl(1 + \omega^2 y^2\bigr)}{1 + \omega^4 x^2}. $$

- **Part (ii):** $V(x) = \frac{1}{2}x^4 - x^2$, so $V'(x) = 2x^3 - 2x = 2x(x^2 - 1)$ and $V''(x) = 6x^2 - 2$. The total energy and coupled system are

$$ E(x, y) = \frac{1}{2}\Bigl(1 + 4x^2(x^2 - 1)^2\Bigr)y^2 + \frac{1}{2}x^4 - x^2, $$

$$ \dot x = y, \qquad \dot y = -\frac{2x(x^2 - 1)\bigl(1 + (6x^2 - 2)y^2\bigr)}{1 + 4x^2(x^2 - 1)^2}. $$

## Step 1: Critical points

Next, we find all equilibrium points by setting $\dot x = 0$ and $\dot y = 0$ simultaneously, which identifies the stationary positions of the bead on the wire.

Setting $f(x, y) = 0$ gives $y = 0$. Substituting $y = 0$ into $g(x, y) = 0$ yields

$$ -\frac{V'(x)\bigl(1 + V''(x)\cdot 0\bigr)}{1 + \bigl[V'(x)\bigr]^2} = -\frac{V'(x)}{1 + \bigl[V'(x)\bigr]^2} = 0 \iff V'(x) = 0. $$

Thus the equilibria are located at $(x^*, 0)$ where $x^*$ is a stationary point of the wire height $V(x)$ — the exact same critical points as in Exercise 5.4:

- **Part (i):** $V'(x) = \omega^2 x = 0 \implies x^* = 0$. Unique critical point: $(0, 0)$.
- **Part (ii):** $V'(x) = 2x(x^2 - 1) = 0 \implies x^* \in \{-1, 0, 1\}$. Three critical points: $(-1, 0)$, $(0, 0)$, and $(1, 0)$.

## Step 2: Linearization

We now compute the Jacobian matrix $J(x, y)$ by differentiating $f(x, y)$ and $g(x, y)$ explicitly and evaluate it at any equilibrium $(x^*, 0)$ where $V'(x^*) = 0$.

For $f(x, y) = y$, the partial derivatives are $\frac{\partial f}{\partial x} = 0$ and $\frac{\partial f}{\partial y} = 1$.

For $g(x, y) = -\frac{N(x, y)}{D(x)}$ with numerator $N(x, y) = V'(x)\bigl(1 + V''(x)y^2\bigr)$ and denominator $D(x) = 1 + [V'(x)]^2$:

- Partial derivative with respect to $x$ by the quotient rule:

$$ \frac{\partial g}{\partial x} = -\frac{\frac{\partial N}{\partial x}\,D(x) - N(x, y)\,D'(x)}{\bigl[D(x)\bigr]^2}, $$

where

$$ \frac{\partial N}{\partial x} = V''(x)\bigl(1 + V''(x)y^2\bigr) + V'(x)V'''(x)y^2, \qquad D'(x) = 2V'(x)V''(x). $$

Evaluating at any equilibrium $(x^*, 0)$, where $V'(x^*) = 0$ and $y = 0$: $N(x^*, 0) = 0$, $D(x^*) = 1 + 0 = 1$, $D'(x^*) = 0$, and $\frac{\partial N}{\partial x}(x^*, 0) = V''(x^*)$. Hence

$$ \frac{\partial g}{\partial x}(x^*, 0) = -\frac{V''(x^*)\cdot 1 - 0\cdot 0}{1^2} = -V''(x^*). $$

- Partial derivative with respect to $y$:

$$ \frac{\partial g}{\partial y} = -\frac{2V'(x)V''(x)y}{1 + \bigl[V'(x)\bigr]^2}. $$

Evaluating at $(x^*, 0)$ gives $\frac{\partial g}{\partial y}(x^*, 0) = 0$.

Therefore, at every equilibrium $(x^*, 0)$ of the curved-wire system, the Jacobian matrix is

$$ J(x^*, 0) = \begin{pmatrix} 0 & 1 \\ -V''(x^*) & 0 \end{pmatrix}. $$

This coincides identically with the Jacobian of the planar potential system $\ddot x = -V'(x)$ in Exercise 5.4, because the geometric factor $[V'(x)]^2$ and the curvature term $V'(x)V''(x)y^2$ are both quadratic or higher order in the perturbations $(x - x^*, y)$.

## Step 3: Local study

We now find the eigenvalues and eigenvectors of $J(x^*, 0)$ at each critical point and determine whether the linear classification persists in the full nonlinear system.

### Part (i): $V(x) = \frac{1}{2}\omega^2 x^2$ at $(0, 0)$

Here $V''(0) = \omega^2$, so

$$ J(0, 0) = \begin{pmatrix} 0 & 1 \\ -\omega^2 & 0 \end{pmatrix}. $$

Characteristic polynomial:

$$ \det\bigl(J(0, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ -\omega^2 & -\lambda \end{pmatrix} = \lambda^2 + \omega^2 = 0 \implies \lambda_\pm = \pm i\omega. $$

Linearization predicts a centre (non-hyperbolic, $\operatorname{Re}\lambda = 0$). To confirm it is a true nonlinear centre, observe that $E(x, y) = \frac{1}{2}(1 + \omega^4 x^2)y^2 + \frac{1}{2}\omega^2 x^2$ is conserved ($\dot E = 0$), satisfies $E(0, 0) = 0$, and satisfies $E(x, y) > 0$ for all $(x, y) \neq (0, 0)$. Hence every level curve $E(x, y) = c > 0$ is a closed loop enclosing $(0, 0)$, proving that $(0, 0)$ is a **global nonlinear centre**.

### Part (ii): $V(x) = \frac{1}{2}x^4 - x^2$

- **At $(0, 0)$:** $V''(0) = -2$, so

$$ J(0, 0) = \begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix}. $$

Characteristic polynomial:

$$ \det\bigl(J(0, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ 2 & -\lambda \end{pmatrix} = \lambda^2 - 2 = 0 \implies \lambda_1 = \sqrt{2}, \quad \lambda_2 = -\sqrt{2}. $$

Row-by-row eigenvectors:
- For $\lambda_1 = \sqrt{2}$: $(J - \sqrt{2}I)\mathbf v_1 = \begin{pmatrix} -\sqrt{2} & 1 \\ 2 & -\sqrt{2} \end{pmatrix}\begin{pmatrix} v_x \\ v_y \end{pmatrix} = \mathbf 0 \implies -\sqrt{2}\,v_x + v_y = 0 \implies \mathbf v_1 = \begin{pmatrix} 1 \\ \sqrt{2} \end{pmatrix}$ (unstable direction, slope $+\sqrt{2}$).
- For $\lambda_2 = -\sqrt{2}$: $(J + \sqrt{2}I)\mathbf v_2 = \begin{pmatrix} \sqrt{2} & 1 \\ 2 & \sqrt{2} \end{pmatrix}\begin{pmatrix} v_x \\ v_y \end{pmatrix} = \mathbf 0 \implies \sqrt{2}\,v_x + v_y = 0 \implies \mathbf v_2 = \begin{pmatrix} 1 \\ -\sqrt{2} \end{pmatrix}$ (stable direction, slope $-\sqrt{2}$).

Since $\lambda_1 > 0 > \lambda_2$, $(0, 0)$ is a hyperbolic **saddle**; by the Hartman–Grobman theorem, the nonlinear trajectories near $(0, 0)$ are tangent to $\mathbf v_1$ and $\mathbf v_2$.

- **At $(-1, 0)$ and $(1, 0)$:** $V''(\pm 1) = 6(\pm 1)^2 - 2 = 4$, so

$$ J(\pm 1, 0) = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}. $$

Characteristic polynomial:

$$ \det\bigl(J(\pm 1, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ -4 & -\lambda \end{pmatrix} = \lambda^2 + 4 = 0 \implies \lambda_\pm = \pm 2i. $$

Because $V(\pm 1) = -\frac{1}{2}$ is a strict local minimum of $V(x)$ and $\frac{1}{2}(1 + [V'(x)]^2)y^2 \ge 0$, the conserved energy $E(x, y)$ has a strict local minimum $E = -\frac{1}{2}$ at both $(-1, 0)$ and $(1, 0)$. Consequently, the level curves $E(x, y) = c$ for $-\frac{1}{2} < c < 0$ are nested closed loops around each minimum, proving that both $(-1, 0)$ and $(1, 0)$ are **nonlinear centres**.

## Step 4: Global picture

We now trace the global energy contours $E(x, y) = c$ and compare the geometry of the wire trajectories against the flat-potential orbits of Exercise 5.4.

In both parts, solving $E(x, y) = c$ for $y$ yields the exact orbit equation

$$ y = \pm\sqrt{\frac{2\bigl(c - V(x)\bigr)}{1 + \bigl[V'(x)\bigr]^2}}. $$

Since $\dot x = y$, every trajectory moves to the right in the upper half-plane ($y > 0$) and to the left in the lower half-plane ($y < 0$), so closed orbits run **clockwise**. The denominator $\sqrt{1 + [V'(x)]^2} \ge 1$ compresses $|y|$ relative to the flat-potential curve $y_{\text{flat}} = \pm\sqrt{2(c - V(x))}$ wherever the wire is steep ($|V'(x)|$ large), because part of the kinetic energy goes into the vertical velocity $\dot z = V'(x)y$.

- **Part (i) ($V(x) = \frac{1}{2}\omega^2 x^2$):** Every energy level $c > 0$ gives a closed periodic orbit oscillating between $x = -\frac{\sqrt{2c}}{\omega}$ and $x = +\frac{\sqrt{2c}}{\omega}$:

$$ y = \pm\sqrt{\frac{2c - \omega^2 x^2}{1 + \omega^4 x^2}}. $$

Near the origin ($|x| \ll \omega^{-2}$), the contours are ellipses, just like the harmonic oscillator. At large amplitudes ($c \gg \omega^{-2}$), the denominator $1 + \omega^4 x^2$ pinches the contours vertically along the flanks, flattening the maximum horizontal velocity $|y|$ compared to the ellipses of Exercise 5.4(i).

- **Part (ii) ($V(x) = \frac{1}{2}x^4 - x^2$):** The qualitative topology is a double-well figure-eight, controlled by the saddle energy $E(0, 0) = 0$:
  - $-\frac{1}{2} < E < 0$: two disjoint families of closed clockwise orbits trapped inside the left valley around $(-1, 0)$ and the right valley around $(1, 0)$.
  - $E = 0$: the **homoclinic separatrix** forming a figure-eight through the saddle $(0, 0)$, given explicitly by

$$ y = \pm\sqrt{\frac{2x^2 - x^4}{1 + 4x^2(x^2 - 1)^2}}, \qquad x \in [-\sqrt{2},\, \sqrt{2}], $$

crossing $(0, 0)$ with slopes $\pm\sqrt{2}$ and turning vertically at $x = \pm\sqrt{2}$ where $V(\pm\sqrt{2}) = 0$.
  - $E > 0$: large clockwise periodic orbits enclosing all three equilibria, flattened vertically where $|V'(x)| = |2x(x^2 - 1)|$ is large.

![[attachments/AM-PS/ch5-e5-ii.svg]]
*Phase portrait of the bead on the double-well wire $V(x) = \frac{1}{2}x^4 - x^2$ (Exercise 5.5(ii)). Centres at $(\pm 1, 0)$, saddle at $(0, 0)$ with slopes $\pm\sqrt{2}$, homoclinic separatrix $E = 0$ reaching $x = \pm\sqrt{2}$, and large periodic orbits for $E > 0$ pinched vertically where the wire slope $|V'(x)|$ is steep.*

## Answers and checks

Before summarizing, we verify the physical dimensions and the small-slope limiting case.

- **Dimensional check (SI units):** Restoring the gravitational acceleration $g$ ($\mathrm{m\,s^{-2}}$) and unit mass $m = 1\,\mathrm{kg}$, the wire height $z = V(x)$ has units of length ($\mathrm{m}$), so $V'(x) = dz/dx$ is dimensionless and $V''(x) = d^2z/dx^2$ has units of $\mathrm{m}^{-1}$. The restored energy $E = \frac{1}{2}m(1 + [V'(x)]^2)\dot x^2 + mgV(x)$ has units of $\mathrm{kg\cdot m^2\,s^{-2}} = \mathrm{J}$ in every term. The restored equation of motion is

$$ \ddot x = -\frac{V'(x)\bigl(g + V''(x)\dot x^2\bigr)}{1 + \bigl[V'(x)\bigr]^2}. $$

Here $[V''(x)\dot x^2] = \mathrm{m}^{-1}\cdot(\mathrm{m\,s^{-1}})^2 = \mathrm{m\,s^{-2}} = [g]$, the denominator $1 + [V'(x)]^2$ is dimensionless, and $V'(x)$ is dimensionless, so the right-hand side has units of $\mathrm{m\,s^{-2}} = [\ddot x]$.

- **Small-slope limit:** When the wire is nearly flat ($|V'(x)| \ll 1$) and the speed is modest ($|V''(x)\dot x^2| \ll 1$ in $g=1$ units), $1 + [V'(x)]^2 \approx 1$ and $1 + V''(x)\dot x^2 \approx 1$, so the equation reduces immediately to $\ddot x = -V'(x)$, recovering Exercise 5.4.

> [!result] Key results
> - **Total energy ($m = 1, g = 1$):** $E(x, y) = \frac{1}{2}\bigl(1 + [V'(x)]^2\bigr)y^2 + V(x)$.
> - **General ODE and system:** $\ddot x = -\dfrac{V'(x)(1 + V''(x)\dot x^2)}{1 + [V'(x)]^2}$, equivalent to $\dot x = y$, $\dot y = -\dfrac{V'(x)(1 + V''(x)y^2)}{1 + [V'(x)]^2}$.
> - **Part (i) ($V = \frac{1}{2}\omega^2 x^2$):** $\dot x = y$, $\dot y = -\dfrac{\omega^2 x(1 + \omega^2 y^2)}{1 + \omega^4 x^2}$. Unique equilibrium $(0, 0)$: global nonlinear centre ($\lambda = \pm i\omega$).
> - **Part (ii) ($V = \frac{1}{2}x^4 - x^2$):** $\dot x = y$, $\dot y = -\dfrac{2x(x^2-1)(1 + (6x^2-2)y^2)}{1 + 4x^2(x^2-1)^2}$. Saddle at $(0, 0)$ ($\lambda = \pm\sqrt{2}$, $\mathbf v_\pm = (1, \pm\sqrt{2})^T$); nonlinear centres at $(\pm 1, 0)$ ($\lambda = \pm 2i$); homoclinic separatrix $E = 0$ turning at $x = \pm\sqrt{2}$.
