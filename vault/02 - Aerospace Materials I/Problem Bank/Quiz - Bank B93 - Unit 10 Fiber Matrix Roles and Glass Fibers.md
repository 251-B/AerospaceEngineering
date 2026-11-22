---
materia: Aerospace Materials I
tema: "Unit 10: roles of fibres and matrix in FRPs, crack transfer and critical fibre length, composite limitations, glass-fibre composition and grades (E, A, C, ECR, S) and surface sizing"
bank_id: B93
title: "Fibre-matrix roles and glass fibres"
category: mt3_test_block
unit: 10
concepts:
  - u10-matrix-role-not
  - u10-matrix-role-primary
  - u10-matrix-role-crack-transfer
  - u10-matrix-role-composite-limits
  - u10-glass-general-properties
  - u10-glass-grades-comparison
  - u10-glass-sizing-role
  - u10-glass-critical-length-calc
  - u10-matrix-role-critical-length
  - u10-glass-grades-ordering
difficulty: 2
origen: "Includes Q8 of MATERIALS_THIRDPARTIAL_2020.pdf and Q3a of MATERIALS_FINALEXAM_2014_ORD.pdf alongside practice items in the style of Part I. Content and data from Session 21 Slides 14-20, 28, 42 and Session 22 Slides 6, 18."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-10
---

# Bank B93 — Fibre-matrix roles and glass fibres

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Question 1 reproduces Q8 of `MATERIALS_THIRDPARTIAL_2020.pdf` (Model B) and Question 2 adapts Q3a of `MATERIALS_FINALEXAM_2014_ORD.pdf`; the remaining eight are practice items. Content: Session 21, Slides 14–20, 28, 42 and Session 22, Slides 6, 18.

## Q93.1 Non-function of the matrix in a fibre composite

- id: B93-Q1
- concept_id: u10-matrix-role-not
- format: identify
- asks: classification
- origin: official-exam

Indicate which of the following is NOT the function of the matrix in a fiber reinforced composite:

a) Transfer external load among fibers
b) Prevents chemical and abrasive degradation of the fibers
c) Keeps fiber orientation
d) Support the major part of the applied load

### Answer

d

### Explanation

MATERIALS_THIRDPARTIAL_2020.pdf, p. 2 (Assessment Test III, Model B Q8) and Session 21, Slide 16: supporting the major part of the applied load is the primary function of the **fibres** ($\sigma_{1f} \gg \sigma_{1m}$), not of the matrix.

- a) True matrix function (Session 21, Slide 16; Session 22, Slide 6): transfers external loads into and out of the fibres.
- b) True matrix function (Session 21, Slide 16): protects the fibres from environmental, chemical and abrasive degradation.
- c) True matrix function (Session 21, Slide 16): maintains fibre alignment and component shape.

### Source

MATERIALS_THIRDPARTIAL_2020.pdf, p. 2 (Model B Q8); Session 21, Slide 16; Session 22, Slide 6.

## Q93.2 Primary roles of matrix and fibres

- id: B93-Q2
- concept_id: u10-matrix-role-primary
- format: topic-true
- asks: definition
- origin: official-exam

Regarding the primary roles of the matrix and the fibres in a continuous-fibre reinforced composite, indicate which statement is TRUE:

a) The matrix carries most of the applied tensile load, while the fibres serve mainly to bind and shape the component
b) The fibres provide strength by carrying most of the applied load, while the matrix transfers load, separates and protects the fibres, maintains orientation and provides ductility and toughness
c) Both phases carry identical axial stresses regardless of elastic modulus, so the matrix supplies the composite's longitudinal stiffness
d) The fibres prevent adjacent matrix cracking by melting locally around flaws, while the matrix keeps the composite purely brittle

### Answer

b

### Explanation

MATERIALS_FINALEXAM_2014_ORD.pdf, p. 5 (Q3a) and Official Key (COMPILATION p. 14), matching Session 21, Slide 16: the strong, stiff, brittle fibres carry most of the applied load, whereas the soft, ductile matrix shapes the part, transfers load into and out of the fibres, separates fibres to arrest crack propagation, protects them from environmental degradation, maintains orientation and provides ductility and toughness.

- a) Inverts the structural division of labour between fibres and matrix.
- c) Confuses isostrain ($\varepsilon_f = \varepsilon_m$) with equal stress: because $E_f \gg E_m$, the fibres operate at much higher axial stress ($\sigma_f \gg \sigma_m$).
- d) Invents local melting of high-melting fibres and reverses the toughness contribution of the ductile matrix.

