---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 2"
dificultad: media
id: "e2"
pill: "Eigenvalue problems with first-derivative term"
tags:
  - problema-resuelto
  - sturm-liouville
  - eigenvalues
  - integrating-factor
  - characteristic-polynomial
---

# Problem 6.2: Non-Standard Constant-Coefficient Eigenvalue Problems

> Official exercise 2 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Determine the eigenvalues and eigenfunctions of the following problems:

1. $y''(x) + y'(x) + (1+\lambda)\,y(x) = 0,\quad y(0) = y(1) = 0$;
2. $y''(x) + 2y'(x) + (1-\lambda)\,y(x) = 0,\quad y(0) = y'(1) = 0$;
3. $y''(x) - 3y'(x) + 3(1+\lambda)\,y(x) = 0,\quad y'(0) = y'(1) = 0$.

## Formulation and Sturm-Liouville Structure

Each equation has the form $y'' + \alpha y' + [\lambda\beta + \gamma]y = 0$ with constant $\alpha, \beta, \gamma$. The integrating factor $\mu(x) = e^{\alpha x}$ (derived in [[Problem - Ch6-P3 Integrating Factor for Sturm-Liouville Self-Adjoint Form]]) turns it into $[\mu y']' + [\lambda\mu\beta + \mu\gamma]y = 0$:

| Part | $\alpha$ | $\beta$ | $\gamma$ | $p = \mu$ | $\sigma = \mu\beta$ | $q = \mu\gamma$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (i) | $1$ | $1$ | $1$ | $e^{x}$ | $e^{x}$ | $e^{x}$ |
| (ii) | $2$ | $-1$ | $1$ | $e^{2x}$ | $-e^{2x}$ | $e^{2x}$ |
| (iii) | $-3$ | $3$ | $3$ | $e^{-3x}$ | $3e^{-3x}$ | $3e^{-3x}$ |

The characteristic polynomial $r^2 + \alpha r + (\lambda\beta + \gamma) = 0$ has discriminant $\Delta = \alpha^2 - 4(\lambda\beta+\gamma)$. All three signs of $\Delta$ are examined in each part; the value of $\lambda$ at which $\Delta$ changes sign is found first. Method: Notes09-12-Nov.pdf (Sturm-Liouville section; page to be confirmed); Haberman, Sec. 5.3.

> [!warning] Sign of $\sigma$ in (ii)
> In (ii) the coefficient of $y$ is $(1 - \lambda)$, so $\sigma = -e^{2x} < 0$. The usual argument "$\lambda > 0$ for $p, \sigma > 0$" is reversed: the eigenvalues turn out to be non-positive.

## Eigenvalue Cases (Negative, Zero, Positive)

### (i) $y'' + y' + (1+\lambda)y = 0$, $y(0) = y(1) = 0$

Roots: $r = \dfrac{-1 \pm \sqrt{1 - 4(1+\lambda)}}{2} = \dfrac{-1 \pm \sqrt{-3-4\lambda}}{2}$, so $\Delta = -3 - 4\lambda$.

- $\Delta > 0$, i.e. $\lambda < -3/4$. Put $\nu = \tfrac12\sqrt{-3-4\lambda} > 0$. Then $y = e^{-x/2}(A\cosh\nu x + B\sinh\nu x)$. $y(0) = A = 0$; $y(1) = Be^{-1/2}\sinh\nu = 0$ with $\sinh\nu > 0$, so $B = 0$. Trivial.
- $\Delta = 0$, i.e. $\lambda = -3/4$. Then $y = e^{-x/2}(c_1 + c_2 x)$. $y(0) = c_1 = 0$; $y(1) = c_2e^{-1/2} = 0$ gives $c_2 = 0$. Trivial.
- $\Delta < 0$, i.e. $\lambda > -3/4$. Put $\omega^2 = \lambda + \tfrac34 > 0$, so $\sqrt{\Delta} = 2i\omega$ and $r = -\tfrac12 \pm i\omega$. Then $y = e^{-x/2}(A\cos\omega x + B\sin\omega x)$. $y(0) = A = 0$; $y(1) = Be^{-1/2}\sin\omega = 0$, so $\sin\omega = 0$ and $\omega = n\pi$, $n \ge 1$.

> [!result] (i)
> $\lambda_n = n^2\pi^2 - \dfrac34,\quad y_n(x) = e^{-x/2}\sin(n\pi x),\quad n = 1, 2, 3, \dots$

