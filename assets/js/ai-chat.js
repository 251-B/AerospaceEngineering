/*!
 * Aerospace Engineering Study Portal: Sideris in-page AI tutor chat drawer.
 *
 * Loaded on every page by assets/js/theme.js (after ai-models.js, ai-rag.js, ai-engine.js;
 * no HTML page carries its own <script> tag). Adds its own stylesheet (assets/css/ai-chat.css).
 * Skipped in PDF print mode (?print=...) and hidden in @media print (print.css untouched).
 *
 * Features:
 *   - Four Sideris profiles: Sideris Lux (2B WebGPU), Sideris Aether (4B WebGPU, default),
 *     Sideris Orion (3.8B calculus WebGPU), Sideris Titan (9B local Ollama/LM Studio),
 *     plus custom Hugging Face ONNX repository or Ollama tag overrides.
 *   - Seamless handoff from assets/js/ask-ai.js: clean user bubble on screen while keeping
 *     <reference_solution hidden="true"> and structured engineering rules in system context.
 *   - Client-side RAG grounding over vault/ shards (assets/js/ai-rag.js).
 *   - Safe DOM-only Markdown + live KaTeX renderer ($...$, $$...$$) + collapsible <think> block.
 *
 * Storage: 'ae_sideris' (JSON prefs; never a key containing "theme"). Answer language synced
 *          with 'ae_ask_lang' ('es' | 'en').
 * API: window.AESideris = { KEY, open, close, isOpen, models, selectModel,
 *      openWithAskRequest, sendUserMessage, clearChat, renderRichText, state }
 */
