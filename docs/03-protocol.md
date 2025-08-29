# CCD for AI (Continuous Context Documentation for AI) Protocol

## Overview

The CCD Protocol defines the continuous loop that keeps context documentation fresh and synchronized with code changes. This document specifies the exact steps, SLAs, SLOs, and KPIs for implementing CCD in any software project.

## The CCD Loop

```
Code Changes → Update Context → Re-index → AI Usage → Telemetry → Back to Code
     ↓              ↓           ↓         ↓         ↓
  Merge PR    Context Files  Embeddings  AI Tools  Feedback
     ↓              ↓           ↓         ↓         ↓
  Trigger     .ctx.md files  Vector DB   RAG      Metrics
     ↓              ↓           ↓         ↓         ↓
  CI/CD       Validation     Search      Results   Drift
```

## The CCD Methodology Loop

```
Development Task → Read Context → Execute → Update Methodological Files → Validate → AI Context Update
       ↓              ↓           ↓              ↓                    ↓           ↓
   Roadmap.md    ENGINEERING_   Code Changes  ENGINEERING_LOG.md   Quality     AI Tools
   Decisions/    LOG.md         ADR Creation  roadmap.md           Gates      Get Fresh
   Context       Context Files  Updates       decisions/           Pass       Context
```

## The CCD Methodology Cycle

The CCD methodology includes a continuous loop that keeps project planning, decisions, and progress synchronized with development activities. This cycle ensures that AI tools and team members always have access to the current state of the project methodology.

### Methodology Loop Components

#### 1. **roadmap.md** - Project Planning and Progress
- **Purpose**: Track project milestones, progress, and timelines
- **Update Frequency**: After each development iteration
- **AI Integration**: AI tools read this file to understand current project state
- **Content**: Milestones, progress indicators, timeline adjustments, next steps

#### 2. **ENGINEERING_LOG.md** - Development History and Patterns
- **Purpose**: Document technical decisions, incidents, and lessons learned
- **Update Frequency**: Within 2h of completing any development task
- **AI Integration**: AI tools use this for context about recent changes and patterns
- **Content**: Timestamped entries with description, impact, resolution, and follow-up

#### 3. **decisions/** - Architectural Decision Records (ADRs)
- **Purpose**: Document and track important architectural decisions
- **Update Frequency**: Within 24h of making architectural decisions
- **AI Integration**: AI tools reference these for understanding system evolution
- **Content**: Decision rationale, alternatives considered, consequences, implementation notes

#### 4. **DEVELOPMENT_RULES.md** - Workflow and Process Rules
- **Purpose**: Define development workflow and best practices
- **Update Frequency**: When workflow improvements are identified
- **AI Integration**: AI tools follow these rules for consistent development practices
- **Content**: Development workflow, context update rules, quality gates

### Methodology Loop Workflow

```
Start Development → Read Methodological Context → Execute Task → Update Methodological Files → AI Context Update
       ↓                      ↓                      ↓              ↓                        ↓
   Check roadmap.md      ENGINEERING_LOG.md      Code Changes   ENGINEERING_LOG.md      AI Tools Get
   Review decisions/     Context Files          ADR Creation   roadmap.md              Fresh Context
   Follow rules         Recent Patterns         Updates         decisions/              Including
                                                                                       Methodology State
```

## Protocol Steps

### Step 1: Code Change Merged

**Trigger**: Pull request merged to main branch
**Timing**: Immediate (within 5 minutes of merge)

**Actions**:
1. CI/CD pipeline detects merge
2. Identifies changed files and modules
3. Determines scope of context updates needed

**Validation**:
- [ ] Merge event detected
- [ ] Changed files identified
- [ ] Update scope determined

### Step 2: Update Context Files

**Timing**: ≤24h after merge (SLA)
**Scope**: All affected modules and files

