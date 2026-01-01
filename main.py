"""
Environmental Policy Analyzer
AI-powered assessment of environmental policies and impact prediction
Author: Pranay M
"""

import ollama
import json
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
import sys

console = Console()
MODEL = "llama3.2"
DATA_DIR = Path("policy_data")
DATA_DIR.mkdir(exist_ok=True)


class PolicyParser:
    """Parse environmental policy documents"""
    
    def parse(self, policy_text: str) -> dict:
        prompt = f"""Parse this environmental policy document:

POLICY TEXT:
{policy_text[:4000]}

Extract:
1. Policy Name/Title
2. Issuing Authority
3. Date/Timeframe
4. Policy Objectives
5. Key Provisions (main rules/requirements)
6. Affected Sectors
7. Enforcement Mechanisms
8. Penalties/Incentives
9. Reporting Requirements
10. Implementation Timeline

Format as JSON."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        try:
            text = response['response']
            start = text.find('{')
            end = text.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(text[start:end])
        except:
            pass
        return {"raw": response['response']}


class ImpactPredictor:
    """Predict environmental policy impacts"""
    
    def predict_environmental(self, policy: dict) -> str:
        prompt = f"""Predict environmental impacts of this policy:

POLICY: {json.dumps(policy, indent=2, default=str)[:2000]}

Analyze impacts on:
1. **Air Quality**: Emissions changes, health effects
2. **Water Resources**: Quality, availability
3. **Land Use**: Habitat, agriculture, development
4. **Biodiversity**: Species, ecosystems
5. **Climate**: GHG emissions, carbon footprint
6. **Waste**: Generation, disposal, recycling

For each, provide:
- Short-term impact (1-2 years)
- Long-term impact (5-10 years)
- Confidence level (High/Medium/Low)
- Key uncertainties"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def predict_economic(self, policy: dict) -> str:
        prompt = f"""Predict economic impacts of this environmental policy:

POLICY: {json.dumps(policy, indent=2, default=str)[:2000]}

Analyze:
1. **Industry Costs**: Compliance costs by sector
2. **Job Impacts**: Job creation/losses
3. **Innovation**: Technology development incentives
4. **Market Effects**: Price changes, competition
5. **Investment**: Green investment flows
6. **Trade**: Import/export implications
7. **GDP Impact**: Overall economic effect

Include:
- Winners and losers
- Transition costs
- Long-term economic benefits"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def predict_social(self, policy: dict) -> str:
        prompt = f"""Predict social impacts of this environmental policy:

POLICY: {json.dumps(policy, indent=2, default=str)[:2000]}

Analyze:
1. **Health Impacts**: Public health changes
2. **Environmental Justice**: Equity considerations
3. **Community Effects**: Local impacts
4. **Behavior Change**: Required lifestyle adjustments
5. **Access**: Effects on transportation, housing
6. **Public Support**: Likely acceptance/resistance

Consider:
- Vulnerable populations
- Urban vs rural impacts
- Generational effects"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class PolicyComparator:
    """Compare environmental policies"""
    
    def compare(self, policy1: dict, policy2: dict) -> str:
        prompt = f"""Compare these two environmental policies:

POLICY 1:
{json.dumps(policy1, indent=2, default=str)[:1500]}

POLICY 2:
{json.dumps(policy2, indent=2, default=str)[:1500]}

Compare:
1. **Stringency**: Which is more strict?
2. **Scope**: Coverage breadth
3. **Mechanisms**: Regulatory vs market-based
4. **Enforcement**: Implementation strength
5. **Flexibility**: Compliance options
6. **Cost-Effectiveness**: Efficiency
7. **Innovation Incentives**: Technology push

Provide:
- Side-by-side comparison table
- Strengths and weaknesses of each
- Recommendation on which approach is better and why"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class EffectivenessEvaluator:
    """Evaluate policy effectiveness"""
    
    def evaluate(self, policy: dict, outcomes: str = "") -> str:
        prompt = f"""Evaluate the potential effectiveness of this environmental policy:

POLICY:
{json.dumps(policy, indent=2, default=str)[:2000]}

OBSERVED OUTCOMES (if any):
{outcomes[:500]}

Evaluate against:
1. **Goal Achievement**: Will it meet stated objectives?
2. **Cost-Effectiveness**: Is this the most efficient approach?
3. **Enforceability**: Can it be enforced practically?
4. **Measurability**: Can progress be tracked?
5. **Adaptability**: Can it adjust to new information?
6. **Political Feasibility**: Is it politically sustainable?
7. **Unintended Consequences**: Potential negative effects

