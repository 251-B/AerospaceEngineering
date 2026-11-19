# Sideris Instant AI Setup (Free Cloudflare Worker)

This guide covers the free Cloudflare Worker that powers **Sideris Lux**, **Sideris Aether**,
**Sideris Orion** and **Sideris Titan** with **0 MB download** inside every study page (desktop and
mobile), grounded in the portal's `vault/` RAG shards.

- **Works out of the box with zero external API keys** via Cloudflare Workers AI (`[ai] binding = "AI"`,
  10,000 free Neurons/day: Llama 3.1 8B Fast, Llama 3.3 70B FP8 Fast, Qwen 3.8 27B).
- **Optional higher quota & frontier boost:** adding free secrets (`GEMINI_API_KEY`, `GROQ_API_KEY`,
  `OPENROUTER_API_KEY`) makes the Worker prefer those first and automatically fall back to Cloudflare AI.
- **Offline / Local mode:** visitors can also switch **Run mode -> Offline / Local** inside Settings
  to download WebGPU browser models (`Lux`, `Aether`, `Orion`) or connect local Ollama (`Titan`).

---

### Answer length and the free daily quota

Orion and Titan are reasoning models: on a long derivation their reasoning alone used the old
2048-token limit and no answer was written. They now get up to 6144 tokens (`maxTokensCap` in the
worker, `maxTokens` in `assets/data/ai-models.js`); Lux and Aether keep 2048. Measured on Workers
AI, an output token costs about 0.29 Neurons, so the 10,000 free Neurons a day are about 34,000
output tokens for the whole portal: roughly five full-length Orion/Titan answers, or about twenty
short ones. When they run out, Sideris stops until 00:00 UTC unless a Gemini or Groq key is set
(section 1): those are tried first and have far larger free quotas.

## 1. Get your free API keys (no credit card required)

At least **one** key is enough; adding two or three gives automatic fallback during exam weeks:

1. **Google AI Studio (Primary — Gemini Flash):** https://aistudio.google.com/apikey -> Create API key.
2. **Groq (Fallback 1 — ultra-fast open models):** https://console.groq.com/keys -> Create API key.
3. **OpenRouter (Fallback 2 — `:free` reasoning models):** https://openrouter.ai/keys -> Create key.

---

## 2. Deploy the Worker to your free Cloudflare account

From the repository root (free plan includes **100,000 requests/day**):

```bash
npx wrangler login
npx wrangler deploy --config tools/cloudflare/wrangler.sideris.toml
```

Wrangler prints your public Worker URL, e.g.:
`https://sideris-ai.<your-subdomain>.workers.dev`

---

## 3. Store the API keys as encrypted Worker secrets

Never commit API keys to Git. Push them directly to Cloudflare:

```bash
npx wrangler secret put GEMINI_API_KEY --config tools/cloudflare/wrangler.sideris.toml
npx wrangler secret put GROQ_API_KEY --config tools/cloudflare/wrangler.sideris.toml
npx wrangler secret put OPENROUTER_API_KEY --config tools/cloudflare/wrangler.sideris.toml
```

Test the health endpoint in your browser:
`https://sideris-ai.<your-subdomain>.workers.dev/health`
You should see `{"ok":true,"providers":["gemini","groq","openrouter"]}`.

---

## 4. Connect the portal

Edit `assets/data/sideris-config.js` and paste your public Worker URL:

```js
window.AE_SIDERIS_CONFIG = window.AE_SIDERIS_CONFIG || {
  workerUrl: 'https://sideris-ai.<your-subdomain>.workers.dev'
};
```

Commit and push. Every student now gets instant Sideris answers with zero downloads.

> **Alternative without deploying a Worker (BYOK):** Any visitor can also open **Sideris -> Settings**
> and paste their own free Google AI Studio, Groq or OpenRouter key; it stays only in their own browser.