**Actions**:
1. **Generate Context Cards**: Create/update `.ctx.md` files for changed files
2. **Update CODEMAP.yaml**: Modify module dependencies if needed
3. **Update INDEX.yaml**: Modify module purpose/I/O if needed
4. **Validate Changes**: Run quality gates on updated context

**Context Card Requirements**:
- **Maximum Length**: 200 lines
- **Warning Threshold**: 160 lines
- **Required Sections**: Overview, Purpose, Dependencies, Key Components
- **Metadata**: File path, language, domain, size, lines, last modified

**Validation**:
- [ ] Context cards generated for all changed files
- [ ] CODEMAP.yaml updated if dependencies changed
- [ ] INDEX.yaml updated if module purpose changed
- [ ] Quality gates pass

### Step 3: Re-index Knowledge

**Timing**: ≤30min after context update (SLA)
**Scope**: All updated context files

**Actions**:
1. **Parse Context**: Extract structured data from context files
2. **Generate Embeddings**: Create vector representations for AI consumption
3. **Update Index**: Modify search index with new context
4. **Validate Index**: Ensure index integrity and completeness

**Index Requirements**:
- **Vector Dimensions**: 1536 (compatible with OpenAI embeddings)
- **Chunk Size**: 300-800 tokens per chunk
- **Metadata**: Include all context card fields
- **Cross-References**: Maintain link integrity

**Validation**:
- [ ] Context parsed successfully
- [ ] Embeddings generated for all content
- [ ] Index updated with new context
- [ ] Index validation passes

### Step 4: Validate Context Health

**Timing**: Continuous during updates
**Scope**: All context files and relationships

**Actions**:
1. **Schema Validation**: Ensure JSON schema compliance
2. **Content Validation**: Check length, required sections, metadata
3. **Coverage Validation**: Verify module mapping completeness
4. **Cross-Reference Validation**: Check link integrity

**Quality Gates**:
- **Schema Compliance**: 100% of files pass schema validation
- **Content Quality**: 95% of files pass content validation
- **Coverage**: 90% of modules have context documentation
- **Cross-References**: 100% of links are valid

**Validation**:
- [ ] All quality gates pass

### Step 5: Update Methodological Files (NEW - Core CCD Loop)

**Timing**: After each development iteration (≤2h after completion)
**Scope**: Project methodology and planning files

