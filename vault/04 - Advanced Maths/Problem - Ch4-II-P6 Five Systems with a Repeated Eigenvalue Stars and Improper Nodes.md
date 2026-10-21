---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 6"
dificultad: media
id: "e6"
pill: "Repeated Eigenvalue • Jordan Chain • Stars and Improper Nodes"
tags:
  - problema-resuelto
  - autovalor-repetido
  - nodo-impropio
  - cadena-de-jordan
---

# Problem 4.II.6: Five Systems with a Repeated Eigenvalue: Stars and Improper Nodes

> Official exercise 6 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Find the eigenvalues and eigenvectors of the matrices occurring in the following equations, and draw the phase portrait. Find also the coordinate transformation that will put the equation into canonical form and show that this works. Write down the general solution.

- (i) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 5 & -4 \\ 1 & 1 \end{pmatrix}\mathbf x$;
- (ii) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} -6 & 2 \\ -2 & -2 \end{pmatrix}\mathbf x$;
- (iii) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} -3 & -1 \\ 1 & -5 \end{pmatrix}\mathbf x$;
- (iv) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 13 & 0 \\ 0 & 13 \end{pmatrix}\mathbf x$;
- (v) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 7 & -4 \\ 1 & 3 \end{pmatrix}\mathbf x$.

## Phase 1: Setup

For every matrix the discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A$ is zero (checked in each item), so there is one repeated eigenvalue $\lambda = \tfrac12\operatorname{tr}A$ with algebraic multiplicity $m_a = 2$. The geometric multiplicity $m_g = \dim\ker(A - \lambda I)$ is $2$ iff $A = \lambda I$ (a **star**) and $1$ otherwise (an **improper node** with a Jordan chain), Topic 4 Sec. 8.2 to 8.4. The canonical form is $J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, $(A - \lambda I)\mathbf v_2 = \mathbf v_1$; for a star there is nothing to transform.

## Phase 2: Formulation

Algorithm (Topic 4 Sec. 8.10): $\lambda = \tfrac12\operatorname{tr}A$; $N = A - \lambda I$; if $N = O$ star, $\mathbf x = e^{\lambda t}\mathbf x_0$; otherwise $\mathbf v_1 \in \ker N$, solve $N\mathbf v_2 = \mathbf v_1$, $Q = [\mathbf v_1 \mid \mathbf v_2]$, $\mathbf z = Q^{-1}\mathbf x$, $z_1 = (c_1 + c_2t)e^{\lambda t}$, $z_2 = c_2e^{\lambda t}$, $\mathbf x = Q\mathbf z$.

## Phase 3: Derivation

### (i) $A = \begin{pmatrix} 5 & -4 \\ 1 & 1 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 5 - \lambda & -4 \\ 1 & 1 - \lambda \end{vmatrix} = (5 - \lambda)(1 - \lambda) - (-4)(1) $$

$$ = \lambda^2 - (5 + 1)\lambda + (5\cdot1 - (-4)\cdot1) = \lambda^2 - (6)\lambda + (9) = \lambda^{2} - 6 \lambda + 9 $$

$\operatorname{tr}A = 6$, $\det A = 9$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 36 - 36 = 0$.

$\Delta = 0$: the characteristic polynomial is a perfect square, $(\lambda - 3)^2 = \lambda^{2} - 6 \lambda + 9$, so

$$ \lambda_1 = \lambda_2 = \lambda = \tfrac12\operatorname{tr}A = 3 \quad (m_a = 2) $$

Geometric multiplicity: $N = A - \lambda I = \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix}$.

$N \neq O$ and $\det N = (2)(-2) - (-4)(1) = 0$, so $N$ has rank 1: $m_g = 1$ and there is a single eigendirection (improper node). By Cayley-Hamilton $N^2 = O$ (Topic 4, Sec. 8.4):

$$ \begin{aligned} (N^2)_{11} &= 2\cdot2 + (-4)\cdot1 = 0 \\ (N^2)_{12} &= 2\cdot(-4) + (-4)\cdot(-2) = 0 \\ (N^2)_{21} &= 1\cdot2 + (-2)\cdot1 = 0 \\ (N^2)_{22} &= 1\cdot(-4) + (-2)\cdot(-2) = 0 \end{aligned} $$

#### Eigenvector

