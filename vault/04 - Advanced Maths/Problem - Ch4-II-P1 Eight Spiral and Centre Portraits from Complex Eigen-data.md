---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 1"
dificultad: media
id: "e1"
pill: "Complex Eigenvalues • Spirals and Centres • Eight Portraits"
tags:
  - problema-resuelto
  - autovalores-complejos
  - espirales
  - centros
  - retrato-de-fase
---

# Problem 4.II.1: Eight Spiral and Centre Portraits from Complex Eigen-data

> Official exercise 1 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Draw the phase portrait for the equation $d\mathbf x/dt = A\mathbf x$, when the eigenvalues ($\lambda_\pm$) and eigenvectors ($\boldsymbol\eta_\pm$) of $A$ are as given. The sign of $\dot x$ is indicated when $x = 0$ and $y > 0$.

- (i) $\lambda_\pm = 1 \pm 3i \text{ with } \boldsymbol\eta_\pm = (1,\ 2 \mp i),\ \dot x < 0$;
- (ii) $\lambda_\pm = \pm 3i \text{ with } \boldsymbol\eta_\pm = (1 \pm 2i,\ 1 \mp 3i),\ \dot x < 0$;
- (iii) $\lambda_\pm = -2 \pm i \text{ with } \boldsymbol\eta_\pm = (1 \mp i,\ 3 \pm i),\ \dot x > 0$;
- (iv) $\lambda_\pm = -1 \pm i \text{ with } \boldsymbol\eta_\pm = (1,\ \pm i),\ \dot x > 0$;
- (v) $\lambda_\pm = 2 \pm 2i \text{ with } \boldsymbol\eta_\pm = (\pm 3i,\ 5 \mp 4i),\ \dot x < 0$;
- (vi) $\lambda_\pm = 5 \pm 3i \text{ with } \boldsymbol\eta_\pm = (2 \pm 5i,\ \mp i),\ \dot x < 0$;
- (vii) $\lambda_\pm = \pm 7i \text{ with } \boldsymbol\eta_\pm = (1 \pm i,\ -1 \pm 2i),\ \dot x > 0$;
- (viii) $\lambda_\pm = -13 \pm 17i \text{ with } \boldsymbol\eta_\pm = (\pm 6i - 8,\ 4 \mp 5i),\ \dot x > 0$.

## Phase 1: Setup and classification

In each item $\lambda_\pm = \rho \pm i\omega$ with $\omega > 0$ and $\boldsymbol\eta_+ = \mathbf u + i\mathbf w$ is the eigenvector of $\lambda_+ = \rho + i\omega$ (the second eigenvector $\boldsymbol\eta_- = \bar{\boldsymbol\eta}_+$ carries no new information). The type is fixed by $\rho$: $\rho < 0$ stable spiral, $\rho > 0$ unstable spiral, $\rho = 0$ centre (Topic 4 Sec. 7.6). The sense of rotation follows from the vector field at $(0, 1)^T$: $\dot{\mathbf x} = A(0, 1)^T = (a_{12}, a_{22})^T$, and $\dot x = a_{12} > 0$ means clockwise, $\dot x < 0$ counter-clockwise (Topic 4 Sec. 7.8). The sign of $\dot x$ given in the statement is therefore the sense of rotation:

| Item | $\rho$ | $\omega$ | Type | Given sign of $\dot x$ at $(0, 1)$ | Sense |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (i) | $1$ | $3$ | unstable spiral | $<\ 0$ | counter-clockwise |
| (ii) | $0$ | $3$ | centre | $<\ 0$ | counter-clockwise |
| (iii) | $-2$ | $1$ | stable spiral | $>\ 0$ | clockwise |
| (iv) | $-1$ | $1$ | stable spiral | $>\ 0$ | clockwise |
| (v) | $2$ | $2$ | unstable spiral | $<\ 0$ | counter-clockwise |
| (vi) | $5$ | $3$ | unstable spiral | $<\ 0$ | counter-clockwise |
| (vii) | $0$ | $7$ | centre | $>\ 0$ | clockwise |
| (viii) | $-13$ | $17$ | stable spiral | $>\ 0$ | clockwise |

## Phase 2: Formulation

For each item the eigenvector gives $\mathbf u = \operatorname{Re}\boldsymbol\eta_+$ and $\mathbf w = \operatorname{Im}\boldsymbol\eta_+$, hence $Q = [\mathbf u \mid \mathbf w]$ and the canonical form $J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix}$ (rotation clockwise in the $\mathbf z$-plane). The matrix $A = QJQ^{-1}$ is rebuilt, the given sign of $\dot x$ is checked against $a_{12}$, and the portrait is drawn in the $\mathbf z$-plane and in the $(x, y)$-plane ($\mathbf x = Q\mathbf z$).

## Phase 3: Derivation of the eight portraits

### (i) $\lambda_\pm = 1 \pm 3i \text{ with } \boldsymbol\eta_\pm = (1,\ 2 \mp i),\ \dot x < 0$

Split the eigenvector of $\lambda_+ = 1 + 3 i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} 1 \\ 2 - i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = 1$, $\omega = 3$ and

$$ \mathbf u = \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} 0 \\ -1 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix}, \quad J = \begin{pmatrix} 1 & 3 \\ -3 & 1 \end{pmatrix}, \quad \det Q = -1, \quad Q^{-1} = \begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 1\cdot1 + 0\cdot(-3) = 1 \\ (QJ)_{12} &= 1\cdot3 + 0\cdot1 = 3 \\ (QJ)_{21} &= 2\cdot1 + (-1)\cdot(-3) = 5 \\ (QJ)_{22} &= 2\cdot3 + (-1)\cdot1 = 5 \end{aligned} $$

