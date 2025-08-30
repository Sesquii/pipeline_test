# BATCH4_PROMPT3_Granite.py

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    responses = ['valid_response']

    # 50% chance of success
    if random.random() > 0.5:
        return jsonify({'message': 'Success!'}), 200

    # 30% chance of 500 error
    elif random.random() > 0.7:
        return jsonify({'error': 'Internal Server Error'}), 500

    # 20% chance of nonsensical valid JSON response
    else:
        responses = [
            {'message': random.choice(['Inconceivable!', 'Foobar', 'Bazquux'])},
            {'error': random.choice(['Nonsense Exception', 'Quux Error'])}
        ]
    
    return jsonify(random.choice(responses)), 200

if __name__ == "__main__":
    app.run(debug=True)