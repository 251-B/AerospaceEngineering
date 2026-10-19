---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 6"
dificultad: easy
badge: "Hooke's law · design"
tags:
  - official-problem
  - solved
  - hooke-law
  - elastic-modulus
  - design
---

# ✏️ Problem: T5-06 — Maximum Length of a Ni Alloy Sample for a Given Allowed Elongation

## 📄 Official Statement
> 6. A sample made of a Ni alloy with an elastic modulus of 207 GPa and an initial diameter of 10.2 mm experiences an elastic deformation only when loads inferior to 8900 N are applied. Calculate the maximum length of the sample before the deformation if the maximum elongation allowed is 0.25 mm.
>
> *(Solution: $l_0 = 475$ mm)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Elastic up to 8900 N.** For loads below 8900 N the deformation is only elastic, so Hooke's law $\sigma = E\varepsilon$ holds [Session 11 Slide 13]. The load of 8900 N is therefore the largest load for which the sample is still elastic.
2. **Uniaxial, uniform stress** along the sample: $\sigma = F/A_0$ and $\varepsilon = \Delta l/l_0$ [Session 11 Slide 9].
3. **Worst case.** The elongation grows with the load and with the length. The longest sample that does not exceed the allowed elongation is found for the largest load that is applied, 8900 N.
4. The cross-section is a circle of 10.2 mm, and it does not change appreciably in the elastic range.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Young's modulus | $E$ | 207 GPa | 207 000 N/mm² |
| Diameter | $d_0$ | 10.2 mm | $10.2\times10^{-3}$ m |
| Largest elastic load | $F$ | 8900 N | 8900 N |
| Maximum elongation allowed | $\Delta l_{max}$ | 0.25 mm | $0.25\times10^{-3}$ m |

**Unknown:** the maximum initial length $l_0$.

---

## 🧠 2. Phase 2: Frames and Strategy

One direction (the axis of the sample), no change of basis.

**Strategy.** Hooke's law relates the stress produced by the load to the strain, and the strain relates the elongation to the length. Combining the three relations,

$$\sigma = \frac{F}{A_0} \qquad \varepsilon = \frac{\sigma}{E} \qquad \Delta l = \varepsilon\,l_0$$

the elongation is proportional to the initial length. The condition $\Delta l \leq 0.25$ mm is then an upper bound for $l_0$, and the maximum length is the one for which $\Delta l = 0.25$ mm.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Area
$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(10.2\ \text{mm})^2}{4}$$

The square is $10.2^2 = 104.04$, then $\pi\times104.04 = 326.85$ and dividing by 4:

$$A_0 = 81.71\ \text{mm}^2$$

### 2. Stress and strain at the largest elastic load
$$\sigma = \frac{F}{A_0} = \frac{8900\ \text{N}}{81.71\ \text{mm}^2} = 108.92\ \text{MPa}$$

$$\varepsilon = \frac{\sigma}{E} = \frac{108.92\ \text{N/mm}^2}{207000\ \text{N/mm}^2} = 5.2617\times 10^{-4}$$

### 3. Maximum initial length
From $\Delta l = \varepsilon\,l_0$ with $\Delta l = 0.25$ mm:

$$l_0 = \frac{\Delta l}{\varepsilon} = \frac{0.25\ \text{mm}}{5.2617\times 10^{-4}} = \mathbf{475.1\ mm}$$

The same result in one step, without the intermediate strain:

$$l_0 = \frac{\Delta l\,A_0\,E}{F} = \frac{0.25\ \text{mm}\times81.71\ \text{mm}^2\times207000\ \text{N/mm}^2}{8900\ \text{N}} = 475.1\ \text{mm}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $\Delta l\,A_0E/F$: mm · mm² · (N/mm²) / N = mm.
- **Back substitution.** For $l_0 = 475.1$ mm, $\Delta l = 5.2617\times 10^{-4}\times475.1 = 0.250$ mm, the allowed elongation.
- **Elastic range.** The strain, $5.2617\times 10^{-4}$, is of the order of $10^{-4}$, typical of the elastic deformation of a metal, so the use of Hooke's law is consistent with the statement.
- **Limit.** For a shorter sample the elongation is smaller (it is proportional to $l_0$) and the condition is satisfied with margin; for a longer one it is exceeded.

### Interpretation
The sample can be at most about 475 mm long. The limit is imposed by the stiffness $E$ (a stiff material elongates little) and by the section (a thicker sample has less stress for the same load); it is not imposed by the strength, because the stress stays elastic.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $l_0$ | 475 mm | 475.1 mm | agrees |

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Hooke's Law, Young's Modulus and Non-Linear Elasticity]]
* [[Concept - Uniaxial Tension Test and Engineering Stress-Strain]]
