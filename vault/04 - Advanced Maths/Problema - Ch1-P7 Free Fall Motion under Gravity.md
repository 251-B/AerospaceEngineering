---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.7"
dificultad: baja
tags:
  - problema-resuelto
  - caida-libre
  - newton-2a-ley
  - integracion-sucesiva
  - cinematica
---

# ✏️ Problem 1.7: Free Fall Motion under Gravity

## 📄 Enunciado (Problem Statement)

Consider an object in free fall from an initial point $y(0) = y_0$ and with initial velocity $0$, under the action of gravity and neglecting air friction. Write a differential equation for the position of the object $y(t)$ and solve it.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Variables and Parameters:
* **Independent variable:** Time $t \ge 0$ $[s]$.
* **Dependent variable:** Vertical position $y(t)$ $[m]$.
* **Parameters:**
  * Acceleration of gravity: $g \approx 9.81\text{ m/s}^2$ (constant, uniform field).
  * Initial position: $y(0) = y_0$ $[m]$.
  * Initial velocity: $y'(0) = v(0) = 0\text{ m/s}$ (released from rest).

### Hypotheses:
* [x] **Point mass approximation:** The object has mass $m$, and rotational degrees of freedom are ignored.
* [x] **Upward vertical coordinate system:** The coordinate axis $y$ is oriented vertically upwards, away from the Earth's surface. Gravity acts in the $-\hat{j}$ direction.
* [x] **Neglect aerodynamic resistance:** Viscous drag and aerodynamic pressure forces are zero ($\vec{F}_{\text{drag}} = \vec{0}$).
* [x] **Constant gravitational field:** Altitudes are small compared to the radius of the Earth ($y_0 \ll R_\oplus$), so $g$ is constant.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Apply **Newton's Second Law of Motion**:
   $$ \sum \vec{F} = m \vec{a} $$
2. In the 1D vertical direction:
   $$ F_{\text{gravity}} = -m g $$
   $$ m \frac{d^2 y}{dt^2} = -m g \implies \frac{d^2 y}{dt^2} = -g $$
3. This is a second-order, linear, inhomogeneous ODE with constant forcing.
4. Perform two successive integrations with respect to time $t$, enforcing the initial conditions at each step.
5. Verify energy conservation and compute the time and speed of ground impact.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Formulation of the Initial Value Problem
From Newton's Second Law:
$$ m \ddot{y}(t) = -m g $$
Dividing both sides by the mass $m > 0$:
$$ \mathbf{\frac{d^2 y}{dt^2} = -g} \tag{1} $$

The associated Initial Value Problem (IVP) is:
$$ \begin{cases} \dfrac{d^2 y}{dt^2} = -g \\ y(0) = y_0 \\ y'(0) = 0 \end{cases} \tag{2} $$

---

### Step 2: First Integration (Determining Velocity $v(t)$)
Express the second derivative as the derivative of velocity:
$$ \frac{d}{dt}\left( \frac{dy}{dt} \right) = -g $$

Integrate both sides with respect to time from $s = 0$ to $s = t$:
$$ \int_0^t \frac{d}{ds}\left( \frac{dy}{ds} \right) \, ds = \int_0^t -g \, ds $$
By the Fundamental Theorem of Calculus:
$$ \left[ \frac{dy}{ds} \right]_0^t = [-g s]_0^t $$
$$ \frac{dy}{dt}(t) - \frac{dy}{dt}(0) = -g t $$

Substitute the initial velocity condition $y'(0) = 0$:
$$ \frac{dy}{dt}(t) - 0 = -g t $$
$$ \mathbf{v(t) = y'(t) = -g t} \tag{3} $$

---

### Step 3: Second Integration (Determining Position $y(t)$)
Integrate the velocity equation $(3)$ with respect to time from $s = 0$ to $s = t$:
$$ \int_0^t \frac{dy}{ds} \, ds = \int_0^t -g s \, ds $$
$$ [y(s)]_0^t = -g \left[ \frac{s^2}{2} \right]_0^t $$
$$ y(t) - y(0) = -g \left( \frac{t^2}{2} - 0 \right) $$
$$ y(t) - y_0 = -\frac{1}{2} g t^2 $$

Isolate the trajectory $y(t)$:
$$ \mathbf{y(t) = y_0 - \frac{1}{2} g t^2} \tag{4} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Answers:
* **Differential Equation:**
  $$ \frac{d^2 y}{dt^2} = -g $$
* **Analytical Solution:**
  $$ \mathbf{y(t) = y_0 - \frac{1}{2} g t^2} $$
* **Velocity Profile:**
  $$ v(t) = -gt $$

### Physical & Kinematic Analysis:
1. **Dimensional Verification:**
   * $[y_0] = [L] = m$.
   * $[g t^2] = [L/T^2] \cdot [T^2] = [L] = m$. Units are strictly consistent.
2. **Impact Time on Ground ($y = 0$):**
   $$ 0 = y_0 - \frac{1}{2} g t_{\text{impact}}^2 \implies t_{\text{impact}} = \sqrt{\frac{2 y_0}{g}} $$
3. **Impact Velocity & Conservation of Mechanical Energy:**
   Evaluating velocity at impact:
   $$ v_{\text{impact}} = -g \sqrt{\frac{2 y_0}{g}} = -\sqrt{2 g y_0} $$
   Checking mechanical energy conservation between $t = 0$ and impact:
   $$ E_{\text{initial}} = E_p + E_k = m g y_0 + 0 = m g y_0 $$
   $$ E_{\text{final}} = 0 + \frac{1}{2} m v_{\text{impact}}^2 = \frac{1}{2} m \left(-\sqrt{2 g y_0}\right)^2 = m g y_0 $$
   Energy is conserved identically: $E_{\text{initial}} = E_{\text{final}}$.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - First-Order Physical Models|First-Order Physical Models]]`
* `[[04 - Advanced Maths/Problema - Ch1-P8 Simple Pendulum Equation of Motion|Problem 1.8: Simple Pendulum Equation of Motion]]`
