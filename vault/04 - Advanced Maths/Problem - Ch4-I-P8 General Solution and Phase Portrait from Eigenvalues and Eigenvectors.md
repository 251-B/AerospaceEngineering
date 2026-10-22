---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 8"
dificultad: media
id: "e8"
pill: "Eigen-data • Nodes and Saddles • Eight Portraits"
tags:
  - problema-resuelto
  - retrato-de-fase
  - nodos
  - puntos-silla
  - autovalores-reales
---

# Problem 4.I.8: General Solution and Phase Portrait from Eigenvalues and Eigenvectors

> Official exercise 8 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Write down the general solution and draw the phase portrait for the equation $\dot{\mathbf x} = A\mathbf x$, when the eigenvalues and eigenvectors of $A$ are as given in each case. You should take particular care with stable (or unstable) nodes to ensure that the trajectories approach (or move away from) the origin tangent to the correct eigenvector.

- (i) $\lambda_1 = 1$, $\mathbf v_1 = (1, 1)$ and $\lambda_2 = 2$, $\mathbf v_2 = (1, -1)$;
- (ii) $\lambda_1 = 1$, $\mathbf v_1 = (1, 0)$ and $\lambda_2 = -2$, $\mathbf v_2 = (1, 1)$;
- (iii) $\lambda_1 = -2$, $\mathbf v_1 = (1, 2)$ and $\lambda_2 = -3$, $\mathbf v_2 = (2, -3)$;
- (iv) $\lambda_1 = 3$, $\mathbf v_1 = (2, 3)$ and $\lambda_2 = -5$, $\mathbf v_2 = (0, 1)$;
- (v) $\lambda_1 = 3$, $\mathbf v_1 = (1, 2)$ and $\lambda_2 = 1$, $\mathbf v_2 = (1, -3)$;
- (vi) $\lambda_1 = 2$, $\mathbf v_1 = (0, 1)$ and $\lambda_2 = -3$, $\mathbf v_2 = (1, 5)$;
- (vii) $\lambda_1 = 1$, $\mathbf v_1 = (1, 1)$ and $\lambda_2 = 2$, $\mathbf v_2 = (2, 1)$;
- (viii) $\lambda_1 = -3$, $\mathbf v_1 = (1, 3)$ and $\lambda_2 = -1$, $\mathbf v_2 = (-3, 2)$;

## Phase 1: Setup and classification

In every item the two eigenvalues are real and distinct, with linearly independent eigenvectors (so $\det[\mathbf v_1\ \mathbf v_2] \neq 0$, checked in each item). The general solution is then $\mathbf x = c_1e^{\lambda_1t}\mathbf v_1 + c_2e^{\lambda_2t}\mathbf v_2$ (Robinson Eq. 28.1) and the portrait is determined by the signs of $\lambda_1, \lambda_2$ (Topic 4 Sec. 6 and 9):

| Signs | Origin | Behaviour |
| :--- | :--- | :--- |
| $\lambda_1, \lambda_2 < 0$ | stable node | all orbits tend to $\mathbf 0$, tangent to the eigenvector of the smaller $\vert \lambda\vert $ |
| $\lambda_1, \lambda_2 > 0$ | unstable node | all orbits leave $\mathbf 0$, tangent to the eigenvector of the smaller $\vert \lambda\vert $ |
| $\lambda_1\lambda_2 < 0$ | saddle | only the orbits on the stable eigenline reach $\mathbf 0$ |

| Item | $\lambda_1, \lambda_2$ | Type | Slow direction (smaller $\vert \lambda\vert $) |
| :--- | :--- | :--- | :--- |
| (i) | $1, 2$ | unstable node | $\mathbf v_1$ = $(1, 1)$ |
| (ii) | $1, -2$ | saddle | not applicable |
| (iii) | $-2, -3$ | stable node | $\mathbf v_1$ = $(1, 2)$ |
| (iv) | $3, -5$ | saddle | not applicable |
| (v) | $3, 1$ | unstable node | $\mathbf v_2$ = $(1, -3)$ |
| (vi) | $2, -3$ | saddle | not applicable |
| (vii) | $1, 2$ | unstable node | $\mathbf v_1$ = $(1, 1)$ |
| (viii) | $-3, -1$ | stable node | $\mathbf v_2$ = $(-3, 2)$ |

## Phase 2: Formulation: how each item is treated

For each item: (1) the general solution; (2) the matrix $A = Q\Lambda Q^{-1}$ reconstructed from the data, used to draw and to check; (3) the canonical system $\dot{\mathbf z} = \Lambda\mathbf z$ with $\mathbf z = Q^{-1}\mathbf x$ and its solution; (4) the portrait in the $\mathbf z$-plane and its image under $\mathbf x = Q\mathbf z$ in the $(x, y)$-plane, with the arrows and the tangent direction decided by the rules above.

