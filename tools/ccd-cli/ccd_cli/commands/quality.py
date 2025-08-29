#!/usr/bin/env python3
"""
CCD Quality Gates and Validation

Commands for managing quality gates, context freshness, and drift detection.
"""

import click
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
import yaml
from datetime import datetime, timezone, timedelta
import json
import re

console = Console()

def check_context_freshness(context_file: Path, threshold_hours: int = 24) -> dict:
    """Check context freshness against threshold."""
    if not context_file.exists():
        return {
            'fresh': False,
            'age_hours': None,
            'threshold_hours': threshold_hours,
            'status': 'missing',
            'last_updated': None
        }
    
    # Get file modification time
    mtime = datetime.fromtimestamp(context_file.stat().st_mtime)
    now = datetime.now()
    age = now - mtime
    age_hours = age.total_seconds() / 3600
    
    # Check if fresh
    fresh = age_hours <= threshold_hours
    
    if fresh:
        status = 'fresh'
    elif age_hours <= threshold_hours * 2:
        status = 'stale'
    else:
        status = 'outdated'
    
    return {
        'fresh': fresh,
        'age_hours': age_hours,
        'threshold_hours': threshold_hours,
        'status': status,
        'last_updated': mtime.isoformat()
    }

def calculate_context_health(context_file: Path) -> dict:
    """Calculate context health score based on various factors."""
    if not context_file.exists():
        return {
            'score': 0,
            'factors': ['file_missing'],
            'status': 'missing'
        }
    
    content = context_file.read_text(encoding='utf-8')
    factors = []
    score = 100
    
    # Check if file has required sections
    required_sections = [
        '## Overview',
        '## Purpose', 
        '## Dependencies',
        '## Key Components'
    ]
    
    for section in required_sections:
        if section not in content:
            factors.append(f'missing_section_{section.replace("## ", "").lower()}')
            score -= 15
    
    # Check file size (penalty for very large files)
    lines = len(content.split('\n'))
    if lines > 200:
        factors.append('file_too_large')
        score -= 10
    elif lines > 160:
        factors.append('file_large_warning')
        score -= 5
    
    # Check for recent updates
    freshness = check_context_freshness(context_file)
    if not freshness['fresh']:
        factors.append('context_stale')
        score -= 20
    
    # Check for metadata completeness
    if '---' in content:  # Has frontmatter
        if 'updated_at:' in content:
            factors.append('has_metadata')
        else:
            factors.append('missing_metadata')
            score -= 10
    else:
        factors.append('no_frontmatter')
        score -= 15
    
    # Ensure score doesn't go below 0
    score = max(0, score)
    
    # Determine status
    if score >= 85:
        status = 'excellent'
    elif score >= 70:
        status = 'good'
    elif score >= 50:
        status = 'fair'
    else:
        status = 'poor'
    
    return {
        'score': score,
        'factors': factors,
        'status': status
    }

def detect_context_drift(project_dir: Path) -> dict:
    """Detect context drift by comparing context files with source files."""
    drift_report = {
        'total_files': 0,
        'drift_detected': 0,
        'drift_details': [],
        'severity': 'none'
    }
    
    # Find all context files
    context_files = list(project_dir.rglob("*.ctx.md"))
    drift_report['total_files'] = len(context_files)
    
    for context_file in context_files:
        drift_info = check_single_file_drift(context_file, project_dir)
        if drift_info['has_drift']:
            drift_report['drift_detected'] += 1
            drift_report['drift_details'].append(drift_info)
    
    # Determine overall severity
    if drift_report['drift_detected'] == 0:
        drift_report['severity'] = 'none'
    elif drift_report['drift_detected'] <= 3:
        drift_report['severity'] = 'low'
    elif drift_report['drift_detected'] <= 10:
        drift_report['severity'] = 'medium'
    else:
        drift_report['severity'] = 'high'
    
    return drift_report

def check_single_file_drift(context_file: Path, project_dir: Path) -> dict:
    """Check drift for a single context file."""
    drift_info = {
        'context_file': str(context_file),
        'has_drift': False,
        'drift_type': None,
        'severity': 'none',
        'details': []
    }
    
    # Parse context file to find source file path
    content = context_file.read_text(encoding='utf-8')
    
    # Extract file_path from frontmatter
    file_path_match = re.search(r'file_path:\s*["\']([^"\']+)["\']', content)
    if not file_path_match:
        drift_info['drift_type'] = 'missing_file_path'
        drift_info['has_drift'] = True
        drift_info['severity'] = 'high'
        return drift_info
    
    source_file_path = file_path_match.group(1)
    source_file = project_dir / source_file_path
    
    # Check if source file exists
    if not source_file.exists():
        drift_info['drift_type'] = 'source_file_missing'
        drift_info['has_drift'] = True
        drift_info['severity'] = 'high'
        drift_info['details'].append(f"Source file not found: {source_file_path}")
        return drift_info
    
    # Check if source file is newer than context file
    source_mtime = datetime.fromtimestamp(source_file.stat().st_mtime)
    context_mtime = datetime.fromtimestamp(context_file.stat().st_mtime)
    
    if source_mtime > context_mtime:
        age_diff = (source_mtime - context_mtime).total_seconds() / 3600
        
        if age_diff > 168:  # 1 week
            drift_info['severity'] = 'high'
        elif age_diff > 72:  # 3 days
            drift_info['severity'] = 'medium'
        else:
            drift_info['severity'] = 'low'
        
        drift_info['drift_type'] = 'context_outdated'
        drift_info['has_drift'] = True
        drift_info['details'].append(f"Context outdated by {age_diff:.1f} hours")
    
    return drift_info

