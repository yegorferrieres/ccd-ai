# CCD for AI (Continuous Context Documentation for AI) Development Workflow

## Overview

This document provides a detailed workflow for developers working with CCD methodology. It covers the complete development cycle from initial context reading to final context updates, ensuring that context documentation remains current and valuable.

## Development Workflow Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Before Dev    │    │  During Dev     │    │   After Dev     │
│                 │    │                 │    │                 │
│ • Read Context  │───▶│ • Reference     │───▶│ • Update        │
│ • Understand    │    │   Patterns      │    │   Context       │
│ • Plan Changes  │    │ • Follow Rules  │    │ • Validate      │
│                 │    │ • Document      │    │ • Commit        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Phase 1: Before Development

### 1.1 Context Discovery

#### Read Project Context
```bash
# Read high-level project context
cat docs/project-context.md

# Check module dependencies
cat docs/codemap.yaml

# Review related context cards
ls docs/examples/*/*.ctx.md
```

#### Read AI-CONTEXT Comments
```bash
# Extract AI-CONTEXT comments from source files
ccd extract-context --file src/main.go

# Check context freshness across project
ccd context-freshness --project .

# Validate AI-CONTEXT comment format
ccd validate-context-comments --file src/main.go

# Prepare complete project context for AI developer
ccd prepare-context --project-dir . --output task-context.txt
```

#### Understand Module Context
```bash
# Read high-level project context
cat docs/project-context.md

# Check module dependencies
cat docs/codemap.yaml

# Review related context cards
ls docs/examples/*/*.ctx.md
```

#### Understand Module Context
```bash
# Read module-specific context
cat docs/index/module-name.yaml

# Check module dependencies
ccd dependencies --module "module-name"

# Review module files
ccd files --module "module-name"
```

#### Identify Related Context
```bash
# Find related context files
ccd search --query "user authentication" --files

# Check cross-references
ccd references --file "src/auth/user.ts"

# Review similar implementations
ccd similar --file "src/auth/user.ts"
```

### 1.2 Context Analysis

#### Assess Context Quality
```bash
# Check context health
ccd health --module "module-name"

# Validate context quality
ccd validate --contexts docs/examples/module-name/

# Check coverage
ccd coverage --module "module-name"
```

#### Identify Context Gaps
```bash
# Find missing context
ccd gaps --module "module-name"

# Check outdated context
ccd stale --module "module-name"

# Identify incomplete context
ccd incomplete --module "module-name"
```

#### Plan Context Updates
- **Required Updates**: Context that must be updated for current changes
- **Optional Updates**: Context that could benefit from updates
- **New Context**: Context that needs to be created
- **Update Priority**: Order and importance of updates

### 1.3 Development Planning

#### Context-First Planning
1. **Understand Current State**: What exists and what's missing
2. **Identify Dependencies**: What context is needed for development
3. **Plan Context Updates**: When and how to update context
4. **Set Quality Targets**: What quality level to achieve

#### Risk Assessment
- **Context Quality**: Is existing context sufficient?
- **Dependency Clarity**: Are dependencies well documented?
- **Pattern Consistency**: Are patterns consistent and clear?
- **Update Complexity**: How complex are required updates?

## Phase 2: During Development

### 2.1 Context Reference

#### Follow Established Patterns
```bash
# Reference similar implementations
ccd similar --file "src/auth/user.ts"

# Check pattern consistency
ccd patterns --module "auth"

# Review best practices
ccd best-practices --domain "authentication"
```

#### Use Context for Decisions
1. **Architecture Decisions**: Reference existing architectural patterns
2. **Implementation Choices**: Follow established implementation patterns
3. **Dependency Management**: Use documented dependency patterns
4. **Error Handling**: Follow established error handling patterns

#### Document Context Usage
```bash
# Log context references
ccd log-reference --file "src/auth/user.ts" --context "user-auth-pattern"

# Track context usage
ccd track-usage --context "user-auth-pattern"
```

### 2.2 Context Maintenance

#### Update Context Incrementally
```bash
# Update context as you work
ccd update-context --file "src/auth/user.ts" --changes "Added user validation"

# Mark context for review
ccd mark-review --file "src/auth/user.ts"
```

#### Follow Context Rules
1. **Context First**: Always read context before making changes
2. **Avoid Duplication**: Don't duplicate existing functionality
3. **Maintain Currency**: Keep context updated with changes
4. **Follow Patterns**: Use established patterns and conventions

#### Quality Assurance
```bash
# Validate context changes
ccd validate --file "src/auth/user.ts"

# Check context quality
ccd quality --file "src/auth/user.ts"

# Verify cross-references
ccd verify-refs --file "src/auth/user.ts"
```

