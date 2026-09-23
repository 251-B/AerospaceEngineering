---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.5"
dificultad: media
tags:
  - problema-resuelto
  - ley-enfriamiento-newton
  - forense
  - estimacion-tiempo-muerte
  - edos-primer-orden
---

# ✏️ Problem 1.5: Forensic Time of Death Estimation

## 📄 Enunciado (Problem Statement)

A body is found in a cold room ($T_A = 5^\circ\text{C}$) at 3 pm, and its temperature then is $19^\circ\text{C}$. An hour later its temperature has dropped to $15^\circ\text{C}$. Use Newton's law of cooling to estimate the time of death, assuming that the living body temperature is $37^\circ\text{C}$ and measuring time in hours.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Known Data:
* Ambient temperature of the room: $T_A = 5^\circ\text{C}$ (constant).
* Time reference convention: Let $t = 0\text{ h}$ correspond to **3:00 pm**.
* Body temperature at discovery ($t = 0$): $T(0) = 19^\circ\text{C}$.
* Body temperature one hour later ($t = 1\text{ h}$, 4:00 pm): $T(1) = 15^\circ\text{C}$.
* Normal physiological living human body temperature: $T(t_d) = 37^\circ\text{C}$.

### Unknowns to Determine:
1. Cooling parameter $k$ $[\text{h}^{-1}]$.
2. Elapsed time back to death: $t_d < 0$ $[\text{h}]$.
3. Actual clock time of death.

### Hypotheses:
* [x] **Constant ambient temperature:** $T_A = 5^\circ\text{C}$ remained uniform and constant from the time of death until discovery.
* [x] **Lumped thermal model:** Newton's law of cooling accurately describes post-mortem cooling (algor mortis).
* [x] **Homeostatic stability prior to death:** The person was alive and had a healthy core temperature of $37^\circ\text{C}$ up to the exact moment of death $t_d$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Formulate the initial value problem using Newton's law of cooling:
   $$ \frac{dT}{dt} = -k(T - T_A) $$
2. Solve the differential equation with $T_A = 5^\circ\text{C}$ and initial condition $T(0) = 19^\circ\text{C}$.
3. Use the measurement at $t = 1\text{ h}$ ($T = 15^\circ\text{C}$) to calculate the exact cooling rate parameter $k = \ln(1.4)$.
4. Set the general solution equal to the living temperature $37^\circ\text{C}$ and solve analytically for $t_d$.
5. Convert the decimal hours into hours and minutes, subtracting from 3:00 pm to establish the clock time.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Solution of the Differential Equation
With constant $T_A = 5^\circ\text{C}$:
$$ \frac{dT}{dt} = -k(T - 5) $$

Defining the temperature difference variable $\theta(t) = T(t) - 5$:
$$ \frac{d\theta}{dt} = -k \theta $$
Separating variables and integrating from $t = 0$ to $t$:
$$ \int_{\theta(0)}^{\theta(t)} \frac{d\xi}{\xi} = \int_0^t -k \, ds \implies \ln\left( \frac{\theta(t)}{\theta(0)} \right) = -kt $$
$$ \theta(t) = \theta(0) e^{-kt} $$

Since $\theta(0) = T(0) - 5 = 19 - 5 = 14^\circ\text{C}$:
$$ T(t) - 5 = 14 e^{-kt} $$
$$ \mathbf{T(t) = 5 + 14 e^{-kt}} \tag{1} $$

---

### Step 2: Determination of the Cooling Parameter $k$
Use the experimental observation at $t = 1\text{ h}$ ($T(1) = 15^\circ\text{C}$):
$$ 15 = 5 + 14 e^{-k(1)} $$

Subtract $5$ from both sides:
$$ 10 = 14 e^{-k} $$

Divide by $14$:
$$ e^{-k} = \frac{10}{14} = \frac{5}{7} $$

Invert both sides to obtain $e^k$:
$$ e^k = \frac{7}{5} = 1.4 $$

