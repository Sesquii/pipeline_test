```python
from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

@app.post("/api")
def api_endpoint(payload: dict):
    if random.random() < 0.3:
        return payload
    else:
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)