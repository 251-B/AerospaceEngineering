---
materia: Aerospace Materials I
tema: "Unit 11: environmental degradation, temperature and Tg effects, CTE mismatch, moisture attack, corrosion and UV/O2 ageing"
bank_id: B112
title: "Environmental Degradation and Durability"
category: mt3_test_block
unit: 11
concepts:
  - u11-degradation-durability-overview
  - u11-degradation-tensile-temperature
  - u11-degradation-above-tg
  - u11-degradation-cte-mismatch-numeric
  - u11-degradation-moisture-mechanisms
  - u11-degradation-moisture-plasticization
  - u11-degradation-moisture-mitigation
  - u11-degradation-galvanic-crevice
  - u11-degradation-uv-oxidation-ageing
  - u11-degradation-evaluation-criteria
difficulty: 2
origen: "Questions written for the bank in the style of Part I of Assessment Test III; not official exercises. Content from Session 24, Slides 32-34."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-11
---

# Bank B112 — Environmental Degradation and Durability

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 24, Slides 32-34.

## Q112.1 Primary limitation and durability factors of bonded joints

- id: B112-Q1
- concept_id: u11-degradation-durability-overview
- format: topic-true
- asks: cause

Referring to the environmental durability of structural adhesive joints, which one of the following statements is TRUE:

a) Gradual environmental degradation is the main long-term problem of adhesive bonds, driven by temperature, moisture, corrosion, combined loads, and UV/thermal oxidation ageing
b) Once fully cured, thermoset adhesive joints remain completely immune to moisture, oxygen diffusion, and thermal cycling
c) Moisture and temperature act independently and never accelerate interfacial degradation when combined with mechanical stress
d) Adhesive joints fail strictly by instantaneous static overload and never suffer progressive property loss over time

### Answer

a

### Explanation

Session 24, Slide 32 identifies gradual degradation—which lowers properties and triggers failure—as the main problem of adhesive bonds, driven by five factors: temperature, moisture, electrochemical corrosion of adherents, combined temperature + moisture + mechanical loads, and UV/thermal ageing.

- b) Even cross-linked thermosets absorb water, suffer oxidative ageing, and degrade at elevated temperature or under thermal mismatch.
- c) Slide 32 explicitly cites the synergistic combination of temperature, moisture, and mechanical loads, and Slide 33 notes moisture degradation increases with temperature.
- d) Gradual environmental degradation reduces strength over service life even below initial static overload levels.

### Source

Session 24, Slides 32-33.

## Q112.2 Temperature effect on adhesive tensile stress-strain curves

- id: B112-Q2
- concept_id: u11-degradation-tensile-temperature
- format: diagram-reading
- asks: figure-reading

![[attachments/T11/s24-tensile-characteristics.png]]

Examine the tensile stress-strain curves measured at $-40\,^\circ\text{C}$, ambient temperature, and $+80\,^\circ\text{C}$. How does lowering the service temperature affect the adhesive's mechanical response?

a) Both tensile strength and elastic modulus fall sharply while fracture strain triples
b) Elastic modulus and tensile strength increase, whereas strain at fracture decreases (more brittle)
c) Strength stays constant across all three temperatures, changing only elastic modulus
d) Cooling to $-40\,^\circ\text{C}$ induces ductile plastic flow beyond 0.14 strain

### Answer

b

### Explanation

Session 24, Slide 33: as the plot indicates with the arrow `T decreasing`, cooling from $+80\,^\circ\text{C}$ through ambient down to $-40\,^\circ\text{C}$ steepens the initial elastic slope (higher modulus) and raises tensile strength (~90 MPa at $-40\,^\circ\text{C}$ vs ~47 MPa at $+80\,^\circ\text{C}$), while shortening fracture strain below ~0.04 (embrittlement).

- a) Describes increasing temperature toward $+80\,^\circ\text{C}$, where the polymer softens and reaches higher strain (~0.115) at lower stress.
- c) Peak stress clearly doubles between $+80\,^\circ\text{C}$ (~47 MPa) and $-40\,^\circ\text{C}$ (~90 MPa), falsifying constant strength.
- d) The highest elongation curve belongs to $+80\,^\circ\text{C}$, whereas $-40\,^\circ\text{C}$ breaks earliest at low strain.

