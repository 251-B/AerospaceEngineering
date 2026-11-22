---
materia: Aerospace Materials I
tema: "Unit 8: glass viscosity reference points, cooling rate effect on Tg, float glass and forming, thermal tempering, optical fibres, Space Shuttle TPS and gas turbine YSZ TBC"
bank_id: B76
title: "Glass processing, tempering and aerospace ceramics"
category: mt3_test_block
unit: 8
concepts:
  - u8-glass-viscosity-points
  - u8-glass-cooling-tg
  - u8-glass-float-forming
  - u8-tempering-thermal-stress
  - u8-optical-fibre-dopants
  - u8-tps-shuttle-tiles
  - u8-tbc-turbine-ysz
difficulty: 2
origen: "Questions written for the bank in the style of Part I of Assessment Test III; not official exercises. Content from Session 18, Slides 30-41 and Session 16, Slide 21."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B76 — Glass processing, tempering and aerospace ceramics

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 18, Slides 30-41 and Session 16, Slide 21.

## Q76.1 Ordering glass viscosity reference points

- id: B76-Q1
- concept_id: u8-glass-viscosity-points
- format: ordering
- asks: comparison

Order the four glass viscosity reference points below by INCREASING temperature (corresponding to decreasing viscosity $\eta$):

a) working point ($\eta = 10^{4}\ \text{P}$), softening point ($4\times 10^{7}\ \text{P}$), annealing point ($10^{13}\ \text{P}$), strain point ($3\times 10^{14}\ \text{P}$)
b) annealing point ($10^{13}\ \text{P}$), strain point ($3\times 10^{14}\ \text{P}$), softening point ($4\times 10^{7}\ \text{P}$), working point ($10^{4}\ \text{P}$)
c) strain point ($\eta = 3\times 10^{14}\ \text{P}$), annealing point ($10^{13}\ \text{P}$), softening point ($4\times 10^{7}\ \text{P}$), working point ($10^{4}\ \text{P}$)
d) strain point ($\eta = 3\times 10^{14}\ \text{P}$), softening point ($4\times 10^{7}\ \text{P}$), annealing point ($10^{13}\ \text{P}$), working point ($10^{4}\ \text{P}$)

### Answer

c

### Explanation

Session 18, Slide 30: as temperature rises, glass viscosity decreases monotonically. Ordering from lowest temperature (highest viscosity) to highest temperature (lowest viscosity) gives: strain point ($3\times 10^{14}\ \text{P}$) $<$ annealing point ($10^{13}\ \text{P}$) $<$ softening point ($4\times 10^{7}\ \text{P}$) $<$ working point ($10^{4}\ \text{P}$) ($<$ melting point, $100\ \text{P}$).

- a) Reverses the temperature order into decreasing temperature (increasing viscosity).
- b) Swaps the strain point and annealing point at the high-viscosity, low-temperature end.
- d) Places the softening point below the annealing point, inverting the $4\times 10^{7}\ \text{P}$ and $10^{13}\ \text{P}$ viscosity order.

### Source

Session 18, Slide 30.

## Q76.2 Reading glass viscosity versus temperature curves

- id: B76-Q2
- concept_id: u8-glass-viscosity-points
- format: diagram-reading
- asks: figure-reading

The viscosity-temperature chart below compares soda-lime, borosilicate, $96\ \%$ silica, and fused silica glasses. Based on the curves, which statement accurately reads their shaping temperatures?

![[attachments/T8/s18-viscosity-temperature.png]]

a) Fused silica reaches its working point ($\eta = 10^{3}\ \text{Pa}\cdot\text{s}$) near $800\ \text{°C}$, below both borosilicate and soda-lime glass
b) At $1000\ \text{°C}$, soda-lime glass has already reached its working point ($\eta \approx 10^{3}\ \text{Pa}\cdot\text{s}$), whereas fused silica remains stiffer than its annealing point
c) All four silicate glasses share the exact same softening temperature near $1000\ \text{°C}$ regardless of composition
d) Borosilicate glass has lower viscosity than soda-lime glass at every temperature between $600\ \text{°C}$ and $1400\ \text{°C}$

### Answer

b

### Explanation

Session 18, Slide 30: reading vertically at $1000\ \text{°C}$, the soda-lime curve crosses the working-point line ($10^{3}\ \text{Pa}\cdot\text{s} = 10^{4}\ \text{P}$), borosilicate lies near $4\times 10^{4}\ \text{Pa}\cdot\text{s}$, $96\ \%$ silica sits between its annealing and softening points, and fused silica does not even reach its strain/annealing region until $\sim 1080\text{–}1140\ \text{°C}$, explaining why pure silica is far harder to shape.