$$ QJ = \begin{pmatrix} 1 & 3 \\ 5 & 5 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 1\cdot1 + 3\cdot2 = 7 \\ (A)_{12} &= 1\cdot0 + 3\cdot(-1) = -3 \\ (A)_{21} &= 5\cdot1 + 5\cdot2 = 15 \\ (A)_{22} &= 5\cdot0 + 5\cdot(-1) = -5 \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} 7 & -3 \\ 15 & -5 \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = -3$, which is negative, in agreement with the statement ($\dot x < 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} 1 \\ 5 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = 1\begin{pmatrix} 1 \\ 2 \end{pmatrix} - 3\begin{pmatrix} 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \\ 5 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 3 \\ 5 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 3\begin{pmatrix} 1 \\ 2 \end{pmatrix} + 1\begin{pmatrix} 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ 5 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix} $$

$\det Q = (1)(-1) - (0)(2) = -1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-1}\begin{pmatrix} -1 & 0 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} 1 & 3 \\ 5 & 5 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 1\cdot1 + 0\cdot5 = 1 \\ (Q^{-1}AQ)_{12} &= 1\cdot3 + 0\cdot5 = 3 \\ (Q^{-1}AQ)_{21} &= 2\cdot1 + (-1)\cdot5 = -3 \\ (Q^{-1}AQ)_{22} &= 2\cdot3 + (-1)\cdot5 = 1 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 1 & 3 \\ -3 & 1 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = z_1 + 3z_2, \qquad \dot z_2 = -3z_1 + z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{1t}\left(c_1\cos 3t + c_2\sin 3t\right), \qquad z_2(t) = e^{1t}\left(c_2\cos 3t - c_1\sin 3t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{1t}\left[\left(c_1\cos 3t + c_2\sin 3t\right)\begin{pmatrix} 1 \\ 2 \end{pmatrix} + \left(c_2\cos 3t - c_1\sin 3t\right)\begin{pmatrix} 0 \\ -1 \end{pmatrix}\right] $$

$$ x(t) = c_{1} e^{t} \cos{3 t} + c_{2} e^{t} \sin{3 t}, \qquad y(t) = c_{1} e^{t} \sin{3 t} + 2 c_{1} e^{t} \cos{3 t} + 2 c_{2} e^{t} \sin{3 t} - c_{2} e^{t} \cos{3 t} $$

#### Phase portrait

$\rho = 1$ and $\omega = 3$: the origin is a **unstable spiral**. In the $\mathbf z$-plane $r = r_0e^{1t}$ and $\theta = \theta_0 - 3t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{\frac{2 \pi}{3}}$ (growing).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} -3 \\ -5 \end{pmatrix}$, so $\dot x = -3$ is $< 0$: to the left at the top of the plane: the rotation is **counter-clockwise**. Cross-check: $\det Q = -1$ is $< 0$, so $Q$ reverses orientation and the clockwise motion of the $\mathbf z$-plane becomes counter-clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-i-z.svg]]
*Canonical $\mathbf z$-plane (unstable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-i-x.svg]]
*Original $(x, y)$-plane (unstable spiral), counter-clockwise.*

### (ii) $\lambda_\pm = \pm 3i \text{ with } \boldsymbol\eta_\pm = (1 \pm 2i,\ 1 \mp 3i),\ \dot x < 0$

Split the eigenvector of $\lambda_+ = 3 i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} 1 + 2 i \\ 1 - 3 i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = 0$, $\omega = 3$ and

$$ \mathbf u = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} 2 \\ -3 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} 1 & 2 \\ 1 & -3 \end{pmatrix}, \quad J = \begin{pmatrix} 0 & 3 \\ -3 & 0 \end{pmatrix}, \quad \det Q = -5, \quad Q^{-1} = \begin{pmatrix} \frac{3}{5} & \frac{2}{5} \\ \frac{1}{5} & - \frac{1}{5} \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 1\cdot0 + 2\cdot(-3) = -6 \\ (QJ)_{12} &= 1\cdot3 + 2\cdot0 = 3 \\ (QJ)_{21} &= 1\cdot0 + (-3)\cdot(-3) = 9 \\ (QJ)_{22} &= 1\cdot3 + (-3)\cdot0 = 3 \end{aligned} $$

$$ QJ = \begin{pmatrix} -6 & 3 \\ 9 & 3 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-6)\cdot\frac{3}{5} + 3\cdot\frac{1}{5} = -3 \\ (A)_{12} &= (-6)\cdot\frac{2}{5} + 3\cdot(- \frac{1}{5}) = -3 \\ (A)_{21} &= 9\cdot\frac{3}{5} + 3\cdot\frac{1}{5} = 6 \\ (A)_{22} &= 9\cdot\frac{2}{5} + 3\cdot(- \frac{1}{5}) = 3 \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} -3 & -3 \\ 6 & 3 \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = -3$, which is negative, in agreement with the statement ($\dot x < 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} -6 \\ 9 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = 0\begin{pmatrix} 1 \\ 1 \end{pmatrix} - 3\begin{pmatrix} 2 \\ -3 \end{pmatrix} = \begin{pmatrix} -6 \\ 9 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 3 \\ 3 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 3\begin{pmatrix} 1 \\ 1 \end{pmatrix} + 0\begin{pmatrix} 2 \\ -3 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 1 & 2 \\ 1 & -3 \end{pmatrix} $$

