---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 11"
dificultad: hard
tags:
  - official-problem
  - solved
  - phase-diagram-construction
  - intermetallic-compounds
  - eutectic
  - peritectic
---

# ✏️ Problem: T4-PD11 — Drawing a Diagram with a Stoichiometric Compound

## 📄 Official Statement
> **11. Draw the hypothetic phase diagram of A and B from the following data. a) Melting temperatures: A = 850 °C; B = 350 °C. b) A and B form an stoichiometric compound AB₂ that melts at 1000 °C; neither A nor B are soluble in the compound. c) There is an invariant eutectic point (70% at. of A, 700 °C). d) There is an invariant peritectic point (80% at. of B, 500 °C). e) The composition of the liquid at 500 °C is 95% at. of B. f) The solubility of B in A is 10% at. at 700 °C and 2% at. at 25 °C. g) The solubility of A in B is 25 % at. at 25 °C. Connect the points with straight lines. Indicate all the phase areas and points in the diagram, and write the reactions of the three phases.**
>
> *(Solution: not given in the sheet)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. Compositions in **atomic percent of B** (at.% B) on the horizontal axis; straight lines between the given points, as the statement asks.
2. **AB₂** contains two B atoms per A atom: $x_B = 2/3 = 66.7$ at.% B. It is stoichiometric and dissolves neither A nor B, so it is a **vertical line** [Session 8 Slide 15]; it melts at 1000 °C as a single phase, so it melts **congruently** (a maximum of the liquidus) [Session 8 Slide 17].
3. The terminal solid solutions are α (B dissolved in A) and β (A dissolved in B).
4. "80 % at. of B" for the peritectic point is the composition of the solid β formed there; the liquid at 500 °C has 95 at.% B (point e).

### Points
| Point | at.% B | T (°C) |
| :--- | ---: | ---: |
| Melting point of A | 0 | 850 |
| Melting point of B | 100 | 350 |
| AB₂ (congruent melting) | 66.7 | 1000 |
| Eutectic E (liquid) | 30 | 700 |
| α at E (max. solubility of B in A) | 10 | 700 |
| α at 25 °C | 2 | 25 |
| Peritectic P (β formed) | 80 | 500 |
| Liquid at 500 °C | 95 | 500 |
| β at 25 °C (25 at.% A) | 75 | 25 |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: composition (at.% B) against temperature (°C). The diagram is built from straight segments between the points; no change of basis is involved.

**How the points connect.**
- Left part (A to AB₂): a **eutectic** system between α and AB₂ [Session 7 Slide 26]: liquidus from A (0, 850) to E (30, 700) and from E up to AB₂ (66.7, 1000); α solidus from (0, 850) to (10, 700); eutectic line from α (10) to AB₂ (66.7) at 700 °C; α solvus from (10, 700) to (2, 25).
- Right part (AB₂ to B): a **peritectic** system [Session 8 Slide 8]: liquidus from AB₂ (66.7, 1000) down to (95, 500) and then to B (100, 350); peritectic line from AB₂ (66.7) to L (95) at 500 °C, with β (80) on it; β solidus from (80, 500) to B (100, 350); β solvus from (80, 500) to (75, 25).

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### The diagram

![[attachments/T4/pd-p11.svg]]

### Phase areas
| Region | Bounded by |
| :--- | :--- |
| L | above the liquidus |
| α + L | 0-30 at.% B, between 850 and 700 °C |
| α | left of the α solidus and solvus |
| α + AB₂ | 10-66.7 at.% B, below 700 °C |
| L + AB₂ (left) | 30-66.7 at.% B, between 700 °C and the liquidus |
| L + AB₂ (right) | 66.7-95 at.% B, between 500 °C and the liquidus |
| AB₂ + β | 66.7 at.% B to the β solvus, below 500 °C |
| L + β | between the β solidus (80 → 100) and the liquidus (95 → 100), from 500 to 350 °C |
| β | right of the β solidus and solvus |

### Reactions of three phases (on cooling)
- **Eutectic, 700 °C:** $L\,(30\ \text{at.\% B}) \rightarrow \alpha\,(10\ \text{at.\% B}) + \text{AB}_2\,(66.7\ \text{at.\% B})$
- **Peritectic, 500 °C:** $\text{AB}_2\,(66.7\ \text{at.\% B}) + L\,(95\ \text{at.\% B}) \rightarrow \beta\,(80\ \text{at.\% B})$

AB₂ melting at 1000 °C involves only two phases (AB₂ and a liquid of the same composition), so it is not a three-phase reaction.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- Each three-phase line has the middle phase in the right place: at 700 °C the liquid (30) lies **between** the two solids (10 and 66.7), the shape of a eutectic; at 500 °C the new solid β (80) lies between AB₂ (66.7) and L (95), with the liquid at one end, the shape of a peritectic [Session 8 Slide 6].
- Phase rule: on each horizontal line three phases coexist, $F = 2 - 3 + 1 = 0$; in each two-phase area $F = 1$ [Session 7 Slide 13].
- **Limiting case** (compositions in the units of the statement): at the composition of the stoichiometric compound the alloy is a single phase, so every lever-rule fraction there is 0 or 1; this is why the compound is drawn as a vertical line.

### Interpretation
The compound AB₂ splits the diagram into two simpler diagrams, A-AB₂ (eutectic) and AB₂-B (peritectic). Since B melts at only 350 °C, the liquid persists to low temperatures on the B side, and β forms from AB₂ and the B-rich liquid at 500 °C.

## ✅ Check against the official solution
The sheet gives no solution for this problem and the official solutions PDF has no page for it, so there is nothing to compare with.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Invariant Reactions in Binary Systems]]
* [[Concept - Intermetallic Compounds and Congruent Melting]]
* [[Problem - T4-PD08 Drawing a Eutectic Diagram and the 40 B Alloy]]
