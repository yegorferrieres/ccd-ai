# MartLive AI Video Assistant - Development Rules

## Core Principles

### 1. Context First
- **ALWAYS** read context files before starting development
- Context files are the source of truth about the project
- Don't start development without understanding existing architecture

### 2. AI-Native Development
- Design for AI tool consumption from the start
- Use clear, structured patterns that AI tools can understand
- Document AI model interfaces and parameters thoroughly

### 3. Maintain Currency
- Update context files after each change
- Validate changes before committing
- Synchronize metadata regularly

## Algorithm for Working with Context Files

### Before Starting Development:

1. **Study the general project context**
   ```bash
   # Read the main context
   cat docs/project-context.md
   ```

2. **Analyze module dependencies**
   ```bash
   # Study the dependency map
   cat docs/codemap.yaml
   ```

3. **Study the context of affected modules**
   ```bash
   # Read .ctx.md files of needed modules
   ls docs/examples/*/*.ctx.md
   ```

4. **Check architectural decisions**
   ```bash
   # Study ADR (Architecture Decision Records)
   ls docs/decisions/*.md
   ```

5. **Search for existing functionality**
   ```bash
   # Check the function catalog
   cat docs/function-catalog.md
   ```

### During Development:

1. **Follow existing patterns** from `.ctx.md` files
2. **Use established contracts** and schemas
3. **Comply with architectural principles** from ADR
4. **Document changes** in context files

### After Completing Development:

1. **Update affected `.ctx.md` files**
2. **Run metadata validation**
   ```bash
   make validate
   ```
3. **Update `docs/codemap.yaml`** if dependencies changed
4. **Run metadata synchronization**
   ```bash
   make coverage
   ```

## **Context Update Workflow (MANDATORY)**

### **Step-by-Step Process:**

1. **Complete Development Task** ✅
2. **Ask User for Confirmation** ❓
   - "All changes completed. Confirm that context files need to be updated?"
3. **After User Confirmation** ✅
   - Update all affected `.ctx.md` files
   - Update `docs/codemap.yaml` if needed
   - Update `docs/ENGINEERING_LOG.md` with new entry
   - Update `docs/README.md` if needed
   - Update `docs/project-context.md` if needed
4. **Run Validation** ✅
   ```bash
   make validate
   ```
5. **Run Full Sync** ✅
   ```bash
   make coverage
   ```
6. **Confirm Completion** ✅
   - "All context files updated and synchronized"

### **Files That Must Be Updated:**
- **All affected `.ctx.md` files** in `docs/examples/`
- **`docs/codemap.yaml`** - if module dependencies changed
- **`docs/ENGINEERING_LOG.md`** - new entry with timestamp and description
- **`docs/README.md`** - if new features or rules added
- **`docs/project-context.md`** - if project status changed
- **`docs/DEVELOPMENT_RULES.md`** - if new rules or processes added
- **`docs/roadmap.md`** - update task status, add completed items, adjust priorities, update current phase and milestone

## AI-Specific Development Rules

### 1. Model Interface Documentation
- **ALWAYS** document AI model parameters and interfaces
- Include example inputs and expected outputs
- Document model versioning and compatibility

### 2. Context Preservation
- Maintain conversation context across service boundaries
- Document context flow between services
- Ensure context is preserved in error scenarios

### 3. Performance Considerations
- Document expected response times for AI operations
- Include token usage estimates and limits
- Document caching strategies and invalidation rules

### 4. Error Handling
- Document AI model failure scenarios
- Include fallback strategies and recovery procedures
- Document retry logic and backoff strategies

## Microservices Development Rules

### 1. Service Boundaries
- **NEVER** create tight coupling between services
- Use well-defined contracts and interfaces
- Document service dependencies clearly

### 2. API Design
- Follow RESTful principles for HTTP APIs
- Use consistent error response formats
- Document all API endpoints with examples

### 3. Data Contracts
- Define clear input/output data structures
- Use schema validation for all data
- Document data transformation rules

## Real-time System Rules

### 1. WebSocket Management
- Document connection lifecycle management
- Include reconnection strategies
- Document message format and validation

### 2. Streaming Considerations
- Document stream processing patterns
- Include backpressure handling strategies
- Document error handling for stream failures

### 3. Performance Monitoring
- Document expected latency targets
- Include monitoring and alerting rules
- Document performance optimization strategies

## File Organization Rules

### Test Files
- **ALL test files must be placed in the `tests/` directory**
- Test files should not be kept in the root directory
- Use descriptive names for test files (e.g., `test_coach_llm.py`, `test_edge_gateway.go`)
- Virtual environments for testing should also be in `tests/` directory

### Code Organization
- Keep source code in appropriate service directories
- Keep configuration in root config files
- Keep documentation in `docs/` and root markdown files

### Context File Rules
- **NEVER create context files for external libraries** installed via package managers
- **NEVER create context files for system packages** or third-party dependencies
- **NEVER create context files for system directories** (`/lib/`, `/usr/`, `/System/`, `Library/`)
- **ONLY create context files for project source code** that we develop ourselves
- **Virtual environment folders** (like `test_env/`, `venv/`, etc.) should not have context files
- **Library directories** (`node_modules/`, `__pycache__/`, etc.) should never be included
- **Binary and include directories** (`bin/`, `include/`, `.local/`) should be excluded

## Pre-commit Checklist

- [ ] All relevant context files have been read
- [ ] No functionality duplication has been verified
- [ ] Affected `.ctx.md` files have been updated
- [ ] Test files are properly placed in `tests/` directory
- [ ] **No context files created for external libraries or virtual environments**
- [ ] **Context Update Workflow completed** (confirmation → update → validate → sync)
- [ ] Metadata validation has passed
- [ ] `docs/codemap.yaml` has been updated (if needed)
- [ ] Metadata synchronization has been run
- [ ] AI model interfaces are documented (if applicable)
- [ ] Service contracts are updated (if applicable)

## Common Mistakes

### ❌ Don't Do:
- Start development without reading context
- Create functions with similar names
- Ignore existing contracts
- Forget to update context files
- **Create context files for external libraries or virtual environments**
- **Include library directories in context files**
- **Skip Context Update Workflow** (confirmation → update → validate → sync)
- **Update code without updating context files**
- **Ignore AI model interface documentation**
- **Create tight coupling between services**

### ✅ Do:
- Always read context before development
- Search for existing functionality
- Follow established patterns
- Maintain documentation currency
- **Only create context files for project source code**
- **Keep virtual environments out of context files**
- **Always complete Context Update Workflow** after development
- **Ask for user confirmation before updating context files**
- **Document AI model interfaces thoroughly**
- **Maintain clear service boundaries**

## Tools

### Main Commands:
- `make validate` - Context validation
- `make coverage` - Context coverage analysis
- `make delta` - Context delta report generation
- `make generate-cards` - Context card generation

### Validation:
```bash
# Full validation
make validate

# Coverage check
make coverage

# Generate new context cards
make generate-cards
```

## Additional Resources

- `docs/README.md` - Overview of the context file system
- `docs/intake_rules.md` - Rules for creating context cards
- `docs/service-contracts.md` - Service contracts
- `docs/function-catalog.md` - Function catalog

---

**Remember: Context files are your best friend during development, especially in AI and microservices projects!**
