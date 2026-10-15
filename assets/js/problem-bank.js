/*!
 * Aerospace Engineering Study Portal: Problem Bank page.
 *
 * Draws a subject's problem bank (window[<data-bank>], written by tools/build_problem_bank.py into
 * subjects/<subject>/data/problems.js) inside <div id="problemBank" data-bank="AE_BM_BANK" data-storage="ae_bm_progress">.
 * Load it with defer, after KaTeX's auto-render and after the bank data:
 *     <script defer src="../data/problems.js"></script>
 *     <script defer src="../../../assets/js/problem-bank.js"></script>
 *
 * Per item: a collapsible card (statement, setup, subquestions) whose Hint, Check and Solution panels stay hidden
 * until asked for (anti-spoiler), and Mastered / Review buttons. Status lives in localStorage under the page's key
 * (never a key containing "theme"): { "<id>": "mastered" | "review" }; anything else counts as pending. The Exam
 * Simulator writes "review" into the same key for the items failed in an exam.
 *
 * Filters: category (tablist), archetype, unit, difficulty, status, and a search over id, title, tags and statement.
 * Shortcuts (ignored while typing or with Ctrl/Alt/Meta): T next reading palette (window.AESurface), / search,
 * Esc close the help or clear the search, ? shortcuts help. A card opens from the URL hash (#P11).
 */
