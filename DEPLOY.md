# 🚀 GitHub Pages 배포 가이드

## 📋 개요

팀 포트폴리오 페이지를 GitHub Actions를 통해 자동으로 배포합니다.

## 🔧 배포 과정

### 1️⃣ GitHub 저장소 생성

```bash
# 1. GitHub에서 새 저장소 생성 (public)
#    https://github.com/new

# 2. 로컬에서 Git 초기화
git init
git add .
git commit -m "🚀 Initial commit: AI 개발팀 포트폴리오"

# 3. 원격 저장소 연결
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 2️⃣ GitHub Pages 활성화

1. GitHub 저장소 페이지 이동
2. **Settings** 탭 클릭
3. 좌측 메뉴에서 **Pages** 클릭
4. **Source** 섹션에서:
   - Source: **GitHub Actions** 선택

### 3️⃣ 자동 배포 확인

```bash
# 코드 수정 후 푸시하면 자동 배포
git add .
git commit -m "Update portfolio"
git push
```

**Actions 탭**에서 배포 진행 상황 확인 가능!

## 🌐 배포 URL

배포 완료 후 다음 URL에서 접속 가능:

```
https://YOUR_USERNAME.github.io/YOUR_REPO/team_portfolio.html
```

## ⚙️ 워크플로우 구성

`.github/workflows/deploy.yml` 파일이 배포를 자동화합니다:

### 트리거
- `main` 브랜치에 push할 때
- 수동 실행 (workflow_dispatch)

### 빌드 단계
1. 코드 체크아웃
2. Python 3.13 설정
3. 의존성 설치 (LangGraph, LangChain 등)
4. `demo_team_page.py` 실행하여 HTML 생성
5. 아티팩트 업로드

### 배포 단계
1. GitHub Pages에 배포
2. 배포 URL 출력

## 🎯 장점

✅ **완전 자동화**: 푸시만 하면 자동 배포
✅ **무료**: GitHub Pages + GitHub Actions 무료
✅ **HTTPS**: 자동으로 SSL 인증서 적용
✅ **CDN**: GitHub의 글로벌 CDN 사용
✅ **버전 관리**: Git으로 모든 변경 사항 추적

## 📁 배포되는 파일

```
langGraph/
├── team_portfolio.html     # 메인 페이지
├── README.md              # 프로젝트 설명
└── .github/
    └── workflows/
        └── deploy.yml     # 배포 워크플로우
```

## 🔄 업데이트 방법

### 팀 정보 변경

`demo_team_page.py` 파일을 수정 후:

```bash
python demo_team_page.py  # 로컬 테스트
git add .
git commit -m "Update team info"
git push  # 자동 배포!
```

### AI로 동적 생성

API 키가 있다면 `create_team_page.py` 사용:

```bash
# .env에 GROQ_API_KEY 설정 필요 (GitHub Secrets)
python create_team_page.py
```

## 🐛 문제 해결

### 배포가 안 될 때

1. **Actions 탭 확인**: 에러 로그 확인
2. **Pages 설정 확인**: Source가 "GitHub Actions"인지 확인
3. **권한 확인**: Settings > Actions > General > Workflow permissions에서 "Read and write permissions" 활성화

### HTML이 업데이트 안 될 때

```bash
# 캐시 삭제 후 재배포
git commit --allow-empty -m "Trigger rebuild"
git push
```

## 💡 고급 설정

### 커스텀 도메인

1. GitHub Pages 설정에서 Custom domain 입력
2. DNS에 CNAME 레코드 추가

### 환경 변수 (Secrets)

Actions에서 API 키 사용하려면:

1. Settings > Secrets and variables > Actions
2. New repository secret 클릭
3. `GROQ_API_KEY` 추가

`.github/workflows/deploy.yml`에 추가:
```yaml
env:
  GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
```

## 📊 배포 상태 뱃지

README에 추가:

```markdown
![Deploy Status](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/deploy.yml/badge.svg)
```
