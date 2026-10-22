---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 3"
dificultad: media
id: "e3"
pill: "Canonical Form • Q = [u | w] • Four Matrices"
tags:
  - problema-resuelto
  - forma-canonica
  - autovalores-complejos
  - cambio-de-base
---

# Problem 4.II.3: Canonical Form of Four Systems with Complex Eigenvalues

> Official exercise 3 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

For the following equations find the eigenvalues and eigenvectors of the matrix on the right-hand side, and hence find the coordinate transformation that will put the equations into their standard simple (canonical) form. Show that this transformation has the desired effect.

- (i) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}\mathbf x$;
- (ii) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} -2 & 3 \\ -6 & 4 \end{pmatrix}\mathbf x$;
- (iii) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} -11 & -2 \\ 13 & -9 \end{pmatrix}\mathbf x$;
- (iv) $\dfrac{d\mathbf x}{dt} = \begin{pmatrix} 7 & -5 \\ 10 & -3 \end{pmatrix}\mathbf x$.

## Phase 1: Setup

The standard (canonical) form for a complex pair $\rho \pm i\omega$ is $\dot{\mathbf z} = J\mathbf z$ with $J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix}$, reached by $\mathbf z = Q^{-1}\mathbf x$ with $Q = [\mathbf u \mid \mathbf w]$, $\mathbf u + i\mathbf w$ the eigenvector of $\rho + i\omega$ (Topic 4 Sec. 7.4). For every matrix $\Delta = (\operatorname{tr}A)^2 - 4\det A < 0$ (checked in each item), so the eigenvalues are complex conjugate.

## Phase 2: Formulation

Steps for each matrix: characteristic equation, eigenvalue $\rho + i\omega$, eigenvector via the first row, $\mathbf u, \mathbf w$, relations (7.4), $Q$ and $Q^{-1}$, and the explicit product $Q^{-1}AQ = J$.

> [!info] Method of the class notes [Notes, p. 10]
> The construction of the notes: complex diagonalisation $A = PDP^{-1}$ with $P = (\mathbf v_+ \mid \mathbf v_-)$, then $Q = (\mathbf v_1 \mid \mathbf v_2) = PM$ with $M = \begin{pmatrix} 1/2 & -i/2 \\ 1/2 & i/2 \end{pmatrix}$, so that $Q^{-1}AQ = M^{-1}P^{-1}APM = M^{-1}DM = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix}$. The explicit product $Q^{-1}AQ$ computed for each matrix below checks this canonical form.

## Phase 3: Derivation

### (i) $A = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 0 - \lambda & -1 \\ 1 & -1 - \lambda \end{vmatrix} = (0 - \lambda)(-1 - \lambda) - (-1)(1) $$

$$ = \lambda^2 - (0 + (-1))\lambda + (0\cdot(-1) - (-1)\cdot1) = \lambda^2 - (-1)\lambda + (1) = \lambda^{2} + \lambda + 1 $$

$\operatorname{tr}A = -1$, $\det A = 1$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 1 - 4 = -3$.

$\Delta < 0$: a complex-conjugate pair. $\lambda = \dfrac{-1 \pm \sqrt{-3}}{2} = \dfrac{-1 \pm \sqrt{3} i}{2}$, so

$$ \lambda_\pm = - \frac{1}{2} \pm \frac{\sqrt{3}}{2}\,i \qquad (\rho = - \frac{1}{2},\ \omega = \frac{\sqrt{3}}{2} > 0) $$

#### Eigenvector of the eigenvalue with positive imaginary part

For $\lambda = \rho + i\omega = - \frac{1}{2} + \frac{\sqrt{3} i}{2}$ the first row of $(A - \lambda I)\mathbf v = \mathbf 0$ reads $(\frac{1}{2} - \frac{\sqrt{3} i}{2})\,v_1 + (-1)\,v_2 = 0$ (the coefficient of $v_2$ is non-zero because $\Delta < 0$ forces $bc < 0$). Choose $v_1 = -1$; then $v_2 = -(\frac{1}{2} - \frac{\sqrt{3} i}{2}) = - \frac{1}{2} + \frac{\sqrt{3} i}{2}$:

$$ \mathbf v = \begin{pmatrix} -1 \\ - \frac{1}{2} + \frac{\sqrt{3} i}{2} \end{pmatrix} = \underbrace{\begin{pmatrix} -1 \\ - \frac{1}{2} \end{pmatrix}}_{\mathbf u} + i\,\underbrace{\begin{pmatrix} 0 \\ \frac{\sqrt{3}}{2} \end{pmatrix}}_{\mathbf w} $$

Check with the second row: $1\cdot(-1) + (- \frac{1}{2} - \frac{\sqrt{3} i}{2})(- \frac{1}{2} + \frac{\sqrt{3} i}{2}) = -1 + 1 = 0$ (using $i^2 = -1$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} \frac{1}{2} \\ - \frac{1}{2} \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = (- \frac{1}{2})\begin{pmatrix} -1 \\ - \frac{1}{2} \end{pmatrix} - \frac{\sqrt{3}}{2}\begin{pmatrix} 0 \\ \frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} \\ - \frac{1}{2} \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} - \frac{\sqrt{3}}{2} \\ - \frac{\sqrt{3}}{2} \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = \frac{\sqrt{3}}{2}\begin{pmatrix} -1 \\ - \frac{1}{2} \end{pmatrix} + (- \frac{1}{2})\begin{pmatrix} 0 \\ \frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} - \frac{\sqrt{3}}{2} \\ - \frac{\sqrt{3}}{2} \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} -1 & 0 \\ - \frac{1}{2} & \frac{\sqrt{3}}{2} \end{pmatrix} $$

