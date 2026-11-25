---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 5"
dificultad: media
id: "e5"
pill: "Nine Fourier series"
tags:
  - problema-resuelto
  - fourier-series
  - convergence
---

# Problem 6.5: Fourier Series of Nine Functions

> Official exercise 5 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Calculate the Fourier series for the given functions:

(i) $f(x) = 1$, $-\pi \le x \le \pi$;
(ii) $f(x) = x$, $-\pi \le x \le \pi$;
(iii) $f(x) = \pi - x$, $-\pi \le x \le \pi$;
(iv) $f(x) = |x|$, $-\pi \le x \le \pi$;
(v) $f(x) = x^2$, $-\pi \le x \le \pi$;
(vi) $f(x) = \cos x$, $0 \le x \le \pi$;
(vii) $f(x) = \begin{cases} 0, & -\pi \le x < 0, \\ \pi, & 0 \le x \le \pi; \end{cases}$
(viii) $f(x) = \begin{cases} -\pi/2, & -\pi \le x < 0, \\ \pi/2, & 0 \le x \le \pi; \end{cases}$
(ix) $f(x) = \begin{cases} 1, & 0 \le x \le \pi/2, \\ 2, & \pi/2 \le x \le \pi. \end{cases}$

## Period, Symmetry and Coefficient Formulas

For a function of period $2L$ the series is (Haberman, Sec. 3.3)

$$f(x) \sim a_0 + \sum_{n=1}^{\infty}\left[a_n\cos\frac{n\pi x}{L} + b_n\sin\frac{n\pi x}{L}\right],$$

$$a_0 = \frac{1}{2L}\int_{-L}^{L} f\,dx,\qquad a_n = \frac{1}{L}\int_{-L}^{L} f\cos\frac{n\pi x}{L}\,dx,\qquad b_n = \frac{1}{L}\int_{-L}^{L} f\sin\frac{n\pi x}{L}\,dx .$$

Here $a_0$ is the mean value of $f$ over a period. For (i) to (v), (vii), (viii) we take $L=\pi$. Parity shortens the work (Haberman, Sec. 3.4; see [[Problem - Ch6-P9 Fourier Series of Even and Odd Periodic Functions]]): if $f$ is even, $b_n=0$ and $a_n=\frac{2}{\pi}\int_0^\pi f\cos nx\,dx$; if $f$ is odd, $a_0=a_n=0$ and $b_n=\frac{2}{\pi}\int_0^\pi f\sin nx\,dx$.

Two integrals used repeatedly, for integer $n\ge1$, with $\sin n\pi = 0$ and $\cos n\pi=(-1)^n$:

$$\int_0^\pi \sin nx\,dx = \left[-\frac{\cos nx}{n}\right]_0^\pi = \frac{1-(-1)^n}{n},\qquad \int_0^\pi \cos nx\,dx = \left[\frac{\sin nx}{n}\right]_0^\pi = 0 .$$

Convergence (Fourier's theorem): at a point where the $2L$-periodic extension is continuous the series equals $f$; at a jump it equals $\tfrac12[f(x^+)+f(x^-)]$.

## Step-by-Step Coefficient Evaluation

### (i) $f(x)=1$

Even. $a_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}1\,dx=1$, $a_n=\frac{2}{\pi}\int_0^\pi\cos nx\,dx=0$, $b_n=0$. The series is $1$ (it is its own series, trivially).

### (ii) $f(x)=x$

Odd, so $a_0=a_n=0$. $b_n=\frac{2}{\pi}\int_0^\pi x\sin nx\,dx$. Integration by parts with $u=x$, $dv=\sin nx\,dx$, $du=dx$, $v=-\frac{\cos nx}{n}$:

$$\int_0^\pi x\sin nx\,dx=\left[-\frac{x\cos nx}{n}\right]_0^\pi+\frac1n\int_0^\pi\cos nx\,dx=-\frac{\pi(-1)^n}{n}-0+0=\frac{\pi(-1)^{n+1}}{n}.$$

Hence $b_n=\dfrac{2(-1)^{n+1}}{n}$ and

$$x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin nx .$$

The $2\pi$-periodic extension jumps at $x=\pm\pi$ (from $\pi$ to $-\pi$): the series gives $\tfrac12(\pi-\pi)=0$, which matches $\sin n\pi=0$. At interior points it equals $x$.

### (iii) $f(x)=\pi-x$

By linearity $f=\pi + (-x)$: $a_0=\pi$, $a_n=0$, $b_n=-\dfrac{2(-1)^{n+1}}{n}=\dfrac{2(-1)^n}{n}$.

$$\pi-x\sim \pi+2\sum_{n=1}^{\infty}\frac{(-1)^n}{n}\sin nx .$$

