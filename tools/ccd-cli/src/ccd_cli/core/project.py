"""
CCD Project Class

Represents a complete CCD (Continuous Context Documentation) project.
"""

from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import yaml

from .codemap import CODEMAP
from .module_index import ModuleIndex
from .context_card import ContextCard


@dataclass
class ProjectMetadata:
    """Project metadata information."""
    name: str
    description: str
    domain: str
    version: str = "1.0.0"
    created: datetime = field(default_factory=datetime.now)
    updated: datetime = field(default_factory=datetime.now)
    maintainers: List[Dict[str, str]] = field(default_factory=list)
    repository_url: Optional[str] = None
    website_url: Optional[str] = None
    license: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class ProjectStats:
    """Project statistics."""
    total_modules: int = 0
    total_files: int = 0
    total_context_cards: int = 0
    coverage_percentage: float = 0.0
    freshness_percentage: float = 0.0
    last_updated: Optional[datetime] = None


class CCDProject:
    """
    Represents a complete CCD project.
    
    This class manages the entire CCD project structure including:
    - Project metadata
    - CODEMAP (repository-level context)
    - Module indexes
    - Context cards
    - Project statistics and health
    """
    
    def __init__(self, project_path: Path):
        """
        Initialize a new CCD project.
        
        Args:
            project_path: Path to the project root directory
        """
        self.project_path = Path(project_path)
        self.metadata: Optional[ProjectMetadata] = None
        self.codemap: Optional[CODEMAP] = None
        self.module_indexes: Dict[str, ModuleIndex] = {}
        self.context_cards: Dict[str, ContextCard] = {}
        self.stats = ProjectStats()
        
        # Ensure project directory exists
        self.project_path.mkdir(parents=True, exist_ok=True)
        
        # Create standard CCD directory structure
        self._create_directory_structure()
    
    def _create_directory_structure(self):
        """Create standard CCD directory structure."""
        directories = [
            "docs",
            "docs/schemas",
            "docs/playbooks", 
            "docs/checklists",
            "docs/templates",
            "docs/examples",
            "docs/context-cards",
            "docs/modules",
            "decisions",
            "phases",
            ".github/workflows",
        ]
        
        for directory in directories:
            (self.project_path / directory).mkdir(parents=True, exist_ok=True)
    
    def initialize(self, name: str, description: str, domain: str, **kwargs) -> None:
        """
        Initialize the project with basic information.
        
        Args:
            name: Project name
            description: Project description
            domain: Project domain
            **kwargs: Additional metadata
        """
        self.metadata = ProjectMetadata(
            name=name,
            description=description,
            domain=domain,
            **kwargs
        )
        
        # Create initial CODEMAP
        self.codemap = CODEMAP(
            project_name=name,
            description=description,
            domain=domain
        )
        
        # Create initial documentation files
        self._create_initial_docs()
        
        # Update project stats
        self._update_stats()
    
    def _create_initial_docs(self):
        """Create initial documentation files."""
        # Create README.md
        readme_content = f"""# {self.metadata.name}

{self.metadata.description}

## CCD (Continuous Context Documentation)

This project uses CCD methodology for maintaining continuous context documentation.

## Quick Start

```bash
# Install CCD CLI
git clone https://github.com/yegorferrieres/ccd-ai.git && cd ccd-ai/tools/ccd-cli && pip install -e .

# Initialize project (already done)
ccd init --project-name "{self.metadata.name}" --domain "{self.metadata.domain}"

# Generate context cards
ccd generate-cards --files "src/**/*.{{py,js,go}}" --output docs/context-cards/

# Validate context
ccd validate-contexts --contexts docs/ --schemas docs/schemas/
```

## Project Structure

- `docs/` - CCD documentation
- `docs/schemas/` - JSON schemas for validation
- `docs/playbooks/` - Operational playbooks
- `docs/checklists/` - Quick checklists
- `docs/templates/` - Documentation templates
- `docs/examples/` - Implementation examples
- `decisions/` - Architecture Decision Records (ADRs)
- `phases/` - Project development phases

## More Information

- [CCD Documentation](https://github.com/yegorferrieres/ccd-ai)
- [CCD CLI](https://github.com/yegorferrieres/ccd-ai)
- [CCD Methodology](https://github.com/yegorferrieres/ccd-ai)
"""
        
        with open(self.project_path / "README.md", "w") as f:
            f.write(readme_content)
        
        # Create CCD manifest
        manifest_content = f"""# CCD Manifest

## Project Information

- **Name**: {self.metadata.name}
- **Description**: {self.metadata.description}
- **Domain**: {self.metadata.domain}
- **Version**: {self.metadata.version}
- **Created**: {self.metadata.created.strftime('%Y-%m-%d %H:%M:%S')}
- **Updated**: {self.metadata.updated.strftime('%Y-%m-%d %H:%M:%S')}

## CCD Implementation

This project implements CCD (Continuous Context Documentation) methodology to maintain:

1. **Repository-level context** via CODEMAP.yaml
2. **Module-level context** via INDEX.yaml files
3. **File-level context** via .ctx.md files
4. **Automated validation** via JSON schemas
5. **CI/CD integration** for continuous updates
6. **Quality gates** for context health

## Success Metrics

- Context Coverage: Target 90%+
- Context Freshness: Target 95%+
- Retrieval Precision: Target 85%+
- Time-to-Context: Target <5 minutes
- Drift MTTR: Target <2 hours

## Maintenance

- Context files are automatically generated and updated
- Regular validation ensures quality and consistency
- Health monitoring provides real-time status
- Automated packaging for distribution and backup
"""
        
        with open(self.project_path / "docs/00-manifest.md", "w") as f:
            f.write(manifest_content)
    
    def add_module(self, module_path: str, module_type: str, description: str, **kwargs) -> ModuleIndex:
        """
        Add a new module to the project.
        
        Args:
            module_path: Path to the module
            module_type: Type of module
            description: Module description
            **kwargs: Additional module properties
            
        Returns:
            Created ModuleIndex instance
        """
        module_index = ModuleIndex(
            module_path=module_path,
            module_type=module_type,
            description=description,
            **kwargs
        )
        
        self.module_indexes[module_path] = module_index
        
        # Update CODEMAP
        if self.codemap:
            self.codemap.add_module(module_index)
        
        # Update stats
        self._update_stats()
        
        return module_index
    
    def add_context_card(self, file_path: str, **kwargs) -> ContextCard:
        """
        Add a new context card to the project.
        
        Args:
            file_path: Path to the file
            **kwargs: Context card properties
            
        Returns:
            Created ContextCard instance
        """
        context_card = ContextCard(file_path=file_path, **kwargs)
        self.context_cards[file_path] = context_card
        
        # Update stats
        self._update_stats()
        
        return context_card
    
    def _update_stats(self):
        """Update project statistics."""
        self.stats.total_modules = len(self.module_indexes)
        self.stats.total_files = len(self.context_cards)
        self.stats.total_context_cards = len(self.context_cards)
        
        # Calculate coverage percentage
        if self.codemap and self.codemap.modules:
            total_files_in_codemap = sum(len(module.get('files', [])) for module in self.codemap.modules)
            if total_files_in_codemap > 0:
                self.stats.coverage_percentage = (len(self.context_cards) / total_files_in_codemap) * 100
        
        # Update last updated timestamp
        self.stats.last_updated = datetime.now()
    
    def save(self) -> None:
        """Save the project to disk."""
        # Save CODEMAP
        if self.codemap:
            codemap_path = self.project_path / "docs" / "CODEMAP.yaml"
            codemap_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(codemap_path, "w") as f:
                yaml.dump(self.codemap.to_dict(), f, default_flow_style=False, sort_keys=False)
        
        # Save module indexes
        for module_path, module_index in self.module_indexes.items():
            module_dir = self.project_path / "docs" / "modules" / module_path
            module_dir.mkdir(parents=True, exist_ok=True)
            
            index_path = module_dir / "INDEX.yaml"
            with open(index_path, "w") as f:
                yaml.dump(module_index.to_dict(), f, default_flow_style=False, sort_keys=False)
        
        # Save context cards
        for file_path, context_card in self.context_cards.items():
            # Determine output path
            if file_path.startswith("src/"):
                output_path = self.project_path / "docs" / "context-cards" / file_path.replace("src/", "")
            else:
                output_path = self.project_path / "docs" / "context-cards" / file_path
            
            # Ensure directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Save as .ctx.md
            ctx_path = output_path.with_suffix('.ctx.md')
            with open(ctx_path, "w") as f:
                f.write(context_card.to_markdown())
    
    def load(self) -> None:
        """Load the project from disk."""
        # Load CODEMAP
        codemap_path = self.project_path / "docs" / "CODEMAP.yaml"
        if codemap_path.exists():
            with open(codemap_path, "r") as f:
                codemap_data = yaml.safe_load(f)
                self.codemap = CODEMAP.from_dict(codemap_data)
        
        # Load module indexes
        modules_dir = self.project_path / "docs" / "modules"
        if modules_dir.exists():
            for module_dir in modules_dir.iterdir():
                if module_dir.is_dir():
                    index_path = module_dir / "INDEX.yaml"
                    if index_path.exists():
                        with open(index_path, "r") as f:
                            index_data = yaml.safe_load(f)
                            module_index = ModuleIndex.from_dict(index_data)
                            self.module_indexes[module_dir.name] = module_index
        
        # Load context cards
        context_cards_dir = self.project_path / "docs" / "context-cards"
        if context_cards_dir.exists():
            for ctx_file in context_cards_dir.rglob("*.ctx.md"):
                # Convert path back to original file path
                relative_path = ctx_file.relative_to(context_cards_dir)
                original_path = str(relative_path).replace('.ctx.md', '')
                
                context_card = ContextCard.from_markdown(ctx_file, original_path)
                self.context_cards[original_path] = context_card
        
        # Update stats
        self._update_stats()
    
    def get_health_report(self) -> Dict[str, Any]:
        """
        Get project health report.
        
        Returns:
            Dictionary containing health metrics
        """
        return {
            "project_name": self.metadata.name if self.metadata else "Unknown",
            "coverage_percentage": self.stats.coverage_percentage,
            "freshness_percentage": self.stats.freshness_percentage,
            "total_modules": self.stats.total_modules,
            "total_files": self.stats.total_files,
            "total_context_cards": self.stats.total_context_cards,
            "last_updated": self.stats.last_updated.isoformat() if self.stats.last_updated else None,
            "health_score": self._calculate_health_score(),
            "recommendations": self._get_recommendations()
        }
    
    def _calculate_health_score(self) -> float:
        """Calculate overall health score (0-100)."""
        score = 0.0
        
        # Coverage score (40%)
        score += min(self.stats.coverage_percentage, 100) * 0.4
        
        # Freshness score (30%)
        score += min(self.stats.freshness_percentage, 100) * 0.3
        
        # Module coverage score (20%)
        if self.codemap and self.codemap.modules:
            module_coverage = (len(self.module_indexes) / len(self.codemap.modules)) * 100
            score += min(module_coverage, 100) * 0.2
        
        # File organization score (10%)
        if self.stats.total_context_cards > 0:
            score += 10.0
        
        return round(score, 1)
    
    def _get_recommendations(self) -> List[str]:
        """Get recommendations for improving project health."""
        recommendations = []
        
        if self.stats.coverage_percentage < 80:
            recommendations.append("Increase context coverage by generating more context cards")
        
        if self.stats.freshness_percentage < 90:
            recommendations.append("Update stale context documentation")
        
        if self.stats.total_modules == 0:
            recommendations.append("Add module indexes for better organization")
        
        if not self.codemap:
            recommendations.append("Create CODEMAP.yaml for repository-level context")
        
        return recommendations
