---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane (lecture of Oct 13)"
tags:
  - teoria
  - concepto-clave
  - sistemas-lineales
  - autovalores-complejos
  - retrato-de-fase
  - espiral
  - centro
dificultad: alta
prerrequisitos:
  - "[[04 - Advanced Maths/Concept - Linear Independence of Functions and the Wronskian Determinant|Linear Independence and the Wronskian]]"
  - "[[04 - Advanced Maths/Concept - Homogeneous Equations with Constant Coefficients and the Characteristic Equation|Constant Coefficients and the Characteristic Equation]]"
  - "Linear algebra (eigenvalues, change of basis)"
fuentes:
  - "Robinson (2004), An Introduction to Ordinary Differential Equations, Ch. 29 (pp. 285-293) and Examples 27.5, 29.1"
---

# Planar Systems with Complex Eigenvalues

> **Key idea in one sentence:** If the real matrix $A$ has eigenvalues $\rho \pm i\omega$ ($\omega>0$), the real and imaginary parts $\mathbf u, \mathbf w$ of an eigenvector form a basis in which the system is "rotate by $\omega$ and scale by $\rho$", so every orbit is a spiral ($\rho \ne 0$) or an ellipse ($\rho = 0$).

Web page: `subjects/advanced-maths/teoria/topic-4.html`, Section 7 (generated from `tools/am_phase/sections_7_8.html` by `tools/am_phase_build.py`; keep both in step with this note). Ground truth: Robinson, *An Introduction to Ordinary Differential Equations*, Ch. 29 (Sec. 29.1 pp. 285-286; Sec. 29.2 pp. 287-290; Sec. 29.3 pp. 291-293), with Examples 27.5 and 29.1 (pp. 265-266, 286). Lecture of **Oct 13**.

Notation: Robinson's $\mathbf v_1, \mathbf v_2, P, \tilde{\mathbf x}$ are $\mathbf u, \mathbf w, Q, \mathbf z$ here.

---

## 1. Setting

$\Delta = (\operatorname{tr}A)^2 - 4\det A < 0$. Eigenvalues $\lambda_\pm = \rho \pm i\omega$ with $\rho = \tfrac12\operatorname{tr}A$, $\omega = \tfrac12\sqrt{-\Delta}$. If $A\mathbf v = \lambda\mathbf v$ then $A\bar{\mathbf v} = \bar\lambda\bar{\mathbf v}$ ($A$ real). Write $\mathbf v = \mathbf u + i\mathbf w$.

## 2. Real general solution (Robinson Sec. 29.1)

A real solution needs conjugate coefficients: $\mathbf x(t) = 2\operatorname{Re}\big[Ce^{(\rho + i\omega)t}(\mathbf u + i\mathbf w)\big]$, $C = \alpha + i\beta$.

1. $Ce^{i\omega t} = (\alpha\cos\omega t - \beta\sin\omega t) + i(\beta\cos\omega t + \alpha\sin\omega t)$.
2. $\operatorname{Re}[(a + ib)(\mathbf u + i\mathbf w)] = a\mathbf u - b\mathbf w$.
3. With $a_1 = 2\alpha$, $b_1 = -2\beta$:

$$\mathbf x(t) = e^{\rho t}\Big[(a_1\cos\omega t + b_1\sin\omega t)\mathbf u + (b_1\cos\omega t - a_1\sin\omega t)\mathbf w\Big].$$

## 3. Action of $A$ on $\mathbf u$ and $\mathbf w$ (Eq. 29.3)

Real and imaginary parts of $A(\mathbf u + i\mathbf w) = (\rho + i\omega)(\mathbf u + i\mathbf w) = (\rho\mathbf u - \omega\mathbf w) + i(\omega\mathbf u + \rho\mathbf w)$:

$$A\mathbf u = \rho\mathbf u - \omega\mathbf w, \qquad A\mathbf w = \omega\mathbf u + \rho\mathbf w.$$

**Lemma ($\mathbf u, \mathbf w$ independent, Exercise 29.4).** If they were dependent, $\mathbf v = \kappa\mathbf r$ with $\mathbf r$ real; then $A\mathbf r = \lambda\mathbf r$ with $A\mathbf r$ and $\mathbf r$ real forces $\lambda$ real, a contradiction.

## 4. Change of basis

