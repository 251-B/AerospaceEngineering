---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 7"
dificultad: hard
badge: "Poisson's ratio · safety factor · design"
tags:
  - official-problem
  - solved
  - poisson-ratio
  - hooke-law
  - safety-factor
  - yield-strength
  - design
---

# ✏️ Problem: T5-07 — Crane Cable: Poisson's Ratio, Safety Factor and Replacement Cable

## 📄 Official Statement
> 7. In a construction site, a change in the diameter of one of the crane cables was detected. When the weight that the cable was withstanding was 48950 N, the change was 5.3 10⁻³ mm, and when the load was removed, the cable recovered its initial diameter of 15 mm. Considering that for this kind of steel the Poisson's ratio ν = 0.33 and according to the manufacturer data the initial length of the cable is 3 m.
>
> - a. Calculate the length of the cable when it's holding the load mentioned above.
> - b. If it has been detected that plastic deformation of the cable begins when it is holding a weight of 10000 kg, can it be considered that the cable is working under safe conditions? Assume a safety factor of 2.
> - c. What is the value of the elastic modulus for this material?
> - d. In order to prevent service problems the provider replaces the cable for a different one, which has a stress-strain curve represented below and an elastic modulus of E = 75 GPa. Can this material replace the previous one? Explain why.
> - e. Calculate the final length of this new cable in case it is working under the same conditions (48950 N).
>
> ![[attachments/T5/t5-p7-chart.png]]
>
> *(Solution: a. $l = 3003.2$ mm; b. yes; c. $E = 261.3$ GPa; d. no; e. $l = 3045$ mm)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Elastic and isotropic cable under a uniaxial load.** When it holds the weight the cable is elastic (it recovers its diameter when the load is removed), the stress is uniform, and Hooke's law $\sigma = E\varepsilon$ and $\varepsilon_{lat} = -\nu\varepsilon_{ax}$ hold [Session 11 Slides 13 and 19].
2. **Lateral strain from the diameter.** The change of 5.3·10⁻³ mm is a decrease of the diameter ($\Delta d < 0$ under tension), and the strain is relative to the initial diameter, 15 mm.
3. **Yield load.** "Plastic deformation begins when it holds a weight of 10 000 kg" means that the yield strength is the stress that this weight produces; the weight in newtons is $m\,g$ with $g = 9.81$ m/s² [Session 11 Slide 28].
4. **Safety factor.** The working stress is $\sigma_w = \sigma_y/N$, and the cable works under safe conditions if the stress that it supports does not exceed $\sigma_w$ [Session 11 Slide 29].
5. **Replacement cable.** Its stress-strain curve is the one printed on the sheet (a chart of ten points), with the modulus given, $E = 75$ GPa. The yield strength of the new material is taken with the 0.2 % offset [Session 11 Slide 28], and the readings of the chart are the values of the markers.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Load in service | $F$ | 48 950 N | 48 950 N |
| Initial diameter | $d_0$ | 15 mm | $15\times10^{-3}$ m |
| Change of diameter | $\Delta d$ | $-5.3\times10^{-3}$ mm | $-5.3\times10^{-6}$ m |
| Poisson's ratio | $\nu$ | 0.33 | dimensionless |
| Initial length | $l_0$ | 3 m | 3000 mm |
| Weight at which plastic deformation begins | $m$ | 10 000 kg | $98\,100$ N |
| Safety factor | $N$ | 2 | dimensionless |
| Modulus of the replacement cable | $E_{new}$ | 75 GPa | 75 000 N/mm² |

**Unknowns:** the length under load (a), whether the cable is safe (b), $E$ (c), whether the new cable can replace it (d), and its length under load (e).

---

## 🧠 2. Phase 2: Frames and Strategy

One direction (the axis of the cable) and the two equal transverse directions; no change of basis.

**Strategy.**
- (a) The measured change of the diameter gives the transverse strain; Poisson's ratio turns it into the axial strain, and the axial strain into the elongation.
- (c) Once the axial strain is known, the modulus is the stress divided by it. Item c is solved before b and d because $E$ is used in the discussion.
- (b) The weight of 10 000 kg gives the yield strength; the safety factor gives the working stress, which is compared with the stress in service.
- (d), (e) The new cable is compared with the old one through the yield strength of the curve of the sheet: if the service stress exceeds it, the cable deforms permanently. The length (e) is read on the curve at the service stress, which is the same, since the section and the load are the same.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Cross-section and stress in service
$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(15\ \text{mm})^2}{4}$$

