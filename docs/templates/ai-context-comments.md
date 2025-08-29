# AI-CONTEXT Comments Template

This document provides templates for adding AI-CONTEXT comments to source code files in different programming languages. These comments enable direct access to context documentation from within the code.

## Comment Format

### Required Fields
- **@file**: Path to the corresponding context card file
- **@freshness**: ISO 8601 timestamp of last context update
- **@health**: Context health score (0-100%)

### Optional Fields
- **@dependencies**: Comma-separated list of key dependencies
- **@tags**: Comma-separated list of relevant tags
- **@owner**: Team member responsible for this file
- **@review**: Next review date
- **@status**: Current development status (active, deprecated, etc.)

## Language-Specific Templates

### Go
```go
// AI-CONTEXT: @file:contexts/files/services/edge-gateway/cmd/edge/main.go.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:95%
// AI-CONTEXT: @dependencies:router.go,middleware.go,config.go
// AI-CONTEXT: @tags:entry-point,server,initialization
// AI-CONTEXT: @owner:backend-team
// AI-CONTEXT: @review:2025-09-27
// AI-CONTEXT: @status:active

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

### Python
```python
# AI-CONTEXT: @file:contexts/files/services/coach-llm/coach_llm.py.ctx.md
# AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
# AI-CONTEXT: @health:92%
# AI-CONTEXT: @dependencies:openai,langchain,fastapi
# AI-CONTEXT: @tags:ai,coaching,llm
# AI-CONTEXT: @owner:ai-team
# AI-CONTEXT: @review:2025-09-27
# AI-CONTEXT: @status:active

import openai
from langchain.llms import OpenAI
from fastapi import FastAPI

class CoachLLM:
    """AI-powered coaching system using LLM technology"""
    
    def __init__(self):
        # ... implementation
```

### JavaScript/TypeScript
```typescript
// AI-CONTEXT: @file:contexts/files/services/web-demo/app.ts.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:88%
// AI-CONTEXT: @dependencies:express,websocket,typescript
// AI-CONTEXT: @tags:web,websocket,demo
// AI-CONTEXT: @owner:frontend-team
// AI-CONTEXT: @review:2025-09-27
// AI-CONTEXT: @status:active

import express from 'express';
import { WebSocketServer } from 'ws';

const app = express();
// ... implementation
```

### Java
```java
// AI-CONTEXT: @file:contexts/files/services/user-service/UserController.java.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:90%
// AI-CONTEXT: @dependencies:UserService,UserRepository,Spring Boot
// AI-CONTEXT: @tags:controller,rest,api
// AI-CONTEXT: @owner:backend-team
// AI-CONTEXT: @review:2025-09-27
// AI-CONTEXT: @status:active

package com.example.userservice.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
@RequestMapping("/api/users")
public class UserController {
    // ... implementation
}
```

### C#
```csharp
// AI-CONTEXT: @file:contexts/files/services/user-service/UserController.cs.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:87%
// AI-CONTEXT: @dependencies:UserService,UserRepository,ASP.NET Core
// AI-CONTEXT: @tags:controller,rest,api
// AI-CONTEXT: @owner:backend-team
// AI-CONTEXT: @review:2025-09-27
// AI-CONTEXT: @status:active

using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;

namespace UserService.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UserController : ControllerBase
    {
        // ... implementation
    }
}
```

### Rust
```rust
// AI-CONTEXT: @file:contexts/files/services/edge-gateway/src/main.rs.ctx.md
// AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
// AI-CONTEXT: @health:93%
// AI-CONTEXT: @dependencies:tokio,axum,serde
// AI-CONTEXT: @tags:entry-point,server,async
// AI-CONTEXT: @owner:backend-team
// AI-CONTEXT: @review:2025-09-27
// AI-CONTEXT: @status:active

use tokio;
use axum::Router;