$Q = [\mathbf u \mid \mathbf w]$, $\mathbf x = Q\mathbf z$, $\dot{\mathbf z} = Q^{-1}AQ\,\mathbf z$. Since $AQ = [\rho\mathbf u - \omega\mathbf w \mid \omega\mathbf u + \rho\mathbf w] = QJ$:

$$Q^{-1}AQ = J = \begin{pmatrix}\rho & \omega \\ -\omega & \rho\end{pmatrix}, \quad \dot z_1 = \rho z_1 + \omega z_2,\ \dot z_2 = -\omega z_1 + \rho z_2.$$

Column order $[\mathbf w \mid \mathbf u]$ gives $J^T$ (anticlockwise); this note always uses $[\mathbf u \mid \mathbf w]$.

## 5. Solving $\dot{\mathbf z} = J\mathbf z$

Polar coordinates $z_1 = r\cos\theta$, $z_2 = r\sin\theta$:

- $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2 = 2\rho r^2 \Rightarrow \dot r = \rho r$.
- $\dot\theta = \dfrac{z_1\dot z_2 - z_2\dot z_1}{r^2} = \dfrac{-\omega r^2}{r^2} = -\omega$ (chain rule on $\arctan(z_2/z_1)$).
- $r = r_0e^{\rho t}$ (Barrow: $[e^{-\rho s}r]_0^t = 0$), $\theta = \theta_0 - \omega t$.

$$\mathbf z(t) = e^{\rho t}\begin{pmatrix}\cos\omega t & \sin\omega t \\ -\sin\omega t & \cos\omega t\end{pmatrix}\mathbf z_0.$$

Shortcut: $\zeta = z_1 + iz_2$ obeys $\dot\zeta = (\rho - i\omega)\zeta$.

## 6. Phase portrait in the $\mathbf z$-plane

Always **clockwise** ($\dot\theta = -\omega$). Orbits $r = r_0\exp(\rho(\theta_0 - \theta)/\omega)$.

| $\rho$ | Origin | Stability |
| :--- | :--- | :--- |
| $< 0$ | stable spiral | asymptotically stable |
| $> 0$ | unstable spiral | unstable |
| $= 0$ | centre (circles, period $2\pi/\omega$) | stable, not attracting |

Radius factor per turn: $e^{2\pi\rho/\omega}$.

## 7. Back to $\mathbf x = Q\mathbf z$

$\mathbf x(t) = e^{\rho t}\big[(z_{10}\cos\omega t + z_{20}\sin\omega t)\mathbf u + (z_{20}\cos\omega t - z_{10}\sin\omega t)\mathbf w\big]$, $(z_{10}, z_{20})^T = Q^{-1}\mathbf x_0$. $Q$ maps circles to ellipses with conjugate semi-diameters $\mathbf u, \mathbf w$ and the axes to the lines through $\mathbf u$, $\mathbf w$ (not invariant).

**Sense of rotation.** In $\mathbf z$: clockwise. In $\mathbf x$: clockwise iff $\det Q > 0$. Practical test: $A(0,1)^T = (a_{12}, a_{22})^T$; $a_{12} > 0$ means clockwise, $a_{12} < 0$ anticlockwise. Never $a_{12} = 0$, because $\Delta = (a_{11} - a_{22})^2 + 4a_{12}a_{21} < 0$ forces $a_{12}a_{21} < 0$.

## 8. Worked examples

**Example 7.1** (Robinson 27.5, 29.1, 29.3): $A = \begin{pmatrix}2 & 5 \\ -2 & 0\end{pmatrix}$. $\lambda^2 - 2\lambda + 10 = 0$, $\lambda = 1 \pm 3i$; $\mathbf v = (5, -1 + 3i)^T$, $\mathbf u = (5, -1)^T$, $\mathbf w = (0, 3)^T$. Checks: $A\mathbf u = (5, -10)^T = \mathbf u - 3\mathbf w$, $A\mathbf w = (15, 0)^T = 3\mathbf u + \mathbf w$. $Q = \begin{pmatrix}5 & 0 \\ -1 & 3\end{pmatrix}$, $\det Q = 15$, $Q^{-1} = \tfrac1{15}\begin{pmatrix}3 & 0 \\ 1 & 5\end{pmatrix}$, $Q^{-1}AQ = \begin{pmatrix}1 & 3 \\ -3 & 1\end{pmatrix}$. $x_1 = 5e^t(z_{10}\cos3t + z_{20}\sin3t)$, $x_2 = e^t[(3z_{20} - z_{10})\cos3t - (3z_{10} + z_{20})\sin3t]$. Unstable spiral, clockwise in both planes ($a_{12} = 5 > 0$).

