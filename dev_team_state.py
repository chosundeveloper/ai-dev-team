"""
개발팀 상태 정의
"""
from typing import TypedDict, List, Dict, Optional


class TeamMember(TypedDict):
    """팀 멤버 정보"""
    name: str
    role: str
    model: str
    skills: List[str]
    description: str


class ProjectIdea(TypedDict):
    """프로젝트 아이디어"""
    title: str
    description: str
    tech_stack: List[str]
    features: List[str]
    timeline: str


class DevTeamState(TypedDict):
    """개발팀 상태"""
    # 팀 구성
    team_members: List[TeamMember]

    # 프로젝트 아이디어
    project_ideas: List[ProjectIdea]

    # PM 산출물
    team_vision: str
    team_strengths: str

    # Designer 산출물
    page_design: str
    color_scheme: Dict[str, str]

    # Frontend 산출물
    html_code: str
    css_code: str
    js_code: str

    # 최종 결과
    final_page: str
