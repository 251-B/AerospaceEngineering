/*!
 * Aerospace Engineering Study Portal: theme manager
 *
 * Load synchronously in <head> (before any stylesheet-dependent paint) so the stored theme
 * is on <html data-theme> before <body> is parsed:
 *     <script src="assets/js/theme.js"></script>
 *
 * Single theme key: 'ae_theme' ('dark' | 'light'). Values left by earlier pages under
 * 'aero-portal-theme' or 'theme' are migrated once, then ignored. Default theme: dark.
 *
 * API: window.AETheme = { get(), set(theme), toggle(), KEY }
 * Wiring: #themeToggle (click) and #themeLabel (text 'Dark' | 'Light') are picked up when present.
 * Event:  document 'ae-theme-change' with detail { theme }.
 *
 * Reading surface (second, independent concern, same file so no page needs another <script>):
 * <html data-surface> selects an ergonomic background palette. Stored under 'ae_surface'
 * ('default' | 'cream' | 'sepia' | 'slate-paper' | 'sage' | 'charcoal'); the palettes themselves
 * are CSS in assets/css/study-surface.css. Every palette has one polarity, so choosing it also
 * sets the theme (light palettes -> 'light', charcoal -> 'dark'), and a theme toggle that would
 * break the pairing resets the surface to 'default'.
 * On pages that load study-surface.css a picker is built in front of #themeToggle.
 *
 * API: window.AESurface = { get(), set(id), list(), KEY }
 * Event: document 'ae-surface-change' with detail { surface }.
 *
 * Site name (fourth concern): SITE_NAME below is the only place where the name of the portal is
 * written. This script sets the browser-tab title from it ("<name>" on the landing page,
 * "<name> <short subject>" on subject pages) and fills every [data-site-name] element.
 * API: window.AESite = { name, subjects, title() }
 *
 * Focus Lab, the study timer and the "What's new" panel (third concern, loaded from here for the
 * same reason): appends <script src="assets/js/focus-lab.js">, <script src="assets/js/pomodoro.js">,
 * <script src="assets/data/updates.js"> (reached as ../data/updates.js from this file),
 * <script src="assets/js/updates.js">, <script src="assets/data/nav.js"> and
 * <script src="assets/js/sidebar.js">, <script src="assets/js/problem-collapse.js">,
 * <script src="assets/js/theory-reader.js"> and <script src="assets/js/solution-close.js"> next to this
 * file, so the study-sound widget, the Pomodoro timer, the updates bell, the side menu, the section rail
 * of theory pages and the "Close" bar
 * at the end of worked solutions are on every page that loads theme.js. Skipped in the PDF print
 * mode (?print=...).
 */
