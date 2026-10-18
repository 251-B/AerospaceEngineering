---
materia: Engineering Mechanics
tema: "Unit 2: damped harmonic oscillator, energy decay and forced response"
bank_id: C07
title: "Damped and forced oscillator: energy decay per period and where the amplitude really peaks"
category: conceptual_question
archetype: oscillations
level: conceptual
unit: 2
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2013, 2014 and 2015); not an official exercise. Verified with scripts/mechanics/c07.py"
tags:
  - problem-bank
  - midterm-1
  - damped-oscillator
  - forced-oscillations
  - resonance
---

# Bank C07 — Damped and forced oscillator

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §5.3 (damped harmonic oscillator, Eqs. 5.20 to 5.28) and §5.4 (damped oscillator under a periodic force, Eqs. 5.32 to 5.45). Every number was checked with SymPy.

## Statement

A block of mass $m=2$ kg moves along the $x$ axis of an inertial frame, attached to a spring of stiffness $k=50$ N/m and to a viscous damper of constant $c=4$ N s/m. Its equation of motion is $m\ddot x+c\dot x+kx=F(t)$, and (Notes Eq. 5.23) $\gamma=c/(2m)$, $\omega_0=\sqrt{k/m}$. Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

## (a) Free motion [1.0 pts]

With $F(t)=0$. Statement: "The motion is underdamped, and over each period $T=2\pi/\omega$ of the damped oscillation the mechanical energy $E=\tfrac12m\dot x^2+\tfrac12kx^2$ is multiplied by the factor $e^{-2\pi/\sqrt6}\approx0.0769$, the square of the factor by which the amplitude decays."

### Hint

Compare $\gamma$ with $\omega_0$. Write the general solution and evaluate $x(t+T)$ and $\dot x(t+T)$.

### Checkpoint

- TRUE.
- $\gamma=1$ s$^{-1}$ $<\omega_0=5$ s$^{-1}$: underdamped; $\omega=\sqrt{\omega_0^2-\gamma^2}=2\sqrt6\approx4.899$ s$^{-1}$, $T\approx1.283$ s.
- $x(t+T)=e^{-\gamma T}x(t)$ and $\dot x(t+T)=e^{-\gamma T}\dot x(t)$ exactly, with $\gamma T=\pi/\sqrt6$: amplitude factor $e^{-\pi/\sqrt6}\approx0.277$, energy factor $e^{-2\pi/\sqrt6}\approx0.0769$.

### Solution

#### Step 1. Type of motion

$\gamma=\dfrac{c}{2m}=\dfrac{4}{4}=1$ s$^{-1}$ and $\omega_0=\sqrt{50/2}=5$ s$^{-1}$. The roots of $mp^2+cp+k=0$ are $p=-\gamma\pm\sqrt{\gamma^2-\omega_0^2}=-1\pm2\sqrt6\,i$: complex, so the motion is **underdamped** (Notes §5.3.1), with $\omega=\sqrt{\omega_0^2-\gamma^2}=\sqrt{24}=2\sqrt6$ s$^{-1}$ and $T=2\pi/\omega\approx1.283$ s.

#### Step 2. Exact decay over one period

The general solution is $x=e^{-\gamma t}\big(A\cos\omega t+B\sin\omega t\big)$. Since $\cos$ and $\sin$ have period $T=2\pi/\omega$, $x(t+T)=e^{-\gamma(t+T)}\big(A\cos\omega t+B\sin\omega t\big)=e^{-\gamma T}x(t)$, and differentiating this identity, $\dot x(t+T)=e^{-\gamma T}\dot x(t)$. Both terms of $E$ are quadratic:

$$E(t+T)=e^{-2\gamma T}E(t),\qquad \gamma T=\frac{2\pi}{2\sqrt6}=\frac{\pi}{\sqrt6}$$

#### Step 3. Numbers

Amplitude factor $e^{-\pi/\sqrt6}\approx0.277$; energy factor $e^{-2\pi/\sqrt6}=\big(e^{-\pi/\sqrt6}\big)^2\approx0.0769$. The energy is dissipated by the damper: $\dot E=\dot x\,(m\ddot x+kx)=-c\dot x^2\le0$. The statement is TRUE.

## (b) Forced motion [1.0 pts]

