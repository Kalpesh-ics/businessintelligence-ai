from __future__ import annotations
import os,time
try:
    import streamlit as st
except ImportError:
    st=None
from openai import OpenAI

MODEL_DEFAULT="gpt-5.6-luna"; INPUT_PRICE_PER_MTOK=0.20; OUTPUT_PRICE_PER_MTOK=1.20
SYSTEM_INSTRUCTIONS='''You are BI.ai, the business intelligence copilot inside BusinessIntelligence.ai. Answer using ONLY the supplied current application context. Never invent KPI values, percentages, dollar impacts, drivers, sources, freshness, constraints, owners, or telemetry. Quantitative values come from the deterministic engine. Distinguish measured contribution, association, likely driver and causal evidence. Do not claim causality when the context does not establish it. For Marketing ROI, explicitly abstain from a causal root cause because Google Ads and Salesforce attribution conflict. Respect budget, discount, ownership and decision-authority constraints. Adapt to the persona: CEO = strategic and concise; Sales Manager = action/owner/monitoring; Analyst = methods/evidence/limitations. If the answer is not supported by context, say you do not have enough evidence in the current prototype context. Do not present synthetic evidence as production data. Keep answers practical and concise.'''

def _secret(name):
    if st is not None:
        try:
            v=st.secrets.get(name,"")
            if v:return str(v)
        except Exception: pass
    return os.getenv(name,"")

def get_model(): return _secret("OPENAI_MODEL") or os.getenv("OPENAI_MODEL",MODEL_DEFAULT)
def has_api_key(): return bool(_secret("OPENAI_API_KEY"))

def ask_bi(question,context):
    key=_secret("OPENAI_API_KEY")
    if not key:return {"answer":"","status":"missing_key","latency_ms":0,"usage":{"input_tokens":0,"output_tokens":0,"total_tokens":0},"model":get_model(),"cost_usd":0.0,"error":"OPENAI_API_KEY is not configured. Add it in Streamlit Cloud Secrets or your local environment."}
    started=time.perf_counter()
    try:
        response=OpenAI(api_key=key).responses.create(model=get_model(),instructions=SYSTEM_INSTRUCTIONS,input="CURRENT BUSINESS CONTEXT\n"+context+"\n\nUSER QUESTION\n"+question.strip())
        latency=int((time.perf_counter()-started)*1000); u=getattr(response,"usage",None); inp=int(getattr(u,"input_tokens",0) or 0); out=int(getattr(u,"output_tokens",0) or 0); total=int(getattr(u,"total_tokens",inp+out) or (inp+out)); cost=(inp/1_000_000)*INPUT_PRICE_PER_MTOK+(out/1_000_000)*OUTPUT_PRICE_PER_MTOK
        return {"answer":(getattr(response,"output_text","") or "").strip(),"status":"success","latency_ms":latency,"usage":{"input_tokens":inp,"output_tokens":out,"total_tokens":total},"model":get_model(),"cost_usd":cost,"error":""}
    except Exception as e:
        return {"answer":"","status":"error","latency_ms":int((time.perf_counter()-started)*1000),"usage":{"input_tokens":0,"output_tokens":0,"total_tokens":0},"model":get_model(),"cost_usd":0.0,"error":str(e)}

def apply_telemetry(engine,result):
    if result.get("status") in {"success","error"}: engine.telemetry.llm_calls+=1
    u=result.get("usage",{}); engine.telemetry.input_tokens+=int(u.get("input_tokens",0)); engine.telemetry.output_tokens+=int(u.get("output_tokens",0)); engine.telemetry.total_tokens+=int(u.get("total_tokens",0)); engine.telemetry.estimated_llm_cost_usd+=float(result.get("cost_usd",0.0)); engine.telemetry.last_llm_latency_ms=int(result.get("latency_ms",0)); engine.telemetry.last_llm_status=str(result.get("status","unknown"))
