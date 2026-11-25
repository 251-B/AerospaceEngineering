---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 8"
dificultad: media
id: "e8"
pill: "Sketching Fourier series"
tags:
  - problema-resuelto
  - fourier-series
  - convergence
  - periodic-extension
---

# Problem 6.8: Sketching Fourier Series and Periodic Extensions

> Official exercise 8 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Sketch the Fourier series of $f(x)$ on $[-L,L]$ for the given function, and compare with the graph of $f(x)$ itself.

(i) $f(x)=x^2$;
(ii) $f(x)=e^x$;
(iii) $f(x)=\begin{cases}1,&x<0,\\x+1,&x\ge0.\end{cases}$

## Period, Extension and Convergence Rule

The Fourier series of $f$ on $[-L,L]$ is $a_0+\sum\left(a_n\cos\frac{n\pi x}{L}+b_n\sin\frac{n\pi x}{L}\right)$, with $a_0=\frac{1}{2L}\int_{-L}^{L}f\,dx$, $a_n=\frac1L\int f\cos\frac{n\pi x}L dx$, $b_n=\frac1L\int f\sin\frac{n\pi x}L dx$. It is a $2L$-periodic function, so the sketch is the graph of the **$2L$-periodic extension** of $f$, with the value at each discontinuity replaced by the average of the one-sided limits (Fourier's Convergence Theorem; Haberman, Sec. 3.4).

Procedure: extend $f$ by $f(x+2L)=f(x)$; test continuity inside $(-L,L)$ and at the junctions $x=(2k+1)L$, where $f(L^-)$ meets $f(-L^+)$; at a continuity point the series equals $f$; at a jump it equals $\frac12[f(x^+)+f(x^-)]$. Below $k=\frac{n\pi}{L}$ abbreviates the frequency and $\sin n\pi=0$, $\cos n\pi=(-1)^n$.

## Step-by-Step Coefficient Evaluation

### (i) $f(x)=x^2$

![[attachments/AM-PS/ch6-e8-i.svg]]
*Sketch (i): the periodic extension of $x^2$ is a chain of parabolic arcs meeting with corners at $x=(2k+1)L$; the Fourier series coincides with it everywhere.*

$f$ is even: $b_n=0$, $a_0=\frac1L\int_0^Lx^2dx=\frac{L^2}{3}$, $a_n=\frac2L\int_0^Lx^2\cos kx\,dx$. By parts with $u=x^2$, $dv=\cos kx\,dx$, $du=2x\,dx$, $v=\frac{\sin kx}{k}$:

$$\int_0^Lx^2\cos kx\,dx=\left[\frac{x^2\sin kx}{k}\right]_0^L-\frac2k\int_0^Lx\sin kx\,dx=-\frac2k\int_0^Lx\sin kx\,dx,$$

since $\sin kL=\sin n\pi=0$. For the remaining integral, $u=x$, $dv=\sin kx\,dx$, $du=dx$, $v=-\frac{\cos kx}{k}$:

$$\int_0^Lx\sin kx\,dx=\left[-\frac{x\cos kx}{k}\right]_0^L+\frac1k\int_0^L\cos kx\,dx=-\frac{L(-1)^n}{k}+\frac{1}{k}\left[\frac{\sin kx}{k}\right]_0^L=-\frac{L(-1)^n}{k}.$$

So $\int_0^Lx^2\cos kx\,dx=\frac{2L(-1)^n}{k^2}=\frac{2L^3(-1)^n}{n^2\pi^2}$ and $a_n=\dfrac{4L^2(-1)^n}{n^2\pi^2}$:

$$x^2\sim\frac{L^2}{3}+\frac{4L^2}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos\frac{n\pi x}{L}.$$

Convergence: $f(-L)=f(L)=L^2$, so the extension is continuous; it has corners at $x=(2k+1)L$ (slope jumps from $2L$ to $-2L$) but no jumps. The series equals $f$ everywhere on $[-L,L]$ and equals the parabolic-arc chain $x\mapsto(x-2kL)^2$ elsewhere; at $x=\pm L$: $L^2$.

### (ii) $f(x)=e^x$

![[attachments/AM-PS/ch6-e8-ii.svg]]
*Sketch (ii): the periodic extension of $e^x$ is a sawtooth of exponential arcs with a jump at each $x=(2k+1)L$; the series sits at the midpoint $\cosh L$ there.*

$a_0=\frac1{2L}\int_{-L}^{L}e^xdx=\frac{e^L-e^{-L}}{2L}=\dfrac{\sinh L}{L}$.

Antiderivatives (verified by differentiating, with the product rule): $\frac{d}{dx}\left[e^x(\cos kx+k\sin kx)\right]=e^x(\cos kx+k\sin kx)+e^x(-k\sin kx+k^2\cos kx)=(1+k^2)e^x\cos kx$, and $\frac{d}{dx}\left[e^x(\sin kx-k\cos kx)\right]=e^x(\sin kx-k\cos kx)+e^x(k\cos kx+k^2\sin kx)=(1+k^2)e^x\sin kx$. Hence

$$\int_{-L}^{L}e^x\cos kx\,dx=\frac{\left[e^x(\cos kx+k\sin kx)\right]_{-L}^{L}}{1+k^2}=\frac{(-1)^n(e^L-e^{-L})}{1+k^2}=\frac{2(-1)^n\sinh L}{1+k^2},$$

$$\int_{-L}^{L}e^x\sin kx\,dx=\frac{\left[e^x(\sin kx-k\cos kx)\right]_{-L}^{L}}{1+k^2}=\frac{-k(-1)^n(e^L-e^{-L})}{1+k^2}=-\frac{2k(-1)^n\sinh L}{1+k^2},$$

using $\sin(\pm kL)=0$, $\cos(\pm kL)=(-1)^n$. With $1+k^2=\frac{L^2+n^2\pi^2}{L^2}$ and the prefactor $\frac1L$:

$$a_n=\frac{2L(-1)^n\sinh L}{L^2+n^2\pi^2},\qquad b_n=-\frac{2n\pi(-1)^n\sinh L}{L^2+n^2\pi^2}.$$

$$e^x\sim\frac{\sinh L}{L}+2\sinh L\sum_{n=1}^{\infty}\frac{(-1)^n}{L^2+n^2\pi^2}\left[L\cos\frac{n\pi x}{L}-n\pi\sin\frac{n\pi x}{L}\right].$$

Convergence: $f$ is continuous and smooth on $(-L,L)$, so the series equals $e^x$ there. At $x=\pm L$ (and all $(2k+1)L$): $f(L^-)=e^L$, $f(-L^+)=e^{-L}$, so the series converges to $\frac{e^L+e^{-L}}2=\cosh L$. Consistency: plugging $x=L$ the sines vanish and $a_0+\sum a_n(-1)^n=\frac{\sinh L}{L}+2L\sinh L\sum\frac1{L^2+n^2\pi^2}=\cosh L$, the classical expansion $\coth L=\frac1L+2L\sum\frac{1}{L^2+n^2\pi^2}$.

### (iii) $f(x)=1$ for $x<0$, $f(x)=x+1$ for $x\ge0$

![[attachments/AM-PS/ch6-e8-iii.svg]]
*Sketch (iii): flat piece at height $1$ on $[-L,0)$, a ramp from $1$ to $L+1$ on $[0,L]$, continuous at $0$ with a corner, jumping at $x=(2k+1)L$ with the series at $1+\frac L2$.*

Continuity at $0$: $f(0^-)=1$, $f(0^+)=0+1=1$, so $f$ is continuous there (with a corner: slope $0$ on the left, $1$ on the right). At the junction $f(L^-)=L+1$ and $f(-L^+)=1$: a jump of size $L$.

$a_0=\frac1{2L}\left[\int_{-L}^{0}1\,dx+\int_0^L(x+1)dx\right]=\frac1{2L}\left[L+\frac{L^2}{2}+L\right]=1+\dfrac{L}{4}$.

$a_n=\frac1L\left[\int_{-L}^0\cos kx\,dx+\int_0^L(x+1)\cos kx\,dx\right]$. Since $\int_{-L}^0\cos kx\,dx=\frac{\sin 0-\sin(-kL)}{k}=0$ and $\int_0^L\cos kx\,dx=\frac{\sin kL}{k}=0$, only $\int_0^Lx\cos kx\,dx$ remains; by parts ($u=x$, $v=\frac{\sin kx}{k}$):

$$\int_0^Lx\cos kx\,dx=\left[\frac{x\sin kx}{k}\right]_0^L-\frac1k\int_0^L\sin kx\,dx=0-\frac1k\left[-\frac{\cos kx}{k}\right]_0^L=\frac{(-1)^n-1}{k^2}.$$

Thus $a_n=\dfrac{1}{L}\cdot\dfrac{L^2\left((-1)^n-1\right)}{n^2\pi^2}=\dfrac{L\left((-1)^n-1\right)}{n^2\pi^2}$, i.e. $-\frac{2L}{n^2\pi^2}$ for odd $n$ and $0$ for even $n$.

$b_n=\frac1L\left[\int_{-L}^0\sin kx\,dx+\int_0^L\sin kx\,dx+\int_0^Lx\sin kx\,dx\right]$. First: $\left[-\frac{\cos kx}{k}\right]_{-L}^{0}=\frac{(-1)^n-1}{k}$; second: $\left[-\frac{\cos kx}{k}\right]_0^L=\frac{1-(-1)^n}{k}$; they cancel. Third (computed in (i)): $-\frac{L(-1)^n}{k}$. So

$$b_n=-\frac{(-1)^n}{k}=\frac{(-1)^{n+1}L}{n\pi}.$$

$$f\sim1+\frac L4+\sum_{n=1}^{\infty}\left[\frac{L\left((-1)^n-1\right)}{n^2\pi^2}\cos\frac{n\pi x}{L}+\frac{(-1)^{n+1}L}{n\pi}\sin\frac{n\pi x}{L}\right].$$

Convergence checks:

- At $x=0$ (continuous): $1+\frac L4+\sum a_n=1+\frac L4-\frac{2L}{\pi^2}\sum_{k\ \mathrm{odd}}\frac1{k^2}=1+\frac L4-\frac{2L}{\pi^2}\cdot\frac{\pi^2}8=1=f(0)$ ✓ (uses $\sum(2j-1)^{-2}=\pi^2/8$, see [[Problem - Ch6-P5 Fourier Series of Nine Functions]]).
- At $x=\pm L$ (jump): sines vanish and $\cos n\pi=(-1)^n$, giving $1+\frac L4+\sum\frac{L(1-(-1)^n)}{n^2\pi^2}=1+\frac L4+\frac{2L}{\pi^2}\cdot\frac{\pi^2}8=1+\frac L2=\frac{(L+1)+1}{2}$ ✓.

## Fourier Series, Convergence and Checks

> [!result] Comparison with the graph of $f$
> | | continuous extension? | Series at $x=\pm L$ | Series vs $f$ on $(-L,L)$ |
> | :--- | :--- | :--- | :--- |
> | (i) $x^2$ | yes (corners at $(2k+1)L$) | $L^2$ | equal |
> | (ii) $e^x$ | no (jump at $(2k+1)L$) | $\cosh L$ | equal, Gibbs overshoot near $\pm L$ |
> | (iii) piecewise | no (jump at $(2k+1)L$, corner at $2kL$) | $1+\frac L2$ | equal (also at $0$) |

> [!warning] Endpoint values
> $f(\pm L)$ itself ($L^2$, $e^{\pm L}$, $L+1$ or $1$) is not what the series returns when the periodic extension jumps: the series returns the average of the one-sided limits. The sketch must show an open/closed dot at the jump and the midpoint value.

Checks: a corner (no jump) means coefficients decay like $n^{-2}$ ((i) and the $a_n$ of (iii)); a jump means $b_n\sim n^{-1}$ ((ii) and (iii)), as the formulas show. Dimensions: $a_n,b_n$ carry the units of $f$ ✓.
