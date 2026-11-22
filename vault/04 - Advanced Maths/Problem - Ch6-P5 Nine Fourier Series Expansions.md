---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 5"
dificultad: media
id: "e5"
pill: "Euler-Fourier Formulas • Nine Functions • Jump Convergence"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.5: Nine Fourier Series Expansions

> Official exercise 5 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Calculate the Fourier series for the given functions:

- (i) $f(x) = 1$, $-\pi \le x \le \pi$.
- (ii) $f(x) = x$, $-\pi \le x \le \pi$.
- (iii) $f(x) = \pi - x$, $-\pi \le x \le \pi$.
- (iv) $f(x) = |x|$, $-\pi \le x \le \pi$.
- (v) $f(x) = x^2$, $-\pi \le x \le \pi$.
- (vi) $f(x) = \cos x$, $0 \le x \le \pi$.
- (vii) $f(x) = \begin{cases} 0, & -\pi \le x < 0, \\ \pi, & 0 \le x \le \pi. \end{cases}$
- (viii) $f(x) = \begin{cases} -\pi/2, & -\pi \le x < 0, \\ \pi/2, & 0 \le x \le \pi. \end{cases}$
- (ix) $f(x) = \begin{cases} 1, & 0 \le x \le \pi/2, \\ 2, & \pi/2 \le x \le \pi. \end{cases}$

## Extension of f

We begin by identifying the domain, period, and parity of each function so we know which periodic extension $\tilde{f}(x)$ the Fourier series represents and which coefficients vanish by symmetry (`Notes09-12-Nov.pdf`, pp. 10–12; Haberman Sec. 3.2–3.3).

For a piecewise smooth function on $[-L, L]$, the full Fourier series is

$$ f(x) \sim a_0 + \sum_{n=1}^{\infty}\left[a_n\cos\frac{n\pi x}{L} + b_n\sin\frac{n\pi x}{L}\right], $$

with the Euler-Fourier coefficients

$$ a_0 = \frac{1}{2L}\int_{-L}^{L} f(x)\,dx, \qquad a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\frac{n\pi x}{L}\,dx, \qquad b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\frac{n\pi x}{L}\,dx. $$

For cases (i)–(v), (vii), and (viii), the domain is $[-\pi, \pi]$, so $L = \pi$ and $\frac{n\pi x}{L} = nx$; the series represents the $2\pi$-periodic extension $\tilde{f}(x + 2\pi) = \tilde{f}(x)$. For cases (vi) and (ix), the function is given only on the half-interval $[0, \pi]$ (Haberman Sec. 3.3). Because the statement does not specify which extension is requested on $[0, \pi]$, we compute all three standard expansions:

1. **Even $2\pi$-periodic extension** (Fourier cosine series on $[0, \pi]$, $L = \pi$, $b_n = 0$).
2. **Odd $2\pi$-periodic extension** (Fourier sine series on $[0, \pi]$, $L = \pi$, $a_0 = a_n = 0$).
3. **Direct $\pi$-periodic full Fourier series** on $[0, \pi]$ (half-period $L = \pi/2$, basis $\cos(2nx), \sin(2nx)$).

The table below summarizes the domain, parity, and endpoint matching of all nine functions.

| Case | Interval | Parity on $[-\pi,\pi]$ | Endpoint values | Jumps of periodic extension |
| :--- | :--- | :--- | :--- | :--- |
| (i) $1$ | $[-\pi,\pi]$ | Even | $f(-\pi) = f(\pi) = 1$ | None (continuous everywhere) |
| (ii) $x$ | $[-\pi,\pi]$ | Odd | $f(-\pi) = -\pi,\; f(\pi) = \pi$ | $x = (2k+1)\pi$ |
| (iii) $\pi - x$ | $[-\pi,\pi]$ | Neither | $f(-\pi) = 2\pi,\; f(\pi) = 0$ | $x = (2k+1)\pi$ |
| (iv) $\|x\|$ | $[-\pi,\pi]$ | Even | $f(-\pi) = f(\pi) = \pi$ | None (continuous everywhere) |
| (v) $x^2$ | $[-\pi,\pi]$ | Even | $f(-\pi) = f(\pi) = \pi^2$ | None (continuous everywhere) |
| (vi) $\cos x$ | $[0,\pi]$ | Half-range | $f(0) = 1,\; f(\pi) = -1$ | Depends on extension |
| (vii) $0 / \pi$ | $[-\pi,\pi]$ | Neither | $f(-\pi) = 0,\; f(\pi) = \pi$ | $x = m\pi$ ($m \in \mathbb{Z}$) |
| (viii) $-\frac{\pi}{2} / \frac{\pi}{2}$ | $[-\pi,\pi]$ | Odd | $f(-\pi) = -\frac{\pi}{2},\; f(\pi) = \frac{\pi}{2}$ | $x = m\pi$ ($m \in \mathbb{Z}$) |
| (ix) $1 / 2$ | $[0,\pi]$ | Half-range | $f(0) = 1,\; f(\pi) = 2$ | $x = \pi/2$ and possibly endpoints |

## Coefficients a_0, a_n, b_n

We now evaluate $a_0$, $a_n$, and $b_n$ for each function in turn, showing every antiderivative, integration by parts, and application of Barrow's rule explicitly.

