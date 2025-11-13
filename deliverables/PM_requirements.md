# 📋 프로젝트 요구사항 문서

**작성자**: PM Alex
**작성일**: 2025-11-14
**프로젝트**: 개발자 일일 뉴스레터 MVP

---

## 1. 프로젝트 개요

### 1.1 프로젝트명
**DevDaily** - AI가 큐레이션하는 개발자 일일 뉴스레터

### 1.2 목표
매일 아침 7시, AI가 GitHub Trending, Hacker News, Reddit을 분석해서 개발자에게 꼭 필요한 뉴스만 3분 분량으로 정리해서 이메일로 발송

### 1.3 타겟 사용자
- 주니어-시니어 개발자 (1-10년 경력)
- IT 종사자, 기술 리더
- 매일 기술 뉴스를 찾지만 시간이 부족한 사람들

---

## 2. 핵심 기능 (MVP)

### 2.1 P0 (필수 기능)
1. **뉴스 크롤링**
   - GitHub Trending 일일 프로젝트
   - Hacker News API
   - Reddit r/programming

2. **AI 요약 및 큐레이션**
   - Groq API (Llama 3.3 70B) 활용
   - 각 뉴스를 1-2문장으로 요약
   - 중요도 점수 산정 (0-100)

3. **이메일 구독**
   - 이메일 주소로 구독
   - 구독 확인 이메일
   - 구독 취소 링크

4. **랜딩 페이지**
   - 서비스 소개
   - 구독 폼
   - 샘플 뉴스레터 미리보기

5. **일일 뉴스레터 발송**
   - 매일 오전 7시 자동 발송
   - 상위 5-7개 뉴스 포함
   - 카테고리별 분류

### 2.2 P1 (중요 기능)
- 아카이브 페이지 (지난 뉴스레터)
- 카테고리 필터 (Frontend, Backend, AI, DevOps)
- 모바일 반응형 디자인
- 사용자 관리 API

### 2.3 P2 (선택 기능)
- 다크 모드
- 소셜 공유

---

## 3. 기술 스택

### 3.1 Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite (MVP) → PostgreSQL (프로덕션)
- **AI**: Groq API (무료, Llama 3.3 70B)
- **Crawler**: DuckDuckGo API + BeautifulSoup
- **Email**: SendGrid (무료 100통/일)
- **Scheduler**: APScheduler

### 3.2 Frontend
- **Framework**: React 18 + Vite
- **Styling**: Tailwind CSS
- **State Management**: React Query + Context API
- **Routing**: React Router v6

### 3.3 배포
- **Backend**: Render (무료)
- **Frontend**: Vercel (무료)
- **CI/CD**: GitHub Actions

---

## 4. 데이터 모델

### 4.1 Subscribers
```python
{
    "id": UUID,
    "email": String,
    "subscribed_at": DateTime,
    "active": Boolean,
    "unsubscribe_token": String
}
```

### 4.2 News
```python
{
    "id": UUID,
    "title": String,
    "summary": String (AI 생성),
    "url": String,
    "source": String (GitHub/HN/Reddit),
    "category": String,
    "importance_score": Integer (0-100),
    "published_at": DateTime,
    "crawled_at": DateTime
}
```

### 4.3 Newsletters
```python
{
    "id": UUID,
    "sent_at": DateTime,
    "news_ids": Array[UUID],
    "recipient_count": Integer,
    "subject": String
}
```

---

## 5. API 엔드포인트

### 5.1 공개 API
- `GET /api/news` - 최신 뉴스 목록
- `POST /api/subscribe` - 이메일 구독
- `GET /api/archive` - 지난 뉴스레터
- `DELETE /api/unsubscribe/:token` - 구독 취소

### 5.2 내부 API
- `POST /api/crawl` - 수동 크롤링 트리거
- `POST /api/send-newsletter` - 뉴스레터 수동 발송

---

## 6. 일정 및 마일스톤

### Week 1 (D+0 ~ D+7)
- ✅ 요구사항 정의
- ✅ 기술 스택 확정
- ✅ 설계 완료
- 🔄 백엔드 개발 (크롤러 + AI)
- 🔄 프론트엔드 개발 (랜딩 페이지)

### Week 2 (D+8 ~ D+14)
- 통합 테스트
- 배포
- 첫 10명 베타 테스터 모집
- ProductHunt 런칭

---

## 7. 성공 지표

### 7.1 기술적 성공
- 크롤링 성공률 > 95%
- AI 요약 품질 (사람이 읽을 만한 수준)
- 이메일 발송 성공률 > 98%
- 페이지 로딩 < 2초

### 7.2 비즈니스 성공
- Week 1: 첫 10명 구독자
- Week 2: 100명 구독자
- Month 1: 500명 구독자
- 구독 취소율 < 10%

---

## 8. 리스크 및 대응

### 8.1 기술적 리스크
| 리스크 | 확률 | 영향 | 대응책 |
|--------|------|------|--------|
| API 제한 (Groq) | 중 | 중 | 캐싱, 요청 최적화 |
| 크롤링 차단 | 중 | 높 | User-Agent, 속도 제한 |
| 이메일 스팸 처리 | 낮 | 높 | SPF/DKIM 설정 |

### 8.2 비즈니스 리스크
| 리스크 | 확률 | 영향 | 대응책 |
|--------|------|------|--------|
| 사용자 관심 부족 | 중 | 높 | 마케팅 강화, 피드백 |
| 경쟁 서비스 | 낮 | 중 | 차별화 (AI 품질) |

---

## 9. 다음 단계

1. ✅ 요구사항 정의 완료
2. ✅ 기술 스택 확정
3. 🔄 백엔드 개발 시작
4. 🔄 프론트엔드 개발 시작
5. ⏳ 통합 테스트
6. ⏳ 배포 및 런칭

---

**작성자**: PM Alex
**승인**: 2025-11-14
**버전**: 1.0
