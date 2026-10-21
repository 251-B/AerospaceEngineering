---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-ii_2627.pdf - Exercise 2"
dificultad: media
id: "e2"
pill: "Real General Solution • Euler's Formula"
tags:
  - problema-resuelto
  - solucion-general
  - autovalores-complejos
  - formula-de-euler
---

# Problem 4.II.2: General Solutions for the Eight Complex Eigen-data

> Official exercise 2 of the sheet `probls_ch4-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 2]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Write down the general solution of the equation $d\mathbf x/dt = A\mathbf x$, when the eigenvalues ($\lambda_\pm$) and eigenvectors ($\boldsymbol\eta_\pm$) of $A$ are those in the previous exercise.

## Phase 1: Setup

The eight eigen-data are those of Exercise 1 (listed there). For each, $\boldsymbol\eta_+ = \mathbf u + i\mathbf w$ is the eigenvector of $\lambda_+ = \rho + i\omega$.

## Phase 2: Formulation: the real general solution

Complex solutions $e^{\lambda_+t}\boldsymbol\eta_+$ and $e^{\lambda_-t}\bar{\boldsymbol\eta}_+$ combine into real ones: choose conjugate coefficients, $\mathbf x = 2\operatorname{Re}\left[Ce^{(\rho + i\omega)t}(\mathbf u + i\mathbf w)\right]$ with $C = \alpha + i\beta$. Expanding $e^{i\omega t} = \cos\omega t + i\sin\omega t$ (Euler) and keeping the real part, with $c_1 = 2\alpha$, $c_2 = -2\beta$ (Topic 4 Eq. 7.3, Robinson Eq. 29.2):

$$ \mathbf x(t) = e^{\rho t}\Big[\left(c_1\cos\omega t + c_2\sin\omega t\right)\mathbf u + \left(c_2\cos\omega t - c_1\sin\omega t\right)\mathbf w\Big] $$

Check of the derivation of the real part: $(a + ib)(\mathbf u + i\mathbf w)$ has real part $a\mathbf u - b\mathbf w$ because $i\cdot i = -1$; with $a = \alpha\cos\omega t - \beta\sin\omega t$ and $b = \beta\cos\omega t + \alpha\sin\omega t$ this is $\frac12[(c_1\cos\omega t + c_2\sin\omega t)\mathbf u + (c_2\cos\omega t - c_1\sin\omega t)\mathbf w]$ after substituting $\alpha = c_1/2$, $\beta = -c_2/2$.

## Phase 3: Derivation: the eight solutions

### (i) $\lambda_\pm = 1 \pm 3i \text{ with } \boldsymbol\eta_\pm = (1,\ 2 \mp i),\ \dot x < 0$

$\rho = 1$, $\omega = 3$, $\mathbf u = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} 0 \\ -1 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{1t}\left[\left(c_1\cos 3t + c_2\sin 3t\right)\begin{pmatrix} 1 \\ 2 \end{pmatrix} + \left(c_2\cos 3t - c_1\sin 3t\right)\begin{pmatrix} 0 \\ -1 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = c_{1} e^{t} \cos{3 t} + c_{2} e^{t} \sin{3 t}, \qquad y(t) = c_{1} e^{t} \sin{3 t} + 2 c_{1} e^{t} \cos{3 t} + 2 c_{2} e^{t} \sin{3 t} - c_{2} e^{t} \cos{3 t} $$

Check: with $A = \begin{pmatrix} 7 & -3 \\ 15 & -5 \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

### (ii) $\lambda_\pm = \pm 3i \text{ with } \boldsymbol\eta_\pm = (1 \pm 2i,\ 1 \mp 3i),\ \dot x < 0$

$\rho = 0$, $\omega = 3$, $\mathbf u = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} 2 \\ -3 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{0t}\left[\left(c_1\cos 3t + c_2\sin 3t\right)\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \left(c_2\cos 3t - c_1\sin 3t\right)\begin{pmatrix} 2 \\ -3 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = - 2 c_{1} \sin{3 t} + c_{1} \cos{3 t} + c_{2} \sin{3 t} + 2 c_{2} \cos{3 t}, \qquad y(t) = 3 c_{1} \sin{3 t} + c_{1} \cos{3 t} + c_{2} \sin{3 t} - 3 c_{2} \cos{3 t} $$

Check: with $A = \begin{pmatrix} -3 & -3 \\ 6 & 3 \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

### (iii) $\lambda_\pm = -2 \pm i \text{ with } \boldsymbol\eta_\pm = (1 \mp i,\ 3 \pm i),\ \dot x > 0$

$\rho = -2$, $\omega = 1$, $\mathbf u = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{-2t}\left[\left(c_1\cos 1t + c_2\sin 1t\right)\begin{pmatrix} 1 \\ 3 \end{pmatrix} + \left(c_2\cos 1t - c_1\sin 1t\right)\begin{pmatrix} -1 \\ 1 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = c_{1} e^{-2 t} \sin{t} + c_{1} e^{-2 t} \cos{t} + c_{2} e^{-2 t} \sin{t} - c_{2} e^{-2 t} \cos{t}, \qquad y(t) = - c_{1} e^{-2 t} \sin{t} + 3 c_{1} e^{-2 t} \cos{t} + 3 c_{2} e^{-2 t} \sin{t} + c_{2} e^{-2 t} \cos{t} $$

Check: with $A = \begin{pmatrix} - \frac{5}{2} & \frac{1}{2} \\ - \frac{5}{2} & - \frac{3}{2} \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

### (iv) $\lambda_\pm = -1 \pm i \text{ with } \boldsymbol\eta_\pm = (1,\ \pm i),\ \dot x > 0$

$\rho = -1$, $\omega = 1$, $\mathbf u = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{-1t}\left[\left(c_1\cos 1t + c_2\sin 1t\right)\begin{pmatrix} 1 \\ 0 \end{pmatrix} + \left(c_2\cos 1t - c_1\sin 1t\right)\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = c_{1} e^{-t} \cos{t} + c_{2} e^{-t} \sin{t}, \qquad y(t) = - c_{1} e^{-t} \sin{t} + c_{2} e^{-t} \cos{t} $$

Check: with $A = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

### (v) $\lambda_\pm = 2 \pm 2i \text{ with } \boldsymbol\eta_\pm = (\pm 3i,\ 5 \mp 4i),\ \dot x < 0$

$\rho = 2$, $\omega = 2$, $\mathbf u = \begin{pmatrix} 0 \\ 5 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} 3 \\ -4 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{2t}\left[\left(c_1\cos 2t + c_2\sin 2t\right)\begin{pmatrix} 0 \\ 5 \end{pmatrix} + \left(c_2\cos 2t - c_1\sin 2t\right)\begin{pmatrix} 3 \\ -4 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = - 3 c_{1} e^{2 t} \sin{2 t} + 3 c_{2} e^{2 t} \cos{2 t}, \qquad y(t) = 4 c_{1} e^{2 t} \sin{2 t} + 5 c_{1} e^{2 t} \cos{2 t} + 5 c_{2} e^{2 t} \sin{2 t} - 4 c_{2} e^{2 t} \cos{2 t} $$

Check: with $A = \begin{pmatrix} \frac{2}{5} & - \frac{6}{5} \\ \frac{82}{15} & \frac{18}{5} \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

### (vi) $\lambda_\pm = 5 \pm 3i \text{ with } \boldsymbol\eta_\pm = (2 \pm 5i,\ \mp i),\ \dot x < 0$

$\rho = 5$, $\omega = 3$, $\mathbf u = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} 5 \\ -1 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{5t}\left[\left(c_1\cos 3t + c_2\sin 3t\right)\begin{pmatrix} 2 \\ 0 \end{pmatrix} + \left(c_2\cos 3t - c_1\sin 3t\right)\begin{pmatrix} 5 \\ -1 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = - 5 c_{1} e^{5 t} \sin{3 t} + 2 c_{1} e^{5 t} \cos{3 t} + 2 c_{2} e^{5 t} \sin{3 t} + 5 c_{2} e^{5 t} \cos{3 t}, \qquad y(t) = c_{1} e^{5 t} \sin{3 t} - c_{2} e^{5 t} \cos{3 t} $$

Check: with $A = \begin{pmatrix} - \frac{5}{2} & - \frac{87}{2} \\ \frac{3}{2} & \frac{25}{2} \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

### (vii) $\lambda_\pm = \pm 7i \text{ with } \boldsymbol\eta_\pm = (1 \pm i,\ -1 \pm 2i),\ \dot x > 0$

$\rho = 0$, $\omega = 7$, $\mathbf u = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{0t}\left[\left(c_1\cos 7t + c_2\sin 7t\right)\begin{pmatrix} 1 \\ -1 \end{pmatrix} + \left(c_2\cos 7t - c_1\sin 7t\right)\begin{pmatrix} 1 \\ 2 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = - c_{1} \sin{7 t} + c_{1} \cos{7 t} + c_{2} \sin{7 t} + c_{2} \cos{7 t}, \qquad y(t) = - 2 c_{1} \sin{7 t} - c_{1} \cos{7 t} - c_{2} \sin{7 t} + 2 c_{2} \cos{7 t} $$

Check: with $A = \begin{pmatrix} - \frac{7}{3} & \frac{14}{3} \\ - \frac{35}{3} & \frac{7}{3} \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

### (viii) $\lambda_\pm = -13 \pm 17i \text{ with } \boldsymbol\eta_\pm = (\pm 6i - 8,\ 4 \mp 5i),\ \dot x > 0$

$\rho = -13$, $\omega = 17$, $\mathbf u = \begin{pmatrix} -8 \\ 4 \end{pmatrix}$, $\mathbf w = \begin{pmatrix} 6 \\ -5 \end{pmatrix}$. Substituting in the general formula,

$$ \mathbf x(t) = e^{-13t}\left[\left(c_1\cos 17t + c_2\sin 17t\right)\begin{pmatrix} -8 \\ 4 \end{pmatrix} + \left(c_2\cos 17t - c_1\sin 17t\right)\begin{pmatrix} 6 \\ -5 \end{pmatrix}\right] $$

Component by component:

$$ x(t) = - 6 c_{1} e^{-13 t} \sin{17 t} - 8 c_{1} e^{-13 t} \cos{17 t} - 8 c_{2} e^{-13 t} \sin{17 t} + 6 c_{2} e^{-13 t} \cos{17 t}, \qquad y(t) = 5 c_{1} e^{-13 t} \sin{17 t} + 4 c_{1} e^{-13 t} \cos{17 t} + 4 c_{2} e^{-13 t} \sin{17 t} - 5 c_{2} e^{-13 t} \cos{17 t} $$

Check: with $A = \begin{pmatrix} \frac{423}{8} & \frac{425}{4} \\ - \frac{697}{16} & - \frac{631}{8} \end{pmatrix}$ (Exercise 1), $\dot{\mathbf x} - A\mathbf x = \mathbf 0$ identically (verified symbolically).

## Phase 4: Interpretation and checks

- The two constants are real and are the initial coordinates in the $(\mathbf u, \mathbf w)$ basis: $(c_1, c_2)^T = Q^{-1}\mathbf x_0$.
- Centres $(\rho = 0)$: (ii) and (vii) give purely periodic $\mathbf x(t)$ with period $2\pi/3$ and $2\pi/7$; spirals have an envelope $e^{\rho t}$.
- Linear independence: $e^{\rho t}(\cos\omega t\,\mathbf u - \sin\omega t\,\mathbf w)$ and $e^{\rho t}(\sin\omega t\,\mathbf u + \cos\omega t\,\mathbf w)$ have Wronskian $e^{2\rho t}\det[\mathbf u\ \mathbf w] \neq 0$ since $\mathbf u, \mathbf w$ are independent (Exercise 4).
- Dimensional check: the exponent $\rho t$ and the phase $\omega t$ are dimensionless when $\rho$ and $\omega$ are rates in s$^{-1}$ and $t$ in s.
