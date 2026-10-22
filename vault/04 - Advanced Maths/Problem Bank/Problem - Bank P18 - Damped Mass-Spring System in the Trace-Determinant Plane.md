---
materia: Advanced Maths
tema: "Unit 4: linear systems and phase portraits"
bank_id: P18
title: "Damped mass-spring as a first-order system: the origin in the trace-determinant plane as the damping grows, and the critically damped motion through a generalised eigenvector"
category: final_problem
archetype: linear-systems-phase-portrait
level: standard
unit: 4
difficulty: 2
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2012_ORD, MATHS_FINALEXAM_2016_PRACTICE and MATHS_FINALEXAM_2024_ORD; not an official exercise. Verified with scripts/am_bank/p18.py"
tags:
  - problem-bank
  - final-exam
  - damped-oscillator
  - trace-determinant
  - repeated-eigenvalue
  - generalised-eigenvector
  - phase-portrait
---

# Bank P18 — Damped mass-spring system in the trace-determinant plane

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FINALEXAM_2012_ORD, MATHS_FINALEXAM_2016_PRACTICE and MATHS_FINALEXAM_2024_ORD. Method: Robinson Sec. 13.1 and 13.3 (spring and damped oscillations), Sec. 25.1 (second-order equation as a system), Ch. 28-30 (real, complex and repeated eigenvalues) and Ch. 31 (summary of phase portraits); Notes, p. 9-10. Every result was checked with SymPy (scripts/am_bank/p18.py).

## Statement

A body of mass $m=1$ kg hangs from a spring of stiffness $k=4$ N/m and moves inside a dashpot of damping coefficient $c\ge0$ (N s/m). Its displacement $x(t)$ (m) from the equilibrium position obeys

$$
m\ddot x+c\dot x+kx=0 .
$$

(a) Write the equation as a first-order system $\dot{\mathbf X}=A\mathbf X$ for $\mathbf X=(x,\,v)^T$ with $v=\dot x$, for general $m,k>0$ and $c\ge0$. Locate $A$ in the trace-determinant plane and classify the origin as a function of $c$: undamped, under-damped, critically damped and over-damped motion. With $m=1$, $k=4$ give the critical value $c_{cr}$ and the eigenvalues for $c=0$, $c=2$ and $c=5$, and describe each phase portrait in words.

(b) Take the critically damped case $c=c_{cr}$. Find the eigenvalue and eigenvector of $A$, a generalised eigenvector $\mathbf w$ with $(A-\lambda I)\mathbf w=\mathbf v$, the matrix $P=[\mathbf v\mid\mathbf w]$, and check explicitly that $P^{-1}AP$ is the Jordan form. Write the general solution. The body is released from $x(0)=1$ m with velocity $v(0)=v_0$: find $x(t)$, the values of $v_0$ for which the body crosses the equilibrium position, and the crossing time for $v_0=-6$ m/s. For $v_0=0$, find the largest speed reached.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $x(t)$ (m), independent variable $t\ge0$ (s). Linear, homogeneous, constant coefficients, second order; $m,k>0$, $c\ge0$.
- Units: $c/m$ and $\sqrt{k/m}$ are s$^{-1}$; $k/m$ is s$^{-2}$. Eigenvalues are rates in s$^{-1}$.
- The coefficients are constant, so the existence and uniqueness theorem (Robinson Thm 11.1, Thm 25.2) gives a unique solution for every $(x(0),v(0))$, defined for all $t$.

| Symbol | Value | Unit |
| :--- | :--- | :--- |
| $m$ | $1$ | kg |
| $k$ | $4$ | N/m |
| $c$ | $\ge0$, parameter | N s/m |
| $x(0)$ | $1$ | m |
| $v(0)$ | $v_0$ | m/s |

#### Phase 2. Canonical formulation

With $x_1=x$, $x_2=v=\dot x$ (Robinson Sec. 25.1): $\dot x_1=x_2$ and, dividing the equation by $m$, $\dot x_2=-\frac km x_1-\frac cm x_2$:

$$
\frac{d}{dt}\begin{pmatrix}x\\v\end{pmatrix}=\begin{pmatrix}0&1\\-\frac km&-\frac cm\end{pmatrix}\begin{pmatrix}x\\v\end{pmatrix},\qquad A=\begin{pmatrix}0&1\\-\frac km&-\frac cm\end{pmatrix}.
$$

## (a) Classification of the origin as the damping varies [1.0 pts]

### Hint

$\operatorname{tr}A=-c/m$, $\det A=k/m$. Compare $(\operatorname{tr}A)^2$ with $4\det A$.

