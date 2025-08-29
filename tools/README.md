# CCD for AI Tools

This directory contains tools and utilities for implementing and managing the CCD for AI (Continuous Context Documentation for AI) methodology.

## Available Tools

### CCD for AI CLI

The main command-line interface for CCD for AI methodology implementation.

**Location**: `tools/ccd-cli/`

**Features**:
- **AI-CONTEXT Integration**: Add and manage context comments in source code
- **Methodology Loop Management**: Automate roadmap, engineering log, and ADR updates
- **Quality Gates**: Comprehensive validation including coverage, freshness, health, and drift detection
- **Context Management**: Generate, validate, and maintain context documentation

**Quick Start**:
```bash
# Install CCD for AI CLI
git clone https://github.com/yegorferrieres/ccd-ai.git && cd ccd-ai/tools/ccd-cli && pip install -e .

# Initialize a new CCD for AI project
ccd init --project-name "My Project" --domain "web-application"

# Add AI-CONTEXT comments to source files
ccd add-context-comments --file src/main.py --context docs/contexts/main.py.ctx.md

# Check methodology status
ccd methodology-status --project-dir .

# Run quality gates
ccd quality-gates --project . --output quality-report.json
```

**Documentation**: [tools/ccd-cli/README.md](ccd-cli/README.md)

**Examples**: [tools/ccd-cli/examples](ccd-cli/examples)

## Tool Categories

### 1. Core CLI Tools
- **ccd-cli**: Main command-line interface for CCD for AI methodology

### 2. Development Tools
- **Validation**: Context validation and quality checking
- **Generation**: Automated context card and documentation generation
- **Monitoring**: Health monitoring and drift detection

### 3. Methodology Tools
- **Engineering Log**: Automated logging of development activities
- **Roadmap Management**: Milestone tracking and progress updates
- **ADR Creation**: Architecture Decision Record management
- **Development Rules**: Workflow pattern management
- **AI Context Preparation**: Complete project context generation for AI developers

### 4. Quality Assurance
- **Quality Gates**: Comprehensive validation framework
- **Context Health**: Health scoring and analysis
- **Drift Detection**: Detection of context-code synchronization issues
- **Coverage Analysis**: Documentation coverage metrics

## Integration Points

### CI/CD Integration
All tools are designed to integrate with modern CI/CD pipelines:

```yaml
# GitHub Actions example
- name: Run CCD Quality Gates
  run: ccd quality-gates --project . --output quality-report.json

- name: Check Context Health
  run: ccd context-health --project . --detailed

- name: Detect Context Drift
  run: ccd drift-detection --project . --output drift-report.json
```

### Development Workflow
Tools integrate with the CCD methodology loop:

```bash
# After completing development
ccd update-engineering-log --description "Implemented feature" --impact "Medium"
ccd update-roadmap --milestone "Feature X" --status "completed"
ccd add-context-comments --file src/feature.py --context docs/contexts/feature.py.ctx.md

# Prepare complete context for AI developer
ccd prepare-context --project-dir . --output task-context.txt
```

## Tool Architecture

### Command Structure
All tools follow a consistent command structure:
- **Primary Commands**: Core functionality (init, generate, validate)
- **AI-CONTEXT Commands**: Context comment management
- **Methodology Commands**: Loop automation
- **Quality Commands**: Validation and health checking
- **Context Preparation Commands**: Complete project context generation for AI developers

### Output Formats
Tools support multiple output formats:
- **Text**: Human-readable output with colors and formatting
- **JSON**: Machine-readable output for automation
- **YAML**: Structured output for configuration

### Configuration
Tools use consistent configuration patterns:
- **Project-level**: `.ccd/` directory for project configuration
- **Global**: User home directory for global settings
- **Environment**: Environment variables for CI/CD integration

## Development Guidelines

### Adding New Tools
1. **Follow Structure**: Use consistent directory and file organization
2. **Documentation**: Include comprehensive README and examples
3. **Testing**: Provide test coverage and validation
4. **Integration**: Ensure integration with existing tools

### Tool Standards
- **Error Handling**: Consistent error handling and user feedback
- **Logging**: Structured logging for debugging and monitoring
- **Performance**: Optimize for common use cases
- **Accessibility**: Clear help text and examples

## Examples and Use Cases

### Basic Project Setup
```bash
# Initialize project
ccd init --project-name "My API" --domain "api-service"

# Generate initial context
ccd generate-cards --files "src/**/*.py" --output docs/contexts/

# Add AI-CONTEXT comments
ccd add-context-comments --file src/main.py --context docs/contexts/main.py.ctx.md

# Validate everything
ccd validate-contexts --contexts docs/ --schemas docs/schemas/
```

### Daily Development Workflow
```bash
# Check current status
ccd methodology-status --project-dir .

# After completing a task
ccd update-engineering-log --description "Implemented user auth" --impact "High"

# Mark milestone complete
ccd update-roadmap --milestone "User Authentication" --status "completed"

# Check quality
ccd quality-gates --project . --output quality-report.json
```

### CI/CD Integration
```bash
# Pre-commit validation
ccd validate-context-comments --project . --strict

# Post-merge quality check
ccd quality-gates --project . --output quality-report.json

# Health monitoring
ccd context-health --project . --detailed
```

## Troubleshooting

### Common Issues

**Tool Installation**
```bash
# Check installation
ccd --version

# Reinstall if needed
cd ccd-ai/tools/ccd-cli
pip uninstall ccd-cli
pip install -e .
```

**Configuration Issues**
```bash
# Check configuration
ccd init --help

# Reset configuration
rm -rf .ccd/
ccd init --project-name "Project" --domain "web-application"
```

**Validation Failures**
```bash
# Run quality gates
ccd quality-gates --project . --output quality-report.json

# Check specific issues
ccd context-health --project . --detailed
ccd drift-detection --project . --output drift-report.json
```

## Contributing

We welcome contributions to CCD for AI tools! See our [Contributing Guide](../CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone repository
git clone https://github.com/yegorferrieres/ccd-ai.git
cd ccd-ai

# Install development dependencies
pip install -e "tools/ccd-cli/.[dev]"

# Run tests
cd tools/ccd-cli
pytest tests/
```

## Resources

- **CCD for AI Methodology**: [docs/README.md](../docs/README.md)
- **CLI Documentation**: [tools/ccd-cli/README.md](ccd-cli/README.md)
- **Examples**: [tools/ccd-cli/examples](ccd-cli/examples)
- **Development Rules**: [docs/DEVELOPMENT_RULES.md](../docs/DEVELOPMENT_RULES.md)

---

**Status**: Active Development  
**Last Updated**: 2025-08-28  
**Version**: 1.0.0
