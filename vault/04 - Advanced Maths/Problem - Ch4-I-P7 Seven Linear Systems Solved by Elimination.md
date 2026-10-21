---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 7"
dificultad: media
id: "e7"
pill: "Elimination Method • Seven IVPs • Undetermined Coefficients"
tags:
  - problema-resuelto
  - metodo-de-eliminacion
  - sistemas-lineales
  - pvi
---

# Problem 4.I.7: Seven Linear Systems Solved by Elimination

> Official exercise 7 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Find the general solutions of the following differential equations by converting them into a single second-order equation. Also find the solution that satisfies the given initial conditions.

- (i) $\dot x = 4x - y,\quad \dot y = 2x + y + t^2$, $\quad x(0) = 0,\ y(0) = 1$;
- (ii) $\dot x = x - 4y + \cos 2t,\quad \dot y = x + y$, $\quad x(0) = 1,\ y(0) = 1$;
- (iii) $\dot x = 2x + 2y,\quad \dot y = 6x + 3y + e^{t}$, $\quad x(0) = 0,\ \dot x(0) = 1$;
- (iv) $\dot x = 5x - 4y + e^{3t},\quad \dot y = x + y$, $\quad x(0) = 1,\ y(0) = -1$;
- (v) $\dot x = 2x + 5y,\quad \dot y = -2x + \cos 3t$, $\quad x(0) = 2,\ y(0) = -1$;
- (vi) $\dot x = x + y + e^{-t},\quad \dot y = 4x - 2y + e^{2t}$, $\quad x(0) = 1,\ y(0) = -1$;
- (vii) $\dot x = 8x + 14y,\quad \dot y = 7x + y$, $\quad x(0) = y(0) = 1$.

## Phase 1: Setup and classification

Each system is linear with constant coefficients, of the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1), homogeneous when $f = g = 0$. In every item $b \neq 0$, so the first equation can be solved for $y$. Hypotheses: coefficients and forcings continuous on $\mathbb R$, so the IVP has a unique solution, which exists on all of $\mathbb R$ (linear system with continuous coefficients; Thm 25.2 gives local existence and uniqueness and the continuation argument of Exercise 4 extends it). Item (iii) gives $x(0)$ and $\dot x(0)$; the value of $y(0)$ then follows from the first equation.

## Phase 2: Method: elimination (Topic 4 Sec. 2.1)

Solve the first equation for $y = (\dot x - ax - f)/b$ (26.2), differentiate, and substitute in the second equation. The result is one second-order equation for $x$ (26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Its coefficients are the trace and determinant of the matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, so its characteristic polynomial is the one of the eigenvalue method. It is solved by the methods of Topic 3 (complementary function plus undetermined coefficients). Then $y$ is recovered from (26.2) and the constants from the data.

## Phase 3: Derivation of the seven solutions

### (i) $\dot x = 4x - y,\quad \dot y = 2x + y + t^2$, $\ x(0) = 0,\ y(0) = 1$

The system is linear with constant coefficients, in the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with

$$ a = 4,\quad b = -1,\quad c = 2,\quad d = 1,\quad f(t) = 0,\quad g(t) = t^{2} $$

#### Elimination of $y$

Since $b = -1 \neq 0$, the first equation can be solved for $y$ (Eq. 26.2):

$$ y = \frac{\dot x - ax - f}{b} = \frac{1}{-1}\left(\dot x - (4)x - (0)\right) $$

Differentiate with respect to $t$ (everything is differentiable):

$$ \dot y = \frac{\ddot x - a\dot x - \dot f}{b} = \frac{1}{-1}\left(\ddot x - (4)\dot x - (0)\right) $$

Substitute both expressions into the second equation, $\dot y = cx + dy + g$, and multiply by $b$:

$$ \ddot x - a\dot x - \dot f = bc\,x + d\,(\dot x - ax - f) + bg $$

Collect the terms in $\ddot x$, $\dot x$ and $x$ (Eq. 26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Numerically, $a + d = 5$, $ad - bc = (4)(1) - (-1)(2) = 6$ and $F(t) := \dot f + bg - df = (0) + (-1)(t^{2}) - (1)(0) = - t^{2}$, so

$$ \ddot{x} - 5\dot{x} + 6x = - t^{2} $$

Initial data. The condition on $y$ is converted into one on $\dot x$ with the first equation at $t = 0$: $\dot x(0) = a\,x(0) + b\,y(0) + f(0) = (4)(0) + (-1)(1) + (0) = -1$.

The homogeneous equation $\ddot{x} - 5\dot{x} + 6x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 5 k + 6 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (-5)^2 - 4(1)(6) = 1$.

Factorising, $P(k) = \left(k - 3\right) \left(k - 2\right)$, so the roots are

$$ k = 2, \qquad k = 3 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{2 t}$, $e^{3 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{2 t} + c_{2} e^{3 t} $$

The forcing $- t^{2}$ is a polynomial of degree 2; a polynomial is $e^{0t}$ times a polynomial, so the exponent to test is $s = 0$: $P(0) = 6$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} + K_{2} t + K_{3} t^{2} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= K_{2} + 2 K_{3} t \\ x_p''(t) &= 2 K_{3} \end{aligned} $$

Substitute into $L[x_p] = x_p'' - 5x_p' + 6x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 6 K_{3}\,t^{2} + \left(6 K_{2} - 10 K_{3}\right)\,t + \left(6 K_{1} - 5 K_{2} + 2 K_{3}\right) $$

This must equal the forcing $F(t) = - t^{2}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $F$:

$$ \begin{aligned} t^{2}: &\quad 6 K_{3} = -1 \\ t: &\quad 6 K_{2} - 10 K_{3} = 0 \\ 1: &\quad 6 K_{1} - 5 K_{2} + 2 K_{3} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} 6 K_{3} &= -1 \quad (1) \\ 6 K_{2} - 10 K_{3} &= 0 \quad (2) \\ 6 K_{1} - 5 K_{2} + 2 K_{3} &= 0 \quad (3) \end{aligned} $$

$6 K_{3} = -1$ contains one unknown only, so $K_{3} = - \frac{1}{6}$.

Substitute in $6 K_{2} - 10 K_{3} = 0$: $6 K_{2} + \frac{5}{3} = 0$.

Substitute in $6 K_{1} - 5 K_{2} + 2 K_{3} = 0$: $6 K_{1} - 5 K_{2} - \frac{1}{3} = 0$.

$6 K_{2} + \frac{5}{3} = 0$ contains one unknown only, so $K_{2} = - \frac{5}{18}$.

Substitute in $6 K_{1} - 5 K_{2} - \frac{1}{3} = 0$: $6 K_{1} + \frac{19}{18} = 0$.

$6 K_{1} + \frac{19}{18} = 0$ contains one unknown only, so $K_{1} = - \frac{19}{108}$.

Hence $K_{1} = - \frac{19}{108}$, $K_{2} = - \frac{5}{18}$, $K_{3} = - \frac{1}{6}$.

Therefore

$$ x_p(t) = - \frac{t^{2}}{6} - \frac{5 t}{18} - \frac{19}{108} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{2 t} + c_{2} e^{3 t} - \frac{t^{2}}{6} - \frac{5 t}{18} - \frac{19}{108} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= 2 c_{1} e^{2 t} + 3 c_{2} e^{3 t} - \frac{t}{3} - \frac{5}{18} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} - \frac{19}{108} = 0 \\ x'(0) &= 2 c_{1} + 3 c_{2} - \frac{5}{18} = -1 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} - \frac{19}{108} &= 0 \quad (1) \\ 2 c_{1} + 3 c_{2} - \frac{5}{18} &= -1 \quad (2) \end{aligned} $$

