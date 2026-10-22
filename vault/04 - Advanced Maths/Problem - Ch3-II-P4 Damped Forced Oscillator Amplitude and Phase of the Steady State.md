---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 4"
dificultad: media
id: "e4"
pill: "Frequency Response • Amplitude M • Phase φ"
tags:
  - problema-resuelto
  - oscilaciones-forzadas
  - amortiguamiento
  - respuesta-en-frecuencia
---

# Problem 3.II.4: Damped Forced Oscillator: Amplitude and Phase of the Steady State

> Official exercise 4 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

Consider the oscillating system of the previous exercise, but now in the presence of a non-negligible viscous drag so that Newton's second law reads

$$ \ddot x + \lambda\dot x + \omega^2 x = a\cos\alpha t, $$

in the underdamped case in which $\lambda^2 < 4\omega^2$. Show that $x_p(t) = M\cos(\alpha t - \phi)$ is a particular solution, finding its amplitude $M$ and phase $\phi$ in terms of the system parameters. Discuss how the relative ratio between the system response and the external forcing, $M/a$, behaves with the external frequency $\alpha$ and compare with the zero-drag ($\lambda = 0$) case.

## Phase 1: Setup and hypotheses

Parameters: $\lambda > 0$ (damping rate, s$^{-1}$), $\omega > 0$ (natural frequency), $\alpha > 0$ (forcing frequency), $a > 0$ (forcing amplitude per unit mass). Underdamped: $\lambda^2 < 4\omega^2$, so the characteristic roots are $-\frac{\lambda}{2} \pm i\sigma$ with $\sigma = \frac12\sqrt{4\omega^2 - \lambda^2} > 0$ (Topic 3, Sec. 4.3) and the complementary function is $x_h = e^{-\lambda t/2}(c_1\cos\sigma t + c_2\sin\sigma t)$, which decays. Only $x_p$ survives at long times.

## Phase 2: Formulation: what has to be shown

We must find constants $M$ and $\phi$ such that $x_p = M\cos(\alpha t - \phi)$ satisfies $L[x_p] = a\cos\alpha t$. Because $\cos(\alpha t - \phi)$ is a shifted cosine, the cosine and sine terms of the guess of Topic 3, Sec. 6.1 are packed in one amplitude and one phase. The subtraction formulas $\cos(\alpha t - \phi) = \cos\alpha t\cos\phi + \sin\alpha t\sin\phi$ and $\sin(\alpha t - \phi) = \sin\alpha t\cos\phi - \cos\alpha t\sin\phi$ will be used.

> [!info] Class notes and complement [Notes, p. 6]
> The guess of the notes for $a\cos\alpha t$ is $A\cos\alpha t + B\sin\alpha t$ ($\pm i\alpha$ is not a root because $\lambda > 0$), and $x = x_H + x_N$ with $x_H \to 0$ (Case 03 with $\rho = -\lambda/2 < 0$). Packing $A$ and $B$ into one amplitude and one phase, $M\cos(\alpha t - \phi)$, is a complement (not in the class notes).

## Phase 3: Derivation

#### Substitution

Differentiate with the chain rule ($\frac{d}{dt}(\alpha t - \phi) = \alpha$):

$$ \dot x_p = -M\alpha\sin(\alpha t - \phi), \qquad \ddot x_p = -M\alpha^2\cos(\alpha t - \phi) $$

Therefore

$$ L[x_p] = \ddot x_p + \lambda\dot x_p + \omega^2x_p = M\left[(\omega^2 - \alpha^2)\cos(\alpha t - \phi) - \lambda\alpha\sin(\alpha t - \phi)\right] $$

Expand the shifted functions and collect cosines and sines of $\alpha t$:

$$ L[x_p] = M\left[(\omega^2 - \alpha^2)\cos\phi + \lambda\alpha\sin\phi\right]\cos\alpha t + M\left[(\omega^2 - \alpha^2)\sin\phi - \lambda\alpha\cos\phi\right]\sin\alpha t $$

