---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 4"
dificultad: media
tags:
  - problema-resuelto
  - coeficientes-constantes
  - ecuacion-caracteristica
  - pvi-segundo-orden
  - oscilaciones
---

# ✏️ Problem 3.4: Second-Order Homogeneous Linear ODEs with IVPs

## 📄 Enunciado (Problem Statement)

Find the general solution of the following differential equations, and then the unique solution satisfying the specified initial conditions:

1. $\ddot{x} - 3\dot{x} + 2x = 0$ with $x(0) = 2$ and $\dot{x}(0) = 6$
2. $y'' - 4y' + 4y = 0$ with $y(0) = 0$ and $y'(0) = 3$
3. $z'' - 4z' + 13z = 0$ with $z(0) = 7$ and $z'(0) = 42$
4. $\ddot{y} + \dot{y} - 6y = 0$ with $y(0) = -1$ and $y'(0) = 8$
5. $\ddot{y} - 4\dot{y} = 0$ with $y(0) = 13$ and $\dot{y}(0) = 0$
6. $\ddot{\theta} + 4\theta = 0$ with $\theta(0) = 0$ and $\dot{\theta}(0) = 10$
7. $\ddot{y} + 2\dot{y} + 10y = 0$ with $y(0) = 3$ and $\dot{y}(0) = 0$
8. $2\ddot{z} + 7\dot{z} - 4z = 0$ with $z(0) = 0$ and $\dot{z}(0) = 9$
9. $\ddot{y} + 2\dot{y} + y = 0$ with $y(0) = 0$ and $\dot{y}(0) = -1$
10. $\ddot{x} + 6\dot{x} + 10x = 0$ with $x(0) = 3$ and $\dot{x}(0) = 1$
11. $4\ddot{x} - 20\dot{x} + 21x = 0$ with $x(0) = -4$ and $\dot{x}(0) = -12$
12. $\ddot{y} + \dot{y} - 2y = 0$ with $y(0) = 4$ and $\dot{y}(0) = -4$
13. $\ddot{y} - 4y = 0$ with $y(0) = 10$ and $\dot{y}(0) = 0$
14. $y'' + 4y' + 4y = 0$ with $y(0) = 27$ and $y'(0) = -54$
15. $\ddot{y} + \omega^2 y = 0$ with $y(0) = 0$ and $\dot{y}(0) = 1$ ($\omega \neq 0$)

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Form:
Every equation in this problem sheet is a second-order linear homogeneous ordinary differential equation with real, constant coefficients:
$$ a \frac{d^2 u}{dt^2} + b \frac{du}{dt} + c u = 0, \qquad a \neq 0 $$
equipped with Cauchy initial conditions at $t_0 = 0$:
$$ u(0) = u_0, \qquad \dot{u}(0) = v_0 $$

By Robinson Theorem 11.1 (Existence and Uniqueness for Linear ODEs), since the coefficients $a, b, c$ are constants and continuous on all of $\mathbb{R}$, each IVP possesses a **unique classical solution defined globally** on $I = (-\infty, \infty)$.

---

## 🧠 2. Estrategia y Método de Resolución (Phase 2)

### Universal 4-Step Procedure:
1. **Characteristic (Auxiliary) Polynomial:**
   Substitute the exponential ansatz $u(t) = e^{rt}$:
   $$ P(r) = a r^2 + b r + c = 0, \qquad \Delta = b^2 - 4ac $$
2. **Roots Classification and General Solution:**
   - **Case $\Delta > 0$ (Distinct Real Roots $r_1 \neq r_2$):**
     $$ u(t) = c_1 e^{r_1 t} + c_2 e^{r_2 t} $$
   - **Case $\Delta = 0$ (Repeated Real Root $r = -b/(2a)$):**
     $$ u(t) = (c_1 + c_2 t) e^{rt} $$
   - **Case $\Delta < 0$ (Conjugate Complex Roots $r = \rho \pm i\omega$, with $\rho = -b/(2a), \omega = \frac{\sqrt{4ac-b^2}}{2a}$):**
     $$ u(t) = e^{\rho t}\left( c_1 \cos(\omega t) + c_2 \sin(\omega t) \right) $$
