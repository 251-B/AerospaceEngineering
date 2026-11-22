---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 6"
dificultad: media
id: "e6"
pill: "Uniqueness • Trigonometric Identities • No Integrals"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.6: Fourier Series via Trigonometric Identities

> Official exercise 6 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Compute the Fourier series of the following functions in $[-\pi, \pi]$:

$$ f(x) = \sin 2x, \qquad f(x) = 2 + 3\cos(2x), \qquad f(x) = \sin(4x), \qquad f(x) = 8\cos^3(3x). $$

Can you compute the Fourier series without using the integral formulas for the coefficients in these cases?

## Classification of the problem

All four functions are smooth, $2\pi$-periodic functions on $[-\pi, \pi]$ ($L = \pi$) that are finite linear combinations of the Fourier basis elements $\{1, \cos(nx), \sin(nx) : n = 1, 2, \dots\}$—in the fourth case after reducing $\cos^3(3x)$ via elementary trigonometric identities (Haberman Sec. 3.2; `Notes09-12-Nov.pdf`, p. 10).

## Method

**Yes**, we can compute every Fourier series here **without evaluating any Euler-Fourier integral**, by appealing to the **uniqueness of the Fourier expansion** on $[-\pi, \pi]$.

Suppose a function $f(x)$ can be written as a finite trigonometric polynomial

$$ f(x) = c_0 + \sum_{k=1}^{N} \big[c_k \cos(kx) + d_k \sin(kx)\big]. $$

If we substitute this finite sum into the Euler-Fourier formulas on $[-\pi, \pi]$,

$$ a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\,dx, \qquad a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(nx)\,dx, \qquad b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin(nx)\,dx, $$

linearity of the integral and the orthogonality relations of $\{1, \cos(nx), \sin(nx)\}$ on $[-\pi, \pi]$ (proved explicitly in [[Problem - Ch6-P7 Orthogonality of Sine and Cosine Systems]]) immediately yield

$$ a_0 = c_0, \qquad a_n = c_n, \qquad b_n = d_n \quad (1 \le n \le N), \qquad a_n = b_n = 0 \quad (n > N). $$

Therefore, any finite linear combination of $\{1, \cos(nx), \sin(nx)\}$ **is its own Fourier series**. Our task is simply to rewrite each given function in that basis and read off the coefficients directly.

## Step-by-step derivation

We examine each of the four functions in turn.

### 1. $f(x) = \sin(2x)$

This function is already a single basis element of the Fourier system $\{1, \cos(nx), \sin(nx)\}$, namely $\sin(nx)$ with $n = 2$ and coefficient $1$.

Matching terms against $a_0 + \sum_{n=1}^{\infty} [a_n\cos(nx) + b_n\sin(nx)]$, we read off

$$ a_0 = 0, \qquad a_n = 0 \;\; (n \ge 1), \qquad b_2 = 1, \qquad b_n = 0 \;\; (n \neq 2). $$

Hence the Fourier series is simply

$$ f(x) = \sin(2x). $$

### 2. $f(x) = 2 + 3\cos(2x)$

This function is already a finite linear combination of the constant basis element $1$ (with coefficient $2$) and the cosine basis element $\cos(2x)$ (with coefficient $3$).

Matching terms against $a_0 + \sum_{n=1}^{\infty} [a_n\cos(nx) + b_n\sin(nx)]$, we read off

$$ a_0 = 2, \qquad a_2 = 3, \qquad a_n = 0 \;\; (n \neq 2), \qquad b_n = 0 \;\; (n \ge 1). $$

Hence the Fourier series is simply

$$ f(x) = 2 + 3\cos(2x). $$

### 3. $f(x) = \sin(4x)$

This function is already the single basis element $\sin(4x)$ ($n = 4$) with coefficient $1$.

Matching terms against the Fourier expansion gives

$$ a_0 = 0, \qquad a_n = 0 \;\; (n \ge 1), \qquad b_4 = 1, \qquad b_n = 0 \;\; (n \neq 4). $$

Hence the Fourier series is simply

$$ f(x) = \sin(4x). $$

### 4. $f(x) = 8\cos^3(3x)$

Because $\cos^3(3x)$ is a third power rather than a linear combination of $\cos(nx)$, we first derive the power-reduction identity for $\cos^3\theta$ step by step.

First we split $\cos^3\theta = \cos^2\theta \cdot \cos\theta$ and replace $\cos^2\theta$ using the half-angle identity $\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$ (which follows from $\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1$).