### 2.3 Context Documentation

#### Document Changes
```bash
# Document implementation decisions
ccd log-decision --file "src/auth/user.ts" --decision "Use bcrypt for password hashing"

# Update context with changes
ccd update-context --file "src/auth/user.ts" --changes "Implemented password hashing with bcrypt"

# Add implementation notes
ccd add-note --file "src/auth/user.ts" --note "Follows OWASP password guidelines"
```

#### Maintain Consistency
1. **Format Consistency**: Follow established context formats
2. **Content Consistency**: Maintain consistent content structure
3. **Reference Consistency**: Keep cross-references accurate
4. **Style Consistency**: Follow established writing style

## Phase 3: After Development

### 3.1 Context Update

#### Update Context Files
```bash
# Generate updated context cards
ccd generate-cards --file "src/auth/user.ts" --force

# Update module index
ccd update-index --module "auth"

# Update repository codemap if needed
ccd update-codemap --check

# Prepare complete project context for AI developer
ccd prepare-context --project-dir . --output task-context.txt
```

#### Update AI-CONTEXT Comments
```bash
# Update AI-CONTEXT comments in source files
ccd update-context-comments --file "src/auth/user.ts" --context docs/contexts/files/src/auth/user.ts.ctx.md

# Validate comment format
ccd validate-context-comments --file "src/auth/user.ts"

# Check comment freshness
ccd context-freshness --file "src/auth/user.ts"
```

#### Validate Context Updates
```bash
# Validate all context changes
ccd validate --contexts docs/examples/auth/

# Check context quality
ccd quality --module "auth"

# Verify cross-references
ccd verify-refs --module "auth"
```

#### Quality Gates
1. **Schema Compliance**: All context files pass schema validation
2. **Content Quality**: Content meets quality standards
3. **Coverage**: All changes are documented
4. **Cross-References**: All links are valid

### 3.2 Context Synchronization

#### Update Related Context
```bash
# Update dependent context
ccd update-dependents --file "src/auth/user.ts"

# Update cross-references
ccd update-refs --file "src/auth/user.ts"

# Update module dependencies
ccd update-dependencies --module "auth"
```

#### Synchronize Metadata
```bash
# Update file metadata
ccd update-metadata --file "src/auth/user.ts"

# Update timestamps
ccd update-timestamps --file "src/auth/user.ts"

# Update change logs
ccd update-changelog --file "src/auth/user.ts"
```

### 3.3 Context Validation

#### Comprehensive Validation
```bash
# Run full validation
ccd validate-all --module "auth"

# Check context health
ccd health --module "auth"

# Generate validation report
ccd validate-report --module "auth" --output auth-validation.json
```

#### Quality Assurance
1. **Content Review**: Review context content for accuracy
2. **Format Review**: Ensure proper formatting and structure
3. **Reference Review**: Verify all cross-references
4. **Coverage Review**: Ensure comprehensive coverage

## Quality Gates & Validation

### 3.4 Pre-Commit Validation

#### Mandatory Checks
```bash
# Schema validation
ccd validate-schemas --file "src/auth/user.ts"

# Content validation
ccd validate-content --file "src/auth/user.ts"

# Cross-reference validation
ccd validate-refs --file "src/auth/user.ts"

# Coverage validation
ccd validate-coverage --module "auth"
```

#### Quality Thresholds
- **Schema Compliance**: 100% (mandatory)
- **Content Quality**: ≥85% (warning if <85%)
- **Cross-Reference Accuracy**: 100% (mandatory)
- **Coverage**: ≥90% (warning if <90%)

### 3.5 Context Health Check

#### Health Metrics
```bash
# Check overall health
ccd health --module "auth"

# Generate health report
ccd health-report --module "auth" --output auth-health.json

# Check health trends
ccd health-trends --module "auth" --days 30
```

#### Health Indicators
- **Context Freshness**: ≤24h since last update
- **Context Quality**: ≥85/100 health score
- **Context Coverage**: ≥90% of files documented
- **Cross-Reference Health**: 100% valid references

## Workflow Automation

### 3.6 CI/CD Integration

#### Automated Validation
```yaml
# GitHub Actions workflow
- name: Validate Context
  run: ccd validate-all --module ${{ matrix.module }}
  
- name: Check Context Health
  run: ccd health --module ${{ matrix.module }}
  
- name: Generate Context Report
  run: ccd validate-report --module ${{ matrix.module }}
```

