/*!
 * Aerospace Engineering Study Portal: Exam Simulator.
 *
 * Builds a simulated exam from a subject's bank (window.AE_BM_BANK) following its blueprint (window.AE_BM_BLUEPRINT),
 * both written by tools/build_problem_bank.py into subjects/<subject>/data/problems.js. Markup hook:
 *     <div id="examSimulator" data-bank="AE_BM_BANK" data-blueprint="AE_BM_BLUEPRINT"
 *          data-storage="ae_bm_exams" data-bank-dir="../extra-problems/">
 * with the three screens #simSetup, #simRunner and #simResults inside it. Load it with defer, after KaTeX's auto-render
 * and after the bank data.
 *
 * Generation: each blueprint part draws `count` items of its category at random; Part I keeps every case in a different
 * unit and theme when the bank allows it; Part II can be limited to one archetype. Options: duration, and skipping the
 * items of the previous simulated exam (relaxed, with a notice, if too few items remain).
 *
 * Live exam: wall-clock countdown (it survives reloads), points summary, quick navigation, a draft box per question,
 * no hints or solutions. When the time is up the exam goes to grading by itself. Grading: key results and full solutions
 * appear; theory cases are graded with the blueprint's grading steps, the problem per subquestion in quarter points;
 * the grade out of the blueprint total is saved in the history, and every item below half of its points is listed,
 * linked to its worked solution on the Extra problems page.
 *
 * Multiple-choice parts (Aerospace Materials I, Assessment Test II): a blueprint part with "type": "multiple_choice"
 * draws items of kind "multiple_choice" (statement, four options, one answer, one explanation per wrong option). They
 * are answered with radio buttons ("Leave blank" is the default), corrected automatically with the part's
 * points_correct / points_wrong / points_blank, and the mark of the part never goes below its floor. A bank that lists
 * its blocks (BANK.blocks) also gets "Practise a block": the ten questions of one block, corrected as you answer.
 *
 * True/False parts (Business Management, Midterm 2): a part with "type": "true_false" draws items of kind "true_false"
 * (a statement, the options T and F, the reasoning and the source). A blueprint may hold several objective parts (a
 * True/False part and a multiple-choice part), each with its own scoring rule, summary and line in the history. When
 * the part has "justification_required", each statement gets a box for the written reason and, after grading, the
 * reason is shown beside the official one with a check box that voids a right answer whose reason was wrong (it then
 * counts as a blank, as in the exam, where no answer is accepted without its reasoning).
 *
 * Flexible modes: a mode that lists "parts" keeps only those parts; "unit_picker" adds unit check boxes and a number of
 * questions ("count_options", "all" = every item of the ticked units), spread evenly over the ticked units;
 * "archetype_picker" adds problem-type check boxes; "instant_feedback" offers "Correct each answer as I go" (no timer,
 * nothing saved). The choices are remembered per exam and mode in the storage key below (store.custom).
 *
 * Storage (never a key containing "theme"): ae_bm_exams = { current: {...} | null, history: [...] }
 * Shortcuts (ignored while typing or with Ctrl/Alt/Meta): T next reading palette, Esc close the help,
 * ? shortcuts help.
 */
