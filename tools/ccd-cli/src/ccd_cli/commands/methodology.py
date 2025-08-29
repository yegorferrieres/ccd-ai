#!/usr/bin/env python3
"""
CCD Methodology Loop Management

Commands for managing the CCD methodology loop including roadmap, engineering log, and decisions.
"""

import click
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.syntax import Syntax
import yaml
from datetime import datetime, timezone
import re

console = Console()

def update_engineering_log(log_file: Path, description: str, impact: str = "Medium", 
                         severity: str = "Medium", technical_changes: str = "", 
                         resolution: str = "", lessons_learned: str = "", 
                         follow_up: str = "") -> bool:
    """Update ENGINEERING_LOG.md with a new entry."""
    if not log_file.exists():
        # Create new engineering log file
        create_engineering_log(log_file)
    
    content = log_file.read_text(encoding='utf-8')
    
    # Generate new entry
    timestamp = datetime.now().strftime("%Y-%m-%d")
    entry = f"""
---

## {timestamp} - {description}

### Description
{description}

### Impact
- **Scope**: {impact}
- **Severity**: {severity}
- **User Impact**: [To be filled]
- **Business Impact**: [To be filled]

### Technical Changes
{technical_changes if technical_changes else "- [To be filled]"}

### Resolution
{resolution if resolution else "- [To be filled]"}

### Lessons Learned
{lessons_learned if lessons_learned else "- [To be filled]"}

### Follow-up Actions
{follow_up if follow_up else "- [ ] [To be filled]"}
"""
    
    # Insert at the beginning after the title
    lines = content.split('\n')
    insert_index = 0
    
    # Find the first entry (after title and description)
    for i, line in enumerate(lines):
        if line.startswith('## ') and ' - ' in line:
            insert_index = i
            break
    
    # Insert new entry
    lines.insert(insert_index, entry)
    
    # Write back to file
    log_file.write_text('\n'.join(lines), encoding='utf-8')
    
    return True

def create_engineering_log(log_file: Path):
    """Create a new engineering log file with template."""
    template = f"""# CCD Engineering Log

This file tracks technical decisions, incidents, and lessons learned during the development of this project.

## {datetime.now().strftime("%Y-%m-%d")} - Engineering Log Created

### Description
Initial engineering log creation for CCD methodology implementation.

### Impact
- **Scope**: Setup
- **Severity**: Low
- **User Impact**: None
- **Business Impact**: None

### Technical Changes
- Created engineering log file
- Established logging structure

### Resolution
- Engineering log ready for use
- Team can now log technical decisions and incidents

### Lessons Learned
- Engineering log is essential for CCD methodology
- Structured logging improves team communication

### Follow-up Actions
- [ ] Log first real development decision
- [ ] Establish logging cadence
- [ ] Train team on logging format

---
"""
    log_file.write_text(template, encoding='utf-8')

def update_roadmap(roadmap_file: Path, milestone: str, status: str = "completed", 
                   notes: str = "") -> bool:
    """Update roadmap.md to mark milestones as completed or in progress."""
    if not roadmap_file.exists():
        console.print(f"[red]Error:[/red] Roadmap file not found: {roadmap_file}")
        return False
    
    content = roadmap_file.read_text(encoding='utf-8')
    
    # Find and update milestone
    lines = content.split('\n')
    updated = False
    
    for i, line in enumerate(lines):
        if milestone.lower() in line.lower() and '[' in line and ']' in line:
            if status == "completed":
                # Mark as completed
                new_line = line.replace('[ ]', '[x]').replace('[ ]', '[x]')
                if '✅' not in new_line:
                    new_line += ' ✅'
            elif status == "in_progress":
                # Mark as in progress
                new_line = line.replace('[x]', '[ ]').replace('[x]', '[ ]')
                if '🔄' not in new_line:
                    new_line += ' 🔄'
            else:
                new_line = line
            
            if notes:
                new_line += f" - {notes}"
            
            lines[i] = new_line
            updated = True
            break
    
    if updated:
        roadmap_file.write_text('\n'.join(lines), encoding='utf-8')
        console.print(f"[green]Successfully updated roadmap milestone: {milestone}[/green]")
        return True
    else:
        console.print(f"[yellow]Warning:[/yellow] Milestone '{milestone}' not found in roadmap")
        return False

