# Quick Start Guide for ccd-cli

## 🚀 Install ccd-cli

```bash
pip install ccd-cli
```

## ✅ Verify Installation

```bash
ccd --help
```

You should see the CCD CLI banner and available commands.

## 🎯 Quick Examples

### 1. Initialize a New CCD Project

```bash
# Create a new CCD project
ccd init --project-name "My Awesome Project" --domain "web-application"

# This creates the basic CCD structure in your current directory
```

### 2. Generate Context Cards

```bash
# Generate context cards for all Python files
ccd generate-cards --file-types py

# Generate for specific directories
ccd generate-cards --paths src/,libs/

# Generate for specific file patterns
ccd generate-cards --files "src/**/*.py"
```

### 3. Check Project Health

```bash
# Basic health check
ccd health

# Detailed health report
ccd health --detailed

# Check context coverage
ccd coverage
```

### 4. Validate Context

```bash
# Validate all contexts
ccd validate

# Validate specific context files
ccd validate-contexts --contexts docs/contexts/
```

### 5. Work with AI-CONTEXT Comments

```bash
# Add context comments to source files
ccd add-context-comments --file "src/main.py" --context "docs/contexts/files/src/main.py.ctx.md"

# Extract existing context comments
ccd extract-context --file "src/main.py"

# Validate comment format
ccd validate-context-comments --file "src/main.py"
```

### 6. Methodology Loop Management

```bash
# Update engineering log
ccd update-engineering-log --description "Implemented new feature" --impact "High"

# Check methodology status
ccd methodology-status

# Create architecture decision record
ccd create-adr --title "Database Schema Changes" --status "Proposed"
```

### 7. Quality Gates

```bash
# Run all quality gates
ccd quality-gates

# Check context freshness
ccd context-freshness

# Detect context drift
ccd drift-detection
```

## 📁 Project Structure After Initialization

```
your-project/
├── docs/
│   ├── contexts/
│   │   ├── files/
│   │   ├── modules/
│   │   └── repository/
│   ├── schemas/
│   ├── ENGINEERING_LOG.md
│   ├── roadmap.md
│   ├── DEVELOPMENT_RULES.md
│   └── decisions/
├── .ccd/
│   └── config.yaml
└── README.md
```

## 🔧 Configuration

The CLI automatically creates a `.ccd/config.yaml` file with default settings. You can customize:

- File patterns to include/exclude
- Output directories
- Validation rules
- Quality gate thresholds

## 📚 Learn More

- **Full Documentation**: Check the main README.md
- **Examples**: See the `examples/` directory
- **GitHub**: https://github.com/yegorferrieres/ccd-ai
- **Issues**: Report bugs or request features

## 🆘 Need Help?

```bash
# Get help for any command
ccd <command> --help

# List all available commands
ccd --help

# Check version
ccd version
```

## 🎉 Congratulations!

You're now ready to use CCD (Continuous Context Documentation) to maintain comprehensive project context for AI tools and team collaboration!
