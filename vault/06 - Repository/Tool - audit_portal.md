---
subject: "Repository"
tags:
  - repository
  - tool
  - web
source: "tools/audit_portal.py"
---

# Tool - audit_portal

## Purpose

Static quality gate for the study portal: `index.html` and every `subjects/**/*.html` page. The module also defines `FileIndex` and `Finding`, which [[Tool - vault_lint]] imports.

## Command

`python tools/audit_portal.py [--root DIR] [-v] [--json] [--only a,b] [--skip a,b] [--quiet]`

## Checks

Every finding is an error: `broken-link`, `missing-backlink`, `katex-parity`, `katex-text-ampersand`, `debris`, `spanish-label`, `false-claim`, `lab-reference`, `theme-key`, `badge-drift`, `missing-source-link`, `missing-ask-ai`, `missing-responsive` and `missing-pdf-export`.

`badge-drift` compares the badges on `index.html` with the topic and problem counts on disk, and with the PDF counts from [[Tool - build_sources_pages]].

## Read and write behaviour

Read-only. The script contains no file-writing code. It reads the HTML pages, the subject folders and `sources/` (through `counts()` in `tools/build_sources_pages.py`).

## When to run

- After any change to `index.html` or a page in `subjects/`.
- Closing gate: 0 errors are required. A run with `--only` or `--skip` is for debugging and does not replace the full run.
- Baseline: `tools/README.md` records 424 errors in 47 files at introduction on 2026-10-08, with zero as the goal.

## Related

[[Repository MOC]] · [[Tool - vault_lint]] · [[Tool - render_check]] · [[Tool - source_links]] · [[Agent - subject-web-builder]]
