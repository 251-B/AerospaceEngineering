---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 2"
dificultad: media
id: "e2"
pill: "Seven two-species models"
tags:
  - problema-resuelto
  - advanced-maths
  - nonlinear-systems
  - population-models
  - competition
  - predator-prey
---

# Problem 5.2: Seven Two-Species Population Models

> Official exercise 2 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

For each of the following models of two population species, describe first the type of situation being modelled, then find the stationary points, determine their stability type and sketch the phase portrait for $x, y \ge 0$. Decide what the phase portrait means for the evolution of the two species.

(i) $\dot x = x(2 - x - y),\ \dot y = y(2 - 2y - 2x)$
(ii) $\dot x = x(2 - x - y),\ \dot y = y(2 - 2y - x/4)$
(iii) $\dot x = x(2 - x - 3y),\ \dot y = y(2 - 2y - 3x)$
(iv) $\dot x = x(1 - 2y),\ \dot y = y(-2 + 3x)$
(v) $\dot x = x(4 - x/2 - 3y),\ \dot y = y(-2 + x)$
(vi) $\dot x = x(10 - x - 3y),\ \dot y = y(1 + x - 10y)$
(vii) $\dot x = x(3 - x - y),\ \dot y = y(-2 + x)$

> [!info] Related worked material
> Models (i) and (ii) are also worked in `Solved_exer_nonlinear_system.pdf` and in `Notes03-05-Nov_v2.pdf` (competition models and their classification by trace and determinant). The computations below are repeated in full here.

## Model Classification and Stationary Points

#### General method

Each system has the form $\dot x=x\,P(x,y)$, $\dot y=y\,Q(x,y)$ with $P,Q$ affine. Both axes are invariant ($x=0\Rightarrow\dot x=0$), so orbits starting in $x,y>0$ never leave the open quadrant. Stationary points come in four types: $(0,0)$; $P=0$ on $y=0$; $Q=0$ on $x=0$; and $P=Q=0$ in the interior. The Jacobian is
$$J=\begin{pmatrix}P+xP_x & xP_y\\ yQ_x & Q+yQ_y\end{pmatrix}.$$
At a stationary point on an axis one of $P,Q$ may be non-zero and $J$ is triangular, at the interior point $P=Q=0$ and $J=\begin{pmatrix}xP_x&xP_y\\yQ_x&yQ_y\end{pmatrix}$. Classification by $\tau=\operatorname{tr}J$, $\Delta=\det J$ and $\tau^2-4\Delta$ (`Notes03-05-Nov_v2.pdf`).

### (i) Competition without coexistence

$x$ and $y$ each have a positive growth rate and each is reduced by itself and by the other (negative cross terms): **competition**. Nullclines $\dot x=0$: $x+y=2$; $\dot y=0$: $x+y=1$ (parallel). Stationary points: $(0,0)$, $y=0\Rightarrow(2,0)$, $x=0\Rightarrow 2-2y=0\Rightarrow(0,1)$; interior: $x+y=2$ and $x+y=1$ are incompatible, **none**.

### (ii) Competition with coexistence

Same signs of coefficients. Nullclines: $x+y=2$ and $2y+x/4=2$. Stationary points $(0,0)$, $(2,0)$, $(0,1)$; interior: $x=2-y$ in $2y+\tfrac14(2-y)=2$ gives $8y+2-y=8$, $y=\tfrac67$, $x=\tfrac87$: $(\tfrac87,\tfrac67)$.

### (iii) Strong competition

Nullclines: $x+3y=2$ and $3x+2y=2$. Stationary points $(0,0)$, $(2,0)$, $(0,1)$; interior: $x=2-3y$ in $3x+2y=2$ gives $6-9y+2y=2$, $y=\tfrac47$, $x=2-\tfrac{12}7=\tfrac27$: $(\tfrac27,\tfrac47)$.

> [!info] Check of the interior point
> Verification: $x+3y=\tfrac27+\tfrac{12}7=2$ and $3x+2y=\tfrac67+\tfrac87=2$. The interior point is $(\tfrac27,\tfrac47)$ (the coordinates $(\tfrac47,\tfrac27)$ fail the second equation: $\tfrac{12}7+\tfrac47\ne2$).

### (iv) Predator-prey without limits (Lotka-Volterra)

