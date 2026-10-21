---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 11"
dificultad: media
id: "e11"
pill: "Zero Eigenvalue • Line of Equilibria • Parallel Orbits"
tags:
  - problema-resuelto
  - autovalor-cero
  - retrato-de-fase
  - equilibrios
---

# Problem 4.I.11: A Zero Eigenvalue: Lines of Equilibria

> Official exercise 11 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Suppose that $A$ has eigenvalues $\lambda_1 = 0$, $\lambda_2 \neq 0$, with eigenvectors $\mathbf v_1$ and $\mathbf v_2$, respectively.

- (i) Write down the general solution of $\dot{\mathbf x} = A\mathbf x$.
- (ii) After changing to a coordinate system $\tilde{\mathbf x}$ referred to the eigenvectors, we obtain $\dfrac{d\tilde{\mathbf x}}{dt} = \begin{pmatrix} 0 & 0 \\ 0 & \lambda_2 \end{pmatrix}\tilde{\mathbf x}$. By solving these equations draw the phase portrait in the $\tilde{\mathbf x}$ system, and sketch the phase portrait for the original coordinates $\mathbf x$.
- (iii) Draw the phase portrait for the equation $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} -2 & 2 \\ 1 & -1 \end{pmatrix}\mathbf x$.

## Phase 1: Setup and hypotheses

$A$ is $2\times 2$ real with eigenvalues $0$ and $\lambda_2 \neq 0$ (both real: $\lambda_1 = 0$ is real and $\lambda_2 = \operatorname{tr}A$ is real because $A$ is real; being distinct, they have independent eigenvectors; $\det A = 0$). $A\mathbf v_1 = \mathbf 0$, $A\mathbf v_2 = \lambda_2\mathbf v_2$. Because $\det A = 0$ the origin is **not** an isolated equilibrium: every point of $\ker A = \operatorname{span}\{\mathbf v_1\}$ is an equilibrium ($A\mathbf x = \mathbf 0$).

## Phase 2: Formulation

Use the general result for distinct eigenvalues, $\mathbf x = c_1e^{\lambda_1t}\mathbf v_1 + c_2e^{\lambda_2t}\mathbf v_2$ (Robinson Eq. 28.1), valid whenever the eigenvalues differ, in particular if one of them is $0$; and $Q = [\mathbf v_1\ \mathbf v_2]$, $\mathbf z = Q^{-1}\mathbf x$.

## Phase 3: Derivation

### (i) General solution

With $\lambda_1 = 0$, $e^{\lambda_1t} = e^{0} = 1$:

$$ \mathbf x(t) = c_1\mathbf v_1 + c_2e^{\lambda_2t}\mathbf v_2 $$

Check: $\dot{\mathbf x} = c_2\lambda_2e^{\lambda_2t}\mathbf v_2$ and $A\mathbf x = c_1A\mathbf v_1 + c_2e^{\lambda_2t}A\mathbf v_2 = \mathbf 0 + c_2\lambda_2e^{\lambda_2t}\mathbf v_2$. They agree. The constant vector $c_1\mathbf v_1$ is an equilibrium and $c_2e^{\lambda_2t}\mathbf v_2$ the time-dependent part.

### (ii) Canonical phase portrait and its image

In the coordinates $\tilde{\mathbf x} = (\tilde x, \tilde y)^T$ referred to $\mathbf v_1, \mathbf v_2$ the system is $\dot{\tilde x} = 0$, $\dot{\tilde y} = \lambda_2\tilde y$. The first gives $\tilde x = c_1$ (constant); the second is separable: $\frac{d\tilde y}{\tilde y} = \lambda_2\,dt$, $\ln|\tilde y| = \lambda_2t + C$, so $\tilde y = c_2e^{\lambda_2t}$.

$$ \tilde x(t) = c_1, \qquad \tilde y(t) = c_2e^{\lambda_2t} $$

- Orbits: the **vertical lines** $\tilde x = c_1$, because $\tilde x$ never changes. Each such line is a pair of half-lines (for $\tilde y > 0$ and $\tilde y < 0$) and the point $(c_1, 0)$ is an equilibrium.
- The $\tilde x$-axis ($\tilde y = 0$) consists entirely of equilibria (it is the image of $\ker A$).
- Direction: if $\lambda_2 < 0$, $|\tilde y| = |c_2|e^{\lambda_2t}$ decreases: the arrows on every vertical line point **towards** the $\tilde x$-axis, which they approach as $t \to +\infty$ without reaching it. If $\lambda_2 > 0$ the arrows point **away** from the axis. The sign of $\dot{\tilde y} = \lambda_2\tilde y$ gives the direction at once.
- Original coordinates: $\mathbf x = Q\tilde{\mathbf x} = \tilde x\mathbf v_1 + \tilde y\mathbf v_2$. The $\tilde x$-axis goes to the line $\operatorname{span}\{\mathbf v_1\}$ of equilibria and the vertical lines go to the lines $c_1\mathbf v_1 + s\mathbf v_2$, $s \in \mathbb R$, **parallel to $\mathbf v_2$**, drawn through the points of the line of equilibria. Straight lines remain straight: the picture is the canonical one sheared, with orbits along $\mathbf v_2$ towards/away from the line of equilibria.

