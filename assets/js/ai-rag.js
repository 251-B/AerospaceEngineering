/*!
 * Aerospace Engineering Study Portal: client-side RAG retriever over vault/ shards.
 *
 * Loaded on every page by assets/js/theme.js (after assets/data/ai-models.js). Skipped in PDF
 * print mode (?print=...). Shards live under assets/data/ai-index/<subject>.json (built by
 * python tools/build_ai_index.py) and are fetched lazily ONLY when Sideris answers a question.
 *
 * Ranking: lightweight BM25 (k1=1.5, b=0.75) over normalised Spanish/English words + LaTeX
 * command tokens (\nabla, \omega, R_1, EBITDA...), boosted by title/heading match, current unit
 * and formula sheets.
 *
 * API: window.AESiderisRAG = { currentSubject, currentUnit, loadSubject, search, formatContext,
 *      setData, clearCache }
 */
(function () {
  'use strict';

  if (window.AESiderisRAG) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var INDEX_BASE = SCRIPT && SCRIPT.src
    ? SCRIPT.src.replace(/js\/ai-rag\.js(\?.*)?$/, 'data/ai-index/')
    : 'assets/data/ai-index/';

  var STOP = Object.create(null);
  (
    'the and for that this with from are was were have has had not but what all can will one two ' +
    'its into than then also only more most some such very how why when where which who whom whose ' +
    'los las del una uno unos unas por para con sin sobre entre desde hasta como cual cuales que ' +
    'este esta estos estas ese esa esos esas pero porque donde cuando quien quienes muy mas menos ' +
    'todo toda todos todas cada otro otra otros otras ser estar son esta estan hay tiene tienen'
  ).split(' ').forEach(function (w) { if (w) STOP[w] = 1; });

  var shards = Object.create(null);   // slug -> { chunks, df, avgdl, N }
  var pending = Object.create(null);  // slug -> Promise

  function currentSubject() {
    var m = location.pathname.match(/\/subjects\/([^/]+)\//);
    return m ? m[1] : '';
  }

  function currentUnit() {
    var f = location.pathname.split('/').pop() || '';
    var m = f.match(/(?:topic|unit)-0*(\d+)/i);
    return m ? parseInt(m[1], 10) : 0;
  }

  function normalise(str) {
    var s = String(str || '').toLowerCase();
    if (s.normalize) s = s.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    return s;
  }

  /* Extract both natural words and LaTeX macro / symbol tokens (\nabla, \tau, r_1, ebitda). */
  function tokenize(text) {
    var raw = normalise(text);
    var out = [];
    var m, re = /\\[a-z]+|[a-z0-9]+(?:_[a-z0-9]+)?/g;
    while ((m = re.exec(raw)) !== null) {
      var tok = m[0];
      if (tok.charAt(0) === '\\') {
        tok = tok.slice(1);
        if (tok.length >= 2 && tok !== 'text' && tok !== 'left' && tok !== 'right' && tok !== 'frac' && tok !== 'cdot') {
          out.push(tok);
        }
        continue;
      }
      if (tok.length < 2 || /^\d+$/.test(tok) || STOP[tok]) continue;
      out.push(tok);
    }
    return out;
  }

  function prepareShard(raw) {
    var chunks = Array.isArray(raw && raw.chunks) ? raw.chunks : [];
    var df = Object.create(null);
    var totalLen = 0;
    var prepared = chunks.map(function (c) {
      var bodyTokens = tokenize(c.x);
      var headTokens = tokenize((c.t || '') + ' ' + (c.h || ''));
      var tf = Object.create(null);
      var htf = Object.create(null);
      var seen = Object.create(null);
      for (var i = 0; i < bodyTokens.length; i++) {
        var t = bodyTokens[i];
        tf[t] = (tf[t] || 0) + 1;
        seen[t] = 1;
      }
      for (var j = 0; j < headTokens.length; j++) {
        var ht = headTokens[j];
        htf[ht] = (htf[ht] || 0) + 1;
        seen[ht] = 1;
      }
      for (var k in seen) df[k] = (df[k] || 0) + 1;
      var dl = Math.max(1, bodyTokens.length);
      totalLen += dl;
      return { raw: c, tf: tf, htf: htf, dl: dl };
    });
    return {
      subject: (raw && raw.subject) || '',
      label: (raw && raw.label) || '',
      chunks: prepared,
      df: df,
      avgdl: prepared.length ? totalLen / prepared.length : 1,
      N: prepared.length
    };
  }

  function setData(slug, raw) {
    if (!slug) return null;
    shards[slug] = prepareShard(raw);
    return shards[slug];
  }

  function loadSubject(slug) {
    if (!slug) return Promise.resolve(null);
    if (shards[slug]) return Promise.resolve(shards[slug]);
    if (pending[slug]) return pending[slug];
    var url = INDEX_BASE + encodeURIComponent(slug) + '.json';
    pending[slug] = fetch(url).then(function (res) {
      if (!res.ok) throw new Error('Could not load course notes index (' + res.status + ')');
      return res.json();
    }).then(function (data) {
      delete pending[slug];
      return setData(slug, data);
    }).catch(function (err) {
      delete pending[slug];
      throw err;
    });
    return pending[slug];
  }

  function inferSubjectFromQuery(q) {
    var s = normalise(q);
    if (/navier|stokes|bernoulli|reynolds|hydrostat|manometer|viscos|continuum|fluido|fluid/.test(s)) return 'fluid-mechanics';
    if (/miller|crystal|bragg|diffus|fick|disloc|martensit|austenit|semiconductor|band gap|material/.test(s)) return 'aerospace-materials-1';
    if (/coriolis|kinemat|euler|rigid body|change of basis|angular velocity|frenet|mecanic|mechanic/.test(s)) return 'engineering-mechanics';
    if (/wronsk|eigen|ode|edo|picard|integrating factor|laplace|bernoulli equation|phase portrait|math/.test(s)) return 'advanced-maths';
    if (/ebitda|ebit|balance sheet|income statement|cash flow|depreciation|amortization|business|empresa/.test(s)) return 'business-management';
    return '';
  }

  function scoreShard(shard, qTokens, unit) {
    if (!shard || !shard.N || !qTokens.length) return [];
    var k1 = 1.5, b = 0.75, N = shard.N, avgdl = shard.avgdl;
    var unique = [];
    var seen = Object.create(null);
    for (var i = 0; i < qTokens.length; i++) {
      if (!seen[qTokens[i]]) { seen[qTokens[i]] = 1; unique.push(qTokens[i]); }
    }
    var scored = [];
    for (var d = 0; d < N; d++) {
      var doc = shard.chunks[d];
      var s = 0;
      for (var j = 0; j < unique.length; j++) {
        var term = unique[j];
        var tf = doc.tf[term] || 0;
        var htf = doc.htf[term] || 0;
        if (!tf && !htf) continue;
        var df = shard.df[term] || 0;
        var idf = Math.log(1 + (N - df + 0.5) / (df + 0.5));
        if (tf) s += idf * ((tf * (k1 + 1)) / (tf + k1 * (1 - b + b * (doc.dl / avgdl))));
        if (htf) s += idf * 2.2;
      }
      if (s <= 0) continue;
      if (unit && doc.raw.u === unit) s *= 1.35;
      if (doc.raw.k === 'f') s *= 1.15;
      if (doc.raw.k === 't') s *= 1.08;
      scored.push({
        score: s,
        subject: shard.subject,
        label: shard.label,
        unit: doc.raw.u,
        kind: doc.raw.k,
        title: doc.raw.t,
        heading: doc.raw.h,
        text: doc.raw.x
      });
    }
    scored.sort(function (a, b) { return b.score - a.score; });
    return scored;
  }

  function search(query, opts) {
    opts = opts || {};
    var slug = opts.subject || currentSubject() || inferSubjectFromQuery(query);
    var unit = opts.unit != null ? opts.unit : currentUnit();
    var limit = opts.limit || 4;
    var qTokens = tokenize(query);
    if (!slug || !qTokens.length) return Promise.resolve([]);
    return loadSubject(slug).then(function (shard) {
      return scoreShard(shard, qTokens, unit).slice(0, limit);
    }).catch(function () {
      return [];
    });
  }

  function formatContext(hits, maxChars) {
    maxChars = maxChars || 3600;
    if (!hits || !hits.length) return '';
    var parts = ['[UC3M COURSE NOTES RETRIEVED FROM VAULT — GROUND YOUR NOTATION AND EQUATIONS HERE]'];
    var used = parts[0].length;
    for (var i = 0; i < hits.length; i++) {
      var h = hits[i];
      var head = '\n\n[' + (i + 1) + '] ' + h.title + (h.heading && h.heading !== h.title ? ' — ' + h.heading : '') +
        (h.unit ? ' (Unit ' + h.unit + ')' : '') + '\n';
      var avail = maxChars - used - head.length;
      if (avail < 120) break;
      var body = h.text.length > avail ? h.text.slice(0, avail - 1) + '…' : h.text;
      parts.push(head + body);
      used += head.length + body.length;
    }
    return parts.join('');
  }

  function clearCache() {
    shards = Object.create(null);
    pending = Object.create(null);
  }

  window.AESiderisRAG = {
    currentSubject: currentSubject,
    currentUnit: currentUnit,
    loadSubject: loadSubject,
    search: search,
    formatContext: formatContext,
    setData: setData,
    clearCache: clearCache
  };
})();