- a) Misreads the leftmost soda-lime/borosilicate curves as fused silica; fused silica is the rightmost curve at highest temperatures.
- c) Ignores the wide horizontal spread across compositions: softening temperatures span roughly $700\ \text{°C}$ for soda-lime up to $> 1600\ \text{°C}$ for fused silica.
- d) Inverts the relative positions of the two leftmost curves: borosilicate consistently lies to the right (higher viscosity at fixed $T$) of soda-lime glass.

### Source

Session 18, Slide 30.

## Q76.3 Effect of cooling rate on glass transition temperature Tg

- id: B76-Q3
- concept_id: u8-glass-cooling-tg
- format: cause-effect
- asks: effect

Unlike the fixed equilibrium melting point $T_m$ of a crystal, the glass transition temperature $T_g$ of a silicate melt depends on thermal history. Cooling a molten glass much more slowly causes $T_g$ and the final specific volume to:

a) both increase, because slow cooling traps high-temperature free volume early
b) increase in $T_g$ while specific volume stays equal to the crystal curve
c) stay strictly unchanged, because viscosity is independent of cooling rate
d) both decrease, because the undercooled liquid follows the equilibrium line down to a lower temperature before freezing

### Answer

d

### Explanation

Session 18, Slide 30: the volume-temperature plot explicitly labels $T_g = f(\text{cooling rate})$ and shows a dashed "slower cooling" path continuing further down the undercooled liquid line before bending at a lower $T_g$ (point g below point e), yielding a denser glass with smaller specific volume.

- a) Inverts the effect of cooling rate: *faster* quenching freezes the liquid structure earlier at higher $T_g$ and larger volume.
- b) Confuses $T_g$ shifts with equilibrium crystallization down to the crystal volume line.
- c) Contradicts the explicit Slide 30 relation $T_g = f(\text{cooling rate})$ and thermal-history dependence of glass viscosity.

### Source

Session 18, Slide 30.

## Q76.4 Float glass and glass forming routes

- id: B76-Q4
- concept_id: u8-glass-float-forming
- format: topic-true
- asks: application

Referring to industrial glass forming processes above $T_g$, which one of the following statements is TRUE:

a) Flat window sheets are made by the float process, flowing molten glass onto molten tin under controlled atmosphere and then through an annealing lehr
b) Continuous flat window panes are formed by cold isostatic pressing in evacuated metallic autoclaves
c) Glass bottles and headlights are produced by drawing viscous glass tubes over a rotating mandrel
d) Short glass wool fibres ($20\text{–}30\ \text{mm}$) are made by casting a colloidal aqueous slip into porous plaster moulds

### Answer

a

### Explanation

Session 18, Slides 31 and 35: flat glass sheets are manufactured by the float process (molten glass floats on a perfectly flat bath of molten tin inside a controlled atmosphere before slow stress relief on rollers in a lehr), rods and tubing are drawn over a rotating mandrel, discrete bottles/headlights are blown or pressed in moulds, and glass wool insulation is spun centrifugally through rotating orifices.

- b) Confuses molten float-glass sheet manufacture with dry-powder ceramic cold isostatic pressing / HIP.
- c) Confuses blowing/pressing of discrete bottles and headlights with mandrel drawing used for rods and tubing (Slide 31).
- d) Confuses centrifugal spinning of molten glass wool (Slide 35) with wet ceramic slip casting in plaster moulds (Slide 15).

### Source

Session 18, Slides 15, 31 and 35.

## Q76.5 Residual stress profile in thermally tempered glass

- id: B76-Q5
- concept_id: u8-tempering-thermal-stress
- format: diagram-reading
- asks: figure-reading

The schematic below compares the through-thickness stress profile of a glass plate at high temperature and after rapid air quenching (thermal tempering). How does the final residual stress profile strengthen the glass?

![[attachments/T8/s16-tempering-stress-profile.png]]

a) Uniform tensile stress across the whole thickness pre-stretches surface flaws so they cannot grow further
b) Residual compressive stress at the outer surfaces balances interior tension, requiring a larger applied tensile stress to open surface cracks
c) High-temperature creep turns the outer skin crystalline while keeping the core under pure compression
d) Zero residual stress remains anywhere after cooling, eliminating all thermal-shock gradients

### Answer

b

### Explanation

Session 16, Slide 21 and Session 18, Slide 33: after tempering, the flat zero-stress profile at high temperature becomes parabolic—**compressive** ($\sigma < 0$) at both outer surfaces and **tensile** ($\sigma > 0$) in the core. Because brittle glass fails when surface cracks open in tension, residual surface compression must first be overcome by any external bending or tensile load, raising apparent strength.

