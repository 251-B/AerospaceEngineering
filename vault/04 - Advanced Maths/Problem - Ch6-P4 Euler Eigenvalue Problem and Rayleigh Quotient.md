---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 4"
dificultad: media
id: "e4"
pill: "Euler Equation • Rayleigh Quotient • Logarithmic Modes"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.4: Euler Eigenvalue Problem and Rayleigh Quotient

> Official exercise 4 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Consider the eigenvalue problem $x^2\phi''(x) + x\phi'(x) + \lambda\phi(x) = 0$ on the interval $[1, 2]$, with boundary conditions $\phi(1) = \phi(2) = 0$.

1. Show that multiplying by $1/x$ puts this equation into Sturm–Liouville form.
2. Show that $\lambda \ge 0$, and determine all possible eigenvalues. Is $\lambda = 0$ an eigenvalue?
3. What are the eigenfunctions?

## Classification of the problem

This is a **Cauchy–Euler eigenvalue problem** on $[1, 2]$ with homogeneous Dirichlet boundary conditions $\phi(1) = \phi(2) = 0$ (Haberman, Sec. 5.3 and 5.6). Because the interval $[1, 2]$ does not contain the singular point $x = 0$, dividing by $x$ yields a **regular Sturm-Liouville problem** with strictly positive $p(x) = x$ and $\sigma(x) = 1/x$.

## Method

We proceed in the three steps requested by the statement:

