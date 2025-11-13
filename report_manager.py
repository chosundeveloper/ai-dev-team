"""Manage agent reports and user responses."""
import argparse
import json
from pathlib import Path
from typing import List

REPORT_PATH = Path("reports/log.jsonl")


class ReportStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _load(self) -> List[dict]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]

    def _save(self, items: List[dict]) -> None:
        with self.path.open("w", encoding="utf-8") as handle:
            for item in items:
                handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    def list(self, status: str = None) -> List[dict]:
        items = self._load()
        if status:
            return [item for item in items if item.get("status") == status]
        return items

    def respond(self, entry_id: str, status: str, feedback: str) -> bool:
        items = self._load()
        updated = False
        for item in items:
            if item["id"] == entry_id:
                item["status"] = status
                item["user_feedback"] = feedback or ""
                updated = True
                break
        if updated:
            self._save(items)
        return updated


def cmd_list(args: argparse.Namespace) -> None:
    store = ReportStore(REPORT_PATH)
    entries = store.list(status=args.status)
    if not entries:
        print("(no entries)")
        return
    for entry in entries:
        print("=" * 60)
        print(f"ID: {entry['id']}")
        print(f"Timestamp: {entry['timestamp']}")
        print(f"Agent: {entry['agent']}")
        print(f"Status: {entry['status']}")
        print(f"Order: {entry['order']}")
        print(f"Response:\n{entry['response']}")
        if entry.get("user_feedback"):
            print(f"Feedback: {entry['user_feedback']}")
    print("=" * 60)


def cmd_respond(args: argparse.Namespace) -> None:
    store = ReportStore(REPORT_PATH)
    ok = store.respond(args.id, args.status, args.feedback)
    if not ok:
        raise SystemExit("❗️ 해당 ID를 찾을 수 없습니다.")
    print(f"✅ Report {args.id} → {args.status}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Agent report manager")
    sub = parser.add_subparsers(dest="command", required=True)

    list_cmd = sub.add_parser("list", help="보고 목록 확인")
    list_cmd.add_argument("--status", choices=["pending", "approved", "needs_changes"], help="특정 상태만 보기")
    list_cmd.set_defaults(func=cmd_list)

    respond_cmd = sub.add_parser("respond", help="보고에 대한 피드백 남기기")
    respond_cmd.add_argument("--id", required=True, help="보고 ID")
    respond_cmd.add_argument("--status", required=True, choices=["approved", "needs_changes"], help="응답 상태")
    respond_cmd.add_argument("--feedback", help="추가 코멘트")
    respond_cmd.set_defaults(func=cmd_respond)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
