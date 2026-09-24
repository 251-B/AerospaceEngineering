---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 6"
dificultad: baja
tags:
  - problema-resuelto
  - forma-amplitud-fase
  - oscilaciones-armonicas
  - trigonometria
  - transformacion-coordenadas
---

# ✏️ Problem 3.6: Amplitude-Phase Transformation for Harmonic Oscillations

## 📄 Enunciado (Problem Statement)

Given an oscillating function of the form:
$$ x(t) = A \cos(\omega t) + B \sin(\omega t) $$
show that it can be rewritten as a "single oscillation":
$$ x(t) = M \cos(\omega t - \phi) $$
with amplitude $M = (A^2 + B^2)^{1/2}$ and phase $\phi = \arctan(B/A)$.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Parameters:
- Cartesian harmonic decomposition: $x(t) = A \cos(\omega t) + B \sin(\omega t)$, where $A, B \in \mathbb{R}$ are constant amplitudes, and $\omega > 0$ is the angular frequency (rad/s).
- Polar amplitude-phase form: $x(t) = M \cos(\omega t - \phi)$, where $M \ge 0$ represents peak amplitude and $\phi \in (-\pi, \pi]$ represents phase lag.
- We assume $(A, B) \neq (0, 0)$ to avoid trivial degeneracies ($M = 0$).

---

## 🧠 2. Estrategia y Planteamiento Matemático (Phase 2)

### Plan:
1. **Trigonometric Angle Difference Expansion:** Expand $\cos(\omega t - \phi)$ using the compound angle identity:
   $$ \cos(\alpha - \beta) = \cos\alpha \cos\beta + \sin\alpha \sin\beta $$
2. **Equate Linear Coefficients:** Equate coefficients of $\cos(\omega t)$ and $\sin(\omega t)$ with the given Cartesian expression.
3. **Solve Polar System:**
   - Sum of squares to determine the magnitude $M$.
   - Ratio of components to determine the phase angle $\phi$.
4. **Geometric Interpretation:** Relate $(A, B)$ to Cartesian coordinates and $(M, \phi)$ to polar coordinates on the phasor plane.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Trigonometric Identity Expansion
Consider the proposed single-oscillation representation:
$$ x(t) = M \cos(\omega t - \phi) $$
Using the subtraction formula for cosine with $\alpha = \omega t$ and $\beta = \phi$:
$$ \cos(\omega t - \phi) = \cos(\omega t)\cos(\phi) + \sin(\omega t)\sin(\phi) $$
Multiplying by the amplitude $M$:
$$ x(t) = (M \cos\phi) \cos(\omega t) + (M \sin\phi) \sin(\omega t) \tag{1} $$

---

### Step 2: Harmonic Balance / Coefficient Identification
Comparing equation (1) with the given form $x(t) = A \cos(\omega t) + B \sin(\omega t)$:
$$ (M \cos\phi) \cos(\omega t) + (M \sin\phi) \sin(\omega t) = A \cos(\omega t) + B \sin(\omega t) $$
Since the functions $\cos(\omega t)$ and $\sin(\omega t)$ are linearly independent on any interval for $\omega \neq 0$ (as proven in Problem 3.1), their coefficients must be identical:
$$ \begin{cases} A = M \cos\phi & \tag{2a} \\ B = M \sin\phi & \tag{2b} \end{cases} $$

---

### Step 3: Derivation of the Amplitude $M$
Square both equations (2a) and (2b):
$$ A^2 = M^2 \cos^2\phi $$
$$ B^2 = M^2 \sin^2\phi $$
Sum both equations:
$$ A^2 + B^2 = M^2 \cos^2\phi + M^2 \sin^2\phi = M^2 (\cos^2\phi + \sin^2\phi) $$
By the Pythagorean trigonometric identity $\cos^2\phi + \sin^2\phi = 1$:
$$ A^2 + B^2 = M^2 $$
Taking the positive square root (since amplitude is physical and non-negative):
$$ \mathbf{M = \sqrt{A^2 + B^2} = (A^2 + B^2)^{1/2}} \tag{3} $$

---

### Step 4: Derivation of the Phase Angle $\phi$
Divide equation (2b) by equation (2a) (assuming $A \neq 0$):
$$ \frac{B}{A} = \frac{M \sin\phi}{M \cos\phi} = \tan\phi $$
Taking the inverse tangent:
$$ \mathbf{\phi = \arctan\left(\frac{B}{A}\right)} \tag{4} $$

> [!NOTE] Four-Quadrant Quadrant Disambiguation (Atan2)
> In computational applications and engineering practice, when $A < 0$, the principal branch of $\arctan(B/A)$ requires adding or subtracting $\pi$ to match the correct signs of $(A, B)$:
> $$ \phi = \operatorname{atan2}(B, A) $$
> If $A = 0$, $\phi = \frac{\pi}{2}$ when $B > 0$, and $\phi = -\frac{\pi}{2}$ when $B < 0$.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Formulas:
$$ \boxed{x(t) = M \cos(\omega t - \phi)} $$
where:
$$ \boxed{M = \sqrt{A^2 + B^2}, \qquad \phi = \arctan\left(\frac{B}{A}\right)} $$

### Engineering & Aerospace Vibration Analysis:
- **Phasor Representation:** In structural dynamics (e.g. wing flutter, satellite attitude oscillations), $(A, B)$ represents the projection of a rotating vector (phasor) of length $M$ rotating counterclockwise at angular velocity $\omega$.
- **Peak Envelope:** The physical maximum displacement is immediately read as $x_{\max} = M$. In contrast, reading $x_{\max}$ directly from $A\cos\omega t + B\sin\omega t$ requires finding derivatives $\dot{x}(t^*) = 0$.
- **Phase Delay:** The phase angle $\phi$ directly quantifies the time delay $\Delta t = \frac{\phi}{\omega}$ of the maximum peak relative to $t = 0$.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Ecuaciones Homogeneas con Coeficientes Constantes y Ecuacion Caracteristica|Ecuaciones Homogéneas]]`
* `[[04 - Advanced Maths/Problema - Ch3-P1 Linear Independence via Wronskian|Problem 3.1: Wronskian Independence]]`
* `[[04 - Advanced Maths/Problema - Ch3-P7 Simple Pendulum Energy and Small Oscillations|Problem 3.7: Simple Pendulum Oscillations]]`
* `[[04 - Advanced Maths/Problema - Ch3-P8 Damped Harmonic Oscillator Regimes|Problem 3.8: Damped Oscillator Regimes]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
