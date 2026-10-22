---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 8"
dificultad: media
id: "e8"
pill: "Reduction of Order • Integrating Factor • General Solution"
tags:
  - problema-resuelto
  - reduccion-de-orden
  - factor-integrante
  - ecuacion-inhomogenea
---

# Problem 3.II.8: Reduction of Order for the Inhomogeneous Equation

> Official exercise 8 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

The so-called method of reduction of order can be used to find one solution of the inhomogeneous equation $L[y] = y'' + p(t)y' + q(t)y = g(t)$, provided one solution $y_1(t)$ of the corresponding homogeneous equation is known. Indeed, writing $y = v(t)y_1(t)$, show that $y(t)$ satisfies $L[y] = g$ if $v$ is a solution of

$$ y_1(t)v'' + \left[2y_1' + p(t)y_1\right]v' = g(t). $$

This is a first order linear equation for $v'(t)$. Solving this equation, integrating the result, and then multiplying by $y_1(t)$ leads to the general solution of the problem for $y(t)$.

## Phase 1: Setup and hypotheses

Hypotheses: $p, q, g$ continuous on an interval $I$; $y_1$ is a known solution of $L[y_1] = 0$ with $y_1 \neq 0$ on $I$ (so that we can divide by $y_1$). Unknown: $v(t)$, with $y = vy_1$.

## Phase 2: Formulation

The idea is the same as in Topic 3, Sec. 7: promote the constant in $Ay_1$ to a function, $y = vy_1$. The product rule is used twice:

$$ y' = v'y_1 + vy_1', \qquad y'' = v''y_1 + 2v'y_1' + vy_1'' $$

> [!info] Class notes and complement [Notes, p. 7]
> The notes reduce the order of the homogeneous equation: with a known solution $u$, set $x = yu$; then $\big[u'' + pu' + qu\big]y + \big[2u' + pu\big]y' + uy'' = 0$, the first bracket is $0$, and $z = y'$ satisfies the first-order equation $uz' + (2u' + pu)z = 0$. Here the notes' $u$ is $y_1$ and their $y$ is $v$; keeping the forcing on the right side is a complement (not in the class notes).

## Phase 3: Derivation

#### Step 1: substitute in $L[y]$

$$ L[y] = y'' + py' + qy = \left(v''y_1 + 2v'y_1' + vy_1''\right) + p\left(v'y_1 + vy_1'\right) + qvy_1 $$

Group the terms by $v''$, $v'$ and $v$:

$$ L[y] = y_1v'' + \left(2y_1' + py_1\right)v' + v\underbrace{\left(y_1'' + py_1' + qy_1\right)}_{L[y_1] = 0} $$

The bracket multiplying $v$ is $L[y_1]$, which is zero because $y_1$ solves the homogeneous equation; this is why the undifferentiated $v$ disappears. Therefore

$$ L[y] = y_1v'' + \left(2y_1' + py_1\right)v'  $$

and $L[y] = g$ holds if and only if $y_1v'' + [2y_1' + py_1]v' = g$, which is the equation of the statement. $\blacksquare$

#### Step 2: solve the first-order equation for $w = v'$

Divide by $y_1 \neq 0$ and put $w = v'$:

$$ w' + \left(\frac{2y_1'}{y_1} + p\right)w = \frac{g}{y_1} $$

This is a linear first-order equation (Topic 2). The integrating factor is $\mu = \exp\int\left(\frac{2y_1'}{y_1} + p\right)dt = y_1^2\,e^{P(t)}$, with $P(t) = \int p\,dt$ (because $\int\frac{2y_1'}{y_1}dt = 2\ln|y_1|$). The product rule gives $\frac{d}{dt}(\mu w) = \mu w' + \mu'w = \mu\left(w' + \left(\frac{2y_1'}{y_1} + p\right)w\right) = \mu\frac{g}{y_1}$:

$$ \frac{d}{dt}\left(y_1^2e^{P}w\right) = y_1e^{P}g \quad\Longrightarrow\quad w(t) = \frac{1}{y_1^2e^{P}}\left[\int y_1e^{P}g\,dt + c_1\right] $$

#### Step 3: integrate for $v$ and multiply by $y_1$

$$ v(t) = \int w\,dt + c_2, \qquad y(t) = y_1(t)\,v(t) = y_1(t)\left\{c_2 + \int\frac{1}{y_1^2e^{P}}\left[c_1 + \int y_1e^{P}g\,dt\right]dt\right\} $$

This expression contains two arbitrary constants $c_1, c_2$. Setting $g = 0$ it reduces to the homogeneous solutions $y = c_2y_1 + c_1y_1\int\frac{dt}{y_1^2e^{P}}$ (the second solution of Robinson Exercise 17.7), and the part that does not contain $c_1, c_2$ is a particular solution of $L[y] = g$. The two homogeneous solutions $y_1$ and $y_2 = y_1\int\frac{dt}{y_1^2e^{P}}$ are independent: by the product rule $y_2' = y_1'\int\frac{dt}{y_1^2e^{P}} + \frac{1}{y_1e^{P}}$, so $W = y_1y_2' - y_2y_1' = e^{-P} \neq 0$ (the terms with the integral cancel). Hence complementary function plus particular integral, with two free constants, is the general solution (Robinson Sec. 14.1).

## Phase 4: Interpretation and checks

- The constant $c_2$ multiplies $y_1$ itself (the known solution) and $c_1$ multiplies $y_1\int\frac{dt}{y_1^2e^{P}}$, a second, independent homogeneous solution. Their Wronskian is $W = e^{-P}$, nowhere zero: consistent with Abel's identity $W = W_0\exp(-\int p)$.
- Check of the Wronskian: $y_2 = y_1\int\frac{dt}{y_1^2e^{P}}$ gives $y_2' = y_1'\int\frac{dt}{y_1^2e^P} + \frac{1}{y_1e^{P}}$, hence $W = y_1y_2' - y_2y_1' = \frac{1}{e^{P}}$ (the $y_1y_1'\int\dots$ terms cancel).
- Compared with variation of constants, reduction of order needs only **one** homogeneous solution, at the price of two nested integrations.
- The method applies on any interval where $y_1 \neq 0$; where $y_1$ vanishes the division is not allowed and the intervals must be treated separately.
