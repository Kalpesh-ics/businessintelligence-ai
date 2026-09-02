from __future__ import annotations

import statistics
import time
from dataclasses import asdict, dataclass
from typing import Any, Dict, List


@dataclass
class Telemetry:
    analytical_latency_ms: int = 0
    materiality_runs: int = 0
    evidence_runs: int = 0
    llm_calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_llm_cost_usd: float = 0.0
    last_llm_latency_ms: int = 0
    last_llm_status: str = "Not used"

    @property
    def latency_ms(self) -> int:
        return self.analytical_latency_ms

    @property
    def tokens_used(self) -> int:
        return self.total_tokens

    @property
    def est_cost_usd(self) -> float:
        return self.estimated_llm_cost_usd

    def snapshot(self) -> Dict[str, Any]:
        payload = asdict(self)
        payload["latency_ms"] = self.latency_ms
        payload["tokens_used"] = self.tokens_used
        payload["est_cost_usd"] = self.est_cost_usd
        return payload


class KPIEngine:
    BASELINE_REVENUE = 100_000_000.0
    CURRENT_REVENUE = 91_800_000.0

    REVENUE_CHANGE = CURRENT_REVENUE - BASELINE_REVENUE
    REVENUE_PERCENT_CHANGE = REVENUE_CHANGE / BASELINE_REVENUE
    BUSINESS_IMPACT = abs(REVENUE_CHANGE)

    BASELINE_REVENUE_SERIES = [
        101200, 99800, 100500, 102100, 99500,
        100800, 101400, 99700, 100200, 101100,
        99600, 100900, 101300, 99800, 100700,
        101500, 100100, 99500, 100600, 101200,
        100400, 99800, 100900, 101100, 100300,
        101000, 99700, 100800, 101400, 100500,
    ]

    CONTRIBUTION_PCT = {
        "Product A Volume": 45.0,
        "Enterprise Customer Decline": 29.0,
        "Price": 13.0,
        "Other / Offset": 13.0,
    }

    EVIDENCE = [
        {
            "source": "Support Tickets",
            "text": "300% spike in outage and latency tags in US-West data centers.",
            "freshness": "15 minutes ago",
            "type": "Unstructured signal",
            "classification": "Association",
        },
        {
            "source": "CRM Notes",
            "text": "Major enterprise accounts threatening non-renewal over missed uptime SLAs.",
            "freshness": "4 hours ago",
            "type": "Customer context",
            "classification": "Likely Driver",
        },
        {
            "source": "Operations",
            "text": "Fulfilment SLA declined by 15 points in the affected operating context.",
            "freshness": "30 minutes ago",
            "type": "Operational signal",
            "classification": "Association",
        },
    ]

    ACTIONS = {
        "Protect Enterprise Renewals": {
            "driver": "Enterprise Customer Decline",
            "lever": "Renewal outreach and account recovery",
            "owner": "Regional Sales + Customer Success",
            "confidence": "Medium",
            "expected_impact": "Protect at-risk enterprise revenue",
            "risk": "Requires coordinated account prioritisation",
            "min_budget": 25_000,
            "required_authority": "Business Unit",
            "metrics": "Enterprise order volume, renewal probability, support activity",
        },
        "Fix Product A Fulfilment": {
            "driver": "Product A Volume",
            "lever": "Operational recovery and fulfilment SLA",
            "owner": "Operations + Product",
            "confidence": "Medium",
            "expected_impact": "Recover lost Product A volume",
            "risk": "Capacity and service recovery may take time",
            "min_budget": 50_000,
            "required_authority": "Business Unit",
            "metrics": "Product A volume, fulfilment SLA, outage/latency tags",
        },
        "Adjust Pricing": {
            "driver": "Price",
            "lever": "Pricing / discounting",
            "owner": "Commercial + Finance",
            "confidence": "Medium-Low",
            "expected_impact": "Test demand response to pricing",
            "risk": "Margin erosion without clear evidence of price sensitivity",
            "min_budget": 10_000,
            "required_authority": "Enterprise",
            "metrics": "Conversion, realised price, gross margin",
        },
    }

    AUTHORITY_RANK = {
        "Regional": 1,
        "Business Unit": 2,
        "Enterprise": 3,
    }

    def __init__(self) -> None:
        self.telemetry = Telemetry()

    def _update_latency(self, started: float) -> None:
        elapsed = int((time.perf_counter() - started) * 1000)
        self.telemetry.analytical_latency_ms = max(
            self.telemetry.analytical_latency_ms,
            elapsed,
        )

    def detect_materiality(
        self,
        current_val: float,
        baseline_series: List[float],
        z_threshold: float = 2.0,
        impact_threshold: float = 0.05,
    ) -> Dict[str, Any]:
        started = time.perf_counter()
        self.telemetry.materiality_runs += 1

        if not baseline_series:
            self._update_latency(started)
            return {
                "is_material": False,
                "pct_change": 0.0,
                "z_score": 0.0,
                "method": "No Baseline Available",
                "observations": 0,
            }

        baseline_mean = statistics.mean(baseline_series)
        pct_change = (
            (current_val - baseline_mean) / baseline_mean
            if baseline_mean != 0
            else 0.0
        )

        if len(baseline_series) >= 14:
            stdev = statistics.stdev(baseline_series)
            z_score = (
                (current_val - baseline_mean) / stdev
                if stdev > 0
                else 0.0
            )
            is_material = (
                abs(z_score) >= z_threshold
                and abs(pct_change) >= impact_threshold
            )
            method = "Historical Baseline + Z-score + Business Impact"
        else:
            z_score = 0.0
            is_material = abs(pct_change) >= impact_threshold
            method = "Cross-sectional Benchmark (Sparse History)"

        self._update_latency(started)

        return {
            "is_material": bool(is_material),
            "pct_change": pct_change,
            "z_score": z_score,
            "method": method,
            "observations": len(baseline_series),
        }

    def get_revenue_contributions(self) -> List[Dict[str, Any]]:
        rows = []
        for driver, pct in self.CONTRIBUTION_PCT.items():
            rows.append(
                {
                    "Driver": driver,
                    "Contribution (%)": pct,
                    "Impact ($)": self.BUSINESS_IMPACT * pct / 100.0,
                }
            )
        return rows

    def retrieve_unstructured_evidence(self, _topic: str) -> List[Dict[str, Any]]:
        started = time.perf_counter()
        self.telemetry.evidence_runs += 1
        result = list(self.EVIDENCE)
        self._update_latency(started)
        return result

    def determine_confidence(
        self,
        structured_variance: float,
        unstructured_evidence: List[Dict[str, Any]],
    ) -> str:
        evidence_count = len(unstructured_evidence)
        if evidence_count < 1 and structured_variance < 0.4:
            return "LOW — ABSTAIN"
        if evidence_count >= 2 and structured_variance >= 0.6:
            return "HIGH"
        return "MEDIUM"

    def generate_narrative(
        self,
        persona: str,
        materiality: Dict[str, Any],
        confidence: str,
    ) -> str:
        magnitude = abs(self.REVENUE_PERCENT_CHANGE)
        confidence_label = confidence.split(" — ")[0]

        if persona == "CEO":
            return (
                f"US-West revenue is {magnitude:.1%} below the $100.0M baseline, "
                f"representing an $8.2M business impact. Product A Volume is "
                f"the largest quantified contributor at 45%. Operational and "
                f"customer signals support the explanation, but causality is not "
                f"established. Confidence is {confidence_label}."
            )

        if persona == "Sales Manager":
            return (
                f"Revenue is down {magnitude:.1%} in US-West. The largest quantified "
                f"contributor is Product A Volume (45%), while Enterprise Customer "
                f"Decline contributes 29%. Prioritise at-risk accounts and coordinate "
                f"with operations. Confidence is {confidence_label}."
            )

        return (
            f"The material movement is {magnitude:.1%} versus baseline. Product A "
            f"Volume contributes 45%, Enterprise Customer Decline 29%, Price 13%, "
            f"and Other/Offset 13%. Support tickets and CRM notes are consistent "
            f"with the operational/customer explanation, but the evidence supports "
            f"association rather than causal certainty. Confidence is "
            f"{confidence_label}."
        )

    def check_action_compatibility(
        self,
        action_name: str,
        available_budget: int,
        max_discount_pct: float,
        authority: str,
    ) -> Dict[str, Any]:
        action = self.ACTIONS[action_name]
        issues: List[str] = []

        if available_budget < action["min_budget"]:
            issues.append(
                f"Budget shortfall: ${available_budget:,.0f} available vs "
                f"${action['min_budget']:,.0f} required."
            )

        if self.AUTHORITY_RANK[authority] < self.AUTHORITY_RANK[action["required_authority"]]:
            issues.append(
                f"Decision authority is insufficient: {authority} cannot approve "
                f"an action requiring {action['required_authority']} authority."
            )

        if action_name == "Adjust Pricing" and max_discount_pct <= 0:
            issues.append(
                "Pricing action is incompatible with a 0% maximum discount."
            )

        return {
            "compatible": not issues,
            "issues": issues,
        }

    def build_context(
        self,
        persona: str,
        available_budget: int,
        max_discount_pct: float,
        authority: str,
        selected_action: str,
    ) -> Dict[str, Any]:
        materiality = self.detect_materiality(
            self.CURRENT_REVENUE,
            self.BASELINE_REVENUE_SERIES,
        )
        evidence = self.retrieve_unstructured_evidence(
            "Enterprise Cloud Hosting"
        )
        confidence = self.determine_confidence(0.7, evidence)

        return {
            "current_application": {
                "product": "BusinessIntelligence.ai",
                "version": "Round 2 Prototype",
                "data_mode": "Synthetic enterprise data",
                "selected_persona": persona,
                "llm_boundary": (
                    "BI.ai is a language interaction layer. Quantitative truth "
                    "comes from deterministic analytics."
                ),
            },
            "revenue_scenario": {
                "region": "US-West",
                "current": self.CURRENT_REVENUE,
                "baseline": self.BASELINE_REVENUE,
                "movement_pct": self.REVENUE_PERCENT_CHANGE,
                "business_impact": self.BUSINESS_IMPACT,
                "materiality": materiality,
                "confidence": confidence,
                "drivers": self.get_revenue_contributions(),
            },
            "supporting_evidence": evidence,
            "other_scenarios": {
                "Q3 Marketing ROI": {
                    "movement_pct": -0.124,
                    "data_completeness": 0.62,
                    "status": "ABSTAIN",
                    "reason": (
                        "Google Ads attribution and Salesforce attribution are "
                        "out of sync."
                    ),
                },
                "AI Data Center Nodes": {
                    "weekly_active_users": 480,
                    "historical_observations": 5,
                    "method": "Cross-sectional Benchmark (Sparse History)",
                    "status": "LOW CONFIDENCE",
                },
            },
            "decision_workspace": {
                "selected_action": selected_action,
                "constraints": {
                    "available_budget": available_budget,
                    "max_discount_pct": max_discount_pct,
                    "authority": authority,
                },
                "action_definition": self.ACTIONS[selected_action],
                "compatibility": self.check_action_compatibility(
                    selected_action,
                    available_budget,
                    max_discount_pct,
                    authority,
                ),
            },
            "governance": {
                "lineage": [
                    "ERP / Sales",
                    "Enterprise Warehouse",
                    "Governed KPI Layer",
                    "Materiality Detection",
                    "Contribution Analysis",
                    "Evidence Retrieval",
                    "Confidence Assessment",
                    "BI.ai Assistant",
                    "Decision Workspace",
                ],
                "causal_boundary": (
                    "Contribution and association do not automatically establish causation."
                ),
                "abstention_boundary": (
                    "Incomplete or contradictory evidence should result in abstention."
                ),
            },
        }
