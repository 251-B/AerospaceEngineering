---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 8"
dificultad: media
id: "e8"
pill: "Qualitative Portraits • Classification • Nine Cases"
tags:
  - problema-resuelto
  - retrato-de-fase
  - clasificacion
  - analisis-cualitativo
---

# Problem 4.II.8: Nine Qualitative Phase Portraits from Partial Data

> Official exercise 8 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Draw the phase portrait for the equation $d\mathbf x/dt = A\mathbf x$ when the eigenvalues and eigenvectors of $A$ are as given:

- (i) $\lambda_1 = 3$ with $\mathbf v_1 = (1, 1)$ and $\lambda_2 = -2$ with $\mathbf v_2 = (1, -2)$;
- (ii) complex conjugate eigenvalues $\lambda_\pm = -1 \pm 3i$, with $\dot x < 0$ when $x = 0$ and $y > 0$;
- (iii) a single eigenvalue $\lambda = 13$ with eigenvector $(3, 2)$, and $\dot x > 0$ when $x = 0$ and $y > 0$;
- (iv) $\lambda_1 = -2$ with $\mathbf v_1 = (2, 1)$ and $\lambda_2 = -3$ with $\mathbf v_2 = (1, -1)$;
- (v) a single eigenvalue $\lambda = -3$ with eigenvector $(1, -1)$, and $\dot x > 0$ when $x = 0$ and $y > 0$;
- (vi) $\lambda_\pm = \pm 2i$, where $\dot y < 0$ when $y = 0$ and $x > 0$;
- (vii) $\lambda_1 = 1$ with $\mathbf v_1 = (3, 2)$ and $\lambda_2 = 5$ with $\mathbf v_2 = (1, -4)$;
- (viii) $\lambda_\pm = 5 \pm i$, and $\dot y > 0$ when $y = 0$ and $x > 0$;
- (ix) a single eigenvalue $\lambda = -7$, with the matrix $A$ being a multiple of the identity.

## Phase 1: Setup: what the data determine

The data fix the **type** of the origin and the position of the eigenlines, which is all that the phase portrait of a linear system needs (Topic 4 Sec. 9, Robinson Ch. 31). A matrix consistent with the data is built in each item, to draw the portrait and to check the sign information numerically; any other matrix with the same data has the same portrait up to a linear distortion of the plane.

| Data | Origin is a | Extra information used |
| :--- | :--- | :--- |
| two real eigenvalues, opposite signs | saddle | eigenlines; stable = negative eigenvalue |
| two real eigenvalues, same sign | node | tangent to the eigenvector of the smaller $\vert \lambda\vert $; stable iff $\lambda < 0$ |
| complex $\rho \pm i\omega$, $\rho \neq 0$ | spiral | stable iff $\rho < 0$; sense from the sign of $\dot x$ at $(0, 1)$ or $\dot y$ at $(1, 0)$ |
| imaginary $\pm i\omega$ | centre | closed orbits; sense from the sign condition |
| single eigenvalue, one eigenvector | improper node | S-shaped orbits along the eigenline; side/orientation from the sign condition |
| single eigenvalue, $A = \lambda I$ | star | straight rays |

## Phase 2: Formulation: how the sign conditions are read

At the point $(0, 1)$ the vector field is $A(0, 1)^T = (a_{12}, a_{22})^T$, so the sign of $\dot x$ there is the sign of $a_{12}$: positive means motion to the right at the top of the plane, which is clockwise; negative means counter-clockwise. At $(1, 0)$ the field is $(a_{11}, a_{21})^T$, so the sign of $\dot y$ there is the sign of $a_{21}$: negative means downwards on the right-hand side, i.e. clockwise; positive means counter-clockwise (Topic 4 Sec. 7.8).

> [!info] Method of the class notes [Notes, pp. 9–10]
> The classification of the notes decides each item. Two real eigenvalues (Case 1) give a node or a saddle, read from the sign table of $\lambda_2/\lambda_1$. A complex pair (Case 2) gives a spiral or a centre from the sign of $\rho$, with the sense of rotation read from the sign of $\dot x$ or $\dot y$ on an axis, as in the example of the notes. A repeated eigenvalue (Case 3) gives a star when $A = \lambda I$ and an improper node, with one eigenvector, otherwise.

## Phase 3: Derivation of the nine portraits

### (i) $\lambda_1 = 3$ with $\mathbf v_1 = (1, 1)$ and $\lambda_2 = -2$ with $\mathbf v_2 = (1, -2)$

