"""Helper to build chat LLMs based on environment variables."""
import os
from functools import lru_cache
from typing import Literal

from dotenv import load_dotenv

Role = Literal["creative", "structured", "default"]


def _temperature(role: Role) -> float:
    if role == "structured":
        return float(os.getenv("LLM_TEMPERATURE_STRUCTURED", "0.2"))
    if role == "creative":
        return float(os.getenv("LLM_TEMPERATURE_CREATIVE", "0.7"))
    return float(os.getenv("LLM_TEMPERATURE", "0.5"))


@lru_cache(maxsize=None)
def build_chat_model(role: Role = "creative"):
    """Return a LangChain-compatible chat LLM for the given role."""
    load_dotenv()
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        from langchain_groq import ChatGroq

        model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        return ChatGroq(model=model, temperature=_temperature(role))

    if provider == "ollama":
        from langchain_community.chat_models import ChatOllama

        model = os.getenv("OLLAMA_MODEL", "llama3.1")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        return ChatOllama(model=model, base_url=base_url, temperature=_temperature(role))

    raise ValueError(f"지원하지 않는 LLM_PROVIDER: {provider}")
