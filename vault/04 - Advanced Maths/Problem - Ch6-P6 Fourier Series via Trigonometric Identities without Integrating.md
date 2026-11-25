---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 6"
dificultad: media
id: "e6"
pill: "Series from identities"
tags:
  - problema-resuelto
  - fourier-series
  - orthogonality
---

# Problem 6.6: Fourier Series via Trigonometric Identities without Integrating

> Official exercise 6 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Compute the Fourier series of the following functions in $[-\pi,\pi]$: $f(x)=\sin2x$, $f(x)=2+3\cos(2x)$, $f(x)=\sin(4x)$, $f(x)=8\cos^3(3x)$. Can you compute the Fourier series without using the integral formulas for the coefficients in these cases?

## Why the Answer Is Yes: Uniqueness of the Coefficients

On $[-\pi,\pi]$ ($L=\pi$) the series is $a_0+\sum_{n\ge1}(a_n\cos nx+b_n\sin nx)$ with the coefficient formulas of [[Problem - Ch6-P5 Fourier Series of Nine Functions]]. The orthogonality relations proved in [[Problem - Ch6-P7 Orthogonality Relations of Sine and Cosine Families]] say that $\{1,\cos nx,\sin nx\}$ is an orthogonal family with $\int_{-\pi}^{\pi}\cos^2nx\,dx=\int_{-\pi}^{\pi}\sin^2nx\,dx=\pi$, $\int_{-\pi}^{\pi}1\,dx=2\pi$.

Suppose $f$ is already a **finite trigonometric polynomial**, $f=c_0+\sum_{n=1}^{N}(\alpha_n\cos nx+\beta_n\sin nx)$. Insert it in $a_m=\frac1\pi\int f\cos mx\,dx$. By linearity and orthogonality every term vanishes except the one containing $\cos mx$, which gives $\frac1\pi\cdot\alpha_m\cdot\pi=\alpha_m$. The same argument gives $b_m=\beta_m$ and $a_0=c_0$ (the sum is finite, so integrating term by term is legitimate). Hence the Fourier coefficients of a trigonometric polynomial are the coefficients with which it is written, and the series is the polynomial itself: the only work is to rewrite $f$ as a combination of $1$, $\cos nx$, $\sin nx$ (Haberman, Sec. 3.3).

## Reading Off the Coefficients

| Function | Rewriting | Non-zero coefficients |
| :--- | :--- | :--- |
| $\sin2x$ | already a basis function | $b_2=1$ |
| $2+3\cos2x$ | already a combination | $a_0=2$, $a_2=3$ |
| $\sin4x$ | already a basis function | $b_4=1$ |
| $8\cos^3 3x$ | product identity below | $a_3=6$, $a_9=2$ |

All other $a_n$, $b_n$ vanish, so each series is a single finite sum.

## Expanding $8\cos^3(3x)$

> [!info] Lemma: $\cos^3\theta=\dfrac{3\cos\theta+\cos3\theta}{4}$
> **Via Euler.** $\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2}$, so
> $$\cos^3\theta=\frac{1}{8}\left(e^{3i\theta}+3e^{i\theta}+3e^{-i\theta}+e^{-3i\theta}\right)=\frac18\left(2\cos3\theta+6\cos\theta\right)=\frac{\cos3\theta+3\cos\theta}{4}.$$
> **Via addition formulas.** $\cos3\theta=\cos(2\theta+\theta)=\cos2\theta\cos\theta-\sin2\theta\sin\theta=(2\cos^2\theta-1)\cos\theta-2\sin^2\theta\cos\theta=(2\cos^2\theta-1)\cos\theta-2(1-\cos^2\theta)\cos\theta=4\cos^3\theta-3\cos\theta$, which gives the same identity.

With $\theta=3x$:

$$8\cos^3(3x)=8\cdot\frac{3\cos3x+\cos9x}{4}=6\cos3x+2\cos9x .$$

## Fourier Series and Checks

$$\sin2x\sim\sin2x,\qquad 2+3\cos2x\sim2+3\cos2x,\qquad\sin4x\sim\sin4x,\qquad 8\cos^3(3x)\sim6\cos3x+2\cos9x .$$

All four functions are continuous and $2\pi$-periodic, so the series converge to $f$ at every point (here trivially, being finite sums).

> [!result] Check by the integral formula (one case)
> $a_3=\frac1\pi\int_{-\pi}^{\pi}8\cos^3(3x)\cos3x\,dx=\frac1\pi\int_{-\pi}^{\pi}(6\cos3x+2\cos9x)\cos3x\,dx=\frac1\pi\left[6\pi+2\cdot0\right]=6$, using $\int_{-\pi}^\pi\cos^23x\,dx=\pi$ and $\int_{-\pi}^\pi\cos9x\cos3x\,dx=0$. Mean value: $a_0=\frac1{2\pi}\int 8\cos^3 3x\,dx=0$, consistent with no constant term. Spot check at $x=0$: $8\cos^30=8$ and $6+2=8$.
