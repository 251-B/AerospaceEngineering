---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane (lecture of Oct 15)"
tags:
  - teoria
  - concepto-clave
  - sistemas-lineales
  - autovalor-repetido
  - forma-de-jordan
  - retrato-de-fase
  - nodo-impropio
  - estrella
dificultad: alta
prerrequisitos:
  - "[[04 - Advanced Maths/Concept - Planar Systems with Complex Eigenvalues|Planar Systems with Complex Eigenvalues]]"
  - "[[04 - Advanced Maths/Concept - Integrating Factor and First-Order Linear Equations|Integrating Factor and First-Order Linear Equations]]"
  - "Linear algebra (rank, kernel, Cayley-Hamilton)"
fuentes:
  - "Notes.pdf (class notes 'Diff Eq', p. 10), sources/cuatrimestre-1/04-advanced-maths/teoria/Notes.pdf"
  - "Robinson (2004), An Introduction to Ordinary Differential Equations, Ch. 30 (pp. 295-298) and Ch. 31 p. 301"
---

# Planar Systems with a Repeated Eigenvalue

> **Key idea in one sentence:** If $\Delta = 0$ the matrix has one eigenvalue $\lambda$ with $m_a = 2$; either $A = \lambda I$ (a star, $m_g = 2$) or a Jordan chain $\mathbf v_1, \mathbf v_2$ gives $Q^{-1}AQ = \begin{pmatrix}\lambda & 1 \\ 0 & \lambda\end{pmatrix}$ and the solution $e^{\lambda t}[c_1\mathbf v_1 + c_2(t\mathbf v_1 + \mathbf v_2)]$ (an improper node, $m_g = 1$).

Web page: `subjects/advanced-maths/teoria/topic-4.html`, Section 8 (generated from `tools/am_phase/sections_7_8.html`; keep in step with this note). Ground truth: Robinson, Ch. 30 (Sec. 30.1 p. 295; Sec. 30.2 pp. 295-298; Eq. 30.1-30.4; Example 30.1 p. 298) and Ch. 31 (p. 301, Jordan form, starred). Lecture of **Oct 15**.

---

## 1. Multiplicities

$\Delta = (\operatorname{tr}A)^2 - 4\det A = 0$, so $\lambda = \tfrac12\operatorname{tr}A$ and $\det(A - \mu I) = (\mu - \lambda)^2$. Algebraic multiplicity $m_a = 2$; geometric multiplicity $m_g = \dim\ker(A - \lambda I) \in \{1, 2\}$.

## 2. Subcase A, $m_g = 2$: stars

**Proposition.** $m_g = 2 \Rightarrow A = \lambda I$. *Proof.* With independent eigenvectors $B = [\mathbf v_1 \mid \mathbf v_2]$: $AB = \lambda B \Rightarrow A = \lambda I$ (or: $\ker(A - \lambda I) = \mathbb R^2$).

$\mathbf x(t) = e^{\lambda t}\mathbf x_0$: every line through the origin is invariant; the matrix is $\lambda I$ in every basis, so no separate $\mathbf z$-plane. **Stable star** $\lambda < 0$, **unstable star** $\lambda > 0$ ($\lambda = 0$: $A = O$, all points are equilibria; Exercise 30.5).

## 3. Subcase 3.2, $m_g = 1$: the construction of the class notes (p. 10)

