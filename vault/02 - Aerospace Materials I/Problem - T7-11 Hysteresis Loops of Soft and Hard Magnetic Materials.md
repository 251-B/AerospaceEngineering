---
materia: "Aerospace Materials I"
tema: "Topic 7: Magnetic and Thermal Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 11"
dificultad: medium
badge: "Soft and hard magnets · B-H loop"
tags:
  - official-problem
  - solved
  - hysteresis
  - soft-magnetic
  - hard-magnetic
  - coercivity
---

# ✏️ Problem: T7-11 — Hysteresis Loops of Soft and Hard Magnetic Materials

## 📄 Official Statement
> 11. Draw the hysteresis curve of a soft magnetic material and a hard magnetic material and indicated in both cases the most significant features. What are the main differences between these two materials?

The sheet prints no solution for this problem.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Saturated loop, quasi-static.** The loop is the one obtained by cycling the field slowly between $+H_{max}$ and $-H_{max}$, with $H_{max}$ large enough to reach saturation. The drawing is a schematic, as the statement asks for a sketch and gives no numbers.
2. **Features to indicate.** The features of the slides are the saturation induction $B_s$ (saturation magnetization $M_s$), the remanence $B_r$, the coercivity $H_c$ and the permeabilities $\mu_i$ and $\mu_{max}$ [Session 15 Slides 16-17].
3. **Soft and hard.** The two classes are separated by the coercivity, $H_c = 10\,000$ A/m [Session 15 Slide 18].
4. **Illustration with data.** The numbers come from the tables of Slide 24 of Session 15: Table 20-4 (soft materials, with $H_c$ in A/m) and Table 20-6 (hard materials, with $\mu_0 H_c$ in tesla). $\mu_0 = 1.257\times10^{-6}$ H/m [Session 15 Slide 4].

### Data
| Soft material | $\mu_{r,max}$ | $H_c$ in A/m | $B_r$ in T |
| :--- | ---: | ---: | ---: |
| Ingot iron (99.8 % Fe) | 5000 | 80 | 0.77 |
| Fe-3 % Si, grain-oriented | 50 000 | 7 | 1.20 |
| Superalloy (Fe-5 % Mo-80 % Ni) | 450 000 | 0.4 | not printed |

| Hard material | $\mu_0 M_r$ in T | $\mu_0 H_c$ in T |
| :--- | ---: | ---: |
| Co-steel (Fe-Co) | 1.07 | 0.02 |
| Alnico-5 (Fe-Co-Al-Ni) | 1.05 | 0.06 |
| Ferrite (BaFe₁₂O₁₉) | 0.42 | 0.31 |
| Sm-Co (SmCo₅) | 0.87 | 0.80 |
| Nd-Fe-B (Nd₂Fe₁₄B) | 1.23 | 1.21 |

**Unknown:** the two loops with their features, and the differences between the materials.

---

## 🧠 2. Model and Strategy

The loop comes from the motion of the Bloch walls. In a soft material the walls move easily, so a small field is enough to magnetize the material and to demagnetize it again. In a hard material the walls are difficult to move, so a large field is needed in both directions [Session 15 Slide 18].

![[attachments/T7/hysteresis-soft-hard.svg]]

**Strategy.**
1. Follow the loop step by step and mark where each feature appears.
2. Put numbers on the features with the tables of Slide 24, converting the hard-material coercivity to A/m so that both classes are compared with the same unit and with the limit of 10 000 A/m.
3. Compare the two classes feature by feature.

---

## 🔢 3. Step-by-Step Derivation

### 1. Path of the loop [Session 15 Slides 16-17]
- Starting from the demagnetized state ($H = 0$, domains at random) the initial curve rises to saturation: $B = B_s$.
- Reducing $H$ to zero does not bring $B$ back to zero: the induction left is the **remanence** $B_r$.
- A field in the opposite direction, of magnitude $H_c$, brings $B$ to zero: the **coercivity**.
- Going on to $-H_{max}$ gives $-B_s$, and the return branch is the mirror image through the origin.

The slope of the initial curve is the initial permeability $\mu_i$, and the line from the origin tangent to the curve gives the maximum permeability $\mu_{max}$.

### 2. Features on each loop
| Feature | Where | Soft material | Hard material |
| :--- | :--- | :--- | :--- |
| $\mu_i$, $\mu_{max}$ | slope of the initial curve | high | low $\mu_i$ |
| $H_c$ | crossing of the $H$ axis | low, below 10 000 A/m | high, above 10 000 A/m |
| $B_r$ | crossing of the $B$ axis | printed as a feature, not as a rule | high, printed on Slide 18 |
| $B_s$ | plateau | reached with a small field | reached only with a large field |
| Loop area | enclosed by the loop | small | large |

