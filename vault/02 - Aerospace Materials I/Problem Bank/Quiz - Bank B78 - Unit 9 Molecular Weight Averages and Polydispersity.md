---
materia: Aerospace Materials I
tema: "Unit 9: molecular weight distributions, Mn, Mw, polydispersity index (PDI), degree of polymerization Xn, and effects of molecular weight on Tm, Tg, strength and melt viscosity"
bank_id: B78
title: "Molecular weight averages and polydispersity"
category: mt3_test_block
unit: 9
concepts:
  - u9-mw-distribution-diagram
  - u9-mw-averages-definitions
  - u9-mw-pdi-monodisperse
  - u9-mw-degree-of-polymerization-calc
  - u9-mw-tg-tm-effect
  - u9-mw-tensile-strength-entanglement
  - u9-mw-melt-viscosity
  - u9-mw-pdi-physical-meaning
  - u9-mw-low-mw-wax-regimes
  - u9-mw-average-ordering
difficulty: 2
origen: "Practice items written for the bank in the style of Part I of Assessment Test III. Content from Session 19 Slides 12–15, 29–30, 43 and 45, and Problems T9 Q1, Q7 and Q8."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-9
---

# Bank B78 — Molecular weight averages and polydispersity

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 19, Slides 12–15, 29–30, 43 and 45, and Problems T9 Q1, Q7 and Q8 (number and weight averages, polydispersity, degree of polymerization, and property effects of molecular weight).

## Q78.1 Weight-average versus number-average position on a distribution curve

- id: B78-Q1
- concept_id: u9-mw-distribution-diagram
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-molecular-weight-distribution.png]]

In the shown molecular weight distribution of a synthetic polymer, why does the weight-average molecular weight $\bar{M}_w$ lie to the right of the number-average molecular weight $\bar{M}_n$?

a) Because $\bar{M}_n$ weights every chain by its squared molecular weight while $\bar{M}_w$ counts each molecule equally
b) Because short low-mass chains contribute more mass per molecule than long chains in any polymer distribution
c) Because $\bar{M}_w$ weights each size fraction by its mass rather than simply counting molecules equally
d) Because $\bar{M}_n$ measures only the crystalline fraction while $\bar{M}_w$ averages both amorphous and crystalline chains

### Answer

c

### Explanation

Session 19, Slides 12–13: $\bar{M}_n = \sum x_i M_i$ counts every macromolecule equally regardless of size, whereas $\bar{M}_w = \sum w_i M_i = \sum N_i M_i^2 / \sum N_i M_i$ weights each chain by its mass. Because heavier chains carry a disproportionate share of the total mass, $\bar{M}_w \ge \bar{M}_n$, shifting $\bar{M}_w$ to the right on the distribution curve.

- a) Inverts the definitions of the two averages: $\bar{M}_w$ uses the $M_i^2$ weighting in molecule counts, whereas $\bar{M}_n$ weights by $N_i$ directly.
- b) Physically false: a longer chain of higher molecular weight carries more mass per molecule than a shorter chain.
- d) Neither $\bar{M}_n$ nor $\bar{M}_w$ separates crystalline from amorphous regions; both average over all chains in the sample.

### Source

Session 19, Slides 12–15.

## Q78.2 Formulas for number-average and weight-average molecular weight

- id: B78-Q2
- concept_id: u9-mw-averages-definitions
- format: topic-false
- asks: definition

Referring to the number-average ($M_n$) and weight-average ($M_w$) molecular weights of a polymer, which one of the following statements is FALSE:

a) The number-average molecular weight is defined by $M_n = \sum w_i M_i$, summing weight fractions $w_i$
b) In terms of molecule counts $N_i$ and range midpoints $M_i$, $M_n = \sum N_i M_i / \sum N_i$
c) In terms of molecule counts $N_i$ and range midpoints $M_i$, $M_w = \sum N_i M_i^2 / \sum N_i M_i$
d) Synthetic polymerization reactions produce a distribution of chain lengths rather than a single molecular weight

### Answer

a

### Explanation

Session 19, Slides 12–13: $\sum w_i M_i$ defines the *weight-average* molecular weight $M_w$, whereas the number-average molecular weight is $M_n = \sum x_i M_i$, where $x_i = N_i / \sum N_i$ is the number fraction. Statement a is false.

