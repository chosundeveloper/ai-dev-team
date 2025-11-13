"""Interactive CrewAI console for issuing agent-specific orders."""
import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from uuid import uuid4

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv

try:
    from langchain_groq import ChatGroq
except ImportError as exc:
    raise SystemExit(
        "langchain_groq is required. Install dependencies with `pip install crewai langchain_groq`"
    ) from exc


def load_llm() -> ChatGroq:
    """Create a Groq-backed chat model based on environment settings."""
    load_dotenv()
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    temperature = float(os.getenv("GROQ_TEMPERATURE", "0.3"))
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise SystemExit("GROQ_API_KEY is missing. Set it in your environment or .env file.")
    return ChatGroq(model=model, temperature=temperature)


def build_agents(llm: ChatGroq) -> dict:
    """Return CrewAI Agent objects keyed by a simple identifier."""
    return {
        "pm": Agent(
            role="Product Manager",
            goal="요구사항을 구조화하고 실행 순서를 제안",
            backstory="Spark Labs의 PM Alex. 시장과 팀 모두를 잘 아는 전략가.",
            llm=llm,
            allow_delegation=False,
        ),
        "designer": Agent(
            role="UI/UX Designer",
            goal="사용자의 감성을 끌어내는 디자인 방향을 제시",
            backstory="Maya는 브랜드 톤과 시각 시스템을 빠르게 잡아주는 디자이너.",
            llm=llm,
            allow_delegation=False,
        ),
        "frontend": Agent(
            role="Frontend Engineer",
            goal="요구사항을 바탕으로 HTML/CSS/JS 솔루션을 설계",
            backstory="Chris는 Next.js/React 경험이 풍부한 프론트 전문가.",
            llm=llm,
            allow_delegation=False,
        ),
        "backend": Agent(
            role="Backend Engineer",
            goal="API와 데이터 파이프라인 설계/최적화를 제안",
            backstory="Jordan은 Python·FastAPI·PostgreSQL에 능숙한 백엔드.",
            llm=llm,
            allow_delegation=False,
        ),
        "growth": Agent(
            role="Growth Strategist",
            goal="바이럴/마케팅 아이디어와 실행 플랜을 제안",
            backstory="Sam은 커뮤니티 기반 성장 전략을 다수 실행해 본 마케터.",
            llm=llm,
            allow_delegation=False,
        ),
    }


def run_order(agent: Agent, order: str) -> str:
    """Send an order to a single agent and return the text response."""
    task = Task(
        description=order,
        expected_output="간결하고 실행 가능한 제안",
        agent=agent,
    )
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
    return crew.kickoff()


REPORT_PATH = Path("reports/log.jsonl")


def append_report(agent_key: str, order: str, response: str) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "id": uuid4().hex,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "agent": agent_key,
        "order": order,
        "response": response,
        "status": "pending",
        "user_feedback": None,
    }
    with REPORT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")


def interactive_loop(agents: dict) -> None:
    """Simple REPL so the user can pick an agent and send orders repeatedly."""
    help_text = dedent(
        """
        사용 가능한 에이전트 키:
          pm | designer | frontend | backend | growth
        `exit` 또는 `quit` 입력 시 종료됩니다.
        """
    )
    print(help_text)
    while True:
        choice = input("에이전트 키> ").strip().lower()
        if choice in {"exit", "quit", "q"}:
            break
        if choice not in agents:
            print("❗️ 알 수 없는 에이전트입니다. 다시 입력하세요.")
            continue
        order = input("오더 입력> ").strip()
        if not order:
            print("⚠️ 내용이 비었습니다. 다시 시도하세요.")
            continue
        print("\n--- 응답 ---")
        response = run_order(agents[choice], order)
        print(response)
        append_report(choice, order, response)
        print("👉 보고가 reports/log.jsonl 에 기록되었습니다. (상태: pending)")
        print("--------------\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CrewAI agent console")
    parser.add_argument("--agent", choices=["pm", "designer", "frontend", "backend", "growth"], help="바로 실행할 에이전트 키")
    parser.add_argument("--order", help="해당 에이전트에 전달할 오더")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    llm = load_llm()
    agents = build_agents(llm)

    if args.agent:
        if not args.order:
            raise SystemExit("--agent 사용 시 --order도 함께 전달하세요.")
        result = run_order(agents[args.agent], args.order)
        print(result)
        append_report(args.agent, args.order, result)
        print("👉 보고가 reports/log.jsonl 에 기록되었습니다. (상태: pending)")
        return

    interactive_loop(agents)


if __name__ == "__main__":
    main()
