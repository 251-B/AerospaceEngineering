---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 3"
dificultad: hard
badge: "Tensile test · true stress and strain · design"
tags:
  - official-problem
  - solved
  - tensile-test
  - true-stress
  - necking
  - design
---

# ✏️ Problem: T5-03 — Tensile Test of a 13 mm Sample: Modulus, Cable Section and True Values at Maximum Load and Fracture

## 📄 Official Statement
> 3. An uniaxial tensile test was performed on a cylindrical sample of 13 mm in diameter getting the results of load and elongation shown in the table below:
>
> - a. Calculate the engineering stress and strain values and draw the stress-strain curve.
> - b. Calculate the value of the elastic modulus (Young's Modulus) and determine the length of a bar of 13 cm on which a tension of 200 MPa is applied.
> - c. What is the recommended cross-section for a cable that has to support an elevator with a maximum weight of 450 kg?
> - d. Calculate the real stress and real strain values at maximum load and at the fracture point, assuming that the diameter of the sample is 12.922 mm and 10.348 mm respectively. Do the calculations without using the engineering stress and strain values.
> - e. Calculate the modulus of resilience.
> - f. Calculate the elastic strain at the moment before fracture.
>
> | Point | Load (kg) | Calibrated length (mm) | Engineering stress (MPa) | Engineering strain |
> | ---: | ---: | ---: | ---: | ---: |
> | 0 | 0 | 5.148 |  |  |
> | 1 | 500 | 5.151 |  |  |
> | 2 | 1500 | 5.156 |  |  |
> | 3 | 2500 | 5.161 |  |  |
> | 4 | 3500 | 5.166 |  |  |
> | 5 | 3750 | 5.225 |  |  |
> | 6 | 3950 | 5.354 |  |  |
> | 7 | 4000 | 5.457 |  |  |
> | 8 | 4000 | 5.560 |  |  |
> | 9 | 3600 | 5.676 |  |  |
>
> *(In the sheet the table has only the first two columns filled; the last two are left blank to be completed in item a. Point 0 is the unloaded sample, points 7 and 8 have the same, maximum, load, and point 9 is the fracture.)*
>
> *(Solution: b. $E = 75.4$ GPa, $l = 13.04$ cm; c. $A_0 \geq 16.9$ mm²; d. maximum load: $\sigma_{UTS} = 300$ MPa, $\varepsilon_{UTS} = 0.012$; fracture: $\sigma_{fracture} = 420$ MPa, $\varepsilon_{fracture} = 0.456$; e. $U_r = 0.457$ MPa; f. $\varepsilon_y = 3.4\times10^{-3}$)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Uniaxial, uniform stress** up to the necking: engineering stress and strain with the original area and length [Session 11 Slide 9].
2. **Weight to force.** The loads are masses in kilograms; the force is $F = m\,g$ with $g = 9.81$ m/s².
3. **Linear elastic start** [Session 11 Slide 13] and **0.2 % offset yield strength** [Session 11 Slide 28].
4. **Calibrated length.** The first row ($m = 0$) gives the initial length $l_0 = 5.148$ mm and the other rows the current length. The strain is a ratio, so only the proportion matters.
5. **True quantities from the measured diameters** (item d). The true strain is $\varepsilon_r = \ln(A_0/A) = 2\ln(D_0/D)$ and the true stress is $\sigma_r = F/A$ with $A$ the instantaneous area [Session 11 Slide 38]. They are valid also after the necking, because they use the actual area at the neck.
6. **Design stress (item c).** The statement does not give a safety factor. The minimum section is the one for which the cable does not yield, $\sigma = F/A_0 \leq \sigma_y$; with the usual factor $N = 2$ it would be larger [Session 11 Slide 29].

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Diameter | $d_0$ | 13 mm | $13\times10^{-3}$ m |
| Initial calibrated length | $l_0$ | 5.148 mm | $5.148\times10^{-3}$ m |
| Gravity | $g$ | 9.81 m/s² | |
| Bar of item b: length, stress | $l_b$, $\sigma$ | 13 cm, 200 MPa | 0.13 m, $200\times10^6$ Pa |
| Elevator (item c) | $m$ | 450 kg | |
| Diameter at maximum load, at fracture | $D_m$, $D_f$ | 12.922 mm, 10.348 mm | |

**Unknowns:** the curve (a), $E$ and the length of the bar (b), the section of the cable (c), the true stress and strain at maximum load and at fracture (d), $U_r$ (e), the elastic strain before the fracture (f).

---

## 🧠 2. Phase 2: Frames and Strategy

One direction (the axis) and uniaxial stress: there is no change of basis.

**Strategy.** The table is converted into $\sigma_n = F/A_0$ and $\varepsilon_n = (l - l_0)/l_0$. Then:
- $E$ is the slope of the straight part (least squares through the origin), and the bar of item b is a direct application of Hooke's law, $\Delta l = (\sigma/E)\,l_b$.
- $\sigma_y$ by the 0.2 % offset is needed twice: for the cable (c) and for the resilience (e).
- The true values (d) are computed from the forces and the measured diameters, as the statement asks, and not from the engineering values.
- The elastic strain before the fracture (f) is $\sigma/E$ with the stress that acts at that moment [Session 11 Slide 32].

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Cross-section and conversions
$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(13\ \text{mm})^2}{4}$$

