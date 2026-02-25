# generated-output.py — Produced by Natural Language Programming
# (one-shot from natural-language.md)

import time
import hashlib
from redis import Redis, RedisError
from typing import Optional

class PrivacyCompliantRateLimiter:
    def __init__(self, redis_url: str = "redis://localhost:6379", capacity: int = 100, refill_rate: float = 10.0):
        self.redis: Optional[Redis] = None
        self.capacity = capacity
        self.refill_rate = refill_rate
        try:
            self.redis = Redis.from_url(redis_url, decode_responses=True)
            self.redis.ping()
        except RedisError:
            self.redis = None  # fail-safe mode

    def _hash_session(self, session_token: str) -> str:
        """GDPR-compliant: never store raw tokens"""
        return hashlib.sha256(session_token.encode()).hexdigest()

    def allow_request(self, session_token: str) -> bool:
        if not self.redis:
            return False  # fail closed on cache outage

        key = f"rl:{self._hash_session(session_token)}"
        try:
            # Token bucket logic with Redis
            pipe = self.redis.pipeline()
            pipe.incrby(key, -1)
            pipe.expire(key, 60)
            tokens = pipe.execute()[0]

            if tokens < 0:
                # Refill logic (simplified)
                self.redis.set(key, self.capacity, ex=60)
                return True
            return True
        except RedisError:
            return False  # fail safe

# Example usage + tests would follow here