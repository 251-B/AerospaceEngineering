---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 4"
dificultad: medium
badge: "Melting temperature · crystallinity, polarity, tacticity"
tags:
  - official-problem
  - solved
  - melting-temperature
  - crystallinity
  - tacticity
  - molecular-weight
---

# ✏️ Problem: T9-04 — Which Polymer of Each Pair Has the Higher Melting Temperature

## 📄 Official Statement
> 4. Which of the following polymer pairs has higher melting temperature? Why?
> a) Branched PE with <Mn> = 850 000 g/mol; Linear PE with <Mn> = 850 000 g/mol
> b) PTFE with density equal to 2.14 g/cm³ and <Mw> = 600 000 g/mol; PTFE with density equal to 2.20 g/cm³ and <Mw> = 600 000 g/mol.
> c) Syndiotactic PVC with <Mn> = 500 000 g/mol; Linear PE with <Mn> = 225 000 g/mol.
> d) Linear and syndiotactic PP with <Mw> = 750 000 g/mol; Atactic and linear PP with <Mw> = 500 000 g/mol.
>
> *(Solution: a) Linear PE > Branched PE; b) PTFE 2.20 > PTFE 2.14; c) PVC > PE; d) Syndiotactic PP > Atactic PP)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Where $T_m$ comes from.** $T_m$ is the transition of the **crystalline** regions [Session 19 Slide 28]: it is the temperature at which the ordered, folded chains of the lamellae come apart. A polymer with no crystalline regions has no melting temperature, only a glass transition [Session 19 Slide 23].
2. **Factors that raise $T_m$.** More crystallinity raises $T_m$ [Session 19 Slide 27]; $T_m$ rises with the molecular weight and levels off for long chains [Session 19 Slide 30]; polar groups increase the intermolecular forces [Session 19 Slide 43] and the ordering [Session 19 Slide 27].
3. **Crystallinity and structure.** Linear and regular (isotactic or syndiotactic) chains crystallize, branched chains less, atactic chains not at all [Session 19 Slides 26-27]; the crystalline polymer is denser than the amorphous one [Session 19 Slide 24].
4. **Reference values.** Melting points printed on Session 20 Slide 8: polyethylene 110 – 137 °C, polyvinyl chloride about 204 °C, polypropylene 165 – 177 °C.

### Data
| Pair | Same in both | Different |
| :--- | :--- | :--- |
| a) PE | $M_n = 850\,000$ g/mol | branched against linear |
| b) PTFE | $M_w = 600\,000$ g/mol | density 2.14 against 2.20 g/cm³ |
| c) | (different polymers) | syndiotactic PVC, $M_n = 500\,000$ g/mol, against linear PE, $M_n = 225\,000$ g/mol |
| d) PP | linear | syndiotactic, $M_w = 750\,000$ g/mol, against atactic, $M_w = 500\,000$ g/mol |

**Unknown:** in each pair, the polymer with the higher $T_m$, and why.

---

## 🧠 2. Model and Strategy

In each pair, find which polymer has more (or better) crystalline regions and stronger forces between its chains: that one needs more thermal energy to break up its crystals. The molecular weight acts in the same direction when it differs, but all the weights here are far above the range where Slide 30 shows a strong effect.

![[attachments/T9/s19-mw-tg-regimes.png]]

**Strategy.** For each pair: identify the controlling factor, apply the rule of the slides, and compare with the printed melting points where they exist.

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Branched PE against linear PE, same $M_n$
The molecular weights are equal, so only the structure differs. The branches keep the chains from packing, so the branched PE has a lower degree of crystallinity and less perfect crystals [Session 19 Slides 26-27]; more crystallinity means a higher $T_m$ [Session 19 Slide 27].

**Answer: the linear PE.** (The range 110 – 137 °C printed for polyethylene on Session 20 Slide 8 covers both kinds; that the low end belongs to the branched, low-density PE and the high end to the linear, high-density PE is an extension.)