3. **Differentiate General Solution:** Compute $\dot{u}(t)$ symbolically.
4. **Impose Initial Conditions:** Solve the $2 \times 2$ algebraic linear system for integration constants $(c_1, c_2)$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Subproblem (i): $\ddot{x} - 3\dot{x} + 2x = 0, \quad x(0) = 2, \; \dot{x}(0) = 6$
* Characteristic equation: $r^2 - 3r + 2 = 0 \implies (r - 1)(r - 2) = 0$.
  Roots: $r_1 = 1, \; r_2 = 2$ (Distinct Real).
* General solution:
  $$ x(t) = c_1 e^t + c_2 e^{2t} $$
* First derivative:
  $$ \dot{x}(t) = c_1 e^t + 2c_2 e^{2t} $$
* Initial conditions:
  $$ x(0) = c_1 + c_2 = 2 $$
  $$ \dot{x}(0) = c_1 + 2c_2 = 6 $$
  Subtracting the first equation from the second: $c_2 = 4$.
  Then $c_1 = 2 - c_2 = 2 - 4 = -2$.
* **IVP Solution:**
  $$ \mathbf{x(t) = -2e^t + 4e^{2t}} $$

---

### Subproblem (ii): $y'' - 4y' + 4y = 0, \quad y(0) = 0, \; y'(0) = 3$
* Characteristic equation: $r^2 - 4r + 4 = 0 \implies (r - 2)^2 = 0$.
  Root: $r = 2$ (Multiplicity 2).
* General solution:
  $$ y(t) = (c_1 + c_2 t) e^{2t} $$
* First derivative:
  $$ y'(t) = c_2 e^{2t} + 2(c_1 + c_2 t)e^{2t} = (2c_1 + c_2 + 2c_2 t)e^{2t} $$
* Initial conditions:
  $$ y(0) = c_1 = 0 $$
  $$ y'(0) = 2(0) + c_2 = 3 \implies c_2 = 3 $$
* **IVP Solution:**
  $$ \mathbf{y(t) = 3t e^{2t}} $$

---

### Subproblem (iii): $z'' - 4z' + 13z = 0, \quad z(0) = 7, \; z'(0) = 42$
* Characteristic equation: $r^2 - 4r + 13 = 0 \implies (r - 2)^2 + 9 = 0$.
  Roots: $r = 2 \pm 3i$ ($\rho = 2, \; \omega = 3$).
* General solution:
  $$ z(t) = e^{2t}\left( c_1 \cos 3t + c_2 \sin 3t \right) $$
* First derivative:
  $$ z'(t) = 2e^{2t}(c_1 \cos 3t + c_2 \sin 3t) + e^{2t}(-3c_1 \sin 3t + 3c_2 \cos 3t) $$
  $$ z'(t) = e^{2t} \left[ (2c_1 + 3c_2)\cos 3t + (2c_2 - 3c_1)\sin 3t \right] $$
* Initial conditions:
  $$ z(0) = c_1 = 7 $$
  $$ z'(0) = 2c_1 + 3c_2 = 42 \implies 2(7) + 3c_2 = 42 \implies 3c_2 = 28 \implies c_2 = \frac{28}{3} $$
* **IVP Solution:**
  $$ \mathbf{z(t) = e^{2t}\left( 7\cos 3t + \frac{28}{3}\sin 3t \right)} $$

---

### Subproblem (iv): $\ddot{y} + \dot{y} - 6y = 0, \quad y(0) = -1, \; y'(0) = 8$
* Characteristic equation: $r^2 + r - 6 = 0 \implies (r + 3)(r - 2) = 0$.
  Roots: $r_1 = 2, \; r_2 = -3$ (Distinct Real).
* General solution:
  $$ y(t) = c_1 e^{2t} + c_2 e^{-3t} $$
* First derivative:
  $$ \dot{y}(t) = 2c_1 e^{2t} - 3c_2 e^{-3t} $$
