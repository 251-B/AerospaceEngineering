---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 1"
dificultad: media
id: "e1"
pill: "Undetermined Coefficients • 11 IVPs • Resonance"
tags:
  - problema-resuelto
  - coeficientes-indeterminados
  - resonancia
  - pvi-segundo-orden
  - oscilaciones
---

# Problem 3.II.1: Constant-Coefficient Equations with Forcing (Eleven IVPs)

> Official exercise 1 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

Find the general solution of the following differential equations. You will find it useful to look up Exercise 4 of Chapter 3, part 1. For each item $(n)$, find the unique solution such that $x(0) = n$ and $\dot x(0) = 0$. E.g. for item (iii), $x(0) = 3$, etc.

- (i) $\ddot x - 4x = t^2$;
- (ii) $\ddot x - 4\dot x = t^2$;
- (iii) $\ddot x + \dot x - 2x = 3e^{-t}$;
- (iv) $\ddot x + \dot x - 2x = e^{t}$;
- (v) $\ddot x + 2\dot x + x = e^{-t}$;
- (vi) $\ddot x + \omega^2 x = \sin(\alpha t)\ \text{ for } \alpha \neq \omega$;
- (vii) $\ddot x + \omega^2 x = \sin(\alpha t)\ \text{ for } \alpha = \omega$;
- (viii) $\ddot x + 2\dot x + 10x = e^{-t}$;
- (ix) $\ddot x + 2\dot x + 10x = e^{-t}\cos(3t)$;
- (x) $\ddot x + 6\dot x + 10x = e^{-3t}\cos t$,
- (xi) $\ddot x + 4\dot x + 4x = e^{2t}$;

## Phase 1: Setup, classification and data

All eleven equations are **linear, second-order, inhomogeneous equations with constant coefficients**, $L[x] = \ddot x + b\dot x + cx = f(t)$ (the coefficient of $\ddot x$ is $1$). The forcing $f$ is built from polynomials, exponentials and sinusoids, so the method of undetermined coefficients applies (Robinson Ch. 14). Hypotheses: for (vi) and (vii) the parameters $\omega > 0$ and $\alpha$ are real, with $\alpha \neq \omega$ in (vi) and $\alpha = \omega$ in (vii).

The coefficients are continuous on all of $\mathbb R$, so for every pair of initial data there is exactly one solution, defined for all $t$ (existence and uniqueness, Robinson Thm 11.1 and Thm 16.1). The data of item $(n)$ are $x(0) = n$, $\dot x(0) = 0$, with $n$ the position of the item in the list:

| Item | Equation $L[x] = f$ | $x(0)$ | $\dot x(0)$ |
| :--- | :--- | :--- | :--- |
| (i) | $\ddot x - 4x = t^2$ | 1 | 0 |
| (ii) | $\ddot x - 4\dot x = t^2$ | 2 | 0 |
| (iii) | $\ddot x + \dot x - 2x = 3e^{-t}$ | 3 | 0 |
| (iv) | $\ddot x + \dot x - 2x = e^{t}$ | 4 | 0 |
| (v) | $\ddot x + 2\dot x + x = e^{-t}$ | 5 | 0 |
| (vi) | $\ddot x + \omega^2 x = \sin(\alpha t)\ \text{ for } \alpha \neq \omega$ | 6 | 0 |
| (vii) | $\ddot x + \omega^2 x = \sin(\alpha t)\ \text{ for } \alpha = \omega$ | 7 | 0 |
| (viii) | $\ddot x + 2\dot x + 10x = e^{-t}$ | 8 | 0 |
| (ix) | $\ddot x + 2\dot x + 10x = e^{-t}\cos(3t)$ | 9 | 0 |
| (x) | $\ddot x + 6\dot x + 10x = e^{-3t}\cos t$ | 10 | 0 |
| (xi) | $\ddot x + 4\dot x + 4x = e^{2t}$ | 11 | 0 |

Strategy (Robinson Sec. 14.1, Lemma): the general solution of $L[x] = f$ is $x = x_h + x_p$, with $x_h$ the general solution of $L[x] = 0$ (two arbitrary constants $c_1, c_2$) and $x_p$ any one particular solution. The constants are then fixed by the two initial conditions.

## Phase 2: Method, notation and the guess for each item

Write $P(k) = k^2 + bk + c$ for the characteristic polynomial. A forcing $c_0\,t^m e^{\sigma t}\{\cos\omega t, \sin\omega t\}$ is, for the purpose of the guess, the exponent $s = \sigma + i\omega$ (and $s = \sigma$ when there is no sinusoid; $s = 0$ for a polynomial). Rule of thumb (Robinson Sec. 14.5, p. 139): take the standard guess of the same form as $f$ with undetermined coefficients, and multiply it by $t^{m_s}$ where $m_s$ is the multiplicity of $s$ as a root of $P$ ($m_s = 0$ when $P(s) \neq 0$).

| Forcing | Standard guess $x_p$ | If $s$ is a root of $P$ of multiplicity $m_s$ |
| :--- | :--- | :--- |
| polynomial of degree $m$ | $K_0 + K_1t + \dots + K_mt^m$ | multiply by $t^{m_s}$ |
| $e^{\sigma t}$ | $Ke^{\sigma t}$ | $Kt^{m_s}e^{\sigma t}$ |
| $\sin\omega t$ or $\cos\omega t$ | $K_1\cos\omega t + K_2\sin\omega t$ (both, always) | $t^{m_s}(K_1\cos\omega t + K_2\sin\omega t)$ |
| $e^{\sigma t}\cos\omega t$ | $e^{\sigma t}(K_1\cos\omega t + K_2\sin\omega t)$ | $t^{m_s}e^{\sigma t}(K_1\cos\omega t + K_2\sin\omega t)$ |

Applying the rule item by item (the roots of $P$ were found in Exercise 4 of part 1 for the homogeneous equations; the last column is $m_s$):

