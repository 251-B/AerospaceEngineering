---
materia: Advanced Maths
tema: "Unit 5: Fourier series and their convergence"
bank_id: P11
title: "Half-range sine and cosine series of f(x) = x^2 on (0, pi): continuity of the extensions, decay of the coefficients, values of the series and three numerical sums"
category: midterm_2_problem
archetype: fourier-series-convergence
level: standard
unit: 5
difficulty: 2
points: 5.0
time_minutes: 45
official: false
origen: "Problem written for the bank in the style of MATHS_SECONDPARTIAL_2020_G45_SOL, MATHS_SECONDPARTIAL_2025_G47_SOL; not an official exercise. Verified with scripts/am_bank/p11.py"
tags:
  - problem-bank
  - midterm-2
  - fourier-series
  - half-range-expansion
  - convergence-theorem
  - integration-by-parts
  - numerical-series
---

# Bank P11 — Sine and cosine series of x squared

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the second midterm papers (MATHS_SECONDPARTIAL_2020_G45_SOL, MATHS_SECONDPARTIAL_2025_G47_SOL). Method: Haberman, *Elementary Applied PDEs* (unit 5 text, `BookPDE's.pdf`), Sec. 3.2 (convergence theorem), Sec. 3.3 (Fourier cosine and sine series) and Sec. 3.4 (term-by-term differentiation and continuity of the extension). Every result was checked with SymPy (scripts/am_bank/p11.py).

## Statement

Let $f(x)=x^2$ for $0<x<\pi$.

(a) Compute the Fourier **sine** series of $f$ on $(0,\pi)$, writing every integration by parts. Give $b_n$ separately for odd and even $n$.

(b) Compute the Fourier **cosine** series of $f$ on $(0,\pi)$.

(c) Which of the two periodic extensions (odd or even, of period $2\pi$) is continuous on $\mathbb R$? Explain why this decides how fast the coefficients of (a) and (b) decay. Then give, with justification, the value of **each** series at $x=\pi$, $x=-\pi/2$ and $x=5\pi/2$.

(d) Use the series to obtain
$$\sum_{n=1}^{\infty}\frac{1}{n^2},\qquad \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2},\qquad \sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^3}=1-\frac1{27}+\frac1{125}-\cdots$$
You may use the Leibniz sum $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}=\frac{\pi}{4}$.

## Setup

#### Phase 1. Hypotheses and setup

- Data: $f(x)=x^2$ on the half-period $(0,L)$ with $L=\pi$. $f$ is smooth on $[0,\pi]$ with $f(0)=0$, $f(\pi)=\pi^2$, $f'(x)=2x$, so $f'(0)=0$, $f'(\pi)=2\pi$.
- Unknowns: the coefficients $b_n$ (sine series) and $a_0,a_n$ (cosine series), and the pointwise sums of both series on all of $\mathbb R$.
- Regularity: $f$ and $f'$ are continuous on $[0,\pi]$, so both extensions are piecewise smooth and the convergence theorem (Haberman Sec. 3.2) applies: each series converges to the extension where it is continuous and to the average of the side limits at a jump.

#### Phase 2. Canonical formulation

With $L=\pi$ (Haberman Sec. 3.3):
$$f(x)\sim\sum_{n=1}^{\infty}b_n\sin nx,\qquad b_n=\frac{2}{\pi}\int_0^{\pi}x^2\sin nx\,dx$$
$$f(x)\sim\frac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos nx,\qquad a_n=\frac{2}{\pi}\int_0^{\pi}x^2\cos nx\,dx\quad(n\ge 0)$$
The sine series represents the **odd** $2\pi$-periodic extension $f_o$ of $f$; the cosine series represents the **even** $2\pi$-periodic extension $f_e$.

## (a) Compute the Fourier sine series of f on (0, pi) [1.5 pts]

### Hint

Integrate by parts twice, always differentiating the power of $x$. Use $\cos n\pi=(-1)^n$ and $\sin n\pi=0$.

### Checkpoint

