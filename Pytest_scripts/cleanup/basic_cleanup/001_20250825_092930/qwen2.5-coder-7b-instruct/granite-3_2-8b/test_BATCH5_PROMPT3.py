from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    response = None

    # 50% chance of success
    if random.random() < 0.5:
        response = {"message": "Success", "data": "Some data"}
    
    # 30% chance of 500 error
    elif random.random() < 0.3:
        return jsonify({"error": "Internal Server Error"}), 500

    # 20% chance of nonsensical JSON response
    else:
        response = {"message": "Success", "data": random.choice(["Nonsense1", "Nonsense2", "Nonsense3"])}
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

# ===== GENERATED TESTS =====
from flask import Flask, jsonify
import random
from typing import Dict, Any

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    response = None

    # 50% chance of success
    if random.random() < 0.5:
        response = {"message": "Success", "data": "Some data"}
    
    # 30% chance of 500 error
    elif random.random() < 0.3:
        return jsonify({"error": "Internal Server Error"}), 500

    # 20% chance of nonsensical JSON response
    else:
        response = {"message": "Success", "data": random.choice(["Nonsense1", "Nonsense2", "Nonsense3"])}
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

import pytest
from flask import Flask, Response

# Fixture to create a test client for the Flask application
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_success(client):
    """Test the API endpoint when it returns success."""
    response: Response = client.get('/api')
    assert response.status_code == 200
    data: Dict[str, Any] = response.json
    assert data['message'] == 'Success'
    assert data['data'] == 'Some data'

def test_api_error(client):
    """Test the API endpoint when it returns an error."""
    with pytest.raises(Response) as exc_info:
        client.get('/api')
    response: Response = exc_info.value
    assert response.status_code == 500
    data: Dict[str, Any] = response.json
    assert data['error'] == 'Internal Server Error'

def test_api_nonsensical_data(client):
    """Test the API endpoint when it returns nonsensical data."""
    response: Response = client.get('/api')
    assert response.status_code == 200
    data: Dict[str, Any] = response.json
    assert data['message'] == 'Success'
    assert data['data'] in ['Nonsense1', 'Nonsense2', 'Nonsense3']

# Test the random nature of the API responses by running multiple tests
@pytest.mark.parametrize("expected_status_code, expected_message, expected_data", [
    (200, "Success", "Some data"),
    (500, "Internal Server Error", None),
    (200, "Success", "Nonsense1")
])
def test_api_randomness(client, expected_status_code: int, expected_message: str, expected_data: Any):
    """Test the API endpoint for random responses."""
    response: Response = client.get('/api')
    assert response.status_code == expected_status_code
    data: Dict[str, Any] = response.json
    if expected_status_code == 200:
        assert data['message'] == expected_message
        if expected_data is not None:
            assert data['data'] == expected_data

This test suite covers all public functions and classes in the provided Flask application. It includes both positive and negative test cases, uses pytest fixtures and parametrization where appropriate, adds type hints to test functions, includes proper docstrings and comments, follows PEP 8 style guidelines, and adds a clear separator between the original code and test code.