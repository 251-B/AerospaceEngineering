---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 3"
dificultad: easy
badge: "Chain orientation · processing and strength"
tags:
  - official-problem
  - solved
  - chain-orientation
  - crystallinity
  - strength
---

# ✏️ Problem: T9-03 — Rolling or Fast-Cooled Casting for a Stronger Thermoplastic

## 📄 Official Statement
> 3. Assuming that a thermoplastic polymer can be produced by rolling (deformation) and casting (with fast cooling). Which one of the two methods will produce a polymer with higher strength? Explain your answer.
>
> *(Solution: polymer produced by rolling)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Same polymer.** Both routes use the same thermoplastic (same chains, same molecular weight); only the processing differs.
2. **Rolling.** Rolling deforms the solid polymer, stretching it in the rolling direction.
3. **Casting with fast cooling.** The polymer is poured as a melt into a mould and cooled quickly, so the chains solidify in the arrangement they had in the liquid.
4. **What the slides say about strength.** Deforming a polymer can increase its strength, because the chains become oriented and interact more effectively; the strength also increases with the degree of crystallinity [Session 19 Slide 43]. An oriented polymer is significantly stronger and stiffer than an isotropic one [Session 19 Slide 39].

### Data
| Route | State of the chains |
| :--- | :--- |
| Rolling | chains aligned by the deformation |
| Fast-cooled casting | chains frozen as random coils, little time to crystallize |

**Unknown:** the route that gives the higher strength, and why.

---

## 🧠 2. Model and Strategy

The strength of a thermoplastic is set by how the chains resist sliding past each other: aligned, well-packed chains share the load through many secondary bonds along their length, while random coils carry it through few contacts and entanglements. The cold-drawing and strain-hardening stages of the tensile test show the same mechanism inside one specimen [Session 19 Slides 38-39].

![[attachments/T9/s19-strain-hardening-chains.png]]

**Strategy.**
1. Describe the chain arrangement after each route.
2. Compare the two with the factors of Slide 43.

---

## 🔢 3. Step-by-Step Derivation

### 1. Rolling [Session 19 Slides 38-39, 43]
The deformation unravels the coiled chains and aligns them parallel to the rolling direction, as in the cold drawing of the tensile test (Slide 38: the chains unravel, aligning themselves parallel to the direction of the applied stress). The aligned chains lie closer and interact more effectively, so more secondary bonds must be broken for them to slide; in a semicrystalline polymer the lamellae are also tilted and their block segments aligned with the axis (Slide 41). This is the strain hardening of Slide 39: the oriented polymer is significantly stronger and stiffer.

### 2. Casting with fast cooling [Session 19 Slides 26, 28]
In the melt the chains are random coils. Fast cooling gives them little time to fold into lamellae before the temperature drops below $T_g$ and the segments freeze (Slide 28): a faster cooling gives smaller crystals (Slide 26), and the chains that have not crystallized stay as an amorphous, isotropic tangle. That the fast cooling also lowers the degree of crystallinity is the author's reading of Slides 26 and 28 (the slides state the effect on the crystal size).

### 3. Comparison
| | Rolling | Fast-cooled casting |
| :--- | :--- | :--- |
| Chain orientation | aligned (anisotropic) | random (isotropic) |
| Interaction between chains | more effective | less effective |
| Crystallinity | kept or increased by alignment | reduced by the fast cooling |
| Strength | higher | lower |

**Answer: the polymer produced by rolling.**

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Direction.** The gain in strength is in the direction of the orientation. Crystallization and orientation raise the anisotropy [Session 19 Slides 23-24], so a rolled sheet is strongest along the rolling direction; in the transverse direction the gain is smaller (extension).
- **Limit of the deformation.** Orientation can only be pushed until no further chain alignment is possible; then the polymer fractures [Session 19 Slide 40]. Rolling is therefore applied with a moderate reduction, not to failure.
- **Same mechanism in fibres.** Fibres are made with linear, oriented, crystalline chains and are the strongest form of a polymer [Session 20 Slide 16], which confirms the role of orientation.

### Interpretation
In metals cold work raises the strength by multiplying dislocations; in a thermoplastic the deformation raises it by aligning the chains. The cast and quenched polymer is the opposite case: its chains are frozen as a disordered tangle, with the least effective interaction between them. Drawing and rolling are the reason why stretched films and fibres are much stronger than moulded blocks of the same polymer.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Stronger route | polymer produced by rolling | rolling | agrees; chain orientation, Session 19 Slides 39 and 43 |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
* [[Concept - Strain Hardening and Percent Cold Work|Strain hardening in metals]]
