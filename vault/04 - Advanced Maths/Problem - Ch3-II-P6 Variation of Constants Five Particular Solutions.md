---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 6"
dificultad: media
id: "e6"
pill: "Variation of Parameters • Euler Equation • Integral Answers"
tags:
  - problema-resuelto
  - variacion-de-constantes
  - wronskiano
  - ecuacion-de-euler
---

# Problem 3.II.6: Variation of Constants: Five Particular Solutions

> Official exercise 6 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

Use the method of variation of constants to find a particular solution for the following equations:

- (i) $y'' - y' - 6y = e^{x}$;
- (ii) $\ddot x - x = t^{-1}$ (leave the answer as an integral);
- (iii) $y'' + 4y = \cot 2x$. Use that $\int\csc x\,dx = \ln|\csc x - \cot x|$;
- (iv) $t^2\ddot x - 2x = t^3$ (to find the solutions of the homogeneous equation, try solutions of the form $x = t^k$ with $k$ a parameter);
- (v) $\ddot x - 4\dot x = \tan t$ (leave your answer as an integral).

## Phase 1: Setup and hypotheses

Each equation is linear, second-order, inhomogeneous. Variation of constants (Lagrange; Robinson Ch. 18, Topic 3 Sec. 8) needs: (a) the equation in **standard form** $\ddot x + p\dot x + qx = g$ with the coefficient of the highest derivative equal to $1$; (b) two linearly independent solutions $x_1, x_2$ of the homogeneous equation; (c) $g$ continuous on an interval $I$ where the coefficients are continuous. Then, on $I$,

$$ x_p = -x_1\int\frac{x_2\,g}{W}\,dt + x_2\int\frac{x_1\,g}{W}\,dt, \qquad W = x_1\dot x_2 - x_2\dot x_1 \neq 0 \quad (\text{Robinson Eq. 18.8}) $$

| Item | Standard form | Interval $I$ where $g$ and the coefficients are continuous |
| :--- | :--- | :--- |
| (i) | $y'' - y' - 6y = e^x$ | $\mathbb R$ |
| (ii) | $\ddot x - x = 1/t$ | $t > 0$ (or $t < 0$) |
| (iii) | $y'' + 4y = \cot 2x$ | $0 < x < \pi/2$ (between zeros of $\sin 2x$) |
| (iv) | $\ddot x - \dfrac{2}{t^2}x = t$ (divide by $t^2$) | $t > 0$ (or $t < 0$) |
| (v) | $\ddot x - 4\dot x = \tan t$ | $-\pi/2 < t < \pi/2$ |

## Phase 2: Formulation: the derivation of the formula, recalled

Replace the constants of $x_h = c_1x_1 + c_2x_2$ by functions: $x = u_1x_1 + u_2x_2$. Choose $\dot u_1x_1 + \dot u_2x_2 = 0$ (18.7), so that $\dot x = u_1\dot x_1 + u_2\dot x_2$; substituting in the equation and using $L[x_1] = L[x_2] = 0$ leaves $\dot u_1\dot x_1 + \dot u_2\dot x_2 = g$. Cramer's rule on the system with determinant $W$ gives

$$ \dot u_1 = -\frac{x_2\,g}{W}, \qquad \dot u_2 = \frac{x_1\,g}{W}, \qquad x_p = u_1x_1 + u_2x_2 $$

Constants of integration only add multiples of $x_1, x_2$, so they may be dropped.

> [!info] Method of the class notes [Notes, p. 8]
> This is the derivation of the notes: $x = u_1x_1 + u_2x_2$, impose $u_1'x_1 + u_2'x_2 = 0$, so $u_1' = -u_2'x_2/x_1$ $(\ast)$; substituting in the equation leaves $u_1'x_1' + u_2'x_2' = f$, and with $(\ast)$ $u_2'(x_1x_2' - x_2x_1')/x_1 = f$, hence $u_2' = \frac{f\,x_1}{W}$ and $u_1' = -\frac{f\,x_2}{W}$. Cramer's rule gives the same without dividing by $x_1$.
>
> Discrepancy with the notes: they print $u_1' = f\,x_2/W$ without the minus sign, but $(\ast)$ gives $-f\,x_2/W$. Check with $x'' + x' - 6x = 12$: the minus sign gives $x_N = -2$, which satisfies the equation; without it $x_N = -\frac25$ and $L[x_N] = \frac{12}{5} \neq 12$.