### Source

Session 24, Slide 33.

## Q112.3 Thermal softening above the glass transition temperature

- id: B112-Q3
- concept_id: u11-degradation-above-tg
- format: what-happens
- asks: effect

If an aircraft epoxy bondline is operated continuously under shear load above its glass transition temperature $T_g$, what happens to joint behaviour?

a) Polymer chains lock into a rigid glass, raising shear strength and stopping creep completely
b) Interfacial chemisorption bonds double in density to compensate for thermal expansion
c) Chain mobility rises sharply, lowering stiffness, adherence, and shear strength while accelerating adhesive creep
d) The cross-linked epoxy melts reversibly into a free-flowing liquid that re-wets cracks on cooling

### Answer

c

### Explanation

Session 24, Slides 31-33 (with polymer $T_g$ fundamentals from Topic 9): heating an adhesive up to and above $T_g$ drops modulus and adherence sharply, activating viscoelastic chain flow that leads to unacceptable adhesive creep (Slide 31) and premature bond failure.

- a) Freezing chain mobility into a rigid glass occurs *below* $T_g$, not above it.
- b) Elevated temperature lowers interfacial adherence (Slide 33) rather than increasing covalent bond density.
- d) Cross-linked thermoset epoxies soften and creep above $T_g$, then thermally degrade at higher temperatures rather than melting reversibly like thermoplastics.

### Source

Session 24, Slides 31-33.

## Q112.4 Differential thermal mismatch strain after curing

- id: B112-Q4
- concept_id: u11-degradation-cte-mismatch-numeric
- format: numeric
- asks: calculation
- calc: (23e-6 - 1e-6) * 100 * 100

An epoxy cures at $120\,^\circ\text{C}$ between an aluminium alloy ($\alpha_{\text{Al}} = 23 \times 10^{-6}\text{ }^\circ\text{C}^{-1}$) and a carbon-epoxy composite ($\alpha_{\text{CFRP}} = 1 \times 10^{-6}\text{ }^\circ\text{C}^{-1}$), and then cools by $\Delta T = 100\,^\circ\text{C}$ to room temperature. What differential free thermal strain $\Delta\varepsilon_{\text{th}} = (\alpha_{\text{Al}} - \alpha_{\text{CFRP}})\Delta T$ (in percent) must be accommodated by residual bondline stresses?

a) 0.022 %
b) 0.12 %
c) 0.44 %
d) 0.22 %

### Answer

d

### Explanation

Session 24, Slides 17 and 32-33 (with thermal strain $\varepsilon_{\text{th}} = \alpha\Delta T$ from Topic 7): the CTE difference is $\Delta\alpha = (23 - 1) \times 10^{-6}\text{ }^\circ\text{C}^{-1} = 22 \times 10^{-6}\text{ }^\circ\text{C}^{-1}$. Over $\Delta T = 100\,^\circ\text{C}$, the differential thermal strain is $\Delta\varepsilon_{\text{th}} = 22 \times 10^{-6} \times 100 = 2.2 \times 10^{-3} = 0.22\text{ \%}$.

- a) Drops a factor of 10 in converting the dimensionless strain $2.2 \times 10^{-3}$ into percent ($0.022\text{ \%}$ instead of $0.22\text{ \%}$).
- b) Uses an incorrect temperature step or arithmetic slip when multiplying $\Delta\alpha$ by $\Delta T$.
- c) Doubles the differential thermal strain ($0.44\text{ \%}$), corresponding to $\Delta T = 200\,^\circ\text{C}$ instead of $100\,^\circ\text{C}$.

### Source

Session 24, Slides 17 and 32-33; Session 15, Slide 45.

## Q112.5 Interfacial moisture attack mechanisms

- id: B112-Q5
- concept_id: u11-degradation-moisture-mechanisms
- format: diagram-reading
- asks: figure-reading

![[attachments/T11/s24-moisture-attack-interface.png]]

