---
subject: "Repository"
tags:
  - repository
  - rules
source: "AGENTS.md"
---

# Rules - AGENTS.md

## Scope

`AGENTS.md` at the repository root. It holds the shared rules for every AI agent in the repository, Claude Code and Gemini alike. Tool-specific rules sit in [[Rules - CLAUDE.md]] and [[Rules - GEMINI.md]].

## Sections

Purpose, Architecture, Mandatory pipeline (Obsidian first, web second), Language and units, Web page rules, Problem-solving standard (with content integrity), Review protocols, Routing, Agent roles, Token economy and memory, Verification tools, Git, Skills.

## Operative rules

- Content flows from `sources/` to `vault/`, then to `subjects/`, then to `index.html`. No web page exists without its vault note.
- Study text is in English. Units are SI, with a dimensional check.
- Generated files are never edited by hand: the theory, problem, sources and exam pages, the PDF deep links, `assets/data/sources.js`, `assets/pdf/` and `vault/07 - Sources/`.
- Web pages use the back-link `../../../index.html`, KaTeX from the CDN and the `ae_theme` key only. They carry no laboratory material and no interactive simulators. Topic pages carry the Ask AI, PDF and responsive helpers.
- Problems follow the lecturer's order of each subject, with no visible "Phase" labels, no algebraic skips, every sine, cosine and sign justified, deduction figures for every plane and rotation, and each result cites its source.
- Official answers are never matched by adjusting data. A discrepancy gets a warning callout, and extensions are labelled as such.
- The `review` gate runs after any single change. The `ultrareview` gate runs after a chapter, problem sheet or exam.
- Every change that users can see on the portal adds one hand-written entry to `assets/data/updates.js`, which feeds the "What's new" bell, panel and toast: English, plain words, newest first, no laboratory material.
- Closure requires 0 errors from vault_lint and audit_portal, a clean render_check on every page you edited, a passing `build_pdfs --check`, and passing tests, plus the updates entry when users can see the change.
- Only the web_qa_reviewer role commits and pushes to `origin/main`. Other agents do so only when asked. Stage only the relevant files.
- Project skills in `.claude/skills/` and `.agents/skills/` must stay identical.

## Tools and agents this rule refers to

Tools: [[Tool - vault_lint]] · [[Tool - audit_portal]] · [[Tool - render_check]] · [[Tool - build_pdfs]] · [[Tool - build_topic_pages]] · [[Tool - build_problem_pages]] · [[Tool - source_links]] · [[Tool - sources_manifest]] · [[Tool - build_sources_pages]] · [[Tool - build_source_notes]] · [[Tool - vault_rename]] · [[Tool - Test suite]]

Agents: [[Agent - web-qa-reviewer]] · [[Agent - subject-web-builder]] · [[Agent - source-researcher]] · [[Agent - problem-step-mentor]] · [[Agent - aerospace-pedagogue]]

Index: [[Repository MOC]]
