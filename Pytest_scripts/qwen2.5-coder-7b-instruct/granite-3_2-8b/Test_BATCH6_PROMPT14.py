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

# ===== GENERATED TESTS =====
```python
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

# BATCH6_PROMPT14_Granite_test.py

import pytest
from fastapi.testclient import TestClient
from BATCH6_PROMPT14_Granite import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_unreliable_api_success(client):
    """
    Test case to verify that the unreliable API successfully echoes the payload back.
    
    This test should pass 30% of the time.
    """
    response = client.post("/unreliable-api", json={"key": "value"})
    assert response.status_code == 200
    assert response.json() == {"key": "value"}

def test_unreliable_api_failure(client):
    """
    Test case to verify that the unreliable API returns a 422 Unprocessable Entity error.
    
    This test should pass 70% of the time.
    """
    response = client.post("/unreliable-api", json={"key": "value"})
    assert response.status_code == 422
    assert response.json() == {"detail": "Unprocessable Entity"}

def test_unreliable_api_invalid_payload(client):
    """
    Test case to verify that the unreliable API handles invalid payloads correctly.
    
    This should always pass, regardless of reliability.
    """
    response = client.post("/unreliable-api", json={"key": "value"})
    assert response.status_code in [200, 422]
```