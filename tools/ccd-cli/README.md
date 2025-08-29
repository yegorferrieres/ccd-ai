# CCD for AI CLI

A Python-based command-line interface for CCD for AI (Continuous Context Documentation for AI) methodology.

## Features

- **Project Initialization**: Set up new CCD projects with proper structure
- **Context Generation**: Automatically generate context cards, module indexes, and CODEMAP
- **AI-CONTEXT Integration**: Add and manage context comments in source code files
- **Validation**: Validate CCD documentation against JSON schemas
- **Health Monitoring**: Check project health and coverage metrics
- **Automation**: CI/CD integration and automated context updates
- **Rich Output**: Beautiful terminal output with colors and formatting

## Installation

### From PyPI (Recommended)

```bash
pip install ccd-cli
```

**✅ Package successfully published to PyPI!**  
You can now install `ccd-cli` directly from PyPI using the command above.

### From Source

```bash
git clone https://github.com/yegorferrieres/ccd-ai.git
cd ccd-ai/tools/ccd-cli
pip install -e .
```

## Publishing to PyPI

### Building the Package

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# This creates dist/ directory with wheel and source distribution
```

### Publishing to TestPyPI

```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ ccd-cli
```

### Publishing to PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Verify installation
pip install ccd-cli
```

### Development Installation

```bash
git clone https://github.com/yegorferrieres/ccd-ai.git
cd ccd-ai/tools/ccd-cli
pip install -e ".[dev]"
```

### Verify Installation

```bash
ccd --help
```

## Quick Start

### 1. Install CCD for AI CLI

```bash
git clone https://github.com/yegorferrieres/ccd-ai.git
cd ccd-ai/tools/ccd-cli
pip install -e .
```

### 2. Initialize a New CCD for AI Project

```bash
ccd init --project-name "My Project" --domain "web-application"
```

### 3. Prepare Context for AI

```bash
# Generate complete project context for AI developer
ccd prepare-context

# Generate to specific file
ccd prepare-context --output my-task-context.txt
```

### Generate Context Cards

```bash
ccd generate-cards --files "src/**/*.py" --output docs/context-cards/
```

### Validate Context

```bash
ccd validate-contexts --contexts docs/ --schemas docs/schemas/
```

### Check Health

```bash
ccd health --detailed
```

### Work with AI-CONTEXT Comments

```bash
# Add context comments to source files
ccd add-context-comments --file "src/main.go" --context "docs/contexts/files/src/main.go.ctx.md"

# Extract existing context comments
ccd extract-context --file "src/main.go"

# Validate comment format
ccd validate-context-comments --file "src/main.go"

# Update context comments
ccd update-context-comments --file "src/main.go" --context "docs/contexts/files/src/main.go.ctx.md"

# Check context freshness
ccd context-freshness --file "src/main.go"
```

## Commands

### `ccd init`

Initialize a new CCD for AI project.

```bash
ccd init --project-name "Project Name" --domain "web-application" --output-dir "./my-project"
```

**Options:**
- `--project-name, -n`: Project name (required)
- `--domain, -d`: Project domain (required)
- `--yes, -y`: Skip prompts and use defaults
- `--output-dir, -o`: Output directory (default: current directory)

**Supported Domains:**
- `web-application`
- `mobile-app`
- `api-service`
- `library`
- `cli-tool`
- `data-pipeline`
- `ml-ai`
- `infrastructure`
- `other`

### `ccd add-context-comments`

Add AI-CONTEXT comments to source code files.

```bash
ccd add-context-comments --file "src/main.go" --context "docs/contexts/files/src/main.go.ctx.md"
```

**Options:**
- `--file, -f`: Source file path (required)
- `--context, -c`: Context card file path (required)
- `--force, -F`: Overwrite existing comments
- `--dry-run`: Show what would be added without making changes

### `ccd extract-context`

Extract AI-CONTEXT comments from source code files.

```bash
ccd extract-context --file "src/main.go"
ccd extract-context --files "src/**/*.go"
ccd extract-context --project .
```

**Options:**
- `--file, -f`: Single file path
- `--files, -F`: Glob pattern for multiple files
- `--project, -p`: Extract from entire project
- `--output, -o`: Output file for extracted comments

### `ccd validate-context-comments`

Validate AI-CONTEXT comment format and content.