For $\lambda = 3$: $(A - (3)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 2v_1 - 4v_2 = 0\quad (\text{row 1}) \\ 1v_1 - 2v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $\frac{1}{2}$ times row 1) and express a single condition. Row 1 reads $2v_1 + (-4)v_2 = 0$, so $v_1 = 2\,v_2$: every eigenvector is a multiple of $(2, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} 6 \\ 3 \end{pmatrix} = 3\mathbf{v_1}$.

#### Generalised eigenvector

Solve $(A - \lambda I)\mathbf v_2 = \mathbf v_1$, i.e. $N\mathbf v_2 = \mathbf v_1$ (Eq. 8.2). The system is solvable because $\operatorname{im}N = \ker N$ (Sec. 8.4):

$$ \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} p \\ q \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} $$

$$ \begin{aligned} 2p - 4q &= 2 \\ 1p - 2q &= 1 \end{aligned} $$

The two equations are proportional (the right-hand sides are in the same ratio as the rows, because $\mathbf v_1 \in \operatorname{im}N$), so one is enough. The solution is not unique: $\mathbf v_2 + s\mathbf v_1$ also works for every $s$, because $N\mathbf v_1 = \mathbf 0$.

Take $q = 0$. Row 1 gives $2p = 2$, so $p = 1$:

$$ \mathbf v_2 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} $$

Check: $N\mathbf v_2 = \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \mathbf v_1$, equivalently $A\mathbf v_2 = \lambda\mathbf v_2 + \mathbf v_1 = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$ (Eq. 8.2).

#### Change of coordinates

$$ Q = [\mathbf v_1 \mid \mathbf v_2] = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix} $$

$\det Q = (2)(0) - (1)(1) = -1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-1}\begin{pmatrix} 0 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & -2 \end{pmatrix} $$

$$ A\mathbf v_1 = \begin{pmatrix} 6 \\ 3 \end{pmatrix} = 3\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 5 \\ 1 \end{pmatrix} = \mathbf v_1 + 3\mathbf v_2 $$

$$ AQ = \begin{pmatrix} 6 & 5 \\ 3 & 1 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 0\cdot6 + 1\cdot3 = 3 \\ (Q^{-1}AQ)_{12} &= 0\cdot5 + 1\cdot1 = 1 \\ (Q^{-1}AQ)_{21} &= 1\cdot6 + (-2)\cdot3 = 0 \\ (Q^{-1}AQ)_{22} &= 1\cdot5 + (-2)\cdot1 = 3 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix} = J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = 3z_1 + z_2, \qquad \dot z_2 = 3z_2 $$

Second equation: $\frac{d}{dt}(e^{-\lambda t}z_2) = e^{-\lambda t}(\dot z_2 - \lambda z_2) = 0$, so $e^{-\lambda t}z_2$ is constant: $z_2 = c_2 e^{3t}$. First equation with this $z_2$: $\dot z_1 - \lambda z_1 = c_2 e^{3t}$. The integrating factor is $e^{-\lambda t}$: by the product rule $\frac{d}{dt}(e^{-\lambda t}z_1) = e^{-\lambda t}(\dot z_1 - \lambda z_1) = c_2$. Barrow's rule between $0$ and $t$:

$$ \left[e^{-\lambda s}z_1(s)\right]_{s=0}^{s=t} = \int_0^t c_2\,ds = c_2 t \;\Longrightarrow\; e^{-\lambda t}z_1(t) - z_1(0) = c_2 t $$

$$ z_1(t) = (c_1 + c_2 t)e^{3t}, \qquad z_2(t) = c_2 e^{3t} \qquad (c_1 = z_1(0),\ c_2 = z_2(0)) $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, hence (Topic 4, Eq. 8.5)

$$ \mathbf x(t) = e^{3t}\left[c_1\begin{pmatrix} 2 \\ 1 \end{pmatrix} + c_2\left(t\begin{pmatrix} 2 \\ 1 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix}\right)\right] $$

$$ x(t) = 2 c_{1} e^{3 t} + 2 c_{2} t e^{3 t} + c_{2} e^{3 t}, \qquad y(t) = c_{1} e^{3 t} + c_{2} t e^{3 t} $$

#### Phase portrait

$\lambda = 3$ is repeated with a single eigendirection and $A \neq \lambda I$: the origin is an **unstable improper node** (Topic 4 Sec. 8.8 and 8.9). In the $\mathbf z$-plane the $z_1$-axis is invariant ($z_2 \equiv 0$, $z_1 = c_1e^{3t}$, arrows away from the origin); the other orbits satisfy $z_1 = z_2\left[K + \frac{1}{\lambda}\ln|z_2|\right]$, are S-shaped, tangent to the $z_1$-axis at the origin and parallel to it far away. Since $\dot z_1 = \lambda z_1 + z_2 = z_2$ on the $z_2$-axis, orbits cross it moving to the right in the upper half-plane and to the left in the lower one.

