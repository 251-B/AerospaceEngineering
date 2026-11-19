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
 * Inference runs only on Cloudflare Workers AI (`env.AI`); each profile tries its models in order.
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
    cfModels: [
      '@cf/meta/llama-3.1-8b-instruct-fast',
      '@cf/meta/llama-3.2-3b-instruct',
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
    ],
  },
  'sideris-aether': {
    temperature: 0.35,
    maxTokens: 1600,
    cfModels: [
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
      '@cf/qwen/qwen3.8-27b',
      '@cf/meta/llama-3.1-8b-instruct-fast',
    ],
  },
  'sideris-orion': {
    // Reasoning model: on long derivations the reasoning alone used 2048 tokens and no answer was written.
    maxTokensCap: 6144,
    temperature: 0.2,
    maxTokens: 1800,
    cfModels: [
      '@cf/qwen/qwen3.8-27b',
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
    ],
  },
  'sideris-titan': {
    // Reasoning model: on long derivations the reasoning alone used 2048 tokens and no answer was written.
    maxTokensCap: 6144,
    temperature: 0.25,
    maxTokens: 2048,
    cfModels: [
      '@cf/qwen/qwen3.8-27b',
      '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
    ],
  },
};

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
      const providers = env.AI ? ['cloudflare-ai'] : [];
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

    // Students only ever see these two generic messages; provider details (quota, plan, model
    // errors) go to the Worker logs, never to the page.
    let lastStatus = 502;
    let lastError = 'Sideris is temporarily unavailable. Please try again in a moment.';

    // Cloudflare Workers AI: try the profile's models in order
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
          const detail = err && err.message ? err.message : String(err);
          console.error(`cloudflare-ai (${cfModel}): ${detail}`);
          if (/\b4006\b|daily free allocation|neurons/i.test(detail)) {
            lastStatus = 429;
            lastError = 'Sideris has reached its daily limit. It will be back tomorrow; Offline mode still works.';
            break;   // the daily allocation is shared by every model: no point trying the next one
          }
        }
      }
    }

    return jsonResponse({ error: lastError }, lastStatus === 429 ? 429 : 502, cors);
  },
};
