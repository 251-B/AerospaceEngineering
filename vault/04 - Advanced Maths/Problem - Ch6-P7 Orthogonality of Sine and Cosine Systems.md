---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 7"
dificultad: media
id: "e7"
pill: "Orthogonality • Product-to-Sum • Barrow Rule"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.7: Orthogonality of Sine and Cosine Systems

> Official exercise 7 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Show that the functions $y_n(x) = \sin\left(\frac{n\pi x}{L}\right)$ satisfy

$$ \int_{-L}^{L} y_n(x)y_m(x)\,dx = \begin{cases} 0, & n \neq m, \\ L, & n = m, \end{cases} $$

for $m, n = 0, 1, 2, \dots$ Show that a similar property holds for $u_n(x) = \cos\left(\frac{n\pi x}{L}\right)$:

$$ \int_{-L}^{L} u_n(x)u_m(x)\,dx = \begin{cases} 0, & n \neq m, \\ L, & n = m \neq 0, \\ 2L, & n = m = 0, \end{cases} $$

for $m, n = 0, 1, 2, \dots$

## Classification of the problem

This is a direct verification of the $L^2([-L, L])$ orthogonality and normalization integrals of the trigonometric Fourier basis $\left\{\sin\frac{n\pi x}{L}, \cos\frac{n\pi x}{L}\right\}$ (Haberman, Appendix to Sec. 2.3, p. 49, and Sec. 3.2, p. 77). These identities are the exact algebraic foundation of the Euler-Fourier coefficient formulas (`Notes09-12-Nov.pdf`, p. 10).

## Method

To evaluate products of sines and cosines without integration by parts, we convert every product into a sum or difference of single cosines using the product-to-sum identities:

$$ \sin A \sin B = \frac{1}{2}\big[\cos(A - B) - \cos(A + B)\big], \qquad \cos A \cos B = \frac{1}{2}\big[\cos(A - B) + \cos(A + B)\big]. $$

These follow immediately from the cosine addition and subtraction formulas:

$$ \cos(A - B) = \cos A\cos B + \sin A\sin B, \qquad \cos(A + B) = \cos A\cos B - \sin A\sin B. $$

Subtracting the second from the first and dividing by $2$ gives the $\sin A\sin B$ identity; adding them and dividing by $2$ gives the $\cos A\cos B$ identity.

We must separate the cases where the angular frequency $(n - m)\frac{\pi}{L}$ or $(n + m)\frac{\pi}{L}$ is zero (so $\int_{-L}^L 1\,dx = 2L$) from the cases where it is a nonzero integer multiple $k\frac{\pi}{L}$ ($k \in \mathbb{Z}\setminus\{0\}$), where

$$ \int_{-L}^{L} \cos\left(\frac{k\pi x}{L}\right)dx = \left[\frac{L}{k\pi}\sin\left(\frac{k\pi x}{L}\right)\right]_{-L}^{L} = \frac{L}{k\pi}\big(\sin(k\pi) - \sin(-k\pi)\big) = \frac{L}{k\pi}(0 - 0) = 0. $$

## Step-by-step derivation

### 1. Orthogonality of the sine system $y_n(x) = \sin\left(\frac{n\pi x}{L}\right)$

Let $I_{nm} = \int_{-L}^{L} \sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)dx$ for integers $m, n \ge 0$.

#### Case 1a: $n = 0$ or $m = 0$

If either $n = 0$ or $m = 0$, then $y_0(x) = \sin(0) \equiv 0$ identically on $[-L, L]$, so the integrand vanishes everywhere and

$$ I_{nm} = \int_{-L}^{L} 0\,dx = 0. $$

In particular, when $n = m = 0$, we obtain $I_{00} = 0$ (not $L$; see the erratum note below).

> [!warning] Sheet erratum for $n = m = 0$ in the sine identity
> The problem sheet writes $m, n = 0, 1, 2, \dots$ with value $L$ for $n = m$. However, for $n = m = 0$, $y_0(x) = \sin(0) \equiv 0$, so $\int_{-L}^{L} y_0(x)^2\,dx = 0 \neq L$. The normalization value $L$ holds for **$n = m \ge 1$**, while $n = 0$ is excluded from the sine basis (which starts at $n = 1$).

#### Case 1b: $n \neq m$ with $n, m \ge 1$

We apply the product-to-sum identity with $A = \frac{n\pi x}{L}$ and $B = \frac{m\pi x}{L}$.

