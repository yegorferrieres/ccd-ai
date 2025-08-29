"""
Configuration Utilities

Configuration loading and management for CCD CLI.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import yaml

from .errors import ConfigurationError


def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Load CCD configuration from file or environment.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
        
    Raises:
        ConfigurationError: If configuration is invalid
    """
    # Default configuration
    default_config = {
        'project': {
            'name': None,
            'domain': None,
            'schemas_path': './docs/schemas',
            'contexts_path': './docs'
        },
        'generation': {
            'auto_update': True,
            'include_tests': False,
            'include_docs': True,
            'max_file_size': '10MB',
            'exclude_patterns': [
                '*.pyc',
                '__pycache__',
                '.git',
                'node_modules',
                '*.log',
                '*.tmp'
            ]
        },
        'validation': {
            'strict_mode': True,
            'fail_fast': False,
            'max_errors': 100,
            'schema_validation': True,
            'content_validation': True
        },
        'output': {
            'default_format': 'text',
            'colors': True,
            'progress_bars': True,
            'verbose': False,
            'quiet': False
        },
        'monitoring': {
            'watch_interval': 60,
            'health_check_interval': 300,
            'coverage_threshold': 80,
            'freshness_threshold': 90
        },
        'ci_cd': {
            'auto_commit': False,
            'auto_push': False,
            'create_pr': False,
            'branch_prefix': 'ccd-update'
        }
    }
    
    # Try to load from specified path
    if config_path:
        config = _load_config_file(config_path)
        return _merge_configs(default_config, config)
    
    # Try to load from default locations
    config = _load_default_config()
    if config:
        return _merge_configs(default_config, config)
    
    # Try to load from environment variables
    env_config = _load_env_config()
    return _merge_configs(default_config, env_config)


