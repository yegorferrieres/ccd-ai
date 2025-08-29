"""
Init Command

Initialize a new CCD project.
"""

from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich.table import Table

from ..core import CCDProject
from ..utils.errors import CCDError

console = Console()


def init_command(ctx, project_name: str, domain: str, yes: bool, output_dir: str):
    """
    Initialize a new CCD project.
    
    Args:
        ctx: Click context
        project_name: Name of the project
        domain: Project domain
        yes: Skip prompts and use defaults
        output_dir: Output directory
    """
    try:
        # Validate inputs
        if not project_name or not domain:
            raise CCDError("Project name and domain are required")
        
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Show project information
        console.print(Panel(
            f"[bold blue]Initializing CCD Project[/bold blue]\n\n"
            f"[bold]Project Name:[/bold] {project_name}\n"
            f"[bold]Domain:[/bold] {domain}\n"
            f"[bold]Output Directory:[/bold] {output_path.absolute()}",
            title="Project Details",
            border_style="blue"
        ))
        
        # Get additional information if not skipping prompts
        if not yes:
            project_description = Prompt.ask(
                "Project description",
                default=f"A {domain.replace('-', ' ')} project using CCD methodology"
            )
            
            technology_stack = Prompt.ask(
                "Technology stack (comma-separated)",
                default="python,fastapi,sqlalchemy"
            ).split(",")
            
            repository_url = Prompt.ask(
                "Repository URL (optional)",
                default=""
            )
            
            website_url = Prompt.ask(
                "Website URL (optional)",
                default=""
            )
            
            license_type = Prompt.ask(
                "License",
                choices=["MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause", "Other"],
                default="MIT"
            )
            
            maintainer_name = Prompt.ask(
                "Maintainer name",
                default="Your Name"
            )
            
            maintainer_email = Prompt.ask(
                "Maintainer email",
                default="your.email@example.com"
            )
        else:
            # Use defaults
            project_description = f"A {domain.replace('-', ' ')} project using CCD methodology"
            technology_stack = ["python", "fastapi", "sqlalchemy"]
            repository_url = ""
            website_url = ""
            license_type = "MIT"
            maintainer_name = "Your Name"
            maintainer_email = "your.email@example.com"
        
        # Show what will be created
        console.print("\n[bold]What will be created:[/bold]")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Component", style="cyan")
        table.add_column("Description", style="white")
        table.add_column("Path", style="green")
        
        table.add_row("Project Root", "Main project directory", str(output_path))
        table.add_row("README.md", "Project overview and CCD guide", str(output_path / "README.md"))
        table.add_row("CCD Manifest", "CCD implementation details", str(output_path / "docs/00-manifest.md"))
        table.add_row("Directory Structure", "CCD standard directories", "docs/, decisions/, phases/, etc.")
        table.add_row("CODEMAP.yaml", "Repository-level context", str(output_path / "docs/CODEMAP.yaml"))
        table.add_row("GitHub Actions", "CI/CD workflows", str(output_path / ".github/workflows/"))
        
        console.print(table)
        
        # Confirm creation
        if not yes:
            if not Confirm.ask("Continue with project creation?"):
                console.print("[yellow]Project creation cancelled[/yellow]")
                return
        
        # Create project with progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            
            # Create CCD project
            task = progress.add_task("Creating CCD project structure...", total=None)
            project = CCDProject(output_path)
            
            # Initialize project
            progress.update(task, description="Initializing project...")
            project.initialize(
                name=project_name,
                description=project_description,
                domain=domain,
                technology_stack=technology_stack,
                repository_url=repository_url if repository_url else None,
                website_url=website_url if website_url else None,
                license=license_type,
                maintainers=[{
                    'name': maintainer_name,
                    'email': maintainer_email,
                    'role': 'Lead'
                }]
            )
            
            # Save project
            progress.update(task, description="Saving project files...")
            project.save()
            
            # Create additional files
            progress.update(task, description="Creating additional files...")
            _create_additional_files(output_path, project_name, domain)
            
            progress.update(task, description="Finalizing...")
        
        # Show success message
        console.print("\n" + Panel(
            f"[bold green]✓ CCD Project Created Successfully![/bold green]\n\n"
            f"Your new CCD project is ready at:\n"
            f"[bold]{output_path.absolute()}[/bold]\n\n"
            f"Next steps:\n"
            f"1. [bold]cd[/bold] into the project directory\n"
            f"2. [bold]git init[/bold] to start version control\n"
            f"3. [bold]ccd generate-cards[/bold] to create context cards\n"
            f"4. [bold]ccd validate-contexts[/bold] to check quality",
            title="Success!",
            border_style="green"
        ))
        
        # Show project structure
        console.print("\n[bold]Project Structure:[/bold]")
        _show_project_structure(output_path)
        
    except Exception as e:
        raise CCDError(f"Failed to initialize project: {str(e)}")