Check of the ODE for $y_n$: $y' = e^{-x/2}\left(-\tfrac12\sin\omega x + \omega\cos\omega x\right)$ (product rule), $y'' = e^{-x/2}\left[\left(\tfrac14 - \omega^2\right)\sin\omega x - \omega\cos\omega x\right]$. Then $y'' + y' + (1+\lambda)y = e^{-x/2}\sin\omega x\left[\tfrac14 - \omega^2 - \tfrac12 + 1 + \lambda\right] + e^{-x/2}\cos\omega x[-\omega + \omega] = e^{-x/2}\sin\omega x\,[\lambda + \tfrac34 - \omega^2] = 0$. ✓.

Orthogonality weight $\sigma = e^{x}$: $\int_0^1 e^{x}y_ny_m\,dx = \int_0^1 e^{x}e^{-x}\sin(n\pi x)\sin(m\pi x)\,dx = \tfrac12\delta_{nm}$.

### (ii) $y'' + 2y' + (1-\lambda)y = 0$, $y(0) = y'(1) = 0$

Roots: $r^2 + 2r + (1-\lambda) = 0$ gives $r = -1 \pm \sqrt{\lambda}$ (here $\Delta = 4\lambda$).

- $\lambda > 0$ ($\Delta > 0$). Put $s = \sqrt\lambda > 0$: $y = e^{-x}(A\cosh sx + B\sinh sx)$; $y(0) = A = 0$, so $y = Be^{-x}\sinh sx$. By the product rule $y' = Be^{-x}(s\cosh sx - \sinh sx)$, so
$$y'(1) = Be^{-1}\left(s\cosh s - \sinh s\right) = 0 \iff \tanh s = s.$$
Define $g(u) = u - \tanh u$. Then $g(0) = 0$ and $g'(u) = 1 - \operatorname{sech}^2 u = \tanh^2 u > 0$ for $u > 0$. Hence $g$ is strictly increasing, so $g(u) > 0$ and $\tanh u < u$ for all $u > 0$. The equation $\tanh s = s$ has no solution with $s > 0$, so $B = 0$. No eigenvalue with $\lambda > 0$.
- $\lambda = 0$ ($\Delta = 0$). $y = e^{-x}(c_1 + c_2x)$. $y(0) = c_1 = 0$. Then $y = c_2xe^{-x}$ and $y' = c_2(1-x)e^{-x}$, so $y'(1) = c_2\cdot 0 = 0$ for every $c_2$. The boundary condition holds identically.

> [!warning] $\lambda = 0$ is an eigenvalue
> $y_0(x) = xe^{-x}$ satisfies $y_0'' + 2y_0' + y_0 = 0$ (since $(r+1)^2 = 0$ with double root $-1$), $y_0(0) = 0$ and $y_0'(1) = (1-1)e^{-1} = 0$. It is non-trivial, so $\lambda_0 = 0$ is an eigenvalue. This is the limit $s \to 0$ of the root condition $s\cosh s - \sinh s = 0$, which vanishes at $s = 0$ because $g(0) = 0$.

- $\lambda < 0$ ($\Delta < 0$). Put $\lambda = -\omega^2$, $\omega > 0$: $r = -1 \pm i\omega$, $y = e^{-x}(A\cos\omega x + B\sin\omega x)$. $y(0) = A = 0$, $y = Be^{-x}\sin\omega x$, $y' = Be^{-x}(\omega\cos\omega x - \sin\omega x)$, and
$$y'(1) = Be^{-1}(\omega\cos\omega - \sin\omega) = 0 \iff \tan\omega = \omega \quad(\cos\omega \ne 0,\text{ otherwise }\sin\omega = \pm1\ne 0).$$

> [!info] Location of the roots of $\tan\omega = \omega$
> Let $h(\omega) = \tan\omega - \omega$, with $h'(\omega) = \tan^2\omega \ge 0$.
> - On $(0, \pi/2)$: $h(0) = 0$ and $h' > 0$ for $\omega > 0$, so $h > 0$: no positive root.
> - On $(n\pi - \pi/2,\ n\pi)$: $\tan\omega \le 0 < \omega$, so $h < 0$: no root.
> - On $\left(n\pi,\ n\pi + \tfrac\pi2\right)$, $n \ge 1$: $h(n\pi) = -n\pi < 0$ and $h \to +\infty$ at the right end; $h$ is strictly increasing, so exactly one root $\omega_n$.
>
> So $\omega_n \in \left(n\pi, \left(n+\tfrac12\right)\pi\right)$: $\omega_1 \approx 4.4934\in(\pi, 3\pi/2)$, $\omega_2 \approx 7.7253$, and $\omega_n \to \left(n+\tfrac12\right)\pi$.

