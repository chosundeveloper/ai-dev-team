"""
PM 에이전트
최종 기획서 작성 및 우선순위 정리
"""
from state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage


def pm_agent(state: AgentState, llm) -> AgentState:
    """최종 기획서 작성"""
    print("📋 [PM 에이전트] 작업 중...")

    # 최고 점수 아이디어 찾기
    if not state['evaluations']:
        state['final_plan'] = "평가 결과가 없습니다."
        return state

    best_idx = max(range(len(state['evaluations'])),
                   key=lambda i: state['evaluations'][i]['overall_score'])

    best_idea = state['ideas'][best_idx]
    best_eval = state['evaluations'][best_idx]

    system_prompt = """당신은 실행력 있는 프로젝트 매니저입니다.

    역할:
    - 최종 기획서 작성
    - 실행 로드맵 수립
    - 우선순위 정리
    - 리스크 및 대응 방안

    기획서는 실무에 바로 적용 가능하도록 구체적으로 작성하세요.
    """

    # 모든 아이디어와 평가 요약
    ideas_summary = "\n\n".join([
        f"아이디어 {i+1}: {idea['title']} (점수: {eval['overall_score']}/10)\n"
        f"- 설명: {idea['description']}\n"
        f"- 평가: {eval['feedback'][:100]}..."
        for i, (idea, eval) in enumerate(zip(state['ideas'], state['evaluations']))
    ])

    user_message = f"""
    전체 분석 결과를 바탕으로 최종 기획서를 작성해주세요.

    === 시장조사 요약 ===
    {state['market_trends'][:300]}...

    === 제안된 아이디어 ===
    {ideas_summary}

    === 최종 선정 아이디어 ===
    제목: {best_idea['title']}
    설명: {best_idea['description']}
    타겟: {best_idea['target_audience']}
    핵심 기능: {', '.join(best_idea['key_features'])}
    차별화: {best_idea['differentiation']}

    종합 점수: {best_eval['overall_score']}/10
    - 바이럴 가능성: {best_eval['viral_potential']}/10
    - 구현 난이도: {best_eval['implementation_difficulty']}/10
    - SEO 점수: {best_eval['seo_score']}/10
    - 수익화 가능성: {best_eval['monetization_potential']}/10

    다음 내용을 포함한 최종 기획서를 작성해주세요:

    1. 📋 프로젝트 개요
    2. 🎯 핵심 가치 제안
    3. 👥 타겟 오디언스 및 페르소나
    4. ⚡ 핵심 기능 상세 (우선순위 포함)
    5. 🚀 3개월 실행 로드맵
    6. 📈 조회수 증대 전략
    7. 💰 수익화 계획
    8. ⚠️ 리스크 및 대응 방안
    9. 📊 성공 지표 (KPI)

    실무에 바로 적용 가능하도록 구체적으로 작성해주세요.
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]

    response = llm.invoke(messages)

    state['final_plan'] = response.content
    print("✅ 최종 기획서 작성 완료")
    return state