| Item | $P(k)$ | Roots of $P$ | Exponent $s$ of $f$ | $m_s$ |
| :--- | :--- | :--- | :--- | :--- |
| (i) | $k^{2} - 4$ | $-2, 2$ | $0$ | 0 |
| (ii) | $k^{2} - 4 k$ | $0, 4$ | $0$ | 1 |
| (iii) | $k^{2} + k - 2$ | $-2, 1$ | $-1$ | 0 |
| (iv) | $k^{2} + k - 2$ | $-2, 1$ | $1$ | 1 |
| (v) | $k^{2} + 2 k + 1$ | $-1\ (\text{double})$ | $-1$ | 2 |
| (vi) | $k^{2} + \omega^{2}$ | $- i \omega, i \omega$ | $i \alpha$ | 0 |
| (vii) | $k^{2} + \omega^{2}$ | $- i \omega, i \omega$ | $i \omega$ | 1 |
| (viii) | $k^{2} + 2 k + 10$ | $-1 - 3 i, -1 + 3 i$ | $-1$ | 0 |
| (ix) | $k^{2} + 2 k + 10$ | $-1 - 3 i, -1 + 3 i$ | $-1 + 3 i$ | 1 |
| (x) | $k^{2} + 6 k + 10$ | $-3 - i, -3 + i$ | $-3 + i$ | 1 |
| (xi) | $k^{2} + 4 k + 4$ | $-2\ (\text{double})$ | $2$ | 0 |

Items with $m_s \geq 1$ (resonant forcing, marked by a non-zero last column) need the extra factor $t^{m_s}$: (ii), (iv), (v), (vii), (ix), (x).

> [!info] Method of the class notes [Notes, p. 6]
> The notes split the solution as $x = x_H + x_N$ (if $x_N$ is one solution, $\Phi = x - x_N$ solves the homogeneous equation) and choose $x_N$ by an educated guess: a polynomial of order $n$ gives a full polynomial; $Ce^{\alpha t}$ gives $Ae^{\alpha t}$ when $\alpha$ is not a root (Case 1) and $Ate^{\alpha t}$ when it is (Case 2); $\alpha\cos\omega t + \beta\sin\omega t$ gives $A\cos\omega t + B\sin\omega t$, times $t$ if it is already in $x_H$; sums are decomposed. The factor $t^{m_s}$ of the table above is the same rule, with $t^2$ for a double root (a complement: the notes treat the simple root).

## Phase 3: Step-by-step derivation of the eleven solutions

### (i) $\ddot{x} - 4x = t^{2}$, with $x(0) = 1$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} - 4x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 4 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (0)^2 - 4(1)(-4) = 16$.

Factorising, $P(k) = \left(k - 2\right) \left(k + 2\right)$, so the roots are

$$ k = -2, \qquad k = 2 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-2 t}$, $e^{2 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-2 t} + c_{2} e^{2 t} $$

The forcing $t^{2}$ is a polynomial of degree 2; a polynomial is $e^{0t}$ times a polynomial, so the exponent to test is $s = 0$: $P(0) = -4$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} + K_{2} t + K_{3} t^{2} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= K_{2} + 2 K_{3} t \\ x_p''(t) &= 2 K_{3} \end{aligned} $$

Substitute into $L[x_p] = x_p'' - 4x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = - 4 K_{3}\,t^{2} - 4 K_{2}\,t + \left(- 4 K_{1} + 2 K_{3}\right) $$

This must equal the forcing $f(t) = t^{2}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} t^{2}: &\quad - 4 K_{3} = 1 \\ t: &\quad - 4 K_{2} = 0 \\ 1: &\quad - 4 K_{1} + 2 K_{3} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 4 K_{3} &= 1 \quad (1) \\ - 4 K_{2} &= 0 \quad (2) \\ - 4 K_{1} + 2 K_{3} &= 0 \quad (3) \end{aligned} $$

$- 4 K_{3} = 1$ contains one unknown only, so $K_{3} = - \frac{1}{4}$.

Substitute in $- 4 K_{1} + 2 K_{3} = 0$: $- 4 K_{1} - \frac{1}{2} = 0$.

$- 4 K_{2} = 0$ contains one unknown only, so $K_{2} = 0$.

$- 4 K_{1} - \frac{1}{2} = 0$ contains one unknown only, so $K_{1} = - \frac{1}{8}$.

Hence $K_{1} = - \frac{1}{8}$, $K_{2} = 0$, $K_{3} = - \frac{1}{4}$.

Therefore

$$ x_p(t) = - \frac{t^{2}}{4} - \frac{1}{8} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-2 t} + c_{2} e^{2 t} - \frac{t^{2}}{4} - \frac{1}{8} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 2 c_{1} e^{-2 t} + 2 c_{2} e^{2 t} - \frac{t}{2} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} - \frac{1}{8} = 1 \\ x'(0) &= - 2 c_{1} + 2 c_{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} - \frac{1}{8} &= 1 \quad (1) \\ - 2 c_{1} + 2 c_{2} &= 0 \quad (2) \end{aligned} $$

Solve $c_{1} + c_{2} - \frac{1}{8} = 1$ for $c_{1}$: $c_{1} = \frac{9}{8} - c_{2}$.

Substitute in $- 2 c_{1} + 2 c_{2} = 0$: $4 c_{2} - \frac{9}{4} = 0$.

$4 c_{2} - \frac{9}{4} = 0$ contains one unknown only, so $c_{2} = \frac{9}{16}$.

Back-substitution: $c_{1} = \frac{9}{8} - c_{2} = \frac{9}{16}$.

Hence $c_{1} = \frac{9}{16}$, $c_{2} = \frac{9}{16}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = - \frac{t^{2}}{4} + \frac{9 e^{2 t}}{16} - \frac{1}{8} + \frac{9 e^{-2 t}}{16}} $$

### (ii) $\ddot{x} - 4\dot{x} = t^{2}$, with $x(0) = 2$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} - 4\dot{x} = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 4 k = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (-4)^2 - 4(1)(0) = 16$.

Factorising, $P(k) = k \left(k - 4\right)$, so the roots are

$$ k = 0, \qquad k = 4 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $1$, $e^{4 t}$, so the complementary function is

$$ x_h(t) = c_{1} + c_{2} e^{4 t} $$

