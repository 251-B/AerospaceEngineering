# Account Calendar Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A personal term calendar for signed-in readers: official class plans per subject and group, the student's own timetable, missed / not-held classes, labs, exams, and "what you will do" with portal links per session.

**Architecture:** Official plans live in vault notes and are compiled by `tools/build_timetable.py` into `assets/data/timetable.js`. A pure, DOM-free module `assets/js/calendar-core.js` turns that data plus the student's `ae_calendar` record into dated occurrences and merges two records for cloud sync. `account/calendar.html` + `assets/js/account-calendar.js` render it; `account.js` syncs the key; the dashboard shows "Next class".

**Tech Stack:** vanilla JS (ES5 style like `account.js`, IIFE, no build), Python 3 stdlib for the tool, `unittest` + headless Edge/Chrome harness (`--dump-dom`) for browser tests.

**Spec:** `docs/superpowers/specs/2026-11-19-account-calendar-design.md`

## Global Constraints

- Storage key `ae_calendar` (never a key containing "theme"); every read/write in try/catch; the page works with storage blocked.
- No emojis, no `<canvas>`, no inline theme code; theme via `assets/js/theme.js` only.
- Fonts Newsreader / Abril Fatface / JetBrains Mono; colours from `tokens.css` and `--study-*`; every text AAA on every reading palette.
- Lab rows: title, date, hour, room only. No link to any lab material; the tool fails on a lab row with a portal link.
- Session text transcribed from `sources/` with the subject's `source`; nothing invented. Maths rows are a past log (`basis: "log"`).
- Term 2026-09-07 to 2026-12-18. Non-teaching days only from sources: 2026-10-09 (Materials: bank holiday), 2026-10-14 (Materials: no lecture; Materials only).
- Session ids: `em-s<N>`, `em-lab<N>`, `em-quiz<N>`, `mat-s<N>`, `mat-test<N>`, `mat-lab<N>`, `am-l<N>`.
- Commit messages `type(scope): summary` ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; stage only task files.

## Review Focus

1. A student with no group chosen yet: calendar opens `My groups`, shows nothing broken, Next class card says "Choose your groups".
2. Custom slots with no plan (Fluids, Business): occurrences appear every week; no content, "Add what was covered" works.
3. Two devices: an event deleted on one does not come back after sync (tombstone).
4. A week with zero classes (after 18 Dec) and the month view across term end: empty state, no errors.
5. Storage blocked (private window): page renders read-only from official data, no thrown errors.

---

### Task 1: Official plans in the vault + build tool

**Files:**
- Create: `vault/03 - Engineering Mechanics/Schedule - Engineering Mechanics 2026-27.md`
- Create: `vault/02 - Aerospace Materials I/Schedule - Aerospace Materials I 2026-27.md`
- Create: `vault/04 - Advanced Maths/Schedule - Advanced Maths 2026-27.md`
- Modify: the three subject MOCs and `vault/00 - Indice Central` (link the notes)
- Create: `tools/build_timetable.py`, `assets/data/timetable.js` (generated)
- Test: `tools/tests/test_build_timetable.py`

**Interfaces:**
- Produces: `window.AE_TIMETABLE = { term: {start, end, daysOff: [{date, subjects|null, why}]}, subjects: { <slug>: { source, basis: "plan"|"log", termEnd, groups: { <id>: { slots: [{dow, start, end, room, kind}], dated: bool } }, labGroups: ["A","B"]|[], sessions: [{ id, n, kind, title, text, date|null, start|null, end|null, room|null, groups: [..]|null, lab: "A"|"B"|null, links: [{label, href}] }] } } }`. `dow` 1=Mon..7=Sun; times `HH:MM`; `href` from repo root (`subjects/...html#id`).
- Python: `build(repo: Path) -> dict`, `render(data: dict) -> str`, `main(argv) -> int` with `--check`.