$$ I_{nm} = \frac{1}{2}\int_{-L}^{L} \left[\cos\left(\frac{(n - m)\pi x}{L}\right) - \cos\left(\frac{(n + m)\pi x}{L}\right)\right]dx. $$

Since $n \neq m$ and $n, m \ge 1$, both integers $n - m \neq 0$ and $n + m \ge 2 \neq 0$ are nonzero, so we integrate both cosines explicitly using $\int \cos(\alpha x)\,dx = \frac{\sin(\alpha x)}{\alpha}$.

$$ I_{nm} = \frac{1}{2}\left[\frac{L}{(n - m)\pi}\sin\left(\frac{(n - m)\pi x}{L}\right) - \frac{L}{(n + m)\pi}\sin\left(\frac{(n + m)\pi x}{L}\right)\right]_{-L}^{L}. $$

Applying Barrow's rule $[F]_{-L}^{L} = F(L) - F(-L)$ and using $\sin(k\pi) = 0$ and $\sin(-k\pi) = 0$ for every integer $k$:

$$ I_{nm} = \frac{1}{2}\left[\frac{L}{(n - m)\pi}\big(\sin((n-m)\pi) - \sin(-(n-m)\pi)\big) - \frac{L}{(n + m)\pi}\big(\sin((n+m)\pi) - \sin(-(n+m)\pi)\big)\right] = \frac{1}{2}(0 - 0) = 0. $$

#### Case 1c: $n = m \ge 1$

When $n = m \ge 1$, the first angle is $A - B = 0$, so $\cos(0) = 1$, and the product-to-sum formula reduces to the half-angle identity $\sin^2\left(\frac{n\pi x}{L}\right) = \frac{1}{2}\left[1 - \cos\left(\frac{2n\pi x}{L}\right)\right]$.

$$ I_{nn} = \frac{1}{2}\int_{-L}^{L} \left[1 - \cos\left(\frac{2n\pi x}{L}\right)\right]dx = \frac{1}{2}\left[x - \frac{L}{2n\pi}\sin\left(\frac{2n\pi x}{L}\right)\right]_{-L}^{L}. $$

Applying Barrow's rule with $\sin(2n\pi) = 0$ and $\sin(-2n\pi) = 0$:

$$ I_{nn} = \frac{1}{2}\left[\big(L - (-L)\big) - \frac{L}{2n\pi}\big(\sin(2n\pi) - \sin(-2n\pi)\big)\right] = \frac{1}{2}(2L - 0) = L. $$

### 2. Orthogonality of the cosine system $u_n(x) = \cos\left(\frac{n\pi x}{L}\right)$

Let $J_{nm} = \int_{-L}^{L} \cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi x}{L}\right)dx$ for integers $m, n \ge 0$.

#### Case 2a: $n = m = 0$

Here $u_0(x) = \cos(0) = 1$, so we integrate the constant $1$ over $[-L, L]$.

$$ J_{00} = \int_{-L}^{L} 1 \cdot 1\,dx = \Big[x\Big]_{-L}^{L} = L - (-L) = 2L. $$

#### Case 2b: $n \neq m$ with $n, m \ge 0$

We apply the product-to-sum identity $\cos A\cos B = \frac{1}{2}[\cos(A - B) + \cos(A + B)]$ with $A = \frac{n\pi x}{L}$ and $B = \frac{m\pi x}{L}$.

$$ J_{nm} = \frac{1}{2}\int_{-L}^{L} \left[\cos\left(\frac{(n - m)\pi x}{L}\right) + \cos\left(\frac{(n + m)\pi x}{L}\right)\right]dx. $$

Because $n \neq m$ and both are nonnegative integers, $n - m \neq 0$ and at least one of $n, m$ is positive, so $n + m \ge 1 \neq 0$. Both denominators are nonzero, and we integrate term by term.

$$ J_{nm} = \frac{1}{2}\left[\frac{L}{(n - m)\pi}\sin\left(\frac{(n - m)\pi x}{L}\right) + \frac{L}{(n + m)\pi}\sin\left(\frac{(n + m)\pi x}{L}\right)\right]_{-L}^{L}. $$

Applying Barrow's rule with $\sin(k\pi) = \sin(-k\pi) = 0$ for all $k \in \mathbb{Z}$:

$$ J_{nm} = \frac{1}{2}\left[\frac{L}{(n - m)\pi}(0 - 0) + \frac{L}{(n + m)\pi}(0 - 0)\right] = 0. $$

(Note that if one index is $0$ and the other is $k \ge 1$, this directly reduces to $\int_{-L}^L \cos\left(\frac{k\pi x}{L}\right)dx = \left[\frac{L}{k\pi}\sin\left(\frac{k\pi x}{L}\right)\right]_{-L}^{L} = 0$.)

