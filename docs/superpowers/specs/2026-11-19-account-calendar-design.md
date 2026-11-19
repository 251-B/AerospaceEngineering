# Account calendar: design

Date: 2026-11-19. Status: approved approach (A, fully customisable); mockup accepted.

## Intent

Signed-in readers (students of several groups, not only G46) get a full calendar of their term: lectures, problem classes, labs and exams. Where an official timetable exists, each class says **what will be done in it** and links to the portal pages that prepare it. Every student can rebuild the calendar to match their own week: choose their group, add or move classes, mark a class they missed (to catch up) or a class that was not held (the plan moves on).

Success: a student opens the calendar, sees "Wed 18 Nov, 15:30, 7.2.J01 — Mechanics session 21: Problems 17, 24" with links to those solved problems, and a list of what they still have to catch up.

## Goals

- Week, month and list views of the term; a "Next class", "To catch up" and "Coming up" column.
- Official plans per subject and group, loaded automatically; content and portal links per session.
- Full personal customisation: group per subject, weekly slots, one-off changes (time, room), extra events, notes, exams.
- Two distinct class states: **missed** (class happened, plan unchanged, goes to "To catch up") and **not held** (plan shifts to the next class).
- Synced across devices like the rest of the account (cloud mode), local-only otherwise.
- A "Next class" card on `account/dashboard.html`.

## Non-goals

- Importing the university `.ics` (option C): later, on top of this design.
- Notifications or reminders.
- Shared or class-wide calendars: every calendar is personal.
- Editing the official plan for everyone: a student's changes affect only their calendar.

## Anti-goals

- A calendar that contradicts the official PDFs (invented dates or content).
- Any link to laboratory material (see Labs).
- Emojis, `<canvas>`, a theme key, inline theme code.
- Losing a student's own changes when the official plan data is rebuilt.

## Sources (what exists today)

| Subject | Source | Groups | Content |
| :--- | :--- | :--- | :--- |
| Engineering Mechanics | `03-engineering-mechanics/schedule/weekly-planning-mechanics_G46.pdf` | G46 (date, hour, room per session) | 28 sessions + Lab 1-4 (A/B) + Quiz 1, Quiz 2 |
| Aerospace Materials I | `02-aerospace-materials-1/schedule/Schedule_MAT AERO I 2026 - 27.pdf` | G45 Wed/Fri 15:30-17:00 (7.1.J06, 7.1.J03), G46 Wed/Fri 17:15-18:45 (7.2.J02); same dates | 26 sessions, bank holiday 9 Oct, "no lecture" 14 Oct, Tests 1-3, G46 lab dates |
| Advanced Maths | `04-advanced-maths/schedule/lecture_schedule_2026-27.txt` | group not stated | lecture log of what was covered, 18 dated lectures up to 22 Oct |
| Fluid Mechanics | none | - | manual slots only |
| Business Management | none | - | manual slots only |

## Approaches considered

- **A. Official plans per subject and group + the student's own timetable (chosen).** Official groups load dated sessions; other groups enter weekly slots and the plan is assigned to their classes in order. Fully customisable. Trade-off: order assignment drifts if a class is skipped, solved by the "not held" state.
- B. Manual calendar with the plan as a side list. Simpler, but does not answer "what is done in this class".
- C. Import the university `.ics`. Comfortable, but depends on an external export not every student has; kept as a later add-on to A.

## Design

### Data, Obsidian first

1. One vault note per subject with an official plan: `vault/<subject>/Schedule - <Subject> 2026-27.md` (Mechanics, Materials, Maths). Frontmatter: `subject`, `term_start`, `term_end`, `source` (path in `sources/`), `groups` (id, weekly slots with day, start, end, room, and whether the dates are official). Body: one table of sessions in order:
   `| Session | Kind | Date | Start | End | Room | Groups | Title | What you will do | Portal |`
   - `Kind`: `lecture`, `problems`, `lab`, `test`, `quiz`, `holiday`, `no-class`.
   - Date/start/room: filled only where the source states them (G46 Mechanics, Materials dates); empty otherwise.
   - `What you will do`: transcribed from the source (short, English, no invention).
   - `Portal`: portal paths (`subjects/.../topic-N-*.html#id`), validated by the tool.
   - Advanced Maths: rows come from the lecture log, labelled in the data as `basis: "log"` (what was covered), not as a forecast.
2. `python tools/build_timetable.py` (`--check`) reads the notes and writes `assets/data/timetable.js` (`window.AE_TIMETABLE = {term, subjects: {id: {source, groups, sessions[]}}}`), checking: dates inside the term, portal paths exist on disk, unique session ids (`em-s21`, `mat-s19`, `em-lab3`, `mat-test2`), no lab material links. Never edit the JS by hand.

### Personal data

`localStorage['ae_calendar']` (no "theme" in the key), added to `SYNC_KEYS` in `account.js` and to the device-data list:

```
{ v: 1, updated,
  groups:   { <subject>: { group: "G46" | "custom", slots: [{ dow, start, end, room, kind }] } },
  marks:    { <occurrenceKey>: { status: "missed" | "notheld" | "done", note, time, room, moveTo, at } },
  events:   [{ id, subject, kind, title, date, start, end, room, note, at }],
  hidden:   [<sessionId>] }
```

- `occurrenceKey = <subject>@<YYYY-MM-DD>@<HH:MM>`, stable for one class on one day.
- Exams: the existing `prefs.exams` (midterm/final per subject) stays the single source for those two dates; the calendar shows and edits them through `AEAccount.updatePrefs`. Official tests/quizzes come from the timetable; other exams are `events` with kind `exam`.
- Cloud merge: per entry, newer `at` wins (marks by key, events by id); `groups` takes the copy with the newer `updated`.

### Building a student's calendar (pure function, testable)

1. For each subject in the student's account subjects: official group with dates → occurrences are those dated sessions. Custom group (or no dates) → occurrences are generated from the weekly slots between `term_start` and `term_end`, minus the term's non-teaching days from the data.
2. Plan assignment for order-mapped groups: walk the plan sessions of kind `lecture`/`problems` in order and assign one per occurrence, skipping occurrences marked `notheld`. Missed classes keep their session.
3. Official dated groups: "Class not held" frees the session and asks for a new date (`moveTo`), defaulting to "next class".
4. Overrides (time, room, note) apply last; `events` are added; `hidden` removes an official item.

### Page and UI

- New page `account/calendar.html` + `assets/js/account-calendar.js` + `assets/css/account-calendar.css`, styled like the other account pages (tokens, study-surface palettes, Newsreader / Abril Fatface / JetBrains Mono, AAA on every palette).
- Toolbar: previous / next, Today, Week / Month / List, `+ Add`, `My groups`.
- Week view: Mon-Fri columns (Sat/Sun shown only if something falls there), subject accent as left border, labs dashed, missed striped with "Missed, catch up", not held faded with "Plan moved".
- Session sheet (dialog): date, time, room, group, title, "What you will do", "Prepare" links, source line ("From the official weekly planning (G46). Your changes override it."), buttons `I missed it`, `Class not held`, `Edit time / room` (this class or every class), `Add note`, and for a manual slot with no plan "What was covered" (free text).
- Side column: Next class, To catch up (missed with links, `Mark as done`), Coming up (exams, tests, quizzes, labs).
- `My groups` dialog: per subject, group select (official groups + "My own timetable") and editable weekly slots.
- Phones: list view by default, the side column below.
- Keyboard: arrows move week, `T` today is not used (the portal reserves `T` on the simulator only; here plain buttons). Esc closes dialogs; focus trapped in dialogs.
- Signed-out readers see the same gate as "My study".
- Dashboard: a "Next class" card above "Upcoming exams" linking to the calendar; a "Calendar" link in the account menu.

### Labs

The calendar shows lab slots (title as in the planning, date, hour, room) because students need them in their week, but **never links to lab material**: no link, no file, no page. `build_timetable.py` fails on a lab row with a portal link. AGENTS.md gets one line saying lab slots may appear in the account calendar while lab material stays off the web.

### Content integrity

Session text is transcribed from the sources and cited (`source` of each subject). The Maths log is shown as "Covered in class (lecture log)". Anything the student writes is shown as theirs.

## Verification

- `tools/tests/test_calendar.py`: the build function (official dates, order mapping, not held shift, missed kept, overrides, events, holidays), storage blocked, the sheet buttons, and no lab links.
- `build_timetable.py --check`, `audit_portal`, `vault_lint`, `build_nav --check` if the nav lists account pages, `test_surface` for the page and the open dialog under every palette, Playwright screenshots at 375, 768 and 1440 px.
- "What's new" entry (`Portal` tag).

## Decisions after the builder check (orchestrator's calls)

