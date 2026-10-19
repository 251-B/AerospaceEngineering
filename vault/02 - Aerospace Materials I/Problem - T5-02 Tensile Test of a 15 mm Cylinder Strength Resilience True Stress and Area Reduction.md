---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 2"
dificultad: medium
badge: "Tensile test · true stress · area reduction"
tags:
  - official-problem
  - solved
  - tensile-test
  - true-stress
  - ductility
  - reduction-of-area
---

# ✏️ Problem: T5-02 — Tensile Test of a 15 mm Cylinder: Strength, Resilience, True Stress and Area Reduction

## 📄 Official Statement
> 2. A cylindrical sample made from a metallic material (assume a Poisson ratio of ν = 0.25) of 15 mm in diameter and a calibrated length of 50 mm was subjected to a tensile test, and the results are shown in the table below:
>
> | Point | Force (kN) | ΔL (mm) |
> | ---: | ---: | ---: |
> | 1 | 70 | 0.25 |
> | 2 | 120 | 0.40 |
> | 3 | 150 | 0.50 |
> | 4 | 160 | 0.60 |
> | 5 | 170 | 0.75 |
> | 6 | 200 | 1.75 |
> | 7 | 220 | 3.00 |
> | 8 | 233 | 5.00 |
> | 9 | 233 | 6.50 |
> | 10 | 220 | 8.00 |
>
> The diameter of the sample after fracture was 12.45 mm. Calculate:
>
> - a. The tensile strength.
> - b. The Young's Modulus (or elastic modulus).
> - c. The yield stress.
> - d. The modulus of resilience.
> - e. The real tension for an engineering deformation of 0.02.
> - f. The percentage of deformation to fracture and percentage of area reduction.
>
> *(The sheet prints the table in two rows; here each point has its own row.)*
>
> *(Solution: a. $\sigma_{UTS} = 1319$ MPa; b. $E = 85$ GPa; c. $\sigma_y = 920$ MPa; d. $U_r = 4.98$ MPa; e. $\sigma_r = 1030$ MPa; f. 15 %, 7.3 %)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Uniaxial, uniform stress.** Up to the necking the stress is uniform along the gauge length, so the engineering quantities use the original area and length [Session 11 Slide 9].
2. **Linear elastic start.** Hooke's law $\sigma = E\varepsilon$ holds on the first points of the curve [Session 11 Slide 13].
3. **Yield strength by the 0.2 % offset.** The statement does not name a criterion; the conventional one for metals is the 0.2 % offset [Session 11 Slide 28].
4. **Straight segments between table rows**, so readings between two rows are linear interpolations.
5. **Uniform deformation before the necking.** The volume is constant, $A\,l = A_0 l_0$, until the maximum load, where the necking starts [Session 11 Slides 30 and 38]. The true stress of item e is computed in that range.
6. **Elastic recovery after the fracture.** The elastic strain disappears when the load does, and what is left is the plastic strain [Session 11 Slide 32]. The reduction of area uses the measured final diameter [Session 11 Slide 33].
7. **The Poisson ratio is not needed.** $\nu = 0.25$ is a datum of the statement, but none of the six items uses it: the only lateral information is the final diameter, which is measured.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Diameter | $d_0$ | 15 mm | $15\times10^{-3}$ m |
| Gauge length | $l_0$ | 50 mm | $50\times10^{-3}$ m |
| Diameter after fracture | $d_f$ | 12.45 mm | $12.45\times10^{-3}$ m |
| Poisson ratio (not used) | $\nu$ | 0.25 | |
| Load, elongation | $F$, $\Delta L$ | table | kN, mm |

**Unknowns:** $\sigma_{UTS}$ (a), $E$ (b), $\sigma_y$ (c), $U_r$ (d), $\sigma_r$ at $\varepsilon_n = 0.02$ (e), the elongation at fracture and the reduction of area (f).

---

## 🧠 2. Phase 2: Frames and Strategy

The only direction is the axis of the cylinder and the stress is uniaxial, so there is no change of basis.

**Strategy.** As in any tensile test, the first step is to turn the table into engineering stress and strain,

$$\sigma_n = \frac{F}{A_0} \qquad \varepsilon_n = \frac{\Delta L}{l_0}$$

and then read each item from it: the maximum stress (a), the slope of the straight part by least squares through the origin (b), the offset construction solved on the crossing segment (c), $U_r = \sigma_y^2/2E$ (d) [Session 11 Slide 35].

**True stress (e).** With constant volume, $A\,l = A_0 l_0$, so $A = A_0 l_0/l = A_0/(1 + \varepsilon_n)$. The true stress is then

$$\sigma_r = \frac{F}{A} = \frac{F}{A_0}\,(1 + \varepsilon_n) = \sigma_n\,(1 + \varepsilon_n)$$

which is the relation of the slide for the uniform deformation [Session 11 Slide 38].

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Cross-section
$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(15\ \text{mm})^2}{4}$$

