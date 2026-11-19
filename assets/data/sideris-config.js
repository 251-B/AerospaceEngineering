/*!
 * Sideris AI Tutor: public cloud-proxy configuration.
 *
 * Loaded on study pages by assets/js/theme.js right before assets/data/ai-models.js.
 * Deploy tools/cloudflare/sideris-worker.js to your free Cloudflare Workers account (see
 * docs/sideris-ai-setup.md), then set `workerUrl` below to its public https://...workers.dev URL.
 *
 * SECURITY: Never put any API key in this file. All provider keys (GEMINI_API_KEY, GROQ_API_KEY,
 * OPENROUTER_API_KEY) live strictly as encrypted Cloudflare Worker secrets.
 */
window.AE_SIDERIS_CONFIG = window.AE_SIDERIS_CONFIG || {
  workerUrl: ''
};
