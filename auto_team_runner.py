#!/usr/bin/env python3
"""
24시간 자동 팀 운영 시스템
PM의 지시에 따라 팀원들이 자동으로 작업을 수행합니다.
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any
import schedule
from dataclasses import dataclass, asdict
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('team_operations.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


@dataclass
class Task:
    """작업 정의"""
    id: str
    title: str
    assigned_to: str  # PM, Designer, Frontend, Backend, Growth
    phase: int  # 1-4
    hour_start: int
    hour_end: int
    priority: str  # P0, P1, P2
    status: str = "pending"  # pending, in_progress, completed, blocked
    dependencies: List[str] = None
    output_file: str = None
    started_at: str = None
    completed_at: str = None
    notes: str = ""

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []


@dataclass
class TeamMember:
    """팀원 정의"""
    name: str
    role: str
    current_task: str = None
    tasks_completed: int = 0
    status: str = "available"  # available, working, break


class TeamOrchestrator:
    """24시간 팀 운영 오케스트레이터"""

    def __init__(self):
        self.start_time = datetime.now()
        self.tasks: Dict[str, Task] = {}
        self.team_members: Dict[str, TeamMember] = {}
        self.reports_dir = Path("reports/24h_operations")
        self.reports_dir.mkdir(parents=True, exist_ok=True)

        self._initialize_team()
        self._initialize_tasks()

    def _initialize_team(self):
        """팀원 초기화"""
        self.team_members = {
            "PM": TeamMember("Alex", "Product Manager"),
            "Designer": TeamMember("Maya", "UI/UX Designer"),
            "Frontend": TeamMember("Chris", "Frontend Engineer"),
            "Backend": TeamMember("Jordan", "Backend Engineer"),
            "Growth": TeamMember("Sam", "Growth Specialist")
        }
        logger.info("✅ 팀 초기화 완료")

    def _initialize_tasks(self):
        """작업 초기화 - PM의 계획에서 로드"""
        tasks = [
            # Phase 1: 준비 및 설계 (0-3시간) - 모든 팀원 즉시 시작!
            Task("PM-001", "프로젝트 요구사항 문서 작성", "PM", 1, 0, 1, "P0"),
            Task("PM-002", "기술 스택 최종 확정", "PM", 1, 0, 1, "P0"),
            Task("PM-003", "작업 분배 및 일정 수립", "PM", 1, 0, 1, "P0"),

            Task("DESIGN-001", "뉴스레터 레이아웃 와이어프레임", "Designer", 1, 0, 3, "P0"),
            Task("DESIGN-002", "컬러 스킴 및 브랜딩 가이드", "Designer", 1, 0, 3, "P0"),
            Task("DESIGN-003", "랜딩 페이지 목업", "Designer", 1, 0, 3, "P0"),

            Task("BE-001", "API 아키텍처 설계", "Backend", 1, 0, 3, "P0"),
            Task("BE-002", "데이터베이스 스키마 설계", "Backend", 1, 0, 3, "P0"),
            Task("BE-003", "크롤링 시스템 구조 설계", "Backend", 1, 0, 3, "P0"),

            Task("FE-001", "컴포넌트 구조 설계", "Frontend", 1, 0, 3, "P0"),
            Task("FE-002", "라우팅 계획", "Frontend", 1, 0, 3, "P0"),
            Task("FE-003", "상태 관리 전략", "Frontend", 1, 0, 3, "P0"),

            Task("GR-001", "타겟 오디언스 분석", "Growth", 1, 0, 3, "P0"),
            Task("GR-002", "초기 마케팅 전략 수립", "Growth", 1, 0, 3, "P0"),

            # Phase 2: 핵심 기능 개발 (3-12시간)
            Task("BE-004", "FastAPI 프로젝트 초기화", "Backend", 2, 3, 6, "P0", ["BE-001"]),
            Task("BE-005", "데이터베이스 설정", "Backend", 2, 3, 6, "P0", ["BE-002"]),
            Task("BE-006", "뉴스 크롤러 프로토타입", "Backend", 2, 3, 6, "P0", ["BE-003"]),
            Task("BE-007", "AI 요약 기능", "Backend", 2, 3, 6, "P0", ["BE-004"]),

            Task("FE-004", "React 프로젝트 초기화", "Frontend", 2, 6, 9, "P0", ["FE-001"]),
            Task("FE-005", "기본 라우팅 설정", "Frontend", 2, 6, 9, "P0", ["FE-002"]),
            Task("FE-006", "랜딩 페이지 구현", "Frontend", 2, 6, 9, "P0", ["DESIGN-003"]),

            Task("DESIGN-004", "UI 컴포넌트 디자인 완성", "Designer", 2, 6, 9, "P0"),
            Task("DESIGN-005", "이메일 템플릿 디자인", "Designer", 2, 6, 9, "P0"),

            Task("BE-008", "AI 뉴스 큐레이션 로직", "Backend", 2, 9, 12, "P0", ["BE-007"]),
            Task("BE-009", "이메일 발송 기능", "Backend", 2, 9, 12, "P0"),

            Task("FE-007", "API 연동", "Frontend", 2, 9, 12, "P0", ["BE-007"]),
            Task("FE-008", "뉴스 목록 표시", "Frontend", 2, 9, 12, "P0", ["FE-007"]),

            # Phase 3: 완성 및 테스트 (12-18시간)
            Task("BE-010", "스케줄러 구현", "Backend", 3, 12, 15, "P0"),
            Task("BE-011", "사용자 관리 API", "Backend", 3, 12, 15, "P1"),

            Task("FE-009", "구독 완료 페이지", "Frontend", 3, 12, 15, "P0"),
            Task("FE-010", "아카이브 페이지", "Frontend", 3, 12, 15, "P1"),
            Task("FE-011", "모바일 최적화", "Frontend", 3, 12, 15, "P1"),

            Task("DESIGN-006", "최종 디자인 QA", "Designer", 3, 12, 15, "P0"),

            Task("TEST-001", "전체 팀 기능 테스트", "PM", 3, 15, 18, "P0"),

            # Phase 4: 배포 및 마케팅 (18-24시간)
            Task("BE-012", "백엔드 배포", "Backend", 4, 18, 21, "P0"),
            Task("FE-012", "프론트엔드 배포", "Frontend", 4, 18, 21, "P0"),

            Task("GR-003", "ProductHunt 제출 준비", "Growth", 4, 21, 24, "P0"),
            Task("GR-004", "커뮤니티 마케팅", "Growth", 4, 21, 24, "P0"),

            Task("PM-004", "런칭 체크리스트 검토", "PM", 4, 21, 24, "P0"),
            Task("PM-005", "다음 24시간 계획", "PM", 4, 21, 24, "P0"),
        ]

        self.tasks = {task.id: task for task in tasks}
        logger.info(f"✅ {len(self.tasks)}개 작업 초기화 완료")

    def get_current_hour(self) -> int:
        """시작 시점으로부터 경과 시간 (시간)"""
        elapsed = datetime.now() - self.start_time
        return int(elapsed.total_seconds() / 3600)

    def get_available_tasks(self, team_member: str) -> List[Task]:
        """팀원이 수행 가능한 작업 목록 - Hour 무시하고 바로바로 진행"""
        available = []

        for task in self.tasks.values():
            if (task.assigned_to == team_member and
                task.status == "pending"):

                # 의존성 체크만 수행 (Hour는 무시)
                dependencies_met = all(
                    self.tasks[dep_id].status == "completed"
                    for dep_id in task.dependencies
                )

                if dependencies_met:
                    available.append(task)

        # 우선순위 정렬 (P0 > P1 > P2)
        priority_order = {"P0": 0, "P1": 1, "P2": 2}
        available.sort(key=lambda t: priority_order.get(t.priority, 999))

        return available

    def assign_task(self, team_member: str, task: Task):
        """작업 할당"""
        task.status = "in_progress"
        task.started_at = datetime.now().isoformat()

        member = self.team_members[team_member]
        member.current_task = task.id
        member.status = "working"

        logger.info(f"📋 [{team_member}] 작업 시작: {task.title}")

    def complete_task(self, task_id: str, output: Dict[str, Any] = None):
        """작업 완료"""
        task = self.tasks[task_id]
        task.status = "completed"
        task.completed_at = datetime.now().isoformat()

        team_member = task.assigned_to
        member = self.team_members[team_member]
        member.current_task = None
        member.tasks_completed += 1
        member.status = "available"

        # 결과 저장
        if output:
            output_file = self.reports_dir / f"{task_id}.json"
            output_file.write_text(json.dumps(output, ensure_ascii=False, indent=2))
            task.output_file = str(output_file)

        logger.info(f"✅ [{team_member}] 작업 완료: {task.title}")

    def simulate_task_execution(self, task: Task) -> Dict[str, Any]:
        """작업 실행 시뮬레이션 (실제로는 AI 에이전트가 수행)"""
        logger.info(f"🔄 [{task.assigned_to}] 실행 중: {task.title}")

        # 실제로는 여기서 CrewAI나 LangGraph 에이전트를 호출
        # 지금은 시뮬레이션으로 처리
        time.sleep(2)  # 실제 작업 시뮬레이션

        return {
            "task_id": task.id,
            "title": task.title,
            "assigned_to": task.assigned_to,
            "result": f"{task.title} 완료됨",
            "completed_at": datetime.now().isoformat()
        }

    def run_cycle(self):
        """1회 실행 사이클 (매 시간마다)"""
        current_hour = self.get_current_hour()
        logger.info(f"\n{'='*60}")
        logger.info(f"⏰ Hour {current_hour}/24 - 작업 사이클 시작")
        logger.info(f"{'='*60}\n")

        # 모든 팀원에 대해
        for member_key, member in self.team_members.items():
            if member.status == "available":
                # 가능한 작업 찾기
                available_tasks = self.get_available_tasks(member_key)

                if available_tasks:
                    # 가장 높은 우선순위 작업 할당
                    task = available_tasks[0]
                    self.assign_task(member_key, task)

                    # 작업 실행
                    try:
                        result = self.simulate_task_execution(task)
                        self.complete_task(task.id, result)
                    except Exception as e:
                        logger.error(f"❌ 작업 실패: {task.id} - {str(e)}")
                        task.status = "blocked"
                        task.notes = str(e)

        # 진행 상황 리포트
        self.generate_progress_report()

    def generate_progress_report(self):
        """진행 상황 리포트 생성"""
        current_hour = self.get_current_hour()

        total_tasks = len(self.tasks)
        completed = sum(1 for t in self.tasks.values() if t.status == "completed")
        in_progress = sum(1 for t in self.tasks.values() if t.status == "in_progress")
        blocked = sum(1 for t in self.tasks.values() if t.status == "blocked")

        report = {
            "timestamp": datetime.now().isoformat(),
            "hour": current_hour,
            "progress": {
                "total_tasks": total_tasks,
                "completed": completed,
                "in_progress": in_progress,
                "blocked": blocked,
                "completion_rate": f"{completed / total_tasks * 100:.1f}%"
            },
            "team_status": {
                member_key: {
                    "name": member.name,
                    "role": member.role,
                    "status": member.status,
                    "current_task": member.current_task,
                    "tasks_completed": member.tasks_completed
                }
                for member_key, member in self.team_members.items()
            },
            "tasks": {
                task_id: {
                    "title": task.title,
                    "status": task.status,
                    "assigned_to": task.assigned_to,
                    "priority": task.priority,
                    "phase": task.phase
                }
                for task_id, task in self.tasks.items()
            }
        }

        # 리포트 저장
        report_file = self.reports_dir / f"progress_hour_{current_hour:02d}.json"
        report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2))

        # 콘솔 출력
        logger.info(f"\n📊 진행 상황 (Hour {current_hour}):")
        logger.info(f"   완료: {completed}/{total_tasks} ({completed / total_tasks * 100:.1f}%)")
        logger.info(f"   진행 중: {in_progress}")
        logger.info(f"   차단됨: {blocked}\n")

    def run_continuous_operation(self):
        """연속 작업 실행 - Hour 구분 없이 모든 작업 연속 진행"""
        logger.info("🚀 연속 작업 모드 시작! (Hour 구분 없이 바로바로 진행)")
        logger.info(f"시작 시간: {self.start_time}")

        cycle_count = 0
        max_cycles = 200  # 무한루프 방지

        try:
            while cycle_count < max_cycles:
                cycle_count += 1
                logger.info(f"\n{'='*60}")
                logger.info(f"⏰ 작업 사이클 #{cycle_count}")
                logger.info(f"{'='*60}\n")

                # 모든 팀원에 대해
                any_work_done = False
                for member_key, member in self.team_members.items():
                    if member.status == "available":
                        # 가능한 작업 찾기
                        available_tasks = self.get_available_tasks(member_key)

                        if available_tasks:
                            any_work_done = True
                            # 가장 높은 우선순위 작업 할당
                            task = available_tasks[0]
                            self.assign_task(member_key, task)

                            # 작업 실행
                            try:
                                result = self.simulate_task_execution(task)
                                self.complete_task(task.id, result)
                            except Exception as e:
                                logger.error(f"❌ 작업 실패: {task.id} - {str(e)}")
                                task.status = "blocked"
                                task.notes = str(e)

                # 진행 상황 리포트
                self.generate_progress_report()

                # 더 이상 할 일이 없으면 종료
                if not any_work_done:
                    logger.info("\n✅ 모든 가능한 작업 완료!")
                    break

                # 짧은 딜레이 (로그 확인용)
                time.sleep(0.5)

        except KeyboardInterrupt:
            logger.info("\n⚠️  사용자에 의해 중단됨")

        logger.info("\n🏁 연속 작업 완료!")
        self.generate_final_report()

    def generate_final_report(self):
        """최종 리포트 생성"""
        logger.info("\n" + "="*60)
        logger.info("📈 최종 리포트")
        logger.info("="*60)

        total_tasks = len(self.tasks)
        completed = sum(1 for t in self.tasks.values() if t.status == "completed")

        logger.info(f"\n✅ 전체 작업: {total_tasks}")
        logger.info(f"✅ 완료: {completed} ({completed / total_tasks * 100:.1f}%)")

        for member_key, member in self.team_members.items():
            logger.info(f"\n👤 {member.name} ({member.role}):")
            logger.info(f"   완료한 작업: {member.tasks_completed}개")

        # 최종 리포트 파일 저장
        final_report_file = self.reports_dir / "final_report.json"
        final_report = {
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.now().isoformat(),
            "total_tasks": total_tasks,
            "completed_tasks": completed,
            "completion_rate": f"{completed / total_tasks * 100:.1f}%",
            "team_performance": {
                member_key: {
                    "name": member.name,
                    "tasks_completed": member.tasks_completed
                }
                for member_key, member in self.team_members.items()
            }
        }

        final_report_file.write_text(json.dumps(final_report, ensure_ascii=False, indent=2))
        logger.info(f"\n📄 최종 리포트 저장: {final_report_file}")


def main():
    """메인 실행 함수"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║         🚀 Spark Labs 24시간 팀 자동 운영 시스템         ║
    ║                                                           ║
    ║  PM(Alex)의 계획에 따라 팀원들이 자동으로 작업합니다     ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    orchestrator = TeamOrchestrator()

    print("\n실행 모드를 선택하세요:")
    print("1. 연속 작업 모드 (Hour 구분 없이 바로바로 진행) ⚡ 추천!")
    print("2. 시간 기반 모드 (1시간 = 1분)")

    choice = input("\n선택 (1 또는 2): ").strip()

    if choice == "1":
        logger.info("⚡ 연속 작업 모드! 모든 작업을 바로바로 진행합니다!")
        orchestrator.run_continuous_operation()
    else:
        logger.info("⏰ 시간 기반 모드로 실행")
        orchestrator.run_24h_operation(interval_minutes=1)


if __name__ == "__main__":
    main()
