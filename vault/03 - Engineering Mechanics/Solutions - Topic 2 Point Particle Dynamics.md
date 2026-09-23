---
title: "Solutions - Topic 2: Point Particle Dynamics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (4-Phase Methodology)"
language: "English"
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
* **Pedagogical Justification:** In a one-dimensional problem where the force depends exclusively on position $x$, the force field is automatically irrotational (curl is trivially zero in 1D) and conservative. By definition of a conservative force (Notes.pdf Section 2.3), the work done by the force corresponds to the negative variation of potential energy, $\mathbf{F} = -\boldsymbol{\nabla} V = -\frac{dV}{dx}\mathbf{i}$. Integrating this relation allows us to replace the second-order nonlinear differential equation $m\ddot{x} + cx^3 = 0$ with an algebraic energy conservation law (first integral of motion).

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
* **Confirmation with UC3M Solution Keys:** Directly verifies the qualitative classification in `Problems.pdf` page 72.

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
* Exact agreement with `Problems.pdf` page 72:
  - If $v_0 > a\sqrt{2K}$, particle moves towards $-\infty$.
  - If $v_0 < a\sqrt{2K}$, particle moves towards $+\infty$ after decelerating before arriving to $x = 0$.
  - If $v_0 = a\sqrt{2K}$, particle takes infinite time to reach $x = 0$.
* Dimensional verification: $[v_{0,crit}] = [a]\sqrt{[K]} = \text{m}\cdot\sqrt{\text{s}^{-2}} = \text{m}/\text{s}$. Correct.

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
This matches the official equation of motion in `Problems.pdf` page 73.

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
This reproduces the exact closed-form solution from `Problems.pdf` page 73.

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

---

## 📌 Problem 21: Rotating Planet & Apparent Weight

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A spherical planet of radius $R$ spins with constant angular velocity $\boldsymbol{\Omega} = \Omega \mathbf{k}$ around its polar axis.
* **Gravitational Field:** Uniform surface gravitational acceleration $g_p$ directed toward the center of the planet.
* **Apparent Weight:** The weight measured by a spring balance or scale is the normal reaction force $\mathbf{N}$ exerted by the surface to support a static mass $m$ on the surface.
* **Problem Condition:** A body on the pole weighs twice as much as on the equator:
  $$ W_{pole} = 2 W_{equator} $$
* **Objective:** Determine the duration of the planet's sidereal day $T_{day} = \frac{2\pi}{\Omega}$.

### Phase 2: Reference Frames & Vector Transformation
* **Inertial Frame $\mathcal{F}_0$:** Frame centered at the planet center $O$.
* **Rotating Frame $\mathcal{F}_1$:** Planet-fixed reference frame rotating with angular velocity $\boldsymbol{\omega}_{1/0} = \Omega\mathbf{k}$.
* **Acceleration of a Stationary Point on the Surface:**
  For a body resting on the surface, relative velocity and acceleration vanish: $\mathbf{v}' = \mathbf{0}$, $\mathbf{a}' = \mathbf{0}$.
  The inertial acceleration is purely centripetal:
  $$ \mathbf{a}_0 = \boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) = -\Omega^2 \boldsymbol{\rho} $$
  where $\boldsymbol{\rho}$ is the projection of the position vector onto the equatorial plane.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Dynamic Equilibrium in the Rotating Frame
* **Pedagogical Justification:** In the non-inertial reference frame of the planet, static equilibrium requires the sum of real gravitational force $\mathbf{F}_g$, reaction force $\mathbf{N}$, and fictitious centrifugal force $\mathbf{F}_{cf} = -m\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) = m\Omega^2 \boldsymbol{\rho}$ to vanish.
$$ \mathbf{F}_g + \mathbf{N} + \mathbf{F}_{cf} = \mathbf{0} \implies \mathbf{N} = -\mathbf{F}_g - \mathbf{F}_{cf} $$
The apparent weight is the magnitude of the normal force, $W = |\mathbf{N}|$.

#### 2. Apparent Weight at the Pole
At the geographic poles, the position vector lies along the rotation axis $\mathbf{k}$:
$$ \mathbf{r}_{pole} = \pm R\mathbf{k} \implies \boldsymbol{\rho}_{pole} = \mathbf{0} $$
The centrifugal force vanishes at the poles:
$$ \mathbf{F}_{cf, pole} = \mathbf{0} $$
Therefore:
$$ \mathbf{N}_{pole} - m g_p \mathbf{k} = \mathbf{0} \implies W_{pole} = m g_p $$