The square is $15^2 = 225$, then $\pi\times225 = 706.86$ and dividing by 4:

$$A_0 = 176.71\ \text{mm}^2$$

### 2. Engineering stress and strain of every point
The loads are in kN, so $F = 1000\times F_{kN}$ newtons. For example, point 1 is $F = 70\,000$ N and $\Delta L = 0.25$ mm, so $\sigma_n = 70\,000/176.71 = 396.1$ MPa and $\varepsilon_n = 0.25/50 = 0.0050$. All the points:

| Point | $F$ (N) | $\Delta L$ (mm) | $\sigma_n$ (MPa) | $\varepsilon_n$ | $\sigma_n/\varepsilon_n$ (GPa) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 70 000 | 0.25 | 396.1 | 0.0050 | 79.2 |
| 2 | 120 000 | 0.40 | 679.1 | 0.0080 | 84.9 |
| 3 | 150 000 | 0.50 | 848.8 | 0.0100 | 84.9 |
| 4 | 160 000 | 0.60 | 905.4 | 0.0120 | 75.5 |
| 5 | 170 000 | 0.75 | 962.0 | 0.0150 | 64.1 |
| 6 | 200 000 | 1.75 | 1131.8 | 0.0350 | 32.3 |
| 7 | 220 000 | 3.00 | 1244.9 | 0.0600 | 20.7 |
| 8 | 233 000 | 5.00 | 1318.5 | 0.1000 | 13.2 |
| 9 | 233 000 | 6.50 | 1318.5 | 0.1300 | 10.1 |
| 10 | 220 000 | 8.00 | 1244.9 | 0.1600 | 7.8 |

![[attachments/T5/t5-p2-curve.svg]]

### a) Tensile strength
The maximum load is $F_{max} = 233\,000$ N, reached at points 8 and 9 ($\varepsilon_n = 0.100$ and $0.130$: the load stays at its maximum while the sample elongates). The area $A_0$ is constant in the engineering stress, so

$$\sigma_{UTS} = \frac{F_{max}}{A_0} = \frac{233\,000\ \text{N}}{176.71\ \text{mm}^2} = \mathbf{1318.5\ MPa}$$

### b) Young's modulus
The secant modulus is 79 to 85 GPa for points 1 to 3, and it drops to 75 GPa at point 4 and to 64 GPa at point 5: the linear zone ends after point 3. The fit through the origin with points 1 to 3 is:

| Point | $\varepsilon_i$ | $\sigma_i$ (MPa) | $\sigma_i\varepsilon_i$ (MPa) | $\varepsilon_i^2$ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.0050 | 396.1 | 1.9806 | $2.500\times 10^{-5}$ |
| 2 | 0.0080 | 679.1 | 5.4325 | $6.400\times 10^{-5}$ |
| 3 | 0.0100 | 848.8 | 8.4883 | $1.000\times 10^{-4}$ |

$$E = \frac{\sum \sigma_i\varepsilon_i}{\sum \varepsilon_i^2} = \frac{15.901}{1.8900\times 10^{-4}} = 84134\ \text{MPa} = \mathbf{84.1\ GPa}$$

### c) Yield stress (0.2 % offset)
The offset line is $\sigma_{off} = E(\varepsilon - 0.002)$ and the sign of $g = \sigma_n - E(\varepsilon_n - 0.002)$ tells where the curve crosses it. The sign changes between points 4 and 5:

| Point | $\varepsilon_n$ | $\sigma_n$ (MPa) | $E(\varepsilon_n - 0.002)$ (MPa) | $g = \sigma_n - E(\varepsilon_n - 0.002)$ (MPa) |
| --- | ---: | ---: | ---: | ---: |
| 3 | 0.01000 | 848.8 | 673.1 | 175.8 |
| 4 | 0.01200 | 905.4 | 841.3 | 64.1 |
| 5 | 0.01500 | 962.0 | 1093.7 | -131.7 |
| 6 | 0.03500 | 1131.8 | 2776.4 | -1644.7 |

On that segment

$$m = \frac{962.00 - 905.41}{0.01500 - 0.01200} = 18862.8\ \text{MPa} \qquad \varepsilon^* = \frac{\sigma_{4} - m\,\varepsilon_{4} + 0.002\,E}{E - m} = \frac{905.41 - 18862.8\times0.01200 + 0.002\times84134}{84134 - 18862.8} = \frac{847.329}{65271.3} = 0.0129817$$

$$\sigma_y = E\,(\varepsilon^* - 0.002) = 84134\times(0.0129817 - 0.002) = \mathbf{923.9\ MPa}$$

### d) Modulus of resilience
$$U_r = \frac{\sigma_y^2}{2E} = \frac{(923.9\ \text{MPa})^2}{2\times84134\ \text{MPa}} = \mathbf{5.07\ MPa}$$

($1\ \text{MPa} = 1\ \text{MJ/m}^3$.)

