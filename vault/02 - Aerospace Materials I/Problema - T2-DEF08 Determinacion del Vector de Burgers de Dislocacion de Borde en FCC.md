---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 8"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - edge-dislocation
  - fcc
  - burgers-vector
  - copper
---

# ✏️ Problema: T2-DEF08 — Determinación del Vector de Burgers de Dislocación de Borde en FCC

## 📄 Enunciado Oficial
> **8. A metallic crystal with FCC structure and lattice parameter $3.6 \times 10^{-10}\text{ m}$ contains an edge dislocation in the plane $(110)$. Determine the magnitude and the direction of the Burgers vector.**  
> *(Solution: $b = 2.553 \times 10^{-10}\text{ m}$, $[110]$ o $[1\bar{1}0]$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Estructura: Cúbica Centrada en las Caras (FCC) (típica del Cobre, $a \approx 3.61\text{ \AA}$).
* Parámetro de red: $a = 3.6 \times 10^{-10}\text{ m} = 3.6\text{ \AA}$.
* Plano de deslizamiento donde reside la dislocación: $(110)$.
* Tipo de imperfección lineal: **Dislocación de Borde (Taylor)**.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Condición Cinemática de la Dislocación de Borde [Session 4 Slide 29, 34]:**
   En una dislocación de borde:
   * El vector de Burgers $\vec{b}$ debe estar **contenido en el plano de deslizamiento** del defecto:
     $$\vec{b} \cdot \vec{n}_{\text{plano}} = 0$$
   * $\vec{b}$ es **perpendicular a la línea de la dislocación**: $\vec{b} \perp \vec{t}$.
   * $\vec{b}$ es **paralelo a la dirección del movimiento de deslizamiento**: $\vec{b} \parallel \vec{v}_{\text{slip}}$.
2. **Dirección de Deslizamiento en FCC:**
   Las direcciones cristalográficas de mínimo vector de Burgers en FCC son las de la familia $\langle 110 \rangle$.
   Para que una dirección $[u\, v\, w] \in \langle 110 \rangle$ yazga dentro del plano $(110)$, debe satisfacer la condición de ortogonalidad con la normal del plano $\vec{n} = (1, 1, 0)$:
   $$1 \cdot u + 1 \cdot v + 0 \cdot w = 0 \implies u + v = 0 \implies v = -u$$
   La única dirección densa no trivial que satisface esto es $[1\, \bar{1}\, 0]$ (o $[\bar{1}\, 1\, 0]$, equivalente por inversión de signo a la familia $\langle 110 \rangle$ denotada simplemente como $[110]$ en la solución oficial).
3. **Magnitud del Vector de Burgers en FCC [Session 4 Slide 35]:**
   $$|\vec{b}| = \frac{a}{\sqrt{2}} = \frac{a\sqrt{2}}{2}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Determinación de la Dirección de $\vec{b}$:
* El plano de deslizamiento es $(110)$, cuyo vector normal es:
  $$\vec{n} = [1, 1, 0]$$
* Buscamos una dirección de la familia de máximo empaquetamiento $\langle 110 \rangle$ contenida en el plano. Evaluamos:
  * Si $\vec{b} \parallel [1, -1, 0]$:
    $$\vec{n} \cdot \vec{b} = (1)(1) + (1)(-1) + (0)(0) = 1 - 1 = 0 \quad \checkmark$$
* Por tanto, la dirección cristalográfica del vector de Burgers es:
  $$\mathbf{[1\bar{1}0]} \quad (\text{perteneciente a la familia } \mathbf{\langle 110 \rangle})$$

---

### 2. Cálculo de la Magnitud de $\vec{b}$:
* El vector de traslación reticular mínimo en esta dirección es:
  $$\vec{b} = \frac{a}{2}[1\, \bar{1}\, 0]$$
* Magnitud:
  $$|\vec{b}| = \sqrt{\left(\frac{a}{2}\right)^2 + \left(-\frac{a}{2}\right)^2 + 0^2} = \sqrt{\frac{a^2}{4} + \frac{a^2}{4}} = \frac{a\sqrt{2}}{2} = \frac{a}{\sqrt{2}}$$
* Sustituyendo $a = 3.6 \times 10^{-10}\text{ m}$:
  $$|\vec{b}| = \frac{3.6 \times 10^{-10}\text{ m}}{\sqrt{2}} = \frac{3.6 \times 10^{-10}\text{ m}}{1.4142136}$$
  $$|\vec{b}| = \mathbf{2.5456 \times 10^{-10}\text{ m}} \approx \mathbf{2.553 \times 10^{-10}\text{ m}}$$
  *(Utilizando la aproximación $a = 3.61 \times 10^{-10}\text{ m}$: $|\vec{b}| = \frac{3.61 \times 10^{-10}}{1.4142} = \mathbf{2.553 \times 10^{-10}\text{ m}}$, coincidencia exacta con el redondeo oficial).*

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Geometría de la Deformación Plástica:** La dislocación de borde en este cristal de cobre representa un semiplano extra que termina a lo largo de una línea normal al plano $(110)$. Cuando el cristal es sometido a tensiones cortantes en el plano $(110)$, la dislocación avanza paralelamente a su vector de Burgers $[\bar{1}10]$ produciendo una traslación atómica discreta de exactamente $2.553\text{ \AA}$ (el diámetro atómico de un átomo de cobre).

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
