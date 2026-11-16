---
materia: Aerospace Materials I
tema: "Unit 6: band structure of metals, Ohm's law, drift velocity, mobility and the origin of resistivity"
bank_id: B34
title: "Metallic conduction, drift velocity and mobility"
category: mt2_test_block
unit: 6
concepts:
  - u6-conductor-band-structure
  - u6-band-gap-classification
  - u6-resistivity-measurement
  - u6-drift-velocity-mobility
  - u6-collisions-origin-resistivity
  - u6-resistance-geometry
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 6-13 and 31."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B34 — Metallic conduction, drift velocity and mobility

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 6-13 and 31.

## Q34.1 Band picture of magnesium

- id: B34-Q1
- concept_id: u6-conductor-band-structure
- format: choose-figure
- asks: figure-reading

Which picture describes the electron band structure of magnesium ($1s^2\,2s^2\,2p^6\,3s^2$)?

a) ![[attachments/MAT-MT2/u6-solid-p.svg]]
b) ![[attachments/MAT-MT2/u6-solid-q.svg]]
c) ![[attachments/MAT-MT2/u6-solid-r.svg]]
d) ![[attachments/MAT-MT2/u6-solid-s.svg]]

### Answer

b

### Explanation

Session 13, Slide 6, case A2: in Mg the filled 3s band overlaps the empty 3p band, so the two bands together are only partly filled and Mg conducts. Picture B shows a filled band overlapping an empty band.

- a) A full valence band with a gap of 0.67 eV is a semiconductor (pure germanium, Slide 8), not a metal.
- c) The half-filled valence band is case A1 of the slide, for metals with one $s$ electron (Na, Cu, Al); Mg has two 3s electrons.
- d) A gap of 7 eV is an insulator such as diamond (Slide 8).

### Source

Session 13, Slides 6 and 8.

## Q34.2 Classification of germanium

- id: B34-Q2
- concept_id: u6-band-gap-classification
- format: complete-sentence
- asks: application

Pure germanium, with a band gap $E_g = 0.67$ eV, is classified as:

a) An insulator, because it has a band gap
b) A conductor, because its gap is below 1 eV
c) A semiconductor, because its valence band is half filled
d) A semiconductor, because its gap is below 2 eV

### Answer

d

### Explanation

Session 13, Slide 8: a semiconductor has a filled valence band separated from an empty conduction band by a narrow gap, $E_g < 2$ eV; pure germanium ($E_g = 0.67$ eV) is the slide's example.

- a) Having a gap does not make a solid an insulator; the limit is $E_g > 2$ eV.
- b) Any gap, however small, separates filled and empty states; a conductor has no gap above its filled states (Slide 6).
- c) Right class with the wrong reason: a half-filled valence band is the band structure of a conductor (Slide 6).

### Source

Session 13, Slides 6 and 8.

## Q34.3 Resistivity from a measured resistance

- id: B34-Q3
- concept_id: u6-resistivity-measurement
- format: numeric
- asks: calculation
- calc: 0.064*pi*(0.5e-3)**2/1.5

A wire 1.5 m long and 1.0 mm in diameter has a measured resistance of 0.064 Ω. Determine the electrical resistivity of its material:

a) $3.35\times10^{-8}$ Ω·m
b) $1.34\times10^{-7}$ Ω·m
c) $3.35\times10^{-2}$ Ω·m
d) $1.22\times10^{5}$ Ω·m

### Answer

a

### Explanation

$R = \rho\,l/A$ (Topic 6 note, Section 4, from $J = \sigma E$ and Session 13, Slide 10), so $\rho = R\,A/l$ with $A = \pi (0.5\times10^{-3})^2 = 7.85\times10^{-7}$ m²: $\rho = 0.064 \cdot 7.85\times10^{-7}/1.5 = 3.35\times10^{-8}$ Ω·m.

- b) The diameter was used as the radius: $A = \pi (1.0\times10^{-3})^2$ is four times too large, giving $1.34\times10^{-7}$ Ω·m.
- c) The area was left in mm² ($0.785$ mm²) instead of m², so the result is $10^{6}$ times too large.
- d) The formula was inverted, $\rho = R\,l/A = 0.064\cdot 1.5/7.85\times10^{-7} = 1.22\times10^{5}$.

### Source

Session 13, Slides 10 and 13 ($I = V/R$, $\rho = 1/\sigma$); Topic 6 note, Section 4 ($R = \rho l/A$).

## Q34.4 Drift velocity of electrons in silicon

- id: B34-Q4
- concept_id: u6-drift-velocity-mobility
- format: numeric
- asks: calculation
- calc: 0.135*500

Determine the drift velocity of the conduction electrons of silicon ($\mu_e = 0.135$ m²/(V·s), $\mu_h = 0.048$ m²/(V·s)) under a field of 500 V/m:

a) 24.0 m/s
b) 67.5 m/s
c) 91.5 m/s
d) 3700 m/s

### Answer

b

### Explanation

Session 13, Slide 11: $v_d = \mu E$; for the electrons $v_d = 0.135 \cdot 500 = 67.5$ m/s (mobility of Si from the table of Slide 31).

- a) The hole mobility was used: $0.048 \cdot 500 = 24.0$ m/s.
- c) Electron and hole mobilities were added: $(0.135 + 0.048)\cdot 500 = 91.5$ m/s; the sum belongs in the conductivity, not in the speed of one carrier.
- d) The field was divided by the mobility, $500/0.135 = 3.70\times10^{3}$ m/s, instead of multiplied.

### Source

Session 13, Slides 11 and 31.

## Q34.5 Relaxation time

- id: B34-Q5
- concept_id: u6-drift-velocity-mobility
- format: complete-sentence
- asks: definition