```bash
ccd validate-context-comments --file "src/main.go"
ccd validate-context-comments --files "src/**/*.go"
ccd validate-context-comments --project .
```

**Options:**
- `--file, -f`: Single file path
- `--files, -F`: Glob pattern for multiple files
- `--project, -p`: Validate entire project
- `--strict`: Fail on any validation errors
- `--report`: Generate detailed validation report

### `ccd update-context-comments`

Update AI-CONTEXT comments with new information.

```bash
ccd update-context-comments --file "src/main.go" --context "docs/contexts/files/src/main.go.ctx.md"
ccd update-context-comments --project . --refresh-timestamps
```

**Options:**
- `--file, -f`: Source file path
- `--context, -c`: Context card file path
- `--project, -p`: Update entire project
- `--refresh-timestamps`: Update all timestamps
- `--dry-run`: Show what would be updated

### `ccd context-freshness`

Check context freshness and health across the project.

```bash
ccd context-freshness --file "src/main.go"
ccd context-freshness --project .
ccd context-freshness --project . --report --output freshness-report.json
```

**Options:**
- `--file, -f`: Single file path
- `--project, -p`: Check entire project
- `--report`: Generate detailed report
- `--output, -o`: Output file for report
- `--threshold`: Set freshness threshold (default: 24h)

### `ccd context-health`

Check context health across the project.

```bash
ccd context-health --file "src/main.go"
ccd context-health --project . --detailed
```

**Options:**
- `--file, -f`: Single file path
- `--project, -p`: Check entire project
- `--detailed`: Show detailed health information

### `ccd drift-detection`

Detect context drift in the project.

```bash
ccd drift-detection --project .
ccd drift-detection --project . --output drift-report.json
```

**Options:**
- `--project, -p`: Check entire project
- `--output, -o`: Output file for drift report

### `ccd quality-gates`

Run all quality gates for the project.

```bash
ccd quality-gates --project .
ccd quality-gates --project . --output quality-report.json
```

**Options:**
- `--project, -p`: Check entire project
- `--output, -o`: Output file for quality report

### `ccd update-engineering-log`

Update ENGINEERING_LOG.md with a new entry.

```bash
ccd update-engineering-log --description "Implemented new feature" --impact "Medium"
```

**Options:**
- `--log-file, -l`: Path to ENGINEERING_LOG.md file (default: ./docs/ENGINEERING_LOG.md)
- `--description, -d`: Description of the development task (required)
- `--impact, -i`: Impact scope (High/Medium/Low, default: Medium)
- `--severity, -s`: Severity (High/Medium/Low, default: Medium)
- `--technical-changes, -t`: Description of technical changes made
- `--resolution, -r`: How the task was resolved
- `--lessons-learned`: Key insights gained from the task
- `--follow-up`: Next steps or follow-up actions

### `ccd update-roadmap`

Update roadmap.md to mark milestones as completed or in progress.

```bash
ccd update-roadmap --milestone "API integration" --status "completed"
```

**Options:**
- `--roadmap-file, -r`: Path to roadmap.md file (default: ./docs/roadmap.md)
- `--milestone, -m`: Milestone to update (required)
- `--status, -s`: New status (completed/in_progress, default: completed)
- `--notes, -n`: Additional notes about the milestone

### `ccd create-adr`

Create a new Architecture Decision Record (ADR).

```bash
ccd create-adr --title "Database Schema Changes" --status "Proposed"
```

**Options:**
- `--decisions-dir, -d`: Path to decisions directory (default: ./docs/decisions)
- `--title, -t`: Title of the ADR (required)
- `--status, -s`: Status (Proposed/Accepted/Deprecated/Superseded, default: Proposed)
- `--context, -c`: Context and forces at play
- `--decision`: The decision made
- `--consequences`: Consequences of the decision

### `ccd update-development-rules`

Update DEVELOPMENT_RULES.md with new workflow patterns.

```bash
ccd update-development-rules --new-rule "Feature Flag Pattern" --context "When implementing feature flags"
```

**Options:**
- `--rules-file, -r`: Path to DEVELOPMENT_RULES.md file (default: ./docs/DEVELOPMENT_RULES.md)
- `--new-rule, -n`: Name of the new workflow pattern (required)

### `ccd prepare-context`

Prepare complete project context for AI developer.

```bash
ccd prepare-context
ccd prepare-context --output my-task-context.txt
ccd prepare-context --no-architecture
ccd prepare-context --dry-run
```

