# BusinessIntelligence.ai

## AI-Powered KPI Intelligence-to-Action Engine

BusinessIntelligence.ai is a prototype intelligence layer that moves business users beyond traditional dashboards.

Instead of stopping at:

> **“What changed?”**

the system is designed to answer:

> **“What changed, what are the likely drivers, what evidence supports them, how confident are we, and what should we do next?”**

The Round 2 prototype demonstrates this workflow using synthetic enterprise data, deterministic analytics, statistical methods, evidence retrieval, confidence assessment, decision constraints, role-based views, governance controls, and human feedback.

---

## 1. Problem

Traditional business dashboards are effective at showing KPI movements but often leave the interpretation to analysts.

For example, a dashboard may show:

**Revenue ↓ 8.2% in US-West**

but does not automatically explain:

* where the movement is concentrated
* which factors contributed most
* whether supporting evidence exists outside structured KPI tables
* whether the explanation is reliable
* what action is feasible
* who should own the action
* what should be monitored afterward

BusinessIntelligence.ai addresses this gap by creating an intelligence-to-action layer between raw business data and business decisions.

---

## 2. Solution

BusinessIntelligence.ai combines:

**Structured business data**

* Sales / ERP
* Finance
* CRM
* Operations
* Marketing

with:

**Unstructured business evidence**

* Support tickets
* CRM notes
* Customer feedback
* Operational signals
* Internal business context

The prototype then follows this workflow:

```text
Business Data
      ↓
Governed KPI Layer
      ↓
Materiality Detection
      ↓
Driver Contribution Analysis
      ↓
Evidence Retrieval
      ↓
Confidence Assessment
      ↓
Business Narrative
      ↓
Decision Workspace
      ↓
Action + Constraints + Owner
      ↓
Approval
      ↓
Monitoring
      ↓
User Feedback
```

---

## 3. Round 2 Prototype Capabilities

The prototype demonstrates the core mechanisms requested in the challenge.

### Material KPI movement detection

The system first checks whether sufficient historical observations are available.

For KPIs with at least 14 observations, the prototype calculates the historical mean, standard deviation, Z-score and percentage deviation. A movement is classified as material only when both conditions are met:

* Z-score ≥ 2.0σ
* Absolute percentage deviation ≥ 5%

For sparse-history KPIs with fewer than 14 observations, conventional Z-score analysis is not applied. The prototype switches to a cross-sectional benchmark approach and uses the 5% deviation threshold for the materiality decision.

This separation prevents insufficient historical data from being treated as a reliable statistical baseline.

### Multi-factor driver analysis

For the revenue scenario, the system decomposes the total movement into quantified contributors:

* Product A Volume
* Enterprise Customer Decline
* Price
* Other / Offset

The driver contribution values are linked to the total simulated revenue impact rather than being presented as independent numbers.

### Structured + unstructured evidence

The prototype combines quantified KPI and driver signals with supporting qualitative evidence from CRM notes and support-ticket patterns, alongside operational signals such as fulfilment SLA.

This demonstrates how a KPI explanation can use information that is not contained in a traditional dashboard.

### Confidence and abstention

The system does not assume that every KPI movement has a known cause.

Where evidence is incomplete or contradictory, the prototype explicitly abstains.

Example:

**Q3 Marketing ROI ↓ 12.4%**

The prototype simulates a conflict between:

* Google Ads attribution
* Salesforce attribution

and refuses to generate an unsupported causal explanation when the available evidence is incomplete or contradictory.

### Sparse-history handling

For newly launched KPIs with insufficient historical observations, the system switches analytical methodology rather than pretending that a stable baseline exists.

Example:

**AI Data Center Nodes — Weekly Active Users**

Historical observations:

**5**

The prototype switches to:

**Cross-sectional Benchmark (Sparse History)**

### Persona-specific views

The sidebar allows the user to select:

* CEO
* Sales Manager
* Analyst

The Decision Workspace and narrative presentation can adapt to the selected persona.

---

# 4. Interactive Decision Workspace

The Decision Workspace is designed as the transition from insight to action.

The workflow is:

```text
Active Decision
      ↓
Why is this happening?
      ↓
Evaluate Actions
      ↓
Business Constraints
      ↓
Compatibility Check
      ↓
Challenge Recommendation
      ↓
What Would Change the Conclusion?
      ↓
Decision Approval
      ↓
Monitor Outcome
```

## Active Decision

The workspace shows:

* business signal
* business impact
* primary contributor
* confidence

## Evaluate Actions

Users can evaluate different business responses.

Current prototype actions include:

### Protect Enterprise Renewals

Driver:

Enterprise customer decline

Lever:

Customer retention

Owner:

Sales + Customer Success

### Fix Product A Fulfilment

Driver:

Fulfilment SLA deterioration

Lever:

Operational capacity

Owner:

Operations

### Adjust Pricing

Driver:

Price contribution

Lever:

Pricing

Owner:

Pricing / Finance

Each action includes:

* driver
* controllable lever
* owner
* confidence
* expected impact
* key risk
* minimum budget
* required decision authority

