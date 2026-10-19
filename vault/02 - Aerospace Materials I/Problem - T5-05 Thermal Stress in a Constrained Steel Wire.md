---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 5"
dificultad: medium
badge: "Thermal stress · constant length"
tags:
  - official-problem
  - solved
  - thermal-stress
  - hooke-law
  - thermal-expansion
---

# ✏️ Problem: T5-05 — Thermal Stress in a Constrained Steel Wire: the Diameter that Cancels the Applied Stress

## 📄 Official Statement
> 5. A steel wire, initially 1 meter in length, is stretched by a force of 1400 N at a temperature of 20 ºC. After the force is applied, the wire is held at a constant length and then heated to 40 ºC. Determine the required diameter of the wire to ensure that the thermal expansion stress compensates for the applied stress.
> >
> > Data: E = 207 GPa; $\alpha_l = 12.5\times10^{-6}$ ºC⁻¹;
>
> *(Solution: 5.86 mm)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Uniaxial, linear elastic wire.** The wire is loaded only along its axis and it stays elastic, so $\sigma = E\varepsilon$ [Session 11 Slide 13].
2. **Constant length while heating.** After the force is applied, the wire is held at a constant length: the total length, and therefore the total strain $\varepsilon$, does not change during the heating.
3. **Linear thermal expansion.** A temperature rise $\Delta T$ produces a free thermal strain $\varepsilon_T = \alpha_l\,\Delta T$. This law is not in the slides of Session 11 and 12 (it belongs to the thermal properties of Topic 7); it is given by the sheet through the datum $\alpha_l$.
4. **Strains add.** The total strain is the elastic (mechanical) strain plus the thermal strain, $\varepsilon = \sigma/E + \alpha_l\,\Delta T$, and $E$ and $\alpha_l$ are constant between 20 and 40 °C.
5. **"Compensates".** The thermal stress compensates the applied stress when the net stress of the wire after heating is zero.
6. **Circular, uniform section.** The area $A = \pi d^2/4$ is the same all along the wire and does not change with the temperature.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Force | $F$ | 1400 N | 1400 N |
| Initial temperature, final temperature | $T_1$, $T_2$ | 20 °C, 40 °C | |
| Temperature rise | $\Delta T$ | 20 °C | 20 K |
| Young's modulus | $E$ | 207 GPa | $207\times10^{9}$ Pa = 207 000 N/mm² |
| Linear expansion coefficient | $\alpha_l$ | $12.5\times10^{-6}$ °C⁻¹ | $12.5\times10^{-6}$ K⁻¹ |
| Initial length | $l_0$ | 1 m | not needed |

**Unknown:** the diameter $d$ of the wire.

---

## 🧠 2. Phase 2: Frames and Strategy

There is a single direction, the axis of the wire; no change of basis is involved.

![[attachments/T5/t5-p5-wire.svg]]

**Strategy.** The key is to follow the strain, because the length is the quantity that is fixed.

1. At 20 °C the force produces the stress $\sigma_F = F/A$ and the strain $\varepsilon_1 = \sigma_F/E$.
2. At 40 °C the strain is the same, $\varepsilon_2 = \varepsilon_1$, but it is now the sum of an elastic part $\sigma_2/E$ and a thermal part $\alpha_l\Delta T$. This gives the stress after the heating, $\sigma_2$.
3. The condition of the statement, $\sigma_2 = 0$, gives the area, and the area gives the diameter.

This is better than thinking in terms of forces, because the wire does not "know" about the force: it only keeps its length, and the stress is whatever is needed to keep it.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Stress after heating at constant length
Before heating, the strain is $\varepsilon_1 = \sigma_F/E$ with $\sigma_F = F/A$. After heating, the strain is the same, and it is the sum of the elastic and the thermal strain:

$$\varepsilon_2 = \frac{\sigma_2}{E} + \alpha_l\,\Delta T = \varepsilon_1 = \frac{\sigma_F}{E}$$

Solving for the stress after the heating:

$$\sigma_2 = \sigma_F - E\,\alpha_l\,\Delta T$$

The second term is the thermal stress: heating at constant length lowers the tension by $E\alpha_l\Delta T$ (if it were larger than $\sigma_F$, $\sigma_2$ would be negative, a compression).

### 2. Condition of the statement
The thermal stress compensates the applied stress when the net stress vanishes, $\sigma_2 = 0$:

$$\frac{F}{A} = E\,\alpha_l\,\Delta T \quad\Rightarrow\quad A = \frac{F}{E\,\alpha_l\,\Delta T}$$

### 3. Numerical value of the thermal stress
With $E = 207000$ N/mm²:

$$E\,\alpha_l = 207000\ \frac{\text{N}}{\text{mm}^2}\times12.5\times10^{-6}\ \text{°C}^{-1} = 2.5875\ \frac{\text{N}}{\text{mm}^2\,\text{°C}}$$

$$E\,\alpha_l\,\Delta T = 2.5875\times20\ \text{°C} = 51.75\ \text{N/mm}^2 = 51.75\ \text{MPa}$$

### 4. Area and diameter
$$A = \frac{F}{E\alpha_l\Delta T} = \frac{1400\ \text{N}}{51.75\ \text{N/mm}^2} = 27.053\ \text{mm}^2$$

From $A = \pi d^2/4$, $d = \sqrt{4A/\pi}$:

$$4A = 108.21\ \text{mm}^2 \qquad \frac{4A}{\pi} = 34.445\ \text{mm}^2 \qquad d = \sqrt{34.445\ \text{mm}^2} = \mathbf{5.869\ mm}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $F/(E\alpha_l\Delta T)$: N divided by (N/mm² · °C⁻¹ · °C) = N/(N/mm²) = mm². The product $\alpha_l\Delta T$ has no units, so $E\alpha_l\Delta T$ is a stress.
- **Direct check.** With this area the applied stress is $F/A = 1400/27.053 = 51.75$ MPa, equal to the thermal stress 51.75 MPa, so $\sigma_2 = 0$.
- **Strains.** The thermal strain $\alpha_l\Delta T = 2.500\times 10^{-4}$ is the same as the elastic strain that the force produced, $\sigma_F/E = 2.500\times 10^{-4}$: heating gives back exactly the stretch that the force had imposed, and since the length cannot change the stress disappears.
- **Length not needed.** The initial length does not appear in the result. The free expansion of 1 m of wire would be $\alpha_l\Delta T\,l_0 = 0.25$ mm, the amount that the supports prevent.

### Interpretation
For a wire thinner than 5.87 mm the applied stress is larger than the thermal one, and some tension remains after the heating. For a thicker wire the applied stress is smaller, and the heating leaves the wire in compression (it could buckle). The result depends on $F/A$, not on the length, because only the strain matters. As $\Delta T \to 0$ the required area tends to infinity: without temperature rise the force cannot be compensated.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Diameter | 5.86 mm | 5.869 mm | agrees (0.15 %): the key is truncated, 5.869 rounds to 5.87 |

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Hooke's Law, Young's Modulus and Non-Linear Elasticity]]
