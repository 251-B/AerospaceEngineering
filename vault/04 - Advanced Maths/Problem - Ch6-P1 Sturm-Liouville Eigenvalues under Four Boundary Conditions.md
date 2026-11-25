---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 1"
dificultad: media
id: "e1"
pill: "Eigenvalues for four boundary conditions"
tags:
  - problema-resuelto
  - sturm-liouville
  - eigenvalues
  - boundary-conditions
  - robin-condition
---

# Problem 6.1: Sturm-Liouville Eigenvalues under Four Boundary Conditions

> Official exercise 1 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Determine the eigenvalues and eigenfunctions of the Sturm-Liouville problems obtained for the equation $\phi''(x) + \lambda\phi(x) = 0$ with $0 < x < 1$ and each of the following boundary conditions:

1. $\phi(0) = \phi(1) = 0$;
2. $\phi(0) = \phi'(1) = 0$;
3. $\phi'(0) = \phi'(1) = 0$;
4. $\phi(0) = \phi'(1) + h\,\phi(1) = 0$, with $h > 0$.

## Formulation and Sturm-Liouville Structure

The equation is already in self-adjoint form with $p(x) = 1$, $\sigma(x) = 1$, $q(x) = 0$, because $[1\cdot\phi']' + [\lambda\cdot 1 + 0]\phi = \phi'' + \lambda\phi$. Method: Notes09-12-Nov.pdf (Sturm-Liouville section; page to be confirmed); Haberman, Sec. 5.3.

> [!info] General solution in each sign case
> The characteristic equation $r^2 + \lambda = 0$ gives $r = \pm\sqrt{-\lambda}$, so the sign of $\lambda$ fixes the type of solution. Since no sign is known in advance, all three cases are tested in every part.
>
> | Case | Write | General solution | Derivative |
> | :--- | :--- | :--- | :--- |
> | $\lambda < 0$ | $\lambda = -\mu^2,\ \mu > 0$ | $\phi = A\cosh\mu x + B\sinh\mu x$ | $\phi' = \mu(A\sinh\mu x + B\cosh\mu x)$ |
> | $\lambda = 0$ | | $\phi = A + Bx$ | $\phi' = B$ |
> | $\lambda > 0$ | $\lambda = \mu^2,\ \mu > 0$ | $\phi = A\cos\mu x + B\sin\mu x$ | $\phi' = \mu(-A\sin\mu x + B\cos\mu x)$ |

Values used repeatedly: $\cosh\mu x > 0$ for all $x$, and $\sinh\mu x > 0$ for $\mu x > 0$. Derivative rule for $\cos$: chain rule $\frac{d}{dx}\cos(\mu x) = -\mu\sin(\mu x)$.

## Eigenvalue Cases (Negative, Zero, Positive)

### (i) $\phi(0) = \phi(1) = 0$

- $\lambda < 0$: $\phi(0) = A = 0$. Then $\phi(1) = B\sinh\mu = 0$ with $\sinh\mu > 0$, so $B = 0$. Only the trivial solution.
- $\lambda = 0$: $\phi(0) = A = 0$, $\phi(1) = A + B = B = 0$. Trivial.
- $\lambda > 0$: $\phi(0) = A = 0$. Then $\phi(1) = B\sin\mu = 0$. A non-trivial solution needs $B \ne 0$, hence $\sin\mu = 0$, so $\mu = n\pi$ ($n = 1, 2, \dots$; $\mu > 0$ excludes $n = 0$ and negative $n$ gives the same functions up to sign).

> [!result] (i)
> $\lambda_n = n^2\pi^2,\quad \phi_n(x) = \sin(n\pi x),\quad n = 1, 2, 3, \dots$

### (ii) $\phi(0) = \phi'(1) = 0$

- $\lambda < 0$: $\phi(0) = A = 0$, so $\phi = B\sinh\mu x$ and $\phi'(1) = B\mu\cosh\mu = 0$. Since $\mu\cosh\mu > 0$, $B = 0$. Trivial.
- $\lambda = 0$: $A = 0$, and $\phi'(1) = B = 0$. Trivial.
- $\lambda > 0$: $A = 0$, $\phi = B\sin\mu x$, $\phi'(1) = B\mu\cos\mu = 0$. With $B \ne 0$ and $\mu > 0$: $\cos\mu = 0$, so $\mu = \frac{(2n-1)\pi}{2}$.

> [!result] (ii)
> $\lambda_n = \left(\dfrac{(2n-1)\pi}{2}\right)^2,\quad \phi_n(x) = \sin\!\left(\dfrac{(2n-1)\pi x}{2}\right),\quad n = 1, 2, 3, \dots$

### (iii) $\phi'(0) = \phi'(1) = 0$

- $\lambda < 0$: $\phi'(0) = \mu B = 0$ gives $B = 0$. Then $\phi'(1) = \mu A\sinh\mu = 0$ with $\sinh\mu > 0$ gives $A = 0$. Trivial.
- $\lambda = 0$: $\phi' = B$, so $\phi'(0) = \phi'(1) = B = 0$. This leaves $\phi = A$ with $A$ arbitrary, which is non-trivial.
- $\lambda > 0$: $\phi'(0) = \mu B = 0$ gives $B = 0$. Then $\phi'(1) = -\mu A\sin\mu = 0$ gives $\sin\mu = 0$, so $\mu = n\pi$, $n \ge 1$.

> [!warning] $\lambda = 0$ is an eigenvalue here
> Unlike (i), (ii) and (iv), the Neumann conditions admit the constant function. So $\lambda_0 = 0$, $\phi_0(x) = 1$. Dropping this case would lose the constant mode of every Fourier cosine series. Check: $\phi_0'' + 0\cdot\phi_0 = 0$ and $\phi_0'(0) = \phi_0'(1) = 0$.

> [!result] (iii)
> $\lambda_0 = 0,\ \phi_0(x) = 1$; and $\lambda_n = n^2\pi^2,\ \phi_n(x) = \cos(n\pi x)$, $n = 1, 2, 3, \dots$ (the formula $\cos(n\pi x)$ with $n = 0$ reproduces $\phi_0$).

### (iv) $\phi(0) = 0$ and $\phi'(1) + h\,\phi(1) = 0$, with $h > 0$

- $\lambda < 0$: $A = 0$, $\phi = B\sinh\mu x$. The second condition is $B(\mu\cosh\mu + h\sinh\mu) = 0$. Since $\mu > 0$, $h > 0$, $\cosh\mu > 0$, $\sinh\mu > 0$, the bracket is strictly positive, so $B = 0$. Trivial.
- $\lambda = 0$: $A = 0$, $\phi = Bx$, $\phi' = B$. Then $\phi'(1) + h\phi(1) = B + hB = B(1+h) = 0$ and $1 + h > 0$, so $B = 0$. Trivial.
- $\lambda > 0$: $A = 0$, $\phi = B\sin\mu x$, and
$$\phi'(1) + h\phi(1) = B\left(\mu\cos\mu + h\sin\mu\right) = 0.$$
If $\cos\mu = 0$ then $\sin\mu = \pm 1$ and the bracket equals $\pm h \ne 0$, so $\cos\mu \ne 0$ at any eigenvalue. Dividing by $h\cos\mu$:
$$\tan\mu = -\frac{\mu}{h}.$$

> [!info] Graphical location of the roots
> Plot $y = \tan\mu$ and $y = -\mu/h$ for $\mu > 0$.
> - On $(0, \pi/2)$ and, in general, on $(n\pi, (2n+1)\pi/2)$: $\tan\mu > 0$ while $-\mu/h < 0$, so there is no intersection.
> - On $\left(\frac{(2n-1)\pi}{2}, n\pi\right)$: $\tan\mu$ rises continuously from $-\infty$ to $0$ while $-\mu/h$ is finite and negative. Define $f(\mu) = \tan\mu + \mu/h$. Then $f \to -\infty$ at the left end, $f(n\pi) = n\pi/h > 0$ at the right end, so a root exists, and it is unique because $f'(\mu) = \sec^2\mu + 1/h > 0$.
>
> Hence exactly one root $\mu_n$ lies in each interval $\left(\frac{(2n-1)\pi}{2}, n\pi\right)$, $n = 1, 2, \dots$ As $n \to \infty$, $-\mu_n/h \to -\infty$, so $\mu_n \to \frac{(2n-1)\pi}{2}$ from above.

![[attachments/AM-PS/ch6-e1-iv.svg]]
*Intersections of $y = \tan\mu$ and $y = -\mu/h$: one root $\mu_n$ in each interval $((2n-1)\pi/2,\ n\pi)$.*

> [!result] (iv)
> $\lambda_n = \mu_n^2$ with $\mu_n$ the unique root of $\tan\mu = -\mu/h$ in $\left(\frac{(2n-1)\pi}{2}, n\pi\right)$, and $\phi_n(x) = \sin(\mu_n x)$, $n = 1, 2, 3, \dots$. No eigenvalue satisfies $\lambda \le 0$ when $h > 0$.

## Eigenfunctions and Checks

- Limiting cases in (iv): dividing the condition $\mu\cos\mu + h\sin\mu = 0$ by $h$ and letting $h \to \infty$ gives $\sin\mu = 0$, so $\mu_n \to n\pi$ (the condition becomes $\phi(1) = 0$, recovering (i)). Letting $h \to 0^+$ gives $\mu\cos\mu = 0$, so $\mu_n \to \frac{(2n-1)\pi}{2}$ (the condition becomes $\phi'(1) = 0$, recovering (ii)). Both limits are the end points of the interval $\left(\frac{(2n-1)\pi}{2}, n\pi\right)$ that contains $\mu_n$.
- Dimensions: $\lambda\,[\mathrm{L}^{-2}]$ since $\phi'' \sim \phi/\mathrm{L}^2$; with $x$ non-dimensionalised by the length, $\mu$ is dimensionless, as is $h$ (units $\mathrm{L}^{-1}$ before scaling).
- Orthogonality with weight $\sigma = 1$: e.g. (i), $\int_0^1\sin(n\pi x)\sin(m\pi x)\,dx = \frac12\delta_{nm}$. Barrow check for $n \ne m$: $\frac12\left[\frac{\sin((n-m)\pi x)}{(n-m)\pi} - \frac{\sin((n+m)\pi x)}{(n+m)\pi}\right]_0^1 = 0$.
- Sign of $\lambda$: the Rayleigh quotient with $p = 1$, $q = 0$ gives $\lambda = \frac{\int(\phi')^2 + h\phi(1)^2}{\int\phi^2} > 0$ in (iv) (boundary term $-[\phi\phi']_0^1 = h\phi(1)^2$ for $h > 0$), which agrees with the direct proof that no $\lambda \le 0$ exists.
