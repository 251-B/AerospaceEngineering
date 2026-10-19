---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 13"
dificultad: easy
badge: "Vickers · Brinell hardness"
tags:
  - official-problem
  - solved
  - hardness
  - vickers
  - brinell
  - indentation
---

# ✏️ Problem: T5-13 — Vickers and Brinell Hardness Numbers from Indentation Measurements

## 📄 Official Statement
> 13. Calculate the Vickers and Brinell hardness numbers for a metallic material on which several hardness tests were performed, obtaining the following results:
>
> - a. When the diamond Vickers hardness test with a load of 30 kg was performed, the average length of the diagonal was: first impression 0.527 mm, second impression 0.481 mm, third impression 0.497 mm.
> - b. When using the Brinell test with a ball of 10 mm and a load of 3000 kg, the diameter of the indentation was 4.01 mm.
>
> *(Solution: 220 HV, 227 HB)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Vickers.** The indenter is a diamond right pyramid with 136° between opposite faces; the hardness is the load divided by the lateral area of the impression, $HV = F/A_{imp}$, which depends only on the mean diagonal $d$ [Session 12 Slide 26]. The slide defines $d$ as the arithmetic mean of the two diagonals $d_1$ and $d_2$ of one impression; here the sheet gives one diagonal length for each of the three impressions, which are averaged first.
2. **Brinell.** The hardness is the load divided by the area $S$ of the spherical cap left by the ball, $HB = P/S$ with $P$ in kg [Session 12 Slide 19]. The result is a number with no units attached by convention.
3. The tests are performed under their standard conditions (flat surface, indentation far from edges and from other impressions) [Session 12 Slide 28].

### Data
| Quantity | Symbol | Value |
| :--- | :--- | ---: |
| Vickers load | $F$ | 30 kgf (HV30) |
| Mean diagonal, impression 1 | $d_1$ | 0.527 mm |
| Mean diagonal, impression 2 | $d_2$ | 0.481 mm |
| Mean diagonal, impression 3 | $d_3$ | 0.497 mm |
| Brinell load | $P$ | 3000 kg |
| Ball diameter | $D$ | 10 mm |
| Diameter of the indentation | $D_i$ | 4.01 mm |

**Unknowns:** $HV$ (a) and $HB$ (b). Both loads are kilogram-force, the unit used by the slides; the hardness numbers are quoted without units (kgf/mm² in the definition, $1\ \text{kgf} = 9.81$ N).

---

## 🧠 2. Phase 2: Frames and Strategy

No frames are involved. Each hardness comes from the load and one measured length, through the formulas of the slides.

**Strategy.**
- (a) Average the three diagonals, as the slide does with $d_1$ and $d_2$, and use $HV = 2F\sin(136^\circ/2)/d^2 = 1.854\,F/d^2$. The expression is derived from the pyramid: the faces make 136° with each other, so the lateral area is $A = d^2/(2\sin 68^\circ)$ and $HV = F/A$.
- (b) Use $HB = 2P/\big[\pi D\,(D - \sqrt{D^2 - D_i^2})\big]$, which is $P$ over the area of the cap, $S = \pi D h$ with $h = (D - \sqrt{D^2-D_i^2})/2$ the depth of the indentation.

![[attachments/T5/t5-brinell-geometry.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Vickers hardness
**Mean diagonal.**

$$\bar d = \frac{d_1 + d_2 + d_3}{3} = \frac{0.527 + 0.481 + 0.497}{3} = \frac{1.505}{3} = 0.50167\ \text{mm}$$

**Constant of the pyramid.** $\sin 68^\circ = 0.927184$, so

$$2\sin\frac{136^\circ}{2} = 2\sin 68^\circ = 1.8544$$

**Hardness.**

$$HV = \frac{2F\sin(136^\circ/2)}{\bar d^{\,2}} = \frac{1.8544\times30}{(0.5017)^2} = \frac{55.631}{0.251669} = \mathbf{221.0\ HV30}$$

so the hardness is about **221 HV**.

### b) Brinell hardness
The indentation is characterised by its diameter $D_i = 4.01$ mm, with the ball of $D = 10$ mm:

$$D_i^2 = 4.01^2 = 16.0801 \qquad D^2 - D_i^2 = 100 - 16.0801 = 83.9199\ \text{mm}^2 \qquad \sqrt{D^2 - D_i^2} = 9.16078\ \text{mm}$$

$$D - \sqrt{D^2 - D_i^2} = 10 - 9.16078 = 0.83922\ \text{mm} \qquad \pi D\,(D - \sqrt{D^2 - D_i^2}) = \pi\times10\times0.83922 = 26.3649\ \text{mm}^2$$

The depth of the indentation is $h = 0.83922/2 = 0.4196$ mm and the area of the cap $S = 26.3649/2 = 13.182$ mm². Therefore

$$HB = \frac{2P}{\pi D\,(D - \sqrt{D^2 - D_i^2})} = \frac{2\times3000}{26.3649} = \mathbf{227.6\ HB}$$

that is, about **228 HB** (equivalently $P/S = 3000/13.182 = 227.6$).

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $F$ in kgf and $d$ in mm give kgf/mm², the unit of hardness; $D^2 - D_i^2$ in mm², and the Brinell denominator is an area (mm²), so $P/S$ is again kgf/mm².
- **Load factor.** $Q = P/D^2 = 3000/10^2 = 30$, one of the standard values of the table of [Session 12 Slide 20] for the ball of 10 mm.
- **Order of magnitude.** $HV\approx221$ and $HB\approx228$ are of the same order, since both scales are defined as a load in kgf over an area in mm²; but the slides remind us that there is no universal conversion between methods [Session 12 Slide 15].
- **Limit.** If $D_i \to 0$ then $D - \sqrt{D^2-D_i^2} \to D_i^2/(2D)$ and $HB \to 4P/(\pi D_i^2)$, the load over the area of the circle of the indentation, as it should for a very shallow cap.

### Interpretation
The metal is a medium-hard alloy, of the order of 220 kgf/mm². The three Vickers impressions differ by 10 % in their diagonals (0.481 to 0.527 mm), which changes the hardness by about 20 % between impressions (240.5 to 200.3 HV): this is the scatter of the measurement, and the reason why several tests are averaged.

> [!note] Average of the diagonals, not of the hardness numbers
> The slide defines $d$ as the mean of the diagonals of the impression, so the diagonals are averaged first and one hardness is computed. Averaging the three hardness numbers instead (225.2, 240.5, 200.3) would give 222.0 HV, which is not the value defined by the slide.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Vickers | 220 HV | 221.0 HV | agrees to the rounding of the key |
| Brinell | 227 HB | 227.6 HB | agrees (the key truncates) |

> [!warning] Small difference with the official solution: Vickers
> The key gives 220 HV and the computation, with $1.854$ from $2\sin68^\circ = 1.8544$, gives 221.0 HV. The difference is below 0.5 %. The computed value is kept; the key looks rounded down to the tens.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Hardness Tests Mohs Brinell Rockwell Vickers]]
