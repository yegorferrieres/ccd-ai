# CCD for AI Schemas

This directory contains JSON schemas for validating CCD for AI context files and ensuring consistency across the methodology implementation.

## Overview

The schemas define the structure and validation rules for all CCD artifacts:
- **CODEMAP.yaml**: Repository-level context and module mapping
- **INDEX.yaml**: Module-level file mapping and I/O contracts
- **Context Cards (.ctx.md)**: File-level documentation with metadata

These schemas serve as quality gates, ensuring that all CCD files meet the required standards and maintain consistency across projects.

## Available Schemas

### 1. CODEMAP Schema

**File**: `codemap.schema.json`

**Purpose**: Validates repository-level `CODEMAP.yaml` files

**Validates**:
- Project metadata (name, description, version)
- Module definitions and relationships
- Dependency mappings
- Technology stack information
- Repository structure

**Key Fields**:
- `project`: Basic project information
- `modules`: List of modules with metadata
- `dependencies`: Module dependency relationships
- `metadata`: Additional project metadata

### 2. INDEX Schema

**File**: `index.schema.json`

**Purpose**: Validates module-level `INDEX.yaml` files

**Validates**:
- Module metadata and description
- File definitions within the module
- I/O contracts and data flow
- API specifications
- Module relationships

**Key Fields**:
- `module`: Module information
- `files`: List of files with metadata
- `contracts`: Input/output specifications
- `apis`: API definitions
- `metadata`: Module-specific metadata

### 3. Context Card Schema

**File**: `context-card.schema.json`

**Purpose**: Validates individual context card (`.ctx.md`) files

**Validates**:
- Front-matter metadata
- Content structure and sections
- File references and dependencies
- Tags and categorization
- Review and maintenance information

**Key Fields**:
- `title`: Context card title
- `owner`: Responsible team member
- `updated_at`: Last update timestamp
- `systems_impacted`: Affected systems
- `file_path`: Source file location
- `file_type`: File type classification
- `dependencies`: Related files
- `tags`: Categorization tags

## Usage

### Schema Validation

#### Command Line

```bash
# Validate CODEMAP.yaml
ccd validate --schema schemas/codemap.schema.json --file CODEMAP.yaml

# Validate INDEX.yaml
ccd validate --schema schemas/index.schema.json --file modules/service/INDEX.yaml

# Validate context card
ccd validate --schema schemas/context-card.schema.json --file src/main.go.ctx.md
```

#### Programmatic

```python
import json
import jsonschema
from pathlib import Path

# Load schema
with open('schemas/context-card.schema.json') as f:
    schema = json.load(f)

# Load context file
with open('src/main.go.ctx.md') as f:
    content = f.read()

# Extract front-matter (YAML)
# ... extract YAML from markdown ...

# Validate
jsonschema.validate(instance=yaml_data, schema=schema)
```

### CI/CD Integration

The schemas are automatically used in CI/CD pipelines:

```yaml
# .github/workflows/validate-context.yml
- name: Validate Context Files
  run: |
    ccd validate-all \
      --schemas docs/schemas/ \
      --project-root .
```

### IDE Integration

Configure your IDE to use these schemas:

**VS Code**:
```json
{
  "yaml.schemas": {
    "docs/schemas/codemap.schema.json": "CODEMAP.yaml",
    "docs/schemas/index.schema.json": "**/INDEX.yaml"
  }
}
```

**PyCharm/IntelliJ**:
- File → Settings → Languages & Frameworks → Schemas and DTDs
- Add schema files and associate with file patterns

## Validation Process

### 1. Schema Loading

The validation process loads the appropriate schema based on file type:
- `CODEMAP.yaml` → `codemap.schema.json`
- `INDEX.yaml` → `index.schema.json`
- `*.ctx.md` → `context-card.schema.json`

### 2. Content Extraction

For context cards, the front-matter YAML is extracted from the markdown file and validated against the schema.

### 3. Validation Rules

Each schema enforces:
- **Required fields**: Must be present and non-empty
- **Data types**: String, number, boolean, array, object
- **Format validation**: Dates, file paths, URLs
- **Value constraints**: Enums, ranges, patterns
- **Cross-references**: File existence, dependency validation

