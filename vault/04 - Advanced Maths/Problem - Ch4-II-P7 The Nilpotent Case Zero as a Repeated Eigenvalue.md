---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 7"
dificultad: media
id: "e7"
pill: "Nilpotent Matrix • Shear • Line of Equilibria"
tags:
  - problema-resuelto
  - matriz-nilpotente
  - autovalor-cero
  - retrato-de-fase
---

# Problem 4.II.7: The Nilpotent Case: Zero as a Repeated Eigenvalue

> Official exercise 7 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Suppose that a non-zero matrix $A$ has zero as a repeated eigenvalue, with eigenvector $\mathbf v$. Then we can change to coordinates referred to $\mathbf v_2$ and $\mathbf v_1 = A\mathbf v_2$, where $\mathbf v_2$ is any vector in a different direction to $\mathbf v$, so that $\tilde{\mathbf x} = \tilde x\mathbf v_1 + \tilde y\mathbf v_2$. The equation $d\mathbf x/dt = A\mathbf x$ becomes $\dfrac{d\tilde{\mathbf x}}{dt} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\tilde{\mathbf x}$, hence,

$$ \frac{d\tilde x}{dt} = \tilde y \quad\text{and}\quad \frac{d\tilde y}{dt} = 0. $$

- (i) Solve the equations for $\tilde x(t)$ and $\tilde y(t)$, and hence write down the general solution for $\mathbf x(t)$.
- (ii) Draw the phase diagram in the $(\tilde x, \tilde y)$ and $(x, y)$ planes.
- (iii) Draw the phase diagram for the equation $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}\mathbf x$.

## Phase 1: Setup and hypotheses

$A \neq O$ is $2\times 2$ with the double eigenvalue $0$: $\operatorname{tr}A = 0$, $\det A = 0$, so by Cayley-Hamilton $A^2 = O$ ($A^2 - (\operatorname{tr}A)A + (\det A)I = O$). Since $A \neq O$, $\ker A$ is one-dimensional, spanned by $\mathbf v$: $m_g = 1$ (Topic 4 Sec. 8.4 with $\lambda = 0$, $N = A$).

Why the proposed basis works: take $\mathbf v_2 \notin \operatorname{span}\{\mathbf v\}$. Then $A\mathbf v_2 \neq \mathbf 0$ (otherwise $\mathbf v_2$ would be in $\ker A$), and $\mathbf v_1 = A\mathbf v_2$ satisfies $A\mathbf v_1 = A^2\mathbf v_2 = \mathbf 0$, so $\mathbf v_1 \in \ker A = \operatorname{span}\{\mathbf v\}$ and $\mathbf v_1 \neq \mathbf 0$ is an eigenvector. $\mathbf v_1, \mathbf v_2$ are independent (not parallel), and

$$ A\mathbf v_1 = \mathbf 0 = 0\cdot\mathbf v_1 + 0\cdot\mathbf v_2, \qquad A\mathbf v_2 = \mathbf v_1 = 1\cdot\mathbf v_1 + 0\cdot\mathbf v_2 \;\Longrightarrow\; Q^{-1}AQ = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} $$

## Phase 2: Formulation

With $Q = [\mathbf v_1 \mid \mathbf v_2]$ and $\mathbf x = Q\tilde{\mathbf x} = \tilde x\mathbf v_1 + \tilde y\mathbf v_2$ the canonical system is $\dot{\tilde x} = \tilde y$, $\dot{\tilde y} = 0$ (the Jordan block of Topic 4 Eq. 8.3 with $\lambda = 0$).

> [!info] Method of the class notes [Notes, p. 10]
> Case 3.2 of the notes with $\lambda = 0$: $\mathbf v_1 = (A - 0I)\mathbf v_2 = A\mathbf v_2$, exactly the change of coordinates of the statement. The solution of the notes becomes $z_2 = C$, $z_1 = Ct + D$ and $\mathbf x = (Ct + D)\mathbf v_1 + C\mathbf v_2$: horizontal lines in the $\tilde{\mathbf x}$-plane, with the line of $\mathbf v_1$ ($C = 0$) made of equilibria.

## Phase 3: Derivation

### (i) Solution

