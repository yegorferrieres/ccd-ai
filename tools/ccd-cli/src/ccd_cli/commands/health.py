"""
Health Command

Check CCD project health and status.
"""

from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text

from ..core import CCDProject
from ..utils.errors import CCDError

console = Console()


def health_command(ctx, detailed: bool, output_format: str):
    """
    Check CCD project health.
    
    Args:
        ctx: Click context
        detailed: Show detailed health information
        output_format: Output format (text, json, yaml)
    """
    try:
        # Find CCD project
        project_path = _find_ccd_project()
        if not project_path:
            raise CCDError("No CCD project found in current directory or parents")
        
        # Load project
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Loading CCD project...", total=None)
            project = CCDProject(project_path)
            project.load()
            progress.update(task, description="Analyzing project health...")
        
        # Get health report
        health_report = project.get_health_report()
        
        # Display results
        if output_format == "text":
            _display_health_text(health_report, detailed)
        elif output_format == "json":
            _display_health_json(health_report)
        elif output_format == "yaml":
            _display_health_yaml(health_report)
        else:
            raise CCDError(f"Unsupported output format: {output_format}")
            
    except Exception as e:
        raise CCDError(f"Failed to check project health: {str(e)}")


def _find_ccd_project() -> Path:
    """Find CCD project root directory."""
    current_dir = Path.cwd()
    
    # Check current directory and parents for CCD indicators
    for i in range(5):  # Check up to 5 levels up
        if _is_ccd_project(current_dir):
            return current_dir
        current_dir = current_dir.parent
        if current_dir == current_dir.parent:  # Reached root
            break
    
    return None


def _is_ccd_project(directory: Path) -> bool:
    """Check if directory is a CCD project."""
    indicators = [
        'docs/CODEMAP.yaml',
        'docs/00-manifest.md',
        'ccd.config.yaml',
        '.ccd.yaml'
    ]
    
    return any((directory / indicator).exists() for indicator in indicators)


def _display_health_text(health_report: dict, detailed: bool):
    """Display health report in text format."""
    
    # Overall health score
    score = health_report.get('health_score', 0)
    score_color = _get_score_color(score)
    
    console.print(Panel(
        f"[bold]Project Health Score:[/bold] [{score_color}]{score}/100[/{score_color}]",
        title="CCD Project Health",
        border_style=score_color
    ))
    
    # Basic metrics
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="white")
    table.add_column("Status", style="green")
    
    # Coverage
    coverage = health_report.get('coverage_percentage', 0)
    coverage_status = _get_coverage_status(coverage)
    table.add_row("Context Coverage", f"{coverage:.1f}%", coverage_status)
    
    # Freshness
    freshness = health_report.get('freshness_percentage', 0)
    freshness_status = _get_freshness_status(freshness)
    table.add_row("Context Freshness", f"{freshness:.1f}%", freshness_status)
    
    # Modules
    modules = health_report.get('total_modules', 0)
    table.add_row("Total Modules", str(modules), "✓" if modules > 0 else "⚠")
    
    # Files
    files = health_report.get('total_files', 0)
    table.add_row("Total Files", str(files), "✓" if files > 0 else "⚠")
    
    # Context Cards
    context_cards = health_report.get('total_context_cards', 0)
    table.add_row("Context Cards", str(context_cards), "✓" if context_cards > 0 else "⚠")
    
    # Last Updated
    last_updated = health_report.get('last_updated')
    if last_updated:
        table.add_row("Last Updated", last_updated, "✓")
    else:
        table.add_row("Last Updated", "Never", "⚠")
    
    console.print(table)
    
    # Recommendations
    recommendations = health_report.get('recommendations', [])
    if recommendations:
        console.print("\n[bold]Recommendations:[/bold]")
        for i, rec in enumerate(recommendations, 1):
            console.print(f"{i}. {rec}")
    
    # Detailed information
    if detailed:
        _display_detailed_health(health_report)


