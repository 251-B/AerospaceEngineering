---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 12"
dificultad: easy
badge: "Porosity · infiltration · density"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - porosity
  - infiltration
  - metal-matrix-composite
---

# ✏️ Problem: T10-12 — Density of a Porous Tungsten Matrix Infiltrated with Silver

## 📄 Official Statement
> 12. A tungsten matrix with 20% porosity is infiltrated with silver. Assuming that the pores are interconnected, what is the density of the composite before and after infiltration with silver? The density of pure tungsten is 19.25 g/cm³ and that of pure silver is 10.49 g/cm³.
>
> *(Solution 17.5g/cm³)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Porosity by volume.** 20 % of the volume of the tungsten body is pores, 80 % is solid tungsten.
2. **Empty pores before infiltration.** The air in the pores has negligible mass, so the pores add volume but no mass.
3. **Complete infiltration.** The pores are interconnected, so the liquid silver reaches all of them and fills the whole 20 % (the principle of liquid infiltration of a porous preform [Session 23 Slides 33-35]).
4. **Rule of mixtures** for the density, $\rho_c = \sum_i f_i\rho_i$ [Session 22 Slide 27], with a pore phase of zero density before infiltration.

### Data
| Constituent | Volume fraction | $\rho$ (g/cm³) |
| :--- | ---: | ---: |
| Tungsten | 0.80 | 19.25 |
| Pores / silver | 0.20 | 0 / 10.49 |

**Unknowns:** $\rho$ before and after infiltration.

---

## 🧠 2. Model and Strategy

[Session 22 Slide 27]:

$$\rho_{before} = f_W\rho_W + f_p \cdot 0 \qquad \rho_{after} = f_W\rho_W + f_p\rho_{Ag}$$

**Strategy.** Work with 1 cm³ of the body: tungsten mass plus the mass that fills the pores (none before, silver after).

---

## 🔢 3. Step-by-Step Derivation

### 1. Before infiltration [Session 22 Slide 27]

$$\rho_{before} = 0.80 \times 19.25\ \text{g/cm}^3 = \mathbf{15.40\ g/cm^3}$$

### 2. After infiltration [Session 22 Slide 27]

$$\rho_{after} = 0.80 \times 19.25 + 0.20 \times 10.49 = 15.40 + 2.098 = \mathbf{17.50\ g/cm^3}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** Volume fraction × g/cm³ = g/cm³.
- **Bounds.** $\rho_{Ag} = 10.49 < 17.50 < \rho_W = 19.25$ g/cm³: the infiltrated body is a two-phase mixture and lies between its phases.
- **Mass gained.** Each cm³ gains $0.20 \times 10.49 = 2.10$ g of silver, 13.6 % of the mass of the porous tungsten.
- **Limits.** Zero porosity gives pure tungsten (19.25 g/cm³); 100 % porosity filled with silver gives pure silver.

### Interpretation
The porous tungsten acts as a preform and the silver as the infiltrated phase, the route of the liquid-phase processing of metal matrix composites [Session 23 Slides 33-35]. The infiltration closes the porosity and raises the density by 2.1 g/cm³; if the pores were closed (not interconnected), the silver could not enter and the density would stay at 15.4 g/cm³.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Before infiltration | (not given) | 15.40 g/cm³ | the key gives only the value after infiltration |
| After infiltration | 17.5 g/cm³ | 17.50 g/cm³ | agrees |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-08 Boron-Aluminium Composite Density and Longitudinal and Transverse Moduli|Problem T10-08]]
