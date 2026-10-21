---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 5"
dificultad: media
id: "e5"
pill: "Inverse Problem • A = Q J Q⁻¹ • Three Matrices"
tags:
  - problema-resuelto
  - problema-inverso
  - autovalores-complejos
  - construccion-de-matrices
---

# Problem 4.II.5: Building a Matrix from a Complex Pair of Eigenvalues and Eigenvectors

> Official exercise 5 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Show how to construct a matrix with a complex conjugate pair of eigenvalues $\lambda_\pm = \rho \pm i\omega$ and corresponding eigenvectors $\boldsymbol\eta_\pm = \mathbf v_1 \pm i\mathbf v_2$. Hence find the matrices with the following eigenvalues and eigenvectors:

- (i) $\lambda_\pm = 3 \pm 3i,\ \boldsymbol\eta_\pm = (2 \pm i,\ 1 \mp i)$;
- (ii) $\lambda_\pm = \pm 3i,\ \boldsymbol\eta_\pm = (\pm i,\ 3 \pm 2i)$;
- (iii) $\lambda_\pm = -2 \pm i,\ \boldsymbol\eta_\pm = (1 \pm i,\ 1 \mp i)$.

## Phase 1: Setup and hypotheses

We look for a real matrix $A$ ($2\times 2$) with $A\boldsymbol\eta_+ = \lambda_+\boldsymbol\eta_+$ where $\boldsymbol\eta_+ = \mathbf v_1 + i\mathbf v_2$ and $\lambda_+ = \rho + i\omega$, with $\mathbf v_1, \mathbf v_2$ real and independent and $\omega \neq 0$. Because $A$ is real, $A\bar{\boldsymbol\eta}_+ = \bar\lambda_+\bar{\boldsymbol\eta}_+$ follows automatically. (Note on the statement: the sheet writes $\boldsymbol\eta_\pm = \mathbf v_1 \pm i\mathbf v_2$ for the eigenvectors of $\lambda_\pm = \rho \pm i\omega$, i.e. $\mathbf v_1 = \mathbf u$, $\mathbf v_2 = \mathbf w$ of Topic 4.)

## Phase 2: Formulation: the construction

Expand $A(\mathbf v_1 + i\mathbf v_2) = (\rho + i\omega)(\mathbf v_1 + i\mathbf v_2)$ and separate real and imaginary parts (both $A\mathbf v_j$ are real vectors, $i^2 = -1$):

$$ A\mathbf v_1 + iA\mathbf v_2 = (\rho\mathbf v_1 - \omega\mathbf v_2) + i(\omega\mathbf v_1 + \rho\mathbf v_2) \;\Longrightarrow\; A\mathbf v_1 = \rho\mathbf v_1 - \omega\mathbf v_2,\quad A\mathbf v_2 = \omega\mathbf v_1 + \rho\mathbf v_2 $$

Collect the two vector equations in one matrix equation, with $Q = [\mathbf v_1 \mid \mathbf v_2]$ (columns): the first column of $QJ$ is $\rho\mathbf v_1 - \omega\mathbf v_2$ for $J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix}$ and the second is $\omega\mathbf v_1 + \rho\mathbf v_2$. Hence $AQ = QJ$, and since $\mathbf v_1, \mathbf v_2$ are independent (Exercise 4) $Q$ is invertible:

$$ \boxed{A = QJQ^{-1}, \qquad Q = [\mathbf v_1 \mid \mathbf v_2], \qquad J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix}} $$

This $A$ is real (a product of real matrices), has the eigenvalues of $J$, $\rho \pm i\omega$ (similar matrices have the same characteristic polynomial), and $A\boldsymbol\eta_+ = \lambda_+\boldsymbol\eta_+$ by construction.

## Phase 3: Derivation of the three matrices

### (i) $\lambda_\pm = 3 \pm 3i,\ \boldsymbol\eta_\pm = (2 \pm i,\ 1 \mp i)$

$\boldsymbol\eta_+ = \begin{pmatrix} 2 + i \\ 1 - i \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} + i\begin{pmatrix} 1 \\ -1 \end{pmatrix}$, so $\mathbf v_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, $\mathbf v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, $\rho = 3$, $\omega = 3$.