def create_adr(decisions_dir: Path, title: str, status: str = "Proposed", 
               context: str = "", decision: str = "", consequences: str = "") -> bool:
    """Create a new Architecture Decision Record (ADR)."""
    if not decisions_dir.exists():
        decisions_dir.mkdir(parents=True, exist_ok=True)
    
    # Find next ADR number
    existing_adrs = list(decisions_dir.glob("*.md"))
    next_number = 1
    
    for adr_file in existing_adrs:
        if adr_file.name.startswith("00"):
            try:
                num = int(adr_file.name.split("-")[0])
                next_number = max(next_number, num + 1)
            except ValueError:
                continue
    
    # Create ADR filename
    filename = f"{next_number:03d}-{title.lower().replace(' ', '-')}.md"
    adr_file = decisions_dir / filename
    
    # Generate ADR content
    timestamp = datetime.now().strftime("%Y-%m-%d")
    adr_content = f"""# [ADR-{next_number:03d}] {title}

## Status
**{status}** - {title}

## Context

{context if context else "[To be filled - Describe the forces at play, including technological, political, social, and project local. These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. It is simply describing facts.]"}

## Decision

{decision if decision else "[To be filled - Describe our response to these forces. It is stated in full sentences, with active voice. 'We will...']"}

## Consequences

{consequences if consequences else "[To be filled - Describe the resulting context, after applying the decision. All consequences should be listed here, not just the 'positive' ones. A particular decision may have positive, negative, and neutral consequences, but all of them are implications of the decision.]"}

## Alternatives Considered

[To be filled - List the alternatives that were considered, and why they were not chosen. This section is optional, but it's good practice to document alternatives that were considered.]

## Implementation Notes

[To be filled - Any notes about the implementation of this decision.]

## Related Decisions

[To be filled - Links to related ADRs or other documentation.]

---

**Date**: {timestamp}  
**Author**: [To be filled]  
**Reviewers**: [To be filled]  
**Status**: {status}
"""
    
    adr_file.write_text(adr_content, encoding='utf-8')
    console.print(f"[green]Successfully created ADR: {adr_file.name}[/green]")
    return True

def update_development_rules(rules_file: Path, new_rule: str, context: str = "", 
                           steps: str = "", validation: str = "") -> bool:
    """Update DEVELOPMENT_RULES.md with new workflow patterns."""
    if not rules_file.exists():
        console.print(f"[red]Error:[/red] Development rules file not found: {rules_file}")
        return False
    
    content = rules_file.read_text(encoding='utf-8')
    
    # Find the end of the file to append new rule
    lines = content.split('\n')
    
    # Generate new rule content
    timestamp = datetime.now().strftime("%Y-%m-%d")
    new_rule_content = f"""

## New Workflow Pattern - {timestamp}

### Context
{context if context else "[To be filled - When to use this pattern]"}

### Steps
{steps if steps else "1. [Step 1]\n2. [Step 2]\n3. [Step 3]"}

### Validation
{validation if validation else "- [ ] [Validation requirement 1]\n- [ ] [Validation requirement 2]"}

---
"""
    
    # Append to the end
    lines.extend(new_rule_content.split('\n'))
    
    rules_file.write_text('\n'.join(lines), encoding='utf-8')
    console.print(f"[green]Successfully added new workflow pattern to development rules[/green]")
    return True

@click.command()
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
def update_engineering_log_cmd(log_file, description, impact, severity, technical_changes, 
                              resolution, lessons_learned, follow_up):
    """Update ENGINEERING_LOG.md with a new entry."""
    try:
        log_path = Path(log_file)
        success = update_engineering_log(
            log_path, description, impact, severity, technical_changes,
            resolution, lessons_learned, follow_up
        )
        
        if success:
            console.print(f"[green]Successfully updated engineering log: {log_path}[/green]")
        else:
            console.print(f"[red]Failed to update engineering log[/red]")
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--roadmap-file', '-r', type=click.Path(), default='./docs/roadmap.md',
              help='Path to roadmap.md file')
@click.option('--milestone', '-m', required=True, help='Milestone to update')
@click.option('--status', '-s', type=click.Choice(['completed', 'in_progress']), default='completed',
              help='New status for the milestone')
