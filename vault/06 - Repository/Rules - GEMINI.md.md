---
subject: "Repository"
tags:
  - repository
  - rules
source: "GEMINI.md"
---

# Rules - GEMINI.md

## Scope

`GEMINI.md` at the repository root holds the Gemini-specific instructions. It assumes that `AGENTS.md` is read first, and it adds only what is specific to Gemini: session setup, NotebookLM scope and the subagent registration.

## Sections

0 Mandatory session initialization, 1 Notebook scope (NotebookLM), 2 Obsidian-first rule, 3 Gemini agent definitions, 4 Scope notes.

## Operative rules

- At the start of each session, check that the five subagents are registered, and define any that are missing before the user's task.
- Delegate role-specific work to the subagents rather than doing it all in the main agent, and let the orchestrator await their results.
- NotebookLM: consult only the `2ndYear` notebooks listed in the file. The four first-year exam-prep notebooks are excluded unless the user asks for them.
- NotebookLM material is structured in `vault/` before it is used on the web.
- The Gemini subagent names use underscores. They correspond to the Claude agent notes: [[Agent - source-researcher]], [[Agent - aerospace-pedagogue]], [[Agent - problem-step-mentor]], [[Agent - subject-web-builder]] and [[Agent - web-qa-reviewer]].
- The simulator agent has been removed by the user's decision, so no interactive simulators are built.
- Commits and pushes follow the git rules in [[Rules - AGENTS.md]].

## Related

[[Rules - AGENTS.md]] · [[Rules - CLAUDE.md]] · [[Agent - web-qa-reviewer]] · [[Agent - subject-web-builder]] · [[Repository MOC]]
