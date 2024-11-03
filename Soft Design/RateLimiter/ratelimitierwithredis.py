import time
import redis

# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def is_rate_limited(user_id: str, max_tokens: int, refill_rate: int) -> bool:
    """
    Rate limit a user using a token bucket algorithm in Redis.
    
    Args:
        user_id (str): Unique identifier for the user (e.g., IP address).
        max_tokens (int): Maximum number of requests allowed per window.
        refill_rate (int): Time in seconds for the token refill interval.
    
    Returns:
        bool: True if rate-limited, False otherwise.
    """
    key = f"rate_limiter:{user_id}"
    
    # Try to fetch the token count and the last refill timestamp
    token_data = redis_client.hgetall(key)
    
    # If the bucket doesn't exist, initialize it with max tokens
    if not token_data:
        redis_client.hmset(key, {"tokens": max_tokens - 1, "last_refill": int(time.time())})
        redis_client.expire(key, refill_rate)  # Set TTL for auto-expiry after refill rate
        return False

    # Retrieve the current number of tokens and last refill time
    current_tokens = int(token_data.get(b"tokens", max_tokens))
    last_refill = int(token_data.get(b"last_refill", int(time.time())))

    # Calculate tokens to refill based on elapsed time
    current_time = int(time.time())
    elapsed_time = current_time - last_refill
    tokens_to_add = elapsed_time * (max_tokens / refill_rate)

    # Refill the tokens if needed
    new_tokens = min(current_tokens + tokens_to_add, max_tokens)

    # If there are no tokens left, rate limit the request
    if new_tokens < 1:
        return True

    # Update the Redis key with the new token count and timestamp
    redis_client.hmset(key, {"tokens": new_tokens - 1, "last_refill": current_time})
    redis_client.expire(key, refill_rate)

    return False

# Example usage
user_id = "user123"
max_tokens = 5     # Allow 5 requests per 10 seconds
refill_rate = 10   # Time window in seconds

if is_rate_limited(user_id, max_tokens, refill_rate):
    print("Rate limited! Try again later.")
else:
    print("Request allowed.")

