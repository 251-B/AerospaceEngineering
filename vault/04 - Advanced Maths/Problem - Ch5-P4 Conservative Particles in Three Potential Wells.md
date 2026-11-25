---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 4"
dificultad: media
id: "e4"
pill: "Particles in potential wells"
tags:
  - problema-resuelto
  - advanced-maths
  - nonlinear-systems
  - conservative-systems
  - potential-energy
---

# Problem 5.4: Conservative Particles in Three Potential Wells

> Official exercise 4 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

For the following choices of potential functions $V(x)$, write down the total energy for a particle of unit mass, and assuming that this is conserved write down a coupled system of equations for $x$ and $y = \dot x$. Sketch the phase portrait and interpret the dynamics in each case.

(i) $V(x) = \tfrac{1}{2}\omega^2 x^2$; (ii) $V(x) = \tfrac{1}{2}x^4 - x^2$; (iii) $V(x) = \tfrac{1}{2}x^6 - \tfrac{5}{4}x^4 + 2x^2$ (as printed on the sheet).

## Model Classification and Stationary Points

#### Energy and the first-order system

For unit mass the kinetic energy is $\tfrac12\dot x^2$, so $E=\tfrac12 y^2+V(x)$ with $y=\dot x$. Conservation, with the chain rule $\frac{d}{dt}V(x(t))=V'(x)\dot x$:

$$0=\frac{dE}{dt}=y\dot y+V'(x)\dot x=y\,(\dot y+V'(x)) \;\Longrightarrow\; \ddot x=-V'(x).$$

The coupled system is
$$\dot x=y,\qquad \dot y=-V'(x).$$

#### General classification

Stationary points: $y=0$ and $V'(x)=0$. The Jacobian is
$$J=\begin{pmatrix}0&1\\-V''(x)&0\end{pmatrix},\quad \tau=0,\ \Delta=V''(x).$$
Eigenvalues $\mu^2=-V''$: $V''>0$ gives $\pm i\sqrt{V''}$ (linear centre), $V''<0$ gives $\pm\sqrt{-V''}$ (saddle). Orbits lie on level curves $y^2=2(E-V(x))$, symmetric in $y\to-y$ and travelled clockwise ($\dot x=y>0$ in the upper half plane). A strict local minimum of $V$ is a strict local minimum of $E$ on the phase plane, so its level sets are closed curves: the linear centre is a **true** nonlinear centre (not a spiral).

## Linearisation and Local Eigenvalues

### (i) $V=\tfrac12\omega^2x^2$

$V'=\omega^2x$, $V''=\omega^2$. System $\dot x=y$, $\dot y=-\omega^2x$. Only stationary point $(0,0)$, $J=\begin{pmatrix}0&1\\-\omega^2&0\end{pmatrix}$, $\mu=\pm i\omega$: centre.

### (ii) $V=\tfrac12x^4-x^2$

$V'=2x^3-2x=2x(x-1)(x+1)$, $V''=6x^2-2$. Stationary points $(0,0)$, $(\pm1,0)$.

| Point | $V''$ | Eigenvalues | Type | $V$ |
| :-- | :-- | :-- | :-- | :-- |
| $(0,0)$ | $-2$ | $\pm\sqrt2$ | saddle | $0$ |
| $(\pm1,0)$ | $4$ | $\pm2i$ | centre | $-\tfrac12$ |

### (iii) $V=\tfrac12x^6-\tfrac54x^4+2x^2$ (sheet as printed)

$V'=3x^5-5x^3+4x=x(3x^4-5x^2+4)$. With $u=x^2$, $3u^2-5u+4$ has discriminant $25-48=-23<0$: no real root, and the quadratic is positive. So $x=0$ is the **only** real root of $V'$. Also
$$V''=15x^4-15x^2+4,\qquad \text{discriminant } 225-240=-15<0,$$
so $V''>0$ for all $x$: $V$ is strictly convex. Stationary point: $(0,0)$ with $V''(0)=4$, $\mu=\pm2i$: centre.

## Global Phase Portrait and Interpretation

### (i) Harmonic oscillator

Level curves $y^2+\omega^2x^2=2E$: concentric ellipses with semi-axes $\sqrt{2E}/\omega$ ($x$) and $\sqrt{2E}$ ($y$), travelled clockwise with period $2\pi/\omega$ independent of the amplitude.

