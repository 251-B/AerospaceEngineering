---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 5"
dificultad: medium
badge: "Isostrain rod · phase forces · elongation"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - load-sharing
  - glass-fibre
---

# ✏️ Problem: T10-05 — E-Glass Polyester Rod: Modulus, Fibre and Matrix Forces and Extension

## 📄 Official Statement
> 5. For an E-glass fiber reinforced polyester composite with continuous aligned fibers, with 40% vol fraction fibers:
> a) Determine the Modulus of elasticity in the longitudinal direction
> b) If a cylindrical rod 19 mm in diameter of this composite is stressed in the longitudinal direction to 50 MPa, determine the forces in the fiber and matrix phases, respectively.
> c) Estimate the specific tensile strength of the composite.
> d) If the rod was originally 1.5 m long, estimate its extension under the applied stress.
>
> Data: E_m = 3400 MPa; σ_m = 69 MPa; ρ_m = 1.3 g/cm³; E_f = 72000 MPa, σ_f = 3500 MPa; ρ_f = 2.5 g/cm³.
>
> *(Solution: a) 30.8 GPa; b) 13212N; 964N; c ) 809.8 kN m/kg; d) 2.44 mm)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Isostrain** along the fibres with a perfect bond, $\varepsilon_C = \varepsilon_f = \varepsilon_m$ [Session 22 Slide 21]; linear elastic phases, so $\sigma_i = E_i\varepsilon$ [Session 22 Slide 20].
2. **Forces.** $F_C = F_f + F_m$ with $F_i = \sigma_i A_i$ and $A_f = V_f A_C$, $A_m = V_m A_C$ [Session 22 Slide 21].
3. **Strength and density** by the rule of mixtures [Session 22 Slides 26-27]; specific strength = strength/density [Session 21 Slide 43].
4. **Extension.** Uniform strain over the length, $\Delta L = \varepsilon L_0$.

### Data
| Quantity | Fibre (E-glass) | Matrix (polyester) |
| :--- | ---: | ---: |
| $V$ | 0.40 | 0.60 |
| $E$ (MPa) | 72 000 | 3 400 |
| $\sigma$ (MPa) | 3 500 | 69 |
| $\rho$ (g/cm³) | 2.5 | 1.3 |

Rod: $d = 19$ mm, $\sigma_C = 50$ MPa, $L_0 = 1.5$ m.

**Unknowns:** (a) $E_{1C}$; (b) $F_f$, $F_m$; (c) $\sigma_C/\rho_c$ at failure; (d) $\Delta L$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 21-22, 26-27]:

$$E_{1C} = V_f E_f + V_m E_m \qquad \varepsilon = \frac{\sigma_C}{E_{1C}} \qquad F_i = E_i\,\varepsilon\,V_i A_C \qquad \Delta L = \varepsilon L_0$$

**Strategy.**
1. Modulus by the isostrain rule (a).
2. Common strain from the applied stress; stress in each phase from Hooke's law; force = stress × phase area (b).
3. Strength and density by the rule of mixtures, then their ratio (c).
4. Extension from the same strain (d).

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Longitudinal modulus [Session 22 Slide 22]

$$E_{1C} = 0.40 \times 72\,000\ \text{MPa} + 0.60 \times 3\,400\ \text{MPa} = 28\,800 + 2\,040 = 30\,840\ \text{MPa} = \mathbf{30.8\ GPa}$$

### 2. b) Forces in the fibre and matrix [Session 22 Slide 21]
Cross-section and total force:

$$A_C = \frac{\pi d^2}{4} = \frac{\pi\,(19\ \text{mm})^2}{4} = 283.53\ \text{mm}^2 \qquad F_C = \sigma_C A_C = 50\ \text{N/mm}^2 \times 283.53\ \text{mm}^2 = 14\,176\ \text{N}$$

Common strain and phase stresses:

$$\varepsilon = \frac{50\ \text{MPa}}{30\,840\ \text{MPa}} = 1.6213\times10^{-3} \qquad \sigma_f = 72\,000 \times 1.6213\times10^{-3} = 116.73\ \text{MPa} \qquad \sigma_m = 3\,400 \times 1.6213\times10^{-3} = 5.512\ \text{MPa}$$

