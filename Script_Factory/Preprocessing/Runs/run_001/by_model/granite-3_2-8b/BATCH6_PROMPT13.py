# BATCH6_PROMPT13_Granite.py

from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Life is 10% what happens to us and 90% how we react to it.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "The best way to predict the future is to create it."
]

@app.route('/status', methods=['GET'])
def status():
    if random.random() > 0.5:  # 50% chance
        quote = random.choice(quotes)
        return jsonify({"message": f"Random Quote: {quote}"}), 200
    else:  # 50% chance
        error_msg = "An internal server error occurred."
        return jsonify({"error": error_msg}), 403

if __name__ == "__main__":
    app.run(debug=True)