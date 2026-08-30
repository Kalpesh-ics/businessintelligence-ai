import streamlit as st
import pandas as pd
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

/* Sidebar headings and labels */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p {
    color: #F9FAFB !important;
}

/* Navigation radio buttons */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    color: #F9FAFB !important;
}

/* Selectbox text and labels */
section[data-testid="stSidebar"] div[data-baseweb="select"] {
    color: #111827 !important;
    background-color: #FFFFFF !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] * {
    color: #111827 !important;
}

/* Selectbox dropdown */
div[data-baseweb="popover"] {
    background-color: #FFFFFF !important;
}

div[data-baseweb="popover"] * {
    color: #111827 !important;
}
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
        margin-bottom: 10px;
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

    .metric-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 22px;
        min-height: 145px;
        box-shadow: 0 2px 10px rgba(16, 24, 40, 0.04);
    }

    .metric-name {
        color: #344054;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .metric-description {
        color: #667085;
        font-size: 14px;
        line-height: 1.5;
    }

    .signal-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(16, 24, 40, 0.04);
    }

    .signal-title {
        color: #101828;
        font-size: 17px;
        font-weight: 750;
        margin-bottom: 10px;
    }

    .signal-up {
        color: #027A48;
        font-weight: 650;
    }

    .signal-down {
        color: #B42318;
        font-weight: 650;
    }

    .signal-neutral {
        color: #475467;
        font-weight: 650;
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
        "Governance & Telemetry",
        "Feedback/Comments"
    ]
)

st.sidebar.markdown("---")

