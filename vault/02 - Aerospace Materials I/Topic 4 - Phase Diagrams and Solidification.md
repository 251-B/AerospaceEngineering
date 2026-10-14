---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
fuentes: "Session 7 T4 Phase diagrams I_2025.pdf, Slides 1-32"
tags:
  - theory
  - topic-moc
  - phase-diagrams
  - gibbs-phase-rule
  - lever-rule
  - eutectic
dificultad: medium
prerrequisitos:
  - "[[Topic 2 - Structure of Materials and Crystalline Defects]]"
  - "[[Topic 3 - Diffusion in Solids and Mass Transport]]"
---

# 🌐 Topic 4: Phase Diagrams and Solidification

> **Central idea:** a phase diagram is a map that tells which phases are stable in a material for each temperature, pressure and composition. Reading it gives three answers for any alloy at any temperature: which phases are present, what each phase is made of, and how much of each there is.

This page follows the official slides of Topic 4 in order. Part I (Session 7) covers the basic vocabulary, one-component diagrams, binary isomorphous systems, the Gibbs phase rule, the tie line and the lever rule, non-equilibrium solidification and binary eutectic systems. Worked examples use only data printed on the slides.

---

# Part I — Phase diagrams I (Session 7)

## 1. Component, phase and microconstituent [Session 7 Slide 2]

Three words are used all through the topic, and they mean different things:

- **Component:** a chemical substance or compound with a fixed composition that can form part of a phase or of an alloy. Examples: aluminium (Al), alumina (Al₂O₃).
- **Phase:** a chemically and structurally homogeneous region that forms part of the microstructure. It can be made of one or of several components. Examples: ferrite (a solid solution of C in Fe with BCC structure), austenite (a solid solution of C in Fe with FCC structure), calcium carbonate (CaCO₃).
- **Microconstituent:** each of the different structures that can be seen on a polished surface of the material. It can be made of one phase or of several phases.

The slide illustrates the three words with food: the components of a potato are water, protein, fat, carbohydrates and so on (a table of grams per 100 g); the potato itself plays the role of a phase; and fries, a structure you can see and that is made from the potato, play the role of a microconstituent.

In a real material, the micrograph below shows a steel with two microconstituents. Region 1 is **ferrite**, a single phase. Regions 2 and 3 are **pearlite**, a microconstituent made of two phases (ferrite and cementite) arranged in thin alternating plates.

![[attachments/T4/s7-ferrite-pearlite.png]]

## 2. The equilibrium phase diagram [Session 7 Slide 3]

An **equilibrium phase diagram** (also called a **stability map**) is a map of the phases in thermodynamic equilibrium that are present in a system of materials at different pressures, temperatures and compositions.

The slide uses the phase diagram of CO₂ as an example:

![[attachments/T4/co2.svg]]

- There is no liquid CO₂ at room temperature and ambient pressure.
- The slope of the solid-liquid line, $dP/dT$, is positive, as it is in almost all substances.
- At the **triple point** (5.1 atm, −56.6 °C) gas, liquid and solid are in equilibrium.
- At temperatures below the triple point CO₂ can sublime: gas → solid (dry ice) on cooling, and solid → gas on heating.
- Above the critical temperature $T_c$ = 31.1 °C and pressure $P_c$ = 73 atm CO₂ is a **supercritical fluid** (used to extract caffeine from coffee).

> [!example] Worked example 1 — Why dry ice does not melt at 1 atm
> **Question.** A block of solid CO₂ is heated at a constant pressure of 1 atm. What phases appear?
>
> **Reading the diagram.** Follow the horizontal line $P$ = 1 atm from left to right. Since 1 atm is below the pressure of the triple point (5.1 atm), the line never enters the liquid region: it goes from the solid region straight into the gas region, crossing the sublimation line at −78.2 °C.
>
> **Answer.** The solid turns directly into gas at −78.2 °C (sublimation). Liquid CO₂ can exist only at pressures above 5.1 atm, which is why there is no liquid CO₂ at room conditions [Session 7 Slide 3].

