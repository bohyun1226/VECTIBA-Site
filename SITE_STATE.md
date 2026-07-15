# vectiba.com → 도메인 이전 완료, 🟡 지금 남은 건 inc.vectiba.com SSL 발급 대기 (2026-07-15 밤 재확인, 0번 먼저 읽을 것)

다음 세션은 **이 문서 하나만 읽고** 이어서 작업. 소스는 이 폴더(`~/vectiba-dev/VECTIBA-Site`, 영구). 클론: `gh repo clone bohyun1226/VECTIBA-Site`.
⚠️ 작업 전 항상 `git fetch && git log --oneline -5` — **다른 세션이 이 레포에 동시 커밋**함(맨 아래 참고).

## 0. 상태 재확인 (2026-07-15 밤, `dig`/`curl`로 직접 확인) — 예전 404 장애는 해소됨
대표님이 Namecheap에서 A레코드를 이미 바꿔주셔서, 아래 4개 항목은 전부 해결됨:
- `vectiba.com`/`www.vectiba.com`/`buy.vectiba.com` DNS → 전부 `76.76.21.21`(Vercel)로 확인됨. 더 이상 404 아님.
- `vectiba.com`/`www.vectiba.com` 루트 접속 시 200 아니고 **307로 `/sell`(vectiba-app 셀러 앱)로 리다이렉트** — 이게 최종 확정된 정상 동작(1-1 참고).
- `buy.vectiba.com/dealer`, `partner.vectiba.com/partner` 둘 다 실제로 열어서 200/307 + 정상 화면(로고까지) 확인됨. Vercel 프로젝트에도 두 도메인 다 `verified:true`로 등록돼 있음. **더 이상 "DNS 대기" 아님 — 완료된 상태.**

**🟡 지금 유일하게 남은 문제**: `inc.vectiba.com`의 DNS(CNAME→`bohyun1226.github.io`, 4개 A레코드)는 맞게 설정돼 있는데, GitHub Pages가 이 커스텀 도메인용 HTTPS 인증서를 아직 발급 안 끝냄 — `curl -v`로 확인하면 `inc.vectiba.com`인데 인증서 주체가 `CN=*.github.io`(범용 인증서)로 나옴, 즉 아직 자기 도메인 인증서가 아님. 그래서 지금 `https://inc.vectiba.com`은 브라우저에서 안 열림.
- 결과적으로 지금 이 순간, **회사소개(마케팅) 페이지가 뜨는 커스텀 도메인이 하나도 없음** — `vectiba.com` 루트는 이미 셀러 앱으로 넘어갔고, `inc.vectiba.com`은 인증서 대기 중이라서.
- 조치: `gh api -X PUT repos/bohyun1226/VECTIBA-Site/pages -f cname="inc.vectiba.com"`로 도메인 재검증을 한 번 걸어둠(2026-07-15 밤) — 깃허브가 자동으로 처리하는 부분이라 보통 몇 분~몇 시간 걸림, 강제로 즉시 끝낼 방법은 없음. 다음 세션은 `curl -v https://inc.vectiba.com/ 2>&1 | grep subject:`로 재확인 — `CN=inc.vectiba.com` 또는 Let's Encrypt로 바뀌어 있으면 완료.
- 그래도 계속 `*.github.io`로 나오면: GitHub 저장소 Settings → Pages에서 커스텀 도메인 필드를 한 번 비웠다가 다시 `inc.vectiba.com` 입력(수동 재트리거), 그래도 안 되면 대표님께 DNS가 실제로 맞는지 재확인 요청.

## 1. 배포
- GitHub Pages, PUBLIC repo `bohyun1226/VECTIBA-Site`, branch `main` root, HTTPS.
- **도메인 이전 진행중(2026-07-14)**: `CNAME` 파일을 `vectiba.com` → **`inc.vectiba.com`**으로 변경함(회사소개 페이지라 inc=Incorporated). 이유·전체 그림은 아래 1-1 참고. 코드/빌드는 전혀 안 바뀜, 도메인만 이동.
  - ✅ 완료: 이 레포 `CNAME` 파일 변경(커밋됨), `inc` DNS 등록(CNAME→bohyun1226.github.io, `dig`로 확인됨).
  - 🟡 진행중: `inc.vectiba.com` SSL 인증서 GitHub Pages가 자동 발급 대기중 — 위 0번 참고(재검증 다시 걸어둠, 재확인 필요).
  - ✅ 완료(2026-07-15 밤): 루트/www DNS는 대표님이 이미 Vercel로 전환함 — 더 이상 404 아님, `vectiba.com`이 이미 셀러 앱으로 넘어가 있음(순서상 inc가 아직 준비 안 된 채로 먼저 넘어간 상태지만, 지금은 그냥 이대로 최종 상태로 봐도 됨 — 위 0번 참고).
