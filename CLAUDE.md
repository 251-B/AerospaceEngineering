# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. Shared rules are in `AGENTS.md`, imported below.

@AGENTS.md

## Claude Code operating framework

The workspace operates under an **Autonomous Triggering Engine** combining specialised subagents, Claude Code Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`), and installed plugins (`superpowers`, `context-mode`, `claude-mem`, `bm`, `skill-creator`).

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
  • Enforce Academic Standards (English, SI)    • Sprint/Milestone ──► Agent Teams + bm
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

### Mandatory closing review (`review-ultrareview`)

Whenever a task changes the repository or the portal (a file created, edited or deleted in `vault/`, `subjects/`, `assets/`, `tools/`, `sources/` or `index.html`, including fixes, new pages and new problems), Claude runs the `review-ultrareview` skill before reporting the task as done, without waiting for the user to ask for it:

- **`review` mode** for a single unit of work (one problem, note, page, fix or small change).
- **`ultrareview` mode** when the work closes a chapter, problem sheet, exam, refactor or milestone, or when the user asks for it.
- Run the skill's checklist together with the repository gates listed in `AGENTS.md` (`vault_lint`, `audit_portal`, `render_check` on edited pages, tests). Fix every finding, re-verify it, and then run the gates again.
- The final message states the outcome: what passed, what failed, what was skipped and why. If a check cannot run here (for example, a CDN or font is blocked), say so explicitly and do not present the task as closed.
- Read-only work (answering questions, reading sources without editing anything) does not trigger this rule.

### Mandatory commit and push

Every task that changes files ends with a commit and a push to `origin`, without waiting for the user to ask. Claude stages only the files of its task, uses a `type(scope): summary` message, and leaves no changes uncommitted. Claude pushes to the branch the session names; when none is named, it pushes to `main`.

## Problem Bank and Exam Simulator (per subject; pilot: Business Management)

These rules apply to every session that builds or changes a subject's Problem Bank or Exam Simulator. They extend the web page rules of `AGENTS.md`; where the two meet, the reconciliation below is binding.

### Two independent tabs

- Each subject keeps the **Problem Bank** and the **Exam Simulator** as two separate pages, never merged into one: `subjects/<subject>/problemas/index.html` (Problem Bank) and `subjects/<subject>/simulator/index.html` (Exam Simulator), a section of its own.
- Every page of the subject shows the same tab strip, in this order: `📘 Theory` (`../teoria/index.html`), `🧩 Problem Bank` (`../problemas/index.html`), `⚡ Exam Simulator` (`../simulator/index.html`), `📂 Official PDFs` (`../sources/index.html`). The current page's tab carries `aria-selected="true"` (or `aria-current="page"` on links).
- Reconciliation with the side-menu rule: the tab strip lives **inside `<main>`, below the header**, with class `subject-tabs` and `role="tablist"`. The header still links only to `../../../index.html`, and the strip never uses the forbidden classes (`pill-nav-bar`, `subchapter-nav-bar`, `pills-bar`, `quick-jump`, `quick-nav`) or `class="tabs"` (`tools/tests/test_sidebar.py`).
- The simulator never lives in `exams/index.html`: that page belongs to `tools/build_sources_pages.py` (official exam PDFs) and is rewritten whenever exam PDFs exist. The `simulator/` section is added to `tools/build_nav.py` (side menu) and gets its own card entry on the root `index.html`.

### Visual style (clone, never invent)

- Tokens from `assets/css/tokens.css`: `--bg-primary`, `--bg-secondary`, `--bg-card`, `--bg-card-hover`, `--bg-input`, `--border-subtle`, `--border-card`, `--text-primary`, `--text-secondary`, `--text-muted`, `--shadow-card`, `--radius-sm|md|lg|xl`, `--transition-fast|medium`, and the subject accent (`--accent-business`, `--neon-business` in dark). Reading surfaces use the `--study-*` variables of `assets/css/study-surface.css`, so the six reading palettes keep working and every text stays AAA.
- Fonts: Newsreader (body), Abril Fatface (display headings), JetBrains Mono (figures, code, timers), from Google Fonts.
- Cards: the existing `problem-card` / `problem-box` containers (one per problem, so `audit_portal` can count them), statements in `.problem-statement-box`, solutions in phase blocks (so `ask-ai.js` splits them). Filters and segmented controls reuse the root `semester-tabs` pattern (`role="tablist"`, `role="tab"`, `aria-selected`); badges reuse `area-badge`.
- Dark/light through `assets/js/theme.js` only (`#themeToggle`, key `ae_theme`); no inline theme code.
- Keyboard shortcuts on the Problem Bank and the Simulator (new; the portal had none): `T` toggles the theme via `AETheme.toggle()`, `/` focuses the search box, `Esc` closes the open panel or clears the search, `?` opens a shortcuts help dialog. They are ignored while focus is in an input, textarea or contenteditable, and never fire with Ctrl/Alt/Meta held.
- Progress and history in `localStorage` under keys that never contain "theme" (`ae_bm_progress`: per-item status `mastered` | `review` | `pending`; `ae_bm_exams`: simulator history), always wrapped in try/catch, with the page still working when storage is blocked.
- The simulator is DOM forms and a timer only: no `<canvas>`, no Three.js (the "no interactive simulators" rule targets physics simulators). Print view through a page `@media print` block; `assets/css/print.css` is not touched.

### Problem banks: real structural variety

