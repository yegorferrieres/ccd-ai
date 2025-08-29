"""
Module Index Class

Represents module-level context documentation in CCD.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import yaml


@dataclass
class FileInfo:
    """File information for module index."""
    path: str
    type: str
    description: str
    language: str
    size: Optional[str] = None
    lines: Optional[int] = None
    context_card: Optional[str] = None
    complexity: Optional[str] = None
    priority: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class InterfaceInfo:
    """Interface information for module index."""
    name: str
    type: str
    description: str
    signature: Optional[str] = None
    parameters: Optional[List[Dict[str, Any]]] = None
    returns: Optional[str] = None


class ModuleIndex:
    """
    Module-level context documentation.
    
    This class represents the context for a specific module within a project,
    including its purpose, files, interfaces, and dependencies.
    """
    
    def __init__(self, module_path: str, module_type: str, description: str, **kwargs):
        """
        Initialize a new module index.
        
        Args:
            module_path: Path to the module
            module_type: Type of module
            description: Module description
            **kwargs: Additional module properties
        """
        self.module = {
            'name': kwargs.get('name', module_path.split('/')[-1]),
            'path': module_path,
            'type': module_type,
            'version': kwargs.get('version'),
            'status': kwargs.get('status', 'development')
        }
        
        self.purpose = description
        self.responsibilities = kwargs.get('responsibilities', [])
        self.files: List[Dict[str, Any]] = []
        self.dependencies: List[Dict[str, Any]] = []
        self.interfaces: List[Dict[str, Any]] = []
        self.configuration = kwargs.get('configuration', {})
        self.testing = kwargs.get('testing', {})
        self.deployment = kwargs.get('deployment', {})
        
        self.metadata = {
            'created': datetime.now().isoformat(),
            'updated': datetime.now().isoformat(),
            'generator': {
                'tool': 'ccd-cli',
                'version': '1.0.0',
                'timestamp': datetime.now().isoformat()
            }
        }
    
    def add_file(self, file_info: FileInfo) -> None:
        """
        Add a file to the module index.
        
        Args:
            file_info: File information
        """
        file_dict = {
            'path': file_info.path,
            'type': file_info.type,
            'description': file_info.description,
            'language': file_info.language,
            'size': file_info.size,
            'lines': file_info.lines,
            'context_card': file_info.context_card,
            'complexity': file_info.complexity,
            'priority': file_info.priority,
            'tags': file_info.tags
        }
        
        # Remove None values
        file_dict = {k: v for k, v in file_dict.items() if v is not None}
        
        self.files.append(file_dict)
        self._update_metadata()
    
    def add_dependency(self, module: str, dep_type: str, description: str, **kwargs) -> None:
        """
        Add a dependency to the module index.
        
        Args:
            module: Dependency module name
            dep_type: Dependency type
            description: Dependency description
            **kwargs: Additional dependency properties
        """
        dependency = {
            'module': module,
            'type': dep_type,
            'description': description,
            'version': kwargs.get('version'),
            'optional': kwargs.get('optional', False)
        }
        
        # Remove None values
        dependency = {k: v for k, v in dependency.items() if v is not None}
        
        self.dependencies.append(dependency)
        self._update_metadata()
    
    def add_interface(self, interface_info: InterfaceInfo) -> None:
        """
        Add an interface to the module index.
        
        Args:
            interface_info: Interface information
        """
        interface_dict = {
            'name': interface_info.name,
            'type': interface_info.type,
            'description': interface_info.description,
            'signature': interface_info.signature,
            'parameters': interface_info.parameters,
            'returns': interface_info.returns
        }
        
        # Remove None values
        interface_dict = {k: v for k, v in interface_dict.items() if v is not None}
        
        self.interfaces.append(interface_dict)
        self._update_metadata()
    
    def _update_metadata(self) -> None:
        """Update metadata timestamps."""
        self.metadata['updated'] = datetime.now().isoformat()
        self.metadata['generator']['timestamp'] = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert module index to dictionary.
        
        Returns:
            Dictionary representation of module index
        """
        return {
            'module': self.module,
            'purpose': self.purpose,
            'responsibilities': self.responsibilities,
            'files': self.files,
            'dependencies': self.dependencies,
            'interfaces': self.interfaces,
            'configuration': self.configuration,
            'testing': self.testing,
            'deployment': self.deployment,
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModuleIndex':
        """
        Create module index from dictionary.
        
        Args:
            data: Dictionary data
            
        Returns:
            ModuleIndex instance
        """
        module_index = cls(
            module_path=data['module']['path'],
            module_type=data['module']['type'],
            description=data['purpose']
        )
        
        module_index.module.update(data['module'])
        module_index.responsibilities = data.get('responsibilities', [])
        module_index.files = data.get('files', [])
        module_index.dependencies = data.get('dependencies', [])
        module_index.interfaces = data.get('interfaces', [])
        module_index.configuration = data.get('configuration', {})
        module_index.testing = data.get('testing', {})
        module_index.deployment = data.get('deployment', {})
        module_index.metadata = data.get('metadata', {})
        
        return module_index
    
    def validate(self) -> List[str]:
        """
        Validate module index structure.
        
        Returns:
            List of validation errors
        """
        errors = []
        
        # Check required fields
        if not self.module.get('name'):
            errors.append("Module name is required")
        
        if not self.module.get('path'):
            errors.append("Module path is required")
        
        if not self.module.get('type'):
            errors.append("Module type is required")
        
        if not self.purpose:
            errors.append("Module purpose is required")
        
        if not self.files:
            errors.append("At least one file is required")
        
        # Check file structure
        for i, file_info in enumerate(self.files):
            if not file_info.get('path'):
                errors.append(f"File {i}: path is required")
            if not file_info.get('type'):
                errors.append(f"File {i}: type is required")
            if not file_info.get('description'):
                errors.append(f"File {i}: description is required")
            if not file_info.get('language'):
                errors.append(f"File {i}: language is required")
        
        # Check dependency structure
        for i, dependency in enumerate(self.dependencies):
            if not dependency.get('module'):
                errors.append(f"Dependency {i}: module is required")
            if not dependency.get('type'):
                errors.append(f"Dependency {i}: type is required")
            if not dependency.get('description'):
                errors.append(f"Dependency {i}: description is required")
        
        # Check interface structure
        for i, interface in enumerate(self.interfaces):
            if not interface.get('name'):
                errors.append(f"Interface {i}: name is required")
            if not interface.get('type'):
                errors.append(f"Interface {i}: type is required")
            if not interface.get('description'):
                errors.append(f"Interface {i}: description is required")
        
        return errors
    
    def get_file_by_path(self, path: str) -> Optional[Dict[str, Any]]:
        """
        Get file by path.
        
        Args:
            path: File path
            
        Returns:
            File dictionary or None
        """
        for file_info in self.files:
            if file_info.get('path') == path:
                return file_info
        return None
    
    def get_files_by_type(self, file_type: str) -> List[Dict[str, Any]]:
        """
        Get files by type.
        
        Args:
            file_type: File type
            
        Returns:
            List of files
        """
        return [f for f in self.files if f.get('type') == file_type]
    
    def get_files_by_language(self, language: str) -> List[Dict[str, Any]]:
        """
        Get files by language.
        
        Args:
            language: Programming language
            
        Returns:
            List of files
        """
        return [f for f in self.files if f.get('language') == language]
    
    def get_dependencies_by_type(self, dep_type: str) -> List[Dict[str, Any]]:
        """
        Get dependencies by type.
        
        Args:
            dep_type: Dependency type
            
        Returns:
            List of dependencies
        """
        return [dep for dep in self.dependencies if dep.get('type') == dep_type]
    
    def get_interfaces_by_type(self, interface_type: str) -> List[Dict[str, Any]]:
        """
        Get interfaces by type.
        
        Args:
            interface_type: Interface type
            
        Returns:
            List of interfaces
        """
        return [intf for intf in self.interfaces if intf.get('type') == interface_type]
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get module index statistics.
        
        Returns:
            Dictionary with statistics
        """
        total_lines = sum(file_info.get('lines', 0) for file_info in self.files)
        
        languages = {}
        for file_info in self.files:
            lang = file_info.get('language', 'unknown')
            languages[lang] = languages.get(lang, 0) + 1
        
        file_types = {}
        for file_info in self.files:
            ftype = file_info.get('type', 'unknown')
            file_types[ftype] = file_types.get(ftype, 0) + 1
        
        return {
            'total_files': len(self.files),
            'total_lines': total_lines,
            'total_dependencies': len(self.dependencies),
            'total_interfaces': len(self.interfaces),
            'languages': languages,
            'file_types': file_types,
            'created': self.metadata.get('created'),
            'updated': self.metadata.get('updated')
        }
