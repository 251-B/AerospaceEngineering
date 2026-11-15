/*!
 * Aerospace Engineering Study Portal: collapsible problem cards.
 *
 * Loaded on every page by assets/js/theme.js (no page carries its own <script> tag for it); its styles
 * are section 15 of assets/css/study-surface.css. Skipped in the PDF print mode (?print=...); the
 * folding is screen-only CSS, so the browser's own print shows every problem in full.
 *
 * On a problem page (problemas/ and extra-problems/, not their index) every problem card starts
 * folded to its heading (number, badges and title), so a page with twenty problems is a short list
 * and the one wanted is a click away. The card is not restructured: the script marks the heading
 * children (.problem-header, .problem-tag, .problem-title) and adds one toggle button; everything
 * else is hidden by the .pc-collapsed class. Cards that already are a <details class="problem-card">
 * (Aerospace Materials I) are simply closed. A bar above the first card expands or folds them all.
 * A link to a card, or to anything inside one (#prob-07, a side-menu section), opens that card.
 * No storage. API: window.AEProblemCollapse = { init, expandAll, collapseAll }
 */
(function () {
  'use strict';

  if (window.AEProblemCollapse) return;
  if (/[?&]print=/.test(location.search)) return;
  if (!/\/(problemas|extra-problems)\/(?!index\.html)[^\/]+\.html$/.test(location.pathname)) {
    window.AEProblemCollapse = { init: function () {}, expandAll: function () {}, collapseAll: function () {} };
    return;
  }

  var SVG_NS = 'http://www.w3.org/2000/svg';
  var HEAD = '.problem-header, .problem-tag, .problem-title';
  var cards = [];

  function chevron() {
    var svg = document.createElementNS(SVG_NS, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('width', '18');
    svg.setAttribute('height', '18');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    var path = document.createElementNS(SVG_NS, 'path');
    path.setAttribute('d', 'M6 9l6 6 6-6');
    svg.appendChild(path);
    return svg;
  }

  function isDetails(card) { return card.tagName === 'DETAILS'; }

  function isOpen(card) {
    return isDetails(card) ? card.open : !card.classList.contains('pc-collapsed');
  }

  function setOpen(card, open) {
    if (isDetails(card)) { card.open = open; return; }
    card.classList.toggle('pc-collapsed', !open);
    var button = card.querySelector('.pc-toggle');
    if (button) {
      button.setAttribute('aria-expanded', String(open));
      button.setAttribute('aria-label', (open ? 'Fold' : 'Open') + ' this problem');
    }
  }

  function prepare(card) {
    if (card.hasAttribute('data-pc')) return;
    card.setAttribute('data-pc', '');
    cards.push(card);
    if (isDetails(card)) { card.open = false; return; }

    var heads = [].filter.call(card.children, function (child) { return child.matches(HEAD); });
    if (!heads.length && card.firstElementChild) heads = [card.firstElementChild];
    heads.forEach(function (head) {
      head.classList.add('pc-head');
      head.addEventListener('click', function (event) {
        if (event.target.closest('a, button, input, select, textarea, summary, label')) return;
        if (String(window.getSelection && window.getSelection()) !== '') return;   // selecting the title
        setOpen(card, !isOpen(card));
      });
    });

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'pc-toggle';
    button.appendChild(chevron());
    button.addEventListener('click', function () { setOpen(card, !isOpen(card)); });
    // Inside the heading, so the scripts that read the card's own children see nothing new.
    (heads[heads.length - 1] || card).appendChild(button);
    card.classList.add('pc-card');
    setOpen(card, false);
  }

  function all(open) { cards.forEach(function (card) { setOpen(card, open); }); }

  function bar(first) {
    if (document.querySelector('.pc-bar') || cards.length < 2) return;
    var wrap = document.createElement('div');
    wrap.className = 'pc-bar';
    var count = document.createElement('span');
    count.className = 'pc-bar__count';
    count.textContent = cards.length + ' problems';
    wrap.appendChild(count);
    [['Open all', true], ['Fold all', false]].forEach(function (pair) {
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'pc-bar__btn';
      button.textContent = pair[0];
      button.addEventListener('click', function () { all(pair[1]); });
      wrap.appendChild(button);
    });
    first.parentNode.insertBefore(wrap, first);
  }

  /* Open the card that holds the target of a #link, then bring the target into view. */
  function reveal(hash, scroll) {
    if (!hash || hash.length < 2) return;
    var target;
    try { target = document.getElementById(decodeURIComponent(hash.slice(1))); } catch (e) { return; }
    var card = target && target.closest('[data-pc]');
    if (!card) return;
    if (!isOpen(card)) setOpen(card, true);
    if (scroll) target.scrollIntoView({ block: 'start' });
  }

  function init() {
    var found = document.querySelectorAll('.problem-card, .problem-box');
    [].forEach.call(found, function (card) {
      if (card.closest('#examSimulator') || card.parentElement.closest('.problem-card, .problem-box')) return;
      prepare(card);
    });
    if (!cards.length) return;
    bar(cards[0]);
    reveal(location.hash, true);
  }

  window.addEventListener('hashchange', function () { reveal(location.hash, true); });
  // The same #link clicked twice fires no hashchange: open its card anyway.
  document.addEventListener('click', function (event) {
    var link = event.target.closest && event.target.closest('a[href*="#"]');
    if (!link || link.pathname !== location.pathname) return;
    reveal(link.hash, false);
  });

  window.AEProblemCollapse = { init: init, expandAll: function () { all(true); }, collapseAll: function () { all(false); } };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
