/*!
 * Aerospace Engineering Study Portal: Sideris inference engine (cloud worker + models installed on this computer).
 *
 * Loaded on study pages by assets/js/theme.js (after sideris-config.js, ai-models.js and ai-rag.js).
 * Skipped in PDF print mode (?print=...).
 *
 * Backends:
 *   - cloud  : instant streaming via the Cloudflare Worker (tools/cloudflare/sideris-worker.js),
 *              which runs on Cloudflare Workers AI.
 *   - webgpu : Transformers.js v4 (jsDelivr ESM) running a model installed on this computer by the
 *              automatic local section below; its files come from the resumable part cache.
 *   - mock   : test hook (setMock) used by tools/tests/test_ai_chat.py.
 *
 * API: window.AESiderisEngine = { hasWebGPU, isLoaded, loadedKey, loadWebGPU, generate, abort,
 *      clearBrowserCache, checkCloud, remaining, local, setMock }
 */
(function () {
  'use strict';

  if (window.AESiderisEngine) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var TFJS_URLS = [
    'https://cdn.jsdelivr.net/npm/@huggingface/transformers@4',
    'https://cdn.jsdelivr.net/npm/@huggingface/transformers@next'
  ];

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

  var tfModule = null;
  var loaded = null;          // { key, repo, dtype, generator, mod }
  var inflight = null;        // { key, promise } of the load in progress
  var activeAbort = null;     // { aborted: boolean, controller?: AbortController, stopper?: any }
  var mockFn = null;          // test hook: async (req, callbacks) -> string

  function hasWebGPU() {
    return typeof navigator !== 'undefined' && !!navigator.gpu;
  }

  function isLoaded(repo, dtype) {
    if (!loaded) return false;
    return loaded.key === (repo + '::' + (dtype || 'q4f16'));
  }

  function loadedKey() {
    return loaded ? loaded.key : '';
  }

  function loadTransformersLib() {
    if (tfModule) return Promise.resolve(tfModule);
    var idx = 0;
    function next(lastErr) {
      if (idx >= TFJS_URLS.length) {
        return Promise.reject(lastErr || new Error('Could not load Transformers.js runtime from CDN.'));
      }
      var url = TFJS_URLS[idx++];
      return import(url).then(function (mod) {
        tfModule = mod;
        if (mod.env) {
          mod.env.allowLocalModels = false;
          mod.env.useBrowserCache = true;
          // Model files come from the resumable part cache below (see modelCache), not one big fetch.
          if (typeof caches !== 'undefined') {
            mod.env.useCustomCache = true;
            mod.env.customCache = modelCache;
          }
        }
        return mod;
      }).catch(function (err) {
        return next(err);
      });
    }
    return next(null);
  }

  function loadWebGPU(opts, onProgress) {
    var repo = String((opts && opts.repo) || '').trim();
    var dtype = String((opts && opts.dtype) || 'q4f16').trim();
    if (!repo) return Promise.reject(new Error('No Hugging Face ONNX repository specified.'));
    var key = repo + '::' + dtype;
    if (loaded && loaded.key === key) {
      if (onProgress) onProgress({ status: 'ready', progress: 100, text: 'Model ready in GPU memory.' });
      return Promise.resolve(loaded);
    }
    if (mockFn) {
      if (onProgress) onProgress({ status: 'progress', progress: 50, text: 'Loading model (test mode)...' });
      loaded = { key: key, repo: repo, dtype: dtype, mock: true };
      if (onProgress) onProgress({ status: 'ready', progress: 100, text: 'Model ready.' });
      return Promise.resolve(loaded);
    }
    if (!hasWebGPU()) {
      return Promise.reject(new Error(
        'This browser does not expose WebGPU, so Sideris answers from the cloud here.'
      ));
    }

    var fileMap = Object.create(null);
    function emitProgress(info) {
      if (!onProgress || !info) return;
      if (info.file && typeof info.total === 'number' && info.total > 0) {
        fileMap[info.file] = { loaded: info.loaded || 0, total: info.total };
      }
      var sumLoaded = 0, sumTotal = 0;
      for (var k in fileMap) { sumLoaded += fileMap[k].loaded; sumTotal += fileMap[k].total; }
      var pct = sumTotal > 0
        ? Math.min(99, Math.round((sumLoaded / sumTotal) * 100))
        : (typeof info.progress === 'number' ? Math.round(info.progress) : 0);
      var mb = sumTotal > 0
        ? ' (' + (sumLoaded / 1048576).toFixed(0) + ' / ' + (sumTotal / 1048576).toFixed(0) + ' MB)'
        : '';
      var label = info.status === 'done' ? 'Preparing WebGPU kernels...'
        : info.file ? 'Downloading ' + info.file.split('/').pop() + mb
        : 'Initialising WebGPU runtime...';
      onProgress({ status: info.status || 'progress', progress: pct, text: label, bytesLoaded: sumLoaded, bytesTotal: sumTotal });
    }

    if (onProgress) onProgress({ status: 'init', progress: 2, text: 'Loading Transformers.js WebGPU runtime...' });

    if (inflight && inflight.key === key) return inflight.promise;   // a question during its own preload waits for it
    var promise = navigator.gpu.requestAdapter().then(function (adapter) {
      if (!adapter) {
        throw new Error('No WebGPU adapter found on this device, so Sideris answers from the cloud here.');
      }
      return loadTransformersLib();
    }).then(function (mod) {
      if (loaded && loaded.generator && typeof loaded.generator.dispose === 'function') {
        try { loaded.generator.dispose(); } catch (e) { /* ignore */ }
      }
      loaded = null;
      return mod.pipeline('text-generation', repo, {
        device: 'webgpu',
        dtype: dtype,
        progress_callback: emitProgress
      }).then(function (generator) {
        loaded = { key: key, repo: repo, dtype: dtype, generator: generator, mod: mod };
        if (onProgress) onProgress({ status: 'ready', progress: 100, text: 'Ready on this device.' });
        return loaded;
      });
    });
    inflight = { key: key, promise: promise };
    var clear = function () { if (inflight && inflight.promise === promise) inflight = null; };
    promise.then(clear, clear);
    return promise;
  }

  function generateWebGPU(req, onToken, onProgress) {
    var token = { aborted: false };
    activeAbort = token;
    return loadWebGPU(req.model, onProgress).then(function (entry) {
      if (token.aborted) return '';
      var mod = entry.mod;
      var gen = entry.generator;
      var full = '';
      var streamer = new mod.TextStreamer(gen.tokenizer, {
        skip_prompt: true,
        skip_special_tokens: true,
        callback_function: function (chunk) {
          if (token.aborted) return;
          full += chunk;
          if (onToken) onToken(chunk, full);
        }
      });

      var genOpts = {
        max_new_tokens: req.maxTokens || 1200,
        temperature: req.temperature != null ? req.temperature : 0.4,
        top_p: 0.9,
        do_sample: true,
        streamer: streamer
      };

      if (mod.InterruptableStoppingCriteria) {
        var stopper = new mod.InterruptableStoppingCriteria();
        token.stopper = stopper;
        genOpts.stopping_criteria = [stopper];
      }

      return gen(req.messages, genOpts).then(function (out) {
        if (!full && Array.isArray(out) && out[0] && out[0].generated_text) {
          var gt = out[0].generated_text;
          var last = Array.isArray(gt) ? gt[gt.length - 1] : null;
          full = last && typeof last.content === 'string' ? last.content : String(gt || '');
          if (onToken && full) onToken(full, full);
        }
        return full;
      });
    }).finally(function () {
      if (activeAbort === token) activeAbort = null;
    });
  }

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

  /* ---------------------------------------------------------------- automatic local models
     Device tiers: 0 = cloud only (phones, tablets, no WebGPU or shader-f16, data saver),
     1 = small models, 2 = mid-size models. Every model of ai-models.js with offlineBackend "webgpu"
     and a "localTier" up to the device tier is downloaded in the background, then probed (a short
     real generation), and from then on answers on the device: free, with no daily allowance.
     WebGPU limits only say a model may load, not that it will (phones with equal limits behave
     differently), hence the probe and the crash guard. */
  var LOCAL_KEY = 'ae_sideris_local';
  var GIB = 1073741824;
  var MIN_TOKENS_PER_SEC = 3;   // slower than this, an answer on the device is worse than the cloud
  var PROBE_V = 2;              // bump when the probe changes: "too slow" verdicts of an older probe are dropped
  var localState = parseLocal(readStore(LOCAL_KEY));   // { ready: {id: true}, failed: {id: why}, loading: id }
  var localJob = null;          // model being downloaded: { id, name, startedAt, loaded, total }
  var localTodo = [];           // models still to download, in order
  var localRunning = null;      // promise of the running startLocal(), shared by every caller
  var localTier = null;
  saveLocal();

  function readStore(key) {
    try { return JSON.parse(localStorage.getItem(key) || 'null'); } catch (e) { return null; }
  }

  function parseLocal(raw) {
    var st = raw && typeof raw === 'object' ? raw : {};
    st.ready = st.ready && typeof st.ready === 'object' ? st.ready : {};
    st.failed = st.failed && typeof st.failed === 'object' ? st.failed : {};
    // Crash guard: "loading" is cleared on success, on failure and on a normal page exit (pagehide),
    // so if it is still set the tab died while loading that model: never try it here again.
    if (st.loading) { st.failed[st.loading] = 'the tab closed while loading'; delete st.ready[st.loading]; }
    st.loading = '';
    if (st.probe !== PROBE_V) {
      for (var id in st.failed) if (/^too slow/.test(st.failed[id])) delete st.failed[id];
      st.probe = PROBE_V;
    }
    return st;
  }

  function saveLocal() {
    try { localStorage.setItem(LOCAL_KEY, JSON.stringify(localState)); } catch (e) { /* blocked */ }
  }

  // Diagnostic trail kept across pages (last 20 steps), read with AESiderisEngine.local.state().log:
  // a real computer can't be debugged from here, so it has to say what it did.
  function note(msg) {
    var d = new Date();
    localState.log = (localState.log || []).concat(d.toTimeString().slice(0, 8) + ' ' + msg).slice(-20);
    saveLocal();
  }

  window.addEventListener('pagehide', function () {
    if (localState.loading) { var id = localState.loading; localState.loading = ''; note(id + ': page left before it finished'); }
  });

  // shortcut: thresholds are estimates (1 GiB / 2 GiB buffers, 8 GB RAM); tune them with real devices.
  function classifyDevice(sig) {
    if (!sig.webgpu || !sig.f16 || sig.mobile || sig.saveData) return 0;
    var tier = sig.maxBuffer >= 2 * GIB ? 2 : sig.maxBuffer >= GIB ? 1 : 0;
    if (sig.memGB && sig.memGB < 8) tier = Math.min(tier, sig.memGB >= 4 ? 1 : 0);   // 0 = not reported
    return tier;
  }

  function detectDevice() {
    var ua = navigator.userAgent || '';
    var conn = navigator.connection || {};
    var sig = {
      webgpu: hasWebGPU(),
      f16: false,
      // iPadOS reports a Mac user agent: a touch screen gives it away
      mobile: /Android|iPhone|iPad|iPod|Mobile/i.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1),
      saveData: !!conn.saveData || /^(slow-2g|2g|3g)$/.test(conn.effectiveType || ''),
      memGB: navigator.deviceMemory || 0,
      maxBuffer: 0,
      freeMB: Infinity
    };
    if (!sig.webgpu || sig.mobile) return Promise.resolve(sig);
    return navigator.gpu.requestAdapter().then(function (a) {
      if (a) { sig.f16 = a.features.has('shader-f16'); sig.maxBuffer = a.limits.maxBufferSize || 0; }
    }).catch(function () {}).then(function () {
      return navigator.storage && navigator.storage.estimate ? navigator.storage.estimate() : null;
    }).then(function (est) {
      if (est && est.quota) sig.freeMB = (est.quota - (est.usage || 0)) / 1048576;
      return sig;
    }, function () { return sig; });
  }

  /* ---------------------------------------------------------------- resumable model files
     A model file (up to a few GB) is fetched in 32 MB ranges, each stored as it arrives in the
     Cache API ('sideris-models'): leaving the page loses at most the range in flight and the next
     page carries on from there. Transformers.js reads the files through env.customCache (match/put,
     checked in its v4 source), so once a model is complete its GPU load never touches the network,
     and a model whose file list is known downloads with no GPU work at all. */
  var CHUNK = 32 * 1048576;
  var MODEL_CACHE = 'sideris-models';
  var LEGACY_CACHE = 'transformers-cache';   // where Transformers.js kept files before this cache
  var FILES_KEY = 'ae_sideris_files';        // repo -> file URLs Transformers.js asked for
  var filesSeen = readStore(FILES_KEY) || {};
  var fetchFn = function (url, opts) { return fetch(url, opts); };   // test hook
  var store = typeof caches !== 'undefined' ? caches : null;          // test hook: the harness swaps in a memory store
  var dlProgress = null;                      // bytes callback of the running job

  function partKey(url, i) { return url + (url.indexOf('?') < 0 ? '?' : '&') + 'sideris_part=' + i; }
  function metaKey(url) { return url + (url.indexOf('?') < 0 ? '?' : '&') + 'sideris_meta=1'; }
  function openParts() { return store.open(MODEL_CACHE); }

  function readMeta(cache, url) {
    return cache.match(metaKey(url)).then(function (r) { return r ? r.json() : null; });
  }

  function writeMeta(cache, url, meta) {
    return cache.put(metaKey(url), new Response(JSON.stringify(meta))).then(function () { return meta; });
  }

  function repoOf(url) {
    var m = /^https?:\/\/[^/]+\/([^/]+\/[^/]+)\/resolve\//.exec(url);
    return m ? m[1] : '';
  }

  function remember(url) {
    var repo = repoOf(url);
    if (!repo) return;
    var list = filesSeen[repo] || (filesSeen[repo] = []);
    if (list.indexOf(url) < 0) {
      list.push(url);
      try { localStorage.setItem(FILES_KEY, JSON.stringify(filesSeen)); } catch (e) { /* blocked */ }
    }
  }

  // Stores a whole response as parts (Transformers.js put() and files kept by the old cache).
  function storeStream(url, res) {
    return openParts().then(function (cache) {
      var reader = res.body.getReader(), meta = { done: false, parts: 0, size: 0 }, buf = [], held = 0;
      function flush() {
        if (!held) return Promise.resolve();
        var part = new Uint8Array(held), off = 0;
        buf.forEach(function (b) { part.set(b, off); off += b.byteLength; });
        buf = []; held = 0;
        return cache.put(partKey(url, meta.parts), new Response(part)).then(function () { meta.parts++; meta.size += part.byteLength; });
      }
      function pump() {
        return reader.read().then(function (step) {
          if (step.done) return flush().then(function () { meta.done = true; return writeMeta(cache, url, meta); });
          buf.push(step.value); held += step.value.byteLength;
          return (held >= CHUNK ? flush() : Promise.resolve()).then(pump);
        });
      }
      return pump();
    });
  }

  // Completes url in the part cache, resuming after the last stored part. Resolves with its meta;
  // a file that does not exist (Transformers.js asks for optional ones) is stored as missing.
  function downloadFile(url) {
    return openParts().then(function (cache) {
      return readMeta(cache, url).then(function (meta) {
        if (meta && meta.done) return meta;
        if (!meta || !meta.parts) {
          // a file the old cache already holds is moved here instead of downloaded again
          var legacy = store.open(LEGACY_CACHE).then(function (c) {
            return c.match(url).then(function (r) {
              return r ? storeStream(url, r).then(function (m) { c.delete(url); return m; }) : null;
            });
          }).catch(function () { return null; });
          return legacy.then(function (m) { return m || fetchParts(cache, url, meta || { done: false, parts: 0, size: 0 }); });
        }
        return fetchParts(cache, url, meta);
      });
    });
  }

  function fetchParts(cache, url, meta) {
    var start = meta.size;
    return fetchFn(url, { headers: { Range: 'bytes=' + start + '-' + (start + CHUNK - 1) } }).then(function (res) {
      if (res.status === 404) return writeMeta(cache, url, { done: true, missing: true, parts: 0, size: 0 });
      if (res.status === 416) { meta.done = true; return writeMeta(cache, url, meta); }   // size was a whole number of parts
      if (!res.ok) throw new Error('HTTP ' + res.status + ' while downloading ' + url.split('/').pop());
      var whole = res.status === 200;   // the server ignored the range: the body is the whole file
      return res.arrayBuffer().then(function (data) {
        if (whole) { meta.parts = 0; meta.size = 0; }
        return cache.put(partKey(url, meta.parts), new Response(data)).then(function () {
          meta.parts++;
          meta.size += data.byteLength;
          if (dlProgress) dlProgress(data.byteLength);
          if (whole || data.byteLength < CHUNK) meta.done = true;
          return writeMeta(cache, url, meta);
        });
      });
    }).then(function (m) { return m.done ? m : fetchParts(cache, url, m); });
  }

  // The stored parts of a complete file, streamed back as one response.
  function partsResponse(url) {
    return openParts().then(function (cache) {
      return readMeta(cache, url).then(function (meta) {
        if (!meta || !meta.done || meta.missing) return undefined;
        var i = 0;
        var body = new ReadableStream({
          pull: function (ctrl) {
            if (i >= meta.parts) { ctrl.close(); return; }
            return cache.match(partKey(url, i++)).then(function (r) {
              if (!r) throw new Error('A stored part of ' + url.split('/').pop() + ' is missing.');
              return r.arrayBuffer();
            }).then(function (b) { ctrl.enqueue(new Uint8Array(b)); });
          }
        });
        return new Response(body, { headers: { 'content-length': String(meta.size) } });
      });
    });
  }

  var modelCache = {
    match: function (key) {
      var url = String((key && key.url) || key);
      if (!/^https?:\/\//.test(url)) return Promise.resolve(undefined);   // local paths: not ours
      remember(url);
      return downloadFile(url).then(function () { return partsResponse(url); })
        .catch(function () { return undefined; });   // network trouble: Transformers.js fetches it itself
    },
    put: function (key, res) {
      var url = String((key && key.url) || key);
      return res && res.body && /^https?:\/\//.test(url) ? storeStream(url, res).then(function () {}) : Promise.resolve();
    }
  };

  // The files of a model from the Hugging Face API (name and size): the config and tokenizer files
  // at the root and the ONNX files of its dtype (graph and external data). Anything else
  // Transformers.js asks for later still comes through the resumable cache.
  function listRepo(m) {
    var suffix = '_' + (m.dtype || 'q4f16') + '.onnx';
    return fetchFn('https://huggingface.co/api/models/' + m.repo + '/tree/main?recursive=1').then(function (r) {
      return r.ok ? r.json() : [];
    }).then(function (items) {
      return (Array.isArray(items) ? items : []).filter(function (it) {
        return it.type === 'file' && (/^[^/]+\.(json|jinja|txt)$/.test(it.path) || (/^onnx\//.test(it.path) && it.path.indexOf(suffix) >= 0));
      }).map(function (it) {
        return { url: 'https://huggingface.co/' + m.repo + '/resolve/main/' + it.path, size: (it.lfs && it.lfs.size) || it.size || 0 };
      });
    }).catch(function () { return []; });
  }

  // Downloads every file of a model with no GPU work; false when its files could not be listed
  // (then the GPU load asks Transformers.js for them, still through the resumable cache).
  function prefetchModel(m) {
    if (mockFn || typeof caches === 'undefined') return Promise.resolve(false);
    var urls;
    return listRepo(m).then(function (files) {
      files.forEach(function (f) { remember(f.url); });
      var total = files.reduce(function (a, f) { return a + f.size; }, 0);
      if (total && localJob) localJob.total = total;
      urls = filesSeen[m.repo] || [];
      return urls.length ? openParts().then(function (cache) {
        return Promise.all(urls.map(function (u) { return readMeta(cache, u); }));
      }) : [];
    }).then(function (metas) {
      if (!urls.length) return false;
      metas.forEach(function (x) { if (x && localJob) localJob.loaded += x.size || 0; });   // already stored
      return urls.reduce(function (chain, u) { return chain.then(function () { return downloadFile(u); }); }, Promise.resolve())
        .then(function () { return true; });
    });
  }

  // A model marked ready whose files the browser has since evicted (Safari does it after 7 days)
  // is downloaded again in the background instead of in front of the student.
  function verifyCached(models) {
    if (mockFn || typeof caches === 'undefined') return Promise.resolve();
    return openParts().then(function (cache) {
      return Promise.all(models.map(function (m) {
        if (!localState.ready[m.id]) return null;
        var urls = filesSeen[m.repo] || [];
        return Promise.all(urls.map(function (u) { return readMeta(cache, u); })).then(function (metas) {
          if (!urls.length || metas.some(function (x) { return !x || !x.done; })) {
            delete localState.ready[m.id];
            note(m.id + ': files no longer stored');
          }
        });
      }));
    }).then(saveLocal, function () {});
  }

  // The GPU part waits until Sideris is not answering, so two models never share the GPU.
  function waitIdle() {
    return new Promise(function (resolve) {
      (function poll() { if (!activeAbort) resolve(); else setTimeout(poll, 1500); })();
    });
  }

  // Tested on a real computer: the first WebGPU generation includes compiling the GPU kernels, so
  // timing it gave 1.4 tokens/s for a model that runs fine. Warm up first, then time only from the
  // first token to the last (decoding speed, what the student feels).
  function probe(m) {
    var model = { id: m.id, backend: 'webgpu', repo: m.repo, dtype: m.dtype };
    var ask = [{ role: 'user', content: 'Reply with one short sentence about fluids.' }];
    var n = 0, tFirst = 0, tLast = 0;
    return generate({ model: model, messages: ask, maxTokens: 4 }, function () {}).then(function () {
      return generate({ model: model, messages: ask, maxTokens: 24 }, function () {
        tLast = Date.now();
        if (!n++) tFirst = tLast;
      });
    }).then(function () {
      return n > 1 ? (n - 1) / Math.max(0.001, (tLast - tFirst) / 1000) : 0;
    });
  }

  function fetchOne(m) {
    localJob = { id: m.id, name: m.name, startedAt: Date.now(), loaded: 0, total: (m.sizeMB || 0) * 1048576, phase: 'download' };
    dlProgress = function (n) { if (localJob) { localJob.loaded += n; localJob.fetched = (localJob.fetched || 0) + n; } };
    note(m.id + ': downloading ' + m.repo);
    var t0 = Date.now();
    return prefetchModel(m).then(function (known) {
      if (known) note(m.id + ': files complete after ' + Math.round((Date.now() - t0) / 1000) + ' s');
      return waitIdle();
    }).then(function () {
      localJob.phase = 'gpu';   // from here other local models wait (busy())
      localState.loading = m.id;   // crash guard: only the GPU part can take the tab down
      note(m.id + ': loading into the GPU');
      t0 = Date.now();
      return loadWebGPU({ repo: m.repo, dtype: m.dtype, name: m.name, auto: true }, function () {});
    }).then(function () {
      note(m.id + ': in GPU after ' + Math.round((Date.now() - t0) / 1000) + ' s');
      return probe(m);
    }).then(function (tps) {
      note(m.id + ': probe ' + tps.toFixed(1) + ' tokens/s');
      if (tps < MIN_TOKENS_PER_SEC) localState.failed[m.id] = 'too slow on this device (' + tps.toFixed(1) + ' tokens/s)';
      else localState.ready[m.id] = true;
    }, function (err) {
      var msg = (err && err.message) || String(err);
      note(m.id + ': error ' + msg.slice(0, 160));
      // a dropped download is tried again on a later visit; anything else means this device can't
      if (!/fetch|network|load failed|abort|HTTP 5/i.test(msg)) localState.failed[m.id] = msg.slice(0, 120);
    }).then(function () {
      localState.loading = '';
      saveLocal();
      localJob = null;
      dlProgress = null;
    });
  }

  function startLocal(models, signals) {
    // an explicit request (signals given) runs after the automatic one instead of sharing its result
    if (localRunning) return signals ? localRunning.then(function () { return startLocal(models, signals); }) : localRunning;
    localRunning = (signals ? Promise.resolve(signals) : detectDevice()).then(function (sig) {
      localTier = classifyDevice(sig);
      note('tier ' + localTier + ' (webgpu ' + sig.webgpu + ', f16 ' + sig.f16 + ', mobile ' + sig.mobile + ', saveData ' + sig.saveData +
        ', mem ' + (sig.memGB || '?') + ' GB, maxBuffer ' + Math.round(sig.maxBuffer / 1048576) + ' MB, free ' +
        (isFinite(sig.freeMB) ? Math.round(sig.freeMB) + ' MB' : '?') + ')');
      var fit = (models || []).filter(function (m) {
        return m.offlineBackend === 'webgpu' && m.localTier && m.localTier <= localTier && !localState.failed[m.id];
      });
      return verifyCached(fit).then(function () {
        var room = sig.freeMB, todo = [];
        fit.forEach(function (m) {
          if (localState.ready[m.id]) return;
          var need = (m.sizeMB || 0) * 1.2;   // weights plus runtime files and some margin
          if (need <= room) { todo.push(m); room -= need; }
        });
        localTodo = todo;
        if (todo.length && navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
        var run = function () {
          return todo.reduce(function (chain, m) {
            return chain.then(function () { localTodo.shift(); return fetchOne(m); });
          }, Promise.resolve());
        };
        if (!todo.length) return null;
        // one tab downloads at a time; the others queue and take over when it closes
        return navigator.locks && navigator.locks.request && !signals ? navigator.locks.request('sideris-models', run) : run();
      });
    }).catch(function () {}).then(function () {
      localRunning = null;
      localJob = null;
      localTodo = [];
      return localTier;
    });
    return localRunning;
  }

  // Seconds until the next model on this device is ready, or null when nothing is coming or the
  // speed is unknown. Uses the speed of the running download, else the reported connection speed.
  function localEta() {
    var next = localJob || (localTodo[0] && { name: localTodo[0].name, loaded: 0, total: (localTodo[0].sizeMB || 0) * 1048576 });
    if (!next) return null;
    var rate = localJob && localJob.fetched > 0 ? localJob.fetched / Math.max(1, (Date.now() - localJob.startedAt) / 1000) : 0;
    if (!rate && navigator.connection && navigator.connection.downlink) rate = navigator.connection.downlink * 125000;   // Mbps -> bytes/s
    if (!rate) return null;
    return { seconds: Math.max(30, Math.round((next.total - next.loaded) / rate) + 20), name: next.name };   // +20 s GPU set-up and probe
  }

  function generate(req, onToken, onProgress) {
    if (mockFn) {
      var token = { aborted: false };
      activeAbort = token;
      return Promise.resolve().then(function () {
        return mockFn(req, {
          onToken: function (chunk, full) { if (!token.aborted && onToken) onToken(chunk, full); },
          onProgress: onProgress,
          isAborted: function () { return token.aborted; }
        });
      }).finally(function () {
        if (activeAbort === token) activeAbort = null;
      });
    }
    var backend = (req && req.model && req.model.backend) || 'webgpu';
    if (backend === 'cloud') return generateCloud(req, onToken);
    return generateWebGPU(req, onToken, onProgress);
  }

  function abort() {
    if (!activeAbort) return;
    activeAbort.aborted = true;
    if (activeAbort.controller) {
      try { activeAbort.controller.abort(); } catch (e) { /* ignore */ }
    }
    if (activeAbort.stopper && typeof activeAbort.stopper.interrupt === 'function') {
      try { activeAbort.stopper.interrupt(); } catch (e) { /* ignore */ }
    }
  }

  function clearBrowserCache() {
    loaded = null;
    localState.ready = {};
    saveLocal();
    filesSeen = {};
    try { localStorage.removeItem(FILES_KEY); } catch (e) { /* blocked */ }
    if (typeof caches === 'undefined') return Promise.resolve(0);
    return caches.keys().then(function (names) {
      var targets = names.filter(function (n) { return /transformers|huggingface|onnx|sideris/i.test(n); });
      return Promise.all(targets.map(function (n) { return caches.delete(n); })).then(function () {
        return targets.length;
      });
    });
  }

  function setMock(fn) {
    mockFn = typeof fn === 'function' ? fn : null;
  }

  window.AESiderisEngine = {
    hasWebGPU: hasWebGPU,
    isLoaded: isLoaded,
    loadedKey: loadedKey,
    loadWebGPU: loadWebGPU,
    generate: generate,
    abort: abort,
    clearBrowserCache: clearBrowserCache,
    checkCloud: checkCloud,
    remaining: function () { return lastRemaining; },
    local: {
      classify: classifyDevice,
      start: startLocal,
      isReady: function (id) { return !!localState.ready[id] && !localState.failed[id]; },
      busy: function () { return !!localJob && localJob.phase === 'gpu'; },   // downloads leave ready models usable
      eta: localEta,
      // Load an installed model into the GPU ahead of the first question (not while another loads).
      prewarm: function (m) {
        if (!localState.ready[m.id] || localJob && localJob.phase === 'gpu' || mockFn) return Promise.resolve();
        var t0 = Date.now();
        return waitIdle().then(function () {
          return loadWebGPU({ repo: m.repo, dtype: m.dtype, name: m.name, auto: true });
        }).then(function () { note(m.id + ': preloaded in ' + Math.round((Date.now() - t0) / 1000) + ' s'); },
          function (err) { note(m.id + ': preload error ' + String((err && err.message) || err).slice(0, 120)); });
      },
      log: note,
      markFailed: function (id, why) { delete localState.ready[id]; localState.failed[id] = String(why || 'error').slice(0, 120); saveLocal(); },
      state: function () { return { tier: localTier, job: localJob ? { id: localJob.id, phase: localJob.phase, loaded: localJob.loaded, total: localJob.total } : null, ready: Object.keys(localState.ready), failed: localState.failed, loading: localJob ? localJob.id + ' (' + localJob.phase + ', ' + Math.round(localJob.loaded / 1048576) + ' MB)' : '', log: localState.log || [] }; },
      cache: modelCache,
      _test: { setFetch: function (f) { fetchFn = f; }, setChunk: function (n) { CHUNK = n; }, setStore: function (st) { store = st; }, download: downloadFile,
        response: partsResponse, files: function () { return filesSeen; } },
      restore: function (raw) { localState = parseLocal(raw); saveLocal(); }   // test hook, same path as a page load
    },
    setMock: setMock
  };
})();
