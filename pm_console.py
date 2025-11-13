"""Simple PM order console that fans out to other agents."""
import json
from dataclasses import dataclass
from pathlib import Path
from typing import List

from crewai import Agent, Crew, Task, Process
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

@dataclass
class AgentSpec:
    key: str
    role: str
    goal: str
    backstory: str

AGENTS: List[AgentSpec] = [
    AgentSpec("pm", "Product Manager", "요구사항을 구조화해 다음 액션을 결정", "Spark Labs의 PM"),
    AgentSpec("designer", "UI/UX Designer", "시각 컨셉/레이아웃 제안", "Maya"),
    AgentSpec("frontend", "Frontend Engineer", "HTML/CSS/JS 솔루션 설계", "Chris"),
    AgentSpec("backend", "Backend Engineer", "API/데이터 파이프라인 설계", "Jordan"),
    AgentSpec("growth", "Growth Specialist", "바이럴/마케팅 아이디어 제안", "Sam"),
]


def build_agent(llm: ChatGroq, spec: AgentSpec) -> Agent:
    return Agent(role=spec.role, goal=spec.goal, backstory=spec.backstory, llm=llm, allow_delegation=False)


def load_llm() -> ChatGroq:
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)


def run_flow(order: str) -> str:
    llm = load_llm()
    agents = {spec.key: build_agent(llm, spec) for spec in AGENTS}

    pm_task = Task(description=order, expected_output="핵심 요구사항과 필요한 역할" , agent=agents["pm"])
    designer_task = Task(description="PM의 요청을 바탕으로 디자인 방향/레이아웃 제안", agent=agents["designer"])
    frontend_task = Task(description="디자인 결과를 HTML/CSS 구현 관점에서 정리", agent=agents["frontend"])

    crew = Crew(
        agents=[agents["pm"], agents["designer"], agents["frontend"]],
        tasks=[pm_task, designer_task, frontend_task],
        process=Process.sequential,
        verbose=True,
    )
    result = crew.kickoff()
    Path("reports").mkdir(exist_ok=True)
    Path("reports/pm_flow.json").write_text(json.dumps({"order": order, "result": result}, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main() -> None:
    order = input("PM에게 전달할 요구사항을 입력하세요> ")
    if not order.strip():
        raise SystemExit("요구사항이 비었습니다.")
    summary = run_flow(order)
    print("\n=== 최종 요약 ===")
    print(summary)


if __name__ == "__main__":
    main()
