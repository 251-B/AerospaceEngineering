---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 8"
dificultad: media
id: "e8"
pill: "Periodic Extension • Jump Midpoints • Three Sketches"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.8: Sketching Fourier Series vs Original Functions

> Official exercise 8 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Sketch the Fourier series of $f(x)$ on $[-L, L]$ for the given function, and compare with the graph of $f(x)$ itself.

- (i) $f(x) = x^2$.
- (ii) $f(x) = e^x$.
- (iii) $f(x) = \begin{cases} 1, & x < 0, \\ x + 1, & x \ge 0. \end{cases}$

## Extension of f

To compare the graph of the Fourier series with the graph of $f(x)$ itself on $\mathbb{R}$, we first form the $2L$-periodic extension $\tilde{f}(x)$ of $f|_{[-L, L]}$ and check continuity both inside $(-L, L)$ and at the periodic joints $x = (2k+1)L$ ($k \in \mathbb{Z}$) (Haberman Sec. 3.2; `Notes09-12-Nov.pdf`, p. 7 and pp. 12–13).

- **(i) $f(x) = x^2$**: Smooth on $[-L, L]$ and even ($f(-x) = f(x)$). At the endpoints, $f(-L) = L^2 = f(L)$, so the $2L$-periodic extension $\tilde{f}$ is **continuous everywhere** on $\mathbb{R}$ (with corners at $x = (2k+1)L$, where the left slope is $+2L$ and the right slope is $-2L$). Outside $[-L, L]$, the Fourier series repeats the parabolic arch on every $2L$-interval, whereas $f(x) = x^2$ keeps growing quadratically to $+\infty$.
- **(ii) $f(x) = e^x$**: Smooth on $[-L, L]$ with no even/odd symmetry. At the endpoints, $f(-L) = e^{-L} \neq e^{L} = f(L)$, so the $2L$-periodic extension $\tilde{f}$ has **jump discontinuities** at every odd multiple $x = (2k+1)L$ ($k \in \mathbb{Z}$), jumping from $e^L$ on the left to $e^{-L}$ on the right. Outside $[-L, L]$, the Fourier series is bounded and $2L$-periodic, whereas $e^x \to +\infty$ as $x \to +\infty$ and $e^x \to 0$ as $x \to -\infty$.
- **(iii) $f(x) = 1$ ($x < 0$), $x + 1$ ($x \ge 0$)**: Inside $(-L, L)$, we check continuity at $x = 0$: $\lim_{x \to 0^-} f(x) = 1$ and $\lim_{x \to 0^+} f(x) = 0 + 1 = 1$, so $f$ is **continuous at $x = 0$** (with a corner where the slope jumps from $0$ to $1$). At the endpoints, $f(-L) = 1 \neq L + 1 = f(L)$, so the $2L$-periodic extension has **jump discontinuities** at every $x = (2k+1)L$, jumping from $L + 1$ on the left to $1$ on the right. Outside $[-L, L]$, the Fourier series repeats this ramp-and-plateau wave periodically, whereas $f(x)$ stays flat at $1$ for $x < -L$ and climbs linearly for $x > L$.

## Coefficients a_0, a_n, b_n

We compute the exact Euler-Fourier coefficients on $[-L, L]$ using the lecturer's formulas (`Notes09-12-Nov.pdf`, p. 10):

$$ a_0 = \frac{1}{2L}\int_{-L}^{L} f(x)\,dx, \qquad a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\frac{n\pi x}{L}\,dx, \qquad b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\frac{n\pi x}{L}\,dx. $$

### (i) $f(x) = x^2$ on $[-L, L]$

Because $x^2$ is even on $[-L, L]$, $x^2\sin\frac{n\pi x}{L}$ is odd and $b_n = 0$ for all $n \ge 1$. For $a_0$ and $a_n$ we fold the even integrands onto $[0, L]$.

We compute $a_0$ using $\int x^2\,dx = \frac{x^3}{3}$.

$$ a_0 = \frac{1}{2L}\int_{-L}^{L} x^2\,dx = \frac{1}{L}\int_{0}^{L} x^2\,dx = \frac{1}{L}\left[\frac{x^3}{3}\right]_{0}^{L} = \frac{1}{L}\left(\frac{L^3}{3} - 0\right) = \frac{L^2}{3}. $$

