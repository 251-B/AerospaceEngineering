---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 15"
dificultad: hard
tags:
  - official-problem
  - solved
  - invariant-reactions
  - congruent-melting
  - lever-rule
  - ti-b
---

# ✏️ Problem: T4-PD15 — The Ti-B System and Ti-10 % B and Ti-18 % B Alloys

## 📄 Official Statement
> **15. Given the phase diagram of the figure, answer the following questions: a. Write down the invariant reactions, indicating the name, temperature and composition of the phases involved. b. List the congruent and incongruent melting phases or compounds. c. For an alloy with 10% B, indicate the composition of the phases, the amount of phases and the amount of microconstituents at 1000 °C and 500 °C. d. Describe the solidification sequence of an alloy with 18% B at a very slow cooling from the liquid state up to 500 °C.**
>
> ![[attachments/T4/pd-p15-tib.png]]
>
> *(Solution: a) peritectic (2200 °C); peritectic (2190 °C); eutectic (1540 °C); eutectic (2080 °C). b) Ti₃B₄ → L + TiB₂. c) 1000 °C: $C_{(\beta Ti)}$ = 0%B; $C_{TiB}$ = 18%B; $X_{(\beta Ti)}$ = 0.44; $X_{(TiB)}$ = 0.56; eutectic (x = 50%) and primary TiB (x = 50%). 500 °C: $C_{(\alpha Ti)}$ = 0%B; $C_{TiB}$ = 18%B; $X_{(\alpha Ti)}$ = 0.44; $X_{(TiB)}$ = 0.56; eutectic (x = 50%) and primary TiB (x = 50%))*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium**, Ti-B diagram of the sheet, read on its **weight percent** scale (bottom axis). Printed values: 1540, 884, ~2200, 2080, 3225 and 2092 °C. Compositions are **readings of the figure** (±1 wt%).
2. Boron is practically insoluble in Ti: (βTi) and (αTi) are taken as 0 wt% B, as the key does.
3. TiB, Ti₃B₄ and TiB₂ are compounds (Slide 15 of Session 8 shows the same system on the atomic scale).

### Data read on the diagram
| Line | Phases (wt% B) |
| :--- | :--- |
| 1540 °C eutectic | (βTi) ≈ 0, L ≈ 2, TiB ≈ 18 |
| ~2200 °C | L ≈ 13, Ti₃B₄ ≈ 24, TiB₂ ≈ 31 |
| ~2190 °C | L ≈ 13, TiB ≈ 18, Ti₃B₄ ≈ 24 |
| 2080 °C eutectic | TiB₂ ≈ 31, L ≈ 94, (βB) ≈ 100 |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Ti-B diagram (wt% B, °C); horizontal tie lines and the vertical line of each alloy; no change of basis. Names of reactions from their shape [Session 8 Slide 6]; amounts from the lever rule [Session 7 Slides 16, 32].

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Invariant reactions (on cooling)
| T (°C) | Reaction | Name |
| :--- | :--- | :--- |
| ~2200 | $L\,(13) + \text{TiB}_2\,(31) \rightarrow \text{Ti}_3\text{B}_4\,(24)$ | peritectic |
| ~2190 | $L\,(13) + \text{Ti}_3\text{B}_4\,(24) \rightarrow \text{TiB}\,(18)$ | peritectic |
| 2080 | $L\,(94) \rightarrow \text{TiB}_2\,(31) + (\beta\text{B})\,(100)$ | eutectic |
| 1540 | $L\,(2) \rightarrow (\beta\text{Ti})\,(0) + \text{TiB}\,(18)$ | eutectic |

At 884 °C the titanium changes from (βTi) to (αTi) (its allotropic change, Topic 2); TiB does not take part.

### b) Melting
- **TiB₂ melts congruently**, at the top of the liquidus, 3225 °C.
- **Ti₃B₄ melts incongruently** ($\text{Ti}_3\text{B}_4 \rightarrow L + \text{TiB}_2$ on heating at ~2200 °C), and so does **TiB** ($\text{TiB} \rightarrow L + \text{Ti}_3\text{B}_4$ at ~2190 °C): both end at peritectic lines [Session 8 Slide 17].

### c) Ti-10 wt% B at 1000 °C and 500 °C
**Phases** at 1000 °C: (βTi) 0 and TiB 18 (length 18):
$$X_{(\beta\text{Ti})} = \frac{18 - 10}{18 - 0} = \frac{8}{18} = 0.44 \qquad X_{\text{TiB}} = \frac{10 - 0}{18} = \frac{10}{18} = 0.56$$
At 500 °C the same, with (αTi) instead of (βTi): 0.44 and 0.56.

**Microconstituents.** $2 < 10 < 18$: hypereutectic, primary TiB and eutectic. Short tie line from the eutectic liquid (2) to TiB (18), length 16:
$$X_{\text{TiB},p} = \frac{10 - 2}{18 - 2} = \frac{8}{16} = 0.50 \qquad X_E = \frac{18 - 10}{16} = 0.50$$
The same at 1000 and 500 °C (the 884 °C change affects only the Ti inside the eutectic).

![[attachments/T4/pd-micro-p15.svg]]

### d) Ti-18 wt% B, very slow cooling to 500 °C
1. **Liquid**, down to the liquidus on the TiB₂ side of the dome (roughly 2500 °C at 18 wt% B, a reading).
2. **L + TiB₂**: primary TiB₂ crystallises; the liquid becomes poorer in B, down to 13 wt% at ~2200 °C.
3. **~2200 °C, peritectic** $L + \text{TiB}_2 \rightarrow \text{Ti}_3\text{B}_4$: since $13 < 18 < 24$, all the TiB₂ is used up and the alloy is L + Ti₃B₄.
4. **~2190 °C, peritectic** $L + \text{Ti}_3\text{B}_4 \rightarrow \text{TiB}$: the alloy has exactly the composition of TiB, so liquid and Ti₃B₄ are both used up: **100 % TiB**.
5. From ~2190 to 500 °C nothing changes: the alloy stays single-phase TiB.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- (c): $0.44 \times 0 + 0.56 \times 18 = 10$ wt% B; the eutectic (0.50) contains all the Ti (0.44) and $0.56 - 0.50 = 0.06$ of TiB, $0.44 + 0.06 = 0.50$ ✓.
- (d): in equilibrium each peritectic is complete; with faster cooling the TiB would surround the Ti₃B₄ (and that the TiB₂) and the reactions would stay incomplete [Session 8 Slide 10].

### Interpretation
A Ti-B alloy with 10 % B is half eutectic (Ti + TiB) and half primary TiB, a hard boride; the 18 % B alloy is a single compound, reached through two peritectic reactions in a row.

## ✅ Check against the official solution
Parts (a), (b) and (c) agree with the key (0.44/0.56 and 50 %/50 % at both temperatures). Part (b) of the key lists only Ti₃B₄; TiB is also incongruent and TiB₂ congruent, as shown above. The key gives no answer for part (d).

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Intermetallic Compounds and Congruent Melting]]
* [[Concept - Invariant Reactions in Binary Systems]]