$$ Q = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}, \quad J = \begin{pmatrix} 3 & 3 \\ -3 & 3 \end{pmatrix}, \quad \det Q = -3, \quad Q^{-1} = \begin{pmatrix} \frac{1}{3} & \frac{1}{3} \\ \frac{1}{3} & - \frac{2}{3} \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 2\cdot3 + 1\cdot(-3) = 3 \\ (QJ)_{12} &= 2\cdot3 + 1\cdot3 = 9 \\ (QJ)_{21} &= 1\cdot3 + (-1)\cdot(-3) = 6 \\ (QJ)_{22} &= 1\cdot3 + (-1)\cdot3 = 0 \end{aligned} $$

$$ \begin{aligned} (A)_{11} &= 3\cdot\frac{1}{3} + 9\cdot\frac{1}{3} = 4 \\ (A)_{12} &= 3\cdot\frac{1}{3} + 9\cdot(- \frac{2}{3}) = -5 \\ (A)_{21} &= 6\cdot\frac{1}{3} + 0\cdot\frac{1}{3} = 2 \\ (A)_{22} &= 6\cdot\frac{1}{3} + 0\cdot(- \frac{2}{3}) = 2 \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} 4 & -5 \\ 2 & 2 \end{pmatrix} $$

#### Verification

$$ A\boldsymbol\eta_+ = \begin{pmatrix} 4 & -5 \\ 2 & 2 \end{pmatrix}\begin{pmatrix} 2 + i \\ 1 - i \end{pmatrix} = \begin{pmatrix} 4\,(2 + i) + (-5)\,(1 - i) = 3 + 9 i \\ 2\,(2 + i) + 2\,(1 - i) = 6 \end{pmatrix} = (3 + 3 i)\,\begin{pmatrix} 2 + i \\ 1 - i \end{pmatrix} $$

Characteristic polynomial: $\lambda^2 - (6)\lambda + (18) = 0$ has $\operatorname{tr}A = 6 = 2\rho$ and $\det A = 18 = \rho^2 + \omega^2$, hence $\lambda = 3 \pm i\sqrt{9}$, i.e. $\rho \pm i\omega$ with $\rho = 3$, $\omega = 3$.

### (ii) $\lambda_\pm = \pm 3i,\ \boldsymbol\eta_\pm = (\pm i,\ 3 \pm 2i)$

$\boldsymbol\eta_+ = \begin{pmatrix} i \\ 3 + 2 i \end{pmatrix} = \begin{pmatrix} 0 \\ 3 \end{pmatrix} + i\begin{pmatrix} 1 \\ 2 \end{pmatrix}$, so $\mathbf v_1 = \begin{pmatrix} 0 \\ 3 \end{pmatrix}$, $\mathbf v_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $\rho = 0$, $\omega = 3$.

$$ Q = \begin{pmatrix} 0 & 1 \\ 3 & 2 \end{pmatrix}, \quad J = \begin{pmatrix} 0 & 3 \\ -3 & 0 \end{pmatrix}, \quad \det Q = -3, \quad Q^{-1} = \begin{pmatrix} - \frac{2}{3} & \frac{1}{3} \\ 1 & 0 \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 0\cdot0 + 1\cdot(-3) = -3 \\ (QJ)_{12} &= 0\cdot3 + 1\cdot0 = 0 \\ (QJ)_{21} &= 3\cdot0 + 2\cdot(-3) = -6 \\ (QJ)_{22} &= 3\cdot3 + 2\cdot0 = 9 \end{aligned} $$

$$ \begin{aligned} (A)_{11} &= (-3)\cdot(- \frac{2}{3}) + 0\cdot1 = 2 \\ (A)_{12} &= (-3)\cdot\frac{1}{3} + 0\cdot0 = -1 \\ (A)_{21} &= (-6)\cdot(- \frac{2}{3}) + 9\cdot1 = 13 \\ (A)_{22} &= (-6)\cdot\frac{1}{3} + 9\cdot0 = -2 \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} 2 & -1 \\ 13 & -2 \end{pmatrix} $$

#### Verification

$$ A\boldsymbol\eta_+ = \begin{pmatrix} 2 & -1 \\ 13 & -2 \end{pmatrix}\begin{pmatrix} i \\ 3 + 2 i \end{pmatrix} = \begin{pmatrix} 2\,(i) + (-1)\,(3 + 2 i) = -3 \\ 13\,(i) + (-2)\,(3 + 2 i) = -6 + 9 i \end{pmatrix} = (3 i)\,\begin{pmatrix} i \\ 3 + 2 i \end{pmatrix} $$

