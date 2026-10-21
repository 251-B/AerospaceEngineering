---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 9"
dificultad: media
id: "e9"
pill: "Diagonalisation • Decoupling • Four Matrices"
tags:
  - problema-resuelto
  - diagonalizacion
  - desacoplamiento
  - retrato-de-fase
---

# Problem 4.I.9: Decoupling Four Systems with Real Eigenvalues

> Official exercise 9 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Find the eigenvalues and eigenvectors of the matrix on the right-hand side in each case, and hence find the coordinate transformation that will decouple the corresponding equations. Show that this transformation has the desired effect. You can also write down the general solution and draw the phase portrait for the equation.

- (i) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 8 & 14 \\ 7 & 1 \end{pmatrix}\mathbf x$;
- (ii) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 2 & 0 \\ -5 & -3 \end{pmatrix}\mathbf x$;
- (iii) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 11 & -2 \\ 3 & 4 \end{pmatrix}\mathbf x$;
- (iv) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 1 & 20 \\ 40 & -19 \end{pmatrix}\mathbf x$.

## Phase 1: Setup

Each system is $\dot{\mathbf x} = A\mathbf x$ with a constant $2\times 2$ matrix. Plan (Topic 4 Sec. 4 and 5): (a) characteristic equation $\det(A - \lambda I) = 0$; (b) eigenvectors from $(A - \lambda I)\mathbf v = \mathbf 0$; (c) if the eigenvalues are real and distinct the eigenvectors are independent and $Q = [\mathbf v_1\ \mathbf v_2]$ defines $\mathbf z = Q^{-1}\mathbf x$ with $\dot{\mathbf z} = Q^{-1}AQ\,\mathbf z$; (d) show $Q^{-1}AQ = \Lambda$ by explicit multiplication.

## Phase 2: Formulation

Since $\mathbf x = Q\mathbf z$ with $Q$ constant, $\dot{\mathbf x} = Q\dot{\mathbf z}$ and $A\mathbf x = AQ\mathbf z$, so $\dot{\mathbf z} = Q^{-1}AQ\,\mathbf z$. If $Q^{-1}AQ = \Lambda = \operatorname{diag}(\lambda_1, \lambda_2)$ the equations $\dot z_1 = \lambda_1z_1$, $\dot z_2 = \lambda_2z_2$ are uncoupled.

## Phase 3: Derivation

### (i) $A = \begin{pmatrix} 8 & 14 \\ 7 & 1 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 8 - \lambda & 14 \\ 7 & 1 - \lambda \end{vmatrix} = (8 - \lambda)(1 - \lambda) - (14)(7) $$

$$ = \lambda^2 - (8 + 1)\lambda + (8\cdot1 - 14\cdot7) = \lambda^2 - (9)\lambda + (-90) = \lambda^{2} - 9 \lambda - 90 $$

$\operatorname{tr}A = 9$, $\det A = -90$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 81 - (-360) = 441$.

$$ \lambda = \frac{9 \pm \sqrt{441}}{2} = \frac{9 \pm 21}{2} \quad\Longrightarrow\quad \lambda_1 = 15,\ \lambda_2 = -6 $$

Check: $\lambda_1 + \lambda_2 = 9 = \operatorname{tr}A$ and $\lambda_1\lambda_2 = -90 = \det A$.

#### Eigenvectors

For $\lambda = 15$: $(A - (15)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} -7 & 14 \\ 7 & -14 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} -7v_1 + 14v_2 = 0\quad (\text{row 1}) \\ 7v_1 - 14v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $-1$ times row 1) and express a single condition. Row 1 reads $-7v_1 + 14v_2 = 0$, so $v_1 = 2\,v_2$: every eigenvector is a multiple of $(2, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} 30 \\ 15 \end{pmatrix} = 15\mathbf{v_1}$.

For $\lambda = -6$: $(A - (-6)I)\mathbf{v_2} = \mathbf 0$, that is

$$ \begin{pmatrix} 14 & 14 \\ 7 & 7 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 14v_1 + 14v_2 = 0\quad (\text{row 1}) \\ 7v_1 + 7v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $\frac{1}{2}$ times row 1) and express a single condition. Row 1 reads $14v_1 + 14v_2 = 0$, so $v_1 = -v_2$: every eigenvector is a multiple of $(-1, 1)^T$. The smallest integer representative is

$$ \mathbf{v_2} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} $$

Check: $A\mathbf{v_2} = \begin{pmatrix} -6 \\ 6 \end{pmatrix} = -6\mathbf{v_2}$.

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix} $$