- b) True (Slide 13): dividing total sample mass $\sum N_i M_i$ by total number of molecules $\sum N_i$ gives $M_n$.
- c) True (Slide 13): substituting $W_i = N_i M_i$ into $\sum W_i M_i / \sum W_i$ yields $\sum N_i M_i^2 / \sum N_i M_i$.
- d) True (Slide 12): polymerization kinetics produce a statistical distribution of molecular weights rather than identical chains.

### Source

Session 19, Slides 12–13.

## Q78.3 Polydispersity index bounds and monodisperse limit

- id: B78-Q3
- concept_id: u9-mw-pdi-monodisperse
- format: true-statement
- asks: definition

Which of the following statements is TRUE:

a) The polydispersity index $I = M_w / M_n$ drops steadily below $1$ as the chain-length distribution broadens
b) For a perfectly monodisperse polymer sample where all chains share equal length, $M_w$ equals twice $M_n$
c) A broad distribution of chain lengths yields $I = M_n / M_w > 1$ because $M_n$ exceeds $M_w$ in practice
d) The polydispersity index satisfies $I = M_w / M_n \ge 1$, equalling $1$ when every chain has the same mass

### Answer

d

### Explanation

Session 19, Slide 13 (and Problem T9-01): the index of polydispersion $I = M_w / M_n$ measures the lack of homogeneity of molecular weights. By the Cauchy-Schwarz inequality, $M_w \ge M_n$ for every distribution, so $I \ge 1$, with $I = 1$ solely for a monodisperse polymer in which every chain shares the exact same molecular weight.

- a) Inverts the bound: broader molecular weight distributions push $M_w$ further above $M_n$, raising $I$ above $1$, never below $1$.
- b) In a monodisperse polymer, $M_w = M_n = M$, so $I = M_w/M_n = 1$, not $2$.
- c) Inverts both the ratio and the inequality: $I = M_w / M_n$ (not $M_n / M_w$), and $M_w$ is greater than or equal to $M_n$.

### Source

Session 19, Slide 13; Problems T9_Polymers.pdf, Problem 1.

## Q78.4 Degree of polymerization of poly(vinyl chloride)

- id: B78-Q4
- concept_id: u9-mw-degree-of-polymerization-calc
- format: numeric
- asks: calculation
- calc: 125000/(2*12+3*1+35.5)

A sample of poly(vinyl chloride) ($\mathrm{-[CH_2{-}CHCl]_n-}$) has a number-average molecular weight $M_n = 125\,000\ \text{g/mol}$. Using atomic weights $\text{C} = 12$, $\text{H} = 1$, and $\text{Cl} = 35.5\ \text{g/mol}$, calculate the number-average degree of polymerization $X_n$:

a) $1000$ repeat units
b) $2000$ repeat units
c) $4464$ repeat units
d) $2475$ repeat units

### Answer

b

### Explanation

Session 19, Slides 12 and 50 (Problem T9-01 style): first determine the molecular weight of one PVC repeat unit $\mathrm{C_2H_3Cl}$: $M_0 = 2(12) + 3(1) + 35.5 = 62.5\ \text{g/mol}$. Then $X_n = M_n / M_0 = 125\,000 / 62.5 = 2000$ repeat units (dimensionless).

- a) Halved $X_n$ to $1000$ by erroneously assuming two repeat units per step instead of dividing $M_n$ directly by $M_0 = 62.5\ \text{g/mol}$.
- c) Used the polyethylene repeat-unit weight $M_0 = 28\ \text{g/mol}$ instead of PVC's $62.5\ \text{g/mol}$, giving $125\,000 / 28 = 4464$.
- d) Omitted one backbone carbon ($12\ \text{g/mol}$) when summing the PVC repeat unit, dividing $125\,000$ by $50.5$ to obtain $2475$.

### Source

Session 19, Slides 12 and 50; Problems T9_Polymers.pdf, Problem 1.

## Q78.5 Influence of molecular weight on transition temperatures

- id: B78-Q5
- concept_id: u9-mw-tg-tm-effect
- format: cause-effect
- asks: effect

As the molecular weight of a linear thermoplastic polymer increases from oligomers ($10^2\ \text{g/mol}$) toward high-polymer chains ($10^5$–$10^6\ \text{g/mol}$), its glass transition temperature $T_g$ and melting temperature $T_m$:

a) both increase rapidly at low molecular weights and gradually approach asymptotic plateaus for very long chains
b) both decrease steadily because longer chains possess fewer rigid chain ends and move more freely
c) $T_g$ increases continuously without bound while $T_m$ drops to room temperature due to entanglement
d) remain completely independent of molecular weight across the entire range from $10^1$ to $10^7\ \text{g/mol}$

