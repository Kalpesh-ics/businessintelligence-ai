import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# =========================================================
# PATH SETUP
# =========================================================
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if ROOT not in sys.path:
    sys.path.append(ROOT)

from engine.core import KPIEngine


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="BusinessIntelligence.ai",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown(
    """
    <style>

    .stApp {
        background-color: #F7F8FC;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: #F9FAFB !important;
    }

    .brand {
        font-size: 26px;
        font-weight: 750;
        color: #FFFFFF;
    }

    .brand-sub {
        color: #9CA3AF;
        font-size: 13px;
        margin-bottom: 20px;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #111827;
        letter-spacing: -1.5px;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #667085;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .welcome-box {
        background: linear-gradient(135deg, #111827, #253047);
        padding: 36px;
        border-radius: 20px;
        color: white;
        margin-bottom: 28px;
    }

    .welcome-title {
        font-size: 32px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    .welcome-text {
        color: #D1D5DB;
        font-size: 16px;
        line-height: 1.6;
        max-width: 900px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 750;
        color: #111827;
        margin-top: 28px;
        margin-bottom: 15px;
    }

    .kpi-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 20px;
        min-height: 145px;
        box-shadow: 0 2px 10px rgba(16, 24, 40, 0.04);
    }

    .kpi-name {
        color: #667085;
        font-size: 14px;
        font-weight: 600;
    }

    .kpi-value {
        color: #111827;
        font-size: 29px;
        font-weight: 800;
        margin-top: 5px;
    }

    .danger {
        color: #DC2626;
        font-weight: 700;
        margin-top: 7px;
    }

    .warning {
        color: #D97706;
        font-weight: 700;
        margin-top: 7px;
    }

    .success {
        color: #059669;
        font-weight: 700;
        margin-top: 7px;
    }

    .alert-card {
        background: white;
        border-left: 5px solid #DC2626;
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(16, 24, 40, 0.04);
    }

    .alert-title {
        color: #111827;
        font-weight: 750;
        font-size: 16px;
    }

    .alert-text {
        color: #667085;
        margin-top: 5px;
        line-height: 1.5;
    }

    .insight-box {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 3px 12px rgba(16, 24, 40, 0.05);
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        color: #98A2B3;
        font-size: 13px;
        padding-top: 45px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# ENGINE
# =========================================================
if "engine" not in st.session_state:
    st.session_state.engine = KPIEngine()

engine = st.session_state.engine


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown(
    '<div class="brand">BusinessIntelligence.ai</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="brand-sub">Intelligence-to-Action Platform</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "KPI Intelligence",
        "Decision Workspace",
        "Evidence & Lineage",
        "Governance & Telemetry"
    ]
)

st.sidebar.markdown("---")

persona = st.sidebar.selectbox(
    "VIEW AS",
    ["CEO", "Sales Manager", "Analyst"]
)

st.sidebar.markdown("---")

st.sidebar.caption("Prototype")
st.sidebar.caption("Synthetic enterprise data")


# =========================================================
# HEADER
# =========================================================
st.markdown(
    '<div class="main-title">BusinessIntelligence.ai</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered KPI Intelligence-to-Action Engine</div>',
    unsafe_allow_html=True
)


# =========================================================
# OVERVIEW
# =========================================================
if page == "Overview":

    st.markdown(
        """
        <div class="welcome-box">
            <div class="welcome-title">
                Welcome to your Business Intelligence Command Center
            </div>

            <div class="welcome-text">
                Monitor how your business is performing, understand what changed,
                investigate the evidence behind KPI movements, and turn insights
                into practical actions.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Business Health — Current Snapshot</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(5)

    kpis = [
        ("Revenue", "$91.8M", "↓ 8.2%", "danger"),
        ("Units Sold", "842K", "↓ 5.4%", "warning"),
        ("Average Price", "$109.0", "↓ 1.7%", "warning"),
        ("Retention", "91.4%", "↓ 3.1%", "warning"),
        ("Fulfilment SLA", "76%", "↓ 15 pts", "danger"),
    ]

    for col, (name, value, change, level) in zip(cols, kpis):
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-name">{name}</div>
                    <div class="kpi-value">{value}</div>
                    <div class="{level}">{change} vs baseline</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">Material Movements Requiring Attention</div>',
        unsafe_allow_html=True
    )

    alerts = [
        (
            "Revenue — US-West",
            "Revenue is 8.2% below baseline. Product A volume is the largest quantified contributor."
        ),
        (
            "Fulfilment SLA",
            "SLA has fallen 15 percentage points and coincides with increased Product A support activity."
        ),
        (
            "Customer Retention",
            "Enterprise retention is trending below baseline and may increase renewal risk."
        )
    ]

    for title, text in alerts:
        st.markdown(
            f"""
            <div class="alert-card">
                <div class="alert-title">{title}</div>
                <div class="alert-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">Explore BusinessIntelligence.ai</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            "**KPI Intelligence**\n\n"
            "Investigate material movements and identify likely drivers."
        )

    with c2:
        st.info(
            "**Decision Workspace**\n\n"
            "Turn evidence into practical actions with owners and monitoring."
        )

    with c3:
        st.info(
            "**Governance & Telemetry**\n\n"
            "Inspect lineage, freshness, security and runtime behaviour."
        )


# =========================================================
# KPI INTELLIGENCE
# =========================================================
elif page == "KPI Intelligence":

    st.markdown(
        '<div class="section-title">KPI Intelligence</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Choose an investigation to see how the engine moves from "
        "KPI movement → evidence → confidence → action."
    )

    scenario = st.selectbox(
        "Select Investigation",
        [
            "Multi-factor Revenue Movement",
            "Low Confidence / Abstention",
            "Sparse History / New KPI"
        ]
    )

    # -----------------------------------------------------
    # SCENARIO 1
    # -----------------------------------------------------
    if scenario == "Multi-factor Revenue Movement":

        st.subheader("US-West Revenue")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Current Revenue", "$91.8M", "-8.2%")
        c2.metric("Baseline", "$100.0M")
        c3.metric("Business Impact", "$8.2M")
        c4.metric("Materiality", "HIGH")

        st.markdown("### 1. Detect Material Movement")

        baseline = [
            101200, 99800, 100500, 102100, 99500,
            100800, 101400, 99700, 100200, 101100,
            99600, 100900, 101300, 99800, 100700,
            101500, 100100, 99500, 100600, 101200,
            100400, 99800, 100900, 101100, 100300,
            101000, 99700, 100800, 101400, 100500
        ]

        mat = engine.detect_materiality(
            91800,
            baseline
        )

        st.success(
            f"Detection method: {mat['method']}"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Deviation",
            f"{mat['pct_change']:.1%}"
        )

        c2.metric(
            "Z-score",
            f"{mat['z_score']:.2f}"
        )

        c3.metric(
            "Material Movement",
            "YES" if mat["is_material"] else "NO"
        )

        st.markdown("### 2. Driver Contribution")

        contribution = pd.DataFrame(
            {
                "Driver": [
                    "Product A Volume",
                    "Enterprise Customer Decline",
                    "Price",
                    "Other / Offset"
                ],
                "Contribution": [45, 29, 13, 13]
            }
        )

        st.bar_chart(
            contribution.set_index("Driver")
        )

        st.caption(
            "Contribution is calculated before the LLM narrative layer."
        )

        st.markdown("### 3. Supporting Evidence")

        evidence = engine.retrieve_unstructured_evidence(
            "Enterprise Cloud Hosting"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Support Tickets**")
            st.info(
                "300% spike in outage and latency tags in US-West data centers."
            )

        with col2:
            st.markdown("**CRM Notes**")
            st.info(
                "Major enterprise accounts are threatening non-renewal over missed uptime SLAs."
            )

        st.markdown("### 4. Confidence")

        confidence = engine.determine_confidence(
            0.7,
            evidence
        )

        if "HIGH" in confidence:
            st.success("HIGH CONFIDENCE")
        elif "MEDIUM" in confidence:
            st.warning("MEDIUM CONFIDENCE")
        else:
            st.error("LOW CONFIDENCE")

        st.markdown("### 5. Business Narrative")

        narrative = engine.generate_narrative(
            persona,
            mat,
            confidence
        )

        st.markdown(
            f"""
            <div class="insight-box">
                {narrative}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            "Evidence → Analysis → Confidence → Narrative"
        )

    # -----------------------------------------------------
    # SCENARIO 2
    # -----------------------------------------------------
    elif scenario == "Low Confidence / Abstention":

        st.subheader("Q3 Marketing ROI")

        c1, c2, c3 = st.columns(3)

        c1.metric("ROI Movement", "-12.4%")
        c2.metric("Data Completeness", "62%")
        c3.metric("Confidence", "LOW")

        st.markdown("### Evidence Conflict")

        st.warning(
            "Google Ads API data and Salesforce attribution are currently out of sync."
        )

        st.markdown("### Engine Decision")

        st.error(
            "ABSTAIN — A causal root cause cannot be established from the available evidence."
        )

        st.markdown(
            """
            <div class="insight-box">
                <b>Why the engine abstains</b><br><br>
                Multiple signals are present, but critical attribution data is
                incomplete or contradictory.<br><br>

                <b>Recommended next step</b><br>
                Restore the attribution pipeline and validate channel-level
                conversion data before taking corrective action.
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # SCENARIO 3
    # -----------------------------------------------------
    else:

        st.subheader("New Product — AI Data Center Nodes")

        c1, c2, c3 = st.columns(3)

        c1.metric("Weekly Active Users", "480")
        c2.metric("Historical Observations", "5")
        c3.metric("Confidence", "LOW")

        baseline = [500, 520, 510, 540, 530]

        mat = engine.detect_materiality(
            480,
            baseline
        )

        st.markdown("### Method Selection")

        st.warning(
            "Sparse history detected — conventional long-term anomaly detection is unreliable."
        )

        st.markdown(
            f"""
            <div class="insight-box">
                <b>Selected analytical method</b><br><br>
                {mat['method']}<br><br>

                The engine switches methodology because this KPI has
                insufficient historical observations to establish a stable
                baseline.
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# DECISION WORKSPACE
# =========================================================
elif page == "Decision Workspace":

    st.markdown(
        '<div class="section-title">Decision Workspace</div>',
        unsafe_allow_html=True
    )

    st.write(
        f"Recommendations are tailored for the selected persona: **{persona}**"
    )

    if persona == "CEO":

        st.markdown(
            """
            <div class="insight-box">

            <h3>Executive Decision Brief</h3>

            <b>Situation</b><br>
            US-West revenue is materially below baseline.

            <br><br>

            <b>Primary quantified contributor</b><br>
            Product A enterprise volume decline.

            <br><br>

            <b>Evidence</b><br>
            Fulfilment SLA deterioration and increased support activity
            coincide with the decline.

            <br><br>

            <b>Decision Focus</b><br>
            Protect enterprise revenue while validating the operational
            root cause.

            <br><br>

            <b>Confidence</b><br>
            Medium for the operational explanation; causality not established.

            </div>
            """,
            unsafe_allow_html=True
        )

    elif persona == "Sales Manager":

        st.markdown(
            """
            <div class="insight-box">

            <h3>Sales Action Plan</h3>

            <b>Driver</b><br>
            Product A enterprise volume decline.

            <br><br>

            <b>Lever</b><br>
            Enterprise retention.

            <br><br>

            <b>Action</b><br>
            Prioritise at-risk enterprise accounts for proactive recovery
            outreach and coordinate with Customer Success.

            <br><br>

            <b>Owner</b><br>
            Regional Sales + Customer Success.

            <br><br>

            <b>Monitoring</b><br>
            Track enterprise order volume, renewal probability and support
            activity weekly.

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="insight-box">

            <h3>Analyst Investigation</h3>

            <b>Primary quantified contributor:</b>
            Product A volume.

            <br><br>

            <b>Supporting signals:</b>
            Fulfilment SLA deterioration, support-ticket increase and
            enterprise retention risk.

            <br><br>

            <b>Analytical limitation:</b>
            Current evidence supports contribution and association but does
            not establish causal certainty.

            <br><br>

            <b>Next analysis:</b>
            Compare affected and unaffected regions using a causal design
            when sufficient historical data becomes available.

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# EVIDENCE & LINEAGE
# =========================================================
elif page == "Evidence & Lineage":

    st.markdown(
        '<div class="section-title">Evidence & Lineage</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Trace every insight back to its sources, freshness and analytical method."
    )

    evidence_table = pd.DataFrame(
        {
            "Evidence": [
                "Regional Revenue",
                "CRM Account Risk",
                "Support Tickets",
                "Fulfilment SLA"
            ],
            "Source": [
                "Sales / ERP",
                "CRM",
                "Customer Support",
                "Operations"
            ],
            "Freshness": [
                "2 hours ago",
                "4 hours ago",
                "15 minutes ago",
                "30 minutes ago"
            ],
            "Role": [
                "Quantitative KPI",
                "Customer context",
                "Unstructured signal",
                "Operational signal"
            ]
        }
    )

    st.dataframe(
        evidence_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### KPI Lineage")

    st.code(
        """
ERP / Sales
      ↓
Enterprise Warehouse
      ↓
Governed KPI Layer
      ↓
Materiality Detection
      ↓
Contribution Analysis
      ↓
Evidence Retrieval
      ↓
Confidence Assessment
      ↓
Narrative + Recommendation
        """,
        language="text"
    )

    st.markdown("### Evidence Classification")

    evidence_classes = pd.DataFrame(
        {
            "Classification": [
                "Observed Fact",
                "Measured Contribution",
                "Association",
                "Likely Driver",
                "Causal Evidence",
                "Unconfirmed Hypothesis"
            ],
            "Meaning": [
                "Direct business measurement",
                "Quantified KPI contribution",
                "Variables moved together",
                "Evidence supports explanation",
                "Stronger causal method available",
                "Plausible but insufficiently supported"
            ]
        }
    )

    st.dataframe(
        evidence_classes,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# GOVERNANCE & TELEMETRY
# =========================================================
else:

    st.markdown(
        '<div class="section-title">Governance & Telemetry</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Role-Based Access")

    security = pd.DataFrame(
        {
            "Persona": [
                "CEO",
                "Sales Manager",
                "Analyst"
            ],
            "Access Scope": [
                "Aggregate business metrics",
                "Regional + customer context",
                "Detailed analytical evidence"
            ],
            "Sensitive Data": [
                "Restricted",
                "Role dependent",
                "Authorized analytical access"
            ]
        }
    )

    st.dataframe(
        security,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Runtime Telemetry")

    telemetry = engine.telemetry

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Latency",
        f"{telemetry['latency_ms']} ms"
    )

    c2.metric(
        "LLM Calls",
        telemetry["llm_calls"]
    )

    c3.metric(
        "Tokens Used",
        telemetry["tokens_used"]
    )

    c4.metric(
        "Estimated Cost",
        f"${telemetry['est_cost_usd']:.4f}"
    )

    st.markdown("### LLM vs Non-LLM")

    processing = pd.DataFrame(
        {
            "Processing Step": [
                "KPI Calculation",
                "Materiality Detection",
                "Contribution Analysis",
                "Evidence Retrieval",
                "Narrative",
                "Recommendation"
            ],
            "Primary Technology": [
                "Deterministic",
                "Statistics + Rules",
                "Deterministic Analytics",
                "Retrieval",
                "LLM",
                "Rules + LLM"
            ]
        }
    )

    st.dataframe(
        processing,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Analyst Feedback")

    feedback = st.selectbox(
        "How useful was this insight?",
        [
            "Useful",
            "Partially useful",
            "Incorrect driver",
            "Missing evidence",
            "Wrong confidence"
        ]
    )

    if st.button("Submit Feedback"):
        st.success(
            f"Feedback captured: {feedback}"
        )

        st.caption(
            "Production implementation would use this feedback for evaluation, "
            "confidence calibration and analyst-review workflows."
        )


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        BusinessIntelligence.ai · Round 2 Prototype · Synthetic Data
        · Evidence before explanation
    </div>
    """,
    unsafe_allow_html=True
)
