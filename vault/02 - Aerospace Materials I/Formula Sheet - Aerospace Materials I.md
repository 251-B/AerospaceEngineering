---
materia: "Aerospace Materials I"
subject: "Aerospace Materials I"
topic: "Formula sheet and solving compendium, Units 4 to 7"
tags:
  - formula-sheet
  - cheat-sheet
  - quick-reference
  - aerospace-materials-1
sources:
  - "sources/cuatrimestre-1/02-aerospace-materials-1/unit-04-phase-diagrams/teoria/Session 7 T4 Phase diagrams I_2025.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/unit-05-mechanical-properties/teoria/Session 11 T5 Mechanical properties I.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/unit-06-electrical-properties/teoria/Session 13 T6 Electrical properties.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/unit-07-magnetic-thermal-properties/teoria/Session 15 T7 Magnetic and thermal properties.pdf"
web: "subjects/aerospace-materials-1/formula-sheet/index.html"
---

# Formula Sheet - Aerospace Materials I

Every formula and every way of calculating that the problems of Units 4 to 7 need (phase diagrams, mechanical properties, electrical properties, magnetic and thermal properties), with where it comes from, how to use it, and the mistakes that cost marks. It gathers the theory notes [[Topic 4 - Phase Diagrams and Solidification]], [[Topic 5 - Mechanical Properties]], [[Topic 6 - Electrical Properties]] and [[Topic 7 - Magnetic and Thermal Properties]] and the solved problems of those units, and keeps the notation and citations of the course slides (Session N Slide M). Anything the slides do not state is marked as an extension.

The page `subjects/aerospace-materials-1/formula-sheet/index.html` is generated from this note by `python tools/build_formula_sheet.py`; edit this note, never the page. Card headings are `### <Kind>: <title>`; a derivation card opens with an `In short:` line; tables headed `| Step | Why |` become the step grid.

## How to solve a materials problem
Pages: Problems=problemas/index.html; Extra problems=extra-problems/index.html

### Algorithm: The order of the course
1. **Data.** Write every datum with its unit and convert to one coherent set: lengths in mm and forces in N give stresses in MPa ($1\ \text{MPa} = 1\ \text{N/mm}^2$); electrical data in SI; temperatures in kelvin whenever an exponential or a ratio of temperatures appears.
2. **Model.** Name the law of the slides that applies (Hooke, lever rule, Matthiessen, Fourier...), with its hypotheses, and say why it holds in this case (elastic zone? two-phase region? intrinsic range?).
3. **Calculation.** One operation per line, symbols first and numbers after; keep three or four significant figures and round only at the end.
4. **Result and checks.** Units, order of magnitude, limiting cases (fractions add to 1, $W \in [0,1]$, $\sigma_y < \sigma_{UTS}$, $\varepsilon_p < \varepsilon_f$), and the official key.

### Table: Constants and conversions
| Quantity | Value | Where it is used |
| :--- | :--- | :--- |
| Boltzmann constant | $k_B = 8.62\times10^{-5}\ \text{eV/K} = 1.38\times10^{-23}\ \text{J/K}$ | semiconductors, Unit 6 |
| Electron volt | $1\ \text{eV} = 1.602\times10^{-19}\ \text{J}$ | band gaps, donor levels |
| Electron charge, mass | $\lvert q_e\rvert = 1.602\times10^{-19}\ \text{C}$ (the slides round to $1.6\times10^{-19}$); $m_e = 9.109\times10^{-31}\ \text{kg}$ | conductivity, drift |
| Permeability of vacuum | $\mu_0 = 1.257\times10^{-6}\ \text{H/m}$ | magnetism |
| Permittivity of vacuum | $\varepsilon_0 = 8.85\times10^{-12}\ \text{F/m}$ | dielectrics |
| Bohr magneton | $\mu_B = 9.27\times10^{-24}\ \text{A}\cdot\text{m}^2$ | magnetic moments |
| Gas constant | $R = 8.314\ \text{J/(mol}\cdot\text{K)}$; $1\ \text{cal} = 4.184\ \text{J}$ | heat capacity, $3R$ |
| Lorenz number | $L = 2.44\times10^{-8}\ \text{W}\cdot\Omega/\text{K}^2$ | Wiedemann-Franz |
| Temperature | $T\,[\text{K}] = T\,[^\circ\text{C}] + 273.15$ | every exponential |
| Resistivity units | $1\ \mu\Omega\cdot\text{cm} = 10^{-8}\ \Omega\cdot\text{m}$; $1\ \Omega\cdot\text{cm} = 10^{-2}\ \Omega\cdot\text{m}$ | metals |
| Stress | $1\ \text{MPa} = 1\ \text{N/mm}^2 = 10^6\ \text{Pa}$; $1\ \text{GPa} = 10^3\ \text{MPa}$ | mechanical |
| Energy per volume | $1\ \text{MPa} = 1\ \text{MJ/m}^3$ | toughness, resilience |
| Force and length | $1\ \text{kgf} = 9.81\ \text{N}$; $1\ \text{in} = 25.4\ \text{mm}$ (extension) | hardness loads, ASTM specimen |

### Algorithm: Linear interpolation between two data points
Use it whenever a table or a straight boundary gives two points $(x_1, y_1)$ and $(x_2, y_2)$ around the value you need: a row of a load-elongation table, a stress-strain table, a straight liquidus or solvus of a diagram you must draw with straight lines.
1. **Bracket.** Find the two consecutive rows with $x_1 \le x \le x_2$ (or $y_1 \le y \le y_2$ if you look for $x$).
2. **Direct reading.** $y = y_1 + \dfrac{y_2 - y_1}{x_2 - x_1}\,(x - x_1)$.
3. **Inverse reading.** $x = x_1 + \dfrac{y - y_1}{y_2 - y_1}\,(x_2 - x_1)$.
4. **Check.** The result must lie between $y_1$ and $y_2$; the slope $m = (y_2 - y_1)/(x_2 - x_1)$ keeps the units of $y/x$ (MPa for $\sigma$ against $\varepsilon$).
5. **Diagram boundary.** On a straight line of the diagram, the composition at temperature $T$ is $C = C_1 + (C_2 - C_1)\,\dfrac{T - T_1}{T_2 - T_1}$.

Example (Problem T5-07, strain read at the service stress $277.00$ MPa between the rows $(0.00350,\ 258.68)$ and $(0.01496,\ 277.16)$): $\varepsilon = 0.00350 + \dfrac{277.00 - 258.68}{277.16 - 258.68}\,(0.01496 - 0.00350) = 0.01486$.

### Trap: Mistakes that cost the most marks
- Mixing units: force in kN against area in mm$^2$ (a factor $10^3$), $\varepsilon$ in % against $\varepsilon$ as a ratio, diameter against radius in $A = \pi d^2/4$.
- Using Hooke's law ($\sigma = E\varepsilon$) outside the elastic zone: past the yield point read the table or the curve.
- Forgetting that the lever rule uses the arm **opposite** to the phase, and that microconstituents and phases use different tie lines.
- Putting a temperature in $^\circ$C into $\exp(-E_g/2kT)$: it must be kelvin.
- Rounding intermediate values: carry at least four significant figures and round at the end.
- Giving a result without unit or without the check that the fractions add up to 1.

## Unit 4 — Phase diagrams and solidification
Pages: Theory=teoria/topic-4-phase-diagrams.html; Problems=problemas/topic-4-phase-diagrams.html

### Definition: Component, phase, microconstituent
- **Component:** a pure element or compound that forms the alloy (the axes of the diagram) [Session 7 Slide 2].
- **Phase:** a homogeneous part of the system, with its own composition and structure, separated from the rest by an interface (liquid, $\alpha$, $\beta$, Fe$_3$C).
- **Microconstituent:** what the microscope shows as one structure: it can be one phase (primary $\alpha$) or a mixture of phases (eutectic, pearlite). **Counting phases and counting microconstituents are two different questions, with two different tie lines.**

