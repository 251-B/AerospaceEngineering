# Aerospace Engineering — Claude Code Autonomous Operating Framework

## 1. Project Overview & Multi-Agent Architecture

This repository contains the study portal, Obsidian second brain (`vault/`), and academic materials for the 2nd Year BSc in Aerospace Engineering at Universidad Carlos III de Madrid (UC3M).

The workspace operates under an **Autonomous Triggering Engine** combining specialized subagents, Claude Code Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`), and installed high-performance plugins (`superpowers`, `context-mode`, `claude-mem`, `buildomator`, `skill-creator`).

---

## 2. Autonomous Triggering Pipeline & Decision Flow

Whenever the user submits a message, the AI **MUST NOT** jump straight into ad-hoc editing. It must automatically follow this **5-Stage Autonomous Execution Pipeline**:

```
[ User Prompt Received ]
         │
         ▼
[ Stage 1: Intent & Scope Classification ] ──────────┐
         │                                            │
         ▼                                            ▼
[ Stage 2: Memory & Context Shielding ]       [ Triggers Detected ]
  • claude-mem: recall past decisions           • Bug / Error ──► superpowers:systematic-debugging
  • context-mode: sandbox file scans            • New Feature ──► superpowers:brainstorming + bm:plan-phase
         │                                      • Theory Note ──► source-researcher ──► aerospace-pedagogue
         ▼                                      • Problem Set ──► problem-step-mentor (4-Phase Protocol)
[ Stage 3: Autonomous Routing & Execution ]     • Web Page    ──► subject-web-builder (Obsidian-First)
  • Single Agent / Subagent vs. Agent Teams     • Skill Work  ──► skill-creator + superpowers:writing-skills
  • Enforce Academic Standards (English, SI)    • Sprint/Milestone ──► Agent Teams + buildomator
         │
         ▼
[ Stage 4: Mandatory Closing Verification Gate ]
  • REVIEW (Single-task completion): KaTeX delimiters, relative links (../../../index.html), YAML frontmatter
  • ULTRAREVIEW (Milestone / Exam completion): 4-Dimensional adversarial audit (algebraic proof, Barrow rule, SI units)
         │
         ▼
[ Stage 5: State Stash & Completion ]
  • claude-mem: persist key findings / architectural decisions (compact summary, <100 tokens)