Solve $c_{1} + c_{2} - \frac{19}{108} = 0$ for $c_{1}$: $c_{1} = \frac{19}{108} - c_{2}$.

Substitute in $2 c_{1} + 3 c_{2} - \frac{5}{18} = -1$: $c_{2} + \frac{2}{27} = -1$.

$c_{2} + \frac{2}{27} = -1$ contains one unknown only, so $c_{2} = - \frac{29}{27}$.

Back-substitution: $c_{1} = \frac{19}{108} - c_{2} = \frac{5}{4}$.

Hence $c_{1} = \frac{5}{4}$, $c_{2} = - \frac{29}{27}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = - \frac{t^{2}}{6} - \frac{5 t}{18} - \frac{29 e^{3 t}}{27} + \frac{5 e^{2 t}}{4} - \frac{19}{108}} $$

#### Recovering $y$

From Eq. 26.2, $y = (\dot x - ax - f)/b$. With the solution found,

$$ \dot x(t) = - \frac{t}{3} - \frac{29 e^{3 t}}{9} + \frac{5 e^{2 t}}{2} - \frac{5}{18} $$

$$ y(t) = \frac{1}{-1}\left(\dot x - (4)x - (0)\right) = - \frac{2 t^{2}}{3} - \frac{7 t}{9} - \frac{29 e^{3 t}}{27} + \frac{5 e^{2 t}}{2} - \frac{23}{54} $$

#### Check in the original system

$$ \begin{aligned} \dot x &= - \frac{t}{3} - \frac{29 e^{3 t}}{9} + \frac{5 e^{2 t}}{2} - \frac{5}{18} \\ ax + by + f &= - \frac{t}{3} - \frac{29 e^{3 t}}{9} + \frac{5 e^{2 t}}{2} - \frac{5}{18} \\[4pt] \dot y &= - \frac{4 t}{3} - \frac{29 e^{3 t}}{9} + 5 e^{2 t} - \frac{7}{9} \\ cx + dy + g &= - \frac{4 t}{3} - \frac{29 e^{3 t}}{9} + 5 e^{2 t} - \frac{7}{9} \end{aligned} $$

Both pairs of expressions coincide, and $x(0) = 0$, $y(0) = 1$ reproduce the initial data.

### (ii) $\dot x = x - 4y + \cos 2t,\quad \dot y = x + y$, $\ x(0) = 1,\ y(0) = 1$

The system is linear with constant coefficients, in the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with

$$ a = 1,\quad b = -4,\quad c = 1,\quad d = 1,\quad f(t) = \cos{2 t},\quad g(t) = 0 $$

#### Elimination of $y$

Since $b = -4 \neq 0$, the first equation can be solved for $y$ (Eq. 26.2):

$$ y = \frac{\dot x - ax - f}{b} = \frac{1}{-4}\left(\dot x - (1)x - (\cos{2 t})\right) $$

Differentiate with respect to $t$ (everything is differentiable):

$$ \dot y = \frac{\ddot x - a\dot x - \dot f}{b} = \frac{1}{-4}\left(\ddot x - (1)\dot x - (- 2 \sin{2 t})\right) $$

Substitute both expressions into the second equation, $\dot y = cx + dy + g$, and multiply by $b$:

$$ \ddot x - a\dot x - \dot f = bc\,x + d\,(\dot x - ax - f) + bg $$

