"""
Spark Labs - Groq과 Claude를 제대로 소개
"""

def create_final_page():
    """Groq과 Claude를 포함한 최종 팀 페이지"""

    html = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spark Labs - Viral Product Builders</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #e2e8f0;
            line-height: 1.6;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }

        /* Hero */
        .hero {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, #f59e0b, #ea580c, #dc2626);
            border-radius: 20px;
            margin-bottom: 4rem;
            position: relative;
            overflow: hidden;
        }
        .hero-actions {
            margin-top: 2rem;
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }
        .hero-actions a {
            padding: 0.9rem 1.8rem;
            border-radius: 999px;
            font-weight: 600;
            text-decoration: none;
            transition: transform 0.2s ease;
        }
        .hero-actions a.primary {
            background: linear-gradient(135deg, #f59e0b, #dc2626);
            color: white;
        }
        .hero-actions a.secondary {
            border: 1px solid rgba(255,255,255,0.5);
            color: white;
        }
        .hero-actions a:hover {
            transform: translateY(-3px);
        }
        .hero::before {
            content: '🔥';
            position: absolute;
            font-size: 15rem;
            opacity: 0.1;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            color: white;
            font-weight: 900;
            position: relative;
            z-index: 1;
        }
        .hero .tagline {
            font-size: 1.5rem;
            color: rgba(255,255,255,0.95);
            position: relative;
            z-index: 1;
        }

        /* Section */
        section { margin-bottom: 5rem; }
        h2 {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(135deg, #f59e0b, #dc2626);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
        }

        /* Infrastructure Team */
        .infra-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }
        .infra-card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 3rem;
            border-radius: 20px;
            border: 2px solid;
            position: relative;
            overflow: hidden;
        }
        .infra-card.groq {
            border-color: #f59e0b;
            background: linear-gradient(135deg, rgba(245,158,11,0.1), rgba(220,38,38,0.1));
        }
        .infra-card.claude {
            border-color: #8b5cf6;
            background: linear-gradient(135deg, rgba(139,92,246,0.1), rgba(99,102,241,0.1));
        }
        .infra-card.codex {
            border-color: #14b8a6;
            background: linear-gradient(135deg, rgba(20,184,166,0.12), rgba(59,130,246,0.08));
        }
        .infra-logo {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        .infra-card h3 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        .infra-card.groq h3 { color: #f59e0b; }
        .infra-card.claude h3 { color: #8b5cf6; }
        .infra-role {
            font-size: 1.2rem;
            color: #cbd5e1;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }
        .infra-description {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #cbd5e1;
            margin-bottom: 2rem;
        }
        .infra-specs {
            background: rgba(0,0,0,0.2);
            padding: 1.5rem;
            border-radius: 15px;
            margin-top: 1.5rem;
        }
        .spec-item {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin: 0.75rem 0;
            font-size: 1rem;
        }
        .spec-icon { font-size: 1.5rem; }

        /* Agent Team */
        .agent-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }
        .agent-card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s;
        }
        .agent-card:hover {
            transform: translateY(-10px);
            border-color: #f59e0b;
            box-shadow: 0 20px 40px rgba(245,158,11,0.2);
        }
        .avatar {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #f59e0b, #dc2626);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            margin: 0 auto 1rem;
        }
        .agent-card h3 {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
            text-align: center;
            color: #f59e0b;
        }
        .role {
            text-align: center;
            color: #cbd5e1;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        .engine {
            text-align: center;
            font-size: 0.85rem;
            color: #f59e0b;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        .description {
            font-size: 0.9rem;
            color: #cbd5e1;
            text-align: center;
        }

        /* Projects */
        .project-card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 2rem;
        }
        .project-title {
            font-size: 2rem;
            color: #f59e0b;
            margin-bottom: 1rem;
        }

        /* Build Plan */
        .plan-section {
            background: rgba(15,23,42,0.6);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 3rem 2rem;
            margin-bottom: 5rem;
        }
        .plan-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
        }
        .plan-step {
            background: rgba(255,255,255,0.04);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .plan-step h3 {
            font-size: 1.2rem;
            color: #f59e0b;
            margin-bottom: 0.5rem;
        }
        .plan-milestone {
            font-size: 0.95rem;
            color: #cbd5e1;
            margin-bottom: 0.75rem;
        }
        .plan-owners {
            font-size: 0.85rem;
            color: #38bdf8;
            font-weight: 600;
        }

        /* Build Report */
        .report-section {
            background: rgba(99,102,241,0.08);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 3rem 2rem;
            margin-bottom: 5rem;
        }
        .report-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .report-card {
            background: rgba(15,23,42,0.6);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .report-card h3 {
            font-size: 1.1rem;
            color: #f59e0b;
            margin-bottom: 0.5rem;
        }
        .report-card p,
        .report-card ul {
            font-size: 0.95rem;
            color: #cbd5e1;
            line-height: 1.5;
        }
        .report-card ul {
            list-style: disc;
            margin-left: 1.25rem;
        }

        /* Contributions */
        .contrib-section {
            background: rgba(15,23,42,0.6);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 3rem 2rem;
            margin-bottom: 5rem;
        }
        .contrib-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
        }
        .contrib-card {
            background: rgba(255,255,255,0.04);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .contrib-card h3 {
            font-size: 1.05rem;
            color: #38bdf8;
            margin-bottom: 0.5rem;
        }
        .contrib-card ul {
            list-style: disc;
            margin-left: 1.25rem;
            color: #cbd5e1;
            line-height: 1.5;
        }
        .viral-badge {
            display: inline-block;
            background: linear-gradient(135deg, #dc2626, #f59e0b);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        footer {
            text-align: center;
            padding: 3rem 2rem;
            color: #64748b;
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .infra-grid { grid-template-columns: 1fr; }
            .agent-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Hero -->
        <div class="hero">
            <h1>🔥 Spark Labs</h1>
            <p class="tagline">Igniting Viral Ideas</p>
            <p style="margin-top: 1rem; font-size: 1.1rem; position: relative; z-index: 1;">
                사용자가 열광하는 바이럴 제품을 2-4주 안에 만듭니다
            </p>
            <div class="hero-actions">
                <a class="primary" href="#build-plan">🧭 Build Plan 보기</a>
                <a class="secondary" href="#build-report">📝 Build Report 보기</a>
            </div>
        </div>

        <!-- Infrastructure Team -->
        <section>
            <h2>⚡ AI Infrastructure</h2>
            <p style="text-align: center; font-size: 1.2rem; color: #cbd5e1; margin-bottom: 3rem;">
                모든 AI 에이전트를 작동시키는 핵심 엔진
            </p>

            <div class="infra-grid">
                <!-- Groq -->
                <div class="infra-card groq">
                    <div class="infra-logo">⚡</div>
                    <h3>Groq</h3>
                    <p class="infra-role">AI Engine Provider</p>
                    <p class="infra-description">
                        초고속 LLM 추론 엔진. 모든 AI 에이전트(Alex, Maya, Chris, Jordan, Sam)의 두뇌를 제공합니다.
                        일반 GPU보다 10배 빠른 LPU(Language Processing Unit) 기술로 실시간 응답을 가능하게 합니다.
                    </p>
                    <div class="infra-specs">
                        <div class="spec-item">
                            <span class="spec-icon">🚀</span>
                            <span><strong>속도:</strong> 일반 대비 10배 빠른 추론</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">🤖</span>
                            <span><strong>모델:</strong> Llama 3.3 70B, Mixtral 8x7b</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">💰</span>
                            <span><strong>가격:</strong> 완전 무료 API (Free Tier)</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">🔗</span>
                            <span><strong>역할:</strong> 5개 에이전트의 LLM 엔진</span>
                        </div>
                    </div>
                </div>

                <!-- Claude -->
                <div class="infra-card claude">
                    <div class="infra-logo">🧠</div>
                    <h3>Claude</h3>
                    <p class="infra-role">Chief Developer & Orchestrator</p>
                    <p class="infra-description">
                        전체 시스템을 총괄하고 실제 코드를 작성하는 AI 개발자.
                        LangGraph로 5개 에이전트를 조율하고, 프론트엔드부터 백엔드까지 풀스택 개발을 담당합니다.
                    </p>
                    <div class="infra-specs">
                        <div class="spec-item">
                            <span class="spec-icon">💻</span>
                            <span><strong>역할:</strong> 실제 코드 작성 및 시스템 설계</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">🔄</span>
                            <span><strong>오케스트레이션:</strong> LangGraph 워크플로우 관리</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">📚</span>
                            <span><strong>컨텍스트:</strong> 200K 토큰 (긴 문서 처리)</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">🎯</span>
                            <span><strong>포지션:</strong> Lead Developer / Architect</span>
                        </div>
                    </div>
                </div>

                <!-- 라Codex -->
                <div class="infra-card codex">
                    <div class="infra-logo">🛠️</div>
                    <h3>라Codex</h3>
                    <p class="infra-role">On-Device Builder & QA</p>
                    <p class="infra-description">
                        Claude의 설계를 바탕으로 실제 로컬 환경에서 코드를 작성하고 테스트하는 실행형 AI 엔지니어.
                        Codex CLI로 repo를 직접 수정하고 lint/test를 돌리며, 모든 산출물을 Git에 남깁니다.
                    </p>
                    <div class="infra-specs">
                        <div class="spec-item">
                            <span class="spec-icon">🧠</span>
                            <span><strong>모델:</strong> GPT-5 Codex (실행 특화)</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">🛠️</span>
                            <span><strong>역할:</strong> 파일 편집, 테스트, 스크립트 실행</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">🧪</span>
                            <span><strong>품질:</strong> 로컬 검증 & 회귀 체크</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-icon">🤝</span>
                            <span><strong>협업:</strong> Claude 지시 ↔ Groq 에이전트 결과 통합</span>
                        </div>
                    </div>
                </div>
            </div>

            <div style="background: rgba(245,158,11,0.1); padding: 2rem; border-radius: 15px; border: 1px solid #f59e0b; margin-top: 2rem;">
                <p style="text-align: center; font-size: 1.1rem;">
                    <strong>🔧 작동 방식:</strong>
                    Claude가 LangGraph로 워크플로우를 구성 →
                    각 에이전트가 Groq 엔진으로 사고 →
                    라Codex가 로컬에서 코드 적용·테스트 →
                    완성된 제품 🎉
                </p>
            </div>
        </section>

        <!-- AI Agent Team -->
        <section>
            <h2>👥 AI Agent Team</h2>
            <p style="text-align: center; font-size: 1.2rem; color: #cbd5e1; margin-bottom: 3rem;">
                Groq 엔진으로 작동하는 5명의 전문 AI 에이전트
            </p>

            <div class="agent-grid">
                <div class="agent-card">
                    <div class="avatar">A</div>
                    <h3>Alex</h3>
                    <p class="role">Product Manager</p>
                    <p class="engine">⚡ Powered by Groq Llama 3.3 70B</p>
                    <p class="description">전략 기획, 시장 분석, 제품 방향 설정</p>
                </div>

                <div class="agent-card">
                    <div class="avatar">M</div>
                    <h3>Maya</h3>
                    <p class="role">UI/UX Designer</p>
                    <p class="engine">⚡ Powered by Groq Llama 3.3 70B</p>
                    <p class="description">디자인 시스템, 사용자 경험</p>
                </div>

                <div class="agent-card">
                    <div class="avatar">C</div>
                    <h3>Chris</h3>
                    <p class="role">Frontend Developer</p>
                    <p class="engine">⚡ Powered by Groq Llama 3.3 70B</p>
                    <p class="description">React, Next.js, UI 구현</p>
                </div>

                <div class="agent-card">
                    <div class="avatar">J</div>
                    <h3>Jordan</h3>
                    <p class="role">Backend Developer</p>
                    <p class="engine">⚡ Powered by Groq Mixtral 8x7b</p>
                    <p class="description">API, 데이터베이스, 서버 로직</p>
                </div>

                <div class="agent-card">
                    <div class="avatar">S</div>
                    <h3>Sam</h3>
                    <p class="role">Growth Hacker</p>
                    <p class="engine">⚡ DuckDuckGo + Groq Llama 3.3</p>
                    <p class="description">실시간 트렌드, 바이럴 마케팅</p>
                </div>
            </div>
        </section>

        <!-- Current Products -->
        <section>
            <h2>🚀 지금 바로 만드는 제품</h2>

            <div class="project-card">
                <h3 class="project-title">🧑‍💻 AI 팀 포트폴리오 퍼블리셔</h3>
                <span class="viral-badge">🔧 실서비스</span>
                <p style="font-size: 1.1rem; margin: 1rem 0; color: #cbd5e1;">
                    PM → 디자이너 → 프론트엔드 에이전트가 협업해 완성된 팀 소개 페이지를 즉시 HTML/CSS로 뽑아냅니다.
                </p>
                <p><strong>출력:</strong> team_portfolio.html | <strong>시간:</strong> 수 분</p>
            </div>

            <div class="project-card">
                <h3 class="project-title">📄 AI 웹사이트 기획서 메이커</h3>
                <span class="viral-badge">🔧 실서비스</span>
                <p style="font-size: 1.1rem; margin: 1rem 0; color: #cbd5e1;">
                    LangGraph 멀티 에이전트가 시장조사→경쟁분석→아이디어→평가→PM 단계를 거쳐 완성된 기획서를 Markdown으로 제공합니다.
                </p>
                <p><strong>출력:</strong> final_plan.md | <strong>시간:</strong> 수 분</p>
            </div>

            <div class="project-card">
                <h3 class="project-title">🧾 Launch Snapshot</h3>
                <span class="viral-badge">🔧 실서비스</span>
                <p style="font-size: 1.1rem; margin: 1rem 0; color: #cbd5e1;">
                    실행 중인 프로젝트의 계획/보고서를 즉시 페이지에 반영해 팀 상태를 공유하는 경량 리포트 모듈입니다.
                </p>
                <p><strong>출력:</strong> Build Plan & Report 섹션 | <strong>시간:</strong> 즉시</p>
            </div>
        </section>

        <!-- Build Plan -->
        <section id="build-plan" class="plan-section">
            <h2>🧭 Build Plan</h2>
            <p style="text-align: center; font-size: 1.1rem; color: #cbd5e1; margin-bottom: 2rem;">
                지금 실제로 돌리고 있는 <strong>AI 팀 포트폴리오 퍼블리셔</strong> 제작 순서입니다. (전체 리드타임: 15분 이내)
            </p>
            <div class="plan-grid">
                <div class="plan-step">
                    <h3>Step 1 · Brief Intake</h3>
                    <p class="plan-milestone">요구사항/톤/색상 입력 정리 (2분)</p>
                    <p class="plan-owners">Owners · Alex (PM)</p>
                </div>
                <div class="plan-step">
                    <h3>Step 2 · Layout & Palette</h3>
                    <p class="plan-milestone">페이지 레이아웃 + 컬러 시스템 확정 (4분)</p>
                    <p class="plan-owners">Owners · Maya (Design)</p>
                </div>
                <div class="plan-step">
                    <h3>Step 3 · Frontend Build</h3>
                    <p class="plan-milestone">완전한 HTML/CSS/애니메이션 작성 (6분)</p>
                    <p class="plan-owners">Owners · Chris (FE), 라Codex (Execution)</p>
                </div>
                <div class="plan-step">
                    <h3>Step 4 · QA & Polish</h3>
                    <p class="plan-milestone">반응형 체크, 카피 정리, CTA 연결 (2분)</p>
                    <p class="plan-owners">Owners · 라Codex (QA), Sam (Growth)</p>
                </div>
                <div class="plan-step">
                    <h3>Step 5 · Publish & Share</h3>
                    <p class="plan-milestone">GitHub Pages 배포 + 링크 공유 (1분)</p>
                    <p class="plan-owners">Owners · Claude (Lead Dev), 라Codex (Execution)</p>
                </div>
            </div>
        </section>

        <!-- Build Report -->
        <section id="build-report" class="report-section">
            <h2>📝 Build Report</h2>
            <p style="text-align: center; font-size: 1.05rem; color: #cbd5e1;">
                방금 실행한 <strong>AI 팀 포트폴리오 퍼블리셔</strong> 결과 보고입니다.
            </p>
            <div class="report-grid">
                <div class="report-card">
                    <h3>What we ship</h3>
                    <p>`team_portfolio.html` + 동일 스타일의 `index.html` (즉시 배포 가능).</p>
                </div>
                <div class="report-card">
                    <h3>Why it matters</h3>
                    <ul>
                        <li>팀 역량·워크플로우를 투명하게 보여주는 레퍼런스</li>
                        <li>투자자/고객에게 즉시 공유 가능한 자산</li>
                    </ul>
                </div>
                <div class="report-card">
                    <h3>Timeline</h3>
                    <p>총 15분. 0-2분 브리프 → 2-6분 디자인 → 6-12분 프론트엔드 → 12-14분 QA → 14-15분 배포.</p>
                </div>
                <div class="report-card">
                    <h3>Owners & stack</h3>
                    <ul>
                        <li>Alex — 요구사항 브리핑</li>
                        <li>Maya — 레이아웃/컬러</li>
                        <li>Chris + 라Codex — HTML/CSS 작성</li>
                        <li>Claude — 배포 & Git 관리</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Contributions -->
        <section id="contributors" class="contrib-section">
            <h2>👥 누가 무엇을 기여했나요?</h2>
            <p style="text-align: center; font-size: 1rem; color: #cbd5e1; margin-bottom: 2rem;">
                이번 AI 팀 포트폴리오 퍼블리셔 실행에서 각 역할이 담당한 범위입니다.
            </p>
            <div class="contrib-grid">
                <div class="contrib-card">
                    <h3>Alex · PM</h3>
                    <ul>
                        <li>요구사항/톤 브리프 정리</li>
                        <li>Build Plan 단계 정의</li>
                        <li>README 실행 요약 작성</li>
                    </ul>
                </div>
                <div class="contrib-card">
                    <h3>Maya · Design</h3>
                    <ul>
                        <li>레이아웃·컬러 토큰 선정</li>
                        <li>Hero/섹션 배치 가이드 제공</li>
                    </ul>
                </div>
                <div class="contrib-card">
                    <h3>Chris · Frontend</h3>
                    <ul>
                        <li>HTML/CSS 구조 구현</li>
                        <li>애니메이션·반응형 세부 조정</li>
                    </ul>
                </div>
                <div class="contrib-card">
                    <h3>라Codex · Execution</h3>
                    <ul>
                        <li>실제 파일 편집 & 테스트</li>
                        <li>Git 커밋/배포 파이프라인 운영</li>
                    </ul>
                </div>
                <div class="contrib-card">
                    <h3>Claude · Lead Dev</h3>
                    <ul>
                        <li>LangGraph 워크플로우 총괄</li>
                        <li>final_spark_labs.py 및 README 지휘</li>
                    </ul>
                </div>
                <div class="contrib-card">
                    <h3>Sam · Growth</h3>
                    <ul>
                        <li>카피·CTA 검수</li>
                        <li>보고서 공유 시나리오 작성</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- CTA -->
        <section style="text-align: center; background: linear-gradient(135deg, rgba(245,158,11,0.1), rgba(220,38,38,0.1)); padding: 4rem 2rem; border-radius: 20px;">
            <h2>Ready to Ship Now?</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem; color: #cbd5e1;">
                AI 팀 포트폴리오와 웹 기획서를 오늘 바로 받아보세요
            </p>
            <a href="https://github.com/chosundeveloper/ai-dev-team"
               style="display: inline-block; padding: 1rem 2.5rem; background: linear-gradient(135deg, #f59e0b, #dc2626); color: white; text-decoration: none; border-radius: 50px; font-weight: 600; font-size: 1.1rem;">
                GitHub 보기 →
            </a>
        </section>
    </div>

    <footer>
        <p><strong>Spark Labs</strong> - Building Products That Go Viral</p>
        <p style="margin-top: 0.5rem;">
            <strong>Infrastructure:</strong> Groq (AI Engine) + Claude (Chief Developer) + 라Codex (On-Device Builder)
        </p>
        <p style="margin-top: 0.5rem;">
            <strong>Agents:</strong> Alex (PM) + Maya (Designer) + Chris (Frontend) + Jordan (Backend) + Sam (Growth)
        </p>
        <p style="margin-top: 1rem; font-size: 0.9rem;">
            Powered by LangGraph × Groq × Claude × 라Codex × Multi-Agent AI
        </p>
    </footer>
</body>
</html>"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("✅ Spark Labs 최종 페이지 생성 완료!")
    print("📄 Groq, Claude, 라Codex를 Infrastructure로 명확히 소개")
    print("👥 5명의 AI 에이전트 (Groq 엔진 사용)")
    print("🚀 3개의 즉시 실행 제품 정보 포함")

if __name__ == "__main__":
    create_final_page()