### (i) $f(x) = 1$ on $[-\pi, \pi]$

We compute $a_0$ directly by integrating the constant $1$ over $[-\pi, \pi]$.

$$ a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} 1\,dx = \frac{1}{2\pi}\Big[x\Big]_{-\pi}^{\pi} = \frac{1}{2\pi}\big(\pi - (-\pi)\big) = \frac{2\pi}{2\pi} = 1. $$

Next we compute $a_n$ for $n \ge 1$ using the antiderivative $\int \cos(nx)\,dx = \frac{1}{n}\sin(nx)$ and the identity $\sin(n\pi) = 0$.

$$ a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} \cos(nx)\,dx = \frac{1}{\pi}\left[\frac{\sin(nx)}{n}\right]_{-\pi}^{\pi} = \frac{1}{n\pi}\big(\sin(n\pi) - \sin(-n\pi)\big) = \frac{1}{n\pi}(0 - 0) = 0. $$

Next we compute $b_n$ for $n \ge 1$ using the antiderivative $\int \sin(nx)\,dx = -\frac{1}{n}\cos(nx)$ and the parity $\cos(-n\pi) = \cos(n\pi)$.

$$ b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} \sin(nx)\,dx = \frac{1}{\pi}\left[-\frac{\cos(nx)}{n}\right]_{-\pi}^{\pi} = -\frac{1}{n\pi}\big(\cos(n\pi) - \cos(-n\pi)\big) = 0. $$

### (ii) $f(x) = x$ on $[-\pi, \pi]$

Because $f(-x) = -x = -f(x)$ is odd on the symmetric interval $[-\pi, \pi]$, both $f(x)$ and $f(x)\cos(nx)$ are odd integrands, so $a_0 = 0$ and $a_n = 0$ for all $n \ge 1$ (proved explicitly in [[Problem - Ch6-P9 Fourier Series of Even and Odd Periodic Functions]]). Meanwhile $x\sin(nx)$ is even, so we fold the integral onto $[0, \pi]$.

$$ b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin(nx)\,dx = \frac{2}{\pi}\int_{0}^{\pi} x\sin(nx)\,dx. $$

We integrate by parts to remove the linear factor $x$: choose $u = x$ and $dv = \sin(nx)\,dx$, which give $du = dx$ and $v = -\frac{\cos(nx)}{n}$.

$$ \int_{0}^{\pi} x\sin(nx)\,dx = \left[-\frac{x\cos(nx)}{n}\right]_{0}^{\pi} - \int_{0}^{\pi} \left(-\frac{\cos(nx)}{n}\right)dx = \left[-\frac{x\cos(nx)}{n}\right]_{0}^{\pi} + \frac{1}{n}\left[\frac{\sin(nx)}{n}\right]_{0}^{\pi}. $$

Now we apply Barrow's rule to both bracketed terms using $\cos(n\pi) = (-1)^n$, $\sin(n\pi) = 0$, and $\sin(0) = 0$.

$$ \int_{0}^{\pi} x\sin(nx)\,dx = \left(-\frac{\pi\cos(n\pi)}{n} - 0\right) + \frac{1}{n^2}\big(\sin(n\pi) - \sin(0)\big) = -\frac{\pi(-1)^n}{n} + 0 = \frac{\pi(-1)^{n+1}}{n}. $$

Multiplying by the prefactor $\frac{2}{\pi}$ gives $b_n$.

$$ b_n = \frac{2}{\pi}\cdot\frac{\pi(-1)^{n+1}}{n} = \frac{2(-1)^{n+1}}{n}, \qquad n \ge 1. $$

### (iii) $f(x) = \pi - x$ on $[-\pi, \pi]$

We compute $a_0$ directly by integrating $\pi - x$ term by term on $[-\pi, \pi]$.

$$ a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} (\pi - x)\,dx = \frac{1}{2\pi}\left[\pi x - \frac{x^2}{2}\right]_{-\pi}^{\pi} = \frac{1}{2\pi}\left[\left(\pi^2 - \frac{\pi^2}{2}\right) - \left(-\pi^2 - \frac{\pi^2}{2}\right)\right] = \frac{2\pi^2}{2\pi} = \pi. $$

For $a_n$ ($n \ge 1$), we split the integral by linearity into $\pi\cos(nx)$ (whose integral over $[-\pi, \pi]$ is $0$ from case (i)) and $-x\cos(nx)$ (an odd integrand on $[-\pi, \pi]$, whose integral is also $0$).

$$ a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} (\pi - x)\cos(nx)\,dx = \int_{-\pi}^{\pi} \cos(nx)\,dx - \frac{1}{\pi}\int_{-\pi}^{\pi} x\cos(nx)\,dx = 0 - 0 = 0. $$

For $b_n$ ($n \ge 1$), we again split by linearity and reuse cases (i) and (ii).

$$ b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} (\pi - x)\sin(nx)\,dx = \int_{-\pi}^{\pi} \sin(nx)\,dx - \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin(nx)\,dx = 0 - \frac{2(-1)^{n+1}}{n} = \frac{2(-1)^n}{n}. $$

### (iv) $f(x) = |x|$ on $[-\pi, \pi]$

