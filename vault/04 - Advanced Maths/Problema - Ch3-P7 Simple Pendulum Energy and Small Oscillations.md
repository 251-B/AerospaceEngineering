---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 7"
dificultad: media
tags:
  - problema-resuelto
  - pendulo-simple
  - conservacion-energia
  - pequenas-oscilaciones
  - mecanica-lagrangiana
---

# ✏️ Problem 3.7: Simple Pendulum Energy and Small Oscillations

## 📄 Enunciado (Problem Statement)

Consider a so-called simple pendulum whose shaft has length $L$ and negligible mass, and a suspended mass $m$ at its end. If the pivot is at the origin of coordinates, show that:

**(i)** The gravitational potential energy is $V(\theta) = mgL(1 - \cos\theta)$, where $g$ is the acceleration of gravity and $\theta$ is the angle with the downward vertical.  
**(ii)** The total (kinetic plus potential) energy is $E = \frac{1}{2}mL^2 \dot{\theta}^2 + mgL(1 - \cos\theta)$.  
**(iii)** The equation of motion reads $\frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta$, which is obtained by requesting that the total energy does not change with time.  
**(iv)** By considering small oscillations around the vertical, the equation becomes $\frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta$. Show that the general solution of this equation reads $\theta(t) = M\cos(\omega t - \phi)$ and relate the oscillation frequency $\omega$ with the system parameters. Does this frequency depend on the mass $m$? Does it depend on the amplitude of oscillations?

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Physical Parameters & Geometry:
- Shaft length: $L$ (rigid, massless rod).
- Concentrated bob mass: $m$ located at $(x, y)$.
- Angle with the downward vertical: $\theta(t)$.
  * Equilibrium position: $\theta = 0$ (straight down).
  * Cartesian coordinates (pivot at origin $(0, 0)$, $y$ pointing upwards):
    $$ x(t) = L \sin\theta(t), \qquad y(t) = -L \cos\theta(t) $$
- Gravity: constant gravitational acceleration $g > 0$ acting in the negative $y$-direction.
- Conservation hypothesis: frictionless pivot, no air resistance $\implies$ mechanical energy is conserved ($\frac{dE}{dt} = 0$).

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

### Plan:
1. **Potential Energy $V(\theta)$:** Compute height relative to the lowest point $y_0 = -L$, setting $V(0) = 0$.
2. **Kinetic Energy $T$:** Compute tangential velocity along the circular arc $v = L\dot{\theta}$ and kinetic energy $T = \frac{1}{2}m v^2$. Form total energy $E = T + V$.
3. **Equation of Motion via First Integral of Motion:** Differentiate $E(t)$ with respect to time $t$ via the chain rule. Since energy is conserved ($\frac{dE}{dt} = 0$), divide by $mL^2\dot{\theta} \neq 0$ to obtain the nonlinear pendulum ODE.
4. **Linearization & Harmonic Solution:** For $|\theta| \ll 1$, apply the first-order Taylor expansion $\sin\theta \approx \theta$. Solve the resulting linear harmonic oscillator using the characteristic equation, convert to amplitude-phase form (using Problem 3.6), and inspect dependencies on mass $m$ and amplitude $M$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): Gravitational Potential Energy $V(\theta)$
With the pivot at the origin $(0, 0)$ and the upward vertical along the positive $y$-axis:
$$ y(\theta) = -L \cos\theta $$
At the lowest equilibrium position ($\theta = 0$):
$$ y_{\text{ref}} = y(0) = -L $$
Choosing the equilibrium configuration as the zero potential energy reference datum ($V(0) = 0$):
$$ V(\theta) = mg \left( y(\theta) - y_{\text{ref}} \right) = mg \left( -L\cos\theta - (-L) \right) $$
Factoring out $mgL$:
$$ \mathbf{V(\theta) = mgL(1 - \cos\theta)} \tag{1} $$

---

### Part (ii): Total Mechanical Energy $E$
The position vector of the point mass is:
$$ \mathbf{r}(t) = L\sin\theta(t)\,\mathbf{i} - L\cos\theta(t)\,\mathbf{j} $$
Differentiating with respect to time:
$$ \mathbf{v}(t) = \dot{\mathbf{r}}(t) = L\dot{\theta}\cos\theta\,\mathbf{i} + L\dot{\theta}\sin\theta\,\mathbf{j} $$
The square of the speed is:
$$ v^2 = \|\mathbf{v}\|^2 = (L\dot{\theta}\cos\theta)^2 + (L\dot{\theta}\sin\theta)^2 = L^2\dot{\theta}^2(\cos^2\theta + \sin^2\theta) = L^2\dot{\theta}^2 $$
The kinetic energy $T$ is therefore:
$$ T = \frac{1}{2}m v^2 = \frac{1}{2} m L^2 \dot{\theta}^2 \tag{2} $$
The total mechanical energy $E$ is the sum of kinetic and potential energies:
$$ \mathbf{E = T + V(\theta) = \frac{1}{2} m L^2 \dot{\theta}^2 + mgL(1 - \cos\theta)} \tag{3} $$

---