def _load_config_file(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a specific file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
        
    Raises:
        ConfigurationError: If file cannot be loaded or parsed
    """
    try:
        path = Path(config_path)
        if not path.exists():
            raise ConfigurationError(f"Configuration file not found: {config_path}")
        
        if not path.is_file():
            raise ConfigurationError(f"Path is not a file: {config_path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        if not isinstance(config, dict):
            raise ConfigurationError(f"Configuration file must contain a dictionary: {config_path}")
        
        return config
        
    except yaml.YAMLError as e:
        raise ConfigurationError(f"Invalid YAML in configuration file: {config_path}", str(e))
    except Exception as e:
        raise ConfigurationError(f"Failed to load configuration file: {config_path}", str(e))


def _load_default_config() -> Optional[Dict[str, Any]]:
    """
    Load configuration from default locations.
    
    Returns:
        Configuration dictionary or None if not found
    """
    # Look for config files in current directory and parent directories
    current_dir = Path.cwd()
    
    config_files = [
        'ccd.config.yaml',
        'ccd.config.yml',
        '.ccd.yaml',
        '.ccd.yml'
    ]
    
    # Check current directory
    for config_file in config_files:
        config_path = current_dir / config_file
        if config_path.exists():
            try:
                return _load_config_file(str(config_path))
            except ConfigurationError:
                continue
    
    # Check parent directories (up to 3 levels)
    for i in range(3):
        current_dir = current_dir.parent
        for config_file in config_files:
            config_path = current_dir / config_file
            if config_path.exists():
                try:
                    return _load_config_file(str(config_path))
                except ConfigurationError:
                    continue
    
    return None


def _load_env_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables.
    
    Returns:
        Configuration dictionary
    """
    config = {}
    
    # Project configuration
    if os.getenv('CCD_PROJECT_NAME'):
        if 'project' not in config:
            config['project'] = {}
        config['project']['name'] = os.getenv('CCD_PROJECT_NAME')
    
    if os.getenv('CCD_PROJECT_DOMAIN'):
        if 'project' not in config:
            config['project'] = {}
        config['project']['domain'] = os.getenv('CCD_PROJECT_DOMAIN')
    
    if os.getenv('CCD_SCHEMAS_PATH'):
        if 'project' not in config:
            config['project'] = {}
        config['project']['schemas_path'] = os.getenv('CCD_SCHEMAS_PATH')
    
    if os.getenv('CCD_CONTEXTS_PATH'):
        if 'project' not in config:
            config['project'] = {}
        config['project']['contexts_path'] = os.getenv('CCD_CONTEXTS_PATH')
    
    # Generation configuration
    if os.getenv('CCD_AUTO_UPDATE'):
        if 'generation' not in config:
            config['generation'] = {}
        config['generation']['auto_update'] = os.getenv('CCD_AUTO_UPDATE').lower() == 'true'
    
    if os.getenv('CCD_INCLUDE_TESTS'):
        if 'generation' not in config:
            config['generation'] = {}
        config['generation']['include_tests'] = os.getenv('CCD_INCLUDE_TESTS').lower() == 'true'
    
    # Validation configuration
    if os.getenv('CCD_STRICT_MODE'):
        if 'validation' not in config:
            config['validation'] = {}
        config['validation']['strict_mode'] = os.getenv('CCD_STRICT_MODE').lower() == 'true'
    
    if os.getenv('CCD_FAIL_FAST'):
        if 'validation' not in config:
            config['validation'] = {}
        config['validation']['fail_fast'] = os.getenv('CCD_FAIL_FAST').lower() == 'true'
    
    # Output configuration
    if os.getenv('CCD_OUTPUT_FORMAT'):
        if 'output' not in config:
            config['output'] = {}
        config['output']['default_format'] = os.getenv('CCD_OUTPUT_FORMAT')
    
    if os.getenv('CCD_COLORS'):
        if 'output' not in config:
            config['output'] = {}
        config['output']['colors'] = os.getenv('CCD_COLORS').lower() == 'true'
    
    if os.getenv('CCD_VERBOSE'):
        if 'output' not in config:
            config['output'] = {}
        config['output']['verbose'] = os.getenv('CCD_VERBOSE').lower() == 'true'
    
    if os.getenv('CCD_QUIET'):
        if 'output' not in config:
            config['output'] = {}
        config['output']['quiet'] = os.getenv('CCD_QUIET').lower() == 'true'
    
    # Monitoring configuration
    if os.getenv('CCD_WATCH_INTERVAL'):
        if 'monitoring' not in config:
            config['monitoring'] = {}
        try:
            config['monitoring']['watch_interval'] = int(os.getenv('CCD_WATCH_INTERVAL'))
        except ValueError:
            pass
    
    if os.getenv('CCD_COVERAGE_THRESHOLD'):
        if 'monitoring' not in config:
            config['monitoring'] = {}
        try:
            config['monitoring']['coverage_threshold'] = int(os.getenv('CCD_COVERAGE_THRESHOLD'))
        except ValueError:
            pass
    
    return config


def _merge_configs(default: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge configuration dictionaries.
    
    Args:
        default: Default configuration
        override: Override configuration
        
    Returns:
        Merged configuration
    """
    result = default.copy()
    
    def _merge_dict(target: Dict[str, Any], source: Dict[str, Any]):
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                _merge_dict(target[key], value)
            else:
                target[key] = value
    
    _merge_dict(result, override)
    return result


def save_config(config: Dict[str, Any], config_path: str) -> None:
    """
    Save configuration to file.
    
    Args:
        config: Configuration dictionary
        config_path: Path to save configuration
        
    Raises:
        ConfigurationError: If configuration cannot be saved
    """
    try:
        path = Path(config_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False, indent=2)
            
    except Exception as e:
        raise ConfigurationError(f"Failed to save configuration: {config_path}", str(e))


def validate_config(config: Dict[str, Any]) -> list:
    """
    Validate configuration structure and values.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        List of validation errors
    """
    errors = []
    
    # Check required sections
    required_sections = ['project', 'generation', 'validation', 'output']
    for section in required_sections:
        if section not in config:
            errors.append(f"Missing required configuration section: {section}")
    
    # Validate project section
    if 'project' in config:
        project = config['project']
        if 'schemas_path' in project:
            schemas_path = Path(project['schemas_path'])
            if not schemas_path.exists():
                errors.append(f"Schemas path does not exist: {schemas_path}")
        
        if 'contexts_path' in project:
            contexts_path = Path(project['contexts_path'])
            if not contexts_path.exists():
                errors.append(f"Contexts path does not exist: {contexts_path}")
    
    # Validate generation section
    if 'generation' in config:
        generation = config['generation']
        if 'max_file_size' in generation:
            max_size = generation['max_file_size']
            if not isinstance(max_size, str) or not _is_valid_size_string(max_size):
                errors.append(f"Invalid max_file_size format: {max_size}")
    
    # Validate validation section
    if 'validation' in config:
        validation = config['validation']
        if 'max_errors' in validation:
            max_errors = validation['max_errors']
            if not isinstance(max_errors, int) or max_errors < 1:
                errors.append(f"max_errors must be a positive integer: {max_errors}")
    
    # Validate output section
    if 'output' in config:
        output = config['output']
        if 'default_format' in output:
            valid_formats = ['text', 'json', 'yaml']
            if output['default_format'] not in valid_formats:
                errors.append(f"Invalid output format: {output['default_format']}. Must be one of: {valid_formats}")
    
    # Validate monitoring section
    if 'monitoring' in config:
        monitoring = config['monitoring']
        if 'coverage_threshold' in monitoring:
            threshold = monitoring['coverage_threshold']
            if not isinstance(threshold, (int, float)) or threshold < 0 or threshold > 100:
                errors.append(f"coverage_threshold must be between 0 and 100: {threshold}")
        
        if 'freshness_threshold' in monitoring:
            threshold = monitoring['freshness_threshold']
            if not isinstance(threshold, (int, float)) or threshold < 0 or threshold > 100:
                errors.append(f"freshness_threshold must be between 0 and 100: {threshold}")
    
    return errors


def _is_valid_size_string(size_str: str) -> bool:
    """
    Check if a size string is valid.
    
    Args:
        size_str: Size string (e.g., "10MB", "1.5GB")
        
    Returns:
        True if valid, False otherwise
    """
    import re
    
    # Pattern: number followed by optional decimal and unit
    pattern = r'^\d+(\.\d+)?\s*(B|KB|MB|GB|TB)$'
    return bool(re.match(pattern, size_str.upper()))
