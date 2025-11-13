"""
LangGraph 멀티 에이전트 워크플로우
5개의 전문 에이전트가 협업하여 웹사이트 기획
"""
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from state import AgentState

# 에이전트 임포트
from agents.market_research import market_research_agent
from agents.competitive_analysis import competitive_analysis_agent
from agents.idea_generator import idea_generator_agent
from agents.evaluator import evaluator_agent
from agents.pm import pm_agent


def create_workflow():
    """LangGraph 워크플로우 생성"""

    # 환경 변수 로드
    load_dotenv()

    # LLM 설정
    llm_provider = os.getenv('LLM_PROVIDER', 'groq')

    if llm_provider == 'groq':
        from langchain_groq import ChatGroq
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",  # 무료, 빠름
            temperature=0.7
        )
        print("🤖 LLM: Groq Llama 3.3 70B (무료)")
    elif llm_provider == 'openai':
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7
        )
        print("🤖 LLM: OpenAI GPT-4o-mini")
    elif llm_provider == 'anthropic':
        from langchain_anthropic import ChatAnthropic
        llm = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            temperature=0.7
        )
        print("🤖 LLM: Anthropic Claude 3.5 Sonnet")
    else:
        raise ValueError(f"지원하지 않는 LLM: {llm_provider}")

    # StateGraph 생성
    workflow = StateGraph(AgentState)

    # 각 에이전트를 노드로 추가 (llm을 바인딩)
    workflow.add_node("market_research",
                     lambda state: market_research_agent(state, llm))
    workflow.add_node("competitive_analysis",
                     lambda state: competitive_analysis_agent(state, llm))
    workflow.add_node("idea_generator",
                     lambda state: idea_generator_agent(state, llm))
    workflow.add_node("evaluator",
                     lambda state: evaluator_agent(state, llm))
    workflow.add_node("pm",
                     lambda state: pm_agent(state, llm))

    # 워크플로우 정의: 순차적 실행
    workflow.set_entry_point("market_research")
    workflow.add_edge("market_research", "competitive_analysis")
    workflow.add_edge("competitive_analysis", "idea_generator")
    workflow.add_edge("idea_generator", "evaluator")
    workflow.add_edge("evaluator", "pm")
    workflow.add_edge("pm", END)

    return workflow.compile()


def run_planning(user_input: str, constraints: str = None):
    """기획 실행"""
    print("=" * 60)
    print("🚀 AI 기획자/PM 시스템 시작")
    print("=" * 60)
    print(f"\n📝 사용자 입력: {user_input}")
    if constraints:
        print(f"⚠️ 제약조건: {constraints}")
    print("\n")

    # 워크플로우 생성
    app = create_workflow()

    # 초기 상태
    initial_state: AgentState = {
        'user_input': user_input,
        'constraints': constraints,
        'market_trends': '',
        'popular_keywords': [],
        'competitor_analysis': '',
        'differentiation_points': [],
        'ideas': [],
        'evaluations': [],
        'final_plan': '',
        'iteration_count': 0,
        'needs_improvement': False
    }

    # 실행
    print("🔄 에이전트 워크플로우 실행 중...\n")
    result = app.invoke(initial_state)

    # 결과 출력
    print("\n" + "=" * 60)
    print("✨ 최종 기획서")
    print("=" * 60)
    print(result['final_plan'])
    print("\n" + "=" * 60)

    return result


if __name__ == "__main__":
    # 예제 실행
    user_input = """
    IT 업계 종사자와 개발자들이 자주 방문할 만한 웹사이트를 만들고 싶어.
    실용적이면서도 매일 확인하고 싶어지는 그런 사이트.
    """

    constraints = """
    - 개발 기간: 1-2개월
    - 혼자서 구현 가능한 수준
    - 광고 수익 모델
    """

    result = run_planning(user_input, constraints)

    # 결과를 파일로 저장
    with open('final_plan.md', 'w', encoding='utf-8') as f:
        f.write(result['final_plan'])

    print("\n💾 기획서가 'final_plan.md' 파일로 저장되었습니다.")
