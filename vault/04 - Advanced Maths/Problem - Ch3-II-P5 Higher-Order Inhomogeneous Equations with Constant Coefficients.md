---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 5"
dificultad: media
id: "e5"
pill: "Third and Fourth Order • Repeated Roots • Undetermined Coefficients"
tags:
  - problema-resuelto
  - orden-superior
  - coeficientes-indeterminados
  - raices-repetidas
---

# Problem 3.II.5: Higher-Order Inhomogeneous Equations with Constant Coefficients

> Official exercise 5 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

Working by analogy with the second order case, find the general solution of the following inhomogeneous higher-order linear equations with constant coefficients:

- (i) $\dfrac{d^3x}{dt^3} - 6\dfrac{d^2x}{dt^2} + 11\dfrac{dx}{dt} - 6x = e^{-t}$,
- (ii) $y''' - 3y' + 2 = \sin x$,
- (iii) $\dfrac{d^4x}{dt^4} - 4\dfrac{d^3x}{dt^3} + 8\dfrac{d^2x}{dt^2} - 8\dfrac{dx}{dt} + 4x = \sin t$.

## Phase 1: Setup, classification and a remark on the statement

All three are linear, constant-coefficient, inhomogeneous equations of order $3$, $3$ and $4$. By the higher-order theory (Robinson Sec. 16.1, Topic 3 Sec. 3 box), the general solution of $a_nx^{(n)} + \dots + a_0x = f$ is $x = x_h + x_p$, where $x_h$ contains $n$ arbitrary constants (the solution space of the homogeneous equation has dimension $n$) and the method of undetermined coefficients gives $x_p$ exactly as for $n = 2$. Hypotheses: coefficients constant, $f$ continuous.

> [!warning] Remark on the statement of (ii)
> The sheet prints $y''' - 3y' + 2 = \sin x$. Read literally this is the linear equation $y''' - 3y' = \sin x - 2$ (the constant $2$ moves to the right-hand side), which is perfectly solvable. The other two items and the form $L[y] = \dots$ suggest that the term $2y$ may have been intended, but that is only a guess from the pattern of the sheet. We therefore solve **both readings in full**: $y''' - 3y' + 2y = \sin x$ (the guessed one) and the literal $y''' - 3y' = \sin x - 2$, each with its own general solution, so that the answer is complete whichever the author meant.

## Phase 2: Method

Characteristic polynomial $P(k) = a_nk^n + \dots + a_0$. A root $k$ of multiplicity $m$ gives $t^je^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ of multiplicity $m$ gives $t^je^{\rho t}\cos\omega t$ and $t^je^{\rho t}\sin\omega t$ for $j = 0, \dots, m - 1$ (Topic 3, Sec. 3 box, Robinson Sec. 16.1). The particular integral uses the guess table of Topic 3, Sec. 5, with the factor $t^{m_s}$ when the exponent $s$ of the forcing is a root of $P$ of multiplicity $m_s$. The derivatives needed are now up to order $n$.

## Phase 3: Derivation

### (i) $x''' - 6x'' + 11x' - 6x = e^{-t}$

The homogeneous equation $\dddot{x} - 6\ddot{x} + 11\dot{x} - 6x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{3} - 6 k^{2} + 11 k - 6 = 0 $$

Factorising, $P(k) = \left(k - 3\right) \left(k - 2\right) \left(k - 1\right)$, so the roots are

$$ k = 1, \qquad k = 2, \qquad k = 3 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{t}$, $e^{2 t}$, $e^{3 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{t} + c_{2} e^{2 t} + c_{3} e^{3 t} $$

The forcing $e^{-t}$ is an exponential with exponent $s = -1$; we test it in the characteristic polynomial: $P(-1) = -24$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} e^{-t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} e^{-t} \\ x_p''(t) &= K_{1} e^{-t} \\ x_p^{(3)}(t) &= - K_{1} e^{-t} \end{aligned} $$

Substitute into $L[x_p] = x_p^{(3)} - 6x_p'' + 11x_p' - 6x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = - 24 K_{1}\,e^{-t} $$

This must equal the forcing $f(t) = e^{-t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} e^{-t}: &\quad - 24 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 24 K_{1} &= 1 \quad (1) \end{aligned} $$

$- 24 K_{1} = 1$ contains one unknown only, so $K_{1} = - \frac{1}{24}$.

