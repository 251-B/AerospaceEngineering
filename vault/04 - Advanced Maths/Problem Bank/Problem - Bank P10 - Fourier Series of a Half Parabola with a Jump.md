---
materia: Advanced Maths
tema: "Unit 5: Fourier series and pointwise convergence"
bank_id: P10
title: "Full Fourier series on (-pi, pi) of the function equal to 0 on the left half and x^2 on the right half: coefficients, Dirichlet values and two numerical series"
category: midterm_2_problem
archetype: fourier-series-convergence
level: standard
unit: 5
difficulty: 2
points: 5.0
time_minutes: 45
official: false
origen: "Problem written for the bank in the style of MATHS_SECONDPARTIAL_2019_MT3_SOL and MATHS_SECONDPARTIAL_2021_G45_SOL; not an official exercise. Verified with scripts/am_bank/p10.py"
tags:
  - problem-bank
  - midterm-2
  - fourier-series
  - dirichlet-theorem
  - integration-by-parts
  - numerical-series
---

# Bank P10 — Fourier series of a half parabola with a jump

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_SECONDPARTIAL_2019_MT3_SOL and MATHS_SECONDPARTIAL_2021_G45_SOL. Method: Unit 5 notes (BookPDE's.pdf): full Fourier series on $(-\pi,\pi)$, Euler formulas for the coefficients, and the Dirichlet pointwise convergence theorem for piecewise smooth functions. Every result was checked with SymPy (scripts/am_bank/p10.py).

## Statement

Let $f$ be defined on $(-\pi,\pi)$ by

$$f(x)=\begin{cases}0,&-\pi<x<0,\\ x^2,&0\le x<\pi,\end{cases}$$

and extended to $\mathbb R$ as a $2\pi$-periodic function.

(a) Describe the graph of the periodic extension on $[-3\pi,3\pi]$: where is it continuous, where does it jump and by how much? Is $f$ piecewise smooth?

(b) Compute the Fourier series $\dfrac{a_0}{2}+\displaystyle\sum_{n\ge1}\big(a_n\cos nx+b_n\sin nx\big)$ of $f$.

(c) Using the Dirichlet theorem, give the sum of the series at $x=0$, $x=\pi$, $x=-\pi$, $x=\pi/2$ and $x=-\pi/2$.

(d) Deduce the sums of $\displaystyle\sum_{n=1}^\infty\frac{1}{n^2}$ and $\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n^2}$, and check that the two results are consistent with each other.

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns: the coefficients $a_0$, $a_n$, $b_n$ ($n\ge1$). Independent variable $x\in\mathbb R$, period $2\pi$ ($L=\pi$).
- $f$ is bounded, and on each of $(-\pi,0)$ and $(0,\pi)$ it is a polynomial: $f$ and $f'$ are piecewise continuous, so $f$ is piecewise smooth and the Dirichlet theorem applies.
- No symmetry: $f$ is neither even nor odd, so both $a_n$ and $b_n$ are needed. Since $f=0$ on $(-\pi,0)$, every integral reduces to $(0,\pi)$.

#### Phase 2. Canonical formulation

Euler formulas on $(-\pi,\pi)$:

$$a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx\ (n\ge0),\qquad b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx\ (n\ge1).$$

Dirichlet theorem: for a piecewise smooth $2\pi$-periodic $f$, the series converges at every $x$ to $\tfrac12\big[f(x^+)+f(x^-)\big]$.

## (a) Periodic extension, continuity and jumps [1.0 pts]

### Hint

Compare the one-sided limits at $x=0$ and at $x=\pm\pi$, and repeat with period $2\pi$.

### Checkpoint

