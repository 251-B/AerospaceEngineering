---
materia: Aerospace Materials I
tema: "Unit 9: glass transition temperature Tg, melting temperature Tm, specific volume vs temperature, Tg/Tm ratio and MW-T state diagram"
bank_id: B84
title: "Glass transition and melting temperatures"
category: mt3_test_block
unit: 9
concepts:
  - u9-tg-vs-tm-definition
  - u9-tg-vs-tm-regions
  - u9-spec-vol-curves
  - u9-density-temp-order
  - u9-tg-less-than-tm
  - u9-tg-tm-kelvin-rule
  - u9-mw-temp-state-map
  - u9-mw-temp-tg-plateau
difficulty: 2
origen: "Practice questions written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020.pdf; not official exercises. Content from Session 19 Slides 23 and 28-30."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-9
---

# Bank B84 — Glass transition and melting temperatures

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 19, Slides 23 and 28–30. Kelvin and Celsius: use $0\,^\circ\text{C} = 273\text{ K}$.

## Q84.1 Physical origin of Tg and Tm

- id: B84-Q1
- concept_id: u9-tg-vs-tm-definition
- format: topic-true
- asks: definition

Referring to the glass transition temperature $T_g$ and the melting temperature $T_m$ in polymers, which one of the following statements is TRUE:

a) $T_g$ governs the melting of ordered crystalline lamellae, whereas $T_m$ marks segment rotation inside disordered amorphous regions
b) $T_g$ marks the onset of segment motion in amorphous regions, whereas $T_m$ marks the melting of crystalline regions
c) Purely amorphous polymers display both a sharp melting temperature $T_m$ and a lower glass transition $T_g$
d) Below $T_g$ a polymer behaves as a low-viscosity liquid, whereas between $T_g$ and $T_m$ all segments remain frozen

### Answer

b

### Explanation

Session 19, Slides 23 and 28: $T_g$ belongs to the amorphous regions (marking where frozen glassy chain segments acquire enough thermal energy to move), while $T_m$ belongs to the crystalline regions (marking the destruction of ordered lamellae so that both amorphous and crystalline segments move as a liquid).

- a) Swaps the two transitions: $T_g$ belongs to the amorphous regions and $T_m$ belongs to the crystalline regions.
- c) Contradicts the definition of an amorphous polymer: with no crystalline fraction, it exhibits only $T_g$ and no $T_m$ (Slide 23).
- d) Inverts the temperature regimes: below $T_g$ the amorphous regions are a rigid glass with frozen segments, not a liquid.

### Source

Session 19, Slides 23 and 28.

## Q84.2 Thermal transitions in amorphous and semicrystalline polymers

- id: B84-Q2
- concept_id: u9-tg-vs-tm-regions
- format: false-statement
- asks: comparison

Which of the following statements about polymer thermal transitions is FALSE:

a) A semicrystalline polymer exhibits both a glass transition at $T_g$ and a melting transition at $T_m$
b) Below $T_g$, amorphous polymer regions behave as a stiff, brittle glass because segmental motion is frozen
c) Above $T_m$, chains from both crystalline and amorphous regions move freely and the polymer becomes a liquid
d) Amorphous polymers undergo a sharp discontinuous volume jump at $T_m$ before softening at $T_g$

### Answer

d

### Explanation

Session 19, Slides 23 and 28: purely amorphous polymers lack ordered crystalline lamellae, so they show no melting transition $T_m$ and no discontinuous volume jump; instead, they soften gradually above $T_g$ from a glass into an undercooled liquid. Statement d is false.

- a) True: semicrystalline polymers contain both ordered lamellae and disordered amorphous zones, so they show both $T_g$ and $T_m$ (Slide 23).
- b) True: below $T_g$, chain-segment mobility in amorphous zones is frozen in the glassy state (Slide 28).
- c) True: above $T_m$, crystalline order breaks down and all segments move in the molten liquid (Slide 28).

### Source

Session 19, Slides 23 and 28.

## Q84.3 Specific volume against temperature curves

- id: B84-Q3
- concept_id: u9-spec-vol-curves
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-specific-volume-temperature.png]]