The second equation $\dot{\tilde y} = 0$ integrates to $\tilde y(t) = c_2$ (a constant). Substituting in the first, $\dot{\tilde x} = c_2$, and Barrow's rule between $0$ and $t$ gives $\tilde x(t) - \tilde x(0) = \int_0^t c_2\,ds = c_2t$:

$$ \tilde x(t) = c_1 + c_2t, \qquad \tilde y(t) = c_2 \qquad (c_1 = \tilde x(0),\ c_2 = \tilde y(0)) $$

Back to the original coordinates, $\mathbf x = \tilde x\mathbf v_1 + \tilde y\mathbf v_2$:

$$ \boxed{\mathbf x(t) = (c_1 + c_2t)\,\mathbf v_1 + c_2\,\mathbf v_2} $$

Check: $\dot{\mathbf x} = c_2\mathbf v_1$ and $A\mathbf x = (c_1 + c_2t)A\mathbf v_1 + c_2A\mathbf v_2 = \mathbf 0 + c_2\mathbf v_1$. They agree. Unlike the case $\lambda \neq 0$ there is no exponential: the secular term grows only **linearly**.

### (ii) Phase diagrams

In the $(\tilde x, \tilde y)$ plane the orbits are the **horizontal lines** $\tilde y = c_2$ (since $\tilde y$ is constant). On the line $\tilde y = c_2 > 0$ the abscissa $\tilde x = c_1 + c_2t$ increases at constant speed $c_2$: motion to the right; for $c_2 < 0$ to the left. The $\tilde x$-axis ($c_2 = 0$) consists of equilibria. There are no curved orbits: the speed is proportional to the height $\tilde y$ (a *shear* flow).

![[attachments/AM-PS/ch4b-e7-ii-z.svg]]
*$(\tilde x, \tilde y)$-plane: horizontal lines $\tilde y = c_2$ traversed to the right above the axis and to the left below it; the $\tilde x$-axis is all equilibria.*

In the $(x, y)$ plane, $\mathbf x = \tilde x\mathbf v_1 + \tilde y\mathbf v_2$ maps horizontal lines to **lines parallel to $\mathbf v_1$**, offset from the line $\operatorname{span}\{\mathbf v_1\}$ of equilibria by $c_2\mathbf v_2$; they are traversed along $+\mathbf v_1$ on the side of $\operatorname{span}\{\mathbf v_1\}$ where $\mathbf v_2$ points and along $-\mathbf v_1$ on the other side. The $(x, y)$-diagram of the following item shows a concrete example.

### (iii) The matrix $\begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}$

$\operatorname{tr}A = -1 + 1 = 0$ and $\det A = (-1)(1) - (1)(-1) = 0$, so the characteristic equation is $\lambda^2 = 0$: the double eigenvalue $0$, and $A \neq O$. Check $A^2 = O$:

$$ \begin{aligned} (A^2)_{11} &= (-1)\cdot(-1) + 1\cdot(-1) = 0 \\ (A^2)_{12} &= (-1)\cdot1 + 1\cdot1 = 0 \\ (A^2)_{21} &= (-1)\cdot(-1) + 1\cdot(-1) = 0 \\ (A^2)_{22} &= (-1)\cdot1 + 1\cdot1 = 0 \end{aligned} $$

Eigenvector: $A\mathbf v = \mathbf 0$ gives $-v_1 + v_2 = 0$ (both rows are the same equation up to sign), so $\mathbf v = (1, 1)^T$. Following the exercise, take any $\mathbf v_2$ not parallel to $\mathbf v$, for instance $\mathbf v_2 = (1, 0)^T$, and set $\mathbf v_1 = A\mathbf v_2$:

$$ \mathbf v_1 = A\mathbf v_2 = \begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} -1 \\ -1 \end{pmatrix} $$

$\mathbf v_1 = (-1, -1)^T$ is indeed an eigenvector ($A\mathbf v_1 = (1 - 1, 1 - 1)^T = \mathbf 0$), a multiple of $\mathbf v$.

$$ Q = [\mathbf v_1 \mid \mathbf v_2] = \begin{pmatrix} -1 & 1 \\ -1 & 0 \end{pmatrix} $$

$\det Q = (-1)(0) - (1)(-1) = 1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{1}\begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix} $$

