/*!
 * Sideris portal: favourites and personal notes on problem cards.
 *
 * Loaded by assets/js/account.js (with assets/css/problem-marks.css) on problem pages
 * (problemas/ and extra-problems/, not their index) when someone is signed in; never in the PDF
 * print mode. Each problem card (.problem-card / .problem-box with an id) gets a star and a note
 * button next to the folding arrow of assets/js/problem-collapse.js, and its note under the
 * heading, so notes stay readable on a folded card. Everything is placed inside the card's
 * heading (or after the <summary> of a <details> card), as problem-collapse does, so the scripts
 * that read a card's own children (Ask AI, the close bar) see nothing new.
 * Data: AEAccount.marks() / AEAccount.setMark(key, patch), stored under 'ae_marks'.
 */
(function () {
  'use strict';
  if (window.AEProblemMarks || /[?&]print=/.test(location.search)) return;
  if (!/\/(problemas|extra-problems)\/(?!index\.html)[^\/]+\.html$/.test(location.pathname)) return;

  var NS = 'http://www.w3.org/2000/svg';
  var STAR = 'M12 3.3l2.6 5.4 5.9.8-4.3 4.1 1 5.9L12 16.7l-5.2 2.8 1-5.9-4.3-4.1 5.9-.8z';
  var NOTE = 'M5 4h10l4 4v12H5zM15 4v4h4M8.5 12h7M8.5 15.5h5';

  function icon(d, size) {
    var svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('width', String(size || 17));
    svg.setAttribute('height', String(size || 17));
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    var path = document.createElementNS(NS, 'path');
    path.setAttribute('d', d);
    svg.appendChild(path);
    return svg;
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text) n.textContent = text;
    return n;
  }

  function pagePath() { return location.pathname.slice(location.pathname.indexOf('subjects/')); }

  function subjectOf() { var m = /subjects\/([^\/]+)\//.exec(location.pathname); return m ? m[1] : ''; }

  function cardTitle(card) {
    // by priority, not by document order (a <summary> wraps the whole heading)
    var t = null;
    ['.problem-title', 'h2', 'h3', 'h4', 'summary'].some(function (sel) { t = card.querySelector(sel); return !!t; });
    var num = card.querySelector('.problem-id, .problem-num, .problem-num-badge, .prob-num-badge, .problem-tag');
    var title = t ? t.textContent.replace(/\s+/g, ' ').trim() : card.id;
    var n = num ? num.textContent.replace(/\s+/g, ' ').trim() : '';
    if (n && n.length < 24 && title.indexOf(n) === -1) title = n + ' · ' + title;
    return title.slice(0, 140);
  }

  function ago(ms) {
    var min = Math.round((Date.now() - ms) / 60000);
    if (min < 1) return 'just now';
    if (min < 60) return min + ' min ago';
    var h = Math.round(min / 60);
    if (h < 24) return h + ' h ago';
    var d = Math.round(h / 24);
    return d === 1 ? 'yesterday' : d + ' days ago';
  }

  function openCard(card) {
    if (card.tagName === 'DETAILS') { card.open = true; return; }
    if (card.classList.contains('pc-collapsed')) {
      var t = card.querySelector('.pc-toggle');
      if (t) t.click(); else card.classList.remove('pc-collapsed');
    }
  }

  function setup(card) {
    if (card.hasAttribute('data-mk') || !card.id) return;
    card.setAttribute('data-mk', '');
    card.classList.add('mk-card');
    var key = pagePath() + '#' + card.id;
    var isDetails = card.tagName === 'DETAILS';
    var summary = isDetails ? card.querySelector(':scope > summary') : null;
    var heads = isDetails ? [] : [].filter.call(card.children, function (c) { return c.classList.contains('pc-head'); });
    var head = isDetails ? summary : (heads[heads.length - 1] || card.firstElementChild);
    if (!head) return;
    // the top row of the heading makes room for the buttons, which sit in the card's top corner
    if (!isDetails && (heads[0] || head)) (heads[0] || head).classList.add('mk-head');

    function mark() { return AEAccount.marks().items[key] || {}; }
    function save(patch) {
      patch.title = cardTitle(card);
      patch.subject = subjectOf();
      patch.path = pagePath();
      patch.card = card.id;
      AEAccount.setMark(key, patch);
      sync();
    }

    // star + note buttons, next to the folding arrow
    var group = el('div', 'mk-actions');
    var star = el('button', 'mk-btn mk-btn--star');
    star.type = 'button';
    star.appendChild(icon(STAR));
    var noteBtn = el('button', 'mk-btn mk-btn--note');
    noteBtn.type = 'button';
    noteBtn.appendChild(icon(NOTE));
    group.appendChild(star);
    group.appendChild(noteBtn);

    // the note: a short view (stays visible on a folded card) and an editor
    var box = el('div', 'mk-note');
    box.hidden = true;
    var view = el('div', 'mk-note__view');
    var viewIcon = icon(NOTE, 15);
    var viewText = el('p', 'mk-note__text');
    var viewMeta = el('span', 'mk-note__meta');
    view.appendChild(viewIcon);
    var viewBody = el('div', 'mk-note__body');
    viewBody.appendChild(viewText);
    viewBody.appendChild(viewMeta);
    view.appendChild(viewBody);
    view.setAttribute('role', 'button');
    view.tabIndex = 0;
    view.setAttribute('aria-label', 'Edit your note');
    var editor = el('div', 'mk-note__editor');
    editor.hidden = true;
    var label = el('label', 'mk-note__label', 'Your note');
    var area = el('textarea', 'mk-note__input');
    var areaId = 'mk-' + card.id;
    area.id = areaId;
    label.setAttribute('for', areaId);
    area.rows = 3;
    area.placeholder = 'What to remember: the trick, the mistake you made, what to ask in class...';
    var foot = el('div', 'mk-note__foot');
    var status = el('span', 'mk-note__status');
    status.setAttribute('aria-live', 'polite');
    var del = el('button', 'mk-note__link', 'Delete note');
    del.type = 'button';
    var done = el('button', 'mk-note__done', 'Done');
    done.type = 'button';
    foot.appendChild(status);
    foot.appendChild(del);
    foot.appendChild(done);
    editor.appendChild(label);
    editor.appendChild(area);
    editor.appendChild(foot);
    box.appendChild(view);
    box.appendChild(editor);

    // The note goes inside the heading when the heading is a box (.problem-header, <summary>);
    // after a bare title it becomes a heading of its own (.pc-head), so a folded card shows it.
    if (isDetails) {
      summary.appendChild(group);
      summary.appendChild(box);
    } else if (head.tagName === 'DIV' && head.classList.contains('problem-header')) {
      head.appendChild(group);
      head.appendChild(box);
    } else {
      head.appendChild(group);
      box.classList.add('pc-head', 'mk-note--sibling');
      head.insertAdjacentElement('afterend', box);
    }

    function grow() { area.style.height = 'auto'; area.style.height = Math.min(area.scrollHeight + 2, 320) + 'px'; }

    function sync() {
      var m = mark();
      star.setAttribute('aria-pressed', String(!!m.fav));
      star.setAttribute('aria-label', m.fav ? 'Remove from favourites' : 'Add to favourites');
      star.title = m.fav ? 'In your favourites' : 'Add to favourites';
      noteBtn.classList.toggle('has-note', !!m.note);
      noteBtn.setAttribute('aria-label', m.note ? 'Edit your note' : 'Add a note');
      noteBtn.title = m.note ? 'Edit your note' : 'Add a note';
      card.classList.toggle('mk-fav', !!m.fav);
      var editing = !editor.hidden;
      box.hidden = !m.note && !editing;
      view.hidden = editing || !m.note;
      viewText.textContent = m.note || '';
      viewMeta.textContent = m.updated ? 'Your note · ' + ago(m.updated) : 'Your note';
    }

    function edit() {
      if (isDetails) card.open = true;
      editor.hidden = false;
      area.value = mark().note || '';
      status.textContent = '';
      sync();
      grow();
      area.focus();
    }

    function finish() {
      editor.hidden = true;
      sync();
      noteBtn.focus();
    }

    var timer = 0;
    area.addEventListener('input', function () {
      grow();
      status.textContent = 'Saving...';
      clearTimeout(timer);
      timer = setTimeout(function () {
        save({ note: area.value.trim() });
        status.textContent = 'Saved';
      }, 450);
    });
    area.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { e.preventDefault(); clearTimeout(timer); save({ note: area.value.trim() }); finish(); }
    });

    // Clicks here must not fold the card or toggle a <details>.
    function guard(e) { e.stopPropagation(); if (isDetails && e.target.closest('summary')) e.preventDefault(); }
    group.addEventListener('click', guard);
    box.addEventListener('click', function (e) { e.stopPropagation(); if (isDetails) e.preventDefault(); /* inside a <summary>: never toggle the card */ });
    box.addEventListener('keydown', function (e) { if (isDetails) e.stopPropagation(); });

    star.addEventListener('click', function () {
      var fav = !mark().fav;
      save({ fav: fav });
      star.classList.remove('is-pop');
      void star.offsetWidth;
      if (fav) star.classList.add('is-pop');
      announce(fav ? 'Added to favourites' : 'Removed from favourites');
    });
    noteBtn.addEventListener('click', function () {
      if (!editor.hidden) { clearTimeout(timer); save({ note: area.value.trim() }); finish(); return; }
      edit();
    });
    view.addEventListener('click', edit);
    view.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); edit(); } });
    done.addEventListener('click', function () { clearTimeout(timer); save({ note: area.value.trim() }); finish(); });
    del.addEventListener('click', function () { clearTimeout(timer); area.value = ''; save({ note: '' }); finish(); announce('Note deleted'); });

    sync();
  }

  var live;
  function announce(text) {
    if (!live) {
      live = el('div', 'mk-live');
      live.setAttribute('role', 'status');
      live.setAttribute('aria-live', 'polite');
      document.body.appendChild(live);
    }
    live.textContent = text;
  }

  function init(tries) {
    tries = tries || 0;
    if (!window.AEAccount || !AEAccount.current()) return;
    var cards = [].filter.call(document.querySelectorAll('.problem-card, .problem-box'), function (c) {
      return !c.closest('#examSimulator') && !c.parentElement.closest('.problem-card, .problem-box');
    });
    // Wait for problem-collapse to mark the headings, so the buttons land beside its arrow.
    if (cards.length && !cards[0].hasAttribute('data-pc') && tries < 40) { setTimeout(function () { init(tries + 1); }, 50); return; }
    cards.forEach(setup);
  }

  window.AEProblemMarks = { init: init };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(0); });
  else init(0);
})();