At $x=\pm\pi$: $f(\pi^-)=0$ and $f(-\pi^+)=2\pi$, so the series gives $\tfrac12(0+2\pi)=\pi=a_0$, consistent with every sine vanishing.

### (iv) $f(x)=|x|$

Even, $b_n=0$. $a_0=\frac{1}{2\pi}\cdot 2\int_0^\pi x\,dx=\frac1\pi\left[\frac{x^2}{2}\right]_0^\pi=\frac{\pi}{2}$. For $n\ge1$, $a_n=\frac2\pi\int_0^\pi x\cos nx\,dx$ with $u=x$, $dv=\cos nx\,dx$, $du=dx$, $v=\frac{\sin nx}{n}$:

$$\int_0^\pi x\cos nx\,dx=\left[\frac{x\sin nx}{n}\right]_0^\pi-\frac1n\int_0^\pi\sin nx\,dx=0-\frac1n\cdot\frac{1-(-1)^n}{n}=\frac{(-1)^n-1}{n^2}.$$

So $a_n=\dfrac{2\left((-1)^n-1\right)}{\pi n^2}$, equal to $-\dfrac{4}{\pi n^2}$ for odd $n$ and $0$ for even $n$. With $n=2k-1$:

$$|x|\sim\frac{\pi}{2}-\frac4\pi\sum_{k=1}^{\infty}\frac{\cos\left((2k-1)x\right)}{(2k-1)^2}.$$

The periodic extension is continuous (since $f(-\pi)=f(\pi)=\pi$), so the series equals $|x|$ everywhere. At $x=0$: $0=\frac\pi2-\frac4\pi S$, so

$$\sum_{k=1}^{\infty}\frac{1}{(2k-1)^2}=\frac{\pi^2}{8}.$$

### (v) $f(x)=x^2$

Even, $b_n=0$. $a_0=\frac1\pi\int_0^\pi x^2dx=\frac1\pi\cdot\frac{\pi^3}{3}=\frac{\pi^2}{3}$. For $a_n=\frac2\pi\int_0^\pi x^2\cos nx\,dx$, first by parts with $u=x^2$, $dv=\cos nx\,dx$, $du=2x\,dx$, $v=\frac{\sin nx}{n}$:

$$\int_0^\pi x^2\cos nx\,dx=\left[\frac{x^2\sin nx}{n}\right]_0^\pi-\frac2n\int_0^\pi x\sin nx\,dx=0-\frac2n\cdot\frac{\pi(-1)^{n+1}}{n}=\frac{2\pi(-1)^n}{n^2},$$

using the integral of (ii). Then $a_n=\dfrac{4(-1)^n}{n^2}$ and

$$x^2\sim\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos nx .$$

The extension is continuous, so equality holds on $[-\pi,\pi]$.

- At $x=\pi$: $\pi^2=\frac{\pi^2}{3}+4\sum\frac{(-1)^n(-1)^n}{n^2}$, so $\sum_{n=1}^{\infty}\frac1{n^2}=\frac{\pi^2}{6}$.
- At $x=0$: $0=\frac{\pi^2}{3}+4\sum\frac{(-1)^n}{n^2}$, so $\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}=\frac{\pi^2}{12}$.

### (vi) $f(x)=\cos x$ on $[0,\pi]$

The function is given only on $[0,\pi]$, so the natural choice is the $\pi$-periodic extension: period $2L=\pi$, $L=\pi/2$, basis $\cos 2nx$, $\sin 2nx$.

$a_0=\frac1\pi\int_0^\pi\cos x\,dx=\frac1\pi[\sin x]_0^\pi=0$.

Product-to-sum: $\cos x\cos 2nx=\tfrac12\left[\cos(2n+1)x+\cos(2n-1)x\right]$ and $\cos x\sin 2nx=\tfrac12\left[\sin(2n+1)x+\sin(2n-1)x\right]$. For odd $m$, $\int_0^\pi\cos mx\,dx=\frac{\sin m\pi}{m}=0$ and $\int_0^\pi\sin mx\,dx=\frac{1-\cos m\pi}{m}=\frac2m$. Therefore

$$a_n=\frac2\pi\cdot\tfrac12\cdot 0=0,\qquad b_n=\frac2\pi\cdot\tfrac12\left[\frac{2}{2n+1}+\frac{2}{2n-1}\right]=\frac2\pi\cdot\frac{4n}{4n^2-1}=\frac{8n}{\pi(4n^2-1)} .$$

$$\cos x\sim\sum_{n=1}^{\infty}\frac{8n}{\pi(4n^2-1)}\sin 2nx .$$

Convergence: the $\pi$-periodic extension has $f(0^+)=1$, $f(\pi^-)=-1$, so it jumps at $x=k\pi$ and the series gives $0$ there (all sines vanish). In $(0,\pi)$ the series equals $\cos x$.