* Initial conditions:
  $$ y(0) = c_1 + c_2 = -1 \implies c_2 = -1 - c_1 $$
  $$ \dot{y}(0) = 2c_1 - 3c_2 = 8 \implies 2c_1 - 3(-1 - c_1) = 5c_1 + 3 = 8 \implies 5c_1 = 5 \implies c_1 = 1 $$
  $$ c_2 = -1 - 1 = -2 $$
* **IVP Solution:**
  $$ \mathbf{y(t) = e^{2t} - 2e^{-3t}} $$

---

### Subproblem (v): $\ddot{y} - 4\dot{y} = 0, \quad y(0) = 13, \; \dot{y}(0) = 0$
* Characteristic equation: $r^2 - 4r = 0 \implies r(r - 4) = 0$.
  Roots: $r_1 = 0, \; r_2 = 4$ (Distinct Real).
* General solution:
  $$ y(t) = c_1 + c_2 e^{4t} $$
* First derivative:
  $$ \dot{y}(t) = 4c_2 e^{4t} $$
* Initial conditions:
  $$ \dot{y}(0) = 4c_2 = 0 \implies c_2 = 0 $$
  $$ y(0) = c_1 + 0 = 13 \implies c_1 = 13 $$
* **IVP Solution:**
  $$ \mathbf{y(t) = 13} \quad \text{(Equilibrium steady state)} $$

---

### Subproblem (vi): $\ddot{\theta} + 4\theta = 0, \quad \theta(0) = 0, \; \dot{\theta}(0) = 10$
* Characteristic equation: $r^2 + 4 = 0 \implies r = \pm 2i$ ($\rho = 0, \; \omega = 2$).
* General solution:
  $$ \theta(t) = c_1 \cos 2t + c_2 \sin 2t $$
* First derivative:
  $$ \dot{\theta}(t) = -2c_1 \sin 2t + 2c_2 \cos 2t $$
* Initial conditions:
  $$ \theta(0) = c_1 = 0 $$
  $$ \dot{\theta}(0) = 2c_2 = 10 \implies c_2 = 5 $$
* **IVP Solution:**
  $$ \mathbf{\theta(t) = 5\sin 2t} $$

---

### Subproblem (vii): $\ddot{y} + 2\dot{y} + 10y = 0, \quad y(0) = 3, \; \dot{y}(0) = 0$
* Characteristic equation: $r^2 + 2r + 10 = 0 \implies (r + 1)^2 + 9 = 0$.
  Roots: $r = -1 \pm 3i$ ($\rho = -1, \; \omega = 3$).
* General solution:
  $$ y(t) = e^{-t}\left( c_1 \cos 3t + c_2 \sin 3t \right) $$
* First derivative:
  $$ \dot{y}(t) = -e^{-t}(c_1 \cos 3t + c_2 \sin 3t) + e^{-t}(-3c_1 \sin 3t + 3c_2 \cos 3t) $$
  $$ \dot{y}(t) = e^{-t} \left[ (3c_2 - c_1)\cos 3t - (3c_1 + c_2)\sin 3t \right] $$
* Initial conditions:
  $$ y(0) = c_1 = 3 $$
  $$ \dot{y}(0) = 3c_2 - c_1 = 0 \implies 3c_2 - 3 = 0 \implies c_2 = 1 $$
* **IVP Solution:**
  $$ \mathbf{y(t) = e^{-t}\left( 3\cos 3t + \sin 3t \right)} $$

---

### Subproblem (viii): $2\ddot{z} + 7\dot{z} - 4z = 0, \quad z(0) = 0, \; \dot{z}(0) = 9$
* Characteristic equation: $2r^2 + 7r - 4 = 0 \implies (2r - 1)(r + 4) = 0$.
  Roots: $r_1 = \frac{1}{2}, \; r_2 = -4$ (Distinct Real).
* General solution:
  $$ z(t) = c_1 e^{t/2} + c_2 e^{-4t} $$
* First derivative:
  $$ \dot{z}(t) = \frac{1}{2}c_1 e^{t/2} - 4c_2 e^{-4t} $$