def _create_additional_files(output_path: Path, project_name: str, domain: str):
    """Create additional project files."""
    
    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# CCD specific
ccd-contexts.zip
health-report.json
coverage-report.yaml
freshness-report.json
"""
    
    with open(output_path / ".gitignore", "w") as f:
        f.write(gitignore_content)
    
    # Create CCD configuration
    config_content = f"""# CCD Configuration
project:
  name: "{project_name}"
  domain: "{domain}"
  schemas_path: "./docs/schemas"
  contexts_path: "./docs"

generation:
  auto_update: true
  include_tests: false
  include_docs: true

validation:
  strict_mode: true
  fail_fast: false

output:
  default_format: "text"
  colors: true
  progress_bars: true
"""
    
    with open(output_path / "ccd.config.yaml", "w") as f:
        f.write(config_content)
    
    # Create Makefile
    makefile_content = f"""# CCD Project Makefile

.PHONY: help init generate validate health coverage pack clean

help: ## Show this help message
	@echo "CCD Project Management Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {{FS = ":.*?## "}}; {{printf "  \\033[36m%-15s\\033[0m %s\\n", $$1, $$2}}'

init: ## Initialize CCD project (already done)
	@echo "Project already initialized at {output_path}"

generate: ## Generate context cards and documentation
	ccd generate-cards --files "src/**/*.py" --output docs/context-cards/
	ccd generate-index --modules "src/*" --output docs/modules/
	ccd update-codemap --output docs/CODEMAP.yaml

validate: ## Validate CCD contexts and schemas
	ccd validate-contexts --contexts docs/ --schemas docs/schemas/

health: ## Check project health
	ccd health --detailed

coverage: ## Show coverage statistics
	ccd coverage --modules --files --min-coverage 80

pack: ## Package contexts for distribution
	ccd pack --output ./ccd-contexts.zip --include-schemas

clean: ## Clean generated files
	rm -rf docs/context-cards/
	rm -rf docs/modules/
	rm -f docs/CODEMAP.yaml
	rm -f ccd-contexts.zip

setup: ## Setup development environment
	pip install -e .
	pip install -r requirements.txt

test: ## Run tests
	pytest

lint: ## Run linting
	black .
	isort .
	flake8 .
	mypy .

format: ## Format code
	black .
	isort .
"""
    
    with open(output_path / "Makefile", "w") as f:
        f.write(makefile_content)
    
    # Create requirements.txt
    requirements_content = """# Core dependencies
fastapi>=0.100.0
uvicorn>=0.20.0
sqlalchemy>=2.0.0
pydantic>=2.0.0

# Development dependencies
pytest>=7.0.0
pytest-asyncio>=0.21.0
black>=23.0.0
isort>=5.12.0
flake8>=6.0.0
mypy>=1.0.0

# CCD CLI
ccd-cli>=1.0.0
"""
    
    with open(output_path / "requirements.txt", "w") as f:
        f.write(requirements_content)
    
    # Create sample source structure
    src_path = output_path / "src"
    src_path.mkdir(exist_ok=True)
    
    # Create __init__.py
    with open(src_path / "__init__.py", "w") as f:
        f.write('"""CCD Project Source Code."""\n')
    
    # Create main.py
    main_content = f"""\"\"\"
{project_name} - Main Application Entry Point

This is the main entry point for the {project_name} application.
\"\"\"

import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="{project_name}",
    description="A {domain.replace('-', ' ')} project using CCD methodology",
    version="1.0.0"
)

@app.get("/")
async def root():
    \"\"\"Root endpoint.\"\"\"
    return {{"message": "Welcome to {project_name}!"}}

@app.get("/health")
async def health():
    \"\"\"Health check endpoint.\"\"\"
    return {{"status": "healthy", "service": "{project_name}"}}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
    
    with open(src_path / "main.py", "w") as f:
        f.write(main_content)


def _show_project_structure(output_path: Path, prefix: str = ""):
    """Show the created project structure."""
    
    def _show_dir(path: Path, prefix: str, is_last: bool):
        console.print(f"{prefix}{'└── ' if is_last else '├── '}[blue]{path.name}/[/blue]")
        
        items = sorted([item for item in path.iterdir() if item.is_dir() or item.suffix in ['.py', '.yaml', '.md', '.txt']])
        
        for i, item in enumerate(items):
            is_last_item = i == len(items) - 1
            new_prefix = prefix + ('    ' if is_last else '│   ')
            
            if item.is_dir():
                _show_dir(item, new_prefix, is_last_item)
            else:
                color = {
                    '.py': 'green',
                    '.yaml': 'yellow', 
                    '.yml': 'yellow',
                    '.md': 'cyan',
                    '.txt': 'white'
                }.get(item.suffix, 'white')
                
                console.print(f"{new_prefix}{'└── ' if is_last_item else '├── '}[{color}]{item.name}[/{color}]")
    
    _show_dir(output_path, "", True)
