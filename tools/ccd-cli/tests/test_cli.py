"""
Test CLI functionality.
"""

import pytest
from click.testing import CliRunner
from ccd_cli.cli import cli


def test_cli_help():
    """Test CLI help command."""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'CCD (Continuous Context Documentation) CLI Tool' in result.output


def test_cli_version():
    """Test CLI version command."""
    runner = CliRunner()
    result = runner.invoke(cli, ['version'])
    assert result.exit_code == 0
    assert 'CCD CLI Version Information' in result.output


def test_cli_init_help():
    """Test CLI init help."""
    runner = CliRunner()
    result = runner.invoke(cli, ['init', '--help'])
    assert result.exit_code == 0
    assert 'Initialize a new CCD project' in result.output


def test_cli_health_help():
    """Test CLI health help."""
    runner = CliRunner()
    result = runner.invoke(cli, ['health', '--help'])
    assert result.exit_code == 0
    assert 'Check CCD project health' in result.output