$\det Q = (1)(-3) - (2)(1) = -5$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-5}\begin{pmatrix} -3 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{3}{5} & \frac{2}{5} \\ \frac{1}{5} & - \frac{1}{5} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} -6 & 3 \\ 9 & 3 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{3}{5}\cdot(-6) + \frac{2}{5}\cdot9 = 0 \\ (Q^{-1}AQ)_{12} &= \frac{3}{5}\cdot3 + \frac{2}{5}\cdot3 = 3 \\ (Q^{-1}AQ)_{21} &= \frac{1}{5}\cdot(-6) + (- \frac{1}{5})\cdot9 = -3 \\ (Q^{-1}AQ)_{22} &= \frac{1}{5}\cdot3 + (- \frac{1}{5})\cdot3 = 0 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 0 & 3 \\ -3 & 0 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = 3z_2, \qquad \dot z_2 = -3z_1 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{0t}\left(c_1\cos 3t + c_2\sin 3t\right), \qquad z_2(t) = e^{0t}\left(c_2\cos 3t - c_1\sin 3t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{0t}\left[\left(c_1\cos 3t + c_2\sin 3t\right)\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \left(c_2\cos 3t - c_1\sin 3t\right)\begin{pmatrix} 2 \\ -3 \end{pmatrix}\right] $$

$$ x(t) = - 2 c_{1} \sin{3 t} + c_{1} \cos{3 t} + c_{2} \sin{3 t} + 2 c_{2} \cos{3 t}, \qquad y(t) = 3 c_{1} \sin{3 t} + c_{1} \cos{3 t} + c_{2} \sin{3 t} - 3 c_{2} \cos{3 t} $$

#### Phase portrait

$\rho = 0$ and $\omega = 3$: the origin is a **centre**. In the $\mathbf z$-plane $r = r_0e^{0t}$ and $\theta = \theta_0 - 3t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and the orbits are circles of period $T = 2\pi/\omega$ (closed orbits).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} -3 \\ 3 \end{pmatrix}$, so $\dot x = -3$ is $< 0$: to the left at the top of the plane: the rotation is **counter-clockwise**. Cross-check: $\det Q = -5$ is $< 0$, so $Q$ reverses orientation and the clockwise motion of the $\mathbf z$-plane becomes counter-clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-ii-z.svg]]
*Canonical $\mathbf z$-plane (centre): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-ii-x.svg]]
*Original $(x, y)$-plane (centre), counter-clockwise.*

### (iii) $\lambda_\pm = -2 \pm i \text{ with } \boldsymbol\eta_\pm = (1 \mp i,\ 3 \pm i),\ \dot x > 0$

Split the eigenvector of $\lambda_+ = -2 + i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} 1 - i \\ 3 + i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = -2$, $\omega = 1$ and

$$ \mathbf u = \begin{pmatrix} 1 \\ 3 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} -1 \\ 1 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} 1 & -1 \\ 3 & 1 \end{pmatrix}, \quad J = \begin{pmatrix} -2 & 1 \\ -1 & -2 \end{pmatrix}, \quad \det Q = 4, \quad Q^{-1} = \begin{pmatrix} \frac{1}{4} & \frac{1}{4} \\ - \frac{3}{4} & \frac{1}{4} \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 1\cdot(-2) + (-1)\cdot(-1) = -1 \\ (QJ)_{12} &= 1\cdot1 + (-1)\cdot(-2) = 3 \\ (QJ)_{21} &= 3\cdot(-2) + 1\cdot(-1) = -7 \\ (QJ)_{22} &= 3\cdot1 + 1\cdot(-2) = 1 \end{aligned} $$

$$ QJ = \begin{pmatrix} -1 & 3 \\ -7 & 1 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-1)\cdot\frac{1}{4} + 3\cdot(- \frac{3}{4}) = - \frac{5}{2} \\ (A)_{12} &= (-1)\cdot\frac{1}{4} + 3\cdot\frac{1}{4} = \frac{1}{2} \\ (A)_{21} &= (-7)\cdot\frac{1}{4} + 1\cdot(- \frac{3}{4}) = - \frac{5}{2} \\ (A)_{22} &= (-7)\cdot\frac{1}{4} + 1\cdot\frac{1}{4} = - \frac{3}{2} \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} - \frac{5}{2} & \frac{1}{2} \\ - \frac{5}{2} & - \frac{3}{2} \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = \frac{1}{2}$, which is positive, in agreement with the statement ($\dot x > 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} -1 \\ -7 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = (-2)\begin{pmatrix} 1 \\ 3 \end{pmatrix} - 1\begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ -7 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 1\begin{pmatrix} 1 \\ 3 \end{pmatrix} + (-2)\begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 1 & -1 \\ 3 & 1 \end{pmatrix} $$

$\det Q = (1)(1) - (-1)(3) = 4$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{4}\begin{pmatrix} 1 & 1 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{4} & \frac{1}{4} \\ - \frac{3}{4} & \frac{1}{4} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} -1 & 3 \\ -7 & 1 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{1}{4}\cdot(-1) + \frac{1}{4}\cdot(-7) = -2 \\ (Q^{-1}AQ)_{12} &= \frac{1}{4}\cdot3 + \frac{1}{4}\cdot1 = 1 \\ (Q^{-1}AQ)_{21} &= (- \frac{3}{4})\cdot(-1) + \frac{1}{4}\cdot(-7) = -1 \\ (Q^{-1}AQ)_{22} &= (- \frac{3}{4})\cdot3 + \frac{1}{4}\cdot1 = -2 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -2 & 1 \\ -1 & -2 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = -2z_1 + z_2, \qquad \dot z_2 = -z_1 - 2z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{-2t}\left(c_1\cos 1t + c_2\sin 1t\right), \qquad z_2(t) = e^{-2t}\left(c_2\cos 1t - c_1\sin 1t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{-2t}\left[\left(c_1\cos 1t + c_2\sin 1t\right)\begin{pmatrix} 1 \\ 3 \end{pmatrix} + \left(c_2\cos 1t - c_1\sin 1t\right)\begin{pmatrix} -1 \\ 1 \end{pmatrix}\right] $$

$$ x(t) = c_{1} e^{-2 t} \sin{t} + c_{1} e^{-2 t} \cos{t} + c_{2} e^{-2 t} \sin{t} - c_{2} e^{-2 t} \cos{t}, \qquad y(t) = - c_{1} e^{-2 t} \sin{t} + 3 c_{1} e^{-2 t} \cos{t} + 3 c_{2} e^{-2 t} \sin{t} + c_{2} e^{-2 t} \cos{t} $$

#### Phase portrait

$\rho = -2$ and $\omega = 1$: the origin is a **stable spiral**. In the $\mathbf z$-plane $r = r_0e^{-2t}$ and $\theta = \theta_0 - 1t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{-4 \pi}$ (shrinking).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} \frac{1}{2} \\ - \frac{3}{2} \end{pmatrix}$, so $\dot x = \frac{1}{2}$ is $> 0$: to the right at the top of the plane: the rotation is **clockwise**. Cross-check: $\det Q = 4$ is $> 0$, so $Q$ preserves orientation and the clockwise motion of the $\mathbf z$-plane becomes clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-iii-z.svg]]
*Canonical $\mathbf z$-plane (stable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-iii-x.svg]]
*Original $(x, y)$-plane (stable spiral), clockwise.*

