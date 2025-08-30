from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    # Simulate API responses based on probability
    response_options = [
        {'success': True, 'data': {'message': 'Request succeeded'}},  # 50% chance of success
        {'success': False, 'code': 500, 'data': None}                 # 30% chance of 500 error
    ]
    
    # Add a 20% chance of a valid but nonsensical JSON response
    if random.random() < 0.2:
        response_options.append({'success': True, 'data': {'message': 'This is a nonsensical response'}})
    
    # Randomly choose one of the responses
    selected_response = random.choice(response_options)
    
    # Return the selected response
    if selected_response['success']:
        return jsonify(selected_response['data']), 200
    else:
        return '', selected_response['code']

if __name__ == "__main__":
    app.run(debug=True, port=5000)