- On each period: zero on $(-\pi,0)$, the parabola arc $x^2$ from $0$ up to $\pi^2$ on $(0,\pi)$.
- Continuous at $x=2k\pi$ ($f(0^-)=f(0^+)=0$, and even $f'(0^\pm)=0$).
- Jumps at $x=(2k+1)\pi$: $f(\pi^-)=\pi^2$, $f(\pi^+)=0$, jump of size $-\pi^2$.
- Piecewise smooth: yes.

### Solution

#### Step 1. One period

On $(-\pi,0)$ the graph is the segment $y=0$; on $[0,\pi)$ it is the arc of $y=x^2$, rising from $(0,0)$ to height $\pi^2$ as $x\to\pi^-$.

#### Step 2. Continuity at the origin

$f(0^-)=0$, $f(0^+)=0^2=0$: continuous. The one-sided derivatives are $0$ (left) and $2\cdot0=0$ (right): the graph even has no corner at $x=0$; only $f''$ jumps there (from $0$ to $2$).

#### Step 3. Jumps at the odd multiples of pi

The extension satisfies $f(x+2\pi)=f(x)$. At $x=\pi$: $f(\pi^-)=\lim_{x\to\pi^-}x^2=\pi^2$, while $f(\pi^+)=f(-\pi^+)=0$. So the extension jumps down by $\pi^2$ at $x=\pm\pi,\pm3\pi$. The graph on $[-3\pi,3\pi]$ is three copies of the period: flat on $(-3\pi,-2\pi)$, arc on $(-2\pi,-\pi)$, flat on $(-\pi,0)$, arc on $(0,\pi)$, flat on $(\pi,2\pi)$, arc on $(2\pi,3\pi)$, with a vertical drop from $\pi^2$ to $0$ at each odd multiple of $\pi$.

## (b) Fourier coefficients [2.0 pts]

### Hint

Integrate by parts twice for $\int x^2\cos nx\,dx$ and $\int x^2\sin nx\,dx$. Use $\sin n\pi=0$ and $\cos n\pi=(-1)^n$.

### Checkpoint

- $a_0=\dfrac{\pi^2}{3}$ (so the constant term is $\dfrac{\pi^2}{6}$).
- $a_n=\dfrac{2(-1)^n}{n^2}$: $a_1=-2$, $a_2=\tfrac12$, $a_3=-\tfrac29$.
- $b_n=\dfrac{(-1)^{n+1}\pi}{n}+\dfrac{2\big((-1)^n-1\big)}{\pi n^3}$: $b_n=\dfrac{\pi}{n}-\dfrac{4}{\pi n^3}$ for $n$ odd, $b_n=-\dfrac{\pi}{n}$ for $n$ even.

### Solution

#### Step 1. Mean value

$$a_0=\frac1\pi\int_0^\pi x^2\,dx=\frac1\pi\Big[\frac{x^3}{3}\Big]_0^\pi=\frac1\pi\cdot\frac{\pi^3}{3}=\frac{\pi^2}{3}.$$

#### Step 2. Two auxiliary integrals ($n\ge1$)

By parts with $u=x$, $dv=\sin nx\,dx$, $du=dx$, $v=-\frac{\cos nx}{n}$:

$$\int x\sin nx\,dx=-\frac{x\cos nx}{n}+\frac1n\int\cos nx\,dx=-\frac{x\cos nx}{n}+\frac{\sin nx}{n^2}.$$

By parts with $u=x$, $dv=\cos nx\,dx$, $du=dx$, $v=\frac{\sin nx}{n}$:

$$\int x\cos nx\,dx=\frac{x\sin nx}{n}-\frac1n\int\sin nx\,dx=\frac{x\sin nx}{n}+\frac{\cos nx}{n^2}.$$

#### Step 3. Cosine coefficients

By parts with $u=x^2$, $dv=\cos nx\,dx$, $du=2x\,dx$, $v=\frac{\sin nx}{n}$, and then Step 2:

$$\int x^2\cos nx\,dx=\frac{x^2\sin nx}{n}-\frac2n\int x\sin nx\,dx=\frac{x^2\sin nx}{n}+\frac{2x\cos nx}{n^2}-\frac{2\sin nx}{n^3}.$$

Barrow's rule on $[0,\pi]$, with $\sin n\pi=\sin0=0$ and $\cos n\pi=(-1)^n$:

$$\int_0^\pi x^2\cos nx\,dx=\Big[0+\frac{2\pi(-1)^n}{n^2}-0\Big]-\Big[0+0-0\Big]=\frac{2\pi(-1)^n}{n^2},\qquad a_n=\frac{2(-1)^n}{n^2}.$$

#### Step 4. Sine coefficients

By parts with $u=x^2$, $dv=\sin nx\,dx$, $du=2x\,dx$, $v=-\frac{\cos nx}{n}$, and then Step 2:

$$\int x^2\sin nx\,dx=-\frac{x^2\cos nx}{n}+\frac2n\int x\cos nx\,dx=-\frac{x^2\cos nx}{n}+\frac{2x\sin nx}{n^2}+\frac{2\cos nx}{n^3}.$$

Barrow's rule on $[0,\pi]$:

$$\int_0^\pi x^2\sin nx\,dx=\Big[-\frac{\pi^2(-1)^n}{n}+0+\frac{2(-1)^n}{n^3}\Big]-\Big[0+0+\frac{2}{n^3}\Big]=-\frac{\pi^2(-1)^n}{n}+\frac{2\big((-1)^n-1\big)}{n^3}.$$

Dividing by $\pi$:

$$b_n=\frac{(-1)^{n+1}\pi}{n}+\frac{2\big((-1)^n-1\big)}{\pi n^3}=\begin{cases}\dfrac{\pi}{n}-\dfrac{4}{\pi n^3},&n\text{ odd},\\[2mm] -\dfrac{\pi}{n},&n\text{ even}.\end{cases}$$

#### Step 5. The series

$$f(x)\sim\frac{\pi^2}{6}+\sum_{n=1}^\infty\left[\frac{2(-1)^n}{n^2}\cos nx+\left(\frac{(-1)^{n+1}\pi}{n}+\frac{2\big((-1)^n-1\big)}{\pi n^3}\right)\sin nx\right].$$

First terms: $\frac{\pi^2}{6}-2\cos x+\big(\pi-\frac4\pi\big)\sin x+\frac12\cos2x-\frac\pi2\sin2x-\frac29\cos3x+\dots$

## (c) Values of the series by the Dirichlet theorem [1.0 pts]

### Hint

At a point of continuity the series gives $f(x)$; at a jump, the midpoint of the jump.

### Checkpoint

- $x=0$: $0$. $\ x=\pm\pi$: $\dfrac{\pi^2}{2}$. $\ x=\pi/2$: $\dfrac{\pi^2}{4}$. $\ x=-\pi/2$: $0$.

### Solution

#### Step 1. Points of continuity

$x=0$: $f$ is continuous there, sum $f(0)=0$. $x=\pi/2$: inside $(0,\pi)$, sum $(\pi/2)^2=\pi^2/4$. $x=-\pi/2$: inside $(-\pi,0)$, sum $0$.

#### Step 2. The endpoints are jump points

For the periodic extension, $x=\pi$ and $x=-\pi$ are the same kind of point: $f(\pi^-)=\pi^2$, $f(\pi^+)=f(-\pi^+)=0$. The series converges to

$$\frac{f(\pi^+)+f(\pi^-)}{2}=\frac{0+\pi^2}{2}=\frac{\pi^2}{2},$$

the same value at $x=-\pi$ (each term is $2\pi$-periodic, so the series takes equal values at $\pm\pi$). It is not $f(\pi)$ of either formula: the series does not "choose" a side.

## (d) Two numerical series [1.0 pts]

### Hint

At $x=0$ and $x=\pi$ every $\sin nx$ vanishes, and $\cos n\pi=(-1)^n$.

### Checkpoint

- $x=0$: $0=\dfrac{\pi^2}{6}+2\displaystyle\sum\frac{(-1)^n}{n^2}$, so $\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n^2}=\frac{\pi^2}{12}$.
- $x=\pi$: $\dfrac{\pi^2}{2}=\dfrac{\pi^2}{6}+2\displaystyle\sum\frac{1}{n^2}$, so $\displaystyle\sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi^2}{6}$.
- Consistency: $\dfrac{\pi^2}{6}-\dfrac{\pi^2}{12}=2\displaystyle\sum_{n\text{ even}}\frac1{n^2}=\frac12\cdot\frac{\pi^2}{6}$.

