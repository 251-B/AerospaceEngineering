---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 2"
dificultad: media
id: "e2"
pill: "Competition • Predator-Prey • Seven Systems"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.2: Seven Two-Species Population Models

> Official exercise 2 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

For each of the following models of two population species, describe first the type of situation being modelled, then find the stationary points, determine their stability type and sketch the phase portrait for $x, y \ge 0$. Decide what the phase portrait means for the evolution of the two species.

(i) $\dot x = x(2 - x - y)$, $\dot y = y(2 - 2y - 2x)$,

(ii) $\dot x = x(2 - x - y)$, $\dot y = y(2 - 2y - x/4)$,

(iii) $\dot x = x(2 - x - 3y)$, $\dot y = y(2 - 2y - 3x)$,

(iv) $\dot x = x(1 - 2y)$, $\dot y = y(-2 + 3x)$,

(v) $\dot x = x(4 - x/2 - 3y)$, $\dot y = y(-2 + x)$,

(vi) $\dot x = x(10 - x - 3y)$, $\dot y = y(1 + x - 10y)$,

(vii) $\dot x = x(3 - x - y)$, $\dot y = y(-2 + x)$.

## Setting up the system

We begin by identifying the ecological interaction represented by each model from the signs of the intrinsic growth rates, self-limitation (logistic) terms, and cross-interaction terms. In all seven systems, $x = 0$ implies $\dot x = 0$ and $y = 0$ implies $\dot y = 0$, so the coordinate axes are invariant manifolds and the biologically meaningful first quadrant $x \ge 0, y \ge 0$ is positively invariant.

### (i) Asymmetric competition (species $x$ dominant)

In $\dot x = x(2 - x - y)$ and $\dot y = y(2 - 2y - 2x)$, both species grow logistically in isolation (carrying capacities $K_x = 2$ and $K_y = 1$), and each cross-term is negative ($-xy$ and $-2xy$). Hence this models **interspecific competition** for a shared resource.

### (ii) Weak competition

In $\dot x = x(2 - x - y)$ and $\dot y = y(2 - 2y - x/4)$, both species again have positive intrinsic growth rates and logistic self-regulation ($K_x = 2$, $K_y = 1$), with negative cross-terms ($-xy$ and $-xy/4$). This is a **weak competition** model in which interspecific inhibition is smaller than intraspecific self-limitation.

### (iii) Strong competition

In $\dot x = x(2 - x - 3y)$ and $\dot y = y(2 - 2y - 3x)$, both species grow logistically alone ($K_x = 2$, $K_y = 1$), but both cross-terms are large and negative ($-3xy$). This models **strong competition**, where each species inhibits its competitor more strongly than itself.

### (iv) Classical Lotka–Volterra predator–prey

In $\dot x = x(1 - 2y)$ and $\dot y = y(-2 + 3x)$, species $x$ grows exponentially in the absence of $y$ ($\dot x = x$) and is harmed by $y$ ($-2xy$), whereas species $y$ decays exponentially without $x$ ($\dot y = -2y$) and benefits from $x$ ($+3xy$). Thus $x$ is the **prey** and $y$ is the **predator** in the classical Lotka–Volterra model without carrying capacity.

### (v) Predator–prey with logistic prey ($K = 8$)

In $\dot x = x(4 - x/2 - 3y)$ and $\dot y = y(-2 + x)$, the prey $x$ obeys logistic growth with carrying capacity $K_x = 8$ in the absence of predators, while the predator $y$ dies out exponentially without prey and grows proportionally to $xy$. This is a **predator–prey model with logistic prey**.

### (vi) Logistic prey and logistic predator with alternative food source

In $\dot x = x(10 - x - 3y)$ and $\dot y = y(1 + x - 10y)$, species $x$ is harmed by $y$ ($-3xy$) and has carrying capacity $K_x = 10$ alone, whereas species $y$ benefits from $x$ ($+xy$) and still has a positive intrinsic growth rate $+1$ with carrying capacity $K_y = 1/10$ when $x = 0$. This models a **prey ($x$) and a generalist predator ($y$) that has an alternative food source** and logistic self-regulation.

### (vii) Predator–prey with logistic prey ($K = 3$)

In $\dot x = x(3 - x - y)$ and $\dot y = y(-2 + x)$, the prey $x$ grows logistically up to carrying capacity $K_x = 3$ alone, while the specialist predator $y$ decays without $x$ and benefits from $x$. This is again a **predator–prey model with logistic prey**.

## Step 1: Critical points

We find all stationary points $(x^*, y^*)$ in the first quadrant $x \ge 0, y \ge 0$ for each system by solving $\dot x = 0$ and $\dot y = 0$ simultaneously.

### (i) Critical points of $\dot x = x(2 - x - y)$, $\dot y = y(2 - 2y - 2x)$

Setting $x(2 - x - y) = 0$ and $y(2 - 2y - 2x) = 0$ yields four factor combinations:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $x = 0$, $2 - 2y = 0 \implies y = 1 \implies B(0, 1)$.
3. $y = 0$, $2 - x = 0 \implies x = 2 \implies C(2, 0)$.
4. $2 - x - y = 0$ and $2 - 2y - 2x = 0$: dividing the second equation by $2$ gives $x + y = 1$, which contradicts $x + y = 2$. These lines are parallel, so there is **no fourth (interior) stationary point**.

### (ii) Critical points of $\dot x = x(2 - x - y)$, $\dot y = y(2 - 2y - x/4)$

