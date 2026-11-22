/*!
 * Sideris AI Tutor: public cloud-proxy configuration.
 *
 * Loaded on study pages by assets/js/theme.js right before assets/data/ai-models.js.
 * Points to the deployed Cloudflare Worker (tools/cloudflare/sideris-worker.js) so Sideris Lux,
 * Sideris Aether, Sideris Orion and Sideris Titan all work immediately with 0 MB download on
 * desktop and mobile. Setup & optional extra keys: docs/sideris-ai-setup.md.
 *
 * SECURITY: Never put any API key in this file. Provider secrets live strictly on Cloudflare.
 */
window.AE_SIDERIS_CONFIG = window.AE_SIDERIS_CONFIG || {
  workerUrl: 'https://sideris-ai.fitplan.workers.dev'
};