### Theorem: Gibbs phase rule
$$F = C - P + N \qquad N = 2\ (T,\ p) \qquad F = C - P + 1\ \ (p = 1\ \text{atm})$$
- $F$: degrees of freedom; $C$: components; $P$: phases present; $N$: non-compositional variables [Session 7 Slide 13].
- Binary alloy at 1 atm: one phase $F = 2$ (T and composition free); two phases $F = 1$ (choosing T fixes the compositions: this is why the tie line is horizontal); three phases (invariant point or line) $F = 0$.
- Unary diagram (water): $F = 1 - P + 2$; triple point $F = 0$.

### Theorem: Tie line and lever rule
In a two-phase region of a binary diagram at temperature $T$, draw the horizontal tie line through the point of the alloy $C_0$. Its ends on the boundaries give the composition of each phase, $C_L$ and $C_\alpha$.
$$W_L = \frac{C_\alpha - C_0}{C_\alpha - C_L} \qquad W_\alpha = \frac{C_0 - C_L}{C_\alpha - C_L} \qquad W_L + W_\alpha = 1$$
- **Rule:** the fraction of a phase is the length of the arm **on the other side** of $C_0$, divided by the whole tie line [Session 7 Slides 15-16].
- The composition axis is in wt%, so $W$ are **mass** fractions. On an atomic-% axis the same construction gives atom (mole) fractions (extension).
- Mass balance check: $W_L C_L + W_\alpha C_\alpha = C_0$.
- Solving backwards: from a measured fraction, $C_0 = C_\alpha + W_\beta\,(C_\beta - C_\alpha)$ (Problems T4-FC05 to FC07).

### Algorithm: Any point of a binary diagram
1. Locate the point $(C_0, T)$ and name the region (one phase, two phases, three phases on a line).
2. **One phase:** $W = 100\,\%$ and its composition is $C_0$.
3. **Two phases:** horizontal tie line through the point, read the compositions at its ends, apply the lever rule.
4. **On an invariant line:** use the tie line just above and just below the line; the liquid just above becomes the eutectic (or the peritectic product).
5. **Microconstituents:** at the first temperature below the invariant line, use the short tie line (see the eutectic card).
6. Check $\sum W = 1$ and the mass balance of the composition.

### Pattern: Eutectic system, phases and microconstituents
Eutectic reaction $L \rightarrow \alpha + \beta$ at $T_E$, with $C_\alpha < C_e < C_\beta$ (Pb-Sn: $T_E = 183\,^\circ$C, $C_\alpha = 18.3$, $C_e = 61.9$, $C_\beta = 97.8$ wt% Sn) [Session 7 Slides 28-32].

| Alloy | Microconstituents just below $T_E$ | Phases just below $T_E$ |
| :--- | :--- | :--- |
| Hypoeutectic $C_\alpha < C_0 < C_e$ | primary $\alpha$: $\dfrac{C_e - C_0}{C_e - C_\alpha}$; eutectic: $\dfrac{C_0 - C_\alpha}{C_e - C_\alpha}$ | $\alpha$: $\dfrac{C_\beta - C_0}{C_\beta - C_\alpha}$; $\beta$: $\dfrac{C_0 - C_\alpha}{C_\beta - C_\alpha}$ |
| Hypereutectic $C_e < C_0 < C_\beta$ | primary $\beta$: $\dfrac{C_0 - C_e}{C_\beta - C_e}$; eutectic: $\dfrac{C_\beta - C_0}{C_\beta - C_e}$ | same formulas as above |
| Eutectic $C_0 = C_e$ | 100 % eutectic | $\alpha$: $\dfrac{C_\beta - C_e}{C_\beta - C_\alpha} = 0.452$; $\beta$: $0.548$ (Pb-Sn) |

