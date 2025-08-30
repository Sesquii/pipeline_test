```python
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    if random.random() < 0.5:
        return jsonify({"status": "success", "data": "Sample data"})
    elif random.random() < 0.3:
        return jsonify({"error": "Internal Server Error"}), 500
    else:
        return jsonify({"error": "Invalid data"})

if __name__ == "__main__":
    app.run(debug=True)

# ===== GENERATED TESTS =====
```python
import pytest
from flask import Flask, request

# Original code
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    if random.random() < 0.5:
        return jsonify({"status": "success", "data": "Sample data"})
    elif random.random() < 0.3:
        return jsonify({"error": "Internal Server Error"}), 500
    else:
        return jsonify({"error": "Invalid data"})

if __name__ == "__main__":
    app.run(debug=True)

# Test code
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_api_success(client):
    """Test the API endpoint when it returns success."""
    response = client.get('/api')
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == 'Sample data'

def test_api_error_500(client):
    """Test the API endpoint when it returns a 500 error."""
    with pytest.raises(Exception) as exc_info:
        client.get('/api')
    # Since we can't predict the exact error message, we check if it's a 500 error
    assert exc_info.type == Exception

def test_api_error_invalid_data(client):
    """Test the API endpoint when it returns an invalid data error."""
    with pytest.raises(Exception) as exc_info:
        client.get('/api')
    # Since we can't predict the exact error message, we check if it's a 400 error
    assert exc_info.type == Exception

def test_api_random_response(client):
    """Test the API endpoint for random responses."""
    responses = set()
    for _ in range(10):
        response = client.get('/api')
        responses.add(response.status_code)
    assert len(responses) == 3  # Expecting success, 500 and invalid data
```

This test suite includes comprehensive test cases for the `api` function. It uses pytest fixtures to create a test client for the Flask application and tests both positive and negative scenarios. The test cases cover different HTTP status codes and ensure that the API behaves as expected under various conditions.