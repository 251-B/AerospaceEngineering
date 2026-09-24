---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 38-46"
tags:
  - teoria
  - concepto-fundamental
  - defectos-planares
  - limites-de-grano
  - hall-petch
  - maclas
  - fallas-de-apilamiento
  - energia-superficial
dificultad: media
prerrequisitos:
  - "[[Concepto - Dislocaciones Vector de Burgers y Deslizamiento en Metales]]"
---

# 🧱 Concepto: Defectos Planares, Límites de Grano, Maclas y Ecuación de Hall-Petch

> **Definición:** Los **defectos planares o bidimensionales** son interfaces o límites que separan un material cristalino en diferentes dominios que poseen idéntica estructura cristalina pero diferente orientación espacial, o bien representan discontinuidades en la secuencia de apilamiento atómico [Slide 38].

---

## 🌾 1. Límites de Grano (Grain Boundaries)

Un material metálico estructural convencional no es un monocristal, sino un **policristal** constituido por millones de cristalitas individuales denominadas **granos**, formados durante la solidificación simultánea a partir de múltiples núcleos independientes [Slide 39-40].

### Características Estructurales y Termodinámicas [Slide 41]:
* **Anchura de la frontera:** Tiene un grosor de únicamente **2 a 5 distancias interatómicas** ($0.5\text{--}1.5\text{ nm}$).
* **Desajuste atómico:** En este estrecho espacio, los átomos no logran alcanzar el espaciado de equilibrio ni la coordinación completa.
* **Alta energía interfacial ($\gamma_{\text{gb}}$):** Debido a la menor densidad de empaquetamiento atómico y enlaces distorsionados, los límites de grano son zonas altamente energéticas:
  * Son caminos preferenciales de **alta difusión atómica en estado sólido** ($D_{\text{gb}} \gg D_{\text{red}}$).
  * Son sitios preferentes para la **precipitación de segundas fases** y la segregación de impurezas.
  * Son reactivos químicamente (susceptibles a la **corrosión intergranular** en aleaciones aeronáuticas de aluminio de las series 2000 y 7000).

---

## 📈 2. Efecto Barrera al Deslizamiento y Ecuación de Hall-Petch

Cuando una dislocación se desplaza bajo una tensión aplicada a lo largo de su plano de deslizamiento, se propaga fácilmente por el interior del grano hasta chocar contra un límite de grano [Slide 41]:
1. El plano y dirección de deslizamiento cambian bruscamente de orientación al cruzar la frontera.
2. El desorden atómico en el límite destruye la continuidad periódica del plano de deslizamiento.
3. Las dislocaciones se apilan en el límite de grano (**dislocation pile-up**), acumulando una controtensión de rechazo que frena el avance de las siguientes dislocaciones.

### Ecuación de Hall-Petch [Slide 41]:
A menor tamaño de grano $d$, mayor es el área total de límites de grano por unidad de volumen y más corto es el camino libre medio de las dislocaciones antes de ser bloqueadas. Esto incrementa exponencialmente el límite elástico del material según la **relación de Hall-Petch**:

$$\sigma_y = \sigma_0 + k_y \cdot d^{-1/2}$$

donde:
* $\sigma_y$: límite elástico aparente del policristal ($\text{MPa}$).
* $\sigma_0$: tensión de fricción de la red (resistencia intrínseca al movimiento de una dislocación aislada dentro del grano).
* $k_y$: coeficiente de bloqueo o constante de endurecimiento de Hall-Petch ($\text{MPa}\cdot\mu\text{m}^{1/2}$).
* $d$: diámetro medio de grano (obtenido mediante metalografía óptica o SEM).

> [!TIP]
> **El Único Mecanismo Sin Compromiso:**
> El refinamiento de grano es el único mecanismo metalúrgico de endurecimiento que **aumenta simultáneamente el límite elástico ($\sigma_y$) y la tenacidad de fractura / ductilidad**, reduciendo además la temperatura de transición dúctil-frágil (DBTT) en aceros y aleaciones de titanio aeroespaciales.

---

## 🪞 2. Maclas (Twin Boundaries)

Una **macla** es un límite planar especial que separa dos regiones cristalinas cuya orientación reticular presenta una relación de **simetría especular (imagen en espejo)** respecto a un plano cristalino común denominado *plano de maclado* [Slide 42].

* **Maclas de Deformación (Mechanical Twinning):** Producidas por una tensión mecánica de cizalladura severa o impacto dinámico a bajas temperaturas. Son determinantes para conferir deformabilidad plástica a metales HCP (como $\text{Ti}$ y $\text{Mg}$) y metales BCC que carecen de suficientes sistemas de deslizamiento activos a baja temperatura.
* **Maclas de Recocido (Annealing Twins):** Se generan durante los tratamientos térmicos de recristalización en metales FCC con baja energía de falla de apilamiento (p. ej., aceros inoxidables austeníticos AISI 304/316, latones $\text{Cu-Zn}$ [Slide 43]).

---

## 📑 3. Fallas de Apilamiento (Stacking Faults)

Una falla de apilamiento es una interrupción local de una o dos capas atómicas en la secuencia periódica regular de empaquetamiento compacto [Slide 44]:

* **Secuencia perfecta en FCC:** $\dots ABC\, ABC\, ABC \dots$
* **Falla de apilamiento intrínseca en FCC:**
  $$\dots ABC\, AB\, ABC \dots$$
  Nótese que en la zona central la secuencia local es $AB\, AB$, que coincide exactamente con la secuencia de una estructura **HCP**. Por tanto, una falla de apilamiento en un cristal FCC es una lámina atómica ultradelgada de simetría HCP.
* **Energía de Falla de Apilamiento (SFE):** Metales con baja SFE (como el latón o el acero inoxidable) disocian sus dislocaciones completas en **dislocaciones parciales de Shockley**, impidiendo el deslizamiento cruzado (cross-slip) y confiriendo una alta tasa de endurecimiento por deformación.

---

## 🌐 4. Superficies Externas y Energía Superficial ($\gamma_s$)

La superficie externa que confina cualquier sólido cristalino es el defecto planar terminal [Slide 45]:
* Los átomos superficiales carecen de sus vecinos exteriores: su **número de coordinación es menor** que en el interior del volumen ($\text{NC}_{\text{sup}} < \text{NC}_{\text{int}}$).
* Estos enlaces atómicos rotos o insatisfechos acumulan un exceso de energía elástica y electrostática denominado **energía libre superficial ($\gamma_s$)**:
  $$E_{\text{superficie}} > E_{\text{interior}}$$
* Termodinámicamente, los materiales tienden a minimizar su área superficial expuesta para reducir su energía libre total (fuerza motriz de la sinterización de polvos cerámicos y metálicos en pulvimetalurgia aeroespacial).

---
*Enlaces Bidireccionales:*
* `[[Concepto - Dislocaciones Vector de Burgers y Deslizamiento en Metales|⬅️ Anterior: Dislocaciones y Deslizamiento]]`
* `[[Concepto - Polimorfismo y Alotropia en Metales y Ceramicos|Siguiente: Polimorfismo y Alotropía ➡️]]`
