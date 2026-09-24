---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 9"
dificultad: media
tags:
  - problema-resuelto
  - cadena-deslizante
  - newton-segunda-ley
  - funciones-hiperbolicas
  - mecanica-clasica
---

# ✏️ Problem 3.9: Falling Chain from Table and Hyperbolic Motion

## 📄 Enunciado (Problem Statement)

A chain of length $\ell = 5\text{ m}$ and mass $m$, with uniform mass density, is sitting on a table. If the chain is initially at rest and $1\text{ m}$ of the chain hangs from the edge of the table, apply Newton’s second law to calculate the time $t_*$ when the whole chain falls off the table, neglecting any friction.

*Hint:* Formulate a second order ODE for the variable $x(t)$, which is the length of the portion of chain that is overhanging, as a function of time.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Physical Parameters:
- Total chain length: $\ell = 5\text{ m}$
- Total chain mass: $m$ [$\text{kg}$]
- Linear mass density (uniform): $\lambda = \frac{m}{\ell}$ [$\text{kg/m}$]
- Gravitational acceleration: $g = 9.8\text{ m/s}^2$ (standard terrestrial value)
- State variable: $x(t) \in [1, 5]$ [$\text{m}$], the instantaneous length of the overhanging portion.
- Initial conditions (chain initially released from rest with $1\text{ m}$ overhanging):
  $$ x(0) = x_0 = 1\text{ m}, \qquad \dot{x}(0) = 0\text{ m/s} $$
- Hypotheses:
  * Table surface is perfectly horizontal and frictionless ($\mu_f = 0$).
  * Chain is perfectly flexible and inextensible.
  * Motion of all links is purely 1D along the chain contour: the entire mass $m$ accelerates at the same rate $\ddot{x}(t)$ until the instant of complete detachment $x(t_*) = \ell$.

---

## 🧠 2. Estrategia y Planteamiento Físico-Mecánico (Phase 2)

### Plan:
1. **Newton's Second Law for the System:**
   Analyze the net driving force along the path of motion.
   - The horizontal segment on the frictionless table has normal reaction $N = m_{\text{table}} g$ balancing gravity vertically, contributing zero net horizontal force.
   - The vertical hanging segment of length $x(t)$ experiences downward gravity:
     $$ F_{\text{ext}}(t) = m_{\text{hang}}(t) g = (\lambda x) g = \frac{m}{\ell} g x(t) $$
   - The total mass being accelerated is the entire chain $m$.
   - Newton's 2nd law states: $m \ddot{x}(t) = F_{\text{ext}}(t)$.
2. **Solve the Homogeneous 2nd-Order ODE:**
   $$ \ddot{x} - \frac{g}{\ell} x = 0 $$
   Characteristic equation $r^2 - \frac{g}{\ell} = 0 \implies r = \pm \alpha$, where $\alpha = \sqrt{g/\ell}$.
3. **Formulate Solution using Hyperbolic Functions:**
   $$ x(t) = c_1 \cosh(\alpha t) + c_2 \sinh(\alpha t) $$
4. **Impose Initial Conditions:** Determine $c_1$ and $c_2$.
5. **Compute Detachment Time $t_*$:**
   Set $x(t_*) = \ell = 5\text{ m}$, solve $\cosh(\alpha t_*) = \frac{\ell}{x_0}$, and evaluate numerically.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Derivation of the Equation of Motion
The linear mass density is:
$$ \lambda = \frac{m}{\ell} $$
The mass of the hanging segment of length $x(t)$ is:
$$ m_{\text{hang}}(t) = \lambda x(t) = \frac{m}{\ell} x(t) $$
The gravitational force pulling the hanging portion downward is:
$$ F_g(t) = m_{\text{hang}}(t) g = \frac{m}{\ell} g x(t) $$
Since the table is frictionless, no opposing friction force acts on the horizontal segment.
Applying Newton's second law to the entire chain of constant total mass $m$:
$$ m \ddot{x}(t) = F_g(t) = \frac{m}{\ell} g x(t) $$
Dividing both sides by the total mass $m$:
$$ \ddot{x}(t) = \frac{g}{\ell} x(t) \iff \mathbf{\ddot{x} - \frac{g}{\ell} x = 0} \tag{1} $$

---

### Step 2: Characteristic Equation and General Solution
Define the characteristic time scale parameter:
$$ \alpha \equiv \sqrt{\frac{g}{\ell}} \tag{2} $$
The differential equation becomes:
$$ \ddot{x} - \alpha^2 x = 0 $$
The characteristic auxiliary polynomial is:
$$ r^2 - \alpha^2 = 0 \implies r = \pm \alpha $$
The two linearly independent solutions are $e^{\alpha t}$ and $e^{-\alpha t}$, or equivalently the hyperbolic basis:
$$ x(t) = c_1 \cosh(\alpha t) + c_2 \sinh(\alpha t) \tag{3} $$
The velocity is given by differentiating with respect to $t$:
$$ \dot{x}(t) = \alpha \left[ c_1 \sinh(\alpha t) + c_2 \cosh(\alpha t) \right] \tag{4} $$

---

### Step 3: Determining Constants from Initial Conditions
Evaluating position and velocity at $t = 0$:
$$ x(0) = c_1 \cosh(0) + c_2 \sinh(0) = c_1 \cdot 1 + c_2 \cdot 0 = c_1 $$
Given that the chain starts with $x(0) = x_0 = 1\text{ m}$:
$$ c_1 = x_0 = 1\text{ m} \tag{5a} $$