- The first pair uses the **short** tie line (from the solvus of the primary phase to the eutectic composition); the second pair uses the **whole** tie line from $\alpha$ to $\beta$.
- The fraction of eutectic equals the fraction of liquid just above $T_E$: all that liquid becomes eutectic.
- $\alpha$ inside the eutectic: $W_{\alpha,e} = W_\alpha - W_{\text{primary}\ \alpha} = W_e\,\dfrac{C_\beta - C_e}{C_\beta - C_\alpha}$. Check: Pb-30 Sn gives $W_{\alpha'} = 0.732$, $W_e = 0.268$, $W_\alpha = 0.853$, $W_\beta = 0.147$ and $0.268 \times 0.452 = 0.121 = 0.853 - 0.732$.

### Derivation: Phase fractions of an alloy from its microconstituents
In short: a eutectic is a fixed mixture of $\alpha$ and $\beta$, so the phase content of any eutectic alloy is its primary phase plus the eutectic times that fixed mixture.

| Step | Why |
| --- | --- |
| $W_{\alpha,e}^{\text{in eutectic}} = \dfrac{C_\beta - C_e}{C_\beta - C_\alpha}$ | lever rule on the whole tie line at the eutectic composition |
| $W_\alpha = W_{\alpha'} + W_e\,W_{\alpha,e}^{\text{in eutectic}}$ | total $\alpha$ is primary $\alpha$ plus the $\alpha$ of the eutectic |
| $W_\beta = W_e\,\bigl(1 - W_{\alpha,e}^{\text{in eutectic}}\bigr)$ | all the $\beta$ of a hypoeutectic alloy lies inside the eutectic |
| $W_\alpha + W_\beta = 1$ | check against the direct lever rule on the whole tie line |

### Pattern: Solid-state precipitation (solvus)
When the alloy crosses the **solvus** on cooling, the solubility of $\alpha$ is exceeded and particles of $\beta$ precipitate and grow as $T$ falls [Session 8 Slides 3-4].
$$W_\beta(T) = \frac{C_0 - C_\alpha(T)}{C_\beta - C_\alpha(T)} \qquad W_\alpha(T) = \frac{C_\beta - C_0}{C_\beta - C_\alpha(T)}$$
- Above the solvus the alloy is single-phase $\alpha$ of composition $C_0$ ($W_\alpha = 1$).
- $C_\alpha(T)$ is read on the solvus at the temperature asked; Pb-16 Sn at 121 $^\circ$C: $W_\beta = \dfrac{16 - 6}{99 - 6} = 0.108$ [Session 8 Slide 4].

### Table: The five invariant reactions
| Reaction | On cooling | Shape on the diagram | Example |
| :--- | :--- | :--- | :--- |
| Eutectic | $L \rightarrow \alpha + \beta$ | liquid region ends in a V on the horizontal line | Pb-Sn |
| Peritectic | $\alpha + L \rightarrow \beta$ | solid region ends in an inverted V below the line | Cu-Zn, Fe-Ni |
| Monotectic | $L_1 \rightarrow L_2 + \alpha$ | liquid miscibility gap above the line | Cu-Pb |
| Eutectoid | $\gamma \rightarrow \alpha + \beta$ | like the eutectic with a solid $\gamma$ | Fe-C (pearlite) |
| Peritectoid | $\alpha + \beta \rightarrow \gamma$ | like the peritectic with two solids | Ti-Si |

Reading rule: the **single phase** is at the top of the V for eutectic, eutectoid and monotectic reactions, and at the bottom of the inverted V for peritectic and peritectoid reactions. The lever rule on the horizontal line just above or below it uses the compositions of the three points of the line (Slides 6-12 of Session 8).

### Pattern: Intermetallic compounds and melting
- A **stoichiometric compound** is a vertical line on the diagram (fixed composition) and divides the diagram into independent sub-diagrams, each treated with its own lever rule [Session 8 Slides 14-15].
- **Congruent melting:** the compound melts at one temperature into a liquid of its own composition (the vertical line reaches the liquidus at a maximum). **Incongruent melting:** it decomposes into a liquid and another solid (a peritectic reaction) [Session 8 Slide 17].
- For an alloy between two compounds $A$ and $B$ of composition $C_A$ and $C_B$: $W_A = \dfrac{C_B - C_0}{C_B - C_A}$, $W_B = \dfrac{C_0 - C_A}{C_B - C_A}$ (Ti-30 Si between Ti$_3$Si at 25 % and Ti$_5$Si$_3$ at 35 %: $0.5$ and $0.5$).

### Table: Fe-Fe3C diagram, the numbers to remember
| Item | Value | Note |
| :--- | :--- | :--- |
| Maximum C in ferrite $\alpha$ | $0.022$ wt% at 727 $^\circ$C | BCC, soft, 7.88 g/cm$^3$ |
| Eutectoid point | $0.76$ wt% C at 727 $^\circ$C | $\gamma\,(0.76) \rightleftharpoons \alpha\,(0.022) + \text{Fe}_3\text{C}\,(6.67)$, product pearlite |
| Maximum C in austenite $\gamma$ | $2.14$ wt% at 1147 $^\circ$C | FCC, not magnetic |
| Eutectic point | $4.30$ wt% C at 1147 $^\circ$C | $L\,(4.30) \rightleftharpoons \gamma\,(2.14) + \text{Fe}_3\text{C}\,(6.67)$, product ledeburite |
| Peritectic | 1493 $^\circ$C | $\delta\,(0.09) + L\,(0.53) \rightleftharpoons \gamma\,(0.16)$ |
| Cementite Fe$_3$C | $6.67$ wt% C | hard, brittle, metastable compound |
| Steels | up to $2.14$ % C | hypoeutectoid up to $0.76$, hypereutectoid from $0.76$ to $2.14$ |
| Cast irons | $2.14$ to $6.67$ % C | hypoeutectic $2.14$ to $4.30$, hypereutectic $4.30$ to $6.67$ |
| Lines | $A_1$ (727 $^\circ$C), $A_3$ ($\gamma$ / $\alpha + \gamma$), $A_{cm}$ ($\gamma$ / $\gamma + \text{Fe}_3\text{C}$) | heat-treatment names |

The drawing of Slide 20 prints older values ($0.8$ % C, 723 $^\circ$C) for the eutectoid; the course uses $0.76$ % and 727 $^\circ$C. Some readings of the slides use $0.02$ instead of $0.022$ for the ferrite limit: use the same value throughout one problem.

### Pattern: Steels below 727 degrees Celsius
Just below the eutectoid line, with $C_\alpha = 0.022$, $C_E = 0.76$ and $C_{\text{Fe}_3\text{C}} = 6.67$ % C [Session 9 Slides 12-20].

| Steel | Microconstituents | Phases |
| :--- | :--- | :--- |
| Eutectoid $C_0 = 0.76$ | 100 % pearlite | $\alpha$: $\dfrac{6.67 - 0.76}{6.648} = 0.889$; Fe$_3$C: $0.111$ |
| Hypoeutectoid $C_0 < 0.76$ | primary $\alpha$: $\dfrac{0.76 - C_0}{0.76 - 0.022}$; pearlite: $\dfrac{C_0 - 0.022}{0.76 - 0.022}$ | $\alpha$: $\dfrac{6.67 - C_0}{6.648}$; Fe$_3$C: $\dfrac{C_0 - 0.022}{6.648}$ |
| Hypereutectoid $C_0 > 0.76$ | primary Fe$_3$C: $\dfrac{C_0 - 0.76}{6.67 - 0.76}$; pearlite: $\dfrac{6.67 - C_0}{6.67 - 0.76}$ | $\alpha$: $\dfrac{6.67 - C_0}{6.648}$; Fe$_3$C: $\dfrac{C_0 - 0.022}{6.648}$ |

- **Every pearlite**, in any steel, is $88.9$ % ferrite and $11.1$ % cementite: it is a fixed mixture.
- Above 727 $^\circ$C (between $A_3$ and $A_1$) the two phases are $\alpha$ and $\gamma$: use the tie line from $0.022$ (or $0.02$) to the $A_3$ composition at that temperature.
- Ferrite of the pearlite: $W_{\alpha,\text{pearlite}} = W_{\text{pearlite}} \times 0.889$.
- Check, 0.3 % C steel: primary $\alpha = 0.623$, pearlite $= 0.377$, total $\alpha = 0.958$, Fe$_3$C $= 0.042$.
- Check, 1.2 % C steel: primary Fe$_3$C $= 0.074$, pearlite $= 0.926$, total Fe$_3$C $= 0.177$.

### Pattern: Cast irons
Use the eutectic tie lines: $\gamma\,(2.14)$ to $L\,(4.30)$ for hypoeutectic and $L\,(4.30)$ to Fe$_3$C $(6.67)$ for hypereutectic alloys, at $1147\,^\circ$C $+\ \Delta T$.
- **Hypoeutectic ($2.14 < C_0 < 4.30$), just above 1147 $^\circ$C:** $W_{\gamma,p} = \dfrac{4.30 - C_0}{4.30 - 2.14}$, $W_L = \dfrac{C_0 - 2.14}{4.30 - 2.14}$.
- **Hypereutectic ($4.30 < C_0 < 6.67$), just above 1147 $^\circ$C:** $W_{\text{Fe}_3\text{C},p} = \dfrac{C_0 - 4.30}{6.67 - 4.30}$, $W_L = \dfrac{6.67 - C_0}{6.67 - 4.30}$.
- **Just below 1147 $^\circ$C (phases):** $W_{\text{Fe}_3\text{C}} = \dfrac{C_0 - 2.14}{6.67 - 2.14}$, $W_\gamma = \dfrac{6.67 - C_0}{6.67 - 2.14}$.
- **Ledeburite** (eutectic) is $52.3$ % austenite and $47.7$ % cementite; below 727 $^\circ$C its austenite becomes pearlite.
- Between 1147 and 727 $^\circ$C the austenite loses carbon along $A_{cm}$ and secondary cementite forms: use the tie line from $\gamma$ on $A_{cm}$ to $6.67$ (Problem T4-FC09: $W_{\text{Fe}_3\text{C}}(800) = \dfrac{3.0 - 1.0}{6.67 - 1.0}$).
- To find $C_0$ from a measured fraction, invert the lever rule (cards above): Problems T4-FC05 to FC07.

### Pattern: Non-equilibrium cooling, coring
With fast cooling the solid has no time to equalise: the **average** composition of the solid follows a **non-equilibrium solidus** to the right of the equilibrium one, so liquid is left below the equilibrium end of solidification [Session 7 Slides 23-24].
- The lever rule is the same, with the end of the tie line on the non-equilibrium solidus: Cu-35 Ni with $C_L = 24$ and average solid $38$ gives $W_L = \dfrac{38 - 35}{38 - 24} = 0.214$.
- **Homogenisation heat treatment:** hold below the solidus so solid-state diffusion (Unit 3) removes the composition gradient.
- Increasing the cooling rate in steels moves the eutectoid to lower T and lower %C: less primary ferrite and finer pearlite (harder) [Session 9 Slide 21].

### Pattern: Ternary composition triangle
- Corners are the pure components $A$, $B$, $C$; sides are binary alloys; the three percentages of a point add to $100$ %.
- **Reading a point:** the line of constant $\%A$ is parallel to the side opposite to $A$ (the side $B$-$C$), and so on for $B$ and $C$. Draw the three parallels, read each percentage on its own axis and check $\sum = 100$ [Session 10 Slide 5].
- Isotherms (horizontal sections), liquidus projections and solidus surfaces show the system (Ag-Cu-Zn, Fe-Cr-Ni at 650 $^\circ$C); phases of a point are the field where it falls (Slides 6-8).
- Example: $60$ % Cr, $20$ % Fe, $20$ % Ni lies in $\alpha + \gamma$; $74$ % Fe + $18$ % Cr + $8$ % Ni is a commercial stainless steel.

### Pattern: Ceramic diagrams and compounds
- Al$_2$O$_3$-Cr$_2$O$_3$ has complete solid solubility: it is an isomorphous diagram and the lever rule is the same [Session 10 Slide 2].
- Al$_2$O$_3$-SiO$_2$ has the compound mullite $3\text{Al}_2\text{O}_3\cdot2\text{SiO}_2$ (about $72$ wt% Al$_2$O$_3$), with the eutectic $L\,(7.7) \rightarrow \text{mullite} + \text{SiO}_2$ and the peritectic $L\,(77) + \text{Al}_2\text{O}_3 \rightarrow \text{mullite}$. Example: at $7.7$ % Al$_2$O$_3$, $W_{\text{mullite}} = \dfrac{7.7 - 0}{72 - 0} = 0.107$ [Session 10 Slides 3-4].
- Extension: the wt% of a compound $A_xB_y$ is $\dfrac{y\,M_B}{x\,M_A + y\,M_B}$ (mullite: $\dfrac{3 \times 101.96}{3\times101.96 + 2\times60.08} = 71.8$ %).

### Trap: Mistakes in phase diagrams
- Using the arm **next to** the phase instead of the opposite one: the fraction of the phase closer to $C_0$ is the **larger**.
- Applying the whole $\alpha$-$\beta$ tie line to microconstituents (and the short one to phases): always ask first "phases or microconstituents?".
- Forgetting that pearlite is **two** phases (88.9 % $\alpha$ + 11.1 % Fe$_3$C) when counting total ferrite or cementite.
- Reading the tie line at the wrong temperature: it is horizontal and must be at the temperature asked, just above or just below an invariant line.
- Reading compositions in at% as wt% (check the axis label).
- Taking the primary phase of a hypereutectic alloy to be $\alpha$ (it is $\beta$) or of a hypereutectoid steel to be ferrite (it is cementite).

## Unit 5 — Mechanical properties
Pages: Theory=teoria/topic-5-mechanical-properties.html; Problems=problemas/topic-5-mechanical-properties.html

### Definition: Engineering stress and strain
$$\sigma_n = \frac{F}{A_0} \qquad \varepsilon_n = \frac{l - l_0}{l_0} = \frac{\Delta l}{l_0} \qquad A_0 = \frac{\pi d_0^2}{4}$$
- $F$ is the load, $A_0$ the original cross-section, $l_0$ the original gauge length [Session 11 Slide 9]. Stress in MPa ($\text{N/mm}^2$) and strain with no units (never in % inside a formula).
- Shear: $\tau = F/A_0$, $\gamma = a/h = \tan\theta$, $\tau = G\gamma$ [Session 11 Slide 7].
- Three-point bend (modulus of rupture): $\text{MOR} = \dfrac{3FL}{2bh^2}$ [Session 11 Slide 6].

### Theorem: Hooke's law and elastic deformation
$$\sigma = E\,\varepsilon \qquad \Delta l = \varepsilon\,l_0 = \frac{F\,l_0}{A_0\,E} \qquad l_0 = \frac{\Delta l\,A_0\,E}{F}$$
- $E$ is the slope of the straight part of the curve; it measures stiffness, depends on the bond strength, and $E_{\text{ceramics}} > E_{\text{metals}} > E_{\text{polymers}}$ [Session 11 Slides 12-13].
- Typical $E$: steel $207$ to $210$ GPa, aluminium $69$ to $70$ GPa, alumina $390$, silica $69$ [Session 11 Slides 13, 17]. Specific modulus: $E/\rho$.
- **Valid only in the elastic zone:** beyond the elastic limit read the table or the curve (Problems T5-01 item i, T5-07).
- **Largest elastic length:** from $\Delta l = F l_0/(A_0E)$ solved for $l_0$ with the largest elastic load (Problem T5-06).

### Theorem: Poisson's ratio and the shear modulus
$$\nu = -\frac{\varepsilon_{\text{transverse}}}{\varepsilon_{\text{longitudinal}}} \qquad \varepsilon_{\text{transverse}} = \frac{\Delta d}{d_0} \qquad E = 2G\,(1 + \nu)$$
- Uniaxial tension: the width shrinks, $\Delta d = -\nu\,\varepsilon_{ax}\,d_0 < 0$ [Session 11 Slide 19].
- Typical $\nu$: metals $0.25$ to $0.4$, polymers $0.3$ to $0.45$, rubber $0.49$; the ideal incompressible limit is $\nu = 0.5$.
- From a measured diameter change: $\varepsilon_{ax} = -\dfrac{\Delta d/d_0}{\nu}$, then $\Delta l = \varepsilon_{ax}\,l_0$ and $E = \sigma/\varepsilon_{ax}$ (Problem T5-07).

### Algorithm: Yield strength by the 0.2 percent offset
1. Draw the elastic line $\sigma = E\varepsilon$ and its parallel through $\varepsilon = 0.002$: **offset line** $\sigma_{off}(\varepsilon) = E\,(\varepsilon - 0.002)$.
2. The yield strength $\sigma_y$ is the stress where the curve crosses the offset line [Session 11 Slide 28].
3. With a table: compute $g = \sigma_n - E(\varepsilon_n - 0.002)$ for each row; the crossing is on the segment where $g$ changes sign.
4. On that segment (rows $a$ and $b$), the curve is the line $\sigma = \sigma_a + m\,(\varepsilon - \varepsilon_a)$ with $m = \dfrac{\sigma_b - \sigma_a}{\varepsilon_b - \varepsilon_a}$. Equate it to the offset line and solve:
$$\varepsilon^* = \frac{\sigma_a - m\,\varepsilon_a + 0.002\,E}{E - m} \qquad \sigma_y = E\,(\varepsilon^* - 0.002)$$
5. Load and elongation at yield: $F_y = \sigma_y A_0$, $\Delta l_y = \varepsilon^* l_0$ (note: $\varepsilon^*$, the **total** strain, not $\varepsilon^* - 0.002$).
6. **Discontinuous yield** (low-carbon steels): $\sigma_y = \dfrac{\sigma_{max} + \sigma_{min}}{2}$ of the upper and lower yield points [Session 11 Slide 28].

Example (Problem T5-01, rows 7 and 8, $E = 196\,160$ MPa): $m = 29\,749$ MPa, $\varepsilon^* = 0.005786$, $\sigma_y = 742.6$ MPa.

### Derivation: The offset intersection
In short: put the straight segment of the table and the offset line equal and solve for the strain at the crossing.

| Step | Why |
| --- | --- |
| $\sigma_{off}(\varepsilon) = E\,(\varepsilon - 0.002)$ | line parallel to the elastic one, shifted by the plastic strain $0.002$ |
| $\sigma(\varepsilon) = \sigma_a + m\,(\varepsilon - \varepsilon_a)$ | between table rows the curve is taken as a straight segment (linear interpolation) |
| $\sigma_a + m(\varepsilon - \varepsilon_a) = E\,(\varepsilon - 0.002)$ | the yield point is on both lines |
| $\sigma_a - m\,\varepsilon_a + 0.002\,E = (E - m)\,\varepsilon$ | collect the terms in $\varepsilon$ |
| $\varepsilon^* = \dfrac{\sigma_a - m\,\varepsilon_a + 0.002\,E}{E - m}$ | solve; $E - m > 0$ because the segment is flatter than the elastic line |

### Theorem: Strength, ductility, toughness and resilience
$$\sigma_{UTS} = \frac{F_{max}}{A_0} \qquad EL\,(\%) = \frac{l_f - l_0}{l_0}\times100 \qquad RA\,(\%) = \frac{A_0 - A_f}{A_0}\times100$$
$$U_r = \int_0^{\varepsilon_y}\sigma\,d\varepsilon = \frac12\,\sigma_y\,\varepsilon_y = \frac{\sigma_y^2}{2E} \qquad \sigma_w = \frac{\sigma_y}{N} \qquad N_{eff} = \frac{\sigma_y}{\sigma_{service}}$$
- **UTS:** maximum nominal stress; with constant $A_0$ it is at the maximum load. Necking follows [Session 11 Slide 30].
- **Elongation after fracture** is measured on the broken pieces: the elastic part is recovered. If the last record before fracture is $(\varepsilon_f,\ \sigma_f)$, then $\varepsilon_p = \varepsilon_f - \sigma_f/E$ and $EL = \varepsilon_p \times 100$ [Session 11 Slide 32].
- **Reduction in area** needs the final area: $A_f = \pi d_f^2/4$; in general $EL\,(\%) \neq RA\,(\%)$ [Session 11 Slide 33].
- **Toughness:** area under the whole curve (energy per volume, MPa $=$ MJ/m$^3$) [Session 11 Slide 34]. By trapezoids over a table: $U_t \approx \sum \tfrac12(\sigma_i + \sigma_{i+1})(\varepsilon_{i+1} - \varepsilon_i)$.
- **Resilience:** area under the elastic line up to $\sigma_y$; high $\sigma_y$ and low $E$ means high resilience (springs) [Session 11 Slide 35].
- **Working stress:** $N$ is between $1.2$ and $4$, usually $2$ when the statement gives none [Session 11 Slide 29]. A cable is safe if $N_{eff} \ge N$ (Problem T5-07).

### Theorem: True stress and true strain
$$\sigma_r = \frac{F}{A_i} = \sigma_n\,\frac{A_0}{A_i} \qquad \varepsilon_r = \int_{l_0}^{l}\frac{dl}{l} = \ln\frac{l}{l_0}$$
- **Before necking** (constant volume, $l_0A_0 = lA_i$): $\sigma_r = \sigma_n\,(1 + \varepsilon_n)$ and $\varepsilon_r = \ln(1 + \varepsilon_n)$ [Session 11 Slide 37].
- **After necking:** use the area, $\sigma_r = F/A_i$ and $\varepsilon_r = \ln\dfrac{A_0}{A_i} = 2\ln\dfrac{d_0}{d_i}$ [Session 11 Slide 38].
- True stress is larger than engineering stress, true strain is smaller than engineering strain, $\sigma_r > \sigma_n$ and $\varepsilon_r < \varepsilon_n$ (for tension).
- **From the reduction in area** (Problem T5-12): $\dfrac{A_f}{A_0} = 1 - \dfrac{RA}{100}$, then $\sigma_{f,r} = \dfrac{\sigma_f}{A_f/A_0}$ and $\varepsilon_r = \ln\dfrac{A_0}{A_f}$.
- The corrected curve after necking accounts for the triaxial stress in the neck.

### Algorithm: Analysis of a tensile test from a load-elongation table
1. **Area:** $A_0 = \pi d_0^2/4$ (mm$^2$). **Rows:** $\sigma_n = F/A_0$ (MPa) and $\varepsilon_n = \Delta L/l_0$ for every point; check the unit of the load column ("N/100" means hundreds of newtons).
2. **Young's modulus:** points that lie on the straight start, $E = \sum\sigma_i\varepsilon_i\big/\sum\varepsilon_i^2$ (least squares through the origin), or the secant $\sigma/\varepsilon$ of one early point.
3. **Yield strength:** offset construction above (algebraic on the sign-change segment).
4. **UTS:** $F_{max}/A_0$ with the largest load of the table.
5. **Ductility:** $\varepsilon_p = \varepsilon_f - \sigma_f/E$ (last row before fracture), $EL = \varepsilon_p\times100$.
6. **Resilience:** $U_r = \sigma_y^2/2E$.
7. **Load or elongation at yield:** $F_y = \sigma_y A_0$, $\Delta l_y = \varepsilon^* l_0$.
8. **Working stress:** $\sigma_w = \sigma_y/N$, $N = 2$ if no value is given.
9. **Load at a given elongation:** if $\Delta l$ is inside the elastic zone use Hooke; otherwise interpolate linearly between the two rows of the table (the interpolation card).

### Pattern: Strengthening mechanisms
All mechanisms work by **blocking the motion of dislocations**; the price is ductility and, in metals, conductivity [Session 12 Slides 4-14].

| Mechanism | What blocks the dislocations | Quantity | Effect on $\sigma_y$ and UTS | Effect on ductility and conductivity |
| :--- | :--- | :--- | :--- | :--- |
| Strain hardening (cold work) | tangles of new dislocations, $10^6$ to $10^{12}\ \text{m/m}^3$ | $\%\text{CW} = \dfrac{A_0 - A_d}{A_0}\times100$ | up | ductility down, conductivity down a little |
| Solid solution | strained lattice around solute atoms (smaller solute: tension; larger: compression) | solute content | up | ductility down, conductivity down a lot |
| Grain size reduction | grain boundaries (smaller $d$, more barriers) | $\sigma_y$ linear in $d^{-1/2}$ | up | ductility generally kept |
| Precipitation (age hardening) | dispersed particles of a second phase | smaller, denser, better dispersed | up (Al-Cu-Mg: UTS $469$ MPa against $45$ pure Al) | conductivity down |

- Extension: the Hall-Petch relation $\sigma_y = \sigma_0 + k_y\,d^{-1/2}$ is the straight line of the slide ($\sigma_0$ and $k_y$ are constants of the material, not given in the slides).
- Extension: for a wire drawn from diameter $d_0$ to $d_d$, $\%\text{CW} = \bigl[1 - (d_d/d_0)^2\bigr]\times100$.
- Cold work produces texture; a recrystallisation anneal restores ductility (Unit 4 diagrams give the temperatures).

### Theorem: Hardness numbers
Hardness is the resistance to a localised plastic indentation [Session 12 Slides 15-30].

| Test | Indenter | Formula | Units and notes |
| :--- | :--- | :--- | :--- |
| Brinell HB (HBW) | ball of diameter $D$ (WC or steel) | $HB = \dfrac{2P}{\pi D\left(D - \sqrt{D^2 - D_i^2}\right)}$ | $P$ in kgf, $D$ and $D_i$ in mm, result in kgf/mm$^2$ |
| Brinell load | | $P = Q\,D^2$ | $Q = 30$ steels, $10$ bronze and brass, $5$ Al alloys, $2.5$ anti-friction alloys |
| Vickers HV | diamond pyramid, $136^\circ$ | $HV = \dfrac{2F\sin(136^\circ/2)}{d^2} = 1.854\,\dfrac{F}{d^2}$ | $F$ in kgf, $d$ the mean of the two diagonals in mm |
| Knoop KHN | diamond pyramid, $l/b = 7.11$ | $KHN = 14.2\,\dfrac{P}{l^2}$ | microhardness, load up to 1 kgf |
| Rockwell HR | diamond cone $120^\circ$ or steel ball | $HR = N - \dfrac{h}{S}$ | $h$ residual depth in mm; $S = 0.002$ mm; $N = 100$ for A, C, D; $N = 130$ for B, E, F, G, K; superficial $N$ and $T$ scales $S = 0.001$, $N = 100$ |

- **Brinell inverse** (indentation diameter for a given $HB$): $k = D - \sqrt{D^2 - D_i^2} = \dfrac{2P}{\pi D\,HB}$, then $D_i^2 = k\,(2D - k)$ (Problem T5-15).
- **Rockwell in depth units:** $HRC = 100 - 500\,t$ and $HRB = 130 - 500\,t$ with $t$ in mm [Session 12 Slide 29].
- **Precautions:** distance to the edge above $4\varnothing$; thickness above $2\varnothing$ (Brinell, Rockwell) or $1.5$ times the diagonal (Vickers).
- **Hardness and strength** both measure plastic deformation, with a different line per material family (chart of Session 12 Slide 30). Extension, for steels only: $\sigma_{UTS}\,[\text{MPa}] \approx 3.45\,HB$.

### Pattern: Thermal stress in a constrained bar (link with Unit 7)
Held at constant length, a bar heated by $\Delta T = T_f - T_0$ develops $\sigma = -E\alpha\,\Delta T$ (compression when heated, tension when cooled). If a load $F$ already acts, the wire stays stretched when $E\alpha\Delta T = F/A$, so $A = \dfrac{F}{E\,\alpha\,\Delta T}$ and $d = \sqrt{4A/\pi}$ (Problem T5-05: $d = 5.87$ mm). The full derivation is in Unit 7.

### Trap: Mistakes in mechanical properties
- Taking the yield strength at the first row below the offset line instead of intersecting with it.
- Using $\varepsilon^* - 0.002$ as the strain at yield: the total strain is $\varepsilon^*$ (elastic plus the $0.002$ offset).
- Measuring ductility at the last point of the table without removing the elastic part $\sigma_f/E$.
- Using engineering values for fracture after necking, or $\ln(1+\varepsilon)$ after necking (it only holds before).
- Using the nominal diameter instead of the instantaneous one for true stress.
- Putting the load in kgf into formulas that need newtons (or the reverse): Brinell and Vickers use kgf.
- Dividing by $A_0$ in mm$^2$ and then treating the result as Pa: it is MPa.
- Confusing resilience (elastic area, $\sigma_y^2/2E$) with toughness (whole area).
- A statement that says "aluminium" with steel-like data: use the data of the statement and state the discrepancy.

## Unit 6 — Electrical properties
Pages: Theory=teoria/topic-6-electrical-properties.html; Problems=problemas/topic-6-electrical-properties.html

### Theorem: Ohm's law, conductivity and mobility
$$V = I\,R \qquad R = \frac{\rho\,l}{A} \qquad \rho = \frac{1}{\sigma} \qquad J = \sigma E \qquad v_d = \mu\,E$$
$$\mu = \frac{\tau\,\lvert q_e\rvert}{m_e} \qquad \sigma = n\,\lvert q_e\rvert\,\mu$$
- $\sigma$ in $(\Omega\cdot\text{m})^{-1}$, $\rho$ in $\Omega\cdot\text{m}$, $\mu$ in m$^2$/(V$\cdot$s), $n$ in m$^{-3}$, $E$ in V/m [Session 13 Slides 10-13].
- Classes by conductivity: insulators $10^{-20}$ to $10^{-10}$, semiconductors $10^{-6}$ to $10^{4}$, conductors about $10^{7}$ $(\Omega\cdot\text{m})^{-1}$.
- Band gap: semiconductors $E_g < 2$ eV (Si $1.1$, Ge $0.67$), insulators $E_g > 2$ eV (diamond $6$ to $7$ eV). Conductors have a half-filled band or overlapping bands.

### Derivation: Conductivity from the drift velocity
In short: the charge crossing a unit area per second is $J = n\lvert q_e\rvert v_d$, and since $v_d = \mu E$ and $J = \sigma E$, the conductivity is $\sigma = n\lvert q_e\rvert\mu$.

| Step | Why |
| --- | --- |
| $a = \dfrac{q_eE}{m_e}$ | Newton's second law for one electron in the field $E$ |
| $v_d = \dfrac{\tau\lvert q_e\rvert E}{m_e} = \mu E$ | collisions with the ions (relaxation time $\tau$) stop the acceleration: constant drift velocity |
| $J = n\lvert q_e\rvert v_d = n\lvert q_e\rvert\mu E$ | charge per unit volume times velocity |
| $J = \sigma E \Rightarrow \sigma = n\lvert q_e\rvert\mu$ | microscopic form of Ohm's law |
| $E = V/l$ and $J = I/A \Rightarrow R = \rho\,l/A$ | link with the macroscopic Ohm's law (derived here) |

### Theorem: Resistivity of metals, Matthiessen's rule
$$\rho_{total} = \rho_T + \rho_r \qquad \rho_r = \rho_i + \rho_d \qquad \rho_T = \rho_0\,(1 + \alpha_T\,\Delta T)$$
- $\rho_T$ comes from the lattice vibrations and grows linearly with $T$; $\rho_r$ is the residual part from impurities ($\rho_i$) and deformation defects ($\rho_d$) and does **not** depend on temperature [Session 13 Slides 14-16].
- $\rho_0$ is the resistivity **at 0 $^\circ$C** and $\Delta T$ is the temperature in $^\circ$C.
- **Solve for a temperature:** $T = \dfrac{\rho_T - \rho_0}{\rho_0\,\alpha_T}$; two metals with the same resistivity: $\rho_{0,1}(1 + \alpha_1T_1) = \rho_{0,2}(1 + \alpha_2T_2)$.
- Example (Problem T6-01): $\rho_{Al,45} = 2.7\times10^{-6}(1 + 0.0039\times45) = 3.173\times10^{-6}\ \Omega\cdot\text{cm}$ and $T_{Ag} = (3.173 - 1.47)/(1.47\times0.0038) = 304.9\,^\circ$C with the rounded $3.173$ (the key gives $305\,^\circ$C).

| Metal | $\rho_0$ ($\mu\Omega\cdot\text{cm}$) | $\alpha_T$ ($^\circ\text{C}^{-1}$) |
| :--- | ---: | ---: |
| Aluminium | 2.7 | 0.0039 |
| Copper | 1.6 | 0.0039 |
| Gold | 2.3 | 0.0034 |
| Iron | 9 | 0.0045 |
| Silver | 1.47 | 0.0038 |

### Pattern: Effect of temperature, alloying and hardening on metals
- Heating: $\rho$ rises (more phonon scattering); cooling: $\rho$ falls toward the constant $\rho_r$.
- Impurities, vacancies, dislocations and grain boundaries raise $\rho_r$ and lower $\sigma$.
- **Every strengthening method lowers conductivity** (the obstacles to dislocations also scatter electrons): cold work lowers it only slightly, solid solution (Zn in Cu) lowers it sharply, precipitates and fine grains in between [Session 13 Slides 18-19].
- Lightest wire with the same strength and conductivity: choose the method that raises the strength most per loss of conductivity (cold work or precipitates, not solid solution).

### Theorem: Intrinsic semiconductors
$$\sigma = n_e\lvert q_e\rvert\mu_e + n_H\lvert q_e\rvert\mu_H = n_i\lvert q_e\rvert(\mu_e + \mu_H) \qquad n_i = \frac{\sigma}{\lvert q_e\rvert(\mu_e + \mu_H)}$$
$$\sigma = \sigma_0\exp\left(-\frac{E_g}{2kT}\right) \qquad \ln\sigma = \ln\sigma_0 - \frac{E_g}{2k}\cdot\frac1T$$
- Electrons and holes come in pairs ($n_e = n_H = n_i$) and $\mu_e > \mu_H$; both $n_i$ and $\sigma$ **rise** with $T$ (the mobility loss is masked) [Session 13 Slides 27-29].
- **Ratio between two temperatures** ($\sigma_0$ cancels): $\sigma_2 = \sigma_1\exp\left[\dfrac{E_g}{2k}\left(\dfrac{1}{T_1} - \dfrac{1}{T_2}\right)\right]$.
- **Band gap from two measurements:** $E_g = 2k\,\dfrac{\ln(\sigma_2/\sigma_1)}{1/T_1 - 1/T_2}$; on a plot of $\ln\sigma$ against $1/T$ the slope is $-E_g/2k$.
- $k = 8.62\times10^{-5}$ eV/K with $E_g$ in eV: the eV cancels. $T$ in kelvin.
- Example (Problem T6-07, Ge, $E_g = 0.67$ eV, $\sigma_{25} = 2.22$): $\sigma_{75} = 2.22\,e^{1.872} = 14.4\ (\Omega\cdot\text{m})^{-1}$.
- Example (Problem T6-08, Si, $\sigma = 4\times10^{-4}$, $\mu_e = 0.14$, $\mu_H = 0.048$): $n_i = 1.33\times10^{16}\ \text{m}^{-3}$.

| Property | Si | Ge |
| :--- | ---: | ---: |
| $E_g$ (eV) | 1.1 | 0.67 |
| $\mu_e$ (m$^2$/(V$\cdot$s)) | 0.135 | 0.39 |
| $\mu_H$ (m$^2$/(V$\cdot$s)) | 0.048 | 0.19 |
| $n_i$ (m$^{-3}$) | $1.5\times10^{16}$ | $2.4\times10^{19}$ |
| $\rho$ ($\Omega\cdot$m) | 2300 | 0.46 |

The slides print slightly different mobilities in two places (Si $0.14$ and $0.05$; Ge $0.38$ and $0.18$ on Slide 33): use the values given in the statement.

### Pattern: Extrinsic semiconductors, n-type and p-type
| | n-type | p-type |
| :--- | :--- | :--- |
| Dopant | more valence electrons than the host: P, As, Sb (group VA) in Si and Ge | fewer valence electrons: B, Al, Ga, In (group IIIA) |
| Role | donor, level $E_d$ just under the conduction band | acceptor, level $E_a$ just above the valence band |
| Majority carriers | electrons, $\sigma \approx n_e\lvert q_e\rvert\mu_e$ | holes, $\sigma \cong p\lvert q_e\rvert\mu_H$ |
| Ionisation energy | $E_c - E_d$ | $E_a - E_v$ |
| Extrinsic range | $\sigma = \sigma_0\exp\left(-\dfrac{E_c - E_d}{2kT}\right)$ | $\sigma = \sigma_0\exp\left(-\dfrac{E_a - E_v}{2kT}\right)$ |

- Type: compare the group of the dopant with the group of the host ($Z_{\text{P}} - Z_{\text{Si}} = 5 - 4 = +1$ means donor, n-type).
- Doping distortion is negligible, so $\sigma$ is controlled by the **number of carriers**, and the majority carrier dominates: $\sigma \approx n_e\lvert q_e\rvert\mu_e$ (Problem T6-06: $n_e = 10^{23}\ \text{m}^{-3}$, $\mu_e = 0.14$ gives $\sigma = 2243\ (\Omega\cdot\text{m})^{-1}$).
- **Dopant concentration:** ppm times atoms per m$^3$ of host; for a host of density $\rho$ and atomic mass $M$, atoms per m$^3$ $= \rho N_A/M$ (extension).
- **Comparing dopants:** the smaller $E_d$ or $E_a$, the more carriers at a given $T$; concentrations are limited by the maximum solubility of the dopant.
- Low $T$ (extrinsic range): carriers come from ionised dopants. High $T$: the intrinsic law takes over.

| Dopant | Si $E_d$ (eV) | Si $E_a$ (eV) | Ge $E_d$ (eV) | Ge $E_a$ (eV) |
| :--- | ---: | ---: | ---: | ---: |
| P | 0.045 | | 0.0120 | |
| As | 0.049 | | 0.0127 | |
| Sb | 0.039 | | 0.0096 | |
| B | | 0.045 | | 0.0104 |
| Al | | 0.057 | | 0.0102 |
| Ga | | 0.065 | | 0.0108 |
| In | | 0.160 | | 0.0112 |

### Algorithm: Ranking semiconductors by conductivity
1. Decide intrinsic or extrinsic (pure material or doped).
2. **Intrinsic:** smaller $E_g$ gives larger $\sigma$ at the same $T$: InSb ($0.17$) > Ge ($0.67$) > Si ($1.11$) > GaAs ($1.42$) > AlP; $E_g$ grows and $\sigma$ falls as the bonding goes from covalent (group IV) to the III-V and II-VI compounds.
3. **Extrinsic:** compare $E_d$ or $E_a$ (smaller is better) and the dopant concentration (more carriers, higher $\sigma$), within the solubility limit.
4. State the temperature range: the criterion holds in the extrinsic range; at high $T$ the intrinsic law dominates.
5. With numbers: $\sigma = n\lvert q_e\rvert\mu$ for each case and compare.

### Pattern: Dielectrics, capacitance and breakdown
$$p = q\,d \qquad C = \varepsilon_r\,\varepsilon_0\,\frac{A}{d} = \varepsilon_r\,C_0 \qquad E_{break} = \frac{U_{break}}{d}$$
- A **dielectric** is an insulator ($E_g$ large) that polarises under a field, aligning its dipoles; it raises the capacitance by $\varepsilon_r$ [Session 13 Slides 51-52].
- An **insulator** should have: high $\rho$, high dielectric strength $E_{break}$, small loss factor $\tan\delta$ and low permittivity [Session 13 Slide 54].
- The **loss factor** is the energy lost as heat when the dipoles cannot follow the alternating field; it grows with moisture, temperature and frequency.
- **Ferroelectric** materials have spontaneous polarisation, a hysteresis loop and a Curie temperature; **piezoelectric** materials convert strain into voltage and the reverse [Session 13 Slides 55-60].
- Units: $\varepsilon_0 = 8.85\times10^{-12}$ F/m, $C$ in F, $E_{break}$ in V/m (or kV/mm).

### Trap: Mistakes in electrical properties
- Using $\rho_0$ of the table with a temperature in kelvin: the table is at 0 $^\circ$C and $\Delta T$ is in $^\circ$C.
- Mixing $\mu\Omega\cdot$cm and $\Omega\cdot$m ($10^{-8}$) or conductivity against resistivity.
- Putting $T$ in $^\circ$C in $\exp(-E_g/2kT)$; forgetting the factor $2$ in the exponent.
- Using $E_g$ in joules with $k$ in eV/K (or the reverse): keep both in eV.
- Adding the hole term in an extrinsic semiconductor (negligible) or forgetting it in an intrinsic one.
- Calling a group IIIA dopant a donor (it is an acceptor) or a group VA dopant an acceptor.
- Believing that heating always lowers $\sigma$: it does for a metal ($\mu$ falls) and raises it for a semiconductor ($n$ rises).

## Unit 7 — Magnetic and thermal properties
Pages: Theory=teoria/topic-7-magnetic-thermal.html; Problems=problemas/topic-7-magnetic-thermal.html

### Theorem: Magnetic field, induction and permeability
$$B = \mu H \qquad B = \mu_0 H \ (\text{vacuum}) \qquad \mu_r = \frac{\mu}{\mu_0} \qquad B = \mu_0 H + \mu_0 M \qquad M = \chi_m H \qquad \mu_r = 1 + \chi_m$$
- $\mu_0 = 1.257\times10^{-6}$ H/m. The magnetic moment of an electron is measured in the Bohr magneton, $\mu_B = 9.27\times10^{-24}\ \text{A}\cdot\text{m}^2$ [Session 15 Slides 3-4].
- Moments of the transition metals in $\mu_B$: Sc 1, Ti 2, V 3, Cr 5, Mn 5, Fe 4, Co 3, Ni 2, Cu 0 (unpaired $3d$ electrons); metallic Fe $2.22$, Co $1.72$, Ni $0.60$, Gd $7.12$.

### Table: Types of magnetism
| Type | Dipoles | $\mu_r$ and $\chi_m$ | Examples |
| :--- | :--- | :--- | :--- |
| Diamagnetic | induced, opposite to $H$, not permanent | $\mu_r < 1$, $\chi_m < 0$ (about $-10^{-5}$) | Au, Ag, Cu, Si, Zn, Al$_2$O$_3$ |
| Paramagnetic | permanent, random, aligned by $H$ | $\mu_r > 1$, $10^{-5} \le \chi_m < 10^{-2}$ | Al, Ti, Cr, Mo, Na, Zr |
| Ferromagnetic | permanent, parallel without a field | $\mu_r \gg 1$, $\chi_m$ up to $10^6$, $B \cong \mu_0 M$ | Fe, Co, Ni, Gd |
| Antiferromagnetic | permanent, antiparallel and equal | no net moment | Cr, Mn, MnO |
| Ferrimagnetic | permanent, antiparallel and unequal | $\mu_r \gg 1$, $\chi_m$ about $10^5$ to $10^6$ | ferrites, garnets, Fe$_3$O$_4$ |

### Pattern: Domains, magnetisation curve and hysteresis
- Domains are regions of aligned dipoles ($10$ to $100\ \mu$m) separated by **Bloch walls** (about $100$ nm). Magnetising means growth of favourable domains, then rotation, then saturation $M_s$ [Session 15 Slides 14-16].
- $\mu_i$ is the initial slope and $\mu_{max}$ the largest $B/H$ (tangent from the origin).
- **Hysteresis loop:** $B_r$ remanence (the induction left at $H = 0$), $H_c$ coercivity (the reverse field that brings $B$ to zero), $B_s$ saturation. The loop area is the energy lost per cycle [Session 15 Slide 17].
- Limit between soft and hard: $H_c = 10\,000$ A/m [Session 15 Slide 18].

| | Soft | Hard |
| :--- | :--- | :--- |
| Bloch walls | easy to move | hard to move |
| Loop | narrow, high initial $\mu$, low $H_c$ | wide, high $B_r$, $B_s$ and $H_c$, low $\mu_i$ |
| Use | transformers, motors, alternating fields (low losses) | permanent magnets |

- **Larger grains:** walls move more easily, so $\mu$ rises and $H_c$, $B_r$ fall. **More inclusions, dislocations, pores:** walls are pinned, so $\mu$ falls and $H_c$, $B_r$ rise [Session 15 Slide 21].
- **Temperature:** the loop shrinks ($M_s$, $B_r$, $H_c$ fall); above the **Curie temperature** $T_c$ a ferromagnet becomes paramagnetic (Fe $1043$ K, Co $1404$, Ni $631$, Gd $289$); antiferromagnets have a Néel temperature (MnO $116$ K, Cr $310$, NiO $523$) [Session 15 Slides 22-24].
- **Superconductors:** zero resistivity below the critical temperature $T_c$, expulsion of the field (Meissner effect), limited by a critical field $H_c$ and a critical current density $J_c$ that fall as $T$ rises; Type I and Type II [Session 15 Slides 25-32].

### Theorem: Heat capacity and thermal expansion
$$C = \frac{dQ}{dT} \qquad c_p = \frac{C}{\text{atomic weight}} \qquad C \approx 3R \ (T > \theta_D) \qquad \frac{\Delta l}{l_0} = \alpha\,\Delta T \quad \Delta T = T_f - T_0$$
- $C$ is per mole, J/(mol$\cdot$K); above the Debye temperature $\theta_D$ it is constant, $3R = 24.9$ J/(mol$\cdot$K) $\approx 6$ cal/(mol$\cdot$K) [Session 15 Slides 34-35]. Heat to warm a mass: $Q = m\,c_p\,\Delta T$ (extension).
- $\alpha$ in $^\circ\text{C}^{-1}$ or K$^{-1}$; typical $10^{-6}$: Al $23.6$, Cu $17.0$, steel about $12$; Invar $1.6$ [Session 15 Slides 36-38]. High melting temperature, strong bond, low $\alpha$.
- Final length $l_f = l_0\,(1 + \alpha\,\Delta T)$; extension: volume $\Delta V/V_0 \approx 3\alpha\Delta T$ for an isotropic solid.
- A **bimetal** bends toward the metal with the smaller $\alpha$ when heated [Session 15 Slide 39].

### Theorem: Heat conduction and Wiedemann-Franz
$$q = \frac{Q}{A} = -k\,\frac{\Delta T}{\Delta x} \qquad k = k_e + k_{ph} \qquad L = \frac{k}{\sigma\,T} = 2.44\times10^{-8}\ \frac{\text{W}\cdot\Omega}{\text{K}^2} \qquad k_e = L\,\sigma\,T$$
- $q$ in W/m$^2$, $k$ in W/(m$\cdot$K); heat flows from hot to cold (minus sign). Same structure as Fick's first law [Session 15 Slide 40].
- Metals: $k \approx k_e$ (free electrons). Insulators and ceramics: $k \approx k_{ph}$ (phonons).
- Alloying, defects and porosity **lower** $k$ (they scatter electrons and phonons) [Session 15 Slide 43].
- Use: good electrical conductors are good thermal conductors; $k_e = L\sigma T$ links Unit 6 and Unit 7 (with $T$ in kelvin).

### Derivation: Thermal stress in a constrained body
In short: a body that cannot expand has zero total strain, so the elastic strain cancels the free thermal strain and the stress is $E\alpha(T_0 - T_f)$.

| Step | Why |
| --- | --- |
| $\varepsilon_{total} = \dfrac{\sigma}{E} + \alpha\,(T_f - T_0) = 0$ | elastic strain plus free thermal strain; the walls keep the length constant |
| $\sigma = -E\,\alpha\,(T_f - T_0)$ | solve for $\sigma$ |
| $\sigma = E\,\alpha\,(T_0 - T_f)$ | the form of the slides, with $\Delta T = T_0 - T_f$ [Session 15 Slide 45] |
| $T_f > T_0$ (heating): $\sigma < 0$, compression; $T_f < T_0$ (cooling): $\sigma > 0$, tension | signs of the slide |
| $[E\alpha\Delta T] = \text{MPa}\cdot{}^\circ\text{C}^{-1}\cdot{}^\circ\text{C} = \text{MPa}$ | dimensional check |

With a pre-existing load, add the stresses: $\sigma_2 = \sigma_F - E\alpha\Delta T$ for a stretched wire that is heated at constant length (Problem T5-05).

### Pattern: Thermal shock
$$TSR = \frac{\sigma_f\,k}{E\,\alpha_l}$$
- Thermal shock resistance rises with a **higher** fracture stress $\sigma_f$ and conductivity $k$, and with a **lower** modulus $E$ and expansion $\alpha_l$ [Session 15 Slides 47-48].
- Phase transformations with a dimensional change make the shock worse.
- Unit: W/m (check, extension).

### Algorithm: Thermal and magnetic problems
1. Name the quantity: expansion (free), stress (constrained), heat flow (gradient), magnetic response (type, loop).
2. Free expansion: $\Delta l = \alpha\,l_0\,\Delta T$. Constrained: $\sigma = E\alpha\Delta T$ and check against $\sigma_y$.
3. Heat flow: $Q = qA = kA\,\lvert\Delta T\rvert/\Delta x$.
4. Hysteresis loops: read $B_r$, $H_c$ and the area; soft or hard by $H_c$ against $10\,000$ A/m; explain the effect of grain size, impurities and porosity on the Bloch walls (Problems T7-11, T7-12).
5. Check units: kelvin differences equal $^\circ$C differences, but absolute temperatures in $\sigma = L$ formulas must be kelvin.

### Trap: Mistakes in magnetic and thermal properties
- The sign of the thermal stress: heating a constrained body gives compression, cooling gives tension.
- Using $\Delta T = T_f - T_0$ in the thermal-stress formula written as $E\alpha(T_0 - T_f)$ (double sign error).
- Mixing $\mu_r$ and $\chi_m$ ($\mu_r = 1 + \chi_m$) or $B$ and $H$ (a vacuum has $B = \mu_0H$).
- Taking a large grain size as harder to magnetise: it makes the walls move more easily (larger $\mu$, lower $H_c$).
- Using $C \approx 3R$ below the Debye temperature.
- Forgetting that alloying lowers thermal conductivity ($k$) as it lowers electrical conductivity.
