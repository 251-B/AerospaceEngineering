---
materia: Aerospace Materials I
tema: "Unit 11: joint stress states, peel versus shear, overlap geometry and thermal expansion compatibility"
bank_id: B109
title: "Joint Design and Stress States"
category: mt3_test_block
unit: 11
concepts:
  - u11-design-2017-ord-l-joint
  - u11-design-2013-ord-butt-vs-lap
  - u11-design-stress-modes-shear-peel
  - u11-design-lap-geometries-eccentricity
  - u11-design-tapered-scarf-stepped
  - u11-design-beveled-edges-mechanism
  - u11-design-combination-joints
  - u11-design-subassemblies-curvature
  - u11-design-cte-selection
  - u11-design-overlap-length-numeric
difficulty: 2
origen: "Questions written for the bank in the style of Part I of Assessment Test III, including Q4B of the January 2013 and Q10 of the January 2017 final exams. Content from Session 24, Slides 17-20 and 28."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-11
---

# Bank B109 — Joint Design and Stress States

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test III, including official final exam questions from January 2013 and January 2017 (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 24, Slides 17-20 and 28.

## Q109.1 L-bracket joint orientation and stress minimization

- id: B109-Q1
- concept_id: u11-design-2017-ord-l-joint
- format: diagram-reading
- asks: application
- origin: official-exam

![[attachments/T11/s24-joint-design-yes-no.png]]

In the middle pair of 90° L-joint brackets shown (top `YES` configuration versus bottom `NO` configuration), why is the top `YES` geometry structurally correct, and which stresses should be maximized and minimized in adhesive joint design?

a) Pulling right puts the adhesive in pure tension; maximize tensile peel and minimize shear
b) The overhanging upper flange presses the vertical flange into the post to compress the loaded edge; maximize shear and compression, and minimize peel, cleavage, and tensile loading
c) Both configurations place identical bending cleavage on the bottom corner, differing only in adhesive thickness
d) The bottom `NO` configuration suppresses opening at the top edge by transferring the load through pure compression

### Answer

b

### Explanation

January 2017 ordinary final exam, Q10 (and Session 24, Slide 18): in the correct `YES` L-joint (left joint in 2017 Q10), the upper flange extends across the top of the vertical post so pulling right presses the vertical overlap together in shear and compression ("compressed peel"), avoiding opening at the loaded edge. In the `NO` geometry, pulling right pries the horizontal leg away from the post, initiating cleavage/peel at the top edge. Good joint design maximizes shear and compression while minimizing tensile peel, cleavage, and pure tension.

- a) Inverts the stress design rules: pure tension and tensile peel cause premature edge fracture and must be minimized.
- c) Misreads the load path: the `NO` flange peels outward at its upper edge, whereas the `YES` flange pushes against the post.
- d) Reverses the two geometries: the bottom `NO` configuration opens under peel/cleavage rather than compressing the bondline.

### Source

MATERIALS_FINALEXAM_2017_ORD.pdf, p. 5 Q10; Session 24, Slide 18.

## Q109.2 Butt joint versus simple lap joint in thin sheets

- id: B109-Q2
- concept_id: u11-design-2013-ord-butt-vs-lap
- format: true-statement
- asks: comparison
- origin: official-exam

When joining two thin metallic sheets subjected to axial tensile forces, which statement explains why a simple lap joint is selected over a butt joint?

a) A simple lap joint provides a large overlap area loaded in shear, whereas a butt joint places a tiny cross-sectional area in direct tension
b) A butt joint places the entire bondline in shear, whereas a simple lap joint avoids all bending moments
c) A butt joint distributes stresses uniformly over a large surface area, whereas a simple lap joint carries load on a single edge line
d) Both joints offer identical static capacity whenever the adhesive thickness equals the sheet thickness

### Answer

a

### Explanation

January 2013 ordinary final exam, Q4B Case 2 (and Session 24, Slides 18-19): a butt joint between thin sheets has a bonding area equal only to the tiny sheet thickness and carries the load in unfavourable pure tension. Converting it to a simple lap joint enlarges the bonded area and transfers the axial force primarily in shear.

- b) Reverses the stress modes: a butt joint under axial pull is in pure tension, while a simple lap joint carries shear (with minor end eccentricity).
- c) Attributes large bonding area to a thin-edge butt joint, which actually has the smallest possible bond area.
- d) Changing adhesive thickness does not compensate for the drastically smaller bonded area and pure tensile stress state of a butt joint.

### Source

MATERIALS_FINALEXAM_2013_ORD.pdf, p. 1 Q4B; Session 24, Slides 18-19.

## Q109.3 Shear and compression versus peel and cleavage

- id: B109-Q3
- concept_id: u11-design-stress-modes-shear-peel
- format: topic-false
- asks: comparison

Regarding the stress states encountered by structural adhesive joints, which one of the following statements is FALSE:

a) Shear and compressive loads are favourable because the whole overlap surface contributes to carrying the force
b) Peel concentrates the entire applied force along a thin line at the advancing adhesion front
c) Cleavage acts like an off-center pry at one edge of a rigid joint, creating severe tensile stress peaks
d) Peel and cleavage distribute stress uniformly across the full bonded area, making them ideal primary design modes

