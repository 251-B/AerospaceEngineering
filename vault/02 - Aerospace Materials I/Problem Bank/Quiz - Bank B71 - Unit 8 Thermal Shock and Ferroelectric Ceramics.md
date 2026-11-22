---
materia: Aerospace Materials I
tema: "Unit 8: thermal shock resistance, rapid cooling vs heating, low-alpha ceramics and ferroelectric/piezoelectric BaTiO3 ceramics"
bank_id: B71
title: "Thermal shock and ferroelectric ceramics"
category: mt3_test_block
unit: 8
concepts:
  - u8-thermal-shock-mechanism
  - u8-thermal-shock-quench
  - u8-thermal-shock-stress-calc
  - u8-thermal-shock-tsr
  - u8-thermal-shock-low-alpha
  - u8-ferro-dielectric-insulators
  - u8-ferro-dipole-symmetry
  - u8-ferro-piezo-mechanisms
difficulty: 2
origen: "Includes an official exam adaptation from MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf (Q7a); remaining items written for the bank in the style of Part I of Assessment Test III. Content from Session 16, Slides 3, 21-22 and 31."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B71 — Thermal shock and ferroelectric ceramics

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong), including an adaptation of Q7a from the June 2016 extraordinary final exam. Content: Session 16, Slides 3, 21-22 and 31.

## Q71.1 Mechanism of thermal shock in ceramics

- id: B71-Q1
- concept_id: u8-thermal-shock-mechanism
- format: cause-effect
- asks: cause
- origin: official-exam

How does thermal shock fracture arise in a ceramic component subjected to sudden temperature changes?

a) Rapid heating or cooling creates temporary temperature gradients whose differential thermal strain generates stresses exceeding the brittle fracture stress
b) Dislocation pile-ups form at grain boundaries during heating and nucleate ductile shear bands across the specimen
c) Sudden cooling transforms ionic bonds at the outer surface into metallic bonds, lowering the local elastic modulus
d) Uniform slow heating eliminates all internal gradients while lowering the lattice packing factor below stability

### Answer

a

### Explanation

`MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf`, Q7a (and Session 16, Slide 21): thermal shock is partial or total fracture caused by rapid $\Delta T$ (creating temporary temperature gradients and residual thermal stresses) or by restriction of thermal expansion; because ceramics cannot yield plastically, fracture occurs once the induced tensile stress reaches $\sigma_f$.

- b) Misapplies metallic dislocation plasticity to brittle ceramics, which lack mobile dislocations at normal temperatures.
- c) Invents a non-existent change of bond character from ionic to metallic upon cooling.
- d) Slow uniform heating avoids temperature gradients and therefore prevents thermal shock rather than causing it.

### Source

MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf, p. 4 (Q7a); Session 16, Slide 21.

## Q71.2 Surface cracking during rapid cooling

- id: B71-Q2
- concept_id: u8-thermal-shock-quench
- format: false-statement
- asks: comparison

Which one of the following statements about rapid cooling versus rapid heating of a brittle ceramic plate is FALSE:

a) During rapid cooling, the outer surface contracts faster than the hot interior, placing the surface in tension
b) Surface tensile stresses developed during sudden quenching are far more likely to fracture a ceramic than compressive surface stresses during rapid heating
c) Rapid heating produces tensile stresses on the outer surface and compressive stresses in the interior, causing immediate surface crack opening
d) Because ceramics lack plastic crack blunting, thermal tensile stresses at surface flaws readily trigger catastrophic failure

### Answer

c

### Explanation

Session 16, Slide 21 (and Session 15, Slide 47): during rapid heating, the hotter exterior tries to expand while restrained by the cooler core, placing the **surface in compression** and the interior in tension; surface tension occurs during **rapid cooling** (quenching), not rapid heating. Statement c) is false.

- a) True: on quenching, the chilled outer layer tries to shrink while the hot core resists contraction, putting the surface under tension.
- b) True: surface flaws propagate readily in tension (quenching) but close under surface compression (rapid heating), making rapid cooling more damaging.
- d) True: brittle ceramics break as soon as surface tensile stress reaches $\sigma_f$ because dislocations cannot blunt crack tips.

### Source

Session 16, Slides 17-18 and 21; Session 15, Slide 47.

## Q71.3 Critical cooling temperature for a constrained ceramic

- id: B71-Q3
- concept_id: u8-thermal-shock-stress-calc
- format: numeric
- asks: calculation
- calc: 250 - 270/(300e3*6.0e-6)

