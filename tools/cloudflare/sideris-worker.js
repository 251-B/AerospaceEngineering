/**
 * Sideris AI Proxy — Free Cloudflare Worker powering Sideris Lux, Aether, Orion & Titan
 * with ZERO downloads on desktop and mobile.
 *
 * Per-profile routing:
 *   - sideris-lux    : fast & crisp answers (low latency, quick theory/RAG checks)
 *   - sideris-aether : flagship balanced aerospace tutor (default)
 *   - sideris-orion  : deep calculus & step-by-step mathematical derivations
 *   - sideris-titan  : maximum reasoning depth for complex problems & exams
 *
 * Provider priority (automatic fallback):
 *   1. Optional free external secrets if configured (GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY)
 *   2. Built-in Cloudflare Workers AI (`env.AI`, 0 external keys needed, works out of the box!)
 */

const MAX_BODY_BYTES = 48 * 1024;
const MAX_TOKENS_CAP = 2048;   // default; a profile may set its own maxTokensCap
const RATE_WINDOW_MS = 60_000;
const RATE_LIMIT = 25;

const ipHits = new Map();

function checkRateLimit(ip) {
  const now = Date.now();
  const list = (ipHits.get(ip) || []).filter((t) => now - t < RATE_WINDOW_MS);
  if (list.length >= RATE_LIMIT) return false;
  list.push(now);
  ipHits.set(ip, list);
  if (ipHits.size > 2000) {
    for (const [k, v] of ipHits) {
      if (!v.length || now - v[v.length - 1] > RATE_WINDOW_MS) ipHits.delete(k);
    }
  }
  return true;
}

function isAllowedOrigin(origin, env) {
  if (!origin) return false;
  const custom = (env.ALLOWED_ORIGINS || '')
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean);
  if (custom.includes(origin)) return true;
  try {
    const u = new URL(origin);
    if (u.origin === 'https://251-b.github.io') return true;
    if (u.protocol === 'https:' && u.hostname.endsWith('.pages.dev')) return true;
    if ((u.hostname === 'localhost' || u.hostname === '127.0.0.1') && u.protocol === 'http:') return true;
  } catch {
    return false;
  }
  return false;
}

function corsHeaders(origin) {
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Expose-Headers': 'X-Sideris-Provider, X-Sideris-Profile',
    'Vary': 'Origin',
  };
}

const PROFILE_DEFAULTS = {
  'sideris-lux': {
    temperature: 0.35,
    maxTokens: 1024,
    geminiModel: 'gemini-2.5-flash-lite',
    groqModel: 'llama-3.1-8b-instant',
    openrouterModel: 'openrouter/free',
    cfModels: [
      '@cf/meta/llama-3.1-8b-instruct-fast',
      '@cf/meta/llama-3.2-3b-instruct',
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
    ],
  },
  'sideris-aether': {
    temperature: 0.35,
    maxTokens: 1600,
    geminiModel: 'gemini-3.8-flash',
    groqModel: 'llama-3.3-70b-versatile',
    openrouterModel: 'openrouter/free',
    cfModels: [
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
      '@cf/qwen/qwen3.8-27b',
      '@cf/meta/llama-3.1-8b-instruct-fast',
    ],
  },
  'sideris-orion': {
    // Reasoning models: the reasoning alone took the whole 2048 tokens on long derivations and no
    // answer was written. 6144 leaves room for both; about 0.29 Neurons per output token on
    // Workers AI, so one full-length answer uses ~1800 of the 10,000 free daily Neurons.
    maxTokensCap: 6144,
    temperature: 0.2,
    maxTokens: 1800,
    geminiModel: 'gemini-3.8-flash',
    groqModel: 'llama-3.3-70b-versatile',
    openrouterModel: 'deepseek/deepseek-r1:free',
    cfModels: [
      '@cf/qwen/qwen3.8-27b',
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
    ],
  },
  'sideris-titan': {
    // Reasoning models: the reasoning alone took the whole 2048 tokens on long derivations and no
    // answer was written. 6144 leaves room for both; about 0.29 Neurons per output token on
    // Workers AI, so one full-length answer uses ~1800 of the 10,000 free daily Neurons.
    maxTokensCap: 6144,
    temperature: 0.25,
    maxTokens: 2048,
    geminiModel: 'gemini-3.8-flash',
    groqModel: 'llama-3.3-70b-versatile',
    openrouterModel: 'openrouter/free',
    cfModels: [
      '@cf/qwen/qwen3.8-27b',
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
    ],
  },
};