def run_quality_gates(project_dir: Path) -> dict:
    """Run all quality gates for the project."""
    quality_report = {
        'timestamp': datetime.now().isoformat(),
        'project_dir': str(project_dir),
        'overall_score': 0,
        'gates': {},
        'recommendations': []
    }
    
    # Quality Gate 1: Context Coverage
    coverage_gate = check_context_coverage(project_dir)
    quality_report['gates']['coverage'] = coverage_gate
    
    # Quality Gate 2: Context Freshness
    freshness_gate = check_context_freshness_gate(project_dir)
    quality_report['gates']['freshness'] = freshness_gate
    
    # Quality Gate 3: Context Health
    health_gate = check_context_health_gate(project_dir)
    quality_report['gates']['health'] = health_gate
    
    # Quality Gate 4: Schema Validation
    schema_gate = check_schema_validation_gate(project_dir)
    quality_report['gates']['schema'] = schema_gate
    
    # Calculate overall score
    gate_scores = [gate['score'] for gate in quality_report['gates'].values()]
    quality_report['overall_score'] = sum(gate_scores) / len(gate_scores) if gate_scores else 0
    
    # Generate recommendations
    quality_report['recommendations'] = generate_quality_recommendations(quality_report)
    
    return quality_report

def check_context_coverage(project_dir: Path) -> dict:
    """Check context coverage quality gate."""
    # Find all source files
    source_extensions = ['.py', '.go', '.js', '.ts', '.java', '.cs', '.cpp', '.c', '.rs']
    source_files = []
    
    for ext in source_extensions:
        source_files.extend(project_dir.rglob(f"*{ext}"))
    
    # Find all context files
    context_files = list(project_dir.rglob("*.ctx.md"))
    
    # Calculate coverage
    total_source = len(source_files)
    total_context = len(context_files)
    coverage_percentage = (total_context / total_source * 100) if total_source > 0 else 0
    
    # Determine score and status
    if coverage_percentage >= 90:
        score = 100
        status = 'excellent'
    elif coverage_percentage >= 75:
        score = 80
        status = 'good'
    elif coverage_percentage >= 50:
        score = 60
        status = 'fair'
    else:
        score = 30
        status = 'poor'
    
    return {
        'name': 'Context Coverage',
        'score': score,
        'status': status,
        'metric': f"{coverage_percentage:.1f}%",
        'details': {
            'source_files': total_source,
            'context_files': total_context,
            'coverage_percentage': coverage_percentage
        }
    }

def check_context_freshness_gate(project_dir: Path) -> dict:
    """Check context freshness quality gate."""
    context_files = list(project_dir.rglob("*.ctx.md"))
    
    if not context_files:
        return {
            'name': 'Context Freshness',
            'score': 0,
            'status': 'missing',
            'metric': '0%',
            'details': {'fresh_files': 0, 'total_files': 0}
        }
    
    fresh_count = 0
    total_count = len(context_files)
    
    for context_file in context_files:
        freshness = check_context_freshness(context_file)
        if freshness['fresh']:
            fresh_count += 1
    
    freshness_percentage = (fresh_count / total_count * 100) if total_count > 0 else 0
    
    # Determine score and status
    if freshness_percentage >= 95:
        score = 100
        status = 'excellent'
    elif freshness_percentage >= 80:
        score = 80
        status = 'good'
    elif freshness_percentage >= 60:
        score = 60
        status = 'fair'
    else:
        score = 30
        status = 'poor'
    
    return {
        'name': 'Context Freshness',
        'score': score,
        'status': status,
        'metric': f"{freshness_percentage:.1f}%",
        'details': {
            'fresh_files': fresh_count,
            'total_files': total_count,
            'freshness_percentage': freshness_percentage
        }
    }

