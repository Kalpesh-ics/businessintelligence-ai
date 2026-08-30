import streamlit as st
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.core import KPIEngine

st.set_page_config(page_title="BusinessIntelligence.ai", layout="wide")
engine = KPIEngine()

st.title("BusinessIntelligence.ai: Intelligence-to-Action")
persona = st.sidebar.selectbox("Simulate Persona", ["CEO", "Sales Manager", "Analyst"])
scenario = st.sidebar.radio("Demo Scenario", [
    "1. Multi-factor Movement (Revenue Drop)", 
    "2. Low Confidence (Missing API Data)", 
    "3. Sparse History (New Feature Launch)"
])

if "1" in scenario:
    st.subheader("US-West Region Revenue: -8.2%")
    if st.button("Explain this movement"):
        baseline = np.random.normal(100000, 5000, 30)
        mat = engine.detect_materiality(91800, baseline)
        evidence = engine.retrieve_unstructured_evidence("Enterprise Cloud Hosting")
        conf = engine.determine_confidence(0.7, evidence)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Deviation vs Baseline", f"{mat['pct_change']:.1%}")
        col2.metric("Detection Method", mat['method'])
        col3.metric("Evidence Confidence", conf)
        
        st.info(engine.generate_narrative(persona, mat, conf))
        st.write("**Traceable Evidence (CRM & Support):**")
        st.json(evidence)

elif "2" in scenario:
    st.subheader("Q3 Marketing ROI: -12.4%")
    if st.button("Analyze ROI"):
        st.error(engine.generate_narrative(persona, {}, engine.determine_confidence(0.2, [])))

elif "3" in scenario:
    st.subheader("New Product: AI Data Center Nodes (Weekly Active Users)")
    if st.button("Analyze Adoption"):
        baseline = [500, 520, 510, 540, 530]
        mat = engine.detect_materiality(480, baseline)
        st.warning(f"**Method Switch:** {mat['method']} triggered due to insufficient KPI history (<14 days of data).")

st.sidebar.json(engine.telemetry)
