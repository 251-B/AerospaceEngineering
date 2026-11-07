---
materia: "Aerospace Materials I"
tema: "Topic 7: Magnetic and Thermal Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 12"
dificultad: medium
badge: "Microstructure · ferromagnetic properties"
tags:
  - official-problem
  - solved
  - microstructure
  - bloch-walls
  - coercivity
  - permeability
---

# ✏️ Problem: T7-12 — Effect of Grain Size, Impurities and Porosity on a Ferromagnetic Material

## 📄 Official Statement
> 12. Specify in the following table how the increase in the following microstructural parameters affect the listed properties of a ferromagnetic material
>
> | | Grain size | Impurities | Porosity |
> | :--- | :--- | :--- | :--- |
> | Hysteresis losses | | | |
> | Conductivity | | | |
> | Permeability | | | |
> | Coercitivity | | | |
> | Saturation Magnetization | | | |
> | Curie Temperature | | | |

The sheet prints no solution for this problem.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **One parameter at a time.** Each column is an increase of that parameter with the composition of the ferromagnetic material and the other parameters kept constant.
2. **Domain walls control the loop.** A larger grain gives the Bloch walls more mobility, and inclusions, dislocations and pores reduce it. With a larger mobility the permeability grows and the coercivity and the remanence fall; with a smaller mobility the opposite happens [Session 15 Slide 21].
3. **Impurities and porosity as obstacles.** The slide groups inclusions, dislocations and pores as obstacles to the walls, so impurities (as particles of a second phase) and pores act in the same way on the loop. The effect of dissolved atoms is the same in direction (extension).
4. **Intrinsic properties.** The saturation magnetization is constant for a material of a given composition [Session 15 Slide 20]. The Curie temperature is the temperature at which the saturation magnetization falls to zero, and the table of Slide 23 gives a different value for each element; both are fixed by the composition and the bonding, not by the microstructure (the link between $T_c$ and the composition is an extension).
5. **Conductivity.** The electrical resistivity grows with the structural imperfections (grain boundaries, dislocations) and with the impurities [Session 13 Slides 16-17]; the effect of pores is an extension.
6. **Hysteresis losses.** The energy lost per cycle is the area of the loop (extension, as in [[Problem - T7-11 Hysteresis Loops of Soft and Hard Magnetic Materials]]): a wider loop (higher $H_c$) means higher losses.

**Unknown:** the effect (increase, decrease or none) of each parameter on each of the six properties.

---

## 🧠 2. Model and Strategy

Two chains separate the properties. The first goes from the microstructure to the mobility of the Bloch walls, and from the mobility to the permeability, the coercivity and the area of the loop. The second contains the properties that the microstructure does not change at all: the saturation magnetization and the Curie temperature, set by the composition. The conductivity follows its own chain, the scattering of the conduction electrons.

| Parameter | Mobility of the Bloch walls | Permeability | Coercivity | Loop area (losses) |
| :--- | :--- | :--- | :--- | :--- |
| Larger grain size | increases | increases | decreases | decreases |
| More impurities, pores | decreases | decreases | increases | increases |

**Strategy.**
1. Fill the first chain from Slide 21.
2. Decide the conductivity from the scattering of the electrons, with Session 13.
3. State why the saturation magnetization and the Curie temperature do not change with the microstructure.
4. Collect the answers in the table of the statement.

---

## 🔢 3. Step-by-Step Derivation

### 1. Grain size [Session 15 Slide 21]
A larger grain size increases the mobility of the Bloch walls, because there are fewer grain boundaries to stop them. So:
- permeability $\mu$: **increases**;
- coercivity $H_c$: **decreases** (and the remanence $B_r$ too);
- hysteresis losses: **decrease**, since a narrower loop has a smaller area;
- conductivity: **increases**, because the grain boundaries are structural imperfections that scatter the electrons and raise the resistivity [Session 13 Slides 16-17].

