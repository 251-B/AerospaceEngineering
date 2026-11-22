---
materia: Aerospace Materials I
tema: "Unit 7: magnetic domains, Bloch walls, soft vs. hard hysteresis loops and permanent-magnet selection"
bank_id: B59
title: "Domains, hysteresis and the selection of magnetic materials"
category: mt2_test_block
unit: 7
concepts:
  - u7-magnet-selection-criteria
  - u7-domains-bloch-walls-origin
  - u7-bloch-wall-mobility
  - u7-soft-hard-comparison
  - u7-magnetization-saturation-mechanism
  - u7-hysteresis-irreversibility
  - u7-ferrimagnetic-ceramics-domains
  - u7-magnetization-curve-sequence
  - u7-loop-area-energy-loss
  - u7-rectangular-loop-materials
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including Q7 of the January 2016 final exam. Content and data from Session 15, Slides 11-24."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B59 — Domains, hysteresis and the selection of magnetic materials

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including an official permanent-magnet selection question from the January 2016 final exam (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 11-24.

## Q59.1 Permanent magnet selection for high field and temperature

- id: B59-Q1
- concept_id: u7-magnet-selection-criteria
- format: diagram-reading
- asks: application
- origin: official-exam

Select the most adequate material from the table to manufacture a permanent magnet for a magnetic energy storage application able to work at magnetic fields above 600 Oersted and a temperature of 500 °C:

| Material | Curie temperature (°C) | Remanence (Gauss) | $H_c$ (Oersted) | $(BH)_{\max}$ (Gauss·Oersted) |
| :--- | ---: | ---: | ---: | ---: |
| Co₅Sm | 725 | 9 500 | 9 500 | 25 000 000 |
| Alnico 1 | 780 | 7 100 | 440 | 1 400 000 |
| Alnico 5 | 900 | 13 100 | 640 | 6 000 000 |
| Nanoperm | 475 | 14 500 | 10 200 | 32 000 000 |

a) Nanoperm
b) Co₅Sm
c) Alnico 5
d) Alnico 1

### Answer

b

### Explanation

January 2016 ordinary final exam, Q7 (and Session 15, Slides 18-19 and 23-24): at 500 °C, any candidate must have $T_c > 500$ °C to remain ferromagnetic (ruling out Nanoperm at 475 °C). To withstand fields above 600 Oe, coercivity must satisfy $H_c > 600$ Oe (ruling out Alnico 1 at 440 Oe). Between Alnico 5 and Co₅Sm, Co₅Sm provides both far greater coercivity margin (9 500 Oe vs 640 Oe) and over four times the maximum energy product $(BH)_{\max}$ (25 000 000 vs 6 000 000 G·Oe) for energy storage.

- a) Fails the temperature requirement: Nanoperm has the highest $(BH)_{\max}$ and $H_c$ in the table, but $T_c = 475\,^\circ\text{C} < 500\,^\circ\text{C}$, so it is paramagnetic at the service temperature.
- c) Meets $T_c$ and barely meets $H_c > 600$ Oe, yet stores more than four times less magnetic energy per unit volume than Co₅Sm ($6\times10^6$ vs $25\times10^6$ G·Oe).
- d) Fails the coercivity requirement: its $H_c = 440$ Oe is below the 600 Oe working field, so it would demagnetize.

### Source

MATERIALS_FINALEXAM_2016_ORD_SOL.pdf, p. 4 Q7; Session 15, Slides 18-19 and 23-24.

## Q59.2 Magnetic domains and Bloch walls

- id: B59-Q2
- concept_id: u7-domains-bloch-walls-origin
- format: topic-true
- asks: cause

Referring to magnetic domains and Bloch walls in ferromagnetic materials, which one of the following statements is TRUE:

a) A single large domain minimizes magnetostatic energy by pushing all magnetic flux lines into the surrounding air
b) Magnetic domains are typically larger than the metal grains, so every crystal grain belongs to a single domain
c) Across a Bloch wall, dipole directions flip abruptly across one atomic plane rather than changing progressively
d) Magnetic domains form spontaneously to reduce magnetostatic energy, separated by gradual ~100 nm Bloch walls

### Answer

d

### Explanation

Session 15, Slides 14-15: magnetic domains form spontaneously so that internal flux closure decreases the external stray field and lowers magnetostatic energy. Adjacent domains are separated by Bloch walls roughly 100 nm (~300 atoms) wide across which dipole orientation turns gradually.

- a) Inverts the magnetostatic energy trend: a single-domain crystal has the largest external stray field and highest magnetostatic energy (Slide 15).
- b) Inverts the size comparison: domains (10–100 µm) are typically smaller than grains, so one large grain holds several domains (Slide 14).
- c) Wrong wall structure: the magnetization turns gradually over ~300 atomic layers across a Bloch wall, not in a single sharp plane (Slide 14).

### Source

Session 15, Slides 14-15.

## Q59.3 Bloch wall mobility, coercivity and permeability

