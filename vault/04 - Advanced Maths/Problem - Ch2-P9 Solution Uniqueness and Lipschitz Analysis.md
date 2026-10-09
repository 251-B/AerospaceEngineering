---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.9"
dificultad: media
tags:
  - problema-resuelto
  - uniqueness
  - lipschitz-continuity
  - picard-theorem
  - non-uniqueness
  - finite-time-blow-up
---

# Problem 2.9: Uniqueness and Lipschitz Analysis

Source: ProblemsCh2.pdf, Exercise 9 (page 2). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 6, Section 6.2 (Theorem 6.2 and its footnote on Lipschitz continuity).

## Problem Statement

Which of the following differential equations have unique solutions (at least on some small time interval) for any non-negative initial condition $x(0) \geq 0$?

(i) $\dot{x} = x(1 - x^2)$,  
(ii) $\dot{x} = x^3$,  
(iii) $\dot{x} = x^{1/3}$,  
(iv) $\dot{x} = x^{1/2}(1+x)^2$,  
(v) $\dot{x} = (1+x)^{3/2}$.  

---

## Phase 1: Classification, Hypotheses and Domain

Each equation is autonomous: $\dot{x} = f(x)$ with initial condition $x(0) = x_0 \geq 0$.

Uniqueness criterion used (Robinson, Theorem 6.2): if $f$ and $\partial f/\partial x$ are continuous in an open neighborhood of $(t_0, x_0)$, then the IVP has a unique solution on some open interval containing $t_0$. This is a sufficient condition, not a necessary one: a more general sufficient condition is that $f$ be locally Lipschitz in $x$, $\lvert f(x) - f(y)\rvert \leq L\lvert x - y\rvert$. When the condition fails at a point, uniqueness there must be examined directly.

| Part | $f(x)$ | $f'(x)$ | Where $f'$ is continuous |
| :--- | :--- | :--- | :--- |
| (i) | $x - x^3$ | $1 - 3x^2$ | all $x$ |
| (ii) | $x^3$ | $3x^2$ | all $x$ |
| (iii) | $x^{1/3}$ | $\frac13 x^{-2/3}$ | $x \neq 0$ |
| (iv) | $x^{1/2}(1+x)^2$ | $\frac12 x^{-1/2}(1+x)^2 + 2x^{1/2}(1+x)$ | $x > 0$ |
| (v) | $(1+x)^{3/2}$ | $\frac32(1+x)^{1/2}$ | $x > -1$ (so all $x \geq 0$) |

---

## Phase 2: Choice of Method and Change of Variables

Why this method: for each $f$, check where $f$ and $f'$ are continuous. On those sets Theorem 6.2 applies. At any point $x_0 \geq 0$ where it does not apply (here only $x_0 = 0$ in (iii) and (iv), where $f'$ is unbounded), decide uniqueness by constructing two solutions (separation of variables) or by showing that they cannot exist.

For a decisive non-uniqueness test at $x_0 = 0$ with $f(0) = 0$ and $f > 0$ for $x > 0$: the constant $x \equiv 0$ is always a solution, and by separation of variables, $t = \int_0^x ds/f(s)$ defines a second solution $x(t) > 0$ for $t > 0$ whenever the integral $\int_0^{\varepsilon} ds/f(s)$ is finite (the time needed to leave $0$ is then finite).

---

## Phase 3: Step-by-Step Derivation

### Part (i): $\dot{x} = x(1 - x^2)$

$f(x) = x - x^3$ and $f'(x) = 1 - 3x^2$ are polynomials, continuous everywhere. Theorem 6.2 applies at every $x_0 \geq 0$. Answer: unique solution for all $x_0 \geq 0$.

### Part (ii): $\dot{x} = x^3$

$f = x^3$, $f' = 3x^2$, continuous everywhere. Answer: unique solution for all $x_0 \geq 0$ (locally in time). Remark: the solution blows up in finite time. Separating, $\int_{x_0}^{x} s^{-3}\,ds = t$ gives $-\frac{1}{2x^2} + \frac{1}{2x_0^2} = t$, so $x(t) = \left(x_0^{-2} - 2t\right)^{-1/2}$ for $x_0 > 0$, which exists only for $t < T^* = \frac{1}{2x_0^2}$. This is why the problem says 'at least on some small time interval'.

### Part (iii): $\dot{x} = x^{1/3}$

$f = x^{1/3}$ is continuous, but $f'(x) = \frac13 x^{-2/3} \to \infty$ as $x \to 0^+$. For $x_0 > 0$, $f$ and $f'$ are continuous near $x_0$, so the solution is unique. For $x_0 = 0$ the theorem does not apply, and uniqueness in fact fails: the constant $x \equiv 0$ is a solution, and separating variables with $x \geq 0$,

$$
\int_0^{x} s^{-1/3}\,ds = \left[\tfrac32 s^{2/3}\right]_0^{x} = \tfrac32 x^{2/3} = t \quad\Longrightarrow\quad x(t) = \left(\tfrac{2t}{3}\right)^{3/2}, \quad t \geq 0,
$$

