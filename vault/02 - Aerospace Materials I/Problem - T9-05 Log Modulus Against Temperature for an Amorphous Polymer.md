---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 5"
dificultad: medium
badge: "log E against T · molecular weight, crosslinking, crystallinity"
tags:
  - official-problem
  - solved
  - modulus-temperature
  - glass-transition
  - crosslinking
  - crystallinity
---

# ✏️ Problem: T9-05 — Logarithm of Young's Modulus Against Temperature for an Amorphous Polymer

## 📄 Official Statement
> 5. Draw three representations of the logarithm of the Young's modulus versus temperature for an amorphous polymer.
> a) In one of those show how the behavior changes when the molecular weight increases.
> b) In another diagram, show the behavior changes when crosslinking increases.
> c) If this polymer is processed so that it has some crystallinity, show how the Young's modulus changes with temperature.

The sheet prints no solution for this problem.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **The base curve.** An amorphous polymer has only a glass transition [Session 19 Slide 23]. Its modulus (measured, for example, as the relaxation modulus $E_r(10)$ at 10 s) goes through five regions as the temperature rises: **glassy**, about $10^3$ MPa, below $T_g$; **leathery**, the steep drop of about three decades around $T_g$; **rubbery**, a plateau; **rubbery flow**; and **viscous flow** (liquid) [Session 19 Slide 49].
2. **Log scale.** The modulus changes by several orders of magnitude, so it is plotted as $\log E$; the drop at $T_g$ is then a step and the plateaus are horizontal lines [Session 19 Slides 45-46].
3. **What changes each curve.** Higher molecular weight means more entanglements [Session 19 Slide 43]; crosslinks are covalent bonds between chains [Session 19 Slide 22]; crystalline regions melt only at $T_m$ [Session 19 Slide 28].
4. **Sketches.** The statement asks for qualitative drawings; the figures of the slides are used as the drawings, and no numbers are needed.

### Data
| Diagram | Parameter that changes |
| :--- | :--- |
| a) | molecular weight (entanglement density) |
| b) | degree of crosslinking |
| c) | degree of crystallinity |

**Unknown:** the three diagrams of $\log E$ against $T$ and the explanation of each change.

---

## 🧠 2. Model and Strategy

The modulus of a polymer is high when the chain segments cannot move (glass) and low when they can (rubber, liquid). Each structural change of the statement adds a different kind of obstacle to that motion above $T_g$, so each one acts on a different part of the base curve.

![[attachments/T9/s19-relaxation-modulus-vs-temperature.png]]

**Strategy.**
1. Draw the base curve of the amorphous polymer and name its regions.
2. For each case, say which region changes, in which direction and why, and give the diagram of the slides.

---

## 🔢 3. Step-by-Step Derivation

### 1. Base curve of the amorphous polymer [Session 19 Slide 49]
Below $T_g$ the segments are frozen and the modulus is high and nearly flat (glassy region). At $T_g$ the segments of the amorphous regions start to move [Session 19 Slide 28] and the modulus drops by about three orders of magnitude (leathery region). Above it the entanglements hold the chains together for a while, which gives the rubbery plateau; at higher temperatures whole chains slide past each other (rubbery flow) and finally the polymer flows as a viscous liquid.

### 2. a) Increasing molecular weight [Session 19 Slides 30, 43, 45]
The glassy region and the position of the drop hardly change ($T_g$ rises only slightly with $M$ and levels off for long chains, Slide 30). The change is **above $T_g$**: longer chains have more entanglements (Slide 43), which act as temporary links, so the rubbery plateau is **longer** and the flow region moves to **higher temperatures**. The slide draws it as curves that stay higher and fall later for higher entanglement density and increasing molecular weight.

![[attachments/T9/s19-stiffness-vs-entanglement.png]]

### 3. b) Increasing crosslinking [Session 19 Slides 46, 49]
Crosslinks are permanent covalent bonds, so the chains can never slide past each other: the **flow regions disappear**, and the plateau above $T_g$ stays up to the temperature at which the polymer degrades. The more crosslinks, the **higher the plateau** and the **smaller the drop** at $T_g$; with heavy crosslinking (a thermoset) the modulus hardly falls at all and $T_g$ moves up. Slide 46 draws no, slight, increasing and heavy crosslinking; curve B of Slide 49 (lightly crosslinked atactic polystyrene) shows the flat rubbery plateau with no flow.

![[attachments/T9/s19-crosslinking-modulus.png]]

### 4. c) Some crystallinity [Session 19 Slides 45, 49]
The crystalline regions do not take part in the glass transition; they stay rigid up to $T_m$ and hold the amorphous regions between them [Session 19 Slide 28]. Therefore:
- the drop at $T_g$ is **smaller**, because only the amorphous fraction softens;
- above $T_g$ the modulus stays on a **high plateau** (leathery and tough) up to $T_m$;
- at $T_m$ the crystals melt and the modulus falls to the flow region.

The more crystalline the polymer, the smaller the drop at $T_g$; a 100 % crystalline polymer has no drop at $T_g$ and falls only at $T_m$. Slide 45 draws the 100 % amorphous, 50 % / 50 % and 100 % crystalline curves, and curve A of Slide 49 (crystalline isotactic polystyrene) shows a polymer that stays stiff up to its melting point.

![[attachments/T9/s19-modulus-vs-temperature-crystallinity.png]]

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Order of magnitude.** On the log scale the glassy modulus of polystyrene is about $10^3$ MPa, about 1 GPa, inside the range 0.007 – 4 GPa of polymers [Session 19 Slides 32, 49]. The plateau is about three decades lower, about 1 MPa, the modulus of a rubber.
- **Limit cases.** No crosslinks and no crystals: the base curve, which flows. Infinite crosslinking: a rigid network with no drop. 100 % crystallinity: no glass transition, one drop at $T_m$. The three diagrams go continuously from the base curve to these limits.
- **Time and rate.** The modulus is measured at a fixed time; at a higher strain rate the whole curve moves to higher temperatures, because a higher rate has the same effect as a lower temperature [Session 19 Slide 48].

### Interpretation
The three changes act on different parts of the curve: the molecular weight only delays the flow, the crosslinks remove the flow and lift the plateau, and the crystallinity props the modulus up between $T_g$ and $T_m$. In use this decides the working temperature: an amorphous thermoplastic must work below $T_g$, a semicrystalline one can work up to near $T_m$, an elastomer works on its rubbery plateau and a thermoset keeps its stiffness until it degrades.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) Molecular weight | not printed on the sheet | longer rubbery plateau, flow at higher $T$ | consistent with Session 19 Slides 30, 43 and 45 |
| b) Crosslinking | not printed on the sheet | higher plateau, smaller drop, no flow | consistent with Session 19 Slides 46 and 49 |
| c) Crystallinity | not printed on the sheet | smaller drop at $T_g$, plateau up to $T_m$ | consistent with Session 19 Slides 45 and 49 |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
* [[Problem - T9-06 Degree of Crystallinity of Polypropylene from Its Density|Problem T9-06]]