### (iv) $\lambda_\pm = -1 \pm i \text{ with } \boldsymbol\eta_\pm = (1,\ \pm i),\ \dot x > 0$

Split the eigenvector of $\lambda_+ = -1 + i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} 1 \\ i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = -1$, $\omega = 1$ and

$$ \mathbf u = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad J = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix}, \quad \det Q = 1, \quad Q^{-1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 1\cdot(-1) + 0\cdot(-1) = -1 \\ (QJ)_{12} &= 1\cdot1 + 0\cdot(-1) = 1 \\ (QJ)_{21} &= 0\cdot(-1) + 1\cdot(-1) = -1 \\ (QJ)_{22} &= 0\cdot1 + 1\cdot(-1) = -1 \end{aligned} $$

$$ QJ = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-1)\cdot1 + 1\cdot0 = -1 \\ (A)_{12} &= (-1)\cdot0 + 1\cdot1 = 1 \\ (A)_{21} &= (-1)\cdot1 + (-1)\cdot0 = -1 \\ (A)_{22} &= (-1)\cdot0 + (-1)\cdot1 = -1 \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = 1$, which is positive, in agreement with the statement ($\dot x > 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} -1 \\ -1 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = (-1)\begin{pmatrix} 1 \\ 0 \end{pmatrix} - 1\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ -1 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 1\begin{pmatrix} 1 \\ 0 \end{pmatrix} + (-1)\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $$

$\det Q = (1)(1) - (0)(0) = 1$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{1}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= 1\cdot(-1) + 0\cdot(-1) = -1 \\ (Q^{-1}AQ)_{12} &= 1\cdot1 + 0\cdot(-1) = 1 \\ (Q^{-1}AQ)_{21} &= 0\cdot(-1) + 1\cdot(-1) = -1 \\ (Q^{-1}AQ)_{22} &= 0\cdot1 + 1\cdot(-1) = -1 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = -z_1 + z_2, \qquad \dot z_2 = -z_1 - z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{-1t}\left(c_1\cos 1t + c_2\sin 1t\right), \qquad z_2(t) = e^{-1t}\left(c_2\cos 1t - c_1\sin 1t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{-1t}\left[\left(c_1\cos 1t + c_2\sin 1t\right)\begin{pmatrix} 1 \\ 0 \end{pmatrix} + \left(c_2\cos 1t - c_1\sin 1t\right)\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right] $$

$$ x(t) = c_{1} e^{-t} \cos{t} + c_{2} e^{-t} \sin{t}, \qquad y(t) = - c_{1} e^{-t} \sin{t} + c_{2} e^{-t} \cos{t} $$

#### Phase portrait

$\rho = -1$ and $\omega = 1$: the origin is a **stable spiral**. In the $\mathbf z$-plane $r = r_0e^{-1t}$ and $\theta = \theta_0 - 1t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{-2 \pi}$ (shrinking).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, so $\dot x = 1$ is $> 0$: to the right at the top of the plane: the rotation is **clockwise**. Cross-check: $\det Q = 1$ is $> 0$, so $Q$ preserves orientation and the clockwise motion of the $\mathbf z$-plane becomes clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-iv-z.svg]]
*Canonical $\mathbf z$-plane (stable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-iv-x.svg]]
*Original $(x, y)$-plane (stable spiral), clockwise.*

### (v) $\lambda_\pm = 2 \pm 2i \text{ with } \boldsymbol\eta_\pm = (\pm 3i,\ 5 \mp 4i),\ \dot x < 0$

Split the eigenvector of $\lambda_+ = 2 + 2 i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} 3 i \\ 5 - 4 i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = 2$, $\omega = 2$ and

$$ \mathbf u = \begin{pmatrix} 0 \\ 5 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} 3 \\ -4 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} 0 & 3 \\ 5 & -4 \end{pmatrix}, \quad J = \begin{pmatrix} 2 & 2 \\ -2 & 2 \end{pmatrix}, \quad \det Q = -15, \quad Q^{-1} = \begin{pmatrix} \frac{4}{15} & \frac{1}{5} \\ \frac{1}{3} & 0 \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 0\cdot2 + 3\cdot(-2) = -6 \\ (QJ)_{12} &= 0\cdot2 + 3\cdot2 = 6 \\ (QJ)_{21} &= 5\cdot2 + (-4)\cdot(-2) = 18 \\ (QJ)_{22} &= 5\cdot2 + (-4)\cdot2 = 2 \end{aligned} $$

