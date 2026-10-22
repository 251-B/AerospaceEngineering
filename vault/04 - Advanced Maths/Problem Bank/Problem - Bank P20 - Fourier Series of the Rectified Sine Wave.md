---
materia: Advanced Maths
tema: "Unit 5: Fourier series and their convergence"
bank_id: P20
title: "Fourier series of the full-wave rectified sine |sin x|: coefficients by product-to-sum formulas, uniform convergence with an error bound, and two numerical series"
category: final_problem
archetype: fourier-series-convergence
level: standard
unit: 5
difficulty: 2
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2013_ORD, MATHS_FINALEXAM_2021_ORD_SOL and MATHS_FINALEXAM_2022_ORD_SOL; not an official exercise. Verified with scripts/am_bank/p20.py"
tags:
  - problem-bank
  - final-exam
  - fourier-series
  - cosine-series
  - uniform-convergence
  - numerical-series
---

# Bank P20 — Fourier series of the rectified sine wave

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FINALEXAM_2013_ORD, MATHS_FINALEXAM_2021_ORD_SOL and MATHS_FINALEXAM_2022_ORD_SOL. Method: Haberman, Elementary Applied PDEs (BookPDE's.pdf, unit 5 theory), Sec. 3.2 (Fourier convergence theorem), Sec. 3.3 (Fourier cosine and sine series, even functions) and Sec. 3.4 (continuity of the series and term-by-term differentiation). Every result was checked with SymPy (scripts/am_bank/p20.py).

## Statement

The output voltage of a full-wave rectifier fed with $\sin x$ is the $2\pi$-periodic function

$$
f(x)=\lvert\sin x\rvert,\qquad -\pi<x\le\pi,
$$

extended periodically to $\mathbb R$. Use the convention

$$
f(x)\sim a_0+\sum_{n=1}^{\infty}\big(a_n\cos nx+b_n\sin nx\big),\qquad a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f\,dx,\quad a_n=\frac1\pi\int_{-\pi}^{\pi}f\cos nx\,dx,\quad b_n=\frac1\pi\int_{-\pi}^{\pi}f\sin nx\,dx .
$$

(a) Compute all the Fourier coefficients of $f$, writing out the product-to-sum formula you use. Treat the case $n=1$ separately.

(b) To which function does the series converge, and is the convergence uniform on $\mathbb R$? Justify both answers, and give an $N$ such that the partial sum $S_N$ (all terms with $n\le N$) differs from $f$ by less than $0.035$ everywhere.

(c) Evaluating the series at suitable points, find

$$
S=\sum_{k=1}^{\infty}\frac1{4k^2-1}\qquad\text{and}\qquad T=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{4k^2-1}.
$$

Check the value of $S$ independently with partial fractions.

## Setup

#### Phase 1. Hypotheses and setup

- Data: $f(x)=\lvert\sin x\rvert$ on $(-\pi,\pi]$, period $2L=2\pi$ ($L=\pi$).
- Regularity: $f$ is continuous on $\mathbb R$ (also across $x=\pm\pi$, where $\lvert\sin\pi\rvert=0=\lvert\sin(-\pi)\rvert$), and piecewise smooth: $f'(x)=\cos x$ on $(0,\pi)$ and $-\cos x$ on $(-\pi,0)$, with corners (jumps of $f'$) at $x=k\pi$.
- Symmetry: $f(-x)=\lvert-\sin x\rvert=f(x)$, so $f$ is **even**. In fact $f$ has period $\pi$, which will kill the odd harmonics.

#### Phase 2. Canonical formulation

Even $f$ (Haberman Sec. 3.3): $b_n=0$ and the series is a cosine series with

$$
a_0=\frac1\pi\int_0^{\pi}f\,dx,\qquad a_n=\frac2\pi\int_0^{\pi}f\cos nx\,dx ,
$$

and on $[0,\pi]$, $f(x)=\sin x$.

## (a) Fourier coefficients [1.2 pts]

### Hint

$\sin A\cos B=\tfrac12\big[\sin(A+B)+\sin(A-B)\big]$. Keep $n\pm1$ in the denominators and watch for $n=1$, where $n-1=0$.

### Checkpoint

- $b_n=0$; $a_0=\dfrac2\pi$; $a_1=0$; $a_n=0$ for odd $n\ge3$; $a_{2k}=-\dfrac{4}{\pi(4k^2-1)}$.
- $\lvert\sin x\rvert=\dfrac2\pi-\dfrac4\pi\displaystyle\sum_{k=1}^\infty\frac{\cos2kx}{4k^2-1}=\frac2\pi-\frac4\pi\Big(\frac{\cos2x}{3}+\frac{\cos4x}{15}+\frac{\cos6x}{35}+\cdots\Big)$.

### Solution

#### Step 1. Sine coefficients

