#!/usr/bin/env python3
"""
AI Dev Team API Server
FastAPI-based web server for LangGraph multi-agent system
"""
import os
from datetime import datetime
from threading import Lock
from typing import Dict, Any, List
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

from langgraph.graph import StateGraph, END
from state import AgentState
from agents.market_research import market_research_agent
from agents.competitive_analysis import competitive_analysis_agent
from agents.idea_generator import idea_generator_agent
from agents.evaluator import evaluator_agent
from agents.pm import pm_agent
from llm_factory import build_chat_model
from agents.utils import log_agent_event

# Load environment variables
load_dotenv()

app = FastAPI(
    title="AI Dev Team API",
    description="LangGraph-powered multi-agent system for website planning",
    version="1.0.0"
)


comment_lock = Lock()
comment_queue: List[Dict[str, Any]] = []


def _list_comments() -> List[Dict[str, str]]:
    with comment_lock:
        return list(comment_queue)

# Serve static files (HTML, CSS, JS)
if Path("deliverables").exists():
    app.mount("/deliverables", StaticFiles(directory="deliverables"), name="deliverables")

# Models
class PlanRequest(BaseModel):
    user_input: str
    constraints: str = ""
    idea_details: str = ""

class AgentLogModel(BaseModel):
    agent: str
    role: str
    event: str
    message: str
    timestamp: str


class PlanResponse(BaseModel):
    success: bool
    plan: str
    steps: Dict[str, Any]
    logs: List[AgentLogModel]

class ReadmeRequest(BaseModel):
    github_url: str

class ReadmeResponse(BaseModel):
    success: bool
    readme: str
    error: str = ""


class CommentRequest(BaseModel):
    message: str