**Options:**
- `--project-dir, -p`: Project directory to analyze (default: current directory)
- `--output, -o`: Output file for context (default: task-context-YYYYMMDD-HHMMSS.txt)
- `--no-architecture`: Skip architecture decisions and codemap
- `--dry-run`: Show what would be generated without creating file

### `ccd methodology-status`

Show status of all methodological files in the project.

```bash
ccd methodology-status --project-dir .
```

**Options:**
- `--project-dir, -p`: Project directory to analyze (default: current directory)

### `ccd validate`

Validate CCD schemas and contexts.

```bash
ccd validate-schemas --schemas ./docs/schemas
ccd validate-contexts --contexts ./docs --schemas ./docs/schemas
```

**Options:**
- `--schemas, -s`: Path to schemas directory
- `--contexts, -c`: Path to contexts directory
- `--output-format, -f`: Output format (text, json, yaml)
- `--detailed, -d`: Show detailed validation results

### `ccd generate`

Generate CCD documentation files.

```bash
ccd generate-cards --files "src/**/*.py" --output docs/context-cards/
ccd generate-index --modules "services/*" --output docs/modules/
ccd update-codemap --output docs/CODEMAP.yaml
```

**Options:**
- `--files, -f`: File pattern to process
- `--output, -o`: Output directory
- `--type, -t`: What to generate (cards, index, codemap)
- `--force`: Overwrite existing files

### `ccd health`

Check CCD project health.

```bash
ccd health --detailed --output-format json
```

**Options:**
- `--detailed, -d`: Show detailed health information
- `--output-format, -f`: Output format (text, json, yaml)

### `ccd coverage`

Show CCD coverage statistics.

```bash
ccd coverage --modules --files --min-coverage 80
```

**Options:**
- `--modules, -m`: Show module coverage
- `--files, -f`: Show file coverage
- `--min-coverage`: Minimum coverage percentage
- `--output-format, -o`: Output format (text, json, yaml)

### `ccd freshness`

Check CCD documentation freshness.

```bash
ccd freshness --days 30 --output-format yaml
```

**Options:**
- `--days, -d`: Number of days to check
- `--output-format, -o`: Output format (text, json, yaml)

### `ccd pack`

Package CCD contexts into archive.

```bash
ccd pack --output ./ccd-contexts.zip --include-schemas --include-templates
```

**Options:**
- `--output, -o`: Output archive path
- `--include-schemas`: Include JSON schemas
- `--include-templates`: Include templates

### `ccd monitor`

Monitor CCD project status.

```bash
ccd monitor --watch --interval 60
```

**Options:**
- `--watch, -w`: Watch for file changes
- `--interval, -i`: Check interval in seconds
- `--output-format, -o`: Output format (text, json, yaml)

### `ccd version`

Show CCD CLI version.

```bash
ccd version
```

## Configuration

### Environment Variables

- `CCD_CONFIG_PATH`: Path to configuration file
- `CCD_VERBOSE`: Enable verbose output
- `CCD_QUIET`: Suppress output

### Configuration File

Create a `ccd.config.yaml` file in your project root:

```yaml
# CCD Configuration
project:
  name: "My Project"
  domain: "web-application"
  schemas_path: "./docs/schemas"
  contexts_path: "./docs"

generation:
  auto_update: true
  include_tests: false
  include_docs: true

validation:
  strict_mode: true
  fail_fast: false

output:
  default_format: "text"
  colors: true
  progress_bars: true
```

## Examples

### Complete Workflow

```bash
# 1. Initialize project
ccd init --project-name "My API Service" --domain "api-service"

# 2. Generate context cards for all Python files
ccd generate-cards --files "src/**/*.py" --output docs/context-cards/

# 3. Generate module indexes
ccd generate-index --modules "src/*" --output docs/modules/

# 4. Update CODEMAP
ccd update-codemap --output docs/CODEMAP.yaml

# 5. Validate everything
ccd validate-contexts --contexts docs/ --schemas docs/schemas/

# 6. Check health
ccd health --detailed

# 7. Package for distribution
ccd pack --output ./ccd-contexts.zip --include-schemas
```

### AI-CONTEXT Integration

