# 🚀 빠른 시작 가이드

## 1️⃣ Groq API 키 발급 (1분, 무료)

1. **https://console.groq.com** 접속
2. **Sign Up** 또는 Google 계정으로 가입
3. 좌측 메뉴에서 **API Keys** 클릭
4. **Create API Key** 버튼 클릭
5. 이름 입력 (예: "langgraph-project")
6. **Submit** 클릭
7. 생성된 키 복사 (⚠️ 한 번만 보여줌!)

## 2️⃣ 프로젝트 설정

```bash
# 1. .env 파일 수정
# 복사한 API 키를 아래에 붙여넣기
nano .env

# 내용:
# GROQ_API_KEY=여기에_발급받은_키_붙여넣기

# 2. 가상환경 활성화
source venv/bin/activate

# 3. 테스트 실행
python main.py
```

## 3️⃣ 실행 결과

5개의 AI 에이전트가 순차적으로 작업합니다:

```
🤖 LLM: Groq Llama 3.3 70B (무료)
🔍 [시장조사 에이전트] 작업 중...
⚔️ [경쟁분석 에이전트] 작업 중...
💡 [기획 에이전트] 작업 중...
📊 [평가 에이전트] 작업 중...
📋 [PM 에이전트] 작업 중...

✨ 최종 기획서
====================================
[상세한 웹사이트 기획서가 출력됩니다]
```

최종 기획서는 `final_plan.md` 파일로 저장됩니다!

## 🎯 커스터마이징

`main.py` 파일 하단의 예제를 수정하세요:

```python
user_input = """
    여기에 원하는 웹사이트 설명 입력
    예: AI 도구 모음 사이트를 만들고 싶어요
"""

constraints = """
    - 제약조건 입력
    예: 1개월 안에 완성, 혼자서 개발
"""
```

## ⚠️ 문제 해결

### API 키 오류
```
Error: Invalid API key
```
→ `.env` 파일의 `GROQ_API_KEY` 확인

### 모듈 없음 오류
```
ModuleNotFoundError: No module named 'langgraph'
```
→ `source venv/bin/activate` 실행 후 재시도

### 인코딩 오류
```
UnicodeDecodeError
```
→ 터미널 인코딩 UTF-8 설정: `export LANG=ko_KR.UTF-8`