Note format: frontmatter `subject`, `source`, `basis`, `term_end`, `groups` (YAML list: `id`, `dated`, `slots` as `"Wed 15:30-17:00 7.1.J06 lecture"` strings); body one table `| Id | Kind | Date | Start | End | Room | Groups | Lab | Title | What you will do | Portal |`, `Portal` cells as `[label](subjects/...)` links separated by `; `. EM: transcribe all rows of `weekly-planning-mechanics_G46.pdf` (sessions 1-28, Lab 1-4 A/B, Quiz 1-2), G46 dated, Mon 15:30-17:00 lecture 7.1.J07 / Wed 15:30-17:00 problems 7.2.J01. Materials: all 26 sessions, tests, G46 labs, groups G45 (Wed 15:30-17:00 7.1.J06, Fri 15:30-17:00 7.1.J03) and G46 (Wed/Fri 17:15-18:45 7.2.J02), both dated. Maths: the 18 log entries, `basis: log`, no groups dated. Links only where the source names a topic number or problem numbers that exist (check ids on disk; EM particle problems `prob-NN`, rigid body `rb-NN`).

- [ ] **Step 1: Write failing tests** in `test_build_timetable.py`: `test_check_is_clean` (`main(["--check"]) == 0`); `test_em_session_21` (`id em-s21`, date `2026-11-18`, start `15:30`, room `7.2.J01`, title contains `Problems 17, 24`); `test_mat_groups` (G45 and G46 slots as above); `test_ids_unique`; `test_links_exist` (every `href` file exists and its `#id` is in the file); `test_no_lab_links` (every `kind == "lab"` session has `links == []`); `test_dates_inside_term`; `test_maths_is_log` (`basis == "log"`, 18 sessions, all dates ≤ `2026-10-22`); `test_lab_row_with_link_fails` (build on a temp copy with a lab link raises `ValueError`).
- [ ] **Step 2: Run** `python -m unittest tools.tests.test_build_timetable -v` from repo root (or `-s tools/tests -p test_build_timetable.py`). Expected: FAIL (module missing).
- [ ] **Step 3: Write the three notes** (transcribed, cited), link them from the MOCs.
- [ ] **Step 4: Implement `tools/build_timetable.py`** (stdlib; reuse the frontmatter parsing style of `tools/build_nav.py`), then `python tools/build_timetable.py`.
- [ ] **Step 5: Run tests + `python tools/vault_lint.py`.** Expected: PASS, 0 errors.
- [ ] **Step 6: Commit** `feat(calendar): official class plans in the vault and timetable data`.

### Task 2: calendar-core.js (pure logic)

**Files:**
- Create: `assets/js/calendar-core.js`
- Test: `tools/tests/test_calendar.py` (static + browser classes), `tools/tests/calendar_harness.html`

**Interfaces:**
- Consumes: `window.AE_TIMETABLE` (Task 1).
- Produces `window.AECalendar = {`
  - `KEY: 'ae_calendar'`
  - `empty() -> Record` : `{ v:1, updated:0, groups:{}, marks:{}, events:[], hidden:[], daysOff:[] }`; `groups[slug] = { group: string|"custom", labGroup: "A"|"B"|null, slots:[{id, dow, start, end, room, kind}], at }`; `marks[key] = { status: "missed"|"notheld"|"done"|null, note, time:{start,end}|null, room, moveTo:"YYYY-MM-DD"|null, at }`; `events[i] = { id, subject|null, kind:"lecture"|"problems"|"lab"|"exam"|"other", title, date, start, end, room, note, at, deleted? }`; `hidden[i] = { id, at, deleted? }`.
  - `load() -> Record`, `save(rec) -> bool` (try/catch, sets `updated`)
  - `build(tt, rec, prefs, fromISO, toISO) -> Occurrence[]` sorted by date+start: `{ key, subject, sessionId|null, kind, title, text, date, start, end, room, group, lab, links, status, note, official: bool, basis, isEvent, isExam }`
  - `pending(occ, todayISO) -> Occurrence[]` (missed, not done, date ≤ today)
  - `next(occ, nowISO_datetime) -> Occurrence|null`
  - `merge(a, b) -> Record` (per mark key / event id / hidden id newer `at` wins, tombstones kept; `groups[slug]` newer `at`; `daysOff` union)
  - `occKey(slug, date, start) -> "slug@date@start"`