A dense ceramic rod ($E = 300\ \text{GPa}$, $\alpha = 6.0\times 10^{-6}\ \text{°C}^{-1}$, tensile fracture stress $\sigma_f = 270\ \text{MPa}$) is rigidly clamped at zero stress at $T_0 = 250\ \text{°C}$ and cooled uniformly. At what temperature $T_f$ does the rod fracture in tension?

a) 150 °C
b) 100 °C
c) 400 °C
d) 249.9 °C

### Answer

b

### Explanation

Session 16, Slide 21: constrained cooling induces tensile stress $\sigma = E\alpha(T_0 - T_f)$. Setting $\sigma = \sigma_f = 270\ \text{MPa}$ with $E = 300\,000\ \text{MPa}$ gives $\Delta T_f = \dfrac{\sigma_f}{E\alpha} = \dfrac{270}{300\,000 \times 6.0\times 10^{-6}} = 150\ \text{°C}$, so fracture occurs at $T_f = 250 - 150 = 100\ \text{°C}$.

- a) Reports the critical temperature drop $\Delta T_f = 150\ \text{°C}$ instead of subtracting it from $T_0 = 250\ \text{°C}$.
- c) Adds $\Delta T_f$ to $T_0$ ($250 + 150 = 400\ \text{°C}$), which corresponds to heating into compression rather than cooling into tension.
- d) Converts $\sigma_f$ to $0.27\ \text{GPa}$ while simultaneously converting $E$ to $300\,000\ \text{MPa}$, creating a factor-of-1000 unit mismatch.

### Source

Session 16, Slide 21.

## Q71.4 Thermal shock resistance parameter TSR

- id: B71-Q4
- concept_id: u8-thermal-shock-tsr
- format: topic-true
- asks: comparison

Referring to the thermal shock resistance parameter $TSR = \sigma_f k / (E\alpha_l)$ of ceramic materials, which one of the following statements is TRUE:

a) Increasing Young's modulus $E$ improves thermal shock resistance because a stiffer crystal resists thermal expansion
b) Increasing the linear expansion coefficient $\alpha_l$ increases $TSR$ by accommodating larger temperature gradients
c) Ceramics as a class have high $TSR$ because their low thermal conductivity prevents heat from entering the bulk
d) Ceramics generally exhibit low $TSR$ because they combine a high elastic modulus $E$ and modest tensile $\sigma_f$ with a low thermal conductivity $k$

### Answer

d

### Explanation

Session 16, Slides 3 and 21: thermal shock resistance $TSR = \sigma_f k/(E\alpha_l)$ is raised by high fracture strength $\sigma_f$ and thermal conductivity $k$, and lowered by high stiffness $E$ and thermal expansion $\alpha_l$. Ceramics typically have high $E$, low $k$, and low tensile fracture strength, giving low thermal shock resistance.

- a) Inverts $E$ in the denominator: higher $E$ produces higher thermal stress $\sigma = E\alpha\Delta T$ for the same strain, lowering $TSR$.
- b) Inverts $\alpha_l$ in the denominator: higher $\alpha_l$ produces larger thermal strain per degree, lowering $TSR$.
- c) Misreads low $k$: low conductivity traps steep temperature gradients near the surface, increasing thermal stresses and reducing $TSR$.

### Source

Session 16, Slides 3 and 21.

## Q71.5 Ordering glasses and glass-ceramics by thermal shock limit

- id: B71-Q5
- concept_id: u8-thermal-shock-low-alpha
- format: ordering
- asks: comparison

Assuming a tensile fracture stress of $69\ \text{MPa}$ and comparable elastic moduli, order the four silicate materials below by INCREASING thermal shock temperature drop to failure:

| Material | $\alpha$ ($\text{°C}^{-1}$) |
| :--- | ---: |
| Fused silica | $0.5\times 10^{-6}$ |
| Soda-lime silicate | $10\times 10^{-6}$ |
| LAS glass-ceramic | $1.2\times 10^{-6}$ |
| Sodium borosilicate | $3\times 10^{-6}$ |

a) soda-lime silicate, sodium borosilicate, LAS glass-ceramic, fused silica
b) fused silica, LAS glass-ceramic, sodium borosilicate, soda-lime silicate
c) soda-lime silicate, LAS glass-ceramic, sodium borosilicate, fused silica
d) sodium borosilicate, soda-lime silicate, fused silica, LAS glass-ceramic

### Answer

a

### Explanation

