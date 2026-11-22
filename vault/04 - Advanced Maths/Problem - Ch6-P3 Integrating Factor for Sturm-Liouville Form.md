---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 3"
dificultad: media
id: "e3"
pill: "Integrating Factor • Self-Adjoint Form"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.3: Integrating Factor for Sturm-Liouville Form

> Official exercise 3 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Consider the ODE $\phi''(x) + \alpha(x)\phi'(x) + [\lambda\beta(x) + \gamma(x)]\phi(x) = 0$. Find an integrating factor $\mu(x)$ in terms of the coefficients of the ODE $\alpha(x)$, $\beta(x)$ and $\gamma(x)$, such that the equation can be brought into Sturm-Liouville form, namely,

$$[p(x)\phi'(x)]' + [\lambda\sigma(x) + q(x)]\phi(x) = 0.$$

## Classification of the problem

This is a **structural reduction problem** for general second-order linear homogeneous ODEs with a spectral parameter $\lambda$ (Haberman, Sec. 5.3). Whenever $\alpha(x)$ is continuous on an interval $[a, b]$, multiplying the equation by a suitable strictly positive integrating factor $\mu(x)$ converts the non-self-adjoint differential operator $\frac{d^2}{dx^2} + \alpha(x)\frac{d}{dx}$ into the **self-adjoint Sturm-Liouville derivative** $\frac{d}{dx}\bigl(p(x)\frac{d}{dx}\bigr)$, which guarantees orthogonality of eigenfunctions with respect to the weight $\sigma(x)$ and enables the Rayleigh quotient.

## Method

We multiply the given ODE by an unknown strictly positive function $\mu(x) > 0$, expand the target Sturm-Liouville derivative $[p(x)\phi'(x)]'$ by the product rule, and match the coefficients of $\phi''(x)$, $\phi'(x)$, and $\phi(x)$. Matching the derivative terms yields a separable first-order ODE for $\mu(x)$, which we integrate explicitly to express $\mu(x)$, $p(x)$, $\sigma(x)$, and $q(x)$ in terms of $\alpha(x)$, $\beta(x)$, and $\gamma(x)$.

## Derivation of the integrating factor

First, we multiply the given ODE throughout by an unknown integrating factor $\mu(x) > 0$:

$$\mu(x)\phi''(x) + \mu(x)\alpha(x)\phi'(x) + \bigl[\lambda\mu(x)\beta(x) + \mu(x)\gamma(x)\bigr]\phi(x) = 0.$$

Next, we expand the derivative term $[p(x)\phi'(x)]'$ in the target Sturm-Liouville equation using the product rule:

$$[p(x)\phi'(x)]' + [\lambda\sigma(x) + q(x)]\phi(x) = p(x)\phi''(x) + p'(x)\phi'(x) + [\lambda\sigma(x) + q(x)]\phi(x) = 0.$$

Comparing the coefficients of $\phi''(x)$ and $\phi'(x)$ in the two equations gives two conditions:

$$p(x) = \mu(x), \qquad p'(x) = \mu(x)\alpha(x).$$

Substituting $p(x) = \mu(x)$ into the second condition yields a first-order separable ODE for $\mu(x)$:

$$\mu'(x) = \mu(x)\alpha(x).$$

Because we require $\mu(x) \neq 0$ (indeed $\mu(x) > 0$ so that multiplying by $\mu(x)$ does not introduce spurious solutions or change the sign of $p(x)$), we divide both sides by $\mu(x)$ and separate variables:

$$\frac{\mu'(x)}{\mu(x)} = \alpha(x) \implies \frac{d\mu}{\mu} = \alpha(x)\,dx.$$

Integrating both sides with respect to $x$ gives:

$$\ln|\mu(x)| = \int \alpha(x)\,dx + C,$$

where $C \in \mathbb{R}$ is an arbitrary constant of integration. Exponentiating both sides yields:

$$\mu(x) = K\exp\!\left(\int \alpha(x)\,dx\right), \qquad K = \pm e^C \neq 0.$$

Because any non-zero constant multiple of a Sturm-Liouville equation is equivalent, we choose $K = 1$ (i.e., $C = 0$) to obtain a strictly positive canonical integrating factor:

$$\mu(x) = \exp\!\left(\int \alpha(x)\,dx\right) > 0.$$

Notice that $\mu(x)$ depends **only on $\alpha(x)$** and is completely independent of $\beta(x)$ and $\gamma(x)$.

## Sturm-Liouville coefficients

Comparing the remaining terms of the multiplied equation with $[p(x)\phi'(x)]' + [\lambda\sigma(x) + q(x)]\phi(x) = 0$ immediately identifies all three Sturm-Liouville coefficients:

$$p(x) = \mu(x) = \exp\!\left(\int \alpha(x)\,dx\right),$$

$$\sigma(x) = \mu(x)\beta(x) = \beta(x)\exp\!\left(\int \alpha(x)\,dx\right),$$

$$q(x) = \mu(x)\gamma(x) = \gamma(x)\exp\!\left(\int \alpha(x)\,dx\right).$$

If the original ODE is regular on $[a, b]$ with $\beta(x) > 0$, then both $p(x) > 0$ and $\sigma(x) > 0$ automatically hold on $[a, b]$.

## Answers and checks

**Product-rule verification.** Differentiating $p(x)\phi'(x) = \mu(x)\phi'(x)$ with $\mu(x) = \exp\!\left(\int \alpha(x)\,dx\right)$ using the chain rule $\mu'(x) = \alpha(x)\mu(x)$ gives:

$$[\mu(x)\phi'(x)]' = \mu(x)\phi''(x) + \mu'(x)\phi'(x) = \mu(x)\phi''(x) + \mu(x)\alpha(x)\phi'(x) = \mu(x)\bigl[\phi''(x) + \alpha(x)\phi'(x)\bigr].$$

Adding $\bigl[\lambda\mu(x)\beta(x) + \mu(x)\gamma(x)\bigr]\phi(x)$ recovers $\mu(x)$ times the original ODE identically.

**Application check 1 (Exercise 6.2(i)).** For $y'' + y' + (1 + \lambda)y = 0$, we have $\alpha(x) = 1$, $\beta(x) = 1$, $\gamma(x) = 1$. The formula gives:

$$\mu(x) = \exp\!\left(\int 1\,dx\right) = e^x,$$

yielding the Sturm-Liouville form $[e^x y'(x)]' + (\lambda e^x + e^x)y(x) = 0$, with $p(x) = e^x$, $\sigma(x) = e^x$, and $q(x) = e^x$.

**Application check 2 (Exercise 6.4).** For the Euler equation $x^2\phi'' + x\phi' + \lambda\phi = 0$ on $[1, 2]$, we first divide by $x^2$ to put it into monic form $\phi'' + \frac{1}{x}\phi' + \frac{\lambda}{x^2}\phi = 0$, giving $\alpha(x) = \frac{1}{x}$, $\beta(x) = \frac{1}{x^2}$, and $\gamma(x) = 0$. The formula gives:

$$\mu(x) = \exp\!\left(\int \frac{1}{x}\,dx\right) = e^{\ln x} = x \quad (x > 0).$$

Multiplying the monic equation by $x$ (which is equivalent to multiplying the original Euler equation by $\frac{x}{x^2} = \frac{1}{x}$) yields $[x\phi'(x)]' + \frac{\lambda}{x}\phi(x) = 0$, matching [[Problem - Ch6-P4 Euler Eigenvalue Problem and Rayleigh Quotient]].

**Dimensional check.** Since $\alpha(x)\phi'(x)$ has the same dimensions as $\phi''(x)$, $[\alpha] = [x]^{-1}$, so the integral $\int \alpha(x)\,dx$ is dimensionless and $\mu(x) = \exp\!\left(\int \alpha(x)\,dx\right)$ is dimensionless as required.

> [!result] Key results
> - **Integrating factor:** $\mu(x) = \exp\!\left(\int \alpha(x)\,dx\right)$ (depends only on $\alpha(x)$, strictly positive).
> - **Sturm-Liouville form:** $[p(x)\phi'(x)]' + [\lambda\sigma(x) + q(x)]\phi(x) = 0$ with
>   $$p(x) = \mu(x), \qquad \sigma(x) = \mu(x)\beta(x), \qquad q(x) = \mu(x)\gamma(x).$$
