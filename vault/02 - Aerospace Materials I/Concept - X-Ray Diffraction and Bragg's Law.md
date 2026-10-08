---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slide 53"
tags:
  - theory
  - fundamental-concept
  - x-ray-diffraction
  - bragg-law
  - interplanar-spacing
  - materials-characterization
dificultad: medium
prerrequisitos:
  - "[[Concept - Miller Notation for Cubic and Hexagonal Directions and Planes]]"
---

# ⚡ Concept: X-Ray Diffraction and Bragg's Law

> **Diffraction Principle:** X-rays have wavelengths of the order of interatomic distances ($\lambda \sim 0.05\text{--}0.25\text{ nm} \sim 0.5\text{--}2.5\text{ \AA}$). When a monochromatic beam strikes a periodic crystal, the waves elastically scattered by the electrons of parallel atomic planes interfere constructively if the optical path difference is an integer multiple of the wavelength [Slide 53].

---

## 📐 1. Interplanar Spacing Equations ($d_{hkl}$)

The interplanar spacing $d_{hkl}$ is the shortest perpendicular distance separating two adjacent crystallographic planes belonging to the same Miller family $(h\, k\, l)$ [Slide 53]:

### 1. Cubic System ($a = b = c$, $\alpha = \beta = \gamma = 90^\circ$):
$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

### 2. General Orthorhombic System ($a \neq b \neq c$, $\alpha = \beta = \gamma = 90^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2} \implies d_{hkl} = \frac{1}{\sqrt{\frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}}}$$

### 3. Tetragonal System ($a = b \neq c$, $\alpha = \beta = \gamma = 90^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{h^2 + k^2}{a^2} + \frac{l^2}{c^2}$$

### 4. Hexagonal System ($a = b \neq c$, $\gamma = 120^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{4}{3}\left(\frac{h^2 + hk + k^2}{a^2}\right) + \frac{l^2}{c^2}$$

---

## 🌊 2. Derivation of Bragg's Law

Consider two parallel incident rays with grazing angle $\theta$ (Bragg angle) reflected from two adjacent parallel atomic planes $(hkl)$ separated by a distance $d_{hkl}$:

```
     Ray 1 \          / Diffracted ray 1
            \   θ    /
 Plane 1 ─────●─────●───── (hkl)
            /|     |\
           / | d   | \
          /  |     |  \
     Ray 2 \ |     | / Diffracted ray 2
            \|  θ  |/
 Plane 2 ─────●─────●───── (hkl)
              A     B
```

* Ray 2 travels an additional distance before reflection equal to $d_{hkl}\sin\theta$.
* After reflection, it travels another identical additional distance equal to $d_{hkl}\sin\theta$.
* **Total optical path difference:**
  $$\Delta = 2\, d_{hkl}\sin\theta$$
* **Condition for Maximum Constructive Interference (Bragg's Law) [Slide 53]:**
  $$n\lambda = 2\, d_{hkl}\sin\theta$$
  where $n$ is the diffraction order ($n = 1$ for first-order diffraction, higher orders being absorbed into the Miller indices: $d_{nh, nk, nl} = d_{hkl}/n$).

---

## 🔍 3. Systematic Extinction Rules (Structure Factor $F_{hkl}$)

Because of destructive interference from intermediate atomic planes in centered cells, certain reflections $(hkl)$ do not appear in the diffractogram:

| Crystal Structure | Allowed Reflection Condition | Typical Observed Reflections | Forbidden (Extinct) Reflections |
| :--- | :--- | :--- | :--- |
| **Simple Cubic (SC)** | Any combination $(hkl)$ | $(100), (110), (111), (200), (210), (211)$ | None |
| **Body-Centered Cubic (BCC)** | $h + k + l = \text{even}$ | $(110), (200), (211), (220), (310), (222)$ | $(100), (111), (210), (300)$ |
| **Face-Centered Cubic (FCC)** | $h, k, l$ all even or all odd | $(111), (200), (220), (311), (222), (400)$ | $(100), (110), (210), (211)$ |

---

## 🔬 4. Applications in Aerospace Engineering

1. **Precise Determination of Lattice Parameters ($a, c$):**
   By accurately measuring the $2\theta$ peak angles, $d_{hkl}$ is calculated and the lattice parameter $a$ is solved for:
   $$a = \frac{\lambda \sqrt{h^2 + k^2 + l^2}}{2\sin\theta}$$
2. **Phase Identification and Polymorphism:**
   It allows allotropic phases to be distinguished instantly (e.g., BCC ferrite $\alpha\text{-Fe}$ vs FCC austenite $\gamma\text{-Fe}$; HCP $\alpha$-titanium vs BCC $\beta$-titanium).
3. **Analysis of Macroscopic Residual Stresses:**
   The presence of tensile or compressive residual stresses (due to shot peening, friction stir welding or machining) alters the interplanar spacing $\Delta d$, angularly shifting the diffraction peaks ($\Delta \theta$).

---
*Bidirectional Links:*
* [[Concept - Volumetric, Linear and Planar Density in Crystal Lattices|⬅️ Previous: Crystallographic Densities]]
* [[Concept - Point Defects, Thermal Vacancies, Schottky and Frenkel|Next: Point Defects ➡️]]
