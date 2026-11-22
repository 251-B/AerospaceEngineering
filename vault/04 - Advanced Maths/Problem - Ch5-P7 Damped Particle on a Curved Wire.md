---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 7"
dificultad: media
id: "e7"
pill: "Damped Wire • Qualitative Equivalence"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.7: Damped Particle on a Curved Wire

> Official exercise 7 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

A particle of unit mass moves on a wire whose height as a function of $x$ is $V(x)$, and is subject to an additional damping force $-k\dot x$. Write down the equation of motion, and show that the behavior of this system is qualitatively the same as that of $\ddot x = -V'(x) - k\dot x$.

## Setting up the system

First, we use the work-energy balance for a unit-mass particle ($m = 1, g = 1$) on the wire $z = V(x)$ under the horizontal damping force $-k\dot x$ ($k > 0$) to derive the equation of motion and its coupled first-order system.

From Exercise 5.5, the total mechanical energy of the bead on the wire $z = V(x)$ is

$$ E(x, \dot x) = \frac{1}{2}\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\dot x^2 + V(x). $$

The rate of change of mechanical energy equals the power delivered by the non-conservative damping force $F_d = -k\dot x$:

$$ \frac{dE}{dt} = F_d\,\dot x = -k\dot x^2. $$

Differentiating $E(x(t), \dot x(t))$ explicitly by the product and chain rules (exactly as in Exercise 5.5):

$$ \frac{dE}{dt} = \Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\dot x\ddot x + V'(x)V''(x)\dot x^3 + V'(x)\dot x. $$

Equating the two expressions for $\frac{dE}{dt}$:

$$ \dot x\left[\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\ddot x + V'(x)V''(x)\dot x^2 + V'(x)\right] = -k\dot x^2. $$

Rearranging all terms to the left-hand side and factoring out $\dot x$:

$$ \dot x\left[\Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\ddot x + V'(x)V''(x)\dot x^2 + V'(x) + k\dot x\right] = 0. $$

On any interval where $\dot x \neq 0$ (and by continuity at isolated points where $\dot x = 0$), the bracket vanishes, giving the second-order equation of motion:

$$ \Bigl(1 + \bigl[V'(x)\bigr]^2\Bigr)\ddot x + V'(x)V''(x)\dot x^2 + k\dot x + V'(x) = 0, $$

or, dividing by $1 + [V'(x)]^2 \ge 1 > 0$,

$$ \ddot x = -\frac{V'(x) + V'(x)V''(x)\dot x^2 + k\dot x}{1 + \bigl[V'(x)\bigr]^2}. $$

Setting $y = \dot x$ yields the coupled first-order system (which we call **System W** for the wire):

$$ \text{(W)} \qquad \dot x = f(x, y) = y, \qquad \dot y = g(x, y) = -\frac{V'(x) + V'(x)V''(x)y^2 + ky}{1 + \bigl[V'(x)\bigr]^2}. $$

We are asked to prove that System (W) is qualitatively equivalent to the flat damped-potential system (**System F**):

$$ \text{(F)} \qquad \dot x = y, \qquad \dot y = -V'(x) - ky. $$

## Step 1: Critical points

First, we show that Systems (W) and (F) have the exact same critical points in the phase plane.

For System (W), $\dot x = 0 \implies y = 0$. Substituting $y = 0$ into $\dot y = 0$ gives

$$ -\frac{V'(x) + 0 + 0}{1 + \bigl[V'(x)\bigr]^2} = 0 \iff V'(x) = 0. $$

For System (F), $\dot x = 0 \implies y = 0$, and $\dot y = 0 \implies -V'(x) = 0 \iff V'(x) = 0$.

Therefore, both systems share the **identical set of equilibria**: $(x^*, 0)$ where $V'(x^*) = 0$.

## Step 2: Linearization

Next, we compute the Jacobian matrix $J_W(x, y)$ of System (W) explicitly using the quotient rule and evaluate it at every equilibrium $(x^*, 0)$, showing that it coincides identically with the Jacobian $J_F(x^*, 0)$ of System (F).

Write $g(x, y) = -\frac{N(x, y)}{D(x)}$ where

$$ N(x, y) = V'(x) + V'(x)V''(x)y^2 + ky, \qquad D(x) = 1 + \bigl[V'(x)\bigr]^2. $$

We compute each partial derivative explicitly:

1. For $f(x, y) = y$: $\frac{\partial f}{\partial x} = 0$ and $\frac{\partial f}{\partial y} = 1$.
2. For $\frac{\partial g}{\partial x}$, apply the quotient rule:

$$ \frac{\partial g}{\partial x} = -\frac{\frac{\partial N}{\partial x}\,D(x) - N(x, y)\,D'(x)}{\bigl[D(x)\bigr]^2}, $$

where

$$ \frac{\partial N}{\partial x} = V''(x) + \Bigl(\bigl[V''(x)\bigr]^2 + V'(x)V'''(x)\Bigr)y^2, \qquad D'(x) = 2V'(x)V''(x). $$

Evaluating at any critical point $(x^*, 0)$ (where $V'(x^*) = 0$ and $y = 0$):
- $N(x^*, 0) = 0 + 0 + 0 = 0$,
- $D(x^*) = 1 + 0 = 1$,
- $D'(x^*) = 0$,
- $\frac{\partial N}{\partial x}(x^*, 0) = V''(x^*) + 0 = V''(x^*)$.

Hence

$$ \frac{\partial g}{\partial x}(x^*, 0) = -\frac{V''(x^*)\cdot 1 - 0\cdot 0}{1^2} = -V''(x^*). $$

3. For $\frac{\partial g}{\partial y}$, note that $D(x)$ does not depend on $y$:

$$ \frac{\partial g}{\partial y} = -\frac{2V'(x)V''(x)y + k}{1 + \bigl[V'(x)\bigr]^2}. $$

Evaluating at $(x^*, 0)$ (where $V'(x^*) = 0$ and $y = 0$):

$$ \frac{\partial g}{\partial y}(x^*, 0) = -\frac{0 + k}{1 + 0} = -k. $$

Assembling the Jacobian of System (W) at $(x^*, 0)$:

$$ J_W(x^*, 0) = \begin{pmatrix} 0 & 1 \\ -V''(x^*) & -k \end{pmatrix}. $$

Meanwhile, for System (F), $\frac{\partial}{\partial x}(-V'(x) - ky) = -V''(x)$ and $\frac{\partial}{\partial y}(-V'(x) - ky) = -k$, so

$$ J_F(x^*, 0) = \begin{pmatrix} 0 & 1 \\ -V''(x^*) & -k \end{pmatrix} = J_W(x^*, 0). $$

The two linearizations are **identical** at every equilibrium point.

## Step 3: Local study

Because $J_W(x^*, 0) = J_F(x^*, 0)$, both systems have the exact same characteristic equation, eigenvalues, and eigenvectors at every equilibrium $(x^*, 0)$:

$$ \det\bigl(J(x^*, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ -V''(x^*) & -k - \lambda \end{pmatrix} = \lambda^2 + k\lambda + V''(x^*) = 0, $$

$$ \lambda_\pm = \frac{-k \pm \sqrt{k^2 - 4V''(x^*)}}{2}. $$

For any $k > 0$ and any non-degenerate stationary point ($V''(x^*) \neq 0$), every equilibrium is **hyperbolic** ($\operatorname{Re}\lambda_\pm \neq 0$):

- **Local maximum of $V$ ($V''(x^*) < 0$):** $\sqrt{k^2 - 4V''(x^*)} > k$, so $\lambda_+ > 0 > \lambda_-$ — a **saddle** in both systems. Row 1 of $(J - \lambda_\pm I)\mathbf v_\pm = \mathbf 0$ reads $-\lambda_\pm v_x + v_y = 0 \implies \mathbf v_\pm = (1, \lambda_\pm)^T$, giving identical stable and unstable tangent slopes $\lambda_-$ and $\lambda_+$.
- **Local minimum of $V$ ($V''(x^*) > 0$):** both eigenvalues have strictly negative real part ($\operatorname{Re}\lambda_\pm < 0$):
  - $0 < k < 2\sqrt{V''(x^*)}$: **stable spiral** (underdamped);
  - $k = 2\sqrt{V''(x^*)}$: **stable improper node** (critically damped, $\lambda = -k/2$);
  - $k > 2\sqrt{V''(x^*)}$: **stable node** (overdamped).

By the Hartman–Grobman theorem, the local phase portraits of (W) and (F) around every non-degenerate equilibrium are topologically conjugate (identical type, stability, and tangent directions).

## Step 4: Global picture

To extend the equivalence from local neighbourhoods to the entire phase plane, we compare the global energy/Lyapunov structure and direction of flow of both systems.

1. **Identical energy dissipation law:** For System (W), $E_W(x, y) = \frac{1}{2}(1 + [V'(x)]^2)y^2 + V(x)$ satisfies $\dot E_W = -ky^2 \le 0$. For System (F), $E_F(x, y) = \frac{1}{2}y^2 + V(x)$ satisfies $\dot E_F = -ky^2 \le 0$. Both energy functions have the exact same critical points and strict local minima (the minima of $V(x)$ on $y = 0$), and both satisfy $E \to +\infty$ whenever $|y| \to \infty$ or $V(x) \to +\infty$.
2. **No periodic orbits and identical LaSalle invariance:** In both systems, $\dot E = 0$ if and only if $y = 0$. On the $x$-axis $y = 0$, the vertical acceleration is
   - in (W): $\dot y = -\frac{V'(x)}{1 + [V'(x)]^2}$,
   - in (F): $\dot y = -V'(x)$,
   which have the **exact same sign** everywhere (since $1 + [V'(x)]^2 \ge 1 > 0$) and vanish only at equilibria $V'(x^*) = 0$. Therefore, no non-equilibrium trajectory can stay on $y = 0$; $E(t)$ decreases strictly along every non-equilibrium orbit, ruling out limit cycles and homoclinic/heteroclinic loops in both systems.
3. **Same flow direction and basin structure:** In both systems $\dot x = y$ (motion to the right for $y > 0$, to the left for $y < 0$), and every bounded trajectory must converge to an equilibrium point (generically a local minimum of $V$, with the one-dimensional stable manifolds of the saddles separating the basins of attraction). The factor $1 + [V'(x)]^2$ in System (W) only compresses the horizontal speed $|y|$ geometrically where the wire is steep, without altering the number, type, stability, or connectivity of the equilibria.

Hence the global phase portrait of the damped bead on the wire (W) is **qualitatively identical** to that of the flat damped-potential system (F).

## Answers and checks

We verify the limiting cases and dimensional consistency of the equation of motion.

- **Undamped limit ($k \to 0^+$):** Setting $k = 0$ in System (W) gives $\dot y = -\frac{V'(x)(1 + V''(x)y^2)}{1 + [V'(x)]^2}$ and $\dot E_W = 0$, recovering Exercise 5.5 identically.
- **Small-slope limit ($|V'(x)| \ll 1$, $|V''(x)y^2| \ll 1$):** Setting $1 + [V'(x)]^2 \approx 1$ and neglecting $V'(x)V''(x)y^2$ reduces System (W) directly to System (F), $\ddot x = -V'(x) - k\dot x$.
- **Dimensional check (SI units):** Restoring $m = 1\,\mathrm{kg}$ and $g$ ($\mathrm{m\,s^{-2}}$), the damping constant $k$ has units of $\mathrm{s}^{-1}$ (since $F_d = -mk\dot x$ has units $\mathrm{kg\,m\,s^{-2}}$) and the restored ODE is

$$ \ddot x = -\frac{gV'(x) + V'(x)V''(x)\dot x^2 + k\dot x}{1 + \bigl[V'(x)\bigr]^2}. $$

Every term in the numerator has units of $\mathrm{m\,s^{-2}}$ ($[gV'] = \mathrm{m\,s^{-2}}$, $[V'V''\dot x^2] = 1\cdot\mathrm{m}^{-1}\cdot\mathrm{m^2\,s^{-2}} = \mathrm{m\,s^{-2}}$, $[k\dot x] = \mathrm{s}^{-1}\cdot\mathrm{m\,s^{-1}} = \mathrm{m\,s^{-2}}$), and the denominator is dimensionless, matching $[\ddot x] = \mathrm{m\,s^{-2}}$.

> [!result] Key results
> - **Equation of motion (damped bead on wire):** $\ddot x = -\dfrac{V'(x) + V'(x)V''(x)\dot x^2 + k\dot x}{1 + [V'(x)]^2}$, equivalent to $\dot x = y$, $\dot y = -\dfrac{V'(x) + V'(x)V''(x)y^2 + ky}{1 + [V'(x)]^2}$.
> - **Proof of qualitative equivalence with $\ddot x = -V'(x) - k\dot x$:**
>   1. **Identical equilibria:** $(x^*, 0)$ with $V'(x^*) = 0$.
>   2. **Identical Jacobian at every equilibrium:** $J_W(x^*, 0) = J_F(x^*, 0) = \begin{pmatrix} 0 & 1 \\ -V''(x^*) & -k \end{pmatrix}$, giving the same eigenvalues, eigenvectors, and local stability/type.
>   3. **Identical global Lyapunov dissipation:** $\dot E_W = -ky^2 \le 0$ and $\dot E_F = -ky^2 \le 0$, with $\dot y$ having the same sign on $y = 0$, ruling out periodic orbits and preserving the basin-of-attraction topology.
