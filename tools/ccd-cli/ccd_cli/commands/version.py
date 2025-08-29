"""
Version Command

Show CCD CLI version information.
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from .. import __version__, __author__, __email__

console = Console()


def version_command():
    """Show CCD CLI version information."""
    
    # Create version table
    table = Table(show_header=False, box=None)
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")
    
    table.add_row("Version", __version__)
    table.add_row("Author", __author__)
    table.add_row("Email", __email__)
    table.add_row("Python Package", "ccd-cli")
    table.add_row("Repository", "https://github.com/yegorferrieres/ccd-ai")
    table.add_row("Documentation", "https://github.com/yegorferrieres/ccd-ai")
    
    # Show version panel
    console.print(Panel(
        table,
        title="CCD CLI Version Information",
        border_style="blue",
        padding=(1, 2)
    ))
    
    # Show additional info
    console.print("\n[bold]CCD (Continuous Context Documentation)[/bold]")
    console.print("A methodology for maintaining continuous context documentation in software projects.")
    
    console.print("\n[bold]Quick Start:[/bold]")
    console.print("  ccd init --project-name 'My Project' --domain 'web-application'")
    console.print("  ccd generate-cards --files 'src/**/*.py' --output docs/context-cards/")
    console.print("  ccd validate-contexts --contexts docs/ --schemas docs/schemas/")
    
    console.print("\n[bold]For more information:[/bold]")
    console.print("  • Documentation: [link=https://github.com/yegorferrieres/ccd-ai]https://github.com/yegorferrieres/ccd-ai[/link]")
    console.print("  • GitHub: [link=https://github.com/yegorferrieres/ccd-ai]https://github.com/yegorferrieres/ccd-ai[/link]")
    console.print("  • Issues: [link=https://github.com/yegorferrieres/ccd-ai/issues]https://github.com/yegorferrieres/ccd-ai/issues[/link]")
