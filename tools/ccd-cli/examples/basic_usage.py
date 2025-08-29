#!/usr/bin/env python3
"""
Basic Usage Example

Demonstrate basic usage of the CCD CLI tool.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command: list) -> tuple:
    """Run a command and return output and exit code."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1


def main():
    """Run basic usage examples."""
    print("CCD CLI Basic Usage Examples")
    print("=" * 50)
    
    # Check if CCD CLI is installed
    print("\n1. Checking CCD CLI installation...")
    stdout, stderr, exit_code = run_command(["ccd", "--version"])
    
    if exit_code == 0:
        print("✓ CCD CLI is installed")
        print(f"Version: {stdout.strip()}")
    else:
        print("✗ CCD CLI is not installed or not in PATH")
        print("Install with: git clone https://github.com/yegorferrieres/ccd-ai.git && cd ccd-ai/tools/ccd-cli && pip install -e .")
        return
    
    # Show help
    print("\n2. Showing CLI help...")
    stdout, stderr, exit_code = run_command(["ccd", "--help"])
    if exit_code == 0:
        print("✓ Help command works")
        # Show first few lines of help
        help_lines = stdout.strip().split('\n')[:10]
        for line in help_lines:
            print(f"  {line}")
        print("  ...")
    else:
        print("✗ Help command failed")
    
    # Show version
    print("\n3. Showing version...")
    stdout, stderr, exit_code = run_command(["ccd", "version"])
    if exit_code == 0:
        print("✓ Version command works")
        # Show first few lines
        version_lines = stdout.strip().split('\n')[:5]
        for line in version_lines:
            print(f"  {line}")
    else:
        print("✗ Version command failed")
    
    # Show init help
    print("\n4. Showing init command help...")
    stdout, stderr, exit_code = run_command(["ccd", "init", "--help"])
    if exit_code == 0:
        print("✓ Init command help works")
        # Show key options
        help_lines = stdout.strip().split('\n')
        for line in help_lines:
            if any(keyword in line.lower() for keyword in ['--project-name', '--domain', '--output-dir']):
                print(f"  {line}")
    else:
        print("✗ Init command help failed")
    
    # Show health help
    print("\n5. Showing health command help...")
    stdout, stderr, exit_code = run_command(["ccd", "health", "--help"])
    if exit_code == 0:
        print("✓ Health command help works")
        # Show key options
        help_lines = stdout.strip().split('\n')
        for line in help_lines:
            if any(keyword in line.lower() for keyword in ['--detailed', '--output-format']):
                print(f"  {line}")
    else:
        print("✗ Health command help failed")
    
    print("\n" + "=" * 50)
    print("Basic usage examples completed!")
    print("\nTo try the CLI:")
    print("1. Initialize a project: ccd init --project-name 'My Project' --domain 'web-application'")
    print("2. Check health: ccd health --detailed")
    print("3. Get help: ccd --help")


if __name__ == "__main__":
    main()