## 3. Unary (one-component) diagrams [Session 7 Slides 5-6]

With a single component the composition is fixed, so the diagram is drawn with **pressure and temperature** as axes (a P-T diagram).

### 3.1 Water [Session 7 Slide 5]

The P-T diagram of water has three lines that meet at the **triple point** $P_T$: the sublimation line (A to $P_T$), the melting line ($P_T$ to B) and the vaporisation line ($P_T$ to C). Cooling at constant pressure along the dashed line, the water vapour first crosses the vaporisation line at $T_v$ and then the melting line at $T_m$.

![[attachments/T4/water.svg]]

The **cooling curve** on the right records the temperature against time along that path. In the stretches 1, 3 and 5 a single phase cools down. In the plateaus 2 (condensation at $T_v$) and 4 (solidification at $T_m$) the temperature stays constant while two phases coexist, because the heat released by the transformation compensates the heat that is lost.

On a diagram with pressure on a log scale, the vertical line at 1 atm meets the melting line at 0 °C (water/ice) and the vaporisation line at 100 °C (steam/water):

![[attachments/T4/water-logp.svg]]

At very high pressures (up to several GPa) water has many different solid phases, the different crystal structures of ice:

![[attachments/T4/s7-water-high-pressure.png]]

### 3.2 Pure iron [Session 7 Slide 6]

Solid iron has **three different crystal structures**, each a different phase: **α-Fe (BCC)** below 910 °C, **γ-Fe (FCC)** between 910 and 1394 °C, and **δ-Fe (BCC)** from 1394 °C up to the melting point, 1538 °C. Different phases coexist at the **triple points**. The slide compares the three solid structures with three varieties of potato (yellow, red and purple) and the liquid with potato purée: the same "substance" in different forms.

![[attachments/T4/iron-pt.svg]]

## 4. Binary isomorphous diagrams [Session 7 Slides 8-11]

### 4.1 Cooling curves [Session 7 Slide 8]

**Cooling curves** are used to determine the temperatures of the phase transitions: the temperature of a cooling molten metal is recorded against time and plotted.

![[attachments/T4/cooling-curves.svg]]

- **Thermal arrest:** while a pure metal solidifies, the heat lost to the surroundings equals the heat supplied by the solidifying metal, so the temperature stays constant (a plateau). Pure iron shows one plateau for solidification and one for each change of crystal structure. (This slide prints 912 °C for the γ → α change; Slide 6 prints 910 °C.)
- **Alloys** solidify over a range of temperatures: they show no thermal arrest, only changes of slope.

### 4.2 Building the diagram from cooling curves [Session 7 Slide 9]

A **binary isomorphous** system has two components with **complete solid solubility**. Its diagram is built from the cooling curves of several compositions: each curve gives the temperature where solidification starts and the one where it ends. Joining the start points gives the **liquidus**; joining the end points gives the **solidus**. Above the liquidus everything is liquid (L), below the solidus everything is a single solid solution (SS), and between them liquid and solid coexist (L + SS).

![[attachments/T4/iso-construction.svg]]

The slide compares the series of compositions with milk: whole, semi-skimmed and skimmed milk are mixtures of water and skim solids in different proportions, just as the alloys are mixtures of A and B.

### 4.3 Microstructure along the cooling [Session 7 Slide 10]

For an alloy of a given composition (the vertical line), the diagram tells what the microstructure is at each temperature:

![[attachments/T4/iso-micro.svg]]

- above the liquidus: **all liquid**;
- at a temperature $T_1$ between the liquidus and the solidus: **crystallites of the solid solution SS₁ in a matrix of liquid L₁**; the compositions of L₁ and SS₁ are read on the liquidus and the solidus at $T_1$;
- below the solidus: a **polycrystalline solid** of a single phase, the solid solution, with the composition of the alloy.

The slide's analogy: milk alone is the liquid; milk with pieces of Manchego cheese is the two-phase mixture; the cheese alone is the solid.

