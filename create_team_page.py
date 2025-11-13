"""
AI 개발팀이 자기 소개 페이지를 만드는 시스템
"""
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from dev_team_state import DevTeamState

# 에이전트 임포트
from dev_agents.pm_agent import pm_agent
from dev_agents.designer_agent import designer_agent
from dev_agents.frontend_agent import frontend_agent
from llm_factory import build_chat_model


def create_team_workflow():
    """개발팀 워크플로우 생성"""
    load_dotenv()

    llm_creative = build_chat_model(role="creative")

    print("🤖 AI 개발팀 시작")
    print("=" * 60)

    # StateGraph 생성
    workflow = StateGraph(DevTeamState)

    # 에이전트 노드 추가
    workflow.add_node("pm", lambda state: pm_agent(state, llm_creative))
    workflow.add_node("designer", lambda state: designer_agent(state, llm_creative))
    workflow.add_node("frontend", lambda state: frontend_agent(state, llm_creative))

    # 워크플로우: PM → Designer → Frontend
    workflow.set_entry_point("pm")
    workflow.add_edge("pm", "designer")
    workflow.add_edge("designer", "frontend")
    workflow.add_edge("frontend", END)

    return workflow.compile()


def main():
    """팀 소개 페이지 생성"""
    print("\n🚀 AI 개발팀이 자기소개 페이지를 만듭니다!\n")
    print("=" * 60)

    # 워크플로우 생성
    app = create_team_workflow()

    # 초기 상태
    initial_state: DevTeamState = {
        'team_members': [],
        'project_ideas': [],
        'team_vision': '',
        'team_strengths': '',
        'page_design': '',
        'color_scheme': {},
        'html_code': '',
        'css_code': '',
        'js_code': '',
        'final_page': ''
    }

    # 실행
    print("\n🔄 개발팀 워크플로우 실행 중...\n")
    result = app.invoke(initial_state)

    # 결과를 HTML 파일로 저장
    output_file = 'team_portfolio.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['final_page'])

    print("\n" + "=" * 60)
    print("✅ 완료!")
    print("=" * 60)
    print(f"\n📄 파일 생성: {output_file}")
    print(f"👥 팀원: {len(result['team_members'])}명")
    print(f"🚀 프로젝트: {len(result['project_ideas'])}개")
    print(f"📝 코드 크기: {len(result['final_page'])} 문자\n")

    print("💡 브라우저에서 열어보세요:")
    print(f"   open {output_file}")
    print()

    return result


if __name__ == "__main__":
    result = main()
