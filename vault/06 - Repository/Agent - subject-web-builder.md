---
subject: "Repository"
tags:
  - repository
  - agent
source: ".claude/agents/subject-web-builder.md"
---

# Agent - subject-web-builder

## Role

Frontend web developer and Obsidian vault architect. It builds study pages in `subjects/` and Markdown notes in `vault/`.

## Tools granted

`Read`, `Grep`, `Glob`, `Edit`, `Write`. It has no shell tool. The frontmatter also sets model and effort options, which this note does not reproduce.

## Scope

The body limits its work to `vault/<subject>/` and `subjects/<subject>/`. The frontmatter does not restrict paths, so the limit is an instruction, not a tool setting. [[Rules - GEMINI.md]] applies the same limit to its Gemini counterpart.

## Rule it enforces

- The vault note comes first, then the web page.
- The theme is handled only by `assets/js/theme.js` with the `ae_theme` key, with no inline theme code and a `#themeToggle` button.
- Back-link `../../../index.html`, no laboratory pages, and no canvas or Three.js.
- Discrepancy: the body names Newsreader and Inter as the typefaces. [[Rules - AGENTS.md]] names Newsreader, Abril Fatface and JetBrains Mono. The two lists are not reconciled here.

## Related

[[Repository MOC]] · [[Agent - web-qa-reviewer]] · [[Tool - audit_portal]] · [[Tool - build_topic_pages]] · [[Rules - CLAUDE.md]]