For $a_n$ ($n \ge 1$), we write $\omega_n = \frac{n\pi}{L}$ for clarity and apply integration by parts twice. First choose $u_1 = x^2$, $dv_1 = \cos(\omega_n x)\,dx$, giving $du_1 = 2x\,dx$ and $v_1 = \frac{\sin(\omega_n x)}{\omega_n}$.

$$ \int_{0}^{L} x^2\cos(\omega_n x)\,dx = \left[\frac{x^2\sin(\omega_n x)}{\omega_n}\right]_{0}^{L} - \frac{2}{\omega_n}\int_{0}^{L} x\sin(\omega_n x)\,dx. $$

Since $\sin(\omega_n L) = \sin(n\pi) = 0$ and $\sin(0) = 0$, the boundary term vanishes. For the remaining integral we integrate by parts a second time with $u_2 = x$, $dv_2 = \sin(\omega_n x)\,dx$, giving $du_2 = dx$ and $v_2 = -\frac{\cos(\omega_n x)}{\omega_n}$.

$$ \int_{0}^{L} x\sin(\omega_n x)\,dx = \left[-\frac{x\cos(\omega_n x)}{\omega_n}\right]_{0}^{L} + \frac{1}{\omega_n}\int_{0}^{L} \cos(\omega_n x)\,dx = \left(-\frac{L\cos(n\pi)}{\omega_n} - 0\right) + \frac{1}{\omega_n}\left[\frac{\sin(\omega_n x)}{\omega_n}\right]_{0}^{L}. $$

Using $\cos(n\pi) = (-1)^n$ and $\sin(n\pi) = \sin(0) = 0$, we obtain $\int_{0}^{L} x\sin(\omega_n x)\,dx = -\frac{L(-1)^n}{\omega_n}$. Substituting back into $a_n = \frac{2}{L}\int_{0}^{L} x^2\cos(\omega_n x)\,dx$ and replacing $\omega_n = \frac{n\pi}{L}$ gives

$$ a_n = \frac{2}{L}\left(-\frac{2}{\omega_n}\right)\left(-\frac{L(-1)^n}{\omega_n}\right) = \frac{4(-1)^n}{\omega_n^2} = \frac{4L^2(-1)^n}{(n\pi)^2}, \qquad n \ge 1. $$

### (ii) $f(x) = e^x$ on $[-L, L]$

First we compute $a_0$ directly using $\int e^x\,dx = e^x$ and the definition $\sinh L = \frac{e^L - e^{-L}}{2}$.

$$ a_0 = \frac{1}{2L}\int_{-L}^{L} e^x\,dx = \frac{1}{2L}\Big[e^x\Big]_{-L}^{L} = \frac{e^L - e^{-L}}{2L} = \frac{\sinh L}{L}. $$

To compute $a_n$ and $b_n$ ($n \ge 1$), set $\omega_n = \frac{n\pi}{L}$ and define the two integrals

$$ C_n = \int_{-L}^{L} e^x\cos(\omega_n x)\,dx, \qquad S_n = \int_{-L}^{L} e^x\sin(\omega_n x)\,dx. $$

We integrate $C_n$ by parts with $u_1 = \cos(\omega_n x)$ and $dv_1 = e^x\,dx$, giving $du_1 = -\omega_n\sin(\omega_n x)\,dx$ and $v_1 = e^x$.

$$ C_n = \Big[e^x\cos(\omega_n x)\Big]_{-L}^{L} + \omega_n \int_{-L}^{L} e^x\sin(\omega_n x)\,dx = \big(e^L\cos(n\pi) - e^{-L}\cos(-n\pi)\big) + \omega_n S_n. $$

Since $\cos(n\pi) = \cos(-n\pi) = (-1)^n$ and $e^L - e^{-L} = 2\sinh L$, this simplifies to

$$ C_n = 2(-1)^n\sinh L + \omega_n S_n. $$

Next we integrate $S_n$ by parts with $u_2 = \sin(\omega_n x)$ and $dv_2 = e^x\,dx$, giving $du_2 = \omega_n\cos(\omega_n x)\,dx$ and $v_2 = e^x$.

$$ S_n = \Big[e^x\sin(\omega_n x)\Big]_{-L}^{L} - \omega_n \int_{-L}^{L} e^x\cos(\omega_n x)\,dx = \big(e^L\sin(n\pi) - e^{-L}\sin(-n\pi)\big) - \omega_n C_n = -\omega_n C_n, $$