Setting $x(2 - x - y) = 0$ and $y(2 - 2y - x/4) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $x = 0$, $2 - 2y = 0 \implies y = 1 \implies B(0, 1)$.
3. $y = 0$, $2 - x = 0 \implies x = 2 \implies C(2, 0)$.
4. Interior equilibrium: solve $x + y = 2$ and $\frac{1}{4}x + 2y = 2$. From the first, $x = 2 - y$; substituting into the second gives
   $$
   \frac{2 - y}{4} + 2y = 2 \;\Longrightarrow\; 2 - y + 8y = 8 \;\Longrightarrow\; 7y = 6 \;\Longrightarrow\; y^* = \frac{6}{7}, \qquad x^* = 2 - \frac{6}{7} = \frac{8}{7}.
   $$
   Hence $D\bigl(\tfrac{8}{7}, \tfrac{6}{7}\bigr)$, which lies in the first quadrant.

### (iii) Critical points of $\dot x = x(2 - x - 3y)$, $\dot y = y(2 - 2y - 3x)$

Setting $x(2 - x - 3y) = 0$ and $y(2 - 2y - 3x) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $x = 0$, $2 - 2y = 0 \implies y = 1 \implies B(0, 1)$.
3. $y = 0$, $2 - x = 0 \implies x = 2 \implies C(2, 0)$.
4. Interior equilibrium: solve $x + 3y = 2$ and $3x + 2y = 2$. From the first, $x = 2 - 3y$; substituting into the second yields
   $$
   3(2 - 3y) + 2y = 2 \;\Longrightarrow\; 6 - 7y = 2 \;\Longrightarrow\; y^* = \frac{4}{7}, \qquad x^* = 2 - \frac{12}{7} = \frac{2}{7}.
   $$
   Hence $D\bigl(\tfrac{2}{7}, \tfrac{4}{7}\bigr)$ in the first quadrant.

### (iv) Critical points of $\dot x = x(1 - 2y)$, $\dot y = y(-2 + 3x)$

Setting $x(1 - 2y) = 0$ and $y(-2 + 3x) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $x = 0$, $-2 + 3(0) = -2 \neq 0 \implies$ no other point on $x = 0$.
3. $y = 0$, $1 - 2(0) = 1 \neq 0 \implies$ no other point on $y = 0$.
4. $1 - 2y = 0$ and $-2 + 3x = 0 \implies x^* = \frac{2}{3}$, $y^* = \frac{1}{2} \implies B\bigl(\tfrac{2}{3}, \tfrac{1}{2}\bigr)$.

### (v) Critical points of $\dot x = x(4 - x/2 - 3y)$, $\dot y = y(-2 + x)$

Setting $x(4 - x/2 - 3y) = 0$ and $y(-2 + x) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $y = 0$, $4 - x/2 = 0 \implies x = 8 \implies B(8, 0)$.
3. $x = 0$ forces $-2 + 0 = -2 \neq 0$, so no non-zero equilibrium on $x = 0$.
4. $-2 + x = 0 \implies x^* = 2$; substituting into $4 - x/2 - 3y = 0$ gives $4 - 1 - 3y = 0 \implies y^* = 1 \implies C(2, 1)$.

### (vi) Critical points of $\dot x = x(10 - x - 3y)$, $\dot y = y(1 + x - 10y)$

Setting $x(10 - x - 3y) = 0$ and $y(1 + x - 10y) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $y = 0$, $10 - x = 0 \implies x = 10 \implies B(10, 0)$.
3. $x = 0$, $1 - 10y = 0 \implies y = \frac{1}{10} \implies C\bigl(0, \tfrac{1}{10}\bigr)$.
4. Interior equilibrium: solve $x + 3y = 10$ and $-x + 10y = 1$. Adding the two equations gives
   $$
   13y = 11 \;\Longrightarrow\; y^* = \frac{11}{13}, \qquad x^* = 10 - \frac{33}{13} = \frac{97}{13}.
   $$
   Hence $D\bigl(\tfrac{97}{13}, \tfrac{11}{13}\bigr)$ in the first quadrant.

### (vii) Critical points of $\dot x = x(3 - x - y)$, $\dot y = y(-2 + x)$

Setting $x(3 - x - y) = 0$ and $y(-2 + x) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $y = 0$, $3 - x = 0 \implies x = 3 \implies B(3, 0)$.
3. $-2 + x = 0 \implies x^* = 2$; substituting into $3 - x - y = 0$ gives $3 - 2 - y = 0 \implies y^* = 1 \implies C(2, 1)$.

## Step 2: Linearization

We compute the Jacobian matrix $J(x,y) = \begin{pmatrix} \partial f/\partial x & \partial f/\partial y \\ \partial g/\partial x & \partial g/\partial y \end{pmatrix}$ explicitly for each system and evaluate it at every stationary point.

### (i) Jacobian matrices

With $f(x,y) = 2x - x^2 - xy$ and $g(x,y) = 2y - 2y^2 - 2xy$:

$$
\frac{\partial f}{\partial x} = 2 - 2x - y, \quad \frac{\partial f}{\partial y} = -x, \quad \frac{\partial g}{\partial x} = -2y, \quad \frac{\partial g}{\partial y} = 2 - 4y - 2x.
$$

Evaluating at $A(0,0)$, $B(0,1)$, and $C(2,0)$:

$$
J(0,0) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \qquad J(0,1) = \begin{pmatrix} 1 & 0 \\ -2 & -2 \end{pmatrix}, \qquad J(2,0) = \begin{pmatrix} -2 & -2 \\ 0 & -2 \end{pmatrix}.
$$

