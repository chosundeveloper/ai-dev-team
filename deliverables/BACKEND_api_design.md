# ⚙️ Backend API 설계 문서

**작성자**: Backend Engineer Jordan
**작성일**: 2025-11-14

---

## 📡 API 엔드포인트

### 1. 뉴스 조회

#### `GET /api/news`
최신 뉴스 목록 조회

**Query Parameters**:
```
?limit=10           # 결과 개수 (기본: 10, 최대: 50)
?category=frontend  # 카테고리 필터
?date=2025-11-14   # 날짜 필터
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "title": "React 19 RC 출시",
      "summary": "새로운 Compiler 기능과 Server Components 안정화",
      "url": "https://github.com/facebook/react/releases",
      "source": "github",
      "category": "frontend",
      "importance_score": 95,
      "published_at": "2025-11-14T08:30:00Z",
      "read_time_minutes": 3
    }
  ],
  "total": 25,
  "page": 1
}
```

---

### 2. 구독 관리

#### `POST /api/subscribe`
이메일 구독

**Request Body**:
```json
{
  "email": "developer@example.com"
}
```

**Response**:
```json
{
  "success": true,
  "message": "구독이 완료되었습니다. 확인 이메일을 확인해주세요.",
  "data": {
    "email": "developer@example.com",
    "subscribed_at": "2025-11-14T09:00:00Z"
  }
}
```

---

#### `DELETE /api/unsubscribe/:token`
구독 취소

**Response**:
```json
{
  "success": true,
  "message": "구독이 취소되었습니다."
}
```

---

### 3. 아카이브

#### `GET /api/archive`
지난 뉴스레터 목록

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": "newsletter-2025-11-14",
      "date": "2025-11-14",
      "subject": "AI 모델 발전과 React 19 출시",
      "news_count": 7,
      "sent_to": 523,
      "url": "/archive/2025-11-14"
    }
  ]
}
```

---

## 🗄️ 데이터베이스 스키마

### Subscribers 테이블
```sql
CREATE TABLE subscribers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT true,
    unsubscribe_token VARCHAR(64) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_subscribers_email ON subscribers(email);
CREATE INDEX idx_subscribers_active ON subscribers(active);
```

### News 테이블
```sql
CREATE TABLE news (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(500) NOT NULL,
    summary TEXT NOT NULL,
    url TEXT NOT NULL,
    source VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    importance_score INTEGER NOT NULL CHECK (importance_score BETWEEN 0 AND 100),
    published_at TIMESTAMP NOT NULL,
    crawled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(url, published_at)
);

CREATE INDEX idx_news_published ON news(published_at DESC);
CREATE INDEX idx_news_category ON news(category);
CREATE INDEX idx_news_score ON news(importance_score DESC);
```

### Newsletters 테이블
```sql
CREATE TABLE newsletters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sent_at TIMESTAMP NOT NULL,
    subject VARCHAR(500) NOT NULL,
    news_ids UUID[] NOT NULL,
    recipient_count INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_newsletters_sent ON newsletters(sent_at DESC);
```

---

## 🤖 AI 큐레이션 로직

### 1. 뉴스 수집 (매일 오전 6시)
```python
async def crawl_daily_news():
    sources = [
        crawl_github_trending(),
        crawl_hacker_news(),
        crawl_reddit_programming()
    ]

    news_items = await asyncio.gather(*sources)
    return flatten(news_items)
```

### 2. AI 요약 및 점수 산정
```python
async def process_with_ai(news_item):
    prompt = f"""
    다음 뉴스를 개발자를 위해 2문장으로 요약하고,
    중요도를 0-100점으로 평가해주세요.

    제목: {news_item.title}
    내용: {news_item.content}
    """

    response = await groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "summary": extract_summary(response),
        "score": extract_score(response)
    }
```

### 3. 뉴스 선정 알고리즘
```python
def select_top_news(news_items, count=7):
    # 1. 중요도 점수 80점 이상
    high_importance = filter(lambda x: x.score >= 80, news_items)

    # 2. 카테고리별 균형 (Frontend 2, Backend 2, AI 2, DevOps 1)
    balanced = balance_categories(high_importance)

    # 3. 중복 제거 (유사도 80% 이상)
    unique = remove_duplicates(balanced, threshold=0.8)

    # 4. 점수 순 정렬
    return sorted(unique, key=lambda x: x.score, reverse=True)[:count]
```

---

## 📧 이메일 발송 시스템

### SendGrid 템플릿
```python
async def send_newsletter(newsletter_id: str):
    newsletter = await get_newsletter(newsletter_id)
    subscribers = await get_active_subscribers()

    for subscriber in subscribers:
        await send_email(
            to=subscriber.email,
            template_id="d-newsletter-template",
            data={
                "date": newsletter.date,
                "news_items": newsletter.news,
                "unsubscribe_link": f"https://devdaily.io/unsubscribe/{subscriber.token}"
            }
        )
```

---

## ⏰ 스케줄러

### APScheduler 설정
```python
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

# 매일 오전 6시: 뉴스 크롤링 및 AI 처리
scheduler.add_job(
    crawl_and_process_news,
    trigger='cron',
    hour=6,
    minute=0
)

# 매일 오전 7시: 뉴스레터 발송
scheduler.add_job(
    send_daily_newsletter,
    trigger='cron',
    hour=7,
    minute=0
)

scheduler.start()
```

---

## 🔒 보안

### 1. Rate Limiting
```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/subscribe")
@limiter.limit("5/hour")
async def subscribe(request: Request, email: str):
    ...
```

### 2. Email 유효성 검사
```python
from email_validator import validate_email

def validate_subscriber_email(email: str):
    try:
        valid = validate_email(email)
        return valid.email
    except EmailNotValidError:
        raise HTTPException(400, "유효하지 않은 이메일")
```

### 3. Unsubscribe Token
```python
import secrets

def generate_unsubscribe_token():
    return secrets.token_urlsafe(32)
```

---

## 📊 모니터링

### 주요 지표
- **크롤링 성공률**: 목표 > 95%
- **AI 처리 속도**: 뉴스 1개당 < 2초
- **이메일 발송 성공률**: 목표 > 98%
- **API 응답 시간**: P95 < 500ms

---

**작성자**: Jordan (Backend Engineer)
**버전**: 1.0
**최종 수정**: 2025-11-14
