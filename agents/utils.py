"""Shared helpers for logging and comment coordination between agents."""
from datetime import datetime
from typing import Literal, List

from state import AgentState

ROLE_LABELS = {
    "market_research": "시장조사",
    "competitive_analysis": "경쟁분석",
    "idea_generator": "기획",
    "evaluator": "평가",
    "pm": "PM",
}

ROLE_AGENTS = {
    "market_research": "Sam",
    "competitive_analysis": "Jordan",
    "idea_generator": "Maya",
    "evaluator": "Chris",
    "pm": "Alex",
}

AGENT_KEYWORDS = {
    "market_research": ["시장", "트렌드", "키워드", "수요", "리서치"],
    "competitive_analysis": ["경쟁", "차별", "벤치마킹", "라이벌", "포지셔닝"],
    "idea_generator": ["아이디어", "기획", "기능", "콘셉트", "디자인", "UX", "UI"],
    "evaluator": ["점수", "리스크", "평가", "우선순위", "가중치"],
    "pm": ["최종", "로드맵", "수익", "전략", "거버넌스", "운영"],
}


def log_agent_event(
    state: AgentState,
    *,
    agent: str,
    role: str,
    event: Literal["start", "result", "info", "error"],
    message: str,
) -> None:
    """Append a structured log entry to the shared conversation timeline."""
    logs = state.get("conversation_logs")
    if logs is None:
        logs = []
        state["conversation_logs"] = logs  # type: ignore[index]

    logs.append(
        {
            "agent": agent,
            "role": role,
            "event": event,
            "message": message.strip(),
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    )


def _matches_comment(message: str, keywords: List[str]) -> bool:
    text = message.lower()
    return any(keyword.lower() in text for keyword in keywords)


def claim_relevant_comments(
    state: AgentState,
    role: str,
    *,
    claim_all: bool = False,
) -> List[dict]:
    """Assign unclaimed user comments to the agent if relevant."""
    comments = state.get("user_comments") or []
    claimed = []
    keywords = AGENT_KEYWORDS.get(role, [])

    for comment in comments:
        owners = comment.setdefault("assigned_to", [])
        if owners:
            continue

        if claim_all or _matches_comment(comment["message"], keywords):
            owners.append(role)
            comment["assigned_to"] = owners
            claimed.append(comment)

    if claimed:
        summary = "\n".join(f"- {c['message']}" for c in claimed)
        log_agent_event(
            state,
            agent=ROLE_AGENTS.get(role, role),
            role=role,
            event="info",
            message=f"사용자 코멘트 배정\n{summary}",
        )

    return claimed


def summarize_user_comments(state: AgentState) -> str:
    """Return human-readable list of user comments and their owners."""
    comments = state.get("user_comments") or []
    if not comments:
        return "없음"

    lines = []
    for comment in comments:
        owners = comment.get("assigned_to") or []
        if owners:
            label = ", ".join(ROLE_LABELS.get(owner, owner) for owner in owners)
        else:
            label = "미정"
        lines.append(f"- ({label}) {comment['message']}")
    return "\n".join(lines)
