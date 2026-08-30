import pandas as pd
import numpy as np
import time


class KPIEngine:

    def __init__(self):

        # Prototype currently does NOT use a live LLM.
        # Therefore all LLM telemetry remains zero.
        self.telemetry = {
            "latency_ms": 0,
            "llm_calls": 0,
            "tokens_used": 0,
            "est_cost_usd": 0.0
        }


    # =====================================================
    # MATERIALITY DETECTION
    # =====================================================

    def detect_materiality(
        self,
        current_val,
        baseline_series,
        z_threshold=2.0,
        impact_threshold=0.05
    ):

        start_time = time.time()

        baseline_series = list(baseline_series)

        if len(baseline_series) < 14:

            if baseline_series and baseline_series[-1] != 0:

                pct_change = (
                    (current_val - baseline_series[-1])
                    / baseline_series[-1]
                )

            else:

                pct_change = 0

            is_material = abs(pct_change) >= impact_threshold

            method_used = "Cross-sectional Benchmark (Sparse History)"

            z_score = 0

        else:

            mean = np.mean(baseline_series)
            std = np.std(baseline_series)

            z_score = (
                (current_val - mean) / std
                if std > 0
                else 0
            )

            pct_change = (
                (current_val - mean) / mean
                if mean > 0
                else 0
            )

            is_material = (
                abs(z_score) >= z_threshold
                and abs(pct_change) >= impact_threshold
            )

            method_used = "Z-Score Anomaly Detection"

        # Runtime latency is real analytical processing latency.
        self.telemetry["latency_ms"] += round(
            (time.time() - start_time) * 1000,
            2
        )

        return {
            "is_material": is_material,
            "z_score": z_score,
            "pct_change": pct_change,
            "method": method_used
        }


    # =====================================================
    # UNSTRUCTURED EVIDENCE
    # =====================================================

    def retrieve_unstructured_evidence(self, driver_focus):

        if driver_focus == "Enterprise Cloud Hosting":

            return [
                {
                    "source": "Support Tickets",
                    "signal": (
                        "300% spike in outage and latency tags "
                        "in US-West data centers."
                    )
                },
                {
                    "source": "CRM Notes",
                    "signal": (
                        "Major enterprise accounts threatening "
                        "non-renewal over missed uptime SLAs."
                    )
                }
            ]

        return []


    # =====================================================
    # CONFIDENCE
    # =====================================================

    def determine_confidence(
        self,
        structured_variance,
        unstructured_evidence
    ):

        evidence_count = len(unstructured_evidence)

        if evidence_count < 1 and structured_variance < 0.4:

            return "LOW - ABSTAIN"

        elif evidence_count >= 2 and structured_variance >= 0.6:

            return "HIGH"

        return "MEDIUM"


    # =====================================================
    # NARRATIVE GENERATION
    # =====================================================

    def generate_narrative(
        self,
        persona,
        context,
        confidence
    ):
        """
        Current prototype uses deterministic templates.

        No external LLM/API is called here.
        Therefore:
            llm_calls = 0
            tokens_used = 0
            est_cost_usd = 0.0
        """

        if "ABSTAIN" in confidence:

            return (
                "⚠️ **ABSTAIN:** Q3 Marketing ROI shows a sudden drop, "
                "but Google Ads API data and Salesforce attribution are "
                "currently out of sync. The engine refuses to generate "
                "a causal root cause until the data mismatch is resolved."
            )

        if persona == "CEO":

            return (
                "Revenue is materially below baseline. "
                "**Enterprise Cloud Hosting** is the primary "
                "quantified contributor. Operational and customer "
                "signals indicate possible fulfilment and SLA issues, "
                "but the available evidence does not establish causality."
            )

        elif persona == "Sales Manager":

            return (
                "**Driver:** Enterprise customer volume decline\n\n"
                "**Lever:** Customer retention\n\n"
                "**Action:** Prioritise affected enterprise accounts "
                "for proactive recovery outreach.\n\n"
                "**Owner:** Sales + Customer Success\n\n"
                f"**Confidence:** {confidence}"
            )

        return (
            "The insight is based on deterministic KPI analysis, "
            "contribution analysis and available supporting evidence."
        )
