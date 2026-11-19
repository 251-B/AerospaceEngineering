# Sideris Instant AI Setup (Cloudflare Worker)

This guide covers the Cloudflare Worker that powers **Sideris Lux**, **Sideris Aether**,
**Sideris Orion** and **Sideris Titan** with **0 MB download** inside every study page (desktop and
mobile), grounded in the portal's `vault/` RAG shards.

- **Cloud inference:** the Worker runs every profile on Cloudflare Workers AI (`[ai] binding = "AI"`
  in `tools/cloudflare/wrangler.sideris.toml`); each profile tries its models in order
  (`PROFILE_DEFAULTS` in `tools/cloudflare/sideris-worker.js`). No other provider is used.
- **Answer length:** Orion and Titan are reasoning models and get up to 6144 tokens
  (`maxTokensCap` in the worker, `maxTokens` in `assets/data/ai-models.js`); Lux and Aether keep 2048.
- **Offline / Local mode:** visitors can also switch **Run mode -> Offline / Local** inside Settings
  to download WebGPU browser models (`Lux`, `Aether`, `Orion`) or connect local Ollama (`Titan`).

---

## 1. Deploy the Worker to your Cloudflare account

From the repository root:

```bash
npx wrangler login
npx wrangler deploy --config tools/cloudflare/wrangler.sideris.toml
```

Wrangler prints your public Worker URL, e.g.:
`https://sideris-ai.<your-subdomain>.workers.dev`

Test the health endpoint in your browser:
`https://sideris-ai.<your-subdomain>.workers.dev/health`
You should see `{"ok":true,"providers":["cloudflare-ai"],...}`.

---

## 2. Connect the portal

Edit `assets/data/sideris-config.js` and paste your public Worker URL:

```js
window.AE_SIDERIS_CONFIG = window.AE_SIDERIS_CONFIG || {
  workerUrl: 'https://sideris-ai.<your-subdomain>.workers.dev'
};
```

Commit and push. Every student now gets instant Sideris answers with zero downloads.
