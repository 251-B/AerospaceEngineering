---
subject: "Repository"
tags:
  - repository
  - tool
  - web
source: "tools/render_check.py"
---

# Tool - render_check

## Purpose

Renders pages in headless Edge or Chrome with the real KaTeX auto-render. It reports KaTeX error elements, leftover `$$` delimiters and inline math that stayed unrendered. Unlike [[Tool - audit_portal]], which checks delimiter parity, this tool catches undefined macros and bad syntax.

## Command

`python tools/render_check.py PAGE [PAGE ...]` or `python tools/render_check.py --all`

`--all` covers `index.html` and every `subjects/**/*.html` page.

## Exit codes

- 0: every page is clean.
- 1: at least one page has KaTeX errors, leftover `$$`, raw inline math or a failed render.
- 2: no Chromium-based browser was found.

## Read and write behaviour

Read-only with respect to the repository. Each page is dumped with `--dump-dom` in a temporary browser profile. The pages load KaTeX from the CDN, so network access is needed. Unlike [[Tool - build_pdfs]], this tool has no local-KaTeX option.

## When to run

- On every page edited in a task (closing gate, see [[Rules - AGENTS.md]]).
- Use `--all` for a chapter-level or full audit.

## Related

[[Repository MOC]] · [[Agent - web-qa-reviewer]] · [[Tool - Test suite]]
