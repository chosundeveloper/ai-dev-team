"""
공유 상태 정의
모든 에이전트가 공유하는 상태 구조
"""
from typing import TypedDict, List, Optional
from typing_extensions import Annotated


class WebsiteIdea(TypedDict):
    """웹사이트 아이디어"""
    title: str
    description: str
    target_audience: str
    key_features: List[str]
    differentiation: str


class EvaluationScore(TypedDict):
    """평가 점수"""
    viral_potential: int  # 1-10
    implementation_difficulty: int  # 1-10
    seo_score: int  # 1-10
    monetization_potential: int  # 1-10
    overall_score: float
    feedback: str


class AgentState(TypedDict):
    """전체 에이전트가 공유하는 상태"""
    # 입력
    user_input: str
    constraints: Optional[str]

    # 시장조사 결과
    market_trends: str
    popular_keywords: List[str]

    # 경쟁분석 결과
    competitor_analysis: str
    differentiation_points: List[str]

    # 기획 결과
    ideas: List[WebsiteIdea]

    # 평가 결과
    evaluations: List[EvaluationScore]

    # 최종 결과
    final_plan: str

    # 반복 제어
    iteration_count: int
    needs_improvement: bool