- a) Inverts the signs shown on the stress profile: uniform tension at the surface would weaken the glass drastically rather than strengthen it.
- c) Inverts the surface vs. interior stress signs and wrongly introduces bulk crystallization (devitrification) into tempered amorphous glass.
- d) Describes stress-relieved *annealed* glass (zero residual stress profile, like the upper line), not tempered glass.

### Source

Session 16, Slide 21; Session 18, Slide 33.

## Q76.6 Thermal tempering temperature window and annealing contrast

- id: B76-Q6
- concept_id: u8-tempering-thermal-stress
- format: topic-false
- asks: comparison

Regarding thermal tempering and stress-relief annealing of silicate glass plates, which one of the following statements is FALSE:

a) Thermal tempering heats the glass plate above $T_g$ (yet below the softening point) and quenches its surfaces rapidly with air jets
b) During tempering, the outer surface cools below $T_g$ and solidifies first, and subsequent contraction of the cooling core pulls the surface into compression
c) To maximize surface compression, tempered glass is cooled as slowly as possible from above the melting point so the interior stays compressed
d) Holding glass near the annealing point ($\eta \approx 10^{13}\ \text{P}$) and cooling slowly relieves internal stresses, whereas tempering intentionally builds surface compression

### Answer

c

### Explanation

Session 18, Slides 30, 31 and 33: slow cooling from high temperature relieves thermal gradients and produces annealed (low-stress) glass rather than tempered glass; thermal tempering requires heating between $T_g$ and the softening point followed by **rapid** cooling so the rigid skin is pulled into compression by the later-contracting core (which ends in tension, not compression). Statement c) is false.

- a) True: Slide 33 specifies heating above $T_g$ and below the softening point followed by rapid cooling.
- b) True: Slide 33 explains that the surface cools below $T_g$ first and the later-contracting interior draws the surface into compression.
- d) True: annealing at $\eta \approx 10^{13}\ \text{P}$ (Slide 30, float lehr Slide 31) removes internal stresses, opposite in goal to thermal tempering.

### Source

Session 18, Slides 30-31 and 33.

## Q76.7 Core and cladding composition of optical glass fibres

- id: B76-Q7
- concept_id: u8-optical-fibre-dopants
- format: complete-sentence
- asks: cause

In a silica optical glass fibre designed to guide light along its axis, the core is doped with $\text{GeO}_2$ and $\text{Al}_2\text{O}_3$ while the outer cladding is pure silica or silica doped with $\text{F}$ or $\text{B}$ in order to:

a) raise the refractive index of the core above that of the cladding for light guidance by internal reflection
b) lower the core refractive index below that of the cladding so light refracts outward through the fibre wall
c) make the core electrically conductive so signals travel as electric current rather than light
d) create $90\ \%$ porosity inside the core for thermal insulation like glass wool

### Answer

a

### Explanation

Session 18, Slide 35: an optical fibre consists of a silica ($\text{SiO}_2$) core doped with $\text{GeO}_2$ and $\text{Al}_2\text{O}_3$ to **increase** the refractive index, surrounded by a cladding of pure $\text{SiO}_2$ or $\text{F}$/$\text{B}$-doped $\text{SiO}_2$ to **decrease** the refractive index so light remains trapped in the core by total internal reflection.

- b) Inverts the refractive-index roles of core and cladding; $n_{\text{core}} < n_{\text{cladding}}$ would cause light to leak out of the core.
- c) Optical fibres guide electromagnetic light waves through dielectric silica glass, not electric currents.
- d) Confuses dense solid optical silica waveguides with porous spun glass wool insulation shown on the same slide.

### Source

Session 18, Slide 35.

## Q76.8 Space Shuttle thermal protection materials by zone

- id: B76-Q8
- concept_id: u8-tps-shuttle-tiles
- format: identify
- asks: classification

On the Space Shuttle Thermal Protection System (TPS), which material protects the hottest nose cap and wing leading edges at temperatures up to $1650\ \text{°C}$?

a) White flexible Nomex aramid felt coated with silicone elastomer (FRSI, up to $400\ \text{°C}$)
b) White borosilicate-coated high-purity silica tiles (LRSI, $400\text{–}650\ \text{°C}$)
c) Black $\text{SiB}_4$-borosilicate-coated $90\ \%$ porous silica tiles (HRSI LI-900, $650\text{–}1260\ \text{°C}$)
d) Pyrolytic carbon-reinforced carbon coated with silicon carbide (RCC)

### Answer

d

### Explanation