function buildExternalProviders(env, profile) {
  const cfg = PROFILE_DEFAULTS[profile] || PROFILE_DEFAULTS['sideris-aether'];
  const list = [];
  if (env.GEMINI_API_KEY) {
    list.push({
      name: 'gemini',
      url: 'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions',
      model: profile === 'sideris-lux' ? cfg.geminiModel : (env.GEMINI_MODEL || cfg.geminiModel),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${env.GEMINI_API_KEY}`,
      },
    });
  }
  if (env.GROQ_API_KEY) {
    list.push({
      name: 'groq',
      url: 'https://api.groq.com/openai/v1/chat/completions',
      model: profile === 'sideris-lux' ? cfg.groqModel : (env.GROQ_MODEL || cfg.groqModel),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${env.GROQ_API_KEY}`,
      },
    });
  }
  if (env.OPENROUTER_API_KEY) {
    list.push({
      name: 'openrouter',
      url: 'https://openrouter.ai/api/v1/chat/completions',
      model: env.OPENROUTER_MODEL || cfg.openrouterModel,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${env.OPENROUTER_API_KEY}`,
        'HTTP-Referer': 'https://251-b.github.io/AerospaceEngineering/',
        'X-Title': 'Sideris Aerospace Study Portal',
      },
    });
  }
  return list;
}

function jsonResponse(obj, status, headers) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...headers },
  });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const allowed = isAllowedOrigin(origin, env);
    const cors = allowed ? corsHeaders(origin) : {};
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      if (!allowed) return new Response('Origin not allowed', { status: 403 });
      return new Response(null, { status: 204, headers: cors });
    }

    if (request.method === 'GET' && (url.pathname === '/' || url.pathname === '/health')) {
      const providers = buildExternalProviders(env, 'sideris-aether').map((p) => p.name);
      if (env.AI) providers.push('cloudflare-ai');
      return jsonResponse({
        ok: providers.length > 0,
        providers,
        profiles: Object.keys(PROFILE_DEFAULTS),
      }, 200, cors);
    }

    if (request.method !== 'POST' || url.pathname !== '/v1/chat/completions') {
      return jsonResponse({ error: 'Not found' }, 404, cors);
    }
    if (!allowed) {
      return jsonResponse({ error: 'Origin not allowed' }, 403, cors);
    }

    const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
    if (!checkRateLimit(ip)) {
      return jsonResponse({ error: 'Too many requests. Please wait a minute and try again.' }, 429, cors);
    }

    const raw = await request.text();
    if (raw.length > MAX_BODY_BYTES) {
      return jsonResponse({ error: 'Request payload is too large.' }, 413, cors);
    }

    let body;
    try {
      body = JSON.parse(raw);
    } catch {
      return jsonResponse({ error: 'Invalid JSON body.' }, 400, cors);
    }

    if (!Array.isArray(body.messages) || body.messages.length === 0 || body.messages.length > 24) {
      return jsonResponse({ error: 'Invalid messages array.' }, 400, cors);
    }

    const profile = PROFILE_DEFAULTS[body.profile] ? body.profile : (PROFILE_DEFAULTS[body.model] ? body.model : 'sideris-aether');
    const cfg = PROFILE_DEFAULTS[profile];

    const cleanMessages = body.messages.map((m) => ({
      role: m.role === 'system' || m.role === 'assistant' ? m.role : 'user',
      content: String(m.content || '').slice(0, 16000),
    }));
    const temperature = typeof body.temperature === 'number'
      ? Math.max(0, Math.min(1.2, body.temperature))
      : cfg.temperature;
    const maxTokens = typeof body.max_tokens === 'number'
      ? Math.max(64, Math.min(cfg.maxTokensCap || MAX_TOKENS_CAP, Math.round(body.max_tokens)))
      : cfg.maxTokens;
    const stream = body.stream !== false;

    let lastStatus = 502;
    let lastError = 'All configured providers are currently unavailable.';

    // 1. Try external free-tier providers if secrets are configured (highest quota & frontier quality)
    for (const p of buildExternalProviders(env, profile)) {
      try {
        const upstream = await fetch(p.url, {
          method: 'POST',
          headers: p.headers,
          body: JSON.stringify({
            model: p.model,
            messages: cleanMessages,
            temperature,
            max_tokens: maxTokens,
            stream,
          }),
        });
        if (upstream.ok) {
          return new Response(upstream.body, {
            status: 200,
            headers: {
              ...cors,
              'Content-Type': upstream.headers.get('Content-Type') || (stream ? 'text/event-stream; charset=utf-8' : 'application/json'),
              'Cache-Control': 'no-store',
              'X-Sideris-Provider': p.name,
              'X-Sideris-Profile': profile,
            },
          });
        }
        lastStatus = upstream.status;
        lastError = `${p.name} returned HTTP ${upstream.status}`;
      } catch (err) {
        lastStatus = 502;
        lastError = `${p.name} unreachable: ${err && err.message ? err.message : 'network error'}`;
      }
    }

    // 2. Built-in Cloudflare Workers AI fallback (works immediately with zero external keys!)
    if (env.AI) {
      for (const cfModel of cfg.cfModels) {
        try {
          const result = await env.AI.run(cfModel, {
            messages: cleanMessages,
            temperature,
            max_tokens: maxTokens,
            stream,
          });
          if (stream && result && typeof result.getReader === 'function') {
            return new Response(result, {
              status: 200,
              headers: {
                ...cors,
                'Content-Type': 'text/event-stream; charset=utf-8',
                'Cache-Control': 'no-store',
                'X-Sideris-Provider': 'cloudflare-ai:' + cfModel,
                'X-Sideris-Profile': profile,
              },
            });
          }
          const text = typeof result === 'string'
            ? result
            : (result && (result.response || (result.choices && result.choices[0] && result.choices[0].message && result.choices[0].message.content))) || '';
          return jsonResponse({
            choices: [{ message: { role: 'assistant', content: text } }],
          }, 200, {
            ...cors,
            'X-Sideris-Provider': 'cloudflare-ai:' + cfModel,
            'X-Sideris-Profile': profile,
          });
        } catch (err) {
          lastStatus = 502;
          lastError = `cloudflare-ai (${cfModel}): ${err && err.message ? err.message : 'error'}`;
        }
      }
    }

    return jsonResponse({ error: lastError }, lastStatus === 429 ? 429 : 502, cors);
  },
};