$$ QJ = \begin{pmatrix} -6 & 6 \\ 18 & 2 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-6)\cdot\frac{4}{15} + 6\cdot\frac{1}{3} = \frac{2}{5} \\ (A)_{12} &= (-6)\cdot\frac{1}{5} + 6\cdot0 = - \frac{6}{5} \\ (A)_{21} &= 18\cdot\frac{4}{15} + 2\cdot\frac{1}{3} = \frac{82}{15} \\ (A)_{22} &= 18\cdot\frac{1}{5} + 2\cdot0 = \frac{18}{5} \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} \frac{2}{5} & - \frac{6}{5} \\ \frac{82}{15} & \frac{18}{5} \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = - \frac{6}{5}$, which is negative, in agreement with the statement ($\dot x < 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} -6 \\ 18 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = 2\begin{pmatrix} 0 \\ 5 \end{pmatrix} - 2\begin{pmatrix} 3 \\ -4 \end{pmatrix} = \begin{pmatrix} -6 \\ 18 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 6 \\ 2 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 2\begin{pmatrix} 0 \\ 5 \end{pmatrix} + 2\begin{pmatrix} 3 \\ -4 \end{pmatrix} = \begin{pmatrix} 6 \\ 2 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 0 & 3 \\ 5 & -4 \end{pmatrix} $$

$\det Q = (0)(-4) - (3)(5) = -15$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-15}\begin{pmatrix} -4 & -3 \\ -5 & 0 \end{pmatrix} = \begin{pmatrix} \frac{4}{15} & \frac{1}{5} \\ \frac{1}{3} & 0 \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} -6 & 6 \\ 18 & 2 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{4}{15}\cdot(-6) + \frac{1}{5}\cdot18 = 2 \\ (Q^{-1}AQ)_{12} &= \frac{4}{15}\cdot6 + \frac{1}{5}\cdot2 = 2 \\ (Q^{-1}AQ)_{21} &= \frac{1}{3}\cdot(-6) + 0\cdot18 = -2 \\ (Q^{-1}AQ)_{22} &= \frac{1}{3}\cdot6 + 0\cdot2 = 2 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 2 & 2 \\ -2 & 2 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = 2z_1 + 2z_2, \qquad \dot z_2 = -2z_1 + 2z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{2t}\left(c_1\cos 2t + c_2\sin 2t\right), \qquad z_2(t) = e^{2t}\left(c_2\cos 2t - c_1\sin 2t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{2t}\left[\left(c_1\cos 2t + c_2\sin 2t\right)\begin{pmatrix} 0 \\ 5 \end{pmatrix} + \left(c_2\cos 2t - c_1\sin 2t\right)\begin{pmatrix} 3 \\ -4 \end{pmatrix}\right] $$

$$ x(t) = - 3 c_{1} e^{2 t} \sin{2 t} + 3 c_{2} e^{2 t} \cos{2 t}, \qquad y(t) = 4 c_{1} e^{2 t} \sin{2 t} + 5 c_{1} e^{2 t} \cos{2 t} + 5 c_{2} e^{2 t} \sin{2 t} - 4 c_{2} e^{2 t} \cos{2 t} $$

#### Phase portrait

$\rho = 2$ and $\omega = 2$: the origin is a **unstable spiral**. In the $\mathbf z$-plane $r = r_0e^{2t}$ and $\theta = \theta_0 - 2t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{2 \pi}$ (growing).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} - \frac{6}{5} \\ \frac{18}{5} \end{pmatrix}$, so $\dot x = - \frac{6}{5}$ is $< 0$: to the left at the top of the plane: the rotation is **counter-clockwise**. Cross-check: $\det Q = -15$ is $< 0$, so $Q$ reverses orientation and the clockwise motion of the $\mathbf z$-plane becomes counter-clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-v-z.svg]]
*Canonical $\mathbf z$-plane (unstable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-v-x.svg]]
*Original $(x, y)$-plane (unstable spiral), counter-clockwise.*

### (vi) $\lambda_\pm = 5 \pm 3i \text{ with } \boldsymbol\eta_\pm = (2 \pm 5i,\ \mp i),\ \dot x < 0$

Split the eigenvector of $\lambda_+ = 5 + 3 i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} 2 + 5 i \\ - i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = 5$, $\omega = 3$ and

$$ \mathbf u = \begin{pmatrix} 2 \\ 0 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} 5 \\ -1 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} 2 & 5 \\ 0 & -1 \end{pmatrix}, \quad J = \begin{pmatrix} 5 & 3 \\ -3 & 5 \end{pmatrix}, \quad \det Q = -2, \quad Q^{-1} = \begin{pmatrix} \frac{1}{2} & \frac{5}{2} \\ 0 & -1 \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 2\cdot5 + 5\cdot(-3) = -5 \\ (QJ)_{12} &= 2\cdot3 + 5\cdot5 = 31 \\ (QJ)_{21} &= 0\cdot5 + (-1)\cdot(-3) = 3 \\ (QJ)_{22} &= 0\cdot3 + (-1)\cdot5 = -5 \end{aligned} $$

$$ QJ = \begin{pmatrix} -5 & 31 \\ 3 & -5 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-5)\cdot\frac{1}{2} + 31\cdot0 = - \frac{5}{2} \\ (A)_{12} &= (-5)\cdot\frac{5}{2} + 31\cdot(-1) = - \frac{87}{2} \\ (A)_{21} &= 3\cdot\frac{1}{2} + (-5)\cdot0 = \frac{3}{2} \\ (A)_{22} &= 3\cdot\frac{5}{2} + (-5)\cdot(-1) = \frac{25}{2} \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} - \frac{5}{2} & - \frac{87}{2} \\ \frac{3}{2} & \frac{25}{2} \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = - \frac{87}{2}$, which is negative, in agreement with the statement ($\dot x < 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} -5 \\ 3 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = 5\begin{pmatrix} 2 \\ 0 \end{pmatrix} - 3\begin{pmatrix} 5 \\ -1 \end{pmatrix} = \begin{pmatrix} -5 \\ 3 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 31 \\ -5 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 3\begin{pmatrix} 2 \\ 0 \end{pmatrix} + 5\begin{pmatrix} 5 \\ -1 \end{pmatrix} = \begin{pmatrix} 31 \\ -5 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 2 & 5 \\ 0 & -1 \end{pmatrix} $$

