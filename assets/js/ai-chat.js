/*!
 * Aerospace Engineering Study Portal: Sideris AI Studio workspace.
 *
 * Loaded on study pages by assets/js/theme.js (after sideris-config.js, ai-models.js,
 * ai-rag.js and ai-engine.js; no HTML page carries its own <script> tag). Adds its own
 * stylesheet (assets/css/ai-chat.css). Skipped in PDF print mode (?print=...) and hidden
 * in @media print (print.css untouched).
 *
 * Features:
 *   - Full-height AI Studio workspace with persistent left conversation history sidebar
 *     and live split-view docking (72% AI Studio + 28% live study page on desktop, with
 *     one-click Split / Fullscreen toggle).
 *   - Clean modern sans-serif UI (Inter / system-ui), inline model picker for Sideris Lux,
 *     Sideris Aether (default), Sideris Orion and Sideris Titan (0 MB instant via Cloudflare
 *     Workers AI; optional offline WebGPU / local Ollama inside Settings).
 *   - Seamless handoff from assets/js/ask-ai.js keeping <reference_solution hidden="true">
 *     out of the visible chat DOM.
 *   - Client-side RAG grounding over vault/ shards (assets/js/ai-rag.js), safe DOM Markdown
 *     (tables, quotes, lists, code) + bulletproof KaTeX ($...$, $$...$$, \(...\), \[...\],
 *     standalone single-$ promotion, \begin{align/equation} support, auto CDN fallback).
 *
 * Storage: 'ae_sideris' (prefs) and 'ae_sideris_chats' (history) — never a key containing "theme".
 *          Answer language synced with 'ae_ask_lang' ('es' | 'en').
 * API: window.AESideris = { KEY, CHATS_KEY, open, close, isOpen, models, selectModel,
 *      openWithAskRequest, sendUserMessage, clearChat, history, loadConversation,
 *      deleteConversation, renderRichText, state }
 */
