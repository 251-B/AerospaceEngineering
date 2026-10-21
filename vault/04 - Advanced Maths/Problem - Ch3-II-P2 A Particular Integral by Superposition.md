---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 2"
dificultad: media
id: "e2"
pill: "Superposition • Exponential Forcing"
tags:
  - problema-resuelto
  - superposicion
  - coeficientes-indeterminados
  - resonancia
---

# Problem 3.II.2: A Particular Integral by Superposition

> Official exercise 2 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

Find a particular solution for $\ddot x + \dot x - 2x = 12e^{-t} - 6e^{t}$. You may find useful parts (iii) and (iv) of the previous exercise.

## Phase 1: Setup

The equation is $L[x] = \ddot x + \dot x - 2x = f$ with $f = 12e^{-t} - 6e^{t}$, the same operator $L$ as items (iii) and (iv) of Exercise 1. $L$ is linear (Robinson Eq. 11.11), so if $L[x_a] = f_a$ and $L[x_b] = f_b$ then $L[\alpha x_a + \beta x_b] = \alpha f_a + \beta f_b$ (Robinson Eq. 14.7). Hypothesis: nothing more is needed, since any single solution of $L[x] = f$ is a particular integral.

## Phase 2: Formulation

Rewrite the forcing in terms of the two forcings of Exercise 1:

$$ f = 12e^{-t} - 6e^{t} = 4\,\underbrace{\left(3e^{-t}\right)}_{f_a\ \text{(item iii)}} - 6\,\underbrace{\left(e^{t}\right)}_{f_b\ \text{(item iv)}} $$

Item (iii) found $x_a$ with $L[x_a] = 3e^{-t}$ and item (iv) found $x_b$ with $L[x_b] = e^{t}$. Then $x_p = 4x_a - 6x_b$.

## Phase 3: Derivation

#### The two particular integrals of Exercise 1

$P(k) = k^2 + k - 2 = (k - 1)(k + 2)$ has roots $1$ and $-2$. For $3e^{-t}$ the exponent is $s = -1$, $P(-1) = 1 - 1 - 2 = -2 \neq 0$, so $x_a = K e^{-t}$ and, since $\dot x_a = -Ke^{-t}$, $\ddot x_a = Ke^{-t}$: $L[x_a] = (K - K - 2K)e^{-t} = -2Ke^{-t} = 3e^{-t}$, hence $K = -\tfrac32$:

$$ x_a(t) = -\tfrac32 e^{-t} $$

For $e^{t}$ the exponent is $s = 1$, a simple root ($P(1) = 1 + 1 - 2 = 0$), so the guess is $x_b = Kte^{t}$. By the product rule $\dot x_b = K(1 + t)e^{t}$ and $\ddot x_b = K(2 + t)e^{t}$, so

$$ L[x_b] = K\left[(2 + t) + (1 + t) - 2t\right]e^{t} = 3Ke^{t} = e^{t} \;\Longrightarrow\; K = \tfrac13,\qquad x_b(t) = \tfrac13\,t\,e^{t} $$

#### Superposition

$$ x_p = 4x_a - 6x_b = 4\left(-\tfrac32 e^{-t}\right) - 6\left(\tfrac13 te^{t}\right) = - 2 t e^{t} - 6 e^{-t} $$

#### Direct verification by substitution

$$ \begin{aligned} \dot x_p &= - 2 t e^{t} - 2 e^{t} + 6 e^{-t} \\ \ddot x_p &= - 2 t e^{t} - 4 e^{t} - 6 e^{-t} \end{aligned} $$

$$ \ddot x_p + \dot x_p - 2x_p = \left(- 2 t e^{t} - 4 e^{t} - 6 e^{-t}\right) + \left(- 2 t e^{t} - 2 e^{t} + 6 e^{-t}\right) - 2\left(- 2 t e^{t} - 6 e^{-t}\right) = - 6 e^{t} + 12 e^{-t} $$

This is $12e^{-t} - 6e^{t}$, as required.

## Phase 4: Interpretation and checks

> [!result] Result
> A particular solution is $x_p(t) = - 2 t e^{t} - 6 e^{-t}$.
>
> The general solution is $x(t) = c_1e^{t} + c_2e^{-2t} - 6e^{-t} - 2te^{t}$ (the roots $1$ and $-2$ of $P$ give the complementary function).

- The term $-2te^{t}$ carries the extra factor $t$ because $e^{t}$ solves the homogeneous equation (resonance); the term $-6e^{-t}$ does not.
- Particular integrals are not unique: adding any multiple of $e^{t}$ or $e^{-2t}$ gives another one; the answer above is the one with no such terms.
- Dimensions: with $[t] = $ s, each term of $L[x]$ has the units of $f$; both sides are exponentials of a dimensionless argument $t/(1\ \mathrm{s})$, so the check is purely numerical.
