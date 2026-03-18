import os
from fastapi import Header, HTTPException

def verify_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    if authorization != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Invalid token")

    return authorization