### 3. Hard-material coercivity in A/m
From $\mu_0 H_c$ in tesla, with $\mu_0 = 1.257\times10^{-6}$ H/m:

$$H_c = \frac{\mu_0 H_c}{\mu_0}$$

For Nd-Fe-B:

$$H_c = \frac{1.21\ \text{T}}{1.257\times10^{-6}\ \text{H/m}} = 9.626\times10^{5}\ \text{A/m}$$

The same division for the others:

| Hard material | $H_c$ in A/m | Above 10 000 A/m? |
| :--- | ---: | :--- |
| Co-steel | $1.59\times10^{4}$ | yes |
| Alnico-5 | $4.77\times10^{4}$ | yes |
| Ferrite | $2.47\times10^{5}$ | yes |
| Sm-Co | $6.36\times10^{5}$ | yes |
| Nd-Fe-B | $9.63\times10^{5}$ | yes |

Ratio of the strongest hard material to the soft ones of the table:

$$\frac{9.626\times10^{5}\ \text{A/m}}{80\ \text{A/m}} = 1.2\times10^{4} \qquad \frac{9.626\times10^{5}\ \text{A/m}}{7\ \text{A/m}} = 1.4\times10^{5}$$

### 4. Energy lost per cycle (extension, order of magnitude)
The energy dissipated per unit volume in one cycle is the area enclosed by the loop, $W = \oint H\,dB$ (this relation is not printed on the slides). For an idealized rectangular loop of width $2H_c$ and height $2B_r$ the area is

$$W \approx 2H_c \times 2B_r = 4\,H_c\,B_r$$

For the grain-oriented Fe-3 % Si and for Nd-Fe-B:

$$W_{soft} \approx 4\times7\ \text{A/m}\times1.20\ \text{T} = 33.6\ \text{J/m}^3 \qquad W_{hard} \approx 4\times9.626\times10^{5}\ \text{A/m}\times1.23\ \text{T} = 4.74\times10^{6}\ \text{J/m}^3$$

The ratio is about $1.4\times10^{5}$, the same as the ratio of coercivities, because the two remanences are similar. This is why the soft materials are the ones used under alternating fields, where the cycle repeats many times per second, and the hard ones are used as permanent magnets, where it never repeats [Session 15 Slides 18-19].

### 5. Main differences
| | Soft magnetic material | Hard magnetic material |
| :--- | :--- | :--- |
| Bloch walls | easy to move | difficult to move |
| Loop | narrow | wide |
| Coercivity | $H_c < 10\,000$ A/m | $H_c > 10\,000$ A/m |
| Permeability | high initial permeability | low initial permeability |
| Losses per cycle | low | high |
| Demagnetization | easy | resistant |
| Use | cores of transformers, generators and motors; materials under alternating fields | permanent magnets |

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units of $H_c$.** $[\mu_0 H_c]/[\mu_0] = \text{T}/(\text{H/m}) = (\text{Wb/m}^2)/(\text{Wb/(A}\cdot\text{m)}) = \text{A/m}$.
- **Units of the energy.** $[H\,B] = (\text{A/m})(\text{T}) = \text{A}\cdot\text{T/m}$, and with $\text{T} = \text{N/(A}\cdot\text{m)}$ this is $\text{N/m}^2 = \text{J/m}^3$, an energy per unit volume.
- **The limit of the slide.** All the soft materials of the table are below 10 000 A/m (the highest is 100 A/m for the low-carbon steel of Table 20-4) and all the hard ones above it. Co-steel, at $1.59\times10^{4}$ A/m, is the closest to the limit.
- **Limit $H_c \to 0$.** The loop collapses into a single line with no area and no loss, the ideal soft material. For a very large $H_c$ the loop is so wide that the material keeps its magnetization against the fields it meets in use, the ideal permanent magnet.

### Interpretation
The decisive difference is the coercivity, and everything else follows from the mobility of the Bloch walls: the width of the loop, the losses and the use. The remanence alone does not separate the classes. The grain-oriented Fe-3 % Si has $B_r = 1.20$ T, more than the ferrite magnet (0.42 T) and about the same as Nd-Fe-B (1.23 T). Slide 18 lists a high remanence among the properties of the hard materials; in the data of Slide 24 it is the coercivity that is orders of magnitude apart ($7$ to $100$ A/m against $10^4$ to $10^6$ A/m), not the remanence.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Loops and features | not printed on the sheet | $B_s$, $B_r$, $H_c$, $\mu_i$, $\mu_{max}$ on both loops | consistent with Session 15 Slides 16-18 |
| Differences | not printed on the sheet | coercivity, loop width, permeability, losses and use | consistent with Session 15 Slides 18-19; the energy per cycle and the numbers of Slide 24 are an extension |

## 🔗 Related Links
* [[Topic 7 - Magnetic and Thermal Properties]]
