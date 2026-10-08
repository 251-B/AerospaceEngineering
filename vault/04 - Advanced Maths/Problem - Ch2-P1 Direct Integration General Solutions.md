---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.1"
dificultad: baja
tags:
  - problema-resuelto
  - direct-integration
  - antiderivatives
  - integral-calculus
---

# Problem 2.1: Direct Integration: General Solutions

Source: ProblemsCh2.pdf, Exercise 1 (page 1). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Section 5.1 (Fundamental Theorem of Calculus) and Section 5.2 (general solutions and initial conditions).

## Problem Statement

Find the general solution to the following equations:

(i) $y'(x) = e^{3x} - x$;  
(ii) $x\,y'(x) = 1$;  
(iii) $y'(x) = x\,e^{x^2}$;  
(iv) $(1+x)\,y'(x) = x$;  
(v) $(1+x^2)\,y'(x) = x$.  

---

## Phase 1: Classification, Hypotheses and Domain

Each equation is first order, explicit once the coefficient of $y'$ is divided out, and the unknown $y$ does not appear on the right-hand side:

$$
\frac{dy}{dx} = f(x).
$$

- (i) $f(x) = e^{3x} - x$, continuous on $\mathbb{R}$.
- (ii) $f(x) = 1/x$, continuous on $(-\infty,0)$ and on $(0,\infty)$; at $x=0$ the equation reads $0 = 1$, so no solution can be defined at $x=0$.
- (iii) $f(x) = x e^{x^2}$, continuous on $\mathbb{R}$.
- (iv) $f(x) = x/(1+x)$, continuous on $(-\infty,-1)$ and on $(-1,\infty)$; at $x=-1$ the equation reads $0 = -1$, so no solution can be defined at $x=-1$.
- (v) $f(x) = x/(1+x^2)$, continuous on $\mathbb{R}$ because $1+x^2 \ge 1 > 0$.

Unknown: a function $y$ differentiable on an interval $I$ on which $f$ is continuous. Because $f$ does not depend on $y$, the right-hand side is trivially Lipschitz in $y$ and the existence-uniqueness theorem (Robinson, Theorem 6.2) gives exactly one solution for each initial condition $y(x_0)=y_0$ on every such interval.

---

## Phase 2: Choice of Method and Change of Variables

Why this method: when $y' = f(x)$ with $f$ continuous on an interval, the Fundamental Theorem of Calculus gives an antiderivative $F$, and two antiderivatives on an interval differ by a constant (a function with zero derivative on an interval is constant, by the Mean Value Theorem). So direct integration produces all solutions.

Change of variables: none is needed for the equation itself. Where an integral is not immediate, a substitution is written explicitly: $u = 3x$ in (i), $u = x^2$ in (iii), $u = 1+x^2$ in (v), and a polynomial division (rewriting $x = (1+x) - 1$) in (iv). Constants of integration are attached separately on each interval of continuity.

$$
y(x) = \int f(x)\,dx = F(x) + C.
$$

---

## Phase 3: Step-by-Step Derivation

### Part (i): $y' = e^{3x} - x$

Integrate term by term:

$$
y(x) = \int e^{3x}\,dx - \int x\,dx.
$$

For the first integral put $u = 3x$, so $du = 3\,dx$ and $dx = du/3$:

$$
\int e^{3x}\,dx = \frac{1}{3}\int e^{u}\,du = \frac{1}{3}e^{u} = \frac{1}{3}e^{3x}.
$$

The second integral is $\int x\,dx = x^2/2$. Hence

$$
y(x) = \frac{1}{3}e^{3x} - \frac{x^2}{2} + C, \qquad C \in \mathbb{R},\ x \in \mathbb{R}.
$$

### Part (ii): $x\,y' = 1$

On each interval $x \neq 0$ divide by $x$ to get $y' = 1/x$. Then

$$
y(x) = \int \frac{dx}{x} = \ln\lvert x\rvert + C.
$$

The absolute value is needed: for $x>0$, $\frac{d}{dx}\ln x = 1/x$; for $x<0$, $\frac{d}{dx}\ln(-x) = \frac{-1}{-x} = \frac{1}{x}$. The two half-lines are not connected, so the constants are independent:

$$
y(x) = \begin{cases} \ln x + C_1, & x>0,\\ \ln(-x) + C_2, & x<0, \end{cases} \qquad C_1, C_2 \in \mathbb{R}.
$$

