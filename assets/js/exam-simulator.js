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
  var BP = window[(examId && /^[\w-]+$/.test(examId) && root.getAttribute('data-blueprint-' + examId)) ||
                  root.getAttribute('data-blueprint') || 'AE_BM_BLUEPRINT'];
  var KEY = root.getAttribute('data-storage') || 'ae_bm_exams';
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
  if (!BANK || !BANK.items || !BP || !BP.parts || !setupEl || !runnerEl || !resultsEl) {
    root.insertAdjacentHTML('afterbegin', '<p class="sim-card">The exam simulator could not load the problem bank.</p>');
    return;
  }
  var BY_ID = {};
  BANK.items.forEach(function (i) { BY_ID[i.id] = i; });
  // Texts that depend on the blueprint (title, structure note, button label), and the current exam link.
  Array.prototype.forEach.call(root.querySelectorAll('[data-bp]'), function (n) {
    var v = BP[n.getAttribute('data-bp')];
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
  function show(screen) {
    [setupEl, runnerEl, resultsEl].forEach(function (s) { s.hidden = s !== screen; });
    window.scrollTo(0, 0);
  }
  var live = document.getElementById('simLive');
  function announce(msg) { if (live) { live.textContent = ''; window.setTimeout(function () { live.textContent = msg; }, 30); } }

  // ---- Setup screen ------------------------------------------------------------------
  // The part whose problem type can be chosen: the one that lists archetypes (Business Management: the Extra Practice problem).
  var part2 = BP.parts.filter(function (p) { return p.selection_rules && p.selection_rules.archetypes; })[0] ||
    BP.parts.filter(function (p) { return p.category === 'extra_practice_problem'; })[0];
  var durationBox = document.getElementById('simDurations');
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
  var archSelect = document.getElementById('simArchetype');
  if (part2 && part2.selection_rules && part2.selection_rules.archetypes) {
    part2.selection_rules.archetypes.forEach(function (a) {
      var o = document.createElement('option');
      o.value = a;
      o.textContent = (BANK.archetypes && BANK.archetypes[a]) || a;
      archSelect.appendChild(o);
    });
  }

  var structure = document.getElementById('simStructure');
  if (structure) {
    var rows = BP.parts.map(function (p) {
      return '<tr><td>' + p.label + '</td><td class="num">' + p.count + ' × ' + fmt1(p.points_each) + '</td><td class="num">' + fmt1(p.points_total) + '</td></tr>';
    }).join('');
    structure.innerHTML = '<thead><tr><th>Part</th><th class="num">Items × points</th><th class="num">Points</th></tr></thead><tbody>' + rows +
      '<tr><td><strong>Total</strong></td><td class="num">' + BP.duration_minutes + ' min</td><td class="num"><strong>' + fmt1(BP.total_points) + '</strong></td></tr></tbody>';
  }

  function renderHistory() {
    var box = document.getElementById('simHistory');
    if (!box) return;
    if (!store.history.length) { box.innerHTML = '<p class="sim-muted">No simulated exam yet. Your grades will appear here.</p>'; return; }
    var rows = store.history.slice().reverse().slice(0, 10).map(function (h) {
      var d = new Date(h.finishedAt);
      var links = h.items.map(function (r) { return '<a href="' + itemHref(r.id) + '">' + r.id + '</a> ' + fmt(r.score) + '/' + fmt(r.points); }).join(' · ');
      return '<tr><td>' + d.toLocaleDateString('en-GB') + ' ' + d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }) +
        '</td><td>' + links + '</td><td class="num"><strong>' + fmt1(h.total) + '</strong> / ' + fmt1(h.max) + '</td></tr>';
    }).join('');
    var avg = store.history.reduce(function (s, h) { return s + h.total; }, 0) / store.history.length;
    box.innerHTML = '<p class="sim-muted">' + store.history.length + ' exam(s) graded · average ' + fmt1(avg) + ' / ' + fmt1(BP.total_points) + '</p>' +
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
        (!archetype || archetype === 'any' || i.archetype === archetype);
    });
    var notes = [];
    var free = pool.filter(function (i) { return !excluded[i.id]; });
    if (free.length < part.count) {
      notes.push(part.label + ': not enough new items, so some excluded ones were allowed again.');
      free = pool;
    }
    shuffle(free);
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
    if (document.getElementById('simSkipPrevious').checked && store.history.length) {
      store.history[store.history.length - 1].items.forEach(function (r) { excluded[r.id] = 1; });
    }
    var minutes = Number((document.querySelector('input[name="simDuration"]:checked') || {}).value || BP.duration_minutes);
    var ids = [], notes = [];
    taken = {};
    BP.parts.forEach(function (part) {
      var res = pickPart(part, excluded, part === part2 ? archSelect.value : null);
      res.items.forEach(function (i) { taken[i.id] = 1; ids.push({ id: i.id, part: part.id }); });
      notes = notes.concat(res.notes);
    });
    var now = Date.now();
    store.current = { items: ids, minutes: minutes, startedAt: now, endAt: now + minutes * 60000, drafts: {}, notes: notes, phase: 'running' };
    save();
    startRunner();
  }

  // ---- Runner ------------------------------------------------------------------------
  var timerEl = document.getElementById('simTimer');
  var timerId = null;

  function labelFor(entry, n) {
    var item = BY_ID[entry.id];
    var isCase = item.category === 'short_theory_case';
    return (isCase ? 'Case ' : 'Problem ') + n + ' [' + fmt(item.points) + 'p]';
  }

  function questionHead(item, n) {
    var head = el('div', 'sim-question__head', null);
    var isCase = item.category === 'short_theory_case';
    head.appendChild(el('h2', null, (isCase ? 'Case ' : 'Problem ') + n));
    var entry = store.current && store.current.items.filter(function (e) { return e.id === item.id; })[0];
    var own = BP.parts.filter(function (p) { return entry ? p.id === entry.part : p.category === item.category; })[0];
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
    for (var v = 0; v <= max + 1e-9; v += step) {
      var o = document.createElement('option');
      o.value = String(Math.round(v * 100) / 100);
      o.textContent = fmt1(v) + ' pts';
      sel.appendChild(o);
    }
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
    cur.items.forEach(function (entry) {
      var item = BY_ID[entry.id], sc = cur.scores[entry.id];
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
    cur.items.forEach(function (entry, idx) {
      var item = BY_ID[entry.id];
      var n = idx + 1;
      var isCase = item.category === 'short_theory_case';
      var q = el('section', 'sim-question', null);
      q.id = 'g' + n;
      var head = questionHead(item, n);
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
    announce('Exam finished. Grade each question with the key results.');
  }

  function saveResult() {
    var cur = store.current;
    var t = totals();
    if (!t.done) return;
    var low = [];
    var items = cur.items.map(function (entry) {
      var item = BY_ID[entry.id], sc = cur.scores[entry.id];
      var score = typeof sc === 'number' ? sc : item.subquestions.reduce(function (s, sub) { return s + (sc[sub.label] || 0); }, 0);
      if (score < item.points / 2) low.push(item.id);
      return { id: item.id, part: entry.part, score: score, points: item.points };
    });
    store.history.push({ startedAt: cur.startedAt, finishedAt: cur.finishedAt || Date.now(), minutes: cur.minutes,
                         timeUp: !!cur.timeUp, items: items, total: t.total, max: BP.total_points });
    store.current = null;
    save();
    var box = document.getElementById('simSaved');
    var html = '<p><strong>Grade saved: ' + fmt1(t.total) + ' / ' + fmt1(BP.total_points) + '.</strong></p>';
    html += low.length
      ? '<p>Below half of their points, worth practising again on the Extra problems page:</p><ul class="sim-result-list">' +
        low.map(function (id) { return '<li><a href="' + itemHref(id) + '">' + id + ' · ' + BY_ID[id].title + '</a></li>'; }).join('') + '</ul>'
      : '<p>Every item reached at least half of its points.</p>';
    box.innerHTML = html;
    box.hidden = false;
    document.getElementById('simSave').hidden = true;
    document.querySelectorAll('#simGradeList select').forEach(function (s) { s.disabled = true; });
    renderHistory();
    announce('Grade saved: ' + fmt1(t.total) + ' out of ' + fmt1(BP.total_points) + '.');
  }

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
