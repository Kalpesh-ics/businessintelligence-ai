from __future__ import annotations
import statistics, time
from dataclasses import dataclass, asdict
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
    def snapshot(self) -> Dict[str, Any]:
        d = asdict(self); d["tokens_used"] = self.total_tokens; d["est_cost_usd"] = self.estimated_llm_cost_usd; d["latency_ms"] = self.analytical_latency_ms; return d

class KPIEngine:
    BASELINE_REVENUE = 100_000_000.0
    CURRENT_REVENUE = 91_800_000.0
    REVENUE_CHANGE = CURRENT_REVENUE - BASELINE_REVENUE
    REVENUE_PERCENT_CHANGE = REVENUE_CHANGE / BASELINE_REVENUE
    BUSINESS_IMPACT = abs(REVENUE_CHANGE)
    BASELINE_REVENUE_SERIES = [101200,99800,100500,102100,99500,100800,101400,99700,100200,101100,99600,100900,101300,99800,100700,101500,100100,99500,100600,101200,100400,99800,100900,101100,100300,101000,99700,100800,101400,100500]
    CONTRIBUTION_PCT = {"Product A Volume":45.0,"Enterprise Customer Decline":29.0,"Price":13.0,"Other / Offset":13.0}
    EVIDENCE = [
        {"source":"Support Tickets","text":"300% spike in outage and latency tags in US-West data centers.","freshness":"15 minutes ago","type":"Unstructured signal","classification":"Association"},
        {"source":"CRM Notes","text":"Major enterprise accounts threatening non-renewal over missed uptime SLAs.","freshness":"4 hours ago","type":"Customer context","classification":"Likely Driver"},
        {"source":"Operations","text":"Fulfilment SLA declined by 15 points in the affected operating context.","freshness":"30 minutes ago","type":"Operational signal","classification":"Association"},
    ]
    ACTIONS = {
        "Protect Enterprise Renewals":{"driver":"Enterprise Customer Decline","lever":"Renewal outreach and account recovery","owner":"Regional Sales + Customer Success","confidence":"Medium","expected_impact":"Protect at-risk enterprise revenue","risk":"Requires coordinated account prioritisation","min_budget":25000,"required_authority":"Business Unit","metrics":"Enterprise order volume, renewal probability, support activity"},
        "Fix Product A Fulfilment":{"driver":"Product A Volume","lever":"Operational recovery and fulfilment SLA","owner":"Operations + Product","confidence":"Medium","expected_impact":"Recover lost Product A volume","risk":"Capacity and service recovery may take time","min_budget":50000,"required_authority":"Business Unit","metrics":"Product A volume, fulfilment SLA, outage/latency tags"},
        "Adjust Pricing":{"driver":"Price","lever":"Pricing / discounting","owner":"Commercial + Finance","confidence":"Medium-Low","expected_impact":"Test demand response to pricing","risk":"Margin erosion without clear evidence of price sensitivity","min_budget":10000,"required_authority":"Enterprise","metrics":"Conversion, realised price, gross margin"},
    }
    AUTHORITY_RANK = {"Regional":1,"Business Unit":2,"Enterprise":3}

    def __init__(self): self.telemetry = Telemetry()
    def _timed(self, started): self.telemetry.analytical_latency_ms=max(self.telemetry.analytical_latency_ms,int((time.perf_counter()-started)*1000))

    def detect_materiality(self,current_val:float,baseline_series:List[float],z_threshold:float=2.0,impact_threshold:float=0.05):
        started=time.perf_counter(); self.telemetry.materiality_runs+=1
        if not baseline_series: return {"is_material":False,"pct_change":0.0,"z_score":0.0,"method":"No Baseline Available","observations":0}
        mean=statistics.mean(baseline_series); pct=(current_val-mean)/mean if mean else 0.0
        if len(baseline_series)>=14:
            sd=statistics.stdev(baseline_series); z=(current_val-mean)/sd if sd>0 else 0.0
            material=abs(z)>=z_threshold and abs(pct)>=impact_threshold; method="Historical Baseline + Z-score + Business Impact"
        else:
            z=0.0; material=abs(pct)>=impact_threshold; method="Cross-sectional Benchmark (Sparse History)"
        self._timed(started)
        return {"is_material":bool(material),"pct_change":pct,"z_score":z,"method":method,"observations":len(baseline_series)}

    def get_revenue_contributions(self):
        return [{"Driver":d,"Contribution (%)":p,"Impact ($)":self.BUSINESS_IMPACT*p/100.0} for d,p in self.CONTRIBUTION_PCT.items()]
    def retrieve_unstructured_evidence(self,_topic):
        started=time.perf_counter(); self.telemetry.evidence_runs+=1; out=list(self.EVIDENCE); self._timed(started); return out
    def determine_confidence(self,structured_variance:float,unstructured_evidence):
        n=len(unstructured_evidence)
        if n<1 and structured_variance<0.4:return "LOW — ABSTAIN"
        if n>=2 and structured_variance>=0.6:return "HIGH"
        return "MEDIUM"
    def generate_narrative(self,persona,materiality,confidence):
        move=f"{abs(self.REVENUE_PERCENT_CHANGE):.1%}"; c=confidence.split(" — ")[0]
        if persona=="CEO": return f"US-West revenue is {move} below the $100.0M baseline, representing an $8.2M business impact. Product A Volume is the largest quantified contributor at 45%. Operational and customer signals support the explanation, but causality is not established. Confidence is {c}."
        if persona=="Sales Manager": return f"Revenue is down {move} in US-West. The largest quantified contributor is Product A Volume (45%), while enterprise customer risk is 29%. Prioritise at-risk accounts and coordinate with operations. Confidence is {c}."
        return f"The material movement is {move} versus baseline. Product A Volume contributes 45%, Enterprise Customer Decline 29%, Price 13%, and Other/Offset 13%. Support tickets and CRM notes are consistent with the operational/customer explanation, but the evidence supports association rather than causal certainty. Confidence is {c}."
    def check_action_compatibility(self,action_name,available_budget,max_discount_pct,authority):
        a=self.ACTIONS[action_name]; issues=[]
        if available_budget<a["min_budget"]: issues.append(f"Budget shortfall: ${available_budget:,.0f} available vs ${a['min_budget']:,.0f} required.")
        if self.AUTHORITY_RANK[authority]<self.AUTHORITY_RANK[a["required_authority"]]: issues.append(f"Decision authority is insufficient: {authority} cannot approve an action requiring {a['required_authority']} authority.")
        if action_name=="Adjust Pricing" and max_discount_pct<=0: issues.append("Pricing action is incompatible with a 0% maximum discount.")
        return {"compatible":not issues,"issues":issues}
    def build_context(self,persona,available_budget,max_discount_pct,authority,selected_action):
        mat=self.detect_materiality(91_800_000,self.BASELINE_REVENUE_SERIES); evidence=self.retrieve_unstructured_evidence("Enterprise Cloud Hosting"); confidence=self.determine_confidence(0.7,evidence)
        return {"system":{"name":"BusinessIntelligence.ai","purpose":"AI-powered KPI intelligence-to-action engine","data_mode":"Synthetic enterprise data","llm_role":"Natural-language assistant only; it does not calculate quantitative truth."},"persona":persona,"kpi":{"name":"US-West Revenue","current":self.CURRENT_REVENUE,"baseline":self.BASELINE_REVENUE,"movement_pct":self.REVENUE_PERCENT_CHANGE,"business_impact":self.BUSINESS_IMPACT,"materiality":mat,"confidence":confidence},"drivers":self.get_revenue_contributions(),"evidence":evidence,"other_scenarios":{"Q3 Marketing ROI":{"movement_pct":-0.124,"data_completeness":0.62,"decision":"ABSTAIN","reason":"Google Ads and Salesforce attribution conflict."},"AI Data Center Nodes":{"weekly_active_users":480,"historical_observations":5,"method":"Cross-sectional Benchmark (Sparse History)"}},"decision":{"selected_action":selected_action,"available_budget":available_budget,"max_discount_pct":max_discount_pct,"decision_authority":authority,"action_definition":self.ACTIONS[selected_action],"compatibility":self.check_action_compatibility(selected_action,available_budget,max_discount_pct,authority)},"governance":{"evidence_rule":"Contribution and association do not automatically establish causality.","abstention_rule":"Low or contradictory evidence should result in abstention.","lineage":["ERP / Sales","Enterprise Warehouse","Governed KPI Layer","Materiality Detection","Contribution Analysis","Evidence Retrieval","Confidence Assessment","Narrative / BI.ai Assistant","Decision Workspace"]}}