In the schematic of moisture attack at an adhesive-metal interface, what does the leftmost mechanism labeled `Segregation` represent compared with `Hydrolysis` and `Corrosion`?

a) Formation of extra covalent primary bonds between water and the polymer matrix
b) Preferential attraction of water molecules to the interface, displacing existing adhesive bonds
c) Precipitation of metallic filler crystals that seal the interface against oxygen
d) Rapid vaporization of adsorbed water causing instant polymer curing

### Answer

b

### Explanation

Session 24, Slide 33 defines the three moisture attacks shown at the interface: **segregation** occurs when water is preferentially attracted to the high-energy interface and physically displaces the adhesive bond; **hydrolysis** chemically cleaves interfacial bonds or hydrated oxide layers ($\text{RO} \to \text{ROH}$); and **corrosion** dissolves the metal adherend ($\text{M}^+$, $\text{OH}^-$).

- a) Water weakens and breaks interfacial adhesion rather than forming durable primary covalent bonds.
- c) Precipitation of mineral crystals is not shown; segregation opens an unbonded water-filled gap at the interface.
- d) Ambient moisture causes gradual interfacial displacement and degradation, not rapid curing.

### Source

Session 24, Slide 33.

## Q112.6 Bulk and interfacial effects of moisture ingress

- id: B112-Q6
- concept_id: u11-degradation-moisture-plasticization
- format: topic-false
- asks: effect

Regarding the effects of absorbed moisture on an adhesive joint, which one of the following statements is FALSE:

a) Absorbed water increases cross-link density inside the polymer, raising $T_g$ and stiffening the bondline
b) Water plasticizes the bulk adhesive, lowering its stiffness and strength
c) Moisture can hydrolyse the oxide layer or corrode metallic adherents at the interface
d) Moisture attack can induce micro-cracking and accelerates strongly when combined with high temperature

### Answer

a

### Explanation

Session 24, Slides 32-33: water acts as a plasticizer inside the polymer (making the adhesive more plastic and softer, lowering $T_g$ rather than cross-linking it), displaces interfacial bonds (segregation), hydrolyses oxides, corrodes metals, and drives micro-cracking. Statement a is false.

- b) True: Slides 32-33 explicitly state that moisture weakens the adhesive by making it more plastic.
- c) True: Slide 33 highlights chemical change of adherents via metal corrosion and hydrolysis of the oxide layer.
- d) True: Slides 32-33 list micro-cracking and explicitly note that moisture effects grow with temperature and humidity.

### Source

Session 24, Slides 32-33.

## Q112.7 Mitigating moisture ingress in adhesive joints

- id: B112-Q7
- concept_id: u11-degradation-moisture-mitigation
- format: identify
- asks: application

Which formulation and joint-protection strategy is specifically used to reduce moisture diffusion and interfacial water degradation in service?

a) Replacing thermoset epoxies with water-base starch glues
b) Increasing surface roughness well beyond the optimum to trap air bubbles
c) Leaving exposed overlap edges unprimed and omitting edge coatings
d) Incorporating mineral fillers into the adhesive and sealing exposed edges with sealants

### Answer

d

### Explanation

Session 24, Slide 32 explicitly recommends countering moisture degradation (plasticization, hydrolysis, micro-cracking) with mineral fillers (which lengthen diffusion tortuosity) and protective edge sealants (blocking moisture ingress paths).

- a) Water-base vegetable glues swell and soften readily in moisture rather than resisting hostile environments.
- b) Trapped air pockets from over-roughening become moisture-accumulation sites that worsen interfacial attack.
- c) Leaving bond edges unprimed and unsealed exposes the high-stress interface directly to humid air and condensed water.

### Source

Session 24, Slide 32 (and Slides 23 and 37).

## Q112.8 Galvanic and crevice corrosion at metal-composite joints

- id: B112-Q8
- concept_id: u11-degradation-galvanic-crevice
- format: cause-effect
- asks: cause

Although an intact polymer adhesive electrically isolates dissimilar adherends, moisture ingress into a damaged or unsealed carbon-fibre composite-to-aluminium lap joint can accelerate aluminium degradation because:

a) absorbed water increases the adhesive's electrical resistivity until sparks jump across the joint
b) aluminium acts as the noble cathode and dissolves carbon fibres by hydrolysis
c) stagnant water inside debonded edge crevices promotes crevice corrosion, while exposed carbon-to-aluminium contact drives galvanic corrosion of aluminium
d) carbon fibres diffuse across the cured epoxy at room temperature to embrittle aluminium grains

### Answer

c

### Explanation

Session 24, Slides 3 and 32-33 (with standard galvanic/crevice corrosion mechanisms): an intact adhesive layer prevents galvanic coupling by electrical isolation (Slide 3). Once moisture penetrates debonded crevices or bridges exposed conductive carbon fibres to aluminium, crevice corrosion and galvanic attack (with aluminium as the active anode) rapidly undermine the interface.

- a) Absorbed electrolyte water lowers electrical resistance rather than raising it to cause sparking.
- b) Aluminium is anodically active relative to noble graphite/carbon fibres, so aluminium corrodes preferentially.
- d) Solid carbon fibres cannot diffuse through cured epoxy into metallic aluminium at room temperature.

### Source

Session 24, Slides 3 and 32-33; Topic 11 durability extension.

## Q112.9 UV and thermal oxidation ageing mechanism

- id: B112-Q9
- concept_id: u11-degradation-uv-oxidation-ageing
- format: complete-sentence
- asks: cause

Under combined ultraviolet light, elevated temperature, and oxygen diffusion into an adhesive, oxidation ageing degrades mechanical strength because oxygen first forms polymer hydroperoxides ($\text{polymer–O–O–H}$) that subsequently decompose into:

a) inert mineral silica fillers that plug surface pores
b) stable cross-linked silane coupling bridges along the interface
c) volatile water vapor that acts as an anionic curing catalyst
d) reactive $\text{R–O}\cdot$ and $\cdot\text{OH}$ free radicals that break the polymer chains

### Answer

d

### Explanation

Session 24, Slide 32 writes the exact ageing sequence: oxygen diffuses into the adhesive to form hydroperoxides ($\text{polymer–O–O–H}$), which split with temperature and UV light into $\text{R–O}\cdot + \cdot\text{OH}$ free radicals that attack and destroy the polymer chains.

- a) Mineral silica is an inorganic filler added during formulation, not a decomposition product of polymer hydroperoxides.
- b) Hydroperoxide breakdown destroys bulk polymer chains rather than forming protective interfacial silane links.
- c) Free radicals cleave existing cured chains and reduce strength rather than catalyzing fresh polymerization.

### Source

Session 24, Slide 32.

## Q112.10 Mechanical versus physical-chemical performance criteria

- id: B112-Q10
- concept_id: u11-degradation-evaluation-criteria
- format: true-statement
- asks: classification

Which of the following statements correctly separates the mechanical and physical-chemical criteria used to qualify structural adhesive performance?

a) Fatigue and impact resistance are physical-chemical criteria, whereas moisture resistance is a purely mechanical criterion
b) Static, fatigue, and impact resistance are mechanical criteria, whereas temperature resistance, thermal ageing, moisture resistance, and chemical-agent resistance are physical-chemical criteria
c) Adhesive qualification evaluates static tensile strength only, omitting fatigue and chemical resistance
d) Creep under heat is classified strictly as a tack property independent of temperature resistance

### Answer

b

### Explanation

Session 24, Slide 34 groups adhesive performance assessment into mechanical criteria (resistance to static loading, fatigue, and impact) and physical-chemical criteria (temperature resistance, ageing with temperature, resistance to moisture, and resistance to chemical agents).

- a) Swaps the two groups: fatigue and impact belong to mechanical criteria, whereas moisture resistance is physical-chemical.
- c) Contradicts aerospace qualification practice on Slide 34, which mandates static, fatigue, impact, thermal, moisture, and chemical criteria.
- d) Creep under load at elevated temperature reflects bulk viscoelastic temperature resistance (Slides 31 and 34), not instantaneous tack.

### Source

Session 24, Slides 31 and 34.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