- $\displaystyle b_n=\frac{2\pi(-1)^{n+1}}{n}+\frac{4\big((-1)^n-1\big)}{\pi n^3}$.
- Odd $n$: $b_n=\dfrac{2\pi}{n}-\dfrac{8}{\pi n^3}$; even $n$: $b_n=-\dfrac{2\pi}{n}$. For example $b_1=2\pi-\dfrac8\pi$, $b_2=-\pi$.
- $\displaystyle x^2=\sum_{n=1}^{\infty}\Big[\frac{2\pi(-1)^{n+1}}{n}+\frac{4((-1)^n-1)}{\pi n^3}\Big]\sin nx$ for $0<x<\pi$.

### Solution

#### Step 1. First integration by parts

Take $u=x^2$, $dv=\sin nx\,dx$, so $du=2x\,dx$, $v=-\dfrac{\cos nx}{n}$:
$$\int x^2\sin nx\,dx=-\frac{x^2\cos nx}{n}+\frac{2}{n}\int x\cos nx\,dx$$

#### Step 2. Second integration by parts

Take $u=x$, $dv=\cos nx\,dx$, so $du=dx$, $v=\dfrac{\sin nx}{n}$:
$$\int x\cos nx\,dx=\frac{x\sin nx}{n}-\frac1n\int\sin nx\,dx=\frac{x\sin nx}{n}+\frac{\cos nx}{n^2}$$
Hence the antiderivative
$$F(x)=-\frac{x^2\cos nx}{n}+\frac{2x\sin nx}{n^2}+\frac{2\cos nx}{n^3}$$
Check: $F'(x)=-\dfrac{2x\cos nx}{n}+x^2\sin nx+\dfrac{2\sin nx}{n^2}+\dfrac{2x\cos nx}{n}-\dfrac{2\sin nx}{n^2}=x^2\sin nx$.

#### Step 3. Barrow's rule

$F(\pi)=-\dfrac{\pi^2(-1)^n}{n}+0+\dfrac{2(-1)^n}{n^3}$ and $F(0)=0+0+\dfrac{2}{n^3}$, so
$$\int_0^{\pi}x^2\sin nx\,dx=[F]_0^{\pi}=F(\pi)-F(0)=\frac{\pi^2(-1)^{n+1}}{n}+\frac{2\big((-1)^n-1\big)}{n^3}$$
Multiplying by $2/\pi$:
$$b_n=\frac{2\pi(-1)^{n+1}}{n}+\frac{4\big((-1)^n-1\big)}{\pi n^3}$$

#### Step 4. Odd and even indices

For odd $n$, $(-1)^{n+1}=1$ and $(-1)^n-1=-2$: $b_n=\dfrac{2\pi}{n}-\dfrac{8}{\pi n^3}$. For even $n$, $(-1)^{n+1}=-1$ and $(-1)^n-1=0$: $b_n=-\dfrac{2\pi}{n}$. The leading term is of order $1/n$ for every $n$.

## (b) Compute the Fourier cosine series of f on (0, pi) [1.0 pts]

### Hint

Compute $a_0$ apart (the general formula divides by $n$). The same two integrations by parts work with $\cos nx$.

### Checkpoint

- $a_0=\dfrac{2\pi^2}{3}$, so the constant term is $\dfrac{a_0}{2}=\dfrac{\pi^2}{3}$.
- $a_n=\dfrac{4(-1)^n}{n^2}$ for $n\ge1$.
- $\displaystyle x^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos nx$ for $0\le x\le\pi$.

### Solution

#### Step 1. Mean value

$$a_0=\frac2\pi\int_0^{\pi}x^2\,dx=\frac2\pi\Big[\frac{x^3}{3}\Big]_0^{\pi}=\frac2\pi\cdot\frac{\pi^3}{3}=\frac{2\pi^2}{3}$$

#### Step 2. Antiderivative

With $u=x^2$, $dv=\cos nx\,dx$ ($du=2x\,dx$, $v=\sin nx/n$), then $u=x$, $dv=\sin nx\,dx$ ($du=dx$, $v=-\cos nx/n$):
$$\int x^2\cos nx\,dx=\frac{x^2\sin nx}{n}-\frac2n\int x\sin nx\,dx=\frac{x^2\sin nx}{n}-\frac2n\Big(-\frac{x\cos nx}{n}+\frac{\sin nx}{n^2}\Big)$$
$$G(x)=\frac{x^2\sin nx}{n}+\frac{2x\cos nx}{n^2}-\frac{2\sin nx}{n^3}$$

