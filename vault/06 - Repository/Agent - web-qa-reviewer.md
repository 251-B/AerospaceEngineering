---
subject: "Repository"
tags:
  - repository
  - agent
source: ".claude/agents/web-qa-reviewer.md"
---

# Agent - web-qa-reviewer

## Role

Quality auditor and technical reviewer. It runs the `review` gate, coordinates `ultrareview` checks on chapters and exams, checks links and KaTeX syntax, and manages the git state.

## Tools granted

`Read`, `Grep`, `Glob`, `Edit`, `Write`, `Bash`, `PowerShell`. It is the only agent in this set with a shell tool. The frontmatter also sets model and effort options, which this note does not reproduce.

## Scope

The frontmatter does not restrict paths. The body covers review and version control across the repository. [[Rules - AGENTS.md]] assigns it commits and pushes to `origin/main` when a task is closed. The body mentions version control but does not name a push.

## Rule it enforces

- The `review` checklist: KaTeX delimiters, back-links, English, YAML frontmatter, subject MOC and index entries, and no scratch files.
- The closing gate: [[Tool - vault_lint]], [[Tool - audit_portal]], [[Tool - render_check]], [[Tool - build_pdfs]] and [[Tool - Test suite]].
- Work isolation: no conflicting overwrites between teammates.

## Related

[[Repository MOC]] · [[Rules - AGENTS.md]] · [[Agent - subject-web-builder]] · [[Agent - aerospace-pedagogue]] · [[Agent - problem-step-mentor]]
