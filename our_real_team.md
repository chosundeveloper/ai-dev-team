# 🔥 Spark Labs - 진짜 팀 구성

## 🤖 AI 엔진 (인프라)

### **Groq** - AI Engine Provider
- **역할**: 모든 에이전트의 LLM 엔진 제공
- **제공 모델**: Llama 3.3 70B, Mixtral 8x7b
- **특징**: 초고속 추론, 무료 API
- **포지션**: Infrastructure / AI Backend

### **Claude (Sonnet 3.5)** - Chief Developer  
- **역할**: 전체 시스템 개발, 실제 코드 작성, 아키텍처 설계
- **담당**: 풀스택 개발, AI 통합, 배포
- **특징**: 긴 컨텍스트, 코드 품질
- **포지션**: Lead Developer / System Architect

### **라Codex (GPT-5)** - On-Device Builder & QA  
- **역할**: 로컬 repo 직접 편집, 테스트/빌드 실행, 회귀 검증
- **담당**: Claude 설계를 실 코드로 구현하고 Git 워크플로우 관리
- **특징**: Codex CLI로 파일 단위 제어, 빠른 QA 루프
- **포지션**: Execution Engineer / Quality Lead

---

## 👥 AI 에이전트 팀 (Groq 엔진으로 구동)

### **Alex** - Product Manager
- **AI 엔진**: Groq Llama 3.3 70B
- **역할**: 전략 기획, 시장 분석, 제품 방향 설정
- **포지션**: PM / Strategy

### **Maya** - UI/UX Designer
- **AI 엔진**: Groq Llama 3.3 70B
- **역할**: 디자인 시스템, 사용자 경험, 프로토타입
- **포지션**: Design Lead

### **Chris** - Frontend Developer
- **AI 엔진**: Groq Llama 3.3 70B
- **역할**: React/Next.js 개발, UI 구현
- **포지션**: Frontend Engineer

### **Jordan** - Backend Developer
- **AI 엔진**: Groq Mixtral 8x7b
- **역할**: API 설계, 데이터베이스, 서버 로직
- **포지션**: Backend Engineer

### **Sam** - Growth Hacker
- **AI 엔진**: DuckDuckGo (검색) + Groq Llama 3.3 (분석)
- **역할**: 실시간 트렌드 분석, 바이럴 마케팅
- **포지션**: Growth / Marketing

---

## 🏗️ 시스템 구조

```
[사용자 요청]
    ↓
[Claude] ← 전체 총괄, 실제 코드 작성
    ↘
   [라Codex] ← 로컬 편집/테스트/QA
    ↓
[LangGraph 워크플로우]
    ↓
[Groq API] ← 5개 에이전트의 두뇌
    ↓
Alex (PM) → Maya (Design) → Chris (Frontend) → Jordan (Backend) ← Sam (Growth)
    ↓
[완성된 제품]
```

---

## 💡 역할 정리

| 이름 | 진짜 정체 | 역할 | 포지션 |
|------|---------|------|--------|
| **Groq** | AI 인프라 | LLM 엔진 제공 | Infrastructure |
| **Claude** | AI 개발자 | 실제 개발, 코드 작성 | Chief Developer |
| **라Codex** | AI 실행 엔진 | 로컬 편집/테스트/QA | Execution & QA |
| **Alex** | AI Agent | 기획, 전략 | Product Manager |
| **Maya** | AI Agent | 디자인 | UI/UX Designer |
| **Chris** | AI Agent | 프론트엔드 | Frontend Dev |
| **Jordan** | AI Agent | 백엔드 | Backend Dev |
| **Sam** | AI Agent | 마케팅 | Growth Hacker |

---

## 🎯 누가 뭘 하나?

- **Groq**: 에이전트들한테 "생각하는 능력" 제공
- **Claude**: 전체를 보고 "실제로 코드 작성"
- **라Codex**: 로컬 환경에서 "실행·테스트·QA" 담당
- **AI 에이전트들**: 각자 전문 분야에서 "아이디어와 전략 제공"

---

**결론**: Groq · Claude · 라Codex가 실제 "엔진"이고, 
에이전트들은 그 엔진을 사용하는 "전문가 팀"!