The forcing $t^{2}$ is a polynomial of degree 2; a polynomial is $e^{0t}$ times a polynomial, so the exponent to test is $s = 0$: $P(0) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t + K_{2} t^{2} + K_{3} t^{3} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= K_{1} + 2 K_{2} t + 3 K_{3} t^{2} \\ x_p''(t) &= 2 K_{2} + 6 K_{3} t \end{aligned} $$

Substitute into $L[x_p] = x_p'' - 4x_p'$ and collect the terms that multiply the same function:

$$ L[x_p] = - 12 K_{3}\,t^{2} + \left(- 8 K_{2} + 6 K_{3}\right)\,t + \left(- 4 K_{1} + 2 K_{2}\right) $$

This must equal the forcing $f(t) = t^{2}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} t^{2}: &\quad - 12 K_{3} = 1 \\ t: &\quad - 8 K_{2} + 6 K_{3} = 0 \\ 1: &\quad - 4 K_{1} + 2 K_{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 12 K_{3} &= 1 \quad (1) \\ - 8 K_{2} + 6 K_{3} &= 0 \quad (2) \\ - 4 K_{1} + 2 K_{2} &= 0 \quad (3) \end{aligned} $$

$- 12 K_{3} = 1$ contains one unknown only, so $K_{3} = - \frac{1}{12}$.

Substitute in $- 8 K_{2} + 6 K_{3} = 0$: $- 8 K_{2} - \frac{1}{2} = 0$.

$- 8 K_{2} - \frac{1}{2} = 0$ contains one unknown only, so $K_{2} = - \frac{1}{16}$.

Substitute in $- 4 K_{1} + 2 K_{2} = 0$: $- 4 K_{1} - \frac{1}{8} = 0$.

$- 4 K_{1} - \frac{1}{8} = 0$ contains one unknown only, so $K_{1} = - \frac{1}{32}$.

Hence $K_{1} = - \frac{1}{32}$, $K_{2} = - \frac{1}{16}$, $K_{3} = - \frac{1}{12}$.

Therefore

$$ x_p(t) = - \frac{t^{3}}{12} - \frac{t^{2}}{16} - \frac{t}{32} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} + c_{2} e^{4 t} - \frac{t^{3}}{12} - \frac{t^{2}}{16} - \frac{t}{32} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= 4 c_{2} e^{4 t} - \frac{t^{2}}{4} - \frac{t}{8} - \frac{1}{32} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} = 2 \\ x'(0) &= 4 c_{2} - \frac{1}{32} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} &= 2 \quad (1) \\ 4 c_{2} - \frac{1}{32} &= 0 \quad (2) \end{aligned} $$

$4 c_{2} - \frac{1}{32} = 0$ contains one unknown only, so $c_{2} = \frac{1}{128}$.

Substitute in $c_{1} + c_{2} = 2$: $c_{1} + \frac{1}{128} = 2$.

$c_{1} + \frac{1}{128} = 2$ contains one unknown only, so $c_{1} = \frac{255}{128}$.

Hence $c_{1} = \frac{255}{128}$, $c_{2} = \frac{1}{128}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = - \frac{t^{3}}{12} - \frac{t^{2}}{16} - \frac{t}{32} + \frac{e^{4 t}}{128} + \frac{255}{128}} $$

### (iii) $\ddot{x} + \dot{x} - 2x = 3 e^{-t}$, with $x(0) = 3$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + \dot{x} - 2x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + k - 2 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (1)^2 - 4(1)(-2) = 9$.

Factorising, $P(k) = \left(k - 1\right) \left(k + 2\right)$, so the roots are

$$ k = -2, \qquad k = 1 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-2 t}$, $e^{t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-2 t} + c_{2} e^{t} $$

The forcing $3 e^{-t}$ is an exponential with exponent $s = -1$; we test it in the characteristic polynomial: $P(-1) = -2$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} e^{-t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} e^{-t} \\ x_p''(t) &= K_{1} e^{-t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + x_p' - 2x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = - 2 K_{1}\,e^{-t} $$

This must equal the forcing $f(t) = 3 e^{-t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{-t}: &\quad - 2 K_{1} = 3 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 2 K_{1} &= 3 \quad (1) \end{aligned} $$

$- 2 K_{1} = 3$ contains one unknown only, so $K_{1} = - \frac{3}{2}$.

Hence $K_{1} = - \frac{3}{2}$.

Therefore

$$ x_p(t) = - \frac{3 e^{-t}}{2} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-2 t} + c_{2} e^{t} - \frac{3 e^{-t}}{2} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 2 c_{1} e^{-2 t} + c_{2} e^{t} + \frac{3 e^{-t}}{2} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} - \frac{3}{2} = 3 \\ x'(0) &= - 2 c_{1} + c_{2} + \frac{3}{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} - \frac{3}{2} &= 3 \quad (1) \\ - 2 c_{1} + c_{2} + \frac{3}{2} &= 0 \quad (2) \end{aligned} $$

Solve $c_{1} + c_{2} - \frac{3}{2} = 3$ for $c_{1}$: $c_{1} = \frac{9}{2} - c_{2}$.

Substitute in $- 2 c_{1} + c_{2} + \frac{3}{2} = 0$: $3 c_{2} - \frac{15}{2} = 0$.

$3 c_{2} - \frac{15}{2} = 0$ contains one unknown only, so $c_{2} = \frac{5}{2}$.

Back-substitution: $c_{1} = \frac{9}{2} - c_{2} = 2$.

Hence $c_{1} = 2$, $c_{2} = \frac{5}{2}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{5 e^{t}}{2} - \frac{3 e^{-t}}{2} + 2 e^{-2 t}} $$

### (iv) $\ddot{x} + \dot{x} - 2x = e^{t}$, with $x(0) = 4$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + \dot{x} - 2x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + k - 2 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (1)^2 - 4(1)(-2) = 9$.

Factorising, $P(k) = \left(k - 1\right) \left(k + 2\right)$, so the roots are

$$ k = -2, \qquad k = 1 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-2 t}$, $e^{t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-2 t} + c_{2} e^{t} $$