Rate overall effectiveness: High/Medium/Low
Suggest improvements."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class StakeholderAnalyzer:
    """Analyze stakeholder impacts"""
    
    def analyze(self, policy: dict) -> str:
        prompt = f"""Analyze stakeholder impacts for this environmental policy:

POLICY:
{json.dumps(policy, indent=2, default=str)[:2000]}

Identify and analyze key stakeholders:
1. **Government**: Federal, state, local
2. **Industry**: Affected businesses by sector
3. **NGOs**: Environmental groups
4. **Communities**: Affected populations
5. **Consumers**: Public impact
6. **Workers**: Employment effects
7. **International**: Cross-border implications

For each stakeholder:
- Interest in the policy
- Potential support/opposition
- Key concerns
- Recommended engagement strategy"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class RecommendationEngine:
    """Generate policy recommendations"""
    
    def recommend_improvements(self, policy: dict, analysis: dict) -> str:
        prompt = f"""Based on this policy analysis, recommend improvements:

POLICY:
{json.dumps(policy, indent=2, default=str)[:1500]}

ANALYSIS FINDINGS:
{json.dumps(analysis, indent=2, default=str)[:1500]}

Provide:
1. **Critical Gaps**: What's missing?
2. **Strengthening Options**: How to make it more effective
3. **Cost Reduction**: Ways to reduce compliance burden
4. **Equity Improvements**: Better environmental justice
5. **Implementation**: Practical improvements
6. **Monitoring**: Better tracking mechanisms

For each recommendation:
- Specific change
- Expected benefit
- Implementation difficulty"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def design_new_policy(self, objective: str, constraints: str = "") -> str:
        prompt = f"""Design an environmental policy for this objective:

OBJECTIVE: {objective}
CONSTRAINTS: {constraints}

Design a comprehensive policy including:
1. **Title and Purpose**
2. **Specific Targets** (quantified goals)
3. **Regulatory Mechanisms**
4. **Economic Instruments** (taxes, subsidies, trading)
5. **Standards** (performance, technology)
6. **Enforcement Framework**
7. **Reporting Requirements**
8. **Timeline and Milestones**
9. **Stakeholder Responsibilities**
10. **Review and Adjustment Process

Make it practical and implementable."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class ReportGenerator:
    """Generate comprehensive policy reports"""
    
    def generate(self, policy: dict, analyses: dict) -> str:
        prompt = f"""Generate a comprehensive environmental policy analysis report:

POLICY:
{json.dumps(policy, indent=2, default=str)[:1500]}

ANALYSES:
{json.dumps(analyses, indent=2, default=str)[:2000]}

Create a professional report with:
1. Executive Summary
2. Policy Overview
3. Environmental Impact Assessment
4. Economic Impact Assessment
5. Social Impact Assessment
6. Stakeholder Analysis
7. Effectiveness Evaluation
8. Recommendations
9. Implementation Considerations
10. Conclusion

Format as a professional policy analysis document."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


# ============= CLI Interface =============

def show_banner():
    banner = """
╔══════════════════════════════════════════════════════════════╗
║          🌍 Environmental Policy Analyzer 🌍                  ║
║           AI-Powered Policy Assessment Tool                   ║
║                   Author: Pranay M                            ║
╚══════════════════════════════════════════════════════════════╝
    """
    console.print(Panel(banner, style="bold green"))


def show_menu():
    table = Table(title="Policy Tools", show_header=False, box=None)
    table.add_column("Option", style="cyan")
    table.add_column("Description")
    
    table.add_row("1", "📄 Parse Policy Document")
    table.add_row("2", "🌱 Predict Environmental Impact")
    table.add_row("3", "💰 Predict Economic Impact")
    table.add_row("4", "👥 Predict Social Impact")
    table.add_row("5", "⚖️  Compare Policies")
    table.add_row("6", "📊 Evaluate Effectiveness")
    table.add_row("7", "🎯 Stakeholder Analysis")
    table.add_row("8", "💡 Design New Policy")
    table.add_row("9", "📑 Generate Full Report")
    table.add_row("0", "🚪 Exit")
    
    console.print(table)


current_policy = {}


def get_text_input() -> str:
    console.print("\n[cyan]Enter policy text (press Enter twice when done):[/cyan]")
    lines = []
    empty_count = 0
    while True:
        try:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines).strip()


def parse_policy():
    global current_policy
    text = get_text_input()
    if not text:
        console.print("[red]No text provided[/red]")
        return
    
    parser = PolicyParser()
    
    with Progress(SpinnerColumn(), TextColumn("Parsing policy...")) as progress:
        task = progress.add_task("", total=None)
        current_policy = parser.parse(text)
    
    if 'raw' in current_policy:
        console.print(Panel(current_policy['raw'], title="Parsed Policy"))
    else:
        console.print(Panel(json.dumps(current_policy, indent=2), title="Parsed Policy"))


def predict_environmental():
    global current_policy
    if not current_policy:
        console.print("[yellow]Parse a policy first, or enter policy details:[/yellow]")
        name = Prompt.ask("Policy name")
        objectives = Prompt.ask("Main objectives")
        provisions = Prompt.ask("Key provisions")
        current_policy = {"name": name, "objectives": objectives, "provisions": provisions}
    
    predictor = ImpactPredictor()
    
    with Progress(SpinnerColumn(), TextColumn("Predicting impacts...")) as progress:
        task = progress.add_task("", total=None)
        impact = predictor.predict_environmental(current_policy)
    
    console.print(Panel(impact, title="Environmental Impact Prediction"))