(function () {
  'use strict';

  // ---- Site name: the one place to change it ------------------------------------------------
  // The browser tab reads SITE_NAME on the landing page and SITE_NAME + ' ' + short subject name
  // on every page under subjects/<slug>/. Elements marked data-site-name get the name as text.
  var SITE_NAME = 'Sideris';
  var SUBJECT_SHORT = {
    'fluid-mechanics': 'Fluids',
    'aerospace-materials-1': 'Materials',
    'engineering-mechanics': 'Mechanics',
    'advanced-maths': 'Maths',
    'business-management': 'Management'
  };
  var PRINT_MODE = /[?&]print=/.test(location.search);

  function siteTitle() {
    var match = /\/subjects\/([^\/]+)\//.exec(location.pathname);
    if (match) return SUBJECT_SHORT[match[1]] ? SITE_NAME + ' ' + SUBJECT_SHORT[match[1]] : null;
    // the landing page marks itself with <html data-celestial-subject="portal">
    return document.documentElement.getAttribute('data-celestial-subject') === 'portal' ? SITE_NAME : null;
  }

  // Set now, in <head>: the study timer (loaded below) reads document.title as its base title and
  // adds the time left in front of it. The page's own <title> stays in the file (search engines,
  // PDF metadata: the print mode keeps it).
  function applySiteName() {
    var title = PRINT_MODE ? null : siteTitle();
    if (title && document.title !== title && document.title.indexOf(' \u2014 ' + title) === -1) document.title = title;
    var marks = document.querySelectorAll('[data-site-name]');
    for (var i = 0; i < marks.length; i++) marks[i].textContent = SITE_NAME;
  }
  applySiteName();

  var KEY = 'ae_theme';
  var LEGACY_KEYS = ['aero-portal-theme', 'theme'];
  var DEFAULT_THEME = 'dark';
  var root = document.documentElement;

  function isValid(theme) {
    return theme === 'dark' || theme === 'light';
  }

  function read(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }

  function write(key, value) {
    try { localStorage.setItem(key, value); } catch (e) { /* storage blocked: keep the theme in memory only */ }
  }

  function stored() {
    var value = read(KEY);
    if (isValid(value)) return value;
    for (var i = 0; i < LEGACY_KEYS.length; i++) {
      value = read(LEGACY_KEYS[i]);
      if (isValid(value)) {
        write(KEY, value);
        return value;
      }
    }
    return null;
  }

  function get() {
    return stored() || DEFAULT_THEME;
  }

  function render(theme) {
    root.setAttribute('data-theme', theme);
    var label = document.getElementById('themeLabel');
    if (label) label.textContent = theme === 'dark' ? 'Dark' : 'Light';
    document.dispatchEvent(new CustomEvent('ae-theme-change', { detail: { theme: theme } }));
  }

  function set(theme) {
    if (!isValid(theme)) return;
    write(KEY, theme);
    render(theme);
  }

  function toggle() {
    set(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  }

  // ---- Reading surface -------------------------------------------------------------------
  var SURFACE_KEY = 'ae_surface';
  var SURFACES = [
    { id: 'default',     label: 'Default',     mode: null,      note: 'The portal\u2019s own surfaces.' },
    { id: 'cream',       label: 'Cream',       mode: 'light', note: 'Warm ivory, no pure white page. Light.' },
    { id: 'sepia',       label: 'Sepia',       mode: 'light', note: 'Warm parchment, less 415\u2013455 nm blue light. Light.' },
    { id: 'slate-paper', label: 'Slate paper', mode: 'light', note: 'Neutral e-ink grey. Light.' },
    { id: 'sage',        label: 'Sage',        mode: 'light', note: 'Muted green near the 555 nm photopic peak. Light.' },
    { id: 'charcoal',    label: 'Charcoal',    mode: 'dark',  note: 'Graphite slate, no pure black (anti-halation). Dark.' }
  ];

  function findSurface(id) {
    for (var i = 0; i < SURFACES.length; i++) if (SURFACES[i].id === id) return SURFACES[i];
    return null;
  }

  function getSurface() {
    var value = read(SURFACE_KEY);
    return findSurface(value) ? value : 'default';
  }

  function applySurface(id) {
    root.setAttribute('data-surface', id);
    document.dispatchEvent(new CustomEvent('ae-surface-change', { detail: { surface: id } }));
  }

  function setSurface(id) {
    var surface = findSurface(id);
    if (!surface) return;
    write(SURFACE_KEY, id);
    applySurface(id);
    // Palette first, then theme: the theme-change listener below then sees a matching pair.
    // No theme toggle: 'default' returns to the portal's own theme, the others to their polarity.
    var mode = surface.mode || DEFAULT_THEME;
    if (root.getAttribute('data-theme') !== mode) set(mode);
  }

  function surfaceFitsTheme(id, theme) {
    var surface = findSurface(id);
    return !surface || !surface.mode || surface.mode === theme;
  }

  // Apply immediately: this runs in <head>, before the body paints.
  root.setAttribute('data-theme', get());
  root.setAttribute('data-surface', getSurface());
  if (!surfaceFitsTheme(getSurface(), get())) {
    // No theme toggle any more: the palette decides the polarity, so a stale stored theme follows it.
    write(KEY, findSurface(getSurface()).mode);
    root.setAttribute('data-theme', findSurface(getSurface()).mode);
  }

  // Another tab changed the theme or the surface. That tab already stored a matching pair, so this
  // one only mirrors it: a theme change that arrives first must not reset (and re-write) the surface.
  var mirroring = false;
  window.addEventListener('storage', function (event) {
    if (event.key === KEY && isValid(event.newValue)) {
      mirroring = true;
      try { render(event.newValue); } finally { mirroring = false; }
    }
    if (event.key === SURFACE_KEY) applySurface(findSurface(event.newValue) ? event.newValue : 'default');
  });

  // A theme change made here that no longer fits the palette's polarity drops the palette.
  document.addEventListener('ae-theme-change', function (event) {
    if (mirroring) return;
    if (!surfaceFitsTheme(root.getAttribute('data-surface'), event.detail.theme)) setSurface('default');
  });

  // ---- Picker UI (only on pages that load study-surface.css) -----------------------------
  function element(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function buildPicker() {
    var toggleButton = document.getElementById('themeToggle');
    if (!toggleButton || !toggleButton.parentNode || document.getElementById('surfacePicker')) return;
    if (!document.querySelector('link[href*="study-surface.css"]')) return;

    var wrap = element('div', 'surface-picker');
    wrap.id = 'surfacePicker';

    var trigger = element('button', 'surface-picker__btn');
    trigger.type = 'button';
    trigger.id = 'surfaceButton';
    trigger.setAttribute('aria-haspopup', 'true');
    trigger.setAttribute('aria-expanded', 'false');
    trigger.setAttribute('aria-controls', 'surfacePanel');
    trigger.title = 'Reading background';
    var current = element('span', 'surface-swatch');
    current.setAttribute('aria-hidden', 'true');
    trigger.appendChild(current);

    var panel = element('div', 'surface-panel');
    panel.id = 'surfacePanel';
    panel.setAttribute('role', 'group');
    panel.setAttribute('aria-label', 'Reading background');
    var row = element('div', 'surface-panel__swatches');
    row.setAttribute('role', 'radiogroup');
    row.setAttribute('aria-label', 'Reading background palette');
    var caption = element('p', 'surface-panel__caption');
    caption.setAttribute('aria-live', 'polite');

    var swatches = SURFACES.map(function (surface) {
      var swatch = element('button', 'surface-swatch');
      swatch.type = 'button';
      swatch.setAttribute('role', 'radio');
      swatch.setAttribute('aria-label', surface.label + '. ' + surface.note);
      swatch.setAttribute('data-surface', surface.id);
      swatch.setAttribute('data-label', surface.label);
      swatch.addEventListener('click', function () { setSurface(surface.id); });
      swatch.addEventListener('mouseenter', function () { describe(surface.id); });
      swatch.addEventListener('focus', function () { describe(surface.id); });
      swatch.addEventListener('mouseleave', function () { describe(root.getAttribute('data-surface')); });
      row.appendChild(swatch);
      return swatch;
    });

    panel.appendChild(row);
    panel.appendChild(caption);
    wrap.appendChild(trigger);
    toggleButton.parentNode.insertBefore(wrap, toggleButton);
    // The panel lives on <body>: inside a header with transform/backdrop-filter, position:fixed
    // would be measured against the header instead of the viewport.
    document.body.appendChild(panel);

    function describe(id) {
      var surface = findSurface(id) || SURFACES[0];
      caption.textContent = '';
      caption.appendChild(element('strong', '', surface.label));
      caption.appendChild(document.createTextNode(' \u2014 ' + surface.note));
    }

    function sync() {
      var id = root.getAttribute('data-surface');
      var surface = findSurface(id) || SURFACES[0];
      current.setAttribute('data-surface', surface.id);
      trigger.setAttribute('aria-label', 'Reading background: ' + surface.label);
      swatches.forEach(function (swatch) {
        var on = swatch.getAttribute('data-surface') === surface.id;
        swatch.setAttribute('aria-checked', on ? 'true' : 'false');
        swatch.tabIndex = on ? 0 : -1;
      });
      describe(surface.id);
    }

    // Desktop: under the trigger, kept inside the viewport. Phone widths: CSS bottom sheet.
    function place() {
      if (window.matchMedia('(max-width: 600px)').matches) {
        panel.style.top = '';
        panel.style.left = '';
        return;
      }
      var box = trigger.getBoundingClientRect();
      var width = panel.offsetWidth;
      var left = Math.max(12, Math.min(box.right - width, window.innerWidth - width - 12));
      panel.style.top = Math.round(box.bottom + 10) + 'px';
      panel.style.left = Math.round(left) + 'px';
    }

    function isOpen() { return panel.classList.contains('is-open'); }

    function open() {
      place();
      wrap.classList.add('is-open');
      panel.classList.add('is-open');
      trigger.setAttribute('aria-expanded', 'true');
      var checked = row.querySelector('[aria-checked="true"]');
      if (checked) checked.focus();
    }

    function close(returnFocus) {
      wrap.classList.remove('is-open');
      panel.classList.remove('is-open');
      trigger.setAttribute('aria-expanded', 'false');
      if (returnFocus) trigger.focus();
    }

    trigger.addEventListener('click', function () {
      if (isOpen()) close(false); else open();
    });

    window.addEventListener('resize', function () { if (isOpen()) place(); });
    window.addEventListener('scroll', function () { if (isOpen()) place(); }, true);

    function onKeydown(event) {
      if (!isOpen()) return;
      if (event.key === 'Escape') {
        event.stopPropagation();
        close(true);
        return;
      }
      if (event.key === 'Tab' && panel.contains(event.target)) {
        event.preventDefault();   // the panel sits at the end of <body>: hand focus back to the trigger
        close(true);
        return;
      }
      var step = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[event.key];
      var index = swatches.indexOf(document.activeElement);
      if (!step || index < 0) return;
      event.preventDefault();
      var next = swatches[(index + step + swatches.length) % swatches.length];
      next.tabIndex = 0;
      swatches[index].tabIndex = -1;
      next.focus();
    }

    wrap.addEventListener('keydown', onKeydown);
    panel.addEventListener('keydown', onKeydown);

    document.addEventListener('click', function (event) {
      if (!wrap.contains(event.target) && !panel.contains(event.target)) close(false);
    });

    document.addEventListener('ae-surface-change', sync);
    sync();
  }

  document.addEventListener('DOMContentLoaded', function () {
    render(root.getAttribute('data-theme'));
    applySiteName();
    var button = document.getElementById('themeToggle');
    if (button) {
      if (document.querySelector('link[href*="study-surface.css"]')) {
        button.hidden = true; button.style.display = 'none';   // palettes own the polarity
      } else {
        // The landing page has no reading palettes: its button switches dark and light.
        button.setAttribute('aria-pressed', String(root.getAttribute('data-theme') === 'light'));
        button.addEventListener('click', function () {
          toggle();
          button.setAttribute('aria-pressed', String(root.getAttribute('data-theme') === 'light'));
        });
      }
    }
    buildPicker();
  });

  // ---- Focus Lab (study sound), the study timer and the updates panel, resolved next to this file
  (function loadWidgets() {
    var self = document.currentScript;
    if (!self || !self.src || /[?&]print=/.test(location.search)) return;
    // Each data file comes before its script: updates.js reads window.AE_UPDATES and sidebar.js
    // window.AE_NAV when they run.
    ['focus-lab.js', 'pomodoro.js', '../data/updates.js', 'updates.js', '../data/nav.js', 'sidebar.js', 'problem-collapse.js', 'theory-reader.js', 'solution-close.js'].forEach(function (name) {
      var script = document.createElement('script');
      script.async = false;   // run in this order, so the widgets always land in the DOM the same way
      script.src = self.src.replace(/theme\.js(\?.*)?$/, name);
      (document.head || document.documentElement).appendChild(script);
    });
  })();

  // Favicon & app shortcut icon for pages that do not link them themselves.
  (function addFavicon() {
    var self = document.currentScript;
    if (!self || !self.src) return;
    if (!document.querySelector('link[rel~="icon"]')) {
      var link = document.createElement('link');
      link.rel = 'icon';
      link.type = 'image/svg+xml';
      link.href = self.src.replace(/js\/theme\.js(\?.*)?$/, 'img/favicon.svg?v=20261117a');
      document.head.appendChild(link);
    }
    if (!document.querySelector('link[rel="apple-touch-icon"]')) {
      var apple = document.createElement('link');
      apple.rel = 'apple-touch-icon';
      apple.setAttribute('sizes', '180x180');
      apple.href = self.src.replace(/js\/theme\.js(\?.*)?$/, 'img/apple-touch-icon.png?v=20261117a');
      document.head.appendChild(apple);
    }
  })();

  // Transparent Sideris constellation + orbit emblem (shared by sidebar, Focus Lab and Study timer).
  function createSiderisMark(size, className) {
    var ns = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '96 96 832 832');
    svg.setAttribute('width', String(size || 24));
    svg.setAttribute('height', String(size || 24));
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    if (className) svg.setAttribute('class', className);

    function node(tag, attrs) {
      var el = document.createElementNS(ns, tag);
      for (var k in attrs) el.setAttribute(k, attrs[k]);
      return el;
    }

    ['M 398.51,379.43 A 355,160 -14 0 1 652.50,634.24',
     'M 624.34,644.98 A 355,160 -14 0 1 370.40,390.21'].forEach(function (d) {
      svg.appendChild(node('path', {
        d: d, 'class': 'sideris-stroke', fill: 'none', 'stroke-width': '18',
        'stroke-linecap': 'round', 'stroke-opacity': '0.94'
      }));
    });
    svg.appendChild(node('polyline', {
      points: '652,286 512,212 368,290 392,430 512,512 632,594 652,736 510,812 368,738',
      'class': 'sideris-stroke', fill: 'none', 'stroke-width': '20',
      'stroke-linecap': 'round', 'stroke-linejoin': 'round'
    }));
    [[652, 286, 23], [512, 212, 26], [368, 290, 22], [392, 430, 25],
     [632, 594, 24], [652, 736, 26], [510, 812, 24], [368, 738, 25]].forEach(function (c) {
      svg.appendChild(node('circle', { cx: c[0], cy: c[1], r: c[2], 'class': 'sideris-fill' }));
    });
    svg.appendChild(node('path', {
      d: 'M 512,454 Q 521.3,502.7 570,512 Q 521.3,521.3 512,570 Q 502.7,521.3 454,512 Q 502.7,502.7 512,454 Z',
      'class': 'sideris-fill'
    }));
    [
      'M 612,370 Q 613.5,390.5 634,392 Q 613.5,393.5 612,414 Q 610.5,393.5 590,392 Q 610.5,390.5 612,370 Z',
      'M 410,616 Q 411.3,634.7 429,636 Q 411.3,637.3 410,656 Q 408.7,637.3 391,636 Q 408.7,634.7 410,616 Z',
      'M 222,336 Q 223.8,358.2 246,360 Q 223.8,361.8 222,384 Q 220.2,361.8 198,360 Q 220.2,358.2 222,336 Z',
      'M 800,600 Q 801.4,618.6 820,620 Q 801.4,621.4 800,640 Q 798.6,621.4 780,620 Q 798.6,618.6 800,600 Z'
    ].forEach(function (d) {
      svg.appendChild(node('path', { d: d, 'class': 'sideris-fill', 'fill-opacity': '0.94' }));
    });
    [[298, 176, 8], [734, 700, 8], [406, 864, 7.5], [158, 676, 7.5], [854, 240, 7.5]].forEach(function (c) {
      svg.appendChild(node('circle', { cx: c[0], cy: c[1], r: c[2], 'class': 'sideris-fill', 'fill-opacity': '0.84' }));
    });
    return svg;
  }

  window.AESite = { name: SITE_NAME, subjects: SUBJECT_SHORT, title: siteTitle, mark: createSiderisMark };
  window.AETheme = { get: get, set: set, toggle: toggle, KEY: KEY };
  window.AESurface = {
    get: function () { return root.getAttribute('data-surface') || getSurface(); },
    set: setSurface,
    list: function () { return SURFACES.map(function (s) { return { id: s.id, label: s.label, mode: s.mode }; }); },
    KEY: SURFACE_KEY
  };
})();
