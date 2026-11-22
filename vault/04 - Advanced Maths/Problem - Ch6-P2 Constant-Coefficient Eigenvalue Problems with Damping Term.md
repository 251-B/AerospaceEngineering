---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 2"
dificultad: media
id: "e2"
pill: "First-Derivative Term • Exponential Factor • Transcendental Roots"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.2: Constant-Coefficient Eigenvalue Problems with Damping Term

> Official exercise 2 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Determine the eigenvalues and eigenfunctions of the following problems:

- (i) $y''(x) + y'(x) + (1 + \lambda)y(x) = 0$, $y(0) = y(1) = 0$.
- (ii) $y''(x) + 2y'(x) + (1 - \lambda)y(x) = 0$, $y(0) = y'(1) = 0$.
- (iii) $y''(x) - 3y'(x) + 3(1 + \lambda)y(x) = 0$, $y'(0) = y'(1) = 0$.

## Classification of the problem

Each problem is a second-order, linear, homogeneous, constant-coefficient boundary-value problem on $[0, 1]$ containing a first-derivative ("damping" or "advection") term $\alpha y'(x)$. Here the unknown $y(x)$ plays the same role as $\phi(x)$ in `Notes09-12-Nov.pdf`. As shown in [[Problem - Ch6-P3 Integrating Factor for Sturm-Liouville Form]] (Haberman, Sec. 5.3), multiplying each equation by the integrating factor $e^{\alpha x}$ converts it into a regular Sturm-Liouville problem with weight $\sigma(x) = e^{\alpha x}$ (or $-e^{2x}$ in part (ii), where the sign of $\lambda$ is flipped). Consequently, all eigenvalues are real and form an unbounded discrete sequence.

## Method

Because all coefficients are constant, we solve each ODE directly with the exponential trial solution $y(x) = e^{rx}$, which produces a quadratic characteristic equation whose discriminant $\Delta$ depends linearly on $\lambda$. Rather than assuming the sign of $\lambda$ in advance, we analyse all three discriminant regimes—$\Delta > 0$ (distinct real roots), $\Delta = 0$ (repeated real root), and $\Delta < 0$ (complex-conjugate roots)—and explicitly check whether $\lambda = 0$ is an eigenvalue in every part.

## Part (i): $y''(x) + y'(x) + (1 + \lambda)y(x) = 0$, $y(0) = y(1) = 0$

Substituting $y(x) = e^{rx}$ gives the characteristic equation and its discriminant:

$$r^2 + r + (1 + \lambda) = 0, \qquad \Delta = 1^2 - 4(1)(1 + \lambda) = -3 - 4\lambda.$$

The sign of $\Delta$ changes at $\lambda = -\frac{3}{4}$. We examine all three cases.

### Case $\Delta > 0$ ($\lambda < -\frac{3}{4}$)

Setting $k = \frac{\sqrt{-3 - 4\lambda}}{2} > 0$, the two distinct real roots are $r = -\frac{1}{2} \pm k$. Writing the general solution in hyperbolic form gives:

$$y(x) = e^{-x/2}\bigl(A\cosh(kx) + B\sinh(kx)\bigr).$$

We apply the left boundary condition $y(0) = 0$:

$$y(0) = e^0\bigl(A\cosh 0 + B\sinh 0\bigr) = A = 0 \implies y(x) = Be^{-x/2}\sinh(kx).$$

Next, we impose the right boundary condition $y(1) = 0$:

$$y(1) = Be^{-1/2}\sinh(k) = 0.$$

Since $e^{-1/2} > 0$ and $\sinh(k) > 0$ for all $k > 0$, we must have $B = 0$. Hence there are **no eigenvalues** with $\lambda < -\frac{3}{4}$.

### Case $\Delta = 0$ ($\lambda = -\frac{3}{4}$)

The characteristic equation has a repeated real root $r = -\frac{1}{2}$, so the general solution is:

$$y(x) = (A + Bx)e^{-x/2}.$$

Applying $y(0) = 0$ gives $A = 0$, so $y(x) = Bxe^{-x/2}$. Applying $y(1) = 0$ gives $Be^{-1/2} = 0 \implies B = 0$. Hence $\lambda = -\frac{3}{4}$ is **not an eigenvalue**.

