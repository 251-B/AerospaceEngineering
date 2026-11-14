/* Geometry simulator of the Engineering Mechanics problem cards.
 *
 * Each simulator lives inside its own problem card as
 *   <div class="m3-sim" data-archetype="..." data-config='{"params":{...},"defaults":{...},"readouts":[...]}'>
 * written by tools/build_mech_problems.py from the frontmatter key `sim` of the problem (never by hand).
 *
 * One engine (orthographic camera, depth-sorted SVG primitives, fold-down panel, controls) and eight declarative
 * archetypes:
 *   curvilinear-3d        particle on a space curve: r, v, a, intrinsic basis, cylindrical basis
 *   rotating-wire-groove  particle on a wire or groove fixed to a frame that turns about the vertical
 *   oscillator-phase      free, damped and forced oscillator with its rotating phasor
 *   rb-euler-kinematics   rigid body with Euler angles 3-1-3 or 3-2-1: angular velocity and instantaneous axis
 *   rb-inertia-principal  inertia tensor of a body: rotation of axes, Steiner shift, principal axes
 *   rb-planar-dynamics    planar body about a pivot: centre of mass, velocity field, forces
 *   rb-rolling-contact    disk, hoop or sphere rolling on a plane or on a cylinder
 *   rb-gyro-multibody     rotor on an axle with precession, nutation and spin
 *
 * Left: orbitable axonometric view (drag, arrow keys, sliders, quick views). Right: the plane normal to the active
 * rotation axis folded down on the paper, with the angle, the right triangle (L cos, L sin) and the live change of
 * basis matrix [0R1] (columns: the rotated unit vectors written in the fixed basis, as in Notes.pdf, chapter 8).
 * Inline SVG only: no canvas, no WebGL, no storage. The default state is the data of the statement; the readouts
 * declared in the configuration are the formulas of that solution, evaluated by a small arithmetic parser (no eval).
 */