### Source

MATERIALS_FINALEXAM_2014_ORD.pdf, p. 5 (Q3a); Official Key COMPILATION p. 14; Session 21, Slide 16.

## Q93.3 Stress redistribution at a broken fibre

- id: B93-Q3
- concept_id: u10-matrix-role-crack-transfer
- format: diagram-reading
- asks: cause

The schematic below shows a longitudinal section of a fibre-reinforced composite in which the central fibre has fractured at $z = 0$. Which mechanism prevents that single fibre break from causing immediate failure of the adjacent intact fibres?

![[attachments/T10/s22-fibre-crack-matrix-functions.png]]

a) The broken fibre ends weld back together instantaneously under axial tension $\sigma_f$
b) The matrix carries zero shear stress along the fibre interface, isolating the broken filament completely
c) Interfacial shear stress $\tau$ in the matrix transfers load around the break over a length $\delta_c$ into neighbouring fibres and back into the broken fibre
d) Adjacent fibres fracture simultaneously across $z = 0$ to equalise strain across every filament

### Answer

c

### Explanation

Session 22, Slide 6 and Session 21, Slide 16: at a fibre crack ($z = 0$), the axial stress in the broken filament drops to zero; the surrounding matrix separates the fibres and transfers load via interfacial shear stress $\tau$ to neighbouring filaments and back into the broken fibre over a transfer distance $\delta_c$, stopping crack propagation.

- a) Brittle fibres cannot cold-weld under tension inside a polymer or ceramic matrix.
- b) Contradicts the diagram arrows labelled $\tau$, which explicitly depict shear stress along the fibre–matrix interface.
- d) Describes catastrophic failure of an unbonded bundle rather than matrix-mediated crack arrest.

### Source

Session 22, Slide 6; Session 21, Slide 16.

## Q93.4 Primary limitations of fibre-reinforced composites

- id: B93-Q4
- concept_id: u10-matrix-role-composite-limits
- format: false-statement
- asks: application

Which of the following statements about high-performance fibre-reinforced composites is FALSE:

a) Extensive plastic yielding around drilled holes allows fibre-reinforced PMCs to redistribute stress concentrations in bolted joints like ductile metals
b) Two primary factors limiting applications of fibre-reinforced composites are the absence of plasticity and low damage tolerance
c) Small accidental impacts can trigger internal delaminations that significantly reduce mechanical resistance
d) Pairing strong, stiff, brittle fibres with a soft, ductile matrix aims to achieve high specific strength and high specific modulus with good fatigue resistance

### Answer

a

### Explanation

Session 21, Slides 15–16: the absence of plasticity in fibre-reinforced composites is critical in mechanical joints because the material cannot yield locally at bolt holes to relieve stress concentrations, and low damage tolerance means minor impacts can cause delaminations that degrade strength.

- b) True (Slide 15): absence of plasticity and low damage tolerance are the two primary limiting factors listed.
- c) True (Slide 15): small accidental impacts induce delaminations leading to a loss of mechanical resistance ($R_{\text{mechanical}}$).
- d) True (Slide 16): combining stiff brittle fibres and a ductile matrix yields high specific strength, specific modulus and fatigue performance.

### Source

Session 21, Slides 15–16.

## Q93.5 Composition and general properties of glass fibres

- id: B93-Q5
- concept_id: u10-glass-general-properties
- format: topic-false
- asks: comparison

Regarding glass fibres used to reinforce polymer matrices, which one of the following statements is FALSE:

a) They are based on $\text{SiO}_2$ ($50\text{–}70\%$) combined with oxides of Ca, Al, B, Na, Mg and K
b) They are amorphous, isotropic, non-combustible and electrically and thermally insulating
c) Low cost, versatility and ease of processing make glass fibres the most widely used polymer reinforcement
d) Compared with carbon and aramid fibres, glass fibres exhibit a higher elastic modulus and lower density

### Answer

d

### Explanation

Session 21, Slide 17: compared with carbon and aramid fibres, glass fibres exhibit **lower** elastic modulus (with higher elongation to failure) and **higher** density ($\sim 2.5\text{–}2.6\text{ g/cm}^3$ vs $\sim 1.44\text{ g/cm}^3$ for aramid and $\sim 1.8\text{ g/cm}^3$ for carbon), although they retain high tensile strength and low cost.