### (ii) Jacobian matrices

With $f(x,y) = 2x - x^2 - xy$ and $g(x,y) = 2y - 2y^2 - \frac{1}{4}xy$:

$$
\frac{\partial f}{\partial x} = 2 - 2x - y, \quad \frac{\partial f}{\partial y} = -x, \quad \frac{\partial g}{\partial x} = -\frac{1}{4}y, \quad \frac{\partial g}{\partial y} = 2 - 4y - \frac{1}{4}x.
$$

Evaluating at $A(0,0)$, $B(0,1)$, $C(2,0)$, and $D\bigl(\tfrac{8}{7}, \tfrac{6}{7}\bigr)$:

$$
J(0,0) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \qquad J(0,1) = \begin{pmatrix} 1 & 0 \\ -\frac{1}{4} & -2 \end{pmatrix}, \qquad J(2,0) = \begin{pmatrix} -2 & -2 \\ 0 & \frac{3}{2} \end{pmatrix},
$$

$$
J\!\left(\frac{8}{7}, \frac{6}{7}\right) = \begin{pmatrix} 2 - \frac{16}{7} - \frac{6}{7} & -\frac{8}{7} \\ -\frac{6}{28} & 2 - \frac{24}{7} - \frac{2}{7} \end{pmatrix} = \begin{pmatrix} -\frac{8}{7} & -\frac{8}{7} \\ -\frac{3}{14} & -\frac{12}{7} \end{pmatrix}.
$$

### (iii) Jacobian matrices

With $f(x,y) = 2x - x^2 - 3xy$ and $g(x,y) = 2y - 2y^2 - 3xy$:

$$
\frac{\partial f}{\partial x} = 2 - 2x - 3y, \quad \frac{\partial f}{\partial y} = -3x, \quad \frac{\partial g}{\partial x} = -3y, \quad \frac{\partial g}{\partial y} = 2 - 4y - 3x.
$$

Evaluating at $A(0,0)$, $B(0,1)$, $C(2,0)$, and $D\bigl(\tfrac{2}{7}, \tfrac{4}{7}\bigr)$:

$$
J(0,0) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \qquad J(0,1) = \begin{pmatrix} -1 & 0 \\ -3 & -2 \end{pmatrix}, \qquad J(2,0) = \begin{pmatrix} -2 & -6 \\ 0 & -4 \end{pmatrix},
$$

$$
J\!\left(\frac{2}{7}, \frac{4}{7}\right) = \begin{pmatrix} 2 - \frac{4}{7} - \frac{12}{7} & -\frac{6}{7} \\ -\frac{12}{7} & 2 - \frac{16}{7} - \frac{6}{7} \end{pmatrix} = \begin{pmatrix} -\frac{2}{7} & -\frac{6}{7} \\ -\frac{12}{7} & -\frac{8}{7} \end{pmatrix}.
$$

### (iv) Jacobian matrices

With $f(x,y) = x - 2xy$ and $g(x,y) = -2y + 3xy$:

$$
\frac{\partial f}{\partial x} = 1 - 2y, \quad \frac{\partial f}{\partial y} = -2x, \quad \frac{\partial g}{\partial x} = 3y, \quad \frac{\partial g}{\partial y} = -2 + 3x.
$$

Evaluating at $A(0,0)$ and $B\bigl(\tfrac{2}{3}, \tfrac{1}{2}\bigr)$:

$$
J(0,0) = \begin{pmatrix} 1 & 0 \\ 0 & -2 \end{pmatrix}, \qquad J\!\left(\frac{2}{3}, \frac{1}{2}\right) = \begin{pmatrix} 0 & -\frac{4}{3} \\ \frac{3}{2} & 0 \end{pmatrix}.
$$

### (v) Jacobian matrices

With $f(x,y) = 4x - \frac{1}{2}x^2 - 3xy$ and $g(x,y) = -2y + xy$:

$$
\frac{\partial f}{\partial x} = 4 - x - 3y, \quad \frac{\partial f}{\partial y} = -3x, \quad \frac{\partial g}{\partial x} = y, \quad \frac{\partial g}{\partial y} = -2 + x.
$$

Evaluating at $A(0,0)$, $B(8,0)$, and $C(2,1)$:

$$
J(0,0) = \begin{pmatrix} 4 & 0 \\ 0 & -2 \end{pmatrix}, \qquad J(8,0) = \begin{pmatrix} -4 & -24 \\ 0 & 6 \end{pmatrix}, \qquad J(2,1) = \begin{pmatrix} -1 & -6 \\ 1 & 0 \end{pmatrix}.
$$

### (vi) Jacobian matrices

With $f(x,y) = 10x - x^2 - 3xy$ and $g(x,y) = y + xy - 10y^2$:

$$
\frac{\partial f}{\partial x} = 10 - 2x - 3y, \quad \frac{\partial f}{\partial y} = -3x, \quad \frac{\partial g}{\partial x} = y, \quad \frac{\partial g}{\partial y} = 1 + x - 20y.
$$

Evaluating at $A(0,0)$, $B(10,0)$, $C\bigl(0, \tfrac{1}{10}\bigr)$, and $D\bigl(\tfrac{97}{13}, \tfrac{11}{13}\bigr)$:

$$
J(0,0) = \begin{pmatrix} 10 & 0 \\ 0 & 1 \end{pmatrix}, \qquad J(10,0) = \begin{pmatrix} -10 & -30 \\ 0 & 11 \end{pmatrix}, \qquad J\!\left(0, \frac{1}{10}\right) = \begin{pmatrix} \frac{97}{10} & 0 \\ \frac{1}{10} & -1 \end{pmatrix},
$$

