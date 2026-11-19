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
  supabaseUrl: 'https://qieouwnpffjquzhcnvoq.supabase.co',
  // anon / public key: safe in the browser, the database's row level security protects the data
  supabaseAnonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFpZW91d25wZmZqcXV6aGNudm9xIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTUwNzY5MTksImV4cCI6MjExMDY1MjkxOX0.RyZD5JAMo0yd6553P0KOI-4YPj7tMkBJHpP6DiYEY3M',
  requireInvite: true     // sign-up asks for an invite code
};