persona = st.sidebar.selectbox(
    "Select Role",
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
                Monitor business performance, understand what changed,
                investigate the evidence behind KPI movements, and turn
                insights into practical actions.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # KEY BUSINESS METRICS
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Key Business Metrics</div>',
        unsafe_allow_html=True
    )

    st.write(
        "These are core metrics businesses typically monitor to understand "
        "financial, customer, commercial and operational health."
    )

    cols = st.columns(3)

    business_metrics = [
        (
            "Revenue",
            "Measures the total income generated by the business."
        ),
        (
            "Gross Margin",
            "Shows how much revenue remains after the direct cost of delivering products or services."
        ),
        (
            "Customer Retention",
            "Measures how effectively the business keeps existing customers."
        ),
        (
            "Customer Acquisition Cost",
            "Shows how much it costs to acquire a new customer."
        ),
        (
            "Conversion Rate",
            "Measures how effectively prospects move through the sales funnel."
        ),
        (
            "Fulfilment SLA",
            "Measures operational reliability against customer service commitments."
        )
    ]

    for i, (name, description) in enumerate(business_metrics):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-name">{name}</div>
                    <div class="metric-description">{description}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # HOW TO READ THE METRICS
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Key Business Signals</div>',
        unsafe_allow_html=True
    )

    signals = [
        (
            "Revenue",
            "Higher revenue generally indicates stronger business income.",
            "Higher → positive",
            "Lower → potential revenue pressure"
        ),
        (
            "Gross Margin",
            "Higher margin generally indicates stronger profitability.",
            "Higher → better profitability",
            "Lower → margin pressure"
        ),
        (
            "Customer Retention",
            "Higher retention means fewer customers are leaving.",
            "Higher → lower churn risk",
            "Lower → higher churn risk"
        ),
        (
            "Customer Acquisition Cost",
            "Lower acquisition cost generally means customers are being acquired more efficiently.",
            "Lower → better acquisition efficiency",
            "Higher → acquisition becoming more expensive"
        ),
        (
            "Conversion Rate",
            "Higher conversion means more prospects are becoming customers.",
            "Higher → stronger funnel performance",
            "Lower → weaker sales efficiency"
        ),
        (
            "Fulfilment SLA",
            "Higher SLA performance means more customer commitments are being met.",
            "Higher → stronger operational reliability",
            "Lower → higher service risk"
        )
    ]

    for name, explanation, positive, negative in signals:

        st.markdown(
            f"""
            <div class="signal-card">
                <div class="signal-title">{name}</div>
                <div style="color:#667085; margin-bottom:8px;">
                    {explanation}
                </div>
                <span class="signal-up">↑ {positive}</span>
                &nbsp;&nbsp;&nbsp;
                <span class="signal-down">↓ {negative}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # EXPLORE
    # -----------------------------------------------------
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

    # =====================================================
    # SCENARIO 1
    # =====================================================
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
            "Contribution is calculated before the narrative generation layer."
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

    # =====================================================
    # SCENARIO 2
    # =====================================================
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

    # =====================================================
    # SCENARIO 3
    # =====================================================
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
elif page == "Governance & Telemetry":

    st.markdown(
        '<div class="section-title">Governance & Telemetry</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Monitor how BusinessIntelligence.ai protects data, controls AI behaviour, "
        "and measures system performance."
    )

    # -----------------------------------------------------
    # SECURITY
    # -----------------------------------------------------
    st.markdown("### Security & Access")

    security = pd.DataFrame(
        {
            "Role": [
                "CEO",
                "Sales Manager",
                "Analyst"
            ],
            "Access": [
                "Aggregate business metrics",
                "Regional and authorised customer information",
                "Detailed analytical evidence"
            ],
            "Sensitive Data": [
                "Restricted",
                "Role dependent",
                "Authorised analytical access"
            ]
        }
    )

    st.dataframe(
        security,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # DATA GOVERNANCE
    # -----------------------------------------------------
    st.markdown("### Data Governance")

    governance = pd.DataFrame(
        {
            "Control": [
                "KPI Definition",
                "Data Freshness",
                "Source Lineage",
                "Access Control",
                "Confidence",
                "Auditability"
            ],
            "Purpose": [
                "Ensure consistent KPI calculations",
                "Show when source data was last updated",
                "Trace insights back to originating systems",
                "Restrict data based on user permissions",
                "Communicate strength of available evidence",
                "Record analytical decisions and outputs"
            ]
        }
    )

    st.dataframe(
        governance,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # TELEMETRY
    # -----------------------------------------------------
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

    # -----------------------------------------------------
    # LLM VS NON-LLM
    # -----------------------------------------------------
    st.markdown("### LLM vs Non-LLM Processing")

    processing = pd.DataFrame(
        {
            "Processing Step": [
                "KPI Calculation",
                "Materiality Detection",
                "Driver Contribution",
                "Evidence Retrieval",
                "Confidence Assessment",
                "Narrative Generation",
                "Recommendation"
            ],
            "Technology": [
                "Deterministic logic",
                "Statistics + business rules",
                "Deterministic analytics",
                "Retrieval",
                "Rules + statistical evidence",
                "LLM",
                "Rules + LLM"
            ],
            "Reason": [
                "Numerical accuracy",
                "Separate signal from normal variation",
                "Quantify measurable contributors",
                "Find relevant qualitative evidence",
                "Avoid unsupported certainty",
                "Convert evidence into natural language",
                "Translate evidence into practical action"
            ]
        }
    )

    st.dataframe(
        processing,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# FEEDBACK & LEARNING
# =========================================================
elif page == "Feedback/Comments":

    st.markdown(
        '<div class="section-title">Feedback & Learning</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Help BusinessIntelligence.ai improve the accuracy of its explanations, "
        "confidence assessments and recommended actions."
    )

    # -----------------------------------------------------
    # HUMAN-IN-THE-LOOP EXPLANATION
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="insight-box">
            <b>Human-in-the-loop learning</b><br><br>

            Business users and analysts can validate whether an insight was
            useful, challenge the identified driver, report missing evidence,
            or flag an incorrect confidence level.

            <br><br>

            This feedback can be used in production to improve driver ranking,
            evidence retrieval, confidence calibration and recommendation quality.
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # FEEDBACK FORM
    # -----------------------------------------------------
    st.markdown("### Submit Feedback")

    feedback_type = st.selectbox(
        "What would you like to tell us?",
        [
            "Insight was useful",
            "Insight was partially useful",
            "Incorrect driver",
            "Missing evidence",
            "Confidence was too high",
            "Confidence was too low",
            "Recommendation was not practical",
            "Other"
        ]
    )

    comment = st.text_area(
        "Comment",
        placeholder=(
            "Tell us what was correct, incorrect, missing, "
            "or what the engine should have considered..."
        ),
        height=160
    )

    role_for_feedback = st.selectbox(
        "Your role",
        [
            "CEO",
            "Sales Manager",
            "Analyst"
        ]
    )

    if st.button("Submit Feedback", type="primary"):

        if not comment.strip():

            st.warning(
                "Please add a comment before submitting your feedback."
            )

        else:

            # Store feedback in session state for prototype demonstration
            if "feedback_history" not in st.session_state:
                st.session_state.feedback_history = []

            st.session_state.feedback_history.append(
                {
                    "Role": role_for_feedback,
                    "Feedback": feedback_type,
                    "Comment": comment
                }
            )

            st.success(
                "Thank you — your feedback has been captured."
            )

            st.caption(
                "In production, feedback would be stored in a governed feedback "
                "store and used for evaluation and model improvement."
            )

    # -----------------------------------------------------
    # FEEDBACK HISTORY
    # -----------------------------------------------------
    st.markdown("### Recent Feedback")

    if "feedback_history" not in st.session_state:
        st.session_state.feedback_history = []

    if len(st.session_state.feedback_history) == 0:

        st.info(
            "No feedback submitted yet. Your first submission will appear here."
        )

    else:

        feedback_df = pd.DataFrame(
            st.session_state.feedback_history
        )

        st.dataframe(
            feedback_df,
            use_container_width=True,
            hide_index=True
        )

    # -----------------------------------------------------
    # LEARNING LOOP
    # -----------------------------------------------------
    st.markdown("### How Feedback Improves the Engine")

    learning_loop = pd.DataFrame(
        {
            "User Feedback": [
                "Incorrect driver",
                "Missing evidence",
                "Wrong confidence",
                "Poor recommendation"
            ],
            "Improvement Area": [
                "Driver ranking",
                "Evidence retrieval",
                "Confidence calibration",
                "Action recommendation"
            ]
        }
    )

    st.dataframe(
        learning_loop,
        use_container_width=True,
        hide_index=True
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
# =========================================================
# FEEDBACK & COMMENTS
# =========================================================
# =========================================================
# FEEDBACK & COMMENTS
# =========================================================
if page == "Feedback/Comments":

    st.markdown(
        '<div class="section-title">Feedback & Learning</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Tell us what worked, what needs improvement, "
        "or where the engine could provide better intelligence."
    )

    st.info(
        "Your feedback helps improve BusinessIntelligence.ai across "
        "analytics, recommendations, evidence quality, governance "
        "and the overall decision-making experience."
    )

    st.markdown("### What would you like to review?")

    feedback_area = st.selectbox(
        "Select area",
        [
            "Overview",
            "KPI Intelligence",
            "Decision Workspace",
            "Evidence & Lineage",
            "Governance & Telemetry",
            "Overall Experience"
        ],
        key="feedback_area"
    )

    st.markdown("### What would you like to tell us?")

    feedback_type = st.selectbox(
        "Feedback type",
        [
            "This section was useful",
            "This section was confusing",
            "Incorrect driver",
            "Missing evidence",
            "Confidence was too high",
            "Confidence was too low",
            "Recommendation was not practical",
            "Data or metric issue",
            "Security or access issue",
            "Performance or latency issue",
            "Other"
        ],
        key="feedback_type"
    )

    feedback_role = st.selectbox(
        "Select your role",
        [
            "CEO",
            "Sales Manager",
            "Analyst"
        ],
        key="feedback_role"
    )

    comment = st.text_area(
        "Comment",
        placeholder=(
            "Tell us what was correct, incorrect, missing, "
            "confusing, or what should be improved..."
        ),
        height=160,
        key="feedback_comment"
    )

    if st.button(
        "Submit Feedback",
        type="primary",
        key="submit_feedback"
    ):

        if not comment.strip():

            st.warning(
                "Please enter a comment before submitting."
            )

        else:

            if "feedback_history" not in st.session_state:
                st.session_state.feedback_history = []

            st.session_state.feedback_history.append(
                {
                    "Area": feedback_area,
                    "Role": feedback_role,
                    "Feedback": feedback_type,
                    "Comment": comment
                }
            )

            st.success(
                f"Feedback captured for {feedback_area}."
            )

    st.markdown("### Recent Feedback")

    if "feedback_history" not in st.session_state:
        st.session_state.feedback_history = []

    if len(st.session_state.feedback_history) == 0:

        st.caption(
            "No feedback submitted yet."
        )

    else:

        feedback_df = pd.DataFrame(
            st.session_state.feedback_history
        )

        st.dataframe(
            feedback_df,
            use_container_width=True,
            hide_index=True
        )

    st.markdown("### How Feedback Improves the Engine")

    learning_loop = pd.DataFrame(
        {
            "Feedback Area": [
                "Overview",
                "KPI Intelligence",
                "Decision Workspace",
                "Evidence & Lineage",
                "Governance & Telemetry"
            ],
            "Improvement Focus": [
                "Clarity and business usability",
                "Driver ranking and confidence",
                "Recommendation quality",
                "Evidence retrieval and traceability",
                "Security, latency and system reliability"
            ]
        }
    )

    st.dataframe(
        learning_loop,
        use_container_width=True,
        hide_index=True
    )