$x$ is the prey ($\dot x=x(1-2y)$: grows alone at rate 1, killed by $y$), $y$ the predator ($\dot y=y(-2+3x)$: dies alone at rate 2, fed by $x$). No self-limitation. Nullclines $y=\tfrac12$ and $x=\tfrac23$. Stationary points: $(0,0)$ and $(\tfrac23,\tfrac12)$ (on the axes $\dot x=0$, $y=0$ gives only the origin).

### (v) Predator-prey, logistic prey

$\dot x=x(4-\tfrac x2-3y)$: prey with carrying capacity $8$ ($4-\tfrac x2=0$), eaten by $y$; $\dot y=y(-2+x)$: predator, no alternative food, needs $x>2$ to grow. Stationary points: $(0,0)$, $(8,0)$; $x=0\Rightarrow\dot y=-2y=0$ gives no new point; interior: $x=2$, $4-1-3y=0$, $y=1$: $(2,1)$.

### (vi) Predator-prey, predator with alternative food

$\dot y=y(1+x-10y)$: the predator grows at rate 1 even without prey and is self-limited (carrying capacity $\tfrac1{10}$ on the axis), increased by $x$. Stationary points: $(0,0)$; $(10,0)$ ($10-x=0$); $(0,\tfrac1{10})$ ($1-10y=0$); interior: $x=10-3y$ in $1+x-10y=0$: $11-13y=0$, $y=\tfrac{11}{13}$, $x=10-\tfrac{33}{13}=\tfrac{97}{13}$: $(\tfrac{97}{13},\tfrac{11}{13})$.

### (vii) Predator-prey, logistic prey (carrying capacity 3)

$\dot x=x(3-x-y)$, $\dot y=y(-2+x)$. Stationary points: $(0,0)$, $(3,0)$, interior $x=2$, $3-2-y=0$, $y=1$: $(2,1)$.

## Linearisation and Local Eigenvalues

### (i)

$J=\begin{pmatrix}2-2x-y&-x\\-2y&2-4y-2x\end{pmatrix}$.

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(2,2)$ | $2,2$ | unstable node |
| $(2,0)$ | $\begin{pmatrix}-2&-2\\0&-2\end{pmatrix}$ | $-2,-2$ ($\tau^2-4\Delta=0$, not diagonal) | stable improper (degenerate) node |
| $(0,1)$ | $\begin{pmatrix}1&0\\-2&-2\end{pmatrix}$ | $1,-2$ | saddle |

At $(2,0)$ the eigenvector of $\mu=-2$ solves $-2v_2=0$: $v=(1,0)$, the $x$-axis.

### (ii)

$J=\begin{pmatrix}2-2x-y&-x\\-y/4&2-4y-x/4\end{pmatrix}$.

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(2,2)$ | $2,2$ | unstable node |
| $(2,0)$ | $\begin{pmatrix}-2&-2\\0&\tfrac32\end{pmatrix}$ | $-2,\tfrac32$ | saddle |
| $(0,1)$ | $\begin{pmatrix}1&0\\-\tfrac14&-2\end{pmatrix}$ | $1,-2$ | saddle |
| $(\tfrac87,\tfrac67)$ | $\begin{pmatrix}-\tfrac87&-\tfrac87\\-\tfrac3{14}&-\tfrac{12}7\end{pmatrix}$ | $-\tfrac67,-2$ | stable node |

At the interior point: $f_x=2-\tfrac{16}7-\tfrac67=-\tfrac87$, $g_y=2-\tfrac{24}7-\tfrac27=-\tfrac{12}7$, $g_x=-\tfrac{6/7}{4}=-\tfrac3{14}$. $\tau=-\tfrac{20}7$, $\Delta=\tfrac{96}{49}-\tfrac{8}{7}\cdot\tfrac{3}{14}=\tfrac{96}{49}-\tfrac{12}{49}=\tfrac{12}7$, $\tau^2-4\Delta=\tfrac{400}{49}-\tfrac{336}{49}=\tfrac{64}{49}>0$, $\mu=\tfrac12(-\tfrac{20}7\pm\tfrac87)=-\tfrac67,-2$.

### (iii)

