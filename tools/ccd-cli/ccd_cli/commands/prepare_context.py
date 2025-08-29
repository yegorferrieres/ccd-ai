#!/usr/bin/env python3
"""
CCD Prepare Context for AI

Command for preparing complete project context for AI developers
"""

import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.syntax import Syntax
from rich.table import Table
import yaml
from datetime import datetime
import subprocess
import sys

console = Console()

def check_prerequisites(project_root: Path) -> bool:
    """Check if required files exist."""
    missing_files = []
    
    # Check core files
    required_files = [
        'DEVELOPMENT_RULES.md',
        'docs/DEVELOPMENT_RULES.md',
        'docs/ENGINEERING_LOG.md',
        'docs/roadmap.md'
    ]
    
    for file_path in required_files:
        if not (project_root / file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        console.print(f"[red]Missing required files:[/red]")
        for file_path in missing_files:
            console.print(f"  - {file_path}")
        return False
    
    console.print("[green]All required files found[/green]")
    return True

def generate_header(project_root: Path) -> str:
    """Generate context header."""
    project_name = project_root.name
    repo_url = "Local repository"
    
    try:
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                              capture_output=True, text=True, cwd=project_root)
        if result.returncode == 0:
            repo_url = result.stdout.strip()
    except:
        pass
    
    return f"""================================================================================
                           CCD PROJECT - FULL CONTEXT FOR AI
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Project: {project_name}
Repository: {repo_url}
================================================================================

"""

def generate_development_rules(project_root: Path) -> str:
    """Generate development rules section."""
    rules_file = project_root / 'docs' / 'DEVELOPMENT_RULES.md'
    if not rules_file.exists():
        rules_file = project_root / 'DEVELOPMENT_RULES.md'
    
    if rules_file.exists():
        content = rules_file.read_text(encoding='utf-8')
        return f"""📋 DEVELOPMENT RULES (MANDATORY FOR AI!)
================================================================================
This section contains the algorithm for working with context files and development rules.
AI MUST follow these rules when performing tasks.

{content}

================================================================================

"""
    else:
        return ""

def generate_roadmap(project_root: Path) -> str:
    """Generate roadmap section."""
    roadmap_file = project_root / 'docs' / 'roadmap.md'
    
    if roadmap_file.exists():
        content = roadmap_file.read_text(encoding='utf-8')
        return f"""🗺️ ROADMAP STATUS
================================================================================
Current development status and planned stages.

{content}

================================================================================

"""
    else:
        return ""

def generate_engineering_log(project_root: Path) -> str:
    """Generate engineering log section."""
    log_file = project_root / 'docs' / 'ENGINEERING_LOG.md'
    
    if log_file.exists():
        content = log_file.read_text(encoding='utf-8')
        return f"""📝 ENGINEERING LOG
================================================================================
Development history, technical decisions, and lessons learned.

{content}

================================================================================

"""
    else:
        return ""

def generate_architecture_decisions(project_root: Path) -> str:
    """Generate architecture decisions section."""
    decisions_dir = project_root / 'docs' / 'decisions'
    
    if decisions_dir.exists() and decisions_dir.is_dir():
        adr_files = list(decisions_dir.glob("*.md"))
        
        if adr_files:
            content = "⚙️ ARCHITECTURE DECISIONS (ADRs)\n"
            content += "=" * 80 + "\n"
            content += "Accepted architectural decisions and their rationale.\n\n"
            
            for adr_file in adr_files:
                adr_content = adr_file.read_text(encoding='utf-8')
                content += f"--- {adr_file.stem} ---\n"
                content += adr_content + "\n\n"
            
            content += "=" * 80 + "\n\n"
            return content
    
    return ""

def generate_codemap(project_root: Path) -> str:
    """Generate current architecture section."""
    codemap_file = project_root / 'contexts' / 'codemap.yaml'
    
    if codemap_file.exists():
        try:
            content = codemap_file.read_text(encoding='utf-8')
            return f"""🔗 CURRENT ARCHITECTURE
================================================================================
Current module structure and their dependencies.

```yaml
{content}
```

================================================================================

"""
        except Exception as e:
            console.print(f"[yellow]Warning: Could not read codemap.yaml: {e}[/yellow]")
    
    return ""

def generate_function_catalog(project_root: Path) -> str:
    """Generate existing functions section."""
    catalog_file = project_root / 'contexts' / 'function-catalog.md'
    
    if catalog_file.exists():
        content = catalog_file.read_text(encoding='utf-8')
        return f"""🛠️ EXISTING FUNCTIONS
================================================================================
Catalog of all existing functions to prevent duplication.

{content}

================================================================================

"""
    else:
        return ""

def generate_ai_context_status(project_root: Path) -> str:
    """Generate AI-CONTEXT comments status."""
    content = """🤖 AI-CONTEXT COMMENTS STATUS
================================================================================
Status of AI-CONTEXT comments integration in source code.

"""
    
    # Check for source files with AI-CONTEXT comments
    source_dirs = ['src', 'app', 'lib', 'services', 'tools']
    total_files = 0
    files_with_context = 0
    
    for source_dir in source_dirs:
        source_path = project_root / source_dir
        if source_path.exists() and source_path.is_dir():
            for file_path in source_path.rglob("*"):
                if file_path.is_file() and file_path.suffix in ['.py', '.go', '.js', '.ts', '.java', '.cpp', '.c']:
                    total_files += 1
                    try:
                        file_content = file_path.read_text(encoding='utf-8')
                        if 'AI-CONTEXT:' in file_content:
                            files_with_context += 1
                    except:
                        pass
    
    if total_files > 0:
        coverage = (files_with_context / total_files) * 100
        content += f"• Total source files: {total_files}\n"
        content += f"• Files with AI-CONTEXT: {files_with_context}\n"
        content += f"• Coverage: {coverage:.1f}%\n"
    else:
        content += "• No source files found in common directories\n"
    
    content += "\n================================================================================\n\n"
    return content

