"""
시장조사 에이전트
트렌드 분석 및 인기 키워드 조사
"""
from state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage
from agents.utils import log_agent_event, summarize_user_comments, claim_relevant_comments


def market_research_agent(state: AgentState, llm) -> AgentState:
    """시장조사 수행"""
    print("🔍 [시장조사 에이전트] 작업 중...")
    log_agent_event(
        state,
        agent="Alex",
        role="market_research",
        event="start",
        message="시장조사 시작",
    )
    claim_relevant_comments(state, "market_research")

    idea_details = state.get('idea_details') or '추가 메모 없음'

    system_prompt = """당신은 웹 트렌드 전문 시장조사 분석가입니다.

    역할:
    - 최신 웹/모바일 트렌드 파악
    - 바이럴 가능성 높은 키워드 발굴
    - 사용자 관심사 분석
    - 성장 가능성 있는 니치 시장 발굴

    조회수를 끌어올릴 수 있는 요소:
    - 독특하고 신선한 콘셉트
    - 실용성 (사람들이 실제로 사용할 만한)
    - 공유 가능성 (SNS에서 공유하고 싶은)
    - 검색 수요 (사람들이 찾는)
    """

    user_comments = summarize_user_comments(state)

    user_message = f"""
    사용자 요구사항: {state['user_input']}
    제약조건: {state.get('constraints', '없음')}
    아이디어 상세 메모: {idea_details}
    추가 사용자 코멘트:
    {user_comments}

    위 요구사항을 바탕으로:
    1. 관련된 최신 웹 트렌드 분석
    2. 조회수를 끌어올릴 수 있는 인기 키워드 5-7개 제시
    3. 타겟 시장의 특성과 기회 분석

    구체적이고 실용적인 분석을 제공해주세요.
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]

    response = llm.invoke(messages)

    # 키워드 추출 (간단한 파싱)
    keywords = []
    if "키워드" in response.content:
        # 실제로는 더 정교한 파싱 필요
        lines = response.content.split('\n')
        for line in lines:
            if any(marker in line for marker in ['1.', '2.', '3.', '4.', '5.', '-', '•']):
                keyword = line.split('.', 1)[-1].split('-', 1)[-1].split('•', 1)[-1].strip()
                if keyword and len(keyword) < 50:
                    keywords.append(keyword)

    state['market_trends'] = response.content
    state['popular_keywords'] = keywords[:7] if keywords else ['AI', '자동화', '생산성']

    print(f"✅ 시장조사 완료: {len(keywords)}개 키워드 발굴")
    log_agent_event(
        state,
        agent="Alex",
        role="market_research",
        event="result",
        message=response.content,
    )
    return state