$\det Q = (2)(-1) - (1)(1) = -3$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-3}\begin{pmatrix} -1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} \frac{1}{3} & \frac{1}{3} \\ \frac{1}{3} & - \frac{2}{3} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} 8 & 14 \\ 7 & 1 \end{pmatrix}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 30 \\ 15 \end{pmatrix} = 15\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 8 & 14 \\ 7 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} -6 \\ 6 \end{pmatrix} = (-6)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 30 & -6 \\ 15 & 6 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{1}{3}\cdot30 + \frac{1}{3}\cdot15 = 15 \\ (Q^{-1}AQ)_{12} &= \frac{1}{3}\cdot(-6) + \frac{1}{3}\cdot6 = 0 \\ (Q^{-1}AQ)_{21} &= \frac{1}{3}\cdot30 + (- \frac{2}{3})\cdot15 = 0 \\ (Q^{-1}AQ)_{22} &= \frac{1}{3}\cdot(-6) + (- \frac{2}{3})\cdot6 = -6 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 15 & 0 \\ 0 & -6 \end{pmatrix} = \Lambda = \begin{pmatrix} 15 & 0 \\ 0 & -6 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 15z_1, \qquad \dot z_2 = -6z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{15t}, \qquad z_2(t) = c_2 e^{-6t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{15t}\begin{pmatrix} 2 \\ 1 \end{pmatrix} + c_2 e^{-6t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} $$

$$ x(t) = 2 c_{1} e^{15 t} + c_{2} e^{-6 t}, \qquad y(t) = c_{1} e^{15 t} - c_{2} e^{-6 t} $$

#### The decoupling transformation

In the original variables $\mathbf x = (x, y)^T$ the new coordinates are $\mathbf z = Q^{-1}\mathbf x$:

$$ z_1 = \frac{x}{3} + \frac{y}{3}, \qquad z_2 = \frac{x}{3} - \frac{2 y}{3} $$

#### Phase portrait

$\lambda_1 = 15$ and $\lambda_2 = -6$ are of opposite signs: the origin is a **saddle** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{15t}$ and $z_2 = c_2e^{-6t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{- \frac{2}{5}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = - \frac{2}{5}$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through $(1, -1)$ (the **stable manifold**), reach the origin as $t \to +\infty$; the line through $(2, 1)$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (2, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, -1)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 15\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = -6\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e9-i-z.svg]]
*Canonical $\mathbf z$-plane (saddle): invariant axes and orbits $z_2 = K|z_1|^{- \frac{2}{5}}$.*

![[attachments/AM-PS/ch4a-e9-i-x.svg]]
*Original $(x, y)$-plane (saddle): dashed lines are the eigenlines $\mathbf v_1 = (2, 1)$ and $\mathbf v_2 = (1, -1)$.*

### (ii) $A = \begin{pmatrix} 2 & 0 \\ -5 & -3 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 2 - \lambda & 0 \\ -5 & -3 - \lambda \end{vmatrix} = (2 - \lambda)(-3 - \lambda) - (0)(-5) $$

$$ = \lambda^2 - (2 + (-3))\lambda + (2\cdot(-3) - 0\cdot(-5)) = \lambda^2 - (-1)\lambda + (-6) = \lambda^{2} + \lambda - 6 $$

$\operatorname{tr}A = -1$, $\det A = -6$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 1 - (-24) = 25$.

$$ \lambda = \frac{-1 \pm \sqrt{25}}{2} = \frac{-1 \pm 5}{2} \quad\Longrightarrow\quad \lambda_1 = 2,\ \lambda_2 = -3 $$

Check: $\lambda_1 + \lambda_2 = -1 = \operatorname{tr}A$ and $\lambda_1\lambda_2 = -6 = \det A$.

#### Eigenvectors

For $\lambda = 2$: $(A - (2)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} 0 & 0 \\ -5 & -5 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 0v_1 + 0v_2 = 0\quad (\text{row 1}) \\ -5v_1 - 5v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 1 is identically zero) and express a single condition. Row 2 reads $-5v_1 + (-5)v_2 = 0$, so $v_1 = -v_2$: every eigenvector is a multiple of $(-1, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} 2 \\ -2 \end{pmatrix} = 2\mathbf{v_1}$.

For $\lambda = -3$: $(A - (-3)I)\mathbf{v_2} = \mathbf 0$, that is

$$ \begin{pmatrix} 5 & 0 \\ -5 & 0 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 5v_1 + 0v_2 = 0\quad (\text{row 1}) \\ -5v_1 + 0v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $-1$ times row 1) and express a single condition. Row 1 reads $5v_1 + 0v_2 = 0$, so $v_1 = 0$ and $v_2$ is free; the simplest choice is