- id: B59-Q3
- concept_id: u7-bloch-wall-mobility
- format: cause-effect
- asks: cause

With an increase in the ease of motion of Bloch walls inside a ferromagnetic material, its coercivity $H_c$ and initial permeability $\mu_i$:

a) $H_c$ decreases and $\mu_i$ increases, producing a narrower hysteresis loop
b) $H_c$ increases and $\mu_i$ decreases, producing a wider hysteresis loop
c) both $H_c$ and $\mu_i$ decrease, shrinking the saturation magnetization $M_s$
d) both $H_c$ and $\mu_i$ increase, raising hysteresis energy losses per cycle

### Answer

a

### Explanation

Session 15, Slides 18 and 21: when Bloch walls move easily, small fields realign domains rapidly (high initial permeability $\mu_i$) and little reverse field is needed to demagnetize the material (low coercivity $H_c$), giving a narrow soft-magnet loop.

- b) Describes the opposite case where obstacles pin the Bloch walls, making them hard to move.
- c) Links easier wall motion to lower permeability and wrongly claims it alters composition-fixed $M_s$.
- d) Contradicts coercivity behaviour: walls that move more easily never require a larger reverse field $H_c$.

### Source

Session 15, Slides 18 and 21.

## Q59.4 Soft and hard ferromagnetic classes

- id: B59-Q4
- concept_id: u7-soft-hard-comparison
- format: topic-false
- asks: comparison

Regarding soft and hard ferromagnetic materials, which one of the following statements is FALSE:

a) Soft magnetic materials have easily moved Bloch walls and low coercivity ($H_c < 10\,000$ A/m)
b) Hard magnetic materials show wide hysteresis loops with high resistance to demagnetization ($H_c > 10\,000$ A/m)
c) Soft magnetic materials require high coercivity ($H_c > 10\,000$ A/m) to minimize losses in alternating fields
d) Hard magnetic materials are chosen for permanent magnets, whereas soft ones are used in transformer and motor cores

### Answer

c

### Explanation

Session 15, Slides 18-19: materials working under alternating fields (transformer, motor, and generator cores) must be soft magnetic materials with *low* coercivity ($H_c < 10\,000$ A/m) and narrow loops so that energy losses per cycle are minimized. Statement c is false.

- a) True: Slide 18 defines soft magnetic materials by easy Bloch-wall motion and $H_c < 10\,000$ A/m.
- b) True: Slide 18 defines hard magnetic materials by $H_c > 10\,000$ A/m and high resistance to demagnetization.
- d) True: Slide 19 matches hard magnets with permanent magnets and soft magnets with cores under alternating fields.

### Source

Session 15, Slides 18-19.

## Q59.5 Domain evolution from demagnetized state to saturation

- id: B59-Q5
- concept_id: u7-magnetization-saturation-mechanism
- format: what-happens
- asks: effect

As the external magnetic field $H$ applied to a demagnetized ferromagnet increases steadily from zero up to saturation, what happens to its magnetic domains?

a) All domains rotate instantaneously into alignment at tiny fields and then shrink as $H$ rises
b) Unfavourable domains expand first to lower the internal energy, followed by thermal randomization
c) Domain walls stay completely fixed while individual atomic moments flip straight to saturation at $H_c$
d) Favourable domains first grow at the expense of unfavourable ones, and remaining domains then rotate into alignment

### Answer

d

### Explanation

Session 15, Slide 16: starting from random domains, the magnetization rises slowly at first, grows rapidly as favourably oriented domains expand at the expense of unfavourable ones by Bloch-wall motion, and finally slows as the remaining domains rotate into the field direction at saturation.

- a) Reverses and distorts the stages: domain growth comes before domain rotation, and domains do not shrink after aligning.
- b) Inverts which domains grow: domains aligned closely with $H$ grow, while unfavourably oriented domains shrink.
- c) Ignores domain-wall motion, which is the main mechanism driving the steep intermediate rise of the initial curve.

### Source

Session 15, Slide 16.

## Q59.6 Origin of remanence on unloading the magnetic field

- id: B59-Q6
- concept_id: u7-hysteresis-irreversibility
- format: complete-sentence
- asks: cause

When a ferromagnetic specimen is driven to saturation and the applied field $H$ is then returned to zero, the induction does not return to zero because:

a) induced diamagnetic currents preserve the full saturation induction indefinitely
b) the magnetic domains do not spontaneously revert to their initial random arrangement
c) the Curie temperature drops below room temperature during magnetization
d) the Bloch walls vanish permanently once saturation is reached

### Answer

b

### Explanation

Session 15, Slide 17: reducing $H$ back to zero leaves part of the domain alignment locked in rather than returning to the original random distribution, producing the remanence $B_r$.

- a) Diamagnetism produces weak opposition while a field acts, not permanent remanent induction.
- c) Magnetizing a specimen does not shift its Curie temperature below room temperature.
- d) Domain walls re-nucleate as the field drops and reverse, which is how a reverse field $-H_c$ demagnetizes the specimen.

### Source