$\det Q = (-1)(\frac{\sqrt{3}}{2}) - (0)(- \frac{1}{2}) = - \frac{\sqrt{3}}{2}$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{- \frac{\sqrt{3}}{2}}\begin{pmatrix} \frac{\sqrt{3}}{2} & 0 \\ \frac{1}{2} & -1 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ - \frac{\sqrt{3}}{3} & \frac{2 \sqrt{3}}{3} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} \frac{1}{2} & - \frac{\sqrt{3}}{2} \\ - \frac{1}{2} & - \frac{\sqrt{3}}{2} \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= (-1)\cdot\frac{1}{2} + 0\cdot(- \frac{1}{2}) = - \frac{1}{2} \\ (Q^{-1}AQ)_{12} &= (-1)\cdot(- \frac{\sqrt{3}}{2}) + 0\cdot(- \frac{\sqrt{3}}{2}) = \frac{\sqrt{3}}{2} \\ (Q^{-1}AQ)_{21} &= (- \frac{\sqrt{3}}{3})\cdot\frac{1}{2} + \frac{2 \sqrt{3}}{3}\cdot(- \frac{1}{2}) = - \frac{\sqrt{3}}{2} \\ (Q^{-1}AQ)_{22} &= (- \frac{\sqrt{3}}{3})\cdot(- \frac{\sqrt{3}}{2}) + \frac{2 \sqrt{3}}{3}\cdot(- \frac{\sqrt{3}}{2}) = - \frac{1}{2} \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} - \frac{1}{2} & \frac{\sqrt{3}}{2} \\ - \frac{\sqrt{3}}{2} & - \frac{1}{2} \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = -\frac{1}{2}z_1 + \frac{\sqrt{3}}{2}z_2, \qquad \dot z_2 = -\frac{\sqrt{3}}{2}z_1 - \frac{1}{2}z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{- \frac{1}{2}t}\left(c_1\cos \frac{\sqrt{3}}{2}t + c_2\sin \frac{\sqrt{3}}{2}t\right), \qquad z_2(t) = e^{- \frac{1}{2}t}\left(c_2\cos \frac{\sqrt{3}}{2}t - c_1\sin \frac{\sqrt{3}}{2}t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{- \frac{1}{2}t}\left[\left(c_1\cos \frac{\sqrt{3}}{2}t + c_2\sin \frac{\sqrt{3}}{2}t\right)\begin{pmatrix} -1 \\ - \frac{1}{2} \end{pmatrix} + \left(c_2\cos \frac{\sqrt{3}}{2}t - c_1\sin \frac{\sqrt{3}}{2}t\right)\begin{pmatrix} 0 \\ \frac{\sqrt{3}}{2} \end{pmatrix}\right] $$

$$ x(t) = - c_{1} e^{-\frac{t}{2}} \cos{\frac{\sqrt{3} t}{2}} - c_{2} e^{-\frac{t}{2}} \sin{\frac{\sqrt{3} t}{2}}, \qquad y(t) = - \frac{\sqrt{3} c_{1} e^{-\frac{t}{2}} \sin{\frac{\sqrt{3} t}{2}}}{2} - \frac{c_{1} e^{-\frac{t}{2}} \cos{\frac{\sqrt{3} t}{2}}}{2} - \frac{c_{2} e^{-\frac{t}{2}} \sin{\frac{\sqrt{3} t}{2}}}{2} + \frac{\sqrt{3} c_{2} e^{-\frac{t}{2}} \cos{\frac{\sqrt{3} t}{2}}}{2} $$

The canonical system is $\dot z_1 = - \frac{1}{2}z_1 + (\frac{\sqrt{3}}{2})z_2$, $\dot z_2 = -(\frac{\sqrt{3}}{2})z_1 + - \frac{1}{2}z_2$: a rotation clockwise with angular speed $\omega = \frac{\sqrt{3}}{2}$ combined with a radial factor $e^{- \frac{1}{2}t}$.

### (ii) $A = \begin{pmatrix} -2 & 3 \\ -6 & 4 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} -2 - \lambda & 3 \\ -6 & 4 - \lambda \end{vmatrix} = (-2 - \lambda)(4 - \lambda) - (3)(-6) $$

$$ = \lambda^2 - (-2 + 4)\lambda + (-2\cdot4 - 3\cdot(-6)) = \lambda^2 - (2)\lambda + (10) = \lambda^{2} - 2 \lambda + 10 $$

$\operatorname{tr}A = 2$, $\det A = 10$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 4 - 40 = -36$.

$\Delta < 0$: a complex-conjugate pair. $\lambda = \dfrac{2 \pm \sqrt{-36}}{2} = \dfrac{2 \pm 6 i}{2}$, so

$$ \lambda_\pm = 1 \pm 3\,i \qquad (\rho = 1,\ \omega = 3 > 0) $$

#### Eigenvector of the eigenvalue with positive imaginary part

For $\lambda = \rho + i\omega = 1 + 3 i$ the first row of $(A - \lambda I)\mathbf v = \mathbf 0$ reads $(-3 - 3 i)\,v_1 + 3\,v_2 = 0$ (the coefficient of $v_2$ is non-zero because $\Delta < 0$ forces $bc < 0$). Choose $v_1 = 3$; then $v_2 = -(-3 - 3 i) = 3 + 3 i$:

$$ \mathbf v = \begin{pmatrix} 3 \\ 3 + 3 i \end{pmatrix} = \underbrace{\begin{pmatrix} 3 \\ 3 \end{pmatrix}}_{\mathbf u} + i\,\underbrace{\begin{pmatrix} 0 \\ 3 \end{pmatrix}}_{\mathbf w} $$

Check with the second row: $-6\cdot3 + (3 - 3 i)(3 + 3 i) = -18 + 18 = 0$ (using $i^2 = -1$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} 3 \\ -6 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = 1\begin{pmatrix} 3 \\ 3 \end{pmatrix} - 3\begin{pmatrix} 0 \\ 3 \end{pmatrix} = \begin{pmatrix} 3 \\ -6 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} 9 \\ 12 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 3\begin{pmatrix} 3 \\ 3 \end{pmatrix} + 1\begin{pmatrix} 0 \\ 3 \end{pmatrix} = \begin{pmatrix} 9 \\ 12 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} 3 & 0 \\ 3 & 3 \end{pmatrix} $$

