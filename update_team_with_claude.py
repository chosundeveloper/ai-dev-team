"""
팀 업데이트: Spark Labs + Claude 포함
"""

def create_spark_labs_page():
    """Spark Labs 팀 페이지 생성"""

    # 새로운 팀명
    team_name = "Spark Labs"
    team_tagline = "Igniting Viral Ideas"
    team_vision = "사용자가 열광하는 바이럴 제품을 만듭니다"
    team_mission = "AI 기술로 매일 수백만 명이 사용하는 서비스를 빠르게 구축하고 성장시킵니다"

    # 팀원 (Claude 포함!)
    team_members = [
        {
            'name': 'Alex',
            'role': 'Product Manager',
            'model': 'Llama 3.3 70B',
            'skills': ['전략 기획', '시장 분석', '바이럴 마케팅', 'Growth Hacking'],
            'description': '조회수 높은 제품을 기획하고 성장 전략을 수립하는 PM'
        },
        {
            'name': 'Claude',
            'role': 'AI Orchestrator & Developer',
            'model': 'Claude 3.5 Sonnet',
            'skills': ['풀스택 개발', 'AI 통합', '시스템 설계', '코드 작성'],
            'description': '전체 개발을 총괄하고 실제 코드를 작성하는 AI 개발자'
        },
        {
            'name': 'Maya',
            'role': 'UI/UX Designer',
            'model': 'Llama 3.3 70B',
            'skills': ['UI 디자인', '사용자 경험', '바이럴 UX', '프로토타이핑'],
            'description': '사용자가 다시 찾아오는 인터페이스를 만드는 디자이너'
        },
        {
            'name': 'Chris',
            'role': 'Frontend Developer',
            'model': 'Llama 3.3 70B',
            'skills': ['React', 'Next.js', '반응형 디자인', 'SEO'],
            'description': '빠르고 아름다운 프론트엔드를 구현하는 개발자'
        },
        {
            'name': 'Jordan',
            'role': 'Backend Developer',
            'model': 'Mixtral 8x7b',
            'skills': ['Python', 'FastAPI', 'PostgreSQL', '확장성'],
            'description': '수백만 사용자를 감당하는 백엔드를 구축하는 엔지니어'
        },
        {
            'name': 'Sam',
            'role': 'Growth Hacker',
            'model': 'DuckDuckGo + Llama 3.3',
            'skills': ['트렌드 분석', 'SEO', '바이럴 마케팅', '데이터 분석'],
            'description': '실시간 트렌드를 포착하고 사용자를 끌어오는 마케터'
        }
    ]

    # 실제 바이럴 프로젝트
    viral_projects = [
        {
            'title': '🗞️ Dev Daily - 개발자 일일 뉴스레터',
            'description': 'AI가 매일 아침 GitHub, Hacker News, Reddit을 분석해서 개발자에게 꼭 필요한 뉴스만 3분 분량으로 큐레이션합니다.',
            'viral_score': 9,
            'target_users': '50만+ 개발자',
            'tech_stack': ['Python', 'FastAPI', 'React', 'DuckDuckGo', 'Email API'],
            'features': [
                '매일 아침 7시 자동 발송',
                'AI 기반 중요도 순위',
                '카테고리별 필터 (Frontend, Backend, AI)',
                '읽는 시간 3분 이내',
                '아카이브 검색',
                '모바일 최적화'
            ],
            'monetization': '무료 + 프리미엄 $5/월',
            'timeline': '2주',
            'growth_strategy': 'Reddit, Hacker News, ProductHunt 런칭'
        },
        {
            'title': '💻 Code Vault - 코드 스니펫 마켓플레이스',
            'description': '개발자들이 자주 쓰는 코드 스니펫을 저장하고 공유하는 플랫폼. AI가 자동으로 태깅하고 검색을 도와드립니다.',
            'viral_score': 10,
            'target_users': '100만+ 개발자',
            'tech_stack': ['Next.js', 'Supabase', 'Tailwind', 'AI Tagging'],
            'features': [
                '원클릭 코드 복사',
                'AI 자동 태깅',
                '언어별/프레임워크별 필터',
                'GitHub Gist 연동',
                '실시간 코드 실행',
                '다크/라이트 테마'
            ],
            'monetization': '무료 + 프리미엄 $3/월',
            'timeline': '3주',
            'growth_strategy': 'GitHub 트렌딩, Dev.to, Twitter'
        },
        {
            'title': '🎯 AI Interview Coach - AI 면접 준비',
            'description': '실제 기업 면접 데이터를 학습한 AI가 1:1 모의 면접을 진행하고 실시간 피드백을 제공합니다.',
            'viral_score': 10,
            'target_users': '200만+ 구직자',
            'tech_stack': ['React', 'FastAPI', 'Groq/OpenAI', 'Speech-to-Text'],
            'features': [
                '직무별 맞춤 질문',
                '음성/텍스트 면접',
                'AI 실시간 피드백',
                '답변 개선 제안',
                '기업별 면접 스타일',
                '진행도 트래킹'
            ],
            'monetization': '무료 3회 + $9.99/월',
            'timeline': '4주',
            'growth_strategy': '유튜브 광고, 대학 커뮤니티, SEO'
        }
    ]

    # HTML 생성
    team_html = ""
    for member in team_members:
        skills_html = ' '.join([f'<span class="skill">{s}</span>' for s in member['skills']])
        # Claude는 특별 표시
        special_class = ' claude-special' if member['name'] == 'Claude' else ''
        team_html += f"""
        <div class="team-card{special_class}">
            <div class="member-avatar">{member['name'][0]}</div>
            <h3>{member['name']}</h3>
            <p class="role">{member['role']}</p>
            <p class="model">🤖 {member['model']}</p>
            <p class="description">{member['description']}</p>
            <div class="skills">{skills_html}</div>
        </div>
        """

    projects_html = ""
    for project in viral_projects:
        tech_html = ' '.join([f'<span class="tech">{t}</span>' for t in project['tech_stack']])
        features_html = ''.join([f'<li>{f}</li>' for f in project['features']])
        projects_html += f"""
        <div class="project-card">
            <div class="project-header">
                <h3>{project['title']}</h3>
                <div class="viral-badge">🔥 바이럴 점수: {project['viral_score']}/10</div>
            </div>
            <p class="description">{project['description']}</p>
            <div class="project-stats">
                <span>🎯 타겟: {project['target_users']}</span>
                <span>⏱️ 개발: {project['timeline']}</span>
            </div>
            <div class="tech-stack">{tech_html}</div>
            <ul class="features">{features_html}</ul>
            <div class="growth">
                <strong>성장 전략:</strong> {project['growth_strategy']}
            </div>
            <div class="monetization">💰 {project['monetization']}</div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{team_name} - Viral Product Builders</title>
    <meta name="description" content="{team_mission}">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #e2e8f0;
            line-height: 1.6;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}

        /* Hero */
        .hero {{
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, #f59e0b, #ea580c, #dc2626);
            border-radius: 20px;
            margin-bottom: 4rem;
            box-shadow: 0 20px 60px rgba(245, 158, 11, 0.3);
            position: relative;
            overflow: hidden;
        }}

        .hero::before {{
            content: '🔥';
            position: absolute;
            font-size: 15rem;
            opacity: 0.1;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }}

        .hero .content {{
            position: relative;
            z-index: 1;
        }}

        .hero h1 {{
            font-size: 3.5rem;
            margin-bottom: 1rem;
            color: white;
            font-weight: 900;
        }}

        .hero .tagline {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: rgba(255,255,255,0.95);
        }}

        .hero .mission {{
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto;
            color: rgba(255,255,255,0.9);
        }}

        /* Sections */
        section {{
            margin-bottom: 5rem;
        }}

        h2 {{
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(135deg, #f59e0b, #dc2626);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
        }}

        /* Team */
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }}

        .team-card {{
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s;
        }}

        .team-card:hover {{
            transform: translateY(-10px);
            border-color: #f59e0b;
            box-shadow: 0 20px 40px rgba(245,158,11,0.2);
        }}

        /* Claude 특별 표시 */
        .claude-special {{
            border: 2px solid #8b5cf6;
            background: linear-gradient(135deg, rgba(139,92,246,0.1), rgba(99,102,241,0.1));
        }}

        .claude-special::before {{
            content: '⭐ Chief Developer';
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.75rem;
            font-weight: 600;
        }}

        .claude-special:hover {{
            border-color: #8b5cf6;
            box-shadow: 0 20px 40px rgba(139,92,246,0.3);
        }}

        .member-avatar {{
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, #f59e0b, #dc2626);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: bold;
            margin: 0 auto 1rem;
            color: white;
        }}

        .claude-special .member-avatar {{
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
        }}

        .team-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: #f59e0b;
        }}

        .claude-special h3 {{
            color: #8b5cf6;
        }}

        .role {{
            color: #f59e0b;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}

        .model {{
            font-size: 0.9rem;
            color: #cbd5e1;
            margin-bottom: 1rem;
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
            background: linear-gradient(135deg, #f59e0b, #dc2626);
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
        }}

        .claude-special .skill {{
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
        }}

        /* Projects */
        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 2rem;
        }}

        .project-card {{
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
        }}

        .project-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 1rem;
            gap: 1rem;
        }}

        .project-card h3 {{
            font-size: 1.5rem;
            color: #f59e0b;
            flex: 1;
        }}

        .viral-badge {{
            background: linear-gradient(135deg, #dc2626, #f59e0b);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            white-space: nowrap;
        }}

        .project-stats {{
            display: flex;
            gap: 1.5rem;
            margin: 1rem 0;
            font-size: 0.95rem;
            color: #cbd5e1;
        }}

        .tech-stack {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1.5rem 0;
        }}

        .tech {{
            background: rgba(245,158,11,0.2);
            border: 1px solid #f59e0b;
            padding: 0.4rem 0.8rem;
            border-radius: 15px;
            font-size: 0.85rem;
            color: #fbbf24;
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

        .features li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: #10b981;
            font-weight: bold;
        }}

        .growth {{
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            font-size: 0.95rem;
            color: #cbd5e1;
        }}

        .monetization {{
            margin-top: 1rem;
            color: #10b981;
            font-weight: 600;
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 3rem 2rem;
            color: #64748b;
            border-top: 1px solid rgba(255,255,255,0.1);
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2.5rem;
            }}
            h2 {{
                font-size: 2rem;
            }}
            .team-grid,
            .projects-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Hero -->
        <div class="hero">
            <div class="content">
                <h1>🔥 {team_name}</h1>
                <p class="tagline">{team_tagline}</p>
                <p class="mission">{team_mission}</p>
            </div>
        </div>

        <!-- Team -->
        <section>
            <h2>👥 Our Team</h2>
            <div class="team-grid">
                {team_html}
            </div>
        </section>

        <!-- Projects -->
        <section>
            <h2>🚀 Viral Projects We Build</h2>
            <div class="projects-grid">
                {projects_html}
            </div>
        </section>

        <!-- CTA -->
        <section style="text-align: center; background: linear-gradient(135deg, rgba(245,158,11,0.1), rgba(220,38,38,0.1)); padding: 4rem 2rem; border-radius: 20px;">
            <h2>Ready to Go Viral?</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem; color: #cbd5e1;">
                바이럴 제품을 2-4주 안에 빠르게 만들어드립니다
            </p>
            <a href="https://github.com/chosundeveloper/ai-dev-team"
               style="display: inline-block; padding: 1rem 2.5rem; background: linear-gradient(135deg, #f59e0b, #dc2626); color: white; text-decoration: none; border-radius: 50px; font-weight: 600; font-size: 1.1rem;">
                GitHub 보기 →
            </a>
        </section>
    </div>

    <footer>
        <p><strong>{team_name}</strong> - Building Products That Go Viral</p>
        <p>Powered by LangGraph × Groq × Claude × Multi-Agent AI</p>
    </footer>
</body>
</html>"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\n✅ {team_name} 팀 페이지 생성 완료!")
    print(f"👥 팀원: {len(team_members)}명 (Claude 포함!)")
    print(f"🚀 프로젝트: {len(viral_projects)}개")
    print(f"📄 파일: index.html\n")

if __name__ == "__main__":
    create_spark_labs_page()