Because $|-x| = |x|$, the function $f(x) = |x|$ is even on $[-\pi, \pi]$, so $|x|\sin(nx)$ is odd and $b_n = 0$ for all $n \ge 1$. For $a_0$ and $a_n$ we fold the even integrands onto $[0, \pi]$, where $|x| = x$.

We evaluate $a_0$ using the antiderivative $\int x\,dx = \frac{x^2}{2}$.

$$ a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} |x|\,dx = \frac{1}{\pi}\int_{0}^{\pi} x\,dx = \frac{1}{\pi}\left[\frac{x^2}{2}\right]_{0}^{\pi} = \frac{1}{\pi}\left(\frac{\pi^2}{2} - 0\right) = \frac{\pi}{2}. $$

For $a_n$ ($n \ge 1$), we integrate by parts with $u = x$, $dv = \cos(nx)\,dx$, so $du = dx$ and $v = \frac{\sin(nx)}{n}$.

$$ a_n = \frac{2}{\pi}\int_{0}^{\pi} x\cos(nx)\,dx = \frac{2}{\pi}\left(\left[\frac{x\sin(nx)}{n}\right]_{0}^{\pi} - \int_{0}^{\pi} \frac{\sin(nx)}{n}\,dx\right). $$

We evaluate the boundary term and integrate $-\frac{\sin(nx)}{n}$ explicitly, whose antiderivative is $+\frac{\cos(nx)}{n^2}$.

$$ a_n = \frac{2}{\pi}\left(\frac{\pi\sin(n\pi) - 0}{n} + \left[\frac{\cos(nx)}{n^2}\right]_{0}^{\pi}\right) = \frac{2}{\pi}\left(0 + \frac{\cos(n\pi) - \cos(0)}{n^2}\right) = \frac{2\big((-1)^n - 1\big)}{\pi n^2}. $$

Separating even and odd $n$, we note that $(-1)^n - 1 = 0$ when $n = 2k$ is even and $(-1)^n - 1 = -2$ when $n = 2k+1$ is odd.

$$ a_n = \begin{cases} 0, & n \text{ even}, \\ -\dfrac{4}{\pi n^2}, & n \text{ odd}. \end{cases} $$

### (v) $f(x) = x^2$ on $[-\pi, \pi]$

Because $(-x)^2 = x^2$, the function is even on $[-\pi, \pi]$, so $b_n = 0$ for all $n \ge 1$ and we fold $a_0$ and $a_n$ onto $[0, \pi]$.

We compute $a_0$ using the antiderivative $\int x^2\,dx = \frac{x^3}{3}$.

$$ a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} x^2\,dx = \frac{1}{\pi}\int_{0}^{\pi} x^2\,dx = \frac{1}{\pi}\left[\frac{x^3}{3}\right]_{0}^{\pi} = \frac{1}{\pi}\left(\frac{\pi^3}{3} - 0\right) = \frac{\pi^2}{3}. $$

For $a_n$ ($n \ge 1$), we apply integration by parts a first time with $u_1 = x^2$, $dv_1 = \cos(nx)\,dx$, giving $du_1 = 2x\,dx$ and $v_1 = \frac{\sin(nx)}{n}$.

$$ \int_{0}^{\pi} x^2\cos(nx)\,dx = \left[\frac{x^2\sin(nx)}{n}\right]_{0}^{\pi} - \frac{2}{n}\int_{0}^{\pi} x\sin(nx)\,dx = \left(\frac{\pi^2\sin(n\pi)}{n} - 0\right) - \frac{2}{n}\int_{0}^{\pi} x\sin(nx)\,dx = -\frac{2}{n}\int_{0}^{\pi} x\sin(nx)\,dx. $$

We apply integration by parts a second time to $\int_0^\pi x\sin(nx)\,dx$ with $u_2 = x$, $dv_2 = \sin(nx)\,dx$, giving $du_2 = dx$ and $v_2 = -\frac{\cos(nx)}{n}$.

$$ \int_{0}^{\pi} x\sin(nx)\,dx = \left[-\frac{x\cos(nx)}{n}\right]_{0}^{\pi} + \frac{1}{n}\int_{0}^{\pi} \cos(nx)\,dx = -\frac{\pi\cos(n\pi)}{n} + \frac{1}{n}\left[\frac{\sin(nx)}{n}\right]_{0}^{\pi} = -\frac{\pi(-1)^n}{n} + 0. $$

Substituting this back into $a_n = \frac{2}{\pi}\int_0^\pi x^2\cos(nx)\,dx$ yields $a_n$.

$$ a_n = \frac{2}{\pi}\left(-\frac{2}{n}\right)\left(-\frac{\pi(-1)^n}{n}\right) = \frac{4(-1)^n}{n^2}, \qquad n \ge 1. $$

### (vi) $f(x) = \cos x$ on $[0, \pi]$

Because $f(x) = \cos x$ is given only on $[0, \pi]$, we compute all three standard Fourier expansions on this interval.

#### 1. Even $2\pi$-periodic extension (Fourier cosine series on $[0, \pi]$)