The forcing $e^{t}$ is an exponential with exponent $s = 1$; we test it in the characteristic polynomial: $P(1) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t e^{t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= K_{1} t e^{t} + K_{1} e^{t} \\ x_p''(t) &= K_{1} t e^{t} + 2 K_{1} e^{t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + x_p' - 2x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 3 K_{1}\,e^{t} $$

This must equal the forcing $f(t) = e^{t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{t}: &\quad 3 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} 3 K_{1} &= 1 \quad (1) \end{aligned} $$

$3 K_{1} = 1$ contains one unknown only, so $K_{1} = \frac{1}{3}$.

Hence $K_{1} = \frac{1}{3}$.

Therefore

$$ x_p(t) = \frac{t e^{t}}{3} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-2 t} + c_{2} e^{t} + \frac{t e^{t}}{3} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 2 c_{1} e^{-2 t} + c_{2} e^{t} + \frac{t e^{t}}{3} + \frac{e^{t}}{3} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} = 4 \\ x'(0) &= - 2 c_{1} + c_{2} + \frac{1}{3} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} &= 4 \quad (1) \\ - 2 c_{1} + c_{2} + \frac{1}{3} &= 0 \quad (2) \end{aligned} $$

Solve $c_{1} + c_{2} = 4$ for $c_{1}$: $c_{1} = 4 - c_{2}$.

Substitute in $- 2 c_{1} + c_{2} + \frac{1}{3} = 0$: $3 c_{2} - \frac{23}{3} = 0$.

$3 c_{2} - \frac{23}{3} = 0$ contains one unknown only, so $c_{2} = \frac{23}{9}$.

Back-substitution: $c_{1} = 4 - c_{2} = \frac{13}{9}$.

Hence $c_{1} = \frac{13}{9}$, $c_{2} = \frac{23}{9}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{t e^{t}}{3} + \frac{23 e^{t}}{9} + \frac{13 e^{-2 t}}{9}} $$

### (v) $\ddot{x} + 2\dot{x} + x = e^{-t}$, with $x(0) = 5$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + 2\dot{x} + x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + 2 k + 1 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (2)^2 - 4(1)(1) = 0$.

Factorising, $P(k) = \left(k + 1\right)^{2}$, so the roots are

$$ k = -1 \ \text{(multiplicity 2)} $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-t}$, $t e^{-t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-t} + c_{2} t e^{-t} $$

The forcing $e^{-t}$ is an exponential with exponent $s = -1$; we test it in the characteristic polynomial: $P(-1) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $2$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{2}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t^{2} e^{-t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} t^{2} e^{-t} + 2 K_{1} t e^{-t} \\ x_p''(t) &= K_{1} t^{2} e^{-t} - 4 K_{1} t e^{-t} + 2 K_{1} e^{-t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + 2x_p' + x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 2 K_{1}\,e^{-t} $$

This must equal the forcing $f(t) = e^{-t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{-t}: &\quad 2 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} 2 K_{1} &= 1 \quad (1) \end{aligned} $$

$2 K_{1} = 1$ contains one unknown only, so $K_{1} = \frac{1}{2}$.

Hence $K_{1} = \frac{1}{2}$.

Therefore

$$ x_p(t) = \frac{t^{2} e^{-t}}{2} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-t} + c_{2} t e^{-t} + \frac{t^{2} e^{-t}}{2} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - c_{1} e^{-t} - c_{2} t e^{-t} + c_{2} e^{-t} - \frac{t^{2} e^{-t}}{2} + t e^{-t} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} = 5 \\ x'(0) &= - c_{1} + c_{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} &= 5 \quad (1) \\ - c_{1} + c_{2} &= 0 \quad (2) \end{aligned} $$

$c_{1} = 5$ contains one unknown only, so $c_{1} = 5$.

Substitute in $- c_{1} + c_{2} = 0$: $c_{2} - 5 = 0$.

$c_{2} - 5 = 0$ contains one unknown only, so $c_{2} = 5$.

Hence $c_{1} = 5$, $c_{2} = 5$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{t^{2} e^{-t}}{2} + 5 t e^{-t} + 5 e^{-t}} $$

### (vi) $\ddot{x} + \omega^{2}x = \sin{\alpha t}$, with $x(0) = 6$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + \omega^{2}x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + \omega^{2} = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (0)^2 - 4(1)(\omega^{2}) = - 4 \omega^{2}$.

Factorising, $P(k) = \left(k - i \omega\right) \left(k + i \omega\right)$, so the roots are

$$ k = - i \omega, \qquad k = i \omega $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $\cos{\omega t}$, $\sin{\omega t}$, so the complementary function is

$$ x_h(t) = c_{1} \cos{\omega t} + c_{2} \sin{\omega t} $$

The forcing $\sin{\alpha t}$ is a sinusoidal term: it is the real or imaginary part of $e^{(i \alpha)t}$, so we test $s = i \alpha$ in the characteristic polynomial: $P(i \alpha) = - \alpha^{2} + \omega^{2}$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} \cos{\alpha t} + K_{2} \sin{\alpha t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} \alpha \sin{\alpha t} + K_{2} \alpha \cos{\alpha t} \\ x_p''(t) &= - K_{1} \alpha^{2} \cos{\alpha t} - K_{2} \alpha^{2} \sin{\alpha t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + \omega^{2}x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = \left(- K_{1} \alpha^{2} + K_{1} \omega^{2}\right)\,\cos \alpha\,t + \left(- K_{2} \alpha^{2} + K_{2} \omega^{2}\right)\,\sin \alpha\,t $$

This must equal the forcing $f(t) = \sin{\alpha t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} \cos \alpha\,t: &\quad - K_{1} \alpha^{2} + K_{1} \omega^{2} = 0 \\ \sin \alpha\,t: &\quad - K_{2} \alpha^{2} + K_{2} \omega^{2} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} - K_{1} \alpha^{2} + K_{1} \omega^{2} &= 0 \quad (1) \\ - K_{2} \alpha^{2} + K_{2} \omega^{2} &= 1 \quad (2) \end{aligned} $$

$- K_{1} \alpha^{2} + K_{1} \omega^{2} = 0$ contains one unknown only, so $K_{1} = 0$.

