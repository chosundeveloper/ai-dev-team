"""Generate meeting summaries from agent reports."""
import argparse
from datetime import datetime
from pathlib import Path
from typing import List
import json

REPORT_PATH = Path("reports/log.jsonl")
MEETING_DIR = Path("meetings")


class ReportStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> List[dict]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]


def assemble_meeting(meeting_title: str, notes: str, status_filter: str) -> Path:
    store = ReportStore(REPORT_PATH)
    reports = store.load()
    if status_filter:
        reports = [r for r in reports if r.get("status") == status_filter]
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    MEETING_DIR.mkdir(parents=True, exist_ok=True)
    meeting_file = MEETING_DIR / f"meeting-{timestamp}.md"

    lines = [f"# {meeting_title or 'AI Team Sync'}", "", f"_UTC {timestamp}_", ""]
    if notes:
        lines.extend(["## Notes", notes, ""])

    if not reports:
        lines.append("(No reports included.)")
    else:
        lines.append("## Reports Reviewed")
        for rep in reports:
            lines.extend([
                "---",
                f"**ID:** {rep['id']}",
                f"**Agent:** {rep['agent']}",
                f"**Status:** {rep.get('status', 'unknown')}",
                f"**Order:** {rep['order']}",
                f"**Response:**\n{rep['response']}",
                f"**Feedback:** {rep.get('user_feedback') or '-'}",
                "",
            ])
    meeting_file.write_text("\n".join(lines), encoding="utf-8")
    return meeting_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Meeting report generator")
    parser.add_argument("--title", help="회의 제목")
    parser.add_argument("--notes", help="간단한 메모")
    parser.add_argument(
        "--status", choices=["pending", "approved", "needs_changes"], help="특정 상태만 포함"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    meeting_file = assemble_meeting(args.title, args.notes, args.status)
    print(f"📄 Meeting summary saved to {meeting_file}")


if __name__ == "__main__":
    main()
