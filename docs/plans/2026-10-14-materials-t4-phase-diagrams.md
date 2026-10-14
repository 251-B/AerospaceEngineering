# Plan: Aerospace Materials I, Topic 4 (Phase Diagrams) on the portal

Fecha: 2026-10-14 · Estado: borrador, pendiente de aprobación

## 1. Objetivo y reglas de alcance

Llevar el Tema 4 completo (teoría + los 26 problemas oficiales) al portal siguiendo la misma línea que los Temas 1–3:
`sources/` → `vault/` → `subjects/` → `index.html`.

Reglas que se aplican en todas las fases:

1. **Solo el contenido de las slides.** La teoría sigue las cuatro sesiones diapositiva a diapositiva, en su orden, y cada sección cita su origen (`[Session 7 Slide 16]`). No se añade teoría que no esté en las slides; si algo hace falta para entender un paso, se marca como *extension* (regla de `AGENTS.md`), y se intenta evitar.
2. **Las mismas figuras que las slides.** Cada figura explicativa de una slide aparece en la página, redibujada como SVG o copiada (ver §4). Las figuras decorativas (logos, portadas) no se copian.
3. **Ejemplos resueltos solo con datos de las slides.** Un ejemplo usa un diagrama, una aleación o un punto que ya aparecen en las slides; si hay que leer un valor de un diagrama, se indica "reading of the figure". Ningún dato inventado ni de fuentes externas.
4. **Problemas: los 26 oficiales**, resueltos con el método de cuatro fases y contrastados con `Solution problems Phase diagrams I/II.pdf`. Si el resultado no coincide con la clave oficial, se mantiene el valor calculado y se añade un aviso de discrepancia; nunca se ajustan datos para cuadrar.

## 2. Inventario de fuentes (`sources/cuatrimestre-1/02-aerospace-materials-1/unit-04-phase-diagrams/`)

| Fichero | Págs. | Contenido |
| :--- | :--- | :--- |
| `teoria/Session 7 T4 Phase diagrams I_2025.pdf` | 32 | Conceptos básicos, diagramas unarios, isomorfos, regla de Gibbs, regla de la palanca, solidificación fuera de equilibrio, eutécticos |
| `teoria/Session 8 T4 Phase diagrams II.pdf` | 17 | Precipitación en estado sólido, reacciones invariantes, intermetálicos, fusión congruente/incongruente |
| `teoria/Session 9 T4 Phase diagrams III.pdf` | 23 | Sistema Fe-C, transformaciones de equilibrio, elementos de aleación |
| `teoria/Session 10 T4 Phase diagrams IV.pdf` | 8 | Diagramas cerámicos y ternarios |
| `problemas/Problems T4_PhaseDiagrams I.pdf` | 7 | 15 problemas (binarios generales) |
| `problemas/Problems T4_PhaseDiagrams II.pdf` | 3 | 11 problemas (Fe-C + 1 ternario) |
| `problemas/Solution problems Phase diagrams I.pdf` | 37 | Soluciones, casi todo diagramas anotados (imagen) |
| `problemas/Solution problems Phase diagrams II.pdf` | 12 | Soluciones, ídem |

Las soluciones oficiales son sobre todo diagramas con anotaciones a mano: su lectura se marca como tal en las notas.

## 3. Estructura de la página de teoría (slide → sección)

Una sola página `subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html` (la ruta ya prevista en el MOC), generada desde la nota `vault/02 - Aerospace Materials I/Topic 4 - Phase Diagrams and Solidification.md`, en cuatro partes (una por sesión). ★ = lleva ejemplo resuelto (§5).

**Part I — Session 7 (Phase diagrams I)**