1. **Deletions sync as tombstones.** A removed event or an un-hidden session is kept as `{ id, deleted: true, at }` so the other device's copy cannot bring it back; tombstones older than the term end are dropped.
2. **Non-teaching days.** `timetable.js` carries one term-wide list built from what the sources state (Materials: 9 Oct bank holiday, 14 Oct no lecture) and nothing invented. Each student can add "day off" dates in `My groups` (stored as `daysOff: [YYYY-MM-DD]` in `ae_calendar`) that remove every class that day. Term: 2026-09-07 to 2026-12-18 (last teaching week of the plans); each subject note states its own `term_end` (last official session).
3. **Order mapping by kind.** When a student's slots carry kinds and the plan has both `lecture` and `problems` sessions (Mechanics alternates them Mon/Wed), a `problems` slot takes the next `problems` session and a `lecture` slot the next `lecture` session. When the slots carry one kind only, all occurrences draw from a single sequence. `test`/`quiz` sessions keep their official date and are shown as events, never shifted.
4. **Advanced Maths** shows "Covered in class (lecture log)" entries on their own dates only. Future Maths slots stay without content ("No plan published yet; add what was covered").
5. **Session content and links.** "What you will do" is the text of the source. A `Portal` link is written only where the source names something the portal has: a topic number (Materials "TOPIC 5" → `teoria/topic-5.html` and its problem page) or problem numbers (Mechanics "Problems 29, 32" → the problem cards `prob-29`, `prob-32`; rigid-body sessions → `rb-NN` where the numbering matches `Problems.pdf` section 2). Where the source names nothing, the cell stays empty. The mapping is checked against `tools/nav.json` and the card ids on disk.
6. **Rooms per slot.** Every weekly slot has its own room (Materials G45: Wed 7.1.J06, Fri 7.1.J03).
7. **Group choice.** The account holds no group today. `ae_calendar.groups[subject].group` is new; on the first visit the calendar opens `My groups` for the student's subjects. No default group is assumed.
8. **Marks follow the session.** A mark on an official plan session is keyed by its session id (`em-s21`), so it follows a `moveTo`. Only classes with no plan session (manual slots in Fluids, Business, future Maths) use `occurrenceKey`.
9. **Lab groups.** Each subject entry stores `labGroup` (`"A"`, `"B"` or `null`). Until the student picks one, both lab rows are shown, marked "A or B". Materials lab dates are published for G46 only; other groups add their own lab events.

## Added 2026-11-19 (user request): set up at sign-up, and a guided tour

### Calendar in the sign-up wizard

The wizard of `account/signup.html` today is Account → Subjects → Palette → Exams → Done. A new step **"Your classes"** goes after Subjects: for every chosen subject a group select (official groups from `timetable.js` + "My own timetable") and, for subjects with lab groups, a lab group select (A / B / Not sure). "My own timetable" opens inline slot rows (day, start, end, room, lecture/problems) with "Add slot". A "Skip for now" link leaves the groups empty (the calendar asks on first visit). The step saves to `ae_calendar` through `AECalendar.save`; the Exams step then lists the official tests and quizzes of the chosen groups as already filled (read-only, "from the official plan") above the midterm/final date inputs. The step counter becomes five.

### Guided tour (walkthrough)

- Shown once, right after the Done step ("Take the tour" primary, "Skip" secondary), and again from the account menu ("Take the tour") at any time.
- A sequence of cards, each pointing at the real element on the real page when it exists (spotlight + card beside it), otherwise a centred card with a small inline SVG figure: 1) My study dashboard, 2) Calendar and "what you will do", 3) Missed / not held, 4) Side menu, 5) Reading palettes, 6) Theory reader (sections, Essential/Full), 7) Problem reader (Answer/Steps/Full) and favourites/notes, 8) Ask AI and the Sideris tutor, 9) Focus sound and study timer, 10) Exam simulator, 11) What's new, 12) Settings and sync.
- Controls: Next, Back, Skip tour (always visible), step dots "3 / 12", Esc = skip, arrows = next/back; focus trapped in the card; `prefers-reduced-motion` removes the movement.
- State `ae_tour` `{ done: bool, step, at }` (no "theme" in the key; synced through `SYNC_KEYS`, newer `at` wins). Skipped in the PDF print mode, hidden in print, no emojis, AAA on every palette.
- Files: `assets/js/tour.js` + `assets/css/tour.css`, loaded by `theme.js` only for signed-in readers (like `problem-marks.js`), steps declared in the script with the selector they point at and a fallback text.

### Extras chosen by the user (2026-11-19)

1. **Revision plan before exams.** For each exam (official test/quiz or `prefs.exams`), "Plan my revision" spreads the topics it covers (from the plan's test row, e.g. "Topics 4, 5, 6 and 7") over the free days between today and the exam, avoiding class hours, as `events` of kind `study` with links to those topics; the student sets hours per day (default 1 h) and can delete or move any block. Topics with missed classes go first.
2. **Study timer link.** Every class and study block has "Study this": opens the study timer (`pomodoro.js`) planner with a duration (block length, or 50 min) and labels the session with the subject so the minutes land in `ae_study_log` for that subject; the timer needs a small public hook `AEPomodoro.plan({ minutes, label, subject })`.
3. **Export to Google Calendar / Outlook.** "Export .ics" downloads an RFC 5545 file of the visible range (classes, labs, exams, study blocks; `Europe/Madrid` times with a `VTIMEZONE`; `UID` = occurrence key). A one-off export, not a subscription.
4. **Attendance and Sideris.** Per subject: classes held, attended, missed, caught up (`done`), shown in the side column and on the dashboard. A missed class has "Explain what I missed": opens the Sideris chat (`ai-chat.js`) with the session's title, text and links as context; needs a public hook `AESideris.ask({ text, context })`.

## Left to the builder

- Exact CSS and the month and list layouts, following the mockup.
- How to show overlapping events (side by side columns).
- Wording of empty states.