Two real eigenvalues with independent eigenvectors ($\det[\mathbf v_1\ \mathbf v_2] = -3 \neq 0$). A consistent matrix is $A = Q\Lambda Q^{-1} = \begin{pmatrix} \frac{4}{3} & \frac{5}{3} \\ \frac{10}{3} & - \frac{1}{3} \end{pmatrix}$ (checked: $A\mathbf v_1 = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3\mathbf v_1$, $A\mathbf v_2 = \begin{pmatrix} -2 \\ 4 \end{pmatrix} = -2\mathbf v_2$).

#### Phase portrait

$\lambda_1 = 3$ and $\lambda_2 = -2$ are of opposite signs: the origin is a **saddle** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{3t}$ and $z_2 = c_2e^{-2t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{- \frac{2}{3}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = - \frac{2}{3}$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through $(1, -2)$ (the **stable manifold**), reach the origin as $t \to +\infty$; the line through $(1, 1)$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (1, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, -2)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 3\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = -2\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4b-e8-i-z.svg]]
*Canonical $\mathbf z$-plane (saddle): invariant axes and orbits $z_2 = K|z_1|^{- \frac{2}{3}}$.*

![[attachments/AM-PS/ch4b-e8-i-x.svg]]
*Original $(x, y)$-plane (saddle): dashed lines are the eigenlines $\mathbf v_1 = (1, 1)$ and $\mathbf v_2 = (1, -2)$.*

### (ii) complex conjugate eigenvalues $\lambda_\pm = -1 \pm 3i$, with $\dot x < 0$ when $x = 0$ and $y > 0$

$\dot x < 0$ at $(0, 1)$ gives $a_{12} < 0$: leftwards at the top of the plane, i.e. **counter-clockwise**. A consistent matrix with eigenvalues $-1 \pm 3i$ is $A = \begin{pmatrix} -1 & -3 \\ 3 & -1 \end{pmatrix}$ ($\operatorname{tr}A = -2$, $\det A = 10$, $\lambda = -1 \pm 3i$; $a_{12} = -3 < 0$).

#### Phase portrait

$\rho = -1$ and $\omega = 3$: the origin is a **stable spiral**. In the $\mathbf z$-plane $r = r_0e^{-1t}$ and $\theta = \theta_0 - 3t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{-\frac{2 \pi}{3}}$ (shrinking).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} -3 \\ -1 \end{pmatrix}$, so $\dot x = -3$ is $< 0$: to the left at the top of the plane: the rotation is **counter-clockwise**. Cross-check: $\det Q = -9$ is $< 0$, so $Q$ reverses orientation and the clockwise motion of the $\mathbf z$-plane becomes counter-clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e8-ii-z.svg]]
*Canonical $\mathbf z$-plane (stable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e8-ii-x.svg]]
*Original $(x, y)$-plane (stable spiral), counter-clockwise.*

### (iii) a single eigenvalue $\lambda = 13$ with eigenvector $(3, 2)$, and $\dot x > 0$ when $x = 0$ and $y > 0$

Single eigenvalue $13$ with one eigenvector $(3, 2)^T$: $A \neq 13I$ (a star would have two independent eigenvectors), so $N = A - 13I$ is non-zero, $N^2 = O$ and $\ker N = \operatorname{span}\{(3, 2)^T\}$. Hence $N = c\begin{pmatrix} 3 \\ 2 \end{pmatrix}(2, -3) = c\begin{pmatrix} 6 & -9 \\ 4 & -6 \end{pmatrix}$ (rows orthogonal to $(3, 2)$ so that $N(3, 2)^T = \mathbf 0$), and $a_{12} = N_{12} = -9c$. The condition $\dot x > 0$ at $(0, 1)$ means $a_{12} > 0$, so $c < 0$; take $c = -1$: $N = \begin{pmatrix} -6 & 9 \\ -4 & 6 \end{pmatrix}$, $A = 13I + N = \begin{pmatrix} 7 & 9 \\ -4 & 19 \end{pmatrix}$.

#### Phase portrait

$\lambda = 13$ is repeated with a single eigendirection and $A \neq \lambda I$: the origin is an **unstable improper node** (Topic 4 Sec. 8.8 and 8.9). In the $\mathbf z$-plane the $z_1$-axis is invariant ($z_2 \equiv 0$, $z_1 = c_1e^{13t}$, arrows away from the origin); the other orbits satisfy $z_1 = z_2\left[K + \frac{1}{\lambda}\ln|z_2|\right]$, are S-shaped, tangent to the $z_1$-axis at the origin and parallel to it far away. Since $\dot z_1 = \lambda z_1 + z_2 = z_2$ on the $z_2$-axis, orbits cross it moving to the right in the upper half-plane and to the left in the lower one.

