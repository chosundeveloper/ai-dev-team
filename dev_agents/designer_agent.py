"""
Designer 에이전트: 페이지 디자인
"""
from dev_team_state import DevTeamState
from langchain_core.messages import SystemMessage, HumanMessage


def designer_agent(state: DevTeamState, llm) -> DevTeamState:
    """Designer가 페이지 디자인을 기획"""
    print("🎨 [Designer] 페이지 디자인 기획 중...")

    system_prompt = """당신은 UI/UX 디자이너 Maya입니다.

    역할:
    - 팀 소개 페이지의 디자인 컨셉 수립
    - 색상 스킴, 레이아웃 구조 정의
    - 사용자 경험 최적화

    디자인 원칙:
    - 모던하고 프로페셔널한 느낌
    - 반응형 디자인
    - 읽기 쉽고 명확한 정보 전달
    - 다크모드 지원
    """

    team_info = f"""
    팀 비전: {state['team_vision']}
    팀 강점: {state['team_strengths']}
    팀원: {len(state['team_members'])}명
    프로젝트: {len(state['project_ideas'])}개
    """

    user_message = f"""
    다음 팀 정보를 바탕으로 페이지 디자인을 기획해주세요:
    {team_info}

    JSON 형식으로 작성:
    {{
      "page_design": "페이지 구조 설명 (Hero, Team, Projects, Contact 섹션)",
      "color_scheme": {{
        "primary": "#컬러코드",
        "secondary": "#컬러코드",
        "background": "#컬러코드",
        "text": "#컬러코드",
        "accent": "#컬러코드"
      }},
      "design_concept": "디자인 컨셉 설명"
    }}
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

        state['page_design'] = data.get('page_design', 'Hero + Team + Projects')
        state['color_scheme'] = data.get('color_scheme', {
            'primary': '#6366f1',
            'secondary': '#8b5cf6',
            'background': '#0f172a',
            'text': '#e2e8f0',
            'accent': '#f59e0b'
        })

    except Exception as e:
        print(f"⚠️ JSON 파싱 실패: {e}")
        state['page_design'] = 'Hero 섹션 + 팀 소개 + 프로젝트 + 연락처'
        state['color_scheme'] = {
            'primary': '#6366f1',
            'secondary': '#8b5cf6',
            'background': '#0f172a',
            'text': '#e2e8f0',
            'accent': '#f59e0b'
        }

    print(f"✅ 디자인 컨셉 완료")
    return state
