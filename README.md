# 🤖 AI 개발팀 - LangGraph 멀티 에이전트 시스템

> **조회수 높은 웹사이트를 자동으로 기획하고 개발하는 AI 팀**

[![GitHub Actions](https://img.shields.io/badge/Deploy-GitHub%20Pages-blue?logo=github)](https://github.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.0-green)](https://github.com/langchain-ai/langgraph)
[![Groq](https://img.shields.io/badge/Groq-Free-orange)](https://groq.com)

**🌐 [팀 포트폴리오 보기](./team_portfolio.html)** | **📖 [배포 가이드](./DEPLOY.md)** | **📚 [팀 소개](./TEAM_README.md)**

---

## 👥 우리 팀을 소개합니다

### **Alex** - Product Manager
- **AI 파트너**: Llama 3.3 70B
- **전문 분야**: 전략 기획, 요구사항 분석, 시장 조사
- **역할**: 팀의 비전을 설정하고 프로젝트를 이끄는 전략가

### **Maya** - UI/UX Designer
- **AI 파트너**: Llama 3.3 70B
- **전문 분야**: UI 디자인, 사용자 경험, 프로토타이핑
- **역할**: 아름답고 직관적인 인터페이스를 설계

### **Chris** - Frontend Developer
- **AI 파트너**: Llama 3.3 70B
- **전문 분야**: React, TypeScript, HTML/CSS, Next.js
- **역할**: 사용자가 보는 모든 것을 완벽하게 구현

### **Jordan** - Backend Developer
- **AI 파트너**: Mixtral 8x7b
- **전문 분야**: Python, FastAPI, PostgreSQL, Docker
- **역할**: 탄탄한 서버 로직과 API 구축

### **Sam** - Market Researcher
- **AI 파트너**: DuckDuckGo + Llama 3.3
- **전문 분야**: 시장 조사, 트렌드 분석, 경쟁 분석
- **역할**: 실시간 시장 데이터로 인사이트 제공

---

## 🎯 우리가 하는 일

### 1️⃣ 웹사이트 기획 시스템

5개의 전문 에이전트가 협업하여 웹사이트 아이디어를 기획합니다:

1. **시장조사 에이전트** - 트렌드 분석, 인기 키워드 조사
2. **경쟁분석 에이전트** - 유사 사이트 분석, 차별화 포인트
3. **기획 에이전트** - 아이디어 생성, 기능 명세
4. **평가 에이전트** - 바이럴 가능성, 구현 난이도, SEO 평가
5. **PM 에이전트** - 최종 기획서 작성, 우선순위 정리

### 2️⃣ 팀 포트폴리오 자동 생성

AI 개발팀이 스스로 소개 페이지를 만듭니다:
- PM이 팀 구성 및 프로젝트 아이디어 기획
- Designer가 페이지 디자인 수립
- Frontend가 완전한 HTML/CSS/JS 코드 작성

**👉 [생성된 팀 포트폴리오 보기](./team_portfolio.html)**

## 🛠️ 설치 방법

### 1. Groq API 키 발급 (무료!)

1. https://console.groq.com 접속
2. 가입/로그인
3. API Keys 메뉴에서 새 키 생성
4. 복사한 키를 `.env` 파일에 입력

```bash
# .env 파일 수정
GROQ_API_KEY=여기에_발급받은_키_입력
```

### 2. 가상환경 활성화

```bash
source venv/bin/activate
```

## 🚀 실행 방법

### 웹사이트 기획 시스템

```bash
# 완전한 기획서 생성
python main.py

# 빠른 테스트
python test_simple.py
```

### 팀 포트폴리오 생성

```bash
# 데모 페이지 생성 (API 불필요)
python demo_team_page.py

# AI 에이전트로 생성 (API 필요)
python create_team_page.py
```

### GitHub Pages 배포

```bash
# Git 초기화 및 배포
git init
git add .
git commit -m "🚀 Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

**상세 배포 가이드**: [DEPLOY.md](./DEPLOY.md)

## 💡 사용 예제

`main.py`의 마지막 부분을 수정하여 원하는 웹사이트를 기획할 수 있습니다:

```python
user_input = """
당신이 만들고 싶은 웹사이트 설명
"""

constraints = """
- 개발 기간: X개월
- 예산: XX만원
- 기타 제약조건
"""
```

## 📋 워크플로우

```
입력 (관심사/제약조건)
  ↓
시장조사 (트렌드 분석)
  ↓
경쟁분석 (차별화 포인트)
  ↓
아이디어 생성 (기획)
  ↓
평가 (바이럴 가능성, SEO 등)
  ↓
개선 반복 (필요시)
  ↓
최종 기획서 출력
```

## 🔧 LLM 제공자 변경

`.env` 파일에서 변경 가능:

- `LLM_PROVIDER=groq` (기본, 무료)
- `LLM_PROVIDER=openai` (GPT-4o-mini)
- `LLM_PROVIDER=anthropic` (Claude 3.5)

## 📁 프로젝트 구조

```
langGraph/
├── .env                          # API 키 설정
├── .gitignore                    # Git 제외 파일
├── .github/
│   └── workflows/
│       └── deploy.yml            # GitHub Actions 배포
│
├── 📋 기획 시스템
│   ├── main.py                   # 웹사이트 기획 메인
│   ├── state.py                  # 공유 상태 정의
│   ├── test_simple.py            # 빠른 테스트
│   └── agents/                   # 기획 에이전트
│       ├── market_research.py
│       ├── competitive_analysis.py
│       ├── idea_generator.py
│       ├── evaluator.py
│       └── pm.py
│
├── 👥 개발팀 시스템
│   ├── demo_team_page.py         # 데모 페이지 생성
│   ├── create_team_page.py       # AI 자동 생성
│   ├── dev_team_state.py         # 팀 상태 정의
│   └── dev_agents/               # 개발 에이전트
│       ├── pm_agent.py
│       ├── designer_agent.py
│       └── frontend_agent.py
│
├── 🌐 결과물
│   └── team_portfolio.html       # 생성된 팀 페이지
│
└── 📚 문서
    ├── README.md                 # 프로젝트 설명
    ├── DEPLOY.md                 # 배포 가이드
    ├── SETUP.md                  # 설치 가이드
    └── TEAM_README.md            # 팀 상세 소개
```

## ✨ 핵심 특징

### 🤖 멀티 에이전트 협업
- 각 팀원이 서로 다른 AI 모델 사용
- 전문 분야별 최적화된 파트너 배정
- LangGraph로 워크플로우 자동 관리

### 💰 완전 무료
- Groq API 무료 티어 사용
- DuckDuckGo 무료 검색
- GitHub Pages 무료 호스팅
- GitHub Actions 무료 배포

### ⚡ 빠른 개발
- 2-4주 내 MVP 완성
- 자동 기획서 생성
- 원클릭 배포

### 🎨 실제 결과물
- 완전한 HTML/CSS/JS 코드
- 반응형 디자인
- 프로덕션 레디

## 🚀 우리가 만든 것

### ✅ AI 웹사이트 기획 도구
조회수 높은 웹사이트를 자동으로 기획

### ✅ 팀 포트폴리오 생성기
AI 개발팀이 스스로 소개 페이지를 제작

## 🔍 지금 무엇을 만들고 있나요?

- **핵심 결과물**: `AI 팀 포트폴리오 퍼블리셔` — 5개 에이전트가 `team_portfolio.html`을 바로 만들어 줍니다.
- **보조 결과물**: `AI 웹사이트 기획서 메이커` — 시장조사→경쟁분석→기획→PM 단계를 거쳐 `final_plan.md`를 바로 생성합니다.
- **Launch Snapshot**: `final_spark_labs.py` 실행으로 소개 페이지(`index.html`)를 재생성해 최신 정보를 즉시 반영합니다.

## 🛠️ 지금 바로 실행하기

1. **AI 팀 포트폴리오 퍼블리셔**
   ```bash
   python3 create_team_page.py
   open team_portfolio.html
   ```
2. **AI 웹사이트 기획서 메이커**
   ```bash
   python3 main.py
   open final_plan.md
   ```
3. **Launch Snapshot (소개 페이지 재생성)**
   ```bash
   python3 final_spark_labs.py
   open index.html
   ```

## 🗂️ CrewAI 오더 콘솔

- 여러 에이전트에게 직접 명령을 내리고 응답을 따로 받고 싶다면 `crew_console.py`를 사용하세요.
- 필요한 패키지 설치: `pip install crewai langchain_groq`
- Groq API 키는 `.env` 또는 환경 변수 `GROQ_API_KEY`에 설정합니다.
- 한 번에 실행 예시:
  ```bash
  python3 crew_console.py --agent pm --order "Landing page 요구사항을 문장으로 정리해줘"
  ```
- 메뉴 기반 인터랙티브 모드:
  ```bash
  python3 crew_console.py
  ```
  이후 `pm`, `designer`, `frontend`, `backend`, `growth` 중 하나를 선택하고 오더를 입력하면 해당 에이전트의 응답을 즉시 확인할 수 있습니다.

## 📝 보고 & 승인 루프

- `crew_console.py`로 실행한 모든 오더는 `reports/log.jsonl`에 `pending` 상태로 기록됩니다.
- `report_manager.py`를 사용해 언제든 보고를 확인하고 승인/수정 요청을 남길 수 있습니다.

### 보고 목록 확인
```bash
python3 report_manager.py list --status pending
```

### 승인 또는 수정 요청 남기기
```bash
python3 report_manager.py respond --id <보고ID> --status approved --feedback "좋습니다"
# 또는
python3 report_manager.py respond --id <보고ID> --status needs_changes --feedback "CTA 색상 수정"
```

- 이렇게 하면 팀이 자동으로 보고를 올리고, 사용자는 `approved / needs_changes` 같은 응답을 남겨 워크플로우를 이어갈 수 있습니다.

### 회의용 요약 생성
- 여러 보고를 묶어서 회의 기록을 만들고 싶다면 `meeting_manager.py`를 사용하세요.
```bash
python3 meeting_manager.py --title "Daily Sync" --notes "CTA 색상 확정" --status pending
```
- `meetings/meeting-*.md` 파일이 생성되며, 선정된 보고 내용을 한눈에 공유할 수 있습니다.

### 👥 누가 뭘 기여했나요?
- **Alex (PM)**: 요구사항 브리핑, Build Plan 설계, README 실행 요약
- **Maya (Design)**: 레이아웃/컬러 토큰, Hero·섹션 배치 가이드
- **Chris (Frontend)**: HTML/CSS 구조, 애니메이션·반응형 폴리싱
- **라Codex (Execution)**: 실제 파일 편집·테스트, Git 커밋/배포
- **Claude (Lead Dev)**: LangGraph 워크플로우 총괄, 최종 페이지 생성 스크립트 관리
- **Sam (Growth)**: 카피·CTA 검수, Build Report 공유 시나리오

## 📚 더 알아보기

- **[TEAM_README.md](TEAM_README.md)** - 팀 상세 소개 및 활용법
- **[DEPLOY.md](DEPLOY.md)** - GitHub Pages 배포 가이드
- **[SETUP.md](SETUP.md)** - 설치 및 문제 해결
- **[LangGraph 공식 문서](https://langchain-ai.github.io/langgraph/)**
- **[Groq 문서](https://console.groq.com/docs)**

---

## 🤝 기여하기

이 프로젝트는 LangGraph 멀티 에이전트 시스템의 예제입니다.
- Issues: 버그 리포트 및 기능 제안
- Pull Requests: 환영합니다!

## 📄 라이센스

MIT License - 자유롭게 사용하세요!

---

<div align="center">

**Made with ❤️ by AI Dev Team**

🤖 **Powered by** LangGraph × Groq × Claude × 라Codex × GitHub Actions

</div>