#### 3. Apparent Weight at the Equator
At the equator, the position vector lies entirely in the equatorial plane:
$$ |\boldsymbol{\rho}_{eq}| = R $$
Gravity acts radially inwards: $\mathbf{F}_{g, eq} = -m g_p \mathbf{e}_r$.
The centrifugal force acts radially outwards: $\mathbf{F}_{cf, eq} = +m \Omega^2 R \mathbf{e}_r$.
Normal reaction from the surface: $\mathbf{N}_{eq} = N_{eq} \mathbf{e}_r$.
Equilibrium equation:
$$ -m g_p \mathbf{e}_r + N_{eq} \mathbf{e}_r + m \Omega^2 R \mathbf{e}_r = \mathbf{0} $$
$$ N_{eq} = m(g_p - \Omega^2 R) $$
Thus, the apparent weight at the equator is:
$$ W_{equator} = m(g_p - \Omega^2 R) $$

#### 4. Computation of the Rotation Rate $\Omega$
Imposing the given condition $W_{pole} = 2 W_{equator}$:
$$ m g_p = 2m(g_p - \Omega^2 R) $$
Divide both sides by $m$:
$$ g_p = 2g_p - 2\Omega^2 R $$
Rearrange to isolate $\Omega^2$:
$$ 2\Omega^2 R = 2g_p - g_p = g_p $$
$$ \Omega^2 = \frac{g_p}{2R} \implies \Omega = \sqrt{\frac{g_p}{2R}} $$

#### 5. Duration of the Day
The duration of one full planetary rotation (the day) is:
$$ T_{day} = \frac{2\pi}{\Omega} = \frac{2\pi}{\sqrt{\frac{g_p}{2R}}} = 2\pi \sqrt{\frac{2R}{g_p}} = 2\sqrt{2}\pi \sqrt{\frac{R}{g_p}} $$

### Phase 4: Physical Interpretation & Stability
* **Dimensional Analysis:**
  $[T_{day}] = \sqrt{\frac{[R]}{[g_p]}} = \sqrt{\frac{\text{m}}{\text{m}/\text{s}^2}} = \sqrt{\text{s}^2} = \text{s}$.
  The result is dimensionally sound.
* **Centrifugal Breakup Limit:**
  A planet becomes gravitationally unbounded at the equator (weightlessness) when $\Omega_{crit} = \sqrt{g_p/R}$. Here $\Omega = \sqrt{g_p/(2R)} = \frac{1}{\sqrt{2}}\Omega_{crit} \approx 0.707\,\Omega_{crit}$, ensuring that objects remain resting on the equatorial surface.

---

## 📌 Problem 23: Simple Pendulum

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ is suspended by a string of length $L$ from pivot $O$, or equivalently moves along the smooth interior of a vertical circular track of radius $L$.
* **Unilateral Constraint:** The particle cannot cross the circular boundary outward, but may detach if the inward contact force drops to zero ($N = 0$, or string slack $T = 0$).
* **Initial Motion:** Pushed from the lowest point ($\theta = 0$) with velocity $v_0$.
* **Part (b) Modification:** The circular track rotates about its vertical diameter with constant angular velocity $\omega$.
* **Parameters:** $m > 0$ [kg], $L > 0$ [m], $g > 0$ [m/s$^2$], $v_0 > 0$ [m/s], $\omega \ge 0$ [rad/s].

### Phase 2: Reference Frames, Vector Bases & Polar Coordinates
* **Inertial Frame $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$:** $Oz$ points vertically upward ($-\mathbf{k}$ is downward).
* **Polar Coordinate Basis $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{j}\}$:**
  Angle $\theta$ measured from the downward vertical ($-\mathbf{k}$):
  $$ \mathbf{e}_r = \sin\theta\,\mathbf{i} - \cos\theta\,\mathbf{k} \quad (\text{pointing radially outward}) $$
  $$ \mathbf{e}_\theta = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{k} \quad (\text{tangential, along increasing } \theta) $$
* **Kinematics:**
  - Position: $\mathbf{r} = L\mathbf{e}_r$.
  - Velocity: $\mathbf{v} = L\dot{\theta}\mathbf{e}_\theta$.
  - Acceleration: $\mathbf{a} = -L\dot{\theta}^2\mathbf{e}_r + L\ddot{\theta}\mathbf{e}_\theta$.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Planar Motion & Detachment Analysis

#### 1. Mechanical Energy Conservation
* **Pedagogical Justification:** The normal constraint force $\mathbf{N} = -N\mathbf{e}_r$ is always perpendicular to velocity $\mathbf{v} = L\dot{\theta}\mathbf{e}_\theta$ ($\mathbf{N} \cdot \mathbf{v} = 0$), so it does no work. Mechanical energy is strictly conserved.
Taking the lowest point $\theta = 0$ as the gravitational potential reference ($V(0) = 0$):
$$ V(\theta) = mg(L - L\cos\theta) = mgL(1 - \cos\theta) $$
$$ E = \frac{1}{2}m v_0^2 = \frac{1}{2}m v^2 + mgL(1 - \cos\theta) $$
Isolate $v^2(\theta)$:
$$ v^2(\theta) = v_0^2 - 2gL(1 - \cos\theta) $$