### Checkpoint

- $\lambda^2+\frac cm\lambda+\frac km=0$; discriminant $\dfrac{c^2-4mk}{m^2}$; $c_{cr}=2\sqrt{mk}=4$ N s/m.
- $c=0$: centre, $\lambda=\pm2i$. $0<c<4$: stable focus ($c=2$: $\lambda=-1\pm\sqrt3\,i$). $c=4$: stable degenerate node, $\lambda=-2$ double. $c>4$: stable node ($c=5$: $\lambda=-1,-4$).
- Rotation in the $(x,v)$ plane is clockwise in every oscillating case.

### Solution

#### Step 1. Trace, determinant, characteristic polynomial

$$
\det(A-\lambda I)=\begin{vmatrix}-\lambda&1\\-\frac km&-\frac cm-\lambda\end{vmatrix}=(-\lambda)\left(-\frac cm-\lambda\right)-1\cdot\left(-\frac km\right)=\lambda^2+\frac cm\lambda+\frac km .
$$

It is the characteristic equation of the scalar ODE divided by $m$, as it must be. Hence $\operatorname{tr}A=-\frac cm\le0$, $\det A=\frac km>0$ and

$$
\lambda_\pm=\frac{-\frac cm\pm\sqrt{\frac{c^2}{m^2}-\frac{4k}m}}{2}=\frac{-c\pm\sqrt{c^2-4mk}}{2m}.
$$

#### Step 2. The point $A$ in the trace-determinant plane

$\det A=k/m$ is fixed and positive, so the origin is never a saddle. As $c$ grows from $0$, the point $(\operatorname{tr},\det)=(-c/m,\,k/m)$ moves left along the horizontal line $\det=k/m$, starting on the $\det$ axis and crossing the parabola $\operatorname{tr}^2=4\det$ at $c/m=2\sqrt{k/m}$, i.e. $c_{cr}=2\sqrt{mk}$ (Robinson Ch. 31):

| Damping | Position | Eigenvalues | Origin |
| :--- | :--- | :--- | :--- |
| $c=0$ (undamped) | on the $\det$ axis | $\pm i\sqrt{k/m}$ | centre (stable, not asymptotically) |
| $0<c<c_{cr}$ (under-damped) | inside the parabola | $-\frac c{2m}\pm i\frac{\sqrt{4mk-c^2}}{2m}$ | stable focus |
| $c=c_{cr}$ (critical) | on the parabola | $-\frac c{2m}$, double | stable degenerate node |
| $c>c_{cr}$ (over-damped) | outside the parabola | two negative reals | stable node |

With $m=1$, $k=4$: $c_{cr}=2\sqrt{1\cdot4}=4$ N s/m.

#### Step 3. The three sample values

- $c=0$: $\lambda^2+4=0$, $\lambda=\pm2i$. Energy $\tfrac12mv^2+\tfrac12kx^2$ is conserved, so the orbits are the ellipses $4x^2+v^2=\text{const}$ (period $\pi$ s). Test vector $\mathbf X=(1,0)$: $A\mathbf X=(0,-4)$ points down, so the motion is **clockwise**.
- $c=2$: $\lambda^2+2\lambda+4=0$, $\lambda=\dfrac{-2\pm\sqrt{4-16}}{2}=-1\pm\sqrt3\,i$. Clockwise spirals into the origin (same test vector: $A(1,0)^T=(0,-4)^T$), amplitude decaying as $e^{-t}$.
- $c=5$: $\lambda^2+5\lambda+4=(\lambda+1)(\lambda+4)=0$, $\lambda_1=-1$, $\lambda_2=-4$. Eigenvectors from row 1 of $(A-\lambda I)\mathbf v=\mathbf 0$, $-\lambda v_1+v_2=0$: $\mathbf v_1=(1,-1)$, $\mathbf v_2=(1,-4)$. Stable node; orbits reach the origin tangent to the slow direction $(1,-1)$ (smaller $\lvert\lambda\rvert$), and far away they are parallel to $(1,-4)$. The body returns to rest without oscillating, and it can cross $x=0$ at most once.

## (b) Critically damped motion with a generalised eigenvector [1.5 pts]

### Hint

With a double eigenvalue and only one eigenvector, try $\mathbf X=e^{\lambda t}(t\mathbf v+\mathbf w)$ (Robinson Ch. 30). The sign of the coefficient of $t$ in $x(t)$ decides whether $x$ can vanish.

### Checkpoint

