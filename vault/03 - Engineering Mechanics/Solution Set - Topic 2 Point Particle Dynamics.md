---
title: "Solution Set - Topic 2: Point Particle Dynamics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (4-Phase Methodology)"
language: "English"
tags:
  - solutions
  - point-particle-dynamics
---

# 📚 Topic 2: Point Particle Dynamics - Full Analytical Solutions

Exhaustive, step-by-step analytical solutions for all 10 solvable problems from Topic 2 (**Point Particle Dynamics**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every problem follows the mandatory 4-phase pedagogical methodology, with explicit justification prior to every equation, zero algebraic omissions, explicit derivative developments (product and chain rules), explicit integral evaluations (substitution, differentials, primitive functions, and Barrow's rule), rotation matrices, and dimensional verifications.

---

## 📌 Problem 10: Conservative Force and Potential I

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ moves along the $Ox$ axis subject to a position-dependent non-linear restoring force directed towards the origin.
* **Kinematic Degree of Freedom:** $1$ degree of freedom, parametrized by the Cartesian coordinate $x(t) \in \mathbb{R}$.
* **Hypotheses:**
  1. The motion is strictly one-dimensional along the $x$-axis.
  2. The particle is treated as an ideal point particle of constant mass $m$.
  3. No dissipative or frictional forces are present (conservative field).
* **Initial Conditions:** At time $t = 0$, the particle is released from rest at position $x(0) = -a$:
  $$ x(0) = -a, \qquad v(0) = \dot{x}(0) = 0 $$
* **Physical Parameters:**
  - $m$: Mass of the particle $[\text{kg}]$.
  - $c$: Positive force proportionality constant $[\text{N}\cdot\text{m}^{-3} = \text{kg}\cdot\text{s}^{-2}\cdot\text{m}^{-2}]$.
  - $a$: Initial displacement amplitude $[\text{m}]$ ($a > 0$).

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Reference Frame:** Let $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ be a fixed Cartesian inertial frame with origin at $O$.
* **Kinematics Vectors:**
  - Position: $\mathbf{r}(t) = x(t)\mathbf{i}$.
  - Velocity: $\mathbf{v}(t) = \dot{x}(t)\mathbf{i}$.
  - Acceleration: $\mathbf{a}(t) = \ddot{x}(t)\mathbf{i}$.
* **Force Vector:**
  $$ \mathbf{F}(x) = -c x^3\mathbf{i} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Calculation of the Potential Energy Function $V(x)$
* **Pedagogical Justification:** In a one-dimensional problem where the force depends exclusively on position $x$, the force field is automatically irrotational (curl is trivially zero in 1D) and conservative. By definition of a conservative force (Notes.pdf Section 4.4, Eqs. 4.14–4.16), the work done by the force corresponds to the negative variation of potential energy, $\mathbf{F} = -\boldsymbol{\nabla} V = -\frac{dV}{dx}\mathbf{i}$. Integrating this relation allows us to replace the second-order nonlinear differential equation $m\ddot{x} + cx^3 = 0$ with an algebraic energy conservation law (first integral of motion).

We define the scalar potential energy $V(x)$ by choosing the reference datum $V(0) = 0$ at the origin:
$$ V(x) - V(0) = -\int_{0}^{x} F_x(x')\,dx' $$
Substitute $F_x(x') = -c x'^3$:
$$ V(x) = -\int_{0}^{x} (-c x'^3)\,dx' = c \int_{0}^{x} x'^3\,dx' $$
Evaluating the definite integral by the Fundamental Theorem of Calculus:
$$ V(x) = c \left[ \frac{x'^4}{4} \right]_0^x = \frac{1}{4}c x^4 $$

#### 2. Evaluation of the Total Mechanical Energy $E$
* **Pedagogical Justification:** Since no non-conservative forces act on the particle, the total mechanical energy $E = T + V(x)$ is an invariant of the motion ($dE/dt = 0$). Evaluating $E$ at the initial release state determines the accessible energy surface for all subsequent times.

At $t = 0$, with $x(0) = -a$ and $v(0) = 0$:
$$ T(0) = \frac{1}{2}m [v(0)]^2 = 0 $$
$$ V(-a) = \frac{1}{4}c (-a)^4 = \frac{1}{4}c a^4 $$
Therefore, the total mechanical energy is:
$$ E = T(0) + V(-a) = \frac{1}{4}c a^4 $$

#### 3. Particle Velocity at $x = 0$
* **Pedagogical Justification:** Conservation of mechanical energy equates the initial potential energy to the sum of kinetic and potential energies at any point $x$. At the origin $x = 0$, the potential energy reaches its absolute minimum $V(0) = 0$, meaning the kinetic energy $T$ is maximized.

Applying conservation of mechanical energy at $x = 0$:
$$ E = T(0) + V(0) \implies \frac{1}{4}c a^4 = \frac{1}{2}m v_0^2 + \frac{1}{4}c(0)^4 $$
$$ \frac{1}{2}m v_0^2 = \frac{1}{4}c a^4 $$
Isolate $v_0^2$:
$$ v_0^2 = \frac{2}{m}\left(\frac{1}{4}c a^4\right) = \frac{c a^4}{2m} $$
Taking the square root:
$$ |v_0| = \sqrt{\frac{c a^4}{2m}} = a^2 \sqrt{\frac{c}{2m}} $$
Direction of motion: Since the particle was released at $x = -a < 0$, the force acting on it for all $x < 0$ is:
$$ F_x = -c x^3 = -c(-|x|)^3 = +c|x|^3 > 0 $$
Because the force is strictly directed along $+\mathbf{i}$, the particle accelerates towards the right. Consequently, upon reaching $x = 0$, its velocity is directed in the positive direction:
$$ \mathbf{v}(0) = a^2 \sqrt{\frac{c}{2m}}\,\mathbf{i} $$

#### 4. Subsequent Stopping Point
* **Pedagogical Justification:** A particle stops momentarily when its velocity vanishes, $v = 0$, which corresponds to a classical turning point where the kinetic energy $T = 0$. By energy conservation, this requires $V(x_{stop}) = E$.

Set kinetic energy to zero:
$$ T = 0 \implies V(x_{stop}) = E $$
$$ \frac{1}{4}c x_{stop}^4 = \frac{1}{4}c a^4 $$
Dividing both sides by the non-zero constant $\frac{1}{4}c$:
$$ x_{stop}^4 = a^4 \implies x_{stop}^4 - a^4 = 0 $$
Factorizing as a difference of squares:
$$ (x_{stop}^2 - a^2)(x_{stop}^2 + a^2) = (x_{stop} - a)(x_{stop} + a)(x_{stop}^2 + a^2) = 0 $$
Since $x_{stop} \in \mathbb{R}$, $x_{stop}^2 + a^2 > 0$, yielding two real solutions:
$$ x_{stop} = -a \quad \text{or} \quad x_{stop} = +a $$
Since the motion started at $x = -a$ and proceeded across $x = 0$ in the $+x$ direction, the *subsequent* stopping point is:
$$ x_{stop} = +a $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Symmetry & Anharmonic Oscillation:** The potential $V(x) = \frac{1}{4}c x^4$ is strictly even ($V(-x) = V(x)$) and convex ($V''(x) = 3cx^2 \ge 0$). The particle is trapped in a symmetric potential well, executing periodic, bounded, anharmonic oscillations between $x = -a$ and $x = +a$.
* **Dimensional Analysis:**
  - $[c] = \text{N}/\text{m}^3 = \text{kg}\cdot\text{m}\cdot\text{s}^{-2}\cdot\text{m}^{-3} = \text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-2}$.
  - $[v_0] = [a^2] \sqrt{[c]/[m]} = \text{m}^2 \sqrt{\frac{\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-2}}{\text{kg}}} = \text{m}^2 \sqrt{\text{m}^{-2}\cdot\text{s}^{-2}} = \text{m}^2 \cdot \text{m}^{-1}\cdot\text{s}^{-1} = \text{m}/\text{s}$.
  The velocity dimensions match perfectly.
* **Limit and numerical check:** the energy balance is dimensionally homogeneous, $[c\,a^4] = \text{N}\cdot\text{m}^{-3}\cdot\text{m}^4 = \text{J}$. For $a \to 0$ the release energy vanishes and $v_0 = a^2\sqrt{c/(2m)} \to 0$. An RK4 integration (step $10^{-4}$, $m = c = a = 1$ in SI) of $m\ddot{x} = -c x^3$ from $x = -1$ at rest gives $v = 0.707107\ \text{m/s}$ at $x = 0$ against $\sqrt{1/2} = 0.707107\ \text{m/s}$, and the next stop at $x = 0.99999999$ against $x_{stop} = +a = 1$.

---

## 📌 Problem 11: Conservative Force and Potential II

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A point particle of mass $m$ moves along the $Ox$ axis in a quartic potential landscape $V(x) = -\frac{c}{2}(x^2 - a^2)^2$.
* **Degree of Freedom:** $1$ degree of freedom, $x(t) \in \mathbb{R}$.
* **Conservative Law:** No friction or external work ($W_{nc} = 0$), so $E = T + V(x) = \text{constant}$.
* **Physical Constraint:** Real physical motion requires real velocity, hence $T = \frac{1}{2}m v^2 \ge 0$. The classically allowed regions are restricted to:
  $$ \{x \in \mathbb{R} : V(x) \le E\} $$
* **Parameters:**
  - $c > 0$: Potential scale constant $[\text{J}/\text{m}^4 = \text{N}/\text{m}^3]$.
  - $a > 0$: Characteristic length $[\text{m}]$.

### Phase 2: Geometric Analysis & Landscape Topography of $V(x)$
* **Potential Expression:**
  $$ V(x) = -\frac{c}{2}(x^2 - a^2)^2 = -\frac{c}{2}(x^4 - 2a^2 x^2 + a^4) $$
* **Symmetry:**
  $$ V(-x) = -\frac{c}{2}((-x)^2 - a^2)^2 = -\frac{c}{2}(x^2 - a^2)^2 = V(x) \implies \text{Even function (symmetric about } x = 0). $$
* **Critical Points & Equilibrium Configurations:**
  *Pedagogical Justification:* Equilibrium points occur where the resultant force vanishes, $F(x) = -\frac{dV}{dx} = 0$.
  $$ \frac{dV}{dx} = -\frac{c}{2} \cdot 2(x^2 - a^2) \cdot (2x) = -2cx(x^2 - a^2) $$
  Setting $\frac{dV}{dx} = 0$ yields three critical points:
  $$ x_1 = 0, \qquad x_2 = +a, \qquad x_3 = -a $$
* **Stability Evaluation ($V''(x)$):**
  $$ V''(x) = \frac{d}{dx}[-2cx(x^2 - a^2)] = \frac{d}{dx}[-2cx^3 + 2ca^2 x] = -6cx^2 + 2ca^2 = 2c(a^2 - 3x^2) $$
  1. At $x = 0$:
     $$ V(0) = -\frac{c}{2}(0 - a^2)^2 = -\frac{1}{2}c a^4 $$
     $$ V''(0) = 2c(a^2 - 0) = +2ca^2 > 0 \implies \mathbf{Local\;Minimum} \text{ (Stable Equilibrium)} $$
  2. At $x = \pm a$:
     $$ V(\pm a) = -\frac{c}{2}(a^2 - a^2)^2 = 0 $$
     $$ V''(\pm a) = 2c(a^2 - 3a^2) = -4ca^2 < 0 \implies \mathbf{Local\;Maxima} \text{ (Unstable Equilibria / Potential Barriers)} $$
* **Asymptotic Limits:**
  $$ \lim_{x \to \pm \infty} V(x) = \lim_{x \to \pm \infty} \left[ -\frac{c}{2} x^4 \right] = -\infty $$

### Phase 3: Step-by-Step Mathematical Deduction & Motion Classification

* **Pedagogical Justification:** By examining the intersection of the horizontal energy line $E$ with the graph of $V(x)$, we locate the turning points ($V(x) = E$) and delineate the allowed intervals where $T = E - V(x) \ge 0$.

#### Case (a): $E > 0$
* **Energy Relation:** The maximum value attained by the potential is $V_{max} = V(\pm a) = 0$. Since $E > 0$, we have:
  $$ E > V(x), \qquad \forall x \in (-\infty, +\infty) $$
* **Turning Points:** The equation $V(x) = E$ has no real solutions because $-\frac{c}{2}(x^2 - a^2)^2 \le 0 < E$.
* **Kinetic Energy:**
  $$ T(x) = E - V(x) = E + \frac{c}{2}(x^2 - a^2)^2 > E > 0 $$
  The velocity never vanishes and never changes sign.
* **Type of Motion:** **Unbounded Motion.**
  - A particle entering from $-\infty$ moves towards $+x$, accelerates as it enters the central region, passes through the barriers at $x = -a$ and $x = +a$ with speed $v \ge \sqrt{2E/m}$, and continues indefinitely to $+\infty$.
  - Symmetrically, a particle entering from $+\infty$ with $v < 0$ traverses the entire axis to $-\infty$.

#### Case (b): $E < -\frac{1}{2}c a^4$
* **Energy Relation:** The energy is strictly below the local minimum at the origin, $E < V(0) = -\frac{1}{2}c a^4$.
* **Central Region:** For $|x| \le a$, the minimum of the potential is $V(0) = -\frac{1}{2}c a^4 > E$. Therefore, in the central region:
  $$ T(x) = E - V(x) < 0 $$
  which is classically forbidden. The particle can **never** enter the region between the outer turning points.
* **Outer Turning Points:** Since $V(x) \to -\infty$ as $|x| \to \infty$, the energy line $E$ intersects $V(x)$ at two points outside $[-a, a]$:
  $$ -\frac{c}{2}(x^2 - a^2)^2 = E \implies (x^2 - a^2)^2 = -\frac{2E}{c} = \frac{2|E|}{c} $$
  Taking the positive square root:
  $$ x^2 - a^2 = \sqrt{\frac{2|E|}{c}} \implies x^2 = a^2 + \sqrt{\frac{2|E|}{c}} $$
  $$ x_t = \pm \sqrt{a^2 + \sqrt{\frac{2|E|}{c}}} = \pm x_{out}, \qquad \text{with } x_{out} > a $$
* **Allowed Regions:** $x \in (-\infty, -x_{out}]$ and $x \in [+x_{out}, +\infty)$.
* **Type of Motion:** **Unbounded Motion with Reflection.**
  - If the particle begins at $+\infty$ heading left ($v < 0$), it decelerates as $V(x)$ increases, stops momentarily at $x = +x_{out}$ ($T = 0$), and is accelerated back towards $+\infty$ by the positive restoring force $F = -V'(x_{out}) > 0$.
  - Similarly, in the negative half-space, a particle from $-\infty$ reflects at $-x_{out}$ and returns to $-\infty$.

#### Case (c): $-\frac{1}{2}c a^4 < E < 0$
* **Energy Relation:** The energy level lies between the central local minimum and the two local maxima:
  $$ V(0) < E < V(\pm a) $$
* **Determination of Turning Points:**
  $$ -\frac{c}{2}(x^2 - a^2)^2 = E \implies (x^2 - a^2)^2 = \frac{2|E|}{c} $$
  Because $|E| < \frac{1}{2}c a^4$, we have $\sqrt{\frac{2|E|}{c}} < a^2$.
  This produces two distinct positive solutions for $x^2$:
  $$ x^2 = a^2 \pm \sqrt{\frac{2|E|}{c}} $$
  yielding four real turning points:
  $$ x_{in} = \sqrt{a^2 - \sqrt{\frac{2|E|}{c}}} \in (0, a) $$
  $$ x_{out} = \sqrt{a^2 + \sqrt{\frac{2|E|}{c}}} > a $$
  Ordered along the real axis:
  $$ -x_{out} < -x_{in} < 0 < x_{in} < x_{out} $$
* **Allowed Regions where $V(x) \le E$:**
  1. **Inner Well Region:** $x \in [-x_{in}, +x_{in}]$.
  2. **Outer Left Region:** $x \in (-\infty, -x_{out}]$.
  3. **Outer Right Region:** $x \in [+x_{out}, +\infty)$.
* **Type of Motion:**
  - **Bounded Oscillatory Motion:** If the particle is placed inside the central well $[-x_{in}, +x_{in}]$, it is permanently confined by the potential barriers. It oscillates back and forth periodically between $-x_{in}$ and $+x_{in}$ around the stable equilibrium $x = 0$.
  - **Unbounded Motion with Reflection:** If the particle begins in the outer regions ($|x| \ge x_{out}$), it approaches from $\pm\infty$, reaches the outer turning point $\pm x_{out}$, and is reflected back to $\pm\infty$.

### Phase 4: Physical Interpretation & Synthesis
* **Summary Table:**
  | Energy Range | Turning Points | Allowed Regions | Motion Description |
  | :--- | :--- | :--- | :--- |
  | **(a)** $E > 0$ | None | $(-\infty, +\infty)$ | Unbounded: traverses from $-\infty$ to $+\infty$ (or vice versa). |
  | **(b)** $E < -\frac{1}{2}ca^4$ | $\pm x_{out}$ | $(-\infty, -x_{out}] \cup [x_{out}, +\infty)$ | Unbounded with reflection at $\pm x_{out}$ back to $\pm\infty$. Inner well forbidden. |
  | **(c)** $-\frac{1}{2}ca^4 < E < 0$ | $\pm x_{in}, \pm x_{out}$ | $[-x_{in}, x_{in}]$ OR $\vert x \vert \ge x_{out}$ | Bounded periodic oscillation in well $[-x_{in}, x_{in}]$, OR reflection at $\pm x_{out}$ back to $\pm\infty$. |
* **Confirmation with UC3M Solution Keys:** The qualitative classification can be compared with the official solution key (Problems.pdf, Solution keys section).
* **Dimensional check:** $[c\,a^4] = (\text{J/m}^4)\,\text{m}^4 = \text{J}$, the same as $E$; $[2|E|/c] = \text{J}/(\text{J/m}^4) = \text{m}^4$, so $\sqrt{2|E|/c}$ is an area (m$^2$) and $x_{out} = \sqrt{a^2 + \sqrt{2|E|/c}}$ is a length.
* **Limiting energies (sympy):**
  - $E \to -\tfrac{1}{2}ca^4$ (bottom of the well): $x_{in}^2 = a^2 - \sqrt{2|E|/c} \to 0$ and $x_{out}^2 \to 2a^2$, so the inner region collapses to the stable point $x = 0$, where the small oscillations have $\omega^2 = V''(0)/m = 2ca^2/m$.
  - $E \to 0^-$ (top of the barriers): $x_{in}, x_{out} \to a$, the four turning points merge pairwise at the unstable equilibria $x = \pm a$ (separatrix between cases (c) and (a)).

---

## 📌 Problem 12: Conservative Force and Potential III

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ undergoes one-dimensional bounded periodic motion under a conservative potential $V(x)$ between two consecutive turning points $x_1$ and $x_2$.
* **General Energy Law:** Total mechanical energy $E = T + V(x)$ is conserved.
* **Turning Point Conditions:** At the extremities $x = x_1$ and $x = x_2$, the particle comes to rest:
  $$ v(x_1) = v(x_2) = 0 \implies E = V(x_1) = V(x_2) $$
* **Specific Potential Model:**
  $$ V(x) = \frac{1}{2}m \omega_0^2(x^2 - b x^4) $$
  where $\omega_0$ is the natural small-amplitude frequency $[\text{rad}/\text{s}]$, and $b$ is the non-linear anharmonicity parameter $[\text{m}^{-2}]$. Amplitude of oscillation is $a$ ($x_1 = -a, x_2 = +a$).

### Phase 2: Mathematical Framework of Quadratures
* **Kinematic Relation:**
  $$ v = \frac{dx}{dt} \implies dt = \frac{dx}{v} $$
* **Kinetic Energy Isolation:**
  $$ T = \frac{1}{2}m v^2 = E - V(x) \implies v^2 = \frac{2}{m}[E - V(x)] $$
  $$ v = \pm \sqrt{\frac{2}{m}[E - V(x)]} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. General Derivation of the Oscillation Period $\tau$
* **Pedagogical Justification:** Because the force is conservative, the equations of motion are invariant under time reversal ($t \to -t$). The time taken to travel forward from $x_1$ to $x_2$ with positive velocity $v = +\sqrt{\frac{2}{m}[E - V(x)]}$ is identical to the return time from $x_2$ to $x_1$ with negative velocity $v = -\sqrt{\frac{2}{m}[E - V(x)]}$. Therefore, the total period $\tau$ is exactly twice the half-period transit integral.

The differential time increment along the forward path is:
$$ dt = \frac{dx}{\sqrt{\frac{2}{m}[E - V(x)]}} = \sqrt{\frac{m}{2[E - V(x)]}}\,dx $$
Integrating from $x = x_1$ to $x = x_2$, the half-period is:
$$ \frac{\tau}{2} = \int_{x_1}^{x_2} \sqrt{\frac{m}{2[E - V(x)]}}\,dx $$
Since $x_2$ is a turning point, the total energy is precisely $E = V(x_2)$. Substituting $E = V(x_2)$:
$$ \tau = 2 \int_{x_1}^{x_2} \sqrt{\frac{m}{2[V(x_2) - V(x)]}}\,dx $$
This proves the general theorem. $\blacksquare$

#### 2. Application to the Anharmonic Potential $V(x) = \frac{1}{2}m\omega_0^2(x^2 - b x^4)$
* **Pedagogical Justification:** For symmetric oscillations of amplitude $a$, the turning points are $x_1 = -a$ and $x_2 = +a$. We evaluate the energy difference $V(a) - V(x)$ algebraically and factor out the singular harmonic core $(a^2 - x^2)$.

Evaluate $V(a)$:
$$ V(a) = \frac{1}{2}m \omega_0^2(a^2 - b a^4) $$
Form the difference $V(a) - V(x)$:
$$ V(a) - V(x) = \frac{1}{2}m\omega_0^2(a^2 - b a^4) - \frac{1}{2}m\omega_0^2(x^2 - b x^4) $$
Factor out $\frac{1}{2}m\omega_0^2$:
$$ V(a) - V(x) = \frac{1}{2}m\omega_0^2 \left[ (a^2 - x^2) - b(a^4 - x^4) \right] $$
Apply the algebraic identity for difference of squares:
$$ a^4 - x^4 = (a^2 - x^2)(a^2 + x^2) $$
Substitute this identity into the bracketed term:
$$ V(a) - V(x) = \frac{1}{2}m\omega_0^2 \left[ (a^2 - x^2) - b(a^2 - x^2)(a^2 + x^2) \right] $$
Factor out the common term $(a^2 - x^2)$:
$$ V(a) - V(x) = \frac{1}{2}m\omega_0^2 (a^2 - x^2)\left[ 1 - b(a^2 + x^2) \right] $$

#### 3. Assembly of the Period Integral
Substitute this factorized expression into the denominator of the general period formula:
$$ 2[V(a) - V(x)] = 2 \left( \frac{1}{2}m\omega_0^2 (a^2 - x^2)\left[ 1 - b(a^2 + x^2) \right] \right) = m\omega_0^2 (a^2 - x^2)\left[ 1 - b(a^2 + x^2) \right] $$
Now take the square root of the ratio:
$$ \sqrt{\frac{m}{2[V(a) - V(x)]}} = \sqrt{\frac{m}{m\omega_0^2 (a^2 - x^2)[1 - b(a^2 + x^2)]}} = \frac{1}{\omega_0 \sqrt{a^2 - x^2}\sqrt{1 - b(a^2 + x^2)}} $$
Substitute this integrand into the period equation with limits from $-a$ to $+a$:
$$ \tau = 2 \int_{-a}^a \frac{dx}{\omega_0 \sqrt{a^2 - x^2}\sqrt{1 - b(a^2 + x^2)}} $$
Factor out the constant $\omega_0$:
$$ \tau = \frac{2}{\omega_0} \int_{-a}^a \frac{dx}{\sqrt{a^2 - x^2}\sqrt{1 - b(a^2 + x^2)}} $$
This completes the exact derivation. $\blacksquare$

### Phase 4: Physical Interpretation & Limiting Behaviors
* **Harmonic Limit ($b \to 0$):**
  When $b = 0$, the potential reduces to the simple harmonic oscillator $V(x) = \frac{1}{2}m\omega_0^2 x^2$.
  The integral becomes:
  $$ \tau = \frac{2}{\omega_0} \int_{-a}^a \frac{dx}{\sqrt{a^2 - x^2}} $$
  Using the trigonometric substitution $x = a\sin\theta$, $dx = a\cos\theta\,d\theta$, with limits $\theta \in [-\pi/2, \pi/2]$:
  $$ \int_{-a}^a \frac{dx}{\sqrt{a^2 - x^2}} = \int_{-\pi/2}^{\pi/2} \frac{a\cos\theta\,d\theta}{a\cos\theta} = \int_{-\pi/2}^{\pi/2} d\theta = [\theta]_{-\pi/2}^{\pi/2} = \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) = \pi $$
  Multiplying by $\frac{2}{\omega_0}$:
  $$ \tau = \frac{2\pi}{\omega_0} $$
  which recovers the classical harmonic period $\tau_0 = 2\pi/\omega_0$, completely independent of the amplitude $a$ (isochronism).
* **Anharmonicity ($b > 0$):**
  For a softening spring ($b > 0$), the factor $\sqrt{1 - b(a^2 + x^2)} < 1$, which makes the integrand strictly larger than in the harmonic case, proving that $\tau > \tau_0$ and that the period grows with amplitude $a$.
* **Dimensional check:** $[b] = \text{m}^{-2}$, so $b(a^2 + x^2)$ is dimensionless; $\int dx/\sqrt{a^2 - x^2}$ is dimensionless and $[\tau] = [1/\omega_0] = \text{s}$.
* **Small anharmonicity:** with $x = a\sin\varphi$, $dx = a\cos\varphi\,d\varphi$ the period reads $\tau = \dfrac{2}{\omega_0}\displaystyle\int_{-\pi/2}^{\pi/2}\frac{d\varphi}{\sqrt{1 - ba^2(1 + \sin^2\varphi)}}$. Expanding to first order in $ba^2$ and using $\langle\sin^2\varphi\rangle = 1/2$ gives $\tau \approx \dfrac{2\pi}{\omega_0}\left(1 + \dfrac{3}{4}ba^2\right)$.
* **Admissible amplitudes:** $V$ has its maximum at $x^2 = 1/(2b)$, so bounded oscillations require $a^2 < 1/(2b)$; as $a^2 \to 1/(2b)$ the factor $1 - b(a^2 + x^2)$ vanishes at the turning points and $\tau \to \infty$.
* **Numerical check ($\omega_0 = 1$, $b = 1$; quadrature against RK4 of $\ddot{x} = -x + 2bx^3$, step $10^{-4}$):**
  - $a = 0.1$: quadrature $6.3309$, RK4 $6.3312$, first-order estimate $6.3303$.
  - $a = 0.3$: quadrature $6.7592$, RK4 $6.7592$, estimate $6.7073$.
  - $a = 0.5$: quadrature $8.0086$, RK4 $8.0088$, estimate $7.4613$.
  - $a = 0.7$ (close to $1/\sqrt{2} = 0.7071$): quadrature $16.947$, RK4 $16.948$; the period grows without bound as $a \to 0.7071$ ($36.6$ at $a = 0.7071$ in the quadrature).

---

## 📌 Problem 13: Conservative Force and Potential IV

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ moves along the $Ox$ axis subject to the cubic potential energy function:
  $$ V(x) = mgx\left[ \left(\frac{x}{a}\right)^2 - 3 \right] = mg\left(\frac{x^3}{a^2} - 3x\right) $$
* **Initial Conditions:** Released at $t = 0$ from position $x_0 = a$ with initial velocity:
  $$ x(0) = a, \qquad v_0 = \dot{x}(0) = +\sqrt{8ga} $$
* **Provided Integration Formula:**
  $$ \int \frac{dy}{(y+1)\sqrt{2-y}} = -\frac{2}{\sqrt{3}}\text{arctanh}\left(\sqrt{\frac{2-y}{3}}\right) + C $$
* **Parameters:** $m > 0$ [kg], $g > 0$ [m/s$^2$], $a > 0$ [m].

### Phase 2: Geometric & Energy Landscape Setup
* **Dimensionless Coordinate:** Let $y(t) = \frac{x(t)}{a} \implies x(t) = a y(t)$, $\dot{x}(t) = a \dot{y}(t)$.
* **Potential Energy in Dimensionless Form:**
  $$ V(y) = mga(y^3 - 3y) $$
* **Extrema of $V(y)$:**
  $$ \frac{dV}{dy} = mga(3y^2 - 3) = 3mga(y^2 - 1) $$
  Setting $\frac{dV}{dy} = 0$:
  - At $y = +1$ ($x = a$): $V(1) = mga(1 - 3) = -2mga$.
    $\frac{d^2V}{dy^2}(1) = 6mga(1) = +6mga > 0 \implies$ **Local Minimum** (Stable equilibrium).
  - At $y = -1$ ($x = -a$): $V(-1) = mga(-1 + 3) = +2mga$.
    $\frac{d^2V}{dy^2}(-1) = -6mga < 0 \implies$ **Local Maximum** (Unstable equilibrium barrier).
* **Total Mechanical Energy $E$:**
  *Pedagogical Justification:* Evaluating the initial energy reveals whether the particle is trapped in the well or has enough kinetic energy to reach other critical points.
  $$ E = T(0) + V(x_0) = \frac{1}{2}m v_0^2 + V(a) $$
  $$ E = \frac{1}{2}m (8ga) + mga(1^3 - 3\cdot 1) = 4mga - 2mga = +2mga $$
  **Critical Analytical Discovery:** The total energy $E = +2mga$ is **identical** to the potential energy at the local maximum: $E = V(-a) = +2mga$.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Quadrature Formulation
* **Pedagogical Justification:** Conservation of mechanical energy $T + V = E$ gives a first-order separable differential equation for $y(t)$.
$$ \frac{1}{2}m \dot{x}^2 = E - V(x) = 2mga - mga(y^3 - 3y) = mga(2 + 3y - y^3) $$
Substitute $\dot{x} = a\dot{y}$:
$$ \frac{1}{2}m a^2 \dot{y}^2 = mga(2 + 3y - y^3) \implies \dot{y}^2 = \frac{2g}{a}(2 + 3y - y^3) $$

#### 2. Factorization of the Cubic Polynomial $P(y) = 2 + 3y - y^3$
Rewrite in descending powers:
$$ P(y) = -(y^3 - 3y - 2) $$
Test candidate roots of $y^3 - 3y - 2 = 0$:
- For $y = -1$: $(-1)^3 - 3(-1) - 2 = -1 + 3 - 2 = 0$. Thus $(y + 1)$ is a factor.
Perform polynomial long division of $y^3 - 3y - 2$ by $(y + 1)$:
$$ \frac{y^3 - 3y - 2}{y + 1} = y^2 - y - 2 = (y + 1)(y - 2) $$
Therefore:
$$ y^3 - 3y - 2 = (y + 1)^2(y - 2) $$
Substituting back into $P(y)$:
$$ P(y) = -(y + 1)^2(y - 2) = (y + 1)^2(2 - y) $$
Hence, the differential equation simplifies to:
$$ \dot{y}^2 = \frac{2g}{a}(y + 1)^2(2 - y) $$

#### 3. Stage 1: Forward Motion to the Turning Point ($0 \le t \le t_1$)
Initially, at $t = 0$, $y(0) = 1$ and $\dot{y}(0) = \frac{v_0}{a} = +\sqrt{\frac{8g}{a}} > 0$.
In the interval $y \in [1, 2]$, we have $y + 1 > 0$ and $2 - y \ge 0$.
Taking the positive square root:
$$ \dot{y} = +\sqrt{\frac{2g}{a}}\,(y + 1)\sqrt{2 - y} $$
Separating variables:
$$ \frac{dy}{(y + 1)\sqrt{2 - y}} = \sqrt{\frac{2g}{a}}\,dt $$
Integrate from $y = 1$ at $t = 0$ to $y(t)$:
$$ \int_{1}^{y(t)} \frac{dy}{(y + 1)\sqrt{2 - y}} = \sqrt{\frac{2g}{a}} \int_{0}^t dt' = \sqrt{\frac{2g}{a}}\,t $$
Apply the provided integral hint:
$$ \left[ -\frac{2}{\sqrt{3}}\text{arctanh}\left(\sqrt{\frac{2 - y}{3}}\right) \right]_1^{y(t)} = \sqrt{\frac{2g}{a}}\,t $$
Evaluate at the lower limit $y = 1$:
$$ \sqrt{\frac{2 - 1}{3}} = \frac{1}{\sqrt{3}} $$
$$ -\frac{2}{\sqrt{3}}\text{arctanh}\left(\sqrt{\frac{2 - y}{3}}\right) - \left( -\frac{2}{\sqrt{3}}\text{arctanh}\left(\frac{1}{\sqrt{3}}\right) \right) = \sqrt{\frac{2g}{a}}\,t $$
Multiply the entire equation by $-\frac{\sqrt{3}}{2}$:
$$ \text{arctanh}\left(\sqrt{\frac{2 - y}{3}}\right) - \text{arctanh}\left(\frac{1}{\sqrt{3}}\right) = -\frac{\sqrt{3}}{2}\sqrt{\frac{2g}{a}}\,t = -\sqrt{\frac{3g}{2a}}\,t $$
$$ \text{arctanh}\left(\sqrt{\frac{2 - y}{3}}\right) = -\sqrt{\frac{3g}{2a}}\,t + \text{arctanh}\left(\frac{1}{\sqrt{3}}\right) $$

#### 4. Turning Point at $y = 2$ ($x = 2a$)
The turning point occurs when $\dot{y} = 0$, which corresponds to $2 - y = 0 \implies y = 2$.
At $y = 2$, $\text{arctanh}(0) = 0$.
The time $t_1$ required to reach the turning point is:
$$ 0 = -\sqrt{\frac{3g}{2a}}\,t_1 + \text{arctanh}\left(\frac{1}{\sqrt{3}}\right) \implies t_1 = \sqrt{\frac{2a}{3g}}\text{arctanh}\left(\frac{1}{\sqrt{3}}\right) $$

#### 5. Stage 2: Reflected Motion towards the Barrier ($t > t_1$)
At $y = 2$, the force acting on the particle is:
$$ F_x(2a) = -\frac{dV}{dx}(2a) = -\frac{3mg}{a^2}(4a^2 - a^2) = -9mg < 0 $$
Because the force is strictly negative, the particle accelerates to the left, so for $t > t_1$, $\dot{y} < 0$:
$$ \dot{y} = -\sqrt{\frac{2g}{a}}\,(y + 1)\sqrt{2 - y} $$
Separating variables from the turning point $(y = 2, t = t_1)$ to $y(t)$:
$$ \int_{2}^{y(t)} \frac{dy}{(y + 1)\sqrt{2 - y}} = -\sqrt{\frac{2g}{a}} \int_{t_1}^t dt' = -\sqrt{\frac{2g}{a}}\,(t - t_1) $$
Using the integral formula and noting that at $y = 2$, $\text{arctanh}(0) = 0$:
$$ -\frac{2}{\sqrt{3}}\text{arctanh}\left(\sqrt{\frac{2 - y}{3}}\right) - 0 = -\sqrt{\frac{2g}{a}}\,(t - t_1) $$
Multiply by $-\frac{\sqrt{3}}{2}$:
$$ \text{arctanh}\left(\sqrt{\frac{2 - y}{3}}\right) = \sqrt{\frac{3g}{2a}}\,(t - t_1) = \sqrt{\frac{3g}{2a}}\,t - \sqrt{\frac{3g}{2a}}\,t_1 $$
Since $\sqrt{\frac{3g}{2a}}\,t_1 = \text{arctanh}\left(\frac{1}{\sqrt{3}}\right)$:
$$ \text{arctanh}\left(\sqrt{\frac{2 - y}{3}}\right) = \sqrt{\frac{3g}{2a}}\,t - \text{arctanh}\left(\frac{1}{\sqrt{3}}\right) $$

### Phase 4: Physical Interpretation & Asymptotic Limit
* **Asymptotic Behavior as $t \to \infty$:**
  As $t \to \infty$, the right-hand side approaches $+\infty$. Because $\text{arctanh}(u) \to +\infty$ as $u \to 1^-$:
  $$ \sqrt{\frac{2 - y}{3}} \to 1 \implies \frac{2 - y}{3} \to 1 \implies 2 - y \to 3 \implies y \to -1 $$
  Consequently, $x(t) = a y(t) \to -a$.
  The particle asymptotically approaches the unstable potential barrier at $x = -a$ over an infinite duration, never crossing it.
* **Maximum / Terminal Speed Verification:**
  During the return motion, the particle passes back through the potential minimum $x = a$ ($y = 1$), where its speed returns to its maximum value:
  $$ v = \sqrt{\frac{2}{m}[E - V(a)]} = \sqrt{\frac{2}{m}[2mga - (-2mga)]} = \sqrt{\frac{8mga}{m}} = \sqrt{8ga} $$
  which corresponds to the characteristic speed referenced in `Problems.pdf` page 72.
* **Dimensional check:** $[\dot{y}^2] = [2g/a] = \text{s}^{-2}$, the argument of $\text{arctanh}$ is dimensionless, and $[t_1] = \sqrt{[a]/[g]} = \text{s}$.
* **Numerical check (RK4, step $10^{-5}$, $g = a = 1$):** integrating $\ddot{y} = -(3g/a)(y^2 - 1)$ from $y = 1$, $\dot{y} = \sqrt{8g/a}$ gives the turning point $y = 2$ at $t = 0.53765\sqrt{a/g}$, in agreement with $t_1 = \sqrt{2a/(3g)}\,\text{arctanh}(1/\sqrt{3}) = 0.537646\sqrt{a/g}$, and $y(0.3) = 1.759553$ in agreement with the closed form $y = 2 - 3\tanh^2\left(\operatorname{arctanh}(1/\sqrt{3}) - \sqrt{3g/(2a)}\,t\right) = 1.759553$.

---

## 📌 Problem 14: Conservative Force and Potential V

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ moves along the $Ox$ axis under a position-dependent non-linear force:
  $$ \mathbf{F}(x) = mK x e^{x/a}\mathbf{i} $$
* **Initial State:** At $t = 0$, the particle starts from $x(0) = a$ with initial velocity directed towards the negative axis:
  $$ \mathbf{v}(0) = -v_0\mathbf{i} \implies \dot{x}(0) = -v_0 < 0 $$
* **Parameters:** $m > 0$ [kg], $K > 0$ [s$^{-2}$], $a > 0$ [m], $v_0 > 0$ [m/s].

### Phase 2: Frame & Potential Energy Derivation
* **Inertial Frame:** Fixed Cartesian frame $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$.
* **Potential Energy Calculation via Integration by Parts:**
  *Pedagogical Justification:* The force is 1D and depends only on $x$, so $\mathbf{F} = -\frac{dV}{dx}\mathbf{i}$. To find $V(x)$, we perform integration by parts on $\int x e^{x/a}\,dx$.
  $$ V(x) = -\int F(x)\,dx = -mK \int x e^{x/a}\,dx $$
  Let:
  $$ u = x \implies du = dx $$
  $$ dv = e^{x/a}\,dx \implies v = a e^{x/a} $$
  Applying the integration by parts formula $\int u\,dv = uv - \int v\,du$:
  $$ \int x e^{x/a}\,dx = a x e^{x/a} - \int a e^{x/a}\,dx = a x e^{x/a} - a^2 e^{x/a} = a^2 e^{x/a}\left(\frac{x}{a} - 1\right) $$
  Therefore:
  $$ V(x) = -mKa^2 e^{x/a}\left(\frac{x}{a} - 1\right) + C $$
  We choose the arbitrary integration constant $C = 0$ so that at the initial position $x = a$:
  $$ V(a) = -mKa^2 e^{1}(1 - 1) = 0 $$
  This normalizes the potential so that $V(a) = 0$.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Topography of the Potential $V(x)$
* First derivative:
  $$ \frac{dV}{dx} = -F(x) = -mK x e^{x/a} $$
  Setting $\frac{dV}{dx} = 0$ yields a single critical point at $x = 0$.
* Second derivative:
  $$ \frac{d^2V}{dx^2} = -mK \frac{d}{dx}(x e^{x/a}) = -mK\left(e^{x/a} + \frac{x}{a}e^{x/a}\right) = -mK e^{x/a}\left(1 + \frac{x}{a}\right) $$
  At $x = 0$:
  $$ \frac{d^2V}{dx^2}(0) = -mK(1) = -mK < 0 \implies \mathbf{Local\;Maximum} $$
  The value of the potential barrier at the origin is:
  $$ V_{max} = V(0) = -mKa^2 e^0 (0 - 1) = +mKa^2 $$
* Asymptotic behaviors:
  - As $x \to -\infty$: $e^{x/a} \to 0$, so $V(-\infty) = 0$.
  - As $x \to +\infty$: $-mKa^2 e^{x/a}(x/a - 1) \to -\infty$.

#### 2. Total Mechanical Energy $E$
Since $V(a) = 0$, the total energy of the particle is entirely kinetic at $t = 0$:
$$ E = T(0) + V(a) = \frac{1}{2}m v_0^2 + 0 = \frac{1}{2}m v_0^2 $$

#### 3. Determination of the Critical Velocity $v_{0,crit}$
* **Pedagogical Justification:** The particle is launched leftwards from $x = a > 0$ towards the barrier at $x = 0$. To reach the summit of the barrier at $x = 0$, its total mechanical energy must at least equal the barrier height $V(0)$:
$$ E = V(0) \implies \frac{1}{2}m v_{0,crit}^2 = mKa^2 $$
Multiplying by $2/m$:
$$ v_{0,crit}^2 = 2Ka^2 \implies v_{0,crit} = a\sqrt{2K} $$

#### 4. Classification of Motion Regimes
1. **Regime 1: $v_0 < a\sqrt{2K}$ ($E < V(0)$)**
   - The initial kinetic energy is insufficient to overcome the potential barrier at $x = 0$.
   - As the particle moves towards the origin, it decelerates because $F(x) = mK x e^{x/a} > 0$ for all $x > 0$.
   - The particle comes to a momentary stop at a turning point $x_{turn} \in (0, a)$, where $V(x_{turn}) = E$.
   - Since $F(x_{turn}) > 0$, it is accelerated back towards the positive direction, passes $x = a$, and accelerates indefinitely towards $+\infty$.
   - **Conclusion:** The particle decelerates before arriving at $x = 0$, stops, and moves towards $+\infty$.

2. **Regime 2: $v_0 = a\sqrt{2K}$ ($E = V(0)$)**
   - The particle has precisely the energy needed to reach the top of the barrier at $x = 0$.
   - Near $x = 0$, Taylor expanding the potential:
     $$ V(x) \approx V(0) + V'(0)x + \frac{1}{2}V''(0)x^2 = mKa^2 - \frac{1}{2}mK x^2 $$
     The velocity as a function of position is:
     $$ \dot{x} = -\sqrt{\frac{2}{m}[E - V(x)]} \approx -\sqrt{\frac{2}{m}\left[ mKa^2 - \left(mKa^2 - \frac{1}{2}mK x^2\right) \right]} = -\sqrt{K}\,x $$
     Separating variables to find the transit time to $x = 0$:
     $$ \int_{a}^{0} \frac{dx}{x} = -\sqrt{K}\int_0^t dt' \implies [\ln x]_a^0 = -\infty $$
   - **Conclusion:** The transit time diverges logarithmically. The particle takes **infinite time** to reach $x = 0$ (it asymptotically approaches $x = 0$ without ever reaching it).

3. **Regime 3: $v_0 > a\sqrt{2K}$ ($E > V(0)$)**
   - The initial energy exceeds the barrier height $V(0)$.
   - The particle reaches $x = 0$ with residual speed:
     $$ v(0) = \sqrt{\frac{2}{m}[E - V(0)]} = \sqrt{v_0^2 - 2Ka^2} > 0 $$
   - Upon crossing into $x < 0$, the force becomes negative ($F(x) = mK x e^{x/a} < 0$ for $x < 0$), accelerating the particle further to the left.
   - **Conclusion:** The particle crosses the origin and moves towards $-\infty$.

### Phase 4: Physical Interpretation & Verification
* Compare with the official solution key (Problems.pdf, Solution keys section):
  - If $v_0 > a\sqrt{2K}$, particle moves towards $-\infty$.
  - If $v_0 < a\sqrt{2K}$, particle moves towards $+\infty$ after decelerating before arriving to $x = 0$.
  - If $v_0 = a\sqrt{2K}$, particle takes infinite time to reach $x = 0$.
* Dimensional verification: $[v_{0,crit}] = [a]\sqrt{[K]} = \text{m}\cdot\sqrt{\text{s}^{-2}} = \text{m}/\text{s}$. Correct.
* **Dimensional check of the barrier:** $[mKa^2] = \text{kg}\cdot\text{s}^{-2}\cdot\text{m}^2 = \text{J}$, the same as $\tfrac{1}{2}mv_0^2$, so $v_0^2/(2Ka^2)$ is dimensionless and decides the regime.
* **Limits:** for $K \to 0$ the force vanishes, $v_{0,crit} \to 0$ and every $v_0 > 0$ crosses the origin (free particle); for $v_0 \gg a\sqrt{2K}$ the barrier is negligible, $v(0) \to v_0$.
* **Numerical check (RK4, step $10^{-4}$, $m = K = a = 1$, $v_{0,crit} = 1.41421$):** for $v_0 = 1.2$ the particle turns at $x = 0.60801$ (root of $-e^{x}(x - 1) = 0.72$ is $0.608007$) and returns to $+\infty$; for $v_0 = 1.6$ it crosses the origin and reaches $x = -6$ with $\dot{x} = -1.5891$, equal to $-\sqrt{2(E - V(-6))} = -1.5891$ from energy conservation.

---

## 📌 Problem 15: Stokes Drag and Terminal Velocity

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A solid sphere of radius $r$ and density $\rho_s$ falls vertically from rest through a quiescent fluid of density $\rho_0$ and dynamic viscosity $\mu$.
* **Forces Acting on the Sphere:**
  1. Gravity (Weight): $W = m g = \rho_s V g$, acting downwards.
  2. Buoyancy (Archimedes' Principle): $F_B = \rho_0 V g$, acting upwards.
  3. Stokes Viscous Drag: $F_D = 6\pi \mu r v$, acting upwards (opposing downward motion $v > 0$).
* **Geometric & Material Relations:**
  - Sphere volume: $V = \frac{4}{3}\pi r^3$.
  - Given sphere density: $\rho_s = 2\rho_0$.
  - Sphere mass: $m = \rho_s V = 2\rho_0 \left(\frac{4}{3}\pi r^3\right) = \frac{8}{3}\pi \rho_0 r^3$.
  - Fluid kinematic viscosity: $\nu = \frac{\mu}{\rho_0} \implies \mu = \rho_0 \nu$.
* **Initial Conditions:**
  $$ x(0) = 0, \qquad v(0) = \dot{x}(0) = 0 $$

### Phase 2: Coordinate Frame & Dynamic Formulation
* **Frame:** Fixed Cartesian frame with the vertical axis $Ox$ directed **downwards** along gravity.
* **Resultant Force:**
  $$ \sum F_x = W - F_B - F_D $$
  Substitute the expressions for each force:
  $$ W = \left(\frac{8}{3}\pi \rho_0 r^3\right) g $$
  $$ F_B = \rho_0 \left(\frac{4}{3}\pi r^3\right) g = \frac{4}{3}\pi \rho_0 r^3 g = \frac{1}{2} W $$
  $$ F_D = 6\pi \mu r \dot{x} = 6\pi (\rho_0 \nu) r \dot{x} $$
  Net buoyancy-corrected gravitational force:
  $$ W - F_B = \frac{8}{3}\pi \rho_0 r^3 g - \frac{4}{3}\pi \rho_0 r^3 g = \frac{4}{3}\pi \rho_0 r^3 g = \frac{1}{2}mg $$

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Derivation of the Equation of Motion
* **Pedagogical Justification:** Applying Newton's second law $\sum F_x = m\ddot{x}$ establishes a linear first-order ODE in velocity $v = \dot{x}$.
$$ m \ddot{x} = (W - F_B) - F_D $$
$$ \left(\frac{8}{3}\pi \rho_0 r^3\right) \ddot{x} = \frac{4}{3}\pi \rho_0 r^3 g - 6\pi \rho_0 \nu r \dot{x} $$
Divide both sides by $\frac{8}{3}\pi \rho_0 r^3$:
$$ \ddot{x} = \frac{\frac{4}{3}\pi \rho_0 r^3 g}{\frac{8}{3}\pi \rho_0 r^3} - \frac{6\pi \rho_0 \nu r}{\frac{8}{3}\pi \rho_0 r^3}\,\dot{x} $$
Simplify each fraction:
$$ \frac{\frac{4}{3}}{\frac{8}{3}} = \frac{1}{2} \implies \text{First term: } \frac{1}{2}g $$
$$ \frac{6\pi \rho_0 \nu r}{\frac{8}{3}\pi \rho_0 r^3} = 6 \cdot \frac{3}{8}\,\frac{\nu}{r^2} = \frac{18}{8}\,\frac{\nu}{r^2} = \frac{9\nu}{4r^2} $$
Therefore, the differential equation reads:
$$ \ddot{x} + \frac{9\nu}{4r^2}\,\dot{x} = \frac{1}{2}g $$
Multiplying through by $4r^2$:
$$ 4r^2 \ddot{x} + 9\nu \dot{x} = 2r^2 g $$
Compare with the official equation of motion in the official solution key (Problems.pdf, Solution keys section).

#### 2. Computation of Terminal Velocity $v_t$
* **Pedagogical Justification:** The terminal velocity is reached when the viscous drag balances the effective weight, so acceleration ceases ($\ddot{x} = 0$).
$$ 4r^2(0) + 9\nu v_t = 2r^2 g \implies v_t = \frac{2r^2 g}{9\nu} $$

#### 3. Analytical Integration for Velocity $v(t)$
Let $\gamma = \frac{9\nu}{4r^2}$ be the characteristic inverse relaxation time ($[\gamma] = \text{s}^{-1}$).
The ODE becomes:
$$ \dot{v} + \gamma v = \frac{1}{2}g = \gamma v_t $$
$$ \frac{dv}{dt} = -\gamma(v - v_t) \implies \frac{dv}{v - v_t} = -\gamma\,dt $$
Integrate with initial condition $v(0) = 0$:
$$ \int_{0}^{v(t)} \frac{dv'}{v' - v_t} = -\gamma \int_{0}^t dt' $$
$$ \left[ \ln|v' - v_t| \right]_0^{v(t)} = -\gamma t $$
$$ \ln\left(\frac{v_t - v(t)}{v_t}\right) = -\gamma t $$
Exponentiate both sides:
$$ 1 - \frac{v(t)}{v_t} = e^{-\gamma t} \implies v(t) = v_t\left(1 - e^{-\gamma t}\right) $$

#### 4. Analytical Integration for Position $x(t)$
* **Pedagogical Justification:** Position is the direct integral of velocity over time, $x(t) = \int_0^t v(t')\,dt'$ with $x(0) = 0$.
$$ x(t) = \int_{0}^t v_t\left(1 - e^{-\gamma t'}\right)dt' = v_t \left[ t' + \frac{1}{\gamma}e^{-\gamma t'} \right]_0^t $$
Evaluate at upper and lower limits:
$$ x(t) = v_t \left( t + \frac{1}{\gamma}e^{-\gamma t} - \left(0 + \frac{1}{\gamma}\right) \right) = v_t \left( t - \frac{1}{\gamma} + \frac{1}{\gamma}e^{-\gamma t} \right) $$
Factor out $\frac{1}{\gamma}$:
$$ x(t) = \frac{v_t}{\gamma}\left[ \gamma t - 1 + e^{-\gamma t} \right] $$
Now substitute $v_t = \frac{2r^2 g}{9\nu}$ and $\gamma = \frac{9\nu}{4r^2}$:
$$ \frac{v_t}{\gamma} = \frac{\frac{2r^2 g}{9\nu}}{\frac{9\nu}{4r^2}} = \frac{2r^2 g}{9\nu} \cdot \frac{4r^2}{9\nu} = \frac{8r^4 g}{81\nu^2} $$
Rewrite $\frac{v_t}{\gamma}[\gamma t - 1 + e^{-\gamma t}]$:
$$ x(t) = \frac{8r^4 g}{81\nu^2}\left[ \frac{9\nu}{4r^2}t - 1 + e^{-\frac{9\nu}{4r^2}t} \right] $$
Multiply the inside by $4r^2$ and divide the outside prefactor by $4r^2$:
$$ \frac{8r^4 g}{81\nu^2} = \frac{2r^2 g}{81\nu^2} \cdot 4r^2 $$
$$ x(t) = \frac{2r^2 g}{81\nu^2}\left[ 4r^2\left(\frac{9\nu}{4r^2}t\right) - 4r^2 + 4r^2 e^{-\frac{9\nu}{4r^2}t} \right] $$
$$ x(t) = \frac{2r^2 g}{81\nu^2}\left[ -4r^2 + 4r^2\exp\left(-\frac{9\nu}{4r^2}t\right) + 9\nu t \right] $$
Compare with the closed-form solution in the official solution key (Problems.pdf, Solution keys section).

### Phase 4: Physical Interpretation & Limiting Cases
* **Short Times ($t \ll \gamma^{-1}$):**
  Expand the exponential $e^{-\gamma t} \approx 1 - \gamma t + \frac{1}{2}\gamma^2 t^2$:
  $$ x(t) = \frac{v_t}{\gamma}\left[ \gamma t - 1 + \left(1 - \gamma t + \frac{1}{2}\gamma^2 t^2\right) \right] = \frac{v_t}{\gamma}\left(\frac{1}{2}\gamma^2 t^2\right) = \frac{1}{2}(\gamma v_t)t^2 = \frac{1}{2}\left(\frac{1}{2}g\right)t^2 = \frac{1}{4}gt^2 $$
  This corresponds to free fall under effective gravity $g_{eff} = g(1 - \rho_0/\rho_s) = g/2$.
* **Long Times ($t \gg \gamma^{-1}$):**
  The exponential term decays to zero:
  $$ x(t) \approx v_t t - \frac{v_t}{\gamma} $$
  The sphere reaches uniform terminal descent at speed $v_t$ with an apparent positional offset $\Delta x = v_t/\gamma$.
* **Dimensional Verification:**
  $[v_t] = [r^2 g / \nu] = \frac{\text{m}^2 \cdot \text{m}\cdot\text{s}^{-2}}{\text{m}^2\cdot\text{s}^{-1}} = \text{m}/\text{s}$. Correct.

---

## 📌 Problem 16: Drag on Falling Football

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A football of mass $m$, frontal cross-sectional area $S$, and aerodynamic drag coefficient $C_D$ falls vertically through air of density $\rho$.
* **Forces:**
  1. Gravity: $W = mg$ downwards.
  2. Aerodynamic Quadratic Drag: $D = \frac{1}{2}\rho v^2 S C_D$ upwards (opposing downward velocity $v > 0$).
* **Initial Conditions:** Released from rest at the coordinate origin:
  $$ s(0) = 0, \qquad v(0) = 0 $$
* **Provided Integration Identities:**
  $$ \int \frac{dx}{x_0^2 - x^2} = \frac{1}{x_0}\text{atanh}\left(\frac{x}{x_0}\right), \qquad \int \tanh x\,dx = \ln\cosh x $$

### Phase 2: Coordinate Frame & Dynamic Formulation
* **Frame:** Fixed inertial frame with axis $Os$ pointing vertically downwards.
* **Equation of Motion:**
  $$ m \frac{dv}{dt} = mg - \frac{1}{2}\rho S C_D v^2 $$

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Terminal Velocity $v_t$
* **Pedagogical Justification:** When drag equals weight, the net vertical force is zero, producing steady downward descent at constant terminal velocity $v_t$.
$$ mg = \frac{1}{2}\rho S C_D v_t^2 \implies v_t = \sqrt{\frac{2mg}{\rho S C_D}} $$

#### 2. Velocity Evolution $v(t)$
* **Pedagogical Justification:** Expressing the drag parameter in terms of $v_t$ simplifies the differential equation and allows direct integration via the inverse hyperbolic tangent.
From the terminal velocity relation:
$$ \frac{1}{2}\rho S C_D = \frac{mg}{v_t^2} $$
Substitute this into the equation of motion:
$$ m \frac{dv}{dt} = mg - \frac{mg}{v_t^2} v^2 = mg \left(1 - \frac{v^2}{v_t^2}\right) = \frac{mg}{v_t^2}(v_t^2 - v^2) $$
Divide by $m$:
$$ \frac{dv}{dt} = \frac{g}{v_t^2}(v_t^2 - v^2) $$
Separate variables:
$$ \frac{dv}{v_t^2 - v^2} = \frac{g}{v_t^2}\,dt $$
Integrate from $v = 0$ at $t = 0$ to $v(t)$:
$$ \int_{0}^{v(t)} \frac{dv'}{v_t^2 - v'^2} = \frac{g}{v_t^2} \int_{0}^t dt' $$
Apply the provided integral identity $\int \frac{dv'}{v_t^2 - v'^2} = \frac{1}{v_t}\text{atanh}\left(\frac{v'}{v_t}\right)$:
$$ \left[ \frac{1}{v_t}\text{atanh}\left(\frac{v'}{v_t}\right) \right]_0^{v(t)} = \frac{g}{v_t^2}\,t $$
Since $\text{atanh}(0) = 0$:
$$ \frac{1}{v_t}\text{atanh}\left(\frac{v(t)}{v_t}\right) = \frac{g}{v_t^2}\,t \implies \text{atanh}\left(\frac{v(t)}{v_t}\right) = \frac{gt}{v_t} $$
Take the hyperbolic tangent of both sides:
$$ v(t) = v_t \tanh\left(\frac{gt}{v_t}\right) $$

#### 3. Position Evolution $s(t)$
* **Pedagogical Justification:** Position is found by integrating velocity over time, using the change of variable $u = \frac{gt'}{v_t}$ and the provided integral identity for $\tanh u$.
$$ s(t) = \int_{0}^t v(t')\,dt' = \int_{0}^t v_t \tanh\left(\frac{gt'}{v_t}\right)dt' $$
Change of variable:
$$ u = \frac{gt'}{v_t} \implies du = \frac{g}{v_t}\,dt' \implies dt' = \frac{v_t}{g}\,du $$
Limits: at $t' = 0$, $u = 0$; at $t' = t$, $u = \frac{gt}{v_t}$.
$$ s(t) = v_t \cdot \frac{v_t}{g} \int_{0}^{gt/v_t} \tanh u\,du = \frac{v_t^2}{g} [\ln\cosh u]_0^{gt/v_t} $$
Since $\cosh(0) = 1$ and $\ln(1) = 0$:
$$ s(t) = \frac{v_t^2}{g} \ln\left[ \cosh\left(\frac{gt}{v_t}\right) \right] $$
This gives the exact analytical position.

### Phase 4: Physical Interpretation & Limiting Behaviors
* **Early Stages ($t \ll v_t/g$):**
  Taylor expand $\tanh(u) \approx u - \frac{u^3}{3}$:
  $$ v(t) \approx v_t \left(\frac{gt}{v_t}\right) = gt $$
  For position, $\cosh(u) \approx 1 + \frac{u^2}{2} \implies \ln\cosh(u) \approx \ln(1 + u^2/2) \approx \frac{u^2}{2}$:
  $$ s(t) \approx \frac{v_t^2}{g}\left(\frac{1}{2}\frac{g^2 t^2}{v_t^2}\right) = \frac{1}{2}gt^2 $$
  Air resistance is negligible initially; the ball is in pure gravitational free fall.
* **Late Stages ($t \gg v_t/g$):**
  As $u \to \infty$, $\tanh(u) \to 1$, so $v(t) \to v_t$.
  Furthermore, $\cosh(u) = \frac{e^u + e^{-u}}{2} \approx \frac{1}{2}e^u$:
  $$ \ln\cosh(u) \approx u - \ln 2 = \frac{gt}{v_t} - \ln 2 $$
  $$ s(t) \approx \frac{v_t^2}{g}\left( \frac{gt}{v_t} - \ln 2 \right) = v_t t - \frac{v_t^2}{g}\ln 2 $$
  The ball reaches terminal velocity with a constant asymptotic positional delay.
* **Dimensional check:** $[v_t] = \sqrt{[mg]/[\rho S C_D]} = \sqrt{\dfrac{\text{kg}\cdot\text{m}\cdot\text{s}^{-2}}{\text{kg}\cdot\text{m}^{-3}\cdot\text{m}^2}} = \text{m/s}$; the argument $gt/v_t$ of $\tanh$ is dimensionless; $[v_t^2/g] = \text{m}$, so $s(t)$ is a length.
* **Numerical check (RK4, step $10^{-4}$, units with $g = v_t = 1$):** integrating $\dot{v} = 1 - v^2$, $\dot{s} = v$ up to $t = 1$ gives $v = 0.761594$ and $s = 0.433781$, equal to $\tanh 1 = 0.761594$ and $\ln\cosh 1 = 0.433781$.

---

## 📌 Problem 17: Linear Central Force

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle $M$ of mass $m$ is subject to:
  1. An attractive 3D linear central force directed towards origin $O$, proportional to mass $m$ and distance $r = OM$, with coefficient $k^2$:
     $$ \mathbf{F}_c = -m k^2 \mathbf{r} $$
  2. Uniform vertical gravity along $-Oz$:
     $$ \mathbf{F}_g = -mg\mathbf{k} $$
* **Initial State ($t = 0$):**
  - Position: $(x_0, y_0, z_0) = \left(\frac{\sqrt{3}g}{k^2}, 0, 0\right)$.
  - Velocity: $(\dot{x}_0, \dot{y}_0, \dot{z}_0) = \left(0, \frac{2g}{k}, 0\right)$.
* **Parameters:** $m > 0$ [kg], $g > 0$ [m/s$^2$], $k > 0$ [s$^{-1}$].

### Phase 2: Reference Frames & Vector Equations
* **Inertial Reference Frame:** Fixed Cartesian frame $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with origin at $O$ and $Oz$ pointing vertically upwards.
* **Position Vector:** $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$.
* **Newton's Second Law:**
  $$ m \ddot{\mathbf{r}} = \mathbf{F}_c + \mathbf{F}_g = -m k^2 \mathbf{r} - mg\mathbf{k} $$
  Divide by $m$:
  $$ \ddot{\mathbf{r}} + k^2 \mathbf{r} = -g\mathbf{k} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Decoupled Component Differential Equations
* **Pedagogical Justification:** Because the system is linear and isotropic in 3D Cartesian coordinates, the vector ODE uncouples into three independent scalar second-order ODEs with constant coefficients.
$$ \ddot{x} + k^2 x = 0 $$
$$ \ddot{y} + k^2 y = 0 $$
$$ \ddot{z} + k^2 z = -g $$

#### 2. Exact Integration of Each Component
1. **$x$-Component:**
   General solution:
   $$ x(t) = A_x \cos(kt) + B_x \sin(kt) $$
   Velocity: $\dot{x}(t) = -k A_x \sin(kt) + k B_x \cos(kt)$.
   Applying initial conditions:
   $$ x(0) = A_x = \frac{\sqrt{3}g}{k^2} $$
   $$ \dot{x}(0) = k B_x = 0 \implies B_x = 0 $$
   $$ x(t) = \frac{\sqrt{3}g}{k^2}\cos(kt) $$

2. **$y$-Component:**
   General solution:
   $$ y(t) = A_y \cos(kt) + B_y \sin(kt) $$
   Velocity: $\dot{y}(t) = -k A_y \sin(kt) + k B_y \cos(kt)$.
   Applying initial conditions:
   $$ y(0) = A_y = 0 $$
   $$ \dot{y}(0) = k B_y = \frac{2g}{k} \implies B_y = \frac{2g}{k^2} $$
   $$ y(t) = \frac{2g}{k^2}\sin(kt) $$

3. **$z$-Component:**
   Non-homogeneous equation with constant forcing $-g$.
   Particular solution: $z_p = -\frac{g}{k^2}$.
   General solution:
   $$ z(t) = -\frac{g}{k^2} + A_z \cos(kt) + B_z \sin(kt) $$
   Velocity: $\dot{z}(t) = -k A_z \sin(kt) + k B_z \cos(kt)$.
   Applying initial conditions:
   $$ z(0) = -\frac{g}{k^2} + A_z = 0 \implies A_z = \frac{g}{k^2} $$
   $$ \dot{z}(0) = k B_z = 0 \implies B_z = 0 $$
   $$ z(t) = \frac{g}{k^2}(\cos(kt) - 1) $$

#### 3. Particle Trajectory Vector
$$ \mathbf{r}_M(t) = \frac{\sqrt{3}g}{k^2}\cos(kt)\,\mathbf{i} + \frac{2g}{k^2}\sin(kt)\,\mathbf{j} + \frac{g}{k^2}(\cos(kt) - 1)\,\mathbf{k} $$

#### 4. Velocity Vector and Modulus
Differentiating with respect to time:
$$ \dot{x}(t) = -\frac{\sqrt{3}g}{k}\sin(kt) $$
$$ \dot{y}(t) = \frac{2g}{k}\cos(kt) $$
$$ \dot{z}(t) = -\frac{g}{k}\sin(kt) $$
Velocity vector:
$$ \mathbf{v}_M(t) = -\frac{\sqrt{3}g}{k}\sin(kt)\,\mathbf{i} + \frac{2g}{k}\cos(kt)\,\mathbf{j} - \frac{g}{k}\sin(kt)\,\mathbf{k} $$
Modulus of velocity:
$$ |\mathbf{v}_M(t)|^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2 = \left(-\frac{\sqrt{3}g}{k}\sin(kt)\right)^2 + \left(\frac{2g}{k}\cos(kt)\right)^2 + \left(-\frac{g}{k}\sin(kt)\right)^2 $$
$$ |\mathbf{v}_M(t)|^2 = \frac{3g^2}{k^2}\sin^2(kt) + \frac{4g^2}{k^2}\cos^2(kt) + \frac{g^2}{k^2}\sin^2(kt) $$
Factor out $\frac{g^2}{k^2}$:
$$ |\mathbf{v}_M(t)|^2 = \frac{g^2}{k^2} \left[ (3 + 1)\sin^2(kt) + 4\cos^2(kt) \right] = \frac{g^2}{k^2} \left[ 4\sin^2(kt) + 4\cos^2(kt) \right] = \frac{4g^2}{k^2} $$
Taking the square root:
$$ |\mathbf{v}_M(t)| = \frac{2g}{k} = \text{constant} $$
The particle travels with strictly **constant speed**!

#### 5. Geometric Nature and Shape of the Trajectory
* **Planarity Test:**
  Notice the direct linear relationship between $x(t)$ and $z(t)$:
  $$ x(t) = \frac{\sqrt{3}g}{k^2}\cos(kt) \implies \cos(kt) = \frac{k^2}{\sqrt{3}g}x(t) $$
  Substitute this into $z(t)$:
  $$ z(t) = \frac{g}{k^2}\cos(kt) - \frac{g}{k^2} = \frac{g}{k^2}\left(\frac{k^2}{\sqrt{3}g}x(t)\right) - \frac{g}{k^2} = \frac{x(t)}{\sqrt{3}} - \frac{g}{k^2} $$
  Multiply through by $\sqrt{3}$:
  $$ \sqrt{3}z = x - \frac{\sqrt{3}g}{k^2} \implies x - \sqrt{3}z = \frac{\sqrt{3}g}{k^2} $$
  This is the equation of a **plane** in $\mathbb{R}^3$. The trajectory is strictly planar!

* **Spherical Surface Test:**
  Consider the distance of $M$ from the point $C\left(0, 0, -\frac{g}{k^2}\right)$:
  $$ x^2 + y^2 + \left(z + \frac{g}{k^2}\right)^2 = \left(\frac{\sqrt{3}g}{k^2}\cos(kt)\right)^2 + \left(\frac{2g}{k^2}\sin(kt)\right)^2 + \left(\frac{g}{k^2}\cos(kt)\right)^2 $$
  $$ = \frac{3g^2}{k^4}\cos^2(kt) + \frac{4g^2}{k^4}\sin^2(kt) + \frac{g^2}{k^4}\cos^2(kt) = \frac{4g^2}{k^4}(\cos^2(kt) + \sin^2(kt)) = \frac{4g^2}{k^4} $$
  This defines a **sphere** centered at $C\left(0, 0, -\frac{g}{k^2}\right)$ with radius:
  $$ R = \frac{2g}{k^2} $$

* **Intersection & Circle Characterization:**
  Check if the center of the sphere $C\left(0, 0, -\frac{g}{k^2}\right)$ lies on the plane $x - \sqrt{3}z = \frac{\sqrt{3}g}{k^2}$:
  $$ 0 - \sqrt{3}\left(-\frac{g}{k^2}\right) = +\frac{\sqrt{3}g}{k^2} $$
  The plane passes directly through the center of the sphere! Therefore, the intersection of the sphere and the plane is a **great circle** of radius $R = \frac{2g}{k^2}$.

### Phase 4: Physical Interpretation & Synthesis
* The motion of the particle is a **uniform circular motion** along a great circle of radius $R = \frac{2g}{k^2}$ with constant orbital speed $v = \frac{2g}{k}$ and angular frequency $\omega = \frac{v}{R} = k$.
* The effective center of attraction is shifted from the origin $O$ to $C(0, 0, -g/k^2)$ because the linear restoring force combines with uniform gravity into an equivalent spring centered at the equilibrium point where $k^2 z_{eq} = -g$.
* **Dimensional check:** $[x] = [g/k^2] = \dfrac{\text{m/s}^2}{\text{s}^{-2}} = \text{m}$; $[v] = [g/k] = \text{m/s}$; $[R] = [2g/k^2] = \text{m}$; and $\omega = v/R = k$ has units s$^{-1}$.
* **Limit $k \to \infty$ (stiff attraction):** $R = 2g/k^2 \to 0$ and the equilibrium offset $z_{eq} = -g/k^2 \to 0$, so gravity becomes negligible against the central force. The centripetal consistency check holds for any $k$: $v^2/R = (4g^2/k^2)/(2g/k^2) = 2g$ equals the effective spring force per unit mass $k^2R = 2g$.
* **Symbolic check (sympy):** the trajectory of Phase 3 satisfies $\ddot{\mathbf{r}} + k^2\mathbf{r} = -g\mathbf{k}$ with zero residual and the initial data $\mathbf{r}(0)$, $\mathbf{v}(0)$; $\|\mathbf{v}\|^2 = 4g^2/k^2$, the squared distance to $C$ is $4g^2/k^4$, and $x - \sqrt{3}z = \sqrt{3}g/k^2$ for all $t$ (the centre $C$ lies on this plane).

---

## 📌 Problem 45: Vibrating Rotor (Unbalanced Turbojet)

### Phase 1: Physical Statement, Hypotheses & Parameters

* **Physical System:** a rigid disk of mass $m$ spins at the constant rate $\omega$. Its geometric centre $C$ is held near the design position $O$ by an elastic restoring force $-k\,\mathbf{r}_C$; its centre of mass $G$ is displaced from $C$ by the fixed distance $\ell$ (unbalance).
* **Hypotheses:** planar motion in the inertial plane $Oxy$; the weight is negligible; the spring (zero natural length) acts at $C$; the only external force is the elastic one, so the motion of $G$ is that of a particle of mass $m$ under that force (Newton's second law applied to $G$).
* **Parameters and units:** $m$ [kg], $k$ [N/m], $\ell$ [m], $\omega$ [rad/s]; natural frequency $\omega_0 = \sqrt{k/m}$ [rad/s].
* **Unknowns:** $x_0^G(t)$, $y_0^G(t)$, $x_0^C(t)$, $y_0^C(t)$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry

* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with $\mathbf{r}_C = x_0^C\,\mathbf{i}_0 + y_0^C\,\mathbf{j}_0$ and $\mathbf{r}_G = x_0^G\,\mathbf{i}_0 + y_0^G\,\mathbf{j}_0$.
* **Unbalance vector:** the segment $CG$ turns with the disk, at the angle $\omega t$ from $\mathbf{i}_0$ (figure):
$$ \mathbf{r}_G = \mathbf{r}_C + \ell\,\mathbf{e}(t), \qquad \mathbf{e}(t) = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0 $$

The unit vector $\mathbf{e}$ is the first column of the change-of-basis matrix from the disk-fixed basis (angle $\omega t$ about $\mathbf{k}_0$), whose determinant and orthogonality are checked:

$$ [{}_0 R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\omega t + \sin^2\omega t = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Equation of the dynamics of $G$

* **Pedagogical Justification:** The only external force is the spring force, which depends on the position of $C$, not on that of $G$. Newton's second law for the centre of mass, with the position of $C$ eliminated through the geometry $\mathbf{r}_C = \mathbf{r}_G - \ell\,\mathbf{e}(t)$, gives a forced linear equation (Notes Sec. 5.4, oscillator under a periodic force).
$$ m\,\ddot{\mathbf{r}}_G = -k\,\mathbf{r}_C = -k\left[\mathbf{r}_G - \ell\,\mathbf{e}(t)\right] $$

Divide by $m$ and use $\omega_0^2 = k/m$; the two components decouple:

$$ \ddot{x}_0^G + \omega_0^2\,x_0^G = \omega_0^2\,\ell\cos\omega t, \qquad \ddot{y}_0^G + \omega_0^2\,y_0^G = \omega_0^2\,\ell\sin\omega t $$

#### 2. Particular solution for $G$

* **Pedagogical Justification:** The general solution is the homogeneous one, $A\cos\omega_0 t + B\sin\omega_0 t$, which the statement assumes damped out, plus a particular solution. Because the forcing is harmonic at frequency $\omega$, try the same harmonic with an unknown amplitude (method of undetermined coefficients).
$$ x_0^G = a\cos\omega t \implies \ddot{x}_0^G = -\omega^2 a\cos\omega t $$

Substitute into the equation of motion:

$$ -\omega^2 a + \omega_0^2 a = \omega_0^2\,\ell \implies a = \frac{\omega_0^2\,\ell}{\omega_0^2 - \omega^2} \qquad (\omega \ne \omega_0) $$

The same steps with $y_0^G = b\sin\omega t$ give $b = a$. Therefore

$$ x_0^G(t) = \frac{\omega_0^2\,\ell}{\omega_0^2 - \omega^2}\cos\omega t, \qquad y_0^G(t) = \frac{\omega_0^2\,\ell}{\omega_0^2 - \omega^2}\sin\omega t $$

#### 3. Position of the geometric centre $C$

From $\mathbf{r}_C = \mathbf{r}_G - \ell\,\mathbf{e}(t)$, component by component:

$$ x_0^C(t) = \left[\frac{\omega_0^2}{\omega_0^2 - \omega^2} - 1\right]\ell\cos\omega t = \frac{\omega^2\,\ell}{\omega_0^2 - \omega^2}\cos\omega t, \qquad y_0^C(t) = \frac{\omega^2\,\ell}{\omega_0^2 - \omega^2}\sin\omega t $$

Both points describe circles about $O$ at the rotation rate $\omega$. Their distances to $O$ are

$$ |\boldsymbol{OG}| = \frac{\omega_0^2\,\ell}{|\omega_0^2 - \omega^2|}, \qquad |\boldsymbol{OC}| = \frac{\omega^2\,\ell}{|\omega_0^2 - \omega^2|}, \qquad \frac{|\boldsymbol{OC}|}{|\boldsymbol{OG}|} = \frac{\omega^2}{\omega_0^2} = \frac{m\,\omega^2}{k} $$

#### 4. Is $|\boldsymbol{OC}| > |\boldsymbol{OG}|$ for $\omega > \sqrt{k/m}$?

Yes. The ratio $|\boldsymbol{OC}|/|\boldsymbol{OG}| = \omega^2/\omega_0^2$ exceeds $1$ exactly when $\omega > \omega_0 = \sqrt{k/m}$ (and $\omega \ne \omega_0$, where the particular solution does not exist and the amplitude grows without bound, the resonance). For $\omega < \omega_0$ the opposite holds, $|\boldsymbol{OC}| < |\boldsymbol{OG}|$.

### Phase 4: Physical Interpretation & Dimensional Verification

* **Slow rotation ($\omega \to 0$):** $x_0^G \to \ell$, $x_0^C \to 0$: the disk sits with $C$ at $O$ and $G$ at distance $\ell$, as for a static unbalanced disk.
* **Fast rotation ($\omega \gg \omega_0$):** $|\boldsymbol{OG}| \to \ell\,\omega_0^2/\omega^2 \to 0$ and $|\boldsymbol{OC}| \to \ell$. Above the critical speed the disk self-centres: it spins about its centre of mass, and $C$ circles $G$ at the radius $\ell$ (opposite in phase to the unbalance, because the factor $\omega_0^2 - \omega^2$ is negative).
* **Resonance ($\omega = \omega_0$):** the amplitudes diverge in this undamped model; real rotors cross this critical speed quickly or are damped.
* **Dimensional check:** $[\omega_0^2\ell/(\omega_0^2 - \omega^2)] = \text{m}$ and $[k/m] = \text{N/m/kg} = \text{s}^{-2} = [\omega^2]$.
* **Symbolic check (sympy):** the two particular solutions satisfy the equations of motion with zero residual, and $x_0^G - \ell\cos\omega t$ equals $\omega^2\ell\cos\omega t/(\omega_0^2 - \omega^2)$.

---

## 📌 Problem 46: Bumpy Taxiway

### Phase 1: Physical Statement, Hypotheses & Parameters

* **Physical System:** the fuselage is a particle of mass $m$ that moves only vertically. The landing gear is a spring of stiffness $k$ and unloaded length $L$ whose lower end (the wheel) follows the runway profile $y_1 = \sin x$ at the horizontal speed $c$.
* **Hypotheses:** the wheel never leaves the ground; the runway profile is read with $x = ct$, so the ground height under the wheel is $y_b(t) = \sin(ct)$ (the profile is written with unit wavenumber, $1\,\text{m}^{-1}$, so the excitation angular frequency is $\Omega = c$ in rad/s when $c$ is in m/s); gravity acts on $m$; the gear is linear.
* **Parameters and units:** $m$ [kg], $k$ [N/m], $L$ [m], $c$ [m/s], $g$ [m/s$^2$]; $\omega_0 = \sqrt{k/m}$ [rad/s]; in part (c) a damper of coefficient $\lambda$ [N s/m] acts between the fuselage and the wheel.
* **Degrees of freedom:** one, the height $y$ of the particle.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry

* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}\}$ with $Oy$ vertical upward and $\mathbf{r}_P = y\,\mathbf{j}$ (the horizontal motion at speed $c$ does not enter the vertical dynamics).
* **Spring length:** $\ell_s = y - y_b(t)$ with $y_b = \sin ct$; the spring force on $P$ is $-k(\ell_s - L)\,\mathbf{j}$ (upward when compressed).
* **Static equilibrium over flat ground:** $y_s = L - mg/k$; the shifted coordinate $z = y - y_s$ measures the motion relative to it.

### Phase 3: Step-by-Step Mathematical Deduction

#### Equation of motion

* **Pedagogical Justification:** Newton's second law along $Oy$ with the weight and the elastic force. The constant weight only shifts the equilibrium, so it disappears in the coordinate $z$.
$$ m\ddot{y} = -k\left[y - \sin(ct) - L\right] - mg $$

Substitute $y = z + L - mg/k$, so that $\ddot{y} = \ddot{z}$ and $-k[y - L] - mg = -kz$:

$$ m\ddot{z} = -kz + k\sin(ct) \implies \ddot{z} + \omega_0^2\,z = \omega_0^2\sin(ct) $$

#### (a) Resonance

* **Pedagogical Justification:** This is a harmonic oscillator forced at the angular frequency $\Omega = c$ by the base motion (Notes Sec. 5.4). Resonance occurs when the forcing frequency equals the natural frequency.
$$ c_{res} = \omega_0 = \sqrt{\frac{k}{m}} $$

With the profile wavelength $2\pi$ (unit wavenumber), the resonant speed is $c = \sqrt{k/m}$; for a general wavelength $\Lambda$ it would be $c = \omega_0\Lambda/2\pi$.

#### (b) Amplitude at very high speed

Try the particular solution $z_p = A\sin(ct)$, for $c \ne \omega_0$:

$$ \ddot{z}_p = -c^2A\sin(ct) \implies (\omega_0^2 - c^2)A = \omega_0^2 \implies A = \frac{\omega_0^2}{\omega_0^2 - c^2} $$

The amplitude of the oscillation of the airplane (the homogeneous part, at $\omega_0$, is the transient set by the initial conditions) is

$$ |A(c)| = \frac{\omega_0^2}{|\omega_0^2 - c^2|} \xrightarrow[c \gg \omega_0]{} \frac{\omega_0^2}{c^2} = \frac{k}{m\,c^2} $$

For very high speed the amplitude decays as $1/c^2$: the mass cannot follow the fast bumps, and $z_p$ is in antiphase with the road ($A  \omega_0$).

#### (c) Landing gear with damping $\lambda$

* **Pedagogical Justification:** The damper acts on the relative velocity between the fuselage and the wheel, $-\lambda(\dot{y} - \dot{y}_b)$. Define $a = \lambda/m = 2\zeta\omega_0$ with the damping ratio $\zeta = \lambda/(2\sqrt{km})$.
$$ \ddot{z} + a\,\dot{z} + \omega_0^2 z = \omega_0^2\sin(ct) + a\,c\cos(ct) $$

**Homogeneous solution (transient).** The characteristic equation $r^2 + a\,r + \omega_0^2 = 0$ has roots $r = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$:

* Underdamped, $\lambda < 2\sqrt{km}$ ($\zeta < 1$): $z_h = e^{-\zeta\omega_0 t}\left(C_1\cos\omega_d t + C_2\sin\omega_d t\right)$ with $\omega_d = \omega_0\sqrt{1 - \zeta^2}$.
* Critical, $\lambda = 2\sqrt{km}$ ($\zeta = 1$): $z_h = (C_1 + C_2 t)\,e^{-\omega_0 t}$, the fastest return without oscillation.
* Overdamped, $\lambda > 2\sqrt{km}$ ($\zeta > 1$): $z_h = C_1 e^{r_1 t} + C_2 e^{r_2 t}$ with $r_{1,2} < 0$ real, slower return.

**Steady state.** Write the forcing as the imaginary part of $(\omega_0^2 + i a c)\,e^{ict}$ and $z_p = \operatorname{Im}[H\,e^{ict}]$:

$$ H = \frac{\omega_0^2 + i\,a c}{\omega_0^2 - c^2 + i\,a c}, \qquad |H|^2 = \frac{\omega_0^4 + a^2c^2}{(\omega_0^2 - c^2)^2 + a^2c^2} $$

The steady amplitude is $|H|$, and it is always finite. At resonance, $c = \omega_0$:

$$ |H(\omega_0)| = \sqrt{1 + \frac{\omega_0^2}{a^2}} = \sqrt{1 + \frac{1}{4\zeta^2}} $$

At very high speed $|H| \approx a\,c/c^2 = a/c = \lambda/(m c)$: it decays only as $1/c$, slower than the undamped $1/c^2$ of part (b).

#### Choice of $\lambda$ and effect of the payload

* Damping removes the resonant divergence ($|H(\omega_0)|$ finite) and kills the transient quickly, but the price is the slower attenuation $1/c$ of the bumps at high speed. A compromise is $\zeta$ below $1$ (not overdamped): $\zeta = 0.5$ gives a resonant peak of $\sqrt{2} = 1.41$ and $\zeta = 0.7$ gives $1.22$, whereas critical damping slows the response and transmits more at high speed.
* Changing the mass changes both $\omega_0 = \sqrt{k/m}$, so the resonant speed $c_{res} = \sqrt{k/m}$ is lower for a heavier aircraft, and $\zeta = \lambda/(2\sqrt{km}) \propto m^{-1/2}$, so a heavier aircraft is less damped. Since $\lambda$ is fixed hardware, it must be chosen so that $\zeta$ stays in the useful range (for example $\zeta \gtrsim 0.3$) for the heaviest payload; the lightest payload then gets a larger $\zeta$ and a higher resonant speed.

### Phase 4: Physical Interpretation & Dimensional Verification

* **Dimensional check:** $[\omega_0^2] = [k/m] = \text{s}^{-2} = [c^2]$ with $c$ in rad/s; $[a] = [\lambda/m] = \text{N s m}^{-1}/\text{kg} = \text{s}^{-1}$, so $\zeta = a/(2\omega_0)$ is dimensionless.
* **Limits:** $c \to 0$ gives $|A| \to 1$, the airplane follows the road quasi-statically; $\lambda \to 0$ in $|H|$ recovers $|A|$ of part (b); $\zeta \to \infty$ gives $|H| \to 1$ for slow runways and $\to \lambda/(mc)$ at high speed.
* **Symbolic check (sympy):** the undamped particular solution and the damped steady state $z_p = \operatorname{Im}[H e^{ict}]$ satisfy their equations with zero residual, and $|H(\omega_0)|^2 = 1 + \omega_0^2/a^2$.
