"""
CCD CLI Commands

Command implementations for the CCD CLI tool.
"""

from .init import init_command
from .validate import validate_command
from .generate import generate_command
from .health import health_command
from .coverage import coverage_command
from .freshness import freshness_command
from .pack import pack_command
from .monitor import monitor_command
from .version import version_command

# AI-CONTEXT Comments Management
from .ai_context import (
    add_context_comments,
    extract_context,
    validate_context_comments
)

# Methodology Loop Management
from .methodology import (
    update_engineering_log_cmd,
    update_roadmap_cmd,
    create_adr_cmd,
    update_development_rules_cmd,
    methodology_status
)

# Quality Gates and Validation
from .quality import (
    context_freshness,
    context_health,
    drift_detection,
    quality_gates
)

# Context Preparation for AI
from .prepare_context import (
    prepare_context_cmd
)

__all__ = [
    "init_command",
    "validate_command", 
    "generate_command",
    "health_command",
    "coverage_command",
    "freshness_command",
    "pack_command",
    "monitor_command",
    "version_command",
    
    # AI-CONTEXT Comments Management
    "add_context_comments",
    "extract_context", 
    "validate_context_comments",
    
    # Methodology Loop Management
    "update_engineering_log_cmd",
    "update_roadmap_cmd",
    "create_adr_cmd",
    "update_development_rules_cmd",
    "methodology_status",
    
    # Quality Gates and Validation
    "context_freshness",
    "context_health",
    "drift_detection",
    "quality_gates",
    
    # Context Preparation for AI
    "prepare_context_cmd",
]