With $15^2 = 225$ and $\pi\times225 = 706.86$:

$$A_0 = 176.71\ \text{mm}^2 \qquad \sigma = \frac{F}{A_0} = \frac{48\,950\ \text{N}}{176.71\ \text{mm}^2} = 277.00\ \text{MPa}$$

### a) Length of the cable under the load
The lateral strain is the change of the diameter over the initial diameter, negative because the diameter shrinks:

$$\varepsilon_{lat} = \frac{\Delta d}{d_0} = \frac{-5.3\times10^{-3}\ \text{mm}}{15\ \text{mm}} = -3.5333\times 10^{-4}$$

From $\nu = -\varepsilon_{lat}/\varepsilon_{ax}$ [Session 11 Slide 19], the axial strain is

$$\varepsilon_{ax} = -\frac{\varepsilon_{lat}}{\nu} = \frac{3.5333\times 10^{-4}}{0.33} = 1.0707\times 10^{-3}$$

and the elongation and the length are

$$\Delta l = \varepsilon_{ax}\,l_0 = 1.0707\times 10^{-3}\times3000\ \text{mm} = 3.212\ \text{mm} \qquad l = l_0 + \Delta l = 3000 + 3.212 = \mathbf{3003.2\ mm}$$

### c) Elastic modulus
$$E = \frac{\sigma}{\varepsilon_{ax}} = \frac{277.00\ \text{N/mm}^2}{1.0707\times 10^{-3}} = 258708\ \text{MPa} = \mathbf{258.7\ GPa}$$

### b) Is the cable working under safe conditions?
The weight at which the plastic deformation begins is $W_y = 10\,000\times9.81 = 98\,100$ N, so the yield strength is

$$\sigma_y = \frac{W_y}{A_0} = \frac{98\,100\ \text{N}}{176.71\ \text{mm}^2} = 555.1\ \text{MPa}$$

With the safety factor of 2 the working stress, and the corresponding load, are

$$\sigma_w = \frac{\sigma_y}{N} = \frac{555.1}{2} = 277.6\ \text{MPa} \qquad F_w = \frac{W_y}{N} = \frac{98\,100}{2} = 49\,050\ \text{N}$$

The stress in service, 277.00 MPa, is not larger than $\sigma_w = 277.6$ MPa (equivalently, $48 950\ \text{N} < 49\,050\ \text{N}$), so the cable **works under safe conditions**: the safety factor really available is

$$N_{eff} = \frac{\sigma_y}{\sigma} = \frac{555.1}{277.00} = 2.004 \geq 2$$

The margin is very small, 0.20 % of the permitted load.

### d) Can the new cable replace the previous one?
The curve of the sheet is a chart of ten points. Its markers are at the strains and stresses of the table of Problem 3 (for example, the point at $\varepsilon = 0.0035$ and $\sigma \approx 259$ MPa, and the maximum at $\approx 296$ MPa), and those values are used as readings.

![[attachments/T5/t5-p7-chart.png]]

The yield strength of the new material, with the offset line $E_{new}(\varepsilon - 0.002)$ and $E_{new} = 75\,000$ MPa, changes sign of $g = \sigma - E_{new}(\varepsilon - 0.002)$ between the points 4 and 5:

| Point | $\varepsilon_n$ | $\sigma_n$ (MPa) | $E(\varepsilon_n - 0.002)$ (MPa) | $g = \sigma_n - E(\varepsilon_n - 0.002)$ (MPa) |
| --- | ---: | ---: | ---: | ---: |
| 3 | 0.00253 | 184.8 | 39.4 | 145.4 |
| 4 | 0.00350 | 258.7 | 112.2 | 146.4 |
| 5 | 0.01496 | 277.2 | 971.8 | -694.6 |
| 6 | 0.04002 | 291.9 | 2851.2 | -2559.2 |

$$m = \frac{277.16 - 258.68}{0.01496 - 0.00350} = 1612.2\ \text{MPa} \qquad \varepsilon^* = \frac{258.68 - 1612.2\times0.00350 + 0.002\times75\,000}{75\,000 - 1612.2} = \frac{403.042}{73387.8} = 0.0054919$$

