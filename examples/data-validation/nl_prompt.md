You are building a GDPR-compliant user registration endpoint for a telehealth SaaS platform.

Full mental model:
- Domain: Healthcare — PHI must never leak; every validation failure is auditable for compliance.
- Intent: Accept clean data, reject junk early, return precise user-facing messages without exposing sensitive details.
- Threat model: Malicious input (SQLi, XSS, timing attacks), PII in error logs, distributed validation failures.
- Constraints: Python 3.11+, Pydantic v2 only, no external services in core path, full test coverage, zero raw PHI in logs.
- Priorities: Privacy & auditability first, then reliability, then developer ergonomics.

Output required:
- Complete Pydantic v2 model(s) with custom validators
- Comprehensive pytest suite (including edge cases and threat simulations)
- Compliance checklist + deployment notes
- User-facing error messages that never leak sensitive data

Generate the complete, ready-to-merge implementation with full comprehension baked in.