> [!info] Method of the class notes [Notes, p. 9]
> Case 1 of the notes: $\mathbf x = C_1e^{\lambda_1t}\mathbf v_1 + C_2e^{\lambda_2t}\mathbf v_2$. With $P = (\mathbf v_1, \mathbf v_2)$ (the $Q$ of this page), $\mathbf z = P^{-1}\mathbf x$ gives $\dot{\mathbf z} = D\mathbf z$ and the orbits $z_2 = \tilde C z_1^{\lambda_2/\lambda_1}$. The table of the notes reads the portrait from $r = \lambda_2/\lambda_1$: eigenvalues of one sign give a node, tangent at the origin to the axis of the eigenvalue of smaller modulus ($z_1$-axis when $r > 1$, $z_2$-axis when $0 < r < 1$); opposite signs give a saddle. Back in $\mathbf x$ the $z$-axes become the eigenvector lines.

## Phase 3: Derivation of the eight portraits

### (i) $\lambda_1 = 1$, $\mathbf v_1 = (1, 1)^T$; $\lambda_2 = 2$, $\mathbf v_2 = (1, -1)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}, \qquad \det Q = -2, \qquad Q^{-1} = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & - \frac{1}{2} \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 1\cdot1 + 1\cdot0 = 1 \\ (Q\Lambda)_{12} &= 1\cdot0 + 1\cdot2 = 2 \\ (Q\Lambda)_{21} &= 1\cdot1 + (-1)\cdot0 = 1 \\ (Q\Lambda)_{22} &= 1\cdot0 + (-1)\cdot2 = -2 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} 1 & 2 \\ 1 & -2 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 1\cdot\frac{1}{2} + 2\cdot\frac{1}{2} = \frac{3}{2} \\ (A)_{12} &= 1\cdot\frac{1}{2} + 2\cdot(- \frac{1}{2}) = - \frac{1}{2} \\ (A)_{21} &= 1\cdot\frac{1}{2} + (-2)\cdot\frac{1}{2} = - \frac{1}{2} \\ (A)_{22} &= 1\cdot\frac{1}{2} + (-2)\cdot(- \frac{1}{2}) = \frac{3}{2} \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} \frac{3}{2} & - \frac{1}{2} \\ - \frac{1}{2} & \frac{3}{2} \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} $$

$\det Q = (1)(-1) - (1)(1) = -2$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-2}\begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & - \frac{1}{2} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} \frac{3}{2} & - \frac{1}{2} \\ - \frac{1}{2} & \frac{3}{2} \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 1\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} \frac{3}{2} & - \frac{1}{2} \\ - \frac{1}{2} & \frac{3}{2} \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \end{pmatrix} = 2\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 1 & 2 \\ 1 & -2 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{1}{2}\cdot1 + \frac{1}{2}\cdot1 = 1 \\ (Q^{-1}AQ)_{12} &= \frac{1}{2}\cdot2 + \frac{1}{2}\cdot(-2) = 0 \\ (Q^{-1}AQ)_{21} &= \frac{1}{2}\cdot1 + (- \frac{1}{2})\cdot1 = 0 \\ (Q^{-1}AQ)_{22} &= \frac{1}{2}\cdot2 + (- \frac{1}{2})\cdot(-2) = 2 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} = \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = z_1, \qquad \dot z_2 = 2z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{1t}, \qquad z_2(t) = c_2 e^{2t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{1t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2 e^{2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} $$

$$ x(t) = c_{1} e^{t} + c_{2} e^{2 t}, \qquad y(t) = c_{1} e^{t} - c_{2} e^{2 t} $$

#### Phase portrait

$\lambda_1 = 1$ and $\lambda_2 = 2$ are both positive: the origin is a **unstable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{1t}$ and $z_2 = c_2e^{2t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{2}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = 2$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 1$, i.e. to the line through $(1, 1)$ (they leave from there (the limit $t \to -\infty$)), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point away from the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, -1)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 1\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = 2\mathbf v_2$ points outward.

![[attachments/AM-PS/ch4a-e8-i-z.svg]]
*Canonical $\mathbf z$-plane (unstable node): invariant axes and orbits $z_2 = K|z_1|^{2}$.*

![[attachments/AM-PS/ch4a-e8-i-x.svg]]
*Original $(x, y)$-plane (unstable node): dashed lines are the eigenlines $\mathbf v_1 = (1, 1)$ and $\mathbf v_2 = (1, -1)$.*

### (ii) $\lambda_1 = 1$, $\mathbf v_1 = (1, 0)^T$; $\lambda_2 = -2$, $\mathbf v_2 = (1, 1)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & -2 \end{pmatrix}, \qquad \det Q = 1, \qquad Q^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 1\cdot1 + 1\cdot0 = 1 \\ (Q\Lambda)_{12} &= 1\cdot0 + 1\cdot(-2) = -2 \\ (Q\Lambda)_{21} &= 0\cdot1 + 1\cdot0 = 0 \\ (Q\Lambda)_{22} &= 0\cdot0 + 1\cdot(-2) = -2 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} 1 & -2 \\ 0 & -2 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 1\cdot1 + (-2)\cdot0 = 1 \\ (A)_{12} &= 1\cdot(-1) + (-2)\cdot1 = -3 \\ (A)_{21} &= 0\cdot1 + (-2)\cdot0 = 0 \\ (A)_{22} &= 0\cdot(-1) + (-2)\cdot1 = -2 \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} 1 & -3 \\ 0 & -2 \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} $$

$\det Q = (1)(1) - (1)(0) = 1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{1}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} 1 & -3 \\ 0 & -2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = 1\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 1 & -3 \\ 0 & -2 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -2 \\ -2 \end{pmatrix} = (-2)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 1 & -2 \\ 0 & -2 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 1\cdot1 + (-1)\cdot0 = 1 \\ (Q^{-1}AQ)_{12} &= 1\cdot(-2) + (-1)\cdot(-2) = 0 \\ (Q^{-1}AQ)_{21} &= 0\cdot1 + 1\cdot0 = 0 \\ (Q^{-1}AQ)_{22} &= 0\cdot(-2) + 1\cdot(-2) = -2 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 1 & 0 \\ 0 & -2 \end{pmatrix} = \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & -2 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = z_1, \qquad \dot z_2 = -2z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{1t}, \qquad z_2(t) = c_2 e^{-2t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{1t}\begin{pmatrix} 1 \\ 0 \end{pmatrix} + c_2 e^{-2t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

$$ x(t) = c_{1} e^{t} + c_{2} e^{-2 t}, \qquad y(t) = c_{2} e^{-2 t} $$

#### Phase portrait

$\lambda_1 = 1$ and $\lambda_2 = -2$ are of opposite signs: the origin is a **saddle** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{1t}$ and $z_2 = c_2e^{-2t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{-2}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = -2$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through $(1, 1)$ (the **stable manifold**), reach the origin as $t \to +\infty$; the line through $(1, 0)$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 0)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, 1)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 1\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = -2\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e8-ii-z.svg]]
*Canonical $\mathbf z$-plane (saddle): invariant axes and orbits $z_2 = K|z_1|^{-2}$.*

