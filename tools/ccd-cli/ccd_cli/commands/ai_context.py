#!/usr/bin/env python3
"""
AI-CONTEXT Comments Management

Commands for managing AI-CONTEXT comments in source code files.
"""

import click
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.syntax import Syntax
import re
import yaml
from datetime import datetime, timezone

console = Console()

def extract_ai_context_comments(file_path: Path) -> dict:
    """Extract AI-CONTEXT comments from a source file."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    content = file_path.read_text(encoding='utf-8')
    comments = {}
    
    # Pattern for AI-CONTEXT comments
    pattern = r'//?\s*AI-CONTEXT:\s*@(\w+):(.+)'
    
    for line in content.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            comments[key] = value
    
    return comments

def validate_ai_context_comments(file_path: Path) -> dict:
    """Validate AI-CONTEXT comments format and content."""
    comments = extract_ai_context_comments(file_path)
    validation = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'missing_required': [],
        'comments': comments
    }
    
    # Required fields
    required_fields = ['file', 'freshness', 'health']
    for field in required_fields:
        if field not in comments:
            validation['missing_required'].append(field)
            validation['valid'] = False
    
    # Validate freshness format (ISO 8601)
    if 'freshness' in comments:
        try:
            datetime.fromisoformat(comments['freshness'].replace('Z', '+00:00'))
        except ValueError:
            validation['errors'].append(f"Invalid freshness format: {comments['freshness']}")
            validation['valid'] = False
    
    # Validate health score (0-100)
    if 'health' in comments:
        try:
            health = int(comments['health'].rstrip('%'))
            if not 0 <= health <= 100:
                validation['warnings'].append(f"Health score out of range: {health}")
        except ValueError:
            validation['errors'].append(f"Invalid health score: {comments['health']}")
            validation['valid'] = False
    
    # Validate file path
    if 'file' in comments:
        context_path = Path(comments['file'])
        if not context_path.exists():
            validation['warnings'].append(f"Context file not found: {comments['file']}")
    
    return validation

def add_ai_context_comments(file_path: Path, context_file: Path, force: bool = False) -> bool:
    """Add AI-CONTEXT comments to a source file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Source file not found: {file_path}")
    
    if not context_file.exists():
        raise FileNotFoundError(f"Context file not found: {context_file}")
    
    # Read source file
    content = file_path.read_text(encoding='utf-8')
    
    # Check if comments already exist
    if 'AI-CONTEXT:' in content and not force:
        console.print(f"[yellow]Warning:[/yellow] AI-CONTEXT comments already exist in {file_path}")
        console.print("Use --force to overwrite existing comments")
        return False
    
    # Generate AI-CONTEXT comments
    comments = generate_ai_context_comments(context_file)
    
    # Determine comment style based on file extension
    comment_style = get_comment_style(file_path)
    
    # Format comments
    formatted_comments = format_ai_context_comments(comments, comment_style)
    
    # Insert comments at the beginning of the file
    lines = content.split('\n')
    
    # Find the first non-comment, non-empty line
    insert_index = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not stripped.startswith(('//', '#', '/*', '<!--')):
            insert_index = i
            break
    
    # Insert comments
    lines.insert(insert_index, '')
    lines.insert(insert_index, formatted_comments)
    
    # Write back to file
    file_path.write_text('\n'.join(lines), encoding='utf-8')
    
    return True

def generate_ai_context_comments(context_file: Path) -> dict:
    """Generate AI-CONTEXT comments from a context card."""
    content = context_file.read_text(encoding='utf-8')
    
    # Parse frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        raise ValueError("Invalid context card format: missing frontmatter")
    
    try:
        metadata = yaml.safe_load(frontmatter_match.group(1))
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in context card: {e}")
    
    # Generate comments
    comments = {
        'file': str(context_file),
        'freshness': datetime.now(timezone.utc).isoformat(),
        'health': '95%',  # Default health score
        'dependencies': metadata.get('dependencies', []),
        'tags': metadata.get('tags', []),
        'owner': metadata.get('owner', ''),
        'review': metadata.get('next_review', ''),
        'status': metadata.get('status', 'active')
    }
    
    return comments

def format_ai_context_comments(comments: dict, style: str) -> str:
    """Format AI-CONTEXT comments according to comment style."""
    if style == 'cpp':
        prefix = '// '
    elif style == 'python':
        prefix = '# '
    elif style == 'html':
        prefix = '<!-- '
        suffix = ' -->'
    else:
        prefix = '// '
        suffix = ''
    
    formatted = []
    for key, value in comments.items():
        if key == 'dependencies' and isinstance(value, list):
            value = ','.join(value)
        elif key == 'tags' and isinstance(value, list):
            value = ','.join(value)
        
        if style == 'html':
            formatted.append(f"{prefix}AI-CONTEXT: @{key}:{value}{suffix}")
        else:
            formatted.append(f"{prefix}AI-CONTEXT: @{key}:{value}")
    
    return '\n'.join(formatted)

