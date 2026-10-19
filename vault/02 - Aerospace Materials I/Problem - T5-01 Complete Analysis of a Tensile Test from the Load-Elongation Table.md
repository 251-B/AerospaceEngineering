---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 1"
dificultad: medium
badge: "Tensile test · full stress-strain analysis"
tags:
  - official-problem
  - solved
  - tensile-test
  - young-modulus
  - yield-strength
  - ductility
  - resilience
---

# ✏️ Problem: T5-01 — Complete Analysis of a Tensile Test from the Load-Elongation Table

## 📄 Official Statement
> 1. A cylindrical aluminum sample has a diameter of 12.8 mm and an initial base length of 12.5 mm and it is subjected to uniaxial tension. Use the data from the load/elongation table to answer the following questions:
>
> - a. Represent the engineering stress data versus the engineering strain.
> - b. Calculate Young's modulus.
> - c. Calculate the yield strength, assuming that the residual strain at the yield point is 0.002.
> - d. Work out the tensile strength of this alloy.
> - e. Determine the approximate value of ductility expressed as a deformation percentage.
> - f. Determine the approximate value of the modulus of resilience.
> - g. Calculate the load (N) and the elongation (mm) of the sample at the yield point.
> - h. Calculate an approximate working stress for this material.
> - i. With the values obtained, is it possible to calculate the load applied to the sample if the elongation produced is 0.1 mm? If it is possible, work it out and if it is not possible, explain your answer and provide an alternative method.
>
> | Point | F (N/100) | ΔL (mm) |
> | ---: | ---: | ---: |
> | 1 | 127 | 0.006 |
> | 2 | 254 | 0.012 |
> | 3 | 381 | 0.019 |
> | 4 | 508 | 0.025 |
> | 5 | 762 | 0.038 |
> | 6 | 891 | 0.051 |
> | 7 | 927 | 0.063 |
> | 8 | 1025 | 0.095 |
> | 9 | 1078 | 0.127 |
> | 10 | 1194 | 0.190 |
> | 11 | 1283 | 0.254 |
> | 12 | 1497 | 0.508 |
> | 13 | 1590 | 0.762 |
> | 14 | 1604 | 0.889 |
> | 15 | 1595 | 1.016 |
> | 16 | 1515 | 1.270 |
> | 17 | 1247 | 1.460 |
>
> *(The sheet prints the table in two rows, F and ΔL, followed by the word "Fracture"; here each point has its own row. Point 17 is the last record before the fracture.)*
>
> *(Solution: b. $E \approx 200$ GPa; c. $\sigma_y = 740$ MPa; d. $\sigma_{max} = 1250$ MPa; e. 11.3 %; f. $U_r = 1.37$ MPa; g. $F = 9.5\times10^4$ N, $\Delta l = 0.071$ mm; h. $\sigma_w = 370$ MPa; i. it can only be obtained graphically, $F = 10.3\times10^4$ N)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Uniaxial, uniform stress.** The load acts along the axis of the cylinder, and up to the necking the stress is the same on every cross-section of the gauge length. Under this hypothesis the engineering stress and strain are defined with the original area and length [Session 11 Slide 9].
2. **Linear elastic start.** For small loads the curve is a straight line through the origin, Hooke's law $\sigma = E\varepsilon$, and the slope of that line is the Young's modulus [Session 11 Slide 13].
3. **Conventional yield strength.** The yield strength is the stress at which the curve crosses the line drawn parallel to the elastic line from the residual strain $0.002$ (0.2 % offset), as the statement asks [Session 11 Slide 28].
4. **Between table rows the curve is a straight segment.** The table gives discrete points, so every reading between two of them is a linear interpolation.
5. **Elastic recovery.** When the sample breaks the load disappears and the elastic strain is recovered, so the ductility is the plastic strain at fracture [Session 11 Slide 32].
6. **Safety factor.** The statement gives none; the slide says that $N$ is usually 2, and that value is used for the working stress [Session 11 Slide 29].

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Diameter | $d_0$ | 12.8 mm | $12.8\times10^{-3}$ m |
| Initial gauge length | $l_0$ | 12.5 mm | $12.5\times10^{-3}$ m |
| Load (table) | $F$ | $100 \times (F/100)$ | N |
| Elongation (table) | $\Delta L$ | see table | mm |
| Safety factor | $N$ | 2 | |

**Unknowns:** the curve (a), $E$ (b), $\sigma_y$ (c), $\sigma_{max}$ (d), the ductility (e), $U_r$ (f), $F_y$ and $\Delta l_y$ (g), $\sigma_w$ (h), and the load at $\Delta L = 0.1$ mm (i).

---

## 🧠 2. Phase 2: Frames and Strategy

