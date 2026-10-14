---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 13"
dificultad: hard
tags:
  - official-problem
  - solved
  - congruent-melting
  - invariant-reactions
  - lever-rule
  - ti-si
---

# ✏️ Problem: T4-PD13 — Compounds and Cooling of a Ti-30 % Si Alloy

## 📄 Official Statement
> **13. Given the following Ti-Si phase diagram answer the next questions: a) Indicate the phases or compounds with incongruent and congruent melting. b) Write down the invariant reactions, specifying their name, temperature, and composition of the phases present. c) For an alloy with 30% Si describe the solidification and cooling sequence to 600 °C. Describe specifically the microstructure that can be expected at 1329 °C, 1169 °C, and 600 °C. d) For the same alloy of part c) and the temperatures of 1329 °C and 1169 °C indicate phase composition, phase fractions and quantity of microconstituents present.**
>
> ![[attachments/T4/pd-p13-tisi.png]]
>
> *(Solution: a) congruent melting: Ti₅Si₃ and TiSi₂; incongruent melting: Ti₃Si, Ti₅Si₄ and TiSi. b) Eutectic, T = 1330 °C; Eutectic, T = 1330 °C; Eutectic, T = 1480 °C; Peritectic, T = 1920 °C; Peritectic, T = 1570 °C; Peritectoid T = 1170 °C; Eutectoid, T = 865 °C. c) T = 1329 °C: $C_{\beta Ti}$ = 5.5% Si and $C_{Ti_5Si_3}$ = 35% Si, $x_{\beta Ti}$ = 0.17, $x_{Ti_5Si_3}$ = 0.83; T = 1169 °C: $C_{Ti_3Si}$ = 25% Si and $C_{Ti_5Si_3}$ = 35% Si, $x_{Ti_5Si_3}$ = 0.5, $x_{Ti_3Si}$ = 0.5. d) T = 1329 °C: $x_{eutectic}$ = 0.24, $x_{Ti_5Si_3,primary}$ = 0.76; T = 1169 °C phases and microconstituents are the same)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium**, Ti-Si diagram of the sheet. Printed temperatures: 1670, 1414, 2130, 1920, 1570, 1480, 1330 (twice), 1170 and 865 °C. Compositions are **readings of the figure** (±1 %), on the axis as printed.
2. The axis is labelled "% wt Silicon", but the compounds sit at 25 (Ti₃Si), 37.5 (Ti₅Si₃), 44.4 (Ti₅Si₄), 50 (TiSi) and 66.7 (TiSi₂), their **atomic** percentages of Si; the numbers below are read on the axis as printed, as the key does.
3. Melting is congruent at a maximum of the liquidus and incongruent at a peritectic line [Session 8 Slide 17].

### Data read on the diagram
| Line | Phases (% Si) |
| :--- | :--- |
| 1330 °C (Ti side) | βTi ≈ 5.5, L ≈ 14, Ti₅Si₃ ≈ 35 |
| 1170 °C | βTi ≈ 4, Ti₃Si 25, Ti₅Si₃ ≈ 35 |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Ti-Si diagram (% Si, °C); all the work is on horizontal lines and the vertical line of the alloy, so no change of basis is needed. Reactions are named by their shape [Session 8 Slide 6], amounts by the lever rule [Session 7 Slides 16, 32].

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Congruent and incongruent melting
- **Congruent:** Ti₅Si₃ (top of the large dome, 2130 °C) and TiSi₂ (small maximum near 1500 °C).
- **Incongruent:** Ti₅Si₄ and TiSi end at peritectic lines (1920 and 1570 °C), and Ti₃Si at the peritectoid line (1170 °C): on heating each decomposes into another phase plus liquid (or, for Ti₃Si, into two solids).

