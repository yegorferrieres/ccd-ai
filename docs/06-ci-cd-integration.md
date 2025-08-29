# CCD for AI (Continuous Context Documentation for AI) CI/CD Integration

## Overview

This document provides comprehensive CI/CD integration examples for implementing CCD in your development workflow. It includes GitHub Actions, GitLab CI, and other CI/CD platform configurations to automate context generation, validation, and deployment.

## GitHub Actions Integration

### 1. Context Validation Workflow

```yaml
# .github/workflows/validate-context.yml
name: Validate Context

on:
  pull_request:
    paths: ['**/*.go', '**/*.py', '**/*.js', '**/*.ts', '**/*.yaml', '**/*.yml']
  push:
    branches: [main, develop]
    paths: ['**/*.go', '**/*.py', '**/*.js', '**/*.ts', '**/*.yaml', '**/*.yml']

jobs:
  validate-context:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          
      - name: Install CCD CLI
        run: npm install -g @ccd/cli
        
      - name: Validate Context Structure
        run: ccd validate-schemas --schemas docs/schemas/
        
      - name: Validate Context Content
        run: ccd validate-contexts --contexts docs/ --fail-on-error
        
      - name: Check Context Coverage
        run: ccd coverage --modules --files --output coverage-report.json
        
      - name: Upload Context Delta Report
        uses: actions/upload-artifact@v4
        with:
          name: context-delta-report
          path: coverage-report.json
          retention-days: 30
          
      - name: Comment PR with Results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = JSON.parse(fs.readFileSync('coverage-report.json', 'utf8'));
            
            const comment = `## Context Validation Results
            
            **Coverage**: ${report.coverage.modules}% modules, ${report.coverage.files}% files
            **Quality**: ${report.quality.score}/100
            **Issues**: ${report.issues.length} found
            
            ${report.issues.length > 0 ? 'Please fix context issues before merging.' : 'All context validation passed!'}`;
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

### 2. Context Generation Workflow

```yaml
# .github/workflows/generate-context.yml
name: Generate Context

on:
  push:
    branches: [main]
    paths: ['**/*.go', '**/*.py', '**/*.js', '**/*.ts', '**/*.yaml', '**/*.yml']

jobs:
  generate-context:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          
      - name: Install CCD CLI
        run: npm install -g @ccd/cli
        
      - name: Generate Context Cards
        run: |
          ccd generate-cards --file-types go,py,js,ts,yaml,yml --force
          ccd generate-cards --file-types go,py,js,ts,yaml,yml --force
          
      - name: Update Module Indexes
        run: ccd update-indexes --modules all
        
      - name: Update Repository CODEMAP
        run: ccd update-codemap --force
        
      - name: Validate Generated Context
        run: ccd validate-contexts --contexts docs/ --fail-on-error
        
      - name: Commit Context Updates
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add docs/
          git commit -m "feat: update context documentation [skip ci]" || exit 0
          git push
```

### 3. Context Health Monitoring

```yaml
# .github/workflows/context-health.yml
name: Context Health Monitoring

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  workflow_dispatch:

jobs:
  context-health:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          
      - name: Install CCD CLI
        run: npm install -g @ccd/cli
        
      - name: Run Health Check
        run: ccd health-check --report --output health-report.json
        
      - name: Pack Contexts
        run: ccd pack-contexts --output contexts-archive.zip
        
      - name: Upload Health Report
        uses: actions/upload-artifact@v4
        with:
          name: context-health-report
          path: |
            health-report.json
            contexts-archive.zip
          retention-days: 90
          
      - name: Create Issue for Problems
        if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = JSON.parse(fs.readFileSync('health-report.json', 'utf8'));
            
            if (report.health_score < 80) {
              github.rest.issues.create({
                owner: context.repo.owner,
                repo: context.repo.repo,
                title: 'Context Health Issues Detected',
                body: `## Context Health Alert
                
                **Health Score**: ${report.health_score}/100
                **Issues Found**: ${report.issues.length}
                
                Please review and fix context health issues.`,
                labels: ['context-health', 'documentation']
              });
            }
```

## GitLab CI Integration

### 1. Context Validation Pipeline

```yaml
# .gitlab-ci.yml
stages: [validate, generate, deploy]

variables:
  CCD_VERSION: "1.0.0"