### 4.4 Complete solid solubility [Session 7 Slide 11]

With complete solubility in the solid state:

- the material is a **polycrystalline single-phase** material: its microstructure (FCC, BCC or any other) is not different from that of the pure metal, because the atoms of B simply replace atoms of A in the same lattice;
- when solute is added, the melting temperature $T_m$ is modified;
- the alloy **does not solidify at a constant temperature** but over a range of temperatures, between the liquidus and the solidus.

![[attachments/T4/complete-solubility.svg]]

## 5. Gibbs phase rule [Session 7 Slide 13]

The **Gibbs phase rule** counts how many variables can be changed independently while keeping the same phases in equilibrium:

$$F = C - P + N$$

- $F$: degrees of freedom, the number of independent variables available to the system;
- $C$: number of components;
- $P$: number of phases;
- $N$: number of non-compositional variables (for example pressure and temperature).

With pressure and temperature both free, $N = 2$ and $F = C - P + 2$. For routine processing of materials the pressure can be considered fixed at 1 atm, so only temperature remains and

$$F = C - P + 1$$

![[attachments/T4/gibbs.svg]]

> [!example] Worked example 2 — Counting degrees of freedom on the slide diagrams
> **One component (water), $F = 1 - P + 2$ [Session 7 Slide 13]:**
> - inside a single-phase region (liquid): $F = 1 - 1 + 2 = 2$; temperature and pressure can both change without leaving the region;
> - on a two-phase line (for example solid-liquid): $F = 1 - 2 + 2 = 1$; if the temperature is chosen, the pressure is fixed by the line;
> - at the triple point: $F = 1 - 3 + 2 = 0$; three phases coexist only at one temperature and one pressure.
>
> **Two components at 1 atm, $F = 2 - P + 1$:**
> - in L or in the solid solution: $F = 2 - 1 + 1 = 2$; temperature and composition can both change;
> - in L + solid (and on its boundaries): $F = 2 - 2 + 1 = 1$;
> - at the melting point of pure B, a single component with two phases: $F = 1 - 2 + 1 = 0$, which is why a pure metal melts at one fixed temperature.
>
> **Consequence for the tie line (§6).** In the α + L region of the Cu-Ni diagram $F = 1$. Choosing the temperature uses that single degree of freedom, so the compositions of the two phases are no longer free: at 1250 °C they can only be $C_L$ = 32 wt% Ni and $C_\alpha$ = 43 wt% Ni [Session 7 Slide 16]. Changing the overall composition of the alloy changes only the amounts of the two phases, not their compositions.

## 6. Tie line and lever rule [Session 7 Slides 15-21]

In a two-phase region two questions are answered with two tools [Session 7 Slide 15]:

- **Phase composition: the tie line.** Draw a horizontal line (constant temperature) through the point of the alloy across the two-phase region. Its intersections with the phase boundaries give, on the composition axis, the composition of each phase.
- **Phase amounts: the lever rule.** The fraction of each phase is computed by taking the length of the tie line from the overall alloy composition to the phase boundary of the **other** phase, and dividing by the total length of the tie line [Session 7 Slide 16].

![[attachments/T4/tie-line.svg]]

For the alloy B, with overall composition $C_0$ and the arms $R = C_0 - C_L$ and $S = C_\alpha - C_0$:

$$W_L = \frac{S}{R + S} = \frac{C_\alpha - C_0}{C_\alpha - C_L} \qquad W_\alpha = \frac{R}{R + S} = \frac{C_0 - C_L}{C_\alpha - C_L} \qquad W_L + W_\alpha = 1$$

where $W_L$ is the mass fraction of liquid and $W_\alpha$ the mass fraction of α.