$\det Q = (2)(-1) - (5)(0) = -2$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-2}\begin{pmatrix} -1 & -5 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & \frac{5}{2} \\ 0 & -1 \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} -5 & 31 \\ 3 & -5 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{1}{2}\cdot(-5) + \frac{5}{2}\cdot3 = 5 \\ (Q^{-1}AQ)_{12} &= \frac{1}{2}\cdot31 + \frac{5}{2}\cdot(-5) = 3 \\ (Q^{-1}AQ)_{21} &= 0\cdot(-5) + (-1)\cdot3 = -3 \\ (Q^{-1}AQ)_{22} &= 0\cdot31 + (-1)\cdot(-5) = 5 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 5 & 3 \\ -3 & 5 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = 5z_1 + 3z_2, \qquad \dot z_2 = -3z_1 + 5z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{5t}\left(c_1\cos 3t + c_2\sin 3t\right), \qquad z_2(t) = e^{5t}\left(c_2\cos 3t - c_1\sin 3t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{5t}\left[\left(c_1\cos 3t + c_2\sin 3t\right)\begin{pmatrix} 2 \\ 0 \end{pmatrix} + \left(c_2\cos 3t - c_1\sin 3t\right)\begin{pmatrix} 5 \\ -1 \end{pmatrix}\right] $$

$$ x(t) = - 5 c_{1} e^{5 t} \sin{3 t} + 2 c_{1} e^{5 t} \cos{3 t} + 2 c_{2} e^{5 t} \sin{3 t} + 5 c_{2} e^{5 t} \cos{3 t}, \qquad y(t) = c_{1} e^{5 t} \sin{3 t} - c_{2} e^{5 t} \cos{3 t} $$

#### Phase portrait

$\rho = 5$ and $\omega = 3$: the origin is a **unstable spiral**. In the $\mathbf z$-plane $r = r_0e^{5t}$ and $\theta = \theta_0 - 3t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{\frac{10 \pi}{3}}$ (growing).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} - \frac{87}{2} \\ \frac{25}{2} \end{pmatrix}$, so $\dot x = - \frac{87}{2}$ is $< 0$: to the left at the top of the plane: the rotation is **counter-clockwise**. Cross-check: $\det Q = -2$ is $< 0$, so $Q$ reverses orientation and the clockwise motion of the $\mathbf z$-plane becomes counter-clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-vi-z.svg]]
*Canonical $\mathbf z$-plane (unstable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-vi-x.svg]]
*Original $(x, y)$-plane (unstable spiral), counter-clockwise.*

### (vii) $\lambda_\pm = \pm 7i \text{ with } \boldsymbol\eta_\pm = (1 \pm i,\ -1 \pm 2i),\ \dot x > 0$

Split the eigenvector of $\lambda_+ = 7 i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} 1 + i \\ -1 + 2 i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = 0$, $\omega = 7$ and

$$ \mathbf u = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} 1 \\ 2 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix}, \quad J = \begin{pmatrix} 0 & 7 \\ -7 & 0 \end{pmatrix}, \quad \det Q = 3, \quad Q^{-1} = \begin{pmatrix} \frac{2}{3} & - \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= 1\cdot0 + 1\cdot(-7) = -7 \\ (QJ)_{12} &= 1\cdot7 + 1\cdot0 = 7 \\ (QJ)_{21} &= (-1)\cdot0 + 2\cdot(-7) = -14 \\ (QJ)_{22} &= (-1)\cdot7 + 2\cdot0 = -7 \end{aligned} $$

$$ QJ = \begin{pmatrix} -7 & 7 \\ -14 & -7 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= (-7)\cdot\frac{2}{3} + 7\cdot\frac{1}{3} = - \frac{7}{3} \\ (A)_{12} &= (-7)\cdot(- \frac{1}{3}) + 7\cdot\frac{1}{3} = \frac{14}{3} \\ (A)_{21} &= (-14)\cdot\frac{2}{3} + (-7)\cdot\frac{1}{3} = - \frac{35}{3} \\ (A)_{22} &= (-14)\cdot(- \frac{1}{3}) + (-7)\cdot\frac{1}{3} = \frac{7}{3} \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} - \frac{7}{3} & \frac{14}{3} \\ - \frac{35}{3} & \frac{7}{3} \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = \frac{14}{3}$, which is positive, in agreement with the statement ($\dot x > 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} -7 \\ -14 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = 0\begin{pmatrix} 1 \\ -1 \end{pmatrix} - 7\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -7 \\ -14 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 7 \\ -7 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 7\begin{pmatrix} 1 \\ -1 \end{pmatrix} + 0\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 7 \\ -7 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix} $$