With $13^2 = 169$ and $\pi\times169 = 530.93$:

$$A_0 = 132.73\ \text{mm}^2$$

For the first loaded point, $F_1 = 500\ \text{kg}\times9.81\ \text{m/s}^2 = 4\,905\ \text{N}$, so

$$\sigma_{n,1} = \frac{4\,905\ \text{N}}{132.73\ \text{mm}^2} = 36.95\ \text{MPa} \qquad \varepsilon_{n,1} = \frac{5.151 - 5.148}{5.148} = 0.00058$$

### a) Engineering stress and strain, and the curve
All the points:

| Point | Load (kg) | $l$ (mm) | $F = m g$ (N) | $\sigma_n$ (MPa) | $\varepsilon_n$ | $\sigma_n/\varepsilon_n$ (GPa) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 5.148 | 0 | 0.00 | 0 | — |
| 1 | 500 | 5.151 | 4 905 | 36.95 | 0.00058 | 63.4 |
| 2 | 1500 | 5.156 | 14 715 | 110.86 | 0.00155 | 71.3 |
| 3 | 2500 | 5.161 | 24 525 | 184.77 | 0.00253 | 73.2 |
| 4 | 3500 | 5.166 | 34 335 | 258.68 | 0.00350 | 74.0 |
| 5 | 3750 | 5.225 | 36 788 | 277.16 | 0.01496 | 18.5 |
| 6 | 3950 | 5.354 | 38 750 | 291.94 | 0.04002 | 7.3 |
| 7 | 4000 | 5.457 | 39 240 | 295.63 | 0.06002 | 4.9 |
| 8 | 4000 | 5.560 | 39 240 | 295.63 | 0.08003 | 3.7 |
| 9 | 3600 | 5.676 | 35 316 | 266.07 | 0.10256 | 2.6 |

![[attachments/T5/t5-p3-curve.svg]]

### b) Young's modulus and the length of the bar
The secant modulus of the last column grows from 63 to 74 GPa in points 1 to 4 and falls to 18 GPa at point 5: the linear zone ends after point 4. The first value is lower because a strain of 0.0006 comes from an elongation of only 0.003 mm, at the limit of the resolution of the table. The fit through the origin on points 1 to 4 is:

| Point | $\varepsilon_i$ | $\sigma_i$ (MPa) | $\sigma_i\varepsilon_i$ (MPa) | $\varepsilon_i^2$ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.00058 | 36.95 | 0.0215 | $3.396\times 10^{-7}$ |
| 2 | 0.00155 | 110.86 | 0.1723 | $2.415\times 10^{-6}$ |
| 3 | 0.00253 | 184.77 | 0.4666 | $6.377\times 10^{-6}$ |
| 4 | 0.00350 | 258.68 | 0.9045 | $1.223\times 10^{-5}$ |