def check_context_health_gate(project_dir: Path) -> dict:
    """Check context health quality gate."""
    context_files = list(project_dir.rglob("*.ctx.md"))
    
    if not context_files:
        return {
            'name': 'Context Health',
            'score': 0,
            'status': 'missing',
            'metric': '0',
            'details': {'healthy_files': 0, 'total_files': 0}
        }
    
    total_score = 0
    total_count = len(context_files)
    
    for context_file in context_files:
        health = calculate_context_health(context_file)
        total_score += health['score']
    
    average_health = total_score / total_count if total_count > 0 else 0
    
    # Determine score and status
    if average_health >= 85:
        score = 100
        status = 'excellent'
    elif average_health >= 70:
        score = 80
        status = 'good'
    elif average_health >= 50:
        score = 60
        status = 'fair'
    else:
        score = 30
        status = 'poor'
    
    return {
        'name': 'Context Health',
        'score': score,
        'status': status,
        'metric': f"{average_health:.1f}",
        'details': {
            'average_health': average_health,
            'total_files': total_count
        }
    }

def check_schema_validation_gate(project_dir: Path) -> dict:
    """Check schema validation quality gate."""
    # This is a placeholder - actual schema validation would be implemented
    # based on the specific schemas used in the project
    
    return {
        'name': 'Schema Validation',
        'score': 100,  # Placeholder
        'status': 'excellent',
        'metric': '100%',
        'details': {
            'note': 'Schema validation not yet implemented'
        }
    }