#[tokio::main]
async fn main() {
    // ... implementation
}
```

### Shell Scripts
```bash
#!/bin/bash
# AI-CONTEXT: @file:contexts/files/scripts/deploy.sh.ctx.md
# AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
# AI-CONTEXT: @health:85%
# AI-CONTEXT: @dependencies:docker,kubectl,helm
# AI-CONTEXT: @tags:deployment,script,automation
# AI-CONTEXT: @owner:devops-team
# AI-CONTEXT: @review:2025-09-27
# AI-CONTEXT: @status:active

# Deployment script for the application
set -e

echo "Starting deployment..."
# ... implementation
```

### YAML/Configuration Files
```yaml
# AI-CONTEXT: @file:contexts/files/config/docker-compose.yml.ctx.md
# AI-CONTEXT: @freshness:2025-08-28T10:00:00Z
# AI-CONTEXT: @health:89%
# AI-CONTEXT: @dependencies:postgres,redis,nginx
# AI-CONTEXT: @tags:configuration,docker,infrastructure
# AI-CONTEXT: @owner:devops-team
# AI-CONTEXT: @review:2025-09-27
# AI-CONTEXT: @status:active

version: '3.8'
services:
  postgres:
    image: postgres:13
    # ... configuration
```

## Best Practices

### 1. Placement
- Place AI-CONTEXT comments at the very beginning of the file
- Use language-appropriate comment syntax
- Keep comments concise but informative

### 2. Content
- Always include required fields (@file, @freshness, @health)
- Use descriptive tags that help with search and categorization
- Keep dependency lists focused on key dependencies only

### 3. Maintenance
- Update @freshness timestamp whenever context is updated
- Recalculate @health score based on context quality metrics
- Review and update @tags as the file evolves

### 4. Validation
- Validate comment format using `ccd validate-context-comments`
- Ensure context file paths are correct and accessible
- Check that all required fields are present

## CLI Commands

### Extract AI-CONTEXT Comments
```bash
# Extract comments from a single file
ccd extract-context --file src/main.go

# Extract comments from multiple files
ccd extract-context --files src/**/*.go

# Extract comments from entire project
ccd extract-context --project .
```

### Validate AI-CONTEXT Comments
```bash
# Validate single file
ccd validate-context-comments --file src/main.go

# Validate multiple files
ccd validate-context-comments --files src/**/*.go

# Validate entire project
ccd validate-context-comments --project .
```

### Update AI-CONTEXT Comments
```bash
# Update comments in a file
ccd update-context-comments --file src/main.go --context docs/contexts/files/src/main.go.ctx.md

# Update comments across project
ccd update-context-comments --project . --refresh-timestamps
```

### Check Context Freshness
```bash
# Check freshness of single file
ccd context-freshness --file src/main.go

# Check freshness across project
ccd context-freshness --project .

# Generate freshness report
ccd context-freshness --project . --report --output freshness-report.json
```

## Integration with Development Workflow

### Before Development
1. Read AI-CONTEXT comments to understand current context
2. Check context freshness to ensure information is current
3. Review context health to identify potential issues
4. Follow context links to detailed documentation

### During Development
1. Reference context directly from code
2. Update context when making significant changes
3. Maintain context links as files are moved or renamed
4. Validate context before committing changes

### After Development
1. Update context cards with new information
2. Refresh AI-CONTEXT comments with new timestamps
3. Validate context health to ensure quality
4. Commit context updates with code changes

## Quality Gates

### Comment Format Validation
- [ ] All required fields are present
- [ ] Comment format follows language conventions
- [ ] File paths are correct and accessible
- [ ] Timestamps are in ISO 8601 format

### Context Synchronization
- [ ] AI-CONTEXT comments match context card content
- [ ] Freshness timestamps are current
- [ ] Health scores are accurate
- [ ] Dependencies and tags are up-to-date

### Integration Validation
- [ ] Context files are accessible from comment paths
- [ ] AI tools can parse and use comments
- [ ] Development workflow includes comment updates
- [ ] Quality gates validate comment compliance

---

**Last Updated**: 2025-08-28  
**Version**: 1.0.0  
**Status**: Active Template
