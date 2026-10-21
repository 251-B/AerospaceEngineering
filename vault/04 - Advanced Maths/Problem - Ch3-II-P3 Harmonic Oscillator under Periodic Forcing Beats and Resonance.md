---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 3"
dificultad: media
id: "e3"
pill: "Forced Oscillations • Resonance • Beats"
tags:
  - problema-resuelto
  - oscilaciones-forzadas
  - resonancia
  - pulsaciones
---

# Problem 3.II.3: Harmonic Oscillator under Periodic Forcing: Beats and Resonance

> Official exercise 3 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

Suppose that $x(t)$ denotes the distance of some system from its equilibrium position, such that it satisfies the differential equation

$$ \ddot x + \omega^2 x = a\cos\alpha t, $$

where the second term on the left hand side accounts for harmonic oscillations and the right hand side is an external forcing that is periodic in time. Discuss the form of the general solution in terms of the natural frequency of oscillation $\omega$ and the frequency $\alpha$ of the external force.

## Phase 1: Setup and classification

Hypotheses: $\omega > 0$ is the natural angular frequency (rad/s), $\alpha \geq 0$ the forcing frequency and $a$ the forcing amplitude per unit mass (m/s$^2$). The equation is linear, second-order, with constant coefficients and a sinusoidal forcing. Its characteristic polynomial $P(k) = k^2 + \omega^2$ has the imaginary roots $k = \pm i\omega$, so the complementary function is the simple harmonic motion $x_h = c_1\cos\omega t + c_2\sin\omega t$ (Topic 3, Sec. 4.2).

The forcing $a\cos\alpha t$ has exponent $s = \pm i\alpha$. The whole discussion hinges on whether $s$ is a root of $P$, that is, on whether $\alpha = \omega$ (**resonance**) or $\alpha \neq \omega$. Both cases are solved below with the method of undetermined coefficients, then compared.

## Phase 2: Method

General solution $x = x_h + x_p$ (Robinson Sec. 14.1). For $x_p$ use the guess table of Topic 3, Sec. 5: $K_1\cos\alpha t + K_2\sin\alpha t$ when $P(i\alpha) \neq 0$ and $t(K_1\cos\omega t + K_2\sin\omega t)$ when $\alpha = \omega$.

## Phase 3: Derivation

### Case A: $\alpha \neq \omega$ (non-resonant forcing)

The homogeneous equation $\ddot{x} + \omega^{2}x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + \omega^{2} = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (0)^2 - 4(1)(\omega^{2}) = - 4 \omega^{2}$.

Factorising, $P(k) = \left(k - i \omega\right) \left(k + i \omega\right)$, so the roots are

$$ k = - i \omega, \qquad k = i \omega $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $\cos{\omega t}$, $\sin{\omega t}$, so the complementary function is

$$ x_h(t) = c_{1} \cos{\omega t} + c_{2} \sin{\omega t} $$

The forcing $a \cos{\alpha t}$ is a sinusoidal term: it is the real or imaginary part of $e^{(i \alpha)t}$, so we test $s = i \alpha$ in the characteristic polynomial: $P(i \alpha) = - \alpha^{2} + \omega^{2}$.

Since $P(s) \neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} \cos{\alpha t} + K_{2} \sin{\alpha t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} \alpha \sin{\alpha t} + K_{2} \alpha \cos{\alpha t} \\ x_p''(t) &= - K_{1} \alpha^{2} \cos{\alpha t} - K_{2} \alpha^{2} \sin{\alpha t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + \omega^{2}x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = \left(- K_{1} \alpha^{2} + K_{1} \omega^{2}\right)\,\cos \alpha\,t + \left(- K_{2} \alpha^{2} + K_{2} \omega^{2}\right)\,\sin \alpha\,t $$

This must equal the forcing $f(t) = a \cos{\alpha t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} \cos \alpha\,t: &\quad - K_{1} \alpha^{2} + K_{1} \omega^{2} = a \\ \sin \alpha\,t: &\quad - K_{2} \alpha^{2} + K_{2} \omega^{2} = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} - K_{1} \alpha^{2} + K_{1} \omega^{2} &= a \quad (1) \\ - K_{2} \alpha^{2} + K_{2} \omega^{2} &= 0 \quad (2) \end{aligned} $$

$- K_{1} \alpha^{2} + K_{1} \omega^{2} = a$ contains one unknown only, so $K_{1} = - \frac{a}{\alpha^{2} - \omega^{2}}$.

$- K_{2} \alpha^{2} + K_{2} \omega^{2} = 0$ contains one unknown only, so $K_{2} = 0$.

Hence $K_{1} = - \frac{a}{\alpha^{2} - \omega^{2}}$, $K_{2} = 0$.

Therefore

