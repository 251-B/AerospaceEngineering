---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 9"
dificultad: media
id: "e9"
pill: "Even and odd series"
tags:
  - problema-resuelto
  - fourier-series
  - symmetry
---

# Problem 6.9: Fourier Series of Even and Odd Periodic Functions

> Official exercise 9 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

What can we say about the Fourier series on $[-L,L]$ of a function $f(x)$ that is $2L$ periodic and even, that is, satisfies $f(-x)=f(x)$ for $x\in\mathbb R$? And if $f(x)$ is $2L$ periodic and odd, $f(-x)=-f(x)$?

## Period, Symmetry and Coefficient Formulas

With $k=\frac{n\pi}{L}$: $a_0=\frac1{2L}\int_{-L}^{L}f\,dx$, $a_n=\frac1L\int_{-L}^{L}f\cos kx\,dx$, $b_n=\frac1L\int_{-L}^{L}f\sin kx\,dx$ (Haberman, Sec. 3.4). Parities of the basis: $\cos kx$ is even and $\sin kx$ is odd, because $\cos(-kx)=\cos kx$ and $\sin(-kx)=-\sin kx$. Products: even$\cdot$even and odd$\cdot$odd are even; even$\cdot$odd is odd.

> [!info] Lemma
> Let $g$ be integrable on $[-L,L]$. Split $\int_{-L}^{L}g=\int_{-L}^{0}g+\int_0^Lg$ and substitute $u=-x$, $du=-dx$ in the first piece; the limits $x=-L\to0$ become $u=L\to0$:
> $$\int_{-L}^{0}g(x)\,dx=\int_{L}^{0}g(-u)(-du)=\int_0^Lg(-u)\,du.$$
> Hence $\int_{-L}^{L}g=\int_0^L\left[g(x)+g(-x)\right]dx$. If $g$ is even this equals $2\int_0^Lg$; if $g$ is odd the bracket is $0$ and $\int_{-L}^{L}g=0$.

## Step-by-Step Result

### Even $f$

$f\cos kx$ is even (even$\cdot$even), so $a_n=\frac2L\int_0^Lf\cos kx\,dx$ and $a_0=\frac1L\int_0^Lf\,dx$. $f\sin kx$ is odd, so $b_n=0$ for all $n$. The series is a **cosine series**:

$$f(x)\sim a_0+\sum_{n=1}^{\infty}a_n\cos\frac{n\pi x}{L}.$$

### Odd $f$

$f\cos kx$ is odd, so $a_n=0$ and $a_0=0$ (the integrand $f$ is odd). $f\sin kx$ is even, so $b_n=\frac2L\int_0^Lf\sin kx\,dx$. The series is a **sine series**:

$$f(x)\sim\sum_{n=1}^{\infty}b_n\sin\frac{n\pi x}{L}.$$

## Fourier Series, Convergence and Checks

> [!result] Answer
> A $2L$-periodic even function has only cosines (and a constant); an odd one has only sines. Coefficients need integration over $[0,L]$ only, doubled.

Parity of derivatives and integrals (chain rule): if $f$ is even, differentiate $f(-x)=f(x)$: $-f'(-x)=f'(x)$, so $f'$ is odd; if $f$ is odd, $-f'(-x)=-f'(x)$, so $f'$ is even. For $F(x)=\int_0^xf(s)ds$, substitution $s=-t$ gives $F(-x)=\int_0^{-x}f(s)ds=-\int_0^{x}f(-t)dt$, so $F$ is odd when $f$ is even and even when $f$ is odd. This explains why term-by-term differentiation of a cosine series gives a sine series and conversely.

> [!warning] Endpoint conditions
> If $f$ is **odd and continuous** at $0$, then $f(0)=-f(0)$, so $f(0)=0$; by $2L$-periodicity $f(L)=f(-L)=-f(L)$, so $f(L)=0$ (and $f(\pm L)=0$). If $f$ has a jump there, the series converges to the average $\tfrac12[f(0^+)+f(0^-)]=0$ (and $0$ at $\pm L$), matching the vanishing of every $\sin\frac{n\pi x}L$. For an even $f$, $f(L)=f(-L)$ holds automatically, so the periodic extension has no jump at $\pm L$; if $f$ is also differentiable, $f'$ is odd, hence $f'(0)=f'(L)=0$ (flat ends), compatible with $\cos$ having zero slope there.

Examples in this chapter: $|x|$ and $x^2$ (cosine series) and $x$ (sine series) in [[Problem - Ch6-P5 Fourier Series of Nine Functions]]; $x^2$ with general $L$ in [[Problem - Ch6-P8 Sketching Fourier Series and Periodic Extensions]]. The relation to half-range expansions is the same lemma: extend a function given on $[0,L]$ evenly (cosine series) or oddly (sine series).
