# CCD for AI Methodology Loop Guide

## Overview

The CCD Methodology Loop is a continuous process that keeps project planning, decisions, and progress synchronized with development activities. This guide explains how to use the loop effectively to ensure AI tools and team members always have access to current project context.

## Quick Start

### 1. Before Starting Development

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

### 2. During Development

- Follow patterns from recent ENGINEERING_LOG.md entries
- Reference ADRs for architectural decisions
- Note any workflow improvements for DEVELOPMENT_RULES.md updates

### 3. After Completing Development (Within 2h)

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

## Methodological Files

### roadmap.md
**Purpose**: Track project milestones, progress, and timelines
**Update**: After each development iteration
**AI Usage**: AI tools read this for current project state and next steps

**Example Update**:
```markdown
- [x] **Month 1**: Complete methodology documentation 
- [x] **Month 1**: Integrate methodological files into CCD loop 
- [ ] **Month 2**: Basic CLI tool development
```

### ENGINEERING_LOG.md
**Purpose**: Document technical decisions, incidents, and lessons learned
**Update**: Within 2h of completing any development task
**AI Usage**: AI tools use this for recent patterns and technical context

**Example Entry**:
```markdown
## 2025-08-28 - [Task Description]

### Description
Brief description of what was accomplished...

### Impact
- Scope: [High/Medium/Low]
- Severity: [High/Medium/Low]
- User Impact: [Description]
- Business Impact: [Description]

### Technical Changes
- [Specific changes made]

### Resolution
- [How the task was completed]

### Lessons Learned
- [Key insights gained]

### Follow-up Actions
- [ ] [Next step 1]
- [ ] [Next step 2]
```

### decisions/
**Purpose**: Document and track important architectural decisions
**Update**: Within 24h of making architectural decisions
**AI Usage**: AI tools reference these for architectural context and consistency

**Example ADR Structure**:
```markdown
# [ADR-XXX] [Brief Title]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
[Forces and constraints]

## Decision
[Chosen approach]

## Consequences
[Positive, negative, and neutral impacts]

## Alternatives Considered
[Other options evaluated]
```

### DEVELOPMENT_RULES.md
**Purpose**: Define development workflow and best practices
**Update**: When workflow improvements are identified
**AI Usage**: AI tools follow these for consistent development practices

**Example Update**:
```markdown
## New Workflow Pattern

### Context
[When to use this pattern]

### Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Validation
- [ ] [Validation requirement 1]
- [ ] [Validation requirement 2]
```

## Quality Gates

### Timing Requirements
- **Methodological files**: Updated within 2h of development completion
- **AI context**: Updated within 1h of methodological file updates
- **Validation**: AI context validation within 30min of update

### Compliance Requirements
- **Methodological files**: 100% compliance with update requirements
- **AI context**: 100% synchronization with methodological files
- **AI integration**: 100% successful context access and usage

## Common Patterns

### Daily Development Workflow
1. **Morning**: Read roadmap.md and recent ENGINEERING_LOG.md entries
2. **During**: Follow DEVELOPMENT_RULES.md and reference decisions/
3. **Evening**: Update ENGINEERING_LOG.md and roadmap.md

### Automated Methodological Updates
```bash
# Update engineering log after completing a task
ccd update-engineering-log --description "Implemented feature" --impact "Medium"

# Mark roadmap milestone as completed
ccd update-roadmap --milestone "API integration" --status "completed"

# Create ADR for architectural decision
ccd create-adr --title "Database Schema Changes" --status "Proposed"

# Check overall methodology status
ccd methodology-status --project-dir .
```

### Weekly Review
1. **Monday**: Review roadmap.md for weekly goals
2. **Wednesday**: Mid-week progress check and timeline adjustments
3. **Friday**: Weekly retrospective and ENGINEERING_LOG.md updates

### Milestone Completion
1. **Complete**: Mark milestone as done in roadmap.md
2. **Document**: Add detailed entry to ENGINEERING_LOG.md
3. **Plan**: Update roadmap.md with next milestones
4. **Validate**: Ensure all methodological files are current

## Troubleshooting

### Common Issues

**Issue**: Methodological files are outdated
**Solution**: Update all files within 2h of development completion

**Issue**: AI tools can't access current context
**Solution**: Verify methodological files are updated and AI context is synchronized

**Issue**: Workflow rules are unclear
**Solution**: Update DEVELOPMENT_RULES.md with clear, actionable guidance

**Issue**: Architectural decisions aren't documented
**Solution**: Create ADR within 24h of making architectural decisions

### Validation Checklist

Before considering development complete:
- [ ] ENGINEERING_LOG.md updated with new entry
- [ ] roadmap.md reflects current progress accurately
- [ ] New ADRs created for architectural decisions (if any)
- [ ] DEVELOPMENT_RULES.md updated if workflow improved
- [ ] All methodological files pass validation
- [ ] AI context updated and synchronized

## Integration with CCD Protocol

The Methodology Loop integrates with the main CCD Protocol:

1. **Steps 1-4**: Standard context update workflow
2. **Step 5**: Update methodological files (NEW)
3. **Step 6**: AI context integration (NEW)

This ensures that both code context and methodology context are kept synchronized and accessible to AI tools.

## Best Practices

1. **Be Consistent**: Update files in the same order every time
2. **Be Timely**: Respect the 2h SLA for development tasks
3. **Be Complete**: Include all required sections in updates
4. **Be Honest**: Document both successes and failures
5. **Be Forward-Looking**: Always include next steps and follow-up actions

## Resources

- **CCD Protocol**: [docs/03-protocol.md](03-protocol.md)
- **Development Rules**: [docs/DEVELOPMENT_RULES.md](DEVELOPMENT_RULES.md)
- **Engineering Log**: [docs/ENGINEERING_LOG.md](ENGINEERING_LOG.md)
- **Roadmap**: [docs/roadmap.md](roadmap.md)
- **Decisions**: [docs/decisions/](decisions/)
- **Templates**: [docs/templates/](templates/)
- **CCD CLI**: [tools/ccd-cli/README.md](../tools/ccd-cli/README.md) - Command-line interface for CCD methodology
- **CCD CLI Examples**: [tools/ccd-cli/examples](../tools/ccd-cli/examples) - Usage examples and demonstrations

---

**Last Updated**: 2025-08-28  
**Version**: 1.0.0  
**Status**: Active Guide
