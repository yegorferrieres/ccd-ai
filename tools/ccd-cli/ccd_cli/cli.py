#!/usr/bin/env python3
"""
CCD CLI - Main entry point

Command-line interface for CCD (Continuous Context Documentation) tool.
"""

import click
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .commands import (
    init_command,
    validate_command,
    generate_command,
    health_command,
    coverage_command,
    freshness_command,
    pack_command,
    monitor_command,
    version_command,
    
    # AI-CONTEXT Comments Management
    add_context_comments,
    extract_context,
    validate_context_comments,
    
    # Methodology Loop Management
    update_engineering_log_cmd,
    update_roadmap_cmd,
    create_adr_cmd,
    update_development_rules_cmd,
    methodology_status,
    
    # Quality Gates and Validation
    context_freshness,
    context_health,
    drift_detection,
    quality_gates,
    
    # Context Preparation for AI
    prepare_context_cmd,
)
from .utils.config import load_config
from .utils.errors import CCDError

console = Console()

def print_banner():
    """Print CCD CLI banner."""
    banner = Text("CCD CLI", style="bold blue")
    subtitle = Text("Continuous Context Documentation", style="italic")
    
    panel = Panel(
        f"{banner}\n{subtitle}",
        border_style="blue",
        padding=(1, 2)
    )
    console.print(panel)

@click.group()
@click.option('--config', '-c', type=click.Path(exists=True), help='Configuration file path')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.option('--quiet', '-q', is_flag=True, help='Suppress output')
@click.pass_context
def cli(ctx, config, verbose, quiet):
    """
    CCD (Continuous Context Documentation) CLI Tool
    
    Manage and maintain continuous context documentation in your software projects.
    """
    # Ensure context object exists
    ctx.ensure_object(dict)
    
    # Load configuration
    if config:
        ctx.obj['config'] = load_config(config)
    else:
        ctx.obj['config'] = load_config()
    
    # Set verbosity
    ctx.obj['verbose'] = verbose
    ctx.obj['quiet'] = quiet
    
    # Set console verbosity
    if quiet:
        console.quiet = True
    elif verbose:
        console.verbose = True

@cli.command()
@click.option('--project-name', '-n', required=True, help='Project name')
@click.option('--domain', '-d', required=True, 
              type=click.Choice(['web-application', 'mobile-app', 'api-service', 'library', 'cli-tool', 'data-pipeline', 'ml-ai', 'infrastructure', 'other']),
              help='Project domain')
@click.option('--yes', '-y', is_flag=True, help='Skip prompts and use defaults')
@click.option('--output-dir', '-o', type=click.Path(), default='.', help='Output directory')
@click.pass_context
def init(ctx, project_name, domain, yes, output_dir):
    """Initialize a new CCD project."""
    try:
        init_command(ctx, project_name, domain, yes, output_dir)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--schemas', '-s', type=click.Path(), default='./docs/schemas', 
              help='Path to schemas directory')
@click.option('--contexts', '-c', type=click.Path(), default='./docs', 
              help='Path to contexts directory')
@click.option('--output-format', '-f', type=click.Choice(['text', 'json', 'yaml']), 
              default='text', help='Output format')
@click.option('--detailed', '-d', is_flag=True, help='Show detailed validation results')
@click.pass_context
def validate(ctx, schemas, contexts, output_format, detailed):
    """Validate CCD schemas and contexts."""
    try:
        validate_command(ctx, schemas, contexts, output_format, detailed)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--files', '-f', required=True, help='File pattern to process (e.g., "src/**/*.py")')
@click.option('--output', '-o', required=True, type=click.Path(), help='Output directory')
@click.option('--type', '-t', type=click.Choice(['cards', 'index', 'codemap']), 
              default='cards', help='What to generate')
@click.option('--force', is_flag=True, help='Overwrite existing files')
@click.pass_context
def generate(ctx, files, output, type, force):
    """Generate CCD documentation files."""
    try:
        generate_command(ctx, files, output, type, force)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--detailed', '-d', is_flag=True, help='Show detailed health information')
@click.option('--output-format', '-f', type=click.Choice(['text', 'json', 'yaml']), 
              default='text', help='Output format')