- $A=\begin{pmatrix}0&1\\-4&-4\end{pmatrix}$, $\lambda=-2$ (double), $\mathbf v=(1,-2)$, $\mathbf w=(0,1)$.
- $P=\begin{pmatrix}1&0\\-2&1\end{pmatrix}$, $P^{-1}=\begin{pmatrix}1&0\\2&1\end{pmatrix}$, $P^{-1}AP=\begin{pmatrix}-2&1\\0&-2\end{pmatrix}$.
- $x(t)=\big(1+(v_0+2)t\big)e^{-2t}$; crosses $x=0$ once iff $v_0<-2$ m/s, at $t^*=-\dfrac1{v_0+2}$; $v_0=-6$ m/s gives $t^*=0.25$ s.
- $v_0=0$: $v(t)=-4te^{-2t}$, largest speed $2/e\approx0.736$ m/s at $t=0.5$ s.

### Solution

#### Step 1. Eigenvalue and eigenvector

With $c=4$: $\lambda^2+4\lambda+4=(\lambda+2)^2=0$, so $\lambda=-2$ with algebraic multiplicity 2. Then

$$
A+2I=\begin{pmatrix}2&1\\-4&-2\end{pmatrix}.
$$

Row 1: $2v_1+v_2=0$; row 2: $-4v_1-2v_2=-2(2v_1+v_2)=0$, the same equation. One free parameter: $\mathbf v=(1,-2)$. Since $A+2I\neq0$, there is no second independent eigenvector.

#### Step 2. Generalised eigenvector

Solve $(A+2I)\mathbf w=\mathbf v$: row 1 gives $2w_1+w_2=1$, row 2 gives $-4w_1-2w_2=-2$, which is row 1 times $-2$ (consistent). Choose $w_1=0$: $\mathbf w=(0,1)$. Check: $(A+2I)\mathbf w=(2\cdot0+1,\ -4\cdot0-2\cdot1)=(1,-2)=\mathbf v$. Also $(A+2I)^2=\begin{pmatrix}4-4&2-2\\-8+8&-4+4\end{pmatrix}=0$, so $(A+2I)^2\mathbf w=\mathbf 0$ as it must.

#### Step 3. Change of basis and Jordan form

$$
P=[\mathbf v\mid\mathbf w]=\begin{pmatrix}1&0\\-2&1\end{pmatrix},\qquad \det P=1\cdot1-0\cdot(-2)=1,\qquad P^{-1}=\frac11\begin{pmatrix}1&0\\2&1\end{pmatrix}.
$$

Columns of $AP$: $A\mathbf v=-2\mathbf v=(-2,4)$ and $A\mathbf w=-2\mathbf w+\mathbf v=(0,-2)+(1,-2)=(1,-4)$; check directly: $A\mathbf w=(0\cdot0+1\cdot1,\ -4\cdot0-4\cdot1)=(1,-4)$. So $AP=\begin{pmatrix}-2&1\\4&-4\end{pmatrix}$ and

$$
\begin{aligned}
(P^{-1}AP)_{11}&=1\cdot(-2)+0\cdot4=-2, & (P^{-1}AP)_{12}&=1\cdot1+0\cdot(-4)=1,\\
(P^{-1}AP)_{21}&=2\cdot(-2)+1\cdot4=0, & (P^{-1}AP)_{22}&=2\cdot1+1\cdot(-4)=-2,
\end{aligned}
\qquad P^{-1}AP=\begin{pmatrix}-2&1\\0&-2\end{pmatrix}=J .
$$

#### Step 4. Solution in the canonical coordinates

With $\mathbf z=P^{-1}\mathbf X$: $\dot z_2=-2z_2$ and $\dot z_1=-2z_1+z_2$. The first gives $z_2=c_2e^{-2t}$. The second is linear: multiply by the integrating factor $e^{2t}$, so by the product rule $\frac d{dt}(e^{2t}z_1)=e^{2t}(\dot z_1+2z_1)=e^{2t}z_2=c_2$. Integrate from $0$ to $t$ with Barrow's rule: $e^{2t}z_1(t)-z_1(0)=c_2\,[s]_0^t=c_2t$, so $z_1=(c_1+c_2t)e^{-2t}$ with $c_1=z_1(0)$.

#### Step 5. General solution

$\mathbf X=P\mathbf z=z_1\mathbf v+z_2\mathbf w$:

$$
\mathbf X(t)=c_1e^{-2t}\begin{pmatrix}1\\-2\end{pmatrix}+c_2e^{-2t}\left[t\begin{pmatrix}1\\-2\end{pmatrix}+\begin{pmatrix}0\\1\end{pmatrix}\right],
\qquad x(t)=(c_1+c_2t)e^{-2t},\quad v(t)=(-2c_1+c_2-2c_2t)e^{-2t}.
$$

Check $v=\dot x$ by the product rule: $\dot x=c_2e^{-2t}+(c_1+c_2t)(-2)e^{-2t}=(c_2-2c_1-2c_2t)e^{-2t}$.

#### Step 6. Initial conditions

$x(0)=c_1=1$, $v(0)=-2c_1+c_2=v_0\Rightarrow c_2=v_0+2$:

$$
x(t)=\big(1+(v_0+2)\,t\big)e^{-2t}.
$$

Substitution check: with $x=(1+\beta t)e^{-2t}$, $\beta=v_0+2$, $\dot x=(\beta-2-2\beta t)e^{-2t}$, $\ddot x=(-4\beta+4+4\beta t)e^{-2t}$, and $\ddot x+4\dot x+4x=e^{-2t}\big[(4-4\beta+4\beta t)+(4\beta-8-8\beta t)+(4+4\beta t)\big]=0$.

#### Step 7. Crossing the equilibrium

$e^{-2t}>0$, so $x(t^*)=0\iff1+(v_0+2)t^*=0\iff t^*=-\dfrac1{v_0+2}$. This is a positive time only if $v_0+2<0$: the body crosses $x=0$ (exactly once) iff $v_0<-2$ m/s, i.e. it is thrown towards the equilibrium fast enough. For $v_0=-6$: $t^*=-\frac1{-4}=0.25$ s. For $v_0\ge-2$ it approaches $x=0$ from above without reaching it.

#### Step 8. Largest speed for $v_0=0$

$x=(1+2t)e^{-2t}$ and $v=\dot x=(2-2-4t)e^{-2t}=-4te^{-2t}$. Then $\dot v=(-4+8t)e^{-2t}=0$ at $t=\tfrac12$ s, a minimum of $v$ (sign of $\dot v$ changes from $-$ to $+$). $\lvert v\rvert_{\max}=4\cdot\tfrac12e^{-1}=\dfrac2e\approx0.736$ m/s.

#### Step 9. Phase portrait

Degenerate stable node (Robinson Ch. 30): the only straight-line orbits lie on the eigenline $v=-2x$, with arrows pointing to the origin. Every other orbit is dominated by $c_2te^{-2t}\mathbf v$ both as $t\to+\infty$ (it enters the origin tangent to $v=-2x$) and as $t\to-\infty$ (it comes from far away parallel to the same line). Test vector $(1,0)$: $A(1,0)^T=(0,-4)^T$, so orbits turn clockwise, and those that start above the eigenline with $v_0<-2$ cross the $v$ axis ($x=0$) once before turning back towards the origin.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $t\to\infty$: $\mathbf X\to\mathbf 0$ for all $c>0$ (all eigenvalues have negative real part). Decay rate of the slowest mode, $\min\lvert\operatorname{Re}\lambda\rvert$: $c/(2m)$ below critical, $2$ s$^{-1}$ at $c=4$, and $\frac{c-\sqrt{c^2-16}}{2}\to0$ as $c\to\infty$ (very strong damping is slow). Critical damping gives the fastest return without oscillation. $c\to0$: focus $\to$ centre.
- **Checks:** dimensions: $c_{cr}=2\sqrt{mk}$ has $\sqrt{\text{kg}\cdot\text{N/m}}=\sqrt{\text{kg}^2\text{s}^{-2}}=$ kg/s = N s/m; $t^*=-1/(v_0+2)$: the $2$ is $2$ s$^{-1}\cdot1$ m, so $v_0+2$ is in m/s and $t^*=x(0)/\lvert v_0+2\rvert$ in s. Substitution of $x(t)$ in the ODE and of $\mathbf X$ in $\dot{\mathbf X}=A\mathbf X$ (script); $P^{-1}AP=J$.
- **Common mistakes in the exam:** (1) looking for a second eigenvector at $\lambda=-2$ and writing $c_1e^{-2t}\mathbf v+c_2e^{-2t}\mathbf v$, which is one solution twice; (2) writing the second solution as $te^{-2t}\mathbf v$ alone, without $\mathbf w$: it does not satisfy the system; (3) saying a critically damped body can never cross equilibrium: it can, once, when $v_0<-2$ m/s; (4) placing the over-damped case inside the parabola: the parabola $\operatorname{tr}^2=4\det$ separates foci (inside) from nodes (outside).

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