### Case $\Delta < 0$ ($\lambda > -\frac{3}{4}$)

Setting $\mu = \frac{\sqrt{3 + 4\lambda}}{2} > 0$, the complex-conjugate roots are $r = -\frac{1}{2} \pm i\mu$, and the real-valued general solution is:

$$y(x) = e^{-x/2}\bigl(A\cos(\mu x) + B\sin(\mu x)\bigr).$$

Imposing $y(0) = 0$ eliminates the cosine term:

$$y(0) = A = 0 \implies y(x) = Be^{-x/2}\sin(\mu x).$$

Imposing $y(1) = 0$ gives:

$$y(1) = Be^{-1/2}\sin(\mu) = 0.$$

Because $e^{-1/2} \neq 0$, a non-trivial solution ($B \neq 0$) requires $\sin(\mu) = 0$. Since $\mu > 0$, this yields $\mu_n = n\pi$ for $n = 1, 2, 3, \dots$. Solving $\frac{\sqrt{3 + 4\lambda_n}}{2} = n\pi$ for $\lambda_n$:

$$3 + 4\lambda_n = 4(n\pi)^2 \implies \lambda_n = (n\pi)^2 - \frac{3}{4}, \qquad n = 1, 2, 3, \dots$$

Note that $\lambda = 0$ lies in this regime ($\Delta = -3 < 0$) and corresponds to $\mu = \frac{\sqrt{3}}{2}$, which is not a positive integer multiple of $\pi$; therefore **$\lambda = 0$ is not an eigenvalue** of part (i). Setting $B = 1$, the eigenfunctions are $y_n(x) = e^{-x/2}\sin(n\pi x)$.

## Part (ii): $y''(x) + 2y'(x) + (1 - \lambda)y(x) = 0$, $y(0) = y'(1) = 0$

Substituting $y(x) = e^{rx}$ gives the characteristic equation, which completes the square directly:

$$r^2 + 2r + (1 - \lambda) = 0 \iff (r + 1)^2 = \lambda.$$

Here the discriminant is $\Delta = 4 - 4(1 - \lambda) = 4\lambda$, so the three discriminant regimes coincide directly with $\lambda > 0$, $\lambda = 0$, and $\lambda < 0$.

### Case $\lambda > 0$ ($\Delta > 0$)

Set $\lambda = k^2$ with $k > 0$. Then $r = -1 \pm k$, and the general solution is:

$$y(x) = e^{-x}\bigl(A\cosh(kx) + B\sinh(kx)\bigr).$$

Applying $y(0) = 0$ gives $A = 0$, so $y(x) = Be^{-x}\sinh(kx)$. We differentiate using the product rule to apply the right boundary condition:

$$y'(x) = Be^{-x}\bigl(k\cosh(kx) - \sinh(kx)\bigr).$$

Evaluating at $x = 1$ and setting $y'(1) = 0$ gives:

$$y'(1) = Be^{-1}\bigl(k\cosh k - \sinh k\bigr) = 0.$$

For $B \neq 0$, this requires $k\cosh k = \sinh k$, or equivalently $\tanh k = k$ (since $\cosh k > 0$). Consider the auxiliary function $f(k) = k - \tanh k$ for $k \ge 0$: we have $f(0) = 0$ and

$$f'(k) = 1 - \operatorname{sech}^2 k = \tanh^2 k > 0 \quad \text{for all } k > 0.$$

Thus $f(k) > 0$ strictly for all $k > 0$, so $\tanh k = k$ has **no positive solution**. Consequently $B = 0$, and there are **no positive eigenvalues**.

### Case $\lambda = 0$ ($\Delta = 0$)

When $\lambda = 0$, $(r + 1)^2 = 0$ gives the repeated root $r = -1$, so the general solution is:

$$y(x) = (A + Bx)e^{-x}.$$

Imposing $y(0) = 0$ gives $A = 0$, leaving $y(x) = Bxe^{-x}$. Differentiating by the product rule:

$$y'(x) = B\bigl(1\cdot e^{-x} + x(-e^{-x})\bigr) = B(1 - x)e^{-x}.$$

