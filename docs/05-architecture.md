# CCD for AI (Continuous Context Documentation for AI) Architecture

## Overview

CCD uses a three-tier architecture to organize and structure context documentation at different levels of abstraction. This architecture ensures that context is comprehensive, maintainable, and optimized for AI consumption.

## Four-Tier Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Repository Level                        │
│                   (CODEMAP.yaml)                          │
│  • Project metadata                                        │
│  • Module overview                                         │
│  • Dependency mapping                                      │
│  • Technology stack                                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     Module Level                           │
│                     (INDEX.yaml)                           │
│  • Module purpose                                          │
│  • Input/output contracts                                  │
│  • File relationships                                      │
│  • Context card links                                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     File Level                             │
│                   (.ctx.md files)                          │
│  • File metadata                                           │
│  • Purpose and functionality                               │
│  • Dependencies and usage                                  │
│  • Key components                                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Code Level                              │
│                (AI-CONTEXT comments)                       │
│  • Direct context links                                    │
│  • Context freshness indicators                            │
│  • Context health status                                   │
│  • Quick context access                                    │
└─────────────────────────────────────────────────────────────┘
```

## Tier 1: Repository Level (CODEMAP.yaml)

### Purpose
Provides a high-level overview of the entire repository, including project metadata, module mapping, and dependency relationships.

### Structure
```yaml
version: "1.0.0"
project:
  name: "Project Name"
  description: "Project description"
  domain: "domain-type"
  technology_stack: ["language1", "language2", "framework1"]
  
modules:
  - name: "Module Name"
    path: "path/to/module"
    type: "service|library|tool|script|config|test"
    description: "Module description"
    language: "go|python|javascript|typescript|yaml|bash"
    size: "size in KB/MB"
    lines: 1234
    
dependencies:
  - from: "source-module"
    to: "target-module"
    type: "import|reference|contract|data|api"
    description: "Dependency description"
```

### Key Benefits
- **Repository Overview**: Quick understanding of project structure
- **Dependency Mapping**: Clear view of module relationships
- **Technology Stack**: Overview of languages and frameworks used
- **Module Discovery**: Easy identification of project components

### Usage Examples
```bash
# View repository overview
cat docs/codemap.yaml

# Check module dependencies
ccd dependencies --module "user-service"

# Analyze technology stack
ccd analyze --tech-stack
```

## Tier 2: Module Level (INDEX.yaml)

### Purpose
Provides detailed information about specific modules, including their purpose, input/output contracts, and file relationships.

### Structure
```yaml
module:
  name: "Module Name"
  path: "path/to/module"
  type: "service|library|tool|script|config|test"
  
purpose: "Detailed description of module purpose and functionality"

input:
  data_formats: ["json", "yaml", "csv"]
  apis: ["REST", "GraphQL", "gRPC"]
  contracts: ["input-schema.json", "validation.yaml"]
  
output:
  data_formats: ["json", "yaml", "csv"]
  apis: ["REST", "GraphQL", "gRPC"]
  contracts: ["output-schema.json", "response.yaml"]
  
files:
  - path: "file1.py"
    type: "source|config|test|doc|script|schema"
    description: "File description"
    language: "python"
    size: "1.2 KB"
    lines: 45
    context_card: "path/to/file1.py.ctx.md"
    
dependencies:
  - module: "dependency-module"
    type: "import|reference|contract|data|api"
    description: "Dependency description"
```

### Key Benefits
- **Module Understanding**: Clear purpose and functionality
- **Contract Definition**: Input/output specifications
- **File Mapping**: Complete file inventory with context links
- **Dependency Details**: Module-specific dependency information

### Usage Examples
```bash
# View module details
cat docs/index/module-name.yaml

# Check module contracts
ccd contracts --module "user-service"

