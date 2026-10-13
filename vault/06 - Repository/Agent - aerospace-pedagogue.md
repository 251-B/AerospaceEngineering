---
subject: "Repository"
tags:
  - repository
  - agent
source: ".claude/agents/aerospace-pedagogue.md"
---

# Agent - aerospace-pedagogue

## Role

Aerospace engineer and academic pedagogue for the second year of the UC3M BSc. It writes theory from first principles, cites the official course sources, and co-audits derivations during an ultrareview.

## Tools granted

`Read`, `Grep`, `Glob`. No write, edit or shell tool is granted. The frontmatter also sets model and effort options, which this note does not reproduce.

## Scope

The body asks it to write notes to `vault/<subject>/` and to update the subject MOC. Its granted tools cannot write files, so that work needs another agent or the main session. [[Rules - AGENTS.md]] describes the role as read-only and, in the same table, as writing theory. The two statements conflict, and this note does not reconcile them.

## Rule it enforces

- Every concept is derived from conservation laws or theorems, with each result cited to a course file and page.
- Academic English, with KaTeX `$...$` inline and `$$...$$` for display equations.
- Obsidian first: the vault note comes before any web page.

## Related

[[Repository MOC]] · [[Agent - source-researcher]] · [[Agent - problem-step-mentor]] · [[Tool - build_topic_pages]]