Session 16, Slide 31: the survivable temperature jump increases inversely with $\alpha$, rising from $80\ \text{°C}$ for soda-lime silicate ($10\times 10^{-6}\ \text{°C}^{-1}$), to $270\ \text{°C}$ for sodium borosilicate ($3\times 10^{-6}$), to $670\ \text{°C}$ for the LAS glass-ceramic ($1.2\times 10^{-6}$), and to $1600\ \text{°C}$ for fused silica ($0.5\times 10^{-6}$).

- b) Reverses the ranking into decreasing thermal shock resistance.
- c) Swaps LAS glass-ceramic and sodium borosilicate despite the 2.5-fold lower expansion of the LAS glass-ceramic.
- d) Misranks adjacent pairs by ignoring the inverse dependence of thermal stress on $\alpha$.

### Source

Session 16, Slide 31.

## Q71.6 Why low-alpha ceramics resist thermal shock

- id: B71-Q6
- concept_id: u8-thermal-shock-low-alpha
- format: complete-sentence
- asks: application

Fused silica and lithium-aluminosilicate (LAS) glass-ceramics tolerate sudden temperature jumps above $600\ \text{°C}$ without cracking chiefly because:

a) their open networks conduct heat rapidly like metals, eliminating surface-to-core gradients
b) ionic diffusion relaxes all internal thermal stresses instantaneously at room temperature
c) their very low linear thermal expansion coefficients $\alpha$ keep constrained thermal strains and stresses small
d) their tensile fracture strengths exceed those of forged aerospace superalloys

### Answer

c

### Explanation

Session 16, Slides 21, 31 and 32: fused silica ($\alpha = 0.5\times 10^{-6}\ \text{°C}^{-1}$) and LAS glass-ceramics ($\alpha = 0.6\text{–}1.2\times 10^{-6}\ \text{°C}^{-1}$) have exceptionally low expansion coefficients, so even large temperature differences generate small thermal stresses $\sigma = E\alpha\Delta T$ and high $TSR$.

- a) False carrier mechanism: fused silica has low thermal conductivity ($k \approx 1.4\ \text{W/(m}\cdot\text{K)}$), nowhere near metallic conduction.
- b) Diffusion is negligible at room temperature and cannot relax rapid thermal stresses in rigid glasses or ceramics.
- d) Glass-ceramics and fused silica fail at modest tensile stresses ($\sim 69\ \text{MPa}$ in the Slide 31 comparison), well below structural alloys.

### Source

Session 16, Slides 21 and 31-32.

## Q71.7 Dielectric and ferroelectric ceramic behaviour

- id: B71-Q7
- concept_id: u8-ferro-dielectric-insulators
- format: true-statement
- asks: classification

Which one of the following statements about the electrical properties of ceramic materials is TRUE:

a) Typical oxide ceramics conduct electricity via mobile valence electron clouds and have low dielectric strength
b) Ceramics are normally electrical insulators with high dielectric strength, while non-centrosymmetric perovskites such as BaTiO₃ are ferroelectric
c) All cubic and HCP ceramic crystals exhibit spontaneous ferroelectricity at room temperature
d) Adding alkali modifiers to silicate ceramics lowers their electrical resistivity to metallic values

### Answer

b

### Explanation

Session 16, Slides 12 and 22: because valence electrons are localized in ionic and covalent bonds, ceramics are usually insulators with high dielectric strength; perovskites such as $\text{BaTiO}_3$ and $\text{SrTiO}_3$ possess unit cells lacking a centre of symmetry and therefore display ferroelectricity.

- a) Inverts electrical behaviour: ceramics lack free electrons and exhibit high dielectric strength and high resistivity.
- c) Wrong symmetry rule: centrosymmetric cubic and closed-packed cells have zero net dipole moment and are not ferroelectric.
- d) Alkali ions introduce modest ionic conduction in glasses at elevated temperature (Slide 31), never metallic conductivity.

### Source

Session 16, Slides 12, 22 and 31.

## Q71.8 Origin of spontaneous dipole in BaTiO3

- id: B71-Q8
- concept_id: u8-ferro-dipole-symmetry
- format: diagram-reading
- asks: figure-reading

The diagram below depicts the room-temperature unit cell of ferroelectric $\text{BaTiO}_3$. Based on the atomic positions and dimensions shown, why does each unit cell carry a permanent electric dipole?

![[attachments/T8/s16-batio3-cell.png]]

