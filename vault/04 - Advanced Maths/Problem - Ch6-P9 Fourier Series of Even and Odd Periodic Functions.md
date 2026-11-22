---
materia: "Advanced Maths"
tema: "Tema 6: Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 9"
dificultad: media
id: "e9"
pill: "Even Cosine Series • Odd Sine Series • Parity Proof"
tags:
  - problema-resuelto
  - sturm-liouville
  - series-de-fourier
---

# Problem 6.9: Fourier Series of Even and Odd Periodic Functions

> Official exercise 9 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Theory and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

What can we say about the Fourier series on $[-L, L]$ of a function $f(x)$ that is $2L$ periodic and even, that is, satisfies $f(-x) = f(x)$ for $x \in \mathbb{R}$? And if $f(x)$ is $2L$ periodic and odd, $f(-x) = -f(x)$?

## Classification of the problem

This is a structural symmetry theorem for Fourier series on a symmetric interval $[-L, L]$ (Haberman Sec. 3.3; `Notes09-12-Nov.pdf`, p. 11). It shows how parity of $f$ eliminates half of the Euler-Fourier coefficients and halves the integration interval for the remaining ones.

## Method

Start from the full Fourier series of a $2L$-periodic piecewise smooth function on $[-L, L]$ (`Notes09-12-Nov.pdf`, p. 10):

$$ f(x) \sim a_0 + \sum_{n=1}^{\infty}\left[a_n\cos\left(\frac{n\pi x}{L}\right) + b_n\sin\left(\frac{n\pi x}{L}\right)\right], $$

with

$$ a_0 = \frac{1}{2L}\int_{-L}^{L} f(x)\,dx, \qquad a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\left(\frac{n\pi x}{L}\right)dx, \qquad b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\left(\frac{n\pi x}{L}\right)dx. $$

We first prove two elementary integration lemmas on the symmetric interval $[-L, L]$ using the change of variable $u = -x$, and then apply them to the products $f(x)\cos\left(\frac{n\pi x}{L}\right)$ and $f(x)\sin\left(\frac{n\pi x}{L}\right)$, noting that $\cos\left(\frac{n\pi x}{L}\right)$ is even and $\sin\left(\frac{n\pi x}{L}\right)$ is odd.

## Step-by-step derivation

### 1. Parity lemmas for integrals on $[-L, L]$

Let $g(x)$ be any integrable function on $[-L, L]$. We split the integral at $x = 0$:

$$ \int_{-L}^{L} g(x)\,dx = \int_{-L}^{0} g(x)\,dx + \int_{0}^{L} g(x)\,dx. $$

In the first integral $\int_{-L}^{0} g(x)\,dx$, we introduce the substitution $u = -x$. Then $x = -u$, the differential is $du = -dx$ (so $dx = -du$), and the limits transform as:
- when $x = -L$, $u = -(-L) = L$;
- when $x = 0$, $u = 0$.

Substituting into the first integral and reversing the limits (which absorbs the minus sign from $-du$) gives

$$ \int_{-L}^{0} g(x)\,dx = \int_{L}^{0} g(-u)\,(-du) = \int_{0}^{L} g(-u)\,du = \int_{0}^{L} g(-x)\,dx, $$

where in the last step we renamed the dummy integration variable $u$ back to $x$. Combining with the second integral yields the general identity

$$ \int_{-L}^{L} g(x)\,dx = \int_{0}^{L} \big[g(-x) + g(x)\big]\,dx. $$

From this identity, both parity rules follow immediately:

- **If $g$ is odd** ($g(-x) = -g(x)$): then $g(-x) + g(x) = 0$, so
$$ \int_{-L}^{L} g(x)\,dx = \int_{0}^{L} 0\,dx = 0. $$
- **If $g$ is even** ($g(-x) = g(x)$): then $g(-x) + g(x) = 2g(x)$, so
$$ \int_{-L}^{L} g(x)\,dx = 2\int_{0}^{L} g(x)\,dx. $$

### 2. Case 1: $f(x)$ is $2L$-periodic and even ($f(-x) = f(x)$)

We check the parity of each integrand in the Euler-Fourier formulas:

1. **$f(x)$**: even by hypothesis. Applying the even-function lemma to $a_0$ gives
$$ a_0 = \frac{1}{2L}\int_{-L}^{L} f(x)\,dx = \frac{1}{2L}\cdot 2\int_{0}^{L} f(x)\,dx = \frac{1}{L}\int_{0}^{L} f(x)\,dx. $$
2. **$f(x)\cos\left(\frac{n\pi x}{L}\right)$**: since $\cos(-z) = \cos z$,
$$ f(-x)\cos\left(\frac{n\pi(-x)}{L}\right) = f(x)\cos\left(\frac{n\pi x}{L}\right), $$
so the integrand is **even** (even $\times$ even $=$ even). Applying the even-function lemma to $a_n$ ($n \ge 1$) gives
$$ a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\left(\frac{n\pi x}{L}\right)dx = \frac{2}{L}\int_{0}^{L} f(x)\cos\left(\frac{n\pi x}{L}\right)dx. $$
3. **$f(x)\sin\left(\frac{n\pi x}{L}\right)$**: since $\sin(-z) = -\sin z$,
$$ f(-x)\sin\left(\frac{n\pi(-x)}{L}\right) = f(x)\left(-\sin\left(\frac{n\pi x}{L}\right)\right) = -f(x)\sin\left(\frac{n\pi x}{L}\right), $$
so the integrand is **odd** (even $\times$ odd $=$ odd). Applying the odd-function lemma to $b_n$ ($n \ge 1$) gives
$$ b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\left(\frac{n\pi x}{L}\right)dx = 0. $$