## Phase 3: Derivation

### (i) $y'' - y' - 6y = e^x$

Homogeneous equation: $y = e^{kx}$ gives $k^2 - k - 6 = (k - 3)(k + 2) = 0$, so $k = 3, -2$.

The homogeneous solutions are $y_1 = e^{3 x}$ and $y_2 = e^{-2 x}$. Their Wronskian is

$$ W = y_1\,y_2' - y_2\,y_1' = (e^{3 x})(- 2 e^{-2 x}) - (e^{-2 x})(3 e^{3 x}) = - 5 e^{x} $$

With $g = e^{x}$ (equation in standard form, coefficient of $y''$ equal to $1$), Cramer's rule gives $u_1' = -\dfrac{y_2\,g}{W}$ and $u_2' = \dfrac{y_1\,g}{W}$:

$$ u_1' = -\frac{(e^{-2 x})(e^{x})}{- 5 e^{x}} = \frac{e^{-2 x}}{5}, \qquad u_2' = \frac{(e^{3 x})(e^{x})}{- 5 e^{x}} = - \frac{e^{3 x}}{5} $$

Integrate (antiderivatives of exponentials, $\int e^{kx}dx = e^{kx}/k$):

$$ u_1 = \int \frac{e^{-2 x}}{5}\,dx = - \frac{e^{-2 x}}{10}, \qquad u_2 = \int - \frac{e^{3 x}}{5}\,dx = - \frac{e^{3 x}}{15} $$

$$ y_p = u_1y_1 + u_2y_2 = \left(- \frac{e^{-2 x}}{10}\right)e^{3x} + \left(- \frac{e^{3 x}}{15}\right)e^{-2x} = - \frac{e^{x}}{6} = - \frac{e^{x}}{6} $$

Check: $y_p' = - \frac{e^{x}}{6}$, $y_p'' = - \frac{e^{x}}{6}$, so $y_p'' - y_p' - 6y_p = (- \frac{e^{x}}{6}) - (- \frac{e^{x}}{6}) - 6(- \frac{e^{x}}{6}) = e^x$.

### (ii) $\ddot x - x = t^{-1}$ (answer as an integral)

Homogeneous equation: $k^2 - 1 = 0$, so $k = \pm 1$: $x_1 = e^{t}$, $x_2 = e^{-t}$.

The homogeneous solutions are $x_1 = e^{t}$ and $x_2 = e^{-t}$. Their Wronskian is

$$ W = x_1\,x_2' - x_2\,x_1' = (e^{t})(- e^{-t}) - (e^{-t})(e^{t}) = -2 $$

With $g = \frac{1}{t}$ (equation in standard form, coefficient of $x''$ equal to $1$), Cramer's rule gives $u_1' = -\dfrac{x_2\,g}{W}$ and $u_2' = \dfrac{x_1\,g}{W}$:

$$ u_1' = -\frac{(e^{-t})(\frac{1}{t})}{-2} = \frac{e^{-t}}{2 t}, \qquad u_2' = \frac{(e^{t})(\frac{1}{t})}{-2} = - \frac{e^{t}}{2 t} $$

The antiderivatives of $e^{-s}/s$ and $e^{s}/s$ are not elementary (they are exponential integrals). We keep them as integrals from a fixed base point $t_0 > 0$ (the interval where $g = 1/t$ is continuous, $t > 0$), which is a legitimate antiderivative by the fundamental theorem of calculus:

$$ u_1(t) = \frac12\int_{t_0}^{t}\frac{e^{-s}}{s}\,ds, \qquad u_2(t) = -\frac12\int_{t_0}^{t}\frac{e^{s}}{s}\,ds $$