Forces:

$$F_f = \sigma_f V_f A_C = 116.73\ \text{N/mm}^2 \times 0.40 \times 283.53\ \text{mm}^2 = \mathbf{13\,239\ N}$$

$$F_m = \sigma_m V_m A_C = 5.512\ \text{N/mm}^2 \times 0.60 \times 283.53\ \text{mm}^2 = \mathbf{938\ N}$$

### 3. c) Specific tensile strength [Session 22 Slides 26-27]

$$\sigma_C = 0.40 \times 3\,500 + 0.60 \times 69 = 1\,400 + 41.4 = 1\,441.4\ \text{MPa} \qquad \rho_c = 0.40 \times 2.5 + 0.60 \times 1.3 = 1.78\ \text{g/cm}^3$$

$$\frac{\sigma_C}{\rho_c} = \frac{1\,441.4\times10^6\ \text{N/m}^2}{1\,780\ \text{kg/m}^3} = 809.8\times10^3\ \text{N m/kg} = \mathbf{809.8\ kN\,m/kg}$$

### 4. d) Extension of the rod

$$\Delta L = \varepsilon L_0 = 1.6213\times10^{-3} \times 1\,500\ \text{mm} = \mathbf{2.43\ mm}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** MPa = N/mm², so N/mm² × mm² = N. $(\text{N/m}^2)/(\text{kg/m}^3) = \text{N m/kg}$ (J/kg, the same as m²/s²).
- **Force balance.** $13\,239 + 938 = 14\,177$ N $= F_C$ (rounding).
- **Ratio of forces.** $F_f/F_m = V_f E_f/(V_m E_m) = 28\,800/2\,040 = 14.12$; also $13\,239/938 = 14.1$.
- **Stress balance.** $0.40 \times 116.73 + 0.60 \times 5.512 = 46.69 + 3.31 = 50.0$ MPa, the applied stress [Session 22 Slide 21].
- **Strain.** $1.6\times10^{-3}$ is far below the failure strain of the glass fibre, about $3500/72\,000 = 4.9\times10^{-3}$, so the rod is elastic.

### Interpretation
At 40 vol% the glass carries 93.4 % of the load. The specific strength, about 810 kN m/kg, is the property where glass-fibre composites stand well above steel and aluminium in the comparisons of the slides [Session 21 Slide 43; Session 22 Slide 29], while their modulus (30.8 GPa) stays below that of aluminium: glass is chosen for strength and cost, not stiffness [Session 21 Slide 17].

> [!warning] Discrepancy with the official solution
> The key splits the 14 176 N as 13 212 N (fibre) and 964 N (matrix). Under isostrain the ratio of the two forces is fixed by the data: $F_f/F_m = V_f E_f/(V_m E_m) = (0.40 \times 72\,000)/(0.60 \times 3\,400) = 14.12$, while the key gives $13\,212/964 = 13.71$, and its fibre share $13\,212/14\,176 = 0.932$ differs from $V_f E_f/E_{1C} = 28\,800/30\,840 = 0.934$. The computed forces, 13 239 N and 938 N, satisfy both the force balance and the isostrain ratio, so they are kept. Part d): $\Delta L = 2.43$ mm; the key's 2.44 mm follows from rounding $E_{1C}$ to 30.8 GPa ($50/30\,800 \times 1500 = 2.435$ mm).

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $E_{1C}$ | 30.8 GPa | 30.84 GPa | agrees |
| b) $F_f$, $F_m$ | 13212 N; 964 N | 13 239 N; 938 N | differs (see the warning) |
| c) $\sigma_C/\rho_c$ | 809.8 kN m/kg | 809.8 kN m/kg | agrees |
| d) $\Delta L$ | 2.44 mm | 2.43 mm | agrees within rounding |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-10 Stress on the Fibres of a Glass-Epoxy Rod|Problem T10-10]]