Hence $K_{1} = - \frac{1}{24}$.

Therefore

$$ x_p(t) = - \frac{e^{-t}}{24} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{t} + c_{2} e^{2 t} + c_{3} e^{3 t} - \frac{e^{-t}}{24} $$

### (ii) $y''' - 3y' + 2y = \sin x$ (independent variable $x$)

The homogeneous equation $y^{(3)} - 3y' + 2y = 0$ has constant coefficients, so we try $y = e^{kx}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kx} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{3} - 3 k + 2 = 0 $$

Factorising, $P(k) = \left(k - 1\right)^{2} \left(k + 2\right)$, so the roots are

$$ k = -2, \qquad k = 1 \ \text{(multiplicity 2)} $$

A real root $k$ of multiplicity $m$ gives $x^j e^{kx}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $x^j e^{\rho x}\cos\omega x$ and $x^j e^{\rho x}\sin\omega x$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-2 x}$, $e^{x}$, $x e^{x}$, so the complementary function is

$$ y_h(x) = c_{1} e^{-2 x} + c_{2} e^{x} + c_{3} x e^{x} $$

The forcing $\sin{x}$ is a sinusoidal term: it is the real or imaginary part of $e^{(i)x}$, so we test $s = i$ in the characteristic polynomial: $P(i) = 2 - 4 i$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ y_p(x) = K_{1} \cos{x} + K_{2} \sin{x} $$

Differentiate term by term (product rule on $x^j e^{\sigma x}$, chain rule on $\cos\omega x$ and $\sin\omega x$):

$$ \begin{aligned} y_p'(x) &= - K_{1} \sin{x} + K_{2} \cos{x} \\ y_p''(x) &= - K_{1} \cos{x} - K_{2} \sin{x} \\ y_p^{(3)}(x) &= K_{1} \sin{x} - K_{2} \cos{x} \end{aligned} $$

Substitute into $L[y_p] = y_p^{(3)} - 3y_p' + 2y_p$ and collect the terms that multiply the same function:

$$ L[y_p] = \left(2 K_{1} - 4 K_{2}\right)\,\cos x + \left(4 K_{1} + 2 K_{2}\right)\,\sin x $$

This must equal the forcing $f(x) = \sin{x}$ for every $x$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} \cos x: &\quad 2 K_{1} - 4 K_{2} = 0 \\ \sin x: &\quad 4 K_{1} + 2 K_{2} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} 2 K_{1} - 4 K_{2} &= 0 \quad (1) \\ 4 K_{1} + 2 K_{2} &= 1 \quad (2) \end{aligned} $$

Solve $2 K_{1} - 4 K_{2} = 0$ for $K_{1}$: $K_{1} = 2 K_{2}$.

Substitute in $4 K_{1} + 2 K_{2} = 1$: $10 K_{2} = 1$.

$10 K_{2} = 1$ contains one unknown only, so $K_{2} = \frac{1}{10}$.

Back-substitution: $K_{1} = 2 K_{2} = \frac{1}{5}$.

Hence $K_{1} = \frac{1}{5}$, $K_{2} = \frac{1}{10}$.

Therefore

$$ y_p(x) = \frac{\sin{x}}{10} + \frac{\cos{x}}{5} $$

The general solution is the complementary function plus the particular integral:

$$ y(x) = y_h(x) + y_p(x) = c_{1} e^{-2 x} + c_{2} e^{x} + c_{3} x e^{x} + \frac{\sin{x}}{10} + \frac{\cos{x}}{5} $$

#### Literal reading of the sheet: $y''' - 3y' = \sin x - 2$

The homogeneous equation $y^{(3)} - 3y' = 0$ has constant coefficients, so we try $y = e^{kx}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kx} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{3} - 3 k = 0 $$

Factorising, $P(k) = k \left(k^{2} - 3\right)$, so the roots are

$$ k = - \sqrt{3}, \qquad k = 0, \qquad k = \sqrt{3} $$

A real root $k$ of multiplicity $m$ gives $x^j e^{kx}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $x^j e^{\rho x}\cos\omega x$ and $x^j e^{\rho x}\sin\omega x$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-\sqrt{3} x}$, $1$, $e^{\sqrt{3} x}$, so the complementary function is