1. Multiply the ODE by $1/x$ and group the derivative terms into $[p(x)\phi'(x)]'$ to identify $p(x)$, $\sigma(x)$, and $q(x)$.
2. Multiply the Sturm-Liouville equation by $\phi(x)$, integrate over $[1, 2]$, and integrate by parts explicitly to obtain the **Rayleigh quotient** and prove $\lambda \ge 0$. Then apply the Euler change of variable $x = e^s$ ($s = \ln x$) using the chain rule explicitly to reduce the ODE to constant coefficients on $[0, \ln 2]$, and examine both $\lambda = 0$ and $\lambda > 0$.
3. Transform the resulting trigonometric modes in $s$ back to $x$ via $s = \ln x$.

## Part 1: Reduction to Sturm-Liouville form

Since $x \in [1, 2]$, we have $x \ge 1 > 0$, so multiplying the ODE by $1/x$ is valid everywhere on $[1, 2]$:

$$\frac{1}{x}\bigl[x^2\phi''(x) + x\phi'(x) + \lambda\phi(x)\bigr] = x\phi''(x) + \phi'(x) + \frac{\lambda}{x}\phi(x) = 0.$$

By the product rule, the first two terms collapse into a single derivative:

$$[x\phi'(x)]' = 1\cdot\phi'(x) + x\phi''(x) = x\phi''(x) + \phi'(x).$$

Hence the equation takes the canonical Sturm-Liouville form $[p(x)\phi'(x)]' + [\lambda\sigma(x) + q(x)]\phi(x) = 0$:

$$[x\phi'(x)]' + \frac{\lambda}{x}\phi(x) = 0, \qquad 1 < x < 2,$$

with coefficients:

$$p(x) = x > 0, \qquad \sigma(x) = \frac{1}{x} > 0, \qquad q(x) = 0.$$

This agrees with the integrating-factor formula of [[Problem - Ch6-P3 Integrating Factor for Sturm-Liouville Form]].

## Part 2: Non-negativity via the Rayleigh quotient and eigenvalues

### Proof that $\lambda \ge 0$ via the Rayleigh quotient

To derive the Rayleigh quotient, we multiply the Sturm-Liouville equation $[x\phi'(x)]' + \frac{\lambda}{x}\phi(x) = 0$ by an eigenfunction $\phi(x) \not\equiv 0$ and integrate from $x = 1$ to $x = 2$:

$$\int_1^2 \phi(x)[x\phi'(x)]'\,dx + \lambda\int_1^2 \frac{[\phi(x)]^2}{x}\,dx = 0.$$

We evaluate the first integral by **integration by parts** with the explicit choice:

$$u = \phi(x), \qquad dv = [x\phi'(x)]'\,dx \implies du = \phi'(x)\,dx, \qquad v = x\phi'(x).$$

Applying $\int_1^2 u\,dv = [uv]_1^2 - \int_1^2 v\,du$ and Barrow's rule $[F]_1^2 = F(2) - F(1)$ gives:

$$\int_1^2 \phi(x)[x\phi'(x)]'\,dx = \bigl[x\phi(x)\phi'(x)\bigr]_1^2 - \int_1^2 x[\phi'(x)]^2\,dx = \bigl(2\phi(2)\phi'(2) - 1\cdot\phi(1)\phi'(1)\bigr) - \int_1^2 x[\phi'(x)]^2\,dx.$$

Because the boundary conditions give $\phi(1) = 0$ and $\phi(2) = 0$, the boundary term vanishes identically:

$$2\phi(2)\phi'(2) - \phi(1)\phi'(1) = 2(0)\phi'(2) - (0)\phi'(1) = 0.$$

Substituting this back into the integrated equation gives:

$$-\int_1^2 x[\phi'(x)]^2\,dx + \lambda\int_1^2 \frac{[\phi(x)]^2}{x}\,dx = 0.$$

Since $\phi(x) \not\equiv 0$ is continuous on $[1, 2]$ and $1/x > 0$ on $[1, 2]$, the denominator integral $\int_1^2 \frac{[\phi(x)]^2}{x}\,dx$ is strictly positive. Solving for $\lambda$ yields the **Rayleigh quotient**:

$$\lambda = \frac{\displaystyle\int_1^2 x[\phi'(x)]^2\,dx}{\displaystyle\int_1^2 \frac{[\phi(x)]^2}{x}\,dx}.$$

On $[1, 2]$, we have $x > 0$ and $[\phi'(x)]^2 \ge 0$, so the numerator is $\ge 0$ while the denominator is $> 0$. Therefore:

$$\lambda \ge 0.$$

### Reduction to constant coefficients via $x = e^s$

To solve the Euler equation explicitly, we introduce the standard logarithmic change of independent variable:

$$x = e^s \iff s = \ln x, \qquad \frac{ds}{dx} = \frac{1}{x}.$$

As $x$ runs over $[1, 2]$, the new variable $s = \ln x$ runs over $[\ln 1, \ln 2] = [0, \ln 2]$. Writing $\Phi(s) = \phi(e^s)$ (and denoting derivatives with respect to $s$ by subscripts $\Phi_s, \Phi_{ss}$), we compute the first derivative by the chain rule:

$$\phi'(x) = \frac{d\phi}{dx} = \frac{d\Phi}{ds}\frac{ds}{dx} = \frac{1}{x}\Phi_s(s).$$

Next, we compute the second derivative using the product rule and the chain rule:

$$\phi''(x) = \frac{d}{dx}\left(\frac{1}{x}\Phi_s(s)\right) = -\frac{1}{x^2}\Phi_s(s) + \frac{1}{x}\frac{d\Phi_s}{ds}\frac{ds}{dx} = -\frac{1}{x^2}\Phi_s(s) + \frac{1}{x^2}\Phi_{ss}(s).$$

We substitute these expressions into $x^2\phi''(x) + x\phi'(x) + \lambda\phi(x) = 0$:

$$x^2\left(-\frac{1}{x^2}\Phi_s + \frac{1}{x^2}\Phi_{ss}\right) + x\left(\frac{1}{x}\Phi_s\right) + \lambda\Phi = (-\Phi_s + \Phi_{ss}) + \Phi_s + \lambda\Phi = 0.$$

The first-derivative terms cancel identically, leaving the standard Dirichlet problem on $[0, \ln 2]$:

$$\Phi_{ss}(s) + \lambda\Phi(s) = 0, \qquad 0 < s < \ln 2, \qquad \Phi(0) = \Phi(\ln 2) = 0.$$

Since we already proved $\lambda \ge 0$, we only need to analyse $\lambda = 0$ and $\lambda > 0$.

### Case $\lambda = 0$

When $\lambda = 0$, the transformed ODE is $\Phi_{ss}(s) = 0$, whose general solution is $\Phi(s) = A + Bs$. Applying the boundary conditions:

$$\Phi(0) = A = 0, \qquad \Phi(\ln 2) = B\ln 2 = 0.$$

Since $\ln 2 \neq 0$, this forces $B = 0$, so $\Phi(s) \equiv 0$ (and $\phi(x) \equiv 0$). Therefore **$\lambda = 0$ is not an eigenvalue**.

*(Remark: This also follows directly from the Rayleigh quotient. If $\lambda = 0$, then $\int_1^2 x[\phi'(x)]^2\,dx = 0$; since $x[\phi'(x)]^2 \ge 0$ is continuous, $\phi'(x) \equiv 0$, so $\phi(x)$ is constant, and $\phi(1) = 0$ forces $\phi(x) \equiv 0$.)*

### Case $\lambda > 0$

Set $\lambda = \mu^2$ with $\mu > 0$. The characteristic equation $r^2 + \mu^2 = 0$ gives $r = \pm i\mu$, so the general solution is:

$$\Phi(s) = A\cos(\mu s) + B\sin(\mu s).$$

Applying the left boundary condition $\Phi(0) = 0$ gives $A = 0$, leaving $\Phi(s) = B\sin(\mu s)$. Applying the right boundary condition $\Phi(\ln 2) = 0$ yields:

$$\Phi(\ln 2) = B\sin(\mu\ln 2) = 0.$$

For a non-trivial solution ($B \neq 0$), we require $\sin(\mu\ln 2) = 0$. Since $\mu > 0$ and $\ln 2 > 0$, the positive solutions are:

$$\mu_n\ln 2 = n\pi \implies \mu_n = \frac{n\pi}{\ln 2}, \qquad n = 1, 2, 3, \dots$$

Squaring $\mu_n$ gives all eigenvalues of the problem:

$$\lambda_n = \left(\frac{n\pi}{\ln 2}\right)^2, \qquad n = 1, 2, 3, \dots$$

## Part 3: Eigenfunctions

Setting $B = 1$ in $\Phi_n(s) = B\sin(\mu_n s)$ and substituting back $s = \ln x$ gives the eigenfunctions in the original variable $x$:

$$\phi_n(x) = \sin\!\left(\frac{n\pi\ln x}{\ln 2}\right), \qquad n = 1, 2, 3, \dots$$

## Eigenvalues and eigenfunctions

| Quantity | Expression | Index range |
| :--- | :--- | :--- |
| Sturm-Liouville coefficients | $p(x) = x$, $\sigma(x) = 1/x$, $q(x) = 0$ | $x \in [1, 2]$ |
| Eigenvalues | $\lambda_n = \left(\dfrac{n\pi}{\ln 2}\right)^2$ | $n = 1, 2, 3, \dots$ ($\lambda = 0$ is not an eigenvalue) |
| Eigenfunctions | $\phi_n(x) = \sin\!\left(\dfrac{n\pi\ln x}{\ln 2}\right)$ | $n = 1, 2, 3, \dots$ |

## Answers and checks

**Direct substitution check.** Let $\mu_n = \frac{n\pi}{\ln 2}$ so that $\phi_n(x) = \sin(\mu_n\ln x)$ and $\lambda_n = \mu_n^2$. Differentiating twice with respect to $x$ by the chain and product rules:

$$\phi_n'(x) = \cos(\mu_n\ln x)\cdot\frac{\mu_n}{x} = \frac{\mu_n}{x}\cos(\mu_n\ln x),$$

$$\phi_n''(x) = -\frac{\mu_n}{x^2}\cos(\mu_n\ln x) - \frac{\mu_n^2}{x^2}\sin(\mu_n\ln x).$$

Substituting into $x^2\phi_n''(x) + x\phi_n'(x) + \lambda_n\phi_n(x)$:

$$x^2\left(-\frac{\mu_n}{x^2}\cos(\mu_n\ln x) - \frac{\mu_n^2}{x^2}\sin(\mu_n\ln x)\right) + x\left(\frac{\mu_n}{x}\cos(\mu_n\ln x)\right) + \mu_n^2\sin(\mu_n\ln x)$$

$$= \bigl(-\mu_n + \mu_n\bigr)\cos(\mu_n\ln x) + \bigl(-\mu_n^2 + \mu_n^2\bigr)\sin(\mu_n\ln x) = 0.$$

**Boundary-condition check.**

- At $x = 1$: $\ln 1 = 0 \implies \phi_n(1) = \sin(0) = 0$.
- At $x = 2$: $\phi_n(2) = \sin\!\left(\frac{n\pi\ln 2}{\ln 2}\right) = \sin(n\pi) = 0$.

**Dimensional check.** In $x^2\phi'' + x\phi' + \lambda\phi = 0$, every term $x^2\phi''$ and $x\phi'$ has the same dimensions as $\phi$ regardless of the units of $x$, so $\lambda$ is dimensionless; likewise $\frac{\ln x}{\ln 2}$ is dimensionless.

> [!result] Key results
> 1. **Sturm-Liouville form:** Multiplying by $1/x$ yields $[x\phi'(x)]' + \frac{\lambda}{x}\phi(x) = 0$, with $p(x) = x > 0$, $\sigma(x) = 1/x > 0$, and $q(x) = 0$.
> 2. **Non-negativity and eigenvalues:** The Rayleigh quotient gives $\lambda = \frac{\int_1^2 x[\phi'(x)]^2\,dx}{\int_1^2 [\phi(x)]^2/x\,dx} \ge 0$. **$\lambda = 0$ is not an eigenvalue.** All eigenvalues are strictly positive:
>    $$\lambda_n = \left(\frac{n\pi}{\ln 2}\right)^2, \qquad n = 1, 2, 3, \dots$$
> 3. **Eigenfunctions:**
>    $$\phi_n(x) = \sin\!\left(\frac{n\pi\ln x}{\ln 2}\right), \qquad n = 1, 2, 3, \dots$$