$$ x_p(t) = - \frac{a \cos{\alpha t}}{\alpha^{2} - \omega^{2}} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = - \frac{a \cos{\alpha t}}{\alpha^{2} - \omega^{2}} + c_{1} \cos{\omega t} + c_{2} \sin{\omega t} $$

Remarks on this case. The guess contained a sine term, but matching showed $K_2 = 0$: with no $\dot x$ term in the equation, cosines are only turned into cosines. The general solution is

$$ x(t) = c_1\cos\omega t + c_2\sin\omega t + \frac{a}{\omega^2 - \alpha^2}\cos\alpha t = M\cos(\omega t - \phi) + \frac{a}{\omega^2 - \alpha^2}\cos\alpha t $$

(the last form uses the amplitude-phase rewriting $c_1\cos\omega t + c_2\sin\omega t = M\cos(\omega t - \phi)$ with $M = \sqrt{c_1^2 + c_2^2}$, Topic 3, Eq. 13.3). The solution is a superposition of two sinusoids with different frequencies, so it is **bounded** for every $t$; it is periodic only if $\omega/\alpha$ is rational. The forced amplitude $|a/(\omega^2 - \alpha^2)|$ is large when $\alpha \approx \omega$.

#### Starting from rest: beats

With $x(0) = 0$, $\dot x(0) = 0$: $x(0) = c_1 + \frac{a}{\omega^2 - \alpha^2} = 0$ gives $c_1 = -\frac{a}{\omega^2 - \alpha^2}$, and $\dot x(0) = \omega c_2 = 0$ gives $c_2 = 0$ (the forced term $\propto \cos\alpha t$ has zero slope at $0$). Hence

$$ x(t) = \frac{a}{\omega^2 - \alpha^2}\left(\cos\alpha t - \cos\omega t\right) $$

Use $\cos A - \cos B = -2\sin\frac{A + B}{2}\sin\frac{A - B}{2}$ with $A = \alpha t$, $B = \omega t$, noting that $\sin\frac{\alpha - \omega}{2}t = -\sin\frac{\omega - \alpha}{2}t$:

$$ x(t) = \frac{2a}{\omega^2 - \alpha^2}\,\sin\frac{(\omega + \alpha)t}{2}\;\sin\frac{(\omega - \alpha)t}{2} $$

This is a fast oscillation at the mean frequency $(\omega + \alpha)/2$ whose amplitude is modulated by the slow envelope $\pm\frac{2a}{|\omega^2 - \alpha^2|}\sin\frac{|\omega - \alpha|t}{2}$: **beats**. The envelope vanishes every $2\pi/|\omega - \alpha|$ (the beat period; the signed factor $\sin\frac{(\omega - \alpha)t}{2}$ itself has period $4\pi/|\omega - \alpha|$), long when $\alpha \approx \omega$, and its peak value $\frac{2a}{|\omega^2 - \alpha^2|}$ grows without bound as $\alpha \to \omega$.

### Case B: $\alpha = \omega$ (resonance)

The homogeneous equation $\ddot{x} + \omega^{2}x = 0$ has constant coefficients, so we try $x = e^{kt}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{kt} \neq 0$ leaves the characteristic equation

$$ P(k) = k^{2} + \omega^{2} = 0 $$

Its discriminant is $\Delta = b^2 - 4ac = (0)^2 - 4(1)(\omega^{2}) = - 4 \omega^{2}$.

Factorising, $P(k) = \left(k - i \omega\right) \left(k + i \omega\right)$, so the roots are

$$ k = - i \omega, \qquad k = i \omega $$

A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \dots, m - 1$; a complex pair $\rho \pm i\omega$ gives $t^j e^{\rho t}\cos\omega t$ and $t^j e^{\rho t}\sin\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is $\cos{\omega t}$, $\sin{\omega t}$, so the complementary function is

$$ x_h(t) = c_{1} \cos{\omega t} + c_{2} \sin{\omega t} $$

The forcing $a \cos{\omega t}$ is a sinusoidal term: it is the real or imaginary part of $e^{(i \omega)t}$, so we test $s = i \omega$ in the characteristic polynomial: $P(i \omega) = 0$.

Since $P(s) = 0$ and $s$ is a root of multiplicity $1$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{1}$.

Guess for the particular integral, with undetermined coefficients:

$$ x_p(t) = K_{1} t \cos{\omega t} + K_{2} t \sin{\omega t} $$

Differentiate term by term (product rule on $t^j e^{\sigma t}$, chain rule on $\cos\omega t$ and $\sin\omega t$):

$$ \begin{aligned} x_p'(t) &= - K_{1} \omega t \sin{\omega t} + K_{1} \cos{\omega t} + K_{2} \omega t \cos{\omega t} + K_{2} \sin{\omega t} \\ x_p''(t) &= - K_{1} \omega^{2} t \cos{\omega t} - 2 K_{1} \omega \sin{\omega t} - K_{2} \omega^{2} t \sin{\omega t} + 2 K_{2} \omega \cos{\omega t} \end{aligned} $$

