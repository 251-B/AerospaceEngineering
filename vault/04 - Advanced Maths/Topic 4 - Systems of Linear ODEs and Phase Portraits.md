---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
tags:
  - moc-tema
  - advanced-maths
  - segundo-curso
  - sistemas-lineales
  - retrato-de-fase
  - autovalores
dificultad: alta
fuentes:
  - "Notes.pdf (class notes 'Diff Eq', pp. 9-10), sources/cuatrimestre-1/04-advanced-maths/teoria/Notes.pdf"
  - "Robinson (2004), An Introduction to Ordinary Differential Equations, Ch. 25-31, Appendix B"
  - "Lecture schedule: Oct 6 - Oct 15"
---

# Topic 4: Systems of Linear ODEs and Phase Portraits

> **Key takeaway:** a planar linear system $\dot{\mathbf x} = A\mathbf x$ is solved and drawn through the eigenvalues of $A$. A change of basis $\mathbf z = P^{-1}\mathbf x$ turns it into a canonical system whose phase portrait is easy to draw: an uncoupled node or saddle (two real eigenvalues), a rotating spiral or centre (complex pair), or a star or improper node (repeated eigenvalue). The portrait in $\mathbf x$ is the canonical one, deformed by $\mathbf x = P\mathbf z$.

This note follows pages 9 and 10 of the class notes (`Notes.pdf`) in their order. Robinson (2004) formalises and extends each step; material not in the notes is labelled **Complement (Robinson)**. The web page is `subjects/advanced-maths/teoria/topic-4.html`: Sections 1-6 and 9 are hand-written from this note, Sections 7-8 are generated from `tools/am_phase/sections_7_8.html` (concept notes [[04 - Advanced Maths/Concept - Planar Systems with Complex Eigenvalues|Complex Eigenvalues]] and [[04 - Advanced Maths/Concept - Planar Systems with a Repeated Eigenvalue|Repeated Eigenvalue]]), and the phase portraits come from `tools/figures/am_phase.py`.

---

## 1. Systems of ODEs [Notes, p. 9; Robinson, Ch. 25]

$n$ dependent variables $x_1, \dots, x_n$, one independent variable $t$: $\dot x_i = f_i(x_1, \dots, x_n, t)$, i.e. $\dot{\mathbf x} = \mathbf f(\mathbf x, t)$. If $\mathbf f$ and $D\mathbf f$ (Jacobian) are continuous in $\mathbf x$ and $t$ near $(\mathbf x_0, t_0)$, the IVP $\mathbf x(t_0) = \mathbf x_0$ has a unique local solution (Robinson Theorem 25.2).

**Important point.** An ODE of order $n \ge 2$ is a system of $n$ first-order ODEs: $\ddot x = f(\dot x, x, t)$ becomes $\dot x_1 = x_2$, $\dot x_2 = f(x_2, x_1, t)$ with $x_1 = x$, $x_2 = \dot x$.

## 2. Method 1: elimination [Notes, p. 9; Robinson, Ch. 26]

$\dot x = ax + by$, $\dot y = cx + dy$, $b \neq 0$: $y = (\dot x - ax)/b$, $\dot y = (\ddot x - a\dot x)/b$; substituting and multiplying by $b$,
$$\ddot x - (a + d)\dot x + (ad - bc)x = 0.$$
(Topic 1: $x' = 2x - y$, $y' = -x + 3y$ gives $\ddot x - 5\dot x + 5x = 0$.) **Complement (Robinson):** forcing terms, Eq. (26.3); Examples 26.1-26.2.

## 3. Linear systems [Notes, p. 9]

$\dot{\mathbf x} = A(t)\mathbf x + \mathbf f(t)$, $\mathbf x(t_0) = \mathbf x_0$ ($A$ an $n\times n$ matrix, $\mathbf f$ a vector function; $\mathbf f = \mathbf 0$ homogeneous). Existence and uniqueness if $A$, $\mathbf f$ are continuous.
- Superposition: combinations of solutions of $\dot{\mathbf x} = A(t)\mathbf x$ are solutions.
- Theorem: $\mathbf x_1, \dots, \mathbf x_k$ are independent iff $W(\mathbf x_1, \dots, \mathbf x_k) = \det(x_{ij}) \neq 0$ for all $t \in I$.
- $n = 2$: a fundamental set is a pair with $W(\mathbf x_1, \mathbf x_2) \neq 0$.
- Theorem: $\mathbf x = \mathbf x_h + \mathbf x_p$.

**Complement.** Liouville's formula $W(t) = W(t_0)e^{\int\operatorname{tr}A}$; variation of parameters $\mathbf x_p = \Phi\int\Phi^{-1}\mathbf f$.