$\det Q = (3)(3) - (0)(3) = 9$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{9}\begin{pmatrix} 3 & 0 \\ -3 & 3 \end{pmatrix} = \begin{pmatrix} \frac{1}{3} & 0 \\ - \frac{1}{3} & \frac{1}{3} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} 3 & 9 \\ -6 & 12 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= \frac{1}{3}\cdot3 + 0\cdot(-6) = 1 \\ (Q^{-1}AQ)_{12} &= \frac{1}{3}\cdot9 + 0\cdot12 = 3 \\ (Q^{-1}AQ)_{21} &= (- \frac{1}{3})\cdot3 + \frac{1}{3}\cdot(-6) = -3 \\ (Q^{-1}AQ)_{22} &= (- \frac{1}{3})\cdot9 + \frac{1}{3}\cdot12 = 1 \end{aligned} $$

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

$$ \mathbf x(t) = e^{1t}\left[\left(c_1\cos 3t + c_2\sin 3t\right)\begin{pmatrix} 3 \\ 3 \end{pmatrix} + \left(c_2\cos 3t - c_1\sin 3t\right)\begin{pmatrix} 0 \\ 3 \end{pmatrix}\right] $$

$$ x(t) = 3 c_{1} e^{t} \cos{3 t} + 3 c_{2} e^{t} \sin{3 t}, \qquad y(t) = - 3 c_{1} e^{t} \sin{3 t} + 3 c_{1} e^{t} \cos{3 t} + 3 c_{2} e^{t} \sin{3 t} + 3 c_{2} e^{t} \cos{3 t} $$

The canonical system is $\dot z_1 = 1z_1 + (3)z_2$, $\dot z_2 = -(3)z_1 + 1z_2$: a rotation clockwise with angular speed $\omega = 3$ combined with a radial factor $e^{1t}$.

### (iii) $A = \begin{pmatrix} -11 & -2 \\ 13 & -9 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} -11 - \lambda & -2 \\ 13 & -9 - \lambda \end{vmatrix} = (-11 - \lambda)(-9 - \lambda) - (-2)(13) $$

$$ = \lambda^2 - (-11 + (-9))\lambda + (-11\cdot(-9) - (-2)\cdot13) = \lambda^2 - (-20)\lambda + (125) = \lambda^{2} + 20 \lambda + 125 $$

$\operatorname{tr}A = -20$, $\det A = 125$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 400 - 500 = -100$.

$\Delta < 0$: a complex-conjugate pair. $\lambda = \dfrac{-20 \pm \sqrt{-100}}{2} = \dfrac{-20 \pm 10 i}{2}$, so

$$ \lambda_\pm = -10 \pm 5\,i \qquad (\rho = -10,\ \omega = 5 > 0) $$

#### Eigenvector of the eigenvalue with positive imaginary part

For $\lambda = \rho + i\omega = -10 + 5 i$ the first row of $(A - \lambda I)\mathbf v = \mathbf 0$ reads $(-1 - 5 i)\,v_1 + (-2)\,v_2 = 0$ (the coefficient of $v_2$ is non-zero because $\Delta < 0$ forces $bc < 0$). Choose $v_1 = -2$; then $v_2 = -(-1 - 5 i) = 1 + 5 i$:

$$ \mathbf v = \begin{pmatrix} -2 \\ 1 + 5 i \end{pmatrix} = \underbrace{\begin{pmatrix} -2 \\ 1 \end{pmatrix}}_{\mathbf u} + i\,\underbrace{\begin{pmatrix} 0 \\ 5 \end{pmatrix}}_{\mathbf w} $$

Check with the second row: $13\cdot(-2) + (1 - 5 i)(1 + 5 i) = -26 + 26 = 0$ (using $i^2 = -1$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} 20 \\ -35 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = (-10)\begin{pmatrix} -2 \\ 1 \end{pmatrix} - 5\begin{pmatrix} 0 \\ 5 \end{pmatrix} = \begin{pmatrix} 20 \\ -35 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} -10 \\ -45 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 5\begin{pmatrix} -2 \\ 1 \end{pmatrix} + (-10)\begin{pmatrix} 0 \\ 5 \end{pmatrix} = \begin{pmatrix} -10 \\ -45 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} -2 & 0 \\ 1 & 5 \end{pmatrix} $$