Orientation in the $\mathbf x$-plane, from $N\mathbf x = (A - \lambda I)\mathbf x = z_2\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = \begin{pmatrix} -4 \\ -2 \end{pmatrix} = -2\,\mathbf v_1$, so there the orbit drifts along $-\mathbf v_1$. The orbits are tangent to the eigenline at the origin and bend into an S around it.

![[attachments/AM-PS/ch4b-e6-i-z.svg]]
*Canonical $\mathbf z$-plane (unstable improper node).*

![[attachments/AM-PS/ch4b-e6-i-x.svg]]
*Original $(x, y)$-plane (unstable improper node); dashed: the eigenline with $\mathbf v_1 = (2, 1)$.*

### (ii) $A = \begin{pmatrix} -6 & 2 \\ -2 & -2 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} -6 - \lambda & 2 \\ -2 & -2 - \lambda \end{vmatrix} = (-6 - \lambda)(-2 - \lambda) - (2)(-2) $$

$$ = \lambda^2 - (-6 + (-2))\lambda + (-6\cdot(-2) - 2\cdot(-2)) = \lambda^2 - (-8)\lambda + (16) = \lambda^{2} + 8 \lambda + 16 $$

$\operatorname{tr}A = -8$, $\det A = 16$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 64 - 64 = 0$.

$\Delta = 0$: the characteristic polynomial is a perfect square, $(\lambda + 4)^2 = \lambda^{2} + 8 \lambda + 16$, so

$$ \lambda_1 = \lambda_2 = \lambda = \tfrac12\operatorname{tr}A = -4 \quad (m_a = 2) $$

Geometric multiplicity: $N = A - \lambda I = \begin{pmatrix} -2 & 2 \\ -2 & 2 \end{pmatrix}$.

$N \neq O$ and $\det N = (-2)(2) - (2)(-2) = 0$, so $N$ has rank 1: $m_g = 1$ and there is a single eigendirection (improper node). By Cayley-Hamilton $N^2 = O$ (Topic 4, Sec. 8.4):

$$ \begin{aligned} (N^2)_{11} &= (-2)\cdot(-2) + 2\cdot(-2) = 0 \\ (N^2)_{12} &= (-2)\cdot2 + 2\cdot2 = 0 \\ (N^2)_{21} &= (-2)\cdot(-2) + 2\cdot(-2) = 0 \\ (N^2)_{22} &= (-2)\cdot2 + 2\cdot2 = 0 \end{aligned} $$

#### Eigenvector

For $\lambda = -4$: $(A - (-4)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} -2 & 2 \\ -2 & 2 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} -2v_1 + 2v_2 = 0\quad (\text{row 1}) \\ -2v_1 + 2v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 is identical to row 1) and express a single condition. Row 1 reads $-2v_1 + 2v_2 = 0$, so $v_1 = v_2$: every eigenvector is a multiple of $(1, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} -4 \\ -4 \end{pmatrix} = -4\mathbf{v_1}$.

#### Generalised eigenvector

Solve $(A - \lambda I)\mathbf v_2 = \mathbf v_1$, i.e. $N\mathbf v_2 = \mathbf v_1$ (Eq. 8.2). The system is solvable because $\operatorname{im}N = \ker N$ (Sec. 8.4):

$$ \begin{pmatrix} -2 & 2 \\ -2 & 2 \end{pmatrix}\begin{pmatrix} p \\ q \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

$$ \begin{aligned} -2p + 2q &= 1 \\ -2p + 2q &= 1 \end{aligned} $$

The two equations are proportional (the right-hand sides are in the same ratio as the rows, because $\mathbf v_1 \in \operatorname{im}N$), so one is enough. The solution is not unique: $\mathbf v_2 + s\mathbf v_1$ also works for every $s$, because $N\mathbf v_1 = \mathbf 0$.

Take $p = 0$. Row 1 gives $2q = 1$, so $q = \frac{1}{2}$:

$$ \mathbf v_2 = \begin{pmatrix} 0 \\ \frac{1}{2} \end{pmatrix} $$

Check: $N\mathbf v_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \mathbf v_1$, equivalently $A\mathbf v_2 = \lambda\mathbf v_2 + \mathbf v_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ (Eq. 8.2).

#### Change of coordinates

