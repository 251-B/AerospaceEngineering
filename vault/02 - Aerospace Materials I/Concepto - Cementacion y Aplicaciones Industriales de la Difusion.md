---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 29-35"
tags:
  - teoria
  - concepto-fundamental
  - aplicaciones-industriales
  - cementacion
  - case-hardening
  - diffusion-bonding
  - sintering
  - rolls-royce-trent
dificultad: media
prerrequisitos:
  - "[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]"
  - "[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]"
---

# ⚙️ Concepto: Cementación y Aplicaciones Industriales de la Difusión

> **Relevancia Tecnológica:** Lejos de ser un fenómeno meramente teórico, la difusión en estado sólido es la base física de los procesos de manufactura más avanzados en la industria mecánica, electrónica y aeroespacial: desde el endurecimiento superficial de componentes de transmisión hasta la fabricación de álabes de turbofán huecos de titanio y circuitos integrados en obleas de silicio [Slides 29-34].

---

## 🏎️ 1. Cementación y Endurecimiento Superficial (*Case Hardening*)

El endurecimiento por carburación gaseosa (*gas carburizing* o cementación) es un tratamiento termoquímico que utiliza la **difusión intersticial de carbono** para generar un perfil de dureza superficial graduado en aceros de bajo carbono (e.g. AISI 1018, AISI 1010) [Slides 29-31]:

### 1.1 Principio Metalúrgico
1. **Atmósfera Reactiva:** La pieza de acero se introduce en un horno a temperatura de austenización ($850^\circ\text{C}\text{--}950^\circ\text{C}$, donde el hierro está en fase $\gamma\text{-Fe}$ FCC con alta solubilidad de carbono). Se inyecta una mezcla controlada de gas metano e hidrógeno ($\text{CH}_4 - \text{H}_2$):
   $$\text{CH}_4 \rightleftharpoons \text{C}_{\text{disuelto}} + 2\text{H}_2$$
2. **Difusión Intersticial:** El átomo de carbono se adsorbe en la superficie y difunde rápidamente hacia el interior siguiendo la solución analítica de la Segunda Ley de Fick [Slide 20].
3. **Mecanismo de Endurecimiento:**
   * Los átomos de carbono ocupan los huecos octaédricos de la red, generando campos de distorsión elástica que **bloquean el deslizamiento de dislocaciones** (*dislocation pinning*), dificultando la deformación plástica [Slide 30].
   * Tras la cementación, la pieza se templa y reviene, transformando la capa superficial rica en carbono en **martensita tetragonizada** de dureza extrema ($\ge 60\text{ HRC}$) [Slide 31].
4. **Tensiones Residuales de Compresión:**
   * La transformación martensítica de la capa superficial conlleva una expansión volumétrica mayor que la del núcleo bajo en carbono. Esto genera un estado superficial de **tensiones residuales de compresión** [Slide 30].
   * Dichas tensiones de compresión retrasan la nucleación y propagación de grietas por fatiga cíclica, elevando enormemente el límite de fatiga del componente [Slide 30].

### 1.2 El Requisito de la Doble Propiedad (Engranajes y Ejes):
* **Capa Exterior (*Outer Case*):** Extremadamente dura y resistente al desgaste por fricción, rozamiento y fatiga por contacto (*pitting*).
* **Núcleo Interior (*Inner Core*):** Dúctil y tenaz para absorber cargas de impacto dinámicas sin fractura catastrófica.
* **Fabricabilidad Óptima:** El mecanizado complejo de los dientes del engranaje se efectúa en el estado "blando" original (fácil maquinado); el endurecimiento termoquímico se realiza posteriormente sobre la geometría final [Slide 30].

---

## 🛩️ 2. Soldadura por Difusión y Conformado Superplástico (DB/SPF)

La **soldadura por difusión** (*Diffusion Bonding*, DB) es un proceso de unión en estado sólido donde dos superficies metálicas limpias y pulidas se presionan íntimamente a temperaturas elevadas ($T > 0.5\text{--}0.7 T_m$) en atmósfera de vacío o gas inerte [Slide 33].

### Mecanismo Físico:
* La deformación plástica microscópica inicial colapsa las asperezas superficiales.
* La interdifusión atómica a través de la interfaz elimina las microporosidades mediante difusión superficial y en bordes de grano.
* La interfaz desaparece completamente por recristalización y crecimiento de grano, formándose una unión monolítica continua con propiedades mecánicas idénticas a las del metal base [Slide 33].

