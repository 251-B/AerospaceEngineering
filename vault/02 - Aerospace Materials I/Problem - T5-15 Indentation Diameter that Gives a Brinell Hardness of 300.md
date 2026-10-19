---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 15"
dificultad: easy
badge: "Brinell hardness · inverse problem"
tags:
  - official-problem
  - solved
  - hardness
  - brinell
  - indentation
---

# ✏️ Problem: T5-15 — Indentation Diameter that Gives a Brinell Hardness of 300

## 📄 Official Statement
> 15. What will be the diameter of the indentation that produces a Brinell hardness of 300 when a load of 500 kg is applied? Diameter of the ball: 10 mm.
>
> *(Solution: $d = 1.453$ mm)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. Same definition as in Problem 14: $HB = P/S$, with $S$ the area of the spherical cap, $HB = \dfrac{2P}{\pi D\left(D - \sqrt{D^2 - D_i^2}\right)}$ [Session 12 Slide 19].
2. $P$ in kilogram-force, lengths in mm; the hardness number has no unit attached.
3. Only the physically meaningful root is retained: the indentation diameter is positive and not larger than the ball, $0 < D_i \leq D$.

### Data
| Quantity | Symbol | Value |
| :--- | :--- | ---: |
| Brinell hardness | $HB$ | 300 |
| Load | $P$ | 500 kg |
| Ball diameter | $D$ | 10 mm |

**Unknown:** the diameter of the indentation $D_i$ (called $d$ in the key).

---

## 🧠 2. Phase 2: Frames and Strategy

This is the *inverse* of Problem 14: the hardness is known, and the indentation is the unknown. The formula of the slide is solved for $D_i$ before substituting numbers:

1. Isolate the bracket: $D - \sqrt{D^2 - D_i^2} = \dfrac{2P}{\pi D\,HB} \equiv k$.
2. Isolate the square root: $\sqrt{D^2 - D_i^2} = D - k$.
3. Square both sides, $D^2 - D_i^2 = (D - k)^2$, and solve: $D_i^2 = D^2 - (D-k)^2 = 2Dk - k^2 = k\,(2D - k)$.

The squaring step is allowed here because $D - k > 0$ (the left side is a square root, and $k$ is a small fraction of $D$), so no spurious root is introduced.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. The bracket $k$
$$k = D - \sqrt{D^2 - D_i^2} = \frac{2P}{\pi D\,HB} = \frac{2\times500}{\pi\times10\times300} = \frac{1000}{9424.78} = 0.106103\ \text{mm}$$

### 2. The indentation diameter
$$D_i^2 = k\,(2D - k) = 0.106103\times(20 - 0.106103) = 0.106103\times19.893897 = 2.11081\ \text{mm}^2$$

$$D_i = \sqrt{2.11081\ \text{mm}^2} = \mathbf{1.4529\ mm}$$

### 3. Verification by substitution
$\sqrt{D^2 - D_i^2} = \sqrt{100 - 2.11081} = 9.893897$ mm, which is $D - k = 10 - 0.106103 = 9.893897$ mm, as imposed in step 2. Putting $D_i = 1.453$ mm back in the formula:

$$HB = \frac{2\times500}{\pi\times10\times\left(10 - 9.893897\right)} = \frac{1000}{\pi\times10\times0.106103} = 300.00$$

which recovers the 300 of the statement.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $k$ is a length (kg over kgf/mm² gives mm² and, divided by mm, a length); $D_i^2 = k(2D-k)$ is in mm².
- **Load factor.** $Q = P/D^2 = 500/10^2 = 5$, a standard value of [Session 12 Slide 20] for the ball of 10 mm.
- **Limit.** Since $k \ll D$ here, $D_i^2 \approx 2Dk = 4P/(\pi\,HB)$, so $D_i \approx \sqrt{4\times500/(\pi\times300)} = 1.4567$ mm: the approximation is within 0.3 % of the exact value (1.4529 mm).
- **Direction.** A harder material (larger $HB$) leaves a smaller indentation under the same load: $D_i \propto HB^{-1/2}$ for small indentations.

### Interpretation
A hardness of 300 HB under 500 kg leaves an indentation of only about 1.45 mm in a ball of 10 mm, with a depth of $h = k/2 = 0.05305$ mm. The ratio $D_i/D = 0.145$ is a very small indentation, which is difficult to measure accurately with a microscope (extension: the usual range of validity of the Brinell test is $0.25D$ to $0.6D$, a rule that is not in the slides).

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| indentation diameter | 1.453 mm | 1.4529 mm | agrees (the key rounds to three decimals) |

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Hardness Tests Mohs Brinell Rockwell Vickers]]