Take the natural logarithm:
$$ \mathbf{k = \ln(1.4) = \ln\left(\frac{7}{5}\right) \approx 0.336472\text{ h}^{-1}} \tag{2} $$

---

### Step 3: Calculation of the Time of Death $t_d$
At the moment of death $t = t_d$, the body temperature was $T(t_d) = 37^\circ\text{C}$. Substitute into $(1)$:
$$ 37 = 5 + 14 e^{-k t_d} $$

Subtract $5$ from both sides:
$$ 32 = 14 e^{-k t_d} $$

Divide by $14$:
$$ e^{-k t_d} = \frac{32}{14} = \frac{16}{7} $$

Take the natural logarithm of both sides:
$$ -k t_d = \ln\left( \frac{16}{7} \right) $$

Multiply by $-1$ and divide by $k$:
$$ t_d = -\frac{\ln(16/7)}{k} = -\frac{\ln(16/7)}{\ln(7/5)} \tag{3} $$

Evaluating the logarithms numerically:
$$ \ln\left(\frac{16}{7}\right) = \ln(2.285714...) \approx 0.826679 $$
$$ \ln\left(\frac{7}{5}\right) = \ln(1.4) \approx 0.336472 $$

Substitute into $(3)$:
$$ t_d = -\frac{0.826679}{0.336472} \approx \mathbf{-2.45690\text{ hours}} $$

---

### Step 4: Conversion to Clock Time
The negative sign confirms that death occurred prior to the discovery time of $3:00\text{ pm}$.

1. Separate integer hours and fractional hours:
   $$ |t_d| = 2.45690\text{ hours} = 2\text{ hours} + 0.45690\text{ hours} $$
2. Convert fractional hours to minutes:
   $$ 0.45690 \times 60\text{ minutes} \approx 27.41\text{ minutes} \approx 27\text{ minutes and } 25\text{ seconds} $$
3. Subtract $2\text{ hours and } 27.41\text{ minutes}$ from $3:00\text{ pm}$ (15:00):
   * $3:00\text{ pm} - 2\text{ hours} = 1:00\text{ pm}$
   * $1:00\text{ pm} - 27.41\text{ minutes} = \mathbf{12:32:35\text{ pm} \approx 12:33\text{ pm}}$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Answers:
* **Cooling Rate Constant:** $k = \ln(1.4) \approx 0.3365\text{ h}^{-1}$
* **Time Elapsed Before Discovery:** $\Delta t_{\text{death}} \approx 2\text{ h } 27\text{ min}$
* **Estimated Time of Death:** $\mathbf{\approx 12:33\text{ pm}}$ (between 12:32 pm and 12:33 pm).

### Physical Consistency Check:
1. **Monotonic Cooling Check:**
   $$ T(t_d) = 37^\circ\text{C} > T(0) = 19^\circ\text{C} > T(1) = 15^\circ\text{C} > T_A = 5^\circ\text{C} $$
   The temperature monotonically decreases towards ambient room temperature, consistent with the 2nd Law of Thermodynamics.
2. **Cooling Rate Deceleration:**
   Between death and 3:00 pm (span of $2.46\text{ h}$), $\Delta T = 37 - 19 = 18^\circ\text{C}$ (average cooling rate $\approx 7.3^\circ\text{C/h}$).
   Between 3:00 pm and 4:00 pm (span of $1\text{ h}$), $\Delta T = 19 - 15 = 4^\circ\text{C/h}$.
   Because the temperature gradient $(T - T_A)$ decreased from $32^\circ\text{C}$ down to $14^\circ\text{C}$, the cooling rate correctly decelerated.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - First-Order Physical Models|First-Order Physical Models]]`
* `[[04 - Advanced Maths/Problema - Ch1-P4 Newton Law of Cooling Modeling|Problem 1.4: Newton's Law of Cooling Formulation]]`
