import json, glob, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
en = {
"nav_about":"Vectiba?","nav_why":"Why","nav_seller":"Service (sellers)","nav_buyer":"Service (buyers/partners)","nav_team":"Team","nav_contact":"Contact","nav_service":"Service",
"hero_kicker":"Dubai · Buy and sell cars across borders",
"hero_h1":"Sell your car to the dealer who pays the most — even if they're in another country.",
"hero_lead":"List your car once. Dealers in different countries bid on it. You see the real price after shipping and customs, then pick the best offer. We handle the inspection, the paperwork and the shipping.",
"hero_cta1":"See how it works","hero_cta2":"Contact us",
"art_h3":"One car, dealers everywhere","art_p":"List it once — buyers in many countries can bid.",
"art_s1":"You list your car on your phone","art_s2":"We check it and add the cost to each country","art_s3":"Dealers abroad bid on it","art_s4":"We ship it and handle customs",
"why_tag":"Why Vectiba?","why_h2":"Am I selling my car for too little?",
"why_story":"Every few years, when it's time to sell, there's always that nagging doubt. The same car is valued differently in every country, and the real selling price differs too. Somewhere there is always a dealer who would value your car higher. Even if that dealer is abroad, all you need is to reach them — remotely. Until now, language, distance, customs and paperwork simply kept you from ever meeting. Vectiba connects the two of you directly, with AI.",
"seller_tag":"Service · For sellers","seller_h2":"We show your car to dealers in many countries at once.",
"seller_sub":"The same car is valued differently in each country, and the real price differs too. Vectiba lets you sell to the dealer who values your car the most — even if that dealer is in another country, entirely remotely.",
"seller_how":"The Vectiba AI agent packages your car so dealers abroad can trust it and bid high, then opens it as an auction. You only need one dealer who really wants your car — you just pick the highest price, within 48 to 72 hours.",
"buyer_tag":"Service · For buyers & partners","buyer_h2":"Reach every used car in the world.",
"buyer_sub":"Still sending staff out to inspect cars? Still buying only through people you happen to know? Have language, distance, customs and paperwork been holding you back?",
"buyer_c1h":"Reach cars worldwide","buyer_c1p":"Access used cars anywhere in the world and deal directly with the owner, remotely — no agencies, no introductions in between.",
"buyer_c2h":"AI inspection checklist","buyer_c2p":"Ask Vectiba AI to check exactly what matters before you buy to resell. You're the pro — the AI backs your judgment.",
"buyer_c3h":"Logistics handled","buyer_c3p":"Language, distance, duties, customs and sea freight — all solved. Vectiba was built by a dealer who sold more cars than anyone.",
"buyer_note":"Shorten the chain, and sellers earn more while buyers land a more reasonable end cost. Buy in the most efficient, structured way of the AI era — and see your revenue and net profit grow several times over.",
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
"team_p1":"I've spent eight years in the car business. I started as a new-car salesman, became a used-car dealer, and then a dealer who put in his own capital to buy and sell cars directly. As CEO, I ran a used-car dealership and an export company. Over those years I traded and exported more than 1,000 cars a year to around 15 countries.",
"team_p2":"From September 2025 I spent six full months on market research alone, and I tore up the product several times because I hadn't found the essence of it. I held on through many setbacks and failures. Now I've found the service the market truly needs, and I'm about to launch it — and I'll keep building it into something everyone needs.",
"team_p3":"I've traveled to more than ten countries in person, meeting partners through cold emails, cold approaches, and introductions from my existing network. To find the partners who share this vision, I'm on the ground on the other side of the world.",
"team_p4":"I was once a dealer who couldn't sell even two cars a month. Using a platform like this, I became a dealer selling over 1,000 cars a year. That experience is where Vectiba began. Together with trusted partners and dealers in each country, we build the dream — and along the way, sellers get a higher price for the car they already own.",
"info_tag":"Contact","info_h2":"Let's talk.","info_sub":"Reach the founder directly.",
"info_loc":"Mina Jebel Ali, Jebel Ali Freezone, Dubai, UAE · Tech team in Seoul","info_cta":"Request materials",
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
tpl = open(os.path.join(ROOT,"_src","tpl.html")).read()
out = tpl.replace("__I18N_JSON__", json.dumps(I18N, ensure_ascii=False))
open(os.path.join(ROOT,"index.html"), "w").write(out)
json.dump(en, open(os.path.join(ROOT,"_src","en.json"), "w"), ensure_ascii=False, indent=0)
print("built:", len(out), "bytes | keys:", len(en), "| langs:", sorted(I18N))
