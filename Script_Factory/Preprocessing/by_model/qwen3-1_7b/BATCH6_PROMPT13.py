```python
from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of sample quotes to randomly select from
quotes = [
    "The only way to do great work is to love what you do.",
    "Innovation distinguishes between a genius and a man who has knowledge.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

@app.route('/status', methods=['GET'])
def status():
    # 50% chance of returning a 200 OK with a random quote
    if random.random() < 0.5:
        return jsonify({'quote': random.choice(quotes)})
    else:
        # 50% chance of returning 403 Forbidden with cryptic error
        return jsonify({'error': 'Forbidden: Unauthorized access'})

if __name__ == '__main__':
    app.run(debug=True)