$$
J\!\left(\frac{97}{13}, \frac{11}{13}\right) = \begin{pmatrix} -\frac{97}{13} & -\frac{291}{13} \\ \frac{11}{13} & -\frac{110}{13} \end{pmatrix}.
$$

### (vii) Jacobian matrices

With $f(x,y) = 3x - x^2 - xy$ and $g(x,y) = -2y + xy$:

$$
\frac{\partial f}{\partial x} = 3 - 2x - y, \quad \frac{\partial f}{\partial y} = -x, \quad \frac{\partial g}{\partial x} = y, \quad \frac{\partial g}{\partial y} = -2 + x.
$$

Evaluating at $A(0,0)$, $B(3,0)$, and $C(2,1)$:

$$
J(0,0) = \begin{pmatrix} 3 & 0 \\ 0 & -2 \end{pmatrix}, \qquad J(3,0) = \begin{pmatrix} -3 & -3 \\ 0 & 1 \end{pmatrix}, \qquad J(2,1) = \begin{pmatrix} -2 & -2 \\ 1 & 0 \end{pmatrix}.
$$

## Step 3: Local study

We compute the characteristic polynomial $\det(J - \lambda I) = 0$ and solve $(J - \lambda I)\vec v = \vec 0$ row by row at every stationary point to classify each equilibrium.

### (i) Local classification

- **$A(0,0)$:** $J(0,0) = 2I$, so $(2 - \lambda)^2 = 0 \implies \lambda_1 = \lambda_2 = 2 > 0$ with two linearly independent eigenvectors $\vec v_1 = (1,0)^T$, $\vec v_2 = (0,1)^T$. **Unstable star.**
- **$B(0,1)$:** Lower triangular, so $(1 - \lambda)(-2 - \lambda) = 0 \implies \lambda_1 = 1 > 0$, $\lambda_2 = -2 < 0$. **Saddle point.**
  - For $\lambda_1 = 1$: $\begin{pmatrix} 0 & 0 \\ -2 & -3 \end{pmatrix}\vec v_1 = \vec 0 \implies -2v_1 - 3v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$.
  - For $\lambda_2 = -2$: $\begin{pmatrix} 3 & 0 \\ -2 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies v_1 = 0 \implies \vec v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
- **$C(2,0)$:** Upper triangular, so $(-2 - \lambda)^2 = 0 \implies \lambda_1 = \lambda_2 = -2 < 0$. Solving $(J(2,0) + 2I)\vec v = \vec 0$:
  $$
  \begin{pmatrix} 0 & -2 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \;\Longrightarrow\; -2v_2 = 0 \;\Longrightarrow\; v_2 = 0.
  $$
  There is only one independent eigenvector $\vec v = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, so $C(2,0)$ is a **stable improper (degenerate) node**, tangent to the $x$-axis.

> [!warning] Discrepancy with the official solution
> In `Solved_exer_nonlinear_system.pdf` (p. 2), the handwritten solution writes $J(2,0) = \begin{pmatrix} -2 & 0 \\ 0 & -2 \end{pmatrix}$ and classifies $C(2,0)$ as a "stable star". That is an algebraic slip in entry $(1,2)$: $\frac{\partial f}{\partial y} = -x$, which evaluates to $-2$ (not $0$) at $(2,0)$. The correct matrix is $\begin{pmatrix} -2 & -2 \\ 0 & -2 \end{pmatrix}$, making $C(2,0)$ a **stable improper node** with single eigenvector $(1,0)^T$. Because both eigenvalues are still $-2 < 0$, the local asymptotic stability and the global biological outcome ($x \to 2$, $y \to 0$) are completely unaffected.

### (ii) Local classification

- **$A(0,0)$:** $J(0,0) = 2I \implies \lambda_1 = \lambda_2 = 2 > 0$, two independent eigenvectors $(1,0)^T, (0,1)^T$. **Unstable star.**
- **$B(0,1)$:** $(1 - \lambda)(-2 - \lambda) = 0 \implies \lambda_1 = 1 > 0$, $\lambda_2 = -2 < 0$. **Saddle point.**
  - For $\lambda_1 = 1$: $\begin{pmatrix} 0 & 0 \\ -1/4 & -3 \end{pmatrix}\vec v_1 = \vec 0 \implies -\frac{1}{4}v_1 - 3v_2 = 0 \implies v_1 = -12v_2 \implies \vec v_1 = \begin{pmatrix} 12 \\ -1 \end{pmatrix}$.
  - For $\lambda_2 = -2$: $\begin{pmatrix} 3 & 0 \\ -1/4 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies v_1 = 0 \implies \vec v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
- **$C(2,0)$:** $(-2 - \lambda)\bigl(\frac{3}{2} - \lambda\bigr) = 0 \implies \lambda_1 = -2 < 0$, $\lambda_2 = \frac{3}{2} > 0$. **Saddle point.**
  - For $\lambda_1 = -2$: $\begin{pmatrix} 0 & -2 \\ 0 & 7/2 \end{pmatrix}\vec v_1 = \vec 0 \implies v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
  - For $\lambda_2 = \frac{3}{2}$: $\begin{pmatrix} -7/2 & -2 \\ 0 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies -\frac{7}{2}v_1 - 2v_2 = 0 \implies \vec v_2 = \begin{pmatrix} -4 \\ 7 \end{pmatrix}$.
