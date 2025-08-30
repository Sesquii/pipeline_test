from flask import Flask, jsonify, make_response
import random

app = Flask(__name__)

@app.route('/flaky-endpoint', methods=['GET'])
def flaky_endpoint():
    # Generate a random number between 0 and 99 to determine response type
    rand_num = random.randint(0, 99)

    if rand_num < 50:
        # 50% chance of success with valid JSON response
        return jsonify({"status": "success", "message": "Request was successful"}), 200

    elif 50 <= rand_num < 80:
        # 30% chance of a 500 error
        return make_response(jsonify({"status": "error", "message": "Internal Server Error"}), 500)

    else:
        # 20% chance of valid but nonsensical JSON response
        return jsonify({"status": "nonsensical", "data": {"random_key": "nonsensical_value"}}), 200

if __name__ == "__main__":
    app.run(debug=True)

# ===== GENERATED TESTS =====
from flask import Flask, jsonify, make_response
import random
import pytest
from typing import Dict, Tuple

app = Flask(__name__)

@app.route('/flaky-endpoint', methods=['GET'])
def flaky_endpoint():
    # Generate a random number between 0 and 99 to determine response type
    rand_num = random.randint(0, 99)

    if rand_num < 50:
        # 50% chance of success with valid JSON response
        return jsonify({"status": "success", "message": "Request was successful"}), 200

    elif 50 <= rand_num < 80:
        # 30% chance of a 500 error
        return make_response(jsonify({"status": "error", "message": "Internal Server Error"}), 500)

    else:
        # 20% chance of valid but nonsensical JSON response
        return jsonify({"status": "nonsensical", "data": {"random_key": "nonsensical_value"}}), 200

if __name__ == "__main__":
    app.run(debug=True)

# Test suite for the flaky_endpoint function
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("expected_status, expected_message", [
    (200, "Request was successful"),
    (500, "Internal Server Error"),
    (200, "nonsensical_value")
])
def test_flaky_endpoint(client: Flask, expected_status: int, expected_message: str) -> None:
    """
    Test the flaky_endpoint function with different random outcomes.
    
    Args:
        client (Flask): The Flask test client to make requests.
        expected_status (int): The expected HTTP status code.
        expected_message (str): The expected message in the JSON response.
    """
    response = client.get('/flaky-endpoint')
    assert response.status_code == expected_status
    
    if expected_status == 200:
        data: Dict[str, str] = response.json
        assert "status" in data
        assert "message" in data
        if expected_message == "nonsensical_value":
            assert data["data"]["random_key"] == "nonsensical_value"
        else:
            assert data["message"] == expected_message
    elif expected_status == 500:
        error_data: Dict[str, str] = response.json
        assert "status" in error_data
        assert "message" in error_data
        assert error_data["message"] == "Internal Server Error"

# Run the tests with pytest
# pytest -v test_flaky_endpoint.py

This test suite includes a fixture to create a Flask test client and parametrized tests to cover different outcomes of the `flaky_endpoint` function. It checks for both successful responses and errors, as well as nonsensical responses.