### 2. Impurities [Session 15 Slide 21]
Inclusions of another phase are obstacles that pin the walls, and the mobility decreases. So:
- permeability: **decreases**;
- coercivity: **increases** (and the remanence too);
- hysteresis losses: **increase**;
- conductivity: **decreases**, because foreign atoms and particles raise the residual resistivity $\rho_i$ [Session 13 Slide 16].

### 3. Porosity [Session 15 Slide 21]
Pores are listed on the slide with the inclusions, so the loop changes as for the impurities:
- permeability: **decreases**;
- coercivity: **increases**;
- hysteresis losses: **increase**;
- conductivity: **decreases** (extension): the pores remove conducting section and scatter the electrons, so the same direction as for the impurities.

### 4. Saturation magnetization [Session 15 Slide 20]
The saturation magnetization is constant for a material of a given composition: it is reached when all the dipoles of the solid are aligned, and the number and the intensity of the dipoles are fixed by the composition. Therefore:
- grain size: **no effect**;
- impurities: **no effect** while they are only inclusions; if an impurity dissolves and changes the composition the value changes (extension);
- porosity: **no effect** on the material itself. Per unit of total volume the pores only dilute the magnetization (extension).

### 5. Curie temperature [Session 15 Slide 23]
$T_c$ is the temperature at which the saturation magnetization falls abruptly to zero. Each material has its own value (Fe 1043 K, Co 1404 K, Ni 631 K, Gd 289 K), which depends on the elements, not on the size of the grains or on the pores. Grain size and porosity have **no effect**. Impurities have **no effect** as inclusions; dissolved elements that change the composition can shift it (extension).

### 6. Result
| Property | Grain size increases | Impurities increase | Porosity increases |
| :--- | :--- | :--- | :--- |
| Hysteresis losses | decrease | increase | increase |
| Conductivity | increases | decreases | decreases |
| Permeability | increases | decreases | decreases |
| Coercivity | decreases | increases | increases |
| Saturation magnetization | no effect | no effect as inclusions | no effect |
| Curie temperature | no effect | no effect as inclusions | no effect |

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Consistency of the table.** Permeability and coercivity move in opposite directions in every column, as the slide says ($\mu$ up with $H_c$ and $B_r$ down for a larger grain, and the reverse for the obstacles). The losses follow the coercivity.
- **Impurities and porosity act alike.** Slide 21 puts inclusions, dislocations and pores in the same line, and the table gives the same entries for both columns, except for the properties that depend on the composition.
- **Limits.** For no obstacles (a pure, dense, coarse-grained material) the walls move freely: the highest permeability and the lowest coercivity and losses. For a very porous material the loop widens and the section that carries the flux and the current shrinks.

### Interpretation
One rule explains the table: whatever stops the Bloch walls raises the coercivity and the losses and lowers the permeability, and whatever frees them does the opposite. The saturation magnetization and the Curie temperature are properties of the composition, so no change in the microstructure alone moves them. The same rule is used on purpose in the two classes of Problem T7-11: soft magnetic materials are made pure, dense and with large grains, and hard magnetic materials are made with obstacles (fine grains, precipitates), which is an extension of the slide. A higher conductivity also raises the currents induced in a core under alternating fields, which adds to the losses; this is an extension, and the table asks only for the effects listed.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| All 18 entries of the table | not printed on the sheet | table of Section 3 | permeability, coercivity: Session 15 Slide 21; saturation magnetization: Slide 20; conductivity: Session 13 Slides 16-17; the entries marked extension (porosity and conductivity, effect of composition on $M_s$ and $T_c$, losses as loop area) are not printed on the slides |

## 🔗 Related Links
* [[Topic 7 - Magnetic and Thermal Properties]]
* [[Topic 6 - Electrical Properties]]
* [[Problem - T7-11 Hysteresis Loops of Soft and Hard Magnetic Materials]]