`}`

Algorithm decisions (the tests pin them):
1. Subjects = `prefs.subjects` (fallback all slugs in `rec.groups`).
2. Group dated → occurrences = sessions whose `groups` include it (or null) and have a date; times/rooms from the group's slot matching that weekday when the session row has none.
3. Group `custom` or not dated → generate from `slots` every week between term start and `termEnd || term.end`, skipping `term.daysOff` (matching subject or null) and `rec.daysOff`. Assign plan sessions (kinds `lecture`/`problems`, `basis: "plan"` only) in order, skipping occurrences marked `notheld`; if the student's slots include both kinds and the plan has both, match by kind, else one sequence. `test`/`quiz`/`lab` sessions keep their own date as events. `basis: "log"` sessions are attached only to the occurrence on the same date (else shown as a dated "Covered in class (lecture log)" item only if the student chose the source group — not applicable: Maths has no group, so log rows attach by date only).
4. Dated group + mark `notheld` with `moveTo` → the session reappears on `moveTo` (same start/room unless overridden).
5. Marks key: `sessionId` when the occurrence has one, else `occKey`.
6. Labs: show only `lab == rec.groups[slug].labGroup`, or both when it is null (title suffixed " (A or B)").
7. `hidden` (not deleted) removes official items; events not deleted are added; `prefs.exams[slug].midterm/final` become exam occurrences.

- [ ] **Step 1: Write the harness** `calendar_harness.html` loading `../../assets/data/timetable.js` and `../../assets/js/calendar-core.js`, recording `{name, pass, detail}` into `<pre id="results">`; scenarios: `dated_g46_em_s21` (2026-11-18 15:30 7.2.J01 em-s21); `custom_slots_weekly` (Fluids Tue 15:30 custom → one occurrence every Tuesday in term, none on 2026-10-09 only if Tue... use Fri slot to hit the day off); `order_mapping_by_kind` (EM custom Mon lecture + Wed problems → first Mon gets em-s1, first Wed gets em-s2); `notheld_shifts_plan` (mark first Mon notheld → em-s1 on second Mon); `missed_keeps_plan` (mark missed → same session, appears in `pending`); `dated_moveTo` (em-s21 notheld moveTo 2026-11-20 → on 11-20); `lab_group_filter` (labGroup A → only LAB nA); `lab_no_links`; `events_and_tombstones` (event added shows; merge with deleted copy newer → gone); `merge_marks_newer_wins`; `exams_from_prefs`; `maths_log_by_date`; `empty_record_no_throw`; `next_class` ; `storage_blocked_load` (stub localStorage throwing → `load()` returns `empty()`).
- [ ] **Step 2: Write `test_calendar.py`**: static tests (`KEY = 'ae_calendar'` only key; no `canvas`, no emoji regex `[\U0001F300-\U0001FAFF]`) and the browser class copying `test_pomodoro.py`'s runner, asserting scenario count 15 and all pass. Run: `python -m unittest discover -s tools/tests -p test_calendar.py`. Expected: FAIL.
- [ ] **Step 3: Implement `calendar-core.js`.**
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** `feat(calendar): calendar core (occurrences, plan mapping, sync merge)`.

### Task 3: Sync and account wiring

**Files:**
- Modify: `assets/js/account.js` (SYNC_KEYS, `absorb()`, device-data list near line 371-385, account menu near line 559)
- Test: extend `tools/tests/test_calendar.py` static tests

**Interfaces:**
- Consumes: `AECalendar.merge` (loaded on account pages only; in `absorb()` use it when present, else keep the newer `updated` record).