# Analyze file relationships
ccd analyze --files --module "user-service"
```

## Tier 3: File Level (Context Cards)

### Purpose
Provides detailed information about specific files, including their purpose, dependencies, key components, and implementation details.

### Structure
```markdown
---
title: "Context Card Title"
owner: "team-member"
updated_at: "2025-08-28"
systems_impacted: ["module-name"]
file_path: "path/to/source/file"
file_type: "go|py|js|ts|yaml|md"
file_size: "0 KB"
lines_of_code: 0
dependencies: []
tags: ["context-card", "template"]
---

# Context Card: [File Name]

## Overview
Brief description of what this file does and its purpose in the system.

## Purpose
- **Primary Function**: Main responsibility of this file
- **Secondary Functions**: Additional responsibilities
- **Business Value**: Why this file exists

## Dependencies
- **Imports**: External libraries and modules
- **Internal Dependencies**: Other project files this depends on
- **System Dependencies**: OS, runtime, or infrastructure requirements

## Key Components
- **Classes/Functions**: Main code structures
- **Configuration**: Settings and parameters
- **Constants**: Important values and definitions

## Data Flow
- **Input**: What data this file receives
- **Processing**: How data is transformed
- **Output**: What data this file produces

## Architecture Context
- **Layer**: Where this fits in the system architecture
- **Pattern**: Design patterns used
- **Contracts**: APIs and interfaces exposed

## Testing
- **Test Coverage**: Current test status
- **Test Files**: Associated test files
- **Test Strategy**: How this should be tested

## Performance Considerations
- **Complexity**: Time/space complexity of key operations
- **Bottlenecks**: Known performance issues
- **Optimization Opportunities**: Areas for improvement

## Security
- **Input Validation**: How inputs are validated
- **Authentication**: Access control mechanisms
- **Data Protection**: How sensitive data is handled

## Monitoring & Observability
- **Metrics**: Key performance indicators
- **Logging**: What gets logged and when
- **Alerts**: Conditions that trigger alerts

## Troubleshooting
- **Common Issues**: Known problems and solutions
- **Debugging**: How to debug this component
- **Recovery**: How to recover from failures

## Future Considerations
- **Technical Debt**: Known issues to address
- **Enhancements**: Planned improvements
- **Migration**: Future architectural changes

## Related Documentation
- **Architecture**: Links to architecture documents
- **API Docs**: API documentation
- **User Guides**: User-facing documentation

## Change Log
- **2025-08-28**: Initial context card creation
- **[Date]**: [Description of change]

---

**Last Updated**: [Date]  
**Next Review**: [Date + 30 days]  
**Owner**: [Team Member]
```

### Key Benefits
- **Comprehensive Documentation**: Detailed information about each file
- **Structured Format**: Consistent organization for easy consumption
- **AI-Optimized**: Format designed for RAG systems and AI tools
- **Maintainable**: Clear structure for updates and maintenance

### Usage Examples
```bash
# View context card for specific file
cat docs/contexts/files/path/to/file.ctx.md

# Search context cards
ccd search --query "user authentication" --contexts

# Validate context card
ccd validate --context docs/contexts/files/path/to/file.ctx.md
```

## Tier 4: Code Level (AI-CONTEXT Comments)

### Purpose
Provides direct access to context documentation from within the source code, enabling developers and AI tools to quickly access relevant context without leaving their development environment.

### Structure
```go
// AI-CONTEXT: @file:contexts/files/services/edge-gateway/cmd/edge/main.go.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:95%
// AI-CONTEXT: @dependencies:router.go,middleware.go,config.go
// AI-CONTEXT: @tags:entry-point,server,initialization

package main

import (
    "github.com/gin-gonic/gin"
    "github.com/sirupsen/logrus"
    "os"
    "os/signal"
    "syscall"
)

