---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 9"
dificultad: hard
tags:
  - official-problem
  - solved
  - invariant-reactions
  - intermetallic-compounds
  - lever-rule
  - al-ni
---

# ✏️ Problem: T4-PD09 — Invariant Reactions and an Al-20 wt% Ni Alloy

## 📄 Official Statement
> **9. Given the Al-Ni phase diagram, answer the questions below. a. What is the maximum solubility of aluminum in solid state nickel? What about nickel in aluminum? b. Write down the invariant reactions, indicating the temperature, the reaction in equation form, the composition of each phase and the name of the reaction. c. Given an Al-20% Ni alloy, indicate at 400 °C: composition and mass fraction of the phases; composition and mass fraction of the microconstituents; draw the microstructure that can be expected when cooling in equilibrium conditions. Point out each microconstituent with arrows.**
>
> ![[attachments/T4/pd-p9-alni.png]]
>
> *(Solution: a) 10%Al; 1%Ni. b) eutectic reaction (639 °C; 1380 °C); peritectoid reaction (700 °C); peritectic reaction (854 °C; 1133 °C, 1400 °C). c) $C_{Al_3Ni}$ = 43%Cu; $C_\alpha$ = 1%Cu; $X_\alpha$ = 0.55; $X_{Al_3Ni}$ = 0.45; Microconstituents: eutectic (X = 0.64) and proeutectic $Al_3Ni$ (X = 0.36))*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium** and the Al-Ni diagram of the sheet (weight percent nickel). Every composition and temperature below is a **reading of the figure**, to about ±1 wt% and ±10 °C, except the temperatures printed on it (639.9, 854, 1133, ~700, 1638 °C).
2. **Invariant reactions** are the horizontal lines where three phases meet ($F = 2 - 3 + 1 = 0$) [Session 7 Slide 13; Session 8 Slide 6]; their type follows from the shape around the line (V above: eutectic; inverted V below: peritectic or peritectoid) [Session 8 Slide 6].
3. **Al₃Ni** is drawn as a vertical line (stoichiometric compound) at about 42 wt% Ni [Session 8 Slide 15].
4. The (Al) phase is the very thin field along the left axis; its solubility limit is about 1 wt% Ni at most.

### Data read on the diagram
| Point | Reading |
| :--- | :--- |
| Eutectic at 639.9 °C | L ≈ 6 wt% Ni, (Al) ≈ 1 wt% Ni, Al₃Ni ≈ 42 wt% Ni |
| (Al) at 400 °C | ≈ 1 wt% Ni |
| (Ni) at its widest | ≈ 90 wt% Ni, i.e. ≈ 10 wt% Al |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Al-Ni diagram (wt% Ni, °C). Each question is answered on horizontal lines (tie lines and invariant lines), so the work is one-dimensional and no change of basis is needed.

**Strategy.** (a) Maximum solubility = the widest point of each terminal solid solution. (b) Scan the diagram from the bottom up for horizontal lines and name each reaction by its shape. (c) Lever rule on the (Al)-Al₃Ni tie line for the phases, and on the short tie line from the eutectic liquid to Al₃Ni (just above 639.9 °C) for the microconstituents [Session 7 Slide 32].

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Maximum solubilities
- **Al in solid Ni:** the (Ni) field is widest at its horizontal line near 1385 °C, at about 90 wt% Ni: about **10 wt% Al**.
- **Ni in solid Al:** the (Al) field is widest at the eutectic temperature, 639.9 °C, at about **1 wt% Ni** (the field is too thin to read more precisely).

### b) Invariant reactions (on cooling)
| T (°C) | Reaction | Name |
| :--- | :--- | :--- |
| 639.9 | $L\,(6) \rightarrow (\text{Al})\,(1) + \text{Al}_3\text{Ni}\,(42)$ | eutectic |
| ~700 | $\text{AlNi}\,(76) + \text{AlNi}_3\,(86) \rightarrow \text{Al}_3\text{Ni}_5\,(81)$ | peritectoid |
| 854 | $L\,(28) + \text{Al}_3\text{Ni}_2\,(56) \rightarrow \text{Al}_3\text{Ni}\,(42)$ | peritectic |
| 1133 | $L\,(44) + \text{AlNi}\,(61) \rightarrow \text{Al}_3\text{Ni}_2\,(59)$ | peritectic |
| ≈1395 | $L\,(86.5) + \text{AlNi}\,(83) \rightarrow \text{AlNi}_3\,(86)$ | peritectic |
| ≈1385 | $L\,(86.5) \rightarrow \text{AlNi}_3\,(86) + (\text{Ni})\,(90)$ | eutectic |