This must equal $a\cos\alpha t + 0\cdot\sin\alpha t$ for every $t$; $\cos\alpha t$ and $\sin\alpha t$ are linearly independent, so both coefficients must match:

$$ \begin{aligned} M\left[(\omega^2 - \alpha^2)\cos\phi + \lambda\alpha\sin\phi\right] &= a \quad (1) \\ M\left[(\omega^2 - \alpha^2)\sin\phi - \lambda\alpha\cos\phi\right] &= 0 \quad (2) \end{aligned} $$

#### Phase

$M \neq 0$, because $M = 0$ would turn equation (1) into $0 = a > 0$. Hence equation (2) gives $(\omega^2 - \alpha^2)\sin\phi = \lambda\alpha\cos\phi$, i.e.

$$ \tan\phi = \frac{\lambda\alpha}{\omega^2 - \alpha^2} $$

To fix the quadrant, introduce $R = \sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2} > 0$ and the angle $\phi$ defined by

$$ \cos\phi = \frac{\omega^2 - \alpha^2}{R}, \qquad \sin\phi = \frac{\lambda\alpha}{R} $$

(these satisfy $\cos^2\phi + \sin^2\phi = \frac{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}{R^2} = 1$ and equation (2): $(\omega^2 - \alpha^2)\frac{\lambda\alpha}{R} - \lambda\alpha\frac{\omega^2 - \alpha^2}{R} = 0$). Because $\sin\phi = \lambda\alpha/R > 0$, $\phi \in (0, \pi)$: $\phi = \operatorname{arccot}\frac{\omega^2 - \alpha^2}{\lambda\alpha}$, i.e. $\phi = \arctan\frac{\lambda\alpha}{\omega^2 - \alpha^2}$ for $\alpha < \omega$ and $\phi = \pi + \arctan\frac{\lambda\alpha}{\omega^2 - \alpha^2}$ for $\alpha > \omega$.

#### Amplitude

Substitute $\cos\phi$ and $\sin\phi$ in equation (1):

$$ M\left[(\omega^2 - \alpha^2)\frac{\omega^2 - \alpha^2}{R} + \lambda\alpha\frac{\lambda\alpha}{R}\right] = M\,\frac{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}{R} = M\,R = a $$

$$ \boxed{M = \frac{a}{\sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}}, \qquad \phi = \operatorname{atan2}\!\left(\lambda\alpha,\ \omega^2 - \alpha^2\right)} $$

so $x_p = M\cos(\alpha t - \phi)$ is indeed a particular solution. It agrees with the sine-cosine form of Topic 3, Eq. 15.5: $M\cos\phi = \frac{a(\omega^2 - \alpha^2)}{R^2}$ and $M\sin\phi = \frac{a\lambda\alpha}{R^2}$ are exactly the coefficients $D$ and $C$ found there.

#### Ratio of response to forcing

$$ \frac{M}{a} = \frac{1}{\sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}} =: F(\alpha) $$

