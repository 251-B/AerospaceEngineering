---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 3"
dificultad: media
id: "e3"
pill: "Two cooperative species"
tags:
  - problema-resuelto
  - advanced-maths
  - nonlinear-systems
  - population-models
  - mutualism
---

# Problem 5.3: Two Cooperative Species Models

> Official exercise 3 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

The situation in which two species cooperate, so that the presence of one enhances the environment for the other, can be modelled by a coupled pair of equations of the form $\dot x = x(A - ax + by)$, $\dot y = y(B + cx - dy)$, where all the parameters are positive. Sketch the phase portraits for the following cooperative equations: (i) $\dot x = x(1 - x + y)$, $\dot y = y(1 + x - 2y)$; (ii) $\dot x = x(2 - x + y)$, $\dot y = y(4 + 2x - y)$.

## Model Classification and Stationary Points

#### General model

Write $\dot x = x(A-ax+by)$, $\dot y = y(B+cx-dy)$ with $A,B,a,b,c,d>0$. Each species grows alone ($A,B>0$), limits itself ($a,d>0$) and is **helped** by the other ($b,c>0$: $\partial\dot x/\partial y = bx>0$, $\partial\dot y/\partial x = cy>0$): mutualism. Only $x,y\ge 0$ is meaningful; both axes are invariant ($x=0\Rightarrow\dot x=0$, $y=0\Rightarrow\dot y=0$).

#### Stationary points

Four cases: $(0,0)$; $x$-axis point $(A/a,0)$; $y$-axis point $(0,B/d)$; interior point from the nullclines
$$ax - by = A,\qquad -cx + dy = B .$$
Cramer's rule gives $x^\ast = \dfrac{Ad+bB}{ad-bc}$, $y^\ast = \dfrac{aB+cA}{ad-bc}$, with denominator $ad-bc$. For positive parameters the numerators are positive, so the interior point lies in the first quadrant **iff** $ad-bc>0$ (self-limitation stronger than mutual help).

#### Jacobian in general

$$J = \begin{pmatrix} A-2ax+by & bx\\ cy & B+cx-2dy\end{pmatrix}.$$

## Linearisation and Local Eigenvalues

### (i) $\dot x = x(1-x+y)$, $\dot y = y(1+x-2y)$

Here $A=a=b=B=c=1$, $d=2$, so $ad-bc = 2-1 = 1>0$.

#### Stationary points

$(0,0)$; $y=0\Rightarrow 1-x=0$: $(1,0)$; $x=0\Rightarrow 1-2y=0$: $(0,\tfrac12)$; interior: $x=1+y$ in $1+x-2y=0$ gives $2+y-2y=0$, $y=2$, $x=3$: $(3,2)$ (Cramer: $x^\ast=(2+1)/1=3$, $y^\ast=(1+1)/1=2$).

#### Jacobian

$$J=\begin{pmatrix}1-2x+y & x\\ y & 1+x-4y\end{pmatrix}.$$

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(1,1)$ | $1,1$ | unstable node |
| $(1,0)$ | $\begin{pmatrix}-1&1\\0&2\end{pmatrix}$ | $-1,\;2$ | saddle |
| $(0,\tfrac12)$ | $\begin{pmatrix}\tfrac32&0\\\tfrac12&-1\end{pmatrix}$ | $\tfrac32,\;-1$ | saddle |
| $(3,2)$ | $\begin{pmatrix}-3&3\\2&-4\end{pmatrix}$ | $-1,\;-6$ | stable node |

At $(3,2)$: $\tau=-7$, $\Delta=12-6=6$, $\tau^2-4\Delta=49-24=25>0$, $\mu=(-7\pm5)/2=-1,-6$. Eigenvector for $\mu=-1$: $(J+I)v=0\Rightarrow -2v_1+3v_2=0$, $v=(3,2)$ (slow direction, along the ray to the origin); for $\mu=-6$: $3v_1+3v_2=0$, $v=(1,-1)$ (fast).

### (ii) $\dot x = x(2-x+y)$, $\dot y = y(4+2x-y)$

Here $A=2,a=1,b=1,B=4,c=2,d=1$, so $ad-bc=1-2=-1<0$.

#### Stationary points

$(0,0)$; $(2,0)$; $(0,4)$. Interior: $\dot x=0$ on $y=x-2$, $\dot y=0$ on $y=2x+4$. Equating: $x-2=2x+4\Rightarrow x=-6$, $y=-8$ (Cramer: $x^\ast=(2+4)/(-1)=-6$): outside the quadrant. **No interior stationary point.**