![[attachments/AM-PS/ch4a-e8-ii-x.svg]]
*Original $(x, y)$-plane (saddle): dashed lines are the eigenlines $\mathbf v_1 = (1, 0)$ and $\mathbf v_2 = (1, 1)$.*

### (iii) $\lambda_1 = -2$, $\mathbf v_1 = (1, 2)^T$; $\lambda_2 = -3$, $\mathbf v_2 = (2, -3)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 1 & 2 \\ 2 & -3 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} -2 & 0 \\ 0 & -3 \end{pmatrix}, \qquad \det Q = -7, \qquad Q^{-1} = \begin{pmatrix} \frac{3}{7} & \frac{2}{7} \\ \frac{2}{7} & - \frac{1}{7} \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 1\cdot(-2) + 2\cdot0 = -2 \\ (Q\Lambda)_{12} &= 1\cdot0 + 2\cdot(-3) = -6 \\ (Q\Lambda)_{21} &= 2\cdot(-2) + (-3)\cdot0 = -4 \\ (Q\Lambda)_{22} &= 2\cdot0 + (-3)\cdot(-3) = 9 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} -2 & -6 \\ -4 & 9 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-2)\cdot\frac{3}{7} + (-6)\cdot\frac{2}{7} = - \frac{18}{7} \\ (A)_{12} &= (-2)\cdot\frac{2}{7} + (-6)\cdot(- \frac{1}{7}) = \frac{2}{7} \\ (A)_{21} &= (-4)\cdot\frac{3}{7} + 9\cdot\frac{2}{7} = \frac{6}{7} \\ (A)_{22} &= (-4)\cdot\frac{2}{7} + 9\cdot(- \frac{1}{7}) = - \frac{17}{7} \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} - \frac{18}{7} & \frac{2}{7} \\ \frac{6}{7} & - \frac{17}{7} \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 2 \\ 2 & -3 \end{pmatrix} $$