### 4. Error Reporting

Validation errors include:
- Field location and path
- Expected vs. actual values
- Missing required fields
- Type mismatches
- Format violations

## Quality Gates

### Schema Compliance

All CCD files must pass schema validation:
- ✅ Valid structure and format
- ✅ Required fields present
- ✅ Data types correct
- ✅ Cross-references valid

### Content Standards

Schemas enforce content quality:
- Minimum content length
- Required documentation sections
- Consistent metadata format
- Proper categorization

### Integration Checks

Schemas validate system integration:
- File path consistency
- Module dependency mapping
- Cross-reference validity
- API contract compliance

## Schema Evolution

### Versioning

Schemas are versioned to handle evolution:
- **Major versions**: Breaking changes
- **Minor versions**: New optional fields
- **Patch versions**: Bug fixes and clarifications

### Migration

When schemas change:
1. **Deprecation notice**: Old fields marked as deprecated
2. **Migration guide**: Instructions for updating files
3. **Backward compatibility**: Support for old format during transition
4. **Validation updates**: New validation rules applied

### Breaking Changes

Breaking changes require:
- **Major version bump**: Schema version increment
- **Migration script**: Automated file updates
- **Documentation updates**: New format examples
- **Team notification**: Clear communication of changes

## Custom Schemas

### Project-Specific Schemas

Create custom schemas for project needs:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Custom Context Schema",
  "type": "object",
  "properties": {
    "custom_field": {
      "type": "string",
      "description": "Project-specific field"
    }
  },
  "required": ["custom_field"]
}
```

### Schema Extension

Extend existing schemas:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "allOf": [
    { "$ref": "context-card.schema.json" },
    {
      "properties": {
        "project_specific": {
          "type": "string"
        }
      }
    }
  ]
}
```

## Best Practices

### Schema Design

- **Clear descriptions**: Document all fields and constraints
- **Consistent naming**: Use consistent field naming conventions
- **Reasonable defaults**: Provide sensible default values
- **Error messages**: Include helpful validation error messages

### Validation Strategy

- **Early validation**: Validate during development, not just CI/CD
- **Progressive validation**: Start with basic structure, add complexity
- **Performance consideration**: Balance validation thoroughness with speed
- **User feedback**: Provide clear error messages and suggestions

### Maintenance

- **Regular review**: Periodically review and update schemas
- **Community feedback**: Incorporate user suggestions and issues
- **Documentation updates**: Keep schema documentation current
- **Testing**: Test schemas with various file types and edge cases

## Troubleshooting

### Common Validation Errors

**Missing Required Fields**:
```
Error: 'title' is a required property
```
**Solution**: Add the missing required field to your file.

**Type Mismatch**:
```
Error: 'updated_at' is not of a type(s) string
```
**Solution**: Ensure the field has the correct data type.

**Invalid Format**:
```
Error: 'file_path' does not match pattern '^[^/]+(/[^/]+)*$'
```
**Solution**: Use valid file path format.

### Schema Issues

**Schema Not Found**:
- Verify schema file exists
- Check file path in validation command
- Ensure schema file is committed to repository

**Schema Syntax Error**:
- Validate JSON syntax of schema file
- Check for missing commas or brackets
- Verify schema follows JSON Schema specification

**Validation Performance**:
- Large files may be slow to validate
- Consider breaking large files into smaller ones
- Use selective validation for specific file types

## Related Documentation

- [CCD Protocol](../03-protocol.md)
- [Architecture Overview](../05-architecture.md)
- [CI/CD Integration](../06-ci-cd-integration.md)
- [Development Rules](../DEVELOPMENT_RULES.md)
- [Templates](../templates/)
- [Examples](../examples/)

## Support

For schema-related questions:
- Check validation error messages
- Review schema field descriptions
- Examine example files
- Consult the main documentation
- Join community discussions

---

*Schemas ensure consistency and quality across all CCD implementations. Regular updates and community feedback keep them relevant and useful.*