## 4. Method 2: eigenvalues [Notes, p. 9; Robinson, Sec. 27.1-27.2]

$\mathbf x = e^{\lambda t}\mathbf v$ gives $A\mathbf v = \lambda\mathbf v$; solve $\det(A - \lambda I) = 0$. **Example [Notes; Robinson 27.1]:** $A = \begin{pmatrix} 2 & 2 \\ 6 & 3\end{pmatrix}$: $(2 - \lambda)(3 - \lambda) - 12 = (\lambda - 6)(\lambda + 1)$; $\lambda = 6$, $\mathbf v = (1, 2)^T$; $\lambda = -1$, $\mathbf v = (2, -3)^T$. For diagonal and upper-triangular matrices the eigenvalues are the diagonal entries. Three cases: two real, complex pair, repeated.

## 5-6. Case 1: two real eigenvalues $\lambda_1 \neq \lambda_2$ [Notes, p. 9; Robinson, Ch. 28]

$\mathbf x = C_1e^{\lambda_1t}\mathbf v_1 + C_2e^{\lambda_2t}\mathbf v_2$ (independence of $\mathbf v_1$, $\mathbf v_2$ to be checked; fundamental set).

**Diagonalisation.** $A = PDP^{-1}$, $P = (\mathbf v_1, \mathbf v_2)$, $D = \operatorname{diag}(\lambda_1, \lambda_2)$. With $\mathbf z = P^{-1}\mathbf x$: $\dot{\mathbf z} = P^{-1}A\mathbf x = DP^{-1}\mathbf x = D\mathbf z$, so $z_1 = C_1e^{\lambda_1t}$, $z_2 = C_2e^{\lambda_2t}$ and
$$z_2 = C_2\big(e^{\lambda_1t}\big)^{\lambda_2/\lambda_1} = C_2C_1^{-\lambda_2/\lambda_1}\big(C_1e^{\lambda_1t}\big)^{\lambda_2/\lambda_1} = \tilde C\,z_1^{\lambda_2/\lambda_1}.$$

| Ordering | $r = \lambda_2/\lambda_1$ | Origin | Near $\mathbf 0$ |
| :--- | :--- | :--- | :--- |
| $0 < \lambda_1 < \lambda_2$ | $> 1$ | unstable node | tangent to $z_1$-axis |
| $0 < \lambda_2 < \lambda_1$ | $(0, 1)$ | unstable node | tangent to $z_2$-axis |
| $\lambda_2 < \lambda_1 < 0$ | $> 1$ | stable node | tangent to $z_1$-axis |
| $\lambda_1 < \lambda_2 < 0$ | $(0, 1)$ | stable node | tangent to $z_2$-axis |
| $\lambda_1 < 0 < \lambda_2$ | $< 0$ | saddle | $z_1$-axis in, $z_2$-axis out |
| $\lambda_2 < 0 < \lambda_1$ | $< 0$ | saddle | $z_1$-axis out, $z_2$-axis in |

Back to $\mathbf x$: $\mathbf x = P\mathbf z = C_1e^{\lambda_1t}\mathbf v_1 + C_2e^{\lambda_2t}\mathbf v_2$; the $z$-axes become the eigenvector lines.

**Example [Notes; Robinson 28.1-28.3]:** $\dot x = x + y$, $\dot y = 4x - 2y$: $\lambda^2 + \lambda - 6 = 0$, $\lambda_1 = 2$, $\mathbf v_1 = (1, 1)^T$, $\lambda_2 = -3$, $\mathbf v_2 = (1, -4)^T$; $\mathbf x = C_1e^{2t}(1, 1)^T + C_2e^{-3t}(1, -4)^T$; saddle ($\lambda_2 < 0 < \lambda_1$), the line of $\mathbf v_1$ out and that of $\mathbf v_2$ in.

**Special case $\lambda_1 = 0$ [Notes, p. 9].** $A\mathbf v_1 = \mathbf 0$: the line $\operatorname{span}\mathbf v_1$ is made of equilibria and $\mathbf x = C_1\mathbf v_1 + C_2e^{\lambda_2t}\mathbf v_2$, straight orbits parallel to $\mathbf v_2$. Example (portal): $A = \begin{pmatrix} -1 & 1 \\ 1 & -1\end{pmatrix}$, $\lambda = 0, -2$, $\mathbf v_1 = (1, 1)^T$, $\mathbf v_2 = (1, -1)^T$, $C_1 = \tfrac12(x_{10} + x_{20})$; solutions slide onto the diagonal keeping $x_1 + x_2$.

