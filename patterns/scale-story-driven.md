# Scale-Story-Driven Pattern

This pattern guides prompts to embed narratives of system growth, ensuring code anticipates scaling from 10 users to 10 million.

## Template
You are building [SYSTEM_DESCRIPTION].
First, the scale story:

Day 1: [INITIAL_SCALE, e.g., 10 users, single server].
Month 6: [MEDIUM_SCALE, e.g., 1k users, load-balanced].
Year 2: [LARGE_SCALE, e.g., 10M users, global distribution, 99.99% uptime].

Core functionality: [MECHANICAL_SPEC].
Comprehension layers:

Performance: [METRICS, e.g., <100ms latency at peak].
Reliability: [FAILOVER, e.g., redundant DBs].
Evolution: [FUTURE_FEATURES, e.g., ML integration].

Output: [LANGUAGE] code with inline comments tying back to the scale story.

## Usage Example
Tie to `../examples/data-validation/`: Add scale story for telehealth app growing from clinic to national network, ensuring validation handles increasing data volume without privacy leaks.

Paste into LLM, refine, and iterate in the notebook.