// Main application entry point for the Edge Gateway service
func main() {
    // ... implementation
}
```

```python
# AI-CONTEXT: @file:contexts/files/services/coach-llm/coach_llm.py.ctx.md
# AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
# AI-CONTEXT: @health:92%
# AI-CONTEXT: @dependencies:openai,langchain,fastapi
# AI-CONTEXT: @tags:ai,coaching,llm

import openai
from langchain.llms import OpenAI
from fastapi import FastAPI

class CoachLLM:
    """AI-powered coaching system using LLM technology"""
    
    def __init__(self):
        # ... implementation
```

```typescript
// AI-CONTEXT: @file:contexts/files/services/web-demo/app.ts.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:88%
// AI-CONTEXT: @dependencies:express,websocket,typescript
// AI-CONTEXT: @tags:web,websocket,demo

import express from 'express';
import { WebSocketServer } from 'ws';

const app = express();
// ... implementation
```

### AI-CONTEXT Comment Format

#### Required Fields
- **@file**: Path to the corresponding context card file
- **@freshness**: ISO 8601 timestamp of last context update
- **@health**: Context health score (0-100%)

#### Optional Fields
- **@dependencies**: Comma-separated list of key dependencies
- **@tags**: Comma-separated list of relevant tags
- **@owner**: Team member responsible for this file
- **@review**: Next review date
- **@status**: Current development status (active, deprecated, etc.)

### Key Benefits
- **Direct Access**: Context available immediately from code
- **Context Freshness**: Real-time indicators of context currency
- **Health Monitoring**: Visual indicators of context quality
- **Developer Experience**: No need to navigate to separate files
- **AI Integration**: AI tools can access context directly from code
- **Context Awareness**: Developers always know context status

### Usage Examples
```bash
# Extract AI-CONTEXT comments from code
ccd extract-context --file src/main.go

# Validate AI-CONTEXT comments
ccd validate-context-comments --file src/main.go

# Update AI-CONTEXT comments
ccd update-context-comments --file src/main.go --context docs/contexts/files/src/main.go.ctx.md

# Check context freshness across project
ccd context-freshness --project .
```

### Integration with Development Workflow

#### Before Development
1. **Read AI-CONTEXT comments** to understand current context
2. **Check context freshness** to ensure information is current
3. **Review context health** to identify potential issues
4. **Follow context links** to detailed documentation

#### During Development
1. **Reference context** directly from code
2. **Update context** when making significant changes
3. **Maintain context links** as files are moved or renamed
4. **Validate context** before committing changes

#### After Development
1. **Update context cards** with new information
2. **Refresh AI-CONTEXT comments** with new timestamps
3. **Validate context health** to ensure quality
4. **Commit context updates** with code changes

### Purpose
Provides detailed information about individual files, including their purpose, dependencies, key components, and usage examples.

### Structure
```markdown
# Context Card: filename.ext

**File Path**: `path/to/file`  
**Language**: Language  
**Domain**: domain  
**Category**: category  
**Size**: size bytes  
**Lines**: lines  
**Last Modified**: timestamp

## Overview
Brief description of file purpose and context.

## Purpose
Detailed purpose and functionality description.

## Dependencies
- **Imports/Includes**: dependencies
- **Referenced By**: files that reference this file

## Key Components
Key functions, classes, or components in the file.

## Usage Examples
Usage examples or patterns.

## Related Files
Related or similar files.

## Notes
Additional context and notes.