In the expression of the electron mobility, $\mu = \tau\,|q_e|/m_e$, the relaxation time $\tau$ is:

a) The time an electron needs to cross the whole conductor
b) The time an electron stays in the conduction band
c) The mean time between collisions of the electrons
d) The time the dipoles need to realign with the field

### Answer

c

### Explanation

Session 13, Slides 11-12: between collisions the electron velocity grows linearly with time and falls back at each collision; $\tau$, the relaxation time, is the mean time between collisions.

- a) The transit time depends on the length of the wire; $\tau$ is a property of the material that sets $v_d$.
- b) Confuses the free-electron model of metals with the excitation of carriers across the gap of a semiconductor.
- d) The realignment of dipoles belongs to dielectrics in alternating fields (loss factor, Slide 53).

### Source

Session 13, Slides 11-12 and 53.

## Q34.6 Relaxation time and mobility

- id: B34-Q6
- concept_id: u6-drift-velocity-mobility
- format: cause-effect
- asks: effect

With an increase in the relaxation time $\tau$ of the conduction electrons, the electron mobility of a metal:

a) Decreases, because the electrons collide more often
b) Increases, because the number of free electrons increases
c) Stays constant, because it depends only on the field
d) Increases, because $\mu$ is proportional to $\tau$

### Answer

d

### Explanation

Session 13, Slide 11: $\mu = \tau|q_e|/m_e$, so a longer time between collisions gives a proportionally larger mobility.

- a) Inverts the meaning of $\tau$: a longer relaxation time means fewer collisions per second, not more.
- b) Right trend with the wrong cause: the number of electrons $n$ is a separate factor of $\sigma = n|q_e|\mu$ and does not enter $\mu$.
- c) Confuses the mobility with the drift velocity: $v_d = \mu E$ depends on the field, while $\mu$ does not.

### Source

Session 13, Slides 11-13.

## Q34.7 Electrons without collisions

- id: B34-Q7
- concept_id: u6-collisions-origin-resistivity
- format: what-happens
- asks: effect

What will happen to the conduction electrons of a metal under a uniform field if they never collided with the ions:

a) They will accelerate and the current will grow without limit
b) They will move at a constant average drift velocity
c) They will stay at rest, as nothing pushes them
d) They will vibrate about fixed positions in the lattice

### Answer

a

### Explanation

Session 13, Slides 10-11: the field gives each electron $a = q_e E/m_e$; only the "friction forces" due to collisions with the ions keep the speed, and so the current, constant for a given $E$.

- b) A constant drift velocity is the result of the collisions; without them nothing would limit the speed.
- c) Forgets that the field exerts a force $F = q_e E$ on every electron.
- d) Vibration about lattice sites describes the ions heated by temperature, not free electrons under a field.

### Source

Session 13, Slides 10-11.

## Q34.8 Origin of the resistivity of a metal

- id: B34-Q8
- concept_id: u6-collisions-origin-resistivity
- format: true-statement
- asks: cause

Which one of the following statements about the resistivity of a metal is TRUE?

a) It falls as the disorder of the metal structure grows
b) It is caused by the acceleration of electrons by the field
c) It depends only on the number of free electrons per volume
d) It grows with the number of electron collisions with the ions

### Answer

d

### Explanation

Session 13, Slide 13: the resistivity $\rho = 1/\sigma$ grows with the disorder in the metal structure and with the number of collisions between non-bonded electrons and metallic ions.

- a) Inverted trend: disorder scatters the electrons, so it raises the resistivity.
- b) The acceleration is what the field does; the resistance comes from the collisions that oppose it (Slide 11).
- c) Ignores the mobility: $\sigma = n|q_e|\mu$ depends on the number of electrons AND their mobility (Slide 13).

### Source

Session 13, Slides 11 and 13.

## Q34.9 Friction forces on the electrons

- id: B34-Q9
- concept_id: u6-collisions-origin-resistivity
- format: identify
- asks: cause

In the free-electron model of a metal, the friction forces that limit the speed of the electrons come from:

a) The repulsion among the free electrons
b) The collisions of the electrons with the ions
c) The band gap the electrons must cross
d) The large mass of the electrons alone

### Answer

b

### Explanation

Session 13, Slide 11: for a given $E$ the current is constant, so there are friction forces, due to collisions with the ions, that counteract the acceleration; they are the origin of the resistivity.

- a) The model of the slides attributes the friction to the ions, not to electron-electron repulsion.
- c) A gap to cross belongs to semiconductors; a metal has empty states just above $E_f$ (Slide 6).
- d) The mass only sets the acceleration $a = q_e E/m_e$; inertia alone cannot keep the speed constant.

### Source

Session 13, Slides 6 and 10-11.

## Q34.10 Longer and thicker wire

- id: B34-Q10
- concept_id: u6-resistance-geometry
- format: what-happens
- asks: effect
- check: 2/2**2 == 0.5

A copper wire is replaced by one of the same copper, twice as long and twice the diameter. What will happen to its resistance:

a) It will double
b) It will stay the same
c) It will be halved
d) It will fall to one quarter

### Answer

c

### Explanation

$R = \rho\,l/A$ with $A = \pi d^2/4$: doubling $l$ multiplies $R$ by 2 and doubling $d$ multiplies $A$ by 4, so $R$ changes by $2/4 = 1/2$.

- a) Only the longer length was considered; the larger cross-section was ignored.
- b) The area was taken as proportional to the diameter instead of its square, so the two factors of 2 cancel.
- d) Only the four times larger area was considered; the doubled length was ignored.

### Source

Session 13, Slides 10 and 13; Topic 6 note, Section 4 ($R = \rho l/A$).

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
