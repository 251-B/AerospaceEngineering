---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 10"
dificultad: easy
badge: "Isostrain · stress in the fibres"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - load-sharing
  - glass-fibre
---

# ✏️ Problem: T10-10 — Stress on the Fibres of a Glass-Epoxy Rod

## 📄 Official Statement
> 10. An epoxy matrix is reinforced with 40 vol% E-glass fibers to produce a 2-cm-diameter composite that is to withstand a load of 25000 N that is applied parallel to the fiber length. Calculate the stress acting on each fiber.
>
> Data: E_glass fiber = 72.4 x10³ MPa MPa; E_matrix = 2.8 x10³ MPa MPa.
>
> *(Solution: 188 MPa)*

The sheet prints the unit twice ("MPa MPa").

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Isostrain.** The load is parallel to the fibres and the bond is perfect, so fibre, matrix and composite share the strain [Session 22 Slide 21]; each phase is linear elastic, $\sigma_i = E_i\varepsilon$ [Session 22 Slide 20].
2. **Force balance.** $F_C = F_f + F_m$, with $F_i = \sigma_i A_i$ and $A_i = V_i A_C$ [Session 22 Slide 21].
3. **"Each fiber"** carries the same stress, the fibre stress $\sigma_f$, because all fibres have the same strain and the same modulus.

### Data
| Quantity | Value |
| :--- | ---: |
| $V_f$, $V_m$ | 0.40, 0.60 |
| $E_f$, $E_m$ | $72.4\times10^3$, $2.8\times10^3$ MPa |
| $d$ | 2 cm = 20 mm |
| $F_C$ | 25 000 N |

**Unknown:** $\sigma_f$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 21-22]:

$$\sigma_C = \frac{F_C}{A_C} \qquad E_{1C} = V_f E_f + V_m E_m \qquad \varepsilon = \frac{\sigma_C}{E_{1C}} \qquad \sigma_f = E_f\,\varepsilon$$

Combining them, $\sigma_f = \sigma_C E_f/E_{1C}$: the fibre stress is the mean stress amplified by the ratio of the fibre modulus to the composite modulus.

---

## 🔢 3. Step-by-Step Derivation

### 1. Mean stress on the rod

$$A_C = \frac{\pi d^2}{4} = \frac{\pi\,(20\ \text{mm})^2}{4} = 314.16\ \text{mm}^2 \qquad \sigma_C = \frac{25\,000\ \text{N}}{314.16\ \text{mm}^2} = 79.58\ \text{MPa}$$

### 2. Modulus and common strain [Session 22 Slide 22]

$$E_{1C} = 0.40 \times 72.4\times10^3 + 0.60 \times 2.8\times10^3 = 28\,960 + 1\,680 = 30\,640\ \text{MPa}$$

$$\varepsilon = \frac{79.58\ \text{MPa}}{30\,640\ \text{MPa}} = 2.597\times10^{-3}$$

### 3. Stress on the fibres

$$\sigma_f = E_f\,\varepsilon = 72\,400\ \text{MPa} \times 2.597\times10^{-3} = \mathbf{188.0\ MPa}$$

The matrix, at the same strain, carries $\sigma_m = 2\,800 \times 2.597\times10^{-3} = 7.27$ MPa.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** N/mm² = MPa; the strain is MPa/MPa, dimensionless; MPa × dimensionless = MPa.
- **Force balance.** $F_f + F_m = (188.04 \times 0.40 + 7.272 \times 0.60) \times 314.16 = (75.22 + 4.36) \times 314.16 = 25\,000$ N.
- **Stress ratio.** $\sigma_f/\sigma_m = E_f/E_m = 25.9$, as isostrain requires [Session 22 Slide 22].
- **Limit.** If the matrix were as stiff as the fibre, $\sigma_f$ would equal the mean stress 79.6 MPa; the soft matrix pushes the fibre stress up to 2.4 times the mean.

### Interpretation
The fibres work at 188 MPa, far below the strength of E-glass (3450 MPa [Session 21 Slide 18]), while the epoxy works at only 7 MPa: the rod has a large margin, and the margin is set by the fibres, which carry $75.2/79.6 = 94.5$ % of the load.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $\sigma_f$ | 188 MPa | 188.0 MPa | agrees |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-05 E-Glass Polyester Rod Modulus Fibre and Matrix Forces and Extension|Problem T10-05]]