$$ \mathbf{v_2} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_2} = \begin{pmatrix} 0 \\ -3 \end{pmatrix} = -3\mathbf{v_2}$.

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} $$

$\det Q = (1)(1) - (0)(-1) = 1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{1}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} 2 & 0 \\ -5 & -3 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \end{pmatrix} = 2\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 2 & 0 \\ -5 & -3 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -3 \end{pmatrix} = (-3)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 2 & 0 \\ -2 & -3 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 1\cdot2 + 0\cdot(-2) = 2 \\ (Q^{-1}AQ)_{12} &= 1\cdot0 + 0\cdot(-3) = 0 \\ (Q^{-1}AQ)_{21} &= 1\cdot2 + 1\cdot(-2) = 0 \\ (Q^{-1}AQ)_{22} &= 1\cdot0 + 1\cdot(-3) = -3 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix} = \Lambda = \begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 2z_1, \qquad \dot z_2 = -3z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{2t}, \qquad z_2(t) = c_2 e^{-3t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} + c_2 e^{-3t}\begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

$$ x(t) = c_{1} e^{2 t}, \qquad y(t) = - c_{1} e^{2 t} + c_{2} e^{-3 t} $$

#### The decoupling transformation

In the original variables $\mathbf x = (x, y)^T$ the new coordinates are $\mathbf z = Q^{-1}\mathbf x$:

$$ z_1 = x, \qquad z_2 = x + y $$

#### Phase portrait

$\lambda_1 = 2$ and $\lambda_2 = -3$ are of opposite signs: the origin is a **saddle** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{2t}$ and $z_2 = c_2e^{-3t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{- \frac{3}{2}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = - \frac{3}{2}$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through $(0, 1)$ (the **stable manifold**), reach the origin as $t \to +\infty$; the line through $(1, -1)$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, -1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (0, 1)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 2\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = -3\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e9-ii-z.svg]]
*Canonical $\mathbf z$-plane (saddle): invariant axes and orbits $z_2 = K|z_1|^{- \frac{3}{2}}$.*

![[attachments/AM-PS/ch4a-e9-ii-x.svg]]
*Original $(x, y)$-plane (saddle): dashed lines are the eigenlines $\mathbf v_1 = (1, -1)$ and $\mathbf v_2 = (0, 1)$.*

### (iii) $A = \begin{pmatrix} 11 & -2 \\ 3 & 4 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 11 - \lambda & -2 \\ 3 & 4 - \lambda \end{vmatrix} = (11 - \lambda)(4 - \lambda) - (-2)(3) $$

$$ = \lambda^2 - (11 + 4)\lambda + (11\cdot4 - (-2)\cdot3) = \lambda^2 - (15)\lambda + (50) = \lambda^{2} - 15 \lambda + 50 $$

$\operatorname{tr}A = 15$, $\det A = 50$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 225 - 200 = 25$.

$$ \lambda = \frac{15 \pm \sqrt{25}}{2} = \frac{15 \pm 5}{2} \quad\Longrightarrow\quad \lambda_1 = 10,\ \lambda_2 = 5 $$

Check: $\lambda_1 + \lambda_2 = 15 = \operatorname{tr}A$ and $\lambda_1\lambda_2 = 50 = \det A$.

#### Eigenvectors

For $\lambda = 10$: $(A - (10)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} 1 & -2 \\ 3 & -6 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 1v_1 - 2v_2 = 0\quad (\text{row 1}) \\ 3v_1 - 6v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $3$ times row 1) and express a single condition. Row 1 reads $1v_1 + (-2)v_2 = 0$, so $v_1 = 2\,v_2$: every eigenvector is a multiple of $(2, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} 20 \\ 10 \end{pmatrix} = 10\mathbf{v_1}$.

For $\lambda = 5$: $(A - (5)I)\mathbf{v_2} = \mathbf 0$, that is

$$ \begin{pmatrix} 6 & -2 \\ 3 & -1 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 6v_1 - 2v_2 = 0\quad (\text{row 1}) \\ 3v_1 - 1v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $\frac{1}{2}$ times row 1) and express a single condition. Row 1 reads $6v_1 + (-2)v_2 = 0$, so $v_1 = \frac{1}{3}\,v_2$: every eigenvector is a multiple of $(\frac{1}{3}, 1)^T$. The smallest integer representative is

$$ \mathbf{v_2} = \begin{pmatrix} 1 \\ 3 \end{pmatrix} $$

Check: $A\mathbf{v_2} = \begin{pmatrix} 5 \\ 15 \end{pmatrix} = 5\mathbf{v_2}$.

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} $$