$- K_{2} \alpha^{2} + K_{2} \omega^{2} = 1$ contains one unknown only, so $K_{2} = - \frac{1}{\alpha^{2} - \omega^{2}}$.

Hence $K_{1} = 0$, $K_{2} = - \frac{1}{\alpha^{2} - \omega^{2}}$.

Therefore

$$ x_p(t) = - \frac{\sin{\alpha t}}{\alpha^{2} - \omega^{2}} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} \cos{\omega t} + c_{2} \sin{\omega t} - \frac{\sin{\alpha t}}{\alpha^{2} - \omega^{2}} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - \frac{\alpha \cos{\alpha t}}{\alpha^{2} - \omega^{2}} - c_{1} \omega \sin{\omega t} + c_{2} \omega \cos{\omega t} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} = 6 \\ x'(0) &= - \frac{\alpha}{\alpha^{2} - \omega^{2}} + c_{2} \omega = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} &= 6 \quad (1) \\ - \frac{\alpha}{\alpha^{2} - \omega^{2}} + c_{2} \omega &= 0 \quad (2) \end{aligned} $$

$c_{1} = 6$ contains one unknown only, so $c_{1} = 6$.

$- \frac{\alpha}{\alpha^{2} - \omega^{2}} + c_{2} \omega = 0$ contains one unknown only, so $c_{2} = \frac{\alpha}{\alpha^{2} \omega - \omega^{3}}$.

Hence $c_{1} = 6$, $c_{2} = \frac{\alpha}{\alpha^{2} \omega - \omega^{3}}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{\alpha \sin{\omega t}}{\alpha^{2} \omega - \omega^{3}} + 6 \cos{\omega t} - \frac{\sin{\alpha t}}{\alpha^{2} - \omega^{2}}} $$

Writing the same solution with the denominator $\omega^2 - \alpha^2$ that appears naturally in the guess (check: $-\frac{1}{\alpha^2 - \omega^2} = \frac{1}{\omega^2 - \alpha^2}$ and $\frac{\alpha}{\alpha^2\omega - \omega^3} = -\frac{\alpha}{\omega(\omega^2 - \alpha^2)}$):

$$ \boxed{x(t) = 6\cos\omega t + \frac{\sin\alpha t - \dfrac{\alpha}{\omega}\sin\omega t}{\omega^2 - \alpha^2}} $$

The first term carries the initial displacement $x(0) = 6$; the fraction vanishes at $t = 0$ and has zero slope there ($\alpha\cos 0 - \alpha\cos 0 = 0$ after dividing by $\omega^2 - \alpha^2$), so the initial conditions hold.

### (vii) $\ddot{x} + \omega^{2}x = \sin{\omega t}$, with $x(0) = 7$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + \omega^{2}x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + \omega^{2} = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (0)^2 - 4(1)(\omega^{2}) = - 4 \omega^{2}$.

Factorising, $P(k) = \left(k - i \omega\right) \left(k + i \omega\right)$, so the roots are

$$ k = - i \omega, \qquad k = i \omega $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $\cos{\omega t}$, $\sin{\omega t}$, so the complementary function is

$$ x_h(t) = c_{1} \cos{\omega t} + c_{2} \sin{\omega t} $$

The forcing $\sin{\omega t}$ is a sinusoidal term: it is the real or imaginary part of $e^{(i \omega)t}$, so we test $s = i \omega$ in the characteristic polynomial: $P(i \omega) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t \cos{\omega t} + K_{2} t \sin{\omega t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} \omega t \sin{\omega t} + K_{1} \cos{\omega t} + K_{2} \omega t \cos{\omega t} + K_{2} \sin{\omega t} \\ x_p''(t) &= - K_{1} \omega^{2} t \cos{\omega t} - 2 K_{1} \omega \sin{\omega t} - K_{2} \omega^{2} t \sin{\omega t} + 2 K_{2} \omega \cos{\omega t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + \omega^{2}x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 2 K_{2} \omega\,\cos \omega\,t - 2 K_{1} \omega\,\sin \omega\,t $$

This must equal the forcing $f(t) = \sin{\omega t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} \cos \omega\,t: &\quad 2 K_{2} \omega = 0 \\ \sin \omega\,t: &\quad - 2 K_{1} \omega = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} 2 K_{2} \omega &= 0 \quad (1) \\ - 2 K_{1} \omega &= 1 \quad (2) \end{aligned} $$

$2 K_{2} \omega = 0$ contains one unknown only, so $K_{2} = 0$.

$- 2 K_{1} \omega = 1$ contains one unknown only, so $K_{1} = - \frac{1}{2 \omega}$.

Hence $K_{1} = - \frac{1}{2 \omega}$, $K_{2} = 0$.

Therefore

$$ x_p(t) = - \frac{t \cos{\omega t}}{2 \omega} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} \cos{\omega t} + c_{2} \sin{\omega t} - \frac{t \cos{\omega t}}{2 \omega} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - c_{1} \omega \sin{\omega t} + c_{2} \omega \cos{\omega t} + \frac{t \sin{\omega t}}{2} - \frac{\cos{\omega t}}{2 \omega} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} = 7 \\ x'(0) &= c_{2} \omega - \frac{1}{2 \omega} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} &= 7 \quad (1) \\ c_{2} \omega - \frac{1}{2 \omega} &= 0 \quad (2) \end{aligned} $$

$c_{1} = 7$ contains one unknown only, so $c_{1} = 7$.

$c_{2} \omega - \frac{1}{2 \omega} = 0$ contains one unknown only, so $c_{2} = \frac{1}{2 \omega^{2}}$.

Hence $c_{1} = 7$, $c_{2} = \frac{1}{2 \omega^{2}}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = 7 \cos{\omega t} - \frac{t \cos{\omega t}}{2 \omega} + \frac{\sin{\omega t}}{2 \omega^{2}}} $$

Check of the resonant solution by the limit $\alpha \to \omega$ of the forced part of item (vi), the fraction, which does not depend on the initial data (L'Hopital's rule, differentiating numerator and denominator with respect to $\alpha$):

