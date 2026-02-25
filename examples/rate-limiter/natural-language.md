# Natural Language Prompt (full mental model)

Implement a token-bucket rate limiter for a healthcare SaaS API.

Must respect GDPR (no persistent user identifiers in logs or telemetry).
Prioritizes privacy over raw throughput because we are in healthcare.
Must handle 10k RPS bursts without false positives.
Fails safe (deny access) on cache/Redis outages.
Logs only hashed session tokens for compliance audits.
Users are identified by hashed session tokens only.

Target language: Python (or C/Rust if requested).
Include: full code, unit tests, documentation, and compliance telemetry.
Output format: production-ready, well-commented, ready to review.