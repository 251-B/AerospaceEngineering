# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. Shared rules are in `AGENTS.md`, imported below.

@AGENTS.md

## Claude Code operating framework

The workspace operates under an **Autonomous Triggering Engine** combining specialised subagents, Claude Code Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`), and installed plugins (`superpowers`, `context-mode`, `claude-mem`, `buildomator`, `skill-creator`).

### Triggering pipeline

Before editing, follow this five-stage pipeline:

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
  • REVIEW (Single-task completion): vault_lint + audit_portal at 0 errors, render_check clean on edited pages, relative links, YAML frontmatter
  • ULTRAREVIEW (Milestone / Exam completion): 4-Dimensional adversarial audit (algebraic proof, Barrow rule, SI units)
         │
         ▼
[ Stage 5: State Stash & Completion ]
  • claude-mem: persist key findings / architectural decisions (compact summary, <100 tokens)
```

### Decision matrix

Classify the prompt against this table and trigger the matching tool chain without waiting for explicit instructions:

| Detected trigger / keywords | Primary plugin / workflow | Assigned role / skill | Invariant rules and expected deliverables |
| :--- | :--- | :--- | :--- |
| **"Error", "bug", "falla", "broken math", "404", "no compila"** | `superpowers:systematic-debugging` | `web-qa-reviewer` | 1. Reproduce error. 2. Formulate falsifiable hypothesis. 3. Fix root cause (never patch symptoms blindly). 4. Test and verify live. |
| **"Crea una página", "diseña", "nuevo tema", "nueva feature"** | `superpowers:brainstorming` + `bm:plan-phase` | `subject-web-builder` / `aerospace-pedagogue` | Socratic clarification before writing files. Check Obsidian first (`vault/`) before creating HTML in `subjects/`. |
| **"Busca en los PDFs", "qué dice la cátedra", "temario", "fórmulas"** | `context-mode` (`ctx_search`, `ctx_execute`) | `source-researcher` | Read local PDFs in `sources/`. Zero hallucinations. Extract exact math in LaTeX and raw numerical data. Keep context lean. |
| **"Explica la teoría", "desarrolla el tema", "apuntes"** | `aerospace-pedagogue` | `aerospace-study-team` | Derive equations from first principles in academic English. Cite official notes. Write notes to `vault/<asignatura>/` using templates. |
| **"Resuelve el problema", "ejercicio", "hoja de problemas", "examen"** | `problem-step-mentor` | 4-phase protocol | 1. Hypotheses and degrees of freedom. 2. Frames and change-of-basis matrix $[{}_0 R_1]$. 3. Continuous derivation: explicit chain rule, differentials, Barrow's rule with limits. 4. SI units and asymptotic limits. |
| **"Maqueta la web", "pasa a HTML", "estilo", "tema oscuro"** | `subject-web-builder` | Frontend builder | Obsidian is source of truth. KaTeX CDN, dark/light switch via `assets/js/theme.js` (key `ae_theme`, no inline theme code), back-link `../../../index.html`. No lab pages. |
| **"Haz todo el tema", "sprint paralelo", "desarrollo completo"** | Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) | `claude-agents` | Spawn 3–5 teammates with distinct scopes (`vault/`, `teoria/`, `problemas/`). Communicate via `SendMessage`. Coordinate shared tasks. |
| **"Revisa lo hecho", "review", cierre de tarea unitaria** | `review-ultrareview` (mode `review`) | `web-qa-reviewer` | Standard checklist from `AGENTS.md`. |
| **"Ultrareview", "auditoría profunda", fin de capítulo/examen** | `review-ultrareview` (mode `ultrareview`) | Multi-agent adversarial gate | Four-dimension audit from `AGENTS.md`, plus sources cross-check. |
| **"Crea una skill", "evalúa la skill", "optimiza el prompt de la skill"** | `skill-creator` | `superpowers:writing-skills` | Draft `SKILL.md` frontmatter, run test cases with `run_eval.py`, run variance analysis with `improve_description.py`. |
| **"Busca en el repositorio", "cuántos archivos hay", "revisa logs"** | `context-mode` (`ctx_execute`) | Context preservation | Never dump raw grep/find output into context. Run sandboxed scripts that filter and report summary counts. |
| **Session resume, reconnection, past task context** | `claude-mem` | Auto-memory | Query and integrate recorded observations and past architectural milestones. |

## Claude Code specifics

- Subagents are defined in `.claude/agents/` (`source-researcher`, `aerospace-pedagogue`, `problem-step-mentor`, `subject-web-builder`, `web-qa-reviewer`). Delegate to them when the task matches a role; work directly when it is small.
- Project skills live in `.claude/skills/` (`review-ultrareview`, `aerospace-study-team`, `claude-agents`, `skill-creator`, `humanizer`). `humanizer` rewrites prose in the author's voice; it must not touch derivations, formulas, or results. Use `review-ultrareview` for chapter- or exam-level audits.
- `.claude/settings.json` enables `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and the plugins `superpowers`, `skill-creator`, `bm`, `context-mode`, `claude-mem` and `humanizer`.
- Agent teams: keep to 3–5 members, limit tasks to 5–6 per teammate, and shut teammates down as soon as they finish.
- Ignore `define_subagent` / `manage_subagents` instructions if you find them elsewhere; they belong to the Gemini setup in `GEMINI.md`.
