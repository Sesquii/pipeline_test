```python
import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_endpoint():
    rand_val = random.random() * 100
    if rand_val < 50:
        return jsonify({"status": "success", "data": "something"})
    elif rand_val < 80:
        return jsonify({"error": "Server Error"})
    else:
        return jsonify({"key": "value"})

if __name__ == "__main__":
    app.run(debug=True)

# ===== GENERATED TESTS =====
```python
import pytest
from flask import Flask, jsonify
from typing import Dict

# Original code
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_endpoint():
    rand_val = random.random() * 100
    if rand_val < 50:
        return jsonify({"status": "success", "data": "something"})
    elif rand_val < 80:
        return jsonify({"error": "Server Error"})
    else:
        return jsonify({"key": "value"})

if __name__ == "__main__":
    app.run(debug=True)

# Test code
@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client

def test_api_endpoint_success(client) -> None:
    """Test the API endpoint when it returns success."""
    response = client.get('/api')
    assert response.status_code == 200
    data: Dict[str, str] = response.json
    assert data['status'] == 'success'
    assert data['data'] == 'something'

def test_api_endpoint_error(client) -> None:
    """Test the API endpoint when it returns an error."""
    with pytest.raises(Exception):
        client.get('/api')

def test_api_endpoint_key_value(client) -> None:
    """Test the API endpoint when it returns a key-value pair."""
    response = client.get('/api')
    assert response.status_code == 200
    data: Dict[str, str] = response.json
    assert 'key' in data and 'value' in data

@pytest.mark.parametrize("status_code, expected_data", [
    (200, {"status": "success", "data": "something"}),
    (500, {"error": "Server Error"}),
    (200, {"key": "value"})
])
def test_api_endpoint_parametrized(client, status_code, expected_data) -> None:
    """Test the API endpoint with parametrized data."""
    response = client.get('/api')
    assert response.status_code == status_code
    data: Dict[str, str] = response.json
    assert all(key in data and data[key] == value for key, value in expected_data.items())
```

This test suite includes comprehensive test cases for the Flask application. It uses pytest fixtures to create a test client and parametrization to test different scenarios. The test functions include positive and negative test cases and follow PEP 8 style guidelines.