```

---

## 3. Autonomous Decision Matrix

Classify the user prompt against the table below to trigger the appropriate tool chain without waiting for explicit instructions:

| Detected Trigger / Keywords | Primary Plugin / Workflow | Assigned Role / Skill | Invariant Rules & Expected Deliverables |
| :--- | :--- | :--- | :--- |
| **"Error", "bug", "falla", "broken math", "404", "no compila"** | `superpowers:systematic-debugging` | `web-qa-reviewer` | 1. Reproduce error.<br>2. Formulate falsifiable hypothesis.<br>3. Fix root cause (never patch symptoms blindly).<br>4. Test and verify live. |
| **"Crea una página", "diseña", "nuevo tema", "nueva feature"** | `superpowers:brainstorming` + `bm:plan-phase` | `subject-web-builder` / `aerospace-pedagogue` | Socratic clarification before writing files. Always check Obsidian First (`vault/`) before creating HTML in `subjects/`. |
| **"Busca en los PDFs", "qué dice la cátedra", "temario", "fórmulas"** | `context-mode` (`ctx_search`, `ctx_execute`) | `source-researcher` | Read local PDFs in `sources/`. Zero hallucinations. Extract exact math in LaTeX and raw numerical data. Keep context lean. |
| **"Explica la teoría", "desarrolla el tema", "apuntes"** | `aerospace-pedagogue` | `aerospace-study-team` | Derive equations from first principles in academic English. Cite official notes. Write notes to `vault/<asignatura>/` using templates. |
| **"Resuelve el problema", "ejercicio", "hoja de problemas", "examen"** | `problem-step-mentor` | 4-Phase Protocol | **Strict 4 Phases:**<br>1. Hypotheses & degrees of freedom.<br>2. Frames & change-of-basis matrix $[{}_0 R_1]$.<br>3. Continuous derivation: explicit chain rule $\frac{d}{dt}f(u)$, differentials $du$, and Barrow's rule with limits.<br>4. SI units and asymptotic limits. |
| **"Maqueta la web", "pasa a HTML", "estilo", "tema oscuro"** | `subject-web-builder` | Frontend Builder | Obsidian is source of truth. Include KaTeX CDN, dark/light switch (`localStorage('ae_theme')`), return link `../../../index.html`. |
| **"Haz todo el tema", "sprint paralelo", "desarrollo completo"** | Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) | `claude-agents` | Spawn 3–5 teammates with distinct scopes (`vault/`, `teoria/`, `problemas/`). Communicate via `SendMessage`. Coordinate shared tasks. |
| **"Revisa lo hecho", "review", cierre de tarea unitaria** | `review-ultrareview` (Mode: `review`) | `web-qa-reviewer` | Run standard checklist: KaTeX delimiters, `../../../index.html` link, YAML frontmatter, clean scratches. |
| **"Ultrareview", "auditoría profunda", fin de capítulo/examen** | `review-ultrareview` (Mode: `ultrareview`) | Multi-Agent Adversarial Gate | 4-Dimension audit: algebraic step completeness, chain rule, Barrow integration, SI dimensions, sources cross-check. |
| **"Crea una skill", "evalúa la skill", "optimiza el prompt de la skill"** | `skill-creator` | `superpowers:writing-skills` | Draft `SKILL.md` frontmatter, run test cases with `run_eval.py`, run variance analysis with `improve_description.py`. |
| **"Busca en el repositorio", "cuántos archivos hay", "revisa logs"** | `context-mode` (`ctx_execute`) | Context Preservation | Never dump raw grep/find outputs into context. Execute sandboxed scripts to filter and report summary counts. |
| **Session resume, reconnection, past task context** | `claude-mem` | Auto-Memory | Query and integrate recorded observations and past architectural milestones. |

---

## 4. Task Completion Protocols: `review` and `ultrareview`

### A. Protocol: `review` (Standard Task Gate)
Runs automatically upon completing any single problem, theory note, web page, or fix:
1. **KaTeX Check:** Validates delimiter parity ($...$ and $$...$$). No raw LaTeX errors.
2. **Relative Links:** Verifies that back-links in `subjects/` point to `../../../index.html`.
3. **Language Standard:** 100% academic English.
4. **Frontmatter:** YAML header complete in `vault/` notes.
5. **Memory Stash:** Records 1-2 sentence completion note into `claude-mem`.

### B. Protocol: `ultrareview` (Deep Adversarial Audit)
Runs when closing full chapters, problem sheets, exam prep sets, or upon user request:
1. **Algebraic & Calculus Proof (`problem-step-mentor`):** Zero algebraic skips. Every chain rule $\frac{d}{dt}f(u) = \frac{df}{du}\dot{u}$, substitution differential $du$, and Barrow limit substitution explicitly shown.
2. **Frames & Orthonormality:** Rotation matrices $[{}_0 R_1]$ verified ($\det R = 1$, $R R^T = I$).
3. **Dimensional Homogeneity:** Dimensional check of every term in SI units.
4. **Official Sourcing (`source-researcher`):** Strict verification against official PDFs in `sources/`.
5. **Web & Layout (`web-qa-reviewer`):** Theme persistence (`localStorage('ae_theme')`), responsive mobile/tablet layout, and zero JS console errors.

---

## 5. Token Economy, Prompt Cache Optimization & Memory Preservation

To prevent context exhaustion, minimize latency, and guarantee high cost efficiency:

1. **Prompt Cache Stability:**
   - Keep system instructions, agent definitions, and skill frontmatter static and invariant.
   - Do NOT inject dynamic timestamps or volatile metadata into initial prompt prefixes.
2. **Context Window Shielding (`context-mode`):**
   - Never dump hundreds of lines of source PDFs, logs, or directory trees into the chat.
   - Use `ctx_execute` (Node, Python, PowerShell) to run filters and parsers in a sandbox, extracting only relevant summaries.
   - Use `ctx_search` for targeted semantic and BM25 queries.
3. **Memory Persistence (`claude-mem`):**
   - Record resolved questions, verified formulas, and established frames in `claude-mem`.
   - On resuming sessions, fetch the memory summary (<100 tokens) rather than re-reading thousands of tokens of historical transcripts.
4. **Concise Response Discipline:**
   - When files are created or modified on disk, **DO NOT** repeat the entire file contents in the chat response. Provide a clickable link, a diff summary, and key rationale.
   - Keep Agent Teams strictly between 3–5 members, limit tasks to 5–6 per teammate, and invoke graceful shutdown immediately upon completion.
