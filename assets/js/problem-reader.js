/*!
 * Aerospace Engineering Study Portal: problem reader (steps, answer view, problem rail, quieter text).
 *
 * Loaded on every page by assets/js/theme.js (no page carries its own <script> tag for it), after
 * problem-collapse.js and theory-reader.js, whose helpers it borrows (window.AEReaderKit) together with
 * the styles of assets/css/theory-reader.css; its own styles are assets/css/problem-reader.css, linked by
 * this script. It acts on worked-problem pages (problemas/ and extra-problems/, not their index) listed
 * in PAGES, and is skipped in the PDF print mode (?print=...). Everything it hides or moves is
 * screen-only: the browser's own print and the PDFs show every problem in full.
 *
 *  - Reading modes, one switch for the page ("Answer", "Steps", "Full"), stored under ae_problem_mode
 *    (try/catch: the page works without storage; ?mode=answer|steps|full overrides it):
 *      Steps  - a worked solution shows one step (.phase-block) at a time, with a row of numbered
 *               step chips above it and "Previous" / "Next" buttons below it;
 *      Answer - an open problem shows its statement and its last step (answers and checks) only,
 *               with the worked solution already unfolded and a button to go through the steps;
 *      Full   - the whole solution, as written.
 *  - Problem rail: a bar per problem at the right edge of the window (title on hover), the problem in
 *    view marked and the ones above it shown as read, and a pill "3 / 9 · ~25 min" above it. The left
 *    and right arrow keys open the previous or next problem and fold the others.
 *  - Quieter text, as on the theory pages: citations inside headings hidden, figure captions folded
 *    after their first sentence ("More"), derivation boxes reduced to their result ("Show derivation"),
 *    a wider column and, on wide screens, a figure beside the paragraph that explains it.
 * API: window.AEProblemReader = { init, mode, setMode }
 */
