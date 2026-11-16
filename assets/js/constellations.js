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
 * faint guide lines. A constellation takes the shape of its
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
  // Each area has its own star shape, so a star is recognised before it is read.
  function starPath(points, outer, inner, turn) {
    var d = '';
    for (var k = 0; k < points * 2; k++) {
      var r = k % 2 === 0 ? outer : outer * inner, a = turn + k * Math.PI / points - Math.PI / 2;
      d += (k ? 'L' : 'M') + (r * Math.cos(a)).toFixed(1) + ' ' + (r * Math.sin(a)).toFixed(1);
    }
    return d + 'Z';
  }
  var SHAPES = {
    theory:   starPath(4, 30, 0.2, 0),                              // a fine four-point sparkle
    problems: starPath(5, 28, 0.45, 0),                             // the classic five-point star
    extra:    starPath(6, 28, 0.55, 0),                             // a six-point star
    formula:  'M0 -34 L17 0 L0 34 L-17 0Z',                         // a tall gem
    sim:      starPath(8, 29, 0.42, 0),                             // an eight-point burst
    pdfs:     'M29 -25 A34 34 0 1 0 29 25 A27 27 0 1 1 29 -25Z',       // a crescent moon
    exams:    starPath(12, 27, 0.7, 0)                              // a toothed seal
  };

  function chain(n, closed) {
    var e = [];
    for (var k = 0; k < n - 1; k++) e.push([k, k + 1]);
    if (closed) e.push([n - 1, 0]);
    return e;
  }
  function rotate(points, deg) {
    var a = deg * Math.PI / 180, c = Math.cos(a), sn = Math.sin(a);
    return points.map(function (p) { return [Math.round(p[0] * c - p[1] * sn), Math.round(p[0] * sn + p[1] * c)]; });
  }
  function seeded(seed) {   // mulberry32: the same sky every visit
    return function () {
      seed |= 0; seed = seed + 0x6D2B79F5 | 0;
      var t = Math.imul(seed ^ seed >>> 15, 1 | seed);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  /* Hand-placed, loose silhouettes: a vortex, a distorted lattice cell, an open orbit, a damped wave
     and a network. `use` says which anchors take a star when the subject has fewer areas than
     anchors; the others stay as faint stars of the figure. `rot` turns the whole figure. */
  var META = {
    'fluid-mechanics': {
      latin: 'Stella Fluidorum', color: 'fluid', rot: -22,
      anchors: [[-215, 70], [-150, -10], [-95, -92], [-12, -60], [58, -128], [120, -20], [40, 50]],
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [5, 6]],
      use: { 4: [0, 2, 4, 6] },
      flow: [[[-215, 20], [-150, -70], [-70, -128], [30, -120], [120, -60]], [[-190, 108], [-100, 70], [-20, 96], [70, 118], [150, 76]]]
    },
    'aerospace-materials-1': {
      latin: 'Stella Materiae', color: 'materials', rot: 17,
      anchors: [[-20, -155], [95, -92], [158, 22], [60, 118], [-85, 150], [-150, 40], [-12, 6]],
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 6], [2, 6], [4, 6]],
      use: { 6: [0, 1, 2, 3, 4, 5] },
      flow: [[[-196, -120], [-60, -196], [60, -190]], [[150, 150], [60, 200], [-70, 196]]]
    },
    'engineering-mechanics': {
      latin: 'Stella Mechanicae', color: 'mechanics', rot: 24,
      anchors: [[-215, 52], [-170, -52], [-70, -110], [48, -64], [150, -92], [196, 18], [92, 98]],
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [3, 6]],
      use: {},
      flow: [[[-30, 4], [60, -40], [140, -100]], [[-210, 100], [-100, 150], [60, 160]]]
    },
    'advanced-maths': {
      latin: 'Stella Matheseos', color: 'maths', rot: -15,
      anchors: [[-250, 30], [-186, -82], [-96, -40], [-24, 56], [58, 112], [120, 10], [214, -70]],
      labels: ['l', 't', 't', 'b', 'b', 't', 'r'],
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
      use: {},
      flow: [[[-240, 36], [-120, 60], [0, 90], [120, 120]], [[-200, -120], [-60, -140], [90, -110], [210, -90]]]
    },
    'business-management': {
      latin: 'Stella Oeconomiae', color: 'business', rot: 31,
      anchors: [[-180, 60], [-112, -92], [-24, 10], [52, -110], [170, -38], [122, 96], [-48, 120]],
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 2], [2, 6], [6, 0], [1, 6]],
      use: { 6: [0, 1, 2, 3, 4, 5] },
      flow: [[[100, -150], [170, -90]], [[-190, -20], [-140, -120]]]
    }
  };
  var ORDER = ['fluid-mechanics', 'aerospace-materials-1', 'engineering-mechanics', 'advanced-maths', 'business-management'];

  // Main areas of a subject, in this order. Labels follow the brief; keys come from nav.json.
  var SECTIONS = [
    { key: 'theory',  label: 'Theory',                 icon: 'i-theory' },
    { key: 'problems', label: 'Solved Problems',        icon: 'i-problems' },
    { key: 'extra',   label: 'Extra Problems',         icon: 'i-extra' },
    { key: 'formula', label: 'Formula Sheet',          icon: 'i-formula' },
    { key: 'sim',     label: 'Exam Simulator',         icon: 'i-sim' },
    { key: 'pdfs',    label: 'Theory & exercise PDFs', icon: 'i-pdf' },
    { key: 'exams',   label: 'Exams',                  icon: 'i-exams' }
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

  /* Layouts of the panorama (centres of the five constellations). */
  var LAND = { box: [1900, 1150], centre: [950, 575], slots: [[350, 350], [930, 215], [1660, 350], [470, 880], [1290, 900]] };
  var PORT = { box: [1000, 2900], centre: [500, 1450], slots: [[260, 260], [740, 800], [240, 1380], [760, 1960], [270, 2540]] };
  var GUIDES = [[0, 1], [1, 2], [2, 4], [4, 3], [3, 0], [1, 3], [1, 4]];

  var ZOOM_H = 480;          // height of the camera box on a constellation (user units)
  var ZOOM_BW = [700, 980];  // minimum width of that box: landscape, portrait

  /* ---------------------------------------------------------------------------------------
     Build
     --------------------------------------------------------------------------------------- */
  var stage, svg, back, caption, titleEl, select, toggle;
  var items = [];           // { slug, g, stars[], slot, title }
  var guides = [];
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
      return { key: sec.key, label: sec.label, icon: sec.icon, href: found[sec.key], count: counterFor(sub.slug, found[sec.key]) };
    });
  }

  function buildConstellation(sub, index) {
    var meta = META[sub.slug];
    var g = s('g', {
      'class': 'const', 'data-slug': sub.slug, tabindex: '0', role: 'button',
      'aria-label': meta.latin + ', ' + sub.name + '. Press Enter to open its areas.'
    });
    g.style.setProperty('--c', 'var(--c-' + meta.color + ')');
    g.style.setProperty('--ct', 'var(--ct-' + meta.color + ')');
    var list = sectionsOf(sub);
    var anchors = rotate(meta.anchors, meta.rot);
    var n = list.length;
    var pick = meta.use[n];
    if (!pick) { pick = []; for (var q = 0; q < n; q++) pick.push(n === anchors.length ? q : Math.round(q * (anchors.length - 1) / Math.max(1, n - 1))); }

    s('circle', { 'class': 'const-hit', cx: 0, cy: 0, r: 235 }, g);

    // flowing guide curves of the figure, faint and dashed
    meta.flow.forEach(function (line) {
      var pts = rotate(line, meta.rot), d = 'M' + pts[0][0] + ' ' + pts[0][1];
      for (var k = 1; k < pts.length; k++) {
        var m = [(pts[k - 1][0] + pts[k][0]) / 2, (pts[k - 1][1] + pts[k][1]) / 2];
        d += ' Q' + pts[k - 1][0] + ' ' + pts[k - 1][1] + ' ' + m[0].toFixed(0) + ' ' + m[1].toFixed(0);
      }
      d += ' T' + pts[pts.length - 1][0] + ' ' + pts[pts.length - 1][1];
      s('path', { 'class': 'const-decor', d: d }, g);
    });

    // the dust of the figure: small stars that twinkle, placed by a fixed seed
    var rnd = seeded(sub.slug.length * 7919 + index * 104729);
    for (var dI = 0; dI < 16; dI++) {
      var ang = rnd() * 6.2832, rad = 70 + rnd() * 190;
      var dx = Math.round(Math.cos(ang) * rad * 1.15), dy = Math.round(Math.sin(ang) * rad * 0.8);
      var tooClose = anchors.some(function (p) { return Math.abs(p[0] - dx) + Math.abs(p[1] - dy) < 34; });
      if (tooClose) continue;
      var dot = s('circle', { 'class': 'dust', cx: dx, cy: dy, r: (0.9 + rnd() * 1.7).toFixed(1) }, g);
      dot.style.setProperty('--d', (rnd() * 5).toFixed(2) + 's');
    }

    var chosen = {};
    pick.forEach(function (ai, i) { chosen[ai] = i; });
    meta.edges.forEach(function (e) {
      var a = anchors[e[0]], b = anchors[e[1]];
      var lit = chosen[e[0]] !== undefined && chosen[e[1]] !== undefined;
      s('line', { 'class': 'const-edge' + (lit ? '' : ' is-faint'), x1: a[0], y1: a[1], x2: b[0], y2: b[1] }, g);
    });
    anchors.forEach(function (p, ai) {
      if (chosen[ai] === undefined) s('circle', { 'class': 'const-dot', cx: p[0], cy: p[1], r: 3.4 }, g);
    });

    var stars = list.map(function (sec, i) {
      var ai = pick[i], p = anchors[ai];
      var a = s('a', {
        'class': 'star' + (/soon/i.test(sec.count) ? ' is-soon' : ''), href: sec.href, tabindex: '-1',
        transform: 'translate(' + p[0] + ' ' + p[1] + ')',
        'aria-label': sec.label + (sec.count ? ', ' + sec.count : '') + ', ' + sub.name
      }, g);
      s('circle', { 'class': 'star-hit', r: 26 }, a);
      s('circle', { 'class': 'star-flare', r: 56, fill: 'url(#flare-' + meta.color + ')' }, a);
      s('path', { 'class': 'star-dot', d: starPath(4, 15, 0.24, 0) }, a);   // every star is the same small sparkle in the panorama
      s('path', { 'class': 'star-glyph', d: SHAPES[sec.key] || SHAPES.theory }, a);   // its own shape appears when the constellation is open
      s('circle', { 'class': 'star-core', r: 3.4 }, a);
      var ic = s('g', { 'class': 'star-icon' }, a);
      s('circle', { 'class': 'star-icon-bg', r: 13 }, ic);
      s('use', { href: '#' + sec.icon, x: -9.5, y: -9.5, width: 19, height: 19, 'class': 'star-icon-glyph' }, ic);
      // The name goes on the free side of the star: away from the lines that reach it and from the figure.
      var incident = [];
      meta.edges.forEach(function (e) {
        var other = e[0] === ai ? e[1] : e[1] === ai ? e[0] : -1;
        if (other >= 0) incident.push(Math.atan2(anchors[other][1] - p[1], anchors[other][0] - p[0]));
      });
      var cx = 0, cy = 0;
      anchors.forEach(function (q) { cx += q[0] / anchors.length; cy += q[1] / anchors.length; });
      var out = Math.atan2(p[1] - cy, p[0] - cx), best = -9, dx = 1, dy = 0;
      for (var step = 0; step < 24; step++) {   // the free direction: far from every line at the star, leaning outward
        var ang = step * Math.PI / 12, gap = 9;
        incident.forEach(function (ia) { var d = Math.abs(Math.atan2(Math.sin(ang - ia), Math.cos(ang - ia))); if (d < gap) gap = d; });
        var score = Math.min(gap, 1.2) + 0.35 * Math.cos(ang - out);
        if (score > best) { best = score; dx = Math.cos(ang); dy = Math.sin(ang); }
      }
      var anchor = dx > 0.35 ? 'start' : dx < -0.35 ? 'end' : 'middle';
      var ny = Math.abs(dy) > 0.5 ? dy * 52 + (dy > 0 ? 10 : -4) : dy * 44 + 5;
      var attrs = { 'text-anchor': anchor, x: Math.round(dx * (anchor === 'middle' ? 0 : 46)), y: Math.round(ny) };
      var name = s('text', attrs, a); name.setAttribute('class', 'star-name'); name.setAttribute('display', 'none'); name.textContent = sec.label;
      var cAttrs = {}; for (var k in attrs) cAttrs[k] = attrs[k];
      cAttrs.y = Math.round(ny) + (dy < -0.5 ? -17 : 18);
      var count = s('text', cAttrs, a); count.setAttribute('class', 'star-count'); count.setAttribute('display', 'none'); count.textContent = sec.count;
      return a;
    });

    // The name of a subject shows when the pointer rests on its constellation (or it has focus), and in the caption once opened.
    var ys = anchors.map(function (q) { return q[1]; });
    var title = s('text', { 'class': 'const-title', x: 0, y: 0, opacity: 0 }, g); title.textContent = meta.latin;
    var subtitle = s('text', { 'class': 'const-sub', x: 0, y: 0, opacity: 0 }, g); subtitle.textContent = sub.name;

    return { slug: sub.slug, name: sub.name, latin: meta.latin, g: g, stars: stars, index: index, sections: list, title: title, subtitle: subtitle, minY: Math.min.apply(null, ys), maxY: Math.max.apply(null, ys) };
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
      var lower = it.slot[1] > L.centre[1] - 60;   // the name goes on the side facing the middle of the map, clear of the page edge
      var ty = lower ? it.minY - 70 : it.maxY + 66;
      it.title.setAttribute('y', ty);
      it.subtitle.setAttribute('y', ty + 26);
    });
    guides.forEach(function (gl) {
      var a = L.slots[gl.a], b = L.slots[gl.b];
      gl.el.setAttribute('x1', a[0]); gl.el.setAttribute('y1', a[1]); gl.el.setAttribute('x2', b[0]); gl.el.setAttribute('y2', b[1]);
    });
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
    svg.style.setProperty('--u', (b.w / px).toFixed(4));
    svg.style.setProperty('--tk', b.w / b.h < 0.85 ? '0.7' : '1');   // text scale on a portrait screen   // user units per CSS pixel: keeps text at a readable size
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
    stage.classList.toggle('has-selection', !!selected);
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
      caption.style.setProperty('--c', 'var(--c-' + META[it.slug].color + ')');
      caption.style.setProperty('--ct', 'var(--ct-' + META[it.slug].color + ')');
      caption.appendChild(h('h2', '', it.latin));
      caption.appendChild(h('p', '', it.name + ' · ' + it.sections.length + ' areas · hover or tap a star for its name · Esc goes back'));
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
    prev.stars.forEach(function (x) { x.classList.remove('is-shown'); });
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

    var defs = s('defs', null, svg);
    Object.keys(META).forEach(function (k) {
      var color = META[k].color;
      var grad = s('radialGradient', { id: 'flare-' + color }, defs);
      var s0 = s('stop', { offset: '0', style: 'stop-color: var(--c-' + color + '); stop-opacity: 0.55' }, grad); void s0;
      s('stop', { offset: '0.35', style: 'stop-color: var(--c-' + color + '); stop-opacity: 0.16' }, grad);
      s('stop', { offset: '1', style: 'stop-color: var(--c-' + color + '); stop-opacity: 0' }, grad);
    });
    var rs = seeded(20260511);   // the far sky: three sizes, three tints, a few twinkling, a few bright with spikes
    var tints = ['t-w', 't-w', 't-w', 't-c', 't-a'];
    for (var bs = 0; bs < 420; bs++) {
      var bx = Math.round(rs() * 2500 - 300), by = Math.round(rs() * 3500 - 300), pk = rs();
      var size = pk < 0.72 ? 's1' : pk < 0.93 ? 's2' : 's3';
      var bd = s('circle', { 'class': 'dust far ' + size + ' ' + tints[Math.floor(rs() * tints.length)] + (rs() < 0.3 ? ' tw' : ''), cx: bx, cy: by, r: 1 }, svg);
      bd.style.setProperty('--d', (rs() * 7).toFixed(2) + 's');
    }
    for (var sp = 0; sp < 26; sp++) {
      var holder = s('g', { transform: 'translate(' + Math.round(rs() * 2500 - 300) + ' ' + Math.round(rs() * 3500 - 300) + ')' }, svg);
      var spark = s('path', { 'class': 'far-spark ' + tints[Math.floor(rs() * tints.length)], d: 'M0 -9 L1.4 -1.4 L9 0 L1.4 1.4 L0 9 L-1.4 1.4 L-9 0 L-1.4 -1.4Z' }, holder);
      spark.style.setProperty('--d', (rs() * 6).toFixed(2) + 's');
      spark.style.setProperty('--k', (0.5 + rs() * 0.7).toFixed(2));
    }
    var guideLayer = s('g', { 'aria-hidden': 'true' }, svg);
    GUIDES.forEach(function (pair) { guides.push({ a: pair[0], b: pair[1], el: s('line', { 'class': 'guide-line' }, guideLayer) }); });

    ORDER.forEach(function (slug, i) {
      if (!subjects[slug] || !META[slug]) return;
      var it = buildConstellation(subjects[slug], i);
      items.push(it);
      svg.appendChild(it.g);
    });

    applyLayout();
    renderState(false);
    built = true;
    moveCamera(true);

    // Clicks: a constellation selects (a star of a closed one must not navigate), empty sky goes back.
    var lastPointer = 'mouse';
    svg.addEventListener('pointerdown', function (event) { lastPointer = event.pointerType || 'mouse'; });
    svg.addEventListener('click', function (event) {
      var star = event.target.closest && event.target.closest('.star');
      if (star && lastPointer === 'touch' && !star.classList.contains('is-shown')) {   // first tap: show the name, second: go
        event.preventDefault();
        items.forEach(function (it) { it.stars.forEach(function (x) { x.classList.remove('is-shown'); }); });
        star.classList.add('is-shown');
        return;
      }
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