#### Step 3. Barrow's rule

$G(\pi)=0+\dfrac{2\pi(-1)^n}{n^2}-0$, $G(0)=0$. Therefore
$$a_n=\frac2\pi\,[G]_0^{\pi}=\frac2\pi\cdot\frac{2\pi(-1)^n}{n^2}=\frac{4(-1)^n}{n^2}$$

## (c) Continuity of the extensions, decay of the coefficients and values of the series [1.25 pts]

### Hint

Compare $f(0^+)$ with $-f(0^+)$ and $f(\pi^-)$ with $-f(\pi^-)$ for the odd extension. A jump in the function gives coefficients of order $1/n$; a continuous extension with a jump in the derivative gives order $1/n^2$.

### Checkpoint

- Odd extension $f_o$: **discontinuous** at $x=\pm\pi,\pm3\pi,\dots$ (jump from $\pi^2$ to $-\pi^2$), so $b_n=O(1/n)$.
- Even extension $f_e$: **continuous** everywhere; only $f_e'$ jumps (from $2\pi$ to $-2\pi$ at odd multiples of $\pi$), so $a_n=O(1/n^2)$.
- Sine series: $0$ at $x=\pi$, $-\pi^2/4$ at $x=-\pi/2$, $\pi^2/4$ at $x=5\pi/2$.
- Cosine series: $\pi^2$ at $x=\pi$, $\pi^2/4$ at $x=-\pi/2$, $\pi^2/4$ at $x=5\pi/2$.

### Solution

#### Step 1. The odd extension

$f_o(x)=x^2$ on $(0,\pi)$, $f_o(x)=-x^2$ on $(-\pi,0)$, repeated with period $2\pi$. At $x=0$ both side limits are $0$: continuous. At $x=\pi$: $f_o(\pi^-)=\pi^2$, while $f_o(\pi^+)=f_o(-\pi^+)=-(\pi)^2=-\pi^2$. Since $f(\pi)\ne0$, the odd extension has a jump of size $2\pi^2$ at every odd multiple of $\pi$.

#### Step 2. The even extension

$f_e(x)=x^2$ on $[-\pi,\pi]$, repeated with period $2\pi$. At $x=\pi$: $f_e(\pi^-)=\pi^2=f_e(-\pi^+)=f_e(\pi^+)$: continuous. The even extension of a continuous function is always continuous. Its derivative is $2x$ on $(-\pi,\pi)$: $f_e'(\pi^-)=2\pi$ and $f_e'(\pi^+)=f_e'(-\pi^+)=-2\pi$, a jump; at $x=0$, $f_e'(0^\pm)=0$, no jump.

#### Step 3. Why continuity controls the decay