(function () {
  'use strict';

  if (window.AESideris) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var KEY = 'ae_sideris';
  var CHATS_KEY = 'ae_sideris_chats';
  var LANG_KEY = 'ae_ask_lang';
  var MAX_CHATS = 30;
  var MODELS = Array.isArray(window.AE_SIDERIS_MODELS) ? window.AE_SIDERIS_MODELS.slice() : [];

  var ICONS = {
    // Minimal geometric orbital-diamond Sideris mark
    brand: '<circle cx="12" cy="12" r="8.5" opacity=".45"/><path d="M12 4.5L14.2 9.8L19.5 12L14.2 14.2L12 19.5L9.8 14.2L4.5 12L9.8 9.8Z"/>',
    sidebar: '<rect x="3" y="4" width="18" height="16" rx="2.5"/><line x1="9" y1="4" x2="9" y2="20"/>',
    split: '<rect x="3" y="4" width="18" height="16" rx="2.5"/><line x1="15" y1="4" x2="15" y2="20"/>',
    expand: '<polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/>',
    gear: '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33h.08a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51h.08a1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82v.08a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    close: '<path d="M18 6L6 18M6 6l12 12"/>',
    chevUp: '<polyline points="6 15 12 9 18 15"/>'
  };

  var SUBJECT_NAMES = {
    'fluid-mechanics': 'Fluid Mechanics',
    'aerospace-materials-1': 'Aerospace Materials I',
    'engineering-mechanics': 'Engineering Mechanics',
    'advanced-maths': 'Advanced Maths',
    'business-management': 'Business Management'
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

  /* ---------------------------------------------------------------- state & persistence */
  function defaultModelId() {
    for (var i = 0; i < MODELS.length; i++) if (MODELS[i].default) return MODELS[i].id;
    return MODELS[0] ? MODELS[0].id : 'sideris-aether';
  }

  function findModel(id) {
    for (var i = 0; i < MODELS.length; i++) if (MODELS[i].id === id) return MODELS[i];
    return MODELS[0] || {
      id: 'sideris-aether', name: 'Sideris Aether', tier: 'Recommended',
      backend: 'cloud', offlineBackend: 'webgpu',
      repo: 'onnx-community/Qwen3.5-4B-ONNX', dtype: 'q4f16',
      sizeLabel: '0 MB · Instant', offlineSizeLabel: '~2.5 GB'
    };
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
      runMode: 'instant',       // 'instant' (0 MB cloud) | 'offline' (WebGPU / Ollama)
      layout: 'split',          // 'split' (72% AI + 28% live page) | 'full' (100% AI)
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
        if (parsed.layout === 'split' || parsed.layout === 'full') base.layout = parsed.layout;
        if (typeof parsed.rag === 'boolean') base.rag = parsed.rag;
        if (typeof parsed.thinking === 'boolean') base.thinking = parsed.thinking;
        if (typeof parsed.customRepo === 'string') base.customRepo = parsed.customRepo;
        if (typeof parsed.workerUrl === 'string') base.workerUrl = parsed.workerUrl;
        if (typeof parsed.byokProvider === 'string') base.byokProvider = parsed.byokProvider;
        if (typeof parsed.byokKey === 'string') base.byokKey = parsed.byokKey;
        if (typeof parsed.ollamaEndpoint === 'string' && parsed.ollamaEndpoint.trim()) base.ollamaEndpoint = parsed.ollamaEndpoint;
        if (typeof parsed.ollamaModel === 'string' && parsed.ollamaModel.trim()) base.ollamaModel = parsed.ollamaModel;
      }
    } catch (e) { /* ignore */ }
    return base;
  }

  function savePrefs() {
    try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (e) { /* blocked */ }
  }

  function effectiveWorkerUrl() {
    var cfg = window.AE_SIDERIS_CONFIG && typeof window.AE_SIDERIS_CONFIG.workerUrl === 'string'
      ? window.AE_SIDERIS_CONFIG.workerUrl.trim()
      : '';
    return (prefs.workerUrl && prefs.workerUrl.trim()) || cfg;
  }

  function loadHistoryStore() {
    try {
      var raw = localStorage.getItem(CHATS_KEY);
      var arr = raw ? JSON.parse(raw) : [];
      return Array.isArray(arr) ? arr.filter(function (c) { return c && typeof c.id === 'string' && Array.isArray(c.messages); }) : [];
    } catch (e) { return []; }
  }

  function saveHistoryStore(list) {
    try { localStorage.setItem(CHATS_KEY, JSON.stringify(list.slice(0, MAX_CHATS))); } catch (e) { /* quota/blocked */ }
  }

  function makeChatId() {
    return 'c-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 6);
  }

  function formatStamp(ms) {
    if (!ms) return '';
    var d = new Date(ms);
    var diff = Math.max(0, Date.now() - ms);
    if (diff < 60000) return 'now';
    if (diff < 3600000) return Math.floor(diff / 60000) + 'm';
    if (diff < 86400000) return Math.floor(diff / 3600000) + 'h';
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return d.getDate() + ' ' + months[d.getMonth()];
  }

  var prefs = loadPrefs();
  var chats = loadHistoryStore();
  var session = {
    open: false,
    settingsOpen: false,
    sidebarCollapsed: false,
    mobileHistoryOpen: false,
    modelMenuOpen: false,
    busy: false,
    chatId: '',
    messages: [],          // { role: 'user'|'assistant', text, displayText, tag, modelName, ragHits, error }
    systemExtra: '',       // hidden context from ask-ai.js (<reference_solution hidden="true">)
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

  function serialiseMessages(list) {
    return list.map(function (m) {
      return {
        role: m.role,
        text: m.text || '',
        displayText: m.displayText || '',
        tag: m.tag || '',
        modelName: m.modelName || '',
        error: !!m.error,
        ragHits: Array.isArray(m.ragHits) ? m.ragHits.map(function (h) {
          return { title: h.title || '', heading: h.heading || '' };
        }) : []
      };
    });
  }

  function persistCurrentChat() {
    if (!session.messages.length) return;
    if (!session.chatId) session.chatId = makeChatId();
    var firstUser = null;
    for (var i = 0; i < session.messages.length; i++) {
      if (session.messages[i].role === 'user') { firstUser = session.messages[i]; break; }
    }
    var rawTitle = (firstUser && (firstUser.displayText || firstUser.text)) || 'Conversation';
    var title = rawTitle.replace(/\s+/g, ' ').trim();
    if (title.length > 64) title = title.slice(0, 61) + '…';

    var slug = window.AESiderisRAG ? window.AESiderisRAG.currentSubject() : '';
    var entry = {
      id: session.chatId,
      title: title,
      subject: SUBJECT_NAMES[slug] || pageTitle().slice(0, 28) || 'Portal',
      modelId: prefs.modelId,
      updatedAt: Date.now(),
      socratic: !!session.socratic,
      systemExtra: session.systemExtra || '',
      messages: serialiseMessages(session.messages)
    };
    chats = chats.filter(function (c) { return c.id !== entry.id; });
    chats.unshift(entry);
    if (chats.length > MAX_CHATS) chats = chats.slice(0, MAX_CHATS);
    saveHistoryStore(chats);
    renderHistory();
  }

  function loadConversation(id) {
    var target = null;
    for (var i = 0; i < chats.length; i++) if (chats[i].id === id) { target = chats[i]; break; }
    if (!target) return false;
    if (session.busy && window.AESiderisEngine) window.AESiderisEngine.abort();
    session.chatId = target.id;
    session.messages = serialiseMessages(target.messages);
    session.socratic = !!target.socratic;
    session.systemExtra = target.systemExtra || '';
    session.mobileHistoryOpen = false;
    setBusy(false);
    setSettings(false);
    syncLayoutClasses();
    renderHistory();
    renderMessages();
    setStatus('Loaded: ' + target.title);
    return true;
  }

  function deleteConversation(id) {
    chats = chats.filter(function (c) { return c.id !== id; });
    saveHistoryStore(chats);
    if (session.chatId === id) {
      session.chatId = '';
      session.messages = [];
      session.systemExtra = '';
      session.socratic = false;
      renderMessages();
    }
    renderHistory();
  }

  /* ---------------------------------------------------------------- bulletproof Markdown + KaTeX renderer */
  var katexLoading = false;

  function ensureKaTeX() {
    if (window.katex && typeof window.katex.render === 'function') return true;
    if (katexLoading) return false;
    katexLoading = true;
    var tries = 0;
    function flush() {
      katexLoading = false;
      if (session.messages.length && ui.messages) renderMessages();
    }
    function poll() {
      if (window.katex && typeof window.katex.render === 'function') { flush(); return; }
      if (++tries < 20) { setTimeout(poll, 120); return; }
      if (!document.querySelector('link[href*="katex"]')) {
        var lk = document.createElement('link');
        lk.rel = 'stylesheet';
        lk.href = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css';
        document.head.appendChild(lk);
      }
      if (!document.querySelector('script[src*="katex.min.js"]')) {
        var sc = document.createElement('script');
        sc.src = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js';
        sc.onload = flush;
        document.head.appendChild(sc);
      }
    }
    setTimeout(poll, 100);
    return false;
  }

  function cleanTex(tex) {
    return String(tex || '')
      .replace(/\\euro\b/g, '\\text{€}')
      .replace(/\\text\{([^{}]*)&([^{}]*)\}/g, '\\text{$1and$2}')
      .replace(/\\\\(?=(?:frac|partial|nabla|vec|mathbf|mathrm|text|sqrt|int|sum|left|right|begin|end|cdot|times|alpha|beta|gamma|delta|rho|mu|sigma|tau|omega|theta|phi|pi|Delta|Omega|Sigma)\b)/g, '\\')
      .trim();
  }

  function renderMathSpan(tex, display) {
    var span = el(display ? 'div' : 'span', display ? 'sd-math-block' : 'sd-math-inline');
    var src = cleanTex(tex);
    if (!src) return span;
    if (ensureKaTeX()) {
      try {
        window.katex.render(src, span, {
          displayMode: !!display,
          throwOnError: false,
          strict: 'ignore',
          trust: false
        });
        return span;
      } catch (e) { /* fall through */ }
    }
    span.textContent = display ? '$$' + src + '$$' : '$' + src + '$';
    return span;
  }

  function appendFormattedText(parent, text) {
    var re = /(`[^`\n]+`|\*\*[^*\n]+\*\*|\*[^*\n]+\*)/g;
    var last = 0, m;
    while ((m = re.exec(text)) !== null) {
      if (m.index > last) parent.appendChild(document.createTextNode(text.slice(last, m.index)));
      var tok = m[0];
      if (tok.charAt(0) === '`') {
        parent.appendChild(el('code', '', tok.slice(1, -1)));
      } else if (tok.indexOf('**') === 0) {
        var strong = el('strong');
        appendInline(strong, tok.slice(2, -2));
        parent.appendChild(strong);
      } else {
        var em = el('em');
        appendInline(em, tok.slice(1, -1));
        parent.appendChild(em);
      }
      last = re.lastIndex;
    }
    if (last < text.length) parent.appendChild(document.createTextNode(text.slice(last)));
  }

  function appendInline(parent, text) {
    var s = String(text || '');
    var i = 0, buf = '';
    function flushBuf() {
      if (buf) { appendFormattedText(parent, buf); buf = ''; }
    }
    while (i < s.length) {
      // Escaped dollar \$
      if (s.charAt(i) === '\\' && s.charAt(i + 1) === '$') {
        buf += '$';
        i += 2;
        continue;
      }
      // Inline code `...`
      if (s.charAt(i) === '`') {
        var ce = s.indexOf('`', i + 1);
        if (ce > i) {
          flushBuf();
          parent.appendChild(el('code', '', s.slice(i + 1, ce)));
          i = ce + 1;
          continue;
        }
      }
      // Display math $$...$$ inline
      if (s.slice(i, i + 2) === '$$') {
        var de = s.indexOf('$$', i + 2);
        if (de > i + 2) {
          flushBuf();
          parent.appendChild(renderMathSpan(s.slice(i + 2, de), true));
          i = de + 2;
          continue;
        }
      }
      // Display math \[...\]
      if (s.slice(i, i + 2) === '\\[') {
        var be = s.indexOf('\\]', i + 2);
        if (be > i + 2) {
          flushBuf();
          parent.appendChild(renderMathSpan(s.slice(i + 2, be), true));
          i = be + 2;
          continue;
        }
      }
      // Inline math \(...\)
      if (s.slice(i, i + 2) === '\\(') {
        var pe = s.indexOf('\\)', i + 2);
        if (pe > i + 2) {
          flushBuf();
          parent.appendChild(renderMathSpan(s.slice(i + 2, pe), false));
          i = pe + 2;
          continue;
        }
      }
      // Inline math $...$ (supports inner spaces like `$ \vec{v} $`, skips plain currency)
      if (s.charAt(i) === '$' && s.charAt(i + 1) !== '$') {
        var j = i + 1, found = -1;
        while (j < s.length) {
          if (s.charAt(j) === '\\') { j += 2; continue; }
          if (s.charAt(j) === '\n') break;
          if (s.charAt(j) === '$' && s.charAt(j + 1) !== '$') { found = j; break; }
          j++;
        }
        if (found > i + 1) {
          var inner = s.slice(i + 1, found);
          var isCurrency = /^\d[\d,.\s]*(?:and|to|or|y|a|€|USD|EUR|m\.u\.)\b/i.test(inner.trim());
          if (!isCurrency && inner.trim()) {
            flushBuf();
            parent.appendChild(renderMathSpan(inner, false));
            i = found + 1;
            continue;
          }
        }
      }
      buf += s.charAt(i);
      i++;
    }
    flushBuf();
  }

  function splitThinking(raw) {
    var text = String(raw || '');
    var open = text.indexOf('<think>');
    if (open < 0) return { think: '', answer: text, thinking: false };
    var close = text.indexOf('</think>', open + 7);
    if (close < 0) {
      return { think: text.slice(open + 7).trim(), answer: text.slice(0, open).trim(), thinking: true };
    }
    return {
      think: text.slice(open + 7, close).trim(),
      answer: (text.slice(0, open) + text.slice(close + 8)).trim(),
      thinking: false
    };
  }

  function normaliseBlockMath(text) {
    var parts = String(text || '').replace(/\r\n/g, '\n').split(/(```[\s\S]*?```)/g);
    return parts.map(function (seg, idx) {
      if (idx % 2 === 1) return seg;
      // Normalise accidental double-escaped delimiters \\[ \\] \\( \\)
      var out = seg
        .replace(/\\\\\[/g, '\\[')
        .replace(/\\\\\]/g, '\\]')
        .replace(/\\\\\(/g, '\\(')
        .replace(/\\\\\)/g, '\\)');
      // Wrap standalone \begin{equation|align|gather|multline|cases|pmatrix|bmatrix}... blocks without $$
      out = out.replace(
        /(^|\n)[ \t]*(\\begin\{(equation|align|gather|multline|cases|pmatrix|bmatrix)\*?\}[\s\S]*?\\end\{\3\*?\})[ \t]*(?=\n|$)/g,
        '$1$$\n$2\n$$'
      );
      return out;
    }).join('');
  }

  function isStandaloneSingleMath(line) {
    // Promote standalone single-dollar or \(...\) equation lines (common from Llama 3.3 / Qwen)
    // to crisp display math blocks!
    var t = (line || '').trim();
    if (!t || t.indexOf('$$') === 0) return null;
    if (t.charAt(0) === '$' && t.charAt(t.length - 1) === '$' && t.length > 4) {
      var body = t.slice(1, -1);
      // Must not contain another unescaped $ inside (otherwise it's a sentence with 2 inline terms)
      if (!/(^|[^\\])\$/.test(body) && /[=\\^_{}]/.test(body)) return body.trim();
    }
    if (t.indexOf('\\(') === 0 && t.slice(-2) === '\\)' && t.length > 6) {
      var pbody = t.slice(2, -2);
      if (pbody.indexOf('\\)') < 0 && /[=\\^_{}]/.test(pbody)) return pbody.trim();
    }
    return null;
  }

  function isTableSep(line) {
    return /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$/.test(line || '');
  }

  function splitTableRow(line) {
    return line.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(function (c) { return c.trim(); });
  }

  function renderMarkdownBlocks(container, text) {
    var lines = normaliseBlockMath(text).split('\n');
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

      // Display math block starting line ($$ or \[)
      var mStart = /^\s*(\$\$|\\\[)(.*)$/.exec(line);
      if (mStart) {
        var openTok = mStart[1];
        var closeTok = openTok === '$$' ? '$$' : '\\]';
        var rest = mStart[2];
        var closeIdx = rest.indexOf(closeTok);
        if (closeIdx >= 0) {
          container.appendChild(renderMathSpan(rest.slice(0, closeIdx), true));
          var after = rest.slice(closeIdx + closeTok.length).trim();
          if (after) {
            var tailP = el('p');
            appendInline(tailP, after);
            container.appendChild(tailP);
          }
          i++;
          continue;
        }
        var mathLines = [rest];
        var trailing = '';
        i++;
        while (i < lines.length) {
          var ci = lines[i].indexOf(closeTok);
          if (ci >= 0) {
            mathLines.push(lines[i].slice(0, ci));
            trailing = lines[i].slice(ci + closeTok.length).trim();
            i++;
            break;
          }
          mathLines.push(lines[i]);
          i++;
        }
        container.appendChild(renderMathSpan(mathLines.join('\n'), true));
        if (trailing) {
          var afterP = el('p');
          appendInline(afterP, trailing);
          container.appendChild(afterP);
        }
        continue;
      }

      // Standalone single-$ or \(...\) equation line -> render in full display mode!
      var singleEq = isStandaloneSingleMath(line);
      if (singleEq) {
        container.appendChild(renderMathSpan(singleEq, true));
        i++;
        continue;
      }

      // Horizontal rule
      if (/^\s*(?:---+|\*\*\*+|___+)\s*$/.test(line)) {
        container.appendChild(el('hr', 'sd-hr'));
        i++;
        continue;
      }

      // Headings
      var hm = /^(#{1,4})\s+(.+)$/.exec(line.trim());
      if (hm) {
        var h = el(hm[1].length <= 2 ? 'h3' : 'h4');
        appendInline(h, hm[2]);
        container.appendChild(h);
        i++;
        continue;
      }

      // Markdown table
      if (line.indexOf('|') >= 0 && i + 1 < lines.length && isTableSep(lines[i + 1])) {
        var wrap = el('div', 'sd-table-wrap');
        var tbl = el('table', 'sd-table');
        var thead = el('thead');
        var htr = el('tr');
        splitTableRow(line).forEach(function (cell) {
          var th = el('th');
          appendInline(th, cell);
          htr.appendChild(th);
        });
        thead.appendChild(htr);
        tbl.appendChild(thead);
        i += 2;
        var tbody = el('tbody');
        while (i < lines.length && lines[i].trim() && lines[i].indexOf('|') >= 0) {
          var btr = el('tr');
          splitTableRow(lines[i]).forEach(function (cell) {
            var td = el('td');
            appendInline(td, cell);
            btr.appendChild(td);
          });
          tbody.appendChild(btr);
          i++;
        }
        tbl.appendChild(tbody);
        wrap.appendChild(tbl);
        container.appendChild(wrap);
        continue;
      }

      // Blockquote
      if (/^\s*>\s?/.test(line)) {
        var qLines = [];
        while (i < lines.length && /^\s*>\s?/.test(lines[i])) {
          qLines.push(lines[i].replace(/^\s*>\s?/, ''));
          i++;
        }
        var bq = el('blockquote', 'sd-quote');
        renderMarkdownBlocks(bq, qLines.join('\n'));
        container.appendChild(bq);
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
      while (i < lines.length && lines[i].trim() &&
        !/^(```|#{1,4}\s|\s*[-*]\s+|\s*\d+[.)]\s+|\s*\$\$|\s*\\\[|\s*>\s?|\s*(?:---+|\*\*\*+)\s*$)/.test(lines[i]) &&
        !isStandaloneSingleMath(lines[i]) &&
        !(lines[i].indexOf('|') >= 0 && i + 1 < lines.length && isTableSep(lines[i + 1]))) {
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
    if (parts.think && prefs.thinking) {
      var det = el('details', 'sd-think');
      if (parts.thinking) det.open = true;
      det.appendChild(el('summary', '', parts.thinking ? 'Reasoning...' : 'Show reasoning'));
      var thinkBody = el('div', 'sd-think__body');
      renderMarkdownBlocks(thinkBody, parts.think);
      det.appendChild(thinkBody);
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

  /* ---------------------------------------------------------------- context & sharper system prompt */
  function pageTitle() {
    var h1 = document.querySelector('h1');
    return ((h1 ? h1.textContent : document.title) || '').replace(/\s+/g, ' ').trim();
  }

  function contextSubtitle() {
    var slug = window.AESiderisRAG ? window.AESiderisRAG.currentSubject() : '';
    var subj = SUBJECT_NAMES[slug] || '';
    var t = pageTitle();
    return [subj, t].filter(Boolean).join(' · ') || 'UC3M Aerospace Tutor';
  }

  function isProblemPage() {
    return /\/(problemas|extra-problems)\//.test(location.pathname);
  }

  function buildSystemPrompt(ragText, lang) {
    var slug = window.AESiderisRAG ? window.AESiderisRAG.currentSubject() : '';
    var business = slug === 'business-management';
    var lines = [
      'You are Sideris, a clear, rigorous engineering tutor for the 2nd year of the BSc in Aerospace Engineering at UC3M.',
      'Current page: ' + pageTitle() + (slug ? ' (subject: ' + slug + ')' : '') + '.',
      'Style and formatting rules:',
      '- Be clear, structured, and easy to scan: use short headings (###), concise paragraphs, and clean bullet lists. Never write walls of text, never use emojis, and never use "Phase 1..4" labels.',
      '- Match the depth to the question: for conceptual questions, give crisp intuition + governing equation + physical meaning; for problems and derivations, show every algebraic and numerical step explicitly with zero skips (chain rule, product rule, substitutions, Barrow limits, and justification of each law).',
      business
        ? '- For accounting problems, present clean tables showing EBITDA -> EBIT -> EBT -> Net Income and balance sheet reconciliation.'
        : '- Define every symbol with its SI unit on first mention, and close solved problems with a brief SI dimensional check.',
      '- ALWAYS write LaTeX cleanly for KaTeX: put EVERY standalone or key equation on its own lines inside $$...$$, and wrap inline symbols in $...$. Never use \\euro (write € inside \\text{}), and never put bare & inside \\text{}.',
      '- Stay faithful to the UC3M course notation and sign conventions from the course notes below.',
      lang === 'es'
        ? '- Answer in natural, clear academic Spanish (unless the student writes in English). On first mention of a key English course term, add it in brackets, e.g. esfuerzo cortante [shear stress].'
        : '- Answer in clear academic English (unless the student explicitly writes in Spanish, in which case reply in Spanish with [English technical terms] on first mention).'
    ];
    if (session.socratic) {
      lines.push('- SOCRATIC MODE IS ACTIVE: never reveal the final solution or the next full step unless the student writes "show solution". Ask one focused guiding question at a time.');
    }
    if (!prefs.thinking) lines.push('/no_think');
    if (session.systemExtra) lines.push('', session.systemExtra);
    if (ragText) lines.push('', ragText);
    return lines.join('\n');
  }

  /* ---------------------------------------------------------------- UI (Full Studio + Left History + Split Page) */
  function buildUI() {
    ensureStyles();

    var launcher = el('button', 'sd-launcher');
    launcher.type = 'button';
    launcher.id = 'siderisButton';
    launcher.setAttribute('aria-haspopup', 'dialog');
    launcher.setAttribute('aria-expanded', 'false');
    launcher.setAttribute('aria-controls', 'siderisDrawer');
    launcher.setAttribute('aria-label', 'Open Sideris AI tutor');
    launcher.title = 'Open Sideris AI tutor';
    var lMark = el('span', 'sd-launcher__mark');
    lMark.appendChild(svg(ICONS.brand, 15));
    launcher.appendChild(lMark);
    launcher.appendChild(el('span', 'sd-launcher__label', 'Sideris'));

    var backdrop = el('div', 'sd-backdrop');
    backdrop.hidden = true;

    var drawer = el('aside', 'sd-drawer');
    drawer.id = 'siderisDrawer';
    drawer.hidden = true;
    drawer.setAttribute('role', 'dialog');
    drawer.setAttribute('aria-modal', 'false');
    drawer.setAttribute('aria-labelledby', 'siderisTitle');

    /* ---- LEFT SIDEBAR (History + New Chat + Current Page + Settings) ---- */
    var sidebar = el('nav', 'sd-sidebar');
    sidebar.setAttribute('aria-label', 'Sideris conversation history');

    var sbTop = el('div', 'sd-sidebar__top');
    var brand = el('div', 'sd-brand');
    var bIcon = el('span', 'sd-brand__icon');
    bIcon.appendChild(svg(ICONS.brand, 16));
    var title = el('h2', 'sd-title', 'Sideris');
    title.id = 'siderisTitle';
    brand.appendChild(bIcon);
    brand.appendChild(title);
    sbTop.appendChild(brand);

    var newBtn = el('button', 'sd-new-chat');
    newBtn.type = 'button';
    newBtn.appendChild(svg(ICONS.plus, 15));
    newBtn.appendChild(el('span', '', 'New chat'));

    var sbHead = el('div', 'sd-sidebar__head');
    sbHead.appendChild(el('p', 'sd-section-label', 'History'));
    var clearAllHistBtn = el('button', 'sd-link-btn', 'Clear all');
    clearAllHistBtn.type = 'button';
    sbHead.appendChild(clearAllHistBtn);

    var historyList = el('div', 'sd-history-list');

    var sbFoot = el('div', 'sd-sidebar__foot');
    var pagePill = el('div', 'sd-page-pill');
    pagePill.appendChild(el('span', 'sd-page-pill__label', 'Current page'));
    var contextSub = el('p', 'sd-context-sub', contextSubtitle());
    pagePill.appendChild(contextSub);

    var footRow = el('div', 'sd-foot-row');
    var settingsBtn = el('button', 'sd-foot-btn');
    settingsBtn.type = 'button';
    settingsBtn.setAttribute('aria-expanded', 'false');
    settingsBtn.appendChild(svg(ICONS.gear, 15));
    settingsBtn.appendChild(el('span', '', 'Settings'));
    footRow.appendChild(settingsBtn);

    sbFoot.appendChild(pagePill);
    sbFoot.appendChild(footRow);

    sidebar.appendChild(sbTop);
    sidebar.appendChild(newBtn);
    sidebar.appendChild(sbHead);
    sidebar.appendChild(historyList);
    sidebar.appendChild(sbFoot);

    /* ---- MAIN WORKSPACE COLUMN ---- */
    var main = el('div', 'sd-main');

    // Top bar
    var topbar = el('div', 'sd-topbar');
    var tbLeft = el('div', 'sd-topbar__left');
    var sbToggleBtn = el('button', 'sd-icon-btn');
    sbToggleBtn.type = 'button';
    sbToggleBtn.setAttribute('aria-label', 'Toggle history sidebar');
    sbToggleBtn.title = 'Toggle history sidebar';
    sbToggleBtn.appendChild(svg(ICONS.sidebar, 17));
    var topModelLabel = el('span', 'sd-topbar__model', 'Sideris Aether');
    var topModeTag = el('span', 'sd-topbar__tag', 'Instant');
    tbLeft.appendChild(sbToggleBtn);
    tbLeft.appendChild(topModelLabel);
    tbLeft.appendChild(topModeTag);

    var tbRight = el('div', 'sd-topbar__right');
    // Quick language switcher right in topbar
    var topLangSeg = el('div', 'sd-seg');
    var langBtns = [];
    [['es', 'ES'], ['en', 'EN']].forEach(function (pair) {
      var b = el('button', 'sd-seg__btn', pair[1]);
      b.type = 'button';
      b.dataset.lang = pair[0];
      b.title = pair[0] === 'es' ? 'Answer in Spanish' : 'Answer in English';
      b.addEventListener('click', function () { writeLang(pair[0]); syncUI(); });
      topLangSeg.appendChild(b);
      langBtns.push(b);
    });

    // Split page vs Fullscreen workspace toggle
    var layoutBtn = el('button', 'sd-pill-btn');
    layoutBtn.type = 'button';
    layoutBtn.title = 'Toggle split view with study page or full-screen AI';
    var layoutIconWrap = el('span');
    var layoutLabel = el('span', '', 'Split');
    layoutBtn.appendChild(layoutIconWrap);
    layoutBtn.appendChild(layoutLabel);

    var closeBtn = el('button', 'sd-icon-btn');
    closeBtn.type = 'button';
    closeBtn.setAttribute('aria-label', 'Close Sideris');
    closeBtn.title = 'Close (Esc)';
    closeBtn.appendChild(svg(ICONS.close, 17));

    tbRight.appendChild(topLangSeg);
    tbRight.appendChild(layoutBtn);
    tbRight.appendChild(closeBtn);
    topbar.appendChild(tbLeft);
    topbar.appendChild(tbRight);

    // Settings panel (collapsible under topbar)
    var settingsPanel = el('div', 'sd-subpanel');
    settingsPanel.hidden = true;
    var spInner = el('div', 'sd-subpanel__inner');
    var spHead = el('div', 'sd-subpanel__head');
    spHead.appendChild(el('p', 'sd-section-label', 'Tutor preferences'));
    var spClose = el('button', 'sd-link-btn', 'Done');
    spClose.type = 'button';
    spClose.addEventListener('click', function () { setSettings(false); });
    spHead.appendChild(spClose);
    spInner.appendChild(spHead);

    // RAG toggle
    var ragRow = el('div', 'sd-setting-row');
    var ragInfo = el('div');
    ragInfo.appendChild(el('span', 'sd-setting-name', 'Use UC3M course notes'));
    ragInfo.appendChild(el('span', 'sd-setting-hint', 'Ground answers in your Obsidian notes for this subject.'));
    var ragLab = el('label', 'sd-check');
    var ragCb = document.createElement('input');
    ragCb.type = 'checkbox';
    ragCb.checked = prefs.rag;
    ragLab.appendChild(ragCb);
    ragLab.appendChild(el('span', '', 'On'));
    ragRow.appendChild(ragInfo);
    ragRow.appendChild(ragLab);
    spInner.appendChild(ragRow);

    // Reasoning toggle
    var thinkRow = el('div', 'sd-setting-row');
    var thinkInfo = el('div');
    thinkInfo.appendChild(el('span', 'sd-setting-name', 'Show step-by-step reasoning'));
    thinkInfo.appendChild(el('span', 'sd-setting-hint', 'Display collapsible reasoning blocks for Orion and Titan.'));
    var thinkLab = el('label', 'sd-check');
    var thinkCb = document.createElement('input');
    thinkCb.type = 'checkbox';
    thinkCb.checked = prefs.thinking;
    thinkLab.appendChild(thinkCb);
    thinkLab.appendChild(el('span', '', 'On'));
    thinkRow.appendChild(thinkInfo);
    thinkRow.appendChild(thinkLab);
    spInner.appendChild(thinkRow);

    // Advanced / Offline
    var adv = el('details', 'sd-advanced');
    adv.appendChild(el('summary', '', 'Advanced: offline browser models, Ollama & API key'));
    var advBody = el('div', 'sd-advanced__body');

    var modeRow = el('div', 'sd-setting-row');
    var modeInfo = el('div');
    modeInfo.appendChild(el('span', 'sd-setting-name', 'Run mode'));
    modeInfo.appendChild(el('span', 'sd-setting-hint', 'Instant uses free cloud (0 MB). Offline downloads weights to GPU / Ollama.'));
    var modeSeg = el('div', 'sd-seg');
    var modeBtns = [];
    [['instant', 'Instant (0 MB)'], ['offline', 'Offline / Local']].forEach(function (pair) {
      var b = el('button', 'sd-seg__btn', pair[1]);
      b.type = 'button';
      b.dataset.mode = pair[0];
      b.addEventListener('click', function () {
        prefs.runMode = pair[0];
        savePrefs();
        hideProgress();
        syncUI();
      });
      modeSeg.appendChild(b);
      modeBtns.push(b);
    });
    modeRow.appendChild(modeInfo);
    modeRow.appendChild(modeSeg);
    advBody.appendChild(modeRow);

    var advNote = el('p', 'sd-help-note');
    advBody.appendChild(advNote);

    var loadRow = el('div', 'sd-load-row');
    var loadBtn = el('button', 'sd-btn sd-btn--primary', 'Test cloud connection');
    loadBtn.type = 'button';
    var clearCacheBtn = el('button', 'sd-btn', 'Clear browser cache');
    clearCacheBtn.type = 'button';
    loadRow.appendChild(loadBtn);
    loadRow.appendChild(clearCacheBtn);
    advBody.appendChild(loadRow);

    var progressWrap = el('div', 'sd-progress');
    progressWrap.hidden = true;
    var progressBar = el('div', 'sd-progress__bar');
    var progressFill = el('div', 'sd-progress__fill');
    progressBar.appendChild(progressFill);
    var progressText = el('p', 'sd-progress__text');
    progressWrap.appendChild(progressBar);
    progressWrap.appendChild(progressText);
    advBody.appendChild(progressWrap);

    var cloudWrap = el('div', 'sd-advanced__body');
    var wField = el('div', 'sd-field');
    var wLab = el('label', '', 'Cloud proxy URL (optional override)');
    wLab.setAttribute('for', 'sdWorkerUrl');
    var wInput = el('input', 'sd-input');
    wInput.id = 'sdWorkerUrl';
    wInput.type = 'url';
    wInput.placeholder = effectiveWorkerUrl() || 'https://sideris-ai.<your-name>.workers.dev';
    wInput.value = prefs.workerUrl;
    wField.appendChild(wLab);
    wField.appendChild(wInput);

    var pField = el('div', 'sd-field');
    var pLab = el('label', '', 'Personal free API key (optional, stored only in your browser)');
    pLab.setAttribute('for', 'sdByokProvider');
    var pSelect = el('select', 'sd-select');
    pSelect.id = 'sdByokProvider';
    [['gemini', 'Google Gemini (free AI Studio key)'], ['groq', 'Groq (free Llama 3.3 70B)'], ['openrouter', 'OpenRouter (:free models)']].forEach(function (pair) {
      var o = el('option', '', pair[1]);
      o.value = pair[0];
      pSelect.appendChild(o);
    });
    pSelect.value = prefs.byokProvider || 'gemini';
    pField.appendChild(pLab);
    pField.appendChild(pSelect);

    var kField = el('div', 'sd-field');
    var kInput = el('input', 'sd-input');
    kInput.id = 'sdByokKey';
    kInput.type = 'password';
    kInput.autocomplete = 'off';
    kInput.placeholder = 'Optional API key (leave empty to use free Sideris cloud)';
    kInput.value = prefs.byokKey;
    kField.appendChild(kInput);

    cloudWrap.appendChild(wField);
    cloudWrap.appendChild(pField);
    cloudWrap.appendChild(kField);
    advBody.appendChild(cloudWrap);

    var customWrap = el('div', 'sd-field');
    var customLab = el('label', '', 'Custom Hugging Face ONNX repo (for your fine-tuned Sideris weights)');
    customLab.setAttribute('for', 'sdCustomRepo');
    var customInput = el('input', 'sd-input');
    customInput.id = 'sdCustomRepo';
    customInput.type = 'text';
    customInput.placeholder = 'e.g. your-user/Sideris-Aether-ONNX';
    customInput.value = prefs.customRepo;
    customWrap.appendChild(customLab);
    customWrap.appendChild(customInput);
    advBody.appendChild(customWrap);

    var ollamaWrap = el('div', 'sd-advanced__body');
    var epField = el('div', 'sd-field');
    var epLab = el('label', '', 'Local OpenAI endpoint (Ollama / LM Studio)');
    epLab.setAttribute('for', 'sdOllamaEndpoint');
    var epInput = el('input', 'sd-input');
    epInput.id = 'sdOllamaEndpoint';
    epInput.type = 'url';
    epInput.value = prefs.ollamaEndpoint;
    epField.appendChild(epLab);
    epField.appendChild(epInput);

    var tagField = el('div', 'sd-field');
    var tagLab = el('label', '', 'Local model tag');
    tagLab.setAttribute('for', 'sdOllamaModel');
    var tagInput = el('input', 'sd-input');
    tagInput.id = 'sdOllamaModel';
    tagInput.type = 'text';
    tagInput.value = prefs.ollamaModel;
    tagField.appendChild(tagLab);
    tagField.appendChild(tagInput);
    ollamaWrap.appendChild(epField);
    ollamaWrap.appendChild(tagField);
    advBody.appendChild(ollamaWrap);

    adv.appendChild(advBody);
    spInner.appendChild(adv);
    settingsPanel.appendChild(spInner);

    // Scrollable message stream
    var messages = el('div', 'sd-messages');
    messages.setAttribute('aria-live', 'polite');

    // Centered composer + inline model picker popover
    var compWrap = el('div', 'sd-composer-wrap');
    var compBox = el('div', 'sd-composer-box');

    var modelMenu = el('div', 'sd-model-menu');
    modelMenu.hidden = true;
    modelMenu.setAttribute('role', 'menu');
    var mmHead = el('div', 'sd-model-menu__head');
    mmHead.appendChild(el('p', 'sd-section-label', 'Choose Sideris model'));
    modelMenu.appendChild(mmHead);

    var modelOptBtns = [];
    MODELS.forEach(function (m) {
      var opt = el('button', 'sd-model-opt');
      opt.type = 'button';
      opt.setAttribute('role', 'menuitemradio');
      opt.dataset.model = m.id;
      var row = el('span', 'sd-model-opt__row');
      row.appendChild(el('span', 'sd-model-opt__name', m.name));
      row.appendChild(el('span', 'sd-model-opt__badge', m.tier));
      opt.appendChild(row);
      opt.appendChild(el('span', 'sd-model-opt__desc', m.summary || m.bestFor || ''));
      opt.addEventListener('click', function () {
        selectModel(m.id);
        toggleModelMenu(false);
        ui.ta.focus();
      });
      modelMenu.appendChild(opt);
      modelOptBtns.push(opt);
    });

    var composer = el('form', 'sd-composer');
    var ta = el('textarea', 'sd-textarea');
    ta.rows = 1;
    ta.placeholder = 'Ask Sideris anything about this topic, a derivation, or a problem...';
    ta.setAttribute('aria-label', 'Message to Sideris');

    var bar = el('div', 'sd-composer__bar');
    var pickerBtn = el('button', 'sd-picker-btn');
    pickerBtn.type = 'button';
    pickerBtn.setAttribute('aria-haspopup', 'menu');
    pickerBtn.setAttribute('aria-expanded', 'false');
    pickerBtn.title = 'Switch Sideris model';
    var pickerName = el('span', 'sd-picker-btn__name', 'Sideris Aether');
    var pickerMode = el('span', 'sd-picker-btn__mode', '· Instant');
    pickerBtn.appendChild(pickerName);
    pickerBtn.appendChild(pickerMode);
    pickerBtn.appendChild(svg(ICONS.chevUp, 13));

    var sendBtn = el('button', 'sd-send', 'Send');
    sendBtn.type = 'submit';

    bar.appendChild(pickerBtn);
    bar.appendChild(sendBtn);
    composer.appendChild(ta);
    composer.appendChild(bar);

    compBox.appendChild(modelMenu);
    compBox.appendChild(composer);
    var status = el('div', 'sd-status-line', 'Sideris ready · grounded in your UC3M notes.');
    status.setAttribute('role', 'status');
    compWrap.appendChild(compBox);
    compWrap.appendChild(status);

    main.appendChild(topbar);
    main.appendChild(settingsPanel);
    main.appendChild(messages);
    main.appendChild(compWrap);

    drawer.appendChild(sidebar);
    drawer.appendChild(main);

    document.body.appendChild(launcher);
    document.body.appendChild(backdrop);
    document.body.appendChild(drawer);

    ui = {
      launcher: launcher, backdrop: backdrop, drawer: drawer,
      sidebar: sidebar, sbToggleBtn: sbToggleBtn, layoutBtn: layoutBtn,
      layoutIconWrap: layoutIconWrap, layoutLabel: layoutLabel,
      topModelLabel: topModelLabel, topModeTag: topModeTag,
      settingsBtn: settingsBtn, settingsPanel: settingsPanel,
      historyList: historyList, clearAllHistBtn: clearAllHistBtn,
      modelMenu: modelMenu, modelOptBtns: modelOptBtns,
      pickerBtn: pickerBtn, pickerName: pickerName, pickerMode: pickerMode,
      modeBtns: modeBtns, langBtns: langBtns, advNote: advNote,
      loadBtn: loadBtn, clearCacheBtn: clearCacheBtn,
      progressWrap: progressWrap, progressFill: progressFill, progressText: progressText,
      cloudWrap: cloudWrap, wInput: wInput, pSelect: pSelect, kInput: kInput,
      customWrap: customWrap, customInput: customInput,
      ollamaWrap: ollamaWrap, epInput: epInput, tagInput: tagInput,
      ragCb: ragCb, thinkCb: thinkCb,
      messages: messages, status: status, ta: ta, sendBtn: sendBtn
    };

    // Events
    launcher.addEventListener('click', function () { if (session.open) close(false); else open(); });
    backdrop.addEventListener('click', function () { close(true); });
    closeBtn.addEventListener('click', function () { close(true); });
    newBtn.addEventListener('click', function () {
      clearChat();
      session.mobileHistoryOpen = false;
      setSettings(false);
      syncLayoutClasses();
    });
    settingsBtn.addEventListener('click', function () { setSettings(!session.settingsOpen); });
    pickerBtn.addEventListener('click', function () { toggleModelMenu(); });

    sbToggleBtn.addEventListener('click', function () {
      if (window.innerWidth < 980) {
        session.mobileHistoryOpen = !session.mobileHistoryOpen;
      } else {
        session.sidebarCollapsed = !session.sidebarCollapsed;
      }
      syncLayoutClasses();
    });

    layoutBtn.addEventListener('click', function () {
      prefs.layout = prefs.layout === 'full' ? 'split' : 'full';
      savePrefs();
      syncLayoutClasses();
    });

    clearAllHistBtn.addEventListener('click', function () {
      chats = [];
      saveHistoryStore(chats);
      renderHistory();
      setStatus('Cleared saved conversation history.');
    });

    loadBtn.addEventListener('click', function () { preloadActiveModel(); });
    clearCacheBtn.addEventListener('click', function () {
      if (!window.AESiderisEngine) return;
      window.AESiderisEngine.clearBrowserCache().then(function (n) {
        setStatus(n ? 'Cleared ' + n + ' browser model cache store(s).' : 'No cached browser models found.');
        syncUI();
      });
    });

    customInput.addEventListener('change', function () { prefs.customRepo = customInput.value.trim(); savePrefs(); syncUI(); });
    wInput.addEventListener('change', function () { prefs.workerUrl = wInput.value.trim(); savePrefs(); syncUI(); });
    pSelect.addEventListener('change', function () { prefs.byokProvider = pSelect.value; savePrefs(); syncUI(); });
    kInput.addEventListener('change', function () { prefs.byokKey = kInput.value.trim(); savePrefs(); syncUI(); });
    epInput.addEventListener('change', function () { prefs.ollamaEndpoint = epInput.value.trim() || 'http://localhost:11434/v1'; savePrefs(); });
    tagInput.addEventListener('change', function () { prefs.ollamaModel = tagInput.value.trim() || 'qwen3.5:9b'; savePrefs(); });
    ragCb.addEventListener('change', function () { prefs.rag = ragCb.checked; savePrefs(); });
    thinkCb.addEventListener('change', function () { prefs.thinking = thinkCb.checked; savePrefs(); renderMessages(); });

    ta.addEventListener('input', function () {
      ta.style.height = 'auto';
      ta.style.height = Math.min(180, ta.scrollHeight) + 'px';
    });

    composer.addEventListener('submit', function (e) {
      e.preventDefault();
      if (session.busy) {
        if (window.AESiderisEngine) window.AESiderisEngine.abort();
        return;
      }
      var text = ta.value.trim();
      if (!text) return;
      ta.value = '';
      ta.style.height = 'auto';
      toggleModelMenu(false);
      sendUserMessage(text);
    });

    ta.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        composer.dispatchEvent(new Event('submit', { cancelable: true }));
      }
    });

    drawer.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        e.stopPropagation();
        if (session.modelMenuOpen) { toggleModelMenu(false); ui.pickerBtn.focus(); return; }
        if (session.settingsOpen) { setSettings(false); return; }
        if (session.mobileHistoryOpen) { session.mobileHistoryOpen = false; syncLayoutClasses(); return; }
        close(true);
      }
    });

    drawer.addEventListener('click', function (e) {
      if (session.modelMenuOpen && !ui.modelMenu.contains(e.target) && !ui.pickerBtn.contains(e.target)) {
        toggleModelMenu(false);
      }
      if (session.mobileHistoryOpen && !ui.sidebar.contains(e.target) && !ui.sbToggleBtn.contains(e.target)) {
        session.mobileHistoryOpen = false;
        syncLayoutClasses();
      }
    });

    document.addEventListener('click', function (e) {
      if (!session.open || !e.target || !e.target.closest) return;
      if (e.target.closest('#focusLabButton, #pomodoroButton, .upd-bell, .ae-nav-btn')) close(false);
    }, true);

    syncUI();
    renderHistory();
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

  function setSettings(openFlag) {
    session.settingsOpen = !!openFlag;
    if (ui.settingsPanel) ui.settingsPanel.hidden = !session.settingsOpen;
    if (ui.settingsBtn) ui.settingsBtn.setAttribute('aria-expanded', session.settingsOpen ? 'true' : 'false');
    if (session.settingsOpen) syncUI();
  }

  function toggleModelMenu(force) {
    session.modelMenuOpen = force != null ? !!force : !session.modelMenuOpen;
    if (ui.modelMenu) ui.modelMenu.hidden = !session.modelMenuOpen;
    if (ui.pickerBtn) ui.pickerBtn.setAttribute('aria-expanded', session.modelMenuOpen ? 'true' : 'false');
  }

  function syncLayoutClasses() {
    if (!ui.drawer) return;
    var isFull = prefs.layout === 'full';
    ui.drawer.classList.toggle('is-full', isFull);
    ui.drawer.classList.toggle('is-sidebar-collapsed', !!session.sidebarCollapsed);
    ui.drawer.classList.toggle('is-mobile-history', !!session.mobileHistoryOpen);

    document.documentElement.classList.toggle('sd-studio-split', session.open && !isFull);
    document.documentElement.classList.toggle('sd-studio-full', session.open && isFull);

    if (ui.layoutBtn) {
      ui.layoutBtn.setAttribute('aria-pressed', isFull ? 'true' : 'false');
      ui.layoutLabel.textContent = isFull ? 'Show page' : 'Full screen';
      ui.layoutIconWrap.textContent = '';
      ui.layoutIconWrap.appendChild(svg(isFull ? ICONS.split : ICONS.expand, 14));
    }
  }

  function renderHistory() {
    if (!ui.historyList) return;
    ui.historyList.textContent = '';
    if (ui.clearAllHistBtn) ui.clearAllHistBtn.hidden = chats.length === 0;
    if (!chats.length) {
      ui.historyList.appendChild(el('p', 'sd-history-empty', 'Your conversations will be saved here automatically.'));
      return;
    }
    chats.forEach(function (c) {
      var item = el('div', 'sd-history-item' + (c.id === session.chatId ? ' is-active' : ''));
      var openBtn = el('button', 'sd-history-open');
      openBtn.type = 'button';
      openBtn.appendChild(el('span', 'sd-history-title', c.title));
      var mName = findModel(c.modelId).name.replace(/^Sideris\s+/i, '');
      openBtn.appendChild(el('span', 'sd-history-meta', [c.subject, mName, formatStamp(c.updatedAt)].filter(Boolean).join(' · ')));
      openBtn.addEventListener('click', function () { loadConversation(c.id); });

      var delBtn = el('button', 'sd-history-del', '×');
      delBtn.type = 'button';
      delBtn.setAttribute('aria-label', 'Delete conversation ' + c.title);
      delBtn.addEventListener('click', function () { deleteConversation(c.id); });

      item.appendChild(openBtn);
      item.appendChild(delBtn);
      ui.historyList.appendChild(item);
    });
  }

  function syncUI() {
    if (!ui.drawer) return;
    var m = activeModelConfig();
    var isCloud = m.backend === 'cloud';
    var isOllama = m.backend === 'ollama';
    var isWebGPU = m.backend === 'webgpu';

    var modeLabel = isCloud ? 'Instant' : isOllama ? 'Local' : 'Offline';
    ui.pickerName.textContent = m.name;
    ui.pickerMode.textContent = '· ' + modeLabel;
    ui.topModelLabel.textContent = m.name;
    ui.topModeTag.textContent = modeLabel;

    ui.modelOptBtns.forEach(function (b) {
      b.setAttribute('aria-checked', b.dataset.model === m.id ? 'true' : 'false');
      var badge = b.querySelector('.sd-model-opt__badge');
      var info = findModel(b.dataset.model);
      if (badge && info) {
        badge.textContent = prefs.runMode === 'offline'
          ? (info.tier + ' · ' + (info.offlineSizeLabel || info.sizeLabel))
          : info.tier;
      }
    });

    ui.modeBtns.forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.mode === prefs.runMode ? 'true' : 'false');
    });

    var lang = readLang();
    ui.langBtns.forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.lang === lang ? 'true' : 'false');
    });

    ui.cloudWrap.hidden = !isCloud;
    ui.customWrap.hidden = !isWebGPU;
    ui.ollamaWrap.hidden = !isOllama;
    ui.clearCacheBtn.hidden = !isWebGPU;

    if (isCloud) {
      var wUrl = effectiveWorkerUrl();
      ui.advNote.textContent = prefs.byokKey
        ? ('Using your personal ' + prefs.byokProvider + ' key (browser-only).')
        : wUrl ? ('Connected to free Sideris cloud (' + wUrl + ').')
        : 'Paste a Worker URL or personal free key below, or switch to Offline / Local.';
      ui.loadBtn.textContent = prefs.byokKey ? 'Clear personal key' : 'Test cloud connection';
    } else if (isOllama) {
      ui.advNote.textContent = 'Connects to Ollama or LM Studio on localhost (' + m.repo + ').';
      ui.loadBtn.textContent = 'Test local connection';
    } else {
      ui.advNote.textContent = 'Downloads ' + m.repo + ' (' + m.sizeLabel + ') once into browser cache for offline use.';
      ui.loadBtn.textContent = (window.AESiderisEngine && window.AESiderisEngine.isLoaded(m.repo, m.dtype))
        ? 'Loaded in GPU'
        : ('Download & load (' + m.sizeLabel + ')');
    }

    syncLayoutClasses();

    var guideCards = ui.messages ? ui.messages.querySelectorAll('.sd-guide-card') : [];
    for (var i = 0; i < guideCards.length; i++) {
      guideCards[i].setAttribute('aria-pressed', guideCards[i].dataset.model === m.id ? 'true' : 'false');
    }
  }

  function selectModel(id) {
    var m = findModel(id);
    prefs.modelId = m.id;
    savePrefs();
    hideProgress();
    syncUI();
    setStatus(m.name + ' selected · ' + (m.bestFor || m.summary || 'ready.'));
  }

  function preloadActiveModel() {
    if (!window.AESiderisEngine) return Promise.resolve();
    var m = activeModelConfig();
    if (m.backend === 'cloud') {
      if (prefs.byokKey) {
        prefs.byokKey = '';
        if (ui.kInput) ui.kInput.value = '';
        savePrefs();
        syncUI();
        setStatus('Cleared personal API key from this browser.');
        return Promise.resolve();
      }
      var wUrl = effectiveWorkerUrl();
      setStatus(wUrl ? 'Checking Sideris cloud...' : 'No Cloudflare Worker URL configured.');
      return window.AESiderisEngine.checkCloud(wUrl).then(function (res) {
        if (res.ok) {
          var provs = res.providers && res.providers.length ? ' (' + res.providers.join(', ') + ')' : '';
          setStatus('Sideris cloud connected' + provs + '.');
        } else {
          setStatus('Cloud proxy unreachable: ' + res.error);
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
      syncUI();
      setStatus(m.name + ' ready in GPU memory (cached offline).');
    }).catch(function (err) {
      ui.loadBtn.disabled = false;
      hideProgress();
      setStatus(err && err.message ? err.message : String(err));
    });
  }

  function regenerateLast() {
    if (session.busy || session.messages.length < 2) return;
    var last = session.messages[session.messages.length - 1];
    if (last.role !== 'assistant') return;
    session.messages.pop();
    var prevUser = session.messages.pop();
    if (!prevUser || prevUser.role !== 'user') return;
    sendUserMessage(prevUser.displayText || prevUser.text, {
      displayText: prevUser.displayText || prevUser.text,
      modelPrompt: prevUser.text,
      tag: prevUser.tag || ''
    });
  }

  function renderMessages() {
    if (!ui.messages) return;
    ui.messages.textContent = '';

    if (!session.messages.length) {
      var wrap = el('div', 'sd-welcome');

      var hero = el('div', 'sd-welcome-hero');
      hero.appendChild(el('h3', 'sd-welcome__title', 'What are we studying today?'));
      hero.appendChild(el('p', 'sd-welcome__body',
        'Grounded in your UC3M Aerospace notes for ' + contextSubtitle() + '. Pick a Sideris model or ask directly below:'));
      wrap.appendChild(hero);

      var grid = el('div', 'sd-guide-grid');
      MODELS.forEach(function (m) {
        var b = el('button', 'sd-guide-card');
        b.type = 'button';
        b.dataset.model = m.id;
        b.setAttribute('aria-pressed', m.id === prefs.modelId ? 'true' : 'false');
        var top = el('span', 'sd-guide-card__top');
        top.appendChild(el('span', 'sd-guide-card__name', m.name));
        top.appendChild(el('span', 'sd-guide-card__tier', m.tier));
        b.appendChild(top);
        b.appendChild(el('span', 'sd-guide-card__desc', m.bestFor || m.summary));
        b.addEventListener('click', function () { selectModel(m.id); });
        grid.appendChild(b);
      });
      wrap.appendChild(grid);

      var starters = isProblemPage() ? [
        'Summarise the step-by-step solving method for this unit',
        'What are the most common exam mistakes in these problems?',
        'Walk me through the governing equations and sign conventions',
        'Quiz me with a quick conceptual check before I solve'
      ] : [
        'Summarise the key equations and hypotheses of this topic',
        'Explain the physical intuition behind this page clearly',
        'Derive the main equation on this page step by step',
        'Quiz me with 3 exam-style questions on this topic'
      ];
      var qWrap = el('div', 'sd-quick');
      starters.forEach(function (q) {
        var qb = el('button', 'sd-quick__btn', q);
        qb.type = 'button';
        qb.addEventListener('click', function () { sendUserMessage(q); });
        qWrap.appendChild(qb);
      });
      wrap.appendChild(qWrap);

      ui.messages.appendChild(wrap);
      return;
    }

    var stream = el('div', 'sd-stream');
    session.messages.forEach(function (msg, idx) {
      var isLast = idx === session.messages.length - 1;
      var card = el('article', 'sd-msg sd-msg--' + msg.role + (msg.error ? ' sd-msg--error' : ''));
      var head = el('div', 'sd-msg__head');
      var roleText = msg.role === 'user' ? 'You' : (msg.modelName || 'Sideris');
      head.appendChild(el('span', 'sd-msg__role', roleText));
      if (msg.role === 'assistant' && !session.busy) {
        var acts = el('div', 'sd-msg__actions');
        if (isLast) {
          var retry = el('button', 'sd-msg__action', 'Retry');
          retry.type = 'button';
          retry.title = 'Regenerate with currently selected Sideris model';
          retry.addEventListener('click', regenerateLast);
          acts.appendChild(retry);
        }
        if (msg.text && !msg.error) {
          var copy = el('button', 'sd-msg__action', 'Copy');
          copy.type = 'button';
          copy.addEventListener('click', function () {
            if (navigator.clipboard && navigator.clipboard.writeText) {
              navigator.clipboard.writeText(msg.text).then(function () {
                copy.textContent = 'Copied';
                setTimeout(function () { copy.textContent = 'Copy'; }, 1200);
              });
            }
          });
          acts.appendChild(copy);
        }
        head.appendChild(acts);
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

      stream.appendChild(card);
      msg._contentEl = content;
    });
    ui.messages.appendChild(stream);
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

    if (!session.chatId) session.chatId = makeChatId();
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
    setSettings(false);
    renderMessages();
    setBusy(true);
    setStatus(
      m.backend === 'cloud' ? m.name + ' is responding...'
        : m.backend === 'ollama' ? m.name + ' (local) is responding...'
        : 'Preparing ' + m.name + '...'
    );

    var ragQuery = opts.ragQuery || (pageTitle() + ' ' + text);
    var ragPromise = (prefs.rag && window.AESiderisRAG)
      ? window.AESiderisRAG.search(ragQuery, { limit: 4 })
      : Promise.resolve([]);

    var rafPending = false;
    function scheduleStreamRender() {
      if (rafPending) return;
      rafPending = true;
      requestAnimationFrame(function () {
        rafPending = false;
        if (assistantMsg._contentEl) {
          renderRichText(assistantMsg._contentEl, assistantMsg.text);
          ui.messages.scrollTop = ui.messages.scrollHeight;
        }
      });
    }

    return ragPromise.then(function (hits) {
      assistantMsg.ragHits = hits || [];
      var ragText = (hits && hits.length && window.AESiderisRAG) ? window.AESiderisRAG.formatContext(hits) : '';
      var sys = buildSystemPrompt(ragText, lang);
      var apiMessages = [{ role: 'system', content: sys }];
      var hist = session.messages.slice(0, -1).slice(-10);
      hist.forEach(function (item) {
        apiMessages.push({ role: item.role, content: item.text });
      });

      return window.AESiderisEngine.generate(
        {
          model: m,
          messages: apiMessages,
          maxTokens: session.socratic ? 512 : 1800,
          cloud: {
            workerUrl: effectiveWorkerUrl(),
            byokProvider: prefs.byokProvider || 'gemini',
            byokKey: prefs.byokKey || ''
          }
        },
        function (_chunk, full) {
          assistantMsg.text = full;
          scheduleStreamRender();
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
      persistCurrentChat();
      syncUI();
      renderMessages();
      setStatus(m.name + ' · ready.');
      ui.ta.focus();
      return assistantMsg.text;
    }).catch(function (err) {
      hideProgress();
      setBusy(false);
      assistantMsg.error = true;
      assistantMsg.text = (err && err.message) ? err.message : String(err);
      persistCurrentChat();
      renderMessages();
      setStatus('Error: ' + assistantMsg.text);
    });
  }

  /* ---------------------------------------------------------------- Ask AI handoff */
  function openWithAskRequest(payload) {
    if (!payload) return;
    open();
    session.chatId = makeChatId();
    session.messages = [];
    session.socratic = !!payload.socratic;
    session.systemExtra = payload.hiddenContext || '';
    if (payload.lang === 'es' || payload.lang === 'en') {
      writeLang(payload.lang);
      syncUI();
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
    session.chatId = '';
    session.messages = [];
    session.systemExtra = '';
    session.socratic = false;
    setBusy(false);
    renderHistory();
    renderMessages();
    setStatus('New conversation.');
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
    syncUI();
    renderHistory();
    requestAnimationFrame(function () {
      ui.backdrop.classList.add('is-open');
      ui.drawer.classList.add('is-open');
    });
    ui.ta.focus({ preventScroll: true });
  }

  function close(returnFocus) {
    if (!session.open || !ui.drawer) return;
    session.open = false;
    session.mobileHistoryOpen = false;
    toggleModelMenu(false);
    setSettings(false);
    syncLayoutClasses();
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
    CHATS_KEY: CHATS_KEY,
    open: open,
    close: close,
    isOpen: function () { return session.open; },
    models: function () { return MODELS.slice(); },
    selectModel: selectModel,
    openWithAskRequest: openWithAskRequest,
    sendUserMessage: sendUserMessage,
    clearChat: clearChat,
    history: function () { return chats.slice(); },
    loadConversation: loadConversation,
    deleteConversation: deleteConversation,
    renderRichText: renderRichText,
    state: function () {
      return {
        open: session.open,
        busy: session.busy,
        model: activeModelConfig(),
        runMode: prefs.runMode,
        layout: prefs.layout,
        rag: prefs.rag,
        thinking: prefs.thinking,
        chatId: session.chatId,
        count: session.messages.length,
        savedChats: chats.length
      };
    }
  };
})();
