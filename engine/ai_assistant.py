from __future__ import annotations

import os
import time
from typing import Any, Dict

import streamlit as st
from openai import OpenAI


DEFAULT_MODEL = "gpt-5.6-luna"

# Published model prices for GPT-5.6 Luna.
INPUT_PRICE_PER_MTOK = 0.20
OUTPUT_PRICE_PER_MTOK = 1.20


SYSTEM_INSTRUCTIONS = """
You are BI.ai, the business intelligence copilot inside BusinessIntelligence.ai.

Use ONLY the current business context supplied by the application.

CORE RULES:
- Never invent numbers, percentages, dollar impacts, sources, freshness,
  owners, constraints, or metrics.
- Never recalculate quantitative values. Use the deterministic engine values.
- Never turn contribution or association into causal certainty.
- Clearly communicate uncertainty.
- If evidence is incomplete or contradictory, abstain.
- The Q3 Marketing ROI scenario is explicitly an abstention case because
  Google Ads and Salesforce attribution conflict.
- The AI Data Center Nodes scenario has sparse history and uses the
  Cross-sectional Benchmark (Sparse History) method.
- Respect budget, maximum discount, decision authority, owner and action
  compatibility.
- For CEO: focus on business impact, strategic decision and risk.
- For Sales Manager: focus on accounts, levers, owners and actions.
- For Analyst: focus on method, evidence, assumptions and limitations.
- If the context does not support the requested answer, say:
  "I don't have enough evidence in the current prototype context to answer that."
- Do not describe synthetic evidence as production data.
- Keep answers concise, practical and business-oriented.
"""


def get_secret(name: str, default: str = "") -> str:
    try:
        value = st.secrets.get(name, "")
        if value:
            return str(value)
    except Exception:
        pass
    return os.getenv(name, default)


def get_api_key() -> str:
    return get_secret("OPENAI_API_KEY", "")


def get_model() -> str:
    return get_secret("OPENAI_MODEL", DEFAULT_MODEL)


def has_api_key() -> bool:
    return bool(get_api_key())


def ask_bi(question: str, context: str) -> Dict[str, Any]:
    question = (question or "").strip()

    empty_result = {
        "answer": "",
        "status": "empty_question",
        "latency_ms": 0,
        "usage": {
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
        },
        "model": get_model(),
        "cost_usd": 0.0,
        "error": "",
    }

    if not question:
        empty_result["error"] = "Please enter a business question."
        return empty_result

    api_key = get_api_key()
    if not api_key:
        empty_result["status"] = "missing_key"
        empty_result["error"] = (
            "OPENAI_API_KEY is not configured. Add it under "
            "Streamlit Cloud → Settings → Secrets."
        )
        return empty_result

    model = get_model()

    prompt = (
        "CURRENT BUSINESS CONTEXT\n"
        "========================\n"
        f"{context}\n\n"
        "USER QUESTION\n"
        "=============\n"
        f"{question}"
    )

    try:
        client = OpenAI(api_key=api_key)
        started = time.perf_counter()

        response = client.responses.create(
            model=model,
            instructions=SYSTEM_INSTRUCTIONS,
            input=prompt,
        )

        latency_ms = int((time.perf_counter() - started) * 1000)

        usage = getattr(response, "usage", None)
        input_tokens = int(getattr(usage, "input_tokens", 0) or 0)
        output_tokens = int(getattr(usage, "output_tokens", 0) or 0)

        total_raw = getattr(usage, "total_tokens", None)
        total_tokens = (
            int(total_raw)
            if total_raw is not None
            else input_tokens + output_tokens
        )

        cost_usd = (
            input_tokens / 1_000_000 * INPUT_PRICE_PER_MTOK
            + output_tokens / 1_000_000 * OUTPUT_PRICE_PER_MTOK
        )

        answer = (getattr(response, "output_text", "") or "").strip()
        if not answer:
            answer = (
                "I could not produce a grounded answer from the current "
                "prototype context."
            )

        return {
            "answer": answer,
            "status": "success",
            "latency_ms": latency_ms,
            "usage": {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": total_tokens,
            },
            "model": model,
            "cost_usd": cost_usd,
            "error": "",
        }

    except Exception as exc:
        return {
            "answer": "",
            "status": "error",
            "latency_ms": 0,
            "usage": {
                "input_tokens": 0,
                "output_tokens": 0,
                "total_tokens": 0,
            },
            "model": model,
            "cost_usd": 0.0,
            "error": f"BI.ai request failed: {str(exc)}",
        }


def apply_telemetry(engine: Any, result: Dict[str, Any]) -> None:
    status = result.get("status", "unknown")
    usage = result.get("usage", {}) or {}

    if status in {"success", "error"}:
        engine.telemetry.llm_calls += 1

    engine.telemetry.input_tokens += int(
        usage.get("input_tokens", 0) or 0
    )
    engine.telemetry.output_tokens += int(
        usage.get("output_tokens", 0) or 0
    )
    engine.telemetry.total_tokens += int(
        usage.get("total_tokens", 0) or 0
    )

    engine.telemetry.estimated_llm_cost_usd += float(
        result.get("cost_usd", 0.0) or 0.0
    )

    engine.telemetry.last_llm_latency_ms = int(
        result.get("latency_ms", 0) or 0
    )
    engine.telemetry.last_llm_status = status
