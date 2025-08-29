# CCD for AI Examples

This directory contains practical examples and implementations of the CCD for AI methodology in real-world projects.

## Overview

The examples demonstrate how to implement CCD in different types of projects, from simple applications to complex microservices architectures. Each example provides:

- Complete project structure with CCD implementation
- Sample context files and schemas
- Development rules and engineering logs
- Architecture decision records (ADRs)
- Practical implementation patterns

## Available Examples

### MartLive AI Video Assistant

**Location**: `martlive/`

**Description**: A comprehensive example of CCD implementation in a production AI video processing system.

**Key Features**:
- Microservices architecture (Go, Python)
- Real-time video processing pipeline
- AI/ML integration with context documentation
- WebSocket-based communication
- Kubernetes deployment configuration

**Architecture**:
- **Edge Gateway Service** (Go): API gateway and request routing
- **ASR Service** (Python): Audio-to-text conversion
- **Coach LLM Service** (Python): AI-powered video analysis
- **Web Demo** (JavaScript): User interface and real-time updates

**CCD Implementation**:
- Repository-level `CODEMAP.yaml` with module mapping
- Module-level `INDEX.yaml` files with I/O contracts
- Context cards for all source files
- Development rules specific to AI/microservices
- Engineering log documenting key decisions
- Architecture decision records (ADRs)

**Learning Outcomes**:
- How to structure CCD for microservices
- Context documentation for AI/ML components
- Real-time system context management
- Multi-language project organization
- Production deployment considerations

## Getting Started

### 1. Choose an Example

Start with the example that best matches your project type:
- **MartLive**: For microservices, AI/ML, or real-time systems
- **Future examples**: Will cover web applications, mobile apps, data pipelines

### 2. Study the Structure

Examine the example's directory structure:
```
example-name/
├── codemap.sample.yaml          # Repository overview
├── index.sample.yaml            # Module mapping
├── context-cards.sample/        # File-level context
├── development-rules.sample.md  # Project-specific rules
├── engineering-log.sample.md    # Engineering decisions
├── decisions.sample/            # Architecture decisions
└── README.md                    # Example overview
```

### 3. Understand the Patterns

Key CCD patterns demonstrated:
- **Three-tier architecture**: Repository → Module → File
- **Context generation**: Automated and manual context creation
- **Quality gates**: Schema validation and content standards
- **Integration**: CI/CD, monitoring, and maintenance

### 4. Adapt to Your Project

Use the examples as templates:
- Copy and modify context file structures
- Adapt development rules to your team
- Customize schemas for your domain
- Implement similar CI/CD workflows

## Example Categories

### By Project Type
- **Microservices**: MartLive (Go, Python)
- **Web Applications**: Coming soon
- **Mobile Apps**: Coming soon
- **Data Pipelines**: Coming soon
- **Desktop Applications**: Coming soon

### By Technology Stack
- **Go**: Edge Gateway service
- **Python**: AI/ML services
- **JavaScript/TypeScript**: Web interfaces
- **YAML**: Configuration and schemas
- **Kubernetes**: Deployment and orchestration

### By Domain
- **AI/ML**: Video processing, natural language
- **Real-time Systems**: WebSocket communication
- **Media Processing**: Audio, video, text
- **Enterprise**: Microservices, monitoring

## Best Practices

### Context File Organization
- Use consistent naming conventions
- Group related files in modules
- Maintain clear dependency relationships
- Regular updates and validation

### Quality Assurance
- Validate against JSON schemas
- Check content completeness
- Verify cross-references
- Monitor context health metrics

### Team Collaboration
- Establish review processes
- Document decision rationale
- Maintain engineering logs
- Regular context audits

## Contributing Examples

### Adding New Examples

1. **Create Directory Structure**:
   ```
   new-example/
   ├── codemap.sample.yaml
   ├── index.sample.yaml
   ├── context-cards.sample/
   ├── development-rules.sample.md
   ├── engineering-log.sample.md
   ├── decisions.sample/
   └── README.md
   ```

2. **Follow Standards**:
   - Use sample file naming convention
   - Include comprehensive context coverage
   - Document architecture decisions
   - Provide clear learning objectives

3. **Update This README**:
   - Add to available examples
   - Describe key features
   - List learning outcomes
   - Categorize appropriately

### Example Requirements

**Minimum Content**:
- Repository overview (CODEMAP.yaml)
- Module mapping (INDEX.yaml)
- Context cards for key files
- Development rules
- Engineering log entries
- Architecture decisions

**Quality Standards**:
- Clear and concise documentation
- Practical implementation patterns
- Real-world scenarios
- Learning value for users

## Troubleshooting

### Common Issues

**Context Validation Errors**:
- Check schema compliance
- Verify required fields
- Validate file references
- Run context health checks

**Missing Context Files**:
- Generate context for new files
- Update module mappings
- Check file organization
- Validate dependencies

**Integration Problems**:
- Verify CI/CD configuration
- Check tool installation
- Validate workflow triggers
- Monitor build logs

### Getting Help

- Check the main CCD documentation
- Review similar examples
- Examine error logs and reports
- Consult the community

## Future Development

### Planned Examples

**Phase 1** (Current):
- MartLive AI Video Assistant ✅

**Phase 2** (Next):
- Web Application (React/Node.js)
- Mobile App (React Native)
- Data Pipeline (Python/Apache Airflow)

**Phase 3** (Future):
- Desktop Application (Electron)
- IoT System (Python/Arduino)
- Blockchain Application (Solidity/Web3)

### Example Enhancements

- Interactive tutorials
- Video walkthroughs
- Performance benchmarks
- Migration guides
- Integration examples

## Related Documentation

- [CCD Protocol](../03-protocol.md)
- [Architecture Overview](../05-architecture.md)
- [CI/CD Integration](../06-ci-cd-integration.md)
- [Development Rules](../DEVELOPMENT_RULES.md)
- [Templates](../templates/)
- [Schemas](../schemas/)

## Support

For questions about examples or CCD implementation:
- Review the main documentation
- Check example-specific README files
- Examine context files and schemas
- Consult the engineering logs
- Join the community discussions

---

*Examples are living documentation that evolve with the CCD methodology. Regular updates ensure they remain relevant and valuable for users.*