### 2. b) PTFE of density 2.14 against 2.20 g/cm³, same $M_w$
Same polymer and same molecular weight, so the density measures the crystallinity: the crystalline regions are denser than the amorphous ones [Session 19 Slide 24], and by the formula of Slide 25 the degree of crystallinity grows with the actual density $\rho_s$ for fixed $\rho_c$ and $\rho_a$:

$$X_c = \frac{\rho_c(\rho_s - \rho_a)}{\rho_s(\rho_c - \rho_a)} \qquad \frac{dX_c}{d\rho_s} = \frac{\rho_c\,\rho_a}{\rho_s^{2}(\rho_c - \rho_a)} > 0$$

(the derivative, by the quotient rule on $(\rho_s - \rho_a)/\rho_s = 1 - \rho_a/\rho_s$, is an extension). The denser PTFE is more crystalline and therefore has the higher $T_m$ [Session 19 Slide 27].

**Answer: the PTFE of density 2.20 g/cm³.**

### 3. c) Syndiotactic PVC against linear PE
Three factors point the same way:
- **Polarity.** PVC carries a polar C-Cl bond in every unit, $\mathrm{-[CH_2{-}CHCl]_n-}$; polar groups increase the intermolecular forces [Session 19 Slide 43] and the ordering [Session 19 Slide 27], so more energy is needed to separate the chains. PE has only C-H bonds and van der Waals forces.
- **Regularity.** The PVC is syndiotactic, so it can crystallize [Session 19 Slide 26].
- **Molecular weight.** $500\,000 > 225\,000$ g/mol, and $T_m$ rises with $M$ [Session 19 Slide 30], although at these weights the effect is small.

The printed melting points confirm it: about 204 °C for PVC against 110 – 137 °C for PE [Session 20 Slide 8]. The same side group raises $T_g$ from $-110$ °C (HDPE) to 87 °C (PVC) [Session 19 Slide 29].

**Answer: the syndiotactic PVC.**

### 4. d) Linear syndiotactic PP against linear atactic PP
The syndiotactic chain has its $\mathrm{CH_3}$ groups in a regular alternating pattern and can crystallize; the atactic chain has them at random and is amorphous [Session 19 Slides 18, 26]. An amorphous polymer has no crystalline regions, so it has no true melting temperature, only $T_g$ [Session 19 Slides 23, 28]: Slide 19 describes atactic PP as a wax-type material. The higher molecular weight of the syndiotactic PP (750 000 against 500 000 g/mol) adds in the same direction [Session 19 Slide 30].

**Answer: the syndiotactic PP.**

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units of the derivative in b).** $[\rho_c\rho_a/(\rho_s^2(\rho_c - \rho_a))] = (\text{g/cm}^3)^2/(\text{g/cm}^3)^3 = \text{cm}^3/\text{g}$, so $dX_c = (\text{cm}^3/\text{g})\,d\rho_s$ is dimensionless, as a fraction must be.
- **Molecular weight.** In pairs a) and b) the weights are equal, so they cannot be the reason; in c) and d) the weight differs but in the same direction as the structural factor, so the answers do not depend on how large its effect is.
- **Limit.** A fully amorphous polymer ($X_c = 0$, case of the atactic PP) has no $T_m$ at all; its stiffness falls at $T_g$ and it softens progressively [Session 19 Slide 45].

### Interpretation
The melting temperature measures how well the chains are packed in crystals and how strongly they attract each other. Linear, regular, polar chains pack well and attract each other strongly; branched, random or non-polar chains do not. This is why the polymers chosen for parts that must work hot are the linear, regular and polar ones, such as the engineering thermoplastics of Session 20 Slide 9 (nylon 6,6, polycarbonate, polysulfone, with melting points of 250 to 315 °C).

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) | linear PE > branched PE | linear PE | agrees |
| b) | PTFE 2.20 > PTFE 2.14 | PTFE 2.20 g/cm³ | agrees |
| c) | PVC > PE | syndiotactic PVC | agrees; about 204 °C against 110 – 137 °C on Session 20 Slide 8 |
| d) | syndiotactic PP > atactic PP | syndiotactic PP | agrees |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
* [[Problem - T9-02 Which Polymer Crystallizes More Easily|Problem T9-02]]