a) The unit cell is perfectly cubic ($0.403\ \text{nm}$ on every edge), locking $\text{Ti}^{4+}$ symmetrically at the centre
b) Free conduction electrons accumulate on the top $\text{O}^{2-}$ face relative to the bottom $\text{Ba}^{2+}$ ions
c) The $\text{Ba}^{2+}$ ions sit in tetrahedral sites that cancel the displacement of the oxygen face centres
d) The cell is slightly tetragonal ($0.403\ \text{nm} \neq 0.398\ \text{nm}$) and non-centrosymmetric because $\text{Ti}^{4+}$ and $\text{O}^{2-}$ shift in opposite vertical directions

### Answer

d

### Explanation

Session 16, Slide 22: the room-temperature $\text{BaTiO}_3$ cell is slightly elongated along one axis ($0.403\ \text{nm}$ vs. $0.398\ \text{nm}$), with $\text{Ti}^{4+}$ shifted upward by $0.006\ \text{nm}$ from the centre and $\text{O}^{2-}$ shifted downward by $0.006\text{–}0.009\ \text{nm}$. This asymmetry separates the positive and negative charge centres, producing a net dipole in every unit cell.

- a) Contradicts the labelled edge lengths ($0.403\ \text{nm}$ vs. $0.398\ \text{nm}$) and the asymmetric ion shifts shown on the right projection.
- b) Ceramics such as $\text{BaTiO}_3$ are insulators with no free conduction-electron cloud; the dipole comes from bound ion displacements.
- c) The diagram places $\text{Ba}^{2+}$ at the cube corners ($\text{C.I.} = 12$ in perovskite), not in tetrahedral interstitials.

### Source

Session 16, Slide 22.

## Q71.9 Direct and reverse piezoelectric effects

- id: B71-Q9
- concept_id: u8-ferro-piezo-mechanisms
- format: topic-false
- asks: definition

Regarding ferroelectric and piezoelectric ceramics such as $\text{BaTiO}_3$ and $\text{PbZrO}_3$–$\text{PbTiO}_3$ (PZT), which one of the following statements is FALSE:

a) In the direct piezoelectric effect, applying an external voltage changes the volume of the crystal while the dipole spacing remains zero
b) Ferroelectric ceramics exhibit piezoelectricity because their unit cells lack a centre of symmetry and contain electric dipoles
c) In the direct piezoelectric effect, an applied compressive stress reduces dipole spacing and generates a voltage difference
d) In the reverse piezoelectric effect, an applied electric field shifts the ion dipoles and produces a dimensional change

### Answer

a

### Explanation

Session 16, Slide 22: applying a voltage to produce a change in volume or shape is the **reverse** piezoelectric effect (not the direct effect), and piezoelectric ceramics require non-zero unit-cell dipoles. Statement a) is false.

- b) True: non-centrosymmetric unit cells with permanent dipoles give ferroelectric compounds their piezoelectric coupling (Slide 22).
- c) True: compressive stress alters the distance between positive and negative charge centres and induces an electric potential difference (direct effect).
- d) True: an applied voltage acts on the charged ions and changes cell dimensions (reverse effect).

### Source

Session 16, Slides 12 and 22.

## Q71.10 Transducer response under stress vs voltage

- id: B71-Q10
- concept_id: u8-ferro-piezo-mechanisms
- format: what-happens
- asks: application

A piezoelectric $\text{BaTiO}_3$ ceramic disk is first squeezed axially by a mechanical force in an open circuit and is later connected to a DC power supply without external load. Respectively, what occurs in the two steps?

a) First, the disk expands thermally; second, it loses its dipole moment permanently
b) First, the disk undergoes a dimensional change from electrostriction; second, it generates an open-circuit voltage
c) First, dipole compression produces an electrical potential difference; second, the applied voltage changes the disk dimensions
d) First, plastic dislocation glide aligns the grains; second, magnetic flux is expelled from the bulk

### Answer

c

### Explanation

Session 16, Slide 22: squeezing the piezoelectric crystal reduces the dipole spacing and produces a voltage (the direct effect used in sensors and spark igniters), whereas applying an electrical voltage displaces the charged ions and alters the crystal volume/dimensions (the reverse effect used in actuators and ultrasonic transducers).

- a) Confuses electromechanical coupling with Joule heating and Curie depolarization.
- b) Swaps the direct and reverse piezoelectric responses between the mechanical and electrical inputs.
- d) Applies metallic dislocation slip and superconducting Meissner flux expulsion to a ceramic dielectric.

### Source

Session 16, Slide 22.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