### b) Invariant reactions (on cooling, % Si read on the axis)
| T (°C) | Reaction | Type |
| :--- | :--- | :--- |
| 1920 | $L\,(\approx 48) + \text{Ti}_5\text{Si}_3\,(\approx 38) \rightarrow \text{Ti}_5\text{Si}_4\,(\approx 44)$ | peritectic |
| 1570 | $L\,(\approx 59) + \text{Ti}_5\text{Si}_4\,(\approx 44) \rightarrow \text{TiSi}\,(50)$ | peritectic |
| 1480 | $L\,(\approx 64) \rightarrow \text{TiSi}\,(50) + \text{TiSi}_2\,(\approx 67)$ | eutectic |
| 1330 | $L\,(\approx 14) \rightarrow \beta\text{Ti}\,(\approx 5.5) + \text{Ti}_5\text{Si}_3\,(\approx 35)$ | eutectic |
| 1330 | $L\,(\approx 84) \rightarrow \text{TiSi}_2\,(\approx 67) + (\text{Si})\,(\approx 100)$ | eutectic |
| 1170 | $\beta\text{Ti}\,(\approx 4) + \text{Ti}_5\text{Si}_3\,(\approx 35) \rightarrow \text{Ti}_3\text{Si}\,(25)$ | peritectoid |
| 865 | $\beta\text{Ti}\,(\approx 1) \rightarrow \alpha\text{Ti}\,(\approx 0.5) + \text{Ti}_3\text{Si}\,(25)$ | eutectoid |

### c) Cooling of Ti-30 % Si to 600 °C
1. Liquid down to the liquidus of Ti₅Si₃ (roughly 1950 °C, a reading); there **primary Ti₅Si₃** starts to crystallise.
2. L + Ti₅Si₃ down to 1330 °C; the liquid becomes poorer in Si along the liquidus and reaches 14 % Si.
3. At 1330 °C the remaining liquid gives the **eutectic** βTi + Ti₅Si₃.
4. Between 1330 and 1170 °C: primary Ti₅Si₃ in a eutectic of βTi + Ti₅Si₃.
5. At 1170 °C the **peritectoid** βTi + Ti₅Si₃ → Ti₃Si uses up all the βTi (the alloy, 30 %, lies between Ti₃Si, 25 %, and Ti₅Si₃, 35 %), so below it the alloy is **Ti₃Si + Ti₅Si₃**.
6. No other line is crossed down to 600 °C; the boundaries of both compounds are vertical, so nothing changes.

**At 1329 °C** (βTi 5.5 / Ti₅Si₃ 35, length 29.5):
$$x_{\beta\text{Ti}} = \frac{35 - 30}{35 - 5.5} = \frac{5}{29.5} = 0.17 \qquad x_{\text{Ti}_5\text{Si}_3} = \frac{30 - 5.5}{29.5} = \frac{24.5}{29.5} = 0.83$$

**At 1169 °C and at 600 °C** (Ti₃Si 25 / Ti₅Si₃ 35, length 10):
$$x_{\text{Ti}_3\text{Si}} = \frac{35 - 30}{35 - 25} = \frac{5}{10} = 0.5 \qquad x_{\text{Ti}_5\text{Si}_3} = \frac{30 - 25}{10} = 0.5$$

### d) Microconstituents
**At 1329 °C:** primary Ti₅Si₃ and eutectic. Short tie line from the eutectic liquid (14) to Ti₅Si₃ (35), length 21:
$$x_{\text{Ti}_5\text{Si}_3,p} = \frac{30 - 14}{35 - 14} = \frac{16}{21} = 0.76 \qquad x_E = \frac{35 - 30}{21} = \frac{5}{21} = 0.24$$

**At 1169 °C:** the peritectoid has turned the βTi (which was inside the eutectic) and part of the Ti₅Si₃ into Ti₃Si; the structure is Ti₃Si and Ti₅Si₃, in the same amounts as the phases, 0.5 and 0.5.

![[attachments/T4/pd-micro-p13.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- 1329 °C: $0.17 \times 5.5 + 0.83 \times 35 = 0.94 + 29.06 = 30.0$ % Si.
- 1169 °C: $0.5 \times 25 + 0.5 \times 35 = 30$ % Si.
- Eutectic at 1329 °C: it holds all the βTi (0.17) and Ti₅Si₃ $0.83 - 0.76 = 0.07$; $0.17 + 0.07 = 0.24 = x_E$ ✓.

### Interpretation
The Ti-rich side combines a eutectic, a peritectoid and a eutectoid. The 30 % alloy ends up made only of two silicides, which are hard and brittle compounds.

## ✅ Check against the official solution
All values agree with the key (0.17/0.83, 0.5/0.5, 0.24/0.76; the classification of the compounds and the seven reactions).

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Intermetallic Compounds and Congruent Melting]]
* [[Concept - Invariant Reactions in Binary Systems]]