$$ \cos^3\theta = \cos^2\theta \cdot \cos\theta = \frac{1 + \cos(2\theta)}{2}\cos\theta = \frac{1}{2}\cos\theta + \frac{1}{2}\cos(2\theta)\cos\theta. $$

Next we expand the product $\cos(2\theta)\cos\theta$ using the product-to-sum identity

$$ \cos A \cos B = \frac{1}{2}\big[\cos(A + B) + \cos(A - B)\big], $$

which follows by adding the cosine addition formulas $\cos(A+B) = \cos A\cos B - \sin A\sin B$ and $\cos(A-B) = \cos A\cos B + \sin A\sin B$ and dividing by $2$. Setting $A = 2\theta$ and $B = \theta$ gives

$$ \cos(2\theta)\cos\theta = \frac{1}{2}\big[\cos(2\theta + \theta) + \cos(2\theta - \theta)\big] = \frac{1}{2}\big[\cos(3\theta) + \cos\theta\big]. $$

Substituting this back into our expression for $\cos^3\theta$ and collecting the $\cos\theta$ terms yields

$$ \cos^3\theta = \frac{1}{2}\cos\theta + \frac{1}{2}\cdot\frac{1}{2}\big[\cos(3\theta) + \cos\theta\big] = \left(\frac{1}{2} + \frac{1}{4}\right)\cos\theta + \frac{1}{4}\cos(3\theta) = \frac{3}{4}\cos\theta + \frac{1}{4}\cos(3\theta). $$

Now we substitute $\theta = 3x$ and multiply both sides by $8$:

$$ 8\cos^3(3x) = 8\left(\frac{3}{4}\cos(3x) + \frac{1}{4}\cos(9x)\right) = 6\cos(3x) + 2\cos(9x). $$

This is now a finite linear combination of the Fourier basis functions $\cos(3x)$ and $\cos(9x)$. By uniqueness, we read off the coefficients directly:

$$ a_0 = 0, \qquad a_3 = 6, \qquad a_9 = 2, \qquad a_n = 0 \;\; (n \notin \{3, 9\}), \qquad b_n = 0 \;\; (n \ge 1). $$

Hence the Fourier series is

$$ 8\cos^3(3x) = 6\cos(3x) + 2\cos(9x). $$

## Answers and checks

We verify the fourth identity numerically at two independent test points, and confirm parity and convergence for all four functions:

1. **Test at $x = 0$**:
   - Original function: $8\cos^3(3\cdot 0) = 8\cos^3(0) = 8(1)^3 = 8$.
   - Fourier expansion: $6\cos(0) + 2\cos(0) = 6 + 2 = 8$. Exact match.
2. **Test at $x = \pi/9$**:
   - Original function: $8\cos^3\!\left(3\cdot\frac{\pi}{9}\right) = 8\cos^3\!\left(\frac{\pi}{3}\right) = 8\left(\frac{1}{2}\right)^3 = 8\cdot\frac{1}{8} = 1$.
   - Fourier expansion: $6\cos\!\left(\frac{\pi}{3}\right) + 2\cos(\pi) = 6\left(\frac{1}{2}\right) + 2(-1) = 3 - 2 = 1$. Exact match.
3. **Parity check**: $\sin(2x)$ and $\sin(4x)$ are odd functions (pure sine terms, $a_0 = a_n = 0$); $2 + 3\cos(2x)$ and $8\cos^3(3x)$ are even functions (pure cosine terms, $b_n = 0$). All four are smooth and $2\pi$-periodic, so each Fourier series equals $f(x)$ identically for all $x \in \mathbb{R}$.

> [!result] Key results
> - **Can we avoid the integrals?** **Yes**, because the orthogonal basis $\{1, \cos(nx), \sin(nx)\}$ makes the Fourier expansion of any finite trigonometric polynomial unique: each function is its own Fourier series once expressed as a linear combination of basis terms.
> - $\sin(2x) = \sin(2x)$ ($b_2 = 1$, all other coefficients $0$).
> - $2 + 3\cos(2x) = 2 + 3\cos(2x)$ ($a_0 = 2,\; a_2 = 3$, all other coefficients $0$).
> - $\sin(4x) = \sin(4x)$ ($b_4 = 1$, all other coefficients $0$).
> - $8\cos^3(3x) = 6\cos(3x) + 2\cos(9x)$ ($a_3 = 6,\; a_9 = 2$, all other coefficients $0$).
