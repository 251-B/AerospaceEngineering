---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 2"
dificultad: medium
badge: "Material selection · modulus and strength limits"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - fibre-selection
  - composite-strength
---

# ✏️ Problem: T10-02 — Choosing the Fibre for an Epoxy Composite with 40 Percent Fibres

## 📄 Official Statement
> 2. A composite material is planned to be manufactured using an epoxy matrix reinforced with continuous, longitudinally aligned fibers . The composite must contain a maximum fiber volume fraction of 40%,, and the minimum values for the elastic modulus and longitudinal tensile strength are set at 5.5·10⁴ and 1.2·10³ MPa respectively. he available candidate reinforcement materials include glass fibers, carbon fibers, and aramid fibers. Determine which reinforcement material is best suited to meet the specified requirements.
>
> | Material | σ (MPa) | E (Gpa) |
> | :--- | ---: | ---: |
> | Epoxy Resin | 69 | 3.1 |
> | Fiberglass | 2000 | 72 |
> | Carbon Fiber | 3500 | 350 |
> | Aramid Fiber | 3500 | 124 |
>
> *(Solution: carbon fiber reinforced composite)*

The sheet prints "40%,," and "he available"; the requirement is $E_{1C} \ge 5.5\times10^4$ MPa = 55 GPa and $\sigma_{1C} \ge 1.2\times10^3$ MPa = 1200 MPa along the fibres.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Isostrain.** Continuous, aligned fibres loaded along their length with a perfect bond: $E_{1C} = V_f E_f + (1 - V_f)E_m$ [Session 22 Slide 22, Eq. 1].
2. **Longitudinal strength.** The strength follows the same rule of mixtures, $\sigma_C = \sigma_f V_f + \sigma_{y,m}(1 - V_f)$ [Session 22 Slide 26]. The table gives only one matrix stress (69 MPa), so it is used as the matrix term, as the key of the sheet does; the term is small next to the fibre term.
3. **Worst case.** Both properties grow with $V_f$, so if a fibre fails at the largest allowed fraction, $V_f = 0.40$, it fails at any lower fraction.

### Data
| Constituent | $\sigma$ (MPa) | $E$ (GPa) |
| :--- | ---: | ---: |
| Epoxy (m) | 69 | 3.1 |
| Glass fibre | 2000 | 72 |
| Carbon fibre | 3500 | 350 |
| Aramid fibre | 3500 | 124 |

Limits: $V_f \le 0.40$, $E_{1C} \ge 55$ GPa, $\sigma_{1C} \ge 1200$ MPa.

**Unknown:** the fibre that meets both limits.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 22, 26]:

$$E_{1C} = V_f E_f + (1 - V_f)E_m \qquad \sigma_{1C} = V_f\sigma_f + (1 - V_f)\sigma_m$$

**Strategy.**
1. Evaluate both properties for each fibre at $V_f = 0.40$ and compare them with the limits.
2. As a second view, solve each rule for the smallest $V_f$ that reaches the limit and compare it with 0.40.

---

## 🔢 3. Step-by-Step Derivation

### 1. Properties at the largest fraction, $V_f = 0.40$ [Session 22 Slides 22, 26]
The matrix terms are common to the three candidates: $0.60 \times 3.1\ \text{GPa} = 1.86$ GPa and $0.60 \times 69\ \text{MPa} = 41.4$ MPa.

Glass:

$$E_{1C} = 0.40 \times 72 + 1.86 = 30.66\ \text{GPa} \qquad \sigma_{1C} = 0.40 \times 2000 + 41.4 = 841.4\ \text{MPa}$$

Carbon:

$$E_{1C} = 0.40 \times 350 + 1.86 = 141.86\ \text{GPa} \qquad \sigma_{1C} = 0.40 \times 3500 + 41.4 = 1441.4\ \text{MPa}$$

Aramid:

$$E_{1C} = 0.40 \times 124 + 1.86 = 51.46\ \text{GPa} \qquad \sigma_{1C} = 0.40 \times 3500 + 41.4 = 1441.4\ \text{MPa}$$

| Fibre | $E_{1C}$ (GPa) | $\ge 55$? | $\sigma_{1C}$ (MPa) | $\ge 1200$? |
| :--- | ---: | :---: | ---: | :---: |
| Glass | 30.7 | no | 841 | no |
| Carbon | 141.9 | yes | 1441 | yes |
| Aramid | 51.5 | no | 1441 | yes |

### 2. Minimum fibre fraction for each limit
Solving $E_{1C} = 55$ GPa and $\sigma_{1C} = 1200$ MPa for $V_f$:

$$V_{f,E} = \frac{E_{min} - E_m}{E_f - E_m} \qquad V_{f,\sigma} = \frac{\sigma_{min} - \sigma_m}{\sigma_f - \sigma_m}$$

| Fibre | $V_{f,E}$ | $V_{f,\sigma}$ | Needed $V_f$ | $\le 0.40$? |
| :--- | ---: | ---: | ---: | :---: |
| Glass | $(55 - 3.1)/(72 - 3.1) = 0.753$ | $(1200 - 69)/(2000 - 69) = 0.586$ | 0.753 | no |
| Carbon | $(55 - 3.1)/(350 - 3.1) = 0.150$ | $(1200 - 69)/(3500 - 69) = 0.330$ | 0.330 | yes |
| Aramid | $(55 - 3.1)/(124 - 3.1) = 0.429$ | $(1200 - 69)/(3500 - 69) = 0.330$ | 0.429 | no |

**Answer: carbon fibre.** It is the only candidate that meets both limits with at most 40 vol% fibre; it needs only 33 vol% (set by the strength). Aramid meets the strength but misses the modulus by a small margin (it would need 42.9 vol%), and glass misses both.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** Each term of $E_{1C}$ is a fraction times a modulus (GPa) and each term of $\sigma_{1C}$ a fraction times a stress (MPa); the limits were converted to the same units (55 GPa, 1200 MPa).
- **Consistency.** The two methods agree: a fibre passes at $V_f = 0.40$ exactly when its needed $V_f$ is below 0.40.
- **Limit.** For $V_f \to 0$ both rules return the epoxy (3.1 GPa, 69 MPa), far below the limits: the matrix alone cannot do the job.

### Interpretation
Strength and stiffness select differently: aramid and carbon have the same tensile strength, but aramid is about three times less stiff, so the modulus limit is the one that rules it out. This matches the slides: glass fibres have a low modulus and aramid a lower modulus than carbon [Session 21 Slides 17, 30], and carbon fibres give the best combination of strength, stiffness and low weight [Session 21 Slide 21].

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Fibre | carbon fiber reinforced composite | carbon fibre ($E_{1C} = 141.9$ GPa, $\sigma_{1C} = 1441$ MPa at 40 vol%) | agrees |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-04 Modulus Strength and Load Fraction of a Kevlar 49-Epoxy Composite|Problem T10-04]]