#### Case 2c: $n = m \ge 1$

When $n = m \ge 1$, the identity reduces to $\cos^2\left(\frac{n\pi x}{L}\right) = \frac{1}{2}\left[1 + \cos\left(\frac{2n\pi x}{L}\right)\right]$.

$$ J_{nn} = \frac{1}{2}\int_{-L}^{L} \left[1 + \cos\left(\frac{2n\pi x}{L}\right)\right]dx = \frac{1}{2}\left[x + \frac{L}{2n\pi}\sin\left(\frac{2n\pi x}{L}\right)\right]_{-L}^{L}. $$

Applying Barrow's rule with $\sin(2n\pi) = \sin(-2n\pi) = 0$:

$$ J_{nn} = \frac{1}{2}\left[\big(L - (-L)\big) + \frac{L}{2n\pi}(0 - 0)\right] = \frac{1}{2}(2L) = L. $$

### 3. Bonus check: cross-orthogonality between sines and cosines

To complete the orthogonality of the full Fourier system on $[-L, L]$, we also check $K_{nm} = \int_{-L}^{L} y_n(x)u_m(x)\,dx = \int_{-L}^{L} \sin\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi x}{L}\right)dx$ for all $n, m \ge 0$.

Because $\sin\left(\frac{n\pi(-x)}{L}\right)\cos\left(\frac{m\pi(-x)}{L}\right) = -\sin\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi x}{L}\right)$, the integrand is an **odd function** on the symmetric interval $[-L, L]$. Splitting the integral at $0$ and substituting $u = -x$ ($du = -dx$, limits $x = -L \to u = L$ and $x = 0 \to u = 0$) gives

$$ K_{nm} = \int_{-L}^{0} y_n(x)u_m(x)\,dx + \int_{0}^{L} y_n(x)u_m(x)\,dx = -\int_{0}^{L} y_n(u)u_m(u)\,du + \int_{0}^{L} y_n(x)u_m(x)\,dx = 0 $$

for every $m, n = 0, 1, 2, \dots$

## Answers and checks

1. **Dimensional check**: If $x$ and $L$ carry length units $[\text{m}]$, then $\frac{n\pi x}{L}$ is dimensionless, $y_n(x)$ and $u_n(x)$ are dimensionless, and $\int_{-L}^{L} y_n(x)y_m(x)\,dx$ has units of $[\text{m}]$, matching $L$ and $2L$.
2. **Pythagorean sum check**: For every $n \ge 1$, adding the two diagonal integrals gives
$$ I_{nn} + J_{nn} = \int_{-L}^{L} \left[\sin^2\left(\frac{n\pi x}{L}\right) + \cos^2\left(\frac{n\pi x}{L}\right)\right]dx = \int_{-L}^{L} 1\,dx = 2L, $$
which matches $L + L = 2L$. For $n = 0$, $I_{00} + J_{00} = 0 + 2L = 2L$, confirming why $I_{00}$ must be $0$ and not $L$.
3. **Recovery of Euler-Fourier prefactors**: Multiplying $f(x) \sim a_0 + \sum_{m=1}^{\infty}[a_m u_m(x) + b_m y_m(x)]$ by $1 = u_0(x)$, $u_n(x)$, and $y_n(x)$ and integrating over $[-L, L]$ yields $2L a_0$, $L a_n$, and $L b_n$, explaining why $a_0$ carries $\frac{1}{2L}$ while $a_n, b_n$ ($n \ge 1$) carry $\frac{1}{L}$.

> [!result] Key results
> - **Sine system** $y_n(x) = \sin\left(\frac{n\pi x}{L}\right)$:
>   $$\int_{-L}^{L} y_n(x)y_m(x)\,dx = \begin{cases} 0, & n \neq m \text{ or } n = m = 0, \\ L, & n = m \ge 1. \end{cases}$$
>   *(Note the sheet erratum: $I_{00} = 0 \neq L$ since $y_0(x) \equiv 0$.)*
> - **Cosine system** $u_n(x) = \cos\left(\frac{n\pi x}{L}\right)$:
>   $$\int_{-L}^{L} u_n(x)u_m(x)\,dx = \begin{cases} 0, & n \neq m, \\ L, & n = m \ge 1, \\ 2L, & n = m = 0. \end{cases}$$
> - **Cross-orthogonality**: $\int_{-L}^{L} y_n(x)u_m(x)\,dx = 0$ for all $m, n \ge 0$.
