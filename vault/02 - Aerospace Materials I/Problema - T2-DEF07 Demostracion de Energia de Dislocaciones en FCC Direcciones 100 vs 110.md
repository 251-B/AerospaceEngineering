---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 7"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - dislocation-energy
  - frank-rule
  - burgers-vector
  - fcc
  - slip-systems
---

# ✏️ Problema: T2-DEF07 — Demostración de Energía de Dislocaciones en FCC: Direcciones [100] vs [110]

## 📄 Enunciado Oficial
> **7. For a metal with FCC structure, $E_1$ and $E_2$ are the energies necessary to generate dislocations in the directions $[100]$ and $[110]$, respectively. Demonstrate that $E_1 / E_2 = 2$.**  
> *(Solution: theory)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Modelo Reticular:
* Estructura: Cúbica Centrada en las Caras (FCC), con parámetro de red $a$.
* Relación con el radio atómico: $a\sqrt{2} = 4R \implies a = 2\sqrt{2}R$.

### Definición de Energías:
* $E_1$: Energía elástica por unidad de longitud para generar una dislocación con vector de Burgers a lo largo de la dirección $[100]$.
* $E_2$: Energía elástica por unidad de longitud para generar una dislocación con vector de Burgers a lo largo de la dirección $[110]$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Citando la teoría de Frank y la mecánica de dislocaciones [Session 4 Slide 29, 35]:
1. **Regla de Frank para la Energía Elástica de una Dislocación:**
   La energía elástica de deformación almacenada en el campo elástico de distorsión que rodea a una dislocación es directamente proporcional al **cuadrado del módulo de su vector de Burgers**:
   $$E \propto |\vec{b}|^2$$
2. **Determinación de los Vectores de Traslación Mínimos:**
   Para que una dislocación sea cinemáticamente estable en la red cristalina, su vector de Burgers debe conectar dos posiciones atómicas reticulares equivalentes:
   * En la dirección $[100]$, la traslación mínima que une dos nudos de la red FCC (dos vértices adyacentes) es la arista completa:
     $$\vec{b}_1 = a[1\, 0\, 0]$$
   * En la dirección $[110]$, debido a la presencia del átomo centrado en la cara, la traslación reticular más corta va desde un vértice hasta el centro de la cara:
     $$\vec{b}_2 = \frac{a}{2}[1\, 1\, 0]$$

---

## 🔢 3. Fase 3: Demostración Analítica Paso a Paso

### 1. Cálculo de $|\vec{b}_1|^2$ para la Dirección $[100]$:
* Vector: $\vec{b}_1 = (a, 0, 0)$.
* Módulo al cuadrado:
  $$|\vec{b}_1|^2 = a^2 + 0^2 + 0^2 = a^2$$
* Expresado en función del radio atómico ($a = 2\sqrt{2}R$):
  $$|\vec{b}_1|^2 = (2\sqrt{2}R)^2 = 8R^2$$
* Por tanto, la energía elástica asociada es:
  $$E_1 = k \cdot |\vec{b}_1|^2 = k \cdot a^2 = k \cdot (8R^2)$$
  donde $k$ es una constante elástica dependiente del módulo de cizalladura $G$ y del coeficiente de Poisson $\nu$.

---

### 2. Cálculo de $|\vec{b}_2|^2$ para la Dirección $[110]$:
* Vector: $\vec{b}_2 = \left(\frac{a}{2}, \frac{a}{2}, 0\right)$.
* Módulo al cuadrado:
  $$|\vec{b}_2|^2 = \left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2 + 0^2 = \frac{a^2}{4} + \frac{a^2}{4} = \frac{2a^2}{4} = \frac{a^2}{2}$$
* Expresado en función del radio atómico ($a = 2\sqrt{2}R$):
  $$|\vec{b}_2|^2 = \frac{8R^2}{2} = 4R^2$$
* Por tanto, la energía elástica asociada es:
  $$E_2 = k \cdot |\vec{b}_2|^2 = k \cdot \frac{a^2}{2} = k \cdot (4R^2)$$

---

### 3. Razón de Energías ($E_1 / E_2$):
Tomando el cociente entre ambas energías elásticas:
$$\frac{E_1}{E_2} = \frac{k \cdot |\vec{b}_1|^2}{k \cdot |\vec{b}_2|^2} = \frac{a^2}{a^2 / 2} = \frac{8R^2}{4R^2} = \mathbf{2}$$

$$\mathbf{\frac{E_1}{E_2} = 2} \quad \blacksquare \text{ Q.E.D.}$$

---

## 🎯 4. Fase 4: Interpretación Física y Consecuencias Metalúrgicas

* **Criterio de Descomposición Espontánea:** Supongamos que artificialmente se creara una dislocación con $\vec{b}_1 = a[100]$. Dado que:
  $$a[100] = \frac{a}{2}[110] + \frac{a}{2}[1\bar{1}0]$$
  La energía de los dos productos de disociación sería:
  $$E_{\text{productos}} \propto \left|\frac{a}{2}[110]\right|^2 + \left|\frac{a}{2}[1\bar{1}0]\right|^2 = \frac{a^2}{2} + \frac{a^2}{2} = a^2$$
  Al ser el vector $\vec{b}_2 = \frac{a}{2}\langle 110 \rangle$ dos veces menos energético individualmente ($E_2 = E_1 / 2$), la energía requerida para mover o activar térmicamente el deslizamiento en $[110]$ es la mitad que en $[100]$.
* Esto constituye la demostración analítica definitiva de la diapositiva 35 [Session 4 Slide 35] de por qué el deslizamiento plástico en metales FCC se restringe exclusivamente a las direcciones $\langle 110 \rangle$.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
