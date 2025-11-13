# 🤖 AI 개발팀 자동 포트폴리오 생성기

## 📋 개요

**AI 개발팀이 스스로 자기소개 웹페이지를 만드는 시스템**

- **PM 에이전트**: 팀 구성, 비전, 프로젝트 아이디어 기획
- **Designer 에이전트**: 디자인 컨셉, 색상 스킴 결정
- **Frontend 에이전트**: 완전한 HTML/CSS/JS 코드 작성

## 🏗️ 팀 구성

| 팀원 | 역할 | AI 모델 | 특기 |
|------|------|---------|------|
| **Alex** | PM | Llama 3.3 70B | 기획, 전략 |
| **Maya** | Designer | Llama 3.3 70B | UI/UX 디자인 |
| **Chris** | Frontend | Llama 3.3 70B | 웹 개발 |
| **Jordan** | Backend | Mixtral 8x7b | API, 서버 |
| **Sam** | Researcher | DuckDuckGo + Llama | 시장조사 |

## 🚀 실행 방법

### 1. API 키 설정

`.env` 파일에 Groq API 키가 있는지 확인:

```bash
GROQ_API_KEY=your_key_here
```

### 2. 팀 포트폴리오 생성

```bash
source venv/bin/activate
python create_team_page.py
```

### 3. 결과 확인

```bash
open team_portfolio.html
```

## 📊 워크플로우

```
[PM 에이전트]
  ↓
팀 구성 완료
- 5명의 팀원 정의
- 팀 비전 수립
- 3개 프로젝트 아이디어 생성
  ↓
[Designer 에이전트]
  ↓
디자인 기획 완료
- 페이지 레이아웃 설계
- 색상 스킴 결정
- UI/UX 컨셉 수립
  ↓
[Frontend 에이전트]
  ↓
코드 작성 완료
- 완전한 HTML 페이지
- 반응형 CSS
- 인터랙티브 JavaScript
  ↓
✅ team_portfolio.html 생성!
```

## 💡 출력 예시

생성되는 웹페이지는 다음을 포함합니다:

### Hero 섹션
- 팀 이름과 로고
- 팀 비전 및 미션

### Team 섹션
- 5명의 팀원 카드
- 각자의 역할, 스킬, 설명

### Projects 섹션
- 3개의 프로젝트 아이디어
- 기술 스택, 기능, 예상 기간

### Contact 섹션
- 프로젝트 시작 버튼

## 🎨 디자인 특징

- ✅ 다크 테마
- ✅ 반응형 디자인 (모바일 최적화)
- ✅ 그라데이션 배경
- ✅ 호버 애니메이션
- ✅ 스크롤 인터랙션
- ✅ 모던한 UI

## 🔧 커스터마이징

각 에이전트의 프롬프트를 수정하여:
- 팀 컨셉 변경
- 디자인 스타일 조정
- 프로젝트 아이디어 유형 변경

## 📁 파일 구조

```
langGraph/
├── create_team_page.py          # 메인 실행 파일
├── dev_team_state.py            # 상태 정의
├── dev_agents/
│   ├── pm_agent.py              # PM 에이전트
│   ├── designer_agent.py        # 디자이너 에이전트
│   └── frontend_agent.py        # 프론트엔드 에이전트
└── team_portfolio.html          # 생성된 결과 (실행 후)
```

## 🌟 주요 특징

1. **완전 자동화**: 한 번의 명령으로 완전한 웹사이트 생성
2. **멀티 에이전트 협업**: 각 전문가가 자기 역할 수행
3. **실시간 생성**: 매번 새로운 디자인과 아이디어
4. **무료**: Groq API 사용 (무료 티어)

## 🎯 활용 사례

- 팀 소개 페이지 자동 생성
- 포트폴리오 사이트 프로토타입
- 랜딩 페이지 아이디어 테스트
- AI 협업 시스템 데모
