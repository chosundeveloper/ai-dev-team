"""
API 없이 데모 팀 페이지 생성
"""
from dev_team_state import DevTeamState, TeamMember, ProjectIdea


def create_demo_page():
    """데모 팀 페이지 생성 (API 불필요)"""
    print("🚀 AI 개발팀 데모 페이지 생성 중...\n")

    # 팀 구성
    team_members: list[TeamMember] = [
        {
            'name': 'Alex',
            'role': 'Product Manager',
            'model': 'Llama 3.3 70B',
            'skills': ['전략 기획', '요구사항 분석', '프로젝트 관리', '시장 분석'],
            'description': '팀의 비전을 설정하고 프로젝트를 이끄는 전략가입니다.'
        },
        {
            'name': 'Maya',
            'role': 'UI/UX Designer',
            'model': 'Llama 3.3 70B',
            'skills': ['UI 디자인', '사용자 경험', '프로토타이핑', '디자인 시스템'],
            'description': '아름답고 직관적인 인터페이스를 만드는 디자이너입니다.'
        },
        {
            'name': 'Chris',
            'role': 'Frontend Developer',
            'model': 'Llama 3.3 70B',
            'skills': ['React', 'TypeScript', 'HTML/CSS', 'Next.js'],
            'description': '사용자가 보는 모든 것을 완벽하게 구현하는 개발자입니다.'
        },
        {
            'name': 'Jordan',
            'role': 'Backend Developer',
            'model': 'Mixtral 8x7b',
            'skills': ['Python', 'FastAPI', 'PostgreSQL', 'Docker'],
            'description': '탄탄한 서버 로직과 API를 구축하는 백엔드 전문가입니다.'
        },
        {
            'name': 'Sam',
            'role': 'Market Researcher',
            'model': 'DuckDuckGo + Llama 3.3',
            'skills': ['시장 조사', '트렌드 분석', '경쟁 분석', 'SEO'],
            'description': '실시간 시장 데이터로 인사이트를 제공하는 리서처입니다.'
        }
    ]

    # 프로젝트 아이디어
    project_ideas: list[ProjectIdea] = [
        {
            'title': '🎯 AI 웹사이트 기획 도구',
            'description': '조회수 높은 웹사이트를 자동으로 기획해주는 멀티 에이전트 시스템. 시장조사부터 최종 기획서까지 5개의 전문 AI가 협업합니다.',
            'tech_stack': ['Python', 'LangGraph', 'Groq API', 'React'],
            'features': [
                '실시간 시장 트렌드 분석',
                '경쟁사 자동 분석',
                '3개의 아이디어 생성 및 평가',
                '완전한 기획서 자동 생성',
                '무료 도구 기반 (Groq)'
            ],
            'timeline': '2주'
        },
        {
            'title': '💻 개발자 생산성 대시보드',
            'description': 'GitHub, Jira, Slack을 통합하여 개발자의 생산성을 시각화하고 최적화하는 도구. AI가 업무 패턴을 분석하고 개선점을 제안합니다.',
            'tech_stack': ['Next.js', 'FastAPI', 'PostgreSQL', 'OpenAI'],
            'features': [
                'GitHub 커밋 분석',
                '작업 시간 패턴 인사이트',
                'AI 기반 생산성 팁',
                '팀 협업 지표',
                '개인 맞춤 리포트'
            ],
            'timeline': '3주'
        },
        {
            'title': '🚀 No-Code AI 챗봇 빌더',
            'description': '코딩 없이 드래그 앤 드롭으로 커스텀 AI 챗봇을 만들 수 있는 플랫폼. LangGraph 기반으로 복잡한 대화 흐름도 쉽게 구현합니다.',
            'tech_stack': ['React Flow', 'LangGraph', 'Supabase', 'Tailwind'],
            'features': [
                '비주얼 워크플로우 에디터',
                '다양한 LLM 선택 (무료 포함)',
                '원클릭 배포',
                '실시간 테스트',
                '사용량 분석 대시보드'
            ],
            'timeline': '4주'
        }
    ]

    # HTML 생성
    team_cards = ""
    for member in team_members:
        skills_html = ' '.join([f'<span class="skill">{skill}</span>' for skill in member['skills']])
        team_cards += f"""
        <div class="team-card">
            <div class="member-avatar">{member['name'][0]}</div>
            <h3>{member['name']}</h3>
            <p class="role">{member['role']}</p>
            <p class="model">🤖 {member['model']}</p>
            <p class="description">{member['description']}</p>
            <div class="skills">{skills_html}</div>
        </div>
        """

    project_cards = ""
    for project in project_ideas:
        tech_html = ' '.join([f'<span class="tech">{tech}</span>' for tech in project['tech_stack']])
        features_html = ''.join([f'<li>{feature}</li>' for feature in project['features']])
        project_cards += f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p class="description">{project['description']}</p>
            <div class="tech-stack">{tech_html}</div>
            <ul class="features">{features_html}</ul>
            <div class="timeline">⏱️ 개발 기간: {project['timeline']}</div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 개발팀 포트폴리오</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #e2e8f0;
            line-height: 1.6;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}

        /* Hero Section */
        .hero {{
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
            border-radius: 20px;
            margin-bottom: 4rem;
            box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
            animation: fadeInDown 1s ease;
        }}

        @keyframes fadeInDown {{
            from {{
                opacity: 0;
                transform: translateY(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .hero h1 {{
            font-size: 3.5rem;
            margin-bottom: 1rem;
            color: white;
            font-weight: 800;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}

        .hero .tagline {{
            font-size: 1.5rem;
            color: rgba(255, 255, 255, 0.95);
            margin-bottom: 1rem;
            font-weight: 300;
        }}

        .hero .description {{
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.85);
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.8;
        }}

        /* Section Titles */
        h2 {{
            font-size: 2.5rem;
            margin-bottom: 3rem;
            text-align: center;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
        }}

        section {{
            margin-bottom: 5rem;
        }}

        /* Team Cards */
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }}

        .team-card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            opacity: 0;
            animation: fadeInUp 0.6s ease forwards;
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .team-card:nth-child(1) {{ animation-delay: 0.1s; }}
        .team-card:nth-child(2) {{ animation-delay: 0.2s; }}
        .team-card:nth-child(3) {{ animation-delay: 0.3s; }}
        .team-card:nth-child(4) {{ animation-delay: 0.4s; }}
        .team-card:nth-child(5) {{ animation-delay: 0.5s; }}

        .team-card:hover {{
            transform: translateY(-10px);
            border-color: #6366f1;
            box-shadow: 0 20px 40px rgba(99, 102, 241, 0.2);
        }}

        .member-avatar {{
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            color: white;
            margin: 0 auto 1rem;
        }}

        .team-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: #f59e0b;
        }}

        .role {{
            color: #6366f1;
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }}

        .model {{
            font-size: 0.9rem;
            color: #8b5cf6;
            margin-bottom: 1rem;
            font-weight: 500;
        }}

        .description {{
            margin-bottom: 1.5rem;
            color: #cbd5e1;
            line-height: 1.6;
        }}

        .skills {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .skill {{
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            color: white;
        }}

        /* Projects */
        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
        }}

        .project-card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            opacity: 0;
            animation: fadeInUp 0.6s ease forwards;
        }}

        .project-card:hover {{
            transform: translateY(-10px);
            border-color: #8b5cf6;
            box-shadow: 0 20px 40px rgba(139, 92, 246, 0.2);
        }}

        .project-card h3 {{
            font-size: 1.75rem;
            margin-bottom: 1rem;
            color: #8b5cf6;
        }}

        .tech-stack {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1.5rem 0;
        }}

        .tech {{
            background: rgba(139, 92, 246, 0.2);
            border: 1px solid #8b5cf6;
            padding: 0.4rem 0.8rem;
            border-radius: 15px;
            font-size: 0.85rem;
            color: #c4b5fd;
            font-weight: 500;
        }}

        .features {{
            list-style: none;
            margin: 1.5rem 0;
        }}

        .features li {{
            padding: 0.5rem 0;
            padding-left: 1.5rem;
            position: relative;
            color: #cbd5e1;
        }}

        .features li:before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: #10b981;
            font-weight: bold;
        }}

        .timeline {{
            color: #f59e0b;
            font-weight: 600;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }}

        /* Contact */
        .contact {{
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
            border-radius: 20px;
            border: 1px solid rgba(99, 102, 241, 0.2);
        }}

        .contact h2 {{
            margin-bottom: 1.5rem;
        }}

        .contact p {{
            font-size: 1.2rem;
            margin-bottom: 2rem;
            color: #cbd5e1;
            line-height: 1.8;
        }}

        .btn {{
            display: inline-block;
            padding: 1rem 2.5rem;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
        }}

        .btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(99, 102, 241, 0.4);
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2.5rem;
            }}

            .hero .tagline {{
                font-size: 1.2rem;
            }}

            h2 {{
                font-size: 2rem;
            }}

            .team-grid, .projects-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 2rem;
            color: #64748b;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Hero Section -->
        <div class="hero">
            <h1>🤖 AI 개발팀</h1>
            <p class="tagline">LangGraph 멀티 에이전트 협업 시스템</p>
            <p class="description">
                서로 다른 AI 모델을 가진 5명의 전문가가 협업하여<br>
                당신의 아이디어를 완전한 웹 서비스로 만들어드립니다
            </p>
        </div>

        <!-- Team Section -->
        <section id="team">
            <h2>👥 Our Team</h2>
            <div class="team-grid">
                {team_cards}
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects">
            <h2>🚀 What We Build</h2>
            <div class="projects-grid">
                {project_cards}
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="contact">
            <h2>📬 Work With Us</h2>
            <p>
                무료 AI 도구 (Groq API)를 활용하여<br>
                빠르고 혁신적인 웹 서비스를 함께 만들어갑니다
            </p>
            <a href="#" class="btn">프로젝트 시작하기 →</a>
        </section>
    </div>

    <footer>
        <p>Powered by LangGraph × Groq API × Multiple AI Agents</p>
        <p>🤖 PM: Llama 3.3 | 🎨 Designer: Llama 3.3 | 💻 Frontend: Llama 3.3 | ⚙️ Backend: Mixtral | 🔍 Research: DuckDuckGo</p>
    </footer>
</body>
</html>"""

    # 파일 저장
    with open('team_portfolio.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("✅ 팀 포트폴리오 페이지 생성 완료!\n")
    print("=" * 60)
    print(f"📄 파일: team_portfolio.html")
    print(f"👥 팀원: {len(team_members)}명")
    print(f"🚀 프로젝트: {len(project_ideas)}개")
    print("=" * 60)
    print("\n💡 브라우저에서 열어보기:")
    print("   open team_portfolio.html\n")

    return html


if __name__ == "__main__":
    create_demo_page()
