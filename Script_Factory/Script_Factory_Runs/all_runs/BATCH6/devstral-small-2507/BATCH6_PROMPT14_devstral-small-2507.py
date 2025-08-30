# BATCH6_PROMPT14_{{model_name}}.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import random

app = FastAPI()

class Payload(BaseModel):
    data: str

@app.post("/simulate")
async def simulate(payload: Payload):
    # Generate a random number between 0 and 99
    rand_num = random.randint(0, 99)

    # With 30% chance (numbers 0-29), respond successfully
    if rand_num < 30:
        return {"received": payload.data}

    # With 70% chance (numbers 30-99), return 422 Unprocessable Entity error
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Unprocessable Entity"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)