### Part (iii): $y' = x e^{x^2}$

Substitute $u = x^2$, so $du = 2x\,dx$ and $x\,dx = du/2$:

$$
y(x) = \int x e^{x^2}\,dx = \frac{1}{2}\int e^{u}\,du = \frac{1}{2}e^{u} + C = \frac{1}{2}e^{x^2} + C.
$$

### Part (iv): $(1+x)\,y' = x$

On each interval $x \neq -1$ divide by $1+x$ and rewrite the numerator as $x = (1+x) - 1$:

$$
y'(x) = \frac{x}{1+x} = \frac{(1+x) - 1}{1+x} = 1 - \frac{1}{1+x}.
$$

Integrate, using $u = 1+x$, $du = dx$ for the second term:

$$
y(x) = \int 1\,dx - \int \frac{du}{u} = x - \ln\lvert 1+x\rvert + C.
$$

Again the constants are independent on $(-\infty,-1)$ and on $(-1,\infty)$:

$$
y(x) = x - \ln\lvert 1+x\rvert + C_{\pm}.
$$

### Part (v): $(1+x^2)\,y' = x$

Since $1+x^2 > 0$ on all of $\mathbb{R}$, divide: $y' = x/(1+x^2)$. Substitute $u = 1+x^2$, so $du = 2x\,dx$ and $x\,dx = du/2$:

$$
y(x) = \int \frac{x\,dx}{1+x^2} = \frac{1}{2}\int \frac{du}{u} = \frac{1}{2}\ln\lvert u\rvert + C = \frac{1}{2}\ln(1+x^2) + C.
$$

No absolute value is needed because $u = 1+x^2 > 0$.

---

## Phase 4: Verification, Limits and Interpretation

Check each result by differentiating (chain rule written out):

- (i) $\frac{d}{dx}\left[\tfrac13 e^{3x} - \tfrac{x^2}{2} + C\right] = \tfrac13\cdot 3e^{3x} - x = e^{3x} - x$.
- (ii) $x\cdot \frac{d}{dx}\ln\lvert x\rvert = x\cdot\frac{1}{x} = 1$ for $x \neq 0$.
- (iii) $\frac{d}{dx}\left[\tfrac12 e^{x^2}\right] = \tfrac12 e^{x^2}\cdot 2x = x e^{x^2}$.
- (iv) $(1+x)\,\frac{d}{dx}\left[x - \ln\lvert 1+x\rvert\right] = (1+x)\left(1 - \frac{1}{1+x}\right) = (1+x) - 1 = x$.
- (v) $(1+x^2)\,\frac{d}{dx}\left[\tfrac12\ln(1+x^2)\right] = (1+x^2)\cdot\frac{1}{2}\cdot\frac{2x}{1+x^2} = x$.

Symbolic check with sympy (dsolve and differentiation of the closed forms) reproduces the five results above.

Domain remarks: the solutions of (i), (iii), (v) are defined on all of $\mathbb{R}$. For (ii) and (iv) the solution cannot be extended through $x=0$ and $x=-1$ respectively, because the equation itself is inconsistent there ($0=1$ and $0=-1$), and $\ln\lvert x\rvert$, $\ln\lvert 1+x\rvert$ are unbounded at those points. The equations in (iv) and (v) look similar but behave differently: only (iv) has a singular point, since $1+x$ vanishes at $x=-1$ whereas $1+x^2$ never vanishes.

#### Results

| Part | General solution | Domain |
| :--- | :--- | :--- |
| (i) | $y = \tfrac13 e^{3x} - \tfrac12 x^2 + C$ | $\mathbb{R}$ |
| (ii) | $y = \ln\lvert x\rvert + C_{\pm}$ | $x \neq 0$ |
| (iii) | $y = \tfrac12 e^{x^2} + C$ | $\mathbb{R}$ |
| (iv) | $y = x - \ln\lvert 1+x\rvert + C_{\pm}$ | $x \neq -1$ |
| (v) | $y = \tfrac12 \ln(1+x^2) + C$ | $\mathbb{R}$ |

---

## Related Notes

- [[04 - Advanced Maths/Concept - Direct Integration and Separable Equations|Direct integration and separable equations]]
- [[04 - Advanced Maths/Problem - Ch2-P2 Separable ODEs and Asymptotic Integrals|Problem 2.2: separable equations]]
