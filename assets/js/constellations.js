/*!
 * Home page, stellar view: interactive constellation map (root index.html only).
 *
 * Load synchronously in <head>, after theme.js and before the body is parsed:
 *     <script src="assets/js/constellations.js"></script>
 * The head part reads the stored view and palette and sets <html data-home-view> and
 * <html data-sky-palette> before the first paint. The map itself is built on window load, once
 * assets/data/nav.js (added by theme.js) has defined window.AE_NAV.
 *
 * Views (key ae_home_view): 'constellations' (default) | 'classic' (the original card view, which
 * stays in the DOM, hidden, so the audit of its badges still reads it).
 * Sky palettes (key ae_sky_palette, never a key with "theme" in it): deep-cosmos, observatory-charcoal,
 * nebula-indigo, stratospheric-light, blueprint-cyan. Each one has a polarity; choosing it also sets
 * the portal theme through window.AETheme, like the reading palettes of the subject pages.
 *
 * Map: one SVG with a camera (the viewBox). Panorama = the five first-semester subjects joined by
 * faint guide lines, plus a pulsar for the second semester. A constellation takes the shape of its
 * subject icon; its stars are the main areas of the subject (Theory, Solved Problems, Extra Problems,
 * Formula Sheet, Exam Simulator, PDFs, Exams) read from window.AE_NAV, with the counters of the
 * classic cards. Click or Enter on a constellation: the camera glides to it. Escape, the back button or
 * a click on empty sky: back to the panorama. prefers-reduced-motion: the camera jumps.
 *
 * API: window.AEConstellations = { select(slug), back(), view(), setView(v), palette(), setPalette(id), playIntro }
 * Event: document 'ae-constellations-ready' once the map is built.
 */
