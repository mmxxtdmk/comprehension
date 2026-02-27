# Threat-Model-First Template

A reusable pattern for Natural Language Programming in security-sensitive features.

## Structure
1. **Feature Description**: [Describe the core functionality in natural language.]
2. **Threat Model**: [List potential attacks, vulnerabilities, and risks.]
3. **Priorities & Trade-offs**: [Rank security vs. performance vs. usability.]
4. **Constraints**: [Legal (e.g., GDPR), technical (e.g., no external deps).]
5. **Output Request**: [Specify code language, tests, docs format.]

## Example Usage
Feature Description: API rate limiter for healthcare SaaS.
Threat Model: DDoS, token theft, side-channel timing attacks.
Priorities: Security > Reliability > Speed.
Constraints: GDPR audit logs; Python 3.10+.
Output: Class impl, pytest tests, README snippet.

Paste into LLM and iterate.

## Why This Pattern?
Forces comprehension of risks upfront, embedding them in context for LLM to generate robust code — unlike traditional programming where threats are afterthoughts.