### Solution

#### Step 1. Evaluation at x = 0

$\cos0=1$, $\sin0=0$, and by (c) the sum is $0$:

$$0=\frac{\pi^2}{6}+\sum_{n=1}^\infty\frac{2(-1)^n}{n^2}\ \Longrightarrow\ \sum_{n=1}^\infty\frac{(-1)^n}{n^2}=-\frac{\pi^2}{12}\ \Longrightarrow\ \sum_{n=1}^\infty\frac{(-1)^{n+1}}{n^2}=1-\frac14+\frac19-\dots=\frac{\pi^2}{12}.$$

#### Step 2. Evaluation at x = pi

$\cos n\pi=(-1)^n$, $\sin n\pi=0$, and by (c) the sum is $\pi^2/2$:

$$\frac{\pi^2}{2}=\frac{\pi^2}{6}+\sum_{n=1}^\infty\frac{2(-1)^n(-1)^n}{n^2}=\frac{\pi^2}{6}+2\sum_{n=1}^\infty\frac1{n^2}\ \Longrightarrow\ \sum_{n=1}^\infty\frac1{n^2}=\frac12\Big(\frac{\pi^2}{2}-\frac{\pi^2}{6}\Big)=\frac{\pi^2}{6}.$$

#### Step 3. Consistency check

