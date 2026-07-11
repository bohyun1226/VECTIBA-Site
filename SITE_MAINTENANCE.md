# vectiba.com — 유지보수 가이드 (다른 세션도 이걸 읽고 관리)

vectiba.com 랜딩 사이트. **정적 HTML 한 파일**을 16개 언어로 빌드해서 GitHub Pages로 서빙한다.

## 구조
```
index.html          ← 배포되는 완성본 (빌드 산출물, 직접 수정 금지)
CNAME               ← vectiba.com
img/                ← vectiba-logo.png(실제 로고, 투명), dustin.jpg(창업자 사진)
demo/               ← 임베드된 셀러 데모앱 (자동재생, demo/index.html + demo/img)
i18n/<lang>.json    ← 언어별 문구 (ar de en... 15개 파일, 각 ~52키). en은 빌드 스크립트 안에 있음
_src/tpl.html       ← HTML 템플릿 (구조·CSS·__I18N_JSON__ 자리)
_src/build.py       ← 빌드 스크립트 (en 원본 dict 포함). tpl + i18n → index.html
_src/en.json        ← 영어 원본 참고본 (빌드시 자동 생성)
```

## 배포 (GitHub Pages)
- 레포: **PUBLIC** `bohyun1226/VECTIBA-Site`, 브랜치 `main`, 루트. (사업 레포 vectiba는 private → Pages 막혀서 이 사이트만 별도 공개 레포)
- Pages 이미 켜져 있음(Settings→Pages, main/root, custom domain vectiba.com, HTTPS on). DNS도 완료.
- push 하면 ~1분 뒤 자동 반영.

## 이 맥에서 클론/푸시 (포트22 자주 막힘 → 443 사용)
```
git clone ssh://git@ssh.github.com:443/bohyun1226/VECTIBA-Site.git
# 또는 기존 클론에서:
git remote set-url origin ssh://git@ssh.github.com:443/bohyun1226/VECTIBA-Site.git
```

## 문구 수정하는 법
1. **영어 수정:** `_src/build.py` 안의 `en = { ... }` dict 편집.
2. **다른 언어 수정:** `i18n/<lang>.json` 편집 (키는 en과 동일해야 함).
3. **빌드:** `python3 _src/build.py` → `index.html` 재생성.
4. **배포:** `git add -A && git commit -m "..." && git push origin main`
> 규칙: 방어적 부정문 금지, 쉬운 말(정본 문서작성원칙). 브랜드 톤 크림#F8F5EE·딥그린#135A4B·골드#BE8B39·Poppins.

## 언어 추가하는 법
1. `_src/tpl.html`의 `<select id="langsel">`에 `<option value="xx">자국어이름</option>` 추가 (라벨은 그 나라 말로, 줄임말 X).
2. RTL 언어면 build 스크립트가 만든 index의 `RTL=['ar','fa']`에 추가 (tpl.html 스크립트).
3. `i18n/xx.json` 생성 (en의 모든 키 번역, `<strong>`·인라인 style 보존).
4. build → push.

## 섹션 순서 (현재)
Hero → 왜 시작했나(문제 통합) → 서비스(+데모) → 구성원(창업자) → 문의(WhatsApp·LinkedIn·이메일). 
menu = why / service / team / contact.

## 로고
`img/vectiba-logo.png` = 명함에서 누끼딴 실제 V(투명). 다시 만들려면 명함 `~/Documents/VECTIBA/09_ 디자인, 샘플/명함 파일.png`에서 초록만 키잉(Pillow). nav+hero가 이 이미지 사용.

## 주의
- 16개 언어 중 **최근 문구 변경은 EN·KO만 반영**된 상태일 수 있음. 나머지 14개는 문구 최종 확정 후 일괄 재번역 필요 (번역은 서브에이전트 병렬로 i18n/*.json 생성).
- 남의 차 사이트/이미지 크롤링 금지(저작권·ToS). 사진은 라이선스 소스(Wikimedia CC 등)나 자체 자산만.