#### 2. Normal Reaction Force $N(\theta)$
* **Pedagogical Justification:** Newton's second law along the inward radial normal $\mathbf{e}_n = -\mathbf{e}_r$ provides an explicit expression for the contact reaction force $N(\theta)$ as a function of angle $\theta$.
The forces acting on the particle are gravity $\mathbf{F}_g = -mg\mathbf{k}$ and track reaction $\mathbf{N} = -N\mathbf{e}_r$ ($N > 0$ pushes inward):
$$ \mathbf{F}_g = -mg\mathbf{k} = -mg(-\cos\theta\,\mathbf{e}_r + \sin\theta\,\mathbf{e}_\theta) = mg\cos\theta\,\mathbf{e}_r - mg\sin\theta\,\mathbf{e}_\theta $$
Projecting Newton's second law along the inward normal $-\mathbf{e}_r$:
$$ \sum F_n = N - mg\cos\theta = m a_n = m \frac{v^2}{L} $$
$$ N(\theta) = mg\cos\theta + \frac{m}{L}v^2(\theta) $$
Substitute the energy relation for $v^2(\theta)$:
$$ N(\theta) = mg\cos\theta + \frac{m}{L}\left[ v_0^2 - 2gL(1 - \cos\theta) \right] $$
Expand and combine terms:
$$ N(\theta) = mg\cos\theta + \frac{m v_0^2}{L} - 2mg + 2mg\cos\theta = \frac{m v_0^2}{L} - 2mg + 3mg\cos\theta $$
$$ N(\theta) = \frac{m v_0^2}{L} - mg(2 - 3\cos\theta) $$

#### 3. Detachment Condition ($N = 0$)
The particle leaves the circumference if $N$ drops to zero while $v > 0$:
$$ N(\theta_d) = 0 \implies \frac{m v_0^2}{L} - 2mg + 3mg\cos\theta_d = 0 $$
$$ 3mg\cos\theta_d = 2mg - \frac{m v_0^2}{L} \implies \cos\theta_d = \frac{2gL - v_0^2}{3gL} $$

#### 4. Motion Regimes and Question Resolution: "Is this point ever reached?"
* **Regime 1: $v_0 \le \sqrt{2gL}$ (Low energy, oscillation in lower semicircle)**
  Velocity reaches zero when $v^2 = 0$:
  $$ v_0^2 - 2gL(1 - \cos\theta_{max}) = 0 \implies \cos\theta_{max} = 1 - \frac{v_0^2}{2gL} \ge 0 \implies \theta_{max} \le \frac{\pi}{2} $$
  At this maximum angle, the reaction force is:
  $$ N(\theta_{max}) = mg\cos\theta_{max} \ge 0 $$
  The particle comes to rest and reverses direction before $N$ can vanish.
  **Conclusion:** The detachment point is **never reached**. The particle oscillates periodically in the lower semicircle.

* **Regime 2: $\sqrt{2gL} < v_0 < \sqrt{5gL}$ (Intermediate energy, detachment occurs)**
  Since $v_0^2 > 2gL$, the particle crosses the horizontal position $\theta = \pi/2$ with positive velocity.
  In the upper semicircle ($\pi/2 < \theta < \pi$), $\cos\theta < 0$.
  Evaluate the detachment angle $\cos\theta_d$:
  $$ \cos\theta_d = \frac{2gL - v_0^2}{3gL} $$
  Because $2gL < v_0^2 < 5gL$:
  $$ -1 = \frac{2gL - 5gL}{3gL} < \cos\theta_d < \frac{2gL - 2gL}{3gL} = 0 $$
  So $\cos\theta_d \in (-1, 0)$, meaning $\theta_d \in (\pi/2, \pi)$ is physically accessible!
  At this point, the speed is:
  $$ v^2(\theta_d) = v_0^2 - 2gL\left(1 - \frac{2gL - v_0^2}{3gL}\right) = v_0^2 - 2gL + \frac{2}{3}(2gL - v_0^2) = \frac{v_0^2 - 2gL}{3} > 0 $$
  **Conclusion:** The detachment point **is reached**. The particle leaves the circular track at angle $\theta_d = \arccos\left(\frac{2gL - v_0^2}{3gL}\right)$ and transitions into free parabolic flight under gravity alone.