---
*This context card helps AI understand the purpose and structure of this file within the codebase.*
```

### Key Benefits
- **File Understanding**: Detailed file purpose and functionality
- **Component Discovery**: Key functions, classes, and structures
- **Dependency Tracking**: Import and reference relationships
- **Usage Guidance**: Examples and patterns for file usage

### Usage Examples
```bash
# View file context
cat docs/examples/*/filename.ext.ctx.md

# Search context content
ccd search --query "user authentication" --files

# Generate context for new file
ccd generate-card --file "new-file.py"
```

## Architecture Benefits

### 1. Scalability
- **Repository Level**: Handles projects of any size
- **Module Level**: Scales with module complexity
- **File Level**: Accommodates any number of files

### 2. Maintainability
- **Separation of Concerns**: Each tier has specific responsibilities
- **Modular Updates**: Changes at one level don't affect others
- **Clear Dependencies**: Explicit relationships between tiers

### 3. AI Optimization
- **Structured Data**: Consistent format for AI consumption
- **Chunkable Content**: Break into digestible pieces
- **Rich Metadata**: Comprehensive information for AI tools

### 4. Developer Experience
- **Easy Navigation**: Clear path from overview to details
- **Consistent Format**: Standardized structure across all levels
- **Quick Access**: Fast retrieval of specific information

## Data Flow

### Context Generation Flow
```
Code Changes → File Analysis → Context Card Generation → Module Index Update → Repository Map Update
     ↓              ↓                    ↓                    ↓                    ↓
  Git Hook    Language Parser    Template Engine    Index Generator    Map Generator
```

### Context Consumption Flow
```
AI Query → Query Parser → Multi-Tier Search → Context Retrieval → Response Generation
    ↓           ↓              ↓                ↓                ↓
  User    Query Type    Repository/Module/File    Context Cards    AI Response
```

### Validation Flow
```
Context Files → Schema Validation → Content Validation → Coverage Validation → Health Report
      ↓              ↓                ↓                ↓                ↓
  All Tiers    JSON Schemas    Quality Rules    Coverage Rules    Metrics
```

## Implementation Guidelines

### 1. Start with Repository Level
- Create CODEMAP.yaml first
- Define high-level project structure
- Identify major modules and dependencies

### 2. Add Module Level
- Create INDEX.yaml for each module
- Define module purpose and contracts
- Map file relationships

### 3. Generate File Level
- Create context cards for all source files
- Follow consistent template structure
- Include comprehensive metadata

### 4. Validate and Optimize
- Run validation across all tiers
- Ensure cross-reference integrity
- Optimize for AI consumption

### 5. Integrate AI-CONTEXT Comments
- Add AI-CONTEXT comments to source files
- Validate comment format and content
- Ensure context synchronization between code and documentation

## Quality Assurance

### Schema Validation
- **CODEMAP.yaml**: Validate against codemap.schema.json
- **INDEX.yaml**: Validate against index.schema.json
- **Context Cards**: Validate against context-card.schema.json

### Content Validation
- **Length Limits**: Maximum 200 lines per context card
- **Required Sections**: All mandatory sections present
- **Metadata Completeness**: All required fields populated

### Coverage Validation
- **Module Coverage**: 90%+ of modules documented
- **File Coverage**: 90%+ of source files have context cards
- **Dependency Coverage**: 100% of dependencies mapped

### Cross-Reference Validation
- **Link Integrity**: All cross-references are valid
- **Path Accuracy**: File paths are correct
- **Relationship Consistency**: Dependencies are consistent across tiers

### AI-CONTEXT Validation
- **Comment Format**: All AI-CONTEXT comments follow required format
- **Context Synchronization**: AI-CONTEXT comments match context card content
- **Freshness Validation**: AI-CONTEXT timestamps are current
- **Drift Detection**: No drift between source code and context documentation

## Performance Considerations

### Indexing Performance
- **Incremental Updates**: Only update changed context
- **Parallel Processing**: Process multiple files simultaneously
- **Caching**: Cache frequently accessed context

### Search Performance
- **Multi-Tier Search**: Search across all levels efficiently
- **Index Optimization**: Optimize search indexes for common queries
- **Result Ranking**: Rank results by relevance and freshness

### Storage Optimization
- **Compression**: Compress context files when possible
- **Deduplication**: Remove duplicate content across tiers
- **Archival**: Archive old context versions

---

**Next**: Read the [CI/CD Integration](06-ci-cd-integration.md) to see how this architecture is implemented in automated workflows.