$$E = \frac{\sum \sigma_i\varepsilon_i}{\sum \varepsilon_i^2} = \frac{1.565}{2.1357\times 10^{-5}} = 73273\ \text{MPa} = \mathbf{73.3\ GPa}$$

For the bar, the strain produced by $\sigma = 200$ MPa is $\varepsilon = \sigma/E$ and the elongation is $\Delta l = \varepsilon\,l_b$:

$$\varepsilon = \frac{200}{73273} = 0.002730 \qquad \Delta l = 0.002730\times130\ \text{mm} = 0.355\ \text{mm}$$

$$l = l_b + \Delta l = 130 + 0.355 = 130.355\ \text{mm} = \mathbf{13.04\ cm}$$

### c) Section of the cable
The yield strength is needed first. With the offset line $E(\varepsilon - 0.002)$ the sign of $g = \sigma_n - E(\varepsilon_n - 0.002)$ changes between points 4 and 5:

| Point | $\varepsilon_n$ | $\sigma_n$ (MPa) | $E(\varepsilon_n - 0.002)$ (MPa) | $g = \sigma_n - E(\varepsilon_n - 0.002)$ (MPa) |
| --- | ---: | ---: | ---: | ---: |
| 3 | 0.00253 | 184.8 | 38.5 | 146.3 |
| 4 | 0.00350 | 258.7 | 109.7 | 149.0 |
| 5 | 0.01496 | 277.2 | 949.4 | -672.3 |
| 6 | 0.04002 | 291.9 | 2785.5 | -2493.6 |

$$m = \frac{277.16 - 258.68}{0.01496 - 0.00350} = 1612.2\ \text{MPa} \qquad \varepsilon^* = \frac{258.68 - 1612.2\times0.00350 + 0.002\times73273}{73273 - 1612.2} = \frac{399.587}{71660.3} = 0.0055761$$

$$\sigma_y = E\,(\varepsilon^* - 0.002) = 73273\times(0.0055761 - 0.002) = \mathbf{262.0\ MPa}$$

The weight of the elevator is $W = 450\times9.81 = 4414.5$ N. For the cable not to yield, $W/A_0 \leq \sigma_y$:

$$A_0 \geq \frac{W}{\sigma_y} = \frac{4414.5\ \text{N}}{262.0\ \text{N/mm}^2} = \mathbf{16.85\ mm^2}$$

If the usual safety factor $N = 2$ is also applied, the design stress is $\sigma_y/2$ and the section doubles, $A_0 \geq 33.7$ mm².

### d) True stress and strain at maximum load and at fracture
**Maximum load.** $F_m = 4000\times9.81 = 39\,240$ N and $D_m = 12.922$ mm:

$$A_m = \frac{\pi\,(12.922)^2}{4} = \frac{\pi\times166.978}{4} = 131.14\ \text{mm}^2$$

$$\sigma_{r,UTS} = \frac{F_m}{A_m} = \frac{39\,240}{131.14} = \mathbf{299.2\ MPa} \qquad \varepsilon_{r,UTS} = 2\ln\frac{D_0}{D_m} = 2\ln\frac{13}{12.922} = 2\ln(1.00604) = 2\times0.006018 = \mathbf{0.01204}$$

**Fracture.** $F_f = 3600\times9.81 = 35\,316$ N and $D_f = 10.348$ mm:

$$A_f = \frac{\pi\,(10.348)^2}{4} = \frac{\pi\times107.081}{4} = 84.10\ \text{mm}^2$$

$$\sigma_{r,f} = \frac{F_f}{A_f} = \frac{35\,316}{84.10} = \mathbf{419.9\ MPa} \qquad \varepsilon_{r,f} = 2\ln\frac{13}{10.348} = 2\ln(1.25628) = 2\times0.22816 = \mathbf{0.4563}$$

