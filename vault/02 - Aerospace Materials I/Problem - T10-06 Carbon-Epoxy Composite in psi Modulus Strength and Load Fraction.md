---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 6"
dificultad: easy
badge: "Isostrain modulus · strength in psi · load fraction"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - load-sharing
  - unit-conversion
---

# ✏️ Problem: T10-06 — Carbon-Epoxy Composite in psi: Modulus, Strength and Load Fraction

## 📄 Official Statement
> 6. Calculate the tensile modulus of elasticity of a unidirectional carbon-fiber-reinforced plastic composite material that contains 64 percent by volume of carbon fibers and is stressed under isostrain conditions. If the tensile strength of the carbon fibers of the 64 percent carbon-fiber-epoxy composite material is 0.31×10⁶ psi and that of the epoxy resin 9.20×10³ psi, calculate the strength of the composite material in psi. What fraction of the load is carried by the carbon fibers? The carbon fibers have a tensile modulus of elasticity of 54.0×10⁶ psi and the epoxy matrix a tensile modulus of elasticity of 0.530×10⁶ psi.
>
> *(Solution: a) 1.39 GPa; b) 0.995)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Isostrain**, perfect bond: $E_{1C} = V_f E_f + (1 - V_f)E_m$ [Session 22 Slide 22, Eq. 1].
2. **Strength** by the rule of mixtures, $\sigma_C = \sigma_f V_f + \sigma_{y,m}(1 - V_f)$ [Session 22 Slide 26], with the resin strength as the matrix term.
3. **Load fraction** $F_f/F_C = V_f E_f/E_{1C}$, from $F_C = F_f + F_m$ under a common strain [Session 22 Slide 21].
4. **Units.** The rules are linear, so they are applied in psi and converted at the end with 1 psi = 6894.757 Pa.

### Data
| Quantity | Fibre (carbon) | Matrix (epoxy) |
| :--- | ---: | ---: |
| $V$ | 0.64 | 0.36 |
| $E$ (psi) | $54.0\times10^6$ | $0.530\times10^6$ |
| $\sigma$ (psi) | $0.31\times10^6$ | $9.20\times10^3$ |

**Unknowns:** $E_{1C}$, $\sigma_C$ (psi), $F_f/F_C$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 21, 22, 26]:

$$E_{1C} = V_f E_f + V_m E_m \qquad \sigma_C = V_f\sigma_f + V_m\sigma_m \qquad \frac{F_f}{F_C} = \frac{V_f E_f}{E_{1C}}$$

**Strategy.** Apply the three relations in psi; convert the modulus and the strength to SI.

---

## 🔢 3. Step-by-Step Derivation

### 1. Tensile modulus [Session 22 Slide 22]

$$E_{1C} = 0.64 \times 54.0\times10^6 + 0.36 \times 0.530\times10^6 = 34.56\times10^6 + 0.191\times10^6 = \mathbf{34.75\times10^6\ psi}$$

In SI:

$$E_{1C} = 34.75\times10^6\ \text{psi} \times 6894.757\ \text{Pa/psi} = 239.6\times10^9\ \text{Pa} = \mathbf{239.6\ GPa}$$

### 2. Tensile strength [Session 22 Slide 26]

$$\sigma_C = 0.64 \times 0.31\times10^6 + 0.36 \times 9.20\times10^3 = 198\,400 + 3\,312 = \mathbf{201\,712\ psi}$$

$$\sigma_C = 201\,712\ \text{psi} \times 6894.757\ \text{Pa/psi} = 1.391\times10^9\ \text{Pa} = 1.39\ \text{GPa}$$

### 3. Fraction of the load carried by the fibres [Session 22 Slide 21]

$$\frac{F_f}{F_C} = \frac{0.64 \times 54.0\times10^6}{34.75\times10^6} = \frac{34.56}{34.75} = \mathbf{0.995}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** All moduli and strengths in psi, so the sums are in psi and the load fraction is dimensionless; the conversion factor has units Pa/psi.
- **Bounds.** $0.53\times10^6 < 34.75\times10^6 < 54.0\times10^6$ psi.
- **Approximation of the slides.** $E_{1C} \approx V_f E_f = 34.56\times10^6$ psi, 0.5 % below the full result, because $E_f/E_m \approx 100$ [Session 22 Slide 22].
- **Order of magnitude.** 240 GPa lies in the range of the unidirectional carbon-epoxy laminates of the slides (UD carbon-epoxy, 57 vol%: 134 GPa with a lower-modulus fibre, [Session 21 Slide 41]); the fibre modulus here, 372 GPa, is that of a high-modulus fibre [Session 21 Slide 22].

### Interpretation
With a fibre about 100 times stiffer than the matrix, 99.5 % of the load goes through the carbon. The matrix adds almost nothing to the stiffness or the strength; its role is to bond, protect and align the fibres and to transfer the load into them [Session 21 Slide 16].

> [!warning] Discrepancy with the official solution
> The key gives "a) 1.39 GPa" for the first question, the tensile modulus. The value 1.39 GPa is the **strength** of the composite: $201\,712\ \text{psi} \times 6894.757\ \text{Pa/psi} = 1.39$ GPa. The isostrain modulus from the data of the statement is $34.75\times10^6$ psi = 239.6 GPa, and the statement asks for the strength in psi (201 712 psi). The key's b) = 0.995 is the load fraction and agrees.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Modulus | (not given) | $34.75\times10^6$ psi = 239.6 GPa | the key's a) is the strength (see the warning) |
| Strength | 1.39 GPa (printed as a) | 201 712 psi = 1.39 GPa | agrees |
| Load fraction | 0.995 | 0.995 | agrees |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-04 Modulus Strength and Load Fraction of a Kevlar 49-Epoxy Composite|Problem T10-04]]