| § | Sección | Slides |
| :--- | :--- | :--- |
| 1 | Component, phase, microconstituent | S7 2 |
| 2 | Definition of the equilibrium phase diagram (stability map) | S7 3 |
| 3 | Unary (P-T) diagrams: water and its cooling curve, pure iron, triple point | S7 5–6 |
| 4 | Binary isomorphous systems: from cooling curves to the diagram (milk/cheese analogy of the slides), complete solid solubility, liquidus/solidus | S7 8–11 |
| 5 ★ | Gibbs phase rule $F=C-P+N$ and its $N=1$ form at 1 atm | S7 13 |
| 6 ★ | Tie line and lever rule (Cu-Ni, $C_0=35$ wt% Ni, step by step as in the slides) | S7 15–21 |
| 7 ★ | Non-equilibrium solidification: coring/microsegregation, homogenisation | S7 23–24 |
| 8 ★ | Binary eutectic systems: invariant reaction, eutectic microstructure, examples (Sn-In, Al-Si, Al-Cu, Mg-Sn), hypo/hypereutectic cooling, lever rule with $P$, $Q$, $R$ | S7 26–32 |

**Part II — Session 8 (Phase diagrams II)**

| § | Sección | Slides |
| :--- | :--- | :--- |
| 9 ★ | Solid-state precipitation: below/above the solvus | S8 2–4 |
| 10 ★ | Invariant reactions: eutectoid (Cu-Zn, $\delta \to \gamma + \varepsilon$), peritectic (worked case at 42.4 % Ag, rapid solidification), peritectoid, monotectic; summary table of the reactions | S8 6–12 |
| 11 | Intermetallic compounds: terminal and intermediate phases | S8 14–15 |
| 12 ★ | Congruent and incongruent melting | S8 17 |

**Part III — Session 9 (Phase diagrams III: Fe-C)**

| § | Sección | Slides |
| :--- | :--- | :--- |
| 13 | Fe-C system: allotropy of iron, the metastable Fe-Fe₃C diagram (peritectic, eutectic, eutectoid), phases α, γ, δ, Fe₃C, two-phase regions, invariant reactions, microconstituents | S9 2–11 |
| 14 ★ | Equilibrium transformations: eutectoid steel (point b), hypoeutectoid 0.3 % C (points c–f), hypereutectoid steel | S9 12–20 |
| 15 | Effect of the cooling rate on pearlite | S9 21 |
| 16 | Influence of alloying elements (α- and γ-stabilisers, shift of the eutectoid) | S9 22–23 |

**Part IV — Session 10 (Phase diagrams IV)**

| § | Sección | Slides |
| :--- | :--- | :--- |
| 17 ★ | Ceramic phase diagrams: Al₂O₃-Cr₂O₃, Al₂O₃-SiO₂ and mullite | S10 2–4 |
| 18 ★ | Ternary diagrams: reading the composition triangle, Ag-Cu-Zn (liquidus/solidus surfaces), Fe-Cr-Ni (points 1 and 2), clay-feldspar-quartz | S10 5–8 |

Notas de concepto (como en T1–T3), enlazadas desde la nota de tema y el MOC:
`Concept - Phases, Components and Microconstituents`, `Concept - Gibbs Phase Rule`, `Concept - Tie Line and Lever Rule`, `Concept - Binary Eutectic Systems and Microconstituents`, `Concept - Invariant Reactions in Binary Systems`, `Concept - Intermetallic Compounds and Congruent Melting`, `Concept - The Fe-Fe3C Diagram and Steel Microstructures`, `Concept - Ceramic and Ternary Phase Diagrams`.

## 4. Figuras

Criterio (híbrido, recomendado):

- **Diagramas de fases, curvas de enfriamiento, tie lines, esquemas** → **SVG redibujado** en `tools/figures/materials_t4.py` con `svgkit` (como T1–T3). Motivo: se leen valores sobre ellos, deben verse bien en los seis palettes de lectura y en el PDF en blanco y negro. Los puntos clave (temperaturas y composiciones) se toman del texto de las slides y se comprueban superponiendo el SVG sobre el render de la slide.
- **Micrografías y fotos** (núcleos de coring, eutécticos, perlita, precipitados, analogías de leche/queso/patata) → **copia** del bitmap original con `pdfimages -png` (resolución nativa, sin recomprimir) en `vault/attachments/T4/`, con pie que cita la slide. Se cubren con las reglas de imágenes raster de `study-surface.css` §7–11.

Lista inicial:

| Figura | Slides | Tipo |
| :--- | :--- | :--- |
| Diagrama P-T del agua + curva de enfriamiento | S7 5 | SVG |
| Diagrama P-T del hierro puro | S7 6 | SVG |
| Fotos de estructuras del Fe / analogía patatas | S7 6 | PNG |
| Curvas de enfriamiento → diagrama isomorfo (0/20/50/80/100 % B) | S7 8–9 | SVG |
| Analogía leche/queso | S7 9–10 | PNG |
| Diagrama Cu-Ni con liquidus/solidus | S7 11 | SVG |
| Diagrama con regiones y valor de $F$ (regla de Gibbs) | S7 13 | SVG |
| Tie line Cu-Ni con $R$ y $S$ (un SVG por paso clave) | S7 15–21 | SVG |
| Coring: diagrama fuera de equilibrio + micrografía | S7 23–24 | SVG + PNG |
| Diagrama eutéctico genérico, temperatura/composición eutéctica | S7 26–27 | SVG |
| Micrografías de eutécticos (Sn-In, Al-Si, Al-Cu, Mg-Sn) | S7 28–29 | PNG |
| Hipo/hipereutéctico con curvas de enfriamiento y microestructuras | S7 30–31 | SVG + PNG |
| Palanca en eutéctico con $P$, $Q$, $R$ | S7 32 | SVG |
| Solvus y precipitación (esquemas + ejemplo) | S8 2–4 | SVG + PNG |
| Eutectoide Cu-Zn, peritéctico, peritectoide, monotéctico | S8 6–12 | SVG |
| Intermetálicos (diagrama con fases intermedias, Ti-B) | S8 14–15 | SVG |
| Fusión congruente/incongruente | S8 17 | SVG |
| Alotropía del Fe, diagrama Fe-Fe₃C completo | S9 3–4, 9–11 | SVG |
| Fases α, γ, δ, Fe₃C (estructuras + micrografías) | S9 5–8 | PNG |
| Perlita, hipo/hipereutectoide (puntos b–f) | S9 12–20 | SVG + PNG |
| Perlita gruesa/fina vs velocidad de enfriamiento | S9 21 | PNG |
| Desplazamiento del eutectoide por aleantes | S9 22–23 | SVG |
| Al₂O₃-Cr₂O₃, Al₂O₃-SiO₂ (mullita) | S10 2–4 | SVG |
| Triángulo ternario, Ag-Cu-Zn, Fe-Cr-Ni, arcilla-feldespato-cuarzo | S10 5–8 | SVG |

Figuras de problemas (en `vault/attachments/T4-problems/`, como `T2-problems/`): Pb-Sn, Ag-Cu, Al-Ni, Cu-Sn, Ni-Mo, Ti-Si, Ti-B, diagramas hipotéticos A-B (P1, P8, P11, P14), Fe-Fe₃C con las temperaturas $T_1$–$T_5$ de cada problema, triángulo ternario del P11 (hoja II). Se redibujan en SVG con las coordenadas que dan el enunciado y la solución oficial.

## 5. Ejemplos resueltos dentro de la teoría

Cada ejemplo va en un callout `> [!example]` en la nota, con las cuatro fases condensadas (datos → planteamiento → cálculo sin saltos → comprobación), y usa solo datos de las slides:

| § | Ejemplo | Datos de |
| :--- | :--- | :--- |
| 5 | Grados de libertad en cada región de las figuras de la slide (agua en el punto triple y en una línea, binario en L+α a 1 atm) | S7 13 |
| 6 | Composición y fracciones en Cu-35 % Ni: $C_L=32$, $C_\alpha=43$ wt% Ni, $W_L=0.73$, $W_\alpha=0.27$ (la slide redondea a 0.72/0.28: se señala) + comprobación $W_L+W_\alpha=1$ y balance de masa | S7 16–21 |
| 7 | Lectura de la secuencia de coring en la figura de la slide (composiciones del primer y último sólido) | S7 23–24 |
| 8 | Aleación hipoeutéctica de la slide: fracciones de fases y de microconstituyentes con $P$, $Q$, $R$; comprobación de que ambas descripciones cuadran | S7 30–32 |
| 9 | Fracción de precipitado tras cruzar el solvus en la aleación de ejemplo de la slide | S8 4 |
| 10 | Peritéctico al 42.4 % Ag: $W_L=(42.4-7)/(55-7)=0.74$, $W_\alpha=0.26$ por encima; solo β por debajo | S8 9 |
| 12 | Clasificar como congruente/incongruente cada compuesto del diagrama Ti-B de la slide | S8 15, 17 |
| 14a | Acero eutectoide (punto b): $W_\alpha$ y $W_{Fe_3C}$ con $C_\alpha=0.022$ y $C_{Fe_3C}=6.67$ % C | S9 13 |
| 14b | Hipoeutectoide 0.3 % C, puntos c → f: fases, composiciones, fracciones, ferrita proeutectoide y perlita | S9 15–18 |
| 14c | Hipereutectoide (aleación de la slide): cementita proeutectoide y perlita | S9 19–20 |
| 17 | Palanca en Al₂O₃-SiO₂ en un punto marcado en la slide | S10 3 |
| 18 | Lectura de composiciones en el triángulo: punto 1 (20 Fe, 60 Cr, 20 Ni) y punto 2 (74 Fe, 18 Cr, 8 Ni) | S10 7 |

## 6. Problemas (26)

Notas en `vault/02 - Aerospace Materials I/`, mismo formato que `Problem - T3-01 ...` (frontmatter, enunciado oficial, cuatro fases, enlaces):

- Hoja I → `Problem - T4-PD01 ...` a `Problem - T4-PD15 ...`: A-B hipotético con tabla (1), 2, Pb-Sn 80 % y 30 % Sn (3–4), Ag-Cu (5–7), A-B eutéctico al 65 % B (8), Al-Ni (9), Cu-Sn (10), dibujar un diagrama A-B (11), Ni-Mo (12), Ti-Si (13), hipotético (14), Ti-B (15).
- Hoja II → `Problem - T4-FC01 ...` a `Problem - T4-FC11 ...`: Fe-C con 0.5, 0.76, 1.5 y 4.3 % C (1–4), composición desde fracciones (5), fundiciones (6–7), barra de 5 kg con 0.55 % C y efecto del Ni (8), fundición 3 % C (9), Fe-Fe₃C general (10), aleación ternaria H (11).

Adaptación del método de cuatro fases a este tema:
1. **Setup:** aleación, temperaturas $T_i$, qué se pide (fases vs microconstituyentes), tabla de datos leídos del diagrama (marcados "reading of the figure").
2. **Frames:** los ejes del diagrama (composición wt % – temperatura); para el ternario, el triángulo y cómo se leen las tres coordenadas (suma = 100 %). Sin matriz de cambio de base salvo que el problema la pida.
3. **Derivation:** tie line en cada $T_i$, regla de la palanca escrita con sus segmentos antes de sustituir, aritmética paso a paso; reacciones invariantes en forma de ecuación.
4. **Interpretation:** comprobaciones (suma de fracciones = 1, balance $W_\alpha C_\alpha + W_\beta C_\beta = C_0$, coherencia fases ↔ microconstituyentes), esquema de microestructura y cotejo con la clave oficial (`Check against the official key`, con aviso de discrepancia cuando toque; p. ej. las claves de la hoja I usan $C_\alpha=19.2$, $C_\beta=97.5$ % Sn para Pb-Sn y hay que confirmar qué valores dan las slides).

Página: `subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html`, una sola página con dos bloques (Hoja I y Hoja II), como `topic-2-problems.html`; 26 `problem-card` con enunciado en `.problem-statement-box` y solución por fases (para que Ask AI separe bien enunciado y solución).

## 7. Integración en el portal

