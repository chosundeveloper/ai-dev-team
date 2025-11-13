"""
조회수 높은 프로젝트 기획 (간단 버전)
"""

def plan_viral_project():
    """조회수/사용자가 많은 프로젝트 아이디어"""

    # PM Alex의 기획
    projects = [
        {
            'title': '개발자 일일 뉴스레터',
            'tagline': 'AI가 매일 아침 큐레이션하는 개발 뉴스',
            'description': '매일 아침 7시, AI가 GitHub 트렌딩, Hacker News, Reddit을 분석해서 개발자에게 꼭 필요한 뉴스만 3분 분량으로 정리해서 보내드립니다.',
            'target_users': '개발자, IT 종사자',
            'viral_potential': 9,
            'why_viral': '개발자는 매일 정보를 찾지만 시간이 없음. 큐레이션된 뉴스는 공유하기 쉬움',
            'tech_stack': ['Python', 'FastAPI', 'React', 'DuckDuckGo API', 'Email API'],
            'features': [
                '매일 아침 7시 자동 발송',
                'AI 기반 중요도 순위',
                '카테고리별 필터 (Frontend, Backend, AI, DevOps)',
                '읽는 시간 3분 이내',
                '아카이브 검색 기능',
                '좋아요/공유 기능'
            ],
            'monetization': '프리미엄 구독 ($5/월), 스폰서 광고',
            'timeline': '2주',
            'user_acquisition': [
                'Reddit r/programming 홍보',
                'Hacker News 제출',
                '개발자 커뮤니티 공유',
                'ProductHunt 런칭'
            ]
        },
        {
            'title': '코드 스니펫 마켓플레이스',
            'tagline': '개발자들이 만들고 공유하는 코드 조각',
            'description': '자주 쓰는 코드를 스니펫으로 저장하고, 다른 개발자와 공유하세요. AI가 자동으로 태그를 달고 검색을 도와드립니다.',
            'target_users': '모든 개발자',
            'viral_potential': 10,
            'why_viral': '개발자는 항상 코드를 재사용. 좋은 스니펫은 즉시 공유됨. 네트워크 효과 강함',
            'tech_stack': ['Next.js', 'Supabase', 'Tailwind', 'AI Tagging'],
            'features': [
                '코드 스니펫 저장/검색',
                'AI 자동 태깅',
                '언어별/프레임워크별 필터',
                '좋아요/북마크',
                'GitHub Gist 연동',
                '실시간 코드 실행 (preview)',
                '다크/라이트 테마',
                '복사 원클릭'
            ],
            'monetization': '프리미엄 기능 ($3/월), 팀 플랜 ($10/월)',
            'timeline': '3주',
            'user_acquisition': [
                'GitHub 트렌딩 활용',
                '개발자 유튜버 협업',
                'Dev.to 콘텐츠 마케팅',
                'Twitter 개발자 커뮤니티'
            ]
        },
        {
            'title': 'AI 면접 준비 플랫폼',
            'tagline': 'AI가 실제 면접처럼 질문하고 피드백',
            'description': '실제 기업의 면접 데이터를 학습한 AI가 1:1 모의 면접을 진행합니다. 답변을 분석하고 개선점을 알려드립니다.',
            'target_users': '구직자, 이직 준비생',
            'viral_potential': 10,
            'why_viral': '누구나 면접 준비 필요. 실제 효과 있으면 입소문 빠름. SNS 공유 유도 쉬움',
            'tech_stack': ['React', 'FastAPI', 'OpenAI/Groq', 'Speech-to-Text'],
            'features': [
                '직무별 맞춤 질문 (개발자, PM, 디자이너)',
                '음성 면접 or 텍스트',
                'AI 실시간 피드백',
                '답변 개선 제안',
                '면접 영상 녹화/분석',
                '모범 답안 제공',
                '진행도 트래킹',
                '기업별 면접 스타일 (네이버, 카카오 등)'
            ],
            'monetization': '무료 3회, 이후 $9.99/월 구독',
            'timeline': '4주',
            'user_acquisition': [
                '유튜브 "면접 준비" 검색 광고',
                '대학 취업 커뮤니티',
                '블로그 SEO (면접 준비 키워드)',
                '성공 후기 바이럴'
            ]
        }
    ]

    # 팀명 후보
    team_names = [
        {
            'name': 'Viral Builders',
            'tagline': 'Building Products People Love',
            'reason': '바이럴한 제품을 만드는 팀'
        },
        {
            'name': 'Growth Hackers',
            'tagline': 'From Zero to Million Users',
            'reason': '성장 전문 팀'
        },
        {
            'name': 'Launch Squad',
            'tagline': 'Ship Fast, Grow Faster',
            'reason': '빠르게 만들고 빠르게 성장'
        },
        {
            'name': 'Spark Labs',
            'tagline': 'Igniting Viral Ideas',
            'reason': '바이럴 아이디어를 불붙이는 팀'
        },
        {
            'name': 'Wave Makers',
            'tagline': 'Creating Digital Waves',
            'reason': '디지털 파도를 만드는 팀'
        }
    ]

    return {
        'projects': projects,
        'team_names': team_names,
        'recommended_project': projects[0],  # 개발자 뉴스레터 (가장 빠르게 시작 가능)
        'recommended_team': team_names[3]    # Spark Labs (기억하기 쉽고 의미 명확)
    }

if __name__ == "__main__":
    result = plan_viral_project()

    print("\n" + "="*60)
    print("🎯 조회수 높은 프로젝트 기획")
    print("="*60)

    print("\n📋 추천 팀명:")
    team = result['recommended_team']
    print(f"   {team['name']} - {team['tagline']}")
    print(f"   이유: {team['reason']}")

    print("\n🚀 1순위 프로젝트:")
    project = result['recommended_project']
    print(f"   제목: {project['title']}")
    print(f"   설명: {project['description']}")
    print(f"   바이럴 점수: {project['viral_potential']}/10")
    print(f"   개발 기간: {project['timeline']}")

    print("\n💡 전체 프로젝트:")
    for i, p in enumerate(result['projects'], 1):
        print(f"   {i}. {p['title']} (바이럴: {p['viral_potential']}/10)")

    print("\n" + "="*60)
