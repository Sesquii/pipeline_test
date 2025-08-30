from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of random quotes for successful responses
QUOTES = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do not wait to strike till the iron is hot; but make it hot by striking.",
    "The way to get started is to quit talking and begin doing.",
    "Your time is limited, don't waste it living someone else's life.",
    "If you look at what you have in life, you'll always have more."
]

# List of cryptic error messages for failed responses
ERROR_MESSAGES = [
    "Access denied: Invalid credentials",
    "Resource temporarily unavailable",
    "Request timed out: Try again later",
    "Server configuration error",
    "Unauthorized access attempt"
]

@app.route('/status', methods=['GET'])
def status():
    # Randomly decide between success and failure
    if random.random() < 0.5:
        # Success case - return a quote with 200 OK
        quote = random.choice(QUOTES)
        return jsonify({
            "status": "success",
            "message": quote
        }), 200
    else:
        # Failure case - return an error message with 403 Forbidden
        error_msg = random.choice(ERROR_MESSAGES)
        return jsonify({
            "status": "error",
            "message": error_msg
        }), 403

if __name__ == '__main__':
    app.run(debug=True)

# To run this script, save it as BATCH6_PROMPT13_{model_name}.py and execute with:
# python BATCH6_PROMPT13_{model_name}.py