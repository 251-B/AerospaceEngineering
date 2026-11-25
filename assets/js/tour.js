/*!
 * Sideris portal: guided tour for new accounts
 *
 * Twelve short cards across the portal, each pointing at the real element when the page has it
 * (spotlight + card beside it) and centred otherwise. Next / Back / Skip tour, arrows, Esc to
 * skip, focus kept inside the card. A step on another page opens it with ?tour=<index>, and the
 * tour resumes there. Loaded by account.js for signed-in readers (menu item "Take the tour" or a
 * ?tour= link); offered at the end of sign-up. State under localStorage 'ae_tour' { done, step,
 * at } (synced with the account). Skipped in the PDF print mode, hidden in print.
 *
 * API: window.AETour = { STEPS, start(index), skip(), state(), configure({ navigate, base }) }
 */
(function () {
  'use strict';

  if (window.AETour) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var KEY = 'ae_tour';
  var self = document.currentScript;
  var cfg = {
    base: self && self.src ? self.src.replace(/assets\/js\/tour\.js(\?.*)?$/, '') : '../',
    navigate: function (url) { location.assign(url); }
  };

  var STEPS = [
    { id: 'study', title: 'My study', page: 'account/dashboard.html', target: '.acc-study-hero',
      text: 'Your study panel: time studied this week, your streak, where you left off and your next class.' },
    { id: 'calendar', title: 'Your calendar', page: 'account/calendar.html', target: '#calGrid',
      text: 'Every class of your group, with what will be done in it and the pages to prepare it. Choose your group in My groups; you can change any class.' },
    { id: 'catchup', title: 'Missed and not held', page: 'account/calendar.html', target: '#calCatchup',
      text: 'Open a class to mark it as missed: it waits here with its material, and Sideris can explain it. If a class is not held, the plan moves to your next one.' },
    { id: 'menu', title: 'Side menu', page: null, target: '#sidebarButton',
      text: 'Every subject, topic and problem page of the portal, and the sections of the page you are reading.' },
    { id: 'palette', title: 'Reading palettes', page: null, target: '#surfacePicker',
      text: 'Six paper colours, light and dark. Pick the one that is easiest on your eyes; your account remembers it.' },
    { id: 'theory', title: 'Theory pages', page: 'subjects/engineering-mechanics/teoria/topic-6.html', target: '.tr-rail',
      text: 'Each topic folds into sections. The rail on the right jumps between them and shows how much is left to read.' },
    { id: 'problems', title: 'Solved problems', page: 'subjects/engineering-mechanics/problemas/topic-8.html', target: '.pr-bar',
      text: 'Answer, Steps or Full: see only the result, one step at a time, or the whole solution. Star a problem or add your own note to it.' },
    { id: 'ask', title: 'Ask AI and Sideris', page: null, target: '#siderisButton',
      text: 'Select any text to ask about it, or open Sideris, the tutor that answers from the course notes and can give hints only.' },
    { id: 'focus', title: 'Study session', page: null, target: '#pomodoroButton',
      text: 'One panel for timing, method and study sound: it picks a study type for the subject, guides each block step by step, and fades sound to silence on breaks.' },
    { id: 'simulator', title: 'Exam simulator', page: 'subjects/aerospace-materials-1/simulator/index.html', target: 'main',
      text: 'Timed practice exams drawn from the bank, corrected at the end, with your results kept in My study.' },
    { id: 'news', title: 'What is new', page: null, target: '#updatesButton',
      text: 'The bell lists every new page and feature as it arrives.' },
    { id: 'settings', title: 'Settings and sync', page: 'account/settings.html', target: 'main',
      text: 'Your subjects, exam dates and preferences. Signed in, your calendar and progress follow you to every device. That is the tour.' }
  ];

  var ui = { card: null, spot: null, index: -1, prevFocus: null, target: null };

  function read() { try { return JSON.parse(localStorage.getItem(KEY) || 'null') || { done: false, step: 0, at: 0 }; } catch (e) { return { done: false, step: 0, at: 0 }; } }
  function write(s) { s.at = Date.now(); try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* blocked */ } if (window.AEAccount && window.AEAccount.changed) window.AEAccount.changed(); }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function onPage(page) { return !page || location.pathname.replace(/\\/g, '/').slice(-page.length - 1) === '/' + page; }

  function close() {
    if (ui.card) ui.card.remove();
    if (ui.spot) ui.spot.remove();
    ui.card = ui.spot = ui.target = null;
    ui.index = -1;
    document.removeEventListener('keydown', onKey, true);
    window.removeEventListener('resize', place);
    window.removeEventListener('scroll', place, true);
    if (ui.prevFocus && ui.prevFocus.focus) { try { ui.prevFocus.focus(); } catch (e) { /* gone */ } }
  }

  function finish() { var s = read(); s.done = true; s.step = STEPS.length - 1; write(s); close(); }
  function skip() { var s = read(); s.done = true; write(s); close(); }

  function go(i) {
    if (i < 0) return;
    if (i >= STEPS.length) { finish(); return; }
    var step = STEPS[i];
    var s = read(); s.step = i; write(s);
    if (!onPage(step.page)) { close(); cfg.navigate(cfg.base + step.page + '?tour=' + i); return; }
    render(i);
  }

  function place() {
    if (!ui.card) return;
    var t = ui.target;
    var r = t && t.getBoundingClientRect();
    if (!t || !r || (!r.width && !r.height)) {
      ui.card.classList.add('tour-card--center');
      ui.spot.hidden = true;
      ui.card.style.top = ui.card.style.left = '';
      return;
    }
    ui.card.classList.remove('tour-card--center');
    ui.spot.hidden = false;
    var pad = 6;
    ui.spot.style.top = (r.top - pad) + 'px';
    ui.spot.style.left = (r.left - pad) + 'px';
    ui.spot.style.width = (r.width + pad * 2) + 'px';
    ui.spot.style.height = (r.height + pad * 2) + 'px';
    var cw = ui.card.offsetWidth, ch = ui.card.offsetHeight, vw = window.innerWidth, vh = window.innerHeight;
    var top = r.bottom + 14;
    if (top + ch > vh - 12) top = r.top - ch - 14;
    if (top < 12) top = Math.max(12, Math.min(vh - ch - 12, r.top + 12));
    var left = Math.min(Math.max(12, r.left + r.width / 2 - cw / 2), vw - cw - 12);
    ui.card.style.top = top + 'px';
    ui.card.style.left = Math.max(12, left) + 'px';
  }

  function render(i) {
    var first = !ui.card;
    if (first) ui.prevFocus = document.activeElement;
    if (ui.card) ui.card.remove();
    if (ui.spot) ui.spot.remove();
    var step = STEPS[i];
    ui.index = i;
    var target = null;
    if (step.target) { try { target = document.querySelector(step.target); } catch (e) { target = null; } }
    if (target && target.getClientRects().length === 0) target = null;
    ui.target = target;

    ui.spot = el('div', 'tour-spot');
    ui.spot.setAttribute('aria-hidden', 'true');
    var card = el('div', 'tour-card');
    card.setAttribute('role', 'dialog');
    card.setAttribute('aria-modal', 'true');
    card.setAttribute('aria-labelledby', 'tourTitle');
    card.setAttribute('aria-describedby', 'tourText');
    card.appendChild(el('p', 'tour-count', (i + 1) + ' / ' + STEPS.length));
    var h = el('h2', 'tour-title', step.title); h.id = 'tourTitle';
    var p = el('p', 'tour-text', step.text); p.id = 'tourText';
    card.appendChild(h); card.appendChild(p);
    var dots = el('div', 'tour-dots'); dots.setAttribute('aria-hidden', 'true');
    STEPS.forEach(function (_, k) { dots.appendChild(el('span', k === i ? 'is-on' : k < i ? 'is-done' : '')); });
    card.appendChild(dots);
    var row = el('div', 'tour-actions');
    function b(name, text, cls) { var x = el('button', 'tour-btn' + (cls ? ' ' + cls : ''), text); x.type = 'button'; x.setAttribute('data-tour', name); row.appendChild(x); return x; }
    var skipB = b('skip', 'Skip tour', 'tour-btn--quiet');
    var backB = b('back', 'Back');
    if (i === 0) backB.disabled = true;
    var nextB = b('next', i === STEPS.length - 1 ? 'Finish' : 'Next', 'tour-btn--primary');
    skipB.addEventListener('click', skip);
    backB.addEventListener('click', function () { go(i - 1); });
    nextB.addEventListener('click', function () { go(i + 1); });
    card.appendChild(row);
    document.body.appendChild(ui.spot);
    document.body.appendChild(card);
    ui.card = card;
    if (target && target.scrollIntoView) {
      var r = target.getBoundingClientRect();
      if (r.top < 0 || r.bottom > window.innerHeight) target.scrollIntoView({ block: 'center' });
    }
    place();
    if (first) {
      document.addEventListener('keydown', onKey, true);
      window.addEventListener('resize', place);
      window.addEventListener('scroll', place, true);
    }
    nextB.focus({ preventScroll: true });
  }

  function onKey(e) {
    if (!ui.card) return;
    if (e.key === 'Escape') { e.preventDefault(); skip(); return; }
    if (e.key === 'Tab') {
      var f = Array.prototype.filter.call(ui.card.querySelectorAll('button'), function (x) { return !x.disabled; });
      if (!f.length) return;
      var at = f.indexOf(document.activeElement);
      e.preventDefault();
      var nextI = e.shiftKey ? (at <= 0 ? f.length - 1 : at - 1) : (at < 0 || at === f.length - 1 ? 0 : at + 1);
      f[nextI].focus();
      return;
    }
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    if (e.key === 'ArrowRight') { e.preventDefault(); go(ui.index + 1); }
    else if (e.key === 'ArrowLeft' && ui.index > 0) { e.preventDefault(); go(ui.index - 1); }
  }

  function start(i) { go(Math.max(0, Math.min(STEPS.length - 1, i || 0))); }

  window.AETour = {
    STEPS: STEPS,
    start: start,
    skip: skip,
    state: function () { return read(); },
    configure: function (o) { Object.keys(o || {}).forEach(function (k) { cfg[k] = o[k]; }); }
  };

  // Resume from ?tour=<index>, once the page widgets have been built.
  var q = new URLSearchParams(location.search).get('tour');
  if (q !== null && /^\d+$/.test(q)) {
    var launch = function () {
      var i = Math.min(STEPS.length - 1, +q), tries = 0;
      (function wait() {
        var step = STEPS[i];
        if (step.target && !document.querySelector(step.target) && tries++ < 20) { setTimeout(wait, 100); return; }
        start(i);
      })();
    };
    if (document.readyState === 'complete') setTimeout(launch, 300);
    else window.addEventListener('load', function () { setTimeout(launch, 300); });
  }
})();
