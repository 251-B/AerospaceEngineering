/*!
 * Subject index pages as solar systems (teoria/, problemas/ and extra-problems/ index.html).
 *
 * Loaded by theme.js on every page; it acts only on those index pages. Each group of cards
 * (.topics-list, .topics-grid, .sets-list, .problem-sets-grid) becomes an orbit around a star:
 * the cards stay the same links, in the same DOM order, and are only placed along an ellipse
 * (clockwise from the upper left, so 01, 02, 03 read left to right across the top and back
 * along the bottom). Each card gets a numbered planet; its own title stays as it is.
 * Desktop only for now: from 900 px of container width the cards sit on the orbit; narrower
 * screens keep the usual card grid.
 * Skipped in the PDF print mode; screen-only, no storage. Styles: assets/css/subject-orbits.css.
 */
(function () {
  'use strict';
  if (/[?&]print=/.test(location.search)) return;
  if (!/\/subjects\/[^\/]+\/(teoria|problemas|extra-problems)\/(index\.html)?$/.test(location.pathname)) return;

  var SVGNS = 'http://www.w3.org/2000/svg';
  var GROUPS = '.topics-list, .topics-grid, .sets-list, .problem-sets-grid';
  var CARDS = '.topic-card, .set-card, .problem-card';
  var WIDE = 900;   // container width from which the orbit is used (desktop only for now)

  function css() {
    var self = document.querySelector('script[src*="subject-orbits.js"]');
    if (!self || document.querySelector('link[data-orbits]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.setAttribute('data-orbits', '');
    link.href = self.src.replace(/js\/subject-orbits\.js(\?.*)?$/, 'css/subject-orbits.css?v=20261119a');
    document.head.appendChild(link);
  }

  function pad(n) { return n < 10 ? '0' + n : String(n); }

  // The number the card already shows (.topic-num), else its position on the page: titles such as
  // "Topic 3 (II)" would give several planets the same number.
  function numberOf(card, fallback) {
    var num = card.querySelector('.topic-num');
    if (num && /\d/.test(num.textContent)) return pad(parseInt(num.textContent.replace(/\D+/g, ''), 10));
    return pad(fallback);
  }

  function prepare(group, start) {
    var cards = Array.prototype.filter.call(group.children, function (c) { return c.matches(CARDS); });
    if (!cards.length) return start;
    group.classList.add('orb-system');
    group.style.setProperty('--orb-n', cards.length);
    if (!group.querySelector(':scope > .orb-sky')) {
      var sky = document.createElementNS(SVGNS, 'svg');
      sky.setAttribute('class', 'orb-sky');
      sky.setAttribute('aria-hidden', 'true');
      sky.setAttribute('focusable', 'false');
      var ring = document.createElementNS(SVGNS, 'ellipse');
      ring.setAttribute('class', 'orb-ring');
      sky.appendChild(ring);
      group.insertBefore(sky, group.firstChild);
      var star = document.createElement('span');
      star.className = 'orb-star';
      star.setAttribute('aria-hidden', 'true');
      group.insertBefore(star, sky.nextSibling);
    }
    cards.forEach(function (card, i) {
      card.classList.add('orb-body');
      if (!card.querySelector(':scope > .orb-planet')) {
        var p = document.createElement('span');
        p.className = 'orb-planet';
        p.setAttribute('aria-hidden', 'true');
        p.textContent = numberOf(card, start + i + 1);
        card.insertBefore(p, card.firstChild);
      }
    });
    group._orbCards = cards;
    return start + cards.length;
  }

  // Ellipse sizes from the number of planets and the room available.
  function layout(group) {
    var cards = group._orbCards;
    if (!cards) return;
    var n = cards.length, W = group.clientWidth;
    // never wider than what the window shows of the group
    var left = group.getBoundingClientRect().left;
    W = Math.min(W, document.documentElement.clientWidth - Math.max(0, left) - 8);
    if (W < WIDE) {
      group.classList.remove('orb-wide');
      group.style.height = '';
      cards.forEach(function (c) { c.style.left = c.style.top = ''; });
      return;
    }
    group.classList.add('orb-wide');
    var label = W < 900 ? (n >= 9 ? 138 : 150) : W < 1100 ? 176 : 200;   // label column width (px)
    group.style.setProperty('--orb-label', label + 'px');
    var rx = Math.max(140, W / 2 - label / 2 - 12);
    if (n <= 2) rx = Math.min(rx, 300);
    // taller orbits on narrower containers, so neighbouring labels never touch
    var step = W < 1100 ? 34 : 22, cap = W < 1100 ? 360 : 250;
    var ry = n <= 2 ? 0 : n <= 4 ? 120 : Math.min(cap, 120 + (n - 4) * step);
    var top = 40, below = 96;                         // room above the top planet and for the label below
    var cy = top + ry, cx = W / 2;
    var H = Math.round(cy + ry + below);
    if (n <= 2) H = 190;
    group.style.height = H + 'px';
    if (n <= 2) cy = 46;
    var ring = group.querySelector('.orb-ring');
    ring.setAttribute('cx', cx); ring.setAttribute('cy', cy);
    ring.setAttribute('rx', rx); ring.setAttribute('ry', Math.max(ry, 1));
    group.classList.toggle('orb-line', n <= 2);
    var star = group.querySelector('.orb-star');
    star.style.left = cx + 'px'; star.style.top = cy + 'px';
    cards.forEach(function (c, i) {
      var a;
      if (n === 1) a = 0;
      else if (n === 2) a = i === 0 ? Math.PI : 0;
      else a = Math.PI * (200 / 180) + (2 * Math.PI * i) / n;   // clockwise from the upper left
      var x = cx + rx * Math.cos(a), y = cy + ry * Math.sin(a);
      if (n === 1) x = cx + Math.min(rx, 220);
      x = Math.max(label / 2 + 4, Math.min(W - label / 2 - 4, x));   // the label stays inside
      c.style.left = Math.round(x) + 'px';
      c.style.top = Math.round(y) + 'px';
    });
  }

  function init() {
    var groups = document.querySelectorAll(GROUPS);
    if (!groups.length) return;
    css();
    var start = 0;
    Array.prototype.forEach.call(groups, function (g) { start = prepare(g, start); });
    var run = function () { Array.prototype.forEach.call(groups, layout); };
    run();
    var t = 0;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(run, 60); });
    // a scrollbar that appears after the first layout changes the width: lay out again
    if (window.ResizeObserver) {
      var last = new WeakMap();
      var ro = new ResizeObserver(function (entries) {
        entries.forEach(function (e) {
          var w = Math.round(e.contentRect.width);
          if (last.get(e.target) !== w) { last.set(e.target, w); layout(e.target); }
        });
      });
      Array.prototype.forEach.call(groups, function (g) { if (g._orbCards) ro.observe(g); });
    }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(run);
    document.documentElement.classList.add('orb-ready');
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
