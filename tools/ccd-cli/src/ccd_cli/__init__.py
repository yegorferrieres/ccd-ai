"""
CCD (Continuous Context Documentation) CLI Tool

A command-line interface for managing and maintaining continuous context documentation
in software projects.
"""

__version__ = "1.0.0"
__author__ = "CCD Team"
__email__ = "yegor@martlive.ai"

from .cli import main
from .core import CCDProject, ContextCard, ModuleIndex, CODEMAP

__all__ = [
    "main",
    "CCDProject",
    "ContextCard", 
    "ModuleIndex",
    "CODEMAP",
]