(function () {
  'use strict';

  var root = document.getElementById('problemBank');
  if (!root) return;
  var DATA = window[root.getAttribute('data-bank') || 'AE_BM_BANK'];
  var KEY = root.getAttribute('data-storage') || 'ae_bm_progress';
  var list = document.getElementById('bankList');
  if (!DATA || !DATA.items || !list) {
    if (list) list.innerHTML = '<p class="bank-empty">The problem bank could not be loaded.</p>';
    return;
  }
  var ITEMS = DATA.items;
  var STATUS_LABEL = { mastered: 'Mastered', review: 'Review', pending: 'Pending' };

  // ---- Progress storage ---------------------------------------------------------------
  var progress = {};
  try {
    var stored = JSON.parse(window.localStorage.getItem(KEY) || '{}');
    if (stored && typeof stored === 'object') progress = stored;
  } catch (e) { progress = {}; }

  function statusOf(id) {
    var s = progress[id];
    return s === 'mastered' || s === 'review' ? s : 'pending';
  }
  function setStatus(id, status) {
    if (status === 'pending') delete progress[id]; else progress[id] = status;
    try { window.localStorage.setItem(KEY, JSON.stringify(progress)); } catch (e) { /* in memory only */ }
  }

  // ---- Helpers -----------------------------------------------------------------------
  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }
  function plain(html) {
    var div = document.createElement('div');
    div.innerHTML = html || '';
    return div.textContent || '';
  }
  function fold(s) {
    return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }
  function points(p) { return (Math.round(p * 100) / 100).toString(); }
  function renderMath(node) {
    if (typeof window.renderMathInElement !== 'function') return false;
    window.renderMathInElement(node, {
      delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }],
      throwOnError: false
    });
    return true;
  }
  var uid = 0;

  // One button that shows / hides one panel (anti-spoiler).
  function reveal(container, label, title, html, kind) {
    var id = 'bank-panel-' + (++uid);
    var button = el('button', 'bank-btn', null);
    button.type = 'button';
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-controls', id);
    button.innerHTML = label;
    var panel = el('div', 'bank-panel bank-panel--' + kind, null);
    panel.id = id;
    panel.hidden = true;
    panel.appendChild(el('p', 'bank-panel__title', title));
    var content = el('div', 'bank-panel__content', null);
    content.innerHTML = html;
    panel.appendChild(content);
    button.addEventListener('click', function () {
      var open = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', open ? 'false' : 'true');
      panel.hidden = open;
    });
    return { button: button, panel: panel };
  }

  // ---- Cards -------------------------------------------------------------------------
  var cards = [];

  function difficultyText(d) { return 'Difficulty ' + ['', '●○○', '●●○', '●●●'][d]; }

  function buildCard(item) {
    var isCase = item.category === 'short_theory_case';
    var article = el('article', 'bank-card', null);
    article.id = item.id;
    var details = el('details', 'bank-card__details', null);
    var summary = el('summary', 'bank-card__summary', null);
    summary.appendChild(el('span', 'bank-card__id', item.id));
    summary.appendChild(el('span', 'bank-card__title', item.title));
    summary.appendChild(el('span', 'bank-card__chev', 'Open'));
    var meta = el('span', 'bank-card__meta', null);
    var catLabel = isCase ? 'Short theory case' : 'Extra Practice problem';
    [catLabel + ' · ' + points(item.points) + ' pts',
     isCase ? item.theme.replace(/-/g, ' ') : (DATA.archetypes[item.archetype] || item.archetype),
     DATA.units[String(item.unit)] || ('Topic ' + item.unit),
     difficultyText(item.difficulty),
     item.time_minutes + ' min',
     item.official ? 'Official exercise' : 'Practice item'].forEach(function (t) {
      meta.appendChild(el('span', 'bank-chip', t));
    });
    var chip = el('span', 'bank-chip bank-chip--status', '');
    meta.appendChild(chip);
    summary.appendChild(meta);
    details.appendChild(summary);

    var body = el('div', 'bank-card__body', null);
    var actions = el('div', 'bank-card__actions', null);
    var bMastered = el('button', 'bank-btn bank-btn--mastered', null);
    bMastered.type = 'button';
    bMastered.innerHTML = 'Mastered';
    var bReview = el('button', 'bank-btn bank-btn--review', null);
    bReview.type = 'button';
    bReview.innerHTML = 'Review';
    actions.appendChild(bMastered);
    actions.appendChild(bReview);
    if (item.page) {
      var link = el('a', 'bank-btn', null);
      link.href = '../../../' + item.page;
      link.innerHTML = 'Open the worked page <span aria-hidden="true">→</span>';
      actions.appendChild(link);
    }
    body.appendChild(actions);

    body.appendChild(el('p', 'bank-section-title', 'Statement'));
    var statement = el('div', 'bank-statement problem-statement-box', null);
    statement.innerHTML = item.statement_html;
    body.appendChild(statement);

    if (item.setup_html) {
      var extra = el('div', 'bank-extra', null);
      var setup = reveal(extra, 'Setup and hypotheses', 'Setup and hypotheses', item.setup_html, 'hint');
      extra.appendChild(setup.button);
      body.appendChild(extra);
      body.appendChild(setup.panel);
    }

    item.subquestions.forEach(function (sub) {
      var section = el('section', 'bank-sub', null);
      var prompt = el('div', 'bank-sub__prompt', null);
      prompt.appendChild(el('span', 'bank-sub__label', '(' + sub.label + ')'));
      var ptext = el('div', 'bank-sub__text', null);
      ptext.innerHTML = sub.prompt_html;
      prompt.appendChild(ptext);
      prompt.appendChild(el('span', 'bank-sub__pts', points(sub.points) + ' pts'));
      section.appendChild(prompt);
      var buttons = el('div', 'bank-sub__buttons', null);
      var hint = reveal(buttons, 'Hint', 'Hint', sub.hint_html, 'hint');
      var check = reveal(buttons, isCase ? 'Checklist' : 'Check key result',
                         isCase ? 'Key concepts the answer must contain' : 'Key figures of the result', sub.checkpoint_html, 'check');
      var sol = reveal(buttons, 'Full step-by-step solution', 'Step-by-step solution', sub.solution_html, 'solution');
      [hint, check, sol].forEach(function (r) { buttons.appendChild(r.button); });
      section.appendChild(buttons);
      [hint, check, sol].forEach(function (r) { section.appendChild(r.panel); });
      body.appendChild(section);
    });

    if (item.interpretation_html) {
      var extra2 = el('div', 'bank-extra', null);
      var interp = reveal(extra2, 'Interpretation and checks', 'Interpretation and checks', item.interpretation_html, 'solution');
      extra2.appendChild(interp.button);
      body.appendChild(el('p', 'bank-section-title', 'After solving'));
      body.appendChild(extra2);
      body.appendChild(interp.panel);
    }
    body.appendChild(el('p', 'bank-card__source', 'Source: ' + item.source));
    details.appendChild(body);
    article.appendChild(details);

    var card = {
      item: item, node: article, details: details, chip: chip, mastered: bMastered, review: bReview,
      text: fold([item.id, item.title, (item.tags || []).join(' '), item.theme, DATA.archetypes[item.archetype] || '',
                  plain(item.statement_html)].join(' '))
    };
    bMastered.addEventListener('click', function () { toggle(card, 'mastered'); });
    bReview.addEventListener('click', function () { toggle(card, 'review'); });
    paint(card);
    return card;
  }

  function paint(card) {
    var s = statusOf(card.item.id);
    card.node.setAttribute('data-status', s);
    card.chip.setAttribute('data-status', s);
    card.chip.textContent = 'Status: ' + STATUS_LABEL[s];
    card.mastered.setAttribute('aria-pressed', s === 'mastered' ? 'true' : 'false');
    card.review.setAttribute('aria-pressed', s === 'review' ? 'true' : 'false');
  }

  function toggle(card, status) {
    var next = statusOf(card.item.id) === status ? 'pending' : status;
    setStatus(card.item.id, next);
    paint(card);
    updateProgress();
    announce(card.item.id + ': ' + STATUS_LABEL[next]);
  }

  // ---- Progress bar ------------------------------------------------------------------
  function updateProgress() {
    var n = ITEMS.length, m = 0, r = 0;
    ITEMS.forEach(function (i) { var s = statusOf(i.id); if (s === 'mastered') m++; else if (s === 'review') r++; });
    var text = document.getElementById('bankProgressText');
    if (text) text.innerHTML = '<strong>' + m + '</strong> mastered · <strong>' + r + '</strong> to review · <strong>' + (n - m - r) + '</strong> pending';
    var pct = document.getElementById('bankProgressPct');
    if (pct) pct.textContent = Math.round(100 * m / n) + '% mastered';
    var segM = document.getElementById('bankSegMastered'), segR = document.getElementById('bankSegReview');
    if (segM) segM.style.width = (100 * m / n) + '%';
    if (segR) segR.style.width = (100 * r / n) + '%';
    var bar = document.getElementById('bankProgressBar');
    if (bar) bar.setAttribute('aria-valuenow', String(m));
  }

  // ---- Filters -----------------------------------------------------------------------
  var state = { category: 'all', archetype: 'all', unit: 'all', difficulty: 'all', status: 'all', query: '' };
  var search = document.getElementById('bankSearch');
  var count = document.getElementById('bankCount');
  var empty = document.getElementById('bankEmpty');

  function fillSelect(id, entries) {
    var select = document.getElementById(id);
    if (!select) return null;
    entries.forEach(function (e) {
      var o = document.createElement('option');
      o.value = e[0];
      o.textContent = e[1];
      select.appendChild(o);
    });
    return select;
  }
  var selArch = fillSelect('bankArchetype', Object.keys(DATA.archetypes).map(function (k) { return [k, DATA.archetypes[k]]; })
    .concat([['theory-case', 'Short theory cases (any theme)']]));
  var selUnit = fillSelect('bankUnit', Object.keys(DATA.units).map(function (k) { return [k, DATA.units[k]]; }));
  var selDiff = document.getElementById('bankDifficulty');
  var selStatus = document.getElementById('bankStatus');

  function apply() {
    var words = fold(state.query).split(/\s+/).filter(Boolean);
    var shown = 0;
    cards.forEach(function (c) {
      var i = c.item;
      var ok = (state.category === 'all' || i.category === state.category) &&
        (state.archetype === 'all' || i.archetype === state.archetype) &&
        (state.unit === 'all' || String(i.unit) === state.unit) &&
        (state.difficulty === 'all' || String(i.difficulty) === state.difficulty) &&
        (state.status === 'all' || statusOf(i.id) === state.status) &&
        words.every(function (w) { return c.text.indexOf(w) >= 0; });
      c.node.hidden = !ok;
      if (ok) shown++;
    });
    if (count) count.textContent = 'Showing ' + shown + ' of ' + cards.length + ' items';
    if (empty) empty.hidden = shown !== 0;
  }

  [[selArch, 'archetype'], [selUnit, 'unit'], [selDiff, 'difficulty'], [selStatus, 'status']].forEach(function (p) {
    if (p[0]) p[0].addEventListener('change', function () { state[p[1]] = p[0].value; apply(); });
  });
  if (search) search.addEventListener('input', function () { state.query = search.value; apply(); });

  var tabs = Array.prototype.slice.call(document.querySelectorAll('#bankCategory [role="tab"]'));
  function selectTab(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
    });
    if (focus) tab.focus();
    state.category = tab.getAttribute('data-value');
    apply();
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener('click', function () { selectTab(tab, false); });
    tab.addEventListener('keydown', function (e) {
      var j = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : null;
      if (j === null) return;
      e.preventDefault();
      selectTab(tabs[(j + tabs.length) % tabs.length], true);
    });
  });

  var reset = document.getElementById('bankReset');
  if (reset) reset.addEventListener('click', function () {
    state = { category: 'all', archetype: 'all', unit: 'all', difficulty: 'all', status: 'all', query: '' };
    [selArch, selUnit, selDiff, selStatus].forEach(function (s) { if (s) s.value = 'all'; });
    if (search) search.value = '';
    if (tabs.length) selectTab(tabs[0], false); else apply();
  });

  // ---- Live announcements ------------------------------------------------------------
  var live = document.getElementById('bankLive');
  var toast = document.getElementById('bankToast');
  var toastTimer = null;
  function announce(message, visible) {
    if (live) { live.textContent = ''; window.setTimeout(function () { live.textContent = message; }, 30); }
    if (visible && toast) {
      toast.textContent = message;
      toast.hidden = false;
      window.clearTimeout(toastTimer);
      toastTimer = window.setTimeout(function () { toast.hidden = true; }, 1800);
    }
  }

  // ---- Shortcuts ---------------------------------------------------------------------
  var help = document.getElementById('bankHelp');
  function openHelp() {
    if (!help) return;
    if (typeof help.showModal === 'function') { if (!help.open) help.showModal(); } else help.setAttribute('open', '');
  }
  function closeHelp() {
    if (!help) return false;
    if (help.open || help.hasAttribute('open')) {
      if (typeof help.close === 'function') help.close(); else help.removeAttribute('open');
      return true;
    }
    return false;
  }
  var helpClose = document.getElementById('bankHelpClose');
  if (helpClose) helpClose.addEventListener('click', closeHelp);
  var helpOpen = document.getElementById('bankHelpOpen');
  if (helpOpen) helpOpen.addEventListener('click', openHelp);

  function nextPalette() {
    var api = window.AESurface;
    if (!api || typeof api.list !== 'function') return;
    var palettes = api.list();
    if (!palettes.length) return;
    var current = api.get();
    var idx = 0;
    for (var i = 0; i < palettes.length; i++) if (palettes[i].id === current) idx = i;
    var next = palettes[(idx + 1) % palettes.length];
    api.set(next.id);
    announce('Reading palette: ' + next.label, true);
  }

  document.addEventListener('keydown', function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    var typing = t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName));
    if (e.key === 'Escape') {
      if (closeHelp()) { e.preventDefault(); return; }
      if (t === search && search.value) { search.value = ''; state.query = ''; apply(); e.preventDefault(); }
      return;
    }
    if (typing || e.defaultPrevented) return;
    if (e.key === '/') { if (search) { e.preventDefault(); search.focus(); search.select(); } }
    else if (e.key === 't' || e.key === 'T') { e.preventDefault(); nextPalette(); }
    else if (e.key === '?') { e.preventDefault(); openHelp(); }
  });

  // ---- Build -------------------------------------------------------------------------
  var frag = document.createDocumentFragment();
  ITEMS.forEach(function (item) {
    var card = buildCard(item);
    cards.push(card);
    frag.appendChild(card.node);
  });
  list.appendChild(frag);
  updateProgress();
  apply();
  if (!renderMath(list)) window.addEventListener('load', function () { renderMath(list); });

  function openFromHash() {
    var id = decodeURIComponent((window.location.hash || '').slice(1));
    for (var i = 0; i < cards.length; i++) {
      if (cards[i].item.id === id) {
        cards[i].node.hidden = false;
        cards[i].details.open = true;
        cards[i].node.scrollIntoView({ block: 'start' });
        return;
      }
    }
  }
  window.addEventListener('hashchange', openFromHash);
  openFromHash();
})();
