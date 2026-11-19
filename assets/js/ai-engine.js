/*!
 * Aerospace Engineering Study Portal: Sideris inference engine (Cloud Worker + WebGPU ONNX + local Ollama).
 *
 * Loaded on study pages by assets/js/theme.js (after sideris-config.js, ai-models.js and ai-rag.js).
 * Skipped in PDF print mode (?print=...). Zero external network requests occur until the user
 * explicitly loads a model, tests a connection or sends a message.
 *
 * Backends:
 *   - cloud  : zero-download instant streaming via your free Cloudflare Worker
 *              (tools/cloudflare/sideris-worker.js), which runs on Cloudflare Workers AI.
 *   - webgpu : lazily imports @huggingface/transformers v4 from jsDelivr ESM CDN, streams ONNX
 *              weights from Hugging Face into browser Cache API / IndexedDB, and runs locally on
 *              the GPU with token streaming.
 *   - ollama : connects to an OpenAI-compatible local server (Ollama http://localhost:11434/v1 or
 *              LM Studio http://localhost:1234/v1) with SSE streaming.
 *   - mock   : test hook (setMock) used by tools/tests/test_ai_chat.py.
 *
 * API: window.AESiderisEngine = { hasWebGPU, isLoaded, loadedKey, loadWebGPU, generate,
 *      abort, clearBrowserCache, checkOllama, checkCloud, setMock }
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
  var activeAbort = null;     // { aborted: boolean, controller?: AbortController, stopper?: any }
  var confirmed = Object.create(null);   // models the student agreed to download on a small device
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
        'This browser does not expose WebGPU. Use Sideris Instant (zero download), Sideris Titan (Ollama), or open the prompt in Claude/Gemini.'
      ));
    }

    // 1.3-2.5 GB of weights in GPU memory is the usual reason a tab dies on phones and laptops
    // with integrated graphics: ask first there (deviceMemory is reported in GB, at most 8).
    var mem = navigator.deviceMemory || 0;
    var mobile = /Android|iPhone|iPad|Mobile/i.test(navigator.userAgent || '');
    if ((mobile || (mem && mem < 8)) && !confirmed[key] && !(opts && opts.auto)) {
      var size = (opts && opts.offlineSizeLabel) || 'over 1 GB';
      var ok = typeof window.confirm !== 'function' || window.confirm(
        'This device ' + (mem ? 'reports ' + mem + ' GB of memory' : 'looks like a phone or tablet') +
        '. Loading ' + ((opts && opts.name) || 'this model') + ' (' + size + ') into the browser (downloaded the first time) may close the tab. ' +
        'Instant mode (0 MB) works without a download. Load it anyway?'
      );
      if (!ok) return Promise.reject(new Error('Download cancelled. Switch Run mode to Instant (0 MB) to chat without downloading a model.'));
      confirmed[key] = true;
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

    return navigator.gpu.requestAdapter().then(function (adapter) {
      if (!adapter) {
        throw new Error('No WebGPU adapter found on this device. Switch to Sideris Instant or Sideris Titan (Ollama).');
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
        if (onProgress) onProgress({ status: 'ready', progress: 100, text: 'Ready (cached offline in browser).' });
        return loaded;
      });
    });
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
        'Instant cloud mode is not configured. Switch Run mode to Offline (WebGPU / Ollama).'
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
        throw new Error('Sideris has reached its daily limit. It will be back tomorrow; Offline mode still works.');
      }
      // The worker's own 429 messages (daily allowance, too many requests) are written for students.
      if (/HTTP 429: /.test(m)) throw new Error(m.replace(/^.*HTTP 429: /, ''));
      if (/HTTP 5\d\d/.test(m)) throw new Error('Sideris is temporarily unavailable. Please try again in a moment.');
      throw err;
    }).finally(function () {
      if (activeAbort === token) activeAbort = null;
    });
  }

  /* ---------------------------------------------------------------- Local Ollama / LM Studio */
  function normaliseEndpoint(ep) {
    var base = String(ep || 'http://localhost:11434/v1').trim().replace(/\/+$/, '');
    if (!/^https?:\/\//i.test(base)) base = 'http://' + base;
    return base;
  }

  function checkOllama(endpoint) {
    var base = normaliseEndpoint(endpoint);
    return fetch(base + '/models', { method: 'GET' }).then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    }).then(function (data) {
      var list = Array.isArray(data && data.data) ? data.data.map(function (m) { return m.id; }) : [];
      return { ok: true, models: list, endpoint: base };
    }).catch(function (err) {
      return { ok: false, error: err && err.message ? err.message : 'Unreachable', endpoint: base };
    });
  }

  function generateOllama(req, onToken) {
    var base = normaliseEndpoint(req.model && req.model.endpoint);
    var modelTag = String((req.model && req.model.repo) || 'qwen3.5:9b').trim();
    var ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
    var token = { aborted: false, controller: ctrl };
    activeAbort = token;

    return streamOpenAICompat(base + '/chat/completions', { 'Content-Type': 'application/json' }, {
      model: modelTag,
      messages: req.messages,
      temperature: req.temperature != null ? req.temperature : 0.4,
      max_tokens: req.maxTokens || 2048,
      stream: true
    }, onToken, token).catch(function (err) {
      if (token.aborted) return '';
      var msg = (err && err.message) || String(err);
      if (/failed to fetch|networkerror|load failed/i.test(msg)) {
        throw new Error(
          'Could not reach local server at ' + base + '. Start Ollama with CORS enabled: ' +
          'OLLAMA_ORIGINS="https://251-b.github.io,*" ollama serve (and run: ollama pull ' + modelTag + ').'
        );
      }
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

  // A model marked ready whose files the browser has since evicted (Safari does it after 7 days)
  // is downloaded again in the background instead of in front of the student.
  function verifyCached(models) {
    if (mockFn || typeof caches === 'undefined') return Promise.resolve();
    return caches.keys().then(function (names) {
      var name = names.filter(function (n) { return /transformers/i.test(n); })[0];
      return name ? caches.open(name).then(function (c) { return c.keys(); }) : [];
    }).then(function (reqs) {
      models.forEach(function (m) {
        var cached = reqs.some(function (r) { return r.url.indexOf(m.repo) >= 0; });
        if (localState.ready[m.id] && !cached) { delete localState.ready[m.id]; note(m.id + ': files no longer cached'); }
      });
      saveLocal();
    }).catch(function () {});
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
    localJob = { id: m.id, name: m.name, startedAt: Date.now(), loaded: 0, total: (m.sizeMB || 0) * 1048576 };
    localState.loading = m.id;
    note(m.id + ': loading ' + m.repo);
    var t0 = Date.now();
    return loadWebGPU({ repo: m.repo, dtype: m.dtype, name: m.name, auto: true }, function (p) {
      if (p && p.bytesLoaded) { localJob.loaded = p.bytesLoaded; if (p.bytesTotal) localJob.total = p.bytesTotal; }
    }).then(function () {
      note(m.id + ': in GPU after ' + Math.round((Date.now() - t0) / 1000) + ' s (' + Math.round(localJob.loaded / 1048576) + ' MB fetched)');
      return probe(m);
    }).then(function (tps) {
      note(m.id + ': probe ' + tps.toFixed(1) + ' tokens/s');
      if (tps < MIN_TOKENS_PER_SEC) localState.failed[m.id] = 'too slow on this device (' + tps.toFixed(1) + ' tokens/s)';
      else localState.ready[m.id] = true;
    }, function (err) {
      var msg = (err && err.message) || String(err);
      note(m.id + ': error ' + msg.slice(0, 160));
      // a dropped download is tried again on a later visit; anything else means this device can't
      if (!/fetch|network|load failed|abort/i.test(msg)) localState.failed[m.id] = msg.slice(0, 120);
    }).then(function () {
      localState.loading = '';
      saveLocal();
      localJob = null;
    });
  }

  function startLocal(models, signals) {
    if (localRunning) return localRunning;
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
        return todo.reduce(function (chain, m) {
          return chain.then(function () { localTodo.shift(); return fetchOne(m); });
        }, Promise.resolve());
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
    var rate = localJob && localJob.loaded > 0 ? localJob.loaded / Math.max(1, (Date.now() - localJob.startedAt) / 1000) : 0;
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
    if (backend === 'ollama') return generateOllama(req, onToken);
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
    checkOllama: checkOllama,
    checkCloud: checkCloud,
    remaining: function () { return lastRemaining; },
    local: {
      classify: classifyDevice,
      start: startLocal,
      isReady: function (id) { return !!localState.ready[id] && !localState.failed[id]; },
      busy: function () { return !!localJob; },
      eta: localEta,
      markFailed: function (id, why) { delete localState.ready[id]; localState.failed[id] = String(why || 'error').slice(0, 120); saveLocal(); },
      state: function () { return { tier: localTier, ready: Object.keys(localState.ready), failed: localState.failed, loading: localJob ? localJob.id : '', log: localState.log || [] }; },
      restore: function (raw) { localState = parseLocal(raw); saveLocal(); }   // test hook, same path as a page load
    },
    setMock: setMock
  };
})();