There is a single direction, the axis of the sample, and the stress state is uniaxial, so no change of basis and no rotation matrix are involved.

**Strategy.** Every item comes from the same table of engineering stress and strain, so the first thing to do is to build it:

$$\sigma_n = \frac{F}{A_0} \qquad \varepsilon_n = \frac{\Delta L}{l_0}$$

- The Young's modulus is the slope of the straight initial part (Hooke's law). A straight line through the origin is fitted by least squares: it minimises $\sum(\sigma_i - E\varepsilon_i)^2$, which gives $E = \sum\sigma_i\varepsilon_i / \sum\varepsilon_i^2$.
- The yield strength is found by the 0.2 % offset construction, solved algebraically on the segment of the table where the curve crosses the offset line.
- The tensile strength is the maximum nominal stress, and since $A_0$ is constant it corresponds to the maximum load.
- The ductility is the plastic strain at fracture, and the modulus of resilience is the area under the elastic line up to the yield point, $U_r = \sigma_y^2/(2E)$ [Session 11 Slide 35].
- For the load at a given elongation the table is used again: Hooke's law only holds in the elastic zone.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Cross-section
$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(12.8\ \text{mm})^2}{4}$$

The square is $12.8^2 = 163.84$, then $\pi \times 163.84 = 514.72$ and dividing by 4:

$$A_0 = 128.68\ \text{mm}^2 = 1.2868\times 10^{-4}\ \text{m}^2$$

### 2. Engineering stress and strain of every point
The load of the table is in hundreds of newtons, so $F = 100\times(F/100)$. For point 1:

$$F_1 = 100 \times 127 = 12\,700\ \text{N} \qquad \sigma_{n,1} = \frac{12\,700\ \text{N}}{128.68\ \text{mm}^2} = 98.69\ \text{MPa} \qquad \varepsilon_{n,1} = \frac{0.006\ \text{mm}}{12.5\ \text{mm}} = 4.80\times 10^{-4}$$

The same operation for all the points (the last column is the secant modulus, used in item b):

| Point | $F$ (N) | $\Delta L$ (mm) | $\sigma_n$ (MPa) | $\varepsilon_n$ | $\sigma_n/\varepsilon_n$ (GPa) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 12 700 | 0.006 | 98.69 | 0.00048 | 205.6 |
| 2 | 25 400 | 0.012 | 197.39 | 0.00096 | 205.6 |
| 3 | 38 100 | 0.019 | 296.08 | 0.00152 | 194.8 |
| 4 | 50 800 | 0.025 | 394.78 | 0.00200 | 197.4 |
| 5 | 76 200 | 0.038 | 592.17 | 0.00304 | 194.8 |
| 6 | 89 100 | 0.051 | 692.42 | 0.00408 | 169.7 |
| 7 | 92 700 | 0.063 | 720.39 | 0.00504 | 142.9 |
| 8 | 102 500 | 0.095 | 796.55 | 0.00760 | 104.8 |
| 9 | 107 800 | 0.127 | 837.74 | 0.01016 | 82.5 |
| 10 | 119 400 | 0.190 | 927.89 | 0.01520 | 61.0 |
| 11 | 128 300 | 0.254 | 997.05 | 0.02032 | 49.1 |
| 12 | 149 700 | 0.508 | 1163.35 | 0.04064 | 28.6 |
| 13 | 159 000 | 0.762 | 1235.63 | 0.06096 | 20.3 |
| 14 | 160 400 | 0.889 | 1246.51 | 0.07112 | 17.5 |
| 15 | 159 500 | 1.016 | 1239.51 | 0.08128 | 15.2 |
| 16 | 151 500 | 1.270 | 1177.34 | 0.10160 | 11.6 |
| 17 | 124 700 | 1.460 | 969.07 | 0.11680 | 8.3 |

### a) Stress-strain curve
The points of the table are plotted as they are, joined by straight segments. The right-hand panel enlarges the elastic part, where the Young's modulus line and the offset line of item c are drawn.

![[attachments/T5/t5-p1-curve.svg]]

### b) Young's modulus
The secant modulus $\sigma_n/\varepsilon_n$ of the last column is almost constant, 195 to 206 GPa, for points 1 to 5, and it drops to 170 GPa at point 6 and to 143 GPa at point 7: the specimen leaves the linear zone after point 5. The straight part is therefore made of points 1 to 5, and the fit through the origin is:

| Point | $\varepsilon_i$ | $\sigma_i$ (MPa) | $\sigma_i\varepsilon_i$ (MPa) | $\varepsilon_i^2$ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.00048 | 98.69 | 0.0474 | $2.304\times 10^{-7}$ |
| 2 | 0.00096 | 197.39 | 0.1895 | $9.216\times 10^{-7}$ |
| 3 | 0.00152 | 296.08 | 0.4500 | $2.310\times 10^{-6}$ |
| 4 | 0.00200 | 394.78 | 0.7896 | $4.000\times 10^{-6}$ |
| 5 | 0.00304 | 592.17 | 1.8002 | $9.242\times 10^{-6}$ |

$$\sum \sigma_i\varepsilon_i = 3.277\ \text{MPa} \qquad \sum \varepsilon_i^2 = 1.6704\times 10^{-5}$$

$$E = \frac{\sum \sigma_i\varepsilon_i}{\sum \varepsilon_i^2} = \frac{3.277}{1.6704\times 10^{-5}} = 196160\ \text{MPa} = \mathbf{196.2\ GPa} \approx 2.0\times10^{2}\ \text{GPa}$$

### c) Yield strength (0.2 % offset)
The offset line starts at $\varepsilon = 0.002$ and is parallel to the elastic line:

$$\sigma_{off}(\varepsilon) = E\,(\varepsilon - 0.002)$$

The curve is above the line while $g = \sigma_n - E(\varepsilon_n - 0.002)$ is positive. The sign of $g$ changes between points 7 and 8, so the crossing is on that segment:

| Point | $\varepsilon_n$ | $\sigma_n$ (MPa) | $E(\varepsilon_n - 0.002)$ (MPa) | $g = \sigma_n - E(\varepsilon_n - 0.002)$ (MPa) |
| --- | ---: | ---: | ---: | ---: |
| 6 | 0.00408 | 692.4 | 408.0 | 284.4 |
| 7 | 0.00504 | 720.4 | 596.3 | 124.1 |
| 8 | 0.00760 | 796.6 | 1098.5 | -301.9 |
| 9 | 0.01016 | 837.7 | 1600.7 | -762.9 |

The segment between the two points is the line

$$\sigma(\varepsilon) = \sigma_{7} + m\,(\varepsilon - \varepsilon_{7}) \qquad m = \frac{\sigma_{8} - \sigma_{7}}{\varepsilon_{8} - \varepsilon_{7}} = \frac{796.55 - 720.39}{0.00760 - 0.00504} = 29749.3\ \text{MPa}$$

Equating it to the offset line, $\sigma_{7} + m(\varepsilon - \varepsilon_{7}) = E(\varepsilon - 0.002)$, and solving for $\varepsilon$:

$$\varepsilon^* = \frac{\sigma_{7} - m\,\varepsilon_{7} + 0.002\,E}{E - m} = \frac{720.39 - 29749.3\times0.00504 + 0.002\times196160}{196160 - 29749.3} = \frac{962.778}{166411.2} = 0.0057855$$

$$\sigma_y = E\,(\varepsilon^* - 0.002) = 196160\times(0.0057855 - 0.002) = \mathbf{742.6\ MPa}$$

### d) Tensile strength
The maximum load of the table is $F_{max} = 160\,400$ N at point 14. The nominal stress uses the original area, so the maximum load gives the maximum stress:

$$\sigma_{max} = \frac{F_{max}}{A_0} = \frac{160\,400\ \text{N}}{128.68\ \text{mm}^2} = \mathbf{1246.5\ MPa}$$

### e) Ductility
The last record before the fracture is point 17: $\Delta L = 1.460$ mm and $F = 124\,700$ N, so

$$\varepsilon_f = \frac{1.460}{12.5} = 0.1168 \qquad \sigma_f = \frac{124\,700}{128.68} = 969.1\ \text{MPa}$$

At that moment the strain is the sum of an elastic and a plastic part, $\varepsilon_t = \varepsilon_e + \varepsilon_p$. After the fracture the load is zero and the elastic part is recovered along a line parallel to the elastic one, so what remains is $\varepsilon_p$ [Session 11 Slide 32]:

$$\varepsilon_e = \frac{\sigma_f}{E} = \frac{969.1}{196160} = 0.00494 \qquad \varepsilon_p = \varepsilon_f - \varepsilon_e = 0.1168 - 0.00494 = 0.1119$$

$$EL\,(\%) = \varepsilon_p \times 100 = \mathbf{11.2\ \%}$$

### f) Modulus of resilience
The area under the elastic line up to the yield point is a triangle, $U_r = \tfrac12\sigma_y\varepsilon_{y}$ with $\varepsilon_{y} = \sigma_y/E$ [Session 11 Slide 35]:

$$U_r = \frac{\sigma_y^2}{2E} = \frac{(742.6\ \text{MPa})^2}{2\times196160\ \text{MPa}} = \mathbf{1.41\ MPa}$$

($1\ \text{MPa} = 1\ \text{MJ/m}^3$.)

