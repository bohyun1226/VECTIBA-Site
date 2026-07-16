import json, glob, os, time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
en = {
"nav_about":"Vectiba?","nav_why":"Why","nav_seller":"For sellers","nav_buyer":"For buyers","nav_team":"Team","nav_contact":"Contact","nav_service":"Service",
"hero_kicker":"Buy and sell cars across borders — worldwide",
"hero_def":"The same car sells for a different price in every country. We connect the people that language, borders and distance kept apart.",
"hero_h1":"We connect people who could never meet.",
"hero_accent":"AI TECHNOLOGY",
"out_tag":"What we built",
"out_h2":"Vectiba runs as three services.",
"out_sell_p":"A car owner lists from a phone, and dealers from many countries bid in an auction.",
"out_buy_p":"Dealers browse cars worldwide on a PC dashboard and place sealed bids at real landed cost.",
"out_partner_p":"Shipping and customs partners handle their assigned deals on their own dashboard.",
"out_visit":"Visit →",
"out_st1":"List from a phone","out_st2":"AI auction","out_st3":"Highest price",
"demo_h3":"Open a global auction — right from your phone.",
"demo_s1":"Talk to the app, add a few photos — AI packages your car so dealers can trust it.",
"demo_s2":"Dealers in many countries bid on it — sealed quotes, real landed cost.",
"demo_s3":"You just pick the highest price — within 48 to 72 hours.",
"out_bt2":"AI inspection",
"out_pt1":"More deals","out_pt2":"Direct requests","out_pt3":"More revenue",
"biz_tag":"Business",
"biz_h2":"How Vectiba expands.",
"biz_c1h":"Four revenue streams",
"biz_c1p":"Transaction fees, advertising, partner listing fees and subscriptions — revenue grows with every deal.",
"biz_c2h":"Local operators per country",
"biz_c2p":"As we expand, local operating companies take the reins and share the operating profit as incentives.",
"biz_c3h":"Expansion markets",
"biz_c3p":"Starting from used-car deals, the same rails extend to new cars, financing, insurance, lease and rental.",
"biz_note":"So far: pre-interviews with about 50 dealers across 6 countries, working in partnership with people from Hyundai Motor, SK, KGM and Kia.",
"hero_lead":"Sellers get more, dealers buy at a fair price and keep the margin, and forwarders see more deals and more revenue — a virtuous cycle.",
"hero_cta1":"See how it works","hero_cta2":"Contact us",
"art_h3":"A system that benefits everyone","art_p":"They need each other, but they could never connect.",
"art_s1":"Seller — a higher price","art_s2":"Dealer — fair purchase, real margin","art_s3":"Forwarder — more deals, more revenue","art_s4":"",
"why_tag":"For sellers","why_h2":"Am I selling my car for too little?",
"why_lead":"The same car is worth different amounts in different countries — and that difference should be yours.",
"why_story":"Every few years, when it's time to sell, you wonder whether the price is right. The same car is valued differently in every country, and the real selling price differs too — so somewhere there is always a dealer who would value your car higher. Until now, the seller and that dealer never met directly: distance, language, customs and paperwork stood in between. Vectiba connects the two directly, with AI — handling inspection, translation and the full landed-cost calculation, so a seller and dealers worldwide meet for the first time.",
"seller_tag":"Service · For sellers","seller_h2":"We show your car to dealers in many countries at once.",
"seller_sub":"The same car is valued differently in each country, and the real price differs too. Vectiba lets you sell to the dealer who values your car the most — even if that dealer is in another country, entirely remotely.",
"seller_how":"Vectiba's AI talks with the seller, organizes the car's details and analyzes the photos so dealers can trust it, then opens it as an auction. The seller just picks the highest price — within 48 to 72 hours.",
"buyer_tag":"For buyers","buyer_h2":"Reach every used car in the world.",
"buyer_sub":"Still sending staff out to inspect cars? Still buying only through people you happen to know? Have language, distance, customs and paperwork been holding you back?",
"buyer_login_cta":"Dealer login","partner_login_cta":"Partner / forwarder login",
"buyer_c1h":"Reach cars worldwide","buyer_c1p":"Access used cars anywhere in the world and deal directly with the owner, remotely — no agencies, no introductions in between.",
"buyer_c2h":"AI inspection checklist","buyer_c2p":"Ask Vectiba AI to check exactly what matters before you buy to resell. You're the pro — the AI backs your judgment.",
"buyer_c3h":"Logistics handled","buyer_c3p":"Language, distance, duties, customs and sea freight — all solved. Vectiba was built by a dealer who sold more cars than anyone.",
"buyer_note":"Shorten the chain, and sellers earn more while buyers land a more reasonable end cost. Buy in the most efficient, structured way of the AI era — and see your revenue and net profit grow several times over.",
"svc_tag":"Service","svc_h2":"A seller lists — dealers around the world send quotes.",
"svc_sub":"Watch both sides connect. A seller lists a car from their phone, and that same car opens to dealers in other countries who send quotes.",
"svc_seller_label":"① Seller's screen · lists from a phone",
"svc_connect":"↓ Here is how that same car looks to a dealer.",
"svc_dealer_label":"② Dealer's screen · sends a quote",
"svc_dealer_sub":"The dealer works out the landed cost in their own currency at today's rate and sends a sealed quote — no one sees anyone else's.",
"why_by":"Dustin Yoo · Founder & CEO",
"why_now":"Why now: AI can finally inspect a car remotely, translate across languages, and work out the full landed cost — so this works today.",
"prob_tag":"The problem","prob_h2":"The buyer who would pay the most usually never sees the car.",
"prob_sub":"A dealer in another country might pay far more than your local one. Today they can't find your car, so that extra money goes to middlemen.",
"prob_c1h":"Sellers settle for the local price","prob_c1p":"Most people take the first easy offer nearby, before a buyer in another country ever hears about the car.",
"prob_c2h":"The best buyer is far away","prob_c2p":"Distance, language and complicated paperwork keep the seller and the buyer who'd pay most from ever meeting.",
"prob_c3h":"Middlemen take the difference","prob_c3p":"Referrals and brokers move cars, but the seller and the buyer never connect directly — so the extra money goes to the middle.",
"sol_tag":"The service","sol_h2":"We open your car to dealers in many countries at once.",
"sol_sub":"Before anyone bids, we make the car easy to trust and easy to price. Then dealers compete, and the best real offer wins.",
"sol_c1h":"We check the car","sol_c1p":"Photos, mileage, history, and an inspection when it's needed — so a dealer far away can trust it without flying out to see it.",
"sol_c2h":"We show the full cost","sol_c2p":"Shipping, customs and fees to each country, added up — so everyone sees the real delivered price before they bid.",
"sol_c3h":"Dealers bid, you choose","sol_c3p":"Dealers in different countries make offers. You see how much you would actually get from each one, and you pick.",
"demo_sub":"The seller just talks to the app, adds a few photos, and the car opens to dealers abroad. It plays automatically above — sample data.",
"team_tag":"The team","team_h2":"The people who built it.","team_role":"Founder & CEO",
"team_p1":"Eight years in the car business — new-car salesman, used-car dealer, then CEO of a dealership and export company, trading more than 1,000 cars a year to around 15 countries.",
"team_p2":"Vectiba is one founder's hands-on work from end to end — the product built and coded himself, the business plan, field research across more than ten countries, user and dealer interviews, and partner companies contacted directly.",
"team_p4":"I was once a dealer who couldn't sell even two cars a month. Using a platform like this, I became a dealer selling over 1,000 cars a year. That experience is where Vectiba began.",
"info_tag":"Contact","info_h2":"Let's talk.","info_sub":"Partnership and investment inquiries both reach the founder directly.",
"info_loc":"Dubai — Jebel Ali Freezone, Dubai, UAE<br>Seoul — 248 Seocho-daero, Seocho-gu, Seoul, Republic of Korea","info_cta":"Request materials",
"form_h":"Dealer & partner application","form_sub":"Leave a few details and the founder will reach out personally.",
"form_name":"Name","form_company":"Company","form_country":"Country","form_role":"I am a…",
"form_role_dealer":"Dealer","form_role_partner":"Partner · forwarder",
"form_email":"Email","form_phone":"WhatsApp / phone","form_msg":"Message (optional)",
"form_submit":"Submit application","form_done":"Thanks — we've received it and will be in touch.",
"foot_1":"<strong style=\"color:var(--green)\">Vectiba</strong> · Buy and sell cars across borders · Dubai / Seoul",
"foot_2":"© 2026 Vectiba. Dustin Yoo, Founder & CEO · ceo@vectiba.com"
}
I18N = {"en": en}
for f in sorted(glob.glob(os.path.join(ROOT,"i18n","*.json"))):
    lang = os.path.splitext(os.path.basename(f))[0]
    d = json.load(open(f))
    if "foot_1" in d and "<strong>" in d["foot_1"]:
        d["foot_1"] = d["foot_1"].replace("<strong>", "<strong style=\"color:var(--green)\">")
    I18N[lang] = d