$$ \lim_{\alpha\to\omega}\frac{\sin\alpha t - \frac{\alpha}{\omega}\sin\omega t}{\omega^2 - \alpha^2} = \lim_{\alpha\to\omega}\frac{t\cos\alpha t - \frac{1}{\omega}\sin\omega t}{-2\alpha} = \frac{t\cos\omega t - \frac{1}{\omega}\sin\omega t}{-2\omega} = -\frac{t\cos\omega t}{2\omega} + \frac{\sin\omega t}{2\omega^2} $$

which is exactly the zero-data (forced) part of the resonant solution just found, i.e. everything except $7\cos\omega t$: the resonant solution is the limit of the non-resonant ones.

### (viii) $\ddot{x} + 2\dot{x} + 10x = e^{-t}$, with $x(0) = 8$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + 2\dot{x} + 10x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + 2 k + 10 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (2)^2 - 4(1)(10) = -36$.

Factorising, $P(k) = \left(k + 1 - 3 i\right) \left(k + 1 + 3 i\right)$, so the roots are

$$ k = -1 - 3 i, \qquad k = -1 + 3 i $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-t} \cos{3 t}$, $e^{-t} \sin{3 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-t} \cos{3 t} + c_{2} e^{-t} \sin{3 t} $$

The forcing $e^{-t}$ is an exponential with exponent $s = -1$; we test it in the characteristic polynomial: $P(-1) = 9$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} e^{-t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} e^{-t} \\ x_p''(t) &= K_{1} e^{-t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + 2x_p' + 10x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 9 K_{1}\,e^{-t} $$

This must equal the forcing $f(t) = e^{-t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{-t}: &\quad 9 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} 9 K_{1} &= 1 \quad (1) \end{aligned} $$

$9 K_{1} = 1$ contains one unknown only, so $K_{1} = \frac{1}{9}$.

Hence $K_{1} = \frac{1}{9}$.

Therefore

$$ x_p(t) = \frac{e^{-t}}{9} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-t} \cos{3 t} + c_{2} e^{-t} \sin{3 t} + \frac{e^{-t}}{9} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 3 c_{1} e^{-t} \sin{3 t} - c_{1} e^{-t} \cos{3 t} - c_{2} e^{-t} \sin{3 t} + 3 c_{2} e^{-t} \cos{3 t} - \frac{e^{-t}}{9} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + \frac{1}{9} = 8 \\ x'(0) &= - c_{1} + 3 c_{2} - \frac{1}{9} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + \frac{1}{9} &= 8 \quad (1) \\ - c_{1} + 3 c_{2} - \frac{1}{9} &= 0 \quad (2) \end{aligned} $$

$c_{1} + \frac{1}{9} = 8$ contains one unknown only, so $c_{1} = \frac{71}{9}$.

Substitute in $- c_{1} + 3 c_{2} - \frac{1}{9} = 0$: $3 c_{2} - 8 = 0$.

$3 c_{2} - 8 = 0$ contains one unknown only, so $c_{2} = \frac{8}{3}$.

Hence $c_{1} = \frac{71}{9}$, $c_{2} = \frac{8}{3}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{8 e^{-t} \sin{3 t}}{3} + \frac{71 e^{-t} \cos{3 t}}{9} + \frac{e^{-t}}{9}} $$

### (ix) $\ddot{x} + 2\dot{x} + 10x = e^{-t} \cos{3 t}$, with $x(0) = 9$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + 2\dot{x} + 10x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + 2 k + 10 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (2)^2 - 4(1)(10) = -36$.

Factorising, $P(k) = \left(k + 1 - 3 i\right) \left(k + 1 + 3 i\right)$, so the roots are

$$ k = -1 - 3 i, \qquad k = -1 + 3 i $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-t} \cos{3 t}$, $e^{-t} \sin{3 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-t} \cos{3 t} + c_{2} e^{-t} \sin{3 t} $$

The forcing $e^{-t} \cos{3 t}$ is a sinusoidal term times an exponential: it is the real or imaginary part of $e^{(-1 + 3 i)t}$, so we test $s = -1 + 3 i$ in the characteristic polynomial: $P(-1 + 3 i) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t e^{-t} \cos{3 t} + K_{2} t e^{-t} \sin{3 t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - 3 K_{1} t e^{-t} \sin{3 t} - K_{1} t e^{-t} \cos{3 t} + K_{1} e^{-t} \cos{3 t} - K_{2} t e^{-t} \sin{3 t} + 3 K_{2} t e^{-t} \cos{3 t} + K_{2} e^{-t} \sin{3 t} \\ x_p''(t) &= 6 K_{1} t e^{-t} \sin{3 t} - 8 K_{1} t e^{-t} \cos{3 t} - 6 K_{1} e^{-t} \sin{3 t} - 2 K_{1} e^{-t} \cos{3 t} - 8 K_{2} t e^{-t} \sin{3 t} - 6 K_{2} t e^{-t} \cos{3 t} - 2 K_{2} e^{-t} \sin{3 t} + 6 K_{2} e^{-t} \cos{3 t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + 2x_p' + 10x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 6 K_{2}\,e^{-t} \cos 3t - 6 K_{1}\,e^{-t} \sin 3t $$

This must equal the forcing $f(t) = e^{-t} \cos{3 t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{-t} \cos 3t: &\quad 6 K_{2} = 1 \\ e^{-t} \sin 3t: &\quad - 6 K_{1} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} 6 K_{2} &= 1 \quad (1) \\ - 6 K_{1} &= 0 \quad (2) \end{aligned} $$

$6 K_{2} = 1$ contains one unknown only, so $K_{2} = \frac{1}{6}$.

$- 6 K_{1} = 0$ contains one unknown only, so $K_{1} = 0$.

Hence $K_{1} = 0$, $K_{2} = \frac{1}{6}$.

Therefore

$$ x_p(t) = \frac{t e^{-t} \sin{3 t}}{6} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-t} \cos{3 t} + c_{2} e^{-t} \sin{3 t} + \frac{t e^{-t} \sin{3 t}}{6} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 3 c_{1} e^{-t} \sin{3 t} - c_{1} e^{-t} \cos{3 t} - c_{2} e^{-t} \sin{3 t} + 3 c_{2} e^{-t} \cos{3 t} - \frac{t e^{-t} \sin{3 t}}{6} + \frac{t e^{-t} \cos{3 t}}{2} + \frac{e^{-t} \sin{3 t}}{6} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} = 9 \\ x'(0) &= - c_{1} + 3 c_{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} &= 9 \quad (1) \\ - c_{1} + 3 c_{2} &= 0 \quad (2) \end{aligned} $$