$$ y_h(x) = c_{1} e^{-\sqrt{3} x} + c_{2} + c_{3} e^{\sqrt{3} x} $$

The forcing is a sum of terms. By linearity (Robinson Eq. 14.7) a particular integral is the sum of particular integrals of the separate terms, each found in turn.

#### Particular integral for the term $\sin{x}$

The forcing $\sin{x}$ is a sinusoidal term: it is the real or imaginary part of $e^{(i)x}$, so we test $s = i$ in the characteristic polynomial: $P(i) = - 4 i$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ y_p(x) = K_{1} \cos{x} + K_{2} \sin{x} $$

Differentiate term by term (product rule on $x^j e^{\sigma x}$, chain rule on $\cos\omega x$ and $\sin\omega x$):

$$ \begin{aligned} y_p'(x) &= - K_{1} \sin{x} + K_{2} \cos{x} \\ y_p''(x) &= - K_{1} \cos{x} - K_{2} \sin{x} \\ y_p^{(3)}(x) &= K_{1} \sin{x} - K_{2} \cos{x} \end{aligned} $$

Substitute into $L[y_p] = y_p^{(3)} - 3y_p'$ and collect the terms that multiply the same function:

$$ L[y_p] = - 4 K_{2}\,\cos x + 4 K_{1}\,\sin x $$

This must equal the forcing $f(x) = \sin{x}$ for every $x$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} \cos x: &\quad - 4 K_{2} = 0 \\ \sin x: &\quad 4 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 4 K_{2} &= 0 \quad (1) \\ 4 K_{1} &= 1 \quad (2) \end{aligned} $$

$- 4 K_{2} = 0$ contains one unknown only, so $K_{2} = 0$.

$4 K_{1} = 1$ contains one unknown only, so $K_{1} = \frac{1}{4}$.

Hence $K_{1} = \frac{1}{4}$, $K_{2} = 0$.

Therefore

$$ y_p(x) = \frac{\cos{x}}{4} $$

#### Particular integral for the term $-2$

The forcing $-2$ is an exponential with exponent $s = 0$; we test it in the characteristic polynomial: $P(0) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $x^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ y_p(x) = K_{1} x $$

Differentiate term by term (product rule on $x^j e^{\sigma x}$, chain rule on $\cos\omega x$ and $\sin\omega x$):

$$ \begin{aligned} y_p'(x) &= K_{1} \\ y_p''(x) &= 0 \\ y_p^{(3)}(x) &= 0 \end{aligned} $$

Substitute into $L[y_p] = y_p^{(3)} - 3y_p'$ and collect the terms that multiply the same function:

$$ L[y_p] = - 3 K_{1} $$

This must equal the forcing $f(x) = -2$ for every $x$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} 1: &\quad - 3 K_{1} = -2 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 3 K_{1} &= -2 \quad (1) \end{aligned} $$

$- 3 K_{1} = -2$ contains one unknown only, so $K_{1} = \frac{2}{3}$.

Hence $K_{1} = \frac{2}{3}$.

Therefore

$$ y_p(x) = \frac{2 x}{3} $$

Adding the particular integrals,

$$ y_p(x) = \frac{2 x}{3} + \frac{\cos{x}}{4} $$

The general solution is the complementary function plus the particular integral:

$$ y(x) = y_h(x) + y_p(x) = c_{1} e^{-\sqrt{3} x} + c_{2} + c_{3} e^{\sqrt{3} x} + \frac{2 x}{3} + \frac{\cos{x}}{4} $$

### (iii) $x^{(4)} - 4x''' + 8x'' - 8x' + 4x = \sin t$

The homogeneous equation $x^{(4)} - 4\dddot{x} + 8\ddot{x} - 8\dot{x} + 4x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{4} - 4 k^{3} + 8 k^{2} - 8 k + 4 = 0 $$

Factorising, $P(k) = \left(k - 1 - i\right)^{2} \left(k - 1 + i\right)^{2}$, so the roots are

