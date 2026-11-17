---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 4"
dificultad: easy
badge: "Isostrain modulus · strength · load fraction"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - load-sharing
  - aramid
---

# ✏️ Problem: T10-04 — Modulus, Strength and Load Fraction of a Kevlar 49-Epoxy Composite

## 📄 Official Statement
> 4. Calculate the elastic modulus of a unidirectional composite material with epoxy matrix and Kevlar 49 fibers, where 63% of its volume is fibers and is under isostrain conditions. If the tensile strength of Kevlar 49 fibers is 3700 MPa and the tensile strength of the epoxy resin is 70 MPa, calculate the tensile strength of the composite material. What fraction of load is carried by the Kevlar fibers?
>
> Data: E_kevlar = 131 GPa; E_epoxy = 3.5 GPa.
>
> *(Solution: a) 83.82 GPa; b) 2.36 GPa; c) 0.984)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Isostrain.** Load along the aligned fibres, perfect bond: $\varepsilon_C = \varepsilon_f = \varepsilon_m$ and $E_{1C} = V_f E_f + (1 - V_f)E_m$ [Session 22 Slides 21-22].
2. **Strength.** $\sigma_C = \sigma_f V_f + \sigma_{y,m}(1 - V_f)$ [Session 22 Slide 26], with the given resin strength as the matrix term.
3. **Load sharing.** The total force is the sum of the forces in the phases, $F_C = F_f + F_m$, and $F_i = \sigma_i A_i$ [Session 22 Slide 21]. With a common strain, $\sigma_f = E_f\varepsilon$ and $\sigma_C = E_{1C}\varepsilon$, and $A_f/A_C = V_f$ for continuous fibres, so

$$\frac{F_f}{F_C} = \frac{\sigma_f A_f}{\sigma_C A_C} = \frac{E_f\varepsilon\,V_f}{E_{1C}\varepsilon} = \frac{V_f E_f}{E_{1C}}$$

### Data
| Quantity | Value |
| :--- | ---: |
| $V_f$ | 0.63 |
| $E_f$, $E_m$ | 131 GPa, 3.5 GPa |
| $\sigma_f$, $\sigma_m$ | 3700 MPa, 70 MPa |

**Unknowns:** $E_{1C}$, $\sigma_C$, $F_f/F_C$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 21, 22, 26]:

$$E_{1C} = V_f E_f + (1 - V_f)E_m \qquad \sigma_C = V_f\sigma_f + (1 - V_f)\sigma_m \qquad \frac{F_f}{F_C} = \frac{V_f E_f}{E_{1C}}$$

**Strategy.** Apply the three relations in order; the load fraction needs the modulus of the first step.

---

## 🔢 3. Step-by-Step Derivation

### 1. Elastic modulus [Session 22 Slide 22]

$$E_{1C} = 0.63 \times 131\ \text{GPa} + 0.37 \times 3.5\ \text{GPa} = 82.53 + 1.295 = \mathbf{83.83\ GPa}$$

### 2. Tensile strength [Session 22 Slide 26]

$$\sigma_C = 0.63 \times 3700\ \text{MPa} + 0.37 \times 70\ \text{MPa} = 2331 + 25.9 = 2356.9\ \text{MPa} = \mathbf{2.36\ GPa}$$

### 3. Fraction of the load carried by the fibres [Session 22 Slide 21]

$$\frac{F_f}{F_C} = \frac{0.63 \times 131\ \text{GPa}}{83.825\ \text{GPa}} = \frac{82.53}{83.825} = \mathbf{0.985}$$

The fibres carry 98.5 % of the load and the epoxy the remaining 1.5 %.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** GPa in the modulus, MPa in the strength; the load fraction is GPa/GPa, dimensionless.
- **Bounds.** $3.5 < 83.8 < 131$ GPa and $70 < 2357 < 3700$ MPa.
- **Approximation of the slides.** With $E_f \gg E_m$, $E_{1C} \approx V_f E_f = 82.5$ GPa, within 1.5 % of the full result [Session 22 Slide 22].
- **Limits.** $F_f/F_C \to 1$ when $E_m \to 0$, and $F_f/F_C = V_f$ when $E_f = E_m$ (a homogeneous material shares the load by area).

### Interpretation
Under isostrain the stress in each phase is proportional to its modulus, so the fibre, 37 times stiffer than the epoxy, works at 37 times the stress. That is the "redistribution of the load" of Slide 22: the matrix holds the fibres in place and transfers the load, but almost all of it is carried by the fibres [Session 21 Slide 16].

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $E_{1C}$ | 83.82 GPa | 83.83 GPa | agrees |
| b) $\sigma_C$ | 2.36 GPa | 2.357 GPa | agrees |
| c) $F_f/F_C$ | 0.984 | 0.9846 (0.985) | agrees; the key truncates instead of rounding |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-06 Carbon-Epoxy Composite in psi Modulus Strength and Load Fraction|Problem T10-06]]