$c_{1} = 9$ contains one unknown only, so $c_{1} = 9$.

Substitute in $- c_{1} + 3 c_{2} = 0$: $3 c_{2} - 9 = 0$.

$3 c_{2} - 9 = 0$ contains one unknown only, so $c_{2} = 3$.

Hence $c_{1} = 9$, $c_{2} = 3$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{t e^{-t} \sin{3 t}}{6} + 3 e^{-t} \sin{3 t} + 9 e^{-t} \cos{3 t}} $$

### (x) $\ddot{x} + 6\dot{x} + 10x = e^{-3 t} \cos{t}$, with $x(0) = 10$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + 6\dot{x} + 10x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + 6 k + 10 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (6)^2 - 4(1)(10) = -4$.

Factorising, $P(k) = \left(k + 3 - i\right) \left(k + 3 + i\right)$, so the roots are

$$ k = -3 - i, \qquad k = -3 + i $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-3 t} \cos{t}$, $e^{-3 t} \sin{t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-3 t} \cos{t} + c_{2} e^{-3 t} \sin{t} $$

The forcing $e^{-3 t} \cos{t}$ is a sinusoidal term times an exponential: it is the real or imaginary part of $e^{(-3 + i)t}$, so we test $s = -3 + i$ in the characteristic polynomial: $P(-3 + i) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t e^{-3 t} \cos{t} + K_{2} t e^{-3 t} \sin{t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} t e^{-3 t} \sin{t} - 3 K_{1} t e^{-3 t} \cos{t} + K_{1} e^{-3 t} \cos{t} - 3 K_{2} t e^{-3 t} \sin{t} + K_{2} t e^{-3 t} \cos{t} + K_{2} e^{-3 t} \sin{t} \\ x_p''(t) &= 6 K_{1} t e^{-3 t} \sin{t} + 8 K_{1} t e^{-3 t} \cos{t} - 2 K_{1} e^{-3 t} \sin{t} - 6 K_{1} e^{-3 t} \cos{t} + 8 K_{2} t e^{-3 t} \sin{t} - 6 K_{2} t e^{-3 t} \cos{t} - 6 K_{2} e^{-3 t} \sin{t} + 2 K_{2} e^{-3 t} \cos{t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + 6x_p' + 10x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 2 K_{2}\,e^{-3 t} \cos t - 2 K_{1}\,e^{-3 t} \sin t $$

This must equal the forcing $f(t) = e^{-3 t} \cos{t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{-3 t} \cos t: &\quad 2 K_{2} = 1 \\ e^{-3 t} \sin t: &\quad - 2 K_{1} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} 2 K_{2} &= 1 \quad (1) \\ - 2 K_{1} &= 0 \quad (2) \end{aligned} $$

$2 K_{2} = 1$ contains one unknown only, so $K_{2} = \frac{1}{2}$.

$- 2 K_{1} = 0$ contains one unknown only, so $K_{1} = 0$.

Hence $K_{1} = 0$, $K_{2} = \frac{1}{2}$.

Therefore

$$ x_p(t) = \frac{t e^{-3 t} \sin{t}}{2} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-3 t} \cos{t} + c_{2} e^{-3 t} \sin{t} + \frac{t e^{-3 t} \sin{t}}{2} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - c_{1} e^{-3 t} \sin{t} - 3 c_{1} e^{-3 t} \cos{t} - 3 c_{2} e^{-3 t} \sin{t} + c_{2} e^{-3 t} \cos{t} - \frac{3 t e^{-3 t} \sin{t}}{2} + \frac{t e^{-3 t} \cos{t}}{2} + \frac{e^{-3 t} \sin{t}}{2} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} = 10 \\ x'(0) &= - 3 c_{1} + c_{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} &= 10 \quad (1) \\ - 3 c_{1} + c_{2} &= 0 \quad (2) \end{aligned} $$

$c_{1} = 10$ contains one unknown only, so $c_{1} = 10$.

Substitute in $- 3 c_{1} + c_{2} = 0$: $c_{2} - 30 = 0$.

$c_{2} - 30 = 0$ contains one unknown only, so $c_{2} = 30$.

Hence $c_{1} = 10$, $c_{2} = 30$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{t e^{-3 t} \sin{t}}{2} + 30 e^{-3 t} \sin{t} + 10 e^{-3 t} \cos{t}} $$

### (xi) $\ddot{x} + 4\dot{x} + 4x = e^{2 t}$, with $x(0) = 11$, $\dot x(0) = 0$

The homogeneous equation $\ddot{x} + 4\dot{x} + 4x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + 4 k + 4 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (4)^2 - 4(1)(4) = 0$.

Factorising, $P(k) = \left(k + 2\right)^{2}$, so the roots are

$$ k = -2 \ \text{(multiplicity 2)} $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-2 t}$, $t e^{-2 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-2 t} + c_{2} t e^{-2 t} $$