Session 18, Slides 36-37: the Space Shuttle nose cap and wing leading edges experience the highest re-entry temperatures (up to $1650\ \text{°C}$) and are protected by **Reinforced Carbon-Carbon (RCC)**—pyrolytic carbon reinforced with carbon fibres and coated with $\text{SiC}$ against oxidation.

- a) FRSI aramid felt blankets protect cooler upper surfaces below $400\ \text{°C}$.
- b) White LRSI silica tiles cover intermediate upper fuselage and tail regions ($400\text{–}650\ \text{°C}$) to reflect solar heating.
- c) Black HRSI LI-900 silica tiles cover $70\ \%$ of the surface (orbiter underside and forward regions) in the $650\text{–}1260\ \text{°C}$ range.

### Source

Session 18, Slides 36-37.

## Q76.9 Why Shuttle HRSI tiles are 90% porous silica with black coating

- id: B76-Q9
- concept_id: u8-tps-shuttle-tiles
- format: what-happens
- asks: cause

The Shuttle's High-temperature Reusable Surface Insulation (HRSI) tiles are fabricated from $90\ \%$ porous high-purity silica fibres sealed with a black $\text{SiB}_4$-doped borosilicate glass glaze. What happens during atmospheric re-entry ($650\text{–}1260\ \text{°C}$) because of this design?

a) The metallic aluminium airframe melts partially while the dense silica interior stores heat by high thermal conductivity
b) The tiles undergo rapid liquid-phase sintering on each flight, shrinking by $20\ \%$ into dense quartz blocks
c) Low-expansion silica resists thermal shock, $90\ \%$ porosity keeps thermal conductivity extremely low to protect the airframe, and the black glass glaze seals pores and radiates heat
d) Open pores draw hot re-entry plasma straight to the aluminium skin to equalize pressure across the tile thickness

### Answer

c

### Explanation

Session 18, Slide 37 (and Session 16, Slide 31): high-purity silica fibres give HRSI tiles an ultra-low $\alpha$ so they survive intense thermal shock without cracking, $90\ \%$ porosity cuts solid conduction paths so $k$ is tiny, and the thin black borosilicate + $\text{SiB}_4$ glass coating provides waterproofing/sealing and high radiative heat emission.

- a) Inverts the thermal insulation function: the tiles' extremely low conductivity keeps the underlying aluminium airframe cool.
- b) Tiles are already sintered refractory fibres and operate below temperatures that would shrink them during re-entry.
- d) The impervious borosilicate glass glaze explicitly seals the outer surface rather than admitting hot plasma.

### Source

Session 18, Slide 37; Session 16, Slide 31.

## Q76.10 Thermal barrier coatings and ceramics in gas turbines

- id: B76-Q10
- concept_id: u8-tbc-turbine-ysz
- format: topic-true
- asks: application

Referring to engineering ceramics in modern gas-turbine engines, which one of the following statements is TRUE:

a) Thermal barrier coatings (TBCs) of yttria-stabilized zirconia ($\text{ZrO}_2$–$\text{Y}_2\text{O}_3$, YSZ) insulate metallic turbine blades so hotter gas temperatures can be sustained safely
b) Gas-turbine rotors and rolling-element bearings use soda-lime glass because its low $T_g$ relieves centrifugal stresses
c) Turbine thermal barrier coatings consist of porous Nomex aramid felt bonded directly onto superalloy combustion blades
d) Yttria-stabilized zirconia is chosen for TBCs because its high metallic thermal conductivity transfers combustor heat rapidly into the blade core

### Answer

a

### Explanation

Session 18, Slides 39-41 (and Session 16, Slide 10): gas turbines employ silicon nitride ($\text{Si}_3\text{N}_4$) rotors, ceramic bearings, and **Thermal Barrier Coatings (TBC)** of yttria-stabilized zirconia (**YSZ**, fluorite structure $\text{ZrO}_2$ stabilized with $\text{Y}_2\text{O}_3$); the thin, low-conductivity YSZ layer lowers the underlying superalloy blade temperature during combustion.

- b) Soda-lime glass softens near $700\ \text{°C}$ and has poor thermal shock resistance; turbine rotors/bearings use engineering ceramics such as $\text{Si}_3\text{N}_4$, $\text{SiC}$, $\text{Al}_2\text{O}_3$, or $\text{ZrO}_2$.
- c) Nomex aramid felt is Shuttle FRSI limited to $400\ \text{°C}$ (Slide 37), far below hot turbine gas temperatures.
- d) Inverts the purpose of a thermal barrier coating: YSZ relies on *low* thermal conductivity to shield the metal blade from heat.

### Source

Session 18, Slides 37 and 39-41; Session 16, Slide 10.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