$\det Q = (1)(-3) - (2)(2) = -7$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-7}\begin{pmatrix} -3 & -2 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} \frac{3}{7} & \frac{2}{7} \\ \frac{2}{7} & - \frac{1}{7} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} - \frac{18}{7} & \frac{2}{7} \\ \frac{6}{7} & - \frac{17}{7} \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -2 \\ -4 \end{pmatrix} = (-2)\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} - \frac{18}{7} & \frac{2}{7} \\ \frac{6}{7} & - \frac{17}{7} \end{pmatrix}\begin{pmatrix} 2 \\ -3 \end{pmatrix} = \begin{pmatrix} -6 \\ 9 \end{pmatrix} = (-3)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} -2 & -6 \\ -4 & 9 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{3}{7}\cdot(-2) + \frac{2}{7}\cdot(-4) = -2 \\ (Q^{-1}AQ)_{12} &= \frac{3}{7}\cdot(-6) + \frac{2}{7}\cdot9 = 0 \\ (Q^{-1}AQ)_{21} &= \frac{2}{7}\cdot(-2) + (- \frac{1}{7})\cdot(-4) = 0 \\ (Q^{-1}AQ)_{22} &= \frac{2}{7}\cdot(-6) + (- \frac{1}{7})\cdot9 = -3 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -2 & 0 \\ 0 & -3 \end{pmatrix} = \Lambda = \begin{pmatrix} -2 & 0 \\ 0 & -3 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = -2z_1, \qquad \dot z_2 = -3z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{-2t}, \qquad z_2(t) = c_2 e^{-3t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{-2t}\begin{pmatrix} 1 \\ 2 \end{pmatrix} + c_2 e^{-3t}\begin{pmatrix} 2 \\ -3 \end{pmatrix} $$

$$ x(t) = c_{1} e^{-2 t} + 2 c_{2} e^{-3 t}, \qquad y(t) = 2 c_{1} e^{-2 t} - 3 c_{2} e^{-3 t} $$

#### Phase portrait

$\lambda_1 = -2$ and $\lambda_2 = -3$ are both negative: the origin is a **stable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{-2t}$ and $z_2 = c_2e^{-3t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{\frac{3}{2}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = \frac{3}{2}$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 2$, i.e. to the line through $(1, 2)$ (they arrive there as $t \to +\infty$), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point towards the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 2)$ and the $z_2$-axis to the line through $\mathbf v_2 = (2, -3)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = -2\mathbf v_1$ points inward; on $\mathbf v_2$: $\dot{\mathbf x} = -3\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e8-iii-z.svg]]
*Canonical $\mathbf z$-plane (stable node): invariant axes and orbits $z_2 = K|z_1|^{\frac{3}{2}}$.*

![[attachments/AM-PS/ch4a-e8-iii-x.svg]]
*Original $(x, y)$-plane (stable node): dashed lines are the eigenlines $\mathbf v_1 = (1, 2)$ and $\mathbf v_2 = (2, -3)$.*

### (iv) $\lambda_1 = 3$, $\mathbf v_1 = (2, 3)^T$; $\lambda_2 = -5$, $\mathbf v_2 = (0, 1)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 2 & 0 \\ 3 & 1 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} 3 & 0 \\ 0 & -5 \end{pmatrix}, \qquad \det Q = 2, \qquad Q^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ - \frac{3}{2} & 1 \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 2\cdot3 + 0\cdot0 = 6 \\ (Q\Lambda)_{12} &= 2\cdot0 + 0\cdot(-5) = 0 \\ (Q\Lambda)_{21} &= 3\cdot3 + 1\cdot0 = 9 \\ (Q\Lambda)_{22} &= 3\cdot0 + 1\cdot(-5) = -5 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} 6 & 0 \\ 9 & -5 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 6\cdot\frac{1}{2} + 0\cdot(- \frac{3}{2}) = 3 \\ (A)_{12} &= 6\cdot0 + 0\cdot1 = 0 \\ (A)_{21} &= 9\cdot\frac{1}{2} + (-5)\cdot(- \frac{3}{2}) = 12 \\ (A)_{22} &= 9\cdot0 + (-5)\cdot1 = -5 \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} 3 & 0 \\ 12 & -5 \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 2 & 0 \\ 3 & 1 \end{pmatrix} $$