### Answer

a

### Explanation

Session 19, Slides 29–30: higher molecular weight reduces chain mobility ($\uparrow M \implies \downarrow \text{chain mobility} \implies \uparrow T_g$), and the molecular-weight map on Slide 30 plots both $T_g$ and $T_m$ rising steeply through $10^2$–$10^4\ \text{g/mol}$ before levelling off asymptotically at high $M$.

- b) Inverts the effect of chain length: longer chains have lower mobility and fewer mobile chain ends, which raises rather than lowers $T_g$ and $T_m$.
- c) Contradicts Slide 30, where $T_m$ stays parallel above $T_g$ and both plateau rather than crossing or dropping at high $M$.
- d) Transition temperatures plateau only at very high $M$ ($10^5$–$10^7\ \text{g/mol}$), not across low and intermediate molecular weights.

### Source

Session 19, Slides 29–30.

## Q78.6 Why molecular weight raises tensile strength and stiffness

- id: B78-Q6
- concept_id: u9-mw-tensile-strength-entanglement
- format: complete-sentence
- asks: cause

Increasing the molecular weight of a thermoplastic polymer generally increases its tensile strength and high-temperature stiffness because:

a) shorter chains pack into perfect defect-free single crystals that resist dislocation glide
b) higher molecular weight converts secondary van der Waals bonds into permanent covalent crosslinks
c) longer chains create a higher density of inter-chain entanglements that resist sliding and pull-out
d) longer chains eliminate all amorphous regions and convert the polymer into a 100 % crystalline solid

### Answer

c

### Explanation

Session 19, Slides 43 and 45: long polymer chains form a high density of entanglements (physical knots) that inhibit chain sliding under stress, increasing tensile strength $\sigma$, elastic modulus $E$, and the rubbery plateau modulus above $T_g$.

- a) Polymers do not strengthen via dislocation glide in extended metallic single crystals; entanglement of long chains is the primary mechanism here.
- b) Increasing chain length does not form covalent crosslinks between separate macromolecules; linear chains remain bonded to neighbours by secondary interactions.
- d) Very long chains actually entangle extensively and never reach 100 % crystallinity.

### Source

Session 19, Slides 43 and 45.

## Q78.7 Effect of molecular weight on melt viscosity above Tm

- id: B78-Q7
- concept_id: u9-mw-melt-viscosity
- format: what-happens
- asks: effect

When a polymer melt is heated above its melting temperature $T_m$, what happens to its flow behaviour and melt viscosity as the molecular weight increases from $10^2$ to $10^6\ \text{g/mol}$?

a) The melt viscosity drops sharply because long chains glide past one another with zero friction
b) The material transforms from a rubbery solid at $10^2\ \text{g/mol}$ into a low-viscosity mobile liquid at $10^6\ \text{g/mol}$
c) Melt viscosity stays constant above $T_m$ because all inter-chain entanglements vanish at the melting point
d) Flow resistance and melt viscosity rise strongly, shifting from a mobile liquid to a viscous liquid and then to a rubbery melt

### Answer

d

### Explanation

Session 19, Slide 30 (and Slide 43): on the molecular-weight map above $T_m$, increasing $M$ moves the polymer across the dashed entanglement boundaries from a mobile liquid ($10^2$–$10^3\ \text{g/mol}$), through a viscous liquid ($10^3$–$10^4\ \text{g/mol}$), into a rubbery entangled state ($10^5$–$10^7\ \text{g/mol}$) with markedly higher melt viscosity (extension: higher entanglement density strongly resists viscous flow).

- a) Inverts viscosity behaviour: longer chains entangle much more strongly, raising resistance to flow rather than lowering it.
- b) Reverses the low-$M$ and high-$M$ regions on Slide 30: mobile liquids occur at low $M$ ($10^2$–$10^3$), whereas rubbery behaviour occurs at high $M$.
- c) Entanglements persist in the melt above $T_m$ and dominate polymer melt viscosity.

### Source

Session 19, Slides 30 and 43.

## Q78.8 Interpreting two polymer batches with equal Mn and different PDI

- id: B78-Q8
- concept_id: u9-mw-pdi-physical-meaning
- format: identify
- asks: comparison

Two polyethylene batches share the same number-average molecular weight $M_n = 50\,000\ \text{g/mol}$, yet Batch X has $\text{PDI} = 1.1$ and Batch Y has $\text{PDI} = 4.5$. Which statement correctly describes Batch Y relative to Batch X?