Session 15, Slide 17.

## Q59.7 Ferrimagnetic ceramics compared with ferromagnetic metals

- id: B59-Q7
- concept_id: u7-ferrimagnetic-ceramics-domains
- format: topic-true
- asks: classification

Regarding ferrimagnetic ceramics (such as ferrites) compared with ferromagnetic metals, which one of the following statements is TRUE:

a) Ferrites form domains and hysteresis loops with high susceptibility, while remaining ceramic oxides with unequal antiparallel moments
b) Ferrites lack magnetic domains and behave like linear diamagnets with negative susceptibility
c) Ferrites are metallic alloys whose antiparallel moments are equal and cancel to zero net magnetization
d) Ferrites have no Curie temperature and retain their spontaneous magnetization at arbitrarily high temperatures

### Answer

a

### Explanation

Session 15, Slides 5, 11, 14 and 23: ferrites and garnets are ferrimagnetic ceramics whose unequal antiparallel ionic moments yield a large net magnetization ($\chi_m$ up to $10^6$), domain structures, and hysteresis loops, while remaining ceramic oxides rather than pure metals.

- b) Confuses ferrimagnetism with diamagnetism: ferrites have $\mu_r \gg 1$ and clear hysteresis loops (Slide 24 lists MnZn and NiZn ferrites).
- c) Confuses ferrimagnetic ceramics with antiferromagnetic metals/oxides: equal antiparallel moments give zero net moment, and ferrites are ceramics.
- d) False: Slide 23 explicitly states that above $T_c$, both ferromagnetic and ferrimagnetic materials (including $\text{Fe}_3\text{O}_4$) become paramagnetic.

### Source

Session 15, Slides 5, 11, 14, 23 and 24.

## Q59.8 Order of the stages of magnetization

- id: B59-Q8
- concept_id: u7-magnetization-curve-sequence
- format: ordering
- asks: application

When a field is applied to a demagnetized ferromagnet and increased up to saturation, the stages follow, in order:

a) random domains, rotation of domains, growth of favourable domains, saturation
b) growth of favourable domains, random domains, rotation of domains, saturation
c) random domains, growth of favourable domains, rotation of domains, saturation
d) random domains, growth of favourable domains, saturation, rotation of domains

### Answer

c

### Explanation

Slide 16: the domains start randomly distributed; the favourable domains grow at the expense of the unfavourable ones (fast rise); later the magnetization slows because the domains must rotate; finally all dipoles are aligned, which is saturation.

- a) Growth and rotation are swapped: rotation is the last, slow stage, since domain walls move before dipoles turn.
- b) The sequence starts with growth: the demagnetized state, with random domains, comes first.
- d) Saturation placed before rotation: saturation is reached only when the rotation has aligned all the dipoles.

### Source

Session 15, Slide 16.

## Q59.9 Energy lost per cycle in a soft core

- id: B59-Q9
- concept_id: u7-loop-area-energy-loss
- format: cause-effect
- asks: cause

A soft magnetic core in an alternating field dissipates little energy per cycle because:

a) its Bloch walls are difficult to move, so it keeps a high remanence
b) its Bloch walls move easily, so its loop encloses a small area
c) its domains are larger than its grains, so its loop encloses a small area
d) its initial permeability is low, so its loop is narrow

### Answer

b

### Explanation

Slides 18-19: in soft materials the Bloch walls are easy to move, so the coercivity is low and the loop is narrow; they are used under alternating fields to minimize energy losses. The energy lost per cycle is proportional to the area of the loop (extension: not written on the slides).

- a) Describes a hard material (walls difficult to move, high remanence), which has a wide loop and large losses.
- c) Wrong cause: domains are usually smaller than the grains (Slide 14), and their size does not set the area of the loop.
- d) Inverted trend: soft materials have a high initial permeability (Slide 18), and a low one belongs to hard materials.

### Source

Session 15, Slides 18-19.

## Q59.10 Material of a rectangular hysteresis loop

- id: B59-Q10
- concept_id: u7-rectangular-loop-materials
- format: identify
- asks: application

How is a material with a rectangular hysteresis cycle produced, and where is it used?

a) a soft magnet heat-treated in a magnetic field, used in magnetic memories
b) a hard magnet quenched from high temperature, used in permanent magnets
c) a soft magnet annealed without field, used in cores of transformers
d) a hard magnet of high remanence, used in cores of electric motors

### Answer

a

### Explanation

Slide 19: rectangular-cycle materials are soft magnetic materials modified by a thermal treatment in the presence of a magnetic field, with low remanence, low saturation magnetization and low coercive field; they serve for magnetic memories, magnetic amplifiers and pulse transformers (data storage).

- b) Hard magnets with wide loops make permanent magnets, not rectangular-cycle memories.
- c) Transformer cores use ordinary soft materials; the rectangular cycle needs the treatment in the field.
- d) Motor cores need soft materials under alternating fields; a high remanence belongs to permanent magnets.

### Source

Session 15, Slide 19.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