- a) True (Slide 17): silica-based ($50\text{–}70\%\ \text{SiO}_2$) with Ca, Al, B, Na, Mg and K oxides.
- b) True (Slide 17): glass fibres are amorphous, isotropic, non-combustible and insulating (low thermal conductivity $k$, low thermal expansion $\alpha$).
- c) True (Slide 17): low cost and processing versatility explain their dominant commercial share in GFRP.

### Source

Session 21, Slide 17.

## Q93.6 Aerospace selection among glass fibre grades

- id: B93-Q6
- concept_id: u10-glass-grades-comparison
- format: identify
- asks: classification

Which type of glass fibre is a boron-free magnesium aluminosilicate ($\sigma_t \approx 4590\text{ MPa}$, $E = 86.0\text{ GPa}$, $T_m = 1454\ ^\circ\text{C}$) selected specifically for aerospace and aeronautical structures requiring high tensile strength and thermal stability?

a) A-glass
b) E-glass
c) S-glass
d) ECR-glass

### Answer

c

### Explanation

Session 21, Slide 18: S-glass is a boron-free magnesium aluminosilicate with the lowest density ($2.48$), highest tensile strength ($4590\text{ MPa}$), highest modulus ($86.0\text{ GPa}$) and highest softening/melting temperature ($1454\ ^\circ\text{C}$), specified for aerospace and aeronautic applications.

- a) A-glass is alkali-rich with the lowest strength ($3040\text{ MPa}$) and modulus ($69.0\text{ GPa}$), used for basic chemical resistance.
- b) E-glass is a Ca aluminoborosilicate ($3450\text{ MPa}$, $72.5\text{ GPa}$), the cheapest grade used for electrical properties and circuit boards.
- d) ECR-glass ($3625\text{ MPa}$, $72.5\text{ GPa}$) targets combined electrical and chemical resistance rather than peak aerospace strength.

### Source

Session 21, Slide 18.

## Q93.7 Role of sizing and coupling agents on glass fibres

- id: B93-Q7
- concept_id: u10-glass-sizing-role
- format: topic-true
- asks: cause

Referring to the surface sizing applied to glass fibres immediately after drawing, which one of the following statements is TRUE:

a) Sizing combines a film-forming polymer and a coupling agent to bind filaments, lubricate against abrasion, impart anti-static behaviour and improve interfacial bonding
b) Uncoated glass fibres maintain maximum tensile strength indefinitely in humid air because adsorbed water heals surface microcracks
c) Sizing consists solely of molten metallic aluminium sprayed onto glass strands to increase electrical conductivity
d) Coupling agents such as organosilanes prevent any chemical bonding between the glass surface and the polymer matrix

### Answer

a

### Explanation

Session 21, Slide 19 and Session 22, Slide 18: glass-fibre strength is governed by surface processing damage and water adsorption; sizing—comprising a film-forming polymer (such as polyvinyl acetate) and a coupling agent (organosilane, titanate or chromate)—binds filaments together, lubricates against abrasion, gives anti-static properties and introduces chemical functionalities to boost interfacial bond strength.

- b) Inverts moisture sensitivity: water adsorption and surface scratches degrade glass-fibre strength by introducing surface flaws.
- c) Misidentifies the chemical composition of sizing (polymer film former plus organosilane/titanate/chromate coupling agent) and ignores glass insulation.
- d) Reverses the purpose of coupling agents: organosilanes form covalent $\text{M–O–Si}$ bonds with glass and diffuse into the polymer to strengthen the interface.

### Source

Session 21, Slide 19; Session 22, Slide 18.

## Q93.8 Critical fibre length calculation

- id: B93-Q8
- concept_id: u10-glass-critical-length-calc
- format: numeric
- asks: calculation
- calc: 3450 * 0.012 / (2 * 23)

Effective reinforcement in a discontinuous-fibre composite requires fibre length $l$ to exceed the critical length $l_c = \dfrac{\sigma_f^* d}{2\tau_c}$, where $\sigma_f^*$ is fibre tensile strength, $d$ is fibre diameter and $\tau_c$ is interfacial shear strength (or matrix shear yield strength). For an E-glass fibre with $\sigma_f^* = 3450\text{ MPa}$ and $d = 12\ \mu\text{m}$ in an epoxy matrix with $\tau_c = 23\text{ MPa}$, calculate $l_c$:

a) 0.45 mm
b) 0.90 mm
c) 1.80 mm
d) 9.00 mm

### Answer

b

### Explanation

Using the critical fibre-length formula (Callister extension of the shear load-transfer distance $\delta_c$ shown in Session 22, Slide 6, with E-glass strength and filament size from Session 21, Slides 18 and 28): converting $d = 12\ \mu\text{m} = 0.012\text{ mm}$, $l_c = \dfrac{3450\text{ MPa} \times 0.012\text{ mm}}{2 \times 23\text{ MPa}} = \dfrac{41.4}{46} = 0.90\text{ mm}$. Units: $\text{MPa}$ cancels in numerator and denominator, leaving $\text{mm}$.

- a) Substituted the fibre radius ($d/2 = 6\ \mu\text{m}$) into the diameter formula, halving $l_c$ to $0.45\text{ mm}$.
- c) Omitted the factor of $2$ in the denominator, giving $3450 \times 0.012 / 23 = 1.80\text{ mm}$.
- d) Misconverted $12\ \mu\text{m}$ as $0.12\text{ mm}$, inflating the answer tenfold to $9.00\text{ mm}$.

### Source

Session 21, Slides 18 and 28; Session 22, Slide 6 (load-transfer distance $\delta_c$, with explicit $l_c = \sigma_f^* d/(2\tau_c)$ extension).

## Q93.9 Effect of degraded interfacial shear strength on critical fibre length

- id: B93-Q9
- concept_id: u10-matrix-role-critical-length
- format: what-happens
- asks: effect

In a short-fibre glass/epoxy composite governed by the critical length $l_c = \dfrac{\sigma_f^* d}{2\tau_c}$, what happens to $l_c$ and load transfer if moisture attack at the interface cuts the shear bond strength $\tau_c$ in half?

a) $l_c$ decreases by half, allowing shorter fibres to fracture before pulling out
b) $l_c$ remains unchanged because critical fibre length depends only on fibre modulus
c) $l_c$ drops to zero because water acts as a plasticizer that transfers tensile stress directly across air gaps
d) $l_c$ doubles, so fibres that previously carried peak fracture stress now slip and pull out at lower composite stress

### Answer

d

### Explanation

Since $l_c = \dfrac{\sigma_f^* d}{2\tau_c}$ is inversely proportional to $\tau_c$ (extension of shear load transfer in Session 22, Slide 6, combined with glass moisture degradation on Session 21, Slide 19), halving $\tau_c$ doubles $l_c$. Longer interface distances are then required to build up $\sigma_f^*$ in the fibre, so formerly effective short fibres slip and pull out prematurely.

- a) Inverts the inverse dependence on $\tau_c$: weaker bonding needs a longer transfer length, not a shorter one.
- b) Ignores $\tau_c$ in the denominator and substitutes modulus for strength and interfacial shear.
- c) Misrepresents moisture attack: adsorbed water degrades interfacial adhesion and surface strength rather than transferring stress.

### Source

Session 21, Slide 19; Session 22, Slide 6 (critical-length scaling extension).

## Q93.10 Glass fibre grades ordered by tensile strength

- id: B93-Q10
- concept_id: u10-glass-grades-ordering
- format: ordering
- asks: comparison

Order the three glass-fibre grades in increasing tensile strength (and elastic modulus):

a) S-glass $<$ E-glass $<$ C-glass
b) E-glass $<$ C-glass $<$ S-glass
c) C-glass $<$ E-glass $<$ S-glass
d) C-glass $<$ S-glass $<$ E-glass

### Answer

c

### Explanation

Session 21, Slide 42 (and Slide 18): tensile strengths and moduli increase in the sequence C-glass ($3100\text{ MPa}$, $69\text{ GPa}$) $<$ E-glass ($3400\text{–}3450\text{ MPa}$, $72.4\text{–}72.5\text{ GPa}$) $<$ S-glass ($4590\text{–}4800\text{ MPa}$, $85.5\text{–}86.0\text{ GPa}$).

- a) Reverses the ranking from highest to lowest strength.
- b) Swaps the electrical/general grade E-glass below chemical-resistant C-glass.
- d) Places aerospace high-strength S-glass below E-glass.

### Source

Session 21, Slides 18 and 42.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