- [ ] **Step 1: Failing static tests**: `'ae_calendar'` in `SYNC_KEYS`; device-data entry label `'Calendar (classes, labs, exams)'`; menu has `['Calendar', 'calendar.html']` after My study.
- [ ] **Step 2: Implement**; `absorb()` writes `merge(local, cloud)` for `ae_calendar`.
- [ ] **Step 3: Run** the test file and `test_theme`/`test_updates` (menu unchanged otherwise). Expected: PASS.
- [ ] **Step 4: Commit** `feat(accounts): sync the calendar and link it from the account menu`.

### Task 4: Calendar page

**Files:**
- Create: `account/calendar.html` (head/header cloned from `account/dashboard.html`; loads `../assets/data/timetable.js`, `../assets/js/calendar-core.js`, `../assets/js/account-calendar.js`, `../assets/css/account-calendar.css`)
- Create: `assets/js/account-calendar.js`, `assets/css/account-calendar.css`
- Test: extend `calendar_harness.html` with an iframe scenario set, `tools/tests/test_surface.py` (add the page and the open sheet if the suite lists account pages; otherwise add them)

**Interfaces:**
- Consumes: `AECalendar.*`, `AEAccount.current()`, `AEAccount.updatePrefs({exams})`, event `ae-account-change`.
- DOM contract (tests use it): `#calGate` (signed out), `#calApp`, toolbar buttons `[data-cal-nav="prev|next|today"]`, `[data-cal-view="week|month|list"]` with `aria-pressed`, `#calAdd`, `#calGroups`; grid `#calGrid` with `.cal-ev[data-key]` (classes `cal-ev--missed`, `--notheld`, `--lab`, `--exam`, `--manual`); sheet `<dialog id="calSheet">` with buttons `[data-act="missed|notheld|edit|note|done|delete|hide"]`; groups `<dialog id="calGroupsDlg">`; side `#calNext`, `#calCatchup`, `#calComing`; `aria-live` region `#calLive`.

Behaviour from the spec and mockup: week view Mon-Fri (+Sat/Sun only if occupied), month, list (default under 640 px); first visit with no `groups` opens `#calGroupsDlg`; sheet shows date · time · room · group, title, "What you will do", "Prepare" links, source line "From the official weekly planning (<group>). Your changes override it." (log: "Covered in class (lecture log, Aula Global)"; manual: "What was covered" textarea saved as note); `notheld` on a dated group asks for `moveTo` (date input, default next occurrence of that subject); edit offers "This class / Every class" (every = edit slot, custom groups only); arrows ← → move the period when focus is not in a field; Esc closes dialogs; focus trapped. Labs dashed, no links. No emojis.

- [ ] **Step 1: Harness scenarios** (iframe on `account/calendar.html` with a stubbed signed-in `AEAccount` and seeded `ae_calendar`): `gate_when_signed_out`, `groups_dialog_first_visit`, `week_shows_em_s21` (seed G46, today 2026-11-18 via `?today=2026-11-18` query the page honours for tests), `sheet_missed_moves_to_catchup`, `sheet_notheld_custom_shifts`, `no_lab_links_in_dom`, `view_switch_aria_pressed`, `list_default_on_narrow` (iframe 375 px). Update expected count.
- [ ] **Step 2: Run** — FAIL.
- [ ] **Step 3: Implement page, script, CSS.**
- [ ] **Step 4: Run** `test_calendar`, `test_surface`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(accounts): calendar page with groups, missed and not-held classes`.

### Task 5: Dashboard card, docs, What's new

**Files:**
- Modify: `account/dashboard.html` (section `#nextClassTitle` "Next class" before "Upcoming exams", list `#nextClass`, link `calendar.html`), `assets/js/account-pages.js` (`initDashboard`: render via `AECalendar.next` when `AE_TIMETABLE` and `AECalendar` exist; else "Open your calendar"), dashboard loads `timetable.js` + `calendar-core.js`
- Modify: `AGENTS.md` (Accounts paragraph: calendar page, `ae_calendar`, `build_timetable.py`, lab slots allowed without material; Verification list: `python tools/build_timetable.py --check`), `CLAUDE.md` not needed
- Modify: `assets/data/updates.js` (entry `2026-11-19-account-calendar`, tag `Portal`, link `account/calendar.html`)
- Test: harness scenario `dashboard_next_class`