> [!result] (ii)
> $\lambda_0 = 0,\ y_0(x) = xe^{-x}$; and $\lambda_n = -\omega_n^2 < 0,\ y_n(x) = e^{-x}\sin(\omega_nx)$, with $\omega_n$ the root of $\tan\omega = \omega$ in $\left(n\pi, (n+\tfrac12)\pi\right)$, $n = 1, 2, \dots$

Why the eigenvalues are non-positive: $\sigma = -e^{2x} < 0$ (see the table), so the roles of $\lambda$ and $-\lambda$ swap relative to the standard problem. With $y = e^{-x}u$ (Liouville shift, see [[Problem - Ch6-P3 Integrating Factor for Sturm-Liouville Self-Adjoint Form]]) the equation becomes $u'' - \lambda u = 0$ with $u(0) = 0$, $u'(1) = u(1)$ (Robin), whose eigenvalue parameter is $-\lambda$, which is $\ge 0$.

Orthogonality, weight $|\sigma| = e^{2x}$: $\int_0^1 e^{2x}y_ny_m\,dx = \int_0^1\sin(\omega_nx)\sin(\omega_mx)\,dx = 0$ for $n \ne m$ (Robin-type problem). Direct check with $y_0$: $\int_0^1 e^{2x}\,xe^{-x}\,e^{-x}\sin\omega_nx\,dx = \int_0^1 x\sin\omega_nx\,dx = \left[-\dfrac{x\cos\omega_nx}{\omega_n}\right]_0^1 + \dfrac1{\omega_n}\int_0^1\cos\omega_nx\,dx = -\dfrac{\cos\omega_n}{\omega_n} + \dfrac{\sin\omega_n}{\omega_n^2}$, which is $0$ because $\sin\omega_n = \omega_n\cos\omega_n$.

### (iii) $y'' - 3y' + 3(1+\lambda)y = 0$, $y'(0) = y'(1) = 0$

Roots: $r = \dfrac{3 \pm \sqrt{9 - 12(1+\lambda)}}{2} = \dfrac{3 \pm \sqrt{-3-12\lambda}}{2}$, so $\Delta = -3 - 12\lambda$.

- $\Delta > 0$, i.e. $\lambda < -1/4$. Put $\mu = \tfrac12\sqrt{-3-12\lambda} = \sqrt{-\tfrac34 - 3\lambda} > 0$, so $r = \tfrac32 \pm \mu$ and $y = e^{3x/2}(A\cosh\mu x + B\sinh\mu x)$. By the product rule
$$y' = e^{3x/2}\left[\tfrac32(A\cosh\mu x + B\sinh\mu x) + \mu(A\sinh\mu x + B\cosh\mu x)\right].$$
$y'(0) = 0$: $\tfrac32A + \mu B = 0$. $y'(1) = 0$: $A\left(\tfrac32\cosh\mu + \mu\sinh\mu\right) + B\left(\tfrac32\sinh\mu + \mu\cosh\mu\right) = 0$. The determinant of the $2\times2$ system in $(A, B)$ is
$$\tfrac32\left(\tfrac32\sinh\mu + \mu\cosh\mu\right) - \mu\left(\tfrac32\cosh\mu + \mu\sinh\mu\right) = \left(\tfrac94 - \mu^2\right)\sinh\mu.$$
With $\sinh\mu > 0$, a non-trivial solution exists only if $\mu = \tfrac32$, that is $-\tfrac34 - 3\lambda = \tfrac94$, so $\lambda = -1$ (consistent with $\lambda < -1/4$). Then $A = -\tfrac{2\mu}{3}B = -B$ and
$$y = B e^{3x/2}\left(\sinh\tfrac{3x}{2} - \cosh\tfrac{3x}{2}\right) = -B e^{3x/2}e^{-3x/2} = -B.$$

> [!warning] A negative eigenvalue with a constant eigenfunction
> At $\lambda = -1$ the equation is $y'' - 3y' = 0$, with general solution $y = c_1 + c_2e^{3x}$. $y' = 3c_2e^{3x}$ and $y'(0) = 3c_2 = 0$ gives $c_2 = 0$, then $y'(1) = 0$ holds. So $y_0(x) = 1$ is an eigenfunction at $\lambda_0 = -1$. Check: $y_0'' - 3y_0' + 3(1 + (-1))y_0 = 0$ ✓, $y_0'(0) = y_0'(1) = 0$ ✓.

