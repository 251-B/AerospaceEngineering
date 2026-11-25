---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 4"
dificultad: media
id: "e4"
pill: "Euler-Cauchy eigenproblem and Rayleigh quotient"
tags:
  - problema-resuelto
  - sturm-liouville
  - rayleigh-quotient
  - euler-cauchy
---

# Problem 6.4: Euler-Cauchy Eigenvalue Problem and Rayleigh Quotient

> Official exercise 4 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Consider the eigenvalue problem $x^2\phi''(x) + x\phi'(x) + \lambda\phi(x) = 0$ on the interval $[1, 2]$, with boundary conditions $\phi(1) = \phi(2) = 0$.

1. Show that multiplying by $1/x$ puts this equation into Sturm-Liouville form.
2. Show that $\lambda \ge 0$, and determine all possible eigenvalues. Is $\lambda = 0$ an eigenvalue?
3. What are the eigenfunctions?

## Formulation and Sturm-Liouville Structure

Multiply the equation by $1/x$ (allowed since $x \in [1,2]$, $x \ne 0$):
$$x\phi'' + \phi' + \frac{\lambda}{x}\phi = 0.$$
By the product rule $(x\phi')' = \phi' + x\phi''$, so
$$\boxed{(x\phi')' + \frac{\lambda}{x}\phi = 0}$$
which is $[p\phi']' + [\lambda\sigma + q]\phi = 0$ with
$$p(x) = x > 0,\qquad \sigma(x) = \frac1x > 0,\qquad q(x) = 0\qquad\text{on }[1,2].$$
This agrees with the integrating factor of [[Problem - Ch6-P3 Integrating Factor for Sturm-Liouville Self-Adjoint Form]]: dividing the original equation by $x^2$ gives $\alpha = 1/x$, so $\mu = e^{\ln x} = x$ and $\sigma = \mu\beta = x\cdot x^{-2} = 1/x$. The problem is regular: $p, p', \sigma, q$ are continuous and $p, \sigma > 0$ on the closed interval. Method: Notes09-12-Nov.pdf (Sturm-Liouville section; page to be confirmed); Haberman, Sec. 5.3 and the Rayleigh quotient discussion that follows it.

## Positivity via the Rayleigh Quotient

Let $\phi$ be a real eigenfunction (self-adjointness of the regular problem guarantees real eigenvalues and real eigenfunctions). Multiply $(x\phi')' + \frac\lambda x\phi = 0$ by $\phi$ and integrate over $[1,2]$:
$$\int_1^2\phi\,(x\phi')'\,dx + \lambda\int_1^2\frac{\phi^2}{x}\,dx = 0.$$

Integrate the first term by parts, $u = \phi$, $dv = (x\phi')'\,dx$, $du = \phi'\,dx$, $v = x\phi'$, and apply Barrow's rule to the boundary term:
$$\int_1^2\phi\,(x\phi')'\,dx = \Big[x\,\phi\,\phi'\Big]_1^2 - \int_1^2x\,(\phi')^2\,dx = 2\phi(2)\phi'(2) - 1\cdot\phi(1)\phi'(1) - \int_1^2x(\phi')^2dx.$$
Because $\phi(1) = \phi(2) = 0$, the boundary term is $0 - 0 = 0$. Hence
$$\boxed{\lambda = \frac{\displaystyle\int_1^2x\,(\phi')^2\,dx}{\displaystyle\int_1^2\frac{\phi^2}{x}\,dx}\ \ge\ 0.}$$
The denominator is positive for $\phi \not\equiv 0$ (the integrand $\phi^2/x$ is continuous and non-negative, and $1/x > 0$), and the numerator is $\ge 0$ because $x > 0$. So $\lambda \ge 0$.

> [!warning] $\lambda = 0$ is not an eigenvalue
> If $\lambda = 0$ then the numerator vanishes: $\int_1^2x(\phi')^2dx = 0$. The integrand is continuous, non-negative and $x \ge 1 > 0$, so $(\phi')^2 \equiv 0$, i.e. $\phi' \equiv 0$ and $\phi \equiv c$. Then $\phi(1) = c = 0$, so $\phi \equiv 0$. Direct check: for $\lambda = 0$ the equation $(x\phi')' = 0$ gives $x\phi' = c_1$, $\phi = c_1\ln x + c_2$; $\phi(1) = c_2 = 0$ and $\phi(2) = c_1\ln2 = 0$ gives $c_1 = 0$. Only the trivial solution, so $\lambda = 0$ is not an eigenvalue and in fact $\lambda > 0$ strictly.

## Eigenvalue Cases (Negative, Zero, Positive)

Solve with the Euler substitution $t = \ln x$, i.e. $x = e^{t}$, $t \in [0, \ln2]$. Write $\phi(x) = \Phi(t(x))$.

- Chain rule: $\phi' = \Phi'(t)\dfrac{dt}{dx} = \dfrac{\Phi'}{x}$.
- Product rule and chain rule again: $\phi'' = \dfrac{d}{dx}\left(\dfrac{\Phi'}{x}\right) = -\dfrac{\Phi'}{x^2} + \dfrac1x\Phi''\dfrac1x = \dfrac{\Phi'' - \Phi'}{x^2}$.
- Hence $x^2\phi'' = \Phi'' - \Phi'$ and $x\phi' = \Phi'$, so $x^2\phi'' + x\phi' + \lambda\phi = \Phi'' - \Phi' + \Phi' + \lambda\Phi = \Phi'' + \lambda\Phi$.

The problem becomes the constant-coefficient one
$$\Phi''(t) + \lambda\Phi(t) = 0,\qquad \Phi(0) = \Phi(\ln2) = 0$$
(since $t(1) = \ln1 = 0$ and $t(2) = \ln2$). This is Exercise 1(i) on an interval of length $L = \ln2$. All three signs, for completeness (item 2 already excludes $\lambda < 0$ and $\lambda = 0$ through the quotient):

- $\lambda < 0$, $\lambda = -\mu^2$: $\Phi = A\cosh\mu t + B\sinh\mu t$, $\Phi(0) = A = 0$, $\Phi(\ln2) = B\sinh(\mu\ln2) = 0$ with $\sinh(\mu\ln2) > 0$, so $B = 0$. Trivial.
- $\lambda = 0$: $\Phi = A + Bt$, $A = 0$, $B\ln2 = 0$. Trivial.
- $\lambda = \mu^2 > 0$: $\Phi = A\cos\mu t + B\sin\mu t$, $A = 0$, $B\sin(\mu\ln2) = 0$, so $\mu\ln2 = n\pi$, $\mu = \dfrac{n\pi}{\ln2}$, $n = 1, 2, \dots$

> [!result] Eigenvalues and eigenfunctions
> $$\lambda_n = \left(\frac{n\pi}{\ln2}\right)^2,\qquad \phi_n(x) = \sin\!\left(\frac{n\pi\ln x}{\ln2}\right),\qquad n = 1, 2, 3, \dots$$
> All $\lambda_n > 0$, so $\lambda = 0$ is not an eigenvalue, consistent with the Rayleigh argument.

## Eigenfunctions and Checks

- Boundary conditions: $\phi_n(1) = \sin(n\pi\cdot 0) = \sin0 = 0$ and $\phi_n(2) = \sin(n\pi\ln2/\ln2) = \sin n\pi = 0$ ✓.
- Direct ODE check (chain rule): $\phi_n' = \dfrac{n\pi}{x\ln2}\cos\!\left(\dfrac{n\pi\ln x}{\ln2}\right)$, and $(x\phi_n')' = \dfrac{d}{dx}\left[\dfrac{n\pi}{\ln2}\cos\!\left(\dfrac{n\pi\ln x}{\ln2}\right)\right] = -\left(\dfrac{n\pi}{\ln2}\right)^2\dfrac1x\sin\!\left(\dfrac{n\pi\ln x}{\ln2}\right)$, so $(x\phi_n')' + \dfrac{\lambda_n}{x}\phi_n = 0$ ✓.
- Rayleigh quotient value: $\int_1^2x(\phi_n')^2dx = \left(\dfrac{n\pi}{\ln2}\right)^2\int_1^2\dfrac1x\cos^2(\dots)dx$ and $\int_1^2\dfrac{\phi_n^2}{x}dx = \int_1^2\dfrac1x\sin^2(\dots)dx$. With $t = \ln x$, $dt = dx/x$: both integrals equal $\int_0^{\ln2}\cos^2$ or $\sin^2\left(\tfrac{n\pi t}{\ln2}\right)dt = \dfrac{\ln2}{2}$, so the quotient is $\left(\dfrac{n\pi}{\ln2}\right)^2 = \lambda_n$ ✓.
- Orthogonality with weight $\sigma(x) = 1/x$: for $n \ne m$, with $t = \ln x$,
$$\int_1^2\frac1x\sin\!\left(\frac{n\pi\ln x}{\ln2}\right)\sin\!\left(\frac{m\pi\ln x}{\ln2}\right)dx = \int_0^{\ln2}\sin\frac{n\pi t}{\ln2}\sin\frac{m\pi t}{\ln2}\,dt = \frac{\ln2}{2}\delta_{nm}.$$
Barrow check for $n \ne m$: $\tfrac12\left[\dfrac{\ln2\,\sin((n-m)\pi t/\ln2)}{(n-m)\pi} - \dfrac{\ln2\,\sin((n+m)\pi t/\ln2)}{(n+m)\pi}\right]_0^{\ln2} = 0$ since $\sin(k\pi) = 0$.
- Dimensions: $x$ is a non-dimensional (scaled) coordinate, so $\ln x$ is well defined and $\lambda$ is dimensionless. Limiting case: on an interval $[1, b]$ the same steps give $\lambda_n = (n\pi/\ln b)^2$, which grows without bound as $b \to 1^+$ (a shrinking interval forces large eigenvalues, as for $\phi'' + \lambda\phi = 0$ on a short interval).