$$ Q = [\mathbf v_1 \mid \mathbf v_2] = \begin{pmatrix} 1 & 0 \\ 1 & \frac{1}{2} \end{pmatrix} $$

$\det Q = (1)(\frac{1}{2}) - (0)(1) = \frac{1}{2}$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{\frac{1}{2}}\begin{pmatrix} \frac{1}{2} & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ -2 & 2 \end{pmatrix} $$

$$ A\mathbf v_1 = \begin{pmatrix} -4 \\ -4 \end{pmatrix} = (-4)\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \mathbf v_1 + (-4)\mathbf v_2 $$

$$ AQ = \begin{pmatrix} -4 & 1 \\ -4 & -1 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 1\cdot(-4) + 0\cdot(-4) = -4 \\ (Q^{-1}AQ)_{12} &= 1\cdot1 + 0\cdot(-1) = 1 \\ (Q^{-1}AQ)_{21} &= (-2)\cdot(-4) + 2\cdot(-4) = 0 \\ (Q^{-1}AQ)_{22} &= (-2)\cdot1 + 2\cdot(-1) = -4 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -4 & 1 \\ 0 & -4 \end{pmatrix} = J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = -4z_1 + z_2, \qquad \dot z_2 = -4z_2 $$

Second equation: $\frac{d}{dt}(e^{-\lambda t}z_2) = e^{-\lambda t}(\dot z_2 - \lambda z_2) = 0$, so $e^{-\lambda t}z_2$ is constant: $z_2 = c_2 e^{-4t}$. First equation with this $z_2$: $\dot z_1 - \lambda z_1 = c_2 e^{-4t}$. The integrating factor is $e^{-\lambda t}$: by the product rule $\frac{d}{dt}(e^{-\lambda t}z_1) = e^{-\lambda t}(\dot z_1 - \lambda z_1) = c_2$. Barrow's rule between $0$ and $t$:

$$ \left[e^{-\lambda s}z_1(s)\right]_{s=0}^{s=t} = \int_0^t c_2\,ds = c_2 t \;\Longrightarrow\; e^{-\lambda t}z_1(t) - z_1(0) = c_2 t $$

$$ z_1(t) = (c_1 + c_2 t)e^{-4t}, \qquad z_2(t) = c_2 e^{-4t} \qquad (c_1 = z_1(0),\ c_2 = z_2(0)) $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, hence (Topic 4, Eq. 8.5)

$$ \mathbf x(t) = e^{-4t}\left[c_1\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2\left(t\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 0 \\ \frac{1}{2} \end{pmatrix}\right)\right] $$

$$ x(t) = c_{1} e^{-4 t} + c_{2} t e^{-4 t}, \qquad y(t) = c_{1} e^{-4 t} + c_{2} t e^{-4 t} + \frac{c_{2} e^{-4 t}}{2} $$

#### Phase portrait

$\lambda = -4$ is repeated with a single eigendirection and $A \neq \lambda I$: the origin is an **stable improper node** (Topic 4 Sec. 8.8 and 8.9). In the $\mathbf z$-plane the $z_1$-axis is invariant ($z_2 \equiv 0$, $z_1 = c_1e^{-4t}$, arrows towards the origin); the other orbits satisfy $z_1 = z_2\left[K + \frac{1}{\lambda}\ln|z_2|\right]$, are S-shaped, tangent to the $z_1$-axis at the origin and parallel to it far away. Since $\dot z_1 = \lambda z_1 + z_2 = z_2$ on the $z_2$-axis, orbits cross it moving to the right in the upper half-plane and to the left in the lower one.

Orientation in the $\mathbf x$-plane, from $N\mathbf x = (A - \lambda I)\mathbf x = z_2\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = \begin{pmatrix} 2 \\ 2 \end{pmatrix} = 2\,\mathbf v_1$, so there the orbit drifts along $+\mathbf v_1$. The orbits are tangent to the eigenline at the origin and bend into an S around it.

![[attachments/AM-PS/ch4b-e6-ii-z.svg]]
*Canonical $\mathbf z$-plane (stable improper node).*

![[attachments/AM-PS/ch4b-e6-ii-x.svg]]
*Original $(x, y)$-plane (stable improper node); dashed: the eigenline with $\mathbf v_1 = (1, 1)$.*

### (iii) $A = \begin{pmatrix} -3 & -1 \\ 1 & -5 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} -3 - \lambda & -1 \\ 1 & -5 - \lambda \end{vmatrix} = (-3 - \lambda)(-5 - \lambda) - (-1)(1) $$