**Actions**:
1. **Update ENGINEERING_LOG.md**: Add new entry with timestamp, description, impact, and resolution
2. **Update roadmap.md**: Mark completed milestones, adjust timelines, update progress
3. **Update decisions/**: Create new ADR if architectural decision made, update existing ADRs
4. **Update DEVELOPMENT_RULES.md**: If workflow rules changed or improved

**Methodological File Requirements**:
- **ENGINEERING_LOG.md**: Entry within 2h of completion, include all required sections
- **roadmap.md**: Update progress indicators, adjust timelines, mark completed items
- **decisions/**: New ADR within 24h if decision made, update existing ADRs as needed
- **DEVELOPMENT_RULES.md**: Update if workflow improvements identified

**Validation**:
- [ ] ENGINEERING_LOG.md updated with new entry
- [ ] roadmap.md reflects current progress accurately
- [ ] New ADRs created for architectural decisions
- [ ] Methodological files pass validation

### Step 6: Update AI-CONTEXT Comments (NEW - Code Integration)

**Timing**: After methodological files updated (≤1h after Step 5)
**Scope**: All source code files with context documentation

**Actions**:
1. **Update AI-CONTEXT Comments**: Add/update context links in source code files
2. **Validate Comment Format**: Ensure all required fields are present
3. **Check Context Freshness**: Update timestamps and health scores
4. **Validate File Paths**: Ensure context file paths are correct

**AI-CONTEXT Comment Requirements**:
- **@file**: Path to corresponding context card file
- **@freshness**: ISO 8601 timestamp of last context update
- **@health**: Context health score (0-100%)
- **@dependencies**: Comma-separated list of key dependencies (optional)
- **@tags**: Comma-separated list of relevant tags (optional)

**Validation**:
- [ ] AI-CONTEXT comments updated in all source files
- [ ] Comment format validation passes
- [ ] Context file paths are correct and accessible
- [ ] Freshness timestamps are current

### Step 7: AI Context Integration (NEW - AI Loop)

**Timing**: After methodological files updated (≤1h after Step 5)
**Scope**: All updated methodological files

**Actions**:
1. **Parse Methodological Context**: Extract planning, decisions, and progress from files
2. **Update AI Context**: Include roadmap progress, recent decisions, and engineering log
3. **Validate AI Context**: Ensure AI tools have access to latest methodology state
4. **Test AI Integration**: Verify AI can access and use updated methodological context

**AI Context Requirements**:
- **Roadmap Context**: Current progress, next milestones, timeline adjustments
- **Decision Context**: Recent architectural decisions, rationale, and implications
- **Engineering Context**: Recent technical changes, lessons learned, and patterns
- **Planning Context**: Current priorities, blockers, and resource allocation

**Validation**:
- [ ] Methodological context parsed successfully
- [ ] AI context updated with latest methodology state
- [ ] AI tools can access methodological context
- [ ] AI integration validation passes
- [ ] Coverage targets met
- [ ] No broken cross-references
- [ ] Context health score ≥85%

### Step 5: Log Decisions & Release Notes

**Timing**: Within 1h of context update
**Scope**: All significant changes and decisions

**Actions**:
1. **Update ENGINEERING_LOG.md**: Log context changes and decisions
2. **Update Roadmap**: Modify task status and priorities
3. **Generate Delta Report**: Document what changed and why
4. **Notify Stakeholders**: Alert team to significant changes

**Log Requirements**:
- **Timestamp**: ISO 8601 format
- **Description**: Clear explanation of changes
- **Impact**: Effect on development workflow
- **Resolution**: Status and next steps

**Validation**:
- [ ] Engineering log updated
- [ ] Roadmap modified if needed
- [ ] Delta report generated
- [ ] Stakeholders notified

### Step 6: Make AI Tools Consume Latest Index

**Timing**: ≤1h after index update (SLA)
**Scope**: All AI tools and RAG systems

**Actions**:
1. **Update AI Context**: Provide new context to AI tools
2. **Validate Consumption**: Ensure tools can access new context
3. **Test Retrieval**: Verify context retrieval accuracy
4. **Monitor Performance**: Track AI tool effectiveness

**AI Context Contract**:
```yaml
ai_context:
  version: "1.0.0"
  index_url: "https://api.example.com/context/index"
  update_webhook: "https://api.example.com/context/webhook"
  validation_endpoint: "https://api.example.com/context/validate"
  metrics_endpoint: "https://api.example.com/context/metrics"
```

**Validation**:
- [ ] AI tools updated with new context
- [ ] Context retrieval working
- [ ] Performance metrics collected
- [ ] No errors in AI consumption

## Service Level Agreements (SLAs)

### Context Update SLA
- **Target**: ≤24h after code merge
- **Measurement**: Time from merge to context update completion
- **Reporting**: Daily SLA compliance report

### Index Update SLA
- **Target**: ≤30min after context update
- **Measurement**: Time from context update to index completion
- **Reporting**: Real-time SLA monitoring

### AI Consumption SLA
- **Target**: ≤1h after index update
- **Measurement**: Time from index completion to AI tool update
- **Reporting**: Hourly SLA compliance report

## Service Level Objectives (SLOs)

### Context Freshness SLO
- **Target**: 95% of context files updated within SLA
- **Measurement**: Percentage of context files meeting freshness requirements
- **Reporting**: Weekly SLO compliance report

### Context Quality SLO
- **Target**: 95% of context files pass quality gates
- **Measurement**: Percentage of files passing all validation checks
- **Reporting**: Continuous quality monitoring

### Context Coverage SLO
- **Target**: 90% of modules have context documentation
- **Measurement**: Percentage of modules with complete context
- **Reporting**: Weekly coverage report

## Key Performance Indicators (KPIs)

### Context Freshness %
**Formula**: (Files updated within SLA / Total files) × 100
**Target**: ≥95%
**Measurement**: Daily calculation

### Retrieval Precision@K
**Formula**: (Relevant results in top K / K) × 100
**Target**: ≥85% for K=5
**Measurement**: Continuous during AI usage

### Context Coverage %
**Formula**: (Modules with context / Total modules) × 100
**Target**: ≥90%
**Measurement**: Weekly calculation

### Drift MTTR (Mean Time To Repair)
**Formula**: Total repair time / Number of drift incidents
**Target**: ≤4h
**Measurement**: Per incident tracking

### Time-to-Context (TTC)
**Formula**: Time from question to context retrieval
**Target**: ≤30min
**Measurement**: Continuous during development

## Context Manifest

### Required Fields
```yaml
context_manifest:
  version: "1.0.0"
  project:
    name: "Project Name"
    description: "Project description"
    domain: "domain-type"
  
  owners:
    - role: "Context Maintainer"
      email: "maintainer@example.com"
      responsibility: "Overall context quality"
    
    - role: "Module Owner"
      email: "owner@example.com"
      responsibility: "Module-specific context"
  
  update_cadence:
    context_cards: "on-change"
    codemap: "weekly"
    index: "daily"
    validation: "continuous"
  
  chunking_guidance:
    target_size: "300-800 tokens"
    max_size: "1000 tokens"
    preferred_breaks: ["sections", "functions", "classes"]
  
  tags:
    - "backend"
    - "api"
    - "database"
    - "frontend"
```

### Optional Fields
```yaml
  ai_integration:
    rag_system: "OpenAI GPT-4"
    embedding_model: "text-embedding-ada-002"
    chunk_overlap: 50
    
  quality_gates:
    schema_validation: true
    content_validation: true
    coverage_validation: true
    cross_reference_validation: true
```

## Implementation Checklist

### Setup Phase
- [ ] Install CCD CLI tool
- [ ] Initialize project structure
- [ ] Configure CI/CD pipelines
- [ ] Set up quality gates
- [ ] Define context manifest
- [ ] Set up methodology loop files (roadmap.md, ENGINEERING_LOG.md, decisions/)
- [ ] Configure AI-CONTEXT comment templates

### First Run
- [ ] Generate initial context cards
- [ ] Create CODEMAP.yaml
- [ ] Create INDEX.yaml files
- [ ] Validate all context
- [ ] Generate initial index

### Ongoing Maintenance
- [ ] Monitor SLA compliance
- [ ] Track SLO performance
- [ ] Measure KPI achievement
- [ ] Update context manifest
- [ ] Optimize quality gates

## Troubleshooting

### Common Issues

**Context Update Failures**
- Check file permissions
- Verify CI/CD pipeline configuration
- Review error logs for specific failures

**Quality Gate Failures**
- Run validation locally: `ccd validate`
- Check schema compliance: `ccd validate-schemas`
- Review content quality: `ccd lint`
- Run quality gates: `ccd quality-gates --project .`
- Check context health: `ccd context-health --project . --detailed`
- Detect context drift: `ccd drift-detection --project .`

**Index Update Delays**
- Monitor embedding generation performance
- Check vector database connectivity
- Verify chunking configuration

**AI Consumption Issues**
- Test context retrieval: `ccd test-retrieval`
- Verify AI context contract
- Check authentication and permissions
- Validate AI-CONTEXT comments: `ccd validate-context-comments --project . --report`
- Check context freshness: `ccd context-freshness --project . --threshold 24`
- Extract AI-CONTEXT comments: `ccd extract-context --project .`

---

**Next**: Read the [CI/CD Integration](06-ci-cd-integration.md) to see how to implement this protocol in your development workflow.
