-- Vectiba landing — dealer/partner application storage
-- Run this in Supabase → SQL Editor. Safe for a public static site:
-- anon role can INSERT only; there is no SELECT policy, so the public key cannot read rows.
-- Read the data in the Supabase Table Editor / via the service_role key only.

create table if not exists public.leads (
  id         uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  name       text,
  company    text,
  country    text,
  role       text,          -- 'dealer' | 'partner'
  email      text,
  phone      text,
  message    text,
  lang       text,          -- UI language used
  source     text default 'landing'
);

alter table public.leads enable row level security;

create policy "anon can insert leads"
  on public.leads for insert
  to anon
  with check (true);