Subtracting the two series, the odd terms cancel and the even ones double: $\sum\frac1{n^2}-\sum\frac{(-1)^{n+1}}{n^2}=2\sum_{m\ge1}\frac{1}{(2m)^2}=\frac12\sum_{m\ge1}\frac1{m^2}$. With the values found: $\frac{\pi^2}{6}-\frac{\pi^2}{12}=\frac{\pi^2}{12}$ and $\frac12\cdot\frac{\pi^2}{6}=\frac{\pi^2}{12}$. They agree.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $a_n=O(1/n^2)$ because $f$ is continuous at $0$, while $b_n\sim(-1)^{n+1}\pi/n$ decays only like $1/n$: that slow part is produced by the jump of size $\pi^2$ at $x=\pm\pi$ (a jump of size $J$ at $x=\pi$ always gives a contribution $\frac{J}{\pi}\frac{(-1)^{n}}{n}$ with $J=-\pi^2$ here). Near the jump the partial sums overshoot by about 9% of the jump (Gibbs phenomenon, **extension**: the overshoot of partial sums near a jump, which does not vanish as $N\to\infty$).
- **Checks:** the antiderivatives of Steps 3 and 4 give back $x^2\cos nx$ and $x^2\sin nx$ when differentiated; partial sums with 4000 terms reproduce $0$ at $x=0$, $\pi^2/2$ at $x=\pi$ and $\pi^2/4$ at $x=\pi/2$ to $10^{-3}$; the mean value $a_0/2=\pi^2/6$ equals $\frac{1}{2\pi}\int_{-\pi}^{\pi}f\,dx$.
- **Common mistakes in the exam:** (1) dividing by $2\pi$ instead of $\pi$ in $a_n$, or forgetting that the constant term is $a_0/2$; (2) evaluating the series at $x=\pi$ as $f(\pi^-)=\pi^2$ instead of the midpoint $\pi^2/2$, which gives $\sum1/n^2=5\pi^2/12$ (wrong); (3) dropping the term $2((-1)^n-1)/(\pi n^3)$ of $b_n$, which only lives on odd $n$; (4) treating $f$ as even or odd and discarding one family of coefficients.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
