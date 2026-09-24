---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 14"
dificultad: baja
tags:
  - problema-oficial
  - resuelto
  - xrd
  - bragg-spacing
  - iron-allotropy
  - bcc
  - fcc
---

# ✏️ Problema: T2-CS14 — Difracción XRD y Espaciados Interplanares en Hierro BCC y FCC

## 📄 Enunciado Oficial
> **14. Fe has a BCC or an FCC structure, depending on the temperature. The X-ray diffraction (XRD) technique allows determining the spacing or distances between crystalline planes, from which the lattice parameters are deduced. For the BCC structure, the lattice parameter is $a = 0.2864\text{ \AA}$, while for the FCC $a = 0.3592\text{ \AA}$.**  
> *(Note: The numerical values in the official text are given directly in angstroms $0.2864\text{ \AA}$ and $0.3592\text{ \AA}$ — corresponding numerically to nanometers $0.2864\text{ nm}$ and $0.3592\text{ nm}$).*  
> **a)** What distance can be expected between the planes $(020)$ for both structures?  
> **b)** Calculate the distance between the most compact planes of both structures.  
> *(Solution: a) $d_{020}(\text{BCC}) = 0.143\text{ \AA}$; $d_{020}(\text{FCC}) = 0.179\text{ \AA}$; b) $\text{BCC } (110) = 0.2025\text{ \AA}$; $\text{FCC } (111) = 0.207\text{ \AA}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Parámetro de red de la fase BCC ($\alpha\text{-Fe}$): $a_{\text{BCC}} = 0.2864\text{ \AA}$.
* Parámetro de red de la fase FCC ($\gamma\text{-Fe}$): $a_{\text{FCC}} = 0.3592\text{ \AA}$.
* Planos de Máxima Compacidad [Session 4 Slide 9]:
  * En estructura BCC: planos más densos $\{110\}$.
  * En estructura FCC: planos más densos $\{111\}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Para cualquier cristal con simetría cúbica, el espaciado interplanar $d_{hkl}$ que separa dos planos paralelos de la misma familia de Miller viene dado por la relación fundamental [Session 3 Slide 53]:

$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

* Para el plano $(020)$:
  $$d_{020} = \frac{a}{\sqrt{0^2 + 2^2 + 0^2}} = \frac{a}{2}$$
* Para el plano más compacto de BCC $(110)$:
  $$d_{110}^{\text{BCC}} = \frac{a_{\text{BCC}}}{\sqrt{1^2 + 1^2 + 0^2}} = \frac{a_{\text{BCC}}}{\sqrt{2}}$$
* Para el plano más compacto de FCC $(111)$:
  $$d_{111}^{\text{FCC}} = \frac{a_{\text{FCC}}}{\sqrt{1^2 + 1^2 + 1^2}} = \frac{a_{\text{FCC}}}{\sqrt{3}}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Distancia entre Planos $(020)$
* **Para la Estructura BCC:**
  $$d_{020}(\text{BCC}) = \frac{a_{\text{BCC}}}{2} = \frac{0.2864\text{ \AA}}{2} = \mathbf{0.1432\text{ \AA}} \approx \mathbf{0.143\text{ \AA}}$$

* **Para la Estructura FCC:**
  $$d_{020}(\text{FCC}) = \frac{a_{\text{FCC}}}{2} = \frac{0.3592\text{ \AA}}{2} = \mathbf{0.1796\text{ \AA}} \approx \mathbf{0.179\text{ \AA}}$$

---

### 2. Apartado b: Distancia entre Planos Más Compactos
* **Estructura BCC (Plano $(110)$):**
  $$d_{110}(\text{BCC}) = \frac{a_{\text{BCC}}}{\sqrt{2}} = \frac{0.2864\text{ \AA}}{1.4142136} = \mathbf{0.20251\text{ \AA}} \approx \mathbf{0.2025\text{ \AA}}$$

* **Estructura FCC (Plano $(111)$):**
  $$d_{111}(\text{FCC}) = \frac{a_{\text{FCC}}}{\sqrt{3}} = \frac{0.3592\text{ \AA}}{1.7320508} = \mathbf{0.20738\text{ \AA}} \approx \mathbf{0.207\text{ \AA}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

1. **Correlación con la Ley de Bragg:** En un ensayo de difracción de rayos X con radiación de cobre $K\alpha$ ($\lambda = 1.5418\text{ \AA}$ o $0.15418\text{ nm}$), el ángulo de difracción $\theta$ está inversamente relacionado con $d_{hkl}$:
   $$\sin\theta = \frac{\lambda}{2 d_{hkl}}$$
   Dado que los planos más compactos tienen el **mayor espaciado interplanar $d_{hkl}$** ($d_{110}^{\text{BCC}} = 0.2025\text{ \AA}$, $d_{111}^{\text{FCC}} = 0.207\text{ \AA}$), producen el **primer pico de difracción a menor ángulo $2\theta$** y con la mayor intensidad en el espectro XRD.
2. **Espaciados muy similares:** Es notable comprobar que $d_{110}^{\text{BCC}} \approx 0.203\text{ \AA}$ y $d_{111}^{\text{FCC}} \approx 0.207\text{ \AA}$ son prácticamente idénticos (diferencia $< 2\%$), lo que confirma que las distancias entre las capas más densas de átomos de hierro apenas varían al cruzar la temperatura de transformación alotrópica de $910^\circ\text{C}$.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
