"""
Context Card Class

Represents file-level context documentation in CCD.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import re


@dataclass
class ImportInfo:
    """Import information for context card."""
    name: str
    purpose: str
    version: Optional[str] = None


@dataclass
class FileDependency:
    """File dependency information for context card."""
    path: str
    relationship: str
    description: Optional[str] = None


@dataclass
class ServiceDependency:
    """Service dependency information for context card."""
    name: str
    type: str
    endpoint: Optional[str] = None
    description: Optional[str] = None


@dataclass
class ComponentInfo:
    """Component information for context card."""
    name: str
    purpose: str
    signature: Optional[str] = None
    methods: Optional[List[Dict[str, str]]] = None
    properties: Optional[List[Dict[str, str]]] = None
    returns: Optional[str] = None


class ContextCard:
    """
    File-level context documentation.
    
    This class represents the context for a specific file within a project,
    including its purpose, dependencies, components, and usage information.
    """
    
    def __init__(self, file_path: str, **kwargs):
        """
        Initialize a new context card.
        
        Args:
            file_path: Path to the file
            **kwargs: Context card properties
        """
        self.metadata = {
            'file_path': file_path,
            'language': kwargs.get('language', self._detect_language(file_path)),
            'domain': kwargs.get('domain', self._detect_domain(file_path)),
            'size': kwargs.get('size'),
            'lines': kwargs.get('lines'),
            'last_modified': kwargs.get('last_modified', datetime.now().isoformat()),
            'author': kwargs.get('author'),
            'version': kwargs.get('version'),
            'complexity': kwargs.get('complexity'),
            'priority': kwargs.get('priority'),
            'tags': kwargs.get('tags', [])
        }
        
        self.overview = kwargs.get('overview', '')
        self.purpose = kwargs.get('purpose', '')
        
        self.dependencies = {
            'imports': kwargs.get('imports', []),
            'files': kwargs.get('files', []),
            'services': kwargs.get('services', [])
        }
        
        self.key_components = {
            'classes': kwargs.get('classes', []),
            'functions': kwargs.get('functions', []),
            'constants': kwargs.get('constants', []),
            'interfaces': kwargs.get('interfaces', [])
        }
        
        self.usage = kwargs.get('usage', {})
        self.testing = kwargs.get('testing', {})
        self.performance = kwargs.get('performance', {})
        self.security = kwargs.get('security', {})
        self.maintenance = kwargs.get('maintenance', {})
        self.related = kwargs.get('related', {})
        self.changelog = kwargs.get('changelog', [])
        self.notes = kwargs.get('notes', '')
    
    def _detect_language(self, file_path: str) -> str:
        """Detect programming language from file extension."""
        ext = Path(file_path).suffix.lower()
        language_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.go': 'go',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.rs': 'rust',
            '.php': 'php',
            '.rb': 'ruby',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.scala': 'scala',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
            '.xml': 'xml',
            '.html': 'html',
            '.css': 'css',
            '.sql': 'sql',
            '.sh': 'bash',
            '.ps1': 'powershell',
            '.md': 'markdown',
            '.adoc': 'asciidoc'
        }
        return language_map.get(ext, 'other')
    
    def _detect_domain(self, file_path: str) -> str:
        """Detect domain from file path."""
        path_lower = file_path.lower()
        
        if any(x in path_lower for x in ['api/', 'endpoint', 'controller', 'route']):
            return 'api'
        elif any(x in path_lower for x in ['service', 'business', 'logic', 'core']):
            return 'business-logic'
        elif any(x in path_lower for x in ['model', 'entity', 'dao', 'repository']):
            return 'data-access'
        elif any(x in path_lower for x in ['config', 'settings', 'env']):
            return 'configuration'
        elif any(x in path_lower for x in ['deploy', 'docker', 'k8s', 'helm']):
            return 'deployment'
        elif any(x in path_lower for x in ['test', 'spec', 'specs']):
            return 'testing'
        elif any(x in path_lower for x in ['ui/', 'component', 'view', 'page']):
            return 'ui'
        elif any(x in path_lower for x in ['util', 'helper', 'common']):
            return 'utility'
        else:
            return 'other'
    
    def add_import(self, name: str, purpose: str, version: Optional[str] = None) -> None:
        """
        Add an import dependency.
        
        Args:
            name: Import name or path
            purpose: Why this import is needed
            version: Required version if specified
        """
        import_info = ImportInfo(name=name, purpose=purpose, version=version)
        self.dependencies['imports'].append(import_info)
    
    def add_file_dependency(self, path: str, relationship: str, description: Optional[str] = None) -> None:
        """
        Add a file dependency.
        
        Args:
            path: Path to the dependent file
            relationship: Type of dependency relationship
            description: Description of the dependency
        """
        file_dep = FileDependency(path=path, relationship=relationship, description=description)
        self.dependencies['files'].append(file_dep)
    
    def add_service_dependency(self, name: str, service_type: str, endpoint: Optional[str] = None, description: Optional[str] = None) -> None:
        """
        Add a service dependency.
        
        Args:
            name: Service name
            service_type: Service type
            endpoint: Service endpoint or connection string
            description: What the service provides
        """
        service_dep = ServiceDependency(name=name, type=service_type, endpoint=endpoint, description=description)
        self.dependencies['services'].append(service_dep)
    
    def add_class(self, name: str, purpose: str, methods: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Add a class component.
        
        Args:
            name: Class name
            purpose: What the class does
            methods: Key methods in the class
        """
        class_info = ComponentInfo(name=name, purpose=purpose, methods=methods)
        self.key_components['classes'].append(class_info)
    
    def add_function(self, name: str, purpose: str, signature: Optional[str] = None, returns: Optional[str] = None) -> None:
        """
        Add a function component.
        
        Args:
            name: Function name
            purpose: What the function does
            signature: Function signature or parameters
            returns: What the function returns
        """
        func_info = ComponentInfo(name=name, purpose=purpose, signature=signature, returns=returns)
        self.key_components['functions'].append(func_info)
    
    def add_constant(self, name: str, value: str, purpose: str) -> None:
        """
        Add a constant component.
        
        Args:
            name: Constant name
            value: Constant value
            purpose: Why this constant exists
        """
        const_info = ComponentInfo(name=name, purpose=purpose)
        self.key_components['constants'].append(const_info)
    
    def add_interface(self, name: str, purpose: str, properties: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Add an interface component.
        
        Args:
            name: Interface name
            purpose: What the interface defines
            properties: Interface properties
        """
        interface_info = ComponentInfo(name=name, purpose=purpose, properties=properties)
        self.key_components['interfaces'].append(interface_info)
    
    def add_changelog_entry(self, date: str, change: str, author: str, **kwargs) -> None:
        """
        Add a changelog entry.
        
        Args:
            date: Date of the change
            change: Description of what changed
            author: Author of the change
            **kwargs: Additional changelog properties
        """
        entry = {
            'date': date,
            'change': change,
            'author': author,
            'version': kwargs.get('version'),
            'reason': kwargs.get('reason')
        }
        
        # Remove None values
        entry = {k: v for k, v in entry.items() if v is not None}
        
        self.changelog.append(entry)
    
    def to_markdown(self) -> str:
        """
        Convert context card to markdown format.
        
        Returns:
            Markdown string representation
        """
        md_lines = []
        
        # Header
        md_lines.append(f"# Context Card: {self.metadata['file_path']}")
        md_lines.append("")
        
        # Metadata
        md_lines.append("## Metadata")
        for key, value in self.metadata.items():
            if value is not None:
                if isinstance(value, list):
                    md_lines.append(f"- **{key.replace('_', ' ').title()}**: {', '.join(value)}")
                else:
                    md_lines.append(f"- **{key.replace('_', ' ').title()}**: {value}")
        md_lines.append("")
        
        # Overview
        if self.overview:
            md_lines.append("## Overview")
            md_lines.append(self.overview)
            md_lines.append("")
        
        # Purpose
        if self.purpose:
            md_lines.append("## Purpose")
            md_lines.append(self.purpose)
            md_lines.append("")
        
        # Dependencies
        if any(self.dependencies.values()):
            md_lines.append("## Dependencies")
            
            if self.dependencies['imports']:
                md_lines.append("### Imports")
                for imp in self.dependencies['imports']:
                    md_lines.append(f"- **{imp.name}**: {imp.purpose}")
                    if imp.version:
                        md_lines.append(f"  - Version: {imp.version}")
                md_lines.append("")
            
            if self.dependencies['files']:
                md_lines.append("### Files")
                for file_dep in self.dependencies['files']:
                    md_lines.append(f"- **{file_dep.path}**: {file_dep.relationship}")
                    if file_dep.description:
                        md_lines.append(f"  - {file_dep.description}")
                md_lines.append("")
            
            if self.dependencies['services']:
                md_lines.append("### Services")
                for service in self.dependencies['services']:
                    md_lines.append(f"- **{service.name}** ({service.type})")
                    if service.endpoint:
                        md_lines.append(f"  - Endpoint: {service.endpoint}")
                    if service.description:
                        md_lines.append(f"  - {service.description}")
                md_lines.append("")
        
        # Key Components
        if any(self.key_components.values()):
            md_lines.append("## Key Components")
            
            if self.key_components['classes']:
                md_lines.append("### Classes")
                for cls in self.key_components['classes']:
                    md_lines.append(f"- **{cls.name}**: {cls.purpose}")
                    if cls.methods:
                        for method in cls.methods:
                            md_lines.append(f"  - `{method.get('name', 'Unknown')}`: {method.get('purpose', 'No description')}")
                md_lines.append("")
            
            if self.key_components['functions']:
                md_lines.append("### Functions")
                for func in self.key_components['functions']:
                    md_lines.append(f"- **{func.name}**: {func.purpose}")
                    if func.signature:
                        md_lines.append(f"  - Signature: `{func.signature}`")
                    if func.returns:
                        md_lines.append(f"  - Returns: {func.returns}")
                md_lines.append("")
            
            if self.key_components['constants']:
                md_lines.append("### Constants")
                for const in self.key_components['constants']:
                    md_lines.append(f"- **{const.name}**: {const.purpose}")
                md_lines.append("")
            
            if self.key_components['interfaces']:
                md_lines.append("### Interfaces")
                for interface in self.key_components['interfaces']:
                    md_lines.append(f"- **{interface.name}**: {interface.purpose}")
                    if interface.properties:
                        for prop in interface.properties:
                            md_lines.append(f"  - `{prop.get('name', 'Unknown')}`: {prop.get('type', 'Unknown')} - {prop.get('description', 'No description')}")
                md_lines.append("")
        
        # Usage
        if self.usage:
            md_lines.append("## Usage")
            
            if self.usage.get('examples'):
                md_lines.append("### Examples")
                for example in self.usage['examples']:
                    if example.get('description'):
                        md_lines.append(f"- **{example['description']}**")
                    if example.get('code'):
                        md_lines.append(f"```{self.metadata['language']}")
                        md_lines.append(example['code'])
                        md_lines.append("```")
                    if example.get('output'):
                        md_lines.append(f"**Output**: {example['output']}")
                    md_lines.append("")
            
            if self.usage.get('common_patterns'):
                md_lines.append("### Common Patterns")
                for pattern in self.usage['common_patterns']:
                    md_lines.append(f"- {pattern}")
                md_lines.append("")
            
            if self.usage.get('best_practices'):
                md_lines.append("### Best Practices")
                for practice in self.usage['best_practices']:
                    md_lines.append(f"- {practice}")
                md_lines.append("")
            
            if self.usage.get('anti_patterns'):
                md_lines.append("### Anti-patterns")
                for anti_pattern in self.usage['anti_patterns']:
                    md_lines.append(f"- {anti_pattern}")
                md_lines.append("")
        
        # Testing
        if self.testing:
            md_lines.append("## Testing")
            
            if self.testing.get('test_file'):
                md_lines.append(f"- **Test File**: {self.testing['test_file']}")
            
            if self.testing.get('test_coverage') is not None:
                md_lines.append(f"- **Test Coverage**: {self.testing['test_coverage']}%")
            
            if self.testing.get('test_scenarios'):
                md_lines.append("- **Test Scenarios**:")
                for scenario in self.testing['test_scenarios']:
                    md_lines.append(f"  - {scenario}")
            
            if self.testing.get('mocking'):
                md_lines.append("- **Mocking Required**:")
                for mock in self.testing['mocking']:
                    md_lines.append(f"  - {mock}")
            
            md_lines.append("")
        
        # Performance
        if self.performance:
            md_lines.append("## Performance")
            
            if self.performance.get('time_complexity'):
                md_lines.append(f"- **Time Complexity**: {self.performance['time_complexity']}")
            
            if self.performance.get('space_complexity'):
                md_lines.append(f"- **Space Complexity**: {self.performance['space_complexity']}")
            
            if self.performance.get('bottlenecks'):
                md_lines.append("- **Known Bottlenecks**:")
                for bottleneck in self.performance['bottlenecks']:
                    md_lines.append(f"  - {bottleneck}")
            
            if self.performance.get('optimizations'):
                md_lines.append("- **Optimizations Applied**:")
                for opt in self.performance['optimizations']:
                    md_lines.append(f"  - {opt}")
            
            md_lines.append("")
        
        # Security
        if self.security:
            md_lines.append("## Security")
            
            if self.security.get('vulnerabilities'):
                md_lines.append("- **Known Vulnerabilities**:")
                for vuln in self.security['vulnerabilities']:
                    md_lines.append(f"  - {vuln}")
            
            if self.security.get('mitigations'):
                md_lines.append("- **Security Mitigations**:")
                for mitigation in self.security['mitigations']:
                    md_lines.append(f"  - {mitigation}")
            
            if self.security.get('authentication'):
                md_lines.append(f"- **Authentication**: {self.security['authentication']}")
            
            if self.security.get('authorization'):
                md_lines.append(f"- **Authorization**: {self.security['authorization']}")
            
            if self.security.get('data_validation'):
                md_lines.append(f"- **Data Validation**: {self.security['data_validation']}")
            
            md_lines.append("")
        
        # Maintenance
        if self.maintenance:
            md_lines.append("## Maintenance")
            
            if self.maintenance.get('owner'):
                md_lines.append(f"- **Owner**: {self.maintenance['owner']}")
            
            if self.maintenance.get('review_schedule'):
                md_lines.append(f"- **Review Schedule**: {self.maintenance['review_schedule']}")
            
            if self.maintenance.get('deprecation_plan'):
                md_lines.append(f"- **Deprecation Plan**: {self.maintenance['deprecation_plan']}")
            
            if self.maintenance.get('migration_path'):
                md_lines.append(f"- **Migration Path**: {self.maintenance['migration_path']}")
            
            md_lines.append("")
        
        # Related
        if self.related:
            md_lines.append("## Related")
            
            for category, items in self.related.items():
                if items:
                    md_lines.append(f"### {category.title()}")
                    for item in items:
                        md_lines.append(f"- {item}")
                    md_lines.append("")
        
        # Changelog
        if self.changelog:
            md_lines.append("## Changelog")
            for entry in self.changelog:
                md_lines.append(f"- **{entry['date']}** - {entry['change']} (by {entry['author']})")
                if entry.get('version'):
                    md_lines.append(f"  - Version: {entry['version']}")
                if entry.get('reason'):
                    md_lines.append(f"  - Reason: {entry['reason']}")
            md_lines.append("")
        
        # Notes
        if self.notes:
            md_lines.append("## Notes")
            md_lines.append(self.notes)
            md_lines.append("")
        
        return "\n".join(md_lines)
    
    @classmethod
    def from_markdown(cls, file_path: Path, original_path: str) -> 'ContextCard':
        """
        Create context card from markdown file.
        
        Args:
            file_path: Path to the markdown file
            original_path: Original file path
            
        Returns:
            ContextCard instance
        """
        # This is a simplified parser - in practice, you'd want a more robust one
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract basic information
        metadata = {
            'file_path': original_path,
            'language': 'other',
            'domain': 'other'
        }
        
        # Try to extract language and domain from content
        if 'language: ' in content:
            lang_match = re.search(r'language:\s*(\w+)', content)
            if lang_match:
                metadata['language'] = lang_match.group(1)
        
        if 'domain: ' in content:
            domain_match = re.search(r'domain:\s*(\w+)', content)
            if domain_match:
                metadata['domain'] = domain_match.group(1)
        
        return cls(original_path, **metadata)
    
    def validate(self) -> List[str]:
        """
        Validate context card structure.
        
        Returns:
            List of validation errors
        """
        errors = []
        
        # Check required fields
        if not self.metadata.get('file_path'):
            errors.append("File path is required")
        
        if not self.metadata.get('language'):
            errors.append("Language is required")
        
        if not self.metadata.get('domain'):
            errors.append("Domain is required")
        
        if not self.overview:
            errors.append("Overview is required")
        
        if not self.purpose:
            errors.append("Purpose is required")
        
        return errors