def get_comment_style(file_path: Path) -> str:
    """Determine comment style based on file extension."""
    ext = file_path.suffix.lower()
    
    if ext in ['.go', '.js', '.ts', '.java', '.cs', '.cpp', '.c', '.rs']:
        return 'cpp'
    elif ext in ['.py', '.sh', '.yaml', '.yml']:
        return 'python'
    elif ext in ['.html', '.xml']:
        return 'html'
    else:
        return 'cpp'  # Default to C++ style

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), required=True, help='Source file path')
@click.option('--context', '-c', type=click.Path(exists=True), required=True, help='Context card file path')
@click.option('--force', '-F', is_flag=True, help='Overwrite existing comments')
@click.option('--dry-run', is_flag=True, help='Show what would be added without making changes')
def add_context_comments(file, context, force, dry_run):
    """Add AI-CONTEXT comments to a source file."""
    try:
        file_path = Path(file)
        context_file = Path(context)
        
        if dry_run:
            console.print(f"[blue]Dry run mode:[/blue] Would add AI-CONTEXT comments to {file_path}")
            comments = generate_ai_context_comments(context_file)
            comment_style = get_comment_style(file_path)
            formatted = format_ai_context_comments(comments, comment_style)
            
            console.print("\n[green]Comments to be added:[/green]")
            console.print(Syntax(formatted, "text", theme="monokai"))
            return
        
        success = add_ai_context_comments(file_path, context_file, force)
        if success:
            console.print(f"[green]Successfully added AI-CONTEXT comments to {file_path}[/green]")
        else:
            console.print(f"[yellow]No changes made to {file_path}[/yellow]")
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--files', '-F', type=click.Path(), help='Glob pattern for multiple files')
@click.option('--project', '-p', type=click.Path(), help='Extract from entire project')
@click.option('--output', '-o', type=click.Path(), help='Output file for extracted comments')
def extract_context(file, files, project, output):
    """Extract AI-CONTEXT comments from source code files."""
    try:
        if file:
            file_path = Path(file)
            comments = extract_ai_context_comments(file_path)
            
            if output:
                output_path = Path(output)
                yaml.dump(comments, output_path.open('w'), default_flow_style=False)
                console.print(f"[green]Comments extracted to {output_path}[/green]")
            else:
                display_comments(file_path, comments)
                
        elif files:
            # TODO: Implement glob pattern extraction
            console.print("[yellow]Glob pattern extraction not yet implemented[/yellow]")
            
        elif project:
            # TODO: Implement project-wide extraction
            console.print("[yellow]Project-wide extraction not yet implemented[/yellow]")
            
        else:
            console.print("[red]Error:[/red] Must specify --file, --files, or --project")
            raise click.Abort()
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Single file path')
@click.option('--files', '-F', type=click.Path(), help='Glob pattern for multiple files')
@click.option('--project', '-p', type=click.Path(), help='Validate entire project')
@click.option('--strict', is_flag=True, help='Fail on any validation errors')
@click.option('--report', is_flag=True, help='Generate detailed validation report')
def validate_context_comments(file, files, project, strict, report):
    """Validate AI-CONTEXT comment format and content."""
    try:
        if file:
            file_path = Path(file)
            validation = validate_ai_context_comments(file_path)
            
            if report:
                display_validation_report(file_path, validation)
            else:
                display_validation_summary(file_path, validation)
                
            if strict and not validation['valid']:
                raise click.Abort()
                
        elif files:
            # TODO: Implement glob pattern validation
            console.print("[yellow]Glob pattern validation not yet implemented[/yellow]")
            
        elif project:
            # TODO: Implement project-wide validation
            console.print("[yellow]Project-wide validation not yet implemented[/yellow]")
            
        else:
            console.print("[red]Error:[/red] Must specify --file, --files, or --project")
            raise click.Abort()
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

def display_comments(file_path: Path, comments: dict):
    """Display extracted comments in a table."""
    table = Table(title=f"AI-CONTEXT Comments in {file_path.name}")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    
    for key, value in comments.items():
        table.add_row(key, str(value))
    
    console.print(table)

def display_validation_summary(file_path: Path, validation: dict):
    """Display validation summary."""
    if validation['valid']:
        console.print(f"[green]✓[/green] {file_path.name}: Valid AI-CONTEXT comments")
    else:
        console.print(f"[red]✗[/red] {file_path.name}: Invalid AI-CONTEXT comments")
        
        if validation['missing_required']:
            console.print(f"  Missing required fields: {', '.join(validation['missing_required'])}")
        
        if validation['errors']:
            for error in validation['errors']:
                console.print(f"  Error: {error}")

def display_validation_report(file_path: Path, validation: dict):
    """Display detailed validation report."""
    panel = Panel(
        f"Validation Report for {file_path.name}\n\n"
        f"Status: {'Valid' if validation['valid'] else 'Invalid'}\n"
        f"Errors: {len(validation['errors'])}\n"
        f"Warnings: {len(validation['warnings'])}\n"
        f"Missing Required: {len(validation['missing_required'])}",
        title="AI-CONTEXT Validation Report",
        border_style="green" if validation['valid'] else "red"
    )
    
    console.print(panel)
    
    if validation['errors']:
        console.print("\n[red]Errors:[/red]")
        for error in validation['errors']:
            console.print(f"  • {error}")
    
    if validation['warnings']:
        console.print("\n[yellow]Warnings:[/yellow]")
        for warning in validation['warnings']:
            console.print(f"  • {warning}")
    
    if validation['missing_required']:
        console.print("\n[red]Missing Required Fields:[/red]")
        for field in validation['missing_required']:
            console.print(f"  • {field}")
    
    if validation['comments']:
        console.print("\n[blue]Current Comments:[/blue]")
        for key, value in validation['comments'].items():
            console.print(f"  • {key}: {value}")