### g) Load and elongation at the yield point
The load is the yield stress times the original area, and the elongation is the total strain of the yield point (the value $\varepsilon^*$ of item c) times the original length:

$$F_y = \sigma_y A_0 = 742.6\ \text{MPa}\times128.68\ \text{mm}^2 = 95\,554\ \text{N} = \mathbf{95.6\ kN}$$

$$\Delta l_y = \varepsilon^* l_0 = 0.0057855\times12.5\ \text{mm} = \mathbf{0.0723\ mm}$$

### h) Working stress
$$\sigma_w = \frac{\sigma_y}{N} = \frac{742.6}{2} = \mathbf{371.3\ MPa}$$

### i) Load for an elongation of 0.1 mm
The elongation of the yield point is 0.0723 mm, so $0.1$ mm is in the plastic zone and the load is not proportional to the elongation. Using Hooke's law anyway, $F = E A_0\Delta l/l_0$, would give

$$F = \frac{196160\ \text{N/mm}^2\times128.68\ \text{mm}^2\times0.1\ \text{mm}}{12.5\ \text{mm}} = 201\,935\ \text{N} = 202\ \text{kN}$$

which is larger than the maximum load that the sample supports, 160 400 N: the answer is **not** possible with the values obtained. The alternative is the table itself. The elongation 0.1 mm is between points 8 ($\Delta L = 0.095$ mm, $F = 102\,500$ N) and 9 ($\Delta L = 0.127$ mm, $F = 107\,800$ N), and a linear interpolation on that segment gives

$$F = F_{8} + \frac{0.1 - 0.095}{0.127 - 0.095}\,(F_{9} - F_{8}) = 102\,500 + 0.15625\times(107\,800 - 102\,500) = \mathbf{103\,328\ N}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $\sigma_n = F/A_0$ in N/mm² is MPa, $\varepsilon_n$ is a ratio of lengths and has no units, so $E = \sigma/\varepsilon$ is in MPa and $U_r = \sigma_y^2/2E$ is in MPa (energy per unit volume).
- **Order.** $\sigma_y = 742.6$ MPa $< \sigma_{max} = 1246.5$ MPa, and the fracture stress ($969.1$ MPa) is below the maximum, as in a ductile sample that necks.
- **The fit.** The secant moduli of points 1 to 5 are within 4.8 % of the fitted $E$, and the offset line crosses the curve between points 7 and 8, inside the segment used.
- **Item i.** The interpolated load, 103.3 kN, is between the loads of the two rows and below the maximum load; the Hooke value, 202 kN, is not.

### Interpretation
The sample is stiff ($E \approx 196$ GPa) and strong, and it yields at about 742.6 MPa, a strain of 0.579 %. From there to the maximum load the strain hardening raises the stress by 504 MPa, and the 11.2 % of plastic elongation at fracture shows that it is also ductile.

> [!warning] The data are not those of aluminium
> The table of Session 11 gives $E = 69$ GPa for aluminium and 207 GPa for steel [Session 11 Slide 17]. The data of this problem give $E \approx 196$ GPa and a yield strength above 700 MPa, which are the values of a steel, not of aluminium. The statement says "aluminum"; the data are used as they are.

## ✅ Check against the official solution
The key printed on the sheet is compared with the values computed here:

| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| b. $E$ | $\approx 200$ GPa | 196.2 GPa | agrees (2 %) |
| c. $\sigma_y$ | 740 MPa | 742.6 MPa | agrees |
| d. $\sigma_{max}$ | 1250 MPa | 1246.5 MPa | agrees (rounded) |
| e. ductility | 11.3 % | 11.2 % | agrees within the reading |
| f. $U_r$ | 1.37 MPa | 1.41 MPa | agrees (2.5 %); the key uses $E = 200$ GPa and $\sigma_y = 740$ MPa |
| g. $F_y$, $\Delta l_y$ | $9.5\times10^4$ N, 0.071 mm | 95 554 N, 0.0723 mm | agrees |
| h. $\sigma_w$ | 370 MPa | 371.3 MPa | agrees |
| i. load at 0.1 mm | $10.3\times10^4$ N, graphically | 103\,328 N | agrees |

> [!note] Reading of the table
> The text of the PDF prints the first load of the table as "1127", but the figure of the sheet shows "127". With 127 the first point gives $\sigma/\varepsilon = 206$ GPa, in line with the rest of the elastic points and with the key, so 127 (12 700 N) is used.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Uniaxial Tension Test and Engineering Stress-Strain]]
* [[Concept - Hooke's Law, Young's Modulus and Non-Linear Elasticity]]
* [[Concept - Yield Strength and the 0.2 Percent Offset]]
* [[Concept - Toughness and Modulus of Resilience]]