# Context validation job
context-validation:
  stage: validate
  image: node:20-alpine
  before_script:
    - npm install -g @ccd/cli@$CCD_VERSION
  script:
    - ccd validate-schemas --schemas docs/schemas/
    - ccd validate-contexts --contexts docs/ --fail-on-error
    - ccd coverage --modules --files --output coverage-report.json
    - ccd quality-gates --project . --output quality-report.json
    - ccd context-health --project . --detailed
  artifacts:
    reports:
      junit: context-validation-report.xml
    paths:
      - coverage-report.json
    expire_in: 1 week
  rules:
    - changes:
        - "**/*.go"
        - "**/*.py"
        - "**/*.js"
        - "**/*.ts"
        - "**/*.yaml"
        - "**/*.yml"
        - "docs/**/*"

# Context generation job
context-generation:
  stage: generate
  image: node:20-alpine
  before_script:
    - npm install -g @ccd/cli@$CCD_VERSION
  script:
    - ccd generate-cards --file-types go,py,js,ts,yaml,yml --force
    - ccd update-indexes --modules all
    - ccd update-codemap --force
    - ccd validate-contexts --contexts docs/ --fail-on-error
  artifacts:
    paths:
      - docs/
    expire_in: 1 month
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      changes:
        - "**/*.go"
        - "**/*.py"
        - "**/*.js"
        - "**/*.ts"
        - "**/*.yaml"
        - "**/*.yml"

# Context health monitoring
context-health:
  stage: validate
  image: node:20-alpine
  before_script:
    - npm install -g @ccd/cli@$CCD_VERSION
  script:
    - ccd health-check --report --output health-report.json
    - ccd pack-contexts --output contexts-archive.zip
    - ccd drift-detection --project . --output drift-report.json
    - ccd context-freshness --project . --threshold 24
  artifacts:
    paths:
      - health-report.json
      - contexts-archive.zip
    expire_in: 3 months
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
  when: always
```

### 2. Advanced GitLab CI with Matrix

```yaml
# .gitlab-ci.yml with matrix strategy
context-validation-matrix:
  stage: validate
  image: node:20-alpine
  parallel:
    matrix:
      - FILE_TYPE: "go"
      - FILE_TYPE: "py"
      - FILE_TYPE: "js"
      - FILE_TYPE: "ts"
      - FILE_TYPE: "yaml"
  before_script:
    - npm install -g @ccd/cli@$CCD_VERSION
  script:
    - ccd validate-contexts --file-types $FILE_TYPE --contexts docs/ --fail-on-error
    - ccd coverage --file-types $FILE_TYPE --output coverage-$FILE_TYPE.json
  artifacts:
    paths:
      - coverage-$FILE_TYPE.json
    expire_in: 1 week
  rules:
    - changes:
        - "**/*.$FILE_TYPE"
```

## Other CI/CD Platforms

### 1. Jenkins Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        CCD_VERSION = '1.0.0'
    }
    
    stages {
        stage('Setup') {
            steps {
                sh 'npm install -g @ccd/cli@${CCD_VERSION}'
            }
        }
        
        stage('Validate Context') {
            steps {
                sh 'ccd validate-schemas --schemas docs/schemas/'
                sh 'ccd validate-contexts --contexts docs/ --fail-on-error'
                sh 'ccd coverage --modules --files --output coverage-report.json'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'coverage-report.json', fingerprint: true
                }
            }
        }
        
        stage('Generate Context') {
            when {
                branch 'main'
            }
            steps {
                sh 'ccd generate-cards --file-types go,py,js,ts,yaml,yml --force'
                sh 'ccd update-indexes --modules all'
                sh 'ccd update-codemap --force'
            }
        }
        
        stage('Health Check') {
            steps {
                sh 'ccd health-check --report --output health-report.json'
                sh 'ccd pack-contexts --output contexts-archive.zip'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'health-report.json,contexts-archive.zip', fingerprint: true
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
```

### 2. CircleCI Configuration

