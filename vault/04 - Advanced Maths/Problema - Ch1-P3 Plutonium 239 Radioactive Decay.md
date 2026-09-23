---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.3"
dificultad: baja
tags:
  - problema-resuelto
  - decaimiento-radiactivo
  - vida-media
  - plutonio-239
  - edos-separables
---

# ✏️ Problem 1.3: Plutonium-239 Radioactive Decay

## 📄 Enunciado (Problem Statement)

Plutonium 239, virtually nonexistent in nature, is one of the radioactive materials used in the production of nuclear weapons, and is a byproduct of the generation of power in a nuclear reactor. Its half-life (i.e., the time it takes for half of the radioactive isotope to decay) is approximately 24,000 years.

Using $\frac{dN}{dt} = -kN$ as an appropriate model for radioactive decay, where $N = N(t)$ is the number of isotopes at time $t$, what is the value of $k$ that should be used for this isotope?

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Known Data:
* Half-life of Plutonium-239: $t_{1/2} = 24{,}000\text{ years} = 2.4 \times 10^4\text{ yr}$.
* Differential model: $\frac{dN}{dt} = -kN$, where $k > 0$.
* Initial number of isotopes at $t = 0$: $N(0) = N_0$.

### Unknown:
* Radioactive decay constant: $k$ $[\text{yr}^{-1}]$ (and in SI units $[\text{s}^{-1}]$).

### Hypotheses:
* [x] **First-order kinetic law:** The probability of nuclear disintegration per unit time is constant for each individual $^{239}\text{Pu}$ nucleus.
* [x] **No external transmutation source:** The isotope is stored in an unpowered environment with no active neutron capture reactions producing new $^{239}\text{Pu}$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Solve the first-order linear homogeneous ODE $\frac{dN}{dt} = -kN$ subject to the initial condition $N(0) = N_0$ via separation of variables.
2. Apply the physical definition of **half-life**: at $t = t_{1/2}$, the remaining quantity of active isotopes equals exactly half of the initial quantity:
   $$ N(t_{1/2}) = \frac{1}{2} N_0 $$
3. Substitute the half-life condition into the analytical solution and isolate the decay parameter $k$ using logarithmic properties.
4. Perform the high-precision numerical evaluation.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Solution of the Radioactive Decay ODE
The governing differential equation is:
$$ \frac{dN}{dt} = -k N $$

For $N > 0$, separate variables:
$$ \frac{1}{N} \, dN = -k \, dt $$

Integrate both sides from $t = 0$ ($N = N_0$) to time $t$ ($N = N(t)$):
$$ \int_{N_0}^{N(t)} \frac{1}{\xi} \, d\xi = \int_0^t -k \, ds $$
$$ \left[ \ln(\xi) \right]_{N_0}^{N(t)} = -k [s]_0^t $$
$$ \ln(N(t)) - \ln(N_0) = -k t $$
Combine logarithms:
$$ \ln\left( \frac{N(t)}{N_0} \right) = -k t $$

Exponentiate both sides:
$$ \frac{N(t)}{N_0} = e^{-kt} \implies \mathbf{N(t) = N_0 e^{-kt}} \tag{1} $$

---

### Step 2: Application of the Half-Life Definition
By definition of half-life, when $t = t_{1/2} = 24{,}000\text{ yr}$, the isotope count is halved:
$$ N(t_{1/2}) = \frac{N_0}{2} $$

Substitute this into equation $(1)$:
$$ N_0 e^{-k t_{1/2}} = \frac{N_0}{2} $$

Divide both sides by $N_0 \neq 0$:
$$ e^{-k t_{1/2}} = \frac{1}{2} = 2^{-1} \tag{2} $$

---

### Step 3: Exact Isolation of $k$
Take the natural logarithm $\ln(\cdot)$ of both sides of $(2)$:
$$ \ln\left( e^{-k t_{1/2}} \right) = \ln\left( 2^{-1} \right) $$

Using the logarithm power rule $\ln(2^{-1}) = -\ln(2)$:
$$ -k t_{1/2} = -\ln(2) $$

Multiply both sides by $-1$:
$$ k t_{1/2} = \ln(2) $$

Isolating the decay constant $k$:
$$ \mathbf{k = \frac{\ln(2)}{t_{1/2}}} \tag{3} $$

---

### Step 4: Numerical Evaluation
Substitute $t_{1/2} = 24{,}000\text{ years}$ and the value of $\ln(2) \approx 0.69314718$:
$$ k = \frac{\ln 2}{24{,}000} = \frac{0.69314718}{24{,}000}\text{ yr}^{-1} $$
$$ k \approx 2.88811 \times 10^{-5}\text{ yr}^{-1} $$

#### SI Unit Conversion (for Aerospace / Physics standards):
Taking $1\text{ civil year} \approx 365.25\text{ days} = 365.25 \times 86{,}400\text{ s} = 31{,}557{,}600\text{ s}$:
$$ k_{\text{SI}} = \frac{2.88811 \times 10^{-5}\text{ yr}^{-1}}{31{,}557{,}600\text{ s/yr}} \approx 9.1519 \times 10^{-13}\text{ s}^{-1} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Value of Decay Constant:
$$ \mathbf{k = \frac{\ln 2}{24{,}000}\text{ yr}^{-1} \approx 2.888 \times 10^{-5}\text{ yr}^{-1}} $$

### Verification & Physical Implications:
1. **Dimensional Verification:**
   $$ [k] = \frac{[\ln 2]}{[t_{1/2}]} = \frac{1}{\text{year}} = [\text{Time}]^{-1} $$
   Multiplying by $N$ (dimensionless count) yields $[dN/dt] = \text{count/year}$, satisfying dimensional homogeneity.
2. **Nuclear Safety and Space Power:**
   * A decay constant on the order of $10^{-5}\text{ yr}^{-1}$ reflects a very slow rate of radioactive decay, explaining why $^{239}\text{Pu}$ poses an extremely persistent radiological concern over geological timescales (it takes $10 \times t_{1/2} = 240{,}000\text{ years}$ to reduce its activity to $(1/2)^{10} \approx 0.098\%$ of its initial value).
   * For spaceborne Radioisotope Thermoelectric Generators (RTGs, such as those on Voyager, Cassini, and Curiosity), the shorter-lived isotope $^{238}\text{Pu}$ ($t_{1/2} \approx 87.7\text{ years}$) is preferred because its higher decay rate produces much greater specific thermal power per unit mass.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - First-Order Physical Models|First-Order Physical Models]]`
* `[[04 - Advanced Maths/Problema - Ch1-P2 Malthusian Population Dynamics|Problem 1.2: Doubling Time vs. Half-Life]]`
