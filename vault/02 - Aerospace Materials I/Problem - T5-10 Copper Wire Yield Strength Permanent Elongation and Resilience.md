---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 10"
dificultad: medium
badge: "Yield · unloading · resilience"
tags:
  - official-problem
  - solved
  - yield-strength
  - elastic-recovery
  - resilience
  - plastic-deformation
---

# ✏️ Problem: T5-10 — Copper Wire: Yield Strength, Permanent Elongation after Unloading and Resilience

## 📄 Official Statement
> 10. Plastic deformation in a copper wire of 200 cm in length and a diameter of 1 mm begins when it is loaded with 15.3 kg. If the elastic modulus for copper is 110 GPa.
>
> - a. Calculate its yield strength.
> - b. Considering that when it is loaded with 29.6 kg the strain is 0.011, calculate the final length of the wire once it has been unloaded.
> - c. Calculate the resilience modulus.
>
> *(Solution: a. $\sigma_y = 190.9$ MPa; b. $l = 201.85$ cm; c. $U_r = 0.165$ MPa)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Uniaxial, uniform stress** in the wire: $\sigma = F/A_0$ [Session 11 Slide 9]. The weight of a mass $m$ is $F = m\,g$ with $g = 9.81$ m/s².
2. **Yield strength.** "Plastic deformation begins when it is loaded with 15.3 kg" gives the yield strength, $\sigma_y = F_y/A_0$ [Session 11 Slide 28].
3. **Total strain under load.** The strain 0.011 of item b is the total strain (elastic plus plastic) measured while the load of 29.6 kg is applied, relative to the initial length: $\varepsilon = \Delta l/l_0$ [Session 11 Slide 9].
4. **Unloading is elastic.** When the load is removed the elastic strain is recovered along a line of slope $E$, parallel to the elastic line, starting from the stress that the wire carried; what remains is the plastic strain [Session 11 Slides 21 and 32].
5. **Resilience** of the elastic range: $U_r = \sigma_y^2/(2E)$ [Session 11 Slide 35].

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Length | $l_0$ | 200 cm | 2.000 m = 2000 mm |
| Diameter | $d_0$ | 1 mm | $1\times10^{-3}$ m |
| Young's modulus | $E$ | 110 GPa | 110 000 N/mm² |
| Mass at which plastic deformation begins | $m_1$ | 15.3 kg | $F_1 = 15.3\times9.81 = 150.09$ N |
| Mass of item b | $m_2$ | 29.6 kg | $F_2 = 29.6\times9.81 = 290.38$ N |
| Total strain under $m_2$ | $\varepsilon$ | 0.011 | 0.011 (dimensionless) |

**Unknowns:** $\sigma_y$ (a), the final length after unloading (b), $U_r$ (c).

---

## 🧠 2. Phase 2: Frames and Strategy

One direction (the axis of the wire); no change of basis.

**Strategy.** (a) is a stress: weight over area. (c) follows from (a) and $E$. Item (b) is the delicate one, and it is solved by following the strain along the load path:

1. The wire is loaded up to $\sigma_2 = F_2/A_0$, above the yield strength, and the total strain there is 0.011.
2. It is unloaded along a straight line of slope $E$: the strain recovered is $\sigma_2/E$ (the stress that it carried, not the yield strength).
3. The strain that remains is permanent, and it gives the final length.