> [!example] Worked example 3 — Cu-35 wt% Ni at 1250 °C [Session 7 Slides 16-21]
> **Data from the slide.** $C_0 = 35$ wt% Ni at 1250 °C (point B). The tie line meets the liquidus at $C_L = 32$ wt% Ni and the solidus at $C_\alpha = 43$ wt% Ni.
>
> **Step 1, the arms of the lever.** $R = C_0 - C_L = 35 - 32 = 3$ wt% Ni and $S = C_\alpha - C_0 = 43 - 35 = 8$ wt% Ni; the whole tie line is $R + S = C_\alpha - C_L = 43 - 32 = 11$ wt% Ni.
>
> **Step 2, the fractions.** Each phase takes the arm on the side of the other phase:
> $$W_L = \frac{S}{R+S} = \frac{43 - 35}{43 - 32} = \frac{8}{11} = 0.727 \qquad W_\alpha = \frac{R}{R+S} = \frac{35 - 32}{43 - 32} = \frac{3}{11} = 0.273$$
>
> **Step 3, checks.** $W_L + W_\alpha = 8/11 + 3/11 = 1$. The nickel of the two phases adds up to the nickel of the alloy: $W_L C_L + W_\alpha C_\alpha = 0.727 \times 32 + 0.273 \times 43 = 23.27 + 11.73 = 35.0$ wt% Ni $= C_0$.
>
> **Answer.** At 1250 °C the alloy is 73 % liquid of 32 wt% Ni and 27 % solid α of 43 wt% Ni. The alloy point is closer to the liquidus, so there is more liquid.

> [!warning] Rounding on the slide
> Slide 21 writes $W_L = 0.72$ and $W_\alpha = 0.28$. The exact values are $8/11 = 0.727$ and $3/11 = 0.273$, so they round to 0.73 and 0.27, as the official solutions of the problem sheet write them (Solution problems Phase diagrams I.pdf, p. 5). The slide truncates $W_L$ and then takes $W_\alpha = 1 - W_L$.

> [!example] Worked example 4 — The same alloy during equilibrium cooling [Session 7 Slide 23]
> Slide 23 prints the equilibrium compositions of the liquid and the solid at several temperatures for the same Cu-35 wt% Ni alloy. Applying the lever rule at each one:
>
> | Point | $C_L$ (wt% Ni) | $C_\alpha$ (wt% Ni) | $W_L = \dfrac{C_\alpha - C_0}{C_\alpha - C_L}$ | $W_\alpha$ |
> | :--- | ---: | ---: | ---: | ---: |
> | b′ (liquidus) | 35 | 46 | $\dfrac{46 - 35}{46 - 35} = 1$ | 0 |
> | c′ | 29 | 40 | $\dfrac{40 - 35}{40 - 29} = \dfrac{5}{11} = 0.455$ | 0.545 |
> | d′ (solidus) | 24 | 35 | $\dfrac{35 - 35}{35 - 24} = 0$ | 1 |
>
> **Interpretation.** At b′ the first solid appears, of 46 wt% Ni, in a liquid that still has the composition of the alloy. As the temperature falls both phases become poorer in Ni (the liquid follows the liquidus, the solid follows the solidus) and the amount of solid grows. At d′ the solid has reached the composition of the alloy, 35 wt% Ni, and the last liquid disappears: in equilibrium, solidification ends on the solidus.

## 7. Non-equilibrium solidification [Session 7 Slides 23-24]

When the alloy goes down through the phase diagram too quickly (high cooling rates), solid-state diffusion has no time to keep the whole solid at the equilibrium composition. Only the surface of each growing crystal has the composition of the solidus; the inside keeps the composition it had when it formed. The result is a microstructure of **heterogeneous composition**, called **microsegregation** (or **cored structure**).

![[attachments/T4/coring.svg]]

In the Cu-35 wt% Ni alloy the first solid is α of 46 wt% Ni (b′). At c′ the new layer is α of 40 wt% Ni, but the crystal still has its 46 % core, so its **average** composition is 42 wt% Ni instead of 40; at d′ the average is 38 instead of 35; at e′ it is 35. The average compositions follow a **non-equilibrium solidus** (dashed) that lies to the right of the equilibrium solidus, so liquid survives below the equilibrium solidus and solidification ends only at e′. The final grains are cored: 46 wt% Ni at the centre and 31 wt% Ni at the edge (f′).

