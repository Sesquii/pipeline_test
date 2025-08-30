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