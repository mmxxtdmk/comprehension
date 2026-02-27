Build a GDPR-compliant token-bucket rate limiter for a healthcare SaaS API.

Full mental model:
- Domain: Healthcare data — strict privacy, audit logs required.
- Intent: Prevent abuse while allowing burst traffic (e.g., 10 req/min base, burst up to 50).
- Trade-offs: Memory efficiency vs. accuracy; use Redis for prod.
- Constraints: No PII leakage; handle distributed systems.

Output:
- Python class with methods.
- Unit tests.
- Deployment notes with GDPR compliance checklist.