In the specific volume versus temperature plot, why do curves B and C exhibit a vertical jump at $T_m$ whereas curve A shows only a change in slope at $T_g$?

a) Curves B and C contain crystalline lamellae that melt at $T_m$, whereas curve A is fully amorphous
b) Curve A undergoes covalent crosslinking at $T_g$, whereas curves B and C break hydrogen bonds at $T_m$
c) Curve A belongs to a crosslinked thermoset elastomer, whereas curves B and C represent ceramic oxides
d) Curves B and C pack with lower density than curve A below $T_g$ and expand discontinuously on heating

### Answer

a

### Explanation

Session 19, Slide 28: curve C (crystalline solid) and curve B (semicrystalline solid) contain ordered crystals that undergo a first-order melting transformation at $T_m$, causing an abrupt increase in specific volume. Curve A (amorphous glass) has no crystals to melt, so it only increases its thermal expansion slope at $T_g$.

- b) Incorrect mechanism: heating across $T_g$ or $T_m$ involves physical chain-segment mobility, not covalent crosslinking reactions.
- c) All three curves represent polymeric solids (amorphous glass, semicrystalline polymer, and crystalline polymer), not ceramics.
- d) Inverts the density ranking: crystalline and semicrystalline solids pack tighter and have *lower* specific volume (higher density) than the amorphous glass.

### Source

Session 19, Slide 28.

## Q84.4 Density versus temperature and the undercooled liquid

- id: B84-Q4
- concept_id: u9-density-temp-order
- format: diagram-reading
- asks: comparison

![[attachments/T9/s19-density-temperature.png]]

On the density versus temperature plot, what state does the bottom (amorphous) curve occupy between $T_g$ and $T_m$, and how do the densities of the three polymer structures compare at a temperature below $T_g$?

a) Rubbery gel; Glass $>$ Semicrystalline $>$ Crystalline
b) Molten fluid; Semicrystalline $>$ Crystalline $>$ Glass
c) Undercooled liquid; Crystalline $>$ Semicrystalline $>$ Glass
d) Crystalline solid; Crystalline $=$ Semicrystalline $>$ Glass

### Answer

c

### Explanation

Session 19, Slides 24 and 28: on the density plot, the amorphous curve passes from the glass below $T_g$ into the undercooled liquid between $T_g$ and $T_m$, joining the liquid above $T_m$. Because ordered chain folding packs chains more efficiently than a random tangle, $\rho_{\text{crystalline}} > \rho_{\text{semicrystalline}} > \rho_{\text{glass}}$ at every temperature below $T_m$.

- a) Inverts the density ranking (glass is the least dense, not the most dense) and misnames the labelled undercooled liquid region.
- b) Places semicrystalline density above fully crystalline density and calls the region between $T_g$ and $T_m$ a molten fluid instead of an undercooled liquid.
- d) An amorphous polymer cannot become a crystalline solid between $T_g$ and $T_m$, and crystalline density strictly exceeds semicrystalline density.

### Source

Session 19, Slides 24 and 28.

## Q84.5 Why Tg is always lower than Tm

- id: B84-Q5
- concept_id: u9-tg-less-than-tm
- format: cause-effect
- asks: cause

For any semicrystalline polymer, the glass transition temperature $T_g$ is lower than the melting temperature $T_m$ because:

a) covalent backbone bonds inside crystalline lamellae break at $T_g$, leaving weak chains to melt at $T_m$
b) segment motion in loose amorphous zones needs less thermal energy than melting dense lamellae
c) amorphous regions possess higher packing density and stronger secondary bonds than crystalline lamellae
d) crystal melting requires rapid cooling below $T_g$ first, whereas the glass transition develops upon heating

### Answer

b

### Explanation

Session 19, Slides 24 and 28: amorphous regions are disordered and less densely packed (more free volume, weaker net interchain attraction), so cooperative rotation of backbone segments begins at a lower temperature $T_g$. Breaking the tightly packed, ordered chain folds of crystalline lamellae demands significantly more thermal energy, so $T_m > T_g$.

