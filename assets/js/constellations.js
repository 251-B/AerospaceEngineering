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

  var view = read(VIEW_KEY) === 'classic' && !/[?&]intro=1/.test(location.search) ? 'classic' : 'constellations';   // ?intro=1 also brings the stellar view back
  var palette = findPalette(read(PALETTE_KEY)) || PALETTES[0];
  root.setAttribute('data-home-view', view);
  root.setAttribute('data-sky-palette', palette.id);

  // The welcome screen (assets/js/sky-intro.js): once per browser session, only in the stellar view.
  // ?intro=1 shows it again, ?intro=0 never.
  var introSeen = false;
  try { introSeen = sessionStorage.getItem('ae_intro') === 'seen'; } catch (e) { /* storage blocked: show it every time */ }
  if (view === 'constellations' && !/[?&]intro=0/.test(location.search) && (/[?&]intro=1/.test(location.search) || !introSeen)) {
    root.setAttribute('data-intro', 'on');
  }

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
  // An open constellation keeps plain four-point sparkles at its vertices; the satellite label says what each star is.
  var SPARKLE = starPath(4, 30, 0.2, 0);

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

  /* Real constellations, drawn from memory of the sky and tilted a little: Delphinus (the dolphin) for the
     fluids, Cygnus (the Northern Cross) for the crystal lattice of the materials, Ursa Major (the Big Dipper)
     for mechanics, Orion for maths and Leo for management. `sc` scales a figure, `rot` turns it; `use` says
     which anchors take a star when the subject has fewer areas than anchors (the others stay as faint stars
     of the figure); `extra` are faint companion stars [x, y, anchor they hang from]. */
  var META = {
    'fluid-mechanics': {   // Delphinus: the small kite, its tail and its head
      latin: 'Stella Fluidorum', color: 'fluid', rot: -18, sc: 1.75,
      anchors: [[-45, -30], [5, -58], [58, -12], [2, 16], [112, 42], [-36, 108]],
      edges: [[0, 1], [1, 2], [2, 3], [3, 0], [2, 4], [3, 5]],
      use: { 4: [0, 1, 2, 3] },
      extra: [[-100, -70, 0], [80, -80, 1], [150, -10, 2], [60, 90, 4], [-90, 60, 5], [40, 160, 5]],
      flow: []
    },
    'aerospace-materials-1': {   // Cygnus: the Northern Cross
      latin: 'Stella Materiae', color: 'materials', rot: 20, sc: 1.05,
      anchors: [[0, -150], [0, -6], [0, 150], [-105, -40], [112, -12], [-48, 72]],
      edges: [[0, 1], [1, 2], [3, 1], [1, 4], [1, 5]],
      use: {},
      extra: [[-150, -120, 3], [60, -110, 0], [160, 40, 4], [90, 130, 2], [-110, 130, 5], [-60, -60, 1]],
      flow: []
    },
    'engineering-mechanics': {   // Ursa Major: the Big Dipper and the pointer to the pole star
      latin: 'Stella Mechanicae', color: 'mechanics', rot: -8, sc: 1.2,
      anchors: [[-215, -22], [-148, -55], [-80, -46], [-18, -20], [-6, 52], [112, 64], [124, -8]],
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 3]],
      use: {},
      extra: [[205, -140, 6], [-170, 70, 0], [40, 140, 4], [-60, -110, 2], [190, 40, 5], [90, -90, 6]],
      flow: []
    },
    'advanced-maths': {   // Orion: shoulders, belt, feet
      latin: 'Stella Matheseos', color: 'maths', rot: 8, sc: 1.3,
      anchors: [[-62, -128], [62, -122], [32, -8], [0, 0], [-32, 6], [-50, 124], [72, 118]],
      edges: [[0, 1], [0, 4], [1, 2], [4, 3], [3, 2], [4, 5], [2, 6]],
      use: {},
      extra: [[0, -170, 0], [-110, -70, 0], [120, -60, 1], [150, 60, 2], [-120, 90, 5], [20, 175, 6], [-20, 50, 3]],
      flow: []
    },
    'business-management': {   // Leo: the Sickle and the triangle of the hindquarters
      latin: 'Stella Oeconomiae', color: 'business', rot: -4, sc: 1.2,
      anchors: [[-170, -128], [-128, -124], [-96, -72], [-104, -14], [-138, 38], [-128, 98], [42, -30], [172, 12], [52, 58]],
      edges: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [3, 6], [6, 7], [7, 8], [8, 6], [8, 5]],
      use: { 6: [1, 2, 3, 5, 6, 7] },
      extra: [[-200, -60, 3], [-60, 130, 5], [110, -70, 6], [150, 90, 7], [-20, 30, 3], [10, 120, 8]],
      flow: []
    }
  };
  var ORDER = ['fluid-mechanics', 'aerospace-materials-1', 'engineering-mechanics', 'advanced-maths', 'business-management'];

  // Main areas of a subject, in this order. Labels follow the brief; keys come from nav.json.
  // short + tag: the two lines of the satellite label (tag stands in when the counter is missing or too long).
  var SECTIONS = [
    { key: 'theory',  label: 'Theory',                 short: 'Theory',        tag: 'Notes',     icon: 'i-theory' },
    { key: 'problems', label: 'Solved Problems',        short: 'Solved',        tag: 'Worked',    icon: 'i-problems' },
    { key: 'extra',   label: 'Extra Problems',         short: 'Extra',         tag: 'Practice',  icon: 'i-extra' },
    { key: 'formula', label: 'Formula Sheet',          short: 'Formula sheet', tag: 'Reference', icon: 'i-formula' },
    { key: 'sim',     label: 'Exam Simulator',         short: 'Simulator',     tag: 'Test mode', icon: 'i-sim' },
    { key: 'pdfs',    label: 'Theory & exercise PDFs', short: 'PDFs',          tag: 'Docs',      icon: 'i-pdf' },
    { key: 'exams',   label: 'Exams',                  short: 'Exams',         tag: 'Archive',   icon: 'i-exams' }
  ];
  function tagOf(sec) {
    if (/soon/i.test(sec.count)) return 'Coming soon';
    return sec.count && sec.count.length <= 18 ? sec.count : sec.tag;   // the real counter whenever it fits
  }
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
  var LAND = { box: [1900, 1150], centre: [950, 575], slots: [[390, 310, 1.05], [930, 540, 0.92], [1490, 330, 1.1], [520, 850, 0.95], [1320, 860, 0.9]] };   // [x, y, scale]: scattered over the whole sky, one near the middle
  var PORT_T = { box: [1100, 2200], centre: [550, 1100], slots: [[300, 270, 1.0], [790, 670, 0.9], [390, 1100, 1.02], [750, 1480, 0.95], [380, 1900, 1.0]] };   // tablet portrait and landscape phones: a loose zigzag, scrolled
  var PORT_S = { box: [680, 3000], centre: [340, 1500], slots: [[270, 340, 1.0], [350, 900, 0.95], [392, 1490, 1.0], [350, 2060, 1.0], [340, 2640, 0.9]] };       // phones: one loose column, scrolled
  var GUIDES = [[0, 1], [1, 2], [0, 3], [3, 4], [2, 4], [1, 3]];

  var ZOOM_H = 480;          // height of the camera box on a constellation (user units)
  var ZOOM_BW = [700, 820, 620];  // minimum width of that box: landscape, tablet portrait, phone

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
      return { key: sec.key, label: sec.label, short: sec.short, tag: sec.tag, icon: sec.icon, href: found[sec.key], count: counterFor(sub.slug, found[sec.key]) };
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
    var sc = meta.sc || 1;
    function place(list) { return rotate(list.map(function (q) { return [q[0] * sc, q[1] * sc]; }), meta.rot); }
    var anchors = place(meta.anchors);
    var n = list.length;
    var pick = meta.use[n];
    if (!pick) { pick = []; for (var q = 0; q < n; q++) pick.push(n === anchors.length ? q : Math.round(q * (anchors.length - 1) / Math.max(1, n - 1))); }

    s('circle', { 'class': 'const-hit', cx: 0, cy: 0, r: 235 }, g);

    // flowing guide curves of the figure, faint and dashed
    meta.flow.forEach(function (line) {
      var pts = place(line), d = 'M' + pts[0][0] + ' ' + pts[0][1];
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
      if (lit) {   // a small light that runs along the line, again and again
        var len = Math.round(Math.sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])));
        var flow = s('line', { 'class': 'const-flow', x1: a[0], y1: a[1], x2: b[0], y2: b[1], 'stroke-dasharray': '16 ' + len }, g);
        flow.style.setProperty('--fl', len + 'px');
        flow.style.setProperty('--fd', (-rnd() * 8).toFixed(2) + 's');
        flow.style.setProperty('--fs', (8 + rnd() * 6).toFixed(2) + 's');
      }
    });
    // faint extra stars round the figure, each tied to one of its stars by a thin dotted line
    var ex = place((meta.extra || []).map(function (e) { return [e[0], e[1]]; }));
    (meta.extra || []).forEach(function (e, i) {
      var q = ex[i], base = anchors[e[2]];
      s('line', { 'class': 'const-extra-link', x1: base[0], y1: base[1], x2: q[0], y2: q[1] }, g);
      var xd = s('path', { 'class': 'const-extra', d: starPath(4, 4.5 + (i % 3), 0.3, 0), transform: 'translate(' + q[0] + ' ' + q[1] + ')' }, g);
      xd.style.setProperty('--sd', (-rnd() * 5).toFixed(2) + 's');
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
      a.style.setProperty('--sd', (-rnd() * 5).toFixed(2) + 's');
      var body = s('g', { 'class': 'star-body' }, a);
      s('circle', { 'class': 'star-hit', r: 26 }, body);
      s('circle', { 'class': 'star-flare', r: 34, fill: 'url(#flare-' + meta.color + ')' }, body);
      s('path', { 'class': 'star-dot', d: starPath(4, 9.5, 0.26, 0) }, body);   // every star is the same small sparkle in the panorama
      s('path', { 'class': 'star-glyph', d: SPARKLE }, body);   // a brighter sparkle when the constellation is open
      s('circle', { 'class': 'star-core', r: 3.4 }, body);
      // The satellite label prefers the free side of the star: away from the lines that reach it and from the figure.
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
      // HUD satellite: a 45-degree leader with a short horizontal run, a ring with the area icon, name and counter.
      // Inside the same <a>, so the whole label opens the area. Positions are set by layoutHud() once the camera is known.
      var sat = s('g', { 'class': 'star-sat', 'aria-hidden': 'true' }, a);
      var tag = tagOf(sec);
      a._hud = {
        ai: ai, p: p, dx: dx, dy: dy, name: sec.short, tag: tag,
        hit: s('rect', { 'class': 'sat-hit' }, sat),
        leader: s('path', { 'class': 'sat-leader', pathLength: 1 }, sat),
        ring: s('circle', { 'class': 'sat-ring' }, sat),
        icon: s('use', { 'class': 'sat-icon', href: '#' + sec.icon }, sat),
        nm: s('text', { 'class': 'sat-name' }, sat),
        tg: s('text', { 'class': 'sat-tag' }, sat)
      };
      a._hud.nm.textContent = sec.short;
      a._hud.tg.textContent = tag;
      return a;
    });

    // The name of a subject shows when the pointer rests on its constellation (or it has focus), and in the caption once opened.
    var ys = anchors.map(function (q) { return q[1]; });
    var title = s('text', { 'class': 'const-title', x: 0, y: 0, opacity: 0 }, g); title.textContent = meta.latin;
    var subtitle = s('text', { 'class': 'const-sub', x: 0, y: 0, opacity: 0 }, g); subtitle.textContent = sub.name;

    // the whole figure drifts a few units, slowly and out of step with the others
    var float = s('g', { 'class': 'const-float' });
    while (g.firstChild) float.appendChild(g.firstChild);
    var sway = s('g', { 'class': 'const-sway' });   // two slow motions, one on top of the other, so the figure floats instead of sliding to and fro
    sway.appendChild(float);
    g.appendChild(sway);
    sway.style.setProperty('--sx', (9 + rnd() * 9).toFixed(1) + 'px');
    sway.style.setProperty('--sdur2', (8 + rnd() * 5).toFixed(1) + 's');
    sway.style.setProperty('--sdel2', (-rnd() * 10).toFixed(1) + 's');
        float.style.setProperty('--fr', (0.8 + rnd() * 1.6).toFixed(2) + 'deg');
    float.style.setProperty('--fy', (11 + rnd() * 9).toFixed(1) + 'px');
    float.style.setProperty('--fdur', (5.5 + rnd() * 3).toFixed(1) + 's');
    float.style.setProperty('--fdel', (-rnd() * 14).toFixed(1) + 's');
    float.style.setProperty('--bd', (12 + rnd() * 9).toFixed(1) + 's');
    float.style.setProperty('--bdel', (-rnd() * 9).toFixed(1) + 's');

    var allX = anchors.concat(ex).map(function (q) { return q[0]; }), allY = anchors.concat(ex).map(function (q) { return q[1]; });
    return { slug: sub.slug, name: sub.name, latin: meta.latin, g: g, stars: stars, anchors: anchors, edges: meta.edges, index: index, sections: list, title: title, subtitle: subtitle, minY: Math.min.apply(null, ys), maxY: Math.max.apply(null, ys), minX: Math.min.apply(null, anchors.map(function (q) { return q[0]; })), maxX: Math.max.apply(null, anchors.map(function (q) { return q[0]; })),
      // bounds of the whole figure, companions included: the camera keeps all of it away from the window edge
      bx0: Math.min.apply(null, allX), bx1: Math.max.apply(null, allX), by0: Math.min.apply(null, allY), by1: Math.max.apply(null, allY) };
  }

  // Phones, tablets held upright and phones on their side get a taller map that scrolls, so the figures stay big
  // and no text is squeezed; computers and landscape tablets fit the whole sky in the window.
  function isCompact() {
    var r = stage.getBoundingClientRect();
    return r.width < 900 && (r.width < 600 || r.width / Math.max(1, r.height) < 0.85 || r.height < 520);
  }

  function currentLayout() {
    var r = stage.getBoundingClientRect();
    if (!isCompact()) return LAND;
    return r.width < 600 ? PORT_S : PORT_T;
  }

  var lastLayout = null, farLayer = null, shootLayer = null;

  // The far sky is drawn for the layout in use (its area decides how many stars), a margin wide all around.
  function buildFarSky(L) {
    if (!farLayer) return;
    while (farLayer.firstChild) farLayer.removeChild(farLayer.firstChild);
    var x0 = -600, y0 = -600, w = L.box[0] + 1200, hgt = L.box[1] + 1200;
    var rs = seeded(20260511), tints = ['t-w', 't-w', 't-w', 't-c', 't-a'];
    var n = Math.min(800, Math.round(w * hgt / 7500));
    for (var i = 0; i < n; i++) {
      var pk = rs(), size = pk < 0.72 ? 's1' : pk < 0.93 ? 's2' : 's3';
      var bd = s('circle', { 'class': 'dust far ' + size + ' ' + tints[Math.floor(rs() * tints.length)] + (rs() < 0.28 ? ' tw' : ''), cx: Math.round(x0 + rs() * w), cy: Math.round(y0 + rs() * hgt), r: 1 }, farLayer);
      bd.style.setProperty('--d', (rs() * 7).toFixed(2) + 's');
    }
    var sparks = Math.round(n / 42);
    farLayer.setAttribute('class', 'far-layer');
    // shooting stars: three, each on its own long cycle, crossing a different part of the map
    while (shootLayer && shootLayer.firstChild) shootLayer.removeChild(shootLayer.firstChild);
    for (var q = 0; shootLayer && q < 5; q++) {
      var holder2 = s('g', { transform: 'translate(' + Math.round(L.box[0] * (0.1 + 0.17 * q + rs() * 0.12)) + ' ' + Math.round(L.box[1] * (0.04 + 0.5 * rs())) + ')' }, shootLayer);
      var streak = s('line', { 'class': 'shoot', x1: 0, y1: 0, x2: -110, y2: -60 }, holder2);
      streak.style.setProperty('--sdur', (7 + q * 2.5 + rs() * 3).toFixed(1) + 's');
      streak.style.setProperty('--sdel', (-rs() * 20).toFixed(1) + 's');
    }
    for (var k = 0; k < sparks; k++) {
      var holder = s('g', { transform: 'translate(' + Math.round(x0 + rs() * w) + ' ' + Math.round(y0 + rs() * hgt) + ')' }, farLayer);
      var spark = s('path', { 'class': 'far-spark ' + tints[Math.floor(rs() * tints.length)], d: 'M0 -9 L1.4 -1.4 L9 0 L1.4 1.4 L0 9 L-1.4 1.4 L-9 0 L-1.4 -1.4Z' }, holder);
      spark.style.setProperty('--d', (rs() * 6).toFixed(2) + 's');
      spark.style.setProperty('--k', (0.28 + rs() * 0.34).toFixed(2));
    }
  }

  // The map is as tall as its layout asks when it scrolls, and as tall as the window when a constellation is open.
  function sizeSvg(L) {
    var compact = isCompact();
    stage.classList.toggle('is-compact', compact);
    svg.classList.toggle('is-compact', compact);
    svg.style.height = compact && !selected ? Math.round(stage.clientWidth * L.box[1] / L.box[0]) + 'px' : '';
  }

  function applyLayout() {
    var L = currentLayout();
    if (L !== lastLayout) { lastLayout = L; buildFarSky(L); }
    sizeSvg(L);
    items.forEach(function (it) {
      it.slot = L.slots[it.index];
      it.g.setAttribute('transform', 'translate(' + it.slot[0] + ' ' + it.slot[1] + ') scale(' + (it.slot[2] || 1) + ')');
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
     HUD satellites of the open constellation: sizes are screen pixels (u = user units per pixel),
     placement is a greedy search over the four diagonals and several leader lengths (plus vertical leaders on
     phones) that avoids the other labels, the stars and the lines of the figure, leaning to each star's free side.
     --------------------------------------------------------------------------------------- */
  function boxHit(a, b) { return a[0] < b[2] && b[0] < a[2] && a[1] < b[3] && b[1] < a[3]; }
  function cross(p, q, r) { return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]); }
  function segCross(a, b, c, d) {   // strict: segments that only share an end do not cross
    return cross(a, b, c) * cross(a, b, d) < 0 && cross(c, d, a) * cross(c, d, b) < 0;
  }
  function segBox(a, b, x) {
    function inside(p) { return p[0] > x[0] && p[0] < x[2] && p[1] > x[1] && p[1] < x[3]; }
    if (inside(a) || inside(b)) return true;
    var c = [[x[0], x[1]], [x[2], x[1]], [x[2], x[3]], [x[0], x[3]]];
    for (var i = 0; i < 4; i++) if (segCross(a, b, c[i], c[(i + 1) % 4])) return true;
    return false;
  }

  function layoutHud(it, u, phone) {
    var k = it.slot[2] || 1, q = u / k;   // local units per screen pixel
    var ks = isCompact() ? Math.min(1.9, Math.max(1, 15 * u / 16)) : 1;
    var R = (phone ? 13 : 16) * q, fN = (phone ? 13 : 15) * q, fT = (phone ? 10.5 : 11.5) * q;
    var gap = 6 * q, run = (phone ? 6 : 16) * q, r0 = 12 * q * ks, pad = 5 * q;
    var segs = it.edges.map(function (e) { return [it.anchors[e[0]], it.anchors[e[1]]]; });
    var boxes = [], legs = [];
    var fx0 = Math.min.apply(null, it.anchors.map(function (a) { return a[0]; })), fx1 = Math.max.apply(null, it.anchors.map(function (a) { return a[0]; }));
    function candidates(hd) {
      var out = [], tw = Math.max(hd.name.length * fN * 0.56, hd.tag.length * fT * 0.62);
      // shapes: the 45-degree leader everywhere; on phones also a vertical one (up or down, then the short run),
      // since a tall narrow screen has room above and below a figure and none beside it
      (phone ? [[true, false], [false, false], [true, true]] : [[false, false]]).forEach(function (shape) {
      var stack = shape[0], vert = shape[1];
      (vert ? [1, 1.7, 2.5, 3.4, 4.4, 5.6, 7] : phone ? [1, 1.7, 2.5, 3.4, 4.4] : [1, 1.7, 2.5, 3.4]).forEach(function (len) { [-1, 1].forEach(function (sy) { [-1, 1].forEach(function (sx) {
        var D = (phone ? 16 : 24) * q * len + r0, ex = vert ? 0 : sx * D, ey = sy * D, nx = ex + sx * (run + R), ny = ey, b;
        if (stack) {   // narrow screens: the text sits under (or over) the ring, so labels stay narrow
          var hw = Math.max(R, tw / 2), th = gap + fN + fT * 1.25;
          b = [nx - hw, sy > 0 ? ny - R : ny - R - th, nx + hw, sy > 0 ? ny + R + th : ny + R];
        } else {
          var hh = Math.max(R, fN * 1.05);
          b = sx > 0 ? [nx - R, ny - hh, nx + R + gap + tw, ny + hh] : [nx - R - gap - tw, ny - hh, nx + R, ny + hh];
        }
        var p = hd.p;
        var s0 = vert ? [0, sy * r0] : [sx * r0 * 0.7, sy * r0 * 0.7];   // the leader starts just clear of the star
        out.push({ stack: stack, vert: vert, sx: sx, sy: sy, len: len, s0: s0, ex: ex, ey: ey, nx: nx, ny: ny, tw: tw, box: [p[0] + b[0] - pad, p[1] + b[1] - pad, p[0] + b[2] + pad, p[1] + b[3] + pad],
          l1: [[p[0] + s0[0], p[1] + s0[1]], [p[0] + ex, p[1] + ey]], l2: [[p[0] + ex, p[1] + ey], [p[0] + nx - sx * R, p[1] + ny]] });
      }); }); }); });
      return out;
    }
    function score(c, hd, i) {
      var sc = -8 * (c.sx * hd.dx + c.sy * hd.dy) + (c.len - 1) * 10 + (phone && !c.stack ? 15 : 0) + (c.vert ? 6 : 0);   // side text on a phone only when stacking collides
      // narrow screens: labels sticking out sideways would leave no width for the figure (and the fit would not
      // converge), so each pixel beyond the figure's sides costs; above and below there is room
      if (phone) sc += 0.6 * (Math.max(0, fx0 - c.box[0]) + Math.max(0, c.box[2] - fx1)) / q;
      var hard = 0;
      boxes.forEach(function (b, j) { if (j !== i && b && boxHit(b, c.box)) hard += 1000; });
      legs.forEach(function (l, j) { if (j !== i && l && (segCross(l[0], l[1], c.l1[0], c.l1[1]) || segCross(l[0], l[1], c.l2[0], c.l2[1]) || segBox(l[0], l[1], c.box))) hard += 300; });
      it.anchors.forEach(function (a, j) { if (j !== hd.ai && a[0] > c.box[0] - 8 * q && a[0] < c.box[2] + 8 * q && a[1] > c.box[1] - 8 * q && a[1] < c.box[3] + 8 * q) sc += 250; });
      segs.forEach(function (sg) {
        if (segBox(sg[0], sg[1], c.box)) sc += 160;
        if (segCross(sg[0], sg[1], c.l1[0], c.l1[1]) || segCross(sg[0], sg[1], c.l2[0], c.l2[1])) sc += 90;
      });
      c.hard = hard;   // label on label or crossing leaders: only these make the camera step back
      return sc + hard;
    }
    var pick = [], clash = 0;
    for (var pass = 0; pass < 2; pass++) {   // the second pass lets early labels move out of the way of later ones
      it.stars.forEach(function (a, i) {
        var best = null, bs = Infinity;
        candidates(a._hud).forEach(function (c) { var v = score(c, a._hud, i); if (v < bs) { bs = v; best = c; } });
        if (pass) clash += best.hard;
        pick[i] = best; boxes[i] = best.box; legs[i] = best.l1;   // the diagonal; the short run lies inside the box margin
      });
    }
    var x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    it.anchors.forEach(function (a) { x0 = Math.min(x0, a[0]); x1 = Math.max(x1, a[0]); y0 = Math.min(y0, a[1]); y1 = Math.max(y1, a[1]); });
    it.stars.forEach(function (a, i) {
      var c = pick[i], hd = a._hud, p = hd.p, f = function (v) { return v.toFixed(1); };
      x0 = Math.min(x0, c.box[0]); x1 = Math.max(x1, c.box[2]); y0 = Math.min(y0, c.box[1]); y1 = Math.max(y1, c.box[3]);
      var b = c.box;
      hd.hit.setAttribute('x', f(b[0] - p[0])); hd.hit.setAttribute('y', f(b[1] - p[1]));
      hd.hit.setAttribute('width', f(b[2] - b[0])); hd.hit.setAttribute('height', f(b[3] - b[1])); hd.hit.setAttribute('rx', f(6 * q));
      hd.leader.setAttribute('d', 'M' + f(c.s0[0]) + ' ' + f(c.s0[1]) + 'L' + f(c.ex) + ' ' + f(c.ey) + 'L' + f(c.nx - c.sx * R) + ' ' + f(c.ny));
      hd.ring.setAttribute('cx', f(c.nx)); hd.ring.setAttribute('cy', f(c.ny)); hd.ring.setAttribute('r', f(R));
      var ic = R * 1.15;
      hd.icon.setAttribute('x', f(c.nx - ic / 2)); hd.icon.setAttribute('y', f(c.ny - ic / 2)); hd.icon.setAttribute('width', f(ic)); hd.icon.setAttribute('height', f(ic));
      var tx, ty, anchor;
      if (c.stack) { anchor = 'middle'; tx = c.nx; ty = c.sy > 0 ? c.ny + R + gap + fN * 0.85 : c.ny - R - gap - fT * 1.25; }
      else { anchor = c.sx > 0 ? 'start' : 'end'; tx = c.nx + c.sx * (R + gap); ty = c.ny - 1 * q; }
      [hd.nm, hd.tg].forEach(function (t, j) {
        t.setAttribute('text-anchor', anchor); t.setAttribute('x', f(tx));
        t.setAttribute('y', f(j ? ty + fT * 1.2 : ty)); t.setAttribute('font-size', f(j ? fT : fN));
      });
      if (!c.stack) { hd.nm.setAttribute('y', f(c.ny - 1.5 * q)); hd.tg.setAttribute('y', f(c.ny + fT * 1.1)); }
      a.setAttribute('data-sat', (c.sx > 0 ? 'e' : 'w') + (c.sy > 0 ? 's' : 'n'));
    });
    return { x0: it.slot[0] + x0 * k, x1: it.slot[0] + x1 * k, y0: it.slot[1] + y0 * k, y1: it.slot[1] + y1 * k, clash: clash };
  }

  /* ---------------------------------------------------------------------------------------
     Camera
     --------------------------------------------------------------------------------------- */
  function target() {
    var L = currentLayout();
    var r = stage.getBoundingClientRect();
    var compact = isCompact();
    if (compact && !selected) return { cx: L.box[0] / 2, cy: L.box[1] / 2, bw: L.box[0], bh: L.box[1], asp: L.box[0] / L.box[1] };
    var asp = r.width / Math.max(1, r.height);
    if (!selected) {   // the box holds every figure (drift and hover titles included), with a margin all round
      var x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
      items.forEach(function (q) {
        var kk = q.slot[2] || 1;
        x0 = Math.min(x0, q.slot[0] + q.bx0 * kk); x1 = Math.max(x1, q.slot[0] + q.bx1 * kk);
        y0 = Math.min(y0, q.slot[1] + q.by0 * kk); y1 = Math.max(y1, q.slot[1] + q.by1 * kk);
      });
      return { cx: (x0 + x1) / 2, cy: (y0 + y1) / 2, bw: x1 - x0 + 300, bh: y1 - y0 + 340, asp: asp };
    }
    var it = byslug(selected);
    var k = it.slot[2] || 1, phone = r.width < 600;
    // The box holds the figure and every satellite label, with screen margins for the header and back button (top),
    // the caption (bottom) and the window sides, plus the drift of the figure. Labels are sized in pixels, so the
    // box and the labels are solved together by a few fixed-point steps.
    var W = Math.max(1, r.width), Hh = Math.max(1, r.height);
    var mt = compact ? 118 : 112, mb = compact ? 112 : 132, ms = phone ? 14 : 30, drift = 8 * k;   // the open figure holds still
    // the real caption keeps the labels above it; its layout box, not its rect, since it slides in on arrival
    if (caption && caption.firstChild && caption.offsetHeight) mb = Math.max(mb, r.height - caption.offsetTop + 12);
    var bw0 = (compact ? (phone ? ZOOM_BW[2] : ZOOM_BW[1]) : ZOOM_BW[0]) * k, bh0 = (compact ? ZOOM_H + 140 : ZOOM_H) * k;
    var fitW = 1 / Math.max(0.3, 1 - 2 * ms / W), fitH = 1 / Math.max(0.3, 1 - (mt + mb) / Hh);
    function needOf(b) { return Math.max((b.x1 - b.x0 + 2 * drift) * fitW, (b.y1 - b.y0 + 2 * drift) * fitH * asp); }
    // Labels are pixel-sized, so they grow with the box. Search from the tightest view outward and keep the first box
    // that holds every label with no collision; failing that, the fitting box with the fewest collisions.
    var w = Math.max(bw0, bh0 * asp, (it.maxX - it.minX) * k * fitW, (it.maxY - it.minY) * k * fitH * asp), hh, bb, best = null;
    for (var i = 0; i < 10; i++, w *= 1.1) {   // at most about 2.5 times the tightest view
      bb = layoutHud(it, w / W, phone);
      if (needOf(bb) > w) continue;
      if (!best || bb.clash < best.clash) best = { w: w, clash: bb.clash };
      if (!bb.clash) break;
    }
    w = best ? best.w : needOf(bb);
    bb = layoutHud(it, w / W, phone);   // the labels drawn match the chosen camera
    hh = w / asp;
    var uu = w / W, free = hh - (bb.y1 - bb.y0 + 2 * drift) - (mt + mb) * uu;
    var top = bb.y0 - drift - mt * uu - Math.max(0, free) / 2;
    return { cx: (bb.x0 + bb.x1) / 2, cy: top + hh / 2, bw: w, bh: hh, asp: asp };
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
    svg.style.setProperty('--tk', '1');
    // on a touch screen the stars of an open constellation grow until the icon is at least ~20 px across
    var ks = selected && isCompact() ? Math.min(1.9, Math.max(1, 15 * (b.w / px) / 16)) : 1;
    svg.style.setProperty('--ks', ks.toFixed(3));
  }

  function reduced() { return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches; }

  function moveCamera(instant) {
    var r = stage.getBoundingClientRect();
    if (!r.width || !r.height) return;   // the map is hidden (classic view): keep the camera, setView() moves it on return
    var to = boxOf(target());
    cancelAnimationFrame(camAnim);
    if (instant || reduced() || !cam || isCompact()) { cam = to; paint(cam); return; }
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

  var savedScroll = 0;
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
      caption.appendChild(h('p', '', it.name + ' · ' + it.sections.length + ' areas · choose a star or its label · Esc goes back'));
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
    if (isCompact() && !selected) savedScroll = stage.scrollTop;
    selected = slug;
    sizeSvg(currentLayout());
    renderState(fromKeyboard ? true : false);   // first: the camera measures the new caption
    moveCamera(false);
  }

  function backToPanorama() {
    if (!selected) return;
    var prev = byslug(selected);
    selected = null;
    sizeSvg(currentLayout());
    moveCamera(false);
    renderState(prev.g);
    if (isCompact()) stage.scrollTop = savedScroll;
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
    document.dispatchEvent(new CustomEvent('ae-home-view', { detail: { view: view } }));
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
    farLayer = s('g', { 'aria-hidden': 'true' }, svg);
    shootLayer = s('g', { 'aria-hidden': 'true', 'class': 'shoot-layer' }, svg);
    var guideLayer = s('g', { 'aria-hidden': 'true' }, svg);
    GUIDES.forEach(function (pair) { guides.push({ a: pair[0], b: pair[1], el: s('line', { 'class': 'guide-line' }, guideLayer) }); });

    ORDER.forEach(function (slug, i) {
      if (!subjects[slug] || !META[slug]) return;
      var it = buildConstellation(subjects[slug], i);
      it.g.style.setProperty('--ci', String(i));
      items.push(it);
      svg.appendChild(it.g);
    });

    applyLayout();
    renderState(false);
    built = true;
    moveCamera(true);

    // Clicks: a constellation selects (a star of a closed one must not navigate), empty sky goes back.
    // a soft chime when the pointer reaches a constellation (when the sound is on), a different note for each
    var lastChime = 0, lastGroup = null;
    svg.addEventListener('pointerover', function (event) {
      if (event.pointerType === 'touch' || !window.AESkySound || !window.AESkySound.isOn()) return;
      var group = event.target.closest && event.target.closest('.const');
      if (!group || group === lastGroup) return;
      lastGroup = group;
      var now = Date.now();
      if (now - lastChime < 500) return;
      lastChime = now;
      var it = byslug(group.getAttribute('data-slug'));
      if (it) window.AESkySound.chime(it.index * 2 + 1, true);
    });
    svg.addEventListener('pointerleave', function () { lastGroup = null; });
    svg.addEventListener('click', function (event) {   // the satellite labels name every star, so one tap opens it
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

    var replay = document.getElementById('introReplay');   // plays the welcome screen again (a reload with ?intro=1)
    if (replay) replay.addEventListener('click', function () {
      try { sessionStorage.removeItem('ae_intro'); } catch (e) { /* storage blocked: the parameter is enough */ }
      location.href = location.pathname + '?intro=1';
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

    // a gentle parallax: the far sky follows the pointer a little (not on touch screens)
    stage.addEventListener('pointermove', function (event) {
      if (event.pointerType === 'touch' || reduced()) return;
      var r = stage.getBoundingClientRect();
      stage.style.setProperty('--mx', ((event.clientX - r.left) / r.width * 2 - 1).toFixed(3));
      stage.style.setProperty('--my', ((event.clientY - r.top) / r.height * 2 - 1).toFixed(3));
    });

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