(function () {
  'use strict';

  if (window.AESideris) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var KEY = 'ae_sideris';
  var LANG_KEY = 'ae_ask_lang';
  var MODELS = Array.isArray(window.AE_SIDERIS_MODELS) ? window.AE_SIDERIS_MODELS.slice() : [];

  var ICONS = {
    star: '<path fill="currentColor" stroke="none" d="M12 2l2.1 6.4L20.5 10.5l-6.4 2.1L12 19l-2.1-6.4L3.5 10.5l6.4-2.1z"/><path fill="currentColor" stroke="none" opacity=".7" d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    gear: '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33h.08a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51h.08a1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82v.08a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    close: '<path d="M18 6L6 18M6 6l12 12"/>'
  };

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function svg(inner, size) {
    var s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    s.setAttribute('viewBox', '0 0 24 24');
    s.setAttribute('width', size);
    s.setAttribute('height', size);
    s.setAttribute('aria-hidden', 'true');
    s.setAttribute('focusable', 'false');
    s.innerHTML = inner;
    return s;
  }

  function ensureStyles() {
    if (document.querySelector('link[data-sideris]')) return;
    var href = SCRIPT && SCRIPT.src ? SCRIPT.src.replace(/js\/ai-chat\.js(\?.*)?$/, 'css/ai-chat.css') : '';
    if (!href) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href;
    link.setAttribute('data-sideris', '');
    document.head.appendChild(link);
  }

  /* ---------------------------------------------------------------- state */
  function defaultModelId() {
    for (var i = 0; i < MODELS.length; i++) if (MODELS[i].default) return MODELS[i].id;
    return MODELS[0] ? MODELS[0].id : 'sideris-aether';
  }

  function findModel(id) {
    for (var i = 0; i < MODELS.length; i++) if (MODELS[i].id === id) return MODELS[i];
    return MODELS[0] || { id: 'sideris-aether', name: 'Sideris Aether', backend: 'webgpu', repo: 'onnx-community/Qwen3.5-4B-ONNX', dtype: 'q4f16', sizeLabel: '~2.5 GB' };
  }

  function readLang() {
    try { var v = localStorage.getItem(LANG_KEY); if (v === 'es' || v === 'en') return v; } catch (e) { /* blocked */ }
    return 'es';
  }

  function writeLang(v) {
    try { localStorage.setItem(LANG_KEY, v); } catch (e) { /* blocked */ }
  }

  function loadPrefs() {
    var base = {
      modelId: defaultModelId(),
      runMode: 'instant',       // 'instant' (0 MB cloud proxy) | 'offline' (WebGPU / Ollama)
      rag: true,
      thinking: true,
      customRepo: '',
      workerUrl: '',
      byokProvider: 'gemini',
      byokKey: '',
      ollamaEndpoint: 'http://localhost:11434/v1',
      ollamaModel: 'qwen3.5:9b'
    };
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return base;
      var parsed = JSON.parse(raw);
      if (parsed && typeof parsed === 'object') {
        if (typeof parsed.modelId === 'string') base.modelId = parsed.modelId;
        if (parsed.runMode === 'instant' || parsed.runMode === 'offline') base.runMode = parsed.runMode;
        if (typeof parsed.rag === 'boolean') base.rag = parsed.rag;
        if (typeof parsed.thinking === 'boolean') base.thinking = parsed.thinking;
        if (typeof parsed.customRepo === 'string') base.customRepo = parsed.customRepo;
        if (typeof parsed.workerUrl === 'string') base.workerUrl = parsed.workerUrl;
        if (typeof parsed.byokProvider === 'string') base.byokProvider = parsed.byokProvider;
        if (typeof parsed.byokKey === 'string') base.byokKey = parsed.byokKey;
        if (typeof parsed.ollamaEndpoint === 'string' && parsed.ollamaEndpoint.trim()) base.ollamaEndpoint = parsed.ollamaEndpoint;
        if (typeof parsed.ollamaModel === 'string' && parsed.ollamaModel.trim()) base.ollamaModel = parsed.ollamaModel;
      }
    } catch (e) { /* ignore corrupted storage */ }
    return base;
  }

  function effectiveWorkerUrl() {
    var cfg = window.AE_SIDERIS_CONFIG && typeof window.AE_SIDERIS_CONFIG.workerUrl === 'string'
      ? window.AE_SIDERIS_CONFIG.workerUrl.trim()
      : '';
    return (prefs.workerUrl && prefs.workerUrl.trim()) || cfg;
  }

  function savePrefs() {
    try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (e) { /* blocked */ }
  }

  var prefs = loadPrefs();
  var session = {
    open: false,
    settingsOpen: false,
    busy: false,
    messages: [],          // { role: 'user'|'assistant', text, displayText, tag, ragHits, error }
    systemExtra: '',       // hidden context from ask-ai.js (e.g. <reference_solution hidden="true">)
    socratic: false,
    lastFocus: null
  };
  var ui = {};

  function activeModelConfig() {
    var base = findModel(prefs.modelId);
    var copy = {};
    for (var k in base) copy[k] = base[k];
    if (prefs.runMode === 'offline') {
      copy.backend = copy.offlineBackend || 'webgpu';
      copy.sizeLabel = copy.offlineSizeLabel || copy.sizeLabel;
    } else {
      copy.backend = 'cloud';
      copy.sizeLabel = '0 MB · Instant';
    }
    if (copy.backend === 'ollama') {
      copy.endpoint = prefs.ollamaEndpoint || copy.endpoint || 'http://localhost:11434/v1';
      copy.repo = prefs.ollamaModel || copy.repo || 'qwen3.5:9b';
    } else if (copy.backend === 'webgpu' && prefs.customRepo && prefs.customRepo.trim()) {
      copy.repo = prefs.customRepo.trim();
    }
    return copy;
  }

  /* ---------------------------------------------------------------- safe Markdown + KaTeX renderer */
  function renderMathSpan(tex, display) {
    var span = el(display ? 'div' : 'span', display ? 'sd-math-block' : 'sd-math-inline');
    if (window.katex && typeof window.katex.render === 'function') {
      try {
        window.katex.render(tex, span, { displayMode: !!display, throwOnError: false, strict: 'ignore' });
        return span;
      } catch (e) { /* fall through */ }
    }
    span.textContent = display ? '$$' + tex + '$$' : '$' + tex + '$';
    return span;
  }

  function appendInline(parent, text) {
    // Matches display/inline math ($...$, \(...\)), inline code (`...`), bold (**...**), italic (*...*).
    var re = /(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$(?!\s)([^$\n]+?)(?!\s)\$|`([^`\n]+)`|\*\*([^*\n]+)\*\*|\*([^*\n]+)\*)/g;
    var last = 0, m;
    while ((m = re.exec(text)) !== null) {
      if (m.index > last) parent.appendChild(document.createTextNode(text.slice(last, m.index)));
      var tok = m[0];
      if (tok.indexOf('$$') === 0) {
        parent.appendChild(renderMathSpan(tok.slice(2, -2).trim(), true));
      } else if (tok.indexOf('\\[') === 0) {
        parent.appendChild(renderMathSpan(tok.slice(2, -2).trim(), true));
      } else if (tok.indexOf('\\(') === 0) {
        parent.appendChild(renderMathSpan(tok.slice(2, -2).trim(), false));
      } else if (m[2] != null) {
        parent.appendChild(renderMathSpan(m[2].trim(), false));
      } else if (m[3] != null) {
        parent.appendChild(el('code', '', m[3]));
      } else if (m[4] != null) {
        var strong = el('strong');
        appendInline(strong, m[4]);
        parent.appendChild(strong);
      } else if (m[5] != null) {
        var em = el('em');
        appendInline(em, m[5]);
        parent.appendChild(em);
      }
      last = re.lastIndex;
    }
    if (last < text.length) parent.appendChild(document.createTextNode(text.slice(last)));
  }

  function splitThinking(raw) {
    var text = String(raw || '');
    var open = text.indexOf('<think>');
    if (open < 0) return { think: '', answer: text, thinking: false };
    var close = text.indexOf('</think>', open + 7);
    if (close < 0) {
      return { think: text.slice(open + 7).trim(), answer: text.slice(0, open).trim(), thinking: true };
    }
    var think = text.slice(open + 7, close).trim();
    var answer = (text.slice(0, open) + text.slice(close + 8)).trim();
    return { think: think, answer: answer, thinking: false };
  }

  function renderMarkdownBlocks(container, text) {
    var lines = String(text || '').replace(/\r\n/g, '\n').split('\n');
    var i = 0;
    while (i < lines.length) {
      var line = lines[i];
      if (!line.trim()) { i++; continue; }

      // Fenced code block
      if (/^```/.test(line.trim())) {
        var codeLines = [];
        i++;
        while (i < lines.length && !/^```/.test(lines[i].trim())) { codeLines.push(lines[i]); i++; }
        if (i < lines.length) i++;
        var pre = el('pre');
        pre.appendChild(el('code', '', codeLines.join('\n')));
        container.appendChild(pre);
        continue;
      }

      // Multi-line display math $$...$$ or \[...\]
      if (/^\s*(\$\$|\\\[)/.test(line)) {
        var isDollar = line.trim().indexOf('$$') === 0;
        var openTok = isDollar ? '$$' : '\\[';
        var closeTok = isDollar ? '$$' : '\\]';
        var trimmed = line.trim();
        if (trimmed.length > openTok.length + closeTok.length && trimmed.slice(-closeTok.length) === closeTok) {
          container.appendChild(renderMathSpan(trimmed.slice(openTok.length, -closeTok.length).trim(), true));
          i++;
          continue;
        }
        var mathLines = [trimmed.slice(openTok.length)];
        i++;
        while (i < lines.length) {
          var idx = lines[i].indexOf(closeTok);
          if (idx >= 0) { mathLines.push(lines[i].slice(0, idx)); i++; break; }
          mathLines.push(lines[i]);
          i++;
        }
        container.appendChild(renderMathSpan(mathLines.join('\n').trim(), true));
        continue;
      }

      // Heading
      var hm = /^(#{1,4})\s+(.+)$/.exec(line.trim());
      if (hm) {
        var h = el(hm[1].length <= 2 ? 'h3' : 'h4');
        appendInline(h, hm[2]);
        container.appendChild(h);
        i++;
        continue;
      }

      // Unordered list
      if (/^\s*[-*]\s+/.test(line)) {
        var ul = el('ul');
        while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
          var li = el('li');
          appendInline(li, lines[i].replace(/^\s*[-*]\s+/, ''));
          ul.appendChild(li);
          i++;
        }
        container.appendChild(ul);
        continue;
      }

      // Ordered list
      if (/^\s*\d+[.)]\s+/.test(line)) {
        var ol = el('ol');
        while (i < lines.length && /^\s*\d+[.)]\s+/.test(lines[i])) {
          var oli = el('li');
          appendInline(oli, lines[i].replace(/^\s*\d+[.)]\s+/, ''));
          ol.appendChild(oli);
          i++;
        }
        container.appendChild(ol);
        continue;
      }

      // Paragraph
      var para = [];
      while (i < lines.length && lines[i].trim() && !/^(```|#{1,4}\s|\s*[-*]\s+|\s*\d+[.)]\s+|\s*\$\$|\s*\\\[)/.test(lines[i])) {
        para.push(lines[i]);
        i++;
      }
      var p = el('p');
      appendInline(p, para.join(' '));
      container.appendChild(p);
    }
  }

  function renderRichText(container, rawText) {
    container.textContent = '';
    var parts = splitThinking(rawText);
    if (parts.think) {
      var det = el('details', 'sd-think');
      if (parts.thinking) det.open = true;
      det.appendChild(el('summary', '', parts.thinking ? 'Reasoning...' : 'Show reasoning'));
      det.appendChild(el('div', 'sd-think__body', parts.think));
      container.appendChild(det);
    }
    var body = el('div', 'sd-msg__body');
    if (parts.answer) {
      renderMarkdownBlocks(body, parts.answer);
    } else if (parts.thinking) {
      body.appendChild(el('p', '', 'Thinking through the steps...'));
    }
    container.appendChild(body);
  }

  /* ---------------------------------------------------------------- system prompt & RAG */
  function pageTitle() {
    var h1 = document.querySelector('h1');
    return ((h1 ? h1.textContent : document.title) || '').replace(/\s+/g, ' ').trim();
  }

  function buildSystemPrompt(ragText, lang) {
    var slug = window.AESiderisRAG ? window.AESiderisRAG.currentSubject() : '';
    var business = slug === 'business-management';
    var lines = [
      'You are Sideris, the dedicated engineering study tutor for the 2nd year of the BSc in Aerospace Engineering at UC3M.',
      'Current page: ' + pageTitle() + (slug ? ' (subject: ' + slug + ')' : '') + '.',
      'Rules:',
      '- Never skip algebraic or numerical steps. Write out the chain rule, product rule, substitutions with differentials, antiderivatives and Barrow limits explicitly.',
      '- Justify each step with the law, assumption, definition or course equation used.',
      business
        ? '- Show every accounting entry, subtotal (EBITDA, EBIT, EBT, Net Income) and balance sheet classification.'
        : '- Define every symbol with its SI unit on first use and include a dimensional check.',
      '- Write all equations in KaTeX-compatible LaTeX: $...$ inline and $$...$$ for display equations. Never use \\euro (write € inside \\text{}).',
      '- Stay faithful to the UC3M course notation and sign conventions from the course notes below. Mark anything beyond the syllabus as "Extension".',
      lang === 'es'
        ? '- Answer in Spanish. On first mention of a technical term from the English notes, write it in Spanish with the English term in brackets.'
        : '- Answer in English.'
    ];
    if (session.socratic) {
      lines.push('- SOCRATIC MODE IS ACTIVE: never reveal the final solution or the next full step unless the student writes "show solution". Ask one short guiding question at a time.');
    }
    if (!prefs.thinking) {
      lines.push('/no_think');
    }
    if (session.systemExtra) {
      lines.push('', session.systemExtra);
    }
    if (ragText) {
      lines.push('', ragText);
    }
    return lines.join('\n');
  }

  /* ---------------------------------------------------------------- UI */
  function buildUI() {
    ensureStyles();

    var launcher = el('button', 'sd-launcher');
    launcher.type = 'button';
    launcher.id = 'siderisButton';
    launcher.setAttribute('aria-haspopup', 'dialog');
    launcher.setAttribute('aria-expanded', 'false');
    launcher.setAttribute('aria-controls', 'siderisDrawer');
    launcher.setAttribute('aria-label', 'Open Sideris AI tutor');
    launcher.title = 'Sideris AI tutor';
    launcher.appendChild(svg(ICONS.star, 15));
    launcher.appendChild(el('span', 'sd-launcher__label', 'Sideris'));

    var backdrop = el('div', 'sd-backdrop');
    backdrop.hidden = true;

    var drawer = el('aside', 'sd-drawer');
    drawer.id = 'siderisDrawer';
    drawer.hidden = true;
    drawer.setAttribute('role', 'dialog');
    drawer.setAttribute('aria-modal', 'false');
    drawer.setAttribute('aria-labelledby', 'siderisTitle');

    // Header
    var head = el('div', 'sd-head');
    var headLeft = el('div', 'sd-head__left');
    headLeft.appendChild(el('p', 'sd-kicker', 'Free In-Page Tutor'));
    var titleRow = el('div', 'sd-title-row');
    var title = el('h2', 'sd-title', 'Sideris');
    title.id = 'siderisTitle';
    var modelPill = el('span', 'sd-model-pill');
    titleRow.appendChild(title);
    titleRow.appendChild(modelPill);
    headLeft.appendChild(titleRow);

    var headActions = el('div', 'sd-head__actions');
    var settingsBtn = el('button', 'sd-icon-btn');
    settingsBtn.type = 'button';
    settingsBtn.setAttribute('aria-label', 'Model and engine settings');
    settingsBtn.setAttribute('aria-expanded', 'false');
    settingsBtn.title = 'Models & settings';
    settingsBtn.appendChild(svg(ICONS.gear, 17));

    var newBtn = el('button', 'sd-icon-btn');
    newBtn.type = 'button';
    newBtn.setAttribute('aria-label', 'New conversation');
    newBtn.title = 'New conversation';
    newBtn.appendChild(svg(ICONS.plus, 17));

    var closeBtn = el('button', 'sd-icon-btn');
    closeBtn.type = 'button';
    closeBtn.setAttribute('aria-label', 'Close Sideris');
    closeBtn.title = 'Close';
    closeBtn.appendChild(svg(ICONS.close, 17));

    headActions.appendChild(settingsBtn);
    headActions.appendChild(newBtn);
    headActions.appendChild(closeBtn);
    head.appendChild(headLeft);
    head.appendChild(headActions);

    // Settings / model selector
    var settings = el('div', 'sd-settings');
    settings.hidden = true;
    var modeRow = el('div', 'sd-load-row');
    var modeSeg = el('div', 'sd-seg');
    modeSeg.setAttribute('role', 'group');
    modeSeg.setAttribute('aria-label', 'Execution mode');
    var modeBtns = [['instant', 'Instant (0 MB)'], ['offline', 'Offline / Local']].map(function (o) {
      var b = el('button', 'sd-seg__btn', o[1]);
      b.type = 'button';
      b.dataset.mode = o[0];
      b.addEventListener('click', function () {
        prefs.runMode = o[0];
        savePrefs();
        hideProgress();
        syncSettings();
        setStatus(o[0] === 'instant' ? 'Instant mode active (0 MB download).' : 'Offline / Local mode active.');
      });
      modeSeg.appendChild(b);
      return b;
    });
    modeRow.appendChild(modeSeg);
    settings.appendChild(el('p', 'sd-section-label', 'Run mode'));
    settings.appendChild(modeRow);
    settings.appendChild(el('p', 'sd-section-label', 'Sideris models'));
    var modelsGrid = el('div', 'sd-models');
    modelsGrid.setAttribute('role', 'group');
    modelsGrid.setAttribute('aria-label', 'Select a Sideris model');

    var modelBtns = MODELS.map(function (m) {
      var b = el('button', 'sd-model-card');
      b.type = 'button';
      b.dataset.model = m.id;
      b.setAttribute('aria-pressed', 'false');
      b.appendChild(el('span', 'sd-model-card__name', m.name));
      b.appendChild(el('span', 'sd-model-card__meta', m.tier + ' · ' + m.sizeLabel));
      b.addEventListener('click', function () { selectModel(m.id); });
      modelsGrid.appendChild(b);
      return b;
    });

    var modelDesc = el('p', 'sd-model-desc');
    var loadRow = el('div', 'sd-load-row');
    var loadBtn = el('button', 'sd-btn sd-btn--primary', 'Download & load');
    loadBtn.type = 'button';
    var clearCacheBtn = el('button', 'sd-btn', 'Clear cache');
    clearCacheBtn.type = 'button';
    loadRow.appendChild(loadBtn);
    loadRow.appendChild(clearCacheBtn);

    var progressWrap = el('div', 'sd-progress');
    progressWrap.hidden = true;
    var progressBar = el('div', 'sd-progress__bar');
    var progressFill = el('div', 'sd-progress__fill');
    progressBar.appendChild(progressFill);
    var progressText = el('p', 'sd-progress__text');
    progressWrap.appendChild(progressBar);
    progressWrap.appendChild(progressText);

    // Instant cloud proxy + optional personal free API key (for Sideris Instant)
    var cloudWrap = el('div', 'sd-field');
    var wLab = el('label', '', 'Cloudflare Worker URL (optional override)');
    wLab.setAttribute('for', 'sdWorkerUrl');
    var wInput = el('input', 'sd-input');
    wInput.id = 'sdWorkerUrl';
    wInput.type = 'text';
    wInput.placeholder = 'https://sideris-ai.<subdomain>.workers.dev';
    wInput.value = prefs.workerUrl || '';
    var pLab = el('label', '', 'Or use your own free API key (stays in this browser)');
    pLab.setAttribute('for', 'sdByokProvider');
    pLab.style.marginTop = '8px';
    var pSelect = el('select', 'sd-select');
    pSelect.id = 'sdByokProvider';
    [
      ['gemini', 'Google AI Studio (Gemini Flash — free)'],
      ['groq', 'Groq (Llama 3.3 70B — free)'],
      ['openrouter', 'OpenRouter (:free models)']
    ].forEach(function (o) {
      var opt = el('option', '', o[1]);
      opt.value = o[0];
      pSelect.appendChild(opt);
    });
    pSelect.value = prefs.byokProvider || 'gemini';
    var kLab = el('label', '', 'Personal API key (optional)');
    kLab.setAttribute('for', 'sdByokKey');
    kLab.style.marginTop = '6px';
    var kInput = el('input', 'sd-input');
    kInput.id = 'sdByokKey';
    kInput.type = 'password';
    kInput.autocomplete = 'off';
    kInput.placeholder = 'Paste free key (stored locally only)';
    kInput.value = prefs.byokKey || '';
    cloudWrap.appendChild(wLab);
    cloudWrap.appendChild(wInput);
    cloudWrap.appendChild(pLab);
    cloudWrap.appendChild(pSelect);
    cloudWrap.appendChild(kLab);
    cloudWrap.appendChild(kInput);

    // Custom HF ONNX repo (for WebGPU models)
    var customWrap = el('div', 'sd-field');
    var customLab = el('label', '', 'Custom Hugging Face ONNX repo (optional)');
    customLab.setAttribute('for', 'sdCustomRepo');
    var customInput = el('input', 'sd-input');
    customInput.id = 'sdCustomRepo';
    customInput.type = 'text';
    customInput.placeholder = 'e.g. your-user/Sideris-Aether-v1-ONNX';
    customInput.value = prefs.customRepo;
    customWrap.appendChild(customLab);
    customWrap.appendChild(customInput);

    // Local Ollama settings (for Sideris Titan)
    var ollamaWrap = el('div', 'sd-field');
    var epLab = el('label', '', 'Local Ollama / LM Studio endpoint');
    epLab.setAttribute('for', 'sdOllamaEp');
    var epInput = el('input', 'sd-input');
    epInput.id = 'sdOllamaEp';
    epInput.type = 'text';
    epInput.value = prefs.ollamaEndpoint;
    var tagLab = el('label', '', 'Local model tag');
    tagLab.setAttribute('for', 'sdOllamaTag');
    tagLab.style.marginTop = '6px';
    var tagInput = el('input', 'sd-input');
    tagInput.id = 'sdOllamaTag';
    tagInput.type = 'text';
    tagInput.value = prefs.ollamaModel;
    ollamaWrap.appendChild(epLab);
    ollamaWrap.appendChild(epInput);
    ollamaWrap.appendChild(tagLab);
    ollamaWrap.appendChild(tagInput);

    // Toggles: RAG, Thinking, Answer language
    var toggles = el('div', 'sd-toggles');
    var ragLabel = el('label', 'sd-check');
    var ragCb = el('input');
    ragCb.type = 'checkbox';
    ragCb.checked = prefs.rag;
    ragLabel.appendChild(ragCb);
    ragLabel.appendChild(el('span', '', 'Course notes (RAG)'));

    var thinkLabel = el('label', 'sd-check');
    var thinkCb = el('input');
    thinkCb.type = 'checkbox';
    thinkCb.checked = prefs.thinking;
    thinkLabel.appendChild(thinkCb);
    thinkLabel.appendChild(el('span', '', 'Reasoning mode'));

    var langSeg = el('div', 'sd-seg');
    langSeg.setAttribute('role', 'group');
    langSeg.setAttribute('aria-label', 'Answer language');
    var langBtns = [['es', 'ES'], ['en', 'EN']].map(function (o) {
      var b = el('button', 'sd-seg__btn', o[1]);
      b.type = 'button';
      b.dataset.lang = o[0];
      b.addEventListener('click', function () { writeLang(o[0]); syncSettings(); });
      langSeg.appendChild(b);
      return b;
    });

    toggles.appendChild(ragLabel);
    toggles.appendChild(thinkLabel);
    toggles.appendChild(langSeg);

    [modelsGrid, modelDesc, loadRow, progressWrap, cloudWrap, customWrap, ollamaWrap, toggles].forEach(function (n) {
      settings.appendChild(n);
    });

    // Messages area
    var messages = el('div', 'sd-messages');
    messages.setAttribute('role', 'log');
    messages.setAttribute('aria-live', 'polite');

    // Status bar
    var status = el('div', 'sd-status', 'Ready. Select a model or ask a question about this page.');
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');

    // Composer
    var composer = el('form', 'sd-composer');
    var ta = el('textarea', 'sd-textarea');
    ta.rows = 1;
    ta.placeholder = 'Ask Sideris about this topic or problem...';
    ta.setAttribute('aria-label', 'Message Sideris');
    var sendBtn = el('button', 'sd-send', 'Send');
    sendBtn.type = 'submit';
    composer.appendChild(ta);
    composer.appendChild(sendBtn);

    drawer.appendChild(head);
    drawer.appendChild(settings);
    drawer.appendChild(messages);
    drawer.appendChild(status);
    drawer.appendChild(composer);

    var live = el('span', 'sd-sr');
    live.setAttribute('aria-live', 'polite');
    drawer.appendChild(live);

    document.body.appendChild(launcher);
    document.body.appendChild(backdrop);
    document.body.appendChild(drawer);

    ui = {
      launcher: launcher, backdrop: backdrop, drawer: drawer,
      modelPill: modelPill, settingsBtn: settingsBtn, newBtn: newBtn, closeBtn: closeBtn,
      settings: settings, modeBtns: modeBtns, modelBtns: modelBtns, modelDesc: modelDesc,
      loadBtn: loadBtn, clearCacheBtn: clearCacheBtn,
      progressWrap: progressWrap, progressFill: progressFill, progressText: progressText,
      customWrap: customWrap, customInput: customInput,
      cloudWrap: cloudWrap, wInput: wInput, pSelect: pSelect, kInput: kInput,
      ollamaWrap: ollamaWrap, epInput: epInput, tagInput: tagInput,
      ragCb: ragCb, thinkCb: thinkCb, langBtns: langBtns,
      messages: messages, status: status, composer: composer, ta: ta, sendBtn: sendBtn, live: live
    };

    // Events
    launcher.addEventListener('click', function () { if (session.open) close(false); else open(); });
    backdrop.addEventListener('click', function () { close(true); });
    closeBtn.addEventListener('click', function () { close(true); });
    newBtn.addEventListener('click', clearChat);
    settingsBtn.addEventListener('click', function () { toggleSettings(); });

    loadBtn.addEventListener('click', function () { preloadActiveModel(); });
    clearCacheBtn.addEventListener('click', function () {
      if (!window.AESiderisEngine) return;
      window.AESiderisEngine.clearBrowserCache().then(function (n) {
        setStatus(n ? 'Cleared ' + n + ' browser model cache store(s).' : 'No cached browser models found.');
        syncSettings();
      });
    });

    customInput.addEventListener('change', function () {
      prefs.customRepo = customInput.value.trim();
      savePrefs();
      syncSettings();
    });
    wInput.addEventListener('change', function () {
      prefs.workerUrl = wInput.value.trim();
      savePrefs();
      syncSettings();
    });
    pSelect.addEventListener('change', function () {
      prefs.byokProvider = pSelect.value;
      savePrefs();
      syncSettings();
    });
    kInput.addEventListener('change', function () {
      prefs.byokKey = kInput.value.trim();
      savePrefs();
      syncSettings();
    });
    epInput.addEventListener('change', function () {
      prefs.ollamaEndpoint = epInput.value.trim() || 'http://localhost:11434/v1';
      savePrefs();
    });
    tagInput.addEventListener('change', function () {
      prefs.ollamaModel = tagInput.value.trim() || 'qwen3.5:9b';
      savePrefs();
    });
    ragCb.addEventListener('change', function () { prefs.rag = ragCb.checked; savePrefs(); });
    thinkCb.addEventListener('change', function () { prefs.thinking = thinkCb.checked; savePrefs(); });

    composer.addEventListener('submit', function (e) {
      e.preventDefault();
      if (session.busy) {
        if (window.AESiderisEngine) window.AESiderisEngine.abort();
        return;
      }
      var text = ta.value.trim();
      if (!text) return;
      ta.value = '';
      sendUserMessage(text);
    });

    ta.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        composer.dispatchEvent(new Event('submit', { cancelable: true }));
      }
    });

    drawer.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { e.stopPropagation(); close(true); }
    });

    // Mutual exclusion with Focus Lab, Pomodoro, Updates and Side menu
    document.addEventListener('click', function (e) {
      if (!session.open || !e.target || !e.target.closest) return;
      if (e.target.closest('#focusLabButton, #pomodoroButton, .upd-bell, .ae-nav-btn')) close(false);
    }, true);

    syncSettings();
    renderMessages();
  }

  function setStatus(text) {
    if (ui.status) ui.status.textContent = text;
  }

  function showProgress(pct, text) {
    if (!ui.progressWrap) return;
    ui.progressWrap.hidden = false;
    ui.progressFill.style.width = Math.max(0, Math.min(100, pct || 0)) + '%';
    ui.progressText.textContent = text || '';
  }

  function hideProgress() {
    if (ui.progressWrap) ui.progressWrap.hidden = true;
  }

  function toggleSettings(force) {
    session.settingsOpen = force != null ? !!force : !session.settingsOpen;
    if (ui.settings) ui.settings.hidden = !session.settingsOpen;
    if (ui.settingsBtn) ui.settingsBtn.setAttribute('aria-expanded', session.settingsOpen ? 'true' : 'false');
  }

  function syncSettings() {
    if (!ui.drawer) return;
    var m = activeModelConfig();
    ui.modelPill.textContent = m.name;
    ui.modeBtns.forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.mode === prefs.runMode ? 'true' : 'false');
    });
    ui.modelBtns.forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.model === m.id ? 'true' : 'false');
      var meta = b.querySelector('.sd-model-card__meta');
      var info = findModel(b.dataset.model);
      if (meta && info) {
        meta.textContent = info.tier + ' · ' + (prefs.runMode === 'offline' ? (info.offlineSizeLabel || info.sizeLabel) : '0 MB · Instant');
      }
    });
    var isCloud = m.backend === 'cloud';
    var isOllama = m.backend === 'ollama';
    var isWebGPU = m.backend === 'webgpu';
    var wUrl = effectiveWorkerUrl();
    if (isCloud) {
      var modeLabel = prefs.byokKey ? ('personal key · ' + prefs.byokProvider)
        : wUrl ? ('Worker · ' + wUrl)
        : 'not configured yet — deploy Worker or paste a free key below';
      ui.modelDesc.textContent = (m.summary || '') + ' (' + modeLabel + ')';
    } else {
      ui.modelDesc.textContent = (m.summary || '') + ' (' + m.repo + ')';
    }
    ui.cloudWrap.hidden = !isCloud;
    ui.customWrap.hidden = !isWebGPU;
    ui.ollamaWrap.hidden = !isOllama;
    ui.clearCacheBtn.hidden = !isWebGPU;
    if (isCloud) {
      ui.loadBtn.textContent = prefs.byokKey ? 'Clear personal key' : 'Test cloud connection';
    } else if (isOllama) {
      ui.loadBtn.textContent = 'Test local connection';
    } else if (window.AESiderisEngine && window.AESiderisEngine.isLoaded(m.repo, m.dtype)) {
      ui.loadBtn.textContent = 'Loaded in GPU';
    } else {
      ui.loadBtn.textContent = 'Download & load (' + m.sizeLabel + ')';
    }
    var lang = readLang();
    ui.langBtns.forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.lang === lang ? 'true' : 'false');
    });
  }

  function selectModel(id) {
    var m = findModel(id);
    prefs.modelId = m.id;
    savePrefs();
    hideProgress();
    syncSettings();
    var mode = m.backend === 'cloud' ? 'instant · 0 MB' : m.backend === 'ollama' ? 'local Ollama' : ('WebGPU ' + m.sizeLabel);
    setStatus('Selected ' + m.name + ' (' + mode + ').');
  }

  function preloadActiveModel() {
    if (!window.AESiderisEngine) return Promise.resolve();
    var m = activeModelConfig();
    if (m.backend === 'cloud') {
      if (prefs.byokKey) {
        prefs.byokKey = '';
        if (ui.kInput) ui.kInput.value = '';
        savePrefs();
        syncSettings();
        setStatus('Cleared personal API key from this browser.');
        return Promise.resolve();
      }
      var wUrl = effectiveWorkerUrl();
      setStatus(wUrl ? 'Checking Sideris cloud proxy...' : 'No Cloudflare Worker URL configured yet.');
      return window.AESiderisEngine.checkCloud(wUrl).then(function (res) {
        if (res.ok) {
          var provs = res.providers && res.providers.length ? ' Active: ' + res.providers.join(', ') : '';
          setStatus('Sideris Instant connected.' + provs);
        } else {
          setStatus('Cloud proxy not ready (' + res.error + '). Paste a free Gemini/Groq key below or deploy tools/cloudflare/sideris-worker.js.');
        }
      });
    }
    if (m.backend === 'ollama') {
      setStatus('Checking local server at ' + m.endpoint + '...');
      return window.AESiderisEngine.checkOllama(m.endpoint).then(function (res) {
        if (res.ok) {
          var found = res.models.length ? ' Available: ' + res.models.slice(0, 4).join(', ') : '';
          setStatus('Connected to local server.' + found);
        } else {
          setStatus('Local server unreachable at ' + res.endpoint + ' (' + res.error + ').');
        }
      });
    }
    ui.loadBtn.disabled = true;
    return window.AESiderisEngine.loadWebGPU(m, function (p) {
      showProgress(p.progress, p.text);
      setStatus(p.text);
    }).then(function () {
      ui.loadBtn.disabled = false;
      syncSettings();
      setStatus(m.name + ' is ready in GPU memory (cached offline).');
    }).catch(function (err) {
      ui.loadBtn.disabled = false;
      hideProgress();
      setStatus(err && err.message ? err.message : String(err));
    });
  }

  function renderMessages() {
    if (!ui.messages) return;
    ui.messages.textContent = '';
    if (!session.messages.length) {
      var empty = el('div', 'sd-empty');
      empty.appendChild(el('p', 'sd-empty__title', 'Ask Sideris'));
      empty.appendChild(el('p', 'sd-empty__body',
        'Your free, downloadable aerospace tutor. Select any text on the page for Ask AI, or start a question below grounded in the UC3M course notes.'));
      var quick = el('div', 'sd-quick');
      [
        'Summarise the key equations of this topic',
        'Give me a 3-question check on this page',
        'What are the typical exam traps here?'
      ].forEach(function (q) {
        var b = el('button', 'sd-quick__btn', q);
        b.type = 'button';
        b.addEventListener('click', function () { sendUserMessage(q); });
        quick.appendChild(b);
      });
      empty.appendChild(quick);
      ui.messages.appendChild(empty);
      return;
    }

    session.messages.forEach(function (msg) {
      var card = el('article', 'sd-msg sd-msg--' + msg.role + (msg.error ? ' sd-msg--error' : ''));
      var head = el('div', 'sd-msg__head');
      head.appendChild(el('span', 'sd-msg__role', msg.role === 'user' ? 'You' : (msg.modelName || 'Sideris')));
      if (msg.role === 'assistant' && msg.text && !msg.error) {
        var copy = el('button', 'sd-msg__copy', 'Copy');
        copy.type = 'button';
        copy.addEventListener('click', function () {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(msg.text).then(function () { copy.textContent = 'Copied'; setTimeout(function () { copy.textContent = 'Copy'; }, 1200); });
          }
        });
        head.appendChild(copy);
      }
      card.appendChild(head);
      if (msg.tag) card.appendChild(el('p', 'sd-msg__tag', msg.tag));
      var content = el('div', 'sd-msg__content');
      if (msg.role === 'user') {
        var body = el('div', 'sd-msg__body');
        renderMarkdownBlocks(body, msg.displayText || msg.text);
        content.appendChild(body);
      } else {
        renderRichText(content, msg.text || '...');
      }
      card.appendChild(content);

      if (msg.ragHits && msg.ragHits.length) {
        var det = el('details', 'sd-rag-notes');
        det.appendChild(el('summary', '', 'Course notes used (' + msg.ragHits.length + ')'));
        var ul = el('ul', 'sd-rag-list');
        msg.ragHits.forEach(function (h) {
          ul.appendChild(el('li', '', h.title + (h.heading && h.heading !== h.title ? ' — ' + h.heading : '')));
        });
        det.appendChild(ul);
        card.appendChild(det);
      }

      ui.messages.appendChild(card);
      msg._contentEl = content;
    });
    ui.messages.scrollTop = ui.messages.scrollHeight;
  }

  function setBusy(busy) {
    session.busy = !!busy;
    if (!ui.sendBtn) return;
    ui.sendBtn.textContent = busy ? 'Stop' : 'Send';
    ui.ta.disabled = busy;
  }

  function sendUserMessage(text, opts) {
    opts = opts || {};
    if (session.busy || !window.AESiderisEngine) return Promise.resolve();
    var m = activeModelConfig();
    var lang = opts.lang || readLang();

    var userMsg = {
      role: 'user',
      text: opts.modelPrompt || text,
      displayText: opts.displayText || text,
      tag: opts.tag || ''
    };
    session.messages.push(userMsg);

    var assistantMsg = {
      role: 'assistant',
      text: '',
      modelName: m.name,
      ragHits: []
    };
    session.messages.push(assistantMsg);
    renderMessages();
    setBusy(true);
    setStatus(
      m.backend === 'cloud' ? 'Streaming from ' + m.name + '...'
        : m.backend === 'ollama' ? 'Streaming from ' + m.name + ' (local)...'
        : 'Preparing ' + m.name + '...'
    );

    var ragQuery = opts.ragQuery || (pageTitle() + ' ' + text);
    var ragPromise = (prefs.rag && window.AESiderisRAG)
      ? window.AESiderisRAG.search(ragQuery, { limit: 4 })
      : Promise.resolve([]);

    return ragPromise.then(function (hits) {
      assistantMsg.ragHits = hits || [];
      var ragText = (hits && hits.length && window.AESiderisRAG) ? window.AESiderisRAG.formatContext(hits) : '';
      var sys = buildSystemPrompt(ragText, lang);
      var apiMessages = [{ role: 'system', content: sys }];
      // Keep last 10 turns to stay fast inside compact context windows.
      var hist = session.messages.slice(0, -1).slice(-10);
      hist.forEach(function (item) {
        apiMessages.push({ role: item.role, content: item.text });
      });

      return window.AESiderisEngine.generate(
        {
          model: m,
          messages: apiMessages,
          maxTokens: session.socratic ? 512 : 1400,
          cloud: {
            workerUrl: effectiveWorkerUrl(),
            byokProvider: prefs.byokProvider || 'gemini',
            byokKey: prefs.byokKey || ''
          }
        },
        function (_chunk, full) {
          assistantMsg.text = full;
          if (assistantMsg._contentEl) {
            renderRichText(assistantMsg._contentEl, full);
            ui.messages.scrollTop = ui.messages.scrollHeight;
          }
        },
        function (p) {
          showProgress(p.progress, p.text);
          setStatus(p.text);
        }
      );
    }).then(function (finalText) {
      if (finalText) assistantMsg.text = finalText;
      if (!assistantMsg.text) assistantMsg.text = '(Generation stopped.)';
      hideProgress();
      setBusy(false);
      syncSettings();
      renderMessages();
      setStatus(m.name + ' · done.');
      ui.ta.focus();
      return assistantMsg.text;
    }).catch(function (err) {
      hideProgress();
      setBusy(false);
      assistantMsg.error = true;
      assistantMsg.text = (err && err.message) ? err.message : String(err);
      renderMessages();
      setStatus('Error: ' + assistantMsg.text);
      toggleSettings(true);
    });
  }

  /* ---------------------------------------------------------------- Ask AI handoff */
  function openWithAskRequest(payload) {
    if (!payload) return;
    open();
    session.messages = [];
    session.socratic = !!payload.socratic;
    session.systemExtra = payload.hiddenContext || '';
    if (payload.lang === 'es' || payload.lang === 'en') {
      writeLang(payload.lang);
      syncSettings();
    }
    var display = payload.visibleText || payload.taskLabel || 'Help me with this section.';
    var tag = [payload.taskLabel, payload.location].filter(Boolean).join(' · ');
    return sendUserMessage(display, {
      displayText: display,
      modelPrompt: payload.modelPrompt || display,
      ragQuery: payload.ragQuery || display,
      tag: tag,
      lang: payload.lang
    });
  }

  function clearChat() {
    if (session.busy && window.AESiderisEngine) window.AESiderisEngine.abort();
    session.messages = [];
    session.systemExtra = '';
    session.socratic = false;
    setBusy(false);
    renderMessages();
    setStatus('Conversation cleared.');
  }

  /* ---------------------------------------------------------------- open / close */
  function open() {
    if (!ui.drawer) buildUI();
    if (session.open) return;
    if (window.AEFocusLab && typeof window.AEFocusLab.close === 'function') window.AEFocusLab.close();
    if (window.AEPomodoro && typeof window.AEPomodoro.close === 'function') window.AEPomodoro.close();
    if (window.AEUpdates && typeof window.AEUpdates.close === 'function') window.AEUpdates.close();
    if (window.AESidebar && typeof window.AESidebar.close === 'function') window.AESidebar.close();

    session.lastFocus = document.activeElement;
    session.open = true;
    ui.backdrop.hidden = false;
    ui.drawer.hidden = false;
    ui.launcher.setAttribute('aria-expanded', 'true');
    syncSettings();
    requestAnimationFrame(function () {
      ui.backdrop.classList.add('is-open');
      ui.drawer.classList.add('is-open');
    });
    ui.ta.focus({ preventScroll: true });
  }

  function close(returnFocus) {
    if (!session.open || !ui.drawer) return;
    session.open = false;
    ui.backdrop.classList.remove('is-open');
    ui.drawer.classList.remove('is-open');
    ui.backdrop.hidden = true;
    ui.drawer.hidden = true;
    ui.launcher.setAttribute('aria-expanded', 'false');
    if (returnFocus) {
      if (session.lastFocus && typeof session.lastFocus.focus === 'function' && document.contains(session.lastFocus)) {
        session.lastFocus.focus();
      } else {
        ui.launcher.focus();
      }
    }
  }

  function boot() {
    if (ui.drawer) return;
    buildUI();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();

  window.AESideris = {
    KEY: KEY,
    open: open,
    close: close,
    isOpen: function () { return session.open; },
    models: function () { return MODELS.slice(); },
    selectModel: selectModel,
    openWithAskRequest: openWithAskRequest,
    sendUserMessage: sendUserMessage,
    clearChat: clearChat,
    renderRichText: renderRichText,
    state: function () { return { open: session.open, busy: session.busy, model: activeModelConfig(), rag: prefs.rag, thinking: prefs.thinking, count: session.messages.length }; }
  };
})();