$$ AQ = [A\mathbf v_1 \mid A\mathbf v_2] = [\mathbf 0 \mid \mathbf v_1] = \begin{pmatrix} 0 & -1 \\ 0 & -1 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 0\cdot0 + (-1)\cdot0 = 0 \\ (Q^{-1}AQ)_{12} &= 0\cdot(-1) + (-1)\cdot(-1) = 1 \\ (Q^{-1}AQ)_{21} &= 1\cdot0 + (-1)\cdot0 = 0 \\ (Q^{-1}AQ)_{22} &= 1\cdot(-1) + (-1)\cdot(-1) = 0 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} $$

By part (i) the general solution is $\mathbf x(t) = (c_1 + c_2t)\mathbf v_1 + c_2\mathbf v_2$:

$$ x(t) = - c_{1} - c_{2} t + c_{2}, \qquad y(t) = - c_{1} - c_{2} t $$

Check: $\dot x = - c_{2}$ and $-x + y = - c_{2}$; $\dot y = - c_{2}$ and $-x + y$ again: both equations $\dot x = -x + y$, $\dot y = -x + y$ hold.

The coordinates are $\tilde{\mathbf x} = Q^{-1}\mathbf x$: $\tilde x = -y$, $\tilde y = x - y$ (first row $(0, -1)$, second row $(1, -1)$ of $Q^{-1}$). Every orbit is a straight line parallel to $\mathbf v = (1, 1)$; the line $y = x$ ($\tilde y = 0$) consists of equilibria.

Direction: $\dot{\mathbf x} = (y - x)(1, 1)^T$. Above the line $y = x$ ($y > x$) the motion is along $+(1, 1)$ (up and to the right); below it, along $-(1, 1)$ (down and to the left). The speed $|y - x|\sqrt2$ grows with the distance to the line of equilibria.

#### Phase portrait

$\lambda = 0$: every point of the eigenline through $\mathbf v_1 = (-1, -1)$ is an equilibrium. In the $\mathbf z$-plane $z_2 = c_2$ is constant and $z_1 = c_1 + c_2t$ moves with constant speed $c_2$: horizontal lines, to the right if $z_2 > 0$ and to the left if $z_2 < 0$. Under $\mathbf x = Q\mathbf z$ they become lines parallel to $\mathbf v_1$: on the side of the eigenline where $\mathbf v_2$ points (for $z_2 > 0$) they are traversed along $+\mathbf v_1$, on the opposite side along $-\mathbf v_1$.

Orientation in the $\mathbf x$-plane, from $N\mathbf x = (A - \lambda I)\mathbf x = z_2\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = \begin{pmatrix} 1 \\ 1 \end{pmatrix} = -1\,\mathbf v_1$, so there the orbit drifts along $-\mathbf v_1$. The orbits are the straight lines parallel to $\mathbf v_1$.

![[attachments/AM-PS/ch4b-e7-iii-z.svg]]
*Canonical $\mathbf z$-plane (line of equilibria (nilpotent shear)).*

![[attachments/AM-PS/ch4b-e7-iii-x.svg]]
*Original $(x, y)$-plane (line of equilibria (nilpotent shear)); dashed: the eigenline with $\mathbf v_1 = (-1, -1)$.*

## Phase 4: Interpretation and checks

- This is the limit $\lambda \to 0$ of the improper node $J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$: the factor $e^{\lambda t}$ disappears and only the shear remains (the origin of the trace-determinant plane): the flow is $\mathbf x(t) = \mathbf x_0 + t\,A\mathbf x_0$ (the series of $e^{At}$ stops after the linear term because $A^2 = O$): in (iii), $\mathbf x(t) = \mathbf x_0 + t(y_0 - x_0)(1, 1)^T$, which matches the direction and speed found.
- Check at a point: $\mathbf x_0 = (1, 0)$: formula gives $\mathbf x(t) = (1, 0) + t(0 - 1)(1, 1) = (1 - t, -t)$, and the general solution with $c_2 = \tilde y(0) = x_0 - y_0 = 1$, $c_1 = \tilde x(0) = -y_0 = 0$ gives $x = -(0 + t)(1) + 1 = 1 - t$ and $y = -t$. They coincide.
- $\operatorname{tr}A = \det A = 0$ is the origin of the trace-determinant plane (Topic 4 Sec. 9.1), where all the portrait types meet.
- The solutions are polynomials in $t$, so every orbit not on the line of equilibria leaves to infinity linearly in time in both directions.