$$ k = 1 - i \ \text{(multiplicity 2)}, \qquad k = 1 + i \ \text{(multiplicity 2)} $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{t} \cos{t}$, $e^{t} \sin{t}$, $t e^{t} \cos{t}$, $t e^{t} \sin{t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{t} \cos{t} + c_{2} e^{t} \sin{t} + c_{3} t e^{t} \cos{t} + c_{4} t e^{t} \sin{t} $$

The forcing $\sin{t}$ is a sinusoidal term: it is the real or imaginary part of $e^{(i)t}$, so we test $s = i$ in the characteristic polynomial: $P(i) = -3 - 4 i$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} \cos{t} + K_{2} \sin{t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} \sin{t} + K_{2} \cos{t} \\ x_p''(t) &= - K_{1} \cos{t} - K_{2} \sin{t} \\ x_p^{(3)}(t) &= K_{1} \sin{t} - K_{2} \cos{t} \\ x_p^{(4)}(t) &= K_{1} \cos{t} + K_{2} \sin{t} \end{aligned} $$

Substitute into $L[x_p] = x_p^{(4)} - 4x_p^{(3)} + 8x_p'' - 8x_p' + 4x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = \left(- 3 K_{1} - 4 K_{2}\right)\,\cos t + \left(4 K_{1} - 3 K_{2}\right)\,\sin t $$

This must equal the forcing $f(t) = \sin{t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} \cos t: &\quad - 3 K_{1} - 4 K_{2} = 0 \\ \sin t: &\quad 4 K_{1} - 3 K_{2} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 3 K_{1} - 4 K_{2} &= 0 \quad (1) \\ 4 K_{1} - 3 K_{2} &= 1 \quad (2) \end{aligned} $$

Solve $- 3 K_{1} - 4 K_{2} = 0$ for $K_{1}$: $K_{1} = - \frac{4 K_{2}}{3}$.

Substitute in $4 K_{1} - 3 K_{2} = 1$: $- \frac{25 K_{2}}{3} = 1$.

$- \frac{25 K_{2}}{3} = 1$ contains one unknown only, so $K_{2} = - \frac{3}{25}$.

Back-substitution: $K_{1} = - \frac{4 K_{2}}{3} = \frac{4}{25}$.

Hence $K_{1} = \frac{4}{25}$, $K_{2} = - \frac{3}{25}$.

Therefore

$$ x_p(t) = - \frac{3 \sin{t}}{25} + \frac{4 \cos{t}}{25} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{t} \cos{t} + c_{2} e^{t} \sin{t} + c_{3} t e^{t} \cos{t} + c_{4} t e^{t} \sin{t} - \frac{3 \sin{t}}{25} + \frac{4 \cos{t}}{25} $$

## Phase 4: Interpretation and checks

| Item | General solution |
| :--- | :--- |
| (i) | $c_{1} e^{t} + c_{2} e^{2 t} + c_{3} e^{3 t} - \frac{e^{-t}}{24}$ |
| (ii), intended | $y(x) = c_{1} e^{-2 x} + c_{2} e^{x} + c_{3} x e^{x} + \frac{\sin{x}}{10} + \frac{\cos{x}}{5}$ |
| (ii), literal reading | $y(x) = c_{1} e^{-\sqrt{3} x} + c_{2} + c_{3} e^{\sqrt{3} x} + \frac{2 x}{3} + \frac{\cos{x}}{4}$ |
| (iii) | $c_{1} e^{t} \cos{t} + c_{2} e^{t} \sin{t} + c_{3} t e^{t} \cos{t} + c_{4} t e^{t} \sin{t} - \frac{3 \sin{t}}{25} + \frac{4 \cos{t}}{25}$ |

- The number of arbitrary constants equals the order ($3$, $3$, $4$), as the dimension of the solution space requires (Robinson Sec. 16.2).
- (i): three distinct real roots $1, 2, 3$, none equal to the exponent $s = -1$ of the forcing, hence no factor $t$.
- (ii): $P(k) = k^3 - 3k + 2 = (k - 1)^2(k + 2)$ has the **double** root $1$, giving $e^x$ and $xe^x$; the forcing exponent is $s = \pm i$, not a root.
- (iii): $P(k) = k^4 - 4k^3 + 8k^2 - 8k + 4 = (k^2 - 2k + 2)^2 = ((k - 1)^2 + 1)^2$ has the **double** complex pair $1 \pm i$, giving $e^t\cos t, e^t\sin t, te^t\cos t, te^t\sin t$; the forcing exponent is $\pm i$, not a root.
- Each particular integral was substituted back into its equation symbolically (script `scripts/verify_topic3_topic4.py`); the residual vanishes identically.