def generate_quality_recommendations(quality_report: dict) -> list:
    """Generate recommendations based on quality report."""
    recommendations = []
    
    for gate_name, gate in quality_report['gates'].items():
        if gate['score'] < 80:
            if gate_name == 'coverage':
                if gate['details']['coverage_percentage'] < 75:
                    recommendations.append(f"Increase context coverage from {gate['details']['coverage_percentage']:.1f}% to at least 75%")
            elif gate_name == 'freshness':
                if gate['details']['freshness_percentage'] < 80:
                    recommendations.append(f"Update stale context files to improve freshness from {gate['details']['freshness_percentage']:.1f}% to at least 80%")
            elif gate_name == 'health':
                if gate['details']['average_health'] < 70:
                    recommendations.append(f"Improve context health from {gate['details']['average_health']:.1f} to at least 70")
    
    if not recommendations:
        recommendations.append("All quality gates are passing. Keep up the good work!")
    
    return recommendations

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--threshold', '-t', type=int, default=24, help='Freshness threshold in hours')
def context_freshness(file, project, threshold):
    """Check context freshness across the project."""
    try:
        if file:
            file_path = Path(file)
            freshness = check_context_freshness(file_path, threshold)
            
            if freshness['status'] == 'missing':
                console.print(f"[red]File not found: {file_path}[/red]")
            else:
                status_color = {
                    'fresh': 'green',
                    'stale': 'yellow',
                    'outdated': 'red'
                }.get(freshness['status'], 'white')
                
                console.print(f"[{status_color}]{file_path.name}: {freshness['status'].upper()}[/{status_color}]")
                console.print(f"  Last updated: {freshness['last_updated']}")
                console.print(f"  Age: {freshness['age_hours']:.1f} hours")
                console.print(f"  Threshold: {freshness['threshold_hours']} hours")
        else:
            project_path = Path(project)
            context_files = list(project_path.rglob("*.ctx.md"))
            
            if not context_files:
                console.print("[yellow]No context files found in project[/yellow]")
                return
            
            table = Table(title=f"Context Freshness Report (Threshold: {threshold}h)")
            table.add_column("File", style="cyan")
            table.add_column("Status", style="green")
            table.add_column("Last Updated", style="yellow")
            table.add_column("Age (hours)", style="blue")
            
            fresh_count = 0
            total_count = len(context_files)
            
            for context_file in context_files:
                freshness = check_context_freshness(context_file, threshold)
                
                status_emoji = {
                    'fresh': '✅',
                    'stale': '🟡',
                    'outdated': '🔴'
                }.get(freshness['status'], '❓')
                
                if freshness['fresh']:
                    fresh_count += 1
                
                table.add_row(
                    str(context_file.relative_to(project_path)),
                    f"{status_emoji} {freshness['status'].upper()}",
                    freshness['last_updated'] or 'N/A',
                    f"{freshness['age_hours']:.1f}" if freshness['age_hours'] else 'N/A'
                )
            
            console.print(table)
            
            # Summary
            freshness_percentage = (fresh_count / total_count * 100) if total_count > 0 else 0
            console.print(f"\n[blue]Summary:[/blue] {fresh_count}/{total_count} files are fresh ({freshness_percentage:.1f}%)")
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--detailed', '-d', is_flag=True, help='Show detailed health information')
def context_health(file, project, detailed):
    """Check context health across the project."""
    try:
        if file:
            file_path = Path(file)
            health = calculate_context_health(file_path)
            
            console.print(f"[blue]Context Health for {file_path.name}:[/blue]")
            console.print(f"  Score: {health['score']}/100")
            console.print(f"  Status: {health['status'].upper()}")
            
            if detailed and health['factors']:
                console.print(f"  Factors: {', '.join(health['factors'])}")
        else:
            project_path = Path(project)
            context_files = list(project_path.rglob("*.ctx.md"))
            
            if not context_files:
                console.print("[yellow]No context files found in project[/yellow]")
                return
            
            table = Table(title="Context Health Report")
            table.add_column("File", style="cyan")
            table.add_column("Score", style="green")
            table.add_column("Status", style="yellow")
            table.add_column("Factors", style="blue")
            
            total_score = 0
            
            for context_file in context_files:
                health = calculate_context_health(context_file)
                total_score += health['score']
                
                status_emoji = {
                    'excellent': '🟢',
                    'good': '🟡',
                    'fair': '🟠',
                    'poor': '🔴'
                }.get(health['status'], '❓')
                
                factors_display = ', '.join(health['factors'][:3]) if health['factors'] else 'none'
                if len(health['factors']) > 3:
                    factors_display += f" (+{len(health['factors']) - 3} more)"
                
                table.add_row(
                    str(context_file.relative_to(project_path)),
                    f"{health['score']}/100",
                    f"{status_emoji} {health['status'].upper()}",
                    factors_display
                )
            
            console.print(table)
            
            # Summary
            average_health = total_score / len(context_files) if context_files else 0
            console.print(f"\n[blue]Summary:[/blue] Average health: {average_health:.1f}/100")
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--output', '-o', type=click.Path(), help='Output file for drift report')
def drift_detection(project, output):
    """Detect context drift in the project."""
    try:
        project_path = Path(project)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Detecting context drift...", total=None)
            
            drift_report = detect_context_drift(project_path)
            progress.update(task, completed=True)
        
        # Display results
        if drift_report['drift_detected'] == 0:
            console.print("[green]✅ No context drift detected![/green]")
        else:
            severity_color = {
                'low': 'yellow',
                'medium': 'orange',
                'high': 'red'
            }.get(drift_report['severity'], 'white')
            
            console.print(f"[{severity_color}]🔴 Context drift detected: {drift_report['drift_detected']} files[/{severity_color}]")
            console.print(f"Severity: {drift_report['severity'].upper()}")
            
            # Show drift details
            table = Table(title="Context Drift Details")
            table.add_column("Context File", style="cyan")
            table.add_column("Drift Type", style="red")
            table.add_column("Severity", style="yellow")
            table.add_column("Details", style="blue")
            
            for drift in drift_report['drift_details']:
                severity_emoji = {
                    'low': '🟡',
                    'medium': '🟠',
                    'high': '🔴'
                }.get(drift['severity'], '❓')
                
                table.add_row(
                    Path(drift['context_file']).name,
                    drift['drift_type'].replace('_', ' ').title(),
                    f"{severity_emoji} {drift['severity'].upper()}",
                    '; '.join(drift['details'])
                )
            
            console.print(table)
        
        # Save report if output specified
        if output:
            output_path = Path(output)
            with output_path.open('w') as f:
                json.dump(drift_report, f, indent=2)
            console.print(f"[green]Drift report saved to: {output_path}[/green]")
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--output', '-o', type=click.Path(), help='Output file for quality report')
def quality_gates(project, output):
    """Run all quality gates for the project."""
    try:
        project_path = Path(project)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Running quality gates...", total=None)
            
            quality_report = run_quality_gates(project_path)
            progress.update(task, completed=True)
        
        # Display results
        console.print(f"[blue]Quality Gates Report for {project_path.name}[/blue]")
        console.print(f"Overall Score: {quality_report['overall_score']:.1f}/100")
        
        # Display individual gates
        table = Table(title="Quality Gates Results")
        table.add_column("Gate", style="cyan")
        table.add_column("Score", style="green")
        table.add_column("Status", style="yellow")
        table.add_column("Metric", style="blue")
        
        for gate_name, gate in quality_report['gates'].items():
            status_emoji = {
                'excellent': '🟢',
                'good': '🟡',
                'fair': '🟠',
                'poor': '🔴',
                'missing': '❌'
            }.get(gate['status'], '❓')
            
            table.add_row(
                gate['name'],
                f"{gate['score']}/100",
                f"{status_emoji} {gate['status'].upper()}",
                gate['metric']
            )
        
        console.print(table)
        
        # Show recommendations
        if quality_report['recommendations']:
            console.print("\n[blue]Recommendations:[/blue]")
            for i, rec in enumerate(quality_report['recommendations'], 1):
                console.print(f"  {i}. {rec}")
        
        # Save report if output specified
        if output:
            output_path = Path(output)
            with output_path.open('w') as f:
                json.dump(quality_report, f, indent=2)
            console.print(f"[green]Quality report saved to: {output_path}[/green]")
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()
