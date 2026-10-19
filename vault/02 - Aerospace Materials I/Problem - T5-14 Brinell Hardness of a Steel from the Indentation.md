---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 14"
dificultad: easy
badge: "Brinell hardness"
tags:
  - official-problem
  - solved
  - hardness
  - brinell
  - indentation
---

# ✏️ Problem: T5-14 — Brinell Hardness of a Steel from the Indentation

## 📄 Official Statement
> 14. A Brinell indenter of 10 mm in diameter produced an indentation of 2.5 mm in diameter in a steel when a load of 1000 kg was applied. Calculate the Brinell hardness for that material.
>
> *(Solution: 200 HB)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. The indentation is a spherical cap left by a hard ball of diameter $D$ pressed with the load $P$, and the hardness is $HB = P/S$ [Session 12 Slide 19].
2. $P$ is in kilogram-force (kg in the slide) and the lengths in mm, so $HB$ is in kgf/mm² and is quoted as a number.
3. The test is standard: the load factor $Q = P/D^2$ of the test must be one of those of [Session 12 Slide 20].

### Data
| Quantity | Symbol | Value |
| :--- | :--- | ---: |
| Ball diameter | $D$ | 10 mm |
| Diameter of the indentation | $D_i$ | 2.5 mm |
| Load | $P$ | 1000 kg |

**Unknown:** the Brinell hardness $HB$.

---

## 🧠 2. Phase 2: Frames and Strategy

No frames are involved: only one formula, applied directly.

**Why this formula.** The slide writes $HB = P/S$ with $S$ the area of the spherical cap. For a sphere of diameter $D$, the cap of height $h$ has area $S = \pi D h$ (Archimedes), and its base circle has radius $D_i/2$, so $h$ follows from $(D/2 - h)^2 + (D_i/2)^2 = (D/2)^2$:

$$h = \frac{D - \sqrt{D^2 - D_i^2}}{2} \quad\Rightarrow\quad S = \frac{\pi D}{2}\left(D - \sqrt{D^2 - D_i^2}\right) \quad\Rightarrow\quad HB = \frac{2P}{\pi D\left(D - \sqrt{D^2 - D_i^2}\right)}$$

which is the expression of [Session 12 Slide 19].

![[attachments/T5/t5-brinell-geometry.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

Square of the indentation diameter and of the ball diameter:

$$D_i^2 = 2.5^2 = 6.25\ \text{mm}^2 \qquad D^2 = 10^2 = 100\ \text{mm}^2$$

Difference and square root:

$$D^2 - D_i^2 = 100 - 6.25 = 93.75\ \text{mm}^2 \qquad \sqrt{D^2 - D_i^2} = 9.68246\ \text{mm}$$

Bracket of the formula and denominator:

$$D - \sqrt{D^2 - D_i^2} = 10 - 9.68246 = 0.31754\ \text{mm} \qquad \pi D\left(D - \sqrt{D^2 - D_i^2}\right) = \pi\times10\times0.31754 = 9.9759\ \text{mm}^2$$

Hardness:

$$HB = \frac{2P}{\pi D\left(D - \sqrt{D^2 - D_i^2}\right)} = \frac{2\times1000\ \text{kg}}{9.9759\ \text{mm}^2} = \mathbf{200.5\ HB}\approx 200\ HB$$

The depth of the indentation is $h = 0.31754/2 = 0.1588$ mm and the area of the cap $S = \pi D h = 4.988$ mm², so $P/S = 1000/4.988 = 200.5$, the same.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $2P$ in kg (kgf) over an area in mm²: kgf/mm², the unit of hardness (no unit is attached to HB).
- **Load factor.** $Q = P/D^2 = 1000/10^2 = 10$, a value of the table of [Session 12 Slide 20] for $D = 10$ mm (load of 1000 kg), so the test is a standard one.
- **Limit.** For $D_i \ll D$, $D - \sqrt{D^2-D_i^2}\approx D_i^2/(2D)$ and $HB \approx 4P/(\pi D_i^2) = 203.7$, close to the exact value (the cap is almost flat); for $D_i \to D$, the cap becomes a hemisphere, $S\to\pi D^2/2$, and $HB \to 2P/(\pi D^2)$.
- **Geometry.** $D_i/D = 0.25$: the indentation is a small fraction of the ball, consistent with a hard steel.

### Interpretation
The steel has a Brinell hardness of about 200 kgf/mm². It is harder than the plain carbon steel of the table of typical values, 150 HBW [Session 12 Slide 28]. Hardness and tensile strength are both indicators of the plastic deformation, with a relation that depends on the material [Session 12 Slide 30].

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Brinell hardness | 200 HB | 200.5 HB | agrees |

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Hardness Tests Mohs Brinell Rockwell Vickers]]