### e) Modulus of resilience
$$U_r = \frac{\sigma_y^2}{2E} = \frac{(262.0\ \text{MPa})^2}{2\times73273\ \text{MPa}} = \mathbf{0.469\ MPa}$$

### f) Elastic strain before the fracture
The stress of the table at the fracture point (point 9) is $\sigma_n = 266.1$ MPa, and the elastic part of the strain is given by Hooke's law:

$$\varepsilon_e = \frac{\sigma_n}{E} = \frac{266.1}{73273} = \mathbf{3.63\times 10^{-3}}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** Masses in kg and $g$ in m/s² give newtons, N/mm² is MPa, the strains have no units, and $A_0 \geq W/\sigma_y$ comes out in mm².
- **Order.** The true stress at maximum load (299.2 MPa) is above the engineering maximum (295.6 MPa) because the area has shrunk, and the true fracture stress (419.9 MPa) is much above the engineering one (266.1 MPa), while the engineering stress falls after the maximum.
- **Limit.** For $D = D_0$ the true strain $2\ln(D_0/D)$ is zero and the true stress is $F/A_0$, the engineering one.
- **Bar.** The elongation, 0.355 mm over 130 mm, is a strain of 0.27 %, well inside the elastic zone (the yield strain is 3.58 × 10⁻³ = 0.36 %).

### Interpretation
The sample is a ductile metal with a clear yield at 262.0 MPa and a long hardening plateau up to 295.6 MPa; the neck makes the true stress at fracture 419.9 MPa. The cable needs at least 16.85 mm² to stay elastic under the elevator, and about twice as much with the usual safety factor.

> [!warning] Diameters and lengths of the table do not describe the same strain
> At the maximum load the length of the table gives $\varepsilon_n = 0.0600$, that is, $\varepsilon_r = \ln(1+\varepsilon_n) = 0.0583$ with the uniform-deformation relation, and constant volume would give a diameter $13/\sqrt{1+\varepsilon_n} = 12.63$ mm. The statement gives $12.922$ mm, with $\varepsilon_r = 0.01204$. At the fracture, $A_0/A_f = 1.578$ while $l/l_0 = 1.1026$. The two sets of data do not describe the same deformation: the diameters measure the strain of the neck, the lengths the average over the calibrated length. The statement asks to compute the true values from the diameters, and that is what is done.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| b. $E$ | 75.4 GPa | 73.3 GPa | agrees (3 %) |
| b. length of the bar | 13.04 cm | 13.04 cm | agrees |
| c. $A_0$ | $\geq 16.9$ mm² | $\geq 16.85$ mm² | agrees: the key uses $\sigma_y$ without safety factor |
| d. $\sigma_{r,UTS}$, $\varepsilon_{r,UTS}$ | 300 MPa, 0.012 | 299.2 MPa, 0.01204 | agrees |
| d. $\sigma_{r,f}$, $\varepsilon_{r,f}$ | 420 MPa, 0.456 | 419.9 MPa, 0.4563 | agrees |
| e. $U_r$ | 0.457 MPa | 0.469 MPa | agrees (2.5 %): the key uses $E = 75.4$ GPa |
| f. elastic strain | $3.4\times10^{-3}$ | $3.63\times 10^{-3}$ | differs 7 % |

> [!warning] Discrepancy with the official solution: elastic strain before the fracture
> The key gives $3.4\times10^{-3}$. With the stress of the table at the fracture, 266.1 MPa, and the fitted modulus the elastic strain is 3.63 × 10⁻³; with the key's modulus, 75.4 GPa, it is 3.53 × 10⁻³. The yield strain, $\sigma_y/E = 3.58\times10^{-3}$, is also not the key value. The value cannot be reproduced exactly, and the computed one is kept.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - True Stress and True Strain]]
* [[Concept - Working Stress and the Safety Factor]]
* [[Concept - Yield Strength and the 0.2 Percent Offset]]
* [[Concept - Hooke's Law, Young's Modulus and Non-Linear Elasticity]]