### e) True stress for $\varepsilon_n = 0.02$
The elongation that corresponds to $\varepsilon_n = 0.02$ is $\Delta L = 0.02\times50 = 1.00$ mm, which is not a row of the table. It is between points 5 ($\Delta L = 0.75$ mm, $F = 170$ kN) and 6 ($\Delta L = 1.75$ mm, $F = 200$ kN):

$$F = F_{5} + \frac{1.00 - 0.75}{1.75 - 0.75}\,(F_{6} - F_{5}) = 170 + \frac{1.00 - 0.75}{1.75 - 0.75}\,(200 - 170) = 177.5\ \text{kN}$$

$$\sigma_n = \frac{177\,500\ \text{N}}{176.71\ \text{mm}^2} = 1004.4\ \text{MPa}$$

This strain is below the one of the maximum load ($\varepsilon_n = 0.100$), so the deformation is still uniform and the relation of Phase 2 applies:

$$\sigma_r = \sigma_n\,(1 + \varepsilon_n) = 1004.4\times(1 + 0.02) = \mathbf{1024.5\ MPa}$$

### f) Elongation at fracture and reduction of area
The last row of the table is the fracture: $\Delta L = 8.00$ mm and $F = 220\,000$ N, so

$$\varepsilon_f = \frac{8.00}{50} = 0.160 \qquad \sigma_f = \frac{220\,000}{176.71} = 1244.9\ \text{MPa}$$

The elastic part of that strain is recovered when the sample breaks, $\varepsilon_e = \sigma_f/E$, and what is left is the plastic strain [Session 11 Slide 32]:

$$\varepsilon_e = \frac{1244.9}{84134} = 0.01480 \qquad \varepsilon_p = 0.160 - 0.01480 = 0.1452 \qquad EL = \mathbf{14.5\ \%}$$

For the reduction of area, the final area from the final diameter is

$$A_f = \frac{\pi\,(12.45\ \text{mm})^2}{4} = \frac{\pi\times155.0025}{4} = 121.74\ \text{mm}^2$$

$$RA\,(\%) = \frac{A_0 - A_f}{A_0}\times100 = \frac{176.71 - 121.74}{176.71}\times100 = \mathbf{31.1\ \%}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** Stresses in N/mm² = MPa, strains without units, $E$ and $U_r$ in MPa.
- **Order.** $\sigma_y = 923.9$ MPa $<\sigma_{UTS} = 1318.5$ MPa, and the stress rises 395 MPa between the yield and the maximum load.
- **True and engineering stress.** The true stress of item e, 1024.5 MPa, is 2 % above the engineering one, 1004.4 MPa, as the factor $1 + \varepsilon_n$ says.
- **Elongation against area reduction.** $RA = 31.1$ % is larger than $EL = 14.5$ %, as expected when a ductile sample necks: the section shrinks much more at the neck than the length grows over the whole gauge length.
- **Neck.** The stress that acts on the neck at the fracture is $F_f/A_f = 220\,000\ \text{N}/121.74\ \text{mm}^2 = 1807$ MPa, far above the engineering fracture stress of 1244.9 MPa because the area is much smaller than $A_0$.

### Interpretation
The sample reaches 1.3 GPa with a plateau of maximum load, and it fails after a clear neck. The measured final diameter, not Poisson's ratio, gives the lateral information: Poisson's ratio only describes the elastic part of the deformation.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a. $\sigma_{UTS}$ | 1319 MPa | 1318.5 MPa | agrees |
| b. $E$ | 85 GPa | 84.1 GPa | agrees (1 %); the key corresponds to the slope between points 2 and 3 |
| c. $\sigma_y$ | 920 MPa | 923.9 MPa | agrees (0.5 %) |
| d. $U_r$ | 4.98 MPa | 5.07 MPa | agrees (2 %); the key uses $E = 85$ GPa and $\sigma_y = 920$ MPa |
| e. $\sigma_r$ | 1030 MPa | 1024.5 MPa | agrees (0.5 %): the key reads $\sigma_n \approx 1010$ MPa at $\varepsilon_n = 0.02$ |
| f. elongation | 15 % | 14.5 % | agrees (rounded) |
| f. area reduction | 7.3 % | 31.1 % | **does not agree** |

> [!warning] Discrepancy with the official solution: area reduction
> The official 7.3 % cannot be reproduced from the data of the statement. With $d_0 = 15$ mm and $d_f = 12.45$ mm the final area is $A_f = 121.74$ mm² and the reduction is $31.1$ %. A reduction of 7.3 % would need a final area of $0.927\,A_0$, that is, a final diameter of $15\sqrt{0.927} = 14.44$ mm. The computed value is kept.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - True Stress and True Strain]]
* [[Concept - Ductility - Percent Elongation and Reduction in Area]]
* [[Concept - Tensile Strength, Necking and Fracture Stress]]
* [[Concept - Toughness and Modulus of Resilience]]
