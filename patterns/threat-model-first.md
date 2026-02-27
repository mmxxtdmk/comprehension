# Threat-Model-First Template

**A core Natural Language Programming pattern for security-sensitive domains.**

This template forces full comprehension of risks, priorities, and constraints **upfront** — before any code is generated.

## The Template

```text
Build [feature] for [domain].

Threat Model:
- [detailed list of threats, attack vectors, side-channels, failure modes]

Priorities (ranked):
- 1. [e.g. Privacy & Compliance]
- 2. [Reliability]
- 3. [Performance]

Constraints:
- Compliance (GDPR, HIPAA, SOC2…)
- Technical
- Non-functional

Success looks like:
- [metrics + user/business impact]

Output requested:
- Production-ready code in [language]
- Tests (unit + integration)
- Documentation + compliance notes
```

## Example Usage (Rate Limiter)

```text
Build a token-bucket rate limiter for a healthcare SaaS API.

Threat Model:
- DDoS and burst attacks
- Token theft / replay
- Side-channel timing attacks
- Cache poisoning and Redis outages

Priorities (ranked):
- 1. Privacy (GDPR compliance)
- 2. Reliability (fail safe)
- 3. Performance

Constraints:
- No persistent user identifiers in logs or telemetry
- Fail closed on cache outage
- Handle 10k RPS bursts without false positives

Success looks like:
- Zero false positives during normal load
- Full auditability for compliance reviews

Output requested:
- Python implementation
- Comprehensive tests
- Deployment and compliance documentation
```

## Why This Pattern Matters

Traditional programming treats threat modeling as an afterthought (added later in comments or separate docs).
Natural Language Programming makes threat comprehension first-class input. The model then operationalizes it into robust, secure code from the first generation.

Copy → adapt → iterate in the notebook.