**Example 7.2** (written for the portal): $A = \begin{pmatrix}1 & -2 \\ 1 & -1\end{pmatrix}$, $\lambda = \pm i$, $\mathbf u = (2, 1)^T$, $\mathbf w = (0, -1)^T$, $Q = \begin{pmatrix}2 & 0 \\ 1 & -1\end{pmatrix}$, $\det Q = -2$, $Q^{-1}AQ = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$. Orbits: ellipses $\tfrac12x_1^2 - x_1x_2 + x_2^2 = r_0^2$ ($\dot V = 0$ checked). Clockwise in $\mathbf z$, **anticlockwise in $\mathbf x$** ($a_{12} = -2 < 0$).

**Example 7.3** (practice item written for the portal, not in the class notes): $A = \begin{pmatrix}0 & -5 \\ 1 & -2\end{pmatrix}$, $\lambda = -1 \pm 2i$, $\mathbf u = (1, 1)^T$, $\mathbf w = (2, 0)^T$, $Q = \begin{pmatrix}1 & 2 \\ 1 & 0\end{pmatrix}$, $Q^{-1}AQ = \begin{pmatrix}-1 & 2 \\ -2 & -1\end{pmatrix}$; $\mathbf x_0 = (1,1)^T \Rightarrow \mathbf x(t) = e^{-t}(\cos2t - 2\sin2t,\ \cos2t)^T$. Stable spiral, anticlockwise in $\mathbf x$.

---

## Links

* [[04 - Advanced Maths/Concept - Planar Systems with a Repeated Eigenvalue|Planar Systems with a Repeated Eigenvalue]] (Oct 15 lecture).
* [[04 - Advanced Maths/Concept - Homogeneous Equations with Constant Coefficients and the Characteristic Equation|Constant Coefficients and the Characteristic Equation]]: complex roots there are the scalar version of this case.
* [[04 - Advanced Maths/Advanced Maths MOC|Advanced Maths MOC]].

## Class notes (p. 10)

The notes write $\mathbf v_\pm = \mathbf v_1 \pm i\mathbf v_2$ ($\mathbf v_1 = \mathbf u$, $\mathbf v_2 = \mathbf w$) and reach $J$ by a complex diagonalisation: $A = PDP^{-1}$ with $P = (\mathbf v_+ \mid \mathbf v_-)$, $D = \operatorname{diag}(\rho + i\omega, \rho - i\omega)$; $Q = (\mathbf v_1 \mid \mathbf v_2) = PM$ with $M = \begin{pmatrix} 1/2 & -i/2 \\ 1/2 & i/2\end{pmatrix}$, $M^{-1} = \begin{pmatrix} 1 & 1 \\ i & -i\end{pmatrix}$, so $Q^{-1}AQ = M^{-1}DM = \begin{pmatrix} \rho & \omega \\ -\omega & \rho\end{pmatrix}$. General solution $\mathbf x = C_1\operatorname{Re}\{\mathbf v e^{\lambda t}\} + C_2\operatorname{Im}\{\mathbf v e^{\lambda t}\}$; particular solution $\mathbf x = r(0)e^{\rho t}\big(\cos(\theta(0) - \omega t)\mathbf v_1 + \sin(\theta(0) - \omega t)\mathbf v_2\big)$. Their four-step example is $A = \begin{pmatrix} 2 & 5 \\ -2 & 0\end{pmatrix}$ (Example 7.1): $\lambda = 1 \pm 3i$, $\mathbf v_\pm = (-5, 1 \mp 3i)^T$, $\dot{\mathbf z} = \begin{pmatrix} 1 & 3 \\ -3 & 1\end{pmatrix}\mathbf z$, unstable spiral, clockwise ($\dot x_1 = 5x_2 > 0$ on the positive $x_2$-axis). See [[04 - Advanced Maths/Topic 4 - Systems of Linear ODEs and Phase Portraits|Topic 4]], Section 7.
