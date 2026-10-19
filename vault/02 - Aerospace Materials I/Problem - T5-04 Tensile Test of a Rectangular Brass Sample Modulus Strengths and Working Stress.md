---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 4"
dificultad: hard
badge: "Tensile test · rectangular brass sample"
tags:
  - official-problem
  - solved
  - tensile-test
  - young-modulus
  - working-stress
  - measurement-resolution
---

# ✏️ Problem: T5-04 — Tensile Test of a Rectangular Brass Sample: Modulus, Strengths, Resilience and Working Stress

## 📄 Official Statement
> 4. A tensile test was performed on a brass sample with a rectangular section and dimensions of 3.2 mm x 19.1 mm. Using the data in the table below, answer the following questions:
>
> - a. Represent the data in terms of engineering stress versus strain.
> - b. Calculate the modulus of elasticity (Young's modulus).
> - c. Determine the yield strength.
> - d. Determine the tensile strength.
> - e. Calculate the modulus of resilience.
> - f. Calculate the working stress of this material.
>
> | Point | Load (N) | Length (mm) | σn (MPa) | εn |
> | ---: | ---: | ---: | ---: | ---: |
> | 0 | 0 | 63.50 |  |  |
> | 1 | 1 380 | 63.53 |  |  |
> | 2 | 2 780 | 63.58 |  |  |
> | 3 | 5 630 | 63.63 |  |  |
> | 4 | 7 430 | 63.70 |  |  |
> | 5 | 8 140 | 63.75 |  |  |
> | 6 | 9 870 | 64.14 |  |  |
> | 7 | 12 850 | 65.41 |  |  |
> | 8 | 14 100 | 66.68 |  |  |
> | 9 | 14 300 | 67.95 |  |  |
> | 10 | 13 830 | 69.22 |  |  |
> | 11 | 12 500 | 70.49 |  |  |
>
> *(The sheet prints the table in two rows, load and length, with two more rows, σn and εn, left blank to be completed. Point 0 is the unloaded sample.)*
>
> *(Solution: b. $E \approx 44$ GPa; c. $\sigma_y = 150$ MPa; d. $\sigma_{UTS} = 234$ MPa; e. $U_r = 0.28$ MPa; f. $\sigma_w = 75$ MPa)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Uniaxial, uniform stress.** The section is a rectangle $3.2\times19.1$ mm, and up to the necking the stress is uniform: $\sigma_n = F/A_0$ and $\varepsilon_n = (l - l_0)/l_0$ [Session 11 Slide 9].
2. **Initial length.** The first value of the length row, 63.50 mm (load 0), is $l_0$.
3. **Linear elastic start**, Hooke's law, with the slope fitted by least squares through the origin [Session 11 Slide 13].
4. **0.2 % offset yield strength** [Session 11 Slide 28].
5. **Working stress** $\sigma_w = \sigma_y/N$ with the usual $N = 2$, which the statement does not give [Session 11 Slide 29].
6. **Resolution of the length.** The length is given to 0.01 mm, so the first elongations (0.03 and 0.08 mm) carry an error of 10 to 30 % of their value. This matters for the modulus, and it is analysed in item b.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Section | $b\times h$ | $19.1\times3.2$ mm | $19.1\times10^{-3}\times3.2\times10^{-3}$ m |
| Initial length | $l_0$ | 63.50 mm | $63.50\times10^{-3}$ m |
| Load, length | $F$, $l$ | table | N, mm |
| Safety factor | $N$ | 2 | |

**Unknowns:** the curve (a), $E$ (b), $\sigma_y$ (c), $\sigma_{UTS}$ (d), $U_r$ (e), $\sigma_w$ (f).

---

## 🧠 2. Phase 2: Frames and Strategy

One direction (the axis of the sample), uniaxial stress, no change of basis.

**Strategy.** The table is turned into $\sigma_n$ and $\varepsilon_n$. Then $E$ is the least-squares slope through the origin of the straight part, $\sigma_y$ comes from the offset construction on the segment that crosses the offset line, $\sigma_{UTS}$ is the maximum load over $A_0$, $U_r = \sigma_y^2/(2E)$ [Session 11 Slide 35] and $\sigma_w = \sigma_y/N$. Since the first points of this table are not perfectly straight, the result is also shown for different choices of points, to see how much it depends on the choice.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Cross-section
$$A_0 = b\,h = 19.1\ \text{mm}\times3.2\ \text{mm} = 61.12\ \text{mm}^2$$

For point 1: $F_1 = 1\,380$ N and $l_1 = 63.53$ mm, so

$$\sigma_{n,1} = \frac{1\,380\ \text{N}}{61.12\ \text{mm}^2} = 22.58\ \text{MPa} \qquad \varepsilon_{n,1} = \frac{63.53 - 63.50}{63.50} = 0.00047$$

### a) Engineering stress and strain, and the curve
All the points:

| Point | $F$ (N) | $l$ (mm) | $\sigma_n$ (MPa) | $\varepsilon_n$ | $\sigma_n/\varepsilon_n$ (GPa) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 63.50 | 0 | 0.00000 | — |
| 1 | 1 380 | 63.53 | 22.58 | 0.00047 | 47.8 |
| 2 | 2 780 | 63.58 | 45.48 | 0.00126 | 36.1 |
| 3 | 5 630 | 63.63 | 92.11 | 0.00205 | 45.0 |
| 4 | 7 430 | 63.70 | 121.56 | 0.00315 | 38.6 |
| 5 | 8 140 | 63.75 | 133.18 | 0.00394 | 33.8 |
| 6 | 9 870 | 64.14 | 161.49 | 0.01008 | 16.0 |
| 7 | 12 850 | 65.41 | 210.24 | 0.03008 | 7.0 |
| 8 | 14 100 | 66.68 | 230.69 | 0.05008 | 4.6 |
| 9 | 14 300 | 67.95 | 233.97 | 0.07008 | 3.3 |
| 10 | 13 830 | 69.22 | 226.28 | 0.09008 | 2.5 |
| 11 | 12 500 | 70.49 | 204.52 | 0.11008 | 1.9 |

![[attachments/T5/t5-p4-curve.svg]]

### b) Modulus of elasticity
The secant modulus of the last column is 34 to 48 GPa for points 1 to 5 and falls to 16 GPa at point 6: the straight part ends after point 5. The scatter between 34 and 48 GPa comes from the resolution of the length: point 1 is an elongation of 0.03 mm, and an error of 0.01 mm is 33 % of it. A fit through the origin on points 1 to 5 weights the points by their strain, so the points with larger elongation, and smaller relative error, count more:

| Point | $\varepsilon_i$ | $\sigma_i$ (MPa) | $\sigma_i\varepsilon_i$ (MPa) | $\varepsilon_i^2$ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.00047 | 22.58 | 0.0107 | $2.232\times 10^{-7}$ |
| 2 | 0.00126 | 45.48 | 0.0573 | $1.587\times 10^{-6}$ |
| 3 | 0.00205 | 92.11 | 0.1886 | $4.191\times 10^{-6}$ |
| 4 | 0.00315 | 121.56 | 0.3829 | $9.920\times 10^{-6}$ |
| 5 | 0.00394 | 133.18 | 0.5243 | $1.550\times 10^{-5}$ |

$$E = \frac{\sum \sigma_i\varepsilon_i}{\sum \varepsilon_i^2} = \frac{1.164}{3.1422\times 10^{-5}} = 37037\ \text{MPa} = \mathbf{37.0\ GPa}$$

### c) Yield strength (0.2 % offset)
With the offset line $E(\varepsilon - 0.002)$ the sign of $g = \sigma_n - E(\varepsilon_n - 0.002)$ changes between points 5 and 6:

| Point | $\varepsilon_n$ | $\sigma_n$ (MPa) | $E(\varepsilon_n - 0.002)$ (MPa) | $g = \sigma_n - E(\varepsilon_n - 0.002)$ (MPa) |
| --- | ---: | ---: | ---: | ---: |
| 4 | 0.00315 | 121.6 | 42.6 | 79.0 |
| 5 | 0.00394 | 133.2 | 71.7 | 61.4 |
| 6 | 0.01008 | 161.5 | 299.2 | -137.7 |
| 7 | 0.03008 | 210.2 | 1040.0 | -829.7 |

$$m = \frac{161.49 - 133.18}{0.01008 - 0.00394} = 4608.6\ \text{MPa} \qquad \varepsilon^* = \frac{133.18 - 4608.6\times0.00394 + 0.002\times37037}{37037 - 4608.6} = \frac{189.110}{32428.3} = 0.0058316$$

$$\sigma_y = E\,(\varepsilon^* - 0.002) = 37037\times(0.0058316 - 0.002) = \mathbf{141.9\ MPa}$$

### d) Tensile strength
The maximum load is $F_{max} = 14\,300$ N (point 9):

$$\sigma_{UTS} = \frac{F_{max}}{A_0} = \frac{14\,300\ \text{N}}{61.12\ \text{mm}^2} = \mathbf{234.0\ MPa}$$

### e) Modulus of resilience
$$U_r = \frac{\sigma_y^2}{2E} = \frac{(141.9\ \text{MPa})^2}{2\times37037\ \text{MPa}} = \mathbf{0.272\ MPa}$$

### f) Working stress
$$\sigma_w = \frac{\sigma_y}{N} = \frac{141.9}{2} = \mathbf{71.0\ MPa}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** N/mm² is MPa, strains have no units, $E$ and $U_r$ are in MPa.
- **Order.** $\sigma_y = 141.9$ MPa $< \sigma_{UTS} = 234.0$ MPa; after the maximum the load falls (point 11 has 12 500 N), the sample necks.
- **Sensitivity to the points chosen for $E$.** The modulus, and through it $\sigma_y$ and $U_r$, depend on how many of the first points are taken:

| Points used for $E$ | $E$ (GPa) | $\sigma_y$ (MPa) | $U_r$ (MPa) | $\sigma_w$ (MPa) |
| --- | ---: | ---: | ---: | ---: |
| 1 to 3 | 42.7 | 139.3 | 0.227 | 69.6 |
| 1 to 4 | 40.2 | 140.4 | 0.245 | 70.2 |
| 1 to 5 | 37.0 | 141.9 | 0.272 | 71.0 |

  Between the three choices the yield strength changes by 1.9 % and $U_r$ by 20 % (because it contains $1/E$): the strengths hardly depend on the choice made for $E$, but the resilience does.

### Interpretation
The brass has a tensile strength of 234.0 MPa and a yield strength of about 141.9 MPa, and between the two the strain hardening adds 92 MPa. The large strain at fracture (11 % at the last point, after the maximum load) shows that it is ductile.

> [!warning] The modulus is much lower than the one of brass in the slide
> The table of Session 11 gives $E = 97$ GPa for brass [Session 11 Slide 17]. The data of this problem give 37 to 43 GPa, less than half. The key also gives 44 GPa, so the sheet itself uses these data. The reason is probably that the elongation of the table includes the slack and the compliance of the testing machine in the first points, which is why the elastic part looks softer than the real material. The data are used as they are.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| b. $E$ | $\approx 44$ GPa | 37.0 GPa | differs 16 %: see the sensitivity table; with points 1 to 3 the fit gives 42.7 GPa |
| c. $\sigma_y$ | 150 MPa | 141.9 MPa | differs 5 % |
| d. $\sigma_{UTS}$ | 234 MPa | 234.0 MPa | agrees |
| e. $U_r$ | 0.28 MPa | 0.272 MPa | agrees (3 %) |
| f. $\sigma_w$ | 75 MPa | 71.0 MPa | consistent with $\sigma_y$ |

> [!warning] Discrepancy with the official solution: modulus and yield strength
> The key gives $E \approx 44$ GPa and $\sigma_y = 150$ MPa. The 0.2 % offset on the data of the table gives $\sigma_y$ between 139 MPa ($E = 44$ GPa) and 142 MPa ($E = 37.0$ GPa), never 150 MPa. A yield strength of 150 MPa corresponds to the stress where the curve bends clearly (points 5 and 6, 133 to 161 MPa), that is, to a reading by eye of the end of the straight part. In addition, with the key values, $U_r = 150^2/(2\times44\,000) = 0.256$ MPa, not 0.28 MPa; the computed resilience, 0.272 MPa, is close to the printed one only by coincidence. The computed values are kept.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Hooke's Law, Young's Modulus and Non-Linear Elasticity]]
* [[Concept - Yield Strength and the 0.2 Percent Offset]]
* [[Concept - Working Stress and the Safety Factor]]
* [[Concept - Toughness and Modulus of Resilience]]