$\det Q = (2)(1) - (0)(3) = 2$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ -3 & 2 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 \\ - \frac{3}{2} & 1 \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} 3 & 0 \\ 12 & -5 \end{pmatrix}\begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 6 \\ 9 \end{pmatrix} = 3\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 3 & 0 \\ 12 & -5 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -5 \end{pmatrix} = (-5)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 6 & 0 \\ 9 & -5 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{1}{2}\cdot6 + 0\cdot9 = 3 \\ (Q^{-1}AQ)_{12} &= \frac{1}{2}\cdot0 + 0\cdot(-5) = 0 \\ (Q^{-1}AQ)_{21} &= (- \frac{3}{2})\cdot6 + 1\cdot9 = 0 \\ (Q^{-1}AQ)_{22} &= (- \frac{3}{2})\cdot0 + 1\cdot(-5) = -5 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 3 & 0 \\ 0 & -5 \end{pmatrix} = \Lambda = \begin{pmatrix} 3 & 0 \\ 0 & -5 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 3z_1, \qquad \dot z_2 = -5z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{3t}, \qquad z_2(t) = c_2 e^{-5t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{3t}\begin{pmatrix} 2 \\ 3 \end{pmatrix} + c_2 e^{-5t}\begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

$$ x(t) = 2 c_{1} e^{3 t}, \qquad y(t) = 3 c_{1} e^{3 t} + c_{2} e^{-5 t} $$

#### Phase portrait

$\lambda_1 = 3$ and $\lambda_2 = -5$ are of opposite signs: the origin is a **saddle** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{3t}$ and $z_2 = c_2e^{-5t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{- \frac{5}{3}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = - \frac{5}{3}$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through $(0, 1)$ (the **stable manifold**), reach the origin as $t \to +\infty$; the line through $(2, 3)$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (2, 3)$ and the $z_2$-axis to the line through $\mathbf v_2 = (0, 1)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 3\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = -5\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e8-iv-z.svg]]
*Canonical $\mathbf z$-plane (saddle): invariant axes and orbits $z_2 = K|z_1|^{- \frac{5}{3}}$.*

![[attachments/AM-PS/ch4a-e8-iv-x.svg]]
*Original $(x, y)$-plane (saddle): dashed lines are the eigenlines $\mathbf v_1 = (2, 3)$ and $\mathbf v_2 = (0, 1)$.*

### (v) $\lambda_1 = 3$, $\mathbf v_1 = (1, 2)^T$; $\lambda_2 = 1$, $\mathbf v_2 = (1, -3)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 1 & 1 \\ 2 & -3 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \det Q = -5, \qquad Q^{-1} = \begin{pmatrix} \frac{3}{5} & \frac{1}{5} \\ \frac{2}{5} & - \frac{1}{5} \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 1\cdot3 + 1\cdot0 = 3 \\ (Q\Lambda)_{12} &= 1\cdot0 + 1\cdot1 = 1 \\ (Q\Lambda)_{21} &= 2\cdot3 + (-3)\cdot0 = 6 \\ (Q\Lambda)_{22} &= 2\cdot0 + (-3)\cdot1 = -3 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} 3 & 1 \\ 6 & -3 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 3\cdot\frac{3}{5} + 1\cdot\frac{2}{5} = \frac{11}{5} \\ (A)_{12} &= 3\cdot\frac{1}{5} + 1\cdot(- \frac{1}{5}) = \frac{2}{5} \\ (A)_{21} &= 6\cdot\frac{3}{5} + (-3)\cdot\frac{2}{5} = \frac{12}{5} \\ (A)_{22} &= 6\cdot\frac{1}{5} + (-3)\cdot(- \frac{1}{5}) = \frac{9}{5} \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} \frac{11}{5} & \frac{2}{5} \\ \frac{12}{5} & \frac{9}{5} \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 1 \\ 2 & -3 \end{pmatrix} $$

$\det Q = (1)(-3) - (1)(2) = -5$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-5}\begin{pmatrix} -3 & -1 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} \frac{3}{5} & \frac{1}{5} \\ \frac{2}{5} & - \frac{1}{5} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} \frac{11}{5} & \frac{2}{5} \\ \frac{12}{5} & \frac{9}{5} \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 6 \end{pmatrix} = 3\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} \frac{11}{5} & \frac{2}{5} \\ \frac{12}{5} & \frac{9}{5} \end{pmatrix}\begin{pmatrix} 1 \\ -3 \end{pmatrix} = \begin{pmatrix} 1 \\ -3 \end{pmatrix} = 1\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 3 & 1 \\ 6 & -3 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{3}{5}\cdot3 + \frac{1}{5}\cdot6 = 3 \\ (Q^{-1}AQ)_{12} &= \frac{3}{5}\cdot1 + \frac{1}{5}\cdot(-3) = 0 \\ (Q^{-1}AQ)_{21} &= \frac{2}{5}\cdot3 + (- \frac{1}{5})\cdot6 = 0 \\ (Q^{-1}AQ)_{22} &= \frac{2}{5}\cdot1 + (- \frac{1}{5})\cdot(-3) = 1 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} = \Lambda = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 3z_1, \qquad \dot z_2 = z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{3t}, \qquad z_2(t) = c_2 e^{1t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{3t}\begin{pmatrix} 1 \\ 2 \end{pmatrix} + c_2 e^{1t}\begin{pmatrix} 1 \\ -3 \end{pmatrix} $$

$$ x(t) = c_{1} e^{3 t} + c_{2} e^{t}, \qquad y(t) = 2 c_{1} e^{3 t} - 3 c_{2} e^{t} $$

#### Phase portrait

$\lambda_1 = 3$ and $\lambda_2 = 1$ are both positive: the origin is a **unstable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{3t}$ and $z_2 = c_2e^{1t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{\frac{1}{3}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = \frac{1}{3}$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 1$, i.e. to the line through $(1, -3)$ (they leave from there (the limit $t \to -\infty$)), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point away from the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 2)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, -3)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 3\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = 1\mathbf v_2$ points outward.

![[attachments/AM-PS/ch4a-e8-v-z.svg]]
*Canonical $\mathbf z$-plane (unstable node): invariant axes and orbits $z_2 = K|z_1|^{\frac{1}{3}}$.*

![[attachments/AM-PS/ch4a-e8-v-x.svg]]
*Original $(x, y)$-plane (unstable node): dashed lines are the eigenlines $\mathbf v_1 = (1, 2)$ and $\mathbf v_2 = (1, -3)$.*

### (vi) $\lambda_1 = 2$, $\mathbf v_1 = (0, 1)^T$; $\lambda_2 = -3$, $\mathbf v_2 = (1, 5)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 0 & 1 \\ 1 & 5 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix}, \qquad \det Q = -1, \qquad Q^{-1} = \begin{pmatrix} -5 & 1 \\ 1 & 0 \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 0\cdot2 + 1\cdot0 = 0 \\ (Q\Lambda)_{12} &= 0\cdot0 + 1\cdot(-3) = -3 \\ (Q\Lambda)_{21} &= 1\cdot2 + 5\cdot0 = 2 \\ (Q\Lambda)_{22} &= 1\cdot0 + 5\cdot(-3) = -15 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} 0 & -3 \\ 2 & -15 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 0\cdot(-5) + (-3)\cdot1 = -3 \\ (A)_{12} &= 0\cdot1 + (-3)\cdot0 = 0 \\ (A)_{21} &= 2\cdot(-5) + (-15)\cdot1 = -25 \\ (A)_{22} &= 2\cdot1 + (-15)\cdot0 = 2 \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} -3 & 0 \\ -25 & 2 \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 0 & 1 \\ 1 & 5 \end{pmatrix} $$

$\det Q = (0)(5) - (1)(1) = -1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-1}\begin{pmatrix} 5 & -1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} -5 & 1 \\ 1 & 0 \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} -3 & 0 \\ -25 & 2 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 2 \end{pmatrix} = 2\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} -3 & 0 \\ -25 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 5 \end{pmatrix} = \begin{pmatrix} -3 \\ -15 \end{pmatrix} = (-3)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 0 & -3 \\ 2 & -15 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= (-5)\cdot0 + 1\cdot2 = 2 \\ (Q^{-1}AQ)_{12} &= (-5)\cdot(-3) + 1\cdot(-15) = 0 \\ (Q^{-1}AQ)_{21} &= 1\cdot0 + 0\cdot2 = 0 \\ (Q^{-1}AQ)_{22} &= 1\cdot(-3) + 0\cdot(-15) = -3 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix} = \Lambda = \begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 2z_1, \qquad \dot z_2 = -3z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{2t}, \qquad z_2(t) = c_2 e^{-3t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{2t}\begin{pmatrix} 0 \\ 1 \end{pmatrix} + c_2 e^{-3t}\begin{pmatrix} 1 \\ 5 \end{pmatrix} $$

$$ x(t) = c_{2} e^{-3 t}, \qquad y(t) = c_{1} e^{2 t} + 5 c_{2} e^{-3 t} $$

#### Phase portrait

$\lambda_1 = 2$ and $\lambda_2 = -3$ are of opposite signs: the origin is a **saddle** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{2t}$ and $z_2 = c_2e^{-3t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{- \frac{3}{2}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = - \frac{3}{2}$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through $(1, 5)$ (the **stable manifold**), reach the origin as $t \to +\infty$; the line through $(0, 1)$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (0, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, 5)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 2\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = -3\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e8-vi-z.svg]]
*Canonical $\mathbf z$-plane (saddle): invariant axes and orbits $z_2 = K|z_1|^{- \frac{3}{2}}$.*

![[attachments/AM-PS/ch4a-e8-vi-x.svg]]
*Original $(x, y)$-plane (saddle): dashed lines are the eigenlines $\mathbf v_1 = (0, 1)$ and $\mathbf v_2 = (1, 5)$.*

### (vii) $\lambda_1 = 1$, $\mathbf v_1 = (1, 1)^T$; $\lambda_2 = 2$, $\mathbf v_2 = (2, 1)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}, \qquad \det Q = -1, \qquad Q^{-1} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 1\cdot1 + 2\cdot0 = 1 \\ (Q\Lambda)_{12} &= 1\cdot0 + 2\cdot2 = 4 \\ (Q\Lambda)_{21} &= 1\cdot1 + 1\cdot0 = 1 \\ (Q\Lambda)_{22} &= 1\cdot0 + 1\cdot2 = 2 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} 1 & 4 \\ 1 & 2 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 1\cdot(-1) + 4\cdot1 = 3 \\ (A)_{12} &= 1\cdot2 + 4\cdot(-1) = -2 \\ (A)_{21} &= 1\cdot(-1) + 2\cdot1 = 1 \\ (A)_{22} &= 1\cdot2 + 2\cdot(-1) = 0 \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} $$

$\det Q = (1)(1) - (2)(1) = -1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-1}\begin{pmatrix} 1 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 1\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix} = 2\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 1 & 4 \\ 1 & 2 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= (-1)\cdot1 + 2\cdot1 = 1 \\ (Q^{-1}AQ)_{12} &= (-1)\cdot4 + 2\cdot2 = 0 \\ (Q^{-1}AQ)_{21} &= 1\cdot1 + (-1)\cdot1 = 0 \\ (Q^{-1}AQ)_{22} &= 1\cdot4 + (-1)\cdot2 = 2 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} = \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = z_1, \qquad \dot z_2 = 2z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{1t}, \qquad z_2(t) = c_2 e^{2t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{1t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2 e^{2t}\begin{pmatrix} 2 \\ 1 \end{pmatrix} $$

$$ x(t) = c_{1} e^{t} + 2 c_{2} e^{2 t}, \qquad y(t) = c_{1} e^{t} + c_{2} e^{2 t} $$

#### Phase portrait

$\lambda_1 = 1$ and $\lambda_2 = 2$ are both positive: the origin is a **unstable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{1t}$ and $z_2 = c_2e^{2t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{2}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = 2$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 1$, i.e. to the line through $(1, 1)$ (they leave from there (the limit $t \to -\infty$)), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point away from the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (2, 1)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 1\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = 2\mathbf v_2$ points outward.

![[attachments/AM-PS/ch4a-e8-vii-z.svg]]
*Canonical $\mathbf z$-plane (unstable node): invariant axes and orbits $z_2 = K|z_1|^{2}$.*

![[attachments/AM-PS/ch4a-e8-vii-x.svg]]
*Original $(x, y)$-plane (unstable node): dashed lines are the eigenlines $\mathbf v_1 = (1, 1)$ and $\mathbf v_2 = (2, 1)$.*

### (viii) $\lambda_1 = -3$, $\mathbf v_1 = (1, 3)^T$; $\lambda_2 = -1$, $\mathbf v_2 = (-3, 2)^T$

The statement gives the eigen-data, not the matrix. Since $A\mathbf v_j = \lambda_j\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\Lambda$ with $Q = [\mathbf v_1 \mid \mathbf v_2]$, the matrix is $A = Q\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):

$$ Q = \begin{pmatrix} 1 & -3 \\ 3 & 2 \end{pmatrix}, \qquad \Lambda = \begin{pmatrix} -3 & 0 \\ 0 & -1 \end{pmatrix}, \qquad \det Q = 11, \qquad Q^{-1} = \begin{pmatrix} \frac{2}{11} & \frac{3}{11} \\ - \frac{3}{11} & \frac{1}{11} \end{pmatrix} $$

$$ \begin{aligned} (Q\Lambda)_{11} &= 1\cdot(-3) + (-3)\cdot0 = -3 \\ (Q\Lambda)_{12} &= 1\cdot0 + (-3)\cdot(-1) = 3 \\ (Q\Lambda)_{21} &= 3\cdot(-3) + 2\cdot0 = -9 \\ (Q\Lambda)_{22} &= 3\cdot0 + 2\cdot(-1) = -2 \end{aligned} $$

$$ Q\Lambda = \begin{pmatrix} -3 & 3 \\ -9 & -2 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-3)\cdot\frac{2}{11} + 3\cdot(- \frac{3}{11}) = - \frac{15}{11} \\ (A)_{12} &= (-3)\cdot\frac{3}{11} + 3\cdot\frac{1}{11} = - \frac{6}{11} \\ (A)_{21} &= (-9)\cdot\frac{2}{11} + (-2)\cdot(- \frac{3}{11}) = - \frac{12}{11} \\ (A)_{22} &= (-9)\cdot\frac{3}{11} + (-2)\cdot\frac{1}{11} = - \frac{29}{11} \end{aligned} $$

$$ A = Q\Lambda Q^{-1} = \begin{pmatrix} - \frac{15}{11} & - \frac{6}{11} \\ - \frac{12}{11} & - \frac{29}{11} \end{pmatrix} $$

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & -3 \\ 3 & 2 \end{pmatrix} $$

$\det Q = (1)(2) - (-3)(3) = 11$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{11}\begin{pmatrix} 2 & 3 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} \frac{2}{11} & \frac{3}{11} \\ - \frac{3}{11} & \frac{1}{11} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} - \frac{15}{11} & - \frac{6}{11} \\ - \frac{12}{11} & - \frac{29}{11} \end{pmatrix}\begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} -3 \\ -9 \end{pmatrix} = (-3)\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} - \frac{15}{11} & - \frac{6}{11} \\ - \frac{12}{11} & - \frac{29}{11} \end{pmatrix}\begin{pmatrix} -3 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 \\ -2 \end{pmatrix} = (-1)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} -3 & 3 \\ -9 & -2 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{2}{11}\cdot(-3) + \frac{3}{11}\cdot(-9) = -3 \\ (Q^{-1}AQ)_{12} &= \frac{2}{11}\cdot3 + \frac{3}{11}\cdot(-2) = 0 \\ (Q^{-1}AQ)_{21} &= (- \frac{3}{11})\cdot(-3) + \frac{1}{11}\cdot(-9) = 0 \\ (Q^{-1}AQ)_{22} &= (- \frac{3}{11})\cdot3 + \frac{1}{11}\cdot(-2) = -1 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -3 & 0 \\ 0 & -1 \end{pmatrix} = \Lambda = \begin{pmatrix} -3 & 0 \\ 0 & -1 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = -3z_1, \qquad \dot z_2 = -z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{-3t}, \qquad z_2(t) = c_2 e^{-1t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{-3t}\begin{pmatrix} 1 \\ 3 \end{pmatrix} + c_2 e^{-1t}\begin{pmatrix} -3 \\ 2 \end{pmatrix} $$

$$ x(t) = c_{1} e^{-3 t} - 3 c_{2} e^{-t}, \qquad y(t) = 3 c_{1} e^{-3 t} + 2 c_{2} e^{-t} $$

#### Phase portrait

$\lambda_1 = -3$ and $\lambda_2 = -1$ are both negative: the origin is a **stable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{-3t}$ and $z_2 = c_2e^{-1t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{\frac{1}{3}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = \frac{1}{3}$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 1$, i.e. to the line through $(-3, 2)$ (they arrive there as $t \to +\infty$), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point towards the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 3)$ and the $z_2$-axis to the line through $\mathbf v_2 = (-3, 2)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = -3\mathbf v_1$ points inward; on $\mathbf v_2$: $\dot{\mathbf x} = -1\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4a-e8-viii-z.svg]]
*Canonical $\mathbf z$-plane (stable node): invariant axes and orbits $z_2 = K|z_1|^{\frac{1}{3}}$.*