Now $F(t)=F_1\cos\omega_1t$ with $F_1=10$ N. Statement: "In the steady state the amplitude is largest when the forcing frequency equals $\omega_0=5$ s$^{-1}$; there the response lags the force by $90^\circ$ and its amplitude is $0.5$ m."

### Hint

The steady amplitude is $a_1=\dfrac{F_1/m}{\sqrt{(\omega_0^2-\omega_1^2)^2+4\gamma^2\omega_1^2}}$ (Notes Eq. 5.41). Minimise the radicand with respect to $\omega_1^2$, not with respect to $\omega_0$.

### Checkpoint

- FALSE (the phase and the value at $\omega_1=\omega_0$ are right; the location of the maximum is not).
- At $\omega_1=\omega_0$: $a_1=\dfrac{F_1}{2m\gamma\omega_0}=0.5$ m, $\tan\alpha_1\to-\infty$, $\alpha_1=-90^\circ$.
- Maximum over $\omega_1$ at $\omega_1^2=\omega_0^2-2\gamma^2=23$ s$^{-2}$ ($\omega_1\approx4.796$ s$^{-1}$): $a_{1,max}=\dfrac{F_1}{2m\gamma\sqrt{\omega_0^2-\gamma^2}}=\dfrac{5}{2\sqrt{24}}\approx0.510$ m $>0.5$ m, with $\alpha_1\approx-78.2^\circ$.

### Solution

#### Step 1. Steady response at $\omega_1=\omega_0$

After the transient dies out (Notes §5.4), $x=a_1\cos(\omega_1t+\alpha_1)$ with $a_1$ above and $\tan\alpha_1=-\dfrac{2\gamma\omega_1}{\omega_0^2-\omega_1^2}$ (Notes Eq. 5.42). At $\omega_1=\omega_0$ the denominator of $\tan\alpha_1$ vanishes and $\alpha_1=-\pi/2$: a lag of $90^\circ$. The amplitude is

$$a_1(\omega_0)=\frac{F_1/m}{2\gamma\omega_0}=\frac{10/2}{2\cdot1\cdot5}=0.5\ \text{m}$$

#### Step 2. Where the maximum over $\omega_1$ is

Let $s=\omega_1^2$ and $D(s)=(\omega_0^2-s)^2+4\gamma^2s$. $a_1$ is largest where $D$ is smallest:

$$\frac{dD}{ds}=-2(\omega_0^2-s)+4\gamma^2=0\ \Longrightarrow\ s^*=\omega_0^2-2\gamma^2=25-2=23\ \text{s}^{-2}$$

($d^2D/ds^2=2>0$: a minimum). Substituting, $D(s^*)=4\gamma^4+4\gamma^2(\omega_0^2-2\gamma^2)=4\gamma^2(\omega_0^2-\gamma^2)$, so

$$a_{1,max}=\frac{F_1/m}{2\gamma\sqrt{\omega_0^2-\gamma^2}}=\frac{5}{2\sqrt{24}}\approx0.510\ \text{m}>0.5\ \text{m}$$

at $\omega_1=\sqrt{23}\approx4.796$ s$^{-1}$, where $\tan\alpha_1=-\dfrac{2\sqrt{23}}{2}=-\sqrt{23}$, $\alpha_1\approx-78.2^\circ$.

#### Step 3. Verdict

The result "maximum at $\omega_0$" of Notes Eq. 5.45 holds when $\omega_1$ is fixed and $\omega_0$ is varied; when the forcing frequency is varied, the peak is shifted below $\omega_0$ by the damping. The statement is FALSE.

## Interpretation

- **Dimensional check:** $\gamma$, $\omega_0$, $\omega_1$ are s$^{-1}$; $F_1/m$ is m s$^{-2}$ and $(F_1/m)/(\gamma\omega_0)$ is m.
- **Limits:** for $\gamma\to0$ the peak returns to $\omega_0$ and $a_{1,max}\to\infty$; for $\gamma\ge\omega_0/\sqrt2$ there is no peak at all ($s^*\le0$) and $a_1$ decreases from its static value $F_1/k=0.2$ m.
- **Common mistakes in the exam:** (1) using the same decay factor for the amplitude and for the energy; (2) placing the amplitude peak at $\omega_0$ for any damping; (3) confusing the $90^\circ$ phase lag (exactly at $\omega_0$) with the amplitude maximum.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