In (a), the term of order $1/n$ came from the boundary value $-\dfrac{x^2\cos nx}{n}\Big|_0^{\pi}$, which is nonzero exactly because $f(\pi)\ne0$, i.e. because $f_o$ jumps. In (b) the corresponding boundary term $\dfrac{x^2\sin nx}{n}\Big|_0^{\pi}$ vanishes for any $f$; the first surviving term is $\Big[\dfrac{2x\cos nx}{n^2}\Big]_0^{\pi}=\dfrac{f'(\pi)(-1)^n-f'(0)}{n^2}$, which is nonzero because $f_e'$ jumps at $x=\pi$ ($f'(\pi)=2\pi\neq0$). Thus a jump in the extension forces $1/n$; a continuous extension with a jump in its derivative gives $1/n^2$. This matches Haberman Sec. 3.4: the cosine series of a continuous $f$ can be differentiated term by term (giving the sine series of $f'=2x$), while the sine series of $x^2$ cannot, because $f_o$ is not continuous.

#### Step 4. Values of the sine series

By the convergence theorem the sine series converges to $\tfrac12\big[f_o(x^+)+f_o(x^-)\big]$:
- $x=\pi$: $\tfrac12(\pi^2-\pi^2)=0$. Indeed every term $b_n\sin n\pi=0$.
- $x=-\pi/2$: $f_o$ continuous there, $f_o(-\pi/2)=-(\pi/2)^2=-\pi^2/4$.
- $x=5\pi/2=\pi/2+2\pi$: by periodicity $f_o(\pi/2)=\pi^2/4$.

#### Step 5. Values of the cosine series

$f_e$ is continuous, so the cosine series equals $f_e$ everywhere:
- $x=\pi$: $\pi^2$.
- $x=-\pi/2$: $f_e(-\pi/2)=(\pi/2)^2=\pi^2/4$.
- $x=5\pi/2$: $f_e(\pi/2)=\pi^2/4$.

## (d) Numerical sums from the series [1.25 pts]

### Hint

Evaluate the cosine series at $x=\pi$ and at $x=0$; evaluate the sine series at $x=\pi/2$, where $\sin(n\pi/2)$ is $0$ for even $n$ and $(-1)^k$ for $n=2k+1$.

### Checkpoint

- $\displaystyle\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}{6}$ (cosine series at $x=\pi$).
- $\displaystyle\sum_{n\ge1}\frac{(-1)^{n+1}}{n^2}=\frac{\pi^2}{12}$ (cosine series at $x=0$).
- $\displaystyle\sum_{k\ge0}\frac{(-1)^k}{(2k+1)^3}=\frac{\pi^3}{32}\approx0.968946$ (sine series at $x=\pi/2$).

### Solution

#### Step 1. Cosine series at x = pi

$\cos n\pi=(-1)^n$, so $(-1)^n\cos n\pi=1$ and
$$\pi^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{1}{n^2}\ \Rightarrow\ \sum_{n=1}^{\infty}\frac1{n^2}=\frac14\Big(\pi^2-\frac{\pi^2}{3}\Big)=\frac{\pi^2}{6}$$

#### Step 2. Cosine series at x = 0

$\cos 0=1$ and $f_e(0)=0$:
$$0=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\ \Rightarrow\ \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}=\frac{\pi^2}{12}$$

#### Step 3. Sine series at x = pi/2

$x=\pi/2$ is a point of continuity of $f_o$, so the series equals $\pi^2/4$. Only odd $n=2k+1$ survive, with $\sin\big((2k+1)\pi/2\big)=(-1)^k$ and $b_{2k+1}=\dfrac{2\pi}{2k+1}-\dfrac{8}{\pi(2k+1)^3}$:
$$\frac{\pi^2}{4}=2\pi\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}-\frac8\pi\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^3}=2\pi\cdot\frac\pi4-\frac8\pi S_3$$
where $S_3$ is the requested sum. Splitting the series is allowed because both pieces converge. Then
$$\frac8\pi S_3=\frac{\pi^2}{2}-\frac{\pi^2}{4}=\frac{\pi^2}{4}\ \Rightarrow\ S_3=\frac{\pi^3}{32}\approx0.968946$$

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** the sine series converges to $0$ at $x=\pi$ although $f(\pi)=\pi^2$; near $x=\pi$ the partial sums overshoot (Gibbs phenomenon, extension: the overshoot of the partial sums near a jump does not vanish as more terms are added, it only moves closer to the jump). The cosine series converges uniformly, since $\sum 4/n^2<\infty$.
- **Checks:** $S_3=1-0.037037+0.008+\dots$: the first three terms give $0.970963$, already within $0.0021$ of $\pi^3/32$. Differentiating the cosine series term by term gives $2x=\sum\frac{4(-1)^{n+1}}{n}\sin nx$, the sine series of $2x$ (as Haberman Sec. 3.4 allows for a continuous even extension).
- **Common mistakes in the exam:** (1) using the general $a_n$ formula with $n=0$ (division by zero) instead of computing $a_0$ apart; (2) forgetting the factor $\tfrac12$ in $a_0/2$, which gives the wrong constant $2\pi^2/3$; (3) claiming the sine series equals $\pi^2$ at $x=\pi$; (4) evaluating at $x=-\pi/2$ with $f$ instead of the extension (the sine series gives $-\pi^2/4$, not $+\pi^2/4$).

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