$J=\begin{pmatrix}2-2x-3y&-3x\\-3y&2-4y-3x\end{pmatrix}$.

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(2,2)$ | $2,2$ | unstable node |
| $(2,0)$ | $\begin{pmatrix}-2&-6\\0&-4\end{pmatrix}$ | $-2,-4$ | stable node |
| $(0,1)$ | $\begin{pmatrix}-1&0\\-3&-2\end{pmatrix}$ | $-1,-2$ | stable node |
| $(\tfrac27,\tfrac47)$ | $\begin{pmatrix}-\tfrac27&-\tfrac67\\-\tfrac{12}7&-\tfrac87\end{pmatrix}$ | $\tfrac47,-2$ | saddle |

At the interior point: $\Delta=\tfrac{16}{49}-\tfrac{72}{49}=-\tfrac87<0$, so a saddle; $\tau=-\tfrac{10}7$, $7\mu^2+10\mu-8=0$, $\mu=\dfrac{-10\pm\sqrt{100+224}}{14}=\dfrac{-10\pm18}{14}=\tfrac47,-2$. Eigenvectors: $\mu=-2$: $\tfrac{12}7v_1-\tfrac67v_2=0$, $v=(1,2)$ (stable manifold); $\mu=\tfrac47$: $v=(1,-1)$.

### (iv)

$J=\begin{pmatrix}1-2y&-2x\\3y&-2+3x\end{pmatrix}$.

- $(0,0)$: $\mathrm{diag}(1,-2)$, saddle (axes are the separatrices).
- $(\tfrac23,\tfrac12)$: $J=\begin{pmatrix}0&-\tfrac43\\\tfrac32&0\end{pmatrix}$, $\tau=0$, $\Delta=2$, $\mu=\pm i\sqrt2$: **linear centre**. The linearisation cannot decide (see Exercise 1), so a first integral is used below.

### (v)

$J=\begin{pmatrix}4-x-3y&-3x\\y&-2+x\end{pmatrix}$.

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(4,-2)$ | $4,-2$ | saddle |
| $(8,0)$ | $\begin{pmatrix}-4&-24\\0&6\end{pmatrix}$ | $-4,6$ | saddle |
| $(2,1)$ | $\begin{pmatrix}-1&-6\\1&0\end{pmatrix}$ | $-\tfrac12\pm\tfrac{\sqrt{23}}2i$ | stable spiral |

At $(2,1)$: $\tau=-1$, $\Delta=6$, $\tau^2-4\Delta=-23<0$. At $(8,0)$ the unstable eigenvector ($\mu=6$) solves $-10v_1-24v_2=0$: $v=(12,-5)$, which points out of the quadrant, so inside $x,y\ge0$ only the stable direction (the $x$-axis) matters.

### (vi)

$J=\begin{pmatrix}10-2x-3y&-3x\\y&1+x-20y\end{pmatrix}$.

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(10,1)$ | $10,1$ | unstable node |
| $(10,0)$ | $\begin{pmatrix}-10&-30\\0&11\end{pmatrix}$ | $-10,11$ | saddle |
| $(0,\tfrac1{10})$ | $\begin{pmatrix}\tfrac{97}{10}&0\\\tfrac1{10}&-1\end{pmatrix}$ | $\tfrac{97}{10},-1$ | saddle |
| $(\tfrac{97}{13},\tfrac{11}{13})$ | $\begin{pmatrix}-\tfrac{97}{13}&-\tfrac{291}{13}\\\tfrac{11}{13}&-\tfrac{110}{13}\end{pmatrix}$ | $\dfrac{-207\pm i\sqrt{12635}}{26}$ | stable spiral (strongly damped) |

At the interior point $P=Q=0$ so $J=\begin{pmatrix}-x&-3x\\y&-10y\end{pmatrix}$ with $x=\tfrac{97}{13}$, $y=\tfrac{11}{13}$: $\tau=-(x+10y)=-\tfrac{207}{13}$, $\Delta=10xy+3xy=13xy=\tfrac{1067}{13}$, $\tau^2-4\Delta=\tfrac{42849}{169}-\tfrac{55484}{169}=-\tfrac{12635}{169}<0$. Real part $-\tfrac{207}{26}\approx-7.96$, imaginary part $\approx\pm4.32$: **complex eigenvalues, a stable spiral** (so not a node as one might guess); the damping is so strong that orbits turn at most about half a turn before reaching it. At $(0,\tfrac1{10})$ the unstable eigenvector ($\mu=\tfrac{97}{10}$) solves $\tfrac1{10}v_1-\tfrac{107}{10}v_2=0$: $v=(107,1)$, pointing into the quadrant.

