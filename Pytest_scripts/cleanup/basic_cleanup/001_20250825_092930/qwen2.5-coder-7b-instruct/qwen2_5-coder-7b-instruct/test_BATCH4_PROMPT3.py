# BATCH4_PROMPT3_flask.py

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/unreliable')
def unreliable_api():
    """
    Simulates a flaky API that responds with:
    - 50% chance of success with a valid but nonsensical JSON response.
    - 30% chance of a 500 error.
    - 20% chance of success with a valid but nonsensical JSON response.
    """
    random_number = random.random()
    
    if random_number < 0.3:
        # 30% chance of returning a 500 error
        return "Internal Server Error", 500
    elif random_number < 0.5:
        # 20% chance of returning a valid but nonsensical JSON response
        return jsonify({"message": "This is a nonsensical response"})
    else:
        # 50% chance of success with a valid but nonsensical JSON response
        return jsonify({"message": "This is a successful response"})

if __name__ == "__main__":
    app.run(debug=True)

# BATCH4_PROMPT3_fastapi.py

from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

@app.get("/api/unreliable")
async def unreliable_api():
    """
    Simulates a flaky API that responds with:
    - 50% chance of success with a valid but nonsensical JSON response.
    - 30% chance of a 500 error.
    - 20% chance of success with a valid but nonsensical JSON response.
    """
    random_number = random.random()
    
    if random_number < 0.3:
        # 30% chance of returning a 500 error
        raise HTTPException(status_code=500, detail="Internal Server Error")
    elif random_number < 0.5:
        # 20% chance of returning a valid but nonsensical JSON response
        return {"message": "This is a nonsensical response"}
    else:
        # 50% chance of success with a valid but nonsensical JSON response
        return {"message": "This is a successful response"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# ===== GENERATED TESTS =====
# BATCH4_PROMPT3_flask.py

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/unreliable')
def unreliable_api():
    """
    Simulates a flaky API that responds with:
    - 50% chance of success with a valid but nonsensical JSON response.
    - 30% chance of a 500 error.
    - 20% chance of success with a valid but nonsensical JSON response.
    """
    random_number = random.random()
    
    if random_number < 0.3:
        # 30% chance of returning a 500 error
        return "Internal Server Error", 500
    elif random_number < 0.5:
        # 20% chance of returning a valid but nonsensical JSON response
        return jsonify({"message": "This is a nonsensical response"})
    else:
        # 50% chance of success with a valid but nonsensical JSON response
        return jsonify({"message": "This is a successful response"})

if __name__ == "__main__":
    app.run(debug=True)

# BATCH4_PROMPT3_fastapi.py

from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

@app.get("/api/unreliable")
async def unreliable_api():
    """
    Simulates a flaky API that responds with:
    - 50% chance of success with a valid but nonsensical JSON response.
    - 30% chance of a 500 error.
    - 20% chance of success with a valid but nonsensical JSON response.
    """
    random_number = random.random()
    
    if random_number < 0.3:
        # 30% chance of returning a 500 error
        raise HTTPException(status_code=500, detail="Internal Server Error")
    elif random_number < 0.5:
        # 20% chance of returning a valid but nonsensical JSON response
        return {"message": "This is a nonsensical response"}
    else:
        # 50% chance of success with a valid but nonsensical JSON response
        return {"message": "This is a successful response"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Tests for BATCH4_PROMPT3_flask.py

import pytest
from flask import Flask, jsonify
from unittest.mock import patch

@pytest.fixture
def client():
    app = Flask(__name__)
    
    @app.route('/api/unreliable')
    def unreliable_api():
        random_number = 0.25  # Mocked to always return a success response
        if random_number < 0.3:
            return "Internal Server Error", 500
        elif random_number < 0.5:
            return jsonify({"message": "This is a nonsensical response"})
        else:
            return jsonify({"message": "This is a successful response"})
    
    with app.test_client() as client:
        yield client

def test_unreliable_api_success(client):
    """Test the unreliable API endpoint for success."""
    response = client.get('/api/unreliable')
    assert response.status_code == 200
    assert response.json == {"message": "This is a successful response"}

def test_unreliable_api_error(client):
    """Test the unreliable API endpoint for error."""
    with patch('random.random', return_value=0.35):  # Mocked to always return an error
        response = client.get('/api/unreliable')
        assert response.status_code == 500
        assert response.data.decode() == "Internal Server Error"

# Tests for BATCH4_PROMPT3_fastapi.py

import pytest
from fastapi import FastAPI, HTTPException
from unittest.mock import patch
from httpx import AsyncClient

@pytest.fixture
async def client():
    app = FastAPI()
    
    @app.get("/api/unreliable")
    async def unreliable_api():
        random_number = 0.25  # Mocked to always return a success response
        if random_number < 0.3:
            raise HTTPException(status_code=500, detail="Internal Server Error")
        elif random_number < 0.5:
            return {"message": "This is a nonsensical response"}
        else:
            return {"message": "This is a successful response"}
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

async def test_unreliable_api_success(client):
    """Test the unreliable API endpoint for success."""
    response = await client.get('/api/unreliable')
    assert response.status_code == 200
    assert response.json() == {"message": "This is a successful response"}

async def test_unreliable_api_error(client):
    """Test the unreliable API endpoint for error."""
    with patch('random.random', return_value=0.35):  # Mocked to always return an error
        response = await client.get('/api/unreliable')
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal Server Error"}
