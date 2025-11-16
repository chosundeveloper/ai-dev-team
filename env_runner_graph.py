"""LangGraph workflow that includes an EnvironmentRunnerAgent.

EnvironmentRunnerAgent responsibilities
- Activate (or create) Python virtual environment
- Install requirements
- Run FastAPI server via uvicorn
- Log each step status
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any

from langgraph.graph import StateGraph, END
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables import RunnableLambda

PROJECT_ROOT = Path("/Users/john/projects/langGraph")
VENV_DIR = PROJECT_ROOT / "venv"
SCENARIO_FILE = PROJECT_ROOT / "ops_scenario.json"
LOG_FILE = PROJECT_ROOT / "env_runner.log"


def run_shell(cmd: str) -> str:
    """Execute shell command and return stdout/stderr."""
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    stdout, _ = proc.communicate()
    return stdout


def ensure_venv() -> str:
    if not VENV_DIR.exists():
        return run_shell(f"cd {PROJECT_ROOT} && python3 -m venv venv")
    return "venv already exists"


def venv_python() -> str:
    if sys.platform == "win32":
        return str(VENV_DIR / "Scripts" / "python")
    return str(VENV_DIR / "bin" / "python")


def pip_install_requirements() -> str:
    req = PROJECT_ROOT / "requirements.txt"
    if not req.exists():
        return "requirements.txt not found"
    python_bin = venv_python()
    return run_shell(f"cd {PROJECT_ROOT} && {python_bin} -m pip install --upgrade pip && "
                     f"{python_bin} -m pip install -r requirements.txt")


def start_uvicorn() -> str:
    python_bin = venv_python()
    run_shell("pkill -f 'uvicorn app:app' || true")
    return run_shell(
        f"cd {PROJECT_ROOT} && nohup {python_bin} -m uvicorn app:app --host 127.0.0.1 --port 8000 "
        ">/tmp/env_runner_uvicorn.log 2>&1 &"
    )


def check_process() -> str:
    return run_shell("ps aux | grep 'uvicorn app:app' | grep -v grep")


def log(message: str) -> None:
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{message}\n")


def environment_runner_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    steps = []
    steps.append("=== EnvironmentRunnerAgent started ===")
    steps.append(ensure_venv())
    steps.append(pip_install_requirements())
    steps.append(start_uvicorn())
    steps.append(check_process())
    log("\n".join(steps))
    state["runner_logs"] = "\n".join(steps)
    state["runner_status"] = "completed"
    return state


def manager_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    if state.get("runner_status") != "completed":
        state["manager_message"] = "Ops agent 실행이 필요합니다."
        state["next"] = "env_runner"
    else:
        state["manager_message"] = "환경이 이미 실행된 상태입니다."
        state["next"] = END
    return state


def create_workflow():
    workflow = StateGraph(dict)
    workflow.add_node("manager", RunnableLambda(manager_agent))
    workflow.add_node("env_runner", RunnableLambda(environment_runner_agent))
    workflow.set_entry_point("manager")
    workflow.add_conditional_edges(
        "manager",
        lambda state: state.get("next"),
        {"env_runner": "env_runner", END: END},
    )
    workflow.add_edge("env_runner", "manager")
    workflow.add_edge("manager", END)
    return workflow.compile()


def main():
    graph = create_workflow()
    result = graph.invoke({})
    print("=== Runner Output ===")
    print(result.get("runner_logs", "(no logs)"))
    print("=== Manager Message ===")
    print(result.get("manager_message", ""))


if __name__ == "__main__":
    main()