$f(x)\sin nx$ is even times odd, i.e. odd, so its integral over the symmetric interval $(-\pi,\pi)$ vanishes: substituting $x=-s$, $dx=-ds$, $\int_{-\pi}^0f(x)\sin nx\,dx=\int_{\pi}^{0}f(s)(-\sin ns)(-ds)=-\int_0^{\pi}f(s)\sin ns\,ds$. Hence $b_n=0$ for all $n$.

#### Step 2. Mean value

$$
a_0=\frac1{2\pi}\int_{-\pi}^{\pi}\lvert\sin x\rvert\,dx=\frac1\pi\int_0^\pi\sin x\,dx=\frac1\pi\big[-\cos x\big]_0^\pi=\frac1\pi\big(-\cos\pi+\cos0\big)=\frac2\pi .
$$

#### Step 3. The case $n=1$

$\sin x\cos x=\tfrac12\sin2x$, so

$$
a_1=\frac2\pi\int_0^\pi\frac{\sin2x}{2}\,dx=\frac1\pi\Big[-\frac{\cos2x}{2}\Big]_0^\pi=\frac1\pi\Big(-\frac{\cos2\pi}2+\frac{\cos0}2\Big)=0 .
$$

#### Step 4. The case $n\ge2$

Product-to-sum with $A=x$, $B=nx$: $\sin x\cos nx=\tfrac12\big[\sin(1+n)x+\sin(1-n)x\big]=\tfrac12\big[\sin(n+1)x-\sin(n-1)x\big]$. For an integer $m\ge1$, with the substitution $s=mx$, $ds=m\,dx$:

$$
\int_0^\pi\sin mx\,dx=\Big[-\frac{\cos mx}{m}\Big]_0^\pi=\frac{1-\cos m\pi}{m}=\frac{1-(-1)^m}{m}.
$$

With $m=n+1$, $1-(-1)^{n+1}=1+(-1)^n$; with $m=n-1\ge1$, $1-(-1)^{n-1}=1+(-1)^n$. Therefore

$$
a_n=\frac2\pi\cdot\frac12\Big[\frac{1+(-1)^n}{n+1}-\frac{1+(-1)^n}{n-1}\Big]=\frac{1+(-1)^n}{\pi}\cdot\frac{(n-1)-(n+1)}{n^2-1}=-\frac{2\big(1+(-1)^n\big)}{\pi(n^2-1)} .
$$

- $n$ odd: $1+(-1)^n=0$, so $a_n=0$ (consistent with Step 3 and with the period $\pi$ of $f$).
- $n=2k$ even: $1+(-1)^n=2$ and $n^2-1=4k^2-1$, so $a_{2k}=-\dfrac{4}{\pi(4k^2-1)}$.

#### Step 5. The series

$$
\lvert\sin x\rvert\sim\frac2\pi-\frac4\pi\sum_{k=1}^\infty\frac{\cos2kx}{4k^2-1}.
$$

First terms: $a_2=-\frac4{3\pi}$, $a_4=-\frac4{15\pi}$, $a_6=-\frac4{35\pi}$.

## (b) Convergence [0.6 pts]

### Hint

Apply the Fourier convergence theorem, then bound the tail of the series with $\lvert\cos2kx\rvert\le1$; the tail telescopes.

### Checkpoint

- The series converges to $\lvert\sin x\rvert$ at **every** $x\in\mathbb R$ (no jumps), and the convergence is uniform.
- $\sup_x\lvert f-S_{2N}\rvert\le\dfrac4\pi\displaystyle\sum_{k>N}\frac1{4k^2-1}=\frac{2}{\pi(2N+1)}$; any $N\ge18$ works; $N=18$ (terms up to $\cos18x$) gives $\le\dfrac{2}{19\pi}\approx0.0335<0.035$.

### Solution

#### Step 1. Pointwise limit

$f$ is piecewise smooth on $[-\pi,\pi]$, so by the Fourier convergence theorem (Haberman Sec. 3.2) its series converges at each $x$ to $\tfrac12\big[f(x^+)+f(x^-)\big]$ of the periodic extension. The periodic extension of $\lvert\sin x\rvert$ is $\lvert\sin x\rvert$ itself on all of $\mathbb R$, which is continuous, so the average equals $f(x)$: the series converges to $\lvert\sin x\rvert$ everywhere, including the corners $x=k\pi$. There is no Gibbs overshoot (Haberman Sec. 3.3: a continuous, piecewise smooth periodic extension gives a continuous limit).

#### Step 2. Uniform convergence

For all $x$, $\Big\lvert\dfrac{\cos2kx}{4k^2-1}\Big\rvert\le\dfrac{1}{4k^2-1}=M_k$ and $\sum M_k<\infty$ (it behaves like $\sum\frac1{4k^2}$). By the Weierstrass M-test the series converges absolutely and uniformly on $\mathbb R$ (equivalently, Haberman Sec. 3.4: a continuous periodic extension with piecewise smooth derivative has a uniformly convergent Fourier series).

#### Step 3. Error bound