Extending $\cos x$ evenly to $[-\pi, \pi]$ reproduces $\cos x$ itself, so $b_n = 0$ for all $n \ge 1$, and by orthogonality of $\{1, \cos(nx)\}$ on $[0, \pi]$ (proved in [[Problem - Ch6-P7 Orthogonality of Sine and Cosine Systems]]), we verify each coefficient explicitly.

$$ a_0 = \frac{1}{\pi}\int_{0}^{\pi} \cos x\,dx = \frac{1}{\pi}\Big[\sin x\Big]_{0}^{\pi} = \frac{1}{\pi}(0 - 0) = 0. $$

For $n = 1$, we use the half-angle identity $\cos^2 x = \frac{1 + \cos(2x)}{2}$.

$$ a_1 = \frac{2}{\pi}\int_{0}^{\pi} \cos^2 x\,dx = \frac{2}{\pi}\int_{0}^{\pi} \frac{1 + \cos(2x)}{2}\,dx = \frac{1}{\pi}\left[x + \frac{\sin(2x)}{2}\right]_{0}^{\pi} = \frac{1}{\pi}\big((\pi + 0) - (0 + 0)\big) = 1. $$

For $n \ge 2$, we apply the product-to-sum identity $\cos x\cos(nx) = \frac{1}{2}\big[\cos((n-1)x) + \cos((n+1)x)\big]$.

$$ a_n = \frac{2}{\pi}\int_{0}^{\pi} \frac{\cos((n-1)x) + \cos((n+1)x)}{2}\,dx = \frac{1}{\pi}\left[\frac{\sin((n-1)x)}{n-1} + \frac{\sin((n+1)x)}{n+1}\right]_{0}^{\pi} = 0. $$

#### 2. Odd $2\pi$-periodic extension (Fourier sine series on $[0, \pi]$)

For the odd extension, $a_0 = 0$ and $a_n = 0$ for all $n \ge 1$, while $b_n = \frac{2}{\pi}\int_{0}^{\pi} \cos x\sin(nx)\,dx$.

First we check $n = 1$ using $\sin(2x) = 2\sin x\cos x$.

$$ b_1 = \frac{2}{\pi}\int_{0}^{\pi} \cos x\sin x\,dx = \frac{1}{\pi}\int_{0}^{\pi} \sin(2x)\,dx = \frac{1}{\pi}\left[-\frac{\cos(2x)}{2}\right]_{0}^{\pi} = -\frac{1}{2\pi}\big(\cos(2\pi) - \cos(0)\big) = -\frac{1}{2\pi}(1 - 1) = 0. $$

For $n \ge 2$, we apply the product-to-sum identity $\sin A\cos B = \frac{1}{2}\big[\sin(A+B) + \sin(A-B)\big]$ with $A = nx$ and $B = x$.

$$ b_n = \frac{2}{\pi}\int_{0}^{\pi} \frac{\sin((n+1)x) + \sin((n-1)x)}{2}\,dx = \frac{1}{\pi}\left[-\frac{\cos((n+1)x)}{n+1} - \frac{\cos((n-1)x)}{n-1}\right]_{0}^{\pi}. $$

We apply Barrow's rule using $\cos((n+1)\pi) = (-1)^{n+1} = -(-1)^n$ and $\cos((n-1)\pi) = (-1)^{n-1} = -(-1)^n$.

$$ b_n = \frac{1}{\pi}\left[\frac{1 - (-1)^{n+1}}{n+1} + \frac{1 - (-1)^{n-1}}{n-1}\right] = \frac{1 + (-1)^n}{\pi}\left(\frac{1}{n+1} + \frac{1}{n-1}\right) = \frac{1 + (-1)^n}{\pi}\cdot\frac{2n}{n^2 - 1} = \frac{2n\big(1 + (-1)^n\big)}{\pi(n^2 - 1)}. $$

When $n$ is odd, $1 + (-1)^n = 0$, so $b_{2k+1} = 0$. When $n = 2k$ ($k \ge 1$) is even, $1 + (-1)^{2k} = 2$, so

$$ b_{2k} = \frac{2(2k)\cdot 2}{\pi((2k)^2 - 1)} = \frac{8k}{\pi(4k^2 - 1)}, \qquad k \ge 1. $$

#### 3. Direct $\pi$-periodic full Fourier series on $[0, \pi]$ ($L = \pi/2$)

Taking $[0, \pi]$ itself as one full period $2L = \pi$ ($L = \pi/2$), the basis functions are $\cos(2nx)$ and $\sin(2nx)$ with $\frac{1}{2L} = \frac{1}{\pi}$ and $\frac{1}{L} = \frac{2}{\pi}$.

$$ a_0 = \frac{1}{\pi}\int_{0}^{\pi} \cos x\,dx = \frac{1}{\pi}\Big[\sin x\Big]_{0}^{\pi} = 0. $$

For $a_n$ ($n \ge 1$), we apply $\cos x\cos(2nx) = \frac{1}{2}\big[\cos((2n-1)x) + \cos((2n+1)x)\big]$; since $2n \pm 1 \neq 0$, every sine vanishes at $0$ and $\pi$.

$$ a_n = \frac{2}{\pi}\int_{0}^{\pi} \cos x\cos(2nx)\,dx = \frac{1}{\pi}\left[\frac{\sin((2n-1)x)}{2n-1} + \frac{\sin((2n+1)x)}{2n+1}\right]_{0}^{\pi} = 0. $$

