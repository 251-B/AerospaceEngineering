---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 10"
dificultad: baja-media
tags:
  - problema-resuelto
  - paracaidista
  - resistencia-lineal
  - velocidad-terminal
  - dinamica-atmosferica
---

# ✏️ Problem 3.10: Parachutist Linear Drag and Terminal Velocity

## 📄 Enunciado (Problem Statement)

A parachutist of mass $m\text{ kg}$ jumps from a plane with initial velocity $0$. Because of the parachute, there is a friction force that avoids free fall; this friction turns out to be proportional (with constant of proportionality $c > 0$) to the velocity.  
Write down an ODE to describe the motion of the parachutist, and determine the terminal speed (when $t \to \infty$). Compare this speed with that of free fall.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Physical Parameters:
- Total system mass (jumper + parachute + gear): $m > 0$ [$\text{kg}$]
- Gravitational acceleration: $g > 0$ [$\text{m/s}^2$] (assumed constant in troposphere)
- Aerodynamic drag coefficient: $c > 0$ [$\text{N}\cdot\text{s/m}$ or $\text{kg/s}$]
- State variables:
  * Downward vertical displacement: $y(t)$ [$\text{m}$] with $y(0) = 0$
  * Downward vertical speed: $v(t) = \dot{y}(t)$ [$\text{m/s}$]
- Initial Cauchy condition:
  $$ v(0) = 0\text{ m/s} $$
- Forces acting on system (taking positive direction pointing downward):
  * Gravity: $F_g = +mg$
  * Aerodynamic drag: $F_{\text{drag}} = -c v(t)$ (directed opposing the velocity vector)

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

### Plan:
1. **Newton's Second Law Formulation:**
   $$ \sum F_y = m a_y \implies m \frac{dv}{dt} = mg - cv $$
   Equivalently, in terms of displacement $y(t)$, this is a second-order linear ODE:
   $$ m \ddot{y} + c \dot{y} = mg $$
2. **Solve the Velocity ODE:**
   Normalize to canonical first-order linear form $\dot{v} + \frac{c}{m} v = g$.
   Use an integrating factor $\mu(t) = \exp\left(\int \frac{c}{m} dt\right) = e^{(c/m)t}$ or decompose into homogeneous plus particular solution.
3. **Impose Initial Condition $v(0) = 0$:**
   Determine the integration constant and isolate $v(t)$.
4. **Determine Terminal Velocity $v_\infty$:**
   Compute the asymptotic limit $\lim_{t \to \infty} v(t)$.
5. **Physical Comparison with Free Fall:**
   Contrast the bounded drag trajectory with the uninhibited free-fall kinematics $v_{\text{free}}(t) = gt$, analyzing short-time ($t \ll \tau$) and long-time ($t \gg \tau$) asymptotic regimes.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Formulation of the Ordinary Differential Equation