The forcing $e^{2 t}$ is an exponential with exponent $s = 2$; we test it in the characteristic polynomial: $P(2) = 16$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} e^{2 t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= 2 K_{1} e^{2 t} \\ x_p''(t) &= 4 K_{1} e^{2 t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + 4x_p' + 4x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 16 K_{1}\,e^{2 t} $$

This must equal the forcing $f(t) = e^{2 t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{2 t}: &\quad 16 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} 16 K_{1} &= 1 \quad (1) \end{aligned} $$

$16 K_{1} = 1$ contains one unknown only, so $K_{1} = \frac{1}{16}$.

Hence $K_{1} = \frac{1}{16}$.

Therefore

$$ x_p(t) = \frac{e^{2 t}}{16} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-2 t} + c_{2} t e^{-2 t} + \frac{e^{2 t}}{16} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 2 c_{1} e^{-2 t} - 2 c_{2} t e^{-2 t} + c_{2} e^{-2 t} + \frac{e^{2 t}}{8} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + \frac{1}{16} = 11 \\ x'(0) &= - 2 c_{1} + c_{2} + \frac{1}{8} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + \frac{1}{16} &= 11 \quad (1) \\ - 2 c_{1} + c_{2} + \frac{1}{8} &= 0 \quad (2) \end{aligned} $$

$c_{1} + \frac{1}{16} = 11$ contains one unknown only, so $c_{1} = \frac{175}{16}$.

Substitute in $- 2 c_{1} + c_{2} + \frac{1}{8} = 0$: $c_{2} - \frac{87}{4} = 0$.

$c_{2} - \frac{87}{4} = 0$ contains one unknown only, so $c_{2} = \frac{87}{4}$.

Hence $c_{1} = \frac{175}{16}$, $c_{2} = \frac{87}{4}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{87 t e^{-2 t}}{4} + \frac{e^{2 t}}{16} + \frac{175 e^{-2 t}}{16}} $$

## Phase 4: Interpretation, long-time behaviour and checks

Summary of the eleven solutions of the IVPs (item $(n)$ has $x(0) = n$, $\dot x(0) = 0$):

| Item | Solution $x(t)$ |
| :--- | :--- |
| (i) | $- \frac{t^{2}}{4} + \frac{9 e^{2 t}}{16} - \frac{1}{8} + \frac{9 e^{-2 t}}{16}$ |
| (ii) | $- \frac{t^{3}}{12} - \frac{t^{2}}{16} - \frac{t}{32} + \frac{e^{4 t}}{128} + \frac{255}{128}$ |
| (iii) | $\frac{5 e^{t}}{2} - \frac{3 e^{-t}}{2} + 2 e^{-2 t}$ |
| (iv) | $\frac{t e^{t}}{3} + \frac{23 e^{t}}{9} + \frac{13 e^{-2 t}}{9}$ |
| (v) | $\frac{t^{2} e^{-t}}{2} + 5 t e^{-t} + 5 e^{-t}$ |
| (vi) | $6\cos\omega t + \dfrac{\sin\alpha t - (\alpha/\omega)\sin\omega t}{\omega^2 - \alpha^2}$ |
| (vii) | $7 \cos{\omega t} - \frac{t \cos{\omega t}}{2 \omega} + \frac{\sin{\omega t}}{2 \omega^{2}}$ |
| (viii) | $\frac{8 e^{-t} \sin{3 t}}{3} + \frac{71 e^{-t} \cos{3 t}}{9} + \frac{e^{-t}}{9}$ |
| (ix) | $\frac{t e^{-t} \sin{3 t}}{6} + 3 e^{-t} \sin{3 t} + 9 e^{-t} \cos{3 t}$ |
| (x) | $\frac{t e^{-3 t} \sin{t}}{2} + 30 e^{-3 t} \sin{t} + 10 e^{-3 t} \cos{t}$ |
| (xi) | $\frac{87 t e^{-2 t}}{4} + \frac{e^{2 t}}{16} + \frac{175 e^{-2 t}}{16}$ |

#### Behaviour as $t \to \infty$

- (i): all terms of the complementary function except the growing one are small: $x \sim \tfrac{9}{16}e^{2t}$, unbounded.
- (ii): the term $\tfrac{1}{128}e^{4t}$ is tiny at first but eventually dominates the cubic polynomial: unbounded.
- (iii): $x \sim \tfrac52 e^{t}$ (the forcing $3e^{-t}$ and the mode $e^{-2t}$ decay): unbounded.
- (iv): resonance with the root $k = 1$: $x \sim (\tfrac{t}{3} + \tfrac{23}{9})e^{t}$, faster than a pure exponential.
- (v): every term carries $e^{-t}$: $x \to 0$, although the resonant term $\tfrac12t^2e^{-t}$ first grows (critical damping, resonant forcing).
- (vi): bounded for all $t$ (a sum of two sinusoids, periodic exactly when $\alpha/\omega$ is rational); no decay; beat-like modulation appears when $\alpha \approx \omega$.
- (vii): resonance: the amplitude of $-\dfrac{t\cos\omega t}{2\omega}$ grows linearly without bound.
- (viii): all terms decay like $e^{-t}$: $x \to 0$; the non-oscillatory forced part $\tfrac19e^{-t}$ is not resonant.
- (ix): resonance with the damped oscillation: the envelope $\tfrac{t}{6}e^{-t}$ peaks at $t = 1$ (value $\tfrac{1}{6e} \approx 0.061$) and then decays; $x \to 0$.
- (x): resonance with $e^{-3t}\cos t$: the envelope $\tfrac{t}{2}e^{-3t}$ peaks at $t = \tfrac13$ and decays; $x \to 0$.
- (xi): $x \sim \tfrac1{16}e^{2t}$: the forced exponential beats the decaying modes $e^{-2t}$, $te^{-2t}$: unbounded.

#### Checks

- Every solution was substituted back into its equation and into both initial conditions symbolically (script `scripts/verify_topic3_topic4.py`): the residual $L[x] - f$ is identically zero and $x(0) = n$, $\dot x(0) = 0$.
- Dimensions: if $x$ is a length and $t$ a time, every term of $\ddot x + b\dot x + cx = f$ has units of length/time$^2$, so $b$ has units s$^{-1}$, $c$ and $\omega^2$ units s$^{-2}$ and $f$ units m/s$^2$ if the equation is read dimensionally. The sheet itself uses dimensionless variables (forcings such as $t^2$ or $e^{-t}$ carry no units), so these units only serve to check the structure of the formulas. In (vi) the combination $\alpha/\omega$ is dimensionless and $1/(\omega^2 - \alpha^2)$ has units s$^2$, so $x$ comes out in metres.
- Resonance diagnostic: the items with a factor $t$ in the particular integral are exactly those where the exponent of $f$ is a root of $P$ (listed in Phase 2).
- Beats versus resonance: as $\alpha \to \omega$, (vi) tends to (vii) (L'Hopital check above); the beat amplitude $\propto 1/(\omega^2 - \alpha^2)$ blows up exactly where the resonant solution replaces it.