because $\sin(n\pi) = \sin(-n\pi) = 0$. Substituting $S_n = -\omega_n C_n$ into our equation for $C_n$ lets us solve algebraically for $C_n$ and $S_n$:

$$ C_n = 2(-1)^n\sinh L - \omega_n^2 C_n \implies (1 + \omega_n^2)C_n = 2(-1)^n\sinh L \implies C_n = \frac{2(-1)^n\sinh L}{1 + \omega_n^2}, $$

$$ S_n = -\omega_n C_n = -\frac{2\omega_n(-1)^n\sinh L}{1 + \omega_n^2}. $$

Now substitute $\omega_n = \frac{n\pi}{L}$ (so $1 + \omega_n^2 = \frac{L^2 + (n\pi)^2}{L^2}$) and divide by $L$:

$$ a_n = \frac{C_n}{L} = \frac{2(-1)^n\sinh L}{L\left(1 + \frac{(n\pi)^2}{L^2}\right)} = \frac{2L(-1)^n\sinh L}{L^2 + (n\pi)^2}, \qquad n \ge 1, $$

$$ b_n = \frac{S_n}{L} = -\frac{2\frac{n\pi}{L}(-1)^n\sinh L}{L\left(1 + \frac{(n\pi)^2}{L^2}\right)} = -\frac{2n\pi(-1)^n\sinh L}{L^2 + (n\pi)^2}, \qquad n \ge 1. $$

### (iii) $f(x) = \begin{cases} 1, & -L \le x < 0, \\ x + 1, & 0 \le x \le L \end{cases}$

Observe that $f(x) = 1 + g(x)$ where $g(x) = 0$ on $[-L, 0)$ and $g(x) = x$ on $[0, L]$. Splitting every integral at $x = 0$ (or using linearity directly) makes the algebra completely transparent.

First we compute $a_0$ by splitting at $x = 0$.

$$ a_0 = \frac{1}{2L}\left(\int_{-L}^{0} 1\,dx + \int_{0}^{L} (x + 1)\,dx\right) = \frac{1}{2L}\left(\Big[x\Big]_{-L}^{0} + \left[\frac{x^2}{2} + x\right]_{0}^{L}\right) = \frac{1}{2L}\left(L + \frac{L^2}{2} + L\right) = 1 + \frac{L}{4}. $$

For $a_n$ ($n \ge 1$), set $\omega_n = \frac{n\pi}{L}$ and note that $\int_{-L}^{L} 1\cdot\cos(\omega_n x)\,dx = 0$, leaving only $\frac{1}{L}\int_{0}^{L} x\cos(\omega_n x)\,dx$. We integrate by parts with $u = x$, $dv = \cos(\omega_n x)\,dx$, giving $du = dx$ and $v = \frac{\sin(\omega_n x)}{\omega_n}$.

$$ a_n = \frac{1}{L}\int_{0}^{L} x\cos(\omega_n x)\,dx = \frac{1}{L}\left(\left[\frac{x\sin(\omega_n x)}{\omega_n}\right]_{0}^{L} - \int_{0}^{L} \frac{\sin(\omega_n x)}{\omega_n}\,dx\right). $$

Evaluating the boundary term ($\sin(n\pi) = \sin(0) = 0$) and integrating $-\frac{\sin(\omega_n x)}{\omega_n}$ explicitly (antiderivative $+\frac{\cos(\omega_n x)}{\omega_n^2}$):

$$ a_n = \frac{1}{L}\left(0 + \left[\frac{\cos(\omega_n x)}{\omega_n^2}\right]_{0}^{L}\right) = \frac{\cos(n\pi) - \cos(0)}{L\omega_n^2} = \frac{(-1)^n - 1}{L\cdot\frac{(n\pi)^2}{L^2}} = \frac{L\big((-1)^n - 1\big)}{(n\pi)^2}, \qquad n \ge 1. $$

Thus $a_n = 0$ for even $n$ and $a_{2k+1} = -\frac{2L}{((2k+1)\pi)^2}$ for odd $n = 2k+1$.

For $b_n$ ($n \ge 1$), note that $\int_{-L}^{L} 1\cdot\sin(\omega_n x)\,dx = 0$, leaving $\frac{1}{L}\int_{0}^{L} x\sin(\omega_n x)\,dx$. We integrate by parts with $u = x$, $dv = \sin(\omega_n x)\,dx$, giving $du = dx$ and $v = -\frac{\cos(\omega_n x)}{\omega_n}$.