# Routes
@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main portfolio page"""
    index_file = Path("index.html")
    if index_file.exists():
        return FileResponse(index_file)

    return HTMLResponse("""
    <html>
        <head><title>AI Dev Team</title></head>
        <body>
            <h1>🤖 AI Dev Team - LangGraph Multi-Agent System</h1>
            <p>Welcome to the AI Development Team API!</p>
            <ul>
                <li><a href="/docs">API Documentation</a></li>
                <li><a href="/team">Team Portfolio</a></li>
                <li><a href="/health">Health Check</a></li>
            </ul>
        </body>
    </html>
    """)

@app.get("/team", response_class=HTMLResponse)
async def team_portfolio():
    """Serve the team portfolio page"""
    portfolio_file = Path("team_portfolio.html")
    if portfolio_file.exists():
        return FileResponse(portfolio_file)
    raise HTTPException(status_code=404, detail="Team portfolio not found")


@app.get("/dashboard", response_class=HTMLResponse)
async def conversation_dashboard():
    """Serve the live agent dashboard"""
    dashboard_file = Path("agent_dashboard.html")
    if dashboard_file.exists():
        return FileResponse(dashboard_file)
    raise HTTPException(status_code=404, detail="Agent dashboard not found")


@app.get("/calculators", response_class=HTMLResponse)
async def calculator_hub():
    """Serve the calculator hub landing page"""
    calc_file = Path("deliverables/calculator_hub.html")
    if calc_file.exists():
        return FileResponse(calc_file)
    raise HTTPException(status_code=404, detail="Calculator hub not found")


@app.get("/lunch", response_class=HTMLResponse)
async def lunch_roulette():
    """Serve the lunch roulette mini tool"""
    lunch_file = Path("deliverables/lunch_roulette.html")
    if lunch_file.exists():
        return FileResponse(lunch_file)
    raise HTTPException(status_code=404, detail="Lunch roulette not found")

@app.get("/health")
async def health_check():
    """Health check endpoint for Fly.io"""
    return {
        "status": "healthy",
        "service": "ai-dev-team",
        "llm_provider": os.getenv("LLM_PROVIDER", "groq"),
        "version": "1.0.0"
    }

@app.post("/api/plan", response_model=PlanResponse)
async def create_plan(request: PlanRequest):
    """
    Generate a website plan using the AI agent team
    """
    try:
        # Create workflow
        llm = build_chat_model(role="creative")
        workflow = StateGraph(AgentState)

        workflow.add_node("market_research", lambda state: market_research_agent(state, llm))
        workflow.add_node("competitive_analysis", lambda state: competitive_analysis_agent(state, llm))
        workflow.add_node("idea_generator", lambda state: idea_generator_agent(state, llm))
        workflow.add_node("evaluator", lambda state: evaluator_agent(state, llm))
        workflow.add_node("pm", lambda state: pm_agent(state, llm))

        # Define workflow
        workflow.set_entry_point("market_research")
        workflow.add_edge("market_research", "competitive_analysis")
        workflow.add_edge("competitive_analysis", "idea_generator")
        workflow.add_edge("idea_generator", "evaluator")
        workflow.add_edge("evaluator", "pm")
        workflow.add_edge("pm", END)

        # Compile and run
        app_workflow = workflow.compile()

        with comment_lock:
            pending_comments = [dict(comment) for comment in comment_queue]
            comment_queue.clear()

        initial_state: AgentState = {
            "user_input": request.user_input,
            "constraints": request.constraints,
            "idea_details": request.idea_details,
            "market_trends": "",
            "popular_keywords": [],
            "competitor_analysis": "",
            "differentiation_points": [],
            "ideas": [],
            "evaluations": [],
            "final_plan": "",
            "iteration_count": 0,
            "needs_improvement": False,
            "conversation_logs": [],
            "user_comments": pending_comments
        }

        for comment in pending_comments:
            log_agent_event(
                initial_state,
                agent="User",
                role="user",
                event="info",
                message=comment["message"],
            )

        result = app_workflow.invoke(initial_state)

        return PlanResponse(
            success=True,
            plan=result.get("final_plan", ""),
            steps={
                "idea_details": result.get("idea_details", ""),
                "market_trends": result.get("market_trends", ""),
                "popular_keywords": result.get("popular_keywords", []),
                "competitor_analysis": result.get("competitor_analysis", ""),
                "differentiation_points": result.get("differentiation_points", []),
                "ideas": result.get("ideas", []),
                "evaluations": result.get("evaluations", [])
            },
            logs=result.get("conversation_logs", [])
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Planning failed: {str(e)}")

@app.get("/api/status")
async def agent_status():
    """Get current agent team status"""
    return {
        "agents": [
            {"name": "Alex", "role": "PM", "model": "Llama 3.3 70B (Groq)", "status": "active"},
            {"name": "Maya", "role": "Designer", "model": "Llama 3.3 70B (Groq)", "status": "active"},
            {"name": "Chris", "role": "Frontend", "model": "Llama 3.3 70B (Groq)", "status": "active"},
            {"name": "Jordan", "role": "Backend", "model": "Mixtral 8x7B (Groq)", "status": "active"},
            {"name": "Sam", "role": "Researcher", "model": "Llama 3.3 70B (Groq)", "status": "active"}
        ],
        "llm_provider": os.getenv("LLM_PROVIDER", "groq"),
        "deployment": "fly.io"
    }


@app.get("/api/comments")
async def get_comments():
    """Return queued user comments"""
    return {"comments": _list_comments()}


@app.post("/api/comments")
async def add_comment(request: CommentRequest):
    """Add a new user comment so agents can see it"""
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Comment message cannot be empty")

    comment = {
        "message": message,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "assigned_to": []
    }
    with comment_lock:
        comment_queue.append(comment)

    return {"success": True, "comment": comment}

@app.get("/readme-gen", response_class=HTMLResponse)
async def readme_generator_page():
    """Serve the README Generator page"""
    readme_page = Path("readme_generator.html")
    if readme_page.exists():
        return FileResponse(readme_page)
    raise HTTPException(status_code=404, detail="README Generator page not found")

@app.post("/api/readme", response_model=ReadmeResponse)
async def generate_readme(request: ReadmeRequest):
    """
    Generate a professional README.md from a GitHub repository URL
    """
    try:
        import re
        from langchain_core.prompts import ChatPromptTemplate

        # Validate GitHub URL
        github_pattern = r'https?://github\.com/[\w-]+/[\w-]+'
        if not re.match(github_pattern, request.github_url):
            return ReadmeResponse(
                success=False,
                readme="",
                error="Invalid GitHub URL. Please provide a valid GitHub repository URL."
            )

        # Extract owner/repo
        parts = request.github_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]

        # Build LLM
        llm = build_chat_model(role="creative")

        # Create prompt for README generation
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert technical writer who creates professional, comprehensive README files.

Given a GitHub repository URL, create a high-quality README.md that includes:
1. Project title and description
2. Key features (bullet points)
3. Installation instructions
4. Usage examples
5. API documentation (if applicable)
6. Contributing guidelines
7. License information
8. Badges (build status, version, license)

Format the output in proper Markdown. Be professional, clear, and comprehensive."""),
            ("human", """Create a professional README.md for this GitHub repository:

Repository: {owner}/{repo}
URL: {url}

Analyze what this project likely does based on the name and create a comprehensive, well-structured README.md file.""")
        ])

        # Generate README
        chain = prompt | llm
        result = chain.invoke({
            "owner": owner,
            "repo": repo,
            "url": request.github_url
        })

        readme_content = result.content if hasattr(result, 'content') else str(result)

        return ReadmeResponse(
            success=True,
            readme=readme_content,
            error=""
        )

    except Exception as e:
        return ReadmeResponse(
            success=False,
            readme="",
            error=f"Failed to generate README: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