- **$D\bigl(\tfrac{8}{7}, \tfrac{6}{7}\bigr)$:** Expanding $\det(J - \lambda I) = 0$:
  $$
  \left(-\frac{8}{7} - \lambda\right)\left(-\frac{12}{7} - \lambda\right) - \left(-\frac{8}{7}\right)\left(-\frac{3}{14}\right) = \lambda^2 + \frac{20}{7}\lambda + \frac{96}{49} - \frac{12}{49} = \lambda^2 + \frac{20}{7}\lambda + \frac{12}{7} = 0.
  $$
  Multiplying by $7$ gives $7\lambda^2 + 20\lambda + 12 = (7\lambda + 6)(\lambda + 2) = 0$, so $\lambda_1 = -\frac{6}{7} < 0$ and $\lambda_2 = -2 < 0$. **Stable node.**
  - For $\lambda_1 = -\frac{6}{7}$: $\begin{pmatrix} -2/7 & -8/7 \\ -3/14 & -6/7 \end{pmatrix}\vec v_1 = \vec 0$. Row 1 gives $-2v_1 - 8v_2 = 0 \implies v_1 = -4v_2$ (Row 2 gives $-\frac{3}{14}(-4v_2) - \frac{6}{7}v_2 = 0$, consistent), so $\vec v_1 = \begin{pmatrix} -4 \\ 1 \end{pmatrix}$ (slow direction).
  - For $\lambda_2 = -2$: $\begin{pmatrix} 6/7 & -8/7 \\ -3/14 & 2/7 \end{pmatrix}\vec v_2 = \vec 0$. Row 1 gives $6v_1 - 8v_2 = 0 \implies 3v_1 = 4v_2$ (Row 2 consistent), so $\vec v_2 = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$ (fast direction).

### (iii) Local classification

- **$A(0,0)$:** $J(0,0) = 2I \implies \lambda_1 = \lambda_2 = 2 > 0$. **Unstable star.**
- **$B(0,1)$:** $(-1 - \lambda)(-2 - \lambda) = 0 \implies \lambda_1 = -1 < 0$, $\lambda_2 = -2 < 0$. **Stable node.**
  - For $\lambda_1 = -1$: $\begin{pmatrix} 0 & 0 \\ -3 & -1 \end{pmatrix}\vec v_1 = \vec 0 \implies \vec v_1 = \begin{pmatrix} 1 \\ -3 \end{pmatrix}$.
  - For $\lambda_2 = -2$: $\begin{pmatrix} 1 & 0 \\ -3 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies \vec v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
- **$C(2,0)$:** $(-2 - \lambda)(-4 - \lambda) = 0 \implies \lambda_1 = -2 < 0$, $\lambda_2 = -4 < 0$. **Stable node.**
  - For $\lambda_1 = -2$: $\begin{pmatrix} 0 & -6 \\ 0 & -2 \end{pmatrix}\vec v_1 = \vec 0 \implies \vec v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
  - For $\lambda_2 = -4$: $\begin{pmatrix} 2 & -6 \\ 0 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies 2v_1 - 6v_2 = 0 \implies \vec v_2 = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$.
- **$D\bigl(\tfrac{2}{7}, \tfrac{4}{7}\bigr)$:** Expanding $\det(J - \lambda I) = 0$:
  $$
  \left(-\frac{2}{7} - \lambda\right)\left(-\frac{8}{7} - \lambda\right) - \left(-\frac{6}{7}\right)\left(-\frac{12}{7}\right) = \lambda^2 + \frac{10}{7}\lambda + \frac{16 - 72}{49} = \lambda^2 + \frac{10}{7}\lambda - \frac{8}{7} = 0.
  $$
  Multiplying by $7$ gives $7\lambda^2 + 10\lambda - 8 = (7\lambda - 4)(\lambda + 2) = 0$, so $\lambda_1 = \frac{4}{7} > 0$, $\lambda_2 = -2 < 0$. **Saddle point.**
  - For $\lambda_1 = \frac{4}{7}$: $\begin{pmatrix} -6/7 & -6/7 \\ -12/7 & -12/7 \end{pmatrix}\vec v_1 = \vec 0 \implies v_1 + v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ (unstable manifold).
  - For $\lambda_2 = -2$: $\begin{pmatrix} 12/7 & -6/7 \\ -12/7 & 6/7 \end{pmatrix}\vec v_2 = \vec 0 \implies 2v_1 - v_2 = 0 \implies \vec v_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ (stable separatrix).

### (iv) Local classification

- **$A(0,0)$:** $(1 - \lambda)(-2 - \lambda) = 0 \implies \lambda_1 = 1 > 0$ with $\vec v_1 = (1,0)^T$, $\lambda_2 = -2 < 0$ with $\vec v_2 = (0,1)^T$. **Saddle point.**
- **$B\bigl(\tfrac{2}{3}, \tfrac{1}{2}\bigr)$:** Characteristic equation:
  $$
  \det\begin{pmatrix} -\lambda & -\frac{4}{3} \\ \frac{3}{2} & -\lambda \end{pmatrix} = \lambda^2 + \frac{4}{3}\cdot\frac{3}{2} = \lambda^2 + 2 = 0 \;\Longrightarrow\; \lambda_\pm = \pm i\sqrt{2}.
  $$
  For $\lambda_+ = i\sqrt{2}$, Row 2 of $(J - i\sqrt{2}I)\vec\eta_+ = \vec 0$ gives $\frac{3}{2}\eta_1 - i\sqrt{2}\eta_2 = 0 \implies 3\eta_1 = 2i\sqrt{2}\eta_2$. Taking $\eta_2 = -3i$ gives $\eta_1 = 2\sqrt{2}$, so $\vec\eta_+ = \begin{pmatrix} 2\sqrt{2} \\ -3i \end{pmatrix}$. Because $\operatorname{Re}(\lambda_\pm) = 0$, $B$ is a **linearized centre**; nonlinear stability must be confirmed globally via a conserved quantity in Step 4.

