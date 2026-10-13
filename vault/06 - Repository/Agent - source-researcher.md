---
subject: "Repository"
tags:
  - repository
  - agent
source: ".claude/agents/source-researcher.md"
---

# Agent - source-researcher

## Role

Documentalist and official source extractor. It reads and indexes the course PDFs, lecture slides, syllabus and problem sheets in `sources/`, and returns exact formulas, statements and data.

## Tools granted

`Read`, `Grep`, `Glob`. It is read-only, which matches its role in [[Rules - AGENTS.md]]. The frontmatter also sets model and effort options, which this note does not reproduce.

## Scope

The body limits it to `sources/`. The frontmatter does not restrict paths. The body also asks it to store extracted formulas in claude-mem. No memory tool is listed in the frontmatter, so whether that step is available is not verified.

## Rule it enforces

- Zero hallucinations: nothing that is absent from the official documents may appear in the output.
- Exact LaTeX for formulas, complete problem statements, and explicit boundary conditions and SI data.
- Context shielding: targeted reads and line ranges, not whole-file dumps.

## Related

[[Repository MOC]] · [[Agent - aerospace-pedagogue]] · [[Tool - sources_manifest]] · [[Tool - source_links]] · [[Rules - AGENTS.md]]