- 빌드: `python3 _src/build.py` → `_src/tpl.html`(HTML) + build.py 안 EN 사전 + `i18n/<lang>.json` 합쳐 `index.html` + `version.txt` 생성 → `git commit` → `git push` (약 1분 반영).
- **자동갱신**: 빌드마다 `version.txt`에 타임스탬프. 페이지가 로드되면 `version.txt`를 no-store로 받아 내 BUILD와 다르면 `?b=<버전>`으로 새로고침 → **대표님 기기도 배포하면 자동으로 최신**(한 번만 수동 새로고침해서 이 스크립트를 받으면 그 뒤로 자동). 캐시 얘기 대표님께 금지.
- 브랜드: 크림 #F8F5EE · 딥그린 #135A4B · 골드 #BE8B39 · 에메랄드 #0B7A5A(딜러 데모) · Poppins · 실제 V로고.
- **로고 확정(2026-07-14)**: `brand/logo/`에 정식 에셋 세트 저장(심볼/가로/세로 lockup × 컬러/화이트 × PNG/SVG, 총 12개). 대표님이 이걸로 고정하기로 결정 — 교체 금지. 브랜드시트 컬러 팔레트(에메랄드 `#12564B` 등)는 `brand/README.md` 참고 — 현재 사이트 색상과 약간 다름, **사이트 전체 컬러 교체는 아직 미확정**(별도 지시 필요).
- **기본 언어 = 영어**. 처음 방문자는 무조건 영어(navigator 자동감지 제거). 언어 바꾸면 localStorage에 저장돼 다음에 그 언어. (`detectLang()` = saved 있으면 그것, 없으면 'en'.)

## 1-1. ⚠️ 전체 도메인 지도 (2026-07-15 최종 확정 — buy/inc/partner 체계, CLAUDE.md에 전체지도 있음)
**이유**: 셀러는 일반 고객이라 검색해서 그냥 들어와야 하니 주소 앞에 아무것도 안 붙임(루트 그대로 씀). 바이어·파트너는 정해진 링크로만 들어오는 사업 파트너라 서브도메인으로 구분. → 별도 `sell.vectiba.com`은 안 씀, 루트가 그 역할.
- **`vectiba.com`(루트)** → **셀러 앱 최종 주소**(서브도메인 안 붙음). DNS 이미 전환 완료(2026-07-15 밤) — 이 레포(마케팅 페이지)는 더 이상 루트에 없음, `inc.vectiba.com`으로 완전히 이전됨. (상태는 0번 참고)
- **`inc.vectiba.com`** → 지금 이 레포(회사소개 페이지)의 정식 위치. DNS는 맞게 설정됨, SSL 인증서만 대기 중(0번 참고).
- **`buy.vectiba.com`** → **바이어 전용 페이지·대시보드**, `vectiba-app` 레포. ✅ 완료(2026-07-15 밤) — DNS·Vercel 도메인 등록·`proxy.ts` 라우팅 전부 확인됨, 실제로 열림.
- **`partner.vectiba.com`** → 운송·통관 등 파트너사(포워더) 전용, `vectiba-app` 레포. ✅ 완료 — DNS·Vercel 등록·실제 접속까지 확인됨(2026-07-15 밤).
- 실제 제품(셀러 AI 인테이크·매물 게시·경매·딜러 대시보드·포워더 대시보드) 코드/DB는 전부 **별도 레포 `vectiba-app`**, Supabase 프로젝트 "Vectiba-app"의 `vectiba-app`쪽 `supabase/migrations/`가 진짜 스키마(`listings`/`listing_media`/`bids`/`auctions` 등).
- **여기(이 레포)에는 매물/경매/딜러승인 같은 실제 제품 데이터·기능을 만들지 말 것.** 문의 폼(`leads` 테이블, 아래 4번)처럼 "관심 등록" 수준 라이트 캡처만.
- 실수 기록: 2026-07-14, 독일 딜러가 매물 올리고 싶어해서 이 레포에 `supabase/car_listings.sql`(매물 상세 테이블)을 만들었다가, `vectiba-app`에 이미 훨씬 완성된 매물 스키마+셀러 AI 인테이크 플로우가 코드 완료 상태인 걸 뒤늦게 확인 → 삭제하고 되돌림. **다음에 "딜러가 차 올리고 싶어함" 같은 요청 오면 → vectiba-app 세션으로 보낼 것, 여기서 새 테이블 만들지 말 것.**

