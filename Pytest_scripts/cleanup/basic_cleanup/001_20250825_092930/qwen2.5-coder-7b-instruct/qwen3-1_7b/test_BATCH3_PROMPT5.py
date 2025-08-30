from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_nonsensical_json():
    """Generates a nonsensical JSON response with an arbitrary error message."""
    return {"error": ''.join(random.choices(string.ascii_letters + string.digits, k=10))}

@app.route('/api', methods=['GET'])
def api():
    if random.random() < 0.5:
        # 50% chance of success
        data = {"status": "success", "data": "some_data"}
        return jsonify(data)
    elif random.random() < 0.3:
        # 30% chance of 500 error
        return (jsonify({"error": "Internal Server Error"}), 500)
    else:
        # 20% chance of invalid JSON
        return jsonify(generate_nonsensical_json())

if __name__ == "__main__":
    app.run(debug=True)

# ===== GENERATED TESTS =====
from flask import Flask, jsonify
import random
import string
import pytest

app = Flask(__name__)

def generate_nonsensical_json():
    """Generates a nonsensical JSON response with an arbitrary error message."""
    return {"error": ''.join(random.choices(string.ascii_letters + string.digits, k=10))}

@app.route('/api', methods=['GET'])
def api():
    if random.random() < 0.5:
        # 50% chance of success
        data = {"status": "success", "data": "some_data"}
        return jsonify(data)
    elif random.random() < 0.3:
        # 30% chance of 500 error
        return (jsonify({"error": "Internal Server Error"}), 500)
    else:
        # 20% chance of invalid JSON
        return jsonify(generate_nonsensical_json())

if __name__ == "__main__":
    app.run(debug=True)

# Test suite for the Flask application

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client

def test_api_success(client):
    """Test the API endpoint when it returns success."""
    response = client.get('/api')
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert 'data' in response.json

def test_api_error_500(client):
    """Test the API endpoint when it returns a 500 error."""
    with pytest.raises(Exception) as exc_info:
        client.get('/api')
    assert exc_info.value.args[0] == (jsonify({"error": "Internal Server Error"}), 500)

def test_api_invalid_json(client):
    """Test the API endpoint when it returns invalid JSON."""
    response = client.get('/api')
    assert response.status_code == 200
    assert 'error' in response.json

@pytest.mark.parametrize("endpoint, expected_status", [
    ('/api', 200),
    ('/nonexistent', 404)
])
def test_api_endpoints(client, endpoint, expected_status):
    """Test multiple API endpoints for different status codes."""
    response = client.get(endpoint)
    assert response.status_code == expected_status

@pytest.mark.parametrize("endpoint, expected_error", [
    ('/api', 'Internal Server Error'),
    ('/nonexistent', 'Not Found')
])
def test_api_error_messages(client, endpoint, expected_error):
    """Test API error messages for different endpoints."""
    with pytest.raises(Exception) as exc_info:
        client.get(endpoint)
    assert expected_error in str(exc_info.value.args[0][1].get_json()['error'])