@click.option('--notes', '-n', help='Additional notes about the milestone')
def update_roadmap_cmd(roadmap_file, milestone, status, notes):
    """Update roadmap.md to mark milestones as completed or in progress."""
    try:
        roadmap_path = Path(roadmap_file)
        success = update_roadmap(roadmap_path, milestone, status, notes)
        
        if not success:
            raise click.Abort()
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--decisions-dir', '-d', type=click.Path(), default='./docs/decisions',
              help='Path to decisions directory')
@click.option('--title', '-t', required=True, help='Title of the ADR')
@click.option('--status', '-s', type=click.Choice(['Proposed', 'Accepted', 'Deprecated', 'Superseded']),
              default='Proposed', help='Status of the ADR')
@click.option('--context', '-c', help='Context and forces at play')
@click.option('--decision', help='The decision made')
@click.option('--consequences', help='Consequences of the decision')
def create_adr_cmd(decisions_dir, title, status, context, decision, consequences):
    """Create a new Architecture Decision Record (ADR)."""
    try:
        decisions_path = Path(decisions_dir)
        success = create_adr(decisions_path, title, status, context, decision, consequences)
        
        if not success:
            raise click.Abort()
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--rules-file', '-r', type=click.Path(), default='./docs/DEVELOPMENT_RULES.md',
              help='Path to DEVELOPMENT_RULES.md file')
@click.option('--new-rule', '-n', required=True, help='Name of the new workflow pattern')
@click.option('--context', '-c', help='When to use this pattern')
@click.option('--steps', '-s', help='Steps to follow for this pattern')
@click.option('--validation', '-v', help='Validation requirements for this pattern')
def update_development_rules_cmd(rules_file, new_rule, context, steps, validation):
    """Update DEVELOPMENT_RULES.md with new workflow patterns."""
    try:
        rules_path = Path(rules_file)
        success = update_development_rules(rules_path, new_rule, context, steps, validation)
        
        if not success:
            raise click.Abort()
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--project-dir', '-p', type=click.Path(), default='.',
              help='Project directory to analyze')
def methodology_status(project_dir):
    """Show status of all methodological files in the project."""
    try:
        project_path = Path(project_dir)
        
        # Check for methodological files
        files_to_check = [
            ('ENGINEERING_LOG.md', 'docs/ENGINEERING_LOG.md'),
            ('roadmap.md', 'docs/roadmap.md'),
            ('DEVELOPMENT_RULES.md', 'docs/DEVELOPMENT_RULES.md'),
            ('decisions/', 'docs/decisions/')
        ]
        
        table = Table(title="CCD Methodology Status")
        table.add_column("File", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Last Updated", style="yellow")
        table.add_column("Notes", style="blue")
        
        for name, path in files_to_check:
            file_path = project_path / path
            
            if file_path.exists():
                if file_path.is_file():
                    # Get last modified time
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    last_updated = mtime.strftime("%Y-%m-%d")
                    
                    # Check if recently updated (within 7 days)
                    days_old = (datetime.now() - mtime).days
                    if days_old <= 7:
                        status = "✅ Current"
                    elif days_old <= 30:
                        status = "🟡 Recent"
                    else:
                        status = "🔴 Outdated"
                    
                    table.add_row(name, status, last_updated, f"Updated {days_old} days ago")
                else:
                    # Directory
                    adr_files = list(file_path.glob("*.md"))
                    if adr_files:
                        latest_adr = max(adr_files, key=lambda f: f.stat().st_mtime)
                        mtime = datetime.fromtimestamp(latest_adr.stat().st_mtime)
                        last_updated = mtime.strftime("%Y-%m-%d")
                        status = f"✅ {len(adr_files)} ADRs"
                        table.add_row(name, status, last_updated, f"Latest: {latest_adr.name}")
                    else:
                        table.add_row(name, "🟡 Empty", "N/A", "No ADRs found")
            else:
                table.add_row(name, "🔴 Missing", "N/A", "File not found")
        
        console.print(table)
        
        # Summary
        console.print("\n[blue]Methodology Loop Status:[/blue]")
        console.print("• Check ENGINEERING_LOG.md for recent development activities")
        console.print("• Review roadmap.md for current progress and next steps")
        console.print("• Examine decisions/ for architectural decisions")
        console.print("• Follow DEVELOPMENT_RULES.md for workflow guidance")
        
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()