## 2. 페이지 구조 (확정)
메뉴 5개: **벡티바? · 셀러 · 바이어 · 팀 · 문의** (모바일은 햄버거 드롭다운).
1. **벡티바?**(히어로, 크림) — 한 줄 카피(대표님 확정):
   - 제목: **"만날 수 없던 사람들을, AI 기술로 이어줍니다."** (`hero_h1`)
   - 부제: **"신뢰 있는 자동차 거래를 만들어 갑니다."** (`hero_def`, 회색 lead)
   - 작은 태그: "전 세계 국경을 넘어 차를 사고팝니다" (`hero_kicker`)
   - 오른쪽 박스: **3축** — 🚗 셀러 더 높은 가격 · 🤝 딜러 합리적 매입·마진 · 🚢 운송사 거래↑·매출↑ ("모두가 이기는 구조", `art_h3/art_s1~3`).
   - (이전의 긴 3축 문장 `hero_lead`는 히어로에서 제거함 — 키는 남아있지만 화면엔 안 씀.)
2. **셀러**(흰색, id=`seller`) — **왼쪽 글 / 오른쪽 폰 데모** 나란히(한 화면). 대표님 셀러 원문(내 차 너무 싸게? / 나라별 가격 다름 / 가장 높게 쳐주는 딜러에게 비대면) + `seller_how`. 아래 문제 3카드 + `why_now`.
3. **바이어**(크림, id=`dealer`) — 라벨 **"바이어 / For buyers"**(`nav_buyer`,`buyer_tag`). **글·카드 위 → PC 딜러 데모 아래 full-width(최대 1280px, `.dealerfull`)**. 대표님 바이어 원문(아직 직원 검수? / 전 세계 매물 / AI검수 / 물류 / 순이익) + 밀봉견적 설명.
4. **팀**(딥그린 배너) — 대표님 1인칭 스토리(8년·15개국·연1,000대·월2대→연1,000대) + 사진 `img/dustin.jpg`.
5. **문의**(흰색) — WhatsApp·LinkedIn·이메일 + **바이어·파트너 신청**(팝업 모달, GitHub 로그인 스타일) + 주소(두바이 Jebel Ali / 서울 Seocho, 둘 다 영어표기).

## 3. 데모
- `demo/` 셀러 폰: AI 대화 인테이크(음성·사진), **16개 언어**. 낙찰=두바이/UAE, 나라이름 다국어. 따뜻한 크림 #F4ECDA. (고정 폰 프레임 — 의도된 고정 높이.)
- `dealer/` 바이어 PC: 에어비앤비식 카드그리드(사이드메뉴X), **밀봉경매**(건수만·낙찰가 표시X), BMW G30 상세(사진 작게+라이트박스), **AI 도착가 계산기**(부가비용 합계 접기/펼치기 + 로드탁송 캐리어/기사 + 화폐선택 + **당일환율** open.er-api.com), [입찰하기]. 에메랄드 헤더 + 화이트/샌드. iframe 높이 자동맞춤(`syncFrameH`, `document.body.scrollHeight`). **16개 언어 전체 지원 완료**(2026-07-14) — `T[lang]` 구조로 ko/en 이분법에서 확장, 나라·도시·연료·상태뱃지는 `COUNTRY`/`DCTRY`/`BADGE`/`FUEL` 공용 lookup(코드 기반, 번역명 문자열 키 아님)이라 언어 추가가 쉬움. 차량 모델명은 한국어(`nameKo`)만 별도 표기, 나머지 15개 언어는 라틴 표기 그대로(국제 표준 관행). RTL(ar/fa) 자동 적용.
- 두 데모 모두 사이트 언어 따라 첫 화면부터 그 언어로 로드(하드코딩 en 제거, applyLang이 src 지정).
- 차 사진: `dealer/img/` 14대 정면 Wikimedia CC(도요타·벤츠·BMW·G클래스·랜드크루저+프랑스 푸조/르노), 출처 `dealer/img/ATTRIBUTIONS.txt`. **크롤링·캡처·브랜드 프레스사진 금지**(운영 땐 셀러가 실사진 올림).