### Answer

d

### Explanation

Session 24, Slides 18 and 27-28: adhesives perform best in shear and compression because the entire bonded surface shares the load uniformly, whereas peel and cleavage concentrate stress along one edge line and must be minimized. Statement d is false.

- a) True: Slide 28 emphasizes that under normal compression and shear the joint operates over the whole surface.
- b) True: Slide 27 explicitly highlights that peel concentrates stresses along the narrow adhesion front line.
- c) True: Slide 18 pairs cleavage with peel and thin-sheet tension in the `NO` row of loading modes.

### Source

Session 24, Slides 18 and 27-28.

## Q109.4 Symmetric overlap geometry and bending eccentricity

- id: B109-Q4
- concept_id: u11-design-lap-geometries-eccentricity
- format: diagram-reading
- asks: figure-reading

![[attachments/T11/s24-lap-joint-types.png]]

Examine the standard adhesive joint cross-sections shown. Which geometry joins a single central plate slotted symmetrically between two integrally forked outer tongues—without separate cover straps—to eliminate the out-of-plane bending eccentricity of a simple lap joint?

a) Simple lap joint
b) Strap joint
c) Double lap joint
d) Butt joint

### Answer

c

### Explanation

Session 24, Slide 20: in a double lap joint, the central plate is sandwiched symmetrically between two upper and lower tongues of the mating member, doubling the shear area and balancing the load path so out-of-plane peel bending moments cancel out.

- a) A simple lap joint has offset load axes that generate an eccentric bending moment and peel stresses at the overlap ends.
- b) A single strap joint is asymmetric on one face only, which still induces bending eccentricity under tension.
- d) A butt joint places the bond plane perpendicular to the load in unfavourable pure tension over a small area.

### Source

Session 24, Slide 20.

## Q109.5 Tapered and scarf joints versus square-ended lap joints

- id: B109-Q5
- concept_id: u11-design-tapered-scarf-stepped
- format: diagram-reading
- asks: comparison

![[attachments/T11/s24-joint-design-poor-good.png]]

In the design comparison shown, why does the scarf/tapered overlap configuration in row `(c) Very good` outperform the square-ended simple lap joint in row `(b) Good`?

a) Tapering the adherend ends aligns the load path and reduces stress peaks at the overlap edges
b) Tapering reduces the bonded overlap area to a small line so stress concentrates evenly
c) Square-ended laps suffer higher compressive loading, whereas scarf joints convert shear into pure peel
d) Row `(c)` eliminates adhesive entirely and relies strictly on mechanical interference

### Answer

a

### Explanation

Session 24, Slides 19-20: row `(b) Good` (simple lap) improves on `(a) Poor` (butt) by loading the overlap in shear, while `(c) Very good` goes further by tapering or scarfing the adherends (reducing stiffness mismatch at the ends and aligning the load line) to suppress edge peel and shear stress spikes.

- b) Good joint design aims for large bonding area and uniform load transfer, never shrinking the area to a single line.
- c) Inverts the mechanics: scarf and tapered joints reduce peel and edge spikes rather than converting shear into peel.
- d) All geometries in rows `(a)`–`(c)` are purely bonded adhesive joints; fasteners appear only in row `(d)`.

### Source

Session 24, Slides 19-20.

## Q109.6 Mechanism of beveled overlap edges and adhesive fillets

- id: B109-Q6
- concept_id: u11-design-beveled-edges-mechanism
- format: cause-effect
- asks: cause

Beveling (tapering) the outer edges of stepped or tapered lap adherends markedly increases joint fatigue resistance because tapering:

a) increases bondline thickness locally at the center so cure shrinkage stops
b) prevents the adhesive from wetting the overlap ends, leaving soft boundary gaps
c) transfers the entire axial load strictly through normal tension across the tip
d) lowers local shear-lag and peel stress concentrations where edge cracks initiate

### Answer

d

### Explanation

Session 24, Slides 18-20 (with standard shear-lag beveling mechanics): abrupt square adherend ends create sharp stiffness jumps and peel/shear stress peaks at the overlap edges. Tapering or beveling those edges provides a gradual stiffness transition that suppresses stress concentrations where cracks nucleate.

- a) Increasing adhesive thickness does not stop shrinkage and usually reduces apparent shear strength (Slide 26).
- b) Poor wetting at the overlap edges introduces unbonded flaws that accelerate fatigue crack growth rather than stopping it.
- c) Normal tension at the overlap tip would drive opening peel fracture rather than improving fatigue life.

### Source

Session 24, Slides 18-20.

## Q109.7 Role of combination (hybrid) joints

- id: B109-Q7
- concept_id: u11-design-combination-joints
- format: identify
- asks: application

Why do aerospace structures sometimes employ combination joints—combining an adhesive bondline with end rivets or spot welds?

a) To melt the polymer adhesive during welding so it flows into an elastic thermoplastic film
b) To resist out-of-plane peel or cleavage at overlap ends and provide fail-safe crack arrest while the adhesive carries shear
c) To eliminate all surface cleaning and degreasing before applying the structural adhesive
d) To increase stress concentration around fastener holes while leaving the overlap unbonded