- A bank is a hand-written, fully solved static set, not a template with random numbers. Items of one archetype must differ in how the data are given (unordered list of items, statements with gaps and target ratios, a narrative with no table, two-year comparisons), in the unknowns asked for, and in the line of reasoning, not only in the figures.
- Every item has `id`, `category` (`short_theory_case` 2.0 pts | `extra_practice_problem` 4.0 pts), `archetype`, `unit`, `title`, `difficulty` (1–3), `points`, `time_minutes`, `tags`, `statement_html`, and `subquestions[]` with `prompt_html`, `hint_html`, `checkpoint_html` (key figures for problems, concept checklist for cases) and `solution_html`. Subquestion points add up to the item's points.
- Accounting tables must balance (Assets = Equity + Liabilities; the income statement cascade EBITDA → EBIT → EBT → Net income). Use the course's terms and unit (`m.u.`) and its sign and ordering conventions (non-current before current assets; equity, non-current then current liabilities).
- Content integrity still applies: items written for the bank are practice material, labelled as such ("Practice item, not an official exercise"), and anything the course PDFs do not define (three-section cash-flow statement, working capital, current ratio, ROA/ROE definitions) is marked **extension** with its definition stated. The course's own "cash flow" is the cash-account reconciliation (initial cash + collections − payments, `T3_Additional_SOLUTIONS.pdf`).
- Obsidian first: every bank item is one note in `vault/<subject>/Problem Bank/` (`Problem - Bank Pnn - ...` for problems, `Problem - Bank Cnn - ...` for theory cases), indexed by `Problem Set - <Subject> Problem Bank`. `python tools/build_problem_bank.py` turns them into `subjects/<subject>/data/problems.json` (and `problems.js`, the same data for pages opened from disk); `--check` fails when the JSON is stale. Never edit the JSON by hand. Bank cards of official exercises do not copy their solution: they embed the sections of the solved note with Obsidian heading embeds (`![[Problem - T3 Extra 2 - ...#Step 2. ...]]`), which the tool resolves.
- The exam structure lives in `subjects/<subject>/data/exam-blueprint.json` (Business Management Midterm 1: 3 short theory cases × 2.0 + 1 Extra Practice problem × 4.0 = 10.0, 90 min). The simulator reads it; never hard-code the structure in the page.

## Claude Code specifics

- Subagents are defined in `.claude/agents/` (`source-researcher`, `aerospace-pedagogue`, `problem-step-mentor`, `subject-web-builder`, `web-qa-reviewer`). Delegate to them when the task matches a role; work directly when it is small.
- Project skills live in `.claude/skills/` (`review-ultrareview`, `aerospace-study-team`, `claude-agents`, `skill-creator`, `humanizer`). `humanizer` rewrites prose in the author's voice; it must not touch derivations, formulas, or results. Use `review-ultrareview` for chapter- or exam-level audits.
- `.claude/settings.json` enables `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and the plugins `superpowers`, `skill-creator`, `bm`, `context-mode`, `claude-mem`, `humanizer` and `claude-code-setup` (recommends hooks, subagents, skills and MCP servers for this project).
- Agent teams: keep to 3–5 members, limit tasks to 5–6 per teammate, and shut teammates down as soon as they finish.
- Ignore `define_subagent` / `manage_subagents` instructions if you find them elsewhere; they belong to the Gemini setup in `GEMINI.md`.
- Token compression (optional, per machine): install with `pip install "headroom-ai[all]"` and register the MCP server with `headroom mcp install` (tool `headroom_retrieve`, shown as `mcp__headroom__headroom_retrieve`). To run a session through the compression proxy, use `headroom wrap claude` instead of `claude`. Check the setup with `headroom mcp status`.
- `task-observer` (meta-skill from `rebelytics/one-skill-to-rule-them-all`) is bundled in `.claude/skills/task-observer/` and `.agents/skills/task-observer/`; keep both copies identical, as with the other project skills.

## Ask AI prompt: repository links and location

`assets/js/ask-ai.js` (`buildPrompt`, fed by `context()`) opens every prompt with links, not with summaries of the theory: nothing about a subject's content is hard-coded in the script, so a new topic or subject needs no change there beyond the steps below.

- Header: portal URL `https://251-b.github.io/AerospaceEngineering/`, subject name (`SUBJECTS` map, keyed by the slug read from the path), the production URL of the current page (`portalUrl()`: the `subjects/...` part of the path appended to the portal URL, so a local copy still points to the live site; `#id` of the problem card or nearest heading when it has one), and the URLs of that subject's `teoria/index.html` and `problemas/index.html`.
- Location block: on a problem page, `Problema <number> — "<title>", Apartado <a)>, correspondiente a la Unidad N — <page title>` (`cardNumber`, `cardName`, `partLabel`: the last `a)`/`(b)`/`Part (c)` label before the selection inside the card); on a theory page, `Unidad N — <page title> — Sección: "<nearest h2/h3>"`. `N` comes from the file name `topic-N-*.html`. The selected fragment goes in with formulas as the LaTeX of the KaTeX `annotation[encoding="application/x-tex"]`.
- Guidelines (Spanish, fixed text): open the URLs, take data and derivations from that page, copy the repository's terminology, notation, sign convention and step-by-step style, and fall back to the pasted material when the links cannot be opened. The statement and reference solution are still pasted below as `# Material` (needed for the Socratic and "check my attempt" tasks), followed by `# Task`, `[MI PREGUNTA]` and `# How to answer`.
- Adding a subject: add its slug to `SUBJECTS`. Adding a topic page needs nothing if it follows `topic-N-*.html`, loads `ask-ai.js` and keeps `problem-card` markup and h2/h3 headings. If a new page family labels its sub-questions differently from `a)`, extend `PART_RE`. If the portal moves, change `PORTAL`.
- Scope: the script loads on `teoria/` and `problemas/` topic pages only (`audit_portal` `missing-ask-ai`); the index and generated `exams/`/`sources/` pages do not carry it.