* Initial conditions:
  $$ z(0) = c_1 + c_2 = 0 \implies c_2 = -c_1 $$
  $$ \dot{z}(0) = \frac{1}{2}c_1 - 4(-c_1) = \frac{9}{2}c_1 = 9 \implies c_1 = 2 \implies c_2 = -2 $$
* **IVP Solution:**
  $$ \mathbf{z(t) = 2e^{t/2} - 2e^{-4t}} $$

---

### Subproblem (ix): $\ddot{y} + 2\dot{y} + y = 0, \quad y(0) = 0, \; \dot{y}(0) = -1$
* Characteristic equation: $r^2 + 2r + 1 = 0 \implies (r + 1)^2 = 0$.
  Root: $r = -1$ (Multiplicity 2).
* General solution:
  $$ y(t) = (c_1 + c_2 t) e^{-t} $$
* First derivative:
  $$ \dot{y}(t) = c_2 e^{-t} - (c_1 + c_2 t)e^{-t} = (c_2 - c_1 - c_2 t)e^{-t} $$
* Initial conditions:
  $$ y(0) = c_1 = 0 $$
  $$ \dot{y}(0) = c_2 - c_1 = c_2 = -1 $$
* **IVP Solution:**
  $$ \mathbf{y(t) = -t e^{-t}} $$

---

### Subproblem (x): $\ddot{x} + 6\dot{x} + 10x = 0, \quad x(0) = 3, \; \dot{x}(0) = 1$
* Characteristic equation: $r^2 + 6r + 10 = 0 \implies (r + 3)^2 + 1 = 0$.
  Roots: $r = -3 \pm i$ ($\rho = -3, \; \omega = 1$).
* General solution:
  $$ x(t) = e^{-3t}\left( c_1 \cos t + c_2 \sin t \right) $$
* First derivative:
  $$ \dot{x}(t) = -3e^{-3t}(c_1 \cos t + c_2 \sin t) + e^{-3t}(-c_1 \sin t + c_2 \cos t) $$
  $$ \dot{x}(t) = e^{-3t}\left[ (c_2 - 3c_1)\cos t - (c_1 + 3c_2)\sin t \right] $$
* Initial conditions:
  $$ x(0) = c_1 = 3 $$
  $$ \dot{x}(0) = c_2 - 3c_1 = 1 \implies c_2 - 3(3) = 1 \implies c_2 = 10 $$
* **IVP Solution:**
  $$ \mathbf{x(t) = e^{-3t}\left( 3\cos t + 10\sin t \right)} $$

---

### Subproblem (xi): $4\ddot{x} - 20\dot{x} + 21x = 0, \quad x(0) = -4, \; \dot{x}(0) = -12$
* Characteristic equation: $4r^2 - 20r + 21 = 0$.
  Discriminant: $\Delta = (-20)^2 - 4(4)(21) = 400 - 336 = 64 = 8^2$.
  Roots: $r = \frac{20 \pm 8}{8} \implies r_1 = \frac{7}{2}, \; r_2 = \frac{3}{2}$.
* General solution:
  $$ x(t) = c_1 e^{3t/2} + c_2 e^{7t/2} $$
* First derivative:
  $$ \dot{x}(t) = \frac{3}{2}c_1 e^{3t/2} + \frac{7}{2}c_2 e^{7t/2} $$
* Initial conditions:
  $$ x(0) = c_1 + c_2 = -4 \implies c_2 = -4 - c_1 $$
  $$ \dot{x}(0) = \frac{3}{2}c_1 + \frac{7}{2}(-4 - c_1) = -2c_1 - 14 = -12 \implies -2c_1 = 2 \implies c_1 = -1 $$
  $$ c_2 = -4 - (-1) = -3 $$
* **IVP Solution:**
  $$ \mathbf{x(t) = -e^{3t/2} - 3e^{7t/2}} $$

---

### Subproblem (xii): $\ddot{y} + \dot{y} - 2y = 0, \quad y(0) = 4, \; \dot{y}(0) = -4$
* Characteristic equation: $r^2 + r - 2 = 0 \implies (r + 2)(r - 1) = 0$.
  Roots: $r_1 = 1, \; r_2 = -2$.
* General solution:
  $$ y(t) = c_1 e^t + c_2 e^{-2t} $$
