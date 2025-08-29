# Contributing to CCD for AI

Thank you for your interest in contributing to the Continuous Context Documentation for AI (CCD for AI) methodology! This document provides guidelines and information for contributors.

## How to Contribute

### 1. **Report Issues**
- Use the [issue templates](.github/ISSUE_TEMPLATE/) to report bugs or request features
- Provide clear descriptions and reproduction steps
- Include relevant context and error messages

### 2. **Submit Pull Requests**
- Fork the repository and create a feature branch
- Follow the [development workflow](docs/development-workflow.md)
- Ensure all tests pass and documentation is updated
- Use conventional commit messages

### 3. **Improve Documentation**
- Fix typos, clarify unclear sections
- Add examples and use cases
- Improve templates and schemas
- Update playbooks and checklists

### 4. **Enhance Tools**
- Improve the `ccd-cli` functionality (Python-based CLI)
- Add new validation rules
- Enhance CI/CD workflows
- Create new templates and schemas

## Development Setup

### Prerequisites
- Python 3.8+ (required for ccd-cli)
- Git
- pip (Python package manager)

### Local Development
```bash
# Clone the repository
git clone https://github.com/yegorferrieres/ccd-ai.git
cd ccd-ai

# Install ccd-cli in development mode
cd tools/ccd-cli
pip install -e ".[dev]"

# Run tests
pytest

# Run linting and formatting
black .
isort .
flake8

# Build CLI
pip install -e .

# Validate context
ccd validate-contexts
```

## Contribution Guidelines

### Code Style
- Follow Python best practices (PEP 8)
- Use Black for code formatting
- Use isort for import sorting
- Use flake8 for linting
- Write meaningful commit messages
- Include docstrings for public APIs

### Documentation Standards
- Use clear, concise language
- Include practical examples
- Follow the established template structure
- Validate against JSON schemas

### Testing Requirements
- Write unit tests using pytest
- Ensure existing tests pass
- Add integration tests for CLI commands
- Test against different file types and scenarios
- Aim for >80% test coverage

## Development Workflow

### 1. **Context First**
- Always read relevant context files before starting
- Understand the existing architecture and patterns
- Check for similar functionality to avoid duplication

### 2. **Follow CCD Principles**
- Update context files after changes
- Validate changes before committing
- Maintain documentation currency
- Follow the established workflow

### 3. **Quality Gates**
- Run validation scripts
- Check schema compliance
- Ensure context coverage
- Test CLI functionality

## Project Structure

### Key Directories
- `docs/` - Core methodology documentation
- `tools/ccd-cli/` - Python-based command-line interface
- `site/` - MkDocs website
- `examples/` - Sample implementations
- `schemas/` - JSON validation schemas

### Important Files
- `DEVELOPMENT_RULES.md` - Development guidelines
- `ENGINEERING_LOG.md` - Change log
- `decisions/` - Architecture Decision Records
- `roadmap.md` - Development roadmap

## Testing

### Running Tests
```bash
# Unit tests
pytest

# With coverage
pytest --cov=ccd_cli

# Integration tests
pytest tests/integration/

# Context validation
ccd validate-contexts

# Schema validation
ccd validate-schemas
```

### Test Coverage
- Aim for >80% test coverage
- Test edge cases and error conditions
- Include performance benchmarks
- Test cross-platform compatibility

## Documentation Updates

### When to Update
- Adding new features or commands
- Changing CLI interfaces
- Updating schemas or templates
- Modifying workflows or processes

### How to Update
- Follow the established template structure
- Include practical examples
- Update related documentation
- Validate against schemas

## Review Process

### Pull Request Review
- All PRs require at least one review
- Maintainers review for technical accuracy
- Community members review for usability
- Automated checks must pass

### Review Criteria
- **Functionality**: Does it work as intended?
- **Documentation**: Is it well-documented?
- **Testing**: Are tests comprehensive?
- **Standards**: Does it follow project guidelines?

## Common Issues

### Context Validation Failures
- Check JSON schema compliance
- Verify required fields are present
- Ensure proper file structure
- Run validation locally first

### CLI Build Issues
- Check Python version compatibility (3.8+)
- Verify all dependencies are installed
- Ensure virtual environment is activated
- Check for syntax errors

### Documentation Build Failures
- Validate markdown syntax
- Check internal links
- Verify front matter format
- Test local MkDocs build

## Contribution Areas

### High Priority
- **CLI Enhancements**: New commands and features for ccd-cli
- **Schema Validation**: Improved validation rules
- **CI/CD Workflows**: Better automation
- **Documentation**: Clearer examples and guides

### Medium Priority
- **Template Library**: More context card templates
- **Integration Examples**: Additional use cases
- **Performance**: Optimization and benchmarking
- **Testing**: Better test coverage and scenarios

### Low Priority
- **Website**: UI/UX improvements
- **Localization**: Multi-language support
- **Analytics**: Usage tracking and metrics
- **Community**: Outreach and engagement

## Getting Help

### Community Resources
- [GitHub Discussions](https://github.com/yegorferrieres/ccd-ai/discussions)
- [Issue Tracker](https://github.com/yegorferrieres/ccd-ai/issues)
- [Documentation](https://github.com/yegorferrieres/ccd-ai)

### Direct Contact
- **Maintainers**: [@yegorferrieres](https://github.com/yegorferrieres)
- **Security Issues**: yegor@martlive.ai

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes and changelog
- Project documentation
- Community acknowledgments

## License

By contributing to CCD for AI, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

**Thank you for contributing to the future of AI-powered software development!**
