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