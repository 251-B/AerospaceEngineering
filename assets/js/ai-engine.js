/*!
 * Aerospace Engineering Study Portal: Sideris inference engine (cloud worker only).
 *
 * Loaded on study pages by assets/js/theme.js (after sideris-config.js, ai-models.js and ai-rag.js).
 * Skipped in PDF print mode (?print=...).
 *
 * Backends:
 *   - cloud : streaming via the Cloudflare Worker (tools/cloudflare/sideris-worker.js), which runs on
 *             Cloudflare Workers AI. Nothing is downloaded to the device.
 *   - mock  : test hook (setMock) used by tools/tests/test_ai_chat.py.
 *
 * Models used to install themselves on computers (Transformers.js + WebGPU). It was dropped: reading a
 * question took tens of seconds on integrated GPUs, browsers evicted the 1.3-2.5 GB files, and few
 * devices could run the mid-size models. cleanupLocal() frees the space those downloads used.
 *
 * API: window.AESiderisEngine = { generate, abort, checkCloud, remaining, cleanupLocal, setMock }
 */
(function () {
  'use strict';

  if (window.AESiderisEngine) return;
  if (new URLSearchParams(location.search).has('print')) return;

  /* Anonymous id for the worker's daily allowance per student: random, kept in this browser only,
     never linked to an account. Without storage it lasts for the page. */
  var CLIENT_KEY = 'ae_sideris_client';
  var memClientId = '';
  var lastRemaining = null;   // X-Sideris-Remaining of the last answer (points left today)

  function clientId() {
    var id = '';
    try { id = localStorage.getItem(CLIENT_KEY) || ''; } catch (e) { /* blocked */ }
    if (/^[A-Za-z0-9-]{8,64}$/.test(id)) return id;
    id = memClientId || (window.crypto && crypto.randomUUID ? crypto.randomUUID()
      : 'c' + Date.now().toString(36) + Math.random().toString(36).slice(2, 12));
    memClientId = id;
    try { localStorage.setItem(CLIENT_KEY, id); } catch (e) { /* blocked */ }
    return id;
  }

  var activeAbort = null;     // { aborted: boolean, controller?: AbortController }
  var mockFn = null;          // test hook: async (req, callbacks) -> string

  /* ---------------------------------------------------------------- shared OpenAI SSE streamer */
  function streamOpenAICompat(url, headers, payload, onToken, token) {
    return fetch(url, {
      method: 'POST',
      headers: headers,
      signal: token.controller ? token.controller.signal : undefined,
      body: JSON.stringify(payload)
    }).then(function (res) {
      var left = res.headers && res.headers.get('X-Sideris-Remaining');
      if (left != null && left !== '') lastRemaining = parseInt(left, 10);
      if (!res.ok) {
        return res.text().then(function (txt) {
          var detail = '';
          try {
            var parsed = JSON.parse(txt);
            detail = (parsed && parsed.error && (parsed.error.message || parsed.error)) || '';
          } catch (e) { detail = txt ? txt.slice(0, 160) : ''; }
          throw new Error('Server returned HTTP ' + res.status + (detail ? ': ' + detail : ''));
        });
      }
      if (!res.body || !res.body.getReader) {
        return res.json().then(function (json) {
          var content = json && json.choices && json.choices[0] && json.choices[0].message && json.choices[0].message.content || '';
          if (onToken && content) onToken(content, content);
          return content;
        });
      }
      var reader = res.body.getReader();
      var decoder = new TextDecoder('utf-8');
      var buffer = '';
      var full = '';
      var inReason = false;

      function read() {
        return reader.read().then(function (step) {
          if (step.done || token.aborted) {
            if (inReason) { full += '</think>\n'; if (onToken) onToken('</think>\n', full); }
            return full;
          }
          buffer += decoder.decode(step.value, { stream: true });
          var lines = buffer.split(/\r?\n/);
          buffer = lines.pop() || '';
          for (var i = 0; i < lines.length; i++) {
            var line = lines[i].trim();
            if (!line || line.indexOf('data:') !== 0) continue;
            var chunkStr = line.slice(5).trim();
            if (chunkStr === '[DONE]') continue;
            try {
              var obj = JSON.parse(chunkStr);
              var delta = obj && obj.choices && obj.choices[0] && obj.choices[0].delta;
              var reason = (delta && (delta.reasoning_content || delta.reasoning)) || (obj && obj.reasoning_content) || '';
              var content = (delta && delta.content != null) ? delta.content : (obj && typeof obj.response === 'string' ? obj.response : '');
              if (!reason && !content) continue;
              var add = '';
              if (reason) {
                if (!inReason) { inReason = true; add += '<think>'; }
                add += reason;
              }
              if (content) {
                if (inReason) { inReason = false; add += '</think>\n'; }
                add += content;
              }
              if (add) {
                full += add;
                if (onToken) onToken(add, full);
              }
            } catch (e) { /* ignore partial chunk */ }
          }
          return read();
        });
      }
      return read();
    });
  }

  /* ---------------------------------------------------------------- Cloud (Sideris worker) */
  function normaliseBase(ep, fallback) {
    var base = String(ep || fallback || '').trim().replace(/\/+$/, '');
    if (base && !/^https?:\/\//i.test(base)) base = 'https://' + base;
    return base;
  }

  function checkCloud(workerUrl) {
    var base = normaliseBase(workerUrl, '');
    if (!base) return Promise.resolve({ ok: false, error: 'No Cloudflare Worker URL configured yet.' });
    return fetch(base + '/health', { method: 'GET' }).then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    }).then(function (data) {
      return {
        ok: !!(data && data.ok),
        providers: Array.isArray(data && data.providers) ? data.providers : [],
        endpoint: base
      };
    }).catch(function (err) {
      return { ok: false, error: err && err.message ? err.message : 'Unreachable', endpoint: base };
    });
  }

  function generateCloud(req, onToken) {
    var cloud = req.cloud || {};
    var ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
    var token = { aborted: false, controller: ctrl };
    activeAbort = token;

    var headers = { 'Content-Type': 'application/json' };
    var modelName = (req.model && req.model.id) || 'sideris-aether';

    if (!cloud.workerUrl || !cloud.workerUrl.trim()) {
      activeAbort = null;
      return Promise.reject(new Error(
        'The Sideris cloud is not configured (workerUrl in assets/data/sideris-config.js).'
      ));
    }
    var url = normaliseBase(cloud.workerUrl, '') + '/v1/chat/completions';

    var body = {
      model: modelName,
      messages: req.messages,
      temperature: req.temperature != null ? req.temperature : 0.35,
      max_tokens: req.maxTokens || 1600,
      stream: true,
      profile: modelName,
      client: clientId()   // in the body, not a header: a new header would fail CORS on an older worker
    };

    // A dropped connection before the first token (seen on the worker in testing, common on phones)
    // is retried once; after that the student gets a plain message and the Retry button.
    var gotToken = false;
    function relay(chunk, full) { gotToken = true; if (onToken) onToken(chunk, full); }
    function isNetwork(err) { return /failed to fetch|network ?error|load failed|network connection/i.test((err && err.message) || String(err)); }
    return streamOpenAICompat(url, headers, body, relay, token).catch(function (err) {
      if (token.aborted || gotToken || !isNetwork(err)) throw err;
      if (typeof AbortController !== 'undefined') token.controller = new AbortController();
      return new Promise(function (r) { setTimeout(r, 800); }).then(function () {
        if (token.aborted) return '';
        return streamOpenAICompat(url, headers, body, relay, token);
      });
    }).catch(function (err) {
      if (token.aborted) return '';
      if (isNetwork(err)) throw new Error('Could not reach the Sideris cloud (the connection dropped). Check your connection and press Retry.');
      // Never show provider details (quota, plan, model names) to students, even from an old worker.
      var m = (err && err.message) || '';
      if (/daily free allocation|\b4006\b|neurons/i.test(m)) {
        throw new Error('Sideris has reached its daily limit. It will be back tomorrow.');
      }
      // The worker's own 429 messages (daily allowance, too many requests) are written for students.
      if (/HTTP 429: /.test(m)) throw new Error(m.replace(/^.*HTTP 429: /, ''));
      if (/HTTP 5\d\d/.test(m)) throw new Error('Sideris is temporarily unavailable. Please try again in a moment.');
      throw err;
    }).finally(function () {
      if (activeAbort === token) activeAbort = null;
    });
  }

  /* ---------------------------------------------------------------- cleanup of the old local models
     Removes the model files and the keys the automatic installs left in this browser (once: the
     caches and keys are gone afterwards, so later pages do nothing). */
  var OLD_CACHES = /^(sideris-models|transformers-cache)$/;
  var OLD_KEYS = ['ae_sideris_local', 'ae_sideris_files'];

  function cleanupLocal() {
    OLD_KEYS.forEach(function (k) { try { localStorage.removeItem(k); } catch (e) { /* blocked */ } });
    if (typeof caches === 'undefined') return Promise.resolve(0);
    return caches.keys().then(function (names) {
      var old = names.filter(function (n) { return OLD_CACHES.test(n); });
      return Promise.all(old.map(function (n) { return caches.delete(n); })).then(function () { return old.length; });
    }).catch(function () { return 0; });
  }

  function generate(req, onToken) {
    if (mockFn) {
      var token = { aborted: false };
      activeAbort = token;
      return Promise.resolve().then(function () {
        return mockFn(req, {
          onToken: function (chunk, full) { if (!token.aborted && onToken) onToken(chunk, full); },
          isAborted: function () { return token.aborted; }
        });
      }).finally(function () {
        if (activeAbort === token) activeAbort = null;
      });
    }
    return generateCloud(req, onToken);
  }

  function abort() {
    if (!activeAbort) return;
    activeAbort.aborted = true;
    if (activeAbort.controller) {
      try { activeAbort.controller.abort(); } catch (e) { /* ignore */ }
    }
  }

  function setMock(fn) {
    mockFn = typeof fn === 'function' ? fn : null;
  }

  window.AESiderisEngine = {
    generate: generate,
    abort: abort,
    checkCloud: checkCloud,
    remaining: function () { return lastRemaining; },
    cleanupLocal: cleanupLocal,
    setMock: setMock
  };
})();