#### Jacobian

$$J=\begin{pmatrix}2-2x+y & x\\ 2y & 4+2x-2y\end{pmatrix}.$$

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(2,4)$ | $2,\;4$ | unstable node |
| $(2,0)$ | $\begin{pmatrix}-2&2\\0&8\end{pmatrix}$ | $-2,\;8$ | saddle |
| $(0,4)$ | $\begin{pmatrix}6&0\\8&-4\end{pmatrix}$ | $6,\;-4$ | saddle |

## Global Phase Portrait and Interpretation

### (i) Bounded mutualism

Signs: $\dot x>0\iff y>x-1$, $\dot y>0\iff y<(1+x)/2$. The two nullclines cross at $(3,2)$. The axes carry the saddle separatrices ($x$-axis: stable direction at $(1,0)$ along the axis; $y$-axis: stable direction at $(0,\tfrac12)$). Every orbit with $x_0,y_0>0$ is bounded (above the nullcline $y=(1+x)/2$ the second species decreases, to the right of $y=x-1$ the first decreases) and tends to the stable node $(3,2)$, arriving tangent to the slow direction $(3,2)$. The unstable node $(0,0)$ expels everything.

> [!result] Interpretation (i)
> Cooperation is weak enough ($bc<ad$) that each species is still limited by itself: both coexist at $x=3$, $y=2$, larger than their isolated carrying capacities $x=1$ and $y=\tfrac12$ ($A/a=1$, $B/d=\tfrac12$). Mutualism raises both equilibrium populations.

![[attachments/AM-PS/ch5-e3-i.svg]]
*Cooperative model (i): unstable node at the origin, saddles at $(1,0)$ and $(0,\tfrac12)$, globally attracting stable node at $(3,2)$.*

### (ii) Unbounded mutualism

Signs: $\dot x>0\iff y>x-2$, $\dot y>0\iff y<2x+4$. Let $D=\{x-2<y<2x+4,\ x,y>0\}$, where $\dot x>0$ and $\dot y>0$.

#### $D$ is forward invariant

- On $y=x-2$: $\dot x=0$ and $\dot y=y(4+2x-(x-2))=y(x+6)>0$, so the field points straight up, into $D$ (which lies above the line).
- On $y=2x+4$: $\dot y=0$ and $\dot x=x(2-x+2x+4)=x(x+6)>0$, so the field points to the right, into $D$ (which lies below that line, and the line rises with $x$).

#### Every orbit enters $D$

- Above $y=2x+4$: $\dot x>0$, $\dot y<0$; $x$ increases and $y$ decreases. Since $2x(t)+4 < y(t) \le y_0$, we also have $x(t) < (y_0 - 4)/2$ (bounded above) and $y(t) > 4$ (bounded below). If the orbit never left, it would converge (monotone and bounded) to a stationary point with $x\ge x_0>0$, $y\ge4$: none exists. So it crosses $y=2x+4$ into $D$.
- Below $y=x-2$ (so $x>2$): $\dot x<0$, $\dot y>0$; the limit would be a stationary point with $y\ge y_0>0$, $x\ge2$: none. So it crosses $y=x-2$ into $D$.

#### Unbounded growth

Inside $D$, $x$ and $y$ are strictly increasing. If they stayed bounded, the orbit would converge to a stationary point with $x\ge x_0>0$, $y\ge y_0>0$; the only stationary points are $(0,0)$, $(2,0)$, $(0,4)$, none of which satisfies this. Hence **$x\to\infty$ and $y\to\infty$**.

#### Asymptotic direction (remark)

$\dfrac{d}{dt}\ln\dfrac yx=\dfrac{\dot y}{y}-\dfrac{\dot x}{x}=(4+2x-y)-(2-x+y)=2+3x-2y$, which vanishes asymptotically on $y\simeq\tfrac32x$. Along that ray $\dot x\simeq x^2/2$, i.e. growth faster than exponential (a finite-time blow-up of the model).

> [!result] Interpretation (ii)
> Mutual help is so strong ($bc>ad$) that it outweighs self-limitation: both populations explode. The model has no saturation, so it is valid only for moderate populations.

![[attachments/AM-PS/ch5-e3-ii.svg]]
*Cooperative model (ii): saddles at $(2,0)$ and $(0,4)$, unstable node at the origin, nullclines $y=x-2$ and $y=2x+4$ not meeting in the quadrant; all orbits escape to infinity along $y\simeq\tfrac32x$.*