## 4. 가입신청 폼 → Supabase ✅ 연결 완료
- 폼=문의 섹션 팝업. **Supabase `leads` 테이블에 실제 저장됨**(테스트 201 확인).
- `_src/tpl.html`의 `LEAD_CFG` 채워짐: url=`https://kxjruqbqjryfjodkkace.supabase.co`, key=`sb_publishable_...`(Publishable=브라우저 안전, 공개 OK). ⚠️ service_role(sb_secret_)은 절대 넣지 말 것.
- 테이블: `supabase/leads.sql` (컬럼 name/company/country/role/email/phone/message/lang/source, **insert-only RLS**). Supabase 프로젝트="Vectiba-app".
- **대표님이 신청자 보는 법**: Supabase → Table Editor → `leads`. (setup-test 행 1개 있음, 삭제 가능.)
- 실패 시 폴백: Supabase 오류→FormSubmit(ceo@vectiba.com 이메일)→mailto. (정상 경로는 Supabase.)

## 5. 남은 일 (다음 세션)
1. ~~13개 언어 재번역~~ ✅ 완료(2026-07-14). EN 소스 기준으로 각 `i18n/<lang>.json` 키 단위 diff → 14개 언어 병렬 서브에이전트로 드리프트 수정(`hero_h1`/`hero_def`/`hero_kicker`, `nav_buyer`/`buyer_tag`, 셀러·바이어 섹션, 폼, 푸터, `svc_dealer_sub` 등). `_src/build.py`로 재빌드·검증 완료.
2. ~~딜러 데모 16개 언어 확장~~ ✅ 완료(2026-07-14). ko/en 이분법 → `T[lang]` 16개 언어 구조로 리팩터, 14개 언어 병렬 서브에이전트로 번역. "Germany from" 어순 버그도 같이 고침(`departfmt` 템플릿 도입).
3. 추가 레이아웃/문구 요청 반영.
4. (참고) 위 두 작업 다 여러 서브에이전트가 **같은 파일을 동시에 수정**하는 방식으로 진행됨 — 매 커밋 전 구조 검증(JSON parse, 키 개수, JS syntax) 통과 확인 후 커밋함. 이후 세션에서 같은 파일 다시 손댈 때도 동일하게 검증 권장.
5. **다음 세션 할 일**: `inc.vectiba.com` SSL 인증서 발급 완료됐는지 `curl -v`로 재확인(0번 참고). 완료됐으면 이 파일 0번 항목도 "완료"로 정리.

## 6. 모바일 (수정 완료)
- 딜러 데모 `<style>` 미닫힘으로 첫 접속 깨지던 치명 버그 수정.
- 940px 이하 햄버거 메뉴(`#hamBtn`+`#mobileMenu`, RTL 대응).
- 딜러 데모 이중 스크롤(iframe 고정높이 vs 5,800px 콘텐츠) → `syncFrameH()`로 자동맞춤.
- 딜러 데모 카드 세로 정렬(모바일), 넘치던 상단 faux-nav 숨김.
- 셀러 폰 데모 좁은 화면 맞춤. 입찰가 음수 방지(min=0 + 클램프).

## 7. ⚠️ 동시 세션 주의
같은 작업 디렉토리에서 다른 Claude 세션이 동시에 커밋·푸시함(여러 차례 확인). 작업 전 `git fetch && git log --oneline -5`, `git status` 필수. 로컬 낯선 uncommitted 변경 지우지 말고 같이 커밋(대개 다른 세션 의도적 작업). 푸시 전 `git pull --rebase`.

## 8. 대표님 작업 규칙 (반드시)
- **대표님 원문 그대로**(가볍게만 다듬기), 내가 다시 쓰지 않음. 재검 안 받고 바로 배포.
- **짧게, 한 번에 한 가지**. 캐시 얘기 금지. 시킨 것만(추가 X). 부정문 금지. "형/반말" 금지 → "대표님"·존댓말.

## 9. 2026-07-15 밤 로그 (vectiba-app 세션이 로고 작업 하다가 겸사겸사 상태 재확인)
- 로고를 크림 원+그린 V 배지 하나로 통일하는 작업(주 담당은 `vectiba-app`) 하면서, 이 레포의 `img/vectiba-logo.png`도 같은 배지로 교체(커밋 `bbb5208`) — `dealer/index.html`의 `.logochip` 이중 원 문제도 같이 수정. `brand/logo/vectiba-badge.svg`/`.png` 정본 추가.
- 겸사겸사 도메인 상태를 `dig`/`curl`로 전부 재확인함 — 위 0/1/1-1번 최신화함. 요약: 예전에 걱정하던 루트 404는 이미 해결돼 있었음(대표님이 Namecheap A레코드 직접 반영), `buy.`/`partner.` 서브도메인도 이미 다 살아있었음. 지금 유일하게 남은 건 `inc.vectiba.com` SSL 인증서 발급 대기뿐 — 재검증 요청은 걸어둠, 시간이 걸리는 부분이라 강제로 끝낼 수는 없음.