The same behaviour in an alloy of Ni-30 wt% Cu (Slide 24): with fast cooling the solid follows the non-equilibrium solidus α′₂ … α′₇ and solidification ends at $T_7$ instead of $T_5$:

![[attachments/T4/coring-nicu.svg]]

![[attachments/T4/s7-coring-sketches.png]]

![[attachments/T4/s7-coring-micrograph.png]]

**Removing the coring.** Microsegregation can be eliminated with a **homogenisation heat treatment** at a temperature below the solidus (for example $T_{TT} < T_7$, below the lowest temperature at which liquid could exist). During the treatment, solid-state diffusion (Topic 3) evens out the composition inside the grains [Session 7 Slide 24].

> [!example] Worked example 5 — How much liquid is left at d′ with fast cooling [Session 7 Slide 23]
> **Data from the slide.** At d′ the liquid is $C_L$ = 24 wt% Ni, and the average composition of the cored solid is 38 wt% Ni (the dashed line). The alloy is $C_0$ = 35 wt% Ni.
>
> **Lever rule on the average composition.** The tie line now ends on the non-equilibrium solidus, at 38 wt% Ni:
> $$W_L = \frac{38 - 35}{38 - 24} = \frac{3}{14} = 0.214 \qquad W_\alpha = \frac{35 - 24}{38 - 24} = \frac{11}{14} = 0.786$$
>
> **Comparison.** In equilibrium (Worked example 4) the alloy is completely solid at d′. With fast cooling about 21 % of the alloy is still liquid there; solidification ends only at e′, where the average composition of the solid reaches 35 wt% Ni and $W_L = (35 - 35)/(35 - 21) = 0$. The slide gives the average compositions; the lever rule is used here with them exactly as in §6.

## 8. Binary eutectic systems [Session 7 Slides 26-32]

### 8.1 Partial solid solubility and the eutectic reaction [Session 7 Slides 26-27]

When the two components have only **partial solid solubility**, two solid solutions appear: α, rich in A, and β, rich in B. Their regions are bounded by three kinds of line:

- the **liquidus**, above which everything is liquid;
- the **solidus**, below which there is no liquid;
- the **solvus**, which gives the maximum solubility of B in α (and of A in β) at each temperature in the solid state.

![[attachments/T4/eutectic-generic.svg]]

The two liquidus lines meet at the **eutectic point**, defined by the **eutectic temperature** and the **eutectic composition**. A liquid of eutectic composition does not pass through a two-phase L + solid region: at the eutectic temperature it transforms at once into **two** solids, in a fine microstructure of alternating layers of α and β.

**Invariant reactions** are produced at a fixed composition and a fixed temperature for a given system, and the result also remains fixed. In a system of two partially soluble components, a solidification reaction occurs at a fixed composition and temperature, with a cooling curve similar to that of a pure solid [Session 7 Slide 27]. This is the **eutectic reaction**:

$$L \;\rightarrow\; \alpha + \beta \quad \text{(on cooling, at the eutectic temperature)}$$

![[attachments/T4/eutectic-cooling.svg]]

With the phase rule of §5 at 1 atm: at the eutectic point three phases (L, α, β) coexist in a two-component system, so $F = 2 - 3 + 1 = 0$. Temperature and the compositions of the three phases are all fixed, which is why the reaction is invariant and the cooling curve shows a plateau.

### 8.2 The Pb-Sn system and the eutectic microstructure [Session 7 Slides 28-29]

The Pb-Sn diagram is the example of the slides. Its eutectic point is at **61.9 wt% Sn and 183 °C**. At 183 °C, α can dissolve at most **18.3 wt% Sn** and β contains **97.8 wt% Sn** [Session 7 Slide 32]. The melting points of the pure metals are 327 °C (Pb) and 232 °C (Sn) (Problems T4_PhaseDiagrams I.pdf, p. 1).

![[attachments/T4/pbsn.svg]]