- a) Neither $T_g$ nor $T_m$ breaks covalent backbone bonds; both transitions overcome secondary interchain barriers and conformational barriers.
- c) Inverts the packing reality: crystalline regions are denser ($\rho_c > \rho_a$) and experience stronger net secondary interactions per unit volume than amorphous regions.
- d) Both $T_g$ and $T_m$ occur at well-defined thermal energy levels regardless of whether the transition is approached by heating or cooling (under equilibrium/quasi-static conditions).

### Source

Session 19, Slides 24 and 28.

## Q84.6 Kelvin ratio Tg/Tm for PVC

- id: B84-Q6
- concept_id: u9-tg-tm-kelvin-rule
- format: numeric
- asks: calculation
- calc: (87 + 273) / (204 + 273)

Polyvinyl chloride (PVC) has a glass transition temperature $T_g = 87\,^\circ\text{C}$ and a melting temperature $T_m = 204\,^\circ\text{C}$. Using $0\,^\circ\text{C} = 273\text{ K}$, what is the ratio $T_g / T_m$ on the absolute kelvin scale?

a) $0.755$
b) $0.426$
c) $1.325$
d) $0.576$

### Answer

a

### Explanation

Converting both temperatures to kelvin gives $T_g = 87 + 273 = 360\text{ K}$ and $T_m = 204 + 273 = 477\text{ K}$, so $T_g / T_m = 360 / 477 = 0.755$, which lies inside the empirical rule of thumb $T_g \approx (0.5\text{–}0.8)\,T_m$ in kelvin.

- b) Computed directly in Celsius ($87 / 204 = 0.426$) without converting to the absolute kelvin scale.
- c) Inverted ratio $T_m / T_g = 477 / 360 = 1.325$, which exceeds unity and violates $T_g < T_m$.
- d) Corresponds to polypropylene ($T_g = -20\,^\circ\text{C} = 253\text{ K}$, $T_m = 166\,^\circ\text{C} = 439\text{ K}$), not PVC.

### Source

Session 19, Slide 29; Session 20, Slide 8 (with standard kelvin conversion for the $T_g/T_m$ ratio).

## Q84.7 Temperature scale in the Tg to Tm rule of thumb

- id: B84-Q7
- concept_id: u9-tg-tm-kelvin-rule
- format: complete-sentence
- asks: application

The empirical relation $T_g \approx (0.5\text{–}0.8)\,T_m$ relating the glass transition and melting temperatures of semicrystalline polymers holds when both temperatures are expressed in:

a) degrees Celsius, because many common polyolefins exhibit sub-zero glass transition temperatures
b) degrees Fahrenheit, because engineering polymer charts use imperial thermal reference scales
c) Celsius for $T_g$ and kelvin for $T_m$, so negative glass transition values are avoided
d) kelvin, because thermal energy $k_B T$ scales directly with absolute temperature from $0\text{ K}$

### Answer

d

### Explanation

Both $T_g$ and $T_m$ measure the thermal energy required to activate chain-segment rotation and crystal melting, respectively, so their ratio is meaningful only on an absolute scale starting at zero thermal energy (kelvin). In Celsius, polymers like polyethylene ($T_g = -110\,^\circ\text{C}$) or polypropylene ($T_g = -20\,^\circ\text{C}$) give negative ratios that break the $0.5\text{–}0.8$ rule.

- a) Fails immediately whenever $T_g < 0\,^\circ\text{C}$ (for example, PE and PP), which would produce a negative ratio.
- b) Degrees Fahrenheit is an arbitrary shifted scale whose zero does not correspond to zero thermal energy.
- c) Mixing Celsius and kelvin in a dimensionless ratio yields unit-inconsistent, physically meaningless numbers.

### Source

Session 19, Slides 28–29; Session 20, Slide 8.

## Q84.8 Heating path across the molecular weight-temperature map

- id: B84-Q8
- concept_id: u9-mw-temp-state-map
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-mw-tg-regimes.png]]

Following the vertical line at molecular weight $M = 10^5\text{ g/mol}$ on the molecular weight–temperature diagram from low temperature to high temperature, which sequence of regions does the polymer traverse?

a) Crystalline solid $\rightarrow$ Viscous liquid $\rightarrow$ Mobile liquid
b) Partially crystalline plastic $\rightarrow$ Mobile liquid $\rightarrow$ Rubber
c) Partially crystalline plastic $\rightarrow$ Tough plastic $\rightarrow$ Rubber
d) Tough plastic $\rightarrow$ Partially crystalline plastic $\rightarrow$ Viscous liquid

