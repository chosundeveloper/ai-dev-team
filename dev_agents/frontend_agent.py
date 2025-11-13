"""
Frontend 에이전트: HTML/CSS/JS 코드 작성
"""
from dev_team_state import DevTeamState
from langchain_core.messages import SystemMessage, HumanMessage
import json


def frontend_agent(state: DevTeamState, llm) -> DevTeamState:
    """Frontend 개발자가 실제 코드를 작성"""
    print("💻 [Frontend] HTML/CSS/JS 코드 작성 중...")

    system_prompt = """당신은 Frontend 개발자 Chris입니다.

    역할:
    - 모던한 HTML5/CSS3/JavaScript 코드 작성
    - 반응형 디자인 구현
    - 애니메이션 및 인터랙션 추가

    기술 스택:
    - 순수 HTML/CSS/JS (프레임워크 없이)
    - Tailwind CSS 스타일의 유틸리티 클래스
    - 부드러운 스크롤 애니메이션
    - 다크모드 기본 적용
    """

    # 팀 정보 포맷팅
    team_html = ""
    for member in state['team_members']:
        team_html += f"""
        <div class="team-member">
            <h3>{member['name']}</h3>
            <p class="role">{member['role']}</p>
            <p class="model">{member['model']}</p>
            <p>{member['description']}</p>
            <div class="skills">
                {' '.join([f'<span>{skill}</span>' for skill in member['skills']])}
            </div>
        </div>
        """

    projects_html = ""
    for project in state['project_ideas']:
        tech_stack = ' '.join([f'<span>{tech}</span>' for tech in project['tech_stack']])
        features_list = ''.join([f'<li>{feature}</li>' for feature in project['features']])
        projects_html += f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p>{project['description']}</p>
            <div class="tech-stack">{tech_stack}</div>
            <ul class="features">{features_list}</ul>
            <p class="timeline">⏱️ {project['timeline']}</p>
        </div>
        """

    colors = state['color_scheme']

    user_message = f"""
    다음 정보로 완전한 웹페이지를 만들어주세요:

    팀 비전: {state['team_vision']}
    팀 강점: {state['team_strengths']}
    색상: {json.dumps(colors)}

    완전한 HTML 파일을 작성해주세요 (CSS, JS 포함).

    구조:
    1. Hero 섹션: 팀 이름, 비전
    2. Team 섹션: {len(state['team_members'])}명 소개
    3. Projects 섹션: {len(state['project_ideas'])}개 프로젝트
    4. Contact 섹션

    요구사항:
    - 반응형 디자인 (모바일 최적화)
    - 스크롤 애니메이션
    - 호버 효과
    - 다크 테마
    - 아름다운 그라데이션

    완전한 HTML 코드만 제공해주세요 (<!DOCTYPE html>부터).
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]

    response = llm.invoke(messages)

    # HTML 코드 추출
    html_code = response.content

    # 코드 블록에서 추출
    if "```html" in html_code:
        html_code = html_code.split("```html")[1].split("```")[0]
    elif "```" in html_code:
        html_code = html_code.split("```")[1].split("```")[0]

    # 팀 정보와 프로젝트 정보를 삽입
    # 기본 HTML이 없으면 템플릿 사용
    if not html_code.strip().startswith("<!DOCTYPE") and not html_code.strip().startswith("<html"):
        html_code = create_default_template(state)

    state['html_code'] = html_code
    state['final_page'] = html_code

    print(f"✅ 코드 작성 완료: {len(html_code)} 문자")
    return state


def create_default_template(state: DevTeamState) -> str:
    """기본 HTML 템플릿"""
    colors = state['color_scheme']

    team_cards = ""
    for member in state['team_members']:
        skills = ' '.join([f'<span class="skill">{skill}</span>' for skill in member['skills']])
        team_cards += f"""
        <div class="team-card">
            <h3>{member['name']}</h3>
            <p class="role">{member['role']}</p>
            <p class="model">🤖 {member['model']}</p>
            <p class="description">{member['description']}</p>
            <div class="skills">{skills}</div>
        </div>
        """

    project_cards = ""
    for project in state['project_ideas']:
        tech = ' '.join([f'<span class="tech">{t}</span>' for t in project['tech_stack']])
        features = ''.join([f'<li>{f}</li>' for f in project['features']])
        project_cards += f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p class="description">{project['description']}</p>
            <div class="tech-stack">{tech}</div>
            <ul class="features">{features}</ul>
            <p class="timeline">⏱️ 개발 기간: {project['timeline']}</p>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 개발팀 소개</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: {colors['background']};
            color: {colors['text']};
            line-height: 1.6;
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
            background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
            border-radius: 20px;
            margin-bottom: 4rem;
        }}

        .hero h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
            color: white;
        }}

        .hero p {{
            font-size: 1.25rem;
            color: rgba(255, 255, 255, 0.9);
            max-width: 600px;
            margin: 0 auto;
        }}

        /* Section */
        section {{
            margin-bottom: 4rem;
        }}

        h2 {{
            font-size: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
            color: {colors['primary']};
        }}

        /* Team Cards */
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }}

        .team-card {{
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease;
        }}

        .team-card:hover {{
            transform: translateY(-10px);
            border-color: {colors['primary']};
        }}

        .team-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: {colors['accent']};
        }}

        .role {{
            color: {colors['primary']};
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}

        .model {{
            font-size: 0.9rem;
            opacity: 0.7;
            margin-bottom: 1rem;
        }}

        .description {{
            margin-bottom: 1rem;
        }}

        .skills {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .skill {{
            background: {colors['primary']};
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
        }}

        /* Project Cards */
        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
        }}

        .project-card {{
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}

        .project-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: {colors['secondary']};
        }}

        .tech-stack {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1rem 0;
        }}

        .tech {{
            background: {colors['secondary']};
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.85rem;
        }}

        .features {{
            list-style-position: inside;
            margin: 1rem 0;
        }}

        .timeline {{
            color: {colors['accent']};
            font-weight: bold;
            margin-top: 1rem;
        }}

        /* Contact */
        .contact {{
            text-align: center;
            padding: 3rem;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
            border-radius: 15px;
        }}

        .contact h2 {{
            margin-bottom: 1rem;
        }}

        .contact p {{
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }}

        .btn {{
            display: inline-block;
            padding: 1rem 2rem;
            background: {colors['primary']};
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            transition: background 0.3s ease;
        }}

        .btn:hover {{
            background: {colors['secondary']};
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}

            h2 {{
                font-size: 1.75rem;
            }}

            .team-grid, .projects-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Hero Section -->
        <div class="hero">
            <h1>🤖 AI 개발팀</h1>
            <p>{state['team_vision']}</p>
            <p style="margin-top: 1rem; font-size: 1rem;">💪 {state['team_strengths']}</p>
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
            <p>LangGraph 기반 멀티 에이전트 시스템으로<br>당신의 아이디어를 현실로 만들어드립니다</p>
            <a href="#" class="btn">프로젝트 시작하기</a>
        </section>
    </div>

    <script>
        // 스크롤 애니메이션
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }}
            }});
        }});

        document.querySelectorAll('.team-card, .project-card').forEach(el => {{
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            observer.observe(el);
        }});
    </script>
</body>
</html>"""
