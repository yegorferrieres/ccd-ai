# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.1 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of CCD seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to **yegor@martlive.ai**.

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

### Required Information

- **Type of issue** (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths of source file(s) related to the vulnerability**
- **The location of the affected source code (tag/branch/commit or direct URL)**
- **Any special configuration required to reproduce the issue**
- **Step-by-step instructions to reproduce the issue**
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue, including how an attacker might exploit it**

This information will help us triage your report more quickly and efficiently.

## Disclosure Policy

When we receive a security bug report, we will assign it to a primary handler. This person will coordinate the fix and release process, involving the following steps:

1. **Confirm the problem** and determine the affected versions.
2. **Audit code** to find any similar problems.
3. **Prepare fixes** for all supported versions. These fixes will be released as new versions.

## Security Best Practices

### For Users

- **Keep CCD CLI updated** to the latest version
- **Validate all context files** before deployment
- **Use HTTPS** for all communications
- **Regularly audit** your context documentation
- **Monitor for security updates** and apply them promptly

### For Contributors

- **Follow secure coding practices** when contributing
- **Validate all inputs** and sanitize data
- **Use secure dependencies** and keep them updated
- **Test security scenarios** in your contributions
- **Report any security concerns** immediately

## Security Features

### Context Validation

CCD includes several security features to protect against common vulnerabilities:

- **Schema Validation**: All context files are validated against JSON schemas
- **Content Sanitization**: Input content is sanitized to prevent injection attacks
- **Access Control**: Context files can include access control metadata
- **Audit Logging**: All context operations are logged for security auditing

### CLI Security

The CCD CLI includes security measures:

- **Input Validation**: All command-line inputs are validated
- **File Permissions**: Respects file system permissions
- **Secure Defaults**: Secure configuration defaults
- **Error Handling**: Secure error messages that don't leak sensitive information

## Vulnerability Response Timeline

We are committed to addressing security vulnerabilities promptly:

- **Initial Response**: Within 48 hours of receiving a report
- **Triage**: Within 5 business days
- **Fix Development**: Within 30 days for critical issues
- **Public Disclosure**: Within 90 days of receiving the report

## Security Updates

Security updates are released as:

- **Patch Releases**: For critical security fixes (e.g., 1.0.1, 1.0.2)
- **Minor Releases**: For security improvements (e.g., 1.1.0, 1.2.0)
- **Major Releases**: For significant security changes (e.g., 2.0.0)

## Responsible Disclosure

We believe in responsible disclosure and will:

- **Credit reporters** in security advisories (unless requested otherwise)
- **Coordinate disclosure** with affected parties when appropriate
- **Provide clear guidance** on applying security updates
- **Maintain transparency** about our security practices

## Security Contacts

- **Security Team**: yegor@martlive.ai
- **Maintainers**: [@yegorferrieres](https://github.com/yegorferrieres)
- **PGP Key**: [Security PGP Key](https://github.com/yegorferrieres/ccd-ai/security)

## Security Acknowledgments

We would like to thank the following security researchers and organizations for their responsible disclosure of security vulnerabilities:

- [List will be populated as vulnerabilities are reported and fixed]

---

**Thank you for helping keep CCD secure!**