Evaluating at $x = 1$ yields:

$$y'(1) = B(1 - 1)e^{-1} = 0,$$

which is satisfied **automatically** for any $B \neq 0$. Choosing $B = 1$, we find that **$\lambda_0 = 0$ is an eigenvalue** with eigenfunction:

$$y_0(x) = xe^{-x}.$$

### Case $\lambda < 0$ ($\Delta < 0$)

Set $\lambda = -\mu^2$ with $\mu > 0$. Then $(r + 1)^2 = -\mu^2 \implies r = -1 \pm i\mu$, and the real-valued general solution is:

$$y(x) = e^{-x}\bigl(A\cos(\mu x) + B\sin(\mu x)\bigr).$$

Applying $y(0) = 0$ gives $A = 0$, so $y(x) = Be^{-x}\sin(\mu x)$. Differentiating by the product rule:

$$y'(x) = Be^{-x}\bigl(\mu\cos(\mu x) - \sin(\mu x)\bigr).$$

Imposing $y'(1) = 0$ gives:

$$y'(1) = Be^{-1}\bigl(\mu\cos\mu - \sin\mu\bigr) = 0.$$

For a non-trivial solution ($B \neq 0$), we need $\mu\cos\mu - \sin\mu = 0$. If $\cos\mu = 0$, then $\sin\mu = \pm 1 \neq 0$, which cannot satisfy the equation; hence $\cos\mu \neq 0$, and dividing by $\cos\mu$ yields the transcendental equation:

$$\tan\mu = \mu, \qquad \mu > 0.$$

We locate the positive roots graphically by intersecting $y = \tan\mu$ with the line $y = \mu$.

![[attachments/AM-PS/ch6-e2-tan.svg]]
*Graphical solution of $\tan\mu = \mu$ for $\mu > 0$: there is no root in $(0, \tfrac{\pi}{2})$, and exactly one root $\mu_n \in \bigl(n\pi, (n + \tfrac{1}{2})\pi\bigr)$ on each subsequent positive branch of $\tan\mu$.*

Checking each interval for $\mu > 0$:

- On $(0, \frac{\pi}{2})$, $\tan\mu > \mu$ strictly (since $g(\mu) = \tan\mu - \mu$ satisfies $g(0) = 0$ and $g'(\mu) = \sec^2\mu - 1 = \tan^2\mu > 0$), so there is **no root** in $(0, \frac{\pi}{2})$.
- On each interval $\bigl((n - \tfrac{1}{2})\pi, n\pi\bigr)$, $\tan\mu < 0 < \mu$, so there are no roots.
- On each interval $\bigl(n\pi, (n + \tfrac{1}{2})\pi\bigr)$ for $n = 1, 2, 3, \dots$, $\tan\mu$ increases from $0$ to $+\infty$ with second derivative $2\sec^2\mu\tan\mu > 0$ (strictly convex), while $\mu$ is linear and positive at $n\pi$; hence there is **exactly one root** $\mu_n$ in each interval:

$$n\pi < \mu_n < \left(n + \frac{1}{2}\right)\pi, \qquad n = 1, 2, 3, \dots$$

The first two positive roots are $\mu_1 \approx 4.4934$ and $\mu_2 \approx 7.7253$, and for large $n$ the intersections approach the right vertical asymptotes: $\mu_n \approx \left(n + \frac{1}{2}\right)\pi$. Setting $B = 1$ gives the negative eigenvalues and their eigenfunctions:

$$\lambda_n = -\mu_n^2, \qquad y_n(x) = e^{-x}\sin(\mu_n x), \qquad n = 1, 2, 3, \dots$$

## Part (iii): $y''(x) - 3y'(x) + 3(1 + \lambda)y(x) = 0$, $y'(0) = y'(1) = 0$

Substituting $y(x) = e^{rx}$ yields the characteristic equation and its discriminant:

$$r^2 - 3r + 3(1 + \lambda) = 0, \qquad \Delta = (-3)^2 - 4(1)\cdot 3(1 + \lambda) = 9 - 12(1 + \lambda) = -3 - 12\lambda.$$

The sign of $\Delta$ changes at $\lambda = -\frac{1}{4}$. We examine all three regimes carefully.

### Case $\Delta > 0$ ($\lambda < -\frac{1}{4}$)

Let $k = \sqrt{-3 - 12\lambda} > 0$. The two distinct real roots are:

$$r_1 = \frac{3 + k}{2}, \qquad r_2 = \frac{3 - k}{2}, \qquad r_1 \neq r_2.$$

The general solution and its derivative are:

$$y(x) = C_1 e^{r_1 x} + C_2 e^{r_2 x}, \qquad y'(x) = r_1 C_1 e^{r_1 x} + r_2 C_2 e^{r_2 x}.$$

Imposing the two Neumann boundary conditions $y'(0) = 0$ and $y'(1) = 0$ produces a homogeneous $2 \times 2$ linear system for $(C_1, C_2)$:

$$\begin{cases} r_1 C_1 + r_2 C_2 = 0, \\ r_1 e^{r_1} C_1 + r_2 e^{r_2} C_2 = 0. \end{cases}$$

A non-trivial solution $(C_1, C_2) \neq (0, 0)$ exists if and only if the determinant of the coefficient matrix vanishes:

$$\det\begin{pmatrix} r_1 & r_2 \\ r_1 e^{r_1} & r_2 e^{r_2} \end{pmatrix} = r_1 r_2 \bigl(e^{r_2} - e^{r_1}\bigr) = 0.$$

Since $r_1 \neq r_2$, we have $e^{r_2} \neq e^{r_1}$, so the determinant vanishes if and only if $r_1 r_2 = 0$. By Vieta's formula for $r^2 - 3r + 3(1 + \lambda) = 0$, the product of the roots is $r_1 r_2 = 3(1 + \lambda)$, hence:

$$3(1 + \lambda) = 0 \implies \lambda_0 = -1.$$

Checking that $\lambda_0 = -1$ indeed lies in the regime $\lambda < -\frac{1}{4}$: $-1 < -\frac{1}{4}$ holds, with $k = \sqrt{-3 - 12(-1)} = \sqrt{9} = 3$, giving $r_1 = 3$ and $r_2 = 0$. Substituting into $r_1 C_1 + r_2 C_2 = 0$ gives $3C_1 + 0\cdot C_2 = 0 \implies C_1 = 0$, while $C_2$ is arbitrary. Choosing $C_2 = 1$ gives the constant eigenfunction:

$$\lambda_0 = -1, \qquad y_0(x) = 1.$$

### Case $\Delta = 0$ ($\lambda = -\frac{1}{4}$)

The characteristic equation has the repeated root $r = \frac{3}{2}$, so the general solution and its derivative are:

$$y(x) = (A + Bx)e^{3x/2}, \qquad y'(x) = \left[\left(\frac{3}{2}A + B\right) + \frac{3}{2}Bx\right]e^{3x/2}.$$

Applying $y'(0) = 0$ gives $\frac{3}{2}A + B = 0$. Substituting this into $y'(1) = 0$ leaves:

$$y'(1) = \frac{3}{2}B e^{3/2} = 0 \implies B = 0 \implies A = 0.$$

Thus $\lambda = -\frac{1}{4}$ yields only the trivial solution and is **not an eigenvalue**.

### Case $\Delta < 0$ ($\lambda > -\frac{1}{4}$)

Setting $\mu = \frac{\sqrt{3 + 12\lambda}}{2} > 0$, the roots are $r = \frac{3}{2} \pm i\mu$, and the general solution is:

$$y(x) = e^{3x/2}\bigl(A\cos(\mu x) + B\sin(\mu x)\bigr).$$

We differentiate $y(x)$ by the product rule and collect the cosine and sine terms:

$$y'(x) = e^{3x/2}\left[\left(\frac{3}{2}A + \mu B\right)\cos(\mu x) + \left(\frac{3}{2}B - \mu A\right)\sin(\mu x)\right].$$

Imposing the left boundary condition $y'(0) = 0$ sets the cosine coefficient to zero:

$$y'(0) = \frac{3}{2}A + \mu B = 0 \implies B = -\frac{3}{2\mu}A \quad \text{(equivalently } A = -\frac{2\mu}{3}B\text{)}.$$

Substituting $\frac{3}{2}A + \mu B = 0$ back into $y'(x)$ simplifies the derivative to a single sine term:

$$y'(x) = e^{3x/2}\left(\frac{3}{2}B - \mu A\right)\sin(\mu x) = -e^{3x/2}\frac{9 + 4\mu^2}{4\mu}A\sin(\mu x).$$

Now we impose $y'(1) = 0$:

$$y'(1) = -e^{3/2}\frac{9 + 4\mu^2}{4\mu}A\sin(\mu) = 0.$$

Since $e^{3/2} > 0$ and $\frac{9 + 4\mu^2}{4\mu} > 0$ for all $\mu > 0$, a non-trivial solution ($A \neq 0$) requires $\sin(\mu) = 0$, hence $\mu_n = n\pi$ for $n = 1, 2, 3, \dots$. Solving $\frac{\sqrt{3 + 12\lambda_n}}{2} = n\pi$ for $\lambda_n$:

$$3 + 12\lambda_n = 4(n\pi)^2 \implies \lambda_n = \frac{(n\pi)^2}{3} - \frac{1}{4}, \qquad n = 1, 2, 3, \dots$$

Note that $\lambda = 0$ lies in this regime ($\Delta = -3 < 0$) with $\mu = \frac{\sqrt{3}}{2} \neq n\pi$, so **$\lambda = 0$ is not an eigenvalue** of part (iii). To avoid fractions in the eigenfunctions, we choose $A = 2\mu_n = 2n\pi$, which gives $B = -\frac{3}{2\mu_n}(2\mu_n) = -3$, yielding:

$$y_n(x) = e^{3x/2}\bigl(2n\pi\cos(n\pi x) - 3\sin(n\pi x)\bigr), \qquad n = 1, 2, 3, \dots$$

## Eigenvalues and eigenfunctions

| Part | Eigenvalues | Eigenfunctions | $\lambda = 0$? |
| :--- | :--- | :--- | :--- |
| (i) | $\lambda_n = (n\pi)^2 - \frac{3}{4}$ ($n = 1, 2, \dots$) | $y_n(x) = e^{-x/2}\sin(n\pi x)$ | No |
| (ii) | $\lambda_0 = 0$; $\lambda_n = -\mu_n^2$ with $\tan\mu_n = \mu_n$, $\mu_n \in \bigl(n\pi, (n + \tfrac{1}{2})\pi\bigr)$ ($n = 1, 2, \dots$) | $y_0(x) = xe^{-x}$; $y_n(x) = e^{-x}\sin(\mu_n x)$ | **Yes** |
| (iii) | $\lambda_0 = -1$; $\lambda_n = \frac{(n\pi)^2}{3} - \frac{1}{4}$ ($n = 1, 2, \dots$) | $y_0(x) = 1$; $y_n(x) = e^{3x/2}\bigl(2n\pi\cos(n\pi x) - 3\sin(n\pi x)\bigr)$ | No |

## Answers and checks

We verify **every** eigenfunction by direct substitution into its ODE and both boundary conditions.

**Check of part (i).** For $y_n(x) = e^{-x/2}\sin(n\pi x)$:

$$y_n'(x) = e^{-x/2}\left(-\frac{1}{2}\sin(n\pi x) + n\pi\cos(n\pi x)\right),$$

$$y_n''(x) = e^{-x/2}\left[\left(\frac{1}{4} - (n\pi)^2\right)\sin(n\pi x) - n\pi\cos(n\pi x)\right].$$

Adding $y_n'' + y_n' + \bigl(1 + (n\pi)^2 - \frac{3}{4}\bigr)y_n$: the cosine terms cancel ($-n\pi + n\pi = 0$) and the sine coefficient is $\bigl(\frac{1}{4} - (n\pi)^2\bigr) - \frac{1}{2} + \bigl(\frac{1}{4} + (n\pi)^2\bigr) = 0$. Endpoints: $y_n(0) = 0$ and $y_n(1) = e^{-1/2}\sin(n\pi) = 0$.

**Check of part (ii).**

- For $\lambda_0 = 0$, $y_0(x) = xe^{-x}$: $y_0' = (1 - x)e^{-x}$ and $y_0'' = (x - 2)e^{-x}$. Then $y_0'' + 2y_0' + (1 - 0)y_0 = \bigl[(x - 2) + 2(1 - x) + x\bigr]e^{-x} = 0$. Endpoints: $y_0(0) = 0$ and $y_0'(1) = (1 - 1)e^{-1} = 0$.
- For $\lambda_n = -\mu_n^2$, $y_n(x) = e^{-x}\sin(\mu_n x)$: $y_n' = e^{-x}\bigl(\mu_n\cos\mu_n x - \sin\mu_n x\bigr)$ and $y_n'' = e^{-x}\bigl((1 - \mu_n^2)\sin\mu_n x - 2\mu_n\cos\mu_n x\bigr)$. Then $y_n'' + 2y_n' + (1 + \mu_n^2)y_n = e^{-x}\bigl[(1 - \mu_n^2 - 2 + 1 + \mu_n^2)\sin\mu_n x + (-2\mu_n + 2\mu_n)\cos\mu_n x\bigr] = 0$. Endpoints: $y_n(0) = 0$ and $y_n'(1) = e^{-1}(\mu_n\cos\mu_n - \sin\mu_n) = 0$ since $\tan\mu_n = \mu_n$.

**Check of part (iii).**

- For $\lambda_0 = -1$, $y_0(x) = 1$: $y_0' = 0$, $y_0'' = 0$, so $0 - 0 + 3(1 - 1)\cdot 1 = 0$, and $y_0'(0) = y_0'(1) = 0$.
- For $\lambda_n = \frac{(n\pi)^2}{3} - \frac{1}{4}$, $y_n(x) = e^{3x/2}\bigl(2n\pi\cos(n\pi x) - 3\sin(n\pi x)\bigr)$:

$$y_n'(x) = -\frac{9 + 4(n\pi)^2}{2}e^{3x/2}\sin(n\pi x),$$

$$y_n''(x) = -\frac{9 + 4(n\pi)^2}{2}e^{3x/2}\left(\frac{3}{2}\sin(n\pi x) + n\pi\cos(n\pi x)\right).$$

Since $3(1 + \lambda_n) = \frac{9 + 4(n\pi)^2}{4}$, substituting into $y_n'' - 3y_n' + 3(1 + \lambda_n)y_n$ gives:

- Cosine coefficient: $\frac{9 + 4(n\pi)^2}{2}(-n\pi) - 0 + \frac{9 + 4(n\pi)^2}{4}(2n\pi) = 0$.
- Sine coefficient: $\frac{9 + 4(n\pi)^2}{4}(-3 + 6 - 3) = 0$.

Endpoints: $y_n'(0) = 0$ and $y_n'(1) = -\frac{9 + 4(n\pi)^2}{2}e^{3/2}\sin(n\pi) = 0$.

> [!result] Key results
> - **(i):** $\lambda_n = (n\pi)^2 - \frac{3}{4}$, $y_n(x) = e^{-x/2}\sin(n\pi x)$ for $n = 1, 2, \dots$ ($\lambda = 0$ is not an eigenvalue).
> - **(ii):** $\lambda_0 = 0$ with $y_0(x) = xe^{-x}$; and $\lambda_n = -\mu_n^2$ with $y_n(x) = e^{-x}\sin(\mu_n x)$ for $n = 1, 2, \dots$, where $\mu_n \in \bigl(n\pi, (n + \tfrac{1}{2})\pi\bigr)$ solves $\tan\mu_n = \mu_n$ ($\mu_1 \approx 4.4934$, $\mu_2 \approx 7.7253$, asymptotically $\mu_n \approx (n + \tfrac{1}{2})\pi$).
> - **(iii):** $\lambda_0 = -1$ with $y_0(x) = 1$; and $\lambda_n = \frac{(n\pi)^2}{3} - \frac{1}{4}$ with $y_n(x) = e^{3x/2}\bigl(2n\pi\cos(n\pi x) - 3\sin(n\pi x)\bigr)$ for $n = 1, 2, \dots$ ($\lambda = 0$ is not an eigenvalue).
