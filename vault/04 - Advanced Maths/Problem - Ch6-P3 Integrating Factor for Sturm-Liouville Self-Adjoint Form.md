---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 3"
dificultad: media
id: "e3"
pill: "Integrating factor to self-adjoint form"
tags:
  - problema-resuelto
  - sturm-liouville
  - integrating-factor
  - self-adjoint
---

# Problem 6.3: Integrating Factor for Sturm-Liouville Self-Adjoint Form

> Official exercise 3 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Consider the ODE $\phi''(x) + \alpha(x)\phi'(x) + [\lambda\beta(x) + \gamma(x)]\phi(x) = 0$. Find an integrating factor $\mu(x)$ in terms of the coefficients of the ODE $\alpha(x)$, $\beta(x)$ and $\gamma(x)$, such that the equation can be brought into Sturm-Liouville form, namely, $[p(x)\phi'(x)]' + [\lambda\sigma(x) + q(x)]\phi(x) = 0$.

## Formulation and Sturm-Liouville Structure

Goal: find $\mu(x) > 0$ such that $\mu\cdot\left(\phi'' + \alpha\phi' + [\lambda\beta+\gamma]\phi\right)$ has the form $[p\phi']' + [\lambda\sigma + q]\phi$. Only the derivative terms can obstruct this, since the term in $\phi$ is just rescaled. Method: Notes09-12-Nov.pdf (Sturm-Liouville section; page to be confirmed); Haberman, Sec. 5.3.

## Derivation of the Integrating Factor

Multiply the ODE by $\mu(x)$:
$$\mu\phi'' + \mu\alpha\phi' + \mu[\lambda\beta + \gamma]\phi = 0.$$