$$ \boxed{x_p(t) = \frac{e^{t}}{2}\int_{t_0}^{t}\frac{e^{-s}}{s}\,ds - \frac{e^{-t}}{2}\int_{t_0}^{t}\frac{e^{s}}{s}\,ds \quad (t, t_0 > 0)} $$

Combining the exponentials inside one integral, $x_p(t) = \dfrac12\displaystyle\int_{t_0}^{t}\frac{e^{t - s} - e^{-(t - s)}}{s}\,ds = \int_{t_0}^{t}\frac{\sinh(t - s)}{s}\,ds$.

#### Verification by differentiation (Leibniz rule)

Let $I_1(t) = \int_{t_0}^{t}e^{-s}s^{-1}ds$ and $I_2(t) = \int_{t_0}^{t}e^{s}s^{-1}ds$, so $I_1' = e^{-t}/t$ and $I_2' = e^{t}/t$. Then $x_p = \frac12(e^tI_1 - e^{-t}I_2)$ and, by the product rule,

$$ \dot x_p = \frac12\left(e^tI_1 + e^{-t}I_2\right) + \frac12\left(e^t\frac{e^{-t}}{t} - e^{-t}\frac{e^{t}}{t}\right) = \frac12\left(e^tI_1 + e^{-t}I_2\right) $$

$$ \ddot x_p = \frac12\left(e^tI_1 - e^{-t}I_2\right) + \frac12\left(e^t\frac{e^{-t}}{t} + e^{-t}\frac{e^{t}}{t}\right) = x_p + \frac1t $$

so $\ddot x_p - x_p = 1/t$, as required.

### (iii) $y'' + 4y = \cot 2x$

Homogeneous equation: $k^2 + 4 = 0$, $k = \pm 2i$, so $y_1 = \cos 2x$, $y_2 = \sin 2x$.

Wronskian (chain rule: $(\cos 2x)' = -2\sin 2x$, $(\sin 2x)' = 2\cos 2x$):

$$ W = \cos 2x\cdot 2\cos 2x - \sin 2x\cdot(-2\sin 2x) = 2(\cos^2 2x + \sin^2 2x) = 2 $$

Cramer's rule with $g = \cot 2x = \cos 2x/\sin 2x$:

$$ u_1' = -\frac{\sin 2x\,\cot 2x}{2} = -\frac{\cos 2x}{2}, \qquad u_2' = \frac{\cos 2x\,\cot 2x}{2} = \frac{\cos^2 2x}{2\sin 2x} $$

For $u_2'$ use $\cos^2 2x = 1 - \sin^2 2x$: $u_2' = \dfrac{1 - \sin^2 2x}{2\sin 2x} = \dfrac12\left(\csc 2x - \sin 2x\right)$. Integrate with the substitution $s = 2x$, $ds = 2\,dx$, and the hint $\int\csc s\,ds = \ln|\csc s - \cot s|$:

$$ u_1 = -\frac12\int\cos 2x\,dx = -\frac12\cdot\frac{\sin 2x}{2} = -\frac{\sin 2x}{4} $$

$$ \int\csc 2x\,dx = \frac12\int\csc s\,ds = \frac12\ln|\csc 2x - \cot 2x|, \qquad \int\sin 2x\,dx = -\frac{\cos 2x}{2} $$

$$ u_2 = \frac12\left[\frac12\ln|\csc 2x - \cot 2x| + \frac{\cos 2x}{2}\right] = \frac14\ln|\csc 2x - \cot 2x| + \frac{\cos 2x}{4} $$

Assemble $y_p = u_1y_1 + u_2y_2$; the terms in $\sin 2x\cos 2x$ cancel:

$$ y_p = -\frac{\sin 2x\cos 2x}{4} + \left[\frac14\ln|\csc 2x - \cot 2x| + \frac{\cos 2x}{4}\right]\sin 2x = \frac14\,\sin 2x\;\ln\left|\csc 2x - \cot 2x\right| $$