### (v) Local classification

- **$A(0,0)$:** $\lambda_1 = 4 > 0$ with $\vec v_1 = (1,0)^T$, $\lambda_2 = -2 < 0$ with $\vec v_2 = (0,1)^T$. **Saddle point.**
- **$B(8,0)$:** $(-4 - \lambda)(6 - \lambda) = 0 \implies \lambda_1 = -4 < 0$, $\lambda_2 = 6 > 0$. **Saddle point.**
  - For $\lambda_1 = -4$: $\begin{pmatrix} 0 & -24 \\ 0 & 10 \end{pmatrix}\vec v_1 = \vec 0 \implies \vec v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
  - For $\lambda_2 = 6$: $\begin{pmatrix} -10 & -24 \\ 0 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies -5v_1 - 12v_2 = 0 \implies \vec v_2 = \begin{pmatrix} -12 \\ 5 \end{pmatrix}$.
- **$C(2,1)$:** Characteristic equation:
  $$
  \det\begin{pmatrix} -1 - \lambda & -6 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 + \lambda + 6 = 0 \;\Longrightarrow\; \lambda_\pm = \frac{-1 \pm i\sqrt{23}}{2}.
  $$
  Since $\operatorname{Re}(\lambda_\pm) = -\frac{1}{2} < 0$ and $\operatorname{Im}(\lambda_\pm) \neq 0$, $C(2,1)$ is a **stable spiral**. For $\lambda_+$, Row 2 of $(J - \lambda_+ I)\vec\eta_+ = \vec 0$ gives $\eta_1 - \lambda_+\eta_2 = 0$; taking $\eta_2 = 2$ gives $\vec\eta_+ = \begin{pmatrix} -1 + i\sqrt{23} \\ 2 \end{pmatrix}$. At $(3,1)$, $\dot y = 1 > 0$, so the spiral winds **counter-clockwise**.

### (vi) Local classification

- **$A(0,0)$:** $\lambda_1 = 10 > 0$ with $\vec v_1 = (1,0)^T$, $\lambda_2 = 1 > 0$ with $\vec v_2 = (0,1)^T$. **Unstable node.**
- **$B(10,0)$:** $(-10 - \lambda)(11 - \lambda) = 0 \implies \lambda_1 = -10 < 0$ with $\vec v_1 = (1,0)^T$, $\lambda_2 = 11 > 0$. For $\lambda_2 = 11$, Row 1 gives $-21v_1 - 30v_2 = 0 \implies 7v_1 = -10v_2 \implies \vec v_2 = \begin{pmatrix} -10 \\ 7 \end{pmatrix}$. **Saddle point.**
- **$C\bigl(0, \tfrac{1}{10}\bigr)$:** $\bigl(\frac{97}{10} - \lambda\bigr)(-1 - \lambda) = 0 \implies \lambda_1 = \frac{97}{10} > 0$, $\lambda_2 = -1 < 0$. **Saddle point.**
  - For $\lambda_1 = \frac{97}{10}$: Row 2 gives $\frac{1}{10}v_1 - \frac{107}{10}v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 107 \\ 1 \end{pmatrix}$.
  - For $\lambda_2 = -1$: Row 1 gives $\frac{107}{10}v_1 = 0 \implies \vec v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
- **$D\bigl(\tfrac{97}{13}, \tfrac{11}{13}\bigr)$:** Here $\operatorname{tr}(J) = -\frac{97 + 110}{13} = -\frac{207}{13}$ and $\det(J) = \frac{97 \cdot 110 + 291 \cdot 11}{169} = \frac{13871}{169} = \frac{1067}{13}$. Characteristic equation:
  $$
  \lambda^2 + \frac{207}{13}\lambda + \frac{1067}{13} = 0.
  $$
  The discriminant is $\Delta = \frac{207^2 - 4 \cdot 13 \cdot 1067}{169} = \frac{42849 - 55484}{169} = -\frac{12635}{169} < 0$, giving
  $$
  \lambda_\pm = \frac{-207 \pm i\sqrt{12635}}{26}.
  $$
  Since $\operatorname{Re}(\lambda_\pm) = -\frac{207}{26} < 0$ and $\operatorname{Im}(\lambda_\pm) \neq 0$, $D$ is a **stable spiral**. From Row 2 of $(J(D) - \lambda_+ I)\vec\eta_+ = \vec 0$, $\frac{11}{13}\eta_1 + \left(-\frac{110}{13} - \frac{-207 + i\sqrt{12635}}{26}\right)\eta_2 = 0 \implies \frac{22}{26}\eta_1 - \frac{13 + i\sqrt{12635}}{26}\eta_2 = 0$, giving $\vec\eta_+ = (13 + i\sqrt{12635},\, 22)^T$. At $(8, 11/13)$, $\dot y = \frac{11}{13}(1 + 8 - \frac{110}{13}) > 0$, so trajectories spiral **counter-clockwise** into $D$.

### (vii) Local classification

