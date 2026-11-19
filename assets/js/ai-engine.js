/*!
 * Aerospace Engineering Study Portal: Sideris inference engine (Cloud Worker/BYOK + WebGPU ONNX + local Ollama).
 *
 * Loaded on study pages by assets/js/theme.js (after sideris-config.js, ai-models.js and ai-rag.js).
 * Skipped in PDF print mode (?print=...). Zero external network requests occur until the user
 * explicitly loads a model, tests a connection or sends a message.
 *
 * Backends:
 *   - cloud  : zero-download instant streaming via your free Cloudflare Worker
 *              (tools/cloudflare/sideris-worker.js) OR direct user-supplied free key (BYOK:
 *              Google AI Studio Gemini Flash, Groq or OpenRouter).
 *   - webgpu : lazily imports @huggingface/transformers v4 from jsDelivr ESM CDN, streams ONNX
 *              weights from Hugging Face into browser Cache API / IndexedDB, and runs locally on
 *              the GPU with token streaming.
 *   - ollama : connects to an OpenAI-compatible local server (Ollama http://localhost:11434/v1 or
 *              LM Studio http://localhost:1234/v1) with SSE streaming.
 *   - mock   : test hook (setMock) used by tools/tests/test_ai_chat.py.
 *
 * API: window.AESiderisEngine = { hasWebGPU, isLoaded, loadedKey, loadWebGPU, generate,
 *      abort, clearBrowserCache, checkOllama, checkCloud, BYOK_PROVIDERS, setMock }
 */
(function () {
  'use strict';

  if (window.AESiderisEngine) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var TFJS_URLS = [
    'https://cdn.jsdelivr.net/npm/@huggingface/transformers@4',
    'https://cdn.jsdelivr.net/npm/@huggingface/transformers@next'
  ];

  var BYOK_PROVIDERS = {
    gemini: {
      label: 'Google AI Studio (Gemini Flash)',
      url: 'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions',
      model: 'gemini-3.8-flash'
    },
    groq: {
      label: 'Groq (Llama 3.3 70B)',
      url: 'https://api.groq.com/openai/v1/chat/completions',
      model: 'llama-3.3-70b-versatile'
    },
    openrouter: {
      label: 'OpenRouter (:free)',
      url: 'https://openrouter.ai/api/v1/chat/completions',
      model: 'openrouter/free'
    }
  };

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
    if ((mobile || (mem && mem < 8)) && !confirmed[key]) {
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
      onProgress({ status: info.status || 'progress', progress: pct, text: label });
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

  /* ---------------------------------------------------------------- Cloud (Worker + BYOK) */
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

    var url = '';
    var headers = { 'Content-Type': 'application/json' };
    var modelName = (req.model && req.model.id) || 'sideris-aether';

    if (cloud.byokKey && cloud.byokKey.trim()) {
      var prov = BYOK_PROVIDERS[cloud.byokProvider] || BYOK_PROVIDERS.gemini;
      url = prov.url;
      modelName = prov.model;
      headers.Authorization = 'Bearer ' + cloud.byokKey.trim();
      if (cloud.byokProvider === 'openrouter') {
        headers['HTTP-Referer'] = 'https://251-b.github.io/AerospaceEngineering/';
        headers['X-Title'] = 'Sideris Aerospace Study Portal';
      }
    } else if (cloud.workerUrl && cloud.workerUrl.trim()) {
      url = normaliseBase(cloud.workerUrl, '') + '/v1/chat/completions';
    } else {
      activeAbort = null;
      return Promise.reject(new Error(
        'Instant cloud mode is not configured. Switch Run mode to Offline (WebGPU / Ollama) or paste a free Gemini/Groq API key in Settings.'
      ));
    }

    var body = {
      model: modelName,
      messages: req.messages,
      temperature: req.temperature != null ? req.temperature : 0.35,
      max_tokens: req.maxTokens || 1600,
      stream: true
    };
    if (!(cloud.byokKey && cloud.byokKey.trim())) {
      body.profile = (req.model && req.model.id) || 'sideris-aether';
    }

    return streamOpenAICompat(url, headers, body, onToken, token).catch(function (err) {
      if (token.aborted) return '';
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
    BYOK_PROVIDERS: BYOK_PROVIDERS,
    setMock: setMock
  };
})();