(function () {
  'use strict';

  var NS = 'http://www.w3.org/2000/svg';
  var DEG = Math.PI / 180;

  /* ------------------------------------------------------------------ DOM helpers */
  function h(tag, attrs, parent, text) {
    var e = document.createElement(tag), k;
    for (k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function s(tag, attrs, parent, text) {
    var e = document.createElementNS(NS, tag), k;
    for (k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function num(v, d) {
    if (!isFinite(v)) return '–';
    var t = v.toFixed(d == null ? 3 : d);
    if (/^-0\.?0*$/.test(t)) t = t.slice(1);
    return t.replace('-', '−');
  }
  /* "i_1" -> i with the subscript 1 */
  function label(g, x, y, text, anchor, cls) {
    var t = s('text', { x: x.toFixed(1), y: y.toFixed(1), 'text-anchor': anchor || 'middle', 'class': 'm3-t ' + (cls || '') }, g);
    var re = /_([A-Za-z0-9,*\u0370-\u03ff]+)/g, last = 0, m;
    while ((m = re.exec(text))) {
      if (m.index > last) t.appendChild(document.createTextNode(text.slice(last, m.index)));
      s('tspan', { 'baseline-shift': 'sub', 'font-size': '72%' }, t, m[1]);
      last = re.lastIndex;
    }
    if (last < text.length) t.appendChild(document.createTextNode(text.slice(last)));
    return t;
  }

  /* labels never sit on one another: each one takes the first free place around its anchor */
  function placer(g) {
    var boxes = [];
    return function (x, y, text, anchor, cls) {
      var w = 7.6 * text.replace(/_/g, '').length + 6, hh = 17, k, r, a, bx, by, x0, ok, i;
      for (k = 0; k < 25; k++) {
        r = k === 0 ? 0 : 9 * Math.ceil(k / 8); a = (k - 1) * Math.PI / 4;
        bx = x + r * Math.cos(a); by = y + r * Math.sin(a);
        x0 = anchor === 'start' ? bx : anchor === 'end' ? bx - w : bx - w / 2;
        ok = true;
        for (i = 0; i < boxes.length; i++) if (x0 < boxes[i][0] + boxes[i][2] && x0 + w > boxes[i][0] && by - hh + 4 < boxes[i][1] + hh && by + 4 > boxes[i][1]) { ok = false; break; }
        if (ok) break;
      }
      boxes.push([x0, by - hh + 4, w, hh]);
      return label(g, bx, by, text, anchor, cls);
    };
  }

  /* ------------------------------------------------------------------ vectors and matrices */
  function add(a, b) { return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]; }
  function sub(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
  function mul(a, k) { return [a[0] * k, a[1] * k, a[2] * k]; }
  function dot(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function cross(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
  function len(a) { return Math.sqrt(dot(a, a)); }
  function unit(a) { var l = len(a); return l < 1e-12 ? [0, 0, 0] : mul(a, 1 / l); }
  function mm(A, B) {
    var C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], i, j, k;
    for (i = 0; i < 3; i++) for (j = 0; j < 3; j++) for (k = 0; k < 3; k++) C[i][j] += A[i][k] * B[k][j];
    return C;
  }
  function mv(A, v) { return [dot(A[0], v), dot(A[1], v), dot(A[2], v)]; }
  function tr(A) { return [[A[0][0], A[1][0], A[2][0]], [A[0][1], A[1][1], A[2][1]], [A[0][2], A[1][2], A[2][2]]]; }
  function col(A, j) { return [A[0][j], A[1][j], A[2][j]]; }
  function det(A) { return dot(A[0], cross(A[1], A[2])); }
  var I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
  var X = [1, 0, 0], Y = [0, 1, 0], Z = [0, 0, 1], O = [0, 0, 0];
  /* elementary rotation: the columns are the rotated unit vectors in the fixed basis */
  function rot(ax, a) {
    var c = Math.cos(a), n = Math.sin(a);
    if (ax === 'x') return [[1, 0, 0], [0, c, -n], [0, n, c]];
    if (ax === 'y') return [[c, 0, n], [0, 1, 0], [-n, 0, c]];
    return [[c, -n, 0], [n, c, 0], [0, 0, 1]];
  }
  /* symmetric 3x3 eigenproblem (Jacobi): values ascending, vectors as columns */
  function eigSym(A) {
    var a = [A[0].slice(), A[1].slice(), A[2].slice()], V = [[1, 0, 0], [0, 1, 0], [0, 0, 1]], it, p, q, i;
    for (it = 0; it < 60; it++) {
      p = 0; q = 1;
      if (Math.abs(a[0][2]) > Math.abs(a[p][q])) { p = 0; q = 2; }
      if (Math.abs(a[1][2]) > Math.abs(a[p][q])) { p = 1; q = 2; }
      if (Math.abs(a[p][q]) < 1e-13) break;
      var th = 0.5 * Math.atan2(2 * a[p][q], a[q][q] - a[p][p]), c = Math.cos(th), n = Math.sin(th);
      for (i = 0; i < 3; i++) { var aip = a[i][p], aiq = a[i][q]; a[i][p] = c * aip - n * aiq; a[i][q] = n * aip + c * aiq; }
      for (i = 0; i < 3; i++) { var api = a[p][i], aqi = a[q][i]; a[p][i] = c * api - n * aqi; a[q][i] = n * api + c * aqi; }
      for (i = 0; i < 3; i++) { var vip = V[i][p], viq = V[i][q]; V[i][p] = c * vip - n * viq; V[i][q] = n * vip + c * viq; }
    }
    var idx = [0, 1, 2].sort(function (u, v) { return a[u][u] - a[v][v]; });
    return { values: idx.map(function (k) { return a[k][k]; }), vectors: idx.map(function (k) { return col(V, k); }) };
  }

  /* ------------------------------------------------------------------ arithmetic parser (readouts and vectors) */
  var FUN = {
    sin: Math.sin, cos: Math.cos, tan: Math.tan, asin: Math.asin, acos: Math.acos, atan: Math.atan, atan2: Math.atan2,
    sqrt: Math.sqrt, abs: Math.abs, exp: Math.exp, log: Math.log, min: Math.min, max: Math.max, pow: Math.pow,
    sign: function (x) { return x > 0 ? 1 : x < 0 ? -1 : 0; }, deg: function (x) { return x / DEG; }, rad: function (x) { return x * DEG; }
  };
  function compile(src) {
    var tok = String(src).match(/\s*(\d+\.?\d*(?:[eE][-+]?\d+)?|\.\d+|[A-Za-z_][A-Za-z_0-9]*|[-+*\/^(),])/g) || [], i = 0;
    tok = tok.map(function (t) { return t.trim(); });
    if (tok.join('') !== String(src).replace(/\s+/g, '')) return function () { return NaN; };
    function peek() { return tok[i]; }
    function expr() {
      var a = term();
      while (peek() === '+' || peek() === '-') { a = bin(tok[i++], a, term()); }
      return a;
    }
    function term() {
      var a = unary();
      while (peek() === '*' || peek() === '/') { a = bin(tok[i++], a, unary()); }
      return a;
    }
    function unary() {
      if (peek() === '-') { i++; var a = unary(); return function (e) { return -a(e); }; }
      if (peek() === '+') { i++; return unary(); }
      var b = atom();
      if (peek() === '^') { i++; var c = unary(); return function (e) { return Math.pow(b(e), c(e)); }; }
      return b;
    }
    function bin(op, a, b) {
      if (op === '+') return function (e) { return a(e) + b(e); };
      if (op === '-') return function (e) { return a(e) - b(e); };
      if (op === '*') return function (e) { return a(e) * b(e); };
      return function (e) { return a(e) / b(e); };
    }
    function atom() {
      var t = tok[i++];
      if (t === undefined) throw new Error('end');
      if (t === '(') { var a = expr(); if (tok[i++] !== ')') throw new Error(')'); return a; }
      if (/^[\d.]/.test(t)) { var v = parseFloat(t); return function () { return v; }; }
      if (/^[A-Za-z_]/.test(t)) {
        if (peek() === '(') {
          i++;
          var args = [];
          if (peek() !== ')') { args.push(expr()); while (peek() === ',') { i++; args.push(expr()); } }
          if (tok[i++] !== ')') throw new Error(')');
          var f = Object.prototype.hasOwnProperty.call(FUN, t) ? FUN[t] : null;
          return function (e) { return f ? f.apply(null, args.map(function (a) { return a(e); })) : NaN; };
        }
        if (t === 'pi') return function () { return Math.PI; };
        return function (e) { return Object.prototype.hasOwnProperty.call(e, t) && typeof e[t] === 'number' ? e[t] : NaN; };
      }
      throw new Error(t);
    }
    try { var f = expr(); if (i !== tok.length) throw new Error('tail'); return f; } catch (err) { return function () { return NaN; }; }
  }

  /* ------------------------------------------------------------------ scene (world coordinates, z up) */
  function Scene() { this.items = []; }
  Scene.prototype.line = function (a, b, cls) { this.items.push({ k: 'line', p: [a, b], cls: cls || '' }); };
  Scene.prototype.arrow = function (a, b, cls, text) { this.items.push({ k: 'arrow', p: [a, b], cls: cls || '', text: text }); };
  Scene.prototype.poly = function (pts, cls, closed) { this.items.push({ k: 'poly', p: pts, cls: cls || '', closed: !!closed }); };
  Scene.prototype.dot = function (p, cls, text) { this.items.push({ k: 'dot', p: [p], cls: cls || '', text: text }); };
  Scene.prototype.text = function (p, text, cls) { this.items.push({ k: 'text', p: [p], text: text, cls: cls || '' }); };
  Scene.prototype.triad = function (o, R, n, cls, L, names) {
    var nm = names || ['i_' + n, 'j_' + n, 'k_' + n], j;
    for (j = 0; j < 3; j++) this.arrow(o, add(o, mul(col(R, j), L)), cls, nm[j]);
  };
  Scene.prototype.circle = function (c, u, v, r, cls, closed, a0, a1) {
    var pts = [], n = 48, i, a;
    a0 = a0 == null ? 0 : a0; a1 = a1 == null ? 2 * Math.PI : a1;
    for (i = 0; i <= n; i++) { a = a0 + (a1 - a0) * i / n; pts.push(add(c, add(mul(u, r * Math.cos(a)), mul(v, r * Math.sin(a))))); }
    this.poly(pts, cls, closed);
  };
  Scene.prototype.box = function (c, R, a, b, d, cls) {
    var e = [col(R, 0), col(R, 1), col(R, 2)], hs = [a / 2, b / 2, d / 2], self = this;
    function P(x, y, z) { return add(c, add(mul(e[0], x * hs[0]), add(mul(e[1], y * hs[1]), mul(e[2], z * hs[2])))); }
    [[-1, -1], [-1, 1], [1, -1], [1, 1]].forEach(function (q) {
      self.line(P(-1, q[0], q[1]), P(1, q[0], q[1]), cls);
      self.line(P(q[0], -1, q[1]), P(q[0], 1, q[1]), cls);
      self.line(P(q[0], q[1], -1), P(q[0], q[1], 1), cls);
    });
  };
  /* right triangle with its right angle at the foot of b on the line (a, a + u) */
  Scene.prototype.triangle = function (a, b, u, cls) {
    var foot = add(a, mul(u, dot(sub(b, a), u)));
    this.poly([a, foot, b], 'm3-tri ' + (cls || ''), true);
    return foot;
  };

  var VIEWS = {
    iso: { name: '3D Isometric', az: 45, el: 35.264 },
    top: { name: 'Top XY', az: -90, el: 90 },
    front: { name: 'Front XZ', az: -90, el: 0 },
    side: { name: 'Side YZ', az: 0, el: 0 },
    omega: { name: 'Plane normal to ω' }
  };

  function camera(az, el) {
    var a = az * DEG, b = el * DEG, ca = Math.cos(a), sa = Math.sin(a), cb = Math.cos(b), sb = Math.sin(b);
    return { right: [-sa, ca, 0], up: [-sb * ca, -sb * sa, cb], depth: [cb * ca, cb * sa, sb] };
  }

  function arrowHead(g, x1, y1, x2, y2, cls) {
    var L = Math.hypot(x2 - x1, y2 - y1);
    if (L < 3) { s('circle', { cx: x2.toFixed(1), cy: y2.toFixed(1), r: 3, 'class': 'm3-head ' + cls }, g); return; }
    var a = Math.atan2(y2 - y1, x2 - x1), k = Math.min(9, L * 0.45);
    s('line', { x1: x1.toFixed(1), y1: y1.toFixed(1), x2: (x2 - 0.7 * k * Math.cos(a)).toFixed(1), y2: (y2 - 0.7 * k * Math.sin(a)).toFixed(1), 'class': 'm3-line ' + cls }, g);
    s('path', {
      d: 'M' + x2.toFixed(1) + ',' + y2.toFixed(1) + 'L' + (x2 - k * Math.cos(a - 0.42)).toFixed(1) + ',' + (y2 - k * Math.sin(a - 0.42)).toFixed(1) +
        'L' + (x2 - k * Math.cos(a + 0.42)).toFixed(1) + ',' + (y2 - k * Math.sin(a + 0.42)).toFixed(1) + 'Z', 'class': 'm3-head ' + cls
    }, g);
  }

  function render(scene, cam, g, cx, cy, sc) {
    function pr(p) { return [cx + sc * dot(p, cam.right), cy - sc * dot(p, cam.up)]; }
    var items = scene.items.map(function (it, n) {
      var d = 0, i;
      for (i = 0; i < it.p.length; i++) d += dot(it.p[i], cam.depth);
      return { it: it, d: d / it.p.length + (it.k === 'poly' && it.closed ? -1e-3 : 0), n: n };
    }).sort(function (a, b) { return a.d - b.d || a.n - b.n; });
    var texts = [];
    items.forEach(function (o) {
      var it = o.it, q = it.p.map(pr);
      if (it.k === 'line') {
        s('line', { x1: q[0][0].toFixed(1), y1: q[0][1].toFixed(1), x2: q[1][0].toFixed(1), y2: q[1][1].toFixed(1), 'class': 'm3-line ' + it.cls }, g);
      } else if (it.k === 'arrow') {
        arrowHead(g, q[0][0], q[0][1], q[1][0], q[1][1], it.cls);
        if (it.text) {
          var dx = q[1][0] - q[0][0], dy = q[1][1] - q[0][1], L = Math.hypot(dx, dy) || 1;
          if (L < 3) { dx = 0.7; dy = -0.7; L = 1; }
          if (/m3-(r|mid)\b/.test(it.cls)) texts.push([(q[0][0] + q[1][0]) / 2 - 12 * dy / L, (q[0][1] + q[1][1]) / 2 + 12 * dx / L + 4, it.text, 'middle']);
          else texts.push([q[1][0] + 13 * dx / L, q[1][1] + 13 * dy / L + 4, it.text, 'middle']);
        }
      } else if (it.k === 'poly') {
        s('path', { d: 'M' + q.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join('L') + (it.closed ? 'Z' : ''), 'class': 'm3-poly ' + it.cls }, g);
      } else if (it.k === 'dot') {
        s('circle', { cx: q[0][0].toFixed(1), cy: q[0][1].toFixed(1), r: 4, 'class': 'm3-dot ' + it.cls }, g);
        if (it.text) texts.push([q[0][0] + 9, q[0][1] - 8, it.text, 'start']);
      } else if (it.k === 'text') {
        texts.push([q[0][0], q[0][1], it.text, 'middle']);
      }
    });
    var put = placer(g);
    texts.forEach(function (t) { put(t[0], t[1], t[2], t[3]); });
  }

  /* ------------------------------------------------------------------ fold-down panel (right) */
  /* rot = { sym, angle, axis, axisLabel, u, v, fixed:[a,b], moved:[a,b], m1, m2, L, R } */
  function foldPanel(g, rt) {
    var ox = 590, oy = 168, A = 92, T = 74, put = placer(g);
    var n = unit(rt.axis), u = unit(rt.u), v = unit(rt.v);
    var out = dot(cross(u, v), n) > 0;                    /* axis towards the reader when (u, v, axis) is right-handed */
    function P(w, k) { return [ox + k * dot(w, u), oy - k * dot(w, v)]; }
    label(g, 600, 22, rt.caption || ('Plane normal to ' + rt.axisLabel + ', folded down'), 'middle', 'm3-cap');
    /* axis symbol */
    if (!rt.caption) {
      s('circle', { cx: 468, cy: 48, r: 9, 'class': 'm3-line m3-sym' }, g);
      if (out) s('circle', { cx: 468, cy: 48, r: 2.6, 'class': 'm3-dot' }, g);
      else { s('line', { x1: 462, y1: 42, x2: 474, y2: 54, 'class': 'm3-line m3-sym' }, g); s('line', { x1: 474, y1: 42, x2: 462, y2: 54, 'class': 'm3-line m3-sym' }, g); }
      label(g, 483, 53, rt.axisLabel + (out ? ' out of the paper' : ' into the paper'), 'start', 'm3-small');
    }
    /* fixed axes */
    arrowHead(g, ox - 40, oy, ox + A, oy, 'm3-fixed');
    arrowHead(g, ox, oy + 40, ox, oy - A, 'm3-fixed');
    put(ox + A + 13, oy + 5, rt.fixed[0], 'middle');
    put(ox, oy - A - 8, rt.fixed[1], 'middle');
    /* moved axes */
    var m1 = P(rt.m1, A * 0.94), m2 = P(rt.m2, A * 0.94);
    var a1 = Math.atan2(oy - m1[1], m1[0] - ox);
    /* right triangle: hypotenuse along the first moved axis */
    var hx = ox + T * Math.cos(a1), hy = oy - T * Math.sin(a1);
    if (Math.abs(Math.sin(a1)) > 0.03 && Math.abs(Math.cos(a1)) > 0.03) {
      s('path', { d: 'M' + ox + ',' + oy + 'L' + hx.toFixed(1) + ',' + oy + 'L' + hx.toFixed(1) + ',' + hy.toFixed(1) + 'Z', 'class': 'm3-poly m3-tri' }, g);
      var q = 7, sx = Math.cos(a1) > 0 ? -1 : 1, sy = Math.sin(a1) > 0 ? -1 : 1;
      s('path', { d: 'M' + (hx + sx * q).toFixed(1) + ',' + oy + 'l0,' + (sy * q) + 'l' + (-sx * q) + ',0', 'class': 'm3-line m3-thin' }, g);
      put((ox + hx) / 2, oy + (Math.sin(a1) > 0 ? 17 : -8), rt.L + ' cos ' + rt.sym, 'middle', 'm3-small');
      put(hx + (Math.cos(a1) > 0 ? 7 : -7), (oy + hy) / 2 + 4, rt.L + ' sin ' + rt.sym, Math.cos(a1) > 0 ? 'start' : 'end', 'm3-small');
    }
    arrowHead(g, ox, oy, m1[0], m1[1], 'm3-b1');
    arrowHead(g, ox, oy, m2[0], m2[1], 'm3-b1');
    function tip(m, t) { var dx = m[0] - ox, dy = m[1] - oy, L = Math.hypot(dx, dy) || 1; put(m[0] - 2 * dx / L + 15 * dy / L, m[1] - 2 * dy / L - 15 * dx / L + 4, t, 'middle'); }
    tip(m1, rt.moved[0]); tip(m2, rt.moved[1]);
    /* arc of the angle, from the first fixed axis to the first moved axis */
    if (Math.abs(a1) > 0.02) {
      var r = 30, ex = ox + r * Math.cos(a1), ey = oy - r * Math.sin(a1);
      s('path', { d: 'M' + (ox + r) + ',' + oy + 'A' + r + ',' + r + ' 0 ' + (Math.abs(a1) > Math.PI ? 1 : 0) + ' ' + (a1 > 0 ? 0 : 1) + ' ' + ex.toFixed(1) + ',' + ey.toFixed(1), 'class': 'm3-line m3-arc' }, g);
      var am = a1 / 2;
      put(ox + (r + 13) * Math.cos(am), oy - (r + 13) * Math.sin(am) + 4, rt.sym, 'middle');
    }
    /* live matrix */
    var R = rt.R, y0 = 292, i, j;
    label(g, 468, y0 + 22, rt.matLabel || '[_0R_1] =', 'start', 'm3-small');
    s('path', { d: 'M548,' + (y0 - 10) + 'h-6v62h6M734,' + (y0 - 10) + 'h6v62h-6', 'class': 'm3-line m3-thin' }, g);
    for (i = 0; i < 3; i++) for (j = 0; j < 3; j++) label(g, 606 + 60 * (j - 0.5) + 28, y0 + 4 + 20 * i, num(R[i][j], 3), 'end', 'm3-mono');
  }

  /* ------------------------------------------------------------------ shared pieces of the archetypes */
  function eulerFrames(seq, psi, th, phi) {
    var second = seq === '321' ? 'y' : 'x', third = seq === '321' ? 'x' : 'z';
    var R1 = rot('z', psi), E2 = rot(second, th), E3 = rot(third, phi);
    var R2 = mm(R1, E2), R3 = mm(R2, E3);
    var a2 = second === 'y' ? 1 : 0, a3 = third === 'x' ? 0 : 2;
    return { R1: R1, R2: R2, R3: R3, E: [R1, E2, E3], axes: [Z, col(R1, a2), col(R2, a3)], a2: a2, a3: a3 };
  }
  var AX = ['i', 'j', 'k'];
  function eulerRotations(fr, ang, syms) {
    var a2 = fr.a2, a3 = fr.a3, p2 = [(a2 + 1) % 3, (a2 + 2) % 3], p3 = [(a3 + 1) % 3, (a3 + 2) % 3];
    return [
      { id: 'r1', sym: syms[0], angle: ang[0], axis: Z, axisLabel: 'k_0', u: X, v: Y, fixed: ['i_0', 'j_0'], moved: ['i_1', 'j_1'],
        m1: col(fr.R1, 0), m2: col(fr.R1, 1), L: 'L', R: fr.E[0], matLabel: '[_0R_1] =' },
      { id: 'r2', sym: syms[1], angle: ang[1], axis: fr.axes[1], axisLabel: AX[a2] + '_1', u: col(fr.R1, p2[0]), v: col(fr.R1, p2[1]),
        fixed: [AX[p2[0]] + '_1', AX[p2[1]] + '_1'], moved: [AX[p2[0]] + '_2', AX[p2[1]] + '_2'],
        m1: col(fr.R2, p2[0]), m2: col(fr.R2, p2[1]), L: 'L', R: fr.E[1], matLabel: '[_1R_2] =' },
      { id: 'r3', sym: syms[2], angle: ang[2], axis: fr.axes[2], axisLabel: AX[a3] + '_2', u: col(fr.R2, p3[0]), v: col(fr.R2, p3[1]),
        fixed: [AX[p3[0]] + '_2', AX[p3[1]] + '_2'], moved: [AX[p3[0]] + '_3', AX[p3[1]] + '_3'],
        m1: col(fr.R3, p3[0]), m2: col(fr.R3, p3[1]), L: 'L', R: fr.E[2], matLabel: '[_2R_3] =' }
    ];
  }
  function zRotation(id, sym, a, Lname, moved) {
    var R = rot('z', a);
    return { id: id, sym: sym, angle: a, axis: Z, axisLabel: 'k_0', u: X, v: Y, fixed: ['i_0', 'j_0'], moved: moved || ['i_1', 'j_1'],
      m1: col(R, 0), m2: col(R, 1), L: Lname || 'L', R: R, matLabel: '[_0R_1] =' };
  }
  function ground(sc, e) { sc.poly([[-e, -e, 0], [e, -e, 0], [e, e, 0], [-e, e, 0]], 'm3-ground', true); }
  function slider(id, labelText, min, max, value, step, unit) { return { id: id, label: labelText, min: min, max: max, value: value, step: step || 1, unit: unit || '' }; }

  /* curves of curvilinear-3d: r(u) in metres */
  var CURVES = {
    helix: function (P, u) { return [P.R * Math.cos(u), P.R * Math.sin(u), P.b * u]; },
    circle: function (P, u) { return [P.R * Math.cos(u), P.R * Math.sin(u), 0]; },
    ellipse: function (P, u) { return [P.a * Math.cos(u), P.b * Math.sin(u), 0]; },
    spiral: function (P, u) { var r = P.a + P.c * u; return [r * Math.cos(u), r * Math.sin(u), 0]; },
    logspiral: function (P, u) { var r = P.a * Math.exp(P.c * u); return [r * Math.cos(u), r * Math.sin(u), 0]; },
    conical: function (P, u) { return [P.c * u * Math.cos(u), P.c * u * Math.sin(u), P.b * u]; },
    cardioid: function (P, u) { var r = P.a * (1 + Math.cos(u)); return [r * Math.cos(u), r * Math.sin(u), 0]; },
    cycloid: function (P, u) { return [P.R * (u - Math.sin(u)), 0, P.R * (1 - Math.cos(u))]; },
    parabola: function (P, u) { return [u, 0, P.k * u * u]; },
    line: function (P, u) { return [P.x0 + P.vx * u, P.y0 + P.vy * u, P.z0 + P.vz * u]; },
    projectile: function (P, u) { return [P.v0 * Math.cos(P.elev * DEG) * u, 0, P.v0 * Math.sin(P.elev * DEG) * u - 0.5 * P.g * u * u]; }
  };
  var LINEAR = { parabola: 1, line: 1, projectile: 1 };

  /* planar outlines of the body shapes, in body axes with the origin at the centre of mass */
  function outline(P) {
    var pts = [], i, a;
    if (P.shape === 'disk' || P.shape === 'hoop' || P.shape === 'sphere') {
      for (i = 0; i <= 40; i++) { a = 2 * Math.PI * i / 40; pts.push([P.R * Math.cos(a), P.R * Math.sin(a), 0]); }
    } else if (P.shape === 'rect') {
      pts = [[-P.a / 2, -P.b / 2, 0], [P.a / 2, -P.b / 2, 0], [P.a / 2, P.b / 2, 0], [-P.a / 2, P.b / 2, 0], [-P.a / 2, -P.b / 2, 0]];
    } else if (P.shape === 'triangle') {
      pts = [[-P.a / 3, -P.b / 3, 0], [2 * P.a / 3, -P.b / 3, 0], [-P.a / 3, 2 * P.b / 3, 0], [-P.a / 3, -P.b / 3, 0]];
    } else {
      pts = [[-P.L / 2, 0, 0], [P.L / 2, 0, 0]];
    }
    return pts;
  }

  /* inertia tensor at the centre of mass, in body axes, and the wireframe of the shape */
  function inertia(P) {
    var m = P.m, d, G = [0, 0, 0], I, parts = [];
    function diag(a, b, c) { return [[a, 0, 0], [0, b, 0], [0, 0, c]]; }
    if (P.tensor) return { I: P.tensor, G: G, parts: parts };
    switch (P.shape) {
      case 'rod': I = diag(0, m * P.L * P.L / 12, m * P.L * P.L / 12); break;
      case 'plate': I = diag(m * P.b * P.b / 12, m * P.a * P.a / 12, m * (P.a * P.a + P.b * P.b) / 12); break;
      case 'disk': I = diag(m * P.R * P.R / 4, m * P.R * P.R / 4, m * P.R * P.R / 2); break;
      case 'cylinder': d = m * (3 * P.R * P.R + P.h * P.h) / 12; I = diag(d, d, m * P.R * P.R / 2); break;
      case 'sphere': d = 0.4 * m * P.R * P.R; I = diag(d, d, d); break;
      case 'shell': d = 2 * m * P.R * P.R / 3; I = diag(d, d, d); break;
      case 'cone': d = 3 * m * (4 * P.R * P.R + P.h * P.h) / 80; I = diag(d, d, 0.3 * m * P.R * P.R); break;
      case 'rects':
        /* thin plate made of rectangles [x, y, w, h] (lower-left corner) of uniform surface density */
        var A = 0, sx = 0, sy = 0, Ixx = 0, Iyy = 0, Ixy = 0;
        P.rects.forEach(function (r) { var a = r[2] * r[3]; A += a; sx += a * (r[0] + r[2] / 2); sy += a * (r[1] + r[3] / 2); });
        G = [sx / A, sy / A, 0];
        P.rects.forEach(function (r) {
          var mi = m * r[2] * r[3] / A, x = r[0] + r[2] / 2 - G[0], y = r[1] + r[3] / 2 - G[1];
          Ixx += mi * (r[3] * r[3] / 12 + y * y); Iyy += mi * (r[2] * r[2] / 12 + x * x); Ixy += mi * x * y;
          parts.push(r);
        });
        I = [[Ixx, -Ixy, 0], [-Ixy, Iyy, 0], [0, 0, Ixx + Iyy]];
        break;
      default: I = diag(m * (P.b * P.b + P.c * P.c) / 12, m * (P.a * P.a + P.c * P.c) / 12, m * (P.a * P.a + P.b * P.b) / 12);
    }
    return { I: I, G: G, parts: parts };
  }
  function steiner(I, m, d) {
    var d2 = dot(d, d), J = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], i, j;
    for (i = 0; i < 3; i++) for (j = 0; j < 3; j++) J[i][j] = I[i][j] + m * ((i === j ? d2 : 0) - d[i] * d[j]);
    return J;
  }
  function drawShape(sc, P, R, c, cls) {
    var e = [col(R, 0), col(R, 1), col(R, 2)];
    function W(p) { return add(c, add(mul(e[0], p[0]), add(mul(e[1], p[1]), mul(e[2], p[2])))); }
    switch (P.shape) {
      case 'rod': sc.line(W([-P.L / 2, 0, 0]), W([P.L / 2, 0, 0]), cls + ' m3-thick'); break;
      case 'plate': sc.poly([W([-P.a / 2, -P.b / 2, 0]), W([P.a / 2, -P.b / 2, 0]), W([P.a / 2, P.b / 2, 0]), W([-P.a / 2, P.b / 2, 0])], cls + ' m3-fill', true); break;
      case 'disk': sc.circle(c, e[0], e[1], P.R, cls + ' m3-fill', true); break;
      case 'sphere': case 'shell': sc.circle(c, e[0], e[1], P.R, cls); sc.circle(c, e[1], e[2], P.R, cls); sc.circle(c, e[0], e[2], P.R, cls); break;
      case 'cylinder':
        sc.circle(add(c, mul(e[2], -P.h / 2)), e[0], e[1], P.R, cls); sc.circle(add(c, mul(e[2], P.h / 2)), e[0], e[1], P.R, cls);
        [0, 1, 2, 3].forEach(function (q) { var a = q * Math.PI / 2, p = [P.R * Math.cos(a), P.R * Math.sin(a)]; sc.line(W([p[0], p[1], -P.h / 2]), W([p[0], p[1], P.h / 2]), cls); });
        break;
      case 'cone':
        /* centre of mass at h/4 above the base */
        sc.circle(add(c, mul(e[2], -P.h / 4)), e[0], e[1], P.R, cls);
        [0, 1, 2, 3].forEach(function (q) { var a = q * Math.PI / 2; sc.line(W([P.R * Math.cos(a), P.R * Math.sin(a), -P.h / 4]), W([0, 0, 3 * P.h / 4]), cls); });
        break;
      case 'rects':
        var G = inertia(P).G;
        P.rects.forEach(function (r) {
          var x = r[0] - G[0], y = r[1] - G[1];
          sc.poly([W([x, y, 0]), W([x + r[2], y, 0]), W([x + r[2], y + r[3], 0]), W([x, y + r[3], 0])], cls + ' m3-fill', true);
        });
        break;
      default: sc.box(c, R, P.a, P.b, P.c, cls);
    }
  }

  /* ------------------------------------------------------------------ the eight archetypes */
  var ARCH = {};

  ARCH['curvilinear-3d'] = {
    title: 'Particle on a curve',
    params: { curve: 'helix', R: 1, a: 1, b: 0.15, c: 0.2, k: 0.5, x0: 0, y0: 0, z0: 0, vx: 1, vy: 0, vz: 0, v0: 5, elev: 45, g: 9.81, rate: 1, accel: 0, umin: 0, umax: 720, extent: 1.6 },
    controls: function (P) {
      return LINEAR[P.curve] ? [slider('u', P.curve === 'projectile' ? 'Time t' : 'Parameter u', P.umin, P.umax, P.umin, (P.umax - P.umin) / 200)]
        : [slider('u', 'Angle θ', P.umin, P.umax, 60, 1, 'deg')];
    },
    build: function (P, S, sc) {
      var f = CURVES[P.curve] || CURVES.helix, u = S.u, hh = 1e-4 * Math.max(1, Math.abs(u));
      var lo = LINEAR[P.curve] ? P.umin : P.umin * DEG, hi = LINEAR[P.curve] ? P.umax : P.umax * DEG;
      var r = f(P, u), d1 = mul(sub(f(P, u + hh), f(P, u - hh)), 1 / (2 * hh));
      var d2 = mul(add(sub(f(P, u + hh), mul(r, 2)), f(P, u - hh)), 1 / (hh * hh));
      var v = mul(d1, P.rate), a = add(mul(d2, P.rate * P.rate), mul(d1, P.accel));
      var sp = len(v), et = unit(v), at = dot(a, et), an = sub(a, mul(et, at)), anm = len(an), en = unit(an), eb = cross(et, en);
      var pts = [], i, e = P.extent;
      for (i = 0; i <= 160; i++) pts.push(f(P, lo + (hi - lo) * i / 160));
      sc.triad(O, I3, 0, 'm3-fixed', 0.55 * e);
      sc.poly(pts, 'm3-path');
      sc.arrow(O, r, 'm3-r', 'r');
      var k = 0.42 * e;
      sc.arrow(r, add(r, mul(et, k)), 'm3-v', 'e_t');
      if (anm > 1e-9) { sc.arrow(r, add(r, mul(en, k)), 'm3-acc', 'e_n'); sc.arrow(r, add(r, mul(eb, 0.7 * k)), 'm3-b1', 'e_b'); }
      var foot = [r[0], r[1], 0], rho = Math.hypot(r[0], r[1]), th = Math.atan2(r[1], r[0]), rots;
      if (rho > 1e-9) {
        sc.line(foot, r, 'm3-dash');
        sc.triangle(O, foot, X, '');
        var er = [Math.cos(th), Math.sin(th), 0], eth = [-Math.sin(th), Math.cos(th), 0];
        sc.arrow(foot, add(foot, mul(er, 0.6 * k)), 'm3-b1', 'e_ρ');
        sc.arrow(foot, add(foot, mul(eth, 0.6 * k)), 'm3-b1', 'e_θ');
        rots = [zRotation('theta', 'θ', th, 'ρ', ['e_ρ', 'e_θ'])];
      } else {
        /* motion in the vertical plane: the tangent turns about j0 (into the paper in the front view) */
        var ga = Math.atan2(et[2], et[0]), Rg = rot('y', -ga);
        rots = [{ id: 'gamma', sym: 'γ', angle: ga, axis: [0, -1, 0], axisLabel: '−j_0', u: X, v: Z, fixed: ['i_0', 'k_0'], moved: ['e_t', 'e_n*'],
          m1: col(Rg, 0), m2: col(Rg, 2), L: 'v', R: Rg, matLabel: '[_0R_t] =' }];
      }
      sc.dot(r, 'm3-p', 'P');
      return {
        rotations: rots, R: rots[0].R, omega: rots[0].axis,
        vars: { u: u, x: r[0], y: r[1], z: r[2], rho: rho, theta: th, v: sp, at: at, an: anm, rhoc: anm > 1e-9 ? sp * sp / anm : Infinity },
        readouts: [['Position r (m)', '(' + num(r[0], 3) + ', ' + num(r[1], 3) + ', ' + num(r[2], 3) + ')'], ['Speed v (m/s)', num(sp, 3)],
          ['Tangential acceleration (m/s²)', num(at, 3)], ['Normal acceleration (m/s²)', num(anm, 3)],
          ['Radius of curvature (m)', anm > 1e-9 ? num(sp * sp / anm, 3) : 'infinite (straight)']]
      };
    }
  };

  ARCH['rotating-wire-groove'] = {
    title: 'Particle on a rotating wire',
    params: { wire: 'line', beta: 30, R: 1, e: 0, hgt: 0, k: 0.5, d: 0.4, Omega: 1, qdot: 0.5, qmin: 0, qmax: 1.5, extent: 1.6 },
    controls: function (P) {
      var ang = P.wire === 'hoop';
      return [slider('psi', 'Frame angle ψ = Ωt', 0, 360, 40, 1, 'deg'),
        ang ? slider('q', 'Position angle θ', -180, 180, 50, 1, 'deg') : slider('q', 'Coordinate along the wire (m)', P.qmin, P.qmax, 0.6 * P.qmax + 0.4 * P.qmin, (P.qmax - P.qmin) / 150)];
    },
    build: function (P, S, sc) {
      var b = P.beta * DEG;
      /* point of the wire in the rotating frame S1 (i1 horizontal, k1 = k0 vertical) */
      function w(q) {
        if (P.wire === 'hoop') return [P.e + P.R * Math.sin(q), 0, P.hgt - P.R * Math.cos(q)];
        if (P.wire === 'parabola') return [q, 0, P.k * q * q];
        if (P.wire === 'chord') return [P.d, q, 0];
        if (P.wire === 'horizontal') return [q, 0, P.hgt];
        return [q * Math.cos(b), 0, P.hgt + q * Math.sin(b)];
      }
      var R1 = rot('z', S.psi), q = S.q, p1 = w(q), r = mv(R1, p1), e = P.extent, pts = [], i;
      var lo = P.wire === 'hoop' ? -Math.PI : P.qmin, hi = P.wire === 'hoop' ? Math.PI : P.qmax;
      for (i = 0; i <= 80; i++) pts.push(mv(R1, w(lo + (hi - lo) * i / 80)));
      var hh = 1e-4, t1 = mul(sub(w(q + hh), w(q - hh)), 1 / (2 * hh));
      var vrel = mv(R1, mul(t1, P.qdot)), om = [0, 0, P.Omega], vdrag = cross(om, r), acor = mul(cross(om, vrel), 2);
      sc.triad(O, I3, 0, 'm3-fixed', 0.55 * e);
      sc.triad(O, R1, 1, 'm3-b1', 0.5 * e);
      sc.line([0, 0, -0.2 * e], [0, 0, 0.9 * e], 'm3-dash');
      sc.poly(pts, 'm3-path');
      var foot = [r[0], r[1], 0];
      sc.line(foot, r, 'm3-dash'); sc.line(O, foot, 'm3-dash');
      sc.triangle(O, foot, X, '');
      sc.arrow(O, r, 'm3-r', 'r');
      var k = 0.35 * e;
      if (len(vrel) > 1e-9) sc.arrow(r, add(r, mul(unit(vrel), k)), 'm3-v', 'v_rel');
      if (len(vdrag) > 1e-9) sc.arrow(r, add(r, mul(unit(vdrag), k)), 'm3-acc', 'v_drag');
      if (len(acor) > 1e-9) sc.arrow(r, add(r, mul(unit(acor), 0.8 * k)), 'm3-w m3-mid', 'a_Cor');
      sc.dot(r, 'm3-p', 'P');
      var rots = [zRotation('psi', 'ψ', S.psi, 'ρ')];
      if (P.wire === 'hoop') {
        var Rq = rot('y', -q), c = mv(R1, [P.e, 0, P.hgt]);
        sc.dot(c, '', 'C');
        rots.push({ id: 'theta', sym: 'θ', angle: q, axis: mul(col(R1, 1), -1), axisLabel: '−j_1', u: mul(Z, -1), v: col(R1, 0),
          fixed: ['−k_1', 'i_1'], moved: ['e_r', 'e_θ'], m1: mv(R1, [Math.sin(q), 0, -Math.cos(q)]), m2: mv(R1, [Math.cos(q), 0, Math.sin(q)]),
          L: 'R', R: Rq, matLabel: '[_1R_2] =' });
      }
      var rho = Math.hypot(p1[0], p1[1]);
      return {
        rotations: rots, R: R1, omega: Z,
        vars: { psi: S.psi, q: q, rho: rho, x1: p1[0], y1: p1[1], z1: p1[2], x: r[0], y: r[1], z: r[2], vrel: len(vrel), vdrag: len(vdrag), acor: len(acor) },
        readouts: [['P in the rotating basis (m)', '(' + num(p1[0], 3) + ', ' + num(p1[1], 3) + ', ' + num(p1[2], 3) + ')'],
          ['P in the fixed basis (m)', '(' + num(r[0], 3) + ', ' + num(r[1], 3) + ', ' + num(r[2], 3) + ')'],
          ['Distance to the axis ρ (m)', num(rho, 3)], ['Drag speed Ωρ (m/s)', num(len(vdrag), 3)],
          ['Coriolis acceleration 2Ω × v_rel (m/s²)', num(len(acor), 3)]]
      };
    }
  };

  function oscillator(P, zeta, rr, t) {
    var wn = P.wn, x0 = P.x0, v0 = P.v0, del = P.delta, w = rr * wn, xp = 0, vp = 0, M = 0, ps = 0, res = false;
    if (P.mode === 'forced') {
      if (zeta < 1e-9 && Math.abs(1 - rr) < 1e-9) res = true;
      else {
        M = 1 / Math.sqrt(Math.pow(1 - rr * rr, 2) + Math.pow(2 * zeta * rr, 2)); ps = Math.atan2(2 * zeta * rr, 1 - rr * rr);
        xp = del * M * Math.cos(w * t - ps); vp = -del * M * w * Math.sin(w * t - ps);
        x0 = P.x0 - del * M * Math.cos(-ps); v0 = P.v0 + del * M * w * Math.sin(-ps);
      }
    }
    var xh, wd = 0, A = 0, ph = 0;
    if (zeta < 1) {
      wd = wn * Math.sqrt(1 - zeta * zeta);
      var B = (v0 + zeta * wn * x0) / wd, env = Math.exp(-zeta * wn * t);
      xh = env * (x0 * Math.cos(wd * t) + B * Math.sin(wd * t));
      A = Math.hypot(x0, B) * env; ph = wd * t - Math.atan2(B, x0);
    } else if (zeta === 1) {
      xh = (x0 + (v0 + wn * x0) * t) * Math.exp(-wn * t);
    } else {
      var q = wn * Math.sqrt(zeta * zeta - 1), s1 = -zeta * wn + q, s2 = -zeta * wn - q, C1 = (v0 - s2 * x0) / (s1 - s2);
      xh = C1 * Math.exp(s1 * t) + (x0 - C1) * Math.exp(s2 * t);
    }
    if (res) xh += del * wn * t / 2 * Math.sin(wn * t);
    return { x: xh + xp, wd: wd, A: A, ph: ph, M: M, psi: ps, X: del * M, res: res, w: w };
  }
  ARCH['oscillator-phase'] = {
    title: 'Oscillator and its phasor',
    view: 'front',
    params: { mode: 'free', wn: 2, zeta: 0.1, r: 0.8, x0: 1, v0: 0, delta: 0.5, tmax: 12, extent: 2.2 },
    controls: function (P) {
      var c = [slider('t', 'Time t (s)', 0, P.tmax, 1.2, P.tmax / 240), slider('zeta', 'Damping ratio ζ', 0, 2, P.zeta, 0.01)];
      if (P.mode === 'forced') c.push(slider('r', 'Frequency ratio ω/ω_n', 0, 3, P.r, 0.01));
      return c;
    },
    build: function (P, S, sc) {
      var o = oscillator(P, S.zeta, S.r == null ? P.r : S.r, S.t), e = P.extent, i, pts = [], x = o.x;
      var xw = -0.9 * e, zs = 0.45 * e, n = 12, sp = [[xw, 0, zs]];
      for (i = 1; i < n; i++) sp.push([xw + (x - 0.2 * e - xw) * i / n, 0, zs + (i % 2 ? 0.08 : -0.08) * e]);
      sp.push([x - 0.2 * e, 0, zs]);
      sc.line([xw, 0, zs - 0.3 * e], [xw, 0, zs + 0.3 * e], 'm3-thick');
      sc.poly(sp, 'm3-path');
      sc.poly([[x - 0.2 * e, 0, zs - 0.15 * e], [x + 0.2 * e, 0, zs - 0.15 * e], [x + 0.2 * e, 0, zs + 0.15 * e], [x - 0.2 * e, 0, zs + 0.15 * e]], 'm3-body m3-fill', true);
      sc.line([0, 0, zs - 0.28 * e], [0, 0, zs + 0.28 * e], 'm3-dash');
      sc.text([0, 0, zs + 0.36 * e], 'equilibrium');
      sc.arrow([0, 0, zs - 0.22 * e], [x, 0, zs - 0.22 * e], 'm3-r', 'x');
      /* trace x(t): time runs down the page */
      var tz = function (tt) { return 0.12 * e - 0.95 * e * tt / P.tmax; };
      for (i = 0; i <= 240; i++) { var tt = P.tmax * i / 240; pts.push([oscillator(P, S.zeta, S.r == null ? P.r : S.r, tt).x, 0, tz(tt)]); }
      sc.arrow([0, 0, 0.12 * e], [0, 0, -0.9 * e], 'm3-fixed', 't');
      sc.poly(pts, 'm3-v');
      sc.dot([x, 0, tz(S.t)], 'm3-p');
      var forced = P.mode === 'forced' && !o.res, amp = forced ? o.X : o.A, ang = forced ? o.w * S.t - o.psi : o.ph, R = rot('z', ang || 0);
      var rt = { id: 'phase', sym: forced ? '(ωt − ψ)' : 'φ', angle: ang || 0, axis: Z, axisLabel: 'the phase plane', caption: 'Rotating phasor: x is its horizontal projection', u: X, v: Y,
        fixed: ['x', 'y'], moved: [forced ? 'X' : 'A', 'A*'], m1: col(R, 0), m2: col(R, 1), L: forced ? 'X' : 'A', R: R, matLabel: 'phasor =' };
      var kind = S.zeta === 0 ? 'undamped' : S.zeta < 1 ? 'underdamped' : S.zeta === 1 ? 'critically damped' : 'overdamped';
      var out = [['Displacement x (m)', num(x, 4)], ['Regime', kind], ['Damped frequency ω_d (rad/s)', S.zeta < 1 ? num(o.wd, 4) : 'none (no oscillation)']];
      if (P.mode === 'forced') out.push(['Magnification M', o.res ? 'unbounded (resonance)' : num(o.M, 4)], ['Phase lag ψ (deg)', o.res ? '90' : num(o.psi / DEG, 2)]);
      else out.push(['Amplitude of the envelope (m)', S.zeta < 1 ? num(o.A, 4) : '–']);
      return { rotations: [rt], R: R, omega: Y, vars: { t: S.t, zeta: S.zeta, r: S.r == null ? P.r : S.r, x: x, wd: o.wd, A: o.A, M: o.M, psi: o.psi, X: o.X }, readouts: out };
    }
  };

  ARCH['rb-euler-kinematics'] = {
    title: 'Euler angles and angular velocity',
    params: { sequence: '313', shape: 'box', a: 1.2, b: 0.8, c: 0.4, R: 0.7, h: 1, L: 1.4, m: 1, psidot: 1, thetadot: 0, phidot: 2, px: 0.6, py: 0.4, pz: 0.2, extent: 1.5 },
    controls: function (P) {
      var n = P.sequence === '321' ? ['Yaw ψ', 'Pitch θ', 'Roll φ'] : ['Precession ψ', 'Nutation θ', 'Spin φ'];
      return [slider('psi', n[0], -180, 180, 40, 1, 'deg'), slider('theta', n[1], -90, 90, 30, 1, 'deg'), slider('phi', n[2], -180, 180, 50, 1, 'deg')];
    },
    build: function (P, S, sc) {
      var fr = eulerFrames(P.sequence, S.psi, S.theta, S.phi), e = P.extent;
      var om = add(mul(fr.axes[0], P.psidot), add(mul(fr.axes[1], P.thetadot), mul(fr.axes[2], P.phidot))), w = len(om);
      var Q = mv(fr.R3, [P.px, P.py, P.pz]), vQ = cross(om, Q);
      sc.triad(O, I3, 0, 'm3-fixed', 0.7 * e);
      sc.triad(O, fr.R3, 3, 'm3-b1', 0.6 * e);
      sc.arrow(O, mul(fr.axes[1], 0.5 * e), 'm3-dashv', P.sequence === '321' ? 'j_1' : 'i_1');
      drawShape(sc, P, fr.R3, O, 'm3-body');
      if (w > 1e-9) {
        var n = unit(om);
        sc.line(mul(n, -0.9 * e), mul(n, 0.9 * e), 'm3-iar');
        sc.arrow(O, mul(n, 0.75 * e), 'm3-w', 'ω');
        sc.text(mul(n, -0.95 * e), 'IAR');
      }
      sc.arrow(O, Q, 'm3-r', 'r');
      if (len(vQ) > 1e-9) sc.arrow(Q, add(Q, mul(unit(vQ), 0.4 * e)), 'm3-v', 'v');
      sc.dot(Q, 'm3-p', 'Q');
      var wb = mv(tr(fr.R3), om);
      return {
        rotations: eulerRotations(fr, [S.psi, S.theta, S.phi], ['ψ', 'θ', 'φ']), R: fr.R3, omega: w > 1e-9 ? om : Z,
        vars: { psi: S.psi, theta: S.theta, phi: S.phi, w: w, wx: om[0], wy: om[1], wz: om[2], w1: wb[0], w2: wb[1], w3: wb[2], vQ: len(vQ) },
        readouts: [['ω in the fixed basis (rad/s)', '(' + num(om[0], 3) + ', ' + num(om[1], 3) + ', ' + num(om[2], 3) + ')'],
          ['ω in the body basis (rad/s)', '(' + num(wb[0], 3) + ', ' + num(wb[1], 3) + ', ' + num(wb[2], 3) + ')'],
          ['|ω| (rad/s)', num(w, 3)], ['Speed of Q, |ω × r| (m/s)', num(len(vQ), 3)]]
      };
    }
  };

  ARCH['rb-inertia-principal'] = {
    title: 'Inertia tensor and principal axes',
    params: { shape: 'plate', m: 1, a: 1.2, b: 0.6, c: 0.4, R: 0.6, h: 1, L: 1.2, axis: 'z', dx: 0, dy: 0, dz: 0, extent: 1.1 },
    controls: function () { return [slider('alpha', 'Rotation of the axes α', -90, 90, 0, 1, 'deg')]; },
    build: function (P, S, sc) {
      var q = inertia(P), d = [P.dx, P.dy, P.dz], IO = steiner(q.I, P.m, d), R = rot(P.axis, S.alpha), e = P.extent;
      var IA = mm(tr(R), mm(IO, R)), eg = eigSym(IO), Gw = mul(d, -1), k = { x: 0, y: 1, z: 2 }[P.axis] || 2, p = [(k + 1) % 3, (k + 2) % 3];
      sc.triad(O, I3, 0, 'm3-fixed', 0.8 * e, ['x', 'y', 'z']);
      sc.triad(O, R, 1, 'm3-b1', 0.65 * e, ["x'", "y'", "z'"]);
      drawShape(sc, P, I3, Gw, 'm3-body');
      sc.dot(Gw, '', 'G');
      eg.vectors.forEach(function (v, i) { sc.line(mul(v, -0.9 * e), mul(v, 0.9 * e), 'm3-iar'); sc.text(mul(v, 0.98 * e), ['I', 'II', 'III'][i]); });
      /* principal angle about the chosen axis: direction, in the plane of the rotation, that cancels the product of inertia */
      var as = 0.5 * Math.atan2(2 * IO[p[0]][p[1]], IO[p[0]][p[0]] - IO[p[1]][p[1]]);
      var ax = [X, Y, Z], rt = { id: 'alpha', sym: 'α', angle: S.alpha, axis: ax[k], axisLabel: 'xyz'[k], u: ax[p[0]], v: ax[p[1]],
        fixed: ['xyz'[p[0]], 'xyz'[p[1]]], moved: ['xyz'[p[0]] + "'", 'xyz'[p[1]] + "'"], m1: col(R, p[0]), m2: col(R, p[1]), L: '1', R: R, matLabel: '[R] =' };
      return {
        rotations: [rt], R: R, omega: ax[k], tensor: IA,
        vars: { alpha: S.alpha, Ixx: IA[0][0], Iyy: IA[1][1], Izz: IA[2][2], Ixy: IA[0][1], Ixz: IA[0][2], Iyz: IA[1][2], I1: eg.values[0], I2: eg.values[1], I3: eg.values[2], alphap: as, xG: Gw[0], yG: Gw[1], zG: Gw[2] },
        readouts: [['Diagonal of the tensor in the rotated axes (kg m²)', '(' + num(IA[0][0], 4) + ', ' + num(IA[1][1], 4) + ', ' + num(IA[2][2], 4) + ')'],
          ['Off-diagonal terms (kg m²)', '(' + num(IA[0][1], 4) + ', ' + num(IA[0][2], 4) + ', ' + num(IA[1][2], 4) + ')'],
          ['Principal moments (kg m²)', '(' + num(eg.values[0], 4) + ', ' + num(eg.values[1], 4) + ', ' + num(eg.values[2], 4) + ')'],
          ['Principal angle about the axis (deg)', num(as / DEG, 2)], ['Trace, the same in every basis (kg m²)', num(IA[0][0] + IA[1][1] + IA[2][2], 4)]]
      };
    }
  };

  ARCH['rb-planar-dynamics'] = {
    title: 'Planar motion of a rigid body',
    view: 'top',
    params: { shape: 'bar', L: 1.2, a: 1, b: 0.6, R: 0.5, m: 1, px: null, py: 0, zero: 'down', thetadot: 1, slide: 0, gx: 0, gy: -1, extent: 1.5 },
    controls: function (P) {
      var c = [slider('theta', 'Angle θ', -180, 180, 35, 1, 'deg')];
      if (P.slide) c.push(slider('x', 'Position of the pivot x (m)', -P.slide, P.slide, 0, P.slide / 100));
      return c;
    },
    build: function (P, S, sc) {
      /* pivot A in body axes (origin at G); by default the end of the bar or the rim of the disk */
      var pa = [P.px == null ? (P.shape === 'bar' ? -P.L / 2 : P.shape === 'rect' ? -P.a / 2 : P.shape === 'triangle' ? -P.a / 3 : -P.R) : P.px, P.py, 0];
      var base = { down: -Math.PI / 2, up: Math.PI / 2, horizontal: 0 }[P.zero] || 0;
      /* angle that puts the line pivot -> G along the reference direction when theta = 0 */
      var off = base - Math.atan2(-pa[1], -pa[0]), R = rot('z', S.theta + off), e = P.extent;
      var A = [S.x || 0, 0, 0], G = sub(A, mv(R, pa)), om = [0, 0, P.thetadot], vG = cross(om, sub(G, A));
      sc.triad(O, I3, 0, 'm3-fixed', 0.6 * e);
      sc.poly(outline(P).map(function (p) { return add(G, mv(R, p)); }), 'm3-body' + (P.shape === 'bar' ? ' m3-thick' : ' m3-fill'), P.shape !== 'bar');
      sc.triad(G, R, 1, 'm3-b1', 0.4 * e);
      var ref = [Math.cos(base), Math.sin(base), 0];
      sc.line(A, add(A, mul(ref, 0.9 * e)), 'm3-dash');
      sc.triangle(A, G, ref, '');
      sc.arrow(A, G, 'm3-r', 'r');
      if (len(vG) > 1e-9) sc.arrow(G, add(G, mul(unit(vG), 0.4 * e)), 'm3-v', 'v_G');
      sc.arrow(G, add(G, mul(unit([P.gx, P.gy, 0]), 0.45 * e)), 'm3-w', 'mg');
      sc.dot(A, '', 'A'); sc.dot(G, 'm3-p', 'G');
      var Rf = rot('z', S.theta), rg = len(sub(G, A));
      var rt = { id: 'theta', sym: 'θ', angle: S.theta, axis: Z, axisLabel: 'k_0', u: ref, v: cross(Z, ref), fixed: { down: ['−j_0', 'i_0'], up: ['j_0', '−i_0'] }[P.zero] || ['i_0', 'j_0'], moved: ['e_r', 'e_θ'],
        m1: unit(sub(G, A)), m2: cross(Z, unit(sub(G, A))), L: 'd', R: Rf, matLabel: '[_0R_1] =' };
      return {
        rotations: [rt], R: Rf, omega: Z,
        vars: { theta: S.theta, x: S.x || 0, xG: G[0], yG: G[1], d: rg, vG: len(vG), thetadot: P.thetadot },
        readouts: [['Centre of mass G (m)', '(' + num(G[0], 3) + ', ' + num(G[1], 3) + ')'], ['Distance A to G, d (m)', num(rg, 3)],
          ['Speed of G, θ̇ d (m/s)', num(len(vG), 3)], ['Instantaneous centre', P.slide ? 'not at A (the pivot moves)' : 'the pivot A']]
      };
    }
  };

  ARCH['rb-rolling-contact'] = {
    title: 'Rolling contact',
    view: 'top',
    params: { surface: 'plane', shape: 'disk', r: 0.4, R: 1.2, beta: 0, e: 0, sdot: 1, smin: -1.5, smax: 1.5, slip: 0, extent: 1.8 },
    controls: function (P) {
      var c = [P.surface === 'plane' ? slider('s', 'Distance travelled s (m)', P.smin, P.smax, 0.5, (P.smax - P.smin) / 300)
        : slider('s', 'Position angle θ', -120, 120, 30, 1, 'deg')];
      if (P.slip) c.push(slider('phi', 'Spin angle φ (free, with slip)', -360, 360, 0, 1, 'deg'));
      return c;
    },
    build: function (P, S, sc) {
      var r = P.r, e = P.extent, b = P.beta * DEG, C, K, phi, n, sv = S.s, rots = [], pts = [], i, a;
      if (P.surface === 'plane') {
        var t = [Math.cos(b), -Math.sin(b), 0]; n = [Math.sin(b), Math.cos(b), 0];
        K = mul(t, sv); C = add(K, mul(n, r)); phi = -sv / r;
        sc.line(mul(t, -1.1 * e), mul(t, 1.1 * e), 'm3-thick');
      } else if (P.surface === 'outer') {
        n = [-Math.sin(sv), Math.cos(sv), 0]; K = mul(n, P.R); C = mul(n, P.R + r); phi = sv * (P.R + r) / r;
        sc.circle(O, X, Y, P.R, 'm3-thick');
      } else {
        n = [-Math.sin(sv), Math.cos(sv), 0]; n = mul(n, -1); K = mul(n, -P.R); C = mul(n, -(P.R - r)); phi = -sv * (P.R - r) / r;
        sc.circle(O, X, Y, P.R, 'm3-thick');
      }
      if (P.slip) phi = S.phi;
      var R = rot('z', phi), G = add(C, mv(R, [P.e, 0, 0]));
      for (i = 0; i <= 48; i++) { a = 2 * Math.PI * i / 48; pts.push(add(C, [r * Math.cos(a), r * Math.sin(a), 0])); }
      sc.triad(O, I3, 0, 'm3-fixed', 0.5 * e);
      sc.poly(pts, 'm3-body m3-fill', true);
      if (P.shape === 'sphere') sc.circle(C, X, Z, r, 'm3-body');
      sc.line(C, add(C, mv(R, [r, 0, 0])), 'm3-b1 m3-thick');
      sc.triad(C, R, 1, 'm3-b1', 0.75 * r);
      /* velocity field: the body turns about the contact point K when it does not slip */
      var rate = P.surface === 'plane' ? -P.sdot / r : phi / (sv || 1) * P.sdot, om = [0, 0, rate];
      var top = add(C, mul(sub(C, K), 1)), vC = cross(om, sub(C, K)), vT = cross(om, sub(top, K));
      if (!P.slip) {
        if (len(vC) > 1e-9) sc.arrow(C, add(C, mul(vC, 0.35 * e / (len(vT) || 1))), 'm3-v', 'v_C');
        if (len(vT) > 1e-9) sc.arrow(top, add(top, mul(vT, 0.35 * e / len(vT))), 'm3-v', '2v_C');
        sc.line(K, top, 'm3-dash');
      }
      sc.dot(K, 'm3-p', 'K'); sc.dot(C, '', 'C');
      if (P.e) sc.dot(G, 'm3-p', 'G');
      rots.push({ id: 'phi', sym: 'φ', angle: phi, axis: Z, axisLabel: 'k_0', u: X, v: Y, fixed: ['i_0', 'j_0'], moved: ['i_1', 'j_1'], m1: col(R, 0), m2: col(R, 1), L: 'r', R: R, matLabel: '[_0R_1] =' });
      if (P.surface !== 'plane') {
        var Rt = rot('z', sv);
        sc.line(O, C, 'm3-dash');
        rots.push({ id: 'theta', sym: 'θ', angle: sv, axis: Z, axisLabel: 'k_0', u: Y, v: mul(X, -1), fixed: ['j_0', '−i_0'], moved: ['e_n', 'e_t'],
          m1: mv(Rt, Y), m2: mv(Rt, mul(X, -1)), L: P.surface === 'outer' ? '(R + r)' : '(R − r)', R: Rt, matLabel: '[_0R_2] =' });
      }
      return {
        rotations: rots, R: R, omega: Z,
        vars: { s: sv, theta: sv, phi: phi, xC: C[0], yC: C[1], xG: G[0], yG: G[1], xK: K[0], yK: K[1], r: r, vC: len(vC) },
        readouts: [['Centre C (m)', '(' + num(C[0], 3) + ', ' + num(C[1], 3) + ')'], ['Contact point K (m)', '(' + num(K[0], 3) + ', ' + num(K[1], 3) + ')'],
          ['Spin angle φ (deg)', num(phi / DEG, 1)], ['Instantaneous axis of rotation', P.slip ? 'not through K (the body slips)' : 'through the contact point K, along k_0'],
          ['Rolling constraint', P.slip ? 'not imposed: φ is independent' : P.surface === 'plane' ? 'r φ = −s' : P.surface === 'outer' ? 'r φ = (R + r) θ' : 'r φ = −(R − r) θ'],
          ['Speed of C (m/s)', P.slip ? '–' : num(len(vC), 3)]]
      };
    }
  };

  ARCH['rb-gyro-multibody'] = {
    title: 'Rotor with precession, nutation and spin',
    params: { L: 1, a: 0.5, arm: 0, floor: 0, psidot: 0.5, thetadot: 0, phidot: 6, I3: 0.5, I1: 0.25, extent: 1.5 },
    controls: function () {
      return [slider('psi', 'Precession ψ', -180, 180, 30, 1, 'deg'), slider('theta', 'Nutation θ', 0, 180, 60, 1, 'deg'), slider('phi', 'Spin φ', -180, 180, 40, 1, 'deg')];
    },
    build: function (P, S, sc) {
      var fr = eulerFrames('313', S.psi, S.theta, S.phi), e = P.extent, k2 = col(fr.R2, 2);
      var A = mul(col(fr.R1, 0), P.arm), C = add(A, mul(k2, P.L));
      if (P.floor) { C[2] += P.a * Math.sin(S.theta) - C[2]; A = sub(C, mul(k2, P.L)); ground(sc, e); }
      var om = add(mul(Z, P.psidot), add(mul(col(fr.R1, 0), P.thetadot), mul(k2, P.phidot))), w = len(om);
      var w3 = dot(om, k2), wt = sub(om, mul(k2, w3)), H = add(mul(wt, P.I1), mul(k2, P.I3 * w3));
      sc.triad(O, I3, 0, 'm3-fixed', 0.7 * e);
      sc.triad(A, fr.R2, 2, 'm3-b1', 0.45 * e);
      if (P.arm) sc.line(O, A, 'm3-body m3-thick');
      sc.line(A, C, 'm3-body m3-thick');
      sc.circle(C, col(fr.R2, 0), col(fr.R2, 1), P.a, 'm3-body m3-fill', true);
      sc.line(C, add(C, mul(col(fr.R3, 0), P.a)), 'm3-b1 m3-thick');
      sc.line(O, [0, 0, 0.9 * e], 'm3-dash');
      sc.triangle(A, C, Z, '');
      if (w > 1e-9) { sc.arrow(A, add(A, mul(unit(om), 0.7 * e)), 'm3-w', 'ω'); sc.line(sub(A, mul(unit(om), 0.5 * e)), add(A, mul(unit(om), 0.9 * e)), 'm3-iar'); }
      if (len(H) > 1e-9) sc.arrow(A, add(A, mul(unit(H), 0.55 * e)), 'm3-acc', 'H');
      sc.dot(A, '', 'O'); sc.dot(C, 'm3-p', 'G');
      var rots = eulerRotations(fr, [S.psi, S.theta, S.phi], ['ψ', 'θ', 'φ']);
      return {
        rotations: rots, R: fr.R3, omega: w > 1e-9 ? om : Z,
        vars: { psi: S.psi, theta: S.theta, phi: S.phi, w: w, w3: w3, wt: len(wt), H: len(H), xG: C[0], yG: C[1], zG: C[2] },
        readouts: [['ω in the fixed basis (rad/s)', '(' + num(om[0], 3) + ', ' + num(om[1], 3) + ', ' + num(om[2], 3) + ')'],
          ['Axial rate ω · k_2 (rad/s)', num(w3, 3)], ['Transverse rate (rad/s)', num(len(wt), 3)],
          ['Angle between H and the axle (deg)', len(H) > 1e-9 ? num(Math.acos(Math.max(-1, Math.min(1, dot(unit(H), k2)))) / DEG, 2) : '–'],
          ['Height of G (m)', num(C[2], 3)]]
      };
    }
  };

  /* ------------------------------------------------------------------ one simulator */
  var uid = 0;
  function mount(root) {
    var name = root.getAttribute('data-archetype'), arch = ARCH[name];
    if (!arch) return;
    var cfg = {}, k;
    try { cfg = JSON.parse(root.getAttribute('data-config') || '{}') || {}; } catch (err) { cfg = {}; }
    var P = {};
    for (k in arch.params) P[k] = arch.params[k];
    for (k in cfg.params || {}) P[k] = cfg.params[k];
    var defs = arch.controls(P), S = {}, id = 'm3-' + (++uid);
    defs.forEach(function (d) {
      var o = (cfg.sliders || {})[d.id] || {};
      ['min', 'max', 'step', 'label'].forEach(function (f) { if (o[f] != null) d[f] = o[f]; });
      if (cfg.defaults && typeof cfg.defaults[d.id] === 'number') d.value = cfg.defaults[d.id];
      d.value = Math.max(d.min, Math.min(d.max, d.value));
    });
    var start = VIEWS[cfg.view] && cfg.view !== 'omega' ? cfg.view : (arch.view || 'iso');
    var cam = { az: VIEWS[start].az, el: VIEWS[start].el }, view = start, active = 0, last = null;
    var readoutDefs = (cfg.readouts || []).map(function (r) { return { label: r.label, f: compile(r.expr), unit: r.unit || '', digits: r.digits == null ? 3 : r.digits }; });
    var vecDefs = (cfg.vectors || []).map(function (v) { return { label: v.label, cls: v.cls || 'm3-w', at: (v.at || ['0', '0', '0']).map(compile), comp: v.comp.map(compile), scale: v.scale || 1 }; });

    root.textContent = '';
    root.classList.add('m3-ready');
    h('div', { 'class': 'm3-title' }, root, 'Geometry simulator: ' + (cfg.title || arch.title));
    h('p', { 'class': 'm3-intro' }, root, cfg.intro || 'Drag the left view to orbit it. The right view is the plane normal to the active rotation axis, with its right triangle and the change of basis matrix.');
    var fig = h('div', { 'class': 'm3-figure' }, root);
    var svg = s('svg', { viewBox: '0 0 760 360', 'class': 'm3-svg', role: 'img', tabindex: '0', 'aria-label': 'Axonometric view and fold-down view of the problem. Arrow keys orbit the camera.' }, fig);
    var panel = h('div', { 'class': 'm3-panel' }, root);
    var ctl = h('div', { 'class': 'm3-controls' }, panel);
    var out = h('dl', { 'class': 'm3-readouts', 'aria-live': 'off' }, panel);

    /* quick views */
    var vb = h('div', { 'class': 'm3-views', role: 'group', 'aria-label': 'Quick views of the camera' }, ctl), viewBtns = {};
    Object.keys(VIEWS).forEach(function (key) {
      var b = h('button', { type: 'button', 'class': 'm3-btn', 'aria-pressed': 'false', 'data-view': key }, vb, VIEWS[key].name);
      b.addEventListener('click', function () { setView(key); });
      viewBtns[key] = b;
    });
    function control(d, onInput) {
      var box = h('div', { 'class': 'm3-control' }, ctl), cid = id + '-' + d.id;
      var lab = h('label', { 'for': cid }, box, d.label + ': ');
      var o = h('output', { 'for': cid }, lab);
      var inp = h('input', { type: 'range', id: cid, min: d.min, max: d.max, step: d.step, value: d.value, 'aria-label': d.label, 'data-control': d.id }, box);
      function show() { o.textContent = num(parseFloat(inp.value), d.step < 1 ? 2 : 0) + (d.unit === 'deg' ? '°' : ''); }
      inp.addEventListener('input', function () { show(); onInput(parseFloat(inp.value)); });
      show();
      return { input: inp, show: show };
    }
    var camAz = control({ id: 'cam-az', label: 'Camera azimuth', min: -180, max: 180, step: 1, value: cam.az, unit: 'deg' }, function (v) { cam.az = v; view = null; draw(); });
    var camEl = control({ id: 'cam-el', label: 'Camera elevation', min: -90, max: 90, step: 1, value: Math.round(cam.el), unit: 'deg' }, function (v) { cam.el = v; view = null; draw(); });
    /* active rotation */
    var selBox = h('div', { 'class': 'm3-control' }, ctl);
    h('label', { 'for': id + '-rot' }, selBox, 'Rotation shown on the right');
    var sel = h('select', { id: id + '-rot', 'aria-label': 'Rotation shown in the fold-down view', 'data-control': 'rotation' }, selBox);
    sel.addEventListener('change', function () { active = sel.selectedIndex; if (view === 'omega') setView('omega'); else draw(); });
    defs.forEach(function (d) {
      S[d.id] = d.value;
      control(d, function (v) { S[d.id] = v; if (view === 'omega') setView('omega'); else draw(); });
    });

    function vals() { var o = {}; defs.forEach(function (d) { o[d.id] = d.unit === 'deg' ? S[d.id] * DEG : S[d.id]; }); return o; }
    function syncCam() {
      camAz.input.value = Math.round(cam.az); camEl.input.value = Math.round(cam.el); camAz.show(); camEl.show();
      Object.keys(viewBtns).forEach(function (key) { viewBtns[key].setAttribute('aria-pressed', key === view ? 'true' : 'false'); });
    }
    function setView(key) {
      view = key;
      if (key === 'omega') {
        var res = arch.build(P, vals(), new Scene()), rt = res.rotations[Math.min(active, res.rotations.length - 1)], n = unit(rt ? rt.axis : res.omega);
        cam.el = Math.asin(Math.max(-1, Math.min(1, n[2]))) / DEG;
        cam.az = Math.hypot(n[0], n[1]) < 1e-9 ? -90 : Math.atan2(n[1], n[0]) / DEG;
      } else { cam.az = VIEWS[key].az; cam.el = VIEWS[key].el; }
      draw();
    }

    function draw() {
      var sc = new Scene(), v = vals(), res = arch.build(P, v, sc), env = {}, key;
      for (key in P) if (typeof P[key] === 'number') env[key] = P[key];
      for (key in v) env[key] = v[key];
      for (key in res.vars) env[key] = res.vars[key];
      vecDefs.forEach(function (d) {
        var a = d.at.map(function (f) { return f(env); }), c = d.comp.map(function (f) { return f(env); });
        if (a.concat(c).every(isFinite) && len(c) > 1e-9) sc.arrow(a, add(a, mul(c, d.scale)), d.cls, d.label);
      });
      if (sel.options.length !== res.rotations.length) {
        sel.textContent = '';
        res.rotations.forEach(function (r) { h('option', {}, sel, r.caption ? r.sym : r.sym + ' about ' + r.axisLabel.replace(/_/g, '')); });
        active = Math.min(active, res.rotations.length - 1); sel.selectedIndex = active;
        selBox.style.display = res.rotations.length > 1 ? '' : 'none';
      }
      var rt = res.rotations[active];
      svg.textContent = '';
      s('rect', { x: 0, y: 0, width: 760, height: 360, 'class': 'm3-bg' }, svg);
      s('line', { x1: 450, y1: 12, x2: 450, y2: 348, 'class': 'm3-line m3-sep' }, svg);
      var clip = s('clipPath', { id: id + '-clip' }, svg);
      s('rect', { x: 0, y: 0, width: 448, height: 360 }, clip);
      var left = s('g', { 'class': 'm3-left', 'clip-path': 'url(#' + id + '-clip)' }, svg), right = s('g', { 'class': 'm3-right' }, svg);
      render(sc, camera(cam.az, cam.el), left, 225, 190, 150 / (P.extent || 1.5));
      label(left, 14, 22, view && VIEWS[view] ? VIEWS[view].name : 'Free view', 'start', 'm3-cap');
      foldPanel(right, rt);
      /* readouts: the formulas of the solution first, then the geometry */
      out.textContent = '';
      var rows = readoutDefs.map(function (d) { return [d.label, num(d.f(env), d.digits) + (d.unit ? ' ' + d.unit : '')]; }).concat(res.readouts);
      rows.push(['Angle ' + rt.sym + ' (deg)', num(rt.angle / DEG, 1)]);
      rows.push(['Check of the matrix', 'det = ' + num(det(rt.R), 3) + ', R Rᵀ = I']);
      rows.forEach(function (r) { h('dt', {}, out, r[0]); h('dd', {}, out, r[1]); });
      syncCam();
      last = { archetype: name, matrix: rt.R, total: res.R, tensor: res.tensor || null, angle: rt.angle, rotation: rt.id, cam: [cam.az, cam.el], view: view, vars: res.vars,
        readouts: rows.map(function (r) { return r[0] + ' = ' + r[1]; }) };
      root.setAttribute('data-state', JSON.stringify(last, function (kk, vv) { return typeof vv === 'number' ? (isFinite(vv) ? Math.round(vv * 1e9) / 1e9 : null) : vv; }));
    }

    /* orbit: pointer drag on the left view, arrow keys on the figure */
    var drag = null;
    svg.addEventListener('pointerdown', function (ev) {
      var box = svg.getBoundingClientRect();
      if ((ev.clientX - box.left) / box.width > 450 / 760) return;
      drag = { x: ev.clientX, y: ev.clientY, az: cam.az, el: cam.el };
      if (svg.setPointerCapture) { try { svg.setPointerCapture(ev.pointerId); } catch (err) { /* synthetic events have no capture */ } }
      ev.preventDefault();
    });
    svg.addEventListener('pointermove', function (ev) {
      if (!drag) return;
      cam.az = ((drag.az - (ev.clientX - drag.x) * 0.5 + 540) % 360) - 180;
      cam.el = Math.max(-90, Math.min(90, drag.el + (ev.clientY - drag.y) * 0.5));
      view = null; draw();
    });
    ['pointerup', 'pointercancel', 'pointerleave'].forEach(function (t) { svg.addEventListener(t, function () { drag = null; }); });
    svg.addEventListener('keydown', function (ev) {
      var d = { ArrowLeft: [-5, 0], ArrowRight: [5, 0], ArrowUp: [0, 5], ArrowDown: [0, -5] }[ev.key];
      if (!d || ev.ctrlKey || ev.altKey || ev.metaKey) return;
      cam.az = ((cam.az + d[0] + 540) % 360) - 180; cam.el = Math.max(-90, Math.min(90, cam.el + d[1]));
      view = null; draw(); ev.preventDefault();
    });

    draw();
  }

  function init() {
    var nodes = document.querySelectorAll('.m3-sim[data-archetype]'), i;
    for (i = 0; i < nodes.length; i++) {
      if (!nodes[i].classList.contains('m3-ready')) {
        try { mount(nodes[i]); } catch (err) { if (window.console) console.error('mechanics-3d-sim', err); }
      }
    }
  }

  window.AEMechanicsSim = { init: init, archetypes: Object.keys(ARCH), views: Object.keys(VIEWS) };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