### Answer

c

### Explanation

Session 19, Slide 30: at $M = 10^5\text{ g/mol}$, the vertical path lies below $T_g$ in the `Partially crystalline plastic` region, crosses $T_g$ into the `Tough plastic` region between $T_g$ and $T_m$, and crosses $T_m$ into the `Rubber` region at high temperature.

- a) Describes a low molecular weight around $M \approx 10^3\text{ g/mol}$, not $M = 10^5\text{ g/mol}$.
- b) Places the mobile liquid between the solid and rubbery states, whereas `Mobile liquid` lies at low $M$ and high $T$.
- d) Reverses the lower two regions (tough plastic sits *above* $T_g$, not below it) and lands in `Viscous liquid` ($10^3\text{–}10^4\text{ g/mol}$ range) instead of `Rubber`.

### Source

Session 19, Slide 30.

## Q84.9 Effect of molecular weight on Tg and Tm

- id: B84-Q9
- concept_id: u9-mw-temp-tg-plateau
- format: what-happens
- asks: effect

As the molecular weight of a linear polymer increases from $10^2\text{ g/mol}$ to $10^6\text{ g/mol}$, what happens to its glass transition temperature $T_g$ and melting temperature $T_m$?

a) Both rise initially with molecular weight and approach constant plateau values at high chain length
b) Both decrease steadily with molecular weight because longer chains create more free volume per unit mass
c) $T_m$ rises linearly without bound while $T_g$ remains strictly constant across all chain lengths
d) $T_g$ falls toward $0\text{ K}$ once chain entanglements begin above $M = 10^4\text{ g/mol}$

### Answer

a

### Explanation

Session 19, Slides 29 and 30: increasing molecular weight reduces the concentration of mobile chain ends and increases entanglements, lowering chain mobility so both $T_g$ and $T_m$ rise steeply at low $M$ and then approach asymptotic plateaus above roughly $10^5\text{ g/mol}$.

- b) Inverts the effect: longer chains have fewer free chain ends per unit volume and higher entanglement density, reducing mobility and *raising* $T_g$ and $T_m$.
- c) Both $T_g$ and $T_m$ depend on molecular weight at low $M$ and both level off at high $M$; neither grows linearly forever.
- d) Absolute temperature cannot drop below $0\text{ K}$, and entanglements increase $T_g$ rather than lowering it.

### Source

Session 19, Slides 29–30.

## Q84.10 Why low-molecular-weight polymers fail to form tough plastics

- id: B84-Q10
- concept_id: u9-mw-temp-state-map
- format: identify
- asks: classification

Why does a polymer with a very low molecular weight ($M \approx 10^2\text{–}10^3\text{ g/mol}$) fail to form a tough plastic or rubbery solid above its transition temperatures?

a) Low-molecular-weight chains crosslink densely into brittle three-dimensional thermoset networks
b) Low-molecular-weight chains exhibit higher $T_g$ than $T_m$, preventing softening between transitions
c) Low-molecular-weight polymers undergo chemical decomposition before reaching $T_g$ during heating
d) Short chains lack entanglements, behaving as crystalline solids below $T_m$ and mobile or viscous liquids above $T_m$

### Answer

d

### Explanation

Session 19, Slide 30: in the $10^2\text{–}10^3\text{ g/mol}$ regime, the chains behave like small molecules—too short to entangle and hold together between $T_g$ and $T_m$ or above $T_m$—so the `Tough plastic` and `Rubber` regimes vanish, leaving only `Crystalline solid`, `Mobile liquid`, and `Viscous liquid`.

- a) Low-$M$ linear oligomers are short chains without crosslinks, not densely crosslinked networks.
- b) In the diagram, the $T_m$ curve remains above the $T_g$ curve across the full molecular-weight range.
- c) Transition from solid to mobile/viscous liquid at low $M$ is physical melting at low temperature, not chemical decomposition.

### Source

Session 19, Slide 30.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]] · [[Aerospace Materials I MOC]]