1. `tools/topic_pages.json`: entrada para la página de teoría (`figures: "materials_t4"`, plantilla `topic-3-diffusion.html`).
2. `tools/source_links.json`: los cuatro PDF de teoría y los dos de problemas; tira "Official material" en ambas páginas; enlace "Original statement" por tarjeta; citas `[Session N Slide M]` enlazadas.
3. `subjects/aerospace-materials-1/teoria/index.html` y `problemas/index.html`: tarjeta del Tema 4 (claves `materials.topic_4_*` en `assets/js/i18n.js`, "Tema 4 · Sesiones 7–10").
4. `index.html`: badges a "4 of 11 units" y el nuevo total de problemas (auditado por `badge-drift`).
5. MOC: quitar "(planned)" del Tema 4 y enlazar nota de tema, conceptos y problemas; `00 - Indice Central` si procede.
6. Regenerar: `build_topic_pages.py`, `source_links.py`, `build_source_notes.py`, `build_pdfs.py`.

## 8. Ejecución por fases

| Fase | Trabajo | Quién | Salida |
| :--- | :--- | :--- | :--- |
| 0 | Render de las 80 slides y páginas de problemas/soluciones a PNG en el scratchpad (`pdftoppm -r 150`); extraer bitmaps con `pdfimages`; inventario slide → texto, fórmulas, figuras, decisión SVG/PNG | `source-researcher` | Inventario (fuera del repo) |
| 1 | Digitalizar los diagramas: tabla de puntos clave por diagrama, sacada del texto de slides/enunciados y comprobada visualmente | `source-researcher` + revisión | Tabla de coordenadas |
| 2a | Nota de tema + notas de concepto + ejemplos resueltos (Partes I–IV) | `aerospace-pedagogue` → `subject-web-builder` | Vault |
| 2b | `tools/figures/materials_t4.py` + PNG copiados | `subject-web-builder` | `vault/attachments/T4/` |
| 2c | Problemas Hoja I (15) | `problem-step-mentor` + builder | Notas `T4-PD**` + SVG |
| 2d | Problemas Hoja II (11) | `problem-step-mentor` + builder | Notas `T4-FC**` + SVG |
| 3 | Generar la página de teoría; montar la de problemas desde la plantilla | `subject-web-builder` | `subjects/...` |
| 4 | Integración (§7) | `subject-web-builder` | Índices, badges, enlaces |
| 5 | Verificación (§9) y `ultrareview` (cierre de capítulo) | `web-qa-reviewer` + equipo | Informe, correcciones |
| 6 | Commits por bloque: `feat(materials): ...` | `web-qa-reviewer` | Git |

2a–2d van en paralelo (Agent Team de 4, cada uno con sus propios ficheros: nota de tema y conceptos / módulo de figuras / notas PD / notas FC). Tamaño estimado: ~18 secciones, ~12 ejemplos, ~30 SVG de teoría, ~15 PNG, 26 problemas con ~20 SVG.

Orden sugerido de entrega si se prefiere ir por partes: Parte I + problemas PD01–PD08 → Parte II + PD09–PD15 → Parte III + FC01–FC10 → Parte IV + FC11.

## 9. Verificación (criterio de cierre)

- `python tools/vault_lint.py` y `python tools/audit_portal.py`: 0 errores.
- `python tools/build_topic_pages.py --check`, `python tools/source_links.py --check`, `python tools/build_source_notes.py --check`, `python tools/build_pdfs.py --check`.
- `python tools/render_check.py` sobre las dos páginas nuevas y los dos índices.
- `python -m unittest discover -s tools/tests` (incluye `test_surface.py`: textos y etiquetas SVG en AAA en todos los palettes).
- Revisión visual en móvil y escritorio, tema claro/oscuro.
- `ultrareview`: (1) aritmética de cada palanca sin saltos; (2) unidades y composiciones homogéneas (wt %, °C/K); (3) cada afirmación y figura trazable a una slide, cada problema contra su enunciado y su clave; (4) web: tema, responsive, consola limpia, `render_check` limpio.

## 10. Decisiones abiertas

1. **Figuras:** híbrido SVG + PNG (recomendado) / todo copiado de las slides / todo redibujado.
2. **Página de teoría:** una página con cuatro partes (recomendado, ya prevista en el MOC) / cuatro páginas, una por sesión.
3. **Entrega:** todo de una vez con equipo de agentes / por partes (§8).