1. Choose $\mathbf v_2$ independent of the eigenvector $\mathbf v$ and define $\mathbf v_1 = (A - \lambda I)\mathbf v_2$ ($\neq \mathbf 0$, otherwise $\mathbf v_2$ would be a second eigenvector).
2. Write $\mathbf v_1 = \alpha\mathbf v_2 + \beta\mathbf v$. Then $(A - \lambda I)\mathbf v_1 = \alpha(A - \lambda I)\mathbf v_2 = \alpha\mathbf v_1$, i.e. $(A - (\lambda + \alpha)I)\mathbf v_1 = \mathbf 0$.
3. The only eigenvalue is $\lambda$, so $\alpha = 0$: $\mathbf v_1 = \beta\mathbf v$ is an eigenvector and $\{\mathbf v_1, \mathbf v_2\}$ a basis.
4. $(A - \lambda I)\mathbf v_2 = \mathbf v_1$, so $A\mathbf v_2 = \mathbf v_1 + \lambda\mathbf v_2$; with $P = (\mathbf v_1, \mathbf v_2)$, $AP = P\begin{pmatrix}\lambda & 1 \\ 0 & \lambda\end{pmatrix}$.
5. $\mathbf z = P^{-1}\mathbf x$: $\dot z_1 = \lambda z_1 + z_2$, $\dot z_2 = \lambda z_2$; $z_2 = Ce^{\lambda t}$, $(z_1e^{-\lambda t})' = C$, $z_1 = (Ct + D)e^{\lambda t}$; $\mathbf x = (Ct + D)e^{\lambda t}\mathbf v_1 + Ce^{\lambda t}\mathbf v_2$.
6. Sketch in $\mathbf z$ from the line $\dot z_1 = 0$, i.e. $z_2 = -\lambda z_1$ (vertical tangents there); in $\mathbf x$ the same picture drawn towards $\mathbf v_1$, the exact shape needs an explicit $A$.

Subcase 3.1 in the notes: $A = PDP^{-1}$ with $D = \lambda I$ gives $A = \lambda I$; every vector is an eigenvector and $\mathbf x(t) = \mathbf x_0e^{\lambda t}$.

## 3b. Complement: the eigenvector-first route (the Jordan chain)

$N = A - \lambda I \ne O$. **Lemma** (Cayley-Hamilton): $A^2 - 2\lambda A + \lambda^2I = N^2 = O$.

- $\mathbf v_1 \ne \mathbf 0$ with $N\mathbf v_1 = \mathbf 0$ (eigenvector).
- $\mathbf v_2$ with $N\mathbf v_2 = \mathbf v_1$, i.e. $A\mathbf v_2 = \lambda\mathbf v_2 + \mathbf v_1$ (generalised eigenvector).

*Existence:* $N^2 = O$ gives $\operatorname{im}N \subseteq \ker N$; both are one-dimensional, so equal, and $\mathbf v_1 \in \operatorname{im}N$. $\mathbf v_2$ is defined up to $+s\mathbf v_1$. *Independence:* $a\mathbf v_1 + b\mathbf v_2 = \mathbf 0$, apply $N$: $b = 0$, then $a = 0$.

Robinson's order (p. 296), the same as the notes': any $\mathbf y \notin \operatorname{span}\mathbf v$, $\mathbf v_2 = \mathbf y$, $\mathbf v_1 = N\mathbf y$ (with the lemma, $N\mathbf v_1 = N^2\mathbf y = \mathbf 0$).

## 4. Change of variable

$Q = [\mathbf v_1 \mid \mathbf v_2]$. $AQ = [\lambda\mathbf v_1 \mid \mathbf v_1 + \lambda\mathbf v_2] = QJ$:

$$Q^{-1}AQ = J = \begin{pmatrix}\lambda & 1 \\ 0 & \lambda\end{pmatrix}, \qquad \dot z_1 = \lambda z_1 + z_2,\ \dot z_2 = \lambda z_2.$$

## 5. Solving for $\mathbf z$

1. $\dfrac{d}{dt}(e^{-\lambda t}z_2) = 0 \Rightarrow z_2 = c_2e^{\lambda t}$.
2. $\dot z_1 - \lambda z_1 = c_2e^{\lambda t}$; integrating factor $e^{-\lambda t}$: $\dfrac{d}{dt}(e^{-\lambda t}z_1) = c_2$.
3. Barrow: $[e^{-\lambda s}z_1]_0^t = c_2t \Rightarrow$ 

$$z_1 = (c_1 + c_2t)e^{\lambda t}, \qquad z_2 = c_2e^{\lambda t}.$$

## 6. Solution in $\mathbf x$

$$\mathbf x(t) = e^{\lambda t}\big[c_1\mathbf v_1 + c_2(t\mathbf v_1 + \mathbf v_2)\big], \qquad (c_1, c_2)^T = Q^{-1}\mathbf x_0.$$