```yaml
# .circleci/config.yml
version: 2.1

jobs:
  validate-context:
    docker:
      - image: node:20-alpine
    steps:
      - checkout
      - run: npm install -g @ccd/cli@1.0.0
      - run: ccd validate-schemas --schemas docs/schemas/
      - run: ccd validate-contexts --contexts docs/ --fail-on-error
      - run: ccd coverage --modules --files --output coverage-report.json
      - store_artifacts:
          path: coverage-report.json
          destination: context-coverage
          
  generate-context:
    docker:
      - image: node:20-alpine
    steps:
      - checkout
      - run: npm install -g @ccd/cli@1.0.0
      - run: ccd generate-cards --file-types go,py,js,ts,yaml,yml --force
      - run: ccd update-indexes --modules all
      - run: ccd update-codemap --force
      - run: ccd validate-contexts --contexts docs/ --fail-on-error
      - run: ccd quality-gates --project . --output quality-report.json
      - run: ccd drift-detection --project . --output drift-report.json
      - run: ccd context-health --project . --detailed
      - add_ssh_keys:
          fingerprints:
            - "your-ssh-fingerprint"
      - run: |
          git config --global user.email "ci@example.com"
          git config --global user.name "CircleCI"
          git add docs/
          git commit -m "feat: update context documentation [skip ci]" || exit 0
          git push origin main

workflows:
  version: 2
  context-workflow:
    jobs:
      - validate-context:
          filters:
            branches:
              only: /.*/
      - generate-context:
          filters:
            branches:
              only: main
          requires:
            - validate-context
```

## LLM-Agnostic Interface Example

### Context Retrieval API

```typescript
// Example interface for retriever step (no external keys)
interface ContextRetriever {
  // Retrieve context based on query
  retrieve(query: string, options?: RetrieveOptions): Promise<ContextResult[]>;
  
  // Get context for specific file or module
  getContext(path: string, type: 'file' | 'module' | 'repository'): Promise<ContextResult>;
  
  // Search across all context tiers
  search(query: string, filters?: SearchFilters): Promise<SearchResult>;
  
  // Get context health metrics
  getHealth(): Promise<HealthMetrics>;
}

interface RetrieveOptions {
  maxResults?: number;
  threshold?: number;
  includeMetadata?: boolean;
  tier?: 'file' | 'module' | 'repository';
}

interface ContextResult {
  content: string;
  metadata: {
    path: string;
    type: 'file' | 'module' | 'repository';
    language?: string;
    domain?: string;
    lastModified: string;
    relevance: number;
  };
  source: string;
}

interface SearchResult {
  results: ContextResult[];
  total: number;
  query: string;
  filters: SearchFilters;
}

interface SearchFilters {
  fileTypes?: string[];
  languages?: string[];
  domains?: string[];
  dateRange?: {
    from: string;
    to: string;
  };
}

interface HealthMetrics {
  coverage: {
    modules: number;
    files: number;
    dependencies: number;
  };
  quality: {
    schemaCompliance: number;
    contentQuality: number;
    crossReferences: number;
  };
  freshness: {
    lastUpdate: string;
    slaCompliance: number;
  };
}
```

## Implementation Checklist

### Setup Phase
- [ ] Install CCD CLI in CI environment
- [ ] Configure context validation workflow
- [ ] Set up context generation pipeline
- [ ] Configure health monitoring
- [ ] Test all workflows

### Integration Phase
- [ ] Connect to existing CI/CD pipelines
- [ ] Configure artifact storage
- [ ] Set up notifications and alerts
- [ ] Monitor pipeline performance
- [ ] Optimize workflow efficiency

### Maintenance Phase
- [ ] Monitor SLA compliance
- [ ] Track pipeline success rates
- [ ] Optimize context generation
- [ ] Update workflows as needed
- [ ] Train team on new processes

## Best Practices

### 1. Pipeline Design
- **Fail Fast**: Validate context early in pipeline
- **Parallel Processing**: Run independent validations in parallel
- **Caching**: Cache CCD CLI and dependencies
- **Artifacts**: Store context reports for analysis

### 2. Error Handling
- **Graceful Degradation**: Continue pipeline even if context validation fails
- **Detailed Logging**: Log all context operations for debugging
- **User Feedback**: Provide clear error messages and suggestions
- **Retry Logic**: Retry failed context operations

### 3. Performance Optimization
- **Incremental Updates**: Only process changed files
- **Parallel Jobs**: Run multiple context operations simultaneously
- **Resource Limits**: Set appropriate resource limits for context operations
- **Monitoring**: Track pipeline performance and optimize bottlenecks

---

**Next**: Read the [Observability & Audit](07-observability-audit.md) to understand how to monitor and measure CCD effectiveness.