def _display_detailed_health(health_report: dict):
    """Display detailed health information."""
    console.print("\n" + "="*60)
    console.print("[bold]Detailed Health Analysis[/bold]")
    console.print("="*60)
    
    # Project information
    project_name = health_report.get('project_name', 'Unknown')
    console.print(f"\n[bold]Project:[/bold] {project_name}")
    
    # Health breakdown
    score = health_report.get('health_score', 0)
    console.print(f"\n[bold]Health Score Breakdown:[/bold]")
    
    breakdown_table = Table(show_header=True, header_style="bold blue")
    breakdown_table.add_column("Component", style="cyan")
    breakdown_table.add_column("Weight", style="yellow")
    breakdown_table.add_column("Score", style="white")
    breakdown_table.add_column("Contribution", style="green")
    
    # Coverage contribution (40%)
    coverage = health_report.get('coverage_percentage', 0)
    coverage_contribution = min(coverage, 100) * 0.4
    breakdown_table.add_row("Context Coverage", "40%", f"{coverage:.1f}%", f"{coverage_contribution:.1f}")
    
    # Freshness contribution (30%)
    freshness = health_report.get('freshness_percentage', 0)
    freshness_contribution = min(freshness, 100) * 0.3
    breakdown_table.add_row("Context Freshness", "30%", f"{freshness:.1f}%", f"{freshness_contribution:.1f}")
    
    # Module coverage contribution (20%)
    modules = health_report.get('total_modules', 0)
    module_coverage = min(modules / max(1, modules), 1) * 100
    module_contribution = min(module_coverage, 100) * 0.2
    breakdown_table.add_row("Module Coverage", "20%", f"{module_coverage:.1f}%", f"{module_contribution:.1f}")
    
    # File organization contribution (10%)
    context_cards = health_report.get('total_context_cards', 0)
    file_contribution = 10.0 if context_cards > 0 else 0.0
    breakdown_table.add_row("File Organization", "10%", "✓" if context_cards > 0 else "✗", f"{file_contribution:.1f}")
    
    breakdown_table.add_row("", "", "[bold]Total[/bold]", f"[bold]{score:.1f}[/bold]")
    
    console.print(breakdown_table)
    
    # Quality indicators
    console.print(f"\n[bold]Quality Indicators:[/bold]")
    
    quality_table = Table(show_header=True, header_style="bold green")
    quality_table.add_column("Indicator", style="cyan")
    quality_table.add_column("Status", style="white")
    quality_table.add_column("Details", style="white")
    
    # Coverage quality
    coverage_quality = _get_quality_level(coverage)
    quality_table.add_row("Coverage Quality", coverage_quality, _get_coverage_description(coverage))
    
    # Freshness quality
    freshness_quality = _get_quality_level(freshness)
    quality_table.add_row("Freshness Quality", freshness_quality, _get_freshness_description(freshness))
    
    # Module organization
    module_org = "Good" if modules > 0 else "Poor"
    module_desc = f"{modules} modules organized" if modules > 0 else "No modules defined"
    quality_table.add_row("Module Organization", module_org, module_desc)
    
    # File documentation
    file_doc = "Good" if context_cards > 0 else "Poor"
    file_desc = f"{context_cards} files documented" if context_cards > 0 else "No context cards"
    quality_table.add_row("File Documentation", file_doc, file_desc)
    
    console.print(quality_table)


def _display_health_json(health_report: dict):
    """Display health report in JSON format."""
    import json
    console.print(json.dumps(health_report, indent=2))


def _display_health_yaml(health_report: dict):
    """Display health report in YAML format."""
    import yaml
    console.print(yaml.dump(health_report, default_flow_style=False, sort_keys=False))


def _get_score_color(score: float) -> str:
    """Get color for health score."""
    if score >= 80:
        return "green"
    elif score >= 60:
        return "yellow"
    else:
        return "red"


def _get_coverage_status(coverage: float) -> str:
    """Get status for coverage percentage."""
    if coverage >= 90:
        return "🟢 Excellent"
    elif coverage >= 80:
        return "🟡 Good"
    elif coverage >= 60:
        return "🟠 Fair"
    else:
        return "🔴 Poor"


def _get_freshness_status(freshness: float) -> str:
    """Get status for freshness percentage."""
    if freshness >= 95:
        return "🟢 Excellent"
    elif freshness >= 85:
        return "🟡 Good"
    elif freshness >= 70:
        return "🟠 Fair"
    else:
        return "🔴 Poor"


def _get_quality_level(value: float) -> str:
    """Get quality level for a metric."""
    if value >= 90:
        return "🟢 Excellent"
    elif value >= 80:
        return "🟡 Good"
    elif value >= 60:
        return "🟠 Fair"
    else:
        return "🔴 Poor"


def _get_coverage_description(coverage: float) -> str:
    """Get description for coverage level."""
    if coverage >= 90:
        return "Excellent coverage - most files documented"
    elif coverage >= 80:
        return "Good coverage - most important files documented"
    elif coverage >= 60:
        return "Fair coverage - some gaps in documentation"
    else:
        return "Poor coverage - many files lack documentation"


def _get_freshness_description(freshness: float) -> str:
    """Get description for freshness level."""
    if freshness >= 95:
        return "Excellent freshness - documentation is current"
    elif freshness >= 85:
        return "Good freshness - documentation is mostly current"
    elif freshness >= 70:
        return "Fair freshness - some documentation may be stale"
    else:
        return "Poor freshness - documentation is outdated"