---

# 5. Business Constraints

Recommendations are checked against business constraints before approval.

The prototype allows the user to specify:

* available budget
* maximum discount
* decision authority

The system then determines whether the selected action is compatible.

For example, a pricing action may require Business Unit authority.

If the user has only Regional authority, the system identifies the conflict instead of allowing the action to proceed.

Similarly, actions can become incompatible when the available budget is below the required threshold.

This demonstrates that recommendations are constrained by **business feasibility and decision rights**, rather than being generic AI suggestions.

---

# 6. Challenging the Recommendation

Users can challenge a recommendation by selecting:

* I agree
* I think the driver is wrong
* Evidence is missing
* This action is not feasible

When a user challenges the driver, an alternative hypothesis can be selected:

* Price
* Competition
* Marketing
* Customer Churn
* Operations
* Other

The prototype then communicates that the alternative should be investigated and compared against the current leading driver.

---

# 7. What Would Change the Conclusion?

The prototype explicitly distinguishes between evidence that would increase or decrease confidence.

Examples of evidence that could increase confidence:

* affected vs unaffected region comparison
* account-level fulfilment timestamps
* validated enterprise churn data

Examples of evidence that could reduce confidence:

* stable fulfilment SLA in affected accounts
* similar decline in unaffected regions
* no corresponding enterprise churn

This is intended to make uncertainty actionable rather than simply displaying a confidence label.

---

# 8. Decision Approval and Monitoring

A user must acknowledge the evidence and uncertainty before approving an action.

Once approved, the prototype creates a monitoring plan containing:

* approved action
* owner
* metrics to monitor
* review frequency
* outcome status

Example monitored metrics:

* Revenue
* Enterprise Volume
* Customer Retention
* Fulfilment SLA
* Support Activity

The initial state is:

**Pending measurement**

This creates an end-to-end decision lifecycle rather than stopping at a recommendation.

---

# 9. Evidence & Lineage

The Evidence & Lineage section makes insights traceable.

The prototype displays:

| Evidence         | Source           | Freshness  | Evidence Type       |
| ---------------- | ---------------- | ---------- | ------------------- |
| Regional Revenue | Sales / ERP      | 2 hours    | Quantitative KPI    |
| CRM Account Risk | CRM              | 4 hours    | Customer context    |
| Support Tickets  | Customer Support | 15 minutes | Unstructured signal |
| Fulfilment SLA   | Operations       | 30 minutes | Operational signal  |

### KPI lineage

```text
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
```

### Evidence classification

The prototype distinguishes:

* Observed Fact
* Measured Contribution
* Association
* Likely Driver
* Causal Evidence
* Unconfirmed Hypothesis

This separation is important because correlation or contribution does not automatically establish causation.

---

# 10. Governance & Telemetry

The Governance & Telemetry section demonstrates operational controls around the intelligence layer.

## Security & Access

Example role scopes:

| Role          | Access                                       |
| ------------- | -------------------------------------------- |
| CEO           | Aggregate business metrics                   |
| Sales Manager | Regional and authorised customer information |
| Analyst       | Detailed analytical evidence                 |

Sensitive information is represented as role-dependent or restricted.

## Data Governance

The prototype surfaces:

* KPI definition
* data freshness
* source lineage
* access control
* confidence
* auditability

---

# 11. Runtime Telemetry

The current prototype does **not make live LLM/API calls**.

Therefore:

```text
LLM Calls        = 0
Tokens Used      = 0
Estimated Cost   = $0.0000
```

The prototype does measure analytical processing latency.

This is intentional.

The architecture separates quantitative truth from language generation:

```text
Deterministic / Statistical Layer
            ↓
      Quantitative Truth
            ↓
      Evidence Layer
            ↓
 Narrative / Recommendation Layer
```

The current proof of concept validates the analytical and decision workflow without requiring a live external LLM.

---

# 12. LLM vs Non-LLM Responsibility

The prototype explicitly separates processing responsibilities.

| Processing Step       | Technology                         | Reason                                  |
| --------------------- | ---------------------------------- | --------------------------------------- |
| KPI Calculation       | Deterministic logic                | Numerical accuracy                      |
| Materiality Detection | Statistics + business rules        | Detect meaningful movement              |
| Driver Contribution   | Deterministic analytics            | Quantify contributors                   |
| Evidence Retrieval    | Retrieval                          | Find relevant qualitative context       |
| Confidence Assessment | Rules + statistical evidence       | Avoid unsupported certainty             |
| Narrative Generation  | Deterministic template in POC      | Controlled output                       |
| Recommendation        | Rules + deterministic logic in POC | Respect constraints and decision rights |

A future production implementation can introduce an LLM as an optional narrative/orchestration layer without allowing the model to become the source of quantitative truth.

---

# 13. Human-in-the-Loop Feedback

The Feedback/Comments section captures feedback by:

**Area**

* Overview
* KPI Intelligence
* Decision Workspace
* Evidence & Lineage
* Governance & Telemetry
* Overall Experience