Expand the target derivative with the product rule, $[\mu\phi']' = \mu'\phi' + \mu\phi''$. The first two terms above equal $[\mu\phi']'$ if and only if the coefficients of $\phi'$ agree:
$$\mu\alpha = \mu' \iff \frac{\mu'}{\mu} = \alpha.$$

Since $\mu > 0$, $\dfrac{\mu'}{\mu} = \dfrac{d}{dx}\ln\mu$ (chain rule), and integrating,
$$\ln\mu(x) = \int\alpha(x)\,dx + C \quad\Longrightarrow\quad \mu(x) = K\exp\left(\int\alpha(x)\,dx\right),\ K = e^{C} > 0.$$
The constant $K$ multiplies the whole equation by a number, so it is irrelevant: take $K = 1$. With limits, $\mu(x) = \exp\left(\int_{x_0}^{x}\alpha(s)\,ds\right)$ for any base point $x_0$ (Barrow's rule gives $\int_{x_0}^x\alpha = A(x) - A(x_0)$, again a constant factor).

> [!result] Integrating factor and coefficients
> $$\mu(x) = \exp\left(\int\alpha(x)\,dx\right) > 0,\qquad p(x) = \mu(x),\quad \sigma(x) = \mu(x)\beta(x),\quad q(x) = \mu(x)\gamma(x).$$

Product-rule check, written out. With $\mu' = \alpha\mu$:
$$[\mu\phi']' = \mu'\phi' + \mu\phi'' = \alpha\mu\phi' + \mu\phi'' = \mu(\phi'' + \alpha\phi'),$$
so $\mu(\phi'' + \alpha\phi') + \mu[\lambda\beta + \gamma]\phi = [\mu\phi']' + [\lambda\,\mu\beta + \mu\gamma]\phi = 0$, which is the required form with the identified $p, \sigma, q$ ✓.

> [!info] Why $\mu$ depends only on $\alpha$
> The equation $\mu' = \alpha\mu$ comes from matching the coefficient of $\phi'$. The terms $\lambda\beta\phi$ and $\gamma\phi$ contain no derivative of $\phi$, so they never enter a product-rule expansion: multiplying by any $\mu$ just rescales them into $\sigma$ and $q$. Therefore $\beta$ and $\gamma$ cannot change $\mu$; they only pass through to $\sigma = \mu\beta$ and $q = \mu\gamma$.

## Conditions for a Regular Sturm-Liouville Form

- $p = \mu = e^{\int\alpha} > 0$ automatically, and $p \in C^1$ whenever $\alpha$ is continuous. ($p' = \alpha p$.)
- $\sigma = \mu\beta > 0 \iff \beta > 0$, because $\mu > 0$. So the weight is positive exactly when the coefficient of $\lambda$ is positive. If $\beta < 0$ (as in Exercise 2(ii), where $\beta = -1$), the weight is negative and the eigenvalues have the opposite sign to the standard expectation; replacing $\lambda$ by $-\lambda$ restores $\sigma > 0$.
- $q = \mu\gamma$ is continuous when $\gamma$ is; its sign has no effect on regularity (it only shifts the spectrum).
- On a finite closed interval with $p, \sigma > 0$ and $p, p', q, \sigma$ continuous the problem is regular, and orthogonality of eigenfunctions holds with weight $\sigma$: $\int_a^b\sigma\phi_n\phi_m\,dx = 0$ for $\lambda_n \ne \lambda_m$.

## Verification on Exercise 2

All three problems of [[Problem - Ch6-P2 Non-Standard Constant-Coefficient Eigenvalue Problems]] have constant coefficients, so $\int\alpha\,dx = \alpha x$ and $\mu = e^{\alpha x}$:

| Part | $\alpha$ | $\mu = e^{\int\alpha}$ | $[\mu y']'$ expanded | $\sigma = \mu\beta$ | $q = \mu\gamma$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2(i) | $1$ | $e^{x}$ | $e^{x}(y'' + y')$ | $e^{x}$ | $e^{x}$ |
| 2(ii) | $2$ | $e^{2x}$ | $e^{2x}(y'' + 2y')$ | $-e^{2x}$ | $e^{2x}$ |
| 2(iii) | $-3$ | $e^{-3x}$ | $e^{-3x}(y'' - 3y')$ | $3e^{-3x}$ | $3e^{-3x}$ |

For instance in 2(iii): $[e^{-3x}y']' = -3e^{-3x}y' + e^{-3x}y'' = e^{-3x}(y'' - 3y')$ by the product and chain rules, so $[e^{-3x}y']' + [3\lambda e^{-3x} + 3e^{-3x}]y = e^{-3x}\{y'' - 3y' + 3(1+\lambda)y\} = 0$ ✓. The weights found here are the ones used for the orthogonality checks in Exercise 2.

## Equivalent Route: Liouville Shift

Substituting $\phi = e^{-\frac12\int\alpha}u$ removes the first-derivative term instead of rescaling the equation. Using $\phi' = e^{-\frac12\int\alpha}\left(u' - \tfrac\alpha2u\right)$ and $\phi'' = e^{-\frac12\int\alpha}\left(u'' - \alpha u' - \tfrac{\alpha'}{2}u + \tfrac{\alpha^2}{4}u\right)$ one obtains
$$u'' + \left[\lambda\beta + \gamma - \tfrac{\alpha'}{2} - \tfrac{\alpha^2}{4}\right]u = 0.$$
For constant $\alpha$ this is the classical constant-coefficient problem, which explains the shifts $\lambda + \tfrac34$ (2(i)), $-\lambda$ (2(ii)) and $3\lambda + \tfrac34$ (2(iii)).

## Answers and Checks

- Answer: $\mu(x) = \exp\left(\int\alpha(x)\,dx\right)$, $p = \mu$, $\sigma = \mu\beta$, $q = \mu\gamma$.
- Limiting case $\alpha = 0$: $\mu = 1$ and the equation is already self-adjoint (as in [[Problem - Ch6-P1 Sturm-Liouville Eigenvalues under Four Boundary Conditions]]).
- Limiting case Euler-Cauchy ($x^2\phi'' + x\phi' + \lambda\phi = 0$ divided by $x^2$): $\alpha = 1/x$, $\mu = e^{\ln x} = x$, $p = x$, $\sigma = x\cdot\dfrac{1}{x^2} = \dfrac1x$, matching [[Problem - Ch6-P4 Euler-Cauchy Eigenvalue Problem and Rayleigh Quotient]].
- Dimensions: $\mu$ is dimensionless (it is the exponential of $\int\alpha\,dx$, and $\alpha\,dx$ is dimensionless since $\alpha\phi'$ and $\phi''$ have the same dimension).