$\det Q = (-2)(5) - (0)(1) = -10$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-10}\begin{pmatrix} 5 & 0 \\ -1 & -2 \end{pmatrix} = \begin{pmatrix} - \frac{1}{2} & 0 \\ \frac{1}{10} & \frac{1}{5} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} 20 & -10 \\ -35 & -45 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= (- \frac{1}{2})\cdot20 + 0\cdot(-35) = -10 \\ (Q^{-1}AQ)_{12} &= (- \frac{1}{2})\cdot(-10) + 0\cdot(-45) = 5 \\ (Q^{-1}AQ)_{21} &= \frac{1}{10}\cdot20 + \frac{1}{5}\cdot(-35) = -5 \\ (Q^{-1}AQ)_{22} &= \frac{1}{10}\cdot(-10) + \frac{1}{5}\cdot(-45) = -10 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} -10 & 5 \\ -5 & -10 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = -10z_1 + 5z_2, \qquad \dot z_2 = -5z_1 - 10z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{-10t}\left(c_1\cos 5t + c_2\sin 5t\right), \qquad z_2(t) = e^{-10t}\left(c_2\cos 5t - c_1\sin 5t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{-10t}\left[\left(c_1\cos 5t + c_2\sin 5t\right)\begin{pmatrix} -2 \\ 1 \end{pmatrix} + \left(c_2\cos 5t - c_1\sin 5t\right)\begin{pmatrix} 0 \\ 5 \end{pmatrix}\right] $$

$$ x(t) = - 2 c_{1} e^{-10 t} \cos{5 t} - 2 c_{2} e^{-10 t} \sin{5 t}, \qquad y(t) = - 5 c_{1} e^{-10 t} \sin{5 t} + c_{1} e^{-10 t} \cos{5 t} + c_{2} e^{-10 t} \sin{5 t} + 5 c_{2} e^{-10 t} \cos{5 t} $$

The canonical system is $\dot z_1 = -10z_1 + (5)z_2$, $\dot z_2 = -(5)z_1 + -10z_2$: a rotation clockwise with angular speed $\omega = 5$ combined with a radial factor $e^{-10t}$.

### (iv) $A = \begin{pmatrix} 7 & -5 \\ 10 & -3 \end{pmatrix}$

Characteristic equation $\det(A - \lambda I) = 0$ (Topic 4, Eq. 27.8):

$$ \det(A - \lambda I) = \begin{vmatrix} 7 - \lambda & -5 \\ 10 & -3 - \lambda \end{vmatrix} = (7 - \lambda)(-3 - \lambda) - (-5)(10) $$

$$ = \lambda^2 - (7 + (-3))\lambda + (7\cdot(-3) - (-5)\cdot10) = \lambda^2 - (4)\lambda + (29) = \lambda^{2} - 4 \lambda + 29 $$

$\operatorname{tr}A = 4$, $\det A = 29$, discriminant $\Delta = (\operatorname{tr}A)^2 - 4\det A = 16 - 116 = -100$.

$\Delta < 0$: a complex-conjugate pair. $\lambda = \dfrac{4 \pm \sqrt{-100}}{2} = \dfrac{4 \pm 10 i}{2}$, so

$$ \lambda_\pm = 2 \pm 5\,i \qquad (\rho = 2,\ \omega = 5 > 0) $$

#### Eigenvector of the eigenvalue with positive imaginary part

For $\lambda = \rho + i\omega = 2 + 5 i$ the first row of $(A - \lambda I)\mathbf v = \mathbf 0$ reads $(5 - 5 i)\,v_1 + (-5)\,v_2 = 0$ (the coefficient of $v_2$ is non-zero because $\Delta < 0$ forces $bc < 0$). Choose $v_1 = -5$; then $v_2 = -(5 - 5 i) = -5 + 5 i$:

$$ \mathbf v = \begin{pmatrix} -5 \\ -5 + 5 i \end{pmatrix} = \underbrace{\begin{pmatrix} -5 \\ -5 \end{pmatrix}}_{\mathbf u} + i\,\underbrace{\begin{pmatrix} 0 \\ 5 \end{pmatrix}}_{\mathbf w} $$

Check with the second row: $10\cdot(-5) + (-5 - 5 i)(-5 + 5 i) = -50 + 50 = 0$ (using $i^2 = -1$).

#### How $A$ acts on $\mathbf u$ and $\mathbf w$

Separating the real and imaginary parts of $A\mathbf v = \lambda\mathbf v$ gives (Topic 4, Eq. 7.4) $A\mathbf u = \rho\mathbf u - \omega\mathbf w$ and $A\mathbf w = \omega\mathbf u + \rho\mathbf w$. Verification with the numbers:

$$ A\mathbf u = \begin{pmatrix} -10 \\ -35 \end{pmatrix}, \qquad \rho\mathbf u - \omega\mathbf w = 2\begin{pmatrix} -5 \\ -5 \end{pmatrix} - 5\begin{pmatrix} 0 \\ 5 \end{pmatrix} = \begin{pmatrix} -10 \\ -35 \end{pmatrix} $$

$$ A\mathbf w = \begin{pmatrix} -25 \\ -15 \end{pmatrix}, \qquad \omega\mathbf u + \rho\mathbf w = 5\begin{pmatrix} -5 \\ -5 \end{pmatrix} + 2\begin{pmatrix} 0 \\ 5 \end{pmatrix} = \begin{pmatrix} -25 \\ -15 \end{pmatrix} $$

#### Change of coordinates

$\mathbf u$ and $\mathbf w$ are linearly independent (they are not parallel when $\omega \neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\mathbf u, \mathbf w$,

$$ Q = [\mathbf u \mid \mathbf w] = \begin{pmatrix} -5 & 0 \\ -5 & 5 \end{pmatrix} $$

$\det Q = (-5)(5) - (0)(-5) = -25$, which is not zero, so $Q$ is invertible. For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (Robinson, Appendix B):

$$ Q^{-1} = \frac{1}{-25}\begin{pmatrix} 5 & 0 \\ 5 & -5 \end{pmatrix} = \begin{pmatrix} - \frac{1}{5} & 0 \\ - \frac{1}{5} & \frac{1}{5} \end{pmatrix} $$

Compute $AQ = [A\mathbf u \mid A\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:

$$ AQ = \begin{pmatrix} -10 & -25 \\ -35 & -15 \end{pmatrix} $$

$$ \begin{aligned} (Q^{-1}AQ)_{11} &= (- \frac{1}{5})\cdot(-10) + 0\cdot(-35) = 2 \\ (Q^{-1}AQ)_{12} &= (- \frac{1}{5})\cdot(-25) + 0\cdot(-15) = 5 \\ (Q^{-1}AQ)_{21} &= (- \frac{1}{5})\cdot(-10) + \frac{1}{5}\cdot(-35) = -5 \\ (Q^{-1}AQ)_{22} &= (- \frac{1}{5})\cdot(-25) + \frac{1}{5}\cdot(-15) = 2 \end{aligned} $$

$$ Q^{-1}AQ = \begin{pmatrix} 2 & 5 \\ -5 & 2 \end{pmatrix} = J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix} $$

#### Solution in the canonical plane

$$ \dot z_1 = 2z_1 + 5z_2, \qquad \dot z_2 = -5z_1 + 2z_2 $$

The two equations are coupled, but they say "scale and rotate", which polar coordinates express directly: $z_1 = r\cos\theta$, $z_2 = r\sin\theta$ (Topic 4, Sec. 7.5).

**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\dot r = 2z_1\dot z_1 + 2z_2\dot z_2$. Substituting $\dot z_1 = \rho z_1 + \omega z_2$ and $\dot z_2 = -\omega z_1 + \rho z_2$:

$$ r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2 $$

The terms in $\omega$ cancel. Dividing by $r \neq 0$ (the origin is the equilibrium): $\dot r = \rho r$.

**The angle.** Differentiate $\tan\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\sec^2\theta\,\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/z_1^2$. Since $\sec^2\theta = r^2/z_1^2$, $\dot\theta = (z_1\dot z_2 - z_2\dot z_1)/r^2$, and

$$ z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega $$

**Integration.** $\frac{d}{dt}\left(e^{-\rho t}r\right) = e^{-\rho t}(\dot r - \rho r) = 0$, and Barrow's rule between $0$ and $t$, $\left[e^{-\rho s}r(s)\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\rho t}$. For the angle, $\theta(t) - \theta_0 = \int_0^t(-\omega)\,ds = -\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\cos\theta_0 = z_1(0)$, $c_2 = r_0\sin\theta_0 = z_2(0)$ and the subtraction formulas $\cos(\theta_0 - \omega t) = \cos\theta_0\cos\omega t + \sin\theta_0\sin\omega t$, $\sin(\theta_0 - \omega t) = \sin\theta_0\cos\omega t - \cos\theta_0\sin\omega t$:

$$ z_1(t) = e^{2t}\left(c_1\cos 5t + c_2\sin 5t\right), \qquad z_2(t) = e^{2t}\left(c_2\cos 5t - c_1\sin 5t\right) $$

Check by substitution (product rule and chain rule): $\dot z_1 = \rho z_1 + e^{\rho t}\omega\left(-c_1\sin\omega t + c_2\cos\omega t\right) = \rho z_1 + \omega z_2$ and $\dot z_2 = \rho z_2 + e^{\rho t}\omega\left(-c_2\sin\omega t - c_1\cos\omega t\right) = \rho z_2 - \omega z_1$, as required.

#### Back to the original coordinates

$\mathbf x = Q\mathbf z = z_1\mathbf u + z_2\mathbf w$, so

$$ \mathbf x(t) = e^{2t}\left[\left(c_1\cos 5t + c_2\sin 5t\right)\begin{pmatrix} -5 \\ -5 \end{pmatrix} + \left(c_2\cos 5t - c_1\sin 5t\right)\begin{pmatrix} 0 \\ 5 \end{pmatrix}\right] $$

$$ x(t) = - 5 c_{1} e^{2 t} \cos{5 t} - 5 c_{2} e^{2 t} \sin{5 t}, \qquad y(t) = - 5 c_{1} e^{2 t} \sin{5 t} - 5 c_{1} e^{2 t} \cos{5 t} - 5 c_{2} e^{2 t} \sin{5 t} + 5 c_{2} e^{2 t} \cos{5 t} $$

The canonical system is $\dot z_1 = 2z_1 + (5)z_2$, $\dot z_2 = -(5)z_1 + 2z_2$: a rotation clockwise with angular speed $\omega = 5$ combined with a radial factor $e^{2t}$.

## Phase 4: Interpretation and checks

- In each item the explicit product $Q^{-1}AQ$ reproduces $J$ exactly (entry-by-entry arithmetic above).
- (i) has an irrational $\omega = \sqrt3/2$ (eigenvalues $-\tfrac12 \pm \tfrac{\sqrt3}{2}i$, with the surds carried exactly): stable spiral. (ii) $1 \pm 3i$, unstable spiral; (iii) $-10 \pm 5i$, stable spiral (fast decay, ratio $|\rho|/\omega = 2$); (iv) $2 \pm 5i$, unstable spiral.
- The orientation of $Q$ ($\det Q$ sign) decides whether the clockwise rotation of the $\mathbf z$-plane stays clockwise in the $\mathbf x$-plane; it is $b\omega$ here (positive iff $b > 0$).
- The eigenvalues of each matrix satisfy $\lambda_+ + \lambda_- = \operatorname{tr}A$ and $\lambda_+\lambda_- = \det A$ (checked in the text).
