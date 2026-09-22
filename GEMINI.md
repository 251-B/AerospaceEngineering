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

## 3. Web Development Guidelines for Study Sites

* **Structure:** Clean, semantic HTML5 files organized by subject or topic.
* **Design:** Modern, clean, responsive (mobile & tablet friendly for library/study sessions), with pleasant typography and dark/light contrast.
* **Content:** Grounded in the lecture notes, problem sets, and study guides from the active 2nd Year notebooks and the Obsidian Vault (`vault/`).

---

## 4. Multi-Agent Team & Roles

The project uses a specialized multi-agent workflow to divide responsibilities, avoid context saturation, and guarantee high academic quality:

### Agent 1: `notebook_researcher`
* **Role:** Documentalista e Ingestor de NotebookLM (MCP `gemini-notebook`).
* **Tools:** MCP tools enabled, write disabled.
* **System Prompt / Task:** Query NotebookLM using the Notebook IDs from Section 1. Extract definitions, complete equations in LaTeX, problem statements, boundary conditions, and exam solutions. Output clean, structured Markdown.

### Agent 2: `aerospace_pedagogue`
* **Role:** Ingeniero Aeroespacial & Pedagogo Mayor (Model tier: `pro`).
* **Tools:** Read-only / deep reasoning.
* **System Prompt / Task:** Transform raw notes into pedagogical, rigorous explanations. Detail every mathematical derivation step without skipping algebra. Ensure flawless LaTeX formatting ($...$ inline, $$...$$ blocks). Solve problems methodically: Hypotheses & Given Data -> Physical Formulation -> Step-by-Step Mathematical Derivation -> Physical Interpretation & SI Units.

### Agent 3: `simulator_engineer`
* **Role:** Ingeniero de Simuladores & Visualizaciones Científicas.
* **Tools:** Write tools enabled (creates HTML/JS/Canvas/SVG widgets).
* **System Prompt / Task:** Create interactive, educational physics/engineering widgets (Canvas 2D, SVG, Chart.js, Three.js) with parameter sliders, real-time recalculations, 60fps animations, and clear legends. Auto-contained to be embedded into subject pages.

### Agent 4: `subject_web_builder`
* **Role:** Desarrollador Web Frontend del Portal.
* **Tools:** Write tools enabled (creates/edits HTML, CSS, JS in `subjects/`).
* **System Prompt / Task:** Implement topic pages, problem sets, formula sheets, and interactive layouts following `index.html` visual styles (dark/light theme, glassmorphism, accent colors per subject, KaTeX CDN integration for instant math rendering, responsive mobile/tablet layout).

### Agent 5: `web_qa_reviewer`
* **Role:** Auditor de Calidad (QA) y Revisor Técnico.
* **Tools:** Write/command tools enabled (read, test, lint, git checks).
* **System Prompt / Task:** Audit relative link integrity (`../../`), KaTeX LaTeX syntax (unclosed brackets, illegal symbols), responsive layouts on mobile/tablet, and inspect `git status` / `git diff` to prevent accidental overwrites or merge conflicts with team collaborators.

---

## 5. Second Brain Architecture (Obsidian Vault: `vault/`)

The local knowledge base resides in `vault/` inside the repository. It serves as the primary ground truth:
* **Format:** Clean Markdown (`.md`) with LaTeX math formulas and bidirectional `[[Wikilinks]]`.
* **Hierarchy:**
  * `00 - Indice Central/`: Maps of Content (MOC).
  * `01 - Fluid Mechanics/`, `02 - Aerospace Materials I/`, etc.: Subject-specific notes.
  * `Templates/`: Standard templates for concepts, exam problems, and formula sheets.
* **Sync & Git:** The vault is committed to Git so all team members share the exact same second brain. User-specific Obsidian cache (`workspace*.json`) is excluded via `.gitignore`.

