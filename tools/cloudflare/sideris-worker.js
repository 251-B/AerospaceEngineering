/**
 * Sideris Instant AI Proxy — Free Cloudflare Worker (zero dependencies).
 *
 * Keeps your free-tier API keys hidden on Cloudflare while letting every student on the
 * static portal chat instantly (0 MB download, works on phones) with automatic fallback:
 *   1. Google AI Studio (Gemini Flash — OpenAI-compatible streaming endpoint)
 *   2. Groq (high-speed open-weight models)
 *   3. OpenRouter (:free reasoning models)
 *
 * Setup & deploy instructions: docs/sideris-ai-setup.md
 * Secrets (never committed): GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY
 */

const MAX_BODY_BYTES = 48 * 1024;
const MAX_TOKENS_CAP = 2048;
const RATE_WINDOW_MS = 60_000;
const RATE_LIMIT = 25;

// Best-effort per-isolate rate limiter (free plan has no KV/DO requirement).
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
    'Access-Control-Expose-Headers': 'X-Sideris-Provider',
    'Vary': 'Origin',
  };
}

function buildProviders(env) {
  const list = [];
  if (env.GEMINI_API_KEY) {
    list.push({
      name: 'gemini',
      url: 'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions',
      model: env.GEMINI_MODEL || 'gemini-3.8-flash',
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
      model: env.GROQ_MODEL || 'llama-3.3-70b-versatile',
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
      model: env.OPENROUTER_MODEL || 'openrouter/free',
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
      const providers = buildProviders(env).map((p) => p.name);
      return jsonResponse({ ok: providers.length > 0, providers }, 200, cors);
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

    const providers = buildProviders(env);
    if (!providers.length) {
      return jsonResponse({ error: 'No free API keys configured on this Worker yet.' }, 503, cors);
    }

    const cleanMessages = body.messages.map((m) => ({
      role: m.role === 'system' || m.role === 'assistant' ? m.role : 'user',
      content: String(m.content || '').slice(0, 16000),
    }));
    const temperature = typeof body.temperature === 'number'
      ? Math.max(0, Math.min(1.2, body.temperature))
      : 0.35;
    const maxTokens = typeof body.max_tokens === 'number'
      ? Math.max(64, Math.min(MAX_TOKENS_CAP, Math.round(body.max_tokens)))
      : 1400;
    const stream = body.stream !== false;

    let lastStatus = 502;
    let lastError = 'All configured free providers are currently busy.';

    for (const p of providers) {
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
            },
          });
        }
        lastStatus = upstream.status;
        lastError = `${p.name} returned HTTP ${upstream.status}`;
        // Retry next provider on quota/rate-limit/server errors.
        if (![401, 403, 404, 429, 500, 502, 503, 504].includes(upstream.status)) break;
      } catch (err) {
        lastStatus = 502;
        lastError = `${p.name} unreachable: ${err && err.message ? err.message : 'network error'}`;
      }
    }

    return jsonResponse({ error: lastError }, lastStatus === 429 ? 429 : 502, cors);
  },
};