Orientation in the $\mathbf x$-plane, from $N\mathbf x = (A - \lambda I)\mathbf x = z_2\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = \begin{pmatrix} 9 \\ 6 \end{pmatrix} = 3\,\mathbf v_1$, so there the orbit drifts along $+\mathbf v_1$. The orbits are tangent to the eigenline at the origin and bend into an S around it.

![[attachments/AM-PS/ch4b-e8-iii-z.svg]]
*Canonical $\mathbf z$-plane (unstable improper node).*

![[attachments/AM-PS/ch4b-e8-iii-x.svg]]
*Original $(x, y)$-plane (unstable improper node); dashed: the eigenline with $\mathbf v_1 = (3, 2)$.*

### (iv) $\lambda_1 = -2$ with $\mathbf v_1 = (2, 1)$ and $\lambda_2 = -3$ with $\mathbf v_2 = (1, -1)$

Two real eigenvalues with independent eigenvectors ($\det[\mathbf v_1\ \mathbf v_2] = -3 \neq 0$). A consistent matrix is $A = Q\Lambda Q^{-1} = \begin{pmatrix} - \frac{7}{3} & \frac{2}{3} \\ \frac{1}{3} & - \frac{8}{3} \end{pmatrix}$ (checked: $A\mathbf v_1 = \begin{pmatrix} -4 \\ -2 \end{pmatrix} = -2\mathbf v_1$, $A\mathbf v_2 = \begin{pmatrix} -3 \\ 3 \end{pmatrix} = -3\mathbf v_2$).

#### Phase portrait

$\lambda_1 = -2$ and $\lambda_2 = -3$ are both negative: the origin is a **stable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{-2t}$ and $z_2 = c_2e^{-3t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{\frac{3}{2}}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = \frac{3}{2}$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 2$, i.e. to the line through $(2, 1)$ (they arrive there as $t \to +\infty$), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point towards the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (2, 1)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, -1)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = -2\mathbf v_1$ points inward; on $\mathbf v_2$: $\dot{\mathbf x} = -3\mathbf v_2$ points inward.

![[attachments/AM-PS/ch4b-e8-iv-z.svg]]
*Canonical $\mathbf z$-plane (stable node): invariant axes and orbits $z_2 = K|z_1|^{\frac{3}{2}}$.*

![[attachments/AM-PS/ch4b-e8-iv-x.svg]]
*Original $(x, y)$-plane (stable node): dashed lines are the eigenlines $\mathbf v_1 = (2, 1)$ and $\mathbf v_2 = (1, -1)$.*

### (v) a single eigenvalue $\lambda = -3$ with eigenvector $(1, -1)$, and $\dot x > 0$ when $x = 0$ and $y > 0$

Single eigenvalue $-3$ with one eigenvector $(1, -1)^T$: $A \neq -3I$ and $N = A + 3I \neq O$ with $\ker N = \operatorname{span}\{(1, -1)^T\}$. Hence $N = c\begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$ and $a_{12} = N_{12} = c$. The condition $\dot x > 0$ at $(0, 1)$ means $a_{12} > 0$, so $c > 0$; take $c = 1$: $N = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$, $A = -3I + N = \begin{pmatrix} -2 & 1 \\ -1 & -4 \end{pmatrix}$.

#### Phase portrait

$\lambda = -3$ is repeated with a single eigendirection and $A \neq \lambda I$: the origin is an **stable improper node** (Topic 4 Sec. 8.8 and 8.9). In the $\mathbf z$-plane the $z_1$-axis is invariant ($z_2 \equiv 0$, $z_1 = c_1e^{-3t}$, arrows towards the origin); the other orbits satisfy $z_1 = z_2\left[K + \frac{1}{\lambda}\ln|z_2|\right]$, are S-shaped, tangent to the $z_1$-axis at the origin and parallel to it far away. Since $\dot z_1 = \lambda z_1 + z_2 = z_2$ on the $z_2$-axis, orbits cross it moving to the right in the upper half-plane and to the left in the lower one.

Orientation in the $\mathbf x$-plane, from $N\mathbf x = (A - \lambda I)\mathbf x = z_2\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = \begin{pmatrix} 1 \\ -1 \end{pmatrix} = 1\,\mathbf v_1$, so there the orbit drifts along $+\mathbf v_1$. The orbits are tangent to the eigenline at the origin and bend into an S around it.

