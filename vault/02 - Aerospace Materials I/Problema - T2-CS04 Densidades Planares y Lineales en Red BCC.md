---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 4"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - planar-density
  - linear-density
  - volumetric-density
  - bcc
---

# ✏️ Problema: T2-CS04 — Densidades Planares y Lineales en Red BCC

## 📄 Enunciado Oficial
> **4. For a BCC structure, determine the surface (planar) density for the planes $(100)$, $(110)$ and $(111)$; the linear density in the direction $[100]$, and the volume density.**  
> *(Solution: $\rho_{(100)} = 1/a^2$, $\rho_{(110)} = \sqrt{2}/a^2$, $\rho_{(111)} = 1/(a^2\sqrt{3})$, $\rho_{[100]} = 1/a$, $\rho_v = 2/a^3$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Contexto Físico:
Se estudia una red Cúbica Centrada en el Cuerpo (BCC) con parámetro de red $a$.

### Datos Reticulares de BCC:
* Átomos por celda unitaria: $n = 2$ (8 en vértices $\times 1/8$ + 1 central).
* Volumen de la celda cúbica: $V_C = a^3$.
* Radio atómico: $R = \frac{a\sqrt{3}}{4}$ (contacto a lo largo de la diagonal del cubo $\langle 111 \rangle$).

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Aplicando las definiciones formales del curso [Session 4 Slides 7-9]:
* **Densidad Planar ($\rho_{(hkl)}$):**
  $$\rho_{(hkl)} = \frac{N_{\text{átomos contenidos en la cara o sección}}}{A_{(hkl)}}$$
* **Densidad Lineal ($\rho_{[uvw]}$):**
  $$\rho_{[uvw]} = \frac{N_{\text{átomos cortados diametralmente}}}{L_{[uvw]}}$$
* **Densidad Volumétrica ($\rho_v$):**
  $$\rho_v = \frac{n}{V_C} = \frac{2}{a^3}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Densidad Planar en el Plano $(100)$:
* **Geometría del plano:** Cara exterior del cubo de dimensiones $a \times a$.
* **Área:** $A_{(100)} = a^2$.
* **Átomos contenidos:** Solo los 4 átomos situados en los vértices del cuadrado (el átomo central de la celda BCC está en $z = a/2$, por lo que no pertenece al plano $z=0$ ni $x=0$).
  $$N_{\text{átomos}} = 4 \times \frac{1}{4} = 1\text{ átomo}$$
* **Densidad planar:**
  $$\rho_{(100)} = \frac{1}{a^2} = \mathbf{\frac{1}{a^2}}$$

### 2. Densidad Planar en el Plano $(110)$:
* **Geometría del plano:** Rectángulo diagonal que cruza el cubo pasando por dos aristas opuestas.
* **Dimensiones:** Base $= a\sqrt{2}$ (diagonal de cara), Altura $= a$.
* **Área:**
  $$A_{(110)} = a\sqrt{2} \times a = a^2\sqrt{2}$$
* **Átomos contenidos:**
  * 4 vértices del rectángulo, aportando cada uno $\frac{1}{4}$: $4 \times \frac{1}{4} = 1\text{ átomo}$.
  * 1 átomo en el centro geométrico de la celda (el plano $(110)$ pasa exactamente por el centro del cubo): aporta $1\text{ átomo}$ completo.
  * Total de átomos: $N_{\text{átomos}} = 1 + 1 = 2\text{ átomos}$.
* **Densidad planar:**
  $$\rho_{(110)} = \frac{2}{a^2\sqrt{2}} = \frac{2\sqrt{2}}{2a^2} = \mathbf{\frac{\sqrt{2}}{a^2}}$$

### 3. Densidad Planar en el Plano $(111)$:
* **Geometría y espaciado:**
  En la red BCC, los planos paralelos $(111)$ tienen un espaciado interplanar $d_{111} = \frac{a}{\sqrt{1^2+1^2+1^2}} = \frac{a}{\sqrt{3}}$.
  Sin embargo, debido a que el átomo central se sitúa exactamente en la mitad de la diagonal del cubo a lo largo de $[111]$, los planos $(111)$ reales se alternan a una distancia efectiva $d_{\text{eff}} = \frac{a}{2\sqrt{3}}$ (correspondiente a la familia reflejada $\{222\}$).
* **Cálculo directo por celda o relación de densidad:**
  Utilizando la relación de conservación fundamental entre densidades [Session 4 Slide 9]:
  $$\rho_v = \frac{\rho_{(hkl)}}{d_{\text{eff}}} \implies \rho_{(111)} = \rho_v \cdot d_{\text{eff}} = \left(\frac{2}{a^3}\right) \cdot \left(\frac{a}{2\sqrt{3}}\right) = \mathbf{\frac{1}{a^2\sqrt{3}}}$$
* **Verificación directa por área geométrica:**
  El plano que corta los vértices $(a, 0, 0)$, $(0, a, 0)$, $(0, 0, a)$ forma un triángulo equilátero de lado $L = a\sqrt{2}$ y área $A = \frac{\sqrt{3}}{4}(a\sqrt{2})^2 = \frac{\sqrt{3}}{2}a^2$.
  El plano no contiene el átomo central (éste se encuentra en $(a/2, a/2, a/2)$, cuya distancia al origen es $\frac{a\sqrt{3}}{2}$, mientras que el plano está a $\frac{a}{\sqrt{3}}$).
  Por tanto, el plano solo contiene los 3 vértices: $N_{\text{átomos}} = 3 \times \frac{1}{6} = \frac{1}{2}\text{ átomo}$.
  $$\rho_{(111)} = \frac{1/2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{1}{a^2\sqrt{3}}}$$

### 4. Densidad Lineal en la Dirección $[100]$:
* **Longitud del segmento de arista:** $L_{[100]} = a$.
* **Átomos cortados:** Corta los dos átomos de los vértices por sus extremos:
  $$N_{\text{átomos}} = 2 \times \frac{1}{2} = 1\text{ átomo}$$
* **Densidad lineal:**
  $$\rho_{[100]} = \frac{1}{a} = \mathbf{\frac{1}{a}}$$

### 5. Densidad Volumétrica ($\rho_v$):
* Contiene $n = 2$ átomos en un volumen de celda $V_C = a^3$:
  $$\rho_v = \mathbf{\frac{2}{a^3}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Comparativa

Comparando las densidades planares obtenidas en la red BCC:
* $\rho_{(110)} = \frac{\sqrt{2}}{a^2} \approx \frac{1.414}{a^2}$
* $\rho_{(100)} = \frac{1}{a^2} = \frac{1.000}{a^2}$
* $\rho_{(111)} = \frac{1}{a^2\sqrt{3}} \approx \frac{0.577}{a^2}$

$$\rho_{(110)} > \rho_{(100)} > \rho_{(111)}$$

El plano $(110)$ es el plano de **mayor densidad atómica de la estructura BCC**, confirmando rigurosamente por qué la familia $\{110\}$ constituye el plano de deslizamiento preferencial de las dislocaciones en metales BCC como el hierro ferrítico ($\alpha\text{-Fe}$), molibdeno, tantalio y wolframio [Session 4 Slide 36].

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