### Aplicación Aeroespacial Insignia: Álabes de Turbofán Rolls-Royce Trent 500
* Los álabes de cuerda ancha (*wide-chord fan blades*) del motor **Rolls-Royce Trent 500** (que propulsa al Airbus A340-500/600) se fabrican mediante la combinación de **Soldadura por Difusión y Conformado Superplástico (DB/SPF)** de chapas de aleación de titanio $\text{Ti-6Al-4V}$ [Slide 33].
* Se genera una estructura de sándwich tridimensional hueca con núcleo interno corrugado (*honeycomb / truss core*).
* **Ventajas Críticas:**
  1. Reducción sustancial del peso del rotor del fan.
  2. Extraordinaria rigidez torsional y estructural.
  3. Resistencia masiva contra el daño por impacto de objetos extraños (**FOD**, *Foreign Object Damage*, e.g. ingestión de aves en despegue) [Slide 33].

---

## 🏺 3. Sinterización de Polvos Metálicos y Cerámicos (*Sintering*)

La **sinterización** es el proceso de consolidación de piezas a partir de polvos cerámicos o metálicos compactados a temperatura inferior al punto de fusión ($T < T_m$) [Slide 32].

* **Definición Oficial:** Proceso de transporte de masa, activado térmicamente, que conduce a la unión química entre partículas adyacentes y a la **reducción progresiva de la porosidad** [Slide 32].
* **Fuerza Impulsora:** Disminución de la energía libre interfacial total del sistema ($\Delta G < 0$) al reemplazar una inmensa área superficial libre sólido-gas ($\gamma_{\text{sv}}$) por fronteras de grano sólido-sólido de menor energía ($\gamma_{\text{gb}}$).
* **Fases Microestructurales [Slide 32]:**
  1. Compacto en verde (*Green compact*): partículas en contacto puntual con alta porosidad abierta.
  2. Formación y crecimiento de cuellos (*neck growth*) a $1220^\circ\text{C}\text{--}1370^\circ\text{C}$ mediante difusión superficial y volumétrica.
  3. Densificación y cierre de poros a $1520^\circ\text{C}$, con crecimiento de grano poligonal.
* **Aplicación Biomédica y Aeroespacial:** Prótesis de cadera de alúmina/circonia, toberas cerámicas de cohetes y componentes de carburo de silicio [Slide 32].

---

## 💧 4. Purificación de Hidrógeno con Membranas de Paladio ($\text{Pd}$)

El paladio metálico posee una solubilidad y permeabilidad selectiva extraordinaria hacia el hidrógeno gaseoso [Slide 35]:

* Las moléculas de $\text{H}_2$ se disocian catalíticamente en la superficie exterior del paladio en átomos de $\text{H}$.
* Los átomos de hidrógeno difunden intersticialmente con gran rapidez a través de la red FCC del $\text{Pd}$ gracias a un gradiente de concentración mantenido por la diferencia de presión parcial de gas entre ambas caras.
* Permite obtener hidrógeno con una pureza superior al $99.9999\%$, esencial para pilas de combustible en satélites y naves tripuladas [Slide 35].

---

## 💻 5. Microelectrónica: Difusión de Dopantes en Obleas de Silicio

La fabricación de semiconductores y circuitos integrados monolíticos (CMOS) depende de la introducción de impurezas aceptoras o donadoras (Boro, Fósforo, Arsénico, Aluminio) en monocristales de Silicio mediante difusión a alta temperatura ($900^\circ\text{C}\text{--}1200^\circ\text{C}$) [Slides 29, Problems 2]:

* Controlando el tiempo $t$ y la temperatura $T$, la solución de la función error ($\text{erf}$) permite modular con precisión nanométrica la profundidad de unión de la juntura $p\text{-}n$ ($x_j$).

---

## 🥛 6. Barreras Poliméricas y Permeación de Gases en Empaquetado y Aeroespacial

La difusión de vapores y gases ($\text{H}_2\text{O}$, $\text{O}_2$, $\text{CO}_2$) a través de films y recubrimientos poliméricos determina la vida útil de materiales compuestos y sistemas presurizados [Slide 34]:

* **Vapor de Agua:** La entrada de humedad deteriora la matriz de resina epoxi en materiales compuestos aeroespaciales (hidrotermalismo, plastificación de la resina y degradación de la temperatura de transición vítrea $T_g$).
* **Oxígeno:** La difusión de oxígeno en polímeros provoca degradación fotoquímica, oxidación de polímeros y corrosión de sustratos metálicos internos [Slide 34].

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]`
* `[[Concepto - Primera Ley de Fick Difusion en Estado Estacionario]]`
* `[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]`
* `[[Problema - T3-01 Carburacion de Engranaje de Acero 1018]]`
* `[[Problema - T3-05 Temperatura de Cementacion de Acero 1010 en 8 Horas]]`
* `[[Problema - T3-06 Purificacion de Hidrogeno con Membrana de Paladio]]`