> [!info] Relation to the half-range expansions on $[0,\pi]$
> With $L=\pi$, the odd extension gives $B_m=\frac2\pi\int_0^\pi\cos x\sin mx\,dx=\frac1\pi\left[\frac{1-\cos(m+1)\pi}{m+1}+\frac{1-\cos(m-1)\pi}{m-1}\right]$ for $m\ne1$. For odd $m$ both numerators vanish, so $B_{2n-1}=0$. For $m=2n$ it is $\frac1\pi\left[\frac2{2n+1}+\frac2{2n-1}\right]=\frac{8n}{\pi(4n^2-1)}$, and $B_1=\frac2\pi\int_0^\pi\cos x\sin x\,dx=\frac1\pi\int_0^\pi\sin 2x\,dx=0$. The half-range sine series is therefore the **same** series as above: $b_{2n}$ survives and $b_{2n-1}=0$. The even (cosine) half-range series is trivially $\cos x$ itself ($a_1=1$, all other coefficients zero, by orthogonality; see [[Problem - Ch6-P6 Fourier Series via Trigonometric Identities without Integrating]]).

### (vii) Step function $0$ on $[-\pi,0)$, $\pi$ on $[0,\pi]$

$a_0=\frac{1}{2\pi}\int_0^\pi\pi\,dx=\frac\pi2$. $a_n=\frac1\pi\int_0^\pi\pi\cos nx\,dx=0$. $b_n=\frac1\pi\int_0^\pi\pi\sin nx\,dx=\frac{1-(-1)^n}{n}$, which is $\frac2n$ for odd $n$ and $0$ for even $n$.

$$f\sim\frac\pi2+2\sum_{k=1}^{\infty}\frac{\sin\left((2k-1)x\right)}{2k-1}.$$

At the jumps $x=0,\pm\pi$ the series gives $\frac\pi2=\tfrac12\left(0+\pi\right)$ as required. Check at $x=\pi/2$ (continuity point, $f=\pi$): $\sin\frac{(2k-1)\pi}2=(-1)^{k-1}$ and $\sum\frac{(-1)^{k-1}}{2k-1}=\frac\pi4$ (Leibniz), so $\frac\pi2+2\cdot\frac\pi4=\pi$.

### (viii) Step function $-\pi/2$ on $[-\pi,0)$, $\pi/2$ on $[0,\pi]$

This is (vii) minus $\pi/2$, so only $a_0$ changes: $a_0=0$. The function is odd (apart from its value at the jump), and

$$f\sim2\sum_{k=1}^{\infty}\frac{\sin\left((2k-1)x\right)}{2k-1}.$$

At $x=0$ the series gives $0=\tfrac12\left(-\frac\pi2+\frac\pi2\right)$; at $x=\pi/2$ it gives $2\cdot\frac\pi4=\frac\pi2=f$.

### (ix) $f=1$ on $[0,\pi/2]$, $f=2$ on $[\pi/2,\pi]$

**Full $\pi$-periodic series** ($L=\pi/2$, basis $\cos2nx$, $\sin2nx$):

$a_0=\frac1\pi\left[\frac\pi2\cdot1+\frac\pi2\cdot2\right]=\frac32$.

$a_n=\frac2\pi\left[\int_0^{\pi/2}\cos2nx\,dx+2\int_{\pi/2}^{\pi}\cos2nx\,dx\right]=\frac2\pi\left[\frac{\sin n\pi}{2n}+2\cdot\frac{\sin2n\pi-\sin n\pi}{2n}\right]=0.$

For $b_n$: $\int_0^{\pi/2}\sin2nx\,dx=\left[-\frac{\cos2nx}{2n}\right]_0^{\pi/2}=\frac{1-(-1)^n}{2n}$ and $\int_{\pi/2}^{\pi}\sin2nx\,dx=\frac{(-1)^n-1}{2n}$. Then

$$b_n=\frac2\pi\left[\frac{1-(-1)^n}{2n}+2\cdot\frac{(-1)^n-1}{2n}\right]=\frac2\pi\cdot\frac{(-1)^n-1}{2n}=\frac{(-1)^n-1}{n\pi},$$

so $b_{2k}=0$ and $b_{2k-1}=-\dfrac{2}{\pi(2k-1)}$:

$$f\sim\frac32-\frac2\pi\sum_{k=1}^{\infty}\frac{\sin\left(2(2k-1)x\right)}{2k-1}.$$

Check at $x=\pi/4$ ($f=1$): $\sin\frac{(2k-1)\pi}{2}=(-1)^{k-1}$, so $\frac32-\frac2\pi\cdot\frac\pi4=1$. At the jump $x=\pi/2$ the series gives $\frac32=\tfrac12(1+2)$.

