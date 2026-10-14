---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 1"
dificultad: medium
tags:
  - official-problem
  - solved
  - lever-rule
  - tie-line
  - solubility-limit
---

# ✏️ Problem: T4-PD01 — Phase Limits from the Phase Fractions of Two Alloys

## 📄 Official Statement
> **1. In the phase diagram of two hypothetic metals, A and B, there is a phase α rich in A and a phase β rich in B. Given the mass fraction of two alloys for a specific temperature (table), determine the composition of the phase limits (or solid solubility limits) of the α and β phases at such temperature.**
>
> | Alloy composition | Fraction of α phase | Fraction of β phase |
> | :---: | :---: | :---: |
> | 30% B | 0.78 | 0.22 |
> | 65% B | 0.36 | 0.64 |
>
> *(Solution: $C_\alpha = 11.7\%$, $C_\beta = 95\%$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium:** both alloys are at the same temperature, in equilibrium, and both contain α and β only, so both lie in the α + β two-phase region [Session 7 Slide 26].
2. **One tie line:** at a fixed temperature and pressure, a two-component, two-phase system has $F = C - P + 1 = 2 - 2 + 1 = 1$ degree of freedom, already used by the temperature [Session 7 Slide 13]. The compositions of α and β are therefore the same for both alloys: $C_\alpha$ and $C_\beta$ are the two ends of one tie line.
3. **Mass fractions** obey the lever rule [Session 7 Slide 16].

### Data
| Quantity | Alloy 1 | Alloy 2 |
| :--- | ---: | ---: |
| Overall composition $C_0$ (% B) | 30 | 65 |
| $W_\alpha$ | 0.78 | 0.36 |
| $W_\beta$ | 0.22 | 0.64 |

**Unknowns:** $C_\alpha$ and $C_\beta$ (% B). Two unknowns and two independent equations (one per alloy; $W_\beta = 1 - W_\alpha$ adds nothing new).

---

## 🧠 2. Phase 2: Frames and Change of Basis

The only frame is the phase diagram itself: composition in % B along the horizontal axis and temperature along the vertical axis. All the work is done on one horizontal line (the tie line at the given temperature), so it is one-dimensional and no change of basis is involved.

**Why the lever rule.** It is the tool that relates the amounts of the phases to the positions of the alloy and of the phase limits on the tie line [Session 7 Slide 16]:

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha}$$

Writing it once for each alloy gives two linear equations in $C_\alpha$ and $C_\beta$.

![[attachments/T4/pd-p1.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. The two equations
Call $D = C_\beta - C_\alpha$ the length of the tie line. Multiplying the lever rule by $D$:

$$W_\alpha D = C_\beta - C_0$$

Alloy 1 ($C_0 = 30$, $W_\alpha = 0.78$) and alloy 2 ($C_0 = 65$, $W_\alpha = 0.36$):

$$0.78\,D = C_\beta - 30 \qquad (1)$$
$$0.36\,D = C_\beta - 65 \qquad (2)$$

### 2. Length of the tie line
Subtracting (2) from (1) eliminates $C_\beta$:

$$0.78\,D - 0.36\,D = (C_\beta - 30) - (C_\beta - 65) \;\Rightarrow\; 0.42\,D = 35 \;\Rightarrow\; D = \frac{35}{0.42} = 83.33\ \%\text{B}$$

### 3. Limit of β
From (1):

$$C_\beta = 30 + 0.78 \times 83.33 = 30 + 65.00 = 95.0\ \%\text{B}$$

### 4. Limit of α

$$C_\alpha = C_\beta - D = 95.0 - 83.33 = 11.67 \approx 11.7\ \%\text{B}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **β fractions** (not used in the solution): $W_\beta = \dfrac{C_0 - C_\alpha}{C_\beta - C_\alpha}$ gives $\dfrac{30 - 11.67}{83.33} = 0.22$ and $\dfrac{65 - 11.67}{83.33} = 0.64$, exactly the values of the table.
- **Mass balance of B** for alloy 1: $0.78 \times 11.67 + 0.22 \times 95.0 = 9.10 + 20.90 = 30.0\ \%$B $= C_0$.
- **Order:** $C_\alpha = 11.7 < 30 < 65 < 95 = C_\beta$, so both alloys are indeed inside the α + β region, as assumed.
- **Units:** all compositions are in % B (mass), fractions are dimensionless; each equation is homogeneous in % B.

### Interpretation
At this temperature α can dissolve at most 11.7 % B and β at most 5 % A (95 % B). The alloy closer to the α limit (30 % B) has more α, as the lever rule predicts.

## ✅ Check against the official solution
The official solution gives $C_\alpha = 11.7\%$ and $C_\beta = 95\%$; the result agrees. The official solutions PDF has no worked page for this problem; only the key of the statement is available.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Tie Line and Lever Rule]]
* [[Concept - Gibbs Phase Rule]]