**Complement (Robinson).** Robinson's $\tilde{\mathbf x}$ notation, Example 28.2 ($P^{-1}AP = \operatorname{diag}(2, -3)$), stable and unstable manifolds (Sec. 28.5).

## 7. Case 2: complex eigenvalues $\rho \pm i\omega$ [Notes, p. 10; Robinson, Ch. 29]

$\mathbf v_\pm = \mathbf v_1 \pm i\mathbf v_2$. Complex diagonalisation $A = PDP^{-1}$, $P = (\mathbf v_+ \mid \mathbf v_-)$; $\mathbf v_1 = \tfrac12(\mathbf v_+ + \mathbf v_-)$, $\mathbf v_2 = -\tfrac i2(\mathbf v_+ - \mathbf v_-)$; $Q = (\mathbf v_1 \mid \mathbf v_2) = PM$, $M = \begin{pmatrix} 1/2 & -i/2 \\ 1/2 & i/2\end{pmatrix}$, $M^{-1} = \begin{pmatrix} 1 & 1 \\ i & -i\end{pmatrix}$; $\mathbf z = Q^{-1}\mathbf x$, $\dot{\mathbf z} = M^{-1}DM\mathbf z = \begin{pmatrix} \rho & \omega \\ -\omega & \rho\end{pmatrix}\mathbf z$. Polar: $r = r(0)e^{\rho t}$, $\theta = \theta(0) - \omega t$ (clockwise in $\mathbf z$).
$$\mathbf x = C_1\operatorname{Re}\{\mathbf v e^{\lambda t}\} + C_2\operatorname{Im}\{\mathbf v e^{\lambda t}\}, \qquad \mathbf x = r(0)e^{\rho t}\big(\cos(\theta(0) - \omega t)\mathbf v_1 + \sin(\theta(0) - \omega t)\mathbf v_2\big).$$
$\rho < 0$ stable spiral, $\rho > 0$ unstable spiral, $\rho = 0$ centre. **Example [Notes]:** $A = \begin{pmatrix} 2 & 5 \\ -2 & 0\end{pmatrix}$, $\lambda = 1 \pm 3i$, $\mathbf v_1 = (5, -1)^T$, $\mathbf v_2 = (0, 3)^T$, unstable spiral, clockwise ($\dot x_1 = 5x_2 > 0$ at $x_1 = 0$, $x_2 > 0$). Details in [[04 - Advanced Maths/Concept - Planar Systems with Complex Eigenvalues|the concept note]].

## 8. Case 3: a repeated eigenvalue [Notes, p. 10; Robinson, Ch. 30]

- **3.1, two eigenvectors:** $A = P(\lambda I)P^{-1} = \lambda I$; every vector is an eigenvector, $\mathbf x = \mathbf x_0e^{\lambda t}$; unstable star ($\lambda > 0$), stable star ($\lambda < 0$).
- **3.2, one eigenvector $\mathbf v$:** choose $\mathbf v_2$ independent of $\mathbf v$, $\mathbf v_1 = (A - \lambda I)\mathbf v_2 = \alpha\mathbf v_2 + \beta\mathbf v$; $(A - (\lambda + \alpha)I)\mathbf v_1 = \mathbf 0$ forces $\alpha = 0$; $A\mathbf v_2 = \mathbf v_1 + \lambda\mathbf v_2$, $A = P\begin{pmatrix} \lambda & 1 \\ 0 & \lambda\end{pmatrix}P^{-1}$; $z_2 = Ce^{\lambda t}$, $z_1 = (Ct + D)e^{\lambda t}$; $\mathbf x = (Ct + D)e^{\lambda t}\mathbf v_1 + Ce^{\lambda t}\mathbf v_2$. Improper node; in $\mathbf z$ the orbits have vertical tangents on $z_2 = -\lambda z_1$. Details in [[04 - Advanced Maths/Concept - Planar Systems with a Repeated Eigenvalue|the concept note]].

## 9. Classification (Robinson, Ch. 31)

Real distinct: node or saddle; complex: spiral or centre; repeated: star or improper node. Trace-determinant plane as a complement.

## Problems

- [[04 - Advanced Maths/Problem Set - Chapter 4 Part 1|Problem Set - Chapter 4 Part 1]] (systems, elimination, real eigenvalues, zero eigenvalue in Exercise 11).
- [[04 - Advanced Maths/Problem Set - Chapter 4 Part 2|Problem Set - Chapter 4 Part 2]] (complex and repeated eigenvalues, canonical forms, nine portraits).

## Navigation

- [[04 - Advanced Maths/Advanced Maths MOC|Advanced Mathematics MOC]]
- Previous: [[04 - Advanced Maths/Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients|Topic 3]]
- [[00 - Indice Central/Master Index|Central Master Index]]