* First derivative:
  $$ \dot{y}(t) = c_1 e^t - 2c_2 e^{-2t} $$
* Initial conditions:
  $$ y(0) = c_1 + c_2 = 4 $$
  $$ \dot{y}(0) = c_1 - 2c_2 = -4 $$
  Subtracting second from first: $3c_2 = 8 \implies c_2 = \frac{8}{3}$.
  Then $c_1 = 4 - \frac{8}{3} = \frac{4}{3}$.
* **IVP Solution:**
  $$ \mathbf{y(t) = \frac{4}{3}e^t + \frac{8}{3}e^{-2t}} $$

---

### Subproblem (xiii): $\ddot{y} - 4y = 0, \quad y(0) = 10, \; \dot{y}(0) = 0$
* Characteristic equation: $r^2 - 4 = 0 \implies r = \pm 2$.
* General solution:
  $$ y(t) = c_1 e^{2t} + c_2 e^{-2t} = A \cosh 2t + B \sinh 2t $$
* First derivative:
  $$ \dot{y}(t) = 2c_1 e^{2t} - 2c_2 e^{-2t} $$
* Initial conditions:
  $$ y(0) = c_1 + c_2 = 10 $$
  $$ \dot{y}(0) = 2(c_1 - c_2) = 0 \implies c_1 = c_2 $$
  Thus $2c_1 = 10 \implies c_1 = 5, \; c_2 = 5$.
* **IVP Solution:**
  $$ \mathbf{y(t) = 5e^{2t} + 5e^{-2t} = 10\cosh(2t)} $$

---

### Subproblem (xiv): $y'' + 4y' + 4y = 0, \quad y(0) = 27, \; y'(0) = -54$
* Characteristic equation: $r^2 + 4r + 4 = 0 \implies (r + 2)^2 = 0$.
  Root: $r = -2$ (Multiplicity 2).
* General solution:
  $$ y(t) = (c_1 + c_2 t) e^{-2t} $$
* First derivative:
  $$ y'(t) = c_2 e^{-2t} - 2(c_1 + c_2 t)e^{-2t} = (c_2 - 2c_1 - 2c_2 t)e^{-2t} $$
* Initial conditions:
  $$ y(0) = c_1 = 27 $$
  $$ y'(0) = c_2 - 2c_1 = -54 \implies c_2 - 2(27) = -54 \implies c_2 - 54 = -54 \implies c_2 = 0 $$
* **IVP Solution:**
  $$ \mathbf{y(t) = 27e^{-2t}} $$

---

### Subproblem (xv): $\ddot{y} + \omega^2 y = 0, \quad y(0) = 0, \; \dot{y}(0) = 1 \quad (\omega \neq 0)$
* Characteristic equation: $r^2 + \omega^2 = 0 \implies r = \pm i\omega$.
* General solution:
  $$ y(t) = c_1 \cos(\omega t) + c_2 \sin(\omega t) $$
* First derivative:
  $$ \dot{y}(t) = -c_1 \omega \sin(\omega t) + c_2 \omega \cos(\omega t) $$
* Initial conditions:
  $$ y(0) = c_1 = 0 $$
  $$ \dot{y}(0) = c_2 \omega = 1 \implies c_2 = \frac{1}{\omega} $$
* **IVP Solution:**
  $$ \mathbf{y(t) = \frac{1}{\omega}\sin(\omega t)} $$

---

## 🎯 4. Resultado Final y Análisis Comparativo (Phase 4)

### Master IVP Solution Summary Table:

| Subproblem | ODE & Initial Conditions | Characteristic Roots | Root Nature | Unique Solution $u(t)$ |
| :---: | :--- | :---: | :---: | :--- |
| **(i)** | $\ddot{x} - 3\dot{x} + 2x = 0$, $x(0)=2, \dot{x}(0)=6$ | $r = 1, 2$ | Distinct Real | $\mathbf{-2e^t + 4e^{2t}}$ |
| **(ii)** | $y'' - 4y' + 4y = 0$, $y(0)=0, y'(0)=3$ | $r = 2$ (mult. 2) | Repeated Real | $\mathbf{3t e^{2t}}$ |
| **(iii)** | $z'' - 4z' + 13z = 0$, $z(0)=7, z'(0)=42$ | $r = 2 \pm 3i$ | Complex Conjugate | $\mathbf{e^{2t}(7\cos 3t + \frac{28}{3}\sin 3t)}$ |
| **(iv)** | $\ddot{y} + \dot{y} - 6y = 0$, $y(0)=-1, y'(0)=8$ | $r = 2, -3$ | Distinct Real | $\mathbf{e^{2t} - 2e^{-3t}}$ |
| **(v)** | $\ddot{y} - 4\dot{y} = 0$, $y(0)=13, \dot{y}(0)=0$ | $r = 0, 4$ | Distinct Real | $\mathbf{13}$ |
| **(vi)** | $\ddot{\theta} + 4\theta = 0$, $\theta(0)=0, \dot{\theta}(0)=10$ | $r = \pm 2i$ | Pure Imaginary | $\mathbf{5\sin 2t}$ |
| **(vii)** | $\ddot{y} + 2\dot{y} + 10y = 0$, $y(0)=3, \dot{y}(0)=0$ | $r = -1 \pm 3i$ | Damped Complex | $\mathbf{e^{-t}(3\cos 3t + \sin 3t)}$ |
| **(viii)** | $2\ddot{z} + 7\dot{z} - 4z = 0$, $z(0)=0, \dot{z}(0)=9$ | $r = \frac{1}{2}, -4$ | Distinct Real | $\mathbf{2e^{t/2} - 2e^{-4t}}$ |
| **(ix)** | $\ddot{y} + 2\dot{y} + y = 0$, $y(0)=0, \dot{y}(0)=-1$ | $r = -1$ (mult. 2) | Repeated Real | $\mathbf{-t e^{-t}}$ |
| **(x)** | $\ddot{x} + 6\dot{x} + 10x = 0$, $x(0)=3, \dot{x}(0)=1$ | $r = -3 \pm i$ | Damped Complex | $\mathbf{e^{-3t}(3\cos t + 10\sin t)}$ |
| **(xi)** | $4\ddot{x} - 20\dot{x} + 21x = 0$, $x(0)=-4, \dot{x}(0)=-12$ | $r = \frac{3}{2}, \frac{7}{2}$ | Distinct Real | $\mathbf{-e^{3t/2} - 3e^{7t/2}}$ |
| **(xii)** | $\ddot{y} + \dot{y} - 2y = 0$, $y(0)=4, \dot{y}(0)=-4$ | $r = 1, -2$ | Distinct Real | $\mathbf{\frac{4}{3}e^t + \frac{8}{3}e^{-2t}}$ |
| **(xiii)** | $\ddot{y} - 4y = 0$, $y(0)=10, \dot{y}(0)=0$ | $r = \pm 2$ | Distinct Real | $\mathbf{10\cosh(2t)}$ |
| **(xiv)** | $y'' + 4y' + 4y = 0$, $y(0)=27, y'(0)=-54$ | $r = -2$ (mult. 2) | Repeated Real | $\mathbf{27e^{-2t}}$ |
| **(xv)** | $\ddot{y} + \omega^2 y = 0$, $y(0)=0, \dot{y}(0)=1$ | $r = \pm i\omega$ | Pure Imaginary | $\mathbf{\frac{1}{\omega}\sin(\omega t)}$ |

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Ecuaciones Homogeneas con Coeficientes Constantes y Ecuacion Caracteristica|Ecuaciones Homogéneas con Coeficientes Constantes]]`
* `[[04 - Advanced Maths/Concepto - Teorema de Existencia y Unicidad para EDOs de Segundo Orden|Teorema de Existencia y Unicidad]]`
* `[[04 - Advanced Maths/Problema - Ch3-P5 Saddle Invariant Manifold and Asymptotic Decay|Problem 3.5: Saddle Invariant Manifold]]`
* `[[04 - Advanced Maths/Problema - Ch3-P8 Damped Harmonic Oscillator Regimes|Problem 3.8: Damped Oscillator Regimes]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
