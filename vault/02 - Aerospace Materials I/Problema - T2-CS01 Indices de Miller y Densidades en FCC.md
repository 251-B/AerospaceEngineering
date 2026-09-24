---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 1"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - miller-indices
  - linear-density
  - planar-density
  - volumetric-density
  - fcc
---

# ✏️ Problema: T2-CS01 — Índices de Miller y Densidades en FCC

## 📄 Enunciado Oficial
> **1. Find the Miller indices corresponding to the planes in the figures:**  
> **Figure I, Figure II, Figure III.**  
> **For an FCC structure, with lattice parameter $a$, calculate the linear density along direction $[110]$, the planar density on the plane drawn on figure I and the volumetric density.**  
> *(Solution: I $(\bar{1}1\bar{1})$; II $(\bar{2}31)$; III $(\bar{1}\bar{1}1)$; $\rho_l = \sqrt{2}/a$; $\rho_s = 4/(a^2\sqrt{3})$; $\rho_v = 4/a^3$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Contexto Físico:
Se analizan tres planos cristalográficos dibujados dentro de celdas cúbicas de arista $a$. Posteriormente, se evalúa una red Cúbica Centrada en las Caras (FCC) de parámetro reticular $a$.

### Datos de Entrada:
* **Figura I:** El plano pasa por el vértice superior derecho, intersectando los ejes en: $x = -a$, $y = a$, $z = -a$ (tomando origen adecuado).
* **Figura II:** El plano corta los ejes en $x = -a/2$, $y = a/3$, $z = a$.
* **Figura III:** El plano corta los ejes en $x = -a$, $y = -a$, $z = a$.
* **Estructura FCC:** Parámetro reticular $a$, número de átomos por celda $n = 4$, radio atómico $R = a\sqrt{2}/4$.

### Hipótesis de Partida:
1. La red cúbica es ortonormal ($a=b=c$, $\alpha=\beta=\gamma=90^\circ$).
2. Para planos con índices negativos, el origen de coordenadas se traslada convenientemente a un vértice adyacente dentro de la celda unitaria [Session 3 Slide 43].
3. Los átomos se modelan como esferas rígidas en contacto a lo largo de las diagonales de cara $\langle 110 \rangle$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Antes de calcular, identificamos los principios rectores del temario oficial:
* **Determinación de Índices de Miller $(h\, k\, l)$ [Session 3 Slides 41-45]:**
  1. Identificar las coordenadas de corte fraccionarias $(p, q, r)$ con los ejes $x, y, z$.
  2. Calcular los recíprocos $(1/p, 1/q, 1/r)$.
  3. Reducir al conjunto de enteros mínimos multiplicando por el MCM.
* **Densidad Lineal ($\rho_l$) [Session 4 Slide 7]:**
  $$\rho_l = \frac{N_{\text{átomos centrados sobre el segmento}}}{L_{[uvw]}}$$
* **Densidad Planar ($\rho_s$ o $\rho_p$) [Session 4 Slide 8]:**
  $$\rho_s = \frac{N_{\text{átomos contenidos en el plano}}}{A_{(hkl)}}$$
* **Densidad Volumétrica ($\rho_v$) [Session 4 Slide 7]:**
  $$\rho_v = \frac{n}{V_C} = \frac{n}{a^3}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Índices de Miller de los Planos:
* **Figura I:**
  * Trasladando el origen a la esquina $(1, 0, 1)$, el plano intersecta los ejes en:
    $$x = -1, \quad y = +1, \quad z = -1$$
  * Recíprocos de las intersecciones:
    $$\frac{1}{-1} = -1, \quad \frac{1}{+1} = 1, \quad \frac{1}{-1} = -1$$
  * Notación de Miller:
    $$\mathbf{(\bar{1}1\bar{1})}$$
    *(Nótese que pertenece a la familia de planos compactos $\{111\}$).*

* **Figura II:**
  * Observando las marcas en los ejes de la Figura II:
    * Eje $x$: corte en $-a/2 \implies p = -1/2$ (con origen trasladado a $x=1$).
    * Eje $y$: corte en $+a/3 \implies q = +1/3$.
    * Eje $z$: corte en $+a \implies r = +1$.
  * Recíprocos:
    $$\frac{1}{-1/2} = -2, \quad \frac{1}{1/3} = 3, \quad \frac{1}{1} = 1$$
  * Notación de Miller:
    $$\mathbf{(\bar{2}31)}$$

* **Figura III:**
  * Trasladando el origen a $(1, 1, 0)$:
    * Eje $x$: corte en $-1 \implies p = -1$.
    * Eje $y$: corte en $-1 \implies q = -1$.
    * Eje $z$: corte en $+1 \implies r = +1$.
  * Recíprocos:
    $$\frac{1}{-1} = -1, \quad \frac{1}{-1} = -1, \quad \frac{1}{1} = 1$$
  * Notación de Miller:
    $$\mathbf{(\bar{1}\bar{1}1)}$$

---

### 2. Cálculos para la Red FCC:
* **Densidad lineal a lo largo de $[110]$:**
  * La dirección $[110]$ es la diagonal de la cara inferior del cubo.
  * Longitud del segmento: $L_{[110]} = a\sqrt{2}$.
  * Número de átomos cortados diametralmente:
    $$N_{\text{átomos}} = 2 \times \left(\frac{1}{2}\right)_{\text{vértices}} + 1_{\text{centro cara}} = 1 + 1 = 2\text{ átomos}$$
  * Densidad lineal:
    $$\rho_l = \frac{2}{a\sqrt{2}} = \frac{2\sqrt{2}}{2a} = \mathbf{\frac{\sqrt{2}}{a}}$$

* **Densidad planar sobre el plano de la Figura I $(\bar{1}1\bar{1}) \in \{111\}$:**
  * El plano $\{111\}$ intercepta tres diagonales de cara de longitud $L = a\sqrt{2}$, formando un triángulo equilátero.
  * Área del triángulo:
    $$A = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4} (a\sqrt{2})^2 = \frac{\sqrt{3}}{4}(2a^2) = \frac{\sqrt{3}}{2}a^2$$
  * Átomos contenidos en el interior del triángulo del plano:
    $$N_{\text{átomos}} = 3 \times \left(\frac{1}{6}\right)_{\text{vértices}} + 3 \times \left(\frac{1}{2}\right)_{\text{aristas}} = \frac{1}{2} + \frac{3}{2} = 2\text{ átomos}$$
  * Densidad planar:
    $$\rho_s = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{4}{a^2\sqrt{3}}}$$

* **Densidad volumétrica ($\rho_v$):**
  * La celda FCC posee $n = 4$ átomos equivalentes en un volumen $V_C = a^3$:
    $$\rho_v = \mathbf{\frac{4}{a^3}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

1. **Dimensionalidad:**
   * $[\rho_l] = \text{longitud}^{-1} \implies \frac{\sqrt{2}}{a}$ tiene dimensiones de $\text{átomos/m}$.
   * $[\rho_s] = \text{longitud}^{-2} \implies \frac{4}{a^2\sqrt{3}}$ tiene dimensiones de $\text{átomos/m}^2$.
   * $[\rho_v] = \text{longitud}^{-3} \implies \frac{4}{a^3}$ tiene dimensiones de $\text{átomos/m}^3$.
2. **Consistencia de empaquetamiento:**
   La dirección $[110]$ es la línea de máxima densidad lineal en FCC ($\rho_l = 1/(2R)$), y el plano $\{111\}$ es el plano de máxima densidad planar ($\text{APF}_{\text{planar}} = \pi/(2\sqrt{3}) \approx 90.7\%$), demostrando por qué $\{111\}\langle 110 \rangle$ es el sistema de deslizamiento canónico de los metales FCC.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
