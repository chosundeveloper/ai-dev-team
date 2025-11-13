"""
간단한 테스트 예제
빠르게 시스템을 테스트할 수 있습니다
"""
from main import run_planning

# 간단한 예제
user_input = "개발자들이 매일 방문하는 실용적인 도구 사이트"
constraints = "혼자서 2주 안에 만들 수 있어야 함"

print("\n🧪 간단한 테스트 실행 중...\n")
result = run_planning(user_input, constraints)

print("\n✅ 테스트 완료!")
print(f"생성된 아이디어 수: {len(result['ideas'])}")
print(f"최고 점수: {max(e['overall_score'] for e in result['evaluations'])}/10")