@click.pass_context
def health(ctx, detailed, output_format):
    """Check CCD project health."""
    try:
        health_command(ctx, detailed, output_format)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--modules', '-m', is_flag=True, help='Show module coverage')
@click.option('--files', '-f', is_flag=True, help='Show file coverage')
@click.option('--min-coverage', type=int, default=80, help='Minimum coverage percentage')
@click.option('--output-format', '-o', type=click.Choice(['text', 'json', 'yaml']), 
              default='text', help='Output format')
@click.pass_context
def coverage(ctx, modules, files, min_coverage, output_format):
    """Show CCD coverage statistics."""
    try:
        coverage_command(ctx, modules, files, min_coverage, output_format)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--days', '-d', type=int, default=30, help='Number of days to check')
@click.option('--output-format', '-o', type=click.Choice(['text', 'json', 'yaml']), 
              default='text', help='Output format')
@click.pass_context
def freshness(ctx, days, output_format):
    """Check CCD documentation freshness."""
    try:
        freshness_command(ctx, days, output_format)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--output', '-o', type=click.Path(), default='./ccd-contexts.zip', 
              help='Output archive path')
@click.option('--include-schemas', is_flag=True, help='Include JSON schemas')
@click.option('--include-templates', is_flag=True, help='Include templates')
@click.pass_context
def pack(ctx, output, include_schemas, include_templates):
    """Package CCD contexts into archive."""
    try:
        pack_command(ctx, output, include_schemas, include_templates)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--watch', '-w', is_flag=True, help='Watch for file changes')
@click.option('--interval', '-i', type=int, default=60, help='Check interval in seconds')
@click.option('--output-format', '-o', type=click.Choice(['text', 'json', 'yaml']), 
              default='text', help='Output format')
@click.pass_context
def monitor(ctx, watch, interval, output_format):
    """Monitor CCD project status."""
    try:
        monitor_command(ctx, watch, interval, output_format)
    except CCDError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
def version():
    """Show CCD CLI version."""
    version_command()

# Context Preparation for AI Commands

@cli.command(name='prepare-context')
@click.option('--project-dir', '-p', type=click.Path(exists=True), default='.',
              help='Project directory to analyze')
@click.option('--output', '-o', type=click.Path(), help='Output file for context')
@click.option('--no-architecture', is_flag=True, help='Skip architecture decisions and codemap')
@click.option('--dry-run', is_flag=True, help='Show what would be generated without creating file')
def prepare_context_cmd_wrapper(project_dir, output, no_architecture, dry_run):
    """Prepare complete project context for AI developer."""
    try:
        from .commands.prepare_context import prepare_context_impl
        prepare_context_impl(project_dir, output, no_architecture, dry_run)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

# AI-CONTEXT Comments Management Commands

@cli.command()
@click.option('--file', '-f', type=click.Path(exists=True), required=True, help='Source file path')
@click.option('--context', '-c', type=click.Path(exists=True), required=True, help='Context card file path')
@click.option('--force', '-F', is_flag=True, help='Overwrite existing comments')
@click.option('--dry-run', is_flag=True, help='Show what would be added without making changes')
def add_context_comments_cmd(file, context, force, dry_run):
    """Add AI-CONTEXT comments to a source file."""
    try:
        add_context_comments(file, context, force, dry_run)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--files', '-F', type=click.Path(), help='Glob pattern for multiple files')
@click.option('--project', '-p', type=click.Path(), help='Extract from entire project')
@click.option('--output', '-o', type=click.Path(), help='Output file for extracted comments')
def extract_context_cmd(file, files, project, output):
    """Extract AI-CONTEXT comments from source code files."""
    try:
        extract_context(file, files, project, output)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--files', '-F', type=click.Path(), help='Glob pattern for multiple files')
@click.option('--project', '-p', type=click.Path(), help='Validate entire project')
@click.option('--strict', is_flag=True, help='Fail on any validation errors')
@click.option('--report', is_flag=True, help='Generate detailed validation report')
def validate_context_comments_cmd(file, files, project, strict, report):
    """Validate AI-CONTEXT comment format and content."""
    try:
        validate_context_comments(file, files, project, strict, report)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

# Methodology Loop Management Commands

@cli.command()
@click.option('--log-file', '-l', type=click.Path(), default='./docs/ENGINEERING_LOG.md', 
              help='Path to ENGINEERING_LOG.md file')