### (vii)

$J=\begin{pmatrix}3-2x-y&-x\\y&-2+x\end{pmatrix}$.

| Point | $J$ | Eigenvalues | Type |
| :-- | :-- | :-- | :-- |
| $(0,0)$ | $\mathrm{diag}(3,-2)$ | $3,-2$ | saddle |
| $(3,0)$ | $\begin{pmatrix}-3&-3\\0&1\end{pmatrix}$ | $-3,1$ | saddle |
| $(2,1)$ | $\begin{pmatrix}-2&-2\\1&0\end{pmatrix}$ | $-1\pm i$ | stable spiral |

At $(2,1)$: $\tau=-2$, $\Delta=2$, $\tau^2-4\Delta=-4$.

## Global Phase Portrait and Interpretation

Direction of the field is read from the signs of $P$ and $Q$ on each side of the nullclines.

### (i)

$\dot x>0\iff x+y<2$, $\dot y>0\iff x+y<1$. Three strips: below $x+y=1$ both grow; between the lines $\dot x>0$, $\dot y<0$; above $x+y=2$ both decrease. Every orbit with $x_0>0$ ends at $(2,0)$ (it crosses into the middle strip, where $x\uparrow$, $y\downarrow$; the $x$-axis is the stable direction). The saddle $(0,1)$ has the $y$-axis as its stable manifold (eigenvalue $-2$, direction $(0,1)^T$, with trajectories climbing from $(0,0)$ to $(0,1)$), while its unstable manifold (eigenvalue $+1$, direction $(3,-2)^T$) enters the first quadrant toward $(2,0)$.

> [!result] Interpretation (i)
> **Competitive exclusion**: species $y$ dies out and $x$ settles at its carrying capacity $2$, whatever the (positive) initial populations, unless $x_0=0$.

![[attachments/AM-PS/ch5-e2-i.svg]]
*Model (i): parallel nullclines, unstable node at the origin, saddle at $(0,1)$ and a stable improper node at $(2,0)$.*

### (ii)

The nullclines cross at $(\tfrac87,\tfrac67)$: on the $x$-axis $\dot y=0$ is at $x=8>2$, on the $y$-axis $\dot x=0$ is at $y=2>1$. Orbits from the quadrant converge to the stable node; the saddles $(2,0)$ and $(0,1)$ have the axes as stable directions and unstable directions pointing into the quadrant towards the node.

> [!result] Interpretation (ii)
> **Stable coexistence**: both species survive at $x=\tfrac87$, $y=\tfrac67$ (each limits itself more than it is limited by the other), regardless of the initial populations as long as both are positive.

![[attachments/AM-PS/ch5-e2-ii.svg]]
*Model (ii): the two nullclines cross at $(8/7,6/7)$, a globally attracting stable node; saddles on the axes.*

### (iii)

Four regions: both grow (near the origin), $\dot x>0>\dot y$ (near $(2,0)$), $\dot y>0>\dot x$ (near $(0,1)$), both decrease. The stable manifold of the saddle $(\tfrac27,\tfrac47)$, tangent to $(1,2)$, separates the basins: orbits above it go to $(0,1)$, orbits below it to $(2,0)$. The unstable direction $(1,-1)$ of the saddle leads to the two nodes.

> [!result] Interpretation (iii)
> **Bistable competition**: the winner depends on the initial conditions; the initially stronger species excludes the other. Coexistence at $(\tfrac27,\tfrac47)$ is unstable and is observed only on the separatrix.

![[attachments/AM-PS/ch5-e2-iii.svg]]
*Model (iii): saddle at $(2/7,4/7)$ whose stable manifold separates the basins of the stable nodes $(2,0)$ and $(0,1)$.*

### (iv)