$$ b_n = \frac{1}{L}\int_{0}^{L} x\sin(\omega_n x)\,dx = \frac{1}{L}\left(\left[-\frac{x\cos(\omega_n x)}{\omega_n}\right]_{0}^{L} + \int_{0}^{L} \frac{\cos(\omega_n x)}{\omega_n}\,dx\right). $$

Applying Barrow's rule with $\cos(n\pi) = (-1)^n$ and $\sin(n\pi) = \sin(0) = 0$:

$$ b_n = \frac{1}{L}\left(-\frac{L\cos(n\pi)}{\omega_n} + \left[\frac{\sin(\omega_n x)}{\omega_n^2}\right]_{0}^{L}\right) = -\frac{(-1)^n}{\omega_n} + 0 = -\frac{L(-1)^n}{n\pi}, \qquad n \ge 1. $$

## The series

Assembling the coefficients gives the three Fourier series on $[-L, L]$:

- **(i)** $f(x) = x^2$:
$$ x^2 \sim \frac{L^2}{3} + \frac{4L^2}{\pi^2}\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}\cos\left(\frac{n\pi x}{L}\right). $$
- **(ii)** $f(x) = e^x$:
$$ e^x \sim \frac{\sinh L}{L} + 2\sinh L \sum_{n=1}^{\infty} \frac{(-1)^n}{L^2 + (n\pi)^2}\left[L\cos\left(\frac{n\pi x}{L}\right) - n\pi\sin\left(\frac{n\pi x}{L}\right)\right]. $$
- **(iii)** $f(x) = 1$ ($x < 0$), $x + 1$ ($x \ge 0$):
$$ f(x) \sim \left(1 + \frac{L}{4}\right) + \sum_{n=1}^{\infty}\left[\frac{L\big((-1)^n - 1\big)}{(n\pi)^2}\cos\left(\frac{n\pi x}{L}\right) - \frac{L(-1)^n}{n\pi}\sin\left(\frac{n\pi x}{L}\right)\right]. $$

## Convergence at the jumps

We now compare the graph of each Fourier series (its pointwise limit $\tilde{f}_{\text{FS}}(x)$) against the graph of the original function $f(x)$ on $[-3L, 3L]$.

### (i) $f(x) = x^2$

Because $f(-L) = f(L) = L^2$, the $2L$-periodic extension has no jumps anywhere on $\mathbb{R}$. Hence the Fourier series converges to $x^2$ at **every** point of $[-L, L]$ (including $x = \pm L$), and outside $[-L, L]$ it forms a continuous periodic chain of parabolic arches of height $L^2$, diverging from the unbounded parabola $y = x^2$.

![[attachments/AM-PS/ch6-e8-i.svg]]
*Original function $f(x) = x^2$ (dashed) compared with the $2L$-periodic limit of its Fourier series (solid) on $[-3L, 3L]$. They agree identically on $[-L, L]$ and are continuous at every periodic joint $x = \pm L$.*

### (ii) $f(x) = e^x$

On the open interval $(-L, L)$, the Fourier series converges to $e^x$. At every odd multiple $x = (2k+1)L$ ($k \in \mathbb{Z}$), including $x = -L$ and $x = L$, the periodic extension jumps between $e^L$ (from the left) and $e^{-L}$ (from the right), so by Fourier's convergence theorem the series converges to the midpoint

$$ \tilde{f}_{\text{FS}}\big((2k+1)L\big) = \frac{e^L + e^{-L}}{2} = \cosh L. $$

Outside $[-L, L]$, the Fourier series repeats this bounded exponential sawtooth periodically, while $e^x$ grows without bound for $x > L$ and decays toward $0$ for $x < -L$.

![[attachments/AM-PS/ch6-e8-ii.svg]]
*Original function $f(x) = e^x$ (dashed) compared with its Fourier series limit (solid) on $[-3L, 3L]$. Open circles mark the one-sided limits $e^{-L}$ and $e^L$ at $x = \pm L$, and filled dots mark the jump midpoint $\cosh L$.*

### (iii) $f(x) = 1$ ($x < 0$), $x + 1$ ($x \ge 0$)