- [ ] **Step 1: Failing scenario** `dashboard_next_class` (G46 seed, today 2026-11-18 morning → "Engineering Mechanics" 15:30 7.2.J01).
- [ ] **Step 2: Implement.**
- [ ] **Step 3: Run** full gates: `python -m unittest discover -s tools/tests`, `python tools/audit_portal.py`, `python tools/vault_lint.py`, `python tools/build_timetable.py --check`, `python tools/build_nav.py --check`, `python tools/build_ai_index.py --check` (new vault notes), `python tools/build_source_notes.py --check`. Expected: all 0 errors (regenerate `ai-index` / source notes if the new notes require it).
- [ ] **Step 4: Screenshots** of `account/calendar.html` at 375, 768, 1440 px with a local test session; console clean.
- [ ] **Step 5: Commit and push** `feat(accounts): next class on the dashboard, docs and What's new`.

### Task 6: "Your classes" step in the sign-up wizard

**Files:**
- Modify: `account/signup.html` (new `<div id="stepClasses" hidden>` after `#stepSubjects`; step bar gets a fifth `<span>`; loads `timetable.js` + `calendar-core.js`), `assets/js/account-pages.js` (`initSignup`: step order `account, subjects, classes, look, dates, done`; render group/lab selects and slot rows; "Skip for now"; the dates step lists official tests/quizzes via `AECalendar.build` filtered to `isExam`)
- Test: harness scenarios `signup_classes_step_saves_groups`, `signup_skip_leaves_groups_empty`, `signup_dates_lists_official_tests`

**Interfaces:**
- Consumes: `AECalendar.empty/load/save/build`, `AE_TIMETABLE.subjects[slug].groups` and `.labGroups`.
- Produces: `renderGroupPicker(container, slugs, rec, onChange)` in `account-pages.js`, reused by the calendar's `#calGroupsDlg` (move it to `calendar-core.js`? no: keep DOM out of core; export it as `window.AECalendarUI.groupPicker` from `account-calendar.js` and load that script on the signup page too).

- [ ] Step 1: failing scenarios. Step 2: run (FAIL). Step 3: implement. Step 4: run `test_calendar`, `test_surface`. Step 5: commit `feat(accounts): set up classes and groups while signing up`.

### Task 7: Guided tour

**Files:**
- Create: `assets/js/tour.js`, `assets/css/tour.css`
- Modify: `assets/js/theme.js` (load `tour.js` after `account.js` when a session exists, like `problem-marks.js`), `assets/js/account.js` (menu item "Take the tour" → `AETour.start(0)`; `ae_tour` in `SYNC_KEYS`, merge newer `at`), `assets/js/account-pages.js` (Done step: "Take the tour" / "Skip" buttons; tour starts on `dashboard.html?tour=1`)
- Test: `tools/tests/test_tour.py` + `tools/tests/tour_harness.html`

**Interfaces:**
- Produces: `window.AETour = { STEPS: [{ id, title, text, page: "account/dashboard.html"|null, target: CSS selector|null, figure: svg string|null }], start(index), skip(), state() }`; DOM: `.tour-card[role="dialog"][aria-modal="true"]`, buttons `[data-tour="next|back|skip"]`, counter `.tour-count`, spotlight `.tour-spot`.
- Steps: the twelve of the spec, in that order (the calendar card mentions revision plans, "Study this", export and attendance); a step whose `page` differs from the current page navigates there with `?tour=<index>`.