$$ = \lambda^2 - (-3 + (-5))\lambda + (-3\cdot(-5) - (-1)\cdot1) = \lambda^2 - (-8)\lambda + (16) = \lambda^{2} + 8 \lambda + 16 $$

$\operatorname{tr}A = -8$, $\det A = 16$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 64 - 64 = 0$.

$\Delta = 0$: the characteristic polynomial is a perfect square, $(\lambda + 4)^2 = \lambda^{2} + 8 \lambda + 16$, so

$$ \lambda_1 = \lambda_2 = \lambda = \tfrac12\operatorname{tr}A = -4 \quad (m_a = 2) $$

Geometric multiplicity: $N = A - \lambda I = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}$.

$N \neq O$ and $\det N = (1)(-1) - (-1)(1) = 0$, so $N$ has rank 1: $m_g = 1$ and there is a single eigendirection (improper node). By Cayley-Hamilton $N^2 = O$ (Topic 4, Sec. 8.4):

$$ \begin{aligned} (N^2)_{11} &= 1\cdot1 + (-1)\cdot1 = 0 \\ (N^2)_{12} &= 1\cdot(-1) + (-1)\cdot(-1) = 0 \\ (N^2)_{21} &= 1\cdot1 + (-1)\cdot1 = 0 \\ (N^2)_{22} &= 1\cdot(-1) + (-1)\cdot(-1) = 0 \end{aligned} $$

#### Eigenvector

For $\lambda = -4$: $(A - (-4)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 1v_1 - 1v_2 = 0\quad (\text{row 1}) \\ 1v_1 - 1v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 is identical to row 1) and express a single condition. Row 1 reads $1v_1 + (-1)v_2 = 0$, so $v_1 = v_2$: every eigenvector is a multiple of $(1, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} -4 \\ -4 \end{pmatrix} = -4\mathbf{v_1}$.

#### Generalised eigenvector

Solve $(A - \lambda I)\mathbf v_2 = \mathbf v_1$, i.e. $N\mathbf v_2 = \mathbf v_1$ (Eq. 8.2). The system is solvable because $\operatorname{im}N = \ker N$ (Sec. 8.4):

$$ \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} p \\ q \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

$$ \begin{aligned} 1p - 1q &= 1 \\ 1p - 1q &= 1 \end{aligned} $$

The two equations are proportional (the right-hand sides are in the same ratio as the rows, because $\mathbf v_1 \in \operatorname{im}N$), so one is enough. The solution is not unique: $\mathbf v_2 + s\mathbf v_1$ also works for every $s$, because $N\mathbf v_1 = \mathbf 0$.

Take $p = 0$. Row 1 gives $-1q = 1$, so $q = -1$:

$$ \mathbf v_2 = \begin{pmatrix} 0 \\ -1 \end{pmatrix} $$

Check: $N\mathbf v_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \mathbf v_1$, equivalently $A\mathbf v_2 = \lambda\mathbf v_2 + \mathbf v_1 = \begin{pmatrix} 1 \\ 5 \end{pmatrix}$ (Eq. 8.2).

#### Change of coordinates

$$ Q = [\mathbf v_1 \mid \mathbf v_2] = \begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix} $$

$\det Q = (1)(-1) - (0)(1) = -1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-1}\begin{pmatrix} -1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix} $$

$$ A\mathbf v_1 = \begin{pmatrix} -4 \\ -4 \end{pmatrix} = (-4)\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 1 \\ 5 \end{pmatrix} = \mathbf v_1 + (-4)\mathbf v_2 $$

$$ AQ = \begin{pmatrix} -4 & 1 \\ -4 & 5 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 1\cdot(-4) + 0\cdot(-4) = -4 \\ (Q^{-1}AQ)_{12} &= 1\cdot1 + 0\cdot5 = 1 \\ (Q^{-1}AQ)_{21} &= 1\cdot(-4) + (-1)\cdot(-4) = 0 \\ (Q^{-1}AQ)_{22} &= 1\cdot1 + (-1)\cdot5 = -4 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -4 & 1 \\ 0 & -4 \end{pmatrix} = J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = -4z_1 + z_2, \qquad \dot z_2 = -4z_2 $$