![[attachments/AM-PS/ch4b-e8-v-z.svg]]
*Canonical $\mathbf z$-plane (stable improper node).*

![[attachments/AM-PS/ch4b-e8-v-x.svg]]
*Original $(x, y)$-plane (stable improper node); dashed: the eigenline with $\mathbf v_1 = (1, -1)$.*

### (vi) $\lambda_\pm = \pm 2i$, where $\dot y < 0$ when $y = 0$ and $x > 0$

$\dot y = a_{21}x + a_{22}y$ at $(1, 0)$ equals $a_{21}$, and $\dot y < 0$ there, so $a_{21} < 0$: at the right-hand side of the plane the motion is downwards, i.e. **clockwise**. A consistent matrix with eigenvalues $\pm 2i$ and $a_{21} < 0$ is $A = \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ ($\operatorname{tr}A = 0$, $\det A = 4$, eigenvalues $\pm 2i$; $a_{21} = -2 < 0$).

#### Phase portrait

$\rho = 0$ and $\omega = 2$: the origin is a **centre**. In the $\mathbf z$-plane $r = r_0e^{0t}$ and $\theta = \theta_0 - 2t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and the orbits are circles of period $T = 2\pi/\omega$ (closed orbits).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$, so $\dot x = 2$ is $> 0$: to the right at the top of the plane: the rotation is **clockwise**. Cross-check: $\det Q = 4$ is $> 0$, so $Q$ preserves orientation and the clockwise motion of the $\mathbf z$-plane becomes clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e8-vi-z.svg]]
*Canonical $\mathbf z$-plane (centre): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e8-vi-x.svg]]
*Original $(x, y)$-plane (centre), clockwise.*

### (vii) $\lambda_1 = 1$ with $\mathbf v_1 = (3, 2)$ and $\lambda_2 = 5$ with $\mathbf v_2 = (1, -4)$

Two real eigenvalues with independent eigenvectors ($\det[\mathbf v_1\ \mathbf v_2] = -14 \neq 0$). A consistent matrix is $A = Q\Lambda Q^{-1} = \begin{pmatrix} \frac{11}{7} & - \frac{6}{7} \\ - \frac{16}{7} & \frac{31}{7} \end{pmatrix}$ (checked: $A\mathbf v_1 = \begin{pmatrix} 3 \\ 2 \end{pmatrix} = 1\mathbf v_1$, $A\mathbf v_2 = \begin{pmatrix} 5 \\ -20 \end{pmatrix} = 5\mathbf v_2$).

#### Phase portrait

$\lambda_1 = 1$ and $\lambda_2 = 5$ are both positive: the origin is a **unstable node** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).

In the canonical $\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{1t}$ and $z_2 = c_2e^{5t}$ (for $c_1 \neq 0$): $|z_1|/|c_1| = e^{\lambda_1t}$, so $e^{t} = (|z_1|/|c_1|)^{1/\lambda_1}$ and $|z_2| = |c_2|e^{\lambda_2t} = |c_2|\,(|z_1|/|c_1|)^{\lambda_2/\lambda_1}$, i.e. $z_2 = K\,|z_1|^{\lambda_2/\lambda_1} = K\,|z_1|^{5}$ with $K = c_2|c_1|^{-\lambda_2/\lambda_1}$ (equivalently, integrate the separable equation $\frac{dz_2}{dz_1} = \frac{\lambda_2z_2}{\lambda_1z_1}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.

The exponent $\lambda_2/\lambda_1 = 5$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\lambda| = 1$, i.e. to the line through $(3, 2)$ (they leave from there (the limit $t \to -\infty$)), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point away from the origin on both eigenlines.

The map $\mathbf x = Q\mathbf z$ sends the $z_1$-axis to the line through $\mathbf v_1 = (3, 2)$ and the $z_2$-axis to the line through $\mathbf v_2 = (1, -4)$. Straight lines stay straight and the origin stays fixed, so the $\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\mathbf v_1$: $\dot{\mathbf x} = A\mathbf v_1 = 1\mathbf v_1$ points outward; on $\mathbf v_2$: $\dot{\mathbf x} = 5\mathbf v_2$ points outward.

![[attachments/AM-PS/ch4b-e8-vii-z.svg]]
*Canonical $\mathbf z$-plane (unstable node): invariant axes and orbits $z_2 = K|z_1|^{5}$.*

![[attachments/AM-PS/ch4b-e8-vii-x.svg]]
*Original $(x, y)$-plane (unstable node): dashed lines are the eigenlines $\mathbf v_1 = (3, 2)$ and $\mathbf v_2 = (1, -4)$.*

### (viii) $\lambda_\pm = 5 \pm i$, and $\dot y > 0$ when $y = 0$ and $x > 0$

$\dot y > 0$ at $(1, 0)$ gives $a_{21} > 0$: upwards on the right-hand side, i.e. **counter-clockwise**. A consistent matrix with eigenvalues $5 \pm i$ is $A = \begin{pmatrix} 5 & -1 \\ 1 & 5 \end{pmatrix}$ ($\operatorname{tr}A = 10$, $\det A = 26$, $\lambda = 5 \pm i$; $a_{21} = 1 > 0$).

#### Phase portrait

$\rho = 5$ and $\omega = 1$: the origin is a **unstable spiral**. In the $\mathbf z$-plane $r = r_0e^{5t}$ and $\theta = \theta_0 - 1t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{10 \pi}$ (growing).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} -1 \\ 5 \end{pmatrix}$, so $\dot x = -1$ is $< 0$: to the left at the top of the plane: the rotation is **counter-clockwise**. Cross-check: $\det Q = -1$ is $< 0$, so $Q$ reverses orientation and the clockwise motion of the $\mathbf z$-plane becomes counter-clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e8-viii-z.svg]]
*Canonical $\mathbf z$-plane (unstable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e8-viii-x.svg]]
*Original $(x, y)$-plane (unstable spiral), counter-clockwise.*

