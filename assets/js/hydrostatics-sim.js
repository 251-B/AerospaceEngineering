/* Hydrostatics exercise simulators (Fluid Mechanics, Topic 5).
 *
 * Each simulator lives inside the solution of its own problem card, as <div class="hs-sim" data-sim="...">,
 * written by tools/fluids_fs/build.py from the note's "Interactive simulator" block:
 *   plane-gate      FS4  plane gate: pressure prism, centroid C, centre of pressure CP, strip dA, moment about C
 *   curved-surface  FS10 cylinder: element dF around the arc, projections F_H and the sector / triangle split of F_V
 *   buoyancy-cube   FS3  floating hollow cube with trapped air: H1, H2, p_c and the forces on the shell
 * Inline SVG redrawn on every input; no canvas, no storage. The default values reproduce the statement, and every
 * readout uses the formulas of that solution (checked in tools/fluids_fs/verify_fluid_statics.py). Colours come from
 * the page variables (assets/css/hydrostatics-sim.css), so the reading palettes and the print layout apply.
 */
(function () {
  'use strict';

  var SVGNS = 'http://www.w3.org/2000/svg';
  var RHO = 1000, G = 9.81;

  function h(tag, attrs, parent, text) {
    var e = document.createElement(tag);
    for (var k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }

  function s(tag, attrs, parent, text) {
    var e = document.createElementNS(SVGNS, tag);
    for (var k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }

  function num(v, d) {
    if (!isFinite(v)) return '–';
    return v.toFixed(d == null ? 2 : d).replace('-', '−');
  }

  function arrow(g, x1, y1, x2, y2, cls, head) {
    var a = Math.atan2(y2 - y1, x2 - x1), k = head || 9;
    var L = Math.hypot(x2 - x1, y2 - y1);
    if (L < 2) return;
    var tx = x2 - 0.6 * k * Math.cos(a), ty = y2 - 0.6 * k * Math.sin(a);
    s('line', { x1: x1, y1: y1, x2: tx, y2: ty, 'class': 'hs-line ' + cls }, g);
    var p1 = [x2 - k * Math.cos(a - 0.4), y2 - k * Math.sin(a - 0.4)];
    var p2 = [x2 - k * Math.cos(a + 0.4), y2 - k * Math.sin(a + 0.4)];
    s('path', { d: 'M' + x2 + ',' + y2 + 'L' + p1 + 'L' + p2 + 'Z', 'class': 'hs-head ' + cls }, g);
  }

  /* "F_H,L" -> F with the subscript "H,L" (SVG tspan); plain text otherwise */
  function label(g, x, y, text, anchor, cls) {
    var t = s('text', { x: x, y: y, 'text-anchor': anchor || 'middle', 'class': cls || '' }, g);
    var m = /^([^_]*)_([^ ]+)(.*)$/.exec(text);
    if (!m) { t.textContent = text; return t; }
    t.appendChild(document.createTextNode(m[1]));
    s('tspan', { 'baseline-shift': 'sub', 'font-size': '75%' }, t, m[2]);
    if (m[3]) s('tspan', { 'baseline-shift': '0' }, t, m[3]);
    return t;
  }

  /* text with "x_sub" pieces written as <sub> (sub = letters and digits, "H,L" allowed) */
  function rich(el, text) {
    var re = /_([A-Za-z0-9]+(?:,[A-Za-z0-9]+)*)/g, last = 0, m;
    while ((m = re.exec(text))) {
      el.appendChild(document.createTextNode(text.slice(last, m.index)));
      h('sub', {}, el, m[1]);
      last = re.lastIndex;
    }
    el.appendChild(document.createTextNode(text.slice(last)));
    return el;
  }

  /* ---------------------------------------------------------------- frame: title, svg, controls, readouts */
  function frame(host, title, intro, width, height) {
    host.innerHTML = '';
    host.classList.add('hs-ready');
    h('div', { 'class': 'hs-title' }, host, title);
    h('p', { 'class': 'hs-intro' }, host, intro);
    var wrap = h('div', { 'class': 'hs-figure' }, host);
    var svg = s('svg', { viewBox: '0 0 ' + width + ' ' + height, 'class': 'hs-svg', role: 'img', 'aria-label': title }, wrap);
    var body = h('div', { 'class': 'hs-panel' }, host);
    var controls = h('div', { 'class': 'hs-controls' }, body);
    var out = h('dl', { 'class': 'hs-readouts', 'aria-live': 'polite' }, body);
    return { svg: svg, controls: controls, out: out };
  }

  function slider(box, id, text, min, max, step, value, unit, digits, onInput) {
    var row = h('div', { 'class': 'hs-control' }, box);
    var lab = rich(h('label', { 'for': id }, row), text + ' ');
    var val = h('output', { 'for': id }, lab);
    var inp = h('input', { type: 'range', id: id, min: min, max: max, step: step, value: value }, row);
    function show() { val.textContent = num(+inp.value, digits) + (unit ? ' ' + unit : ''); }
    inp.addEventListener('input', function () { show(); onInput(); });
    show();
    return {
      get: function () { return +inp.value; },
      set: function (v) { inp.value = v; show(); }
    };
  }

  function select(box, id, text, options, value, onInput) {
    var row = h('div', { 'class': 'hs-control' }, box);
    h('label', { 'for': id }, row, text);
    var sel = h('select', { id: id }, row);
    options.forEach(function (o) {
      var op = h('option', { value: o[0] }, sel, o[1]);
      if (o[0] === value) op.selected = true;
    });
    sel.addEventListener('change', onInput);
    return { get: function () { return sel.value; } };
  }

  function readouts(dl, rows) {
    dl.innerHTML = '';
    rows.forEach(function (r) {
      rich(h('dt', {}, dl), r[0]);
      rich(h('dd', r[2] ? { 'class': 'hs-note' } : {}, dl), r[1]);
    });
  }

  var uid = 0;

  /* ================================================================ 1. plane gate (FS4) */
  var SHAPES = {
    square: { name: 'square', A: function (L) { return L * L; }, uC: function (L) { return L / 2; },
              I: function (L) { return Math.pow(L, 4) / 12; }, w: function (u, L) { return L; } },
    triangle: { name: 'triangle', A: function (L) { return L * L / 2; }, uC: function (L) { return L / 3; },
                I: function (L) { return Math.pow(L, 4) / 36; }, w: function (u, L) { return L * (1 - u / L); } },
    circle: { name: 'circle', A: function (L) { return Math.PI * L * L / 4; }, uC: function (L) { return L / 2; },
              I: function (L) { return Math.PI * Math.pow(L, 4) / 64; },
              w: function (u, L) { var r = L / 2, d = u - r; return 2 * Math.sqrt(Math.max(r * r - d * d, 0)); } }
  };

  function planeGate(host) {
    var n = ++uid;
    var f = frame(host, 'Simulator: plane gate, pressure prism and centre of pressure',
      'Default: the square valve of FS4 (vertical, side L = 1 m, water depth h = 3 m). The gate is a plate of size L along ' +
      'its own plane, inclined at θ to the free surface, with its lower edge at the depth h. The strip slider moves the ' +
      'element dA = w(s) ds along the gate.', 720, 340);
    var c = f.controls;
    var cH = slider(c, 'hs' + n + 'h', 'Depth of the lower edge h:', 0.2, 10, 0.1, 3, 'm', 1, draw);
    var cT = slider(c, 'hs' + n + 't', 'Inclination θ:', 15, 90, 1, 90, '°', 0, draw);
    var cL = slider(c, 'hs' + n + 'l', 'Size L:', 0.2, 3, 0.1, 1, 'm', 1, draw);
    var cS = select(c, 'hs' + n + 's', 'Shape:', [['square', 'Square L × L'], ['triangle', 'Triangle, base L at the bottom'],
      ['circle', 'Circle of diameter L']], 'square', draw);
    var cU = slider(c, 'hs' + n + 'u', 'Strip position (from the lower edge):', 0, 100, 1, 30, '%', 0, draw);

    function draw() {
      var th = cT.get() * Math.PI / 180, sn = Math.sin(th), cs = Math.cos(th);
      var L = cL.get(), shape = SHAPES[cS.get()], hb = cH.get(), raised = false;
      if (hb < L * sn) { hb = L * sn; cH.set(Math.ceil(hb * 10) / 10); hb = cH.get(); raised = true; }
      var sb = hb / sn, st = sb - L;                          // s of the lower and the upper edge
      var A = shape.A(L), uC = shape.uC(L), I = shape.I(L);
      var sC = sb - uC, e = I / (sC * A), sCP = sC + e;
      var F = RHO * G * sn * sC * A, MC = RHO * G * sn * I;
      var u = cU.get() / 100 * L, su = sb - u, wu = shape.w(u, L);
      var svg = f.svg;
      while (svg.firstChild) svg.removeChild(svg.firstChild);

      /* side view */
      var g = s('g', {}, svg);
      var x0 = 100, y0 = 46;
      var k = Math.min(250 / Math.max(hb, 0.1), 230 / Math.max(sb * cs + 0.2, 0.2), 140);
      var P = function (ss) { return [x0 + ss * cs * k, y0 + ss * sn * k]; };
      var up = [sn, -cs];                                     // normal towards the water (screen)
      var Pb = P(sb), Pt = P(st);
      s('path', { d: 'M' + x0 + ',' + y0 + 'L350,' + y0 + 'L350,' + (Pb[1] + 4) + 'L' + Pb[0] + ',' + (Pb[1] + 4) + 'Z', 'class': 'hs-water' }, g);
      s('line', { x1: 20, y1: y0, x2: 350, y2: y0, 'class': 'hs-line hs-surface' }, g);
      label(g, 340, y0 - 8, 'pₐ', 'end', 'hs-t');
      s('line', { x1: x0, y1: y0, x2: Pt[0], y2: Pt[1], 'class': 'hs-line hs-wall' }, g);
      s('line', { x1: Pt[0], y1: Pt[1], x2: Pb[0], y2: Pb[1], 'class': 'hs-line hs-gate' }, g);
      var kp = 70 / sb, i, ss, a, q;
      for (i = 0; i <= 8; i++) {
        ss = st + (sb - st) * i / 8;
        q = P(ss);
        a = [q[0] + up[0] * kp * ss, q[1] + up[1] * kp * ss];
        arrow(g, a[0], a[1], q[0], q[1], 'hs-blue', 6);
      }
      var qa = P(st), qb = P(sb);
      s('path', { d: 'M' + qa + 'L' + [qa[0] + up[0] * kp * st, qa[1] + up[1] * kp * st] + 'L' +
        [qb[0] + up[0] * kp * sb, qb[1] + up[1] * kp * sb] + 'L' + qb, 'class': 'hs-line hs-blue hs-thin' }, g);
      var pc = P(sC), pp = P(sCP);
      s('circle', { cx: pc[0], cy: pc[1], r: 4, 'class': 'hs-dot' }, g);
      s('circle', { cx: pp[0], cy: pp[1], r: 4, 'class': 'hs-dot hs-acc' }, g);
      arrow(g, pp[0] - up[0] * 4, pp[1] - up[1] * 4, pp[0] - up[0] * 70, pp[1] - up[1] * 70, 'hs-acc', 11);
      label(g, pp[0] - up[0] * 82, pp[1] - up[1] * 82 + 5, 'F', 'middle', 'hs-t hs-big');
      label(g, pc[0] - up[0] * 30 - cs * 16, pc[1] - up[1] * 30 - sn * 16 + 4, 'C', 'middle', 'hs-t');
      label(g, pp[0] - up[0] * 30 + cs * 20, pp[1] - up[1] * 30 + sn * 20 + 6, 'CP', 'middle', 'hs-t');
      if (cT.get() < 90) {
        var r = 30;
        s('path', { d: 'M' + (x0 + r) + ',' + y0 + 'A' + r + ',' + r + ' 0 0 1 ' + (x0 + r * cs) + ',' + (y0 + r * sn), 'class': 'hs-line hs-thin' }, g);
        label(g, x0 + 38 * Math.cos(th / 2) + 4, y0 + 38 * Math.sin(th / 2) + 6, 'θ', 'start', 'hs-t');
      }
      var pu = P(su);
      s('circle', { cx: pu[0], cy: pu[1], r: 3.5, 'class': 'hs-dot hs-green' }, g);
      label(g, 190, 330, 'side view', 'middle', 'hs-t hs-small');

      /* front view, folded down */
      var gf = s('g', {}, svg);
      var cx = 560, yt = 60, yb2 = 280, sc = (yb2 - yt) / L;
      var Y = function (uu) { return yb2 - uu * sc; };
      var pts = [], j, uu, ww;
      for (j = 0; j <= 60; j++) { uu = L * j / 60; ww = shape.w(uu, L) * sc / 2; pts.push([cx - ww, Y(uu)]); }
      for (j = 60; j >= 0; j--) { uu = L * j / 60; ww = shape.w(uu, L) * sc / 2; pts.push([cx + ww, Y(uu)]); }
      s('polygon', { points: pts.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' '), 'class': 'hs-plate' }, gf);
      var ws = Math.max(wu * sc, 2);
      s('rect', { x: cx - ws / 2, y: Y(u) - 4, width: ws, height: 8, 'class': 'hs-strip' }, gf);
      s('line', { x1: cx - 120, y1: Y(uC), x2: cx + 120, y2: Y(uC), 'class': 'hs-line hs-axis' }, gf);
      s('circle', { cx: cx, cy: Y(uC), r: 4, 'class': 'hs-dot' }, gf);
      s('circle', { cx: cx, cy: Y(uC) + e * sc, r: 4, 'class': 'hs-dot hs-acc' }, gf);
      label(gf, cx - 128, Y(uC) + 5, 'C', 'end', 'hs-t');
      label(gf, cx + 14, Y(uC) + e * sc + 16, 'CP', 'start', 'hs-t');
      label(gf, cx + ws / 2 + 10, Y(u) + 5, 'dA', 'start', 'hs-t');
      label(gf, cx, 312, 'front view, scaled to fit the panel', 'middle', 'hs-t hs-small');
      label(gf, cx, 330, 'C on the dashed axis, CP below it by e', 'middle', 'hs-t hs-small');

      var rows = [
        ['Area A', num(A, 3) + ' m²'],
        ['Centroid: s_C, depth', num(sC, 3) + ' m, ' + num(sC * sn, 3) + ' m'],
        ['F = ρg sinθ s_C A', num(F / 1000, 2) + ' kN (normal to the gate)'],
        ['e = s_CP − s_C = I_C/(s_C A)', num(e * 1000, 1) + ' mm'],
        ['Moment about the centroidal axis ρg sinθ I_C', num(MC / 1000, 3) + ' kN m (independent of h)'],
        ['Strip: s, gauge pressure', num(su, 3) + ' m, ' + num(RHO * G * su * sn / 1000, 2) + ' kPa'],
        ['Strip: w(s)', num(wu, 3) + ' m']
      ];
      if (cS.get() === 'square') rows.push(['F_A at the lower edge (FS4, arm L/2)', num(MC / (L / 2) / 1000, 3) + ' kN = ρgL³/6 when θ = 90°']);
      if (raised) rows.push(['Note', 'h was raised to L sinθ so that the gate stays under water', true]);
      readouts(f.out, rows);
    }
    draw();
  }

  /* ================================================================ 2. curved surface (FS10) */
  function curvedSurface(host) {
    var n = ++uid;
    var f = frame(host, 'Simulator: cylinder, integration and projections',
      'Default: the cylinder of FS10 (R = 0.5 m, L = 5 m, water up to the top on the left and up to the centre on the right). ' +
      'Integration view: the element dF at the angle θ from the upward vertical on the left half. Projection view: F_H on ' +
      'the vertical projections and F_V as the weight of the displaced water, a circular sector plus or minus a right triangle.',
      720, 340);
    var c = f.controls;
    var cM = select(c, 'hs' + n + 'm', 'View:', [['int', 'Integration: element dF'], ['proj', 'Projections: F_H and F_V']], 'int', draw);
    var cR = slider(c, 'hs' + n + 'r', 'Radius R:', 0.1, 1.5, 0.05, 0.5, 'm', 2, draw);
    var cL = slider(c, 'hs' + n + 'l', 'Length L:', 1, 10, 0.5, 5, 'm', 1, draw);
    var cA = slider(c, 'hs' + n + 'a', 'Left level h_L / 2R:', 0, 1, 0.01, 1, '', 2, draw);
    var cB = slider(c, 'hs' + n + 'b', 'Right level h_R / 2R:', 0, 1, 0.01, 0.5, '', 2, draw);
    var cT = slider(c, 'hs' + n + 't', 'Element angle θ (left half):', 0, 180, 1, 55, '°', 0, draw);

    function area(R, hh) {                                      // half-disc area below the level hh
      var beta = Math.acos(Math.max(-1, Math.min(1, (R - hh) / R)));
      return { beta: beta, sector: R * R * beta / 2, tri: (R - hh) * R * Math.sin(beta) / 2,
               A: R * R * beta / 2 - (R - hh) * R * Math.sin(beta) / 2 };
    }

    function draw() {
      var R = cR.get(), L = cL.get(), hL = cA.get() * 2 * R, hR = cB.get() * 2 * R, th = cT.get() * Math.PI / 180;
      var proj = cM.get() === 'proj';
      var svg = f.svg;
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      var g = s('g', {}, svg);
      var Rp = 115, sc = Rp / R, cx = 360, fl = 300, cy = fl - Rp;
      var yL = fl - hL * sc, yR = fl - hR * sc;
      s('rect', { x: 40, y: yL, width: cx - 40, height: fl - yL, 'class': 'hs-water' }, g);
      s('rect', { x: cx, y: yR, width: 680 - cx, height: fl - yR, 'class': 'hs-water' }, g);
      if (hL > 0) s('line', { x1: 40, y1: yL, x2: cx, y2: yL, 'class': 'hs-line hs-surface' }, g);
      if (hR > 0) s('line', { x1: cx, y1: yR, x2: 680, y2: yR, 'class': 'hs-line hs-surface' }, g);
      s('circle', { cx: cx, cy: cy, r: Rp, 'class': 'hs-body' }, g);
      s('line', { x1: 30, y1: fl, x2: 690, y2: fl, 'class': 'hs-line hs-floor' }, g);
      s('circle', { cx: cx, cy: cy, r: 3, 'class': 'hs-dot' }, g);
      label(g, cx + 8, cy - 6, 'C', 'start', 'hs-t');

      var aL = area(R, hL), aR = area(R, hR);
      var FHL = RHO * G * L * hL * hL / 2, FHR = RHO * G * L * hR * hR / 2;
      var FVL = RHO * G * L * aL.A, FVR = RHO * G * L * aR.A;
      var rows;

      if (!proj) {
        /* pressure on both wetted arcs, then the chosen element */
        var t, x, y, d, len, i;
        for (i = 0; i <= 36; i++) {
          t = Math.PI * i / 36;
          [[-1, hL], [1, hR]].forEach(function (side) {
            x = cx + side[0] * Rp * Math.sin(t); y = cy - Rp * Math.cos(t);
            d = side[1] - (R + R * Math.cos(t));
            if (d <= 1e-9) return;
            len = 55 * d / (2 * R);
            arrow(g, x + side[0] * Math.sin(t) * len, y - Math.cos(t) * len, x, y, 'hs-blue hs-thin', 5);
          });
        }
        var px = cx - Rp * Math.sin(th), py = cy - Rp * Math.cos(th);
        var depth = hL - (R + R * Math.cos(th)), p = RHO * G * Math.max(depth, 0);
        s('line', { x1: cx, y1: cy, x2: px, y2: py, 'class': 'hs-line hs-green' }, g);
        s('line', { x1: px, y1: py, x2: px, y2: cy, 'class': 'hs-line hs-green hs-dash' }, g);
        s('line', { x1: px, y1: cy, x2: cx, y2: cy, 'class': 'hs-line hs-green hs-dash' }, g);
        s('line', { x1: cx, y1: cy, x2: cx, y2: cy - Rp - 20, 'class': 'hs-line hs-axis' }, g);
        if (th > 0.05) s('path', { d: 'M' + cx + ',' + (cy - 34) + 'A34,34 0 0 0 ' + (cx - 34 * Math.sin(th)) + ',' + (cy - 34 * Math.cos(th)), 'class': 'hs-line hs-thin' }, g);
        label(g, cx - 40 * Math.sin(th / 2) - 4, cy - 40 * Math.cos(th / 2), 'θ', 'end', 'hs-t');
        var nx = -Math.sin(th), ny = -Math.cos(th);                    // outward normal in screen coordinates
        var tx = ny, ty = -nx;                                       // unit tangent (screen), towards the top
        arrow(g, px, py, px + nx * 45, py + ny * 45, 'hs-blue', 9);
        label(g, px + nx * 56 - tx * 10, py + ny * 56 - ty * 10 + 5, 'n', 'middle', 'hs-t');
        if (depth > 0) {
          var Lf = 20 + 60 * depth / (2 * R);
          arrow(g, px + nx * (Lf + 6) + 24 * tx, py + ny * (Lf + 6) + 24 * ty, px + 24 * tx, py + 24 * ty, 'hs-acc', 10);
          label(g, px + nx * (Lf + 14) + 40 * tx, py + ny * (Lf + 14) + 40 * ty + 5, 'dF', 'middle', 'hs-t');
        }
        s('circle', { cx: px, cy: py, r: 4, 'class': 'hs-dot hs-acc' }, g);
        rows = [
          ['Element: height y = R + R cosθ', num(R + R * Math.cos(th), 3) + ' m'],
          ['Depth h_L − y, gauge pressure', depth > 0 ? num(depth, 3) + ' m, ' + num(p / 1000, 2) + ' kPa' : 'dry (above the left level)'],
          ['dF_x / dθ = (p − pₐ) sinθ L R', num(p * Math.sin(th) * L * R / 1000, 3) + ' kN/rad (to the right)'],
          ['dF_y / dθ = −(p − pₐ) cosθ L R', num(-p * Math.cos(th) * L * R / 1000, 3) + ' kN/rad (up positive)'],
          ['Left: F_1 = ρg L h_L²/2', num(FHL / 1000, 3) + ' kN, to the right'],
          ['Right: F_2 = ρg L h_R²/2', num(FHR / 1000, 3) + ' kN, to the left'],
          ['Net horizontal force F_1 − F_2', num((FHL - FHR) / 1000, 3) + ' kN (FS10: 18.394 kN)']
        ];
      } else {
        /* projections */
        var xp = 70, xq = 650, k2 = 60 / (2 * R);
        if (hL > 0) {
          s('rect', { x: xp, y: yL, width: 8, height: fl - yL, 'class': 'hs-proj' }, g);
          s('path', { d: 'M' + xp + ',' + yL + 'L' + (xp - hL * k2) + ',' + fl + 'L' + xp + ',' + fl, 'class': 'hs-line hs-blue hs-thin hs-nofill' }, g);
          arrow(g, xp + 12, fl - hL * sc / 3, xp + 70, fl - hL * sc / 3, 'hs-acc', 10);
          label(g, xp + 40, fl - hL * sc / 3 - 8, 'F_H,L', 'middle', 'hs-t');
        }
        if (hR > 0) {
          s('rect', { x: xq - 8, y: yR, width: 8, height: fl - yR, 'class': 'hs-proj' }, g);
          arrow(g, xq - 12, fl - hR * sc / 3, xq - 70, fl - hR * sc / 3, 'hs-acc', 10);
          label(g, xq - 40, fl - hR * sc / 3 - 8, 'F_H,R', 'middle', 'hs-t');
        }
        [[-1, hL, aL, yL], [1, hR, aR, yR]].forEach(function (side) {
          var sg = side[0], hh = side[1], ar = side[2], yy = side[3];
          if (hh <= 0) return;
          var bx = cx, by = cy + Rp;
          var P = [cx + sg * Rp * Math.sin(ar.beta), cy + Rp * Math.cos(ar.beta)];
          s('path', { d: 'M' + cx + ',' + cy + 'L' + bx + ',' + by + 'A' + Rp + ',' + Rp + ' 0 0 ' + (sg < 0 ? 1 : 0) + ' ' + P[0] + ',' + P[1] + 'Z', 'class': 'hs-sector' }, g);
          if (Math.abs(R - hh) > 1e-6 && Math.sin(ar.beta) > 1e-6)
            s('path', { d: 'M' + cx + ',' + cy + 'L' + cx + ',' + yy + 'L' + P[0] + ',' + P[1] + 'Z', 'class': hh < R ? 'hs-tri-minus' : 'hs-tri-plus' }, g);
          arrow(g, cx + sg * Rp * 0.45, fl - 20, cx + sg * Rp * 0.45, fl - 20 - 60 * ar.A / (Math.PI * R * R / 2), 'hs-acc', 10);
          label(g, cx + sg * (Rp * 0.45 + 14), fl - 34, sg < 0 ? 'F_V,L' : 'F_V,R', sg < 0 ? 'end' : 'start', 'hs-t');
        });
        rows = [
          ['Left: β_L, sector R²β/2', num(aL.beta * 180 / Math.PI, 1) + '°, ' + num(aL.sector, 4) + ' m²'],
          ['Left: triangle (R − h)R sinβ/2', (hL < R ? 'minus ' : 'plus ') + num(Math.abs(aL.tri), 4) + ' m²'],
          ['Right: β_R, sector', num(aR.beta * 180 / Math.PI, 1) + '°, ' + num(aR.sector, 4) + ' m²'],
          ['Right: triangle', (hR < R ? 'minus ' : 'plus ') + num(Math.abs(aR.tri), 4) + ' m²'],
          ['F_H,L = ρgL h_L²/2,  F_H,R', num(FHL / 1000, 3) + ' kN,  ' + num(FHR / 1000, 3) + ' kN'],
          ['Net F_x = F_H,L − F_H,R', num((FHL - FHR) / 1000, 3) + ' kN'],
          ['F_V = ρgL (A_L + A_R), upward', num((FVL + FVR) / 1000, 3) + ' kN (beyond the statement)']
        ];
        label(g, 360, 330, 'green: circular sector; pink: triangle subtracted (h < R); orange outline: triangle added (h > R)', 'middle', 'hs-t hs-small');
      }
      readouts(f.out, rows);
    }
    draw();
  }

  /* ================================================================ 3. floating hollow cube (FS3) */
  function buoyancyCube(host) {
    var n = ++uid;
    var f = frame(host, 'Simulator: floating hollow cube with trapped air',
      'Two dimensionless numbers fix the equilibrium of FS3: the weight ratio W/(ρgL³) and the pressure ratio ' +
      'pₐ/(ρgL) (about 10.3 for water and L = 1 m). Lower the pressure ratio to see the air being compressed.',
      720, 320);
    var c = f.controls;
    var cW = slider(c, 'hs' + n + 'w', 'Weight ratio W/(ρgL³):', 0.02, 0.95, 0.01, 0.4, '', 2, draw);
    var cP = slider(c, 'hs' + n + 'p', 'Pressure ratio pₐ/(ρgL):', 0.2, 20, 0.1, 10.3, '', 1, draw);

    function draw() {
      var w = cW.get(), pr = cP.get();
      var H1 = w, H2 = w / (pr + w), pc = 1 + w / pr;           // H1/L, H2/L, p_c/p_a
      var svg = f.svg;
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      var g = s('g', {}, svg);
      var Lp = 200, x0 = 150, ws = 120;                         // outer free surface at y = ws
      var yBase = ws + (H1 + H2) * Lp, yTop = yBase - Lp, yInt = ws + H1 * Lp;
      s('rect', { x: 20, y: ws, width: 440, height: 310 - ws, 'class': 'hs-water' }, g);
      s('rect', { x: x0, y: yTop, width: Lp, height: Lp, 'class': 'hs-air' }, g);
      s('rect', { x: x0, y: yInt, width: Lp, height: yBase - yInt, 'class': 'hs-water hs-inner' }, g);
      s('rect', { x: x0, y: yTop, width: Lp, height: Lp, 'class': 'hs-line hs-shell' }, g);
      s('line', { x1: 20, y1: ws, x2: x0, y2: ws, 'class': 'hs-line hs-surface' }, g);
      s('line', { x1: x0 + Lp, y1: ws, x2: 460, y2: ws, 'class': 'hs-line hs-surface' }, g);
      s('line', { x1: x0, y1: yInt, x2: x0 + Lp, y2: yInt, 'class': 'hs-line hs-surface' }, g);
      s('line', { x1: x0 + Lp / 2 - 9, y1: yBase, x2: x0 + Lp / 2 + 9, y2: yBase, 'class': 'hs-line hs-gap' }, g);
      label(g, 60, ws - 10, 'pₐ', 'middle', 'hs-t');
      label(g, x0 + Lp / 2, Math.max(yTop + 26, Math.min(yInt - 10, yTop + Lp / 2)), 'p_c', 'middle', 'hs-t');
      /* dimensions */
      var xd = x0 + Lp + 40;
      s('line', { x1: x0 + Lp, y1: yInt, x2: xd + 6, y2: yInt, 'class': 'hs-line hs-dash' }, g);
      s('line', { x1: x0 + Lp, y1: yBase, x2: xd + 6, y2: yBase, 'class': 'hs-line hs-dash' }, g);
      if (H1 * Lp > 4) { arrow(g, xd, ws + 2, xd, yInt, 'hs-dim', 6); arrow(g, xd, yInt - 2, xd, ws, 'hs-dim', 6); }
      label(g, xd + 8, (ws + yInt) / 2 + 5, 'H₁', 'start', 'hs-t');
      if (H2 * Lp > 4) { arrow(g, xd + 50, yInt + 2, xd + 50, yBase, 'hs-dim', 6); arrow(g, xd + 50, yBase - 2, xd + 50, yInt, 'hs-dim', 6); }
      label(g, xd + 58, (yInt + yBase) / 2 + 5, 'H₂', 'start', 'hs-t');
      /* forces on the shell: outside and inside of the top face, weight */
      var kf = 26;
      for (var i = 0; i < 4; i++) {
        var xx = x0 + 30 + i * 46;
        arrow(g, xx, yTop - kf - 8, xx, yTop - 2, 'hs-blue', 6);
        arrow(g, xx + 12, yTop + kf * pc + 6, xx + 12, yTop + 3, 'hs-acc', 6);
      }
      arrow(g, x0 + Lp / 2 + 30, yTop + 70, x0 + Lp / 2 + 30, yTop + 120, 'hs-pink', 10);
      label(g, x0 + Lp / 2 + 40, yTop + 112, 'W', 'start', 'hs-t');
      label(g, 560, 70, 'arrows on the top face:', 'middle', 'hs-t hs-small');
      label(g, 560, 88, 'outside pₐ L² (down), inside p_c L² (up)', 'middle', 'hs-t hs-small');
      var ok = H1 + H2 < 1;
      readouts(f.out, [
        ['H₁/L = W/(ρgL³)', num(H1, 4)],
        ['H₂/L = W/(pₐL² + W)', num(H2, 4)],
        ['p_c/pₐ = 1 + W/(pₐL²)', num(pc, 4)],
        ['Check (p_c − pₐ)L² = W', 'both equal ' + num(w / pr, 4) + ' pₐL²'],
        ['Top face above the outer surface?', ok ? 'yes: H₁ + H₂ = ' + num(H1 + H2, 3) + ' L < L' :
          'no: H₁ + H₂ ≥ L, the cube would sink below the surface and the model of the statement no longer holds', !ok]
      ]);
    }
    draw();
  }

  var SIMS = { 'plane-gate': planeGate, 'curved-surface': curvedSurface, 'buoyancy-cube': buoyancyCube };

  function init() {
    var nodes = document.querySelectorAll('.hs-sim[data-sim]');
    for (var i = 0; i < nodes.length; i++) {
      var fn = SIMS[nodes[i].getAttribute('data-sim')];
      if (fn && !nodes[i].classList.contains('hs-ready')) {
        try { fn(nodes[i]); } catch (err) { if (window.console) console.error('hydrostatics-sim', err); }
      }
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
