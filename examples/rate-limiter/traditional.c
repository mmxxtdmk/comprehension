// traditional.c — Rate limiter written in C (mnemonic / portable-assembly style)
// This is what "programming speed" looked like before NL

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// TODO: GDPR compliance - no persistent user IDs
// TODO: Privacy over speed
// TODO: Handle 10k RPS bursts
// TODO: Fail safe on Redis outage
// TODO: Log only hashed session tokens

typedef struct {
    int tokens;
    time_t last_refill;
} TokenBucket;

TokenBucket* create_bucket(int capacity) {
    TokenBucket* b = malloc(sizeof(TokenBucket));
    b->tokens = capacity;
    b->last_refill = time(NULL);
    return b;
}

int allow_request(TokenBucket* b) {
    // TODO: real token bucket math + Redis integration
    // TODO: compliance telemetry
    return 1; // placeholder
}

int main() {
    printf("Traditional C rate-limiter stub\n");
    // Pages of pointer arithmetic would go here in a real low-level version
    return 0;
}