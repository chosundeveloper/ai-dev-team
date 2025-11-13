# ⚡ 빠른 시작 가이드

## 🎯 단계별 배포 (5분 완성)

### 1️⃣ GitHub 저장소 생성 (1분)

1. **https://github.com/new** 접속
2. Repository name 입력 (예: `ai-dev-team`)
3. **Public** 선택
4. ✅ **Add a README file** 체크 해제
5. **Create repository** 클릭

### 2️⃣ 코드 푸시 (1분)

```bash
# 원격 저장소 연결 (YOUR_USERNAME과 YOUR_REPO 수정!)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# 푸시
git push -u origin main
```

**예시**:
```bash
git remote add origin https://github.com/john/ai-dev-team.git
git push -u origin main
```

### 3️⃣ GitHub Pages 활성화 (1분)

1. GitHub 저장소 페이지에서 **Settings** 탭
2. 좌측 메뉴 **Pages** 클릭
3. **Source** → **GitHub Actions** 선택
4. 완료!

### 4️⃣ 배포 확인 (2분)

1. **Actions** 탭 클릭
2. 워크플로우 실행 확인 (🟢 초록색이 성공)
3. 배포 완료 후 URL 확인:
   ```
   https://YOUR_USERNAME.github.io/YOUR_REPO/team_portfolio.html
   ```

## ✅ 완료!

이제 팀 포트폴리오가 온라인에 배포되었습니다! 🎉

### 다음 단계

#### 로컬에서 테스트
```bash
# 가상환경 활성화
source venv/bin/activate

# 팀 페이지 재생성
python demo_team_page.py

# 브라우저에서 확인
open team_portfolio.html
```

#### 웹사이트 기획 시스템 사용
```bash
# Groq API 키 설정
# .env 파일에 GROQ_API_KEY 입력

# 기획 시스템 실행
python main.py
```

#### 내용 업데이트
```bash
# demo_team_page.py 수정 후
git add .
git commit -m "Update team info"
git push

# 자동으로 재배포됨! 🚀
```

## 🆘 문제 해결

### 푸시가 안 될 때
```bash
# 인증 확인
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Personal Access Token 사용
# https://github.com/settings/tokens
```

### 배포가 실패할 때
1. **Actions** 탭에서 에러 로그 확인
2. `.github/workflows/deploy.yml` 파일 확인
3. 의존성 설치 문제: `requirements.txt` 추가 고려

### 페이지가 안 보일 때
- Actions 탭에서 배포 완료 확인
- 5분 정도 기다린 후 새로고침
- URL이 정확한지 확인

## 📚 더 자세한 가이드

- **[DEPLOY.md](DEPLOY.md)** - 상세 배포 가이드
- **[README.md](README.md)** - 프로젝트 전체 설명
- **[TEAM_README.md](TEAM_README.md)** - 팀 활용법

---

**💡 팁**: 이 프로젝트를 포크(Fork)해서 시작하면 더 빠릅니다!