(compositions in wt% Ni, readings of the figure). The two reactions near 1390 °C are only a few degrees and a few percent apart; the key gives them as 1400 °C (peritectic) and 1380 °C (eutectic).

### c) Al-20 wt% Ni at 400 °C
**Phases.** (Al) of about 1 wt% Ni and Al₃Ni of 42 wt% Ni (tie line length $42 - 1 = 41$):

$$W_{(\text{Al})} = \frac{C_{\text{Al}_3\text{Ni}} - C_0}{C_{\text{Al}_3\text{Ni}} - C_{(\text{Al})}} = \frac{42 - 20}{42 - 1} = \frac{22}{41} = 0.537 \qquad W_{\text{Al}_3\text{Ni}} = \frac{20 - 1}{41} = \frac{19}{41} = 0.463$$

**Microconstituents.** $6 < 20 < 42$: the alloy is **hypereutectic** with respect to the 639.9 °C eutectic, so Al₃Ni forms first (primary, proeutectic) and the remaining liquid of 6 wt% Ni becomes eutectic. Just above 639.9 °C (tie line from 6 to 42, length 36):

$$W_{\text{Al}_3\text{Ni},p} = \frac{C_0 - C_e}{C_{\text{Al}_3\text{Ni}} - C_e} = \frac{20 - 6}{42 - 6} = \frac{14}{36} = 0.389 \qquad W_E = \frac{42 - 20}{36} = \frac{22}{36} = 0.611$$

The microconstituents keep these amounts on cooling to 400 °C (Al₃Ni has a fixed composition and the (Al) solvus barely moves).

![[attachments/T4/pd-micro-p9.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- Mass balance at 400 °C: $0.537 \times 1 + 0.463 \times 42 = 0.54 + 19.45 = 20.0$ wt% Ni.
- All the (Al) is inside the eutectic: $W_{(\text{Al})} = 0.537 < W_E = 0.611$, and the rest of the eutectic, $0.611 - 0.537 = 0.074$, is eutectic Al₃Ni; total Al₃Ni $= 0.389 + 0.074 = 0.463$ ✓.
- **Limiting cases** (fractions dimensionless, compositions in % Ni): at $C_0 \approx 6$ (the eutectic) the alloy would be all eutectic and at $C_0 = 42$ all primary Al₃Ni; 20 % Ni lies nearer the eutectic end, hence most of the alloy (0.61) is eutectic.

### Interpretation
The alloy is mostly eutectic of soft (Al) with about 39 % of hard Al₃Ni crystals that grew from the liquid between about 800 °C (liquidus at 20 wt% Ni, reading) and 639.9 °C. The Ni-rich side of the diagram is crowded with intermetallic compounds formed by peritectic and peritectoid reactions.

## ✅ Check against the official solution
Parts (a) and (b) agree with the key (10 % Al, 1 % Ni; eutectics at 639.9 and ~1380 °C, peritectoid at ~700 °C, peritectics at 854, 1133 and ~1400 °C). The key writes the compositions of part (c) as "%Cu"; they are wt% Ni.

> [!warning] Discrepancy with the official solution
> For part (c) the key uses $C_{\text{Al}_3\text{Ni}} = 43$ % (its eutectic liquid is not stated; the key's eutectic fraction 0.64 implies about 7 % Ni), and gives $X_\alpha = 0.55$, $X_{\text{Al}_3\text{Ni}} = 0.45$, eutectic 0.64 and primary Al₃Ni 0.36. The figure places the Al₃Ni line at about 42 % and the eutectic point at about 6 % Ni, which give 0.537/0.463 and 0.611/0.389. With the key's readings the same formulas give $(43 - 20)/(43 - 1) = 23/42 = 0.548$ for (Al) and $(43 - 20)/(43 - 7) = 23/36 = 0.64$ for the eutectic: the difference comes only from the readings, which are within the precision of the drawing. The values read here are kept.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Invariant Reactions in Binary Systems]]
* [[Concept - Intermetallic Compounds and Congruent Melting]]
* [[Concept - Tie Line and Lever Rule]]