Characteristic polynomial: $\lambda^2 - (0)\lambda + (9) = 0$ has $\operatorname{tr}A = 0 = 2\rho$ and $\det A = 9 = \rho^2 + \omega^2$, hence $\lambda = 0 \pm i\sqrt{9}$, i.e. $\rho \pm i\omega$ with $\rho = 0$, $\omega = 3$.

### (iii) $\lambda_\pm = -2 \pm i,\ \boldsymbol\eta_\pm = (1 \pm i,\ 1 \mp i)$

$\boldsymbol\eta_+ = \begin{pmatrix} 1 + i \\ 1 - i \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} + i\begin{pmatrix} 1 \\ -1 \end{pmatrix}$, so $\mathbf v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $\mathbf v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, $\rho = -2$, $\omega = 1$.

$$ Q = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad J = \begin{pmatrix} -2 & 1 \\ -1 & -2 \end{pmatrix}, \quad \det Q = -2, \quad Q^{-1} = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & - \frac{1}{2} \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 1\cdot(-2) + 1\cdot(-1) = -3 \\ (QJ)_{12} &= 1\cdot1 + 1\cdot(-2) = -1 \\ (QJ)_{21} &= 1\cdot(-2) + (-1)\cdot(-1) = -1 \\ (QJ)_{22} &= 1\cdot1 + (-1)\cdot(-2) = 3 \end{aligned} $$

$$ \begin{aligned} (A)_{11} &= (-3)\cdot\frac{1}{2} + (-1)\cdot\frac{1}{2} = -2 \\ (A)_{12} &= (-3)\cdot\frac{1}{2} + (-1)\cdot(- \frac{1}{2}) = -1 \\ (A)_{21} &= (-1)\cdot\frac{1}{2} + 3\cdot\frac{1}{2} = 1 \\ (A)_{22} &= (-1)\cdot\frac{1}{2} + 3\cdot(- \frac{1}{2}) = -2 \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} -2 & -1 \\ 1 & -2 \end{pmatrix} $$

#### Verification

$$ A\boldsymbol\eta_+ = \begin{pmatrix} -2 & -1 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} 1 + i \\ 1 - i \end{pmatrix} = \begin{pmatrix} (-2)\,(1 + i) + (-1)\,(1 - i) = -3 - i \\ 1\,(1 + i) + (-2)\,(1 - i) = -1 + 3 i \end{pmatrix} = (-2 + i)\,\begin{pmatrix} 1 + i \\ 1 - i \end{pmatrix} $$

Characteristic polynomial: $\lambda^2 - (-4)\lambda + (5) = 0$ has $\operatorname{tr}A = -4 = 2\rho$ and $\det A = 5 = \rho^2 + \omega^2$, hence $\lambda = -2 \pm i\sqrt{1}$, i.e. $\rho \pm i\omega$ with $\rho = -2$, $\omega = 1$.

## Phase 4: Interpretation and checks

- The matrix is **not unique** if only the eigenvalues are prescribed, but it is unique once $\boldsymbol\eta_+$ is given (up to the complex scalar multiple that every eigenvector admits: rescaling $\boldsymbol\eta_+$ by $c = c_r + ic_i$ changes $(\mathbf v_1, \mathbf v_2)$ and leaves $A$ unchanged, since $A\bar{\boldsymbol\eta}_+$, $A\boldsymbol\eta_+$ still determine $A$ on the basis $\{\boldsymbol\eta_+, \bar{\boldsymbol\eta}_+\}$ of $\mathbb C^2$).
- For the three items $\operatorname{tr}A = 6, 0, -4$ and $\det A = 18, 9, 5$ respectively, which are $2\rho$ and $\rho^2 + \omega^2$ as the construction predicts.
- (ii) has $\rho = 0$: a centre. $A = \begin{pmatrix} 2 & -1 \\ 13 & -2 \end{pmatrix}$ has trace zero and determinant $9 = \omega^2$.
- This is the inverse of Exercise 3: from $A$ to $(Q, J)$ there, from $(Q, J)$ to $A$ here.
