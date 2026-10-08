# GEMINI.md

Gemini-specific instructions for this repository. **Read `AGENTS.md` first**: it holds the shared rules (architecture, language, web page rules, problem-solving standard, review protocols, routing, token economy, git policy, agent roles). This file adds only what is specific to Gemini.

## 0. Mandatory session initialization (Gemini)

At the start of any new conversation, session, or task, check whether the 5 subagents are registered (`manage_subagents` with action `list`). If any is missing, call `define_subagent` for each one as your first action, before the user's task:

1. `source_researcher`: read/search tools enabled, write disabled. Reads `sources/` only.
2. `aerospace_pedagogue`: model tier `pro`. Deep reasoning, theory, zero hallucinations.
3. `problem_step_mentor`: model tier `pro`. Audits problem solutions against the standard in `AGENTS.md`.
4. `subject_web_builder`: write tools enabled, limited to `vault/` and `subjects/`.
5. `web_qa_reviewer`: write and command tools enabled. Runs the review gates in `AGENTS.md`.

Delegate role-specific work to these subagents with `invoke_subagent` rather than performing it monolithically in the main agent. Its results must be awaited and coordinated by the orchestrator.

## 1. Notebook scope (NotebookLM)

When using study material from NotebookLM, consult only the **`2ndYear`** notebooks:

| Asignatura | Notebook name | Notebook ID |
| :--- | :--- | :--- |
| Fluid Mechanics | `Fluid Mechanics` | `3080c1f2-5689-4a39-90c3-091d58f39684` |
| Aerospace Materials I | `Aerospace Materials I` | `9b324478-69e9-482c-813c-5709ec031820` |
| Engineering Mechanics | `Engineering Mechanics` | `473546c3-3716-4426-b0c4-58de530f91c8` |
| Advanced Maths | `Advanced Maths` | `c27033c3-5a64-403f-a517-5847831aabcb` |
| Business Management | `Business management` | `e691ea81-0acf-4032-98d1-b9e5a7b93d70` |

New second-semester subjects will be added to this table when their notebooks exist.

Do **not** use, cite, or query these 1st-year notebooks unless the user explicitly asks for 1st-year content:
- `Final Exam Prep Chemistry`
- `Final Exam Prep Calculus 2`
- `Physics 2 Final Exam Prep`
- `Engineering Graphics Final Exam Prep`

## 2. Obsidian-first rule (NotebookLM content)

Material taken from NotebookLM notebooks is structured in `vault/` first (see the pipeline in `AGENTS.md`), then used for web pages.

## 3. Gemini agent definitions

Short descriptions for the Gemini subagent registration in section 0. The shared responsibilities are in `AGENTS.md`.

- **`source_researcher`:** ingest and index official PDFs, slides, and problem sheets from `sources/`. Extract definitions, LaTeX formulas, problem statements, boundary conditions, and numerical data. Output clean Markdown without inventing anything.
- **`aerospace_pedagogue`:** write theory with maximum pedagogical clarity and analytical rigour. Solve problems step by step, following the 4-phase method in `AGENTS.md`.
- **`problem_step_mentor`:** check that every solution, class exercise, and exam follows the problem-solving standard: justify each equation before using it, cite its source, connect coordinate changes to their change-of-basis matrices, leave no algebraic skips, and develop every derivative and integral explicitly.
- **`subject_web_builder`:** build clean, readable study pages in `subjects/` with editorial typography, KaTeX, a working dark/light theme, and the back-link `../../../index.html`.
- **`web_qa_reviewer`:** audit relative links, KaTeX delimiter balance, responsive layout, and git state. Commits and pushes are governed by the git rules in `AGENTS.md`.

## 4. Scope notes

- The simulator agent is removed and inactive by the user's decision; the effort goes into the solidity of theory and analysis. No interactive simulators are built.