**Feedback type**

* Useful
* Confusing
* Incorrect driver
* Missing evidence
* Confidence too high
* Confidence too low
* Recommendation not practical
* Data or metric issue
* Security or access issue
* Performance or latency issue
* Other

**Role**

* CEO
* Sales Manager
* Analyst

**Comment**

Users can submit written feedback, which is retained during the prototype session.

The intended production learning loop is:

```text
User Feedback
      ↓
Feedback Store
      ↓
Evaluation Dataset
      ↓
Driver Accuracy
Confidence Calibration
Evidence Quality
Recommendation Quality
      ↓
Continuous Improvement
```

---

# 14. Prototype Scenarios

The prototype includes three core scenarios.

## Scenario 1 — Multi-factor Revenue Movement

**US-West Revenue**

Current revenue:

**$91.8M**

Baseline:

**$100.0M**

Movement:

**-8.2%**

Business impact:

**$8.2M**

The engine demonstrates:

* materiality detection
* driver contribution
* supporting evidence
* source freshness
* confidence
* persona-specific narrative

## Scenario 2 — Low Confidence / Abstention

**Q3 Marketing ROI**

Movement:

**-12.4%**

Data completeness:

**62%**

The engine detects conflicting attribution sources and abstains from claiming a causal root cause.

## Scenario 3 — Sparse History / New KPI

**AI Data Center Nodes**

Weekly active users:

**480**

Historical observations:

**5**

The engine changes methodology because insufficient history exists for a conventional long-term baseline.

---

# 15. Project Structure

```text
businessintelligence-ai/
│
├── app/
│   └── streamlit_app.py
│
├── engine/
│   └── core.py
│
├── data/
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 16. Technology Stack

The current prototype uses:

* Python
* Streamlit
* Pandas
* NumPy
* SciPy
* PyYAML

The system is intentionally lightweight so the proof of concept can run without enterprise infrastructure or paid model APIs.

---

# 17. Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/businessintelligence-ai.git
```

Move into the project:

```bash
cd businessintelligence-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/streamlit_app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 18. Live Demo

**Live Prototype:**
Add your Streamlit Cloud URL here.

Example:

```text
https://YOUR-APP-NAME.streamlit.app
```

---

# 19. Demo Video

**Prototype Demo Video:**
Add your public demo video link here.

The recommended demo flow is:

```text
1. Overview
2. Select Role
3. KPI Intelligence
4. Multi-factor Revenue Movement
5. Evidence + Confidence
6. Decision Workspace
7. Evaluate Action
8. Change Constraints
9. Challenge Recommendation
10. Approve Action
11. Monitor Outcome
12. Low-confidence Abstention
13. Sparse-history Scenario
14. Evidence & Lineage
15. Governance & Telemetry
16. Feedback/Comments
```

---

# 20. Design Principles

BusinessIntelligence.ai follows several principles:

### Quantitative truth is deterministic

The LLM should not invent KPI values, percentages, business impact or contribution figures.

### Evidence before explanation

A narrative should be grounded in observable business evidence.

### Confidence before certainty

The system should communicate uncertainty and abstain when evidence is insufficient.

### Actionability with constraints

Recommendations should account for business levers, ownership, budget and decision rights.

### Traceability

Users should be able to understand where an insight came from.

### Human oversight

Users should be able to challenge, correct and provide feedback on the engine.

---

# 21. Limitations of the Current POC

This prototype uses synthetic data and simplified analytical logic.

It is not production-ready and does not currently include:

* direct enterprise warehouse connectors
* production authentication
* persistent feedback storage
* advanced causal inference
* real-time streaming pipelines
* production-grade vector retrieval
* live LLM integration
* enterprise data masking
* automated model drift monitoring

These are deliberate scope limitations for a competition proof of concept.

---

# 22. Future Roadmap

### Phase 1 — Prototype

* Synthetic enterprise datasets
* KPI semantic layer
* Materiality detection
* Driver contribution
* Evidence retrieval
* Confidence and abstention
* Decision workspace
* Feedback capture

### Phase 2 — Enterprise Integration

* Snowflake / Databricks / Fabric connectivity
* CRM and support integrations
* Governed KPI contracts
* Row- and column-level access controls
* Persistent feedback store

### Phase 3 — Advanced Intelligence

* Causal inference
* Experiment-aware reasoning
* Forecasting
* Alternative hypothesis ranking
* Automated drift detection
* Real-time KPI monitoring

### Phase 4 — AI Decision Copilot

* Optional LLM narrative layer
* Natural-language analytical interaction
* Enterprise retrieval
* Action orchestration
* Workflow integrations
* Continuous learning from business outcomes

---

# 23. Competition Objective

BusinessIntelligence.ai aims to transform business intelligence from:

> **Monitor the metric**

to:

> **Understand the movement**

to:

> **Evaluate the evidence**

to:

> **Choose an action**

to:

> **Monitor the outcome**

The central principle is simple:

**Don't just tell the business what happened. Help it understand what happened, know how certain that explanation is, decide what to do, and learn from the outcome.**