---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 4"
dificultad: media
id: "e4"
pill: "Linear Independence • Complex Eigenvectors"
tags:
  - problema-resuelto
  - independencia-lineal
  - autovectores-complejos
  - demostracion
---

# Problem 4.II.4: Real and Imaginary Parts of a Complex Eigenvector Are Independent

> Official exercise 4 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

In the previous chapter we used the result that eigenvectors which correspond to distinct eigenvalues are linearly independent. Use this result to show that the real and imaginary parts of complex eigenvectors are linearly independent.

## Phase 1: Setup and hypotheses

Let $A$ be a real $2\times 2$ matrix with a non-real eigenvalue $\lambda = \rho + i\omega$ ($\omega \neq 0$) and eigenvector $\mathbf v = \mathbf u + i\mathbf w \in \mathbb C^2$, $\mathbf u, \mathbf w \in \mathbb R^2$. To show: $\mathbf u$ and $\mathbf w$ are linearly independent over $\mathbb R$, i.e. $\alpha\mathbf u + \beta\mathbf w = \mathbf 0$ with $\alpha, \beta \in \mathbb R$ implies $\alpha = \beta = 0$.

## Phase 2: Formulation

Ingredients: (a) $\bar{\mathbf v} = \mathbf u - i\mathbf w$ is an eigenvector for $\bar\lambda$ (conjugate $A\mathbf v = \lambda\mathbf v$ and use $\bar A = A$ since $A$ is real); (b) $\lambda \neq \bar\lambda$ because $\omega \neq 0$; (c) eigenvectors of distinct eigenvalues are linearly independent (over $\mathbb C$) (Topic 4, Appendix B argument).

> [!info] Method of the class notes [Notes, p. 10]
> Route of the notes: $\mathbf v_1 = \tfrac12(\mathbf v_+ + \mathbf v_-)$ and $\mathbf v_2 = -\tfrac i2(\mathbf v_+ - \mathbf v_-)$, that is $Q = (\mathbf v_1 \mid \mathbf v_2) = PM$ with $P = (\mathbf v_+ \mid \mathbf v_-)$ and $M = \begin{pmatrix} 1/2 & -i/2 \\ 1/2 & i/2 \end{pmatrix}$. $P$ is invertible because $\mathbf v_\pm$ belong to the distinct eigenvalues $\rho \pm i\omega$ ($\omega \neq 0$), and $\det M = \frac{i}{4} + \frac{i}{4} = \frac{i}{2} \neq 0$. So $\det Q = \det P\,\det M \neq 0$ and the real vectors $\mathbf v_1$, $\mathbf v_2$ are independent: the argument below, written with matrices.

## Phase 3: Derivation

#### Step 1: $\mathbf v$ and $\bar{\mathbf v}$ are independent

By (a), (b) and the quoted result, $\mathbf v$ and $\bar{\mathbf v}$ are linearly independent in $\mathbb C^2$: $\gamma\mathbf v + \delta\bar{\mathbf v} = \mathbf 0$ with $\gamma, \delta \in \mathbb C$ forces $\gamma = \delta = 0$.

#### Step 2: express $\mathbf u, \mathbf w$ through $\mathbf v, \bar{\mathbf v}$

$$ \mathbf u = \frac{\mathbf v + \bar{\mathbf v}}{2}, \qquad \mathbf w = \frac{\mathbf v - \bar{\mathbf v}}{2i} $$

#### Step 3: a real relation must be trivial

Suppose $\alpha\mathbf u + \beta\mathbf w = \mathbf 0$ with $\alpha, \beta \in \mathbb R$. Substitute Step 2 and collect the coefficients of $\mathbf v$ and $\bar{\mathbf v}$:

$$ \alpha\frac{\mathbf v + \bar{\mathbf v}}{2} + \beta\frac{\mathbf v - \bar{\mathbf v}}{2i} = \underbrace{\left(\frac{\alpha}{2} + \frac{\beta}{2i}\right)}_{\gamma}\mathbf v + \underbrace{\left(\frac{\alpha}{2} - \frac{\beta}{2i}\right)}_{\delta}\bar{\mathbf v} = \mathbf 0 $$

By Step 1, $\gamma = \delta = 0$. Using $\frac1i = -i$: $\gamma = \frac{\alpha - i\beta}{2}$ and $\delta = \frac{\alpha + i\beta}{2}$. Then $\gamma = 0$ means $\alpha - i\beta = 0$; with $\alpha, \beta$ real, real and imaginary parts give $\alpha = 0$ and $\beta = 0$. $\blacksquare$

#### Check against the direct argument

Alternative (Topic 4 Sec. 7.3): if $\mathbf w = k\mathbf u$ (or $\mathbf u = \mathbf 0$), $\mathbf v$ would be a complex multiple of one real vector $\mathbf r$, forcing $A\mathbf r = \lambda\mathbf r$ with $A\mathbf r$ real, so $\lambda$ would be real: contradiction. The two proofs agree; the one above only uses the independence of eigenvectors of distinct eigenvalues, as the exercise requests.

## Phase 4: Interpretation and checks

- Consequence: $Q = [\mathbf u \mid \mathbf w]$ is invertible, which is what makes the change of coordinates $\mathbf z = Q^{-1}\mathbf x$ possible for complex eigenvalues (Exercises 3 and 1).
- Numerical check with the eigenvector of Topic 4 Example 7.1, $\mathbf v = (5, -1 + 3i)^T$: $\mathbf u = (5, -1)^T$, $\mathbf w = (0, 3)^T$, $\det[\mathbf u\ \mathbf w] = 15 \neq 0$.
- The argument fails for a real eigenvalue ($\lambda = \bar\lambda$): then $\mathbf w = \mathbf 0$ can occur, consistent with Step 1 breaking down.
- In dimension $n$ the same idea shows that the real and imaginary parts of eigenvectors of different conjugate pairs together with real eigenvectors remain independent.