Therefore, the Fourier series of an even $2L$-periodic function reduces to a **pure Fourier cosine series**:

$$ f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\left(\frac{n\pi x}{L}\right), \qquad a_0 = \frac{1}{L}\int_{0}^{L} f(x)\,dx, \quad a_n = \frac{2}{L}\int_{0}^{L} f(x)\cos\left(\frac{n\pi x}{L}\right)dx. $$

### 3. Case 2: $f(x)$ is $2L$-periodic and odd ($f(-x) = -f(x)$)

We again check the parity of each integrand in the Euler-Fourier formulas:

1. **$f(x)$**: odd by hypothesis. Applying the odd-function lemma to $a_0$ gives
$$ a_0 = \frac{1}{2L}\int_{-L}^{L} f(x)\,dx = 0. $$
2. **$f(x)\cos\left(\frac{n\pi x}{L}\right)$**: since $\cos(-z) = \cos z$,
$$ f(-x)\cos\left(\frac{n\pi(-x)}{L}\right) = \big(-f(x)\big)\cos\left(\frac{n\pi x}{L}\right) = -f(x)\cos\left(\frac{n\pi x}{L}\right), $$
so the integrand is **odd** (odd $\times$ even $=$ odd). Applying the odd-function lemma to $a_n$ ($n \ge 1$) gives
$$ a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\left(\frac{n\pi x}{L}\right)dx = 0. $$
3. **$f(x)\sin\left(\frac{n\pi x}{L}\right)$**: since $\sin(-z) = -\sin z$,
$$ f(-x)\sin\left(\frac{n\pi(-x)}{L}\right) = \big(-f(x)\big)\left(-\sin\left(\frac{n\pi x}{L}\right)\right) = +f(x)\sin\left(\frac{n\pi x}{L}\right), $$
so the integrand is **even** (odd $\times$ odd $=$ even). Applying the even-function lemma to $b_n$ ($n \ge 1$) gives
$$ b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\left(\frac{n\pi x}{L}\right)dx = \frac{2}{L}\int_{0}^{L} f(x)\sin\left(\frac{n\pi x}{L}\right)dx. $$

Therefore, the Fourier series of an odd $2L$-periodic function reduces to a **pure Fourier sine series**:

$$ f(x) \sim \sum_{n=1}^{\infty} b_n\sin\left(\frac{n\pi x}{L}\right), \qquad b_n = \frac{2}{L}\int_{0}^{L} f(x)\sin\left(\frac{n\pi x}{L}\right)dx. $$

## Answers and checks

1. **Cross-check with Exercise 6.5 (`Notes09-12-Nov.pdf`, p. 11)**:
   - Even functions in [[Problem - Ch6-P5 Nine Fourier Series Expansions]]: (iv) $f(x) = |x|$ and (v) $f(x) = x^2$ both gave $b_n = 0$ and pure cosine series.
   - Odd functions in [[Problem - Ch6-P5 Nine Fourier Series Expansions]]: (ii) $f(x) = x$ and (viii) the $-\frac{\pi}{2}/\frac{\pi}{2}$ step both gave $a_0 = a_n = 0$ and pure sine series.
2. **Converse check**: Conversely, every convergent cosine series $a_0 + \sum a_n\cos\left(\frac{n\pi x}{L}\right)$ is automatically $2L$-periodic and even, and every convergent sine series $\sum b_n\sin\left(\frac{n\pi x}{L}\right)$ is automatically $2L$-periodic and odd (and vanishes at $x = 0$ and $x = \pm L$, consistent with the jump midpoint $\frac{f(0^+) + f(0^-)}{2} = \frac{f(0^+) - f(0^+)}{2} = 0$ of any odd function).
3. **Half-range implication**: This theorem also justifies half-range expansions on $[0, L]$ (Haberman Sec. 3.3): extending any function defined on $[0, L]$ evenly to $[-L, L]$ produces its Fourier cosine series, while extending it oddly produces its Fourier sine series.

> [!result] Key results
> - **If $f$ is $2L$-periodic and even ($f(-x) = f(x)$)**: all sine coefficients vanish ($b_n = 0$), and the Fourier series is a **pure cosine series**:
>   $$f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\left(\frac{n\pi x}{L}\right), \qquad a_0 = \frac{1}{L}\int_{0}^{L} f(x)\,dx, \quad a_n = \frac{2}{L}\int_{0}^{L} f(x)\cos\left(\frac{n\pi x}{L}\right)dx.$$
> - **If $f$ is $2L$-periodic and odd ($f(-x) = -f(x)$)**: all constant and cosine coefficients vanish ($a_0 = 0$, $a_n = 0$), and the Fourier series is a **pure sine series**:
>   $$f(x) \sim \sum_{n=1}^{\infty} b_n\sin\left(\frac{n\pi x}{L}\right), \qquad b_n = \frac{2}{L}\int_{0}^{L} f(x)\sin\left(\frac{n\pi x}{L}\right)dx.$$
