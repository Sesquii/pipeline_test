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

# ===== GENERATED TESTS =====
```python
# BATCH6_PROMPT14_{{model_name}}.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import random
from typing import Dict
import pytest
from httpx import AsyncClient

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

# Test Suite

@pytest.fixture(scope="module")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c

@pytest.mark.parametrize("payload_data, expected_status_code, expected_response",
                         [
                             ("test123", 200, {"received": "test123"}),
                             (None, 422, None),
                             ("", 422, None)
                         ])
async def test_simulate(client: AsyncClient, payload_data: str, expected_status_code: int, expected_response: Dict):
    """
    Test the /simulate endpoint with different payloads and check the response status code and content.
    """
    if payload_data is not None:
        response = await client.post("/simulate", json={"data": payload_data})
    else:
        response = await client.post("/simulate")

    assert response.status_code == expected_status_code
    if expected_response is not None:
        assert response.json() == expected_response

@pytest.mark.parametrize("payload_data, expected_exception",
                         [
                             ("test123", HTTPException),
                             (None, HTTPException),
                             ("", HTTPException)
                         ])
async def test_simulate_exception(client: AsyncClient, payload_data: str, expected_exception):
    """
    Test the /simulate endpoint with different payloads and check if it raises an exception as expected.
    """
    if payload_data is not None:
        response = await client.post("/simulate", json={"data": payload_data})
    else:
        response = await client.post("/simulate")

    assert isinstance(response.exception, expected_exception)
```

This test suite includes comprehensive test cases for the `simulate` function in the provided script. It uses pytest fixtures and parametrization to handle different scenarios and validate both successful responses and exceptions. The tests ensure that the endpoint behaves as expected under various conditions.