Substitute into $L[x_p] = x_p'' + \omega^{2}x_p$ and collect the terms that multiply the same function:

$$ L[x_p] = 2 K_{2} \omega\,\cos \omega\,t - 2 K_{1} \omega\,\sin \omega\,t $$

This must equal the forcing $f(t) = a \cos{\omega t}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in $f$:

$$ \begin{aligned} \cos \omega\,t: &\quad 2 K_{2} \omega = a \\ \sin \omega\,t: &\quad - 2 K_{1} \omega = 0 \end{aligned} $$

The linear system is

$$ \begin{aligned} 2 K_{2} \omega &= a \quad (1) \\ - 2 K_{1} \omega &= 0 \quad (2) \end{aligned} $$

$2 K_{2} \omega = a$ contains one unknown only, so $K_{2} = \frac{a}{2 \omega}$.

$- 2 K_{1} \omega = 0$ contains one unknown only, so $K_{1} = 0$.

Hence $K_{1} = 0$, $K_{2} = \frac{a}{2 \omega}$.

Therefore

$$ x_p(t) = \frac{a t \sin{\omega t}}{2 \omega} $$

The general solution is the complementary function plus the particular integral:

$$ x(t) = x_h(t) + x_p(t) = \frac{a t \sin{\omega t}}{2 \omega} + c_{1} \cos{\omega t} + c_{2} \sin{\omega t} $$

Remarks on this case. Now $s = i\omega$ is a simple root of $P$, so the guess is multiplied by $t$ and matching gives $K_1 = 0$, $K_2 = \frac{a}{2\omega}$:

$$ x(t) = c_1\cos\omega t + c_2\sin\omega t + \frac{a}{2\omega}\,t\sin\omega t $$

The last term oscillates at the natural frequency with an amplitude $\frac{a}{2\omega}t$ that **grows linearly in time**: the response is unbounded (Robinson Sec. 15.1.2). For zero initial data, $c_1 = c_2 = 0$ (the particular integral and its derivative $\frac{a}{2\omega}(\sin\omega t + \omega t\cos\omega t)$ vanish at $t = 0$), so $x(t) = \frac{a}{2\omega}\,t\sin\omega t$.

### Case C: resonance as the limit of beats

Let $\alpha \to \omega$ in the beat solution of Case A, which is $0/0$ at $\alpha = \omega$. L'Hopital's rule (differentiate numerator and denominator with respect to $\alpha$, at fixed $t$):

$$ \lim_{\alpha\to\omega}\frac{a(\cos\alpha t - \cos\omega t)}{\omega^2 - \alpha^2} = \lim_{\alpha\to\omega}\frac{-at\sin\alpha t}{-2\alpha} = \frac{a\,t\sin\omega t}{2\omega} $$

which is exactly the resonant solution of Case B: the linear growth is the limit of beats whose period and peak both tend to infinity.

![[attachments/AM-PS/ch3b-e3-beats.svg]]
*Response of $\ddot x + x = \cos\alpha t$ from rest ($\omega = 1$): beats for $\alpha = 0.85$ (blue, bounded, envelope dashed) and resonance for $\alpha = 1$ (pink, amplitude $t/2$).*

## Phase 4: Interpretation and checks

| Frequency ratio | Particular integral | Behaviour of the general solution |
| :--- | :--- | :--- |
| $\alpha \neq \omega$ | $\dfrac{a}{\omega^2 - \alpha^2}\cos\alpha t$ | bounded superposition of two sinusoids; beats if the data are those of rest; large amplitude near $\alpha \approx \omega$ |
| $\alpha = \omega$ | $\dfrac{a}{2\omega}t\sin\omega t$ | amplitude grows linearly: resonance |
| $\alpha \to 0$ | $\dfrac{a}{\omega^2}$ | static deflection $a/\omega^2$ under a constant force (Hooke's law) |
| $\alpha \to \infty$ | $\approx -\dfrac{a}{\alpha^2}\cos\alpha t$ | response tends to $0$: inertia dominates |

- There is no damping in this model, so the transient $x_h$ never dies: unlike Exercise 4, the steady state is not isolated from the initial data.
- Dimensions: $[a] = \mathrm{m/s^2}$, $[\omega^2 - \alpha^2] = \mathrm{s^{-2}}$, so $[a/(\omega^2 - \alpha^2)] = \mathrm m$ and for the resonant term $[a\,t/(2\omega)] = (\mathrm{m/s^2})(\mathrm s)/(\mathrm{s^{-1}}) = \mathrm m$ (radians are dimensionless).
- Engineering reading: a structure with natural frequency $\omega$ must not be forced at (or near) $\omega$ for long; real systems have damping, which keeps the amplitude finite (Exercise 4).
