"""
평가 에이전트
아이디어의 바이럴 가능성, 구현 난이도, SEO 등 평가
"""
from state import AgentState, EvaluationScore
from langchain_core.messages import SystemMessage, HumanMessage
import json


def evaluator_agent(state: AgentState, llm) -> AgentState:
    """아이디어 평가"""
    print("📊 [평가 에이전트] 작업 중...")

    system_prompt = """당신은 웹사이트 성공 가능성을 평가하는 전문가입니다.

    평가 기준:
    1. 바이럴 가능성 (1-10): SNS 공유, 입소문 가능성
    2. 구현 난이도 (1-10): 기술적 복잡도 (낮을수록 좋음)
    3. SEO 점수 (1-10): 검색 노출 가능성
    4. 수익화 가능성 (1-10): 광고, 구독 등 수익 모델

    객관적이고 현실적인 평가를 제공하세요.
    """

    evaluations = []

    for idx, idea in enumerate(state['ideas']):
        user_message = f"""
        아이디어 평가 요청:

        제목: {idea['title']}
        설명: {idea['description']}
        타겟: {idea['target_audience']}
        기능: {', '.join(idea['key_features'])}
        차별화: {idea['differentiation']}

        다음 형식으로 평가해주세요:
        {{
          "viral_potential": 7,
          "implementation_difficulty": 5,
          "seo_score": 8,
          "monetization_potential": 6,
          "feedback": "구체적인 피드백..."
        }}

        JSON으로만 응답해주세요.
        """

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_message)
        ]

        response = llm.invoke(messages)

        # JSON 파싱
        try:
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]

            eval_data = json.loads(content.strip())

            # 전체 점수 계산 (구현 난이도는 역수)
            overall = (
                eval_data['viral_potential'] * 0.3 +
                (10 - eval_data['implementation_difficulty']) * 0.2 +
                eval_data['seo_score'] * 0.3 +
                eval_data['monetization_potential'] * 0.2
            )

            evaluation: EvaluationScore = {
                'viral_potential': eval_data['viral_potential'],
                'implementation_difficulty': eval_data['implementation_difficulty'],
                'seo_score': eval_data['seo_score'],
                'monetization_potential': eval_data['monetization_potential'],
                'overall_score': round(overall, 2),
                'feedback': eval_data['feedback']
            }

        except Exception as e:
            print(f"⚠️ 평가 파싱 실패 ({idx+1}): {e}")
            evaluation: EvaluationScore = {
                'viral_potential': 5,
                'implementation_difficulty': 5,
                'seo_score': 5,
                'monetization_potential': 5,
                'overall_score': 5.0,
                'feedback': '자동 평가'
            }

        evaluations.append(evaluation)
        print(f"  아이디어 {idx+1}: 종합점수 {evaluation['overall_score']}/10")

    state['evaluations'] = evaluations
    print(f"✅ 평가 완료: {len(evaluations)}개 아이디어")
    return state
