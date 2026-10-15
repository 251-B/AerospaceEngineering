---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 10"
dificultad: hard
tags:
  - official-problem
  - solved
  - invariant-reactions
  - eutectoid
  - peritectic
  - lever-rule
  - cu-sn
---

# ✏️ Problem: T4-PD10 — Reactions and Eutectoids in the Cu-Sn System

## 📄 Official Statement
> **10. Considering the Cu-Sn phase diagram: a. Indicate the type of transformations, and write the reactions that take place at $T_1$ = 798 °C; $T_2$ = 755 °C; $T_3$ = 588 °C; $T_4$ = 415 °C; $T_5$ = 1084.87 °C. b. For a Cu-20%Sn alloy, indicate the phases and microconstituents, their composition and amount at $T_1$: 521 °C and $T_2$: 519 °C. c. Determine the percentage of Sn in an alloy having 54% liquid phase at 900 °C. Is this alloy in solid state at 700 °C?**
>
> ![[attachments/T4/pd-p10-cusn.png]]
>
> *(Solution: a) peritectic; peritectic, eutectoid; peritectic and solidification of Cu. b) 521 °C: $C_{(Cu)}$ = 15.8%Sn; $C_\gamma$ = 27%Sn; $X_\gamma$ = 0.37; $X_{(Cu)}$ = 0.63; X(eutectoid): 0.48; X(proeutectoid Cu): 0.52. 519 °C: $C_{(Cu)}$ = 15.8%Sn; $C_\delta$ = 32%Sn; $X_\delta$ = 0.26; $X_{(Cu)}$ = 0.74; X(eutectoid): 0.37 and X(proeutectoid Cu): 0.63. c) 14.5%Sn)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium**, Cu-Sn diagram of the sheet (wt% Sn). Printed values: 798 °C with 13.5, 22 and 25.5 wt% Sn; 755 °C with 30.6; 586 °C with 24.6; 520 °C with 15.8 and 27.0; 415 °C with 59 and 92.4. The rest are **readings of the figure** (±1 wt%).
2. The statement's 588 °C is the 586 °C line of the diagram.
3. The type of each reaction follows from its shape [Session 8 Slide 6].

### Data
| Line | Phases and compositions (wt% Sn) |
| :--- | :--- |
| 798 °C | (Cu) 13.5, β 22, L 25.5 |
| 755 °C | β ≈ 24, γ ≈ 25.5, L 30.6 |
| 586 °C | (Cu) 15.8, β 24.6, γ ≈ 25.5 |
| 520 °C | (Cu) 15.8, γ 27.0, δ ≈ 32 |
| 415 °C | ε ≈ 38, η 59, L 92.4 |
| 900 °C | (Cu) ≈ 9, L ≈ 19 (on the solidus and liquidus) |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Cu-Sn diagram (wt% Sn, °C); all the work is on horizontal lines, so no change of basis is needed.

**Strategy.** (a) Name each line by its shape. (b) Lever rule on the tie lines just above and just below 520 °C; the microconstituents come from the history of the alloy (it crosses 798, 586 and 520 °C). (c) Write the lever rule for the liquid at 900 °C and solve it for $C_0$.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Transformations
| T | Reaction on cooling | Type |
| :--- | :--- | :--- |
| $T_1$ = 798 °C | $(\text{Cu})\,(13.5) + L\,(25.5) \rightarrow \beta\,(22)$ | peritectic |
| $T_2$ = 755 °C | $\beta\,(\approx 24) + L\,(30.6) \rightarrow \gamma\,(\approx 25.5)$ | peritectic |
| $T_3$ = 586 °C | $\beta\,(24.6) \rightarrow (\text{Cu})\,(15.8) + \gamma\,(\approx 25.5)$ | eutectoid |
| $T_4$ = 415 °C | $\varepsilon\,(\approx 38) + L\,(92.4) \rightarrow \eta\,(59)$ | peritectic |
| $T_5$ = 1084.87 °C | $L \rightarrow (\text{Cu})$ for pure Cu | solidification of a pure metal |

### b) Cu-20 wt% Sn
**History.** $13.5 < 20 < 22$: at 798 °C the peritectic consumes all the liquid and leaves (Cu) + β. On cooling, β is transformed at 586 °C by the eutectoid into (Cu) + γ, and γ at 520 °C by a second eutectoid into (Cu) + δ.

