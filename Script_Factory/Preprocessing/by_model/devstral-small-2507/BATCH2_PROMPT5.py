from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/flaky-endpoint', methods=['GET'])
def flaky_endpoint():
    # Generate a random number between 0 and 99 to determine response type
    rand_num = random.randint(0, 99)

    if rand_num < 50:
        # 50% chance of success with valid JSON response
        return jsonify({"status": "success", "data": {"message": "Request processed successfully"}}), 200

    elif 50 <= rand_num < 80:
        # 30% chance of a 500 error
        return jsonify({"error": "Internal Server Error"}), 500

    else:
        # 20% chance of a valid but nonsensical JSON response
        return jsonify({"status": "nonsense", "data": {"message": "This is nonsense data"}}), 200

if __name__ == "__main__":
    app.run(debug=True)