- **$A(0,0)$:** $\lambda_1 = 3 > 0$ with $\vec v_1 = (1,0)^T$, $\lambda_2 = -2 < 0$ with $\vec v_2 = (0,1)^T$. **Saddle point.**
- **$B(3,0)$:** $(-3 - \lambda)(1 - \lambda) = 0 \implies \lambda_1 = -3 < 0$ with $\vec v_1 = (1,0)^T$, $\lambda_2 = 1 > 0$. For $\lambda_2 = 1$, Row 1 gives $-4v_1 - 3v_2 = 0 \implies \vec v_2 = \begin{pmatrix} -3 \\ 4 \end{pmatrix}$. **Saddle point.**
- **$C(2,1)$:** Characteristic equation:
  $$
  \det\begin{pmatrix} -2 - \lambda & -2 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 + 2\lambda + 2 = 0 \;\Longrightarrow\; \lambda_\pm = -1 \pm i.
  $$
  Since $\operatorname{Re}(\lambda_\pm) = -1 < 0$, $C(2,1)$ is a **stable spiral**. Row 2 of $(J - \lambda_+ I)\vec\eta_+ = \vec 0$ gives $\eta_1 - (-1+i)\eta_2 = 0$, so taking $\eta_2 = 1$ yields $\vec\eta_+ = \begin{pmatrix} -1 + i \\ 1 \end{pmatrix}$. At $(3,1)$, $\dot y = 1 > 0$, so the spiral is **counter-clockwise**.

## Step 4: Global picture

We combine the non-trivial nullclines, vector-field signs, and local portraits to assemble the global phase portrait in $x, y \ge 0$ and interpret the long-term evolution of both species.

### (i) Competitive exclusion of $y$ by $x$

The non-trivial nullclines are the parallel lines $y = 2 - x$ ($\dot x = 0$) and $y = 1 - x$ ($\dot y = 0$). Between them ($1 < x + y < 2$), $\dot x > 0$ and $\dot y < 0$, pushing every interior trajectory downward and to the right toward $C(2,0)$. Every initial state with $x(0) > 0$ converges to $(2,0)$: **species $x$ always outcompetes species $y$ and drives it to extinction**, reaching its own carrying capacity $x = 2$.

![[attachments/AM-PS/ch5-e2-i.svg]]
*Phase portrait of model (i) in $x, y \ge 0$: parallel nullclines $y = 2 - x$ and $y = 1 - x$ funnel all interior trajectories into the stable improper node $C(2,0)$.*

### (ii) Stable coexistence

The nullclines $y = 2 - x$ ($\dot x = 0$) and $y = 1 - x/8$ ($\dot y = 0$) cross at $D\bigl(\tfrac{8}{7}, \tfrac{6}{7}\bigr)$, dividing the first quadrant into four regions whose vector-field arrows all point inward toward $D$. Every initial population with $x(0) > 0$ and $y(0) > 0$ approaches $D\bigl(\tfrac{8}{7}, \tfrac{6}{7}\bigr)$: **both species coexist stably**, each at a lower level than its isolated carrying capacity.

![[attachments/AM-PS/ch5-e2-ii.svg]]
*Phase portrait of model (ii) in $x, y \ge 0$: all interior trajectories converge to the stable coexistence node $D(8/7, 6/7)$.*

### (iii) Bistable competitive exclusion

The nullclines $y = (2 - x)/3$ ($\dot x = 0$) and $y = 1 - \frac{3}{2}x$ ($\dot y = 0$) intersect at the saddle $D\bigl(\tfrac{2}{7}, \tfrac{4}{7}\bigr)$. The stable manifold of $D$ (entering from $A(0,0)$ and from infinity along slope $v_2/v_1 = 2$) acts as a **separatrix** dividing the first quadrant into two basins of attraction: initial conditions above the separatrix converge to $B(0,1)$ ($y$ wins, $x$ dies out), while those below converge to $C(2,0)$ ($x$ wins, $y$ dies out). Coexistence at $D$ is unstable.

![[attachments/AM-PS/ch5-e2-iii.svg]]
*Phase portrait of model (iii) in $x, y \ge 0$: the stable manifold of the saddle $D(2/7, 4/7)$ separates the basins of attraction of $B(0,1)$ and $C(2,0)$.*

### (iv) Periodic predator–prey oscillations (nonlinear centre proof)

The nullclines $y = 1/2$ ($\dot x = 0$) and $x = 2/3$ ($\dot y = 0$) divide the interior into four quadrants with counter-clockwise circulation around $B\bigl(\tfrac{2}{3}, \tfrac{1}{2}\bigr)$. To prove that $B$ is a **true nonlinear centre**, separate variables in the orbit equation $\frac{dy}{dx} = \frac{y(-2+3x)}{x(1-2y)}$:

$$
\frac{1 - 2y}{y}\,dy = \frac{-2 + 3x}{x}\,dx \;\Longrightarrow\; \int \left(\frac{1}{y} - 2\right)dy = \int \left(-\frac{2}{x} + 3\right)dx \;\Longrightarrow\; \ln y - 2y = -2\ln x + 3x - C.
$$

Define $H(x,y) = 3x - 2\ln x + 2y - \ln y$ on $x > 0, y > 0$. Differentiating along any trajectory by the chain rule verifies that $H$ is strictly conserved:

$$
\dot H = \left(3 - \frac{2}{x}\right)\dot x + \left(2 - \frac{1}{y}\right)\dot y = \frac{3x - 2}{x}\,x(1 - 2y) + \frac{2y - 1}{y}\,y(-2 + 3x) = (3x - 2)(1 - 2y) - (1 - 2y)(3x - 2) = 0.
$$

