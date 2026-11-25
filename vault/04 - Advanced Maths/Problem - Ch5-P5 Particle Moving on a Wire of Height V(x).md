---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 5"
dificultad: media
id: "e5"
pill: "Particle on a wire y = V(x)"
tags:
  - problema-resuelto
  - advanced-maths
  - nonlinear-systems
  - conservative-systems
  - constrained-motion
---

# Problem 5.5: Particle Moving on a Wire of Height V(x)

> Official exercise 5 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

For the functions $V(x)$ in parts (i) and (ii) of the previous exercise, write down the kinetic energy of a particle of unit mass moving on a wire whose height as a function of $x$ is $V(x)$. Working in physical units for which the acceleration of gravity is $g = 1$, write down the total energy, and hence derive the second order differential equation satisfied by $x$. Write down a coupled system of equations for $x$ and $y = \dot x$, and sketch the phase portrait.

## Model Classification and Stationary Points

#### Kinetic and total energy

The particle sits at $(x,\,V(x))$ and is constrained to the wire, so one degree of freedom, $x$. Velocity: $(\dot x,\ \tfrac{d}{dt}V(x))=(\dot x,\ V'(x)\dot x)$ by the chain rule. For unit mass

$$T=\tfrac12\left(\dot x^2+V'(x)^2\dot x^2\right)=\tfrac12\big(1+[V'(x)]^2\big)\dot x^2 .$$

Potential energy $mgh$ with $m=g=1$ and $h=V(x)$: $E=T+V(x)$.

#### Equation of motion from $dE/dt=0$

Differentiate $T$ with the product and chain rules, $\frac{d}{dt}[V'(x)^2]=2V'V''\dot x$:

$$\frac{dT}{dt}=\tfrac12\cdot2V'V''\dot x\cdot\dot x^2+\big(1+V'^2\big)\dot x\ddot x=V'V''\dot x^3+\big(1+V'^2\big)\dot x\ddot x,\qquad \frac{dV}{dt}=V'\dot x.$$

Add and set to zero:

$$0=\dot x\Big[\big(1+V'^2\big)\ddot x+V'V''\dot x^2+V'\Big].$$

Dividing by $\dot x\ne0$ (the bracket must vanish, also by continuity when $\dot x=0$):

$$\boxed{\ddot x=-\frac{V'(x)\big(1+V''(x)\dot x^2\big)}{1+[V'(x)]^2}.}$$

Coupled system, $y=\dot x$:

$$\dot x=y,\qquad \dot y=-\frac{V'(x)\,\big(1+V''(x)\,y^2\big)}{1+[V'(x)]^2}.$$

#### Stationary points

$y=0$ and $V'(x)\big(1+V''\cdot0\big)=V'(x)=0$ (the denominator is $\ge1$). The stationary points are exactly those of Exercise 4, as expected: the wire is in equilibrium where it is horizontal.

## Linearisation and Local Eigenvalues

Write $\dot y=F(x,y)=-V'N/D$ with $N=1+V''y^2$, $D=1+V'^2$. At a point with $V'=0$, $y=0$ (so $N=D=1$):

$$\frac{\partial F}{\partial x}=-V''\frac ND-V'\frac{\partial}{\partial x}\!\Big(\frac ND\Big)=-V'',\qquad \frac{\partial F}{\partial y}=-V'\frac{2V''y}{D}=0.$$

Hence
$$J=\begin{pmatrix}0&1\\-V''(x_0)&0\end{pmatrix},$$
identical to Exercise 4: eigenvalues $\pm i\sqrt{V''}$ (centre) when $V''>0$, $\pm\sqrt{-V''}$ (saddle) when $V''<0$. Because $E$ has a strict minimum at the centres, they remain true nonlinear centres.

### (i) $V=\tfrac12\omega^2x^2$

$V'=\omega^2x$, $V''=\omega^2$, so
$$\ddot x=-\frac{\omega^2x\,(1+\omega^2\dot x^2)}{1+\omega^4x^2}.$$
Stationary point $(0,0)$ with $\mu=\pm i\omega$: centre.

### (ii) $V=\tfrac12x^4-x^2$

$V'=2x^3-2x$, $V''=6x^2-2$, so
$$\ddot x=-\frac{(2x^3-2x)\,(1+(6x^2-2)\dot x^2)}{1+(2x^3-2x)^2}.$$

| Point | $V''$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $-2$ | $\pm\sqrt2$ | saddle |
| $(\pm1,0)$ | $4$ | $\pm2i$ | centre |

## Global Phase Portrait and Interpretation

Level curves of the conserved energy: $E=\tfrac12(1+V'^2)y^2+V(x)$, so

$$y^2=\frac{2\,(E-V(x))}{1+[V'(x)]^2}.$$

Compared with Exercise 4, the allowed region $V(x)\le E$ (the turning points) is **the same**, the stationary points and their types are the same, and the separatrix energies are the same. The only change is the shape: the numerator is divided by $1+V'^2\ge1$, so orbits are squeezed in $y$, most where the wire is steep (the particle must also move vertically, so for a given energy its horizontal speed is smaller). The phase portrait is therefore **qualitatively equivalent** to that of Exercise 4 (topologically conjugate by the rescaling $y\mapsto y\sqrt{1+V'^2}$).

### (i) Harmonic wire (parabola)

Orbits $y^2=\dfrac{2E-\omega^2x^2}{1+\omega^4x^2}$: closed non-elliptical curves (pinched at large $|x|$), clockwise, around the centre; the small-oscillation frequency is $\omega$, as for Exercise 4(i), but the period now depends on amplitude.

![[attachments/AM-PS/ch5-e5-i.svg]]
*Particle on the parabola $V=\tfrac12\omega^2x^2$: closed orbits around the centre, flatter in $y$ than the ellipses of Exercise 4(i).*

### (ii) Double-well wire

Separatrix $E=0$: $y^2=\dfrac{x^2(2-x^2)}{1+4x^2(x^2-1)^2}$ (using $2(0-V)=x^2(2-x^2)$), a figure of eight through the saddle at the origin reaching $|x|=\sqrt2$; separate orbits in each well for $-\tfrac12<E<0$, and orbits around both wells for $E>0$.

![[attachments/AM-PS/ch5-e5-ii.svg]]
*Particle on the double-well wire: same stationary points and separatrix topology as Exercise 4(ii), with the loops squeezed where the wire is steep.*

> [!result] Conclusion
> A wire of height $V(x)$ at $g=1$ keeps the equilibria, their stability and the topology of the phase portrait of the potential problem $\ddot x=-V'(x)$, but changes the equation of motion (inertia $1+V'^2$ and a centrifugal-like term $V''\dot x^2$) and the quantitative shape of the orbits.

#### Check

Small slope limit $V'\to0$: $\ddot x\to-V'(x)$, recovering Exercise 4. Dimensions with $g=1$: $[V]=[x]=\mathrm L$, $V'$ dimensionless, $\ddot x$ and $g V'$ both in $[\mathrm L\,\mathrm T^{-2}]$.
