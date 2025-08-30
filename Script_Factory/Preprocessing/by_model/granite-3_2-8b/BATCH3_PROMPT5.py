from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    responses = ['success', 'error', 'nonsensical']
    
    if random.random() < 0.5:
        return jsonify({'status': 'success', 'data': 'simulated data'}), 200
    
    elif random.random() < 0.3:
        return jsonify({'error': 'Internal Server Error'}), 500
    
    else:
        return jsonify(random.choice([{'a': 'b'}, {'c': 'd'}])), 200

if __name__ == "__main__":
    app.run(debug=True)