Second equation: $\frac{d}{dt}(e^{-\lambda t}z_2) = e^{-\lambda t}(\dot z_2 - \lambda z_2) = 0$, so $e^{-\lambda t}z_2$ is constant: $z_2 = c_2 e^{-4t}$. First equation with this $z_2$: $\dot z_1 - \lambda z_1 = c_2 e^{-4t}$. The integrating factor is $e^{-\lambda t}$: by the product rule $\frac{d}{dt}(e^{-\lambda t}z_1) = e^{-\lambda t}(\dot z_1 - \lambda z_1) = c_2$. Barrow's rule between $0$ and $t$:

$$ \left[e^{-\lambda s}z_1(s)\right]_{s=0}^{s=t} = \int_0^t c_2\,ds = c_2 t \;\Longrightarrow\; e^{-\lambda t}z_1(t) - z_1(0) = c_2 t $$

$$ z_1(t) = (c_1 + c_2 t)e^{-4t}, \qquad z_2(t) = c_2 e^{-4t} \qquad (c_1 = z_1(0),\ c_2 = z_2(0)) $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, hence (Topic 4, Eq. 8.5)

$$ \mathbf x(t) = e^{-4t}\left[c_1\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2\left(t\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 0 \\ -1 \end{pmatrix}\right)\right] $$

$$ x(t) = c_{1} e^{-4 t} + c_{2} t e^{-4 t}, \qquad y(t) = c_{1} e^{-4 t} + c_{2} t e^{-4 t} - c_{2} e^{-4 t} $$

#### Phase portrait

$\lambda = -4$ is repeated with a single eigendirection and $A \neq \lambda I$: the origin is an **stable improper node** (Topic 4 Sec. 8.8 and 8.9). In the $\mathbf z$-plane the $z_1$-axis is invariant ($z_2 \equiv 0$, $z_1 = c_1e^{-4t}$, arrows towards the origin); the other orbits satisfy $z_1 = z_2\left[K + \frac{1}{\lambda}\ln|z_2|\right]$, are S-shaped, tangent to the $z_1$-axis at the origin and parallel to it far away. Since $\dot z_1 = \lambda z_1 + z_2 = z_2$ on the $z_2$-axis, orbits cross it moving to the right in the upper half-plane and to the left in the lower one.

Orientation in the $\mathbf x$-plane, from $N\mathbf x = (A - \lambda I)\mathbf x = z_2\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = \begin{pmatrix} -1 \\ -1 \end{pmatrix} = -1\,\mathbf v_1$, so there the orbit drifts along $-\mathbf v_1$. The orbits are tangent to the eigenline at the origin and bend into an S around it.

![[attachments/AM-PS/ch4b-e6-iii-z.svg]]
*Canonical $\mathbf z$-plane (stable improper node).*

![[attachments/AM-PS/ch4b-e6-iii-x.svg]]
*Original $(x, y)$-plane (stable improper node); dashed: the eigenline with $\mathbf v_1 = (1, 1)$.*

### (iv) $A = \begin{pmatrix} 13 & 0 \\ 0 & 13 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 13 - \lambda & 0 \\ 0 & 13 - \lambda \end{vmatrix} = (13 - \lambda)(13 - \lambda) - (0)(0) $$

$$ = \lambda^2 - (13 + 13)\lambda + (13\cdot13 - 0\cdot0) = \lambda^2 - (26)\lambda + (169) = \lambda^{2} - 26 \lambda + 169 $$

$\operatorname{tr}A = 26$, $\det A = 169$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 676 - 676 = 0$.

$\Delta = 0$: the characteristic polynomial is a perfect square, $(\lambda - 13)^2 = \lambda^{2} - 26 \lambda + 169$, so

$$ \lambda_1 = \lambda_2 = \lambda = \tfrac12\operatorname{tr}A = 13 \quad (m_a = 2) $$

Geometric multiplicity: $N = A - \lambda I = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.

$N = O$: every vector is an eigenvector ($m_g = 2$) and $A = \lambda I$ (Topic 4, Sec. 8.3). The system is already uncoupled in every basis.

$$ \dot x = 13x, \qquad \dot y = 13y $$

Each equation is separable, $\frac{d}{dt}(e^{-\lambda t}x_i) = 0$, so $x_i = c_i e^{13t}$ and

$$ \mathbf x(t) = e^{13t}\mathbf x_0 = c_1 e^{13t}\begin{pmatrix} 1 \\ 0 \end{pmatrix} + c_2 e^{13t}\begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

#### Phase portrait

$A = 13I$: every line through the origin is invariant and every solution moves along its own ray, $\mathbf x(t) = e^{13t}\mathbf x_0$, away from the origin (the origin is a **unstable star**). The picture is the same in every basis, so there is no separate canonical plane.