Check: $\dot{\mathbf x} = \lambda\mathbf x + c_2e^{\lambda t}\mathbf v_1 = A\mathbf x$ using $A\mathbf v_2 = \lambda\mathbf v_2 + \mathbf v_1$. Wronskian $e^{2\lambda t}\det[\mathbf v_1\ \mathbf v_2] \ne 0$.

## 7. Phase portraits

**$\mathbf z$-plane.** Eliminating $t$: $z_1 = z_2\big[K + \tfrac1\lambda\ln|z_2|\big]$ (also from $\dfrac{dz_1}{dz_2} = \dfrac{z_1}{z_2} + \dfrac1\lambda$). The $z_1$-axis is invariant (the only eigendirection); $\dot z_1 = z_2$ on the $z_2$-axis, so orbits cross it to the right above and to the left below. Orbits are tangent to the $z_1$-axis at the origin (logarithmically slowly) and parallel to it at infinity, S-shaped, point-symmetric.

**$\mathbf x$-plane.** $z_1$-axis $\mapsto \operatorname{span}\mathbf v_1$; $\mathbf v_2$ fixes the side and the drift: $(A - \lambda I)\mathbf x = z_2\mathbf v_1$ (use it at one point off the line to orient the S). $\det Q < 0$ mirrors the picture.

## 8. Worked example (Robinson 30.1; Example 8.1 on the web page)

$A = \begin{pmatrix}5 & -4 \\ 1 & 1\end{pmatrix}$: $\operatorname{tr} = 6$, $\det = 9$, $\lambda = 3$ ($m_a = 2$); $N = \begin{pmatrix}2 & -4 \\ 1 & -2\end{pmatrix}$ has rank 1, so $m_g = 1$. $\mathbf v_1 = (2, 1)^T$; $N\mathbf v_2 = \mathbf v_1$ gives $\mathbf v_2 = (1, 0)^T$. $Q = \begin{pmatrix}2 & 1 \\ 1 & 0\end{pmatrix}$, $\det Q = -1$, $Q^{-1} = \begin{pmatrix}0 & 1 \\ 1 & -2\end{pmatrix}$; $AQ = \begin{pmatrix}6 & 5 \\ 3 & 1\end{pmatrix}$, $Q^{-1}AQ = \begin{pmatrix}3 & 1 \\ 0 & 3\end{pmatrix}$ ✓.

$x_1 = e^{3t}[2c_1 + c_2(2t + 1)]$, $x_2 = e^{3t}[c_1 + c_2t]$, $c_1 = x_{20}$, $c_2 = x_{10} - 2x_{20}$ (verified by direct differentiation).

| $(c_1, c_2)$ | $\mathbf x(t)$ |
| :--- | :--- |
| $(1, 0)$ | $e^{3t}(2, 1)^T$ |
| $(0, 1)$ | $e^{3t}(2t + 1, t)^T$ |
| $(1, 1)$ | $e^{3t}(2t + 3, t + 1)^T$ |

Unstable improper node. Stable twin: $A' = -A$, $\lambda' = -3$, $Q' = [\mathbf v_1 \mid -\mathbf v_2]$, same curves, arrows reversed.

## Algorithm

1. $\lambda = \tfrac12\operatorname{tr}A$, $N = A - \lambda I$. 2. $N = O$: star. 3. Else $\mathbf v_1 \in \ker N$, solve $N\mathbf v_2 = \mathbf v_1$, $Q = [\mathbf v_1 \mid \mathbf v_2]$. 4. $\mathbf x(t) = e^{\lambda t}[c_1\mathbf v_1 + c_2(t\mathbf v_1 + \mathbf v_2)]$.

---

## Links

* [[04 - Advanced Maths/Concept - Planar Systems with Complex Eigenvalues|Planar Systems with Complex Eigenvalues]] (Oct 13 lecture; contains Example 7.3, a practice stable spiral).
* [[04 - Advanced Maths/Topic 4 - Systems of Linear ODEs and Phase Portraits|Topic 4]] (the whole topic in the order of the class notes).
* [[04 - Advanced Maths/Concept - Homogeneous Equations with Constant Coefficients and the Characteristic Equation|Constant Coefficients and the Characteristic Equation]]: the scalar repeated root $te^{\lambda t}$.
* [[04 - Advanced Maths/Advanced Maths MOC|Advanced Maths MOC]].