- $\Delta = 0$, i.e. $\lambda = -1/4$. $y = e^{3x/2}(c_1 + c_2x)$, $y' = e^{3x/2}\left[\tfrac32c_1 + \tfrac32c_2x + c_2\right]$. $y'(0) = \tfrac32c_1 + c_2 = 0$; $y'(1) = e^{3/2}\left[\tfrac32c_1 + \tfrac52c_2\right] = 0$. Subtracting: $\tfrac32c_2 = 0$, so $c_2 = 0$ and $c_1 = 0$. Trivial.
- $\Delta < 0$, i.e. $\lambda > -1/4$. Put $\omega^2 = 3\lambda + \tfrac34 > 0$, so $r = \tfrac32 \pm i\omega$ and $y = e^{3x/2}(A\cos\omega x + B\sin\omega x)$. Then
$$y' = e^{3x/2}\left[\left(\tfrac32A + \omega B\right)\cos\omega x + \left(\tfrac32B - \omega A\right)\sin\omega x\right].$$
$y'(0) = \tfrac32A + \omega B = 0$. With this condition the coefficient of $\cos\omega x$ in $y'$ is exactly $0$, so $y'(1) = e^{3/2}\left(\tfrac32B - \omega A\right)\sin\omega = 0$. If $\tfrac32B - \omega A = 0$, then together with $\tfrac32A + \omega B = 0$ the matrix $\begin{pmatrix}\tfrac32 & \omega\\ -\omega & \tfrac32\end{pmatrix}$ has determinant $\tfrac94 + \omega^2 > 0$, so $A = B = 0$ (trivial). Hence $\sin\omega = 0$, $\omega = n\pi$, $n \ge 1$, and $\lambda_n = \dfrac{n^2\pi^2 - 3/4}{3} = \dfrac{n^2\pi^2}{3} - \dfrac14$. Choose $A = 1$; then $B = -\dfrac{3}{2n\pi}$.

> [!result] (iii)
> $\lambda_0 = -1,\ y_0(x) = 1$; and $\lambda_n = \dfrac{n^2\pi^2}{3} - \dfrac14,\quad y_n(x) = e^{3x/2}\left[\cos(n\pi x) - \dfrac{3}{2n\pi}\sin(n\pi x)\right],\quad n = 1, 2, \dots$

## Eigenfunctions and Checks

- Boundary conditions of $y_n$ in (iii), explicitly: $y_n'(0) = \tfrac32\cdot1 + n\pi\left(-\tfrac{3}{2n\pi}\right) = 0$ ✓; $y_n'(1) = e^{3/2}\left[0\cdot\cos n\pi + \left(-\tfrac{9}{4n\pi} - n\pi\right)\sin n\pi\right] = 0$ ✓ (first bracket is $0$, second multiplies $\sin n\pi = 0$).
- Orthogonality in (iii), weight $\sigma = 3e^{-3x}$: $y_0 = 1$ against $y_n$ gives $\int_0^1 e^{-3x}e^{3x/2}\left[\cos n\pi x - \tfrac{3}{2n\pi}\sin n\pi x\right]dx = \int_0^1\dfrac{1}{n\pi}\dfrac{d}{dx}\left[e^{-3x/2}\sin n\pi x\right]dx$, because $\dfrac{d}{dx}\left[e^{-3x/2}\sin n\pi x\right] = e^{-3x/2}\left(n\pi\cos n\pi x - \tfrac32\sin n\pi x\right)$. By Barrow's rule the value is $\dfrac1{n\pi}\left[e^{-3x/2}\sin n\pi x\right]_0^1 = 0$ ✓.
- Liouville-shift check ($y = e^{-\alpha x/2}u$ gives $u'' + [\lambda\beta + \gamma - \alpha^2/4]u = 0$): (i) $u'' + (\lambda + \tfrac34)u = 0$; (ii) $u'' - \lambda u = 0$; (iii) $u'' + (3\lambda + \tfrac34)u = 0$. These match $\omega^2 = \lambda + \tfrac34$, $\omega^2 = -\lambda$ and $\omega^2 = 3\lambda + \tfrac34$ above.
- Dimensions: each term of the ODE has dimension $[y]/\mathrm{L}^2$ with $x$ non-dimensional, so $\lambda$ is dimensionless.
