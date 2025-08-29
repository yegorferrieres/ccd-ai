# CCD for AI (Continuous Context Documentation for AI)

> **CCD for AI (Continuous Context Documentation for AI) keeps AI and humans aligned with a continuously updated project context. It operationalizes RAG for software development by adding a rigorous update loop.**

> **🚀 Production Ready**: The CLI tool is now available on PyPI! The methodology is fully functional and ready for production use.

** A comprehensive methodology for implementing RAG (Retrieval-Augmented Generation) in software development through continuous context documentation and AI-CONTEXT integration.**

** Transform your AI development workflow with structured context management and automated documentation.**



[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://github.com/yegorferrieres/ccd-ai)
[![CI Status](https://img.shields.io/badge/CI-validating%20context-green)](https://github.com/yegorferrieres/ccd-ai/actions)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](https://github.com/yegorferrieres/ccd-ai)
[![PyPI](https://img.shields.io/badge/PyPI-ccd--cli-blue)](https://pypi.org/project/ccd-cli/)


## Key Features

- ** AI-CONTEXT Integration**: Direct context access in source code
- ** Methodology Loop**: Automated project planning and decision tracking
- ** Quality Gates**: Comprehensive validation and health monitoring
- ** CLI Tools**: Command-line interface for automation
- ** Four-Tier Architecture**: Repository → Module → File → Code level context
- ** RAG Optimization**: Enhanced AI tool performance with structured context

## Quick Start

### Install ccd-cli
```bash
# Install from PyPI (Recommended)
pip install ccd-cli

# Or install from source
git clone https://github.com/yegorferrieres/ccd-ai.git
cd ccd-ai/tools/ccd-cli
pip install -e .
```

### Initialize and Use
```bash
# Initialize a new CCD project
ccd init --project-name "My Project" --domain "web-application"

# Generate context cards
ccd generate-cards --file-types go,py,js,ts

# Validate contexts
ccd validate-contexts

# Check project health
ccd health
```

**That's it!** Your AI tools now have fresh, structured context about your codebase.

## The CCD for AI Loop

```
Code Changes → Update Context → Re-index → AI Usage → Telemetry → Back to Code
     ↓              ↓           ↓         ↓         ↓
  Merge PR    Context Files  Embeddings  AI Tools  Feedback
     ↓              ↓           ↓         ↓         ↓
  Trigger     .ctx.md files  Vector DB   RAG      Metrics
     ↓              ↓           ↓         ↓         ↓
  CI/CD       Validation     Search      Results   Drift
```

## The CCD for AI Methodology Loop

```
Start Development → Read Context → Execute → Update Methodological Files → Validate → AI Context Update
       ↓              ↓           ↓              ↓                    ↓           ↓
   Roadmap.md    ENGINEERING_   Code Changes  ENGINEERING_LOG.md   Quality     AI Tools
   Decisions/    LOG.md         ADR Creation  roadmap.md           Gates      Get Fresh
   Context       Context Files  Updates       decisions/           Pass       Context
```

The CCD for AI methodology includes a continuous loop that keeps project planning, decisions, and progress synchronized with development activities. This ensures AI tools always have access to current project state, architectural decisions, and development patterns.

## Four-Tier Context Architecture

### 1. **CODEMAP.yaml** - Repository Overview
- Project metadata and module mapping
- Dependency relationships and contracts
- Technology stack and deployment info

### 2. **INDEX.yaml** - Module Mapping  
- Module purpose and I/O contracts
- File relationships and context card links
- Input/output data formats and APIs

### 3. **Context Cards (.ctx.md)** - File Documentation
- Structured metadata (language, domain, size, lines)
- Purpose, dependencies, and key components
- Cross-references and relationships

### 4. **AI-CONTEXT Comments** - Code Integration
- Direct context links in source code files
- Context freshness indicators and health scores
- Quick access to documentation from within code
- Language-specific comment formats for all programming languages

## Core Methodological Files

### **roadmap.md** - Project Planning & Progress
- Track project milestones, progress, and timelines
- Update after each development iteration
- AI tools read this for current project state and next steps

### **ENGINEERING_LOG.md** - Development History & Patterns
- Document technical decisions, incidents, and lessons learned
- Update within 2h of completing any development task
- AI tools use this for recent patterns and technical context

### **decisions/** - Architectural Decision Records (ADRs)
- Document and track important architectural decisions
- Update within 24h of making architectural decisions
- AI tools reference these for architectural context and consistency

### **DEVELOPMENT_RULES.md** - Workflow & Process Rules
- Define development workflow and best practices
- Update when workflow improvements are identified
- AI tools follow these for consistent development practices

## AI-CONTEXT Comments Integration

### **Purpose**
AI-CONTEXT comments provide direct access to context documentation from within source code, enabling developers and AI tools to quickly understand the current state and purpose of any file.

### **Format**
```go
// AI-CONTEXT: @file:contexts/files/services/edge-gateway/cmd/edge/main.go.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:95%
// AI-CONTEXT: @dependencies:router.go,middleware.go,config.go
// AI-CONTEXT: @tags:entry-point,server,initialization
```

### **Benefits**
- **Immediate Context**: Understand file purpose without leaving code editor
- **Context Freshness**: Know when context was last updated
- **Health Indicators**: Visual feedback on context quality
- **Quick Navigation**: Direct links to detailed documentation

## Key Metrics

- **Context Freshness**: ≤24h after merge
- **Retrieval Precision@K**: ≥85%
- **Context Coverage**: ≥90% of modules mapped
- **Drift MTTR**: ≤4h
- **Time-to-Context (TTC)**: ≤30min

## Tools & Automation

- **ccd-cli**: Command-line interface for context management with AI-CONTEXT integration
- **Automated Generation**: Context cards on file changes
- **AI-CONTEXT Integration**: Direct context links in source code with validation
- **Methodology Loop**: Automated management of roadmap, engineering log, and ADRs
- **Quality Gates**: Comprehensive validation including coverage, freshness, health, and drift detection
- **CI/CD Integration**: Validation and health monitoring with quality gates

## Documentation

- [Full Documentation](docs/README.md)
- [Getting Started](docs/01-overview.md)
- [Methodology Loop Guide](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/methodology-loop-guide.md)
- [Development Rules](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/DEVELOPMENT_RULES.md)
- [Engineering Log](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/ENGINEERING_LOG.md)
- [Project Roadmap](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/roadmap.md)
- [Architecture Decisions](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/decisions)
- [AI-CONTEXT Templates](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/templates/ai-context-comments.md)
- [AI-CONTEXT Examples](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/examples/ai-context-integration)
- [CCD CLI Documentation](https://github.com/yegorferrieres/ccd-ai/tree/main/tools/ccd-cli/README.md)
- [CCD CLI Examples](https://github.com/yegorferrieres/ccd-ai/tree/main/tools/ccd-cli/examples)
- [PyPI Package](https://pypi.org/project/ccd-cli/)
- [Playbooks](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/playbooks)
- [Checklists](https://github.com/yegorferrieres/ccd-ai/tree/main/docs/checklists)
- [API Reference](https://github.com/yegorferrieres/ccd-ai/tree/main/docs)

## Why CCD (Continuous Context Documentation)?

- **Always Fresh**: Context updates automatically with code changes
- **AI-Native**: Designed for RAG systems and AI tools
- **Developer-Friendly**: Minimal overhead, maximum value
- **Enterprise-Ready**: Scales from startups to large organizations
- **Open Source**: Community-driven and transparent

## Benefits of the Methodology Loop

- **Continuous Synchronization**: Project state is always current and synchronized
- **Pattern Recognition**: AI tools can learn from recent development patterns and decisions
- **Consistency**: Development follows established architectural patterns and workflow rules
- **Knowledge Preservation**: All decisions and patterns are systematically documented
- **AI Context Awareness**: AI tools always have access to current project methodology state

## Using the CCD Methodology Loop

### Before Starting Development
```bash
# Check current project state
cat docs/roadmap.md

# Review recent development patterns
tail -20 docs/ENGINEERING_LOG.md

# Understand architectural context
ls docs/decisions/*.md

# Follow established workflow
cat docs/DEVELOPMENT_RULES.md
```

### After Completing Development (Within 2h)
```bash
# Update engineering log
echo "## $(date +%Y-%m-%d) - [Task Description]" >> docs/ENGINEERING_LOG.md

# Update roadmap progress
# Edit docs/roadmap.md to mark completed items

# Create ADR if architectural decision made
# Copy template: cp docs/templates/adr-template.md docs/decisions/adr-XXX-decision.md

# Update development rules if workflow improved
# Edit docs/DEVELOPMENT_RULES.md
```

## Examples

### Basic Usage
```bash
# Verify installation
ccd --help
```

### Generate and Validate Context
```bash
# Generate context cards for all source files
ccd generate-cards --force

# Generate for specific file types
ccd generate-cards --file-types go,py,js

# Validate contexts
ccd validate

# Check project health
ccd health
```

### AI-CONTEXT Integration
```bash
# Add context comments to source files
ccd add-context-comments --file src/main.go --context docs/contexts/files/src/main.go.ctx.md

# Extract context comments from source files
ccd extract-context --file src/main.go

# Validate comment format
ccd validate-context-comments --file src/main.go
```

### Methodology Loop
```bash
# Update engineering log
ccd update-engineering-log --description "Implemented feature" --impact "Medium"

# Update roadmap milestone
ccd update-roadmap --milestone "API integration" --status "completed"

# Create architecture decision record
ccd create-adr --title "Database Schema Changes" --status "Proposed"

# Check methodology status
ccd methodology-status --project-dir .
```

### CI/CD Integration
```yaml
# .github/workflows/context-validation.yml
- name: Validate Context
  run: ccd validate-contexts --fail-on-error
  
- name: Generate Context Cards
  run: ccd generate-cards --file-types go,py,js,ts
  
- name: Health Check
  run: ccd health
```

## Quality Gates & Validation

### Timing Requirements
- **Methodological files**: Updated within 2h of development completion
- **AI context**: Updated within 1h of methodological file updates
- **Validation**: AI context validation within 30min of update

### Compliance Requirements
- **Methodological files**: 100% compliance with update requirements
- **AI context**: 100% synchronization with methodological files
- **AI integration**: 100% successful context access and usage

### Validation Checklist
Before considering development complete:
- [ ] ENGINEERING_LOG.md updated with new entry
- [ ] roadmap.md reflects current progress accurately
- [ ] New ADRs created for architectural decisions (if any)
- [ ] DEVELOPMENT_RULES.md updated if workflow improved
- [ ] All methodological files pass validation
- [ ] AI context updated and synchronized

## Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Quick Links

- ** [Documentation](docs/)**: Complete methodology guide
- ** [CCD for AI CLI](tools/ccd-cli/)**: Command-line interface
- ** [PyPI Package](https://pypi.org/project/ccd-cli/)**: Install directly from PyPI
- ** [Examples](docs/examples/)**: Real-world implementations
- ** [Research](research/)**: Academic papers and research
- ** [Website](site/)**: MkDocs documentation site

## Community & Support

- ** [Discussions](https://github.com/yegorferrieres/ccd-ai/discussions)**: Community Q&A
- ** [Issues](https://github.com/yegorferrieres/ccd-ai/issues)**: Bug reports & feature requests
- ** [Contributing](CONTRIBUTING.md)**: How to contribute
- ** [Code of Conduct](CODE_OF_CONDUCT.md)**: Community guidelines

---

**Last Updated**: 2025-08-29  
**Made with dedication by the CCD for AI (Continuous Context Documentation for AI) community**
