import pandas as pd
import numpy as np
import time

class KPIEngine:
    def __init__(self):
        self.telemetry = {"latency_ms": 0, "llm_calls": 0, "tokens_used": 0, "est_cost_usd": 0.0}

    def detect_materiality(self, current_val, baseline_series, z_threshold=2.0, impact_threshold=0.05):
        start_time = time.time()
        if len(baseline_series) < 14:
            pct_change = (current_val - baseline_series[-1]) / baseline_series[-1] if baseline_series else 0
            is_material = abs(pct_change) >= impact_threshold
            method_used = "Cross-sectional Benchmark (Sparse History)"
            z_score = 0
        else:
            mean, std = np.mean(baseline_series), np.std(baseline_series)
            z_score = (current_val - mean) / std if std > 0 else 0
            pct_change = (current_val - mean) / mean if mean > 0 else 0
            is_material = abs(z_score) >= z_threshold and abs(pct_change) >= impact_threshold
            method_used = "Z-Score Anomaly Detection"
        
        self.telemetry["latency_ms"] += round((time.time() - start_time) * 1000, 2)
        return {"is_material": is_material, "z_score": z_score, "pct_change": pct_change, "method": method_used}

    def retrieve_unstructured_evidence(self, driver_focus):
        if driver_focus == "Enterprise Cloud Hosting":
            return [
                {"source": "Support Tickets", "signal": "300% spike in 'outage' and 'latency' tags in US-West data centers."},
                {"source": "CRM Notes", "signal": "Major enterprise accounts threatening non-renewal over missed uptime SLAs."}
            ]
        return []

    def determine_confidence(self, structured_variance, unstructured_evidence):
        evidence_count = len(unstructured_evidence)
        if evidence_count < 1 and structured_variance < 0.4:
            return "LOW - ABSTAIN"
        elif evidence_count >= 2 and structured_variance >= 0.6:
            return "HIGH"
        return "MEDIUM"

    def generate_narrative(self, persona, context, confidence):
        self.telemetry["llm_calls"] += 1
        self.telemetry["tokens_used"] += 450
        self.telemetry["est_cost_usd"] += 0.002
        
        if "ABSTAIN" in confidence:
            return "⚠️ **ABSTAIN:** Q3 Marketing ROI shows a sudden drop, but Google Ads API data and Salesforce attribution are currently out of sync. The engine refuses to generate a causal root cause until the API sync is restored."
        if persona == "CEO":
            return f"Revenue is materially below baseline. **Enterprise Cloud Hosting** is the primary contributor, driven by localized outages in the US-West region triggering SLA penalties."
        elif persona == "Sales Manager":
            return f"**Driver:** US-West Data Center Outage (Enterprise Cloud Hosting)\n**Lever:** Proactive SLA credits & account management\n**Action:** Issue automatic 5% SLA credits to affected Tier 1 accounts before they file tickets\n**Impact:** Protect $1.2M in at-risk Q3 renewals\n**Owner:** VP Customer Success\n**Confidence:** {confidence}"
        return "Insight generated based on statistical contribution."