![[attachments/T5/t5-p10-unloading.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Area of the wire
$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(1\ \text{mm})^2}{4} = 0.7854\ \text{mm}^2$$

### a) Yield strength
The force at which the plastic deformation begins is

$$F_1 = m_1\,g = 15.3\ \text{kg}\times9.81\ \text{m/s}^2 = 150.09\ \text{N}$$

$$\sigma_y = \frac{F_1}{A_0} = \frac{150.09\ \text{N}}{0.7854\ \text{mm}^2} = \mathbf{191.1\ MPa}$$

### b) Length after unloading
The stress under the load of 29.6 kg is

$$F_2 = 29.6\times9.81 = 290.38\ \text{N} \qquad \sigma_2 = \frac{290.38}{0.7854} = 369.7\ \text{MPa}$$

which is above the yield strength (93 % higher), so the wire is in the plastic zone and the total strain, $\varepsilon = 0.011$, is the sum of an elastic part and a plastic part, $\varepsilon = \varepsilon_e + \varepsilon_p$. On unloading, the elastic part is recovered along the line of slope $E$ that starts at $\sigma_2$:

$$\varepsilon_e = \frac{\sigma_2}{E} = \frac{369.7\ \text{N/mm}^2}{110000\ \text{N/mm}^2} = 3.3611\times 10^{-3}$$

The strain that remains is

$$\varepsilon_p = \varepsilon - \varepsilon_e = 0.011 - 3.3611\times 10^{-3} = 0.007639$$

and the final length, once unloaded, is

$$l_f = l_0\,(1 + \varepsilon_p) = 200\ \text{cm}\times(1 + 0.007639) = \mathbf{201.53\ cm}$$

(that is, the wire is left 1.53 cm longer than at the beginning).

### c) Modulus of resilience
$$U_r = \frac{\sigma_y^2}{2E} = \frac{(191.1\ \text{MPa})^2}{2\times110000\ \text{MPa}} = \mathbf{0.166\ MPa}$$

($1\ \text{MPa} = 1\ \text{MJ/m}^3$.)

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** kg·m/s² = N; N/mm² = MPa; the strains have no units; $l_f$ in the unit of $l_0$ (cm).
- **Order.** $\varepsilon_e = 3.3611\times 10^{-3} < \varepsilon = 0.011$, and $\varepsilon_p > 0$: the wire does not return to 200 cm. If the load were removed from the yield point, the permanent strain would be zero; here the wire has gone beyond it.
- **Elastic strain at yield.** The strain of the yield point, $\sigma_y/E = 0.001737$, is smaller than the elastic strain recovered from $\sigma_2$ ($3.3611\times 10^{-3}$): the unloading starts from a higher stress, and the recovery is larger.
- **Limits.** If $\sigma_2 = \sigma_y$ the wire would be exactly at the yield point and $\varepsilon_p$ would be (almost) zero; the larger the stress reached, the larger the elastic recovery and the permanent strain.

### Interpretation
The copper wire yields at about 191.1 MPa, and after being loaded to 369.7 MPa it keeps a permanent elongation of 1.53 cm in 200 cm. A load that goes beyond the yield strength leaves a trace: the length after unloading depends on how far the stress went.

> [!note] Value of $g$
> The key is consistent with $g = 9.8$ m/s², which gives $\sigma_y = 190.9$ MPa instead of 191.1 MPa ($0.1$ % difference) and $U_r = 0.1657$ MPa. The result here uses $g = 9.81$ m/s² throughout the sheet.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a. $\sigma_y$ | 190.9 MPa | 191.1 MPa | agrees (the key uses $g = 9.8$ m/s²) |
| b. final length | 201.85 cm | 201.53 cm | **does not agree**, see below |
| c. $U_r$ | 0.165 MPa | 0.166 MPa | agrees |

> [!warning] Discrepancy with the official solution: length after unloading
> The key, 201.85 cm, is obtained by recovering only the elastic strain of the yield point, $\sigma_y/E = 1.7373\times 10^{-3}$: $l = 200\,(1 + 0.011 - 1.7373\times 10^{-3}) = 201.85$ cm. That is the unloading of a wire that had been stressed to $\sigma_y$. But the wire of item b carried $\sigma_2 = 369.7$ MPa, and on unloading it recovers $\sigma_2/E = 3.3611\times 10^{-3}$. The correct permanent strain is therefore $0.007639$ and the length 201.53 cm. The key therefore recovers less elastic strain than the wire really does. The computed value is kept.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Yield Strength and the 0.2 Percent Offset]]
* [[Concept - Toughness and Modulus of Resilience]]
* [[Concept - Ductility - Percent Elongation and Reduction in Area]]