### Part (iii): Equation of Motion via Time-Invariance of Energy
In the absence of non-conservative forces, mechanical energy is conserved:
$$ \frac{dE}{dt} = 0 $$
Differentiating equation (3) with respect to $t$ using the chain rule:
$$ \frac{d}{dt}\left[ \frac{1}{2} m L^2 (\dot{\theta})^2 \right] = \frac{1}{2} m L^2 \cdot \left( 2\dot{\theta}\ddot{\theta} \right) = m L^2 \dot{\theta} \ddot{\theta} $$
$$ \frac{d}{dt}\left[ mgL(1 - \cos\theta) \right] = mgL \cdot \left( 0 - (-\sin\theta \cdot \dot{\theta}) \right) = mgL \dot{\theta} \sin\theta $$
Setting the sum to zero:
$$ \frac{dE}{dt} = mL^2 \dot{\theta}\ddot{\theta} + mgL \dot{\theta}\sin\theta = 0 $$
Factoring out $mL^2 \dot{\theta}$:
$$ mL^2 \dot{\theta} \left( \ddot{\theta} + \frac{g}{L}\sin\theta \right) = 0 $$
For non-trivial motion ($\dot{\theta} \not\equiv 0$), the term in parentheses must vanish identically:
$$ \mathbf{\frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta} \tag{4} $$

---

### Part (iv): Small Oscillations Linearization & Frequency Dependencies
For small angular displacements $|\theta| \ll 1$ (radians), the Taylor series of the sine function gives:
$$ \sin\theta = \theta - \frac{\theta^3}{3!} + \mathcal{O}(\theta^5) \approx \theta $$
Substituting into equation (4):
$$ \frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta \iff \ddot{\theta} + \frac{g}{L}\theta = 0 \tag{5} $$

Let $\omega^2 = \frac{g}{L} \implies \omega = \sqrt{\frac{g}{L}}$.
The characteristic equation is:
$$ r^2 + \omega^2 = 0 \implies r = \pm i\omega $$
The general Cartesian solution is:
$$ \theta(t) = c_1 \cos(\omega t) + c_2 \sin(\omega t) $$
Using the amplitude-phase transformation established in Problem 3.6:
$$ \mathbf{\theta(t) = M \cos(\omega t - \phi)} \tag{6} $$
with $M = \sqrt{c_1^2 + c_2^2}$ and $\phi = \arctan(c_2 / c_1)$.

#### Relation with System Parameters:
$$ \mathbf{\omega = \sqrt{\frac{g}{L}}} \quad \left[\text{rad/s}\right], \qquad T_0 = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{L}{g}} \quad \left[\text{s}\right] $$

#### Answering the Conceptual Questions:
1. **Dependence on mass $m$:**  
   **NO.** The mass $m$ cancels identically from both terms in Newton's 2nd law / energy balance. The frequency $\omega$ is strictly independent of the suspended mass $m$.
2. **Dependence on oscillation amplitude $M$:**  
   - In the **linear small-amplitude approximation** ($\theta \ll 1$), **NO**. The frequency $\omega = \sqrt{g/L}$ is completely independent of the amplitude $M$ (Galileo's property of **isochronism**).  
   - In the **exact nonlinear system**, the true period $T$ **DOES depend on amplitude** and elongates with larger angles according to the complete elliptic integral of the first kind:
     $$ T(M) = 4\sqrt{\frac{L}{g}} K\left(\sin^2\frac{M}{2}\right) \approx T_0 \left( 1 + \frac{1}{16}M^2 + \frac{11}{3072}M^4 + \dots \right) $$

---

## 🎯 4. Resultado Final y Conclusiones Físicas (Phase 4)

### Master Equation Summary:

| Quantity | Mathematical Expression | Physical Units |
| :--- | :--- | :---: |
| **Potential Energy** | $V(\theta) = mgL(1 - \cos\theta)$ | $\text{J}$ |
| **Total Energy** | $E = \frac{1}{2}mL^2\dot{\theta}^2 + mgL(1 - \cos\theta)$ | $\text{J}$ |
| **Nonlinear ODE** | $\ddot{\theta} + \frac{g}{L}\sin\theta = 0$ | $\text{rad/s}^2$ |
| **Linear ODE** | $\ddot{\theta} + \omega^2\theta = 0$ | $\text{rad/s}^2$ |
| **Natural Frequency** | $\omega = \sqrt{\frac{g}{L}}$ | $\text{rad/s}$ |
| **General Solution** | $\theta(t) = M\cos\left(\sqrt{\frac{g}{L}}\,t - \phi\right)$ | $\text{rad}$ |

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Problema - Ch1-P8 Simple Pendulum Equation of Motion|Problem 1.8: Pendulum Modeling]]`
* `[[04 - Advanced Maths/Problema - Ch3-P6 Amplitude-Phase Transformation for Oscillations|Problem 3.6: Amplitude-Phase Transformation]]`
* `[[04 - Advanced Maths/Problema - Ch3-P8 Damped Harmonic Oscillator Regimes|Problem 3.8: Damped Harmonic Oscillator]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