(function () {
  'use strict';

  if (window.AEProblemReader) return;
  var stub = { init: function () {}, mode: function () { return 'full'; }, setMode: function () {} };
  if (/[?&]print=/.test(location.search)) return;
  // Pilot pages first; the list grows to every problem page once the layout is approved.
  var PAGES = /\/subjects\/(fluid-mechanics\/problemas\/topic-5-hydrostatics|engineering-mechanics\/problemas\/topic-6)\.html$/;
  if (!/\/(problemas|extra-problems)\/(?!index\.html)[^\/]+\.html$/.test(location.pathname) || !PAGES.test(location.pathname)) {
    window.AEProblemReader = stub;
    return;
  }

  var MODE_KEY = 'ae_problem_mode';
  var MODES = [['answer', 'Answer'], ['steps', 'Steps'], ['full', 'Full']];
  var ANSWER_RE = /answer|result|check|conclusion|interpretation|summary/i;
  var kit, collapse, problems = [], mode = 'steps', modeButtons = [], info = null, progress = null;

  function linkStyles() {
    var self = document.querySelector('script[src*="problem-reader.js"]');
    if (!self || document.querySelector('link[href*="problem-reader.css"]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = self.src.replace(/js\/problem-reader\.js(\?.*)?$/, 'css/problem-reader.css');
    document.head.appendChild(link);
  }

  function button(cls, text) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = cls;
    if (text) b.textContent = text;
    return b;
  }

  function textOf(el) { return el ? kit.headingText(el) : ''; }

  /* ----------------------------------------------------------------- cards */
  function isOpen(p) { return collapse ? collapse.isOpen(p.card) : true; }
  function setOpen(p, open) { if (collapse && collapse.isOpen(p.card) !== open) collapse.setOpen(p.card, open); }

  function titleOf(card) {
    var title = card.querySelector('.problem-title, .problem-summary h2, h2, h3');
    var num = card.querySelector('.problem-num, .problem-id, .problem-number, .problem-tag');
    var n = num ? num.textContent.replace(/\s+/g, ' ').trim() : '';
    var t = textOf(title);
    return { num: n, text: n && t && t.indexOf(n) < 0 ? n + ' · ' + t : (t || n || 'Problem') };
  }

  /* The steps of a worked solution: its .phase-block elements (not nested ones), each with its title. */
  function stepsOf(card) {
    return [].filter.call(card.querySelectorAll('.phase-block'), function (b) {
      return !b.parentElement.closest('.phase-block');
    }).map(function (block, i) {
      var head = block.querySelector('.phase-heading, h3, h4');
      return { el: block, title: textOf(head) || 'Step ' + (i + 1) };
    });
  }

  function answerIndex(steps) {
    for (var i = steps.length - 1; i >= 0; i--) if (ANSWER_RE.test(steps[i].title)) return i;
    return steps.length - 1;
  }

  /* ----------------------------------------------------------------- steps */
  function buildStepper(p) {
    var steps = p.steps;
    var first = steps[0].el, last = steps[steps.length - 1].el;

    var top = document.createElement('div');
    top.className = 'pr-stepper';
    var label = document.createElement('p');
    label.className = 'pr-stepper__label';
    top.appendChild(label);
    var list = document.createElement('ol');
    list.className = 'pr-chips';
    list.setAttribute('aria-label', 'Steps of the solution');
    steps.forEach(function (step, i) {
      var li = document.createElement('li');
      var b = button('pr-chip');
      var n = document.createElement('span');
      n.className = 'pr-chip__n';
      n.textContent = String(i + 1);
      var t = document.createElement('span');
      t.className = 'pr-chip__t';
      t.textContent = step.title;
      b.appendChild(n);
      b.appendChild(t);
      b.title = step.title;
      b.addEventListener('click', function () { go(p, i, true); });
      li.appendChild(b);
      list.appendChild(li);
      step.chip = b;
    });
    top.appendChild(list);
    first.parentNode.insertBefore(top, first);

    var nav = document.createElement('div');
    nav.className = 'pr-stepnav';
    var prev = button('pr-stepnav__btn pr-stepnav__prev', 'Previous');
    var count = document.createElement('span');
    count.className = 'pr-stepnav__count';
    var next = button('pr-stepnav__btn pr-stepnav__next');
    prev.addEventListener('click', function () { go(p, p.step - 1, true); });
    next.addEventListener('click', function () {
      if (p.step < steps.length - 1) go(p, p.step + 1, true);
      else nextProblem(p);
    });
    nav.appendChild(prev);
    nav.appendChild(count);
    nav.appendChild(next);
    // After the container of the steps, so .phase-block:last-child still matches the last step.
    var host = last.parentElement;
    if (host && host !== p.card && host.matches('.solution-content, .card-body')) host.parentNode.insertBefore(nav, host.nextSibling);
    else last.parentNode.insertBefore(nav, last.nextSibling);

    // Answer view: a short line above the answer with the way into the steps.
    var ans = document.createElement('div');
    ans.className = 'pr-answer-note';
    var note = document.createElement('span');
    note.textContent = 'Showing the answer only.';
    var walk = button('pr-stepnav__btn', 'Go through the steps');
    walk.addEventListener('click', function () { p.override = 'steps'; apply(p); go(p, 0, true); });
    ans.appendChild(note);
    ans.appendChild(walk);
    first.parentNode.insertBefore(ans, first);

    p.ui = { top: top, label: label, nav: nav, prev: prev, next: next, count: count, answer: ans };
  }

  function modeOf(p) { return p.override || mode; }

  function go(p, i, scroll) {
    if (!p.steps.length) return;
    p.step = Math.max(0, Math.min(p.steps.length - 1, i));
    apply(p);
    if (scroll && p.ui) {
      var rect = p.ui.top.getBoundingClientRect();
      if (rect.top < kit.headerHeight() || rect.top > window.innerHeight * 0.6) kit.place(p.ui.top);
    }
    kit.balanceAll();
    update();
  }

  /* Shows the steps the current mode asks for. Nothing is moved: hidden steps get pr-hidden. */
  function apply(p) {
    if (!p.steps.length) return;
    var m = modeOf(p);
    p.card.setAttribute('data-pr-mode', m);
    p.steps.forEach(function (step, i) {
      var shown = m === 'full' || (m === 'steps' && i === p.step) || (m === 'answer' && i === p.answer);
      step.el.classList.toggle('pr-hidden', !shown);
      step.el.classList.toggle('pr-current', m === 'steps' && i === p.step);
      if (step.chip) {
        step.chip.classList.toggle('pr-chip--done', i < p.step);
        if (i === p.step) step.chip.setAttribute('aria-current', 'step');
        else step.chip.removeAttribute('aria-current');
      }
    });
    if (!p.ui) return;
    var n = p.steps.length, s = p.step;
    p.ui.label.textContent = 'Step ' + (s + 1) + ' of ' + n;
    p.ui.count.textContent = (s + 1) + ' / ' + n;
    p.ui.prev.disabled = s === 0;
    var nextP = problems[problems.indexOf(p) + 1];
    p.ui.next.textContent = s < n - 1 ? 'Next: ' + p.steps[s + 1].title : (nextP ? 'Next problem' : 'Last step');
    p.ui.next.disabled = s === n - 1 && !nextP;
    // Answer view: the worked solution must be unfolded to show its last step.
    if (m === 'answer' && p.details && !p.details.open && isOpen(p)) p.details.open = true;
  }

  /* ------------------------------------------------------------------ modes */
  function initialMode() {
    var q = /[?&]mode=(answer|steps|full)\b/.exec(location.search);
    if (q) return q[1];
    try {
      var saved = localStorage.getItem(MODE_KEY);
      return saved === 'answer' || saved === 'full' ? saved : 'steps';
    } catch (e) { return 'steps'; }
  }

  function setMode(m, remember) {
    mode = m === 'answer' || m === 'full' ? m : 'steps';
    document.documentElement.setAttribute('data-pr-page-mode', mode);
    modeButtons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-mode') === mode)); });
    if (remember) { try { localStorage.setItem(MODE_KEY, mode); } catch (e) {} }
    problems.forEach(function (p) { p.override = null; apply(p); });
    kit.balanceAll();
    update();
  }

  function modeSwitch() {
    var group = document.createElement('div');
    group.className = 'tr-mode pr-mode';
    group.setAttribute('role', 'group');
    group.setAttribute('aria-label', 'How much of each solution to show');
    MODES.forEach(function (pair) {
      var b = button('tr-mode__btn', pair[1]);
      b.setAttribute('data-mode', pair[0]);
      b.addEventListener('click', function () { setMode(pair[0], true); });
      modeButtons.push(b);
      group.appendChild(b);
    });
    return group;
  }

  function buildBar() {
    var bar = document.querySelector('.pc-bar');
    var wrap = document.createElement('div');
    wrap.className = 'pr-bar';
    info = document.createElement('span');
    info.className = 'pr-bar__info';
    var total = problems.reduce(function (n, p) { return n + p.words; }, 0);
    info.textContent = problems.length + ' problems · about ' + kit.minutes(total) + ' min of reading';
    wrap.appendChild(info);
    if (problems.some(function (p) { return p.steps.length; })) wrap.appendChild(modeSwitch());
    var hint = document.createElement('span');
    hint.className = 'pr-bar__hint';
    hint.textContent = 'Keys ← → move between problems';
    if (bar) {
      bar.classList.add('pr-host');
      var count = bar.querySelector('.pc-bar__count');
      if (count) count.remove();   // the line above gives the count
      bar.insertBefore(wrap, bar.firstChild);
      bar.appendChild(hint);
    } else if (problems[0]) {
      wrap.appendChild(hint);
      problems[0].card.parentNode.insertBefore(wrap, problems[0].card);
    }
  }

  /* ------------------------------------------------------------------ rail */
  var active = -1;

  function jump(p) {
    setOpen(p, true);
    kit.place(p.card);
    if (p.card.id && history.replaceState) history.replaceState(null, '', '#' + p.card.id);
    update();
  }

  function nextProblem(p) {
    var i = problems.indexOf(p);
    if (i < problems.length - 1) focusProblem(i + 1);
  }

  function focusProblem(i) {
    var target = problems[i];
    problems.forEach(function (p) { if (p !== target) setOpen(p, false); });
    setOpen(target, true);
    if (target.steps.length && modeOf(target) === 'steps') { target.step = 0; apply(target); }
    jump(target);
  }

  function update() {
    var line = kit.headerHeight() + window.innerHeight * 0.3;
    var i = -1;
    for (var k = 0; k < problems.length; k++) {
      if (problems[k].card.getBoundingClientRect().top <= line) i = k; else break;
    }
    if (i !== active) {
      active = i;
      problems.forEach(function (p, k) {
        if (!p.bar) return;
        p.bar.classList.toggle('tr-bar--read', k < i);
        if (k === i) p.bar.setAttribute('aria-current', 'location'); else p.bar.removeAttribute('aria-current');
      });
    }
    if (progress) {
      var left = problems.slice(Math.max(0, i)).reduce(function (n, p) { return n + p.words; }, 0);
      progress.textContent = (i < 0 ? problems.length + ' problems' : (i + 1) + ' / ' + problems.length) +
        ' · ~' + kit.minutes(left) + ' min';
      progress.title = i < 0 ? problems.length + ' problems' : 'Problem ' + (i + 1) + ' of ' + problems.length;
    }
  }

  function buildRail() {
    var nav = document.createElement('nav');
    nav.className = 'tr-rail pr-rail';
    nav.setAttribute('aria-label', 'Problems of this page');
    progress = document.createElement('p');
    progress.className = 'tr-progress';
    nav.appendChild(progress);
    var list = document.createElement('ol');
    list.className = 'tr-rail__list';
    list.style.setProperty('--tr-n', String(problems.length));
    problems.forEach(function (p) {
      var li = document.createElement('li');
      var b = button('tr-bar tr-bar--h2');
      b.setAttribute('aria-label', p.title.text);
      var line = document.createElement('span');
      line.className = 'tr-bar__line';
      line.setAttribute('aria-hidden', 'true');
      var tip = document.createElement('span');
      tip.className = 'tr-bar__tip';
      tip.setAttribute('aria-hidden', 'true');
      tip.textContent = p.title.text;
      b.appendChild(line);
      b.appendChild(tip);
      b.addEventListener('click', function () { jump(p); });
      li.appendChild(b);
      list.appendChild(li);
      p.bar = b;
    });
    nav.appendChild(list);
    document.body.appendChild(nav);
    document.documentElement.classList.add('tr-has-rail');
    var queued = false;
    window.addEventListener('scroll', function () {
      if (queued) return;
      queued = true;
      requestAnimationFrame(function () { queued = false; update(); });
    }, { passive: true });
    window.addEventListener('resize', update);
  }

  /* Left and right arrows: previous or next problem (it opens and the others fold). Ignored while
     typing, with a modifier held, inside a simulator (its own keys) and while a dialog is open. */
  function onKey(event) {
    if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
    if (event.ctrlKey || event.altKey || event.metaKey || event.shiftKey) return;
    var t = event.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    if (t && t.closest && t.closest('svg, .m3-sim, .hs-sim, [role="slider"], [role="dialog"]')) return;
    if (document.querySelector('[role="dialog"][aria-modal="true"]:not([hidden])')) return;
    var next = Math.max(0, Math.min(problems.length - 1, active + (event.key === 'ArrowRight' ? 1 : -1)));
    if (next === active && active >= 0) return;
    event.preventDefault();
    focusProblem(next);
  }

  /* ------------------------------------------------------------------ init */
  function init() {
    if (document.documentElement.classList.contains('pr-on')) return;
    kit = window.AEReaderKit;
    collapse = window.AEProblemCollapse;
    if (!kit) return;
    kit.linkStyles();
    linkStyles();
    var scope = document.querySelector('main') || document.body;
    var cards = collapse && collapse.cards().length ? collapse.cards()
      : [].slice.call(scope.querySelectorAll('.problem-card, .problem-box'));
    if (!cards.length) return;
    document.documentElement.classList.add('tr-on', 'tr-wide', 'pr-on');

    kit.wrapCitations(scope);
    [].forEach.call(scope.querySelectorAll('.diagram-caption, figcaption'), kit.foldCaption);
    [].forEach.call(scope.querySelectorAll('.derivation-box'), kit.foldDerivation);

    cards.forEach(function (card) {
      var p = { card: card, title: titleOf(card), steps: stepsOf(card), step: 0, override: null,
        details: card.querySelector('details.solution-details'), words: kit.countWords(card) };
      p.answer = p.steps.length ? answerIndex(p.steps) : -1;
      if (p.steps.length >= 2) buildStepper(p); else p.steps = [];
      card.addEventListener('toggle', function () { if (isOpen(p)) { apply(p); kit.balanceAll(); } update(); });
      if (p.details) p.details.addEventListener('toggle', function () { kit.balanceAll(); update(); });
      problems.push(p);
    });

    kit.buildPairs(scope);
    buildBar();
    if (problems.length >= 2) buildRail();
    setMode(initialMode());
    document.addEventListener('keydown', onKey);
    window.addEventListener('load', kit.balanceAll);
    window.addEventListener('resize', kit.balanceAll);
    setTimeout(kit.balanceAll, 800);   // after the formulas are typeset
    update();
  }

  window.AEProblemReader = { init: init, mode: function () { return mode; }, setMode: function (m) { setMode(m, false); } };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