For $b_n$ ($n \ge 1$), we use $\sin(2nx)\cos x = \frac{1}{2}\big[\sin((2n+1)x) + \sin((2n-1)x)\big]$ and note that $\cos((2n\pm 1)\pi) = -1$.

$$ b_n = \frac{2}{\pi}\int_{0}^{\pi} \cos x\sin(2nx)\,dx = \frac{1}{\pi}\left[-\frac{\cos((2n+1)x)}{2n+1} - \frac{\cos((2n-1)x)}{2n-1}\right]_{0}^{\pi} = \frac{1}{\pi}\left(\frac{2}{2n+1} + \frac{2}{2n-1}\right) = \frac{8n}{\pi(4n^2 - 1)}. $$

Notice that the direct $\pi$-periodic series coincides identically with the odd $2\pi$-periodic sine series because the odd extension of $\cos x$ on $[-\pi, \pi]$ already has period $\pi$!

### (vii) $f(x) = \begin{cases} 0, & -\pi \le x < 0, \\ \pi, & 0 \le x \le \pi \end{cases}$

Because $f(x) = 0$ on $[-\pi, 0)$, every integral collapses to $[0, \pi]$ where $f(x) = \pi$.

We compute $a_0$ directly.

$$ a_0 = \frac{1}{2\pi}\int_{0}^{\pi} \pi\,dx = \frac{1}{2}\Big[x\Big]_{0}^{\pi} = \frac{\pi}{2}. $$

Next we compute $a_n$ for $n \ge 1$.

$$ a_n = \frac{1}{\pi}\int_{0}^{\pi} \pi\cos(nx)\,dx = \left[\frac{\sin(nx)}{n}\right]_{0}^{\pi} = \frac{\sin(n\pi) - \sin(0)}{n} = 0. $$

Next we compute $b_n$ for $n \ge 1$ using $\cos(n\pi) = (-1)^n$ and $\cos(0) = 1$.

$$ b_n = \frac{1}{\pi}\int_{0}^{\pi} \pi\sin(nx)\,dx = \left[-\frac{\cos(nx)}{n}\right]_{0}^{\pi} = -\frac{\cos(n\pi) - \cos(0)}{n} = \frac{1 - (-1)^n}{n}. $$

Thus $b_n = 0$ for even $n$ and $b_{2k+1} = \frac{2}{2k+1}$ for odd $n = 2k+1$ ($k \ge 0$).

### (viii) $f(x) = \begin{cases} -\pi/2, & -\pi \le x < 0, \\ \pi/2, & 0 \le x \le \pi \end{cases}$

Observe that $f_{\text{viii}}(x) = f_{\text{vii}}(x) - \frac{\pi}{2}$ for all $x \in [-\pi, \pi]$, and moreover $f_{\text{viii}}(-x) = -f_{\text{viii}}(x)$ for $x \neq 0$, so $f_{\text{viii}}$ is odd on $[-\pi, \pi]$. We verify $a_0$, $a_n$, and $b_n$ directly by splitting at $x = 0$.

$$ a_0 = \frac{1}{2\pi}\left(\int_{-\pi}^{0} \left(-\frac{\pi}{2}\right)dx + \int_{0}^{\pi} \frac{\pi}{2}\,dx\right) = \frac{1}{2\pi}\left(-\frac{\pi^2}{2} + \frac{\pi^2}{2}\right) = 0. $$

$$ a_n = \frac{1}{\pi}\left(-\frac{\pi}{2}\left[\frac{\sin(nx)}{n}\right]_{-\pi}^{0} + \frac{\pi}{2}\left[\frac{\sin(nx)}{n}\right]_{0}^{\pi}\right) = 0. $$

For $b_n$ ($n \ge 1$), since the integrand is even, we fold onto $[0, \pi]$.

$$ b_n = \frac{2}{\pi}\int_{0}^{\pi} \frac{\pi}{2}\sin(nx)\,dx = \int_{0}^{\pi} \sin(nx)\,dx = \left[-\frac{\cos(nx)}{n}\right]_{0}^{\pi} = \frac{1 - (-1)^n}{n}. $$

Thus $b_{2k} = 0$ and $b_{2k+1} = \frac{2}{2k+1}$, identical to case (vii) except that the constant term $a_0$ shifts from $\pi/2$ to $0$.

### (ix) $f(x) = \begin{cases} 1, & 0 \le x \le \pi/2, \\ 2, & \pi/2 \le x \le \pi \end{cases}$

Because $f$ is given only on $[0, \pi]$, we again compute all three standard expansions.

#### 1. Even $2\pi$-periodic extension (Fourier cosine series on $[0, \pi]$)

Here $b_n = 0$ for all $n \ge 1$. We split the integrals at $x = \pi/2$.

$$ a_0 = \frac{1}{\pi}\left(\int_{0}^{\pi/2} 1\,dx + \int_{\pi/2}^{\pi} 2\,dx\right) = \frac{1}{\pi}\left(\frac{\pi}{2} + 2\cdot\frac{\pi}{2}\right) = \frac{3}{2}. $$