* **Regime 3: $v_0 \ge \sqrt{5gL}$ (High energy, complete vertical loops)**
  At the very top of the circle ($\theta = \pi, \cos\pi = -1$):
  $$ N(\pi) = \frac{m v_0^2}{L} - mg(2 - 3(-1)) = \frac{m v_0^2}{L} - 5mg \ge 0 $$
  The reaction force remains positive throughout the entire loop.
  **Conclusion:** The particle **never leaves** the circumference and performs complete revolutions.

---

#### Part (b): Rotating Circumference with Angular Velocity $\omega$

#### 1. Equations of Motion in the Rotating Frame
* **Pedagogical Justification:** When the circular track rotates at constant angular speed $\omega$ about the vertical diameter $Oz$, we analyze the motion in the rotating frame $\mathcal{F}_1$. The centrifugal force $\mathbf{F}_{cf} = m\omega^2 \boldsymbol{\rho}$ adds a horizontal outward component.
Let cylindrical coordinates be $(\rho, \phi, z)$, with $\rho = R\sin\theta$, $z = -R\cos\theta$.
In the rotating frame, the unit tangent along increasing $\theta$ is:
$$ \mathbf{e}_\theta = \cos\theta\,\mathbf{e}_\rho + \sin\theta\,\mathbf{k} $$
Forces acting on the particle:
1. Gravity: $\mathbf{F}_g = -mg\mathbf{k}$.
2. Centrifugal force: $\mathbf{F}_{cf} = m\omega^2 \rho\,\mathbf{e}_\rho = m\omega^2 R\sin\theta\,\mathbf{e}_\rho$.
3. Reaction force $\mathbf{N}$ (normal to the wire, along $\mathbf{e}_r$ and $\mathbf{e}_\phi$).
Projecting along the tangent $\mathbf{e}_\theta$:
$$ m R \ddot{\theta} = (\mathbf{F}_g + \mathbf{F}_{cf}) \cdot \mathbf{e}_\theta $$
$$ \mathbf{F}_g \cdot \mathbf{e}_\theta = (-mg\mathbf{k}) \cdot (\cos\theta\,\mathbf{e}_\rho + \sin\theta\,\mathbf{k}) = -mg\sin\theta $$
$$ \mathbf{F}_{cf} \cdot \mathbf{e}_\theta = (m\omega^2 R\sin\theta\,\mathbf{e}_\rho) \cdot (\cos\theta\,\mathbf{e}_\rho + \sin\theta\,\mathbf{k}) = m\omega^2 R\sin\theta\cos\theta $$
Therefore:
$$ m R \ddot{\theta} = -mg\sin\theta + m\omega^2 R\sin\theta\cos\theta $$
Divide by $m R$:
$$ \ddot{\theta} + \frac{g}{R}\sin\theta - \omega^2\sin\theta\cos\theta = 0 $$
$$ \ddot{\theta} + \left(\frac{g}{R} - \omega^2\cos\theta\right)\sin\theta = 0 $$

#### 2. Computation of Equilibrium Locations
* **Pedagogical Justification:** Equilibrium configurations in the rotating frame correspond to static solutions where $\ddot{\theta} = 0$ and $\dot{\theta} = 0$.
Setting the angular acceleration to zero:
$$ \left(\frac{g}{R} - \omega^2\cos\theta\right)\sin\theta = 0 $$
This equation is satisfied if either factor vanishes:
1. **Vertical Alignments ($\sin\theta = 0$):**
   $$ \theta_1 = 0 \quad (\text{lowest point / bottom}) $$
   $$ \theta_2 = \pi \quad (\text{highest point / top}) $$
2. **Off-Axis Equilibrium ($\cos\theta = \frac{g}{\omega^2 R}$):**
   This solution exists physically if and only if:
   $$ \left| \frac{g}{\omega^2 R} \right| \le 1 \iff \omega^2 \ge \frac{g}{R} $$
   When $\omega > \sqrt{\frac{g}{R}}$, two symmetric equilibrium positions emerge:
   $$ \theta_{3,4} = \pm \arccos\left(\frac{g}{\omega^2 R}\right) $$

### Phase 4: Physical Interpretation & Bifurcation Analysis
* **Supercritical Pitchfork Bifurcation:**
  - For slow rotation $\omega < \omega_c = \sqrt{g/R}$, the bottom $\theta = 0$ is the only stable equilibrium.
  - When the rotation rate crosses the critical threshold $\omega_c$, the bottom becomes unstable, and the particle naturally climbs up the wire to settle at the tilted angle $\theta_0 = \arccos\left(\frac{g}{\omega^2 R}\right)$, where the upward component of the centrifugal force balances gravity.
  - As $\omega \to \infty$, $\cos\theta_0 \to 0 \implies \theta_0 \to \pi/2$ (the particle moves toward the equator).

---
