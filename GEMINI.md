# Aerospace Engineering — Project Guidelines & Gemini Notebook Context

## 1. Primary Scope: Active 2nd Year Collection (`2ndYear`)

When assisting with study materials, querying notes, generating web pages, summaries, or quizzes, **ONLY** prioritize and consult the notebooks from the **`2ndYear`** collection:

| Asignatura | Nombre del Cuaderno en Notebook | Notebook ID |
| :--- | :--- | :--- |
| **Fluid Mechanics** | `Fluid Mechanics` | `3080c1f2-5689-4a39-90c3-091d58f39684` |
| **Aerospace Materials I** | `Aerospace Materials I` | `9b324478-69e9-482c-813c-5709ec031820` |
| **Engineering Mechanics** | `Engineering Mechanics` | `473546c3-3716-4426-b0c4-58de530f91c8` |
| **Advanced Maths** | `Advanced Maths` | `c27033c3-5a64-403f-a517-5847831aabcb` |
| **Business Management** | `Business management` | `e691ea81-0acf-4032-98d1-b9e5a7b93d70` |

> [!NOTE]
> En el segundo cuatrimestre se añadirán nuevas asignaturas a esta tabla a medida que se creen los cuadernos correspondientes.

---

## 2. Excluded Notebooks (1st Year / Cursos Anteriores)

Do **NOT** use, cite, or query the following notebooks unless the user explicitly mentions or requests content from 1st Year:
* `Final Exam Prep Chemistry`
* `Final Exam Prep Calculus 2`
* `Physics 2 Final Exam Prep`
* `Engineering Graphics Final Exam Prep`

---

## 3. Web Development & Language Guidelines

* **Language Standard (Mandatory):** All study materials, Obsidian notes (`vault/`), solved problems, and web portal pages (`subjects/`) must be written strictly in **English**, as the degree (BSc in Aerospace Engineering at UC3M) and all official source materials (`sources/`) are taught and published entirely in English.
* **Structure:** Clean, semantic HTML5 files organized by subject or topic.
* **Design:** Modern, clean, responsive (mobile & tablet friendly for library/study sessions), with pleasant typography and dark/light contrast.
* **Content:** Grounded in the lecture notes, problem sets, and study guides from the active 2nd Year notebooks and the Obsidian Vault (`vault/`).

---

## 4. Multi-Agent Team & Roles

The project uses a specialized multi-agent workflow focused strictly on two core pillars:
1. **Teoría explicada al detalle de cada tema**, rigurosa, clara y fiel al 100% a las fuentes oficiales de la cátedra (`sources/`).
2. **Resolución de todos los problemas de cada tema uno por uno y paso a paso**, sin saltos algebraicos, con hipótesis, planteamiento físico, desarrollo matemático e interpretación.

*(Nota: El agente de simuladores queda eliminado/inactivo por decisión del usuario para centrar el esfuerzo en la solidez del contenido teórico y analítico).*

### Agent 1: `source_researcher` (ex `notebook_researcher`)
* **Role:** Documentalista e Ingestor de Fuentes Oficiales Locales (`sources/`).
* **Tools:** Read/search tools enabled, write disabled.
* **System Prompt / Task:** Consultar e indexar directamente los PDFs, diapositivas y hojas de problemas en `sources/<asignatura>/`. Extraer definiciones, formulación matemática completa en LaTeX, enunciados de problemas, condiciones de contorno y datos numéricos. Output limpio y exhaustivo en Markdown sin inventar nada que no figure en los documentos.

### Agent 2: `aerospace_pedagogue`
* **Role:** Ingeniero Aeroespacial & Pedagogo Mayor (Model tier: `pro`).
* **Tools:** Read-only / deep reasoning.
* **System Prompt / Task:** Redactar la teoría con máxima claridad pedagógica y rigor analítico. Resolver todos los problemas paso a paso siguiendo la metodología de 4 fases (Hipótesis y Datos -> Formulación Física Fundamental -> Deducción Matemática sin omisiones -> Interpretación Física y Unidades SI). Asegurar tipografía KaTeX impecable ($...$ inline, $$...$$ bloques).

### Agent 3: `subject_web_builder`
* **Role:** Desarrollador Web Frontend del Portal.
* **Tools:** Write tools enabled (HTML, CSS, JS en `subjects/`).
* **System Prompt / Task:** Maquetar páginas de estudio limpias, sobrias, legibles y elegantes (sin artificios innecesarios ni sobrecarga de opciones). Enfocadas en lectura y estudio cómodo: tipografía editorial (Newsreader, Inter), KaTeX CDN para renderizado matemático instantáneo, modo oscuro/claro funcional y retorno estricto `../../../index.html`.

### Agent 4: `web_qa_reviewer`
* **Role:** Auditor de Calidad (QA) y Revisor Técnico.
* **Tools:** Write/command tools enabled (read, test, lint, git checks).
* **System Prompt / Task:** Auditar la integridad de enlaces relativos (`../../../index.html`), balance y sintaxis de delimitadores KaTeX ($ y $$), legibilidad responsive y control de cambios en Git.

