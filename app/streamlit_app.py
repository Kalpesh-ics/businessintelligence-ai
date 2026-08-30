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

    /* =========================
       MAIN APP
       ========================= */

    .stApp {
        background-color: #F7F8FC;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #F9FAFB !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        color: #F9FAFB !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: #111827 !important;
    }

    div[data-baseweb="popover"] {
        background-color: #FFFFFF !important;
    }

    div[data-baseweb="popover"] * {
        color: #111827 !important;
    }


    /* =========================
       BRAND
       ========================= */

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


    /* =========================
       HEADER
       ========================= */

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


    /* =========================
       WELCOME
       ========================= */

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


    /* =========================
       SECTION TITLES
       ========================= */

    .section-title {
        font-size: 23px;
        font-weight: 750;
        color: #111827;
        margin-top: 28px;
        margin-bottom: 15px;
    }


    /* =========================
       BUSINESS METRIC CARDS
       ========================= */

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


    /* =========================
       SIGNAL CARDS
       ========================= */

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


    /* =========================
       INSIGHT BOX
       ========================= */

    .insight-box {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 3px 12px rgba(16, 24, 40, 0.05);
        margin-top: 15px;
        margin-bottom: 20px;
    }


    /* =========================
       DECISION CARDS
       ========================= */

    .decision-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 22px;
        min-height: 210px;
        box-shadow: 0 2px 10px rgba(16, 24, 40, 0.04);
    }

    .decision-card-title {
        font-size: 18px;
        font-weight: 750;
        color: #101828;
        margin-bottom: 10px;
    }

    .decision-card-text {
        color: #667085;
        font-size: 14px;
        line-height: 1.6;
    }


    /* =========================
       FOOTER
       ========================= */

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
# SESSION STATE
# =========================================================
if "feedback_history" not in st.session_state:
    st.session_state.feedback_history = []

if "approved_action" not in st.session_state:
    st.session_state.approved_action = None

