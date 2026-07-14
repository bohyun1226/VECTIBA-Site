-- Vectiba landing — dealer car listing intake
-- Run this in Supabase → SQL Editor (same project as leads.sql, "Vectiba-app").
-- Same security model as leads: anon role can INSERT only, no SELECT policy,
-- so the public site key cannot read other dealers' listings. Read in the
-- Supabase Table Editor / via the service_role key only.

create table if not exists public.car_listings (
  id                 uuid primary key default gen_random_uuid(),
  created_at         timestamptz not null default now(),
  status             text default 'new',      -- 'new' | 'reviewed' | 'live' | 'rejected' (Dustin's own triage)

  -- dealer contact (self-contained; no join required to read a listing)
  dealer_name        text,
  dealer_company     text,
  dealer_country     text,
  dealer_email       text,
  dealer_phone       text,

  -- vehicle identity
  brand              text,
  model              text,
  trim               text,
  year               int,
  month              int,
  plate_no           text,                    -- 차량번호
  vin                text,                    -- 차대번호

  -- spec
  mileage_km         int,
  fuel               text,                    -- petrol | diesel | hybrid | electric
  transmission       text,                    -- auto | manual
  color_exterior     text,
  color_interior     text,
  sunroof            boolean,                 -- 썬루프 유무
  adas               boolean,                 -- 자율주행/운전자보조 유무

  -- condition
  accident_status    text,                    -- 'none' | 'minor' | 'frame' (완전무사고 | 단순교환있음 | 프레임사고있음)
  accident_minor_count int,                   -- 단순교환 건수 (accident_status='minor'일 때만)
  smoked             boolean,                 -- 흡연차량 유무
  paint_thickness    jsonb,                   -- 패널별 도막 측정값, 선택 입력 {"본넷":120,"트렁크":135,...}
  notes              text,                    -- 자유 메모 (평가사 코멘트 등)

  -- price
  price_asking       numeric,                 -- 희망 판매가
  price_new          numeric,                 -- 신차가 (참고, 선택)
  currency           text default 'EUR',

  -- media (uploaded to the car-listing-photos storage bucket, URLs stored here)
  photo_urls         text[],

  lang               text,                    -- UI language used
  source             text default 'landing'
);

alter table public.car_listings enable row level security;

create policy "anon can insert car listings"
  on public.car_listings for insert
  to anon
  with check (true);

-- Storage bucket for listing photos. Public-read so photos display on the
-- dealer auction card once a listing goes live; anon can upload (insert)
-- but not overwrite/delete others' files (enforced by using a random path
-- per upload from the client, e.g. `${listingId}/${uuid()}.jpg`).
insert into storage.buckets (id, name, public)
values ('car-listing-photos', 'car-listing-photos', true)
on conflict (id) do nothing;

create policy "anon can upload car listing photos"
  on storage.objects for insert
  to anon
  with check (bucket_id = 'car-listing-photos');

create policy "public can view car listing photos"
  on storage.objects for select
  to public
  using (bucket_id = 'car-listing-photos');
