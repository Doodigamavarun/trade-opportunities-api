from fastapi import HTTPException

request_counts = {}

def check_rate_limit(user: str):
    if user not in request_counts:
        request_counts[user] = 1
    else:
        request_counts[user] += 1

    if request_counts[user] > 5:
        raise HTTPException(status_code=429, detail="Rate limit exceeded (max 5 requests)")