A liquid of 61.9 wt% Sn, cooled to 183 °C, forms colonies of α and β layers that grow together into the liquid until the whole structure is eutectic (the **eutectic product**). The layers alternate with a spacing λ:

![[attachments/T4/s7-eutectic-sketches.png]]

![[attachments/T4/s7-eutectic-lamellae.png]]

![[attachments/T4/s7-pbsn-eutectic-micrograph.png]]

The shape of the eutectic changes from one system to another: rods, plates, globules or needles of one phase in the other.

![[attachments/T4/s7-eutectic-micrographs.png]]

> [!note] Pb-Sn values in the problem sheet
> The diagram printed in the problem sheet (Problems T4_PhaseDiagrams I.pdf, p. 1) and the official solutions use 19.2 wt% Sn for α and 97.5 wt% Sn for β at 183 °C, instead of the 18.3 and 97.8 of Slide 32: they come from a different drawing of the same system. The worked examples of this page use the slide values; the solved problems use the values of the sheet.

> [!example] Worked example 6 — Phases in the Pb-Sn eutectic product [Session 7 Slides 28, 32]
> **Question.** A Pb-61.9 wt% Sn alloy (eutectic composition) is cooled just below 183 °C. What are the amounts of α and β in the eutectic?
>
> **Tie line.** Just below 183 °C the tie line crosses the α + β region from $C_\alpha$ = 18.3 to $C_\beta$ = 97.8 wt% Sn; its length is $97.8 - 18.3 = 79.5$ wt% Sn.
>
> **Lever rule.**
> $$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{97.8 - 61.9}{97.8 - 18.3} = \frac{35.9}{79.5} = 0.452 \qquad W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{61.9 - 18.3}{79.5} = \frac{43.6}{79.5} = 0.548$$
>
> **Check.** $0.452 + 0.548 = 1$ and $0.452 \times 18.3 + 0.548 \times 97.8 = 8.27 + 53.59 = 61.9$ wt% Sn $= C_0$.
>
> **Answer.** The alloy is 100 % eutectic microconstituent, and inside it 45.2 % of the mass is α and 54.8 % is β. Every eutectic of this system, whatever the alloy it comes from, has these proportions (used in Worked example 7).

### 8.3 Hypoeutectic and hypereutectic alloys [Session 7 Slides 30-31]

An alloy between the α limit and the eutectic composition is **hypoeutectic**; one between the eutectic composition and the β limit is **hypereutectic**.

**Hypoeutectic alloy** (the slide uses Pb-Sn with about 30 wt% Sn, a reading of the figure):

![[attachments/T4/hypoeutectic.svg]]

1. Above the liquidus the alloy is liquid. The cooling curve shows the liquidus at 260 °C, where crystals of α start to form.
2. Between 260 and 183 °C, α and liquid coexist; α grows, and the liquid becomes richer in Sn along the liquidus.
3. Just above 183 °C the solid is α of about 19 wt% Sn and the liquid has reached the eutectic composition, 61.9 wt% Sn.
4. At 183 °C that liquid transforms at constant temperature into the eutectic ($L \rightarrow \alpha + \beta$): a plateau in the cooling curve.
5. Below 183 °C the structure is **primary (proeutectic) α** surrounded by **eutectic**.

![[attachments/T4/s7-hypoeutectic-sketches.png]]

![[attachments/T4/s7-hypoeutectic-micrograph.png]]

In a casting, the primary α grows from the mould wall, and the liquid trapped between the crystals is the last to solidify, with the eutectic composition:

![[attachments/T4/s7-hypoeutectic-mould.png]]

**Hypereutectic alloy:** the same sequence with the roles of the solids exchanged. Primary β forms between the liquidus and the eutectic temperature, the remaining liquid gives the eutectic at the eutectic temperature, and the final structure is **primary β plus eutectic**.

![[attachments/T4/hypereutectic.svg]]

![[attachments/T4/s7-hypereutectic-sketches.png]]

![[attachments/T4/s7-hypereutectic-micrograph.png]]