![[attachments/AM-PS/ch4b-e6-iv-x.svg]]
*Unstable star: straight rays out of the origin.*

### (v) $A = \begin{pmatrix} 7 & -4 \\ 1 & 3 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 7 - \lambda & -4 \\ 1 & 3 - \lambda \end{vmatrix} = (7 - \lambda)(3 - \lambda) - (-4)(1) $$

$$ = \lambda^2 - (7 + 3)\lambda + (7\cdot3 - (-4)\cdot1) = \lambda^2 - (10)\lambda + (25) = \lambda^{2} - 10 \lambda + 25 $$

$\operatorname{tr}A = 10$, $\det A = 25$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 100 - 100 = 0$.

$\Delta = 0$: the characteristic polynomial is a perfect square, $(\lambda - 5)^2 = \lambda^{2} - 10 \lambda + 25$, so

$$ \lambda_1 = \lambda_2 = \lambda = \tfrac12\operatorname{tr}A = 5 \quad (m_a = 2) $$

Geometric multiplicity: $N = A - \lambda I = \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix}$.

$N \neq O$ and $\det N = (2)(-2) - (-4)(1) = 0$, so $N$ has rank 1: $m_g = 1$ and there is a single eigendirection (improper node). By Cayley-Hamilton $N^2 = O$ (Topic 4, Sec. 8.4):

$$ \begin{aligned} (N^2)_{11} &= 2\cdot2 + (-4)\cdot1 = 0 \\ (N^2)_{12} &= 2\cdot(-4) + (-4)\cdot(-2) = 0 \\ (N^2)_{21} &= 1\cdot2 + (-2)\cdot1 = 0 \\ (N^2)_{22} &= 1\cdot(-4) + (-2)\cdot(-2) = 0 \end{aligned} $$

#### Eigenvector

For $\lambda = 5$: $(A - (5)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 2v_1 - 4v_2 = 0\quad (\text{row 1}) \\ 1v_1 - 2v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $\frac{1}{2}$ times row 1) and express a single condition. Row 1 reads $2v_1 + (-4)v_2 = 0$, so $v_1 = 2\,v_2$: every eigenvector is a multiple of $(2, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} 10 \\ 5 \end{pmatrix} = 5\mathbf{v_1}$.

#### Generalised eigenvector

Solve $(A - \lambda I)\mathbf v_2 = \mathbf v_1$, i.e. $N\mathbf v_2 = \mathbf v_1$ (Eq. 8.2). The system is solvable because $\operatorname{im}N = \ker N$ (Sec. 8.4):

$$ \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} p \\ q \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} $$

$$ \begin{aligned} 2p - 4q &= 2 \\ 1p - 2q &= 1 \end{aligned} $$

The two equations are proportional (the right-hand sides are in the same ratio as the rows, because $\mathbf v_1 \in \operatorname{im}N$), so one is enough. The solution is not unique: $\mathbf v_2 + s\mathbf v_1$ also works for every $s$, because $N\mathbf v_1 = \mathbf 0$.

Take $q = 0$. Row 1 gives $2p = 2$, so $p = 1$:

$$ \mathbf v_2 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} $$

Check: $N\mathbf v_2 = \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \mathbf v_1$, equivalently $A\mathbf v_2 = \lambda\mathbf v_2 + \mathbf v_1 = \begin{pmatrix} 7 \\ 1 \end{pmatrix}$ (Eq. 8.2).

#### Change of coordinates

$$ Q = [\mathbf v_1 \mid \mathbf v_2] = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix} $$

$\det Q = (2)(0) - (1)(1) = -1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-1}\begin{pmatrix} 0 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & -2 \end{pmatrix} $$

$$ A\mathbf v_1 = \begin{pmatrix} 10 \\ 5 \end{pmatrix} = 5\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 7 \\ 1 \end{pmatrix} = \mathbf v_1 + 5\mathbf v_2 $$

$$ AQ = \begin{pmatrix} 10 & 7 \\ 5 & 1 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 0\cdot10 + 1\cdot5 = 5 \\ (Q^{-1}AQ)_{12} &= 0\cdot7 + 1\cdot1 = 1 \\ (Q^{-1}AQ)_{21} &= 1\cdot10 + (-2)\cdot5 = 0 \\ (Q^{-1}AQ)_{22} &= 1\cdot7 + (-2)\cdot1 = 5 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 5 & 1 \\ 0 & 5 \end{pmatrix} = J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = 5z_1 + z_2, \qquad \dot z_2 = 5z_2 $$