Collect the terms in $\ddot x$, $\dot x$ and $x$ (Eq. 26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Numerically, $a + d = 2$, $ad - bc = (1)(1) - (-4)(1) = 5$ and $F(t) := \dot f + bg - df = (- 2 \sin{2 t}) + (-4)(0) - (1)(\cos{2 t}) = - 2 \sin{2 t} - \cos{2 t}$, so

$$ \ddot{x} - 2\dot{x} + 5x = - 2 \sin{2 t} - \cos{2 t} $$

Initial data. The condition on $y$ is converted into one on $\dot x$ with the first equation at $t = 0$: $\dot x(0) = a\,x(0) + b\,y(0) + f(0) = (1)(1) + (-4)(1) + (1) = -2$.

The homogeneous equation $\ddot{x} - 2\dot{x} + 5x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 2 k + 5 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (-2)^2 - 4(1)(5) = -16$.

Factorising, $P(k) = \left(k - 1 - 2 i\right) \left(k - 1 + 2 i\right)$, so the roots are

$$ k = 1 - 2 i, \qquad k = 1 + 2 i $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{t} \cos{2 t}$, $e^{t} \sin{2 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{t} \cos{2 t} + c_{2} e^{t} \sin{2 t} $$

The forcing $- 2 \sin{2 t} - \cos{2 t}$ is a sinusoidal term: it is the real or imaginary part of $e^{(2 i)t}$, so we test $s = 2 i$ in the characteristic polynomial: $P(2 i) = 1 - 4 i$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} \cos{2 t} + K_{2} \sin{2 t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - 2 K_{1} \sin{2 t} + 2 K_{2} \cos{2 t} \\ x_p''(t) &= - 4 K_{1} \cos{2 t} - 4 K_{2} \sin{2 t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' - 2x_p' + 5x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = \left(K_{1} - 4 K_{2}\right)\,\cos 2t + \left(4 K_{1} + K_{2}\right)\,\sin 2t $$

This must equal the forcing $F(t) = - 2 \sin{2 t} - \cos{2 t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $F$:

$$ \begin{aligned} \cos 2t: &\quad K_{1} - 4 K_{2} = -1 \\ \sin 2t: &\quad 4 K_{1} + K_{2} = -2 \end{aligned} $$

The linear system is

$$ \begin{aligned} K_{1} - 4 K_{2} &= -1 \quad (1) \\ 4 K_{1} + K_{2} &= -2 \quad (2) \end{aligned} $$

Solve $K_{1} - 4 K_{2} = -1$ for $K_{1}$: $K_{1} = 4 K_{2} - 1$.

Substitute in $4 K_{1} + K_{2} = -2$: $17 K_{2} - 4 = -2$.

$17 K_{2} - 4 = -2$ contains one unknown only, so $K_{2} = \frac{2}{17}$.

Back-substitution: $K_{1} = 4 K_{2} - 1 = - \frac{9}{17}$.

Hence $K_{1} = - \frac{9}{17}$, $K_{2} = \frac{2}{17}$.

Therefore

$$ x_p(t) = \frac{2 \sin{2 t}}{17} - \frac{9 \cos{2 t}}{17} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{t} \cos{2 t} + c_{2} e^{t} \sin{2 t} + \frac{2 \sin{2 t}}{17} - \frac{9 \cos{2 t}}{17} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 2 c_{1} e^{t} \sin{2 t} + c_{1} e^{t} \cos{2 t} + c_{2} e^{t} \sin{2 t} + 2 c_{2} e^{t} \cos{2 t} + \frac{18 \sin{2 t}}{17} + \frac{4 \cos{2 t}}{17} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} - \frac{9}{17} = 1 \\ x'(0) &= c_{1} + 2 c_{2} + \frac{4}{17} = -2 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} - \frac{9}{17} &= 1 \quad (1) \\ c_{1} + 2 c_{2} + \frac{4}{17} &= -2 \quad (2) \end{aligned} $$

$c_{1} - \frac{9}{17} = 1$ contains one unknown only, so $c_{1} = \frac{26}{17}$.

Substitute in $c_{1} + 2 c_{2} + \frac{4}{17} = -2$: $2 c_{2} + \frac{30}{17} = -2$.

$2 c_{2} + \frac{30}{17} = -2$ contains one unknown only, so $c_{2} = - \frac{32}{17}$.

Hence $c_{1} = \frac{26}{17}$, $c_{2} = - \frac{32}{17}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = - \frac{32 e^{t} \sin{2 t}}{17} + \frac{26 e^{t} \cos{2 t}}{17} + \frac{2 \sin{2 t}}{17} - \frac{9 \cos{2 t}}{17}} $$

#### Recovering $y$

From Eq. 26.2, $y = (\dot x - ax - f)/b$. With the solution found,

$$ \dot x(t) = - \frac{84 e^{t} \sin{2 t}}{17} - \frac{38 e^{t} \cos{2 t}}{17} + \frac{18 \sin{2 t}}{17} + \frac{4 \cos{2 t}}{17} $$

$$ y(t) = \frac{1}{-4}\left(\dot x - (1)x - (\cos{2 t})\right) = \frac{13 e^{t} \sin{2 t}}{17} + \frac{16 e^{t} \cos{2 t}}{17} - \frac{4 \sin{2 t}}{17} + \frac{\cos{2 t}}{17} $$

#### Check in the original system

$$ \begin{aligned} \dot x &= - \frac{84 e^{t} \sin{2 t}}{17} - \frac{38 e^{t} \cos{2 t}}{17} + \frac{18 \sin{2 t}}{17} + \frac{4 \cos{2 t}}{17} \\ ax + by + f &= - \frac{84 e^{t} \sin{2 t}}{17} - \frac{38 e^{t} \cos{2 t}}{17} + \frac{18 \sin{2 t}}{17} + \frac{4 \cos{2 t}}{17} \\[4pt] \dot y &= - \frac{19 e^{t} \sin{2 t}}{17} + \frac{42 e^{t} \cos{2 t}}{17} - \frac{2 \sin{2 t}}{17} - \frac{8 \cos{2 t}}{17} \\ cx + dy + g &= - \frac{19 e^{t} \sin{2 t}}{17} + \frac{42 e^{t} \cos{2 t}}{17} - \frac{2 \sin{2 t}}{17} - \frac{8 \cos{2 t}}{17} \end{aligned} $$

Both pairs of expressions coincide, and $x(0) = 1$, $y(0) = 1$ reproduce the initial data.

### (iii) $\dot x = 2x + 2y,\quad \dot y = 6x + 3y + e^{t}$, $\ x(0) = 0,\ \dot x(0) = 1$

The system is linear with constant coefficients, in the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with

$$ a = 2,\quad b = 2,\quad c = 6,\quad d = 3,\quad f(t) = 0,\quad g(t) = e^{t} $$

#### Elimination of $y$

Since $b = 2 \neq 0$, the first equation can be solved for $y$ (Eq. 26.2):

$$ y = \frac{\dot x - ax - f}{b} = \frac{1}{2}\left(\dot x - (2)x - (0)\right) $$

Differentiate with respect to $t$ (everything is differentiable):

$$ \dot y = \frac{\ddot x - a\dot x - \dot f}{b} = \frac{1}{2}\left(\ddot x - (2)\dot x - (0)\right) $$

Substitute both expressions into the second equation, $\dot y = cx + dy + g$, and multiply by $b$:

$$ \ddot x - a\dot x - \dot f = bc\,x + d\,(\dot x - ax - f) + bg $$

Collect the terms in $\ddot x$, $\dot x$ and $x$ (Eq. 26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Numerically, $a + d = 5$, $ad - bc = (2)(3) - (2)(6) = -6$ and $F(t) := \dot f + bg - df = (0) + (2)(e^{t}) - (3)(0) = 2 e^{t}$, so

$$ \ddot{x} - 5\dot{x} - 6x = 2 e^{t} $$

Initial data. Here $x(0)$ and $\dot x(0)$ are given; the value of $y(0)$ follows from the first equation at $t = 0$: $y(0) = \dfrac{\dot x(0) - a\,x(0) - f(0)}{b} = \dfrac{1 - (2)(0) - (0)}{2} = \frac{1}{2}$.

The homogeneous equation $\ddot{x} - 5\dot{x} - 6x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 5 k - 6 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (-5)^2 - 4(1)(-6) = 49$.

Factorising, $P(k) = \left(k - 6\right) \left(k + 1\right)$, so the roots are

$$ k = -1, \qquad k = 6 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-t}$, $e^{6 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-t} + c_{2} e^{6 t} $$

The forcing $2 e^{t}$ is an exponential with exponent $s = 1$; we test it in the characteristic polynomial: $P(1) = -10$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} e^{t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= K_{1} e^{t} \\ x_p''(t) &= K_{1} e^{t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' - 5x_p' - 6x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = - 10 K_{1}\,e^{t} $$

This must equal the forcing $F(t) = 2 e^{t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $F$:

$$ \begin{aligned} e^{t}: &\quad - 10 K_{1} = 2 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 10 K_{1} &= 2 \quad (1) \end{aligned} $$

$- 10 K_{1} = 2$ contains one unknown only, so $K_{1} = - \frac{1}{5}$.

Hence $K_{1} = - \frac{1}{5}$.

Therefore

$$ x_p(t) = - \frac{e^{t}}{5} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-t} + c_{2} e^{6 t} - \frac{e^{t}}{5} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - c_{1} e^{-t} + 6 c_{2} e^{6 t} - \frac{e^{t}}{5} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} - \frac{1}{5} = 0 \\ x'(0) &= - c_{1} + 6 c_{2} - \frac{1}{5} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} - \frac{1}{5} &= 0 \quad (1) \\ - c_{1} + 6 c_{2} - \frac{1}{5} &= 1 \quad (2) \end{aligned} $$

Solve $c_{1} + c_{2} - \frac{1}{5} = 0$ for $c_{1}$: $c_{1} = \frac{1}{5} - c_{2}$.

Substitute in $- c_{1} + 6 c_{2} - \frac{1}{5} = 1$: $7 c_{2} - \frac{2}{5} = 1$.

$7 c_{2} - \frac{2}{5} = 1$ contains one unknown only, so $c_{2} = \frac{1}{5}$.

Back-substitution: $c_{1} = \frac{1}{5} - c_{2} = 0$.

Hence $c_{1} = 0$, $c_{2} = \frac{1}{5}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{e^{6 t}}{5} - \frac{e^{t}}{5}} $$

#### Recovering $y$

From Eq. 26.2, $y = (\dot x - ax - f)/b$. With the solution found,

$$ \dot x(t) = \frac{6 e^{6 t}}{5} - \frac{e^{t}}{5} $$

$$ y(t) = \frac{1}{2}\left(\dot x - (2)x - (0)\right) = \frac{2 e^{6 t}}{5} + \frac{e^{t}}{10} $$

#### Check in the original system

$$ \begin{aligned} \dot x &= \frac{6 e^{6 t}}{5} - \frac{e^{t}}{5} \\ ax + by + f &= \frac{6 e^{6 t}}{5} - \frac{e^{t}}{5} \\[4pt] \dot y &= \frac{12 e^{6 t}}{5} + \frac{e^{t}}{10} \\ cx + dy + g &= \frac{12 e^{6 t}}{5} + \frac{e^{t}}{10} \end{aligned} $$

Both pairs of expressions coincide, and $x(0) = 0$, $y(0) = \frac{1}{2}$ reproduce the initial data.

### (iv) $\dot x = 5x - 4y + e^{3t},\quad \dot y = x + y$, $\ x(0) = 1,\ y(0) = -1$

The system is linear with constant coefficients, in the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with

$$ a = 5,\quad b = -4,\quad c = 1,\quad d = 1,\quad f(t) = e^{3 t},\quad g(t) = 0 $$

#### Elimination of $y$

Since $b = -4 \neq 0$, the first equation can be solved for $y$ (Eq. 26.2):

$$ y = \frac{\dot x - ax - f}{b} = \frac{1}{-4}\left(\dot x - (5)x - (e^{3 t})\right) $$

Differentiate with respect to $t$ (everything is differentiable):

$$ \dot y = \frac{\ddot x - a\dot x - \dot f}{b} = \frac{1}{-4}\left(\ddot x - (5)\dot x - (3 e^{3 t})\right) $$

Substitute both expressions into the second equation, $\dot y = cx + dy + g$, and multiply by $b$:

$$ \ddot x - a\dot x - \dot f = bc\,x + d\,(\dot x - ax - f) + bg $$

Collect the terms in $\ddot x$, $\dot x$ and $x$ (Eq. 26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Numerically, $a + d = 6$, $ad - bc = (5)(1) - (-4)(1) = 9$ and $F(t) := \dot f + bg - df = (3 e^{3 t}) + (-4)(0) - (1)(e^{3 t}) = 2 e^{3 t}$, so

$$ \ddot{x} - 6\dot{x} + 9x = 2 e^{3 t} $$

Initial data. The condition on $y$ is converted into one on $\dot x$ with the first equation at $t = 0$: $\dot x(0) = a\,x(0) + b\,y(0) + f(0) = (5)(1) + (-4)(-1) + (1) = 10$.

The homogeneous equation $\ddot{x} - 6\dot{x} + 9x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 6 k + 9 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (-6)^2 - 4(1)(9) = 0$.

Factorising, $P(k) = \left(k - 3\right)^{2}$, so the roots are

$$ k = 3 \ \text{(multiplicity 2)} $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{3 t}$, $t e^{3 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{3 t} + c_{2} t e^{3 t} $$

The forcing $2 e^{3 t}$ is an exponential with exponent $s = 3$; we test it in the characteristic polynomial: $P(3) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $2$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{2}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t^{2} e^{3 t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= 3 K_{1} t^{2} e^{3 t} + 2 K_{1} t e^{3 t} \\ x_p''(t) &= 9 K_{1} t^{2} e^{3 t} + 12 K_{1} t e^{3 t} + 2 K_{1} e^{3 t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' - 6x_p' + 9x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 2 K_{1}\,e^{3 t} $$

This must equal the forcing $F(t) = 2 e^{3 t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $F$:

$$ \begin{aligned} e^{3 t}: &\quad 2 K_{1} = 2 \end{aligned} $$

The linear system is

$$ \begin{aligned} 2 K_{1} &= 2 \quad (1) \end{aligned} $$

$2 K_{1} = 2$ contains one unknown only, so $K_{1} = 1$.

Hence $K_{1} = 1$.

Therefore

$$ x_p(t) = t^{2} e^{3 t} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{3 t} + c_{2} t e^{3 t} + t^{2} e^{3 t} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= 3 c_{1} e^{3 t} + 3 c_{2} t e^{3 t} + c_{2} e^{3 t} + 3 t^{2} e^{3 t} + 2 t e^{3 t} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} = 1 \\ x'(0) &= 3 c_{1} + c_{2} = 10 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} &= 1 \quad (1) \\ 3 c_{1} + c_{2} &= 10 \quad (2) \end{aligned} $$

$c_{1} = 1$ contains one unknown only, so $c_{1} = 1$.

Substitute in $3 c_{1} + c_{2} = 10$: $c_{2} + 3 = 10$.

$c_{2} + 3 = 10$ contains one unknown only, so $c_{2} = 7$.

Hence $c_{1} = 1$, $c_{2} = 7$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = t^{2} e^{3 t} + 7 t e^{3 t} + e^{3 t}} $$

#### Recovering $y$

From Eq. 26.2, $y = (\dot x - ax - f)/b$. With the solution found,

$$ \dot x(t) = 3 t^{2} e^{3 t} + 23 t e^{3 t} + 10 e^{3 t} $$

$$ y(t) = \frac{1}{-4}\left(\dot x - (5)x - (e^{3 t})\right) = \frac{t^{2} e^{3 t}}{2} + 3 t e^{3 t} - e^{3 t} $$

#### Check in the original system

$$ \begin{aligned} \dot x &= 3 t^{2} e^{3 t} + 23 t e^{3 t} + 10 e^{3 t} \\ ax + by + f &= 3 t^{2} e^{3 t} + 23 t e^{3 t} + 10 e^{3 t} \\[4pt] \dot y &= \frac{3 t^{2} e^{3 t}}{2} + 10 t e^{3 t} \\ cx + dy + g &= \frac{3 t^{2} e^{3 t}}{2} + 10 t e^{3 t} \end{aligned} $$

Both pairs of expressions coincide, and $x(0) = 1$, $y(0) = -1$ reproduce the initial data.

### (v) $\dot x = 2x + 5y,\quad \dot y = -2x + \cos 3t$, $\ x(0) = 2,\ y(0) = -1$

The system is linear with constant coefficients, in the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with

$$ a = 2,\quad b = 5,\quad c = -2,\quad d = 0,\quad f(t) = 0,\quad g(t) = \cos{3 t} $$

#### Elimination of $y$

Since $b = 5 \neq 0$, the first equation can be solved for $y$ (Eq. 26.2):

$$ y = \frac{\dot x - ax - f}{b} = \frac{1}{5}\left(\dot x - (2)x - (0)\right) $$

Differentiate with respect to $t$ (everything is differentiable):

$$ \dot y = \frac{\ddot x - a\dot x - \dot f}{b} = \frac{1}{5}\left(\ddot x - (2)\dot x - (0)\right) $$

Substitute both expressions into the second equation, $\dot y = cx + dy + g$, and multiply by $b$:

$$ \ddot x - a\dot x - \dot f = bc\,x + d\,(\dot x - ax - f) + bg $$

Collect the terms in $\ddot x$, $\dot x$ and $x$ (Eq. 26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Numerically, $a + d = 2$, $ad - bc = (2)(0) - (5)(-2) = 10$ and $F(t) := \dot f + bg - df = (0) + (5)(\cos{3 t}) - (0)(0) = 5 \cos{3 t}$, so

$$ \ddot{x} - 2\dot{x} + 10x = 5 \cos{3 t} $$

Initial data. The condition on $y$ is converted into one on $\dot x$ with the first equation at $t = 0$: $\dot x(0) = a\,x(0) + b\,y(0) + f(0) = (2)(2) + (5)(-1) + (0) = -1$.

The homogeneous equation $\ddot{x} - 2\dot{x} + 10x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 2 k + 10 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (-2)^2 - 4(1)(10) = -36$.

Factorising, $P(k) = \left(k - 1 - 3 i\right) \left(k - 1 + 3 i\right)$, so the roots are

$$ k = 1 - 3 i, \qquad k = 1 + 3 i $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{t} \cos{3 t}$, $e^{t} \sin{3 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{t} \cos{3 t} + c_{2} e^{t} \sin{3 t} $$

The forcing $5 \cos{3 t}$ is a sinusoidal term: it is the real or imaginary part of $e^{(3 i)t}$, so we test $s = 3 i$ in the characteristic polynomial: $P(3 i) = 1 - 6 i$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} \cos{3 t} + K_{2} \sin{3 t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - 3 K_{1} \sin{3 t} + 3 K_{2} \cos{3 t} \\ x_p''(t) &= - 9 K_{1} \cos{3 t} - 9 K_{2} \sin{3 t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' - 2x_p' + 10x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = \left(K_{1} - 6 K_{2}\right)\,\cos 3t + \left(6 K_{1} + K_{2}\right)\,\sin 3t $$

This must equal the forcing $F(t) = 5 \cos{3 t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $F$:

$$ \begin{aligned} \cos 3t: &\quad K_{1} - 6 K_{2} = 5 \\ \sin 3t: &\quad 6 K_{1} + K_{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} K_{1} - 6 K_{2} &= 5 \quad (1) \\ 6 K_{1} + K_{2} &= 0 \quad (2) \end{aligned} $$

Solve $K_{1} - 6 K_{2} = 5$ for $K_{1}$: $K_{1} = 6 K_{2} + 5$.

Substitute in $6 K_{1} + K_{2} = 0$: $37 K_{2} + 30 = 0$.

$37 K_{2} + 30 = 0$ contains one unknown only, so $K_{2} = - \frac{30}{37}$.

Back-substitution: $K_{1} = 6 K_{2} + 5 = \frac{5}{37}$.

Hence $K_{1} = \frac{5}{37}$, $K_{2} = - \frac{30}{37}$.

Therefore

$$ x_p(t) = - \frac{30 \sin{3 t}}{37} + \frac{5 \cos{3 t}}{37} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{t} \cos{3 t} + c_{2} e^{t} \sin{3 t} - \frac{30 \sin{3 t}}{37} + \frac{5 \cos{3 t}}{37} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 3 c_{1} e^{t} \sin{3 t} + c_{1} e^{t} \cos{3 t} + c_{2} e^{t} \sin{3 t} + 3 c_{2} e^{t} \cos{3 t} - \frac{15 \sin{3 t}}{37} - \frac{90 \cos{3 t}}{37} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + \frac{5}{37} = 2 \\ x'(0) &= c_{1} + 3 c_{2} - \frac{90}{37} = -1 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + \frac{5}{37} &= 2 \quad (1) \\ c_{1} + 3 c_{2} - \frac{90}{37} &= -1 \quad (2) \end{aligned} $$

$c_{1} + \frac{5}{37} = 2$ contains one unknown only, so $c_{1} = \frac{69}{37}$.

Substitute in $c_{1} + 3 c_{2} - \frac{90}{37} = -1$: $3 c_{2} - \frac{21}{37} = -1$.

$3 c_{2} - \frac{21}{37} = -1$ contains one unknown only, so $c_{2} = - \frac{16}{111}$.

Hence $c_{1} = \frac{69}{37}$, $c_{2} = - \frac{16}{111}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = - \frac{16 e^{t} \sin{3 t}}{111} + \frac{69 e^{t} \cos{3 t}}{37} - \frac{30 \sin{3 t}}{37} + \frac{5 \cos{3 t}}{37}} $$

#### Recovering $y$

From Eq. 26.2, $y = (\dot x - ax - f)/b$. With the solution found,

$$ \dot x(t) = - \frac{637 e^{t} \sin{3 t}}{111} + \frac{53 e^{t} \cos{3 t}}{37} - \frac{15 \sin{3 t}}{37} - \frac{90 \cos{3 t}}{37} $$

$$ y(t) = \frac{1}{5}\left(\dot x - (2)x - (0)\right) = - \frac{121 e^{t} \sin{3 t}}{111} - \frac{17 e^{t} \cos{3 t}}{37} + \frac{9 \sin{3 t}}{37} - \frac{20 \cos{3 t}}{37} $$

#### Check in the original system

$$ \begin{aligned} \dot x &= - \frac{637 e^{t} \sin{3 t}}{111} + \frac{53 e^{t} \cos{3 t}}{37} - \frac{15 \sin{3 t}}{37} - \frac{90 \cos{3 t}}{37} \\ ax + by + f &= - \frac{637 e^{t} \sin{3 t}}{111} + \frac{53 e^{t} \cos{3 t}}{37} - \frac{15 \sin{3 t}}{37} - \frac{90 \cos{3 t}}{37} \\[4pt] \dot y &= \frac{32 e^{t} \sin{3 t}}{111} - \frac{138 e^{t} \cos{3 t}}{37} + \frac{60 \sin{3 t}}{37} + \frac{27 \cos{3 t}}{37} \\ cx + dy + g &= \frac{32 e^{t} \sin{3 t}}{111} - \frac{138 e^{t} \cos{3 t}}{37} + \frac{60 \sin{3 t}}{37} + \frac{27 \cos{3 t}}{37} \end{aligned} $$

Both pairs of expressions coincide, and $x(0) = 2$, $y(0) = -1$ reproduce the initial data.

### (vi) $\dot x = x + y + e^{-t},\quad \dot y = 4x - 2y + e^{2t}$, $\ x(0) = 1,\ y(0) = -1$

The system is linear with constant coefficients, in the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with

$$ a = 1,\quad b = 1,\quad c = 4,\quad d = -2,\quad f(t) = e^{-t},\quad g(t) = e^{2 t} $$

#### Elimination of $y$

Since $b = 1 \neq 0$, the first equation can be solved for $y$ (Eq. 26.2):

$$ y = \frac{\dot x - ax - f}{b} = \frac{1}{1}\left(\dot x - (1)x - (e^{-t})\right) $$

Differentiate with respect to $t$ (everything is differentiable):

$$ \dot y = \frac{\ddot x - a\dot x - \dot f}{b} = \frac{1}{1}\left(\ddot x - (1)\dot x - (- e^{-t})\right) $$

Substitute both expressions into the second equation, $\dot y = cx + dy + g$, and multiply by $b$:

$$ \ddot x - a\dot x - \dot f = bc\,x + d\,(\dot x - ax - f) + bg $$

Collect the terms in $\ddot x$, $\dot x$ and $x$ (Eq. 26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Numerically, $a + d = -1$, $ad - bc = (1)(-2) - (1)(4) = -6$ and $F(t) := \dot f + bg - df = (- e^{-t}) + (1)(e^{2 t}) - (-2)(e^{-t}) = e^{2 t} + e^{-t}$, so

$$ \ddot{x} + \dot{x} - 6x = e^{2 t} + e^{-t} $$

Initial data. The condition on $y$ is converted into one on $\dot x$ with the first equation at $t = 0$: $\dot x(0) = a\,x(0) + b\,y(0) + f(0) = (1)(1) + (1)(-1) + (1) = 1$.

The homogeneous equation $\ddot{x} + \dot{x} - 6x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + k - 6 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (1)^2 - 4(1)(-6) = 25$.

Factorising, $P(k) = \left(k - 2\right) \left(k + 3\right)$, so the roots are

$$ k = -3, \qquad k = 2 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-3 t}$, $e^{2 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-3 t} + c_{2} e^{2 t} $$

The forcing is a sum of terms. By linearity (Robinson Eq. 14.7) a particular integral is the sum of particular integrals of the separate terms, each found in turn.

#### Particular integral for the term $e^{-t}$

The forcing $e^{-t}$ is an exponential with exponent $s = -1$; we test it in the characteristic polynomial: $P(-1) = -6$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} e^{-t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} e^{-t} \\ x_p''(t) &= K_{1} e^{-t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + x_p' - 6x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = - 6 K_{1}\,e^{-t} $$

This must equal the forcing $F(t) = e^{-t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $F$:

$$ \begin{aligned} e^{-t}: &\quad - 6 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} - 6 K_{1} &= 1 \quad (1) \end{aligned} $$

$- 6 K_{1} = 1$ contains one unknown only, so $K_{1} = - \frac{1}{6}$.

Hence $K_{1} = - \frac{1}{6}$.

Therefore

$$ x_p(t) = - \frac{e^{-t}}{6} $$

#### Particular integral for the term $e^{2 t}$

The forcing $e^{2 t}$ is an exponential with exponent $s = 2$; we test it in the characteristic polynomial: $P(2) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t e^{2 t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= 2 K_{1} t e^{2 t} + K_{1} e^{2 t} \\ x_p''(t) &= 4 K_{1} t e^{2 t} + 4 K_{1} e^{2 t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + x_p' - 6x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 5 K_{1}\,e^{2 t} $$

This must equal the forcing $F(t) = e^{2 t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $F$:

$$ \begin{aligned} e^{2 t}: &\quad 5 K_{1} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} 5 K_{1} &= 1 \quad (1) \end{aligned} $$

$5 K_{1} = 1$ contains one unknown only, so $K_{1} = \frac{1}{5}$.

Hence $K_{1} = \frac{1}{5}$.

Therefore

$$ x_p(t) = \frac{t e^{2 t}}{5} $$

Adding the particular integrals,

$$ x_p(t) = \frac{t e^{2 t}}{5} - \frac{e^{-t}}{6} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = c_{1} e^{-3 t} + c_{2} e^{2 t} + \frac{t e^{2 t}}{5} - \frac{e^{-t}}{6} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 3 c_{1} e^{-3 t} + 2 c_{2} e^{2 t} + \frac{2 t e^{2 t}}{5} + \frac{e^{2 t}}{5} + \frac{e^{-t}}{6} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} - \frac{1}{6} = 1 \\ x'(0) &= - 3 c_{1} + 2 c_{2} + \frac{11}{30} = 1 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} - \frac{1}{6} &= 1 \quad (1) \\ - 3 c_{1} + 2 c_{2} + \frac{11}{30} &= 1 \quad (2) \end{aligned} $$

Solve $c_{1} + c_{2} - \frac{1}{6} = 1$ for $c_{1}$: $c_{1} = \frac{7}{6} - c_{2}$.

Substitute in $- 3 c_{1} + 2 c_{2} + \frac{11}{30} = 1$: $5 c_{2} - \frac{47}{15} = 1$.

$5 c_{2} - \frac{47}{15} = 1$ contains one unknown only, so $c_{2} = \frac{62}{75}$.

Back-substitution: $c_{1} = \frac{7}{6} - c_{2} = \frac{17}{50}$.

Hence $c_{1} = \frac{17}{50}$, $c_{2} = \frac{62}{75}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{t e^{2 t}}{5} + \frac{62 e^{2 t}}{75} - \frac{e^{-t}}{6} + \frac{17 e^{-3 t}}{50}} $$

#### Recovering $y$

From Eq. 26.2, $y = (\dot x - ax - f)/b$. With the solution found,

$$ \dot x(t) = \frac{2 t e^{2 t}}{5} + \frac{139 e^{2 t}}{75} + \frac{e^{-t}}{6} - \frac{51 e^{-3 t}}{50} $$

$$ y(t) = \frac{1}{1}\left(\dot x - (1)x - (e^{-t})\right) = \frac{t e^{2 t}}{5} + \frac{77 e^{2 t}}{75} - \frac{2 e^{-t}}{3} - \frac{34 e^{-3 t}}{25} $$

#### Check in the original system

$$ \begin{aligned} \dot x &= \frac{2 t e^{2 t}}{5} + \frac{139 e^{2 t}}{75} + \frac{e^{-t}}{6} - \frac{51 e^{-3 t}}{50} \\ ax + by + f &= \frac{2 t e^{2 t}}{5} + \frac{139 e^{2 t}}{75} + \frac{e^{-t}}{6} - \frac{51 e^{-3 t}}{50} \\[4pt] \dot y &= \frac{2 t e^{2 t}}{5} + \frac{169 e^{2 t}}{75} + \frac{2 e^{-t}}{3} + \frac{102 e^{-3 t}}{25} \\ cx + dy + g &= \frac{2 t e^{2 t}}{5} + \frac{169 e^{2 t}}{75} + \frac{2 e^{-t}}{3} + \frac{102 e^{-3 t}}{25} \end{aligned} $$

Both pairs of expressions coincide, and $x(0) = 1$, $y(0) = -1$ reproduce the initial data.

### (vii) $\dot x = 8x + 14y,\quad \dot y = 7x + y$, $\ x(0) = y(0) = 1$

The system is linear with constant coefficients, in the form $\dot x = ax + by + f(t)$, $\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with

$$ a = 8,\quad b = 14,\quad c = 7,\quad d = 1,\quad f(t) = 0,\quad g(t) = 0 $$

#### Elimination of $y$

Since $b = 14 \neq 0$, the first equation can be solved for $y$ (Eq. 26.2):

$$ y = \frac{\dot x - ax - f}{b} = \frac{1}{14}\left(\dot x - (8)x - (0)\right) $$

Differentiate with respect to $t$ (everything is differentiable):

$$ \dot y = \frac{\ddot x - a\dot x - \dot f}{b} = \frac{1}{14}\left(\ddot x - (8)\dot x - (0)\right) $$

Substitute both expressions into the second equation, $\dot y = cx + dy + g$, and multiply by $b$:

$$ \ddot x - a\dot x - \dot f = bc\,x + d\,(\dot x - ax - f) + bg $$

Collect the terms in $\ddot x$, $\dot x$ and $x$ (Eq. 26.3):

$$ \ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df $$

Numerically, $a + d = 9$, $ad - bc = (8)(1) - (14)(7) = -90$ and $F(t) := \dot f + bg - df = (0) + (14)(0) - (1)(0) = 0$, so

$$ \ddot{x} - 9\dot{x} - 90x = 0 $$

Initial data. The condition on $y$ is converted into one on $\dot x$ with the first equation at $t = 0$: $\dot x(0) = a\,x(0) + b\,y(0) + f(0) = (8)(1) + (14)(1) + (0) = 22$.

The homogeneous equation $\ddot{x} - 9\dot{x} - 90x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} - 9 k - 90 = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (-9)^2 - 4(1)(-90) = 441$.

Factorising, $P(k) = \left(k - 15\right) \left(k + 6\right)$, so the roots are

$$ k = -6, \qquad k = 15 $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $e^{-6 t}$, $e^{15 t}$, so the complementary function is

$$ x_h(t) = c_{1} e^{-6 t} + c_{2} e^{15 t} $$

The equation is homogeneous, so there is no particular integral and the general solution is the complementary function:

$$ x(t) = x_h(t) = c_{1} e^{-6 t} + c_{2} e^{15 t} $$

Initial conditions. Differentiate the general solution (product and chain rules):

$$ \begin{aligned} x'(t) &= - 6 c_{1} e^{-6 t} + 15 c_{2} e^{15 t} \end{aligned} $$

Evaluate at $t = 0$, using $e^{0} = 1$, $\cos 0 = 1$ and $\sin 0 = 0$:

$$ \begin{aligned} x(0) &= c_{1} + c_{2} = 1 \\ x'(0) &= - 6 c_{1} + 15 c_{2} = 22 \end{aligned} $$

The linear system is

$$ \begin{aligned} c_{1} + c_{2} &= 1 \quad (1) \\ - 6 c_{1} + 15 c_{2} &= 22 \quad (2) \end{aligned} $$

Solve $c_{1} + c_{2} = 1$ for $c_{1}$: $c_{1} = 1 - c_{2}$.

Substitute in $- 6 c_{1} + 15 c_{2} = 22$: $21 c_{2} - 6 = 22$.

$21 c_{2} - 6 = 22$ contains one unknown only, so $c_{2} = \frac{4}{3}$.

Back-substitution: $c_{1} = 1 - c_{2} = - \frac{1}{3}$.

Hence $c_{1} = - \frac{1}{3}$, $c_{2} = \frac{4}{3}$.

Substituting the constants into the general solution,

$$ \boxed{x(t) = \frac{4 e^{15 t}}{3} - \frac{e^{-6 t}}{3}} $$

#### Recovering $y$

From Eq. 26.2, $y = (\dot x - ax - f)/b$. With the solution found,

$$ \dot x(t) = 20 e^{15 t} + 2 e^{-6 t} $$

$$ y(t) = \frac{1}{14}\left(\dot x - (8)x - (0)\right) = \frac{2 e^{15 t}}{3} + \frac{e^{-6 t}}{3} $$

#### Check in the original system

$$ \begin{aligned} \dot x &= 20 e^{15 t} + 2 e^{-6 t} \\ ax + by + f &= 20 e^{15 t} + 2 e^{-6 t} \\[4pt] \dot y &= 10 e^{15 t} - 2 e^{-6 t} \\ cx + dy + g &= 10 e^{15 t} - 2 e^{-6 t} \end{aligned} $$

Both pairs of expressions coincide, and $x(0) = 1$, $y(0) = 1$ reproduce the initial data.

## Phase 4: Interpretation and checks

| Item | $x(t)$ | $y(t)$ |
| :--- | :--- | :--- |
| (i) | $- \frac{t^{2}}{6} - \frac{5 t}{18} - \frac{29 e^{3 t}}{27} + \frac{5 e^{2 t}}{4} - \frac{19}{108}$ | $- \frac{2 t^{2}}{3} - \frac{7 t}{9} - \frac{29 e^{3 t}}{27} + \frac{5 e^{2 t}}{2} - \frac{23}{54}$ |
| (ii) | $- \frac{32 e^{t} \sin{2 t}}{17} + \frac{26 e^{t} \cos{2 t}}{17} + \frac{2 \sin{2 t}}{17} - \frac{9 \cos{2 t}}{17}$ | $\frac{13 e^{t} \sin{2 t}}{17} + \frac{16 e^{t} \cos{2 t}}{17} - \frac{4 \sin{2 t}}{17} + \frac{\cos{2 t}}{17}$ |
| (iii) | $\frac{e^{6 t}}{5} - \frac{e^{t}}{5}$ | $\frac{2 e^{6 t}}{5} + \frac{e^{t}}{10}$ |
| (iv) | $t^{2} e^{3 t} + 7 t e^{3 t} + e^{3 t}$ | $\frac{t^{2} e^{3 t}}{2} + 3 t e^{3 t} - e^{3 t}$ |
| (v) | $- \frac{16 e^{t} \sin{3 t}}{111} + \frac{69 e^{t} \cos{3 t}}{37} - \frac{30 \sin{3 t}}{37} + \frac{5 \cos{3 t}}{37}$ | $- \frac{121 e^{t} \sin{3 t}}{111} - \frac{17 e^{t} \cos{3 t}}{37} + \frac{9 \sin{3 t}}{37} - \frac{20 \cos{3 t}}{37}$ |
| (vi) | $\frac{t e^{2 t}}{5} + \frac{62 e^{2 t}}{75} - \frac{e^{-t}}{6} + \frac{17 e^{-3 t}}{50}$ | $\frac{t e^{2 t}}{5} + \frac{77 e^{2 t}}{75} - \frac{2 e^{-t}}{3} - \frac{34 e^{-3 t}}{25}$ |
| (vii) | $\frac{4 e^{15 t}}{3} - \frac{e^{-6 t}}{3}$ | $\frac{2 e^{15 t}}{3} + \frac{e^{-6 t}}{3}$ |

- Every pair $(x, y)$ was substituted in **both** original equations and in the initial data (shown in each item and re-checked symbolically in `scripts/verify_topic3_topic4.py`).
- Characteristic exponents seen: (i) $2, 3$ (real); (ii) $1 \pm 2i$ (spiral) with the forcing $\cos 2t$ at a different frequency; (iii) $6, -1$ (saddle; the forcing $e^{t}$ has exponent $1$, which is **not** a root, so no extra factor $t$); (iv) $3$ double (improper-node type), and the forcing $e^{3t}$ resonates with the double root, giving $t^2e^{3t}$; (v) $1 \pm 3i$; (vi) $2, -3$ with the forcing exponent $2$ resonant (term $te^{2t}$) and $-1$ not; (vii) $15, -6$ (homogeneous saddle).
- Cross-check of the homogeneous parts with Topic 4: (iv) and (v) have the same matrices as Examples 8.2 and 7.1; (vii) is the matrix of Exercise 9 (i).
- Dimensions: with $t$ in seconds the matrix entries have units s$^{-1}$ and the forcings those of $\dot x$; the elimination keeps this consistent ($a + d$ in s$^{-1}$, $ad - bc$ in s$^{-2}$).
