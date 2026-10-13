# tools/: quality gates and generators

Pure-stdlib Python 3 (no installs). Run everything from the repository root.

| Tool | Purpose | Exit code |
|---|---|---|
| `python tools/audit_portal.py` | Static gate for `index.html` + `subjects/**/*.html` | 1 if any error |
| `python tools/vault_lint.py` | Lint the Obsidian `vault/` (`--fix` applies the safe fixes) | 1 if any error |
| `python tools/build_topic_pages.py` | Generate the theory pages listed in `tools/topic_pages.json` from their vault notes (sections, tables, callouts, math, `![[attachments/…svg]]` figures from `tools/figures/`, question cards) and apply the PDF deep links; also writes the figure SVGs to `vault/attachments/`; `--check` = fail if a page or figure is stale | 1 if stale (`--check`) |
| `python tools/source_links.py` | Add deep links to the official PDFs (problem statements, topic panel, inline citations) from `tools/source_links.json`; `--check` = fail if stale, `--refresh-anchors` = re-resolve labels with `pdftotext`, `-v` = list unresolved citations | 1 if stale (`--check`) or a problem card has no PDF page |
| `python tools/build_sources_pages.py` | Generate each subject's `sources/index.html` (Theory & exercise PDFs by unit) and `exams/index.html` (exams by partial/final, newest year first, identical copies listed once) from the same scan; `--check` = fail if stale | 1 if stale (`--check`) |
| `python tools/build_pdfs.py` | Print every theory and problem page (and each problem card) to A4 PDFs in `assets/pdf/` with headless Edge/Chrome and `assets/css/print.css`; reprints only what changed (hashes in `assets/pdf/manifest.json`); `--check` = fail if stale (no browser), `--katex DIR` = local KaTeX, `--only`, `--force`, `--jobs` | 1 if stale (`--check`) or a print failed |
| `python tools/sources_manifest.py` | Regenerate `assets/data/sources.js` from `sources/cuatrimestre-1/` (`--check` = fail if stale) | 1 if stale (`--check`) |
| `python tools/build_source_notes.py` | Write one generated note per file under `sources/` into `vault/07 - Sources/` (path, kind, size, status, and the vault notes that reference it) plus one index per subject; settings in `tools/source_notes.json`; `--check` = fail if a note is missing, stale or orphaned | 1 if stale (`--check`) or a file that is not generated blocks a write |
| `python -m unittest discover -s tools/tests` | Test suite for all of the above + `tokens.css` + `theme.js` (headless Edge/Chrome) | 1 on failure |

Common flags for both linters: `-v` list every finding, `--json`, `--only a,b`, `--skip a,b`, `--quiet`.

## audit_portal.py checks

`broken-link` (case-sensitive, like GitHub Pages) · `missing-backlink` · `katex-parity` ·
`katex-text-ampersand` · `debris` (scratch "Wait", U+FFFD, `??` headers, raw markdown) ·
`spanish-label` · `false-claim` ("fully verified", "zero hallucinations") ·
`lab-reference` (labs are not on the web) · `theme-key` (only `ae_theme`) · `badge-drift` ·
`missing-source-link` · `missing-ask-ai` / `missing-responsive` (every `teoria/` and `problemas/` topic page loads `assets/js/ask-ai.js` and `assets/css/responsive.css`).

**Markup contracts the checks rely on**

- Hub cards: `<article data-subject="<slug>">` containing `<a href=".../teoria|problemas/...">` with a
  `<span class="area-badge ...">3 topics</span>` / `38 prob.`. A "topic" is a distinct `topic-N` file number.
- A solved problem is one `class="problem-card"` (or `problem-box`) element on a `problemas/*.html` page.
  New pages should use `problem-card`.

## vault_lint.py

Errors: `no-frontmatter`, `backticked-wikilink` (fixable), `text-ampersand` (fixable), `broken-wikilink`,
`dangling-source-path`. Warnings: `frontmatter-keys`, `spanish-note`.
`--fix` is idempotent, skips fenced code, preserves CRLF/accents, and skips non-UTF-8 files.
Excluded folders: `.obsidian`, `.trash`, `Templates`, `attachments`.
Known limit: a link whose alias ends in `]` (`...[101]]]`) is ambiguous and must be fixed by hand.

## Shared assets

- `assets/css/tokens.css`: design tokens, verbatim from the original `index.html`.
- `assets/js/ask-ai.js` + `assets/css/ask-ai.css`: "Ask AI" (Claude or Gemini) on selected text and on every problem card (prefilled link or copied prompt; no API).
- `assets/js/theme.js`: load synchronously in `<head>`. Single key `ae_theme`; migrates `aero-portal-theme`
  and `theme`; default dark; syncs tabs; `window.AETheme`; wires `#themeToggle` / `#themeLabel`.
- `assets/js/focus-lab.js` + `assets/css/focus-lab.css`: "Focus Lab" study sound (Web Audio synthesis: binaural,
  isochronic, brown/pink noise), loaded on every page by `theme.js`; key `ae_focus_lab`; tested by `tests/test_focus_lab.py`.
- `assets/data/sources.js`: `window.AE_SOURCES` = official PDFs (160 files) per subject / unit / category
  (`teoria`, `slides`, `problemas`, `examenes`, `schedule`). **Laboratory material is never included.**
  Hrefs are repo-root-relative and URL-encoded; prefix them with the page's relative path to the root.

## Baseline when these tools were introduced (2026-10-08)

`audit_portal.py`: 424 errors in 47 files (14 broken links, 196 debris, 77 Spanish labels, 5 false claims,
8 lab references, 122 legacy theme keys, 2 badge drifts).
`vault_lint.py`: 989 errors / 105 warnings (915 backticked links and 26 ampersands are auto-fixable).
The goal of the remediation phases is zero errors from both.
