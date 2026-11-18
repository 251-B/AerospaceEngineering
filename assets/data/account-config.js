/*!
 * Sideris accounts: where they live. Read by assets/js/account.js (loaded by theme.js before it).
 *
 * Empty (as shipped): local mode, every account stays in its own browser.
 * Filled with a Supabase project: sign-up needs an invite code (single use, checked and spent by the
 * database: supabase/migrations/0001_sideris_accounts.sql), sign-in works on any device and each
 * reader's data is synced. Setup steps: docs/supabase-setup.md.
 *
 * Both values are public by design (they are in every visitor's browser); what protects the data
 * is the row level security of the database. Never put the service_role key here.
 */
window.AE_ACCOUNT_CONFIG = window.AE_ACCOUNT_CONFIG || {
  supabaseUrl: '',        // e.g. 'https://abcdefghijklmnop.supabase.co'
  supabaseAnonKey: '',    // Project Settings > API > Project API keys > anon / public
  requireInvite: true     // sign-up asks for an invite code
};