$\det Q = (2)(3) - (1)(1) = 5$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} \frac{3}{5} & - \frac{1}{5} \\ - \frac{1}{5} & \frac{2}{5} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} 11 & -2 \\ 3 & 4 \end{pmatrix}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 20 \\ 10 \end{pmatrix} = 10\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 11 & -2 \\ 3 & 4 \end{pmatrix}\begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 5 \\ 15 \end{pmatrix} = 5\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 20 & 5 \\ 10 & 15 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{3}{5}\cdot20 + (- \frac{1}{5})\cdot10 = 10 \\ (Q^{-1}AQ)_{12} &= \frac{3}{5}\cdot5 + (- \frac{1}{5})\cdot15 = 0 \\ (Q^{-1}AQ)_{21} &= (- \frac{1}{5})\cdot20 + \frac{2}{5}\cdot10 = 0 \\ (Q^{-1}AQ)_{22} &= (- \frac{1}{5})\cdot5 + \frac{2}{5}\cdot15 = 5 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 10 & 0 \\ 0 & 5 \end{pmatrix} = \Lambda = \begin{pmatrix} 10 & 0 \\ 0 & 5 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 10z_1, \qquad \dot z_2 = 5z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{10t}, \qquad z_2(t) = c_2 e^{5t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{10t}\begin{pmatrix} 2 \\ 1 \end{pmatrix} + c_2 e^{5t}\begin{pmatrix} 1 \\ 3 \end{pmatrix} $$

$$ x(t) = 2 c_{1} e^{10 t} + c_{2} e^{5 t}, \qquad y(t) = c_{1} e^{10 t} + 3 c_{2} e^{5 t} $$

#### The decoupling transformation

In the original variables $\mathbf x = (x, y)^T$ the new coordinates are $\mathbf z = Q^{-1}\mathbf x$:

$$ z_1 = \frac{3 x}{5} - \frac{y}{5}, \qquad z_2 = - \frac{x}{5} + \frac{2 y}{5} $$

#### Phase portrait

$\lambda_1 = 10$ and $\lambda_2 = 5$ are both positive: the origin is a **unstable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{10t}$ and $z_2 = c_2e^{5t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{\frac{1}{2}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = \frac{1}{2}$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 5$, i.e. to the line through $(1, 3)$ (they leave from there (the limit $t \to -\infty$)), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point away from the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (2, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, 3)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 10\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = 5\mathbf v_2$ points outward.

![[attachments/AM-PS/ch4a-e9-iii-z.svg]]
*Canonical $\mathbf z$-plane (unstable node): invariant axes and orbits $z_2 = K|z_1|^{\frac{1}{2}}$.*

![[attachments/AM-PS/ch4a-e9-iii-x.svg]]
*Original $(x, y)$-plane (unstable node): dashed lines are the eigenlines $\mathbf v_1 = (2, 1)$ and $\mathbf v_2 = (1, 3)$.*

### (iv) $A = \begin{pmatrix} 1 & 20 \\ 40 & -19 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 1 - \lambda & 20 \\ 40 & -19 - \lambda \end{vmatrix} = (1 - \lambda)(-19 - \lambda) - (20)(40) $$

$$ = \lambda^2 - (1 + (-19))\lambda + (1\cdot(-19) - 20\cdot40) = \lambda^2 - (-18)\lambda + (-819) = \lambda^{2} + 18 \lambda - 819 $$

$\operatorname{tr}A = -18$, $\det A = -819$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 324 - (-3276) = 3600$.

$$ \lambda = \frac{-18 \pm \sqrt{3600}}{2} = \frac{-18 \pm 60}{2} \quad\Longrightarrow\quad \lambda_1 = 21,\ \lambda_2 = -39 $$

Check: $\lambda_1 + \lambda_2 = -18 = \operatorname{tr}A$ and $\lambda_1\lambda_2 = -819 = \det A$.

#### Eigenvectors

For $\lambda = 21$: $(A - (21)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} -20 & 20 \\ 40 & -40 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} -20v_1 + 20v_2 = 0\quad (\text{row 1}) \\ 40v_1 - 40v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $-2$ times row 1) and express a single condition. Row 1 reads $-20v_1 + 20v_2 = 0$, so $v_1 = v_2$: every eigenvector is a multiple of $(1, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} 21 \\ 21 \end{pmatrix} = 21\mathbf{v_1}$.

For $\lambda = -39$: $(A - (-39)I)\mathbf{v_2} = \mathbf 0$, that is

$$ \begin{pmatrix} 40 & 20 \\ 40 & 20 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 40v_1 + 20v_2 = 0\quad (\text{row 1}) \\ 40v_1 + 20v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 is identical to row 1) and express a single condition. Row 1 reads $40v_1 + 20v_2 = 0$, so $v_1 = - \frac{1}{2}\,v_2$: every eigenvector is a multiple of $(- \frac{1}{2}, 1)^T$. The smallest integer representative is