- [ ] Step 1: failing tests: static (key `ae_tour` only, no emoji, hidden in print, `theme.js` loads it only when signed in); browser: `tour_starts_from_query`, `skip_sets_done`, `esc_skips`, `next_back_counter` ("3 / 12"), `missing_target_centres_card`, `focus_trapped`, `reduced_motion_no_transition`.
- [ ] Step 2: run (FAIL). Step 3: implement. Step 4: run `test_tour`, `test_surface` (open card under every palette), `test_theme`. Step 5: "What's new" entry for the tour, AGENTS.md line, commit and push `feat(accounts): skippable guided tour of the portal for new accounts`.

### Task 8: Revision plan and "Study this"

**Order:** run Tasks 8-10 before Task 7, so the tour describes the finished calendar.

**Files:**
- Modify: `assets/js/calendar-core.js` (`revisionPlan(tt, rec, prefs, examOcc, todayISO, hoursPerDay) -> Event[]`, events of kind `study` with `links`, ids `rev-<examKey>-<n>`), `assets/js/account-calendar.js` (sheet button `[data-act="revise"]` on exams with an hours input; `[data-act="study"]` on every class and study block), `assets/js/pomodoro.js` (public `window.AEPomodoro.plan({ minutes, label, subject })`: opens the panel on the planner with that total and records the subject for `ae_study_log`)
- Test: `calendar_harness.html` scenarios `revision_avoids_class_hours`, `revision_missed_topics_first`, `revision_blocks_before_exam_only`; `pomodoro_harness.html` scenario `public_plan_hook` (update its expected count in `test_pomodoro.py`)

- [ ] Steps: failing scenarios → run (FAIL) → implement → run `test_calendar`, `test_pomodoro` (PASS) → commit `feat(calendar): revision plans before exams and study-this timer link`.

### Task 9: Export .ics

**Files:**
- Modify: `assets/js/calendar-core.js` (`toICS(occ[], nowISO) -> string`: `BEGIN:VCALENDAR`, `PRODID:-//Sideris//Calendar//EN`, one `VTIMEZONE` for `Europe/Madrid` (CET/CEST rules), `VEVENT` with `UID:<key>@sideris`, `DTSTART;TZID=Europe/Madrid:YYYYMMDDTHHMMSS`, `SUMMARY`, `LOCATION`, `DESCRIPTION` = "What you will do"; CRLF line ends, lines folded at 75 octets, text escaped `\ ; ,` and newlines), `assets/js/account-calendar.js` (toolbar `#calExport` downloads `sideris-calendar.ics` for the visible range or the whole term)
- Test: scenarios `ics_escapes_and_folds`, `ics_has_timezone`, `ics_labs_have_no_url`

- [ ] Steps: failing scenarios → FAIL → implement → PASS → commit `feat(calendar): export classes, labs and exams as .ics`.

### Task 10: Attendance and "Explain what I missed"

**Files:**
- Modify: `assets/js/calendar-core.js` (`attendance(occ, todayISO) -> { <slug>: { held, attended, missed, caughtUp } }`; held excludes `notheld`), `assets/js/account-calendar.js` (side card `#calAttendance`; sheet `[data-act="explain"]` on missed classes), `assets/js/ai-chat.js` (public `window.AESideris.ask({ text, context })`: opens the drawer and sends the question with `context` as page context; never stores it beyond the chat's own history), `assets/js/account-pages.js` (dashboard attendance line per subject)
- Test: scenarios `attendance_counts`, `explain_calls_sideris_hook` (stub `AESideris.ask`); `test_ai_chat.py` static check that `AESideris.ask` exists

- [ ] Steps: failing scenarios → FAIL → implement → PASS (`test_calendar`, `test_ai_chat`) → commit `feat(calendar): attendance per subject and explain-what-I-missed with Sideris`.

### Final gate (after Task 7)

`review-ultrareview` in `ultrareview` mode (milestone), all gates of AGENTS.md, screenshots at 375 / 768 / 1440 px, "What's new" entries, commit and push to `main`.