(The cooling curve of Slide 31 repeats the temperature labels of the hypoeutectic curve, 260 and 183 °C; for a hypereutectic Pb-Sn alloy the liquidus is below 232 °C, so the curve is drawn here with generic labels $T_L$ and $T_E$.)

### 8.4 Lever rule in binary eutectic diagrams [Session 7 Slide 32]

Just below the eutectic temperature, the tie line of a hypoeutectic alloy $C'_4$ is cut by the alloy and by the eutectic composition into three segments, $P$, $Q$ and $R$:

![[attachments/T4/eutectic-lever.svg]]

$$W_{\alpha'} = \frac{Q}{P + Q} \qquad W_e = W_L = \frac{P}{P + Q} \qquad W_\alpha = \frac{Q + R}{P + Q + R} \qquad W_\beta = \frac{P}{P + Q + R}$$

- $W_e$: fraction of eutectic microconstituent, equal to $W_L$, the fraction of liquid just above the eutectic temperature (all that liquid becomes eutectic);
- $W_{\alpha'}$: fraction of α′ phase, the **primary** α;
- $W_\alpha$: **total** fraction of α (primary α plus the α inside the eutectic);
- $W_\beta$: fraction of β phase (all of it inside the eutectic).

The first two use the short tie line between α and the eutectic liquid (microconstituents); the last two use the whole tie line between α and β (phases).

> [!example] Worked example 7 — Microconstituents and phases of Pb-30 wt% Sn [Session 7 Slides 30, 32]
> **Data.** Alloy $C_0$ = 30 wt% Sn (the hypoeutectic alloy of Slide 30), just below 183 °C, with the values of Slide 32: $C_\alpha$ = 18.3, $C_e$ = 61.9, $C_\beta$ = 97.8 wt% Sn.
>
> **Step 1, the segments.** $P = C_0 - C_\alpha = 30 - 18.3 = 11.7$; $Q = C_e - C_0 = 61.9 - 30 = 31.9$; $R = C_\beta - C_e = 97.8 - 61.9 = 35.9$; so $P + Q = 43.6$ and $P + Q + R = 79.5$ (all in wt% Sn).
>
> **Step 2, microconstituents** (short tie line, from α to the eutectic liquid):
> $$W_{\alpha'} = \frac{Q}{P+Q} = \frac{31.9}{43.6} = 0.732 \qquad W_e = \frac{P}{P+Q} = \frac{11.7}{43.6} = 0.268$$
>
> **Step 3, phases** (whole tie line, from α to β):
> $$W_\alpha = \frac{Q+R}{P+Q+R} = \frac{67.8}{79.5} = 0.853 \qquad W_\beta = \frac{P}{P+Q+R} = \frac{11.7}{79.5} = 0.147$$
>
> **Step 4, the α inside the eutectic.** It is the total α minus the primary α: $W_{\alpha,e} = W_\alpha - W_{\alpha'} = 0.853 - 0.732 = 0.121$.
>
> **Check, phases against microconstituents.** By Worked example 6 every eutectic is 45.2 % α and 54.8 % β. Then $W_e \times 0.452 = 0.268 \times 0.452 = 0.121 = W_{\alpha,e}$ and $W_e \times 0.548 = 0.268 \times 0.548 = 0.147 = W_\beta$: both descriptions of the alloy agree.
>
> **Answer.** Just below 183 °C the alloy is 73.2 % primary α and 26.8 % eutectic. Counting phases, it is 85.3 % α (73.2 % primary plus 12.1 % in the eutectic) and 14.7 % β. Just above 183 °C the same lever gives 73.2 % α of 18.3 wt% Sn and 26.8 % liquid of 61.9 wt% Sn: that liquid is what becomes the eutectic.

See also [[Concept - Phases, Components and Microconstituents]], [[Concept - Gibbs Phase Rule]], [[Concept - Tie Line and Lever Rule]], [[Concept - Binary Eutectic Systems and Microconstituents]].

---

**Back to:** [[Aerospace Materials I MOC]]