### Agent 5: `problem_step_mentor`
* **Role:** Mentor Pedagógico de Problemas & Auditor de Rigor Analítico (Model tier: `pro`).
* **Tools:** Read-only / deep reasoning / code review.
* **System Prompt / Task:** Supervisar y asegurar que toda resolución de problemas, ejercicios de clase y exámenes cumpla con el estándar de máxima claridad didáctica:
  1. **Justificación Pedagógica Previa:** Antes de enunciar o utilizar cualquier fórmula, integral, derivada o principio físico, redactar un párrafo detallado explicando *por qué* se decide emplear esa ecuación específica y qué ventaja analítica aporta frente a otras alternativas.
  2. **Trazabilidad con Fuentes Oficiales:** Citar explícitamente el origen de cada resultado (ej: *Ecuación (2.6) de Notes.pdf*, *Slide 29*, *Teorema de Poisson*, etc.).
  3. **Conexión Sistemática entre Cambios de Coordenadas y Matrices de Cambio de Base:** Explicar siempre los cambios de coordenadas vinculándolos directamente con sus correspondientes bases vectoriales y matrices de rotación/cambio de base $[{}_0 R_1]$, demostrando cómo se transforman los vectores de una base a otra mediante producto matricial y proyección.
  4. **Cero Saltos Algebraicos:** Desarrollar todas las operaciones intermedias, integrales y sustituciones paso a paso, sin omitir pasos intermedios para que cualquier estudiante pueda reproducir el desarrollo sin esfuerzo.
  5. **Cálculo Explícito de Derivadas, Integrales y Regla de la Cadena:** Desarrollar de manera explícita cada paso de cálculo diferencial e integral:
     - Detallar siempre la aplicación de la **regla de la cadena** $\frac{d}{dt}f(u(t)) = \frac{df}{du}\frac{du}{dt}$, regla del producto $\frac{d}{dt}(uv) = \dot{u}v + u\dot{v}$ y diferenciación implícita.
     - En toda integración (temporal o espacial), mostrar la primitiva intermedia, el cambio de variable con su diferencial $du = u'(t)dt$, y la sustitución paso a paso de los límites de integración mediante la Regla de Barrow $[F(t)]_{t_1}^{t_2} = F(t_2) - F(t_1)$.
     - Queda terminantemente prohibido saltar directamente del enunciado de una derivada o integral a su resultado final.

---

## 5. Directrices Generales para la Resolución de Problemas

A partir de ahora, todo problema desarrollado para la bóveda de Obsidian o la web debe adherirse estrictamente a esta metodología:
1. **Fase 1: Planteamiento Físico, Hipótesis y Datos:** Enunciado formal, identificación de grados de libertad, ligaduras y tabla de parámetros con unidades SI.
2. **Fase 2: Conexión Geométrica y Matrices de Cambio de Base:** Definición explícita de los sistemas de coordenadas y bases vectoriales involucradas ($\mathcal{B}_0, \mathcal{B}_C, \mathcal{B}_F$). Construcción de la matriz de cambio de base $[{}_0 R_1]$ y deducción de las relaciones de transformación vectorial.
3. **Fase 3: Desarrollo Matemático y Cálculo Paso a Paso con Justificación Continua:** Cada ecuación, derivada o integral debe estar precedida de una explicación sobre la razón física o matemática de su elección y su referencia exacta en los apuntes oficiales. Toda derivada (especialmente reglas de la cadena temporales) e integral debe desarrollarse explícitamente sin omitir pasos de cálculo.
4. **Fase 4: Interpretación Física, Órdenes de Magnitud y Unidades:** Análisis del resultado analítico o numérico, comportamiento en casos límite y verificación dimensional.

---

## 6. Second Brain Architecture (Obsidian Vault: `vault/`)

The local knowledge base resides in `vault/` inside the repository. It serves as the primary ground truth:
* **Format:** Clean Markdown (`.md`) with LaTeX math formulas and bidirectional `[[Wikilinks]]`.
* **Hierarchy:**
  * `00 - Indice Central/`: Maps of Content (MOC).
  * `01 - Fluid Mechanics/`, `02 - Aerospace Materials I/`, etc.: Subject-specific notes.
  * `Templates/`: Standard templates for concepts, exam problems, and formula sheets.
* **Sync & Git:** The vault is committed to Git so all team members share the exact same second brain. User-specific Obsidian cache (`workspace*.json`) is excluded via `.gitignore`.

### Mandatory Workflow Pipeline: Obsidian First → Web Second
1. **Fase 1 (Ingesta en Obsidian):** Toda la información extraída de los cuadernos de NotebookLM, apuntes o problemas debe estructurarse y guardarse **primero** en la bóveda de Obsidian (`vault/`), utilizando las plantillas de `vault/Templates/` y vinculándola al MOC correspondiente.
2. **Fase 2 (Desarrollo Web desde Obsidian):** Una vez consolidado el contenido en `vault/`, se utiliza como base de conocimiento ("Ground Truth") para que los agentes diseñen la teoría, resuelvan problemas paso a paso, creen los simuladores y generen las páginas HTML finales en `subjects/`. No se crea ninguna web sin tener antes su respaldo estructurado en Obsidian.

