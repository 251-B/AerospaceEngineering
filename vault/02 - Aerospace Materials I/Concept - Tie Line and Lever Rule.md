---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
fuentes: "Session 7 T4 Phase diagrams I_2025.pdf, Slides 15-21, 32"
tags:
  - theory
  - key-concept
  - lever-rule
  - tie-line
dificultad: medium
prerrequisitos:
  - "[[Concept - Gibbs Phase Rule]]"
---

# 📖 Concept: Tie Line and Lever Rule

> **Key idea in one sentence:** in a two-phase region the tie line gives the composition of each phase and the lever rule gives how much of each there is.

Full explanation: [[Topic 4 - Phase Diagrams and Solidification]].

## Tie line [Session 7 Slide 15]
Horizontal line at the temperature of interest through the alloy point; its ends on the phase boundaries give $C_L$ and $C_\alpha$ on the composition axis.

## Lever rule [Session 7 Slide 16]
Each phase takes the arm of the tie line on the side of the **other** phase:
$$W_L = \frac{C_\alpha - C_0}{C_\alpha - C_L} \qquad W_\alpha = \frac{C_0 - C_L}{C_\alpha - C_L} \qquad W_L + W_\alpha = 1$$

![[attachments/T4/tie-line.svg]]

## Example [Session 7 Slides 16-21]
Cu-35 wt% Ni at 1250 °C, $C_L = 32$, $C_\alpha = 43$: $W_L = 8/11 = 0.727$, $W_\alpha = 3/11 = 0.273$ (the slide writes 0.72 and 0.28). Check: $0.727 \times 32 + 0.273 \times 43 = 35$.

## In eutectic diagrams [Session 7 Slide 32]
Just below the eutectic temperature, with $P = C_0 - C_\alpha$, $Q = C_e - C_0$, $R = C_\beta - C_e$: microconstituents $W_{\alpha'} = Q/(P+Q)$, $W_e = P/(P+Q)$; phases $W_\alpha = (Q+R)/(P+Q+R)$, $W_\beta = P/(P+Q+R)$.

**Back to:** [[Topic 4 - Phase Diagrams and Solidification]] · [[Aerospace Materials I MOC]]