$$\sigma_{y,new} = E_{new}\,(\varepsilon^* - 0.002) = 75\,000\times(0.0054919 - 0.002) = 261.9\ \text{MPa}$$

The stress that the new cable would carry is the same, 277.00 MPa, since the load and the section are the same. It is **larger** than its yield strength, $277.00 > 261.9$ MPa:

$$N_{eff,new} = \frac{\sigma_{y,new}}{\sigma} = \frac{261.9}{277.00} = 0.945 < 1 \quad (\text{the old cable has } 2.004)$$

Equivalently, the yield load of the new cable is $\sigma_{y,new}A_0 = 46.3$ kN, below the 48 950 N of service. The new cable would deform plastically and permanently under the same load, with no safety margin: the answer is **no**.

### e) Length of the new cable under the same conditions
The strain is read on the curve at the service stress $\sigma = 277.00$ MPa, which is between the points 4 and 5 ($\sigma = 258.68$ MPa at $\varepsilon = 0.00350$ and $\sigma = 277.16$ MPa at $\varepsilon = 0.01496$). By linear interpolation:

$$\varepsilon = 0.00350 + \frac{277.00 - 258.68}{277.16 - 258.68}\,(0.01496 - 0.00350) = 0.01486$$

$$\Delta l = \varepsilon\,l_0 = 0.01486\times3000\ \text{mm} = 44.6\ \text{mm} \qquad l = 3000 + 44.6 = \mathbf{3044.6\ mm}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $\Delta d/d_0$ and the strains have no units; N/mm² is MPa; $m\,g$ in kg·m/s² is N.
- **Poisson.** $\varepsilon_{lat}$ is negative and $\varepsilon_{ax}$ positive, and $|\varepsilon_{lat}| = 0.33\,\varepsilon_{ax}$, as the definition of $\nu$ demands.
- **Elastic range of the old cable.** The strain, $1.0707\times 10^{-3}$, is a small fraction of the one at which it yields, $\sigma_y/E = 555.1/258708 = 2.1\times10^{-3}$ (it works at about half of it, as the safety factor 2 says).
- **Consistency of $E$.** The modulus 258.7 GPa is larger than the one of steel in the table of the slide, 207 GPa [Session 11 Slide 17], by about 25 %. The text of the sheet speaks of "this kind of steel", so the value is plausible within the data of the problem.
- **New cable.** Its length under load, 3044.6 mm, is 14 times the elongation of the old one (3.2 mm against 44.6 mm), and permanent: on unloading it recovers $\sigma/E_{new} = 277.00/75\,000$ and keeps $\varepsilon_p = 0.01117$, that is, about 33.5 mm of permanent elongation.

### Interpretation
The two cables have the same section and carry the same load, but the old one works at 50 % of its yield strength and the new one above 100 %. A cable is not defined by its stiffness but by its yield strength: the new one is also much more flexible ($E = 75$ GPa against 259 GPa) and elongates by about 14 times as much. To keep the safety factor of 2 with the new material the section should be at least $A \geq N F/\sigma_{y,new} = 2\times48 950/261.9 = 373.8$ mm², that is, a diameter of 21.8 mm instead of 15 mm.

> [!note] The last item of the sheet
> The statement prints a "f." after item e, followed only by the chart of the stress-strain curve. There is no item f: the chart is the one that item d refers to ("a stress-strain curve represented below").

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a. length | 3003.2 mm | 3003.2 mm | agrees |
| b. safe? | yes | yes ($N_{eff} = 2.004$) | agrees, with a margin of 0.20 % |
| c. $E$ | 261.3 GPa | 258.7 GPa | differs 1 % |
| d. can replace? | no | no ($N_{eff,new} = 0.945$) | agrees |
| e. length | 3045 mm | 3044.6 mm | agrees |

> [!warning] Discrepancy with the official solution: modulus of the cable
> The key gives $E = 261.3$ GPa. The data of the statement give 258.7 GPa from the unrounded strain, and 259.7 GPa if the elongation is rounded to 3.2 mm. The 261.3 GPa of the key is not reproduced by either value (it needs an axial strain of $1.060\times10^{-3}$); the difference is 1 % and it does not affect the other answers. The computed value is kept.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Poisson's Ratio and the Shear Modulus]]
* [[Concept - Working Stress and the Safety Factor]]
* [[Concept - Yield Strength and the 0.2 Percent Offset]]
