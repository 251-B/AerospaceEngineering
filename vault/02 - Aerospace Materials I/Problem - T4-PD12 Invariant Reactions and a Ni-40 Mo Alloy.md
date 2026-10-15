---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 12"
dificultad: medium
tags:
  - official-problem
  - solved
  - invariant-reactions
  - lever-rule
  - microconstituents
  - ni-mo
---

# ✏️ Problem: T4-PD12 — Invariant Reactions and a Ni-40 at.% Mo Alloy

## 📄 Official Statement
> **12. According to the Ni-Mo phase, indicate: a. The equations that represent the invariant reactions, specifying the composition of the phases, temperature and type of reaction. b. The maximum solubility of Mo in Ni and at what temperature it is produced. c. The maximum solubility of Ni in Mo and at what temperature it is produced. d. Melting temperature of Ni and Mo. e. Present phases, their composition and amount for a Ni-40%Mo alloy at 1309 °C. f. Microconstituents and their amount for a Ni-40%Mo alloy at 1309 °C. Sketch the microstructure.**
>
> ![[attachments/T4/pd-p12-nimo.png]]
>
> *(Solution: a) eutectic reaction (1310 °C); peritectoid reaction (910 °C); peritectic reaction (1362 °C). b) 26% Mo. c) 4% Ni. d) 1455 °C; 2623 °C. e) $C_{NiMo}$ = 52%Mo; $C_\alpha$ = 27%Mo; $X_\alpha$ = 0.48; $X_{NiMo}$ = 0.52. f) $X_{NiMo,p}$ = 0.25; $X_E$ = 0.75)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium**, Ni-Mo diagram of the sheet. Its axis reads only "Mo (%)", but the compounds sit at their **atomic** compositions (Ni₄Mo ≈ 20, Ni₃Mo = 25, NiMo ≈ 52 % Mo; in wt% they would be at 29.0, 35.3 and 62.0), so the axis is in **atomic % Mo** (at.%), like the Ti-Si diagram of Problem 13. Printed temperatures: 1455, 2623, 1362, 1310, 910 and 870 °C. Compositions are **readings of the figure** (±1 at.%).
2. α is the Ni-rich solid solution and β the Mo-rich one; NiMo is an intermediate phase with a narrow composition range; Ni₃Mo and Ni₄Mo are compounds that form in the solid.

### Data read on the diagram
| Line | Phases (at.% Mo) |
| :--- | :--- |
| 1310 °C | α ≈ 27, L ≈ 36, NiMo ≈ 52 |
| 1362 °C | L ≈ 38, NiMo ≈ 55, β ≈ 96 |
| 910 °C | α ≈ 22, Ni₃Mo ≈ 25, NiMo ≈ 52 |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Ni-Mo diagram (at.% Mo, °C); one horizontal line per question, so no change of basis is needed. Reactions are named by their shape [Session 8 Slide 6]; amounts by the lever rule [Session 7 Slides 16, 32].

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Invariant reactions (on cooling)
| T (°C) | Reaction | Type |
| :--- | :--- | :--- |
| 1362 | $L\,(38) + \beta\,(96) \rightarrow \text{NiMo}\,(55)$ | peritectic |
| 1310 | $L\,(36) \rightarrow \alpha\,(27) + \text{NiMo}\,(52)$ | eutectic |
| 910 | $\alpha\,(22) + \text{NiMo}\,(52) \rightarrow \text{Ni}_3\text{Mo}\,(25)$ | peritectoid |

At 870 °C the compound Ni₄Mo appears inside the α field (the small dome); only α and Ni₄Mo take part, so it is not a three-phase reaction.

### b), c), d)
- Maximum solubility of **Mo in Ni**: about **27 at.% Mo** (the key writes 26 %), at the eutectic temperature, **1310 °C**.
- Maximum solubility of **Ni in Mo**: about **4 at.% Ni** (β at 96 at.% Mo), at the peritectic temperature, **1362 °C**.
- Melting points: **Ni 1455 °C**, **Mo 2623 °C**.

### e) Phases of Ni-40 at.% Mo at 1309 °C
Just below the eutectic: α (27) + NiMo (52), tie line length 25. On an at.% axis the lever rule gives **atom (mole) fractions** $X$, as the key writes them (the lever rule is a balance of whatever the axis counts; this remark is an extension, since the slides use wt% axes):
$$X_\alpha = \frac{C_{\text{NiMo}} - C_0}{C_{\text{NiMo}} - C_\alpha} = \frac{52 - 40}{52 - 27} = \frac{12}{25} = 0.48 \qquad X_{\text{NiMo}} = \frac{40 - 27}{25} = \frac{13}{25} = 0.52$$

### f) Microconstituents at 1309 °C
$36 < 40 < 52$: the alloy is **hypereutectic**, so primary NiMo forms first and the liquid of 36 at.% Mo becomes eutectic. Short tie line from 36 to 52 (length 16):
$$X_{\text{NiMo},p} = \frac{C_0 - C_e}{C_{\text{NiMo}} - C_e} = \frac{40 - 36}{52 - 36} = \frac{4}{16} = 0.25 \qquad X_E = \frac{52 - 40}{16} = \frac{12}{16} = 0.75$$

![[attachments/T4/pd-micro-p12.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- Atom balance at 1309 °C: $0.48 \times 27 + 0.52 \times 52 = 12.96 + 27.04 = 40.0$ at.% Mo.
- Phases inside the eutectic: all the α (0.48) and NiMo $0.52 - 0.25 = 0.27$; $0.48 + 0.27 = 0.75 = X_E$ ✓. The eutectic alone is $(52 - 36)/(52 - 27) = 16/25 = 0.64$ α, and $0.75 \times 0.64 = 0.48$ ✓.
- **Limiting cases** (atom fractions, dimensionless; compositions in at.% Mo): at $C_0 = 36$ the alloy would be all eutectic and at $C_0 = 52$ all primary NiMo; 40 at.% lies close to the eutectic end, hence three quarters eutectic.

### Interpretation
The alloy is three quarters eutectic (α + NiMo) with a quarter of primary NiMo crystals. On further cooling, the α and NiMo of this alloy reach the 910 °C peritectoid, where they react to form Ni₃Mo.

## ✅ Check against the official solution
All values agree with the key (0.48/0.52; 0.25/0.75; 1455 and 2623 °C; the three reactions). The key gives 26 % Mo for part (b) and uses 27 % Mo in part (e); the figure reads about 27 %. All compositions are at.% and the fractions are atom fractions, as in the key's $X$.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Invariant Reactions in Binary Systems]]
* [[Concept - Binary Eutectic Systems and Microconstituents]]