For $a_n$ ($n \ge 1$), we integrate $\cos(nx)$ on each subinterval and apply Barrow's rule.

$$ a_n = \frac{2}{\pi}\left(\int_{0}^{\pi/2} \cos(nx)\,dx + \int_{\pi/2}^{\pi} 2\cos(nx)\,dx\right) = \frac{2}{\pi}\left(\left[\frac{\sin(nx)}{n}\right]_{0}^{\pi/2} + 2\left[\frac{\sin(nx)}{n}\right]_{\pi/2}^{\pi}\right). $$

Evaluating at the endpoints using $\sin(0) = 0$ and $\sin(n\pi) = 0$:

$$ a_n = \frac{2}{n\pi}\left(\sin\frac{n\pi}{2} - 0 + 2\left(0 - \sin\frac{n\pi}{2}\right)\right) = -\frac{2\sin(n\pi/2)}{n\pi}. $$

When $n$ is even, $\sin(n\pi/2) = 0$, so $a_{2k} = 0$. When $n = 2k+1$ ($k \ge 0$) is odd, $\sin\big((2k+1)\frac{\pi}{2}\big) = (-1)^k$, so

$$ a_{2k+1} = -\frac{2(-1)^k}{(2k+1)\pi}, \qquad k \ge 0. $$

#### 2. Odd $2\pi$-periodic extension (Fourier sine series on $[0, \pi]$)

Here $a_0 = 0$ and $a_n = 0$ for all $n \ge 1$, and we split $b_n$ at $x = \pi/2$.

$$ b_n = \frac{2}{\pi}\left(\int_{0}^{\pi/2} \sin(nx)\,dx + \int_{\pi/2}^{\pi} 2\sin(nx)\,dx\right) = \frac{2}{\pi}\left(\left[-\frac{\cos(nx)}{n}\right]_{0}^{\pi/2} + 2\left[-\frac{\cos(nx)}{n}\right]_{\pi/2}^{\pi}\right). $$

Applying Barrow's rule with $\cos(0) = 1$ and $\cos(n\pi) = (-1)^n$:

$$ b_n = \frac{2}{n\pi}\left(1 - \cos\frac{n\pi}{2} + 2\left(\cos\frac{n\pi}{2} - (-1)^n\right)\right) = \frac{2\big(1 + \cos(n\pi/2) - 2(-1)^n\big)}{n\pi}. $$

#### 3. Direct $\pi$-periodic full Fourier series on $[0, \pi]$ ($L = \pi/2$)

With $L = \pi/2$, the basis is $\cos(2nx)$ and $\sin(2nx)$.

$$ a_0 = \frac{1}{\pi}\left(\int_{0}^{\pi/2} 1\,dx + \int_{\pi/2}^{\pi} 2\,dx\right) = \frac{3}{2}. $$

For $a_n$ ($n \ge 1$), every boundary sine vanishes because $\sin(n\pi) = 0$ and $\sin(2n\pi) = 0$.

$$ a_n = \frac{2}{\pi}\left(\left[\frac{\sin(2nx)}{2n}\right]_{0}^{\pi/2} + 2\left[\frac{\sin(2nx)}{2n}\right]_{\pi/2}^{\pi}\right) = \frac{1}{n\pi}\big((\sin(n\pi) - 0) + 2(\sin(2n\pi) - \sin(n\pi))\big) = 0. $$

For $b_n$ ($n \ge 1$), we use $\cos(n\pi) = (-1)^n$ and $\cos(2n\pi) = 1$.

$$ b_n = \frac{2}{\pi}\left(\left[-\frac{\cos(2nx)}{2n}\right]_{0}^{\pi/2} + 2\left[-\frac{\cos(2nx)}{2n}\right]_{\pi/2}^{\pi}\right) = \frac{1}{n\pi}\big((1 - (-1)^n) + 2((-1)^n - 1)\big) = -\frac{1 - (-1)^n}{n\pi}. $$

Thus $b_{2k} = 0$ and $b_{2k+1} = -\frac{2}{(2k+1)\pi}$ ($k \ge 0$).

## The series

Assembling the coefficients from the previous section gives the nine Fourier series:

- **(i)** $f(x) = 1$:
$$ 1 \sim 1. $$
- **(ii)** $f(x) = x$ on $[-\pi, \pi]$:
$$ x \sim \sum_{n=1}^{\infty} \frac{2(-1)^{n+1}}{n}\sin(nx) = 2\left(\sin x - \frac{\sin(2x)}{2} + \frac{\sin(3x)}{3} - \cdots\right). $$
- **(iii)** $f(x) = \pi - x$ on $[-\pi, \pi]$:
$$ \pi - x \sim \pi + \sum_{n=1}^{\infty} \frac{2(-1)^{n}}{n}\sin(nx) = \pi - 2\left(\sin x - \frac{\sin(2x)}{2} + \frac{\sin(3x)}{3} - \cdots\right). $$
- **(iv)** $f(x) = |x|$ on $[-\pi, \pi]$:
$$ |x| \sim \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{\cos((2k+1)x)}{(2k+1)^2} = \frac{\pi}{2} - \frac{4}{\pi}\left(\cos x + \frac{\cos(3x)}{9} + \frac{\cos(5x)}{25} + \cdots\right). $$
- **(v)** $f(x) = x^2$ on $[-\pi, \pi]$:
$$ x^2 \sim \frac{\pi^2}{3} + 4\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}\cos(nx) = \frac{\pi^2}{3} - 4\left(\cos x - \frac{\cos(2x)}{4} + \frac{\cos(3x)}{9} - \cdots\right). $$
- **(vi)** $f(x) = \cos x$ on $[0, \pi]$:
- Even (cosine) extension of (vi): $\cos x \sim \cos x$.
- Odd (sine) extension and direct $\pi$-periodic extension of (vi) (identical):
$$ \cos x \sim \frac{8}{\pi}\sum_{k=1}^{\infty} \frac{k}{4k^2 - 1}\sin(2kx) = \frac{8}{\pi}\left(\frac{1}{3}\sin(2x) + \frac{2}{15}\sin(4x) + \frac{3}{35}\sin(6x) + \cdots\right). $$
- **(vii)** Step function $0$ on $[-\pi, 0)$, $\pi$ on $[0, \pi]$:
$$ f(x) \sim \frac{\pi}{2} + 2\sum_{k=0}^{\infty} \frac{\sin((2k+1)x)}{2k+1} = \frac{\pi}{2} + 2\left(\sin x + \frac{\sin(3x)}{3} + \frac{\sin(5x)}{5} + \cdots\right). $$
- **(viii)** Odd step function $-\pi/2$ on $[-\pi, 0)$, $\pi/2$ on $[0, \pi]$:
$$ f(x) \sim 2\sum_{k=0}^{\infty} \frac{\sin((2k+1)x)}{2k+1} = 2\left(\sin x + \frac{\sin(3x)}{3} + \frac{\sin(5x)}{5} + \cdots\right). $$
- **(ix)** Step function $1$ on $[0, \pi/2]$, $2$ on $[\pi/2, \pi]$:
- Even (cosine) extension of (ix):
$$ f(x) \sim \frac{3}{2} - \frac{2}{\pi}\sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}\cos\big((2k+1)x\big). $$
- Odd (sine) extension of (ix):
$$ f(x) \sim \frac{2}{\pi}\sum_{n=1}^{\infty} \frac{1 + \cos(n\pi/2) - 2(-1)^n}{n}\sin(nx). $$
- Direct $\pi$-periodic extension of (ix) ($L = \pi/2$):
$$ f(x) \sim \frac{3}{2} - \frac{2}{\pi}\sum_{k=0}^{\infty} \frac{\sin\big(2(2k+1)x\big)}{2k+1}. $$

## Convergence at the jumps

By Fourier's convergence theorem (`Notes09-12-Nov.pdf`, pp. 12–13; Haberman Sec. 3.2), the Fourier series of a piecewise smooth function converges to $\tilde{f}(x)$ wherever the periodic extension $\tilde{f}$ is continuous, and to the midpoint $\frac{1}{2}\big[\tilde{f}(x^+) + \tilde{f}(x^-)\big]$ at every jump discontinuity.

- **(i), (iv), (v)**: The $2\pi$-periodic extensions of $1$, $|x|$, and $x^2$ are continuous everywhere on $\mathbb{R}$ because $f(-\pi) = f(\pi)$ in each case. Hence the series converge to $\tilde{f}(x)$ at every $x \in \mathbb{R}$ (with no jumps).
- **(ii)**: The periodic extension of $x$ jumps from $+\pi$ to $-\pi$ at $x = (2k+1)\pi$ ($k \in \mathbb{Z}$), where the series converges to $\frac{\pi + (-\pi)}{2} = 0$ (matching $\sin(n(2k+1)\pi) = 0$).
- **(iii)**: The periodic extension of $\pi - x$ jumps from $0$ to $2\pi$ at $x = (2k+1)\pi$, where the series converges to $\frac{0 + 2\pi}{2} = \pi$.
- **(vi)**: The cosine series equals $\cos x$ everywhere (continuous). The sine / $\pi$-periodic series has jumps at $x = m\pi$ ($m \in \mathbb{Z}$) between $-1$ and $+1$, where it converges to $\frac{-1 + 1}{2} = 0$.
- **(vii)**: The $2\pi$-periodic step function jumps between $0$ and $\pi$ at every integer multiple $x = m\pi$ ($m \in \mathbb{Z}$), where the series converges to $\frac{0 + \pi}{2} = \frac{\pi}{2}$.

![[attachments/AM-PS/ch6-e5-step.svg]]
*Periodic extension of the step function in (vii) together with its partial sums $S_1$, $S_5$, and $S_{15}$, showing convergence to the midpoint $\pi/2$ at every jump $x = m\pi$ and the Gibbs overshoot near the jumps.*

- **(viii)**: The odd step function jumps between $-\pi/2$ and $\pi/2$ at every $x = m\pi$ ($m \in \mathbb{Z}$), where the series converges to $\frac{-\pi/2 + \pi/2}{2} = 0$.
- **(ix)**: At the interior jump $x = \pi/2$, all three extensions jump between $1$ and $2$ and converge to $\frac{1 + 2}{2} = \frac{3}{2}$. At $x = 0$ and $x = \pi$: the even extension is continuous (values $1$ and $2$), the odd extension jumps from $-1$ to $1$ at $0$ and from $2$ to $-2$ at $\pi$ (converging to $0$ at both), and the direct $\pi$-periodic extension jumps between $2$ and $1$ at $x = m\pi$ (converging to $3/2$).