if "decision_status" not in st.session_state:
    st.session_state.decision_status = "Pending"


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
    [
        "CEO",
        "Sales Manager",
        "Analyst"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption("Round 2 Prototype")
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

    st.markdown(
        '<div class="section-title">Key Business Metrics</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Core metrics businesses typically monitor to understand "
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
                    <div class="metric-description">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">Key Business Signals</div>',
        unsafe_allow_html=True
    )

    signals = [
        (
            "Revenue",
            "Higher revenue generally indicates stronger business income.",
            "Higher → stronger income",
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
            "Higher → stronger reliability",
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
            "Evaluate actions, constraints and outcomes."
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
        "Move from KPI movement to quantified drivers, supporting evidence "
        "and calibrated confidence."
    )

    scenario = st.selectbox(
        "Select Investigation",
        [
            "Multi-factor Revenue Movement",
            "Low Confidence / Abstention",
            "Sparse History / New KPI"
        ],
        key="kpi_scenario"
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
                    "Prod A Volume",
                    "Enterprise Customer Decline",
                    "Price",
                    "Other / Offset"
                ],
                "Contribution": [
                    45,
                    29,
                    13,
                    13
                ]
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
                "Major enterprise accounts are threatening non-renewal "
                "over missed uptime SLAs."
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
                <b>Why the engine abstains</b>

                <p>
                    Multiple signals are present, but critical attribution
                    data is incomplete or contradictory.
                </p>

                <b>Recommended next step</b>

                <p>
                    Restore the attribution pipeline and validate
                    channel-level conversion data before taking corrective action.
                </p>
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

        baseline = [
            500,
            520,
            510,
            540,
            530
        ]

        mat = engine.detect_materiality(
            480,
            baseline
        )

        st.markdown("### Method Selection")

        st.warning(
            "Sparse history detected — conventional long-term anomaly "
            "detection is unreliable."
        )

        st.markdown(
            f"""
            <div class="insight-box">
                <b>Selected analytical method</b>

                <p>{mat['method']}</p>

                <p>
                    The engine switches methodology because this KPI has
                    insufficient historical observations to establish
                    a stable baseline.
                </p>
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
        f"Use evidence, constraints and AI recommendations to move "
        f"from insight to an actionable business decision."
    )

    # -----------------------------------------------------
    # ACTIVE DECISION
    # -----------------------------------------------------

    st.markdown("### Active Decision")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Business Signal",
        "Revenue ↓ 8.2%"
    )

    c2.metric(
        "Business Impact",
        "$8.2M"
    )

    c3.metric(
        "Primary Contributor",
        "Prod A Volume"
    )

    c4.metric(
        "Confidence",
        "Medium"
    )

    st.markdown("---")

    # -----------------------------------------------------
    # WHY
    # -----------------------------------------------------

    st.markdown("### Why is this happening?")

    st.write(
        "The engine traces the material movement through quantified "
        "contributors and supporting business signals."
    )

    why_df = pd.DataFrame(
        {
            "Business Signal": [
                "Revenue",
                "Prod A Volume",
                "Enterprise Customers",
                "Fulfilment SLA",
                "Support Activity"
            ],
            "Observed Movement": [
                "↓ 8.2%",
                "↓ 14%",
                "↓ Enterprise volume",
                "↓ 15 pts",
                "↑ 300%"
            ],
            "Evidence Type": [
                "KPI",
                "Contribution",
                "CRM",
                "Operations",
                "Unstructured"
            ]
        }
    )

    st.dataframe(
        why_df,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Prod A volume is the largest quantified contributor. "
        "Fulfilment deterioration and support activity are supporting signals, "
        "but current evidence does not establish causality."
    )

    # -----------------------------------------------------
    # ASK BI.AI
    # -----------------------------------------------------

    st.markdown("### Ask BusinessIntelligence.ai")

    question = st.text_input(
        "Ask a business question",
        placeholder="Example: What happens if we do nothing?",
        key="decision_question"
    )

    if st.button(
        "Ask",
        key="ask_decision"
    ):

        if question.strip():

            q = question.lower()

            if "do nothing" in q:

                st.warning(
                    "At the current run rate, continued revenue pressure "
                    "is likely. This is a directional scenario, not a causal forecast."
                )

            elif "customer" in q or "account" in q:

                st.info(
                    "Enterprise customers are the most affected segment. "
                    "Prioritising at-risk accounts is therefore the most direct "
                    "controllable response supported by the available evidence."
                )

            elif "price" in q:

                st.info(
                    "Price is a smaller quantified contributor than Prod A "
                    "volume. Pricing should therefore not be the first intervention "
                    "based on current evidence."
                )

            elif "why" in q:

                st.info(
                    "Prod A volume is the largest measured contributor. "
                    "Operational and support signals suggest fulfilment disruption "
                    "may be involved, but causality has not been established."
                )

            else:

                st.info(
                    "The strongest current signals are Prod A volume and "
                    "enterprise customer impact. More evidence is required "
                    "for a more specific conclusion."
                )

        else:

            st.warning(
                "Enter a business question first."
            )

    # -----------------------------------------------------
    # ACTION EVALUATION
    # -----------------------------------------------------

    st.markdown("### Evaluate Actions")

    st.write(
        "Compare practical responses using available evidence, "
        "business levers and decision rights."
    )

    actions = {
        "Protect Enterprise Renewals": {
            "driver": "Enterprise customer decline",
            "lever": "Customer retention",
            "owner": "Sales + Customer Success",
            "confidence": "HIGH",
            "impact": "Potentially protects at-risk enterprise revenue",
            "risk": "Requires account-level coordination"
        },
        "Fix Prod A Fulfilment": {
            "driver": "Fulfilment SLA deterioration",
            "lever": "Operational capacity",
            "owner": "Operations",
            "confidence": "MEDIUM",
            "impact": "Potentially reduces service-related revenue pressure",
            "risk": "Root cause is not yet causally established"
        },
        "Adjust Pricing": {
            "driver": "Price contribution",
            "lever": "Pricing",
            "owner": "Pricing / Finance",
            "confidence": "LOW",
            "impact": "May influence volume but could reduce margin",
            "risk": "Price is not the dominant quantified contributor"
        }
    }

    selected_action = st.selectbox(
        "Choose an action to evaluate",
        list(actions.keys()),
        key="selected_action"
    )

    action = actions[selected_action]

    ac1, ac2 = st.columns(2)

    with ac1:

        st.markdown(
            f"""
            <div class="decision-card">
                <div class="decision-card-title">
                    Action Assessment
                </div>

                <div class="decision-card-text">

                    <b>Driver</b><br>
                    {action["driver"]}<br><br>

                    <b>Controllable Lever</b><br>
                    {action["lever"]}<br><br>

                    <b>Owner</b><br>
                    {action["owner"]}<br><br>

                    <b>Confidence</b><br>
                    {action["confidence"]}

                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with ac2:

        st.markdown(
            f"""
            <div class="decision-card">
                <div class="decision-card-title">
                    Expected Outcome
                </div>

                <div class="decision-card-text">

                    <b>Expected Impact</b><br>
                    {action["impact"]}<br><br>

                    <b>Key Risk</b><br>
                    {action["risk"]}

                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # BUSINESS CONSTRAINTS
    # -----------------------------------------------------

    st.markdown("### Business Constraints")

    cc1, cc2, cc3 = st.columns(3)

    with cc1:

        budget = st.number_input(
            "Available budget ($)",
            min_value=0,
            value=250000,
            step=25000,
            key="decision_budget"
        )

    with cc2:

        max_discount = st.slider(
            "Maximum discount (%)",
            min_value=0,
            max_value=20,
            value=5,
            key="decision_discount"
        )

    with cc3:

        authority = st.selectbox(
            "Decision authority",
            [
                "Regional",
                "Business Unit",
                "Enterprise"
            ],
            key="decision_authority"
        )

    st.caption(
        f"Current constraints: ${budget:,.0f} budget · "
        f"{max_discount}% maximum discount · "
        f"{authority} decision authority"
    )

    # -----------------------------------------------------
    # CONSTRAINT CHECK
    # -----------------------------------------------------

    st.markdown("### Constraint Check")

    if selected_action == "Adjust Pricing" and authority == "Regional":

        st.warning(
            "Pricing is outside the selected regional decision authority. "
            "The recommendation requires escalation to Pricing / Finance."
        )

    elif (
        selected_action == "Protect Enterprise Renewals"
        and budget < 100000
    ):

        st.warning(
            "The selected budget may constrain the proposed account-recovery "
            "program. Consider narrowing the target account set."
        )

    else:

        st.success(
            "Selected action is compatible with the current prototype constraints."
        )

    # -----------------------------------------------------
    # CHALLENGE THE AI
    # -----------------------------------------------------

    st.markdown("### Challenge the Recommendation")

    challenge = st.radio(
        "How do you want to challenge the current recommendation?",
        [
            "I agree",
            "I think the driver is wrong",
            "Evidence is missing",
            "This action is not feasible"
        ],
        key="challenge_recommendation"
    )

    if challenge == "I agree":

        st.success(
            "Recommendation accepted. Continue to approval."
        )

    elif challenge == "I think the driver is wrong":

        alternative_driver = st.selectbox(
            "Which driver should be investigated instead?",
            [
                "Price",
                "Competition",
                "Marketing",
                "Customer Churn",
                "Operations",
                "Other"
            ],
            key="alternative_driver"
        )

        st.info(
            f"The engine will investigate {alternative_driver} as an "
            "alternative hypothesis and compare its evidence against "
            "the current leading driver."
        )

    elif challenge == "Evidence is missing":

        st.info(
            "Suggested evidence: account-level churn, channel-level "
            "performance, operational incident logs and affected-vs-"
            "unaffected regional comparisons."
        )

    else:

        st.info(
            "The recommendation should be filtered through business "
            "constraints and decision rights before approval."
        )

    # -----------------------------------------------------
    # WHAT WOULD CHANGE THE CONCLUSION?
    # -----------------------------------------------------

    st.markdown("### What Would Change This Conclusion?")

    evidence_change = pd.DataFrame(
        {
            "Evidence That Increases Confidence": [
                "Affected vs unaffected region comparison",
                "Account-level fulfilment timestamps",
                "Validated enterprise churn data"
            ],
            "Evidence That Reduces Confidence": [
                "Stable fulfilment SLA in affected accounts",
                "Similar decline in regions without disruption",
                "No corresponding enterprise churn"
            ]
        }
    )

    st.dataframe(
        evidence_change,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # DECISION APPROVAL
    # -----------------------------------------------------

    st.markdown("### Decision Approval")

    understand = st.checkbox(
        "I understand the evidence and uncertainty and want to approve this action.",
        key="approve_understanding"
    )

    if understand:

        if st.button(
            "Approve Action",
            type="primary",
            key="approve_action"
        ):

            st.session_state.approved_action = selected_action
            st.session_state.decision_status = "Approved"

            st.success(
                f"Decision recorded: {selected_action}"
            )

    # -----------------------------------------------------
    # MONITOR OUTCOME
    # -----------------------------------------------------

    st.markdown("### Monitor Outcome")

    if st.session_state.approved_action:

        st.markdown(
            f"""
            <div class="insight-box">

                <b>Status</b><br>
                {st.session_state.decision_status}

                <br>

                <b>Approved Action</b><br>
                {st.session_state.approved_action}

                <br>

                <b>Owner</b><br>
                {actions[st.session_state.approved_action]["owner"]}

                <br>

                <b>Metrics to Monitor</b><br>
                Revenue · Enterprise Volume · Retention ·
                Fulfilment SLA · Support Activity

                <br>

                <b>Review Frequency</b><br>
                Weekly

                <br>

                <b>Outcome</b><br>
                Pending measurement

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.caption(
            "Approve an action to activate its monitoring plan."
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
        "Trace every insight back to its source, freshness and analytical method."
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
        "Monitor data quality, security, analytical methods and system performance."
    )

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
                "Restrict data based on permissions",
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

    st.markdown("### Runtime Telemetry")

    telemetry = engine.telemetry

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Latency",
        f"{telemetry['00']} ms"
    )

    c2.metric(
        "LLM Calls",
        telemetry["0"]
    )

    c3.metric(
        "Tokens Used",
        telemetry["0"]
    )

    c4.metric(
        "Estimated Cost",
        f"${telemetry['0']:.4f}"
    )

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
# FEEDBACK & COMMENTS
# =========================================================

elif page == "Feedback/Comments":

    st.markdown(
        '<div class="section-title">Feedback & Learning</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Tell us what worked, what needs improvement, or where the "
        "engine could provide better intelligence."
    )

    st.info(
        "Your feedback helps improve analytics, recommendations, evidence "
        "quality, governance and the overall decision-making experience."
    )

    # -----------------------------------------------------
    # AREA
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # FEEDBACK TYPE
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # ROLE
    # -----------------------------------------------------

    feedback_role = st.selectbox(
        "Select your role",
        [
            "CEO",
            "Sales Manager",
            "Analyst"
        ],
        key="feedback_role"
    )

    # -----------------------------------------------------
    # COMMENT
    # -----------------------------------------------------

    comment = st.text_area(
        "Comment",
        placeholder=(
            "Tell us what was correct, incorrect, missing, "
            "confusing, or what should be improved..."
        ),
        height=160,
        key="feedback_comment"
    )

    # -----------------------------------------------------
    # SUBMIT
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # RECENT FEEDBACK
    # -----------------------------------------------------

    st.markdown("### Recent Feedback")

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

    # -----------------------------------------------------
    # LEARNING LOOP
    # -----------------------------------------------------

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