Applying Newton's second law along the downward vertical axis:
$$ m \frac{dv}{dt} = mg - c v(t) $$
Dividing by $m$:
$$ \mathbf{\frac{dv}{dt} + \frac{c}{m} v = g} \tag{1} $$
Or expressed in terms of vertical position $y(t)$ with $v = \dot{y}$:
$$ \mathbf{m \ddot{y} + c \dot{y} = mg \iff \ddot{y} + \frac{c}{m} \dot{y} = g} \tag{1'} $$

Define the aerodynamic characteristic relaxation time:
$$ \tau \equiv \frac{m}{c} \quad [\text{s}] $$
Then equation (1) reads: $\dot{v} + \frac{1}{\tau} v = g$.

---

### Step 2: Analytical Solution via Integrating Factor
The integrating factor for equation (1) is:
$$ \mu(t) = \exp\left( \int \frac{c}{m} \, dt \right) = e^{(c/m)t} $$
Multiplying equation (1) by $\mu(t)$:
$$ e^{(c/m)t} \frac{dv}{dt} + \frac{c}{m} e^{(c/m)t} v = g e^{(c/m)t} $$
By the product rule, the left-hand side is an exact total derivative:
$$ \frac{d}{dt}\left[ v(t) e^{(c/m)t} \right] = g e^{(c/m)t} $$
Integrating both sides with respect to time $t$:
$$ v(t) e^{(c/m)t} = \int g e^{(c/m)t} \, dt = g \left( \frac{m}{c} \right) e^{(c/m)t} + C = \frac{mg}{c} e^{(c/m)t} + C $$
Multiplying through by $e^{-(c/m)t}$:
$$ v(t) = \frac{mg}{c} + C e^{-(c/m)t} \tag{2} $$

---

### Step 3: Imposition of the Initial Condition $v(0) = 0$
At $t = 0$:
$$ v(0) = \frac{mg}{c} + C e^0 = \frac{mg}{c} + C = 0 \implies C = -\frac{mg}{c} $$
Substituting $C$ back into equation (2):
$$ v(t) = \frac{mg}{c} - \frac{mg}{c} e^{-(c/m)t} $$
$$ \mathbf{v(t) = \frac{mg}{c} \left( 1 - e^{-(c/m)t} \right) = \frac{mg}{c} \left( 1 - e^{-t/\tau} \right)} \tag{3} $$

---

### Step 4: Terminal Speed Calculation ($t \to \infty$)
Since $c > 0$ and $m > 0$, the ratio $\frac{c}{m} > 0$.
Therefore, as $t \to +\infty$:
$$ \lim_{t \to \infty} e^{-(c/m)t} = 0 $$
Evaluating the asymptotic limit of velocity:
$$ v_\infty \equiv \lim_{t \to \infty} v(t) = \lim_{t \to \infty} \left[ \frac{mg}{c} \left( 1 - e^{-(c/m)t} \right) \right] = \frac{mg}{c} (1 - 0) $$
$$ \mathbf{v_\infty = \frac{mg}{c}} \tag{4} $$

*Dynamic Equilibrium Check:*  
Terminal velocity corresponds to steady-state zero acceleration ($\frac{dv}{dt} = 0$).  
Setting $\frac{dv}{dt} = 0$ in equation (1) immediately yields $0 + \frac{c}{m} v_\infty = g \implies v_\infty = \frac{mg}{c}$.

---

### Step 5: Detailed Comparison with Free Fall

| Feature | Free Fall ($c = 0$) | Parachutist with Drag ($c > 0$) |
| :--- | :--- | :--- |
| **Governing ODE** | $\dot{v} = g$ | $\dot{v} + \frac{c}{m} v = g$ |
| **Velocity Function** | $v_{\text{free}}(t) = g t$ | $v(t) = \frac{mg}{c}\left(1 - e^{-(c/m)t}\right)$ |
| **Asymptotic Limit ($t \to \infty$)** | $v \to +\infty$ (Unbounded) | $v \to v_\infty = \frac{mg}{c}$ (Finite Constant) |
| **Acceleration Profile** | Constant: $a(t) \equiv g$ | Decaying: $a(t) = g e^{-(c/m)t} \to 0$ |
| **Displacement $y(t)$** | Parabolic: $y(t) = \frac{1}{2}gt^2$ | Asymptotically Linear: $y(t) \approx v_\infty t - \frac{m^2 g}{c^2}$ |

#### Short-Time Asymptotic Expansion ($t \ll \tau = m/c$):
Using the Taylor series expansion $e^{-u} = 1 - u + \frac{u^2}{2} - \dots$:
$$ 1 - e^{-(c/m)t} = 1 - \left( 1 - \frac{c}{m}t + \frac{c^2}{2m^2}t^2 - \mathcal{O}(t^3) \right) = \frac{c}{m}t - \frac{c^2}{2m^2}t^2 + \dots $$
Substituting into equation (3):
$$ v(t) = \frac{mg}{c} \left( \frac{c}{m}t - \frac{c^2}{2m^2}t^2 + \dots \right) = \mathbf{gt - \frac{cg}{2m}t^2 + \dots} $$
- For times much smaller than the relaxation time ($t \ll m/c$), the velocity is linear: $v(t) \approx gt = v_{\text{free}}(t)$. The parachutist starts identically in free fall.
- As time progresses, aerodynamic drag decelerates the gain in speed until terminal velocity is attained (reaching $99\%$ of $v_\infty$ at $t \approx 4.6 \tau$).

---

## 🎯 4. Resultado Final y Síntesis Aeroespacial (Phase 4)

### Master Formulas:
$$ \boxed{\frac{dv}{dt} + \frac{c}{m}v = g, \quad v(0) = 0} $$
$$ \boxed{v(t) = \frac{mg}{c}\left( 1 - e^{-(c/m)t} \right)} $$
$$ \boxed{v_\infty = \frac{mg}{c}} $$

### Aeronautical Engineering Application:
- In recovery parachute sizing for planetary probes (e.g. Mars landing capsules) or ejector seats, the parachute canopy diameter is calculated so that the terminal velocity satisfies the maximum survivable touch-down impact velocity:
  $$ v_\infty = \frac{mg}{c} \le v_{\text{safe}} \implies c \ge \frac{mg}{v_{\text{safe}}} $$

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - First-Order Physical Models|Modelos Físicos de Primer Orden]]`
* `[[04 - Advanced Maths/Problema - Ch1-P7 Free Fall Motion under Gravity|Problem 1.7: Free Fall Motion]]`
* `[[04 - Advanced Maths/Problema - Ch3-P8 Damped Harmonic Oscillator Regimes|Problem 3.8: Damped Harmonic Oscillator]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