## Answers and checks

We run five independent cross-checks against the class notes and classical identities:

1. **Class notes check for (ii) and (vii)**: Setting $L = \pi$ in the $f(x) = x$ example of `Notes09-12-Nov.pdf` (pp. 11–12), $\frac{2L}{\pi}\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}\sin\frac{n\pi x}{L}$ becomes $\sum_{n=1}^{\infty} \frac{2(-1)^{n+1}}{n}\sin(nx)$, matching (ii). Scaling the unit step example on pp. 10–11 by $\pi$ gives $\frac{\pi}{2} + 2\sum_{k=0}^\infty \frac{\sin((2k+1)x)}{2k+1}$, matching (vii).
2. **Linearity check for (iii) and (viii)**: Since $\pi - x = \pi\cdot(1) - x$, subtracting series (ii) from $\pi$ times series (i) gives $\pi - \sum_{n=1}^\infty \frac{2(-1)^{n+1}}{n}\sin(nx) = \pi + \sum_{n=1}^\infty \frac{2(-1)^n}{n}\sin(nx)$, matching (iii). Similarly, $f_{\text{viii}} = f_{\text{vii}} - \frac{\pi}{2}$ cancels $a_0 = \frac{\pi}{2}$ and leaves $b_n$ unchanged, matching (viii).
3. **Evaluation of (iv) at $x = 0$**: Since $|x|$ is continuous at $x = 0$ with $|0| = 0$, setting $x = 0$ in (iv) yields
$$ 0 = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{1}{(2k+1)^2} \implies \sum_{k=0}^{\infty} \frac{1}{(2k+1)^2} = \frac{\pi^2}{8}, $$
which is a known exact sum.
4. **Evaluation of (v) at $x = \pi$ (Basel problem)**: Since the $2\pi$-periodic extension of $x^2$ is continuous at $x = \pi$ with value $\pi^2$ and $\cos(n\pi) = (-1)^n$ gives $(-1)^n\cos(n\pi) = (-1)^{2n} = 1$, setting $x = \pi$ in (v) yields
$$ \pi^2 = \frac{\pi^2}{3} + 4\sum_{n=1}^{\infty} \frac{1}{n^2} \implies \frac{2\pi^2}{3} = 4\sum_{n=1}^{\infty} \frac{1}{n^2} \implies \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}, $$
confirming the exact Basel identity.
5. **Midpoint check on (ix)**: Evaluating the even series at $x = \pi/2$ gives $\frac{3}{2} - 0 = \frac{3}{2}$, and evaluating the direct $\pi$-periodic series at $x = 0$ and $x = \pi/2$ gives $\frac{3}{2} - 0 = \frac{3}{2}$, matching the jump midpoint $\frac{1 + 2}{2} = \frac{3}{2}$.

> [!result] Key results
> - **(i)** $1 \sim 1$.
> - **(ii)** $x \sim \sum_{n=1}^{\infty} \frac{2(-1)^{n+1}}{n}\sin(nx)$ on $[-\pi,\pi]$; converges to $0$ at $x = (2k+1)\pi$.
> - **(iii)** $\pi - x \sim \pi + \sum_{n=1}^{\infty} \frac{2(-1)^n}{n}\sin(nx)$ on $[-\pi,\pi]$; converges to $\pi$ at $x = (2k+1)\pi$.
> - **(iv)** $|x| \sim \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{\cos((2k+1)x)}{(2k+1)^2}$ on $[-\pi,\pi]$; continuous everywhere.
> - **(v)** $x^2 \sim \frac{\pi^2}{3} + 4\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}\cos(nx)$ on $[-\pi,\pi]$; continuous everywhere.
> - **(vi)** On $[0,\pi]$: cosine series $\cos x$; sine series and $\pi$-periodic series $\frac{8}{\pi}\sum_{k=1}^{\infty} \frac{k}{4k^2-1}\sin(2kx)$.
> - **(vii)** Step $0/\pi$: $\frac{\pi}{2} + 2\sum_{k=0}^{\infty} \frac{\sin((2k+1)x)}{2k+1}$; converges to $\frac{\pi}{2}$ at $x = m\pi$.
> - **(viii)** Odd step $-\frac{\pi}{2}/\frac{\pi}{2}$: $2\sum_{k=0}^{\infty} \frac{\sin((2k+1)x)}{2k+1}$; converges to $0$ at $x = m\pi$.
> - **(ix)** Step $1/2$ on $[0,\pi]$: cosine series $\frac{3}{2} - \frac{2}{\pi}\sum_{k=0}^\infty \frac{(-1)^k}{2k+1}\cos((2k+1)x)$; sine series $\frac{2}{\pi}\sum_{n=1}^\infty \frac{1+\cos(n\pi/2)-2(-1)^n}{n}\sin(nx)$; $\pi$-periodic series $\frac{3}{2} - \frac{2}{\pi}\sum_{k=0}^\infty \frac{\sin(2(2k+1)x)}{2k+1}$.