$\det Q = (1)(2) - (1)(-1) = 3$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{3}\begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{2}{3} & - \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} -7 & 7 \\ -14 & -7 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{2}{3}\cdot(-7) + (- \frac{1}{3})\cdot(-14) = 0 \\ (Q^{-1}AQ)_{12} &= \frac{2}{3}\cdot7 + (- \frac{1}{3})\cdot(-7) = 7 \\ (Q^{-1}AQ)_{21} &= \frac{1}{3}\cdot(-7) + \frac{1}{3}\cdot(-14) = -7 \\ (Q^{-1}AQ)_{22} &= \frac{1}{3}\cdot7 + \frac{1}{3}\cdot(-7) = 0 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 0 & 7 \\ -7 & 0 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = 7z_2, \qquad \dot z_2 = -7z_1 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{0t}\left(c_1\cos 7t + c_2\sin 7t\right), \qquad z_2(t) = e^{0t}\left(c_2\cos 7t - c_1\sin 7t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{0t}\left[\left(c_1\cos 7t + c_2\sin 7t\right)\begin{pmatrix} 1 \\ -1 \end{pmatrix} + \left(c_2\cos 7t - c_1\sin 7t\right)\begin{pmatrix} 1 \\ 2 \end{pmatrix}\right] $$

$$ x(t) = - c_{1} \sin{7 t} + c_{1} \cos{7 t} + c_{2} \sin{7 t} + c_{2} \cos{7 t}, \qquad y(t) = - 2 c_{1} \sin{7 t} - c_{1} \cos{7 t} - c_{2} \sin{7 t} + 2 c_{2} \cos{7 t} $$

#### Phase portrait

$\rho = 0$ and $\omega = 7$: the origin is a **centre**. In the $\mathbf z$-plane $r = r_0e^{0t}$ and $\theta = \theta_0 - 7t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and the orbits are circles of period $T = 2\pi/\omega$ (closed orbits).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} \frac{14}{3} \\ \frac{7}{3} \end{pmatrix}$, so $\dot x = \frac{14}{3}$ is $> 0$: to the right at the top of the plane: the rotation is **clockwise**. Cross-check: $\det Q = 3$ is $> 0$, so $Q$ preserves orientation and the clockwise motion of the $\mathbf z$-plane becomes clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-vii-z.svg]]
*Canonical $\mathbf z$-plane (centre): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-vii-x.svg]]
*Original $(x, y)$-plane (centre), clockwise.*

### (viii) $\lambda_\pm = -13 \pm 17i \text{ with } \boldsymbol\eta_\pm = (\pm 6i - 8,\ 4 \mp 5i),\ \dot x > 0$

Split the eigenvector of $\lambda_+ = -13 + 17 i$ into real and imaginary parts, $\boldsymbol\eta_+ = \begin{pmatrix} -8 + 6 i \\ 4 - 5 i \end{pmatrix} = \mathbf u + i\mathbf w$, so $\rho = -13$, $\omega = 17$ and

$$ \mathbf u = \begin{pmatrix} -8 \\ 4 \end{pmatrix}, \qquad \mathbf w = \begin{pmatrix} 6 \\ -5 \end{pmatrix} $$

The matrix is not given; it is rebuilt from $A\mathbf u = \rho\mathbf u - \omega\mathbf w$, $A\mathbf w = \omega\mathbf u + \rho\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\mathbf u \mid \mathbf w]$, so $A = QJQ^{-1}$:

$$ Q = \begin{pmatrix} -8 & 6 \\ 4 & -5 \end{pmatrix}, \quad J = \begin{pmatrix} -13 & 17 \\ -17 & -13 \end{pmatrix}, \quad \det Q = 16, \quad Q^{-1} = \begin{pmatrix} - \frac{5}{16} & - \frac{3}{8} \\ - \frac{1}{4} & - \frac{1}{2} \end{pmatrix} $$

$$ \begin{aligned} (QJ)_{11} &= (-8)\cdot(-13) + 6\cdot(-17) = 2 \\ (QJ)_{12} &= (-8)\cdot17 + 6\cdot(-13) = -214 \\ (QJ)_{21} &= 4\cdot(-13) + (-5)\cdot(-17) = 33 \\ (QJ)_{22} &= 4\cdot17 + (-5)\cdot(-13) = 133 \end{aligned} $$

$$ QJ = \begin{pmatrix} 2 & -214 \\ 33 & 133 \end{pmatrix} $$

$$ \begin{aligned} (A)_{11} &= 2\cdot(- \frac{5}{16}) + (-214)\cdot(- \frac{1}{4}) = \frac{423}{8} \\ (A)_{12} &= 2\cdot(- \frac{3}{8}) + (-214)\cdot(- \frac{1}{2}) = \frac{425}{4} \\ (A)_{21} &= 33\cdot(- \frac{5}{16}) + 133\cdot(- \frac{1}{4}) = - \frac{697}{16} \\ (A)_{22} &= 33\cdot(- \frac{3}{8}) + 133\cdot(- \frac{1}{2}) = - \frac{631}{8} \end{aligned} $$

$$ A = QJQ^{-1} = \begin{pmatrix} \frac{423}{8} & \frac{425}{4} \\ - \frac{697}{16} & - \frac{631}{8} \end{pmatrix} $$

Check of the given sign: $\dot x$ at $(0, 1)$ equals $a_{12} = \frac{425}{4}$, which is positive, in agreement with the statement ($\dot x > 0$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} 2 \\ 33 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = (-13)\begin{pmatrix} -8 \\ 4 \end{pmatrix} - 17\begin{pmatrix} 6 \\ -5 \end{pmatrix} = \begin{pmatrix} 2 \\ 33 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} -214 \\ 133 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 17\begin{pmatrix} -8 \\ 4 \end{pmatrix} + (-13)\begin{pmatrix} 6 \\ -5 \end{pmatrix} = \begin{pmatrix} -214 \\ 133 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} -8 & 6 \\ 4 & -5 \end{pmatrix} $$

