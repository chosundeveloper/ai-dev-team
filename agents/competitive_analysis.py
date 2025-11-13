"""
경쟁분석 에이전트
유사 사이트 분석 및 차별화 포인트 발굴
"""
from state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage


def competitive_analysis_agent(state: AgentState, llm) -> AgentState:
    """경쟁 분석 수행"""
    print("⚔️ [경쟁분석 에이전트] 작업 중...")

    system_prompt = """당신은 경쟁 분석 및 차별화 전략 전문가입니다.

    역할:
    - 기존 유사 서비스/웹사이트 분석
    - 시장 공백 파악
    - 차별화 포인트 발굴
    - Blue Ocean 전략 수립

    차별화 전략:
    - 기존 서비스의 불편함 해결
    - 새로운 관점/접근법 제시
    - 타겟 세분화 (더 좁고 깊게)
    - 독특한 UX/기능 조합
    """

    user_message = f"""
    시장조사 결과:
    {state['market_trends']}

    발굴된 키워드: {', '.join(state['popular_keywords'])}

    위 정보를 바탕으로:
    1. 이 분야의 주요 경쟁 서비스/사이트 분석
    2. 기존 서비스의 한계점 파악
    3. 차별화 가능한 5가지 포인트 제시

    구체적이고 실행 가능한 차별화 전략을 제안해주세요.
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]

    response = llm.invoke(messages)

    # 차별화 포인트 추출
    diff_points = []
    lines = response.content.split('\n')
    for line in lines:
        if any(marker in line for marker in ['1.', '2.', '3.', '4.', '5.', '-', '•']):
            point = line.split('.', 1)[-1].split('-', 1)[-1].split('•', 1)[-1].strip()
            if point and 10 < len(point) < 200:
                diff_points.append(point)

    state['competitor_analysis'] = response.content
    state['differentiation_points'] = diff_points[:5] if diff_points else ['독특한 UX', '틈새 타겟팅']

    print(f"✅ 경쟁분석 완료: {len(diff_points)}개 차별화 포인트 발굴")
    return state
