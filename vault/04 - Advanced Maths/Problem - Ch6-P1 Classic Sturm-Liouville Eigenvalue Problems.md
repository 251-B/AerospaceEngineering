---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 1"
dificultad: media
id: "e1"
pill: "Dirichlet • Mixed • Neumann • Robin"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.1: Classic Sturm-Liouville Eigenvalue Problems

> Official exercise 1 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Determine the eigenvalues and eigenfunctions of the Sturm-Liouville problems obtained for the equation $\phi''(x) + \lambda\phi(x) = 0$ with $0 < x < 1$ and each of the following boundary conditions:

- (i) $\phi(0) = \phi(1) = 0$.
- (ii) $\phi(0) = \phi'(1) = 0$.
- (iii) $\phi'(0) = \phi'(1) = 0$.
- (iv) $\phi(0) = \phi'(1) + h\phi(1) = 0$, with $h > 0$.

## Classification of the problem

Each of the four boundary-value problems is a **regular Sturm-Liouville eigenvalue problem** on the finite interval $[0, 1]$, of the canonical self-adjoint form (Haberman, Sec. 2.3–2.4 and 5.8; `Notes09-12-Nov.pdf`, pp. 1–5):

$$[p(x)\phi'(x)]' + [\lambda\sigma(x) + q(x)]\phi(x) = 0, \qquad 0 < x < 1,$$

with constant coefficients $p(x) = 1 > 0$, $\sigma(x) = 1 > 0$, and $q(x) = 0$. The boundary conditions at the endpoints $x = 0$ and $x = 1$ are separated and homogeneous:

- (i) **Dirichlet–Dirichlet** (fixed value at both ends).
- (ii) **Mixed (Dirichlet–Neumann)** (fixed value at $x = 0$, zero flux at $x = 1$).
- (iii) **Neumann–Neumann** (zero flux at both ends).
- (iv) **Mixed (Dirichlet–Robin)** (fixed value at $x = 0$, Newton-cooling / elastic condition at $x = 1$ with $h > 0$).

A number $\lambda$ is an **eigenvalue** if and only if the boundary-value problem admits a **non-trivial** solution $\phi(x) \not\equiv 0$, called an **eigenfunction** (unique up to a non-zero multiplicative constant).

## Method

We solve the constant-coefficient linear homogeneous ODE $\phi''(x) + \lambda\phi(x) = 0$ by forming its characteristic equation $r^2 + \lambda = 0$. Because the form of the general solution depends on the sign of $\lambda$, we examine all three real regimes—$\lambda > 0$, $\lambda = 0$, and $\lambda < 0$—for each set of boundary conditions (i)–(iv) without assuming in advance that $\lambda \ge 0$. For the Robin condition in (iv), the eigenvalue condition is transcendental, so we locate its roots graphically and derive their large-$n$ asymptotic behaviour.

## Case λ > 0

To write the oscillatory general solution cleanly, we set $\lambda = \mu^2$ with $\mu > 0$.

Substituting $\phi(x) = e^{rx}$ into $\phi''(x) + \mu^2\phi(x) = 0$ gives the characteristic equation:

$$r^2 + \mu^2 = 0 \implies r = \pm i\mu.$$

Using Euler's formula, the real-valued general solution and its first derivative are:

$$\phi(x) = A\cos(\mu x) + B\sin(\mu x), \qquad \phi'(x) = -A\mu\sin(\mu x) + B\mu\cos(\mu x),$$

where $A, B \in \mathbb{R}$ are arbitrary constants. We now apply each pair of boundary conditions in turn.

### Part (i): Dirichlet–Dirichlet, $\phi(0) = \phi(1) = 0$

We first evaluate $\phi(x)$ at $x = 0$ to eliminate one constant:

$$\phi(0) = A\cos(0) + B\sin(0) = A = 0 \implies \phi(x) = B\sin(\mu x).$$

Next, we impose the boundary condition at $x = 1$:

$$\phi(1) = B\sin(\mu) = 0.$$

To obtain a non-trivial solution we must take $B \neq 0$, which forces $\sin(\mu) = 0$. Since $\mu > 0$, the roots are:

$$\mu_n = n\pi, \qquad n = 1, 2, 3, \dots$$

Squaring $\mu_n$ and setting $B = 1$ yields the positive eigenvalues and eigenfunctions for (i):

$$\lambda_n = (n\pi)^2, \qquad \phi_n(x) = \sin(n\pi x), \qquad n = 1, 2, 3, \dots$$

### Part (ii): Mixed (Dirichlet–Neumann), $\phi(0) = \phi'(1) = 0$

Applying the left boundary condition $\phi(0) = 0$ again eliminates $A$:

$$\phi(0) = A = 0 \implies \phi(x) = B\sin(\mu x), \qquad \phi'(x) = B\mu\cos(\mu x).$$

We now impose the right boundary condition $\phi'(1) = 0$:

$$\phi'(1) = B\mu\cos(\mu) = 0.$$

For a non-trivial solution we need $B \neq 0$, and we already have $\mu > 0$, so $\cos(\mu) = 0$. The positive zeros of the cosine function are odd multiples of $\frac{\pi}{2}$:

$$\mu_n = \left(n - \frac{1}{2}\right)\pi = \frac{(2n - 1)\pi}{2}, \qquad n = 1, 2, 3, \dots$$

Squaring $\mu_n$ and setting $B = 1$ gives the positive eigenvalues and eigenfunctions for (ii):

$$\lambda_n = \left[\left(n - \frac{1}{2}\right)\pi\right]^2, \qquad \phi_n(x) = \sin\!\left[\left(n - \frac{1}{2}\right)\pi x\right], \qquad n = 1, 2, 3, \dots$$

### Part (iii): Neumann–Neumann, $\phi'(0) = \phi'(1) = 0$

We first evaluate the derivative $\phi'(x)$ at $x = 0$:

$$\phi'(0) = -A\mu\sin(0) + B\mu\cos(0) = B\mu = 0.$$

Because $\mu > 0$, this forces $B = 0$, reducing the solution and its derivative to:

$$\phi(x) = A\cos(\mu x), \qquad \phi'(x) = -A\mu\sin(\mu x).$$

We now impose $\phi'(1) = 0$:

$$\phi'(1) = -A\mu\sin(\mu) = 0.$$

For a non-trivial solution we require $A \neq 0$; combined with $\mu > 0$, this gives $\sin(\mu) = 0$, hence $\mu_n = n\pi$ for $n = 1, 2, 3, \dots$. Setting $A = 1$ yields the positive eigenvalues and eigenfunctions for (iii):

$$\lambda_n = (n\pi)^2, \qquad \phi_n(x) = \cos(n\pi x), \qquad n = 1, 2, 3, \dots$$

### Part (iv): Dirichlet–Robin, $\phi(0) = \phi'(1) + h\phi(1) = 0$ ($h > 0$)

Imposing $\phi(0) = 0$ eliminates the cosine term:

$$\phi(0) = A = 0 \implies \phi(x) = B\sin(\mu x), \qquad \phi'(x) = B\mu\cos(\mu x).$$

Next, we substitute $\phi(1)$ and $\phi'(1)$ into the Robin boundary condition at $x = 1$:

$$\phi'(1) + h\phi(1) = B\mu\cos(\mu) + hB\sin(\mu) = B\bigl(\mu\cos\mu + h\sin\mu\bigr) = 0.$$

For a non-trivial solution ($B \neq 0$), $\mu > 0$ must satisfy:

$$\mu\cos\mu + h\sin\mu = 0.$$

Before dividing by $\cos\mu$, we verify that $\cos\mu \neq 0$: if $\cos\mu = 0$, then $\sin\mu = \pm 1$, and the equation would reduce to $\pm h = 0$, contradicting $h > 0$. Dividing through by $h\cos\mu$ gives the transcendental eigenvalue equation:

$$\tan\mu = -\frac{\mu}{h}, \qquad \mu > 0.$$

To locate all positive roots, we intersect the graph of $y = \tan\mu$ with the straight line $y = -\mu/h$ of negative slope $-1/h < 0$ (Haberman, Sec. 5.8).

![[attachments/AM-PS/ch6-e1-robin.svg]]
*Graphical solution of $\tan\mu = -\mu/h$ for $h = 1$: each vertical branch of $\tan\mu$ on $\bigl((n - \tfrac{1}{2})\pi, n\pi\bigr)$ intersects the line $y = -\mu/h$ at a unique root $\mu_n$.*

We check each interval of length $\pi/2$ for $\mu > 0$:

- On $(0, \frac{\pi}{2})$, $\tan\mu > 0$ while $-\mu/h < 0$, so there is **no root** in $(0, \frac{\pi}{2})$.
- On each interval $\bigl((n - \tfrac{1}{2})\pi, n\pi\bigr)$ ($n = 1, 2, 3, \dots$), $\tan\mu$ is continuous and strictly increasing from $-\infty$ to $0$, whereas $-\mu/h$ is strictly decreasing and strictly negative. By the Intermediate Value Theorem and monotonicity, there is **exactly one root** $\mu_n$ in each interval:

$$\left(n - \frac{1}{2}\right)\pi < \mu_n < n\pi, \qquad n = 1, 2, 3, \dots$$

- On each interval $\bigl(n\pi, (n + \tfrac{1}{2})\pi\bigr)$, $\tan\mu > 0$ while $-\mu/h < 0$, so no additional roots occur.

For the representative case $h = 1$, the first three positive roots are $\mu_1 \approx 2.0288$, $\mu_2 \approx 4.9132$, and $\mu_3 \approx 7.9787$.

To find the **large-$n$ asymptotic behaviour**, note that as $n \to \infty$, $-\mu_n/h \to -\infty$, so $\tan\mu_n \to -\infty$ and $\mu_n$ approaches the left vertical asymptote $\bigl(n - \tfrac{1}{2}\bigr)\pi$ from above. Writing $\mu_n = \bigl(n - \tfrac{1}{2}\bigr)\pi + \delta_n$ with $0 < \delta_n \ll 1$, we use the trigonometric identity $\tan\bigl((n - \tfrac{1}{2})\pi + \delta_n\bigr) = -\cot\delta_n$:

$$-\cot\delta_n = -\frac{\left(n - \tfrac{1}{2}\right)\pi + \delta_n}{h}.$$

Since $\cot\delta_n \approx \frac{1}{\delta_n}$ for small $\delta_n$, we obtain at leading order:

$$\frac{1}{\delta_n} \approx \frac{\left(n - \tfrac{1}{2}\right)\pi}{h} \implies \delta_n \approx \frac{h}{\left(n - \tfrac{1}{2}\right)\pi}.$$

Therefore, for large $n$:

$$\mu_n \approx \left(n - \frac{1}{2}\right)\pi + \frac{h}{\left(n - \tfrac{1}{2}\right)\pi}, \qquad \lambda_n = \mu_n^2 \approx \left[\left(n - \frac{1}{2}\right)\pi\right]^2.$$

Setting $B = 1$, the eigenfunctions for (iv) are $\phi_n(x) = \sin(\mu_n x)$ with $\lambda_n = \mu_n^2$.

## Case λ = 0

When $\lambda = 0$, the ODE simplifies to $\phi''(x) = 0$. Integrating twice with respect to $x$ gives the linear general solution and its derivative:

$$\phi'(x) = B, \qquad \phi(x) = A + Bx,$$

where $A, B \in \mathbb{R}$. We test all four sets of boundary conditions to see whether $\lambda = 0$ is an eigenvalue.

- **(i) $\phi(0) = \phi(1) = 0$:** $\phi(0) = A = 0$, and then $\phi(1) = 0 + B(1) = B = 0$. Thus $\phi(x) \equiv 0$, so **$\lambda = 0$ is not an eigenvalue**.
- **(ii) $\phi(0) = \phi'(1) = 0$:** $\phi(0) = A = 0$, and $\phi'(1) = B = 0$. Thus $\phi(x) \equiv 0$, so **$\lambda = 0$ is not an eigenvalue**.
- **(iii) $\phi'(0) = \phi'(1) = 0$:** $\phi'(0) = B = 0$ and $\phi'(1) = B = 0$ both hold when $B = 0$, leaving $A$ completely arbitrary. Thus $\phi(x) = A \not\equiv 0$ for any $A \neq 0$. Choosing $A = 1$, **$\lambda_0 = 0$ is an eigenvalue** with constant eigenfunction $\phi_0(x) = 1$.
- **(iv) $\phi(0) = \phi'(1) + h\phi(1) = 0$ ($h > 0$):** $\phi(0) = A = 0$ gives $\phi(x) = Bx$ and $\phi'(x) = B$. Substituting into the Robin condition at $x = 1$:

$$\phi'(1) + h\phi(1) = B + hB = B(1 + h) = 0.$$

Since $h > 0$, we have $1 + h > 1 \neq 0$, which forces $B = 0$. Hence $\phi(x) \equiv 0$, so **$\lambda = 0$ is not an eigenvalue**.

## Case λ < 0

To examine negative eigenvalues, we write $\lambda = -k^2$ with $k > 0$.

The ODE becomes $\phi''(x) - k^2\phi(x) = 0$, whose characteristic equation is $r^2 - k^2 = 0 \implies r = \pm k$. Expressing the general solution in hyperbolic form (which is algebraically equivalent to $C_1 e^{kx} + C_2 e^{-kx}$ and simplifies boundary evaluations at $x = 0$) gives:

$$\phi(x) = A\cosh(kx) + B\sinh(kx), \qquad \phi'(x) = Ak\sinh(kx) + Bk\cosh(kx).$$

We check all four boundary conditions using $\cosh(0) = 1$, $\sinh(0) = 0$, and the fact that $\sinh(k) > 0$ and $\cosh(k) > 1$ for all $k > 0$:

- **(i) $\phi(0) = \phi(1) = 0$:** $\phi(0) = A = 0 \implies \phi(1) = B\sinh(k) = 0$. Because $\sinh(k) > 0$, $B = 0$, giving only the trivial solution.
- **(ii) $\phi(0) = \phi'(1) = 0$:** $\phi(0) = A = 0 \implies \phi'(1) = Bk\cosh(k) = 0$. Because $k > 0$ and $\cosh(k) > 0$, $B = 0$, giving only the trivial solution.
- **(iii) $\phi'(0) = \phi'(1) = 0$:** $\phi'(0) = Bk = 0 \implies B = 0$. Then $\phi'(1) = Ak\sinh(k) = 0 \implies A = 0$, giving only the trivial solution.
- **(iv) $\phi(0) = \phi'(1) + h\phi(1) = 0$ ($h > 0$):** $\phi(0) = A = 0$, so $\phi(x) = B\sinh(kx)$ and $\phi'(x) = Bk\cosh(kx)$. Substituting into the Robin condition at $x = 1$:

$$\phi'(1) + h\phi(1) = B\bigl(k\cosh k + h\sinh k\bigr) = 0.$$

Since $k > 0$, $h > 0$, $\cosh k > 0$, and $\sinh k > 0$, the quantity $k\cosh k + h\sinh k$ is strictly positive (equivalently, $\tanh k = -k/h$ has no solution because $\tanh k > 0$ while $-k/h < 0$). Therefore $B = 0$, giving only the trivial solution.

Hence **none of the four problems has any negative eigenvalues**.

## Eigenvalues and eigenfunctions

Collecting the non-trivial solutions from all three regimes gives the complete spectrum for each boundary condition:

| Part | Boundary conditions | Eigenvalues $\lambda_n$ | Eigenfunctions $\phi_n(x)$ | Index range | $\lambda = 0$? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (i) | $\phi(0) = \phi(1) = 0$ | $(n\pi)^2$ | $\sin(n\pi x)$ | $n = 1, 2, \dots$ | No |
| (ii) | $\phi(0) = \phi'(1) = 0$ | $\left((n - \tfrac{1}{2})\pi\right)^2$ | $\sin\!\left((n - \tfrac{1}{2})\pi x\right)$ | $n = 1, 2, \dots$ | No |
| (iii) | $\phi'(0) = \phi'(1) = 0$ | $\lambda_0 = 0$; $\lambda_n = (n\pi)^2$ | $\phi_0 = 1$; $\phi_n = \cos(n\pi x)$ | $n = 1, 2, \dots$ | **Yes** |
| (iv) | $\phi(0) = \phi'(1) + h\phi(1) = 0$ ($h > 0$) | $\lambda_n = \mu_n^2$, $\tan\mu_n = -\mu_n/h$ | $\sin(\mu_n x)$ | $n = 1, 2, \dots$ | No |

## Answers and checks

**Direct substitution check.** For every positive mode $\phi_n(x) = \sin(\mu_n x)$ or $\cos(\mu_n x)$, differentiating twice yields $\phi_n''(x) = -\mu_n^2\phi_n(x) = -\lambda_n\phi_n(x)$, so $\phi_n'' + \lambda_n\phi_n = 0$ identically on $(0, 1)$. For $\phi_0(x) = 1$ in (iii), $\phi_0'' + 0\cdot\phi_0 = 0$ and $\phi_0'(0) = \phi_0'(1) = 0$. Checking the endpoints:

- (i) $\sin(0) = 0$ and $\sin(n\pi) = 0$.
- (ii) $\sin(0) = 0$ and $\phi_n'(1) = \bigl(n - \tfrac{1}{2}\bigr)\pi\cos\!\bigl((n - \tfrac{1}{2})\pi\bigr) = 0$.
- (iii) $\phi_n'(0) = -n\pi\sin(0) = 0$ and $\phi_n'(1) = -n\pi\sin(n\pi) = 0$.
- (iv) $\sin(0) = 0$ and $\phi_n'(1) + h\phi_n(1) = \mu_n\cos\mu_n + h\sin\mu_n = h\cos\mu_n\bigl(\tfrac{\mu_n}{h} + \tan\mu_n\bigr) = 0$ by the root equation $\tan\mu_n = -\mu_n/h$.

**Limiting-case check for the Robin condition (iv).**

- As $h \to 0^+$, the Robin condition $\phi'(1) + h\phi(1) = 0$ reduces to the Neumann condition $\phi'(1) = 0$ of part (ii). Correspondingly, $-\mu/h \to -\infty$, pushing every root $\mu_n \in \bigl((n - \tfrac{1}{2})\pi, n\pi\bigr)$ toward the left endpoint $\bigl(n - \tfrac{1}{2}\bigr)\pi$, recovering part (ii).
- As $h \to +\infty$, dividing $\phi'(1) + h\phi(1) = 0$ by $h$ yields $\phi(1) = 0$, the Dirichlet condition of part (i). Correspondingly, $-\mu/h \to 0^-$, pushing every root $\mu_n$ toward the right endpoint $n\pi$, recovering part (i).

**Dimensional check.** Here $x \in [0, 1]$ is dimensionless, so $\lambda$, $\mu$, and $h$ are dimensionless; on a physical rod of length $L$ (in $\text{m}$), $[\phi''] = [\phi]\,\text{m}^{-2}$ forces $[\lambda] = \text{m}^{-2}$, $[\mu] = \text{m}^{-1}$, and $[h] = \text{m}^{-1}$, making $\mu L$ and $\mu/h$ dimensionless.

> [!result] Key results
> - **(i) Dirichlet:** $\lambda_n = (n\pi)^2$, $\phi_n(x) = \sin(n\pi x)$ for $n = 1, 2, \dots$ ($\lambda = 0$ is not an eigenvalue).
> - **(ii) Mixed:** $\lambda_n = \bigl((n - \tfrac{1}{2})\pi\bigr)^2$, $\phi_n(x) = \sin\!\bigl((n - \tfrac{1}{2})\pi x\bigr)$ for $n = 1, 2, \dots$ ($\lambda = 0$ is not an eigenvalue).
> - **(iii) Neumann:** $\lambda_0 = 0$ with $\phi_0(x) = 1$, and $\lambda_n = (n\pi)^2$ with $\phi_n(x) = \cos(n\pi x)$ for $n = 1, 2, \dots$
> - **(iv) Robin ($h > 0$):** $\lambda_n = \mu_n^2$ and $\phi_n(x) = \sin(\mu_n x)$ for $n = 1, 2, \dots$, where $\mu_n \in \bigl((n - \tfrac{1}{2})\pi, n\pi\bigr)$ are the positive roots of $\tan\mu = -\mu/h$ (asymptotically $\mu_n \approx (n - \tfrac{1}{2})\pi + \frac{h}{(n - 1/2)\pi}$; $\lambda = 0$ is not an eigenvalue).
