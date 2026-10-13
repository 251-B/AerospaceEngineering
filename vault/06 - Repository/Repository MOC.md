---
subject: "Repository"
tags:
  - repository
  - moc
source:
  - "AGENTS.md"
  - "CLAUDE.md"
  - "GEMINI.md"
  - "tools/README.md"
  - ".claude/agents/"
  - "tools/"
---

# Repository MOC

## Purpose

Map of content for the repository's own tooling, agents and rules. The study content lives in the other vault folders. This folder documents how that content is generated, checked and maintained.

## Notes

| Note | Kind | Purpose |
| :--- | :--- | :--- |
| [[Rules - AGENTS.md]] | Rules | Shared rules for every agent: architecture, web and problem standards, review gates and git. |
| [[Rules - CLAUDE.md]] | Rules | Claude Code framework: triggering pipeline, decision matrix, subagents and agent teams. |
| [[Rules - GEMINI.md]] | Rules | Gemini session setup, NotebookLM scope and subagent definitions. |
| [[Agent - aerospace-pedagogue]] | Agent | Writes theory from first principles, cited to the sources. |
| [[Agent - problem-step-mentor]] | Agent | Enforces the four-phase method on problem solutions. |
| [[Agent - source-researcher]] | Agent | Read-only extraction of formulas and statements from `sources/`. |
| [[Agent - subject-web-builder]] | Agent | Builds `subjects/` pages and `vault/` notes. |
| [[Agent - web-qa-reviewer]] | Agent | Runs the review gates and manages git. |
| [[Tool - vault_lint]] | Tool | Lints `vault/` notes; fixes links and ampersands with `--fix`. |
| [[Tool - audit_portal]] | Tool | Static gate for `index.html` and `subjects/` pages. |
| [[Tool - build_topic_pages]] | Tool | Generates six theory pages from vault notes and figures. |
| [[Tool - build_problem_pages]] | Tool | Generates the two Business Management Topic 3 problem pages. |
| [[Tool - source_links]] | Tool | Adds deep links to the official PDFs. |
| [[Tool - build_sources_pages]] | Tool | Generates the sources and exams index pages per subject. |
| [[Tool - sources_manifest]] | Tool | Regenerates `assets/data/sources.js` from `sources/`. |
| [[Tool - build_pdfs]] | Tool | Prints theory and problem pages to A4 PDFs. |
| [[Tool - render_check]] | Tool | Renders pages in a headless browser to catch KaTeX errors. |
| [[Tool - vault_rename]] | Tool | Renames vault notes and rewrites their wikilinks. |
| [[Tool - Test suite]] | Tool | Runs the unittest suite under `tools/tests/`. |

## Where the sources of truth are

- `sources/`: the official course material, which is the ground truth for content. It is extracted from, never invented. Its layout is described in `sources/README.md`.
- `vault/`: the Obsidian notes built from `sources/`. They are written first, and the web pages follow.
- `subjects/`: the static HTML study pages. Each one must agree with its vault note. Generated pages are not edited by hand.
- `index.html`: the portal landing page. Its subject badges are audited against the pages on disk.
- Generator settings: `tools/topic_pages.json`, `tools/source_links.json` and `tools/source_anchors.json`. The tool summary is in `tools/README.md`.

## Closing gate

From [[Rules - AGENTS.md]]: 0 errors from vault_lint and audit_portal, a clean render_check on every edited page, a passing `build_pdfs --check`, and passing tests.

## Business Management run order

build_topic_pages, then build_problem_pages, then source_links, then build_pdfs. This order is set in [[Rules - AGENTS.md]].

## Observations

- [[Agent - aerospace-pedagogue]] and [[Agent - problem-step-mentor]] describe writing tasks but are granted only read tools.
- [[Agent - subject-web-builder]] names typefaces that differ from [[Rules - AGENTS.md]].
- Not covered here: `.codex/agents/`, `.agents/skills/` and `.claude/skills/`.