Given that the chain is released from rest ($\dot{x}(0) = 0$):
$$ \dot{x}(0) = \alpha \left[ c_1 \sinh(0) + c_2 \cosh(0) \right] = \alpha (c_1 \cdot 0 + c_2 \cdot 1) = \alpha c_2 = 0 $$
Since $\alpha > 0$:
$$ c_2 = 0 \tag{5b} $$

Substituting $c_1 = x_0$ and $c_2 = 0$ into equation (3):
$$ \mathbf{x(t) = x_0 \cosh(\alpha t) = x_0 \cosh\left( \sqrt{\frac{g}{\ell}}\,t \right)} \tag{6} $$

---

### Step 4: Analytical Resolution for the Detachment Time $t_*$
The entire chain has fallen off the table when the overhanging length equals the total length $\ell$:
$$ x(t_*) = \ell $$
Substituting into equation (6):
$$ x_0 \cosh(\alpha t_*) = \ell \implies \cosh(\alpha t_*) = \frac{\ell}{x_0} \tag{7} $$
Inverting the hyperbolic cosine function:
$$ \alpha t_* = \operatorname{arcosh}\left(\frac{\ell}{x_0}\right) = \ln\left( \frac{\ell}{x_0} + \sqrt{\left(\frac{\ell}{x_0}\right)^2 - 1} \right) \tag{8} $$
Dividing by $\alpha = \sqrt{g/\ell}$:
$$ \mathbf{t_* = \sqrt{\frac{\ell}{g}} \ln\left( \frac{\ell}{x_0} + \sqrt{\left(\frac{\ell}{x_0}\right)^2 - 1} \right)} \tag{9} $$

---

### Step 5: Numerical Evaluation
Substitute the physical values:
- $\ell = 5\text{ m}$
- $x_0 = 1\text{ m} \implies \frac{\ell}{x_0} = \frac{5}{1} = 5$
- Standard gravity: $g = 9.8\text{ m/s}^2$

1. Compute $\alpha$:
   $$ \alpha = \sqrt{\frac{9.8}{5}} = \sqrt{1.96} = 1.4\text{ s}^{-1} $$
   $$ \sqrt{\frac{\ell}{g}} = \frac{1}{\alpha} = \frac{1}{1.4} = \frac{5}{7}\text{ s} \approx 0.714286\text{ s} $$

2. Compute the logarithmic factor:
   $$ \frac{\ell}{x_0} + \sqrt{\left(\frac{\ell}{x_0}\right)^2 - 1} = 5 + \sqrt{5^2 - 1} = 5 + \sqrt{24} = 5 + 2\sqrt{6} $$
   $$ \sqrt{24} \approx 4.898979 \implies 5 + \sqrt{24} \approx 9.898979 $$
   $$ \ln(5 + \sqrt{24}) \approx \ln(9.898979) \approx 2.292432 $$

3. Compute $t_*$:
   $$ t_* = \frac{2.292432}{1.4} \approx \mathbf{1.63745\text{ s} \approx 1.637\text{ s}} $$

*(Note: If using $g = 9.81\text{ m/s}^2$, $\alpha = \sqrt{9.81/5} \approx 1.400714\text{ s}^{-1} \implies t_* = \frac{2.292432}{1.400714} \approx 1.6366\text{ s} \approx 1.637\text{ s}$).*

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Formulas:
$$ \boxed{x(t) = \cosh(1.4\,t)\text{ m}} $$
$$ \boxed{t_* = \frac{\operatorname{arcosh}(5)}{1.4} = \frac{\ln(5 + 2\sqrt{6})}{1.4} \approx 1.637\text{ s}} $$

### Physical Speed at Detachment:
Differentiating equation (6):
$$ v(t) = \dot{x}(t) = x_0 \alpha \sinh(\alpha t) $$
At $t = t_*$, using the identity $\sinh(\operatorname{arcosh} u) = \sqrt{u^2 - 1}$:
$$ v(t_*) = x_0 \alpha \sqrt{\left(\frac{\ell}{x_0}\right)^2 - 1} = 1 \cdot 1.4 \cdot \sqrt{24} = 1.4 \times 4.89898 \approx \mathbf{6.859\text{ m/s}} $$

### Energy Verification (Conservation of Mechanical Energy):
- Initial energy (at rest with $x = x_0$):
  $$ E_0 = -m_{\text{hang}}(0) g \left(\frac{x_0}{2}\right) = -\frac{m}{\ell} g \frac{x_0^2}{2} $$
- Final energy at detachment (entire mass moving at $v_*$, center of gravity at $-\ell/2$):
  $$ E_f = \frac{1}{2}m v_*^2 - mg\frac{\ell}{2} $$
- By energy conservation:
  $$ \frac{1}{2}m v_*^2 = mg\frac{\ell}{2} - \frac{m}{\ell} g \frac{x_0^2}{2} = \frac{mg}{2\ell}(\ell^2 - x_0^2) $$
  $$ v_*^2 = \frac{g}{\ell}(\ell^2 - x_0^2) = \alpha^2 (\ell^2 - x_0^2) = (1.4)^2 (25 - 1) = 1.96 \times 24 = 47.04 $$
  $$ v_* = \sqrt{47.04} \approx 6.85857\text{ m/s} $$
The energy conservation calculation matches our ODE solution with exact precision!

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Ecuaciones Homogeneas con Coeficientes Constantes y Ecuacion Caracteristica|Ecuaciones Homogéneas]]`
* `[[04 - Advanced Maths/Problema - Ch3-P5 Saddle Invariant Manifold and Asymptotic Decay|Problem 3.5: Saddle Invariant Manifold]]`
* `[[04 - Advanced Maths/Problema - Ch3-P7 Simple Pendulum Energy and Small Oscillations|Problem 3.7: Pendulum Energy]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
