---
subject: "Repository"
tags:
  - repository
  - tool
  - testing
source: "tools/tests/"
---

# Tool - Test suite

## Purpose

Runs the unit and behavioural tests for the scripts in `tools/`, the design tokens in `assets/css/tokens.css`, and the theme and reading-surface behaviour of `assets/js/theme.js`.

## Command

`python -m unittest discover -s tools/tests`

## Contents

- 13 test modules in `tools/tests/` and 176 `def test_` functions (counted with grep). The largest are `tools/tests/test_audit_portal.py` (50), `tools/tests/test_vault_lint.py` (38), `tools/tests/test_source_links.py` (18) and `tools/tests/test_sources_manifest.py` (14).
- Harness pages used by the browser tests: `tools/tests/surface_harness.html`, `tools/tests/surface_pages_harness.html` and `tools/tests/theme_harness.html`.

## Browser and skip behaviour

`tools/tests/test_render_check.py`, `tools/tests/test_surface.py` and `tools/tests/test_theme.py` need a Chromium-based browser and are skipped without one. `tools/tests/test_sources_manifest.py` is skipped when `sources/cuatrimestre-1/` is absent.

## Read and write behaviour

Fixtures are written into temporary directories. Some tests read real repository files, such as `index.html` and `assets/css/tokens.css`, or run the `--check` modes of the generators. The test modules contain no write to those real files.

## When to run

Before closing any task that changed a tool, its configuration or the pages it generates. [[Rules - AGENTS.md]] requires the tests to pass for a task to be closed.

## Related

[[Repository MOC]] · [[Tool - vault_lint]] · [[Tool - audit_portal]] · [[Tool - build_pdfs]] · [[Tool - render_check]]