```bash
# Add AI-CONTEXT comments to source files
ccd add-context-comments --file src/main.py --context docs/contexts/files/src/main.py.ctx.md

# Extract and validate AI-CONTEXT comments
ccd extract-context --file src/main.py
ccd validate-context-comments --file src/main.py --report

# Check context freshness and health
ccd context-freshness --project . --threshold 48
ccd context-health --project . --detailed
```

### Methodology Loop Management

```bash
# Update engineering log after completing a task
ccd update-engineering-log \
  --description "Implemented user authentication" \
  --impact "High" \
  --technical-changes "Added JWT middleware and user model" \
  --resolution "Successfully deployed to staging"

# Mark roadmap milestone as completed
ccd update-roadmap --milestone "User Authentication" --status "completed"

# Create ADR for architectural decision
ccd create-adr \
  --title "JWT vs Session-based Authentication" \
  --status "Accepted" \
  --decision "We will use JWT for stateless authentication"

# Check overall methodology status
ccd methodology-status --project-dir .
```

### Quality Assurance

```bash
# Run all quality gates
ccd quality-gates --project . --output quality-report.json

# Detect context drift
ccd drift-detection --project . --output drift-report.json

# Monitor specific quality metrics
ccd context-freshness --project . --threshold 24
ccd context-health --project . --detailed
```

### CI/CD Integration

```yaml
# .github/workflows/ccd-validation.yml
name: CCD Validation

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  validate-ccd:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          
      - name: Install CCD CLI
        run: |
          git clone https://github.com/yegorferrieres/ccd-ai.git
          cd ccd-ai/tools/ccd-cli
          pip install -e .
        
      - name: Validate CCD Contexts
        run: ccd validate-contexts --contexts docs/ --schemas docs/schemas/
        
      - name: Check Health
        run: ccd health --output-format json > health-report.json
        
      - name: Upload Health Report
        uses: actions/upload-artifact@v3
        with:
          name: ccd-health-report
          path: health-report.json
```

### Automated Monitoring

```bash
# Watch for changes and auto-update
ccd monitor --watch --interval 30

# Check freshness every day
ccd freshness --days 1 --output-format json > freshness-report.json

# Generate coverage report
ccd coverage --modules --files --min-coverage 90 --output-format yaml > coverage-report.yaml
```

## Output Formats

### Text (Default)

Human-readable output with colors and formatting.

### JSON

Machine-readable output for automation and integration.

```json
{
  "status": "success",
  "data": {
    "coverage_percentage": 85.5,
    "total_modules": 12,
    "total_files": 156,
    "health_score": 78.2
  }
}
```

### YAML

Human-readable structured output.

```yaml
status: success
data:
  coverage_percentage: 85.5
  total_modules: 12
  total_files: 156
  health_score: 78.2
```

## Error Handling

The CLI provides clear error messages and exit codes:

- `0`: Success
- `1`: General error
- `130`: User interruption (Ctrl+C)

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure you're using the right Python environment
python -m pip install --upgrade ccd-cli
```

**Permission Errors**
```bash
# Use user installation
pip install --user ccd-cli
```

**Schema Validation Failures**
```bash
# Check schema files exist and are valid JSON
ccd validate-schemas --schemas ./docs/schemas --verbose
```

### Debug Mode

Enable verbose output for debugging:

```bash
ccd --verbose health --detailed
```

## Development

### Setup Development Environment

```bash
git clone https://github.com/yegorferrieres/ccd-ai.git
cd ccd-ai
pip install -e "tools/ccd-cli/.[dev]"
```

### Run Tests

```bash
pytest
pytest --cov=ccd_cli --cov-report=html
```

### Code Quality

```bash
# Format code
black ccd_cli/

# Sort imports
isort ccd_cli/

# Lint code
flake8 ccd_cli/

# Type checking
mypy ccd_cli/
```

### Pre-commit Hooks

```bash
pre-commit install
pre-commit run --all-files
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [https://github.com/yegorferrieres/ccd-ai](https://github.com/yegorferrieres/ccd-ai)
- **Issues**: [GitHub Issues](https://github.com/yegorferrieres/ccd-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yegorferrieres/ccd-ai/discussions)
- **Email**: yegor@martlive.ai

## Related Projects

- [CCD Methodology](https://github.com/yegorferrieres/ccd-ai) - Core CCD methodology
- [CCD Website](https://github.com/yegorferrieres/ccd-ai) - Documentation website
- [CCD Examples](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/examples) - Implementation examples
