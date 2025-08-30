from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def unreliable_api():
    # Randomly decide the response type
    response_type = random.choices(['success', 'error', 'nonsensical'], [0.5, 0.3, 0.2])[0]
    
    if response_type == 'success':
        return jsonify({'message': 'Request succeeded!'})
    elif response_type == 'error':
        return jsonify({'error': 'Internal Server Error'}), 500
    else:
        return jsonify({'nonsensical_data': 'This is a nonsensical JSON response!'})

if __name__ == "__main__":
    app.run(debug=True)