# 언어 목록·순서·RTL·저장키는 공용 정본에서 가져온다(손으로 박지 않음).
# 원본: ~/vectiba-dev/vectiba-i18n/languages.json — 여기 _src/languages.json 은 그 사본.
# 언어를 바꾸려면 정본을 고치고 이 사본으로 다시 복사(조율자가 점검, ~/VECTIBA/작업일지.md).
LANGS_RAW = json.load(open(os.path.join(ROOT,"_src","languages.json")))
LANGS = {k: v for k, v in LANGS_RAW.items() if not k.startswith("_")}  # 주석(_comment) 제외
# 언어 선택 UI(알약버튼+국기 그리드)는 tpl.html 이 LANGS 로 직접 그린다 — 여기선 목록만 주입.
# 정본 언어 ↔ 실제 번역 파일 어긋남 경고(핸드오프용)
cfg_codes = {l["code"] for l in LANGS["languages"]}
missing_tr = sorted(cfg_codes - set(I18N))      # 목록엔 있는데 번역 없음
missing_cfg = sorted(set(I18N) - cfg_codes)     # 번역은 있는데 목록에 없음
if missing_tr:  print("⚠️ 정본에 있으나 번역파일 없음:", missing_tr)
if missing_cfg: print("⚠️ 번역파일 있으나 정본 목록에 없음:", missing_cfg)

tpl = open(os.path.join(ROOT,"_src","tpl.html")).read()
BUILD = str(int(time.time()))
out = (tpl
    .replace("__I18N_JSON__", json.dumps(I18N, ensure_ascii=False))
    .replace("__LANGS_JSON__", json.dumps(LANGS, ensure_ascii=False))
    .replace("__BUILD__", BUILD))
open(os.path.join(ROOT,"index.html"), "w").write(out)
open(os.path.join(ROOT,"version.txt"), "w").write(BUILD)
json.dump(en, open(os.path.join(ROOT,"_src","en.json"), "w"), ensure_ascii=False, indent=0)
print("built:", len(out), "bytes | keys:", len(en), "| langs(정본순):", [l["code"] for l in LANGS["languages"]])