Partial fractions: $\dfrac{1}{4k^2-1}=\dfrac{1}{(2k-1)(2k+1)}=\dfrac12\Big(\dfrac1{2k-1}-\dfrac1{2k+1}\Big)$ (check: $\frac12\cdot\frac{(2k+1)-(2k-1)}{(2k-1)(2k+1)}=\frac{1}{4k^2-1}$). The tail telescopes:

$$
\sum_{k=K+1}^{\infty}\frac{1}{4k^2-1}=\frac12\Big[\Big(\frac1{2K+1}-\frac1{2K+3}\Big)+\Big(\frac1{2K+3}-\frac1{2K+5}\Big)+\cdots\Big]=\frac{1}{2(2K+1)} .
$$

The partial sum with all harmonics $n\le N=2K$ keeps the terms $k\le K$, so

$$
\lvert f(x)-S_{2K}(x)\rvert\le\frac4\pi\sum_{k>K}\frac1{4k^2-1}=\frac{2}{\pi(2K+1)}\quad\text{for all }x .
$$

$\frac{2}{\pi(2K+1)}<0.035\iff2K+1>\frac{2}{0.035\pi}=18.19\iff K\ge9$. $K=9$ ($N=18$) already gives $\frac2{19\pi}=0.0335$; with $K=10$ ($N=20$) the bound is $\frac{2}{21\pi}\approx0.0303$. Any $N\ge18$ works. The bound is attained at $x=0$, where every cosine equals $1$.

## (c) Two numerical series [0.7 pts]

### Hint

At $x=0$ every $\cos2kx=1$; at $x=\pi/2$, $\cos(2k\cdot\pi/2)=\cos k\pi=(-1)^k$.

### Checkpoint

- $x=0$: $S=\dfrac12$.
- $x=\pi/2$: $T=\dfrac{\pi-2}{4}\approx0.2854$.
- Partial sums $S_K=\dfrac12-\dfrac1{2(2K+1)}\to\dfrac12$.

### Solution

#### Step 1. At $x=0$

By (b) the series equals $f(0)=\lvert\sin0\rvert=0$ there:

$$
0=\frac2\pi-\frac4\pi\sum_{k=1}^\infty\frac{1}{4k^2-1}\ \Longrightarrow\ S=\frac{2/\pi}{4/\pi}=\frac12 .
$$

#### Step 2. At $x=\pi/2$

$f(\pi/2)=1$ and $\cos(k\pi)=(-1)^k$:

$$
1=\frac2\pi-\frac4\pi\sum_{k=1}^\infty\frac{(-1)^k}{4k^2-1}=\frac2\pi+\frac4\pi\sum_{k=1}^\infty\frac{(-1)^{k+1}}{4k^2-1}=\frac2\pi+\frac4\pi\,T .
$$

So $T=\dfrac\pi4\Big(1-\dfrac2\pi\Big)=\dfrac{\pi-2}{4}\approx0.2854$. Check with the first terms: $\frac13-\frac1{15}+\frac1{35}-\frac1{63}=0.2794$, approaching $0.2854$ with alternating error smaller than the next term $\frac1{99}$.

#### Step 3. Independent check of $S$

From the telescoping of (b), Step 3, with $K=0$: the partial sum is $S_K=\sum_{k=1}^K\frac1{4k^2-1}=\frac12\Big(1-\frac1{2K+1}\Big)=\frac12-\frac{1}{2(2K+1)}$, so $S=\lim_{K\to\infty}S_K=\frac12$, the same value as in Step 1.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** the coefficients decay like $1/n^2$, the rate expected for a continuous function with a jump in its derivative (a function with jumps would give $1/n$); the mean value $a_0=2/\pi\approx0.637$ is the DC output of the rectifier, the classical result for a full-wave rectifier of unit amplitude.
- **Checks:** every coefficient by direct integration over $(-\pi,0)$ and $(0,\pi)$ (script, $n\le11$); the series at $x=0.7$ and $x=-2.5$ matches $\lvert\sin x\rvert$; Parseval's identity (extension: $\frac1\pi\int_{-\pi}^{\pi}f^2dx=2a_0^2+\sum a_n^2$ in this convention) gives $\sum\frac{1}{(4k^2-1)^2}=\frac{\pi^2-8}{16}$, also checked. Term-by-term differentiation (Haberman Sec. 3.4) is allowed because $f$ is continuous and periodic: the derived series $\frac8\pi\sum\frac{k\sin2kx}{4k^2-1}$ converges to $f'$, and to $0$ (the average of the jump $\pm1$) at $x=k\pi$.
- **Common mistakes in the exam:** (1) using the formula for $a_n$ with $n=1$, which divides by $n-1=0$; (2) integrating $\sin x\cos nx$ over $(-\pi,\pi)$ without the absolute value, which gives $a_n=0$ for all $n$; (3) mixing conventions: with $\frac{a_0}{2}$ in front, $a_0=\frac4\pi$, not $\frac2\pi$; (4) claiming only "convergence in the mean" or a Gibbs overshoot at $x=0$: the extension is continuous, so convergence is uniform.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
