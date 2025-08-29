# Publishing ccd-cli to PyPI

This document describes how to publish the `ccd-cli` package to PyPI.

## ✅ SUCCESS: Package Published!

**ccd-cli 0.1.0 is now available on PyPI!**

- **PyPI**: https://pypi.org/project/ccd-cli/0.1.0/
- **TestPyPI**: https://test.pypi.org/project/ccd-cli/0.1.0/
- **Install**: `pip install ccd-cli`

## Prerequisites

1. **PyPI Account**: You need a PyPI account at [pypi.org](https://pypi.org)
2. **TestPyPI Account**: You need a TestPyPI account at [test.pypi.org](https://test.pypi.org)
3. **Build Tools**: Install required tools:
   ```bash
   pip install build twine
   ```

## Building the Package

From the `tools/ccd-cli/` directory:

```bash
# Build source distribution and wheel
python -m build

# This creates:
# - dist/ccd_cli-0.1.0.tar.gz (source distribution)
# - dist/ccd_cli-0.1.0-py3-none-any.whl (wheel)
```

## Testing on TestPyPI

Before publishing to PyPI, test on TestPyPI:

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ ccd-cli

# Test the CLI
ccd --help
```

## Publishing to PyPI

Once tested on TestPyPI:

```bash
# Upload to PyPI
twine upload dist/*

# Verify installation
pip install ccd-cli
ccd --help
```

## Automated Publishing

The package is automatically published to PyPI when a GitHub release is published.

### GitHub Secrets Required

Set these secrets in your GitHub repository:

- `pypi_username`: Your PyPI username
- `pypi_password`: Your PyPI password or API token

### Release Process

1. Update version in `pyproject.toml`
2. Create and push a new tag
3. Create a GitHub release
4. The GitHub Action will automatically build and publish to PyPI

## Package Structure

```
tools/ccd-cli/
├── pyproject.toml          # Package configuration
├── README.md               # Package documentation
├── LICENSE                 # MIT license
├── .pypirc                 # PyPI credentials (local only)
├── src/                    # Source code layout
│   └── ccd_cli/
│       ├── __init__.py
│       ├── __main__.py     # Entry point for console script
│       ├── cli.py          # Main CLI logic
│       ├── commands/       # CLI commands
│       ├── core/           # Core functionality
│       └── utils/          # Utility functions
├── examples/               # Usage examples
└── tests/                  # Test suite
```

## Entry Point

The console script `ccd` is configured to call `ccd_cli.__main__:main` from the `__main__.py` file.

## Version Management

- Update version in `pyproject.toml`
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Current version: 0.1.0

## Troubleshooting

### Build Issues

- Ensure all dependencies are installed
- Check that `src/` layout is correct
- Verify `pyproject.toml` syntax

### Upload Issues

- Check PyPI credentials in `.pypirc`
- Ensure package name is unique
- Verify package format with `twine check dist/*`

### Installation Issues

- Test with `pip install -e .` first
- Check console script entry point
- Verify package structure

## Current Status

- ✅ Package built successfully
- ✅ Package uploaded to TestPyPI
- ✅ Package tested on TestPyPI
- ✅ Package uploaded to PyPI
- ✅ Package tested on PyPI
- ✅ CLI working correctly
- ✅ GitHub Actions workflow configured

## Next Steps

For future releases:

1. Update version in `pyproject.toml`
2. Run `python -m build`
3. Test on TestPyPI: `twine upload --repository testpypi dist/*`
4. Publish to PyPI: `twine upload dist/*`
5. Or create GitHub release for automated publishing