a) Batch Y has a narrower chain-length spread and a lower weight-average molecular weight $M_w$
b) Batch Y has a broader chain-length spread with both very short and very long chains, giving a higher $M_w$
c) Batch Y is strictly monodisperse, whereas Batch X contains a high fraction of low-molecular-weight wax
d) Both batches have identical $M_w$ and identical melt flow behaviour because $M_n$ alone fixes all properties

### Answer

b

### Explanation

Session 19, Slide 13: since $I = \text{PDI} = M_w / M_n$, at fixed $M_n = 50\,000\ \text{g/mol}$, Batch X has $M_w = 55\,000\ \text{g/mol}$ while Batch Y has $M_w = 225\,000\ \text{g/mol}$. The much larger PDI signifies a broad distribution containing both very short and very long chains.

- a) Confuses larger PDI with narrower spread: PDI closer to $1$ (Batch X) is narrower, whereas $\text{PDI} = 4.5$ is much broader.
- c) A strictly monodisperse polymer has $\text{PDI} = 1.0$; Batch X ($1.1$) is far closer to monodisperse than Batch Y ($4.5$).
- d) Long high-$M$ tail chains strongly elevate $M_w$ and melt viscosity even when $M_n$ is identical.

### Source

Session 19, Slide 13.

## Q78.9 Physical states across the molecular-weight map

- id: B78-Q9
- concept_id: u9-mw-low-mw-wax-regimes
- format: topic-true
- asks: classification

Referring to the physical states of a polymer as a function of molecular weight and temperature, which one of the following statements is TRUE:

a) Useful tough plastics typically require ultra-short chains below $500\ \text{g/mol}$ so that chains align without entanglements
b) Above $T_m$, polymers with molecular weights exceeding $10^5\ \text{g/mol}$ flow freely as mobile, low-viscosity liquids
c) Increasing molecular weight lowers room-temperature toughness by preventing any chain entanglement in the amorphous phase
d) Very low-molecular-weight chains ($10^2$–$10^3\ \text{g/mol}$) behave like waxes or mobile liquids rather than tough structural plastics

### Answer

d

### Explanation

Session 19, Slide 30: at low molecular weights ($10^2$–$10^3\ \text{g/mol}$), chains are too short to entangle effectively, yielding crystalline waxes below $T_m$ and mobile liquids above $T_m$. Useful tough and partially crystalline structural plastics appear only at higher molecular weights ($\ge 10^4$–$10^5\ \text{g/mol}$).

- a) Ultra-short chains below $500\ \text{g/mol}$ lack entanglements and behave as brittle waxes or mobile liquids, not tough plastics.
- b) Above $T_m$ at $M > 10^5\ \text{g/mol}$, Slide 30 places the polymer in the rubbery regime rather than the mobile liquid regime.
- c) Higher molecular weight increases entanglement density and strength rather than preventing entanglements.

### Source

Session 19, Slide 30.

## Q78.10 Ranking repeat-unit weight and molecular weight averages

- id: B78-Q10
- concept_id: u9-mw-average-ordering
- format: ordering
- asks: comparison

For a synthetic polydisperse polymer composed of chains averaging at least 100 repeat units ($X_n \ge 100$), rank the repeat-unit molecular weight $M_0$, the number-average molecular weight $M_n$, and the weight-average molecular weight $M_w$ in strictly increasing order:

a) $M_n < M_w < M_0$
b) $M_0 < M_w < M_n$
c) $M_0 < M_n < M_w$
d) $M_w < M_n < M_0$

### Answer

c

### Explanation

Session 19, Slides 12–13 (and Problems T9-07, T9-08): since $M_n = X_n M_0$ with $X_n \ge 100$, $M_n$ is at least one hundred times larger than $M_0$, and because the polymer is polydisperse ($I = M_w / M_n > 1$), $M_w$ strictly exceeds $M_n$. Therefore $M_0 < M_n < M_w$.

- a) Places the single repeat-unit weight $M_0$ above the full macromolecular averages $M_n$ and $M_w$.
- b) Swaps $M_w$ and $M_n$: in any polydisperse distribution, the weight average is larger than the number average.
- d) Reverses the entire order, putting both $M_w < M_n$ and the macromolecular weights below $M_0$.

### Source

Session 19, Slides 12–13; Problems T9_Polymers.pdf, Problems 7 and 8.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
