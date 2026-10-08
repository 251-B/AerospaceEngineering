/*!
 * Aerospace Engineering Study Portal: theme manager
 *
 * Load synchronously in <head> (before any stylesheet-dependent paint) so the stored theme
 * is on <html data-theme> before <body> is parsed:
 *     <script src="assets/js/theme.js"></script>
 *
 * Single storage key: 'ae_theme' ('dark' | 'light'). Values left by earlier pages under
 * 'aero-portal-theme' or 'theme' are migrated once, then ignored. Default theme: dark.
 *
 * API: window.AETheme = { get(), set(theme), toggle(), KEY }
 * Wiring: #themeToggle (click) and #themeLabel (text 'Dark' | 'Light') are picked up when present.
 * Event:  document 'ae-theme-change' with detail { theme }.
 */
(function () {
  'use strict';

  var KEY = 'ae_theme';
  var LEGACY_KEYS = ['aero-portal-theme', 'theme'];
  var DEFAULT_THEME = 'dark';
  var root = document.documentElement;

  function isValid(theme) {
    return theme === 'dark' || theme === 'light';
  }

  function read(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }

  function write(key, value) {
    try { localStorage.setItem(key, value); } catch (e) { /* storage blocked: keep the theme in memory only */ }
  }

  function stored() {
    var value = read(KEY);
    if (isValid(value)) return value;
    for (var i = 0; i < LEGACY_KEYS.length; i++) {
      value = read(LEGACY_KEYS[i]);
      if (isValid(value)) {
        write(KEY, value);
        return value;
      }
    }
    return null;
  }

  function get() {
    return stored() || DEFAULT_THEME;
  }

  function render(theme) {
    root.setAttribute('data-theme', theme);
    var label = document.getElementById('themeLabel');
    if (label) label.textContent = theme === 'dark' ? 'Dark' : 'Light';
    document.dispatchEvent(new CustomEvent('ae-theme-change', { detail: { theme: theme } }));
  }

  function set(theme) {
    if (!isValid(theme)) return;
    write(KEY, theme);
    render(theme);
  }

  function toggle() {
    set(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  }

  // Apply immediately: this runs in <head>, before the body paints.
  root.setAttribute('data-theme', get());

  // Another tab changed the theme.
  window.addEventListener('storage', function (event) {
    if (event.key === KEY && isValid(event.newValue)) render(event.newValue);
  });

  document.addEventListener('DOMContentLoaded', function () {
    render(root.getAttribute('data-theme'));
    var button = document.getElementById('themeToggle');
    if (button) button.addEventListener('click', toggle);
  });

  window.AETheme = { get: get, set: set, toggle: toggle, KEY: KEY };
})();