![[attachments/AM-PS/ch5-e4-i.svg]]
*Harmonic well: concentric ellipses around the centre, clockwise motion.*

### (ii) Double well

$V\to+\infty$ as $|x|\to\infty$, so there is no escape. Turning points solve $V(x)=E$.

- $-\tfrac12<E<0$: two separate closed orbits, one in each well, around $(\pm1,0)$ (the particle cannot cross the barrier $V(0)=0$).
- $E=0$ (separatrix): $y^2=-x^4+2x^2=x^2(2-x^2)$, i.e. $y=\pm x\sqrt{2-x^2}$, a figure of eight through the saddle, reaching $|x|=\sqrt2$ (roots of $V=0$). Near the origin $y\simeq\pm\sqrt2x$, matching the eigenvectors of $\mu=\pm\sqrt2$.
- $E>0$: one large orbit encircling both wells.
- $E=-\tfrac12$: the particle rests at $x=\pm1$. Small oscillations there have angular frequency $\sqrt{V''}=2$.

![[attachments/AM-PS/ch5-e4-ii.svg]]
*Double well: centres at $(\pm1,0)$, saddle at the origin, the figure-eight separatrix $E=0$ and outer orbits for $E>0$.*

### (iii) Printed potential: single convex well

$V$ is strictly convex with minimum $V(0)=0$ and $V\to\infty$, so for every $E>0$ the level set $y^2=2(E-V)$ is one closed orbit. The dynamics is a nonlinear oscillator with one stable equilibrium; the period varies with $E$ (small amplitude: $2\pi/2=\pi$).

![[attachments/AM-PS/ch5-e4-iii-sheet.svg]]
*Printed potential: a single centre at the origin surrounded by nested closed orbits.*

> [!warning] Possible misprint in the official sheet (vs Robinson Ex. 34.1(iii))
> The sheet prints $V=\tfrac12x^6-\tfrac54x^4+2x^2$, which has a single well. Robinson's exercise (Robinson, Ex. 34.1(iii)) has $V(x)=\tfrac16x^6-\tfrac54x^4+2x^2$, whose derivative factorises nicely. This is the probable intended potential; both are solved here. The coefficient $\tfrac16$ is the one for which $V'=x^5-5x^3+4x=x(x^2-1)(x^2-4)$.

#### Robinson's potential $V=\tfrac16x^6-\tfrac54x^4+2x^2$

$V'=x^5-5x^3+4x=x(x^4-5x^2+4)=x(x^2-1)(x^2-4)$, so the roots are $x=0,\pm1,\pm2$. $V''=5x^4-15x^2+4$.

| $x$ | $V''$ | Type | $V$ |
| :-- | :-- | :-- | :-- |
| $0$ | $4$ | centre ($\mu=\pm2i$) | $0$ |
| $\pm1$ | $5-15+4=-6$ | saddle ($\mu=\pm\sqrt6$) | $\tfrac16-\tfrac54+2=\tfrac{11}{12}$ |
| $\pm2$ | $80-60+4=24$ | centre ($\mu=\pm2\sqrt6\,i$) | $\tfrac{64}{6}-20+8=-\tfrac43$ |

Triple well: wells at $0$ (depth $0$) and $\pm2$ (depth $-\tfrac43$), separated by barriers at $\pm1$ of height $\tfrac{11}{12}$.

- $E<\tfrac{11}{12}$ (and $\ge-\tfrac43$): closed orbits trapped in a single well; for $0<E<\tfrac{11}{12}$ there are three separate families (centre well and the two outer wells), for $-\tfrac43\le E<0$ only the two outer wells.
- $E=\tfrac{11}{12}$: separatrices through the saddles $(\pm1,0)$ joining the wells.
- $E>\tfrac{11}{12}$: orbits encircling all three centres.

![[attachments/AM-PS/ch5-e4-iii-robinson.svg]]
*Robinson's triple well: centres at $(0,0)$, $(\pm2,0)$, saddles at $(\pm1,0)$ and separatrices at $E=11/12$.*

#### Check

$[V]=[\mathrm{L}^2\mathrm{T}^{-2}]$ per unit mass, equal to $[y^2]$; so $\mu^2=-V''$ has units $[\mathrm{T}^{-2}]$, consistent with the coefficient scaling.
