# BATCH6_PROMPT14_Granite.py
from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

@app.post("/unreliable-api")
async def unreliable_api(payload: dict):
    """
    Endpoint to simulate an unreliable API.

    With 30% chance, it successfully echoes the payload back.
    With 70% chance, it returns a 422 Unprocessable Entity error.
    
    Request Example: 
    POST /unreliable-api
    Content-Type: application/json

    {
        "key": "value"
    }
    """
    # Generate random number to simulate the unreliability
    if random.random() < 0.3:  # 30% chance for success
        return payload
    else:  # 70% chance for failure
        raise HTTPException(status_code=422, detail="Unprocessable Entity")