Both coordinates oscillate. Seek a first integral from
$$\frac{dy}{dx}=\frac{y(-2+3x)}{x(1-2y)}\;\Longrightarrow\;\frac{1-2y}{y}\,dy=\frac{-2+3x}{x}\,dx\;\Longrightarrow\;\Big(\frac1y-2\Big)dy=\Big(-\frac2x+3\Big)dx.$$
Integrating: $\ln y-2y=-2\ln x+3x+c$, i.e.
$$H(x,y)=3x-2\ln x+2y-\ln y=C .$$
Check by the chain rule: $\dot H=\big(3-\tfrac2x\big)\dot x+\big(2-\tfrac1y\big)\dot y=(3x-2)(1-2y)+(2y-1)(3x-2)=0$ ✓. Moreover $H_x=3-\tfrac2x=0$, $H_y=2-\tfrac1y=0$ at $(\tfrac23,\tfrac12)$, with $H_{xx}=\tfrac2{x^2}=\tfrac92>0$, $H_{yy}=\tfrac1{y^2}=4>0$, $H_{xy}=0$: a strict minimum, $H_{\min}=3+\ln\tfrac92$, and $H\to\infty$ at the axes and at infinity. Therefore the level curves are **closed curves around $(\tfrac23,\tfrac12)$**: the centre is genuine, orbits are periodic, counter-clockwise (on $y=\tfrac12$ to the right of the centre $\dot y>0$).

> [!result] Interpretation (iv)
> Neutral predator-prey cycles: prey grow while predators are few ($y<\tfrac12$), predators grow when prey are abundant ($x>\tfrac23$). The amplitude depends on the initial conditions (conserved $H$), the mean levels stay at $(\tfrac23,\tfrac12)$, and neither species dies out; the origin is a saddle with both axes as separatrices.

![[attachments/AM-PS/ch5-e2-iv.svg]]
*Model (iv): saddle at the origin and closed level curves of $H=3x-2\ln x+2y-\ln y$ around the centre $(2/3,1/2)$.*

### (v)

$\dot x>0\iff y<\tfrac43-\tfrac x6$, $\dot y>0\iff x>2$. Orbits spiral counter-clockwise (at $(2+u,1)$ the linearisation gives $\dot v=u>0$) into $(2,1)$. Along $y=0$ the prey grow from $0$ to the capacity $8$ (the $x$-axis is the unstable direction of $(0,0)$ and the stable one of $(8,0)$); along $x=0$ the predators alone decay to $0$ (the $y$-axis is the stable direction of $(0,0)$).

> [!result] Interpretation (v)
> Prey limited by its carrying capacity $8$ and predators coexist: oscillations are damped, populations settle at $x=2$, $y=1$. Removing the predators drives prey to $8$; removing prey kills the predators.

![[attachments/AM-PS/ch5-e2-v.svg]]
*Model (v): saddles at $(0,0)$ and $(8,0)$, damped counter-clockwise spiral into $(2,1)$.*

### (vi)

$\dot x>0\iff x+3y<10$, $\dot y>0\iff 10y<1+x$. The origin is a source of the quadrant; the saddle $(0,\tfrac1{10})$ sends its unstable manifold (direction $(107,1)$) into the interior towards the spiral, the saddle $(10,0)$ is approached along the $x$-axis and left towards the interior. All interior orbits tend to $(\tfrac{97}{13},\tfrac{11}{13})$ with at most a small overshoot.

> [!result] Interpretation (vi)
> Because the predator has alternative food, it never dies out even if prey is absent ($y\to\tfrac1{10}$ on the axis), and the system settles at $x\approx7.46$, $y\approx0.85$.

![[attachments/AM-PS/ch5-e2-vi.svg]]
*Model (vi): unstable node at the origin, saddles at $(0,1/10)$ and $(10,0)$ and the stable interior point $(97/13,11/13)$ (a strongly damped spiral).*

### (vii)

$\dot x>0\iff x+y<3$, $\dot y>0\iff x>2$. The prey nullcline meets the predator nullcline $x=2$ at $(2,1)$. Orbits spiral counter-clockwise into it; the saddle $(3,0)$ has the $x$-axis as stable direction and its unstable direction $(3,-4)$ (from $-4v_1-3v_2=0$ in $(J-I)v=0$ with $J-I=\begin{pmatrix}-4&-3\\0&0\end{pmatrix}$) points out of the quadrant.

> [!result] Interpretation (vii)
> Logistic prey (capacity $3$) sustains the predators: damped oscillations with $\operatorname{Re}\mu=-1$ and period $2\pi$ to the stable coexistence point $x=2$, $y=1$.

![[attachments/AM-PS/ch5-e2-vii.svg]]
*Model (vii): saddles at $(0,0)$ and $(3,0)$ and a stable spiral at $(2,1)$.*