def generate_quality_status(project_root: Path) -> str:
    """Generate quality status section."""
    content = """✅ QUALITY STATUS
================================================================================
Current context quality and validation status.

"""
    
    # Check for validation files
    validation_files = [
        'docs/schemas/',
        '.github/workflows/',
        'scripts/'
    ]
    
    for validation_path in validation_files:
        full_path = project_root / validation_path
        if full_path.exists():
            if full_path.is_dir():
                items = list(full_path.iterdir())
                content += f"• {validation_path}: {len(items)} items found\n"
            else:
                content += f"• {validation_path}: exists\n"
        else:
            content += f"• {validation_path}: not found\n"
    
    content += "\n================================================================================\n\n"
    return content

def generate_footer(output_file: Path) -> str:
    """Generate context footer."""
    return f"""================================================================================
                                CONTEXT PREPARATION COMPLETE
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Output file: {output_file.name}
Project: {output_file.parent.name}

NEXT STEPS:
1. Review the generated context above
2. Send this context to AI developer with your task
3. AI will follow the Development Rules workflow
4. Update context files after task completion
5. Run validation: ccd quality-gates --project .

Remember: Follow DEVELOPMENT_RULES.md workflow for all development tasks!
================================================================================
"""

def prepare_context(project_root: Path, output_file: Path, include_architecture: bool = True) -> bool:
    """Prepare complete context for AI developer."""
    try:
        console.print("[blue]Starting context generation...[/blue]")
        
        # Check prerequisites
        if not check_prerequisites(project_root):
            return False
        
        # Generate all sections
        context_parts = []
        
        context_parts.append(generate_header(project_root))
        context_parts.append(generate_development_rules(project_root))
        context_parts.append(generate_roadmap(project_root))
        context_parts.append(generate_engineering_log(project_root))
        
        if include_architecture:
            context_parts.append(generate_architecture_decisions(project_root))
            context_parts.append(generate_codemap(project_root))
        
        context_parts.append(generate_function_catalog(project_root))
        context_parts.append(generate_ai_context_status(project_root))
        context_parts.append(generate_quality_status(project_root))
        context_parts.append(generate_footer(output_file))
        
        # Combine all parts
        full_context = ''.join(context_parts)
        
        # Write to output file
        output_file.write_text(full_context, encoding='utf-8')
        
        console.print(f"[green]Context successfully generated to: {output_file}[/green]")
        console.print(f"File size: {output_file.stat().st_size / 1024:.1f} KB")
        console.print(f"Line count: {len(full_context.splitlines())}")
        
        return True
        
    except Exception as e:
        console.print(f"[red]Error generating context: {e}[/red]")
        return False

def prepare_context_impl(project_dir: str, output: str = None, no_architecture: bool = False, dry_run: bool = False):
    """Implementation of prepare context command."""
    project_path = Path(project_dir).resolve()
    
    # Generate output filename if not provided
    if not output:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = project_path / f"task-context-{timestamp}.txt"
    else:
        output_file = Path(output)
    
    console.print(f"[blue]Project directory:[/blue] {project_path}")
    console.print(f"[blue]Output file:[/blue] {output_file}")
    
    if dry_run:
        console.print("[yellow]DRY RUN MODE - Context would be generated to:[/yellow]")
        console.print(f"  {output_file}")
        console.print("[yellow]Run without --dry-run to actually generate the file[/yellow]")
        console.print("\n[blue]Context sections that would be generated:[/blue]")
        console.print("  - Development Rules")
        console.print("  - Roadmap Status")
        console.print("  - Engineering Log")
        if not no_architecture:
            console.print("  - Architecture Decisions (ADRs)")
            console.print("  - Current Architecture (codemap.yaml)")
        console.print("  - Existing Functions")
        console.print("  - AI-CONTEXT Comments Status")
        console.print("  - Quality Status")
        return
    
    # Prepare context
    success = prepare_context(project_path, output_file, not no_architecture)
    
    if success:
        console.print("\n[blue]You can now:[/blue]")
        console.print(f"  - Review: cat {output_file}")
        console.print(f"  - Send to AI: cat {output_file} | pbcopy  # (macOS)")
        console.print(f"  - Edit if needed: vim {output_file}")
    else:
        raise click.Abort()

@click.command()
@click.option('--project-dir', '-p', default='.',
              help='Project directory to analyze')
@click.option('--output', '-o', help='Output file for context')
@click.option('--no-architecture', is_flag=True, help='Skip architecture decisions and codemap')
@click.option('--dry-run', is_flag=True, help='Show what would be generated without creating file')
def prepare_context_cmd(project_dir, output, no_architecture, dry_run):
    """Prepare complete project context for AI developer."""
    try:
        prepare_context_impl(project_dir, output, no_architecture, dry_run)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()

if __name__ == '__main__':
    prepare_context_cmd()
