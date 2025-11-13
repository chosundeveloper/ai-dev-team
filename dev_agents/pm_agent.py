"""
PM 에이전트: 팀 구성 및 비전 수립
"""
from dev_team_state import DevTeamState, TeamMember, ProjectIdea
from langchain_core.messages import SystemMessage, HumanMessage


def pm_agent(state: DevTeamState, llm) -> DevTeamState:
    """PM이 팀을 구성하고 비전을 수립"""
    print("👔 [PM] 팀 구성 및 비전 수립 중...")

    system_prompt = """당신은 AI 개발팀을 이끄는 Product Manager입니다.

    역할:
    - 팀원 구성 및 역할 정의
    - 팀의 강점과 비전 수립
    - 만들 수 있는 프로젝트 아이디어 제시

    당신의 팀은 LangGraph 기반 멀티 에이전트 시스템으로:
    - 각 팀원은 서로 다른 AI 모델을 사용하는 전문가
    - 협업을 통해 완전한 웹사이트를 개발
    - 무료 도구만 사용 (Groq API)
    """

    user_message = """
    우리 AI 개발팀을 소개하는 내용을 만들어주세요.

    팀 구성:
    1. PM (당신) - Llama 3.3 70B
    2. UI/UX Designer - Llama 3.3 70B
    3. Frontend Developer - Llama 3.3 70B
    4. Backend Developer - Mixtral 8x7b
    5. Market Researcher - DuckDuckGo + Llama 3.3

    다음을 JSON 형식으로 작성:
    {
      "team_vision": "우리 팀의 비전과 목표",
      "team_strengths": "우리 팀만의 강점 3가지",
      "project_ideas": [
        {
          "title": "프로젝트 제목",
          "description": "설명",
          "tech_stack": ["React", "Node.js", ...],
          "features": ["기능1", "기능2", ...],
          "timeline": "개발 기간"
        }
      ]
    }

    3개의 프로젝트 아이디어를 제시해주세요.
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]

    response = llm.invoke(messages)

    # JSON 파싱
    import json
    try:
        content = response.content
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]

        data = json.loads(content.strip())

        state['team_vision'] = data.get('team_vision', '혁신적인 웹 서비스 개발')
        state['team_strengths'] = data.get('team_strengths', '빠른 개발')
        state['project_ideas'] = data.get('project_ideas', [])

    except Exception as e:
        print(f"⚠️ JSON 파싱 실패: {e}")
        state['team_vision'] = "AI 기반 협업으로 혁신적인 웹 서비스를 빠르게 개발하는 팀"
        state['team_strengths'] = "멀티 에이전트 협업, 무료 도구 활용, 빠른 프로토타이핑"
        state['project_ideas'] = [
            {
                'title': 'AI 웹사이트 기획 도구',
                'description': '조회수 높은 웹사이트를 기획해주는 AI',
                'tech_stack': ['Python', 'LangGraph', 'React'],
                'features': ['시장조사', '경쟁분석', '아이디어 생성'],
                'timeline': '2주'
            }
        ]

    # 팀 멤버 정보 설정
    state['team_members'] = [
        {
            'name': 'Alex (PM)',
            'role': 'Product Manager',
            'model': 'Llama 3.3 70B',
            'skills': ['기획', '요구사항 분석', '프로젝트 관리'],
            'description': '팀을 이끄는 전략가'
        },
        {
            'name': 'Maya (Designer)',
            'role': 'UI/UX Designer',
            'model': 'Llama 3.3 70B',
            'skills': ['디자인', '사용자 경험', '프로토타이핑'],
            'description': '아름다운 인터페이스 창조자'
        },
        {
            'name': 'Chris (Frontend)',
            'role': 'Frontend Developer',
            'model': 'Llama 3.3 70B',
            'skills': ['React', 'JavaScript', 'HTML/CSS'],
            'description': '사용자가 보는 모든 것을 구현'
        },
        {
            'name': 'Jordan (Backend)',
            'role': 'Backend Developer',
            'model': 'Mixtral 8x7b',
            'skills': ['Python', 'API 설계', '데이터베이스'],
            'description': '탄탄한 서버 로직 구축'
        },
        {
            'name': 'Sam (Researcher)',
            'role': 'Market Researcher',
            'model': 'DuckDuckGo + Llama 3.3',
            'skills': ['시장조사', '트렌드 분석', '경쟁분석'],
            'description': '실시간 시장 인사이트 제공'
        }
    ]

    print(f"✅ 팀 구성 완료: {len(state['team_members'])}명")
    print(f"✅ 프로젝트 아이디어: {len(state['project_ideas'])}개")
    return state