Moreover, $H_{xx} = 2/x^2 > 0$, $H_{yy} = 1/y^2 > 0$, and $H_{xy} = 0$, so $H$ is strictly convex on $x, y > 0$ with a unique global minimum at $B\bigl(\tfrac{2}{3}, \tfrac{1}{2}\bigr)$ and $H \to +\infty$ as $x \to 0^+$, $y \to 0^+$, or $x + y \to \infty$. Therefore every level curve $H(x,y) = C$ is a closed orbit around $B$: **prey and predator populations undergo sustained, periodic counter-clockwise oscillations** whose amplitude is fixed by the initial condition.

![[attachments/AM-PS/ch5-e2-iv.svg]]
*Phase portrait of model (iv) in $x, y \ge 0$: closed counter-clockwise level curves of $H(x,y) = 3x - 2\ln x + 2y - \ln y$ around the true nonlinear centre $B(2/3, 1/2)$.*

### (v) Damped oscillations to coexistence

The nullclines $y = (4 - x/2)/3$ ($\dot x = 0$) and $x = 2$ ($\dot y = 0$) cross at the stable spiral $C(2,1)$. Logistic self-limitation of the prey introduces damping that destroys the neutral cycles of model (iv): all interior trajectories spiral counter-clockwise into $C(2,1)$, so **both populations experience damped oscillations and settle to stable coexistence at $(2,1)$**.

![[attachments/AM-PS/ch5-e2-v.svg]]
*Phase portrait of model (v) in $x, y \ge 0$: interior trajectories spiral counter-clockwise into the stable coexistence spiral $C(2,1)$.*

### (vi) Coexistence with a generalist predator

The nullclines $y = (10 - x)/3$ ($\dot x = 0$) and $y = (1 + x)/10$ ($\dot y = 0$) cross at $D\bigl(\tfrac{97}{13}, \tfrac{11}{13}\bigr)$. Because the boundary equilibria $B(10,0)$ and $C(0, 1/10)$ are both saddles and $A(0,0)$ is an unstable node, every interior trajectory spirals counter-clockwise into $D$: **both species coexist stably at $(97/13, 11/13)$**, with the predator sustained above its alternative-food carrying capacity $1/10$.

![[attachments/AM-PS/ch5-e2-vi.svg]]
*Phase portrait of model (vi) in $x, y \ge 0$: all interior trajectories converge via damped counter-clockwise oscillations to $D(97/13, 11/13)$.*

### (vii) Damped oscillations to coexistence

The nullclines $y = 3 - x$ ($\dot x = 0$) and $x = 2$ ($\dot y = 0$) cross at the stable spiral $C(2,1)$. As in model (v), logistic prey growth damps out the predator–prey oscillations: every interior trajectory spirals counter-clockwise into $C(2,1)$, yielding **stable coexistence via damped oscillations**.

![[attachments/AM-PS/ch5-e2-vii.svg]]
*Phase portrait of model (vii) in $x, y \ge 0$: interior trajectories spiral counter-clockwise into the stable coexistence spiral $C(2,1)$.*

## Answers and checks

- **Check against the lecturer's solution (`Solved_exer_nonlinear_system.pdf`, pp. 1–5):**
  - Part (i) matches on all three stationary points $A(0,0)$ (unstable star), $B(0,1)$ (saddle), and the absence of a fourth equilibrium, as well as the global extinction of $y$. The single discrepancy at $C(2,0)$ (improper node vs star) is documented in the warning callout above.
  - Part (ii) agrees identically with `Solved_exer_nonlinear_system.pdf` (pp. 3–5) on all four equilibria, every Jacobian matrix, all eigenvalues ($\lambda_1 = -6/7$, $\lambda_2 = -2$ at $D$), all eigenvectors, and global coexistence at $(8/7, 6/7)$.
- **Dimensional / scaling check:** Treating populations $x, y$ as dimensionless scaled densities and time $t$ as dimensionless, every growth rate and interaction coefficient has dimension $[T^{-1}]$, every eigenvalue has dimension $[T^{-1}]$, and $H(x,y)$ in (iv) is dimensionless.

> [!result] Key results
> | Model | Ecological type | Equilibria in $x,y \ge 0$ & stability | Long-term outcome ($x_0, y_0 > 0$) |
> | :--- | :--- | :--- | :--- |
> | **(i)** | Competition | $(0,0)$ unstable star; $(0,1)$ saddle; $(2,0)$ stable improper node | $x \to 2,\; y \to 0$ ($x$ excludes $y$) |
> | **(ii)** | Weak competition | $(0,0)$ unstable star; $(0,1),(2,0)$ saddles; $(8/7,6/7)$ stable node | Coexistence at $(8/7, 6/7)$ |
> | **(iii)** | Strong competition | $(0,0)$ unstable star; $(0,1),(2,0)$ stable nodes; $(2/7,4/7)$ saddle | Bistable exclusion (depends on initial state) |
> | **(iv)** | Lotka–Volterra predator–prey | $(0,0)$ saddle; $(2/3,1/2)$ nonlinear centre | Periodic counter-clockwise oscillations |
> | **(v)** | Logistic prey–predator | $(0,0),(8,0)$ saddles; $(2,1)$ stable spiral | Damped oscillations to $(2,1)$ |
> | **(vi)** | Generalist predator–prey | $(0,0)$ unstable node; $(10,0),(0,1/10)$ saddles; $(97/13,11/13)$ stable spiral | Coexistence at $(97/13, 11/13)$ |
> | **(vii)** | Logistic prey–predator | $(0,0),(3,0)$ saddles; $(2,1)$ stable spiral | Damped oscillations to $(2,1)$ |
