"""
아이디어 생성 에이전트
웹사이트 아이디어 및 기능 명세 생성
"""
from state import AgentState, WebsiteIdea
from langchain_core.messages import SystemMessage, HumanMessage
import json


def idea_generator_agent(state: AgentState, llm) -> AgentState:
    """아이디어 생성"""
    print("💡 [기획 에이전트] 작업 중...")

    system_prompt = """당신은 창의적이고 실용적인 웹 서비스 기획자입니다.

    역할:
    - 조회수 높은 웹사이트 아이디어 생성
    - 구체적인 기능 명세 작성
    - 타겟 오디언스 정의
    - 바이럴 요소 포함

    좋은 아이디어 특징:
    - 명확한 가치 제안
    - 실행 가능한 기능 구성
    - 공유하고 싶어지는 요소
    - SEO 친화적 콘텐츠 구조
    """

    user_message = f"""
    시장조사 결과:
    {state['market_trends'][:500]}...

    경쟁분석 결과:
    차별화 포인트: {', '.join(state['differentiation_points'])}

    위 분석을 바탕으로 웹사이트 아이디어 3개를 제안해주세요.

    각 아이디어는 다음 형식으로:
    1. 제목: (간결하고 매력적인)
    2. 설명: (핵심 가치 제안)
    3. 타겟: (구체적인 사용자층)
    4. 핵심 기능 5가지:
       - 기능1
       - 기능2
       ...
    5. 차별화 포인트: (왜 이게 성공할 것인가)

    JSON 형식으로 응답해주세요:
    {{
      "ideas": [
        {{
          "title": "...",
          "description": "...",
          "target_audience": "...",
          "key_features": ["...", "..."],
          "differentiation": "..."
        }}
      ]
    }}
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]

    response = llm.invoke(messages)

    # JSON 파싱 시도
    try:
        # JSON 부분 추출
        content = response.content
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]

        data = json.loads(content.strip())
        ideas = data.get('ideas', [])

    except Exception as e:
        print(f"⚠️ JSON 파싱 실패: {e}, 기본 아이디어 생성")
        # 파싱 실패시 기본 아이디어
        ideas = [{
            'title': '조회수 증폭 웹사이트',
            'description': '시장조사와 경쟁분석 기반 웹사이트',
            'target_audience': '웹 사용자',
            'key_features': state['differentiation_points'][:3],
            'differentiation': '데이터 기반 차별화'
        }]

    state['ideas'] = ideas
    print(f"✅ 아이디어 생성 완료: {len(ideas)}개")
    return state