Differentiate the radicand $D(\alpha) = (\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2$ with the chain rule: $D'(\alpha) = -4\alpha(\omega^2 - \alpha^2) + 2\lambda^2\alpha = 2\alpha\left(2\alpha^2 - 2\omega^2 + \lambda^2\right)$. The critical points are $\alpha = 0$ and $\alpha_r^2 = \omega^2 - \frac{\lambda^2}{2}$, which is real only if $\lambda^2 < 2\omega^2$.

- **Case $\lambda^2 < 2\omega^2$ (light damping).** $D$ has a minimum at $\alpha_r = \sqrt{\omega^2 - \lambda^2/2} < \omega$ and $F$ a maximum. There $\omega^2 - \alpha_r^2 = \frac{\lambda^2}{2}$, so $D(\alpha_r) = \frac{\lambda^4}{4} + \lambda^2\left(\omega^2 - \frac{\lambda^2}{2}\right) = \lambda^2\left(\omega^2 - \frac{\lambda^2}{4}\right)$ and $\left(\frac{M}{a}\right)_{\max} = \frac{1}{\lambda\sqrt{\omega^2 - \lambda^2/4}} = \frac{1}{\lambda\sigma}$: finite, large for small $\lambda$, and attained slightly below $\omega$ (pseudo-resonance).
- **Case $2\omega^2 \leq \lambda^2 < 4\omega^2$.** $D'(\alpha) \geq 0$ for $\alpha > 0$: no peak, and $M/a$ decreases monotonically from its value at $\alpha = 0$.
- **Limits.** $\alpha \to 0$: $M/a \to 1/\omega^2$ (static deflection under a constant force); $\alpha = \omega$: $M/a = 1/(\lambda\omega)$; $\alpha \to \infty$: $M/a \approx 1/\alpha^2 \to 0$.
- **Phase.** $\phi$ increases continuously from $0$ at $\alpha = 0$ through $\pi/2$ at $\alpha = \omega$ (there $\cos\phi = 0$) to $\pi$ as $\alpha \to \infty$: the response lags the forcing by a quarter period exactly at the natural frequency.

#### Comparison with the undamped case

For $\lambda = 0$, $M/a = \frac{1}{|\omega^2 - \alpha^2|}$, which tends to $+\infty$ as $\alpha \to \omega$ (resonance, Exercise 3), and $\phi$ jumps discontinuously from $0$ (for $\alpha < \omega$) to $\pi$ (for $\alpha > \omega$): the response is in phase below $\omega$ and in antiphase above. Any $\lambda > 0$ regularises this: the peak becomes finite, $1/(\lambda\sigma)$, and the phase jump is smoothed over a band of width $\sim\lambda$ around $\omega$. As $\lambda \to 0$, $\alpha_r \to \omega$ and the peak height $1/(\lambda\sigma) \to \infty$, recovering resonance.

![[attachments/AM-PS/ch3b-e4-response.svg]]
*Amplitude ratio $\omega^2M/a$ against $\alpha/\omega$ for $\lambda/\omega = 0.2, 0.5, 1, 1.5$ (blue to pink) and the undamped limit (dashed, $\lambda = 0$).*

## Phase 4: Interpretation and checks

> [!result] Result
> $x_p(t) = M\cos(\alpha t - \phi)$ with $M = \dfrac{a}{\sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}}$ and $\phi = \operatorname{atan2}(\lambda\alpha, \omega^2 - \alpha^2) \in (0, \pi)$.
>
> The general solution is $x = e^{-\lambda t/2}(c_1\cos\sigma t + c_2\sin\sigma t) + M\cos(\alpha t - \phi)$: the transient decays and the steady state at the forcing frequency remains, independent of the initial data.

- Numerical check of (1) and (2) at $\omega = 2$, $\lambda = 1$, $\alpha = 1$, $a = 1$: $R = \sqrt{9 + 1} = \sqrt{10}$, $M = 1/\sqrt{10}$, $\cos\phi = 3/\sqrt{10}$, $\sin\phi = 1/\sqrt{10}$, and $M[3\cos\phi + 1\cdot\sin\phi] = \frac{1}{\sqrt{10}}\cdot\frac{9 + 1}{\sqrt{10}} = 1 = a$ (checked symbolically in `scripts/verify_topic3_topic4.py`).
- Dimensions: $[\omega^2 - \alpha^2] = [\lambda\alpha] = \mathrm{s^{-2}}$, so $[R] = \mathrm{s^{-2}}$ and $[M] = [a]/[R] = \mathrm{m/s^2\cdot s^2} = \mathrm m$; $\phi$ is dimensionless.
- Condition $\lambda^2 < 4\omega^2$ is only needed for the form of $x_h$; the formulas for $M$ and $\phi$ hold for every $\lambda > 0$.