$\det Q = (-8)(-5) - (6)(4) = 16$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{16}\begin{pmatrix} -5 & -6 \\ -4 & -8 \end{pmatrix} = \begin{pmatrix} - \frac{5}{16} & - \frac{3}{8} \\ - \frac{1}{4} & - \frac{1}{2} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} 2 & -214 \\ 33 & 133 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= (- \frac{5}{16})\cdot2 + (- \frac{3}{8})\cdot33 = -13 \\ (Q^{-1}AQ)_{12} &= (- \frac{5}{16})\cdot(-214) + (- \frac{3}{8})\cdot133 = 17 \\ (Q^{-1}AQ)_{21} &= (- \frac{1}{4})\cdot2 + (- \frac{1}{2})\cdot33 = -17 \\ (Q^{-1}AQ)_{22} &= (- \frac{1}{4})\cdot(-214) + (- \frac{1}{2})\cdot133 = -13 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -13 & 17 \\ -17 & -13 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = -13z_1 + 17z_2, \qquad \dot z_2 = -17z_1 - 13z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{-13t}\left(c_1\cos 17t + c_2\sin 17t\right), \qquad z_2(t) = e^{-13t}\left(c_2\cos 17t - c_1\sin 17t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{-13t}\left[\left(c_1\cos 17t + c_2\sin 17t\right)\begin{pmatrix} -8 \\ 4 \end{pmatrix} + \left(c_2\cos 17t - c_1\sin 17t\right)\begin{pmatrix} 6 \\ -5 \end{pmatrix}\right] $$

$$ x(t) = - 6 c_{1} e^{-13 t} \sin{17 t} - 8 c_{1} e^{-13 t} \cos{17 t} - 8 c_{2} e^{-13 t} \sin{17 t} + 6 c_{2} e^{-13 t} \cos{17 t}, \qquad y(t) = 5 c_{1} e^{-13 t} \sin{17 t} + 4 c_{1} e^{-13 t} \cos{17 t} + 4 c_{2} e^{-13 t} \sin{17 t} - 5 c_{2} e^{-13 t} \cos{17 t} $$

#### Phase portrait

$\rho = -13$ and $\omega = 17$: the origin is a **stable spiral**. In the $\mathbf z$-plane $r = r_0e^{-13t}$ and $\theta = \theta_0 - 17t$: the motion is always **clockwise** ($\dot\theta = -\omega < 0$), and one full turn takes $T = 2\pi/\omega$ while the radius is multiplied by $e^{2\pi\rho/\omega} = e^{-\frac{26 \pi}{17}}$ (shrinking).

Sense of rotation in the $\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\dot{\mathbf x} = A(0, 1)^T = \begin{pmatrix} \frac{425}{4} \\ - \frac{631}{8} \end{pmatrix}$, so $\dot x = \frac{425}{4}$ is $> 0$: to the right at the top of the plane: the rotation is **clockwise**. Cross-check: $\det Q = 16$ is $> 0$, so $Q$ preserves orientation and the clockwise motion of the $\mathbf z$-plane becomes clockwise in the $\mathbf x$-plane, in agreement.

![[attachments/AM-PS/ch4b-e1-viii-z.svg]]
*Canonical $\mathbf z$-plane (stable spiral): clockwise, $\dot\theta = -\omega$.*

![[attachments/AM-PS/ch4b-e1-viii-x.svg]]
*Original $(x, y)$-plane (stable spiral), clockwise.*

## Phase 4: Interpretation and checks

| Item | $A$ | Type | Sense of rotation |
| :--- | :--- | :--- | :--- |
| (i) | $\begin{pmatrix} 7 & -3 \\ 15 & -5 \end{pmatrix}$ | unstable spiral | counter-clockwise |
| (ii) | $\begin{pmatrix} -3 & -3 \\ 6 & 3 \end{pmatrix}$ | centre | counter-clockwise |
| (iii) | $\begin{pmatrix} - \frac{5}{2} & \frac{1}{2} \\ - \frac{5}{2} & - \frac{3}{2} \end{pmatrix}$ | stable spiral | clockwise |
| (iv) | $\begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix}$ | stable spiral | clockwise |
| (v) | $\begin{pmatrix} \frac{2}{5} & - \frac{6}{5} \\ \frac{82}{15} & \frac{18}{5} \end{pmatrix}$ | unstable spiral | counter-clockwise |
| (vi) | $\begin{pmatrix} - \frac{5}{2} & - \frac{87}{2} \\ \frac{3}{2} & \frac{25}{2} \end{pmatrix}$ | unstable spiral | counter-clockwise |
| (vii) | $\begin{pmatrix} - \frac{7}{3} & \frac{14}{3} \\ - \frac{35}{3} & \frac{7}{3} \end{pmatrix}$ | centre | clockwise |
| (viii) | $\begin{pmatrix} \frac{423}{8} & \frac{425}{4} \\ - \frac{697}{16} & - \frac{631}{8} \end{pmatrix}$ | stable spiral | clockwise |

- In every item $\det Q$ and the sign of $a_{12}$ agree (the code asserts $\det Q > 0 \Leftrightarrow a_{12} > 0$), which is the Topic 4 rule: the $\mathbf z$-plane turns clockwise, and $Q$ reverses the sense exactly when $\det Q < 0$.
- Centres (ii) and (vii) ($\rho = 0$): $\operatorname{tr}A = 0$ and $\det A = \omega^2 > 0$; the orbits are closed ellipses with period $2\pi/\omega$ ($2\pi/3$ and $2\pi/7$).
- Spirals: (i), (v), (vi) unstable; (iii), (iv), (viii) stable. The growth/decay factor per turn is $e^{2\pi\rho/\omega}$, stated in each item; (viii) decays extremely fast ($e^{-26\pi/17} \approx 0.008$ per turn), so its spiral is nearly invisible after one turn.
- The eigen-data are consistent: $A\boldsymbol\eta_+ = \lambda_+\boldsymbol\eta_+$ holds in each item by construction of $A$ (Eq. 7.4 verified entry by entry).