**Half-range cosine series on $[0,\pi]$** ($L=\pi$, even extension): $a_0=\frac32$ and, evaluating each antiderivative by Barrow's rule with substitution $u = nx$,

$$a_n=\frac2\pi\left[\int_0^{\pi/2}\cos nx\,dx+2\int_{\pi/2}^{\pi}\cos nx\,dx\right]=\frac2\pi\left(\left[\frac{\sin nx}{n}\right]_0^{\pi/2}+2\left[\frac{\sin nx}{n}\right]_{\pi/2}^{\pi}\right)=\frac2\pi\left[\frac{\sin(n\pi/2)}{n}-\frac{2\sin(n\pi/2)}{n}\right]=-\frac{2\sin(n\pi/2)}{n\pi}.$$

Only odd $n=2k-1$ survive, with $\sin\frac{(2k-1)\pi}2=(-1)^{k-1}$:

$$f\sim\frac32-\frac2\pi\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}\cos\left((2k-1)x\right).$$

The even extension has a single jump in $(0,\pi)$ (at $\pi/2$, mirrored at $-\pi/2$) and is continuous at $0$ and $\pi$.

**Half-range sine series on $[0,\pi]$** ($L=\pi$, odd extension): $a_0=a_n=0$, and applying Barrow's rule with $u = nx$, $\int_0^{\pi/2}\sin nx\,dx=\left[-\frac{\cos nx}{n}\right]_0^{\pi/2}=\frac{1-\cos(n\pi/2)}{n}$ and $\int_{\pi/2}^{\pi}\sin nx\,dx=\left[-\frac{\cos nx}{n}\right]_{\pi/2}^{\pi}=\frac{\cos(n\pi/2)-\cos n\pi}{n}$, so

$$b_n=\frac2\pi\left[\frac{1-\cos(n\pi/2)}{n}+2\,\frac{\cos(n\pi/2)-\cos n\pi}{n}\right]=\frac{2}{n\pi}\left(1+\cos\frac{n\pi}2-2(-1)^n\right).$$

$$f\sim\sum_{n=1}^{\infty}\frac{2}{n\pi}\left(1+\cos\frac{n\pi}2-2(-1)^n\right)\sin nx=\frac6\pi\sin x-\frac2\pi\sin2x+\frac2\pi\sin3x+0\cdot\sin4x+\cdots$$

(values: $b_1=\frac{6}{\pi}$, $b_2=-\frac2\pi$, $b_3=\frac2\pi$, $b_4=0$). The odd extension jumps at $x=0,\pm\pi$ (where the series gives $0$) and at $\pm\pi/2$.

## Fourier Series, Convergence and Checks

> [!result] Summary
> | Function | Series | Converges to $f$? |
> | :--- | :--- | :--- |
> | (i) $1$ | $1$ | everywhere |
> | (ii) $x$ | $2\sum\frac{(-1)^{n+1}}{n}\sin nx$ | interior; $0$ at $\pm\pi$ |
> | (iii) $\pi-x$ | $\pi+2\sum\frac{(-1)^n}{n}\sin nx$ | interior; $\pi$ at $\pm\pi$ |
> | (iv) $\lvert x\rvert$ | $\frac\pi2-\frac4\pi\sum\frac{\cos(2k-1)x}{(2k-1)^2}$ | everywhere; gives $\sum(2k-1)^{-2}=\pi^2/8$ |
> | (v) $x^2$ | $\frac{\pi^2}3+4\sum\frac{(-1)^n}{n^2}\cos nx$ | everywhere; gives $\pi^2/6$ and $\pi^2/12$ |
> | (vi) $\cos x$ on $[0,\pi]$ | $\sum\frac{8n}{\pi(4n^2-1)}\sin2nx$ | on $(0,\pi)$; $0$ at $0,\pi$ |
> | (vii) step $0/\pi$ | $\frac\pi2+2\sum\frac{\sin(2k-1)x}{2k-1}$ | away from jumps; $\frac\pi2$ at jumps |
> | (viii) step $\mp\frac\pi2$ | $2\sum\frac{\sin(2k-1)x}{2k-1}$ | away from jumps; $0$ at jumps |
> | (ix) $1/2$ on $[0,\pi]$ | $\frac32-\frac2\pi\sum\frac{\sin2(2k-1)x}{2k-1}$ | away from jumps; $\frac32$ at $\frac\pi2$ |

> [!warning] Convention
> The sheet's convention for the constant term is the mean value, $a_0=\frac1{2L}\int f$, so the series reads $a_0+\sum(\dots)$. If a source writes $\frac{a_0}{2}$ the stored value doubles; the series itself does not change.

Checks: dimensionless (all functions are pure numbers or lengths of the argument $x$ in radians); a termwise sanity test at one interior point was made in (vii) and (ix).