$$ \mathbf{v_2} = \begin{pmatrix} 1 \\ -2 \end{pmatrix} $$

Check: $A\mathbf{v_2} = \begin{pmatrix} -39 \\ 78 \end{pmatrix} = -39\mathbf{v_2}$.

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix} $$

$\det Q = (1)(-2) - (1)(1) = -3$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-3}\begin{pmatrix} -2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{2}{3} & \frac{1}{3} \\ \frac{1}{3} & - \frac{1}{3} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} 1 & 20 \\ 40 & -19 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 21 \\ 21 \end{pmatrix} = 21\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 1 & 20 \\ 40 & -19 \end{pmatrix}\begin{pmatrix} 1 \\ -2 \end{pmatrix} = \begin{pmatrix} -39 \\ 78 \end{pmatrix} = (-39)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 21 & -39 \\ 21 & 78 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{2}{3}\cdot21 + \frac{1}{3}\cdot21 = 21 \\ (Q^{-1}AQ)_{12} &= \frac{2}{3}\cdot(-39) + \frac{1}{3}\cdot78 = 0 \\ (Q^{-1}AQ)_{21} &= \frac{1}{3}\cdot21 + (- \frac{1}{3})\cdot21 = 0 \\ (Q^{-1}AQ)_{22} &= \frac{1}{3}\cdot(-39) + (- \frac{1}{3})\cdot78 = -39 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 21 & 0 \\ 0 & -39 \end{pmatrix} = \Lambda = \begin{pmatrix} 21 & 0 \\ 0 & -39 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 21z_1, \qquad \dot z_2 = -39z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{21t}, \qquad z_2(t) = c_2 e^{-39t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{21t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2 e^{-39t}\begin{pmatrix} 1 \\ -2 \end{pmatrix} $$

$$ x(t) = c_{1} e^{21 t} + c_{2} e^{-39 t}, \qquad y(t) = c_{1} e^{21 t} - 2 c_{2} e^{-39 t} $$

#### The decoupling transformation

In the original variables $\mathbf x = (x, y)^T$ the new coordinates are $\mathbf z = Q^{-1}\mathbf x$:

$$ z_1 = \frac{2 x}{3} + \frac{y}{3}, \qquad z_2 = \frac{x}{3} - \frac{y}{3} $$

#### Phase portrait

$\lambda_1 = 21$ and $\lambda_2 = -39$ are of opposite signs: the origin is a **saddle** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{21t}$ and $z_2 = c_2e^{-39t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{- \frac{13}{7}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = - \frac{13}{7}$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through $(1, -2)$ (the **stable manifold**), reach the origin as $t \to +\infty$; the line through $(1, 1)$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, -2)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 21\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = -39\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e9-iv-z.svg]]
*Canonical $\mathbf z$-plane (saddle): invariant axes and orbits $z_2 = K|z_1|^{- \frac{13}{7}}$.*

![[attachments/AM-PS/ch4a-e9-iv-x.svg]]
*Original $(x, y)$-plane (saddle): dashed lines are the eigenlines $\mathbf v_1 = (1, 1)$ and $\mathbf v_2 = (1, -2)$.*

## Phase 4: Interpretation and checks

- Each $Q^{-1}AQ$ was multiplied out entry by entry above and equals $\Lambda$ exactly; the eigenvalues satisfy $\lambda_1 + \lambda_2 = \operatorname{tr}A$ and $\lambda_1\lambda_2 = \det A$.
- (i) $15$ and $-6$: saddle; (ii) $2$ and $-3$ (lower-triangular matrix: the eigenvalues are the diagonal entries): saddle; (iii) $10$ and $5$: unstable node, tangent at the origin to the eigenvector of $5$; (iv) $21$ and $-39$: saddle with very different rates.
- (i) is the homogeneous part of Exercise 7(vii) and (ii) shows that for a triangular matrix the eigenvalues can be read off the diagonal (Topic 4 Examples 27.2 and 27.3).
- The change of coordinates is not the efficient way to solve the system (the general solution follows directly from the eigenpairs), but it is what justifies the portrait: it reduces every case to the uncoupled one (Robinson Sec. 28.2).
- Dimensional check: with $t$ in seconds the eigenvalues have units s$^{-1}$, and $Q$ is dimensionless (it mixes coordinates of equal units).