![[attachments/AM-PS/ch4a-e11-ii-neg.svg]]
*Canonical $\tilde{\mathbf x}$-plane, $\lambda_2 < 0$: the $\tilde x$-axis (green) is a line of equilibria and the vertical orbits approach it.*

![[attachments/AM-PS/ch4a-e11-ii-pos.svg]]
*Canonical $\tilde{\mathbf x}$-plane, $\lambda_2 > 0$: the vertical orbits leave the line of equilibria.*

![[attachments/AM-PS/ch4a-e11-ii-x.svg]]
*Original $(x, y)$-plane for the example $\mathbf v_1 = (1, 0)$, $\mathbf v_2 = (1, 1)$, $\lambda_2 = -2$: equilibria on the line of $\mathbf v_1$, orbits parallel to $\mathbf v_2$.*

(For the sketch in the original plane, take the example $\mathbf v_1 = (1, 0)$, $\mathbf v_2 = (1, 1)$, $\lambda_2 = -2$, whose matrix is $A = Q\Lambda Q^{-1} = \begin{pmatrix} 0 & -2 \\ 0 & -2 \end{pmatrix}$; any other eigen-data give the same picture up to a linear change of the axes.)

### (iii) The matrix $\begin{pmatrix} -2 & 2 \\ 1 & -1 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} -2 - \lambda & 2 \\ 1 & -1 - \lambda \end{vmatrix} = (-2 - \lambda)(-1 - \lambda) - (2)(1) $$

$$ = \lambda^2 - (-2 + (-1))\lambda + (-2\cdot(-1) - 2\cdot1) = \lambda^2 - (-3)\lambda + (0) = \lambda^{2} + 3 \lambda $$

$\operatorname{tr}A = -3$, $\det A = 0$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 9 - 0 = 9$.

$$ \lambda = \frac{-3 \pm \sqrt{9}}{2} = \frac{-3 \pm 3}{2} \quad\Longrightarrow\quad \lambda_1 = 0,\ \lambda_2 = -3 $$

Check: $\lambda_1 + \lambda_2 = -3 = \operatorname{tr}A$ and $\lambda_1\lambda_2 = 0 = \det A$.

#### Eigenvectors

For $\lambda = 0$: $(A - (0)I)\mathbf{v_1} = \mathbf 0$, that is

$$ \begin{pmatrix} -2 & 2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} -2v_1 + 2v_2 = 0\quad (\text{row 1}) \\ 1v_1 - 1v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 equals $- \frac{1}{2}$ times row 1) and express a single condition. Row 1 reads $-2v_1 + 2v_2 = 0$, so $v_1 = v_2$: every eigenvector is a multiple of $(1, 1)^T$. The smallest integer representative is

$$ \mathbf{v_1} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

Check: $A\mathbf{v_1} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} = 0\mathbf{v_1}$.

For $\lambda = -3$: $(A - (-3)I)\mathbf{v_2} = \mathbf 0$, that is

$$ \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{aligned} 1v_1 + 2v_2 = 0\quad (\text{row 1}) \\ 1v_1 + 2v_2 = 0\quad (\text{row 2}) \end{aligned} $$

The coefficient matrix is singular ($\det(A - \lambda I) = 0$), so the rows are proportional (row 2 is identical to row 1) and express a single condition. Row 1 reads $1v_1 + 2v_2 = 0$, so $v_1 = -2\,v_2$: every eigenvector is a multiple of $(-2, 1)^T$. The smallest integer representative is

$$ \mathbf{v_2} = \begin{pmatrix} 2 \\ -1 \end{pmatrix} $$

Check: $A\mathbf{v_2} = \begin{pmatrix} -6 \\ 3 \end{pmatrix} = -3\mathbf{v_2}$.

#### Change of coordinates

The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\mathbf v_1 \mid \mathbf v_2]$, and define the new coordinates by $\mathbf z = Q^{-1}\mathbf x$, i.e. $\mathbf x = Q\mathbf z$:

$$ Q = \begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix} $$

$\det Q = (1)(-1) - (2)(1) = -3$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-3}\begin{pmatrix} -1 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{3} & \frac{2}{3} \\ \frac{1}{3} & - \frac{1}{3} \end{pmatrix} $$

Since $Q$ is constant, $\dot{\mathbf z} = Q^{-1}\dot{\mathbf x} = Q^{-1}A\mathbf x = (Q^{-1}AQ)\mathbf z$. Compute $AQ$ one column at a time, with $A\mathbf v_j = \lambda_j\mathbf v_j$:

$$ A\mathbf v_1 = \begin{pmatrix} -2 & 2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} = 0\mathbf v_1, \qquad A\mathbf v_2 = \begin{pmatrix} -2 & 2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} -6 \\ 3 \end{pmatrix} = (-3)\mathbf v_2 $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = \begin{pmatrix} 0 & -6 \\ 0 & 3 \end{pmatrix} $$

Now multiply by $Q^{-1}$ on the left, entry by entry:

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{1}{3}\cdot0 + \frac{2}{3}\cdot0 = 0 \\ (Q^{-1}AQ)_{12} &= \frac{1}{3}\cdot(-6) + \frac{2}{3}\cdot3 = 0 \\ (Q^{-1}AQ)_{21} &= \frac{1}{3}\cdot0 + (- \frac{1}{3})\cdot0 = 0 \\ (Q^{-1}AQ)_{22} &= \frac{1}{3}\cdot(-6) + (- \frac{1}{3})\cdot3 = -3 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 0 & 0 \\ 0 & -3 \end{pmatrix} = \Lambda = \begin{pmatrix} 0 & 0 \\ 0 & -3 \end{pmatrix} $$

The transformation has decoupled the system (the matrix is diagonal), as claimed.

#### Solution in the canonical plane

$$ \dot z_1 = 0, \qquad \dot z_2 = -3z_2 $$

Each equation is separable. If $z_i \neq 0$, $\frac{dz_i}{z_i} = \lambda_i\,dt$ and integrating, $\ln|z_i| = \lambda_i t + C_i$, so $z_i = c_i e^{\lambda_i t}$ with $c_i = \pm e^{C_i}$ (the solution $z_i \equiv 0$ corresponds to $c_i = 0$). Equivalently, $\frac{d}{dt}(e^{-\lambda_i t}z_i) = 0$.

$$ z_1(t) = c_1 e^{0t}, \qquad z_2(t) = c_2 e^{-3t} $$

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf v_1 + z_2\mathbf v_2$, so the general solution is

$$ \mathbf x(t) = c_1 e^{0t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2 e^{-3t}\begin{pmatrix} 2 \\ -1 \end{pmatrix} $$

$$ x(t) = c_{1} + 2 c_{2} e^{-3 t}, \qquad y(t) = c_{1} - c_{2} e^{-3 t} $$

#### Phase portrait

One eigenvalue is zero and the other is $\lambda_2 = -3 \neq 0$. In the canonical plane $\dot z_1 = 0$, so $z_1$ is constant along every solution (Topic 4, case $\lambda = 0$).

Every point of the line through $\mathbf v_1 = (1, 1)$ is an equilibrium, because $A\mathbf v_1 = \mathbf 0$. Every other solution moves on a straight line parallel to $\mathbf v_2 = (2, -1)$ with $\mathbf x - \mathbf x_{eq} \propto e^{-3t}$: it approaches the line of equilibria as $t \to +\infty$ (the equilibria are stable but each orbit ends at a different point). The arrows point towards the line of equilibria.

![[attachments/AM-PS/ch4a-e11-iii-z.svg]]
*Canonical $\mathbf z$-plane: the line of equilibria (green) and the trajectories parallel to the other axis.*

![[attachments/AM-PS/ch4a-e11-iii-x.svg]]
*Original $(x, y)$-plane: equilibria on the line through $(1, 1)$ (green); trajectories parallel to $(2, -1)$, towards that line.*

## Phase 4: Interpretation and checks

- (iii): $\operatorname{tr}A = -3$ and $\det A = (-2)(-1) - 2\cdot 1 = 0$, so the eigenvalues are $0$ and $-3$: the general solution is $\mathbf x = c_1(1, 1)^T + c_2e^{-3t}(2, -1)^T$, every orbit converges to the equilibrium $c_1(1, 1)^T$, i.e. $\mathbf x(t) \to \mathbf x_\infty$ on the line $y = x$ along the direction $(2, -1)$.
- Explicit limit for $\mathbf x(0) = (x_0, y_0)$: $\mathbf x_\infty = c_1(1, 1)^T$ with $c_1 = (x_0 + 2y_0)/3$ (from $Q^{-1}$ computed above, first row $(\tfrac13, \tfrac23)$). Example: $\mathbf x(0) = (2, -1)$ gives $c_1 = 0$ and the orbit is the line $\mathbf x = e^{-3t}(2, -1)$ going to the origin.
- The origin is no longer an isolated equilibrium: the node/saddle/spiral classification of Topic 4 Sec. 9 assumes $\det A \neq 0$ (see the trace-determinant discussion), and here $\det A = 0$, which is the borderline between a stable node ($\lambda_2 < 0$) and a saddle.
- Conserved quantity: the combination $\tilde x = c_1$ is a first integral of the motion ($x + 2y$ in (iii), up to the factor $\tfrac13$): $\frac{d}{dt}(x + 2y) = (-2x + 2y) + 2(x - y) = 0$ $\checkmark$.