def predict_economic():
    global current_policy
    if not current_policy:
        console.print("[yellow]Parse a policy first[/yellow]")
        return
    
    predictor = ImpactPredictor()
    
    with Progress(SpinnerColumn(), TextColumn("Predicting...")) as progress:
        task = progress.add_task("", total=None)
        impact = predictor.predict_economic(current_policy)
    
    console.print(Panel(impact, title="Economic Impact Prediction"))


def predict_social():
    global current_policy
    if not current_policy:
        console.print("[yellow]Parse a policy first[/yellow]")
        return
    
    predictor = ImpactPredictor()
    
    with Progress(SpinnerColumn(), TextColumn("Predicting...")) as progress:
        task = progress.add_task("", total=None)
        impact = predictor.predict_social(current_policy)
    
    console.print(Panel(impact, title="Social Impact Prediction"))


def compare_policies():
    console.print("[cyan]Enter first policy details:[/cyan]")
    name1 = Prompt.ask("Policy 1 name")
    desc1 = Prompt.ask("Policy 1 description")
    
    console.print("[cyan]Enter second policy details:[/cyan]")
    name2 = Prompt.ask("Policy 2 name")
    desc2 = Prompt.ask("Policy 2 description")
    
    comparator = PolicyComparator()
    
    with Progress(SpinnerColumn(), TextColumn("Comparing...")) as progress:
        task = progress.add_task("", total=None)
        comparison = comparator.compare(
            {"name": name1, "description": desc1},
            {"name": name2, "description": desc2}
        )
    
    console.print(Panel(comparison, title="Policy Comparison"))


def evaluate_effectiveness():
    global current_policy
    if not current_policy:
        console.print("[yellow]Parse a policy first[/yellow]")
        return
    
    outcomes = Prompt.ask("Known outcomes (optional)", default="")
    
    evaluator = EffectivenessEvaluator()
    
    with Progress(SpinnerColumn(), TextColumn("Evaluating...")) as progress:
        task = progress.add_task("", total=None)
        evaluation = evaluator.evaluate(current_policy, outcomes)
    
    console.print(Panel(evaluation, title="Effectiveness Evaluation"))


def stakeholder_analysis():
    global current_policy
    if not current_policy:
        console.print("[yellow]Parse a policy first[/yellow]")
        return
    
    analyzer = StakeholderAnalyzer()
    
    with Progress(SpinnerColumn(), TextColumn("Analyzing stakeholders...")) as progress:
        task = progress.add_task("", total=None)
        analysis = analyzer.analyze(current_policy)
    
    console.print(Panel(analysis, title="Stakeholder Analysis"))


def design_policy():
    objective = Prompt.ask("Policy objective")
    constraints = Prompt.ask("Constraints (budget, timeline, etc.)", default="")
    
    engine = RecommendationEngine()
    
    with Progress(SpinnerColumn(), TextColumn("Designing policy...")) as progress:
        task = progress.add_task("", total=None)
        policy = engine.design_new_policy(objective, constraints)
    
    console.print(Panel(policy, title="New Policy Design"))


def generate_report():
    global current_policy
    if not current_policy:
        console.print("[yellow]Parse a policy first[/yellow]")
        return
    
    predictor = ImpactPredictor()
    evaluator = EffectivenessEvaluator()
    reporter = ReportGenerator()
    
    analyses = {}
    
    with Progress(SpinnerColumn(), TextColumn("Generating report...")) as progress:
        task = progress.add_task("", total=None)
        
        progress.update(task, description="Environmental analysis...")
        analyses['environmental'] = predictor.predict_environmental(current_policy)
        
        progress.update(task, description="Economic analysis...")
        analyses['economic'] = predictor.predict_economic(current_policy)
        
        progress.update(task, description="Effectiveness evaluation...")
        analyses['effectiveness'] = evaluator.evaluate(current_policy)
        
        progress.update(task, description="Generating report...")
        report = reporter.generate(current_policy, analyses)
    
    console.print(Panel(report[:3000] + "..." if len(report) > 3000 else report, title="Policy Analysis Report"))
    
    if Confirm.ask("Save report?"):
        filename = f"policy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        Path(filename).write_text(report)
        console.print(f"[green]Saved to {filename}[/green]")


def main():
    show_banner()
    
    try:
        ollama.list()
    except Exception:
        console.print("[red]Error: Ollama not running. Start with: ollama serve[/red]")
        sys.exit(1)
    
    while True:
        show_menu()
        choice = Prompt.ask("\nSelect option", default="0")
        
        actions = {
            "1": parse_policy, "2": predict_environmental, "3": predict_economic,
            "4": predict_social, "5": compare_policies, "6": evaluate_effectiveness,
            "7": stakeholder_analysis, "8": design_policy, "9": generate_report
        }
        
        if choice == "0":
            console.print("[yellow]Goodbye![/yellow]")
            break
        elif choice in actions:
            actions[choice]()
        else:
            console.print("[red]Invalid option[/red]")
        
        console.print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