### Answer

b

### Explanation

Session 24, Slide 19 (`(d) Combination joints`): pairing adhesive bonding with rivets or spot welds combines the uniform shear transfer of the adhesive with mechanical/metallurgical arrest of out-of-plane peel and crack propagation at joint boundaries.

- a) Spot welding near an adhesive requires controlled weld-bonding sequencing so the adhesive is not thermally destroyed, not melted into a thermoplastic film.
- c) Reliable adhesive bonding in combination joints still demands full surface preparation and cleanliness.
- d) The purpose of bonding in a hybrid joint is to carry shear smoothly and relieve fastener hole loads, not leave the overlap unbonded.

### Source

Session 24, Slide 19.

## Q109.8 Subassembly planning and curvature restrictions

- id: B109-Q8
- concept_id: u11-design-subassemblies-curvature
- format: complete-sentence
- asks: application

To maximize manufacturability and bondline reliability across an airframe assembly, bonded subassemblies should be designed to:

a) maximize the number of sequential adhesive cures and incorporate tight double-curved flanges
b) orient every structural bondline perpendicular to the primary tensile load
c) minimize the number of adhesive operations and avoid parts with complex curvature
d) rely solely on thick adhesive fillets to fill mismatched 5 mm assembly gaps

### Answer

c

### Explanation

Session 24, Slide 19 explicitly specifies two practical design rules for adhesive assemblies: subassemblies should be designed to minimize adhesive operations, and parts with complex curvature should be avoided (since complex curvature complicates uniform pressure/jigging and bondline thickness control).

- a) Adding sequential bonding steps and complex curves multiplies defect risk and tooling cost.
- b) Placing bondlines perpendicular to tension creates butt joints (explicitly discouraged on Slide 18).
- d) Excessive bondline gaps weaken structural shear strength (Slide 26) and exceed gap limits of fast-curing structural adhesives.

### Source

Session 24, Slides 18-19 and 26.

## Q109.9 Coefficient of thermal expansion (CTE) compatibility in adhesive selection

- id: B109-Q9
- concept_id: u11-design-cte-selection
- format: what-happens
- asks: effect

When an aluminium wing rib ($\alpha \approx 23 \times 10^{-6}\text{ }^\circ\text{C}^{-1}$) is bonded to a quasi-isotropic carbon-epoxy spar ($\alpha \approx 2 \times 10^{-6}\text{ }^\circ\text{C}^{-1}$) with a stiff adhesive cured at 180 °C, what happens as the assembly cools to service temperatures?

a) Both adherends shrink identically so the bondline remains completely stress-free
b) The adhesive lowers both substrates' CTE values to match each other permanently
c) Curing shrinkage converts the thermoset epoxy into a ductile metal matrix
d) Differential contraction induces residual thermal stresses across the bondline, increasing debonding risk

### Answer

d

### Explanation

Session 24, Slides 17 and 32-33: compatible coefficients of thermal expansion are a key adhesive-selection criterion because differences in thermal expansion between bonded adherends generate residual stresses ($\sigma_{\text{residual}}$) on cooling and during thermal cycling.

- a) Aluminium has roughly ten times the linear thermal expansion coefficient of carbon-epoxy, so contractions differ strongly.
- b) An adhesive cannot alter the intrinsic thermal expansion coefficients of bulk metallic or composite adherends.
- c) Cure shrinkage is a polymer cross-linking/volume contraction effect and never turns epoxy into a metal matrix.

### Source

Session 24, Slides 17 and 32-33.

## Q109.10 Required overlap length for a single-lap shear joint

- id: B109-Q10
- concept_id: u11-design-overlap-length-numeric
- format: numeric
- asks: calculation
- calc: 6000 / (25 * 8.0)

A single-lap joint of bond width $w = 25\text{ mm}$ must carry an axial tensile force $F = 6.0\text{ kN}$ while keeping the average adhesive shear stress below an allowable limit $\tau_{\text{allow}} = 8.0\text{ MPa}$. What minimum overlap length $L$ is required?

a) 30 mm
b) 15 mm
c) 48 mm
d) 60 mm

### Answer

a

### Explanation

Session 24, Slides 25 and 28: in a single-lap joint loaded in shear over a uniform bonded area $A = w L$, average shear stress is $\tau = F/(wL)$. Setting $\tau = \tau_{\text{allow}} = 8.0\text{ MPa} = 8.0\text{ N/mm}^2$ gives $L = F/(w\tau_{\text{allow}}) = 6000\text{ N} / (25\text{ mm} \times 8.0\text{ N/mm}^2) = 30\text{ mm}$.

- b) Halves the required overlap ($15\text{ mm}$), which would correspond to a double-lap joint with two shear planes or double the allowable stress.
- c) Computes $6000/(25 \times 5)$ or misapplies a unit factor, giving an oversized overlap of 48 mm.
- d) Applies an extra factor of 2 ($60\text{ mm}$), corresponding to an unstated $4.0\text{ MPa}$ stress limit.

### Source

Session 24, Slides 25 and 28.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
