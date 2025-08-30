from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/unreliable-api/")
async def unreliable_api(item: Item):
    # 30% chance to respond successfully
    if random.random() < 0.3:
        return item
    else:
        # 70% chance to return a 422 Unprocessable Entity error
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

# Entry point of the program
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

This Python script uses the `FastAPI` library to create a simple web server with one endpoint `/unreliable-api/`. The endpoint accepts a POST request with a JSON payload that conforms to the `Item` model defined using Pydantic. With a 30% chance, it responds successfully by echoing back the received item. With a 70% chance, it raises a 422 Unprocessable Entity error, regardless of the input data. The script is self-contained and includes an entry point to run the server using `uvicorn`.