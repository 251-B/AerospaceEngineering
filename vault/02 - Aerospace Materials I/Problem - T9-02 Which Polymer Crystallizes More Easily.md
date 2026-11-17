---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 2"
dificultad: easy
badge: "Crystallinity · branching, copolymers, tacticity"
tags:
  - official-problem
  - solved
  - crystallinity
  - tacticity
  - copolymer
  - branching
---

# ✏️ Problem: T9-02 — Which Polymer of Each Pair Crystallizes More Easily

## 📄 Official Statement
> 2. Describe for each of the following polymer pairs, which one is more likely to crystallize? Explain your answer.
> a) Branched Polyethylene vs linear polyethylene.
> b) Polyethylene vs polyethylene-polypropylene co-polymer.
> c) Isotactic Polypropylene vs Atactic polypropylene.
>
> *(Solution: a) Liner PE, b) PE, c) Isostatic PP)*

The key prints "Liner" and "Isostatic"; they mean linear and isotactic.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **What crystallinity needs.** The crystallinity of a polymer is the degree to which there are regions where the chains are aligned with one another [Session 19 Slide 23]; in the crystalline lamellae the chains fold back and forth in an ordered way [Session 19 Slide 25]. A chain crystallizes easily when it is **regular** along its length, so that neighbouring segments fit next to each other.
2. **Factors of the slides.** Linear polymers pack best and are the most crystalline, branched ones less; symmetric and simple monomers favour crystallinity, complex ones lower it; random and graft copolymers are amorphous and alternating and block copolymers have some crystallinity; atactic polymers are amorphous, isotactic and syndiotactic ones probably crystalline [Session 19 Slides 26-27].
3. **Same conditions.** Within each pair the cooling rate and the molecular weight are taken as equal, so only the structure of the chain decides.

### Data
| Pair | Structural difference |
| :--- | :--- |
| a) | branched against linear chain of the same polymer |
| b) | homopolymer against copolymer with a second monomer |
| c) | regular (isotactic) against random (atactic) side groups |

**Unknown:** in each pair, the polymer that is more likely to crystallize, and why.

---

## 🧠 2. Model and Strategy

Each pair differs in only one structural feature, so each answer follows from one of the factors of Slides 26 and 27: the molecular structure (a), the copolymer sequence and the simplicity of the monomer (b), and the tacticity (c).

![[attachments/T9/s19-molecular-structure-types.png]]

**Strategy.** For each pair, name the feature, say how it changes the regularity of the chain, and apply the rule of the slides.

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Branched polyethylene against linear polyethylene [Session 19 Slides 22, 26-27]
The branches are side chains that stick out of the backbone at irregular places. They keep the backbones apart and prevent them from lying side by side in the folded lamellae, so the packing is poorer. Slide 26 states that linear polymers have a higher amount of packing and a higher degree of crystallinity, and branched polymers a lower one; the table of Slide 27 gives "most probable" for linear and "sometimes" for branched.

**Answer: linear polyethylene.**

### 2. b) Polyethylene against a polyethylene-polypropylene copolymer [Session 19 Slides 20, 27]
Polyethylene, $\mathrm{-[CH_2{-}CH_2]_n-}$, is the example of a symmetric and simple monomer ("Simple, YES" on Slide 27): every unit is the same and the chain is perfectly regular. In the copolymer, propylene units with a $\mathrm{CH_3}$ side group are inserted among the ethylene units. The statement does not say the type of copolymer; for a random sequence (the usual one) the $\mathrm{CH_3}$ groups appear at random places and the chain is irregular, so the copolymer is amorphous (Slide 27: random and graft copolymers are amorphous). Even an alternating or block copolymer has only "some crystallinity" according to the same slide, less than the regular homopolymer.

**Answer: polyethylene.**

### 3. c) Isotactic polypropylene against atactic polypropylene [Session 19 Slides 18-19, 26]
In polypropylene, $\mathrm{-[CH_2{-}CH(CH_3)]_n-}$, the $\mathrm{CH_3}$ groups can be all on the same side (isotactic), alternating (syndiotactic) or at random (atactic) [Session 19 Slide 18]. The isotactic chain repeats the same arrangement all along, so its segments fit together; the atactic chain has no pattern and cannot pack. Slide 26 states that atactic polymers are amorphous and isotactic or syndiotactic ones are probably crystalline, and Slide 19 adds that atactic polypropylene is a wax-type material with very bad mechanical properties.

**Answer: isotactic polypropylene.**

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **One rule behind the three answers.** In every pair the polymer chosen is the more regular one: no branches, one kind of unit, one arrangement of the side groups. Regularity is what lets chains fold into lamellae.
- **Consistency with the density.** The crystalline polymer is denser than the amorphous one [Session 19 Slide 24], so in each pair the chosen polymer would show the higher density for the same cooling, which is how the difference would be measured (the formula of Slide 25).
- **Limit cases.** A crosslinked polymer is the extreme of irregular packing: "almost never" crystalline [Session 19 Slide 27]. At the other extreme, a linear, isotactic homopolymer of a simple monomer is the most likely to crystallize.

### Interpretation
Crystallinity is a question of geometry: chains crystallize when they can lie parallel and close together. Branches, foreign units and random side groups all break that order. The practical consequence is that the more crystalline member of each pair is also the denser, stiffer and stronger one with the higher melting temperature [Session 19 Slides 27, 43], which is why linear high-density polyethylene and isotactic polypropylene are the grades used for structural plastic parts.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) | linear PE (printed "Liner PE") | linear PE | agrees |
| b) | PE | PE | agrees |
| c) | isotactic PP (printed "Isostatic PP") | isotactic PP | agrees |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