@click.option('--description', '-d', required=True, help='Description of the development task')
@click.option('--impact', '-i', type=click.Choice(['High', 'Medium', 'Low']), default='Medium',
              help='Impact scope of the task')
@click.option('--severity', '-s', type=click.Choice(['High', 'Medium', 'Low']), default='Medium',
              help='Severity of the task')
@click.option('--technical-changes', '-t', help='Description of technical changes made')
@click.option('--resolution', '-r', help='How the task was resolved')
@click.option('--lessons-learned', help='Key insights gained from the task')
@click.option('--follow-up', help='Next steps or follow-up actions')
def update_engineering_log(log_file, description, impact, severity, technical_changes, 
                          resolution, lessons_learned, follow_up):
    """Update ENGINEERING_LOG.md with a new entry."""
    try:
        update_engineering_log_cmd(log_file, description, impact, severity, technical_changes,
                                 resolution, lessons_learned, follow_up)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--roadmap-file', '-r', type=click.Path(), default='./docs/roadmap.md',
              help='Path to roadmap.md file')
@click.option('--milestone', '-m', required=True, help='Milestone to update')
@click.option('--status', '-s', type=click.Choice(['completed', 'in_progress']), default='completed',
              help='New status for the milestone')
@click.option('--notes', '-n', help='Additional notes about the milestone')
def update_roadmap(roadmap_file, milestone, status, notes):
    """Update roadmap.md to mark milestones as completed or in progress."""
    try:
        update_roadmap_cmd(roadmap_file, milestone, status, notes)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--decisions-dir', '-d', type=click.Path(), default='./docs/decisions',
              help='Path to decisions directory')
@click.option('--title', '-t', required=True, help='Title of the ADR')
@click.option('--status', '-s', type=click.Choice(['Proposed', 'Accepted', 'Deprecated', 'Superseded']),
              default='Proposed', help='Status of the ADR')
@click.option('--context', '-c', help='Context and forces at play')
@click.option('--decision', help='The decision made')
@click.option('--consequences', help='Consequences of the decision')
def create_adr(decisions_dir, title, status, context, decision, consequences):
    """Create a new Architecture Decision Record (ADR)."""
    try:
        create_adr_cmd(decisions_dir, title, status, context, decision, consequences)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--rules-file', '-r', type=click.Path(), default='./docs/DEVELOPMENT_RULES.md',
              help='Path to DEVELOPMENT_RULES.md file')
@click.option('--new-rule', '-n', required=True, help='Name of the new workflow pattern')
@click.option('--context', '-c', help='When to use this pattern')
@click.option('--steps', '-s', help='Steps to follow for this pattern')
@click.option('--validation', '-v', help='Validation requirements for this pattern')
def update_development_rules(rules_file, new_rule, context, steps, validation):
    """Update DEVELOPMENT_RULES.md with new workflow patterns."""
    try:
        update_development_rules_cmd(rules_file, new_rule, context, steps, validation)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--project-dir', '-p', type=click.Path(), default='.',
              help='Project directory to analyze')
def methodology_status_cmd(project_dir):
    """Show status of all methodological files in the project."""
    try:
        methodology_status(project_dir)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

# Quality Gates and Validation Commands

@cli.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--threshold', '-t', type=int, default=24, help='Freshness threshold in hours')
def context_freshness_cmd(file, project, threshold):
    """Check context freshness across the project."""
    try:
        context_freshness(file, project, threshold)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--detailed', '-d', is_flag=True, help='Show detailed health information')
def context_health_cmd(file, project, detailed):
    """Check context health across the project."""
    try:
        context_health(file, project, detailed)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--output', '-o', type=click.Path(), help='Output file for drift report')
def drift_detection_cmd(project, output):
    """Detect context drift in the project."""
    try:
        drift_detection(project, output)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.option('--project', '-p', type=click.Path(), default='.', help='Project directory')
@click.option('--output', '-o', type=click.Path(), help='Output file for quality report')
def quality_gates_cmd(project, output):
    """Run all quality gates for the project."""
    try:
        quality_gates(project, output)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

def main():
    """Main entry point."""
    try:
        print_banner()
        cli()
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")
        if console.verbose:
            console.print_exception()
        sys.exit(1)

if __name__ == '__main__':
    main()