Second equation: $\frac{d}{dt}(e^{-\lambda t}z_2) = e^{-\lambda t}(\dot z_2 - \lambda z_2) = 0$, so $e^{-\lambda t}z_2$ is constant: $z_2 = c_2 e^{5t}$. First equation with this $z_2$: $\dot z_1 - \lambda z_1 = c_2 e^{5t}$. The integrating factor is $e^{-\lambda t}$: by the product rule $\frac{d}{dt}(e^{-\lambda t}z_1) = e^{-\lambda t}(\dot z_1 - \lambda z_1) = c_2$. Barrow's rule between $0$ and $t$:

$$ \left[e^{-\lambda s}z_1(s)\right]_{s=0}^{s=t} = \int_0^t c_2\,ds = c_2 t \;\Longrightarrow\; e^{-\lambda t}z_1(t) - z_1(0) = c_2 t $$

$$ z_1(t) = (c_1 + c_2 t)e^{5t}, \qquad z_2(t) = c_2 e^{5t} \qquad (c_1 = z_1(0),\ c_2 = z_2(0)) $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, hence (Topic 4, Eq. 8.5)

$$ \mathbf x(t) = e^{5t}\left[c_1\begin{pmatrix} 2 \\ 1 \end{pmatrix} + c_2\left(t\begin{pmatrix} 2 \\ 1 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix}\right)\right] $$

$$ x(t) = 2 c_{1} e^{5 t} + 2 c_{2} t e^{5 t} + c_{2} e^{5 t}, \qquad y(t) = c_{1} e^{5 t} + c_{2} t e^{5 t} $$

#### Phase portrait

$\lambda = 5$ is repeated with a single eigendirection and $A \neq \lambda I$: the origin is an **unstable improper node** (Topic 4 Sec. 8.8 and 8.9). In the $\mathbf z$-plane the $z_1$-axis is invariant ($z_2 \equiv 0$, $z_1 = c_1e^{5t}$, arrows away from the origin); the other orbits satisfy $z_1 = z_2\left[K + \frac{1}{\lambda}\ln|z_2|\right]$, are S-shaped, tangent to the $z_1$-axis at the origin and parallel to it far away. Since $\dot z_1 = \lambda z_1 + z_2 = z_2$ on the $z_2$-axis, orbits cross it moving to the right in the upper half-plane and to the left in the lower one.

Orientation in the $\mathbf x$-plane, from $N\mathbf x = (A - \lambda I)\mathbf x = z_2\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = \begin{pmatrix} -4 \\ -2 \end{pmatrix} = -2\,\mathbf v_1$, so there the orbit drifts along $-\mathbf v_1$. The orbits are tangent to the eigenline at the origin and bend into an S around it.

![[attachments/AM-PS/ch4b-e6-v-z.svg]]
*Canonical $\mathbf z$-plane (unstable improper node).*

![[attachments/AM-PS/ch4b-e6-v-x.svg]]
*Original $(x, y)$-plane (unstable improper node); dashed: the eigenline with $\mathbf v_1 = (2, 1)$.*

## Phase 4: Interpretation and checks

| Item | $\lambda$ | Type |
| :--- | :--- | :--- |
| (i) | $3$ | unstable improper node |
| (ii) | $-4$ | stable improper node |
| (iii) | $-4$ | stable improper node |
| (iv) | $13$ | unstable star |
| (v) | $5$ | unstable improper node |

- (i) is exactly the worked Example 8.2 of Topic 4 (Robinson Example 30.1): $\lambda = 3$, $\mathbf v_1 = (2, 1)^T$, $\mathbf v_2 = (1, 0)^T$ and $J = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$ — the result reproduces it step by step.
- In each improper node $Q^{-1}AQ = J$ was multiplied out entry by entry; $N^2 = O$ was checked (Cayley-Hamilton).
- The general solution $\mathbf x = e^{\lambda t}[c_1\mathbf v_1 + c_2(t\mathbf v_1 + \mathbf v_2)]$ contains the secular term $te^{\lambda t}\mathbf v_1$, which makes all orbits tangent to $\mathbf v_1$ at both ends (S-shaped).
- (iv) is a multiple of the identity: every vector is an eigenvector and the orbits are rays; the canonical form is $A$ itself, and any basis (for instance $Q = I$) works.
- A repeated eigenvalue is a borderline case between nodes ($\Delta > 0$) and spirals ($\Delta < 0$).
