"""
CODEMAP Class

Represents repository-level context documentation in CCD.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import yaml


@dataclass
class ModuleInfo:
    """Module information for CODEMAP."""
    name: str
    path: str
    type: str
    description: str
    language: str
    size: Optional[str] = None
    lines: Optional[int] = None
    files: Optional[int] = None
    complexity: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class DependencyInfo:
    """Dependency information for CODEMAP."""
    module: str
    type: str
    description: str
    version: Optional[str] = None
    optional: bool = False


class CODEMAP:
    """
    Repository-level context documentation.
    
    This class represents the top-level context for a software repository,
    including project information, modules, dependencies, and metadata.
    """
    
    def __init__(self, project_name: str, description: str, domain: str, **kwargs):
        """
        Initialize a new CODEMAP.
        
        Args:
            project_name: Name of the project
            description: Project description
            domain: Project domain
            **kwargs: Additional project properties
        """
        self.version = kwargs.get('version', '1.0.0')
        self.project = {
            'name': project_name,
            'description': description,
            'domain': domain,
            'technology_stack': kwargs.get('technology_stack', []),
            'repository_url': kwargs.get('repository_url'),
            'website_url': kwargs.get('website_url'),
            'license': kwargs.get('license'),
            'maintainers': kwargs.get('maintainers', [])
        }
        self.modules: List[Dict[str, Any]] = []
        self.dependencies: List[Dict[str, Any]] = []
        self.metadata = {
            'created': datetime.now().isoformat(),
            'updated': datetime.now().isoformat(),
            'generator': {
                'tool': 'ccd-cli',
                'version': '1.0.0',
                'timestamp': datetime.now().isoformat()
            }
        }
    
    def add_module(self, module: ModuleInfo) -> None:
        """
        Add a module to the CODEMAP.
        
        Args:
            module: Module information
        """
        module_dict = {
            'name': module.name,
            'path': module.path,
            'type': module.type,
            'description': module.description,
            'language': module.language,
            'size': module.size,
            'lines': module.lines,
            'files': module.files,
            'complexity': module.complexity,
            'status': module.status,
            'priority': module.priority,
            'tags': module.tags
        }
        
        # Remove None values
        module_dict = {k: v for k, v in module_dict.items() if v is not None}
        
        self.modules.append(module_dict)
        self._update_metadata()
    
    def add_dependency(self, dependency: DependencyInfo) -> None:
        """
        Add a dependency to the CODEMAP.
        
        Args:
            dependency: Dependency information
        """
        dependency_dict = {
            'module': dependency.module,
            'type': dependency.type,
            'description': dependency.description,
            'version': dependency.version,
            'optional': dependency.optional
        }
        
        # Remove None values
        dependency_dict = {k: v for k, v in dependency_dict.items() if v is not None}
        
        self.dependencies.append(dependency_dict)
        self._update_metadata()
    
    def _update_metadata(self) -> None:
        """Update metadata timestamps."""
        self.metadata['updated'] = datetime.now().isoformat()
        self.metadata['generator']['timestamp'] = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert CODEMAP to dictionary.
        
        Returns:
            Dictionary representation of CODEMAP
        """
        return {
            'version': self.version,
            'project': self.project,
            'modules': self.modules,
            'dependencies': self.dependencies,
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CODEMAP':
        """
        Create CODEMAP from dictionary.
        
        Args:
            data: Dictionary data
            
        Returns:
            CODEMAP instance
        """
        codemap = cls(
            project_name=data['project']['name'],
            description=data['project']['description'],
            domain=data['project']['domain']
        )
        
        codemap.version = data.get('version', '1.0.0')
        codemap.project.update(data['project'])
        codemap.modules = data.get('modules', [])
        codemap.dependencies = data.get('dependencies', [])
        codemap.metadata = data.get('metadata', {})
        
        return codemap
    
    def validate(self) -> List[str]:
        """
        Validate CODEMAP structure.
        
        Returns:
            List of validation errors
        """
        errors = []
        
        # Check required fields
        if not self.project.get('name'):
            errors.append("Project name is required")
        
        if not self.project.get('description'):
            errors.append("Project description is required")
        
        if not self.project.get('domain'):
            errors.append("Project domain is required")
        
        # Check module structure
        for i, module in enumerate(self.modules):
            if not module.get('name'):
                errors.append(f"Module {i}: name is required")
            if not module.get('path'):
                errors.append(f"Module {i}: path is required")
            if not module.get('type'):
                errors.append(f"Module {i}: type is required")
            if not module.get('description'):
                errors.append(f"Module {i}: description is required")
            if not module.get('language'):
                errors.append(f"Module {i}: language is required")
        
        # Check dependency structure
        for i, dependency in enumerate(self.dependencies):
            if not dependency.get('module'):
                errors.append(f"Dependency {i}: module is required")
            if not dependency.get('type'):
                errors.append(f"Dependency {i}: type is required")
            if not dependency.get('description'):
                errors.append(f"Dependency {i}: description is required")
        
        return errors
    
    def get_module_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get module by name.
        
        Args:
            name: Module name
            
        Returns:
            Module dictionary or None
        """
        for module in self.modules:
            if module.get('name') == name:
                return module
        return None
    
    def get_module_by_path(self, path: str) -> Optional[Dict[str, Any]]:
        """
        Get module by path.
        
        Args:
            path: Module path
            
        Returns:
            Module dictionary or None
        """
        for module in self.modules:
            if module.get('path') == path:
                return module
        return None
    
    def get_dependencies_by_type(self, dep_type: str) -> List[Dict[str, Any]]:
        """
        Get dependencies by type.
        
        Args:
            dep_type: Dependency type
            
        Returns:
            List of dependencies
        """
        return [dep for dep in self.dependencies if dep.get('type') == dep_type]
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get CODEMAP statistics.
        
        Returns:
            Dictionary with statistics
        """
        total_files = sum(module.get('files', 0) for module in self.modules)
        total_lines = sum(module.get('lines', 0) for module in self.modules)
        
        languages = {}
        for module in self.modules:
            lang = module.get('language', 'unknown')
            languages[lang] = languages.get(lang, 0) + 1
        
        module_types = {}
        for module in self.modules:
            mtype = module.get('type', 'unknown')
            module_types[mtype] = module_types.get(mtype, 0) + 1
        
        return {
            'total_modules': len(self.modules),
            'total_files': total_files,
            'total_lines': total_lines,
            'total_dependencies': len(self.dependencies),
            'languages': languages,
            'module_types': module_types,
            'created': self.metadata.get('created'),
            'updated': self.metadata.get('updated')
        }