**Just above 586 °C** ((Cu) 15.8, β 24.6; length 8.8):
$$W_\beta = \frac{20 - 15.8}{24.6 - 15.8} = \frac{4.2}{8.8} = 0.477 \qquad W_{(\text{Cu})} = \frac{24.6 - 20}{8.8} = \frac{4.6}{8.8} = 0.523$$
This (Cu) is **proeutectoid**, and this β becomes the **eutectoid** microconstituent at 586 °C.

**At 521 °C (phases)**, (Cu) 15.8 and γ 27.0 (length 11.2):
$$W_\gamma = \frac{20 - 15.8}{27.0 - 15.8} = \frac{4.2}{11.2} = 0.375 \qquad W_{(\text{Cu})} = \frac{27.0 - 20}{11.2} = \frac{7.0}{11.2} = 0.625$$
**Microconstituents at 521 °C:** proeutectoid (Cu) 0.523 and eutectoid [(Cu) + γ] 0.477.

**At 519 °C (phases)**, below the 520 °C eutectoid $\gamma\,(27.0) \rightarrow (\text{Cu})\,(15.8) + \delta\,(32)$; (Cu) 15.8 and δ ≈ 32 (length 16.2):
$$W_\delta = \frac{20 - 15.8}{32 - 15.8} = \frac{4.2}{16.2} = 0.259 \qquad W_{(\text{Cu})} = \frac{32 - 20}{16.2} = \frac{12}{16.2} = 0.741$$
**Microconstituents at 519 °C, counted with respect to the 520 °C reaction:** the γ present at 521 °C (0.375) becomes eutectoid [(Cu) + δ], and all the (Cu) that existed before (0.625) counts as proeutectoid. That (Cu) is made of the proeutectoid (Cu) of 586 °C (0.523) plus the (Cu) of the first eutectoid ($0.625 - 0.523 = 0.102$).

### c) Alloy with 54 % liquid at 900 °C
At 900 °C the tie line goes from (Cu) at $C_S \approx 9$ to L at $C_L \approx 19$ wt% Sn (readings). The lever rule for the liquid:
$$W_L = \frac{C_0 - C_S}{C_L - C_S} \;\Rightarrow\; C_0 = C_S + W_L\,(C_L - C_S) = 9 + 0.54 \times (19 - 9) = 9 + 5.4 = 14.4\ \text{wt\% Sn}$$

**Solid at 700 °C?** $13.5 < 14.4 < 22$, so at 798 °C the peritectic uses up all the liquid: below 798 °C the alloy is (Cu) + β, both solid. At 700 °C the (Cu) boundary is at about 14.5 wt% Sn (it goes from 13.5 at 798 °C to 15.8 at 586 °C), so the alloy (14.4) is (Cu), practically single-phase. The key gives 14.5 wt% Sn; the 0.1 difference is well within the ±1 wt% of the readings and does not change the answer. **Yes, it is solid at 700 °C.**

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- 519 °C: $0.741 \times 15.8 + 0.259 \times 32 = 11.71 + 8.29 = 20.0$ wt% Sn.
- 521 °C: $0.625 \times 15.8 + 0.375 \times 27.0 = 9.88 + 10.13 = 20.0$ wt% Sn.
- (c): with $C_0 = 14.4$, $W_L = (14.4 - 9)/(19 - 9) = 0.54$ ✓.
- **Limiting cases** (fractions dimensionless, compositions in wt% Sn): in (c), $W_L \to 0$ as $C_0 \to C_S = 9$ and $W_L \to 1$ as $C_0 \to C_L = 19$; 14.4 lies a little past the middle of the tie line, consistent with 0.54 of liquid.

### Interpretation
The Cu-rich side of Cu-Sn (bronzes) shows how one alloy can cross several invariant reactions: a peritectic during solidification and two eutectoids in the solid. Each eutectoid turns a single solid phase into a fine two-phase mixture.

## ✅ Check against the official solution
All values agree with the key: 0.37/0.63 and 0.48/0.52 at 521 °C; 0.26/0.74 and 0.37/0.63 at 519 °C (the key counts microconstituents with respect to the 520 °C reaction, as explained in part b); 14.5 % Sn. The key's part (c) does not answer the question about 700 °C.

> [!warning] Erratum in the worked solution
> The annotated diagram of Solution problems Phase diagrams I.pdf, p. 35, labels the field above the liquidus at about 50 % Sn and 900 °C as "(Cu)+ε"; that field is the liquid L, as the sheet's own diagram shows.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Invariant Reactions in Binary Systems]]
* [[Concept - Tie Line and Lever Rule]]
