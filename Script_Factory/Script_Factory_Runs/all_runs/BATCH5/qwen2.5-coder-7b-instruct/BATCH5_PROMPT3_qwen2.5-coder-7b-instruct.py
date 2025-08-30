from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/unreliable', methods=['GET'])
def unreliable_api():
    # Determine the response based on random chance
    outcome = random.random()
    
    if outcome < 0.5:
        return "API is working as expected", 200
    elif outcome < 0.8:
        return jsonify({"error": "Internal server error"}), 500
    else:
        return jsonify({"message": "This is a nonsensical response"}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Explanation:
- The script uses Flask to create a simple web server.
- The `/api/unreliable` endpoint simulates an unreliable API with the specified behavior:
  - 50% chance of returning "API is working as expected" with status code 200.
  - 30% chance of returning a JSON object indicating an internal server error with status code 500.
  - 20% chance of returning a nonsensical JSON object with status code 200.
- The `if __name__ == "__main__":` block runs the Flask app when the script is executed directly.