### (ix) a single eigenvalue $\lambda = -7$, with the matrix $A$ being a multiple of the identity

$A$ is a multiple of the identity with eigenvalue $-7$: $A = \begin{pmatrix} -7 & 0 \\ 0 & -7 \end{pmatrix}$.

#### Phase portrait

$A = -7I$: every line through the origin is invariant and every solution moves along its own ray, $\mathbf x(t) = e^{-7t}\mathbf x_0$, towards the origin (the origin is a **stable star**). The picture is the same in every basis, so there is no separate canonical plane.

![[attachments/AM-PS/ch4b-e8-ix-x.svg]]
*Stable star: straight rays into the origin.*

## Phase 4: Interpretation and checks

| Item | Origin | Stability |
| :--- | :--- | :--- |
| (i) | saddle | unstable |
| (ii) | spiral, counter-clockwise | stable |
| (iii) | improper node | unstable |
| (iv) | node, tangent to $\mathbf v_1 = (2, 1)$ | stable |
| (v) | improper node | stable |
| (vi) | centre, clockwise | stable, not asymptotically |
| (vii) | node, tangent to $\mathbf v_1 = (3, 2)$ | unstable |
| (viii) | spiral, counter-clockwise | unstable |
| (ix) | star | asymptotically stable |

- The nine items cover the nine pictures of Robinson's classification (Ch. 31, Fig. 31.1, as reproduced in Topic 4 Fig. 4.11; the unstable star is the time reversal of the stable one): saddle (i); stable node (iv); unstable node (vii); stable spiral (ii); unstable spiral (viii); centre (vi); stable star (ix); stable improper node (v); unstable improper node (iii).
- The tangency of nodes was verified on the numerical orbits: the orbits of (iv) are tangent at the origin to $\mathbf v_1 = (2, 1)$ ($|\lambda| = 2 < 3$) and those of (vii) to $\mathbf v_1 = (3, 2)$ ($1 < 5$).
- In (iii) and (v) the sign condition only chooses the orientation of the S-shaped orbits (on which side of the eigenline the orbit moves along $+\mathbf v_1$); the eigenline and the type do not depend on it.
- Trace-determinant check: (i) $\det A = -6 < 0$ saddle; (iv) $\operatorname{tr} = -5$, $\det = 6$, $\Delta = 1 > 0$ stable node; (vii) $\operatorname{tr} = 6$, $\det = 5$ unstable node; (iii) $\operatorname{tr}^2 = 4\det = 676$; (ix) $\operatorname{tr}^2 = 4\det = 196$.
- Spiral (viii) has $\rho/\omega = 5$: one turn multiplies the radius by $e^{2\pi\rho/\omega} = e^{10\pi} \approx 4\times 10^{13}$, so it is a genuine spiral that, on the scale of the figure, looks like almost radial curves (the winding is invisible after the first fraction of a turn); in (ii), $\rho/\omega = -\tfrac13$ the winding is clearly visible.
