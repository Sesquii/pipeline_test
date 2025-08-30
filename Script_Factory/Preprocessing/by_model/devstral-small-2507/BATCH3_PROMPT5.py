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