![[attachments/AM-PS/ch4a-e8-viii-x.svg]]
*Original $(x, y)$-plane (stable node): dashed lines are the eigenlines $\mathbf v_1 = (1, 3)$ and $\mathbf v_2 = (-3, 2)$.*

## Phase 4: Interpretation and checks

| Item | General solution |
| :--- | :--- |
| (i) | $\mathbf x = c_1e^{1t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2e^{2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ |
| (ii) | $\mathbf x = c_1e^{1t}\begin{pmatrix} 1 \\ 0 \end{pmatrix} + c_2e^{-2t}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ |
| (iii) | $\mathbf x = c_1e^{-2t}\begin{pmatrix} 1 \\ 2 \end{pmatrix} + c_2e^{-3t}\begin{pmatrix} 2 \\ -3 \end{pmatrix}$ |
| (iv) | $\mathbf x = c_1e^{3t}\begin{pmatrix} 2 \\ 3 \end{pmatrix} + c_2e^{-5t}\begin{pmatrix} 0 \\ 1 \end{pmatrix}$ |
| (v) | $\mathbf x = c_1e^{3t}\begin{pmatrix} 1 \\ 2 \end{pmatrix} + c_2e^{1t}\begin{pmatrix} 1 \\ -3 \end{pmatrix}$ |
| (vi) | $\mathbf x = c_1e^{2t}\begin{pmatrix} 0 \\ 1 \end{pmatrix} + c_2e^{-3t}\begin{pmatrix} 1 \\ 5 \end{pmatrix}$ |
| (vii) | $\mathbf x = c_1e^{1t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2e^{2t}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ |
| (viii) | $\mathbf x = c_1e^{-3t}\begin{pmatrix} 1 \\ 3 \end{pmatrix} + c_2e^{-1t}\begin{pmatrix} -3 \\ 2 \end{pmatrix}$ |

- In every item the reconstructed $A$ satisfies $A\mathbf v_j = \lambda_j\mathbf v_j$ (checked in the text) and $\det A = \lambda_1\lambda_2$, $\operatorname{tr}A = \lambda_1 + \lambda_2$.
- Nodes: the tangent direction at the origin is the eigenvector of the **smaller** $|\lambda|$ because $|z_2|/|z_1|^{\lambda_2/\lambda_1}$ is constant: if $|\lambda_2| > |\lambda_1|$ the exponent $r = \lambda_2/\lambda_1$ exceeds $1$, so $z_2 = K|z_1|^{r}$ tends to $0$ faster than $z_1$ and the curve hugs the $z_1$-axis (the slower eigendirection) near the origin; if $r < 1$ it hugs the $z_2$-axis, which is then the slower one. The phase portraits drawn above show this numerically (curves integrated from the matrix $A$ itself, not from the formula, so the tangency is a genuine check).
- Saddles (ii), (iv), (vi): the stable manifold is the eigenline of the negative eigenvalue.
- Items (ii), (iv) and (vi) have an eigenvector with a zero entry ((ii) $\mathbf v_1 = (1, 0)$, (iv) $\mathbf v_2 = (0, 1)$, (vi) $\mathbf v_1 = (0, 1)$): that eigenline is an axis of the $(x, y)$-plane.