(function () {
  'use strict';

  var root = document.getElementById('examSimulator');
  if (!root) return;
  var BANK = window[root.getAttribute('data-bank') || 'AE_BM_BANK'];
  // A subject with several exams (Advanced Maths) lists them as data-blueprint-<exam> and picks one with ?exam=<exam>.
  var examId = '';
  try { examId = new URLSearchParams(window.location.search).get('exam') || ''; } catch (e) { examId = ''; }
  var BP_FULL = window[(examId && /^[\w-]+$/.test(examId) && root.getAttribute('data-blueprint-' + examId)) ||
                  root.getAttribute('data-blueprint') || 'AE_BM_BLUEPRINT'];
  var BP = BP_FULL;   // the blueprint of the chosen practice scope (see setMode); BP_FULL when the blueprint lists no modes
  var KEY = root.getAttribute('data-storage') || 'ae_bm_exams';
  var examKey = examId || root.getAttribute('data-default-exam') || '';
  // The Extra problems section: theory cases and practice problems live on two pages of their own.
  var BANK_DIR = root.getAttribute('data-bank-dir') || '../extra-problems/';
  function itemHref(id) {
    var it = BY_ID[id];
    var pages = BANK.pages || {};
    var page = (it && pages[it.category]) || (it && it.category === 'short_theory_case' ? 'midterm-1-theory.html' : 'midterm-1-problems.html');
    return BANK_DIR + page + '#' + id;
  }
  var setupEl = document.getElementById('simSetup');
  var runnerEl = document.getElementById('simRunner');
  var resultsEl = document.getElementById('simResults');
  if (!BANK || !BANK.items || !BP_FULL || !BP_FULL.parts || !setupEl || !runnerEl || !resultsEl) {
    root.insertAdjacentHTML('afterbegin', '<p class="sim-card">The exam simulator could not load the problem bank.</p>');
    return;
  }
  var BY_ID = {};
  BANK.items.forEach(function (i) { BY_ID[i.id] = i; });
  // Texts that depend on the blueprint (title, structure note, button label), and the current exam link.
  Array.prototype.forEach.call(root.querySelectorAll('[data-bp]'), function (n) {
    var v = BP_FULL[n.getAttribute('data-bp')];
    if (typeof v === 'string' && v) n.textContent = v;
  });
  Array.prototype.forEach.call(document.querySelectorAll('[data-exam-link]'), function (a) {
    var cur = (a.getAttribute('data-exam-link') === (examId || root.getAttribute('data-default-exam')));
    if (cur) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
  });

  // ---- Storage -----------------------------------------------------------------------
  function readJSON(key, fallback) {
    try {
      var v = JSON.parse(window.localStorage.getItem(key) || 'null');
      return v && typeof v === 'object' ? v : fallback;
    } catch (e) { return fallback; }
  }
  function writeJSON(key, value) {
    try { window.localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* in memory only */ }
  }
  var store = readJSON(KEY, null) || {};
  if (!Array.isArray(store.history)) store.history = [];
  if (store.current && !store.current.items) store.current = null;
  function save() { writeJSON(KEY, store); }
  // One storage key serves every exam of a subject: an exam in progress belongs to its own blueprint, so go back to it.
  if (store.current && (store.current.exam || '') !== examKey && store.current.exam) {
    window.location.replace('?exam=' + encodeURIComponent(store.current.exam));
    return;
  }
  function history() { return store.history.filter(function (h) { return (h.exam || '') === examKey || (!h.exam && examKey === (root.getAttribute('data-default-exam') || '')); }); }

  // ---- Helpers -----------------------------------------------------------------------
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function fmt(x) { return (Math.round(x * 100) / 100).toFixed(2).replace(/\.?0+$/, '') || '0'; }
  function fmt1(x) { return (Math.round(x * 100) / 100).toFixed(2); }
  function renderMath(node) {
    if (typeof window.renderMathInElement !== 'function') {
      window.addEventListener('load', function () { renderMath(node); }, { once: true });
      return;
    }
    window.renderMathInElement(node, {
      delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }],
      throwOnError: false
    });
  }
  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  var blockEl = null;   // the "Practise a block" screen, created on demand
  function show(screen) {
    [setupEl, runnerEl, resultsEl, blockEl].forEach(function (s) { if (s) s.hidden = s !== screen; });
    window.scrollTo(0, 0);
  }
  var live = document.getElementById('simLive');
  function announce(msg) { if (live) { live.textContent = ''; window.setTimeout(function () { live.textContent = msg; }, 30); } }

  // ---- Objective items: multiple choice and True/False ---------------------------------
  // isMC is true for every automatically corrected item (both kinds); isTF only for True/False statements.
  function isTF(item) { return !!item && item.kind === 'true_false'; }
  function isMC(item) { return !!item && (item.kind === 'multiple_choice' || item.kind === 'true_false'); }
  function isObjPart(p) { return !!p && (p.type === 'multiple_choice' || p.type === 'true_false'); }
  function partOf(entry) {
    return BP.parts.filter(function (p) { return p.id === entry.part; })[0] ||
      BP_FULL.parts.filter(function (p) { return p.id === entry.part; })[0];
  }
  var mcPart = null;   // the first objective part of the current scope, set by setMode()
  var objParts = [];   // every objective part of the current scope
  function signed(x) { return (x > 0 ? '+' : '') + fmt(x); }
  // Points of one answer under the rules of its part: right, wrong or blank. A right answer voided by the student
  // (its written reason was wrong) counts as a blank.
  function mcPoints(part, item, choice, voided) {
    if (!choice) return part.points_blank || 0;
    if (choice === item.answer) return voided ? (part.points_blank || 0) : part.points_correct;
    return part.points_wrong;
  }
  // Mark of an objective part: the sum of its answers, never below the floor of the part.
  function mcPartScore(part, entries, answers, invalid) {
    var raw = 0, right = 0, wrong = 0, blank = 0, voided = 0;
    invalid = invalid || {};
    entries.forEach(function (e) {
      var item = BY_ID[e.id], c = answers[e.id] || '', v = !!invalid[e.id] && c === item.answer;
      raw += mcPoints(part, item, c, v);
      if (!c) blank++; else if (c === item.answer) { if (v) voided++; else right++; } else wrong++;
    });
    raw = Math.round(raw * 100) / 100;
    var floor = typeof part.floor === 'number' ? part.floor : -Infinity;
    return { raw: raw, score: Math.max(floor, raw), right: right, wrong: wrong, blank: blank, voided: voided };
  }
  function answerWord(item, label) { return isTF(item) ? (label === 'T' ? 'True' : 'False') : label + ')'; }
  function mcOptions(item, name, chosen, onChange, withBlank) {
    var box = el('fieldset', 'sim-mcq', null);
    var lg = el('legend', 'bank-sr', 'Options'); box.appendChild(lg);
    var list = item.options.slice();
    if (withBlank) list.push({ label: '', html: 'Leave blank' });
    list.forEach(function (o) {
      var lab = el('label', 'sim-mcq__opt' + (o.label ? '' : ' sim-mcq__opt--blank'), null);
      var input = document.createElement('input');
      input.type = 'radio'; input.name = name; input.value = o.label;
      input.checked = (chosen || '') === o.label;
      input.addEventListener('change', function () { if (input.checked) onChange(o.label); });
      lab.appendChild(input);
      if (o.label) lab.appendChild(el('span', 'sim-mcq__letter', isTF(item) ? o.label : o.label + ')'));
      var t = el('span', 'sim-mcq__text', null); t.innerHTML = o.html; lab.appendChild(t);
      box.appendChild(lab);
    });
    if (isTF(item)) box.className += ' sim-mcq--tf';
    return box;
  }
  // The written reason of a True/False statement (kept with the drafts of the exam).
  function reasonBox(id, value, onInput) {
    var w = el('div', 'sim-draft sim-reason', null);
    var lab = el('label', 'sim-label', 'Your reason (required: in the exam no answer counts without it)');
    lab.setAttribute('for', 'reason-' + id);
    var ta = document.createElement('textarea');
    ta.id = 'reason-' + id;
    ta.rows = 2;
    ta.placeholder = 'Why is the statement true or false? One or two sentences.';
    ta.value = value || '';
    ta.addEventListener('input', function () { onInput(ta.value); });
    w.appendChild(lab); w.appendChild(ta);
    return w;
  }
  // The corrected view of one question: every option marked, the reason for the answer and for each wrong option.
  // For a True/False statement the student's written reason (if any) is shown beside the official one.
  function mcReview(item, choice, reason) {
    var box = el('div', 'sim-mcq sim-mcq--review' + (isTF(item) ? ' sim-mcq--tf' : ''), null);
    item.options.forEach(function (o) {
      var state = o.label === item.answer ? 'right' : (o.label === choice ? 'wrong' : 'other');
      var row = el('div', 'sim-mcq__opt', null);
      row.setAttribute('data-state', state);
      row.appendChild(el('span', 'sim-mcq__letter', isTF(item) ? o.label : o.label + ')'));
      var t = el('span', 'sim-mcq__text', null); t.innerHTML = o.html; row.appendChild(t);
      row.appendChild(el('span', 'sim-mcq__mark', state === 'right' ? (choice === o.label ? 'Right answer (yours)' : 'Right answer') : (state === 'wrong' ? 'Your answer' : '')));
      box.appendChild(row);
    });
    if (isTF(item)) {
      var cmp = el('div', 'sim-reason-compare', null);
      var mine = el('div', 'bank-panel bank-panel--hint', null);
      mine.appendChild(el('p', 'bank-panel__title', 'Your reason'));
      mine.appendChild(el('p', 'sim-reason-compare__text', reason && reason.trim() ? reason : '(no reason written)'));
      var off = el('div', 'bank-panel bank-panel--solution', null);
      off.appendChild(el('p', 'bank-panel__title', 'Reasoning: the statement is ' + answerWord(item, item.answer).toLowerCase()));
      var oc = el('div', null, null); oc.innerHTML = item.explanation_html; off.appendChild(oc);
      if (item.source_html) { var os = el('div', 'sim-muted', null); os.innerHTML = item.source_html; off.appendChild(os); }
      cmp.appendChild(mine); cmp.appendChild(off);
      box.appendChild(cmp);
      return box;
    }
    var why = el('div', 'bank-panel bank-panel--solution', null);
    why.appendChild(el('p', 'bank-panel__title', 'Why ' + item.answer + ') is right'));
    var c = el('div', null, null); c.innerHTML = item.explanation_html; why.appendChild(c);
    var ul = el('ul', 'sim-mcq__why', null);
    Object.keys(item.distractors || {}).sort().forEach(function (k) {
      var li = el('li', null, null); li.innerHTML = '<strong>' + k + ')</strong> ' + item.distractors[k]; ul.appendChild(li);
    });
    why.appendChild(el('p', 'bank-panel__title', 'Why the other options are wrong'));
    why.appendChild(ul);
    if (item.source_html || item.origin === 'official-exam') {
      var s = el('div', 'sim-muted sim-source-line', null);
      if (item.origin === 'official-exam') s.appendChild(el('span', 'sim-origin-badge', 'Official exam'));
      if (item.source_html) { var sh = el('span', null, null); sh.innerHTML = item.source_html; s.appendChild(sh); }
      why.appendChild(s);
    }
    box.appendChild(why);
    return box;
  }
  function verdictText(item, choice, voided) {
    if (!choice) return 'Left blank';
    if (choice === item.answer) return voided ? 'Right, but voided: your reason was wrong (counts as a blank)' : 'Right';
    return 'Wrong: you chose ' + answerWord(item, choice) + ', the answer is ' + answerWord(item, item.answer);
  }

  // ---- Practice scopes (blueprint "modes") ---------------------------------------------
  // A blueprint may list modes: each one fixes the number of test questions per unit (selection_rules.per_unit of the
  // multiple-choice part), may drop the problem part (include_problem false: the exam is the test only and is graded
  // out of its own points) and may carry its own clock. The effective blueprint BP is rebuilt from BP_FULL on every change.
  var MODES = Array.isArray(BP_FULL.modes) && BP_FULL.modes.length ? BP_FULL.modes : null;
  var modeId = '';
  var part2 = null;
  function effectiveBlueprint(mode) {
    var bp = JSON.parse(JSON.stringify(BP_FULL));
    delete bp.modes;
    if (!mode) return bp;
    if (Array.isArray(mode.parts)) {
      // Flexible mode: keep the listed parts; the pickers (applyCustom) then set the counts.
      bp.parts = bp.parts.filter(function (p) { return mode.parts.indexOf(p.id) >= 0; });
      if (Array.isArray(mode.archetypes)) {
        bp.parts.forEach(function (p) {
          if (!isObjPart(p)) {
            p.selection_rules = p.selection_rules || {};
            p.selection_rules.archetypes = mode.archetypes.slice();
            delete p.selection_rules.must_archetypes;
            delete p.selection_rules.units;
          }
        });
      }
      bp.total_points = Math.round(bp.parts.reduce(function (s, p) { return s + p.count * p.points_each; }, 0) * 100) / 100;
      if (mode.duration_minutes) bp.duration_minutes = mode.duration_minutes;
      if (mode.duration_options_minutes) bp.duration_options_minutes = mode.duration_options_minutes;
      bp.mode = { id: mode.id, label: mode.label };
      return bp;
    }
    bp.parts = bp.parts.filter(function (p) { return mode.include_problem !== false || p.type === 'multiple_choice'; });
    bp.parts.forEach(function (p) {
      if (p.type === 'multiple_choice' && mode.per_unit) {
        p.selection_rules = p.selection_rules || {};
        p.selection_rules.per_unit = mode.per_unit;
      }
    });
    bp.total_points = Math.round(bp.parts.reduce(function (s, p) { return s + p.count * p.points_each; }, 0) * 100) / 100;
    if (mode.duration_minutes) bp.duration_minutes = mode.duration_minutes;
    if (mode.duration_options_minutes) bp.duration_options_minutes = mode.duration_options_minutes;
    bp.mode = { id: mode.id, label: mode.label };
    return bp;
  }
  function modeById(id) { return MODES ? (MODES.filter(function (m) { return m.id === id; })[0] || null) : null; }
  function defaultMode() { return MODES ? (MODES.filter(function (m) { return m.default; })[0] || MODES[0]) : null; }
  function setMode(id) {
    var mode = modeById(id) || defaultMode();
    modeId = mode ? mode.id : '';
    BP = effectiveBlueprint(mode);
    applyCustom();
    objParts = BP.parts.filter(isObjPart);
    mcPart = objParts[0] || null;
    // The part whose problem type can be chosen: the one that lists archetypes (Business Management: the Extra Practice problem).
    part2 = BP.parts.filter(function (p) { return p.selection_rules && p.selection_rules.archetypes; })[0] ||
      BP.parts.filter(function (p) { return p.category === 'extra_practice_problem'; })[0] || null;
  }

  // ---- Pickers of the flexible modes (units, number of items, problem types, instant feedback) ----------
  var UNIT_LABELS = BP_FULL.unit_labels || BANK.units || {};
  function unitWord() {
    var first = Object.keys(UNIT_LABELS).map(function (k) { return UNIT_LABELS[k]; })[0] || '';
    return /^Topic\b/i.test(first) ? 'Topic ' : 'Unit ';
  }
  function customKey() { return (examKey || 'default') + ':' + modeId; }
  function customFor() {
    var mode = modeById(modeId);
    if (!mode || !Array.isArray(mode.parts)) return null;
    if (!store.custom || typeof store.custom !== 'object') store.custom = {};
    var c = store.custom[customKey()];
    if (!c || typeof c !== 'object') c = store.custom[customKey()] = {};
    if (!Array.isArray(c.units)) c.units = Object.keys(UNIT_LABELS);
    if (c.count == null || (mode.count_options && mode.count_options.indexOf(c.count) < 0)) c.count = mode.default_count;
    var allArch = Array.isArray(mode.archetypes) ? mode.archetypes.slice() : [];
    if (!allArch.length) {
      BP.parts.forEach(function (p) {
        if (!isObjPart(p) && p.selection_rules) {
          allArch = allArch.concat(p.selection_rules.archetypes || [], p.selection_rules.must_archetypes || []);
        }
      });
    }
    if (!Array.isArray(c.archetypes)) c.archetypes = allArch;
    c.instant = !!(c.instant && mode.instant_feedback);
    return c;
  }
  // Spread `want` items over the ticked units, as evenly as the bank allows; returns {unit: n}.
  function spread(want, units, avail) {
    var out = {}, left = want, open = units.filter(function (u) { return avail[u] > 0; });
    units.forEach(function (u) { out[u] = 0; });
    while (left > 0 && open.length) {
      var share = Math.max(1, Math.floor(left / open.length));
      shuffle(open).forEach(function (u) {
        if (left <= 0) return;
        var take = Math.min(share, avail[u] - out[u], left);
        out[u] += take; left -= take;
      });
      open = open.filter(function (u) { return avail[u] > out[u]; });
    }
    Object.keys(out).forEach(function (u) { if (!out[u]) delete out[u]; });
    return out;
  }
  // Rebuild the counts of the current scope from the pickers (flexible modes only).
  function applyCustom() {
    var mode = modeById(modeId), c = customFor();
    if (!c) return;
    BP.parts.forEach(function (p) {
      var rules = p.selection_rules = p.selection_rules || {};
      if (isObjPart(p) && mode.unit_picker) {
        var avail = {};
        c.units.forEach(function (u) {
          avail[u] = BANK.items.filter(function (i) { return i.category === p.category && String(i.unit) === String(u); }).length;
        });
        var total = c.units.reduce(function (s, u) { return s + avail[u]; }, 0);
        var want = c.count === 'all' ? total : Math.min(Number(c.count) || 0, total);
        rules.per_unit = spread(want, c.units.slice(), avail);
        rules.units = c.units.map(Number);
        p.count = want;
      } else if (!isObjPart(p) && mode.archetype_picker) {
        rules.only_archetypes = c.archetypes.slice();
        var pool = BANK.items.filter(function (i) {
          return i.category === p.category && c.archetypes.indexOf(i.archetype) >= 0 &&
            (!rules.units || rules.units.indexOf(i.unit) >= 0) &&
            (!rules.must_archetypes || rules.must_archetypes.indexOf(i.archetype) >= 0);
        });
        p.count = Math.min(Number(c.count) || 1, pool.length);
      }
      p.points_total = Math.round(p.count * p.points_each * 100) / 100;
    });
    BP.total_points = Math.round(BP.parts.reduce(function (s, p) { return s + p.points_total; }, 0) * 100) / 100;
  }
  // The last scope chosen, per exam (older versions stored one string for the whole subject).
  function lastMode() {
    var lm = store.lastMode;
    if (typeof lm === 'string') return lm;
    return (lm && typeof lm === 'object' && lm[examKey || 'default']) || '';
  }
  function rememberMode(id) {
    if (!store.lastMode || typeof store.lastMode !== 'object') store.lastMode = {};
    store.lastMode[examKey || 'default'] = id;
  }
  setMode(store.current && store.current.mode ? store.current.mode : lastMode());

  // ---- Setup screen ------------------------------------------------------------------
  var durationBox = document.getElementById('simDurations');
  var archSelect = document.getElementById('simArchetype');
  var structure = document.getElementById('simStructure');
  function renderDurations() {
    durationBox.innerHTML = '';
    (BP.duration_options_minutes || [BP.duration_minutes]).forEach(function (m) {
      var label = el('label', 'sim-radio', null);
      var input = document.createElement('input');
      input.type = 'radio';
      input.name = 'simDuration';
      input.value = String(m);
      input.checked = m === BP.duration_minutes;
      label.appendChild(input);
      label.appendChild(document.createTextNode(' ' + m + ' min' + (m === BP.duration_minutes ? ' (standard)' : '')));
      durationBox.appendChild(label);
    });
  }
  function renderArchetypes() {
    while (archSelect.options.length > 1) archSelect.remove(1);
    if (part2 && part2.selection_rules && part2.selection_rules.archetypes) {
      part2.selection_rules.archetypes.forEach(function (a) {
        var o = document.createElement('option');
        o.value = a;
        o.textContent = (BANK.archetypes && BANK.archetypes[a]) || a;
        archSelect.appendChild(o);
      });
    }
    archSelect.value = 'any';
    // A scope without the problem part has no problem type to choose, nor one whose types are ticked below.
    var mode = modeById(modeId);
    if (archSelect.parentNode) archSelect.parentNode.hidden = !part2 || !!(mode && mode.archetype_picker);
  }
  function unitMix(p) {
    var pu = p.selection_rules && p.selection_rules.per_unit;
    if (!pu) return '';
    return '<br><span class="sim-muted">' + Object.keys(pu).map(function (u) { return unitWord() + u + ': ' + pu[u]; }).join(' · ') + '</span>';
  }
  function renderStructure() {
    if (!structure) return;
    var rows = BP.parts.map(function (p) {
      var rule = isObjPart(p) ? '<br><span class="sim-muted">right ' + signed(p.points_correct) + ' · wrong ' + signed(p.points_wrong) + ' · blank ' + fmt(p.points_blank || 0) + ' · never below ' + fmt(p.floor) + (p.justification_required ? ' · a written reason for each answer' : '') + '</span>' + (MODES ? unitMix(p) : '') : '';
      return '<tr><td>' + p.label + rule + '</td><td class="num">' + p.count + ' × ' + fmt1(p.points_each) + '</td><td class="num">' + fmt1(p.points_total) + '</td></tr>';
    }).join('');
    structure.innerHTML = '<thead><tr><th>Part</th><th class="num">Items × points</th><th class="num">Points</th></tr></thead><tbody>' + rows +
      '<tr><td><strong>Total</strong></td><td class="num">' + BP.duration_minutes + ' min</td><td class="num"><strong>' + fmt1(BP.total_points) + '</strong></td></tr></tbody>';
  }
  function renderGenerateLabel() {
    var mode = modeById(modeId);
    var span = document.querySelector('#simGenerate [data-bp="generate_label"]');
    if (span) span.textContent = (mode && mode.generate_label) || BP_FULL.generate_label || span.textContent;
  }
  // The pickers of a flexible mode, rebuilt on every change of scope.
  var customBox = null;
  function checkboxes(legendText, keys, labels, chosen, onChange, quick) {
    var fs = document.createElement('fieldset');
    fs.className = 'sim-picks';
    fs.appendChild(el('legend', null, legendText));
    var list = el('div', 'sim-picks__list', null);
    var inputs = [];
    keys.forEach(function (k) {
      var lab = el('label', 'sim-check', null);
      var input = document.createElement('input');
      input.type = 'checkbox'; input.value = k; input.checked = chosen.indexOf(k) >= 0;
      input.addEventListener('change', function () {
        onChange(inputs.filter(function (x) { return x.checked; }).map(function (x) { return x.value; }));
      });
      inputs.push(input);
      lab.appendChild(input);
      lab.appendChild(el('span', null, ' ' + labels[k]));
      list.appendChild(lab);
    });
    fs.appendChild(list);
    if (quick) {
      var row = el('div', 'sim-picks__quick', null);
      [['All ' + quick, true], ['Clear', false]].forEach(function (b) {
        var btn = el('button', 'bank-btn', b[0]);
        btn.type = 'button';
        btn.addEventListener('click', function () {
          inputs.forEach(function (x) { x.checked = b[1]; });
          onChange(b[1] ? keys.slice() : []);
        });
        row.appendChild(btn);
      });
      fs.appendChild(row);
    }
    return fs;
  }
  function renderCustom() {
    var mode = modeById(modeId), c = customFor();
    if (!customBox) {
      if (!durationBox || !durationBox.closest || !durationBox.closest('.sim-options')) return;
      customBox = el('div', 'sim-custom', null);
      customBox.id = 'simCustom';
      var opts = durationBox.closest('.sim-options');
      var modesFs = document.getElementById('simModes');
      opts.insertBefore(customBox, modesFs ? modesFs.nextSibling : opts.firstChild);
    }
    customBox.innerHTML = '';
    var hasPickers = !!(mode && (mode.unit_picker || mode.archetype_picker || mode.count_options || mode.instant_feedback));
    customBox.hidden = !c || !hasPickers;
    if (!c || !hasPickers) return;
    function changed() { save(); applyCustom(); renderStructure(); renderGenerateState(); }
    if (mode.unit_picker) {
      customBox.appendChild(checkboxes('Units', Object.keys(UNIT_LABELS), UNIT_LABELS, c.units, function (v) { c.units = v; changed(); }, 'units'));
    }
    if (mode.archetype_picker) {
      var keys = Array.isArray(mode.archetypes) ? mode.archetypes.slice() : [];
      if (!keys.length) {
        BP.parts.forEach(function (p) {
          if (!isObjPart(p) && p.selection_rules) {
            keys = keys.concat(p.selection_rules.archetypes || [], p.selection_rules.must_archetypes || []);
          }
        });
      }
      var labels = {};
      keys.forEach(function (k) { labels[k] = (BANK.archetypes && BANK.archetypes[k]) || k; });
      customBox.appendChild(checkboxes('Types of problem', keys, labels, c.archetypes, function (v) { c.archetypes = v; changed(); }, 'types'));
    }
    if (mode.count_options) {
      var w = el('div', null, null);
      var lab = el('label', 'sim-label', mode.archetype_picker ? 'Number of problems' : 'Number of questions');
      lab.setAttribute('for', 'simCount');
      var sel = document.createElement('select');
      sel.id = 'simCount'; sel.className = 'sim-select';
      mode.count_options.forEach(function (n) {
        var o = document.createElement('option');
        o.value = String(n); o.textContent = n === 'all' ? 'All available' : String(n);
        sel.appendChild(o);
      });
      sel.value = String(c.count);
      sel.addEventListener('change', function () { c.count = sel.value === 'all' ? 'all' : Number(sel.value); changed(); });
      w.appendChild(lab); w.appendChild(sel);
      customBox.appendChild(w);
    }
    if (mode.instant_feedback) {
      var il = el('label', 'sim-check', null);
      var ic = document.createElement('input');
      ic.type = 'checkbox'; ic.id = 'simInstant'; ic.checked = !!c.instant;
      ic.addEventListener('change', function () { c.instant = ic.checked; changed(); });
      il.appendChild(ic);
      il.appendChild(el('span', null, ' Correct each answer as I go (no timer, nothing saved)'));
      customBox.appendChild(il);
    }
    var msg = el('p', 'sim-muted', null);
    msg.id = 'simCustomMsg';
    msg.setAttribute('aria-live', 'polite');
    customBox.appendChild(msg);
  }
  // The generate button is off while the pickers leave nothing to draw.
  function renderGenerateState() {
    var btn = document.getElementById('simGenerate'), msg = document.getElementById('simCustomMsg');
    var curMode = modeById(modeId);
    var empty = curMode && curMode.archetype_picker ? BP.parts.every(function (p) { return !p.count; }) : BP.parts.some(function (p) { return !p.count; });
    var c = customFor();
    if (btn) btn.disabled = empty;
    if (msg) {
      var n = BP.parts.reduce(function (s, p) { return s + p.count; }, 0);
      msg.textContent = empty ? 'Tick at least one ' + (modeById(modeId).archetype_picker ? 'type of problem' : 'unit') + ' with items in the bank.'
        : n + ' item(s) will be drawn' + (c && c.instant ? ', corrected as you answer.' : ', graded out of ' + fmt1(BP.total_points) + ' points.');
    }
    var timed = !(c && c.instant);
    if (durationBox && durationBox.closest) { var fs = durationBox.closest('fieldset'); if (fs) fs.hidden = !timed; }
  }
  function renderSetup() { renderDurations(); renderArchetypes(); renderCustom(); renderStructure(); renderGenerateLabel(); renderGenerateState(); }
  // The scope picker: radio buttons at the head of the "New exam" options, only when the blueprint lists modes.
  function buildModePicker() {
    if (!MODES || !durationBox || !durationBox.closest) return;
    var opts = durationBox.closest('.sim-options');
    if (!opts) return;
    var fs = document.createElement('fieldset');
    fs.className = 'sim-modes';
    fs.id = 'simModes';
    var lg = document.createElement('legend');
    lg.textContent = 'Practice scope';
    fs.appendChild(lg);
    var box = el('div', 'sim-radios', null);
    var desc = el('p', 'sim-muted', null);
    desc.id = 'simModeDesc';
    MODES.forEach(function (m) {
      var label = el('label', 'sim-radio', null);
      var input = document.createElement('input');
      input.type = 'radio';
      input.name = 'simMode';
      input.value = m.id;
      input.checked = m.id === modeId;
      input.addEventListener('change', function () {
        if (!input.checked) return;
        setMode(m.id);
        rememberMode(m.id);
        save();
        renderSetup();
        desc.textContent = m.description || '';
      });
      label.appendChild(input);
      label.appendChild(document.createTextNode(' ' + m.label));
      box.appendChild(label);
    });
    var cur = modeById(modeId);
    desc.textContent = (cur && cur.description) || '';
    fs.appendChild(box);
    fs.appendChild(desc);
    opts.insertBefore(fs, opts.firstChild);
  }
  buildModePicker();
  renderSetup();

  function renderHistory() {
    var box = document.getElementById('simHistory');
    if (!box) return;
    var hist = history();
    if (!hist.length) { box.innerHTML = '<p class="sim-muted">No simulated exam yet. Your grades will appear here.</p>'; return; }
    var rows = hist.slice().reverse().slice(0, 10).map(function (h) {
      var d = new Date(h.finishedAt);
      var links = h.items.filter(function (r) { return !isMC(BY_ID[r.id]); }).map(function (r) { return '<a href="' + itemHref(r.id) + '">' + r.id + '</a> ' + fmt(r.score) + '/' + fmt(r.points); });
      (h.parts || []).forEach(function (pr) { links.unshift(pr.label + ': ' + pr.right + ' right, ' + pr.wrong + ' wrong, ' + pr.blank + ' blank' + (pr.voided ? ' (' + pr.voided + ' voided)' : '') + ' = ' + fmt(pr.score) + '/' + fmt(pr.max)); });
      links = links.join(' · ');
      return '<tr><td>' + d.toLocaleDateString('en-GB') + ' ' + d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }) +
        (h.modeLabel ? '<br><span class="sim-muted">' + h.modeLabel + '</span>' : '') + '</td><td>' + links + '</td><td class="num"><strong>' + fmt1(h.total) + '</strong> / ' + fmt1(h.max) + '</td></tr>';
    }).join('');
    var avg = hist.reduce(function (s, h) { return s + h.total; }, 0) / hist.length;
    var sameMax = hist.every(function (h) { return h.max === hist[0].max; });
    // Scopes with different maxima (test only, whole exam) are averaged as a share of the points available.
    var avgText = sameMax ? fmt1(avg) + ' / ' + fmt1(BP.total_points)
      : Math.round(100 * hist.reduce(function (s, h) { return s + h.total; }, 0) / hist.reduce(function (s, h) { return s + h.max; }, 0)) + '% of the points';
    box.innerHTML = '<p class="sim-muted">' + hist.length + ' exam(s) graded · average ' + avgText + '</p>' +
      '<div class="sim-table-wrap"><table class="sim-history"><thead><tr><th>Date</th><th>Items and points</th><th class="num">Grade</th></tr></thead><tbody>' + rows + '</tbody></table></div>';
  }

  // ---- Generation --------------------------------------------------------------------
  // Items already drawn for an earlier part of the same exam (several parts can share a category).
  var taken = {};
  function pickPart(part, excluded, archetype) {
    var rules = part.selection_rules || {};
    var pool = BANK.items.filter(function (i) {
      return i.category === part.category && !taken[i.id] &&
        (!rules.units || rules.units.indexOf(i.unit) >= 0) &&
        (!rules.must_archetypes || rules.must_archetypes.indexOf(i.archetype) >= 0) &&
        (!rules.only_archetypes || rules.only_archetypes.indexOf(i.archetype) >= 0) &&
        (!archetype || archetype === 'any' || i.archetype === archetype);
    });
    var notes = [];
    var free = pool.filter(function (i) { return !excluded[i.id]; });
    if (free.length < part.count) {
      notes.push(part.label + ': not enough new items, so some excluded ones were allowed again.');
      free = pool;
    }
    shuffle(free);
    if (rules.per_unit) {
      // A fixed number of items per unit (the mix of the real paper), each on a different concept when possible.
      var picked = [], seenTheme = {}, seenBlock = {};
      Object.keys(rules.per_unit).forEach(function (u) {
        var want = rules.per_unit[u], got = 0, mine = free.filter(function (i) { return String(i.unit) === String(u); });
        // First a different block and a different concept for every question, then only a different concept, then any.
        ['block', 'concept', 'any'].forEach(function (level) {
          mine.forEach(function (it) {
            if (got >= want || picked.indexOf(it) >= 0) return;
            if (level !== 'any' && seenTheme[it.theme]) return;
            if (level === 'block' && it.block && seenBlock[it.block]) return;
            picked.push(it); seenTheme[it.theme] = 1; if (it.block) seenBlock[it.block] = 1; got++;
          });
        });
      });
      free.forEach(function (it) { if (picked.length < part.count && picked.indexOf(it) < 0) picked.push(it); });
      return { items: shuffle(picked.slice(0, part.count)), notes: notes };
    }
    var tiers = [[rules.distinct_units, rules.distinct_themes], [false, rules.distinct_themes], [false, false]];
    for (var t = 0; t < tiers.length; t++) {
      var chosen = [], units = {}, themes = {};
      for (var k = 0; k < free.length && chosen.length < part.count; k++) {
        var it = free[k];
        if (tiers[t][0] && units[it.unit]) continue;
        if (tiers[t][1] && themes[it.theme]) continue;
        chosen.push(it); units[it.unit] = 1; themes[it.theme] = 1;
      }
      if (chosen.length === part.count) return { items: chosen, notes: notes };
    }
    return { items: free.slice(0, part.count), notes: notes };
  }

  function generate() {
    var excluded = {};
    var hist = history();
    if (document.getElementById('simSkipPrevious').checked && hist.length) {
      hist[hist.length - 1].items.forEach(function (r) { excluded[r.id] = 1; });
    }
    var minutes = Number((document.querySelector('input[name="simDuration"]:checked') || {}).value || BP.duration_minutes);
    var ids = [], notes = [];
    taken = {};
    applyCustom();
    var mode = modeById(modeId);
    BP.parts.forEach(function (part) {
      if (!part.count) return;
      var res = pickPart(part, excluded, part === part2 && !(mode && mode.archetype_picker) ? archSelect.value : null);
      res.items.forEach(function (i) { taken[i.id] = 1; ids.push({ id: i.id, part: part.id }); });
      notes = notes.concat(res.notes);
    });
    if (!ids.length) return;
    var c = customFor();
    if (c && c.instant) {
      // Corrected as you answer: no timer, nothing stored (like "Practise a block").
      startInstant((mode ? mode.label : 'Practice') + ' · ' + ids.length + ' items', ids.filter(function (e) { return isMC(BY_ID[e.id]); }), notes);
      return;
    }
    var now = Date.now();
    store.current = { items: ids, minutes: minutes, startedAt: now, endAt: now + minutes * 60000, drafts: {}, answers: {}, invalid: {}, notes: notes, phase: 'running', exam: examKey, mode: modeId };
    save();
    startRunner();
  }

  // ---- Runner ------------------------------------------------------------------------
  var timerEl = document.getElementById('simTimer');
  var timerId = null;

  function labelFor(entry, n) {
    var item = BY_ID[entry.id];
    var isCase = item.category === 'short_theory_case';
    if (isTF(item)) return 'S' + n;
    if (isMC(item)) return 'Q' + n;
    return (isCase ? 'Case ' : 'Problem ') + n + ' [' + fmt(item.points) + 'p]';
  }

  function questionHead(item, n) {
    var head = el('div', 'sim-question__head', null);
    var isCase = item.category === 'short_theory_case';
    head.appendChild(el('h2', null, (isTF(item) ? 'Statement ' : isMC(item) ? 'Question ' : isCase ? 'Case ' : 'Problem ') + n));
    var entry = store.current && store.current.items.filter(function (e) { return e.id === item.id; })[0];
    var own = BP.parts.filter(function (p) { return entry ? p.id === entry.part : p.category === item.category; })[0];
    if (isMC(item)) {
      head.appendChild(el('span', null, (own ? own.label : 'Test') + (own ? ' · right ' + signed(own.points_correct) + ', wrong ' + signed(own.points_wrong) : '')));
      return head;
    }
    var partName = BP.parts.length > 1 && item.category === 'short_theory_case' ? 'Part I · short theory case'
      : BP.parts.length > 1 && item.category === 'extra_practice_problem' ? 'Part II · practical problem'
      : (own ? own.label : 'Problem');
    head.appendChild(el('span', null, partName + ' · ' + fmt(item.points) + ' points'));
    return head;
  }

  function startRunner() {
    var cur = store.current;
    var list = document.getElementById('simQuestions');
    var nav = document.getElementById('simNav');
    list.innerHTML = '';
    nav.innerHTML = '';
    var notice = document.getElementById('simRunNotice');
    notice.hidden = !cur.notes.length;
    notice.textContent = cur.notes.join(' ');
    var pts = document.getElementById('simPoints');
    pts.innerHTML = BP.parts.map(function (p) {
      return p.label.split(' — ')[0] + ': <strong>' + fmt1(p.points_total) + ' pts</strong>';
    }).join(' | ') + ' | Total: <strong>' + fmt1(BP.total_points) + ' pts</strong>';
    var printHead = document.getElementById('simPrintMeta');
    if (printHead) printHead.textContent = cur.minutes + ' minutes · ' + fmt1(BP.total_points) + ' points · ' + BP.parts.map(function (p) { return p.label + ' (' + fmt1(p.points_total) + ' pts)'; }).join(' · ');

    cur.items.forEach(function (entry, idx) {
      var item = BY_ID[entry.id];
      var n = idx + 1;
      var q = el('section', 'sim-question', null);
      q.id = 'q' + n;
      q.appendChild(questionHead(item, n));
      var st = el('div', 'sim-statement', null);
      st.innerHTML = item.statement_html;
      q.appendChild(st);
      if (!cur.answers) cur.answers = {};
      if (isMC(item)) {
        q.className += ' sim-question--mcq';
        var navLink = el('a', null, labelFor(entry, n));
        navLink.href = '#q' + n;
        if (cur.answers[entry.id]) navLink.setAttribute('data-answered', 'true');
        q.appendChild(mcOptions(item, 'mc-' + n, cur.answers[entry.id] || '', function (v) {
          cur.answers[entry.id] = v; save();
          if (v) navLink.setAttribute('data-answered', 'true'); else navLink.removeAttribute('data-answered');
        }, true));
        var own = partOf(entry);
        if (isTF(item) && own && own.justification_required) {
          q.appendChild(reasonBox('run-' + n, cur.drafts[entry.id], function (v) { cur.drafts[entry.id] = v; save(); }));
        }
        list.appendChild(q);
        nav.appendChild(navLink);
        return;
      }
      item.subquestions.forEach(function (sub) {
        var s = el('div', 'sim-sub', null);
        var p = el('div', 'sim-sub__prompt', null);
        p.appendChild(el('span', 'sim-sub__label', '(' + sub.label + ')'));
        var t = el('div', null, null);
        t.innerHTML = sub.prompt_html;
        p.appendChild(t);
        p.appendChild(el('span', 'sim-sub__pts', fmt(sub.points) + ' pts'));
        s.appendChild(p);
        q.appendChild(s);
      });
      var draft = el('div', 'sim-draft', null);
      var lab = el('label', 'sim-label', 'Your answer (draft, kept in this browser)');
      lab.setAttribute('for', 'draft-' + n);
      var ta = document.createElement('textarea');
      ta.id = 'draft-' + n;
      ta.placeholder = 'Write your answer or your key figures here before grading…';
      ta.value = cur.drafts[entry.id] || '';
      ta.addEventListener('input', function () { cur.drafts[entry.id] = ta.value; save(); });
      draft.appendChild(lab);
      draft.appendChild(ta);
      q.appendChild(draft);
      list.appendChild(q);
      var a = el('a', null, labelFor(entry, n));
      a.href = '#q' + n;
      nav.appendChild(a);
    });
    renderMath(list);
    show(runnerEl);
    tick();
    window.clearInterval(timerId);
    timerId = window.setInterval(tick, 1000);
    announce('Exam started: ' + cur.minutes + ' minutes.');
  }

  function tick() {
    var cur = store.current;
    if (!cur || cur.phase !== 'running') { window.clearInterval(timerId); return; }
    var left = Math.max(0, Math.round((cur.endAt - Date.now()) / 1000));
    var h = Math.floor(left / 3600), m = Math.floor((left % 3600) / 60), s = left % 60;
    timerEl.textContent = (h ? h + ':' + String(m).padStart(2, '0') : String(m).padStart(2, '0')) + ':' + String(s).padStart(2, '0');
    timerEl.setAttribute('data-warn', left <= 300 ? 'true' : 'false');
    if (left === 300) announce('Five minutes left.');
    if (left === 0) { finish(true); }
  }

  // ---- Grading -----------------------------------------------------------------------
  function finish(timeUp) {
    var cur = store.current;
    if (!cur) return;
    if (cur.phase === 'running') {
      cur.phase = 'grading';
      cur.finishedAt = timeUp ? Math.min(Date.now(), cur.endAt) : Date.now();
      cur.timeUp = !!timeUp;
      cur.scores = cur.scores || {};
      save();
    }
    window.clearInterval(timerId);
    startGrading();
  }

  function scoreSelect(max, step, value, onChange, label) {
    var sel = document.createElement('select');
    sel.className = 'sim-select';
    sel.setAttribute('aria-label', label);
    var values = [];
    for (var v = 0; v <= max + 1e-9; v += step) values.push(Math.round(v * 100) / 100);
    // A part worth a value that is not a multiple of the step (1.3, 0.6) still gets its full mark.
    if (values[values.length - 1] < Math.round(max * 100) / 100) values.push(Math.round(max * 100) / 100);
    values.forEach(function (x) {
      var o = document.createElement('option');
      o.value = String(x);
      o.textContent = fmt1(x) + ' pts';
      sel.appendChild(o);
    });
    if (value != null) sel.value = String(value);
    else sel.selectedIndex = -1;
    sel.addEventListener('change', function () { onChange(Number(sel.value)); });
    return sel;
  }

  var uid = 0;
  function revealPanel(container, label, title, html, kind, open) {
    var id = 'sim-panel-' + (++uid);
    var b = el('button', 'bank-btn', null);
    b.type = 'button';
    b.innerHTML = label;
    b.setAttribute('aria-controls', id);
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
    var panel = el('div', 'bank-panel bank-panel--' + kind, null);
    panel.id = id;
    panel.hidden = !open;
    panel.appendChild(el('p', 'bank-panel__title', title));
    var c = el('div', null, null);
    c.innerHTML = html;
    panel.appendChild(c);
    b.addEventListener('click', function () {
      var o = b.getAttribute('aria-expanded') === 'true';
      b.setAttribute('aria-expanded', o ? 'false' : 'true');
      panel.hidden = o;
    });
    container.appendChild(b);
    return panel;
  }

  function caseSteps() {
    var p1 = BP.parts.filter(function (p) { return p.category === 'short_theory_case'; })[0];
    return (p1 && p1.grading_steps) || [0, 0.5, 1, 1.5, 2];
  }

  function totals() {
    var cur = store.current, total = 0, done = true;
    BP.parts.forEach(function (part) {
      if (!isObjPart(part)) return;
      total += mcPartScore(part, cur.items.filter(function (e) { return e.part === part.id; }), cur.answers || {}, cur.invalid).score;
    });
    cur.items.forEach(function (entry) {
      var item = BY_ID[entry.id], sc = cur.scores[entry.id];
      if (isMC(item)) return;
      if (item.category === 'short_theory_case') {
        if (typeof sc !== 'number') done = false; else total += sc;
      } else {
        item.subquestions.forEach(function (sub) {
          var v = sc && typeof sc === 'object' ? sc[sub.label] : undefined;
          if (typeof v !== 'number') done = false; else total += v;
        });
      }
    });
    return { total: total, done: done };
  }

  function updateTotal() {
    var t = totals();
    document.getElementById('simScore').textContent = fmt1(t.total);
    var maxEl = document.getElementById('simMax');
    if (maxEl) maxEl.textContent = fmt1(BP.total_points);
    var btn = document.getElementById('simSave');
    btn.disabled = !t.done;
    document.getElementById('simScoreHint').textContent = t.done ? 'All questions graded.' : 'Grade every question to save the result.';
  }

  function startGrading() {
    var cur = store.current;
    var list = document.getElementById('simGradeList');
    list.innerHTML = '';
    document.getElementById('simTimeUp').hidden = !cur.timeUp;
    var used = Math.min(cur.minutes * 60, Math.round(((cur.finishedAt || Date.now()) - cur.startedAt) / 1000));
    document.getElementById('simUsed').textContent = 'Time used: ' + Math.floor(used / 60) + ' min ' + String(used % 60).padStart(2, '0') + ' s of ' + cur.minutes + ' min.';
    if (!cur.invalid) cur.invalid = {};
    var summaries = {};
    function fillSummary(part) {
      var card = summaries[part.id];
      var r = mcPartScore(part, cur.items.filter(function (e) { return e.part === part.id; }), cur.answers || {}, cur.invalid);
      // one objective part: 'the test' (Materials); several: 'this part' (Business Management Midterm 2)
      var partWord = objParts.length > 1 ? 'this part' : 'the test';
      card.innerHTML = '';
      card.appendChild(el('h2', null, part.label + ' · corrected automatically'));
      card.appendChild(el('p', null, r.right + ' right × ' + signed(part.points_correct) + ', ' + r.wrong + ' wrong × ' + signed(part.points_wrong) +
        ', ' + (r.blank + r.voided) + ' blank' + (r.voided ? ' (' + r.voided + ' voided)' : '') + ' × ' + fmt(part.points_blank || 0) + ' = ' + fmt1(r.raw) +
        (r.score !== r.raw ? ' → ' + fmt1(r.score) + ' (the mark of ' + partWord + ' never goes below ' + fmt(part.floor) + ')' : '') + '.'));
      if (part.justification_required) {
        card.appendChild(el('p', 'sim-muted', 'Compare each of your reasons with the official one below. In the exam no answer counts without a right reason: void a right answer whose reason was wrong or missing, and it will count as a blank.'));
      }
      var strong = el('p', 'sim-mcq-summary__score', null);
      strong.innerHTML = 'Mark of ' + partWord + ': <strong>' + fmt1(r.score) + '</strong> / ' + fmt1(part.points_total);
      card.appendChild(strong);
    }
    BP.parts.forEach(function (part) {
      if (!isObjPart(part)) return;
      var card = el('section', 'sim-card sim-mcq-summary', null);
      card.id = 'simSummary-' + part.id;
      summaries[part.id] = card;
      fillSummary(part);
      list.appendChild(card);
    });
    cur.items.forEach(function (entry, idx) {
      var item = BY_ID[entry.id];
      var n = idx + 1;
      var isCase = item.category === 'short_theory_case';
      var q = el('section', 'sim-question', null);
      q.id = 'g' + n;
      var head = questionHead(item, n);
      if (isMC(item)) {
        var mcp = partOf(entry), ch = (cur.answers || {})[entry.id] || '';
        var mlink = el('a', null, item.id + ' · ' + item.title);
        mlink.href = itemHref(item.id);
        head.appendChild(mlink);
        q.appendChild(head);
        q.className += ' sim-question--mcq';
        q.setAttribute('data-result', !ch ? 'blank' : ch === item.answer ? 'right' : 'wrong');
        var stm = el('div', 'sim-statement', null);
        stm.innerHTML = item.statement_html;
        q.appendChild(stm);
        var verdict = el('p', 'sim-mcq__verdict', null);
        function setVerdict() {
          var v = !!cur.invalid[entry.id];
          verdict.textContent = verdictText(item, ch, v) + ' · ' + signed(mcPoints(mcp, item, ch, v)) + ' points';
        }
        setVerdict();
        q.appendChild(verdict);
        q.appendChild(mcReview(item, ch, isTF(item) ? cur.drafts[entry.id] : null));
        if (isTF(item) && mcp && mcp.justification_required && ch && ch === item.answer) {
          var vl = el('label', 'sim-check sim-void', null);
          var vc = document.createElement('input');
          vc.type = 'checkbox'; vc.checked = !!cur.invalid[entry.id];
          vc.addEventListener('change', function () {
            if (vc.checked) cur.invalid[entry.id] = true; else delete cur.invalid[entry.id];
            save(); setVerdict(); fillSummary(mcp); updateTotal();
          });
          vl.appendChild(vc);
          vl.appendChild(el('span', null, ' My reason was wrong or missing: do not count this answer'));
          q.appendChild(vl);
        }
        list.appendChild(q);
        return;
      }
      var link = el('a', null, item.id + ' · ' + item.title);
      link.href = itemHref(item.id);
      head.appendChild(link);
      q.appendChild(head);
      var draftText = cur.drafts[entry.id];
      q.appendChild(el('p', 'sim-label', 'Your draft'));
      q.appendChild(el('div', 'sim-draft__readonly', draftText ? draftText : '(empty)'));
      var st = el('div', 'sim-no-print', null);
      var stPanelHost = el('div', 'bank-sub__buttons', null);
      st.appendChild(stPanelHost);
      st.appendChild(revealPanel(stPanelHost, 'Statement', 'Statement', item.statement_html, 'hint', false));
      q.appendChild(st);
      item.subquestions.forEach(function (sub) {
        var s = el('div', 'sim-sub', null);
        var p = el('div', 'sim-sub__prompt', null);
        p.appendChild(el('span', 'sim-sub__label', '(' + sub.label + ')'));
        var t = el('div', null, null);
        t.innerHTML = sub.prompt_html;
        p.appendChild(t);
        p.appendChild(el('span', 'sim-sub__pts', fmt(sub.points) + ' pts'));
        s.appendChild(p);
        var check = el('div', 'bank-panel bank-panel--check', null);
        check.appendChild(el('p', 'bank-panel__title', isCase ? 'Key concepts the answer must contain' : 'Key figures of the result'));
        var cc = el('div', null, null);
        cc.innerHTML = sub.checkpoint_html;
        check.appendChild(cc);
        s.appendChild(check);
        var host = el('div', 'bank-sub__buttons', null);
        s.appendChild(host);
        s.appendChild(revealPanel(host, 'Full step-by-step solution', 'Step-by-step solution', sub.solution_html, 'solution', false));
        if (!isCase) {
          var g = el('div', 'sim-grade', null);
          g.appendChild(el('span', null, 'Your points for (' + sub.label + '):'));
          var prev = cur.scores[entry.id] && cur.scores[entry.id][sub.label];
          g.appendChild(scoreSelect(sub.points, 0.25, prev, function (v) {
            if (!cur.scores[entry.id] || typeof cur.scores[entry.id] !== 'object') cur.scores[entry.id] = {};
            cur.scores[entry.id][sub.label] = v;
            save();
            updateTotal();
          }, 'Points for problem ' + n + ' part ' + sub.label));
          s.appendChild(g);
        }
        q.appendChild(s);
      });
      if (isCase) {
        var gc = el('div', 'sim-grade', null);
        gc.appendChild(el('span', null, 'Your points for case ' + n + ' (whole case):'));
        var sel = document.createElement('select');
        sel.className = 'sim-select';
        sel.setAttribute('aria-label', 'Points for case ' + n);
        caseSteps().forEach(function (v) {
          var o = document.createElement('option');
          o.value = String(v);
          o.textContent = fmt1(v) + ' pts';
          sel.appendChild(o);
        });
        if (typeof cur.scores[entry.id] === 'number') sel.value = String(cur.scores[entry.id]); else sel.selectedIndex = -1;
        sel.addEventListener('change', function () { cur.scores[entry.id] = Number(sel.value); save(); updateTotal(); });
        gc.appendChild(sel);
        q.appendChild(gc);
      }
      list.appendChild(q);
    });
    renderMath(list);
    show(resultsEl);
    updateTotal();
    var hasOpen = BP.parts.some(function (p) { return !isObjPart(p); });
    announce(mcPart ? (hasOpen ? 'Exam finished. The objective parts are corrected; grade the problems with the key results.' : 'Exam finished. Every answer is corrected.')
      : 'Exam finished. Grade each question with the key results.');
  }

  function saveResult() {
    var cur = store.current;
    var t = totals();
    if (!t.done) return;
    var low = [];
    var items = cur.items.map(function (entry) {
      var item = BY_ID[entry.id], sc = cur.scores[entry.id];
      if (isMC(item)) {
        var ch = (cur.answers || {})[entry.id] || '', voided = !!(cur.invalid || {})[entry.id] && ch === item.answer;
        if (ch !== item.answer || voided) low.push(item.id);
        return { id: item.id, part: entry.part, score: mcPoints(partOf(entry), item, ch, voided), points: item.points, choice: ch, voided: voided || undefined };
      }
      var score = typeof sc === 'number' ? sc : item.subquestions.reduce(function (s, sub) { return s + (sc[sub.label] || 0); }, 0);
      if (score < item.points / 2) low.push(item.id);
      return { id: item.id, part: entry.part, score: score, points: item.points };
    });
    var partResults = BP.parts.filter(isObjPart).map(function (p) {
      var r = mcPartScore(p, cur.items.filter(function (e) { return e.part === p.id; }), cur.answers || {}, cur.invalid);
      return { id: p.id, label: p.label.split(' — ')[0], right: r.right, wrong: r.wrong, blank: r.blank + r.voided, voided: r.voided, raw: r.raw, score: r.score, max: p.points_total };
    });
    store.history.push({ startedAt: cur.startedAt, finishedAt: cur.finishedAt || Date.now(), minutes: cur.minutes,
                         timeUp: !!cur.timeUp, items: items, parts: partResults, total: t.total, max: BP.total_points, exam: examKey, mode: modeId, modeLabel: BP.mode ? BP.mode.label : '' });
    store.current = null;
    save();
    var box = document.getElementById('simSaved');
    var html = '<p><strong>Grade saved: ' + fmt1(t.total) + ' / ' + fmt1(BP.total_points) + '.</strong></p>';
    html += low.length
      ? '<p>' + (mcPart ? 'Wrong or blank test questions and items below half of their points' : 'Below half of their points') + ', worth practising again on the Extra problems page:</p><ul class="sim-result-list">' +
        low.map(function (id) { return '<li><a href="' + itemHref(id) + '">' + id + ' · ' + BY_ID[id].title + '</a></li>'; }).join('') + '</ul>'
      : '<p>Every item reached at least half of its points.</p>';
    box.innerHTML = html;
    box.hidden = false;
    document.getElementById('simSave').hidden = true;
    document.querySelectorAll('#simGradeList select').forEach(function (s) { s.disabled = true; });
    renderHistory();
    announce('Grade saved: ' + fmt1(t.total) + ' out of ' + fmt1(BP.total_points) + '.');
  }

  // ---- Practise a block (multiple choice, corrected as you answer) --------------------
  // The objective part of the whole exam that scores a kind of item (blocks of Materials carry no kind: multiple choice).
  function partForKind(kind) {
    return BP_FULL.parts.filter(function (p) { return p.type === (kind || 'multiple_choice'); })[0] || null;
  }
  var practiceBlocks = Array.isArray(BANK.blocks) ? BANK.blocks.filter(function (b) {
    return partForKind(b.kind) && (!b.exam || !examKey || b.exam === examKey);
  }) : [];
  function setupBlockPractice() {
    if (!practiceBlocks.length) return;
    var card = el('div', 'sim-card sim-block-card', null);
    card.appendChild(el('h2', null, 'Practise a block'));
    card.appendChild(el('p', 'sim-muted', 'Ten items of one block, corrected as you answer, with the reason for every answer. No timer and nothing is saved.'));
    var row = el('div', 'sim-options', null);
    function field(id, text) {
      var w = el('div', null, null), lab = el('label', 'sim-label', text), sel = document.createElement('select');
      lab.setAttribute('for', id); sel.id = id; sel.className = 'sim-select';
      w.appendChild(lab); w.appendChild(sel); row.appendChild(w);
      return sel;
    }
    var unitSel = field('simBlockUnit', 'Unit'), blockSel = field('simBlockSelect', 'Block');
    var units = [];
    practiceBlocks.forEach(function (b) { if (units.indexOf(b.unit) < 0) units.push(b.unit); });
    units.forEach(function (u) {
      var o = document.createElement('option');
      o.value = String(u); o.textContent = UNIT_LABELS[String(u)] || ('Unit ' + u);
      unitSel.appendChild(o);
    });
    var kinds = {};
    practiceBlocks.forEach(function (b) { kinds[b.kind || 'multiple_choice'] = 1; });
    var mixed = Object.keys(kinds).length > 1;
    function fillBlocks() {
      blockSel.innerHTML = '';
      practiceBlocks.filter(function (b) { return String(b.unit) === unitSel.value; }).forEach(function (b) {
        var o = document.createElement('option');
        o.value = b.id; o.textContent = b.id + ' · ' + (mixed ? (b.kind === 'true_false' ? 'True/False · ' : 'Multiple choice · ') : '') + b.title;
        blockSel.appendChild(o);
      });
    }
    unitSel.addEventListener('change', fillBlocks);
    fillBlocks();
    card.appendChild(row);
    var actions = el('div', 'sim-actions', null);
    var go = el('button', 'bank-btn sim-primary', 'Practise this block');
    go.type = 'button'; go.id = 'simBlockStart';
    go.addEventListener('click', function () { startBlock(blockSel.value); });
    actions.appendChild(go);
    card.appendChild(actions);
    var hist = setupEl.querySelector('.sim-history-card');
    setupEl.insertBefore(card, hist || null);
    makeInstantScreen();
  }
  function makeInstantScreen() {
    if (blockEl) return;
    blockEl = el('section', null, null);
    blockEl.id = 'simBlock'; blockEl.hidden = true;
    blockEl.setAttribute('aria-label', 'Practice corrected as you answer');
    resultsEl.parentNode.insertBefore(blockEl, resultsEl.nextSibling);
  }

  function startBlock(blockId) {
    var block = practiceBlocks.filter(function (b) { return b.id === blockId; })[0];
    if (!block) return;
    var part = partForKind(block.kind);
    var entries = block.items.map(function (id) { return { id: id, part: part.id }; });
    startInstant(block.id + ' · ' + block.title, entries, [], BANK_DIR + ((BANK.pages || {})[part.category] || '') + '#' + block.id);
  }

  // Objective items corrected as they are answered: a block, or a practice drawn by a flexible mode. Nothing is stored.
  function startInstant(title, entries, notes, pageHref) {
    if (!blockEl) makeInstantScreen();
    var answers = {};
    blockEl.innerHTML = '';
    var top = el('div', 'sim-card', null);
    top.appendChild(el('h2', null, title));
    if (notes && notes.length) top.appendChild(el('p', 'sim-notice', notes.join(' ')));
    var tally = el('p', 'sim-block-tally', null);
    tally.id = 'simBlockTally';
    tally.setAttribute('aria-live', 'polite');
    top.appendChild(tally);
    var back = el('button', 'bank-btn', 'Back to the simulator');
    back.type = 'button'; back.id = 'simBlockBack';
    back.addEventListener('click', function () { show(setupEl); });
    var acts = el('div', 'sim-actions', null);
    acts.appendChild(back);
    if (pageHref) {
      var pageLink = el('a', 'bank-btn', 'Open this block on the Extra problems page');
      pageLink.href = pageHref;
      acts.appendChild(pageLink);
    }
    top.appendChild(acts);
    blockEl.appendChild(top);
    var reasons = {};
    function updateTally() {
      var done = Object.keys(answers).length, parts = {}, txt = [];
      entries.forEach(function (e) { (parts[e.part] = parts[e.part] || []).push(e); });
      Object.keys(parts).forEach(function (pid) {
        var p = partOf({ part: pid });
        var r = mcPartScore(p, parts[pid].filter(function (e) { return answers[e.id]; }), answers);
        txt.push((Object.keys(parts).length > 1 ? p.label.split(' — ')[0] + ': ' : '') + r.right + ' right, ' + r.wrong + ' wrong · with the exam rule: ' +
          fmt1(r.score) + ' / ' + fmt1(parts[pid].length * p.points_correct) + (r.score !== r.raw ? ' (' + fmt1(r.raw) + ' before the floor)' : ''));
      });
      tally.textContent = done + ' of ' + entries.length + ' answered · ' + txt.join(' | ');
    }
    entries.forEach(function (entry, idx) {
      var item = BY_ID[entry.id], n = idx + 1, p = partOf(entry);
      var q = el('section', 'sim-question sim-question--mcq', null);
      q.id = 'b' + n;
      var head = el('div', 'sim-question__head', null);
      head.appendChild(el('h2', null, (isTF(item) ? 'Statement ' : 'Question ') + n));
      head.appendChild(el('span', null, item.id));
      q.appendChild(head);
      var st = el('div', 'sim-statement', null);
      st.innerHTML = item.statement_html;
      q.appendChild(st);
      var rb = isTF(item) && p && p.justification_required
        ? reasonBox('ins-' + n, '', function (v) { reasons[entry.id] = v; }) : null;
      var opts = mcOptions(item, 'blk-' + n, '', function (v) {
        answers[entry.id] = v;
        q.setAttribute('data-result', v === item.answer ? 'right' : 'wrong');
        var review = mcReview(item, v, reasons[entry.id]);
        var verdict = el('p', 'sim-mcq__verdict', verdictText(item, v, false));
        q.replaceChild(review, opts);
        if (rb) q.removeChild(rb);
        q.insertBefore(verdict, review);
        renderMath(review);
        updateTally();
        announce((isTF(item) ? 'Statement ' : 'Question ') + n + ': ' + (v === item.answer ? 'right' : 'wrong, the answer is ' + answerWord(item, item.answer)));
      }, false);
      if (rb) q.appendChild(rb);
      q.appendChild(opts);
      blockEl.appendChild(q);
    });
    updateTally();
    renderMath(blockEl);
    show(blockEl);
    announce(title + ': corrected as you answer.');
  }
  setupBlockPractice();

  // ---- Wiring ------------------------------------------------------------------------
  document.getElementById('simGenerate').addEventListener('click', generate);
  document.getElementById('simFinish').addEventListener('click', function () {
    if (window.confirm('Finish the exam and see the solutions? You cannot go back to the exam afterwards.')) finish(false);
  });
  document.getElementById('simPrint').addEventListener('click', function () { window.print(); });
  document.getElementById('simSave').addEventListener('click', saveResult);
  document.getElementById('simNew').addEventListener('click', function () {
    if (store.current && store.current.phase === 'grading' && !window.confirm('Leave this exam without saving the grade?')) return;
    store.current = null;
    save();
    document.getElementById('simSaved').hidden = true;
    document.getElementById('simSave').hidden = false;
    renderHistory();
    show(setupEl);
  });
  var abandon = document.getElementById('simAbandon');
  if (abandon) abandon.addEventListener('click', function () {
    if (!window.confirm('Abandon this exam? It will not be graded.')) return;
    window.clearInterval(timerId);
    store.current = null;
    save();
    renderHistory();
    show(setupEl);
  });

  // Keep the exam bar below the sticky page header.
  function placeBar() {
    var header = document.querySelector('.back-bar');
    root.style.setProperty('--sim-bar-top', (header ? header.getBoundingClientRect().height : 0) + 'px');
  }
  window.addEventListener('resize', placeBar);
  placeBar();

  // ---- Shortcuts ---------------------------------------------------------------------
  var help = document.getElementById('simHelp');
  function openHelp() { if (help) { if (typeof help.showModal === 'function') { if (!help.open) help.showModal(); } else help.setAttribute('open', ''); } }
  function closeHelp() {
    if (help && (help.open || help.hasAttribute('open'))) { if (typeof help.close === 'function') help.close(); else help.removeAttribute('open'); return true; }
    return false;
  }
  var hc = document.getElementById('simHelpClose');
  if (hc) hc.addEventListener('click', closeHelp);
  var ho = document.getElementById('simHelpOpen');
  if (ho) ho.addEventListener('click', openHelp);
  var toast = document.getElementById('simToast');
  var toastTimer = null;
  function nextPalette() {
    var api = window.AESurface;
    if (!api || typeof api.list !== 'function') return;
    var list = api.list(), cur = api.get(), idx = 0;
    for (var i = 0; i < list.length; i++) if (list[i].id === cur) idx = i;
    var next = list[(idx + 1) % list.length];
    api.set(next.id);
    announce('Reading palette: ' + next.label);
    if (toast) { toast.textContent = 'Reading palette: ' + next.label; toast.hidden = false; window.clearTimeout(toastTimer); toastTimer = window.setTimeout(function () { toast.hidden = true; }, 1800); }
  }
  document.addEventListener('keydown', function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    var typing = t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName));
    if (e.key === 'Escape') { if (closeHelp()) e.preventDefault(); return; }
    if (typing || e.defaultPrevented) return;
    if (e.key === 't' || e.key === 'T') { e.preventDefault(); nextPalette(); }
    else if (e.key === '?') { e.preventDefault(); openHelp(); }
  });

  // ---- Start -------------------------------------------------------------------------
  renderHistory();
  if (store.current && store.current.phase === 'running') {
    if (Date.now() >= store.current.endAt) finish(true); else startRunner();
  } else if (store.current && store.current.phase === 'grading') {
    startGrading();
  } else {
    show(setupEl);
  }
})();