is a second solution with $x(0) = 0$. Check: $\dot{x} = \frac32\cdot\frac23\left(\frac{2t}{3}\right)^{1/2} = \left(\frac{2t}{3}\right)^{1/2}$ and $x^{1/3} = \left(\frac{2t}{3}\right)^{1/2}$. So there are at least two solutions from $x_0 = 0$ (indeed infinitely many, obtained by staying at $0$ until any time $c \geq 0$ and then following $\left(\frac{2(t-c)}{3}\right)^{3/2}$). Answer: unique for $x_0 > 0$, not unique for $x_0 = 0$.

### Part (iv): $\dot{x} = x^{1/2}(1+x)^2$

$f(x) = \sqrt{x}\,(1+x)^2$ is continuous on $x \geq 0$ and $f'(x) = \frac{(1+x)^2}{2\sqrt{x}} + 2\sqrt{x}\,(1+x) \to \infty$ as $x \to 0^+$. For $x_0 > 0$ Theorem 6.2 applies and the solution is unique. At $x_0 = 0$ the theorem does not apply. We show non-uniqueness: besides $x \equiv 0$, separate variables for $x > 0$ and substitute $s = r^2$, $ds = 2r\,dr$ (so $\sqrt{s} = r$):

$$
t = \int_0^{x}\frac{ds}{\sqrt{s}\,(1+s)^2} = \int_0^{\sqrt{x}}\frac{2\,dr}{(1+r^2)^2} = \left[\frac{r}{1+r^2} + \arctan r\right]_0^{\sqrt{x}} = \frac{\sqrt{x}}{1+x} + \arctan\sqrt{x}.
$$

The primitive is checked by differentiation: $\frac{d}{dr}\left[\frac{r}{1+r^2} + \arctan r\right] = \frac{1 - r^2}{(1+r^2)^2} + \frac{1}{1+r^2} = \frac{2}{(1+r^2)^2}$. The function $T(x) = \frac{\sqrt{x}}{1+x} + \arctan\sqrt{x}$ is continuous and strictly increasing on $x \geq 0$ (its derivative is $1/(\sqrt{x}(1+x)^2) > 0$), with $T(0) = 0$ and $T(x) \to \pi/2$ as $x \to \infty$. Its inverse $x(t) = T^{-1}(t)$, $0 \leq t < \pi/2$, is a solution with $x(0) = 0$ and $x(t) > 0$ for $t > 0$. So at $x_0 = 0$ there are at least two solutions. Answer: unique for $x_0 > 0$, not unique for $x_0 = 0$.

### Part (v): $\dot{x} = (1+x)^{3/2}$

$f = (1+x)^{3/2}$ and $f' = \frac32(1+x)^{1/2}$ are continuous for $x > -1$, in particular for every $x_0 \geq 0$. Answer: unique solution for all $x_0 \geq 0$. The solution exists only up to a finite time: separating,

$$
\int_{x_0}^{x}(1+s)^{-3/2}\,ds = \left[-2(1+s)^{-1/2}\right]_{x_0}^{x} = -\frac{2}{\sqrt{1+x}} + \frac{2}{\sqrt{1+x_0}} = t,
$$

so $x(t) = \left(\frac{1}{\sqrt{1+x_0}} - \frac{t}{2}\right)^{-2} - 1$, which blows up at $T^* = \frac{2}{\sqrt{1+x_0}}$ (for $x_0 = 0$, $T^* = 2$).

---

## Phase 4: Verification, Limits and Interpretation

Summary of the criterion check and numerical cross-checks: for (iii), with $x(t) = (2t/3)^{3/2}$ the residual $\dot{x} - x^{1/3}$ evaluated at $t = 0.7, 1.3, 5$ is of order $10^{-17}$ (rounding); for (iv), sympy gives $T'(x)\,f(x) = 1$ identically; for (ii) and (v) the closed forms give residual $0$ symbolically.

Non-uniqueness and the Lipschitz condition are consistent: in (iii) and (iv), $\frac{\lvert f(x) - f(0)\rvert}{x} = x^{-2/3}$ and $\sim x^{-1/2}$ respectively, which are unbounded as $x \to 0^+$, so no Lipschitz constant exists near $0$. (For (iii) and (iv) the integral $\int_0 ds/f(s)$ converges, which is exactly what allows the solution to leave $0$ in finite time.) By contrast, in (i), (ii), (v) $f$ is Lipschitz on every bounded interval, and uniqueness holds.

#### Answer

| Part | Unique for every $x_0 \geq 0$? | Comment |
| :--- | :--- | :--- |
| (i) | Yes | $f \in C^1$; solutions stay bounded |
| (ii) | Yes (locally in time) | blow-up at $T^* = 1/(2x_0^2)$ for $x_0 > 0$ |
| (iii) | No | fails at $x_0 = 0$: $x \equiv 0$ and $x = (2t/3)^{3/2}$ |
| (iv) | No | fails at $x_0 = 0$: $x \equiv 0$ and $x = T^{-1}(t)$ |
| (v) | Yes (locally in time) | blow-up at $T^* = 2/\sqrt{1+x_0}$ |

---

## Related Notes

- [[04 - Advanced Maths/Concept - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Problem - Ch2-P14 Non-Lipschitz Branching Pathology in Picard Theorem|Problem 2.14: non-Lipschitz branching]]
- [[04 - Advanced Maths/Problem - Ch2-P13 Multi-Equilibria Autonomous Phase Line Dynamics|Problem 2.13: finite-time blow-up on the phase line]]
