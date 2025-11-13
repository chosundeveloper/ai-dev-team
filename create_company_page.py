"""
AI 회사 소개 페이지 생성
"""

def create_company_page():
    """AI 기술 회사 소개 페이지 생성"""

    # 회사 정보
    company = {
        'name': 'NeuroFlow AI',
        'tagline': 'Intelligent Solutions, Limitless Possibilities',
        'description': '차세대 AI 기술로 비즈니스의 미래를 만들어갑니다',
        'founded': '2024',
        'mission': 'AI 기술의 민주화를 통해 모든 비즈니스가 혁신할 수 있도록 돕습니다',
        'values': [
            '혁신 (Innovation)',
            '투명성 (Transparency)',
            '협업 (Collaboration)',
            '지속가능성 (Sustainability)'
        ]
    }

    # 팀 (AI 에이전트들)
    team = [
        {
            'name': 'Alex Chen',
            'role': 'CEO & AI Strategist',
            'bio': '15년 경력의 AI 전략가. MIT AI Lab 출신',
            'specialty': 'AI 전략, 비즈니스 모델'
        },
        {
            'name': 'Maya Rodriguez',
            'role': 'Chief Design Officer',
            'bio': '사용자 중심 AI 인터페이스 디자인 전문가',
            'specialty': 'UX/UI, 인간-AI 상호작용'
        },
        {
            'name': 'Chris Park',
            'role': 'Head of Engineering',
            'bio': '대규모 AI 시스템 구축 경험 10년+',
            'specialty': 'MLOps, 시스템 아키텍처'
        },
        {
            'name': 'Jordan Lee',
            'role': 'Lead ML Engineer',
            'bio': 'LLM 파인튜닝 및 최적화 전문가',
            'specialty': 'LLM, 멀티 에이전트 시스템'
        },
        {
            'name': 'Sam Taylor',
            'role': 'Research Scientist',
            'bio': '최신 AI 연구를 제품화하는 브릿지 역할',
            'specialty': 'AI 연구, 논문 구현'
        }
    ]

    # 서비스/제품
    services = [
        {
            'icon': '🤖',
            'title': 'AI Agent Platform',
            'description': '멀티 에이전트 시스템으로 복잡한 업무를 자동화합니다',
            'features': ['LangGraph 기반', '무제한 확장', '실시간 협업']
        },
        {
            'icon': '🧠',
            'title': 'Custom LLM Solutions',
            'description': '비즈니스에 최적화된 맞춤형 AI 모델을 제공합니다',
            'features': ['파인튜닝', 'RAG 시스템', '프라이빗 배포']
        },
        {
            'icon': '📊',
            'title': 'AI Analytics',
            'description': 'AI 기반 데이터 분석으로 인사이트를 발견합니다',
            'features': ['실시간 분석', '자동 리포트', '예측 모델']
        },
        {
            'icon': '🚀',
            'title': 'AI Consulting',
            'description': 'AI 전략 수립부터 구현까지 전문가가 함께합니다',
            'features': ['전략 컨설팅', 'POC 개발', '팀 교육']
        }
    ]

    # 고객사/실적
    achievements = [
        {'number': '50+', 'label': '완료 프로젝트'},
        {'number': '30+', 'label': '파트너 기업'},
        {'number': '99.9%', 'label': '고객 만족도'},
        {'number': '5M+', 'label': '처리 요청 수'}
    ]

    # HTML 생성
    team_html = ""
    for member in team:
        team_html += f"""
        <div class="team-member">
            <div class="avatar">{member['name'][0]}</div>
            <h3>{member['name']}</h3>
            <p class="role">{member['role']}</p>
            <p class="bio">{member['bio']}</p>
            <p class="specialty"><strong>전문분야:</strong> {member['specialty']}</p>
        </div>
        """

    services_html = ""
    for service in services:
        features = ' '.join([f'<li>{f}</li>' for f in service['features']])
        services_html += f"""
        <div class="service-card">
            <div class="service-icon">{service['icon']}</div>
            <h3>{service['title']}</h3>
            <p>{service['description']}</p>
            <ul class="features">{features}</ul>
        </div>
        """

    achievements_html = ""
    for achievement in achievements:
        achievements_html += f"""
        <div class="achievement">
            <div class="number">{achievement['number']}</div>
            <div class="label">{achievement['label']}</div>
        </div>
        """

    values_html = ' '.join([f'<span class="value">{v}</span>' for v in company['values']])

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{company['name']} - AI Technology Company</title>
    <meta name="description" content="{company['description']}">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --accent: #f59e0b;
            --dark: #0f172a;
            --dark-light: #1e293b;
            --text: #e2e8f0;
            --text-dim: #cbd5e1;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--dark);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}

        /* Header */
        header {{
            background: linear-gradient(135deg, var(--primary), var(--secondary), #ec4899);
            padding: 6rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}

        header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120"><path fill="%23ffffff" fill-opacity="0.1" d="M0,0 Q300,40 600,20 T1200,0 V120 H0 Z"/></svg>');
            background-size: cover;
            opacity: 0.3;
        }}

        header .content {{
            position: relative;
            z-index: 1;
        }}

        .logo {{
            font-size: 3rem;
            font-weight: 900;
            margin-bottom: 1rem;
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }}

        .tagline {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 300;
            opacity: 0.95;
        }}

        .description {{
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 2rem;
            opacity: 0.9;
        }}

        .cta-button {{
            display: inline-block;
            padding: 1rem 2.5rem;
            background: white;
            color: var(--primary);
            text-decoration: none;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}

        .cta-button:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }}

        /* Sections */
        section {{
            padding: 5rem 2rem;
        }}

        h2 {{
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
        }}

        /* Mission */
        .mission-box {{
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 3rem;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }}

        .mission-box p {{
            font-size: 1.3rem;
            line-height: 1.8;
            color: var(--text-dim);
        }}

        .values {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 2rem;
        }}

        .value {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            padding: 0.75rem 1.5rem;
            border-radius: 25px;
            font-weight: 600;
        }}

        /* Services */
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }}

        .service-card {{
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s;
        }}

        .service-card:hover {{
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 40px rgba(99,102,241,0.2);
        }}

        .service-icon {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}

        .service-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--accent);
        }}

        .service-card .features {{
            list-style: none;
            margin-top: 1rem;
        }}

        .service-card .features li {{
            padding: 0.5rem 0;
            padding-left: 1.5rem;
            position: relative;
            color: var(--text-dim);
        }}

        .service-card .features li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: #10b981;
            font-weight: bold;
        }}

        /* Team */
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }}

        .team-member {{
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
            transition: all 0.3s;
        }}

        .team-member:hover {{
            transform: translateY(-10px);
            border-color: var(--secondary);
        }}

        .avatar {{
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: bold;
            margin: 0 auto 1rem;
        }}

        .team-member h3 {{
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
        }}

        .team-member .role {{
            color: var(--primary);
            font-weight: 600;
            margin-bottom: 1rem;
        }}

        .team-member .bio {{
            font-size: 0.95rem;
            color: var(--text-dim);
            margin-bottom: 1rem;
        }}

        .team-member .specialty {{
            font-size: 0.9rem;
            color: var(--accent);
        }}

        /* Achievements */
        .achievements {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }}

        .achievement {{
            text-align: center;
            padding: 2rem;
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
        }}

        .achievement .number {{
            font-size: 3rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .achievement .label {{
            font-size: 1.1rem;
            color: var(--text-dim);
            margin-top: 0.5rem;
        }}

        /* Contact */
        .contact {{
            background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.1));
            padding: 4rem 2rem;
            border-radius: 20px;
            text-align: center;
            border: 1px solid rgba(99,102,241,0.2);
        }}

        .contact h2 {{
            margin-bottom: 1.5rem;
        }}

        .contact p {{
            font-size: 1.2rem;
            margin-bottom: 2rem;
            color: var(--text-dim);
        }}

        .contact-info {{
            display: flex;
            justify-content: center;
            gap: 3rem;
            flex-wrap: wrap;
            margin-top: 2rem;
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1.1rem;
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 3rem 2rem;
            color: var(--text-dim);
            border-top: 1px solid rgba(255,255,255,0.1);
        }}

        footer p {{
            margin: 0.5rem 0;
        }}

        .tech-stack {{
            margin-top: 1rem;
            font-size: 0.9rem;
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .logo {{
                font-size: 2rem;
            }}

            .tagline {{
                font-size: 1.2rem;
            }}

            h2 {{
                font-size: 2rem;
            }}

            .services-grid,
            .team-grid,
            .achievements {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="content">
            <div class="logo">{company['name']}</div>
            <p class="tagline">{company['tagline']}</p>
            <p class="description">{company['description']}</p>
            <a href="#contact" class="cta-button">문의하기 →</a>
        </div>
    </header>

    <!-- Mission -->
    <section>
        <div class="container">
            <h2>Our Mission</h2>
            <div class="mission-box">
                <p>{company['mission']}</p>
                <div class="values">
                    {values_html}
                </div>
            </div>
        </div>
    </section>

    <!-- Services -->
    <section style="background: var(--dark-light);">
        <div class="container">
            <h2>Our Services</h2>
            <div class="services-grid">
                {services_html}
            </div>
        </div>
    </section>

    <!-- Team -->
    <section>
        <div class="container">
            <h2>Our Team</h2>
            <div class="team-grid">
                {team_html}
            </div>
        </div>
    </section>

    <!-- Achievements -->
    <section style="background: var(--dark-light);">
        <div class="container">
            <h2>Our Impact</h2>
            <div class="achievements">
                {achievements_html}
            </div>
        </div>
    </section>

    <!-- Contact -->
    <section>
        <div class="container contact">
            <h2 id="contact">Contact Us</h2>
            <p>AI 기술로 비즈니스를 혁신하고 싶으신가요?<br>언제든 문의해주세요.</p>
            <div class="contact-info">
                <div class="contact-item">
                    📧 <a href="mailto:contact@neuroflow.ai" style="color: var(--primary); text-decoration: none;">contact@neuroflow.ai</a>
                </div>
                <div class="contact-item">
                    🌐 <a href="https://github.com/chosundeveloper/ai-dev-team" style="color: var(--primary); text-decoration: none;" target="_blank">GitHub</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p><strong>{company['name']}</strong> © {company['founded']}- 2025. All Rights Reserved.</p>
        <p>Powered by LangGraph × Groq × AI Multi-Agent Systems</p>
        <p class="tech-stack">🤖 AI-First Company | Built with AI Technology</p>
    </footer>

    <script>
        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }});
        }});

        // Intersection Observer for animations
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }}
            }});
        }}, {{ threshold: 0.1 }});

        document.querySelectorAll('.service-card, .team-member, .achievement').forEach(el => {{
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        }});
    </script>
</body>
</html>"""

    # index.html로 저장 (GitHub Pages 메인 페이지)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ {company['name']} 회사 소개 페이지 생성 완료!")
    print(f"📄 파일: index.html")
    print(f"👥 팀원: {len(team)}명")
    print(f"🚀 서비스: {len(services)}개")

    return html

if __name__ == "__main__":
    create_company_page()