(function () {
  'use strict';

  var VIEW_KEY = 'ae_home_view';
  var PALETTE_KEY = 'ae_sky_palette';
  var root = document.documentElement;
  var SVGNS = 'http://www.w3.org/2000/svg';

  function read(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }
  function write(key, value) { try { localStorage.setItem(key, value); } catch (e) { /* storage blocked: keep it in memory */ } }

  var PALETTES = [
    { id: 'deep-cosmos',           label: 'Deep Cosmos',           mode: 'dark' },
    { id: 'observatory-charcoal',  label: 'Observatory Charcoal',  mode: 'dark' },
    { id: 'nebula-indigo',         label: 'Nebula Indigo',         mode: 'dark' },
    { id: 'stratospheric-light',   label: 'Stratospheric Light',   mode: 'light' },
    { id: 'blueprint-cyan',        label: 'Blueprint Cyan',        mode: 'dark' }
  ];

  function findPalette(id) {
    for (var i = 0; i < PALETTES.length; i++) if (PALETTES[i].id === id) return PALETTES[i];
    return null;
  }

  var view = read(VIEW_KEY) === 'classic' ? 'classic' : 'constellations';
  var palette = findPalette(read(PALETTE_KEY)) || PALETTES[0];
  root.setAttribute('data-home-view', view);
  root.setAttribute('data-sky-palette', palette.id);

  // The palette decides the polarity of the portal while the stellar view is on.
  function syncTheme() {
    if (view !== 'constellations' || !window.AETheme) return;
    if (root.getAttribute('data-theme') !== palette.mode) window.AETheme.set(palette.mode);
  }
  syncTheme();

  /* ---------------------------------------------------------------------------------------
     Subjects: Latin titles and the silhouette of each constellation (local coordinates, about
     +-180). anchors() are the places the stars take, in section order; edges join anchors by
     index; decor are faint extra paths that complete the silhouette.
     --------------------------------------------------------------------------------------- */
  function ring(n, rx, ry, start, rot) {
    var out = [], c = Math.cos(rot || 0), s = Math.sin(rot || 0);
    for (var k = 0; k < n; k++) {
      var a = start + k * 2 * Math.PI / n, x = rx * Math.cos(a), y = ry * Math.sin(a);
      out.push([Math.round(x * c - y * s), Math.round(x * s + y * c)]);
    }
    return out;
  }
  function chain(n, closed) {
    var e = [];
    for (var k = 0; k < n - 1; k++) e.push([k, k + 1]);
    if (closed) e.push([n - 1, 0]);
    return e;
  }

  var META = {
    'fluid-mechanics': {
      latin: 'Stella Fluidorum', color: 'fluid',
      anchors: (function () {
        var out = [];
        for (var k = 0; k < 7; k++) {   // a spiral that unwinds like a vortex
          var a = -2.7 + k * 0.98, r = 182 - k * 21;
          out.push([Math.round(r * Math.cos(a)), Math.round(r * Math.sin(a) * 0.82)]);
        }
        return out;
      })(),
      edges: chain(7, false),
      decor: ['M-190 -100 C-110 -150 -20 -50 60 -100 S160 -90 195 -120', 'M-195 120 C-115 80 -35 160 45 120 S150 130 195 100']
    },
    'aerospace-materials-1': {
      latin: 'Stella Materiae', color: 'materials',
      anchors: ring(6, 118, 118, -Math.PI / 2).concat([[0, 0]]),   // a hexagonal lattice cell and its centre
      edges: chain(6, true).concat([[0, 6], [2, 6], [4, 6]]),
      decor: ['M0 -160 L139 -80 L139 80 L0 160 L-139 80 L-139 -80 Z']
    },
    'engineering-mechanics': {
      latin: 'Stella Mechanicae', color: 'mechanics',
      anchors: ring(7, 175, 88, -2.2, -0.35),   // an elliptic orbit
      edges: chain(7, true),
      decor: ['M0 0 L165 -62', 'M-190 40 L190 -40']
    },
    'advanced-maths': {
      latin: 'Stella Matheseos', color: 'maths',
      anchors: (function () {   // one period of a harmonic wave, a star at every node and extremum
        var out = [];
        for (var k = 0; k < 7; k++) out.push([-240 + k * 80, Math.round(-100 * Math.sin(k * Math.PI / 3))]);
        return out;
      })(),
      labels: ['l', 't', 'b', 't', 'b', 't', 'r'],
      edges: chain(7, false),
      decor: (function () {
        var d = 'M-240 0';
        for (var x = -230; x <= 240; x += 10) d += ' L' + x + ' ' + (-115.5 * Math.sin((x + 240) / 80 * Math.PI / 3)).toFixed(1);
        return ['M-250 0 L250 0', d];
      })()
    },
    'business-management': {
      latin: 'Stella Oeconomiae', color: 'business',
      anchors: [[-155, 38], [-82, -76], [0, 22], [76, -84], [158, -8], [62, 92], [-64, 104]],   // a network graph
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 2], [2, 6], [6, 0], [1, 6]],
      decor: ['M-155 38 L62 92']
    }
  };
  var ORDER = ['fluid-mechanics', 'aerospace-materials-1', 'engineering-mechanics', 'advanced-maths', 'business-management'];

  // Main areas of a subject, in this order. Labels follow the brief; keys come from nav.json.
  var SECTIONS = [
    { key: 'theory',  label: 'Theory' },
    { key: 'problems', label: 'Solved Problems' },
    { key: 'extra',   label: 'Extra Problems' },
    { key: 'formula', label: 'Formula Sheet' },
    { key: 'sim',     label: 'Exam Simulator' },
    { key: 'pdfs',    label: 'Theory & exercise PDFs' },
    { key: 'exams',   label: 'Exams' }
  ];
  function keyOf(id, label) {
    if (id === 'teoria') return 'theory';
    if (id === 'problemas') return 'problems';
    if (id === 'extra-problems') return 'extra';
    var l = String(label || '').toLowerCase();
    if (l.indexOf('simulator') >= 0) return 'sim';
    if (l.indexOf('formula') >= 0) return 'formula';
    if (l.indexOf('pdf') >= 0) return 'pdfs';
    if (l.indexOf('exam') >= 0) return 'exams';
    return null;
  }

  /* Layouts of the panorama (centres of the five constellations and of the pulsar). */
  var LAND = { box: [1600, 960], centre: [800, 480], slots: [[330, 255], [800, 205], [1270, 265], [560, 590], [1065, 600]], pulsar: [1490, 800] };
  var PORT = { box: [1000, 2150], centre: [500, 1075], slots: [[260, 210], [740, 610], [260, 1010], [740, 1410], [260, 1810]], pulsar: [800, 2050] };
  var GUIDES = [[0, 1], [1, 2], [2, 4], [4, 3], [3, 0], [1, 3], [1, 4]];

  var ZOOM_H = 400;          // height of the camera box on a constellation (user units)
  var ZOOM_BW = [640, 800];  // minimum width of that box: landscape, portrait

  /* ---------------------------------------------------------------------------------------
     Build
     --------------------------------------------------------------------------------------- */
  var stage, svg, back, caption, titleEl, select, toggle;
  var items = [];           // { slug, g, stars[], slot, title }
  var guides = [], pulsarG;
  var selected = null;
  var cam = null, camAnim = 0;
  var built = false;

  function s(tag, attrs, parent) {
    var node = document.createElementNS(SVGNS, tag);
    if (attrs) for (var k in attrs) if (Object.prototype.hasOwnProperty.call(attrs, k)) node.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(node);
    return node;
  }
  function h(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  // The counters of the classic cards, found by href, keep the map and the audited badges in step.
  function counterFor(slug, href) {
    var card = document.querySelector('.subject-card[data-subject="' + slug + '"]');
    var link = card && card.querySelector('a[href="' + href + '"]');
    if (!link) return '';
    var badge = link.querySelector('.area-badge');
    if (badge) return badge.textContent.trim();
    var label = link.getAttribute('aria-label') || '';
    var i = label.indexOf(': ');
    return i >= 0 ? label.slice(i + 2) : '';
  }

  function sectionsOf(sub) {
    var found = {};
    (sub.groups || []).forEach(function (g) { var k = keyOf(g.id, g.label); if (k) found[k] = g.href; });
    (sub.extras || []).forEach(function (e) { var k = keyOf(null, e.label); if (k) found[k] = e.href; });
    return SECTIONS.filter(function (sec) { return found[sec.key]; }).map(function (sec) {
      return { key: sec.key, label: sec.label, href: found[sec.key], count: counterFor(sub.slug, found[sec.key]) };
    });
  }

  function buildConstellation(sub, index, defs) {
    var meta = META[sub.slug];
    var g = s('g', {
      'class': 'const', 'data-slug': sub.slug, tabindex: '0', role: 'button',
      'aria-label': meta.latin + ', ' + sub.name + '. Press Enter to open its areas.'
    });
    g.style.setProperty('--c', 'var(--c-' + meta.color + ')');
    var list = sectionsOf(sub);

    s('circle', { 'class': 'const-hit', cx: 0, cy: 0, r: 215 }, g);
    s('circle', { 'class': 'const-glow', cx: 0, cy: 0, r: 140 }, g);
    meta.decor.forEach(function (d) { s('path', { 'class': 'const-decor', d: d }, g); });

    var used = list.length;
    meta.edges.forEach(function (e) {
      if (e[0] >= used && e[1] >= used) return;
      var a = meta.anchors[e[0]], b = meta.anchors[e[1]];
      s('line', { 'class': 'const-edge', x1: a[0], y1: a[1], x2: b[0], y2: b[1] }, g);
    });
    meta.anchors.slice(used).forEach(function (p) { s('circle', { 'class': 'const-dot', cx: p[0], cy: p[1], r: 3.2 }, g); });

    var stars = list.map(function (sec, i) {
      var p = meta.anchors[i];
      var a = s('a', {
        'class': 'star' + (/soon/i.test(sec.count) ? ' is-soon' : ''), href: sec.href, tabindex: '-1',
        transform: 'translate(' + p[0] + ' ' + p[1] + ')',
        'aria-label': sec.label + (sec.count ? ', ' + sec.count : '') + ', ' + sub.name
      }, g);
      s('circle', { 'class': 'star-hit', r: 24 }, a);
      s('circle', { 'class': 'star-halo', r: 15 }, a);
      var glyph = s('path', { 'class': 'star-glyph', d: 'M0 -17 L4 -4 L17 0 L4 4 L0 17 L-4 4 L-17 0 L-4 -4Z' }, a);
      s('circle', { 'class': 'star-core', r: 3.2 }, a);
      // label side: from the constellation when it lists one, else the star's own side of the shape
      var side = (meta.labels && meta.labels[i]) || (Math.abs(p[0]) < 22 ? (p[1] < 0 ? 't' : 'b') : (p[0] < 0 ? 'l' : 'r'));
      var vertical = side === 't' || side === 'b';
      var attrs = vertical
        ? { 'text-anchor': 'middle', x: 0, y: side === 't' ? -26 : 34 }
        : { 'text-anchor': side === 'l' ? 'end' : 'start', x: side === 'l' ? -22 : 22, y: 5 };
      var name = s('text', attrs, a); name.setAttribute('class', 'star-name'); name.textContent = sec.label;
      var cAttrs = {}; for (var k in attrs) cAttrs[k] = attrs[k];
      cAttrs.y = Number(attrs.y) + (side === 't' ? -16 : 18);
      var count = s('text', cAttrs, a); count.setAttribute('class', 'star-count'); count.textContent = sec.count;
      void glyph;
      return a;
    });

    // panorama labels (hidden while zoomed)
    var t = s('text', { 'class': 'const-title', x: 0, y: 232 }, g); t.textContent = meta.latin;
    var u = s('text', { 'class': 'const-sub', x: 0, y: 256 }, g); u.textContent = sub.name;

    return { slug: sub.slug, name: sub.name, latin: meta.latin, g: g, stars: stars, index: index, sections: list };
  }

  function currentLayout() {
    var r = stage.getBoundingClientRect();
    return r.width / Math.max(1, r.height) < 0.85 ? PORT : LAND;
  }

  function applyLayout() {
    var L = currentLayout();
    items.forEach(function (it) {
      it.slot = L.slots[it.index];
      it.g.setAttribute('transform', 'translate(' + it.slot[0] + ' ' + it.slot[1] + ')');
    });
    guides.forEach(function (gl) {
      var a = L.slots[gl.a], b = L.slots[gl.b];
      gl.el.setAttribute('x1', a[0]); gl.el.setAttribute('y1', a[1]); gl.el.setAttribute('x2', b[0]); gl.el.setAttribute('y2', b[1]);
    });
    pulsarG.setAttribute('transform', 'translate(' + L.pulsar[0] + ' ' + L.pulsar[1] + ')');
    return L;
  }

  /* ---------------------------------------------------------------------------------------
     Camera
     --------------------------------------------------------------------------------------- */
  function target() {
    var L = currentLayout();
    var r = stage.getBoundingClientRect();
    var asp = r.width / Math.max(1, r.height);
    if (!selected) return { cx: L.centre[0], cy: L.centre[1], bw: L.box[0], bh: L.box[1], asp: asp };
    var it = byslug(selected);
    return { cx: it.slot[0], cy: it.slot[1] + 38, bw: ZOOM_BW[asp < 0.85 ? 1 : 0], bh: ZOOM_H, asp: asp };
  }

  function boxOf(t) {   // the viewBox that holds the target box at the container's aspect ratio
    var w = Math.max(t.bw, t.bh * t.asp);
    var hh = w / t.asp;
    return { x: t.cx - w / 2, y: t.cy - hh / 2, w: w, h: hh };
  }

  function paint(b) {
    svg.setAttribute('viewBox', b.x.toFixed(2) + ' ' + b.y.toFixed(2) + ' ' + b.w.toFixed(2) + ' ' + b.h.toFixed(2));
    var px = svg.getBoundingClientRect().width || 1;
    svg.style.setProperty('--u', (b.w / px).toFixed(4));   // user units per CSS pixel: keeps text at a readable size
  }

  function reduced() { return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches; }

  function moveCamera(instant) {
    var to = boxOf(target());
    cancelAnimationFrame(camAnim);
    if (instant || reduced() || !cam) { cam = to; paint(cam); return; }
    var from = cam, start = null, dur = 750;
    function step(now) {
      if (start === null) start = now;
      var p = Math.min(1, (now - start) / dur);
      var e = p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
      cam = {
        x: from.x + (to.x - from.x) * e, y: from.y + (to.y - from.y) * e,
        w: from.w + (to.w - from.w) * e, h: from.h + (to.h - from.h) * e
      };
      paint(cam);
      if (p < 1) camAnim = requestAnimationFrame(step);
    }
    camAnim = requestAnimationFrame(step);
  }

  /* ---------------------------------------------------------------------------------------
     State
     --------------------------------------------------------------------------------------- */
  function byslug(slug) {
    for (var i = 0; i < items.length; i++) if (items[i].slug === slug) return items[i];
    return null;
  }

  var HINT = 'Choose a constellation to explore a subject. Tab and Enter work too.';

  function renderState(focus) {
    svg.classList.toggle('is-zoomed', !!selected);
    items.forEach(function (it) {
      var on = it.slug === selected;
      it.g.classList.toggle('is-active', on);
      it.g.setAttribute('tabindex', selected && !on ? '-1' : '0');
      it.g.setAttribute('aria-expanded', on ? 'true' : 'false');
      it.stars.forEach(function (a) { a.setAttribute('tabindex', on ? '0' : '-1'); });
    });
    back.hidden = !selected;
    caption.textContent = '';
    if (selected) {
      var it = byslug(selected);
      caption.appendChild(h('h2', '', it.latin));
      caption.appendChild(h('p', '', it.name + ' · ' + it.sections.length + ' areas · Esc returns to all constellations'));
    } else {
      caption.appendChild(h('p', '', HINT));
    }
    if (focus) {
      var node = selected ? (byslug(selected).stars[0] || byslug(selected).g) : (focus === true ? null : focus);
      if (node && node.focus) node.focus({ preventScroll: true });
    }
  }

  function selectConstellation(slug, fromKeyboard) {
    if (!byslug(slug)) return;
    selected = slug;
    moveCamera(false);
    renderState(fromKeyboard ? true : false);
  }

  function backToPanorama() {
    if (!selected) return;
    var prev = byslug(selected);
    selected = null;
    moveCamera(false);
    renderState(prev.g);
  }

  /* ---------------------------------------------------------------------------------------
     Views and palettes
     --------------------------------------------------------------------------------------- */
  function renderToggle() {
    if (!toggle) return;
    toggle.textContent = view === 'constellations' ? 'Classic view' : 'Stellar view';
    toggle.title = view === 'constellations' ? 'Switch to the classic card view' : 'Switch to the stellar map';
    toggle.setAttribute('aria-label', toggle.title);
  }

  function setView(next) {
    if (next !== 'classic' && next !== 'constellations') return;
    view = next;
    write(VIEW_KEY, view);
    root.setAttribute('data-home-view', view);
    if (view === 'constellations') {
      syncTheme();
      if (built) moveCamera(true);
    } else if (selected) {
      selected = null;
      if (built) renderState(false);
    }
    renderToggle();
  }

  function setPalette(id) {
    var p = findPalette(id);
    if (!p) return;
    palette = p;
    write(PALETTE_KEY, p.id);
    root.setAttribute('data-sky-palette', p.id);
    if (select) select.value = p.id;
    syncTheme();
  }

  // A theme change from elsewhere (the T key, another tab) that breaks the polarity picks the
  // default palette of the new polarity.
  document.addEventListener('ae-theme-change', function (event) {
    if (view !== 'constellations') return;
    var mode = event.detail && event.detail.theme;
    if (mode && palette.mode !== mode) {
      for (var i = 0; i < PALETTES.length; i++) if (PALETTES[i].mode === mode) { setPalette(PALETTES[i].id); return; }
    }
  });

  /* ---------------------------------------------------------------------------------------
     Hook for a future entrance animation: nothing plays today; an intro would replace this
     function (it may return a Promise) and the map would wait for it before taking input.
     --------------------------------------------------------------------------------------- */
  function playIntro() { return Promise.resolve(); }

  /* ---------------------------------------------------------------------------------------
     Init
     --------------------------------------------------------------------------------------- */
  function build() {
    var nav = window.AE_NAV;
    stage = document.getElementById('skyView');
    svg = document.getElementById('skySvg');
    back = document.getElementById('skyBack');
    caption = document.getElementById('skyCaption');
    toggle = document.getElementById('homeViewToggle');
    select = document.getElementById('skyPalette');
    if (!nav || !stage || !svg) return false;

    var subjects = {};
    nav.subjects.forEach(function (sub) { subjects[sub.slug] = sub; });

    var guideLayer = s('g', { 'aria-hidden': 'true' }, svg);
    GUIDES.forEach(function (pair) { guides.push({ a: pair[0], b: pair[1], el: s('line', { 'class': 'guide-line' }, guideLayer) }); });

    ORDER.forEach(function (slug, i) {
      if (!subjects[slug] || !META[slug]) return;
      var it = buildConstellation(subjects[slug], i);
      items.push(it);
      svg.appendChild(it.g);
    });

    pulsarG = s('g', { 'class': 'pulsar', 'aria-label': 'Second semester: in preparation', role: 'img' }, svg);
    s('circle', { 'class': 'pulsar-ring', r: 10 }, pulsarG);
    s('circle', { 'class': 'pulsar-core', r: 4 }, pulsarG);
    var pl = s('text', { 'class': 'pulsar-label', x: -20, y: 5 }, pulsarG); pl.textContent = 'In Preparation · Q2';

    applyLayout();
    renderState(false);
    built = true;
    moveCamera(true);

    // Clicks: a constellation selects (a star of a closed one must not navigate), empty sky goes back.
    svg.addEventListener('click', function (event) {
      var star = event.target.closest && event.target.closest('.star');
      var group = event.target.closest && event.target.closest('.const');
      if (group && group.getAttribute('data-slug') !== selected) {
        event.preventDefault();
        selectConstellation(group.getAttribute('data-slug'), false);
        return;
      }
      if (!star && !group) backToPanorama();
      else if (!star && group) { /* inside the open constellation: nothing */ }
    });

    svg.addEventListener('keydown', function (event) {
      var group = event.target.classList && event.target.classList.contains('const') ? event.target : null;
      if (group && (event.key === 'Enter' || event.key === ' ')) {
        event.preventDefault();
        if (group.getAttribute('data-slug') !== selected) selectConstellation(group.getAttribute('data-slug'), true);
      }
    });

    back.addEventListener('click', backToPanorama);

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && view === 'constellations' && selected) {
        var tag = event.target && event.target.tagName;
        if (tag === 'INPUT' || tag === 'TEXTAREA') return;
        backToPanorama();
      }
    });

    if (toggle) toggle.addEventListener('click', function () { setView(view === 'constellations' ? 'classic' : 'constellations'); });
    if (select) {
      PALETTES.forEach(function (p) {
        var o = document.createElement('option'); o.value = p.id; o.textContent = p.label; select.appendChild(o);
      });
      select.value = palette.id;
      select.addEventListener('change', function () { setPalette(select.value); });
    }
    renderToggle();

    var resizeTimer = 0;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () { applyLayout(); moveCamera(true); }, 80);
    });

    playIntro().then(function () {
      document.dispatchEvent(new CustomEvent('ae-constellations-ready'));
    });
    return true;
  }

  function start() {
    var tries = 0;
    (function attempt() {
      if (build()) return;
      if (++tries < 40) setTimeout(attempt, 100);   // theme.js adds nav.js after the parse: wait for window.AE_NAV
    })();
  }

  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);

  window.AEConstellations = {
    select: function (slug) { selectConstellation(slug, false); },
    back: backToPanorama,
    view: function () { return view; },
    setView: setView,
    palette: function () { return palette.id; },
    setPalette: setPalette,
    palettes: function () { return PALETTES.map(function (p) { return { id: p.id, label: p.label, mode: p.mode }; }); },
    playIntro: playIntro
  };
})();