Since $\csc 2x - \cot 2x = \dfrac{1 - \cos 2x}{\sin 2x} = \dfrac{2\sin^2x}{2\sin x\cos x} = \tan x$, an equivalent form is $y_p = \tfrac14\sin 2x\,\ln|\tan x|$.

Check by differentiating $y_p = \frac14\sin 2x\,\ell$ with $\ell = \ln\tan x$, $\ell' = \frac{\sec^2x}{\tan x} = \frac{2}{\sin 2x}$: $y_p' = \frac12\cos 2x\,\ell + \frac14\sin 2x\cdot\frac{2}{\sin 2x} = \frac12\cos 2x\,\ell + \frac12$; $y_p'' = -\sin 2x\,\ell + \frac12\cos 2x\cdot\frac{2}{\sin 2x} = -\sin 2x\,\ell + \cot 2x$; hence $y_p'' + 4y_p = -\sin 2x\,\ell + \cot 2x + \sin 2x\,\ell = \cot 2x$.

### (iv) $t^2\ddot x - 2x = t^3$

Homogeneous equation $t^2\ddot x - 2x = 0$. Try $x = t^k$ (chain/power rule): $\dot x = kt^{k-1}$, $\ddot x = k(k - 1)t^{k-2}$, so $t^2\ddot x - 2x = [k(k - 1) - 2]t^k = (k^2 - k - 2)t^k = (k - 2)(k + 1)t^k = 0$, hence $k = 2, -1$: $x_1 = t^2$, $x_2 = t^{-1}$ ($t > 0$).

Standard form: divide by $t^2$ (coefficient of $\ddot x$ must be $1$): $\ddot x - \dfrac{2}{t^2}x = \dfrac{t^3}{t^2} = t$, so $g(t) = t$ (**not** $t^3$).

The homogeneous solutions are $x_1 = t^{2}$ and $x_2 = \frac{1}{t}$. Their Wronskian is

$$ W = x_1\,x_2' - x_2\,x_1' = (t^{2})(- \frac{1}{t^{2}}) - (\frac{1}{t})(2 t) = -3 $$

With $g = t$ (equation in standard form, coefficient of $x''$ equal to $1$), Cramer's rule gives $u_1' = -\dfrac{x_2\,g}{W}$ and $u_2' = \dfrac{x_1\,g}{W}$:

$$ u_1' = -\frac{(\frac{1}{t})(t)}{-3} = \frac{1}{3}, \qquad u_2' = \frac{(t^{2})(t)}{-3} = - \frac{t^{3}}{3} $$

$$ u_1 = \int \frac{1}{3}\,dt = \frac{t}{3}, \qquad u_2 = \int - \frac{t^{3}}{3}\,dt = - \frac{t^{4}}{12} $$

$$ x_p = u_1x_1 + u_2x_2 = \left(\frac{t}{3}\right)t^2 + \left(- \frac{t^{4}}{12}\right)t^{-1} = \frac{t^{3}}{4} = \frac{t^{3}}{4} $$

Check in the original equation: $\ddot x_p = \frac{3 t}{2}$, so $t^2\ddot x_p - 2x_p = \frac{3 t^{3}}{2} - \frac{t^{3}}{2} = t^3$.

### (v) $\ddot x - 4\dot x = \tan t$ (answer as an integral)

Homogeneous equation: $k^2 - 4k = k(k - 4) = 0$, $k = 0, 4$: $x_1 = 1$, $x_2 = e^{4t}$.

The homogeneous solutions are $x_1 = 1$ and $x_2 = e^{4 t}$. Their Wronskian is

$$ W = x_1\,x_2' - x_2\,x_1' = (1)(4 e^{4 t}) - (e^{4 t})(0) = 4 e^{4 t} $$

With $g = \tan {t}$ (equation in standard form, coefficient of $x''$ equal to $1$), Cramer's rule gives $u_1' = -\dfrac{x_2\,g}{W}$ and $u_2' = \dfrac{x_1\,g}{W}$:

$$ u_1' = -\frac{(e^{4 t})(\tan {t})}{4 e^{4 t}} = - \frac{\tan {t}}{4}, \qquad u_2' = \frac{(1)(\tan {t})}{4 e^{4 t}} = \frac{e^{-4 t} \tan {t}}{4} $$

The first integral is elementary: $\int -\frac14\tan t\,dt = \frac14\ln|\cos t|$ (since $\frac{d}{dt}\ln\cos t = -\tan t$). The second, $\int e^{-4s}\tan s\,ds$, is not elementary, so it is left as an integral from a base point $t_0 \in (-\pi/2, \pi/2)$:

$$ u_1(t) = \frac14\ln\cos t, \qquad u_2(t) = \frac14\int_{t_0}^{t}e^{-4s}\tan s\,ds $$

$$ \boxed{x_p(t) = \frac14\ln\cos t + \frac{e^{4t}}{4}\int_{t_0}^{t}e^{-4s}\tan s\,ds \qquad (|t|, |t_0| < \pi/2)} $$

#### Verification by differentiation

With $I(t) = \int_{t_0}^{t}e^{-4s}\tan s\,ds$, $I' = e^{-4t}\tan t$. Product rule: $\dot x_p = -\frac14\tan t + e^{4t}I + \frac{e^{4t}}{4}e^{-4t}\tan t = e^{4t}I$ (the two tangent terms cancel). Again, $\ddot x_p = 4e^{4t}I + e^{4t}e^{-4t}\tan t = 4\dot x_p + \tan t$, i.e. $\ddot x_p - 4\dot x_p = \tan t$.

## Phase 4: Interpretation and checks

| Item | Particular solution $x_p$ | Domain |
| :--- | :--- | :--- |
| (i) | $-\dfrac{e^{x}}{6}$ | $\mathbb R$ |
| (ii) | $\dfrac{e^{t}}{2}\displaystyle\int_{t_0}^{t}\frac{e^{-s}}{s}ds - \dfrac{e^{-t}}{2}\int_{t_0}^{t}\frac{e^{s}}{s}ds$ | $t > 0$ |
| (iii) | $\dfrac14\sin 2x\,\ln\vert \csc 2x - \cot 2x\vert  = \dfrac14\sin 2x\,\ln\vert \tan x\vert $ | $0 < x < \pi/2$ |
| (iv) | $\dfrac{t^3}{4}$ | $t > 0$ |
| (v) | $\dfrac14\ln\cos t + \dfrac{e^{4t}}{4}\displaystyle\int_{t_0}^{t}e^{-4s}\tan s\,ds$ | $\vert t\vert  < \pi/2$ |

- The general solution of each equation is $x_h + x_p$ with the two homogeneous solutions used above.
- (i) and (iv) could also have been found by undetermined coefficients ($Ke^x$ and $Kt^3$); both methods agree ($-\frac16e^x$ and $\frac14t^3$), a useful cross-check of the Wronskian bookkeeping. (iii) and (v) have forcings ($\cot$, $\tan$) outside the family of undetermined coefficients, which is the reason for the method.
- (iv) is an Euler equation: the substitution $x = t^k$ turns it into an algebraic equation for $k$, and its standard form needs the division by $t^2$ before applying the formula.
- Wronskians: $-5e^{x}$ in (i) (consistent with Abel's identity, $W = W_0e^{x}$ since $p = -1$), $-2$ in (ii), $2$ in (iii), $-3$ in (iv) and $4e^{4t}$ in (v) (Abel: $p = -4$, $W = W_0e^{4t}$); none vanishes on its interval.
- The sheet works in dimensionless variables, so no unit check is attached to the forcings ($t^3$, $e^{x}$, $\cot 2x$, $\tan t$ are pure numbers); the check that matters is that each particular solution reproduces its forcing exactly, which was done symbolically.
- Every particular solution (and the integral forms, via the differentiation above) was verified symbolically in `scripts/verify_topic3_topic4.py`.