On the open interval $(-L, L)$, the function is continuous everywhere—including at $x = 0$, where $\lim_{x \to 0^-} f(x) = 1 = \lim_{x \to 0^+} f(x)$—so the Fourier series converges to $f(x)$ throughout $(-L, L)$. At every odd multiple $x = (2k+1)L$ ($k \in \mathbb{Z}$), the periodic extension jumps from $L + 1$ (on the left) to $1$ (on the right), so the Fourier series converges to the midpoint

$$ \tilde{f}_{\text{FS}}\big((2k+1)L\big) = \frac{(L + 1) + 1}{2} = 1 + \frac{L}{2}. $$

Outside $[-L, L]$, the Fourier series repeats the flat-then-ramp wave periodically, whereas $f(x)$ remains constant at $1$ for $x < -L$ and increases linearly as $x + 1$ for $x > L$.

![[attachments/AM-PS/ch6-e8-iii.svg]]
*Original function (dashed) compared with its Fourier series limit (solid) on $[-3L, 3L]$. The graph is continuous at $x = 0$ (value $1$) and has jump discontinuities at $x = \pm L$, where filled dots mark the midpoint $1 + L/2$.*

## Answers and checks

1. **Consistency of (i) with Exercise 6.5 (v)**: Setting $L = \pi$ in (i) gives $a_0 = \frac{\pi^2}{3}$ and $a_n = \frac{4\pi^2(-1)^n}{(n\pi)^2} = \frac{4(-1)^n}{n^2}$, reproducing [[Problem - Ch6-P5 Nine Fourier Series Expansions]] (v) identically.
2. **Midpoint check for (ii) at $x = L$**: Substituting $x = L$ into series (ii) sets $\sin(n\pi) = 0$ and $\cos(n\pi) = (-1)^n$, so $(-1)^n\cos(n\pi) = 1$, leaving
$$ \frac{\sinh L}{L} + 2L\sinh L\sum_{n=1}^{\infty} \frac{1}{L^2 + (n\pi)^2} = \cosh L, $$
which is the classical partial-fraction expansion of $\coth L = \frac{1}{L} + \sum_{n=1}^{\infty} \frac{2L}{L^2 + (n\pi)^2}$ multiplied by $\sinh L$.
3. **Continuity and midpoint check for (iii)**:
   - At $x = 0$: $\sin(0) = 0$, $\cos(0) = 1$, so the series gives $1 + \frac{L}{4} - \frac{2L}{\pi^2}\sum_{k=0}^\infty \frac{1}{(2k+1)^2} = 1 + \frac{L}{4} - \frac{2L}{\pi^2}\cdot\frac{\pi^2}{8} = 1 + \frac{L}{4} - \frac{L}{4} = 1 = f(0)$.
   - At $x = L$: $\sin(n\pi) = 0$, $\cos(n\pi) = (-1)^n = -1$ for odd $n$, so the series gives $1 + \frac{L}{4} + \frac{2L}{\pi^2}\sum_{k=0}^\infty \frac{1}{(2k+1)^2} = 1 + \frac{L}{4} + \frac{L}{4} = 1 + \frac{L}{2}$, matching the jump midpoint exactly!

> [!result] Key results
> - **(i) $f(x) = x^2$**: $a_0 = \frac{L^2}{3}$, $a_n = \frac{4L^2(-1)^n}{(n\pi)^2}$, $b_n = 0$. Continuous periodic extension everywhere ($f(-L) = f(L) = L^2$); agrees with $x^2$ on all of $[-L, L]$ and repeats periodically outside.
> - **(ii) $f(x) = e^x$**: $a_0 = \frac{\sinh L}{L}$, $a_n = \frac{2L(-1)^n\sinh L}{L^2 + (n\pi)^2}$, $b_n = -\frac{2n\pi(-1)^n\sinh L}{L^2 + (n\pi)^2}$. Agrees with $e^x$ on $(-L, L)$; jumps at $x = (2k+1)L$ between $e^L$ and $e^{-L}$, converging to $\cosh L$.
> - **(iii) $f(x) = 1$ ($x < 0$), $x+1$ ($x \ge 0$)**: $a_0 = 1 + \frac{L}{4}$, $a_n = \frac{L((-1)^n - 1)}{(n\pi)^2}$, $b_n = -\frac{L(-1)^n}{n\pi}$. Continuous at $x = 0$ (value $1$), agrees with $f(x)$ on $(-L, L)$, and jumps at $x = (2k+1)L$ between $L+1$ and $1$, converging to $1 + \frac{L}{2}$.