#### Quality Gates
```yaml
# Quality gate configuration
- name: Quality Gate Check
  run: |
    if ! ccd quality-gate --module ${{ matrix.module }}; then
      echo "Quality gates failed"
      exit 1
    fi
```

### 3.7 Automated Context Updates

#### Context Generation
```yaml
# Automated context generation
- name: Generate Context
  run: ccd generate-cards --file-types ${{ matrix.file-types }}
  
- name: Update Indexes
  run: ccd update-indexes --modules all
  
- name: Update CODEMAP
  run: ccd update-codemap --force
```

#### Validation Pipeline
```yaml
# Validation pipeline
- name: Validate Generated Context
  run: ccd validate-all --contexts docs/
  
- name: Check Quality Gates
  run: ccd quality-gates --strict
  
- name: Generate Health Report
  run: ccd health-report --output health-report.json
```

## Best Practices

### 3.8 Context Management

#### Keep Context Current
1. **Update Frequently**: Update context with every significant change
2. **Validate Regularly**: Run validation checks regularly
3. **Monitor Health**: Monitor context health continuously
4. **Address Issues**: Fix context issues promptly

#### Maintain Quality
1. **Follow Standards**: Adhere to established context standards
2. **Review Content**: Regularly review context content
3. **Optimize Structure**: Continuously optimize context structure
4. **Measure Effectiveness**: Track context effectiveness metrics

### 3.9 Team Collaboration

#### Coordinate Updates
1. **Communicate Changes**: Inform team of context changes
2. **Coordinate Updates**: Coordinate updates across modules
3. **Share Knowledge**: Share context knowledge and insights
4. **Train Team**: Train team on context best practices

#### Continuous Improvement
1. **Gather Feedback**: Collect feedback on context quality
2. **Identify Improvements**: Identify areas for improvement
3. **Implement Changes**: Implement improvement changes
4. **Measure Impact**: Measure impact of improvements

## Troubleshooting

### 3.10 Common Issues

#### Context Generation Failures
```bash
# Check file accessibility
ls -la src/auth/user.ts

# Verify CCD CLI installation
ccd --version

# Check error logs
ccd generate-cards --file "src/auth/user.ts" --verbose
```

#### Validation Failures
```bash
# Check schema compliance
ccd validate-schemas --file "src/auth/user.ts"

# Review content quality
ccd validate-content --file "src/auth/user.ts" --detailed

# Fix cross-reference issues
ccd fix-refs --file "src/auth/user.ts"

# Run quality gates
ccd quality-gates --project . --output quality-report.json

# Check context health
ccd context-health --project . --detailed

# Detect context drift
ccd drift-detection --project . --output drift-report.json
```

#### Performance Issues
```bash
# Check context size
ccd size --file "src/auth/user.ts"

# Optimize context structure
ccd optimize --file "src/auth/user.ts"

# Monitor performance
ccd performance --module "auth"
```

#### AI-CONTEXT Issues
```bash
# Validate AI-CONTEXT comments
ccd validate-context-comments --file "src/auth/user.ts" --report

# Check context freshness
ccd context-freshness --file "src/auth/user.ts" --threshold 24

# Extract AI-CONTEXT comments
ccd extract-context --file "src/auth/user.ts"
```

### 3.11 Escalation

#### When to Escalate
1. **Persistent Failures**: Context generation consistently fails
2. **Quality Issues**: Context quality below acceptable thresholds
3. **Performance Problems**: Significant performance degradation
4. **Team Blockers**: Context issues blocking team progress

#### Escalation Process
1. **Document Issue**: Document the issue and impact
2. **Attempt Resolution**: Try to resolve the issue
3. **Escalate to Lead**: Escalate to context maintainer
4. **Follow Up**: Follow up on resolution progress

## Success Metrics

### 3.12 Workflow Effectiveness

#### Developer Experience
- **Context Usage**: 90%+ of developers use context before development
- **Update Frequency**: Context updated within 24h of changes
- **Quality Satisfaction**: 4.5+ rating on context quality
- **Workflow Adherence**: 95%+ adherence to CCD workflow

#### Context Quality
- **Freshness**: 95%+ of context updated within SLA
- **Coverage**: 90%+ of modules and files documented
- **Health Score**: 85+ average context health score
- **Validation Success**: 95%+ of validation checks passing

#### Performance Metrics
- **Time-to-Context**: ≤30min average TTC
- **Update Latency**: ≤24h average update latency
- **Validation Speed**: ≤5min average validation time
- **Generation Performance**: ≤2min average generation time

---

**Next**: Read the [Context Update Process](context-update-process.md) for detailed information about updating context documentation.
