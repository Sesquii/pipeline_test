from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_endpoint():
    # 50% chance of success (returning a valid JSON)
    if random.random() < 0.5:
        return jsonify({"message": "Success", "data": "Some meaningful data"}), 200

    # 30% chance of a 500 error
    elif random.random() < 0.3:
        return jsonify({"error": "Internal Server Error"}), 500

    # 20% chance of nonsensical JSON response
    else:
        return jsonify({"message": "Something went wrong", "data": random.choice(["banana", "apple", "carrot"])}), 200

if __name__ == "__main__":
    app.run(debug=True)